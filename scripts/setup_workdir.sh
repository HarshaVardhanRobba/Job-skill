#!/bin/bash
# NOT part of the original skill (added for this repo).
# usage: setup_workdir.sh <target_dir>
# Copies template.tex, build_tex.py and build.sh side by side, as Steps 3-6 of SKILL.md require.
set -e
T="${1:?usage: setup_workdir.sh <target_dir>}"
H="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$T"
cp "$H/assets/template.tex" "$T/template.tex"
cp "$H/scripts/build_tex.py" "$H/scripts/build.sh" "$T/"
chmod +x "$T/build.sh"
echo "workdir ready: $T"
