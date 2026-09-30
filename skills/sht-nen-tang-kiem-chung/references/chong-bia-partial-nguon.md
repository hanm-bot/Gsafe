# Chống bịa: bản PARTIAL và thứ tự ưu tiên nguồn

*(thêm 30/09/2026, v0.30.0 — báo cáo gap `THỰC HÀNH-AI/04_Kiem-Chung-Upgrade/2026-09-30_GAP-sht-skills-vs-tai-lieu-hoc.md`)*

Nguồn: `THỰC HÀNH-AI/05_Kien-Thuc-Trich-Xuat/02_chuoi-artifact.md` §2.2–2.4 (khung Prompt Spec PS-006/007/009), SHT viết lại. Bổ sung cho §8 "Phân loại phát biểu theo độ chắc chắn" của `SKILL.md` — bốn mức ở §8 là bản duy nhất; file này không định nghĩa lại.

## 1. Bản PARTIAL — giao một phần thay vì bịa cho đủ

Khi dữ liệu không đủ để hoàn thành deliverable, **không** lấp chỗ trống bằng suy đoán. Giao bản PARTIAL, mở đầu bằng khối 5 phần:

| Phần | Ghi gì |
|---|---|
| **Đã hoàn thành** | Phần nào làm xong, dựa trên nguồn nào |
| **Còn thiếu** | Mục nào chưa làm được |
| **Lý do** | Thiếu dữ liệu gì, vì sao không lấy được (không truy cập được, nguồn mâu thuẫn, chưa có trong hồ sơ) |
| **Cần bổ sung** | Đầu vào cụ thể người dùng phải cung cấp để làm tiếp |
| **Trạng thái đề xuất** | Ví dụ: "PARTIAL — chưa dùng cho văn bản chính thức", "PARTIAL — dùng được phần A, chờ B" |

Tên file hoặc tiêu đề ghi rõ `PARTIAL`. Không bàn giao bản PARTIAL như bản hoàn chỉnh (checklist bàn giao §10).

### Phải làm / Không được làm

| Tình huống | Phải | Không được |
|---|---|---|
| Yêu cầu mơ hồ | Hỏi lại, hoặc liệt kê các cách hiểu | Tự chọn một cách hiểu rồi làm |
| Hai thực thể trùng tên (người, công ty, chi nhánh) | Liệt kê các ứng viên kèm dấu hiệu phân biệt | Gộp bừa thành một |
| Không tìm thấy bản ghi | Ghi NOT FOUND / chưa có dữ liệu, nêu đã tìm ở đâu | Bịa số liệu, lô hàng, ngày tháng |
| Nguồn mâu thuẫn | Nêu cả hai, xếp theo mục 2, ghi nguồn nào thắng | Lấy trung bình hoặc chọn im lặng |

## 2. Thứ tự ưu tiên nguồn khi mâu thuẫn

Khung chung (cao → thấp):

1. Tài liệu gốc do người dùng/khách cung cấp (bản ký, bản scan gốc)
2. Cổng thông tin / đăng ký nhà nước
3. Nguồn chính thức của công ty liên quan
4. Cơ sở dữ liệu thương mại tin cậy
5. Nguồn ngành tin cậy
6. Hồ sơ nghề nghiệp công khai
7. Tin tức / danh bạ công khai → chỉ dùng làm **Suy luận** (mức 2), không làm Dữ kiện

Skill nghiệp vụ **được** khai thứ tự riêng cho miền của mình, miễn ghi ra và trỏ về đây — ví dụ `sht-normalize-account` (Mã Dự Án `ma` thắng tên free-text `kh`), `sht-xacthuc-baocao-hoatdong` (hệ thống nguồn CRM thắng số trong báo cáo cũ), `sht-phap-che-sot` (văn bản gốc trên cổng nhà nước thắng bản trích lại). Lưu ý hồ sơ cũ trong workspace có thể đóng băng ở mốc quá khứ — đọc `00_NGUON-HO-SO.md` trước khi coi nó là tầng 1.
