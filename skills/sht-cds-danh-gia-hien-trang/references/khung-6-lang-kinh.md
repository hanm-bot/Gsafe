# Khung 6 lăng kính thị trường và lựa chọn hướng triển khai B2B

<!-- cố ý lặp với .agents/knowledge/02_Chien-luoc-Lo-trinh/khung-6-lang-kinh.md (bản cho người đọc web) — sửa một bản thì sửa cả hai. Bản trong skill để plugin chạy được ở máy/Cowork không có cây .agents/. -->

> Điều kiện đầu vào: workspace **đã có đầu ra Giai đoạn 01** (luật cứng #4).
> Khung dùng ở Giai đoạn 02 để chọn và xếp ưu tiên hướng triển khai. Khung này **không** phải thiết kế giải pháp (việc thiết kế giải pháp thuộc Giai đoạn 03).
> Phương pháp gốc: AI48S `phan-tich-thi-truong-opc/resources/8-lenses-framework.md` (vietduc·ai), SHT viết lại cho B2B Bank/Telco 27/09/2026.

## L1. Nhu cầu cấp bách (Urgent Pain)
- **Câu hỏi cần trả lời:** Điểm nghẽn As-Is nào đang gây tổn thất lớn nhất và cần xử lý ngay?
- **Đầu vào:** Bảng tổng hợp điểm nghẽn quy trình As-Is từ đầu ra Giai đoạn 01.
- **Đầu ra:** Ghi nhận vào sheet #1 (MV-GSM) và sheet #4 (Mục tiêu – KPI theo 3 trụ).

## L2. Ba lực tác động (Tri-Force Dynamics)
- **Câu hỏi cần trả lời:** Lực cầu, lực cung và lực cấu trúc (pháp lý, an ninh mạng, dữ liệu) thúc đẩy hướng nào?
- **Đầu vào:** Báo cáo hiện trạng Giai đoạn 01 và căn cứ pháp lý qua `sht-phap-che-sot` (tra hiệu lực tại mốc vụ việc: quy định NHNN, Luật An ninh mạng, Luật Bảo vệ dữ liệu cá nhân — skill có từ 0.28.0).
- **Đầu ra:** Ghi nhận vào sheet #3 (SWOT / PEST / USP / UVP).

## L3. Khoảng trống quy trình (Niche Process Vacuum)
- **Câu hỏi cần trả lời:** Khoảng trống đặc thù nào theo công thức Ngành × Vấn đề × Quy trình đóng gói chưa có giải pháp đáp ứng?
- **Đầu vào:** Danh mục quy trình nghiệp vụ đặc thù ngành Bank/Telco từ đầu ra Giai đoạn 01.
- **Đầu ra:** Ghi nhận vào sheet #2 (Business Model Canvas - BMC) và sheet #5 (Backlog use-case).

## L4. Lợi thế bền vững (Defensibility Moat)
- **Câu hỏi cần trả lời:** Lợi thế phòng thủ độc quyền nào bảo đảm giải pháp không bị thay thế (case study, dữ liệu riêng, quy trình đóng gói sâu; bỏ tầng thương hiệu cá nhân)?
- **Đầu vào:** Báo cáo tài sản số, quy trình độc quyền của SHT và của khách hàng từ Giai đoạn 01.
- **Đầu ra:** Ghi nhận vào sheet #3 (USP / UVP).

## L5. Đe doạ và đòn bẩy AI (AI Threat vs Leverage)
- **Câu hỏi cần trả lời:** Khâu nào tự động hóa bằng đòn bẩy AI, khâu nào bắt buộc giữ con người phê duyệt (Human-In-The-Loop - HITL)? Thiết kế agent chi tiết thực hiện tại Giai đoạn 03 (`sht-cds-thiet-ke-agent`).
- **Đầu vào:** Bảng phân loại tác vụ As-Is từ đầu ra Giai đoạn 01.
- **Đầu ra:** Ghi nhận vào sheet #5 (Backlog use-case: phân loại nhóm Crawl/Walk/Run).

## L6. Kinh tế đơn vị và hiệu quả đầu tư (Unit Economics & Value-based)
- **Câu hỏi cần trả lời:** Giá trị kinh tế mang lại là bao nhiêu theo nguyên tắc định giá theo giá trị?
- **Đầu vào:** Chỉ số đo lường hiệu quả (ROI) sơ bộ đã đo ở Giai đoạn 01.
- **Đầu ra:** Ghi nhận vào sheet #6 (Business case & ROI sơ bộ).

---
*Ghi chú kết thúc:* L7 (kiểm chứng 0-code) và L8 (marketing cá nhân) của bản gốc bị bỏ. Với khách hàng khối Bank/Telco, việc kiểm chứng giải pháp được thực hiện qua Hồ sơ Pilot tại Giai đoạn 04 (`tao-ho-so-pilot`).
