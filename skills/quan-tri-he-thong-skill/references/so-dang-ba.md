# SỔ ĐĂNG BẠ

*Cập nhật lần cuối: 14/09/2026 — 19 skill, cả 19 đã đăng ký. 0 lỗi mức CAO. Phiên bản v0.18.2.*

| Skill | Tầng | Sở hữu logic | Dùng chung với | Không đụng tới |
|---|---|---|---|---|
| `sht-nen-tang-kiem-chung` | **0** | Lan truyền hiệu chỉnh · đổi tên hàng loạt an toàn (+ cụm bảo vệ) · một-bản-có-hiệu-lực + **ghi tên bản bị thay thế vào bản có hiệu lực trước khi xóa (§3)** · **ghi đúng thư mục đích (§3.1)** · đặt câu hỏi ngược với nguồn, **kể cả tài liệu phân tích của phiên trước (§4)** · checklist bàn giao chung · **kết xuất theo người đọc (5 dạng báo cáo; 2 đường xuất PDF theo công cụ có thật; dò trang trống bằng máy; quét `grep` xác minh — §6)** · **tự kiểm trước khi báo xong (§7)** | **Mọi** skill tầng 1 — nạp kèm trong mọi phiên có bàn giao file | Nghiệp vụ cụ thể của bất kỳ miền nào |
| `quan-tri-he-thong-skill` | **0** | Ranh giới giữa các skill, audit, phân tầng, quy trình nâng cấp, Sổ đăng bạ · khung ca kiểm thử hành vi (§9b) | `skill-creator` để viết nội dung bên trong một skill | Nội dung nghiệp vụ bên trong từng skill |
| `chuan-hoa-du-lieu-du-an` | 1 | 4 cổng kiểm transcript · xác định người phát ngôn · đối chiếu chéo · truy vết timestamp · metadata & epoch ẩn · giữ thể thức + watermark gốc · từ vựng trạng thái | `sht-nen-tang-kiem-chung`; `chuan-hoa-du-lieu-nhansu` khi tài liệu có tên người | Chấm điểm ứng viên; dữ liệu CRM; thẩm quyền QĐ; hợp đồng CNTT |
| `chuan-hoa-du-lieu-nhansu` | 1 | Chốt danh tính với QĐ/hợp đồng · nhiều người trùng tên · một người kiêm nhiệm nhiều vai | `sht-qd-nhansu-alignment` khi soạn QĐ; `sht-xacthuc-baocao-hoatdong` khi hồ sơ có số liệu | Thẩm quyền/mô hình tổ chức; ứng viên chưa tuyển |
| `sht-qd-nhansu-alignment` | 1 | Đối chiếu thẩm quyền & quan hệ báo cáo giữa các QĐ (7 khía cạnh) · cơ chế Điều chỉnh vs Thay thế toàn bộ · thể thức QĐ | `chuan-hoa-du-lieu-nhansu` chốt tên trước; `sht-xacthuc-baocao-hoatdong` nếu Căn cứ có số liệu | Xác minh tên riêng; tính đúng đắn của số liệu |
| `sht-xacthuc-baocao-hoatdong` | 1 | Truy số về truy vấn gốc · 4 bẫy dữ liệu Turso · thứ tự truy nguyên nhân khi lệch · nhãn ✅/⚠️/❓ | `sht-normalize-account` khi đếm khách hàng/chi nhánh; `sht-qd-nhansu-alignment` khi số vào QĐ | Gộp/rollup account; thể thức văn bản |
| `sht-normalize-account` | 1 | Gộp account theo Mã Dự Án (`ma`) · parser mã CN · tự kiểm số chi nhánh | `sht-xacthuc-baocao-hoatdong` khi số liệu vào báo cáo | Danh tính người; tính đúng đắn của doanh số |
| `chuan-hoa-du-lieu-tuyen-dung` | 1 | Săn CV & lọc cổng tuyển dụng · chấm ASK có bằng chứng (2 phiên bản trọng số: A30/S40/K30 ứng viên thường, A60/S30/K10 cán bộ quản lý) · đối chiếu 3P · **soạn JD mới kèm khảo sát lương thị trường 2 lớp khi chưa có JD (§2b)** · **mẫu chấm vai kỹ thuật/tích hợp: ánh xạ ASK↔domain, tiêu chí bối cảnh khớp đối tác, mâu thuẫn domain-fit vs ASK-total (`references/mau-cham-vai-tich-hop.md`)** · scorecard + infographic | `sht-nen-tang-kiem-chung`; `chuan-hoa-du-lieu-nhansu` khi ứng viên vào hồ sơ nội bộ | Hồ sơ nhân sự đã tuyển |
| `ra-soat-hop-dong-vendor` | 1 | Gap analysis SoW/BRD · chuỗi Mua/Bán back-to-back · license & rủi ro pháp lý/kỹ thuật · đo tỷ lệ copy phụ lục & diff phiên bản · **tình trạng ký & gán toạ độ tệp-phiên bản cho từng khiếm khuyết (§0.2b)** · **đồng hồ hiệu lực (§0.3)** · **hệ tác nhân độc lập theo lớp (§0.4)** · **mâu thuẫn nội bộ trong cùng một văn kiện (§1.4b)** · **ba nhãn phát biểu: dữ kiện / vị thế / suy luận** | `sht-nen-tang-kiem-chung`; `chuan-hoa-ho-so-tai-lieu` khi có PDF scan; `superpowers:dispatching-parallel-agents` cho cơ chế dispatch chung | Dự án XDCB; hồ sơ nhân sự; thẩm quyền QĐ |
| `chuan-hoa-ho-so-tai-lieu` | 1 | **Chuyển đổi & bóc tách mọi định dạng file (chủ sở hữu)** · trích dẫn có toạ độ · xếp hạng độ vững luận cứ · viết bản đối ngoại không đối kháng | `sht-nen-tang-kiem-chung`; `ra-soat-hop-dong-vendor` khi hồ sơ có hợp đồng CNTT | Soạn QĐ nhân sự; săn CV tuyển dụng; dự án XDCB |
| `sht-cds-danh-gia-hien-trang` | 1 | Đánh giá hiện trạng & DMI 6 trụ cột · kiểm toán chất lượng dữ liệu 6 chiều · bản đồ điểm nghẽn As-Is · thẩm định Cổng G1 | `sht-nen-tang-kiem-chung` khi xuất báo cáo hiện trạng & bàn giao; `sht-cds-thiet-ke-prd` (bàn giao bảng điểm nghẽn As-Is sang Giai đoạn 03) | Rà soát hợp đồng CNTT; chuẩn hóa account CRM; bóc tách hồ sơ scan |
| `sht-cds-thiet-ke-prd` | 1 | Thiết kế quy trình To-Be · soạn PRD 10 khối (mẫu ở references) · truy vết yêu cầu↔điểm nghẽn/KPI · NFR tuân thủ NĐ13/NHNN + sơ đồ luồng dữ liệu · đặc tả dữ liệu & tích hợp · MoSCoW & scope Pilot · review đối kháng PRD · nhánh hướng thi công trung lập | `sht-cds-danh-gia-hien-trang` (nhận bảng điểm nghẽn As-Is làm đầu vào); `sht-cds-thiet-ke-agent` (hand-off khi hướng chốt là AI agent); `sht-nen-tang-kiem-chung` khi bàn giao | Đo DMI/đánh giá hiện trạng; thiết kế nội tại AI agent; rà soát PRD/SoW hợp đồng vendor; dựng UI từ PRD |
| `sht-cds-thiet-ke-agent` | 1 | Khai báo agent 3 chiều Purpose/Scope/Boundaries · 3 tầng confidence · Tiered Governance L1–L3 · bộ ca kiểm thử có ca gài · vòng đời sandbox→pilot→production→review | `sht-cds-danh-gia-hien-trang` (bắt buộc qua Giai đoạn 01 trước); `sht-cds-thiet-ke-prd` (PRD là đầu vào khi hướng thi công là agent); `sht-nen-tang-kiem-chung` khi bàn giao | Đo DMI/đánh giá hiện trạng; rà soát hợp đồng vendor; chuẩn hóa dữ liệu CRM |
| `sht-quan-tri-dn` | 1 | **Tầm điều phối cả đội** (chủ sở hữu): Cổng I/O 2 tầng (script + hook cấp user) · ngân sách token tổng 5 vai · Chốt chặn HITL Gate 1-3 & Sổ cái SHA-256 · quy tắc thẩm định QA Lớp 2 đối chiếu thực nghiệm (không tin báo cáo tự chấm, nghi ngờ HITL bất thường) · nhân rộng 9 phòng ban qua Blueprint + Workshop B5 | `sht-nen-tang-kiem-chung` khi bàn giao/xuất báo cáo; `sht-xacthuc-baocao-hoatdong` khi đối chiếu số liệu phản biện; trỏ xuống `sht-vai1..5` khi một nhân sự chỉ cần đúng một vai | Xác thực báo cáo doanh số/CRM thuần túy; xuất báo cáo PDF in ấn chuyên dụng; rà soát hợp đồng vendor; tuyển dụng/JD; quy trình chi tiết từng bước của một vai riêng lẻ (chủ sở hữu là `sht-vai1..5`) |
| `sht-vai1-harvester` | 1 | **Tầm cá nhân một vai** (chủ sở hữu): quy trình thực thi 4 bước Thu thập/Làm sạch/Masking Vùng Đỏ của riêng Vai 1 | `sht-quan-tri-dn` §0 cho cơ chế Cổng I/O đầy đủ; vai kế tiếp `sht-vai2-analyzer` | Điều phối cả chuỗi 5 vai (`sht-quan-tri-dn`); phân tích/báo cáo/phản biện |
| `sht-vai2-analyzer` | 1 | **Tầm cá nhân một vai** (chủ sở hữu): quy trình thực thi 4 bước Phân tích điểm nghẽn/5 Whys/Grounding của riêng Vai 2 | `sht-quan-tri-dn`; vai trước `sht-vai1-harvester`; vai sau `sht-vai3-dispatcher`/`sht-vai4-reporter` | Điều phối cả chuỗi 5 vai; làm sạch dữ liệu thô; soạn báo cáo |
| `sht-vai3-dispatcher` | 1 | **Tầm cá nhân một vai** (chủ sở hữu): quy trình thực thi 4 bước Đôn đốc/soạn thông điệp nhắc việc/lập lịch của riêng Vai 3 | `sht-quan-tri-dn`; chạy song song `sht-vai2-analyzer`; vai sau `sht-vai4-reporter` | Điều phối cả chuỗi 5 vai; phân tích điểm nghẽn; soạn báo cáo điều hành |
| `sht-vai4-reporter` | 1 | **Tầm cá nhân một vai** (chủ sở hữu): quy trình thực thi 4 bước soạn Báo cáo Điều hành 4 phần AIS48 của riêng Vai 4 | `sht-quan-tri-dn`; vai trước `sht-vai1..3`; vai sau (bắt buộc) `sht-vai5-critic` | Điều phối cả chuỗi 5 vai; phân tích điểm nghẽn; phản biện/duyệt |
| `sht-vai5-critic` | 1 | **Tầm cá nhân một vai** (chủ sở hữu): quy trình thực thi 4 bước Phản biện đối kháng 3 tầng của riêng Vai 5; ghi Sổ Cái trỏ về `sht-quan-tri-dn` §2/§6 (không sở hữu lệnh ghi log) | `sht-quan-tri-dn` §2/§6 cho cơ chế Sổ Cái & bài học QA đầy đủ; vai trước (bắt buộc) `sht-vai4-reporter` | Điều phối cả chuỗi 5 vai; soạn bản nháp báo cáo ban đầu |

**Đã đóng (14/09/2026 — v0.18.0, MINOR — THÊM 5 SKILL):**

Nguồn: phiên thẩm định QA nhiều vòng cho kế hoạch nâng cấp kiến trúc AIS48 (`docs/audit/2026-09-14_QA-audit-*.md`) + yêu cầu song song của anh Hà cho Anti tạo trực tiếp 5 skill theo từng vai (không qua `save_skill`, ghi thẳng vào nguồn plugin). **Quyết định kiến trúc: +5 skill mới** — mỗi vai trong Đội 5 Agent (Blueprint `Playbooks-Thuc-Chien/01_Cau-truc-Workspace-9-Phong-ban/BLUEPRINT_DOI_5_AGENT_PHONG_BAN.md`) nay có skill riêng cho nhân sự chỉ cần tự tay làm đúng một vai, tách khỏi `sht-quan-tri-dn` vốn chỉ mô tả tầm điều phối cả đội.

- **`sht-vai1-harvester` .. `sht-vai5-critic` (MỚI, tầng 1):** quy trình thực thi 4 bước của từng vai (Thu thập & Cổng I/O · Phân tích & Grounding · Đôn đốc & lập lịch · Báo cáo Điều hành 4 phần · Phản biện 3 tầng & Sổ Cái). Tạo bởi Anti trực tiếp trong nguồn plugin (không qua `save_skill`) theo yêu cầu của anh Hà, song song với việc Claude cập nhật `sht-quan-tri-dn`.
- **Audit lần đầu phát hiện 1 mức CAO (E8, cả 5 skill chưa đăng ký) + 10 E6 (description mở đầu gần trùng khuôn "Kỹ năng chuyên môn Nhân sự Vai N") + 5 E3 (đảo cô lập, không skill nào trỏ qua lại với `sht-quan-tri-dn` hay với nhau).**
- **Đã sửa theo §3 "Chốt chủ sở hữu":** Cổng I/O (2 tầng, bài học `"/test"`) và cơ chế Sổ Cái HITL/ghi log vẫn thuộc `sht-quan-tri-dn` (§0, §2, §6) — nội dung trùng ở `sht-vai1-harvester` Bước 2 và `sht-vai5-critic` Bước 4 được rút gọn thành con trỏ, không lặp lại lệnh/bài học. Mỗi vai giữ đúng phần **thực thi riêng** của mình (không ai khác có).
- **Sửa E6 bằng chuyên biệt hoá mở đầu description** (theo mẹo §1): đổi khuôn chung "Kỹ năng chuyên môn Nhân sự Vai N (...)" thành động từ + đối tượng riêng của từng vai ("Bóc tách & làm sạch...", "Phân tích điểm nghẽn...", "Đôn đốc tiến độ...", "Soạn Báo cáo Điều hành...", "Phản biện độc lập..."), mỗi description đều có vùng loại trừ trỏ rõ tới `sht-quan-tri-dn` (điều phối cả chuỗi) và 2 vai liền kề.
- **Sửa E3 bằng khối `> **Quan hệ:**` ở đầu mỗi skill** (vai trước/vai sau/điều phối tổng) + `sht-quan-tri-dn` §1 và description trỏ ngược xuống cả 5 vai.
- **10 cảnh báo E4 còn lại (dòng `Mã định danh chuẩn AIS48: ... · Hạn mức: X`) là tín hiệu giả theo §1** — cùng một khuôn định dạng số liệu có chủ đích (mỗi vai tự nêu mã định danh + ngân sách token riêng), không phải logic bị trùng chủ sở hữu. Giữ nguyên, không đục thêm (§9).
- **Đăng bạ & Manifest:** Tăng version MINOR `0.17.1` → `0.18.0`. Cập nhật Sổ đăng bạ đủ 19 hàng khớp 19 thư mục trong `skills/`.

**Đã đóng (14/09/2026 — v0.18.1, PATCH):**

Nguồn: anh Hà thử upload `sht-skills-0.18.0.plugin` lên marketplace desktop app → bị từ chối: *"Plugin description must be at most 500 characters"*. `description` trong `.claude-plugin/plugin.json` là 529 ký tự — vượt trần **của chính ứng dụng cài đặt** (khác trần 1024 ký tự áp cho `description` của từng SKILL.md, §4). `release.py` không có cổng nào kiểm giới hạn này nên gói 0.18.0 đóng "sạch" theo 9 cổng nhưng vẫn bị app từ chối khi cài — lỗ hổng phạm vi kiểm giống loại đã từng xảy ra với E7-E11 (§7): công cụ chỉ kiểm được đúng phạm vi nó biết trước.

- **Rút `description` plugin từ 529 → 396 ký tự**, giữ nguyên đủ ý (19 skill, 5 vai, các miền nghiệp vụ chính), chỉ cắt bớt liệt kê.
- **Dọn E9 phát sinh giữa chừng:** gói `sht-skills-0.18.0.plugin` từng bị đóng nhầm vào trong chính thư mục nguồn (`SKILL file/sht-skills/`) do gọi `release.py` không chỉ định `--out` ra ngoài — đã dọn sang `SKILL file/_plugin-builds/` (không xoá, theo luật cứng #3) và từ nay **luôn đóng gói ra thư mục `_plugin-builds/` bên ngoài nguồn**, không đóng vào chính `sht-skills/`.
- **Ghi nhận việc còn thiếu ở `release.py`:** chưa có cổng kiểm giới hạn ký tự của `description` cấp plugin (500) — chỉ có cổng 3 kiểm manifest hợp lệ về cấu trúc, không kiểm độ dài theo giới hạn thật của app cài đặt. Để dịp sửa `release.py` sau, không sửa vội trong phiên này (đang ưu tiên ra bản cài được ngay).
- **Phiên bản: PATCH** (`0.18.0` → `0.18.1`) — không thêm/bớt/di chuyển skill, chỉ sửa độ dài một trường trong manifest.

**Đã đóng (14/09/2026 — v0.18.2, PATCH):**

Nguồn: thẩm định ngược sau phiên nâng cấp Đội 5 Agent — phát hiện `doi_chieu_ban.py` (công cụ đối chiếu 3 bản: nguồn/gói/bản cài, dùng ở cổng 0 của `release.py`) hardcode tên plugin `'sht-skills'` khi dò bản đang cài, thay vì đọc từ manifest của chính thư mục nguồn đang được kiểm. Sự cố thật: chạy `release.py` cho plugin `grill-me` nhưng công cụ lại đi so với bản cài của `sht-skills`, báo nhầm "thiếu 14 skill".

- **Sửa `tim_ban_dang_chay()` gọi từ `main()` trong `doi_chieu_ban.py`:** đọc `name` từ `.claude-plugin/plugin.json` của thư mục nguồn đang kiểm để xác định tên plugin cần dò bản cài; đọc lỗi hoặc thiếu trường thì lùi về mặc định `'sht-skills'` để không phá hành vi hiện có.
- **Phạm vi ảnh hưởng:** chỉ tác động khi dùng `release.py`/`doi_chieu_ban.py` cho một plugin khác `sht-skills` (ví dụ `grill-me`) đang cùng máy có bản `sht-skills` cài sẵn. Không đổi hành vi đóng gói `sht-skills` chính nó.
- **Phiên bản: PATCH** (`0.18.1` → `0.18.2`) — chỉ sửa lỗi logic một script nội bộ, không thêm/bớt/di chuyển skill.

**Đã đóng (11/09/2026 — v0.17.1, PATCH):**

Nguồn: Đồng bộ tài liệu sau khi gỡ bỏ cờ `--approve-gate3` khỏi `.agents/scripts/sht_enterprise_squad_engine.py` và chuyển `--test-hitl` sang chế độ DRY-RUN (không tự động ghi Sổ Cái thật), căn cứ sự cố `HITL-20260911-005/006` và bản đính chính `HITL-20260911-007`.

- **`sht-quan-tri-dn`:** Xoá bỏ mô tả cờ `--approve-gate3` khỏi `SKILL.md`. Cập nhật mô tả `--test-hitl` (chế độ DRY-RUN, in lệnh mẫu không ghi Sổ Cái thật). Ghi rõ nguyên tắc bất di bất dịch: mọi phê duyệt Gate 3 phải do chính Mr. Hà gõ trực tiếp trong phiên làm việc thật với Claude hoặc Antigravity, không qua cờ CLI tự động của engine.
- **Manifest:** Tăng version PATCH `0.17.0` → `0.17.1` trong `.claude-plugin/plugin.json`.

**Đã đóng (11/09/2026 — v0.17.0, MINOR — THÊM SKILL):**

Nguồn: Kế hoạch triển khai Đội 5 Agent Quản trị Doanh nghiệp SHT (`plans/20260911-doi-agent-quan-tri-dn/`), nghiệm thu Gate 3 (`HITL-20260911-001/002`). **Quyết định kiến trúc: +1 skill mới** — đóng gói quy trình điều phối 5 Agent quản trị vận hành nội bộ theo chuẩn AIS48.

- **`sht-quan-tri-dn` (MỚI, tầng 1, Giai đoạn 03/04):** Điều phối 5 vai (Thu thập SHT-CORP-HARVESTER, Phân tích SHT-CORP-ANALYST, Nhắc việc SHT-CORP-REMINDER, Báo cáo SHT-CORP-REPORTER, Phản biện SHT-CORP-AUDITOR), Lưới lọc an toàn Vùng Đỏ (tên tiếng Việt, PII, Lương), Quản trị ngân sách Token (Soft Cap 80%, Hard Stop 100%), Chốt chặn HITL Gate 3 ghi nhận Sổ Cái `HITL_APPROVAL_LEDGER.jsonl` (SHA-256).
- **Đăng bạ & Manifest:** Tăng version MINOR `0.16.5` → `0.17.0` trong `plugin.json` (14 skill). Cập nhật Sổ đăng bạ đủ 14 hàng khớp 14 thư mục trong `skills/`.


**Đã đóng (10/09/2026 — v0.16.5, PATCH):**

Nguồn: pilot G30 nội bộ "Sàng CV PO Payment" (kế hoạch `plans/20260910-ap-dung-cd4-cd5-noi-bo/`, workspace `data/workspaces/Pilot_Sang_CV/`). **Quyết định kiến trúc: 0 skill mới** — bài học thuộc đúng miền săn CV/chấm ASK/soạn JD của `chuan-hoa-du-lieu-tuyen-dung`, theo §8 mặc định nghiêng về mục mới trong skill cũ.

- **`chuan-hoa-du-lieu-tuyen-dung` +1 reference `mau-cham-vai-tich-hop.md`** cho vai kỹ thuật/tích hợp (PO/BA payment, sở hữu đặc tả API): (1) mẫu ánh xạ ASK↔domain JD; (2) tiêu chí bối cảnh **khớp cựu công ty ứng viên ↔ đối tác tích hợp trong JD** (ca thật: ứng viên từng làm VTC Pay = đúng đối tác SHT); (3) cách trình **mâu thuẫn domain-fit vs tổng ASK** cho người quyết, không tự nâng/hạ trọng số. Thân SKILL.md +1 con trỏ ở §5.1 (273 → 275 dòng, vẫn < 300).
- **`references/ca-kiem-thu.md` +2 ca** (TD-08 mâu thuẫn domain-fit/ASK-total; TD-09 loại trừ vai payment thiếu đặc tả API). **Trạng thái: CHƯA VẬN HÀNH** — chờ người chấm độc lập theo §9b luật 3 (không để agent tự chạy tự chấm). Ghi chú: pilot G30 do chính Claude chạy tay là *bằng chứng phương pháp*, chưa thay được phép chấm độc lập.
- **Phiên bản: PATCH** (0.16.4 → 0.16.5) — chỉ bổ sung nội dung trong đúng chủ sở hữu, không thêm/bỏ skill, không di chuyển logic. Kiểm E4/E6 với `sht-chuan-hoa-ho-so-ung-vien`/`sht-quy-trinh-tuyen-dung` khi audit.

**Đã đóng (07/09/2026 — v0.16.3, PATCH):**

- **E10 ở `sht-cds-thiet-ke-prd` — ĐÃ ĐÓNG.** Ghi nhận ở v0.16.0 mức THẤP theo §9 (không sửa ngay). Phiên này người dùng yêu cầu xử lý E10 nên đằng nào cũng mở skill ra sửa — đúng điều kiện §9 để đụng cảnh báo THẤP. Rút description **994 → 871 ký tự** (dưới ngưỡng THẤP 952, biên 81; dưới trần cứng 1024 là 153) bằng cách cắt phần liệt kê năng lực và bớt 2 trigger ví dụ (`"user story cho khách"`, `"chốt scope pilot"`), **giữ nguyên toàn bộ vùng loại trừ và cả 4 quan hệ skill**. Audit sau khi sửa: sạch, 0 phát hiện. Phát hành qua `release.py` chín cổng.

**Đã đóng (07/09/2026 — v0.16.2, PATCH):**

- **Lớp 3 ca kiểm thử hành vi của `sht-cds-thiet-ke-prd` → ĐÃ VẬN HÀNH (đầy đủ).** Đóng nốt điểm "một phần" của v0.16.1: PRD-02/03/04 chạy bằng **3 subagent độc lập, blind** (không biết skill do ai dựng) — thoả §9b luật 3 (người chạy độc lập, không phải agent dựng skill). Kết quả 3/3 định tuyến đúng: PRD-02 chọn `ra-soat-hop-dong-vendor` và chủ động loại `thiet-ke-prd`; PRD-03 dùng `thiet-ke-prd` rồi hand-off agent sang `thiet-ke-agent`; PRD-04 dừng ở cổng chặn, đòi Giai đoạn 01 trước. Cộng PRD-01 (live phiên chính) → cả 4 ca có bằng chứng live. Ghi vào `references/ca-kiem-thu.md`.

**Đã đóng (07/09/2026 — v0.16.1, PATCH):**

- **Lớp 3 ca kiểm thử hành vi của `sht-cds-thiet-ke-prd` → ĐÃ VẬN HÀNH (một phần).** Phiên "Test kiểm thử hệ thống Skill": chạy Lớp 1 (audit sạch) + Lớp 2 (skill nạp live) + Lớp 3 (4 ca gài). PRD-01 chấm **live** (gọi skill thật, cổng chặn bật đúng); PRD-02/03/04 chấm ở mức đối chiếu description/thiết kế. **Người chấm: anh Hà** (§9b luật 3). Ghi vào `references/ca-kiem-thu.md`. (Nâng lên đầy đủ ở v0.16.2.)

**Đã đóng (07/09/2026 — v0.16.0, MINOR — THÊM SKILL):**

Nguồn: phiên "thẩm định & lên kế hoạch skill phân tích quy trình → PRD". Thẩm định `ck:plan` (claudekit-engineer) làm ứng viên process→PRD → đạt ~3/11 nhu cầu PRD của SHT (skill lập kế hoạch code trên codebase, sai tầng). **Quyết định kiến trúc: +1 skill mới** — có khoảng trống thật ở nhịp 02→03: `danh-gia-hien-trang` dừng ở bảng điểm nghẽn, `thiet-ke-agent` giả định giải pháp đã là AI agent; không skill nào sở hữu tầng "quy trình To-Be + PRD".

- **`sht-cds-thiet-ke-prd` (MỚI, tầng 1, Giai đoạn 03).** Nhận bảng điểm nghẽn As-Is → thiết kế To-Be → soạn PRD 10 khối. Trung lập với hướng thi công; hand-off phần thiết kế AI agent sang `sht-cds-thiet-ke-agent`. Kèm 3 references: `mau-prd-sht.md`, `checklist-tuan-thu-nd13-nhnn.md`, `ca-kiem-thu.md` (4 ca gài ranh giới — CHƯA VẬN HÀNH, chờ người chấm theo §9b luật 3).
- **Mượn 2 hạt giống từ `ck:plan`** (không mượn nguyên khối): ưu tiên hoá MoSCoW/YAGNI (§6) và review đối kháng PRD (§8, tinh thần red-team/validate).
- **Nối chuỗi CĐS (sửa E3 đảo một chiều):** `danh-gia-hien-trang` §5 nay route G1 → `thiet-ke-prd` → (nếu là agent) `thiet-ke-agent`; câu định vị `thiet-ke-agent` nay ghi rõ PRD là đầu vào. Ranh giới đối xứng với `ra-soat-hop-dong-vendor` (rà PRD vendor ≠ soạn PRD SHT) ghi ở vùng loại trừ.
- **Còn tồn (mức THẤP, theo §9 không sửa ngay):** E10 ở `sht-cds-thiet-ke-prd` (description 994/1024 — sát trần); lần bổ sung tới rút phần liệt kê trigger trước, giữ vùng loại trừ. Ca kiểm thử hành vi chưa vận hành.

**Đã đóng (03/09/2026 — v0.15.4):**

Nguồn: phiên rà soát chuỗi hợp đồng ba lớp dự án Metro TP.HCM Tuyến 1, nhật ký `NHAT_KY_PHIEN_LAM_VIEC_v5_2026-09-03.md`. **Quyết định kiến trúc: 0 skill mới.** Toàn bộ bài học đều thuộc miền của hai skill đã có — theo §8, mặc định nghiêng về mục mới trong skill cũ.

- **Kiểm trùng trước khi thêm — 60% bài học đã có sẵn.** Trước khi viết, đối chiếu từng phát hiện của phiên với `references/red-flags-hop-dong.md`: mục §4 đã có "đối chiếu ngày hết hạn với ngày hiện tại" và "giới hạn định lượng so với số thực tế"; §5 đã có deemed acceptance và back-to-back SLA; §7 đã có "hiệu lực báo giá còn hay đã hết" và "trường để trống `[INSERT]`"; §2 đã có **đúng** cảnh báo "nếu thiết bị đã chốt HTTP/cURL long-polling thì đừng khuyến nghị MQTT" — trùng khít một phát hiện của phiên. Nên chỉ bổ sung **4 gạch đầu dòng thật mới**, không thêm mục mới. Đây là cách chặn E4 tại nguồn thay vì chữa sau.
- **`ra-soat-hop-dong-vendor` +5 logic** (123 → 190 dòng, vẫn dưới ngưỡng E5): §0.2b tình trạng ký & gán toạ độ tệp-phiên bản · §0.3 đồng hồ hiệu lực · §0.4 hệ tác nhân độc lập theo lớp (trỏ `superpowers:dispatching-parallel-agents` cho cơ chế chung) · §1.4b mâu thuẫn nội bộ trong cùng một văn kiện · nguyên tắc cốt lõi #7 toạ độ tệp và #8 ba nhãn phát biểu. Bảng "Sai lầm cần tránh" +8 hàng.
  → **Sự cố gốc:** một khiếm khuyết thuộc **bản dự thảo** đã đi vào công văn có số, có dấu, **đã gửi đối tác**; và một tài liệu phân tích nội bộ kết luận sai tình trạng ký của một SoW đã ký đủ hai bên. Cả hai chỉ lộ ra vì hai tác nhân độc lập bất đồng.
- **`references/ca-kiem-thu.md` của `ra-soat-hop-dong-vendor`: rỗng → 8 ca.** Trước phiên này skill chưa từng hỏng trên việc thật nên file rỗng có chủ ý. Nay có 3 sự cố thật + 5 quy tắc đã trả giá, nên theo §9b luật 1 mỗi sự cố sinh đúng một ca. **Trạng thái: CHƯA VẬN HÀNH** — ca đã viết, chưa ca nào được người chấm.
- **`sht-nen-tang-kiem-chung` +3 logic** (210 → 225 dòng): §3 ghi tên bản bị thay thế vào bản có hiệu lực **trước** khi xóa, kèm ngoại lệ khi bản cũ là cơ sở của văn bản đã phát hành ra ngoài · §4 tài liệu phân tích của phiên trước thuộc diện phải kiểm chứng · §6.1 dò trang trống bằng máy + checklist §5 thêm một mục.
- **Sửa lỗi thật trong `sht-nen-tang-kiem-chung` §6.1: skill đang chỉ định một công cụ không tồn tại.** Mục này quy định xuất PDF bằng WeasyPrint như đường duy nhất; trên máy người dùng không có WeasyPrint, cũng không có `pdftoppm` lẫn `pandoc` (nhật ký một dự án còn ghi là có — sai). Nay thành **hai đường chọn theo công cụ có thật** (WeasyPrint, hoặc `python-docx` + COM tới Word), kèm quy tắc **kiểm công cụ trước, đừng tin ghi chú môi trường của phiên cũ**. Đây là loại lỗi skill không audit nào bắt được: cú pháp đúng, cấu trúc đúng, nội dung sai với thực tế.
- **E10 ở `sht-nen-tang-kiem-chung` — ĐÃ ĐÓNG.** Ghi nhận từ 30/08 ở mức THẤP theo §9 (không sửa ngay). Phiên này đằng nào cũng mở skill ra sửa, nên xử lý luôn theo đúng §9: rút description 975 → **825** ký tự bằng cách cắt phần liệt kê bốn quy tắc, giữ nguyên toàn bộ vùng loại trừ, và **thêm** ba trigger mới (`"xoá bản cũ"`, `"dọn thư mục"`, dò trang trống). `ra-soat-hop-dong-vendor` cũng thêm 4 trigger (763 → 874 ký tự), gồm `"đối soát giấy phép"` và `"đây là bản dự thảo hay bản ký"`.
- **Sửa cảnh báo giả trong chính phép kiểm gói của `quan-tri-he-thong-skill`.** Phép kiểm ghi trong mục "Bảo trì plugin" dùng `unzip -l <file>.plugin | grep -c 'skill-upgrade\|\.plugin$'` và yêu cầu kết quả bằng 0. Nhưng `unzip -l` in dòng tiêu đề `Archive: <tên gói>.plugin`, dòng đó **tự khớp** mẫu `\.plugin$` — nên phép kiểm luôn trả về ≥1 kể cả khi gói hoàn toàn sạch. Đã đổi sang `unzip -Z1` (chỉ liệt kê tên tệp). Phát hiện khi tự chạy phép kiểm này ở phiên 03/09/2026 và nhận kết quả 1 trên một gói sạch. Đây đúng loại lỗi mà §1 và §9b cảnh báo: **cảnh báo giả kéo dài làm người ta ngừng đọc báo cáo**, nguy hiểm không kém bỏ sót.
- **`ra-soat-hop-dong-vendor` §0.2b +luật số 5, và ca kiểm thử +HD-09, +HD-10.** Cuối phiên người dùng bổ sung hai văn kiện mà thư mục chưa có, làm lộ ca thứ BA cùng một họ lỗi trong cùng một ngày: một số hiệu đơn đặt hàng do chính bản dự thảo tự ghi đã được dùng xuyên suốt năm tài liệu, trong khi số đó thực tế đã cấp cho hạng mục khác và đã ký từ hai tuần trước. Nay chốt luật: **định danh đọc từ bản dự thảo là ĐỀ XUẤT, không phải định danh**; riêng số hiệu phải đối chiếu thêm xem có đang dùng cho hạng mục khác không. Ba ca cùng họ được ghi thành một khối ví dụ trong §0.2b để lần sau nhận ra nhanh.
- **Phiên bản: ba PATCH liên tiếp (0.15.1 → 0.15.2 → 0.15.3 → 0.15.4).** Theo quy tắc đã ghi: MINOR chỉ dành cho thêm/bỏ skill hoặc đổi ranh giới. Phiên này không thêm skill nào, không di chuyển logic giữa các chủ sở hữu — chỉ bổ sung logic trong đúng chủ sở hữu sẵn có và sửa hai lỗi nội dung. Gói `0.15.2` được dựng rồi **thay ngay bằng `0.15.3` trong cùng phiên** khi phát hiện lỗi phép kiểm ở trên; gói 0.15.2 chưa từng được cài ở đâu và đã bị xóa để thư mục không có hai gói cùng phiên. Ghi lại lý do ở đây để lần sau không phải suy luận lại.

**Đã đóng (25/08/2026 — v0.11.0):**

- **Công cụ audit không có ai kiểm.** Đối chiếu ngược 4 lỗi thật của phiên v0.9.0: script bắt được **1**. Ba lỗi lọt đều mang tính cơ học nhưng nằm ngoài phạm vi nó soi — nó chỉ đọc *bên trong* các SKILL.md, còn lỗi lại ở **skill nằm ở đâu**, **sổ có khớp thực tế không**, **gói chứa gì**. Đã thêm E7–E10 (phiên trước) và E11 (phiên này), cộng `test_audit.py` 29 ca.
  → **Quy tắc: khi một lỗi lọt qua audit, việc đầu tiên không phải sửa lỗi đó mà là hỏi "vì sao script không thấy?" rồi vá phạm vi.**
- **E11 — Sổ đăng bạ khai báo quan hệ không có thật.** E8 chỉ kiểm *tên* trong sổ; nhưng cột "Dùng chung với" mới là kiến trúc được tuyên bố. Chạy lần đầu bắt ngay: sổ khai `sht-normalize-account` dùng chung với `sht-xacthuc-baocao-hoatdong` trong khi SKILL.md không hề nhắc tới. Đã nối con trỏ thật.
- **`release.py` — chín cổng phát hành.** Mọi lỗi phát hành đã gặp đều do quên một bước thủ công. Cổng 2 cố ý **không** soi skill cá nhân: E7 là lỗi phía cài đặt, chặn phát hành vì nó sẽ khoá cứng việc ra bản mới chỉ vì người dùng chưa kịp xoá một skill cũ. Cổng 4 (thêm 30/08/2026) chặn đóng gói khi file `--out` đã tồn tại và version bên trong bằng version ở nguồn — gói cũ có thể đã được cài, không ai truy được nó đã đi tới đâu (sự cố: hai lần đóng gói cách nhau 37 phút cùng giữ `0.15.0`, gói sau ghi đè gói trước, mất 7 bản vá).
- **Bảng lỗi E1–E11 chuyển sang `references/bang-loi.md`** — áp chính quy tắc E5 cho skill này, giữ thân file dưới ngưỡng.

**Đã đóng (25/08/2026 — v0.9.0):**

- **`sht-cds-thiet-ke-agent` nằm ngoài plugin** — skill thứ 12 được lưu dạng skill cá nhân trong khi nó trỏ tới hai skill nằm trong plugin. Hai đường bảo trì song song, đúng loại lỗi trôi phiên bản mà skill này sinh ra để chặn; ngoài ra nó không đi kèm plugin khi chia sẻ cho đồng nghiệp. Đã đưa vào `skills/` của plugin và đăng ký vào Sổ.
- **Sổ đăng bạ tự trôi** — tồn tại một khối mồ côi 3 hàng (`chuan-hoa-ho-so-tai-lieu`, `ra-soat-hop-dong-vendor`, `sht-cds-danh-gia-hien-trang`) nằm tách dưới bảng chính, nội dung cũ và khác hẳn hàng chính thức. Dòng đầu sổ ghi "11 skill, cả 11 đã đăng ký" trong khi tài khoản có 12. Đã gộp về một hàng cho mỗi skill và sửa lại dòng tổng.
  → **Quy tắc mới: khi bổ sung skill vào Sổ, sửa hàng có sẵn, không append thêm bảng mới ở cuối.** Sau mỗi lần sửa Sổ, đếm số hàng phải bằng số thư mục trong `skills/`.
- **Nhóm CDS là đảo một chiều** — `sht-cds-thiet-ke-agent` trỏ tới `sht-cds-danh-gia-hien-trang` nhưng không có chiều ngược lại, nên khi đang làm Giai đoạn 01 sẽ không ai gọi bước thiết kế agent. Đã nối chiều còn lại.

**Đã đóng (25/08/2026 — v0.8.0):**

- **Nâng cấp `chuan-hoa-du-lieu-tuyen-dung` từ chiến dịch Platform BA & PM (ID 2422770):**
  §1 chuyển sang hỏi bằng văn bản đánh số nếu người dùng bỏ qua widget hai lần ·
  §3 nới một điều kiện lọc không được phá bộ lọc domain dùng chung ô (chạy nhiều lượt riêng) + xác nhận chip sau khi chọn dropdown ·
  **§4.1 MỚI: hai phép quét bắt buộc trước khi gửi lời mời — quét tên công ty mình trong pool (phát hiện cựu nhân sự) và quét hồ sơ trùng người bằng chuỗi công ty** ·
  §10 quy tắc nơi lưu file (chưa có quyền thì hỏi trước, không lưu tạm rồi báo xong; đặt tên theo quy ước sẵn có của folder; thử biến thể đường dẫn trước khi báo lỗi) + đếm số lượng từ log và màn hình xác nhận của nền tảng ·
  Checklist +4 mục.
- **`references/thao-tac-cong-tuyen-dung.md` +3 mục tra cứu:** §5 sửa state Vue khi ô lọc chết (chip đúng ≠ state đúng, phải kiểm tầng cha), §6 quét hàng loạt từ `p4.cvs` gồm trường `request_connection`, §7 LinkedIn dùng URL `/preload/custom-invite/` thay modal shadow DOM; §3 bổ sung phân biệt lỗi cục bộ/hệ thống bằng đối tượng thứ hai và cảnh báo zoom làm treo renderer.
- **Sổ đăng bạ lệch version:** sổ ghi v0.5.0 trong khi `plugin.json` thực tế đã ở v0.7.0 — sổ không được cập nhật ở lần phát hành v0.6.0/v0.7.0. Đã đồng bộ về v0.8.0. → **Nhắc lại quy tắc: cập nhật Sổ đăng bạ NGAY TRONG cùng phiên phát hành, sổ lệch thực tế nguy hiểm hơn không có sổ.**

**Đã đóng (25/08/2026 — v0.8.1, PATCH):**

- **`chuan-hoa-du-lieu-tuyen-dung` §5.3 — chốt cách xử lý khoảng trống dòng thời gian.** Phát hiện khi chấm thử lại một hồ sơ Mua hàng Nội địa để kiểm chứng skill: quy tắc "tính lại từ năm tốt nghiệp" chỉ nói phải *phát hiện* khoảng trống, không nói xử lý ra sao — nên dễ bị trừ điểm hai lần (vừa hạ tiêu chí minh bạch, vừa ghi thành rủi ro). Nay chốt rõ: khoảng trống là dữ kiện cho **bảng rủi ro + câu hỏi phỏng vấn**, KHÔNG phải căn cứ trừ điểm; chỉ trừ khi có bằng chứng khai sai. Kèm cảnh báo Điều 8 BLLĐ 2019 — quy khoảng trống thành điểm trừ có nguy cơ gián tiếp phạt vì lý do cá nhân (nghỉ sinh, chăm sóc gia đình, học tiếp). Checklist +1 mục.
- **Kiểm chứng ngược khung chấm:** cùng hồ sơ, ba bản chấm trước cho 4.30 · 4.24 · 4.05 (hợp nhất còn 4.03); bản chấm độc lập 25/08 cho 3.77–3.83. Dải **3.77 → 4.03 nằm gọn trong khoảng HIRE (3.6–4.2), không cắt ngưỡng** → theo §5.4 nghĩa là khung đủ chặt, chênh lệch không đổi kết luận. Không cần bổ sung tiêu chí.

**Đã đóng (27/08/2026 — v0.14.1, PATCH):**

- **`sht-nen-tang-kiem-chung` §3.1 MỚI — ghi đúng thư mục đích.** Sự cố thật: hồ sơ ứng viên tuyển dụng bị ghi thẳng vào thư mục nguồn plugin `sht-skills/`, người dùng phải tự phát hiện và nhắc. Nguyên nhân gốc: coi thư mục làm việc mặc định là nơi đổ sản phẩm mà không nhìn cấu trúc bên trong. Nay chốt bảng nhận diện 4 loại thư mục theo dấu hiệu (`.claude-plugin/` · `.git/` · `.env` · chỉ tài liệu nghiệp vụ), quy tắc **hỏi trước khi ghi** nếu rơi vào thư mục hạ tầng, kèm ngoại lệ khi chính hạ tầng là đối tượng công việc. Checklist §5 +1 mục đặt ở **vị trí đầu tiên** — kiểm trước khi ghi file, không phải lúc bàn giao.
- **Sửa thứ tự đánh số §5/§6** ở cùng skill: khối §6 (kết xuất) đang nằm trước §5 (checklist). Giữ nguyên số mục để không gãy 8 tham chiếu chéo từ 5 skill tầng 1, chỉ hoán đổi vị trí vật lý.
- **Description** cập nhật từ 885 → 975 ký tự (trần 1024): bổ sung quy tắc ghi đúng thư mục vào phần liệt kê và trigger `"lưu nhầm chỗ"`.

**Việc còn tồn:**

- **E10 mức THẤP ở `sht-nen-tang-kiem-chung`:** description 975/1024 ký tự — sát trần. Ghi nhận theo §9, **không sửa ngay**. Lần bổ sung nội dung tới phải rút gọn phần liệt kê ví dụ trước, giữ nguyên vùng loại trừ.
- Chuẩn tên `sht-<miền>-<hành động>` chưa áp cho nhóm `chuan-hoa-*` (4 skill). Đổi tên sẽ gãy tham chiếu chéo — chỉ làm khi có dịp tái cấu trúc lớn.
- **E4 (10/09/2026 — cập nhật):** 6 cảnh báo E4 đều là tín hiệu giả (mở đọc thân, xác minh). Đã chuyên biệt hoá tiêu đề để dập 5/6: `"Quy trình"` (normalize) → `"Quy trình chuẩn hoá account"`; `"10. Bàn giao"` (tuyển dụng) + `"Checklist trước khi bàn giao"` gắn hậu tố; `"Checklist chốt trước khi trình đề xuất"` → `"…đề xuất agentic"`. **Còn 1 benign không dập được:** `chuan-hoa-ho-so-tai-lieu` GĐ5 ↔ `ra-soat-hop-dong-vendor` GĐ2 (kết xuất báo cáo) — E4 khớp vì **thân mục có câu con trỏ giống hệt** ("theo `sht-nen-tang-kiem-chung` §6, không định nghĩa lại"), mà trùng đó là **đúng** (cùng trỏ một chủ). Audit bản này chưa tự bỏ qua cặp con-trỏ có phần "Riêng cho…" đi kèm. **Giữ nguyên, không đục thêm** (§9). Muốn dập sạch phải vá `audit_skills.py` để bỏ qua cặp con trỏ — để dịp sửa tool sau.

**Đã đóng (24/08/2026 — v0.5.0):**

- **Hòa mạng toàn diện `sht-cds-danh-gia-hien-trang`:** Bổ sung description chuẩn 4 phần kèm vùng loại trừ, liên kết Tầng 0 `sht-nen-tang-kiem-chung` khi xuất báo cáo hiện trạng (bản điều hành / bản chi tiết), chuyên biệt hóa tiêu đề mục để khử triệt để cảnh báo E4.
- **Khử lỗi E1 mức CAO ở `sht-nen-tang-kiem-chung`:** Rút gọn description từ 1027 ký tự xuống < 950 ký tự trong khi bảo toàn 100% từ khóa và vùng loại trừ.
- **Đồng bộ hệ thống:** Nâng cấp Sổ đăng bạ, README.md (11 skill, 3 tầng) và `plugin.json` (v0.5.0), đưa toàn bộ hệ thống về 0 lỗi mức CAO.

**Đã đóng trước đó:**

- Tham chiếu gãy tới skill xác thực báo cáo → đã tạo `sht-xacthuc-baocao-hoatdong`.
- Frontmatter chồng khối ở `chuan-hoa-du-lieu-tuyen-dung` → đã dọn.
- Bốn logic tầng 0 rải rác ở 4 skill → đã nâng lên `sht-nen-tang-kiem-chung`.
- E5 ở `chuan-hoa-du-lieu-du-an` (466 dòng) → đóng gói plugin, tách Phụ lục A/B sang `references/`, còn 262 dòng.
- Tinh gọn `ra-soat-hop-dong-vendor` và `chuan-hoa-ho-so-tai-lieu` → **v0.2.0 (10 skill)**.
- v0.3.0: Hai overlap thật giữa `ra-soat` và `chuan-hoa-ho-so-tai-lieu` (kết xuất báo cáo nâng lên nền §6; chuyển đổi định dạng file giao `chuan-hoa-ho-so-tai-lieu` sở hữu).
- v0.4.0: Mở rộng `chuan-hoa-du-lieu-tuyen-dung` sang soạn JD + khảo sát lương 2 lớp + tách khung ASK Quản lý A60/S30/K10.

---

**Đã đóng (24/08/2026):**

- **Sổ đăng bạ lệch thực tế** — sổ ghi 8 skill, plugin đã có 11. Đã bổ sung `chuan-hoa-ho-so-tai-lieu`, `ra-soat-hop-dong-vendor`, `sht-cds-danh-gia-hien-trang` vào sổ.
- **`chuan-hoa-du-lieu-tuyen-dung` trôi thành HAI NHÁNH song song** — bản folder nguồn (21/08: §2b soạn JD, khung CBQL A60/S30/K10, tinh chỉnh §4/§6/§10) và bản đóng trong plugin đã cài (23/08: toàn bộ quy tắc LinkedIn). **Không bản nào là tập cha của bản kia.** Nguyên nhân: lần phát hành 23/08 đóng gói từ một bản nền cũ thay vì từ folder nguồn. Đã hợp nhất thành một bản duy nhất (293 dòng) và kiểm chứng bằng cách quét từng dòng dài của cả hai nhánh. → **Quy tắc mới bắt buộc: mỗi lần phát hành plugin phải đóng gói TỪ ĐÚNG folder nguồn, và sau khi cài phải đối chiếu mục lục + số dòng giữa folder nguồn và bản cache.**
- **E5 ở `chuan-hoa-du-lieu-tuyen-dung` đã xử lý bằng `references/`** — tách 18 khối tra cứu (thao tác TopCV/LinkedIn, xử lý lỗi công cụ trình duyệt, luồng nút kết nối) sang `references/thao-tac-cong-tuyen-dung.md`, và phụ lục nguồn sang `references/nguon-quy-tac.md`. Thân 293 → 269 dòng, khối lượng thật giảm 20% (43.9k → 35.0k ký tự), không mất dòng nào (đã quét đối chiếu từng dòng dài). **Ranh giới tách đặt ra làm chuẩn cho mọi skill về sau: thân giữ logic QUYẾT ĐỊNH (chấm gì, theo chuẩn nào, được/không được làm gì), `references/` giữ phần TRA CỨU (nền tảng cư xử ra sao, gặp lỗi nào thì làm gì).** Đây cũng là chỗ tăng nhanh nhất — từ nay quy tắc thao tác nền tảng mới phải vào `references/`, không vào thân.
- Nâng cấp `chuan-hoa-du-lieu-tuyen-dung` từ chiến dịch Chuyên viên Mua hàng Nội địa: §5.1 rubric tiêu chí con + tiêu chí bối cảnh nghiệp vụ, §5.2 gắn nhãn độ tin cậy thay vì trừ ngược điểm, §5.3 ba phép kiểm bắt buộc (tính từ năm tốt nghiệp, kiểm chứng số liệu thành tích, hạn ứng tuyển), §5.4 đối chiếu chéo nhiều bản chấm bằng dải điểm vs ngưỡng, §7 tách deliverable 1 trang/2 trang + cấu trúc scorecard 7 khối, §4 bẫy trang tin tuyển dụng TopCV. Skill 212 → 293 dòng, sau khi tách references/ còn **269 dòng**.

---


