#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render.py — Render file PlantUML (.puml) thành ảnh vector SVG.

Dùng server công khai plantuml.com (không cần cài Java/plantuml.jar cục bộ).
LƯU Ý: script này GỬI NGUYÊN VĂN nội dung file .puml ra internet (server
plantuml.com) mỗi lần chạy để render. Không dùng cho sơ đồ chứa dữ liệu
khách hàng nhạy cảm — chỉ dùng cho sơ đồ kiến trúc/luồng nghiệp vụ trừu
tượng (Use Case, Swimlane...) không có số liệu thật.

Cách dùng:
    python render.py "duong/dan/toi/file.puml"
    python render.py "duong/dan/toi/file.puml" --out "duong/dan/ra/anh.svg"
"""

import argparse
import io
import os
import sys
import urllib.error
import urllib.request
import zlib

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

# Bảng mã hoá 64 ký tự riêng của PlantUML — KHÁC base64 chuẩn (RFC 4648).
# Nguồn: thuật toán mã hoá chính thức của plantuml.com.
_PLANTUML_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"


def _encode6bit(b: int) -> str:
    return _PLANTUML_ALPHABET[b & 0x3F]


def _append3bytes(b1: int, b2: int, b3: int) -> str:
    c1 = b1 >> 2
    c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
    c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
    c4 = b3 & 0x3F
    return _encode6bit(c1) + _encode6bit(c2) + _encode6bit(c3) + _encode6bit(c4)


def encode_plantuml(text: str) -> str:
    """Nén deflate (raw, không header zlib) rồi mã hoá theo bảng chữ PlantUML."""
    data = text.encode("utf-8")
    compressor = zlib.compressobj(9, zlib.DEFLATED, -15)
    compressed = compressor.compress(data) + compressor.flush()

    out = []
    i = 0
    n = len(compressed)
    while i < n:
        b1 = compressed[i]
        b2 = compressed[i + 1] if i + 1 < n else 0
        b3 = compressed[i + 2] if i + 2 < n else 0
        out.append(_append3bytes(b1, b2, b3))
        i += 3
    return "".join(out)


def render_puml_to_svg(puml_path: str, out_path: str = None, server: str = "https://www.plantuml.com/plantuml") -> str:
    if not os.path.exists(puml_path):
        raise FileNotFoundError(f"Không tìm thấy file: {puml_path}")

    with open(puml_path, "r", encoding="utf-8") as f:
        text = f.read()

    if not out_path:
        out_path = os.path.splitext(puml_path)[0] + ".svg"

    encoded = encode_plantuml(text)
    url = f"{server}/svg/{encoded}"

    print(f"[*] Đang gửi sơ đồ tới {server} để render SVG ...")
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) usecase-diagram-skill/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status != 200:
                raise RuntimeError(f"Server trả về mã lỗi HTTP {resp.status}")
            svg_bytes = resp.read()
    except urllib.error.URLError as ex:
        raise RuntimeError(
            f"Không gọi được server plantuml.com — kiểm tra kết nối mạng. Chi tiết: {ex}"
        ) from ex

    os.makedirs(os.path.dirname(os.path.abspath(out_path)) or ".", exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(svg_bytes)

    print(f"[+] Đã render xong -> {out_path}")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Render file PlantUML (.puml) thành SVG qua plantuml.com")
    parser.add_argument("puml_file", help="Đường dẫn file .puml đầu vào")
    parser.add_argument("--out", default=None, help="Đường dẫn file .svg đầu ra (mặc định: cùng tên, đổi đuôi .svg)")
    args = parser.parse_args()

    try:
        render_puml_to_svg(args.puml_file, args.out)
    except Exception as ex:
        print(f"[LỖI] {ex}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
