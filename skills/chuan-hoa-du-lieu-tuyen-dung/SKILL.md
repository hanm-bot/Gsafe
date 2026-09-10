---
name: "chuan-hoa-du-lieu-tuyen-dung"
description: "Săn CV, chấm điểm ứng viên, và soạn JD mới kèm khảo sát lương thị trường cho SHT — tìm & lọc trên cổng tuyển dụng (TopCV/VietnamWorks/LinkedIn) với bộ lọc đã test bằng số liệu, đọc chi tiết CV, chấm theo mô hình ASK (nhân viên/ứng viên thường: Attitude 30%/Skills 40%/Knowledge 30%; cán bộ quản lý: A60/S30/K10) có bằng chứng trích dẫn, đối chiếu lương kỳ vọng với khung 3P hoặc benchmark thị trường mới dựng, và xuất song song infographic PDF + Excel scorecard theo chuẩn màu/font SHT. Dùng khi người dùng yêu cầu \"săn CV\", \"hunt CV\", \"tìm ứng viên\", \"lọc hồ sơ\", \"chấm điểm ứng viên\", \"lập scorecard tuyển dụng\", \"so ứng viên\", \"soạn JD\", \"khảo sát lương\", hoặc thao tác trên cổng tuyển dụng — kể cả khi chỉ gõ vỏn vẹn \"hunt CV\" hay \"viết JD cho anh\" mà không nêu chi tiết. KHÔNG dùng cho hồ sơ nhân sự đã tuyển (việc của chuan-hoa-du-lieu-nhansu). Luôn dùng KÈM sht-nen-tang-kiem-chung cho quy tắc bàn giao chung."
---

# Chuẩn hóa dữ liệu tuyển dụng (SHT)

Quy trình săn CV, chấm điểm và xếp hạng ứng viên: từ tìm kiếm thô trên cổng tuyển dụng đến scorecard + infographic sẵn sàng trình hội đồng.

Nguyên tắc bao trùm: **một yêu cầu tuyển dụng thật thường đến dưới dạng một câu ngắn cụt ("Hunt CV"), còn kết quả phải trình được lên hội đồng.** Khoảng cách đó chỉ lấp được bằng cách hỏi đúng thứ tự, lọc đúng nguồn, và không bao giờ chấm điểm ứng viên bằng thứ không phải bằng chứng.

Quy tắc bàn giao chung (lan truyền hiệu chỉnh, một-bản-có-hiệu-lực, checklist nền) nằm ở `sht-nen-tang-kiem-chung` — skill này chỉ giữ phần đặc thù tuyển dụng.

---

## LUỒNG CHUẨN: YÊU CẦU CỘC LỐC → SCORECARD TRÌNH HỘI ĐỒNG

```
[1] Làm rõ yêu cầu — tối đa 2 vòng hỏi (§1)
     ↓
[2] Kiểm tra dữ liệu đã có (folder JD/CV nội bộ) trước khi ra ngoài tìm (§2)
     ↓
     [2b] Nếu CHƯA có JD → nghiên cứu nội bộ + khảo sát lương thị trường, soạn JD trước (§2b)
     ↓
[3] Tìm & lọc trên cổng tuyển dụng — lọc theo vòng, test ngữ nghĩa bộ lọc bằng số liệu (§3)
     ↓
[4] Đọc chi tiết CV — biết trước đây là vùng dễ vỡ (§4)
     ↓
[5] Chấm điểm ASK có bằng chứng + đối chiếu ngân sách JD (§5, §6)
     ↓
[6] Xuất Excel scorecard (công thức thật) + PDF chuẩn SHT — 1 trang khi sàng lọc,
     2 trang khi đánh giá vòng cuối (§7)
     ↓
[7] Bàn giao — tóm tắt cực ngắn, không liệt kê lại mọi thứ (§8, §9, §10)
```

Không nhảy cóc bước 1 và bước 2 — phần lớn thời gian lãng phí trong tuyển dụng đến từ việc lọc sai đối tượng hoặc tìm lại thứ đã có sẵn trong folder.

---

## 1. Làm rõ yêu cầu trước khi bắt đầu

Yêu cầu "hunt CV" / "tìm ứng viên" gần như luôn thiếu ít nhất 2 trong 3 thứ: **vị trí cụ thể**, **nguồn dữ liệu** (đã có CV sẵn hay cần tìm mới), **định dạng đầu ra** mong muốn. Dùng công cụ hỏi lựa chọn (không hỏi bằng câu hỏi mở) để chốt nhanh, nhưng gộp câu hỏi thay vì tách rời — hai câu hỏi tách rời mô tả cùng một ý định mơ hồ dễ ra câu trả lời tự mâu thuẫn (VD: người dùng chọn "đã có CV sẵn" ở câu 1 nhưng "tìm trên web" ở câu 2, vì thực ra họ muốn cả hai). Luôn có lựa chọn "cả hai" khi hai phương án không loại trừ lẫn nhau.

**Nếu người dùng bỏ qua widget hỏi lựa chọn hai lần liên tiếp, chuyển hẳn sang hỏi bằng văn bản có cấu trúc** — danh sách đánh số trong tin nhắn, để họ trả lời gọn theo số thứ tự. Việc bị bỏ qua form **không** có nghĩa là họ không muốn được hỏi; ca thật: sau hai lần bỏ qua widget, chính người dùng chủ động nhắn "tôi cần verify lại yêu cầu với bạn trước khi triển khai để khỏi mất thời gian". Họ coi trọng việc chốt yêu cầu, chỉ là muốn trao đổi bằng cách khác.

Thứ tự ưu tiên hỏi: **vị trí cụ thể trước tiên** (mọi bước sau đều phụ thuộc vào việc biết JD nào), rồi mới đến nguồn dữ liệu.

## 2. Kiểm tra dữ liệu nội bộ trước khi ra ngoài tìm

Trước khi mở trình duyệt, quét folder chia sẻ của công ty tìm:

- File JD của đúng vị trí (để lấy yêu cầu kinh nghiệm, mô tả công việc, và **khung lương 3P** — dùng ở §6).
- CV đã có sẵn cho vị trí đó (đặt tên file có thể không rõ ràng — quét toàn bộ danh sách file, không chỉ tìm theo từ khóa tên vị trí).

Nếu không có JD, hỏi người dùng trước khi tự suy đoán yêu cầu công việc — chấm điểm ứng viên mà không có JD làm chuẩn là chấm điểm theo cảm tính.

## 2b. Khi CHƯA có JD — soạn JD mới kèm khảo sát lương thị trường

Xảy ra rõ nhất với vị trí mới/C-level (CFO, CCO...) chưa có sẵn JD hay bậc lương 3P. Trước khi viết một dòng JD nào:

1. **Đọc dữ liệu công ty thật trước khi viết** — hồ sơ năng lực công ty (quy mô, doanh thu, khách hàng tiêu biểu, sơ đồ tổ chức), Quy chế lương 3P hiện hành, và Khung năng lực & Đánh giá Cán bộ quản lý (nếu vị trí là cấp quản lý) trong folder chia sẻ. JD không được viết từ suy đoán chung chung khi công ty đã có sẵn dữ liệu thật.
2. **Khảo sát lương thị trường bằng 2 lớp, không chỉ 1**: (a) tìm 3–4 nguồn khảo sát lương bên ngoài (career site, salary guide của headhunter, salary survey...) phân theo quy mô doanh nghiệp; (b) đối chiếu với dữ liệu ứng viên **thực tế đã tự ứng tuyển vào chính công ty** cho vị trí liền kề thấp hơn một cấp (VD: muốn định lương CFO thì soi mức lương kỳ vọng công khai của các ứng viên Kế toán trưởng đã nộp CV vào công ty) — đây là pool tự chọn lọc (self-selected), sát với khả năng thu hút thực tế của công ty hơn số liệu thị trường chung chung. Định vị vị trí cần tuyển ở trên trần của nhóm liền kề thấp hơn.
3. **Không có bậc 3P sẵn cho vị trí này thì không suy diễn từ khung chung** — trình bày rõ là "đề xuất — cần phê duyệt", không viết như số đã chốt.
4. **Nếu vị trí thuộc cấp quản lý (Trưởng phòng/Giám đốc bộ phận trở lên), kiểm tra khung ASK áp dụng đúng phiên bản** — xem §5 về khác biệt A30/S40/K30 (thực thi/ứng viên thường) và A60/S30/K10 (cán bộ quản lý); dùng nhầm khung sẽ khiến JD lẫn scorecard sau này chấm sai trọng số.
5. Tích hợp khung năng lực thẳng vào JD (không tách file riêng) — một JD dùng được cho cả đăng tuyển lẫn làm căn cứ đánh giá định kỳ sau này.

## 3. Tìm & lọc trên cổng tuyển dụng — lọc theo vòng

**Nếu người dùng đã có tài khoản nhà tuyển dụng** (TopCV Employer, VietnamWorks Employer...) và cho địa chỉ link trực tiếp vào chiến dịch/portal đã đăng nhập, dùng luôn — không tự ý tạo tìm kiếm mới hay đăng nhập tài khoản khác.

**Chiến lược lọc — mở rộng phạm vi phải đi kèm đổi cách sắp xếp:**

1. Vòng đầu: từ khóa vị trí trong phạm vi hẹp (VD chỉ trong "vị trí ứng tuyển") → thường ra kết quả ít nhưng nhiều nhiễu (trùng từ khóa nhưng sai chuyên môn).
2. Mở rộng phạm vi tìm (thêm "Kinh nghiệm" + "Kỹ năng" vào phạm vi quét), thêm **từ khóa bắt buộc** đặc trưng của công việc (VD "dự toán" cho vị trí QS), thêm mọi địa điểm JD cần.
3. **Bắt buộc đổi cách sắp xếp từ "mới nhất" sang "phù hợp nhất"/"liên quan nhất"** nếu cổng có tùy chọn đó. Chỉ mở rộng phạm vi mà không đổi cách sắp xếp sẽ cho ra nhiều kết quả hơn nhưng không *đúng* hơn — đầu danh sách vẫn có thể toàn nhiễu.
4. Đọc dữ liệu tóm tắt ở trang danh sách (title, công ty, số năm kinh nghiệm, học vấn, mục tiêu nghề nghiệp) bằng công cụ trích xuất văn bản — trang danh sách thường đọc được, không cần chụp ảnh.

**Đừng đoán ngữ nghĩa AND/OR của trường lọc — test bằng số liệu.** Các cổng tuyển dụng không luôn công bố rõ trường "bắt buộc có từ khóa" xử lý nhiều chip theo AND hay OR. Cách xác định nhanh: thêm 2–3 từ khóa cùng lúc vào trường đó, chạy tìm kiếm, và quan sát số kết quả — nếu tụt sâu bất thường (VD 58 → 8), đó là AND (CV phải chứa TẤT CẢ các từ); nếu chỉ giảm nhẹ, đó là OR. Đừng đưa từ khóa vào bộ lọc rồi tin ngay vào số lượng kết quả trả về mà không hiểu cơ chế lọc đứng sau.

**Nới một điều kiện phải kiểm tra nó có dùng chung ô với điều kiện khác không.** Khi người dùng yêu cầu đổi "A **và** B" thành "A **hoặc** B", phản xạ tự nhiên là đẩy cả hai xuống ô "có một trong các từ khóa" — nhưng ô đó thường **đang giữ bộ từ khóa domain**, ghi đè vào đó sẽ xóa sạch bộ lọc chuyên môn và làm kết quả nở ra hàng nghìn hồ sơ nhiễu. Cách đúng: **chạy nhiều lượt tìm kiếm riêng**, mỗi lượt một từ khóa bắt buộc, giữ nguyên ô OR, rồi gộp kết quả và loại trùng. Ca thật: yêu cầu "Business Analyst hoặc Product Owner" → chạy 2 lượt cho ra 754 và 353 hồ sơ mà vẫn giữ đủ 6 từ khóa payment; nếu gộp vào ô OR thì mất hoàn toàn bộ lọc thanh toán.

**Tránh viết tắt trong từ khóa bắt buộc.** Từ khóa ngắn 2-3 ký tự (VD "PO", "BA") khớp chuỗi con vào rất nhiều từ không liên quan (Position, Portfolio, PO Box, Bachelor, Mobile Developer...) — gần như không lọc được gì dù trông có vẻ đúng chuyên môn (thực tế: 98 → 93, vô dụng; đổi sang cụm đầy đủ ra 98 → 70, sạch). Luôn dùng cụm từ đầy đủ ("Product Owner", "Business Analyst") cho trường bắt buộc, dù kết quả ít hơn — ít mà trúng đích tốt hơn nhiều mà toàn nhiễu.

**Sau mỗi lần chọn từ dropdown, đọc lại chip vừa tạo để xác nhận.** Danh sách gợi ý của cổng tuyển dụng dịch chuyển sau khi gõ, rất dễ click trúng mục liền kề. Ca thật: gõ "Hồ Chí Minh" nhưng chọn trúng "Quận 1 - Hồ Chí Minh (Cũ)" thay vì "TP Hồ Chí Minh" — thu hẹp phạm vi tìm mà không hay biết.


> **Chi tiết thao tác LinkedIn** (xác nhận loại tài khoản, từ khóa cụm trong ngoặc kép, danh sách bị virtualized): `references/thao-tac-cong-tuyen-dung.md` §1.1.
>
> **Khi ô lọc ngừng nhận ký tự, hoặc cần quét nhanh nhiều trang kết quả**: `references/thao-tac-cong-tuyen-dung.md` §5–§6.

## 4. Đọc chi tiết CV — vùng dễ vỡ, biết trước để không lặp lỗi

> **Trước khi mở trang chi tiết đầu tiên, đọc `references/thao-tac-cong-tuyen-dung.md`** — cách mở trang bị iframe, bẫy trang tin tuyển dụng TopCV, cuộn/chụp, thông tin bị che, và toàn bộ cách xử lý lỗi công cụ. Không đọc trước thì sẽ lặp lại đúng những lỗi đã trả giá.

**Đừng loại một ứng viên chỉ dựa vào dữ liệu tóm tắt trang danh sách.** Tiêu chí phụ như địa điểm, tuổi hồ sơ có thể sai lệch so với thực tế trong CV chi tiết — ca thật: một ứng viên bị loại vì "địa chỉ Hồ Chí Minh" trên danh sách, nhưng CV chi tiết ghi rõ đang chuyển ra Hà Nội. Trước khi loại hẳn một hồ sơ có domain/kinh nghiệm mạnh chỉ vì 1 tiêu chí phụ, mở chi tiết xác nhận lại — đặc biệt khi người dùng chủ động hỏi lại về một ứng viên đã bị loại.

**Phân biệt lỗi cục bộ và lỗi hệ thống bằng cách test trên ≥2 đối tượng khác nhau, không chỉ retry trên cùng một tab.** Khi "Cannot attach to this target" lặp lại sau 2 lần đóng/mở tab như quy tắc trên, đừng dừng lại ở kết luận "tab này hỏng" — mở thử một hồ sơ/CV **khác** bằng đúng thao tác đó. Nếu lỗi giống hệt trên đối tượng thứ hai, đây là lỗi hệ thống của phiên trình duyệt (không phải lỗi riêng một hồ sơ) → dừng toàn bộ nhánh thao tác đó ngay, báo cáo minh bạch, không lãng phí retry từng người còn lại trong danh sách.

**Đối chiếu headline PR với phần Kinh nghiệm chi tiết trước khi xếp hạng cao — đừng chấm điểm chỉ vì tiêu đề kêu.** Ca thật: một hồ sơ ghi headline "Digital Transformation in Fintech & Banking" nhưng nội dung Kinh nghiệm thực tế lại là BA ERP/CRM chung chung, không có bằng chứng ngân hàng/fintech cụ thể nào. Luôn mở phần kinh nghiệm để xác nhận headline có bằng chứng đi kèm hay chỉ là câu PR, áp dụng cho mọi cổng tìm kiếm chứ không riêng LinkedIn.

**Nếu người dùng chặn một hành động giữa chừng** (ví dụ báo họ đang thao tác tay trên chính trình duyệt đó), dừng ngay mọi thao tác, báo lại, và chỉ tiếp tục khi được yêu cầu rõ ràng. Không thử lại âm thầm hành động vừa bị chặn.

### 4.1 Hai phép quét bắt buộc trước khi gửi lời mời

**Quét tên công ty mình trong toàn bộ pool.** Trước khi gửi lời mời cho bất kỳ ai, tìm mọi biến thể tên công ty (VD "SHT", "đầu tư công nghệ SHT", "SHT INVESTMENT") trong trường kinh nghiệm của tất cả hồ sơ đã thu thập. Có kết quả nghĩa là **cựu nhân sự đang nằm trong pool ứng viên** — dừng lại, tách riêng, báo người dùng, **không gửi lời mời tự động**. Lý do: (a) cựu nhân sự cần kênh tiếp cận riêng — lãnh đạo hoặc HR gọi trực tiếp, không phải lời mời máy móc từ hệ thống tuyển dụng; (b) chỉ nội bộ mới biết lý do người đó rời đi, đó là dữ kiện quyết định có nên mời lại hay không. Ca thật: một Commercial Card Product Owner tại VPBank — hồ sơ trúng JD nhất cả đợt — có dòng "giám đốc dự án công ty cổ phần đầu tư công nghệ SHT" giai đoạn 2021–2023 trong CV.

**Quét hồ sơ trùng người.** Cùng một ứng viên có thể có nhiều hồ sơ trên cổng (bản tiếng Việt và bản tiếng Anh, hoặc nhiều lần tải lên). Tên viết tắt hiển thị giống nhau không đủ để kết luận, mà tên viết tắt khác nhau cũng không loại trừ được. **Đối chiếu chuỗi công ty trong phần kinh nghiệm** — trùng chuỗi là trùng người. Không quét bước này thì gửi hai lời mời cho cùng một người: tốn gấp đôi credit và mất chuyên nghiệp.

## 5. Chấm điểm ASK — chỉ chấm bằng bằng chứng

Mô hình chuẩn SHT cho nhân viên thực thi/ứng viên tuyển dụng thường: **Attitude 30% + Skills 40% + Knowledge 30% = Điểm ASK tổng** (thang 1–5).
Ngưỡng xếp loại: **≥4.2 STRONG HIRE · ≥3.6 HIRE · ≥3.0 MIXED · <3.0 NO HIRE.**

**Vị trí Cán bộ quản lý (Trưởng Ban/Trưởng phòng/Giám đốc bộ phận trở lên) dùng trọng số RIÊNG: A60/S30/K10**, theo "Khung năng lực & Đánh giá Cán bộ quản lý SHT" (Phòng Nhân sự chủ quản) — vì kết quả của người quản lý đến từ dẫn dắt người khác, không từ tự mình làm. Cấu trúc tiêu chí: A1 Gắn kết nhân sự (20%), A2 Phát triển đội ngũ (20%), A3 Trách nhiệm & tuân thủ chỉ đạo (10%), A4 Cầu thị & minh bạch (10%), S1 Ủy quyền & phân công (10%), S2 Lập kế hoạch & kiểm soát tiến độ (10%), S3 Kiểm soát chi phí/nghiệp vụ đặc thù vị trí (10%), K1 Chuyên môn ngành (5%), K2 Quản trị & pháp lý liên quan (5%). Ngưỡng xếp loại dùng chung một chuẩn với ASK thường (≥4.2/3.6/3.0). **Luôn xác nhận đang chấm theo khung nào trước khi chấm** — cùng một ứng viên ra điểm khác hẳn nhau giữa hai khung vì trọng số lệch hoàn toàn (thực tế đã ghi nhận: một CBQL mạnh về Knowledge nhưng yếu về lãnh đạo con người tụt điểm khi đổi từ A30/S40/K30 sang A60/S30/K10, đúng như thiết kế).

**Quy tắc bắt buộc, không thương lượng:** điểm Attitude chỉ được chấm dựa trên **bằng chứng hành vi cụ thể xuất hiện trong CV** — lộ trình thăng tiến, trích dẫn nhận xét của quản lý cũ, mục tiêu nghề nghiệp thể hiện tư duy chủ động, sáng kiến/cải tiến quy trình đã làm. **Tuyệt đối không dùng ngoại hình, tuổi, giới tính, tình trạng hôn nhân** trong bất kỳ điểm số nào — vi phạm Điều 8 Bộ luật Lao động 2019 (nghiêm cấm phân biệt đối xử trong lao động). In dòng cảnh báo này ngay trên deliverable cuối cùng (cả Excel lẫn PDF), không chỉ tự nhắc thầm trong lúc chấm — biến nguyên tắc nội bộ thành thứ hội đồng nhìn thấy và tự kiểm chứng được.

### 5.1 Rubric phải có tiêu chí con — cấm chấm gộp

**Mỗi nhóm A/S/K tối thiểu 4–6 tiêu chí con**, mỗi tiêu chí một điểm 1–5 kèm **một câu bằng chứng trích từ CV**; điểm nhóm = trung bình các tiêu chí con, tính bằng công thức thật trong Excel. Chấm gộp mỗi nhóm một con số là lỗi: nó **che mất chỗ yếu** và khiến hội đồng không biết hỏi gì. Ca thật: Skills chấm gộp 4.6 đã giấu mất việc năng lực mua vật tư dự án chỉ đáng 3.0 — tách tiêu chí con ra thì tổng điểm tụt từ 4.24 (STRONG HIRE) xuống 4.03 (HIRE), đổi hẳn khuyến nghị.

**Bắt buộc có ít nhất một "tiêu chí bối cảnh"** trong Skills và một trong Knowledge, đo độ khớp với **nghiệp vụ thật của SHT**, tách riêng khỏi các tiêu chí khớp câu chữ JD. JD mô tả *đầu việc*, không mô tả *bối cảnh áp dụng* — đọc JD xong vẫn phải hỏi "vị trí này ở SHT thực tế làm gì". Ca thật: JD Mua hàng Nội địa không hề nói SHT mua vật tư cho **dự án cải tạo phòng giao dịch ngân hàng**; ứng viên mạnh ở **mua theo danh mục** (FMCG/bán lẻ, kế hoạch quý) trong khi SHT cần **mua theo dự án** (tiến độ gấp, chủng loại lẻ, bản vẽ chưa chốt) — hai mô hình khác nhau về nhịp làm việc.

### 5.2 Thiếu bằng chứng thì gắn nhãn, không trừ ngược điểm

Phân biệt hai tình huống, đừng trộn lẫn:

- **Không có bằng chứng nào cho tiêu chí này** → chấm thấp, hợp lệ.
- **Có bằng chứng nhưng chưa xác minh được** (chưa reference check, số liệu tự khai) → **giữ nguyên điểm, gắn nhãn độ tin cậy** ngay cạnh tên nhóm (VD "Attitude — toàn bộ tự khai, độ tin cậy thấp") và đưa việc cần xác minh sang bảng rủi ro. Trừ điểm phần *đã chứng minh được* vì phần *chưa xác minh* là lỗi trộn hai loại thông tin — làm hỏng cả điểm số lẫn cảnh báo.

### 5.3 Ba phép kiểm bắt buộc trên mọi CV

**Tính lại dòng thời gian từ NĂM TỐT NGHIỆP**, không từ mốc việc làm đầu tiên ứng viên liệt kê. Khoảng trống bị giấu chỉ lộ ra khi lấy năm tốt nghiệp làm mốc gốc. Ca thật: CV liệt kê từ 01/2017 (9 năm 7 tháng, khớp yêu cầu JD), nhưng tốt nghiệp 2009 → **khoảng trống ~7,5 năm** không giải thích — lỗ hổng lớn nhất của hồ sơ, suýt bị bỏ qua vì chỉ soi mốc đầu tiên trong CV.

**Khoảng trống tìm được là dữ kiện cho bảng rủi ro và câu hỏi phỏng vấn — KHÔNG phải căn cứ trừ điểm.** Phép kiểm này để *phát hiện*, không phải để *phạt*. Đưa khoảng trống vào bảng rủi ro kèm câu hỏi đóng mã là đủ; nếu đồng thời hạ điểm tiêu chí "minh bạch/độ tin cậy" thì cùng một sự việc bị phạt hai lần, và tổng điểm tụt sai lệch. Chỉ trừ điểm khi có **bằng chứng ứng viên khai sai**, không phải khi CV đơn thuần viết gọn. Ca thật 25/08/2026: chấm lại một hồ sơ Mua hàng Nội địa, khoảng trống 8 năm vừa bị hạ A4 xuống 2.8 vừa ghi thành rủi ro R1 → tổng 3.77; bỏ phần trừ điểm trùng thì về 3.83, cùng xếp loại HIRE nhưng phản ánh đúng hơn.

**Cảnh báo tuân thủ đi kèm:** quy khoảng trống thành điểm trừ có nguy cơ gián tiếp phạt ứng viên vì lý do cá nhân (nghỉ sinh con, chăm sóc gia đình, đi học tiếp, chữa bệnh) — đúng loại suy diễn mà Điều 8 Bộ luật Lao động 2019 nghiêm cấm. Hỏi thẳng trong phỏng vấn là cách xử lý đúng, suy đoán rồi trừ điểm là cách sai.

**Mọi con số thành tích phải kèm câu hỏi kiểm chứng** về (a) vai trò cá nhân hay của cả bộ phận, (b) phương pháp đo. "Tiết kiệm 10–20%/năm" tính theo giá năm trước, giá chào ban đầu, hay ngân sách được duyệt — ba cách cho ba con số khác hẳn nhau. Chưa hỏi thì chưa được dùng làm căn cứ chấm điểm cao.

**Hạn ứng tuyển là dữ kiện bắt buộc**, không phải thông tin phụ. Đưa lên header trang 1 cùng trạng thái (đã/chưa phỏng vấn), và biến thành khuyến nghị có mốc thời gian. Một đánh giá không gắn deadline thì hội đồng không biết cần quyết nhanh đến mức nào.

### 5.4 Khi có nhiều bản chấm độc lập — so dải điểm với ngưỡng

Khi cùng một CV được chấm bởi nhiều bên (HR, trợ lý AI, phiên làm việc khác), **đừng vội hỏi ai đúng ai sai — so dải điểm với ngưỡng xếp loại trước**:

- Dải nằm gọn một phía ngưỡng → khung đủ chặt, chênh lệch không đổi kết luận.
- **Dải cắt qua ngưỡng → lỗi hệ thống của khung**, không phải lỗi người chấm. Phải bổ sung tiêu chí rồi chấm lại trước khi trình hội đồng.

Ca thật: HR 4.30 · bản A 4.24 · bản B 4.05, ngưỡng STRONG HIRE 4.20 nằm lọt giữa dải → khuyến nghị đổi theo *ai chấm* chứ không theo *ứng viên*. Sau khi hợp nhất khung, điểm mới 4.03 **hội tụ** về bản chặt nhất (4.05, lệch 0.02) — dùng chính sự hội tụ đó làm kiểm chứng ngược cho khung mới, thay vì tự tuyên bố "khung này tốt hơn".

Trong bảng rubric, thêm cột **"Nguồn tiêu chí"** ghi tiêu chí đến từ bản chấm nào. Về sau rà soát sẽ biết nguồn nào hay bỏ sót gì.

Khi người dùng đưa ra **thứ tự ưu tiên xếp hạng riêng cho một đợt tuyển cụ thể** (VD "1. Kinh nghiệm 2. Kỹ năng 3. Banking 4. Địa chỉ Hà Nội 5. CV cập nhật <3 tháng"), dùng thứ tự đó để sắp xếp danh sách trước khi chấm ASK chi tiết — đây là bộ lọc thô nhanh để chọn ra nhóm đáng chấm điểm sâu, không thay thế cho mô hình ASK khi xuất deliverable cuối.

## 6. Đối chiếu lương kỳ vọng với ngân sách JD

JD của SHT thường đi kèm khung lương 3P (P1 = vị trí, P2 = hiệu suất/KPI, P3 = 20–30% thưởng vượt KPI). **Luôn đọc số thật trong JD của từng vị trí** — khung 3P khác nhau theo từng JD, không suy diễn từ khung chung của công ty. Tính trần ngân sách tham chiếu = P1 tối đa + P2 tối đa (P3 là biến động, không cộng cứng vào trần).

Khung 3P tổng quát của SHT (dùng khi JD không nêu số riêng):

- Sale: P1 Bậc 1 = 8tr → Bậc 5 = 16tr; P2 Bậc 1 = 4tr → Bậc 9 = 12tr.
- Back Office: P1 Bậc 1 = 8tr → Bậc 6 = 18tr; P2 Bậc 1 = 2tr → Bậc 9 = 10tr.
- Chuẩn chung: 14 tháng lương/năm, ăn trưa + xăng 1tr/tháng, du lịch 10tr/năm, 12 ngày phép/năm, lương công khai. Trần chuyên gia nước ngoài (Hàn Quốc): 5.000 USD/tháng.

Khi ứng viên có công khai mức lương kỳ vọng, so với trần và gắn nhãn rõ (phù hợp / vượt ngân sách / cần thương lượng). Khi không công khai, ghi "Thỏa thuận" — không tự đoán một con số.

**Vị trí chưa có bậc 3P sẵn (thường là C-level mới mở)**: dựng trần ngân sách bằng kỹ thuật đối chiếu 2 lớp mô tả ở §2b.2 — khảo sát thị trường ngoài + dữ liệu ứng viên thực đã ứng tuyển vào chính công ty ở vị trí liền kề thấp hơn. Hai lớp lệch nhau nhiều thì ưu tiên lớp dữ liệu nội bộ (sát khả năng thu hút thực tế hơn số liệu thị trường chung), nhưng vẫn trình cả hai để người phê duyệt tự đối chiếu, không chỉ đưa một con số chốt sẵn.

## 7. Xuất deliverable song song

**Bắt buộc xuất cả hai:**

- **Excel scorecard** — công cụ làm việc của HR: có công thức thật (không hard-code kết quả), có cột bằng chứng trích dẫn cho từng điểm số, có công thức xếp loại và đối chiếu ngân sách tự động tính lại được khi đổi số liệu đầu vào.
- **PDF trình hội đồng** — trực quan, không cần biết đọc Excel. Chuẩn màu/font SHT: header navy đặc `#0B2545` (không dùng gradient), font Times New Roman, nền trắng, khổ A4 nằm ngang.

Không gộp hai mục đích vào một file — người chấm điểm cần công thức để audit, hội đồng cần nhìn là hiểu, hai nhu cầu này không thỏa mãn bằng cùng một layout.

**Chọn độ dài PDF theo mục đích, không mặc định 1 trang:**

| Mục đích | Định dạng |
|---|---|
| Sàng lọc / so nhiều ứng viên | Infographic **1 trang** — nhìn là hiểu, xếp cạnh nhau so được |
| Đánh giá ứng viên vào vòng cuối | Scorecard **2 trang** (cấu trúc 7 khối bên dưới) |

**Cấu trúc scorecard 2 trang — dùng làm template:**

*Trang 1 — bức tranh & bằng chứng:* (1) header có điểm tổng, 3 điểm nhóm, hạn ứng tuyển, trạng thái; (2) kết luận sơ bộ 3–4 câu; (3) chi tiết chấm điểm theo tiêu chí con kèm thanh điểm; (4) lộ trình nghề nghiệp **tính lại từ năm tốt nghiệp**; (5) bảng đối chiếu từng dòng yêu cầu bắt buộc của JD với nhãn VƯỢT / ĐẠT / ĐẠT CÓ ĐIỀU KIỆN / CHƯA ĐẠT.

*Trang 2 — hành động:* (6) điểm mạnh; (7) bảng rủi ro **mã hóa R1…Rn** kèm mức CAO/T.BÌNH/THẤP và nguồn phát hiện; (8) câu hỏi phỏng vấn, **mỗi câu ghi rõ đóng mã rủi ro nào** ("ĐÓNG R3"); (9) bài tập tình huống; (10) khuyến nghị bước tiếp theo có mốc thời gian; (11) khối chữ ký ba cấp (người lập / GĐ Nhân sự / Ban Lãnh đạo).

Gắn mã rủi ro với câu hỏi là điểm mấu chốt — không còn cảnh liệt kê một loạt rủi ro rồi một loạt câu hỏi mà không ai biết câu nào giải quyết rủi ro nào.

### 7.1 Excel — quy tắc kỹ thuật

- Dùng `openpyxl`, viết công thức thật (`=I6*0.3+K6*0.4+M6*0.3`), không tính sẵn bằng Python rồi ghi số. Xếp loại dùng `IF` lồng nhau (an toàn với LibreOffice) thay vì `_xlfn.IFS`.
- **Luôn chạy `recalc.py` sau khi tạo/sửa file**, yêu cầu `total_errors: 0`.
- Sau `recalc`, đọc lại bằng `load_workbook(data_only=True)` và kiểm tra **cả cột chữ lẫn cột số** — lỗi chuỗi literal (VD dư dấu cách trong `"Cần thương lượng"`) không bị `recalc.py` báo lỗi vì nó không phải lỗi công thức, chỉ hiện ra khi đọc lại giá trị thật.
- Nếu `rm`/ghi đè file bị từ chối quyền ngay sau khi một chương trình ngoài (LibreOffice, `pdftoppm`...) vừa chạy trên file đó (thường do file khoá `.~lock.*#` hoặc đổi chủ sở hữu trong sandbox): đừng cố gỡ khoá, chuyển sang thư mục/tên file mới — nhanh hơn nhiều so với debug quyền hạn.

### 7.2 PDF — quy tắc kỹ thuật

- Dựng bằng HTML/CSS render qua WeasyPrint (`pip install weasyprint --break-system-packages` nếu chưa có sẵn) — cho phép thiết kế card, thanh điểm ASK, tag màu theo xếp loại nhanh hơn nhiều so với vẽ tay bằng `reportlab`. Kỹ thuật xuất PDF dùng chung (CSS chuẩn tiếng Việt, khổ cố định): theo `sht-nen-tang-kiem-chung` §6.1.
- **Khổ chuẩn của scorecard: A4 ngang, 96dpi ≈ 1122px trừ lề.** Quy tắc tính bề rộng in được và ép `flex-wrap: nowrap`: theo nền §6.1.
- Render thử ra ảnh (`pdftoppm -png -r 100`) và **nhìn tận mắt** trước khi giao — chữ không bị cắt, thanh điểm không tràn khung. Kiểm **số trang bằng `pdfinfo`** trước khi render: khối chữ ký cuối trang 2 rất hay đẩy tràn thành trang 3 trắng — khi đó nén khoảng cách dọc (margin khối chữ ký, `margin-bottom` của `li`), đừng giảm cỡ chữ.
- In cảnh báo tuân thủ (§5) trực tiếp trên trang, không chỉ trong Excel.

## 8. Ranh giới hành động

**Được làm tự do, không cần hỏi:** tìm kiếm, lọc, mở xem CV công khai, chấm điểm, tính toán, xuất báo cáo.

**Luôn hỏi trước khi làm:** gửi yêu cầu kết nối với ứng viên, dùng phí/CP của tài khoản để mở khóa thông tin liên hệ, nhắn tin/gọi điện cho ứng viên, đăng tin tuyển dụng mới. Đây là hành động gửi thông tin thay mặt người dùng hoặc tốn phí tài khoản của họ — không tự ý thực hiện dù có vẻ "hợp lý để tiết kiệm thời gian cho người dùng".

> Luồng UI thực tế của nút kết nối trên TopCV và LinkedIn (trạng thái nào bấm được, trạng thái nào không): `references/thao-tac-cong-tuyen-dung.md` §4. Khi modal kết nối LinkedIn không thao tác được: §7.

**LinkedIn — không tự động hoá gửi kết nối thành thao tác lặp lại định kỳ.** Khác với tài khoản nhà tuyển dụng TopCV (nền tảng B2B chính thức), LinkedIn cá nhân có giới hạn số lời mời/tuần và cơ chế phát hiện hành vi bất thường — gửi hàng loạt lặp lại mỗi ngày như một scheduled task có rủi ro ảnh hưởng tài khoản cá nhân của người dùng. Mỗi đợt gửi kết nối LinkedIn phải **xin phép lại** (không dùng phạm vi đã duyệt từ lần trước), và chỉ gửi theo danh sách cụ thể đã được duyệt, không tự mở rộng thêm.


## 9. Vận hành scheduled task hunt CV định kỳ

Khi hunt CV được đưa vào lịch chạy hàng ngày/định kỳ (không phải chạy 1 lần):

- Mỗi chiến dịch/nguồn cần hunt định kỳ nên có bộ lọc **đã được tinh chỉnh và test bằng số liệu** (theo §3) trước khi đưa vào task, không đưa bộ lọc thô "đoán đại" vào chạy lặp lại mỗi ngày. Một lỗi cấu hình sẽ âm thầm chạy sai suốt nhiều ngày.
- Khi thêm một chiến dịch mới vào task đang chạy nhiều chiến dịch, **rà soát lại các chiến dịch cũ** — nếu một chiến dịch có bộ lọc lỏng hơn so với chiến dịch mới vừa tinh chỉnh kỹ, đề xuất bỏ bớt thay vì cộng dồn mãi. "Lean" cấu hình định kỳ, không chỉ cộng dồn.
- Ghi rõ trong task: retry tối đa 2 lần cho lỗi kỹ thuật trình duyệt trước khi dừng và báo cáo; lỗi ở 1 chiến dịch không được chặn các chiến dịch còn lại.
- Báo cáo mỗi lượt chạy nêu rõ số ứng viên MỚI so với lần trước (không liệt kê lại ứng viên cũ đã đánh giá), tách rõ theo từng chiến dịch.
- **Chỉ đưa vào lịch chạy tự động lặp lại các nguồn có tài khoản nhà tuyển dụng chính thức (TopCV, VietnamWorks Employer).** LinkedIn cá nhân không đưa vào scheduled task định kỳ (xem lý do ở §8) — mỗi lượt hunt LinkedIn là một tác vụ được yêu cầu và duyệt phạm vi riêng.

### 9.1 Cổng kiểm bộ lọc — chạy trước khi đọc ứng viên đầu tiên

**Bộ lọc trên cổng tuyển dụng là trạng thái lưu trên server theo chiến dịch, không nằm trong URL.** Mọi thay đổi thủ công — của người dùng, của đồng nghiệp, hay của chính lần chạy trước — sẽ dính vĩnh viễn cho tất cả các lần chạy sau. "URL đúng" không bảo chứng "bộ lọc đúng". Vì vậy mọi task hunt CV định kỳ phải ghi bộ lọc chuẩn thành **danh sách chip tường minh** trong chính task, và mỗi lượt chạy phải kiểm lại trước khi đọc ứng viên.

**Đối chiếu theo TẬP HỢP CHÍNH XÁC, không theo phép "có chứa".** Kiểm kiểu "đủ các chip cần thiết chưa" chỉ bắt được chip *thiếu* và mù hoàn toàn với chip *thừa* — trong khi chip thừa mới là thứ nguy hiểm nhất, vì một chip lạ trong ô AND bóp kết quả về gần 0 mà giao diện vẫn trông bình thường. Phải báo cả hai chiều: thừa gì, thiếu gì. Ca thật 28/08/2026, chiến dịch "Platform BA & PM": một chip "FinOps" thừa trong ô "bắt buộc có từ khóa" đã bóp kết quả từ **155 xuống 1** ứng viên; nếu lần chạy đó chỉ báo "hôm nay chỉ có 1 ứng viên" thì chiến dịch coi như mù mà không ai biết.

**Ghi baseline số kết quả vào task và kiểm ngưỡng mỗi lượt chạy.** Task phải lưu con số ứng viên đo được với bộ lọc chuẩn tại ngày thiết lập. Mỗi lượt chạy so tổng số trả về với baseline đó:
- Tụt dưới ~2/3 baseline → coi là bất thường, quay lại kiểm bộ lọc lần nữa **trước khi** kết luận bất cứ điều gì.
- **Tuyệt đối không báo "không có ứng viên mới" khi tổng số tụt sâu bất thường** — đó gần như luôn là lỗi cấu hình, không phải thị trường cạn hồ sơ. Kết luận "không có ai mới" chỉ hợp lệ sau khi cổng kiểm bộ lọc đã PASS.
- Lệch >30% theo cả hai chiều mà bộ lọc đã đúng chuẩn → vẫn ghi vào báo cáo để người dùng biết pool đã đổi.

**Agent tự sửa bộ lọc lệch rồi báo cáo rõ, không dừng chờ duyệt và cũng không sửa im lặng.** Dừng chờ duyệt làm mất trọn một ngày hunt; sửa im lặng thì lần sau lại tái diễn mà không ai truy được nguyên nhân. Đường đúng: đưa bộ lọc về chuẩn, chạy tiếp, và đặt **"Tình trạng bộ lọc" làm mục đầu tiên của báo cáo** — khớp hay lệch, chip nào đã thừa/thiếu, tổng số so với baseline.

**Agent không được tự thêm từ khóa vào bộ lọc của task định kỳ.** Đọc CV thấy một thuật ngữ hay (VD "FinOps") là cảm hứng để *đề xuất*, không phải lý do để tự chỉnh bộ lọc đang chạy. Đổi bộ lọc phải do người dùng yêu cầu rõ ràng, và phải cập nhật lại danh sách chip chuẩn + baseline trong chính task — nếu không, task và thực tế sẽ trôi xa nhau.


## 10. Bàn giao (tuyển dụng)

Tóm tắt cuối cùng phải **ngắn**: nêu 1–2 hành động ưu tiên rõ nhất (VD "liên hệ ứng viên X trước — điểm cao nhất khu vực Y"), 1–2 cảnh báo quan trọng nhất (vượt ngân sách, đã liên hệ trước nhưng chưa phản hồi...). Không liệt kê lại toàn bộ bảng điểm trong tin nhắn — dữ liệu đầy đủ đã nằm trong file Excel/PDF.

**Chưa có quyền ghi vào thư mục nghiệp vụ thì hỏi trước, tuyệt đối không lưu tạm rồi báo hoàn thành.** Khi phiên làm việc chưa kết nối thư mục nào của người dùng, chỗ duy nhất ghi được là thư mục tạm của phiên — người dùng **không nhìn thấy** thư mục này. Ghi vào đó rồi báo "đã lưu xong" là báo cáo sai sự thật, dù file có tồn tại thật. Đường đi đúng: yêu cầu quyền truy cập thư mục nghiệp vụ trước, rồi ghi thẳng vào đó. Câu "đã lưu xong" chỉ được nói khi file nằm ở nơi người dùng mở được. Ca thật 25/08: file danh sách CV bị ghi vào thư mục tạm của phiên và báo hoàn thành, người dùng phát hiện "output đang ghi lung tung".

Khi người dùng có nhiều folder chia sẻ khác nhau, **chọn đúng folder theo nghiệp vụ của deliverable** (VD: JD/hồ sơ ứng viên → folder tuyển dụng, không mặc định lưu vào folder làm việc/kho skill chung đầu tiên tìm thấy), và **đặt tên file theo quy ước sẵn có trong chính folder đó** — mở folder xem các file cùng loại đang đặt tên thế nào rồi theo, đừng tự nghĩ quy ước mới. Nếu đường dẫn người dùng đưa báo không tồn tại, **thử các biến thể gần đúng** (thiếu/thừa chữ "s", dấu tiếng Việt, tên thư mục cha) trước khi báo lỗi — người dùng gõ nhanh thường sai một ký tự. Dùng công cụ trình bày file để người dùng thấy ngay, không chỉ nói "đã lưu xong".

**Số lượng hành động đã thực hiện phải đếm từ log thao tác thực tế, không từ trí nhớ của các báo cáo trước**, và phải **đối chiếu với màn hình xác nhận của chính nền tảng** (Trình quản lý lời mời của LinkedIn, trạng thái "Chờ UV phản hồi" của TopCV). Ca thật: báo cáo "16 lời mời" trong khi thực tế là 18 — sót 2 người khi tổng hợp từ các báo cáo giữa chừng. Sai số này làm hỏng cả bảng theo dõi lẫn niềm tin vào các con số còn lại.

Xưng hô: xưng "em", gọi người dùng "anh"; trả lời tiếng Việt; súc tích.

---

## Checklist trước khi bàn giao (riêng tuyển dụng)

Chạy checklist nền ở `sht-nen-tang-kiem-chung` §5, rồi chạy tiếp checklist riêng của tuyển dụng ở `references/checklist-tuyen-dung.md` — mở khi sắp bàn giao, không nạp sẵn.

## Sổ tra cứu thao tác — mở khi cần, không nạp sẵn

| File | Nội dung | Khi nào mở |
|---|---|---|
| `references/thao-tac-cong-tuyen-dung.md` | Lọc & đọc trang trên TopCV/LinkedIn, xử lý lỗi công cụ trình duyệt, luồng nút kết nối, **sửa state Vue khi ô lọc chết (§5), quét hàng loạt từ `p4.cvs` (§6), LinkedIn `/preload/custom-invite/` khi modal shadow DOM (§7)** | **Bắt buộc** trước bước [3]–[4] khi có thao tác trình duyệt |
| `references/nguon-quy-tac.md` | Nguồn của từng nhóm quy tắc theo chiến dịch, lịch sử nâng cấp, cảnh báo trôi nhánh | Khi rà soát/nâng cấp skill, hoặc cần biết một quy tắc đến từ đâu |

Khi phát sinh chiến dịch mới có bài học mới: **quy tắc quyết định** bổ sung vào thân
(§1–§10), **chi tiết thao tác nền tảng** bổ sung vào `references/`. Không thêm phụ lục
case study mới vào thân — skill phình to là skill khó nâng cấp.
