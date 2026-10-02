---
name: "job-search-flow"
description: "Run the job-search flow for a given resume: ask how many roles and the recency window, find exactly that many fitting Indeed postings (VA first, else remote+onsite+hybrid), rank by honest fit with H-1B sponsorship flagged first, tailor one one-page PDF resume per posting (conditional-positioning, optional portfolio-project-fit, Harvard + XYZ, final write-without-ai-tells), log to the tracker, then hand off to the Indeed apply step."
---

# Job-Search Flow

Run when the user hands over a resume and wants fresh roles found, ranked, and a tailored resume written for each. Works for any resume; re-run per resume. This skill is the spine; it calls other skills at set points (load each with the Skill tool when its step is reached).

## Step 0 — Ask the user (required, every run)
Ask, before searching:
1. **How many postings** to find for THIS resume. Their choice each time — never assume a number. Call it N. Everything is sized to N: find N postings, deliver N resumes. (15 → 15 postings → 15 PDFs.)
2. **Recency window.** Offer options: last 24 hours, last 3 days, last 5 days, last 7 days, or a custom duration the user names (down to minutes). Note honestly: Indeed's `search_jobs` returns a posted-on date at day granularity, so windows shorter than a day approximate to "today" — tell the user that if they pick a sub-day window.
3. **Location**, if they want to override the default. Default: **Virginia (VA) as primary priority**; if the user skips location or VA is thin, fall back to **remote + onsite + hybrid** as secondary. Ask if unsure.
4. Whether to run the optional **portfolio-project-fit** audit (see Steps 3–6).

## Other inputs
- The resume (attached file or path). Read it fully before anything else.
- Titles / field to search (default from the resume's field: e.g. AI Engineer, LLM Engineer, Machine Learning Engineer, Generative AI Engineer, Agentic AI Engineer, Full Stack Engineer Python).
- Tracker path, if logging (ask if unknown).

## Step 1 — Find exactly N postings (Indeed connector)
Use the Indeed `search_jobs` tool, country_code "US", one search per title × location, with VA as the primary location and remote/onsite/hybrid as the fallback per Step 0. Keep postings inside the chosen recency window, deduplicate by Job Link URL and Company+Title, select the N best-fit. If fewer than N exist, say so and widen titles/locations or the window until N is reached (or report the true maximum found). Pull `get_job_details` on each selected posting for real screening keywords and hard gates (years, clearance, sponsorship, required stacks).

## Step 2 — Rank honestly
Sort the N into Top / Stretch / Weak by BOTH skill match and realistic chance given seniority and gates. For each: one line on why, the real gap, and the exact ATS keywords it scans for. Never inflate fit. **Flag sponsorship explicitly, H-1B sponsorship as the main priority** — state whether each posting offers H-1B sponsorship; only if that is unavailable fall back to noting other work authorization (OPT, green card, citizenship, clearance). ALL N postings get a tailored resume — the ranking is guidance for the user, not a filter that drops any.

## Steps 3–6 — Tailor ONE resume per posting (loop over all N)
For EACH of the N postings, produce its own dedicated resume:
1. **portfolio-project-fit (OPTIONAL — only if the user said yes in Step 0)** — load the skill; audit the resume's projects against this role; pick which 3–4 projects to lead with and whether each is framed tightly.
2. **conditional-positioning** — load the skill; set the angle for this role: identity + target at the top, every claim tied to this role's value pillars, a committed primary role. Drives the summary, skills order, and bullet emphasis.
3. **Write the tailored resume**, applying 1–2. Rules, enforced:
   - Harvard guide: no personal pronouns; action-verb-first; reverse-chronological; Technical Skills after Education for tech; no photo, age, gender, or references; no line starting with a date; consistent formatting; ONE page.
   - Google XYZ on every bullet: accomplished X, measured by Y, by doing Z.
   - Honesty is non-negotiable. Never invent skills, tools, employers, or metrics. Use only numbers present in the source resume; where a real metric would help, leave a bracketed placeholder and tell the user to fill it. If a JD wants a skill the resume lacks, surface it as a gap — never add it.
   - Tailoring = reordering + emphasis + mirroring the JD's real language, not fabricating. Strip first-person summaries, stale dates, and anything a hiring manager flags in 10 seconds.
4. **write-without-ai-tells** — load the skill; run it over the finished prose as the FINAL content pass (never before positioning).

Building a shared master first is fine, but each posting must end with its own distinctly tailored resume.

## Step 7 — Produce N separate PDFs (required deliverable)
For each posting, build its resume as .docx with the `docx` skill (ATS-safe font, 0.5in margins, ~9.5–10pt body), verify ONE page (convert with `soffice.py --convert-to pdf`; check `pdfinfo` Pages == 1; tighten or condense the least-relevant entry until it fits, never below ~9pt), then export each to **PDF**. Required output: N individual PDF resumes, one per posting, each named for its company/role. Deliver all N with SendUserFile. Keep the .docx too for edits.

## Step 8 — Log to the tracker (if one exists)
Tracker "Job Tracker" columns (11): Date Found | Date Applied | Company | Title | Location | Salary | Fit | Status | Last Updated | Resume Used | Job Link. Stage the file, load with openpyxl, dedupe new rows by Job Link, append (Date Found = today, Status = "Not applied", Fit from Step 2, Resume Used = that posting's resume filename, Job Link as an "Apply" hyperlink), preserve formatting + the Status dropdown + Summary tab, commit back to the same path.

## Step 9 — Hand off to the Indeed apply step
After delivering the PDFs and updating the tracker, tell the user — clearly, with status — to run the applications themselves via Claude in the desktop browser:
1. Download the N PDF resumes.
2. Open Indeed in the browser and log in.
3. Open the Claude desktop app (so Claude can act in that logged-in tab).
4. Paste this prompt to that session, with the shortlist and the matching resume files:

> "I'm logged into Indeed in this tab. Here is my shortlist and the tailored resume for each role. Go through the list one by one, open each posting, and complete the application using the matching tailored resume. Start with the Easy Apply listings. If a posting asks something you can't answer from my resume, pause and ask me. Show me the first three before you submit them, then keep going."

Then ask the user to actually run this Step 9 handoff so the applications can be tracked in the Claude desktop, and confirm back whether it works. Safety note for that apply session: it submits only with the user present and approving (first three shown before submitting), pauses on any question it can't answer from the resume, and never enters passwords, payment, or government-ID details — the user does those.

## Close
List the N postings (company, title, location, salary, link) each paired with its delivered PDF, then the Top/Stretch/Weak read, H-1B sponsorship status per role, and every honest gap and filter. One page each.

## Recap
Ask N + window + location + optional project-fit → find N postings (VA first, else remote/onsite/hybrid) → rank (H-1B flagged first) → for EACH posting: optional portfolio-project-fit → conditional-positioning → write → write-without-ai-tells → N individual PDF resumes → tracker → Step 9 Indeed apply handoff. N, window, and location are the user's choice.