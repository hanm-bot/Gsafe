#!/usr/bin/env python3
"""Ca kiểm thử cho doi_chieu_ban.py — mỗi ca kiểm HAI CHIỀU."""
import json, os, subprocess, sys, tempfile, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from doi_chieu_ban import (
    tim_ban_dang_chay, doc_thu_muc, doc_goi, bam, so_sanh, xac_dinh_phat_hien,
)

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

def dung_plugin_moi(goc, marketplace, ten, skills=('a',)):
    """Dựng một thư mục plugin giả theo cấu trúc MỚI (app đổi chỗ cài):
    <goc>/plugins/marketplaces/<marketplace>/<ten>/.claude-plugin/plugin.json"""
    p = os.path.join(goc, 'plugins', 'marketplaces', marketplace, ten)
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

    # --- LOI 1: vi tri MOI (app da doi cho cai plugin sang plugins/marketplaces/) ---
    with tempfile.TemporaryDirectory() as t_moi:
        dung_plugin_moi(t_moi, 'local-desktop-app-uploads', 'sht-skills')
        kq_moi = tim_ban_dang_chay('sht-skills', t_moi)
        # Chieu 1 — phai tim thay ban o vi tri MOI
        ktra('Tim thay ban o vi tri MOI (plugins/marketplaces/.../.claude-plugin/plugin.json)',
             len(kq_moi) == 1)
        ktra('Duong dan vi tri MOI cung tro toi thu muc skills/',
             all(p.endswith('skills') for p in kq_moi))

    # --- LOI 1: CA HAI vi tri (CU + MOI) cung luc, duoi cung mot goc — khong dem trung ---
    with tempfile.TemporaryDirectory() as t_ca_hai:
        dung_plugin(t_ca_hai, 'FFF', 'sht-skills')          # kieu CU: rpm/plugin_FFF/...
        dung_plugin_moi(t_ca_hai, 'mkt', 'sht-skills')      # kieu MOI: plugins/marketplaces/mkt/sht-skills/...
        kq_ca_hai = tim_ban_dang_chay('sht-skills', t_ca_hai)
        # Chieu 1 — phai tim thay CA HAI ban, mot o moi kieu cau truc
        ktra('Tim thay ca hai vi tri (CU + MOI) duoi cung mot goc', len(kq_ca_hai) == 2)
        # Chieu 2 — khong duoc dem trung (danh sach khong co phan tu lap lai)
        ktra('Khong dem trung khi ca hai vi tri cung co ban', len(kq_ca_hai) == len(set(kq_ca_hai)))

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

        # Vong sua 1 — SKILL.md khong doc duoc (byte khong hop le UTF-8) khong duoc
        # lam sap doc_thu_muc; skill hop le canh no van phai doc duoc binh thuong.
        os.makedirs(os.path.join(d, 'sk_hop_le'), exist_ok=True)
        with open(os.path.join(d, 'sk_hop_le', 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write('dong 1\ndong 2\n')
        os.makedirs(os.path.join(d, 'sk_loi_encoding'), exist_ok=True)
        with open(os.path.join(d, 'sk_loi_encoding', 'SKILL.md'), 'wb') as f:
            f.write(b'\xff\xfe khong phai utf8')
        m_loi = doc_thu_muc(d)
        # Chiều 1 — khong nap, khong bao KeyError o buoc doc
        ktra('SKILL.md loi encoding: khong nap vao ket qua',
             'sk_loi_encoding' not in m_loi)
        # Chiều 2 — skill hop le canh no van duoc doc binh thuong, khong bi keo theo
        ktra('SKILL.md loi encoding: skill hop le canh ben van doc duoc',
             'sk_hop_le' in m_loi and m_loi['sk_hop_le'][0] == 2)

        z = os.path.join(t3, 'goi.plugin')
        with zipfile.ZipFile(z, 'w') as zf:
            zf.writestr('skills/sk1/SKILL.md', 'dong 1\ndong 2\ndong 3\n')
        g = doc_goi(z)
        ktra('Doc goi .plugin ra cung ket qua voi thu muc', g == m)
        ktra('Goi khong ton tai tra ve rong', doc_goi(os.path.join(t3, 'khong-co.plugin')) == {})

        # --- Task 3: phân loại phát hiện ---
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
        #
        # V2 co HAI nhanh doc lap trong so_sanh(): "goi THIEU mot skill co o nguon" va
        # "goi THUA mot skill khong co o nguon". Truoc day mot fixture (goi_thieu_sk1 =
        # {'sk_khac': ...}) kich CA HAI nhanh cung luc — vua thieu 'sk1' cua nguon, vua
        # thua 'sk_khac'. Tach thanh hai ca rieng de moi ca kiem dung MOT nhanh.
        A2 = {'sk1': (10, bam('a')), 'sk2': (5, bam('b'))}

        # Nhanh "thieu": goi co du 'sk2' nhung thieu 'sk1' cua nguon; khong co skill thua.
        goi_thieu_sk1 = {'sk2': (5, bam('b'))}
        kq_thieu = so_sanh(A2, goi_thieu_sk1, [A2])
        ktra('V2 khi goi thieu mot skill cua nguon (chi nhanh thieu)',
             any(x[0] == 'V2' and 'thiếu trong gói' in x[2] for x in kq_thieu))
        ktra('Nhanh thieu: khong lan sang thong bao cua nhanh thua',
             not any('không có ở nguồn' in x[2] for x in kq_thieu))

        # Nhanh "thua": goi co du ca 'sk1' va 'sk2' cua nguon, them 'sk3' ma nguon khong co.
        goi_thua_sk3 = {'sk1': (10, bam('a')), 'sk2': (5, bam('b')), 'sk3': (1, bam('c'))}
        kq_thua = so_sanh(A2, goi_thua_sk3, [A2])
        ktra('V2 khi goi thua mot skill nguon khong co (chi nhanh thua)',
             any(x[0] == 'V2' and 'không có ở nguồn' in x[2] for x in kq_thua))
        ktra('Nhanh thua: khong lan sang thong bao cua nhanh thieu',
             not any('thiếu trong gói' in x[2] for x in kq_thua))
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

        # --- LOI 2: "khong tim thay ban dang cai nao" phai la PHAT HIEN CAO (V0),
        # tuyet doi khong duoc bao "sach". Ca nay phai TRUOT neu bo ban va di.
        # Chieu no: chay=[] => phai co V0 muc CAO.
        kq_v0 = xac_dinh_phat_hien(A, {}, [])
        ktra('LOI 2 - chay rong thi phai co phat hien V0', 'V0' in ma(kq_v0))
        ktra('LOI 2 - V0 muc CAO', all(x[1] == 'CAO' for x in kq_v0 if x[0] == 'V0'))
        # Chieu im: co it nhat mot ban dang cai => KHONG duoc co V0
        kq_khong_v0 = xac_dinh_phat_hien(A, {}, [A])
        ktra('LOI 2 - da tim thay it nhat mot ban dang cai thi KHONG co V0',
             'V0' not in ma(kq_khong_v0))
        # V0 khong duoc chan phat hanh (giong V3/V4) — chi V1/V2 moi chan.
        # Mo phong dung logic 'chan' cua main() tren ket qua co V0.
        chan_gia_lap = [x for x in kq_v0 if x[0] in ('V1', 'V2')]
        ktra('LOI 2 - V0 khong bi tinh vao nhom chan phat hanh (V1/V2)', chan_gia_lap == [])

    # --- I-3: hai thu tu co (--goi truoc hay sau nguon) phai cho CUNG ket qua qua CLI ---
    # Truoc ban vá, gia tri cua --goi (khong bat dau bang '--') bi nhat vao args vi tri
    # khi dat TRUOC nguon (`--goi X <nguon>`), lam goc_nguon bi doc nham thanh X. Ca nay
    # phai truot neu bo ban vá o main() cua doi_chieu_ban.py.
    with tempfile.TemporaryDirectory() as t4:
        os.makedirs(os.path.join(t4, 'skills', 'sk1'), exist_ok=True)
        with open(os.path.join(t4, 'skills', 'sk1', 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write('dong 1\ndong 2\n')
        goi_path = os.path.join(t4, 'goi.plugin')
        with zipfile.ZipFile(goi_path, 'w') as zf:
            zf.writestr('skills/sk1/SKILL.md', 'dong 1\ndong 2\n')

        script = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'doi_chieu_ban.py')
        env = dict(os.environ, PYTHONUTF8='1')
        r_goi_truoc = subprocess.run(
            [sys.executable, script, '--goi', goi_path, t4],
            capture_output=True, text=True, encoding='utf-8', env=env)
        r_goi_sau = subprocess.run(
            [sys.executable, script, t4, '--goi', goi_path],
            capture_output=True, text=True, encoding='utf-8', env=env)
        ktra('I-3: --goi truoc hay sau nguon cho cung stdout',
             r_goi_truoc.stdout == r_goi_sau.stdout)
        ktra('I-3: --goi truoc hay sau nguon cho cung ma thoat',
             r_goi_truoc.returncode == r_goi_sau.returncode)
        # Khong khang dinh "sach" o day: main() con doi chieu voi MOI ban dang cai thuc
        # tren may (tim_ban_dang_chay() khong nhan tham so trong main()), nen may co cai
        # san sht-skills se tao ra V3/V4 hop le — khong lien quan gi den loi I-3. Thu doc
        # lap duy nhat can kiem la hai thu tu cho CUNG mot ket qua, da kiem ben tren.

    print(f'\n---- KET QUA: {DAT} dat / {TRUOT} truot ----')
    sys.exit(0 if TRUOT == 0 else 1)

if __name__ == '__main__':
    main()
