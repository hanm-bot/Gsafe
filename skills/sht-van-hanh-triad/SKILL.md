---
name: sht-van-hanh-triad
version: 1.0
description: "Điều phối dự án nhiều bước theo bộ ba Claude – Anti – Mr. Hà (SHT-SOP-AI-01): đo trước khi lập plan, phiếu giao việc có DoD, QA Lớp 2 độc lập, RFC, Gate 3 và Sổ Cái HITL. LUÔN dùng khi nói \"giao Anti làm…\", \"đối chiếu DoD\", \"soạn RFC\", \"nghiệm thu P…\", \"duyệt Gate\", kể cả khi chỉ đưa việc cần chia bước giao người khác. KHÔNG dùng cho cổng JEV (sht-jev-cong-quyet-dinh), chuỗi 5 vai AIS48 (sht-quan-tri-dn), phỏng vấn yêu cầu (grill-me), phát hành skill."
---

# Vận hành bộ ba Claude – Anti – Mr. Hà (SHT-SOP-AI-01)

Skill này là **sổ tay tác chiến** rút từ dự án `SHT-UPSA-01` (26/09/2026, hồ sơ ở
`plans/20260926-khung-giai-quyet-van-de-3-duong-ray/`). Quy chế là luật; skill này là cách
làm đúng luật mà không lặp lại những lỗi đã trả giá.

Một câu để nhớ: **không ai tự chấm sản phẩm của mình, và không ai kết luận trên thứ mình chưa
tự chạy lại.**

> Skill là **Loại B**: chỉ có hiệu lực trong gốc dự án `G:\CHUYỂN ĐỔI SỐ SHT`, nơi có quy chế,
> script và Sổ Cái ở mục 1. Mở ở chỗ khác thì chỉ còn là tài liệu.

---

## 0. Luồng một dự án

```
Lệnh của Mr. Hà
  → [0] Hiểu đúng lệnh: viết tắt/mơ hồ → HỎI, không đoán               (§2.1)
  → [1] Thẩm định hạ tầng thật + ĐO số liệu, không đoán                (§2.2)
  → [2] Plan: bảng bước P…, người phụ trách, DoD → Gate 1 (Mr. Hà)
  → [3] Chọn đường ray cho từng ca → Gate 2 chỉ khi đổi phạm vi/chọn RFC
  → [4] Phiếu giao việc (task-XX.md) → Anti thực thi → report-XX.md
  → [5] QA Lớp 2 (Claude, độc lập) → ĐẠT | trả vòng 2 | hết 2 vòng → RFC
  → [6] Trình Gate 3 → Mr. Hà nghiệm thu → ghi Sổ Cái → lan truyền
```

Mỗi mũi tên có một người chịu trách nhiệm (§3). Mỗi quyết định của Mr. Hà vào Sổ Cái **ngay
lúc nhận lệnh**, trích nguyên văn — không ghi gộp cuối phiên.

---

## 1. File thật — tra ở đâu

| Việc | File |
|---|---|
| Quy chế (luật) | `docs/QUY_CHE_PHOI_HOP_TAC_CHIEN_CLAUDE_ANTI_SHT.md` — §3.5 QA 3 lớp, §5.2 bế tắc/RFC, §6 chốt, phụ lục biểu mẫu plan/task/report/RFC |
| Sổ Cái HITL | `docs/audit/HITL_APPROVAL_LEDGER.jsonl` — chỉ ghi qua `python .agents/scripts/ghi-log-hitl.py --append …`, kiểm bằng `--verify` |
| Ủy quyền mốc nội bộ | `.agents/config/uy-quyen-moc-noi-bo.json` |
| Bảng chọn đường ray | `sht-cds-thiet-ke-agent/references/chon-duong-ray.md` |
| Thư mục một dự án | `plans/<ngày>-<chủ-đề>/` → `plan.md`, `buoc-XX/task-XX.md`, `reports/`, `rfc/` |
| Phiếu QA | `docs/audit/<ngày>_QA-audit-<mã-dự-án>-<bước>[-vong-2].md` |
| Plan cũ cùng chủ đề | tìm trong `plans/` + Sổ Cái **trước** khi lập plan mới — có rồi thì bổ sung task |

Nhãn cổng hợp lệ và luật người ghi: quy chế §6 và `ghi-log-hitl.py` (danh sách trắng). Đừng
chép danh sách nhãn vào đây — nó đổi theo phiên bản quy chế.

---

## 2. Năm luật tư duy — mỗi luật sinh ra từ một lỗi thật

### 2.1. Lệnh mơ hồ thì hỏi, không đoán
"để lại P5 vì NDD nằm ngoài scope" bị hiểu thành "bỏ P5 — Nghị định 30 ngoài phạm vi". Thật ra
NĐ30 là quy chuẩn làm việc của Mr. Hà (đính chính `HITL-20260926-020`). Sai một chữ viết tắt →
gỡ nhầm cả một hạng mục và ghi nhầm vào Sổ Cái. → Lệnh HITL có chữ viết tắt hoặc hai cách hiểu:
**hỏi một câu sắc** trước khi ghi sổ. Đã ghi sai thì ghi bản ghi "Đính chính", không sửa dòng cũ.

### 2.2. Đo, đừng đoán
"3 loại văn bản anh dùng nhiều nhất là QĐ, CV, TTr" — đoán, bị trả "Try again". Đo tên file
toàn ổ G:\ (387 họ văn bản, 12 tháng; số đo ghi ở `buoc-13/task-13.md`) ra **BB 26 · CV 22 ·
BC 14** — TTr bằng 0. → Mọi đề xuất "cái gì quan trọng nhất / nhiều nhất" phải có số đo, ghi
cách đo và giới hạn phạm vi đo.

### 2.3. Khai báo ≠ đang chạy; không kiểm được ≠ sạch
Hook, lệnh tắt, test: chưa chạy thật thì ⚠️. Harness đột biến của QA hỏng cả ca đối chứng →
ghi "không kiểm được", **không** kết luận đạt hay trượt.

### 2.4. Kiểm nguồn trước khi phát biểu "không có"
"SOP-AI-02 không có bản .md nguồn" — sai; dòng đầu file .docx ghi rõ nguồn. → Trước khi viết
"không tồn tại / còn treo", tìm ở thư mục gốc và đọc chính file dẫn xuất.

### 2.5. Chốt kiểm là luật, không phải chướng ngại
Bên thực thi đổi style đoạn sang `Body Text` để lọt qua máy kiểm cỡ chữ — và ghi thẳng trong
report là để "vượt qua kiểm tra" (phiếu `docs/audit/2026-09-26_QA-audit-SHT-UPSA-01-P5d-vong-2.md`
H2). Máy kiểm có lỗ thì **báo vướng (RFC)**, không lách. Lách chốt kiểm nặng hơn mọi lỗi báo cáo
sai, vì nó vô hiệu hoá chính công cụ phát hiện sai.

---

## 3. Năm vai của một dự án Claude–Anti

| Vai | Ai | Việc chính | Phiếu |
|---|---|---|---|
| ① Điều phối & kiến trúc | Claude | Thẩm định, đo, lập plan, chọn ray, viết phiếu giao có DoD đo được, soạn RFC | `references/phan-vai-triad.md` §1 |
| ② Thực thi | Anti | Làm đúng phiếu, dán bằng chứng chạy lúc viết report, báo vướng thay vì lách | §2 |
| ③ QA Lớp 2 | Claude (Anti khi đảo vai) | Kiểm mtime → chạy lại độc lập → ca đối kháng → phiếu 5 mục → phán quyết | §3 (+ quy tắc chung `sht-quan-tri-dn` §6) |
| ④ Người duyệt HITL | Mr. Hà | Gate 1/3, chọn RFC, trả lời câu hỏi, bấm push | §4 |
| ⑤ Soạn văn bản NĐ30 | người được giao soạn | Sinh .docx đúng Tầng 1/2, không bịa, kiểm L4 + PDF qua Word | §5 (luật ở `sht-nen-tang-kiem-chung` §9) |

**Đảo vai:** ai viết sản phẩm thì người kia QA. Claude sửa chốt kiểm (RFC-02, RFC-03 phương án
A) thì Anti QA — Claude không tự tuyên bố nghiệm thu.

---

## 4. Phiếu giao việc — DoD chống bằng chứng giả

Một DoD tốt buộc bên thực thi nộp thứ **không chép được từ lần trước**:

- **Output nguyên văn** của mọi bộ test, chạy lúc viết report.
- **Đột biến trong thư mục tạm mới** (`tempfile`), ghi tên thư mục và thời gian chạy — QA so
  với report cũ; trùng thư mục tạm, trùng thời gian, trùng số dòng là chép.
- Đột biến phải chứng minh **test FAIL**, không chỉ "máy kiểm báo lỗi" — hai việc khác nhau.
- SHA-256 **đủ** các sổ thật, trước = sau; `find` nguyên văn chứng minh không để rác.
- Ảnh/đầu ra lưu **đúng đường dẫn** ghi trong phiếu (không ở thư mục riêng của công cụ).
- Mục "Không được làm": file được phép sửa, sổ cấm ghi, dữ liệu mẫu phải **giả lập**.
- **Ba đường dẫn bắt buộc** trong mọi phiếu/lệnh giao (Anti hoặc subagent): **thư mục làm việc thật** (không phải chỗ người giao đang đứng), **nơi ghi báo cáo**, **nơi đọc kế hoạch**. Bên nhận không thấy hội thoại — thiếu đường dẫn là báo cáo rơi sai chỗ (rule 04 §1).
- **Ghi thì tuần tự, nghiên cứu thì song song.** Trước khi giao song song, trả lời: hai bên có ghi cùng một file không? Không chắc → tuần tự (rule 04 §2). *(Hai dòng này thêm 30/09/2026, v0.29.0.)*

Phiếu viết lỏng thì lỗi là của người viết phiếu: QA ghi "của phiếu Claude", đính chính trong
task, không phạt bên thực thi.

---

## 5. Vòng QA và RFC

- **Tối đa 2 vòng.** Vòng 2 chỉ sửa đúng danh sách C1…Cn của phiếu vòng 1; phát hiện mới ngoài
  phạm vi → RFC hoặc tiền điều kiện bước sau, **không** mở vòng 3.
- **RFC 3 phương án A/B/C**, có khuyến nghị, nêu nguyên nhân gốc (thường là spec lỏng hoặc
  chốt kiểm có lỗ), ghi `rfc/rfc-XX.md`. Mr. Hà chọn → ghi Sổ Cái trước khi làm.
- Phương án "đảo vai" (Claude sửa, Anti QA) hợp khi lỗi đã khoanh chính xác và bên thực thi đã
  hết 2 vòng.
- Mỗi phiếu QA cuối có dòng **"Ghi cho M5"** — loại lỗi của bên thực thi, dùng cho lần đo lại.

---

## 6. Nghiệm thu và lan truyền

Trước khi trình Gate 3, kiểm đủ:

1. Phiếu QA cuối ĐẠT; mọi mục "không kiểm được" nêu rõ, không gộp vào "đạt".
2. Plan cập nhật dòng bước + mã HITL; các mục mở đánh số (M1, M2…) có người và mốc.
3. Lan truyền trong cùng phiên: `CLAUDE.md`, bản đồ `docs/HE-DIEU-HANH-AI-5-LOP.md`, skill
   liên quan, memory — mỗi nơi một dòng có ngày, trỏ về nguồn.
4. Văn bản .docx sinh lại từ .md (không sửa tay .docx), đạt chuẩn NĐ30 (vai ⑤).
5. Push: đưa lệnh một dòng, **Mr. Hà tự bấm**; sau đó mới cập nhật bản cài và `diff` kiểm.

Báo cáo cuối cho Mr. Hà luôn ba mục: **đã làm gì / còn tồn gì / cần anh quyết gì**.

---

## 7. Điều cấm tuyệt đối

- Không ghi Sổ Cái thay lời Mr. Hà, không ghi gộp, không sửa tay dòng cũ.
- Không tự push, không force-push, không bật tự hợp nhất.
- Không xoá: rác của bên thực thi `mv` vào `_archive/<ngày>_<lý-do>/`.
- Không chạy script đột biến/phản biện trên kho thật — chỉ trên bản sao, đo md5 sổ trước/sau.
- Không đọc workspace khách ngoài phạm vi được chỉ định; không đưa dữ liệu khách vào `THỰC HÀNH-AI/`.

---

## 8. Giới hạn đã biết (nguồn: `docs/audit/2026-09-26_GATE3-SHT-UPSA-01.md` mục mở M1–M8, 26/09/2026)

- **M5 đo lại** tỷ lệ báo cáo sai của Anti: lịch 10/10/2026 (tác vụ hẹn giờ M5 của Claude Desktop, ghi ra `docs/audit/2026-10-10_M5-DO-LAI-SHT-UPSA-01.md`).
- Ủy quyền mốc nội bộ đang ở **L1** theo `.agents/config/uy-quyen-moc-noi-bo.json` — mọi mốc vẫn cần người.
- Đường ray 2 chưa có ca thật; chỉ mở qua RFC.
- Tầng 2 NĐ30 mới có BB/CV/BC (`buoc-13/task-13.md` mục 6); QĐ, HĐ, KH, TB là đợt sau.
- Bộ ca kiểm thử hành vi cần người chấm, không chạy tự động.

Toàn bộ tư duy, việc đã làm, việc còn mở của phiên: `references/bai-hoc-upsa.md`.
Ca kiểm thử hành vi: `references/ca-kiem-thu.md`.

---

## 9. Skill đi kèm theo vai

- `sht-quan-tri-dn` §6 — quy tắc QA Lớp 2 chung (vai ③ bắt buộc đọc).
- `sht-nen-tang-kiem-chung` §9 + `references/the-thuc-nd30.md` — đường ống xuất bản và quy chuẩn NĐ30 (vai ⑤).
- `sht-cds-thiet-ke-agent` — bảng chọn đường ray; thiết kế cho khách.
- `sht-jev-cong-quyet-dinh` — khi một bước của dự án là cổng quyết định JEV.
- `grill-me` — khi lệnh ban đầu còn mơ hồ, cần phỏng vấn trước khi lập plan.
- `quan-tri-he-thong-skill` — khi đầu ra của dự án là sửa/phát hành skill.
- `sht-qa-kiem-chung-skill-hook` — khi câu hỏi là "chốt/hook có thật sự chạy không".
