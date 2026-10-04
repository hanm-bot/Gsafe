---
name: "lua-chon-tham-dinh-ncc"
description: "Lựa chọn và thẩm định nhà cung cấp CNTT: dựng đề bài kỹ thuật trung lập, soạn NDA/RFI, thiết kế bài test PoC có ngưỡng loại, chấm điểm và so sánh báo giá. LUÔN dùng khi cần chọn vendor CNTT, thẩm định năng lực đối tác, xử lý báo giá lệch nhiều lần, thiết kế bài thi PoC. KHÔNG dùng để rà soát hợp đồng đã chọn (ra-soat-hop-dong-vendor), thẩm định ý tưởng kinh doanh/thị trường (tham-dinh-thi-truong), đặc tả ranh giới hệ thống nội bộ (sht-ky-thuat-ranh-gioi-tich-hop)."
---

# Lựa chọn và thẩm định nhà cung cấp CNTT

Quy trình chọn nhà cung cấp cho dự án CNTT, từ chuẩn hoá đề bài tới quyết định có hồ sơ tự bảo vệ.

Làm việc bằng **tiếng Việt, ngôn ngữ kỹ thuật chuyên ngành**, trừ khi người dùng yêu cầu khác.

**Ranh giới với hai skill liên quan.** `chuan-hoa-ho-so-tai-lieu` lo tầng đọc và chuẩn hoá dữ liệu từ tệp thô. `ra-soat-hop-dong-vendor` lo tầng phân tích hợp đồng và chuỗi hợp đồng. Skill này lo tầng **chọn và thẩm định nhà cung cấp**. Khi cần đọc hồ sơ scan hoặc rà soát điều khoản hợp đồng, gọi skill tương ứng.

---

## NGUYÊN TẮC CỐT LÕI

1. **Mọi lượt phải kết thúc bằng một lệnh gọi công cụ hoặc một câu trả lời có nội dung. Không bao giờ kết thúc bằng rỗng.** Khi người dùng chọn phương án hoặc nói "tiếp tục", hành động đầu tiên là gọi công cụ, viết văn sau.
2. **Đề bài trước, báo giá sau.** Báo giá lệch nhau nhiều lần không có nghĩa một bên đắt — thường nghĩa là chưa có đề bài chung.
3. **Phân loại nhà cung cấp trước khi chấm điểm.** Nhà cung cấp thuần, đối thủ, và đối tác tiềm năng dùng ba khung đánh giá khác nhau.
4. **Ưu tiên bằng chứng không sao chép được.** Thiết bị chạy thật > khách hàng xác nhận > nhân sự trả lời > tài liệu nộp.
5. **Tiêu chí ký trước, kết quả sau.** Mọi bài kiểm chứng phải có tiêu chí đạt hoặc không đạt ghi thành văn bản trước khi thực hiện.
6. **Không gán nhãn nội dung cho tệp chưa đọc.** Khi liệt kê thư mục, chỉ ghi tên và dung lượng.
7. **Đọc điều khoản theo hai chiều** — tìm cả rủi ro lẫn quyền đã được cấp mà chưa dùng.
8. **Báo điểm chặn ngay.** Thiếu quyền, thiếu công cụ, tệp không đọc được: nói một câu và đề xuất đường vòng.

---

## GIAI ĐOẠN 0 — PHÂN LOẠI VÀ ĐỊNH KHUNG

### 0.1 Hỏi định hướng dài hạn TRƯỚC khi phân tích

Với quyết định chọn nhà cung cấp có yếu tố chiến lược, hỏi ngay từ đầu:

> Với đơn vị này, mục tiêu dài hạn của anh là **ngăn chặn** hay **hợp tác**?

Không hỏi câu này thì phân tích có thể đi sai hướng hoàn toàn và phải làm lại. Đây là nguyên nhân của việc nhận định đổi chiều nhiều lần.

### 0.2 Phân loại từng ứng viên

| Loại | Dấu hiệu | Khung đánh giá |
|---|---|---|
| **Nhà cung cấp thuần** | Không cạnh tranh phân khúc của mình; phụ thuộc mình để tiếp cận khách hàng | Chấm điểm theo trọng số kỹ thuật và thương mại thông thường |
| **Đối thủ** | Có sản phẩm hoặc nền tảng cạnh tranh cùng phân khúc; có đường tiếp cận khách hàng độc lập | **Trọng số kỹ thuật không còn áp dụng.** Bài toán chuyển từ tối ưu sang bảo vệ vị thế |
| **Đối tác tiềm năng** | Vừa cạnh tranh vừa bổ trợ; có thể trở thành kênh hoặc khách hàng | Đánh giá theo **bất đối xứng giá trị** — xem 0.3 |

**Cảnh báo:** cùng một đơn vị có thể chuyển loại khi biết thêm dữ kiện. Ghi rõ căn cứ phân loại để khi đổi thì biết đổi vì sao.

### 0.3 Bất đối xứng giá trị

Khi ứng viên là đối thủ hoặc đối tác tiềm năng lớn, luôn lập bảng:

| Hạng mục | Tính chất | Quy mô |
|---|---|---|
| Hạng mục đang tranh | Một lần / một dự án | |
| Quan hệ dài hạn có thể mất | Lặp lại / nhiều năm | |

Nếu quan hệ dài hạn lớn hơn nhiều lần, tranh hạng mục nhỏ là đổi cái lớn lấy cái nhỏ.

### 0.4 Xác định cổng chặn ngoài tầm kiểm soát

Liệt kê những điều kiện tiên quyết mà **mình không bảo đảm được** — thường là quyền từ hãng, giấy phép, chấp thuận của khách hàng cuối. Nếu có, đó là cổng chặn phải xử lý trước mọi việc khác, vì:

- Không có nó thì nhà cung cấp không khởi động được
- Không có nó thì chính mình cũng không tổ chức được PoC

---

## GIAI ĐOẠN 1 — CHUẨN HOÁ ĐỀ BÀI

> **Đây là giai đoạn tạo giá trị lớn nhất, và là thứ hay bị bỏ qua nhất.**

### 1.1 Dấu hiệu đề bài chưa chuẩn

- Các báo giá lệch nhau **trên 3 lần**
- Mỗi nhà cung cấp mô tả phạm vi một kiểu
- Tài liệu yêu cầu có mâu thuẫn nội tại
- Yêu cầu phi chức năng không có con số
- Ranh giới giữa các bên chưa chốt

Gặp bất kỳ dấu hiệu nào: **dừng so giá, dựng đặc tả trước.**

### 1.2 Dựng bản đặc tả yêu cầu kỹ thuật của chính mình

Không phải bản sao tài liệu khách hàng, mà bản đã sửa mâu thuẫn và bổ sung tham số. Cấu trúc:

| Mục | Nội dung |
|---|---|
| 0 | Hướng dẫn đọc — quy ước nhãn nguồn, ba quyết định nền tảng |
| 1 | Bối cảnh và **ranh giới tích hợp** — đánh mã RG-1, RG-2… |
| 2 | **Các quyết định nền tảng còn treo** — nêu phương án, yêu cầu báo giá riêng từng phương án |
| 3 | Định lượng cơ sở |
| 4 | Yêu cầu chức năng — đánh mã, đã sửa mâu thuẫn |
| 5 | **Yêu cầu phi chức năng định lượng** |
| 6 | Yêu cầu an ninh |
| 7 | Ràng buộc đã biết |
| 8 | Tiêu chí nghiệm thu, gồm **bài kiểm bắt buộc** |
| 9 | Ngoài phạm vi |
| 10 | Yêu cầu đối với hồ sơ chào |

### 1.3 Gắn nhãn nguồn cho từng con số

| Nhãn | Ý nghĩa | Mức ràng buộc |
|---|---|---|
| **NGUỒN** | Trích từ tài liệu khách hàng hoặc hợp đồng đã ký | Cứng, không đổi |
| **MÌNH** | Do mình xác định để bịt khoảng trống | Mềm, nhà cung cấp đề xuất khác được nếu có lập luận |
| **ĐO** | Cần đo thực tế trước khi chốt | Nêu phương pháp đo; giá điều chỉnh sau |

Tác dụng kép: nhà cung cấp biết chỗ nào thương lượng được, và khi khách hàng chất vấn thì mỗi con số truy được về nguồn.

### 1.4 Bịt khoảng trống tham số bằng suy luận có kiểm chứng

Khi tài liệu nguồn chỉ có hai mốc cách nhau quá xa, đặt tham số trung gian sao cho **đạt đúng mốc gốc một cách có kiểm soát**, không phủ định tài liệu nguồn.

Ví dụ đã dùng: nguồn chỉ có *phản hồi dưới 3 giây* và *báo lỗi trên 300 giây*. Bịt bằng: chu kỳ tín hiệu 60 giây → cảnh báo 180 giây (3 lần miss) → lỗi 300 giây (5 lần miss).

### 1.5 Danh mục tham số phi chức năng phải có số

Hiệu năng: thời gian phản hồi (nêu phân vị) · **chu kỳ tín hiệu định kỳ** · ngưỡng cảnh báo · ngưỡng lỗi · thời gian truy vấn · thời gian tải giao diện · mức ảnh hưởng tới nghiệp vụ chính.

Dung lượng: tần suất thu thập · thời hạn lưu trữ từng tầng · dung lượng phát sinh mỗi đơn vị mỗi ngày · ngưỡng cảnh báo dung lượng.

Sẵn sàng: tỷ lệ sẵn sàng · thời gian khôi phục mục tiêu · mức mất dữ liệu mục tiêu · chu kỳ sao lưu và **chu kỳ kiểm thử khôi phục**.

Mức dịch vụ: phân loại mức nghiêm trọng · **thời gian phản hồi và thời gian khắc phục cho từng mức** · khung giờ theo giờ vận hành của khách hàng cuối · chế tài.

**Kiểm tra thứ tự ưu tiên:** thời gian khắc phục phải tăng dần khi mức nghiêm trọng giảm dần. Đề xuất nào có mức nhẹ được xử lý nhanh hơn mức nặng là lỗi soạn thảo.

### 1.6 Yêu cầu bắt buộc trong hồ sơ chào

- **Báo giá riêng theo từng phương án** của các quyết định còn treo, không gộp một con số
- **Báo giá tách theo khối** để cho phép mua từng phần
- **Bảng đối chiếu theo từng mã yêu cầu**: đáp ứng đầy đủ / một phần / không, kèm giải thích. *Hồ sơ không có bảng này bị trả lại trước khi đánh giá.* Đây là biện pháp chặn hiệu quả nhất đối với hồ sơ sao chép.
- Kiến trúc đề xuất · mô hình dung lượng có bài toán · kế hoạch triển khai · SLA và chế tài · điều kiện thương mại · bản kê thành phần mã nguồn mở

### 1.7 Kiểm tài liệu trước khi gửi ra

```bash
grep -icoE "TênĐốiTác|TênKháchHàng|TênHãng|TênDựÁn|SốLượngNhạyCảm" tailieu.html
```

Tài liệu gửi cho nhiều nhà cung cấp phải **trung tính** — không lộ bối cảnh thương mại, không lộ tên các bên khác. Mục tiêu 0 lần xuất hiện.

---

## GIAI ĐOẠN 2 — SÁU TẦNG KIỂM CHỨNG

| Tầng | Nội dung | Tin cậy | Áp dụng cho |
|---|---|---|---|
| 1 | Hồ sơ khai báo (RFI) | Thấp nhất | Mọi ứng viên |
| 2 | Kiểm chứng tham chiếu | Trung bình | Mọi ứng viên |
| 3 | Phỏng vấn kỹ thuật sâu | Trung bình cao | Mọi ứng viên |
| 4 | Demo sản phẩm đang chạy | Cao | 3 ứng viên dẫn đầu |
| 5 | **PoC trên thiết bị hoặc môi trường thật** | Cao nhất | 2 ứng viên cuối |
| 6 | Kiểm thử tải và bảo mật | Cao nhất | 2 ứng viên cuối |

Chi tiết thiết kế RFI, 6 câu hỏi kiểm chứng tham chiếu, phỏng vấn sâu, thiết kế bài kiểm PoC và chuẩn bị nội bộ: xem `references/huong-dan-kiem-chung-ncc.md`.

---

## GIAI ĐOẠN 3 — CHẤM ĐIỂM VÀ QUYẾT ĐỊNH

### 3.1 Công bố trọng số trước khi nhận hồ sơ

Mẫu trọng số cho dự án kỹ thuật:

| Trọng số | Nhóm |
|---|---|
| 30% | Kết quả PoC |
| 20% | Năng lực kỹ thuật qua phỏng vấn |
| 15% | Kinh nghiệm lĩnh vực **đã kiểm chứng** |
| 15% | Điều kiện thương mại |
| 10% | Tiến độ |
| 10% | Cam kết vận hành |

**Ngưỡng loại:** không đạt một bài chặn của PoC · hoặc tổng dưới 60%. Chênh dưới 5 điểm giữa hai ứng viên dẫn đầu thì quyết bằng tiêu chí phụ đã công bố, không quyết cảm tính.

### 3.2 Đối chiếu thành phần để phát hiện trùng phạm vi

Khi có nhiều đề xuất cho cùng bài toán, hoặc khi đã có hợp đồng ký với bên khác cho hạng mục liên quan: lập bảng **thành phần × nhà cung cấp**, đối chiếu từng khối chức năng.

**So bằng chức năng, không so bằng tên gọi** — mỗi bên dùng thuật ngữ khác nhau cho cùng một thứ.

Trùng phạm vi nghĩa là trả tiền hai lần. Tính lại tổng chi phí đầu vào so với doanh thu đầu ra trước khi quyết.

### 3.3 Phát hiện suy thoái giữa các bản dự thảo

Khi một bên gửi bản mới và mô tả là đã nhượng bộ, **luôn lập bảng đối chiếu ba cột**: nội dung / bản cũ / bản mới, cộng cột **chiều** với ký hiệu tăng, giảm, giữ nguyên.

Bảng đó tự nó là lập luận đàm phán mạnh nhất. Không cần tranh luận thái độ.

Kiểm riêng: cam kết nào bị **xoá hoàn toàn** — đây là dạng suy thoái nặng nhất và dễ bị bỏ sót vì không có gì để so.

### 3.4 Đọc ngôn ngữ đàm phán để suy ra vị thế

Cụm từ kiểu *"trong trường hợp bên anh vẫn cần"*, *"chắc chắn không sửa được"*, *"cân nhắc cho kịp"*, *"chắc không tiếp tục được đâu"* là ngôn ngữ của bên tin rằng mình không thể bị thay thế.

> **Lợi thế của họ nằm ở giả định đó, không nằm ở điều khoản.** Xử lý đúng là làm cho giả định sai — xây phương án thay thế bằng văn bản — chứ không phải thương lượng tiếp từng điều.

---

## TÌNH HUỐNG ĐẶC BIỆT

Hướng dẫn xử lý 3 tình huống đặc biệt (ứng viên vừa là đối thủ vừa là đối tác; đối tác đe doạ rút; khách hàng nghi vấn bên thứ ba): xem `references/tinh-huong-dac-biet.md`.

---

## SAI LẦM CẦN TRÁNH

| Sai lầm | Cách đúng |
|---|---|
| **Trả về phản hồi rỗng khi người dùng đang chờ** | Mọi lượt kết thúc bằng lệnh gọi công cụ hoặc câu trả lời có nội dung |
| So giá khi chưa có đề bài chung | Lệch trên 3 lần là dấu hiệu đề bài chưa chuẩn — dựng đặc tả trước |
| Chấm điểm đối thủ bằng khung nhà cung cấp thuần | Phân loại ứng viên trước khi chấm |
| Phân tích trước khi hỏi định hướng dài hạn | Hỏi ngăn chặn hay hợp tác ngay từ đầu |
| Coi RFI là công cụ thẩm định giải pháp | RFI là tầng 1 trong sáu tầng |
| Gửi RFI cho bên đã ở giai đoạn đàm phán hợp đồng | Dùng yêu cầu giải trình kỹ thuật có mục tiêu |
| Làm biểu mẫu chỉ ở dạng PDF | Xuất song song bản Word ngay từ đầu |
| Ô trả lời có chiều cao cố định lớn | Để ô co theo nội dung, kẻ dòng nhạt |
| Gán nhãn nội dung cho tệp chưa đọc | Chỉ ghi tên và dung lượng khi liệt kê |
| So đề xuất bằng tên gọi thành phần | So bằng chức năng — mỗi bên dùng thuật ngữ khác |
| Bỏ qua cam kết bị **xoá** giữa hai bản dự thảo | Kiểm riêng mục nào biến mất, không chỉ mục nào đổi |
| Nhận ưu đãi miễn phí không thời hạn | Yêu cầu thời hạn và điều kiện chuyển đổi bằng văn bản |
| Tiếp cận đối tác lớn trước khi bảo đảm vị thế thượng nguồn | Thượng nguồn trước, đối tác sau |
| Chỉ tìm rủi ro trong điều khoản | Tìm cả quyền đã được cấp mà chưa dùng |
| Trộn lập luận nội bộ vào tài liệu gửi ra | Tách hai văn bản, kiểm bằng grep trước khi gửi |
| Cảnh báo mất dữ liệu khi thư mục hiện rỗng | Kiểm các mount khác trước khi cảnh báo |
| Đánh giá cảm tính sau khi xem demo | Tiêu chí ký trước, chấm theo tiêu chí |

---

## HỎI LÀM RÕ

Bốn câu có giá trị nhất, hỏi sớm:

1. **Với đơn vị này, mục tiêu dài hạn là ngăn chặn hay hợp tác?**
2. **Hạng mục đang xét là tài sản chiến lược hay hạng mục chi phí cần tối thiểu hoá?**
3. **Có điều kiện tiên quyết nào phụ thuộc bên thứ ba không?**
4. **Mốc ràng buộc với khách hàng cuối là gì, và đã bắt đầu tính chưa?**

Câu 4 hay bị bỏ qua nhất và thường quyết định phương án khả thi.

