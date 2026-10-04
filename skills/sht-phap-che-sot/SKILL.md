---
name: "sht-phap-che-sot"
description: "Tra và trích nguyên văn văn bản pháp luật VN có toạ độ Điều/Khoản, hiệu lực TẠI MỐC vụ việc, bảng Source of Truth, xung đột luật, stress-test. LUÔN dùng khi hỏi \"căn cứ pháp lý\", \"luật còn hiệu lực không\", \"mức phạt\", \"lấy SOT\". KHÔNG dùng để rà hợp đồng, soạn QĐ; tư vấn rủi ro chung: phap-che-doanh-nghiep. Không thay luật sư."
---

# Pháp chế & Căn cứ Source of Truth (SHT)

> Phương pháp gốc: AI48S tư vấn pháp luật (vietduc·ai). SHT viết lại 27/09/2026 theo 5 luật cứng; mọi điều luật cụ thể lấy từ references/danh-muc-van-ban-goc.md (Claude đối chiếu).

Skill này là chốt chặn căn cứ pháp lý: tra cứu, trích xuất nguyên văn có tọa độ chính xác (Chương/Điều/Khoản/Điểm) và thẩm định hiệu lực văn bản quy phạm pháp luật Việt Nam tại đúng mốc thời gian của vụ việc. Skill cung cấp bảng Source of Truth (SOT) chuẩn mực cho các tác vụ tư vấn nội bộ, soạn quyết định hoặc rà soát hợp đồng.

---

## CỔNG CHẶN & NGUYÊN TẮC BẤT DI BẤT DỊCH

1. **Công cụ tra cứu chuẩn:** Chỉ sử dụng `WebSearch` và `WebFetch`. Đây là các công cụ deferred, bắt buộc nạp qua `ToolSearch` (`select:WebSearch,WebFetch`) trước khi gọi. Tuyệt đối không gọi các tên công cụ không tồn tại.
2. **Đường dẫn ghi đầu ra:** Kết quả phân tích và bảng SOT lưu tại `data/workspaces/<ws>/phap-che/<chu-de>/`. Nếu chưa xác định được workspace, bắt buộc hỏi người dùng theo hiến pháp SHT, không suy đoán.
3. **Phân biệt tiến trình:** Sử dụng các nhãn bước H1–H5 hoặc 'bước' tác nghiệp; không dùng chữ 'giai đoạn' để tránh nhầm lẫn với 11 giai đoạn chuyển đổi số SHT.
4. **Không tự khẳng định số hiệu luật thật:** Agent dùng skill tuyệt đối không tự khẳng định số hiệu văn bản, điều khoản hoặc tình trạng hiệu lực. Mọi trích dẫn cụ thể phải đối chiếu qua `references/danh-muc-van-ban-goc.md` và `references/sot-mau-da-doi-chieu.md`.
5. **Ranh giới trách nhiệm:** Báo cáo pháp chế nội bộ phục vụ quản trị và kiểm soát rủi ro, không thay thế ý kiến tư vấn pháp lý chính thức của luật sư có chứng chỉ hành nghề. Bàn giao văn bản theo `sht-nen-tang-kiem-chung`.

---

## BƯỚC H1 — CHUYỂN ĐỔI YÊU CẦU SANG 5 TRỤC TỌA ĐỘ PHÁP LÝ

> Nguồn AI48S: §3 5 trục toạ độ + cảnh báo bẫy ngược.

Khi tiếp nhận yêu cầu từ người dùng hoặc từ các skill nghiệp vụ khác, hệ thống chuẩn hóa tình huống thành 5 trục tọa độ định danh:

| Trục Tọa Độ | Ý Nghĩa Nghiệp Vụ | Ví Dụ Bối Cảnh Doanh Nghiệp / CNTT | Định Danh Pháp Lý Mục Tiêu |
|---|---|---|---|
| **ĐỐI TƯỢNG** | Chủ thể tham gia quan hệ pháp luật | Doanh nghiệp phần mềm, nhà thầu phụ CNTT, khách hàng tổ chức | Pháp nhân thương mại, bên cung ứng dịch vụ, bên sử dụng dịch vụ |
| **HÀNH VI** | Hành vi pháp lý phát sinh | Tạm ngừng dịch vụ Cloud, vi phạm SLA, đơn phương hủy bỏ hợp đồng | Vi phạm nghĩa vụ hợp đồng, chấm dứt thực hiện nghĩa vụ |
| **TÁC ĐỘNG** | Hậu quả, thiệt hại và chế tài | Nguy cơ bị phạt hợp đồng, đòi bồi thường thiệt hại, tranh chấp | Phạt vi phạm, bồi thường thiệt hại, chế tài tài chính |
| **PHẠM VI** | Lĩnh vực chuyên ngành, địa bàn | Cung cấp giải pháp SaaS xuyên biên giới, xử lý dữ liệu cá nhân | Pháp luật thương mại, công nghệ thông tin, an toàn thông tin |
| **THỜI ĐIỂM ★** | Mốc thời gian cốt tử của sự kiện | Hợp đồng ký ngày DD/MM/YYYY, sự cố phát sinh ngày DD/MM/YYYY | Xác định văn bản quy phạm pháp luật có hiệu lực tại thời điểm ký/vi phạm |

> **Cảnh báo Bẫy Ngược (Reverse Trap Warning):** Ngay khi giải mã tình huống, nếu phát hiện ý định áp dụng chế tài trái luật (như ấn định mức phạt vi phạm vượt quá trần luật định, giữ lương trái quy định, đơn phương chấm dứt hợp đồng không tuân thủ thời hạn báo trước), skill kích hoạt cảnh báo đỏ về rủi ro pháp lý mà chính doanh nghiệp sẽ gánh chịu.

---

## BƯỚC H2 — THẨM VẤN NGƯỢC KHI THIẾU DỮ KIỆN

> Nguồn AI48S: §4 Thẩm vấn ngược.

Pháp luật đòi hỏi chứng cứ xác thực. Khi tình huống người dùng cung cấp còn thiếu dữ kiện mấu chốt, skill không đưa ra kết luận giả định mà kích hoạt phỏng vấn ngược theo 3 nhóm câu hỏi tử huyệt:

1. **Về Thẩm quyền & Quy chế nền tảng:**
   - Người ký kết hợp đồng/văn bản có đúng thẩm quyền đại diện theo pháp luật hoặc văn bản ủy quyền hợp lệ không?
   - Doanh nghiệp đã ban hành và công bố quy chế nội bộ, quy trình kỹ thuật liên quan hợp lệ chưa?
2. **Về Hồ sơ Bằng chứng vật lý:**
   - Sự kiện vi phạm hoặc nghiệm thu có biên bản hiện trường, log hệ thống, email công vụ xác nhận giữa hai bên không?
   - Các bên đã lập văn bản thông báo hoặc biên bản làm việc ghi nhận sự việc chưa?
3. **Về Trình tự & Thời hạn luật định:**
   - Mốc thời gian xảy ra vụ việc đến nay có còn trong thời hiệu khiếu nại hoặc khởi kiện không?
   - Bên khiếu nại đã gửi thông báo bằng văn bản trước bao nhiêu ngày theo đúng thỏa thuận hợp đồng và quy định pháp luật?

*Lưu ý:* Khi cần phỏng vấn chuyên sâu kéo dài để làm rõ bài toán phức tạp, chuyển sang kỹ năng `grill-me`.

---

## BƯỚC H3 — CHU TRÌNH PDCA CASCADE & THUẬT TOÁN PHÂN XỬ XUNG ĐỘT

> Nguồn AI48S: §5 PDCA + Lex.

Nghiên cứu và thiết lập căn cứ pháp lý được vận hành theo chu trình PDCA:

- **[P] Plan (Kế hoạch tra cứu):** Xác định từ khóa tra cứu theo 3 chiều (chiều dọc văn bản hướng dẫn, chiều ngang sửa đổi/bổ sung, chiều thời gian hiệu lực).
- **[D] Do (Tra cứu thực chứng):** Nạp `ToolSearch` (`select:WebSearch,WebFetch`), tra cứu nguồn chính thống (xem `references/nguon-tra-cuu.md`). Trích xuất nguyên văn có tọa độ: Cấp văn bản – Số hiệu – Điều – Khoản – Điểm. Chi tiết định dạng: xem `references/trich-dan-sot.md`. Văn bản gốc là **PDF scan** (trích chữ gần như rỗng) hoặc trang web không tải được nội dung: xem `references/nguon-tra-cuu.md` mục 6 — không kết luận "không có điều X" từ lần tìm chữ rỗng.
- **[C] Check (Kiểm tra & Phân xử xung đột):** So khớp trạng thái hiệu lực tại mốc thời điểm. Khi có xung đột giữa các văn bản, áp dụng thuật toán phân xử:
  * **Lex superior (Thứ bậc):** Văn bản cấp cao hơn ưu tiên áp dụng so với văn bản cấp thấp hơn (Luật > Nghị định > Thông tư).
  * **Lex posterior (Thời gian):** Cùng cấp ban hành, văn bản ban hành sau ưu tiên áp dụng so với văn bản ban hành trước.
  * **Lex specialis (Chuyên ngành):** Lex specialis là **nguyên tắc học lý**; Đ.58 Luật 64/2025 chỉ quy định văn bản cấp cao hơn (k.3) và văn bản ban hành sau (k.4) — xem `references/danh-muc-van-ban-goc.md` mục 1.
- **[A] Act (Lập bảng SOT & Lưu vết):** Tổng hợp dữ liệu vào bảng Source of Truth (SOT) và lưu vết tại `data/workspaces/<ws>/phap-che/<chu-de>/`.

Chi tiết kỹ thuật tra cứu 3 chiều: xem `references/tra-cheo-3-chieu.md`. Tổng quan hệ thống văn bản: xem `references/he-thong-vbqppl.md`.

---

## BƯỚC H4 — KHUNG STRESS-TEST PHÁP LÝ & GIẢ LẬP ĐÒN PHẢN CÔNG

> Nguồn AI48S: §6 Stress-test.

Trước khi hoàn thiện giải pháp, tiến hành kiểm thử độ bền pháp lý bằng cách đóng vai đối phương hoặc cơ quan thanh tra để tìm điểm yếu theo khung 3 cột:

| Kịch Bản Đòn Tấn Công Đối Phương | Cơ Sở Lập Luận Phản Bác | Biện Pháp Phòng Vệ / Chứng Cứ Cần Lập |
|---|---|---|
| **Đòn 1: Vô hiệu hóa quy trình / thẩm quyền** | Nại lý do người ký không đủ thẩm quyền, thông báo không hợp lệ | Chuẩn bị văn bản ủy quyền, dấu thời gian gửi bưu chính có bảo đảm, log xác thực điện tử |
| **Đòn 2: Phản tố điều khoản vô hiệu / vượt trần** | Khiếu nại mức phạt vi phạm hoặc lãi suất thỏa thuận vượt mức trần luật định | Tách bạch khoản phạt vi phạm với bồi thường thiệt hại thực tế; kiểm tra trần theo SOT |
| **Đòn 3: Tranh chấp phạm vi & thoái thác nghĩa vụ** | Đối tác từ chối nhận lỗi vi phạm SLA hoặc chậm tiến độ do lỗi bên thứ ba | Cung cấp biên bản nghiệm thu từng phần, log ghi nhận sự cố chi tiết, điều khoản bất khả kháng |

---

## BƯỚC H5 — CẤU TRÚC BÁO CÁO PHÁP CHẾ 5 PHẦN

> Nguồn AI48S: §7 Báo cáo 5 phần.

Báo cáo pháp chế được xuất thành văn bản độc lập tại `data/workspaces/<ws>/phap-che/<chu-de>/bao-cao-phap-che.md` gồm 5 phần:

1. **Phần 1: Xác lập tọa độ 5 trục & Tóm tắt sự kiện pháp lý:** Khái quát bối cảnh, chủ thể, hành vi và mốc thời gian cốt tử.
2. **Phần 2: Bảng Source of Truth (SOT) Căn cứ pháp lý:** Bảng tổng hợp trích dẫn nguyên văn, tọa độ pháp lý, tình trạng hiệu lực, URL nguồn + ngày truy cập, và vai trò giải quyết vụ việc.
3. **Phần 3: Phân tích & Ma trận đánh giá phương án:** So sánh các kịch bản hành động theo thang điểm 1–5 (Độ vững pháp lý, Mức độ rủi ro, Tính khả thi vận hành).
4. **Phần 4: Khuyến nghị đường lối & Kế hoạch hành động:** Lộ trình triển khai từng bước kèm danh mục biểu mẫu, văn bản cần chuẩn bị.
5. **Phần 5: Khung Stress-test phòng vệ & Cảnh báo rủi ro:** Phân tích điểm tựa phản biện và tuyên bố miễn trừ trách nhiệm pháp lý.

---

## CỔNG KIỂM SOÁT CHẤT LƯỢNG (QUALITY GATE)

> Nguồn AI48S: §9 Cổng chất lượng.

Trước khi bàn giao kết quả, agent bắt buộc kiểm tra 13 tiêu chí chất lượng (1–12 và 10b):

- [ ] 1. Đã chuyển hóa tình huống thành đủ 5 trục tọa độ (đặc biệt xác định chính xác THỜI ĐIỂM)?
- [ ] 2. Đã cảnh báo người dùng nếu phát hiện dấu hiệu vi phạm pháp luật (bẫy ngược)?
- [ ] 3. Đã kích hoạt thẩm vấn ngược khi dữ kiện mấu chốt còn thiếu (trỏ `grill-me` khi cần)?
- [ ] 4. Mọi trích dẫn đều có tọa độ chính xác: Cấp văn bản – Số hiệu – Điều – Khoản – Điểm?
- [ ] 5. Mỗi dòng trong bảng SOT đều có URL nguồn + ngày truy cập cụ thể, và bảng có **ít nhất 3 trích dẫn NGUYÊN VĂN** (không diễn giải)? Vụ việc chỉ có 1–2 căn cứ thật thì ghi rõ số căn cứ, không độn cho đủ 3.
- [ ] 6. Trạng thái hiệu lực của văn bản khớp chính xác với mốc thời gian của vụ việc?
- [ ] 7. Đã tra chéo đủ 3 chiều: Chiều dọc (Nghị định/Thông tư), Chiều ngang (Sửa đổi), Chiều thời gian — **và chiều chuyên ngành** khi vụ việc có luật chuyên ngành (ngân hàng, viễn thông, xây dựng…) đè lên luật chung?
- [ ] 8. Đã phân xử mâu thuẫn theo nguyên tắc Lex superior / posterior / specialis (specialis: học lý)?
- [ ] 9. Đã thực hiện Stress-test theo khung 3 cột giả định đòn phản công?
- [ ] 10. Đã so sánh các phương án xử lý theo thang điểm 1–5?
- [ ] 10b. Đã lập **phòng tuyến bảo vệ**: liệt kê hồ sơ/bằng chứng SHT cần lập hoặc lưu ngay bây giờ để đứng vững nếu bị thanh tra/khởi kiện?
- [ ] 11. Đã ghi file báo cáo độc lập vào `data/workspaces/<ws>/phap-che/<chu-de>/`?
- [ ] 12. Khung chat chỉ hiển thị bản tóm tắt điều hành, bảng định danh 5 trục và liên kết mở báo cáo?

**Đối chiếu với 15 tiêu chí gốc AI48S** *(thêm 30/09/2026, v0.29.0 — bản 0.28.0 rút 15→12 mà không ghi lý do, không tìm thấy lý do trong plan/report P3, nên ghi đối chiếu tại đây)*:

| Gốc AI48S | Ở đây | Lý do |
|---|---|---|
| #1–3, #6, #7, #9, #10, #12, #15 | 1–4, 6, 8–10, 12 | Giữ nguyên ý |
| #4 tạo thư mục `legal_research_*/` + file phase | gộp vào 11 | SHT ghi vào `data/workspaces/<ws>/phap-che/` (luật Output) |
| #5 ≥3 trích dẫn nguyên văn | **khôi phục** vào 5 | Bị rút không lý do; nguyên văn là lõi của SOT |
| #8 chiều chuyên ngành | **khôi phục** vào 7 | Bản 0.28.0 thay bằng "chiều thời gian"; nay giữ cả hai |
| #11 phòng tuyến bảo vệ | **khôi phục** thành 10b | Bị rút không lý do; là đầu ra hành động cho SHT |
| #13 báo cáo độc lập | 11 | Giữ ý, đổi đường dẫn |
| #14 khối bàn giao cho skill xuất bản của gói AI48S | **bỏ có chủ ý** | Skill nhận không có trong SHT; bàn giao theo mục "Phối hợp & bàn giao liên skill" |

---

## PHỐI HỢP & BÀN GIAO LIÊN SKILL

- **Rà soát hợp đồng:** Khi rà soát điều khoản chi tiết, SoW, BRD, chuỗi hợp đồng CNTT hoặc phân tích rủi ro thương mại, bàn giao cho `ra-soat-hop-dong-vendor`.
- **Quyết định nhân sự:** Khi cần soạn thảo hoặc căn chỉnh thể thức Quyết định nhân sự, chuyển tiếp sang `sht-qd-nhansu-alignment`.
- **Kiến trúc hồ sơ:** Khi cần quy hoạch toàn diện danh mục hồ sơ pháp lý theo các pha vòng đời, bàn giao cho `sht-kien-truc-ho-so`.
- **Xuất bản & Kiểm chứng:** Mọi hoạt động bàn giao, kiểm chứng số liệu và xuất bản văn bản tuân thủ chuẩn `sht-nen-tang-kiem-chung`.
- **Đại diện tác nghiệp (chỉ khi mở dự án SHT):** Nếu phiên có agent `sht-legal` (khai báo ở `.claude/agents/` của dự án SHT, **không** đóng trong gói plugin này), có thể giao vai pháp chế cho agent đó. Không có thì tự làm theo skill này — không coi là lỗi.
