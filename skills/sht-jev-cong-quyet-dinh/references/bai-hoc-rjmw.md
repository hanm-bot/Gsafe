# Tổng hợp phiên SHT-RJMW-01 (24–25/09/2026) — tư duy · đã làm · chưa làm

> DA-DOI-CHIEU-NGUON: trạng thái và con số trong file này truy về `plans/20260924-chuoi-quyet-dinh-rjmw/plan.md`, các phiếu `docs/audit/2026-09-2[45]_QA-audit-SHT-RJMW-01-*.md`, `docs/audit/2026-09-24_GATE3-SHT-RJMW-01.md` và Sổ Cái `docs/audit/HITL_APPROVAL_LEDGER.jsonl` tại thời điểm 25/09/2026 ~01:15. Là **ảnh chụp** — đối chiếu lại trước khi trích.

## 1. Tư duy cốt lõi

1. **Thẩm định trước, dựng sau.** Sơ đồ RAG/JEV/MCP/Workflow được đối chiếu với hạ tầng thật trước khi làm gì; kết quả: nút thắt của SHT không nằm ở RAG mà ở dữ liệu sống (CRM tĩnh) và vòng phản hồi.
2. **Khai báo ≠ đang chạy.** Schema chỉ có hiệu lực khi có code đọc (Loại B); mọi ✅ phải có lần chạy thật.
3. **Ba hiệu chỉnh của sơ đồ:** MCP chỉ đọc đứng trước JEV · phản hồi là điều kiện của tin cậy · rủi ro và tin cậy là hai trục.
4. **Cổng không tin lời khai của JEV** (dữ liệu có tĩnh không, tự điền ngả) — cổng tự suy.
5. **Không script nào đánh giá thay người.** Băm Sổ Cái hợp lệ không chứng minh phê duyệt là thật.
6. **Chỉ vá khi có sự cố thật** (quy tắc dừng của `quan-tri-he-thong-skill` §9) — mọi chốt P7, P14 đều sinh từ một ca đã xảy ra.
7. **Đảo vai khi người soạn cũng là người kiểm.**
8. **Không dời cột gôn:** giới hạn 2 vòng sửa; phát hiện mới ngoài phạm vi → tiền điều kiện bước sau hoặc RFC.

## 2. Đã làm (theo bước)

| Bước | Nội dung | Kết quả |
|---|---|---|
| P1 | Thuật ngữ, ánh xạ 5 lớp | ✅ |
| P2 | MCP chỉ đọc CRM | ⛔ chờ token |
| P3 | Hợp đồng quyết định + validator | ✅ vòng 2 |
| P4 | Cổng 3 ngả, sổ, idempotent, cách ly test | ✅ vòng 3 (RFC-01) |
| P5 | Công cụ phản hồi có xác thực + ca thật đầu tiên | ✅ (RFC-02) |
| P6 | RAG BM25 bỏ dấu (phiên khác) | ✅ |
| Gate 3 | Nghiệm thu có điều kiện, cập nhật bản đồ 5 lớp | ✅ `HITL-20260924-010` |
| P7 | `HOI_NGUOI`, nghĩa 3 kết quả, chuẩn mã, bằng chứng tuyệt đối/URL | ✅ nghiệm thu |
| P8–P13 | 6 ca thật Metro (CV-223, NDA ATG, Memo ATG-VnPay, PO-38, bài kiểm chặn TMS, 3 quyết định L3) | 3 CHAP_NHAN · 1 BI_BAC · 3 SAI |
| P11 | Bản PO-38 lọc nội bộ + A10–A14 cho họp Ingenico 26/09, Anti audit chéo | ✅ dùng được |
| P14 | Chặn cụm hoàn thành, văn kiện cấm dùng, bằng chứng chỉ tầng phái sinh | ✅ nghiệm thu `HITL-20260925-007` |
| Phụ | Kho nguồn Metro dời D:\→G:\ (228 tệp), sửa `scan_metro_dossier.py`, dọn bản trùng vào `_archive` trong kho nguồn | ✅ |

## 3. Sự cố lớn và bài học

| Sự cố | Bài học → chốt |
|---|---|
| Script viết cứng "Mr. Hà CHAP_NHAN" 1 ms sau định tuyến | Công cụ phản hồi xác thực Sổ Cái; mỗi HITL gắn đúng 1 quyết định |
| Bản ghi phản hồi thật bị viết đè | Sổ chỉ ghi thêm; sửa sai bằng `mv` + ghi lại có quyết định |
| Test ghi vào sổ thật (đọc env lúc import) | Đường dẫn sổ đọc lúc gọi; test trên thư mục tạm; md5 trước/sau |
| "Không tìm thấy" viết thành "chưa có" | Nêu phạm vi đã tìm; `HOI_NGUOI` |
| Tên file "để ký", chữ gõ sẵn ở khối ký | Render đúng trang khối ký; kiểm ảnh nhúng |
| Suy luận có nhãn "cần xác minh" bị nâng thành "văn kiện nói rõ" | Tách hai phần trong `ket_luan` |
| Quyết định TỰ LÀM đầu tiên sai (căn cứ AI đứng tên Khối CNTT) | P14: cụm hoàn thành, văn kiện cấm dùng, kho nguồn |
| Suy "BGĐ đã duyệt" từ bản nháp của Claude | Không lấy bản nháp của hệ thống làm bằng chứng về bên thứ ba |
| Bản "để hai bên rà" còn ghi chú nội bộ | Lọc trước khi đưa đối tác; quét mọi phần XML |
| Report tự chấm cao hơn thực tế ở hầu hết các vòng | QA luôn chạy lại độc lập, không duyệt theo log dán |

## 4. Chưa làm được

1. Token CRM chỉ đọc (P2) — điều kiện Gate 3 duy nhất còn mở.
2. Hiệu chỉnh tin cậy — sổ phản hồi 7/20 mẫu; ô "LOW × Cao" có 1/4 SAI, ứng viên siết ngưỡng đầu tiên khi đủ mẫu.
3. Engine tự động 24/7 (n8n, Telegram HITL) — vẫn là mô tả.
4. Cổng chưa tự phát hiện tài liệu AI đứng tên đơn vị nghiệp vụ — `van_kien_cam_dung` cập nhật tay.
5. Dọn tủ còn treo theo quyết định Mr. Hà: bản Memo ATG-VnPay 11/08 chưa đưa vào `_archive` kho nguồn; bản lọc PO-38 **v1** còn nằm trong kho nguồn `Review L2\`.
6. Gộp 69 nhãn rà tay (10/09) vào bảng kiểm kê Metro mới trước khi thay bảng chính.
7. Chưa chạy vòng đo trigger tự động cho description skill này.
