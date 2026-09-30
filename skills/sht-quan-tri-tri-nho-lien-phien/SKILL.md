---
name: sht-quan-tri-tri-nho-lien-phien
version: 1.0
description: "Quyết định sự thật nào đáng lưu memory liên phiên, cập nhật file sẵn có thay vì tạo trùng, đánh dấu \"đã giải quyết\" khi tình huống đổi, giữ MEMORY.md khớp nội dung. LUÔN dùng trước khi ghi trí nhớ liên phiên hoặc khi nghi MEMORY.md lệch. KHÔNG dùng cho dữ liệu nhạy cảm khách (luật cứng #5), không thay 00_NGUON-HO-SO.md của workspace."
---

# Thủ Kho Trí Nhớ Liên Phiên

Vai trò: người quyết định cái gì đáng nhớ, giữ kho trí nhớ liên phiên gọn — không phình to vì trùng lặp, không nói sai vì lỗi thời. Rút từ phiên ghi/cập nhật memory xuyên suốt buổi làm việc BrandOS + hạ tầng hook SHT (20-21/09/2026).

## Nguyên tắc lõi — cái gì đáng lưu, cái gì không

**Đáng lưu:** sự thật KHÔNG suy ra lại được từ code/git/tài liệu sẵn có — ví dụ máy này không có ổ D:\, một thư mục đã đổi tên nhưng tài liệu chưa cập nhật, một quyết định anh Hà đã chốt kèm lý do. Đây là loại thông tin mà nếu quên, phiên sau **sẽ lặp lại đúng sai lầm đã sửa**.

**Không đáng lưu:** thứ tự do repo/git đã ghi lại, kết luận chỉ có ý nghĩa trong phạm vi 1 câu hỏi của phiên này, hoặc bất cứ gì đã nằm sẵn trong CLAUDE.md/tài liệu dự án.

## Quy trình chuẩn

1. **Luôn kiểm memory/ hiện có trước khi viết mới** — đọc index `MEMORY.md`, tìm file nào đã đụng tới đúng chủ đề. Có rồi thì **cập nhật**, không tạo file trùng nội dung.
2. Ghi theo đúng khuôn: frontmatter `name`/`description`/`metadata.type`, thân bài có `**Why:**` (vì sao đáng nhớ) và `**How to apply:**` (dùng nó thế nào ở phiên sau). Link liên quan bằng `[[ten-file-khac]]`.
3. **Khi một việc trong memory cũ vừa được giải quyết** — quay lại đúng file đó, thêm đoạn "✅ Đã sửa ngày X" ngay trong nội dung cũ, **không viết đè** dòng mô tả vấn đề gốc (giữ dấu vết trước/sau). Cập nhật luôn `description` trong frontmatter nếu nó còn ngụ ý vấn đề chưa giải quyết.
   **Phân biệt với trí nhớ SAI** *(thêm 30/09/2026, v0.28.7 — khớp `THỰC HÀNH-AI/.agents/rules/06_tri-nho-lien-phien.md` §4.5)*: bước 3 chỉ áp cho việc **đã đúng lúc ghi rồi tình huống đổi**. Nếu điều đã ghi **sai ngay từ đầu** (sự kiện không có thật, suy luận sai, số nhầm) thì **gỡ câu sai khỏi nội dung** và ghi câu đúng thay vào — không giữ câu sai kèm ghi chú, vì phiên sau có thể đọc trúng câu sai. Đây là sửa nội dung trong file, không phải xoá file (luật cứng #3); cả file sai hết thì `mv` vào `_archive/` và gỡ dòng khỏi `MEMORY.md`.
4. Cập nhật `MEMORY.md` — dòng tóm tắt phải khớp trạng thái MỚI NHẤT, không phải trạng thái lúc mới phát hiện.
5. Trước khi báo "đã cập nhật memory xong" — đọc lại cả file lẫn dòng trong `MEMORY.md`, xác nhận không mâu thuẫn nhau.

## Ví dụ áp dụng từ phiên thật

Phát hiện ban đầu ghi trong 1 file: *"CLAUDE.md khai sai gốc dự án là D:\..."* — sau khi tự tay sửa xong `CLAUDE.md`, **không xoá đoạn mô tả lỗi cũ** mà thêm ngay bên dưới: *"✅ Đã sửa ngày 21/09/2026: cả 2 file CLAUDE.md nay ghi đúng G:\..."* — đồng thời sửa `description` frontmatter từ "CLAUDE.md nói sai" thành "CLAUDE.md từng khai sai... đã sửa lại đúng ngày 21/09/2026". Phiên sau đọc vào thấy đúng trạng thái hiện tại, không tưởng nhầm vẫn còn lỗi.

## Ranh giới quan trọng

Trí nhớ liên phiên là bộ nhớ CỦA AGENT (kiến thức, quyết định, bài học vận hành) — khác hoàn toàn `data/workspaces/<ws>/00_NGUON-HO-SO.md` (hồ sơ nghiệp vụ của khách hàng, đọc trước khi kết luận về workspace) và khác luật cứng #5 (cấm ghi dữ liệu nhạy cảm khách hàng vào `THỰC HÀNH-AI/`). Không lẫn ba thứ này với nhau.

## Dùng kèm

Cùng nguyên tắc "không viết đè lịch sử, chỉ thêm ghi chú cập nhật" với `sht-quan-tri-hien-phap-tai-lieu` — khác đối tượng: skill đó lo tài liệu vận hành (CLAUDE.md và tương đương), skill này lo trí nhớ riêng của agent. Khi một fact vừa sửa xong ở tài liệu vận hành, quay lại đây cập nhật memory tương ứng theo cùng logic.
