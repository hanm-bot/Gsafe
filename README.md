# sht-skills

Bộ skill nghiệp vụ nội bộ của **Công ty CP Đầu tư Công nghệ SHT**. 29 skill, chia bốn tầng, mỗi logic có đúng một chủ sở hữu.

Nguyên tắc xuyên suốt: **dữ liệu sai lan nhanh hơn dữ liệu đúng.** Một con số sai nhân bản ra 4–5 deliverable; một cái tên bị thay nhầm đi thẳng vào văn bản trình ký. Mọi skill ở đây tối ưu cho việc chặn lỗi sớm.

---

## Kiến trúc

```
TẦNG 0 — NỀN TẢNG (Áp cho mọi miền)
  sht-nen-tang-kiem-chung          quy tắc chung + ghi đúng thư mục + checklist bàn giao + 5 dạng báo cáo
  quan-tri-he-thong-skill          quản trị chính hệ thống skill (audit, chống overlap, Sổ đăng bạ)
       ▲ trỏ về
TẦNG 1 — NGHIỆP VỤ CHUYÊN SÂU (11 skill)
  chuan-hoa-du-lieu-du-an          dữ liệu & tài liệu dự án XDCB/nội thất
  chuan-hoa-du-lieu-nhansu         xác minh danh tính nhân sự
  sht-qd-nhansu-alignment          soạn & rà soát Quyết định tổ chức
  chuan-hoa-du-lieu-tuyen-dung     săn CV, chấm điểm ASK & soạn JD mới
  sht-normalize-account            chuẩn hóa account CRM (Turso/Base.vn)
  sht-xacthuc-baocao-hoatdong      xác thực số liệu báo cáo kinh doanh
  ra-soat-hop-dong-vendor          gap analysis hợp đồng CNTT, chuỗi Mua/Bán back-to-back, license
  chuan-hoa-ho-so-tai-lieu         chuẩn hoá PDF scan/docx/xlsx thành dữ liệu trích dẫn được
  sht-cds-danh-gia-hien-trang      đánh giá hiện trạng & sẵn sàng chuyển đổi số (DMI 6 trụ cột)
  sht-cds-thiet-ke-prd             thiết kế quy trình To-Be & soạn PRD (nhịp 02→03, trung lập hướng thi công)
  sht-cds-thiet-ke-agent           thiết kế & thẩm định use-case AI agentic (Purpose/Scope/Boundaries)

TẦNG 1B — ĐỘI 5 AGENT QUẢN TRỊ DOANH NGHIỆP / AIS48 (6 skill)
  sht-quan-tri-dn                  điều phối cả chuỗi 5 vai + nhân rộng 9 phòng ban (Cổng I/O, Sổ Cái HITL)
       ▼ gọi từng vai khi nhân sự tự làm một vai riêng lẻ
  sht-vai1-harvester               [DEPT]-01 thu thập, làm sạch, Masking Vùng Đỏ
  sht-vai2-analyzer                [DEPT]-02 phân tích điểm nghẽn, 5 Whys, Grounding
  sht-vai3-dispatcher              [DEPT]-03 đôn đốc tiến độ, soạn nhắc việc, lập lịch
  sht-vai4-reporter                [DEPT]-04 soạn Báo cáo Điều hành 4 phần AIS48
  sht-vai5-critic                  [DEPT]-05 phản biện độc lập, tờ trình HITL, Sổ Cái SHA-256
       ▼ gọi
TẦNG 2 — ĐỊNH DẠNG ĐẦU RA (Skill dựng sẵn)
  docx · xlsx · pptx · pdf
```

Skill tầng 1 **trỏ tới** tầng 0, không chép lại. Skill nhà không viết lại kỹ thuật dựng file — chỉ nêu quy ước riêng của SHT rồi gọi tầng 2.

---

## 29 skill

| Skill | Dùng khi |
|---|---|
| **sht-nen-tang-kiem-chung** | Trước **mọi** lần bàn giao file. Lan truyền hiệu chỉnh, đổi tên hàng loạt an toàn, một-bản-có-hiệu-lực, checklist chung, xuất 5 dạng báo cáo |
| **quan-tri-he-thong-skill** | Gõ "UPGRADE SKILL". Audit hệ skill, chống trùng logic, quy trình nâng cấp an toàn |
| **chuan-hoa-du-lieu-du-an** | Soạn biên bản từ ghi âm, bảng tiến độ, công văn, báo cáo khảo sát, phục dựng văn bản có watermark |
| **chuan-hoa-du-lieu-nhansu** | Hồ sơ bổ nhiệm, đánh giá cán bộ, onboarding — bất cứ tài liệu nào có tên người |
| **sht-qd-nhansu-alignment** | Soạn/rà soát Quyết định, xung đột thẩm quyền, "Under CCO" |
| **chuan-hoa-du-lieu-tuyen-dung** | "hunt CV", lọc hồ sơ, chấm điểm ứng viên, scorecard, soạn JD mới kèm khảo sát lương thị trường |
| **sht-normalize-account** | Đếm khách hàng/chi nhánh, gộp account, Account 360 |
| **sht-xacthuc-baocao-hoatdong** | "Số này lấy ở đâu", đối chiếu báo cáo với CRM trước khi đưa vào văn bản chính thức |
| **ra-soat-hop-dong-vendor** | Rà soát hợp đồng CNTT, gap analysis spec vs SoW/BRD, chuỗi mua bán back-to-back, license |
| **chuan-hoa-ho-so-tai-lieu** | Bóc tách PDF scan tiếng Việt, trích dẫn chứng cứ có toạ độ trang/điều, soạn báo cáo đối ngoại trung tính |
| **sht-cds-danh-gia-hien-trang** | "Đánh giá hiện trạng CĐS", khảo sát DMI 6 trụ cột, kiểm toán dữ liệu 6 chiều, bản đồ điểm nghẽn As-Is trước Cổng G1 |
| **sht-cds-thiet-ke-prd** | "Thiết kế PRD", "viết PRD", "quy trình To-Be", "chốt scope pilot" — nhận điểm nghẽn As-Is → thiết kế To-Be → soạn PRD cho giải pháp CĐS (Giai đoạn 03) |
| **sht-cds-thiet-ke-agent** | "Thiết kế use-case AI", "AI được tự quyết đến đâu", "HITL" — khai báo agent 3 chiều, tầng confidence, Tiered Governance (khi PRD chốt hướng là agent) |
| **sht-quan-tri-dn** | Vận hành quy trình quản trị tuần, giám sát đầu việc liên phòng ban, `/goal` `/teamwork` `/schedule`, thẩm định QA Lớp 2, dựng Đội 5 Agent cho phòng ban mới |
| **sht-jev-cong-quyet-dinh** | "Chạy ca thật", "JEV", "cổng quyết định", "chấp nhận/bác/sai JEV-…", "vá cổng" — vận hành cổng 3 ngả nội bộ, ghi phản hồi xác thực Sổ Cái, luật ca thật trên kho nguồn, phiếu việc 4 vai |
| **sht-vai1-harvester** | "Làm sạch dữ liệu", "ẩn danh hồ sơ", "mask PII" — tự tay làm sạch dữ liệu thô trước khi giao bước phân tích |
| **sht-vai2-analyzer** | "Vì sao trễ", "phân tích nguyên nhân", "5 Whys" — chẩn đoán chỉ tiêu/đầu việc bị lệch, đèn giao thông 3 mức |
| **sht-vai3-reporter** | "Viết báo cáo điều hành", "tóm tắt cho sếp" — Báo cáo Điều hành 4 phần AIS48, kiểm soát ngân sách token |
| **sht-vai4-reminder** | "Nhắc việc", "soạn tin đôn đốc", "ai đang trễ hạn" — phân loại quá hạn/sắp hạn, soạn nhắc việc 4 phần |
| **sht-vai5-critic** | "Phản biện", "kiểm tra chéo trước khi trình", "rà số liệu" — thẩm tra 3 tầng, tờ trình HITL, Sổ Cái SHA-256 |
| **brainstorm** | Bóc tách ý tưởng thô thành Bản đặc tả Brainstorm 12 phần qua phỏng vấn sâu 7 nhóm (Deep Interview). |
| **prd-architect** | Thiết kế PRD Enterprise, phỏng vấn sâu 7 nhóm nghiệp vụ, xuất sơ đồ trực quan và báo cáo HTML Single-Page. |
| **usecase-diagram** | Render sơ đồ PlantUML (Use Case, Activity) thành ảnh vector .svg, hỗ trợ `prd-architect`. |
| **sht-qa-kiem-chung-skill-hook** | Kiểm chứng bằng hành vi thật xem skill/hook có đang chạy không, tránh kết luận sai lệch giữa tài liệu và thực tế. |
| **sht-ha-tang-va-path-portable** | Phát hiện và sửa đường dẫn hardcode, đảm bảo tương thích đường dẫn portable trên mọi máy. |
| **sht-quan-tri-hien-phap-tai-lieu** | Giữ tài liệu vận hành (CLAUDE.md, README) khớp đúng thực tế máy hiện tại khi phát hiện sai lệch. |
| **sht-quan-tri-tri-nho-lien-phien** | Quản trị bộ nhớ liên phiên, quyết định ghi/xóa memory thay vì tạo mới, giữ trạng thái memory luôn chính xác. |
| **archify** | Vẽ sơ đồ quy trình (workflow diagram) từ một kế hoạch đã chốt hoặc mô tả quy trình bằng Mermaid. |
| **grill-me** | Phỏng vấn/khảo sát người dùng để làm rõ yêu cầu, chốt phương án thành kế hoạch trước khi thực thi. |

Mỗi skill tự kích hoạt theo mô tả của nó — không cần gọi tên. Muốn gọi tay thì gõ `/<tên-skill>`.

---

## Các bài học xương máu được đóng gói ở đây

1. **Không bao giờ find/replace thẳng trên tên người tiếng Việt.** `Hà` → `Anh Hà` biến "Hà Giang" thành "Anh Hà Giang". Skill nền giữ danh sách cụm bảo vệ và quy trình dry-run bắt buộc.
2. **Gộp account theo Mã Dự Án, không theo tên khách hàng.** Làm sai chỗ này từng tách 1 ngân hàng thành 446 account ảo.
3. **Số liệu chưa truy được về nguồn thì không được vào phần Căn cứ của Quyết định.** Hệ nhãn ✅/⚠️/❓ buộc phải gắn cho mọi con số trước khi ký.
4. **Không dùng OCR cho văn bản pháp lý tiếng Việt.** Render ảnh và đọc thị giác trực tiếp bằng subagent để bảo toàn dấu tiếng Việt và số liệu.
5. **Soạn văn bản đối ngoại theo nguyên tắc đồng thuận lợi ích.** Chứng minh điều mình đề xuất cũng mang lại lợi ích doanh thu lớn hơn cho đối tác thay vì chỉ trích lỗi đối kháng.
6. **Không tự động hóa trên quy trình lộn xộn.** Bắt buộc đo lường DMI 6 trụ cột và làm sạch dữ liệu rác (>15%) trước khi đề xuất giải pháp công nghệ.

---

## Bảo trì

Sau khi cài plugin, **sửa skill thì sửa ở nguồn plugin rồi đóng gói lại** — không dùng công cụ lưu skill cá nhân, vì sẽ tạo hai bản cùng tên trôi khác nhau.

Rà định kỳ:

```bash
python3 skills/quan-tri-he-thong-skill/scripts/audit_skills.py skills/
```

Thoát mã 0 = sạch, 1 = còn lỗi mức CAO. Trên Windows đặt `PYTHONUTF8=1` trước khi chạy.

Sổ đăng bạ — nguồn sự thật về quan hệ giữa các skill — nằm ở Phụ lục B của `quan-tri-he-thong-skill`. Cập nhật nó trong **cùng phiên** mỗi khi thêm/sửa/xóa skill.

---

## Phạm vi

Nội bộ SHT. Các skill dẫn chiếu dữ liệu và văn bản thật của công ty (hệ thống SHT Sales Pipeline trên Turso, Quyết định bổ nhiệm, khung lương 3P, hợp đồng CNTT, khung đánh giá DMI). Không phát hành ra ngoài.

Phiên bản 0.24.2 — 26/09/2026.
