# CHECKLIST TUÂN THỦ — Luật BVDLCN & NHNN cho PRD giải pháp CĐS Bank/Telco

> Đây là checklist NFR nhóm tuân thủ, không phải tư vấn pháp lý. Khi PRD ra hồ sơ bán cho khách, đối chiếu bản gốc văn bản pháp luật và để pháp chế khách duyệt. Không kết luận "đạt/không đạt" mà chưa đối chiếu văn bản gốc (luật cứng SHT #1).

> **Căn cứ mục 1 (tra 30/09/2026, v0.30.3, qua `sht-phap-che-sot`):** Luật Bảo vệ dữ liệu cá nhân **91/2025/QH15** (Quốc hội thông qua 26/06/2025) và **NĐ 356/2025/NĐ-CP** (ban hành 31/12/2025), cùng hiệu lực **01/01/2026**, trạng thái "Còn hiệu lực" trên CSDL quốc gia về pháp luật (Bộ Tư pháp): https://vbpl.vn/van-ban/chi-tiet/179252 · https://vbpl.vn/van-ban/chi-tiet/187276 (truy cập 30/09/2026). **NĐ 13/2023/NĐ-CP hết hiệu lực** theo NĐ 356/2025 Đ.42 k.2 (nguyên văn: "Nghị định số 13/2023/NĐ-CP ngày 17 tháng 4 năm 2023 của Chính phủ về bảo vệ dữ liệu cá nhân hết hiệu lực kể từ ngày Nghị định này có hiệu lực thi hành"). Tên file giữ `…nd13…` để không gãy tham chiếu.
>
> **Chuyển tiếp** (Luật 91/2025 Đ.39): sự đồng ý/thoả thuận đã có theo NĐ 13/2023 trước 01/01/2026 thì tiếp tục, không phải xin lại; hồ sơ đánh giá tác động đã được tiếp nhận thì tiếp tục dùng, cập nhật theo luật mới.
>
> **Miễn trừ quy mô** (Luật Đ.38 k.2–3; NĐ 356 Đ.41): doanh nghiệp nhỏ/khởi nghiệp được chọn không làm Đ.21, Đ.22 (hồ sơ đánh giá tác động xử lý) trong 5 năm; hộ kinh doanh, doanh nghiệp siêu nhỏ không phải làm — **trừ** khi kinh doanh dịch vụ xử lý DLCN, xử lý DLCN nhạy cảm, hoặc từ **100 nghìn** chủ thể trở lên. Khách Bank/Telco gần như luôn thuộc phần "trừ".

## 1. Luật 91/2025/QH15 + NĐ 356/2025/NĐ-CP — Bảo vệ dữ liệu cá nhân (nền chung mọi ngành)

| # | Điểm kiểm | Căn cứ (Điều/Khoản) | PRD phải ghi gì | Có trong PRD? |
|---|---|---|---|---|
| 1 | Xác định rõ **dữ liệu cá nhân cơ bản** và **nhạy cảm** được xử lý | Luật Đ.2 k.1–3; NĐ 356 Đ.3 (danh mục cơ bản), Đ.4 (danh mục nhạy cảm) | Bảng loại dữ liệu × nhóm. Lưu ý NĐ Đ.4 k.1 điểm k, l: thông tin tài khoản/thẻ/lịch sử giao dịch ngân hàng, tín dụng và dữ liệu theo dõi hành vi dùng viễn thông là **nhạy cảm** — hầu hết giải pháp Bank/Telco chạm nhóm này | ☐ |
| 2 | Căn cứ xử lý: sự đồng ý, hoặc trường hợp **không cần đồng ý** | Luật Đ.9 k.1; Đ.19 k.1 (điểm a–đ), k.2 (cơ chế giám sát bắt buộc khi không xin đồng ý) | Mỗi luồng dữ liệu ghi căn cứ. Dùng Đ.19 thì phải có quy trình, đánh giá rủi ro, kiểm tra định kỳ, kênh tiếp nhận phản ánh (Đ.19 k.2) | ☐ |
| 3 | Cơ chế thu thập **sự đồng ý** và **rút lại** đồng ý | Luật Đ.9 k.2–4 (tự nguyện, biết rõ loại dữ liệu/mục đích/bên kiểm soát/quyền; từng mục đích; "Sự im lặng hoặc không phản hồi không được coi là sự đồng ý"); Đ.10; NĐ 356 Đ.6 (phương thức kiểm chứng được, lưu trữ sự đồng ý, cấm mặc định đồng ý, báo rõ khi là dữ liệu nhạy cảm) | Màn hình/luồng xin đồng ý theo từng mục đích, không tick sẵn; nơi lưu bằng chứng đồng ý; luồng rút lại. Ngân hàng: nội dung xin đồng ý theo NĐ 356 Đ.8 k.2 (mục đích kể cả chấm điểm tín dụng, nguồn thu thập, thời gian lưu trữ, cách rút lại và chính sách xoá) | ☐ |
| 4 | **Quyền của chủ thể** được hệ thống hỗ trợ, đúng thời hạn | Luật Đ.4 k.1 (biết; đồng ý/rút lại; xem, chỉnh sửa; yêu cầu cung cấp, xoá, hạn chế, phản đối; khiếu nại…), k.5; NĐ 356 Đ.5 | Chức năng tiếp nhận yêu cầu + SLA theo NĐ Đ.5: phản hồi **02 ngày làm việc**; rút lại/hạn chế/phản đối thực hiện **15 ngày**; xem/chỉnh sửa/cung cấp **10 ngày**; xoá **20 ngày** (có thời hạn riêng khi phải yêu cầu bên xử lý/bên thứ ba; gia hạn tối đa 01 lần) | ☐ |
| 5 | **Sơ đồ luồng dữ liệu** — đi đâu, lưu ở đâu, ai truy cập, có ra khỏi hạ tầng khách không | NĐ 356 Đ.19 k.3 điểm c (sơ đồ luồng dữ liệu là nội dung bắt buộc của báo cáo đánh giá tác động); Đ.18 k.3 điểm c | Sơ đồ đủ để đưa thẳng vào hồ sơ đánh giá tác động | ☐ |
| 6 | **Chuyển dữ liệu xuyên biên giới** (kể cả dùng cloud/nền tảng ở nước ngoài) | Luật Đ.20 k.1 (3 trường hợp, gồm dùng nền tảng ngoài lãnh thổ), k.2 (lập hồ sơ, gửi bản chính trong **60 ngày** từ lần chuyển đầu), k.6 (miễn trừ); NĐ 356 Đ.17, Đ.18 (hồ sơ: Mẫu 09 + hợp đồng + chính sách) | Xác định có chuyển xuyên biên giới không (API mô hình AI đặt ở nước ngoài cũng tính theo Đ.20 k.1 điểm c); nếu có: ai lập hồ sơ, hạn 60 ngày | ☐ |
| 7 | Masking/khử nhận dạng, **mã hoá** | Luật Đ.12 k.1 ("dữ liệu cá nhân sau khi được mã hóa vẫn là dữ liệu cá nhân"); Đ.14 k.6 (khử nhận dạng, cấm tái nhận dạng); Đ.2 k.1 (sau khử nhận dạng không còn là DLCN); NĐ 356 Đ.12 k.4 (trên cloud "phải được mã hóa ở trạng thái nghỉ và truyền") | Quy tắc masking trong log/DB/màn hình; mã hoá at-rest + in-transit nếu dùng cloud; không coi dữ liệu đã mã hoá là hết nghĩa vụ | ☐ |
| 8 | **Thời hạn lưu trữ** & quy trình xoá/huỷ | Luật Đ.3 k.3 (lưu trong thời gian phù hợp mục đích); Đ.14 k.1 (6 trường hợp xoá, huỷ), k.3 (biện pháp an toàn, chống khôi phục trái phép), k.5 (không xoá được thì báo chủ thể) | Bảng thời hạn lưu theo loại dữ liệu; cơ chế xoá an toàn; ngoại lệ Đ.19 | ☐ |
| 9 | Ứng phó sự cố lộ, mất dữ liệu | Luật Đ.23 (thông báo vi phạm — ⚠️ chưa trích nguyên văn); NĐ 356 Đ.28 (nội dung thông báo); **Ngân hàng/tín dụng:** NĐ 356 Đ.8 k.3 — thông báo cơ quan chuyên trách và chủ thể "trong thời hạn không quá 72 giờ" sau khi phát hiện lộ, mất dữ liệu nhạy cảm | Quy trình sự cố có mốc 72 giờ cho khách tài chính; mẫu thông báo | ☐ |

### 1b. Điểm mới cần thêm (luật mới quy định, bản NĐ 13 cũ chưa có trong checklist)

| # | Điểm kiểm | Căn cứ | Có trong PRD? |
|---|---|---|---|
| 9a | **Hồ sơ đánh giá tác động xử lý DLCN**: lập từ khi bắt đầu xử lý, gửi bản chính trong **60 ngày**; nội dung gồm mục đích, loại dữ liệu, sơ đồ luồng, đồng ý, lưu trữ/xoá, biện pháp bảo vệ, kết quả tự đánh giá tuân thủ, đánh giá rủi ro | Luật Đ.21 k.1, k.7; NĐ 356 Đ.19 k.2–4 (Mẫu 10, Mẫu 02a/02b) | ☐ |
| 9b | **Khách tài chính, ngân hàng, tín dụng:** áp tiêu chuẩn, quy chuẩn bảo vệ DLCN; tự đánh giá tuân thủ **01 năm/lần**; **ghi nhật ký toàn bộ hoạt động xử lý DLCN**; không dùng thông tin tín dụng để chấm điểm khi chưa có đồng ý | Luật Đ.27 k.1; NĐ 356 Đ.8 k.1 | ☐ |
| 9c | **Có AI xử lý DLCN:** phân loại theo mức rủi ro; thông báo chủ thể về xử lý tự động, giải thích nguyên tắc thuật toán, cho quyền không tham gia; kết quả suy luận của AI nhận diện được người cũng là DLCN; giám sát và trách nhiệm giải trình; tự đánh giá tuân thủ 01 năm/lần | Luật Đ.30 k.1, k.3, k.4; NĐ 356 Đ.10 k.2, k.3, k.5 | ☐ |
| 9d | **Dùng điện toán đám mây:** hợp đồng với nhà cung cấp cloud nêu rõ tuân thủ pháp luật VN, luồng xử lý và vai trò, biện pháp bảo mật, thời hạn xử lý/xoá, bảo đảm quyền chủ thể; mã hoá nghỉ và truyền | Luật Đ.30 k.3; NĐ 356 Đ.12 k.2, k.4 | ☐ |
| 9e | **Vai trò các bên** (SHT thường là bên xử lý của khách): bên xử lý chỉ nhận dữ liệu sau khi có hợp đồng/thoả thuận xử lý, xử lý đúng hợp đồng | Luật Đ.2 k.7–9; Đ.37 k.2 điểm a, b | ☐ |

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
