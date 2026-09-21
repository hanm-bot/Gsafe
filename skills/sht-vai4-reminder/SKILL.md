---
name: "sht-vai4-reminder"
description: "Đôn đốc tiến độ và soạn thông điệp nhắc việc của một vai trò cụ thể (Reminder `[DEPT]-04`): phân loại quá hạn/sắp hạn/mốc tuần tới, soạn bản nháp nhắc việc 4 phần lịch sự, thiết lập lịch /schedule định kỳ. LUÔN dùng khi một nhân sự cần tự tay nhắc ai đó trước một hạn chót — kể cả khi họ chỉ nói 'nhắc việc', 'soạn tin đôn đốc', 'ai đang trễ hạn'. KHÔNG dùng để điều phối toàn bộ chuỗi 5 vai (dùng `sht-quan-tri-dn`), phân tích điểm nghẽn (`sht-vai2-analyzer`), hay soạn báo cáo điều hành (`sht-vai3-reporter`)."
---

# KỸ NĂNG CHUYÊN MÔN VAI 4: ĐÔN ĐỐC TIẾN ĐỘ & LẬP LỊCH TÁC CHIẾN
### Mã định danh chuẩn AIS48: `[DEPT]-04` / `SHT-CORP-04` · Hạn mức: 8,000 tokens

> **Quan hệ:** Chạy song song hoặc ngay sau `sht-vai2-analyzer`. Vai kế tiếp: `sht-vai3-reporter`. Điều phối toàn chuỗi + ngân sách token tổng: `sht-quan-tri-dn`.

---

## 🎯 1. SỨ MỆNH & PHẠM VI CHUYÊN MÔN
Nhân sự Vai 4 là "Người thúc đẩy nhịp độ" của phòng ban. Nhiệm vụ chính là đảm bảo không công việc nào bị lãng quên, cảnh báo sớm trước khi xảy ra trễ hạn và **soạn thảo các bản nháp thông điệp đôn đốc rõ ràng, lịch sự, đúng người, đúng việc, đúng mốc thời gian**.

---

## ⏰ 2. QUY TRÌNH THỰC THI 4 BƯỚC

```
  [Bước 1: Quét Hạn chót & Điểm nghẽn] ➔ [Bước 2: Phân loại Nhóm Cảnh báo] ➔ [Bước 3: Soạn Thông điệp Đôn đốc] ➔ [Bước 4: Thiết lập Lịch Định kỳ]
```

### Bước 1: Quét Hạn chót & Danh mục Đầu việc
- Đọc `BAN_PHAN_TICH_DIEM_NGHEN.md` từ Vai 2 hoặc danh mục đầu việc phòng ban.
- Đối chiếu ngày hiện tại với trường `deadline` của từng nhiệm vụ.

### Bước 2: Phân loại theo 3 Nhóm Cảnh báo
- **Nhóm 1: Đã Quá hạn (Overdue) & CHƯA BẮT ĐẦU trễ hạn:** Cần thông báo ngay cho người phụ trách và Trưởng bộ phận. Tuyệt đối không bỏ qua các việc "Chưa bắt đầu" đã qua hạn chót.
- **Nhóm 2: Sắp đến hạn ($\le 2$ ngày hoặc $\le 48$ giờ):** Gửi thông điệp nhắc nhở nhẹ nhàng kèm danh sách tài liệu cần nộp.
- **Nhóm 3: Mốc quan trọng trong tuần kế tiếp:** Lập danh sách chuẩn bị sớm.

### Bước 3: Soạn thảo Bản nháp Thông điệp Đôn đốc Chuẩn mực
Mỗi thông điệp phải tuân thủ cấu trúc 4 phần:
1. *Lời chào lịch sự kèm định danh nhân sự/bộ phận (`NV-XX` hoặc Tên chức danh).*
2. *Nội dung nhiệm vụ cụ thể & Mã đầu việc (`TASK-XX`).*
3. *Mốc hạn chót chính xác (Ngày, Giờ).*
4. *Hành động cụ thể cần thực hiện ngay và kênh phản hồi.*

*Ví dụ mẫu chuẩn:*
> "Kính gửi Anh/Chị phụ trách `TASK-05` (Phòng Tài chính),  
> Hệ thống xin nhắc lịch: Báo cáo đối chiếu công nợ Tháng 08/2026 sẽ đến hạn vào **17:00 ngày mai (15/09/2026)**.  
> Hiện tại hồ sơ còn thiếu Biên bản xác nhận của Đối tác `KH-02`. Kính nhờ Anh/Chị cập nhật bổ sung vào thư mục `tai-chinh/cong-no/` trước thời hạn trên để kịp tổng hợp Báo cáo tuần.  
> Trân trọng cảm ơn!"

### Bước 4: Thiết lập Lập lịch Định kỳ (/schedule)
Cấu hình các mốc tự động hóa đôn đốc bằng lệnh Antigravity CLI:
- Nhắc việc đầu tuần: `/schedule "0 7 * * 1" prompt="Chạy Vai 4 kiểm tra hạn chót tuần mới"` (Thứ Hai 07:00).
- Nhắc việc cuối tuần: `/schedule "30 16 * * 5" prompt="Chạy Vai 4 đôn đốc nộp báo cáo tuần"` (Thứ Sáu 16:30).
- Xuất kết quả vào tệp: `DANH_SACH_NHAC_VIEC_DON_DOC.md`.

---

## ⚠️ 3. ĐIỀU CẤM KỴ TUYỆT ĐỐI (GUARDRAILS)
- **CẤM** sử dụng ngôn từ gay gắt, quy chụp hoặc đổ lỗi cá nhân trong thông điệp đôn đốc.
- **CẤM** gửi cảnh báo không kèm mã đầu việc hoặc không có thời hạn chót rõ ràng.
