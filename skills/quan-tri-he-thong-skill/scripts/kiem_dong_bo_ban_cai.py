"""Kiểm sht-skills có cùng phiên bản và cùng nội dung ở mọi nơi cài.

Chỉ đọc, không sửa gì. So bốn chỗ với nguồn `SKILL file/sht-skills`:
  1. Git: commit cục bộ đã lên remote chưa
  2. Tab Code: bản cài `sht-skills@sht-local` (installed_plugins.json + thư mục cache)
  3. Cowork: bản thư viện tổ chức đồng bộ về máy (thư mục rpm)
  4. Skill cá nhân của tài khoản trùng tên với skill trong plugin

Nội dung so sau khi chuẩn hoá CRLF→LF, bỏ __pycache__.
Exit: 0 = khớp hết · 1 = có lệch · 2 = không kiểm được (không thấy đối tượng để so).
Chạy SAU phát hành (push + cập nhật tab Code + tải lên thư viện tổ chức), từ bản nguồn:
  python "SKILL file/sht-skills/skills/quan-tri-he-thong-skill/scripts/kiem_dong_bo_ban_cai.py"
Chạy từ bản đã cài (cache) thì phải trỏ nguồn bằng --nguon <thư mục sht-skills>.
"""
import glob
import hashlib
import json
import os
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TEN = "sht-skills"
# scripts/ → quan-tri-he-thong-skill/ → skills/ → sht-skills/
NGUON = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
if "--nguon" in sys.argv:
    NGUON = os.path.abspath(sys.argv[sys.argv.index("--nguon") + 1])
HOME = os.path.expanduser("~")
APPDATA = os.environ.get("APPDATA", os.path.join(HOME, "AppData", "Roaming"))
SESSIONS = os.path.join(APPDATA, "Claude", "local-agent-mode-sessions")


def doc_json(p):
    with open(p, encoding="utf-8-sig") as f:
        return json.load(f)


def phien_ban(goc):
    p = os.path.join(goc, ".claude-plugin", "plugin.json")
    return doc_json(p).get("version") if os.path.isfile(p) else None


def bang_bam(goc_skills):
    """{đường dẫn tương đối: sha256 nội dung đã chuẩn hoá} cho mọi file dưới skills/."""
    kq = {}
    for r, ds, fs in os.walk(goc_skills):
        ds[:] = [d for d in ds if d != "__pycache__"]
        for f in fs:
            if f.endswith(".pyc"):
                continue
            p = os.path.join(r, f)
            with open(p, "rb") as h:
                b = h.read().replace(b"\r\n", b"\n")
            kq[os.path.relpath(p, goc_skills).replace("\\", "/")] = hashlib.sha256(b).hexdigest()
    return kq


def so_noi_dung(ten_cho, goc, bam_nguon):
    bam = bang_bam(os.path.join(goc, "skills"))
    khac = sorted(k for k in bam_nguon.keys() & bam.keys() if bam_nguon[k] != bam[k])
    thieu = sorted(bam_nguon.keys() - bam.keys())
    thua = sorted(bam.keys() - bam_nguon.keys())
    so_skill = len({k.split("/")[0] for k in bam})
    print(f"   nội dung: {len(bam)} file / {so_skill} skill — khác {len(khac)}, thiếu {len(thieu)}, thừa {len(thua)}")
    for nhan, ds in (("khác", khac), ("thiếu", thieu), ("thừa", thua)):
        for k in ds[:10]:
            print(f"     [{nhan}] {k}")
        if len(ds) > 10:
            print(f"     … và {len(ds) - 10} file {nhan} nữa")
    return not (khac or thieu or thua)


def main():
    lech = False
    khong_kiem_duoc = []

    print(f"== Nguồn: {NGUON}")
    v_nguon = phien_ban(NGUON)
    if not v_nguon:
        print("   KHÔNG KIỂM ĐƯỢC: không đọc được plugin.json của nguồn")
        return 2
    bam_nguon = bang_bam(os.path.join(NGUON, "skills"))
    ten_skill_nguon = {k.split("/")[0] for k in bam_nguon}
    print(f"   phiên bản {v_nguon} · {len(bam_nguon)} file / {len(ten_skill_nguon)} skill")
    if os.path.join(".claude", "plugins") in NGUON or "local-agent-mode-sessions" in NGUON:
        print("   KHÔNG KIỂM ĐƯỢC: đang chạy từ bản đã cài, không phải nguồn — truyền --nguon")
        return 2

    # 1. Git
    print("\n== 1. Git (nguồn ↔ remote)")
    try:
        g = lambda *a: subprocess.run(["git", "-C", NGUON, *a], capture_output=True, text=True, timeout=30)
        nhanh = g("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
        head = g("rev-parse", "--short", "HEAD").stdout.strip()
        r = g("rev-list", "--left-right", "--count", "HEAD...@{u}")
        print(f"   nhánh {nhanh} @ {head}")
        if r.returncode:
            print("   ⚠️ không có nhánh upstream để so")
            khong_kiem_duoc.append("git")
        else:
            truoc, sau = r.stdout.split()
            print(f"   ahead {truoc}, behind {sau} (so với remote đã fetch lần cuối; chưa chạy ls-remote)")
            if truoc != "0":
                print("   ✗ còn commit chưa push")
                lech = True
            if g("status", "--porcelain").stdout.strip():
                print("   ✗ có thay đổi chưa commit")
                lech = True
    except (OSError, subprocess.SubprocessError) as e:
        print(f"   KHÔNG KIỂM ĐƯỢC: {e}")
        khong_kiem_duoc.append("git")

    # 2. Tab Code
    print("\n== 2. Tab Code (sht-skills@sht-local)")
    p = os.path.join(HOME, ".claude", "plugins", "installed_plugins.json")
    muc = []
    if os.path.isfile(p):
        for k, ds in doc_json(p).get("plugins", {}).items():
            if k.split("@")[0] == TEN:
                muc += [(k, d) for d in ds]
    if not muc:
        print(f"   KHÔNG KIỂM ĐƯỢC: không thấy {TEN} trong {p}")
        khong_kiem_duoc.append("tab Code")
    for k, d in muc:
        v, goc = d.get("version"), d.get("installPath", "")
        print(f"   {k}: phiên bản {v} · cập nhật {d.get('lastUpdated')} · {goc}")
        if v != v_nguon:
            print(f"   ✗ lệch phiên bản (nguồn {v_nguon})")
            lech = True
        if os.path.isdir(goc):
            lech |= not so_noi_dung("tab Code", goc, bam_nguon)
        else:
            print("   ✗ thư mục cài không tồn tại")
            lech = True

    # 3. Cowork / thư viện tổ chức
    print("\n== 3. Cowork — bản thư viện tổ chức trên máy (rpm)")
    rpm = []
    for pj in glob.glob(os.path.join(SESSIONS, "*", "*", "rpm", "plugin_*", ".claude-plugin", "plugin.json")):
        try:
            if doc_json(pj).get("name") == TEN:
                rpm.append(os.path.dirname(os.path.dirname(pj)))
        except (OSError, ValueError):
            pass
    if not rpm:
        print(f"   KHÔNG KIỂM ĐƯỢC: không thấy bản {TEN} nào dưới {SESSIONS}")
        khong_kiem_duoc.append("Cowork")
    for goc in rpm:
        v = phien_ban(goc)
        print(f"   phiên bản {v} · {goc}")
        if v != v_nguon:
            print(f"   ✗ lệch phiên bản (nguồn {v_nguon}) — cần tải gói {v_nguon} lên thư viện tổ chức")
            lech = True
        lech |= not so_noi_dung("Cowork", goc, bam_nguon)

    # 4. Skill cá nhân trùng tên
    print("\n== 4. Skill cá nhân của tài khoản trùng tên với plugin")
    thu_muc = glob.glob(os.path.join(SESSIONS, "skills-plugin", "*", "*", "skills"))
    if not thu_muc:
        print("   KHÔNG KIỂM ĐƯỢC: không thấy thư mục skill cá nhân")
        khong_kiem_duoc.append("skill cá nhân")
    for t in thu_muc:
        ca_nhan = {d for d in os.listdir(t) if os.path.isdir(os.path.join(t, d))}
        trung = sorted(ca_nhan & ten_skill_nguon)
        print(f"   đã kiểm {len(ca_nhan)} skill cá nhân · trùng {len(trung)}")
        for d in trung:
            print(f"     ✗ {d}")
        lech |= bool(trung)

    print("\n== KẾT LUẬN")
    if lech:
        print("✗ CÓ LỆCH — xem các dòng ✗ ở trên")
        return 1
    if khong_kiem_duoc:
        print(f"⚠️ KHÔNG KIỂM ĐƯỢC phần: {', '.join(khong_kiem_duoc)} — không được coi là khớp")
        return 2
    print(f"✓ Khớp: mọi nơi cài đều là {v_nguon}, nội dung trùng nguồn, không có skill cá nhân trùng tên")
    return 0


if __name__ == "__main__":
    sys.exit(main())
