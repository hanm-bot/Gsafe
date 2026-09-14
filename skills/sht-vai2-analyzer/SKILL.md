---
name: "sht-vai2-analyzer"
description: "Phân tích điểm nghẽn vận hành của một vai trò cụ thể (Analyzer `[DEPT]-02`): so khớp tiến độ thực tế với kế hoạch cơ sở, phân loại 3 mức đèn giao thông, truy vết nguyên nhân gốc rễ 5 Whys, trích dẫn tọa độ Second Brain Grounding. LUÔN dùng khi một nhân sự cần tự tay chẩn đoán vì sao một chỉ tiêu/đầu việc bị lệch — kể cả khi họ chỉ nói 'vì sao trễ', 'phân tích nguyên nhân', '5 Whys'. KHÔNG dùng để điều phối toàn bộ chuỗi 5 vai (dùng `sht-quan-tri-dn`), làm sạch dữ liệu thô (`sht-vai1-harvester`), hay soạn thông điệp đôn đốc (`sht-vai3-dispatcher`)."
---

# KỸ NĂNG CHUYÊN MÔN VAI 2: PHÂN TÍCH ĐIỂM NGHẼN & GROUNDING ĐỐI SOÁT
### Mã định danh chuẩn AIS48: `[DEPT]-02` / `SHT-CORP-02` · Hạn mức: 12,000 tokens

> **Quan hệ:** Vai trước: `sht-vai1-harvester`. Vai kế tiếp: `sht-vai3-dispatcher` (chạy song song được) và `sht-vai4-reporter`. Điều phối toàn chuỗi + ngân sách token tổng: `sht-quan-tri-dn`.

---

## 🎯 1. SỨ MỆNH & PHẠM VI CHUYÊN MÔN
Nhân sự Vai 2 là "Bộ não chẩn đoán" của phòng ban. Nhiệm vụ cốt lõi là so sánh dữ liệu thực tế với kế hoạch/chỉ tiêu, vạch rõ các điểm nghẽn vận hành, truy tìm nguyên nhân gốc rễ theo phương pháp 5 Whys và bảo đảm **100% nhận định đều có tọa độ bằng chứng đối soát (Zero Hallucination)**.

---

## 🔬 2. QUY TRÌNH THỰC THI 4 BƯỚC

```
  [Bước 1: Tiếp nhận Dữ liệu Sạch] ➔ [Bước 2: So khớp Tiến độ & Phân loại] ➔ [Bước 3: Truy vết 5 Whys] ➔ [Bước 4: Trích dẫn Grounding]
```

### Bước 1: Tiếp nhận Dữ liệu Sạch từ Vai 1
- Đọc tệp `DU_LIEU_LAM_SACH.md`. Kiểm tra sự hiện diện của nhãn xác thực `[IO_GATE_VERIFIED]`.
- Nạp kế hoạch cơ sở (Baseline / KPI targets) của phòng ban.

### Bước 2: So khớp Tiến độ & Phân loại 3 Mức độ Rủi ro
Tính toán tỷ lệ hoàn thành và phân loại các đầu việc/chỉ tiêu theo chuẩn đèn giao thông:
- 🔴 **MỨC ĐỎ (Nghiêm trọng / Trễ hạn):** Công việc đã quá hạn chót hoặc chỉ tiêu hụt > 20% so với kế hoạch cơ sở.
- 🟡 **MỨC VÀNG (Cảnh báo / Nguy cơ trễ):** Công việc còn $\le 2$ ngày đến hạn hoặc chỉ tiêu đạt từ 80% - 95%.
- 🟢 **MỨC XANH (Bình thường / Đạt chuẩn):** Đúng tiến độ, số liệu khớp hoàn toàn.

### Bước 3: Truy vết Nguyên nhân Gốc rễ (5 Whys Root Cause Analysis)
Với mỗi điểm nghẽn Mức Đỏ, thực hiện truy vấn 5 câu hỏi "Tại sao":
1. *Tại sao việc này bị trễ hạn / sai lệch?*
2. *Tại sao nguyên nhân đó không được phát hiện sớm?*
3. *Tại sao quy trình phối hợp chưa cảnh báo kịp thời?*
4. *Tại sao nhân sự phụ trách gặp khó khăn?*
5. *Nguyên nhân gốc rễ ở tầng quy trình/hạ tầng là gì?*

### Bước 4: Trích xuất Tọa độ Đối soát (Second Brain Grounding)
Kích hoạt Grounding Engine để liên kết mọi kết luận với quy chuẩn hoặc tài liệu nguồn:
```bash
python .agents/scripts/sht_grounding_engine.py --query "<tu_khoa_nghiep_vu>"
```
- Bắt buộc mọi khẳng định quan trọng phải kèm bảng Grounding Snippet:
  | Mã Đầu việc | Nhận định Phân tích | Tệp Nguồn Đối soát | Tiêu đề Mục / Dòng | Trích đoạn Minh chứng |
  |:---:|---|---|:---:|---|
  | `TASK-XX` | Trễ tiến độ 05 ngày | `ke-hoach/2026_Ke_hoach.xlsx` | Sheet 1, Dòng 42 | `"Hạn chót: 05/09/2026; Trạng thái: Đang làm"` |

- Xuất kết quả vào tệp: `BAN_PHAN_TICH_DIEM_NGHEN.md`.

---

## ⚠️ 3. ĐIỀU CẤM KỴ TUYỆT ĐỐI (GUARDRAILS)
- **CẤM** đưa ra kết luận cảm tính không có số liệu chứng minh (Zero Hallucination).
- **CẤM** bỏ qua các đầu việc Mức Đỏ mà không truy vết nguyên nhân 5 Whys.
