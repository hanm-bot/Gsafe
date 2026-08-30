#!/usr/bin/env python3
"""
doi_chieu_ban.py — Lớp 1 QA: đối chiếu ba phiên bản của plugin sht-skills.

So: thư mục nguồn · gói .plugin · MỌI bản đang cài.
Dò bản đang cài theo TÊN trong .claude-plugin/plugin.json, không hardcode đường dẫn —
ID phiên và ID plugin đổi mỗi lần cài lại, tên thì không.

Thoát mã 1 nếu có phát hiện V1 hoặc V2 (mức chặn phát hành).
"""
import glob
import json
import os

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
                if json.load(fh).get('name') != ten_plugin:
                    continue
        except (OSError, ValueError):
            continue  # manifest hỏng thì bỏ qua, không làm chết cả lần quét
        thu_muc_skills = os.path.join(os.path.dirname(os.path.dirname(f)), 'skills')
        if os.path.isdir(thu_muc_skills):
            ket_qua.append(thu_muc_skills)
    return sorted(ket_qua)
