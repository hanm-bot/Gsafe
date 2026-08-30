# SỔ ĐĂNG BẠ

*Cập nhật lần cuối: 27/08/2026 — 12 skill, cả 12 đã đăng ký. 0 lỗi. Phiên bản v0.14.1.*

| Skill | Tầng | Sở hữu logic | Dùng chung với | Không đụng tới |
|---|---|---|---|---|
| `sht-nen-tang-kiem-chung` | **0** | Lan truyền hiệu chỉnh · đổi tên hàng loạt an toàn (+ cụm bảo vệ) · một-bản-có-hiệu-lực · **ghi đúng thư mục đích (§3.1)** · đặt câu hỏi ngược với nguồn · checklist bàn giao chung · **kết xuất theo người đọc (5 dạng báo cáo, xuất PDF/Excel, quét `grep` xác minh)** · **tự kiểm trước khi báo xong (§7)** | **Mọi** skill tầng 1 — nạp kèm trong mọi phiên có bàn giao file | Nghiệp vụ cụ thể của bất kỳ miền nào |
| `quan-tri-he-thong-skill` | **0** | Ranh giới giữa các skill, audit, phân tầng, quy trình nâng cấp, Sổ đăng bạ · khung ca kiểm thử hành vi (§9b) | `skill-creator` để viết nội dung bên trong một skill | Nội dung nghiệp vụ bên trong từng skill |
| `chuan-hoa-du-lieu-du-an` | 1 | 4 cổng kiểm transcript · xác định người phát ngôn · đối chiếu chéo · truy vết timestamp · metadata & epoch ẩn · giữ thể thức + watermark gốc · từ vựng trạng thái | `sht-nen-tang-kiem-chung`; `chuan-hoa-du-lieu-nhansu` khi tài liệu có tên người | Chấm điểm ứng viên; dữ liệu CRM; thẩm quyền QĐ; hợp đồng CNTT |
| `chuan-hoa-du-lieu-nhansu` | 1 | Chốt danh tính với QĐ/hợp đồng · nhiều người trùng tên · một người kiêm nhiệm nhiều vai | `sht-qd-nhansu-alignment` khi soạn QĐ; `sht-xacthuc-baocao-hoatdong` khi hồ sơ có số liệu | Thẩm quyền/mô hình tổ chức; ứng viên chưa tuyển |
| `sht-qd-nhansu-alignment` | 1 | Đối chiếu thẩm quyền & quan hệ báo cáo giữa các QĐ (7 khía cạnh) · cơ chế Điều chỉnh vs Thay thế toàn bộ · thể thức QĐ | `chuan-hoa-du-lieu-nhansu` chốt tên trước; `sht-xacthuc-baocao-hoatdong` nếu Căn cứ có số liệu | Xác minh tên riêng; tính đúng đắn của số liệu |
| `sht-xacthuc-baocao-hoatdong` | 1 | Truy số về truy vấn gốc · 4 bẫy dữ liệu Turso · thứ tự truy nguyên nhân khi lệch · nhãn ✅/⚠️/❓ | `sht-normalize-account` khi đếm khách hàng/chi nhánh; `sht-qd-nhansu-alignment` khi số vào QĐ | Gộp/rollup account; thể thức văn bản |
| `sht-normalize-account` | 1 | Gộp account theo Mã Dự Án (`ma`) · parser mã CN · tự kiểm số chi nhánh | `sht-xacthuc-baocao-hoatdong` khi số liệu vào báo cáo | Danh tính người; tính đúng đắn của doanh số |
| `chuan-hoa-du-lieu-tuyen-dung` | 1 | Săn CV & lọc cổng tuyển dụng · chấm ASK có bằng chứng (2 phiên bản trọng số: A30/S40/K30 ứng viên thường, A60/S30/K10 cán bộ quản lý) · đối chiếu 3P · **soạn JD mới kèm khảo sát lương thị trường 2 lớp khi chưa có JD (§2b)** · scorecard + infographic | `sht-nen-tang-kiem-chung`; `chuan-hoa-du-lieu-nhansu` khi ứng viên vào hồ sơ nội bộ | Hồ sơ nhân sự đã tuyển |
| `ra-soat-hop-dong-vendor` | 1 | Gap analysis SoW/BRD · chuỗi Mua/Bán back-to-back · license & rủi ro pháp lý/kỹ thuật · đo tỷ lệ copy phụ lục & diff phiên bản | `sht-nen-tang-kiem-chung`; `chuan-hoa-ho-so-tai-lieu` khi có PDF scan | Dự án XDCB; hồ sơ nhân sự; thẩm quyền QĐ |
| `chuan-hoa-ho-so-tai-lieu` | 1 | **Chuyển đổi & bóc tách mọi định dạng file (chủ sở hữu)** · trích dẫn có toạ độ · xếp hạng độ vững luận cứ · viết bản đối ngoại không đối kháng | `sht-nen-tang-kiem-chung`; `ra-soat-hop-dong-vendor` khi hồ sơ có hợp đồng CNTT | Soạn QĐ nhân sự; săn CV tuyển dụng; dự án XDCB |
| `sht-cds-danh-gia-hien-trang` | 1 | Đánh giá hiện trạng & DMI 6 trụ cột · kiểm toán chất lượng dữ liệu 6 chiều · bản đồ điểm nghẽn As-Is · thẩm định Cổng G1 | `sht-nen-tang-kiem-chung` khi xuất báo cáo hiện trạng & bàn giao | Rà soát hợp đồng CNTT; chuẩn hóa account CRM; bóc tách hồ sơ scan |
| `sht-cds-thiet-ke-agent` | 1 | Khai báo agent 3 chiều Purpose/Scope/Boundaries · 3 tầng confidence · Tiered Governance L1–L3 · bộ ca kiểm thử có ca gài · vòng đời sandbox→pilot→production→review | `sht-cds-danh-gia-hien-trang` (bắt buộc qua Giai đoạn 01 trước); `sht-nen-tang-kiem-chung` khi bàn giao | Đo DMI/đánh giá hiện trạng; rà soát hợp đồng vendor; chuẩn hóa dữ liệu CRM |

**Đã đóng (25/08/2026 — v0.11.0):**

- **Công cụ audit không có ai kiểm.** Đối chiếu ngược 4 lỗi thật của phiên v0.9.0: script bắt được **1**. Ba lỗi lọt đều mang tính cơ học nhưng nằm ngoài phạm vi nó soi — nó chỉ đọc *bên trong* các SKILL.md, còn lỗi lại ở **skill nằm ở đâu**, **sổ có khớp thực tế không**, **gói chứa gì**. Đã thêm E7–E10 (phiên trước) và E11 (phiên này), cộng `test_audit.py` 29 ca.
  → **Quy tắc: khi một lỗi lọt qua audit, việc đầu tiên không phải sửa lỗi đó mà là hỏi "vì sao script không thấy?" rồi vá phạm vi.**
- **E11 — Sổ đăng bạ khai báo quan hệ không có thật.** E8 chỉ kiểm *tên* trong sổ; nhưng cột "Dùng chung với" mới là kiến trúc được tuyên bố. Chạy lần đầu bắt ngay: sổ khai `sht-normalize-account` dùng chung với `sht-xacthuc-baocao-hoatdong` trong khi SKILL.md không hề nhắc tới. Đã nối con trỏ thật.
- **`release.py` — bảy cổng phát hành.** Mọi lỗi phát hành đã gặp đều do quên một bước thủ công. Cổng 2 cố ý **không** soi skill cá nhân: E7 là lỗi phía cài đặt, chặn phát hành vì nó sẽ khoá cứng việc ra bản mới chỉ vì người dùng chưa kịp xoá một skill cũ.
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
- Bốn cảnh báo E4 còn lại đều là **tín hiệu giả**, chỉ trùng tên tiêu đề: `"10. Bàn giao" ≈ "5. Bàn giao"`, `"Quy trình" ≈ "Quy trình 6 bước"`, và các mục kết xuất báo cáo nay đều chỉ trỏ về nền §6. Đã mở ra đọc, xác minh, không xử lý.

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


