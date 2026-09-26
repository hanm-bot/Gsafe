# Phân vai bộ ba — phiếu việc từng người

Mỗi phiếu ghi: **Đầu vào · Các bước · ĐẠT khi · Bẫy đã gặp**. Bảng này là phân công, không
định nghĩa luật — luật ở quy chế `docs/QUY_CHE_PHOI_HOP_TAC_CHIEN_CLAUDE_ANTI_SHT.md` và ở
skill chủ sở hữu được trỏ tới. Bẫy lấy từ dự án `SHT-UPSA-01` (26/09/2026); hồ sơ gốc ở
`plans/20260926-khung-giai-quyet-van-de-3-duong-ray/` và `docs/audit/2026-09-26_QA-audit-SHT-UPSA-01-*.md`.

---

## §1. Vai ① — Điều phối & kiến trúc (Claude)

**Đầu vào:** lệnh của Mr. Hà (có thể kèm ảnh, link, kiến trúc mẫu); `CLAUDE.md`; memory;
`plans/` cũ cùng chủ đề; `00_NGUON-HO-SO.md` nếu đụng workspace.

**Các bước**
1. Đọc lệnh, đánh dấu chữ viết tắt / chỗ hai nghĩa → hỏi một câu (AskUserQuestion, có phương án khuyến nghị).
2. Thẩm định: đối chiếu thứ người dùng gửi với hạ tầng thật (file, script, hook có chạy không). Nguồn ngoài (link luật, bài viết) → mở bản gốc chính thức; link sai thì nói.
3. Đo khi cần xếp hạng/ưu tiên: ghi câu lệnh đo, phạm vi, giới hạn.
4. Lập `plan.md`: bước P1…Pn, cột Trách nhiệm, DoD, mục ngoài phạm vi → trình Gate 1.
5. Với từng ca: chọn đường ray theo `sht-cds-thiet-ke-agent/references/chon-duong-ray.md` (ray 1 mặc định; ray 3 = có cổng JEV; ray 2 chỉ qua RFC).
6. Viết `buoc-XX/task-XX.md`: mục tiêu, việc cần làm, test (bảng ca → kỳ vọng), **không được làm**, DoD bằng chứng (SKILL.md §4), ngoài phạm vi.
7. Hết 2 vòng QA → soạn `rfc/rfc-XX.md` 3 phương án có khuyến nghị.

**ĐẠT khi:** mỗi DoD đo được bằng một lệnh; phiếu nêu đúng file được sửa; mọi con số trong plan có nguồn.

**Bẫy đã gặp**
- Đoán "3 loại văn bản dùng nhiều nhất" thay vì đo → bị trả lại.
- Hiểu nhầm "NDD" → gỡ nhầm P5 khỏi plan, phải ghi đính chính.
- Phiếu viết "đoạn nội dung thường" mà không định nghĩa → máy kiểm xác định theo tên style → sinh lỗ `Body Text` (RFC-03).
- Phiếu bắt báo THIẾU cho khoá vốn tuỳ chọn (`co_quan_chu_quan`) → lỗi của phiếu, phải đính chính trong task.

---

## §2. Vai ② — Thực thi (Anti)

**Đầu vào:** `task-XX.md` đã qua Gate 1; phiếu QA vòng trước nếu là vòng 2.

**Các bước**
1. Đọc đủ phiếu và mẫu gốc được chỉ (không dựng theo trí nhớ).
2. Làm đúng danh sách file được phép sửa; dữ liệu thử giả lập trong `tempfile`.
3. Chạy test, đột biến **mới** trong thư mục tạm mới; dán output nguyên văn, tên thư mục tạm, thời gian.
4. Băm SHA-256 đủ các sổ thật trước/sau; `find` rác; dọn `scratch/`.
5. Gặp chốt kiểm chặn một yêu cầu hợp lệ → **dừng, ghi "vướng" trong report**, đề xuất RFC.
6. Ghi `reports/report-XX[-vong-2].md` đúng thư mục; không tự tuyên bố nghiệm thu.

**ĐẠT khi:** QA chạy lại ra đúng những gì report ghi.

**Bẫy đã gặp** (loại lỗi thật, để vai ③ biết mà soi)
- Chép mã băm và output đột biến từ report cũ.
- Ghi "toàn văn" nhưng chỉ dán một phần; ghi "`find` rỗng" khi còn file sót.
- Để bản script đột biến trong `scratch/` của kho; để rác test trong workspace.
- Report/ảnh lưu ngoài kho (thư mục riêng của IDE).
- Đột biến "tắt kiểm Tiêu ngữ" không được áp — output vẫn báo thiếu Tiêu ngữ.
- Đổi style sang `Body Text` để lọt máy kiểm cỡ chữ (lách chốt — lỗi nặng nhất).

---

## §3. Vai ③ — QA Lớp 2 (Claude; Anti khi đảo vai)

**Đầu vào:** report, phiếu giao, phiếu QA vòng trước. Quy tắc chung: `sht-quan-tri-dn` §6 (đọc trước).

**Các bước**
1. Kiểm mtime: report/code có đổi so với lần QA trước không.
2. Chạy lại độc lập mọi bộ test; tự băm sổ; tự `find`.
3. Tự dựng ≥ 1 ca đối kháng không có trong report (với chốt kiểm: ít nhất một ca cố né).
4. Đột biến trên bản sao trong thư mục tạm: chứng minh test bảo vệ chốt FAIL khi chốt bị gỡ. Ca đối chứng cũng hỏng → "không kiểm được".
5. Với .docx: xuất PDF bằng Word, liệt kê phông nhúng, render trang 1 và so ảnh với mẫu gốc.
6. Phân loại từng lỗi: **của phiếu** (người viết phiếu) hay **của bên thực thi**.
7. Ghi phiếu 5 mục; phán quyết ĐẠT / vòng 2 (danh sách C1…Cn) / RFC; dòng "Ghi cho M5".

**ĐẠT khi:** mọi kết luận trong phiếu có lệnh/đầu ra tự chạy đứng sau.

**Bẫy đã gặp**
- Mọi ca thử của QA đều dùng style `Normal` → bỏ sót lỗ chỉ-kiểm-`Normal` suốt hai bước (P5b → P5d).
- `echo exit=$?` sau ống lệnh đo exit của lệnh cuối, không phải của script.
- Ghi file bằng Python mặc định đổi LF → CRLF, `diff` báo sửa cả file.
- Harness đột biến lệch đường dẫn → cả đối chứng cũng FAIL; đã ghi đúng "không kiểm được".

---

## §4. Vai ④ — Người duyệt HITL (Mr. Hà)

**Đầu vào:** plan (Gate 1), RFC, phiếu Gate 3, câu hỏi của vai ①.

**Các bước**
1. Gate 1: duyệt phạm vi + người + DoD.
2. Chọn phương án RFC (A/B/C) hoặc chọn ca/đường ray khi được hỏi.
3. Gate 3: nghiệm thu sau khi đọc phiếu QA cuối.
4. Tự bấm push (lệnh một dòng do Claude đưa).

**ĐẠT khi:** mỗi quyết định có bản ghi Sổ Cái trích nguyên văn, đúng nhãn cổng, `actor` là `hanm@shtech.com.vn`.

**Bẫy đã gặp**
- Lệnh ngắn có chữ viết tắt ("NDD") bị agent hiểu sai → nên đọc lại câu agent tóm tắt lệnh trước khi agent ghi sổ.
- "Try again" là tín hiệu hữu ích: agent đang đoán; buộc agent đo.

---

## §5. Vai ⑤ — Soạn văn bản NĐ30

**Luật và thông số:** `sht-nen-tang-kiem-chung` §9 và `references/the-thuc-nd30.md`; phân vai
chi tiết soạn/kiểm: `references/phan-vai-duong-ong-xuat-ban.md` Vai C, Vai D. Phiếu này chỉ tóm
đường chạy.

**Các bước**
1. Văn bản nội bộ/quy chế (Tầng 1): viết `.md` → `python .agents/scripts/sinh-word-tu-md.py <file.md>`.
2. Biên bản / công văn / báo cáo (Tầng 2): `.md` có YAML front matter (`loai: BB|CV|BC`) → `python .agents/scripts/sinh_van_ban_nd30.py <vao.md> <ra.docx>`. Khoá thiếu → giữ `…` và đọc dòng `THIẾU:`; **không** tự điền số, ngày, người ký.
3. Kiểm: `kiem_xuat_ban_docx.py <file.docx> [--loai BB|CV|BC]` phải exit 0.
4. Xuất PDF bằng Word (`SaveAs2`, FileFormat 17) → phông nhúng chỉ `TimesNewRoman*` (+ Consolas cho khối mã) → nhìn ảnh trang 1.
5. Sửa văn bản thì sửa `.md` rồi sinh lại; `.docx` có dòng "BẢN IN DẪN XUẤT … từ bản nguồn" chỉ tới `.md` gốc.

**ĐẠT khi:** L4 exit 0 **và** PDF qua Word chỉ nhúng Times New Roman (+ Consolas).

**Bẫy đã gặp:** xem Vai D ở `phan-vai-duong-ong-xuat-ban.md` (lỗ `Body Text`, emoji, Quốc hiệu gãy dòng).
