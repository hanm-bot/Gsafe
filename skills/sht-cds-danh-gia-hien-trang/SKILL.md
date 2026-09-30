---
name: "sht-cds-danh-gia-hien-trang"
description: "Đánh giá hiện trạng CĐS (DMI) Giai đoạn 01 và lập Chiến lược – Lộ trình Giai đoạn 02 SHT: 6 trụ cột, dữ liệu, API, điểm nghẽn As-Is, cổng G1; rồi 6 lăng kính thị trường B2B, backlog use-case, business case sơ bộ. LUÔN dùng khi nói \"đánh giá hiện trạng\", \"khảo sát DMI\", \"tìm điểm nghẽn\", \"lập chiến lược CĐS\", \"backlog use-case\", \"6 lăng kính\". KHÔNG dùng cho PRD/giải pháp (sht-cds-thiet-ke-prd), rà hợp đồng vendor, chuẩn hoá CRM (sht-normalize-account)."
---

# Đánh giá Hiện trạng & Chiến lược Chuyển đổi số (SHT Phase 01 → 02)

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

Vượt G1 xong, **không dừng ở báo cáo hiện trạng** và **không nhảy thẳng sang 03**: làm Giai đoạn 02 ở §6 trước (luật cứng #4 đòi đủ đầu ra 01 **và** 02). Sau 02, bảng điểm nghẽn As-Is cùng backlog use-case đã xếp ưu tiên là **đầu vào cho `sht-cds-thiet-ke-prd`** (Giai đoạn 03): thiết kế quy trình To-Be và soạn PRD cho giải pháp — tài liệu yêu cầu trung lập mà mọi hướng thi công đều đọc. Chỉ **khi PRD đã chốt hướng thi công là AI agent** mới chuyển tiếp sang `sht-cds-thiet-ke-agent` để khai báo agent đủ 3 chiều, gán tầng confidence và chốt mức Tiered Governance trước khi đề xuất cho khách Bank/Telco.

Không đề xuất một use-case AI nào khi chưa qua Giai đoạn 01 — thiếu bản đồ As-Is thì không chứng minh được agent giải quyết điểm nghẽn nào, và không có KPI gốc để đo cải thiện.

## 6. Giai đoạn 02 — Chiến lược & Lộ trình *(thêm 30/09/2026, v0.29.0 — báo cáo gap `THỰC HÀNH-AI/04_Kiem-Chung-Upgrade/2026-09-30_GAP-sht-skills-vs-tai-lieu-hoc.md`)*

**Điều kiện vào:** workspace đã có đầu ra 01 và đã qua G1. Chưa có → dừng, làm §3 trước. Không workspace nào có đầu ra 01 thì **hỏi**, không tự dựng giả định.

Giai đoạn 02 trả lời "làm gì trước, vì sao, có đáng tiền không" — **không** thiết kế giải pháp (việc của 03).

1. **Chọn và xếp ưu tiên hướng triển khai bằng 6 lăng kính** — `references/khung-6-lang-kinh.md` (L1 nhu cầu cấp bách · L2 ba lực · L3 khoảng trống quy trình · L4 lợi thế bền vững · L5 đe doạ/đòn bẩy AI · L6 kinh tế đơn vị). Mỗi lăng kính lấy đầu vào **từ đầu ra 01**, ghi vào đúng sheet của workbook 02.
2. **Điền workbook 6 sheet** (`.agents/knowledge/02_Chien-luoc-Lo-trinh/02_noi-dung.md`): MV-GSM · BMC · SWOT/PEST/USP/UVP · Mục tiêu–KPI theo 3 trụ · Backlog use-case (chấm giá trị/khả thi) · Business case & ROI sơ bộ.
3. **Backlog use-case:** mỗi dòng phải map về ít nhất một trụ (Tài chính / Khách hàng / Hệ thống) — không map được thì loại. Với khách ngân hàng, gom nhóm theo 3 cụm: gian lận/rủi ro · khách hàng · vận hành.
4. **Business case:** chi phí AI biến đổi theo lượng dùng (token/lượt gọi), không tính như license phẳng — xem `sht-cds-thiet-ke-agent` §8. Mọi con số qua luật cứng #2 (truy được nguồn hoặc gắn "chưa đối chiếu"). Không dùng số minh hoạ của tài liệu gốc AI48S.
5. **Căn cứ pháp lý của lực cấu trúc (L2)** lấy qua `sht-phap-che-sot`, không tự khẳng định hiệu lực luật.
6. **Cổng ra 02:** backlog đã xếp ưu tiên + business case sơ bộ được Sponsor duyệt (HITL). Có rồi mới sang `sht-cds-thiet-ke-prd`.

Không dùng khung này để "bán ý tưởng" trước khi có 01 — đó chính là lỗi luật #4 chặn. L7 (kiểm chứng 0-code) và L8 (marketing) của bản gốc bị bỏ có chủ ý: kiểm chứng với khách Bank/Telco là Pilot Giai đoạn 04.
