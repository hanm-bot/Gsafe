---
name: "sht-cds-danh-gia-hien-trang"
description: >-
  Đánh giá hiện trạng và mức độ sẵn sàng chuyển đổi số (Digital Maturity Index — DMI) cho doanh nghiệp B2B theo Giai đoạn 01 phương pháp luận SHT/Vietduc AI — khảo sát 6 trụ cột, kiểm toán chất lượng dữ liệu 6 chiều, rà soát hạ tầng API/webhook, lập bản đồ điểm nghẽn quy trình As-Is, lập Báo cáo Hiện trạng trước Cổng kiểm soát G1.
  LUÔN dùng khi người dùng nói "đánh giá hiện trạng CĐS", "khảo sát DMI", "đo maturity", "tính điểm DMI", "tìm điểm nghẽn quy trình", hoặc chuẩn bị tư vấn lộ trình CĐS.
  Xong Giai đoạn 01 thì chuyển sang sht-cds-thiet-ke-agent; xuất báo cáo và bàn giao theo sht-nen-tang-kiem-chung.
  KHÔNG dùng cho rà soát hợp đồng vendor (dùng ra-soat-hop-dong-vendor), chuẩn hóa account CRM (dùng sht-normalize-account), hay bóc tách hồ sơ scan (dùng chuan-hoa-ho-so-tai-lieu).

---

# Đánh giá Hiện trạng & Sẵn sàng Chuyển đổi số (SHT Phase 01)

## 1. Mục tiêu & Nguyên lý Đánh giá Hiện trạng
"Không giải pháp nếu chưa chẩn đoán". Trước khi tư vấn công cụ AI hay tự động hóa, doanh nghiệp bắt buộc phải đi qua Giai đoạn 01 để đo lường năng lực thực tế, phát hiện rác dữ liệu và xác định điểm nghẽn quy trình. Bỏ qua bước này sẽ dẫn đến tình trạng "tự động hóa cái lộn xộn" và gây lãng phí ngân sách.

Skill này kế thừa toàn bộ quy tắc nền tảng từ `sht-nen-tang-kiem-chung` (lan truyền hiệu chỉnh, một bản có hiệu lực, đo lường trước khi kết luận, kết xuất báo cáo theo người đọc).

## 2. Ba nguyên tắc BẮT BUỘC của Đánh giá Hiện trạng
1. **Chấm điểm phải có bằng chứng cụ thể:** Không ước lượng cảm tính. Mỗi điểm số từ 1.0 - 5.0 phải gắn với dữ liệu kiểm toán, ảnh chụp màn hình hoặc kết quả phỏng vấn.
2. **Kiểm toán dữ liệu trước khi vẽ giải pháp:** Phải đo tỷ lệ lỗi ở 6 chiều (Đầy đủ, Chính xác, Nhất quán, Kịp thời, Duy nhất, Hợp lệ). Dữ liệu rác > 15% phải lên kế hoạch làm sạch trước.
3. **Điểm nghẽn phải gắn với thiệt hại kinh tế:** Mô tả điểm nghẽn phải kèm thời lượng (phút/ngày) hoặc tỷ lệ sai sót (%) để làm căn cứ tính ROI ở các bước sau.

## 3. Quy trình Đánh giá 4 bước (DMI & As-Is)

### Bước 1: Khảo sát & Chấm điểm 6 Trụ cột (DMI)
- Đọc thang điểm chuẩn tại `references/khung-danh-gia-6-tru-cot.md`.
- Thu thập điểm số 6 trụ cột từ bảng khảo sát: `van_hoa`, `du_lieu`, `cong_nghe`, `quy_trinh`, `con_nguoi`, `khach_hang`.
- Gọi script tính toán:
```python
import sys; sys.path.append("scripts")
from calculate_readiness import calculate_dmi
dmi_score, level_label, gaps = calculate_dmi(scores)
```

### Bước 2: Kiểm toán Dữ liệu & Khảo sát Hạ tầng
- Tra cứu tiêu chí tại `references/kiem-toan-du-lieu-ha-tang.md`.
- Lập bảng danh mục hệ thống hiện tại (KiotViet, myXteam, CRM, Zalo OA, Sheets...).
- Ghi nhận: Có API/Webhook không? Ai giữ Super Admin? Rủi ro Single Point of Failure ở đâu?

### Bước 3: Bản đồ Quy trình As-Is & Định vị Điểm nghẽn
- Chọn 3-5 quy trình lõi (Tiếp nhận Lead, Xử lý đơn, Quản lý kho, Chăm sóc sau bán).
- Liệt kê các bước: Ai làm, công cụ gì, mất bao lâu, thao tác tay hay tự động?
- Xác định điểm nghẽn có mức độ lãng phí thời gian và tỷ lệ sai sót cao nhất.

### Bước 4: Lập Báo cáo Hiện trạng & Thẩm định Cổng G1
- Tổng hợp thành Báo cáo Hiện trạng theo chuẩn `sht-nen-tang-kiem-chung` §6:
  - **Bản Điều hành (1-2 trang):** Điểm DMI tổng thể & Radar khoảng cách, Top 3 rủi ro dữ liệu / hạ tầng cần xử lý ngay, Top 3 điểm nghẽn quy trình mang lại cơ hội Quick-Win.
  - **Bản Chi tiết Kỹ thuật:** Bảng ma trận 6 trụ cột kèm bằng chứng, danh mục hệ thống API, và bảng phân tích As-Is.
- Xin phê duyệt của Ban Lãnh đạo (Sponsor) để vượt Cổng kiểm soát G1 trước khi bước sang Giai đoạn 02.

## 4. Đầu ra kỳ vọng & Deliverable
1. **Bảng điểm DMI:** Điểm số (1.0 - 5.0), Phân cấp trưởng thành số, Khoảng cách từng trụ cột so với chuẩn Doanh nghiệp (Level 4).
2. **Ma trận Hệ thống & Dữ liệu:** Danh mục phần mềm, tình trạng API/Webhook, tỷ lệ lỗi dữ liệu 6 chiều.
3. **Bảng phân tích Điểm nghẽn:** Danh sách các bước lãng phí thao tác tay kèm KPI tác động kỳ vọng (thời gian tiết kiệm, tỷ lệ lỗi giảm).

## 5. Bước tiếp theo sau Cổng G1

Vượt G1 xong, **không dừng ở báo cáo hiện trạng**. Bảng điểm nghẽn As-Is ở Bước 3 chính là **đầu vào cho `sht-cds-thiet-ke-prd`** (Giai đoạn 03): thiết kế quy trình To-Be và soạn PRD cho giải pháp — tài liệu yêu cầu trung lập mà mọi hướng thi công đều đọc. Chỉ **khi PRD đã chốt hướng thi công là AI agent** mới chuyển tiếp sang `sht-cds-thiet-ke-agent` để khai báo agent đủ 3 chiều, gán tầng confidence và chốt mức Tiered Governance trước khi đề xuất cho khách Bank/Telco.

Không đề xuất một use-case AI nào khi chưa qua Giai đoạn 01 — thiếu bản đồ As-Is thì không chứng minh được agent giải quyết điểm nghẽn nào, và không có KPI gốc để đo cải thiện.
