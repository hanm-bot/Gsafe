---
name: sht-qa-kiem-chung-skill-hook
version: 1.0
description: Kiểm chứng bằng hành vi thật xem một skill/hook/chốt cưỡng chế có đang thực sự chạy hay chỉ mới được khai báo trong tài liệu — tái hiện lỗi bằng đối chứng, so checksum có chuẩn hoá, chạy lại bộ test sẵn có, gọi thẳng công cụ thật để lấy bằng chứng quyết định thay vì đọc code suy luận. LUÔN dùng trước khi kết luận "skill X đang chạy", "hook Y đã chặn thật", "phiên bản Z đã cài đúng" — bất kỳ câu kết luận nào về trạng thái RUNNING của một thành phần harness. KHÔNG dùng để tự thiết kế skill mới từ đầu (dùng skill-creator), không dùng để audit quan hệ giữa các skill (dùng sht-skills:quan-tri-he-thong-skill) — skill này chỉ lo một câu hỏi duy nhất: "cái này có THẬT SỰ chạy không, hay chỉ là tài liệu nói vậy?"
---

# QA / Kiểm Chứng Viên Skill & Hook

Vai trò: người không tin bất kỳ khẳng định "đang chạy" nào cho tới khi tự tay ép nó chạy thật và xem kết quả. Rút từ phiên làm việc kiểm chứng gói skill BrandOS-Cho-Chu-Doanh-Nghiep và hạ tầng 5 luật cứng SHT (20-21/09/2026).

## Nguyên tắc lõi

> **Luật nền:** không kết luận một chốt/skill/tác vụ/phiên bản **đang chạy** khi mới chỉ thấy nó **được khai báo**. Chưa thử thật thì ghi ⚠️, không ghi ✅.

Điều này áp dụng cho MỌI khẳng định về trạng thái vận hành: "hook đã chặn", "skill đã cài", "path đã đúng", "test đã pass" — dù tài liệu, code comment, hay chính agent trước đó nói gì.

## 6 kỹ thuật đã kiểm chứng dùng được thật

### 1. Tái hiện lỗi bằng đối chứng (A/B testing thật)
Không suy luận "thiếu file X thì sẽ lỗi Y" — dựng 2 bản: một có điều kiện, một không, chạy song song, so kết quả thật.
> *Case:* nghi ngờ thiếu `context/` làm vỡ skill `brand-design`. Dựng 2 project scaffold (có/không `context/`), giao cho 2 agent độc lập chạy cùng yêu cầu → 1 bên `FileNotFoundError` thật, 1 bên chạy trót lọt. Kết luận có bằng chứng, không phải suy đoán.

### 2. So checksum phải chuẩn hoá trước khi kết luận "lệch"
Byte-so-byte thô dễ dương tính giả (CRLF/LF, BOM, encoding). Luôn tính lại sau khi chuẩn hoá, và **kiểm chứng giả thuyết bằng số** (vd: `delta byte == số ký tự CR`) trước khi kết luận.
> *Case:* checksum 13 skill "lệch" ban đầu — hoá ra script ghi text-mode Windows (`\n`→`\r\n`), không phải lệch nội dung thật. Chuẩn hoá xong: khớp 100%.

### 3. Chạy lại bộ test sẵn có, đừng tự bịa test mới nếu đã có
Nhiều hook/script trong hệ SHT có sẵn `test-*.cjs` đi kèm — chạy trực tiếp lấy kết quả thật (đạt/trượt bao nhiêu ca), đừng chỉ đọc code rồi đoán nó đúng.
> *Case:* sau khi vá path 6 hook cấp user, chạy lại đủ 6 bộ `test-chan-*.cjs` → phát hiện 1 bộ thật sự fail (assertion lỗi) dù 5 bộ kia sạch — nếu chỉ đọc code sẽ không thấy.

### 4. Gọi thẳng công cụ thật — bằng chứng quyết định, không gì thuyết phục hơn
Với skill: gọi `Skill(skill="...")` trực tiếp. Với quyền: thử chính lệnh bị nghi ngờ (`rm`) và xem có bị từ chối không. Đừng dừng ở "tôi thấy file tồn tại" hay "cấu hình có ghi".
> *Case:* file `.skill` tồn tại, nội dung hợp lệ — vẫn gọi `Skill()` ra `Unknown skill`. Chỉ sau khi cài đúng chỗ + đổi đúng gốc dự án, gọi lại mới thành công. Không có bước gọi thật này sẽ báo sai "đã cài xong".

### 5. Đối chứng phủ định cũng là bằng chứng
"Không tìm thấy X ở đâu" chỉ có giá trị khi đã tìm **toàn diện** (nhiều ổ đĩa, nhiều thư mục, không chỉ 1 chỗ đoán mò) — nếu không, đó là "chưa tìm thấy", không phải "không tồn tại".
> *Case:* kết luận `usecase-diagram` không tồn tại trên máy chỉ sau khi rà cả `~/.gemini/config/skills/` (19 skill liệt kê) lẫn toàn bộ `G:\CHUYỂN ĐỔI SỐ SHT` — không phải chỉ nhìn 1 thư mục rồi kết luận.

### 6. `Skill()` gọi bằng tên trơn có thể trả CACHE cũ trong cùng phiên — ưu tiên namespace đầy đủ khi cần chắc chắn
Khi một skill từng tồn tại **2 bản trùng tên** (vd: bản project-local `.claude/skills/` và bản trong plugin), rồi một bản bị xoá/di chuyển **giữa chừng phiên đang chạy** — gọi lại bằng tên trơn (`Skill(skill="ten-skill")`) vẫn có thể trả về nội dung cũ, "Base directory" trỏ vào đường dẫn **đã không còn tồn tại trên đĩa**. Đây không phải lỗi cấu trúc, mà là cache trong-phiên của chính harness, tự hết khi mở phiên mới.
**Cách kiểm chắc chắn:** gọi bằng namespace đầy đủ (`Skill(skill="sht-skills:ten-skill")`) — route đúng vào nguồn thật, không bị cache tên trơn đánh lừa.
> *Case:* vừa `mv` bản project-local của `brainstorm` đi, `ls` xác nhận `No such file or directory` — nhưng `Skill(skill="brainstorm")` vẫn trả về Base directory trỏ đúng đường dẫn vừa xoá đó. Gọi lại bằng `Skill(skill="sht-skills:brainstorm")` mới route đúng vào plugin, nội dung khớp bản mới nhất.

## Quy trình chuẩn khi được giao "kiểm chứng X"

1. Đọc tài liệu/code khai báo X — ghi lại đúng những gì nó TỰ NHẬN.
2. Tìm cách tái hiện tình huống thật (đối chứng nếu cần) — không suy luận suông.
3. Nếu có sẵn bộ test — chạy nó trước, đừng bỏ qua vì "chắc đã pass rồi".
4. Gọi trực tiếp công cụ/API thật liên quan để lấy tín hiệu quyết định.
5. Kết luận **kèm bằng chứng cụ thể** (exit code, số ca đạt/trượt, thông báo lỗi nguyên văn) — không kết luận suông "đã chạy được".
6. Nếu phát hiện gãy — sửa xong phải **lặp lại đúng bước 3-4** để xác nhận đã sửa thật, không dừng ở "tôi nghĩ đã sửa đúng rồi".

## Dùng kèm

Nếu lỗi phát hiện được là do đường dẫn hardcode (path máy tác giả, ổ đĩa cũ, tên thư mục đã đổi) — chuyển sang `sht-ha-tang-va-path-portable` để vá đúng kỹ thuật, rồi quay lại đây lặp bước 3-4 xác nhận đã sửa thật.
