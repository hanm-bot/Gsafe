# MẪU PRD CHUẨN SHT — điền theo 10 khối

> Điền trực tiếp, xoá phần chú thích *(nghiêng)*. Số liệu chưa đối chiếu gắn ⚠️. Mỗi yêu cầu phải **đo được, nghiệm thu được, truy nguồn được**.

---

## 0. Đầu trang
- **Tên giải pháp / use-case:**
- **Khách hàng / bối cảnh:**  **Ngành:** Bank / Telco / khác
- **Phiên bản PRD:** v___  **Ngày:** ___  **Người soạn:**
- **Trạng thái:** Dự thảo / Trình duyệt / Đã duyệt (Cổng G___)
- **Nguồn Báo cáo hiện trạng (GĐ01):** *(đường dẫn/tên file + ngày)*

## 1. Bối cảnh & vấn đề
*(Trích từ Báo cáo hiện trạng — không viết lại từ đầu. Nêu điểm nghẽn cốt lõi PRD này giải quyết.)*

## 2. Mục tiêu & phi-mục-tiêu
| # | Mục tiêu (đo được) |
|---|---|
| G-01 | |

| # | Phi-mục-tiêu (CỐ Ý không làm lần này) | Vì sao để ngoài |
|---|---|---|
| NG-01 | | |

## 3. Truy vết mục tiêu ↔ điểm nghẽn
| Mã MT | Điểm nghẽn nguồn (GĐ01) | KPI gốc (baseline) | Nguồn số | Mục tiêu To-Be | Giá trị kỳ vọng |
|---|---|---|---|---|---|
| MT-01 | | | | | |

## 4. Quy trình To-Be
| Bước | Ai/cái gì làm | Chế độ (tự động/HITL/thủ công) | Dữ liệu vào → ra | Điểm kiểm soát | Xoá điểm nghẽn As-Is nào |
|---|---|---|---|---|---|
| B1 | | | | | |

*(Kèm sơ đồ mermaid nếu có; đặt As-Is ↔ To-Be cạnh nhau.)*

## 5. User story + tiêu chí nghiệm thu
| Mã | User story ("Là… tôi muốn… để…") | Tiêu chí nghiệm thu (Given/When/Then hoặc danh sách kiểm) | Ưu tiên |
|---|---|---|---|
| US-01 | | | Must/Should/Could |

## 6. Yêu cầu chức năng (FR)
| Mã FR | Mô tả | Trỏ về user story | MoSCoW |
|---|---|---|---|
| FR-01 | | US-01 | Must |

## 7. Yêu cầu phi chức năng (NFR)
*(Điền `checklist-tuan-thu-nd13-nhnn.md` rồi tổng hợp vào đây.)*
| Nhóm | Yêu cầu (số, không tính từ) | Cách nghiệm thu |
|---|---|---|
| Bảo mật & quyền | | |
| Tuân thủ (NĐ13/NHNN) | | |
| Luồng dữ liệu cá nhân | *(đính kèm sơ đồ luồng dữ liệu)* | |
| Hiệu năng & tải (SLA) | | |
| HITL & phê duyệt | | |
| Khả kiểm & rollback | | |

## 8. Đặc tả dữ liệu & tích hợp
| Tích hợp | Hệ nguồn → đích | Có API/webhook? | Dữ liệu trao đổi | Che PII (masking) | Sự kiện/trace |
|---|---|---|---|---|---|
| INT-01 | | | | | |

## 9. Ưu tiên hoá & phạm vi Pilot
- **Tập Must (= phạm vi Pilot):**
- **Nhóm/chi nhánh chạy Pilot:**   **KPI đo trong Pilot:**
- **Cảnh báo:** Pilot đạt ≠ scale đạt vì ___

## 10. Rủi ro, giả định & phụ thuộc
| # | Rủi ro/giả định | Ảnh hưởng | Cách xử lý |
|---|---|---|---|
| R-01 | *(vd: dữ liệu bẩn > 15% ở cổng chặn #3)* | | |

## 11. Hướng thi công & chuyển tiếp
- **Hướng chốt:** AI agent → `sht-cds-thiet-ke-agent` / Luồng-portal-tích hợp → đội build / Còn treo (tiêu chí chốt: ___)
- **Trả lời bằng văn bản:** *"Nếu hệ thống sai cho khách hàng của khách thì ai chịu?"* → ___
