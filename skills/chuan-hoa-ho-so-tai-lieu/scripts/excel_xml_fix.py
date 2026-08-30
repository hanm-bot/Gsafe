#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
excel_xml_fix.py — Ghi cached value vào file XML của .xlsx khi openpyxl không tự tính.
Giúp file Excel có sẵn giá trị xem trước khi mở bằng các công cụ preview.
"""
import sys, os, re, zipfile, tempfile, shutil

def fix_cached_values(xlsx_path, cell_values_dict, sheet_name="sheet1.xml"):
    """
    cell_values_dict: dict dạng {'C4': '7', 'C5': '0', 'C8': '7'}
    """
    tmp_dir = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(xlsx_path, 'r') as zin:
            zin.extractall(tmp_dir)
            
        sheet_path = os.path.join(tmp_dir, 'xl', 'worksheets', sheet_name)
        if os.path.exists(sheet_path):
            with open(sheet_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            def replace_cell(m):
                ref, whole = m.group(1), m.group(0)
                if '<f>' not in whole or ref not in cell_values_dict:
                    return whole
                return whole.replace('<v></v>', f'<v>{cell_values_dict[ref]}</v>')
                
            new_content = re.sub(r'<c r="([A-Z]+\d+)"[^>]*>.*?</c>', replace_cell, content)
            with open(sheet_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
        # Cập nhật workbook.xml để ép Excel tính toán lại khi mở
        wb_path = os.path.join(tmp_dir, 'xl', 'workbook.xml')
        if os.path.exists(wb_path):
            with open(wb_path, 'r', encoding='utf-8') as f:
                wb_content = f.read()
            if '<calcPr' not in wb_content:
                wb_content = wb_content.replace('</workbook>', '<calcPr calcId="124519" fullCalcOnLoad="1"/></workbook>')
                with open(wb_path, 'w', encoding='utf-8') as f:
                    f.write(wb_content)
                    
        # Đóng gói lại
        base_name = os.path.splitext(xlsx_path)[0]
        out_zip = base_name + '_fixed.xlsx'
        with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as zout:
            for root, _, files in os.walk(tmp_dir):
                for file in files:
                    full_p = os.path.join(root, file)
                    rel_p = os.path.relpath(full_p, tmp_dir)
                    zout.write(full_p, rel_p)
        print(f"Đã sửa và lưu tại: {out_zip}")
        return out_zip
    finally:
        shutil.rmtree(tmp_dir)

if __name__ == '__main__':
    print("Mô đun excel_xml_fix: Import và gọi hàm fix_cached_values(xlsx_path, cell_values_dict)")
