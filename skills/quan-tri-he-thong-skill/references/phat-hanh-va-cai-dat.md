# Phát hành và cài đặt sht-skills — ba kênh, ai bấm gì

> DA-DOI-CHIEU-NGUON: rút từ các lần phát hành 0.23.0 → 0.25.0 (25–26/09/2026), ghi ở dòng phiên bản đầu `references/so-dang-ba.md` và memory `project_sht-skills-rel-01.md`. Là cách làm đã chạy thật tới 26/09/2026 — kênh cài có thể đổi theo bản Claude Desktop.

## 1. Ba kênh — ba bản có thể lệch nhau

| Kênh | Bản nằm ở | Cập nhật bằng | Ai bấm |
|---|---|---|---|
| Nguồn + GitHub | `SKILL file/sht-skills/` → `origin` (`Gsafe`), nhánh `qa-hanh-vi` và `main` | `git -C "G:\CHUYỂN ĐỔI SỐ SHT\SKILL file\sht-skills" push origin qa-hanh-vi qa-hanh-vi:main` | **Mr. Hà** — agent chỉ commit và đưa lệnh một dòng |
| Tab Code (Claude Desktop) | cache `~/.claude/plugins/cache/sht-local/sht-skills/<version>/` | `claude.exe` đi kèm Desktop: `plugin marketplace update sht-local` rồi `plugin update sht-skills@sht-local` | Claude, sau khi Mr. Hà đã push |
| Cowork (Organization library) | máy chủ claude.ai | Mr. Hà tải file `_plugin-builds/sht-skills-v<x>.plugin` lên trang quản trị | **Mr. Hà** |

`claude.exe` đi kèm Desktop tìm bằng: `ls -d "$APPDATA"/Claude/claude-code/*/claude.exe | tail -1`.

## 2. Luật đã trả giá

- **Đã tải một gói lên Organization library thì sửa nguồn phải nâng số hiệu.** Hai gói khác nội dung trùng số hiệu → máy chủ giữ bản cũ, không báo lỗi (0.23.0 → 0.23.1, 25/09).
- **Kênh Cowork/Organization library: "đã tải lên" chưa phải "đã cài".** Kiểm số hiệu trong `installed_plugins.json`/manifest của Cowork trên máy **và** grep một chuỗi chỉ có ở bản mới trong thư mục skill đang nạp (ca 10/09/2026, 0.16.4). *(thêm 30/09/2026, v0.29.0)*
- **Thông báo "Zip file contains path with invalid characters" có thể chỉ sai chỗ.** Ca 10/09: căn nguyên là `Compress-Archive` sinh entry trùng `plugin.json` và lẫn `.gitignore`, không phải tên tiếng Việt. Soi nội dung gói (`unzip -Z1`), và chỉ đóng gói bằng `release.py`. *(thêm 30/09/2026, v0.29.0)*
- **Cập nhật tab Code xong phải `diff -rq` cache với nguồn.** "Đã cập nhật" chưa phải bằng chứng; chỉ `diff` rỗng mới là.
- **Nhánh `main` cục bộ theo kịp bằng `git fetch origin main:main`** sau khi Mr. Hà push `qa-hanh-vi:main` — không `checkout`/`merge` trên nhánh đang làm.
- **Không tự push, không force-push** — kể cả khi đã có lệnh duyệt rõ; lệnh cuối để Mr. Hà bấm.
- **Ghi file bằng Python phải `newline=''`** trên Windows, nếu không file LF thành CRLF và `git diff` báo sửa cả file.
- **Không cài qua `save_skill`** cho skill thuộc plugin — sinh bản cá nhân song song cùng tên (E7).
