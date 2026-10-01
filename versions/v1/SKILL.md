---
name: "job-search-flow"
description: "Run the job-search flow for a given resume: find ~20 fresh fitting Indeed roles, rank by honest fit, then tailor a one-page resume to each target using conditional-positioning, portfolio-project-fit, Harvard + Google XYZ, and a final write-without-ai-tells pass, and log them to the tracker spreadsheet."
---

# Job-Search Flow

Run when the user hands over a resume and wants fresh roles found, ranked, and tailored resumes written. Works for any resume; re-run per resume. This skill is the spine; it calls three other skills at set points (load each with the Skill tool when its step is reached). It never uses the sanjeev-sriram-resume-pattern skill — that encodes one specific person's rules and does not apply.

## Inputs to confirm first
- The resume (attached file or path). Read it fully before anything else.
- Target count (default 20 roles).
- Titles to search (default: AI Engineer, LLM Engineer, Machine Learning Engineer, Generative AI Engineer, Agentic AI Engineer, Full Stack Engineer Python — adapt to the resume's actual field).
- Locations (default: remote + the user's metro).
- Recency window (default: posted in last 5 days).
- Tracker path, if logging (ask if unknown).

## Step 1 — Find roles (Indeed connector)
Use the Indeed `search_jobs` tool, country_code "US", one search per title × location. Keep only postings inside the recency window. Deduplicate by Job Link URL and Company+Title. Trim to the target count, best-fit first. Pull `get_job_details` on the strongest matches for real screening keywords and hard gates (years, clearance, sponsorship, required stacks).

## Step 2 — Rank honestly
Sort Top / Stretch / Weak by BOTH skill match and realistic chance given seniority and gates. For each: one line on why, the real gap, and the exact ATS keywords that posting scans for. Never inflate fit. Flag citizenship/clearance and visa-sponsorship filters explicitly. Have the user pick which roles to tailor for.

## Step 3 — Project fit (per target role) — call `portfolio-project-fit`
Load the `portfolio-project-fit` skill and run it to audit the resume's projects against that role. Use its verdict to choose which 3–4 projects to lead with and whether each is framed tightly. Feed the result into Step 5.

## Step 4 — Positioning (per target role) — call `conditional-positioning`
Load the `conditional-positioning` skill. Use it to set the angle: identity + target at the top, every claim tied to that role's value pillars, a committed primary role (and a deliberate secondary if any). This drives the summary, skills order, and bullet emphasis in Step 5.

## Step 5 — Write the tailored resume
Build a master first, then one per target, applying Steps 3–4. Rules, enforced:
- **Harvard guide:** no personal pronouns; action-verb-first; reverse-chronological; Technical Skills after Education for tech; no photo, age, gender, or references; no line starting with a date; consistent formatting; ONE page.
- **Google XYZ** on every bullet: accomplished X, measured by Y, by doing Z.
- **Honesty is non-negotiable.** Never invent skills, tools, employers, or metrics. Use only numbers present in the source resume; where a real metric would strengthen a bullet, leave a clear bracketed placeholder and tell the user to fill it. If a JD wants a skill the resume doesn't support, surface it as a gap — never add it.
- Tailoring = reordering + emphasis + mirroring the JD's real language, not fabricating. Strip first-person summaries, stale dates, and anything a hiring manager flags in 10 seconds.

## Step 6 — De-AI pass (per resume, last on the prose) — call `write-without-ai-tells`
Load the `write-without-ai-tells` skill and run it over the finished resume prose to strip machine-written tells. Always the final content pass, after Steps 3–5 are set — never before, or it rewrites content that positioning still needs to shape.

## Step 7 — Produce files
- Use the `docx` skill to build each resume as .docx (ATS-safe font, 0.5in margins, ~9.5–10pt body).
- Verify one page: convert with `soffice.py --convert-to pdf` and check `pdfinfo` Pages == 1; tighten spacing or condense the least-relevant entry until it fits. Never shrink below ~9pt.
- Export PDF when asked. Deliver with SendUserFile.

## Step 8 — Log to the tracker (if one exists)
Tracker "Job Tracker" sheet columns (11): Date Found | Date Applied | Company | Title | Location | Salary | Fit | Status | Last Updated | Resume Used | Job Link. Stage the file, load with openpyxl, dedupe new rows by Job Link, append (Date Found = today, Status = "Not applied", Fit from Step 2, Job Link as an "Apply" hyperlink), preserve formatting + the Status dropdown + Summary tab, commit back to the same path.

## Close
State top picks, the stretch/weak split, and every honest gap and filter. Offer PDFs, cover letters, or tracker logging as next steps. One page each.

## Skill order recap
job-search-flow (spine) → portfolio-project-fit (Step 3) → conditional-positioning (Step 4) → write content (Step 5) → write-without-ai-tells (Step 6) → files + tracker. portfolio-project-fit is optional; the other two are standard.