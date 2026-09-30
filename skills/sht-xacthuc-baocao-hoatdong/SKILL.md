---
name: "sht-xacthuc-baocao-hoatdong"
description: "Xác thực số liệu báo cáo kinh doanh SHT với hệ thống nguồn (Turso/Base.vn CRM, dashboard) TRƯỚC khi vào văn bản chính thức: truy từng số về truy vấn sinh ra nó, phát hiện lệch do dữ liệu cũ, gắn nhãn đã/chưa đối chiếu. LUÔN dùng khi soạn/rà báo cáo doanh số, KPI, pipeline, QĐ căn cứ thành tích, hoặc nói \"số này lấy ở đâu\", \"đối chiếu với CRM\". KHÔNG dùng để gộp account (sht-normalize-account) hay soạn thể thức QĐ (sht-qd-nhansu-alignment)."
---

# Xác thực báo cáo hoạt động kinh doanh (SHT)

Một con số chưa kiểm chứng lọt vào Quyết định bổ nhiệm hay báo cáo trình Ban lãnh đạo thì rất khó rút lại — nó đã thành căn cứ. Skill này chặn ở khâu trước đó.

Nguyên tắc: **mỗi con số trong báo cáo phải truy được về câu truy vấn hoặc màn hình đã sinh ra nó.** Con số không truy được xuất xứ thì không được đưa vào văn bản chính thức, dù nghe có vẻ hợp lý.

Ranh giới: skill này lo **tính đúng đắn của con số**. Việc gộp account/chi nhánh là của `sht-normalize-account`; thể thức và thẩm quyền văn bản là của `sht-qd-nhansu-alignment`; quy tắc bàn giao chung là của `sht-nen-tang-kiem-chung`.

---

## LUỒNG CHUẨN

```
[1] Liệt kê mọi con số trong báo cáo, đánh dấu số nào là căn cứ ra quyết định   (§1)
[2] Với mỗi số → truy về nguồn, ghi lại câu truy vấn/màn hình                    (§2)
[3] Đối chiếu — lệch thì truy nguyên nhân, KHÔNG vội kết luận ai sai             (§3)
[4] Gắn nhãn ba trạng thái: đã đối chiếu / lệch có giải thích / chưa kiểm được   (§4)
[5] Bàn giao kèm bảng truy vết                                                    (§5)
```

Báo cáo **kể việc** ("đã chốt", "đã xong", "KH đồng ý") thay vì con số: chạy thêm §7.

---

## 1. Phân loại con số trước khi kiểm

Không phải con số nào cũng đáng bỏ công. Chia ba nhóm:

| Nhóm | Ví dụ | Mức kiểm |
|---|---|---|
| **Căn cứ ra quyết định** | Doanh số làm căn cứ bổ nhiệm, % hoàn thành KPI, số hợp đồng ký | **Bắt buộc** truy về truy vấn gốc, không có ngoại lệ |
| **Bối cảnh** | Tổng số deal trong pipeline, số khách hàng đang chăm | Đối chiếu, chấp nhận sai số nếu ghi rõ ngày chốt số |
| **Minh họa** | "khoảng 20 chi nhánh", "gần một nửa" | Chỉ cần không mâu thuẫn với nhóm trên |

Nếu người dùng đưa một báo cáo và hỏi "kiểm giúp", **hỏi ngay con số nào sẽ thành căn cứ ra quyết định** — đó là danh sách phải kiểm kỹ.

---

## 2. Truy về nguồn — biết trước bẫy của hệ thống

Nguồn: SHT Sales Pipeline (Turso libSQL, `/v2/pipeline`), đồng bộ ~2h/lần từ Base.vn CRM. Token read-only, **không nhúng vào tài liệu hay skill**.

Năm bảng: `deals` (khóa `ma`), `staff` (khóa `id`), `purchase_txns`, `kpi_targets`, `audit_log`.

**Bốn bẫy làm sai số liệu — kiểm trước khi tin kết quả truy vấn:**

1. **Lọc giai đoạn phải dùng `stageId` (1–12), KHÔNG dùng `stageName`.** Tên hiển thị đổi theo thời gian; báo cáo cũ lọc theo tên sẽ ra số khác báo cáo mới.
2. **AM ≠ Executor.** AM (người phụ trách, cố định) = JOIN `deals.amUser` ↔ `staff.username`; cột `am` thường rỗng hoặc `[EXTERNAL]`. `executor` là người làm bước hiện tại, đổi theo giai đoạn. Quy doanh số cho executor thay vì AM là lỗi kinh điển.
3. **Nghỉ việc đọc ở `staff.status`**, KHÔNG dùng `amStatus`/`executorStatus` (chỉ là state thô của Base.vn).
4. **Gộp account theo `ma`, KHÔNG theo `kh`.** Chi tiết ở `sht-normalize-account` — làm sai chỗ này tách 1 chi nhánh thành hàng trăm account ảo, mọi con số "số khách hàng" đều hỏng.

**Ý nghĩa giai đoạn:** `1,2,3` = CHKD (Tiếp nhận → Thuyết phục → Chốt); `4–9` = Sales (Tiếp nhận PAKD → Hồ sơ → Ký HĐ → Triển khai → Xuất hóa đơn → Thu tiền); `10` = Done; `11` = Failed CHKD; `12` = Failed Sales.

Hai lỗi phạm vi hay gặp: gộp `11`/`12` vào "đang chạy", và tính "đã ký" mà quên rằng `6` (Ký HĐ) khác `9` (Thu tiền) — doanh số ghi nhận theo mốc nào phải nói rõ.

**Target cá nhân của AM nằm ở Google Sheet ngoài**, không có trong `kpi_targets` (bảng này chỉ có target theo team/nhóm). Đừng tính % hoàn thành cá nhân từ `kpi_targets`.

Với mỗi con số, ghi lại: **câu truy vấn hoặc màn hình + thời điểm chốt số**. Vì hệ thống đồng bộ 2h/lần, hai người chạy cách nhau vài giờ sẽ ra số khác nhau mà cả hai đều đúng.

---

## 3. Khi lệch — truy nguyên nhân, đừng vội kết luận ai sai

Đây là phần quan trọng nhất của skill này.

**Không có nguồn nào mặc định đúng hơn.** Dashboard có thể lỗi thời; người báo cáo có thể nắm thông tin hệ thống chưa cập nhật.

Thứ tự truy khi thấy lệch:

1. **Khác phạm vi?** Hai bên có cùng khoảng thời gian, cùng `stageId`, cùng cách quy AM không? Phần lớn ca lệch dừng ở đây.
2. **Khác thời điểm chốt số?** Chênh một chu kỳ đồng bộ là đủ lệch.
3. **Dữ liệu hệ thống lỗi thời?** Nhân sự nghỉ việc/chuyển bộ phận chưa cập nhật, deal đã ký chưa đẩy lên.
4. **Chỉ khi loại hết ba khả năng trên** mới xét khả năng một bên tính sai.

**Ca thật:** dashboard CRM liệt kê 10 AM thuộc một trung tâm kinh doanh, người phụ trách báo "5/8". Nếu kết luận ngay là người báo cáo nhầm thì đã sai — truy tiếp phát hiện 2 trong 10 AM đã nghỉ việc mà hệ thống chưa cập nhật; loại ra thì khớp chính xác. **Hệ thống mới là bên có dữ liệu lỗi thời.**

Khi lệch chưa giải thích được, **hỏi người phụ trách một câu cụ thể** ("có ai nghỉ việc/chuyển bộ phận/deal nào chưa đẩy lên hệ thống không?") thay vì báo chung chung là "số liệu không khớp".

---

## 4. Gắn nhãn ba trạng thái — không có trạng thái thứ tư

Mọi con số trong báo cáo bàn giao phải mang đúng một nhãn:

| Nhãn | Nghĩa | Được dùng làm căn cứ? |
|---|---|---|
| ✅ **Đã đối chiếu** | Khớp nguồn, có câu truy vấn + thời điểm chốt | Có |
| ⚠️ **Lệch có giải thích** | Không khớp nhưng đã truy ra nguyên nhân, ghi rõ | Có, kèm ghi chú nguyên nhân |
| ❓ **Chưa kiểm được** | Không truy được nguồn, hoặc nguồn không tồn tại | **Không** |

Cấm tuyệt đối: để một con số trôi vào văn bản chính thức mà không mang nhãn nào. Nếu người dùng giục gấp, vẫn phải nêu rõ con số nào đang ở nhãm ❓ — để họ quyết định chịu rủi ro, chứ không phải để mình quyết thay.

Không tự chọn một bên khi hai nguồn mâu thuẫn. Ghi cả hai kèm nguyên nhân vào mục "Vấn đề bỏ ngỏ", kể cả khi được yêu cầu rút gọn.

---

## 5. Bàn giao

Áp checklist chung ở `sht-nen-tang-kiem-chung` §5, cộng thêm bảng truy vết:

| Con số | Giá trị | Nguồn / truy vấn | Thời điểm chốt | Nhãn |
|---|---|---|---|---|

Bổ sung riêng cho báo cáo hoạt động:

- [ ] Mọi con số nhóm "căn cứ ra quyết định" đều mang nhãn ✅ hoặc ⚠️, **không còn ❓**
- [ ] Đã ghi rõ mốc ghi nhận doanh số (ký HĐ hay thu tiền) — không để mập mờ
- [ ] Đã kiểm quy AM theo `amUser`↔`staff.username`, không theo cột `am` hay executor
- [ ] Đã kiểm lọc giai đoạn theo `stageId`, không theo `stageName`
- [ ] Nếu có đếm khách hàng/chi nhánh: đã gộp theo `ma` (qua `sht-normalize-account`), có dòng tự kiểm số CN
- [ ] Thời điểm chốt số ghi ngay trên báo cáo, không để người đọc tự đoán
- [ ] Token/chuỗi kết nối **không** xuất hiện trong bất kỳ file bàn giao nào

---

## 6. Khi số liệu đi vào Quyết định nhân sự

Ca đặc biệt, mức rủi ro cao nhất: một QĐ bổ nhiệm căn cứ "thành tích doanh số/KPI/hoạt động Engage".

- Chạy đủ §1–§4 **trước khi** soạn văn bản, không phải sau khi đã dựng xong file.
- Con số ở nhãn ❓ **không được đưa vào phần Căn cứ** của QĐ. Nếu người dùng vẫn muốn, đề nghị chuyển sang diễn đạt định tính, hoặc lùi ngày ban hành để kiểm xong.
- Chốt danh tính người được nhắc bằng `chuan-hoa-du-lieu-nhansu` trước; thẩm quyền và thể thức theo `sht-qd-nhansu-alignment`.
- Ghi thời điểm chốt số vào phần Căn cứ ("theo số liệu SHT Sales Pipeline chốt ngày …") — QĐ không ghi mốc thời gian sẽ không bảo vệ được khi số liệu thay đổi về sau.

---

## 7. Khi báo cáo kể kết quả thay vì nêu con số

Báo cáo Engage/hoạt động thường viết "chốt", "đã xong", "thiện chí". Mỗi câu như vậy là một tuyên bố cần đối chiếu như một con số.

1. **Tách từng dòng thành** đối tượng (khách hàng/chi nhánh/mã) + tuyên bố kết quả.
2. **Bắt câu tự mâu thuẫn.** Ví dụ "Chốt… CN sẽ báo lại số lượng sau": "chốt" thật không thể đi kèm "chưa có số lượng" — dấu hiệu nhãn bị thổi phồng.
3. **Đối chiếu với hệ thống gốc:** có hồ sơ/mã tương ứng không; hồ sơ đang ở `stageId` nào so với giai đoạn báo cáo ngầm định; **ngày tạo hồ sơ** có khớp thời điểm hoạt động không, hay hồ sơ đã có từ trước (việc cũ bị kể thành việc mới). ⚠️ Tên cột ngày tạo trong bảng `deals` chưa được đối chiếu với schema thật — kiểm trước khi viết truy vấn.
4. **Xếp lại theo thang tiến độ 3 mức** (thang này đo *tiến độ* của việc; nhãn ✅/⚠️/❓ ở §4 vẫn đo *độ tin* của bằng chứng — dùng cả hai):

| Mức | Điều kiện |
|---|---|
| Đã chốt | Có số lượng/giá trị cụ thể **và** hồ sơ hệ thống khớp giai đoạn tương ứng |
| Thiện chí | Đồng ý nguyên tắc nhưng thiếu số lượng/giá trị, hoặc hồ sơ mới ở giai đoạn đầu |
| Đang theo dõi | Đưa vào kế hoạch tương lai, chưa có hành động cụ thể trong kỳ |

Không tự đặt thang khác trừ khi người dùng yêu cầu — thang càng đơn giản càng áp nhất quán cho cả đội.

5. **Bàn giao hai bảng tách riêng:** (a) bảng báo cáo đã điền lại — Đối tượng · Gặp ai/Phụ trách · Công việc · Kết quả đã rà soát; (b) bảng rà soát tuân thủ — từng tiêu chí đạt/không kèm bằng chứng. Không gộp.
6. **Kết luận ghi rõ** đây là cải thiện quy trình báo cáo, không phải đánh giá năng lực cá nhân — trừ khi người dùng yêu cầu đánh giá.

**Đừng bỏ cột chỉ để "gọn".** Cột "AM phụ trách" tưởng là hành chính nhưng là căn cứ đối chiếu ngược Ownership của AM. Trước khi bỏ một trường, hỏi: nó còn phục vụ mục đích nào khác không? Nếu có, thu gọn (tên ngắn, mã) thay vì xoá.
