---
name: "quan-tri-he-thong-skill"
description: "Quản trị quan hệ giữa các skill SHT: audit trùng lặp, xung đột trigger, tham chiếu gãy, frontmatter hỏng; nâng cấp và phát hành an toàn. LUÔN dùng khi nói \"upgrade skill\", \"audit skill\", \"skill không tự kích hoạt\", \"gộp/tách skill\". KHÔNG dùng để viết nội dung bên trong một skill (skill-creator)."
---

# Quản trị logic hệ thống skill (SHT)

Skill này không dạy cách viết một skill. Nó dạy cách giữ cho **cả đàn skill** không giẫm chân nhau.

Nguyên tắc bao trùm: **một logic — một chủ sở hữu.** Khi cùng một quy tắc được viết ở hai skill, hai bản đó sẽ trôi xa nhau. Ba tháng sau, bản nào cũng "đúng" và không ai biết bản nào mới. Overlap không phải chuyện thẩm mỹ — nó là nợ kỹ thuật sinh lãi kép.

Phân biệt với `skill-creator`: skill-creator lo **bên trong** một skill (nội dung, description, eval). Skill này lo **giữa** các skill (ai sở hữu logic gì, ai trỏ tới ai). Việc tạo skill mới trong một miền đã có skill cũ thì dùng **cả hai**: skill này chốt ranh giới trước, skill-creator viết nội dung sau.

---

## LUỒNG CHUẨN: "UPGRADE SKILL" → HỆ THỐNG SẠCH

```
[1] Chạy audit tự động          → có danh sách phát hiện, không phán đoán cảm tính (§1)
[2] Phân loại: lỗi kỹ thuật hay lỗi kiến trúc                                  (§2)
[3] Với mỗi overlap → chốt CHỦ SỞ HỮU logic, skill còn lại trỏ tới             (§3)
[4] Sửa description theo công thức 4 phần, luôn có vùng loại trừ               (§4)
[5] Áp dụng thay đổi bằng save_skill (overwrite) — KHÔNG sửa file trên đĩa     (§5)
[6] Chạy lại audit + cập nhật Sổ đăng bạ → phát hiện phải về 0 mức CAO         (§6)
[7] Phát hành qua release.py — mười cổng, trượt cổng nào là không ra file      (§6)
```

Không bỏ bước [1]. Người dùng thường chỉ nhớ một triệu chứng ("skill này không tự chạy"), trong khi audit thường lôi ra 3–4 lỗi nặng hơn mà họ không biết.

---

## 1. Audit trước, phán đoán sau

Ghi script ở Phụ lục A ra file rồi chạy trên thư mục skill. Script bắt 13 lớp lỗi:

| Mã | Lỗi | Mức |
|---|---|---|
| E1 | Frontmatter thiếu / trùng khối / `name` lệch thư mục | CAO |
| E2 | Trỏ tới skill không tồn tại | CAO |
| E3 | Đảo cô lập hoặc đảo một chiều | TRUNG–THẤP |
| E4 | Hai skill trùng **cả tiêu đề lẫn nội dung** một mục | TRUNG |
| E5 | SKILL.md quá khổ (>300 dòng) | TRUNG |
| E6 | Hai description mở đầu gần trùng | TRUNG |
| E7 | Skill nhà nằm ngoài plugin / tồn tại hai bản song song | CAO |
| E8 | Sổ đăng bạ thiếu, thừa, hoặc trùng hàng | CAO |
| E9 | Nguồn plugin lẫn thư mục nháp hoặc `.plugin` cũ | TRUNG–CAO |
| E10 | `description` vượt hoặc sát chuẩn 500 ký tự; **tổng** cả gói > 14.000 ký tự (ngân sách danh sách skill) | CAO–THẤP |
| E11 | Sổ khai báo quan hệ mà SKILL.md không nhắc | TRUNG |
| E12 | `description` thiếu vùng loại trừ "KHÔNG dùng…" | THẤP |
| E13 | Frontmatter không đọc được bằng trình YAML thật / mô tả bị cắt | CAO |
| E14 | File chữ trong skill bị hỏng mã hoá (UTF-8 đọc thành cp1252 — dấu vết ghi bằng PowerShell); BOM chỉ cảnh báo | CAO–THẤP |
| E15 | Sổ đăng bạ thiếu cột `Lớp` / giá trị khác "Quy Trình"·"Vận Hành" (CAO); README đặt skill sai bảng lớp (TRUNG) | CAO–TRUNG |

Chi tiết từng lớp, cách xử lý và lý do chọn ngưỡng: `references/bang-loi.md`.

Đọc kết quả theo mức: **CAO sửa ngay trong phiên này**, TRUNG lên kế hoạch, THẤP ghi nhận.

Script là bộ lọc thô, không phải quan tòa. E4 hay báo giả — hai mục chỉ **trùng tên tiêu đề** ("Quy trình" ≈ "Quy trình 6 bước", "10. Bàn giao" ≈ "5. Bàn giao") trong khi nội dung khác hẳn. Luôn mở cả hai mục ra đọc trước khi kết luận là overlap thật.

**Chính script cũng phải bị nghi ngờ.** Lần chạy đầu tiên trên hệ thống này, script báo 12 lỗi rác vì nó soi cả skill dựng sẵn của Anthropic (docx/pptx/xlsx vốn giống nhau là đương nhiên) và bắt nhầm chuỗi glob `chuan-hoa-du-lieu-*` thành tên skill. Sau khi chạy audit, **đọc từng phát hiện và tự hỏi "cái này có phải lỗi thật không"** trước khi báo cho người dùng — báo cáo đầy tín hiệu giả sẽ khiến lần sau không ai đọc nữa.

**Mẹo khử tín hiệu giả E4:** nếu hai skill bị báo trùng chỉ vì tiêu đề H1 cùng khuôn ("Chuẩn hóa dữ liệu X (SHT)"), đổi tiêu đề cho khác hẳn nhau. Vừa hết báo giả, vừa giúp người đọc phân biệt skill nhanh hơn.

---

## 2. Hai loại lỗi — hai cách chữa khác nhau

**Lỗi kỹ thuật** (E1, E2): sửa được ngay, không cần hỏi ai. Frontmatter trùng thì xóa khối thừa. Tham chiếu gãy thì hoặc gỡ bỏ, hoặc tạo skill còn thiếu — nhưng phải **hỏi người dùng** chọn hướng nào, vì tham chiếu gãy thường là dấu vết của một skill đã lên kế hoạch mà chưa làm.

**Lỗi kiến trúc** (E3, E4, E6): đụng tới ranh giới trách nhiệm. Không tự ý gộp hay tách skill. Trình bày phương án rồi xin quyết định — gộp nhầm hai skill đang chạy tốt gây thiệt hại lớn hơn để nguyên overlap.

---

## 3. Xử lý overlap — chốt chủ sở hữu, đừng xóa mù quáng

Khi hai skill cùng dạy một logic, có đúng bốn lựa chọn:

| Phương án | Dùng khi | Cách làm |
|---|---|---|
| **Chốt chủ sở hữu** (mặc định) | Logic là chung, một skill dùng nó sâu hơn | Giữ bản đầy đủ ở skill sở hữu; skill kia rút còn 1 dòng + trỏ tới: "Quy tắc X: theo `<skill-chủ>` §n" |
| **Nâng lên tầng nền** | ≥3 skill cùng dùng | Tạo một skill nền tảng, cả ba trỏ về |
| **Chuyên biệt hóa** | Nghe giống nhau nhưng khác thật | Đổi tiêu đề cho khác hẳn, ghi rõ điểm khác ngay dòng đầu mục |
| **Giữ nguyên có chủ ý** | Logic ngắn, sống còn, tách ra sẽ bị bỏ qua | Ghi chú `<!-- cố ý lặp với <skill> — đồng bộ khi sửa -->` ở cả hai nơi |

Cấm tuyệt đối: xóa logic ở skill B rồi **không** để lại con trỏ nào. Đó là cách chắc chắn nhất để mất một bước kiểm chứng.

**Chuẩn phân tầng của SHT** — mọi skill phải thuộc đúng một tầng:

- **Tầng 0 — Nền tảng**: quy tắc đúng cho mọi miền (lan truyền hiệu chỉnh, đổi tên hàng loạt an toàn, một-bản-có-hiệu-lực, checklist bàn giao).
- **Tầng 1 — Nghiệp vụ**: dự án, nhân sự, tuyển dụng, CRM, quyết định, xác thực báo cáo. Kế thừa tầng 0 bằng cách **trỏ tới**, không chép lại.
- **Tầng 2 — Định dạng đầu ra**: docx, xlsx, pptx, pdf (skill dựng sẵn). Skill nhà **không** được viết lại kỹ thuật dựng file — chỉ nêu quy ước riêng của SHT (màu, font, thể thức) rồi gọi skill tầng 2.

Nếu một logic tầng 0 đang nằm rải rác ở tầng 1, đó chính là E4 cần nâng lên tầng nền.


**Hai lớp skill** (task-07, v0.33.0 — Mr. Hà phê chuẩn 05/10/2026, `HITL-20261005-013`):
Ngoài trục Tầng (0/1/2), toàn bộ 44 skill chia làm 2 lớp nghiệp vụ trong cùng một plugin:
- **Lớp Quy Trình (20 skill):** cách SHT làm việc với AI và quản trị chính hệ AI (điều phối, cổng duyệt JEV/Triad, kiểm chứng, phát hành, 5 vai AIS48, quy tắc nền, làm rõ yêu cầu). Dùng được cho mọi nghiệp vụ, không gắn cố định một phòng ban.
- **Lớp Vận Hành (24 skill):** nghiệp vụ hằng ngày tạo ra sản phẩm/văn bản cho một miền cụ thể (hợp đồng CNTT/thiết bị, nhân sự/tuyển dụng, CĐS DMI/PRD, hồ sơ scan/văn bản đối tác...).
Quy tắc: Khi tạo skill mới (§8), bắt buộc phải khai báo lớp (`Quy Trình` hoặc `Vận Hành`) vào cột cuối của Sổ đăng bạ. Audit E15 sẽ chặn nếu thiếu hoặc sai lớp.

---

## 4. Sửa trigger — công thức 4 phần

Description là thứ duy nhất model thấy khi quyết định có nạp skill hay không. Viết đủ bốn phần, theo đúng thứ tự:

1. **Làm gì** — động từ + đối tượng cụ thể, không nói chung chung.
2. **Bắt bằng gì** — trích **nguyên văn** cách người dùng hay gõ, kể cả kiểu cộc lốc ("UPGRADE SKILL", "hunt CV").
3. **Bắt cả khi không đúng từ khóa** — mô tả tình huống: "kể cả khi họ không nhắc chữ ...".
4. **Vùng loại trừ** — "KHÔNG dùng skill này khi ...". **Phần bị bỏ quên nhiều nhất, và là thuốc chữa E6 hiệu quả nhất.** Hai skill cùng miền mà đều thiếu vùng loại trừ thì chắc chắn tranh nhau.

Kiểm nhanh: đọc description skill A, hỏi "câu này có mô tả đúng một việc mà skill B cũng nhận không?". Nếu có → thêm vùng loại trừ vào cả hai, đối xứng nhau.

Tránh mở đầu bằng khuôn mẫu dùng chung ("Chuẩn hóa dữ liệu ... của SHT", "Use this skill whenever..."). Sáu từ đầu nên nêu đúng miền riêng biệt.

**Chuẩn SHT: description tối đa 500 ký tự** (05/10/2026, `HITL-20261005-008`; `audit_skills.py` E10 = CAO, `release.py` không đóng gói). `save_skill` chặn ở 1024, nhưng description dài bị harness cắt khi danh sách skill vượt trần → skill mất mô tả, không tự kích hoạt. Bốn phần trên phải nằm gọn trong ngân sách đó — cắt phần liệt kê ví dụ trước, giữ nguyên vùng loại trừ.

---

## 5. Áp dụng thay đổi — chỉ một đường duy nhất

**Sửa file SKILL.md trên đĩa KHÔNG có tác dụng.** Thư mục skill là bản cache chỉ đọc; sửa xong sẽ mất. Đường duy nhất để thay đổi bền vững là `save_skill` với `overwrite: true`.

Hệ quả bắt buộc phải nhớ:

- `save_skill` **thay toàn bộ** SKILL.md. Phải có **trọn vẹn** nội dung mới trước khi gọi — đọc hết file cũ, sửa, rồi ghi lại. Không bao giờ gọi `save_skill` với nội dung rút gọn "cho nhanh", vì phần không viết lại sẽ mất vĩnh viễn.
- Các file khác trong skill (`references/`, `scripts/`) **được giữ nguyên**, nhưng cũng **không thêm/sửa được** qua `save_skill`. Nếu skill cần script, hoặc nhúng thẳng vào SKILL.md, hoặc giao file rời cho người dùng vào thư mục làm việc.
- Skill trên 300 dòng: đọc lại toàn bộ trước khi ghi đè rất tốn. Đây là lý do thật của ngưỡng E5 — skill phình to là skill khó nâng cấp.
- **Ước lượng ngân sách trước khi bắt đầu.** Ghi đè một skill 450 dòng tốn khoảng gấp đôi từng đó cho cả đọc lẫn viết. Nếu context còn ít, **dừng lại và hẹn phiên sau** thay vì ghi đè dở — làm dở nguy hiểm hơn không làm, vì phần chưa viết lại mất luôn.

Trước khi ghi đè một skill dài, sao lưu bản hiện tại ra thư mục làm việc của người dùng để có đường lùi.

---

## 6. Kiểm chứng ngược và Sổ đăng bạ

Sau khi sửa:

1. Chạy lại script audit — mức CAO phải về **0**. Nếu còn, chưa xong.
2. Với mỗi trigger vừa sửa, tự đặt 2 câu gõ thật của người dùng và trả lời: câu này gọi skill nào? Có mơ hồ không?
3. Cập nhật **Sổ đăng bạ** (Phụ lục B) — nguồn sự thật duy nhất về quan hệ giữa các skill. Mỗi lần thêm/sửa/xóa skill, cập nhật **trong cùng phiên**. Sổ lệch thực tế còn nguy hiểm hơn không có sổ.
4. Báo cáo cho người dùng theo đúng ba mục, không dài dòng: **đã sửa gì / còn tồn gì / cần anh quyết gì**.

---

## 7. Bài học đã trả giá

- **Tham chiếu gãy im lặng.** Hai skill từng cùng trỏ tới một skill xác thực báo cáo chưa hề được tạo. Không có lỗi nào báo ra; agent chỉ lặng lẽ bỏ qua bước xác thực số liệu trước khi đưa vào văn bản trình ký. → Mọi tên skill nhắc trong SKILL.md phải kiểm tra tồn tại (E2), và kiểm sau **mỗi** lần sửa.
- **Frontmatter dán đè.** Một skill từng có hai khối YAML liên tiếp do dán chồng khi cập nhật; khối thứ hai chảy vào phần nội dung. Mắt thường đọc lướt không thấy. → Luôn chạy audit sau khi ghi đè, đừng tin cảm giác "vừa dán xong chắc ổn".
- **Checklist bàn giao nhân bản 4 nơi.** Cùng một checklist xuất hiện ở bốn skill với bốn dị bản khác nhau. Không bản nào sai hẳn, nhưng không bản nào đủ. → Đã nâng lên `sht-nen-tang-kiem-chung`; skill nghiệp vụ chỉ giữ mục đặc thù và ghi rõ "chạy sau checklist nền".
- **Phụ lục case study mọc dồn.** Một skill tuyển dụng phình vì mỗi chiến dịch lại thêm một case study đầy đủ vào đuôi. → Case study chỉ giữ lại **quy tắc rút ra**, không giữ diễn biến. Diễn biến để ở tài liệu dự án, không để trong skill.
- **E5 không phải lúc nào cũng sửa được bằng `save_skill`.** Một skill 466 dòng chứa hai phụ lục tra cứu lớn (prompt transcribe 95 dòng, bộ script 68 dòng). Đúng ra phải đẩy sang `references/`, nhưng `save_skill` **không tạo/sửa được file trong `references/`** — mà bản `references/` sẵn có lại cũ và nghèo hơn bản trong SKILL.md, nên trỏ sang đó là làm hỏng. → Cắt được phần trùng tầng 0 (466 → 414 dòng), phần còn lại **chấp nhận vượt ngưỡng có chủ ý** và ghi vào Sổ đăng bạ. Muốn xử lý dứt điểm phải đóng gói skill thành plugin. Bài học: khi E5 không sửa được sạch, **ghi rõ lý do vào sổ** thay vì để nó báo đỏ mãi mà không ai biết vì sao.
- **Audit tự động chỉ đáng tin bằng phạm vi nó soi.** Phiên v0.9.0 có 4 lỗi thật, script bắt được **1**. Ba lỗi lọt (skill nằm ngoài plugin, Sổ đăng bạ trùng hàng, nguồn phát hành lẫn file nháp) đều mang tính cơ học, thừa sức bắt bằng máy — chúng lọt chỉ vì script khi đó chỉ đọc *bên trong* các SKILL.md, còn lỗi lại nằm ở **skill ở đâu**, **sổ có khớp thực tế không**, và **gói chứa gì**. Đã bổ sung E7–E10. Bài học chung: khi một lỗi lọt qua audit, việc đầu tiên không phải sửa lỗi đó mà là hỏi *"vì sao script không thấy?"* và vá phạm vi.
- **Regex dò tham chiếu đừng hardcode tiền tố tên.** Bản cũ chỉ nhận `sht-*`, `chuan-hoa-*`, `quan-tri-*` nên **mù hoàn toàn** với `ra-soat-hop-dong-vendor` — mọi tham chiếu tới nó không được đếm, khiến nó bị báo nhầm là đảo một chiều và một tham chiếu gãy tới nó sẽ không bao giờ bị phát hiện. Nay dò theo **tên thật của skill đang có** cộng mẫu kebab tổng quát.
- **E4 phải so nội dung, không chỉ so tiêu đề.** Ba cảnh báo giả tồn tại suốt nhiều phiên (`"Quy trình" ≈ "Quy trình 6 bước"`) chỉ vì so tên mục. Nay bắt buộc trùng **cả tiêu đề lẫn thân mục**, và **bỏ qua khi cả hai mục đều là con trỏ** về một chủ sở hữu — đó là cách chữa overlap, không phải triệu chứng. Cảnh báo giả kéo dài làm người ta ngừng đọc báo cáo, nguy hiểm không kém bỏ sót.
- **Chuẩn tên chưa nhất quán.** Hệ thống đang tồn tại song song hai tiền tố (`sht-*` và `chuan-hoa-du-lieu-*`). Chuẩn đi tới: `sht-<miền>-<hành động>`. Đổi tên làm gãy mọi tham chiếu chéo, nên **chỉ đổi khi có dịp sửa lớn**, và phải quét lại toàn bộ tham chiếu ngay trong phiên đó.

---

## 8. Khi được yêu cầu tạo skill mới

Trước khi viết một dòng nội dung nào:

0. Tiêu chí mở: việc đã làm với Claude **hơn một lần** theo cùng cách — một lần thì chưa đáng đóng skill. *(thêm 30/09/2026, v0.30.1 — mục THẤP báo cáo gap 30/09)*
1. Liệt kê skill hiện có cùng miền nghiệp vụ.
2. Hỏi: việc này là **skill mới**, hay là **một mục** trong skill đã có? Mặc định nghiêng về mục mới trong skill cũ — hệ thống nhiều skill nhỏ chồng lấn tệ hơn ít skill mạch lạc.
3. Nếu vẫn là skill mới: viết trước **vùng loại trừ** của nó và của các skill hàng xóm, rồi mới viết nội dung. Khai luôn **artifact đầu ra** (file gì, ghi ở đâu) — skill không nói ra được đầu ra là skill chưa rõ việc.
4. Khai báo tầng và lớp (Quy Trình / Vận Hành), cập nhật Sổ đăng bạ, rồi bàn giao cho `skill-creator` viết nội dung.

---

## 9. Quy tắc dừng — khi nào NGỪNG mở rộng lưới kiểm

Skill này dạy cách vá phạm vi khi có lỗi lọt (§1, §7). Mục này dạy điều ngược lại, và cũng quan trọng ngang.

**Chỉ thêm lớp kiểm mới khi một sự cố thật đã gây hậu quả thật. Không thêm vì nghĩ ra được.**

Ca thật: trong một phiên nâng cấp, agent tự thêm **6 lớp kiểm (E7–E12) chỉ trong vài vòng**. Mỗi lớp mới lại tìm ra thêm thứ gì đó, tạo cảm giác hệ thống đang hỏng dần. Thực tế ngược lại — mức độ nghiêm trọng giảm đều, ba vòng cuối chỉ còn phát hiện mức THẤP. Người dùng phải hỏi *"cứ sửa, update và lỗi tiếp ah?"* thì mới dừng.

Bài học: **mở rộng lưới kiểm thì luôn bắt được thêm thứ gì đó — điều đó không chứng minh việc mở rộng là đáng.** Đến một điểm, bộ máy kiểm tốn hơn thứ nó tiết kiệm.

**Ba dấu hiệu đã đến lúc dừng:**

- Hai vòng liên tiếp chỉ còn phát hiện mức THẤP.
- Lớp kiểm mới định thêm chưa từng có sự cố tương ứng, chỉ là "phòng xa".
- Người dùng bắt đầu hỏi vì sao cứ phải sửa nữa. Đây là tín hiệu đáng tin — họ nhìn được chi phí mà agent đang không nhìn thấy.

**Xử lý cảnh báo mức THẤP:** ghi nhận, **không sửa ngay**. Chỉ xử lý khi đằng nào cũng đang mở skill đó ra sửa. Cảnh báo THẤP là báo sớm, không phải việc phải làm.

**Khi báo cáo mức độ hội tụ, đưa bằng chứng bằng số** — mức nghiêm trọng qua từng vòng — chứ đừng khẳng định suông "đang tốt dần".

---

## 9b. Ca kiểm thử hành vi

Audit ở §1 kiểm **hiện vật** — file có đúng cấu trúc không. Nó không kiểm được **hành vi**:
chạy skill trên đầu vào thật thì nó quyết định đúng không.

Mỗi skill giữ ca của mình ở `references/ca-kiem-thu.md`. Khung dùng chung là schema của
`sht-cds-thiet-ke-agent` — cùng bảng SHT bán cho khách Bank/Telco.

**Ba luật:**

1. **Ca chỉ mọc từ sự cố thật.** Mỗi mục mới trong `debug_notes.md` sinh đúng một ca.
   Không thêm ca từ tưởng tượng — đây là §9 áp cho Lớp 3.
   **Nguyên tắc Hashimoto** (rule 00 §3): lỗi lần 1 → ghi `debug_notes.md` + một ca; **lặp lần 2** → nâng thành
   luật trong skill, và nếu kiểm được bằng máy thì thành hook/cổng. *(thêm 30/09/2026, v0.30.0)*
2. **Mỗi ca kiểm hai chiều.** Khi mới viết, chạy hai lần: một lần hành vi đúng (phải đạt),
   một lần hành vi cố tình sai (phải trượt). Ca không trượt được khi đáng trượt thì bỏ.
3. **Người chấm, không phải agent.** Để agent tự chấm agent là bỏ mất chốt độc lập.

**Không phải cổng tự động.** Ca hành vi cần một agent chạy thật, không nhét vào
`release.py` được. Nó là mục bắt buộc trong checklist sửa skill. Ghi rõ điều này để tránh
tình trạng một control được mô tả như tự động nhưng chưa từng chạy.

Skill chưa có sự cố thì file ca kiểm thử **rỗng có chủ ý** — đó là trạng thái đúng.

---

## 10. Rà định kỳ

Tác vụ `audit-skill-sht-hang-tuan` chạy sáng thứ Hai hàng tuần: bộ tự kiểm công cụ → audit 12 lớp → đối chiếu ba phiên bản (nguồn / file `.plugin` / bản đang cài).

**Chỉ 12/13 lớp, không phải 13.** Lệnh trong tác vụ không truyền `--personal`, vì tác vụ tự
động không biết trước thư mục skill cá nhân nằm ở đâu trên máy người dùng. Thiếu
`--personal` thì công cụ tự in *"chưa truyền --personal nên KHÔNG kiểm được E7"* — E7 (skill
nhà nằm ngoài plugin / tồn tại hai bản song song) bị bỏ qua ở lần chạy tuần. Muốn kiểm cả
E7 thì chạy tay: `audit_skills.py skills/ --personal <thư_mục_skill_cá_nhân> --plugin .`

Nguyên tắc của tác vụ đó, giữ nguyên khi sửa nó:

- **Chỉ báo cáo, không tự sửa, không đóng gói lại, không tăng phiên bản.** Nhiệm vụ tuần là phát hiện, không phải khắc phục.
- **Không thêm lớp kiểm mới** — theo §9.
- Sạch thì trả lời **đúng một dòng**. Đây là trường hợp thường gặp nhất; báo dài khiến người ta ngừng đọc.
- Cảnh báo THẤP gộp một dòng, không phân tích.

---

## 11. Tiêu chuẩn cấu trúc Agent & Skill theo SHT-SOP-AI-02

Khi thiết kế, audit hoặc nâng cấp bất kỳ Agent/Skill nào trong hệ sinh thái SHT, bắt buộc đối chiếu với:
👉 `.agents/rules/agent_design_standards.md` (Quy chuẩn Quản trị & Thiết kế 12 Thành Phần của Agent tại SHT - SHT-SOP-AI-02).

**5 Chốt chặn bắt buộc (Non-negotiables):**
1. **Description 4 phần:** (Làm gì + Bắt bằng gì + Bắt cả khi không đúng từ khóa + Vùng loại trừ). Thiếu vùng loại trừ coi như chưa đạt. Độ dài ≤ 500 ký tự (E10).
2. **SKILL.md tinh gọn:** ≤ 300 dòng; mẫu biểu, prompt dài đẩy vào `references/`.
3. **Phân định môi trường:** Rạch ròi giữa Antigravity IDE (`.agents/rules/`, `.agents/scripts/`) và Claude Code CLI (`.claude/settings.json`, `.claude/commands/`, `CLAUDE.md`). Tuyệt đối không khai báo file giả.
4. **Handoff Artifact:** Đặt tên IN HOA, bảng biểu cố định, chốt HITL rõ ràng.
5. **Nguồn sự thật duy nhất:** Đăng ký vào Sổ đăng bạ & Sitemap `AGENTS.md`.

---

# PHỤ LỤC A — SCRIPT AUDIT

Script nằm ở `scripts/audit_skills.py`. Chạy:

```bash
python3 scripts/audit_skills.py skills/ --personal <thư_mục_skill_cá_nhân> --plugin .
```

Thoát mã 1 nếu còn lỗi mức CAO, 0 nếu sạch — dùng được trong scheduled task để rà định kỳ.

Trên Windows, đặt `PYTHONUTF8=1` trước khi chạy, nếu không terminal sẽ hiện tiếng Việt thành ký tự rác.

Khi bổ sung lớp lỗi mới hoặc chỉnh ngưỡng (`OVERSIZE`, `OVERLAP_MIN`), sửa thẳng trong script và ghi lý do vào Sổ đăng bạ — đừng sửa tạm rồi quên.

---

# PHỤ LỤC B — SỔ ĐĂNG BẠ

Sổ nằm ở **`references/so-dang-ba.md`** — nguồn sự thật duy nhất về quan hệ giữa các skill. Đây là **dữ liệu**, không phải logic quyết định, nên tách khỏi thân file theo đúng quy tắc E5.

Mỗi lần thêm/sửa/xóa skill: sửa **hàng có sẵn** trong sổ, không append bảng mới ở cuối; xong thì đếm số hàng phải bằng số thư mục trong `skills/`. `audit_skills.py` đọc sổ ở đó (E8, E11) và tự lùi về đọc trong SKILL.md nếu file kia không có.

## Bộ công cụ trong `scripts/`

| File | Việc | Khi nào chạy |
|---|---|---|
| `audit_skills.py` | Quét 15 lớp lỗi E1–E15 | Bước [1] và [6] của luồng chuẩn |
| `test_audit.py` | **Tự kiểm chính công cụ audit** — 32 ca, mỗi lớp lỗi kiểm hai chiều | Mỗi lần sửa `audit_skills.py`, và tự động ở cổng 1 khi phát hành |
| `release.py` | Mười cổng phát hành rồi mới đóng gói | Mọi lần ra bản mới — thay cho việc nén tay |
| `kiem_dong_bo_ban_cai.py` | So nguồn ↔ Git ↔ tab Code ↔ Cowork (phiên bản + nội dung từng file) và tìm skill cá nhân trùng tên | **Bước cuối mỗi lần phát hành**, sau push + cập nhật tab Code + tải lên tổ chức. Chỉ exit 0 mới được báo "đã phát hành xong" |

```bash
python3 scripts/release.py <thư_mục_gốc_plugin> --personal <skill_cá_nhân> --out <file.plugin>
```

**Vì sao có hai công cụ này, và toàn bộ quy tắc bảo trì plugin** (bản nguồn, số hiệu, đóng gói, vệ sinh nguồn, ba kênh phát hành): `references/phat-hanh-va-cai-dat.md` mục 0. Tóm tắt bắt buộc: sửa ở nguồn plugin rồi đóng gói bằng `release.py` (không `save_skill`, không nén tay); mỗi lần phát hành tăng `version`; kết thúc bằng `kiem_dong_bo_ban_cai.py` exit 0.
