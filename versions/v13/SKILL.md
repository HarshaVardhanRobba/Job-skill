---
name: "job-search-flow"
description: "Run when the user hands over a resume and wants fresh roles found, ranked, and a tailored resume written for each."
---

# Job-Search Flow

Run when the user hands over a resume and wants fresh roles found, ranked, and a tailored resume written for each. Works for any resume; re-run per resume. This skill is the spine; it calls other skills at set points (load each with the Skill tool when its step is reached).

## Standing profile (defaults for Harshavardhan Robba; use without asking)
- Base resume: `C:\Users\robba\OneDrive\Desktop\New folder (2)\Harshavardhan_Robba_Resume1.pdf` (stage it from the device and read it fully).
- Tracker: `C:\Users\robba\OneDrive\Desktop\New folder (2)\Harshavardhan_Robba_Job_Tracker.xlsx`. Always log here; do not ask.
- Boards: Dice (`https://www.dice.com/home-feed`) and Indeed (`https://www.indeed.com/`).
- Page length: there is NO page limit. Never trim projects or bullets to fit a page, and never check page count.
- Screening answers (from the user's profile screenshot; reuse for every form):
  - Authorized to work in the US: Yes (F-1 OPT, EAD).
  - Require sponsorship now or in the future: Yes.
  - Start date: immediately. Salary: negotiable.
  - Veteran: No. Disability: No. Gender: Male. LGBTQ+: No. Race: Asian. Hispanic or Latino: No. Sexual orientation: Heterosexual. Pronouns: He/Him.
  - On-site/relocation willingness: Yes for any posting inside the location choice the user made in Step 0.
  - Profile skills the user may confirm as used: LangChain, LangGraph, RAG, retrieval pipelines, agent workflows, tool calling, prompt engineering, DeepEval, Azure OpenAI, OpenAI Realtime, Gemini 2.0, function calling, structured outputs, guardrails, hallucination detection, Node.js, Python, tRPC, REST, async streaming, API design, Inngest, Next.js, TypeScript, PostgreSQL, MongoDB, Prisma, SQL, ETL, ELT, PySpark, Databricks, Amazon RDS, Docker, Azure, AWS, GCP, CI, MCP, Twilio WebSockets, Deepgram STT, Stream Video SDK, WebRTC, real time audio processing.
  - Years of experience on any skill: answer only what the resume supports. Never inflate, never tick "yes" for a skill outside the list above or the resume. If a REQUIRED question cannot be answered truthfully, skip that application, log it as Held with the question, and ask the user at the end.
  - Questions with no stored answer (for example "only C2C or 1099?"): do not guess. Hold that application, ask the user once, then store the answer here.

## Core rule: never change the request on your own
The user's N, recency window, location, titles, boards and seniority are fixed by their Step 0 answers. If the search cannot deliver what was asked, DO NOT widen, relax, pad, substitute or quietly settle for fewer. Stop, tell the user exactly what was found and why more were not found, offer selectable options, and wait for their pick. Only then change anything, and only what they picked. This applies to windows, titles, locations, seniority, employment types, boards, and adding or dropping postings.

## Step 0 — Offer the setup choices up front, once, as selectable options (required, every run)
Prepare silently, then present the decisions as a **pick-from-options menu** before any searching, tailoring or file work. After the user picks, run the flow until the first checkpoint (Step 1 shortfall check) without asking anything else.

**Prepare silently first (no questions yet):**
- Stage and read the base resume from the Standing profile path. List every project and every job in it; this is the PROJECT LIST used in Step 3–6.
- Stage the tracker from the Standing profile path and note its row count.
- Check that the Dice and Indeed connectors are connected, and that Claude in Chrome is available.
- Work out the default titles from the resume's field (AI Engineer, LLM Engineer, Machine Learning Engineer, Generative AI Engineer, Agentic AI Engineer, Full Stack Engineer Python).

**Ask with AskUserQuestion (one call, four questions). The tracker, base resume, boards, apply step and screening answers are NOT asked; they come from the Standing profile.**
1. Header "Postings" — "How many job postings should I find?" — options: 5 / 10 / 15 / 20. The batch size is the user's choice; do not mark one as recommended. Other = custom number. N postings, N resumes.
2. Header "Recency" — options: Last 3 days / Last 5 days / Last 24 hours / Last 7 days. Job tools report posted dates at day granularity.
3. Header "Location" — options: Virginia first, then everywhere / Remote only / Washington DC area / Anywhere in the US.
4. Header "Job titles" — options: Based on my resume / AI, LLM and agentic roles only / Broader: add ML, data and full-stack.

If AskUserQuestion is unavailable, print the same menus as a lettered list and accept replies like "1A 2B 3A 4A". Skip the project-fit audit by default.

**After the answers:** restate the choices in one short confirmation line and proceed. If the run is unattended, use Recency Last 3 days, Location Virginia first then everywhere, Titles based on the resume, N = 10, and say so at the top.

## Step 1 — Find exactly N postings (Dice + Indeed)
Use each connector's `search_jobs`, one search per title x location, following the Location choice. Dice and Indeed only unless the user adds another board. If one board returns nothing inside the window, continue with the other board alone; say which board returned nothing. Indeed has no date filter, so check each result's posted date yourself. Deduplicate by Company + Title and job URL, and also against the tracker rows already logged (by Job Link and Company+Title); drop anything already in the tracker. Pull full details (`get_job_details`) for every candidate. Keep each posting's real URL exactly as returned.

**Hard gates are applied BEFORE ranking and BEFORE any resume is written.** Drop at this point, and list them in the shortfall message with the reason: citizen-only or green-card-only, security clearance required, "no sponsorship / no OPT / no visa" statements that exclude the user, 5 or more required years, W2-only vs C2C-only mismatches the user has ruled out, and posting already closed. Never build a resume for a dropped posting. Check the posting is still open when it is fetched.

**Shortfall checkpoint (required whenever fewer than N usable postings are found).** Do this BEFORE writing any resume:
1. Tell the user plainly how many were found out of N, list the postings found (company, title, location, link), and why the rest were not found (name any board that was down).
2. Ask with AskUserQuestion, multi-select, recommended first: Widen the window / Add title variants / Widen the location / Include stretch roles / Continue with only the postings found / Retry the failed board.
3. Wait. Apply exactly what was selected. If still short, show the new count and ask again. Never loop silently.

Do not pad N with postings the user would be rejected from, and do not label hard-gated roles as fits.

## Step 2 — Rank honestly, SEPARATELY PER BOARD, in the fixed ranking format
Deliver one ranking per board (DICE, INDEED), each as its own titled block. A posting on more than one board is listed under the board where it was found first. Within each board group into tiers with these exact headings, skipping empty tiers: **TOP CANDIDATE — apply now**, **SOLID — worth applying**, **STRETCH — long shot**. Number postings continuously within each board.

Every posting uses exactly this entry format (plain text, no tables):

```
1. [Job Title](job URL) — Company — Location (Remote/Hybrid/Onsite) — $salary/yr or /hr (write "salary not listed" if absent)
Why: one or two lines tying the posting's core asks to the resume's real projects and experience.
Gap: the honest shortfall (years required, seniority, missing stack, school filters, clearance) and how to handle it. Never inflate fit.
Sponsorship: H-1B sponsorship stated / not stated / not offered; if H-1B is unavailable, note OPT, green card, citizenship or clearance requirements.
ATS scans: the exact keywords from the posting's screening language, comma-separated.
Resume: the filename of this posting's tailored PDF.
```

The job title MUST be a clickable markdown link to the real posting URL; never invent or shorten a link. Flag sponsorship explicitly. ALL kept postings get a tailored resume.

## Steps 3–6 — Tailor ONE resume per posting (loop over all kept postings)
For EACH kept posting:
1. **conditional-positioning** — load the skill; set the angle for this role: identity + target in the opening words of the Summary, every claim tied to this role's value pillars, a committed primary role. The target role is expressed ONLY inside the Summary text.
2. **Write the tailored resume content.** Rules, enforced:
   - **Every resume contains ALL projects and ALL jobs from the base resume (the PROJECT LIST from Step 0). Never drop a project to save space or because it seems less relevant.** For each project and job, compare its existing bullets against this posting's requirements. If the existing bullets already fit the posting, keep them as they are and leave them alone. If they do not, rewrite or add bullets so the project's real work is framed in the posting's language: lead with the facts of that project that match what the posting asks for, mirror its keywords where they truly apply, and reorder bullets so the most relevant ones come first. Put the projects most relevant to the posting first in the Projects section, and the rest after them, all present. A project missing from a draft is added back. Rewriting means re-expressing real work; it never adds a tool, skill, scope or result that the project does not have.
   - Harvard guide: no personal pronouns; action-verb-first; reverse-chronological; Technical Skills after Education; no photo, age, gender or references; no line starting with a date. No page limit.
   - Google XYZ on every bullet: accomplished X, measured by Y, by doing Z.
   - Honesty is non-negotiable. Never invent skills, tools, employers or metrics. **Never leave bracketed placeholders or empty slots.** Numbers come only from these sources: (a) the base resume; (b) figures the user states in chat; (c) facts the assistant can count and verify itself from the user's own material, such as the number of API endpoints, tools, agents, services, data sources or integrations in a repo or project description. Do NOT make up user counts, latency, accuracy, revenue or percentage improvements. Where no real number exists, write the bullet without one: state what was built, for whom and with which tools, plus the outcome in plain words, and drop any clause that depended on the missing figure. When a run ends with bullets that have no numbers, tell the user they can supply real figures (or authorize counting from their repos) and the assistant will add them.
   - If a JD wants a skill the resume lacks, surface it as a gap in the ranking; never add it.
   - Tailoring = reordering + emphasis + mirroring the JD's real language.
3. **write-without-ai-tells** — load the skill; run it over the finished prose as the FINAL content pass (no em dashes, no banned words).
4. Save the finished content as a **spec JSON** (schema in Step 7).

## Step 7 — Produce separate PDFs in the FIXED house layout, delivered as one ZIP per board (required deliverable)
**Layout is fixed. NEVER improvise fonts, headings, spacing, alignment or colours, and never hand-build the .docx with other code.** Calibri (renders as Carlito), centred bold name, grey contact line directly under it, then straight into the Summary — NO "Target role" line, NO job title or company name line anywhere in the header — UPPERCASE bold section headings with a bottom rule, bold left text with right-aligned location/dates, italic grey sub-lines, "•" bullets, section order Summary → Education → Technical Skills → Projects → Experience, Letter size, 0.5in side margins. The resume may run to as many pages as the content needs.

**Embedded links are required.** In the header, "LinkedIn", "GitHub" and "Portfolio" are clickable hyperlinks (the `links` array), and every project's right-hand link text is a clickable hyperlink (`link` = visible text, `url` = target). Link registry for Harshavardhan Robba:
- LinkedIn: https://www.linkedin.com/in/harshavardhanrobba
- GitHub: https://github.com/HarshaVardhanRobba
- Portfolio: https://portfolio-harshavardhanrobba.vercel.app/
- Project Websito: visible text "Live: websito-eight.vercel.app", url https://websito-eight.vercel.app/
- Project Web-base: visible text "Live: web-base-workflow.vercel.app", url https://web-base-workflow.vercel.app/
- Project Elara: visible text "Live: elaravoiceai.onrender.com", url https://elaravoiceai.onrender.com
- EVERY OTHER project: visible text "Source on GitHub", url https://github.com/HarshaVardhanRobba
After building, verify the links survived into the PDF (for example `python3 -c "import re,sys;print(sorted(set(re.findall(rb'/URI\s*\(([^)]*)\)',open(sys.argv[1],'rb').read()))))" file.pdf`).

Setup once per run: create a working folder, save the two files below as `make_resume.js` and `fit.sh` in it, and run `npm install docx` there if missing.

For each posting: write `<Company>_<Role>.json`, then run `bash fit.sh <Company>_<Role>.json Harshavardhan_Robba_Resume_<Company>_<Role>`. It builds the .docx and converts it to PDF with no page check. Soffice writes the PDF into the current directory, so move it to the target folder with `mv`. Render and look at at least the first PDF.

**Resume check before upload (required, automatic).** For every resume, run a script that extracts the PDF text and fails the run if any of these are true: any project or job from the base resume (the PROJECT LIST) is missing by name; a square-bracket placeholder appears; a number or percentage appears that is not in the base resume, was not stated by the user, and is not a verified count from the user's own material; a skill or tool name appears that is not in the base resume or the Standing profile skills list; an em dash appears. Fix the spec and rebuild until clean.

**Deliver the PDFs as ONE ZIP PER BOARD**, named `Dice resumes.zip` and `Indeed resumes.zip` (only boards with postings). Each ZIP holds only that board's PDFs, flat. Check with `unzip -l` and confirm the PDF count equals the number of kept postings. Send the ZIPs with SendUserFile. Copy the PDFs to a folder under `/home/claude/work/` (this path is accepted by the browser upload tool; `/mnt/user-data/outputs/` subfolders are rejected) for the apply step.

**Spec JSON schema (no "target" field):**
```json
{
  "name": "Full Name",
  "contact": "City, ST  •  phone  •  email",
  "links": [
    { "label": "LinkedIn", "url": "https://www.linkedin.com/in/harshavardhanrobba" },
    { "label": "GitHub", "url": "https://github.com/HarshaVardhanRobba" },
    { "label": "Portfolio", "url": "https://portfolio-harshavardhanrobba.vercel.app/" }
  ],
  "summary": "2–3 line role-tailored summary, no pronouns",
  "education": [ { "school": "", "loc": "", "degree": "", "date": "" } ],
  "skills": [ { "label": "Agentic Engineering", "items": "comma-separated skills actually in the resume" } ],
  "projects": [ { "name": "", "date": "", "meta": "tech stack", "link": "Live: websito-eight.vercel.app  (or: Source on GitHub)", "url": "https://websito-eight.vercel.app/  (or: https://github.com/HarshaVardhanRobba)", "bullets": ["XYZ bullet"] } ],
  "experience": [ { "org": "", "loc": "", "title": "", "date": "", "bullets": ["XYZ bullet"] } ]
}
```
Keep 3–4 bullets per project, 1–3 per job; all projects present, most role-relevant first.

**fit.sh (no page limit):**
```bash
#!/bin/bash
# usage: fit.sh spec.json out_basename   -> writes out_basename.docx and out_basename.pdf (any page count)
SPEC="$1"; OUT="$2"; DIR="$(cd "$(dirname "$0")" && pwd)"
node "$DIR/make_resume.js" "$SPEC" "$OUT.docx" 0 >/dev/null || exit 1
rm -f "$OUT.pdf"
python /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf "$OUT.docx" >/dev/null 2>&1 || soffice --headless --convert-to pdf "$OUT.docx" >/dev/null 2>&1
PAGES=$(pdfinfo "$OUT.pdf" 2>/dev/null | awk '/^Pages/{print $2}')
if [ -n "$PAGES" ]; then echo "OK $OUT pages=$PAGES"; exit 0; fi
echo "FAILED to build $OUT.pdf"; exit 2
```

**make_resume.js:**
```js
// usage: node make_resume.js spec.json out.docx [level 0-3]
// Renders a resume in the fixed house layout. Do not change the layout.
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, ExternalHyperlink, TabStopType, AlignmentType, BorderStyle, LevelFormat } = require('docx');

const [specPath, outPath, levelArg] = process.argv.slice(2);
const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
const L = Math.max(0, Math.min(3, parseInt(levelArg || '0', 10)));

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
const sub = (left, right, url) => new Paragraph({
  spacing: { before: 0, after: 8 },
  tabStops: [{ type: TabStopType.RIGHT, position: RIGHT }],
  children: [
    new TextRun({ text: left, italics: true, size: 20, font: FONT, color: '333333' }),
    new TextRun({ text: '\t', italics: true, size: 20, font: FONT }),
    ...(url && right
      ? [new ExternalHyperlink({ link: url, children: [new TextRun({ text: right, italics: true, size: 20, font: FONT, color: '333333' })] })]
      : [new TextRun({ text: right || '', italics: true, size: 20, font: FONT, color: '333333' })]),
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
const cRun = (t) => new TextRun({ text: t, size: 18, font: FONT, color: '333333' });
const contactKids = [cRun(spec.contact)];
(spec.links || []).forEach(l => {
  contactKids.push(cRun('  •  '));
  contactKids.push(new ExternalHyperlink({ link: l.url, children: [cRun(l.label)] }));
});
k.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 28 }, children: contactKids }));

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
  k.push(sub(p.meta, p.link || '', p.url));
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

## Step 8 — Log to the tracker (always; path from the Standing profile)
Columns: Date Found | Date Applied | Company | Title | Location | Salary | Fit | Status | Resume Used | Job Link (match the file's own header if it differs). ALWAYS re-stage the tracker from the device immediately before editing (never reuse an older copy), load with openpyxl, dedupe by Job Link and Company+Title, append rows (Date Found = today, Status "Not applied", Job Link as an "Apply" hyperlink), preserve formatting and the Status dropdown, save to the outputs folder, and commit with `expectedMtimeMs` from that fresh stage. **Verify the write:** re-stage the file again after the commit and confirm the row count and the new rows are present; if not, redo it. Never save back a copy loaded from a stale stage; that silently drops rows.

## Step 9 — Apply directly (automatic, right after the resumes are built)
Do not hand off prompts. Apply yourself through Claude in Chrome, in the user's real logged-in browser. Load the Chrome tools in one ToolSearch call (tabs_context_mcp, navigate, computer, find, read_page, file_upload, browser_batch, get_page_text, tabs_create_mcp, tabs_close_mcp). Use a new tab.

1. **Dice:** navigate to `https://www.dice.com/home-feed`. If the page shows a login wall, STOP and tell the user to sign in; never enter a password and never create an account. **Indeed:** navigate to `https://www.indeed.com/`; same rule. If a board has no postings in this run, skip it and proceed with the other board only.
2. **Dice procedure (proven):** for each posting open `https://www.dice.com/job-applications/<guid>/wizard` (guid from the job URL). If the page says Inactive, or redirects to `/wizard/applied`, record it (Closed or Already applied) and move on. Otherwise: `find` the "File options" button, click it, `find` and click "Replace", `read_page` (interactive) to get the file input ref (type=file, the first one is the resume; the ref number changes, so read it each time), `file_upload` the posting's PDF from `/home/claude/work/<folder>/`, click Next (type=submit). On the review step, confirm the resume file name shown equals the intended PDF, then `find` "button labeled exactly Submit" and click it. Some postings insert an "Application Questions" step: answer from the Standing profile; if a required question has no truthful stored answer, do NOT submit; leave it, move on, and report it. Navigating away from a half-filled form may show a "Leave site?" dialog; use a fresh tab instead.
3. **Indeed procedure:** open the posting, use Apply / Easy Apply, attach the matching PDF, answer questions from the Standing profile only. If it redirects to an employer site requiring an account, password or CAPTCHA, skip it and report.
4. Submit only the postings from this run, each with its own tailored resume. Never complete CAPTCHAs, never enter passwords or payment or government IDs.
5. **Verify every submission:** after Submit, the URL must be `/wizard/success`, then reopen the job page and confirm an "Applied" button (Dice) or the board's applied confirmation. Only then count it as applied. Do not rely on screenshots (they time out); use find, read_page and get_page_text. Batch the browser calls with browser_batch where refs are already known.
6. Dice replaces the profile resume each time; mention that at the end.

## Step 10 — Final proof check (required)
Before the final message, reconcile: found N = built N resumes = applied + closed + already applied + held. Print that equation. Re-stage the tracker, set Status to Applied and Date Applied for each verified submission (Closed, Already applied, or Held with the reason otherwise), commit, then re-stage and confirm the counts match what the browser verified. Tell the user the two or three they should spot-check themselves (open Dice, Applied jobs).

## Close
Deliver in this order: (1) the per-board ranked lists from Step 2 with linked job titles and each posting's PDF named, plus the ZIPs as files; (2) the apply results: applied (verified), closed, already applied, held with the question that blocked it; (3) the reconciliation line from Step 10; (4) every honest gap; (5) every minor default decision made mid-run, plus a one-line record of each scope change the user picked. State plainly that all projects are in every resume, no metrics were invented and no placeholders remain, and offer to add real numbers if the user supplies them or authorizes counting from their repos.

## Recap
Stage base resume and tracker from the Standing profile paths and list every project and job → ask only batch size, recency, location, titles → search Dice and Indeed (a board with nothing is skipped, not an error) → drop hard-gated, closed and already-logged postings BEFORE ranking → shortfall checkpoint if under N → rank per board in the fixed format → tailor each resume: ALL projects and jobs present, existing bullets kept if they already fit, otherwise rewritten or added in the posting's language from real facts only, most relevant projects first, no placeholders, only real or verifiable numbers, write-without-ai-tells → build with the fixed generator (no page limit), run the resume check (including missing-project check), zip per board → re-stage the tracker and log rows, verify the write → open dice.com/home-feed and indeed.com in Chrome (stop at any login wall) and apply with each posting's resume, answering screening questions from the Standing profile only and holding anything not truthfully answerable → verify each application → reconcile counts, update and re-verify the tracker → Close.