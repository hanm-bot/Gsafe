#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gộp ba lớp kiểm thành MỘT phiếu trình người duyệt (lớp L5).

Đường ống: L1 cổng pháp lý (hook) → L2 agent → L3 giọng văn → L4 .docx → L5 phiếu này.

Script KHÔNG tự phê duyệt và KHÔNG tự ghi Sổ Cái. Nó dựng phiếu và in sẵn câu
lệnh ghi sổ để NGƯỜI duyệt chạy sau khi đã đọc — đúng nguyên tắc HITL: máy
chuẩn bị hồ sơ, người bấm nút cuối.

Exit: 0 = đủ điều kiện trình duyệt · 2 = có lỗi nặng, chưa trình được.

Dùng:
    python phieu_xuat_ban.py VANBAN.md [--docx VANBAN.docx] [-o PHIEU-XUAT-BAN.md]
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CHAM_VAN_PHONG = SCRIPT_DIR / "cham_van_phong.py"
KIEM_DOCX = SCRIPT_DIR / "kiem_xuat_ban_docx.py"

LOAI_RA_NGOAI = "Gate 3"
LOAI_NOI_BO = "Gate 2"


def chay(lenh):
    ket = subprocess.run(lenh, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return ket.returncode, (ket.stdout or "") + (ket.stderr or "")


def kiem_phap_ly(van_ban):
    """Đối chiếu lớp L1: QĐ thì phải có file .nguon.md hoặc nhãn thoát.

    Hook đã chặn lúc GHI; ở đây chỉ báo lại trạng thái cho người duyệt thấy,
    vì văn bản có thể đã được ghi từ phiên khác.
    """
    noi_dung = van_ban.read_text(encoding="utf-8", errors="replace")
    la_qd = ("QUYẾT ĐỊNH" in noi_dung[:400].upper()
             or "QĐ-" in noi_dung[:400]
             or van_ban.name.upper().startswith("QD"))
    if not la_qd:
        return True, "Không phải Quyết định — lớp truy vết Căn cứ không áp dụng."

    nguon = van_ban.with_suffix("").with_suffix(".nguon.md")
    nguon_don = van_ban.parent / (van_ban.stem + ".nguon.md")
    if nguon.exists() or nguon_don.exists():
        return True, f"Có file nguồn đi kèm: `{nguon_don.name}`"

    co_nhan = any(d in noi_dung for d in ("DA-DOI-CHIEU-NGUON", "chưa đối chiếu", "chưa kiểm chứng", "⚠️"))
    if co_nhan:
        return True, "Không có file .nguon.md nhưng Căn cứ đã gắn nhãn chưa đối chiếu — người duyệt tự cân."
    return False, f"Là Quyết định, có Căn cứ, nhưng THIẾU `{nguon_don.name}` và không có nhãn thoát."


def main():
    for luong in (sys.stdout, sys.stderr):
        if hasattr(luong, "reconfigure"):
            luong.reconfigure(encoding="utf-8", errors="replace")

    p = argparse.ArgumentParser(description="Dựng phiếu trình duyệt trước khi xuất bản")
    p.add_argument("van_ban", help="File .md nguồn của văn bản")
    p.add_argument("--docx", help="Bản .docx đã sinh (nếu có)")
    p.add_argument("--ra-ngoai", action="store_true", help="Văn bản gửi ra ngoài -> Gate 3 (Mr. Hà)")
    p.add_argument("-o", "--dau-ra", help="Nơi ghi phiếu")
    ts = p.parse_args()

    van_ban = Path(ts.van_ban)
    if not van_ban.exists():
        print(f"Không thấy file: {van_ban}", file=sys.stderr)
        return 2

    phap_ly_dat, phap_ly_ly_do = kiem_phap_ly(van_ban)

    ma_vp, ra_vp = chay([sys.executable, str(CHAM_VAN_PHONG), str(van_ban)])
    dong_vp = [d for d in ra_vp.splitlines() if d.startswith("## Kết quả")]
    tom_tat_vp = dong_vp[0].replace("## Kết quả: ", "") if dong_vp else "không chấm được"
    vp_co_loi_phai = "#3 Câu bị động" in ra_vp

    docx_dat, tom_tat_docx = None, "Chưa sinh bản .docx"
    if ts.docx:
        ma_docx, ra_docx = chay([sys.executable, str(KIEM_DOCX), ts.docx])
        docx_dat = (ma_docx == 0)
        nang = [d.strip() for d in ra_docx.splitlines() if "[NẶNG]" in d]
        tom_tat_docx = "Đạt phần máy kiểm được" if docx_dat else f"{len(nang)} lỗi nặng: " + "; ".join(nang[:3])

    chan = (not phap_ly_dat) or (docx_dat is False)
    gate = LOAI_RA_NGOAI if ts.ra_ngoai else LOAI_NOI_BO

    d = []
    d.append("# PHIẾU TRÌNH DUYỆT XUẤT BẢN")
    d.append("")
    d.append(f"- Văn bản: `{van_ban.name}`")
    d.append(f"- Bản .docx: `{Path(ts.docx).name}`" if ts.docx else "- Bản .docx: chưa sinh")
    d.append(f"- Dựng phiếu lúc: {datetime.now().strftime('%H:%M %d/%m/%Y')}")
    d.append(f"- Cổng duyệt: **{gate}**" + (" — riêng Mr. Hà" if ts.ra_ngoai else ""))
    d.append("")
    d.append("## Ba lớp kiểm")
    d.append("")
    d.append("| Lớp | Cơ chế | Kết quả |")
    d.append("|---|---|---|")
    d.append(f"| L1 Pháp lý — truy vết Căn cứ | Hook chặn cứng khi ghi | {'✅' if phap_ly_dat else '❌'} {phap_ly_ly_do} |")
    d.append(f"| L3 Giọng văn | Cảnh báo, không chặn | {'⚠️' if vp_co_loi_phai else '✅'} {tom_tat_vp} |")
    d.append(f"| L4 Định dạng .docx | Chặn cứng lỗi nặng | {'—' if docx_dat is None else ('✅' if docx_dat else '❌')} {tom_tat_docx} |")
    d.append("")

    if chan:
        d.append("## ❌ CHƯA ĐỦ ĐIỀU KIỆN TRÌNH")
        d.append("")
        if not phap_ly_dat:
            d.append(f"- Lớp pháp lý chưa qua: {phap_ly_ly_do}")
        if docx_dat is False:
            d.append(f"- Bản .docx còn lỗi nặng: {tom_tat_docx}")
        d.append("")
        d.append("Sửa xong chạy lại phiếu này.")
    else:
        d.append("## ✅ ĐỦ ĐIỀU KIỆN TRÌNH DUYỆT")
        d.append("")
        if vp_co_loi_phai:
            d.append("Lưu ý: còn cảnh báo giọng văn ở tiêu chí **bắt buộc #3**. Máy không chặn —")
            d.append("người duyệt đọc phiếu văn phong rồi quyết giữ hay sửa.")
            d.append("")
        d.append("### Máy KHÔNG kiểm được — người duyệt phải tự đọc")
        d.append("")
        d.append("- Thể thức nghiệp vụ (số hiệu, nơi nhận, khối ký) đúng mẫu chưa")
        d.append("- Nội dung có đúng nghiệp vụ và đúng thẩm quyền không")
        d.append("- Tiêu chí #7: văn bản có tô hồng trạng thái thật không")
        d.append("")
        d.append("### Sau khi duyệt — ghi Sổ Cái rồi mới xuất bản")
        d.append("")
        d.append("```bash")
        d.append(f'python .agents/scripts/ghi-log-hitl.py --append --gate "{gate}" \\')
        d.append('  --channel "Claude Code CLI" --actor "<người duyệt>" \\')
        d.append(f'  --target "{van_ban.name}" --command "<câu duyệt nguyên văn>"')
        d.append("```")

    phieu = "\n".join(d) + "\n"

    if ts.dau_ra:
        dich = Path(ts.dau_ra)
        if dich.exists():
            print(f"Đã có {dich} — không ghi đè (luật cứng #3).\n", file=sys.stderr)
            print(phieu)
        else:
            dich.write_text(phieu, encoding="utf-8")
            print(f"Đã ghi phiếu: {dich}")
    else:
        print(phieu)

    return 2 if chan else 0


if __name__ == "__main__":
    sys.exit(main())
