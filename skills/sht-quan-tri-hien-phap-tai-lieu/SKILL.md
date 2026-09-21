---
name: sht-quan-tri-hien-phap-tai-lieu
version: 1.0
description: Giữ tài liệu vận hành (CLAUDE.md, README, bảng hiệu lực) khớp đúng thực tế máy/hệ thống hiện tại khi phát hiện lệch — sửa bằng cách thêm ghi chú cập nhật kèm ngày cạnh chỗ sai, không viết đè log lịch sử; lan truyền một sự thật đã đổi sang MỌI nơi đang trích dẫn nó. LUÔN dùng khi phát hiện tài liệu vận hành nói khác thực tế đã kiểm chứng (đường dẫn, tên thư mục, số phiên bản, trạng thái ✅/⚠️), khi một cái tên/con số xuất hiện ở nhiều file cần sửa đồng loạt, hoặc trước khi bàn giao tài liệu cần đối chiếu tính nhất quán. KHÔNG dùng để soạn tài liệu nghiệp vụ mới từ đầu, không thay thế sht-nen-tang-kiem-chung (quy tắc chung cho MỌI deliverable) — skill này chuyên riêng cho tài liệu VẬN HÀNH/HIẾN PHÁP của hệ thống, không phải sản phẩm giao khách hàng.
---

# Quản Trị Tài Liệu / Hiến Pháp

Vai trò: người giữ cho tài liệu vận hành (CLAUDE.md và tương đương) luôn khớp với thực tế máy đang chạy, không để nó trở thành nguồn gây kết luận sai cho phiên sau. Rút từ phiên sửa `CLAUDE.md` khi phát hiện gốc dự án thật là `G:\` chứ không phải `D:\`, và `Tu-Hoc-Tu-Hanh-AI` đã đổi tên thành `THỰC HÀNH-AI` (21/09/2026).

## Nguyên tắc lõi

> Tài liệu vận hành là nơi phiên sau tin theo đầu tiên. Nếu nó sai mà không ai sửa, mọi phiên sau đều kế thừa đúng cái sai đó — và càng "có vẻ chính thức" thì càng ít ai nghi ngờ.

**Không viết đè log lịch sử.** Một dòng "ngày 05/09 đã chốt X" là bản ghi lịch sử thật tại thời điểm đó — nếu X không còn đúng, đừng xoá hay sửa lại dòng đó thành như chưa từng sai. Thêm ghi chú ngay cạnh: *"(cập nhật ngày Y — X không còn đúng, thực tế là Z)"*. Giữ được cả dấu vết cũ lẫn sự thật mới.

## Quy trình chuẩn khi phát hiện tài liệu lệch thực tế

1. **Xác nhận lệch bằng bằng chứng thật** trước khi sửa — không sửa theo cảm giác "chắc là vậy". (Dùng kèm `sht-qa-kiem-chung-skill-hook`.)
2. **Grep toàn diện** tìm MỌI chỗ đang trích dẫn cùng một fact sai — tài liệu vận hành thường lặp lại 1 con số/tên ở nhiều mục (mục lục, bảng hiệu lực, log lịch sử, phần "cách tra cứu"...). Sửa 1 chỗ mà bỏ sót chỗ khác sẽ gây tài liệu tự mâu thuẫn nội bộ.
3. Với mỗi chỗ tìm được — phân loại trước khi sửa:
   - **Khai báo hiện trạng** (vd "Gốc dự án là D:\...") → sửa thẳng, thêm ghi chú ngày cập nhật.
   - **Log lịch sử** (vd "05/09/2026 — đã làm X") → **giữ nguyên câu gốc**, chỉ thêm ghi chú cập nhật ngay trong ngoặc, không xoá/viết lại.
4. Sửa xong — **đọc lại toàn bộ đoạn vừa sửa** trước khi báo xong (lỗi gõ ký tự đặc biệt khi sửa file tiếng Việt dễ lọt qua nếu không đọc lại).
5. Grep lại lần cuối xác nhận 0 chỗ còn sót giá trị cũ (trừ những chỗ cố ý giữ làm log lịch sử + đã có ghi chú "tên cũ"/"cập nhật").

## Cạm bẫy đã gặp thật — cẩn thận khi sửa file có dấu tiếng Việt

Khi gõ lại các từ có dấu tổ hợp (như "ĐỔI"), dễ phát sinh lỗi encode một cách âm thầm — công cụ báo "sửa thành công" nhưng nội dung/đường dẫn thực tế bị hỏng. **Luôn đọc lại file ngay sau khi sửa xong bất kỳ đoạn nào chứa từ có dấu phức tạp** — đừng tin thông báo "thành công" là đủ. Nếu sửa đường dẫn/tên file (không chỉ nội dung văn bản), rủi ro cao hơn: lỗi gõ ở đó có thể khiến công cụ tạo nhầm một file/thư mục hoàn toàn mới ở vị trí sai thay vì báo lỗi — phải kiểm tồn tại ở cả đường dẫn đúng lẫn nghi ngờ có bản lạc ở đâu đó.

## Ví dụ áp dụng từ phiên thật

`CLAUDE.md` mục 6 gốc: *"Gốc dự án là D:\CHUYỂN ĐỔI SỐ SHT (chốt 05/09/2026)."* — sau khi xác nhận máy hiện tại không có ổ D:\, sửa thành: *"Gốc dự án là G:\CHUYỂN ĐỔI SỐ SHT (chốt 05/09/2026, cập nhật 21/09/2026 — máy hiện tại không có ổ D:\, cây thật nằm ở ổ G:\)."* — giữ mốc thời gian gốc, thêm sự thật mới, không xoá gì.

## Dùng kèm

Sau khi sửa xong tài liệu vận hành, kiểm xem có memory liên phiên nào đang mô tả đúng vấn đề vừa sửa — cập nhật luôn bằng `sht-quan-tri-tri-nho-lien-phien` (cùng nguyên tắc không viết đè lịch sử, khác đối tượng: đây là tài liệu vận hành, kia là trí nhớ riêng của agent).
