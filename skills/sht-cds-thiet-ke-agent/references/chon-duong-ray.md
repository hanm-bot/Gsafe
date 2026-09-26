# Cổng chọn đường ray triển khai — Ray 1 / Ray 3 / Ray 2

Dùng **sau B5** của khung giải quyết vấn đề (plan/PRD đã chốt, đã có sơ đồ `archify`), trước khi dựng bất cứ thứ gì. Bản đồ khung: `docs/HE-DIEU-HANH-AI-5-LOP.md` mục 1c.

- **Việc nội bộ SHT:** dùng thẳng bảng này. Cổng chặn 01/02 ở đầu `SKILL.md` **không áp** — luật cứng #4 chỉ áp cho tài liệu bán khách.
- **Việc bán khách:** chỉ dùng sau khi đã qua cổng chặn 01/02 của `SKILL.md`.
- Kết quả của bảng là **đề xuất**. Người (Mr. Hà hoặc chủ quản use-case) duyệt ray; AI không tự chốt.

## Ba đường ray

| Ray | Là gì | Ở SHT hiện có |
|---|---|---|
| **1 · Agent & Skill (0-code)** | Skill + agent + workspace thư mục; người gọi, AI làm, kết quả là hiện vật file | `sht-skills`, `.claude/agents/`, `data/workspaces/` |
| **3 · Hybrid** | Ray 1 + cổng quyết định (rủi ro × tin cậy → TỰ LÀM / NGƯỜI DUYỆT / CHỈ GHI LOG) + MCP **chỉ đọc** trước quyết định, MCP ghi **sau** cổng | chuỗi RJMW, skill `sht-jev-cong-quyet-dinh` |
| **2 · Full App Stack** | Frontend + backend + CSDL + API, cần dev bài bản | **chưa có hạ tầng** |

## Năm câu hỏi — trả lời theo thứ tự, dừng ở câu đầu tiên ra kết quả

| # | Câu hỏi | Nếu CÓ |
|---|---|---|
| Q1 | Kết quả có **ghi/gửi ra hệ thống ngoài** (CRM, email khách, cổng thanh toán, văn bản phát hành) mà không qua tay người mở file? | → **Ray 3** tối thiểu (cần cổng + sổ quyết định) |
| Q2 | Có **quyết định lặp lại** trên dữ liệu sống (≥ hàng tuần), mà sai thì có người/tiền thiệt? | → **Ray 3** |
| Q3 | Có **người không dùng Claude/CLI** phải thao tác hằng ngày (nhập liệu, bấm duyệt) trên giao diện riêng? | → xét **Ray 2**, nhưng thử trước bằng Artifact có trạng thái (Ray 1). Artifact không đủ thì mới lập RFC Ray 2 |
| Q4 | Cần **trạng thái bền nhiều người dùng đồng thời**, phân quyền, hoặc chạy 24/7 không người gọi? | → **RFC Ray 2** (hoặc Ray 3 + engine lịch; hiện ❌ chưa có, xem `AI_Architecture_Core.md` §4) |
| Q5 | Không câu nào trên đúng | → **Ray 1** (mặc định) |

**Luật cứng của bảng:**
- **Ray 2 không bao giờ là đầu ra trực tiếp.** Nó luôn ra "cần RFC" kèm lý do Artifact/Ray 3 không đủ. Tiền lệ 05/09/2026: không dựng hạ tầng khi chưa có ca thật chứng minh cần.
- **Phân vân giữa hai ray → chọn ray có cổng người duyệt chặt hơn** (Ray 3 hơn Ray 1). Cùng tinh thần "phân vân thì chọn mức cao hơn" ở mục 4.
- Chọn Ray 3 thì mức tự chủ **khởi đầu L1** (mục 4). Không vào thẳng TỰ LÀM.
- Dữ liệu CRM chưa có token MCP → Ray 3 vẫn chạy được nhưng mọi quyết định phải ghi rõ **dữ liệu TĨNH**.

## Mẫu ghi kết quả (dán vào cuối plan/PRD)

```
## Chọn đường ray
- Q1 … Q5: <có/không + một câu lý do mỗi câu>
- Đề xuất: Ray <1|3> | "Cần RFC Ray 2" vì <…>
- Mức tự chủ khởi đầu (nếu Ray 3): L1
- Người duyệt ray: <tên> · mã HITL: <HITL-…>
```
