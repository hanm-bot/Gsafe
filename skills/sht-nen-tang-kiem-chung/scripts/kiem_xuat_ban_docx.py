#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm file .docx trước khi phát hành — lỗi đo được bằng máy.

CHẶN CỨNG (thoát 2) khi có lỗi NẶNG, vì đây là lỗi khách quan đo được, khác
với giọng văn (chủ quan, chỉ cảnh báo — xem cham_van_phong.py).

Kiểm 5 nhóm:
  1. Heading nhảy cấp   (H1 -> H3 không qua H2)
  2. Bảng vỡ            (số ô các hàng không khớp hàng tiêu đề)
  3. Font tiếng Việt    (thiếu w:eastAsia -> Word thay font, vỡ dấu)
  4. Trang trống        (ngắt trang liền nhau / ngắt trang ở cuối file)
  5. Watermark          (báo còn/mất để người soát đối chiếu bản gốc)

Dùng:
    python kiem_xuat_ban_docx.py VANBAN.docx [--watermark-bat-buoc]
"""

import argparse
import sys
import zipfile
from pathlib import Path

try:
    from docx import Document
except ImportError:
    print("Thiếu python-docx. Cài: pip install python-docx", file=sys.stderr)
    sys.exit(3)

NS_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NANG = "NẶNG"
NHE = "NHẸ"


def cap_heading(doan):
    ten = (doan.style.name or "") if doan.style is not None else ""
    if ten.startswith("Heading "):
        duoi = ten.split("Heading ", 1)[1].strip()
        if duoi.isdigit():
            return int(duoi)
    return None


def kiem_heading(tai_lieu):
    loi = []
    cap_truoc = 0
    for chi_so, doan in enumerate(tai_lieu.paragraphs, start=1):
        cap = cap_heading(doan)
        if cap is None:
            continue
        if cap_truoc and cap > cap_truoc + 1:
            loi.append((NANG, f"Heading nhảy cấp H{cap_truoc} → H{cap} tại đoạn {chi_so}: "
                              f"\"{doan.text.strip()[:60]}\""))
        cap_truoc = cap
    return loi


def kiem_bang(tai_lieu):
    loi = []
    for so_bang, bang in enumerate(tai_lieu.tables, start=1):
        if not bang.rows:
            loi.append((NANG, f"Bảng {so_bang}: không có hàng nào"))
            continue
        so_o_tieu_de = len(bang.rows[0].cells)
        for so_hang, hang in enumerate(bang.rows[1:], start=2):
            if len(hang.cells) != so_o_tieu_de:
                loi.append((NANG, f"Bảng {so_bang} hàng {so_hang}: {len(hang.cells)} ô, "
                                  f"hàng tiêu đề có {so_o_tieu_de} ô"))
    return loi


def kiem_font_tieng_viet(duong_dan):
    """Thiếu w:eastAsia thì Word tự thay font, dấu tiếng Việt vỡ."""
    with zipfile.ZipFile(duong_dan) as z:
        ten = z.namelist()
        than = z.read("word/document.xml").decode("utf-8", errors="replace")
        kieu = z.read("word/styles.xml").decode("utf-8", errors="replace") if "word/styles.xml" in ten else ""
    if "w:eastAsia" in than or "w:eastAsia" in kieu:
        return []
    return [(NANG, "Không thấy khai báo w:eastAsia — Word có thể thay font và làm vỡ dấu tiếng Việt")]


def kiem_trang_trong(tai_lieu):
    loi = []
    truoc_la_ngat = False
    co_noi_dung_tu_lan_ngat = False
    for chi_so, doan in enumerate(tai_lieu.paragraphs, start=1):
        la_ngat = "w:br" in doan._p.xml and 'w:type="page"' in doan._p.xml
        if la_ngat:
            if truoc_la_ngat and not co_noi_dung_tu_lan_ngat:
                loi.append((NANG, f"Hai lần ngắt trang liền nhau, không có nội dung ở giữa (đoạn {chi_so}) "
                                  f"— sinh ra trang trống"))
            truoc_la_ngat = True
            co_noi_dung_tu_lan_ngat = False
            continue
        if doan.text.strip():
            co_noi_dung_tu_lan_ngat = True

    if truoc_la_ngat and not co_noi_dung_tu_lan_ngat:
        loi.append((NANG, "Ngắt trang ở cuối tài liệu, sau đó không có nội dung — sinh trang trống cuối"))
    return loi


def kiem_watermark(duong_dan, bat_buoc):
    with zipfile.ZipFile(duong_dan) as z:
        ten = z.namelist()
        header = [t for t in ten if t.startswith("word/header")]
        co_watermark = False
        for h in header:
            noi = z.read(h).decode("utf-8", errors="replace")
            if "WordArt" in noi or "PowerPlusWaterMarkObject" in noi or "watermark" in noi.lower():
                co_watermark = True
                break
        anh_header = [t for t in ten if t.startswith("word/media/")]

    if co_watermark:
        return [(NHE, f"Có watermark trong {len(header)} file header — đối chiếu bản gốc xem đúng trang chưa")]
    if bat_buoc:
        return [(NANG, "Bản gốc yêu cầu watermark nhưng file này KHÔNG có watermark trong header")]
    return [(NHE, f"Không thấy watermark (file có {len(anh_header)} ảnh nhúng) — "
                  "nếu bản gốc có watermark thì đã mất")]


def main():
    for luong in (sys.stdout, sys.stderr):
        if hasattr(luong, "reconfigure"):
            luong.reconfigure(encoding="utf-8", errors="replace")

    p = argparse.ArgumentParser(description="Kiểm .docx trước khi phát hành")
    p.add_argument("docx", help="File .docx cần kiểm")
    p.add_argument("--watermark-bat-buoc", action="store_true",
                   help="Bản gốc có watermark — thiếu là lỗi NẶNG")
    tham_so = p.parse_args()

    duong_dan = Path(tham_so.docx)
    if not duong_dan.exists():
        print(f"Không thấy file: {duong_dan}", file=sys.stderr)
        return 3

    tai_lieu = Document(str(duong_dan))
    loi = []
    loi += kiem_heading(tai_lieu)
    loi += kiem_bang(tai_lieu)
    loi += kiem_font_tieng_viet(duong_dan)
    loi += kiem_trang_trong(tai_lieu)
    loi += kiem_watermark(duong_dan, tham_so.watermark_bat_buoc)

    nang = [m for m in loi if m[0] == NANG]
    nhe = [m for m in loi if m[0] == NHE]

    print(f"KIỂM XUẤT BẢN: {duong_dan.name}")
    print(f"  Đoạn: {len(tai_lieu.paragraphs)} · Bảng: {len(tai_lieu.tables)}")
    print()

    for muc, mo_ta in nang:
        print(f"  [{muc}] {mo_ta}")
    for muc, mo_ta in nhe:
        print(f"  [{muc}] {mo_ta}")

    print()
    if nang:
        print(f"❌ CHẶN PHÁT HÀNH — {len(nang)} lỗi nặng phải sửa trước.")
        return 2
    print(f"✅ Đạt phần máy kiểm được ({len(nhe)} ghi chú cần người soát đối chiếu).")
    print("   Lưu ý: máy không kiểm được thể thức nghiệp vụ và giọng văn.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
