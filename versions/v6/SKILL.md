---
name: "job-search-flow"
description: "Run the job-search flow for a given resume: offer all setup choices once up front as pick-from-options menus (count, recency, location, titles, project audit, tracker, boards, apply prompts), then find that many postings across Indeed, Dice and ZipRecruiter, rank by honest fit with H-1B flagged first, tailor one one-page PDF resume per posting, log to the tracker, and hand off with a ready-to-paste apply prompt for each board."
---

# Job-Search Flow

Run when the user hands over a resume and wants fresh roles found, ranked, and a tailored resume written for each. Works for any resume; re-run per resume. This skill is the spine; it calls other skills at set points (load each with the Skill tool when its step is reached).

## Step 0 — Offer ALL setup choices up front, once, as selectable options (required, every run)
As soon as the user starts the skill with a resume, prepare silently, then present every setup decision as a **pick-from-options menu** — never as an open-ended question the user has to type an answer to. Present them all before any searching, tailoring or file work. After the user picks, run the whole flow start to finish without stopping to ask anything else.

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

Do NOT ask any question that is not in this list, and do NOT use free-text questions. If AskUserQuestion is unavailable in the session, print the same eight menus as a lettered list in plain text (recommended option marked and listed first) and accept a reply like "1A 2B 3A…" or simply "defaults". If the user replies "defaults" or "go", use every Recommended option.

**Standing defaults (stated in the confirmation so the user can object once, never asked as questions):** if fewer than N postings turn up, widen automatically in this order — more title variants, then wider location, then a longer window — and report the true maximum if N still cannot be reached; when the same job appears on more than one board, it is listed under the board where it was found first; resumes use only facts and numbers already in the resume, with bracketed placeholders where a real metric is missing.

**After the answers:** restate the choices in one short confirmation line and proceed. If something unexpected comes up mid-run, do not stop to ask — take the most reasonable default, keep going, and list every such decision in the Close. The only reason to pause mid-run is a hard blocker that cannot be defaulted (for example no job-board connector is available at all).

If the run is unattended (no one to answer), skip the menus and use every Recommended option (10 postings, last 5 days, Virginia first then everywhere, titles based on the resume, no project audit, log to the tracker if reachable, all connected boards, apply prompts included), saying at the top of the work which defaults were used.

## Step 1 — Find exactly N postings (Indeed + Dice + ZipRecruiter)
Sources, in this order: **Indeed** (primary), then **Dice** (tech-focused), then **ZipRecruiter** (broad aggregator), using the boards chosen in Step 0. LinkedIn, Workday and JobRight have no connector — do not claim to search them.

Use each connector's `search_jobs` tool (Indeed: country_code "US"), one search per title × location, following the Location choice from Step 0 (VA as the primary location, remote/onsite/hybrid as the fallback, unless the user chose otherwise). Start with Indeed; add Dice and ZipRecruiter to fill N or to widen the pool when Indeed is thin. Keep postings inside the chosen recency window. **Deduplicate across all sources** by Company + Title (normalized) and by job URL, since the same posting often appears on more than one board; keep one entry and note which sources carried it. Select the N best-fit. If fewer than N exist, apply the widening defaults from Step 0 (titles, then location, then window) until N is reached, or report the true maximum found. Pull full details (Indeed `get_job_details`, Dice `get_job_details`, or each source's equivalent / the posting text returned) for each selected posting for real screening keywords and hard gates (years, clearance, sponsorship, required stacks). Check each result's posted date against the window; do not trust a source's own recency filter.

## Step 2 — Rank honestly
Sort the N into Top / Stretch / Weak by BOTH skill match and realistic chance given seniority and gates. For each: one line on why, the real gap, the source it came from, and the exact ATS keywords it scans for. Never inflate fit. **Flag sponsorship explicitly, H-1B sponsorship as the main priority** — state whether each posting offers H-1B sponsorship; only if that is unavailable fall back to noting other work authorization (OPT, green card, citizenship, clearance). ALL N postings get a tailored resume — the ranking is guidance for the user, not a filter that drops any.

## Steps 3–6 — Tailor ONE resume per posting (loop over all N)
For EACH of the N postings, produce its own dedicated resume:
1. **portfolio-project-fit (OPTIONAL — only if the user chose "Run it" in Step 0)** — load the skill; audit the resume's projects against this role; pick which 3–4 projects to lead with and whether each is framed tightly.
2. **conditional-positioning** — load the skill; set the angle for this role: identity + target at the top, every claim tied to this role's value pillars, a committed primary role. Drives the summary, skills order, and bullet emphasis.
3. **Write the tailored resume**, applying 1–2. Rules, enforced:
   - Harvard guide: no personal pronouns; action-verb-first; reverse-chronological; Technical Skills after Education for tech; no photo, age, gender, or references; no line starting with a date; consistent formatting; ONE page.
   - Google XYZ on every bullet: accomplished X, measured by Y, by doing Z.
   - Honesty is non-negotiable. Never invent skills, tools, employers, or metrics. Use only numbers present in the source resume; where a real metric would help, leave a bracketed placeholder and list it in the Close for the user to fill. If a JD wants a skill the resume lacks, surface it as a gap — never add it.
   - Tailoring = reordering + emphasis + mirroring the JD's real language, not fabricating. Strip first-person summaries, stale dates, and anything a hiring manager flags in 10 seconds.
4. **write-without-ai-tells** — load the skill; run it over the finished prose as the FINAL content pass (never before positioning).

Building a shared master first is fine, but each posting must end with its own distinctly tailored resume.

## Step 7 — Produce N separate PDFs (required deliverable)
For each posting, build its resume as .docx with the `docx` skill (ATS-safe font, 0.5in margins, ~9.5–10pt body), verify ONE page (convert with `soffice.py --convert-to pdf`; check `pdfinfo` Pages == 1; tighten or condense the least-relevant entry until it fits, never below ~9pt), then export each to **PDF**. Required output: N individual PDF resumes, one per posting, each named for its company/role. Deliver all N with SendUserFile. Keep the .docx too for edits.

## Step 8 — Log to the tracker (only if the user chose to log in Step 0)
Tracker "Job Tracker" columns (11): Date Found | Date Applied | Company | Title | Location | Salary | Fit | Status | Last Updated | Resume Used | Job Link. Stage the file from the path chosen in Step 0, load with openpyxl, dedupe new rows by Job Link (and Company+Title across sources), append (Date Found = today, Status = "Not applied", Fit from Step 2, Resume Used = that posting's resume filename, Job Link as an "Apply" hyperlink), preserve formatting + the Status dropdown + Summary tab, commit back to the same path.

## Step 9 — Hand off to the apply step, one prompt per board (only if the user chose to include them in Step 0)
After delivering the PDFs and updating the tracker, tell the user — clearly, with status — to run the applications themselves via Claude in the desktop browser. Group the shortlist by the board each posting came from (Indeed, Dice, ZipRecruiter) and give them a SEPARATE ready-to-paste prompt for every board that has postings in this run — never only the Indeed one. Postings carried by more than one board go under the board where they were found first.

Steps for the user, per board:
1. Download the N PDF resumes.
2. Open that board (Indeed, Dice, or ZipRecruiter) in the browser and log in.
3. Open the Claude desktop app (so Claude can act in that logged-in tab).
4. Paste that board's prompt below, with that board's shortlist and the matching resume files.

**Indeed prompt:**
> "I'm logged into Indeed in this tab. Here is my shortlist and the tailored resume for each role. Go through the list one by one, open each posting, and complete the application using the matching tailored resume. Start with the Easy Apply listings. If a posting asks something you can't answer from my resume, pause and ask me. Show me the first three before you submit them, then keep going."

**Dice prompt:**
> "I'm logged into Dice in this tab. Here is my shortlist and the tailored resume for each role. Go through the list one by one, open each posting, and complete the application using the matching tailored resume. Start with the Easy Apply listings. If a posting asks something you can't answer from my resume, pause and ask me. Show me the first three before you submit them, then keep going."

**ZipRecruiter prompt:**
> "I'm logged into ZipRecruiter in this tab. Here is my shortlist and the tailored resume for each role. Go through the list one by one, open each posting, and complete the application using the matching tailored resume. Start with the 1-Click Apply listings. If a posting asks something you can't answer from my resume, pause and ask me. Show me the first three before you submit them, then keep going."

Only print the prompts for boards that actually have postings in this run, each paired with that board's own shortlist (company, title, link, and the resume filename to use). Some postings on any board redirect to the employer's own site to apply; the apply session should treat those like any other and pause if it hits a login or a question it can't answer.

Then invite the user to run this Step 9 handoff so the applications can be tracked in the Claude desktop, and to confirm back whether it works. (This closing invitation is part of the final message, not a mid-run question.) Safety note for that apply session: it submits only with the user present and approving (first three shown before submitting), pauses on any question it can't answer from the resume, and never enters passwords, payment, or government-ID details — the user does those.

## Close
List the N postings (company, title, location, salary, source, link) each paired with its delivered PDF, then the Top/Stretch/Weak read, H-1B sponsorship status per role, every honest gap and filter, every bracketed placeholder the user needs to fill, and every default decision made mid-run. One page each.

## Recap
Offer all setup choices once as selectable menus (postings, recency, location, titles, project audit, tracker, boards, apply prompts; recommended option first, "Other" for custom) → no more questions → find N postings across the chosen boards (VA first, else remote/onsite/hybrid; dedupe across sources) → rank (H-1B flagged first) → for EACH posting: optional portfolio-project-fit → conditional-positioning → write → write-without-ai-tells → N individual PDF resumes → tracker → Step 9 apply handoff with one prompt per board → Close listing every default taken.