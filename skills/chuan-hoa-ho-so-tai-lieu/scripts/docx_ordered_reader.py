#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
docx_ordered_reader.py — Đọc file .docx giữ nguyên thứ tự đoạn văn và bảng biểu.
Dùng duyệt iterchildren() để không bị tách rời bảng khỏi đoạn văn dẫn nhập.
"""
import sys
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

def read_docx(docx_path, out_txt_path):
    d = Document(docx_path)
    out = []
    table_idx = 0
    for child in d.element.body.iterchildren():
        if child.tag.endswith('}p'):
            p = Paragraph(child, d)
            text = p.text.strip()
            if text:
                out.append(f"[{p.style.name}] {text}")
        elif child.tag.endswith('}tbl'):
            tb = Table(child, d)
            out.append(f"=== TABLE {table_idx} ===")
            for r in tb.rows:
                row_str = " || ".join(c.text.strip().replace('\n', ' | ') for c in r.cells)
                out.append(row_str)
            out.append(f"=== /TABLE {table_idx} ===")
            table_idx += 1
            
    with open(out_txt_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(out))
    print(f"Đã xuất: {out_txt_path} ({len(out)} dòng)")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Sử dụng: python docx_ordered_reader.py <input.docx> <output.txt>")
        sys.exit(1)
    read_docx(sys.argv[1], sys.argv[2])
