# GĐ 6 — Báo cáo trình Ban lãnh đạo

## Cấu trúc báo cáo ứng viên — 10 mục bắt buộc

1. Kết luận sơ bộ
2. Tổng điểm phù hợp
3. Mức độ tin cậy của đánh giá
4. Điểm mạnh nổi bật
5. Khoảng trống so với yêu cầu
6. Rủi ro tuyển dụng — **đánh mã R1, R2, R3...** để tiện theo dõi ở các bước sau
7. Thông tin cần xác minh
8. Câu hỏi phỏng vấn đề xuất
9. Bài tập tình huống nên giao
10. Khuyến nghị bước tiếp theo

Mỗi điểm số phải giải thích bằng bằng chứng cụ thể (trang CV hoặc timestamp transcript). Không đưa một con số tổng rồi thôi.

Kết thúc bằng câu: *"Quyết định tuyển/loại cuối cùng cần có sự phê duyệt của HR và Ban lãnh đạo — báo cáo này là input hỗ trợ, không thay thế quyết định của Hội đồng."*

---

## Pipeline PDF infographic

### Chuẩn bị môi trường
```bash
pip install weasyprint --break-system-packages
mkdir -p fonts
BASE="https://raw.githubusercontent.com/google/fonts/main"
curl -sL -o fonts/SpaceGrotesk-Bold.ttf    "$BASE/ofl/spacegrotesk/SpaceGrotesk%5Bwght%5D.ttf"
curl -sL -o fonts/Inter-Variable.ttf       "$BASE/ofl/inter/Inter%5Bopsz%2Cwght%5D.ttf"
curl -sL -o fonts/IBMPlexMono-Regular.ttf  "$BASE/ofl/ibmplexmono/IBMPlexMono-Regular.ttf"
curl -sL -o fonts/IBMPlexMono-SemiBold.ttf "$BASE/ofl/ibmplexmono/IBMPlexMono-SemiBold.ttf"
```

### Ba khai báo BẮT BUỘC
```css
@page { size: A4 landscape; margin: 0; }   /* hoặc: size: A4; cho khổ dọc */
```
```python
HTML('report.html', base_url='.').write_pdf('out.pdf')   # thiếu base_url → font không nạp
```
```css
.page { width:297mm; height:210mm; overflow:hidden; }    /* khổ dọc: 210mm x 297mm */
```

> **Lỗi đã gặp thực tế:** thiếu `@page` → WeasyPrint dùng khổ Letter mặc định + margin mặc định → toàn bộ cột phải của mọi trang bị cắt. Lỗi này **không phát hiện được bằng cách xem ảnh render**, vì ảnh render ra chính là bản đã bị cắt nên trông vẫn "bình thường".

### Bảng màu & font chuẩn SHT
```css
--bg:#EEF1F4;  --panel:#FFF;   --ink:#0E1621;  --tx:#1D2A36;  --tx2:#5C6B78;  --tx3:#8A97A3;
--line:#E2E7EC; --line2:#CDD5DD; --accent:#0E6E63; --chip:#EAF3F1;
--xanh:#128A63; --xanhbg:#E4F3EC;   /* đạt / tích cực */
--vang:#C67F12; --vangbg:#FBF0DA;   /* cần làm rõ */
--do:#C93B3B;   --dobg:#FBE7E7;     /* rủi ro */
--disp:'Space Grotesk'; --body:'Inter'; --mono:'IBM Plex Mono';
```

### Bố cục khổ ngang (chống khoảng trắng thừa)
```css
.page      { display:flex; flex-direction:column; }
.body-wrap { flex:1; display:flex; flex-direction:column; min-height:0; }
.cols      { display:flex; gap:5mm; flex:1; min-height:0; }
.col.left  { flex:0 0 36%; }   /* hoặc 41% / 47% tùy nội dung */
.col.right { flex:1; }
```

Chia cột theo trang:
- **Trang tổng quan:** trái = kết luận + chỉ số lớn · phải = biểu đồ + bảng bằng chứng
- **Trang so sánh:** bảng full-width ở trên · 2 cột (điểm mạnh | rủi ro) ở dưới
- **Trang khuyến nghị:** 3 thẻ chỉ số ngang trên cùng · dưới chia 2 cột (đề xuất | lộ trình dạng lưới 2×2)

### QA BẮT BUỘC — ba phép kiểm tra định lượng
Xem ảnh bằng mắt là **không đủ**. Luôn chạy cả ba:

```bash
# 1. Đúng khổ giấy? A4 dọc = 595x842pt · A4 ngang = 842x595pt
pdfinfo out.pdf | grep -E "Pages|Page size"

# 2. Có chữ nào bị mất không? (đặc biệt cột phải)
pdftotext -layout out.pdf - | head -20

# 3. Nội dung tràn lề hay thừa khoảng trắng?
pdftoppm -png -r 110 out.pdf page
python3 -c "
from PIL import Image; import numpy as np
import glob
for f in sorted(glob.glob('page-*.png')):
    a = np.array(Image.open(f).convert('L')); h,w = a.shape
    m = a < 230
    r = np.where(m.any(axis=1))[0]; c = np.where(m.any(axis=0))[0]
    print(f, 'lề phải:', w-1-c.max(), 'px · lề dưới:', h-1-r.max(), 'px')
"
```

Lề phải và lề dưới nên xấp xỉ nhau và tương ứng padding đã đặt. Lề dưới lớn bất thường → còn khoảng trắng thừa, bố cục lại. Lề phải ≈ 0 → đang bị tràn/cắt.

### Cấu trúc 3 trang chuẩn
| Trang | Nội dung |
|---|---|
| 1 | Kết luận sơ bộ · Điểm ASK trước/sau PV · Bảng bằng chứng đóng khoảng trống (kèm timestamp) |
| 2 | Benchmark với nhân sự nội bộ · Điểm mạnh xác nhận · Rủi ro R1-R4 |
| 3 | Chỉ số tóm tắt · Đề xuất quyết định · Lộ trình onboarding · Khung ký duyệt |

Footer mọi trang: `CÔNG TY CP ĐẦU TƯ CÔNG NGHỆ SHT — TÀI LIỆU MẬT, LƯU HÀNH NỘI BỘ HỘI ĐỒNG TUYỂN DỤNG`

---

## Định dạng đầu ra khác

Tùy yêu cầu, có thể dùng: bảng kế hoạch triển khai · bản mô tả công việc · khung năng lực · ma trận chấm điểm · phiếu đánh giá ứng viên · báo cáo shortlist · bộ câu hỏi phỏng vấn.

Tài liệu dùng để phân phối nên xuất **cả DOCX và PDF**.
