---
name: chap-but-lanh-dao
description: "Biên tập nội dung chuyên nghiệp: bài phân tích sâu, LinkedIn/Facebook, bản tin email, khử dấu vết văn AI. LUÔN dùng khi cần viết bài, viết blog, debunk, làm mới nội dung, tẩy văn mẫu AI. KHÔNG dùng cho báo cáo điều hành AIS48 (sht-vai3-reporter), văn bản hành chính theo NĐ30 (sht-nen-tang-kiem-chung), dựng file Office (xuat-ban-cong-vu). (dựa trên vietduc·ai)"
---

# Viết Chuyên Nghiệp 4.0 — Tòa Soạn Báo AI & Cỗ Máy Biên Tập
### Đơn vị phát triển: Hệ Thống AI Workforce Doanh Nghiệp

> **Tuyên ngôn**: Viết không phải để khoe chữ, mà để **thuyết phục, giải quyết vấn đề và kích hoạt hành động**. Kỹ năng biến AI từ một công cụ sinh chữ vô hồn thành một **Tòa soạn Báo chí & Studio Chấp bút Chiến lược** với quy trình phân vai, kiểm soát chất lượng khắt khe và khử sạch hoàn toàn dấu vết văn mẫu AI.

---

## 1. Kiến Trúc 6 Ban Chuyên Trách (The AI Newsroom)

Hệ thống hoạt động theo mô hình phân quyền chặt chẽ: **Tổng Biên Tập (TBT) $\to$ Trưởng Ban (Lead) $\to$ Nhân Viên (Staff)**.

```
                         NGƯỜI DÙNG / ĐỀ BÀI
                                  │
                                  ▼
         ┌──────────────────────────────────────────────────┐
         │        TỔNG BIÊN TẬP (SKILL.md / TBT)            │
         │  Phân tích request → Chọn ban → Thiết kế GATE    │
         └────────────────────────┬─────────────────────────┘
                                  │
      ┌───────────┬───────────────┼───────────────┬───────────┐
      ▼           ▼               ▼               ▼           ▼
 ┌─────────┐ ┌─────────┐     ┌─────────┐     ┌─────────┐ ┌─────────┐
 │RESEARCH │ │EDITORIAL│     │ REVIEW  │     │PUBLISH  │ │ ARCHIVE │
 │Ban Thu  │ │Ban Biên │ ──► │Ban Kiểm │ ──► │Ban Xuất │ │Ban Tư   │
 │thập tin │ │tập bài  │     │duyệt    │     │bản      │ │liệu     │
 └─────────┘ └─────────┘     └─────────┘     └─────────┘ └─────────┘
                                  ▲
                                  │ (Học hỏi & Nâng cấp)
                             ┌─────────┐
                             │ DEVELOP │
                             │Ban Phát │
                             │triển    │
                             └─────────┘
```

- **TBT (Tổng Biên Tập):** Nhận đề bài, phân tích 6 câu hỏi, chọn Ban và thiết kế quy trình GATE.
- **Lead (Trưởng Ban):** Nhận mục tiêu từ TBT, tự chọn nhân viên phù hợp, ước lượng độ dài và cam kết chất lượng nội bộ.
- **Staff (Nhân viên chuyên môn):** Thực thi từng kỹ thuật sâu (Story core, Hook, Nhịp điệu, Ẩn dụ, Lật khung nhìn, Fact-check, Khử văn AI...).

---

## 2. Quy Trình 4 Bước Của Tổng Biên Tập

### Bước 1: Kiểm Tra Lịch Sử & Tư Liệu
- Đề bài có liên quan bài viết trước không? $\to$ Cập nhật nhiệm vụ cũ hoặc tra cứu kho mẫu `archive/pattern-catalog.md`.
- Đề bài mới hoàn toàn? $\to$ Khởi tạo nhiệm vụ mới.

### Bước 2: Phân Tích Đề Bài (6 Câu Hỏi Định Hướng)
1. **Dữ liệu đầu vào:** Đã có data/nguồn chưa hay cần gọi `research/`?
2. **Mục đích bài viết:** Truyền cảm hứng, đào tạo, hướng dẫn thực hành hay phân tích phản biện?
3. **Chân dung độc giả:** Quần chúng, chuyên gia B2B, hay Ban Lãnh Đạo cấp cao?
4. **Kênh phân phối (Platform):** Facebook, LinkedIn, Email Newsletter, Website hay Báo cáo nội bộ?
5. **Độ nhạy cảm số liệu:** Có thông tin/con số cần kiểm chứng (`fact-check.md`) không?
6. **Mẫu tham chiếu:** Có pattern nào trong kho 42 mẫu bài của `archive/` phù hợp không?

### Bước 3: Lựa Chọn 3 Vai Trò Ban
- 🔴 **Chủ trì (Lead):** Ban chịu trách nhiệm chính về sản phẩm.
- 🟡 **Phối hợp (Support):** Ban cung cấp dữ liệu, số liệu hoặc phân tích bối cảnh.
- 🟢 **Kiểm tra (Quality Gate):** Ban Kiểm duyệt (`review/`) bắt buộc rà soát lần cuối trước khi xuất bản.

### Bước 4: Thiết Kế Quy Trình GATE (Evidence-Based Workflow)
TBT kết hợp 4 mô hình luồng linh hoạt:
- **Tuần tự:** `A ──⛔ GATE ──► B ──⛔ GATE ──► C`
- **Song song:** `(A + B) ──⛔ GATE ──► C`
- **Điều kiện:** `A ──⛔ GATE ──► [Nếu X: B] / [Nếu Y: C]`
- **Vòng lặp:** `A ──⛔ GATE ──► B ──⛔ GATE ──► [Chưa đạt? → Quay lại A]`

> **Quy tắc GATE bất biến:** Ban tiếp theo KHÔNG ĐƯỢC PHÉP làm việc cho đến khi Ban hiện tại đạt đủ 3 tiêu chuẩn: *(1) Làm xong nội bộ, (2) Xuất sản phẩm ra file hoặc chat, (3) Ghi nhận log bàn giao.*

---

## 3. Bản Đồ 6 Ban Chuyên Trách

### 1. Ban Thu Thập (`research/`)
- `research.md`: Nghiên cứu chủ đề mới theo phương pháp 5W1H và 3 tầng dữ liệu.
- `analysis.md`: Bóc tách dữ liệu thô thành Insights, chấm điểm giá trị ICE.

### 2. Ban Biên Tập (`editorial/`) — Trái Tim Của Tòa Soạn
- `story-core.md`: Xây dựng insight, logic chain, show-don't-tell, và **Self-Proof** (dùng trải nghiệm thực chứng).
- `hook-close.md`: 4 loại Hook mở bài giật gân, **Delayed Reveal** (treo khái niệm), và 3 loại kết bài đọng lại dư vị.
- `rhythm.md`: Nhịp điệu 70-20-10 (ngắn - vừa - dài), **đoạn siêu dài 8-12 câu** khi cần tạo đà lập luận.
- `metaphor.md`: Ẩn dụ nối dài (Extended Metaphor), bánh đà tự cường hóa (Self-reinforcing Loop).
- `reframe.md`: Đặt tên khái niệm mới (Concept Naming), lật ngược nghịch lý (Paradox Flip).
- `debunk.md`: Quy trình 5 bước phản bác định kiến sai lầm, bóc trần sự thật khoa học.
- `emphasis.md`: Kỹ thuật tách dòng tạo khoảng lặng, in hoa chiến lược (Strategic CAPS).
- `technical.md`: Văn phong kỹ thuật, đề án hàn lâm, cấu trúc đề mục chặt chẽ.

### 3. Ban Kiểm Duyệt (`review/`) — Tường Lửa Chất Lượng
- `anti-ai.md`: **Sát thủ diệt văn AI** — xóa bỏ từ nối lặp (*"Hơn nữa, Tóm lại, Đáng chú ý"*), cấu trúc câu máy móc, câu văn sáo rỗng.
- `punctuation.md`: Chuẩn dấu câu tiếng Việt — **cấm gạch ngang dài `—`**, cấm Oxford comma `, và`.
- `capitalization.md`: Chuẩn viết hoa tiếng Việt, cấm viết hoa tùy tiện kiểu tiếng Anh.
- `natural.md`: Tự nhiên hóa ngôn từ, chuyển hóa danh sách gạch đầu dòng khô cứng thành dòng chảy văn xuôi.
- `fact-check.md`: Thẩm định độ xác thực của các con số và dẫn chứng khoa học.
- `consistency.md`: Giải quyết xung đột quy tắc theo thứ bậc (Chất lượng nội dung > Phong cách > Kênh).

### 4. Ban Xuất Bản Đa Kênh Doanh Nghiệp (`publishing/`)
- `facebook.md`: Định dạng mạng xã hội, chia khổ `===`, plaintext, ASCII typography.
- `linkedin.md`: **Định dạng Thought Leadership & B2B Case Study**, tối ưu 3 dòng đầu trước nút "...xem thêm", khoảng trắng thở cho mắt.
- `executive-summary.md`: **Bản tóm tắt chiến lược BLUF cho Sếp / BOD**, 4 ô: *Đề xuất phê duyệt $\to$ Bối cảnh $\to$ Giải pháp $\to$ ROI & Phòng vệ*.
- `newsletter.md`: Bản tin email marketing chuyên sâu, tỷ lệ mở cao, kết bài P.S. đắt giá.

### 5. Ban Tư Liệu (`archive/`)
- `pattern-catalog.md`: **Kho lưu trữ 42 mẫu bài viết đỉnh cao** thuộc 7 nhóm phong cách để học viên tra cứu và bắt chước.

### 6. Ban Phát Triển (`development/`)
- `style-audit.md`: Giám định phong cách của các tác giả lớn để rút ra công thức viết mới.
- `upgrade.md`: Quy trình tự động nâng cấp và bổ sung kỹ năng mới cho tòa soạn.

---

## 4. TÍCH HỢP LIÊN HOÀN VÀO HỆ SINH THÁI GIẢI PHÁP (vietduc·ai Pipeline)

`chap-but-lanh-dao` là **"TẦNG BIÊN TẬP VĂN PHONG & THỔI HỒN NỘI DUNG"** kết nối trực tiếp với 3 kỹ năng còn lại:

```
┌────────────────────────────────┐       ┌────────────────────────────────┐
│ 1. THỊ TRƯỜNG & PHÁP LÝ        │       │ 2. TÒA SOẠN BÁO AI             │
│ • tham-dinh-thi-truong     │ ────► │ • chap-but-lanh-dao           │
│   (Nỗi đau ngách, Unit Econ)   │       │   (Biên tập câu chuyện, nhịp   │
│ • phap-che-doanh-nghiep             │       │   điệu, dẫn chứng thực chiến,  │
│   (Căn cứ luật, SOT nguyên văn)│       │   khử sạch 100% văn mẫu AI)    │
└────────────────────────────────┘       └───────────────┬────────────────┘
                                                         │
                                                         ▼
                                         ┌────────────────────────────────┐
                                         │ 3. NHÀ MÁY XUẤT BẢN TÀI LIỆU   │
                                         │ • xuat-ban-cong-vu             │
                                         │   (Đổ văn bản đã trau chuốt    │
                                         │   vào Word NĐ 30, Slide Pitch  │
                                         │   Deck hoặc Bảng tính Excel)   │
                                         └────────────────────────────────┘
```

- **Khi phối hợp với `tham-dinh-thi-truong`:** Lấy báo cáo thị trường khô khan biến thành một bài viết LinkedIn thu hút hàng nghìn lượt đọc hoặc một bài chào hàng (Sales Pitch) chạm đúng tim đen khách hàng.
- **Khi phối hợp với `phap-che-doanh-nghiep`:** Lấy các điều luật khô cứng biến thành bài viết cảnh báo rủi ro pháp lý đời thường, giúp khách hàng nhận ra hiểm họa mà không bị ngộp bởi thuật ngữ chuyên ngành.
- **Khi phối hợp với `xuat-ban-cong-vu`:** Cung cấp văn bản thuần Việt mượt mà, không một lỗi dấu câu để `xuat-ban-cong-vu` dàn trang xuất bản file Word, PDF hoặc Slide tuyệt đẹp.

---

## 5. Bản Quyền & Tác Giả
*Ghi chú phát hành SHT (0.31.3): mục này cố ý lặp ở 5 skill dựa trên vietduc·ai (`chap-but-lanh-dao`, `kien-truc-tai-lieu`, `phap-che-doanh-nghiep`, `tham-dinh-thi-truong`, `xuat-ban-cong-vu`) để ghi công tác giả đi cùng từng skill khi được dùng riêng; không định nghĩa lại quy tắc nghiệp vụ nào.*


**Hệ Thống AI Workforce Doanh Nghiệp (vietduc·ai)**  
Chuyên gia Đào tạo & Chuyển giao Giải pháp Tự động hóa AI Doanh nghiệp  
Hệ sinh thái: **vietduc.ai**
