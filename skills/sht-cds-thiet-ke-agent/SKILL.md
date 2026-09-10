---
name: "sht-cds-thiet-ke-agent"
description: "Thiết kế & thẩm định use-case AI agentic trước khi đề xuất cho khách Bank/Telco — khai báo agent đủ 3 chiều Purpose/Scope/Boundaries, gán 3 tầng confidence (tự hành động / người duyệt / chỉ ghi log), chọn mức Tiered Governance L1-L2-L3, dựng bộ ca kiểm thử có ca gài, chốt vòng đời sandbox→pilot→production→review và 4 hạng mục bàn giao. LUÔN dùng khi người dùng nói \"thiết kế use-case AI\", \"AI được tự quyết đến đâu\", \"chatbot cho ngân hàng\", \"mức tự động hóa\", \"kiểm thử chất lượng AI\", \"HITL\", \"agent có tự chạy được không\", \"khách hỏi nếu AI sai thì ai chịu\" — kể cả khi chỉ mô tả tình huống mà không nhắc chữ \"agentic\". Dùng KÈM sht-cds-danh-gia-hien-trang (bắt buộc qua Giai đoạn 01 trước) và sht-nen-tang-kiem-chung (bàn giao). KHÔNG dùng để đo DMI/đánh giá hiện trạng, rà soát hợp đồng vendor, hay chuẩn hóa dữ liệu CRM."
---

# Thiết kế & quản trị use-case AI agentic cho Bank/Telco

Skill này lo **phần thiết kế AI agent** của **Giai đoạn 03 (Thiết kế giải pháp) · 04 (Pilot) · 06 (Quản trị rủi ro)** trong khung 11 giai đoạn CĐS của SHT. Giai đoạn 01 do `sht-cds-danh-gia-hien-trang` lo. Phần **quy trình To-Be + PRD** của Giai đoạn 03 do `sht-cds-thiet-ke-prd` lo — **PRD là đầu vào của skill này** khi hướng thi công đã chốt là AI agent; đừng khai báo agent khi chưa có PRD hoặc bảng điểm nghẽn. Quy tắc bàn giao do `sht-nen-tang-kiem-chung` lo.

Câu tổng kết của cả skill: **"Autonomy isn't risk. Unsupervised autonomy is risk."** Tự chủ không phải rủi ro; tự chủ *không có giám sát* mới là rủi ro.

Nguồn: *The Agentic Bank* (Driss Temsamani) Ch.3–5, 7 · tài liệu 11 giai đoạn CĐS SHT mục 04, 06 · bài học vận hành nội bộ.

---

## CỔNG CHẶN — kiểm trước khi làm bất cứ việc gì

**Luật cấm kỵ của SHT:** không đề xuất giải pháp AI (03) nếu chưa đi qua Đánh giá hiện trạng (01) và Chiến lược (02).

Hỏi ngay đầu phiên:

1. Đã có Báo cáo hiện trạng / DMI của khách chưa? Chưa → dừng, chuyển sang `sht-cds-danh-gia-hien-trang`.
2. Use-case này đã nằm trong Backlog use-case ở Giai đoạn 02 chưa, và map về trụ nào (Tài chính / Khách hàng / Hệ thống)? Không map được trụ nào → **loại**, đây là "làm AI vì đối thủ có".
3. Chất lượng dữ liệu của khách ở mức nào? Dữ liệu bẩn → không thiết kế agent, quay lại làm sạch trước. *Rác vào thì rác ra.*

Ba câu này là guardrail. Bỏ qua là hỏng cả đề xuất.

---

## 1. Khai báo agent — đủ 3 chiều, thiếu 1 là thiết kế hỏng

| Chiều | Câu hỏi | Ví dụ đạt |
|---|---|---|
| **Purpose** | Agent tối ưu cho **kết quả** gì? | "Giữ đệm thanh khoản, giảm vốn nhàn rỗi" |
| **Scope** | Truy cập **dữ liệu nào**, được **hành động** tới đâu? | "Đọc số dư ERP + luồng FX; tự chạy sweep nội bộ; escalate chuyển liên NH >$10M" |
| **Boundaries** | **Giới hạn** nào phải tôn trọng? | "Dừng & báo nếu biến động FX >3%, đệm <105%, hoặc mô hình dự báo mâu thuẫn" |

**Bảng dùng khi review thiết kế:**

| Agent định nghĩa tốt | Agent định nghĩa tồi |
|---|---|
| Mục tiêu cụ thể: "tối ưu thanh khoản" | Mơ hồ: "quản lý tiền" |
| Quyền API có phạm vi: chỉ ERP & FX | Quyền rộng: mọi hệ thống |
| Có ngưỡng: escalate ở $10M | Không trigger: lỗi phát hiện sau khi đã xảy ra |

> Agent thiết kế tốt hành xử như một cấp phó đáng tin. Agent định nghĩa tồi hành xử như thực tập sinh cầm chìa khóa vạn năng.

**Ba lớp ràng buộc — dùng cả ba, không chọn một:**

1. **Architectural** (cứng): access control, quyền API, phân tách dữ liệu. Tuyến phòng thủ đầu tiên.
2. **Behavioral** (trong logic agent): luật mã hoá, khung ra quyết định, heuristic nội bộ.
3. **Supervisory** (động): monitoring, feedback loop, HITL — can thiệp khi dữ liệu mập mờ, mục tiêu xung đột, tình huống chưa từng gặp.

Quan trọng nhất: **agent phải biết khi nào nó đang đuối.** Không chắc thì hỏi, đừng đoán.

---

## 2. Ba tầng confidence — quyết định AI được tự làm đến đâu

Confidence phải **tính được**, không cảm tính. Cấu thành: độ nhất quán tín hiệu giữa nhiều mô hình · độ sẵn có & mới của dữ liệu · độ tin cậy lịch sử của quyết định tương tự · input có nằm trong miền đã huấn luyện không.

| Tầng | Hành vi | Vai trò |
|---|---|---|
| **Cao** | **Tự hành động** — chạy phản ứng đã cấp phép trước (chặn giao dịch gian lận rõ ràng, khoá tài khoản bị xâm nhập) | Người thực thi |
| **Trung bình** | **Đối tác của người** — chuẩn bị tóm tắt kèm ngữ cảnh (sự cố trước, rủi ro đã biết, lịch sử khách) rồi chuyển người duyệt | *Decision concierge*, **không phải quan toà** |
| **Thấp** | **Quan sát thầm lặng** — ghi log, gắn thẻ phân tích sau. Góp vào trí nhớ tổ chức mà không tạo nhiễu | Bộ nhớ |

Ngưỡng **không cố định**: agent nhận feedback (được chấp nhận / bị override / bị đánh dấu lỗi) → huấn luyện lại → điều chỉnh ngưỡng.

**Ví dụ ba tầng trên cùng một khách:** quẹt thẻ Chicago 14:00, 30 phút sau quẹt Miami → bất khả thi địa lý → **chặn ngay** (cao). Quán cà phê mới nhưng đúng giờ, đúng khu, đúng mức chi → **cho qua + ghi lại** (thấp). Cửa hàng xa xỉ đã từng đến nhưng số tiền gấp đôi → **dừng, gắn cờ, chuyển người** (trung bình).

---

## 3. Bốn trục ngữ cảnh — confidence chỉ là một nửa

Điều chỉnh hành vi agent **kể cả khi confidence cao**:

| Trục | Luật |
|---|---|
| **Hạng khách hàng** | Khách VIP/private → agent chỉ ở chế độ *khuyến nghị*, không tự khoá. Khách phổ thông hành vi ổn định → tự chủ hơn |
| **Giá trị giao dịch** | Ngưỡng theo trọng số rủi ro. Sai $15 là phiền; sai $15.000 là khủng hoảng. Giá trị cao phải escalate **kể cả confidence cao** |
| **Thời gian & địa điểm** | Giờ hành chính: escalate cho người trong vài phút. 02:00 Chủ nhật: agent tự chặn trước rồi log lại. Cần **chính sách escalate theo thời gian** |
| **Tải hệ thống & mệt cảnh báo** | Khi người xử lý đang ngập cảnh báo, agent giảm escalate việc không khẩn, ưu tiên ca rủi ro cao / có phơi nhiễm pháp lý |

---

## 4. Tiered Governance — lộ trình mở rộng an toàn

- **L1 – Advisory:** agent gắn cờ rủi ro, khuyến nghị; **người giữ toàn quyền**
- **L2 – Controlled Execution:** agent xử lý ca rủi ro thấp trong ngưỡng chặt; không chắc → escalate
- **L3 – Autonomous Playbooks:** agent chạy trong playbook đã định, tự ưu tiên ca, escalate theo mẫu đã học; người review ngoại lệ + cập nhật chính sách

Xuyên suốt cả 3 level: **explainability · auditability · regulatory alignment**. Mọi hành động phải truy vết được và **phản bác được** (contestable).

**Quy tắc mặc định của SHT khi bán cho Bank:** chiếu 3 câu phân loại rủi ro — *Nếu AI sai, ai thiệt và bao nhiêu? Kết quả có gửi ra ngoài? Có chạm dữ liệu cá nhân/tiền?* Hầu hết use-case ngân hàng chạm cả ba → mức **Cao** → mặc định **HITL + ghi log**, khởi đầu ở **L1**, không nhảy thẳng L3. Phân vân thì chọn mức cao hơn trong tháng đầu.

---

## 5. Kiểm thử chất lượng AI (Giai đoạn 04)

AI tạo sinh **tự tin cả khi sai**. Mỗi câu trả lời là một đầu ra cần nghiệm thu.

- Xây **≥30–50 ca**: ca thường + ca biên (dữ liệu thiếu/mập mờ) + **ca gài ≥20%** (hỏi điều không có, xem có bịa không)
- Chấm theo 4 nhãn: **Đúng / Sai / Bịa / Từ chối đúng**
- Quy tắc vàng: **"Từ chối đúng" (nói không biết) = ĐẠT**
- Bắt AI **trích nguồn** và nói "không có thông tin" khi thiếu
- HITL bắt buộc ở báo giá / cam kết: AI gợi ý, **người duyệt gửi**

Cột bảng ca kiểm thử: `Mã ca · Loại (thường/biên/gài) · Câu hỏi · Đáp án/nguồn chuẩn · Đầu ra AI · Có trích nguồn? · Kết quả · Mức rủi ro · Cần người duyệt?`

Lỗi hay gặp: bộ ca toàn câu dễ; không có tiêu chí "đúng"; để AI báo giá tự động không người duyệt → bịa số.

> Thà một AI biết nói "tôi chưa biết" còn hơn mười AI trả lời trơn tru mà bịa.

---

## 6. Vòng đời agent — không phải "bắn rồi quên"

```
sandbox → pilot → production → review
```

Trước khi lên production bắt buộc có: **stress test** (mô phỏng khủng hoảng thật) · **staged rollout** (bắt đầu chế độ chỉ-đọc → thực thi có giới hạn dưới giám sát) · **governance sign-off** (nghiệp vụ + rủi ro + tuân thủ cùng duyệt) · **version control** (rollback được trong vài phút).

| Bẫy | Cách chặn |
|---|---|
| Agent cấp quyền quá tay, trôi khỏi làn | **Least-privilege access** |
| Vai trò để nguyên khi chính sách đã đổi | **Review vai trò hằng quý** |
| Không rollback khi cập nhật hỏng | **Bắt buộc có đường rollback** |

**Bẫy lớn nhất khi scale:** pilot đạt **không** đảm bảo scale đạt. Pilot chạy trên nhóm nhỏ với dữ liệu quen; mở rộng thì agent gặp dữ liệu ngoài phân phối pilot và chất lượng tụt. Khác biệt căn bản với phần mềm thường — phần mềm scale chỉ lo tải, AI scale lo cả tải lẫn chất lượng.

---

## 7. Hai cơ chế giám sát cấp tổ chức

**Agent Review Committee** — product owner + quản lý rủi ro + data scientist + tuân thủ + lãnh đạo nghiệp vụ. Trả lời: *Agent nào an toàn để scale? Override tăng ở đâu, vì sao? Quyết định có khớp giá trị và kỳ vọng pháp lý? Khi nào tạm dừng / huấn luyện lại / cho nghỉ một agent?*

> Không agent nào được **âm thầm** tốt nghiệp từ trợ lý lên tự chủ mà không qua review chính thức.

**Control Room Dashboard** — số quyết định mỗi agent · tỷ lệ escalate & override theo mảng · chỉ báo thiên lệch theo nhân khẩu/địa lý/hạng khách · xung đột người ↔ agent (bên nào cuối cùng đúng) · **agent drift** (output lệch khỏi mẫu dự kiến).

---

## 8. KPI riêng cho use-case AI

Ngoài 4 nhóm KPI chuẩn (Giá trị kinh doanh · Áp dụng · Chất lượng/Vận hành · Rủi ro/Tuân thủ), bổ sung 2 chỉ số đặc thù AI tạo sinh:

| Chỉ số | Ghi chú |
|---|---|
| **% Bịa** | Chế độ hỏng đặc thù của AI tạo sinh, khác "sai sót nhập liệu". Lấy từ bộ ca kiểm thử §5 |
| **% Từ chối đúng** | **Tăng là tốt** — ngược trực giác thông thường |

Chi phí AI **biến đổi theo lượng dùng** (token/lượt gọi), khác license phẳng. Business case ở Giai đoạn 02 tính như license cố định sẽ sai khi scale.

**Baseline là nguyên tắc thép:** đo **TRƯỚC** khi triển khai. Không đo trước → không chứng minh được ROI → không có hợp đồng giai đoạn 2.

---

## 9. Bốn hạng mục bắt buộc trong hồ sơ bàn giao

1. **Bộ ca kiểm thử đầy đủ** — khách tự chạy lại được khi nâng cấp
2. **Prompt / cấu hình / nguồn tri thức RAG** đang dùng
3. **Quy trình xử lý khi AI sai** — ai phát hiện, báo ai, khắc phục ra sao, trong bao lâu
4. **Danh sách giới hạn đã biết** — những gì agent này chắc chắn làm không tốt

Mục 4 là thứ khách Bank đánh giá cao nhất và nhà cung cấp hay giấu nhất. Nói thẳng giới hạn tạo uy tín; giấu đến lúc lộ thì mất cả hợp đồng lẫn quan hệ.

Câu khách sẽ hỏi ở buổi nghiệm thu: *"Nếu AI trả lời sai cho khách hàng của chúng tôi thì ai chịu trách nhiệm?"* — phải có câu trả lời **bằng văn bản** trong hồ sơ, không trả lời miệng.

---

## 10. Ba yếu tố lòng tin — thiết kế vào kiến trúc, không phải phụ kiện đạo đức

| Yếu tố | Câu hỏi | Hành vi hệ thống cần có |
|---|---|---|
| **Transparency** | Tôi có hiểu agent đã làm gì và vì sao? | Lý luận thuật lại được, quyết định soi được |
| **Alignment** | Agent theo đúng mục tiêu với đúng luật? | Hành động trong phạm vi chính sách |
| **Accountability** | Ai chịu trách nhiệm khi agent sai? | Bản đồ escalate, vòng huấn luyện lại, hồ sơ override |

Phân biệt **functional trust** (agent chạy đúng, giải thích rõ, escalate hợp lý — từ chất lượng kỹ thuật) và **strategic trust** (các bên tin mục tiêu hệ thống khớp mục tiêu của họ — từ sự rõ ràng của tổ chức). Thiếu strategic trust thì **quyết định đúng vẫn có cảm giác tuỳ tiện**.

---

## 11. Lưu ý riêng ngành Bank/Telco tại Việt Nam

- **NĐ 13/2023** về bảo vệ dữ liệu cá nhân là mức nền chung. Ngân hàng còn chịu quy định riêng của **NHNN** về an toàn hệ thống thông tin.
- Khách có yếu tố nước ngoài / yêu cầu chuẩn quốc tế: đối chiếu thêm **EU AI Act** (phân loại hệ thống AI theo mức rủi ro) và **NIST AI RMF**.
- Câu khách Bank chắc chắn hỏi: *"Dữ liệu khách hàng có rời khỏi hạ tầng của chúng tôi không?"* — trả lời bằng **sơ đồ luồng dữ liệu**, không bằng lời hứa.

---

## Checklist chốt trước khi trình đề xuất agentic

- [ ] Đã qua Giai đoạn 01 (hiện trạng) và 02 (use-case map về ít nhất 1 trụ)
- [ ] Agent khai báo đủ Purpose · Scope · Boundaries
- [ ] Đã gán 3 tầng confidence + 4 trục ngữ cảnh
- [ ] Đã chọn mức Tiered Governance, mặc định khởi đầu L1
- [ ] Có bộ ca kiểm thử ≥30 ca, ca gài ≥20%
- [ ] Có kế hoạch vòng đời + đường rollback
- [ ] Có baseline đo trước triển khai
- [ ] Hồ sơ bàn giao đủ 4 hạng mục (nhất là danh sách giới hạn đã biết)
- [ ] Đã chạy checklist bàn giao của `sht-nen-tang-kiem-chung`

