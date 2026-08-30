---
name: "chuan-hoa-ho-so-tai-lieu"
description: "Chuẩn hoá hồ sơ tài liệu dự án/pháp lý đa định dạng (PDF scan tiếng Việt, docx, xlsx, JSON) thành dữ liệu trích dẫn được có toạ độ trang và điều khoản, và kết xuất báo cáo đa góc nhìn (nội bộ, đối ngoại không đối kháng, điều hành). LUÔN dùng skill này khi người dùng yêu cầu \"chuẩn hóa hồ sơ\", \"đọc PDF scan tiếng Việt\", \"trích dẫn chứng cứ từ tài liệu\", \"đối chiếu hồ sơ pháp lý\", \"kiểm kê tài liệu dự án\", \"viết báo cáo đối ngoại không xung đột\", \"đối chiếu nhiều văn bản scan\", kể cả khi gửi tập tài liệu scan hỗn hợp kèm yêu cầu trích xuất chứng cứ. KHÔNG dùng skill này cho rà soát hợp đồng CNTT/SoW/Gap analysis chuyên sâu (dùng `ra-soat-hop-dong-vendor`), không dùng cho hồ sơ nhân sự (dùng `chuan-hoa-du-lieu-nhansu`), và không dùng cho tài liệu dự án XDCB/nội thất có bóc băng ghi âm (dùng `chuan-hoa-du-lieu-du-an`)."
---

# Chuẩn hoá hồ sơ tài liệu thành dữ liệu trích dẫn được (SHT)

Quy trình biến một thư mục hồ sơ hỗn hợp (PDF scan, docx, xlsx, JSON) thành tập dữ liệu **trích dẫn được và truy vết được có toạ độ**, rồi kết xuất thành báo cáo phù hợp cho từng đối tượng người đọc. Kế thừa toàn bộ nguyên tắc nền tảng từ `sht-nen-tang-kiem-chung`.

Nguyên tắc chi phối: **Một khẳng định chỉ có giá trị khi kèm được nguyên văn và toạ độ nguồn** (số trang, số điều, số dòng).

---

## NGUYÊN TẮC CỐT LÕI — DỮ KIỆN PHẢI MỞ LẠI ĐƯỢC
1. **Chép nguyên văn, không nhớ lại rồi viết:** Ghi số điều và số trang ngay lúc trích.
2. **Phân biệt ba loại phát biểu:** *Quan sát* (thấy trên văn bản) — *Suy luận* (rút ra từ quan sát) — *Giả định* (chưa có căn cứ). Gắn nhãn rõ ràng trong báo cáo.
3. **Đếm bằng máy, không đếm bằng mắt:** Mọi con số về số lượng đều phải qua `grep -c` hoặc script đếm.
4. **Xác định đúng chủ thể trước khi phân tích:** Đọc trang đầu xác định pháp nhân và Mã số thuế (MST). Cùng MST = cùng pháp nhân; khác MST = công ty liên kết (chứng cứ gián tiếp).
5. **Bản đầu chưa bao giờ đúng hoàn toàn:** Tài liệu ra ngoài tổ chức bắt buộc qua kiểm chứng độc lập bằng subagent.

---

## GIAI ĐOẠN 0 & 1 — KIỂM KÊ VÀ CHUYỂN ĐỔI THEO LOẠI FILE

### 0.1 Điều tra Metadata & Tính đầy đủ
- **Metadata:** Đọc Title, Pages, Producer, CreationDate bằng `pdfinfo`. Lệch số trang giữa 2 file cùng tên = bản in thiếu phụ lục.
- **Xác nhận tính đầy đủ:** Thiếu loại hồ sơ nào, hỏi ngay người dùng trước khi phân tích, ghi rõ phần chưa kết luận được.

### 1.1 Chuyển đổi định dạng văn bản
- **File `.doc`:** Chuyển sang docx: `soffice --headless --convert-to docx <file.doc>`.
- **File `.docx` có bảng:** Dùng script `scripts/docx_ordered_reader.py` để duyệt `body.iterchildren()`, giữ nguyên thứ tự đoạn văn và bảng.
- **File `.docx` thuần văn bản:** Chạy `pandoc --columns=250 -t plain`.
- **File `.xlsx`:** Đọc bằng `openpyxl` hai lượt (lượt 1 lấy formula, lượt 2 với `data_only=True` lấy cached value).
- **File `.pdf` scan tiếng Việt:** **TUYỆT ĐỐI KHÔNG DÙNG OCR (Tesseract).** Render ảnh bằng `pdftoppm -png -r 200` và giao subagent đọc trực tiếp từ ảnh thị giác (mỗi subagent ≤ 20 trang). Yêu cầu trích NGUYÊN VĂN, rà từ khóa CÓ/KHÔNG, ghi rõ trang mờ không đọc được.

---

## GIAI ĐOẠN 2 & 3 — TRÍCH DỮ KIỆN & CHUYỂN THÀNH LUẬN CỨ

### 2.1 Trích dữ kiện có toạ độ
- **Phép đếm:** Dùng `grep -c` đếm tần suất xuất hiện của từ khóa ("thuê", "chấm dứt", số điều khoản trách nhiệm bên A vs bên B).
- **Bảng đối chiếu chéo:** Lập bảng so sánh cùng một tham số trên nhiều văn bản (kể cả nguồn im lặng).
- **Dẫn chiếu nội bộ & Phụ lục:** So sánh thân văn bản với phụ lục để tìm mâu thuẫn (phụ lục tạo nghĩa vụ mà thân văn bản đã loại trừ).
- **Kiểm tra tình trạng ký:** Ghi nhận rõ phụ lục nào có/chưa có khối ký, con dấu, ô ngày hoặc dấu giáp lai.

### 3.1 Xếp hạng độ vững của luận cứ
- **Hạng A (Mạnh nhất):** Mâu thuẫn nội tại giữa 2 đoạn trong chính văn bản đó — đối phương không có đường lùi.
- **Hạng B:** Trái quy định pháp luật hiện hành — cần luật sư đối chiếu.
- **Hạng C:** Bất cân xứng thương mại — cơ sở để đàm phán thương lượng.

### 3.2 Đọc bản chất kinh tế & Quyền chưa dùng
- Đọc bản chất kinh tế: Phí sàn hay phí dịch vụ (xem biến thiên của tỷ lệ phí theo doanh số).
- Đọc hai chiều tìm quyền chưa dùng: Quyền chấm dứt không phạt · Điều khoản khách hàng ưu đãi nhất (MFN) · Quyền chọn nhà cung cấp.
- Lỗi hình thức là đòn bẩy trung tính: Dùng lỗi hình thức/phiên bản làm lý do để làm lại toàn văn hợp đồng thay vì vá phụ lục.

---

## GIAI ĐOẠN 4 — KIỂM CHỨNG BẮT BUỘC TRƯỚC PHÁT HÀNH

### 4.1 Tự kiểm bằng máy & Subagent độc lập
- **Tự kiểm:** Chạy `grep -c` trên file nguồn cho từng đoạn trích nguyên văn (phải trả về ≥ 1).
- **Reviewer độc lập:** Giao subagent đọc lại file scan gốc để kiểm chứng từng khẳng định và phát hiện 7 loại lỗi: Trích sai số mục · Gán nhầm nguồn · Phóng đại · Suy luận trình bày như quan sát · Đọc ngược chiều câu · Đếm thiếu · Lập luận trên dữ kiện chưa kiểm.

---

## GIAI ĐOẠN 5 — KẾT XUẤT BÁO CÁO

Năm dạng báo cáo chuẩn, quy tắc chọn dạng, kỹ thuật xuất PDF/Excel và bước quét `grep` xác minh: theo `sht-nen-tang-kiem-chung` §6. Không định nghĩa lại ở đây.

Riêng cho hồ sơ tài liệu:

- **Bản đầy đủ** bắt buộc mỗi dữ kiện đi kèm **toạ độ gốc** (điều/khoản/trang) — đây là điểm khác biệt của skill này, mọi luận cứ phải mở lại được đúng chỗ trong file nguồn.
- **Bảng luận điểm đàm phán** dựng từ bảng xếp hạng độ vững ở §3.1, không dựng lại từ đầu.

### 5.1 Viết bản đối ngoại không tạo xung đột

Đây là phần đặc thù nhất, không nằm ở tầng nền:

- Nguyên tắc chi phối: **chứng minh điều mình muốn cũng chính là điều đối phương muốn** (tối ưu dòng thu, giảm rủi ro thanh tra) — không phải làm nhẹ đi yêu cầu của mình.
- Chuyển đổi từ vựng đối kháng sang trung tính theo `references/tu-vung-trung-tinh.md`.
- Sau khi viết, chạy bước quét từ đối kháng và đặt rào chắn nội bộ theo nền §6.2.

### 5.2 Excel có công thức

Khi cần mở preview mà công thức chưa được tính, dùng `scripts/excel_xml_fix.py` để ghi cached values vào XML.

---

## SAI LẦM CẦN TRÁNH KHI BÓC TÁCH HỒ SƠ
| Sai lầm | Xử lý đúng |
|---|---|
| Tin tên file | Mở trang đầu đọc tên pháp nhân và Mã số thuế |
| OCR tiếng Việt trên văn bản pháp lý | Render ảnh và giao subagent đọc thị giác |
| Đọc .docx bằng docx.paragraphs rời rạc | Dùng `docx_ordered_reader.py` duyệt `body.iterchildren()` |
| Rút gọn bản nội bộ làm bản đối ngoại | Viết lại hoàn toàn từ góc nhìn lợi ích của người nhận |
| Chứng minh đối phương sai để thuyết phục | Chứng minh đề xuất của mình có lợi cho dòng doanh thu của họ |
| Đưa hết phát hiện vào bản đối ngoại | Phân loại: Dùng ngay / Giữ dự phòng / Không dùng |
| Tin là đã viết đủ hòa hoãn | Chạy grep quét từ đối kháng trên bản đối ngoại |
