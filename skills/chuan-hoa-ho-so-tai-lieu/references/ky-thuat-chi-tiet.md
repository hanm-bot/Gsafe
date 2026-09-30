# Kỹ thuật chi tiết — chuẩn hoá hồ sơ tài liệu

Tách từ bản skill cá nhân cũ (gộp vào gói ở 0.28.6, 30/09/2026). `SKILL.md` giữ quy tắc; file này giữ lệnh, mẫu chỉ thị và cách làm từng bước. Các ca thật đã được viết lại ẩn danh.

---

## 1. Vệ sinh dữ liệu giữa khách hàng (SKILL.md §0.2)

Khi nhiều thư mục dự án cùng được kết nối, chúng thường thuộc **các khách hàng và end-user khác nhau**. Hồ sơ của dự án A **không được đưa vào phân tích của dự án B**, kể cả khi tài liệu cần tìm tình cờ nằm ở thư mục A.

- Trước khi lấy một file, hỏi: **file này thuộc thư mục của khách hàng nào?** Khác khách hàng đang làm thì dừng lại.
- Nếu tài liệu thực chất thuộc quan hệ đang phân tích nhưng bị lưu nhầm ở thư mục khách khác: **xin bản gốc riêng** rồi dẫn nguồn theo bản đó. Không dẫn sang thư mục của khách khác.
- Quy tắc áp cho **cả phần dẫn nguồn lẫn phần đối chứng** trong báo cáo.
- Trước khi phát hành, **quét dấu vết**:

```bash
for p in "<tên dự án khác>" "<tên thư mục khác>" "<tên đối tác khác>"; do
  c=$(pdftotext bao_cao.pdf - | grep -ci "$p"); [ "$c" -gt 0 ] && echo "⚠ [$c] $p"
done
```

> **Ca thật (ẩn danh).** Cần một phụ lục hợp đồng, tìm thấy nó trong thư mục dự án của một khách khác, lấy ra dùng và dẫn nguồn thẳng vào báo cáo. Chủ đầu tư phải nhắc. Dù văn bản là hợp đồng của chính tổ chức mình (chỉ lưu nhầm chỗ), việc dẫn nguồn sang thư mục khách khác vẫn để lại dấu vết quan hệ chéo trong tài liệu có thể lưu hành.

Quy tắc này là bước kiểm cụ thể của guardrail Context Isolation trong `CLAUDE.md` gốc dự án.

---

## 2. PDF scan tiếng Việt — độ phân giải và mẫu chỉ thị subagent (SKILL.md §1.1)

```bash
pdftoppm -png -r 200 -f 1 -l 20 "file.pdf" pg    # 200 DPI cho văn bản thường
pdftoppm -png -r 450 -f 7 -l 7  "file.pdf" zoom  # 450 DPI khi đọc con số hoặc dấu
```

Trên ~10 trang scan: giao subagent chạy song song, mỗi agent ≤ 20 trang.

Mẫu chỉ thị — các dòng in đậm bắt buộc:

> Đọc file `<đường dẫn>`, phạm vi **trang N đến M**. PDF scan — **đọc trực tiếp từ ảnh, TUYỆT ĐỐI KHÔNG dùng tesseract/OCR**.
> Trích **NGUYÊN VĂN**, không tóm tắt, không diễn giải.
> Với mỗi Điều/Khoản: số hiệu, tiêu đề, chép đủ nội dung. Chép **mọi con số, mọi bảng biểu, đủ từng ô**.
> Với mỗi con số quan trọng: đọc ở 450 DPI và ghi **mức độ chắc chắn** (chắc chắn / hơi mờ / không đọc được).
> **Rà từ khoá** `<liệt kê cụ thể>` — mỗi từ trả lời CÓ/KHÔNG, nếu có thì trích nguyên văn cả câu kèm số trang.
> Ghi rõ: chỗ trống chưa điền, ô ngày để trống, chữ viết tay, con dấu, ký nháy, dấu giáp lai, sửa tay.
> **Ghi rõ trang nào không đọc được — KHÔNG suy đoán.**
> Định dạng: markdown theo thứ tự trang, mỗi phần mở đầu `[Trang N]`.

Kết quả "không xuất hiện lần nào trong 42 trang" thường có giá trị cao hơn nội dung tìm được — vì vậy luôn bắt trả lời CÓ/KHÔNG.

---

## 3. Tên file Unicode tiếng Việt (NFD)

Tên tiếng Việt thường ở dạng NFD, khiến `pdfinfo` báo *No such file* dù `ls` vẫn thấy. Cách lách: để shell tự khớp tên thay vì gõ lại.

```bash
cd "$DIR" && for f in *.pdf; do case "$f" in *"từ khoá"*) pdfinfo "$f";; esac; done
```

Lỗi đường dẫn nói chung (ổ cũ, tên thư mục đã đổi): dùng `sht-ha-tang-va-path-portable`.

---

## 4. So biểu phí giữa hai hợp đồng — quy về một cơ sở (SKILL.md §3.2)

Không so trực tiếp con số với con số: hai biểu phí có thể nằm ở hai vị trí khác nhau trong chuỗi giá trị và **ngược chiều dòng tiền**.

1. **Xác định chiều dòng tiền** của từng hợp đồng: ai trả ai?
2. **Chọn một câu hỏi chung** cho cả hai, ví dụ *"trên mỗi 100 đồng doanh số, bên X giữ lại bao nhiêu?"*
3. **Ánh xạ nhóm ngành theo mã MCC**, không theo tên nhóm — hai hợp đồng thường chia nhóm khác nhau.
4. **Lập bảng đối chiếu theo từng mã MCC**, tính chênh lệch điểm phần trăm.
5. **Nêu rõ nhóm ngành bên mình bất lợi** — đừng chỉ trình phần có lợi.

> **Ca thật (ẩn danh).** Một hợp đồng chia 3 nhóm ngành, hợp đồng kia chia 8. Ánh xạ theo MCC cho thấy có lợi ở phần lớn nhóm nhưng **bất lợi nặng ở 2 nhóm**, vì các MCC đó không nằm trong danh mục ưu đãi của hợp đồng thứ hai. Phát hiện này đổi cả phạm vi khuyến nghị.

---

## 5. Đọc mù kiểm chứng chéo — khi có hai bản in (SKILL.md §4.1)

Cùng một văn bản có **hai bản in khác nhau** (khác Producer, khác lần scan, khác nguồn) là cơ hội kiểm chứng mạnh nhất:

1. Agent thứ nhất đọc bản A.
2. Agent thứ hai đọc bản B, **không được biết kết quả của lần một**.
3. So từng ô bằng script — kết luận lấy từ biến đếm, không gõ sẵn:

```python
lech = 0
for k in A:
    for i, (a, b) in enumerate(zip(A[k], B[k])):
        if a != b:
            print(f"LỆCH {k} cột {i+1}: A={a} B={b}"); lech += 1
print(f"Số ô lệch: {lech}")
```

Đọc mù không chỉ xác nhận mà còn bổ sung: trong ca gốc, lần đọc thứ hai lôi ra hai điểm lần đầu bỏ sót (hai năm khác nhau trong cùng một trang, một bảng thiếu hẳn một cột).

---

## 6. Tài liệu cầm tay cho buổi đàm phán (SKILL.md §5.1)

Bản 1 trang mang vào phòng họp, đúng bảy mục theo thứ tự:

1. **Mục tiêu của vòng này** — nói rõ vòng đầu **không chốt thương mại** nếu còn thiếu số liệu nội bộ.
2. **Kịch bản mở đầu theo bước** — ghi nhận cụ thể → đặt khung → đưa lợi ích của họ trước → sau đó mới nêu đề nghị.
3. **Con số mang vào phòng** — bảng gọn, kèm một câu chốt viết sẵn. Mọi con số phải có nguồn (luật cứng #2).
4. **Tuyệt đối không nói** — danh sách cấm, quan trọng ngang danh sách cần nói.
5. **Thông tin phải lấy được** — câu hỏi đặt cho đối phương, kèm lý do cần.
6. **Câu đối phương sẽ hỏi và trả lời sẵn** — nhất là câu bẫy.
7. **Điều kiện dừng** — câu nói sẵn khi bị ép chốt, và ranh giới không nhượng bộ.

Dòng đầu tài liệu ghi: **"Tài liệu tự dùng, không phát cho đối tác"**.
