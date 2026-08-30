---
name: "chuan-hoa-du-lieu-du-an"
description: >-
  Kiểm chứng nguồn và dựng tài liệu dự án XDCB/thiết kế/nội thất của SHT — bốn cổng kiểm transcript ghi âm, xác định đúng người phát ngôn bằng bằng chứng trong âm thanh, truy vết từng ý về mốc thời gian có thật, đối chiếu chéo nhiều nguồn để lộ mâu thuẫn, kiểm chứng ngày tháng qua metadata file và epoch timestamp ẩn trong tên ảnh, giữ nguyên thể thức và watermark khi phục dựng văn bản hành chính gốc.
  LUÔN dùng khi soạn biên bản họp từ ghi âm/transcript, cần prompt transcribe, lập bảng tiến độ, công văn, báo cáo khảo sát; hoặc khi người dùng nói "sửa số liệu", "sửa người nói", "giữ nguyên template gốc", "ảnh này chụp ngày nào" — kể cả khi không nhắc chữ "chuẩn hóa".
  Dùng KÈM sht-nen-tang-kiem-chung, và chuan-hoa-du-lieu-nhansu khi tài liệu có tên người.
  KHÔNG dùng cho ứng viên tuyển dụng hay dữ liệu CRM.

---

# Dữ liệu & tài liệu dự án XDCB / nội thất (SHT)

Quy trình làm việc với dữ liệu dự án XDCB, thiết kế & nội thất: từ nguồn thô (ghi âm, báo giá, bản vẽ, ảnh chat, file gốc của khách hàng) đến deliverable cuối (biên bản, Excel, công văn, infographic, báo cáo khảo sát PDF/docx).

Nguyên tắc bao trùm: **dữ liệu sai lan nhanh hơn dữ liệu đúng.** Một con số sai trong file nguồn sẽ nhân bản ra 4–5 deliverable; một cái tên bị thay nhầm sẽ đi thẳng vào văn bản trình ký. Mọi bước dưới đây tối ưu cho việc *chặn lỗi sớm* thay vì sửa muộn.

**Quy tắc nền dùng chung nằm ở `sht-nen-tang-kiem-chung`** — lan truyền hiệu chỉnh, đổi tên hàng loạt an toàn (kèm danh sách cụm bảo vệ), một-tài-liệu-một-bản-có-hiệu-lực, checklist bàn giao chung. Nạp kèm skill đó trong mọi phiên; file này chỉ giữ phần đặc thù dự án.

> **Prompt transcribe và script kiểm chứng nằm ngay trong file này**, ở Phụ lục A và B. Các file trong `references/` là bản cũ hơn — khi mâu thuẫn, lấy nội dung trong file này làm chuẩn.

---

## LUỒNG CHUẨN: GHI ÂM → BIÊN BẢN

```
[1] Transcribe verbatim (Phụ lục A)
     ↓
[2] BỐN CỔNG KIỂM — trượt cổng 1 là DỪNG HẲN (§1)
     ↓
[3] Xác định người phát ngôn + hỏi người dùng xác nhận (§2)
     ↓
[4] Dựng deliverable, truy vết từng ý về nguồn (§5)
     ↓
[5] Đối chiếu ngược bằng script — phải rỗng (Phụ lục B)
     ↓
[6] Render ảnh, nhìn tận mắt → bàn giao + hủy bản cũ (nền §3, §5)
```

Không được nhảy cóc. Mỗi bước bỏ qua đều đã từng gây ra một deliverable phải hủy.

Luồng tương tự áp dụng khi đầu vào là **file khảo sát/báo cáo gốc của khách hàng hoặc đội hiện trường** thay vì ghi âm: thay bước [1]–[2] bằng đối chiếu chéo nhiều file gốc + kiểm chứng qua metadata (§1.3), và ở bước [4] cân nhắc kỹ khi cần "giữ nguyên bản template/ảnh tư liệu" (§9).

---

## 1. Kiểm chứng nguồn trước khi sản xuất

### 1.1 Transcript từ AI — bốn cổng kiểm bắt buộc

**Cổng 1 — Ký tự rác = TÍN HIỆU DỪNG, không phải cảnh báo.**

Nếu transcript chứa chuỗi phụ âm rời rạc vô nghĩa (`s d h l b`, `d h n cho d rẻ s`, `r s r`, `h l l b h b s s`), đó là model gõ bừa để lấp chỗ nó không nghe được. **Tuyên bố transcript không dùng được, yêu cầu transcribe lại.**

Tuyệt đối không "vẫn dựng deliverable rồi gắn nhãn [ĐỘ TIN CẬY THẤP]" — đó là hợp thức hóa dữ liệu bịa. Đã từng làm và phải hủy nguyên một biên bản.

**Cổng 2 — Dấu hiệu đã bị "làm mượt".**

Transcript thật của cuộc họp tiếng Việt **phải** lộn xộn: từ đệm (ạ, dạ, ừm, đấy, vâng), câu dở dang, ngắt lời, lặp từ, cross-talk, nhãn nghe không rõ. Văn bản trôi chảy, câu nào cũng hoàn chỉnh → model đã tóm tắt và **bịa**.

**Cổng 3 — Độ phủ thời lượng.**

Yêu cầu dòng `Tổng thời lượng: mm:ss — Đã transcribe đến: mm:ss` ở đầu output. Hai số lệch = có đoạn bị bỏ. Đối chiếu thêm độ dài văn bản với thời lượng ghi âm.

**Cổng 4 — Bỏ qua phần tự đánh giá độ tin cậy của công cụ.**

Bài học đắt nhất. Một công cụ transcribe từng tự viết *"Độ tin cậy về phân vai đạt mức rất cao"* trong khi gán sai hoàn toàn danh tính người nói. **Tự đánh giá độ tin cậy là phần đáng nghi nhất trong toàn bộ output.** Kiểm chứng chéo bằng nội dung, không bằng lời tự khẳng định.

### 1.2 Các loại nguồn khác

- **File nhị phân**: kiểm định dạng thực bằng `file <path>` trước khi mở. File đuôi `.pdf`/`.docx` có thể thực chất là zip ảnh hoặc text thuần — mở sai cách sẽ ra rỗng và dẫn tới kết luận "không có dữ liệu" sai lầm.
- **Số liệu tài chính**: đối chiếu "bằng số" với "bằng chữ"; trước-VAT với sau-VAT. Chênh lệch là lỗi thật, phải cờ lên chứ không tự làm tròn.

Khi phát hiện nguồn cũ đã dùng để tạo deliverable là sai: **nói thẳng deliverable đó vô hiệu, đề nghị hủy, và hủy ngay tại chỗ** — kèm liệt kê cụ thể điểm sai lệch.

### 1.3 Kiểm chứng ngày tháng & danh tính qua metadata file và timestamp ẩn

Khi nội dung văn bản tự mâu thuẫn về ngày tháng (VD tiêu đề ghi một ngày, thân bài ghi ngày khác), đừng chỉ hỏi người dùng "chọn bên nào" — trước hết tìm thêm bằng chứng độc lập:

- **Document properties của .docx/.pptx/.xlsx**: `unzip -p file.docx docProps/core.xml` cho ra `dcterms:created`, `dcterms:modified`, `dc:creator`, `cp:lastModifiedBy`. Đây là ngày **file thực sự được soạn** và **ai soạn** — thường khác với ngày sự kiện hay "người thực hiện" ghi tay trong bảng, nhưng là mốc tin cậy để suy luận bên nào hợp lý hơn. Đối chiếu thêm `docProps/app.xml` (Company, Application) nếu cần.
- **Timestamp ẩn trong tên file ảnh tải từ Zalo/Messenger**: tên dạng `<13-chữ-số>_<id>_<id>_<hash>.jpg` — chuỗi số đầu là epoch mili-giây. Giải mã bằng `date -d @<epoch_giây_bỏ_3_số_cuối>` (UTC, cộng 7 giờ ra giờ VN) để suy ra ngày ảnh thực sự được gửi/chụp, kể cả khi EXIF đã mất do nền tảng nén lại ảnh (`exifread` trả `None`).
- **Timestamp overlay trong ảnh/video** (kiểu app "Timemark", "GPS Map Camera"): đọc trực tiếp bằng mắt qua Read tool — đây là bằng chứng hiện trường mạnh, nhưng cần phân biệt ảnh **khảo sát hiện tại** với ảnh **tư liệu giới thiệu công trình đã hoàn thành trước đó** do đối tác/vendor gửi (thường có mốc thời gian xa hơn nhiều so với đợt khảo sát đang làm).

Không dùng các bằng chứng này để **tự quyết định** thay người dùng nếu vẫn còn mơ hồ — trình bày bằng chứng ("file được tạo/chia sẻ ngày X, gần với mốc Y hơn mốc Z") và nêu rõ đây là suy luận có căn cứ chứ chưa phải xác nhận chính thức, trừ khi người dùng chốt.

## 2. Xác định đúng người phát ngôn

**Gán sai phát ngôn = gán sai trách nhiệm.** Nhãn tên do công cụ transcribe gán thường sai và phải luôn được kiểm chứng.

### 2.1 Ba kỹ thuật suy luận từ nội dung

**Bằng chứng ngôi thứ ba** — nếu một người nói nhắc tên X ở ngôi thứ ba thì người đó **không phải** X. Áp dụng cho mọi tên xuất hiện trong lời thoại.

**Cặp hỏi–đáp làm neo** — một cặp như:

> A: *"Hôm nay X cũng mới là buổi đầu tiên ngồi với Ban QLDA đúng không?"*
> B: *"Vâng, buổi đầu tiên."*

xác định chắc chắn cả hai người cùng lúc: B = X, A ≠ X. Tìm những cặp này trước, rồi suy ra phần còn lại.

**Xưng hô cấp bậc** — ai gọi ai là "anh"/"em" cho biết quan hệ trên–dưới. Kết hợp sơ đồ tổ chức để loại trừ.

### 2.2 Ba dấu hiệu nhãn bị gán nhầm

- Một nhãn **vừa hỏi vừa tự trả lời** trong hai lượt liên tiếp
- Một nhãn **tự nhắc tên chính mình ở ngôi thứ ba** ngay đầu lượt thoại
- Nhãn có tên nhưng người đó **được nhắc như người vắng mặt** ở chỗ khác

### 2.3 Quy tắc xử lý

Chỉ gán tên khi có bằng chứng trực tiếp trong âm thanh (tự xưng, hoặc được gọi tên ngay trước/sau). **Không suy đoán theo nội dung, chức vụ, hay phong cách nói** — người nói nhiều nhất không mặc nhiên là người chủ trì.

Khi không chắc: trình bày bằng chứng cho người dùng và **hỏi**, không tự quyết. Nêu rõ mốc thời gian và trích dẫn cụ thể.

Khi hồ sơ có nhiều người trùng tên hoặc một người kiêm nhiệm nhiều chức danh, dùng thêm `chuan-hoa-du-lieu-nhansu`.

### 2.4 Quy trình xác nhận cho người dùng (4 mốc, ~40 giây)

Thay vì bảo "anh kiểm tra lại giúp", đưa 4 mốc cụ thể để nghe:

1. Một **cặp hỏi–đáp** xác định danh tính hai người
2. Một câu có **xưng hô cấp bậc** rõ ràng
3. Một câu **nhắc tên người vắng mặt** ở ngôi thứ ba
4. Một mốc **bất kỳ do người dùng tự chọn** để đối chiếu lời nói

### 2.5 File transcript đã hiệu chỉnh

Khi sửa nhãn người nói, xuất ra file `.md` riêng với:

- Bảng đầu file ghi rõ: nhãn gốc → nhãn đúng → **căn cứ** (mốc thời gian + trích dẫn)
- Toàn bộ lời nói, timestamp, nhãn nghe không rõ giữ nguyên **100%** — chỉ thay nhãn tên
- Mục ghi chú độ tin cậy được giữ lại và **bổ sung** những điểm công cụ bỏ sót

## 3. Tách rời hai giai đoạn — không chuẩn hóa sớm

**Transcribe** = giữ thô tuyệt đối, kể cả từ đệm, câu dở dang, từ lóng, phát âm sai.
**Dựng deliverable** = chuẩn hóa có kiểm chứng.

Chuẩn hóa sớm ở khâu transcribe sẽ xóa mất chính những dấu vết dùng để phát hiện lỗi về sau.

**Không đưa danh sách tên nhân sự vào prompt transcribe.** Nghe có vẻ hữu ích nhưng thực chất là mồi cho model gán tên theo suy đoán. Danh sách tên chỉ dùng để **đối chiếu chính tả sau khi đã có transcript**.

## 4. Đối chiếu chéo và cờ xung đột

Khi có từ 2 nguồn trở lên, luôn đối chiếu chéo và chủ động nêu mâu thuẫn — người dùng thường không biết chúng mâu thuẫn.

| Trục | Ví dụ lỗi thật đã gặp |
|---|---|
| Tiến độ ↔ Hợp đồng | Thi công khởi động **trước** mốc ký HĐ/tạm ứng |
| Tiến độ ↔ Phê duyệt | Bàn giao xong **trước** khi duyệt shop drawing |
| Tiến độ ↔ Biện pháp | Thời lượng tính ngày lịch trong khi thực tế chỉ thi công ban đêm |
| Tiêu đề ↔ Nội dung ↔ BOQ | "Tầng 1;2&5" ≠ "Tầng 1,3,5" ≠ BOQ chỉ có T1+T3 |
| Khối lượng ↔ Giá | Hạng mục chiếm thời lượng lớn nhất nhưng **không có Bill giá** |
| Sheet A ↔ Sheet B | Cùng một mốc xuất hóa đơn ghi hai ngày khác nhau |
| **Đơn vị tính ↔ Đơn vị tính** | "460 nghìn **một mét**" so với ba-rem "250 nghìn **một mét vuông**" — khác đơn vị thì phép so sánh giá đang lệch |
| **Báo cáo khảo sát ↔ Khái toán vendor** | Số phòng/diện tích trong báo cáo khảo sát trực tiếp (VD 2 phòng/446m²) không khớp khái toán do đối tác cung cấp sau đó (VD 3 phòng/592m²) — cả hai đều là "dữ liệu chính chủ" nhưng không đồng nhất, phải nêu cả hai, không tự chọn số "nghe hợp lý hơn" |
| **Tên đối tác/thương hiệu ↔ Đầu mối liên hệ thực tế** | Báo cáo văn bản ghi tên công ty A là đơn vị thi công, nhưng đầu mối trao đổi trực tiếp kỹ thuật/giá lại thuộc công ty B — có thể là 2 đơn vị hợp tác thật (không phải lỗi chính tả), cần xác nhận quan hệ trước khi khẳng định một bên là "sai" |

**Mâu thuẫn trong chính lời nói thì ghi lại cả mâu thuẫn, không tự chọn một bên.** Ví dụ khi số lượng đơn vị thiết kế được nêu ba con số khác nhau (sáu / bốn / năm) trong cùng một mạch trao đổi, biên bản ghi đủ cả ba kèm mốc thời gian, để người dùng chốt lại.

Phân loại theo mức độ (Nghiêm trọng / Cao / Trung bình), luôn kèm **bằng chứng trích dẫn cụ thể** — không nhận định chung chung.

**Khi người quyết định yêu cầu bỏ một cảnh báo mâu thuẫn khỏi một vị trí cụ thể** (để bản trình bày gọn hơn), không xóa sạch nó khỏi toàn bộ hồ sơ — vẫn giữ lại đúng **một** nơi ghi nhận chính thức (mục tổng hợp "Vấn đề bỏ ngỏ / Cần xác nhận" ở cuối văn bản, xem §8). Xóa sạch mọi dấu vết một mâu thuẫn dữ liệu thật, dù được yêu cầu, có rủi ro làm hồ sơ nội bộ mất khả năng truy vết về sau.

## 5. Truy vết từng ý về nguồn

> **Mỗi ý trong deliverable = một mốc thời gian có thật + một người nói xác định.**

**Cấm bịa timestamp.** Lỗi thường gặp và rất khó tự phát hiện: nội dung nằm trong khối `[00:13]` nhưng khi viết lại "ước lượng" ra `[01:20]` cho tự nhiên. Đây là bịa vô thức, tưởng vô hại, nhưng làm hỏng khả năng truy vết của cả văn bản. Bắt bằng script ở Phụ lục B.

**Số liệu giữ đúng cách người nói phát âm.** Họ nói bằng chữ thì ghi bằng chữ. Không tự quy đổi, không tự thêm đơn vị nếu người nói không nêu.

**Khi cần "giữ nguyên ảnh tư liệu" từ tài liệu nguồn** (báo cáo khảo sát có ảnh + caption ghép trong bảng), **không tự tách rời từng ảnh rồi đoán ảnh nào khớp caption nào** — kể cả khi biết thứ tự nhúng ảnh trong file (`v:imagedata`/`a:blip` theo `r:id` tăng dần thường đúng thứ tự đọc, nhưng không tuyệt đối). Rủi ro gán sai ảnh-caption trong văn bản trình cấp trên/đối tác Nhà nước là không chấp nhận được. Giải pháp an toàn tuyệt đối: **render nguyên trang PDF gốc thành ảnh** (`pdftoppm`) rồi **nhúng nguyên trang đó** vào tài liệu mới như một khối tư liệu — vừa đảm bảo đúng 100% cặp ảnh–caption như tác giả gốc trình bày, vừa nhanh hơn nhiều so với tái dựng bảng ảnh từ đầu.

## 6. Bảo toàn từ khóa nghiệp vụ

Một số cách gọi mang **thông tin nghiệp vụ**, không được "chuẩn hóa" cho đẹp:

- `"bạn Thúy"` ≠ `"chị Thúy"` — chữ "bạn" hàm ý đầu mối bên ngoài/đối tác. Giữ nguyên.
- Phân biệt người trùng tên: **Thanh Huyền (COO)** ≠ **Khánh Huyền (BA)**. Gộp nhầm = gán sai phát ngôn và sai trách nhiệm.
- Từ lóng và tiếng Anh phát âm kiểu Việt trong transcript (VD "hân-đờ" = handle, "pen-đinh" = pending, "lai" = line, "lick-đai" = deep dive): giữ nguyên cách phát âm, ghi chú cách hiểu trong ngoặc vuông, không thay thẳng bằng từ tiếng Anh chuẩn.
- Dòng chữ ký cuối văn bản hành chính: chỉ ghi họ tên đầy đủ, **không** thêm "Anh/Chị". Nếu chưa có họ tên đầy đủ đáng tin, để `[Cần bổ sung]` thay vì suy đoán từ tên gọi thân mật hay đuôi email.
- Mã dự án dùng tiền tố nhất quán: `VTB Hà Giang`, `VTB Đông Hà Nội`, `VTB Thái Nguyên`, `VTB Yên Bái`, `VTB CN Thủ Thiêm`, `VTB PGD Tây Nha Trang`.

Khi không chắc một cách gọi là từ khóa hay lỗi chính tả, **hỏi trước khi sửa**.

Lưu ý khi thay tên hàng loạt: những cách gọi trên nằm trong **danh sách cụm bảo vệ** ở `sht-nen-tang-kiem-chung` — bổ sung cụm mới vào đó, không tạo danh sách riêng ở đây.

## 7. Chuẩn hóa từ vựng trạng thái

`Chưa có` → `Đang làm` → `Đã gửi CĐT` → `CĐT đã nhận` → `Đã ký` / `Đã có`

Điểm mấu chốt: **"CĐT đã nhận" không phải "đã ký", và "đã ký" không phải "đã thu tiền".** Khi checklist đạt 100% "CĐT đã nhận", vẫn phải cảnh báo điều kiện kích hoạt thanh toán chưa đủ. Kèm cột ngày cho mỗi lần chuyển trạng thái.

## 8. Tính trung thực của văn bản

Tài liệu client-facing và nội bộ viết bằng **tiếng Việt**. Văn bản hành chính theo đúng thể thức: quốc hiệu, số hiệu, kính gửi, nơi nhận, khối chữ ký.

Với biên bản họp, **bắt buộc** có hai mục:

- **"Vấn đề còn bỏ ngỏ / Chưa thống nhất"**
- **"Các điểm cần xác nhận lại"**

Đây không phải phần thiếu sót — đây là phần có giá trị nhất. Nó cho người đọc biết cuộc họp đã *không* quyết định điều gì, để lần họp sau biết mở đầu từ đâu.

Luôn để trống nếu nguồn không có: ngày/giờ/địa điểm họp, tên thư ký, thời hạn các đầu việc chưa ấn định. Ghi `[Cần bổ sung]` và tô màu cảnh báo, không tự điền.

## 9. Giữ nguyên thể thức & yếu tố hình ảnh gốc khi phục dựng/hợp nhất văn bản hành chính

Khi người dùng yêu cầu tạo lại, hợp nhất, hoặc nâng cấp một văn bản trên cơ sở **file gốc có sẵn thể thức chính thức** của công ty/tổ chức (không phải soạn mới hoàn toàn), mặc định **giữ nguyên toàn bộ thể thức gốc**, không tự ý áp phong cách/thương hiệu riêng — kể cả khi phong cách riêng "đẹp hơn". Việc tự ý đổi thể thức đã từng bị người dùng yêu cầu sửa lại giữa phiên.

Checklist "giữ nguyên template" phải đủ 4 yếu tố, không chỉ phần dễ thấy:

1. **Khối tiêu đề hành chính** — quốc hiệu, tiêu ngữ, tên công ty, đúng bố cục 2 cột như bản gốc (không thay bằng logo/tagline tự chế).
2. **Font, cỡ chữ, màu chữ** — văn bản hành chính thường dùng đen/trắng thuần, không tự thêm màu thương hiệu trừ khi bản gốc có.
3. **Khung bảng & bố cục ảnh** — nếu bản gốc trình bày ảnh trong bảng 2 cột kèm caption, giữ đúng bố cục đó (xem §5 về nhúng nguyên trang thay vì ghép lại).
4. **Watermark/logo nền** — dễ bị bỏ sót nhất vì mờ, không để ý ngay từ đầu. Cách trích xuất đúng bản gốc:
   - Watermark kiểu Word nằm trong `word/header*.xml` dưới dạng `<v:shape>` có thuộc tính `gain`/`blacklevel` (preset "Washout" chuẩn của Word) trỏ tới một ảnh trong `word/media/` qua `word/_rels/header*.xml.rels`.
   - Ảnh watermark thường "mồ côi" — không xuất hiện trong danh sách `r:embed` thông thường của `word/document.xml`, phải tìm riêng qua rels của header.
   - Khi tái tạo (vì công cụ dựng tài liệu mới không hỗ trợ watermark kiểu Word trực tiếp): giảm alpha ảnh gốc rồi overlay lên PDF cuối bằng script (PIL chỉnh opacity + reportlab vẽ canvas + pypdf `merge_page`), **không áng chừng một con số opacity** — luôn dựng thử, render, và **so sánh cạnh-cạnh với trang có watermark gốc** trước khi chốt độ mờ.
   - **Watermark có chọn lọc theo trang**: nếu tài liệu mới trộn cả trang tự soạn (chưa có watermark) lẫn trang nhúng nguyên ảnh/trang gốc (đã có sẵn watermark từ trước), chỉ overlay watermark vào các trang **thuần văn bản, chưa có sẵn** — overlay đồng loạt mọi trang sẽ gây watermark chồng đôi ở các trang ảnh gốc.

## 10. Kiểm tra deliverable trước khi bàn giao

**Đối chiếu ngược bằng script, không bằng mắt** — xem Phụ lục B.

- **Excel**: chạy recalc, yêu cầu `total_errors: 0`. Đọc lại **giá trị đã tính** (không chỉ công thức). Cẩn thận công thức dùng cả cột (`$D:$D`) — nó đếm cả ô tiêu đề và làm lệch tỷ lệ %; luôn giới hạn dải cụ thể (`$D$5:$D$18`).
- **Word/PDF**: convert sang PDF, render ảnh và **xem tận mắt**. Kiểm tra cột bảng có bị cắt chữ tiêu đề không ("STT" hiện thành "ST").

Không tuyên bố "đã xong" khi mới chạy lệnh mà chưa xác minh kết quả. **Khi export PDF báo lỗi kiểu "Please verify input parameters" nhưng lệnh vẫn thoát mà không dừng script — luôn `ls -la` kiểm tra dung lượng/thời gian sửa đổi file đầu ra để chắc chắn nó thực sự mới, không phải file cũ còn sót lại từ lần chạy trước.** Khi nghi ngờ ghi đè, export ra thư mục mới (`--outdir`) rồi copy, tránh xung đột.

### Checklist riêng của tài liệu dự án

Chạy **sau** checklist nền ở `sht-nen-tang-kiem-chung` §5, không thay thế nó.

- [ ] Nguồn đã qua đủ 4 cổng kiểm (§1.1), hoặc đã đối chiếu metadata/timestamp nếu là file gốc (§1.3)
- [ ] Danh tính người nói/người soạn đã được người dùng xác nhận (§2.4)
- [ ] Script B1 chạy ra kết quả rỗng — không có timestamp bịa
- [ ] Số liệu then chốt khớp nguồn (B2), giữ đúng cách người nói phát âm
- [ ] Mọi mâu thuẫn đã ghi vào "Vấn đề bỏ ngỏ", không tự chọn một bên — kể cả khi được yêu cầu ẩn bớt ở một vị trí cụ thể (§4)
- [ ] Từ khóa nghiệp vụ giữ nguyên, không bị "chuẩn hóa cho đẹp" (§6)
- [ ] Từ vựng trạng thái đúng bậc — không nhầm "CĐT đã nhận" với "đã ký" (§7)
- [ ] Nếu phục dựng/hợp nhất văn bản có mẫu gốc: đã đối chiếu đủ 4 yếu tố thể thức — quốc hiệu/tiêu ngữ, font/màu, khung bảng-ảnh, watermark (§9)
- [ ] Đã `ls -la` xác minh file PDF/Excel đầu ra thực sự mới, không phải bản cũ sót lại (§10)

## Phụ lục E — Xử lý sự cố kỹ thuật thường gặp

- **`rm`/ghi đè vào thư mục người dùng báo "Permission denied"** → xem `sht-nen-tang-kiem-chung` §3 (file đang mở ở ứng dụng khác trên máy người dùng; thử lại, dùng `_v2` tạm, rồi đổi lại tên chuẩn).
- **LibreOffice (`soffice --convert-to pdf`) báo lỗi nhưng không dừng script, để lại file cũ** → luôn kiểm tra `ls -la` (dung lượng, thời gian sửa đổi) file đầu ra sau mỗi lần convert; khi nghi ngờ, dùng `--outdir` để xuất vào thư mục riêng tránh xung đột ghi đè.
- **Ảnh tải từ mạng xã hội không còn EXIF** (`exifread` trả `None`) → kiểm tra tên file có chuỗi 13 chữ số ở đầu (epoch mili-giây) trước khi kết luận "không xác định được thời gian chụp".
- **Cần biết ảnh nào được nhúng theo thứ tự nào trong .docx** → `unzip -p file.docx word/document.xml | grep -o 'v:imagedata r:id="rId[0-9]*"'` (hoặc `r:embed=`) cho thứ tự xuất hiện; đối chiếu với `word/_rels/document.xml.rels` để map `rId` → tên file ảnh trong `word/media/`.
- **Cần xác định tác giả/ngày tạo thật của .docx** → `unzip -p file.docx docProps/core.xml`.

---

---

## Tài liệu tra cứu đi kèm

Đọc khi cần, không nạp sẵn:

| File | Nội dung | Khi nào mở |
|---|---|---|
| `references/prompt-transcribe.md` | Prompt transcribe verbatim đầy đủ | Trước khi gửi file ghi âm đi transcribe (bước [1]) |
| `references/scripts-kiem-chung.md` | B1–B6: đối chiếu timestamp, số liệu, quét ký tự rác, render ảnh, trích metadata .docx, giải mã epoch | Bước [5], và ở CỔNG 1 (§1.1) với B3 |
| `references/tu-vung-chuan.md` | Danh sách tên riêng & thuật ngữ đã chốt | Khi chuẩn hóa tên/mã dự án (§6) |
| `scripts/safe_rename.py` | Đổi tên có cụm bảo vệ + dry-run | Khi thay tên hàng loạt — xem `sht-nen-tang-kiem-chung` §2 |

Các script trong `references/scripts-kiem-chung.md` là **bắt buộc chạy**, không phải tùy chọn: B3 ở cổng kiểm nguồn, B1 và B2 trước mọi lần bàn giao.
