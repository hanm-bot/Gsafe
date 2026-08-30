---
name: "ra-soat-hop-dong-vendor"
description: "Rà soát, đối chiếu và phân tích khoảng trống (gap analysis) hợp đồng CNTT, chuỗi hợp đồng nhiều bên (back-to-back), SoW/BRD, license phần mềm và phân lớp trách nhiệm kỹ thuật - thương mại. LUÔN dùng skill này khi người dùng yêu cầu \"rà soát hợp đồng\", \"gap analysis hợp đồng\", \"đối chiếu spec với hợp đồng\", \"kiểm tra rủi ro back-to-back\", \"rà soát license\", \"kiểm tra SoW/BRD\", \"chuỗi hợp đồng mua bán CNTT\", kể cả khi chỉ gửi tập hồ sơ hợp đồng scan/text kèm yêu cầu đánh giá trước khi ký. KHÔNG dùng skill này để chuẩn hóa hồ sơ scan/PDF đa định dạng chung chung (dùng `chuan-hoa-ho-so-tai-lieu`), không dùng cho Quyết định nhân sự (dùng `sht-qd-nhansu-alignment`), và không dùng cho tài liệu dự án XDCB/nội thất (dùng `chuan-hoa-du-lieu-du-an`)."
---

# Rà soát hợp đồng CNTT — Gap Analysis, Chuỗi & Đặc tả (SHT)

Quy trình chuẩn hóa để rà soát hợp đồng và đặc tả CNTT trước khi ký kết. Kế thừa toàn bộ nguyên tắc nền tảng từ `sht-nen-tang-kiem-chung` (đo lường trước kết luận sau, đếm bằng máy, một bản có hiệu lực, checklist bàn giao).

Ba chế độ rà soát, chọn theo cấu trúc hồ sơ:
- **Chế độ A — Hai văn bản:** Đối chiếu tài liệu yêu cầu chủ đầu tư với đề xuất/hợp đồng vendor.
- **Chế độ B — Chuỗi hợp đồng:** Khi tổ chức vừa mua vừa bán (nhà tích hợp, phân phối, BOT) — chuỗi Mua vào → Bán ra.
- **Chế độ C — Nhiều giai đoạn:** Cùng một nền tảng tích tụ chức năng qua nhiều SoW/BRD/Phase theo thời gian.

---

## NGUYÊN TẮC CỐT LÕI — KHOẢNG TRỐNG CAM KẾT
1. **Người dùng chọn xong = lệnh thực thi:** Khi người dùng đã chọn phương án hoặc nói "tiếp tục", hành động đầu tiên là gọi công cụ đọc file/phân tích, câu xác nhận viết sau.
2. **Xác nhận hồ sơ đủ trước khi kết luận:** Thiếu loại văn bản nào thì nêu rõ chưa kết luận được, không kết luận trên phần đã có.
3. **Đọc điều khoản theo hai chiều:** Vừa tìm rủi ro bất lợi, vừa tìm quyền đã được cấp mà chưa dùng (như quyền sublicense, quyền chọn vendor).
4. **Không khuyến nghị kiến trúc cho một lớp trước khi đọc đặc tả lớp kề:** Chưa có tài liệu thì chuyển thành câu hỏi.
5. **Ghi nhận điểm tốt của đối tác:** Nêu cụ thể điểm tích cực để tăng độ tin cậy phần phê bình.
6. **Đính chính công khai:** Nếu bản trước phát hành có lỗi, xuất bản mục đính chính kèm nguyên nhân kỹ thuật.

---

## GIAI ĐOẠN 0 — CHUẨN HOÁ DỮ LIỆU & ĐIỀU TRA HỒ SƠ

### 0.1 Quét và kiểm kê danh mục hồ sơ
Quét toàn bộ thư mục và đối chiếu danh mục cần thiết cho chuỗi hợp đồng:
- Thỏa thuận khung / Thỏa thuận phân phối với nhà cung cấp.
- PO hoặc hợp đồng mua vào — **từng đợt, từng giai đoạn**.
- SoW / Statement of Work & BRD — **từng giai đoạn**.
- Hợp đồng bán ra cho khách hàng cuối & Giấy chứng nhận license phần mềm.
- Biên bản nghiệm thu, danh mục serial, đặc tả bên thứ ba được dẫn chiếu.

> Nếu phát hiện thiếu: Hỏi thẳng người dùng: *"Hồ sơ hiện thiếu [loại văn bản]. Anh có bản bổ sung không, hay tôi phân tích trên phần hiện có và ghi rõ phần chưa kết luận được?"*

### 0.2 Đọc hồ sơ hợp đồng

Kỹ thuật chuyển đổi và bóc tách mọi định dạng (`.doc`, `.docx` có bảng, `.xlsx`, PDF scan tiếng Việt): theo `chuan-hoa-ho-so-tai-lieu` §1.1. **Tuyệt đối không dùng OCR tiếng Việt** — quy tắc đó thuộc skill kia, đọc ở đó trước khi bắt đầu.

Hai phép đọc chỉ dùng cho hợp đồng:

- **Đo tỷ lệ tương đồng** giữa yêu cầu của SHT và phụ lục kỹ thuật vendor nộp. Nếu > 95% → vendor chép nguyên văn, hàm lượng kỹ thuật bằng không; ghi thành cảnh báo đỏ.
- **Diff giữa các phiên bản hợp đồng** — **điều bị xóa quan trọng hơn điều được thêm.** Luôn liệt kê phần mất trước phần thêm.

---

## GIAI ĐOẠN 1 — PHÂN TÍCH GAP & ĐỐI CHIẾU KỸ THUẬT

### 1.1 Phân rã Scope of Work (Workstreams WS1–WS10)
Phân rã phạm vi thành các luồng độc lập: WS1 Phần mềm thiết bị · WS2 Nền tảng OS/firmware · WS3 Truyền thông thiết bị ↔ máy chủ · WS4 Điều khiển từ xa · WS5 Tích hợp bên thứ ba · WS6 Chứng nhận & Tuân thủ · WS7 Backend · WS8 Hạ tầng HA/DR · WS9 Đào tạo & Chuyển giao · WS10 Escrow & Tính liên tục.

### 1.2 Đếm cam kết đầu ra so với nguồn đầu vào
Liệt kê từng hạng mục đơn lẻ đã cam kết ở đầu ra, tìm văn bản đầu vào tương ứng. Đếm theo **từng hạng mục đơn lẻ**, không gộp cụm (ví dụ: chứng nhận 6 tổ chức thẻ phải lập 6 dòng riêng).

### 1.3 Bảng đối chiếu chéo tham số định lượng
Lập bảng đối chiếu giữa các nguồn và yêu cầu cho các tham số nhạy cảm: Số thiết bị vs Số license · Kết nối đồng thời · Thời gian phản hồi · Timeout · Heartbeat · Dung lượng · Thời hạn bảo hành. Chỗ trống cũng là dữ liệu.

### 1.4 Kiểm tra dẫn chiếu đặc tả
- **Dẫn chiếu nội bộ:** So sánh tài liệu được dẫn chiếu ở Scope vs Assumptions vs Phụ lục Đặc tả (Attachment A). Ưu tiên kiểm tra Phụ lục Đặc tả vì đây là phần ràng buộc pháp lý.
- **Tham chiếu treo:** Đối chiếu tập ký hiệu dùng trong nội dung (`[API]`, `[IPC]`) với bảng References.
- **Lệch định danh tệp:** Tên file thực tế vs Tên file hợp đồng dẫn chiếu vs Ngày trong nội dung.

### 1.5 Trôi phiên bản & Phân biệt Năng lực vs Chứng nhận
- **Kiểm toán trôi phiên bản (Chế độ C):** Lập bảng Đặc tả × Giai đoạn để phát hiện phiên bản trôi dạt hoặc mất định danh.
- **Phân biệt Năng lực vs Chứng nhận:** Năng lực phần cứng (như EMV L1) khác hoàn toàn Chứng nhận ứng dụng (EMV L3 từng tổ chức thẻ). Datasheet ghi hỗ trợ không đồng nghĩa đã có chứng nhận.

### 1.6 Kiểm tra Danh mục Cảnh báo đỏ (Red Flags)
Tra cứu chi tiết 7 nhóm rủi ro chí tử tại `references/red-flags-hop-dong.md`:
1. Rủi ro Phạm vi (Scope traps).
2. Rủi ro Kiến trúc & Giao thức truyền thông.
3. Rủi ro An ninh & Masking dữ liệu thẻ/PII.
4. Rủi ro Giấy chứng nhận LICENSE (hạn dùng, cấm bên thứ 3, định lượng node).
5. Rủi ro Nghiệm thu & SLA Vận hành (deemed acceptance, back-to-back SLA).
6. Rủi ro Mã nguồn & IP (Source code escrow, OSS compliance).
7. Rủi ro Thương mại & Pháp lý Việt Nam (trần lãi 20% Đ468 BLDS, trần phạt 8% Đ301 LTM).

---

## GIAI ĐOẠN 1B — PHÂN TÍCH CHUỖI HỢP ĐỒNG (Chế độ B)

### 1B.1 Bản đồ chuỗi & Bảng đối chiếu Back-to-Back
- Lập bảng luồng: Nhà cung cấp → Nhà tích hợp → Khách hàng cuối.
- Đối chiếu song song điều khoản Mua vào và Bán ra: Luật áp dụng · Chế tài chậm tiến độ · Trần trách nhiệm · Bất khả kháng · SLA · Thời hạn nghiệm thu.
- **Tìm điều khoản chặn Back-to-back:** Điều khoản dạng *"Điều kiện mua hàng của khách hàng không có hiệu lực với nhà cung cấp"*.

### 1B.2 Định lượng khoảng trống truy đòi & Dòng tiền
- Lập bảng 3 cột: Mua vào — Bán ra — Biên lãi. Tuyệt đối không nhầm chênh lệch giá mua/bán là "mức tăng giá".
- So sánh khoảng trống trách nhiệm tối đa với tổng biên lãi toàn chuỗi.
- Đánh giá lệch pha dòng tiền: Mốc chi cho vendor vs Mốc thu từ khách hàng cuối.

---

## GIAI ĐOẠN 2 — KẾT XUẤT BÁO CÁO

Năm dạng báo cáo chuẩn, quy tắc chọn dạng, kỹ thuật xuất PDF/Excel và bước quét `grep` xác minh: theo `sht-nen-tang-kiem-chung` §6. Không định nghĩa lại ở đây.

Riêng cho rà soát hợp đồng:

- **Bản đầy đủ** dựng theo **12 mục tiêu chuẩn** của báo cáo gap analysis, kèm bảng đối chiếu chi tiết từng Workstream.
- **Bản thuần kỹ thuật** tập trung SoW, Specs, ICD, Kiến trúc — bắt buộc chạy bước quét từ khóa tiền tệ ở nền §6.2 trước khi gửi ra ngoài.
- **Bản điều hành** nêu đúng 3 vấn đề cần quyết, không dàn trải.

### 2.1 Danh mục Specs & PRD cần bổ sung

Tra cứu 22 hạng mục tài liệu kỹ thuật chuẩn, phân bổ theo P0/P1/P2, tại `references/specs-prd-catalog.md`.

---

## SAI LẦM CẦN TRÁNH KHI RÀ HỢP ĐỒNG
| Sai lầm | Xử lý đúng |
|---|---|
| Trả lời rỗng khi người dùng chờ | Gọi công cụ đọc file ngay, viết phản hồi sau |
| Kết luận khi hồ sơ chưa đủ | Đối chiếu danh mục 0.1, hỏi người dùng, ghi rõ phần chưa kết luận |
| Lấy số trong tài liệu yêu cầu làm số thực tế | Số thực nằm ở PO, HĐ mua bán, biên bản nghiệm thu, serial |
| So giá mua vào với bán ra rồi gọi là "tăng giá" | Đó là **biên lãi**. Lập bảng 3 cột Mua - Bán - Biên trước khi kết luận |
| Bỏ qua Phụ lục Đặc tả | Phụ lục là phần ràng buộc pháp lý chính — kiểm tra trước phần thân |
| Hiểu "hỗ trợ" trong datasheet là "đã chứng nhận" | Phân biệt rõ **năng lực phần cứng** và **chứng nhận ứng dụng** |
| Đếm cam kết theo cụm | Đếm theo **từng hạng mục đơn lẻ** |
| Bỏ qua Giấy chứng nhận License | Rà soát license như một hợp đồng độc lập có trục rủi ro riêng |
| Chỉ tìm rủi ro, không tìm quyền | Tìm cả quyền có lợi chưa dùng (như quyền sublicense) |
