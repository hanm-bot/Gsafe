#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
safe_rename.py — Thay thế tên/cụm từ hàng loạt AN TOÀN cho văn bản tiếng Việt.

Vấn đề nó giải quyết:
    Tên người Việt trùng âm tiết với địa danh và từ vựng thông thường.
    Find/replace ngây thơ sẽ tạo ra "Anh Hà Giang", "Thái Anh Nguyên",
    "Anh Phương pháp" — những lỗi đi thẳng vào văn bản trình ký.

Cách dùng:
    # 1. Xem trước (LUÔN chạy bước này đầu tiên)
    python safe_rename.py --file bienban.js --rules rules.json --dry-run

    # 2. Áp dụng sau khi đã duyệt
    python safe_rename.py --file bienban.js --rules rules.json --apply

    # 3. Quét lỗi sau khi áp dụng
    python safe_rename.py --file bienban.js --audit

Định dạng rules.json:
{
  "protect": [
    "Hà Giang", "Đông Hà Nội", "Thái Nguyên", "Yên Bái",
    "phương pháp", "phương án", "an toàn", "an ninh",
    "khoa học", "Việt Nam", "nguyên tắc", "nguyên nhân", "thảo luận"
  ],
  "rename": [
    {"from": "Hà",      "to": "Anh Hà"},
    {"from": "Chiến",   "to": "Anh Chiến"},
    {"from": "Phương",  "to": "Anh Phương"},
    {"from": "An",      "to": "Chị An"},
    {"from": "Thanh Huyền", "to": "Chị Thanh Huyền"}
  ]
}

Nguyên tắc hoạt động:
    - Cụm trong "protect" được đóng băng (thay bằng placeholder) TRƯỚC khi
      chạy rename, rồi khôi phục lại sau. Nhờ vậy "Hà Giang" không bao giờ
      bị đụng tới khi đổi "Hà".
    - Rule dài được xử lý trước rule ngắn ("Thanh Huyền" trước "Huyền").
    - Không thay nếu vị trí đó đã mang sẵn tiền tố đích (tránh "Anh Anh Hà").
"""

import argparse
import json
import re
import sys
import unicodedata

# Ký tự riêng tư (Unicode Private Use Area) làm placeholder — gần như
# không bao giờ xuất hiện trong văn bản thật.
PLACEHOLDER_START = 0xE000


def freeze(text, protected):
    """Đóng băng các cụm bảo vệ thành placeholder. Trả về (text, mapping).

    Khớp KHÔNG phân biệt hoa/thường (để bắt cả "Phương pháp" đầu câu và
    "ĐÔNG HÀ NỘI" trong tiêu đề), nhưng giữ nguyên dạng chữ gốc khi khôi phục.
    """
    mapping = {}
    counter = [0]

    def make_token(matched):
        # Mỗi biến thể hoa/thường được một token riêng để khôi phục chính xác
        for tok, val in mapping.items():
            if val == matched:
                return tok
        tok = chr(PLACEHOLDER_START + counter[0])
        counter[0] += 1
        mapping[tok] = matched
        return tok

    # Cụm dài trước để "Đông Hà Nội" được bắt trước "Hà Nội"
    for phrase in sorted(protected, key=len, reverse=True):
        # \b không đáng tin với tiếng Việt có dấu -> dùng lookaround theo ký tự chữ
        pattern = r'(?<![^\W\d_])' + re.escape(phrase) + r'(?![^\W\d_])'
        text = re.sub(pattern,
                      lambda m: make_token(m.group()),
                      text,
                      flags=re.IGNORECASE)
    return text, mapping


def thaw(text, mapping):
    """Khôi phục placeholder về cụm gốc."""
    for token, phrase in mapping.items():
        text = text.replace(token, phrase)
    return text


def word_pattern(word):
    """Ranh giới từ hoạt động đúng với chữ có dấu tiếng Việt."""
    return r'(?<![^\W\d_])' + re.escape(word) + r'(?![^\W\d_])'


def apply_rules(text, rules, protected):
    """Áp dụng rename an toàn. Trả về (text_mới, danh_sách_thay_đổi)."""
    text, mapping = freeze(text, protected)
    changes = []

    # Rule dài trước
    for rule in sorted(rules, key=lambda r: len(r['from']), reverse=True):
        src, dst = rule['from'], rule['to']
        # Bỏ qua nếu đã mang sẵn tiền tố đích (VD "Anh Hà" khi đổi "Hà"->"Anh Hà")
        prefix = dst[: -len(src)] if dst.endswith(src) and len(dst) > len(src) else None
        pattern = word_pattern(src)
        if prefix:
            pattern = r'(?<!' + re.escape(prefix) + r')' + pattern

        for m in re.finditer(pattern, text):
            s = max(0, m.start() - 35)
            e = min(len(text), m.end() + 35)
            changes.append({
                'from': src,
                'to': dst,
                'context': thaw(text[s:e], mapping).replace('\n', ' '),
            })
        text = re.sub(pattern, dst, text)

    return thaw(text, mapping), changes


def audit(text, rules=None):
    """Quét các mẫu lỗi thường gặp sau khi rename."""
    problems = []

    # Tiền tố lặp
    for bad in ['Anh Anh', 'Chị Chị', 'chị Chị', 'anh Anh', 'Anh Chị', 'Chị Anh',
                'Ông Ông', 'Bà Bà', 'VTB VTB']:
        for m in re.finditer(re.escape(bad), text):
            s = max(0, m.start() - 35)
            e = min(len(text), m.end() + 35)
            problems.append((bad, text[s:e].replace('\n', ' ')))

    # Tiền tố dính vào từ viết thường (dấu hiệu bắt nhầm danh từ chung)
    for m in re.finditer(r'(?:Anh|Chị) [A-ZĐÀ-Ỹ][a-zà-ỹ]+ [a-zà-ỹ]{3,}', text):
        frag = m.group()
        # heuristic: "Anh Phương pháp", "Chị An toàn"
        tail = frag.split()[-1]
        if tail in ('pháp', 'án', 'toàn', 'ninh', 'học', 'tắc', 'nhân', 'luận', 'trình'):
            problems.append(('tiền tố dính danh từ chung', frag))

    return problems


def check_uppercase(text, rules):
    """Cảnh báo nguồn đổi tên xuất hiện dạng VIẾT HOA trong file.

    Tình huống thật: đổi "Đông Hà Nội" -> "VTB Đông Hà Nội" nhưng tiêu đề
    ghi "DỰ ÁN ĐÔNG HÀ NỘI" (viết hoa) nên regex phân biệt hoa/thường bỏ sót.
    Đây là lỗi rất dễ lọt tới bản trình ký.
    """
    warnings = []
    for rule in rules:
        src = rule['from']
        upper = src.upper()
        if upper != src and upper in text:
            warnings.append((src, rule['to']))
    return warnings


def strip_accents_upper(s):
    return unicodedata.normalize('NFC', s).upper()


def main():
    ap = argparse.ArgumentParser(description='Thay thế tên hàng loạt an toàn.')
    ap.add_argument('--file', required=True, help='File cần xử lý')
    ap.add_argument('--rules', help='File rules.json')
    ap.add_argument('--dry-run', action='store_true', help='Chỉ xem trước, không ghi')
    ap.add_argument('--apply', action='store_true', help='Ghi thay đổi vào file')
    ap.add_argument('--audit', action='store_true', help='Chỉ quét lỗi trong file hiện tại')
    args = ap.parse_args()

    with open(args.file, encoding='utf-8') as f:
        text = f.read()

    if args.audit:
        problems = audit(text)
        if not problems:
            print('✓ Không phát hiện lỗi tiền tố lặp / dính danh từ chung.')
        else:
            print(f'✗ Phát hiện {len(problems)} vấn đề:\n')
            for kind, ctx in problems:
                print(f'  [{kind}] ...{ctx}...')
        return 0 if not problems else 1

    if not args.rules:
        ap.error('--rules bắt buộc khi không dùng --audit')

    with open(args.rules, encoding='utf-8') as f:
        cfg = json.load(f)
    protected = cfg.get('protect', [])
    rules = cfg.get('rename', [])

    new_text, changes = apply_rules(text, rules, protected)

    print(f'Số vị trí sẽ thay đổi: {len(changes)}\n')
    grouped = {}
    for c in changes:
        grouped.setdefault((c['from'], c['to']), []).append(c['context'])
    for (src, dst), ctxs in sorted(grouped.items(), key=lambda kv: -len(kv[1])):
        print(f'  {src!r} -> {dst!r}  ({len(ctxs)} vị trí)')
        for ctx in ctxs[:3]:
            print(f'      ...{ctx}...')
        if len(ctxs) > 3:
            print(f'      ... và {len(ctxs) - 3} vị trí khác')
        print()

    # Cảnh báo viết hoa
    up = check_uppercase(text, rules)
    if up:
        print('⚠ CẢNH BÁO: các cụm cần đổi sau còn xuất hiện dạng VIẾT HOA —')
        print('  phép thay ở trên KHÔNG bắt được, phải sửa tiêu đề thủ công:')
        for src, dst in up:
            print(f'    - {src.upper()}   → cần sửa thành: {dst.upper()}')
        print()

    # Quét lỗi trên kết quả
    problems = audit(new_text)
    if problems:
        print(f'⚠ Kết quả sau thay thế có {len(problems)} vấn đề cần xem lại:')
        for kind, ctx in problems:
            print(f'    [{kind}] ...{ctx}...')
        print()

    if args.apply:
        with open(args.file, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print(f'✓ Đã ghi thay đổi vào {args.file}')
        print('  Bước tiếp theo: render file ra ảnh và KIỂM TRA BẰNG MẮT trang nhiều tên nhất.')
    else:
        print('(Chế độ xem trước — chưa ghi gì. Dùng --apply để áp dụng.)')

    return 0


if __name__ == '__main__':
    sys.exit(main())
