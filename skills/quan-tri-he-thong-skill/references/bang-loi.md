# Bảng lớp lỗi E1–E11 — chi tiết

Mở khi cần tra một mã lỗi cụ thể. Phần thân SKILL.md chỉ giữ bảng tóm tắt.

| Mã | Lỗi | Vì sao chết người |
|---|---|---|
| **E1** | Frontmatter thiếu / trùng khối / `name` lệch tên thư mục | Skill không kích hoạt, hoặc khối YAML thừa hiện ra như nội dung |
| **E2** | Trỏ tới một skill **không tồn tại** | Agent được lệnh "dùng thêm skill X" rồi không tìm thấy → âm thầm bỏ qua cả bước kiểm chứng |
| **E3** | Đảo cô lập — không trỏ ai, không ai trỏ tới | Skill sẽ không bao giờ được gọi kèm khi cần dùng chồng |
| **E4** | Hai skill có mục trùng logic | Nguồn sự thật nhân đôi → trôi phiên bản |
| **E5** | SKILL.md quá khổ (>300 dòng) | Phần tra cứu chiếm chỗ phần quyết định; nên đẩy sang `references/` |
| **E6** | Hai description mở đầu gần trùng | Tranh chấp kích hoạt — model chọn nhầm skill |
| **E7** | Skill nhà nằm **ngoài** plugin, hoặc tồn tại đồng thời bản cá nhân lẫn bản plugin | Hai đường bảo trì song song → chắc chắn trôi; bản cá nhân không đi kèm khi chia sẻ plugin |
| **E8** | Sổ đăng bạ lệch thực tế — thiếu hàng, thừa hàng, hoặc **trùng hàng** | Sổ sai còn nguy hiểm hơn không có sổ; hai hàng cùng skill sẽ trôi khác nhau |
| **E9** | Nguồn plugin lẫn thư mục nháp / file `.plugin` cũ | Bản phát hành bọc luôn các bản trước, phình theo cấp số nhân |
| **E10** | `description` vượt hoặc sát trần 1024 ký tự | `save_skill` từ chối thẳng; sát trần thì lần bổ sung tới sẽ vỡ |
| **E11** | Sổ đăng bạ khai báo quan hệ mà SKILL.md không hề nhắc | Sổ mô tả một kiến trúc không tồn tại; người đọc tin vào sơ đồ sai |
| **E12** | `description` thiếu vùng loại trừ | E6 chỉ bắt được khi câu MỞ ĐẦU trùng nên bỏ lọt phần lớn ca tranh chấp kích hoạt thật |

---

## Cách xử lý từng lớp

| Mã | Mức mặc định | Hướng xử lý |
|---|---|---|
| E1 | CAO | Sửa ngay, không cần hỏi ai. Xóa khối frontmatter thừa, sửa `name` cho khớp thư mục. |
| E2 | CAO | Hỏi người dùng: **tạo skill còn thiếu** hay **gỡ tham chiếu**? Tham chiếu gãy thường là dấu vết của một skill đã lên kế hoạch mà chưa làm. |
| E3 | TRUNG / THẤP | Đảo hai chiều: xét xem skill có thừa không. Đảo một chiều: bổ sung con trỏ ngược ở skill liên quan. |
| E4 | TRUNG | Không tự gộp. Chọn một trong bốn phương án ở §3 rồi xin quyết định. |
| E5 | TRUNG / THẤP | Đẩy phần tra cứu sang `references/`. Chỉ làm được khi skill nằm trong plugin — `save_skill` không tạo được file trong `references/`. |
| E6 | TRUNG | Thêm **vùng loại trừ** đối xứng vào description của cả hai skill. |
| E7 | CAO | Đưa skill vào `skills/` của plugin, đóng gói lại, rồi xóa bản cá nhân. Đây là lỗi phía **cài đặt**, không chặn phát hành gói. |
| E8 | CAO | Sửa **hàng có sẵn** trong Sổ, tuyệt đối không append bảng mới ở cuối. Sau khi sửa, đếm số hàng phải bằng số thư mục trong `skills/`. |
| E9 | TRUNG / CAO | Chuyển thư mục nháp ra ngoài nguồn plugin. File `.plugin` cũ nằm trong nguồn là mức CAO — nó làm gói bọc các bản phát hành trước. |
| E10 | CAO / THẤP | Cắt phần liệt kê ví dụ trong description trước, **giữ nguyên vùng loại trừ**. |
| E11 | TRUNG | Hoặc bổ sung con trỏ thật vào SKILL.md, hoặc sửa Sổ cho đúng. Đừng để sổ nói một đằng, skill làm một nẻo. |

---

## Ngưỡng và vì sao chọn số đó

| Hằng số | Giá trị | Lý do |
|---|---|---|
| `OVERSIZE_LINES` | 300 | Trên mức này thì đọc-trọn-rồi-ghi-đè quá tốn, skill thành khó nâng cấp. Báo sớm từ 93% (280 dòng). |
| `OVERLAP_TITLE` | 0.55 | Đủ chặt để bỏ qua tiêu đề chỉ chung chữ đệm. |
| `OVERLAP_BODY` | 0.35 | **Phải vượt cả hai ngưỡng mới báo.** Bản chỉ so tiêu đề từng sinh 3 cảnh báo giả kéo dài nhiều phiên. |
| `DESC_MAX` | 1024 | Giới hạn cứng của `save_skill`, vượt là bị từ chối thẳng. Báo sớm từ 93% (953 ký tự). |

Đổi ngưỡng thì phải chạy lại `test_audit.py` và ghi lý do vào Sổ đăng bạ.

**E12 — xử lý:** thêm câu "KHÔNG dùng skill này khi/cho …" vào cuối description, nêu rõ skill nào mới là chủ. Đây là phần §4 gọi là "bị bỏ quên nhiều nhất". Nếu description đã sát trần 1024 ký tự, cắt phần liệt kê ví dụ trước — **giữ nguyên vùng loại trừ**.
