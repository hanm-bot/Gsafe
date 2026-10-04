# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

F="Times New Roman"

doc=Document()
sec=doc.sections[0]
sec.page_width=Cm(21.0); sec.page_height=Cm(29.7)
sec.top_margin=Cm(2.0); sec.bottom_margin=Cm(2.0)
sec.left_margin=Cm(3.0); sec.right_margin=Cm(1.5)

st=doc.styles['Normal']; st.font.name=F; st.font.size=Pt(13)
st.element.rPr.rFonts.set(qn('w:eastAsia'),F)

def para(text="", size=13, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
         before=0, after=6, indent=None, first=None, line=1.3):
    p=doc.add_paragraph()
    p.alignment=align
    pf=p.paragraph_format
    pf.space_before=Pt(before); pf.space_after=Pt(after)
    pf.line_spacing=line
    if indent is not None: pf.left_indent=Cm(indent)
    if first is not None: pf.first_line_indent=Cm(first)
    if text:
        r=p.add_run(text); r.font.name=F; r.font.size=Pt(size); r.bold=bold; r.italic=italic
        r.element.rPr.rFonts.set(qn('w:eastAsia'),F)
    return p

def addrun(p,text,size=13,bold=False,italic=False):
    r=p.add_run(text); r.font.name=F; r.font.size=Pt(size); r.bold=bold; r.italic=italic
    r.element.rPr.rFonts.set(qn('w:eastAsia'),F)
    return r

def no_borders(tbl):
    tblPr=tbl._tbl.tblPr
    b=OxmlElement('w:tblBorders')
    for e in ('top','left','bottom','right','insideH','insideV'):
        el=OxmlElement(f'w:{e}'); el.set(qn('w:val'),'none'); b.append(el)
    tblPr.append(b)

def cellp(cell,text,size=13,bold=False,italic=False,align=WD_ALIGN_PARAGRAPH.CENTER,after=0):
    p=cell.paragraphs[0] if not cell.paragraphs[0].runs else cell.add_paragraph()
    p.alignment=align
    p.paragraph_format.space_after=Pt(after); p.paragraph_format.space_before=Pt(0)
    p.paragraph_format.line_spacing=1.15
    r=p.add_run(text); r.font.name=F; r.font.size=Pt(size); r.bold=bold; r.italic=italic
    r.element.rPr.rFonts.set(qn('w:eastAsia'),F)
    return p

# ===== HEADER 2 cot =====
tbl=doc.add_table(rows=1,cols=2); tbl.alignment=WD_TABLE_ALIGNMENT.CENTER
no_borders(tbl)
tbl.columns[0].width=Cm(6.8); tbl.columns[1].width=Cm(9.7)
tbl.rows[0].cells[0].width=Cm(6.8); tbl.rows[0].cells[1].width=Cm(9.7)
c0,c1=tbl.rows[0].cells
cellp(c0,"CÃ”NG TY Cá»” PHáº¦N",size=12,bold=True)
cellp(c0,"Äáº¦U TÆ¯ CÃ”NG NGHá»† SHT",size=12,bold=True)
p=cellp(c0,"Sá»‘:        /2026/CV-SHT",size=13)
cellp(c0,"V/v phá»‘i há»£p giáº£i trÃ¬nh vá»›i cÆ¡ quan thuáº¿ vá» nghÄ©a vá»¥ láº­p hÃ³a Ä‘Æ¡n GTGT theo Há»£p Ä‘á»“ng sá»‘ [Sá»_HÄ]",size=11,italic=True)
cellp(c1,"Cá»˜NG HÃ’A XÃƒ Há»˜I CHá»¦ NGHÄ¨A VIá»†T NAM",size=12,bold=True)
cellp(c1,"Äá»™c láº­p â€“ Tá»± do â€“ Háº¡nh phÃºc",size=13,bold=True)
cellp(c1,"________________________",size=11)
cellp(c1,"HÃ  Ná»™i, ngÃ y       thÃ¡ng 8 nÄƒm 2026",size=13,italic=True)

para("",after=8)
para("KÃ­nh gá»­i: BAN LÃƒNH Äáº O NGÃ‚N HÃ€NG TMCP VIá»†T NAM THá»ŠNH VÆ¯á»¢NG ([NGÃ‚N_HÃ€NG_A])",bold=True,align=WD_ALIGN_PARAGRAPH.CENTER,after=10)

# ===== Can cu =====
for t in [
 "CÄƒn cá»© Há»£p Ä‘á»“ng nguyÃªn táº¯c cung cáº¥p hÃ ng hÃ³a sá»‘ [Sá»_HÄ] kÃ½ ngÃ y [NGÃ€Y_KÃ] giá»¯a NgÃ¢n hÃ ng TMCP Viá»‡t Nam Thá»‹nh VÆ°á»£ng vÃ  CÃ´ng ty Cá»• pháº§n Äáº§u tÆ° CÃ´ng nghá»‡ SHT, cÃ¹ng cÃ¡c Phá»¥ lá»¥c Há»£p Ä‘á»“ng sá»‘ 01, 02, 03 (sau Ä‘Ã¢y gá»i lÃ  â€œHá»£p Ä‘á»“ngâ€);",
 "CÄƒn cá»© ÄÆ¡n Ä‘áº·t hÃ ng sá»‘ 01 vá»›i sá»‘ lÆ°á»£ng [Sá»_LÆ¯á»¢NG] thiáº¿t bá»‹ POS vÃ  bá»™ há»“ sÆ¡ bÃ n giao Ä‘Ã£ xÃ¡c láº­p giá»¯a CÃ¡c BÃªn;",
 "CÄƒn cá»© Äiá»u 9 Nghá»‹ Ä‘á»‹nh sá»‘ 123/2020/NÄ-CP ngÃ y 19/10/2020 cá»§a ChÃ­nh phá»§: thá»i Ä‘iá»ƒm láº­p hÃ³a Ä‘Æ¡n Ä‘á»‘i vá»›i bÃ¡n hÃ ng hÃ³a lÃ  thá»i Ä‘iá»ƒm chuyá»ƒn giao quyá»n sá»Ÿ há»¯u hoáº·c quyá»n sá»­ dá»¥ng hÃ ng hÃ³a cho ngÆ°á»i mua, khÃ´ng phÃ¢n biá»‡t Ä‘Ã£ thu Ä‘Æ°á»£c tiá»n hay chÆ°a thu Ä‘Æ°á»£c tiá»n;",
 "CÄƒn cá»© ThÃ´ng bÃ¡o sá»‘ [Sá»_THÃ”NG_BÃO_THUáº¾] ngÃ y [NGÃ€Y] cá»§a [CÆ _QUAN_THUáº¾] vá» káº¿ hoáº¡ch kiá»ƒm tra táº¡i trá»¥ sá»Ÿ ngÆ°á»i ná»™p thuáº¿ nÄƒm 2026 Ä‘á»‘i vá»›i CÃ´ng ty Cá»• pháº§n Äáº§u tÆ° CÃ´ng nghá»‡ SHT (cÄƒn cá»© Quyáº¿t Ä‘á»‹nh sá»‘ 6568/QÄ-HAN-KTr1 ngÃ y 06/5/2026 cá»§a TrÆ°á»Ÿng [CÆ _QUAN_THUáº¾]),",
]:
    para(t,italic=True,first=1.0,after=4)

para("CÃ´ng ty Cá»• pháº§n Äáº§u tÆ° CÃ´ng nghá»‡ SHT (sau Ä‘Ã¢y gá»i lÃ  â€œSHTâ€) thÃ´ng bÃ¡o vÃ  Ä‘á» nghá»‹ QuÃ½ NgÃ¢n hÃ ng nhÆ° sau:",first=1.0,before=6)

# ===== I =====
para("I. TÃ“M Táº®T Sá»° VIá»†C",bold=True,before=8)
items=[
 ("1. ","Thá»±c hiá»‡n Há»£p Ä‘á»“ng vÃ  ÄÆ¡n Ä‘áº·t hÃ ng sá»‘ 01, SHT Ä‘Ã£ hoÃ n thÃ nh nháº­p kháº©u hÃ ng hÃ³a vÃ  tá»• chá»©c bÃ n giao theo tiáº¿n Ä‘á»™. Äáº¿n nay, QuÃ½ NgÃ¢n hÃ ng má»›i tiáº¿p nháº­n 1.755/[Sá»_LÆ¯á»¢NG] thiáº¿t bá»‹ POS; sá»‘ cÃ²n láº¡i SHT Ä‘Ã£ sáºµn sÃ ng bÃ n giao nhÆ°ng chÆ°a Ä‘Æ°á»£c tiáº¿p nháº­n."),
 ("2. ","NgÃ y 04/11/2025, SHT cÃ³ vÄƒn báº£n Ä‘á» xuáº¥t bÃ n giao tiáº¿p 1.800 thiáº¿t bá»‹ POS. Äá» xuáº¥t khÃ´ng Ä‘Æ°á»£c QuÃ½ NgÃ¢n hÃ ng tiáº¿p nháº­n."),
 ("3. ","NgÃ y 30/12/2025, SHT tiáº¿p tá»¥c cÃ³ vÄƒn báº£n (thÆ° Ä‘iá»‡n tá»­ cá»§a bÃ  [Há»Œ_TÃŠN_NGÆ¯á»œI_Gá»¬I] gá»­i cÃ¡c Ä‘áº§u má»‘i cÃ³ tháº©m quyá»n cá»§a QuÃ½ NgÃ¢n hÃ ng, kÃ¨m hÃ³a Ä‘Æ¡n nhÃ¡p) Ä‘á» nghá»‹: láº­p hÃ³a Ä‘Æ¡n GTGT Ä‘á»‘i vá»›i 1.755 thiáº¿t bá»‹ Ä‘Ã£ bÃ n giao Ä‘Ãºng thá»i Ä‘iá»ƒm káº¿t thÃºc nÄƒm tÃ i chÃ­nh 2025; pháº§n cÃ²n láº¡i vÃ  hÃ ng khuyáº¿n máº¡i kÃ¨m theo láº­p hÃ³a Ä‘Æ¡n khi bÃ n giao trong nÄƒm 2026."),
 ("4. ","CÃ¹ng ngÃ y 30/12/2025, QuÃ½ NgÃ¢n hÃ ng (thÆ° Ä‘iá»‡n tá»­ cá»§a bÃ  [Há»Œ_TÃŠN_Äáº¦U_Má»I_Äá»I_TÃC]) tá»« chá»‘i viá»‡c láº­p hÃ³a Ä‘Æ¡n nÄƒm 2025; Ä‘á»“ng thá»i Ä‘á» xuáº¥t â€œhá»— trá»£ SHT kÃ½ biÃªn báº£n tá»« chá»‘i nháº­n bÃ n giao Ä‘á»ƒ gá»­i cÆ¡ quan thuáº¿â€. SHT kháº³ng Ä‘á»‹nh khÃ´ng thá»ƒ thá»±c hiá»‡n Ä‘á» xuáº¥t nÃ y, vÃ¬ ná»™i dung biÃªn báº£n khÃ´ng pháº£n Ã¡nh Ä‘Ãºng thá»±c táº¿ giao dá»‹ch vÃ  viá»‡c láº­p há»“ sÆ¡ khÃ´ng Ä‘Ãºng thá»±c táº¿ Ä‘á»ƒ cung cáº¥p cho cÆ¡ quan thuáº¿ lÃ  hÃ nh vi phÃ¡p luáº­t nghiÃªm cáº¥m."),
 ("5. ","NgÃ y [NGÃ€Y], cÆ¡ quan thuáº¿ ban hÃ nh ThÃ´ng bÃ¡o kiá»ƒm tra nÃªu trÃªn. Qua rÃ  soÃ¡t há»“ sÆ¡ nháº­p kháº©u, quáº£n lÃ½ kho vÃ  Há»£p Ä‘á»“ng, cÆ¡ quan thuáº¿ Ä‘Ã£ ghi nháº­n viá»‡c SHT nháº­p kháº©u, xuáº¥t kho bÃ¡n hÃ ng cho [NGÃ‚N_HÃ€NG_A] nhÆ°ng chÆ°a láº­p hÃ³a Ä‘Æ¡n GTGT."),
]
for n,t in items:
    p=para("",first=1.0,after=4); addrun(p,n,bold=True); addrun(p,t)

# ===== II =====
para("II. QUAN ÄIá»‚M PHÃP LÃ Cá»¦A SHT",bold=True,before=8)
for n,t in [
 ("1. ","NghÄ©a vá»¥ láº­p hÃ³a Ä‘Æ¡n Ä‘á»‘i vá»›i 1.755 thiáº¿t bá»‹ Ä‘Ã£ bÃ n giao phÃ¡t sinh táº¡i thá»i Ä‘iá»ƒm chuyá»ƒn giao hÃ ng hÃ³a theo Äiá»u 9 Nghá»‹ Ä‘á»‹nh sá»‘ 123/2020/NÄ-CP, khÃ´ng phá»¥ thuá»™c viá»‡c Ä‘Ã£ thu tiá»n hay chÆ°a vÃ  khÃ´ng phá»¥ thuá»™c Ã½ chÃ­ cá»§a bÃªn mua."),
 ("2. ","NguyÃªn nhÃ¢n trá»±c tiáº¿p dáº«n Ä‘áº¿n viá»‡c chÆ°a láº­p hÃ³a Ä‘Æ¡n Ä‘Ãºng thá»i Ä‘iá»ƒm lÃ  viá»‡c QuÃ½ NgÃ¢n hÃ ng khÃ´ng hoÃ n thÃ nh tiáº¿p nháº­n, nghiá»‡m thu hÃ ng hÃ³a vÃ  tá»« chá»‘i phá»‘i há»£p láº­p hÃ³a Ä‘Æ¡n, máº·c dÃ¹ SHT Ä‘Ã£ hai láº§n chá»§ Ä‘á»™ng Ä‘á» xuáº¥t báº±ng vÄƒn báº£n trong nÄƒm 2025."),
 ("3. ","SHT Ä‘ang lÆ°u giá»¯ Ä‘áº§y Ä‘á»§ vÃ  sáº½ cung cáº¥p cho cÆ¡ quan thuáº¿ toÃ n bá»™ há»“ sÆ¡ chá»©ng minh diá»…n biáº¿n nÃªu trÃªn, bao gá»“m: Há»£p Ä‘á»“ng vÃ  cÃ¡c Phá»¥ lá»¥c; ÄÆ¡n Ä‘áº·t hÃ ng sá»‘ 01; há»“ sÆ¡ nháº­p kháº©u; há»“ sÆ¡ bÃ n giao 1.755 thiáº¿t bá»‹; cÃ¡c thÆ° Ä‘iá»‡n tá»­ trao Ä‘á»•i ngÃ y 04/11/2025 vÃ  30/12/2025 cÃ¹ng hÃ³a Ä‘Æ¡n nhÃ¡p Ä‘Ã­nh kÃ¨m."),
 ("4. ","Sá»± viá»‡c hiá»‡n khÃ´ng cÃ²n lÃ  rá»§i ro hÃ nh chÃ­nh riÃªng cá»§a SHT. Há»“ sÆ¡ thá»ƒ hiá»‡n rÃµ chuá»—i hÃ nh vi vÃ  trÃ¡ch nhiá»‡m cá»§a tá»«ng BÃªn; viá»‡c cháº­m phá»‘i há»£p giáº£i trÃ¬nh chá»‰ lÃ m phÃ¡t sinh thÃªm tiá»n cháº­m ná»™p, má»Ÿ rá»™ng pháº¡m vi kiá»ƒm tra vÃ  báº¥t lá»£i cho cáº£ hai BÃªn."),
]:
    p=para("",first=1.0,after=4); addrun(p,n,bold=True); addrun(p,t)

# ===== III =====
para("III. Äá»€ NGHá»Š",bold=True,before=8)
para("SHT Ä‘á» nghá»‹ Ban LÃ£nh Ä‘áº¡o QuÃ½ NgÃ¢n hÃ ng lá»±a chá»n vÃ  xÃ¡c nháº­n báº±ng vÄƒn báº£n má»™t trong ba phÆ°Æ¡ng Ã¡n sau Ä‘á»ƒ hai BÃªn thá»‘ng nháº¥t phá»‘i há»£p giáº£i trÃ¬nh vá»›i [CÆ _QUAN_THUáº¾]:",first=1.0,after=6)

para("PhÆ°Æ¡ng Ã¡n 1: ",bold=True,first=1.0,after=2)
para("QuÃ½ NgÃ¢n hÃ ng tiáº¿p nháº­n Ä‘á»§ [Sá»_LÆ¯á»¢NG] thiáº¿t bá»‹ POS theo Há»£p Ä‘á»“ng vÃ  ÄÆ¡n Ä‘áº·t hÃ ng Ä‘Ã£ kÃ½; hai BÃªn hoÃ n táº¥t bÃ n giao, nghiá»‡m thu; SHT láº­p hÃ³a Ä‘Æ¡n GTGT cho toÃ n bá»™ hÃ ng hÃ³a Ä‘á»ƒ ná»™p thuáº¿ vÃ o ngÃ¢n sÃ¡ch nhÃ  nÆ°á»›c; QuÃ½ NgÃ¢n hÃ ng chá»‹u 100% tiá»n pháº¡t vi pháº¡m hÃ nh chÃ­nh vÃ  tiá»n cháº­m ná»™p phÃ¡t sinh do hÃ nh vi láº­p hÃ³a Ä‘Æ¡n sai thá»i Ä‘iá»ƒm, vÃ¬ nguyÃªn nhÃ¢n trá»±c tiáº¿p lÃ  viá»‡c cháº­m tiáº¿p nháº­n hÃ ng hÃ³a cá»§a QuÃ½ NgÃ¢n hÃ ng.",first=1.0,after=6)

para("PhÆ°Æ¡ng Ã¡n 2: ",bold=True,first=1.0,after=2)
para("Hai BÃªn hoÃ n táº¥t nghiá»‡m thu 1.755 thiáº¿t bá»‹ POS Ä‘Ã£ bÃ n giao theo Há»£p Ä‘á»“ng, ÄÆ¡n Ä‘áº·t hÃ ng vÃ  há»“ sÆ¡ bÃ n giao Ä‘Ã£ kÃ½; SHT láº­p hÃ³a Ä‘Æ¡n GTGT tÆ°Æ¡ng á»©ng Ä‘á»ƒ ná»™p thuáº¿ vÃ o ngÃ¢n sÃ¡ch nhÃ  nÆ°á»›c; QuÃ½ NgÃ¢n hÃ ng chá»‹u 100% tiá»n pháº¡t vi pháº¡m hÃ nh chÃ­nh vÃ  tiá»n cháº­m ná»™p phÃ¡t sinh do hÃ nh vi láº­p hÃ³a Ä‘Æ¡n sai thá»i Ä‘iá»ƒm. Sá»‘ lÆ°á»£ng cÃ²n láº¡i cá»§a ÄÆ¡n Ä‘áº·t hÃ ng Ä‘Æ°á»£c CÃ¡c BÃªn xá»­ lÃ½ báº±ng thá»a thuáº­n riÃªng.",first=1.0,after=6)

para("PhÆ°Æ¡ng Ã¡n 3: ",bold=True,first=1.0,after=2)
para("NgÆ°á»i Ä‘áº¡i diá»‡n theo phÃ¡p luáº­t cá»§a QuÃ½ NgÃ¢n hÃ ng vÃ  cá»§a SHT cÃ¹ng trÃ¬nh diá»‡n [CÆ _QUAN_THUáº¾] Ä‘á»ƒ trá»±c tiáº¿p giáº£i trÃ¬nh toÃ n bá»™ sá»± viá»‡c, cung cáº¥p há»“ sÆ¡ cá»§a má»—i BÃªn vÃ  ghi nháº­n tÃ¬nh tráº¡ng tranh cháº¥p Há»£p Ä‘á»“ng Ä‘á»ƒ cÆ¡ quan thuáº¿ xem xÃ©t, xá»­ lÃ½ theo quy Ä‘á»‹nh phÃ¡p luáº­t.",first=1.0,after=6)

# ===== IV =====
para("IV. THá»œI Háº N VÃ€ Báº¢O LÆ¯U QUYá»€N",bold=True,before=8)
for n,t in [
 ("1. ","Äá» nghá»‹ QuÃ½ NgÃ¢n hÃ ng cÃ³ vÄƒn báº£n pháº£n há»“i chÃ­nh thá»©c vá» phÆ°Æ¡ng Ã¡n lá»±a chá»n trÆ°á»›c 17h00 ngÃ y 28/8/2026 (05 ngÃ y lÃ m viá»‡c ká»ƒ tá»« ngÃ y CÃ´ng vÄƒn nÃ y Ä‘Æ°á»£c phÃ¡t hÃ nh), gá»­i vá» trá»¥ sá»Ÿ SHT theo Ä‘á»‹a chá»‰ nÃªu táº¡i pháº§n Ä‘áº§u CÃ´ng vÄƒn nÃ y."),
 ("2. ","QuÃ¡ thá»i háº¡n nÃªu trÃªn mÃ  khÃ´ng nháº­n Ä‘Æ°á»£c pháº£n há»“i, SHT sáº½ Ä‘á»™c láº­p giáº£i trÃ¬nh vá»›i cÆ¡ quan thuáº¿ trÃªn cÆ¡ sá»Ÿ toÃ n bá»™ há»“ sÆ¡ thá»±c táº¿ nÃªu táº¡i Má»¥c II, bao gá»“m cáº£ cÃ¡c thÆ° Ä‘iá»‡n tá»­ trao Ä‘á»•i giá»¯a hai BÃªn."),
 ("3. ","SHT báº£o lÆ°u toÃ n bá»™ quyá»n yÃªu cáº§u QuÃ½ NgÃ¢n hÃ ng bá»“i thÆ°á»ng thiá»‡t háº¡i phÃ¡t sinh (tiá»n pháº¡t, tiá»n cháº­m ná»™p, chi phÃ­ giáº£i trÃ¬nh vÃ  cÃ¡c thiá»‡t háº¡i khÃ¡c) vÃ  quyá»n khá»Ÿi kiá»‡n theo Äiá»u 10 Há»£p Ä‘á»“ng cÃ¹ng quy Ä‘á»‹nh phÃ¡p luáº­t cÃ³ liÃªn quan."),
]:
    p=para("",first=1.0,after=4); addrun(p,n,bold=True); addrun(p,t)

para("SHT trÃ¢n trá»ng Ä‘á» nghá»‹ Ban LÃ£nh Ä‘áº¡o QuÃ½ NgÃ¢n hÃ ng quan tÃ¢m, chá»‰ Ä‘áº¡o xá»­ lÃ½. Sá»± viá»‡c chá»‰ cÃ³ thá»ƒ giáº£i quyáº¿t trá»n váº¹n khi hai BÃªn cÃ¹ng thá»±c hiá»‡n Ä‘Ãºng nghÄ©a vá»¥ vá»›i ngÃ¢n sÃ¡ch nhÃ  nÆ°á»›c trÃªn cÆ¡ sá»Ÿ thá»±c táº¿ giao dá»‹ch.",first=1.0,before=6,after=10)

# ===== Sign block =====
tbl2=doc.add_table(rows=1,cols=2); no_borders(tbl2)
tbl2.columns[0].width=Cm(8.0); tbl2.columns[1].width=Cm(8.5)
tbl2.rows[0].cells[0].width=Cm(8.0); tbl2.rows[0].cells[1].width=Cm(8.5)
c0,c1=tbl2.rows[0].cells
cellp(c0,"NÆ¡i nháº­n:",size=12,bold=True,align=WD_ALIGN_PARAGRAPH.LEFT)
for t in ["- NhÆ° trÃªn;","- [CÆ _QUAN_THUáº¾] (Ä‘á»ƒ b/c);","- HÄQT, Ban TGÄ (Ä‘á»ƒ b/c);","- LÆ°u: VT, PhÃ¡p cháº¿."]:
    cellp(c0,t,size=11,italic=True,align=WD_ALIGN_PARAGRAPH.LEFT)
cellp(c1,"CÃ”NG TY Cá»” PHáº¦N Äáº¦U TÆ¯ CÃ”NG NGHá»† SHT",size=12,bold=True)
cellp(c1,"Tá»”NG GIÃM Äá»C",size=13,bold=True)
for _ in range(4): cellp(c1,"",size=13)
cellp(c1,"[Há»Œ_TÃŠN_NGÆ¯á»œI_KÃ]",size=13,bold=True)

out="test.docx"
doc.save(out); print("saved",out)

