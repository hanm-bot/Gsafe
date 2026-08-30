---
name: "sht-qd-nhansu-alignment"
description: "Soạn thảo và rà soát Quyết định (QĐ) nhân sự/tổ chức tại Công ty CP Đầu tư Công nghệ SHT — bổ nhiệm, phân giao nhiệm vụ, điều chỉnh mô hình tổ chức — sao cho nhất quán thẩm quyền và quan hệ báo cáo với các QĐ liên quan đang có hiệu lực. LUÔN dùng khi soạn QĐ cho vị trí có cấp trên hoặc cấp dưới trực tiếp đã có QĐ riêng; khi người dùng nhắc xung đột quyền hạn, mô hình tổ chức, \"Under CCO\"/\"Under GĐ\", đối chiếu QĐ, điều chỉnh quyết định, bổ nhiệm lại; hoặc khi một QĐ mới có thể ảnh hưởng nội dung một QĐ cũ đang hiệu lực — kể cả khi họ chỉ mô tả tình huống, ví dụ hỏi vừa bổ nhiệm CCO thì có ảnh hưởng gì đến các Giám đốc Trung tâm Kinh doanh không. Dùng KÈM chuan-hoa-du-lieu-nhansu (chốt danh tính trước khi viết), sht-xacthuc-baocao-hoatdong (nếu Căn cứ dẫn số liệu thành tích), sht-nen-tang-kiem-chung (quy tắc bàn giao). KHÔNG dùng để xác minh tên riêng hay kiểm tính đúng đắn của số liệu — việc của hai skill kia."
---

# Chuẩn hóa & Rà soát Quyết định Nhân sự/Tổ chức — SHT

Skill này đóng gói lại quy trình đã kiểm chứng qua thực tế: soạn QĐ Bổ nhiệm CCO Phạm Việt Phương và xử lý xung đột quyền hạn với QĐ bổ nhiệm GĐ TTKD 2 (Lê Quang Tuấn).

## Nguyên tắc cốt lõi (không được vi phạm)

> **Một Quyết định không được đơn phương "diễn giải lại" hoặc ngầm định thay đổi nội dung của một Quyết định khác đang có hiệu lực, nếu Quyết định đó không được dẫn chiếu và cập nhật trực tiếp.**

Mọi bước dưới đây tồn tại để phục vụ nguyên tắc này.

## Khi nào dùng skill này

- Soạn QĐ bổ nhiệm/phân giao nhiệm vụ cho một chức danh **mới xen giữa** cấp trên và cấp dưới đã tồn tại (ví dụ: thêm CCO ở giữa BLĐ và các Giám đốc Trung tâm Kinh doanh).
- Thay đổi mô hình tổ chức (VD "X Under Y") và cần kiểm tra các QĐ hiện hành có còn đúng với mô hình mới không.
- Người dùng yêu cầu "đối chiếu", "rà soát xung đột quyền hạn", "có cần điều chỉnh QĐ khác không".

## Chuẩn bị — hai việc phải làm trước khi viết chữ nào

1. **Chốt danh tính mọi người được nhắc trong QĐ** bằng `chuan-hoa-du-lieu-nhansu`. Tên trong QĐ là tên có giá trị pháp lý nội bộ; sai một chữ là phải ban hành lại.
2. **Nếu QĐ có phần Căn cứ dẫn số liệu thành tích** (doanh số, KPI, hoạt động Engage khách hàng), chạy `sht-xacthuc-baocao-hoatdong` trước. Con số ở nhãn ❓ (chưa kiểm được) **không được đưa vào phần Căn cứ** — hoặc chuyển sang diễn đạt định tính, hoặc lùi ngày ban hành để kiểm xong.

## Quy trình 6 bước

### Bước 1 — Thu thập toàn bộ văn bản liên quan

Không chỉ đọc QĐ đang soạn. Tìm và đọc:

- QĐ hiện hành của cấp trên trực tiếp (nếu có).
- QĐ hiện hành của (các) cấp dưới trực tiếp bị ảnh hưởng.
- Ít nhất 1-2 văn bản tiền lệ **thật** của công ty cho cùng loại QĐ, dùng làm chuẩn định dạng — không tự bịa cấu trúc (căn cứ, số Điều, nơi nhận, khối ký...). Xem `references/qd-format-mau.md`.

### Bước 2 — Lập bảng đối chiếu song song

Với mỗi cặp văn bản (QĐ mới vs QĐ liên quan hiện hành), dựng bảng gồm các cột: **# | Nội dung | QĐ A | QĐ B | Mức xung đột (🔴 Cao / 🟡 Trung bình / — Không) | Vấn đề cụ thể**.

Các khía cạnh bắt buộc phải kiểm tra:

1. Danh xưng/tư cách đại diện ("đại diện BLĐ", "trực tiếp điều hành"...)
2. Thẩm quyền phê duyệt kế hoạch/ngân sách theo chu kỳ
3. Thẩm quyền nhân sự (tuyển dụng, khen thưởng, kỷ luật) — đặc biệt phân biệt rõ **cấp nào** (chính người giữ chức danh cấp dưới, hay nhân sự thuộc quyền của người đó)
4. Xây dựng chiến lược/kế hoạch — ai làm khung, ai làm chi tiết
5. Hệ thống đo lường hiệu quả — số liệu gốc từ đâu
6. Trách nhiệm cá nhân trước cấp nào (giữ nguyên trách nhiệm trước BLĐ hay chuyển hẳn sang cấp trung gian?)
7. Thời gian thử việc/thử thách — so với tiền lệ tương đương, có bất thường không

Không tự chấm điểm alignment là "đã ổn" nếu chưa liệt kê đủ 7 khía cạnh này.

### Bước 3 — Với mỗi điểm 🔴/🟡, đề xuất và xin xác nhận mức quyền hạn cụ thể

Không tự ý chọn mức quyền hạn (VD "phê duyệt" hay "cho ý kiến", "đề xuất trực tiếp" hay "chỉ phê duyệt"). Trình bày rõ 2 lựa chọn kèm hệ quả, hỏi người quyết định chọn — dùng bảng lựa chọn ngắn, không hỏi dồn quá 2-3 câu một lúc.

### Bước 4 — Chọn cơ chế xử lý: Điều chỉnh hay Thay thế toàn bộ

Khi QĐ mới đòi hỏi sửa nội dung của QĐ cũ đang hiệu lực, có 2 phương án:

| Phương án | Khi nên dùng | Rủi ro |
|---|---|---|
| **Văn bản điều chỉnh** (ngắn, dẫn chiếu QĐ gốc, chỉ sửa đúng phần xung đột) | Số lượng thay đổi ít, muốn giữ nguyên vẹn lịch sử văn bản gốc | Người thực thi phải đọc **2 văn bản** mới hiểu đầy đủ — dễ bị coi là khó hiểu |
| **Thay thế toàn bộ** (viết lại đầy đủ, tự đủ nghĩa, nêu rõ "thay thế toàn bộ QĐ số...") | Muốn người thực thi chỉ cần đọc 1 văn bản; số thay đổi tương đối nhiều | Phải cẩn thận chép đủ toàn bộ nội dung gốc còn giá trị, không được bỏ sót |

**Luôn hỏi người quyết định chọn phương án nào** trước khi soạn — đây là quyết định về trải nghiệm đọc văn bản, không phải kỹ thuật soạn thảo.

Nếu chọn **Thay thế toàn bộ**, bắt buộc:

- Nêu rõ trong Điều cuối: "Quyết định này có hiệu lực kể từ ngày ký và **thay thế toàn bộ** Quyết định số ... ngày ...".
- **Giữ nguyên các mốc thời gian đã phát sinh hiệu lực từ QĐ gốc** (đặc biệt thời gian thử việc/thử thách) — ghi rõ câu dạng: "...được tính liên tục kể từ ngày [ngày QĐ gốc có hiệu lực] theo Quyết định số ..., không tính lại từ ngày ký Quyết định này." Đây là lỗi hay gặp nhất khi viết lại từ đầu.

### Bước 5 — Rà lại văn bản "cấp trên" sau khi chọn cơ chế xử lý (bước dễ bị bỏ sót nhất)

Nếu văn bản của cấp trên (VD QĐ CCO) đã được soạn **trước khi** chốt cơ chế điều chỉnh/thay thế cho văn bản cấp dưới, phải quay lại rà từng Điều của văn bản cấp trên xem có đoạn nào:

- Giả định cơ chế xử lý cũ (VD nhắc "sẽ có văn bản điều chỉnh riêng" trong khi thực tế chọn thay thế toàn bộ).
- Dùng thuật ngữ không nhất quán với văn bản cấp dưới (VD "cấp Khối" ở một Điều, "cấp AM/ASM" ở Điều khác cho cùng một khái niệm).

Đây chính là lỗi đã xảy ra trong phiên gốc: Điều 1.6 của QĐ CCO Phương vẫn viết theo giả định "văn bản điều chỉnh riêng" sau khi đã đổi sang "thay thế toàn bộ" cho QĐ của GĐ TTKD.

### Bước 6 — Kiểm tra hoàn chỉnh mô hình tổ chức

Nếu mô hình tổ chức áp dụng cho nhiều đơn vị cùng cấp (VD "TTKD 1 & 2 Under CCO"), kiểm tra đã có văn bản tương ứng cho **tất cả** các đơn vị chưa, không chỉ đơn vị có sẵn dữ liệu. Nếu thiếu, nêu rõ đây là điểm còn treo, không tự nhận là mô hình đã hoàn chỉnh.

## Kỹ thuật dựng file .docx

- Đọc SKILL.md của skill `docx` trước khi tạo file.
- Dùng khối mã boilerplate tại `references/qd-format-mau.md` (bảng 2 cột không viền cho phần quốc hiệu/tiêu ngữ, bảng 2 cột không viền cho phần "Nơi nhận"/chữ ký) — đây là định dạng đã đối chiếu đúng với 3 văn bản thật của công ty (QĐ KPI, QĐ bổ nhiệm GĐ TTKD Tuấn, Tùng).
- Sau khi dựng file, luôn render sang ảnh để kiểm tra bố cục trước khi gửi:

  ```
  soffice --headless --convert-to pdf <file>.docx
  pdftoppm -jpeg -r 110 <file>.pdf page
  ```

  rồi xem từng trang ảnh.

## Checklist riêng của Quyết định

Chạy **sau** checklist nền ở `sht-nen-tang-kiem-chung` §5, không thay thế nó.

- [ ] Danh tính mọi người được nhắc đã chốt với QĐ/hợp đồng gốc (`chuan-hoa-du-lieu-nhansu`)
- [ ] Số liệu ở phần Căn cứ đã mang nhãn ✅ hoặc ⚠️, không còn ❓ (`sht-xacthuc-baocao-hoatdong`)
- [ ] Đã đối chiếu với ≥1 văn bản tiền lệ thật cho định dạng
- [ ] Đã lập bảng đối chiếu đủ 7 khía cạnh với mọi QĐ liên quan
- [ ] Mọi điểm 🔴/🟡 đã được người quyết định xác nhận mức quyền hạn cụ thể
- [ ] Đã chọn rõ cơ chế: điều chỉnh hay thay thế toàn bộ — có xác nhận của người quyết định
- [ ] Nếu thay thế toàn bộ: đã giữ nguyên mốc thời gian thử việc/hiệu lực gốc
- [ ] Đã rà lại văn bản cấp trên xem có đoạn nào giả định cơ chế xử lý cũ không
- [ ] Thuật ngữ nhất quán xuyên suốt từng văn bản
- [ ] Đã nêu rõ những đơn vị/vị trí còn thiếu văn bản tương ứng (nếu mô hình áp dụng nhiều đơn vị)
- [ ] Đã render file sang ảnh và kiểm tra bố cục trước khi gửi

