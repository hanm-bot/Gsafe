# sht-skills

Bộ skill nghiệp vụ nội bộ của **Công ty CP Đầu tư Công nghệ SHT**. Mười ba skill, chia ba tầng, mỗi logic có đúng một chủ sở hữu.

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
       ▼ gọi
TẦNG 2 — ĐỊNH DẠNG ĐẦU RA (Skill dựng sẵn)
  docx · xlsx · pptx · pdf
```

Skill tầng 1 **trỏ tới** tầng 0, không chép lại. Skill nhà không viết lại kỹ thuật dựng file — chỉ nêu quy ước riêng của SHT rồi gọi tầng 2.

---

## Mười ba skill

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

Phiên bản 0.16.0 — 07/09/2026.
