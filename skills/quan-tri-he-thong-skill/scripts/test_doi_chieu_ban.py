#!/usr/bin/env python3
"""Ca kiểm thử cho doi_chieu_ban.py — mỗi ca kiểm HAI CHIỀU."""
import json, os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doi_chieu_ban import tim_ban_dang_chay

DAT = TRUOT = 0

def ktra(nhan, dieu_kien):
    global DAT, TRUOT
    if dieu_kien:
        DAT += 1; print(f'  OK    {nhan}')
    else:
        TRUOT += 1; print(f'  TRUOT {nhan}')

def dung_plugin(goc, ma, ten, skills=('a',)):
    """Dựng một thư mục plugin giả giống cấu trúc rpm/plugin_*/."""
    p = os.path.join(goc, 'rpm', f'plugin_{ma}')
    os.makedirs(os.path.join(p, '.claude-plugin'), exist_ok=True)
    with open(os.path.join(p, '.claude-plugin', 'plugin.json'), 'w', encoding='utf-8') as f:
        json.dump({'name': ten, 'version': '1.0.0'}, f)
    for s in skills:
        os.makedirs(os.path.join(p, 'skills', s), exist_ok=True)
        with open(os.path.join(p, 'skills', s, 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write(f'---\nname: {s}\n---\n\nNoi dung.\n')
    return p

def main():
    with tempfile.TemporaryDirectory() as t:
        dung_plugin(t, 'AAA', 'sht-skills')
        dung_plugin(t, 'BBB', 'sht-skills')
        dung_plugin(t, 'CCC', 'plugin-khac')

        kq = tim_ban_dang_chay('sht-skills', t)
        # Chiều 1 — phải TÌM THẤY đúng 2 bản
        ktra('Tim thay dung 2 ban sht-skills', len(kq) == 2)
        ktra('Duong dan tro toi thu muc skills/', all(p.endswith('skills') for p in kq))
        # Chiều 2 — phải KHÔNG nhận nhầm plugin khác
        ktra('Khong nhan nham plugin-khac', all('CCC' not in p for p in kq))
        # Chiều 2 — tên không tồn tại thì trả rỗng, không nổ
        ktra('Ten khong ton tai tra ve rong', tim_ban_dang_chay('khong-co', t) == [])
        # Chống sập
        ktra('Thu muc khong ton tai tra ve rong',
             tim_ban_dang_chay('sht-skills', os.path.join(t, 'khong-co-that')) == [])

    print(f'\n---- KET QUA: {DAT} dat / {TRUOT} truot ----')
    sys.exit(0 if TRUOT == 0 else 1)

if __name__ == '__main__':
    main()
