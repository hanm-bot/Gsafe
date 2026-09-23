# Phân vai đường ống xuất bản — phiếu việc từng người

> Năm vai khớp năm lớp của đường ống tại `SKILL.md` §9. Mỗi vai một phiếu riêng bên dưới:
> đầu vào, việc phải làm, lệnh chạy, tiêu chí ĐẠT, giao cho ai.
>
> **Đây là bảng phân công, không phải nơi định nghĩa luật.** Mọi quy tắc đều thuộc một skill
> chủ sở hữu — phiếu chỉ trỏ tới. Sửa luật thì sửa ở skill chủ, không sửa ở đây.
>
> Rút từ phiên làm việc thật ngày 23/09/2026 (hồ sơ VTCPay: một phụ lục hợp đồng và một
> BRD). Mọi "cạm bẫy" bên dưới đều là lỗi đã xảy ra thật trong phiên đó, không phải phòng xa.

| Vai | Lớp | Câu hỏi vai đó trả lời |
|---|---|---|
| A — Chuẩn bị hồ sơ | trước L1 | Bản nào là bản có hiệu lực? |
| B — Rà pháp lý | L1 | Văn bản này có tựa vào thứ gì chưa chắc chắn không? |
| C — Soạn thảo | L2–L3 | Câu chữ có ra giọng người không? |
| D — Kiểm xuất bản | L4 | File in ra có vỡ không? |
| E — Trình duyệt & phát hành | L5 | Đủ điều kiện trình chưa, ai ký, ghi sổ chưa? |

---

## Vai A — Chuẩn bị hồ sơ

**Đầu vào:** thư mục dự án, thường lẫn nhiều bản dự thảo tên gần giống nhau.
**Đầu ra:** đúng **một** bản có hiệu lực ở thư mục chính; các bản còn lại nằm trong `_archive/`.

**Việc phải làm**

1. Liệt kê mọi file cùng tên gốc, kể cả trong thư mục con (`Claude outputs/`, `draft/`…).
2. **So nội dung, không so giờ sửa file.** Trích text từng bản rồi `diff`.
3. Chọn bản hiệu lực. Nếu không bản nào trội hoàn toàn thì ghép, và ghi rõ lấy phần nào từ bản nào.
4. `mv` các bản còn lại vào `_archive/<ngày>_<việc>/`, đổi tên theo **vai trò** chứ không theo số thứ tự.
5. Viết `00_LY-DO-GOM.md` trong thư mục archive: bảng từng bản, vì sao không dùng.

**Cạm bẫy đã gặp thật**

- **Bản mới nhất có thể là bản thoái lui.** Bản sửa sau cùng bị mất tên pháp nhân hai Bên và
  dòng "(Ký, ghi rõ họ tên, đóng dấu)" trong khối chữ ký — thứ bắt buộc phải có khi đem đi ký.
  Bản cũ hơn 9 phút lại đầy đủ. Nếu chọn theo giờ sửa file thì đã bàn giao bản hỏng.
- **Phần bị xoá quan trọng hơn phần được thêm.** Khi đọc diff, liệt kê phần mất trước.
- **Đổi tên file trong archive theo vai trò** (`C_22-53_khoi-chu-ky-duoc-giu.docx`) — sáu tháng
  sau không ai nhớ `bản 2` là bản nào.

**Tiêu chí ĐẠT:** `ls` thư mục chính chỉ ra một file cho mỗi tài liệu · `_archive/` có file lý do ·
không file nào bị xoá.

**Luật ở đâu:** `sht-nen-tang-kiem-chung` §3 (một tài liệu — một bản có hiệu lực).
**Giao cho:** Vai B.

---

## Vai B — Rà pháp lý

**Đầu vào:** bản có hiệu lực từ Vai A.
**Đầu ra:** kết luận văn bản có tựa vào thứ gì chưa chắc chắn không, kèm toạ độ cụ thể.

**Việc phải làm**

1. **Lập bảng tình trạng ký cho mọi văn kiện liên quan** trước khi phân tích bất kỳ điều khoản nào.
2. Với mỗi văn kiện: **nhìn khối chữ ký**. Bản scan thì render trang ký ra ảnh rồi đọc bằng mắt.
   Với `.docx`, kiểm nhanh bằng máy: gói không có ảnh nhúng nào thì không thể chứa chữ ký tay
   hay con dấu scan.
3. Dựng **đồng hồ hiệu lực**: mọi mốc hạn trong hồ sơ, cột cuối là "so với hôm nay".
4. Kiểm **dẫn chiếu chéo**: mỗi chỗ văn bản A trỏ sang văn bản B, mở B ra xem thứ được trỏ có
   tồn tại không.

**Cạm bẫy đã gặp thật**

- **Số hiệu giống nhau nhưng thuộc hợp đồng khác.** Một file tên rất giống thứ đang tìm, có dấu
  đỏ thật, hoá ra là phụ lục của một hợp đồng hoàn toàn khác với đối tác khác. Suýt dùng làm
  bằng chứng tình trạng ký. Luôn mở ra xem hợp đồng gốc mà nó kèm theo.
- **Ô ngày để trống không đồng nghĩa chưa ký**, và ngược lại tên đánh máy trong khối chữ ký
  không đồng nghĩa đã ký.
- **Dẫn chiếu treo.** Một phụ lục trỏ "tiêu chí quy định tại BRD" trong khi BRD không có mục tiêu
  chí nào. Chỉ phát hiện được bằng cách mở BRD ra tìm, không phát hiện được bằng đọc phụ lục.
- **Mốc đã trôi qua là cảnh báo đỏ, nêu trước mọi nội dung khác** — không phải việc hành chính.
- **"Không tìm thấy" chỉ có giá trị khi đã tìm toàn diện.** Rà theo nhiều mẫu tên, nhiều thư mục,
  và quét cả text trong PDF trước khi kết luận một văn kiện không tồn tại.

**Chốt cưỡng chế:** hook `chan-can-cu-khong-nguon.cjs` chặn ghi Quyết định có mục Căn cứ mà
thiếu file `<tên>.nguon.md` đi kèm. Đường thoát: tạo file nguồn, hoặc gắn nhãn "chưa đối chiếu"/⚠️,
hoặc ghi dòng `DA-DOI-CHIEU-NGUON`.

**Tiêu chí ĐẠT:** mỗi phát biểu về trạng thái nghĩa vụ đều có nguồn kèm toạ độ · mọi dẫn chiếu
đã mở ra kiểm · đồng hồ hiệu lực đã dựng.

**Luật ở đâu:** `ra-soat-hop-dong-vendor` §0.2b (tình trạng ký), §0.3 (đồng hồ hiệu lực),
§1.4 (dẫn chiếu). **Giao cho:** Vai C.

---

## Vai C — Soạn thảo

**Đầu vào:** nội dung nghiệp vụ đã chốt + kết quả rà của Vai B.
**Đầu ra:** bản `.md` hoặc `.docx` đã tự chấm giọng.

**Việc phải làm**

```bash
python cham_van_phong.py VANBAN.md
```

Đọc phiếu, sửa những chỗ mình thấy đúng, giữ lại những chỗ mình thấy máy bắt sai — **và ghi lại
vì sao giữ**, để Vai E khỏi hỏi lại.

**Cạm bẫy đã gặp thật**

- **Máy không kết luận thay người.** Từ trong danh sách "mùi AI" chỉ sai khi rải trang trí. Một
  công văn thật dùng chữ "toàn diện" kèm dẫn đúng số điều khoản là dùng đúng.
- **Tiếng Việt nêu chủ thể bằng `được + <ai>`**, không bằng "bởi". "đang được hai Bên thương thảo"
  là câu có chủ thể rõ, không phải câu bị động giấu chủ thể.
- **Rubric chỉ áp cho QĐ · công văn · biên bản · tờ trình.** Tài liệu kỹ thuật (BRD, đặc tả) nằm
  ngoài phạm vi — chấm thì được, nhưng kết quả chỉ để tham khảo.
- Máy **không** chấm được tiêu chí #2 (lý lẽ nghĩa vụ), #5 (xưng hô theo vai), #7 (trung thực
  trạng thái). Ba tiêu chí này người viết tự soi.

**Tiêu chí ĐẠT:** phiếu văn phong không còn lỗi tiêu chí #3 chưa giải thích · người viết đã đọc
lại ba tiêu chí máy không chấm được.

**Luật ở đâu:** `sht-nen-tang-kiem-chung/references/rubric-van-phong-nguoi.md` (7 tiêu chí +
danh sách từ). **Giao cho:** Vai D.

---

## Vai D — Kiểm xuất bản

**Đầu vào:** bản `.docx` từ Vai C.
**Đầu ra:** PDF sạch, đã nhìn tận mắt.

**Việc phải làm**

```bash
python kiem_xuat_ban_docx.py VANBAN.docx      # exit 2 = còn lỗi nặng, chưa xuất
```

Xuất PDF bằng Word COM `SaveAs2(FileFormat=17)` — **không dùng `docx2pdf`**. Sau đó **render
trang quan trọng ra ảnh và nhìn**: trang chữ ký, trang có bảng.

**Cạm bẫy đã gặp thật**

- **Trích text không thấy lỗi trình bày.** Ba lỗi trong phiên chỉ lộ ra khi nhìn ảnh render: cột
  bảng chia đều làm cột rộng thừa còn cột hẹp bị bóp; bảng trải hai trang mà không lặp hàng tiêu
  đề; hàng bị cắt ngang giữa hai trang. Máy báo "đạt" ở cả ba.
- **`SaveAs2` trượt khi file PDF đích đang mở.** Xuất ra tên tạm rồi `Move-Item` đè vào.
- **Script Python in tiếng Việt ra stdout trên Windows sẽ vỡ `UnicodeEncodeError`** — và vỡ *sau
  khi* file đã ghi xong, khiến script trông như thất bại dù đã chạy đúng. Luôn
  `sys.stdout.reconfigure(encoding='utf-8')` đầu chương trình.
- Bảng dài thì bật lặp hàng tiêu đề (`w:tblHeader`) và chống cắt hàng (`w:cantSplit`).

**Tiêu chí ĐẠT:** `kiem_xuat_ban_docx.py` exit 0 · PDF không trang trống · đã render và nhìn
trang chữ ký cùng mọi trang có bảng.

**Luật ở đâu:** `sht-nen-tang-kiem-chung` §6.1 (kết xuất, dò trang trống), §9 (đường ống).
**Giao cho:** Vai E.

---

## Vai E — Trình duyệt & phát hành

**Đầu vào:** `.docx` + `.pdf` đã qua Vai D.
**Đầu ra:** phiếu trình duyệt, quyết định của người duyệt, bản ghi Sổ Cái, rồi mới phát hành.

**Việc phải làm**

```bash
python phieu_xuat_ban.py VANBAN.md --docx VANBAN.docx --ra-ngoai
```

Trình phiếu cho người duyệt đúng cổng: văn bản ra ngoài là **Gate 3**. Sau khi duyệt mới ghi Sổ Cái:

```bash
python .agents/scripts/ghi-log-hitl.py --append --gate "Gate 3" \
  --channel "Claude Code CLI" --actor "<người duyệt>" \
  --target "<tên tài liệu>" --command "<câu duyệt nguyên văn>"
```

**Cạm bẫy đã gặp thật**

- **Phiếu không tự phê duyệt và máy không thẩm được nghiệp vụ.** Phiếu ✅ chỉ nghĩa là phần đo
  được bằng máy đã sạch. Thể thức, đúng/sai nghiệp vụ, và chuyện văn bản có tô hồng trạng thái
  hay không đều do người đọc.
- **Kiểm tài liệu phụ thuộc trước khi gửi.** Một phụ lục dẫn chiếu tới mục chỉ có ở bản BRD mới;
  gửi phụ lục một mình thì đối tác ký một điều khoản trỏ vào tài liệu họ chưa nhận. Tài liệu phụ
  thuộc nhau thì gửi cùng nhau.
- **Người ký không chắc là người đang trao đổi thư.** Phụ lục ghi người ký là một Phó Tổng Giám
  đốc theo giấy uỷ quyền, trong khi mọi luồng thư đều đi qua đầu mối kỹ thuật. Xác định kênh tới
  đúng người ký trước khi gửi.
- **Gửi ra ngoài là không rút lại được.** Người soạn không tự bấm gửi cho đối tác.

**Tiêu chí ĐẠT:** `phieu_xuat_ban.py` exit 0 · người duyệt đúng cổng đã quyết · Sổ Cái có bản ghi ·
mọi tài liệu phụ thuộc đã sẵn sàng đi cùng.

**Luật ở đâu:** `sht-vai5-critic` (thẩm tra 3 tầng, tờ trình HITL), `sht-quan-tri-dn` §2 (ba cổng,
Sổ Cái SHA-256), `sht-nen-tang-kiem-chung` §5 (checklist bàn giao).

---

## Một người kiêm nhiều vai

Đội nhỏ thì gộp A+B (chuẩn bị & rà hồ sơ), C+D (soạn & kiểm), giữ **E tách riêng**. Lý do giữ E
tách: vai duyệt mất giá trị khi chính người soạn tự duyệt bản của mình — đó là điểm kiểm độc lập
duy nhất trong cả đường ống.
