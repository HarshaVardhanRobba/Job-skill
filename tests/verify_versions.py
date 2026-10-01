"""NOT part of the original skill. Checks versions/vN/SKILL.md against versions/CHECKSUMS.sha256
and that v23 equals references/original-SKILL.md.  usage: python3 -I tests/verify_versions.py"""
import hashlib, os, sys
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ok = True
for line in open(os.path.join(H, "versions/CHECKSUMS.sha256")):
    sha, name = line.split()
    good = hashlib.sha256(open(os.path.join(H, "versions", name), "rb").read()).hexdigest() == sha
    ok &= good
    print(("OK   " if good else "FAIL ") + name)
same = open(os.path.join(H, "versions/v23/SKILL.md"), "rb").read() == open(os.path.join(H, "references/original-SKILL.md"), "rb").read()
ok &= same
print(("OK   " if same else "FAIL ") + "v23 == references/original-SKILL.md")
sys.exit(0 if ok else 1)
