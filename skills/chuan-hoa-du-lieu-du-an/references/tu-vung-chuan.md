# Từ vựng chuẩn hóa

Cập nhật danh sách này khi có thông tin mới từ người dùng. Khi gặp tên/thuật ngữ chưa có ở đây, **hỏi trước khi tự chuẩn hóa**.

---

## 1. Vai trò & nhân sự

Phân biệt người trùng tên là bắt buộc — gộp nhầm sẽ gán sai phát ngôn và sai trách nhiệm trong biên bản.

| Tên | Vai trò | Ghi chú |
|---|---|---|
| Nguyễn Mạnh Hà | Chủ tịch / chủ trì họp | Xưng hô trong văn bản: **Anh Hà**. Dòng chữ ký: **chỉ ghi họ tên**, không có "Anh" |
| Thanh Huyền | COO | **Khác** Khánh Huyền |
| Khánh Huyền | BA lead (Chuyển đổi số) | **Khác** Thanh Huyền |
| Chiến | GĐ Ban QLDA | Cũng là người tự phát triển App QLDA |
| Việt | AM — được giao điều hành Ban QLDA | |
| Phương | AM / kinh doanh chi nhánh | Coi chừng trùng "phương pháp", "phương án" |
| An | AM | Coi chừng trùng "an toàn", "an ninh" |
| Tuấn | AM (tham gia từ xa) | |
| Nguyên | Phó ban QLDA — kiến trúc/nội thất/giám sát | Coi chừng trùng "Thái Nguyên", "nguyên tắc", "nguyên nhân" |
| Ngọc | QS / dự toán | |
| Thảo | QS đầu ra / hồ sơ | Coi chừng trùng "thảo luận" |
| Khoa | IT / thiết bị phần cứng | Coi chừng trùng "khoa học" |
| Thúy | Đầu mối tạo cơ hội (bên ngoài) | **Giữ nguyên "bạn Thúy"** — không đổi thành "chị Thúy" |

**Quy ước xưng hô trong văn bản:** `Anh <tên>` / `Chị <tên>`. Ngoại lệ: dòng chữ ký cuối văn bản hành chính chỉ ghi họ tên đầy đủ.

### Squad PCCV (dự án thi công)

| Mã | Vai trò |
|---|---|
| CHT | Chỉ huy trưởng — hiện trường, biện pháp, an ninh ra/vào |
| QS-ĐR | QS Đầu ra — đầu mối **duy nhất** với CĐT về HĐ, dòng tiền (One Voice) |
| QS-ĐV | QS Đầu vào — khối lượng, đơn giá, HĐ nhà thầu phụ |
| AM | Account Manager — CSKH |
| ĐP | Điều phối — hồ sơ, pháp lý |
| NTP | Nhà thầu phụ — **nghiêm cấm** làm việc trực tiếp với CĐT |

---

## 2. Mã dự án

Dùng tiền tố nhất quán cho dự án VietinBank:

- `VTB Hà Giang`
- `VTB Đông Hà Nội`
- `VTB Thái Nguyên`
- `VTB Yên Bái`
- `VTB CN Thủ Thiêm`
- `VTB PGD Tây Nha Trang`

Dự án ngân hàng khác giữ tên gốc: `ABBank Ngô Quyền`, `ABBank Hội sở`, `PGD 31B Sơn Tây`...

**Nguyên tắc:** mã dự án nghiệp vụ thống nhất là khóa liên kết giữa các hệ thống (Base ↔ App QLDA ↔ file theo dõi). Không gom nhiều điểm thi công vào một tên chung — mỗi điểm có tiến độ và AM riêng.

---

## 3. Từ vựng trạng thái hồ sơ

Thang bậc chuẩn, thể hiện rõ mức độ sẵn sàng:

```
Chưa có → Đang làm → Đã gửi CĐT → CĐT đã nhận → Đã ký / Đã có → (N/A)
```

| Trạng thái | Ý nghĩa | Tính là hoàn tất? |
|---|---|---|
| Chưa có | Chưa bắt đầu | Không |
| Đang làm | Đang chuẩn bị | Không |
| Đã gửi CĐT | Đã gửi đi, **chưa xác nhận nhận** | Không |
| CĐT đã nhận | CĐT xác nhận đã nhận bản cứng/mềm | Có (nhưng chưa ký) |
| Đã ký / Đã có | Có văn bản ký hoặc tài liệu hoàn chỉnh | Có |

**Cảnh báo bắt buộc:** "CĐT đã nhận" ≠ "đã ký" ≠ "đã thu tiền". Khi checklist đạt 100% "CĐT đã nhận", vẫn phải nêu rõ điều kiện kích hoạt thanh toán **chưa đủ** — thường còn thiếu biên bản có chữ ký và hóa đơn.

Mỗi lần chuyển trạng thái phải kèm **cột ngày**.

---

## 4. Từ vựng trạng thái tiến độ

Tự động theo % hoàn thành và ngày chốt số liệu:

```
Chưa bắt đầu · Chưa BĐ – TRỄ · Đang làm · Đang làm – TRỄ · Hoàn thành
```

Loại dòng trong bảng tiến độ: `Nhóm` · `Công việc` · `Cổng duyệt` · `Mốc`

---

## 5. Cụm bảo vệ khi đổi tên hàng loạt

Nạp danh sách này vào `protect` của `scripts/safe_rename.py`:

```json
[
  "Hà Giang", "Đông Hà Nội", "Thái Nguyên", "Yên Bái", "Hà Nội",
  "Việt Nam", "Ninh Thuận", "Bạc Liêu", "Bắc Thăng Long", "Ba Vì",
  "Sơn Tây", "Thủ Thiêm", "Nha Trang", "Vĩnh Hải",
  "phương pháp", "phương án", "phương tiện",
  "an toàn", "an ninh", "phương án kinh doanh",
  "khoa học", "nguyên tắc", "nguyên nhân", "nguyên vật liệu",
  "thảo luận", "chiến lược", "bạn Thúy"
]
```

Danh sách này **không đầy đủ** — luôn chạy `--dry-run` và đọc ngữ cảnh trước khi áp dụng.
