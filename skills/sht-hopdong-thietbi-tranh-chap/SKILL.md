---
name: sht-hopdong-thietbi-tranh-chap
description: "Rà soát hợp đồng bán thiết bị POS/SoundPOS của SHT (vị thế Bên Bán) và xử lý tranh chấp nghiệm thu, hóa đơn GTGT, kiểm tra thuế. LUÔN dùng khi rà soát hợp đồng/PO bán thiết bị, chậm nghiệm thu, xuất hóa đơn sai thời điểm, giải trình thuế, soạn công văn đanh thép gửi đối tác hoặc giải trình mềm gửi thuế. KHÔNG dùng cho hợp đồng mua sắm CNTT (ra-soat-hop-dong-vendor), tư vấn pháp chế chung (phap-che-doanh-nghiep), văn bản theo NĐ30 (sht-nen-tang-kiem-chung)."
---

# SHT — Rà soát hợp đồng bán thiết bị & Xử lý tranh chấp nghiệm thu, hóa đơn, thuế

Skill chuyên biệt cho SHT, đúc kết từ phiên rà soát HĐNT [SỐ_HĐ] (08/2026).
Dùng kèm skill tổng quát `ra-soat-hop-dong-vendor` khi cần gap analysis chuỗi nhiều lớp.
Làm việc bằng tiếng Việt. Deliverable mặc định: Word thể thức hành chính VN + Excel issue register.

---

## BỐI CẢNH CỐ ĐỊNH — đọc trước mọi việc khác

- **[SẢN_PHẨM_POS_C]/S-POS/SoundPOS là nền tảng do SHT đầu tư theo mô hình BOT** (Build–Operate–Transfer),
  hợp tác với [ĐỐI_TÁC_C], [ĐỐI_TÁC_D], [ĐỐI_TÁC_E], [NGÂN_HÀNG_B], [NGÂN_HÀNG_A]... **KHÔNG phải sản phẩm của [ĐỐI_TÁC_C].**
  Nhầm điểm này sẽ map sai toàn bộ quan hệ hợp đồng.
- SHT thường mang HAI vai đồng thời: **Bên Bán thiết bị** (hợp đồng mua bán) và **bên vận hành nền tảng**
  (hợp đồng hợp tác). Mọi rà soát phải soi xung đột giữa hai vai này.
- Đối tác ngân hàng soạn hợp đồng theo mẫu mua hàng của ngân hàng: đúng trần pháp luật
  nhưng phân bổ rủi ro nghiêng về Bên Mua. Góc nhìn rà soát mặc định: **bảo vệ SHT (Bên Bán)**.

## NƠI LƯU DELIVERABLE — kiểm trước khi kết thúc mọi việc

Nếu người dùng đã kết nối một thư mục trên máy của họ, **mọi deliverable cuối phải được lưu vào
thư mục đó**, không để lại trong thư mục outputs tạm của phiên. Thư mục tạm bị dọn giữa phiên
và không phải nơi người dùng tìm file về sau.

Cách làm: tạo thư mục con theo vụ việc, dạng `<Ten-vu-viec>_<YYYY-MM-DD>`, lưu vào đó:
- văn bản hoàn chỉnh (docx, xlsx, pdf),
- **kèm cả script sinh văn bản** (python-docx/openpyxl) — để tái tạo hoặc chỉnh sửa về sau
  mà không phải viết lại từ đầu.

Trước khi kết thúc lượt cuối, liệt kê thư mục đích và đối chiếu đủ số file. Đây là bước kiểm
chốt cuối, không phải việc tùy chọn — người dùng chỉ thấy công việc đã làm khi file nằm đúng chỗ họ mở.

## NGUYÊN TẮC SỐ 0 — CHỐNG MAP SAI HỒ SƠ

Lỗi nguy hiểm nhất không phải đọc sót điều khoản mà là **hiểu sai văn bản nào, bên nào, quan hệ gì**.

1. **Không suy đoán quan hệ các bên từ tên file hay tiêu đề.** Mở trang định danh các bên
   (Bên A/Bên B, Bên Mua/Bên Bán) của TỪNG văn bản trước khi xếp nó vào bản đồ hồ sơ.
2. Trình bản đồ hồ sơ cho người dùng **xác nhận trước khi phân tích**: bảng
   `Văn bản | Số hiệu | Ngày | Các bên (nguyên văn) | Sản phẩm/đối tượng`.
3. **Khi người dùng nói "map sai": dừng ngay, không giải thích, không đoán tiếp.**
   Xuất bảng dữ kiện thô thuần túy (chỉ những gì đọc được nguyên văn trên văn bản)
   và để người dùng chỉ vào ô sai. Chỉ tiếp tục khi họ xác nhận bằng chữ của chính họ.
4. Với hồ sơ đa dự án: hỏi "**rà văn bản NÀO**" trước, "**theo cách nào**" sau.
5. Số liệu người dùng cung cấp có thể lệch văn bản gốc (ví dụ [SỐ_PO] vs tổng gói [SỐ_LƯỢNG] trong phụ lục):
   nêu chênh lệch, hỏi một lần, dùng theo xác nhận của người dùng và ghi chú lại trong deliverable.

## KỸ THUẬT ĐỌC HỒ SƠ

- Hợp đồng scan tiếng Việt: `pdftoppm -jpeg -r 145` từng trang rồi **đọc ảnh trực tiếp bằng vision**.
  **Cấm OCR tesseract** cho văn bản pháp lý tiếng Việt (thường chỉ có gói eng, sai dấu nghiêm trọng).
- Trích dẫn phải **nguyên văn + số điều + số trang**. Không diễn giải lại rồi trích trong ngoặc kép.
- Xác nhận tính đầy đủ hồ sơ trước khi kết luận: mẫu Đơn đặt hàng, mẫu Biên bản nghiệm thu,
  license phần mềm bên thứ ba, BRD được dẫn chiếu, PO/BBNT đã phát hành, bảng giá vốn.
  **Thiếu văn bản nào thì phần liên quan ghi "chưa kết luận được" và chuyển thành câu hỏi bắt buộc — không suy đoán.**
- Giữ mọi script sinh văn bản (python-docx, openpyxl) trong thư mục làm việc:
  **nguồn sự thật là script + data, không phải file output** — file có thể bị dọn giữa phiên, script tái tạo được ngay.

## QUY TRÌNH A — RÀ SOÁT HỢP ĐỒNG BÁN THIẾT BỊ (vị thế Bên Bán)

Chạy checklist đặc thù tại `references/checklist-ben-ban.md` (bắt buộc đọc khi rà soát).
Các nhóm: Thương mại · Dòng tiền · Chế tài · Nghiệm thu · Bảo hành-SLA · SHTT-License ·
An ninh-Tuân thủ · Quyền-Nghĩa vụ · Pháp lý-Hình thức · Hồ sơ thiếu.

Nguyên tắc xuyên suốt:
- **"Chỗ trống cũng là dữ liệu."** Soi cả những gì hợp đồng KHÔNG có: trần trách nhiệm,
  điều khoản IP, điều khoản an toàn dữ liệu thẻ, ô để trống trong bản đã ký.
- **Đọc hai chiều**: tìm rủi ro VÀ tìm quyền đang có (không độc quyền, không non-circumvention
  = tài sản của mô hình BOT, phải bảo vệ trong mọi phụ lục sau).
- **Định lượng mọi rủi ro thành tiền** (trần phạt, đỉnh vốn bảo lãnh, vốn tồn kho dự phòng, số ngày chạm trần).
- **Đơn giá thực nhận sau khuyến mại** mới là giá so với giá vốn (mua 100 tặng 8 = chiết khấu 7,41%).
- **Ghi nhận điểm tích cực** của đối tác (mức OK) — tăng độ tin cậy phần phê bình.
- Phân mức: **P0** xử lý ngay không chờ đàm phán · **P1** đưa vào phụ lục điều chỉnh/vòng gia hạn · **P2** ghi nhận.
- Với hợp đồng ĐÃ KÝ đang vận hành: tách riêng nhóm **"Việc làm ngay bằng văn bản đơn phương/biên bản xác nhận"**
  khỏi nhóm phải đàm phán.

Deliverable: báo cáo Word (kiểm kê → tóm tắt điều hành với 3-4 con số cần nhớ → các vấn đề cần quyết
mỗi vấn đề kết bằng "Đề nghị quyết" → đối chiếu định lượng → danh mục đầy đủ → việc làm ngay →
câu hỏi bắt buộc → ghi nhận tích cực → đề xuất quyết định) + Excel issue register
(cột: Mã, Nhóm, Vị trí, Trích dẫn nguyên văn, Vấn đề, Mức, Tác động định lượng, Đề xuất, Trạng thái).

## QUY TRÌNH B — TRANH CHẤP NGHIỆM THU / HÓA ĐƠN / KIỂM TRA THUẾ

Tình huống điển hình: SHT giao hàng, đối tác không hoàn thành tiếp nhận-nghiệm thu và từ chối
phối hợp xuất hóa đơn → cơ quan thuế phát hiện "xuất kho bán hàng không xuất VAT".

**Hai công văn, hai giọng văn — đọc mẫu chi tiết tại `references/mau-cong-van.md`:**

1. **Gửi đối tác — giọng ĐANH THÉP** (văn phong quy phạm pháp luật, ngắn, sắc):
   Tóm tắt sự việc có ngày tháng + tài liệu chứng minh → quan điểm pháp lý (neo Điều 9 NĐ 123/2020/NĐ-CP:
   nghĩa vụ hóa đơn phát sinh khi chuyển giao, không phụ thuộc ý chí bên mua) → đưa 2-3 phương án
   cho đối tác chọn, phương án nào cũng gắn đối tác chịu chi phí phạt → thời hạn phản hồi cụ thể
   (5 ngày làm việc, giờ chốt) → bảo lưu quyền khởi kiện → **nơi nhận cc cơ quan thuế**.
   Leverage mạnh nhất: ghi lại nguyên văn các đề nghị sai trái của đối tác (ví dụ đề nghị ký biên bản
   không đúng thực tế) kèm khẳng định SHT đã từ chối.

2. **Gửi cơ quan thuế — giọng MỀM, THỪA NHẬN, CAM KẾT** (điều kiện xét tình tiết giảm nhẹ NĐ 125/2020/NĐ-CP):
   Thừa nhận thẳng vi phạm là có thật → chứng minh nguyên nhân khách quan bằng bảng dòng thời gian
   khớp từng dòng với danh mục tài liệu đánh số → chứng minh không che giấu doanh thu (thuế khâu nhập khẩu
   đã nộp, hồ sơ kho minh bạch) → **cam kết nộp thuế + tiền chậm nộp TRƯỚC, không chờ kết quả tranh chấp**
   → đề nghị hướng dẫn xử lý phần chưa nghiệm thu → kiến nghị mời đối tác cùng làm việc.
   Nguyên tắc: tách nghĩa vụ với ngân sách khỏi tranh chấp dân sự.

**Trước khi phát hành bất kỳ công văn nào:** kiểm tra nhân sự/email đầu mối còn làm việc tại SHT không.

## KỸ THUẬT SINH VĂN BẢN

- Công văn: python-docx, Times New Roman 13pt, A4, lề 2-3-2-1.5cm, **header 2 cột bằng bảng không viền**
  (không dùng tab), thân justify, thụt đầu dòng 1cm, khối ký + nơi nhận bằng bảng không viền.
  Dùng script mẫu `scripts/cong_van_template.py` làm khung.
- Số công văn và ngày để trống cho văn thư điền.
- QA bắt buộc: convert PDF → render ảnh → đọc lại từng trang trước khi giao.
- Excel: openpyxl; không gán alignment bằng biểu thức ternary đọc-rồi-gán (lỗi StyleProxy unhashable);
  chạy recalc sau khi ghi công thức.

## BÀI HỌC GỐC

Toàn bộ đúc kết phiên gốc (lỗi đã mắc, tư duy sửa, phát hiện đắt giá) tại `references/handwriter-goc.md` —
đọc khi cần hiểu vì sao skill quy định như trên.
