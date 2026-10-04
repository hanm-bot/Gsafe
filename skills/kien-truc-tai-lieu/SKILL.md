---
name: kien-truc-tai-lieu
description: "Lập bản đồ tài liệu doanh nghiệp chung: vòng đời dự án, ma trận khoảng trống, nguồn thu thập, dàn ý. LUÔN dùng khi lên khung bộ tài liệu ngoài nghiệp vụ hồ sơ SHT. KHÔNG dùng cho hồ sơ SHT H1–H5 (sht-kien-truc-ho-so), trích chứng cứ (chuan-hoa-ho-so-tai-lieu), dựng file Office (xuat-ban-cong-vu). (dựa trên vietduc·ai)"
---

# Kiến Trúc Sư Hồ Sơ & Giải Pháp Tài Liệu Doanh Nghiệp (vietduc·ai Edition)

Hệ thống tư duy chiến lược dành cho **Kiến Trúc Sư Giải Pháp Tài Liệu**. Chuyển hóa người dùng từ "thợ gõ văn bản" thành chuyên gia nắm trọn bức tranh tổng thể của mọi nghiệp vụ hành chính, doanh nghiệp và nghiên cứu khoa học.

---

## 1. TỔNG QUAN HỆ THỐNG KIẾN TRÚC 3 TẦNG

```
┌─────────────────────────────────────────────────────────────────────────┐
│ TẦNG 1: CHẨN ĐOÁN VỊ TRÍ & MA TRẬN HỒ SƠ 5 GIAI ĐOẠN (GAP ANALYSIS)    │
│  - Tiếp nhận: Yêu cầu + Ngữ cảnh + Tài liệu hiện có                    │
│  - Định vị: Học viên đang ở giai đoạn nào trong 5 giai đoạn?           │
│  - Xuất ra: Ma trận đối chiếu (Đã có gì? Còn thiếu gì? Cần làm gì?)     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ TẦNG 2: BẢN ĐỒ ĐỊNH DẠNG & QUY CHUẨN THỂ THỨC (FORMAT SPECIFICATION)   │
│  - Word (.docx): Pháp lý, điều khoản, lập luận (Chuẩn NĐ 30 / Brand Kit)│
│  - Excel (.xlsx): Số liệu, dự toán, công thức động, dashboard KPI       │
│  - PowerPoint (.pptx): Trình chiếu bảo vệ, tóm tắt 5 phút lãnh đạo     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ TẦNG 3: CẨM NĂNG TRUY VẾT & THU THẬP NGUỒN DỮ LIỆU (DATA SOURCING)     │
│  - Nguồn Pháp lý & Quy chuẩn: Tra cứu Nghị định, Thông tư, Quy chế      │
│  - Nguồn Thực tế Nội bộ: ERP, CRM, Báo cáo tài chính, Voice-note họp    │
│  - Nguồn Tri thức Thị trường: Nghiên cứu ngành, Statista, Scholar       │
│  - Chỉ dẫn cụ thể: Lấy ở đâu? Bằng câu lệnh (Prompt) nào?               │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ [ĐIỀU PHỐI ĐẦU RA SANG xuat-ban-cong-vu ĐỂ XUẤT XƯỞNG TOÀN BỘ FILE]     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. TẦNG 1: QUY TẮC "VÒNG ĐỜI BỘ HỒ SƠ 5 GIAI ĐOẠN"

Mọi nghiệp vụ trong doanh nghiệp, cơ quan hay viện nghiên cứu **đều tuân thủ 5 giai đoạn bất biến**:

```
[1. KHỞI TẠO] ──► [2. THẨM ĐỊNH] ──► [3. PHÁP LÝ] ──► [4. VẬN HÀNH] ──► [5. NGHIỆM THU]
```

### 2.1. Bản Đồ Hồ Sơ Tham Chiếu Theo Các Nghiệp Vụ Điển Hình

| Giai Đoạn | Nghiệp vụ A: ĐỀ TÀI NGHIÊN CỨU | Nghiệp vụ B: DỰ ÁN KINH DOANH / ĐẦU TƯ | Nghiệp vụ C: MUA SẮM THIẾT BỊ / CNTT |
| :--- | :--- | :--- | :--- |
| **GĐ 1: Khởi tạo (Initiation)** | 1. Đề cương nghiên cứu sơ bộ<br>2. Phiếu đăng ký đề tài | 1. Tờ trình chủ trương đầu tư<br>2. Phiếu đề xuất dự án | 1. Phiếu đề xuất mua sắm thiết bị<br>2. Biên bản kiểm tra hiện trạng thiết bị cũ |
| **GĐ 2: Thẩm định (Appraisal)** | 1. Tổng quan tài liệu (Literature Review)<br>2. Bảng dự toán kinh phí nghiên cứu | 1. Báo cáo nghiên cứu khả thi (FS)<br>2. Bảng dự toán tài chính & Dòng tiền | 1. Bảng so sánh báo giá (ít nhất 3 đơn vị)<br>2. Bảng dự toán kinh phí tổng hợp |
| **GĐ 3: Pháp lý (Approval)** | 1. Quyết định phê duyệt đề tài<br>2. Biên bản họp Hội đồng xét duyệt<br>3. Hợp đồng nghiên cứu khoa học | 1. Quyết định phê duyệt dự án<br>2. Biên bản họp HĐQT / Ban Giám đốc<br>3. Hợp đồng kinh tế / Hợp đồng đối tác | 1. Tờ trình phê duyệt kinh phí mua sắm<br>2. Quyết định phê duyệt chỉ định/chào hàng<br>3. Hợp đồng mua bán thiết bị |
| **GĐ 4: Vận hành (Execution)** | 1. Phiếu khảo sát / Bảng dữ liệu thô<br>2. Báo cáo tiến độ định kỳ | 1. Quy trình thao tác chuẩn (SOP dự án)<br>2. Dashboard Excel theo dõi KPI hàng tuần | 1. Kế hoạch bàn giao & lắp đặt<br>2. Nhật ký bàn giao kỹ thuật |
| **GĐ 5: Nghiệm thu (Closure)** | 1. Báo cáo toàn văn đề tài (Full Report)<br>2. Tóm tắt đề tài (Executive Summary)<br>3. Slide PowerPoint bảo vệ Hội đồng | 1. Biên bản nghiệm thu dự án<br>2. Báo cáo tài chính quyết toán<br>3. Slide tổng kết dự án trước lãnh đạo | 1. Biên bản bàn giao & nghiệm thu thiết bị<br>2. Hồ sơ bảo hành & thanh quyết toán |

### 2.2. Quy Trình Chẩn Đoán Vị Trí & Phân Tích Khoảng Trống (Gap Matrix Workflow)

Khi học viên đưa vào một yêu cầu kèm tài liệu hiện có, Agent thực hiện **3 bước chẩn đoán**:

1. **Bước 1 - Nhận diện Nghiệp vụ & Vị trí**: Xác định học viên đang giải quyết nghiệp vụ gì và đang đứng ở giai đoạn nào (GĐ 1, 2, 3, 4 hay 5).
2. **Bước 2 - Lập Ma Trận Khoảng Trống (Gap Matrix)**:
   * **[ĐÃ CÓ]**: Tài liệu học viên đã cung cấp (kèm đánh giá chất lượng).
   * **[CẦN BỔ SUNG NGAY]**: Tài liệu then chốt đang thiếu để được duyệt qua bước tiếp theo.
   * **[TÀI LIỆU TIẾP THEO]**: Tài liệu chuẩn bị cho giai đoạn kế tiếp.
3. **Bước 3 - Tính Điểm Sẵn Sàng (Readiness Score)**: Ví dụ: *"Hồ sơ của bạn hiện đạt 40% (mới có Đề xuất và Ghi chép họp, thiếu Bảng dự toán và Dự thảo Tờ trình chính thức)"*.

---

## 3. TẦNG 2: BẢN ĐỒ ĐỊNH DẠNG & CƠ CHẾ BÓC TÁCH ĐỘNG THEO TỪNG NGHIỆP VỤ (DYNAMIC DECOMPOSITION)

> **NGUYÊN TẮC BẤT DI BẤT DỊCH:** Cấu trúc tài liệu **TUYỆT ĐỐI KHÔNG ĐƯỢC ĐÓNG CỨNG (NO HARDCODING)**. Không có một mẫu Word hay bảng Excel nào dùng chung cho mọi bài toán. Kiến trúc sư phải **"Đo ni đóng giày"** cấu trúc xương sống dựa trên đúng bản chất nghiệp vụ thực tế.

---

### 3.1. QUY TRÌNH 4 BƯỚC BÓC TÁCH ĐỘNG (THE 4-STEP ADAPTIVE PROCESS)

Khi học viên đưa vào một bài toán bất kỳ, Agent vận hành cỗ máy bóc tách động qua 4 bước:

```
[BƯỚC 1: KHÁM BỆNH BẢN CHẤT] ──► [BƯỚC 2: DỰNG CÂY WORD] ──► [BƯỚC 3: DỰNG SCHEMA EXCEL] ──► [BƯỚC 4: DỰNG NARRATIVE SLIDE]
  (Mục tiêu? Người nhận?           (Heading 1-2-3 tự sinh        (Các sheet & Trường dữ        (Mạch kể chuyện phù hợp
   Trọng tâm thuyết phục?)          theo ngữ cảnh)                liệu khớp bài toán)           thời lượng & bối cảnh)
```

1. **Bước 1 - Khám bệnh Bản chất Nghiệp vụ**:
   * *Mục tiêu tối thượng là gì?* (Xin duyệt tiền / Tuyển dụng / Giải trình sự cố / Báo cáo quản trị / Đề tài nghiên cứu / Chào thầu).
   * *Ai là đối tượng đọc & phê duyệt?* (Tổng Giám đốc / Hội đồng Khoa học / Cơ quan Nhà nước / Khách hàng B2B / Nội bộ phòng ban).
   * *Trọng tâm thuyết phục là gì?* (Tính pháp lý / Tính khả thi tài chính / Năng lực chuyên môn / Tốc độ xử lý rủi ro).
2. **Bước 2 - Tự động Dựng Sơ đồ Cây Word (Adaptive Information Tree)**:
   * Sinh cây phân cấp Heading 1 $\to$ Heading 2 $\to$ Heading 3 khớp 100% với bản chất bài toán.
3. **Bước 3 - Tự động Thiết kế Kiến trúc Sổ cái Excel (Adaptive Multi-Sheet & Data Schema)**:
   * Giữ nguyên lý: `Dashboard` $\to$ `Tính toán` $\to$ `Dữ liệu phẳng` $\to$ `Cấu hình`.
   * Nhưng **các Sheet, các Cột dữ liệu (Fields) và Công thức biến đổi hoàn toàn linh hoạt**.
4. **Bước 4 - Tự động Dựng Kịch bản Trình chiếu Slide (Adaptive Presentation Arc)**:
   * Co giãn nhịp điệu (3 slide ngắn, 7 slide chuẩn, hoặc 15 slide chuyên sâu) tùy thời lượng báo cáo.

---

### 3.2. MINH HỌA TÍNH LINH HOẠT TRÊN 4 NGHIỆP VỤ HOÀN TOÀN KHÁC NHAU

#### 📌 CASE 1: Nghiệp vụ "TUYỂN DỤNG & PHÁT TRIỂN NHÂN SỰ"
* **Word (Cây phân cấp tự sinh)**:
  * `I. Thực trạng & Nhu cầu định biên nhân sự` (Khối lượng công việc tăng, tỷ lệ nghỉ việc, năng suất hiện tại).
  * `II. Chân dung ứng viên & Khung năng lực ASHAM` (Mô tả công việc JD, Tiêu chuẩn tuyển chọn, KPIs yêu cầu).
  * `III. Kế hoạch tuyển dụng & Phân bổ kênh nguồn` (Kênh nội bộ, Headhunt, LinkedIn, Timeline phỏng vấn).
  * `IV. Dự toán chi phí & Chính sách đãi ngộ` (Ngân sách tìm kiếm, Quỹ lương thưởng, Quyền lợi ứng viên).
  * `V. Lộ trình đào tạo hòa nhập (Onboarding 30-60-90 ngày)`.
* **Excel (Data Schema động)**:
  * `Sheet Data_UngVien`: `Ma_UngVien`, `Ho_Ten`, `Vi_Tri`, `Kenh_Nguon`, `Diem_Test`, `Ket_Qua_PV`, `Luong_De_Xuat`, `Trang_Thai`.
  * `Sheet Cost_Model`: Chi phí tuyển dụng trên mỗi đầu người (Cost-per-hire), Thời gian tuyển dụng (Time-to-fill).
* **PowerPoint**: Nhấn mạnh vào khoảng trống nhân tài và lộ trình cung ứng nhân lực cho quý tới.

#### 📌 CASE 2: Nghiệp vụ "BÁO CÁO GIẢI TRÌNH SỰ CỐ / KHỦNG HOẢNG"
* **Word (Cây phân cấp tự sinh)**:
  * `I. Diễn biến sự cố & Nhật ký thời gian (Timeline log)`.
  * `II. Đánh giá mức độ thiệt hại & Phạm vi ảnh hưởng` (Tài chính, Dữ liệu, Khách hàng, Uy tín thương hiệu).
  * `III. Biện pháp ứng phó khẩn cấp đã triển khai` (Cô lập sự cố, Bồi thường, Truyền thông trấn an).
  * `IV. Phân tích nguyên nhân gốc rễ (Root Cause Analysis - 5 Whys & Fishbone)`.
  * `V. Biện pháp khắc phục triệt để & Kế hoạch phòng ngừa tái diễn`.
  * `VI. Đề xuất trách nhiệm & Quyết định xử lý nội bộ`.
* **Excel (Data Schema động)**:
  * `Sheet Log_SuCo`: `Timestamp`, `Phan_He_Loi`, `Nguoi_Phat_Hien`, `Muc_Do_Nghiem_Trong`, `Hanh_Dong_Xu_Ly`.
  * `Sheet Thiet_Hai_Financial`: Chi phí khắc phục, Chi phí đền bù, Doanh thu gián đoạn.
* **PowerPoint**: Slide ngắn 5 trang tập trung vào: "Chuyện gì đã xảy ra $\to$ Đã dập tắt thế nào $\to$ Làm sao để không bao giờ lặp lại".

#### 📌 CASE 3: Nghiệp vụ "MUA SẮM THIẾT BỊ / ĐẦU TƯ CÔNG NGHỆ"
* **Word (Cây phân cấp tự sinh)**:
  * `I. Căn cứ pháp lý & Đánh giá hiện trạng thiết bị cũ`.
  * `II. Yêu cầu kỹ thuật & Tiêu chuẩn tính năng mới`.
  * `III. Bảng so sánh 3 phương án chào giá thị trường`.
  * `IV. Bảng tổng hợp dự toán kinh phí & Nguồn vốn`.
  * `V. Kế hoạch nghiệm thu, bàn giao & Bảo hành`.
* **Excel (Data Schema động)**:
  * `Sheet Data_ThietBi`: `Ma_TB`, `Ten_TB`, `Hang_SX`, `So_Luong`, `Don_Gia`, `VAT`, `Tong_Tien`, `Nha_Cung_Cap`.
  * `Sheet Dashboard`: Tỷ trọng chi tiêu theo phòng ban, so sánh giá giữa các nhà thầu.

#### 📌 CASE 4: Nghiệp vụ "ĐỀ TÀI NGHIÊN CỨU KHOA HỌC"
* **Word (Cây phân cấp tự sinh)**:
  * `Mở đầu`: Lý do chọn đề tài, Mục tiêu, Câu hỏi & Giả thuyết nghiên cứu.
  * `Chương 1`: Cơ sở lý luận & Tổng quan tài liệu (Literature Review & Research Gap).
  * `Chương 2`: Phương pháp nghiên cứu, Thiết kế mẫu & Dữ liệu thực nghiệm.
  * `Chương 3`: Bàn luận kết quả, Đóng góp học thuật & Giải pháp ứng dụng.
  * `Kết luận, Danh mục tham khảo & Phụ lục`.
* **Excel (Data Schema động)**:
  * `Sheet Raw_Survey_Data`: `Respondent_ID`, `Question_1..N`, `Demographics`.
  * `Sheet Statistical_Model`: Bảng hồi quy, Giá trị P-value, Độ tin cậy Cronbach's Alpha.
* **PowerPoint**: Kịch bản 12 slide bảo vệ trước Hội đồng chấm luận văn.

---

### 3.3. NGUYÊN TẮC ĐỒNG THIẾT KẾ CÙNG HỌC VIÊN (CO-DESIGN INTERACTION)

Agent **không bao giờ áp đặt** một cấu trúc cứng mà luôn trình bày sơ đồ bóc tách dưới dạng **"Bản thiết kế sơ bộ (Architectural Draft)"** để học viên phản biện:

> *"Dựa trên nghiệp vụ **[Tên nghiệp vụ]** và đối tượng người đọc là **[Người nhận]**, tôi đã kiến trúc riêng cho bạn:*
> * 1. Sơ đồ cây văn bản Word gồm [X] mục chính.
> * 2. Kiến trúc bảng tính Excel gồm [Y] sheets với các trường thông tin đặc thù.
> * 3. Kịch bản bài slide gồm [Z] bước.
> 
> *Bạn xem qua cấu trúc này đã sát nhất với thực tế vận hành tại công ty/đơn vị của bạn chưa, hay cần thêm/bớt/sửa mục nào trước khi tiến hành xuất bản?"*

---

## 4. TẦNG 3: CẨM NĂNG TRUY VẾT & THU THẬP NGUỒN DỮ LIỆU

Agent trả lời chính xác 2 câu hỏi của học viên: **"Lấy ở đâu?"** và **"Lấy như thế nào?"**.

### 4.1. Tam Giác 3 Nguồn Dữ Liệu Cốt Lõi

```
                         [ NGUỒN 1: PHÁP LÝ & QUY CHUẨN ]
                              (Luật, Nghị định, Thông tư,
                              Quy chuẩn ISO, Quy chế nội bộ)
                                           ▲
                                           │
                        ┌──────────────────┴──────────────────┐
                        ▼                                     ▼
        [ NGUỒN 2: THỰC TẾ NỘI BỘ ]              [ NGUỒN 3: TRI THỨC THỊ TRƯỜNG ]
      (Báo cáo tài chính, ERP, CRM,              (Statista, Báo cáo ngành, Nghiên cứu
      Biên bản họp, Khảo sát, Voice-note)         đối thủ, Google Scholar, Tạp chí KH)
```

### 4.2. Hướng Dẫn Kỹ Thuật Khai Thác Bằng AI

| Loại Dữ Liệu Cần | Lấy Ở Đâu? | Công Cụ & Kỹ Thuật Khai Thác |
| :--- | :--- | :--- |
| **Căn cứ pháp lý, điều kiện phê duyệt, rà soát điều khoản** | Thư viện Pháp luật, Hệ thống VBQPPL, Cổng thông tin Chính phủ. | ⚖️ **KÍCH HOẠT SKILL `phap-che-doanh-nghiep`**: Định danh 5 trục (Chủ thể, Hành vi, Tác động, Phạm vi, Thời điểm) $\to$ Tra cứu chéo Luật-Nghị định-Thông tư $\to$ Trích dẫn nguyên văn Source of Truth (SOT) có tọa độ Điều/Khoản để làm căn cứ vững chắc cho văn bản. |
| **Số liệu hiện trạng, tồn đọng nội bộ** | File Excel kế toán, Báo cáo phòng ban, File ghi âm cuộc họp. | Nạp dữ liệu thô vào AI: *"Rà soát dữ liệu sau, tổng hợp thành bảng thống kê số lượng thiết bị hỏng, phân loại theo phòng ban và tính tỷ lệ hư hao."* |
| **Đơn giá, thông số kỹ thuật, khoảng trống ngách thị trường** | Báo giá nhà cung cấp, Khảo sát đối thủ, Cổng thông tin ngành. | 📊 **KÍCH HOẠT SKILL `tham-dinh-thi-truong`**: Mổ xẻ 8 lăng kính vòng quay nhu cầu, phát hiện khoảng trống ngách (Niche Vacuum) bị ông lớn bỏ quên, thẩm định Unit Economics và kiểm chứng 0-code. |
| **Cơ sở lý luận cho đề tài nghiên cứu** | Google Scholar, ResearchGate, Thư viện số luận văn. | Yêu cầu AI: *"Tóm lược 5 công trình nghiên cứu gần nhất về chủ đề [X], chỉ ra khoảng trống nghiên cứu (Research Gap) mà đề tài này sẽ giải quyết."* |

---

## 5. MẪU PHẢN HỒI CHUẨN CỦA KIẾN TRÚC SƯ HỒ SƠ

Khi người dùng đưa ra yêu cầu, Agent luôn phản hồi theo cấu trúc **4 Khối Chiến Lược**:

```markdown
### 🏛️ BẢN ĐỒ KIẾN TRÚC HỒ SƠ: [TÊN NGHIỆP VỤ]

#### 1. ĐỊNH VỊ VÒNG ĐỜI & CHẨN ĐOÁN
- **Vị trí hiện tại**: Giai đoạn [X] / 5 ([Tên giai đoạn])
- **Độ sẵn sàng hồ sơ**: [XX]%
- **Đánh giá**: [1-2 câu nhận xét về hiện trạng dữ liệu học viên cung cấp]

#### 2. MA TRẬN KHOẢNG TRỐNG HỒ SƠ (GAP MATRIX)
| TT | Tên Tài Liệu | Giai Đoạn | Tình Trạng | Định Dạng Chuẩn | Nguồn Dữ Liệu Cần Lấy |
|:---|:---|:---:|:---:|:---:|:---|
| 1 | [Tài liệu A] | GĐ 1 | ✅ Đã có sơ bộ | Word (NĐ 30) | Ghi chép nội bộ |
| 2 | [Tài liệu B] | GĐ 2 | ⚠️ CẦN LÀM NGAY | Excel (Live formula) | Khảo sát qua skill tham-dinh-thi-truong |
| 3 | [Tài liệu C] | GĐ 3 | ⚖️ CẦN THẨM ĐỊNH | Word (Hợp đồng/Tờ trình)| Tra cứu qua skill phap-che-doanh-nghiep |

#### 3. KẾ HOẠCH HÀNH ĐỘNG CỤ THỂ (ACTION PLAN)
- **Bước 1**: [Kích hoạt tham-dinh-thi-truong để bóc tách nhu cầu & ngách thị trường]
- **Bước 2**: [Kích hoạt phap-che-doanh-nghiep để lấy căn cứ pháp lý & điều khoản hợp đồng]
- **Bước 3**: [Chuyển giao toàn bộ sang xuat-ban-cong-vu để xuất xưởng trọn bộ]

#### 4. KÍCH HOẠT DÂY CHUYỀN XUẤT XƯỞNG
👉 Gõ **[THỊ TRƯỜNG]** để chuyển sang **tham-dinh-thi-truong** phân tích ngách và Unit Economics.
👉 Gõ **[PHÁP LÝ]** để chuyển sang **phap-che-doanh-nghiep** thẩm định điều khoản và lấy SOT.
👉 Gõ **[BẮT ĐẦU]** để chuyển sang **xuat-ban-cong-vu** xuất bản file chuẩn ngay lập tức!
```

---

## 6. SƠ ĐỒ PHỐI HỢP LIÊN HOÀN (vietduc·ai Master Architecture)

```
┌────────────────────────────────────────────────────────┐
│               1. KIẾN TRÚC SƯ HỒ SƠ                    │
│                (kien-truc-tai-lieu)                    │
│   - Bắt bệnh nghiệp vụ & định vị 5 giai đoạn           │
│   - Lập ma trận khoảng trống (Gap Matrix)              │
│   - Bóc tách sơ đồ cây động thích ứng từng ngành       │
└──────────────────────────┬─────────────────────────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
┌──────────────────────────┐  ┌──────────────────────────┐
│   2. PHÁP CHẾ SỐ         │  │   3. THỊ TRƯỜNG OPC      │
│   (phap-che-doanh-nghiep)     │  │ (tham-dinh-thi-truong│
│ - Định danh 5 trục       │  │ - 8 lăng kính vòng quay  │
│ - Tra cứu chéo SOT       │  │ - Tìm khoảng trống ngách │
│ - Đòn phản công giả lập  │  │ - Unit Economics & 0-code│
└────────┬─────────────────┘  └────────┬─────────────────┘
         │                             │
         └──────────────┬──────────────┘
                        ▼
┌────────────────────────────────────────────────────────┐
│               4. AI OFFICE MASTER                      │
│                (xuat-ban-cong-vu)                      │
│   - Nhận cấu trúc hồ sơ, SOT luật & phân tích thị trường│
│   - Xuất xưởng file Word NĐ 30 chuẩn thể thức chính phủ│
│   - Xuất xưởng Excel sống 4 sheets (Data + Formulas)   │
│   - Xuất xưởng Slide PowerPoint Pitch Deck chuyên nghiệp│
└────────────────────────────────────────────────────────┘
```

---

## Tác giả & Bản quyền Phương pháp
*Ghi chú phát hành SHT (0.31.3): mục này cố ý lặp ở 5 skill dựa trên vietduc·ai (`chap-but-lanh-dao`, `kien-truc-tai-lieu`, `phap-che-doanh-nghiep`, `tham-dinh-thi-truong`, `xuat-ban-cong-vu`) để ghi công tác giả đi cùng từng skill khi được dùng riêng; không định nghĩa lại quy tắc nghiệp vụ nào.*


**Hệ Thống AI Workforce Doanh Nghiệp (vietduc·ai)**  
Chuyên gia Đào tạo & Chuyển giao Giải pháp Tự động hóa AI Doanh nghiệp  
Hệ sinh thái: **vietduc.ai**
