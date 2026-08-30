# BỘ TIÊU CHUẨN KIỂM TOÁN DỮ LIỆU & HẠ TẦNG CÔNG NGHỆ

---

## 1. Kiểm toán Dữ liệu 6 Chiều (Data Quality 6 Dimensions)

| Chiều đánh giá | Ý nghĩa kiểm tra | Ngưỡng rủi ro | Hành động khắc phục |
| :--- | :--- | :--- | :--- |
| **1. Đầy đủ (Completeness)** | Các trường bắt buộc (SĐT, Email, Mã định danh, Giá trị) có bị bỏ trống không? | Trống > 10% ➔ Cao | Bổ sung trường bắt buộc, khóa form |
| **2. Chính xác (Accuracy)** | Số liệu trong hệ thống có khớp với thực tế (Tồn kho, Doanh thu, Thông tin KH)? | Lệch > 5% ➔ Cao | Kiểm kê đối soát, validate format |
| **3. Nhất quán (Consistency)** | Đơn vị tính (triệu vs đồng), định dạng ngày tháng, quy ước mã có đồng nhất không? | Không đồng nhất ➔ Trung bình | Viết script chuẩn hóa tự động |
| **4. Kịp thời (Timeliness)** | Dữ liệu có được cập nhật realtime hay bị trễ (VD: cuối tuần mới nhập một lần)? | Trễ > 24h ➔ Cao | Đẩy luồng Webhook realtime |
| **5. Duy nhất (Uniqueness)** | Khách hàng/sản phẩm có bị tạo trùng lặp nhiều dòng không? | Trùng lặp > 5% ➔ Cao | Chạy Deduplication (gộp account) |
| **6. Hợp lệ (Validity)** | Định dạng số điện thoại, email, MST có đúng chuẩn Regex không? | Sai chuẩn > 5% ➔ Trung bình | Thêm logic kiểm tra biểu thức chính quy |

---

## 2. Kiểm toán Hạ tầng & Khả năng Tích hợp (Integration Audit)

Checklist đánh giá từng phần mềm trước khi tích hợp vào trục tự động hóa:
- [ ] **API/Webhook:** Phần mềm có hỗ trợ REST API hoặc Webhook gửi sự kiện không?
- [ ] **Quyền quản trị:** Ai là Super Admin giữ tài khoản (tránh phụ thuộc cá nhân)?
- [ ] **Hạn mức (Rate Limit):** Giới hạn số request/phút hoặc chi phí API tính thêm?
- [ ] **Sơ đồ luồng:** Dữ liệu vào từ đâu, lưu ở đâu, và trả về cho ai?
- [ ] **Điểm chết đơn (SPOF):** Nếu hệ thống sập, luồng dự phòng (Fallback) là gì?
