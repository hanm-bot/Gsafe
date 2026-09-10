# CHECKLIST TUÂN THỦ — NĐ13/2023 & NHNN cho PRD giải pháp CĐS Bank/Telco

> Đây là checklist NFR nhóm tuân thủ, không phải tư vấn pháp lý. Khi PRD ra hồ sơ bán cho khách, đối chiếu bản gốc văn bản pháp luật và để pháp chế khách duyệt. Không kết luận "đạt/không đạt" mà chưa đối chiếu văn bản gốc (luật cứng SHT #1).

## 1. NĐ 13/2023/NĐ-CP — Bảo vệ dữ liệu cá nhân (nền chung mọi ngành)

| # | Điểm kiểm | Có trong PRD? |
|---|---|---|
| 1 | Xác định rõ **dữ liệu cá nhân** và **dữ liệu cá nhân nhạy cảm** nào được xử lý | ☐ |
| 2 | Cơ sở pháp lý xử lý (sự đồng ý của chủ thể / nghĩa vụ hợp đồng / luật định) | ☐ |
| 3 | Cơ chế thu thập **sự đồng ý** và rút lại đồng ý | ☐ |
| 4 | Quyền của chủ thể dữ liệu (truy cập, chỉnh sửa, xoá, phản đối) được hệ thống hỗ trợ | ☐ |
| 5 | **Sơ đồ luồng dữ liệu** — dữ liệu đi đâu, lưu ở đâu, ai truy cập, có ra khỏi hạ tầng khách không | ☐ |
| 6 | Chuyển dữ liệu ra nước ngoài (nếu có) — đánh giá tác động + hồ sơ theo NĐ13 | ☐ |
| 7 | Masking/truncation PII trong log, DB, màn hình | ☐ |
| 8 | Thời hạn lưu trữ & quy trình xoá/huỷ dữ liệu | ☐ |
| 9 | Quy trình ứng phó sự cố lộ lọt dữ liệu (thông báo trong thời hạn luật định) | ☐ |

## 2. Quy định NHNN — riêng cho khách Ngân hàng / TCTD

| # | Điểm kiểm | Có trong PRD? |
|---|---|---|
| 10 | An toàn hệ thống thông tin theo cấp độ (đối chiếu quy định ATTT ngành ngân hàng hiện hành) | ☐ |
| 11 | Xác thực & phân quyền truy cập hệ thống lõi (least-privilege) | ☐ |
| 12 | Nhật ký giao dịch & khả năng truy vết (audit trail) không sửa được | ☐ |
| 13 | Sao lưu, phục hồi, phương án dự phòng (BCP/DR) | ☐ |
| 14 | Kiểm soát bên thứ ba / thuê ngoài (nếu giải pháp dùng dịch vụ ngoài) | ☐ |
| 15 | Với eKYC/định danh: đối chiếu quy định định danh điện tử hiện hành | ☐ |

## 3. Có yếu tố nước ngoài / chuẩn quốc tế (tuỳ khách)

| # | Điểm kiểm | Có trong PRD? |
|---|---|---|
| 16 | **EU AI Act** — phân loại hệ thống AI theo mức rủi ro (nếu giải pháp có AI ra quyết định) | ☐ |
| 17 | **NIST AI RMF** — khung quản trị rủi ro AI | ☐ |

## 4. Câu khách chắc chắn hỏi ở nghiệm thu — PRD phải trả lời bằng văn bản

- "Dữ liệu khách hàng có rời khỏi hạ tầng của chúng tôi không?" → **sơ đồ luồng dữ liệu**, không phải lời hứa.
- "Nếu hệ thống sai cho khách hàng của chúng tôi thì ai chịu trách nhiệm?" → bản đồ escalate + quy trình xử lý khi sai.
- "Dữ liệu cá nhân nhạy cảm được che thế nào?" → quy tắc masking cụ thể ở §8 PRD.
