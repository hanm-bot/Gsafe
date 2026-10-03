# Phát hành và cài đặt sht-skills — ba kênh, ai bấm gì

> DA-DOI-CHIEU-NGUON: rút từ các lần phát hành 0.23.0 → 0.25.0 (25–26/09/2026), ghi ở dòng phiên bản đầu `references/so-dang-ba.md` và memory `project_sht-skills-rel-01.md`. Là cách làm đã chạy thật tới 26/09/2026 — kênh cài có thể đổi theo bản Claude Desktop.

## 0. Bảo trì plugin `sht-skills` và lý do của bộ công cụ

> Chuyển từ cuối `SKILL.md` ngày 03/10/2026 (v0.30.12) vì SKILL.md sát ngưỡng 300 dòng (E5). Nội dung giữ nguyên.

### 0.1 Bảo trì plugin `sht-skills`

Mọi skill trong thư mục `skills/` của plugin `sht-skills` phải có dòng tương ứng trong Sổ đăng bạ. Số skill hiện tại xem ở dòng đầu Sổ đăng bạ, không ghi cứng ở đây (câu này từng ghi "19 skill" và bị cũ khi plugin lên 29 — sửa 25/09/2026). Hệ quả cho mọi lần nâng cấp về sau:

- **Sửa skill trong plugin thì sửa ở nguồn plugin rồi đóng gói lại**, không dùng `save_skill` — `save_skill` tạo bản skill cá nhân song song, gây hai bản cùng tên trôi khác nhau (đúng loại lỗi skill này sinh ra để chặn).
- Tăng `version` trong `.claude-plugin/plugin.json` mỗi lần phát hành: sửa lỗi → PATCH, thêm/bỏ skill hoặc đổi ranh giới → MINOR.
- **Đóng gói TỪ ĐÚNG folder nguồn của người dùng**, không từ bản cache plugin đang cài và không từ một bản copy cũ. Trước khi đóng gói, `diff` mục lục + số dòng giữa folder nguồn và bản cache: lệch nhau nghĩa là đã trôi nhánh, phải hợp nhất trước (đã xảy ra 23–24/08/2026 với skill tuyển dụng).
- **Đóng gói bằng `scripts/release.py`, không nén tay.** Nó chạy tự kiểm → audit → kiểm manifest/nguồn/sổ → nén → kiểm lại chính gói. Trượt cổng nào là không ra file.
- **Thư mục nguồn plugin chỉ được chứa 3 thứ: `.claude-plugin/`, `skills/`, `README.md`.** Phiên v0.9.0 phát hiện hai thư mục làm việc (`skill-upgrade-24082026/`, `skill-upgrade-25082026/`) nằm lẫn trong nguồn, chứa cả các file `.plugin` cũ — nên bản phát hành **gói luôn ba bản phát hành trước vào bên trong**, phình từ 129 KB lên 513 KB. Để lâu thì mỗi bản lại bọc bản trước, lớn theo cấp số nhân. Sau khi đóng gói, kiểm: kích thước không nhảy vọt bất thường, và `unzip -Z1 <file>.plugin | grep -c 'skill-upgrade\|\.plugin$'` phải bằng 0. **Dùng `-Z1`, không dùng `-l`** — `unzip -l` in dòng tiêu đề `Archive: <tên gói>.plugin`, dòng đó tự khớp mẫu `\.plugin$` nên phép kiểm luôn trả về ≥1 dù gói hoàn toàn sạch. Cảnh báo giả này đã xảy ra ở phiên 03/09/2026. File nháp của phiên để ở thư mục làm việc của người dùng, không để trong nguồn plugin.
- Ghi thay đổi vào Sổ đăng bạ ngay trong cùng phiên phát hành.
- Push, cập nhật tab Code, tải lên Organization library — ai bấm gì, kiểm gì: `references/phat-hanh-va-cai-dat.md`. Kết thúc bằng `scripts/kiem_dong_bo_ban_cai.py`: chỉ exit 0 mới coi là phát hành xong.

### 0.2 Vì sao có `test_audit.py` và `release.py`

**Vì sao có `test_audit.py`:** `audit_skills.py` là thứ cả hệ dựa vào để kết luận "sạch hay không", mà nó đã từng có 2 lỗi thật và **cả hai đều lộ ra tình cờ**. Một công cụ kiểm chứng không được kiểm chứng thì chỉ là niềm tin. Mỗi ca kiểm **hai chiều**: lỗi phải nổ khi có lỗi, và phải im khi không có lỗi — thiếu chiều thứ hai thì không bắt được cảnh báo giả, đúng loại lỗi đã làm hỏng E4 suốt nhiều phiên.

**Vì sao có `release.py`:** mọi lỗi phát hành đã gặp đều do quên một bước thủ công. Checklist trong đầu không đáng tin; cổng chặn thì đáng tin. Cổng 2 cố ý **không** soi skill cá nhân — E7 là lỗi phía cài đặt, chặn phát hành vì nó sẽ khoá cứng việc ra bản mới chỉ vì người dùng chưa kịp xoá một skill cũ.

## 1. Ba kênh — ba bản có thể lệch nhau

| Kênh | Bản nằm ở | Cập nhật bằng | Ai bấm |
|---|---|---|---|
| Nguồn + GitHub | `SKILL file/sht-skills/` → `origin` (`Gsafe`), nhánh `qa-hanh-vi` và `main` | `git -C "G:\CHUYỂN ĐỔI SỐ SHT\SKILL file\sht-skills" push origin qa-hanh-vi qa-hanh-vi:main` | **Mr. Hà** — agent chỉ commit và đưa lệnh một dòng |
| Tab Code (Claude Desktop) | cache `~/.claude/plugins/cache/sht-local/sht-skills/<version>/` | `claude.exe` đi kèm Desktop: `plugin marketplace update sht-local` rồi `plugin update sht-skills@sht-local` | Claude, sau khi Mr. Hà đã push |
| Cowork (Organization library) | máy chủ claude.ai | Mr. Hà tải file `_plugin-builds/sht-skills-v<x>.plugin` lên trang quản trị | **Mr. Hà** |

`claude.exe` đi kèm Desktop tìm bằng: `ls -d "$APPDATA"/Claude/claude-code/*/claude.exe | tail -1`.

## 1b. Bước cuối: kiểm đồng bộ ba kênh *(thêm 03/10/2026, v0.30.10)*

Sau khi đã push, cập nhật tab Code và Mr. Hà đã tải gói lên tổ chức (chờ Cowork đồng bộ về máy), chạy:

```bash
python "G:\CHUYỂN ĐỔI SỐ SHT\SKILL file\sht-skills\skills\quan-tri-he-thong-skill\scripts\kiem_dong_bo_ban_cai.py"
```

Nó so nguồn với: Git (ahead/behind, thay đổi chưa commit) · bản cài tab Code (`installed_plugins.json` + nội dung cache) · bản Cowork trên máy (`rpm/plugin_*`) · skill cá nhân trùng tên. Exit **0** = khớp hết → mới được báo "đã phát hành xong". Exit **1** = lệch, in từng file/kênh lệch. Exit **2** = không thấy kênh nào để so — **không** được coi là khớp.

Vì sao: ca 03/10/2026 — tab Code đã 0.30.9 nhưng phiên vẫn nạp 0.30.8, vì skill được nạp từ bản Cowork (rpm) chứ không từ cache `sht-local`. Kiểm từng kênh bằng tay thì dễ sót đúng kênh đang thật sự được dùng.

## 2. Luật đã trả giá

- **Đã tải một gói lên Organization library thì sửa nguồn phải nâng số hiệu.** Hai gói khác nội dung trùng số hiệu → máy chủ giữ bản cũ, không báo lỗi (0.23.0 → 0.23.1, 25/09).
- **Kênh Cowork/Organization library: "đã tải lên" chưa phải "đã cài".** Kiểm số hiệu trong `installed_plugins.json`/manifest của Cowork trên máy **và** grep một chuỗi chỉ có ở bản mới trong thư mục skill đang nạp (ca 10/09/2026, 0.16.4). *(thêm 30/09/2026, v0.29.0)*
- **Thông báo "Zip file contains path with invalid characters" có thể chỉ sai chỗ.** Ca 10/09: căn nguyên là `Compress-Archive` sinh entry trùng `plugin.json` và lẫn `.gitignore`, không phải tên tiếng Việt. Soi nội dung gói (`unzip -Z1`), và chỉ đóng gói bằng `release.py`. *(thêm 30/09/2026, v0.29.0)*
- **Cập nhật tab Code xong phải `diff -rq` cache với nguồn.** "Đã cập nhật" chưa phải bằng chứng; chỉ `diff` rỗng mới là.
- **Nhánh `main` cục bộ theo kịp bằng `git fetch origin main:main`** sau khi Mr. Hà push `qa-hanh-vi:main` — không `checkout`/`merge` trên nhánh đang làm.
- **Không tự push, không force-push** — kể cả khi đã có lệnh duyệt rõ; lệnh cuối để Mr. Hà bấm.
- **Ghi file bằng Python phải `newline=''`** trên Windows, nếu không file LF thành CRLF và `git diff` báo sửa cả file.
- **Không cài qua `save_skill`** cho skill thuộc plugin — sinh bản cá nhân song song cùng tên (E7).
