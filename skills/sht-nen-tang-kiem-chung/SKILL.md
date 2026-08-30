---
name: "sht-nen-tang-kiem-chung"
description: "Bốn quy tắc nền tảng áp cho MỌI deliverable của SHT, không phân biệt miền: (1) lan truyền hiệu chỉnh — khi số liệu/tên đổi thì tự quét và sửa mọi file đã tạo; (2) đổi tên hàng loạt an toàn — cụm bảo vệ, dry-run, không find/replace thẳng trên tên người tiếng Việt; (3) một tài liệu — một bản có hiệu lực, xóa bản cũ khi bàn giao, và ghi đúng thư mục đích — không đổ deliverable vào repo mã nguồn/kho skill; (4) checklist bàn giao chung & xuất 5 dạng báo cáo. LUÔN dùng skill này trước khi bàn giao bất kỳ file nào (docx/xlsx/pdf/pptx/biên bản/báo cáo), khi sửa con số hoặc cái tên xuất hiện ở nhiều file, khi người dùng nói \"sửa lại\", \"cập nhật\", \"đổi tên\", \"thay tên\", \"file nào mới nhất\", \"bản nào đúng\", \"lưu nhầm chỗ\", hoặc khi thư mục có nhiều phiên bản. KHÔNG dùng riêng lẻ để xử lý nghiệp vụ cụ thể — luôn dùng KÈM skill nghiệp vụ tương ứng (dự án, nhân sự, tuyển dụng, QĐ, CRM, hợp đồng, CĐS), skill này chỉ giữ phần quy tắc chung mà các skill đó trỏ về."
---

# Nền tảng kiểm chứng & bàn giao (SHT — tầng 0)

Skill này giữ bốn quy tắc mà **mọi** skill nghiệp vụ của SHT đều cần. Trước đây bốn quy tắc này được chép lại ở từng skill, mỗi nơi một dị bản; sửa một nơi thì ba nơi kia lệch. Từ nay chúng chỉ có một bản — bản này.

Skill nghiệp vụ (dự án, nhân sự, tuyển dụng, QĐ, CRM) **trỏ về đây**, chỉ giữ lại phần đặc thù của riêng miền mình.

Nguyên tắc bao trùm: **dữ liệu sai lan nhanh hơn dữ liệu đúng.** Một con số sai nhân bản ra 4–5 deliverable; một cái tên bị thay nhầm đi thẳng vào văn bản trình ký.

---

## 1. Lan truyền hiệu chỉnh — bắt buộc, không đợi nhắc

Khi một số liệu, một cái tên, hay một mẩu ngữ cảnh thay đổi giữa phiên: **tự động cập nhật mọi deliverable đã tạo.** Không đợi người dùng nhắc. Sau đó báo rõ đã đổi những gì.

**Quy trình:**

1. Liệt kê **mọi** file đã sinh ra trong phiên, cộng với file cũ liên quan trong các thư mục kết nối.
2. Xác định file nào chứa giá trị đó — **kể cả dạng đã làm tròn hoặc viết khác**. "1,30 tỷ" nằm cạnh "1.299.473.618" là cùng một con số; sửa một, sót một là chuyện thường gặp.
3. Quét **toàn bộ thư mục liên quan**, không chỉ file người dùng vừa nhắc. Người yêu cầu sửa thường chỉ nhớ được vài file.
4. Quét đủ **mọi định dạng**: PDF bằng `pdftotext`, DOCX/XLSX bằng `unzip -p | strings`. Đừng kiểm mỗi định dạng dễ nhất rồi coi là xong.
5. Sửa tất cả, rồi **verify bằng cách trích xuất lại nội dung file** — không tin vào việc "đã chạy lệnh sửa".
6. Báo cáo minh bạch: đã quét những đâu, đã sửa những gì. Không chỉ báo "đã sửa xong".

**Hai ca thật đã xảy ra:**

- VAT gói nội thất bổ sung 33.827.200đ → phải cập nhật đồng thời file Excel mô hình (giá trị **và** công thức tổng), công văn (bảng chi tiết **và** phần thân), tin nhắn Zalo, infographic PDF (cả KPI rút gọn "1,33 tỷ" lẫn tỷ lệ %).
- Người dùng gửi lại vài file để sửa tên. Quét chủ động cả 3 thư mục kết nối lôi ra thêm một PDF cũ ở thư mục khác vẫn còn tên sai — không nằm trong danh sách được chỉ định.

Nguyên tắc này cũng áp khi **bổ sung ngữ cảnh giữa phiên** (VD "anh X là chuyên gia 20 năm kinh nghiệm"): rà lại toàn bộ tài liệu để cập nhật mọi vị trí liên quan — thành phần tham dự, dàn ý trình bày, phân công trả lời câu hỏi, người phụ trách hạng mục — không chỉ thêm một dòng ở chỗ vừa được hỏi.

---

## 2. Đổi tên hàng loạt — vùng nguy hiểm nhất

**Không bao giờ chạy find/replace thẳng trên tên người tiếng Việt.** Âm tiết tên người trùng với địa danh và từ vựng thông thường.

| Thay thế ngây thơ | Hậu quả |
|---|---|
| `Hà` → `Anh Hà` | "Hà Giang" → "Anh Hà Giang"; "Đông Hà Nội" → "Đông Anh Hà Nội" |
| `Nguyên` → `Anh Nguyên` | "Thái Nguyên" → "Thái Anh Nguyên" |
| `Phương` → `Anh Phương` | "phương pháp" → "Anh Phương pháp" |
| `An` → `Chị An` | "an toàn", "an ninh" |
| `Khoa` → `Anh Khoa` | "khoa học" |
| `Việt` → `Anh Việt` | "Việt Nam" |

**Quy trình an toàn — sáu bước, không rút gọn:**

1. **Thay theo cụm họ tên đầy đủ** (3 từ trở lên: "Bùi Việt Phương"), không theo âm tiết đơn lẻ.
2. Khai báo danh sách **cụm bảo vệ** (§Phụ lục) trước khi chạy.
3. Chạy **dry-run**: xem trước mọi vị trí sẽ đổi kèm ngữ cảnh, duyệt rồi mới áp dụng.
4. Với DOCX/XLSX: xác nhận cụm cần thay nằm nguyên trong **một run**. Word hay tách chuỗi thành nhiều mảnh do spell-check/revision marker — nếu có dấu hiệu tách, gộp run trước (skill `docx`, `merge_runs.py`).
5. Sau khi áp dụng, **quét lại** ba thứ: (a) mẫu lỗi `Anh Anh`, `Chị Chị`, `chị Chị`; (b) cụm bảo vệ có bị dính tiền tố không; (c) chỗ dùng tên đúng mục đích khác (người khác cùng âm tiết) có bị đổi nhầm không.
6. **Kiểm riêng tiêu đề viết HOA** — regex chữ thường không bắt được `ĐÔNG HÀ NỘI`. Lỗi này rất dễ sót.
7. **Render ra ảnh và nhìn tận mắt** trang có nhiều tên nhất.

---

## 3. Một tài liệu — một bản có hiệu lực

Sinh file mới mỗi lần sửa mà không hủy bản cũ tạo hỗn loạn phiên bản: thư mục đầy `_v2`, `_v3`, `_040826`, `_UPGRADED`, và **không ai biết bản nào đúng để trình ký**. Đã xảy ra: 7 phiên bản cùng một biên bản họp.

- Khi thay thế một tài liệu, **ghi rõ ngay trong chính văn bản**: "Bản này thay thế hoàn toàn bản trước, đề nghị hủy/không sử dụng bản cũ."
- **Xóa bản cũ ngay tại thời điểm bàn giao.** Nếu lệnh xóa bị chặn quyền, **xin quyền rồi thực hiện** — không dừng ở việc khuyên người dùng tự xóa.
- **File trong thư mục người dùng chọn có thể bị hệ điều hành khóa** nếu đang mở ở Word/trình xem PDF trên máy họ; quyền cấp qua công cụ nội bộ không thắng được khóa cấp OS. Khi `rm`/ghi đè báo "Permission denied" dù đã xin quyền: thử lại 1–2 lần; nếu vẫn lỗi, lưu tạm bằng hậu tố `_v2`, báo người dùng đóng file gốc, rồi **hoàn tất đổi lại đúng tên chuẩn** ngay khi họ xác nhận. Không dừng ở việc báo lỗi suông.
- Đặt tên file theo **nội dung + trạng thái hiệu lực**, không theo số lần sửa.
- Sửa nhiều vòng trong cùng một phiên → **ghi đè lên cùng một file**.
- Cuối phiên, liệt kê danh mục file có hiệu lực, phân biệt rõ **file mình tạo** với **file gốc của người dùng** (không bao giờ tự động xóa file gốc).
- Một tài liệu quan trọng có thể **chưa từng được lưu ra file** — chỉ tồn tại trong lịch sử hội thoại phiên trước. Khi được yêu cầu "tìm file X" mà không thấy trong thư mục, kiểm tra khả năng này trước khi kết luận không tồn tại. Nếu phải dựng lại từ lịch sử, **trích nguyên văn** đoạn người dùng đã cung cấp thay vì diễn giải theo trí nhớ; nếu chỉ có bản tóm tắt, phải gắn nhãn "bản dựng lại — cần xác nhận trước khi dùng chính thức".
### 3.1 Ghi đúng chỗ — thư mục sản phẩm không phải thư mục hạ tầng

Thư mục làm việc mặc định **không mặc nhiên là nơi chứa deliverable**. Nó có thể là repo mã nguồn, kho skill, hoặc thư mục cấu hình mà người dùng đang mở sẵn vì lý do khác.

**Trước khi ghi file đầu tiên của phiên, nhìn vào cấu trúc thư mục đích:**

| Dấu hiệu bên trong | Loại thư mục | Được đổ sản phẩm? |
|---|---|---|
| `.claude-plugin/`, `skills/`, `plugin.json` | Kho skill / plugin | ❌ |
| `.git/`, `src/`, `package.json`, `requirements.txt` | Repo mã nguồn | ❌ |
| `.env`, `config/`, `node_modules/` | Cấu hình / phụ thuộc | ❌ |
| Chỉ có tài liệu nghiệp vụ (`.docx`, `.xlsx`, `.pdf`, `.md`) | Thư mục sản phẩm | ✅ |

Rơi vào ba loại đầu: **hỏi người dùng nơi lưu trước khi ghi**, không ghi rồi dọn sau. Deliverable lẫn trong repo gây rối khi họ đóng gói, commit hoặc chia sẻ — và thường chính họ phải phát hiện ra.

**Ngoại lệ:** khi bản thân thư mục hạ tầng *là* đối tượng công việc (sửa skill, sửa mã nguồn, cập nhật cấu hình) thì ghi vào đó mới đúng. Phân biệt bằng một câu hỏi: *file này là sản phẩm giao cho người dùng, hay là một phần của hệ thống đang được sửa?*

**Ca thật (27/08/2026):** hồ sơ ứng viên tuyển dụng bị ghi thẳng vào thư mục nguồn plugin `sht-skills/`. Nguyên nhân: coi thư mục làm việc mặc định là nơi đổ sản phẩm mà không nhìn cấu trúc bên trong. Người dùng phải tự phát hiện và nhắc.


---

## 4. Đặt câu hỏi ngược với nguồn "tưởng đúng tuyệt đối"

Không có nguồn nào mặc định đúng hơn nguồn khác. CRM, dashboard, skill cũ, tài liệu đã đóng gói — tất cả đều có thể lỗi thời hoặc đã mang sẵn lỗi lan truyền.

- Khi số liệu con người cung cấp lệch với hệ thống, **đừng mặc định hệ thống đúng**. Truy tiếp nguyên nhân lệch trước khi kết luận.
- Khi một skill hay tài liệu cũ đã "chốt" một thông tin, vẫn đối chiếu lại với nguồn gốc mỗi lần tái sử dụng — không tin theo chỉ vì đã dùng nhiều lần.

**Ca thật:** dashboard CRM liệt kê 10 AM thuộc một trung tâm kinh doanh, người phụ trách nói "5/8". Truy tiếp thì 2 trong 10 AM đã nghỉ việc mà hệ thống chưa cập nhật; loại ra thì khớp chính xác. **Hệ thống mới là bên sai.**

---

## 5. Checklist bàn giao chung

Chạy trước khi nói "đã xong". Lệnh chạy thành công **không đồng nghĩa** kết quả đúng.

- [ ] Đã xác định đúng thư mục đích **trước khi ghi file đầu tiên** — không đổ deliverable vào repo mã nguồn/kho skill (§3.1)
- [ ] Mọi số liệu then chốt đã đối chiếu ngược về nguồn, không có con số nào không truy được xuất xứ
- [ ] Mâu thuẫn giữa các nguồn đã ghi vào mục "Vấn đề bỏ ngỏ", **không tự chọn một bên** — kể cả khi được yêu cầu ẩn bớt
- [ ] Ô trống dùng `[Cần bổ sung]`, không tự điền
- [ ] Nếu có đổi tên/số liệu: đã lan truyền sang **mọi** file (§1) và verify bằng cách trích xuất lại nội dung
- [ ] Nếu có thay tên hàng loạt: đã quét lại `Anh Anh`/`Chị Chị`, cụm bảo vệ, và tiêu đề viết HOA (§2)
- [ ] Đã **render ra ảnh và đọc từng trang** — không bàn giao file chưa nhìn tận mắt
- [ ] Bản cũ vô hiệu đã bị **xóa thật**, không chỉ được khuyên xóa (§3)
- [ ] Đã liệt kê danh mục file có hiệu lực cuối phiên, phân biệt file mình tạo với file gốc
- [ ] Nếu deliverable có ràng buộc nội dung (thuần kỹ thuật / đối ngoại): đã chạy `grep` xác minh, không chỉ đọc bằng mắt (§6.2)
- [ ] Tóm tắt bàn giao **ngắn** — chỉ nêu hành động ưu tiên và cảnh báo, không liệt kê lại toàn bộ nội dung file

Skill nghiệp vụ bổ sung mục riêng của mình vào checklist này, không viết lại checklist mới.

---

## 6. Kết xuất theo người đọc

**Một deliverable phục vụ đúng một người đọc.** Gộp hai mục đích vào một file thì không thỏa mãn được ai: người thẩm định cần trích dẫn và công thức để audit, lãnh đạo cần vài trang nhìn là quyết được, đối tác cần bản không có ngôn ngữ đối kháng.

Năm dạng chuẩn của SHT — chọn dạng, không tự chế:

| Dạng | Người đọc | Đặc trưng bắt buộc |
|---|---|---|
| **Bản đầy đủ** | Team dự án, kỹ thuật, pháp chế | Trích dẫn nguyên văn kèm toạ độ (điều/trang/mốc thời gian), bảng đối chiếu chi tiết |
| **Bản điều hành** | Ban Lãnh đạo | 2–7 trang. Cấu trúc: tình hình nổi bật → các vấn đề cần quyết, mỗi vấn đề kết bằng khung **"Đề nghị quyết"** → việc làm ngay không chờ ký → bảng phân công người quyết định |
| **Bản thuần kỹ thuật** | Đối tác kỹ thuật, bộ phận triển khai | Loại bỏ **hoàn toàn** yếu tố tài chính/thương mại |
| **Bản đối ngoại** | Khách hàng, đối tác | Viết từ lợi ích của đối phương, tuyệt đối không dùng ngôn ngữ đối kháng |
| **Bảng luận điểm đàm phán** | Người trực tiếp đàm phán | 4 cột: Yêu cầu — Căn cứ — Lập luận đối phương dự kiến — Phản biện |

Skill nghiệp vụ **chọn dạng cần dùng và bổ sung nội dung đặc thù**, không định nghĩa lại dạng mới trùng nghĩa.

### 6.1 Xuất file

- **PDF**: WeasyPrint với file định kiểu chuẩn `references/pdf-style.css` (font Liberation/DejaVu cho tiếng Việt, bảng dài ngắt trang bằng `class="brk"`, header lặp lại). Không tự viết CSS mới cho từng báo cáo.
- **Khổ cố định** (infographic, A4 ngang): tính trước bề rộng in được = bề rộng trang − 2×lề, ép `flex-wrap: nowrap` cho layout cột cố định. Đừng để trình duyệt tự tính rồi tràn trang.
- **Excel có công thức**: viết công thức thật, không hard-code kết quả; chạy recalc yêu cầu `total_errors: 0`, rồi đọc lại **giá trị đã tính** cả cột chữ lẫn cột số.

### 6.2 Xác minh bằng máy trước khi phát hành

Bản có ràng buộc về nội dung phải được **quét bằng `grep`**, không tin vào việc "đã viết cẩn thận":

- **Bản thuần kỹ thuật** → quét sạch mọi từ khóa tiền tệ (`VNĐ`, `đồng`, `tỷ`, số tiền lớn).
- **Bản đối ngoại** → quét sạch từ đối kháng (`mâu thuẫn`, `vô hiệu`, `trái luật`, `vi phạm`, `phạt`, `chấm dứt`). Kèm rào chắn nội bộ: *"Chưa gửi văn bản chính thức cho [đối tác] khi chưa có phê duyệt này."*

Quét xong vẫn phải render ra ảnh và đọc từng trang (§5).

---

## 7. Tự kiểm trước khi báo xong

Luật này sinh ra từ hai lỗi thật trong phiên hunt CV 25/08/2026: báo "đã lưu xong" khi
file nằm ở thư mục tạm người dùng không mở được, và báo "16 lời mời" khi thật là 18 vì
đếm từ trí nhớ thay vì từ log.

Cả hai cùng một họ: **tuyên bố một điều là đúng mà chưa đối chiếu nguồn thật.**

### Cơ chế: dán bằng chứng vào câu báo cáo

Mỗi tuyên bố phải kèm nguồn kiểm chứng ngay tại chỗ. Muốn trích được nguồn thì buộc
phải đi nhìn — đó là toàn bộ lý do cơ chế này hiệu quả.

| Không được viết | Phải viết |
|---|---|
| "Đã lưu xong file" | "Đã lưu: `<đường dẫn tuyệt đối>` — mở lại được, N sheet" |
| "Đã gửi 16 lời mời" | "18 lời mời — đếm từ `<màn hình xác nhận của nền tảng>`" |
| "Đã lọc theo TP.HCM" | "Chip đang áp: `TP Hồ Chí Minh` (đọc lại sau khi chọn)" |
| "Đã xong" | "Xong — `<việc>`, kiểm bằng `<nguồn>`" |

### Bốn câu chốt

1. **File ở đâu?** Đường dẫn tuyệt đối, đã mở lại được. Chưa có quyền ghi vào thư mục
   nghiệp vụ thì **hỏi trước**, không lưu tạm rồi báo hoàn thành.
2. **Con số lấy từ đâu?** Đếm lại từ log thao tác hoặc màn hình xác nhận của chính nền
   tảng. Không lấy từ báo cáo trước của mình.
3. **Thao tác đã áp đúng chưa?** Sau mỗi lần chọn từ dropdown hoặc bộ lọc, đọc lại giá
   trị thực đang áp trước khi chạy tiếp.
4. **Có gì chưa xác minh được không?** Chưa đọc được bằng chứng thì không thực hiện hành
   động tốn phí hoặc không hoàn tác được.

Chưa dựng chốt máy cho luật này. **Điều kiện leo thang:** nếu sau khi có luật này mà vẫn
xuất hiện thêm một lần "báo xong chưa kiểm chứng", lần đó là căn cứ dựng hook.

---

# PHỤ LỤC — CỤM BẢO VỆ KHI ĐỔI TÊN HÀNG LOẠT

```json
["Hà Giang", "Đông Hà Nội", "Thái Nguyên", "Yên Bái", "Hà Nội",
 "Việt Nam", "Ninh Thuận", "Tây Ninh", "Bạc Liêu", "Bắc Thăng Long", "Ba Vì",
 "Sơn Tây", "Thủ Thiêm", "Nha Trang", "Vĩnh Hải", "Ngô Quyền", "Cần Thơ",
 "phương pháp", "phương án", "phương tiện", "phương án kinh doanh",
 "an toàn", "an ninh", "khoa học",
 "nguyên tắc", "nguyên nhân", "nguyên vật liệu", "nguyên văn",
 "thảo luận", "chiến lược", "bạn Thúy"]
```

Danh sách **không đầy đủ** — luôn chạy dry-run và đọc ngữ cảnh trước khi áp dụng. Bổ sung cụm mới vào đây mỗi khi gặp một ca dính nhầm.

