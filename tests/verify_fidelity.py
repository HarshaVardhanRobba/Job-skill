"""NOT part of the original skill. Proves SKILL.md + moved files == original SKILL.md.
usage: python3 -I tests/verify_fidelity.py"""
import hashlib, os, sys
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: open(os.path.join(H, p), encoding="utf-8").read()
orig = rd("references/original-SKILL.md")
L = orig.split("\n")
def blk(a, b): return "\n".join(L[a:b]) + "\n"
moved = {"references/spec-schema.json": blk(157, 174), "scripts/build.sh": blk(179, 190),
         "scripts/build_tex.py": blk(194, 267), "assets/template.tex": blk(271, 409)}
ok = True
for p, want in moved.items():
    good = rd(p) == want
    ok &= good
    print(("OK   " if good else "FAIL ") + p)
cur = rd("SKILL.md").split("\n")
out = [l for l in cur if not l.startswith("(Moved to `")]
rebuilt = L[:156] + L[175:178] + L[191:193] + L[268:270] + L[410:]
good = out == rebuilt
ok &= good
print(("OK   " if good else "FAIL ") + "SKILL.md == original minus 4 moved code blocks")
print("original sha256", hashlib.sha256(orig.encode()).hexdigest())
sys.exit(0 if ok else 1)
