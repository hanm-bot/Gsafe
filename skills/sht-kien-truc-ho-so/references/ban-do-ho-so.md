# Bản đồ hồ sơ tham chiếu theo pha H1–H5

> Điểm xuất phát để đồng thiết kế — không phải danh sách cứng. Cột "Bắt buộc" do người dùng xác nhận cho từng hồ sơ cụ thể.

## 1. Ba nghiệp vụ gốc (từ tài liệu lớp AI48S — vietduc·ai)

| Pha | A. Đề tài nghiên cứu | B. Dự án kinh doanh / đầu tư | C. Mua sắm thiết bị / CNTT |
|---|---|---|---|
| **H1 Khởi tạo** | Đề cương sơ bộ; Phiếu đăng ký đề tài | Tờ trình chủ trương đầu tư; Phiếu đề xuất dự án | Phiếu đề xuất mua sắm; BB kiểm tra hiện trạng thiết bị cũ |
| **H2 Thẩm định** | Tổng quan tài liệu; Dự toán kinh phí | Báo cáo nghiên cứu khả thi (FS); Dự toán tài chính & dòng tiền | Bảng so sánh báo giá (≥ 3 đơn vị); Dự toán tổng hợp |
| **H3 Pháp lý** | QĐ phê duyệt đề tài; BB họp Hội đồng xét duyệt; Hợp đồng NCKH | QĐ phê duyệt dự án; BB họp HĐQT/BGĐ; Hợp đồng kinh tế | Tờ trình phê duyệt kinh phí; QĐ chỉ định/chào hàng; Hợp đồng mua bán |
| **H4 Vận hành** | Phiếu khảo sát / dữ liệu thô; Báo cáo tiến độ | SOP dự án; Dashboard KPI tuần | Kế hoạch bàn giao & lắp đặt; Nhật ký bàn giao kỹ thuật |
| **H5 Nghiệm thu** | Báo cáo toàn văn; Tóm tắt; Slide bảo vệ | BB nghiệm thu; Báo cáo quyết toán; Slide tổng kết | BB bàn giao & nghiệm thu; Hồ sơ bảo hành & thanh quyết toán |

## 2. Hai nghiệp vụ riêng của SHT

### D. Dự án CĐS bán cho khách Bank/Telco (ánh xạ 11 giai đoạn 00–10)

| Pha | Giai đoạn CĐS | Tài liệu điển hình | Skill SHT |
|---|---|---|---|
| H1 | 00 | Phiếu tiếp nhận nhu cầu; `00_NGUON-HO-SO.md` | — |
| H2 | 01, 02 | Báo cáo hiện trạng/DMI (cổng G1); Chiến lược & lộ trình | `sht-cds-danh-gia-hien-trang` |
| H3 | 03 (**chỉ khi đã có 01, 02** — luật #4) | PRD; Thiết kế agent; Đề xuất/Hợp đồng dịch vụ; Go/No-Go (HITL) | `sht-cds-thiet-ke-prd`, `sht-cds-thiet-ke-agent`, `ra-soat-hop-dong-vendor` |
| H4 | 04–07 | Hồ sơ Pilot; Báo cáo tiến độ; SOP vận hành | lệnh `/tao-ho-so-pilot`, `/kiem-tra-giai-doan` |
| H5 | 08–10 | BB nghiệm thu; Báo cáo đo giá trị/ROI; Bàn giao | `sht-nen-tang-kiem-chung` |

> Ánh xạ pha ↔ giai đoạn là đề xuất ban đầu — ⚠️ chưa đối chiếu với `.agents/knowledge/`, soát lại khi dùng ca thật đầu tiên.

### E. Hợp đồng cung cấp thiết bị IoT (chuỗi back-to-back)

| Pha | Tài liệu điển hình |
|---|---|
| H1 | Yêu cầu khách / RFI; Phiếu đề xuất |
| H2 | Báo giá NCC; Bảng so sánh; Spec kỹ thuật đối chiếu |
| H3 | Hợp đồng đầu ra (khách) + đầu vào (NCC) khớp back-to-back; PO |
| H4 | Kế hoạch giao hàng/lắp đặt; BB bàn giao từng đợt; License/bảo hành |
| H5 | BB nghiệm thu; Hồ sơ thanh toán; Theo dõi hạn bảo hành/license |

## 3. Minh hoạ bóc tách động (4 ca)

- **Tuyển dụng:** Word — Nhu cầu định biên · Chân dung & khung năng lực · Kế hoạch kênh nguồn · Dự toán & đãi ngộ · Onboarding 30-60-90. Excel — `Data_UngVien` (Ma, Vi_Tri, Kenh_Nguon, Diem, Trang_Thai…), `Cost_Model` (cost-per-hire, time-to-fill). *(SHT: chấm ứng viên theo ASK qua `chuan-hoa-du-lieu-tuyen-dung`.)*
- **Giải trình sự cố:** Word — Diễn biến & timeline · Thiệt hại · Ứng phó khẩn · RCA (5 Whys/Fishbone) · Phòng ngừa · Trách nhiệm. Excel — `Log_SuCo`, `Thiet_Hai`. Slide 5 trang: xảy ra gì → dập thế nào → không lặp lại.
- **Mua sắm CNTT:** Word — Căn cứ & hiện trạng · Yêu cầu kỹ thuật · So sánh 3 báo giá · Dự toán & nguồn vốn · Nghiệm thu & bảo hành. Excel — `Data_ThietBi`, `Dashboard`.
- **Đề tài nghiên cứu:** Mở đầu · Ch.1 Cơ sở lý luận · Ch.2 Phương pháp · Ch.3 Kết quả · Kết luận/Phụ lục. Excel — `Raw_Survey_Data`, `Statistical_Model`. Slide 12 trang bảo vệ.
