# Chuẩn Trích dẫn & Template Bảng Source of Truth (SOT)

> **Mục đích:** Quy định format trích dẫn nguyên văn văn bản quy phạm pháp luật và template bảng Source of Truth (SOT). Trích dẫn chính xác có tọa độ là nền tảng cốt lõi của thẩm định pháp chế.

---

## 1. Format Trích dẫn Đơn lẻ

Mỗi trích dẫn từ văn bản quy phạm pháp luật phải có đủ 4 thành phần:

### Tọa độ pháp lý

```
[Cấp VB] [Số hiệu] – Điều X, Khoản Y, Điểm Z
```

Ví dụ định dạng (dùng số hiệu giả định):
- `Luật 00/2099/QH99 – Điều 36, Khoản 1, Điểm a`
- `NĐ 00/2099/NĐ-CP – Điều 12, Khoản 3`
- `TT 00/2099/TT-BXD – Điều 5`

Quy ước viết tắt cấp VB:
| Viết đầy đủ | Viết tắt |
|---|---|
| Bộ luật | BL |
| Luật | Luật |
| Nghị định | NĐ |
| Thông tư | TT |
| Quyết định | QĐ |
| Nghị quyết | NQ |

### Nguyên văn (Verbatim)

Sao chép chính xác từ nguồn chính thống. Giữ nguyên:
- Dấu câu gốc (dấu chấm, phẩy, hai chấm)
- Chữ hoa / thường
- Số thứ tự (a, b, c hoặc 1, 2, 3)

Nếu đoạn trích dài, chỉ trích phần liên quan trực tiếp và dùng `[...]` để đánh dấu phần lược bỏ.

### Trạng thái hiệu lực

| Trạng thái | Ý nghĩa | Khi nào dùng |
|---|---|---|
| `đang hiệu lực` | VB/điều khoản còn nguyên vẹn, chưa bị sửa đổi, thay thế | VB gốc chưa sửa đổi |
| `đã sửa đổi bởi [VB]` | Nội dung đã thay đổi, cần đối chiếu văn bản sửa đổi | VB gốc bị sửa đổi một phần |
| `hết hiệu lực` | Toàn bộ VB/điều khoản không còn áp dụng | VB bị thay thế hoặc bãi bỏ |
| `chuyển tiếp` | Áp dụng theo điều khoản chuyển tiếp | Giai đoạn chuyển giao giữa luật cũ và mới |

### Ngày hiệu lực

Định dạng: DD/MM/YYYY. Ghi nhận ngày văn bản bắt đầu phát sinh hiệu lực thi hành, không phải ngày ký ban hành.

---

## 2. Template Bảng SOT

Bảng SOT tổng hợp tất cả trích dẫn căn cứ đã thu thập, sắp xếp theo thứ bậc văn bản.

### Format Markdown

```markdown
## Source of Truth (SOT)

**Vấn đề:** [Mô tả vấn đề pháp lý cần giải quyết]
**Mốc thời điểm:** [DD/MM/YYYY]
**Lĩnh vực:** [Tên lĩnh vực chuyên ngành]

| # | Tọa độ pháp lý | Trích dẫn nguyên văn | Trạng thái | Hiệu lực | URL nguồn + ngày truy cập | Vai trò |
|---|---|---|---|---|---|---|
| 1 | [Cấp] [Số hiệu] – Đ.X, K.Y | "[copy nguyên văn]" | [trạng thái] | [DD/MM/YYYY] | [URL] (truy cập DD/MM/YYYY) | [vai trò trong vấn đề] |
| 2 | ... | ... | ... | ... | ... | ... |

### Xung đột (nếu có)
⚠️ Trích dẫn #X và #Y mâu thuẫn về [nội dung]. 
Áp dụng [lex superior / posterior / specialis] → ưu tiên #[X/Y].
Lý do: [giải thích nguyên tắc áp dụng].
```

### Cột "Vai trò"

Ghi ngắn gọn trích dẫn này đóng vai trò gì trong vấn đề đang phân tích:
- "Quy định điều kiện [X]"
- "Xác định thẩm quyền [cơ quan]"
- "Quy định thời hạn [Y ngày]"
- "Chế tài xử lý vi phạm"
- "Sửa đổi, bổ sung điều kiện tại #[trích dẫn gốc]"

---

## 3. Ví dụ SOT Hoàn chỉnh Đã Đối Chiếu

Ví dụ đã đối chiếu: xem references/sot-mau-da-doi-chieu.md.

---

## 4. Lỗi Trích dẫn Phổ biến (Cần Tránh)

| Lỗi | Nguyên nhân sai lệch | Cách xử lý đúng chuẩn |
|---|---|---|
| Diễn giải thay vì copy nguyên văn | Làm sai lệch chi tiết và câu từ định lượng của luật | Sao chép nguyên văn, dùng `[...]` nếu văn bản dài |
| Thiếu Khoản / Điểm | Một Điều luật có nhiều Khoản với hệ quả pháp lý khác nhau | Ghi đủ tọa độ cấp sâu nhất: Điều – Khoản – Điểm |
| Không ghi trạng thái hiệu lực | Nguy cơ áp dụng văn bản đã bị sửa đổi hoặc bãi bỏ | Luôn tra cứu và ghi rõ trạng thái hiệu lực tại mốc thời gian |
| Nhầm ngày ban hành và ngày hiệu lực | Nhiều văn bản ban hành trước nhưng hiệu lực sau nhiều tháng | Luôn ghi ngày phát sinh hiệu lực thực tế |
| Thiếu URL nguồn và ngày truy cập | Không thể kiểm chứng tính nguyên bản và thời điểm xác thực | Bắt buộc ghi URL nguồn chính thống kèm ngày truy cập |
