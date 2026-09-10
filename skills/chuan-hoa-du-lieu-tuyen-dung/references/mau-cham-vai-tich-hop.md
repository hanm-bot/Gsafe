# Mẫu chấm ASK cho vai kỹ thuật/tích hợp (PO/BA payment, đặc tả API)

> Mở khi chấm ứng viên cho vai **sở hữu đặc tả kỹ thuật / tích hợp đa bên** (PO tích hợp thanh toán, BA hệ thống, PO nền tảng). Bổ sung cho §5–§5.1 của SKILL.md, không thay thế. Nguồn: pilot G30 "Sàng CV PO Payment SHT" (10/09/2026) — mỗi mục là quy tắc rút từ ca thật, không suy diễn.

## 1. Ánh xạ ASK ↔ domain JD kỹ thuật/tích hợp

Khi JD mô tả vai *kỹ thuật/tích hợp* nhưng khung chấm vẫn là ASK A30/S40/K30, đừng chấm theo câu chữ JD — ánh xạ domain vào 3 nhóm ASK bằng tiêu chí con (mỗi nhóm ≥4–6, mỗi tiêu chí 1 câu bằng chứng):

- **Knowledge (30%):** nghiệp vụ lõi (vd vòng đời giao dịch/Bill/đối soát/an toàn dòng tiền) · kiến trúc tích hợp (REST/webhook/callback/MQTT/RPC đồng bộ vs bất đồng bộ) · bảo mật (TLS/HMAC/chống replay/vòng đời khóa) · đọc–viết tài liệu kỹ thuật tiếng Anh · **[bối cảnh] khớp hệ sinh thái thật của SHT**.
- **Skills (40%):** viết & sở hữu đặc tả (envelope/mã lỗi/idempotency/versioning), không chỉ User Story/BRD chung · chuyển điều khoản hợp đồng → test case nghiệm thu/UAT/SLA · điều phối đa bên (đối tác/hãng thiết bị/ngân hàng) · Agile/backlog/mô hình hóa (BPMN/UML) · công cụ đặc tả–tích hợp (OpenAPI/Swagger, Postman, công cụ MQTT, sequence diagram) · **[bối cảnh] đã làm sản phẩm cùng loại** (POS/ví/cổng thanh toán/AFC).
- **Attitude (30%):** chủ động sở hữu/định hướng · học domain mới · kỷ luật versioning tài liệu · ổn định · giao tiếp đối tác.

**Ranh giới quan trọng (từ JD):** vai này **không yêu cầu lập trình**, nhưng **bắt buộc đọc hiểu & biên soạn đặc tả kỹ thuật**. Cho điểm S "viết đặc tả" cao chỉ khi có bằng chứng tự tay viết tài liệu API/tích hợp thật — không tính "tham gia UAT" hay "viết BRD sản phẩm B2C" là tương đương.

## 2. Tiêu chí bối cảnh mạnh nhất: khớp cựu công ty ↔ đối tác tích hợp trong JD

Ngoài "khớp nghiệp vụ thật của SHT" (§5.1), với vai tích hợp có một tín hiệu bối cảnh **mạnh và cụ thể hơn**: ứng viên **từng làm tại chính đối tác/hãng nêu trong JD**.

- Ca thật: JD PO Payment SHT nêu đối tác **VTC Pay, Ingenico, Sacombank**; một ứng viên từng làm **BizDev tại VTC Pay** — hiểu sẵn phía đối tác của luồng tích hợp. Cho điểm tiêu chí bối cảnh K5/S6 cao, **ghi rõ tên đối tác trùng khớp làm bằng chứng**.
- Tách tiêu chí này khỏi khớp câu chữ JD: khớp *tên đối tác* là bối cảnh; liệt kê đúng *đầu việc* JD là bề mặt.
- Cảnh báo ngược: "từng ở đối tác" là điểm cộng bối cảnh, **không** tự động thay cho chiều sâu đặc tả kỹ thuật — vẫn phải kiểm §1 (K2/K3/S1) và đóng ở phỏng vấn.

## 3. Mâu thuẫn domain-fit vs ASK-total — nêu rõ, không giấu sau con số

Ứng viên **đúng domain nhất** có thể **thua tổng ASK** một ứng viên broad hơn (mạnh kỹ thuật/giao hàng/ổn định). Đây là mâu thuẫn thật, không phải lỗi khung.

- Ca thật: Frank (domain thanh toán mạnh, từng ở VTC Pay) tổng 3.43 MIXED; Dũng (kỹ thuật + giao hàng + ổn định) tổng 3.61 HIRE — người đúng domain lại xếp dưới.
- Xử đúng: **trình cả hai điểm + nêu thẳng mâu thuẫn cho người quyết** — "ưu tiên domain/đối tác → chọn A; ưu tiên năng lực đặc tả + giao hàng → chọn B". Không tự chọn hộ bằng cách nâng/hạ trọng số cho ra kết quả mình thích.
- Đây là mở rộng của §5.4 (dải điểm cắt ngưỡng): ở đây không phải nhiều người chấm, mà **một phép chấm để lộ hai ưu tiên tuyển dụng khác nhau** — quyết định thuộc về người, AI chỉ làm rõ đánh đổi.

## 4. Điều kiện loại trừ nhanh (giúp sàng)

Vai tích hợp có tiêu chí loại trừ rõ trong JD — dùng để hạ nhanh, vẫn kèm bằng chứng:
- Chỉ có kinh nghiệm CĐS/vận hành nội bộ hoặc sản phẩm B2C, **chưa chạm hệ thống giao dịch/tích hợp đối tác** → K/S domain rất thấp (vd ca thật ứng viên hạ tầng IT: tổng 2.57 NO HIRE cho vai này, dù giỏi hạ tầng).
- **Chưa từng tự viết một đặc tả API/tích hợp thật** → S1 thấp.
