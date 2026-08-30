#!/usr/bin/env python3
"""
doi_chieu_ban.py — Lớp 1 QA: đối chiếu ba phiên bản của plugin sht-skills.

So: thư mục nguồn · gói .plugin · MỌI bản đang cài.
Dò bản đang cài theo TÊN trong .claude-plugin/plugin.json, không hardcode đường dẫn —
ID phiên và ID plugin đổi mỗi lần cài lại, tên thì không.

Thoát mã 1 nếu có phát hiện V1 hoặc V2 (mức chặn phát hành).
"""
import glob
import hashlib
import json
import os
import zipfile

GOC_MAC_DINH = os.path.expandvars(
    r'%APPDATA%\Claude\local-agent-mode-sessions')


def tim_ban_dang_chay(ten_plugin='sht-skills', goc=None):
    """Trả về danh sách thư mục skills/ của mọi bản đang cài mang tên ten_plugin."""
    goc = goc or GOC_MAC_DINH
    ket_qua = []
    mau = os.path.join(goc, '**', 'rpm', 'plugin_*', '.claude-plugin', 'plugin.json')
    for f in glob.glob(mau, recursive=True):
        try:
            with open(f, encoding='utf-8') as fh:
                du_lieu = json.load(fh)
            if not isinstance(du_lieu, dict) or du_lieu.get('name') != ten_plugin:
                continue
        except (OSError, ValueError):
            continue  # manifest hỏng thì bỏ qua, không làm chết cả lần quét
        thu_muc_skills = os.path.join(os.path.dirname(os.path.dirname(f)), 'skills')
        if os.path.isdir(thu_muc_skills):
            ket_qua.append(thu_muc_skills)
    return sorted(ket_qua)


def bam(noi_dung):
    """sha256 của nội dung đã chuẩn hoá xuống dòng — CRLF và LF cho cùng kết quả."""
    chuan = noi_dung.replace('\r\n', '\n').replace('\r', '\n')
    return hashlib.sha256(chuan.encode('utf-8')).hexdigest()


def _do(noi_dung):
    """Đếm số dòng theo số ký tự xuống dòng (cùng quy ước với `wc -l`), rồi băm.

    Đây là quy ước CÓ CHỦ ĐÍCH, không phải lỗi: file KHÔNG kết thúc bằng newline sẽ ra
    ít hơn số dòng văn bản thực tế MỘT đơn vị — giống hệt cách `wc -l` đếm. Chọn quy ước
    này để so_dong công cụ in ra khớp với bảng số liệu trong tài liệu thiết kế
    (273 / 258 / 173 / 153 dòng), vì bảng đó cũng được sinh bằng `wc -l`. so_dong chỉ
    phục vụ người đọc ước lượng mức lệch giữa các bản; thứ quyết định hai bản có khác
    nhau hay không là hash, và hash không bị ảnh hưởng bởi quy ước đếm dòng này.
    """
    return (noi_dung.replace('\r\n', '\n').count('\n'), bam(noi_dung))


def doc_thu_muc(thu_muc):
    """{ten_skill: (so_dong, hash)} đọc từ một thư mục skills/."""
    ket_qua = {}
    if not os.path.isdir(thu_muc):
        return ket_qua
    for ten in sorted(os.listdir(thu_muc)):
        f = os.path.join(thu_muc, ten, 'SKILL.md')
        if os.path.isfile(f):
            with open(f, encoding='utf-8') as fh:
                ket_qua[ten] = _do(fh.read())
    return ket_qua


def doc_goi(duong_dan_plugin):
    """{ten_skill: (so_dong, hash)} đọc từ file .plugin (zip)."""
    ket_qua = {}
    if not os.path.isfile(duong_dan_plugin):
        return ket_qua
    try:
        with zipfile.ZipFile(duong_dan_plugin) as zf:
            for ten_file in zf.namelist():
                phan = ten_file.replace('\\', '/').split('/')
                if len(phan) >= 3 and phan[-3] == 'skills' and phan[-1] == 'SKILL.md':
                    ket_qua[phan[-2]] = _do(zf.read(ten_file).decode('utf-8'))
    except (OSError, zipfile.BadZipFile):
        return {}
    return ket_qua


def so_sanh(nguon, goi, chay):
    """Trả về [(ma, muc, mo_ta)]. V1/V2 chặn phát hành; V3/V4 chỉ báo."""
    pd = []

    # V2 — thiếu/thừa skill giữa nguồn và gói
    if goi:
        thieu = sorted(set(nguon) - set(goi))
        thua = sorted(set(goi) - set(nguon))
        for s in thieu:
            pd.append(('V2', 'CAO', f'{s}: có ở nguồn, thiếu trong gói .plugin'))
        for s in thua:
            pd.append(('V2', 'CAO', f'{s}: có trong gói .plugin, không có ở nguồn'))

        # V1 — cùng tên nhưng nội dung khác
        for s in sorted(set(nguon) & set(goi)):
            if nguon[s][1] != goi[s][1]:
                pd.append(('V1', 'CAO',
                           f'{s}: nguồn {nguon[s][0]} dòng ≠ gói {goi[s][0]} dòng'))

    # V2 — skill có ở bản đang chạy nhưng THIẾU ở nguồn.
    # Đây là dấu hiệu chắc chắn đang đóng gói từ nguồn khuyết → nuốt ngược
    # bản đang chạy. Chặn phát hành. (Ruling R4)
    da_bao = set()
    for i, b in enumerate(chay):
        for s in sorted(set(b) - set(nguon)):
            if s not in da_bao:
                da_bao.add(s)
                pd.append(('V2', 'CAO',
                           f'{s}: có ở bản đang chạy #{i + 1}, THIẾU ở nguồn — '
                           f'đóng gói lúc này sẽ xoá skill khỏi bản cài'))

    # V3 — nguồn khác bản đang chạy
    for i, b in enumerate(chay):
        for s in sorted(set(nguon) & set(b)):
            if nguon[s][1] != b[s][1]:
                pd.append(('V3', 'TRUNG',
                           f'{s}: nguồn {nguon[s][0]} dòng ≠ bản chạy #{i + 1} {b[s][0]} dòng'))

    # V4 — hai bản đang chạy khác nhau
    for i in range(len(chay)):
        for j in range(i + 1, len(chay)):
            for s in sorted(set(chay[i]) & set(chay[j])):
                if chay[i][s][1] != chay[j][s][1]:
                    pd.append(('V4', 'CAO',
                               f'{s}: bản chạy #{i + 1} ({chay[i][s][0]} dòng) '
                               f'≠ bản chạy #{j + 1} ({chay[j][s][0]} dòng)'))
    return pd


def main():
    import sys
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    goc_nguon = os.path.abspath(args[0] if args else '.')
    nguon = doc_thu_muc(os.path.join(goc_nguon, 'skills'))
    duong_dan_goi = sys.argv[sys.argv.index('--goi') + 1] if '--goi' in sys.argv else ''
    goi = doc_goi(duong_dan_goi) if duong_dan_goi else {}
    chay = [doc_thu_muc(p) for p in tim_ban_dang_chay()]

    pd = so_sanh(nguon, goi, chay)
    if not pd:
        print(f'ĐỐI CHIẾU BẢN — sạch. {len(nguon)} skill, {len(chay)} bản đang cài.')
        return 0

    print(f'ĐỐI CHIẾU BẢN — {len(pd)} phát hiện\n')
    for ma, muc, mo_ta in pd:
        print(f'  [{ma}] {muc:5} {mo_ta}')
    chan = [x for x in pd if x[0] in ('V1', 'V2')]
    print(f'\n{len(chan)} phát hiện mức chặn phát hành (V1/V2).')
    return 1 if chan else 0


if __name__ == '__main__':
    raise SystemExit(main())
