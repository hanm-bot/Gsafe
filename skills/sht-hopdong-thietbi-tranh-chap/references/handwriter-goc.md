# HANDWRITER — ĐÚC KẾT PHIÊN LÀM VIỆC
## Rà soát HĐNT 145/2025/HĐNT/VPBANK-SHT & Xử lý tranh chấp hóa đơn – thuế
*Ngày: 20/08/2026 · Người dùng: Mr Hà (SHT) · Phạm vi: hợp đồng bán thiết bị mobiPOS cho VPBank*

---

## 1. NHỮNG VIỆC ĐÃ ĐẠT ĐƯỢC

**Rà soát hợp đồng (deliverable 1+2):**
- Đọc trọn 17 trang bản scan bằng render ảnh + đọc trực tiếp (không OCR), trích dẫn nguyên văn có truy vết trang/điều.
- Danh mục **56 vấn đề (32 P0, 17 P1, 4 P2, 3 ghi nhận tích cực)** — báo cáo Word 23 trang + Excel 5 sheet (Issue register lọc được, Tổng hợp, Định lượng có công thức, Việc làm ngay, Câu hỏi bắt buộc).
- Các phát hiện đắt giá nhất:
  - **Ô người có thẩm quyền ký nghiệm thu ĐỂ TRỐNG** trong bản đã ký (PL01 Đ4.7) — toàn bộ dòng tiền treo vào một ô chưa điền.
  - **3 dẫn chiếu treo** trong Điều 5 PL01 (trỏ nhầm sang Điều 3 thanh toán) — vô hiệu hóa chính lá chắn miễn trách bảo hành của SHT.
  - **License TMS Cloud** gộp "trọn đời" vào đơn giá trong khi bản chất có thể là subscription — rủi ro biên lãi lớn nhất.
  - **Giá một chiều**: SHT tăng tối đa 5% *kèm* VPBank phải đồng ý (= 0%), VPBank giảm bất kỳ lúc nào theo "nhận định đơn phương" (Đ1.5/Đ1.6 PL01).
  - **Không có trần trách nhiệm** + 4 điều khoản bồi thường không trần một chiều lên SHT.
  - **Đơn giá thực nhận sau khuyến mại 8/100 = 7.314.815 VNĐ**, không phải 7,9 triệu — con số đúng để so giá vốn.
  - Đỉnh vốn bảo lãnh vô điều kiện = **11,613 tỷ VNĐ** nếu chạy đủ tổng gói.

**Xử lý tranh chấp hóa đơn – thuế (deliverable 3+4):**
- Công văn **đanh thép** gửi Ban lãnh đạo VPBank: 3 phương án (nhận đủ 4.555 / nghiệm thu 1.755 / cùng trình diện cơ quan thuế), VPBank chịu 100% phạt, deadline 5 ngày làm việc, bảo lưu quyền khởi kiện, nơi nhận cc Thuế cơ sở 6.
- Công văn **giải trình mềm** gửi Thuế cơ sở 6: thừa nhận thẳng vi phạm → chứng minh nguyên nhân khách quan → cam kết nộp thuế TRƯỚC không chờ tranh chấp → bảng timeline khớp 9 tài liệu chứng cứ.
- Cả hai đều xuất Word + PDF, thể thức văn bản hành chính VN chuẩn, QA bằng render từng trang.

## 2. NHỮNG VIỆC CHƯA ĐẠT / CÒN TREO

- **Chưa kết luận biên lãi** — thiếu bảng tính giá vốn.
- Chưa có: license Ingenico (quyết định IP-01 + TM-05), các PO/BBNT đã phát hành, BRD MobiFone có phiên bản, Thỏa thuận liên danh Dagoras–SHT.
- Chưa chạy kịch bản Q&A cho buổi làm việc trực tiếp với đoàn kiểm tra thuế.
- Số 4.555 (PO 01) lệch số 4.200 (tổng gói PL01) — user xác nhận giữ 4.555, nhưng chênh lệch trên văn bản gốc vẫn là điểm cần đối chiếu khi có PO thực tế.

## 3. CHỖ MẮC LỖI & TƯ DUY SỬA

**Lỗi 1 — Map sai bản đồ hồ sơ, HAI LẦN.**
- Sai lần 1: tưởng HĐ SHT–VPBank FINAL R2 (SoundPOS) thuộc dòng mobiPOS. Sai lần 2: hiểu "MobiPOS vs VPBank" là đối chiếu nhánh MobiFone với nhánh VPBank.
- Gốc rễ: **suy đoán quan hệ các bên từ tên file và tiêu đề trước khi đọc trang định danh các bên**, và **nhầm MobiPOS là sản phẩm của MobiFone** — trong khi MobiPOS là nền tảng BOT do SHT đầu tư, hợp tác với MobiFone, Dagoras, VTCPay, Sacombank...
- Tư duy sửa (đã hiệu quả): khi user nói "map sai" — **dừng phân tích ngay, không giải thích, không đoán tiếp**. Xuất một bảng dữ kiện thô thuần túy: file → tiêu đề nguyên văn → số hiệu → ngày → các bên ghi TRÊN văn bản. Để user chỉ vào ô sai. Chỉ tiếp tục khi user xác nhận phạm vi bằng chữ của chính họ.

**Lỗi 2 — Hỏi phương pháp trước khi chốt đối tượng.**
- Đã hỏi "đối chiếu theo hướng nào" (back-to-back, 2 hợp đồng...) khi chưa chắc user muốn rà hợp đồng NÀO. Với hồ sơ đa dự án, câu hỏi đầu tiên phải là "**văn bản nào**", sau đó mới "**cách nào**".

**Lỗi 3 — Kỹ thuật nhỏ:** openpyxl không nhận ternary gán alignment (StyleProxy unhashable); scratch outputs bị dọn giữa phiên làm mất file docx.
- Tư duy sửa: **nguồn sự thật là script + data, không phải file output**. Giữ mọi script sinh văn bản trong thư mục làm việc → tái tạo deliverable bằng một lệnh. Chính điều này đã cứu công văn VPBank khi file biến mất.

## 4. TƯ DUY HAY / Ý TƯỞNG MỚI ĐÁNG GIỮ LẠI

1. **"Chỗ trống cũng là dữ liệu."** Ba phát hiện lớn nhất phiên này đều là thứ KHÔNG có trong hợp đồng: ô ký nghiệm thu trống, không điều khoản IP, không điều khoản PCI/an toàn dữ liệu thẻ.
2. **Đọc điều khoản hai chiều** — vừa tìm rủi ro vừa tìm quyền đang có: việc hợp đồng KHÔNG có độc quyền/non-circumvention là tài sản lớn nhất của mô hình BOT, phải bảo vệ trong mọi phụ lục sau.
3. **Phân biệt năng lực và chứng nhận**: EMV L1/L2 ≠ chứng nhận L3 từng tổ chức thẻ; PCI PTS (phần cứng) ≠ PCI DSS (hệ thống). Đ4.2k "hỗ trợ AMEX, UPI,… miễn phí" là bẫy chứng nhận.
4. **Đơn giá thực nhận sau khuyến mại** mới là giá so với giá vốn — mua 100 tặng 8 = chiết khấu 7,41%.
5. **Hai giọng văn cho hai đối tượng** trong cùng một vụ việc: đanh thép với đối tác thương mại (leverage = email từ chối + đề nghị ký biên bản sai thực tế của chính họ); mềm – thừa nhận – cam kết với cơ quan nhà nước (điều kiện xét tình tiết giảm nhẹ NĐ 125/2020).
6. **Cam kết nộp trước, đòi bồi hoàn sau**: tách nghĩa vụ với ngân sách khỏi tranh chấp dân sự — vừa đúng luật vừa là vị thế đàm phán.
7. **Nơi nhận cc cơ quan thuế** trong công văn gửi đối tác — một dòng, sức nặng lớn.
8. **Định lượng mọi rủi ro thành tiền** (trần phạt = 2,654 tỷ; 267 ngày chạm trần; 84 máy dự phòng = 663,6 triệu vốn chết) — báo cáo có sức thuyết phục hơn hẳn rủi ro định tính.
9. **Ghi nhận điểm tích cực của đối tác** (3 mục OK) — tăng độ tin cậy phần phê bình.

## 5. NHỮNG ĐIỀU CẦN CHÚ Ý VỀ SAU

- **MobiPOS = nền tảng BOT của SHT** — không bao giờ nhầm với MobiFone. SHT vừa bán thiết bị (Bên Bán) vừa vận hành nền tảng (BOT), hai vai này tạo xung đột tiềm tàng cần soi ở mọi hợp đồng.
- Văn bản pháp lý tiếng Việt scan: **render ảnh + đọc trực tiếp, cấm OCR tesseract** (chỉ có eng, sai dấu).
- Số liệu user cung cấp có thể lệch văn bản gốc (4.555 vs 4.200) — nêu lệch, hỏi một lần, dùng theo xác nhận của user và ghi chú lại.
- Trước khi phát hành bất kỳ văn bản đối ngoại nào: kiểm tra email/nhân sự đầu mối còn làm việc không (vụ vietld@).
- Mốc theo dõi: hạn phản hồi VPBank **28/8/2026**; hết hiệu lực HĐ **07/07/2027**; đàm phán gia hạn bắt đầu ngay.
