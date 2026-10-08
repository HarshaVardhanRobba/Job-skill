---
name: "job-search-flow"
description: "Run when the user hands over a resume and wants fresh roles found, ranked, and a tailored resume written for each."
---

# Job-Search Flow

Run when the user hands over a resume and wants fresh roles found, ranked, and a tailored resume written for each. Works for any resume; re-run per resume. This skill is the spine; it calls other skills at set points (load each with the Skill tool when its step is reached).

## Core rule: never change the request on your own
The user's N, recency window, location, titles, boards and seniority are fixed by their Step 0 answers. If the search cannot deliver what was asked, DO NOT widen, relax, pad, substitute or quietly settle for fewer. Stop, tell the user exactly what was found and why more were not found, offer selectable options, and wait for their pick. Only then change anything, and only what they picked. This applies to windows, titles, locations, seniority, employment types, boards, and adding or dropping postings.

## Step 0 — Offer ALL setup choices up front, once, as selectable options (required, every run)
As soon as the user starts the skill with a resume, prepare silently, then present every setup decision as a **pick-from-options menu** — never as an open-ended question the user has to type an answer to. Present them all before any searching, tailoring or file work. After the user picks, run the flow until the first checkpoint (Step 1 shortfall check) without asking anything else.

**Prepare silently first (no questions yet):**
- Read the resume fully.
- Check which job-board connectors are connected in this session (Indeed, Dice, ZipRecruiter) and whether a tracker spreadsheet is reachable. Build the Boards and Tracker menus from what is actually available.
- Work out the default titles from the resume's field (e.g. AI Engineer, LLM Engineer, Machine Learning Engineer, Generative AI Engineer, Agentic AI Engineer, Full Stack Engineer Python).

**Present the menus with AskUserQuestion — two back-to-back calls of four questions each (the tool allows at most four per call), both before any work starts.** Every question has 2–4 concrete options, the recommended option FIRST and labelled "(Recommended)"; the tool adds an "Other" choice automatically so the user can still type a custom value. Use these menus:

Call A:
1. Header "Postings" — "How many job postings should I find for this resume?" — options: 10 postings (Recommended) / 5 postings / 15 postings / 20 postings. (Other = custom number.) This is N: find N postings, deliver N resumes.
2. Header "Recency" — "How recent should the postings be?" — options: Last 5 days (Recommended) / Last 24 hours / Last 3 days / Last 7 days. (Other = a custom duration, even in hours or minutes.) Note honestly in the option description or the confirmation: the job tools report posted dates at day granularity, so windows under a day approximate to "today".
3. Header "Location" — "Where should I search?" — options: Virginia first, then everywhere (Recommended — VA is the primary priority, falling back to remote + onsite + hybrid) / Remote only / Washington DC area / Anywhere in the US (remote + onsite + hybrid).
4. Header "Job titles" — "Which titles should I search?" — options: Based on my resume (Recommended — the defaults worked out in preparation) / AI, LLM and agentic roles only / Broader: add ML, data and full-stack.

Call B:
5. Header "Project audit" — "Run the optional project-fit audit for each role?" — options: Skip it (Recommended — faster, fewer tokens) / Run it for each role.
6. Header "Tracker" — "Log the postings to your tracker spreadsheet?" — options: Log to my tracker (Recommended — only offer if one is reachable; name the file) / Don't log. (Other = a different file path.) If no tracker is reachable, offer: Skip logging / and let Other take a path.
7. Header "Job boards" — "Which job boards should I search?" — options built from the connected boards: All connected boards (Recommended) / Indeed only / Dice only / ZipRecruiter only (omit any board that is not connected; if Dice or ZipRecruiter is missing, say so in the description and that connecting it widens the pool).
8. Header "Apply prompts" — "Include the ready-to-paste apply prompts at the end?" — options: Include them (Recommended) / Skip them.

Do NOT ask any question that is not in this list at setup, and do NOT use free-text questions. If AskUserQuestion is unavailable in the session, print the same eight menus as a lettered list in plain text (recommended option marked and listed first) and accept a reply like "1A 2B 3A…" or simply "defaults". If the user replies "defaults" or "go", use every Recommended option.

**Standing defaults (stated in the confirmation so the user can object once):** when the same job appears on more than one board, it is listed under the board where it was found first; resumes use only facts and numbers already in the resume, with bracketed placeholders where a real metric is missing. Widening the search is NOT a standing default: it only happens after the user picks it at the shortfall checkpoint (Step 1).

**After the answers:** restate the choices in one short confirmation line and proceed. If something unexpected comes up mid-run that changes what the user asked for, stop at that point and ask with options (see Step 1 checkpoint). Details that do not change the request (file names, ordering inside a tier) take the most reasonable default and are listed in the Close.

If the run is unattended (no one to answer), skip the menus and use every Recommended option (10 postings, last 5 days, Virginia first then everywhere, titles based on the resume, no project audit, log to the tracker if reachable, all connected boards, apply prompts included), saying at the top of the work which defaults were used. If a shortfall happens in an unattended run, do NOT widen: build resumes only for the postings found inside the original settings, and end with the shortfall options for the user to choose later.

## Step 1 — Find exactly N postings (Indeed + Dice + ZipRecruiter)
Sources, in this order: **Indeed** (primary), then **Dice** (tech-focused), then **ZipRecruiter** (broad aggregator), using the boards chosen in Step 0. LinkedIn, Workday and JobRight have no connector — do not claim to search them.

Use each connector's `search_jobs` tool (Indeed: country_code "US"), one search per title × location, following the Location choice from Step 0 (VA as the primary location, remote/onsite/hybrid as the fallback, unless the user chose otherwise). Start with Indeed; add Dice and ZipRecruiter to fill N within the user's chosen boards. Keep postings inside the chosen recency window. **Deduplicate across all sources** by Company + Title (normalized) and by job URL, since the same posting often appears on more than one board; keep one entry and note which sources carried it. Pull full details (Indeed `get_job_details`, Dice `get_job_details`, or each source's equivalent / the posting text returned) for each candidate for real screening keywords and hard gates (years, clearance, sponsorship, required stacks). Check each result's posted date against the window; do not trust a source's own recency filter. Keep each posting's real job URL exactly as the connector returned it — the rankings and apply prompts depend on those links.

**Shortfall checkpoint (required whenever fewer than N usable postings are found).** Do this BEFORE writing any resume, so no work is built on a changed request:
1. Tell the user plainly, in a few lines: how many were found out of N, the list of the postings found (company, title, location, link), and the reasons the rest were not found (for example: most results were senior roles, clearance-gated, non-software, outside the window, or a board failed to connect — name any board that was down).
2. Ask with AskUserQuestion, multi-select, 2–4 options, recommended first. Use these options as appropriate: Widen the window (name the next step, such as 3 days then 7 days) / Add title variants (name them) / Widen the location / Include stretch roles (higher years required) and contract roles / Continue with only the postings found. Other lets the user type anything. If a board was down, include "Retry the failed board" as an option.
3. Wait for the answer. Apply exactly what was selected, nothing more. If still short of N afterwards, show the new count and ask again with the remaining options. Never loop silently.
4. The user may stop at any point with "Continue with only the postings found". Then proceed with that count and state it as the final count.
5. With several resumes in one run, report the shortfall per resume in one message and ask once with options that apply to all of them (or per resume if the user asks).

Do not pad N with postings the user would be rejected from just to reach the number, and do not label hard-gated roles as fits.

## Step 2 — Rank honestly, SEPARATELY PER BOARD, in the fixed ranking format
Deliver one ranking **per board**, each as its own clearly titled block so the user can copy a single board's block into the apply session for that board: first **INDEED**, then **DICE**, then **ZIPRECRUITER** (only boards that have postings in this run). A posting that appears on more than one board is listed only under the board where it was found first. Within each board, rank by BOTH skill match and realistic chance given seniority and gates, and group into tiers with these exact headings, skipping any tier that is empty: **TOP CANDIDATE — apply now**, **SOLID — worth applying**, **STRETCH — long shot**. Number the postings continuously within each board (1, 2, 3 …).

Every posting uses exactly this entry format (plain text, no tables):

```
1. [Job Title](job URL) — Company — Location (Remote/Hybrid/Onsite) — $salary/yr or /hr (write "salary not listed" if absent)
Why: one or two lines tying the posting's core asks to the resume's real projects and experience.
Gap: the honest shortfall (years required, seniority, missing stack, school filters, clearance) and how to handle it. Never inflate fit.
Sponsorship: H-1B sponsorship stated / not stated / not offered; if H-1B is unavailable, note OPT, green card, citizenship or clearance requirements.
ATS scans: the exact keywords from the posting's screening language, comma-separated.
Resume: the filename of this posting's tailored PDF.
```

The job title MUST be a clickable markdown link to the real posting URL from Step 1; never invent or shorten a link. **Flag sponsorship explicitly, H-1B sponsorship as the main priority.** ALL postings that are kept get a tailored resume — the ranking is guidance for the user, not a filter that drops any.

## Steps 3–6 — Tailor ONE resume per posting (loop over all kept postings)
For EACH kept posting, produce its own dedicated resume:
1. **portfolio-project-fit (OPTIONAL — only if the user chose "Run it" in Step 0)** — load the skill; audit the resume's projects against this role; pick which 3–4 projects to lead with and whether each is framed tightly.
2. **conditional-positioning** — load the skill; set the angle for this role: identity + target in the opening words of the Summary, every claim tied to this role's value pillars, a committed primary role. Drives the summary, skills order, and bullet emphasis. The target role is expressed ONLY inside the Summary text — the resume has no separate "Target role" line and no company name in a header line.
3. **Write the tailored resume content**, applying 1–2. Rules, enforced:
   - Harvard guide (content rules): no personal pronouns; action-verb-first; reverse-chronological; Technical Skills after Education for tech; no photo, age, gender, or references; no line starting with a date; consistent formatting; ONE page.
   - Google XYZ on every bullet: accomplished X, measured by Y, by doing Z.
   - Honesty is non-negotiable. Never invent skills, tools, employers, or metrics. Use only numbers present in the source resume; where a real metric would help, leave a bracketed placeholder and list it in the Close for the user to fill. If a JD wants a skill the resume lacks, surface it as a gap — never add it.
   - Tailoring = reordering + emphasis + mirroring the JD's real language, not fabricating. Strip first-person summaries, stale dates, and anything a hiring manager flags in 10 seconds.
4. **write-without-ai-tells** — load the skill; run it over the finished prose as the FINAL content pass (never before positioning).
5. Save the finished content as a **spec JSON** (schema in Step 7). Content lives in the spec; layout lives only in the generator.

Building a shared master first is fine, but each posting must end with its own distinctly tailored resume.

## Step 7 — Produce separate PDFs in the FIXED house layout, delivered as one ZIP per board (required deliverable)
**Layout is fixed. NEVER improvise fonts, headings, spacing, alignment or colours, and never hand-build the .docx with other code.** The Harvard/XYZ rules above govern content only; the look is defined solely by the generator below, so every resume in every session looks identical: Calibri (renders as Carlito), centred bold name, grey contact line directly under it, then straight into the Summary — NO "Target role" line, NO job title or company name line anywhere in the header — UPPERCASE bold section headings with a bottom rule, bold left text with right-aligned location/dates, italic grey sub-lines, "•" bullets, section order Summary → Education → Technical Skills → Projects → Experience, Letter size, 0.5in side margins.

Setup once per run: create a working folder, save the two files below as `make_resume.js` and `fit.sh` in it, and run `npm install docx` there if the `docx` package is missing.

For each posting: write `<Company>_<Role>.json` per the schema, then run `bash fit.sh <Company>_<Role>.json Harshavardhan_Robba_Resume_<Company>_<Role>` (use the user's own name in the filename). It builds the .docx, converts to PDF, and confirms exactly one page, tightening spacing automatically through 4 levels. If it prints "TOO LONG", condense the least-relevant bullet or entry in the spec (never shrink fonts or edit the generator) and rerun. Open or render at least the first PDF to look at it before delivering all of them. Keep the .docx files too.

**Deliver the PDFs as ONE ZIP PER BOARD, never as loose files.** Put each posting's PDF in the folder of the board it is listed under in Step 2, then zip each folder with exactly these names: `Indeed resumes.zip`, `Dice resumes.zip`, `Ziprecruiter resumes.zip` (only boards that have postings in this run). Each ZIP holds only that board's PDFs, flat (no subfolders), so the filenames match the "Resume:" lines in that board's ranked list. Example: `mkdir -p "Indeed resumes" && cp <that board's PDFs> "Indeed resumes"/ && zip -j "Indeed resumes.zip" "Indeed resumes"/*.pdf` (if `zip` is missing, use Python's `zipfile`). Check each ZIP with `unzip -l` before sending, and confirm the PDF count across all ZIPs equals the number of kept postings. Send the ZIPs with SendUserFile (one call, all ZIPs together). Do not also send the individual PDFs unless the user asks. The .docx files can be bundled the same way as `<Board> resumes (docx).zip` only if the user asks for editable copies.

**Spec JSON schema (there is no "target" field — do not add one):**
```json
{
  "name": "Full Name",
  "contact": "City, ST  •  phone  •  email  •  LinkedIn  •  GitHub  •  Portfolio",
  "summary": "2–3 line role-tailored summary, no pronouns",
  "education": [ { "school": "", "loc": "", "degree": "", "date": "" } ],
  "skills": [ { "label": "Agentic Engineering", "items": "comma-separated skills actually in the resume" } ],
  "projects": [ { "name": "", "date": "", "meta": "tech stack", "link": "Live: site or Source on GitHub", "bullets": ["XYZ bullet"] } ],
  "experience": [ { "org": "", "loc": "", "title": "", "date": "", "bullets": ["XYZ bullet"] } ]
}
```
Keep 3–4 bullets per project, 1–3 per job, and put the most role-relevant projects first.

**fit.sh:**
```bash
#!/bin/bash
# usage: fit.sh spec.json out_basename   -> writes out_basename.docx and out_basename.pdf, exactly one page
SPEC="$1"; OUT="$2"; DIR="$(cd "$(dirname "$0")" && pwd)"
for LEVEL in 0 1 2 3; do
  node "$DIR/make_resume.js" "$SPEC" "$OUT.docx" $LEVEL >/dev/null || exit 1
  rm -f "$OUT.pdf"
  python /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf "$OUT.docx" >/dev/null 2>&1
  PAGES=$(pdfinfo "$OUT.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
  if [ "$PAGES" = "1" ]; then echo "OK $OUT level=$LEVEL pages=1"; exit 0; fi
done
echo "TOO LONG $OUT pages=$PAGES - condense the least-relevant entry in the spec and rerun"; exit 2
```
(If `soffice.py` is not at that path, use `soffice --headless --convert-to pdf` instead.)

**make_resume.js:**
```js
// usage: node make_resume.js spec.json out.docx [level 0-3]
// Renders a one-page resume in the fixed house layout. Do not change the layout.
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, TabStopType, AlignmentType, BorderStyle, LevelFormat } = require('docx');

const [specPath, outPath, levelArg] = process.argv.slice(2);
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const L = Math.max(0, Math.min(3, parseInt(levelArg || '0', 10)));

// fit levels: 0 normal -> 3 tightest (never below 9pt body)
const T = [
  { body: 19, line: 222, gap: 3, head: 90, entry: 54, top: 504, bot: 432 },
  { body: 19, line: 216, gap: 2, head: 72, entry: 44, top: 468, bot: 396 },
  { body: 18, line: 212, gap: 2, head: 60, entry: 38, top: 432, bot: 360 },
  { body: 18, line: 206, gap: 1, head: 50, entry: 30, top: 396, bot: 324 },
][L];

const FONT = 'Calibri', RIGHT = 10800;

const heading = (t) => new Paragraph({
  spacing: { before: T.head, after: 36 },
  border: { bottom: { color: '000000', space: 2, style: BorderStyle.SINGLE, size: 6 } },
  children: [new TextRun({ text: t.toUpperCase(), bold: true, size: 22, font: FONT, color: '1a1a1a' })],
});
const entry = (left, right, before) => new Paragraph({
  spacing: { before: before ?? T.entry, after: 0 },
  tabStops: [{ type: TabStopType.RIGHT, position: RIGHT }],
  children: [
    new TextRun({ text: left, bold: true, size: 21, font: FONT }),
    new TextRun({ text: '\t' + (right || ''), size: 20, font: FONT }),
  ],
});
const sub = (left, right) => new Paragraph({
  spacing: { before: 0, after: 8 },
  tabStops: [{ type: TabStopType.RIGHT, position: RIGHT }],
  children: [
    new TextRun({ text: left, italics: true, size: 20, font: FONT, color: '333333' }),
    new TextRun({ text: '\t' + (right || ''), italics: true, size: 20, font: FONT, color: '333333' }),
  ],
});
const bullet = (t) => new Paragraph({
  numbering: { reference: 'b', level: 0 },
  spacing: { before: T.gap, after: T.gap, line: T.line },
  children: [new TextRun({ text: t, size: T.body, font: FONT })],
});
const skill = (label, items) => new Paragraph({
  spacing: { before: T.gap, after: T.gap, line: T.line },
  children: [
    new TextRun({ text: label + ': ', bold: true, size: T.body, font: FONT }),
    new TextRun({ text: items, size: T.body, font: FONT }),
  ],
});

const k = [];
k.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 12 },
  children: [new TextRun({ text: spec.name, bold: true, size: 34, font: FONT })] }));
k.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 28 },
  children: [new TextRun({ text: spec.contact, size: 18, font: FONT, color: '333333' })] }));

k.push(heading('Summary'));
k.push(new Paragraph({ spacing: { before: 16, after: 8, line: T.line },
  children: [new TextRun({ text: spec.summary, size: 20, font: FONT })] }));

k.push(heading('Education'));
spec.education.forEach(e => { k.push(entry(e.school, e.loc, 60)); k.push(sub(e.degree, e.date)); });

k.push(heading('Technical Skills'));
spec.skills.forEach(s => k.push(skill(s.label, s.items)));

k.push(heading('Projects'));
spec.projects.forEach(p => {
  k.push(entry(p.name, p.date || ''));
  k.push(sub(p.meta, p.link || ''));
  p.bullets.forEach(b => k.push(bullet(b)));
});

k.push(heading('Experience'));
spec.experience.forEach(x => {
  k.push(entry(x.org, x.loc));
  k.push(sub(x.title, x.date));
  x.bullets.forEach(b => k.push(bullet(b)));
});

const doc = new Document({
  creator: spec.name,
  styles: { default: { document: { run: { font: FONT } } } },
  numbering: { config: [{ reference: 'b', levels: [{
    level: 0, format: LevelFormat.BULLET, text: '•', alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 200, hanging: 160 } } } }] }] },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 },
      margin: { top: T.top, bottom: T.bot, left: 720, right: 720 } } },
    children: k,
  }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync(outPath, b); console.log('wrote', outPath, 'level', L); });
```

## Step 8 — Log to the tracker (only if the user chose to log in Step 0)
Tracker "Job Tracker" columns (11): Date Found | Date Applied | Company | Title | Location | Salary | Fit | Status | Last Updated | Resume Used | Job Link. If the existing file has a different header, match the file's own columns instead. Stage the file from the path chosen in Step 0, load with openpyxl, dedupe new rows by Job Link (and Company+Title across sources), append (Date Found = today, Status = "Not applied", Fit from Step 2, Resume Used = that posting's resume filename, Job Link as an "Apply" hyperlink), preserve formatting + the Status dropdown + Summary tab, save the result under the outputs folder and commit back to the same path (the commit tool only accepts files from the outputs folder, not the uploads folder).

## Step 9 — Hand off to the apply step, one prompt + one ranked list + one ZIP per board (only if the user chose to include them in Step 0)
After delivering the ZIPs and updating the tracker, tell the user — clearly, with status — to run the applications themselves via Claude in the desktop browser. For EVERY board that has postings in this run (Indeed, Dice, ZipRecruiter) print one self-contained, copy-ready block in this order: the board's name as a heading, the name of that board's ZIP (for example "Resumes: Dice resumes.zip"), the board's ranked list exactly in the Step 2 format (tiers, numbered entries with clickable job-title links, Why / Gap / Sponsorship / ATS scans / Resume), then that board's apply prompt directly underneath. Never merge boards into one list and never give only the Indeed one. The user pastes one block into the Claude desktop app per logged-in board, so each block must make sense on its own and must name the resume file to use for each posting. Postings carried by more than one board go under the board where they were found first.

Steps for the user, per board:
1. Download that board's ZIP (`Indeed resumes.zip`, `Dice resumes.zip` or `Ziprecruiter resumes.zip`) and unzip it.
2. Open that board (Indeed, Dice, or ZipRecruiter) in the browser and log in.
3. Open the Claude desktop app (so Claude can act in that logged-in tab).
4. Paste that board's block (ranked list + prompt) and attach the PDFs from that board's unzipped folder.

**Indeed prompt:**
> "I'm logged into Indeed in this tab. Here is my shortlist and the tailored resume for each role. Go through the list one by one, open each posting, and complete the application using the matching tailored resume. Start with the Easy Apply listings. If a posting asks something you can't answer from my resume, pause and ask me. Show me the first three before you submit them, then keep going."

**Dice prompt:**
> "I'm logged into Dice in this tab. Here is my shortlist and the tailored resume for each role. Go through the list one by one, open each posting, and complete the application using the matching tailored resume. Start with the Easy Apply listings. If a posting asks something you can't answer from my resume, pause and ask me. Show me the first three before you submit them, then keep going."

**ZipRecruiter prompt:**
> "I'm logged into ZipRecruiter in this tab. Here is my shortlist and the tailored resume for each role. Go through the list one by one, open each posting, and complete the application using the matching tailored resume. Start with the 1-Click Apply listings. If a posting asks something you can't answer from my resume, pause and ask me. Show me the first three before you submit them, then keep going."

Only print blocks for boards that actually have postings in this run. Some postings on any board redirect to the employer's own site to apply; the apply session should treat those like any other and pause if it hits a login or a question it can't answer.

Then invite the user to run this Step 9 handoff so the applications can be tracked in the Claude desktop, and to confirm back whether it works. (This closing invitation is part of the final message, not a mid-run question.) Safety note for that apply session: it submits only with the user present and approving (first three shown before submitting), pauses on any question it can't answer from the resume, never completes bot checks or CAPTCHAs, and never enters passwords, payment, or government-ID details — the user does those.

## Close
Deliver in this order: (1) the per-board ranked lists from Step 2 (INDEED, DICE, ZIPRECRUITER), each in the fixed entry format with linked job titles and each posting's PDF named, each followed by that board's apply prompt per Step 9, with the three resume ZIPs delivered as files; (2) every honest gap and filter not already covered; (3) every bracketed placeholder the user needs to fill; (4) every minor default decision made mid-run, plus a one-line record of every scope change the user picked at the shortfall checkpoint. Never list a scope change here that the user did not pick. Do not repeat the same postings in a second combined table.

## Recap
Offer all setup choices once as selectable menus (postings, recency, location, titles, project audit, tracker, boards, apply prompts; recommended option first, "Other" for custom) → find N postings across the chosen boards using exactly those settings (VA first, else remote/onsite/hybrid; dedupe across sources; keep real job URLs) → if fewer than N are found, STOP: show what was found and why, offer selectable options (widen window, add titles, widen location, include stretch/contract roles, retry a failed board, or continue with what was found), wait, apply only what the user picks, and never decide on your own → rank SEPARATELY PER BOARD in the fixed format (TOP CANDIDATE / SOLID / STRETCH tiers, linked job title — company — location — salary, then Why / Gap / Sponsorship / ATS scans / Resume; H-1B flagged first) → for EACH kept posting: optional portfolio-project-fit → conditional-positioning (target role only inside the Summary) → write content (Harvard + XYZ + honesty) → write-without-ai-tells → save as spec JSON (no target-role line) → render every resume with the fixed generator (make_resume.js + fit.sh) into identical-looking one-page PDFs → zip them per board (Indeed resumes.zip, Dice resumes.zip, Ziprecruiter resumes.zip) and send the ZIPs → tracker → Step 9: one block per board (ZIP name + ranked list + apply prompt) → Close listing minor defaults and the scope changes the user chose.