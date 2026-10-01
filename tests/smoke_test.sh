#!/bin/bash
# NOT part of the original skill (added for this repo).
# Builds examples/example-spec.json with the original build.sh / build_tex.py / template.tex
# and checks: PDF exists, hyperlinks embedded, no em dash, Projects before Experience.
set -e
H="$(cd "$(dirname "$0")/.." && pwd)"
W="$(mktemp -d)"
bash "$H/scripts/setup_workdir.sh" "$W" >/dev/null
cp "$H/examples/example-spec.json" "$W/spec.json"
( cd "$W" && bash build.sh spec.json Smoke_Resume )
PDF="$W/Smoke_Resume.pdf"
[ -f "$PDF" ] || { echo "FAIL: no pdf"; exit 1; }
TXT="$(pdftotext "$PDF" -)"
echo "$TXT" | grep -q "—" && { echo "FAIL: em dash"; exit 1; }
echo "$TXT" | head -4 | grep -qi "target" && { echo "FAIL: 'target' in header"; exit 1; }
python3 -I - "$PDF" <<'PY' || { echo "FAIL: links"; exit 1; }
import sys
try:
    import pypdf
except ImportError:
    print("SKIP link check (pip install pypdf)"); sys.exit(0)
r = pypdf.PdfReader(sys.argv[1])
uris = {a.get_object()["/A"]["/URI"] for p in r.pages for a in (p.get("/Annots") or [])}
need = ["https://www.linkedin.com/in/harshavardhanrobba", "https://github.com/HarshaVardhanRobba",
        "https://portfolio-harshavardhanrobba.vercel.app/", "https://github.com/HarshaVardhanRobba/Brand_guardian"]
miss = [u for u in need if u not in uris]
sys.exit("missing links: %s" % miss if miss else 0)
PY
P=$(echo "$TXT" | grep -n "^PROJECTS" | head -1 | cut -d: -f1); E=$(echo "$TXT" | grep -n "^EXPERIENCE" | head -1 | cut -d: -f1)
[ "$P" -lt "$E" ] || { echo "FAIL: section order"; exit 1; }
echo "PASS ($PDF)"
