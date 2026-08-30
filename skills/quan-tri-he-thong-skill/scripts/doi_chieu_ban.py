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
