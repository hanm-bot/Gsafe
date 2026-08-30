# Danh mục Specs & PRD Chuẩn Trong Rà Soát Hợp Đồng CNTT

Bảng danh mục tài liệu kỹ thuật, đặc tả và quy trình cần bổ sung/chốt trước khi ký hoặc trước khi phát triển.

---

## 1. Ma trận phân bổ ưu tiên tài liệu

| Mức ưu tiên | Thời điểm bắt buộc hoàn thành | Hậu quả nếu thiếu |
|---|---|---|
| **P0** | **Trước khi ký kết hợp đồng/SoW** | Không thể xác định ranh giới trách nhiệm pháp lý và kỹ thuật |
| **P1** | **Sau khi ký, trước khi bắt đầu phát triển** | Nguy cơ làm sai thiết kế, xung đột kiến trúc và trôi tiến độ |
| **P2** | **Trước khi nghiệm thu bàn giao** | Không thể bàn giao vận hành, khó bảo trì dài hạn |

---

## 2. Danh mục 22 hạng mục tài liệu kỹ thuật thường thiếu

1. **SoW Matrix & RACI**: Ma trận phân công trách nhiệm chi tiết từng đầu việc giữa Bên Mua - Bên Bán - Bên Thứ Ba.
2. **Sửa đổi dẫn chiếu đặc tả sai**: Đính chính mọi tham chiếu gãy hoặc trỏ sai phiên bản trong Phụ lục hợp đồng.
3. **Truy xuất văn bản khung còn thiếu**: Bổ sung Thỏa thuận khung / Thỏa thuận phân phối gốc.
4. **Định danh tham chiếu treo**: Làm rõ mọi mã hiệu đặc tả xuất hiện trong nội dung mà chưa có trong danh mục References.
5. **Phân tích tác động trôi phiên bản**: Báo cáo đánh giá chi phí và tiến độ khi nâng cấp phiên bản đặc tả giữa các giai đoạn.
6. **Kế hoạch kiểm thử (Test Plan & Test Cases FAT/SAT)**: Tiêu chí nghiệm thu định lượng chốt trước khi nghiệm thu.
7. **Tài liệu kiến trúc mức cao (HLD - High Level Design)**: Sơ đồ kiến trúc tổng thể, luồng dữ liệu chính.
8. **Tài liệu thiết kế chi tiết (LLD - Low Level Design)**: Thiết kế chi tiết từng module, database schema.
9. **Đặc tả tích hợp giao diện (ICD - Interface Control Document)**: API spec, payload, error code cho từng hệ thống bên thứ ba.
10. **Message & Topic Specification**: Đặc tả định dạng bản tin, cơ chế publish/subscribe, trace ID, schema validation.
11. **Device Security Spec**: Đặc tả an ninh phần cứng và firmware thiết bị đầu cuối.
12. **Đặc tả Masking/Truncation dữ liệu**: Quy tắc che mờ số thẻ, dữ liệu PII trong log và database.
13. **Đánh giá tác động chứng nhận bảo mật**: Đánh giá ảnh hưởng khi thay đổi thiết kế lên các chứng chỉ bảo mật hiện có.
14. **Mô hình tải & dung lượng (Capacity & Performance Model)**: Tính toán sizing hạ tầng dựa trên số lượng giao dịch và người dùng.
15. **Chỉ số phi chức năng định lượng (NFR)**: Thời gian phản hồi tối đa, throughput TPS, độ trễ, heartbeat, timeout.
16. **Bảng chuyển đổi chuẩn mật mã**: Lộ trình nâng cấp thuật toán mã hóa và chiều dài khóa.
17. **Quy trình quản lý khóa mật mã (Key Management Specification)**: Tạo, lưu trữ, xoay vòng và hủy khóa bảo mật.
18. **Tài liệu vận hành & Khắc phục sự cố (Runbook & DR Plan)**: Kịch bản ứng cứu sự cố, RTO/RPO và backup.
19. **Kế hoạch đào tạo & Chuyển giao (Training Plan)**: Giáo trình, thời lượng, đối tượng và bài kiểm tra đánh giá.
20. **Báo cáo tuân thủ phần mềm nguồn mở (SBOM & OSS Compliance)**: Danh mục thư viện open-source và giấy phép sử dụng.
21. **Thỏa thuận ký quỹ mã nguồn (Source Code Escrow Agreement)**: Hợp đồng 3 bên với tổ chức ký quỹ mã nguồn độc lập.
22. **Văn bản chấp thuận bên thứ ba truy cập License**: Giấy phép cho phép tích hợp hệ thống bên thứ ba vào phần mềm được cấp phép.
