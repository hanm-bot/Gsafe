#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chấm giọng văn bản hành chính theo rubric "Văn phong người thật".

CẢNH BÁO, KHÔNG CHẶN. Luôn thoát 0. Rubric ghi rõ giọng văn là chủ quan, do
người soát quyết (chốt phiên 22/09/2026) — script chỉ chỉ ra chỗ đáng nhìn lại.

Danh sách từ "mùi AI" KHÔNG viết trong file này: đọc thẳng từ
references/rubric-van-phong-nguoi.md để rubric là nguồn luật duy nhất.

Dùng:
    python cham_van_phong.py VANBAN.md [-o PHIEU-VAN-PHONG.md] [--rubric ĐƯỜNG_DẪN]
"""

import argparse
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RUBRIC_MAC_DINH = SCRIPT_DIR.parent / "references" / "rubric-van-phong-nguoi.md"

TIEU_DE_MUC_TU_MUI_AI = "Danh sách từ/cụm"
BAT_BUOC = {3, 7}


def doc_tu_mui_ai(duong_dan_rubric):
    """Rút danh sách từ mùi AI từ mục tương ứng trong rubric.

    Trả về (danh_sách_từ, cảnh_báo). Chỉ lấy các cụm trong dấu backtick của
    mục đó, bỏ phần ví dụ mở bài dạng câu dài và các cụm có "…" (không khớp
    nguyên văn được).
    """
    if not duong_dan_rubric.exists():
        return [], f"Không thấy rubric tại {duong_dan_rubric}"

    dong = duong_dan_rubric.read_text(encoding="utf-8").splitlines()
    trong_muc = False
    than_muc = []
    for d in dong:
        if d.startswith("#"):
            if TIEU_DE_MUC_TU_MUI_AI in d:
                trong_muc = True
                continue
            if trong_muc:
                break
        if trong_muc:
            than_muc.append(d)

    if not than_muc:
        return [], f"Không thấy mục '{TIEU_DE_MUC_TU_MUI_AI}' trong rubric"

    tu = []
    for cum in re.findall(r"`([^`]+)`", "\n".join(than_muc)):
        cum = cum.strip()
        if "…" in cum or "..." in cum:
            continue  # cụm có chỗ trống, không khớp nguyên văn được
        if cum:
            tu.append(cum)
    return tu, None


def quet_tu_mui_ai(dong_van_ban, danh_sach_tu):
    phat_hien = []
    for so_dong, noi_dung in dong_van_ban:
        for tu in danh_sach_tu:
            for khop in re.finditer(re.escape(tu), noi_dung, re.IGNORECASE):
                phat_hien.append((so_dong, tu, noi_dung.strip(), khop.start()))
    return phat_hien


def quet_bi_dong(dong_van_ban):
    """Tiêu chí #3 (bắt buộc): câu chủ động, chủ thể rõ.

    Bắt cụm bị động giấu chủ thể: "sẽ được ...", "đã được ..." mà không có
    "bởi <ai>" theo sau trong cùng câu.
    """
    phat_hien = []
    # Tiếng Việt nêu chủ thể ngay sau "được": "đang được hai Bên thương thảo".
    chu_the = (r"(hai Bên|các Bên|Bên Bán|Bên Mua|Bên A|Bên B|SHT|Quý Công ty|Chủ đầu tư|Nhà thầu"
               r"|ngân hàng|đối tác|khách hàng|nhà cung cấp|cơ quan|công ty|tổ chức|đơn vị"
               r"|hệ thống|bộ phận|phòng ban|người dùng|thu ngân|kế toán)")
    mau = re.compile(r"\b(sẽ được|đang được|đã được)\s+(\w+)", re.IGNORECASE)
    for so_dong, noi_dung in dong_van_ban:
        for khop in mau.finditer(noi_dung):
            duoi = noi_dung[khop.end() - len(khop.group(2)):][:90]
            if re.match(r"\s*" + chu_the, duoi, re.IGNORECASE):
                continue  # chủ thể đứng ngay sau "được" — không giấu
            if re.search(r"\bbởi\s+\S", duoi, re.IGNORECASE):
                continue  # "bởi <ai đó>" — luôn có nêu chủ thể
            phat_hien.append((so_dong, khop.group(0), noi_dung.strip()))
    return phat_hien


def quet_so_trang_trong(dong_van_ban):
    """Tiêu chí #4 (nên): số trang trọng viết kèm chữ trong ngoặc, nhất quán."""
    don_vi = r"(tài khoản|ngày làm việc|ngày|tháng|bên|bản|điều|khoản|người|lần)"
    co_ngoac = re.compile(r"\((\d{2})\)")
    tran_so = re.compile(r"(?<![\d(])\b(\d{1,2})\s+" + don_vi, re.IGNORECASE)

    # "ngày 09 tháng 09 năm 2026" là thể thức ngày tháng chuẩn — không phải số lộn xộn.
    ngay_thang = re.compile(r"ngày\s+\d{1,2}\s+tháng\s+\d{1,2}\s+năm\s+\d{4}", re.IGNORECASE)

    kieu_co_ngoac = 0
    tran = []
    for so_dong, noi_dung in dong_van_ban:
        kieu_co_ngoac += len(co_ngoac.findall(noi_dung))
        vung_ngay_thang = [k.span() for k in ngay_thang.finditer(noi_dung)]
        for khop in tran_so.finditer(noi_dung):
            if any(dau <= khop.start() < cuoi for dau, cuoi in vung_ngay_thang):
                continue
            tran.append((so_dong, khop.group(0).strip(), noi_dung.strip()))

    # Chỉ báo khi văn bản ĐÃ dùng kiểu có ngoặc ở chỗ khác -> tức là không nhất quán.
    if kieu_co_ngoac == 0:
        return []
    return tran


def quet_ket_cut(dong_van_ban):
    """Tiêu chí #6 (nên): kết bằng thiện chí, không cụt."""
    co_noi_dung = [(n, d) for n, d in dong_van_ban if d.strip()]
    if not co_noi_dung:
        return []
    duoi = co_noi_dung[-6:]
    for so_dong, noi_dung in duoi:
        if re.fullmatch(r"\**\s*Trân trọng\.?\s*\**[.!]?", noi_dung.strip(), re.IGNORECASE):
            truoc = [d.strip() for _, d in co_noi_dung if d.strip()]
            vi_tri = truoc.index(noi_dung.strip())
            cau_truoc = truoc[vi_tri - 1] if vi_tri > 0 else ""
            if len(cau_truoc) < 60:
                return [(so_dong, "Trân trọng.", "kết cụt, không có câu thiện chí/lợi ích chung đi trước")]
    return []


def quet_mo_bai(dong_van_ban):
    """Tiêu chí #1 (nên): mở bằng bối cảnh + ghi nhận quan hệ."""
    mau = re.compile(r"(trong bối cảnh|trong thời đại|kính thưa quý vị)", re.IGNORECASE)
    phat_hien = []
    for so_dong, noi_dung in dong_van_ban[:40]:
        khop = mau.search(noi_dung)
        if khop:
            phat_hien.append((so_dong, khop.group(0), noi_dung.strip()))
    return phat_hien


def dung_phieu(ten_file, ket_qua, danh_sach_tu, canh_bao_rubric):
    d = []
    d.append("# PHIẾU CHẤM VĂN PHONG")
    d.append("")
    d.append(f"- Văn bản: `{ten_file}`")
    d.append("- Rubric: `sht-nen-tang-kiem-chung/references/rubric-van-phong-nguoi.md`")
    d.append(f"- Số cụm \"mùi AI\" đang canh: {len(danh_sach_tu)}")
    d.append("- **Phiếu này KHÔNG chặn xuất bản.** Giọng văn do người soát quyết.")
    if canh_bao_rubric:
        d.append(f"- ⚠️ {canh_bao_rubric}")
    d.append("")

    # Rubric: các cụm này chỉ sai khi "rải trang trí", đúng khi có nội dung thật đỡ.
    # Máy không phân biệt được -> liệt kê để người soát xác nhận, KHÔNG tính là lỗi.
    can_nguoi_xac_nhan = ket_qua.pop("tu_mui_ai", [])

    tong = sum(len(v) for v in ket_qua.values())
    if tong == 0 and can_nguoi_xac_nhan:
        d.append("## Kết quả: máy không bắt được lỗi nào")
        d.append("")
        d.append(f"Nhưng có {len(can_nguoi_xac_nhan)} cụm thuộc danh sách \"mùi AI\" — **người soát xác nhận**")
        d.append("xem có nội dung thật đỡ không, hay chỉ rải trang trí:")
        d.append("")
        d.append("| Dòng | Cụm | Trích |")
        d.append("|---|---|---|")
        for m in can_nguoi_xac_nhan[:25]:
            trich = str(m[2]).replace("|", "\\|")
            trich = trich[:90] + "…" if len(trich) > 90 else trich
            d.append(f"| {m[0]} | `{m[1]}` | {trich} |")
        d.append("")
        d.append("## Máy không chấm được — người soát đọc")
        d.append("")
        d.append("- **#2** Đóng khung yêu cầu bằng lý lẽ nghĩa vụ, không ra lệnh trần")
        d.append("- **#5** Xưng hô & kính ngữ đúng độ theo vai người ký–người nhận")
        d.append("- **#7 (bắt buộc)** Trung thực về trạng thái — có tô hồng hay không, người đọc mới thấy")
        return "\n".join(d) + "\n"

    if tong == 0:
        d.append("## Kết quả: không thấy dấu hiệu giọng máy nào bằng máy quét")
        d.append("")
        d.append("Các tiêu chí định tính (#2 lý lẽ nghĩa vụ, #5 xưng hô, #7 trung thực trạng thái)")
        d.append("máy không chấm được — vẫn cần người soát đọc.")
        return "\n".join(d) + "\n"

    d.append(f"## Kết quả: {tong} chỗ đáng nhìn lại")
    d.append("")

    nhan = {
        "tu_mui_ai": ('Từ/cụm "mùi AI"', "nên", "Bỏ, hoặc thay bằng nội dung thật đỡ câu"),
        "bi_dong": ("#3 Câu bị động, giấu chủ thể", "**phải**", "Nêu rõ ai làm: SHT / Bên Bán / hai Bên"),
        "mo_bai": ("#1 Mở bài kiểu sáo", "nên", "Mở bằng bối cảnh thật + ghi nhận quan hệ"),
        "so_trang_trong": ("#4 Số không nhất quán", "nên", 'Viết kèm chữ trong ngoặc: "hai (02) tài khoản"'),
        "ket_cut": ("#6 Kết cụt", "nên", "Kết bằng thiện chí + lợi ích chung của hai bên"),
    }

    for khoa, cac_dong in ket_qua.items():
        if not cac_dong:
            continue
        ten, muc, cach_sua = nhan[khoa]
        d.append(f"### {ten} — mức: {muc}")
        d.append("")
        d.append("| Dòng | Chỗ vướng | Trích |")
        d.append("|---|---|---|")
        for muc_phat_hien in cac_dong[:25]:
            so_dong = muc_phat_hien[0]
            cho = str(muc_phat_hien[1]).replace("|", "\\|")
            trich = str(muc_phat_hien[2]).replace("|", "\\|")
            if len(trich) > 90:
                trich = trich[:90] + "…"
            d.append(f"| {so_dong} | `{cho}` | {trich} |")
        if len(cac_dong) > 25:
            d.append(f"| … | còn {len(cac_dong) - 25} chỗ nữa | |")
        d.append("")
        d.append(f"→ Hướng sửa: {cach_sua}")
        d.append("")

    if can_nguoi_xac_nhan:
        d.append('### Cụm "mùi AI" — người soát xác nhận, máy không kết luận')
        d.append("")
        d.append("Rubric: các cụm này chỉ sai khi rải trang trí, đúng khi có nội dung thật đỡ.")
        d.append("")
        d.append("| Dòng | Cụm | Trích |")
        d.append("|---|---|---|")
        for m in can_nguoi_xac_nhan[:25]:
            trich = str(m[2]).replace("|", "\\|")
            trich = trich[:90] + "…" if len(trich) > 90 else trich
            d.append(f"| {m[0]} | `{m[1]}` | {trich} |")
        d.append("")

    d.append("## Máy không chấm được — người soát đọc")
    d.append("")
    d.append("- **#2** Đóng khung yêu cầu bằng lý lẽ nghĩa vụ, không ra lệnh trần")
    d.append("- **#5** Xưng hô & kính ngữ đúng độ theo vai người ký–người nhận")
    d.append("- **#7 (bắt buộc)** Trung thực về trạng thái — phần truy vết do hook luật #1/#2 canh,")
    d.append("  nhưng chuyện *có tô hồng hay không* thì người đọc mới thấy.")
    return "\n".join(d) + "\n"


def main():
    # Windows mặc định cp1252, in tiếng Việt ra stdout sẽ vỡ UnicodeEncodeError.
    for luong in (sys.stdout, sys.stderr):
        if hasattr(luong, "reconfigure"):
            luong.reconfigure(encoding="utf-8", errors="replace")

    p = argparse.ArgumentParser(description="Chấm giọng văn bản theo rubric văn phong người thật")
    p.add_argument("van_ban", help="File .md cần chấm")
    p.add_argument("-o", "--dau-ra", help="Nơi ghi phiếu (mặc định: in ra màn hình)")
    p.add_argument("--rubric", default=str(RUBRIC_MAC_DINH), help="Đường dẫn rubric")
    tham_so = p.parse_args()

    nguon = Path(tham_so.van_ban)
    if not nguon.exists():
        print(f"Không thấy file: {nguon}", file=sys.stderr)
        return 0  # vẫn không chặn

    danh_sach_tu, canh_bao = doc_tu_mui_ai(Path(tham_so.rubric))
    dong_van_ban = list(enumerate(nguon.read_text(encoding="utf-8").splitlines(), start=1))

    ket_qua = {
        "bi_dong": quet_bi_dong(dong_van_ban),
        "tu_mui_ai": quet_tu_mui_ai(dong_van_ban, danh_sach_tu),
        "mo_bai": quet_mo_bai(dong_van_ban),
        "so_trang_trong": quet_so_trang_trong(dong_van_ban),
        "ket_cut": quet_ket_cut(dong_van_ban),
    }

    phieu = dung_phieu(nguon.name, ket_qua, danh_sach_tu, canh_bao)

    if tham_so.dau_ra:
        dich = Path(tham_so.dau_ra)
        if dich.exists():
            print(f"Đã có {dich} — không ghi đè (luật cứng #3). In ra màn hình thay thế.\n", file=sys.stderr)
            print(phieu)
        else:
            dich.write_text(phieu, encoding="utf-8")
            print(f"Đã ghi phiếu: {dich}")
    else:
        print(phieu)

    return 0  # LUÔN 0 — cảnh báo, không chặn


if __name__ == "__main__":
    sys.exit(main())
