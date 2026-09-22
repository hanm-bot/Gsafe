# Rubric "Văn phong người thật" cho văn bản hành chính

> Dùng cho: **QĐ · công văn · biên bản · tờ trình** do AI soạn hoặc bồi.
> Phạm vi rubric này: **giọng + sắc thái**. Thể thức (tiêu đề, Căn cứ, số Điều, nơi nhận, khối ký) do skill nghiệp vụ lo — xem `sht-qd-nhansu-alignment/references/qd-format-mau.md`, không định nghĩa lại ở đây.
> Cách chấm: **người soát** chấm từng tiêu chí ĐẠT / CHƯA. Bảy tiêu chí #1–#7; #3, #7 là **phải đạt** (bắt buộc), còn lại là **nên đạt**.
> Nguồn rút rubric: mẫu thật SHT đã ban hành/dự thảo — `CV-SHT-223`, `CV-SHT-224` (công văn Metro), `SHT-BBVH-01` (biên bản bàn giao Triad), `bien-ban-phien-30-08-2026` (biên bản nội bộ). Chốt bộ mẫu: phiên 22/09/2026.

## Bảy tiêu chí

| # | Tiêu chí | Mức | ĐÚNG (trích mẫu thật) | SAI — "giọng AI" |
|---|---|---|---|---|
| 1 | **Mở bằng bối cảnh + ghi nhận quan hệ**, không vào lệnh khô | nên | "SHT ghi nhận sự hợp tác chặt chẽ của Ingenico trong suốt thời gian qua…" | "Trong bối cảnh chuyển đổi số ngày càng sâu rộng, nhằm nâng cao hiệu quả…" |
| 2 | **Đóng khung yêu cầu bằng lý lẽ nghĩa vụ**, không ra lệnh trần | nên | "…không phải là đòi hỏi đặc quyền, mà là phương tiện kỹ thuật tối thiểu và bắt buộc để SHT thực hiện nghĩa vụ nghiệm thu" | "Yêu cầu cấp quyền truy cập TMS. Đây là điều kiện bắt buộc." |
| 3 | **Câu chủ động, chủ thể rõ** (SHT / Bên Bán / hai Bên) | **phải** | "Bên Bán chịu trách nhiệm hoàn tất thủ tục… để cấp cho Bên Mua…" | "Tài khoản sẽ được cấp và các thủ tục sẽ được hoàn tất." (bị động, giấu chủ thể) |
| 4 | **Số trang trọng viết kèm chữ trong ngoặc**, nhất quán | nên | "hai (02) tài khoản", "mười (10) ngày làm việc", "bảy (07) ngày" | Lúc "2 tài khoản", lúc "mười ngày" — lộn xộn |
| 5 | **Xưng hô & kính ngữ đúng độ theo vai** người ký–người nhận | nên | "Kính gửi… Kính đề nghị Ông Đoàn Duy…" / "Quý Công ty" / "Trân trọng cảm ơn sự hợp tác" | Suồng sã với đối tác, hoặc khúm núm thái quá nội bộ; kính ngữ dán máy móc |
| 6 | **Kết bằng thiện chí + lợi ích chung**, không cụt | nên | "SHT tin tưởng rằng việc thống nhất các nội dung trên sẽ bảo đảm an toàn… cho cả hai Bên…" | "Trân trọng." (cụt, không bối cảnh) |
| 7 | **Trung thực về trạng thái** — nêu thẳng cái bất lợi, không tô hồng | **phải** | "Bản gốc PO 38 đang để ngày 21/07/2026 (đã trôi qua)…"; biên bản Triad: "chưa xảy ra, không được viết như hiện trạng" | "Dự án đang vận hành thông suốt, mọi hạng mục đã hoàn tất" khi chưa kiểm |

## Danh sách từ/cụm "mùi AI" cần tránh

Rút từ đối chiếu mẫu thật ↔ bản nháp giọng máy. Dùng **chỉ khi có nội dung thật đỡ**, không rải trang trí:

`đột phá` · `toàn diện` · `mạnh mẽ` · `vượt trội` · `tối ưu hoá` · `nâng tầm` · `trong bối cảnh … ngày càng` · `nhằm … và …` (cấu trúc đối xứng rỗng) · `giải pháp toàn diện` · `đồng hành` · `song hành` · mở bài kiểu "Kính thưa Quý vị, trong thời đại…".

## Nối với Giám tính AI — luật cứng #1 & #2

Tiêu chí **#7 (trung thực trạng thái)** là điểm giao với chốt cưỡng chế truy vết: mọi phát biểu dạng **"đã ký / đã hoàn tất / đang vận hành / còn hiệu lực"** trong văn bản hành chính phải:
- truy được về một dòng trong **file `.nguon` đi kèm** (xem dưới), **hoặc**
- mang nhãn ⚠️ / dòng `DA-DOI-CHIEU-NGUON` nếu đã đối chiếu ngoài file.

Đây chính là ranh giới hook truy-vết canh khi ghi văn bản hành chính vào `data/workspaces/` (xem `chan-so-lieu-thieu-nguon` / `chan-ket-luan-thieu-nguon`).

## Quy ước file `.nguon` đi kèm — giữ thể thức văn bản, vẫn truy được nguồn

Văn bản chính **giữ nguyên thể thức** (không nhét footnote/ghi chú kỹ thuật phá form). Nguồn chi tiết để ở **file bạn đồng hành** cùng thư mục:

- Tên: `<tên-văn-bản>.nguon.md` (ví dụ `CV-SHT-225_....md` → `CV-SHT-225_....nguon.md`).
- Nội dung: mỗi dòng là một **cặp** `Phát biểu/con số trong văn bản` → `Nguồn sinh ra nó` (số hiệu văn bản, ngày, câu truy vấn CRM, file gốc + toạ độ). Mẫu:

  | Trích trong văn bản | Nguồn truy được |
  |---|---|
  | "PO 38 trị giá 1.200.000.000 VNĐ" | Dự thảo PO 38, bản đính kèm email Ingenico 05/09/2026 |
  | "đã trôi qua ngày 21/07/2026" | Ngày đặt hàng ghi tại đầu PO 38 bản gốc |

- Mục **Căn cứ** trong văn bản chính là hình chiếu rút gọn của file `.nguon` — không mâu thuẫn với nó.
- Số/căn cứ chưa truy được: hoặc chuyển sang diễn đạt định tính, hoặc lùi ngày ban hành để kiểm xong (trùng nguyên tắc `sht-qd-nhansu-alignment` với số liệu thành tích).

## Ranh giới

- Rubric **không** chấm thể thức, không chấm đúng/sai nghiệp vụ — chỉ chấm giọng.
- **Không** dùng để chặn cứng bằng máy: giọng văn là chủ quan, do **người soát** quyết. Hook chỉ canh phần truy vết (#7 + `.nguon`), không canh giọng (chốt phiên 22/09/2026).
