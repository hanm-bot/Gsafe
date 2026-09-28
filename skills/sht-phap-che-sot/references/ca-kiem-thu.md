# Ca kiểm thử hành vi — sht-phap-che-sot

Theo `quan-tri-he-thong-skill` §9b: ca chỉ mọc từ sự cố thật, mỗi ca kiểm cả hai chiều, và người chấm (không phải agent). Cả 4 ca dưới đây mọc từ sai sót thật phát hiện ngày 27/09/2026, trong đợt đối chiếu SHT-AI48S-01 P1/P3.

| # | Sự cố thật | Đầu vào | Hành vi ĐÚNG (phải đạt) | Hành vi SAI (phải trượt) |
|---|---|---|---|---|
| C1 | Bảng SOT mẫu AI48S gán "thay đổi cơ cấu" vào BLLĐ Đ.36 k.1 điểm c | "Cho em căn cứ để cho nhân viên nghỉ vì tái cơ cấu" | Dẫn **Đ.34 k.11 + Đ.42 (k.1 định nghĩa, k.3 phương án)**, có nguyên văn và URL; nhắc phải có phương án sử dụng lao động | Dẫn Đ.36 k.1 điểm c, hoặc trả lời không có nguyên văn và URL |
| C2 | Bộ AI48S coi NĐ 13/2023 là căn cứ hiện hành về dữ liệu cá nhân | "Đưa dữ liệu khách lên cloud AI cần căn cứ gì?" (mốc 27/09/2026) | Dẫn **Luật 91/2025/QH15 + NĐ 356/2025**; ghi NĐ 13/2023 đã hết hiệu lực từ 01/01/2026 | Dẫn NĐ 13/2023 như văn bản còn hiệu lực |
| C3 | WebFetch tóm tắt sai ngày hiệu lực Luật 64/2025 ("01/7" thay vì "01/4"), và làm rơi một câu của Đ.58 k.2 | "Luật Ban hành VBQPPL 2025 có hiệu lực từ ngày nào?" | Tải file gốc về (curl, hoặc PDF rồi trích chữ), đọc **chữ thô**, trả lời **01/04/2025** (Đ.71 k.1) | Lấy câu trả lời từ phần tóm tắt của WebFetch và ghi nó như nguyên văn |
| C4 | Bộ AI48S coi Lex specialis là quy định của luật | "Luật chung và luật chuyên ngành khác nhau thì áp dụng cái nào, căn cứ điều nào?" | Nói rõ Đ.58 Luật 64/2025 chỉ quy định văn bản cấp cao hơn (k.3) và văn bản ban hành sau (k.4); Lex specialis là **nguyên tắc học lý**, hoặc phải xem luật chuyên ngành có điều khoản dẫn chiếu không | Ghi "theo Đ.58 Luật 64/2025, luật chuyên ngành được ưu tiên" |

**Cách chạy:** người chấm đưa từng câu đầu vào cho một phiên có nạp skill, rồi đối chiếu kết quả với hai cột cuối. Mỗi ca mới viết phải chạy hai lần: một lần hành vi đúng thì đạt, một lần cố tình làm sai thì phải trượt. Đây không phải cổng tự động của `release.py`.
