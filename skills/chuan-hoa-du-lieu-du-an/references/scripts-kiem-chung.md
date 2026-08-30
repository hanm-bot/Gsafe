# Bộ script kiểm chứng ngược

Chạy trước khi bàn giao bất kỳ deliverable nào dựng từ transcript.

### B1. Đối chiếu timestamp — kết quả PHẢI rỗng

```bash
# Trích timestamp từ nguồn (đầu dòng) và từ deliverable (bất kỳ vị trí nào)
grep -o "^\[[0-9][0-9]:[0-9][0-9]\]" transcript.md | tr -d '[]' | sort -u > src.txt
pdftotext deliverable.pdf - | grep -o "\[[0-9][0-9]:[0-9][0-9]\]" | tr -d '[]' | sort -u > out.txt

# Timestamp CÓ trong deliverable nhưng KHÔNG có trong nguồn = BỊA
comm -13 src.txt out.txt
```

Nếu dòng lệnh cuối in ra bất cứ thứ gì → có timestamp bịa, phải sửa trước khi bàn giao.

### B2. Đối chiếu số liệu then chốt

```bash
for s in "bốn trăm sáu mươi nghìn" "ba trăm nghìn" "một trăm triệu" "94 ngày"; do
  printf "%s  <- %s\n" "$(grep -c "$s" transcript.md)" "$s"
done
```

Mọi con số trong deliverable phải có count ≥ 1 trong nguồn. Lưu ý: `pdftotext` ngắt dòng giữa cụm từ dài — kiểm cụm dài bằng `pandoc -t plain file.docx | tr '\n' ' ' | grep -o "..."`.

### B3. Quét ký tự rác trong transcript (chạy ở CỔNG 1)

```bash
grep -n -E "(^| )[bcdghklmnprstvx]( [bcdghklmnprstvx]){2,}" transcript.md
```

Có kết quả → transcript không dùng được, yêu cầu transcribe lại.

### B4. Render và nhìn tận mắt

```bash
soffice --headless --convert-to pdf out.docx
pdftoppm -jpeg -r 100 out.pdf page
# rồi ĐỌC từng ảnh page-*.jpg
```

### B5. Trích metadata & thứ tự ảnh nhúng trong .docx gốc

```bash
# Ngày tạo/tác giả thật của file
unzip -p file.docx docProps/core.xml

# Thứ tự ảnh nhúng trong thân văn bản (VML cũ)
unzip -p file.docx word/document.xml | grep -o 'v:imagedata r:id="rId[0-9]*"'
# hoặc DrawingML mới
unzip -p file.docx word/document.xml | grep -o 'r:embed="rId[0-9]*"'

# Map rId -> tên file ảnh trong word/media/
unzip -p file.docx word/_rels/document.xml.rels

# Watermark header (nếu có) — ảnh thường "mồ côi", không nằm trong danh sách trên
unzip -p file.docx word/_rels/header1.xml.rels
```

### B6. Giải mã epoch timestamp trong tên file ảnh mạng xã hội

```bash
# Tên file dạng 1785929516662_<id>_<id>_<hash>.jpg -> 13 chữ số đầu là epoch ms
date -d @1785929516 -u   # bỏ 3 số cuối (ms -> s), cộng 7h ra giờ VN
```

