# Phân vai cổng quyết định JEV — phiếu việc từng người

Mỗi phiếu: **đầu vào · các bước · tiêu chí ĐẠT · bẫy đã gặp thật**. Luật chung nằm ở `SKILL.md`; phiếu chỉ ghi việc riêng của vai.

Triad theo `SHT-SOP-AI-01`: Claude (kiến trúc & QA) · Anti (thực thi) · Mr. Hà (duyệt). Một người kiêm nhiều vai được, trừ việc **tự làm QA cho sản phẩm của chính mình**.

---

## Vai A — Kiến trúc & soạn task (Claude)

**Đầu vào:** yêu cầu của Mr. Hà; `00_NGUON-HO-SO.md` của workspace; hàng chờ và sổ JEV hiện tại; danh sách nhắc việc hoặc câu hỏi nghiệp vụ.

**Các bước:**
1. **Hỏi chọn ca, đừng tự chọn** khi phạm vi chưa được duyệt — đưa 3–4 ứng viên kèm lý do ca đó là phép thử tốt (câu trả lời mơ hồ như "2, 3" thì hỏi lại một câu sắc).
2. Ghi phạm vi vào Sổ Cái (`ghi-log-hitl.py --append`, `--gate "Gate 2"`) bằng **nguyên văn** câu chọn.
3. **Dò trước bằng chứng theo tên file** trong kho nguồn và workspace để biết bẫy của ca nằm đâu — nhưng **không** đưa đáp án vào task. Chỉ đặt luật chung (truy nguồn, không suy từ tên file, nêu phạm vi đã tìm…) để kiểm được bên thực thi có đọc thật không.
4. Viết task ở `plans/<dự án>/buoc-NN/task-NN.md`: câu hỏi nghiệp vụ nguyên văn, luật riêng của ca, chuẩn P7, DoD đo được, nơi nộp report.
5. Khi Mr. Hà bổ sung thông tin giữa chừng (ví dụ "PO-38 đang hoàn thiện", "họp Ingenico ngày mai") → cập nhật task bằng mục có ngày + nguyên văn, **không** viết đè.

**ĐẠT khi:** task đọc riêng là làm được; mỗi mục DoD kiểm được bằng lệnh; có hạn nếu có mốc thật.

**Bẫy đã gặp:**
- Spec viết lỏng một chữ → bên thực thi làm đúng chữ mà sai ý: "`target_doc` **chứa** mã" sinh lỗi so chuỗi con (W4); "danh sách loại trừ kiểm **trước**" sinh khe tắt cả phép dò (T5b); "bằng chứng phải là file tồn tại" chặn luôn URL nguồn sống (T4). → Viết spec như viết test: nêu cả ca phải qua lẫn ca phải trượt.
- Ticket thiếu trường `ket_luan` khiến phép dò cụm trạng thái đặt nhầm vào câu hỏi (P3 vòng 1). → Liệt kê đủ trường trước khi giao.

---

## Vai B — Lập quyết định ca thật (Anti)

**Đầu vào:** task đã duyệt; quyền đọc kho nguồn theo `00_NGUON-HO-SO.md`.

**Các bước:**
1. Đọc **toàn bộ** `00_NGUON-HO-SO.md` — kể cả các mục "đã kiểm lại", "cấm dùng làm căn cứ".
2. Tìm mọi văn kiện liên quan ở **kho nguồn**; với từng văn kiện ghi người soạn và ngày **theo chính văn kiện**, phân biệt văn kiện gốc với tài liệu phân tích.
3. Trích **nguyên văn** kèm tên file cho từng ý dùng làm căn cứ.
4. Lập `data/workspaces/<ws>/_drafts/quyet_dinh_<ma>.json` đúng schema; `ket_luan` tách "văn kiện nói rõ" / "suy luận"; phần chưa rõ → `HOI_NGUOI` + câu hỏi cụ thể.
5. Chạy cổng bằng **một script lưu trong `buoc-NN/`**, dán dòng log định tuyến và dòng mới trong sổ.
6. Report ở `plans/<dự án>/reports/report-NN.md` (không phải `reports/` ở gốc kho): phương pháp + lệnh thật + kết quả thật + md5 sổ trước/sau + mục "Chưa làm / không làm được" nêu thật.

**ĐẠT khi:** validator chấp nhận; đúng 1 dòng mới trong đúng sổ; mọi trích dẫn khớp nguyên văn; mỗi câu "đã kiểm X" khớp đúng việc đã chạy.

**Bẫy đã gặp:**
- Viết "đã kiểm tra bằng mắt" nhưng mô tả chép từ phiếu rà soát cũ, ảnh render lại là trang khác (P8-F1).
- Khai "đã so lớp hình ảnh" trong khi chỉ đếm ảnh nhúng (P9-G1).
- Gọi tài liệu AI soạn đứng tên Khối CNTT là "văn kiện gốc", bỏ qua phiếu đã cấm dùng → quyết định đi TỰ LÀM và sai (P12).
- Suy "Ban Giám đốc đã duyệt" từ một dòng chỉ có trong bản nháp của Claude (P13).
- Chọn "bản mới nhất" chỉ theo giờ sửa, không so nội dung hai tệp cùng tên (P10).
- Đặt file quyết định sai schema rồi tự ghi `"status": "HANG_CHO"` và báo đã qua cổng (K2).
- Để file trích văn bản PO-38 nội bộ trong `plans/…/reports/` (P11).
- Report ghi "hoàn thành 100% / không có gì chưa làm" ở hầu hết các vòng — người QA đã không tin và đúng khi không tin.

---

## Vai C — QA Lớp 2 (Claude)

Quy tắc chung: `sht-quan-tri-dn` §6. Phiếu này là trình tự riêng cho cổng JEV.

**Các bước:**
1. **Kiểm mtime trước tiên.** "Đã nộp" ≠ file đã đổi — đã xảy ra 4 lần trong một phiên. So giờ sửa report, code, sổ với lần QA trước; không có gì mới thì báo lại, không QA lại bản cũ.
2. **md5 3 sổ JEV + Sổ Cái** và `ghi-log-hitl.py --verify`; soi dòng cuối Sổ Cái xem có bản ghi lạ không.
3. **Chạy lại độc lập trên bản sao** trong scratchpad (copy scripts + schemas, sổ tạm); kho thật chỉ để đo md5 trước/sau. Script phản biện của QA phải **từ chối chạy** nếu chưa trỏ vào bản sao (`JEV_SCRIPTS_DIR`).
4. Nếu bên thực thi sửa script phản biện của QA → `diff` với bản gốc, chỉ chấp nhận thay đổi thích ứng schema.
5. **Đối chiếu từng trích dẫn** với văn kiện gốc (docx qua `word/document.xml`, PDF qua PyMuPDF, chuẩn hoá NFC + khoảng trắng); kiểm file bằng chứng tồn tại và ngày khai khớp ngày thật.
6. **Tự nghĩ ca phản biện mới** nhắm vào đúng phần vừa sửa (không dấu, viết hoa, chuỗi con, mã trùng khác nội dung, bằng chứng trộn…).
7. Rà rác: `find -mmin` trong kho, thư mục `scratch/`, file trích văn bản nguồn, bản sao đặt nhầm chỗ.
8. Phiếu ở `docs/audit/<ngày>_QA-audit-<dự án>-<bước>.md` có dòng `DA-DOI-CHIEU-NGUON`; trình Mr. Hà theo **đã sửa gì / còn gì / cần anh quyết gì**, kèm khuyến nghị phản hồi.

**Giới hạn vòng:** tối đa 2 vòng sửa (SOP-AI-01 §5.2). Phát hiện **mới** ngoài phạm vi phiếu trước → không trả vòng 3 (dời cột gôn); chuyển thành tiền điều kiện bước sau hoặc mở RFC. Lỗi do chính spec của QA viết lỏng → nhận lỗi, sửa nhỏ không tính vòng.

**Không tự chấm bản mình soạn.** Khi Claude là người soạn (ví dụ bản PO-38 lọc nội bộ), giao Anti kiểm; Claude chỉ đối chiếu report của Anti với thực tế.

**Bẫy đã gặp:** QA chạy bộ đếm tự động thô rồi báo sai — luôn in thẳng dòng kết quả ra xem trước khi kết luận; sổ mặc định của bản sao còn dữ liệu lần trước làm ca idempotent "trượt giả" — dùng bản sao mới cho mỗi lần chạy.

---

## Vai D — Người duyệt HITL (Mr. Hà)

**Việc của vai:**
1. **Chọn phạm vi** (ca nào, workspace nào, ngưỡng nào) — mọi phạm vi mới là một Gate 2.
2. **Trả lời câu hỏi `HOI_NGUOI`** bằng hiểu biết hoặc văn kiện anh có (ca NDA: anh đưa bản ATG đã ký vào kho, câu trả lời vào `tra_loi`).
3. **Ra phản hồi** bằng một câu có mã quyết định: *"Chấp nhận JEV-…"*, *"Bác JEV-…, lý do: …"*, *"Sai JEV-…, lý do: …"*. Chọn theo nghĩa ở `SKILL.md` §4 — nhầm BI_BAC với SAI làm lệch số liệu hiệu chỉnh.
4. **Quyết RFC** khi QA đã hết 2 vòng: vòng ngoại lệ có khung, hay đóng có điều kiện.
5. **Cấp và thu quyền** (đọc kho nguồn bằng Python, vòng qua sandbox) — ghi phạm vi vào `00_NGUON-HO-SO.md`.
6. **Nghiệm thu** từng bước và Gate 3 (cho phép sửa bản đồ 5 lớp, `AI_Architecture_Core.md`).

**Mẹo:** câu duyệt được ghi **nguyên văn từng ký tự** vào Sổ Cái — gõ rõ mã quyết định; một câu duyệt nhiều quyết định vẫn được, Claude sẽ tách thành nhiều bản ghi cùng nguyên văn.
