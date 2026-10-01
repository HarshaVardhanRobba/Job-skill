---
name: "job-search-flow"
description: "Run when the user hands over a resume and wants fresh roles found, ranked, and a tailored resume written for each."
---

# Job-Search Flow

Run when the user hands over a resume and wants fresh roles found, ranked, and a tailored resume written for each. Works for any resume; re-run per resume. This skill is the spine; it calls other skills at set points (load each with the Skill tool when its step is reached).

## Standing profile (defaults for Harshavardhan Robba; use without asking)
- Base resume: `C:\Users\robba\OneDrive\Desktop\New folder (2)\Robba_Harshavardhan_Resume.pdf` (stage it from the device and read it fully). The **Reference resume template** at the end of Step 7 is the exact LaTeX source of the user's resume and the single source of truth for layout AND base content (projects, bullets, skills, jobs, links). If the PDF and the template disagree, the template wins.
- Tracker: `C:\Users\robba\OneDrive\Desktop\New folder (2)\Harshavardhan_Robba_Job_Tracker.xlsx`. Always log here, in this one file; do not ask. Update the original file itself, do not make a separate copy (see Step 8).
- Boards: Dice (`https://www.dice.com/home-feed`) and Indeed (`https://www.indeed.com/`).
- Page length: there is NO page limit. Never trim projects or bullets to fit a page, and never check page count.
- Screening info source (read it whenever a form asks something the list below does not cover): the screenshot `C:\Users\robba\OneDrive\Pictures\Screenshots\Screenshot 2026-10-10 194828.png`. It sits outside the connected folder, so request folder access to `C:\Users\robba\OneDrive\Pictures\Screenshots` with `device_request_folder_access` if it is not connected, then stage the file and read it. The list below was copied from it and matches it.
- Screening answers (from the user's profile screenshot; reuse for every form; the answers are already saved, so do not ask for them again):
  - Authorized to work in the US: Yes (F-1 OPT, EAD).
  - Require sponsorship now or in the future: Yes.
  - Start date: immediately. Salary: negotiable.
  - Veteran: No. Disability: No. Gender: Male. LGBTQ+: No. Race: Asian. Hispanic or Latino: No. Sexual orientation: Heterosexual. Pronouns: He/Him.
  - Willing to relocate: Yes. On-site/relocation willingness: Yes for any posting inside the location choice the user made in Step 0.
  - Profile skills the user may confirm as used: LangChain, LangGraph, RAG, retrieval pipelines, agent workflows, tool calling, prompt engineering, DeepEval, Azure OpenAI, OpenAI Realtime, Gemini 2.0, function calling, structured outputs, guardrails, hallucination detection, Node.js, Python, tRPC, REST, async streaming, API design, Inngest, Next.js, TypeScript, PostgreSQL, MongoDB, Prisma, SQL, ETL, ELT, PySpark, Databricks, Amazon RDS, Docker, Azure, AWS, GCP, CI, MCP, Twilio WebSockets, Deepgram STT, Stream Video SDK, WebRTC, real time audio processing.
  - Technical writing is real experience: Technical Writer at JavaTpoint (Sep 2022 to Feb 2023). Technical-writer, documentation and knowledge-article roles are valid targets.
  - Years of experience on any skill: answer only what the resume supports. Never inflate, never tick "yes" for a skill outside the list above or the resume. If a REQUIRED question cannot be answered truthfully, skip that application, log it as Held with the question, and ask the user at the end.
  - C2C or 1099 contract: OK (user confirmed 2026-10-13). W2 contract: OK.
  - Direct W2 employment from day one: Yes. Work authorization choice list: pick "Other (H1B, OPT/EAD, NAFTA, etc.)".
  - Questions with no stored answer: do not guess. Hold that application, ask the user once, then store the answer here.
  - The user already applied to many Dice jobs by hand and in earlier sessions, so the tracker alone does not know every applied job. See the Step 1 already-applied check.

## Core rule: never change the request on your own
The user's N, recency window, location, titles, boards and seniority are fixed by their Step 0 answers. If the search cannot deliver what was asked, DO NOT widen, relax, pad, substitute or quietly settle for fewer on your own. Stop, tell the user exactly what was found and why more were not found, offer selectable options, and wait for their pick. Only then change anything, and only what they picked.
Standing exceptions the user chose on 2026-10-13 (use them automatically, in this order, and say so in the shortfall message): (1) the Dice recommended-jobs fallback in Step 1b; (2) the Tier 2 relaxation below. Both keep the same recency window. The Indeed site search in Step 1a is part of the normal search for Indeed, not a widening.

## Two-tier screening rule (user instruction, 2026-10-13)
- **Tier 1 (first pass):** postings that pass the normal gates below. Apply to these first.
- **Tier 2 (second checkpoint, used only when Tier 1 cannot reach N):** relax everything except citizenship. A posting that is Easy Apply on Dice, inside the window, and not clearly citizenship-bound is applied to even when it asks for 5+ years, is senior or lead, is W2 only, is a different field the resume supports (for example technical writing), or is far away or onsite. Also widen years, remote and location as needed, searching as effectively as possible.
- **The only rejection in Tier 2 is clear citizenship:** "U.S. citizen required", green-card only, or a clearance (Secret, TS/SCI, public trust) that itself requires citizenship. Do not reject on years, seniority, W2, field or skill gaps in Tier 2; the resume stays truthful (never claim a skill the resume lacks) and the Gap is stated in the Close.
- Still never apply where the form needs an untruthful answer; hold and report it.

## Step 0 — Offer the setup choices up front, once, as selectable options (required, every run)
Prepare silently, then present the decisions as a **pick-from-options menu** before any searching, tailoring or file work. After the user picks, run the flow until the first checkpoint (Step 1 shortfall check) without asking anything else.

**Prepare silently first (no questions yet):**
- Stage and read the base resume from the Standing profile path. List every project and every job in it (cross-check against the Reference resume template); this is the PROJECT LIST used in Step 3–6.
- Stage the tracker from the Standing profile path and note its row count.
- Check that the Dice and Indeed connectors are connected, and that Claude in Chrome is available. If the Indeed connector is not connected or errors, do NOT drop Indeed: search it with Step 1a (Indeed site search in Chrome) alone and say the connector was down.
- Work out the default titles from the resume's field (AI Engineer, LLM Engineer, Machine Learning Engineer, Generative AI Engineer, Agentic AI Engineer, Full Stack Engineer Python).

**Ask with AskUserQuestion (one call, four questions). The tracker, base resume, boards, apply step and screening answers are NOT asked; they come from the Standing profile.**
1. Header "Postings" — "How many job postings should I find?" — options: 5 / 10 / 15 / 20. The batch size is the user's choice; do not mark one as recommended. Other = custom number. N postings, N resumes.
2. Header "Recency" — options: Last 3 days / Last 5 days / Last 24 hours / Last 7 days. Job tools report posted dates at day granularity.
3. Header "Location" — options: Virginia first, then everywhere / Remote only / Washington DC area / Anywhere in the US.
4. Header "Job titles" — options: Based on my resume / AI, LLM and agentic roles only / Broader: add ML, data and full-stack. (Technical writing is also in scope under Tier 2.)

If AskUserQuestion is unavailable, print the same menus as a lettered list and accept replies like "1A 2B 3A 4A". Skip the project-fit audit by default.

**After the answers:** restate the choices in one short confirmation line and proceed. If the run is unattended, use Recency Last 3 days, Location Virginia first then everywhere, Titles based on the resume, N = 10, and say so at the top.

## Step 1 — Find exactly N postings (Dice + Indeed)
Use each connector's `search_jobs`, one search per title x location, following the Location choice. Use as many title variants as the Titles choice allows. Dice `search_jobs` notes: `posted_date` takes ONE, THREE or SEVEN (not THREE_DAYS); it returns 5 results per page, so page deeper (page 2, 3, ...) on every productive query before calling it exhausted; `get_job_details` takes the `guid`, not the `id`. Search Virginia first; search the rest of the US only if Virginia has too few. Dice and Indeed only unless the user adds another board. The Indeed connector has no date filter and its "Posted on" dates are unreliable (verified 2026-10-13: it showed Sept 30 for postings that were live and fresh on indeed.com, and a Virginia search returned nothing usable inside a 3-day window while indeed.com's own 3-day filter returned 25 jobs). So NEVER conclude "Indeed has 0 usable postings" from the connector alone: whenever Indeed is searched, also run Step 1a. Run Indeed connector searches ONE AT A TIME, not in parallel: the connector rate-limits (error code -32429, "Try again in N seconds"); on that error wait the stated seconds and retry the same search once, and never count a rate-limited or errored search as "no results". If one board returns nothing inside the window after all its steps (Dice: search plus Step 1b; Indeed: connector plus Step 1a), continue with the other board alone; say which board returned nothing and what was tried. Deduplicate by Company + Title and job URL, and also against the tracker rows already logged (by Job Link and Company+Title); drop anything already in the tracker. Pull full details (`get_job_details` for Dice; the job detail pane or `viewjob` page for Indeed) for every candidate. Keep each posting's real URL exactly as returned.

**Already-applied check (required, before ranking and before any resume is written).**
1. Sync the tracker with Dice first: open `https://www.dice.com/my-jobs?type=applied` in Claude in Chrome, `get_page_text` on every page (use the "Next" link until the last page), and add every listed job that is not in the tracker as Status "Applied" (Date Applied from the "Applied today / 1d ago" text; Resume Used "(not tracked)"). For listed jobs already in the tracker with Status other than Applied, set them to Applied. Match by title plus company, loosely, because Dice shows aggregator names (eFinancialCareers, Radancy) for employers the tracker lists by their own name. Commit and re-stage to verify.
2. Then, for every candidate that survives dedupe, open `https://www.dice.com/job-applications/<guid>/wizard` (guid from the job URL). If the page shows "You've already applied" or lands on `/wizard/applied`, drop it as Already applied. Do this in 2 to 3 browser tabs at once. Never build a resume for a posting that is already applied.
3. The tracker plus Dice's Applied list are the record. Never rely on the tracker alone. For Indeed candidates, also drop any posting whose Indeed page already shows it as applied.

**Tier 1 hard gates are applied BEFORE ranking and BEFORE any resume is written.** Drop at this point (they become Tier 2 candidates, except citizenship, which is dropped for good), and list them in the shortfall message with the reason: citizen-only or green-card-only, security clearance required, "no sponsorship / no OPT / no visa" statements that exclude the user, 5 or more required years (read the WHOLE description, including the Must have list, for "5+", "7+", "10 years" and similar), W2-only vs C2C-only mismatches, and posting already closed. Never build a resume for a closed posting. Check the posting is still open when it is fetched.

## Step 1a — Indeed site search in Chrome (required whenever Indeed is searched; added 2026-10-13)
The Indeed connector alone is not trusted for recency or for "zero results" (see Step 1). Run this step for every Indeed search, in addition to the connector, using Claude in Chrome in the user's real logged-in Indeed (new tab; if Indeed shows a login wall, STOP and tell the user to sign in; never enter a password).
1. **Search URL per title x location:** `https://www.indeed.com/jobs?q=<title, + for spaces>&l=<location>&fromage=<N>&sort=date`. Map the Recency choice to `fromage`: Last 24 hours = 1, Last 3 days = 3, Last 7 days = 7, Last 5 days = 7 (Indeed has no 5-day value; then drop cards older than 5 days using the age shown on the card or detail pane). Page with `&start=10`, `&start=20`, ... on every productive query before calling it exhausted.
2. **Read each results page** with `get_page_text` (one call per page). Cards show title, company, location, pay, "Easily apply" and "New" tags, but the list text may not show the posting age, so the `fromage` filter is the recency gate. Verified 2026-10-13: `fromage=3&sort=date` for "AI Engineer" in Virginia returned 25 jobs, several tagged "New".
3. **Judge relevance honestly.** Indeed's results for a title include many unrelated roles (cyber, civil, network, manufacturing). Keep only roles that fit the Titles choice (or Tier 2 field-adjacent roles the resume supports).
4. **Get each kept card's real URL and details:** open the card (the detail pane text is included in `get_page_text`), and collect the job link with a read-only `javascript_tool` call on the list page (read links only, for example `a[data-jk]` job keys mapped to `https://www.indeed.com/viewjob?jk=<jk>`; never set form values). Read the FULL description for the Tier 1 gates (citizenship, clearance, years, sponsorship, W2/C2C, closed). Where the card or page shows the posting age ("Posted 2 days ago", "Active 1 day ago"), confirm it is inside the window; if no age is shown anywhere, rely on the `fromage` filter and note "age from Indeed filter" in the Close.
5. **Apply path:** note whether the card is "Easily apply" (Indeed form) or "Apply on company site" (employer site). Apply only through Indeed Easy Apply per Step 9; for company-site roles that need an account, password or CAPTCHA, skip and report them.
6. **Optional extra pool, only if still under N after steps 1 to 5:** the Indeed home feed `https://www.indeed.com/?from=gnav-homepage` (sections "Matches your preferences", "Based on your recent applications", "Based on your recent searches"). Its list text shows NO posted ages, so a feed posting counts toward N only after its age is verified (detail page or a search with `fromage`). Feed postings whose age cannot be verified are listed in the shortfall message as "recency unverified" and are not applied to.
7. **Reporting rules:** the Close and any shortfall message state, for Indeed, how many came from the connector and how many from the site search, and never say "Indeed gave 0" unless the connector AND this step both returned 0 inside the window. If the connector was rate-limited or errored, say so.
8. Dedupe these results against the connector results and the tracker by Company + Title and URL, then continue with the Tier 1 gates, ranking and the rest of the flow exactly as for any posting. Close the tabs opened here when done.

## Step 1b — Recommended-jobs fallback (standing instruction, 2026-10-13)
When Step 1 (and Step 1a for Indeed) cannot deliver N usable postings, before the shortfall checkpoint, go to `https://www.dice.com/recommended-jobs` in Claude in Chrome (the user's logged-in Dice) and look for more there, then apply to the usable ones directly.
1. Page through `?page=1`, `?page=2`, ... (about 20 cards per page, up to 20 pages). The list reshuffles between loads, so collect guids in the same call that reads each page. `get_page_text` gives title, company, location, age ("Today", "Yesterday", "3d ago") and the button ("Easy Apply", "Apply Now", "Applied"). Keep only cards inside the user's recency window and drop "Applied" cards.
2. Get each kept card's guid with `javascript_tool` on the list page (read-only: collect `a[href*="/job-detail/"]` hrefs and map guid to title or card text; this is allowed because it only reads links, unlike setting form values), then run `get_job_details`.
3. Judge each card by the two-tier rule: Tier 1 first; if Tier 1 does not reach N, go to Tier 2 and apply to every Easy Apply card in the window that is not clearly citizenship-bound, including technical-writer and other field-adjacent roles the resume supports.
4. Apply only where the Dice wizard works (Step 9). Cards marked "Apply Now" can still use the Dice wizard (Kforce, Eliassen did) but some send the user to the employer site: if `/wizard` shows no "File options" button or redirects off Dice, skip it and report it.
5. Tailor, build, check, log and apply exactly as for any other posting (Steps 3 to 10). Show in the Close which postings came from the recommended-jobs page and which tier each was in.
6. If still under N after the fallback and Tier 2, run the shortfall checkpoint below.

**Shortfall checkpoint (required whenever fewer than N usable postings are found, after Step 1a, Step 1b and Tier 2).** Do this BEFORE writing any further resume:
1. Tell the user plainly how many were found out of N, list the postings found (company, title, location, link), and why the rest were not found (name any board that was down or rate-limited, and which Indeed source, connector or site search, produced what). Be concrete about the pool: the recommended and search pools are large (hundreds), but most hits fail citizenship, the window, or the Easy Apply requirement.
2. Ask with AskUserQuestion, multi-select, recommended first: Widen the window / Add title variants / Widen the location / Continue with only the postings found / Retry the failed board.
3. Wait. Apply exactly what was selected. If the user picks nothing, change nothing and ask again in plain text. If still short, show the new count and ask again. Never loop silently.

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

## Steps 3–6 — Tailor ONE resume per posting (write them IN PARALLEL with subagents)
**Setup once per run, in the working folder (use `/home/claude/work/<folder>/`, which the browser upload tool accepts):**
- Save the Reference resume template (end of Step 7) as `template.tex`. Write `build_tex.py` and `build.sh` (Step 7; copy them exactly from the code blocks below; if the copy has a stray ``` line at the top of build.sh, delete it).
- Check a LaTeX engine exists (`which xelatex pdflatex`). If none, try `apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-xetex`; if the network refuses, tell the user plainly and stop before tailoring.
- Write `gen.py`: a Python module holding the base resume as data, taken from `template.tex` (every project with its bullets, the skill lines, education, the two jobs with their bullets, and each entry's link text and URL), and `build(file, role, summary, order, skorder, lead=None, over=None, exp_over=None, exp_first=False)` that writes the spec JSON (`role` = the header role line, see Step 7; `exp_first` = writes `experience_first`, see the section-order rule below; `order` = all project keys, most relevant first; `lead` = bullet-index reorder per project; `over` = rewrite one bullet; skill item text is fixed). The generator MUST emit the template spec JSON of Step 7 with the `role` field, the `links` array and each project's `link`/`url`, never a docx layout, and never a label such as "Target role" or "Targeted role" in front of the role line.
- Write `check.py` (the Step 7 resume check; it scans every PDF in the folder and prints one OK or error line per file). Prove the setup by building one resume yourself first.

**Then spawn one subagent per posting in ONE message** (subagent_type general-purpose; they run at the same time, about 20 seconds for five resumes). Each prompt must be self-contained, because a subagent has none of this conversation: working folder; read gen.py and a worked example; the exact output names (`spec_<X>.py` calling build once, `<Company>_<Role>.json`, the build.sh command, run check.py until that file's line says OK, copy the PDF to the apply folder); the strict rules below; and the posting's key requirements plus the list of tools the resume does NOT have (so none are added). The subagent replies in under 80 words: PDF name, angle, honest gaps. Do not let subagents edit shared files (gen.py, check.py, build_tex.py, build.sh, template.tex). After they return, run `python3 check.py` yourself and view the first PDF. For a batch of 12 or fewer, writing the specs directly in one script (a dict of summary, project order, skill order per posting) is fine and faster.
For EACH kept posting (the subagent or you):
1. **conditional-positioning** — load the skill; set the angle for this role: identity + target in the opening words of the Summary, every claim tied to this role's value pillars, a committed primary role. The target role is expressed in two places only: the header role line (the `role` field, Step 7) and the opening words of the Summary. Write the `role` as a plain professional title in the posting's own title language, `Title | keyword, keyword, keyword` (for example `AI Engineer | LLM Applications, RAG, Agent Systems`), with the 2 or 3 skills the posting cares about most after the divider, using only skills the resume truly has. Never prefix it with "Target role", "Targeted role", "Applying for" or any label, and never put the company name in it.
2. **Write the tailored resume content.** Rules, enforced:
   - **Every resume contains ALL projects and ALL jobs from the base resume (the PROJECT LIST from Step 0). Never drop a project to save space or because it seems less relevant.** For each project and job, compare its existing bullets against this posting's requirements. If the existing bullets already fit the posting, keep them as they are and leave them alone. If they do not, rewrite or add bullets so the project's real work is framed in the posting's language: lead with the facts of that project that match what the posting asks for, mirror its keywords where they truly apply, and reorder bullets so the most relevant ones come first. Put the projects most relevant to the posting first in the Projects section, and the rest after them, all present. A project missing from a draft is added back. Rewriting means re-expressing real work; it never adds a tool, skill, scope or result that the project does not have.
   - **Bold keywords as the template does.** In bullets, wrap the technologies and terms that matter to this posting in `**double asterisks**` (build_tex.py turns them into `\textbf{}`), exactly like the template bolds LangGraph, Inngest, PostgreSQL and so on. Bold only real tools the bullet names.
   - **Section order by posting focus (user instruction, 2026-10-13).** Read what the posting mostly asks for. If most of its duties and requirements are about work the projects do not show (technical writing, documentation, knowledge articles, content, or other non-engineering duties), put Experience ABOVE Projects (`exp_first=True` / `"experience_first": true`), and in the Experience bullets lead with the facts that match the posting (for example the JavaTpoint runnable-sample writing for a technical-writer role). If the posting is mostly engineering, AI or agent work, keep Projects above Experience. When the posting mixes both, go by which the larger share of its requirements points to. Say which order each resume got, and why in a few words, in the Close.
   - Harvard guide: no personal pronouns; action-verb-first; reverse-chronological; Technical Skills after Education; no photo, age, gender or references; no line starting with a date. No page limit.
   - Google XYZ on every bullet: accomplished X, measured by Y, by doing Z.
   - Honesty is non-negotiable. Never invent skills, tools, employers or metrics. **Never leave bracketed placeholders or empty slots.** Numbers come only from these sources: (a) the base resume and Reference resume template (including 1000+ users, 500+ registrations, 300+ articles); (b) figures the user states in chat; (c) facts the assistant can count and verify itself from the user's own material, such as the number of API endpoints, tools, agents, services, data sources or integrations in a repo or project description. Do NOT make up user counts, latency, accuracy, revenue or percentage improvements. Where no real number exists, write the bullet without one: state what was built, for whom and with which tools, plus the outcome in plain words, and drop any clause that depended on the missing figure. When a run ends with bullets that have no numbers, tell the user they can supply real figures (or authorize counting from their repos) and the assistant will add them.
   - If a JD wants a skill the resume lacks (for example Palantir, Java/Spring, Angular), surface it as a gap in the Close; never add it. For Tier 2 roles outside AI and engineering (technical writing), the Summary leads with the real writing experience and never claims domain experience the resume lacks.
   - Tailoring = reordering + emphasis + mirroring the JD's real language.
3. **write-without-ai-tells** — load the skill; run it over the finished prose as the FINAL content pass (no em dashes, no banned words).
4. Save the finished content as a **spec JSON** (schema in Step 7).

## Step 7 — Produce separate PDFs in the FIXED template layout (LaTeX), delivered as one ZIP per board (required deliverable)
**The layout is the user's LaTeX template, and it is fixed (user instruction, 2026-10-13: follow the exact txt template format for every resume).** Every resume is the Reference resume template below with only the content changed. NEVER improvise or edit the preamble, fonts, colours, spacing, margins, section order macros (`\row`, `\bi`, `\bstart`, `\bend`) or heading style, and never build resumes in docx, python-docx or any other format. What the template looks like: Helvetica (psnfss `helvet`, scaled 0.95), centred bold name at `\LARGE`, a `\footnotesize` contact line directly under it (phone, email, then the LinkedIn, GitHub and Portfolio links, separated by bullets), then the role line in `\small\bfseries` accent colour burgundy `128,0,32` (the `role` field: `Title | keyword, keyword, keyword`, written with `$|$`), then UPPERCASE bold section headings with a bottom rule, each entry as a two-line `\row` (bold left text and right text on line one, italic left sub-line and right text on line two), `\small` bullets with the `\textbullet` label, default section order Summary → Education → Technical Skills → Projects → Experience, Letter size. The role line carries NO label (never "Target role", "Targeted role" or similar), NO company name and NO tagline. **Experience-first exception:** when the posting is mostly about work the projects do not show, set `"experience_first": true` in the spec and the order becomes Summary → Education → Technical Skills → Experience → Projects. Nothing else changes, and every project and job is still present. The resume may run to as many pages as the content needs. The template has no Certifications section; do not add one.

**Embedded links are required.** In the header, "LinkedIn", "GitHub" and "Portfolio" are clickable hyperlinks (the `links` array), and every project's right-hand link text is a clickable, underlined hyperlink (`link` = visible text, `url` = target). Link registry for Harshavardhan Robba (identical to the template):
- LinkedIn: https://www.linkedin.com/in/harshavardhanrobba
- GitHub: https://github.com/HarshaVardhanRobba
- Portfolio: https://portfolio-harshavardhanrobba.vercel.app/
- Websito: visible text "websito-eight.vercel.app", url https://websito-eight.vercel.app/
- Web-base: visible text "web-base-workflow.vercel.app", url https://web-base-workflow.vercel.app/
- Elara: visible text "elaravoiceai.onrender.com", url https://elaravoiceai.onrender.com
- Brand Guardian: "Source on GitHub", url https://github.com/HarshaVardhanRobba/Brand_guardian
- Pharmacy Voice Agent: "Source on GitHub", url https://github.com/HarshaVardhanRobba/Voice-Agent
- Bizpulse: "Source on GitHub", url https://github.com/HarshaVardhanRobba/Bizpulse
- TeamOmnifield: no link (empty link and url).
After building, verify the links survived into the PDF (for example `python3 -c "import re,sys;print(sorted(set(re.findall(rb'/URI\s*\(([^)]*)\)',open(sys.argv[1],'rb').read()))))" file.pdf`).

Setup once per run is in Steps 3–6 (template.tex, build_tex.py, build.sh, gen.py, check.py). For each posting: write `<Company>_<Role>.json`, then run `bash build.sh <Company>_<Role>.json Harshavardhan_Robba_Resume_<Company>_<Role>`. It writes the .tex and compiles it to PDF with no page check; move the PDF to the target folder with `mv`. Render and look at at least the first PDF.

**Resume check before upload (required, automatic).** For every resume, run a script (`pdftotext` on each PDF) that fails the run if any of these are true: any project or job from the base resume (the PROJECT LIST) is missing by name; a square-bracket placeholder appears; a number or percentage appears that is not in the base resume or template, was not stated by the user, and is not a verified count from the user's own material; a skill or tool name appears that is not in the base resume, the template or the Standing profile skills list; an em dash appears; the expected hyperlinks (LinkedIn, GitHub, Portfolio, the three live project URLs, the three source URLs) are missing from the PDF; the role line is missing from the header or is empty; the word "target" or "targeted" appears in the header (the first 4 lines of text); the company name appears in the role line; the Experience and Projects headings are in the wrong order for the spec's `experience_first` value; LaTeX left a stray `\textbf`, `**` or `\` fragment in the text. Fix the spec and rebuild until clean.

**Deliver the PDFs as ONE ZIP PER BOARD**, named `Dice resumes.zip` and `Indeed resumes.zip` (only boards with postings; a later round in the same session may use a suffix such as `(round 2)`). Each ZIP holds only that board's PDFs, flat. Check with `unzip -l` and confirm the PDF count equals the number of kept postings. Send the ZIPs with SendUserFile. Copy the PDFs to a folder under `/home/claude/work/` (this path is accepted by the browser upload tool; `/mnt/user-data/outputs/` subfolders are rejected) for the apply step. Also offer the `.tex` of any resume on request.

**Spec JSON schema (`role` is the unlabelled header role line; `experience_first` swaps Experience above Projects; there is no "target" field; gen.py `build` writes this for you; bullets and summary may contain `**bold**` markup, plain text otherwise, and are LaTeX-escaped by build_tex.py, so write `C#` and `85%` as plain text):**
```json
{
  "name": "Harshavardhan Robba",
  "phone": "+1-703-853-6964",
  "email": "robbaharsha834@gmail.com",
  "role": "AI Engineer | LLM Applications, RAG, Agent Systems",
  "experience_first": false,
  "links": [
    { "label": "LinkedIn", "url": "https://www.linkedin.com/in/harshavardhanrobba" },
    { "label": "GitHub", "url": "https://github.com/HarshaVardhanRobba" },
    { "label": "Portfolio", "url": "https://portfolio-harshavardhanrobba.vercel.app/" }
  ],
  "summary": "role-tailored summary, 1 to 3 lines, no pronouns",
  "education": [ { "school": "", "loc": "", "degree": "", "date": "" } ],
  "skills": [ { "label": "Languages", "items": "comma-separated skills actually in the resume" } ],
  "projects": [ { "name": "Websito | Agentic Website-Generation SaaS", "meta": "tech stack", "link": "websito-eight.vercel.app  (or: Source on GitHub, or empty)", "url": "https://websito-eight.vercel.app/  (or the GitHub repo URL, or empty)", "bullets": ["XYZ bullet with **bold** keywords"] } ],
  "experience": [ { "org": "", "loc": "", "title": "", "date": "", "bullets": ["XYZ bullet"] } ]
}
```
Bullet counts follow the template (4 to 8 per project, 2 per job, 1 for JavaTpoint); rewrite in place, never trim to fit. All projects present, most role-relevant first.

**build.sh (no page limit):**
```bash
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
```

**build_tex.py** (fills the template; the preamble is read from `template.tex`, so the layout can never drift):
```python
# usage: python3 -I build_tex.py spec.json out.tex
import json, os, re, sys

SPECIALS = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#',
            '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}

def esc(t):
    return ''.join(SPECIALS.get(c, c) for c in t)

def fmt(t):  # escape, then turn **x** into \textbf{x}
    parts = re.split(r'\*\*(.+?)\*\*', t)
    return ''.join(esc(p) if i % 2 == 0 else r'\textbf{' + esc(p) + '}' for i, p in enumerate(parts))

def title(t):  # names and role lines: ' | ' becomes $|$
    return esc(t).replace(' | ', ' $|$ ')

def row(a, b, c, d):
    return r'\row{%s}{%s}{%s}{%s}' % (a, b, c, d)

def bullets(items):
    return [r'\bstart'] + [r'\bi{%s}' % fmt(b) for b in items] + [r'\bend']

def link(text, url):
    if not text:
        return ''
    return r'\href{%s}{\underline{%s}}' % (url, esc(text))

spec = json.load(open(sys.argv[1], encoding='utf-8'))
here = os.path.dirname(os.path.abspath(__file__))
template = open(os.path.join(here, 'template.tex'), encoding='utf-8').read()
preamble = template.split(r'\begin{document}')[0]

L = [preamble.rstrip(), r'\begin{document}', r'\begin{center}',
     r'{\LARGE\bfseries %s}\\[3pt]' % esc(spec['name'])]
hdr = r'{\footnotesize %s $\bullet$' % esc(spec['phone'])
hdr += '\n' + r'\href{mailto:%s}{%s}' % (spec['email'], esc(spec['email']))
for l in spec['links']:
    hdr += r' $\bullet$' + '\n' + r'\href{%s}{%s}' % (l['url'], esc(l['label']))
hdr += r'}\\[3pt]'
L += [hdr, r'{\small\bfseries\color{accent} %s}' % title(spec['role']),
      r'\end{center}', r'\vspace{-8pt}', '']

def summary():
    return [r'\section{Summary}', r'{\small %s}' % fmt(spec['summary']), '']

def education():
    rows = [row(esc(e['school']), esc(e['loc']), esc(e['degree']), esc(e['date'])) for e in spec['education']]
    return [r'\section{Education}', (r'\\[2pt]' + '\n').join(rows), '']

def skills():
    out = [r'\section{Technical Skills}', r'\begin{itemize}[leftmargin=0em,label={},itemsep=1pt]']
    out += [r'  \item \textbf{%s:} %s' % (esc(s['label']), esc(s['items'])) for s in spec['skills']]
    return out + [r'\end{itemize}', '']

def projects():
    out = [r'\section{Projects}', '']
    for p in spec['projects']:
        out.append(row(title(p['name']), '', esc(p['meta']), link(p.get('link', ''), p.get('url', ''))))
        out += bullets(p['bullets']) + ['']
    return out

def experience():
    out = [r'\section{Experience}']
    for x in spec['experience']:
        out.append(row(esc(x['org']), esc(x['loc']), esc(x['title']), esc(x['date'])))
        out += bullets(x['bullets'])
    return out + ['']

L += summary() + education() + skills()
L += (experience() + projects()) if spec.get('experience_first') else (projects() + experience())
L += [r'\end{document}', '']
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(L))
print('wrote', sys.argv[2])
```

**Reference resume template** (the user's exact file, supplied 2026-10-13; save as `template.tex`; it is the single source of truth for layout and base content; never alter anything above `\begin{document}`):
```latex
%!TEX program = xelatex
% Compiles with XeLaTeX or pdfLaTeX (font: Helvetica via psnfss, standard in TeX Live)
\documentclass[letterpaper,10pt]{article}
\usepackage[empty]{fullpage}
\usepackage[T1]{fontenc}
\usepackage[scaled=0.95]{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{titlesec}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\definecolor{accent}{RGB}{128,0,32}
\addtolength{\oddsidemargin}{-0.55in}
\addtolength{\evensidemargin}{-0.55in}
\addtolength{\textwidth}{1.1in}
\addtolength{\topmargin}{-0.7in}
\addtolength{\textheight}{1.4in}
\raggedbottom\raggedright
\setlength{\parindent}{0pt}\setlength{\tabcolsep}{0pt}
\titleformat{\section}{\bfseries\normalsize\raggedright}{}{0em}{\MakeUppercase}[\vspace{-5pt}\rule{\textwidth}{0.5pt}]
\titlespacing*{\section}{0pt}{4pt}{1pt}
\renewcommand{\arraystretch}{0.92}
\newcommand{\bi}[1]{\item{\small #1}}
\newcommand{\row}[4]{\begin{tabular*}{\textwidth}[t]{l@{\extracolsep{\fill}}r}
\textbf{#1} & \small #2 \\ \textit{\small #3} & \small #4 \\ \end{tabular*}\vspace{0pt}}
\newcommand{\bstart}{\begin{itemize}[leftmargin=0.16in,itemsep=0.8pt,parsep=0pt,topsep=1pt,label=\textbullet]}
\newcommand{\bend}{\end{itemize}\vspace{1pt}}
\begin{document}
\begin{center}
{\LARGE\bfseries Harshavardhan Robba}\\[3pt]
{\footnotesize +1-703-853-6964 $\bullet$
\href{mailto:robbaharsha834@gmail.com}{robbaharsha834@gmail.com} $\bullet$
\href{https://www.linkedin.com/in/harshavardhanrobba}{LinkedIn} $\bullet$
\href{https://github.com/HarshaVardhanRobba}{GitHub} $\bullet$
\href{https://portfolio-harshavardhanrobba.vercel.app/}{Portfolio}}\\[3pt]
{\small\bfseries\color{accent} Software Engineer $|$ AI Agents, Full Stack, Backend}
\end{center}
\vspace{-8pt}

\section{Summary}
{\small Full stack and agentic AI engineer working in TypeScript, Python, and C\# over PostgreSQL.}

\section{Education}
\row{University of North Texas}{Denton, TX}{Master of Science in Computer Science (AI/ML and Data Science)}{May 2026}\\[2pt]
\row{B V Raju Institute of Technology}{Hyderabad, India}{Bachelor of Technology in Computer Science}{2024}

\section{Technical Skills}
\begin{itemize}[leftmargin=0em,label={},itemsep=1pt]
  \item \textbf{Languages:} TypeScript, JavaScript, Python, C\#, SQL
  \item \textbf{Agents and LLMs:} LangGraph, LangChain, Inngest agent-kit, tool calling, structured outputs, MCP, RAG, guardrails, DeepEval, Azure OpenAI, Gemini 2.0, OpenAI Realtime, gpt-4o-mini
  \item \textbf{Retrieval, tracing, sandboxes:} Azure AI Search, LangSmith, OpenTelemetry, E2B sandboxes, Browserbase, Stagehand
  \item \textbf{Interfaces:} React 19, Next.js 16, React Flow, Liveblocks, Tailwind CSS, shadcn/ui
  \item \textbf{Services and APIs:} Node.js, ASP.NET Core MVC, .NET 10, FastAPI, Pydantic, tRPC, REST, Zod, Clerk, Polar billing, better-auth
  \item \textbf{Data:} PostgreSQL, Drizzle ORM, Prisma, Neon serverless, MongoDB, Redis, ETL, ELT, PySpark, Databricks, Amazon RDS
  \item \textbf{Reliability and voice:} Trigger.dev durable tasks, Inngest retries, HMAC webhook verification, asyncio, Twilio WebSockets, Deepgram STT, Stream Video SDK, WebRTC
  \item \textbf{Infrastructure and shipping:} Docker, Nginx, Vercel, Render, AWS, Azure, GCP, CI, Vitest, Git, pull request review, branch workflow
\end{itemize}

\section{Projects}

\row{Websito $|$ Agentic Website-Generation SaaS}{}{Inngest agent-kit, Gemini 2.0, E2B, Prisma, Clerk}{\href{https://websito-eight.vercel.app/}{\underline{websito-eight.vercel.app}}}
\bstart
\bi{Prevented runaway agent runs from draining user credits, as measured by a hard cap of 20 loops, by adding explicit state transitions and \textbf{structured outputs} to the multi-step \textbf{agent workflow}.}
\bi{Eliminated broken previews, as measured by every generated site building in an \textbf{E2B} sandbox before the user sees it, by validating each tool-generated site pre-deploy.}
\bi{Cut site delivery from four to eight weeks of manual development to 30 to 90 seconds by moving generation onto \textbf{Inngest} background jobs with \textbf{Gemini 2.0}.}
\bi{Matched pricing to compute cost, as measured by 1 credit per generation against caps of 10 (free) and 100 (paid) a month, by building credit-based billing.}
\bi{Held \textbf{tRPC} responses under 100 ms under load by pooling database connections with \textbf{Prisma Accelerate}.}
\bend

\row{Brand Guardian $|$ Video Compliance Auditor}{}{LangGraph, LangChain, Azure OpenAI, Azure AI Search, FastAPI}{\href{https://github.com/HarshaVardhanRobba/Brand_guardian}{\underline{Source on GitHub}}}
\bstart
\bi{Replaced a reviewer watching a full video to catch one spoken claim with a 2-node \textbf{LangGraph} pipeline that audits each video automatically.}
\bi{Grounded every verdict in a retrieved policy rule, as measured by each finding tied to a passage from \textbf{Azure AI Search}, by indexing policy PDFs for \textbf{RAG}.}
\bi{Kept reviewer reports from breaking on free text, as measured by valid JSON with severity and status on every audit, by enforcing \textbf{structured outputs} from \textbf{Azure OpenAI}.}
\bi{Gave reviewers per-node visibility into tokens and latency by tracing every run through \textbf{LangSmith} and \textbf{OpenTelemetry}.}
\bend

\row{Pharmacy Voice Agent $|$ Phone Support Agent}{}{Twilio, Deepgram nova-3, OpenAI gpt-4o-mini, asyncio}{\href{https://github.com/HarshaVardhanRobba/Voice-Agent}{\underline{Source on GitHub}}}
\bstart
\bi{Cut response time from six seconds to 1.5 to 2.5 seconds per call by tuning audio frame size and barge-in handling.}
\bi{Prevented wrong orders, as measured by every function call validated before a write, across 3 \textbf{tool calls} for drug lookup, order placement, and order status.}
\bi{Kept callers on the line when a drug lookup fails by returning tool crashes as spoken responses instead of dropped calls.}
\bi{Held live-call latency by moving audio in both directions through \textbf{asyncio} queues, with 160-byte frames mapping one to one with 20 ms of 8 kHz mulaw audio.}
\bi{Made the slow step in any call visible, as measured by per-call latency and failure tracking, by instrumenting each stage of the call.}
\bi{Kept lookups from adding delay, as measured by O(1) in-memory reads over 15 drugs and every order.}
\bend

\row{Web-base $|$ Browser Workflow Platform}{}{Next.js 16, React Flow, Trigger.dev, Browserbase, Clerk}{\href{https://web-base-workflow.vercel.app/}{\underline{web-base-workflow.vercel.app}}}
\bstart
\bi{Cut flow-building time from two hours of manual \textbf{Playwright} scripting to minutes by building a node-based \textbf{React Flow} canvas that ops teams use without a developer.}
\bi{Kept runs alive through browser steps that wait minutes, and halted each run at the first failed step, by executing every node as a durable \textbf{Trigger.dev} task.}
\bi{Gave users a live view of each run by integrating \textbf{Browserbase} with \textbf{Stagehand} and streaming the browser session back.}
\bi{Prevented cross-tenant reads in a shared database, as measured by every query filtered on organization ID, by scoping all reads under \textbf{Clerk} tenancy.}
\bi{Blocked malformed graphs before a paid run starts, as measured by 3 \textbf{Vitest} files covering graph and registry parity, by validating each workflow graph.}
\bi{Replaced status polling with a token scoped to one run that streams updates through useRealtimeRun, cutting wasted requests.}
\bi{Ended overwrites when two people edit one flow, as measured by a shared canvas, by syncing it through a \textbf{Liveblocks} room.}
\bend

\row{Elara $|$ Real-Time AI Meeting Agent}{}{Stream Video, OpenAI Realtime, Inngest, Drizzle ORM, Neon}{\href{https://elaravoiceai.onrender.com}{\underline{elaravoiceai.onrender.com}}}
\bstart
\bi{Replaced manual meeting minutes with a summary delivered within 12 seconds of hangup by processing calls with \textbf{OpenAI Realtime} and background jobs.}
\bi{Stopped transcript loss at the request timeout, as measured by summaries completing in 5 to 12 seconds, by moving summarization to \textbf{Inngest} background jobs with retries.}
\bi{Closed a gap where one org could see another's meetings, as measured by every row scoped to its owner, by redesigning the \textbf{PostgreSQL} schema with \textbf{Drizzle ORM}.}
\bi{Blocked spoofed webhook writes by gating every write behind \textbf{HMAC} signature verification.}
\bi{Resolved races among 6 webhook events by driving each event through a single explicit state change.}
\bi{Enabled paid plans by integrating \textbf{Polar} billing through better-auth.}
\bi{Answered post-call questions from the saved summary by adding a chat channel to each meeting.}
\bi{Held one-way voice latency near 500 ms on the \textbf{OpenAI Realtime} path.}
\bend

\row{Bizpulse $|$ Inventory, Invoicing, and Payroll}{}{Next.js 16, PostgreSQL, Drizzle ORM, Zod}{\href{https://github.com/HarshaVardhanRobba/Bizpulse}{\underline{Source on GitHub}}}
\bstart
\bi{Replaced 3 disconnected shop tools with one data model, as measured by 7 tables across 3 domains shipped in 27 commits.}
\bi{Eliminated oversold stock by committing each invoice and its stock deduction in a single \textbf{PostgreSQL} transaction, with an immutable StockLevel that refuses deductions below zero.}
\bi{Kept past paystubs exact when tax rules change by versioning tax brackets so every paystub is pinned to the rule that priced it.}
\bi{Made API failures consistent, as measured by 3 typed AppError subclasses mapping to one HTTP status each, by centralizing error handling.}
\bend

\row{TeamOmnifield $|$ Restaurant Ordering Platform (2-Person Team)}{}{ASP.NET Core MVC, .NET 10, PostgreSQL, Docker, Nginx}{}
\bstart
\bi{Gave a teammate a place to start, as measured by 3 working portals shipped as the base for the remaining work, by building them in \textbf{ASP.NET Core MVC} on \textbf{.NET 10}.}
\bi{Replaced hand-taken phone orders with a storefront and an admin console, as measured by owners no longer taking orders by hand, on \textbf{PostgreSQL}.}
\bi{Carried 85\% of lines across 6 of 18 merged \textbf{pull requests}, with every change reviewed before merge.}
\bi{Settled client and admin disputes over tickets with one ticket path, shipped across 3 pull requests.}
\bend

\section{Experience}
\row{Club InQuizitive}{Hyderabad, India}{Lead Full Stack Developer}{Jul 2023 -- Dec 2023}
\bstart
\bi{Delivered the club's main website and event platforms over a full semester, as measured by 1000+ users, by leading developers and setting each member's scope.}
\bi{Replaced paper sign-up with live event registration, as measured by 500+, by pairing \textbf{Firebase} with \textbf{PostgreSQL}.}
\bend
\row{JavaTpoint}{Remote}{Technical Writer}{Sep 2022 -- Feb 2023}
\bstart
\bi{Ensured tutorial accuracy, as measured by every \textbf{Python} and \textbf{SQL} sample run before publication across 300+, by writing and testing runnable code.}
\bend

\end{document}
```

## Step 8 — Log to the tracker (always; path from the Standing profile)
**Update the ORIGINAL tracker file** at the Standing profile path; do not leave a trail of `_v2`, `_v3` copies. Work from a fresh stage of that file, save the edited copy in the outputs folder, then commit it over the original path with `force: true` if Excel's mtime changed. After EVERY commit, re-stage the original and count rows and statuses; if the staged copy still shows the old content or the byte size is unchanged, wait a few seconds and re-stage once more. Only if the commit is rejected or the verified content is wrong (for example the file is locked open in Excel) fall back to a new filename (`..._vN.xlsx`), tell the user why, and ask them to close Excel so the original can be updated next time. Log Not applied right after the resumes are built, and update statuses right after each verified submit batch.
Columns: Date Found | Date Applied | Company | Title | Location | Salary | Fit | Status | Resume Used | Job Link (match the file's own header if it differs). ALWAYS re-stage the tracker from the device immediately before editing (never reuse an older copy), load with openpyxl, dedupe by Job Link and Company+Title, append rows (Date Found = today, Status "Not applied", Job Link as an "Apply" hyperlink), copy each new row's cell styles from the row above, preserve formatting and the Status dropdown, and save. **Verify the write:** re-stage the file again after the commit and confirm the row count and the new rows are present; if not, redo it. Never save back a copy loaded from a stale stage; that silently drops rows.

## Step 9 — Apply directly (automatic, right after the resumes are built)
Do not hand off prompts. Apply yourself through Claude in Chrome, in the user's real logged-in browser. Load the Chrome tools in one ToolSearch call (tabs_context_mcp, navigate, computer, find, read_page, file_upload, browser_batch, get_page_text, tabs_create_mcp, tabs_close_mcp, javascript_tool). Use a new tab.

**Speed method (tested):** per posting use about six calls. `browser_batch` actions take the form `{"name": "navigate", "input": {...}}` (arguments go inside `input`). Call A (`browser_batch`): `navigate` to the wizard (pass `force: true` so a leftover "Leave site?" dialog from an unsubmitted page is discarded), `find` "File options button, or Inactive/already applied message", click it, `find` "Replace menu item". If it is the already-applied heading, record it and move on. Call B: click the Replace ref you just found (it is `ref_154` or `ref_153` depending on the page, so NEVER click a remembered ref blind; use the one the last `find` returned), then `find` "resume file input type=file (first)". Call C: `file_upload` the PDF to that ref (separate call, it is not a batch action), then `find` "button labeled exactly Next". Call D (`browser_batch`): click Next, wait 2 seconds, `get_page_text` (the review step must show the intended resume file name), `find` "button labeled exactly Submit". Call E: click Submit, wait 4 seconds, `tabs_context_mcp` (URL must be `/wizard/success`); the same batch can already navigate to the next posting and run Call A for it. Element refs change from page to page; blind clicks on guessed refs once clicked the wrong element. For radio buttons click the LABEL refs (find "visible label elements"), because clicks on the radio input refs do not register. Do not use `javascript_tool` to set form values; the browser safety check blocks it (reading links on a list page is fine).

**Learned notes (2026-10-13):** (1) If the review step shows "Resume * <file name>", "Work Authorization: Employment Auth Document" and the location, the saved answers prefilled and no question step is needed. (2) `file_upload` only accepts session-readable paths: use `/home/claude/work/<folder>/` or the scratchpad; `/mnt/user-data/outputs/` subfolders were rejected. (3) Screenshots can time out and freeze a tab. If a tab stops responding, open a new tab with `tabs_create_mcp` and continue there; use `find`, `read_page` and `get_page_text` only. A frozen tab may refuse `tabs_close_mcp`; tell the user to close it. (4) Dice "Replace" overwrites the profile resume each time. (5) After the batch, `https://www.dice.com/my-jobs?type=applied` is the final proof; reconcile against it. (6) Merely opening a wizard page for a posting you then drop (for example a citizenship-bound one) does not apply; discard it with `force: true`.

**Parallel tabs (fill tested in 2 tabs up to the review step; same session, no new session needed):** open one tab per posting with `tabs_create_mcp`, put each tab's `tabId` on every call, and run the same steps interleaved in single `browser_batch` calls. Refs are per tab. Use at most 3 tabs, and open only as many tabs as will be submitted. Fill all tabs in parallel, then **submit ONE TAB AT A TIME, never in parallel**: before each Submit, confirm that tab's own review step shows the intended resume file name; after Submit, confirm `/wizard/success`, then go on to the next tab. A single tab worked through postings one after another was reliable and is the default. If a tab has a problem before Submit, fix it and submit it first, then continue with the next tab. Do not abandon an UNSUBMITTED tab: its "Leave site?" dialog can make `tabs_close_mcp` time out, so finish and submit it, or ask the user to close it.

**Browser method: read the page structure, do not look at pictures.** The agent does not need to "see" a page. A screenshot is a picture; the page also has a text structure, and that structure is more reliable here (screenshots time out repeatedly in this environment). Prefer these tools for every step:
- `find` and `read_page` return buttons and inputs by name and ref, for example "button labeled exactly Submit" or "button labeled exactly Next". Click by ref, never by pixel coordinates.
- To go to the next step of a wizard, `find` "button labeled exactly Next" and click that ref. To finish, `find` "button labeled exactly Submit". Use the exact phrase each time, because a loose query such as "Submit" can return Next.
- `file_upload` attaches the PDF straight to the hidden file input by path. No file-picker window is needed, so no sight is needed.
- `get_page_text` reads the review step text. The resume file name shown there is the proof the right PDF is attached before Submit.
- URL check: `/wizard/success` means submitted. The Applied list is the second proof.
Screenshots are a fallback only: take one only when `find`, `read_page` and `get_page_text` are ambiguous or fail, and then at reduced scale or zoomed on one region. Never make a screenshot the only proof of anything.

1. **Dice:** navigate to `https://www.dice.com/home-feed`. If the page shows a login wall, STOP and tell the user to sign in; never enter a password and never create an account. **Indeed:** navigate to `https://www.indeed.com/`; same rule. If a board has no postings in this run, skip it and proceed with the other board only.
2. **Dice procedure (proven):** for each posting open `https://www.dice.com/job-applications/<guid>/wizard` (guid from the job URL). If the page says Inactive, or redirects to `/wizard/applied`, record it (Closed or Already applied) and move on. Otherwise follow the Speed method above. Some postings insert an "Application Questions" step: answer from the Standing profile and the screening-info screenshot, then continue with "button labeled exactly Next"; if a required question has no truthful stored answer, do NOT submit; leave it, move on, and report it.
3. **Indeed procedure:** open the posting (the `viewjob` URL from Step 1a), use Apply / Easy Apply, attach the matching PDF, answer questions from the Standing profile only, and move between steps with "button labeled exactly Next" (or Continue if that is the button's exact name). If it redirects to an employer site requiring an account, password or CAPTCHA, skip it and report.
4. Submit only the postings from this run, each with its own tailored resume. Never complete CAPTCHAs, never enter passwords or payment or government IDs.
5. **Verify every submission:** after Submit, the URL must be `/wizard/success`, and at the end the posting must appear in the Dice Applied list as "Applied today". Only then count it as applied. For Indeed, the confirmation page after Submit is the proof; no Indeed Applied-list check is defined yet, so say so in the Close.
6. Dice replaces the profile resume each time; mention that at the end.

## Step 10 — Final proof check (required)
Before the final message, reconcile: found N = built N resumes = applied + closed + already applied + held. Print that equation. Re-stage the tracker, set Status to Applied and Date Applied for each verified submission (Closed, Already applied, or Held with the reason otherwise), commit, then re-stage and confirm the counts match what the browser verified. Tell the user the two or three they should spot-check themselves (open Dice, Applied jobs).

## Close
Deliver in this order: (1) the per-board ranked lists from Step 2 with linked job titles and each posting's PDF named, plus the ZIPs as files; (2) the apply results: applied (verified), closed, already applied, held with the question that blocked it, which postings came from the recommended-jobs fallback, which came from the Indeed site search versus the Indeed connector, and which were Tier 2; (3) the reconciliation line from Step 10; (4) every honest gap (years, seniority, missing stack); (5) every minor default decision made mid-run, including which section order each resume got (Projects first or Experience first) and why, plus a one-line record of each scope change the user picked. State plainly that every resume uses the user's LaTeX template layout unchanged, all projects are in every resume, no metrics were invented and no placeholders remain, and offer to add real numbers if the user supplies them or authorizes counting from their repos.

## Recap
Stage base resume and tracker from the Standing profile paths and list every project and job (the Reference resume template is the layout and content source of truth) → ask only batch size, recency, location, titles → search Dice and Indeed with as many title variants as allowed, paging deeper on every query; for Indeed run the connector one search at a time (retry on rate limit) AND the Chrome site search with `fromage` and `sort=date` (Step 1a), and never report "Indeed 0" from the connector alone → sync the tracker with Dice's Applied list and check each candidate's wizard page for already-applied → apply Tier 1 gates BEFORE ranking → if under N, run the recommended-jobs fallback, then Tier 2 (reject only clear citizenship), then the shortfall checkpoint → rank per board in the fixed format → set up template.tex, build_tex.py, build.sh, gen.py and check.py and build each tailored resume (ALL projects and jobs present, real facts only, no placeholders, only real or verifiable numbers, **bold** keywords, write-without-ai-tells, the unchanged LaTeX template layout with embedded links and the unlabelled burgundy role line under the contact line, for example `AI Engineer | LLM Applications, RAG, Agent Systems`; Experience goes above Projects when the posting is mostly about non-project work such as technical writing) → run the resume check, zip per board → re-stage the tracker, add rows and update the ORIGINAL tracker file, verify the write by re-staging → apply on Dice with find first and the ref each find returned, one tab at a time, each verified (review-step file name, /wizard/success, Applied list) → answer screening questions from the Standing profile and the screening-info screenshot only → reconcile counts, update and re-verify the tracker → Close.