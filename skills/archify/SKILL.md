---
name: archify
description: "Vẽ sơ đồ quy trình (workflow diagram) từ một KẾ HOẠCH đã chốt hoặc một mô tả quy trình bất kỳ, đánh dấu rõ bước tự động hoá / điểm người duyệt / chỗ AI dừng chờ xác nhận bằng Mermaid flowchart. LUÔN dùng khi người dùng nói \"vẽ sơ đồ quy trình\", \"archify\", \"vẽ workflow\", \"trực quan hoá kế hoạch\", hoặc ngay sau khi grill-me chốt xong một KẾ HOẠCH và người dùng muốn xem sơ đồ. KHÔNG dùng để tự lập kế hoạch từ đầu (dùng grill-me hoặc superpowers:writing-plans), không dùng cho biểu đồ dữ liệu/số liệu (dùng dataviz), không dùng để vẽ sơ đồ kiến trúc kỹ thuật chi tiết (class/sequence diagram) nằm ngoài phạm vi một quy trình nghiệp vụ."
---

# Archify — Vẽ Sơ Đồ Quy Trình Từ Kế Hoạch

Mục tiêu: biến một KẾ HOẠCH (chuỗi bước, mỗi bước có AI/người/SOP/tiêu chí ĐẠT — đúng định dạng `grill-me` pha ② tạo ra, hoặc một mô tả quy trình bất kỳ người dùng cung cấp trực tiếp) thành **một sơ đồ trực quan duy nhất**, giúp người xem thấy ngay luồng đi, chỗ máy tự chạy, chỗ người phải bấm duyệt, và chỗ AI dừng lại chờ.

## Đầu vào
- Một KẾ HOẠCH đã chốt (từ `grill-me` pha ②), HOẶC
- Một mô tả quy trình bất kỳ người dùng gõ trực tiếp — không bắt buộc phải qua `grill-me` trước.

Nếu đầu vào còn thiếu bước hoặc mơ hồ ở giữa chừng, hỏi ngắn gọn đúng 1 câu để bổ sung — không tự suy diễn bước còn thiếu rồi vẽ luôn.

## Quy tắc ký hiệu (bắt buộc dùng nhất quán trong mọi sơ đồ)
Mỗi bước phải thuộc đúng MỘT trong 3 loại, đánh dấu bằng hình dạng + nhãn cố định:
- 🤖 **Tự động (AI/hệ thống chạy thẳng):** hình chữ nhật thường (`[Tên bước]`).
- 🧑 **Điểm người duyệt (Human Checkpoint):** hình thoi quyết định (`{Tên bước?}`), ghi rõ AI DỪNG chờ tín hiệu gì mới đi tiếp.
- 🛑 **AI dừng/chặn cứng (Guardrail):** nhãn bắt đầu bằng "🛑 DỪNG:" — nơi AI tuyệt đối không tự quyết, bắt buộc thoát ra hỏi người.

Không được để một bước "lửng" không rõ thuộc loại nào trong 3 loại trên.

## Định dạng xuất
Mặc định vẽ bằng **Mermaid** (`flowchart TD`) đặt trong khối ```mermaid — render trực tiếp trong Artifact và hầu hết trình xem Markdown, không cần thư viện thêm. Nếu môi trường không render được Mermaid, xuất kèm bảng liệt kê các bước làm bản dự phòng dạng chữ (Bước · Loại · Điều kiện đi tiếp).

## Quy trình 3 bước
1. **Bóc tách các bước** từ đầu vào, gán đúng 1 trong 3 loại ký hiệu cho từng bước.
2. **Vẽ sơ đồ Mermaid**, nối các bước theo đúng thứ tự luồng đã mô tả; mỗi nhánh rẽ (nếu có) ghi rõ điều kiện rẽ trên cạnh mũi tên.
3. **Trình sơ đồ + hỏi đúng 1 câu:** "Sơ đồ này đã đúng luồng và đúng chỗ dừng/duyệt chưa? Cần chỉnh gì trước khi coi là chốt không?" — không tự ý coi sơ đồ là bản cuối khi chưa có xác nhận.

## Bàn giao ngược `grill-me`
Nếu người dùng chỉnh sửa luồng ngay trên sơ đồ (thêm bước, đổi loại ký hiệu một bước) và đầu vào ban đầu là KẾ HOẠCH từ `grill-me`, nhắc người dùng: thay đổi này cần phản ánh ngược lại vào KẾ HOẠCH gốc trước khi qua Cổng Proceed của `grill-me` — không để sơ đồ và kế hoạch lệch nhau, sơ đồ chỉ là hình chiếu của kế hoạch, không phải bản thay thế.

## Vị trí trong khung giải quyết vấn đề (B5)
archify là bước cuối trước **cổng chọn đường ray** (bản đồ `docs/HE-DIEU-HANH-AI-5-LOP.md` mục 1c). Đầu vào có thể là KẾ HOẠCH của `grill-me` (nhánh QUY TRÌNH) hoặc một PRD đã chốt (`prd-architect` / `sht-cds-thiet-ke-prd`, nhánh SẢN PHẨM). Với PRD thì vẽ luồng To-Be tổng thể và giữ đúng điểm người duyệt đã ghi trong PRD. Sơ đồ chốt xong thì gợi ý chọn ray bằng `../sht-cds-thiet-ke-agent/references/chon-duong-ray.md`, không tự chốt ray.

## Ranh giới — giữ skill gọn
Không tự vẽ thêm chi tiết kỹ thuật không có trong kế hoạch gốc (không tự bịa tên hệ thống, tên bảng dữ liệu, tên API). Không dùng skill này để vẽ biểu đồ số liệu/thống kê (việc của `dataviz`) hay sơ đồ kiến trúc phần mềm chi tiết (class/sequence diagram cấp code) — chỉ vẽ đúng một luồng quy trình nghiệp vụ ở mức người đọc phi kỹ thuật cũng hiểu được.
