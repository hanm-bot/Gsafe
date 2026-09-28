# Hướng dẫn Tra chéo 3 Chiều Văn Bản Pháp Luật

> **Mục đích:** Kỹ thuật trace từ khóa qua các tầng văn bản quy phạm pháp luật, phát hiện văn bản sửa đổi/thay thế, và xác định đúng phiên bản có hiệu lực tại mốc thời gian của vụ việc.

---

## Chiều 1: Tra XUỐNG (Vertical Down)

**Mục đích:** Từ Luật (khung nguyên tắc chung) → tìm Nghị định (quy định chi tiết) → Thông tư (hướng dẫn thực thi cụ thể).

### Cách tra

1. Đọc nội dung Luật → tìm cụm từ "Chính phủ quy định chi tiết" hoặc "Bộ trưởng hướng dẫn thi hành".
2. Tra cứu Nghị định quy định chi tiết:
   ```
   WebSearch: site:thuvienphapluat.vn "quy định chi tiết" "[tên luật]" nghị định
   ```
3. Trong Nghị định → tìm cụm "Bộ trưởng Bộ [X] hướng dẫn" → tra cứu Thông tư:
   ```
   WebSearch: site:thuvienphapluat.vn "hướng dẫn" "[số hiệu NĐ]" thông tư
   ```

### Nhận diện liên kết văn bản
- Mục **"Văn bản được hướng dẫn"** trên cơ sở dữ liệu pháp luật liệt kê Luật/Nghị định mà văn bản này hướng dẫn.
- Phần mở đầu Nghị định luôn nêu: "Căn cứ Luật số... ngày..." → xác nhận mối quan hệ trực tiếp với Luật gốc.

### Mô hình dẫn chiếu hướng dẫn (Ví dụ minh họa giả định)
- `Luật Mẫu 00/2099/QH99 (Khung nguyên tắc)`
  - `→ NĐ 00/2099/NĐ-CP (Quy định chi tiết)`
    - `→ Các Thông tư hướng dẫn chuyên ngành`
*(Chi tiết chuỗi văn bản thực tế đã đối chiếu: xem references/danh-muc-van-ban-goc.md)*

---

## Chiều 2: Tra NGANG (Horizontal — Sửa đổi / Thay thế / Bãi bỏ)

**Mục đích:** Xác định văn bản gốc còn nguyên vẹn hay đã bị sửa đổi, bổ sung. Tuyệt đối không áp dụng văn bản đã hết hiệu lực.

### Cách tra

1. Tra cứu văn bản sửa đổi, thay thế:
   ```
   WebSearch: site:thuvienphapluat.vn "sửa đổi" "[số hiệu VB gốc]"
   WebSearch: site:thuvienphapluat.vn "thay thế" "[số hiệu VB gốc]"
   ```
2. Kiểm tra thông tin hiệu lực:
   - **"Văn bản sửa đổi"**: Liệt kê các văn bản đã sửa đổi văn bản hiện tại.
   - **"Văn bản bị thay thế"**: Văn bản cũ mà văn bản này thay thế hoàn toàn.
   - **"Tình trạng hiệu lực"**: Còn hiệu lực / Hết hiệu lực / Hết hiệu lực một phần.

### Cách đọc văn bản sửa đổi ghép bản hợp nhất
Văn bản sửa đổi thường có cấu trúc:
```
"Điều X. Sửa đổi, bổ sung một số điều của [VB gốc]:
  1. Sửa đổi khoản Y Điều Z như sau: [nội dung mới]
  2. Bổ sung điểm A vào sau điểm B khoản C Điều D"
```
Khi trích dẫn, cần đọc đồng thời: phần giữ nguyên của văn bản gốc + phần sửa đổi trong văn bản mới để trích đúng nội dung có hiệu lực.

*(Chi tiết danh mục văn bản sửa đổi đã đối chiếu: xem references/danh-muc-van-ban-goc.md)*

---

## Chiều 3: Tra THỜI GIAN (Temporal)

**Mục đích:** Xác định chính xác phiên bản văn bản áp dụng tại mốc thời điểm của vụ việc.

### Quy tắc áp dụng

| Mốc thời điểm sự kiện | Quan hệ với ngày hiệu lực VB mới | Nguyên tắc áp dụng |
|---|---|---|
| Trước ngày hiệu lực của VB mới | Mốc sự kiện < Ngày hiệu lực | Áp dụng VB cũ (trừ khi có quy định hồi tố hoặc chuyển tiếp) |
| Sau ngày hiệu lực của VB mới | Mốc sự kiện ≥ Ngày hiệu lực | Áp dụng VB mới |
| Trong giai đoạn chuyển tiếp | Nằm trong khoảng chuyển tiếp | Áp dụng điều khoản chuyển tiếp của VB mới |

### Các bước kiểm tra
1. Xác định mốc thời điểm xảy ra hành vi hoặc thời điểm ký kết hợp đồng.
2. Kiểm tra ngày có hiệu lực thi hành của văn bản trên cơ sở dữ liệu chính thống.
3. Rà soát kỹ **Điều khoản chuyển tiếp** ở các chương cuối của văn bản mới ban hành để xem các quan hệ phát sinh trước đó được xử lý theo quy định nào.

*(Chi tiết các tình huống mẫu: xem references/sot-mau-da-doi-chieu.md)*

---

## Checklist Tra chéo 3 Chiều

Trước khi đưa bất kỳ trích dẫn nào vào bảng SOT:
- [ ] Đã xác định được văn bản gốc (Luật / Bộ luật)?
- [ ] Tra XUỐNG: Đã tìm Nghị định quy định chi tiết và Thông tư hướng dẫn?
- [ ] Tra NGANG: Đã kiểm tra các văn bản sửa đổi, bổ sung hoặc thay thế?
- [ ] Tra THỜI GIAN: Phiên bản trích dẫn đúng mốc thời gian của vụ việc?
- [ ] Đã kiểm tra điều khoản chuyển tiếp?
- [ ] Đã sao chép nguyên văn và ghi tọa độ chính xác kèm URL nguồn?
