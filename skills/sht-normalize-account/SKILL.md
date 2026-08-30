---
name: sht-normalize-account
description: >-
  Chuẩn hóa danh tính khách hàng/tài khoản trong dữ liệu SHT Sales Pipeline (Turso/Base.vn CRM)
  trước khi phân tích theo account, chi nhánh, hoặc Account 360. LUÔN dùng skill này bất cứ khi nào
  làm việc với bảng `deals`, đếm số khách hàng/chi nhánh, gộp/rollup theo account, hay tính điểm
  sức khỏe account — kể cả khi người dùng không nói chữ "chuẩn hóa". Skill đóng gói bài học xương máu:
  gộp account phải theo Mã Dự Án có cấu trúc (`ma`), KHÔNG theo tên khách hàng free-text (`kh`) — làm
  sai chỗ này sẽ tách khống 1 chi nhánh thành hàng trăm account ảo. Khi con số sẽ vào văn bản
  chính thức, chuyển tiếp sang `sht-xacthuc-baocao-hoatdong`. KHÔNG dùng skill này để kiểm
  tính đúng đắn của doanh số (việc của `sht-xacthuc-baocao-hoatdong`) hay xác minh danh tính
  người (việc của `chuan-hoa-du-lieu-nhansu`).
---

# Chuẩn hóa account SHT Sales Pipeline

## Vì sao cần skill này
Trong bảng `deals`, cột `kh` (tên khách hàng) do người nhập tay nên **một chi nhánh có hàng trăm biến thể tên** ("Vietinbank CN Tây Hà Nội", "VTB - CN Tây Hà Nội", "Ngân hàng TMCP Công thương Việt Nam- CN Tây HN"...). Gộp account theo `kh` sẽ **tách khống** (một lần thực tế: 1 ngân hàng → 446 account ảo). Định danh đúng nằm ở **Mã Dự Án `ma`** — chuỗi có cấu trúc do hệ thống sinh.

## Ba nguyên tắc BẮT BUỘC
1. **Khóa account = mã có cấu trúc trong `ma`, KHÔNG phải `kh`.** Cấu trúc: `[Năm 2-4 số][<BANK>][Mã CN][STT 3 số]` — ví dụ `26VTBTN007` = 2026 · VTB · TN(Thái Nguyên) · 007.
2. **Parse `ma` thất bại → gom vào 1 bucket "chưa xác định".** TUYỆT ĐỐI không fallback về gộp theo `kh` (sẽ phồng lại số account).
3. **Chuẩn hóa xong → TỰ KIỂM.** Số mã CN phải ≤ danh mục CN thật (Vietinbank ~155). Vượt xa ⇒ dừng và nghi ngờ chính mình. Đừng mặc định phân tích đầu tiên là đúng.

## Quy trình
1. Đọc `deals` với ít nhất `ma`, `kh` (và các cột phân tích cần thiết).
2. Với mỗi dòng, gọi `account_key(ma, kh)` từ `scripts/normalize.py` → trả `(bank, code, key)`. Gộp theo `key`.
3. Tên hiển thị: `clean_label(kh)` (lấy biến thể `kh` phổ biến nhất của nhóm).
4. Chạy `validate_branch_count(số_mã_CN)` và báo kết quả tự kiểm cho người dùng.
5. Nếu người dùng có **danh mục mã CN chuẩn (mã → tên, ~155 dòng)**, map để đưa về CN chính thức và tách PGD/công ty con.

## Dùng script (deterministic — luôn ưu tiên gọi script thay vì tự regex)
```python
import sys; sys.path.append("scripts")
from normalize import account_key, clean_label, validate_branch_count
bank, code, key = account_key(ma, kh)     # gộp theo `key`
```
Tự kiểm nhanh: `python3 scripts/normalize.py` (10 ca test, gồm các `ma` khó đã biết).

## Bốn bẫy dữ liệu Turso (đọc `references/data-traps.md` để đầy đủ)
- Dùng `stageId` (1–12), KHÔNG `stageName`.
- AM thật = JOIN `deals.amUser` ↔ `staff.username` (cột `am` hay rỗng/`[EXTERNAL]`).
- Nghỉ việc = `staff.status`, KHÔNG dùng `amStatus`/`executorStatus`.
- Account key = `ma` (chính là skill này).

## Cạm bẫy phân loại bank
Luật cụ thể phải đặt TRƯỚC luật chung: "cong thuong" (Vietinbank) trùng với "Sài Gòn Công Thương" (Saigonbank) → Saigonbank phải xét trước. `bank_key()` đã xử lý; khi thêm bank mới, giữ thứ tự này.

## Đầu ra kỳ vọng
Mỗi account gộp có: `bank`, `code` (mã CN hoặc `—`/rỗng), `label` (tên gọn), và số biến thể `kh` đã gom. Kèm 1 dòng kết quả tự kiểm số CN.

## Khi số liệu đi tiếp vào báo cáo

Gộp account xong thường là để đếm khách hàng/chi nhánh cho một báo cáo. Nếu con số đó sẽ vào văn bản chính thức (báo cáo tháng/quý, Căn cứ của một Quyết định), chuyển sang `sht-xacthuc-baocao-hoatdong` để truy nó về câu truy vấn gốc và gắn nhãn ✅/⚠️/❓ — kèm dòng tự kiểm số chi nhánh làm bằng chứng đã chuẩn hóa đúng.

Quy tắc bàn giao chung: `sht-nen-tang-kiem-chung`.
