#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quét sức khỏe hệ thống skill SHT — 12 lớp lỗi E1..E12.

Dùng:
    python3 audit_skills.py <thư_mục_skills> [tuỳ chọn]

Tuỳ chọn:
    --personal DIR   thư mục skill cá nhân (cache) — bật kiểm E7
    --plugin DIR     thư mục gốc plugin (chứa .claude-plugin/) — bật kiểm E9
    --json           in kết quả dạng JSON

Thoát mã 1 nếu còn lỗi mức CAO.

LỊCH SỬ: bản E1–E6 chỉ soi nội dung BÊN TRONG các SKILL.md. Phiên nâng cấp
v0.9.0 có 4 lỗi thật thì nó bắt được 1 — ba lỗi lọt đều nằm ngoài phạm vi đó:
skill nằm sai chỗ (E7), Sổ đăng bạ lệch thực tế (E8), nguồn/gói bẩn (E9).
Đừng thu hẹp phạm vi trở lại.
"""
import sys, os, re, json, unicodedata
from itertools import combinations

OVERSIZE_LINES = 300
OVERLAP_TITLE = 0.55        # ngưỡng tương đồng TIÊU ĐỀ
OVERLAP_BODY = 0.35         # ngưỡng tương đồng NỘI DUNG — phải vượt cả hai mới báo
TRIGGER_PREFIX_WORDS = 6
DESC_MAX = 1024             # giới hạn cứng của save_skill

BUILTIN = {'docx', 'pptx', 'xlsx', 'pdf', 'schedule', 'morning', 'setup-cowork',
           'skill-creator', 'consolidate-memory', 'explain-usage', 'import-memory'}
SELF = 'quan-tri-he-thong-skill'
PLUGIN_ALLOWED = {'.claude-plugin', 'skills', 'README.md', 'agents',
                  '.mcp.json', 'CONNECTORS.md', 'hooks'}
STOP = {'va', 'cua', 'khi', 'cho', 'mot', 'cac', 'la', 'tren', 'truoc', 'sau',
        'voi', 'theo', 'trong', 'sht', 'skill', 'nay', 'khong', 'phai', 'duoc'}


def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower())
                if unicodedata.category(c) != 'Mn')
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9\s]', ' ', s)).strip()


def toks(s):
    return {w for w in norm(s).split() if len(w) > 2 and w not in STOP}


def jac(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def parse(path):
    lines = open(path, encoding='utf-8').read().splitlines()
    fm, i, blocks = {}, 0, 0
    while i + 1 < len(lines):
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i >= len(lines) or lines[i].strip() != '---':
            break
        close = next((j for j in range(i + 1, len(lines))
                      if lines[j].strip() == '---'), None)
        if close is None:
            break
        if blocks == 0:
            body = '\n'.join(lines[i + 1:close])
            m = re.search(r'^name:\s*["\']?([^"\'\n]+)', body, re.M)
            if m:
                fm['name'] = m.group(1).strip()
            m = re.search(r'^description:\s*(.*?)(?=\n[a-z_]+:|\Z)', body, re.M | re.S)
            if m:
                fm['description'] = re.sub(
                    r'\s+', ' ', m.group(1).strip().lstrip('>|-').strip('"\' '))
        blocks += 1
        i = close + 1

    # cắt thân theo từng mục để so nội dung, không chỉ so tiêu đề
    sections, cur, buf = [], None, []
    for l in lines:
        if re.match(r'^#{1,3}\s', l):
            if cur is not None:
                sections.append((cur, '\n'.join(buf)))
            cur, buf = l.lstrip('#').strip(), []
        elif cur is not None:
            buf.append(l)
    if cur is not None:
        sections.append((cur, '\n'.join(buf)))

    return {'raw': '\n'.join(lines), 'fm': fm, 'blocks': blocks,
            'n': len(lines), 'sections': sections,
            'h': [t for t, _ in sections]}


def read_registry(skills_dir):
    """Đọc Sổ đăng bạ. Trả list (tên_skill, tập_skill_khai_báo_dùng_chung).

    Sổ là DỮ LIỆU nên nằm ở references/so-dang-ba.md. Vẫn lùi về đọc trong
    SKILL.md để không gãy với bản cũ chưa tách file.
    """
    base = os.path.join(skills_dir, SELF)
    ref = os.path.join(base, 'references', 'so-dang-ba.md')
    if os.path.isfile(ref):
        txt, pat = open(ref, encoding='utf-8').read(), r'SỔ ĐĂNG BẠ.*'
    else:
        p = os.path.join(base, 'SKILL.md')
        if not os.path.isfile(p):
            return None
        txt, pat = open(p, encoding='utf-8').read(), r'PHỤ LỤC B.*'
    m = re.search(pat, txt, re.S)
    if not m:
        return None
    rows = []
    for line in m.group(0).splitlines():
        mm = re.match(r'^\|\s*`([a-z0-9-]+)`\s*\|(.*)$', line)
        if mm:
            cells = [c.strip() for c in mm.group(2).split('|')]
            declared = set(re.findall(r'`([a-z0-9-]{6,})`', cells[2] if len(cells) > 2 else ''))
            rows.append((mm.group(1), declared))
    return rows


def audit(root, personal=None, plugin_root=None):
    skills = {}
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d, 'SKILL.md')
        if os.path.isfile(p):
            skills[d] = parse(p)
    names = set(skills)
    F = []

    def add(sev, code, who, msg):
        F.append({'sev': sev, 'code': code, 'skill': who, 'msg': msg})

    out_ref = {k: set() for k in skills}
    in_ref = {k: set() for k in skills}

    for n, s in skills.items():
        # --- E1 frontmatter
        if not s['fm'].get('name'):
            add('CAO', 'E1', n, 'Thiếu hoặc không đọc được `name:`')
        elif s['fm']['name'] != n:
            add('CAO', 'E1', n, f"`name:` = \"{s['fm']['name']}\" lệch thư mục \"{n}\"")
        if s['blocks'] > 1:
            add('CAO', 'E1', n, f"{s['blocks']} khối frontmatter liên tiếp — khối thừa chảy vào nội dung")
        d = s['fm'].get('description')
        if not d:
            add('CAO', 'E1', n, 'Thiếu `description:` — skill không bao giờ tự kích hoạt')
        # --- E10 ngân sách description
        elif len(d) > DESC_MAX:
            add('CAO', 'E10', n,
                f'description {len(d)} ký tự — vượt giới hạn {DESC_MAX}, `save_skill` sẽ từ chối')
        elif len(d) > DESC_MAX * 0.93:
            add('THẤP', 'E10', n,
                f'description {len(d)}/{DESC_MAX} ký tự — sát trần, lần bổ sung tới sẽ vỡ')

        # --- E12 description thiếu VÙNG LOẠI TRỪ
        # §4 gọi đây là "phần bị bỏ quên nhiều nhất, và là thuốc chữa E6 hiệu quả
        # nhất". Thiếu nó thì hai skill cùng miền chắc chắn tranh nhau kích hoạt,
        # mà E6 chỉ bắt được khi câu MỞ ĐẦU trùng — bỏ lọt phần lớn ca thật.
        if d and n not in BUILTIN and not re.search(r'KHÔNG dùng|không dùng cho', d):
            add('THẤP', 'E12', n,
                'description thiếu vùng loại trừ ("KHÔNG dùng ... khi/cho ...") — '
                'phần chống tranh chấp kích hoạt với skill cùng miền')

        # --- E2 tham chiếu gãy
        # Dò theo TÊN THẬT của skill đang có, cộng thêm mẫu kebab tổng quát để bắt
        # tham chiếu tới skill không tồn tại. KHÔNG hardcode tiền tệ tên — bản cũ
        # chỉ nhận sht-/chuan-hoa-/quan-tri- nên mù hoàn toàn với ra-soat-hop-dong-vendor.
        cands = set(re.findall(r'`([a-z][a-z0-9]*(?:-[a-z0-9]+){2,})`', s['raw']))
        for other in names:
            if other != n and re.search(r'\b' + re.escape(other) + r'\b', s['raw']):
                cands.add(other)
        for c in cands:
            if c == n or len(c) < 6:
                continue
            if c in names:
                out_ref[n].add(c)
                in_ref[c].add(n)
                continue
            if any(r.startswith(c) for r in names):
                continue
            if n != SELF and not c.endswith(('.py', '.md', '.css', '.json')):
                add('CAO', 'E2', n, f'Trỏ tới skill `{c}` — KHÔNG tồn tại')

        # --- E5 quá khổ
        if n not in BUILTIN and s['n'] > OVERSIZE_LINES:
            add('TRUNG', 'E5', n,
                f"{s['n']} dòng — vượt ngưỡng {OVERSIZE_LINES}, tách phần tra cứu sang references/")
        elif n not in BUILTIN and s['n'] > OVERSIZE_LINES * 0.93:
            add('THẤP', 'E5', n,
                f"{s['n']}/{OVERSIZE_LINES} dòng — sát ngưỡng, lần bổ sung tới nên đẩy bớt sang references/")

    own = [n for n in skills if n not in BUILTIN]

    # --- E3 đảo cô lập / đảo một chiều
    for n in own:
        if len(own) <= 2 or n == SELF:
            continue
        if not out_ref[n] and not in_ref[n]:
            add('TRUNG', 'E3', n, 'Đảo cô lập — không trỏ ai, không ai trỏ tới')
        elif not in_ref[n] - {SELF}:
            add('THẤP', 'E3', n,
                'Đảo MỘT CHIỀU — nó trỏ đi nhưng không skill nghiệp vụ nào trỏ về, '
                'nên sẽ không được gọi kèm khi đang làm việc ở skill kia')

    # --- E4 overlap: phải trùng CẢ tiêu đề LẪN nội dung
    for a, b in combinations(sorted(skills), 2):
        if a in BUILTIN and b in BUILTIN:
            continue
        hits = []
        for t1, b1 in skills[a]['sections']:
            for t2, b2 in skills[b]['sections']:
                if len(toks(t1)) < 2:
                    continue
                if jac(toks(t1), toks(t2)) < OVERLAP_TITLE:
                    continue
                jb = jac(toks(b1), toks(b2))
                ptr = re.compile(r'theo `[a-z0-9-]+`|[Kk]hông định nghĩa lại|xem `[a-z0-9-]+`')
                if ptr.search(b1) and ptr.search(b2):
                    continue          # cả hai đều trỏ về một chủ sở hữu -> đúng chuẩn
                if jb >= OVERLAP_BODY:
                    hits.append(f'"{t1}" ≈ "{t2}" (nội dung {jb:.0%})')
        if hits:
            add('TRUNG', 'E4', f'{a} ↔ {b}',
                f'{len(hits)} mục trùng cả tiêu đề lẫn nội dung: ' + ' | '.join(hits[:3]))

    # --- E6 tranh chấp trigger
    for a, b in combinations(sorted(skills), 2):
        if a in BUILTIN and b in BUILTIN:
            continue
        da, db = skills[a]['fm'].get('description'), skills[b]['fm'].get('description')
        if not da or not db:
            continue
        pa = set(norm(da).split()[:TRIGGER_PREFIX_WORDS])
        pb = set(norm(db).split()[:TRIGGER_PREFIX_WORDS])
        if jac(pa, pb) >= 0.6:
            add('TRUNG', 'E6', f'{a} ↔ {b}', 'Description mở đầu gần trùng — tranh chấp kích hoạt')

    # --- E7 skill nhà nằm sai chỗ / tồn tại hai bản
    if personal and os.path.isdir(personal):
        for d in sorted(os.listdir(personal)):
            if d in BUILTIN or not os.path.isfile(os.path.join(personal, d, 'SKILL.md')):
                continue
            if d in names:
                add('CAO', 'E7', d,
                    'Tồn tại ĐỒNG THỜI bản cá nhân và bản trong plugin — hai đường bảo trì '
                    'song song, chắc chắn trôi. Xóa bản cá nhân, chỉ giữ bản plugin.')
            else:
                add('CAO', 'E7', d,
                    'Skill nhà nằm NGOÀI plugin (bản cá nhân) — không đi kèm khi chia sẻ '
                    'plugin, và sửa bằng save_skill sẽ tạo nhánh riêng. Đưa vào skills/ của plugin.')

    # --- E8 Sổ đăng bạ lệch thực tế
    rows = read_registry(root)
    reg = [r[0] for r in rows] if rows is not None else None
    if reg is not None:
        dup = sorted({x for x in reg if reg.count(x) > 1})
        if dup:
            add('CAO', 'E8', SELF,
                f'Sổ đăng bạ có hàng TRÙNG cho: {", ".join(dup)} — hai hàng cùng skill sẽ trôi khác nhau. '
                'Sửa hàng có sẵn, không append bảng mới ở cuối.')
        miss = sorted(set(own) - set(reg))
        if miss:
            add('CAO', 'E8', SELF,
                f'Chưa đăng ký trong Sổ: {", ".join(miss)} — sổ lệch thực tế nguy hiểm hơn không có sổ.')
        extra = sorted(set(reg) - set(own))
        if extra:
            add('TRUNG', 'E8', SELF,
                f'Sổ còn ghi skill không tồn tại: {", ".join(extra)}')

        # --- E11 Sổ khai báo quan hệ KHÔNG khớp tham chiếu thật trong SKILL.md
        # E8 chỉ kiểm TÊN có mặt trong sổ. Nhưng cột "Dùng chung với" mới là phần
        # kiến trúc được tuyên bố — nếu nó lệch tham chiếu thật thì sổ đang nói dối,
        # và người đọc sổ sẽ tin vào một sơ đồ không tồn tại.
        for nm, declared in rows:
            if nm not in skills or nm == SELF:
                continue
            ghost = sorted(d for d in declared if d in names and d not in out_ref.get(nm, set()))
            if ghost:
                add('TRUNG', 'E11', nm,
                    'Sổ khai báo dùng chung với ' + ', '.join(f'`{g}`' for g in ghost) +
                    ' nhưng SKILL.md KHÔNG hề nhắc tới — sổ mô tả một quan hệ không tồn tại. '
                    'Hoặc bổ sung con trỏ vào skill, hoặc sửa sổ cho đúng.')

    # --- E9 vệ sinh nguồn plugin
    if plugin_root and os.path.isdir(plugin_root):
        stray = [x for x in os.listdir(plugin_root)
                 if not x.startswith('.git') and x not in PLUGIN_ALLOWED]
        if stray:
            add('TRUNG', 'E9', os.path.basename(plugin_root.rstrip('/')),
                f'Nguồn plugin lẫn thứ không thuộc về: {", ".join(sorted(stray))} — '
                'sẽ bị gói vào bản phát hành. Nguồn chỉ chứa .claude-plugin/, skills/, README.md.')
        nested = []
        for dp, _, fns in os.walk(plugin_root):
            nested += [f for f in fns if f.endswith('.plugin')]
        if nested:
            add('CAO', 'E9', os.path.basename(plugin_root.rstrip('/')),
                f'Có {len(nested)} file .plugin nằm trong nguồn — bản phát hành sẽ bọc các bản '
                'phát hành trước, phình theo cấp số nhân.')

    rank = {'CAO': 0, 'TRUNG': 1, 'THẤP': 2}
    F.sort(key=lambda f: (rank[f['sev']], f['code'], f['skill']))
    return skills, F


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    root = args[0] if args else '.'

    def opt(flag):
        if flag in sys.argv:
            i = sys.argv.index(flag)
            if i + 1 < len(sys.argv):
                return sys.argv[i + 1]
        return None

    skills, F = audit(root, personal=opt('--personal'), plugin_root=opt('--plugin'))

    if '--json' in sys.argv:
        print(json.dumps(F, ensure_ascii=False, indent=2))
        return 1 if any(f['sev'] == 'CAO' for f in F) else 0

    print(f'Đã quét {len(skills)} skill tại {root}\n')
    if not F:
        print('✅ Sạch — không phát hiện vấn đề.')
        return 0
    cur = None
    for f in F:
        if f['sev'] != cur:
            cur = f['sev']
            print(f'\n───── MỨC {cur} ─────')
        print(f"[{f['code']}] {f['skill']}\n      {f['msg']}")
    hi = sum(1 for f in F if f['sev'] == 'CAO')
    print(f'\nTổng: {len(F)} phát hiện ({hi} mức CAO cần sửa ngay).')
    if not opt('--personal'):
        print('Lưu ý: chưa truyền --personal nên KHÔNG kiểm được E7 (skill nằm ngoài plugin).')
    if not opt('--plugin'):
        print('Lưu ý: chưa truyền --plugin nên KHÔNG kiểm được E9 (vệ sinh nguồn phát hành).')
    return 1 if hi else 0


if __name__ == '__main__':
    sys.exit(main())
