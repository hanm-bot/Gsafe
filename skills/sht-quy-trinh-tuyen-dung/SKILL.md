---
name: sht-quy-trinh-tuyen-dung
description: "Quy trình tuyển dụng đầu-cuối nội bộ SHT: chuẩn hoá hồ sơ, phỏng vấn ASK, đề xuất đãi ngộ theo 3P/job family, báo cáo Ban lãnh đạo, onboarding 30/60/90. LUÔN dùng khi chạy một đợt tuyển dụng, phân tích phỏng vấn, kế hoạch thử việc. KHÔNG dùng cho săn CV, soạn JD, khảo sát lương (chuan-hoa-du-lieu-tuyen-dung), nhân sự đã tuyển (chuan-hoa-du-lieu-nhansu)."
---

# Quy trình tuyển dụng SHT — đầu đến cuối

Skill này mã hóa quy trình đã kiểm chứng qua thực tế tuyển dụng tại SHT (vị trí CCO, Kỹ sư QS, PM/PO). Mỗi giai đoạn có một file tham chiếu riêng — **chỉ đọc file cần dùng**, không nạp toàn bộ.

## Nguyên tắc xuyên suốt (áp dụng cho mọi giai đoạn)

1. **AI không quyết định tuyển hay loại.** Mọi đầu ra là input hỗ trợ; quyết định thuộc HR + quản lý tuyển dụng + Ban lãnh đạo. Ghi rõ điều này ở cuối mọi báo cáo.
2. **Không dùng yếu tố nhạy cảm để chấm năng lực** (Điều 8 BLLĐ 2019): giới tính, hôn nhân, kế hoạch sinh con, dân tộc, tôn giáo, quê quán, ngoại hình, ảnh, tuổi, sức khỏe không liên quan công việc. Nếu hồ sơ có, loại khỏi phân tích và **nói rõ đã loại**.
3. **Phân biệt 4 loại thông tin**, không trộn lẫn: tự khai · bằng chứng có số liệu · cần xác minh · suy luận của hệ thống.
4. **Tính lại mọi con số từ nguồn gốc.** Tài liệu phái sinh có thể sai đồng loạt vì cùng chép từ một bản tóm tắt lỗi.
5. **Không nêu tên khách hàng trọng yếu** (đối tác ngân hàng) trong tài liệu công khai hoặc tin tuyển dụng.
6. **Mọi kết luận phải truy vết được** về một trang CV, một mốc timestamp, hoặc một tài liệu cụ thể.

---

## Bản đồ 7 giai đoạn

| GĐ | Tên | Dùng khi | File tham chiếu |
|---|---|---|---|
| 1 | Chân dung vị trí & JD | Mở vị trí mới, viết/sửa JD, xây khung năng lực, chốt trọng số ASK | `references/1-chan-dung-jd.md` |
| 2 | Nguồn ứng viên & đăng tuyển | Tìm nguồn CV, đăng tin, xử lý vấn đề nền tảng tuyển dụng | `references/2-nguon-dang-tuyen.md` |
| 3 | Chuẩn hóa hồ sơ | Có CV/hồ sơ/phiếu đánh giá cần sàng lọc, so sánh, chấm điểm | `references/3-chuan-hoa-ho-so.md` |
| 4 | Thiết kế & phân tích phỏng vấn | Soạn câu hỏi, transcribe ghi âm, phân tích transcript, chấm ASK | `references/4-phong-van.md` |
| 5 | Lương & đàm phán | Đề xuất mức lương, benchmark nội bộ, xử lý kỳ vọng ứng viên | `references/5-luong-3p.md` |
| 6 | Báo cáo trình Ban lãnh đạo | Lập báo cáo quyết định, infographic PDF | `references/6-bao-cao-bld.md` |
| 7 | Onboarding & đánh giá | Lộ trình hội nhập, phân công kèm cặp, mốc 30/60/90 ngày | `references/7-onboarding.md` |

**Nếu yêu cầu chạm nhiều giai đoạn, đọc nhiều file.** Ví dụ "review ứng viên này rồi đề xuất lương" → đọc GĐ 3 + GĐ 5.

---

## Xác định giai đoạn từ đầu vào

| Người dùng đưa gì | Giai đoạn |
|---|---|
| Mô tả nhu cầu vị trí, dữ liệu kinh doanh nội bộ | 1 |
| Link tin tuyển dụng, câu hỏi về TopCV/nguồn CV | 2 |
| CV, phiếu đánh giá, bảng so sánh ứng viên | 3 |
| File ghi âm, transcript, yêu cầu bộ câu hỏi | 4 |
| Bảng lương team, con số kỳ vọng của ứng viên | 5 |
| Yêu cầu "trình Ban lãnh đạo", "làm báo cáo", "xuất PDF" | 6 |
| Ứng viên đã nhận việc, hỏi về hội nhập | 7 |

---

## Bốn bẫy đã gặp trong thực tế (kiểm tra ở mọi giai đoạn)

### Bẫy 1 — Nhầm loại tài liệu
Người dùng yêu cầu "review kết quả phỏng vấn" nhưng tài liệu gửi lên là **đánh giá CV trước phỏng vấn**. Luôn phân loại tài liệu TRƯỚC khi phân tích nội dung, và nói ngay nếu lệch với yêu cầu.

### Bẫy 2 — Trùng tên khác ngữ cảnh
Một cái tên có thể xuất hiện ở hai mảng nghiệp vụ hoàn toàn khác nhau trong cùng công ty (một người tên X ở mảng kinh doanh, một người tên X ở mảng kỹ thuật). **Hỏi xác nhận, không suy đoán.**

### Bẫy 3 — Mâu thuẫn giả
Trước khi kết luận ứng viên nói mâu thuẫn, kiểm tra xem có phải **hai khái niệm khác nhau bị gọi bằng từ giống nhau**. Ví dụ *lập dự toán theo định mức nhà nước* (đầu dự án) khác *thanh quyết toán vốn nhà nước* (cuối dự án).

### Bẫy 4 — So sai nhóm đối chiếu
Benchmark lương với người lương cao nhất trong phòng là sai nếu người đó khác job family. Xác định job family trước, so sánh sau.

---

## Checklist trước khi trả bất kỳ kết quả nào

- [ ] Đã xác định đúng giai đoạn và đọc file tham chiếu tương ứng
- [ ] Đã phân loại đúng loại tài liệu, nói rõ nếu lệch với yêu cầu người dùng
- [ ] Đã tính lại số liệu định lượng từ nguồn gốc
- [ ] Đã loại yếu tố nhạy cảm khỏi chấm năng lực và nói rõ đã loại
- [ ] Mỗi kết luận truy vết được về nguồn cụ thể
- [ ] Đã phân biệt: tự khai / bằng chứng số liệu / cần xác minh / suy luận
- [ ] Phần có độ tin cậy thấp đã được đánh dấu và giải thích lý do
- [ ] Con số lương ghi rõ Net hay Gross, đã chốt hay chưa chốt
- [ ] Có câu ghi rõ quyết định cuối thuộc HR + Ban lãnh đạo
