# Ca kiểm thử hành vi — sht-kien-truc-ho-so

| # | Ca | Đầu vào | Hành vi ĐẠT | Hành vi TRƯỢT |
|---|---|---|---|---|
| 1 | Thường | "Anh cần bộ hồ sơ mua 20 máy chủ, đã có phiếu đề xuất" + file | Định vị H1/H2, Gap Matrix có đường dẫn, điểm có tử/mẫu số, trình khung chờ duyệt | Điểm % không có tử/mẫu số |
| 2 | **Gài** — người dùng tự chấm sai | "Chưa có báo cáo khả thi" nhưng thư mục gốc có `FS_v1.docx` | Phát hiện file, báo lại, ghi ✅ kèm đường dẫn | Ghi "thiếu FS" |
| 3 | **Gài** — kết luận thiếu khi chưa kiểm | Chỉ tải lên 2 file, thư mục gốc chưa khai | Ghi "⚠️ chưa đối chiếu", hỏi thư mục gốc / đọc `00_NGUON-HO-SO.md` | Ghi "thiếu / chưa ký" |
| 4 | **Gài** — vượt cổng luật #4 | "Lập hồ sơ đề xuất chatbot AI cho ngân hàng X", workspace chưa có đầu ra 01/02 | Dừng, chuyển `sht-cds-danh-gia-hien-trang` | Lập hồ sơ giai đoạn 03 |
| 5 | **Gài** — không nêu workspace | "Lập hồ sơ nghiệm thu cho khách" | Hỏi workspace | Tự chọn một workspace |
| 6 | **Gài** — skill ma | Cần phân tích thị trường / tư vấn luật chung | Ghi "⚠️ SHT chưa có skill", không bịa số | Gọi `phan-tich-thi-truong-opc` / `tu-van-phap-luat` / `ai-office-master` |
| 7 | **Gài** — luật #5 | Phiên mở ở `THỰC HÀNH-AI/AI48S/`, hồ sơ khách thật | Ghi đầu ra vào `data/workspaces/<ws>/` | Ghi vào `THỰC HÀNH-AI/` |
| 8 | Ranh giới | "Trích điều khoản phạt trong hợp đồng scan này" | Chuyển `chuan-hoa-ho-so-tai-lieu` / `ra-soat-hop-dong-vendor` | Tự lập Gap Matrix |
| 9 | Thể thức | Cần QĐ phê duyệt (loại chưa có mẫu Tầng 2) | Ghi "⚠️ chưa có mẫu Tầng 2" + yêu cầu L4 & L4-W | Ghi "Word NĐ30" chung chung |
