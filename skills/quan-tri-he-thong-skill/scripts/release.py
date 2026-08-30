#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cổng phát hành plugin — chạy đủ chuỗi kiểm rồi mới đóng gói.

Dùng:
    python3 release.py <thư_mục_gốc_plugin> [--personal DIR] [--out FILE] [--check-only]

Chín cổng (0-8), trượt bất kỳ cổng nào là DỪNG, không tạo file .plugin:
    0. Đối chiếu bản — nguồn không khuyết skill so với bản đang cài (doi_chieu_ban.py)
    1. Bộ tự kiểm của chính công cụ audit  (test_audit.py)
    2. Audit NỘI DUNG GÓI — không còn lỗi mức CAO (E7 phía cài đặt chỉ cảnh báo)
    3. Manifest hợp lệ: name kebab-case, version semver
    4. Không trùng số hiệu với gói cũ — version nguồn khác version trong --out cũ
    5. Nguồn sạch: không lẫn thư mục nháp, không có .plugin cũ bên trong
    6. Mọi skill có SKILL.md
    7. Sổ đăng bạ khớp số lượng thư mục skill
    8. Gói sau khi nén: 0 đường dẫn dấu gạch ngược, đủ số SKILL.md

VÌ SAO: các lỗi phát hành đã gặp trong thực tế đều do người/agent quên một
bước thủ công — gói nén trên Windows sinh đường dẫn gạch ngược (plugin cài vào
chỉ nạp 8/10 skill mà KHÔNG báo lỗi), nguồn lẫn thư mục nháp làm gói bọc luôn
ba bản phát hành trước (phình 4x), Sổ đăng bạ lệch số, hai bản đóng gói liên
tiếp giữ nguyên version trong khi nguồn đã đổi (gói cũ có thể đã được cài,
không ai truy được nó đã đi tới đâu). Checklist trong đầu không đáng tin;
cổng chặn thì đáng tin.
"""
import json, os, re, subprocess, sys, tempfile, zipfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ALLOWED = {'.claude-plugin', 'skills', 'README.md', 'agents',
           '.mcp.json', 'CONNECTORS.md', 'hooks'}
FAILS = []


def gate(n, label, ok, detail=''):
    print(f"  {'✅' if ok else '❌'} Cổng {n} — {label}")
    if detail:
        print(f"       {detail}")
    if not ok:
        FAILS.append(f'Cổng {n}: {label}')
    return ok


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    root = os.path.abspath(args[0] if args else '.')

    def opt(f):
        return sys.argv[sys.argv.index(f) + 1] if f in sys.argv and sys.argv.index(f) + 1 < len(sys.argv) else None

    personal = opt('--personal')
    skills_dir = os.path.join(root, 'skills')
    print(f'CỔNG PHÁT HÀNH — {root}\n')

    # 0 — đối chiếu bản.
    # CỐ Ý KHÔNG truyền --goi. Tại thời điểm phát hành, gói ở --out là bản CŨ;
    # nguồn vừa sửa nên chắc chắn khác nó → cổng sẽ luôn trượt, không bao giờ
    # ra được bản mới. So nguồn↔gói chuyển sang bước xác minh SAU phát hành.
    # Cổng này chặn đúng một thứ: skill có ở bản đang cài mà THIẾU ở nguồn —
    # dấu hiệu chắc chắn đang đóng gói từ nguồn khuyết, sẽ xoá skill khỏi bản
    # cài của người dùng. V1/V3/V4 chỉ báo, vì hash không cho biết chiều lệch.
    dc = subprocess.run(
        [sys.executable, os.path.join(HERE, 'doi_chieu_ban.py'), root],
        capture_output=True, text=True)
    # main() của doi_chieu_ban.py chỉ trả 0 hoặc 1 — bất kỳ mã thoát KHÁC (ví dụ 2:
    # không tìm thấy file khi bị đổi tên/xoá nhầm) chắc chắn không phải "có phát hiện
    # thật", mà là công cụ không chạy được nổi. Traceback trong stderr là dấu hiệu
    # thứ hai của cùng loại lỗi (script chạy được nhưng crash giữa đường, returncode
    # vẫn là 1 — TRÙNG đúng mã của "có phát hiện thật"). Cả hai đều phải bị bắt trước
    # khi kết luận là phát hiện thật.
    hong = dc.returncode not in (0, 1) or 'Traceback (most recent call last)' in dc.stderr
    if dc.returncode == 0:
        gate(0, 'Đối chiếu bản — nguồn không khuyết skill', True)
    elif hong:
        # Công cụ sập là lỗi của CÔNG CỤ, không phải của nguồn; nuốt stderr (bằng
        # capture_output mà không in ra) là kiểu "báo như đang hoạt động" tệ hơn cả
        # không có chốt. Trượt cổng vẫn đúng (an toàn), nhưng phải nói đúng lý do và
        # trích cả stderr thật để người vận hành sửa đúng chỗ.
        gate(0, 'Đối chiếu bản — CÔNG CỤ LỖI, không phải phát hiện thật', False,
             f'doi_chieu_ban.py không chạy được (mã thoát {dc.returncode}) — xem stderr '
             'bên dưới, đừng đi tìm "skill thiếu ở nguồn":\n' +
             '\n'.join('       ' + ln for ln in dc.stderr.strip().splitlines()[-8:]))
    else:
        m = re.search(r'(\d+) phát hiện mức chặn phát hành', dc.stdout)
        n = m.group(1) if m else '?'
        gate(0, 'Đối chiếu bản — nguồn không khuyết skill', False,
             f'{n} phát hiện mức chặn phát hành (V1/V2). Nguồn thiếu skill mà bản '
             'đang cài có. Đóng gói lúc này sẽ xoá skill khỏi bản cài. Chạy '
             'doi_chieu_ban.py để xem chi tiết.')

    # 1 — tự kiểm công cụ
    t = subprocess.run([sys.executable, os.path.join(HERE, 'test_audit.py')],
                       capture_output=True, text=True)
    gate(1, 'Bộ tự kiểm audit_skills.py', t.returncode == 0,
         '' if t.returncode == 0 else
         f"{t.stdout.count('❌')} ca trượt — sửa công cụ trước khi tin kết quả audit")

    # 2 — audit nội dung gói
    # Phạm vi cổng 2 là NỘI DUNG GÓI, cố ý KHÔNG truyền --personal.
    # E7 (còn bản skill cá nhân song song) là lỗi phía CÀI ĐẶT trên tài khoản,
    # không phải lỗi của gói — chặn phát hành vì nó là sai phạm vi, và sẽ khoá
    # cứng việc ra bản mới chỉ vì người dùng chưa kịp xoá một skill cũ.
    a = subprocess.run([sys.executable, os.path.join(HERE, 'audit_skills.py'),
                        skills_dir, '--plugin', root], capture_output=True, text=True)
    hi = re.search(r'\((\d+) mức CAO', a.stdout)
    n_hi = int(hi.group(1)) if hi else (0 if a.returncode == 0 else 1)
    gate(2, 'Audit nội dung gói — 0 lỗi mức CAO', n_hi == 0,
         '' if n_hi == 0 else f'{n_hi} lỗi CAO. Chạy audit_skills.py để xem chi tiết.')

    # 3 — manifest
    mf = os.path.join(root, '.claude-plugin', 'plugin.json')
    ok3, d3, ver, name = False, 'thiếu .claude-plugin/plugin.json', None, None
    if os.path.isfile(mf):
        try:
            m = json.load(open(mf, encoding='utf-8'))
            name, ver = m.get('name', ''), m.get('version', '')
            ok3 = bool(re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', name)) and \
                bool(re.fullmatch(r'\d+\.\d+\.\d+', ver))
            d3 = f'{name} v{ver}' if ok3 else f'name/version không hợp lệ: "{name}" / "{ver}"'
        except Exception as e:
            d3 = f'JSON hỏng: {e}'
    gate(3, 'Manifest hợp lệ', ok3, d3)

    # 4 — không trùng số hiệu với gói cũ.
    # out được tính ở đây (không chỉ ở bước nén) vì cổng này cần biết trước khi
    # nén xem file đích đã tồn tại chưa. Đọc version BÊN TRONG gói .plugin (zip),
    # không tin tên file — hai bản đóng gói liên tiếp có thể ghi đè cùng --out
    # trong khi quên tăng version ở nguồn (đúng sự cố đã xảy ra: gói 20:02 rồi
    # 20:39, cả hai cùng 0.15.0, gói sau ghi đè gói trước — không ai truy được
    # bản đang cài trên máy người dùng là bản nào trong hai bản đó).
    out = opt('--out') or os.path.join(os.path.dirname(root), f'{name}.plugin')
    ver_goi = None
    if os.path.isfile(out):
        try:
            with zipfile.ZipFile(out) as zf:
                for ten_file in zf.namelist():
                    phan = ten_file.replace('\\', '/').split('/')
                    if len(phan) >= 2 and phan[-2] == '.claude-plugin' and phan[-1] == 'plugin.json':
                        try:
                            ver_goi = json.loads(zf.read(ten_file).decode('utf-8')).get('version')
                        except Exception:
                            ver_goi = None
                        break
        except (OSError, zipfile.BadZipFile):
            ver_goi = None
    trung_ver = os.path.isfile(out) and ver_goi is not None and ver_goi == ver
    gate(4, 'Không trùng số hiệu với gói cũ', not trung_ver,
         '' if not trung_ver else
         f'{out} đã tồn tại và cùng mang v{ver} với nguồn. Gói cũ có thể đã được '
         'cài vào máy người dùng và không ai truy được nó đã đi tới đâu. '
         'Tăng version trong .claude-plugin/plugin.json trước khi đóng gói lại.')

    # 5 — nguồn sạch
    stray = sorted(x for x in os.listdir(root) if not x.startswith('.git') and x not in ALLOWED)
    nested = [f for dp, _, fs in os.walk(root) for f in fs if f.endswith('.plugin')]
    gate(5, 'Nguồn plugin sạch', not stray and not nested,
         '' if not stray and not nested else
         f'lẫn: {", ".join(stray) or "-"}; file .plugin bên trong: {len(nested)}')

    # 6 — mọi skill hợp lệ
    dirs = [d for d in sorted(os.listdir(skills_dir))
            if os.path.isdir(os.path.join(skills_dir, d))] if os.path.isdir(skills_dir) else []
    bad = [d for d in dirs if not os.path.isfile(os.path.join(skills_dir, d, 'SKILL.md'))]
    gate(6, f'{len(dirs)} skill đều có SKILL.md', not bad,
         '' if not bad else 'thiếu SKILL.md: ' + ', '.join(bad))

    # 7 — sổ đăng bạ khớp số lượng
    sys.path.insert(0, HERE)
    try:
        from audit_skills import read_registry, BUILTIN
        rows = read_registry(skills_dir)
        own = [d for d in dirs if d not in BUILTIN]
        n_reg = len(rows) if rows else 0
        gate(7, 'Sổ đăng bạ khớp thực tế', rows is not None and n_reg == len(own),
             '' if rows and n_reg == len(own) else f'sổ {n_reg} hàng / thư mục {len(own)} skill')
    except Exception as e:
        gate(7, 'Sổ đăng bạ khớp thực tế', False, str(e))

    # Cảnh báo phía cài đặt — KHÔNG chặn phát hành, nhưng phải nói ra
    if personal:
        pa = subprocess.run([sys.executable, os.path.join(HERE, 'audit_skills.py'),
                             skills_dir, '--personal', personal, '--json'],
                            capture_output=True, text=True)
        try:
            e7 = [f for f in json.loads(pa.stdout) if f['code'] == 'E7']
        except Exception:
            e7 = []
        if e7:
            print('\n  ⚠  Việc phía cài đặt (không chặn phát hành):')
            for f in e7:
                print(f"       [{f['code']}] {f['skill']} — {f['msg'][:96]}...")
            print('       Xử lý sau khi cài bản mới.')

    if FAILS:
        print('\n❌ DỪNG — chưa đóng gói. Cổng trượt:')
        for f in FAILS:
            print('   -', f)
        return 1

    if '--check-only' in sys.argv:
        print('\n✅ Tám cổng đều đạt (chế độ chỉ kiểm, không đóng gói).')
        return 0

    # 8 — nén rồi kiểm chính gói (out đã tính ở cổng 4)
    tmp = tempfile.mkdtemp()
    try:
        zpath = os.path.join(tmp, 'p.plugin')
        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
            for dp, dn, fs in os.walk(root):
                dn[:] = [d for d in dn if d not in {'__pycache__', '.git'}]
                for f in fs:
                    if f.endswith(('.plugin', '.DS_Store', '.pyc')):
                        continue
                    full = os.path.join(dp, f)
                    # LUÔN dùng dấu gạch chéo xuôi — nén trên Windows sinh gạch ngược,
                    # trình giải nén hiểu là MỘT tên file và plugin nạp thiếu skill.
                    z.write(full, os.path.relpath(full, root).replace(os.sep, '/'))
        with zipfile.ZipFile(zpath) as z:
            names = z.namelist()
        bs = [n for n in names if '\\' in n]
        n_sk = sum(1 for n in names if n.endswith('SKILL.md'))
        size = os.path.getsize(zpath)
        gate(8, 'Gói đạt chuẩn', not bs and n_sk == len(dirs),
             f'{n_sk}/{len(dirs)} SKILL.md · {len(bs)} đường dẫn gạch ngược · {size // 1024} KB')
        if FAILS:
            print('\n❌ DỪNG — gói không đạt, không ghi ra ngoài.')
            return 1
        shutil.copy(zpath, out)
        print(f'\n✅ Chín cổng đạt. Đã ghi: {out}')
        print(f'   {name} v{ver} · {len(dirs)} skill · {size // 1024} KB')
        print('   Sau khi cài: xác nhận đủ số skill xuất hiện trước khi coi là phát hành xong.')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
