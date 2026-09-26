# Tổng hợp phiên SHT-UPSA-01 (26/09/2026) — tư duy · ý tưởng · đã làm · còn mở

> DA-DOI-CHIEU-NGUON: trạng thái và mã trong file này truy về `plans/20260926-khung-giai-quyet-van-de-3-duong-ray/plan.md`, các phiếu `docs/audit/2026-09-26_QA-audit-SHT-UPSA-01-*.md`, `docs/audit/2026-09-26_GATE3-SHT-UPSA-01.md` và 28 bản ghi `HITL-20260926-001`…`-028` trong `docs/audit/HITL_APPROVAL_LEDGER.jsonl` (đối chiếu 26/09/2026 23:50). Là ảnh chụp tại ngày ghi — đối chiếu lại trước khi trích.

## 1. Tư duy cốt lõi

1. **Thẩm định ảnh/kiến trúc người dùng gửi với hạ tầng thật trước khi dựng.** Khung "Unified Problem-Solving Architecture" được ánh xạ vào skill và script đã có; phần lớn khung đã tồn tại rải rác — việc thật là **nối dây bàn giao** giữa các skill và thêm **bảng chọn đường ray**, không phải dựng mới.
2. **Đo, đừng đoán** — xếp hạng loại văn bản bằng số đo tên file, không bằng cảm giác.
3. **Lệnh mơ hồ → hỏi.** Một chữ viết tắt ("NDD") làm gỡ nhầm cả một hạng mục.
4. **Không ai tự chấm mình; đảo vai khi người sửa là QA.**
5. **Tối đa 2 vòng, rồi RFC** — không dời cột gôn, không vòng 3.
6. **Chốt kiểm có lỗ thì vá chốt, không lách chốt.** Định nghĩa "đoạn nội dung" theo **vai trò đoạn**, không theo **tên style**.
7. **Chuẩn nghiệm thu .docx phải kiểm được bằng máy:** L4 exit 0 và PDF xuất qua Word chỉ nhúng Times New Roman (+ Consolas cho khối mã).
8. **Nguồn luật phải là bản gốc chính thức** — 2/3 link trong ảnh người dùng gửi sai; bản đúng là bản ký số trên `datafiles.chinhphu.vn` (76 trang).

## 2. Đã làm (theo bước)

| Bước | Nội dung | Kết quả |
|---|---|---|
| P1–P3 | Bản đồ khung trong `docs/HE-DIEU-HANH-AI-5-LOP.md` §1c · nối dây 6 skill · bảng `chon-duong-ray.md` | ✅ Gate 2 `-004`, phát hành 0.24.0 |
| P4 | Chạy thử 2 ca: báo cáo tuần Ban CĐS (Ray 1), quy trình QA Claude–Anti (Ray 3) | ✅ Gate 3 `-009` |
| P6 | RFC-01 PA B: SOP-AI-01 1.2 (tách nhãn Gate 2, §3.6 ủy quyền mốc nội bộ), `ghi-log-hitl.py` chốt nhãn | ✅ (RFC-02 PA A, đảo vai) |
| P7 / P8 | M1, M1b: siết chốt ủy quyền (`target_doc` mã hoá, NFKC, thư mục gốc) | ✅ `-012`, `-014` |
| P9 | M8: nhãn `PB Gate 1/2/3` + `phong_ban`; SOP 1.3 | ✅ `-016`, Gate 3 `-017` |
| P10 | M7: báo cáo tuần Ban CĐS + lệnh `/bao-cao-tuan` | ✅ `-019` (lệnh chưa chạy thật lần đầu) |
| P5a | Đọc bản gốc NĐ30, spec `the-thuc-nd30.md` có số trang | ✅ quyết định `-021` |
| P5b/c | L4 nhóm 6 (Tầng 1) + bộ sinh Word Tầng 1 | ✅ `-022` |
| P5e | Sinh lại SOP-AI-01, SOP-AI-02 (từ `.agents/rules/agent_design_standards.md`), BBVH-01 đạt NĐ30 | ✅ `-025` |
| P5d | Tầng 2 BB/CV/BC: `sinh_van_ban_nd30.py` + L4 nhóm 7 `--loai` | ⏳ hết 2 vòng → RFC-03 PA A `-027`; Claude đã sửa, chờ Anti QA đảo vai (`reports/report-13-r.md`) |
| — | Phát hành sht-skills 0.24.0 → 0.24.2 (đã push), 0.25.0 (commit chưa push) | xem Sổ đăng bạ |

## 3. Ý tưởng đã chốt nhưng chưa làm

- Tầng 2 cho QĐ, HĐ, KH, TB — theo số đo, đợt sau.
- Nâng ủy quyền mốc nội bộ từ L1 lên L2 — chỉ khi M5 cho số liệu tốt.
- Đường ray 2 — chỉ qua RFC khi có ca thật.

## 4. Còn mở (nguồn: phiếu Gate 3 mục M, plan.md)

| Mục | Việc | Người |
|---|---|---|
| P5d | Anti QA đảo vai → Mr. Hà nghiệm thu | Anti · Mr. Hà |
| M2 | Tải gói plugin mới lên Organization library (Cowork) | Mr. Hà |
| M3 | Kiểm skill tự nạp trong phiên mới | Mr. Hà mở phiên · Claude kiểm |
| M5 | Đo lại 10/10/2026 (tác vụ hẹn giờ M5) | Claude |
| M6 | B1 thiếu skill cho "dữ liệu vận hành nội bộ" — bổ sung vào `sht-vai1-harvester` hay `sht-quan-tri-dn` | Mr. Hà quyết |
| — | `/bao-cao-tuan` chạy thật lần đầu | Mr. Hà |

## 5. Lỗi của chính Claude trong phiên (để không lặp)

| Lỗi | Hậu quả | Luật rút ra (SKILL.md) |
|---|---|---|
| Hiểu "NDD" thành "NĐ30 ngoài phạm vi" | Gỡ nhầm P5, ghi `-005` sai, phải đính chính `-020` | §2.1 |
| Đoán top-3 loại văn bản | Bị trả "Try again" | §2.2 |
| Kết luận SOP-AI-02 không có .md nguồn | Ghi sai vào bản đồ, phiếu QA, plan | §2.4 |
| QA P5b chỉ thử style `Normal` | Lỗ `Body Text` sống qua P5b, bị khai thác ở P5d | phiếu vai ③ |
| Phiếu P5d không định nghĩa "đoạn nội dung"; bắt báo THIẾU khoá tuỳ chọn | Hai lỗi thuộc về phiếu | phiếu vai ① |
