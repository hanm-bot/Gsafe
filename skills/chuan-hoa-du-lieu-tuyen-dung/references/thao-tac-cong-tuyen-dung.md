# Thao tác cổng tuyển dụng — sổ tra cứu

Mở file này **khi thực sự thao tác trình duyệt** trên TopCV/LinkedIn (bước [3] và [4]
của luồng chuẩn). Thân skill giữ nguyên tắc quyết định; file này giữ chi tiết nền tảng
cư xử ra sao và gặp lỗi nào thì làm gì.

Mọi quy tắc dưới đây đều rút từ chiến dịch thật, không phải suy đoán.

---

## 1. Lọc & tìm kiếm

### 1.1 LinkedIn

**LinkedIn — xác nhận loại tài khoản trước khi cam kết phạm vi.** Tài khoản cá nhân (kể cả Premium) không có bộ lọc boolean/CV như Recruiter hay Sales Navigator — kiểm tra ngay trên giao diện (menu "Dành cho doanh nghiệp", badge Premium) trước khi hứa hẹn độ chính xác tìm kiếm với người dùng.

**LinkedIn — dùng từ khóa dạng cụm trong ngoặc kép, không để nền tảng tự suy luận.** `"Business Analyst" "payment"` cho kết quả sạch và đúng domain hơn hẳn so với chuỗi từ khóa rời rạc hoặc nối bằng OR (kết quả loãng, nền tảng tự chấm độ liên quan không đáng tin). Test bằng cách đổi 1-2 query khác nhau và so sánh chất lượng headline trả về, giống nguyên tắc test AND/OR ở trên.

**LinkedIn — danh sách kết quả bị virtualized, `read_page` chỉ thấy vài thẻ đầu tiên đã render.** Đừng cố lấy toàn bộ href bằng một lệnh `read_page` duy nhất; dùng `find()` với tên ứng viên cụ thể để lấy đúng href hồ sơ cần, lặp lại cho từng người.

---

## 2. Mở & đọc trang chi tiết

**Trang chi tiết hồ sơ ứng viên trên cổng tuyển dụng thường render nội dung chính trong iframe.** Công cụ trích xuất văn bản (`get_page_text`, `read_page`) sẽ chỉ đọc được lớp vỏ ngoài (banner, quảng cáo, nút bấm) — không đọc được nội dung CV thật. Đi thẳng vào `screenshot` + cuộn tay từng đoạn khi mở trang chi tiết, đừng tốn lượt gọi thử `get_page_text` trước rồi mới nhận ra không có tác dụng.

**Trang chi tiết TIN TUYỂN DỤNG (không phải CV) trên TopCV có bẫy riêng.** `get_page_text` trả về widget khảo sát góp ý chứ không phải nội dung JD → dùng `screenshot` + cuộn. Click tiêu đề tin ở trang danh sách mở tab mới rồi tab chết ngay ("Browser connection is unavailable" → "Tab no longer exists") → lấy URL tin rồi **điều hướng thẳng trong cùng tab**. Mục *Yêu cầu ứng viên* bị thu gọn, phải bấm nút **"Xem đầy đủ mô tả công việc"** mới hiện — không bấm thì mất trọn phần yêu cầu bắt buộc, dẫn tới chấm điểm thiếu căn cứ.

**`resize_window` KHÔNG làm tăng chiều cao ảnh chụp** — chiều cao bị giới hạn bởi chính công cụ chụp, không theo kích thước cửa sổ. Đừng lên kế hoạch dựa vào giả định này; cuộn + chụp nhiều đoạn là cách duy nhất.

**Cuộn vùng iframe bằng bước vừa phải (5–7), không dùng `scroll_amount` tối đa.** Cuộn một bước quá lớn trên trang chi tiết có thể nhảy cóc qua cả một đoạn giữa (từng xảy ra: bỏ sót nốt phần cuối một mục kinh nghiệm làm việc). Sau mỗi lần cuộn, liếc phần đầu ảnh chụp mới có trùng với phần cuối ảnh trước không (chồng lấn) — nếu không trùng, đã nhảy cóc, phải cuộn ngược lại để dò đoạn bị bỏ sót trước khi đọc tiếp.

**Thông tin liên hệ (điện thoại/email/họ tên đầy đủ) thường bị che** cho đến khi ứng viên đồng ý kết nối hoặc nhà tuyển dụng dùng phí nền tảng để mở khóa. **Một số hồ sơ dạng "web-profile" (không phải file CV đính kèm) còn không có cả nút tải/xuất file** — chỉ có Lưu CV, Chia sẻ CV, Báo cáo CV, Gửi tin nhắn, Yêu cầu kết nối. Đây là giới hạn cứng của thiết kế nền tảng — không cố lấy bằng cách khác, không đoán, giữ nguyên `[protected data]` trong ghi chú và báo rõ nếu người dùng yêu cầu tải CV mà nền tảng không hỗ trợ.

**Khi người dùng xin "gửi CV này" cho một hồ sơ dạng web-profile không tải được:** cuộn + chụp toàn bộ nội dung công khai rồi dựng lại thành file Word/PDF chuẩn SHT (không phải file gốc của ứng viên) — ghi rõ nguồn trích xuất, giữ nguyên `[protected data]` cho phần bị khoá, và hỏi người dùng có muốn gửi yêu cầu kết nối để mở khoá liên hệ hay không (xem §8) thay vì tự ý gửi.

### 2.1 LinkedIn — đọc hồ sơ

**LinkedIn — dùng sub-page `.../details/experience/` để đọc kinh nghiệm sạch.** Trang hồ sơ chính trộn lẫn hàng nghìn từ hoạt động/bài đăng lại (repost) trước phần Kinh nghiệm, khiến `get_page_text` tốn token khổng lồ mà chưa chắc lấy được đúng phần cần. Điều hướng thẳng tới `https://www.linkedin.com/in/<vanity-name>/details/experience/` để lấy đúng danh sách chức danh — công ty — mốc thời gian, không lẫn nội dung khác.

---

## 3. Xử lý lỗi công cụ trình duyệt

**Gộp thao tác trình duyệt bằng `browser_batch` ngay từ hành động đầu tiên**, không gọi từng lệnh đơn lẻ rồi đợi bị nhắc.

**Khi công cụ chụp màn hình/click báo lỗi lặp lại** (VD "Cannot attach to this target") trên một tab vừa mở: thử lại tối đa 2 lần (đóng tab, mở lại, đợi vài giây). Quá 2 lần vẫn lỗi trên **tất cả các phương thức tương tác đã thử** (click, screenshot, `find()`, `javascript_exec`...) → **dừng cố lấy chi tiết, dùng dữ liệu tóm tắt sẵn có ở trang danh sách và ghi rõ trong deliverable rằng hồ sơ này chưa được xem đầy đủ.** Chỉ 1 phương thức lỗi (VD chỉ `screenshot` lỗi nhưng `find()` vẫn đọc được DOM) chưa đủ để kết luận tab hỏng — thử phương thức khác trước khi bỏ cuộc.

**Lỗi cấp tool không đồng nghĩa hành động đã thất bại.** Một lệnh `click` có thể báo lỗi ngay cả khi thao tác đã thực sự thành công phía server — trước khi kết luận thất bại và retry/bỏ cuộc, gọi lại `find()` hoặc chụp ảnh để xác minh trạng thái trang thực tế (VD tìm chữ "Chờ UV phản hồi", "Gửi yêu cầu kết nối đến ứng viên thành công!").

**Khi click theo `ref` (từ `find()`) vào tên ứng viên không mở được tab chi tiết mới** (thường gặp ở hồ sơ đã có trạng thái tương tác trước đó như "Đã xem"/"Đã mở"): chụp ảnh màn hình và click trực tiếp vào toạ độ pixel hiển thị của tên ứng viên, thay vì lặp lại thao tác qua `ref`.

**Khi cần chuyển nhiều trang kết quả của cùng một lượt tìm kiếm** (VD đọc lần lượt 70 ứng viên qua 6 trang): sửa tham số `?page=N` trên URL của **cùng một tab** đang mở, không mở tab/phiên mới cho từng trang. Mở lại tìm kiếm ở tab mới có thể khiến chế độ sắp xếp tự đổi (VD từ "Mới cập nhật" sang "Có kinh nghiệm"), làm thứ tự ứng viên giữa các trang không khớp với lần đọc trước.

---

**`Cannot attach to this target` — phân biệt lỗi cục bộ và lỗi hệ thống bằng đối tượng thứ hai.** Sau 2 lần retry thất bại trên cùng một hồ sơ, **mở một hồ sơ khác** bằng đúng thao tác đó. Hồ sơ khác mở được → lỗi cục bộ của riêng hồ sơ đầu: ghi chú "chưa gửi được — lỗi kỹ thuật trình duyệt", chuyển sang người tiếp theo. Hồ sơ khác cũng lỗi → lỗi hệ thống của phiên: dừng cả nhánh thao tác, báo cáo minh bạch, không đốt lượt retry cho từng người còn lại. Ca thật 25/08: một hồ sơ lỗi cả 3 lần trong khi hai hồ sơ ngay sau đó mở bình thường.

**Thu nhỏ trang bằng `document.documentElement.style.zoom` có thể treo renderer.** Khi modal cao hơn khung nhìn, đừng zoom để nhìn thấy nút — zoom làm lệch hệ tọa độ (click theo ảnh không còn khớp `elementFromPoint`) và trên trang nặng thì `Page.captureScreenshot` timeout vĩnh viễn. Dùng đường khác: đọc cây accessibility lấy ref, hoặc tìm URL chuyên biệt của luồng đó (xem §5).

## 4. Luồng gửi yêu cầu kết nối

> Ranh giới cho phép nằm ở thân skill §8 — **luôn xin phép người dùng trước**.
> Phần dưới chỉ mô tả nền tảng cư xử thế nào sau khi đã được phép.

**Luồng UI gửi yêu cầu kết nối (TopCV):** nút hiện "Gửi yêu cầu kết nối" cho ứng viên chưa từng liên hệ, hoặc "Yêu cầu lại" cho ứng viên đã "Quá hạn UV phản hồi" — cả hai đều mở hộp thoại "Yêu cầu kết nối ứng viên" với nội dung mẫu mặc định, xác nhận gửi bằng nút "Gửi yêu cầu". **Không thể gửi lại khi đang ở trạng thái "Chờ UV phản hồi"** (chưa quá hạn) — đừng lãng phí thao tác thử gửi lại sớm. Hồ sơ đã chuyển sang "Chat với ứng viên" không còn nút kết nối chuẩn.

**LinkedIn — nút "Kết nối" hành vi khác nhau tùy cấp độ kết nối (hiển thị "· 2" / "· 3" cạnh tên).** Với ứng viên cấp 3, nút mở modal JS ngay tại chỗ. Với ứng viên cấp 2 (có kết nối chung), nút thực chất là link điều hướng tới `/preload/custom-invite/?vanityName=...` — click trực tiếp qua `ref` hoặc tọa độ pixel nhiều lần không có phản hồi vì trang chưa kịp điều hướng. Khi click lặp lại không ăn thua, đọc `href` thật của phần tử qua `read_page` rồi điều hướng thẳng URL đó thay vì đoán mò thêm.

**LinkedIn — kiểm tra cấp kết nối trước khi định gửi lời mời.** Nếu hồ sơ đã hiện "· 1" (kết nối cấp 1 sẵn có), không gửi lại lời mời — đề xuất phương án nhắn tin trực tiếp thay thế.

## 5. Ô lọc ngừng nhận ký tự — đường đi qua state Vue (TopCV)

Triệu chứng: ô multiselect "Trong CV bắt buộc có từ khóa" không nhận ký tự. Đã thử và thất bại hết: gõ trực tiếp, `form_input`, native setter + dispatch `input`/`keydown`, click theo ref, click theo tọa độ, tải lại trang.

**Bước 1 — tìm component:**

    const inp = [...document.querySelectorAll('input')]
      .filter(i => i.placeholder && i.placeholder.includes('Nhập từ khóa và nhấn enter'))[0];
    const vm = inp.parentElement.parentElement.__vue__;   // vue-multiselect

**Bước 2 — thêm/xóa chip qua chính component:**

    vm.$emit('input', [{value:'Business Analyst', text:'Business Analyst'}]);   // thêm
    vm.removeElement(vm.value[0]);                                             // xóa

**Bước 3 — CẢNH BÁO: chip hiện đúng KHÔNG có nghĩa là state đúng.** Sau bước 2 chip hiển thị chuẩn nhưng kết quả tìm kiếm **không đổi**, vì state ở component cha vẫn giữ giá trị cũ. Leo lên tìm trang cha:

    let p = vm.$parent; for (let i=0; i<4; i++) p = p.$parent;
    JSON.stringify(p.filters);
    // → and_tags: ["Product Owner","Business Analyst"]   ← CẢ HAI, dù chip chỉ còn một

**Bước 4 — sửa thẳng state cha rồi gọi hàm nạp dữ liệu của trang:**

    p.filters.and_tags = ['Business Analyst'];
    p.filters.page = '1';
    p.loadCaptchaAndFetchData();        // → 754 kết quả, đúng bộ lọc mới

Đặt sẵn helper để dùng lại trong cả phiên:

    window.__getP4 = function () {
      const inp = [...document.querySelectorAll('input')]
        .filter(i => i.placeholder && i.placeholder.includes('Nhập từ khóa và nhấn enter'))[0];
      let p = inp.parentElement.parentElement.__vue__.$parent;
      for (let i=0; i<4; i++) p = p.$parent;
      return p;
    };

**Quy tắc chung rút ra:** giao diện hiển thị đúng không đảm bảo tham số gửi lên server đúng. Khi bấm nút tìm kiếm mà số kết quả **không đổi** dù bộ lọc trông đã khác, kiểm tra state tầng cha trước khi kết luận "trang bị lỗi".

## 6. Quét dữ liệu hàng loạt từ state — nhanh hơn ~10 lần

`p4.cvs` chứa sẵn mọi thứ cần cho vòng sàng lọc thô: `fullname` · `title` · `city` · `experiences` · `educations` · `last_update_time_str` · **`request_connection`** (null = chưa gửi lời mời; có giá trị = đã gửi).

Trường `request_connection` đặc biệt giá trị: biết ngay ai đã được gửi kết nối **mà không tốn credit mở CV** và không phải mở từng hồ sơ để đọc trạng thái.

Quét toàn bộ chiến dịch:

    const p4 = window.__getP4();
    window.__all = [];
    for (let pg = 1; pg <= 6; pg++) {
      p4.filters.page = String(pg);
      p4.loadCaptchaAndFetchData();
      await new Promise(r => setTimeout(r, 4500));      // chờ API trả về
      p4.cvs.forEach(c => window.__all.push({
        pg, key: c.private_key, name: c.fullname, title: c.title, city: c.city,
        exp: (c.experiences || []).join(' ; '),
        upd: c.last_update_time_str,
        rc: c.request_connection ? 'SENT' : 'NONE'
      }));
    }

72 hồ sơ trong ~30 giây, so với điều hướng + chụp màn hình từng trang: nhanh hơn khoảng 10 lần và không dính lỗi `Cannot attach`.

**Lưu ý khi in kết quả:** chuỗi chứa dữ liệu giống cookie/query string bị công cụ chặn hiển thị (`[BLOCKED: Cookie/query string data]`). Khi gặp, in **từng trường ngắn** thay vì `JSON.stringify` cả object.

## 7. LinkedIn — gửi lời mời khi modal nằm trong shadow DOM

Nút "Kết nối" trên trang hồ sơ mở modal **không thao tác được**: click theo ref thất bại, `document.querySelector('button')` không thấy nút trong modal, screenshot lỗi, và thu nhỏ trang làm treo renderer.

Đọc cây accessibility thấy nút thực chất là một link:

    /preload/custom-invite/?vanityName=<username>

Điều hướng thẳng vào URL đó → dialog xuất hiện trong **DOM thường**, thao tác bình thường.

Luồng đầy đủ cho mỗi ứng viên (~4 bước):

1. `navigate` → `https://www.linkedin.com/preload/custom-invite/?vanityName=<username>`
2. chờ ~8 giây, rồi:

        [...document.querySelectorAll('button')]
          .find(x => /Thêm ghi chú/i.test(x.innerText)).click();

3. `find` ô ghi chú → `form_input` (tài khoản Premium: tối đa **300 ký tự**)
4. gửi:

        const b = [...document.querySelectorAll('button')]
          .find(x => x.getAttribute('aria-label') === 'Gửi lời mời');
        if (b && !b.disabled) b.click();

**Xác minh sau khi gửi:** mở `linkedin.com/mynetwork/invitation-manager/sent/` — danh sách chỉ hiện ~10 lời mời mới nhất; người gửi sớm hơn phải kiểm tra trực tiếp trên hồ sơ (nút chuyển từ "Kết nối" thành "Đang chờ xử lý").

**Quy tắc chung rút ra:** khi modal của SPA không thao tác được, đọc `href` của nút mở modal — nhiều ứng dụng có URL riêng cho cùng luồng đó, và trang riêng thường không dùng shadow DOM.
