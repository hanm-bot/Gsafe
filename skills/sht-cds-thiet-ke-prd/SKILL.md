---
name: "sht-cds-thiet-ke-prd"
description: >-
  Phân tích quy trình To-Be và soạn PRD cho giải pháp chuyển đổi số B2B theo Giai đoạn 03 phương pháp luận SHT — biến bảng điểm nghẽn As-Is (từ Giai đoạn 01) thành PRD: luồng To-Be, yêu cầu chức năng/phi chức năng, user story, tiêu chí nghiệm thu, đặc tả dữ liệu & tích hợp, tuân thủ NĐ13/NHNN, ưu tiên MoSCoW, truy vết yêu cầu↔điểm nghẽn/ROI trước Cổng G2/G3.
  LUÔN dùng khi người dùng nói "thiết kế PRD", "viết PRD", "đặc tả yêu cầu", "quy trình To-Be" — kể cả khi chỉ mô tả một quy trình cần số hoá mà chưa nhắc chữ PRD.
  Khi giải pháp chốt là AI agent, chuyển phần thiết kế agent sang sht-cds-thiet-ke-agent; bàn giao theo sht-nen-tang-kiem-chung.
  KHÔNG dùng để đo DMI/đánh giá hiện trạng (dùng sht-cds-danh-gia-hien-trang), thiết kế nội tại AI agent (dùng sht-cds-thiet-ke-agent), rà soát PRD/SoW trong hợp đồng vendor (dùng ra-soat-hop-dong-vendor), hay dựng UI từ PRD.
---

# Thiết kế quy trình To-Be & soạn PRD cho giải pháp CĐS (SHT Phase 03)

Skill này lo **cầu nối đang đứt trong chuỗi CĐS**: giữa *chẩn đoán* (Giai đoạn 01) và *thi công*. Nó biến bảng điểm nghẽn As-Is thành một **PRD (Product Requirements Document)** — tài liệu yêu cầu mà **mọi hướng thi công** (AI agent, tự động hoá luồng, cổng/portal, tích hợp hệ thống) đều đọc để làm.

Ba câu định vị của cả skill:

- **Chẩn đoán → kê đơn.** `sht-cds-danh-gia-hien-trang` chẩn (As-Is, điểm nghẽn). Skill này kê đơn (To-Be, yêu cầu). `sht-cds-thiet-ke-agent` bào chế thuốc AI — *nếu* chọn hướng agent.
- **PRD trung lập với hướng thi công.** Viết *cái gì cần đạt*, không khoá vào *dựng bằng gì*. Khoá công nghệ quá sớm là làm hỏng đề xuất.
- **Mỗi yêu cầu phải truy được về một điểm nghẽn có thật và một KPI gốc.** Yêu cầu không truy được nguồn là yêu cầu thừa — cắt.

Skill này kế thừa toàn bộ quy tắc nền tảng từ `sht-nen-tang-kiem-chung` (truy vết nguồn, một bản có hiệu lực, kết xuất theo người đọc, checklist bàn giao). Không chép lại — trỏ về.

---

## CỔNG CHẶN — kiểm trước khi viết một dòng PRD

**Luật cấm kỵ của SHT:** không đề xuất giải pháp (03) khi chưa qua Đánh giá hiện trạng (01) và Chiến lược (02).

Hỏi ngay đầu phiên:

1. **Đã có bảng điểm nghẽn As-Is / Báo cáo hiện trạng chưa?** Chưa → dừng, chuyển `sht-cds-danh-gia-hien-trang`. Không có bản đồ As-Is thì không chứng minh được PRD giải quyết điểm nghẽn nào, và không có KPI gốc để đo cải thiện.
2. **Use-case này đã map về trụ chiến lược nào (Tài chính / Khách hàng / Hệ thống) chưa?** Không map được → **loại**, đây là "làm CĐS vì đối thủ có".
3. **Dữ liệu nguồn cho giải pháp ở mức nào?** Dữ liệu bẩn > 15% → ghi thành *giả định rủi ro* trong PRD và yêu cầu làm sạch trước, đừng đặc tả trên nền rác.

Ba câu này là guardrail. Bỏ qua là hỏng cả PRD.

> **Ngoại lệ dùng nội bộ:** khi PRD là để SHT tự dùng (công cụ nội bộ), không phải bán cho khách, cổng #2 nới lỏng — vẫn giữ #1 và #3.

---

## 1. Từ điểm nghẽn → mục tiêu giải pháp (bảng truy vết)

Đây là xương sống chống yêu cầu thừa. Mỗi mục tiêu buộc trỏ về ≥1 điểm nghẽn Giai đoạn 01 và một KPI gốc đo được **trước** khi làm.

| Mã MT | Điểm nghẽn nguồn (từ GĐ01) | KPI gốc (baseline) ⚠️ có nguồn | Mục tiêu To-Be | Giá trị kỳ vọng |
|---|---|---|---|---|
| MT-01 | *(dẫn đúng dòng bảng As-Is)* | *(số + nguồn sinh ra số)* | *(trạng thái mong muốn)* | *(giảm bao nhiêu %/giờ)* |

Quy tắc thép: **baseline đo TRƯỚC**. Không có baseline thì không chứng minh được ROI → không có hợp đồng giai đoạn sau. Mọi con số baseline phải gắn nguồn (luật cứng SHT #1, #2); số chưa đối chiếu gắn nhãn ⚠️.

---

## 2. Thiết kế quy trình To-Be

Trước khi viết yêu cầu, vẽ **luồng nghiệp vụ mới**. To-Be không phải As-Is bỏ bớt bước — nó là cách làm lại.

Với mỗi bước To-Be, chốt 4 thuộc tính:

| Thuộc tính | Câu hỏi |
|---|---|
| **Ai/cái gì thực hiện** | Người, hệ thống, hay agent? |
| **Chế độ** | Tự động hoàn toàn · người-trong-vòng (HITL) · thủ công |
| **Dữ liệu vào/ra** | Lấy từ đâu, đẩy đi đâu |
| **Điểm kiểm soát** | Nơi cần duyệt, nơi cần log |

Đánh dấu rõ **bước nào HITL** (§4 giải thích vì sao chỗ chạm tiền/PII bắt buộc HITL). Ghi kèm điểm nghẽn As-Is mà mỗi bước To-Be xoá bỏ — đó là bằng chứng thiết kế có mục đích, không phải vẽ cho đẹp.

Sơ đồ luồng: mô tả bằng bảng bước hoặc sơ đồ mermaid. So As-Is ↔ To-Be cạnh nhau để lộ đúng chỗ thay đổi.

---

## 3. Cấu trúc PRD chuẩn SHT

Điền theo mẫu `references/mau-prd-sht.md`. Mười khối bắt buộc:

1. **Bối cảnh & vấn đề** — trích từ Báo cáo hiện trạng, không viết lại từ đầu.
2. **Mục tiêu & phi-mục-tiêu** — *phi-mục-tiêu* (cái PRD này CỐ Ý không làm) quan trọng ngang mục tiêu; nó chặn phình phạm vi.
3. **Bảng truy vết mục tiêu ↔ điểm nghẽn** (§1).
4. **Quy trình To-Be** (§2).
5. **User story + tiêu chí nghiệm thu** — mỗi story: *"Là [vai], tôi muốn [hành động] để [giá trị]"*, kèm acceptance criteria đo được (Given/When/Then hoặc danh sách kiểm).
6. **Yêu cầu chức năng (FR)** — đánh số, mỗi FR trỏ về ≥1 user story.
7. **Yêu cầu phi chức năng (NFR)** — §4.
8. **Đặc tả dữ liệu & tích hợp** — §5.
9. **Ưu tiên hoá MoSCoW + phạm vi Pilot** — §6.
10. **Rủi ro, giả định & phụ thuộc** — gồm giả định dữ liệu bẩn ở cổng chặn #3.

Nguyên tắc viết yêu cầu: **đo được, nghiệm thu được, truy nguồn được**. Yêu cầu không kiểm chứng được ("hệ thống phải thân thiện") là yêu cầu hỏng — viết lại thành số.

---

## 4. Yêu cầu phi chức năng & tuân thủ (khối hay bị bỏ nhất)

Đây là chỗ PRD generic từ công cụ ngoài luôn thiếu, và là chỗ khách Bank/Telco soi kỹ nhất. Đọc và điền `references/checklist-tuan-thu-nd13-nhnn.md`.

Sáu nhóm NFR bắt buộc cân nhắc:

| Nhóm | Chốt gì |
|---|---|
| **Bảo mật & quyền** | Least-privilege, phân tách dữ liệu, ai thấy gì |
| **Tuân thủ** | **NĐ 13/2023** (bảo vệ DLCN) là nền; Bank thêm quy định **NHNN** về ATTT hệ thống; có yếu tố nước ngoài thì đối chiếu EU AI Act / NIST AI RMF |
| **Luồng dữ liệu cá nhân** | **Sơ đồ luồng dữ liệu** — trả lời "dữ liệu KH có rời hạ tầng khách không?" bằng sơ đồ, không bằng lời hứa |
| **Hiệu năng & tải** | SLA, thông lượng, thời gian phản hồi — số, không tính từ |
| **HITL & phê duyệt** | Mọi bước chạm **tiền hoặc PII** mặc định HITL: hệ thống gợi ý, **người duyệt** thực thi |
| **Khả kiểm & rollback** | Log truy vết được, quyết định phản bác được, có đường lùi |

Quy tắc phân loại rủi ro (mượn từ `sht-cds-thiet-ke-agent`): *Nếu hệ thống sai, ai thiệt và bao nhiêu? Kết quả có ra ngoài? Có chạm tiền/PII?* Chạm cả ba → mức **Cao** → HITL bắt buộc, ghi thẳng vào NFR.

---

## 5. Đặc tả dữ liệu & tích hợp

Nối trực tiếp với khảo sát hạ tầng của Giai đoạn 01 (danh mục hệ thống, tình trạng API/webhook). Với mỗi tích hợp:

- **Hệ thống nguồn/đích** (core banking, CRM, cổng eKYC, hệ AML…) và **có API/webhook không** — nếu không, đó là một giả định rủi ro.
- **Dữ liệu trao đổi**: trường, định dạng, khối lượng, tần suất.
- **Che dữ liệu**: quy tắc masking/truncation cho PII trong log & DB.
- **Sự kiện & trạng thái**: cái gì kích hoạt bước tiếp, cái gì cần trace ID.

Không đặc tả xuống mức schema DB hay code — đó là việc của thiết kế chi tiết (LLD) sau PRD. PRD chốt *cần trao đổi gì với ai*, không chốt *bảng nào cột nào*.

---

## 6. Ưu tiên hoá MoSCoW & cắt phạm vi Pilot

Không PRD nào làm hết một lần. Gắn mỗi FR một mức:

- **Must** — thiếu là giải pháp vô nghĩa. Đây là ranh giới Pilot.
- **Should** — quan trọng nhưng Pilot sống thiếu được.
- **Could** — làm nếu còn nguồn lực.
- **Won't (lần này)** — ghi ra để chặn phình phạm vi; chính là phi-mục-tiêu ở §3.

**Phạm vi Pilot = tập Must, đủ nhỏ để chạy trên một nhóm/chi nhánh và đo được KPI.** Pilot đạt KHÔNG đảm bảo scale đạt — ghi cảnh báo này vào phần rủi ro.

---

## 7. Nhánh quyết định hướng thi công — PRD giữ trung lập

Cuối PRD, chốt hướng thi công nhưng **không nhét thiết kế chi tiết của hướng đó vào PRD**:

| Hướng chốt | Chuyển tiếp |
|---|---|
| Giải pháp **là AI agent / GenAI** | Hand-off `sht-cds-thiet-ke-agent`: khai báo Purpose/Scope/Boundaries, tầng confidence, Tiered Governance, bộ ca kiểm thử agent. **Không** chép các phần đó vào PRD này |
| Luồng tự động / RPA / cổng-portal / tích hợp | Bàn giao đội build với PRD + đặc tả tích hợp §5 làm đầu vào |
| Chưa đủ dữ liệu để chốt hướng | Ghi thành *quyết định còn treo*, nêu tiêu chí sẽ dùng để chốt |

Lý do giữ trung lập: cùng một PRD phải sống được qua việc đổi hướng thi công. Nếu PRD đã dính chặt vào "microservice X, hàng đợi Y", đổi hướng là viết lại từ đầu.

---

## 8. Review đối kháng PRD trước khi chốt

Trước khi trình, tự chất vấn PRD bằng bộ câu hỏi tới hạn (tinh thần red-team, không phải thủ tục):

- Mỗi yêu cầu: **đo được không? nghiệm thu bằng gì? thiếu nó thì hỏng ở đâu?**
- Có yêu cầu nào **không truy được** về điểm nghẽn/KPI không? → cắt hoặc bổ nguồn.
- NFR tuân thủ có sơ đồ luồng dữ liệu chưa, hay mới là lời hứa?
- Phạm vi Pilot có thật sự chạy được trên nguồn lực khách nêu không?
- Câu khách sẽ hỏi ở nghiệm thu: *"Nếu hệ thống sai cho khách hàng của chúng tôi thì ai chịu?"* — PRD đã trả lời **bằng văn bản** chưa?

Yêu cầu nào trượt một trong các câu trên thì sửa trước khi chốt, đừng để khách tìm ra.

---

## 9. Cổng kiểm soát & bàn giao

PRD là **artefact chốt trước Cổng G2/G3** — không có PRD được duyệt thì không sang thi công.

Kết xuất theo `sht-nen-tang-kiem-chung` §6, hai bản:

- **Bản Điều hành (1–2 trang):** vấn đề · mục tiêu & giá trị kỳ vọng · phạm vi Pilot (Must) · rủi ro chính · quyết định cần Sponsor duyệt.
- **Bản Chi tiết:** toàn bộ 10 khối PRD.

Chạy checklist bàn giao của `sht-nen-tang-kiem-chung` (ghi đúng thư mục đích, một bản có hiệu lực, dò trang trống khi xuất PDF, tự kiểm trước khi báo xong).

---

## Checklist chốt trước khi trình PRD

- [ ] Đã qua Giai đoạn 01 (có bảng điểm nghẽn As-Is) và use-case map về ≥1 trụ chiến lược
- [ ] Mỗi mục tiêu truy về ≥1 điểm nghẽn + KPI gốc có nguồn (số ⚠️ nếu chưa đối chiếu)
- [ ] Có sơ đồ quy trình To-Be, đánh dấu bước HITL
- [ ] PRD đủ 10 khối; mỗi FR trỏ về ≥1 user story; mỗi story có tiêu chí nghiệm thu đo được
- [ ] NFR có nhóm tuân thủ (NĐ13/NHNN) + **sơ đồ luồng dữ liệu**
- [ ] Đặc tả tích hợp nối với khảo sát hạ tầng GĐ01
- [ ] Đã gắn MoSCoW, chốt phạm vi Pilot = tập Must
- [ ] Đã chốt hướng thi công + chuyển tiếp đúng (agent → `sht-cds-thiet-ke-agent`)
- [ ] Đã chạy review đối kháng §8
- [ ] Đã xuất bản Điều hành + Chi tiết và chạy checklist `sht-nen-tang-kiem-chung`

---

Nguồn: phương pháp luận 11 giai đoạn CĐS SHT (nhịp 02→03) · biên giới với `sht-cds-danh-gia-hien-trang` và `sht-cds-thiet-ke-agent` · hai hạt giống mượn từ `ck:plan` (ưu tiên hoá YAGNI/MoSCoW §6, review đối kháng §8). Ca kiểm thử hành vi: `references/ca-kiem-thu.md`.
