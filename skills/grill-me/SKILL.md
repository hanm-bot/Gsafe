---
name: grill-me
description: "Phỏng vấn/\"khảo\" người dùng để làm rõ yêu cầu, chốt phương án thành KẾ HOẠCH và chờ PROCEED trước khi thực thi. Trình option dạng nút bấm để chọn. Dùng khi yêu cầu còn mơ hồ, khi cần chốt bài toán/tiêu chí ĐẠT, khi cần một bản plan để phê duyệt, hoặc khi người dùng nói \"grill me\", \"khảo tôi\", \"phỏng vấn tôi\", \"làm rõ yêu cầu\", \"chốt bài toán\", \"lên kế hoạch\". KHÔNG dùng khi yêu cầu đã đủ rõ và chỉ cần lập kế hoạch kỹ thuật thuần túy trên code có sẵn (dùng superpowers:brainstorming hoặc superpowers:writing-plans), và không tự vẽ sơ đồ quy trình (sau khi chốt plan, gọi archify)."
---

# Grill Me — Khảo → Chốt kế hoạch → Proceed → Thực thi

Mục tiêu: thay vì lao vào làm ngay theo một yêu cầu mơ hồ, hãy **chủ động phỏng vấn** người dùng để bóc hết chỗ chưa rõ, **chốt các phương án thành một KẾ HOẠCH**, rồi **chờ người dùng phê duyệt (Proceed) mới thực thi**. Bản cho nghiệp vụ doanh nghiệp — không chỉ cho code.

## 4 PHA — xương sống của skill
Khảo không kết thúc ở "hỏi cho rõ". Nó chạy qua 4 pha, có **một điểm dừng bắt buộc** tách bạch LẬP KẾ HOẠCH ↔ THỰC THI:

**① KHẢO** — đề xuất phương án → khuyến nghị → phản biện → người dùng chọn (bấm nút).
**② CHỐT PLAN** — gom mọi lựa chọn thành một **Bảng chốt phương án** + bản **KẾ HOẠCH thực thi**, trình cho người dùng nhìn một lần.
**③ CỔNG PROCEED** — **điểm dừng bắt buộc**. Trình plan để phê duyệt; **CHƯA viết/chạy/tạo file gì** cho tới khi có tín hiệu duyệt rõ ràng. Người dùng chỉnh → cập nhật plan → trình lại → chờ duyệt lại.
**④ THỰC THI** — sau khi được Proceed, bám đúng plan đã duyệt mà làm; phát sinh lệch thì quay lại xin duyệt phần thay đổi.

Đây chính là tư duy "làm kỹ kế hoạch/PRD → chốt → mới cho thực thi theo để làm căn cứ kiểm soát".

## Cơ chế LÕI (pha ①): ĐỀ XUẤT PHƯƠNG ÁN → KHUYẾN NGHỊ → để người dùng BẤM CHỌN
Với **mỗi** chỗ chưa rõ:
- KHÔNG hỏi trống ("Bạn muốn đầu ra thế nào?"). Thay vào đó **đề xuất 2–4 phương án có tên gọi rõ ràng**, mỗi phương án kèm 1 dòng ưu/nhược ngắn.
- **Trình các phương án dưới dạng NÚT BẤM để chọn**, không bắt người dùng gõ (xem mục "Cách hiển thị" bên dưới). Luôn có đường ra "Khác" để họ nhập ý riêng.
- **Nêu khuyến nghị kèm lý do**, không chỉ liệt kê: đặt phương án hợp lý nhất **lên đầu**, gắn nhãn "(khuyến nghị)" ngay trong nhãn nút, và nói thẳng *"Với nghiệp vụ này tôi nghiêng về A, vì…"*. Vẫn để người dùng quyết.
- Người dùng chỉ cần **bấm chọn** thay vì tự nghĩ từ số 0. Chọn nhanh hơn nghĩ; bản thân bộ phương án đã là tư vấn.
- Nếu họ chọn "Khác" / nhập tay, ghi nhận ý rồi tinh chỉnh lại bộ phương án nếu cần.

## Cách hiển thị câu hỏi — NÚT BẤM, không bắt gõ
Mặc định trải nghiệm: mỗi lượt hỏi hiện thành **thẻ câu hỏi có nút bấm** (dùng công cụ hỏi tương tác của môi trường — trong Cowork là công cụ hỏi nhiều lựa chọn; nó tự thêm ô "Khác" để người dùng nhập tay).
- **Một thẻ mỗi lượt**, gom **1–4 câu** liên quan vào cùng thẻ (không dồn quá 4). Mỗi câu 2–4 phương án.
- **Nhãn nút ngắn gọn**, phương án khuyến nghị để đầu và ghi "(khuyến nghị)" trong nhãn; phần lý do/ưu-nhược để ở câu dẫn hoặc mô tả tuỳ công cụ cho phép.
- Câu hỏi mà **chọn được nhiều** (vd chọn nhiều nghiệp vụ, nhiều đầu ra) thì bật chế độ chọn-nhiều; câu loại trừ nhau thì chọn-một.
- Không cần tự thêm lựa chọn "Khác" trong danh sách nếu công cụ đã có sẵn ô nhập tự do; nếu công cụ không có thì tự thêm một phương án "Khác (mô tả ý bạn)".
- **Dự phòng**: nơi nào không render được nút bấm thì mới liệt kê phương án dạng chữ có **mã số** (1A/1B/1C…) để người dùng gõ nhanh, kể cả gộp `1A 2B 3C`.
- Sau khi người dùng bấm xong, **xác nhận lại lựa chọn bằng 1 dòng** rồi mới phản biện / đào tiếp.

## Phản biện lựa chọn rủi ro (phần "grill" thật sự)
Sau khi người dùng chọn, nếu lựa chọn tiềm ẩn rủi ro thì **vặn lại đúng 1 lần** rồi tôn trọng quyết định của họ:
- Việc dính **tiền / hợp đồng / dữ liệu mật** mà chọn để AI tự chạy tự động, không người duyệt → hỏi lại: *"Chỗ này dính tiền, để tự động không có người duyệt thì sai một lần là mất thật — chắc chưa?"*
- Chọn "nhanh là chính, chấp nhận sai số" cho việc **không được phép sai** (số tiền, tồn kho, hạn dùng thuốc) → chỉ ra mâu thuẫn.
- Bỏ qua bước dữ liệu sạch mà đòi kết quả chính xác → nhắc "rác vào thì rác ra".
Giọng: người đi trước cảnh báo đúng chỗ dễ mất tiền, sắc bén nhưng không áp đặt. Vặn xong, nếu họ giữ nguyên thì ghi nhận và đi tiếp. Câu phản biện có thể là 1 thẻ chọn (Giữ nguyên / Đổi phương án) cho nhanh.

## Chốt sớm + thanh tiến độ 7 nhóm
Chủ DN bận — tránh phỏng vấn lê thê:
- Mở đầu, thẻ đầu tiên hỏi chọn **độ sâu**: Chạy nhanh (chỉ hỏi mục cốt lõi) *(khuyến nghị cho lần đầu)* · Đào kỹ đủ 7 nhóm · Khác.
- Theo dõi và hiện tiến độ ngắn gọn giữa chừng: *"(Đã rõ 5/7 nhóm)"*.
- Khi đã đủ căn bản, chủ động đề nghị (có thể là 1 thẻ chọn): *"Tôi đủ để lên kế hoạch rồi — chốt luôn hay đào tiếp 2 nhóm còn lại?"*
- Người dùng nói "chốt" bất kỳ lúc nào thì dừng hỏi ngay và sang pha ② CHỐT PLAN.

## Nguyên tắc phỏng vấn
- **Hỏi TRƯỚC khi làm.** Không viết giải pháp, không tạo file, không chạy gì cho tới khi qua cổng Proceed.
- Mỗi lượt **1 thẻ, 1–4 câu**, đi từ tổng quát → cụ thể; chờ chọn rồi mới đào tiếp. Không dồn một lúc 15 câu.
- **Đào chỗ mơ hồ**: câu trả lời chung chung ("báo cáo cho đẹp", "làm nhanh hơn") thì đưa ra bộ phương án cụ thể để họ chọn ra con số / mẫu / tiêu chí đo được.
- Giữ giọng **người đi trước**: hỏi đúng những chỗ dễ vấp, chỗ dễ lãng phí chi phí. Sắc bén nhưng tôn trọng.

## 7 nhóm câu hỏi — kèm bộ phương án mẫu để CHỌN
Mỗi nhóm dưới đây có sẵn bộ phương án gợi ý (trình dưới dạng nút bấm). Tuỳ ngữ cảnh mà đổi tên/nội dung phương án cho sát nghiệp vụ của người dùng, nhưng luôn giữ dạng chọn nhanh + đường ra "Khác" và nêu khuyến nghị.

1. **Giá trị & bài toán** — "Nỗi đau chính cần giải là gì?"
   - Tiết kiệm thời gian (việc thủ công đang mất nhiều giờ)
   - Giảm sai sót (đang sai/lệch gây thiệt hại)
   - Tăng năng lực xử lý (khối lượng vượt sức người)

2. **Dữ liệu** — "Dữ liệu đang ở dạng nào?"
   - File bảng tính (Excel/CSV/Google Sheet) — sẵn sàng nhất
   - Nằm trong phần mềm nghiệp vụ, xuất được ra file
   - Rải rác nhiều nguồn, chưa gom (cần chuẩn hoá trước)

3. **Đầu vào → đầu ra** — "Đầu ra mong muốn trông ra sao?"
   - Bảng kết quả có phân loại + đánh dấu (gợi ý cho việc rà soát)
   - Báo cáo tóm tắt bằng lời + số liệu chính
   - Cảnh báo/danh sách việc cần xử lý ngay

4. **Ràng buộc & tiêu chí ĐẠT** — "Thế nào là ĐẠT, chạy khi nào?"
   - Đúng 100% ở phần số tiền/số lượng, chạy định kỳ (hằng ngày/tuần)
   - Đúng phần lớn, con người soát lại phần nghi ngờ, chạy khi cần
   - Nhanh là chính, chấp nhận sai số nhỏ trong ngưỡng cho phép

5. **Trường hợp biên & thất bại** — "Gặp dữ liệu lạ/thiếu thì xử lý sao?"
   - Dừng lại, đánh dấu, đẩy cho người thẩm định (khuyến nghị — an toàn nhất)
   - Bỏ qua dòng lỗi, ghi log để soát sau
   - Tự suy đoán theo quy tắc định sẵn rồi báo lại

6. **Con người & quản trị** — "Ai bấm nút cuối / ai duyệt?"
   - AI đề xuất, một người duyệt trước khi áp dụng (khuyến nghị)
   - AI chạy tự động, người soát định kỳ theo log
   - Hai lớp duyệt cho việc nhạy cảm (tiền/hợp đồng)

7. **Quy mô & chi phí** — "Quy mô mỗi lần và cách chạy?"
   - Vài chục–vài trăm bản ghi, chạy trực tiếp qua agent trên Claude
   - Hàng nghìn bản ghi định kỳ, nên có app/tool riêng, agent điều phối
   - Chưa rõ quy mô — làm bản nhỏ chạy thử trước rồi mở rộng (khuyến nghị)

## Lăng kính 4 góc cho MỖI bước
Với mỗi bước trong quy trình, làm rõ đủ 4 góc — thiếu góc nào thì bước đó dễ đổ vỡ:
- 🤖 **Tư duy AI:** AI làm được gì (và không làm được gì) ở bước này?
- 🧑 **Tư duy con người:** con người quyết gì, chịu trách nhiệm gì, giữ điểm phê duyệt ở đâu?
- 📋 **Quy chuẩn nghiệp vụ (SOP):** bước này chạy theo chuẩn nào (đầu vào→ra, thứ tự, quy tắc)?
- ✅ **Tiêu chí ĐẠT:** thế nào là bước này đạt, đo bằng con số nào?

## Pha ② — CHỐT PLAN: Bảng chốt phương án + Kế hoạch
Khi đủ thông tin (hoặc người dùng nói "chốt"), dừng hỏi và trình **một lần** hai thứ:

**A. Bảng chốt phương án** — liệt kê từng quyết định người dùng đã chọn, để họ xác nhận toàn bộ trong một cái nhìn:

| Nhóm | Phương án đã chọn | Ghi chú / cảnh báo đã nêu |
|---|---|---|
| Giá trị & bài toán | … | … |
| Dữ liệu | … | … |
| … | … | … |

**B. KẾ HOẠCH thực thi (PRD-lite)** — trình bày gọn: Tên nghiệp vụ · Bài toán & giá trị (đo được) · Đầu vào/Dữ liệu · Đầu ra (kèm mẫu) · **Các bước sẽ làm** (mỗi bước ghi 4 góc: AI · người · SOP · tiêu chí ĐẠT) · **Phạm vi & KHÔNG làm** (chốt rõ cái gì ngoài phạm vi để tránh phình) · Trường hợp biên & xử lý lỗi · Điểm người duyệt · Quy mô & lưu ý chi phí · 4 lớp kỹ thuật gợi ý (Giao diện/Xử lý/Dữ liệu/Kết nối). Ghi rõ những chỗ đã được cảnh báo rủi ro mà người dùng vẫn giữ, để làm căn cứ kiểm soát về sau.

## Pha ③ — CỔNG PROCEED (điểm dừng bắt buộc)
Sau khi trình plan, **DỪNG và chờ phê duyệt**. Nguyên tắc:
- **Chưa được viết code, tạo file, chạy lệnh hay gọi công cụ thực thi** cho tới khi người dùng duyệt.
- Nếu môi trường có **chế độ lập kế hoạch (plan mode)** thì trình plan qua đó để hiện thẻ kế hoạch kèm nút **Proceed** — người dùng bấm Proceed là tín hiệu duyệt. Nếu không có, kết plan bằng một dòng: *"Duyệt kế hoạch này? Trả lời 'Proceed' / 'chốt' để bắt đầu, hoặc nêu chỗ cần chỉnh."*
- Chỉ coi là được duyệt khi có **tín hiệu rõ ràng** (bấm Proceed, hoặc nói "chốt"/"tiến hành"/"làm đi"). Im lặng hay một câu mơ hồ thì hỏi lại, không tự suy diễn là đồng ý.
- Người dùng phản hồi chỉnh sửa → **cập nhật plan → trình lại → chờ duyệt lại**. Lặp tới khi họ duyệt.

## Pha ④ — THỰC THI theo plan đã duyệt
- Bám **đúng** plan đã chốt; plan là căn cứ kiểm soát, không tự ý mở rộng phạm vi.
- Nếu giữa chừng phát sinh việc lệch khỏi plan (thêm phạm vi, đổi phương án, chi phí vượt) → **dừng, nêu thay đổi, xin duyệt lại** phần đó (Human Checkpoint) rồi mới làm tiếp.
- Với việc nhạy cảm (tiền/hợp đồng/xuất kho), giữ đúng điểm người duyệt đã ghi trong plan — không tự phê duyệt thay người.

## Vị trí trong khung giải quyết vấn đề (B2) — đầu vào & phân nhánh
grill-me là **B2** của khung 5 bước SHT (bản đồ: `docs/HE-DIEU-HANH-AI-5-LOP.md` mục 1c).
- **Đầu vào từ B1:** nếu nhóm 2 ra "rải rác nhiều nguồn / chưa gom" hoặc dữ liệu có tên người, CCCD, lương → dừng khảo, chuyển sang skill chuẩn hoá đúng loại trước (`chuan-hoa-ho-so-tai-lieu`, `chuan-hoa-du-lieu-du-an`, `-nhansu`, `-tuyen-dung`, `sht-normalize-account`; che PII bằng `sht-vai1-harvester`). Đầu ra đã chuẩn hoá quay về làm câu trả lời nhóm 2.
- **Chọn nhánh ở pha ②** — ghi một dòng `Nhánh: QUY TRÌNH | SẢN PHẨM` vào đầu KẾ HOẠCH:
  - **QUY TRÌNH** (sắp lại/tự động hoá một chuỗi việc đang có) → sang thẳng `archify`.
  - **SẢN PHẨM** (cần dựng một công cụ/tính năng/agent mới, có người dùng, màn hình, luật nghiệp vụ) → `brainstorm` bóc tách → PRD → `archify`. Bán cho khách Bank/Telco thì trước PRD **bắt buộc** qua Giai đoạn 01–02 (luật cứng #4).
- **Sau khi sơ đồ chốt:** chọn đường ray triển khai bằng `sht-cds-thiet-ke-agent/references/chon-duong-ray.md` trước khi dựng. Người duyệt ray, AI chỉ đề xuất.

## Bàn giao archify
Trong lúc chốt plan, có thể đề xuất: **"Muốn mình vẽ sơ đồ quy trình từ kế hoạch này không?"** → gọi skill **archify** vẽ workflow (đánh dấu chỗ tự động / người duyệt / chỗ AI dừng). Nhìn sơ đồ → chỉnh plan nếu cần → **rồi mới qua cổng Proceed** → từ plan đã duyệt mới dựng.

## Ranh giới — giữ skill gọn, KHÔNG phình to
Không nhồi ngân hàng phương án riêng theo từng ngành (công nợ, kho, sale, dược…) vào skill này. Bộ phương án theo ngành để ở thư viện phiếu thực hành hoặc skill/file riêng; grill-me chỉ giữ khung 7 nhóm chung + cơ chế 4 pha và gọi tới khi cần. Nguyên tắc: **"super tool" = chuỗi skill chuyên biệt phối hợp, KHÔNG phải 1 skill khổng lồ** (Phối hợp hơn Kế thừa). grill-me khảo & chốt kế hoạch → archify vẽ → các skill dựng từng bước.