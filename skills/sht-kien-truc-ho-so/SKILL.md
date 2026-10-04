---
name: "sht-kien-truc-ho-so"
description: "Quy hoạch bộ hồ sơ một nghiệp vụ SHT theo vòng đời H1–H5, Gap Matrix có bằng chứng, điểm sẵn sàng bằng đếm file thật. LUÔN dùng khi nói \"lập hồ sơ\", \"thiếu giấy tờ gì\", \"gap matrix\", \"đủ chưa\". KHÔNG dùng để trích chứng cứ (chuan-hoa-ho-so-tai-lieu), rà hợp đồng, soạn QĐ, bản đồ tài liệu chung (kien-truc-tai-lieu)."
---

# Kiến trúc hồ sơ doanh nghiệp (SHT)

Skill này trả lời **một câu**: *bộ hồ sơ của nghiệp vụ này cần những tài liệu gì, đã có gì, còn thiếu gì, làm ở định dạng nào, lấy dữ liệu ở đâu.* Nó **quy hoạch**, không soạn nội dung và không xuất file.

Ranh giới với skill láng giềng:

- `chuan-hoa-ho-so-tai-lieu` — tài liệu **đã có nói gì** (trích dẫn, toạ độ trang). Skill này — **cần những tài liệu gì**.
- `sht-nen-tang-kiem-chung` — quy tắc nền (truy vết nguồn, một bản có hiệu lực, bàn giao, thể thức NĐ30). Kế thừa, không chép lại.

> Phương pháp gốc: tài liệu lớp học AI48S — vietduc·ai (bản gốc: `THỰC HÀNH-AI/AI48S/kien-truc-tai-lieu/`). SHT đã Việt hoá theo 5 luật cứng và hạ tầng đang chạy.

**Thuật ngữ:** vòng đời hồ sơ đánh số **pha H1–H5**, cố ý không gọi "giai đoạn" để khỏi lẫn với 11 giai đoạn CĐS 00–10 và bước P1–P5 của SOP-AI-01.

---

## CỔNG CHẶN — kiểm trước khi lập Gap Matrix

1. **Workspace nào?** Hồ sơ bán cho khách → đầu ra chỉ ghi vào `data/workspaces/<ws>/`. Chưa xác định được workspace → **hỏi, không đoán**. Không đọc/ghi workspace khác (Context Isolation).
2. **Đọc `data/workspaces/<ws>/00_NGUON-HO-SO.md` trước.** Nó khai hồ sơ cập nhật đến ngày nào, bản gốc ở đâu. Chưa có → tạo từ bản mẫu `data/workspaces/Workspace_Demo/00_NGUON-HO-SO.md` rồi mới làm tiếp. Hồ sơ nội bộ không có workspace → hỏi thư mục gốc của hồ sơ.
3. **Hồ sơ là đề xuất giải pháp AI cho khách (giai đoạn CĐS 03)?** → phải đã có đầu ra 01 và 02 (luật cứng #4, hook đọc đĩa sẽ chặn). Chưa có → chuyển `sht-cds-danh-gia-hien-trang`, không lập hồ sơ 03.
4. **Không ghi dữ liệu khách vào `THỰC HÀNH-AI/`** (luật cứng #5) — kể cả khi skill được gọi từ thư mục học tập.

---

## 1. Vòng đời 5 pha & bản đồ tham chiếu

```
[H1 KHỞI TẠO] → [H2 THẨM ĐỊNH] → [H3 PHÁP LÝ] → [H4 VẬN HÀNH] → [H5 NGHIỆM THU]
```

Bản đồ tài liệu chuẩn theo từng loại nghiệp vụ (nghiên cứu, dự án đầu tư, mua sắm CNTT, **dự án CĐS Bank/Telco ↔ 11 giai đoạn**, **hợp đồng thiết bị IoT**): `references/ban-do-ho-so.md`. Bản đồ là **điểm xuất phát để đồng thiết kế**, không phải danh sách cứng.

---

## 2. Quy trình 3 bước chẩn đoán

### Bước 1 — Nhận diện nghiệp vụ & pha
Nghiệp vụ gì? Người duyệt cuối là ai? Trọng tâm thuyết phục (pháp lý / tài chính / năng lực / xử lý rủi ro)? Đang ở pha nào?

### Bước 2 — Lập Gap Matrix (mẫu: `references/mau-gap-matrix.md`)

Ba nhóm: **✅ ĐÃ CÓ** · **⚠️ CẦN BỔ SUNG NGAY** (thiếu thì không qua được pha kế) · **➡️ TÀI LIỆU TIẾP THEO**.

**Luật truy vết của Gap Matrix (không được bỏ):**

- Mỗi dòng ✅ phải có **đường dẫn file thật** (và ngày/bản). Không có đường dẫn → không được ghi ✅.
- **Trước khi ghi "thiếu / chưa ký / chưa có / hết hạn":** kiểm ở thư mục gốc khai trong `00_NGUON-HO-SO.md`, hoặc **hỏi người**. Không kết luận thiếu chỉ vì người dùng chưa tải lên. *(Luật sinh từ lỗi thật lặp hai lần 03/09 và 05/09/2026 — hạng mục đã xong bị báo là còn treo.)*
- Chưa kiểm được → trạng thái **"⚠️ chưa đối chiếu"**, không phải "thiếu".
- Người dùng nói "chưa có X" mà đĩa có X → tin đĩa, báo lại cho người dùng (luật cứng #1).

### Bước 3 — Điểm sẵn sàng (đếm, không ước)

```
Điểm sẵn sàng pha Hx = (số tài liệu BẮT BUỘC của pha Hx có trạng thái ✅ kèm đường dẫn)
                       / (tổng tài liệu BẮT BUỘC của pha Hx) × 100%
```

- Ghi kèm tử số/mẫu số và danh sách tài liệu được đếm. Cấm con số trần kiểu "khoảng 40%".
- Tài liệu "⚠️ chưa đối chiếu" **không tính vào tử số**; ghi riêng số lượng.
- Danh sách tài liệu bắt buộc phải được người dùng **xác nhận** ở bước đồng thiết kế trước khi điểm có hiệu lực.

---

## 3. Bóc tách định dạng — đo ni đóng giày

**Không đóng cứng mẫu.** Với mỗi tài liệu cần làm, dựng khung theo 4 bước: khám bản chất (mục tiêu, người duyệt, trọng tâm) → cây Word (Heading 1-2-3) → schema Excel (`Dashboard → Tính toán → Dữ liệu phẳng → Cấu hình`, cột và công thức theo bài toán) → mạch Slide (3 / 7 / 15 slide theo thời lượng).

| Định dạng | Dùng cho | Chuẩn SHT phải qua |
|---|---|---|
| Word `.docx` | Pháp lý, lập luận, trình ký | NĐ30 Tầng 1 cho mọi docx; Tầng 2 thể thức: tra bảng "Tình trạng công cụ sinh Tầng 2" trong `the-thuc-nd30.md` (tính đến 27/09/2026: 17 loại Mẫu 1.4 + CV + BB đã nghiệm thu; 6 mẫu riêng NQ/QĐ/CĐ/GM/GGT/GNP đã sinh, ⚠️ chờ QA + Gate 3; HĐ/biên bản ghi nhớ/thoả thuận/thư công theo mẫu nội bộ, chưa có file mẫu). Loại chưa nghiệm thu ghi "⚠️ chưa có mẫu Tầng 2 nghiệm thu" trong Gap Matrix. *(Sửa 30/09/2026, v0.29.0 — bản cũ ghi "chỉ có BB/CV/BC".)* Nghiệm thu: L4 `kiem_xuat_ban_docx.py` exit 0 **và** L4-W `kiem_word_nd30.py` exit 0. Thông số: `sht-nen-tang-kiem-chung/references/the-thuc-nd30.md` |
| Excel `.xlsx` | Số liệu, dự toán, KPI | Mọi con số truy được về nguồn (luật cứng #2); dùng skill `xlsx` để dựng |
| Slide `.pptx` | Trình bày lãnh đạo/hội đồng | Số liệu trên slide phải trùng Excel nguồn; dùng skill `pptx` |

Minh hoạ 4 ca bóc tách (tuyển dụng, giải trình sự cố, mua sắm CNTT, đề tài nghiên cứu): `references/ban-do-ho-so.md` §3.

**Đồng thiết kế (HITL):** luôn trình khung là *bản thiết kế sơ bộ* — "[X] mục Word · [Y] sheet Excel · [Z] slide" — và hỏi thêm/bớt/sửa gì **trước** khi chuyển sang soạn.

---

## 4. Nguồn dữ liệu — lấy ở đâu, chuyển cho ai

| Cần | Nguồn | Chuyển sang (skill SHT có thật) |
|---|---|---|
| Căn cứ pháp lý, điều khoản hợp đồng | VBQPPL, hợp đồng gốc | `ra-soat-hop-dong-vendor` (hợp đồng CNTT) · `sht-qd-nhansu-alignment` (QĐ tổ chức). `sht-phap-che-sot` (tra luật, trích nguyên văn Điều/Khoản, hiệu lực tại mốc vụ việc). Kết luận pháp lý thay luật sư: ngoài phạm vi skill → ghi "⚠️ cần chuyên gia pháp chế" *(sửa 30/09/2026, v0.28.8 — bản cũ ghi "SHT chưa có skill" dù `sht-phap-che-sot` có từ 0.28.0)* |
| Nội dung tài liệu đã có, bản scan | Thư mục gốc hồ sơ | `chuan-hoa-ho-so-tai-lieu` |
| Số liệu CRM / doanh số | Turso/Base.vn | `sht-normalize-account` → `sht-xacthuc-baocao-hoatdong` |
| Tên người, chức danh | QĐ bổ nhiệm, hợp đồng | `chuan-hoa-du-lieu-nhansu` |
| Biên bản từ ghi âm, hồ sơ XDCB | Transcript, ảnh hiện trường | `chuan-hoa-du-lieu-du-an` |
| Hiện trạng / PRD cho khách CĐS | Workspace khách | `sht-cds-danh-gia-hien-trang` → `sht-cds-thiet-ke-prd` |
| Phân tích thị trường, đơn giá ngành | — | **SHT chưa có skill** (đã lập việc riêng) → ghi "⚠️ chưa có nguồn kiểm chứng", không bịa số |

---

## 5. Mẫu phản hồi 4 khối

```markdown
### BẢN ĐỒ KIẾN TRÚC HỒ SƠ: [TÊN NGHIỆP VỤ]
Workspace: [ws] · Nguồn: 00_NGUON-HO-SO.md cập nhật [ngày]

#### 1. Định vị
- Pha hiện tại: H[x] ([tên pha])
- Điểm sẵn sàng H[x]: [a]/[b] tài liệu bắt buộc = [..]% (+ [c] tài liệu ⚠️ chưa đối chiếu)

#### 2. Gap Matrix
| TT | Tài liệu | Pha | Bắt buộc | Trạng thái | Bằng chứng (đường dẫn) | Định dạng & chuẩn | Nguồn dữ liệu / skill |

#### 3. Kế hoạch hành động
Bước 1..n — mỗi bước ghi skill SHT xử lý, người duyệt.

#### 4. Chờ duyệt
Anh/chị xác nhận danh sách tài liệu bắt buộc và khung bóc tách trước khi chuyển soạn.
```

---

## 6. Trước khi bàn giao

- Mọi dòng ✅ có đường dẫn; mọi "thiếu" đã kiểm thư mục gốc hoặc hỏi người.
- Điểm sẵn sàng có tử/mẫu số.
- Không trỏ tới skill không tồn tại trong `sht-skills`.
- Đầu ra nằm trong `data/workspaces/<ws>/` (hồ sơ khách) — không trong `THỰC HÀNH-AI/`.
- Checklist bàn giao chung: `sht-nen-tang-kiem-chung`.

Ca kiểm thử hành vi: `references/ca-kiem-thu.md`.
