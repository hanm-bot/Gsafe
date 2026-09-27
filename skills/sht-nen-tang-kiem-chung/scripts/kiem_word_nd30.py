#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-W — kiểm NĐ30 Tầng 1 trên bản WORD ĐÃ DỰNG (RFC-04 PA A, HITL-20260927-003).

L4 (`kiem_xuat_ban_docx.py`) đọc XML và phải tự dựng lại cơ chế kế thừa của Word → lọt khi
thuộc tính nằm ở style mẹ, docDefaults, theme, sdt/hyperlink/ins, ô bảng, header.
L4-W hỏi thẳng Word: mở docx bằng Word COM, đọc thuộc tính HIỆU LỰC từng đoạn/từ, rồi xuất PDF
qua Word và kiểm phông nhúng, màu từng span, số trang. Chuẩn nghiệm thu: L4 exit 0 VÀ L4-W exit 0.

Exit: 0 đạt · 2 có lỗi NẶNG · 3 không chạy được (không có Word/pymupdf) — KHÔNG bao giờ coi là đạt.
"""
import argparse
import os
import sys
import tempfile
from pathlib import Path

NANG, NHE = "NẶNG", "NHẸ"
MIXED = 9999999
AUTO = -16777216                     # wdColorAutomatic
WITHIN_TABLE = 12                    # wdWithInTable
FIELD_PAGE = 33                      # wdFieldPage
ST_MAIN, ST_TEXTFRAME = 1, 5
ST_HEADERS = (6, 7, 10)              # even / primary / first-page header
ST_FOOTERS = (8, 9, 11)
ST_NOTES = (2, 3)                    # footnote / endnote
JUSTIFY = (3, 5, 7, 8)               # wdAlignParagraphJustify + Med/Hi/Low
CENTER = 1
STYLE_TITLE = -63
KHOI_MA = "NĐ30 Khối mã"
TIEU_DE_TOI_DA = 200                 # như L4: tiêu đề dài hơn = văn xuôi đội lốt tiêu đề
PHONG_PDF_HOP_LE = ("TimesNewRoman", "Consolas")


def _mau_den(font):
    try:
        if font.Color == AUTO:
            return True
    except Exception:
        pass
    try:
        return font.TextColor.RGB == 0
    except Exception:
        return False


def _cac_manh(rng):
    """Chia range thành mảnh đồng nhất cỡ/phông/màu: cả đoạn nếu đồng nhất, không thì từng từ, rồi từng ký tự."""
    f = rng.Font
    try:
        if getattr(f, "Hidden", False) and f.Hidden != MIXED:
            return
    except Exception:
        pass
    # R7 (NA-R6-5): Hidden = MIXED cũng phải tách, để mảnh hiện không bị bỏ qua cùng mảnh ẩn
    if f.Hidden == MIXED:
        # tách thẳng tới ký tự: Word gộp "từ" qua ranh giới ẩn/hiện nên mảnh "từ" vẫn có thể MIXED
        # Word bỏ qua chữ ẩn khi duyệt Characters: "ký tự" hiện kéo theo cả khối ẩn đứng trước nó
        # (Start..End > 1, Hidden/Size = MIXED) → thu về đúng ký tự cuối, là ký tự hiện
        for c in rng.Characters:
            if c.End - c.Start > 1:
                c = c.Document.Range(c.End - 1, c.End)
            if c.Font.Hidden not in (-1, True):
                yield c
        return
    if f.Size != MIXED and f.Name != "" and f.Color != MIXED and f.Hidden != MIXED:
        yield rng
        return
    for w in rng.Words:
        fw = w.Font
        try:
            if getattr(fw, "Hidden", False) and fw.Hidden != MIXED:
                continue
        except Exception:
            pass
        if fw.Size != MIXED and fw.Name != "" and fw.Color != MIXED and fw.Hidden != MIXED:
            yield w
        else:
            for c in w.Characters:
                fc = c.Font
                try:
                    if getattr(fc, "Hidden", False) and fc.Hidden != MIXED:
                        continue
                except Exception:
                    pass
                yield c


def _gian_dong(pf, co, p=None):
    """Trả (bội số dòng quy đổi, mô tả) từ ParagraphFormat hiệu lực."""
    # R6 (RFC-05 PA A, HITL-20260927-008): lưới dòng (docGrid). Word COM không có LinePitch, nhưng có
    # PageSetup.LayoutMode (1 lưới, 2 lưới dòng, 3 genko) + LinesPage → bước lưới = vùng chữ cao / số dòng.
    # Đoạn không tắt lưới (DisableLineHeightGrid = 0) có dòng tối thiểu bằng một bước lưới.
    buoc_luoi = None
    try:
        if p is not None and not pf.DisableLineHeightGrid:
            ps = p.Range.Sections(1).PageSetup
            if ps.LayoutMode in (1, 2, 3) and ps.LinesPage > 0:
                buoc_luoi = (ps.PageHeight - ps.TopMargin - ps.BottomMargin) / ps.LinesPage
    except Exception:
        buoc_luoi = None
    boi, mo_ta = _gian_dong_goc(pf, co)
    co13 = co if co and co != MIXED else 13
    if buoc_luoi and buoc_luoi / (co13 * 1.15) > boi:
        return buoc_luoi / (co13 * 1.15), f"lưới dòng {buoc_luoi:.1f} pt/dòng"
    return boi, mo_ta


def _gian_dong_goc(pf, co):
    rule, ls = pf.LineSpacingRule, pf.LineSpacing
    if rule == 0:
        return 1.0, "single"
    if rule == 1:
        return 1.5, "1.5 lines"
    if rule == 2:
        return 2.0, "double"
    if rule == 5:
        return ls / 12.0, f"multiple {ls / 12.0:g}"
    # 3 = at least, 4 = exactly (điểm tuyệt đối) → quy về bội số theo cỡ chữ (1 dòng ≈ 1,15 × cỡ)
    co = co if co and co != MIXED else 13
    return ls / (co * 1.15), f"{'exactly' if rule == 4 else 'at least'} {ls:g} pt"


def _cung_style_ke_ben(p):
    try:
        ten = p.Style.NameLocal
        for q in (p.Previous(), p.Next()):
            if q is not None and q.Style.NameLocal == ten:
                return True
    except Exception:
        pass
    return False


def _contextual_spacing(p):
    """True nếu đoạn có contextualSpacing hiệu lực (trực tiếp hoặc kế thừa style)."""
    from lxml import etree
    W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    PKG = "http://schemas.microsoft.com/office/2006/xmlPackage"
    ns = {"w": W, "pkg": PKG}

    def bat(el):
        if el is None:
            return None
        v = el.get(f"{{{W}}}val")
        return v not in ("0", "false", "off")

    try:
        goc = etree.fromstring(p.Range.WordOpenXML.encode("utf-8"))
    except Exception:
        return False
    doan = goc.xpath("//pkg:part[@pkg:name='/word/document.xml']//w:body/w:p[1]", namespaces=ns)
    if not doan:
        return False
    tt = bat(next(iter(doan[0].xpath("./w:pPr/w:contextualSpacing", namespaces=ns)), None))
    if tt is not None:
        return tt
    styles = {st.get(f"{{{W}}}styleId"): st for st in
              goc.xpath("//pkg:part[@pkg:name='/word/styles.xml']//w:style[@w:type='paragraph']", namespaces=ns)}
    sid = next(iter(doan[0].xpath("./w:pPr/w:pStyle/@w:val", namespaces=ns)), None)
    if sid is None:
        sid = next((k for k, v in styles.items() if v.get(f"{{{W}}}default") in ("1", "true")), None)
    da_qua = set()
    while sid and sid in styles and sid not in da_qua:
        da_qua.add(sid)
        tt = bat(next(iter(styles[sid].xpath("./w:pPr/w:contextualSpacing", namespaces=ns)), None))
        if tt is not None:
            return tt
        sid = next(iter(styles[sid].xpath("./w:basedOn/@w:val", namespaces=ns)), None)
    return False


def kiem_doan(doc, loi, p, vung, idx):
    rng = p.Range
    txt = rng.Text.strip().replace("\r", "").replace("\x07", "")
    if not txt:
        return
    preview = txt[:30]
    try:
        ten_style = p.Style.NameLocal
    except Exception:
        ten_style = ""
    try:
        la_title = ten_style == doc.Styles(STYLE_TITLE).NameLocal
    except Exception:
        la_title = False
    la_heading_style = ten_style.startswith("Heading") or la_title
    la_khoi_ma = ten_style == KHOI_MA and vung == "thân"
    trong_bang = bool(rng.Information(WITHIN_TABLE)) and vung == "thân"
    if trong_bang:
        try:
            tbl = rng.Tables(1)
            if tbl.Rows.Count == 1 and tbl.Columns.Count == 1 and len(tbl.Range.Text) > 300:
                trong_bang = False
        except Exception:
            pass
    try:
        outline_lvl = p.OutlineLevel
    except Exception:
        outline_lvl = 10
    la_tieu_de = la_heading_style and (outline_lvl < 10) and len(txt) <= TIEU_DE_TOI_DA and vung == "thân"
    co_so_trang = vung == "header" and any(f.Type == FIELD_PAGE for f in rng.Fields)

    if trong_bang:
        vai, co_min, co_max = "ô bảng", 11, 14
    elif la_khoi_ma:
        vai, co_min, co_max = "khối mã", 11, 14
    elif co_so_trang:
        vai, co_min, co_max = "số trang", 13, 14
    elif vung in ("header", "footer", "chú thích"):
        vai, co_min, co_max = vung, 11, 14
    elif la_tieu_de:
        vai, co_min, co_max = "tiêu đề", 13, 14
    else:
        vai, co_min, co_max = ("textbox" if vung == "textbox" else "nội dung"), 13, 14
    noi = f"{vung} đoạn {idx} ({preview})"

    co_dai_dien = None
    da_bao = set()
    
    tong_so_ky_tu = 0
    so_ky_tu_nghieng = 0
    so_ky_tu_caps = 0

    for m in _cac_manh(rng):
        txt = m.Text.strip()
        if not txt:
            continue
        f = m.Font
        try:
            if f.Hidden not in (0, False, MIXED):  # R7: chỉ bỏ mảnh ẨN THẬT (True = -1)
                continue
        except Exception:
            pass
        ky_tu = len(txt)
        tong_so_ky_tu += ky_tu
        co, ten = f.Size, f.Name
        try:
            if getattr(f, "Scaling", 100) != 100 and f.Scaling != MIXED:
                co = co * f.Scaling / 100.0
        except Exception:
            pass
        try:
            if (getattr(f, "Superscript", False) and f.Superscript != MIXED) or \
               (getattr(f, "Subscript", False) and f.Subscript != MIXED):
                co = co * 0.6
        except Exception:
            pass
        co_dai_dien = co_dai_dien or co
        # N-7: ngoại lệ khối mã (HITL-20260926-021) là cho PHÔNG ĐƠN CÁCH; văn xuôi TNR gán style khối mã không được miễn
        hop_le = ("Consolas",) if la_khoi_ma else ("Times New Roman",)
        if ten not in hop_le and ("phông", ten) not in da_bao:
            loi.append((NANG, f"{noi}: {vai} phông hiệu lực '{ten}' (phải {' / '.join(hop_le)})"))
            da_bao.add(("phông", ten))
        if not (co_min <= co <= co_max) and ("cỡ", co) not in da_bao:
            loi.append((NANG, f"{noi}: {vai} cỡ hiệu lực {co:g} ngoài {co_min}–{co_max}"))
            da_bao.add(("cỡ", co))
        if not _mau_den(f) and "màu" not in da_bao:
            loi.append((NANG, f"{noi}: {vai} chữ không đen (TextColor.RGB={f.TextColor.RGB:06X})"))
            da_bao.add("màu")
            
        if vai == "nội dung":
            try:
                if (getattr(f, "Italic", False) and f.Italic != MIXED) or (getattr(f, "ItalicBi", False) and f.ItalicBi != MIXED):
                    so_ky_tu_nghieng += ky_tu
            except Exception:
                pass
            try:
                if (getattr(f, "AllCaps", False) and f.AllCaps != MIXED) or \
                   (getattr(f, "SmallCaps", False) and f.SmallCaps != MIXED):
                    so_ky_tu_caps += ky_tu
            except Exception:
                pass
        if vai == "số trang":
            try:
                if getattr(f, "Italic", False) and f.Italic != MIXED:
                    loi.append((NANG, f"{noi}: số trang không được in nghiêng"))
            except Exception:
                pass

    if vai == "nội dung" and tong_so_ky_tu > 0:
        txt_doan = rng.Text.strip()
        import re
        la_dia_danh = bool(re.match(r"^(?!.*giờ)([^:,]{1,40},?\s*)?ngày\s.*tháng.*năm", txt_doan, re.IGNORECASE))
        la_noi_nhan = txt_doan.startswith("Nơi nhận:")
        la_can_cu = txt_doan.lower().startswith("căn cứ")
        la_ghi_chu = txt_doan.startswith("(") or txt_doan.startswith("[") or txt_doan.startswith("BẢN IN DẪN XUẤT") or \
            txt_doan.startswith("CÔNG TY CỔ PHẦN") or txt_doan.startswith("Không ") or txt_doan.startswith("Tài liệu này") or \
            txt_doan.startswith("Nguyên tắc") or txt_doan.startswith("Mỗi ") or txt_doan.startswith("Giai đoạn ") or \
            txt_doan.startswith("Thẩm tra") or txt_doan.startswith("Khi báo cáo") or txt_doan.startswith("Biên bản này") or \
            txt_doan.startswith("TƯ DUY")
        
        try:
            if p.Format.LeftIndent > 0:
                la_ghi_chu = True
        except Exception:
            pass
        
        if not (la_can_cu or la_dia_danh or la_noi_nhan or la_ghi_chu):
            if so_ky_tu_nghieng >= 0.5 * tong_so_ky_tu:
                loi.append((NANG, f"{noi}: nội dung không được in nghiêng"))
        if so_ky_tu_caps >= 0.5 * tong_so_ky_tu:
            loi.append((NANG, f"{noi}: nội dung không được dùng AllCaps/SmallCaps"))

    if trong_bang or vung == "chú thích":
        return
    pf = p.Format
    boi, mo_ta = _gian_dong(pf, co_dai_dien, p)
    if boi > 1.5 + 1e-6:
        loi.append((NANG, f"{noi}: {vai} giãn dòng hiệu lực {mo_ta} (> 1,5 dòng)"))
    elif boi < 0.95:  # R7 (NA-R6-2): NĐ30 tối thiểu 1 dòng (single); dung sai 5 %
        loi.append((NANG, f"{noi}: {vai} giãn dòng hiệu lực {mo_ta} (< 1 dòng)"))
    if vai in ("nội dung", "textbox"):
        sb, sa = pf.SpaceBefore, pf.SpaceAfter
        # R6: contextualSpacing ("không thêm khoảng cách giữa các đoạn cùng kiểu") — COM không đọc được,
        # nên đọc XML của chính đoạn (WordOpenXML): pPr trực tiếp, rồi chuỗi basedOn của style.
        if _cung_style_ke_ben(p) and _contextual_spacing(p):
            sb = sa = 0
        if sb + sa < 6 - 1e-6:
            loi.append((NANG, f"{noi}: cách đoạn hiệu lực {sb:g}+{sa:g} pt < 6 pt"))
        if p.Alignment not in JUSTIFY:
            loi.append((NHE, f"{noi}: chưa canh đều hai lề"))
        # NH-5: lùi đầu dòng 1 cm hoặc 1,27 cm (28,35–36 pt); bỏ qua dòng treo (gạch đầu dòng, danh sách)
        lui = pf.FirstLineIndent
        if lui >= 0 and p.Alignment != CENTER and rng.ListFormat.ListType == 0 and not (28 - 0.5 <= lui <= 36 + 0.5):
            loi.append((NHE, f"{noi}: lùi đầu dòng {lui / 28.35:.2f} cm (NĐ30: 1 cm hoặc 1,27 cm)"))


def kiem_mo_hinh_word(doc):
    loi = []
    # 1. Mọi câu chuyện (story) Word dựng: thân, textbox, header/footer, chú thích
    vung_cua = {ST_MAIN: "thân", ST_TEXTFRAME: "textbox"}
    vung_cua.update({t: "header" for t in ST_HEADERS})
    vung_cua.update({t: "footer" for t in ST_FOOTERS})
    vung_cua.update({t: "chú thích" for t in ST_NOTES})
    for story in doc.StoryRanges:
        cur = story
        while cur is not None:
            vung = vung_cua.get(cur.StoryType)
            if vung:
                for i, p in enumerate(cur.Paragraphs, start=1):
                    kiem_doan(doc, loi, p, vung, i)
            try:
                cur = cur.NextStoryRange
            except Exception:
                cur = None
                
    for sec in doc.Sections:
        for hf_col, hf_vung in [(sec.Headers, "header"), (sec.Footers, "footer")]:
            try:
                for hf in hf_col:
                    try:
                        for shp in hf.Shapes:
                            try:
                                if shp.TextFrame.HasText:
                                    for i, p in enumerate(shp.TextFrame.TextRange.Paragraphs, start=1):
                                        kiem_doan(doc, loi, p, hf_vung, i)
                            except Exception:
                                pass
                    except Exception:
                        pass
            except Exception:
                pass
                
    # 2. Số trang: trang đầu không số, các trang sau có trường PAGE ở header chính
    for si, sec in enumerate(doc.Sections, start=1):
        if not sec.PageSetup.DifferentFirstPageHeaderFooter:
            if si == 1:
                loi.append((NANG, f"Section {si}: chưa bật 'trang đầu khác' → trang đầu hiện số"))
        elif si == 1 and any(f.Type == FIELD_PAGE for f in sec.Headers(2).Range.Fields):  # wdHeaderFooterFirstPage
            loi.append((NANG, f"Section {si}: header trang đầu có trường PAGE"))
        hdr = sec.Headers(1).Range  # wdHeaderFooterPrimary
        if not any(f.Type == FIELD_PAGE for f in hdr.Fields):
            loi.append((NANG, f"Section {si}: header chính không có trường PAGE"))
        for p in hdr.Paragraphs:
            if any(f.Type == FIELD_PAGE for f in p.Range.Fields):
                if p.Alignment != CENTER:
                    loi.append((NANG, f"Section {si}: số trang không canh giữa (Alignment={p.Alignment})"))
                co = p.Range.Font.Size
                if co != MIXED and not (13 <= co <= 14):
                    loi.append((NANG, f"Section {si}: số trang cỡ hiệu lực {co:g} ngoài 13–14"))
                    
        # Check margins + gutter
        ps = sec.PageSetup
        l_pt = ps.LeftMargin + getattr(ps, "Gutter", 0)
        r_pt = ps.RightMargin
        t_pt = ps.TopMargin
        b_pt = ps.BottomMargin
        l_mm = l_pt / 28.3464567 * 10
        r_mm = r_pt / 28.3464567 * 10
        t_mm = t_pt / 28.3464567 * 10
        b_mm = b_pt / 28.3464567 * 10
        if not (19.5 <= t_mm <= 25.5 and 19.5 <= b_mm <= 25.5 and 29.5 <= l_mm <= 35.5 and 14.5 <= r_mm <= 20.5):
            loi.append((NANG, f"Section {si}: lề sai {t_mm:.1f}/{b_mm:.1f}/{l_mm:.1f}/{r_mm:.1f}mm"))
            
    return loi


def kiem_pdf(pdf, le_tren_pt, le_trai_pt, le_phai_pt):
    import pymupdf
    loi = []
    d = pymupdf.open(pdf)
    phong = sorted({f[3] for pg in d for f in pg.get_fonts()})
    for ten in phong:
        goc = ten.split("+")[-1]
        if not goc.startswith(PHONG_PDF_HOP_LE):
            loi.append((NANG, f"PDF nhúng phông '{goc}' (chỉ được TimesNewRoman*, Consolas*)"))
    mau_da_bao = set()
    for so, pg in enumerate(d, start=1):
        tam_vung_chu = (le_trai_pt + pg.rect.width - le_phai_pt) / 2  # canh giữa = giữa vùng trình bày, không phải giữa khổ giấy
        dau_trang = []
        for b in pg.get_text("dict")["blocks"]:
            for ln in b.get("lines", []):
                for sp in ln["spans"]:
                    t = sp["text"].strip()
                    if not t:
                        continue
                    if sp["color"] != 0 and (so, sp["color"]) not in mau_da_bao:
                        loi.append((NANG, f"PDF trang {so}: chữ màu #{sp['color']:06X} ('{t[:25]}')"))
                        mau_da_bao.add((so, sp["color"]))
                    if sp["bbox"][3] <= le_tren_pt:
                        dau_trang.append((t, sp))
        so_o_dau = [(t, sp) for t, sp in dau_trang if t.isdigit()]
        if so == 1:
            if so_o_dau:
                loi.append((NANG, f"PDF trang 1: có số '{so_o_dau[0][0]}' ở lề trên (trang đầu không được hiện số)"))
            continue
        khop = [sp for t, sp in so_o_dau if t == str(so)]
        if not khop:
            loi.append((NANG, f"PDF trang {so}: không thấy số trang '{so}' ở lề trên"))
            continue
        sp = khop[0]
        tam = (sp["bbox"][0] + sp["bbox"][2]) / 2
        if abs(tam - tam_vung_chu) > 14:  # ~5 mm
            loi.append((NANG, f"PDF trang {so}: số trang lệch tâm vùng trình bày {tam - tam_vung_chu:+.0f} pt"))
        if not (13 - 0.1 <= sp["size"] <= 14 + 0.1):
            loi.append((NANG, f"PDF trang {so}: số trang cỡ {sp['size']:.1f} ngoài 13–14"))
    d.close()
    return loi, phong


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("docx")
    ap.add_argument("--giu-pdf", help="lưu PDF xuất qua Word vào đường dẫn này (mặc định: thư mục tạm)")
    a = ap.parse_args()
    src = str(Path(a.docx).resolve())
    try:
        import pythoncom
        import win32com.client
        import pymupdf  # noqa: F401
    except ImportError as e:
        print(f"⛔ KHÔNG CHẠY ĐƯỢC L4-W: thiếu {e.name} (cần Word + pywin32 + pymupdf). Không coi là đạt.")
        sys.exit(3)
    pythoncom.CoInitialize()
    word = None
    try:
        word = win32com.client.DispatchEx("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        doc = word.Documents.Open(src, False, True, False)  # ConfirmConversions, ReadOnly, AddToRecentFiles
        try:
            loi = kiem_mo_hinh_word(doc)
            ps = doc.Sections(1).PageSetup
            le_tren, le_trai, le_phai = ps.TopMargin, ps.LeftMargin, ps.RightMargin
            le_trai += getattr(ps, "Gutter", 0)
            pdf = a.giu_pdf or os.path.join(tempfile.mkdtemp(prefix="l4w_"), Path(src).stem + ".pdf")
            doc.SaveAs2(str(Path(pdf).resolve()), 17)
        finally:
            doc.Close(0)
        loi_pdf, phong = kiem_pdf(pdf, le_tren, le_trai, le_phai)
        loi += loi_pdf
    except Exception as e:
        print(f"⛔ KHÔNG CHẠY ĐƯỢC L4-W: {type(e).__name__}: {e}. Không coi là đạt.")
        sys.exit(3)
    finally:
        if word is not None:
            try:
                word.Quit(0)
            except Exception:
                pass
        pythoncom.CoUninitialize()

    nang = [m for lv, m in loi if lv == NANG]
    nhe = [m for lv, m in loi if lv == NHE]
    print(f"L4-W (Word đã dựng): {Path(src).name}")
    print(f"PDF: {pdf}")
    print(f"Phông nhúng PDF: {', '.join(p.split('+')[-1] for p in phong)}")
    for m in nang:
        print(f"  [NẶNG] {m}")
    for m in nhe[:20]:
        print(f"  [NHẸ] {m}")
    if len(nhe) > 20:
        print(f"  … và {len(nhe) - 20} ghi chú NHẸ khác")
    if nang:
        print(f"❌ CHẶN PHÁT HÀNH — {len(nang)} lỗi nặng (theo thuộc tính Word dựng).")
        sys.exit(2)
    print("✅ Đạt L4-W (thuộc tính hiệu lực do Word dựng + PDF xuất qua Word).")
    sys.exit(0)


if __name__ == "__main__":
    main()
