---
name: "sht-quan-tri-dn"
description: "Điều phối Đội 5 Agent Quản trị Doanh nghiệp chuẩn AIS48 (5 vai: Harvester/Analyzer/Reminder/Reporter/Critic), cả quy mô nội bộ lẫn nhân rộng 9 phòng ban SHT qua Blueprint + Workshop B5, bảo vệ bởi Cổng I/O 2 tầng (script + hook cấp user chặn PII) và Sổ Cái HITL SHA-256. LUÔN dùng khi vận hành quy trình quản trị tuần, giám sát đầu việc liên phòng ban, kiểm soát tiến độ 11 giai đoạn CĐS, chạy /goal /teamwork /schedule, thẩm định QA Lớp 2 một kế hoạch/walkthrough do Anti soạn (đối chiếu thực nghiệm, không tin báo cáo tự chấm), hoặc dựng Đội 5 Agent cho phòng ban mới — kể cả khi chỉ nói 'thẩm định QA', 'audit chéo', 'kích hoạt workshop phòng ban'. KHÔNG dùng khi chỉ xác thực báo cáo doanh số/CRM (dùng sht-xacthuc-baocao-hoatdong), xuất PDF kiểm chứng in ấn (dùng sht-nen-tang-kiem-chung), khi một nhân sự chỉ cần tự làm đúng một vai riêng lẻ (dùng sht-vai1..5), hoặc khi vận hành cổng quyết định JEV / chạy ca thật JEV (dùng sht-jev-cong-quyet-dinh)."
---

# KỸ NĂNG: ĐỘI 5 AGENT QUẢN TRỊ DOANH NGHIỆP TRÊN ANTIGRAVITY (SHT-AIS48)

Kỹ năng này đóng gói phương pháp luận AIS48 và quy chuẩn tác chiến SHT để tự động hóa toàn diện chu trình quản trị vận hành nội bộ hoặc dự án B2B — áp dụng cho cả một đội nội bộ lẫn nhân rộng ra 9 phòng ban.

## 0. CỔNG I/O 2 TẦNG (BẢO VỆ VÙNG ĐỎ TOÀN HỆ THỐNG)

Nguyên liệu nạp vào Vai 1 (Harvester) — và mọi thao tác ghi file của bất kỳ agent nào trong đội — đều đi qua Cổng I/O trước khi chạm dữ liệu Vùng Đỏ:

- **Tầng 1 — Script độc lập** `.agents/scripts/sht_io_gate.py`: quét cấu trúc + regex Vùng Đỏ (CCCD/CMND, STK ngân hàng — yêu cầu có từ khóa ngữ cảnh đi kèm số, ví dụ "cccd:", "stk:", để tránh báo động giả với mã đầu việc/hợp đồng). `--scan <file>` → Exit 0 (PASS) / Exit 2 (BLOCKED). Tích hợp trực tiếp vào engine qua lời gọi `verify_input_file()` trước Chặng 1.
- **Tầng 2 — Hook cấp user** đăng ký tại `~/.claude/settings.json` (khối `matcher: "Write|Edit|NotebookEdit|Bash"` dùng chung với các hook cưỡng chế khác), gọi `sht_io_gate.py --hook`, nhận payload PreToolUse qua stdin, trả `{"hookSpecificOutput": {"permissionDecision": "deny", ...}}` khi phát hiện PII thô chưa Masking trong bất kỳ tác vụ ghi file nào — không cần cài đặt riêng cho từng đội phòng ban.
- **Bài học xương máu (14/09/2026):** danh sách loại trừ ở Tầng 2 tuyệt đối KHÔNG được dùng mẫu con chung chung kiểu `"/test"` — nó vô hiệu hóa bảo vệ cho MỌI file có chữ đó trong tên, kể cả file nghiệp vụ thật (`UAT_test.csv`, `KPI_test_nghiem_thu.md`). Chỉ loại trừ đúng thư mục scratch/self-test cố định đã biết (`/_drafts/`, `/scratch/`, `/_io_gate_selftest/`...). Mỗi lần sửa danh sách loại trừ, bắt buộc thử lại ít nhất 1 ca đối kháng (tên file thật có chứa từ khóa dễ gây hiểu nhầm) trước khi coi là an toàn.

## 1. NGUYÊN TẮC VẬN HÀNH 5 VAI TRÒ

Khi kích hoạt kỹ năng này, hệ thống vận hành theo chuỗi 5 vai chuyên biệt với điểm bàn giao chuẩn hóa. Đây là mô tả **ở tầm điều phối cả đội** — khi một nhân sự cụ thể chỉ cần tự tay thực hiện đúng một vai (không điều phối cả chuỗi), dùng skill riêng của vai đó để có đầy đủ quy trình thực thi từng bước: `sht-vai1-harvester`, `sht-vai2-analyzer`, `sht-vai4-reminder`, `sht-vai3-reporter`, `sht-vai5-critic`.

1. **Vai 1 · Thu Thập (`SHT-CORP-HARVESTER`):**
   - Đọc dữ liệu từ workspace mục tiêu (CSV, Excel, Task tracker), sau khi đã qua Cổng I/O (Mục 0).
   - Tự động quét và Masking dữ liệu Vùng Đỏ (PII nhân sự, thông tin lương).
   - Giao ra: `DU_LIEU_QUAN_TRI_SACH.md`.
2. **Vai 2 · Phân Tích (`SHT-CORP-ANALYST`):**
   - Tiếp nhận `DU_LIEU_QUAN_TRI_SACH.md`.
   - Tính toán % việc trễ hạn, so sánh xu hướng tuần, phát hiện 3 điểm rủi ro.
   - Giao ra: `BAN_PHAN_TICH_VAN_HANH.md` (mỗi ý 1 dòng có số kèm theo, đánh dấu `[CẢNH BÁO]`).
3. **Vai 4 · Nhắc Việc (`SHT-CORP-REMINDER`):**
   - Chạy song song với Vai 2.
   - Lọc đầu việc trễ hạn hoặc sắp trễ ($\le 2$ ngày).
   - Giao ra: `DANH_SACH_NHAC_VIEC.md` kèm câu nhắc soạn sẵn lịch sự.
4. **Vai 3 · Báo Cáo (`SHT-CORP-REPORTER`):**
   - Nhận đầu vào từ `BAN_PHAN_TICH_VAN_HANH.md`.
   - Biên soạn Báo cáo điều hành tuần theo cấu trúc 4 phần chuẩn AIS48:
     * (1) Tóm tắt 3 dòng cho Lãnh đạo
     * (2) Bảng số liệu cốt lõi
     * (3) Rủi ro & Điểm cần lưu ý
     * (4) Đề xuất 1–2 hành động ưu tiên
   - Giao ra: `BAN_NHAP_BAO_CAO_DIEU_HANH.md`.
5. **Vai 5 · Phản Biện (`SHT-CORP-AUDITOR` - Độc Lập):**
   - Nhận `BAN_NHAP_BAO_CAO_DIEU_HANH.md` đối chiếu chéo với `DU_LIEU_QUAN_TRI_SACH.md`.
   - Kế thừa logic đối chiếu từ `sht-xacthuc-baocao-hoatdong` và `sht-nen-tang-kiem-chung`.
   - Kiểm tra: Mọi con số có khớp dữ liệu gốc không? Có suy diễn không có số đỡ lưng không?
   - Khi vai này thẩm định một kế hoạch/báo cáo **do Anti soạn** (không phải dữ liệu quản trị nội bộ), áp dụng thêm quy tắc đối chiếu thực nghiệm ở Mục 6.
   - Giao ra: `CHECKLIST_DUYET_PHAN_BIEN.md` (✓ Đạt / ✗ Cần sửa).
   - **Chặn cứng:** Nếu có ✗, kiên quyết từ chối phát hành và gửi trả Vai 3 sửa.

---

## 2. CHỐT CHẶN HITL & GHI LOG SỔ CÁI

Chỉ khi Vai 5 đạt `✓ 100%`, báo cáo mới được trình lên Mr. Hà (Lãnh đạo).
Khi Mr. Hà phê duyệt Gate 3, bắt buộc kích hoạt lệnh ghi log qua subprocess:

```bash
python .agents/scripts/ghi-log-hitl.py --append \
    --channel "Antigravity IDE" \
    --session "<session_id>" \
    --actor "hanm@shtech.com.vn" \
    --gate "Gate 3" \
    --command "Phê duyệt Báo cáo điều hành" \
    --target "<duong_dan_bao_cao>"
```

Sau khi ghi, chạy `python .agents/scripts/ghi-log-hitl.py --verify` để xác thực toàn vẹn chuỗi mã băm SHA-256.

---

## 3. LỆNH ĐIỀU PHỐI NHANH QUA ANTIGRAVITY

- Khởi động mục tiêu: `/goal Chạy toàn bộ Đội 5 Agent Quản trị SHT cho tuần này`
- Chạy song song: `/teamwork Chạy đồng thời Vai 2 Phân tích và Vai 4 Nhắc việc`
- Lập lịch định kỳ: `/schedule Mỗi Thứ Hai 07:00 chạy Vai 4 Nhắc việc (task-472); Mỗi Thứ Sáu 16:30 chạy toàn chuỗi 5 Agent (task-344)`

---

## 4. THAM SỐ DÒNG LỆNH CỦA ĐỘNG CƠ ĐIỀU PHỐI (`sht_enterprise_squad_engine.py`)

Động cơ thực thi tại `.agents/scripts/sht_enterprise_squad_engine.py` hỗ trợ các tham số chuẩn mực:

- `--run-all`: Kích hoạt toàn bộ chuỗi 5 vai trò theo quy trình chuẩn AIS48.
- `--teamwork`: Chạy song song Chặng 2 (Vai 2 Phân tích) và Chặng 3 (Vai 4 Nhắc việc) qua `ThreadPoolExecutor`.
- `--step {1,2,3,4,5}`: Thực thi đơn lẻ một chặng tác chiến (1: Thu thập, 2: Phân tích, 3: Nhắc việc, 4: Báo cáo, 5: Phản biện).
- `--draft`: Kích hoạt chế độ sinh bản nháp nghiệp vụ DRAFT, xuất toàn bộ 5 tệp kết quả vào thư mục `_drafts/<TEN_FILE>.DRAFT-<timestamp>.md`, **tuyệt đối không ghi đè 5 tệp báo cáo chính thức**.
- `--tasks-file <tên_file>`: Chỉ định tệp danh mục đầu việc tùy chỉnh (ví dụ: `TEST_VIETNAMESE_NAMES_PII.csv`).
  > ⚠️ **CẢNH BÁO AN TOÀN BẮT BUỘC:** Khi sử dụng `--tasks-file` với tệp khác `DANH_MUC_DAU_VIEC_SHT.csv` trên môi trường sản xuất, hệ thống sẽ **tự động cưỡng chế chế độ `--draft`** để bảo vệ 5 báo cáo sản xuất chính thức. Nếu cố tình muốn ghi đè thật, bắt buộc phải truyền thêm cờ `--force-overwrite-production`.
- `--schedule-mode`: Chế độ chạy ngầm tự động theo lịch cron của Antigravity (Thứ Sáu 16:30).
- `--triggered-by <manual|cron:task-472|cron:task-344>`: Ghi nhận nguồn kích hoạt phiên chạy vào JSON trạng thái, phục vụ kiểm toán độc lập việc daemon có thực sự tự chạy hay không.
- `--test-hitl`: Chế độ DRY-RUN thử nghiệm quy trình HITL (chỉ in câu lệnh mẫu dự kiến ra màn hình, **tuyệt đối không ghi Sổ Cái thật**).
  > ⚠️ **NGUYÊN TẮC BẤT DI BẤT DỊCH VỀ PHÊ DUYỆT GATE 3:** Mọi phê duyệt Gate 3 phải do chính Mr. Hà gõ trực tiếp với Claude hoặc Antigravity trong phiên thật, không qua cờ CLI tự động của engine.
- `--status`: In bảng trạng thái pipeline, tình trạng lương token (`current_run` phiên hiện hành tách bạch khỏi `last_approved_record` lịch sử phê duyệt quá khứ) và thông tin phê duyệt Gate 3.

---

## 5. NGÂN SÁCH TOKEN CHUẨN 5 VAI (HARD STOP)

| Vai | Hard Stop |
|---|---:|
| Vai 1 · Thu thập | 7.000 |
| Vai 2 · Phân tích | 12.000 |
| Vai 3 · Báo cáo | 10.000 |
| Vai 4 · Nhắc việc | 8.000 |
| Vai 5 · Phản biện | 15.000 |
| **Tổng đội** | **52.000** |

Soft Cap = 80% tổng (41.600 token): kích hoạt chế độ tóm tắt ngắn. Hard Stop 100%: dừng khẩn cấp, yêu cầu HITL can thiệp mở rộng.

---

## 6. QUY TẮC THẨM ĐỊNH QA LỚP 2 (ĐỐI CHIẾU THỰC NGHIỆM, KHÔNG TIN BÁO CÁO TỰ CHẤM)

Áp dụng khi Vai 5 (Phản biện) hoặc Claude QA Lead thẩm định một **kế hoạch/walkthrough do Anti soạn** (khác với đối chiếu số liệu quản trị nội bộ ở Mục 1):

1. **Không đọc mô tả rồi tin — tự chạy lại.** Chính lệnh mà báo cáo dẫn ra (`--test`, `--scan`, mô phỏng payload hook qua stdin...), đọc trực tiếp code/file được trích dẫn, `diff` các bản sao được cho là đồng bộ. Một báo cáo có link file/lệnh cụ thể không đồng nghĩa nó đã được chạy thật.
2. **Luôn thêm ít nhất một ca đối kháng tự nghĩ ra** khi kiểm một cơ chế loại trừ/bảo vệ — không chỉ lặp lại đúng ca "vui vẻ" mà báo cáo tự chạy. Đây là cách duy nhất phát hiện lỗ hổng dạng "chỉ né đúng ca bị bắt quả tang".
3. **Băm SHA-256 hợp lệ trong Sổ Cái chỉ chứng minh bản ghi không bị sửa sau khi ghi — KHÔNG chứng minh hành động phê duyệt là thật.** Bất kỳ bản ghi HITL nào có `actor` lệch định dạng chuẩn (`hanm@shtech.com.vn`) hoặc `command_text` đọc như agent tự thuật lại hành động của chính mình (thay vì lời một người ra lệnh), đều phải dừng lại dùng AskUserQuestion hỏi trực tiếp người có thẩm quyền trước khi dùng bản ghi đó làm căn cứ ban hành — không tự kết luận theo bất kỳ chiều nào dù chuỗi băm PASS 100%.
4. **Ghi phiếu kiểm toán theo 5 mục cố định:** Kết luận ngắn / Phát hiện (kèm mức độ 🔴 nghiêm trọng · 🟡 cần sửa · ℹ️ nhẹ) / Phần đã tự kiểm và xác nhận đúng / Đề xuất Audit chéo / Checklist hành động cho Anti — không viết tự do ngoài khuôn này.
5. **Chỉ trả kế hoạch về sửa khi phát hiện thật sự chặn** (overclaim phạm vi khiến người đọc hiểu sai mức hoàn thành, lỗ hổng bảo mật tái hiện được, số liệu bịa đặt hoặc suy luận vượt quá bằng chứng đưa ra). Phát hiện mức nhẹ (lệch 1 dòng đếm, mô tả matcher sai câu chữ, timestamp lệch vài giây) ghi nhận nhưng không chặn tiến độ.
6. **Kiểm mtime trước khi QA.** "Đã nộp" không có nghĩa là file đã đổi — phiên 24–25/09/2026 gặp 4 lần. So giờ sửa report/code/sổ với lần QA trước; không đổi thì báo lại, không QA lại bản cũ.
7. **Chạy lại trên bản sao cô lập, đo kho thật bằng md5 trước/sau.** Script phản biện của QA phải từ chối chạy khi chưa trỏ vào bản sao; bên thực thi sửa script QA thì `diff` với bản gốc trước khi tin kết quả.
8. **Tối đa 2 vòng sửa, không dời cột gôn.** Phát hiện mới ngoài phạm vi phiếu trước → tiền điều kiện bước sau hoặc RFC cho Mr. Hà, không trả vòng 3. Lỗi do spec của QA viết lỏng → nhận lỗi, sửa nhỏ không tính vòng.
9. **Không tự chấm sản phẩm của chính mình.** Claude soạn thì Anti kiểm, Claude chỉ đối chiếu report với thực tế.
10. **Rà rác sau mỗi lần nộp:** thư mục `scratch/` trong kho, file trích văn bản hồ sơ nguồn, report đặt sai thư mục, bản sao code nằm trong kho.

Trình tự QA riêng cho cổng quyết định JEV: `sht-jev-cong-quyet-dinh` → `references/phan-vai-jev.md` §C.

---

## 7. NHÂN RỘNG 9 PHÒNG BAN (SCALE-OUT)

Khi dựng Đội 5 Agent cho một phòng ban cụ thể (Giai đoạn 2 chuẩn AIS48), dùng đúng bộ tài liệu chuẩn đã ban hành — không viết lại nội dung, chỉ trỏ tới:

- **Kiến trúc mẫu:** `Playbooks-Thuc-Chien/01_Cau-truc-Workspace-9-Phong-ban/BLUEPRINT_DOI_5_AGENT_PHONG_BAN.md`
- **Biểu mẫu tác nghiệp Workshop 5 bước (B5):** `Playbooks-Thuc-Chien/01_Cau-truc-Workspace-9-Phong-ban/BIEU_MAU_WORKSHOP_5_BUOC_B5_9_PHONG_BAN.md`
- **Theo dõi tiến độ:** `Playbooks-Thuc-Chien/01_Cau-truc-Workspace-9-Phong-ban/BANG_THEO_DOI_TIEN_DO_WORKSHOP_9_PHONG_BAN.md` và các hồ sơ đã điền trong `workshops/`

Nguyên tắc phân cấp giữ nguyên cho mọi phòng ban: **Gate 1 và Gate 2** (kế hoạch, nghiệm thu nội bộ) do **Trưởng phòng ban** phê duyệt; **Gate 3** (xuất bản chính thức/ra ngoài) luôn giữ riêng cho **Mr. Hà**, ghi Sổ Cái SHA-256 theo đúng Mục 2. Mỗi đội phòng ban dùng chung một Cổng I/O (Mục 0) — không cài đặt lại logic Masking riêng lẻ.

> **Đừng lẫn thang cổng.** Gate 1/2/3 ở mục này là thang duyệt **của phòng ban AIS48** (Trưởng phòng / Mr. Hà). Nó khác Gate của `SHT-SOP-AI-01` 1.2 (từ 26/09/2026, Gate 2 của SOP chỉ còn nghĩa đổi phạm vi / chọn phương án RFC giữa Claude–Anti–Mr. Hà). Ghi Sổ Cái cổng phòng ban bằng nhãn **`PB Gate 1/2/3` + `--phong-ban <MÃ>`** (SOP-AI-01 1.3 §6.10, có hiệu lực 26/09/2026 `HITL-20260926-017`); lệnh mẫu và luật `actor` ở `sht-vai5-critic` Bước 4. Workspace khách (Metro…) **không** phải phòng ban.
