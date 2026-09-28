# Nguồn Tra cứu & Chiến lược Tìm kiếm Căn cứ Pháp lý

> **Mục đích:** Danh bạ cơ sở dữ liệu pháp luật chính thống tại Việt Nam, cú pháp tìm kiếm chuẩn xác và quy trình xác thực hiệu lực văn bản.

---

## 1. Nguồn Cơ sở Dữ liệu Chính thống

### Nhóm 1 — Cơ sở dữ liệu pháp luật quốc gia & Cổng thông tin

| Nguồn CSDL | Tên miền / URL | Đặc điểm dữ liệu | Lưu ý khi tra cứu |
|---|---|---|---|
| **Cơ sở dữ liệu quốc gia về VBQPPL** | vbpl.vn | Cổng chính thống quốc gia, dữ liệu chuẩn xác | Nguồn chuẩn xác định hiệu lực nhưng máy không đọc được (trang dựng bằng JavaScript); dùng vanban.chinhphu.vn, datafiles, congbao |
| **Thư Viện Pháp Luật** | thuvienphapluat.vn | Cập nhật nhanh, có lịch sử hiệu lực, sơ đồ liên kết | Cần kiểm tra chéo văn bản gốc |
| **Luật Việt Nam** | luatvietnam.vn | Giao diện rõ ràng, có tóm tắt điểm mới văn bản | Dùng tham khảo nhanh |
| **Cổng Thông tin điện tử Chính phủ** | chinhphu.vn | Công báo điện tử, văn bản chỉ đạo điều hành | Nguồn ban hành chính thức |

### Nhóm 2 — Cổng thông tin các Bộ, Ngành chuyên môn

| Cơ quan ban hành | Tên miền / URL | Lĩnh vực chuyên trách |
|---|---|---|
| Bộ Tư pháp | moj.gov.vn ⚠️ chưa kiểm URL sau sáp nhập bộ 2025 | Quản lý hệ thống VBQPPL, thi hành pháp luật |
| Tòa án nhân dân tối cao | toaan.gov.vn ⚠️ chưa kiểm URL sau sáp nhập bộ 2025 | Án lệ, nghị quyết của Hội đồng Thẩm phán |
| Bộ Tài chính | mof.gov.vn ⚠️ chưa kiểm URL sau sáp nhập bộ 2025 | Quản lý thuế, phí, lệ phí, tài chính doanh nghiệp |
| Bộ Kế hoạch và Đầu tư | mpi.gov.vn ⚠️ chưa kiểm URL sau sáp nhập bộ 2025 | Doanh nghiệp, đầu tư kinh doanh, đấu thầu |
| Bộ Thông tin và Truyền thông | mic.gov.vn ⚠️ chưa kiểm URL sau sáp nhập bộ 2025 | Công nghệ thông tin, viễn thông, an toàn dữ liệu |
| Bộ Công Thương | moid.gov.vn ⚠️ chưa kiểm URL sau sáp nhập bộ 2025 | Thương mại, thương mại điện tử, dịch vụ logistics |

---

## 2. Cú pháp Tra cứu qua Công cụ `WebSearch`

Trước khi gọi công cụ tra cứu, bắt buộc nạp qua `ToolSearch` (`select:WebSearch,WebFetch`).

### Tìm kiếm văn bản theo từ khóa chính
```
site:thuvienphapluat.vn "[từ khóa nghiệp vụ]" "[năm]"
site:thuvienphapluat.vn "[tên luật]" "điều [X]"
site:thuvienphapluat.vn "[số hiệu văn bản]"
```

### Tìm kiếm văn bản sửa đổi, bổ sung
```
site:thuvienphapluat.vn "sửa đổi" "[số hiệu văn bản gốc]"
site:thuvienphapluat.vn "thay thế" "[số hiệu văn bản gốc]"
site:thuvienphapluat.vn "bãi bỏ" "[số hiệu văn bản gốc]"
```

### Tìm kiếm Nghị định quy định chi tiết
```
site:thuvienphapluat.vn "quy định chi tiết" "[tên luật]" "nghị định"
site:thuvienphapluat.vn "hướng dẫn thi hành" "[số hiệu luật]"
```

### Đọc nội dung văn bản cụ thể qua `WebFetch`
Sau khi `WebSearch` tìm được URL chính thức, dùng `WebFetch` để đọc trực tiếp nội dung điều, khoản cần trích xuất có tọa độ.
**Không lấy nguyên văn từ phần tóm tắt của WebFetch.** Tải file gốc (curl/PDF), trích chữ thô, rồi mới chép — xem `ca-kiem-thu.md` C3.

---

## 3. Quy trình Xác minh Hiệu lực Văn bản

Trước khi đưa bất kỳ điều luật nào vào bảng SOT:
1. **Kiểm tra tình trạng hiệu lực trên banner:**
   - 🟢 Còn hiệu lực: Đủ điều kiện sử dụng.
   - 🟡 Hết hiệu lực một phần: Phải tra cứu xem điều/khoản trích dẫn có nằm trong phần bị sửa đổi không.
   - 🔴 Hết hiệu lực: Không dùng (trừ khi vụ việc phát sinh trước thời điểm hết hiệu lực).
2. **Kiểm tra tab Lịch sử hiệu lực:** Xem ngày ký, ngày có hiệu lực, và danh sách các văn bản sửa đổi/thay thế kèm theo.
3. **Đối chiếu mốc thời gian của vụ việc:** Khớp chính xác ngày xảy ra sự kiện pháp lý với khoảng thời gian văn bản có hiệu lực.

---

## 4. Quy ước Ký hiệu Số hiệu Văn bản

Hiểu cấu trúc số hiệu giúp định danh nhanh cấp văn bản (Ví dụ minh họa giả định):

| Mẫu số hiệu giả định | Cấp văn bản | Cơ quan ban hành |
|---|---|---|
| `00/2099/QH99` | Luật / Nghị quyết | Quốc hội |
| `00/2099/NĐ-CP` | Nghị định | Chính phủ |
| `00/2099/TT-BXD` | Thông tư | Bộ Xây dựng |
| `00/2099/QĐ-TTg` | Quyết định | Thủ tướng Chính phủ |
| `00/2099/QĐ-UBND` | Quyết định | Ủy ban nhân dân cấp tỉnh |

---

## 5. Dấu hiệu Nhận Biết Nguồn Không Đáng Tin Cậy (Red Flags)

- Bài viết trên blog cá nhân, mạng xã hội diễn giải luật mà không kèm số hiệu và tọa độ Điều/Khoản.
- Văn bản trích dẫn không ghi rõ ngày có hiệu lực hoặc không thể kiểm chứng trên Cổng CSDL quốc gia.
- Kết quả tìm kiếm là bài bình luận báo chí mang tính quan điểm thay vì văn bản quy phạm pháp luật gốc.
- Văn bản có định dạng cũ không có thông tin cập nhật tình trạng bãi bỏ hoặc thay thế.
