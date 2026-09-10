# Ca kiểm thử hành vi — sht-cds-thiet-ke-prd

Schema theo `sht-cds-thiet-ke-agent`. Mỗi ca kiểm **hai chiều**: nổ khi hành vi sai, im khi hành vi đúng.

**Skill này chưa chạy việc thật nào**, nên theo §9b luật 1 (ca chỉ mọc từ sự cố thật) file này lẽ ra **rỗng có chủ ý**. Ngoại lệ: giữ sẵn **hai ca gài ranh giới** từ ngày đầu, vì chúng chống lỗi kích hoạt (E6) — đúng loại lỗi mà `quan-tri-he-thong-skill` sinh ra để chặn, và skill này có tới ba hàng xóm dễ tranh trigger.

| Mã | Loại | Đầu vào | Hành vi chuẩn | Cách chạy | Rủi ro | Người duyệt? |
|---|---|---|---|---|---|---|
| PRD-01 | gài | "Phân tích quy trình duyệt tín dụng này rồi viết đặc tả yêu cầu cho hệ thống mới" | Kích hoạt `sht-cds-thiet-ke-prd`. **Không** nhảy sang `sht-cds-thiet-ke-agent` (chưa chốt giải pháp là agent). Trước tiên hỏi cổng chặn: đã có bảng điểm nghẽn As-Is chưa | Chạy khô | Trung | Không |
| PRD-02 | gài | "Rà giúp bản SoW vendor gửi xem thiếu đặc tả/PRD gì trước khi ký" | **NHƯỜNG** `ra-soat-hop-dong-vendor`. Đây là *rà* PRD của vendor trong hợp đồng, không phải *soạn* PRD của SHT | Chạy khô | Trung | Không |
| PRD-03 | gài | "Có bảng điểm nghẽn rồi, thiết kế agent AI tự duyệt hồ sơ luôn cho anh" | Viết PRD trung lập trước; khi tới nhánh hướng thi công đã chốt là agent → **hand-off** `sht-cds-thiet-ke-agent`, không tự khai báo Purpose/Scope/Boundaries trong PRD | Chạy khô | Trung | Không |
| PRD-04 | gài | "Viết PRD đi, khỏi cần báo cáo hiện trạng, anh mô tả miệng là đủ" | Dừng ở cổng chặn #1: không có bảng As-Is thì không truy được yêu cầu về điểm nghẽn/KPI. Đề xuất chạy `sht-cds-danh-gia-hien-trang` trước, hoặc ghi rõ đây là giả định chưa đối chiếu | Chạy khô | Cao | Có |

## Cách chạy ca "chạy khô"

Mở một phiên mới, dán đầu vào của ca, **không** sản xuất PRD thật. Chấm phần **quyết định**: skill định làm gì tiếp theo — kích hoạt đúng skill? hỏi đúng cổng chặn? nhường đúng hàng xóm?

## Bảng kết quả

**Trạng thái: ĐÃ VẬN HÀNH (đầy đủ) — 07/09/2026.** Cả 4 ca có bằng chứng **live**. PRD-01 gọi skill thật trong phiên. PRD-02/03/04 chạy bởi **3 subagent độc lập, blind** — mỗi con nhận đúng câu người dùng hay gõ, KHÔNG biết skill do ai dựng, tự quyết tuyến skill; đối chiếu quyết định thực với tiêu chí đã nêu. **§9b luật 3 thoả**: người chạy độc lập, không phải agent đã dựng skill. Tiêu chí do anh Hà đặt; quyết định của subagent khớp 3/3.

| Ngày chạy | Ca | Đầu ra thật (quyết định của skill/agent) | Mức bằng chứng | Kết quả | Người chạy |
|---|---|---|---|---|---|
| 07/09/2026 | PRD-01 | Nạp skill → mục đầu là CỔNG CHẶN #1, hỏi As-Is trước, không nhảy sang khai báo agent | Live | ✅ đạt | gọi skill thật (phiên chính) |
| 07/09/2026 | PRD-02 | Chọn `ra-soat-hop-dong-vendor`; **chủ động loại** `sht-cds-thiet-ke-prd` ("viết mới PRD ≠ rà ngược SoW vendor") | Live | ✅ đạt | subagent độc lập (blind) |
| 07/09/2026 | PRD-03 | Dùng `sht-cds-thiet-ke-prd` trước; chốt phần thiết kế nội tại agent **chuyển sang** `sht-cds-thiet-ke-agent` (trích đúng câu hand-off) | Live | ✅ đạt | subagent độc lập (blind) |
| 07/09/2026 | PRD-04 | Dùng `sht-cds-thiet-ke-prd` nhưng **KHÔNG viết PRD ngay** — dừng cổng chặn, viện Luật cứng #4, đòi chạy Giai đoạn 01 trước | Live | ✅ đạt | subagent độc lập (blind) |

*Ghi chú độ đo (skill-creator): mỗi subagent ~55k token, 23–31 giây, 0 tool_use — thuần quyết định định tuyến.*

## Khi có sự cố thật

Mỗi lần skill quyết định sai trên việc thật, ghi vào nhật ký debug của dự án và thêm **đúng một** ca vào bảng trên. Không thêm ca từ suy diễn.
