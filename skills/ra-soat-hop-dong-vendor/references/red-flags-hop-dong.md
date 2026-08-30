# Danh mục Cảnh báo đỏ Rà soát Hợp đồng & SoW CNTT (SHT)

Tập hợp các điểm kiểm tra rủi ro chí tử khi rà soát hợp đồng, SoW, BRD và Giấy chứng nhận license trong các dự án CNTT.

---

## 1. Cảnh báo đỏ — Phạm vi (Scope)
- [ ] Phần mềm trên thiết bị giao cho ai? Ai sở hữu mã nguồn ứng dụng hiện hành? Có SDK và quyền ký số không?
- [ ] Đơn vị cấp phép có bao trùm hết phạm vi dự án thực tế?
- [ ] "Môi trường tương thích" có liệt kê đủ hệ thống bên thứ ba?
- [ ] Có điều khoản miễn trách khi bên thứ ba thay đổi API/giao thức không? Rủi ro dồn về ai?
- [ ] Định danh sản phẩm có nhất quán giữa tên file, tiêu đề, phụ lục?
- [ ] Backend nằm trong scope của ai, hay chỉ là giả định *"available and ready"*?
- [ ] Nhà cung cấp có làm lắp đặt và tích hợp hiện trường không? Thường là **không** — kiểm tra kỹ điều khoản GTC.

---

## 2. Cảnh báo đỏ — Kiến trúc & Kỹ thuật
- [ ] **Giao thức truyền thông có được định danh cụ thể?** Nếu chỉ ghi "pub/sub", đọc điều khoản OSS/bản quyền để suy ra stack thực tế.
- [ ] **Hai lớp có nói cùng giao thức?** Đọc đặc tả phía thiết bị trước. Nếu thiết bị đã chốt HTTP/cURL long-polling thì đừng khuyến nghị MQTT.
- [ ] Có cơ chế phát hiện thiết bị mất kết nối không? (HTTP long-polling không có Last Will & Testament).
- [ ] Quy ước topic, định dạng payload, trace ID có được đặc tả và **hai lớp có khớp nhau**?
- [ ] Tham số hiệu năng nhất quán không? (thời gian phản hồi vs timeout vs heartbeat).
- [ ] Có kiến trúc HA/DR, RTO/RPO cụ thể? Ai chịu trách nhiệm backup dữ liệu?
- [ ] Có mô hình tính toán dung lượng dựa trên cơ sở đo đạc thực tế?

---

## 3. Cảnh báo đỏ — An ninh & Dữ liệu
- [ ] Log có chứa dữ liệu nhạy cảm? (Với thiết bị thanh toán: PAN, track data, PIN block, CVV. Có đặc tả masking/truncation không?).
- [ ] Thiết kế logging mới ghi vào đâu? Nếu ghi vào thẻ nhớ trên thiết bị **đã chứng nhận bảo mật**, cần đánh giá tác động chứng nhận.
- [ ] Trách nhiệm tuân thủ chuẩn bảo mật thẻ (PCI-DSS) thuộc ai? Tìm điều khoản nhà cung cấp **từ chối trách nhiệm**.
- [ ] Xác thực thiết bị: chỉ TLS hay có mTLS? Có cơ chế cấp phát/thu hồi chứng chỉ (enrollment/revocation)?
- [ ] **Lệnh điều khiển hàng loạt** có cơ chế phê duyệt 2 người, rate limit, audit log không?
- [ ] Chuẩn mật mã có nhất quán giữa các giai đoạn? Có đặc tả quản lý khóa (Key Management)?
- [ ] Tấn công mạng có bị xếp là sự kiện bất khả kháng để miễn trách cho nhà cung cấp?

---

## 4. Cảnh báo đỏ — LICENSE (Trục rà soát độc lập)
Giấy chứng nhận license phải rà soát **như hợp đồng độc lập**, thường chứa ràng buộc chí tử có thể chặn đứng thiết kế đã bán cho khách.
- [ ] **Ngày hết hạn chính xác** — đối chiếu ngày hiện tại. Mốc hết hạn có khớp ngày ký cộng thời hạn?
- [ ] **Có điều khoản gia hạn không?** Thường là không có điều khoản tự động gia hạn.
- [ ] **License cấp cho ai?** Nếu cấp trực tiếp cho khách hàng cuối, nhà tích hợp **không phải một bên** nhưng vẫn bị ràng buộc nghĩa vụ.
- [ ] **Có cấm bên thứ ba truy cập?** Nếu có, mọi hệ thống của nhà tích hợp hoặc vendor khác gọi vào đều là vi phạm. Chế tài thường là **thu hồi license và buộc xóa phần mềm ngay lập tức**.
- [ ] **Giới hạn định lượng:** kết nối đồng thời, số terminal, số CPU/server — so sánh với số thực tế đang vận hành.
- [ ] **Neo kỹ thuật:** khóa vào Machine ID, MAC, hostname, serial? Có điều khoản cấp lại khi migrate hạ tầng hoặc kích hoạt DR?
- [ ] **Quyền cấp phép lại (sublicense):** có được phép cấp lại cho khách hàng cuối không? Tìm cả trong GTC và thỏa thuận khung. Đây là **quyền có lợi** thường bị bỏ sót.
- [ ] Giới hạn xuất xứ thiết bị; điều kiện thu hồi; thời hạn khắc phục vi phạm.

---

## 5. Cảnh báo đỏ — Nghiệm thu & Vận hành
- [ ] **Bộ Test case chốt trước hay sau khi ký?** Nếu sau khi ký: vendor tự định nghĩa tiêu chuẩn thành công.
- [ ] Có cơ chế **deemed acceptance / tự động nghiệm thu** không? Thời hạn kích hoạt là bao lâu?
- [ ] **So sánh thời hạn nghiệm thu đầu vào với đầu ra.** Nếu đầu vào ngắn hơn đầu ra, nhà tích hợp mất quyền từ chối trước khi khách hàng kiểm thử xong.
- [ ] **Điều khoản thông báo vi phạm bảo hành:** nếu yêu cầu thông báo trong thời hạn nghiệm thu ngắn, cam kết bảo hành dài hạn có thể bị vô hiệu hóa trên thực tế.
- [ ] **Phân loại mức độ nghiêm trọng có gắn thời gian phản hồi/khắc phục?** Nếu chỉ định nghĩa theo tỷ lệ test case mà không có thời gian cam kết, SLA không thể thực thi.
- [ ] So sánh SLA đầu vào với SLA đã cam kết đầu ra (Back-to-back SLA).
- [ ] Khung giờ hỗ trợ có khớp với khung giờ vận hành thực tế của khách hàng cuối?
- [ ] Có giai đoạn pilot/vận hành thử hiện trường không? Nghiệm thu cuối bắt buộc gắn với vận hành tải thực tế.
- [ ] Hồ sơ bàn giao có runbook, quy trình DR, tài liệu kiến trúc, sơ đồ mạng?
- [ ] **Cam kết vòng đời cung cấp linh kiện/phụ kiện thay thế** so với vòng đời khai thác dự kiến của hệ thống.
- [ ] Nâng cấp phiên bản phần mềm (minor/major patch) có thuộc phạm vi bảo hành hay phải ký SoW riêng?

---

## 6. Cảnh báo đỏ — Mã nguồn & Quyền Sở hữu Trí tuệ (IP)
- [ ] **Có điều khoản Ký quỹ mã nguồn (Source Code Escrow)?** Bắt buộc nếu vendor quy mô nhỏ hoặc hệ thống có vòng đời khai thác dài.
- [ ] Quyền sở hữu IP thuộc về ai? Nếu quyền chỉ là "revocable, non-exclusive, non-transferable" thì bên mua **không thể tự bảo trì hay chuyển giao**.
- [ ] Phần phát triển riêng theo đơn đặt hàng thuộc sở hữu của ai? Tách bạch rõ giữa "sản phẩm nền" và "phần tùy biến".
- [ ] Có điều khoản chống lách luật / độc quyền lĩnh vực (Non-circumvention / Non-compete)?
- [ ] Danh mục phần mềm nguồn mở (OSS) có đầy đủ không? Có bảng SBOM? Có cấm các license copyleft như GPL/AGPL trong thành phần phân phối thương mại?

---

## 7. Cảnh báo đỏ — Thương mại & Pháp lý (Việt Nam)
*(Bỏ mục này nếu người dùng yêu cầu báo cáo thuần kỹ thuật)*
- [ ] Lãi chậm thanh toán: kiểm tra mức trần tối đa 20%/năm theo Điều 468 Bộ luật Dân sự 2015.
- [ ] Phạt vi phạm hợp đồng: mức trần 8% giá trị phần nghĩa vụ bị vi phạm theo Điều 301 Luật Thương mại 2005.
- [ ] Giá đã bao gồm thuế VAT chưa? Bên nào chịu? Lưu ý: chuyển giao phần mềm và dịch vụ phần mềm không chịu thuế GTGT.
- [ ] **Chồng chế tài:** phạt vi phạm + hoàn trả + bồi thường 100% có thể dẫn tới tổng chế tài vượt 200% giá trị hợp đồng.
- [ ] Trần trách nhiệm bồi thường có tương xứng với rủi ro thiệt hại tiềm tàng không? Danh mục ngoại lệ có đầy đủ?
- [ ] Thời hạn hiệu lực của báo giá còn hay đã hết? Có điều kiện treo phát sinh chi phí không?
- [ ] Số liệu có nhất quán giữa chữ số và chữ viết? Có các trường để trống dạng `[INSERT]`, ngày chưa điền?
