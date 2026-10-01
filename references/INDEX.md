# Numbered index of the skill's components

The skill's 23 saved versions are indexed in `../versions/INDEX.md`. The list below covers the 18 named sections inside the current version (v23), in order.
Line numbers refer to `references/original-SKILL.md`.

| # | Component | Original heading | Lines | Purpose (from the source) |
|---|-----------|------------------|-------|---------------------------|
| 1 | Standing profile | `## Standing profile` | 10-28 | Defaults for the user: base resume path, tracker path, boards, no page limit, screening answers |
| 2 | Core rule | `## Core rule: never change the request on your own` | 30-32 | Never widen, relax, pad or settle for fewer without the user's pick; two standing exceptions |
| 3 | Two-tier screening rule | `## Two-tier screening rule` | 34-38 | Tier 1 normal gates; Tier 2 relaxes everything except clear citizenship |
| 4 | Step 0 | `## Step 0` | 40-57 | Silent prep, then one AskUserQuestion call with 4 questions (Postings, Recency, Location, Job titles); unattended defaults |
| 5 | Step 1 | `## Step 1` | 59-60 | Find exactly N postings on Dice + Indeed; search rules, rate limits, dedupe |
| 6 | Already-applied check | `**Already-applied check**` (inside Step 1) | 62-65 | Sync tracker with Dice Applied list; check each wizard page |
| 7 | Tier 1 hard gates | `**Tier 1 hard gates ...**` (inside Step 1) | 67 | Drop citizenship, clearance, no-sponsorship, 5+ years, W2/C2C mismatch, closed |
| 8 | Step 1a | `## Step 1a` | 69-78 | Indeed site search in Chrome (`fromage`, `sort=date`) |
| 9 | Step 1b | `## Step 1b` | 80-87 | Dice recommended-jobs fallback |
| 10 | Shortfall checkpoint | `**Shortfall checkpoint**` (after Step 1b) | 89-94 | Report shortfall, ask multi-select options, wait |
| 11 | Step 2 | `## Step 2` | 96-110 | Rank per board in fixed format (TOP CANDIDATE / SOLID / STRETCH) |
| 12 | Steps 3-6 | `## Steps 3–6` | 112-132 | Setup, parallel subagents, conditional-positioning, tailoring rules, write-without-ai-tells, spec JSON |
| 13 | Step 7 | `## Step 7` | 134-409 | Fixed LaTeX template layout, links, resume check, one ZIP per board; contains build.sh, build_tex.py, template.tex, spec schema |
| 14 | Step 8 | `## Step 8` | 412-414 | Log to the original tracker xlsx and verify the write |
| 15 | Step 9 | `## Step 9` | 416-438 | Apply on Dice / Indeed through Claude in Chrome; speed method, parallel tabs, browser method |
| 16 | Step 10 | `## Step 10` | 440-441 | Final proof check and reconciliation equation |
| 17 | Close | `## Close` | 443-444 | Final message contents and order |
| 18 | Recap | `## Recap` | 446-447 | One-paragraph summary of the whole flow |

## Step 0 run options (the only "choices" the skill defines)

| Question | Options |
|----------|---------|
| Postings | 5 / 10 / 15 / 20 / Other (custom number) |
| Recency | Last 3 days / Last 5 days / Last 24 hours / Last 7 days |
| Location | Virginia first, then everywhere / Remote only / Washington DC area / Anywhere in the US |
| Job titles | Based on my resume / AI, LLM and agentic roles only / Broader: add ML, data and full-stack |

Unattended defaults (original text): Recency Last 3 days, Location Virginia first then everywhere, Titles based on the resume, N = 10.

## Where each moved block lives

| Original block | Repo file |
|----------------|-----------|
| Spec JSON schema | `references/spec-schema.json` |
| `build.sh` | `scripts/build.sh` |
| `build_tex.py` | `scripts/build_tex.py` |
| Reference resume template | `assets/template.tex` |
