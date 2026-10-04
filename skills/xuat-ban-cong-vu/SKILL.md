---
name: xuat-ban-cong-vu
description: "Dựng và chuyển đổi file văn phòng bằng code: Word, PowerPoint, Excel, PDF theo bộ nhận diện thương hiệu. LUÔN dùng khi cần tạo slide, bảng tính, tài liệu thương hiệu, chuyển đổi/cắt ghép PDF. KHÔNG dùng cho văn bản hành chính hay docx giao anh Hà theo NĐ30 (sht-nen-tang-kiem-chung), trích chứng cứ PDF scan (chuan-hoa-ho-so-tai-lieu). (dựa trên vietduc·ai)"
---

# AI Office Master 2.0 (Bi-directional Pipeline & Multi-Skill Orchestrator)
### Đơn vị phát triển: Hệ Thống AI Workforce Doanh Nghiệp

> **Tuyên ngôn**: Không bao giờ chỉnh sửa chắp vá trên file cũ bị lỗi rác format. Hệ thống hoạt động theo **Kiến trúc Song song 2 Chiều (Extractor & Generator)**: Chiều Đọc bóc tách Dữ liệu & Brand DNA từ file mẫu cũ; Chiều Ghi vẽ lại hoàn toàn sạch 100% bằng Code, tích hợp tự động với chuỗi giải pháp của Hệ Thống AI Workforce.

---

## 1. Nguyên Lý Vận Hành 2 Chiều (Bi-directional Architecture)

Mọi tài liệu đi qua hệ thống đều được phân tách rành mạch thành Tầng Dữ Liệu (Content) và Tầng Hiển Thị (UI/Theme).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    KIẾN TRÚC SONG SONG 2 CHIỀU (PIPELINE)                    │
├──────────────────────────────────────┬──────────────────────────────────────┤
│     CHIỀU ĐỌC (THE EXTRACTOR)        │       CHIỀU GHI (THE GENERATOR)      │
│            (Python / XML)            │         (Node.js & Python)           │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ 1. Content: Cào text, số, bảng biểu  │ 1. Global Styles: Nạp brand_kit.json │
│    (markitdown, openpyxl, pdfplumber)│    hoặc chuẩn NĐ 30 vào Document.    │
│ 2. Brand Kit: Chạy extract_brand.py  │ 2. Tái tạo Assets: Nhúng logo, vẽ lại│
│    đọc theme1.xml xuất brand_kit.json│    biểu đồ sống (không dán ảnh chết).│
│ 3. Assets: Trích ảnh/logo từ media/  │ 3. Đổ Content: Nạp nội dung biên tập │
│    bóc số liệu biểu đồ (chống ảnh)   │    vào khung đã chuẩn hóa Brand DNA. │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

---

## 2. Cổng Tiếp Nhận Thông Minh & Đường Ray Đôi (Dual-Track)

Trước khi tạo file, Agent xác định luồng thực thi dựa trên đầu vào của người dùng hoặc khối Payload:

```
════════════════════════════════════════════════════════════════════════════════
   VIETDUC.AI — NHÀ MÁY XUẤT BẢN TÀI LIỆU VĂN PHÒNG CHUYÊN NGHIỆP
════════════════════════════════════════════════════════════════════════════════
[1] CHUẨN HÀNH CHÍNH QUỐC GIA (NGHỊ ĐỊNH 30/2020/NĐ-CP)
    → Công văn, Tờ trình, Quyết định, Báo cáo cơ quan nhà nước.
    → Đen/Trắng tuyệt đối, font Times New Roman, lề chuẩn (Trái 3, Phải 1.5, Trên/Dưới 2).
    → Cấm tuyệt đối Brand Kit hay màu mè. Dùng templates/docx-hanh-chinh-*.md.

[2] CHUẨN THẨM MỸ DOANH NGHIỆP HIỆN ĐẠI (BRAND KIT TRACK)
    → Đề án, Kế hoạch kinh doanh, Báo cáo tài chính, Slide thuyết trình (Pitch Deck).
    → Áp dụng 1 trong 10 bộ Brand Kit chuẩn quốc tế (Formal Navy, Dark Tech, Luxury Gold...)
    → Bảng zebra striping, Callout box nhấn mạnh, biểu đồ sống, bố cục hiện đại.

[3] BÓC TÁCH FORMAT FILE MẪU CỦA DOANH NGHIỆP (EXTRACTOR ONLY)
    → Phân tích file mẫu cũ của khách hàng, số hóa thành brand_kit.json và thư viện assets/.
────────────────────────────────────────────────────────────────────────────────
👉 Tự động kích hoạt: Nếu người dùng gửi kèm [LEGAL_HANDOVER_PAYLOAD] hoặc
   [MARKET_HANDOVER_PAYLOAD], hệ thống sẽ tự động phân loại và xuất bản trọn bộ!
════════════════════════════════════════════════════════════════════════════════
```

---

## 3. Cỗ Máy Tự Động Bắt Payload Từ Hệ Sinh Thái (Ecosystem Ingestion)

Đây là điểm nâng cấp đột phá, kết nối `xuat-ban-cong-vu` với 3 kỹ năng còn lại:

### 3.1. Bắt Khối `[LEGAL_HANDOVER_PAYLOAD]` (từ `phap-che-doanh-nghiep`):
- **Word NĐ 30:** Tự động lấy mảng `legal_basis_citations` điền vào phần *"Căn cứ..."* đầu Tờ trình / Quyết định; điền `substantive_clauses` vào các điều khoản quy định.
- **Excel:** Tự động tạo Sheet 2 *"Checkpoint Tuân thủ Pháp lý"* và Sheet 3 *"Ma trận Lượng hóa Rủi ro"*.
- **PowerPoint:** Tự động tạo Slide *"Phòng tuyến Pháp lý & Chứng cứ Bảo vệ"*.

### 3.2. Bắt Khối `[MARKET_HANDOVER_PAYLOAD]` (từ `tham-dinh-thi-truong`):
- **Word Đề án:** Điền phân tích cơ hội thị trường, 8 lăng kính nhu cầu, khoảng trống ngách (Niche Vacuum) vào Thuyết minh đề án.
- **Excel Unit Economics:** Đổ bảng giá Value-based, dự toán doanh thu 12 tháng, điểm hòa vốn (Break-even) với công thức sống (`SUM`, `AVERAGE`, `IF`).
- **PowerPoint Pitch Deck:** Đổ cấu trúc 7 slide (Problem $\to$ Market Gap $\to$ Solution $\to$ Business Model $\to$ Traction $\to$ Financials $\to$ Ask).

### 3.3. Bắt Kế hoạch từ `kien-truc-tai-lieu`:
- Đồng bộ cấu trúc cây thông tin động (Adaptive Information Tree) vào các cấp Heading của văn bản.

---

## 4. Bộ Chuyển Đổi "Văn Nói Đời Thường" ──► Thể Thức Chuẩn Mực

Học viên chỉ cần nói bằng ngôn ngữ giao tiếp hằng ngày, Agent tự động nhận diện và đề xuất chuẩn hóa:

| Văn Nói Của Học Viên / Người Dùng | Agent Tự Động Quy Chuẩn | Định Dạng Đầu Ra Đề Xuất |
|---|---|---|
| "Sếp bắt làm văn bản xin tiền mua 10 cái máy tính mới" | **Tờ trình xin phê duyệt chủ trương và kinh phí mua sắm** | DOCX Chuẩn NĐ 30 (`templates/docx-hanh-chinh-to-trinh.md`) |
| "Gửi văn bản thông báo cho đối tác nhắc họ trả nợ" | **Công văn đôn đốc thực hiện nghĩa vụ thanh toán** | DOCX Chuẩn NĐ 30 (`templates/docx-hanh-chinh-cong-van.md`) |
| "Lập kế hoạch doanh thu năm nay cho công ty 1 người" | **Mô hình tài chính & Dự toán Unit Economics 4 Sheet** | XLSX Live Formula (`standards/dynamic_structure/xlsx-structure.md`) |
| "Làm slide báo cáo ban giám đốc về dự án chuyển đổi số" | **Executive Pitch Deck 7 Slide chuyên nghiệp** | PPTX Brand Kit (`standards/brand_kits/preset-formal-navy`) |

---

## 5. Thư Viện 10 Brand Kits Doanh Nghiệp Chuẩn Quốc Tế

Khi xuất bản theo **Track 2 (Doanh nghiệp)**, Agent chủ động đề xuất hoặc nhận diện 1 trong 10 bộ màu chuẩn trong `standards/brand_kits/`:

1. `preset-formal-navy`: Xanh navy đậm & Vàng gold nhạt — Uy tín, ngân hàng, luật, tài chính.
2. `preset-modern-blue`: Xanh dương công nghệ & Xám bạc — Phần mềm, AI, CNTT, viễn thông.
3. `preset-dark-tech`: Nền tối than chì & Xanh neon/cyan — Khởi nghiệp công nghệ, Web3, hacker.
4. `preset-luxury-dark-gold`: Đen tuyền & Ánh kim đồng — Bất động sản cao cấp, trang sức, VIP.
5. `preset-fresh-nature`: Xanh lá rừng & Xanh bạc hà — Nông nghiệp sạch, y tế, môi trường, ESG.
6. `preset-vibrant-coral`: Cam san hô & Đỏ hoàng hôn — Thương mại điện tử, F&B, thời trang trẻ.
7. `preset-editorial-burgundy`: Đỏ rượu vang & Kem cổ điển — Báo chí, xuất bản, học viện, giáo dục.
8. `preset-warm-earth`: Nâu đất nung & Cát ấm — Kiến trúc, nội thất, thủ công mỹ nghệ.
9. `preset-neutral-minimal`: Đen carbon & Trắng xám tối giản — Thiết kế, kiến trúc sư, studio.
10. `preset-classic-ivory`: Xanh chàm & Giấy ngà truyền thống — Doanh nghiệp gia đình, hành chính cao cấp.

---

## 6. Chiến Lược Thực Thi Kỹ Thuật (Dual-Engine Execution)

Để đảm bảo tài liệu được sinh ra hoàn hảo trên mọi môi trường:

### Môi trường 1: Máy tính cá nhân / Antigravity IDE (Đã có sẵn Node.js & Python)
- **Track 1 (NĐ 30):** Sử dụng template markdown + script format Pandoc/Python (`scripts/extractor/format/format_docx.py`) hoặc Node.js để xuất file `.docx` đúng từng milimet lề và font.
- **Track 2 (Brand Kit):** Sử dụng các script trong `scripts/generator/` (`template_docx.js`, `template_xlsx.js`, `template_pptx.js`) với các thư viện `docx`, `exceljs`, `pptxgenjs`.
- **Chỉnh sửa giữ format:** Dùng toolkit XML unpack/pack (`scripts/extractor/office/unpack.py` & `pack.py`).

### Môi trường 2: Claude Web / Cowork Sandbox (Không có node modules toàn cục)
- Tự động chuyển đổi sang **Python Fallback Engine**:
  - Dùng `python-docx` để dựng file Word với bảng styles chuẩn.
  - Dùng `openpyxl` để dựng file Excel với Live Formula và định dạng màu ô.
  - Dùng `python-pptx` để dựng file Slide với layout tỷ lệ 16:9 sắc nét.
  $\implies$ **Đảm bảo 100% người dùng tải được file hoàn chỉnh về máy.**

---

## 7. Bộ Lọc Khử Dấu Vết AI Trong Văn Phong (Anti-AI Punctuation & Style)

Văn bản chuyên nghiệp tuyệt đối không được có dấu vết "văn máy". Áp dụng nghiêm ngặt các quy tắc:
1. **Cấm tuyệt đối dấu gạch ngang dài (em dash `—`):** Thay bằng gạch ngang tiêu chuẩn có khoảng trắng ` - ` hoặc dùng từ nối văn bản.
2. **Cấm dấu hai chấm tùy tiện trong tiêu đề:** Tiêu đề phải là một cụm danh từ hoặc mệnh đề gãy gọn, không dùng dạng `"Kế hoạch: Giải pháp ABC"`.
3. **Cấm dấu phẩy Oxford kiểu tiếng Anh (`, và`):** Thay bằng `"và"` chuẩn ngữ pháp tiếng Việt.
4. **Kiểm tra sau xuất xưởng:** Số lượng `—`, `, và` trong toàn bộ văn bản phải bằng 0.

---

## 8. Nguyên Tắc Kiểm Soát Chất Lượng Tuyệt Đối (QA Gate)

1. ✅ Đã xác nhận rõ Track 1 (Hành chính NĐ 30 đen trắng) hay Track 2 (Doanh nghiệp Brand Kit)?
2. ✅ Track 1: Đúng lề Trái 3cm, Phải 1.5cm, Trên 2cm, Dưới 2cm; Font Times New Roman; Header Quốc hiệu 2 cột?
3. ✅ Track 2: Đã nạp đúng `brand_kit.json` (không hardcode màu bừa bãi); Đạt độ tương phản WCAG?
4. ✅ Mọi ô tính toán trong Excel đều dùng Live Formula (cấm điền số chết)?
5. ✅ Sơ đồ và biểu đồ được vẽ lại dạng sống (cấm chụp màn hình dán ảnh chết)?
6. ✅ Đã khử sạch dấu vết AI (`—`, `, và`, `:` trong heading)?
7. ✅ File xuất xưởng mở được ngay trên Microsoft Office (Word, Excel, PowerPoint) không bị lỗi XML?

---

## 9. Tác Giả & Bản Quyền

**Hệ Thống AI Workforce Doanh Nghiệp (vietduc·ai)**  
Chuyên gia Đào tạo & Chuyển giao Giải pháp Tự động hóa AI Doanh nghiệp  
Hệ sinh thái: **vietduc.ai**
