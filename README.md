# job-search-flow

A Claude skill that takes a resume and runs the whole job-hunt loop: find fresh postings on Dice and Indeed, screen and rank them, write one tailored LaTeX resume per posting, log everything in an Excel tracker, and apply through the user's logged-in browser.

> Exported on 2026-10-15. Root `SKILL.md` is v23 (current) with four large code blocks moved into files. `references/original-SKILL.md` is the untouched v23. `versions/` holds v1 to v23.

## Variations = the 23 saved versions
The skill's "variations" are its 23 saved versions (v1 to v23, v23 current), read from the claude.ai Skills page on 2026-10-15. Every version is in `versions/vN/SKILL.md`, byte-for-byte, with SHA-256 checksums. The numbered index with line counts, size and section changes is [`versions/INDEX.md`](versions/INDEX.md). Per-version dates and change notes are not shown by claude.ai, so none are given. An earlier draft of this export wrongly referred to "25 variations"; there are 23 versions.

## Warning before you publish
Every version contains personal data of the original author: name, phone, email, local Windows paths, work-authorization and sponsorship status, and demographic screening answers (race, gender, veteran, disability and others). Review or replace the "Standing profile" section, `assets/template.tex` and all of `versions/` before pushing this repo to a public GitHub repository. Prefer a private repo.

## Purpose
Given a resume, the skill:
1. Asks four setup questions once (how many postings, recency, location, job titles).
2. Searches Dice and Indeed, checks what was already applied to, and drops postings the user cannot take (citizenship, clearance, no sponsorship, 5+ years, closed).
3. Ranks postings per board.
4. Builds one resume PDF per posting from a fixed LaTeX template, using real facts only.
5. Logs rows in the tracker, applies on Dice and Indeed, verifies each submission, and reconciles the counts.

## Folder structure
```
job-search-flow-skill/
├── SKILL.md                     skill entry point (YAML frontmatter + flow)
├── README.md
├── .gitignore
├── assets/
│   └── template.tex             Reference resume template (LaTeX)
├── scripts/
│   ├── build.sh                 compile a spec JSON to PDF
│   ├── build_tex.py             fill template.tex from a spec JSON
│   └── setup_workdir.sh         (added) copy the three build files together
├── versions/
│   ├── INDEX.md                 numbered index of all 23 versions
│   ├── CHECKSUMS.sha256
│   └── v1/ ... v23/SKILL.md     every saved version, byte-for-byte
├── references/
│   ├── INDEX.md                 numbered index of all components
│   ├── UNRECOVERABLE.md         missing / non-existent items
│   ├── spec-schema.json         spec JSON schema from Step 7
│   └── original-SKILL.md        byte-identical original
├── examples/
│   └── example-spec.json        (added) small spec built from template content
├── tests/
│   ├── smoke_test.sh            (added) builds the example, checks the PDF
│   ├── verify_fidelity.py       (added) proves the split matches v23
│   └── verify_versions.py       (added) checks all 23 versions against checksums
└── companion-skills/
    ├── conditional-positioning/SKILL.md
    └── write-without-ai-tells/SKILL.md
```
Items marked "(added)" are not part of the original skill.

## Installation
The skill is a folder with `SKILL.md`. Install the main skill and both companions (the flow loads them in Steps 3-6):
```bash
# Claude Code, personal skills
mkdir -p ~/.claude/skills
cp -r . ~/.claude/skills/job-search-flow
cp -r companion-skills/conditional-positioning ~/.claude/skills/
cp -r companion-skills/write-without-ai-tells ~/.claude/skills/
```
For claude.ai, zip the `job-search-flow` folder (with `SKILL.md` at its root) and upload it under Settings > Capabilities > Skills. Zip each companion the same way.

Requirements: `xelatex` or `pdflatex` (TeX Live), `pdftotext` and `pdfinfo` (poppler), Python 3, and `openpyxl` for the tracker. The full flow also needs the Dice and Indeed connectors, Claude in Chrome, and file access to the user's computer. These come from the host, not this repo.

## Test
```bash
bash tests/smoke_test.sh            # builds examples/example-spec.json into a PDF and checks links, order, em dashes
python3 -I tests/verify_fidelity.py # confirms SKILL.md plus moved files equal v23
python3 -I tests/verify_versions.py # checks all 23 versions against SHA-256 checksums
```
`smoke_test.sh` checks hyperlinks with `pypdf` (`pip install pypdf`); it skips that check if missing.

## Usage
Ask Claude: "run job-search-flow with my resume". Step 0 offers the setup menus. Before the build steps, run `bash scripts/setup_workdir.sh /home/claude/work/<folder>` as the skill's Steps 3-6 describe.

## Numbered index of the variations (versions)
| # | File | Lines | Main section changes (computed, see `versions/INDEX.md`) |
|---|------|-------|------------------------------------------------------------|
| 1 | [`versions/v1/SKILL.md`](versions/v1/SKILL.md) | 52 | see index |
| 2 | [`versions/v2/SKILL.md`](versions/v2/SKILL.md) | 62 | see index |
| 3 | [`versions/v3/SKILL.md`](versions/v3/SKILL.md) | 64 | see index |
| 4 | [`versions/v4/SKILL.md`](versions/v4/SKILL.md) | 75 | see index |
| 5 | [`versions/v5/SKILL.md`](versions/v5/SKILL.md) | 87 | see index |
| 6 | [`versions/v6/SKILL.md`](versions/v6/SKILL.md) | 93 | see index |
| 7 | [`versions/v7/SKILL.md`](versions/v7/SKILL.md) | 231 | see index |
| 8 | [`versions/v8/SKILL.md`](versions/v8/SKILL.md) | 244 | see index |
| 9 | [`versions/v9/SKILL.md`](versions/v9/SKILL.md) | 256 | see index |
| 10 | [`versions/v10/SKILL.md`](versions/v10/SKILL.md) | 258 | see index |
| 11 | [`versions/v11/SKILL.md`](versions/v11/SKILL.md) | 255 | see index |
| 12 | [`versions/v12/SKILL.md`](versions/v12/SKILL.md) | 278 | see index |
| 13 | [`versions/v13/SKILL.md`](versions/v13/SKILL.md) | 268 | see index |
| 14 | [`versions/v14/SKILL.md`](versions/v14/SKILL.md) | 276 | see index |
| 15 | [`versions/v15/SKILL.md`](versions/v15/SKILL.md) | 291 | see index |
| 16 | [`versions/v16/SKILL.md`](versions/v16/SKILL.md) | 303 | see index |
| 17 | [`versions/v17/SKILL.md`](versions/v17/SKILL.md) | 311 | see index |
| 18 | [`versions/v18/SKILL.md`](versions/v18/SKILL.md) | 311 | see index |
| 19 | [`versions/v19/SKILL.md`](versions/v19/SKILL.md) | 322 | see index |
| 20 | [`versions/v20/SKILL.md`](versions/v20/SKILL.md) | 335 | see index |
| 21 | [`versions/v21/SKILL.md`](versions/v21/SKILL.md) | 342 | see index |
| 22 | [`versions/v22/SKILL.md`](versions/v22/SKILL.md) | 447 | see index |
| 23 | [`versions/v23/SKILL.md`](versions/v23/SKILL.md) | 447 | see index |

v23 is current. v22 to v23 changed one line: the base resume filename in the Standing profile.

### Components inside v23 (18 named sections)
See [`references/INDEX.md`](references/INDEX.md): Standing profile, Core rule, Two-tier screening rule, Step 0, Step 1, Already-applied check, Tier 1 hard gates, Step 1a, Step 1b, Shortfall checkpoint, Step 2, Steps 3-6, Step 7, Step 8, Step 9, Step 10, Close, Recap.

## Changes from the original
Root `SKILL.md` differs from v23 only in that four code blocks in Step 7 were moved out of `SKILL.md` into files (spec schema, `build.sh`, `build_tex.py`, `template.tex`), each replaced by a one-line pointer. Every other character is unchanged. `tests/verify_fidelity.py` checks this.

## License
None chosen. Add one before publishing.
