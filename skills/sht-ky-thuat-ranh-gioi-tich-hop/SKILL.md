---
name: "sht-ky-thuat-ranh-gioi-tich-hop"
description: "Kỹ thuật tích hợp thiết bị SHT với hãng và vendor: phân lớp hệ thống, đặc tả ICD, ngân sách độ trễ, giao thức kết nối, ma trận đáp ứng và test case nghiệm thu. LUÔN dùng khi bóc tách BRD/SoW kỹ thuật, phân định ranh giới hệ thống, dựng đề bài kỹ thuật trung lập, kiểm tương thích thiết bị. KHÔNG dùng cho PRD giải pháp CĐS bán khách (sht-cds-thiet-ke-prd), rà hợp đồng (ra-soat-hop-dong-vendor), chấm điểm chọn NCC (lua-chon-tham-dinh-ncc), soạn PO (sht-pm-van-ban-doi-tac-po)."
---

# Kỹ thuật — ranh giới tích hợp, đặc tả, nghiệm thu

Vai: kỹ thuật / dev phía SHT. Việc: nói rõ **mã nào chạy ở đâu thì thuộc ai**, bên nào phải đưa tài liệu gì, và thế nào là đạt. Câu trả lời kỹ thuật của vai này là nguyên liệu để PM viết vào CV/PO và để lãnh đạo chốt lập trường.

Giọng văn và thể thức đầu ra: theo mục 5 của `sht-pm-van-ban-doi-tac-po`.

## 1. Phân lớp trước, rồi mới bàn phạm vi

Mẫu phân lớp cho hệ thống giám sát thiết bị đầu cuối (thay tên thành phần theo dự án):

| Lớp | Thành phần | Chủ thể |
|---|---|---|
| Thiết bị | Ứng dụng thanh toán, kernel, lớp ghi log, client truyền thông, bộ thực thi lệnh | Hãng thiết bị |
| Ranh giới | Giao thức, lược đồ thông điệp, định dạng tệp log | Hãng phát hành tài liệu giao diện (ICD), SHT phê duyệt |
| Máy chủ | Thu nhận, lưu trữ, truy vấn, gửi lệnh, sổ thiết bị, dashboard, phân quyền | SHT hoặc nhà cung cấp SHT thuê |
| Hệ nghiệp vụ | Thu phí, trung tâm thanh toán, gate, hệ quản trị thiết bị (TMS) | Bên thứ ba — chỉ giám sát kết nối |

Nguyên tắc phân định, không có ngoại lệ: **mã chạy trên thiết bị thuộc hãng; mã chạy trên máy chủ thuộc bên làm máy chủ.** Tranh chấp phạm vi nào cũng quy về câu hỏi "mã này nạp vào đâu".

Ba ranh giới cần gọi tên: thiết bị ↔ máy chủ (kênh trạng thái, kênh lệnh, tải log); máy chủ ↔ hệ nghiệp vụ (chỉ kiểm sống, không gọi API nghiệp vụ); máy chủ ↔ hệ quản trị thiết bị của hãng (kích hoạt tải tham số/ứng dụng — hay vướng license).

## 2. Hãng phải phát hành gì — tài liệu giao diện 9 nhóm

1. Định danh thiết bị (một khoá duy nhất dùng xuyên hệ thống, kèm ánh xạ sang các mã khác).
2. Giao thức truyền tải (chiều khởi tạo, giữ kết nối, mất kết nối, bộ đệm khi máy chủ không sẵn sàng).
3. Quy ước kênh (tên kênh, quyền publish/subscribe mỗi phía).
4. Lược đồ thông điệp (trường bắt buộc, kiểu, phiên bản, mã truy vết để khớp lệnh với phản hồi).
5. Danh mục lệnh (tham số, thời gian thực thi tối đa, mã trả về; **lệnh không được ngắt giao dịch đang chạy**).
6. Sự kiện thiết bị tự gửi (khởi động, tải xong tham số, lỗi…).
7. Cấu trúc tệp log (bảng, cột, bảng ánh xạ cờ phân loại, xoay vòng, tải từng phần).
8. Đồng bộ thời gian (nguồn NTP nội bộ, độ lệch cho phép, múi giờ log).
9. Bảo mật kênh (xác thực từng thiết bị, vòng đời chứng thư, cấp và thu hồi, chống phát lại).

Khi hãng chậm, xin **bản sơ bộ trước** gồm các nhóm quyết định (4, 5, 7, 8), bản đủ sau.

Có hai hướng, lãnh đạo chọn: SHT đi xin hãng phát hành ICD, hoặc **SHT tự viết đặc tả phía máy chủ và buộc mọi thiết bị (kể cả thiết bị tương lai) tuân theo**. Hướng thứ hai giữ quyền định nghĩa giao diện ở SHT, giúp module giám sát độc lập hãng và bán lại được cho khách khác.

## 3. Những chỗ kỹ thuật hay vỡ

- **Tương thích giao thức trước khi đánh giá vendor.** Nếu BRD đã chốt một cơ chế (ví dụ HTTP long-polling) mà vendor lớp máy chủ chào kiến trúc khác (ví dụ MQTT có Last-Will), đó là điều kiện chặn, phải xử lý trước khi chấm điểm vendor.
- **Ngân sách độ trễ chia theo chặng.** Chỉ tiêu "phản hồi lệnh dưới 3 giây" là đầu–cuối; chia cho máy chủ xử lý, mạng, thiết bị thực thi, máy chủ hiển thị, và ghi vào hợp đồng của từng bên. Chỉ tiêu không có trong BRD thì đừng ép vào CV với hãng; đưa sang buổi kỹ thuật.
- **Giới hạn license và kết nối.** Hệ quản trị thiết bị có thể giới hạn số kết nối đồng thời thấp hơn số thiết bị thực tế. Đo số kết nối đỉnh thực tế vài ngày trước khi kết luận; thiết kế máy chủ không phụ thuộc việc mọi thiết bị kết nối cùng lúc.
- **Lệnh qua hệ quản trị thiết bị của hãng** thường cần chấp thuận riêng vì license cấp cho tổ chức tài chính. Chưa có chấp thuận thì tách thành hạng mục có điều kiện, không đưa vào nghiệm thu chính.
- **Đổi nền tảng thiết bị** (ví dụ từ hệ điều hành nhúng của hãng sang Android để có thêm QR) thì rà lại toàn bộ giả định về giao thức và lớp ghi log.
- **Dữ liệu thẻ:** log thiết bị và máy chủ không được chứa số thẻ đầy đủ ở bất kỳ đâu.

## 4. Đối chiếu BRD với cam kết khách hàng — tự làm, không tin hộp đen

Khi hãng viết cả BRD lẫn SoW, SHT dễ thành "hộp đen": chỉ biết yêu cầu chạy được. Ba bước:
1. Khớp từng mục cam kết với khách hàng cuối với từng mục BRD. Mục nào không có bên nhận là gap, báo PM và lãnh đạo.
2. SHT **tự viết test case** từ BRD và cam kết khách hàng, không dùng test case của hãng.
3. Bộ tiêu chí nghiệm thu thống nhất và ký **trước khi ký hợp đồng**, không để tới lúc bàn giao.

## 5. Tiêu chí nghiệm thu mẫu

Hai giai đoạn: nghiệm thu chức năng trên môi trường thử với ít nhất 3 thiết bị thật; nghiệm thu vận hành sau tối thiểu 30 ngày chạy thật với 20–30 thiết bị.

Bốn bài kiểm bắt buộc (trượt một bài là không qua):
- Luồng log đầu–cuối: sinh bản ghi định trước trên thiết bị, tải lên, truy vấn ra đúng bản ghi đó.
- Phát hiện mất kết nối: ngắt một thiết bị, hệ thống chuyển cảnh báo trong 180 giây, lỗi trong 300 giây.
- Không lưu dữ liệu thẻ: giao dịch thử rồi quét toàn bộ log, không thấy số thẻ đầy đủ.
- Khớp lệnh – phản hồi: gửi đồng thời nhiều lệnh tới nhiều thiết bị, mọi phản hồi khớp đúng lệnh theo mã truy vết.

Kèm bài kiểm tải mô phỏng đủ số thiết bị thật; nhà cung cấp đưa công cụ, SHT kiểm chứng độc lập.

## 6. Đề bài kỹ thuật cho nhiều nhà cung cấp

- Phần chung (kiến trúc, ranh giới, yêu cầu, kiểm thử) **giống hệt** cho mọi vendor; chỉ mục cuối "điều chỉnh so với đề xuất đã nhận" là riêng từng vendor.
- Trước khi phát hành: quét để chắc bản gửi vendor này **không có tên vendor khác và không có giá**.
- Kèm bảng đối chiếu đáp ứng (mỗi yêu cầu một dòng, cột Đáp ứng đủ / Một phần / Không), đánh dấu các dòng bắt buộc.
- Yêu cầu tối thiểu với vendor lớp máy chủ: bảo hành 12 tháng từ nghiệm thu vận hành (không phải 3 tháng); nêu rõ mức dịch vụ, RTO/RPO; tính cấu hình theo số thiết bị thật, cấu hình mở rộng tách riêng.
- Quyền mã nguồn/SDK: thường **không** có trong thoả thuận phân phối gốc với hãng, phải ký thoả thuận riêng. Có vendor khác chào giao mã nguồn thì ghi nhận, xác minh ai chào và điều kiện gì trước khi dựa vào.

## Trỏ tới

| Việc | Skill |
|---|---|
| Chọn, chấm điểm, PoC nhà cung cấp | `lua-chon-tham-dinh-ncc` |
| Điều khoản thương mại, pháp lý, license | `ra-soat-hop-dong-vendor` |
| Đưa nội dung kỹ thuật vào CV/PO | `sht-pm-van-ban-doi-tac-po` |
| Lập trường đàm phán khi kỹ thuật vướng | `sht-lanh-dao-dam-phan-chuoi-hop-dong` |

