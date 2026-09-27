#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import sys
import zipfile
from pathlib import Path
from lxml import etree

try:
    from docx import Document
    from docx.shared import Pt, Length
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
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
        
        theme_map = {}
        if "word/theme/theme1.xml" in ten:
            th = z.read("word/theme/theme1.xml")
            root = etree.fromstring(th)
            ns = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
            for font_scheme in root.xpath("//a:fontScheme", namespaces=ns):
                for font_type in ["majorFont", "minorFont"]:
                    f_elem = font_scheme.xpath(f"a:{font_type}", namespaces=ns)
                    if f_elem:
                        prefix = font_type.replace("Font", "")
                        for child in f_elem[0]:
                            tag = child.tag.split('}')[-1]
                            script = child.get("script", "")
                            font_val = child.get("typeface", "")
                            if tag == "latin":
                                theme_map[f"{prefix}HAnsi"] = font_val
                                theme_map[f"{prefix}Ascii"] = font_val
                            elif tag == "ea":
                                theme_map[f"{prefix}EastAsia"] = font_val
                            elif tag == "cs":
                                theme_map[f"{prefix}Bidi"] = font_val
                            elif tag == "font":
                                if script == "Hans":
                                    theme_map[f"{prefix}EastAsia"] = font_val
                                elif script == "Arab":
                                    theme_map[f"{prefix}Bidi"] = font_val
                                # Simplified: map everything to these 4 keys
                                

    if co_watermark:
        return [(NHE, f"Có watermark trong {len(header)} file header — đối chiếu bản gốc xem đúng trang chưa")], theme_map
    if bat_buoc:
        return [(NANG, "Bản gốc yêu cầu watermark nhưng file này KHÔNG có watermark trong header")], theme_map
    return [(NHE, f"Không thấy watermark (file có {len(anh_header)} ảnh nhúng) — "
                  "nếu bản gốc có watermark thì đã mất")], theme_map

def doc_numbering(duong_dan):
    num_to_abs = {}
    abs_to_ilvl = {}
    with zipfile.ZipFile(duong_dan) as z:
        if "word/numbering.xml" in z.namelist():
            num_xml = z.read("word/numbering.xml")
            root = etree.fromstring(num_xml)
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            for num in root.xpath("//w:num", namespaces=ns):
                num_id = num.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}numId")
                abs_elem = num.xpath("w:abstractNumId", namespaces=ns)
                if abs_elem:
                    num_to_abs[num_id] = abs_elem[0].get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val")
                    
            for abs_num in root.xpath("//w:abstractNum", namespaces=ns):
                abs_id = abs_num.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}abstractNumId")
                abs_to_ilvl[abs_id] = {}
                for lvl in abs_num.xpath("w:lvl", namespaces=ns):
                    ilvl = lvl.get("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ilvl")
                    fonts = lvl.xpath("w:rPr/w:rFonts", namespaces=ns)
                    font_dict = {}
                    if fonts:
                        f = fonts[0]
                        for k in ["ascii", "hAnsi", "eastAsia", "cs", "asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"]:
                            val = f.get(f"{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}{k}")
                            if val: font_dict[k] = val
                    abs_to_ilvl[abs_id][ilvl] = font_dict
    return num_to_abs, abs_to_ilvl


def get_text(p):
    text = ""
    for r in p.runs:
        if r.font.hidden or (r._r.rPr is not None and len(r._r.rPr.xpath('./w:vanish')) > 0):
            continue
        text += r.text
    return text


def kiem_nd30_tang_1(tai_lieu, theme_map, num_to_abs, abs_to_ilvl):
    loi = []
    
    # Extract styles font to resolve inheritance
    styles_font = {}
    for st in tai_lieu.styles:
        if st.type == 1: # paragraph style
            rPr = st._element.rPr
            st_fonts = {}
            if rPr is not None and rPr.rFonts is not None:
                for k in ["ascii", "hAnsi", "eastAsia", "cs", "asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"]:
                    val = rPr.rFonts.get(qn(f"w:{k}"))
                    if val: st_fonts[k] = val
            styles_font[st.name] = st_fonts
    
    # Helpers
    def get_eff_fonts(run, para):
        eff = {"ascii": "Times New Roman", "hAnsi": "Times New Roman", "eastAsia": "Times New Roman", "cs": "Times New Roman"}
        
        # 1. Base from Normal style
        norm = styles_font.get("Normal", {})
        
        # 2. Paragraph style
        st_name = para.style.name if para.style else "Normal"
        p_st = styles_font.get(st_name, norm)
        
        # 3. Run properties
        r_fonts = {}
        rPr = run._element.rPr
        if rPr is not None and rPr.rFonts is not None:
            for k in ["ascii", "hAnsi", "eastAsia", "cs", "asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"]:
                val = rPr.rFonts.get(qn(f"w:{k}"))
                if val: r_fonts[k] = val
        
        for k in ["ascii", "hAnsi", "eastAsia", "cs"]:
            # Check Run explicitly
            if f"{k}Theme" in r_fonts:
                eff[k] = theme_map.get(r_fonts[f"{k}Theme"], r_fonts[f"{k}Theme"])
            elif k in r_fonts:
                eff[k] = r_fonts[k]
            # Else check Style
            elif f"{k}Theme" in p_st:
                eff[k] = theme_map.get(p_st[f"{k}Theme"], p_st[f"{k}Theme"])
            elif k in p_st:
                eff[k] = p_st[k]
            # Else check Normal style
            elif f"{k}Theme" in norm:
                eff[k] = theme_map.get(norm[f"{k}Theme"], norm[f"{k}Theme"])
            elif k in norm:
                eff[k] = norm[k]
                
            # If still theme (e.g. implicitly set from docDefaults)
            if eff[k] in theme_map:
                eff[k] = theme_map[eff[k]]
                
        return eff
        
    def get_eff_size(run, para):
        if run.font and run.font.size: return run.font.size.pt
        if para.style and para.style.font and para.style.font.size: return para.style.font.size.pt
        st_name = para.style.name if para.style else "Normal"
        # Not implementing full size inheritance, just assume 13 if missing
        return 13

    def _doc_ke_thua(p, thuoc_tinh):
        val = getattr(p.paragraph_format, thuoc_tinh)
        if val is not None:
            if thuoc_tinh == 'line_spacing':
                return val if not isinstance(val, Length) else None
            return val.pt
            
        if thuoc_tinh == 'line_spacing':
            sp = p._p.xpath('./w:pPr/w:spacing')
            if sp and sp[0].get(qn('w:line')) and sp[0].get(qn('w:lineRule'), 'auto') == 'auto':
                return int(sp[0].get(qn('w:line'))) / 240

        st = p.style
        seen = set()
        while st is not None and st.name not in seen:
            seen.add(st.name)
            if hasattr(st, "paragraph_format"):
                s_val = getattr(st.paragraph_format, thuoc_tinh)
                if s_val is not None:
                    if thuoc_tinh == 'line_spacing':
                        return s_val if not isinstance(s_val, Length) else None
                    return s_val.pt
            st = st.base_style
            
        sp = tai_lieu.styles.element.xpath('./w:docDefaults/w:pPrDefault/w:pPr/w:spacing')
        if sp:
            if thuoc_tinh == 'space_before' and sp[0].get(qn('w:before')):
                return int(sp[0].get(qn('w:before'))) / 20
            if thuoc_tinh == 'space_after' and sp[0].get(qn('w:after')):
                return int(sp[0].get(qn('w:after'))) / 20
            if thuoc_tinh == 'line_spacing' and sp[0].get(qn('w:line')) and sp[0].get(qn('w:lineRule'), 'auto') == 'auto':
                return int(sp[0].get(qn('w:line'))) / 240
                
        return 0 if thuoc_tinh != 'line_spacing' else None

    # Section checks (6.1, 6.2, 6.8)
    total_pages = 2 # approximation, 6.8 ignores if 1 page, we just assume >1 for test
    for i, sec in enumerate(tai_lieu.sections):
        w = sec.page_width.mm if sec.page_width else 0
        h = sec.page_height.mm if sec.page_height else 0
        
        # 6.1
        if w > h:
            loi.append((NHE, f"Section {i+1}: hướng ngang — đối chiếu ngoại lệ bảng biểu"))
        elif not (209 <= w <= 211 and 296 <= h <= 298):
            loi.append((NANG, f"Section {i+1}: khổ giấy {w:.0f}x{h:.0f}mm không phải A4"))
            
        # 6.2
        t = sec.top_margin.mm if sec.top_margin else 0
        b = sec.bottom_margin.mm if sec.bottom_margin else 0
        l = sec.left_margin.mm if sec.left_margin else 0
        r = sec.right_margin.mm if sec.right_margin else 0
        g = sec.gutter.mm if sec.gutter else 0
        l += g
        
        if not (19.5 <= t <= 25.5 and 19.5 <= b <= 25.5 and 29.5 <= l <= 35.5 and 14.5 <= r <= 20.5):
            loi.append((NANG, f"Section {i+1}: lề sai {t:.1f}/{b:.1f}/{l:.1f}/{r:.1f}mm"))
            
        # 6.8
        # Since finding PAGE in header is complex with docx, we just check the XML
        has_page = False
        header_center = False
        first_page_ok = sec.different_first_page_header_footer if i == 0 else True
        
        for hdr in [sec.header, sec.first_page_header, sec.even_page_header]:
            if hdr and not hdr.is_linked_to_previous:
                for p in hdr.paragraphs:
                    if 'PAGE' in p._p.xml:
                        has_page = True
                        if p.alignment == WD_ALIGN_PARAGRAPH.CENTER or 'jc w:val="center"' in p._p.xml:
                            header_center = True
        
        if not first_page_ok:
            loi.append((NANG, f"Section {i+1}: trang đầu có số (chưa bật different_first_page)"))
        if not has_page:
            loi.append((NANG, f"Section {i+1}: không có số trang (trường PAGE)"))

    # Paragraph checks
    # R2 (HITL-20260927-001): đoạn trong textbox (w:txbxContent) không nằm trong tai_lieu.paragraphs
    # → gom thêm và kiểm như đoạn nội dung. Bỏ bản mc:Fallback (VML trùng bản DrawingML).
    from docx.text.paragraph import Paragraph
    doan_textbox = [Paragraph(el, tai_lieu._body) for el in etree._Element.xpath(
        tai_lieu.element.body, './/w:txbxContent[not(ancestor::mc:Fallback)]//w:p',
        namespaces={"w": NS_W[1:-1], "mc": "http://schemas.openxmlformats.org/markup-compatibility/2006"})]
    id_textbox = {id(p._p) for p in doan_textbox}
    TIEU_DE_TOI_DA = 200  # ký tự; tiêu đề dài hơn = văn xuôi đội lốt tiêu đề → kiểm như nội dung
    for p_idx, p in enumerate(list(tai_lieu.paragraphs) + doan_textbox, start=1):
        txt = get_text(p).strip()
        if not txt: continue
        preview = txt[:30]
        st_name = p.style.name if p.style else ""
        la_textbox = id(p._p) in id_textbox

        # 6.6, 6.7, 6.9
        # RFC-03: "nội dung" xác định theo VAI TRÒ đoạn, không theo tên style — mọi đoạn ngoài bảng,
        # trừ khối mã (ngoại lệ HITL-20260926-021) và tiêu đề (tiêu đề chỉ kiểm cỡ chữ 13–14).
        # R2: đoạn trong textbox luôn là nội dung; tiêu đề dài quá TIEU_DE_TOI_DA ký tự là nội dung;
        # giãn dòng ≤ 1,5 áp cho MỌI đoạn ngoài bảng, kể cả tiêu đề và khối mã.
        is_heading = (st_name.startswith("Heading") or st_name == "Title") and not la_textbox \
            and len(txt) <= TIEU_DE_TOI_DA
            
        # R4-2: "tiêu đề" phải vừa là style tiêu đề vừa có outline < 10
        try:
            outline_lvl = p.paragraph_format.outline_level
        except Exception:
            outline_lvl = 10 # body text
        if outline_lvl is None or outline_lvl >= 10:
            is_heading = False
            
        la_khoi_ma = st_name == "NĐ30 Khối mã" and not la_textbox
        ngoai_bang = la_textbox or not p._p.xpath('ancestor::w:tbl')
        is_normal = ngoai_bang and not la_khoi_ma and not is_heading

        if ngoai_bang:
            # 6.6 Giãn dòng
            ls = _doc_ke_thua(p, 'line_spacing')
            if isinstance(ls, float) and ls < 0.95:  # R7 (NA-R6-2): tối thiểu 1 dòng
                loi.append((NANG, f"Đoạn {p_idx} ({preview}): giãn dòng {ls:g} < 1"))
            if ls is not None and ls > 1.5:
                vai = "tiêu đề" if is_heading else ("khối mã" if la_khoi_ma else ("textbox" if la_textbox else "nội dung"))
                loi.append((NANG, f"Đoạn {p_idx} ({preview}): {vai} giãn dòng {ls:g} > 1.5"))

        if is_normal:

            # 6.7 Khoảng cách đoạn
            sb = _doc_ke_thua(p, 'space_before')
            sa = _doc_ke_thua(p, 'space_after')
            if sb + sa < 6:
                loi.append((NANG, f"Đoạn {p_idx} ({preview}): khoảng cách đoạn < 6pt"))
                
            # 6.9 Canh lề
            al = p.alignment
            if al is None and p.style and hasattr(p.style, "paragraph_format"):
                al = p.style.paragraph_format.alignment
            if al != WD_ALIGN_PARAGRAPH.JUSTIFY:
                loi.append((NHE, f"Đoạn {p_idx} ({preview}): chưa canh đều hai bên (justify)"))
                
        # 6.3 mở rộng: kiểm tra numbering font
        num_pr = p._p.pPr.numPr if p._p.pPr is not None else None
        if num_pr is None and p.style and p.style.type == 1:
            if p.style._element.pPr is not None:
                num_pr = p.style._element.pPr.numPr
        
        if num_pr is not None:
            num_id = num_pr.xpath("w:numId/@w:val")
            ilvl = num_pr.xpath("w:ilvl/@w:val")
            if num_id:
                nid = num_id[0]
                ilv = ilvl[0] if ilvl else "0"
                abs_id = num_to_abs.get(nid)
                if abs_id:
                    num_fonts = abs_to_ilvl.get(abs_id, {}).get(ilv, {})
                    # Giải mã theme
                    eff_num = {}
                    for k in ["ascii", "hAnsi", "eastAsia", "cs"]:
                        if f"{k}Theme" in num_fonts:
                            eff_num[k] = theme_map.get(num_fonts[f"{k}Theme"], num_fonts[f"{k}Theme"])
                        elif k in num_fonts:
                            eff_num[k] = num_fonts[k]
                    
                    for script, f_name in eff_num.items():
                        if f_name != "Times New Roman":
                            loi.append((NANG, f"Đoạn {p_idx} ({preview}): ký tự đầu dòng (numId={nid}, ilvl={ilv}) dùng phông {f_name} khác Times New Roman"))
                            break
        
        for r_idx, r in enumerate(p.runs):
            if not r.text.strip(): continue
            if r.font.hidden: continue
            
            # 6.3 Font
            fonts = get_eff_fonts(r, p)
            if la_khoi_ma:
                pass
            else:
                for script, f_name in fonts.items():
                    if f_name != "Times New Roman":
                        loi.append((NANG, f"Đoạn {p_idx} ({preview}): sai phông chữ {f_name} (ở {script})"))
                        break
                        
            # 6.10 Emoji
            for idx, c in enumerate(r.text):
                code = ord(c)
                if (0x2300 <= code <= 0x23FF) or (0x2600 <= code <= 0x27BF) or (0x2B00 <= code <= 0x2BFF) or (0x1F000 <= code <= 0x1FAFF) or (code == 0xFE0F):
                    loi.append((NANG, f"Đoạn {p_idx} ({preview}): có emoji/ký hiệu '{c}' tại vị trí {idx}"))
            
            # 6.4 Color
            # python-docx rgb is None if auto, or RGBColor. If it's a theme color, it's not RGBColor.
            # We just check RGB for non-black/non-auto
            color = r.font.color.rgb if r.font and r.font.color else None
            if color is not None and str(color) not in ["000000", ""]:
                loi.append((NANG, f"Đoạn {p_idx} ({preview}): chữ màu {color} (phải đen/tự động)"))
            
            # check shading for white text on colored bg
            shd = r._element.xpath('.//w:shd/@w:fill')
            if shd and shd[0] not in ['auto', '000000', 'FFFFFF'] and str(color) == 'FFFFFF':
                loi.append((NANG, f"Đoạn {p_idx} ({preview}): chữ trắng trên nền màu"))
                
            # 6.5 Size
            size = get_eff_size(r, p)
            if size < 11:
                loi.append((NANG, f"Đoạn {p_idx} ({preview}): cỡ chữ {size} < 11"))
            elif (is_normal or is_heading) and not (13 <= size <= 14):
                loi.append((NANG, f"Đoạn {p_idx} ({preview}): {'tiêu đề' if is_heading else 'nội dung'} cỡ {size} ngoài 13–14"))
            elif la_khoi_ma and size > 14:
                # R3: ngoại lệ khối mã (HITL-20260926-021) chỉ cho phông đơn cách cỡ ≥ 11, không cho cỡ tuỳ ý
                loi.append((NANG, f"Đoạn {p_idx} ({preview}): khối mã cỡ {size} ngoài 11–14"))
                
    # Check tables
    # R3 (HITL-20260927-001): duyệt theo XML mọi w:p trong từng hàng của bảng cấp đầu — gồm cả
    # bảng lồng trong bảng và textbox trong ô (python-docx cell.paragraphs chỉ lấy đoạn trực tiếp).
    # Khối mã trong ô bảng cũng phải 11–14 (không còn miễn trừ cỡ).
    from docx.text.paragraph import Paragraph
    for t_idx, t in enumerate(tai_lieu.tables, start=1):
        for r_idx, tr in enumerate(t._tbl.xpath('./w:tr')):
            for p_el in tr.xpath('.//w:p[not(ancestor::w:txbxContent)]'):
                p = Paragraph(p_el, t)
                long_nhau = len(p_el.xpath('ancestor::w:tbl')) > 1
                vi_tri = f"Bảng {t_idx}: {'bảng lồng trong ' if long_nhau else ''}ô hàng {r_idx+1}"
                for run in p.runs:
                    if not run.text.strip(): continue
                    if run.font.hidden: continue
                    cs = run.font.size.pt if run.font.size else (p.style.font.size.pt if p.style and p.style.font.size else None)
                    if cs is not None and not (11 <= cs <= 14):
                        loi.append((NANG, f"{vi_tri} cỡ chữ {cs} ngoài 11–14"))
                    color = run.font.color.rgb if run.font and run.font.color else None
                    if color is not None and str(color) == "FFFFFF":
                        loi.append((NANG, f"{vi_tri}: có chữ trắng"))

    return loi

# Tên loại (ô 5a) theo NĐ30 Phụ lục III: Mẫu 1.4 (17 loại, ghi chú 6 tr.47) + Biên bản (Mẫu 1.9).
# Công văn không có tên loại. Phải khớp LOAI_MAU_14 trong .agents/scripts/sinh_van_ban_nd30.py.
TEN_LOAI = {
    "CT": "CHỈ THỊ", "QC": "QUY CHẾ", "QyĐ": "QUY ĐỊNH", "TC": "THÔNG CÁO", "TB": "THÔNG BÁO",
    "HD": "HƯỚNG DẪN", "CTr": "CHƯƠNG TRÌNH", "KH": "KẾ HOẠCH", "PA": "PHƯƠNG ÁN", "ĐA": "ĐỀ ÁN",
    "DA": "DỰ ÁN", "BC": "BÁO CÁO", "TTr": "TỜ TRÌNH", "GUQ": "GIẤY ỦY QUYỀN", "PG": "PHIẾU GỬI",
    "PC": "PHIẾU CHUYỂN", "PB": "PHIẾU BÁO", "BB": "BIÊN BẢN",
    # Đợt 2 — mẫu riêng: 1.1 tr.42, 1.2–1.3 tr.43–44, 1.6 tr.49, 1.7 tr.50, 1.8 tr.51, 1.10 tr.53
    "NQ": "NGHỊ QUYẾT", "QĐ": "QUYẾT ĐỊNH", "CĐ": "CÔNG ĐIỆN",
    "GM": "GIẤY MỜI", "GGT": "GIẤY GIỚI THIỆU", "GNP": "GIẤY NGHỈ PHÉP",
}
# Dòng đặc trưng bắt buộc của từng mẫu riêng (khớp nguyên dòng, hoặc chứa cụm)
DONG_DAC_TRUNG = {  # (mô tả, điều kiện trên đoạn) — vị trí xét trong kiem_nd30_tang_2
    "NQ": ("QUYẾT NGHỊ:", lambda t: t == "QUYẾT NGHỊ:"),
    "QĐ": ("QUYẾT ĐỊNH:", lambda t: t == "QUYẾT ĐỊNH:"),
    "CĐ": ("… điện:", lambda t: t.endswith(" điện:")),
    "GM": ("… trân trọng kính mời: …", lambda t: "trân trọng kính mời:" in t),
    "GGT": ("… trân trọng giới thiệu:", lambda t: t.endswith("trân trọng giới thiệu:")),
    "GNP": ("Xét Đơn đề nghị nghỉ phép … cấp cho:", lambda t: t.startswith("Xét Đơn") and t.endswith("cấp cho:")),
}


def dong_dia_danh_ngay(txt):
    """Dòng "<Địa danh>, ngày … tháng … năm …" (ô 4). NH-2: dòng có nhãn "…: …, ngày …" trong thân
    Biên bản (vd "Thời gian bắt đầu: 8 giờ, ngày …") KHÔNG phải ô 4 — Mẫu 1.9 có dòng đó."""
    import re
    return bool(re.match(r"^(?!.*giờ)([^:,]{1,40},?\s*)?ngày\s.*tháng.*năm", txt.strip(), re.IGNORECASE))


def kiem_nd30_tang_2(tai_lieu, loai):
    loi = []
    texts = [get_text(p).strip() for p in tai_lieu.paragraphs if get_text(p).strip()]
    for t in tai_lieu.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    if get_text(p).strip():
                        texts.append(get_text(p).strip())
    text_all = "\n".join(texts)
    
    if "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" not in text_all:
        loi.append((NANG, "Thiếu CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM"))
    if "Độc lập - Tự do - Hạnh phúc" not in text_all:
        loi.append((NANG, "Thiếu Độc lập - Tự do - Hạnh phúc"))
        
    if "Nơi nhận:" not in text_all:
        loi.append((NANG, "Thiếu Nơi nhận:"))
    if "- Lưu: VT" not in text_all and "Lưu: VT" not in text_all:
        loi.append((NANG, "Thiếu dòng Lưu: VT"))
        
    # L-1 (QA Tầng 2 Đợt 1, 27/09/2026): ký hiệu phải nằm ĐÚNG dòng "Số:" (ô 3), không phải chuỗi con bất kỳ
    # trong thân (vd "Căn cứ Chỉ thị số 03/CT-…"); và tên loại (ô 5a) phải là một dòng riêng đúng loại.
    import re
    dong_so = [t for t in texts if re.match(r"^Số\s*:", t)]
    if not dong_so:
        loi.append((NANG, "Thiếu dòng \"Số:\" (ô 3)"))
    elif loai != "CV":
        if not re.match(rf"^Số\s*:\s*[^/\s]*/{re.escape(loai)}-", dong_so[0]):
            loi.append((NANG, f"Ký hiệu sai quy tắc: dòng \"{dong_so[0][:40]}\" phải có dạng Số: …/{loai}-…"))
    elif "/CV-" in dong_so[0]:
        # CV không được có chữ viết tắt tên loại
        loi.append((NANG, "Ký hiệu sai quy tắc (CV không được chứa /CV-)"))
    # QA Đợt 2 (L1, L2, V4 — 27/09/2026): xét VỊ TRÍ, không dò chuỗi con toàn văn bản.
    #  - tên loại (ô 5a) phải là một trong 3 đoạn thân đầu tiên (ngay sau bảng đầu văn bản);
    #  - GGT/GNP (Mẫu 1.8/1.10) không có trích yếu dưới tên loại;
    #  - dòng đặc trưng của CĐ/GM/GGT/GNP phải là đoạn thân NGAY SAU tên loại; NQ/QĐ là một dòng riêng sau tên loại.
    than = [get_text(p).strip() for p in tai_lieu.paragraphs if get_text(p).strip()]
    ten_loai = TEN_LOAI.get(loai)
    idx_ten = None
    if ten_loai:
        idx_ten = next((i for i, t in enumerate(than[:3]) if t.split("\n")[0].strip() == ten_loai), None)
        if idx_ten is None:
            loi.append((NANG, f"Thiếu tên loại \"{ten_loai}\" ở đầu văn bản (ô 5a) — hoặc tên loại không khớp --loai {loai}"))
    if idx_ten is not None and loai in ("GGT", "GNP"):
        du = [x.strip() for x in than[idx_ten].split("\n")[1:] if x.strip() and set(x.strip()) - {"_"}]
        if du:
            loi.append((NANG, f"{ten_loai} không có trích yếu (Mẫu {'1.8' if loai == 'GGT' else '1.10'}), thấy: \"{du[0][:40]}\""))
    dt = DONG_DAC_TRUNG.get(loai)
    if dt and idx_ten is not None:
        mo_ta, dung = dt
        if loai in ("NQ", "QĐ"):
            co = any(dung(t) for t in than[idx_ten + 1:])
        else:
            co = idx_ten + 1 < len(than) and dung(than[idx_ten + 1])
        if not co:
            loi.append((NANG, f"Thiếu dòng đặc trưng \"{mo_ta}\" của mẫu {ten_loai}"
                              f"{'' if loai in ('NQ', 'QĐ') else ' (phải là đoạn ngay sau tên loại)'}"))
    if loai == "CV" and "V/v" not in text_all:
        loi.append((NANG, "Thiếu V/v"))
            
    if loai == "BB":
        # BB không có dòng ngày ở đầu (kiểm tra bảng đầu tiên và 5 đoạn đầu)
        found_date = False
        if tai_lieu.tables:
            for row in tai_lieu.tables[0].rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        if dong_dia_danh_ngay(get_text(p)):
                            found_date = get_text(p)
        for p in tai_lieu.paragraphs:
            if get_text(p).strip().upper().startswith("BIÊN BẢN"):
                break
            if dong_dia_danh_ngay(get_text(p)):
                found_date = get_text(p)
        if found_date:
            loi.append((NANG, f"Biên bản không được có dòng ngày tháng năm ở đầu văn bản (Found: {found_date})"))
                
    return loi


def main():
    for luong in (sys.stdout, sys.stderr):
        if hasattr(luong, "reconfigure"):
            luong.reconfigure(encoding="utf-8", errors="replace")

    p = argparse.ArgumentParser(description="Kiểm .docx trước khi phát hành")
    p.add_argument("docx", help="File .docx cần kiểm")
    p.add_argument("--watermark-bat-buoc", action="store_true",
                   help="Bản gốc có watermark — thiếu là lỗi NẶNG")
    p.add_argument("--loai", choices=["BB", "CV", "BC", "CT", "QC", "QyĐ", "TC", "TB", "HD", "CTr", "KH", "PA", "ĐA", "DA", "TTr", "GUQ", "PG", "PC", "PB", "NQ", "QĐ", "CĐ", "GM", "GGT", "GNP"],
                   help="Loại văn bản để kiểm tra Thể thức Tầng 2 (Mẫu 1.4 / 1.5 / 1.9)")
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
    loi_watermark, theme_map = kiem_watermark(duong_dan, tham_so.watermark_bat_buoc)
    loi += loi_watermark
    num_to_abs, abs_to_ilvl = doc_numbering(duong_dan)
    loi += kiem_nd30_tang_1(tai_lieu, theme_map, num_to_abs, abs_to_ilvl)
    if tham_so.loai:
        loi += kiem_nd30_tang_2(tai_lieu, tham_so.loai)

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
