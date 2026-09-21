---
name: "sht-vai1-harvester"
description: "Bóc tách & làm sạch nguyên liệu nghiệp vụ đầu vào của một vai trò cụ thể (Harvester `[DEPT]-01`): tiếp nhận file, gọi Cổng I/O, thực thi Masking Vùng Đỏ (CCCD/STK/lương/họ tên) thành mã ẩn danh. LUÔN dùng khi một nhân sự cần tự tay làm sạch dữ liệu thô trước khi giao cho bước phân tích — kể cả khi họ chỉ nói 'làm sạch dữ liệu', 'ẩn danh hồ sơ', 'mask PII'. KHÔNG dùng để điều phối toàn bộ chuỗi 5 vai cho cả đội (dùng `sht-quan-tri-dn`), phân tích điểm nghẽn (`sht-vai2-analyzer`), hay soạn báo cáo (`sht-vai3-reporter`)."
---

# KỸ NĂNG CHUYÊN MÔN VAI 1: THU THẬP, LÀM SẠCH & KIỂM SOÁT CỔNG I/O
### Mã định danh chuẩn AIS48: `[DEPT]-01` / `SHT-CORP-01` · Hạn mức: 7,000 tokens

> **Quan hệ:** Vai kế tiếp trong chuỗi: `sht-vai2-analyzer`. Điều phối toàn chuỗi 5 vai + ngân sách token tổng + Sổ Cái HITL: `sht-quan-tri-dn`. Khi cần dựng cả đội cho một phòng ban mới (không chỉ vai này), dùng `sht-quan-tri-dn` §7.

---

## 🎯 1. SỨ MỆNH & PHẠM VI CHUYÊN MÔN
Nhân sự Vai 1 là "Người gác cổng nguyên liệu" của phòng ban. Nhiệm vụ tối thượng là bảo đảm mọi dữ liệu trước khi nạp vào chuỗi AI đều phải **sạch cấu trúc, đầy đủ tính toàn vẹn và che chắn 100% dữ liệu nhạy cảm Vùng Đỏ**.

---

## 🛡️ 2. QUY TRÌNH THỰC THI 4 BƯỚC

```
  [Bước 1: Tiếp nhận Tệp nguồn] ➔ [Bước 2: Quét Cổng I/O Tự động] ➔ [Bước 3: Thực thi Masking Vùng Đỏ] ➔ [Bước 4: Xuất bản Dữ liệu Sạch]
```

### Bước 1: Tiếp nhận Tệp nguồn Nghiệp vụ
- Quét các tệp đầu vào trong Workspace phòng ban (`ke-hoach/`, `bao-cao-don-vi/`, `chung-tu/`, `tasks.csv`...).
- Xác định định dạng tệp: `.xlsx`, `.csv`, `.docx`, `.pdf`, `.json`.

### Bước 2: Thẩm định Cổng I/O Tự động (Harness Gate)
- Kích hoạt module Cổng I/O để kiểm tra tính toàn vẹn và quét mã độc/lỗi cấu trúc:
  ```bash
  python .agents/scripts/sht_io_gate.py --scan "<duong_dan_tep_nguon>"
  ```
  Exit 0 (PASS) → cấp nhãn `[IO_GATE_VERIFIED:<hash>]`, sang Bước 3. Exit 2 (BLOCKED) → dừng ngay, báo Data Owner.
  **Cơ chế đầy đủ (2 tầng, kể cả hook cấp user chặn mọi agent ghi PII) và bài học vận hành: xem `sht-quan-tri-dn` §0 — không lặp lại ở đây.**

### Bước 3: Thực thi Kỹ thuật Masking Vùng Đỏ (Traffic Light Security)
Áp dụng bộ mẫu regex chuẩn hóa để ẩn danh hóa dữ liệu trước khi lưu:
1. **CCCD/CMND (9-12 số):** Thay thế bằng mã định danh cấu trúc `[PII_CCCD_NV-XX]`.
2. **Số Tài khoản Ngân hàng (8-19 số):** Thay thế bằng `[STK_AN_DANH_NH-XX]`.
3. **Bảng lương / Thu nhập cá nhân:** Tách riêng lưu máy cục bộ, thay bằng `[MUC_LUONG_KHUNG_BẬC_X]`.
4. **Họ tên cá nhân:** Thay thế bằng mã thống nhất:
   - Nhân sự nội bộ: `NV-01`, `NV-02`, ...
   - Khách hàng: `KH-01`, `KH-02`, ...
   - Nhà cung cấp: `NCC-01`, `NCC-02`, ...
   - Ứng viên tuyển dụng: `UV-01`, `UV-02`, ...

### Bước 4: Xuất bản Dữ liệu Làm sạch
- Xuất kết quả vào tệp: `DU_LIEU_LAM_SACH.md` (hoặc `DU_LIEU_QUAN_TRI_SACH.md`).
- Bắt buộc đính kèm:
  * Bảng đối chiếu mã ẩn danh (chỉ lưu mã và phòng ban, không lưu họ tên thật).
  * Mã băm SHA-256 của tệp nguồn.
  * Nhãn xác thực của Cổng I/O.

---

## ⚠️ 3. ĐIỀU CẤM KỴ TUYỆT ĐỐI (GUARDRAILS)
- **CẤM** ghi tệp chứa dữ liệu Vùng Đỏ thô. Hook PreToolUse (`sht_io_gate.py --hook`) sẽ chặn cứng thao tác ghi tệp vi phạm.
- **CẤM** tự ý suy diễn hoặc chỉnh sửa số liệu nghiệp vụ gốc trong quá trình làm sạch.
