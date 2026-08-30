#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tự kiểm audit_skills.py bằng bộ ca dựng sẵn.

Chạy: python3 test_audit.py     (thoát mã 1 nếu có ca trượt)

VÌ SAO CẦN: audit_skills.py là thứ cả hệ skill dựa vào để kết luận "sạch hay
không". Nó đã từng có 2 lỗi thật, và cả hai đều được phát hiện TÌNH CỜ chứ
không phải do kiểm:
  - regex dò tham chiếu hardcode tiền tố tên -> mù hoàn toàn với
    ra-soat-hop-dong-vendor: mọi tham chiếu tới skill đó không được đếm.
  - E4 chỉ so tiêu đề -> 3 cảnh báo giả tồn tại suốt nhiều phiên.
Một công cụ kiểm chứng mà không được kiểm chứng thì chỉ là niềm tin.

Mỗi ca kiểm HAI chiều: lỗi phải nổ khi có lỗi (dương tính), và phải im khi
không có lỗi (âm tính). Thiếu chiều âm tính thì không phát hiện được cảnh
báo giả — đúng loại lỗi đã làm hỏng E4.
"""
import os, sys, shutil, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from audit_skills import audit  # noqa: E402

FAILED = []


def mkskill(root, name, desc=None, body='## Mục A\n\nNội dung.\n',
            fm=True, dup_fm=False, nameval=None):
    # Description mặc định phải KHÁC NHAU theo tên. Bản đầu dùng chung một câu
    # cho mọi fixture nên E6 nổ ở khắp nơi và làm nhiễu mọi ca khác — đúng loại
    # nhiễu mà chính E6 sinh ra để cảnh báo.
    if desc is None:
        desc = f'Nghiệp vụ riêng biệt số {abs(hash(name)) % 9973} dành cho {name.replace("-", " ")}.'
    d = os.path.join(root, name)
    os.makedirs(d, exist_ok=True)
    head = ''
    if fm:
        block = f'---\nname: {nameval or name}\ndescription: "{desc}"\n---\n'
        head = block + (block if dup_fm else '')
    open(os.path.join(d, 'SKILL.md'), 'w', encoding='utf-8').write(
        head + f'\n# {name}\n\n' + body)
    return d


def codes(root, **kw):
    _, F = audit(root, **kw)
    return [f['code'] for f in F]


def case(label, got, must_have=(), must_not=()):
    ok = all(c in got for c in must_have) and all(c not in got for c in must_not)
    print(('  ✅ ' if ok else '  ❌ ') + label)
    if not ok:
        FAILED.append(label)
        print(f'       kỳ vọng có {list(must_have)}, không có {list(must_not)}; thực tế: {sorted(set(got))}')


def run():
    tmp = tempfile.mkdtemp(prefix='audit-test-')
    try:
        # ---------- E1 frontmatter ----------
        r = os.path.join(tmp, 'e1'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba'); mkskill(r, 'skill-ba-bon')
        case('E1 âm tính — frontmatter chuẩn thì không nổ', codes(r), must_not=['E1'])

        mkskill(r, 'skill-bon-nam', dup_fm=True)
        case('E1 dương tính — 2 khối frontmatter', codes(r), must_have=['E1'])

        r = os.path.join(tmp, 'e1b'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba')
        mkskill(r, 'skill-lech-ten', nameval='ten-khac-han')
        case('E1 dương tính — name lệch tên thư mục', codes(r), must_have=['E1'])

        # ---------- E2 tham chiếu gãy ----------
        r = os.path.join(tmp, 'e2'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai', body='Dùng kèm `skill-hai-ba` khi cần.\n')
        mkskill(r, 'skill-hai-ba'); mkskill(r, 'skill-ba-bon')
        case('E2 âm tính — trỏ tới skill có thật', codes(r), must_not=['E2'])

        mkskill(r, 'skill-bon-nam', body='Dùng kèm `skill-khong-ton-tai` nhé.\n')
        case('E2 dương tính — trỏ tới skill không tồn tại', codes(r), must_have=['E2'])

        # HỒI QUY: lỗi thật đã gặp — tên không mở đầu bằng sht-/chuan-hoa-/quan-tri-
        r = os.path.join(tmp, 'e2reg'); os.makedirs(r)
        mkskill(r, 'ra-soat-hop-dong-vendor',
                body='Dùng kèm `chuan-hoa-ho-so-tai-lieu` và `sht-nen-tang-kiem-chung`.\n')
        mkskill(r, 'chuan-hoa-ho-so-tai-lieu',
                body='KHÔNG dùng cho hợp đồng (dùng `ra-soat-hop-dong-vendor`). Bàn giao theo `sht-nen-tang-kiem-chung`.\n')
        mkskill(r, 'sht-nen-tang-kiem-chung',
                body='Nền chung cho `ra-soat-hop-dong-vendor` và `chuan-hoa-ho-so-tai-lieu`.\n')
        case('E2/E3 hồi quy — đếm được tham chiếu tới tên không có tiền tố quen',
             codes(r), must_not=['E2', 'E3'])

        # ---------- E3 đảo cô lập ----------
        r = os.path.join(tmp, 'e3'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai', body='Xem `skill-hai-ba`.\n')
        mkskill(r, 'skill-hai-ba', body='Xem `skill-mot-hai`.\n')
        mkskill(r, 'skill-co-lap-han')
        mkskill(r, 'skill-them-vao', body='Xem `skill-mot-hai`.\n')
        case('E3 dương tính — skill không trỏ ai, không ai trỏ tới', codes(r), must_have=['E3'])

        # ---------- E4 overlap ----------
        than = ('Quy tắc chi tiết về kiểm chứng nguồn dữ liệu đầu vào, đối chiếu số liệu '
                'tài chính, xác minh danh tính người phát ngôn và ghi nhận mâu thuẫn.\n')
        r = os.path.join(tmp, 'e4'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai', body='## Kiểm chứng nguồn\n\n' + than)
        mkskill(r, 'skill-hai-ba', body='## Kiểm chứng nguồn\n\n' + than)
        mkskill(r, 'skill-ba-bon')
        case('E4 dương tính — trùng cả tiêu đề lẫn nội dung', codes(r), must_have=['E4'])

        # HỒI QUY: cảnh báo giả kéo dài nhiều phiên — trùng TÊN, khác NỘI DUNG
        r = os.path.join(tmp, 'e4reg'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai',
                body='## Quy trình\n\nBước một là gộp tài khoản theo mã dự án có cấu trúc.\n')
        mkskill(r, 'skill-hai-ba',
                body='## Quy trình 6 bước\n\nĐối chiếu thẩm quyền phê duyệt ngân sách giữa các quyết định.\n')
        mkskill(r, 'skill-ba-bon')
        case('E4 hồi quy — trùng tên mục nhưng khác nội dung thì KHÔNG báo',
             codes(r), must_not=['E4'])

        # HỒI QUY: cả hai mục đều là con trỏ -> đó là cách chữa, không phải bệnh
        ptr = ('Năm dạng báo cáo chuẩn và kỹ thuật xuất file: theo `sht-nen-tang-kiem-chung` §6. '
               'Không định nghĩa lại ở đây.\n')
        r = os.path.join(tmp, 'e4ptr'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai', body='## Kết xuất báo cáo\n\n' + ptr)
        mkskill(r, 'skill-hai-ba', body='## Kết xuất báo cáo\n\n' + ptr)
        mkskill(r, 'sht-nen-tang-kiem-chung')
        case('E4 hồi quy — hai mục cùng trỏ về một chủ sở hữu thì KHÔNG báo',
             codes(r), must_not=['E4'])

        # ---------- E5 quá khổ ----------
        r = os.path.join(tmp, 'e5'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba')
        mkskill(r, 'skill-qua-kho', body='\n'.join(f'dòng {i}' for i in range(320)))
        case('E5 dương tính — vượt 300 dòng', codes(r), must_have=['E5'])

        r = os.path.join(tmp, 'e5b'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba')
        mkskill(r, 'skill-sat-nguong', body='\n'.join(f'dòng {i}' for i in range(288)))
        case('E5 báo sớm — sát ngưỡng thì cảnh báo THẤP', codes(r), must_have=['E5'])

        # ---------- E6 tranh chấp trigger ----------
        same = 'Chuẩn hóa dữ liệu nghiệp vụ của công ty theo quy trình nội bộ đã ban hành.'
        r = os.path.join(tmp, 'e6'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai', desc=same)
        mkskill(r, 'skill-hai-ba', desc=same)
        mkskill(r, 'skill-ba-bon', desc='Săn hồ sơ ứng viên trên cổng tuyển dụng và chấm điểm.')
        case('E6 dương tính — hai description mở đầu trùng', codes(r), must_have=['E6'])

        # ---------- E7 skill nằm sai chỗ ----------
        r = os.path.join(tmp, 'e7'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba'); mkskill(r, 'skill-ba-bon')
        per = os.path.join(tmp, 'e7-personal'); os.makedirs(per)
        case('E7 âm tính — không có skill cá nhân thì im',
             codes(r, personal=per), must_not=['E7'])

        mkskill(per, 'skill-mot-hai')
        case('E7 dương tính — tồn tại đồng thời bản cá nhân và bản plugin',
             codes(r, personal=per), must_have=['E7'])

        per2 = os.path.join(tmp, 'e7b-personal'); os.makedirs(per2)
        mkskill(per2, 'skill-rieng-le')
        case('E7 dương tính — skill nhà nằm hẳn ngoài plugin',
             codes(r, personal=per2), must_have=['E7'])

        mkskill(per2, 'docx')
        _, F = audit(r, personal=per2)
        case('E7 âm tính — skill dựng sẵn của Anthropic không bị tính là skill nhà',
             [f['skill'] for f in F if f['code'] == 'E7'], must_not=['docx'])

        # ---------- E8 Sổ đăng bạ ----------
        def registry(rows):
            head = '# PHỤ LỤC B — SỔ ĐĂNG BẠ\n\n| Skill | Tầng |\n|---|---|\n'
            return head + ''.join(f'| `{x}` | 1 |\n' for x in rows)

        r = os.path.join(tmp, 'e8'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba')
        mkskill(r, 'quan-tri-he-thong-skill',
                body=registry(['skill-mot-hai', 'skill-hai-ba', 'quan-tri-he-thong-skill']))
        case('E8 âm tính — sổ khớp thực tế', codes(r), must_not=['E8'])

        r = os.path.join(tmp, 'e8dup'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba')
        mkskill(r, 'quan-tri-he-thong-skill',
                body=registry(['skill-mot-hai', 'skill-hai-ba', 'skill-hai-ba',
                               'quan-tri-he-thong-skill']))
        case('E8 dương tính — sổ có hàng TRÙNG', codes(r), must_have=['E8'])

        r = os.path.join(tmp, 'e8miss'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba'); mkskill(r, 'skill-chua-dang-ky')
        mkskill(r, 'quan-tri-he-thong-skill',
                body=registry(['skill-mot-hai', 'skill-hai-ba', 'quan-tri-he-thong-skill']))
        case('E8 dương tính — có skill chưa đăng ký trong sổ', codes(r), must_have=['E8'])

        # HỒI QUY: sổ tách sang references/ vẫn phải đọc được
        r = os.path.join(tmp, 'e8ref'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba')
        q = mkskill(r, 'quan-tri-he-thong-skill', body='Sổ nằm ở references/so-dang-ba.md.\n')
        os.makedirs(os.path.join(q, 'references'), exist_ok=True)
        open(os.path.join(q, 'references', 'so-dang-ba.md'), 'w', encoding='utf-8').write(
            registry(['skill-mot-hai', 'skill-hai-ba', 'quan-tri-he-thong-skill'])
            .replace('# PHỤ LỤC B — SỔ ĐĂNG BẠ', '# SỔ ĐĂNG BẠ'))
        case('E8 âm tính — đọc được sổ đã tách sang references/', codes(r), must_not=['E8'])

        open(os.path.join(q, 'references', 'so-dang-ba.md'), 'w', encoding='utf-8').write(
            registry(['skill-mot-hai', 'quan-tri-he-thong-skill'])
            .replace('# PHỤ LỤC B — SỔ ĐĂNG BẠ', '# SỔ ĐĂNG BẠ'))
        case('E8 dương tính — sổ ở references/ thiếu hàng vẫn bị bắt',
             codes(r), must_have=['E8'])

        # ---------- E11 sổ khai báo quan hệ không có thật ----------
        def reg2(rows):
            head = '# PHỤ LỤC B — SỔ ĐĂNG BẠ\n\n| Skill | Tầng | Sở hữu | Dùng chung với |\n|---|---|---|---|\n'
            return head + ''.join(f'| `{n}` | 1 | x | {d} |\n' for n, d in rows)

        r = os.path.join(tmp, 'e11ok'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai', body='Dùng kèm `skill-hai-ba`.\n')
        mkskill(r, 'skill-hai-ba', body='Dùng kèm `skill-mot-hai`.\n')
        mkskill(r, 'quan-tri-he-thong-skill',
                body=reg2([('skill-mot-hai', '`skill-hai-ba`'),
                           ('skill-hai-ba', '`skill-mot-hai`'),
                           ('quan-tri-he-thong-skill', '—')]))
        case('E11 âm tính — sổ khai báo khớp tham chiếu thật', codes(r), must_not=['E11'])

        r = os.path.join(tmp, 'e11bad'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai', body='Không nhắc ai cả.\n')
        mkskill(r, 'skill-hai-ba', body='Dùng kèm `skill-mot-hai`.\n')
        mkskill(r, 'quan-tri-he-thong-skill',
                body=reg2([('skill-mot-hai', '`skill-hai-ba`'),
                           ('skill-hai-ba', '`skill-mot-hai`'),
                           ('quan-tri-he-thong-skill', '—')]))
        case('E11 dương tính — sổ khai báo quan hệ mà skill không hề nhắc',
             codes(r), must_have=['E11'])

        # ---------- E12 description thiếu vùng loại trừ ----------
        r = os.path.join(tmp, 'e12'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai', desc='Làm việc A cho công ty. KHÔNG dùng cho việc B.')
        mkskill(r, 'skill-hai-ba', desc='Làm việc C cho công ty. KHÔNG dùng cho việc D.')
        mkskill(r, 'skill-ba-bon', desc='Làm việc E cho công ty. KHÔNG dùng cho việc F.')
        case('E12 âm tính — có vùng loại trừ thì im', codes(r), must_not=['E12'])

        mkskill(r, 'skill-thieu-loai-tru', desc='Làm việc G cho công ty, không nêu giới hạn nào.')
        case('E12 dương tính — thiếu vùng loại trừ', codes(r), must_have=['E12'])

        # ---------- E9 vệ sinh nguồn ----------
        root9 = os.path.join(tmp, 'e9'); sk9 = os.path.join(root9, 'skills'); os.makedirs(sk9)
        os.makedirs(os.path.join(root9, '.claude-plugin'), exist_ok=True)
        open(os.path.join(root9, 'README.md'), 'w').write('x')
        mkskill(sk9, 'skill-mot-hai'); mkskill(sk9, 'skill-hai-ba'); mkskill(sk9, 'skill-ba-bon')
        case('E9 âm tính — nguồn sạch', codes(sk9, plugin_root=root9), must_not=['E9'])

        os.makedirs(os.path.join(root9, 'skill-upgrade-25082026'), exist_ok=True)
        case('E9 dương tính — nguồn lẫn thư mục nháp', codes(sk9, plugin_root=root9), must_have=['E9'])

        open(os.path.join(root9, 'skill-upgrade-25082026', 'cu.plugin'), 'w').write('x')
        case('E9 dương tính — có file .plugin cũ nằm trong nguồn',
             codes(sk9, plugin_root=root9), must_have=['E9'])

        # ---------- E10 ngân sách description ----------
        r = os.path.join(tmp, 'e10'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba')
        mkskill(r, 'skill-vo-tran', desc='x' * 1100)
        case('E10 dương tính — description vượt 1024', codes(r), must_have=['E10'])

        r = os.path.join(tmp, 'e10b'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba')
        mkskill(r, 'skill-sat-tran', desc='x' * 1000)
        case('E10 báo sớm — sát trần', codes(r), must_have=['E10'])

        r = os.path.join(tmp, 'e10c'); os.makedirs(r)
        mkskill(r, 'skill-mot-hai'); mkskill(r, 'skill-hai-ba'); mkskill(r, 'skill-ba-bon')
        case('E10 âm tính — description ngắn thì im', codes(r), must_not=['E10'])

    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    print('Tự kiểm audit_skills.py\n')
    run()
    print()
    if FAILED:
        print(f'❌ {len(FAILED)} ca TRƯỢT:')
        for f in FAILED:
            print('   -', f)
        sys.exit(1)
    print('✅ Toàn bộ ca kiểm đạt.')
    sys.exit(0)
