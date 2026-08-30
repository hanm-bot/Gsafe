# Định dạng chuẩn Quyết định nhân sự/tổ chức — SHT

Đối chiếu từ 3 văn bản thật: QĐ 050326-QĐ/SHT-01 (phân giao KPI), QĐ 010626/QĐ-SHT (bổ nhiệm Lê Quang Tuấn), QĐ 110326/QĐ-SHT (bổ nhiệm Nguyễn Thanh Tùng).

## Cấu trúc chung

1. Bảng 2 cột không viền: trái = Công ty + số hiệu QĐ (format `ddmmyy/QĐ-SHT`, không dấu gạch trước QĐ, không hậu tố trừ khi cùng ngày có nhiều QĐ thì thêm `-02`, `-03`...); phải = Quốc hiệu tiêu ngữ + ngày tháng.
2. Tiêu đề "QUYẾT ĐỊNH" (in đậm, giữa trang) + dòng "V/v: ..." (in đậm, giữa trang).
3. Các dòng "Căn cứ ..." (in nghiêng, không đánh số, mỗi dòng bắt đầu bằng gạch đầu dòng "-").
4. Các Điều, đánh số La Mã kiểu "Điều 1.", "Điều 2."... Nội dung chi tiết trong mỗi Điều đánh số 1, 2, 3... thụt lề trái.
5. Điều cuối luôn nêu: đơn vị chịu trách nhiệm thi hành + "Quyết định này có hiệu lực kể từ ngày ký" + (nếu thay thế QĐ cũ) "và thay thế toàn bộ Quyết định số ... ngày ...".
6. Bảng 2 cột không viền cuối văn bản: trái = "Nơi nhận:" (in nghiêng, gồm "Như trên;" và "Lưu HCNS, TCKT."); phải = Tên công ty + "TM. HỘI ĐỒNG QUẢN TRỊ" (in đậm, giữa, chừa khoảng trống ký tên).

## Các cấu phần Điều thường gặp (tùy loại QĐ)

- **Bổ nhiệm chức vụ + nhiệm vụ chính** — luôn có, đánh số 1..n nhiệm vụ.
- **Quyền hạn** — chỉ xuất hiện ở QĐ cấp quản lý cao hơn 1 cấp thuần túy (VD Khối trưởng), không cần ở QĐ Giám đốc đơn vị thường.
- **Thời gian thử thách/thử việc** — xuất hiện ở hầu hết QĐ bổ nhiệm mới; nêu rõ số tháng, ai theo dõi đánh giá, ai quyết định chính thức hóa. Nếu là QĐ thay thế cho người đang tại vị, phải nêu rõ mốc tính tiếp từ ngày nào, không tính lại từ đầu.
- **Quan hệ báo cáo & trách nhiệm cá nhân** — bắt buộc nêu rõ báo cáo cho ai, chịu trách nhiệm cá nhân trước ai (có thể vừa báo cáo cấp trung gian vừa giữ trách nhiệm cá nhân trước BLĐ — không mâu thuẫn nếu nêu rõ cả hai).
- **Thi hành & hiệu lực** — luôn là Điều cuối.

## Boilerplate code (Node.js, thư viện `docx`)

```javascript
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, VerticalAlign
} = require("docx");

const FONT = "Times New Roman";
const noBorder = {
  top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
};

function p(opts) {
  return new Paragraph({
    alignment: opts.align || AlignmentType.LEFT,
    spacing: { after: opts.after !== undefined ? opts.after : 120, line: 300 },
    indent: opts.indent,
    children: (opts.runs || [{ text: opts.text || "" }]).map(r => new TextRun({
      text: r.text, bold: r.bold || false, italics: r.italics || false, font: FONT, size: r.size || 24,
    })),
  });
}

// Bảng header: 2 cột, mỗi cột width 4819 DXA (tổng 9638 DXA ~ A4 trừ margin)
// Cột trái: Công ty (bold) + gạch ngang + Số hiệu
// Cột phải: Quốc hiệu (bold) + Tiêu ngữ (bold) + gạch ngang + ngày tháng (italic)

// Bảng footer: 2 cột, trái 3200 DXA "Nơi nhận" (italic), phải 6438 DXA
// tên công ty (bold, giữa) + "TM. HỘI ĐỒNG QUẢN TRỊ" (bold, giữa) + khoảng trống ký tên

// Xem file build.js của QĐ Bổ nhiệm CCO / QĐ Bổ nhiệm lại GĐ TTKD trong lịch sử làm việc
// để lấy full code mẫu — cấu trúc header/footer table giống hệt nhau giữa các QĐ,
// chỉ phần "children" nội dung giữa 2 bảng là thay đổi theo từng Điều.
```

## Quy trình render kiểm tra bố cục

```bash
soffice --headless --convert-to pdf <file>.docx
pdftoppm -jpeg -r 110 <file>.pdf page
```
Sau đó `view` từng ảnh `page-1.jpg`, `page-2.jpg`... trước khi copy sang `/mnt/user-data/outputs/` và gọi `present_files`.
