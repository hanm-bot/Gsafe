---
name: sht-ha-tang-va-path-portable
version: 1.0
description: Phát hiện và sửa đường dẫn hardcode theo máy/môi trường cụ thể (path tác giả, ổ đĩa cũ, tên thư mục đã đổi) trong script/hook/skill, chuyển sang tự suy đường dẫn để chạy được trên mọi máy — kiểm bằng cách chạy thật từ thư mục làm việc khác. LUÔN dùng khi một script/skill báo lỗi "không tìm thấy file" dù file rõ ràng có tồn tại, khi mang một gói skill/script sang máy khác thì không chạy, khi vừa đổi tên/di chuyển thư mục dự án, hoặc khi rà thấy chuỗi kiểu "c:\Users\ tên người dùng cụ thể \..." hay "D:\" trong code. KHÔNG dùng để viết skill mới từ đầu, không dùng để kiểm skill có chạy đúng logic nghiệp vụ hay không (dùng sht-qa-kiem-chung-skill-hook) — skill này chỉ lo một việc: đường dẫn có tự trỏ đúng bất kể máy nào không.
---

# Kỹ Sư Hạ Tầng & Path Portable

Vai trò: người dò và vá lỗi "chạy trên máy tôi thì được" (works-on-my-machine) trong script, hook, và skill. Rút từ phiên vá `setup_all_student_skills.py`, `verify_skills.py`, hook `.cjs`, và skill `prd-architect` (20-21/09/2026).

## Dấu hiệu nhận biết path hardcode

- Chuỗi tuyệt đối có tên người dùng cụ thể: `c:\Users\KCCShopVn\...`, `~/.gemini/config/skills/...`
- Ổ đĩa cụ thể không còn đúng sau khi máy/dự án di chuyển: `D:\CHUYỂN ĐỔI SỐ SHT` trong khi máy hiện tại chỉ có ổ `C:` và `G:`
- Tên thư mục cũ còn sót lại sau khi đổi tên: `Tu-Hoc-Tu-Hanh-AI` trong khi thư mục thật đã thành `THỰC HÀNH-AI`
- Script tự copy từ một nguồn ngoài dự án thay vì nhúng nội dung: `src_skills = r"c:\Users\...\Antigravity-Marketing-OS\skills"`

**Quan trọng — hardcode có thể nằm ở 2 tầng khác nhau, phải soát cả hai:**
1. Tầng **cấu hình chạy nó** (vd `~/.claude/settings.json` trỏ tới hook) — dễ thấy.
2. Tầng **logic bên trong chính file đó** (vd một hàm trong `.cjs` tự ghép `path.join(GOC, 'Tu-Hoc-Tu-Hanh-AI', 'docs')`) — dễ bỏ sót vì tưởng chỉ cần sửa cấu hình là đủ.
> *Case:* sửa xong path hook ở `settings.json`, chạy bộ test vẫn có 1 bộ fail — hoá ra logic *thật* của `chan-ban-trung.cjs` (không phải file test) cũng hardcode tên thư mục cũ ở 2 dòng riêng.

## Cách sửa chuẩn — tự suy đường dẫn, không hardcode

**Python/script chạy độc lập:**
```python
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(SCRIPT_DIR, "ten-thu-muc-can-tim")
```

**Skill Claude Code (SKILL.md tự tham chiếu tới file khác của chính nó):**
Không viết cứng `~/.gemini/...` hay `/path/to/...` — mô tả bằng "Base directory for this skill" (giá trị Claude Code tự báo lúc kích hoạt skill), ví dụ:
```
node "<base-dir-của-skill>/scripts/build.mjs" ...
```

**Script Node.js dò gốc dự án theo vị trí file:**
```js
const GOC_DU_AN = path.resolve(__dirname, '..', '..', '..', '..');
```
(đếm đúng số cấp `..` từ vị trí file thật tới gốc — không giả định drive letter.)

## Quy trình chuẩn

1. `grep` toàn diện tìm chuỗi path nghi vấn — không chỉ 1 file, quét **cả cây liên quan** (kể cả file test, lib phụ trợ, tài liệu hướng dẫn có link `file://`).
2. Với mỗi chỗ tìm được: xác định đây là hardcode thật hay chỉ là comment/log — chỉ sửa chỗ ảnh hưởng hành vi.
3. Sửa sang mẫu tự suy đường dẫn (`__file__`-relative hoặc "base directory" runtime).
4. **Nếu không chắc file gốc có đang được phiên khác chỉnh sửa song song** — tạo bản vá tạm trong scratchpad, chạy thử bản vá trước, không sửa trực tiếp file gốc khi còn nghi ngờ.
5. Kiểm bằng cách chạy **từ thư mục làm việc khác** (không phải nơi thường chạy) — loại trừ khả năng script ngầm phụ thuộc `cwd` hiện tại.
6. Chạy lại mọi bộ test liên quan (không chỉ file vừa sửa) để chắc không phá thứ khác.
