#!/usr/bin/env python3
"""Ca kiểm thử cho doi_chieu_ban.py — mỗi ca kiểm HAI CHIỀU."""
import json, os, sys, tempfile, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doi_chieu_ban import tim_ban_dang_chay, doc_thu_muc, doc_goi, bam

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

def dung_plugin_json_tho(goc, ma, noi_dung):
    """Dựng plugin.json cú pháp hợp lệ nhưng KHÔNG phải object (list/null/chuoi/so)."""
    p = os.path.join(goc, 'rpm', f'plugin_{ma}')
    os.makedirs(os.path.join(p, '.claude-plugin'), exist_ok=True)
    with open(os.path.join(p, '.claude-plugin', 'plugin.json'), 'w', encoding='utf-8') as f:
        json.dump(noi_dung, f)
    return p

def main():
    with tempfile.TemporaryDirectory() as t:
        dung_plugin(t, 'AAA', 'sht-skills')
        dung_plugin(t, 'BBB', 'sht-skills')
        dung_plugin(t, 'CCC', 'plugin-khac')
        # plugin.json là [] — hợp lệ cú pháp nhưng không phải object; đứng cạnh 2 bản hợp lệ
        dung_plugin_json_tho(t, 'DDD', [])

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
        # Chiều 2 — plugin.json khong phai object (vi du bi ghi de/cat cut) khong duoc lam sap
        # vong quet, va khong duoc nhan nham la ban hop le
        ktra('plugin.json khong phai object: khong sap, khong nhan nham',
             len(kq) == 2 and all('DDD' not in p for p in kq))

    # Ca rieng — chung minh vong quet khong phu thuoc so tang ID phien:
    # duong dan thuc tren may co HAI tang ID long nhau truoc rpm/, vd:
    # local-agent-mode-sessions/<id-1>/<id-2>/rpm/plugin_X/
    with tempfile.TemporaryDirectory() as t2:
        goc_long_id_phien = os.path.join(t2, 'id-phien-1', 'id-phien-2')
        dung_plugin(goc_long_id_phien, 'EEE', 'sht-skills')
        kq2 = tim_ban_dang_chay('sht-skills', t2)
        # Chiều 1 — phải tìm thấy dù bản nằm sau hai tầng ID phiên lồng nhau
        ktra('Tim thay ban nam sau 2 tang ID phien long nhau (dung dang may thuc)',
             len(kq2) == 1)

    # --- Task 2: đọc thư mục và băm — khối riêng, không mượn thư mục tạm đã đóng ---
    with tempfile.TemporaryDirectory() as t3:
        d = os.path.join(t3, 'nguon')
        os.makedirs(os.path.join(d, 'sk1'), exist_ok=True)
        with open(os.path.join(d, 'sk1', 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write('dong 1\ndong 2\ndong 3\n')
        m = doc_thu_muc(d)
        ktra('Doc dung so dong', m['sk1'][0] == 3)
        ktra('Hash la chuoi 64 ky tu', len(m['sk1'][1]) == 64)

        # Quy uoc dem dong CO CHU DICH cua _do(): giong wc -l, khop bang so lieu trong
        # tai lieu thiet ke. Kiem qua doc_thu_muc (duong di thuc), khong goi _do truc tiep.
        os.makedirs(os.path.join(d, 'sk_co_newline_cuoi'), exist_ok=True)
        with open(os.path.join(d, 'sk_co_newline_cuoi', 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write('a\nb\nc\n')
        os.makedirs(os.path.join(d, 'sk_thieu_newline_cuoi'), exist_ok=True)
        with open(os.path.join(d, 'sk_thieu_newline_cuoi', 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write('a\nb\nc')
        m_quy_uoc = doc_thu_muc(d)
        # Chiều 1 — co newline cuoi thi dem dung so dong van ban
        ktra('Co newline cuoi: dem dung 3 dong', m_quy_uoc['sk_co_newline_cuoi'][0] == 3)
        # Chiều 2 — thieu newline cuoi thi ra it hon 1, dung y do (quy uoc wc -l)
        ktra('Dem dong theo quy uoc wc -l: thieu newline cuoi thi ra 2, dung y do',
             m_quy_uoc['sk_thieu_newline_cuoi'][0] == 2)

        # Chiều 2 — nội dung khác thì hash phải khác
        ktra('Noi dung khac -> hash khac', bam('a\n') != bam('b\n'))
        # Chiều 2 — chỉ khác kiểu xuống dòng thì hash phải GIỐNG
        ktra('CRLF va LF cho cung hash', bam('a\r\nb\r\n') == bam('a\nb\n'))

        z = os.path.join(t3, 'goi.plugin')
        with zipfile.ZipFile(z, 'w') as zf:
            zf.writestr('skills/sk1/SKILL.md', 'dong 1\ndong 2\ndong 3\n')
        g = doc_goi(z)
        ktra('Doc goi .plugin ra cung ket qua voi thu muc', g == m)
        ktra('Goi khong ton tai tra ve rong', doc_goi(os.path.join(t3, 'khong-co.plugin')) == {})

        # --- Task 3: phân loại phát hiện ---
        from doi_chieu_ban import so_sanh
        A = {'sk1': (10, bam('a'))}
        B = {'sk1': (10, bam('b'))}
        ma = lambda kq: {x[0] for x in kq}

        ktra('Giong het -> khong phat hien gi', so_sanh(A, A, [A]) == [])
        ktra('V1 khi nguon khac goi', 'V1' in ma(so_sanh(A, B, [A])))
        # goi rong {} nghia la "khong duoc cung cap" (khop main(): khong co --goi thi
        # goi={}) nen bi guard "if goi:" bo qua co tinh, tranh bao gia tran lan. De kiem
        # dung "goi THIEU mot skill" phai dung goi CO noi dung nhung thieu dung skill do,
        # khong the dung {} vi {} trung nghia voi "chua cung cap" (xung dot voi ca
        # 'Khong bao V2 khi nguon du skill' o duoi, cung dung goi={} nhung ky vong V2
        # KHONG xuat hien — hai ky vong doi lap tren cung mot gia tri {} khong the cung
        # dung, da kiem chung bang cach bo guard: bo guard thi ca do lai trot).
        goi_thieu_sk1 = {'sk_khac': (5, bam('c'))}
        ktra('V2 khi goi thieu skill', 'V2' in ma(so_sanh(A, goi_thieu_sk1, [A])))
        ktra('V3 khi nguon khac ban dang chay', 'V3' in ma(so_sanh(A, A, [B])))
        ktra('V4 khi hai ban dang chay khac nhau', 'V4' in ma(so_sanh(A, A, [A, B])))
        # Chiều 2 — không báo nhầm
        ktra('Khong bao V4 khi chi co mot ban chay', 'V4' not in ma(so_sanh(A, A, [A])))
        ktra('Khong bao V1 khi goi trung nguon', 'V1' not in ma(so_sanh(A, A, [B])))
        ktra('Khong co ban chay -> khong nen sap', isinstance(so_sanh(A, A, []), list))
        # Ruling R4 — skill co o ban dang chay nhung THIEU o nguon => V2 (chan)
        AB = {'sk1': (10, bam('a')), 'sk2': (5, bam('c'))}
        ktra('V2 khi nguon thieu skill ma ban chay co', 'V2' in ma(so_sanh(A, {}, [AB])))
        ktra('Khong bao V2 khi nguon du skill', 'V2' not in ma(so_sanh(AB, {}, [AB])))

    print(f'\n---- KET QUA: {DAT} dat / {TRUOT} truot ----')
    sys.exit(0 if TRUOT == 0 else 1)

if __name__ == '__main__':
    main()
