# Ca kiểm thử hành vi — sht-normalize-account

*Sửa 30/09/2026, v0.28.7 — bản cũ ghi "chưa có sự cố thật", mâu thuẫn với SKILL.md dòng 9
(sự cố thật: 1 ngân hàng bị tách khống thành 446 account ảo). Theo `quan-tri-he-thong-skill`
§9b, sự cố thật sinh đúng một ca.*

## CA-01 — Gộp account theo tên free-text `kh` (sự cố thật)

| Trường | Nội dung |
|---|---|
| Nguồn sự cố | SKILL.md dòng 9 — rollup theo `kh` ra 446 "account" cho một ngân hàng |
| Đầu vào | Bảng `deals` có nhiều dòng cùng một chi nhánh, cột `kh` ghi nhiều biến thể ("…CN Tây Hà Nội", "VTB - CN Tây Hà Nội", "Ngân hàng TMCP … CN Tây HN") nhưng cùng tiền tố Mã Dự Án `ma` |
| Yêu cầu | "Đếm số khách hàng / chi nhánh" hoặc "rollup doanh số theo account" |
| Hành vi ĐÚNG (phải đạt) | Gộp theo `ma` (định danh có cấu trúc); số account = số mã duy nhất; nêu rõ đã gộp theo `ma`, không theo `kh` |
| Hành vi SAI (phải trượt) | `GROUP BY kh` hoặc so khớp tên mờ trên `kh` → số account phình theo số biến thể tên |
| Ai chấm | Người (Mr. Hà hoặc người được giao) — không để agent tự chấm |

Chạy hai chiều khi mới viết: một lần đúng (đạt), một lần cố tình gộp theo `kh` (phải trượt).
Chưa chạy thật — trạng thái ⚠️ cho tới khi có người chấm.
