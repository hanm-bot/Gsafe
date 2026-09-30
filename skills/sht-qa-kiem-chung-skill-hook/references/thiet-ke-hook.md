# Thiết kế hook cưỡng chế SHT

*(thêm 30/09/2026, v0.30.0 — báo cáo gap `THỰC HÀNH-AI/04_Kiem-Chung-Upgrade/2026-09-30_GAP-sht-skills-vs-tai-lieu-hoc.md`)*

Nguồn gốc: `THỰC HÀNH-AI/.agents/rules/03_cuong-che-luat-bang-hook.md` §3.8, §4, §5 — bản đầy đủ kèm ca thật nằm ở đó; file này là bản rút gọn để skill mang theo được. Kiểm hook có sống không: `SKILL.md` kỹ thuật 7–8.

## 1. Chọn bậc cưỡng chế — thang leo

`CLAUDE.md` (nhắc) → `.agents/rules/` (giải thích) → `permissions.deny` (chặn theo tên lệnh / mẫu đường dẫn tĩnh) → **hook** (chặn theo điều kiện trạng thái).

- Luật chặn được bằng **tên lệnh hoặc đường dẫn tĩnh** → `permissions.deny`.
- Luật phụ thuộc **trạng thái** (file đã tồn tại chưa, giai đoạn trước xong chưa, nội dung có nguồn chưa) → **bắt buộc hook**. Ca luật #3: `deny Write(./_archive/**)` chặn luôn việc `mv` vào `_archive/` mà luật ra lệnh phải làm; phải chuyển sang hook chỉ chặn ghi đè file **đã tồn tại**.
- `Edit`-deny **cũng chặn tạo mới và di chuyển vào** — đọc tên luật rồi suy hành vi là đoán; thử thật rồi mới kết luận.
- `permissions` cấp project chỉ nạp từ **gốc dự án**; thêm deny mới phải thêm ở cả `.claude/settings.json` gốc và `THỰC HÀNH-AI/.claude/settings.json`.
- **Agent không tự nới `settings.json`.** Quy trình: dựng lớp thay thế → kiểm chứng chạy thật → xin người tháo lớp cũ.
- Trước khi đặt điều kiện mới cho chốt, **đọc lại câu luật** tìm mệnh đề giới hạn có sẵn (ví dụ luật #4 "áp cho tài liệu bán khách").

## 2. Tám nguyên tắc

1. **Bọc chống sập** — toàn thân hook trong `try/catch`; hook lỗi không được làm chết phiên.
2. **Công tắc riêng từng hook** — tắt độc lập qua file cấu hình, không sửa `settings.json`.
3. **Exit code:** `0` cho qua · `2` chặn.
4. **Tách logic lõi** ra module riêng để viết được ca kiểm thử.
5. **Có đường thoát có kiểm soát** (nhãn ⚠️, `DA-DOI-CHIEU-NGUON`…) — chặn tuyệt đối đẻ ra hành vi lách.
6. **Im lặng khi không có việc** — hook không liên quan thoát ngay, không in gì.
7. **Cấm `\b` trong mẫu có tiếng Việt — tuyệt đối, kể cả trước chuỗi ASCII.** `\b` của JS chỉ hiểu ASCII: `/\bđã/.test(' đã')` → `false`. Dùng lookbehind Unicode + cờ `u`: `(?<![\p{L}\p{N}_])`.
8. **Ca kiểm thử soi cấu trúc mẫu**, không chỉ hành vi: mọi mẫu có cờ `u`, không mẫu nào chứa `\b` — và ca phải phủ **MỌI mẫu trong file**, không chỉ mẫu vừa sửa. Ca phủ thiếu tệ hơn không có.

Thêm: không đọc được đối tượng (workspace, file) thì fail-open nhưng ghi mã riêng kiểu `khong-doc-duoc-*` vào nhật ký, **không** ghi thành `qua`.

## 3. Môi trường chạy

- Lệnh hook dùng **đường dẫn tuyệt đối tới runtime** (node.exe, python.exe). App desktop giữ PATH chụp lúc Explorer khởi động; cài runtime xong terminal thấy mà app không thấy.
- Đặt hook ở `~/.claude/settings.json` (cấp user), tự giới hạn phạm vi bằng khoá kiểu `thuMucBaoVe`. Phạm vi xét theo `cwd` của phiên, nên file ghi ra ngoài cây vẫn bị soi — fail-safe, không phải lỗi.
- Test bằng chính chuỗi lệnh trong `settings.json` qua `cmd /c` với stdin giả; chắc nhất là thử vi phạm thật trong phiên.
- Nhận diện định danh (CCCD, MST…) theo **cấu trúc thật** của nó, không nới ngưỡng và không chỉ dựa từ khoá ngữ cảnh — xem `sht-quan-tri-dn` §0.
