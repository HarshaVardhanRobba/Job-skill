#!/bin/bash
# usage: build.sh spec.json out_basename   -> writes out_basename.tex and out_basename.pdf (any page count)
SPEC="$1"; OUT="$2"; DIR="$(cd "$(dirname "$0")" && pwd)"
python3 -I "$DIR/build_tex.py" "$SPEC" "$OUT.tex" || exit 1
ENGINE=$(command -v xelatex || command -v pdflatex) || { echo "no LaTeX engine"; exit 3; }
rm -f "$OUT.pdf"
"$ENGINE" -interaction=nonstopmode -halt-on-error "$OUT.tex" >/dev/null 2>&1
rm -f "$OUT.aux" "$OUT.log" "$OUT.out"
PAGES=$(pdfinfo "$OUT.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
if [ -n "$PAGES" ]; then echo "OK $OUT pages=$PAGES"; exit 0; fi
echo "FAILED to build $OUT.pdf"; exit 2
