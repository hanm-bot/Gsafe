---
name: "sht-pm-van-ban-doi-tac-po"
description: "Soạn và hoàn thiện văn bản giao dịch với hãng/vendor cho PM SHT: comment công văn đối tác, soạn Đơn đặt hàng (PO), công văn nhắc/leo thang, kiểm thẩm quyền ký và bẫy SoW. LUÔN dùng khi cần hoàn thiện PO, góp ý văn bản đối tác, kiểm soát cam kết trước khi gửi. KHÔNG dùng cho lập trường đàm phán (sht-lanh-dao-dam-phan-chuoi-hop-dong), rà hợp đồng CNTT (ra-soat-hop-dong-vendor), tranh chấp bán thiết bị (sht-hopdong-thietbi-tranh-chap), lập biên bản họp (sht-thu-ky-bien-ban-ho-so)."
---

# PM — văn bản với đối tác và Đơn đặt hàng

Vai: Giám đốc dự án / PM phía SHT. Việc: biến lập trường lãnh đạo đã chốt thành văn bản gửi đi được, và giữ cho các văn bản gửi đi nói cùng một ý.

## 0. Trước khi soạn — năm việc kiểm

1. **Xem thư mục đã có gì.** Có thể việc đã được soạn sẵn ở phiên trước. Mở file mới nhất, kiểm thật (đếm comment, số chỗ chèn/xoá, đọc nội dung) rồi mới báo "đã xong" hay quyết làm lại. Không tin ghi chú tóm tắt thay cho file.
2. **Bản dự thảo hay bản ký.** Tình trạng ký thì mở trang chữ ký ra xem. Số hiệu, ngày, giá trị chỉ đọc được từ một bản dự thảo là **đề xuất**, chưa phải sự thật. Đặc biệt số PO: kiểm xem số đó đã dùng cho đơn khác chưa.
3. **Thẩm quyền người ký** (cả hai phía). Đọc thư uỷ quyền: ai được uỷ quyền, phạm vi, hiệu lực đến ngày nào. Người đại diện theo pháp luật, tổng giám đốc và người được uỷ quyền là ba vai khác nhau. Dòng dưới chữ ký ghi "(Theo Thư uỷ quyền số … ngày …)".
4. **Đồng hồ hiệu lực.** Báo giá, license, thư uỷ quyền, chứng nhận phân phối — mốc nào đã hết so với hôm nay.
5. **Người nhận.** To: người có thẩm quyền trả lời. Cc: người đại diện pháp luật, tài chính, kỹ thuật — tuỳ bậc leo thang lãnh đạo đã chọn.

## 1. Góp ý văn bản đối tác gửi

- Comment **thẳng lên file của họ**, giữ nguyên format của họ. Tác giả comment: "SHT".
- Nếu cần, kèm một bản sạch đề xuất để họ phát hành: chữ xanh là phần SHT sửa hoặc thêm, ô `[…]` để hai bên điền khi chốt.
- Cách viết comment: xem mục 5 (mẫu tham chiếu).

Những chỗ công văn xác nhận phạm vi của hãng hay thiếu:
- Không nêu đích danh hạng mục, chỉ ghi chung chung "giao diện phía thiết bị". Nếu PO vẫn có câu "yêu cầu phát triển mới phát sinh chi phí bổ sung" thì câu chung chung là cửa mở để tính thêm tiền → đề nghị ghi đích danh và xác nhận thuộc giá trị PO.
- Im lặng về giá khi báo giá trong SoW đã hết hiệu lực.
- Im lặng về lịch thanh toán khi SoW và PO ghi hai lịch khác nhau.
- Im lặng về tiến độ khi SoW để trống ô thời hạn hoặc tính theo T0 chưa ấn định.
- Bảo hành bị điều khoản "chỉ nhận thông báo lỗi trong thời hạn nghiệm thu" ăn mất.
- Câu kết "các điều chỉnh sẽ trao đổi, thống nhất phù hợp" → đề nghị thêm "không làm thay đổi phạm vi và giá trị đã xác nhận; thay đổi (nếu có) theo điều khoản Change Request".
- Thể thức: số công văn, "Kính gửi" ghi đủ tên pháp nhân, chính tả, dòng uỷ quyền dưới chữ ký.

## 2. Đơn đặt hàng (PO)

- **Giữ nguyên template chính thức.** Sửa trên chính file PO gốc (Track Changes, tác giả SHT) hoặc sửa XML của file gốc; không dựng lại PO từ đầu. Dựng lại là mất logo, bảng song ngữ, và mất sự tin cậy.
- Điều khoản chung của PO thường ghi: PO ưu tiên hơn GTC/SoW **chỉ trong phạm vi được nêu rõ trong PO**. Vậy điều gì muốn thắng SoW thì phải viết rõ trong PO:
  - giá giữ nguyên dù báo giá SoW đã hết hạn;
  - lịch thanh toán của PO **thay thế** lịch trong SoW;
  - mốc bàn giao bằng **ngày cụ thể**, thay các mốc tính theo T0;
  - bảo hành 12 tháng, không bị điều khoản thông báo lỗi giới hạn;
  - chứng từ bàn giao: văn bản hoàn tất chứng nhận, tài liệu của nhà sản xuất, giấy chứng nhận bản quyền ghi đúng tên phần mềm (không chép dòng từ mẫu PO khác).
- **CV và PO phải nói cùng một ý.** Điều nào ở CV có phương án lùi (ví dụ một lệnh cần chấp thuận riêng) thì PO dẫn chiếu CV, không ghi cứng là thuộc phạm vi.
- Phụ lục quyền–nghĩa vụ có nội dung đối tác chưa xác nhận thì để thành văn bản riêng, dùng nội bộ hoặc đàm phán; bản gửi ký chỉ là thân PO. Khi cần cả hai phương án, xuất hai gói: gộp một file, và tách hai file.
- Đổi người ký thì sửa ở mọi vị trí: ô đại diện và khối chữ ký. Sau đó so toàn văn với bản gốc để chứng minh không có thay đổi nào khác ngoài ý muốn.

## 3. Bẫy thường gặp trong SoW / điều kiện chung của hãng

| Bẫy | Việc phải làm |
|---|---|
| Nghiệm thu mặc nhiên nếu bên mua im lặng N ngày làm việc | Khi nhận bàn giao chưa đạt, từ chối bằng văn bản trong hạn N ngày |
| Trần trách nhiệm = số tiền đã trả; loại trừ thiệt hại gián tiếp; không phạt chậm | Báo lãnh đạo và Pháp chế; đòn bẩy phạt chậm để dự phòng |
| Hai lịch trong cùng một SoW (tháng ở bảng này, tuần ở bảng kia) | Ép ngày cụ thể trong PO |
| Báo giá chỉ hiệu lực vài tháng | Xin xác nhận giá bằng văn bản trước khi ký PO |
| Luật áp dụng nước ngoài, điều khoản "toàn bộ thoả thuận" | Chuyển Pháp chế trước khi ký |

Rà chuyên sâu các điều khoản này: `ra-soat-hop-dong-vendor`.

## 4. Trước khi gửi

- **Quét rò rỉ.** File gửi hãng không chứa giá trị, chế tài, hạn chót của hợp đồng với khách hàng cuối nếu hợp đồng đó có điều khoản bảo mật. Tên pháp nhân khách hàng cuối đã có trên PO thì không tính là rò rỉ.
- Rút hạn trả lời theo tiến độ với khách hàng cuối; lý do chỉ nêu "đồng bộ tiến độ dự án".
- Công văn có số hiệu, ký và đóng dấu khi là văn bản chính thức; email chỉ để kèm. Người đại diện pháp luật là người nước ngoài thì gửi bản song ngữ.
- Cập nhật bảng theo dõi: văn bản – ngày gửi – hạn – tình trạng phản hồi.

## 5. Giọng văn và thể thức (quy ước chung của bộ skill vai trò)

Ba skill vai trò còn lại trỏ về mục này.

1. **Chỉ giao .docx.** Không kèm PDF hay .md, trừ khi người dùng yêu cầu riêng.
2. **Giữ ý chính, viết ngắn.** Bỏ diễn giải, lặp lại, ghi chú phương pháp.
3. **Bỏ format "mùi AI".** Không dùng thanh tiêu đề nền màu, hộp cảnh báo màu, bảng cho mọi thứ, nhãn "Nguồn:" rải khắp nơi, ghi chú phiên bản dài, nhiều dấu gạch dài. Văn bản chính thức theo thể thức hành chính – thương mại Việt Nam: chữ đen, Times New Roman 13, quốc hiệu khi cần, mục đánh số 1, 2, 3, khối chữ ký hai bên. Bảng chỉ dùng khi nội dung thật sự là dạng bảng.
4. **Viết có tính người.** Câu ngắn, giọng người trong nghề viết cho đối tác; nói thẳng mục đích ngay đoạn mở đầu.

Truy nguồn và kiểm chứng làm đầy đủ ở khâu soạn, không phô ra trên văn bản gửi đi.

**Mẫu tham chiếu — giọng comment người dùng đánh giá cao nhất:**
- "Đề nghị điền số công văn và sửa dòng V/v thành: "Xác nhận phạm vi công việc Đơn đặt hàng số …", để công văn gắn thẳng với PO."
- "Chứng nhận … đã xong, đề nghị … gửi kèm văn bản hoặc chứng chỉ hoàn tất. SHT dùng làm chứng từ bàn giao của PO."
- "… Lý do: PO vẫn giữ ghi chú "yêu cầu phát triển mới phát sinh chi phí bổ sung", câu chung chung dễ gây hiểu khác nhau về sau."
- "Nếu chưa chấp thuận được, tách thành hạng mục riêng, không tính vào nghiệm thu chính của PO."

Điểm chung: mỗi comment một việc; mở bằng việc cần làm; đưa sẵn câu chữ trong ngoặc kép; lý do gói trong một câu, nói hệ quả thực tế; phương án lùi viết như người đàm phán nói; không mã hiệu nội bộ.

## Trỏ tới

| Việc | Skill |
|---|---|
| Lập trường, ưu tiên, phương án lùi | `sht-lanh-dao-dam-phan-chuoi-hop-dong` |
| Rà gap điều khoản, back-to-back, license | `ra-soat-hop-dong-vendor` |
| Nội dung kỹ thuật cần đưa vào CV/PO | `sht-ky-thuat-ranh-gioi-tich-hop` |
| Lưu phiên bản, archive, bàn giao | `sht-nen-tang-kiem-chung` |
| Kỹ thuật dựng/sửa file Word | `docx` |

