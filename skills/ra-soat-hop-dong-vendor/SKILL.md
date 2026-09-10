---
name: "ra-soat-hop-dong-vendor"
description: "Rà soát, đối chiếu và phân tích khoảng trống (gap analysis) hợp đồng CNTT, chuỗi hợp đồng nhiều bên (back-to-back), SoW/BRD, license phần mềm và phân lớp trách nhiệm kỹ thuật - thương mại. LUÔN dùng skill này khi người dùng yêu cầu \"rà soát hợp đồng\", \"gap analysis hợp đồng\", \"đối chiếu spec với hợp đồng\", \"kiểm tra rủi ro back-to-back\", \"rà soát license\", \"kiểm tra SoW/BRD\", \"chuỗi hợp đồng mua bán CNTT\", \"đối soát giấy phép\", \"giấy phép hết hạn\", \"hợp đồng này đã ký chưa\", \"đây là bản dự thảo hay bản ký\", kể cả khi chỉ gửi tập hồ sơ hợp đồng scan/text kèm yêu cầu đánh giá trước khi ký. KHÔNG dùng skill này để chuẩn hóa hồ sơ scan/PDF đa định dạng chung chung (dùng `chuan-hoa-ho-so-tai-lieu`), không dùng cho Quyết định nhân sự (dùng `sht-qd-nhansu-alignment`), và không dùng cho tài liệu dự án XDCB/nội thất (dùng `chuan-hoa-du-lieu-du-an`)."
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
3. **Đọc điều khoản theo hai chiều:** Vừa tìm rủi ro bất lợi, vừa tìm quyền đã được cấp mà chưa dùng (như quyền sublicense, quyền chọn vendor). Áp cả cho **điều khoản dẫn chiếu**: "Scope of Services = As in <BRD>" vừa là rủi ro (phạm vi mỏng, dễ bị phủ nhận hạng mục không nêu tên) vừa là quyền (phạm vi được định nghĩa **trọn** bằng BRD, nên mọi thứ trong BRD đều thuộc phạm vi đã ký). Viết ra cả hai kết luận trước khi chọn dùng cái nào.
4. **Không khuyến nghị kiến trúc cho một lớp trước khi đọc đặc tả lớp kề:** Chưa có tài liệu thì chuyển thành câu hỏi.
5. **Ghi nhận điểm tốt của đối tác:** Nêu cụ thể điểm tích cực để tăng độ tin cậy phần phê bình.
6. **Đính chính công khai:** Nếu bản trước phát hành có lỗi, xuất bản mục đính chính kèm nguyên nhân kỹ thuật.
7. **Mỗi khiếm khuyết phải có toạ độ tệp + phiên bản:** Câu hỏi đầu tiên không phải *"khiếm khuyết này nặng đến đâu"* mà *"khiếm khuyết này thuộc văn kiện nào"*. Không có toạ độ tệp thì **không** đưa vào văn bản gửi ra ngoài. Xem §0.2b.
8. **Ba nhãn phát biểu — gắn nhãn trước khi viết:** (a) **dữ kiện** có trong văn kiện đã ký của cả hai bên; (b) **vị thế của mình**, có căn cứ nhưng đối phương chưa xác nhận; (c) **suy luận** chưa có căn cứ văn bản. Chỉ loại (a) được phát biểu như sự thật. Loại (b) nêu đúng là quan điểm của mình kèm căn cứ; loại (c) chuyển thành câu hỏi.

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
- **Diff giữa các phiên bản hợp đồng** — **điều bị xóa quan trọng hơn điều được thêm.** Luôn liệt kê phần mất trước phần thêm. **Ghi rõ mốc so sánh** ("bản X so với bản Y") ngay cạnh mọi con số đếm được; một báo cáo ghi "xấu hơn 10 điểm" mà không nêu so với bản nào sẽ bị đối tác bác lại.

### 0.2b Xác định tình trạng ký và gán toạ độ cho từng khiếm khuyết

Thư mục dự án gần như luôn chứa **cả bản dự thảo và bản đã ký** với tên tệp gần giống nhau. Một khiếm khuyết của bản dự thảo rất dễ bị gán cho bản ký — và đi thẳng vào công văn có số, có dấu, gửi ra ngoài.

Bốn bước, không rút gọn:

1. **Lập bảng tình trạng ký cho MỌI văn kiện** trước khi phân tích bất cứ điều khoản nào. Cột: tên tệp · số hiệu · ngày hiệu lực · **đã ký / dự thảo** · căn cứ kết luận.
2. **Kết luận "đã ký" hay "chưa ký" chỉ được đưa ra sau khi NHÌN trang chữ ký.** Với PDF scan: render trang cuối và các trang có khối chữ ký ra ảnh rồi đọc bằng mắt. Tìm ba dấu hiệu: chữ ký tay · con dấu · dòng tuyên bố loại "EXECUTED as an agreement". **Không** kết luận từ tên tệp, từ hậu tố `_draft`/`_final`, hay từ kết luận của một tài liệu phân tích khác.
3. **Ô ngày để trống không đồng nghĩa chưa ký.** Một văn kiện có thể đủ chữ ký và con dấu hai bên mà ô Date vẫn trống. Ghi nhận đúng: *"đã ký, ngày ký chưa xác định"* — rồi đưa việc chốt ngày ký vào danh mục cần làm rõ.
4. **Mỗi khiếm khuyết tìm được phải ghi kèm tên tệp + phiên bản + vị trí.** Trước khi đưa bất kỳ khiếm khuyết nào vào văn bản gửi đối tác, kiểm lại: khiếm khuyết này còn tồn tại ở **bản mới nhất đã ký** không, hay đã được sửa ở bản đó?
5. **Định danh đọc từ một BẢN DỰ THẢO không phải là định danh — nó là đề xuất.** Số hiệu, ngày, giá trị, tình trạng ký: nếu chỉ đọc được từ bản dự thảo thì gắn nhãn *"theo dự thảo, chưa kiểm chứng độc lập"* và **không** dùng làm định danh trong văn bản gửi ra ngoài cho tới khi có bản đã ký hoặc văn bản của đối tác xác nhận. Riêng SỐ HIỆU còn phải kiểm thêm một chiều nữa: **số đó có đang được dùng cho hạng mục khác không** — đối chiếu với toàn bộ đơn đặt hàng và hợp đồng đã ký trong hồ sơ trước khi coi nó là số của hạng mục mình đang xét.

> **Ba ca thật cùng một họ, cùng một phiên (03/09/2026)** — đọc đúng chữ, gán sai văn kiện: (a) tình trạng ký của một SoW; (b) khiếm khuyết dẫn chiếu thuộc bản dự thảo hay bản ký; (c) một số hiệu đơn đặt hàng mà bản dự thảo tự ghi, trong khi số đó đã được cấp cho hạng mục hoàn toàn khác và đã ký từ hai tuần trước. Ca (c) đi vào năm tài liệu trước khi bị bắt. Bài học: mức độ nghiêm trọng của khiếm khuyết là câu hỏi THỨ HAI; câu hỏi thứ nhất luôn là *"thuộc văn kiện nào, phiên bản nào"*.

> **Ca thật (03/09/2026).** Một công văn đã phát hành nêu Attachment A dẫn chiếu sai sang BRD của tổ chức thẻ khác. Nhận định đúng — nhưng đúng với **bản dự thảo** trước đó; bản đã ký đã sửa lỗi này. Nếu đối tác chỉ ra, toàn bộ độ tin cậy của các luận điểm còn lại bị ảnh hưởng. Song song, một tài liệu phân tích nội bộ kết luận SoW "chưa ký" trong khi bản scan có đủ chữ ký và con dấu hai bên.

### 0.3 Đồng hồ hiệu lực — dựng ngay, không để tới lúc phân tích điều khoản

Mọi mốc hiệu lực trong hồ sơ nằm rải ở các văn kiện khác nhau, nên không ai thấy mốc nào đã trôi qua. Lập **một bảng duy nhất**, cột cuối là "so với hôm nay":

| Loại mốc | Cần kiểm |
|---|---|
| Giấy chứng nhận license | Ngày cấp · thời hạn · ngày hết hạn · **có điều khoản tự động gia hạn không** |
| Hiệu lực báo giá | Số hiệu báo giá · đã phát hành chưa (ô ngày trống = chưa) · thời hạn hiệu lực |
| Hiệu lực giá trong SoW | Nhiều SoW giới hạn hiệu lực phí theo tháng kể từ ngày hiệu lực |
| Thư uỷ quyền người đại diện đối tác | Thời hạn — mọi văn kiện cần người đó ký phải hoàn tất trước mốc này |
| Giấy chứng nhận phân phối / uỷ quyền bán | Thời hạn · có tự động gia hạn không |
| Bảo hành | Mốc bắt đầu là ngày nghiệm thu **hoặc nghiệm thu mặc định** — phải xác định ngày cụ thể |
| Bảo lãnh thực hiện, bảo lãnh tạm ứng | Thời hạn hiệu lực chứng thư |

Hai quy tắc đọc bảng này:

- **Mốc đã trôi qua trên một hệ thống đang khai thác là cảnh báo đỏ, không phải việc hành chính.** Nêu trước mọi nội dung khác.
- **Đối chiếu tiến độ khắc phục với mức độ cấp thiết.** Nếu phương án gia hạn có tiến độ *giao hàng + cài đặt* dài hơn khoảng thời gian đã quá hạn, thì câu cần hỏi đối tác **không phải câu về giá** mà là *phương án bảo đảm liên tục trong thời gian chờ*.

### 0.4 Hệ tác nhân độc lập theo lớp (hồ sơ lớn, Chế độ B và C)

Với chuỗi từ ba lớp trở lên hoặc trên ~40 văn kiện, chia việc cho các tác nhân độc lập — một tác nhân một lớp. Cơ chế dispatch chung: theo `superpowers:dispatching-parallel-agents`. Bốn quy tắc riêng của rà soát hợp đồng:

1. **Mỗi tác nhân một tập văn kiện tách biệt hoàn toàn**, và **không** nhận kết luận của tác nhân khác làm đầu vào. Giá trị của hệ nằm ở chỗ chúng **bất đồng** — điểm bất đồng chỉ ra nơi cần kiểm chứng thủ công.
2. **Cấm tác nhân ghi file.** Chỉ đọc và trả báo cáo văn bản; chỉ người điều phối sản xuất deliverable. Giữ được nguyên tắc một-bản-có-hiệu-lực và loại bỏ xung đột ghi đè.
3. **Đóng khung schema đầu ra**, luôn có mục cuối *"phần chưa kết luận được"*. Không có mục này thì tác nhân lấp khoảng trống bằng suy đoán.
4. **Người điều phối tự mở bản gốc kiểm lại hai thứ:** mọi điểm hai tác nhân bất đồng, và **mọi cảnh báo đỏ định lượng**. Tác nhân có thể trích dẫn đúng nguyên văn nhưng hiểu sai cấu trúc bảng — lỗi này rất khó thấy vì trích dẫn chính xác.

> **Vùng xám phải xử lý:** sau khi phân tập, liệt kê các tệp **không thuộc tập nào** và quyết định từng tệp — đọc, hay ghi nhận là cố ý bỏ. Đây chính là chỗ dễ sót nhất.

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
- **Lệch định danh tệp:** Tên file thực tế vs Tên file hợp đồng dẫn chiếu vs Ngày trong nội dung. Lệch một ngày hoặc lệch một hậu tố (`_update`, `_final`) trên tài liệu **định nghĩa phạm vi** là sai lệch phải xử lý bằng phụ lục — nếu hai bên đang giữ hai bản mang định danh khác nhau thì không xác định được bản nào ràng buộc khi nghiệm thu.
- **Chủ sở hữu tài liệu được dẫn chiếu:** Kiểm cột Owner trong bảng References. Nếu tài liệu đặc tả thuộc **bên thứ ba**, thì vendor chỉ có nghĩa vụ *tuân thủ theo*, không có nghĩa vụ *soạn ra* nó — muốn có tài liệu đặc tả thì phải biến nó thành **kết quả bàn giao có tên, có ngày, có tiêu chí nghiệm thu** trong một phụ lục hoặc yêu cầu thay đổi phạm vi.

### 1.4b Mâu thuẫn nội bộ trong CÙNG một văn kiện

Rà soát chuỗi có thiên hướng đối chiếu văn kiện A với văn kiện B và bỏ qua việc đối chiếu **bảng này với bảng kia trong cùng một văn kiện**. Mâu thuẫn nội bộ nguy hiểm hơn vì không bên nào có thể viện bản khác để giải thích.

Bắt buộc đối chiếu ba bảng trong mỗi SoW hoặc hợp đồng — **ba bảng phải kể cùng một câu chuyện**:

| Bảng | Kiểm gì |
|---|---|
| Bảng kết quả bàn giao (Deliverables) | Có bao nhiêu dòng? Hạng mục nào **không** xuất hiện ở đây thì chưa được cam kết bàn giao |
| Bảng tiến độ (Project Plan / Milestones) | Đơn vị thời gian là **tuần hay tháng**? Mốc T0 có được ấn định bằng văn bản chưa? |
| Bảng thanh toán (Fees / Payment schedule) | Từng đợt gắn với mốc nào? Đơn vị thời gian có khớp bảng tiến độ? Tỷ lệ % còn trong ngoặc vuông không? |

> **Ca thật (03/09/2026).** Cùng một SoW: bảng tiến độ ghi kiểm thử tích hợp tại T0+2,5 **tháng** và bàn giao tại T0+3 **tháng**; bảng thanh toán ghi bàn giao để kiểm thử tại T0+2 **tuần** và chạy thử tại T0+3 **tuần**. Lệch tới bốn lần, và 50% giá trị thanh toán gắn vào chỗ lệch đó. Mốc T0 cũng chưa được ấn định.

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

## GIAI ĐOẠN 2 — XUẤT BÁO CÁO GAP ANALYSIS

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
| Gán khiếm khuyết của bản dự thảo cho bản đã ký | Lập bảng tình trạng ký ở §0.2b trước; mỗi khiếm khuyết ghi kèm tên tệp + phiên bản |
| Kết luận "chưa ký" từ tên tệp hoặc từ tài liệu phân tích khác | **Render trang chữ ký và nhìn.** Ô ngày trống không đồng nghĩa chưa ký |
| Bỏ qua mốc hiệu lực đã trôi qua vì nó nằm rải ở nhiều văn kiện | Dựng đồng hồ hiệu lực §0.3 ngay ở Giai đoạn 0 |
| Chỉ đối chiếu văn kiện A với văn kiện B | Đối chiếu cả ba bảng trong CÙNG một văn kiện — §1.4b |
| Nhận cảnh báo đỏ định lượng của tác nhân mà không kiểm lại | Người điều phối tự mở bản gốc; tác nhân trích đúng chữ vẫn có thể hiểu sai cấu trúc bảng |
| Nêu con số diff mà không nêu mốc so sánh | Ghi "bản X so với bản Y" ngay cạnh mọi con số đếm được |
| Phát biểu vị thế của mình như dữ kiện đã được đối phương xác nhận | Gắn ba nhãn ở nguyên tắc cốt lõi #8 trước khi viết |
