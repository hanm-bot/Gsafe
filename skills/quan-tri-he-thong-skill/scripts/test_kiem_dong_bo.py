#!/usr/bin/env python3
"""Ca kiểm thử cho kiem_dong_bo_ban_cai.py — mỗi ca kiểm HAI CHIỀU (phải nổ khi lệch, phải im khi khớp).

Dựng máy giả trong thư mục tạm: nguồn (không có git) · HOME giả (installed_plugins.json + cache) ·
APPDATA giả (rpm + skill cá nhân). Phần Git ở máy giả luôn "không kiểm được" (không có upstream),
nên ca khớp mong exit 2 do Git, còn các kênh khác phải không có dòng ✗.
"""
import json, os, shutil, subprocess, sys, tempfile

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kiem_dong_bo_ban_cai.py')
DAT = TRUOT = 0


def ktra(nhan, dieu_kien):
    global DAT, TRUOT
    if dieu_kien:
        DAT += 1; print(f'  OK    {nhan}')
    else:
        TRUOT += 1; print(f'  TRUOT {nhan}')


def dung_plugin(p, ver, skills, crlf=False):
    os.makedirs(os.path.join(p, '.claude-plugin'), exist_ok=True)
    with open(os.path.join(p, '.claude-plugin', 'plugin.json'), 'w', encoding='utf-8') as f:
        json.dump({'name': 'sht-skills', 'version': ver}, f)
    for s, nd in skills.items():
        os.makedirs(os.path.join(p, 'skills', s), exist_ok=True)
        with open(os.path.join(p, 'skills', s, 'SKILL.md'), 'w', encoding='utf-8', newline='') as f:
            f.write(nd.replace('\n', '\r\n') if crlf else nd)


def may_gia(goc, ver_code='1.0.0', ver_rpm='1.0.0', nd_rpm='A\n', ca_nhan=(), crlf_rpm=False):
    nguon = os.path.join(goc, 'nguon')
    dung_plugin(nguon, '1.0.0', {'a': 'A\n', 'b': 'B\n'})
    home, app = os.path.join(goc, 'home'), os.path.join(goc, 'app')
    cache = os.path.join(home, 'cache', ver_code)
    dung_plugin(cache, ver_code, {'a': 'A\n', 'b': 'B\n'})
    os.makedirs(os.path.join(home, '.claude', 'plugins'))
    with open(os.path.join(home, '.claude', 'plugins', 'installed_plugins.json'), 'w', encoding='utf-8') as f:
        json.dump({'plugins': {'sht-skills@sht-local': [{'version': ver_code, 'installPath': cache}]}}, f)
    s = os.path.join(app, 'Claude', 'local-agent-mode-sessions')
    dung_plugin(os.path.join(s, 'x', 'y', 'rpm', 'plugin_1'), ver_rpm, {'a': nd_rpm, 'b': 'B\n'}, crlf_rpm)
    cn = os.path.join(s, 'skills-plugin', 'y', 'x', 'skills')
    os.makedirs(cn)
    for d in ('docx',) + tuple(ca_nhan):
        os.makedirs(os.path.join(cn, d))
    return nguon, home, app


def chay(nguon, home, app):
    env = dict(os.environ, USERPROFILE=home, HOME=home, APPDATA=app, PYTHONIOENCODING='utf-8')
    r = subprocess.run([sys.executable, SCRIPT, '--nguon', nguon], capture_output=True,
                       text=True, encoding='utf-8', env=env)
    return r.returncode, r.stdout


def ca(nhan, **kw):
    goc = tempfile.mkdtemp()
    try:
        return chay(*may_gia(goc, **kw))
    finally:
        shutil.rmtree(goc, ignore_errors=True)


print('[1] Khớp hết (kể cả rpm ghi CRLF) → không có ✗, chỉ Git không kiểm được → exit 2')
rc, out = ca('khop', crlf_rpm=True)
ktra('exit 2', rc == 2)
ktra('không có dòng ✗', '✗' not in out)
ktra('báo rõ phần Git không kiểm được', 'KHÔNG KIỂM ĐƯỢC phần: git' in out)

print('[2] Cowork lệch phiên bản → exit 1, nêu cần tải lên tổ chức')
rc, out = ca('lech-ver', ver_rpm='0.9.0')
ktra('exit 1', rc == 1)
ktra('nêu tải lên thư viện tổ chức', 'tải gói 1.0.0 lên thư viện tổ chức' in out)

print('[3] Cùng phiên bản nhưng nội dung rpm khác → exit 1, chỉ đúng file')
rc, out = ca('lech-nd', nd_rpm='A cu\n')
ktra('exit 1', rc == 1)
ktra('chỉ ra a/SKILL.md', '[khác] a/SKILL.md' in out)
ktra('không chỉ nhầm b', '[khác] b/SKILL.md' not in out)

print('[4] Tab Code lệch phiên bản → exit 1')
rc, out = ca('lech-code', ver_code='0.9.0')
ktra('exit 1', rc == 1)

print('[5] Skill cá nhân trùng tên → exit 1, nêu tên; skill cá nhân không trùng thì im')
rc, out = ca('trung', ca_nhan=('a',))
ktra('exit 1', rc == 1)
ktra('nêu skill trùng', '✗ a' in out)
ktra('không nêu docx', '✗ docx' not in out)

print('[6] Không thấy kênh nào → exit 2, không báo khớp')
goc = tempfile.mkdtemp()
try:
    nguon = os.path.join(goc, 'nguon')
    dung_plugin(nguon, '1.0.0', {'a': 'A\n'})
    rc, out = chay(nguon, os.path.join(goc, 'trong'), os.path.join(goc, 'trong'))
finally:
    shutil.rmtree(goc, ignore_errors=True)
ktra('exit 2', rc == 2)
ktra('không in "✓ Khớp"', '✓ Khớp' not in out)

print('[7] Chạy với --nguon trỏ vào bản đã cài → từ chối, exit 2')
goc = tempfile.mkdtemp()
try:
    gia = os.path.join(goc, '.claude', 'plugins', 'cache', 'sht-skills')
    dung_plugin(gia, '1.0.0', {'a': 'A\n'})
    rc, out = chay(gia, goc, goc)
finally:
    shutil.rmtree(goc, ignore_errors=True)
ktra('exit 2', rc == 2)
ktra('nói rõ không phải nguồn', 'không phải nguồn' in out)

print(f'\n{DAT} đạt, {TRUOT} trượt')
sys.exit(1 if TRUOT else 0)
