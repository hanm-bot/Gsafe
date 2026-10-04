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
cellp(c0,"CÔNG TY CỔ PHẦN",size=12,bold=True)
cellp(c0,"ĐẦU TƯ CÔNG NGHỆ SHT",size=12,bold=True)
p=cellp(c0,"Số:        /2026/CV-SHT",size=13)
cellp(c0,"V/v phối hợp giải trình với cơ quan thuế về nghĩa vụ lập hóa đơn GTGT theo Hợp đồng số 145/2025/HĐNT/VPBANK-SHT",size=11,italic=True)
cellp(c1,"CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM",size=12,bold=True)
cellp(c1,"Độc lập – Tự do – Hạnh phúc",size=13,bold=True)
cellp(c1,"________________________",size=11)
cellp(c1,"Hà Nội, ngày       tháng 8 năm 2026",size=13,italic=True)

para("",after=8)
para("Kính gửi: BAN LÃNH ĐẠO NGÂN HÀNG TMCP VIỆT NAM THỊNH VƯỢNG (VPBANK)",bold=True,align=WD_ALIGN_PARAGRAPH.CENTER,after=10)

# ===== Can cu =====
for t in [
 "Căn cứ Hợp đồng nguyên tắc cung cấp hàng hóa số 145/2025/HĐNT/VPBANK-SHT ký ngày 07/07/2025 giữa Ngân hàng TMCP Việt Nam Thịnh Vượng và Công ty Cổ phần Đầu tư Công nghệ SHT, cùng các Phụ lục Hợp đồng số 01, 02, 03 (sau đây gọi là “Hợp đồng”);",
 "Căn cứ Đơn đặt hàng số 01 với số lượng 4.555 thiết bị POS và bộ hồ sơ bàn giao đã xác lập giữa Các Bên;",
 "Căn cứ Điều 9 Nghị định số 123/2020/NĐ-CP ngày 19/10/2020 của Chính phủ: thời điểm lập hóa đơn đối với bán hàng hóa là thời điểm chuyển giao quyền sở hữu hoặc quyền sử dụng hàng hóa cho người mua, không phân biệt đã thu được tiền hay chưa thu được tiền;",
 "Căn cứ Thông báo số 16342/TB-TCS6-KTr1 ngày 22/5/2026 của Thuế cơ sở 6 Thành phố Hà Nội về kế hoạch kiểm tra tại trụ sở người nộp thuế năm 2026 đối với Công ty Cổ phần Đầu tư Công nghệ SHT (căn cứ Quyết định số 6568/QĐ-HAN-KTr1 ngày 06/5/2026 của Trưởng Thuế TP Hà Nội),",
]:
    para(t,italic=True,first=1.0,after=4)

para("Công ty Cổ phần Đầu tư Công nghệ SHT (sau đây gọi là “SHT”) thông báo và đề nghị Quý Ngân hàng như sau:",first=1.0,before=6)

# ===== I =====
para("I. TÓM TẮT SỰ VIỆC",bold=True,before=8)
items=[
 ("1. ","Thực hiện Hợp đồng và Đơn đặt hàng số 01, SHT đã hoàn thành nhập khẩu hàng hóa và tổ chức bàn giao theo tiến độ. Đến nay, Quý Ngân hàng mới tiếp nhận 1.755/4.555 thiết bị POS; số còn lại SHT đã sẵn sàng bàn giao nhưng chưa được tiếp nhận."),
 ("2. ","Ngày 04/11/2025, SHT có văn bản đề xuất bàn giao tiếp 1.800 thiết bị POS. Đề xuất không được Quý Ngân hàng tiếp nhận."),
 ("3. ","Ngày 30/12/2025, SHT tiếp tục có văn bản (thư điện tử của bà Trần Thanh Huyền gửi các đầu mối có thẩm quyền của Quý Ngân hàng, kèm hóa đơn nháp) đề nghị: lập hóa đơn GTGT đối với 1.755 thiết bị đã bàn giao đúng thời điểm kết thúc năm tài chính 2025; phần còn lại và hàng khuyến mại kèm theo lập hóa đơn khi bàn giao trong năm 2026."),
 ("4. ","Cùng ngày 30/12/2025, Quý Ngân hàng (thư điện tử của bà Dương Thanh Thúy) từ chối việc lập hóa đơn năm 2025; đồng thời đề xuất “hỗ trợ SHT ký biên bản từ chối nhận bàn giao để gửi cơ quan thuế”. SHT khẳng định không thể thực hiện đề xuất này, vì nội dung biên bản không phản ánh đúng thực tế giao dịch và việc lập hồ sơ không đúng thực tế để cung cấp cho cơ quan thuế là hành vi pháp luật nghiêm cấm."),
 ("5. ","Ngày 22/5/2026, cơ quan thuế ban hành Thông báo kiểm tra nêu trên. Qua rà soát hồ sơ nhập khẩu, quản lý kho và Hợp đồng, cơ quan thuế đã ghi nhận việc SHT nhập khẩu, xuất kho bán hàng cho VPBank nhưng chưa lập hóa đơn GTGT."),
]
for n,t in items:
    p=para("",first=1.0,after=4); addrun(p,n,bold=True); addrun(p,t)

# ===== II =====
para("II. QUAN ĐIỂM PHÁP LÝ CỦA SHT",bold=True,before=8)
for n,t in [
 ("1. ","Nghĩa vụ lập hóa đơn đối với 1.755 thiết bị đã bàn giao phát sinh tại thời điểm chuyển giao hàng hóa theo Điều 9 Nghị định số 123/2020/NĐ-CP, không phụ thuộc việc đã thu tiền hay chưa và không phụ thuộc ý chí của bên mua."),
 ("2. ","Nguyên nhân trực tiếp dẫn đến việc chưa lập hóa đơn đúng thời điểm là việc Quý Ngân hàng không hoàn thành tiếp nhận, nghiệm thu hàng hóa và từ chối phối hợp lập hóa đơn, mặc dù SHT đã hai lần chủ động đề xuất bằng văn bản trong năm 2025."),
 ("3. ","SHT đang lưu giữ đầy đủ và sẽ cung cấp cho cơ quan thuế toàn bộ hồ sơ chứng minh diễn biến nêu trên, bao gồm: Hợp đồng và các Phụ lục; Đơn đặt hàng số 01; hồ sơ nhập khẩu; hồ sơ bàn giao 1.755 thiết bị; các thư điện tử trao đổi ngày 04/11/2025 và 30/12/2025 cùng hóa đơn nháp đính kèm."),
 ("4. ","Sự việc hiện không còn là rủi ro hành chính riêng của SHT. Hồ sơ thể hiện rõ chuỗi hành vi và trách nhiệm của từng Bên; việc chậm phối hợp giải trình chỉ làm phát sinh thêm tiền chậm nộp, mở rộng phạm vi kiểm tra và bất lợi cho cả hai Bên."),
]:
    p=para("",first=1.0,after=4); addrun(p,n,bold=True); addrun(p,t)

# ===== III =====
para("III. ĐỀ NGHỊ",bold=True,before=8)
para("SHT đề nghị Ban Lãnh đạo Quý Ngân hàng lựa chọn và xác nhận bằng văn bản một trong ba phương án sau để hai Bên thống nhất phối hợp giải trình với Thuế Thành phố Hà Nội:",first=1.0,after=6)

para("Phương án 1: ",bold=True,first=1.0,after=2)
para("Quý Ngân hàng tiếp nhận đủ 4.555 thiết bị POS theo Hợp đồng và Đơn đặt hàng đã ký; hai Bên hoàn tất bàn giao, nghiệm thu; SHT lập hóa đơn GTGT cho toàn bộ hàng hóa để nộp thuế vào ngân sách nhà nước; Quý Ngân hàng chịu 100% tiền phạt vi phạm hành chính và tiền chậm nộp phát sinh do hành vi lập hóa đơn sai thời điểm, vì nguyên nhân trực tiếp là việc chậm tiếp nhận hàng hóa của Quý Ngân hàng.",first=1.0,after=6)

para("Phương án 2: ",bold=True,first=1.0,after=2)
para("Hai Bên hoàn tất nghiệm thu 1.755 thiết bị POS đã bàn giao theo Hợp đồng, Đơn đặt hàng và hồ sơ bàn giao đã ký; SHT lập hóa đơn GTGT tương ứng để nộp thuế vào ngân sách nhà nước; Quý Ngân hàng chịu 100% tiền phạt vi phạm hành chính và tiền chậm nộp phát sinh do hành vi lập hóa đơn sai thời điểm. Số lượng còn lại của Đơn đặt hàng được Các Bên xử lý bằng thỏa thuận riêng.",first=1.0,after=6)

para("Phương án 3: ",bold=True,first=1.0,after=2)
para("Người đại diện theo pháp luật của Quý Ngân hàng và của SHT cùng trình diện Thuế Thành phố Hà Nội để trực tiếp giải trình toàn bộ sự việc, cung cấp hồ sơ của mỗi Bên và ghi nhận tình trạng tranh chấp Hợp đồng để cơ quan thuế xem xét, xử lý theo quy định pháp luật.",first=1.0,after=6)

# ===== IV =====
para("IV. THỜI HẠN VÀ BẢO LƯU QUYỀN",bold=True,before=8)
for n,t in [
 ("1. ","Đề nghị Quý Ngân hàng có văn bản phản hồi chính thức về phương án lựa chọn trước 17h00 ngày 28/8/2026 (05 ngày làm việc kể từ ngày Công văn này được phát hành), gửi về trụ sở SHT theo địa chỉ nêu tại phần đầu Công văn này."),
 ("2. ","Quá thời hạn nêu trên mà không nhận được phản hồi, SHT sẽ độc lập giải trình với cơ quan thuế trên cơ sở toàn bộ hồ sơ thực tế nêu tại Mục II, bao gồm cả các thư điện tử trao đổi giữa hai Bên."),
 ("3. ","SHT bảo lưu toàn bộ quyền yêu cầu Quý Ngân hàng bồi thường thiệt hại phát sinh (tiền phạt, tiền chậm nộp, chi phí giải trình và các thiệt hại khác) và quyền khởi kiện theo Điều 10 Hợp đồng cùng quy định pháp luật có liên quan."),
]:
    p=para("",first=1.0,after=4); addrun(p,n,bold=True); addrun(p,t)

para("SHT trân trọng đề nghị Ban Lãnh đạo Quý Ngân hàng quan tâm, chỉ đạo xử lý. Sự việc chỉ có thể giải quyết trọn vẹn khi hai Bên cùng thực hiện đúng nghĩa vụ với ngân sách nhà nước trên cơ sở thực tế giao dịch.",first=1.0,before=6,after=10)

# ===== Sign block =====
tbl2=doc.add_table(rows=1,cols=2); no_borders(tbl2)
tbl2.columns[0].width=Cm(8.0); tbl2.columns[1].width=Cm(8.5)
tbl2.rows[0].cells[0].width=Cm(8.0); tbl2.rows[0].cells[1].width=Cm(8.5)
c0,c1=tbl2.rows[0].cells
cellp(c0,"Nơi nhận:",size=12,bold=True,align=WD_ALIGN_PARAGRAPH.LEFT)
for t in ["- Như trên;","- Thuế cơ sở 6 TP Hà Nội (để b/c);","- HĐQT, Ban TGĐ (để b/c);","- Lưu: VT, Pháp chế."]:
    cellp(c0,t,size=11,italic=True,align=WD_ALIGN_PARAGRAPH.LEFT)
cellp(c1,"CÔNG TY CỔ PHẦN ĐẦU TƯ CÔNG NGHỆ SHT",size=12,bold=True)
cellp(c1,"TỔNG GIÁM ĐỐC",size=13,bold=True)
for _ in range(4): cellp(c1,"",size=13)
cellp(c1,"Nguyễn Quang Việt",size=13,bold=True)

# Đường dẫn ra: đối số thứ nhất, mặc định thư mục hiện hành. Bản gốc ghi cứng thư mục sandbox Cowork
# (/sessions/.../mnt/outputs) nên chạy ngoài Cowork là FileNotFoundError (QA task-06, 05/10/2026).
import sys, os
out=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.getcwd(),"CV_SHT_gui_VPBank_Phoi_hop_giai_trinh_thue.docx")
doc.save(out); print("saved",out)
