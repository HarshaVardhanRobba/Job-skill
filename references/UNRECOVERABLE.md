# What could not be recovered, and what does not exist

Nothing below was invented to fill a gap.

## 1. Versions: all 23 recovered, with limits
All 23 saved versions (v1 to v23) are in `versions/`. Not recoverable: per-version dates, authors' change notes and the reason for each change, because claude.ai shows only the version number. An earlier draft of this export said the source had "no 25 variations"; the intended meaning was 23 saved versions, and they are now included.

## 2. Files the skill refers to but does not contain
| Referenced file | Where referenced | Status |
|-----------------|------------------|--------|
| `gen.py` | Steps 3-6 | Only described in prose (signature `build(file, role, summary, order, skorder, lead=None, over=None, exp_over=None, exp_first=False)`). Source not in the skill. Not recreated. |
| `check.py` | Steps 3-6, Step 7 | Only described in prose (the Step 7 resume check). Source not in the skill. Not recreated. |
| Worked example for subagents | Steps 3-6 | Mentioned ("read gen.py and a worked example"); not included. |
| `spec_<X>.py` | Steps 3-6 | Per-run output name only. |
| `human_check.py` | `companion-skills/write-without-ai-tells` | Optional script the companion skill mentions; not shipped with it. |

## 3. External user data (not in the skill, not exported)
- Base resume PDF: `C:\Users\robba\OneDrive\Desktop\New folder (2)\Robba_Harshavardhan_Resume.pdf`
- Tracker: `C:\Users\robba\OneDrive\Desktop\New folder (2)\Harshavardhan_Robba_Job_Tracker.xlsx`
- Screening screenshot: `C:\Users\robba\OneDrive\Pictures\Screenshots\Screenshot 2026-10-10 194828.png`

## 4. Unconfirmed reference
Step 0 says "Skip the project-fit audit by default" without naming a skill. A skill named `portfolio-project-fit` exists in the same store, but the source never names it, so it is not bundled and not assumed to be the one meant.

## 5. Skills and tools the flow calls (not bundled except the two named skills)
Bundled in `companion-skills/`: `conditional-positioning`, `write-without-ai-tells` (the only two skills `SKILL.md` names).
Not bundled, provided by the host: Skill tool, AskUserQuestion, ToolSearch, SendUserFile, subagents (`general-purpose`), Dice and Indeed connectors, Claude in Chrome tools, remote-devices file staging tools, plus system tools `xelatex`/`pdflatex`, `pdftotext`, `pdfinfo`, `unzip`, Python with `openpyxl`.
