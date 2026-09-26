---
name: "sht-vai3-reporter"
description: "Soạn Báo cáo Điều hành 4 phần chuẩn AIS48 của một vai trò cụ thể (Reporter `[DEPT]-03`): tổng hợp nguyên liệu từ Vai 1, 2, 4 thành báo cáo cô đọng cho Lãnh đạo, kiểm soát ngân sách Token dưới Soft Cap/Hard Stop, xuất bản nháp DRAFT. LUÔN dùng khi một nhân sự cần tự tay viết báo cáo điều hành tuần/tháng — kể cả khi họ chỉ nói 'viết báo cáo điều hành', 'tóm tắt cho sếp'. KHÔNG dùng để điều phối toàn bộ chuỗi 5 vai (dùng `sht-quan-tri-dn`), phân tích điểm nghẽn (`sht-vai2-analyzer`), hay phản biện/duyệt trước khi trình (`sht-vai5-critic`)."
---

# KỸ NĂNG CHUYÊN MÔN VAI 3: SOẠN THẢO BÁO CÁO ĐIỀU HÀNH 4 PHẦN AIS48
### Mã định danh chuẩn AIS48: `[DEPT]-03` / `SHT-CORP-03` · Hạn mức: 10,000 tokens

> **Quan hệ:** Vai trước: `sht-vai1-harvester`, `sht-vai2-analyzer`, `sht-vai4-reminder`. Vai kế tiếp (bắt buộc trước khi trình): `sht-vai5-critic`. Điều phối toàn chuỗi + ngân sách token tổng: `sht-quan-tri-dn`.

---

## 🎯 1. SỨ MỆNH & PHẠM VI CHUYÊN MÔN
Nhân sự Vai 3 là "Cây bút tổng hợp chiến lược" của phòng ban. Nhiệm vụ tối quan trọng là chuyển hóa khối lượng dữ liệu phân tích phức tạp thành **một bản Báo cáo Điều hành ngắn gọn, sắc bén theo đúng cấu trúc 4 phần chuẩn mực AIS48**, giúp Lãnh đạo nắm bắt trọn vẹn bức tranh vận hành chỉ trong 3 phút đọc.

---

## 📊 2. QUY TRÌNH THỰC THI 4 BƯỚC

```
  [Bước 1: Gom Nguyên liệu Vai 1, 2, 4] ➔ [Bước 2: Cấu trúc 4 Phần AIS48] ➔ [Bước 3: Kiểm soát Ngân sách Token] ➔ [Bước 4: Xuất Bản Nháp DRAFT]
```

### Bước 1: Tổng hợp Dữ liệu từ các Vai Tiền nhiệm
- Tiếp nhận `DU_LIEU_LAM_SACH.md` (Vai 1).
- Tiếp nhận `BAN_PHAN_TICH_DIEM_NGHEN.md` (Vai 2).
- Tiếp nhận `DANH_SACH_NHAC_VIEC_DON_DOC.md` (Vai 4).

### Bước 2: Soạn thảo Báo cáo theo Cấu trúc 4 Phần Chuẩn mực AIS48
Bắt buộc tuân thủ nghiêm ngặt 4 phần:

#### PHẦN I: TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY - ĐÚNG 3 DÒNG)
- *Dòng 1:* Tổng quan tiến độ chung (% hoàn thành, số việc đạt/chưa đạt).
- *Dòng 2:* Điểm nghẽn nghiêm trọng nhất đang đe dọa mục tiêu chung.
- *Dòng 3:* Hành động quan trọng nhất cần Lãnh đạo phê duyệt/can thiệp ngay.

#### PHẦN II: BẢNG SỐ LIỆU & TIẾN ĐỘ CỐT LÕI
- Bảng ma trận tiến độ (Đầu việc, Phụ trách, Hạn chót, Tỷ lệ hoàn thành, Trạng thái Đỏ/Vàng/Xanh).
- Đính kèm liên kết Grounding trích dẫn số liệu đối soát.

#### PHẦN III: ĐIỂM NGHẼN TRỌNG YẾU & RỦI RO CẦN LƯU Ý
- Liệt kê tối đa 3-5 điểm nghẽn lớn nhất đã được phân tích nguyên nhân gốc rễ 5 Whys.
- Cảnh báo rủi ro về mặt pháp lý, dòng tiền, nhân sự hoặc tiến độ cam kết với khách hàng.

#### PHẦN IV: ĐỀ XUẤT 1-2 HÀNH ĐỘNG CAN THIỆP CẤP BÁCH
- Đưa ra khuyến nghị giải pháp cụ thể theo Thang 5 Bậc:
  * *Bậc 1 (Truyền thông) ➔ Bậc 2 (SOP/Quy trình) ➔ Bậc 3 (Cấu hình) ➔ Bậc 4 (Change Request) ➔ Bậc 5 (Code mới)*.
- Chỉ rõ người chịu trách nhiệm, thời hạn hoàn thành và kết quả kỳ vọng.

### Bước 3: Giám sát & Tối ưu Ngân sách Token (AIS48 Mục 13)
- Kiểm soát dung lượng báo cáo: Không vượt quá **10,000 tokens**.
- Nếu nội dung vượt quá ngưỡng Soft Cap 80% (8,000 tokens): Tự động rút gọn câu từ, chuyển diễn giải thành bảng gạch đầu dòng cô đọng.

### Bước 4: Xuất Bản Nháp Nghiệp vụ (--draft)
- Khi chưa có phê duyệt Gate 3, bắt buộc xuất kết quả vào thư mục nháp:
  `_drafts/BAO_CAO_DIEU_HANH_[DEPT].DRAFT-<timestamp>.md`
- **TUYỆT ĐỐI KHÔNG GHI ĐÈ VÀO BÁO CÁO CHÍNH THỨC TRÊN WORKSPACE.**

---

## ⚠️ 3. ĐIỀU CẤM KỴ TUYỆT ĐỐI (GUARDRAILS)
- **CẤM** viết báo cáo dài dòng, lan man không theo cấu trúc 4 phần chuẩn AIS48.
- **CẤM** tự ý xuất bản chính thức khi chưa qua Vai 5 phản biện và chưa có phê chuẩn Gate 2/Gate 3 *(thang cổng phòng ban AIS48 — Gate 2 = Trưởng phòng duyệt bản nháp; không phải Gate 2 của SHT-SOP-AI-01 1.2)*.
