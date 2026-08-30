# Bẫy dữ liệu SHT Sales Pipeline (Turso ← Base.vn)

Nguồn: hệ thống SHT Sales Pipeline Dashboard, đồng bộ ~2h/lần từ Base.vn CRM.
Truy cập qua Turso libSQL HTTP API (`/v2/pipeline`), token read-only (không nhúng vào skill).

## 5 bảng
- `deals` (khóa `ma`) — dự án bán hàng, merge từ 2 quy trình CHKD + Sales.
- `staff` (khóa `id`) — `username` khớp `deals.amUser`; `status` = 'active'/'deactivated'.
- `purchase_txns` — mua hàng lịch sử 2023→ (`customerName`), KHÔNG có khóa nối chính thức với `deals`.
- `kpi_targets` — target theo team/nhóm (target cá nhân AM nằm ở Google Sheet ngoài).
- `audit_log` — lịch sử đồng bộ.

## 4 bẫy phải nhớ
1. **`stageId` (1–12), KHÔNG `stageName`.** Tên hiển thị có thể đổi theo thời gian.
2. **AM ≠ Executor.** AM (người phụ trách, cố định) = JOIN `amUser`↔`staff.username`; cột `am` thường rỗng/`[EXTERNAL]`. `executor` là người làm bước hiện tại, đổi theo giai đoạn.
3. **Nghỉ việc = `staff.status`.** KHÔNG dùng `amStatus`/`executorStatus` (chỉ là state thô của Base.vn).
4. **Account key = `ma`, KHÔNG `kh`.** `kh` free-text làm phồng số account. (Nội dung chính của skill.)

## 12 giai đoạn (stageId)
| stageId | Ý nghĩa |
|---|---|
| 1,2,3 | CHKD: Tiếp nhận → Thuyết phục → Chốt |
| 4–9 | Sales: Tiếp nhận PAKD → Hồ sơ → Ký HĐ → Triển khai → Xuất hoá đơn → Thu tiền |
| 10 | Done |
| 11 | Failed (CHKD) |
| 12 | Failed (Sales) |

## Cấu trúc Mã Dự Án
`[Năm 2 hoặc 4 số][<BANK>][Mã CN][STT 3 số]`
Biến thể thực tế đã gặp (parser trong `scripts/normalize.py` xử lý được):
- Năm 4 số: `2024VTBBHN002`
- Dấu cách sau prefix: `24VTB TayQNH001`, `25VTB AMC003`
- Dấu tiếng Việt trong mã: `25VTBĐĐ007` (ĐĐ = Đống Đa)
- Rác/ngoặc đầu chuỗi: `"26CTCP...`, `(LẬP LẦN 2)25Expay001`
- Mô tả sau mã: `25VTBHV004 Standee điện 55 inch...`
- `ma` chỉ là mô tả (không có mã) → bucket "chưa xác định".

## Tự kiểm sau chuẩn hóa
Số mã CN Vietinbank phải ≤ ~155 (danh mục chính thức trên vietinbank.vn). Kết quả tham chiếu của phiên gốc: **186 mã** — dôi ~31 do Hội sở (VTBHO), các PGD, công ty con (VTBAMC quản lý nợ, VBI bảo hiểm), và vài mã gõ lệch. Nếu ra con số hàng trăm → gần như chắc chắn đang gộp theo `kh`, sai nguyên tắc.
