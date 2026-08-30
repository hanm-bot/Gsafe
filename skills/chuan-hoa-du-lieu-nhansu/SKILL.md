---
name: "chuan-hoa-du-lieu-nhansu"
description: "Xác minh danh tính nhân sự trong hồ sơ tổ chức/nhân sự tại SHT — chốt tên riêng với nguồn chính thức (QĐ bổ nhiệm/hợp đồng) TRƯỚC khi sản xuất tài liệu, phân biệt nhiều người trùng tên trong cùng bối cảnh, và tách đúng \"vai\" khi một người kiêm nhiệm nhiều chức danh. LUÔN dùng skill này khi soạn/sửa hồ sơ nhân sự — bổ nhiệm, đánh giá cán bộ, onboarding, biên bản họp có nhắc tên người — đặc biệt khi có từ 2 người trở lên khả năng trùng tên/trùng họ trong cùng luồng công việc, hoặc khi một người giữ đồng thời nhiều chức danh. Dùng cùng lúc với sht-qd-nhansu-alignment khi việc là rà soát/soạn Quyết định, với sht-xacthuc-baocao-hoatdong khi hồ sơ có số liệu từ CRM/dashboard, và với sht-nen-tang-kiem-chung cho quy tắc lan truyền hiệu chỉnh & bàn giao. KHÔNG dùng cho ứng viên chưa tuyển (việc của chuan-hoa-du-lieu-tuyen-dung) hay cho thẩm quyền/mô hình tổ chức trong văn bản QĐ (việc của sht-qd-nhansu-alignment)."
---

# Chuẩn hóa dữ liệu nhân sự (SHT)

Quy trình xác minh danh tính và bảo toàn tính nhất quán tên riêng trong hồ sơ tổ chức, nhân sự, đánh giá cán bộ. Đúc kết từ một phiên làm việc mà lỗi tên "Bùi Việt Phương" (sai, đúng phải là "Phạm Việt Phương" theo QĐ 040826/QĐ-SHT) đã lan xuyên suốt một skill file và nhiều deliverable mà không ai phát hiện — kể cả khi chính phiên đó đã tự điều tra một nghi vấn tên liên quan mà vẫn không quay lại xác minh với nguồn gốc.

Nguyên tắc bao trùm: **một cái tên sai chốt ở đầu phiên sẽ tự nhân bản qua mọi deliverable tiếp theo, kể cả khi có cơ hội phát hiện giữa chừng.** Việc xác minh danh tính phải xảy ra TRƯỚC khi sản xuất hàng loạt tài liệu, không phải sau khi đã lan ra nhiều file.

## Quan hệ với các skill khác

| Skill | Dùng khi |
|---|---|
| **sht-nen-tang-kiem-chung** (tầng 0) | Lan truyền hiệu chỉnh, đổi tên hàng loạt an toàn, một-bản-có-hiệu-lực, checklist bàn giao — **nạp kèm mọi phiên** |
| **sht-qd-nhansu-alignment** | Soạn thảo/rà soát Quyết định — đối chiếu thẩm quyền, quan hệ báo cáo giữa các QĐ |
| **sht-xacthuc-baocao-hoatdong** | Hồ sơ có số liệu doanh số/KPI lấy từ CRM/dashboard cần đối chiếu trước khi đưa vào văn bản |
| **chuan-hoa-du-lieu-nhansu** (skill này) | Xác minh danh tính người — chạy **trước** hoặc song song với các skill trên bất cứ khi nào hồ sơ có tên người |

Ví dụ dùng chồng: rà soát QĐ (dùng `sht-qd-nhansu-alignment`) nhưng trước khi viết văn bản, chốt danh tính người liên quan bằng skill này; nếu QĐ căn cứ vào thành tích có số liệu, chạy thêm `sht-xacthuc-baocao-hoatdong`.

---

## 1. Chốt danh tính với nguồn chính thức TRƯỚC khi sản xuất tài liệu

Trước khi bắt đầu viết bất kỳ hồ sơ nào có tên người (QĐ, đánh giá, biên bản, check-in onboarding), xác định **nguồn chính thức duy nhất** cho tên riêng của từng nhân vật liên quan:

- Với nhân sự có chức danh chính thức: **Quyết định bổ nhiệm/hợp đồng lao động** — không phải tên đã dùng quen trong hội thoại, không phải tên trong một biên bản họp trước đó.
- Nếu tên xuất hiện dưới nhiều biến thể trong các nguồn khác nhau (transcript, biên bản, báo cáo cũ), **không tự chọn biến thể "nghe hợp lý nhất"** — đối chiếu ngược với văn bản gốc có giá trị pháp lý cao nhất: **QĐ > hợp đồng > biên bản họp > tin nhắn/ghi chú.**

**Ví dụ thật đã xảy ra:** một phiên trước dùng "Bùi Việt Phương" xuyên suốt (kể cả trong 1 skill file), trong khi QĐ bổ nhiệm ghi rõ "Phạm Việt Phương". Phiên đó từng phát hiện một biến thể sai khác ("Trịnh Anh Phương" trong biên bản Ban QLDA) và tự điều tra — nhưng vì không quay lại đối chiếu với QĐ gốc, vẫn không nhận ra "Bùi Việt Phương" cũng sai.

**Bài học: phát hiện một biến thể sai không tự động xác nhận biến thể còn lại là đúng — luôn đối chiếu MỌI biến thể với nguồn gốc, không so sánh các biến thể với nhau.**

## 2. Xử lý tên trùng lặp giữa nhiều người

Khi từ 2 người trở lên trong cùng bối cảnh làm việc có tên giống hoặc gần giống nhau (trùng tên đệm, trùng họ tên lót), đây là vùng rủi ro cao cho việc gán nhầm.

**Quy tắc bắt buộc:**

- Lập danh sách tất cả người trùng tên ngay khi phát hiện, ghi rõ **chức danh + vai trò** phân biệt từng người (VD: "Huyền" có thể là COO, có thể là BA/trợ lý, có thể là nhân sự của một tổ chức khác hoàn toàn không liên quan).
- Khi một cái tên xuất hiện **không kèm chức danh rõ ràng**, không suy đoán theo ngữ cảnh (ai "nghe hợp lý hơn" ở vị trí đó) — dừng lại và xác nhận với người dùng, hoặc tra cứu chức danh trước khi gán.
- Việc suy đoán sai thường xảy ra ở chỗ **tưởng là hợp lý nhất theo ngữ cảnh**: một việc tầm lãnh đạo cấp cao bị gán nhầm cho người có chức vụ thấp hơn cùng tên chỉ vì "gần" trong câu văn.

**Ví dụ thật đã xảy ra:** trong một luồng hội thoại có 3 người tên Huyền (COO Trần Thanh Huyền, Khánh Huyền — BA/trợ lý, và Phó Giám đốc một chi nhánh ngân hàng — không liên quan SHT), việc "dẫn CCO giới thiệu Giám đốc chi nhánh" (việc tầm lãnh đạo cấp cao) bị gán nhầm cho "Khánh Huyền (BA)" thay vì đúng người là COO. Nguyên nhân: đoạn văn bản đứng gần dòng nhắc tên Khánh Huyền hơn, không phải vì chức danh khớp.

**Không tự đổi chức danh để giải quyết xung đột danh xưng.** Nếu 2 người có thể gây nhầm lẫn vai trò (VD "CCO" vs "COO" đọc gần giống), giữ đúng chức danh chính thức của từng người theo QĐ/hợp đồng — không đổi chức danh của người này cho "khớp" với vai trò cảm nhận, vì sẽ tạo xung đột danh xưng với văn bản đã ban hành.

## 3. Một người — nhiều vai trò kiêm nhiệm

§2 xử lý trường hợp NHIỀU NGƯỜI trùng tên. Đây là trường hợp ngược lại: MỘT người giữ đồng thời nhiều chức danh (VD một Giám đốc Khối kiêm nhiệm luôn vị trí SM/quản lý trực tiếp một trung tâm trực thuộc). Rủi ro không phải gán sai người, mà là **gán sai "vai"** — quy công cho cấp cao trong khi hành vi thực ra chỉ thuộc phạm vi công việc của vai thấp hơn mà người đó kiêm nhiệm.

**Quy tắc bắt buộc:**

- Khi dựng hồ sơ đánh giá năng lực/tác động theo MỘT vai trò cụ thể (VD "đánh giá impact ở cấp Khối"), với người đang kiêm nhiệm nhiều vai, phải hỏi rõ: hành vi/bằng chứng này chỉ có thể thực hiện được nhờ thẩm quyền của vai đang đánh giá, hay là việc thường nhật của vai kiêm nhiệm khác cũng làm được?
- Bằng chứng **chỉ tính vào đánh giá của vai đang xét** nếu vượt phạm vi/thẩm quyền của vai kiêm nhiệm còn lại. Hoạt động điều hành thường nhật giới hạn trong phạm vi của vai kiêm nhiệm phải loại khỏi đánh giá vai cấp cao, dù người dùng có xu hướng gộp chung vì "cùng một người làm".
- Không tự suy luận việc kiêm nhiệm — đây là thông tin tổ chức phải được người có thẩm quyền xác nhận trực tiếp (không suy ra từ nhãn/tên nhóm chat hay chức danh không chính thức).

**Ví dụ thật đã xảy ra:** một CCO (Giám đốc Khối Kinh doanh, quản lý 2 trung tâm kinh doanh) được xác nhận kiêm nhiệm thêm chức SM1 (quản lý trực tiếp 1 trong 2 trung tâm đó). Một loạt hoạt động quản lý qua nhóm chat ban đầu bị gộp chung vào "bằng chứng impact cấp CCO" — sau khi biết việc kiêm nhiệm, phải rà lại và loại bỏ các hoạt động chỉ giới hạn trong phạm vi trung tâm mà người đó kiêm SM1 (nhắc lịch chi tiêu một chi nhánh, chúc mừng riêng AM thuộc trung tâm đó...), chỉ giữ lại phần hành vi vượt phạm vi 1 trung tâm (chỉ đạo xuyên cả 2 trung tâm, tương tác với Ban Lãnh đạo/phòng ban khác) làm bằng chứng cấp Khối.

**Hệ quả phụ dễ bỏ sót:** mẫu dữ liệu hiện trường (site visit, đồng hành AM) dùng để đối chiếu cũng sẽ chỉ tập trung ở trung tâm kiêm nhiệm — cần chủ động bổ sung dữ liệu từ trung tâm còn lại, tránh kết luận từ một mẫu lệch.

---

## 4. Bổ sung riêng cho nhân sự trên nền tảng chung

Bốn quy tắc nền (lan truyền hiệu chỉnh, đổi tên hàng loạt an toàn, một-bản-có-hiệu-lực, đặt câu hỏi ngược với nguồn) nằm đầy đủ ở `sht-nen-tang-kiem-chung`. Dưới đây chỉ là phần đặc thù hồ sơ nhân sự:

**Khi quét tìm một cái tên sai** (nền: tầng 0 §1) — chuỗi cần tìm phải là **cụm họ tên đầy đủ** ("Bùi Việt Phương"), không phải một âm tiết đơn lẻ. Quét đủ mọi định dạng: PDF bằng `pdftotext`, DOCX/XLSX bằng `unzip -p | strings`. Ca thật: người dùng chỉ gửi lại vài file để sửa tên; quét chủ động cả 3 thư mục kết nối lôi ra thêm một PDF cũ ở thư mục khác vẫn còn tên sai.

**Khi thay tên trong DOCX/XLSX** (nền: tầng 0 §2) — xác nhận cụm cần thay nằm nguyên trong **một run**; Word hay tách chuỗi do spell-check/revision marker. Nếu có dấu hiệu tách, gộp run trước bằng `docx` → `merge_runs.py`.

**Khi số liệu nhân sự từ hệ thống mâu thuẫn với người cung cấp** (nền: tầng 0 §4) — hỏi cụ thể "có ai nghỉ việc/chuyển bộ phận/đổi vai trò chưa được cập nhật không" trước khi kết luận bên nào sai. Nếu số liệu đó sẽ vào văn bản chính thức, chạy `sht-xacthuc-baocao-hoatdong`.

**Khi một skill hay hồ sơ cũ đã "chốt" một danh tính** — vẫn đối chiếu lại với QĐ gốc mỗi lần tái sử dụng. Chính lỗi "Bùi Việt Phương" đã nằm sẵn trong một skill file và được tin theo nhiều phiên liền.

---

## 5. Checklist riêng của hồ sơ nhân sự

Chạy **sau** checklist nền ở `sht-nen-tang-kiem-chung` §5, không thay thế nó.

- [ ] Danh tính từng người liên quan đã đối chiếu với nguồn chính thức (QĐ/hợp đồng), không suy đoán
- [ ] Mọi biến thể tên đã được đối chiếu với nguồn gốc — không kết luận biến thể này đúng vì biến thể kia đã sai
- [ ] Nếu có tên trùng lặp: đã lập danh sách phân biệt theo chức danh, không gán theo "gần trong câu"
- [ ] Chức danh giữ nguyên theo văn bản đã ban hành, không tự đổi để giải quyết nhầm lẫn danh xưng
- [ ] Nếu người liên quan kiêm nhiệm nhiều vai: đã tách bằng chứng theo đúng vai đang đánh giá, và đã kiểm tra mẫu dữ liệu có bị lệch về một vai không
- [ ] Thay tên theo cụm họ tên đầy đủ, đã gộp run nếu file DOCX có dấu hiệu tách chuỗi
- [ ] Số liệu nhân sự mâu thuẫn giữa hệ thống và người cung cấp đã được hỏi lại, không mặc định bên nào đúng
- [ ] Bản dựng lại từ lịch sử hội thoại (nếu có) đã gắn nhãn "cần xác nhận trước khi dùng chính thức"

