# GĐ 4 — Thiết kế & phân tích phỏng vấn

## Phần A — Thiết kế bộ phỏng vấn

Bộ phỏng vấn đầy đủ cho vị trí quản lý gồm: phỏng vấn kinh nghiệm/thành tích · phỏng vấn năng lực lãnh đạo · phỏng vấn tình huống · bài tập phân tích dữ liệu · thuyết trình kế hoạch 90-100 ngày · kiểm tra tham chiếu · xác minh kết quả kinh doanh quan trọng.

Vị trí chuyên môn có thể rút gọn nhưng **phải giữ tối thiểu 2 loại**: kỹ thuật + hành vi.

### Câu hỏi phải làm rõ được 9 điểm
Bối cảnh · mục tiêu · vai trò thực tế · hành động cá nhân · quy mô nguồn lực · kết quả định lượng · khó khăn · bài học · khả năng áp dụng tại SHT.

### Thiết kế bài tập tình huống
Ưu tiên dùng **dữ liệu/hồ sơ thật của SHT (đã ẩn danh)** thay vì case giả định — bài test khi đó đo đúng năng lực áp dụng chứ không phải khả năng nói lý thuyết. Bài tập nên nhắm trực tiếp vào **khoảng trống đã phát hiện ở GĐ 3**.

---

## Phần B — Chuyển ghi âm thành transcript

Cấp nguyên văn prompt sau cho người dùng, kèm hướng dẫn upload file lên Google AI Studio (Gemini) hoặc công cụ tương đương. Thay `[...]` bằng thông tin thực tế.

```
Bạn là trợ lý transcribe chuyên nghiệp. Hãy nghe file ghi âm đính kèm và thực hiện:

1. TRANSCRIBE toàn bộ nội dung cuộc phỏng vấn bằng tiếng Việt, giữ nguyên văn phong nói
   (không chỉnh sửa câu chữ của người nói).

2. GẮN NHÃN NGƯỜI NÓI theo vai trò suy đoán từ ngữ cảnh hội thoại, ví dụ:
   - [PVV1 - [Tên], [Chức danh]]
   - [PVV2 - [Tên], [Chức danh]]
   - [Ứng viên - [Tên]]
   Nếu không chắc chắn ai đang nói, ghi rõ [Không xác định] thay vì đoán bừa.

3. GẮN TIMESTAMP mỗi 1-2 phút hoặc mỗi khi chuyển người nói, định dạng [mm:ss].

4. Nếu đoạn nào nghe không rõ, ghi chú [không nghe rõ], không tự suy diễn nội dung.

5. Xuất kết quả dạng bảng hoặc kịch bản, theo trình tự thời gian, không tóm tắt, không lược bỏ.

6. Ở cuối, liệt kê riêng các mốc thời gian có câu hỏi liên quan đến:
   [chủ đề 1], [chủ đề 2], [chủ đề 3] — để tiện tra cứu lại.

Không tóm lược, không diễn giải, không nhận xét về ứng viên — chỉ transcribe thuần túy.
```

**Cách chọn chủ đề ở mục 6:** lấy trực tiếp từ danh sách khoảng trống đã phát hiện ở GĐ 3. Mỗi khoảng trống = một chủ đề cần tra cứu.

**Khi nhận transcript về:**
- AI có thể tự thêm tóm tắt/nhận xét dù đã yêu cầu không — bỏ qua, chỉ dùng phần hội thoại có timestamp.
- Nhãn người nói do AI suy đoán **có thể sai**. Nếu một phát ngôn không khớp vai trò được gán (ví dụ ứng viên "trả lời" câu hỏi của chính mình), đối chiếu lại ngữ cảnh trước khi trích dẫn.

---

## Phần C — Phân tích transcript

### C.1 Nhận diện loại phỏng vấn TRƯỚC khi chấm

| Loại | Chấm tốt được | Không chấm được |
|---|---|---|
| Q&A kỹ thuật | Skill, Knowledge | Attitude (thiếu câu hỏi hành vi) |
| STAR / hành vi | Attitude, cách xử lý tình huống | Chiều sâu kỹ thuật |
| Bài tập tình huống | Năng lực áp dụng thực tế | — |

Nếu buổi PV thiên một loại, **ghi rõ nhóm điểm nào có độ tin cậy thấp hơn** (đánh dấu `*`) và đề xuất bổ sung.

### C.2 Ánh xạ bằng chứng theo mốc thời gian

Mỗi khoảng trống từ GĐ 3 → tìm bằng chứng trong transcript → gắn timestamp → kết luận một trong bốn nhãn:

`ĐÃ ĐÓNG` · `CẦN HỎI LẠI` · `VƯỢT KỲ VỌNG` · `GIỚI HẠN THẬT`

Đồng thời ghi nhận **năng lực mới phát hiện** không có trong CV — thường là giá trị lớn nhất của buổi phỏng vấn.

### C.3 Ba bẫy phân tích

**Bẫy 1 — Mâu thuẫn giả.** Trước khi kết luận ứng viên nói mâu thuẫn, kiểm tra có phải hai khái niệm khác nhau bị gọi bằng từ giống nhau.
> Ví dụ: "ít làm tổng mức đầu tư kiểu nhà nước" và "hồ sơ thanh toán nhà nước nắm chắc" — không mâu thuẫn: *lập dự toán đầu dự án* vs *thanh quyết toán cuối dự án*.

**Bẫy 2 — Lời tự nhận giới hạn.** Ghi vào **cả hai chỗ**: rủi ro năng lực (giới hạn thật) và điểm mạnh Attitude (trung thực, không nhận bừa).

**Bẫy 3 — Người phỏng vấn nội bộ cũng là dữ liệu.**

---

## Phần D — Benchmark khi không có ứng viên đối sánh

Khi không có ứng viên thứ hai, dùng **nhân sự nội bộ đang làm tốt vị trí đó** làm chuẩn:

1. Lấy các chủ đề nhân sự nội bộ đặt câu hỏi trong buổi PV.
2. Mỗi chủ đề = một năng lực vị trí này **thực sự cần tại SHT** (khác JD lý thuyết).
3. Đối chiếu câu trả lời ứng viên → `Nội bộ nhỉnh hơn` / `Ngang nhau` / `Bổ trợ nhau` / `Cần xác nhận thêm`.
4. **Diễn giải đúng khoảng cách:** chênh lệch giữa nhân sự đã hội nhập và ứng viên mới là *tự nhiên*, phản ánh độ "thấm" quy trình nội bộ, không phải năng lực gốc yếu hơn.
5. Khoảng trống lộ ra ở bước này chính là **nội dung onboarding** ở GĐ 7.

---

## Phần E — Chấm ASK trước/sau phỏng vấn

Luôn trình bày **hai cột: điểm hồ sơ → điểm sau phỏng vấn**, kèm giải thích nguyên nhân thay đổi bằng bằng chứng có timestamp. Đánh dấu `*` cho nhóm điểm độ tin cậy thấp và chú thích lý do.

Điểm sau phỏng vấn **không được cao hơn điểm hồ sơ ở nhóm mà buổi PV không kiểm tra**. Nếu không hỏi về Attitude thì không nâng điểm Attitude.
