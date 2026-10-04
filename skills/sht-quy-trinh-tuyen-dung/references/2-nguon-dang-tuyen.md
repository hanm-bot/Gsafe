# GĐ 2 — Nguồn ứng viên & đăng tuyển

## Nguồn hợp pháp — thứ tự ưu tiên

1. API hoặc kết nối đối tác được nền tảng chấp thuận
2. Chức năng xuất dữ liệu chính thức của nền tảng
3. CV của ứng viên đã chủ động ứng tuyển
4. CV do HR tải xuống trong phạm vi tài khoản được cấp quyền
5. ATS của doanh nghiệp
6. Form Talent Pool có thông báo xử lý dữ liệu
7. Nguồn giới thiệu nội bộ hoặc đơn vị tuyển dụng được ủy quyền

## Tuyệt đối không đề xuất hoặc hướng dẫn

Vượt CAPTCHA · giả lập hành vi người dùng để quét dữ liệu hàng loạt · dùng tài khoản không được ủy quyền · khai thác lỗ hổng website · thu thập trái phép email/số điện thoại · vượt giới hạn truy cập nền tảng · tự động đăng nhập hoặc tải hàng loạt CV khi chưa có chấp thuận · lách điều khoản sử dụng của TopCV hay nền tảng tuyển dụng khác.

Khi đề xuất giải pháp chạm tới pháp luật, quyền riêng tư hoặc điều khoản nền tảng: **ghi rõ đây là đề xuất quản trị, cần bộ phận pháp chế xác nhận.**

---

## Phân tầng theo cấp vị trí

| Cấp vị trí | Cơ chế tiếp nhận phù hợp |
|---|---|
| Vận hành, số lượng lớn (AM, kỹ thuật viên) | Tự động hóa intake hợp lý (form, ATS, luồng ứng tuyển) |
| Chuyên môn (QS, PM, kỹ sư) | Bán tự động — sàng lọc có người rà |
| Cấp cao (CCO, GĐ trung tâm) | **Không tự động hóa** — tiếp cận trực tiếp, giới thiệu, headhunt được ủy quyền |

---

## Nội dung tin tuyển dụng

**Bắt buộc:**
- Không nêu tên khách hàng trọng yếu (đối tác ngân hàng, viễn thông) trong tin công khai. Mô tả bằng loại hình: "khách hàng khối tài chính - ngân hàng".
- Mô tả trách nhiệm gắn kết quả đo lường được, lấy từ bản chân dung ở GĐ 1.
- Nêu rõ cấp bậc thật của vị trí. Tin viết ở mức junior sẽ kéo về hồ sơ junior kể cả khi thực tế cần senior.

**Kiểm tra trước khi đăng:**
- [ ] Cấp bậc trong tiêu đề khớp với yêu cầu kinh nghiệm trong mô tả
- [ ] Không lộ tên khách hàng
- [ ] Yêu cầu bắt buộc vs ưu tiên được tách rõ
- [ ] Có nêu khu vực làm việc và phạm vi di chuyển thực tế

---

## Vấn đề kỹ thuật đã gặp với nền tảng TopCV

- **Trình soạn thảo rich-text (contenteditable DIV) từ chối input tự động.** Mọi thao tác điền nội dung mô tả công việc phải **dán thủ công**. Khi hỗ trợ người dùng sửa tin, chuẩn bị sẵn nội dung dạng text để họ copy, không hứa tự động điền được.
- Nhãn tự động của nền tảng (ví dụ "Chưa phù hợp") **có thể sai** — đặc biệt với CV viết bằng tiếng Anh hoặc CV có trang đầu không đại diện nội dung. Luôn mở toàn bộ CV trước khi chấp nhận nhãn hệ thống.

> Ca thực tế: một hồ sơ bị gắn "Chưa phù hợp" tự động, nhưng đọc đủ 6 trang cho thấy đây là hồ sơ chuyên môn mạnh nhất trong pipeline. Trang 1 của CV gợi ý sai hướng chuyên môn.
