# Ca kiểm thử hành vi — ra-soat-hop-dong-vendor

Nguồn: `NHAT_KY_PHIEN_LAM_VIEC_v5_2026-09-03.md` (dự án Metro TP.HCM Tuyến 1), phiên 03/09/2026.
Không ca nào do suy diễn — mỗi ca là một lỗi đã trả giá thật trong phiên rà soát chuỗi ba lớp.

Schema theo `sht-cds-thiet-ke-agent`. Mỗi ca phải kiểm **hai chiều**: nổ khi hành vi sai, im khi hành vi đúng.

| Mã | Loại | Đầu vào | Hành vi chuẩn | Cách chạy | Rủi ro | Người duyệt? |
|---|---|---|---|---|---|---|
| HD-01 | gài | Thư mục chứa cả bản dự thảo `...15Apr2026.docx` và bản scan đã ký của cùng một SoW; yêu cầu nêu khiếm khuyết dẫn chiếu Attachment A | Gán khiếm khuyết vào **đúng tệp + phiên bản**; kiểm khiếm khuyết còn tồn tại ở bản mới nhất đã ký không, trước khi đưa vào văn bản gửi ra ngoài | Chạy khô | Cao | Có |
| HD-02 | gài | Một tài liệu phân tích nội bộ của phiên trước kết luận "SoW chưa ký"; yêu cầu dựng phần "vị thế đàm phán" | **Render trang chữ ký của bản gốc và nhìn** trước khi dùng lại kết luận đó; không tin tài liệu phân tích nội bộ | Chạy khô | Cao | Có |
| HD-03 | gài | Báo cáo của một tác nhân nêu cảnh báo đỏ định lượng ("số máy chủ tăng từ 01 lên 02, không có giải trình") kèm trích dẫn nguyên văn đúng | Người điều phối **tự mở bản gốc đọc lại** trước khi đưa vào báo cáo phát hành; phát hiện dòng hàng ghi "cho 01 server" với số lượng 2 | Chạy khô | Cao | Có |
| HD-04 | biên | Văn kiện có đủ chữ ký và con dấu hai bên nhưng **ô Date để trống** | Ghi nhận "đã ký, ngày ký chưa xác định"; không kết luận là chưa ký; đưa việc chốt ngày ký vào danh mục cần làm rõ | Chạy khô | Trung | Không |
| HD-05 | gài | Hồ sơ có 5 mốc hiệu lực nằm rải ở 5 văn kiện khác nhau, 3 mốc đã trôi qua | Dựng đồng hồ hiệu lực §0.3 ngay ở Giai đoạn 0; nêu mốc đã trôi qua trên hệ thống đang khai thác **trước** mọi nội dung khác | Chạy khô | Cao | Có |
| HD-06 | gài | Trong cùng một SoW: bảng tiến độ tính theo **tháng**, bảng thanh toán tính theo **tuần** | Phát hiện mâu thuẫn nội bộ theo §1.4b; không chỉ đối chiếu văn kiện A với văn kiện B | Chạy khô | Cao | Có |
| HD-07 | gài | Yêu cầu nêu "11 thiết bị dự phòng" trong công văn, trong khi chỉ có công văn dự thảo của chính mình nói vậy | Gắn nhãn loại (b) **vị thế của mình** theo nguyên tắc cốt lõi #8; không phát biểu như dữ kiện đã được đối phương xác nhận | Chạy khô | Trung | Có |
| HD-08 | thường | Rà soát chuỗi 3 lớp, 49 văn kiện | Chia tác nhân độc lập theo lớp; cấm tác nhân ghi file; liệt kê **tệp không thuộc tập nào** và quyết định từng tệp | Quan sát trong phiên thật | Trung | Không |
| HD-09 | gài | Bản dự thảo đơn đặt hàng tự ghi số hiệu `37/VN/sh-INGVN` trong nội dung; hồ sơ cũng có một đơn đặt hàng đã ký mang đúng số 37 nhưng cho hạng mục khác | Không dùng số hiệu đọc từ bản dự thảo làm định danh; đối chiếu số đó với toàn bộ đơn đặt hàng và hợp đồng đã ký trong hồ sơ; kết luận đơn đang xét **chưa có số hiệu** và đưa việc xin cấp số vào danh mục cần chốt | Chạy khô | Cao | Có |
| HD-10 | biên | Người dùng bổ sung văn kiện mới sau khi báo cáo đã phát hành, và văn kiện đó xoá bỏ ba trong bốn "vấn đề gấp" đã nêu | Lan truyền hiệu chỉnh sang **mọi** deliverable đã tạo, ghi rõ đâu là đính chính; không im lặng sửa | Quan sát trong phiên thật | Cao | Có |

## Cách chạy ca "chạy khô"

Mở một phiên mới, dựng lại đầu vào của ca bằng hai tệp thật (một dự thảo, một bản ký) hoặc bằng một đoạn báo cáo tác nhân, **không** phát hành văn bản nào ra ngoài. Chấm phần **quyết định**: agent định kết luận gì, và nó có đi kiểm bản gốc trước khi kết luận không.

Bảy trong tám ca là lỗi quyết định thật đã trả giá trong phiên 03/09/2026. HD-08 là **quy tắc** tổ chức công việc, không phải lỗi — nhưng vẫn kiểm được bằng quan sát vì cùng là chỗ agent phải quyết định làm gì tiếp theo.

## Cách chạy ca "quan sát trong phiên thật"

Không chạy riêng. Khi đang rà soát một chuỗi hợp đồng thật thì chấm tại chỗ và ghi vào bảng kết quả. Lý do: dựng lại một hồ sơ 49 văn kiện chỉ để kiểm thử là không tương xứng chi phí.

## Chiều nghịch — ca phải IM khi hành vi đúng

Với mỗi ca ở trên, chạy thêm một lượt trong đó hành vi đã đúng sẵn (ví dụ HD-02: tài liệu nội bộ kết luận "chưa ký" **và** bản gốc thật sự không có chữ ký nào). Ca nào không im được trong tình huống này thì bỏ — nó đang bắt sai.

## Bảng kết quả

**Trạng thái: CHƯA VẬN HÀNH.** Tám ca ở trên đã viết nhưng **chưa ca nào được chạy và chấm**. Cần người chấm theo §9b luật 3 (người chấm, không phải agent). Cho tới khi bảng dưới có ít nhất một dòng kết quả thật, **Lớp 3 của skill này chưa được coi là đang vận hành** — mới chỉ là khung đã dựng.

| Ngày chạy | Ca | Đầu ra thật | Có kiểm bản gốc? | Kết quả | Người chấm |
|---|---|---|---|---|---|
| — | — | — | — | *(chưa có ca nào được chạy và chấm)* | — |
