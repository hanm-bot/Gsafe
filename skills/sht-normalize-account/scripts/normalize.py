"""
sht-normalize-account · chuẩn hóa entity khách hàng trong SHT Sales Pipeline.

NGUYÊN TẮC LÕI (rút ra từ lỗi thực tế):
  1) Khóa account = MÃ CÓ CẤU TRÚC trong `ma` (Project ID), KHÔNG phải tên `kh` free-text.
     `kh` do người nhập tay -> 1 chi nhánh có hàng trăm biến thể -> tách khống account.
  2) Parse `ma` thất bại -> gom vào 1 BUCKET "chưa xác định", KHÔNG fallback về gộp theo `kh`
     (fallback này làm phồng lại số entity).
  3) Chuẩn hóa xong PHẢI tự kiểm: số CN phải <= danh mục CN thật (Vietinbank ~155).

CẤU TRÚC MÃ DỰ ÁN: [Năm 2 hoặc 4 số][<BANK>][Mã CN][STT 3 số]
  vd 26VTBTN007 = 2026 · VTB · TN(Thái Nguyên) · 007
Các biến thể ĐÃ xử lý: năm 4 số (2024VTB...), dấu cách sau prefix (VTB AMC),
dấu tiếng Việt trong mã (VTBĐĐ=Đống Đa), rác/ngoặc đầu chuỗi, mô tả đằng sau mã.

Dùng:
  from normalize import account_key, bank_key, branch_code, clean_label
  bank, code, key = account_key(ma, kh)
Chạy self-test:  python3 normalize.py
"""
import re, unicodedata

# ---- khử dấu (giữ Đ/đ -> D/d vì NFD không tách được) ----
def deacc(s: str) -> str:
    if not s: return ""
    s = s.replace("Đ", "D").replace("đ", "d")
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")

def _low(s: str) -> str:
    return deacc(s).lower()

# ---- phân loại ngân hàng: LUẬT CỤ THỂ TRƯỚC LUẬT CHUNG ----
# (Saigonbank đặt trước Vietinbank vì "cong thuong" trùng "Sài Gòn Công Thương")
BANK_RULES = [
    ("Saigonbank",  ["sai gon cong thuong", "saigonbank"]),
    ("Vietinbank",  ["vietinbank", "vtb", "cong thuong", "ctg"]),
    ("VPBank",      ["vpbank", "vp bank", "thinh vuong"]),
    ("VIB",         ["vib", "quoc te"]),
    ("BIDV",        ["bidv", "dau tu va phat trien"]),
    ("Vietcombank", ["vietcombank", "vcb", "ngoai thuong"]),
    ("Agribank",    ["agribank", "nong nghiep"]),
    ("MB Bank",     ["mbbank", "mb bank", "quan doi"]),
    ("ACB",         ["acb", "a chau"]),
    ("Techcombank", ["techcombank", "tcb", "ky thuong"]),
    ("Sacombank",   ["sacombank", "stb", "sai gon thuong tin"]),
    ("SHB", ["shb"]), ("TPBank", ["tpbank"]), ("HDBank", ["hdbank"]),
    ("MSB", ["msb", "hang hai"]), ("SeABank", ["seabank"]),
    ("OCB", ["ocb", "phuong dong"]), ("Eximbank", ["eximbank", "eib"]),
    ("Nam A Bank", ["nam a"]), ("BAC A BANK", ["bac a"]),
    ("LPBank", ["lpbank", "lienviet", "buu dien"]),
]

def bank_key(kh: str) -> str:
    """Phân loại ngân hàng mẹ từ tên khách hàng. Trả 'KHÁC' nếu phi ngân hàng."""
    s = _low(kh)
    for name, keys in BANK_RULES:
        if any(k in s for k in keys):
            return name
    return "KHÁC"

# ---- tách mã chi nhánh Vietinbank từ `ma` ----
def branch_code(ma: str, prefix: str = "VTB") -> str | None:
    """
    Trả 'VTB<Mã CN>' nếu `ma` khớp cấu trúc, ngược lại None.
    Đổi `prefix` để dùng cho bank khác có cùng quy ước mã.
    """
    if not ma:
        return None
    s = deacc(ma).upper()
    s = re.sub(r"\(.*?\)", " ", s)          # bỏ ghi chú (LẬP LẦN 2)...
    s = re.sub(r"^[^0-9A-Z]+", "", s)       # bỏ rác/ngoặc kép đầu chuỗi
    s = re.sub(r"^(20\d{2}|\d{2})", "", s)  # bỏ năm 4 số hoặc 2 số
    m = re.search(prefix + r"\s*([A-Z0-9]+)", s)   # cho phép dấu cách sau prefix
    if not m:
        return None
    code = re.sub(r"\d{3}$", "", m.group(1)) or m.group(1)  # bỏ STT 3 số cuối
    return (prefix + code) if code else None

UNASSIGNED = "__UNK__"

def account_key(ma: str, kh: str):
    """
    Trả (bank, code, key):
      - Vietinbank có mã: bank='Vietinbank', code='VTB..', key='VTB::VTB..'
      - Vietinbank thiếu mã: code='—', key='VTB::__UNK__'  (BUCKET, không tách theo kh)
      - Bank/KH khác: code='', key='<bank>||<kh chuẩn hóa nhẹ>'
    """
    code = branch_code(ma)
    if code:
        return "Vietinbank", code, "VTB::" + code
    bank = bank_key(kh)
    if bank == "Vietinbank":
        return "Vietinbank", "—", "VTB::" + UNASSIGNED
    return bank, "", bank + "||" + _norm_kh(kh)

def _norm_kh(kh: str) -> str:
    s = _low(kh); s = re.sub(r"[^a-z0-9 ]", " ", s)
    for w in ["ngan hang", "tmcp", "co phan", "cong thuong", "viet nam", "chi nhanh", "cn"]:
        s = s.replace(w, " ")
    return re.sub(r"\s+", " ", s).strip() or "__x__"

def clean_label(kh: str) -> str:
    """Tên hiển thị gọn: rút prefix pháp lý dài về 'Vietinbank'."""
    if not kh: return "(trống)"
    l = re.sub(r"Ng[aâ]n h[aà]ng.*?C[oô]ng [Tt]h[uươ]ng Vi[eệ]t Nam\s*-?\s*",
               "Vietinbank ", kh, flags=re.I)
    return re.sub(r"\s+", " ", l).strip(" -")[:46]

def validate_branch_count(n_codes: int, official: int = 155):
    """Tự kiểm: số mã CN không được vượt xa danh mục thật. Trả (ok, message)."""
    if n_codes <= official:
        return True, f"OK: {n_codes} mã CN ≤ {official} CN chính thức."
    delta = n_codes - official
    lvl = "CHÚ Ý" if delta <= official * 0.25 else "CẢNH BÁO"
    return (delta <= official * 0.25), (
        f"{lvl}: {n_codes} mã CN > {official} chính thức (dôi {delta}). "
        f"Kỳ vọng dôi ít do Hội sở/PGD/công ty con/typo; nếu dôi nhiều → nghi chuẩn hóa lỗi.")

# --------------------------- SELF-TEST (offline) ---------------------------
if __name__ == "__main__":
    CASES = [
        ("26VTBTN007", None, "VTBTN"),
        ("2024VTBBHN002 khai trương PGD Ngọc", None, "VTBBHN"),   # năm 4 số + mô tả
        ("24VTB TayQNH001", None, "VTBTAYQNH"),                    # dấu cách sau VTB
        ("25VTBĐĐ007 - Hệ thống âm thanh", None, "VTBDD"),         # tiếng Việt trong mã
        ("25VTB AMC003", None, "VTBAMC"),                          # công ty con
        ("26VTBCN3004", None, "VTBCN3"),                           # CN số
        ("26VTBCN12005", None, "VTBCN12"),
        ("VTBDHN002 Màn Led P3", None, "VTBDHN"),                  # thiếu năm
        ("Đổ mực máy in", "Vietinbank CN X", "—"),                 # ma là mô tả -> bucket
        ("25saigonbank001", "Ngân hàng TMCP Sài Gòn Công Thương", None),  # KHÔNG nhầm Vietinbank
    ]
    ok = 0
    for ma, kh, want in CASES:
        bank, code, key = account_key(ma, kh)
        got = code if code else None
        if ma == "25saigonbank001":
            passed = (bank == "Saigonbank")
            info = f"bank={bank}"
        else:
            passed = (got == want) or (want == "—" and code == "—")
            info = f"code={code}"
        ok += passed
        print(("✓" if passed else "✗"), f"{ma[:34]:<34} -> {info}")
    print(f"\n{ok}/{len(CASES)} pass")
    print(validate_branch_count(186)[1])
