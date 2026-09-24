---
name: sht-jev-cong-quyet-dinh
version: 1.0
description: "Vận hành cổng quyết định JEV nội bộ của SHT (chuỗi RAG → JEV → MCP → Workflow): lập quyết định có kiểu theo schema, cho qua cổng 3 ngả TỰ LÀM / NGƯỜI DUYỆT / CHỈ GHI LOG, ghi phản hồi CHAP_NHAN / BI_BAC / SAI có xác thực Sổ Cái HITL, và chạy ca thật trên kho nguồn khách mà không suy trạng thái từ tên file, chữ gõ sẵn hay tài liệu phân tích; kèm phiếu việc 4 vai (kiến trúc, lập quyết định, QA Lớp 2, người duyệt). LUÔN dùng khi nói 'chạy ca thật', 'JEV', 'cổng quyết định', 'hàng chờ duyệt', 'ghi phản hồi', 'chấp nhận/bác/sai JEV-…', 'vá cổng', hoặc khi agent sắp kết luận trạng thái hồ sơ khách để hành động — kể cả khi không nhắc chữ JEV. KHÔNG dùng để thiết kế use-case agentic bán cho khách (dùng sht-cds-thiet-ke-agent), không dùng cho chuỗi báo cáo quản trị 5 vai AIS48 (dùng sht-quan-tri-dn, sht-vai1..5), không thay quy tắc QA Lớp 2 chung (sht-quan-tri-dn §6)."
---

# Cổng quyết định JEV — vận hành nội bộ SHT

Skill này là **sổ tay vận hành** của chuỗi quyết định đã dựng và chạy thật trong dự án `SHT-RJMW-01` (24–25/09/2026). SHT dạy mô hình cổng quyết định cho khách (`sht-cds-thiet-ke-agent` §2–§4); skill này là chỗ SHT **tự vận hành** mô hình đó, với đúng các file, luật và bẫy đã gặp.

Một câu để nhớ: **JEV không được quyết định trên thứ nó chưa đọc, và không script nào được đánh giá thay người.**

> Skill là **Loại B**: chỉ có hiệu lực trong gốc dự án `G:\CHUYỂN ĐỔI SỐ SHT`, nơi có các script và sổ ở mục 1. Mở ở chỗ khác thì chỉ còn là tài liệu.

---

## 0. Luồng và ba điểm hiệu chỉnh

```
Ngữ cảnh (CLAUDE.md, memory, 00_NGUON-HO-SO.md)
  → Lấy thông tin: RAG tri thức ổn định + MCP CHỈ ĐỌC trạng thái sống
  → JEV: file quyết định có kiểu (schema)
  → Cổng: validator + ma trận rủi ro × tin cậy → TỰ LÀM / NGƯỜI DUYỆT / CHỈ GHI LOG
  → Hành động ghi ra ngoài: luôn qua người
  → Sổ phản hồi (xác thực Sổ Cái) ──→ hiệu chỉnh ngưỡng khi đủ mẫu
```

Ba điểm khác sơ đồ phổ biến — đừng đảo lại:
1. **MCP tách đôi.** MCP *chỉ đọc* thuộc bước lấy thông tin, đứng **trước** JEV. Để JEV quyết trước rồi mới đọc trạng thái sống là tái tạo đúng lỗi "quyết định trên dữ liệu đóng băng" (CLAUDE.md §3).
2. **Phản hồi là điều kiện của tin cậy,** không phải phần phụ cuối sơ đồ. Tin cậy do mô hình tự báo mang nhãn `TU_BAO_CHUA_HIEU_CHINH` tới khi sổ phản hồi đủ ngưỡng mẫu.
3. **Rủi ro và tin cậy là hai trục vuông góc.** Gọi đúng: "tầng rủi ro" (LOW/HIGH/CRITICAL), "tầng tin cậy" (Cao/Trung bình/Thấp); kết quả của hai trục là **"ngả"**.

---

## 1. File thật — tra ở đâu

| Việc | File | Ghi chú |
|---|---|---|
| Hợp đồng quyết định | `.agents/schemas/quyet-dinh-jev.schema.json` | Code **không đọc** file này; `test_schema_drift` giữ hai bên khớp |
| Cấu hình cổng | `.agents/schemas/jev-cau-hinh.json` | ngưỡng tin cậy, cụm trạng thái, cụm hoàn thành, `van_kien_cam_dung`, `goc_kho_nguon`, `nguon_song`, `max_data_age_days` (30), `nguong_mau_hieu_chinh` (20), regex mã |
| Validator | `.agents/scripts/kiem_quyet_dinh_jev.py` | `validate_payload()` trả **3 phần tử** (ngả, lý do, danh sách nâng ngả) và **không sửa** payload bên gọi |
| Cổng | `.agents/scripts/cong_jev.py` → `route_jev(payload, so_quyet_dinh=None, hang_cho=None)` | đường dẫn sổ đọc **lúc gọi**; ghi `_ly_do_nang_nga` ở cấp bản ghi |
| Ghi phản hồi | `.agents/scripts/ghi_phan_hoi_jev.py` | **cách duy nhất** được ghi `so-phan-hoi.jsonl` |
| Tổng hợp | `.agents/scripts/tong_hop_phan_hoi_jev.py` | tách tỷ lệ SAI và BI_BAC theo ô ma trận; từ chối đề xuất hiệu chỉnh khi dưới ngưỡng |
| Sổ | `data/_he-thong/jev/` — `hang-cho-duyet.jsonl`, `so-quyet-dinh.jsonl`, `so-phan-hoi.jsonl` | chỉ ghi thêm; **không bao giờ sửa tay** |
| Sổ Cái HITL | `docs/audit/HITL_APPROVAL_LEDGER.jsonl` qua `.agents/scripts/ghi-log-hitl.py` | kiểm toàn vẹn: `--verify` |
| Kế hoạch & phiếu QA gốc | `plans/20260924-chuoi-quyet-dinh-rjmw/`, `docs/audit/2026-09-2[45]_QA-audit-SHT-RJMW-01-*.md` | lịch sử từng chốt |

---

## 2. Hợp đồng quyết định (tối thiểu)

- `ma_quyet_dinh`: `JEV-<WS>-<YYYYMMDD>-<NNN>` (regex trong cấu hình). Số hiệu nghiệp vụ để ở `tham_chieu`. Mã chưa có trong hàng chờ/sổ.
- `cau_hoi` (câu hỏi nghiệp vụ, **không** đổi sang câu dễ trả lời hơn) · `ket_luan` (tách **văn kiện nói rõ** khỏi **suy luận**).
- `hanh_dong`: `TRA_LOI` · `DE_XUAT` · `GHI_NHAP` · `GUI_RA_NGOAI` · `GHI_HE_THONG` · `HOI_NGUOI`. `HOI_NGUOI` bắt buộc kèm `cau_hoi_cho_nguoi`; kết luận có cụm "cần hỏi người/cần xác minh" thì hành động **phải** là `HOI_NGUOI`.
- `tang_rui_ro`: `muc_do` + 3 câu hỏi có kiểu (`ai_thiet_bao_nhieu`, `gui_ra_ngoai`, `cham_tien_hoac_du_lieu_ca_nhan`). Chạm tiền hoặc gửi ra ngoài → tối thiểu HIGH.
- `bang_chung[]`: `duong_dan` **tuyệt đối, có thật** (hoặc URL có tiền tố thuộc `nguon_song`) + `do_moi` = **ngày sửa thật** của file. Liệt kê **từng văn kiện** đã đọc, không chỉ ghi một thư mục.
- `nguon_tin_cay`: `TU_BAO_CHUA_HIEU_CHINH`. `ngai_de_xuat` chỉ được điền khi trùng ngả validator tính.

---

## 3. Cổng — các chốt theo thứ tự

1. **Schema** hỏng / kiểu sai / chuỗi rỗng / mã sai định dạng → TỪ CHỐI (lỗi nội bộ cũng → TỪ CHỐI, không trả chuỗi "CRASH").
2. **Văn kiện cấm dùng** (`van_kien_cam_dung` — hiện `BCKT-L3-TMS-01`, `PRSNS-PO38-01`) → TỪ CHỐI, nêu phiếu đã cấm.
3. **Hành động luôn qua người:** `GUI_RA_NGOAI`, `GHI_HE_THONG`, `HOI_NGUOI` → NGƯỜI DUYỆT.
4. **Tự suy dữ liệu tĩnh:** chỉ cần **một** bằng chứng không thuộc `nguon_song` là coi tĩnh; lời khai `du_lieu_tinh=false` của JEV không hạ được mức này.
5. **Cụm trạng thái** (`state_phrases`, chuẩn hoá NFC + bỏ dấu + gộp khoảng trắng; cụm loại trừ được **xoá trước** rồi mới dò) khi dữ liệu tĩnh → NGƯỜI DUYỆT.
6. **Tuổi dữ liệu** vượt `max_data_age_days` → NGƯỜI DUYỆT; `do_moi` tương lai → TỪ CHỐI; `do_moi` mới hơn ngày sửa thật của file → `_canh_bao`.
7. **Cụm hoàn thành** (`completion_phrases`) → không bao giờ TỰ LÀM.
8. **Không có bằng chứng thuộc `goc_kho_nguon`/`nguon_song`** (chỉ tầng phái sinh) → không TỰ LÀM.
9. **Ma trận** (khởi đầu L1 — chặt nhất):

| | Tin cậy Cao | Trung bình | Thấp |
|---|---|---|---|
| **LOW** | TỰ LÀM (chỉ `TRA_LOI`/`GHI_NHAP`) | NGƯỜI DUYỆT | CHỈ GHI LOG |
| **HIGH** | NGƯỜI DUYỆT | NGƯỜI DUYỆT | CHỈ GHI LOG |
| **CRITICAL** | NGƯỜI DUYỆT | NGƯỜI DUYỆT | NGƯỜI DUYỆT |

Trùng mã + trùng nội dung → "đã xử lý"; trùng mã + khác nội dung → TỪ CHỐI (không lặng lẽ bỏ).

---

## 4. Phản hồi — nghĩa và cách ghi

| Kết quả | Nghĩa | Với `HOI_NGUOI` |
|---|---|---|
| `CHAP_NHAN` | Đồng ý đúng như JEV đề xuất | Câu hỏi đúng, đáng hỏi — câu trả lời ghi `--tra-loi` |
| `BI_BAC` | Không đồng ý, **JEV không sai dữ kiện** | Hỏi thừa |
| `SAI` | **JEV sai dữ kiện**: trích sai, kết luận thiếu căn cứ, nâng suy luận thành sự thật | Câu hỏi dựa trên tiền đề sai |

Chỉ tỷ lệ `SAI` dùng cho hiệu chỉnh tin cậy. `BI_BAC`/`SAI` bắt buộc `--ly-do`.

**Trình tự ghi (chỉ khi người duyệt nói thật trong phiên):**
1. `ghi-log-hitl.py --append … --command "<nguyên văn người duyệt>" --target "<…>#<ma_quyet_dinh>"` — **một bản ghi cho đúng một quyết định**; một câu duyệt nhiều quyết định thì tách nhiều bản ghi cùng nguyên văn.
2. `ghi_phan_hoi_jev.py --ma-quyet-dinh <ma> --ket-qua <…> --ma-hitl <id vừa ghi> --nguyen-van "<y hệt command_text>" [--ly-do …] [--tra-loi …]` — công cụ tự kiểm mã HITL có thật, nguyên văn khớp từng ký tự, đích sau `#` khớp **chính xác** mã quyết định.
3. `ghi-log-hitl.py --verify` + `tong_hop_phan_hoi_jev.py`.

Giữ nguyên văn cả khi có lỗi gõ ("Châp nhận") — công cụ so từng ký tự. Sổ chỉ ghi thêm; không phân loại lại mẫu cũ.

---

## 5. Luật ca thật — mỗi luật sinh ra từ một sự cố

Đầy đủ diễn biến và ca kiểm thử: `references/ca-kiem-thu.md`.

1. **Đọc `data/workspaces/<ws>/00_NGUON-HO-SO.md` toàn bộ trước.** Nó ghi kho nguồn ở đâu, và các kết luận đã được Lớp 2 kiểm lại (ví dụ hai bản Memo trùng nội dung, văn kiện bị cấm dùng).
2. **Kho nguồn ≠ workspace.** Workspace là tầng phái sinh; bảng nhắc việc, phương án đàm phán, báo cáo tuần **đóng băng ở ngày soạn**. Mọi trạng thái trong đó là phát biểu **cần truy nguồn**, không phải căn cứ.
3. **Không suy trạng thái ký/gửi từ tên file hay chữ gõ sẵn.** Tên kiểu "(Finallized để ký)" và dòng chữ gõ sẵn ở khối ký của một bản dự thảo đều không phải chữ ký. PDF → render **đúng trang khối ký chính** bằng PyMuPDF và xem ảnh; docx → kiểm `word/media/` có ảnh nhúng không. DA-DOI-CHIEU-NGUON: hai ví dụ trên là mẫu bẫy đã gặp ở ca NDA ATG 24/09, không phải phát biểu về hồ sơ.
4. **"Không tìm thấy" không phải "chưa có".** Viết "không tìm thấy trong <phạm vi đã tìm>" và liệt kê phạm vi. Tệp ghi âm → "chưa nghe".
5. **Hai tài liệu nội bộ nói khác nhau** → nêu cả hai kèm ngày, kiểm lại bằng văn kiện gốc; nói rõ đã so ở lớp nào (văn bản / ảnh render / chữ ký) và lớp nào chưa.
6. **Không lấy bản nháp của chính hệ thống làm bằng chứng.** Một dòng do Claude/Anti vừa soạn không chứng minh được một bên thứ ba đã quyết định gì (ca A14, 25/09).
7. **Hai tệp cùng tên chưa chắc cùng nội dung** — so trước khi chọn "bản mới nhất" (ca PO-38 gốc vs `Review L2`: một bản nội bộ, một bản để hai bên rà).
8. **Tài liệu đưa đối tác phải lọc ghi chú nội bộ** (các đoạn "Lưu ý nội bộ", back-to-back, mức phạt, lý do đàm phán) — quét cả header, footer, comment, tracked changes, chữ ẩn, `docProps`.
9. **Không để văn bản trích từ hồ sơ nguồn nằm trong kho dự án** (`plans/`, gốc kho). File tạm ở thư mục tạm hệ điều hành.
10. **Gặp rào chặn công cụ thì báo lại**, không tự vòng qua; quyền đọc kho nguồn bằng Python chỉ theo phạm vi Mr. Hà đã cho (ghi trong `00_NGUON-HO-SO.md`).

---

## 6. Phân vai — mỗi người một phiếu việc

| Vai | Ai | Việc chính | Phiếu |
|---|---|---|---|
| A — Kiến trúc & soạn task | Claude | Chốt phạm vi ca, cài bẫy mà **không** đưa đáp án, viết DoD đo được | `references/phan-vai-jev.md` §A |
| B — Lập quyết định ca thật | Anti | Đọc nguồn, trích nguyên văn, lập file quyết định, chạy cổng, report trung thực | §B |
| C — QA Lớp 2 | Claude | Kiểm mtime → chạy lại độc lập trên bản sao → phản biện → phiếu; không tự chấm bản mình soạn | §C (+ quy tắc chung `sht-quan-tri-dn` §6) |
| D — Người duyệt HITL | Mr. Hà | Chọn phạm vi, trả lời câu hỏi `HOI_NGUOI`, ra CHAP_NHAN/BI_BAC/SAI, quyết RFC | §D |

Một người kiêm nhiều vai thì **không** được làm C cho chính sản phẩm của mình ở A hoặc B — đảo vai để người khác kiểm (ca PO-38 v2, 25/09).

---

## 7. Điều cấm tuyệt đối

- Không script nào tự ghi `ket_qua` thay người duyệt (sự cố P5, 24/09: phản hồi "Mr. Hà CHAP_NHAN" viết cứng, cách lúc định tuyến 1 ms).
- Không sửa tay dòng nào trong 3 sổ JEV hay Sổ Cái; sửa sai bằng cách `mv` sổ vào `_archive/` rồi ghi lại qua công cụ, có quyết định của Mr. Hà.
- Test và script phản biện **không** được ghi vào sổ thật: đường dẫn sổ truyền tham số, chạy trên thư mục tạm, đo md5 sổ trước/sau.
- Không gửi gì ra ngoài; `GUI_RA_NGOAI` chỉ là đề xuất trong hàng chờ.

---

## 8. Chưa làm được / giới hạn đã biết

- **MCP chỉ đọc CRM (P2) chưa có token** → mọi bằng chứng CRM là tĩnh; `nguon_song` đang rỗng.
- **Tin cậy chưa hiệu chỉnh:** sổ phản hồi 7/20 mẫu (25/09/2026 01:15). Ô "LOW × Cao" — ô duy nhất được TỰ LÀM — đã có 1/4 SAI.
- **Engine 24/7 (n8n, Telegram) vẫn là mô tả**; cổng chỉ chạy khi có người/agent gọi.
- **Danh sách cụm từ không bao giờ đủ** — rào chắn cuối vẫn là luật 5.4 và CLAUDE.md §3.
- `van_kien_cam_dung` do người cập nhật tay theo phiếu QA; cổng không tự phát hiện tài liệu AI đứng tên đơn vị nghiệp vụ.

Toàn bộ tư duy, việc đã làm, việc chưa làm của phiên: `references/bai-hoc-rjmw.md`.

---

## 9. Dùng kèm

- `sht-quan-tri-dn` §6 — quy tắc QA Lớp 2 chung khi thẩm định sản phẩm của Anti (vai C dùng kèm).
- `sht-nen-tang-kiem-chung` — một bản có hiệu lực, bàn giao, phân loại phát biểu Dữ kiện/Suy luận/Giả định.
- `sht-cds-thiet-ke-agent` — khi cần **thiết kế** cổng tương tự cho khách (skill này chỉ **vận hành** cổng của SHT).
- `sht-qa-kiem-chung-skill-hook` — khi câu hỏi là "hook/chốt có thật sự chạy không".
- `anthropic-skills:docx`, `anthropic-skills:pdf` — khi lọc/render văn kiện.
