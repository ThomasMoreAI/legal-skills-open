---
name: cold-start-interview-uk-agents
title: /legal-clinic-uk:cold-start-interview
description: Supervisor's one-time UK clinic setup — practice areas, jurisdiction (England & Wales / Scotland / Northern Ireland), supervision style (formal review queue / configurable flags / lighter-touch), SRA/BSB authorisation confirmation, and handbook/rules upload. Writes CLAUDE.md so every other skill and every student who runs /legal-clinic-uk:ramp reads from the same clinic context. Use on fresh install, when CLAUDE.md has placeholders, when re-doing setup with --redo, or when re-checking integrations with --check-integrations.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /legal-clinic-uk:cold-start-interview

1. Check `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`. If populated and no `--redo`, confirm before overwriting.
2. Run the supervisor interview below, starting with Part 0 (supervising solicitor/barrister role check → ethical preconditions → SRA/BSB authorisation → integration availability). If the user isn't the supervising solicitor or barrister, stop and redirect.
3. Seed docs: clinic handbook, filing guides, court/tribunal rules, intake form(s), one scrubbed example file.
4. Key decision: supervision style (formal queue / flags / lighter-touch).
5. Migration: if a populated CLAUDE.md (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/uk-legal-plugins/legal-clinic-uk/*/CLAUDE.md` but not at the config path, copy it to the config path and show the user what was migrated.
6. Write `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` including `## Who's using this` and `## Available integrations`. Show supervision choice and practice-area templates for confirmation.
7. Offer `/legal-clinic-uk:ramp` preview.

```
/legal-clinic-uk:cold-start-interview
```

**`--check-integrations`:** Re-run only the Part 0 integration-availability check (case management, document storage). Updates `## Available integrations` in `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` without touching the role, ethical preconditions, supervision style, or practice-area templates. Use after adding or removing an MCP connector.

When probing: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to for confirming. Never report ✓ based on `.mcp.json` declarations alone.

---

# Cold-Start Interview: UK Law School Clinic

## Purpose

UK law school clinics are structurally capacity-constrained. A supervising solicitor or barrister manages five to ten students, each carrying a handful of cases while juggling lectures, and the whole workforce turns over every term. The waitlist grows. People give up waiting.

This plugin's job is to cut the time cost of everything *around* the lawyering — intake write-up, first drafts, research starting points, status updates — so the same students and supervisor serve more clients, and students spend more time on the analysis and strategy that make clinical legal education worthwhile.

This interview sets up the clinic context once, so every student who onboards via `/legal-clinic-uk:ramp` and every skill that runs afterward is working from the same understanding of how *this* clinic operates, which jurisdiction it serves, and which SRA or BSB supervision framework applies.

**Audience: the supervising solicitor or barrister.** Students don't run this — they run `/legal-clinic-uk:ramp`.

## Cold-start check

Read `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the user and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

## Check for the shared company profile

Look for `~/.claude/plugins/config/uk-legal-plugins/company-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation: "You're [name], [practice setting], at [school/law centre], operating in [jurisdictions]. Right? (Or say 'update' to change the shared profile.)" If confirmed, skip the company questions — go straight to the plugin-specific ones.
- **If it doesn't exist:** You'll be the first plugin this user set up. After the orientation and fork, ask the company questions and write them to the shared profile, then continue with the plugin-specific questions. Tell the user: "I've saved your company profile — the other legal plugins will read it and skip these questions."

## Install scope check

Before the orientation, if you notice the working directory is inside a project (not the user's home directory), flag it once:

> **Heads up — it looks like this plugin may be project-scoped, which means I can only read files in [current directory]. If you'll want me to read documents from elsewhere (Downloads, Documents, Dropbox), install user-scoped instead. You can continue with project scope, but you'll need to move files into this folder.**

Ask the user to confirm before proceeding.

## Before the interview starts

Show this preamble first (3-4 short lines, nothing more):

> **`legal-clinic-uk` is for supervising solicitors and barristers setting up a UK law school clinic and onboarding students.** Not your area? Look for the right plugin.
>
> **2 minutes** gets you practice area(s), jurisdiction (England & Wales / Scotland / Northern Ireland), and supervision model basics — plus working defaults for client-letter format, IRAC scaffolding, and deadline cadence. **15 minutes** adds your SRA/BSB authorisation record, supervision flag triggers, per-practice-area document templates, handbook content feeding `/legal-clinic-uk:ramp`, court/tribunal rules feeding `/legal-clinic-uk:draft`, and term dates.
>
> Quick or full? (Upgrade any time with `/legal-clinic-uk:cold-start-interview --full`.)

## After the user picks quick or full

Once the supervisor has picked, orient them. Cover, in your own voice:

- **What this plugin maintains:** your clinic profile (practice areas, supervision model, house templates), per-case files (intake, deadlines, comms log, handoff memos), and a supervisor review queue.
- **What this setup does:** supports a UK law school legal clinic — intake, case memos, client letters, status updates, deadlines — across your practice areas, with supervision built in. Writes everything into a plain-text file every skill reads from.
- **Data sources:** setup builds a fresh clinic profile from the supervisor's answers and from documents uploaded during the interview. It does not read personal Claude history or other conversations.
- **Next up:** Part 0 — who's running the setup and the ethical preconditions.

**Why this matters.** Every `/legal-clinic-uk:ramp` onboarding, every `/legal-clinic-uk:client-intake`, every `/legal-clinic-uk:draft`, every `/legal-clinic-uk:client-letter`, every `/legal-clinic-uk:status` reads from the configuration this interview writes. A generic configuration gives students generic output. Telling the plugin the practice areas, supervision style, jurisdiction, and local formatting is what makes the difference between "a clinic AI tool" and "a tool that runs the way the clinic runs."

### Quick start or full setup — branching

**Quick start path:** ask only the basics (practice area, jurisdiction, supervision style). Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for client-letter format, IRAC scaffolding, and deadline cadence. Run `/legal-clinic-uk:cold-start-interview --full` anytime to do the whole interview."

**Full setup path:** the existing interview flow below.

## Interview pacing

- **Assume the answer exists somewhere.** When a question asks for information that's probably written down somewhere — clinic handbook, jurisdiction list, supervision matrix — prompt for a link or a paste before asking the user to type it from memory.

- **Pause for real answers.** Part 0 has tap-through role and integration checks. The ethical preconditions, Parts 1–5, and especially Part 4 (seed documents) need the supervisor to type out answers or upload files.

- **Before writing the practice profile:** review the interview. List every question that was skipped or answered with a placeholder. Say: "Before I write your practice profile, here's what's still open: [list]. Want to fill any of these now, or leave them as placeholders?" Then wait.

- **Pause and resume.** Tell the supervisor up front: "If you need to stop, say 'pause' and I'll save your progress. Run `/legal-clinic-uk:cold-start-interview` again later and I'll pick up where you left off." When the supervisor pauses, write a partial configuration with a `<!-- SETUP PAUSED AT: [section name] -->` comment and `[PENDING]` markers on unanswered fields.

- **Verify user-stated legal facts as they come up.** When the user answers with a specific rule citation, statute number, limitation period, or jurisdiction — and it's something you can sanity-check — do the check. A wrong fact written into CLAUDE.md propagates into every future output.

## The interview

### Part 0: Who's running this setup, ethical preconditions, and what's connected

#### Who's running this setup?

> Are you the supervising solicitor or barrister for this clinic? You need to hold a valid practising certificate (solicitor) or be authorised by the BSB (barrister) and be supervising students under your institution's supervised-practice framework for this setup to be valid.
>
> 1. **Yes, I'm the supervising solicitor or barrister.** Continue.
> 2. **No, I'm a student / staff / administrator.** Stop. This setup writes the clinic's governing context — supervision model, client-data rules, ethical preconditions — and must be done by the supervising solicitor or barrister. Ask them to run `/legal-clinic-uk:cold-start-interview`. Students run `/legal-clinic-uk:ramp` to onboard each term.

If the answer is 2, stop the interview. Do not proceed.

If the answer is 1, record it under `## Who's using this` (Role: Supervising solicitor / barrister; name, authorisation number, practising certificate status) and continue.

*Why this matters:* The clinic runs on a supervised-practice framework that requires supervision by a solicitor or barrister with a valid practising certificate. Cold-start decisions — supervision model, consequential-action gating, ethics preconditions — are the supervising solicitor's or barrister's call. The role question gates those decisions to the right person.

#### Ethical & confidentiality preconditions

Before the supervisor interview starts — and before any student uses this plugin on a real client matter — confirm the following:

1. **Account tier and data-handling terms.** Your Claude account tier and its data retention and training policies. Confirm which tier the clinic is on and what the applicable terms say about client data. Document the answer in the plugin config.

2. **Client consent and disclosure practices for AI-assisted work.** Review the SRA Code of Conduct 2019 (Principle 7 — acting in clients' best interests; Principle 6 — behaving in a way that maintains trust in the profession; SRA Standards and Regulations on competence), BSB Handbook (gC18, gC19 on supervision of work done by others), and your school's professional responsibility guidance. Decide whether and how the clinic discloses AI use to clients, and document the practice.

3. **How privileged and confidential material is handled.** What gets pasted into sessions, where outputs are stored, who has access, how long material is retained locally, how student turnover affects access. Students are not solicitors or barristers — they must understand that privilege belongs to the client and cannot give formal legal advice without supervision.

4. **Practice-area heightened-confidentiality considerations.** Immigration / asylum, criminal defence, domestic violence, some family and civil rights matters carry heightened confidentiality and security expectations. Confirm whether any clinic practice area requires additional safeguards — and decide whether the plugin is appropriate for those case types at all.

5. **SRA Minimum Terms and Conditions.** If the clinic is authorised by the SRA, confirm that the clinic's professional indemnity insurance covers AI-assisted work product produced under supervision. The SRA Warning Notice on third-party managed accounts may be relevant if the clinic handles client money.

Capture the supervisor's answers. If any precondition is unresolved, flag that in the plugin config and note that students should not use the plugin on real client matters until resolved.

#### What's connected?

> This plugin can work with a case management system (Clio, LEAP, Osprey) and document storage (Google Drive, SharePoint, Box). Let me check which connectors are configured.

Check what's actually connected, not just configured. Report only ✓ on a successful tool call response:

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified. Open your MCP settings to confirm.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.]

Write Part 0 answers to the plugin config under `## Who's using this` and `## Available integrations`.

### Opening

> This is the one-time setup for your UK law school clinic. Ten to fifteen minutes. I'll ask about your practice areas, your jurisdiction, how you supervise, and then I'll ask you to point me at your clinic handbook and any filing guides or tribunal/court rules you give students. Everything I learn here feeds the `/legal-clinic-uk:ramp` onboarding your students will run at the start of each term, and every other command in this plugin.
>
> None of this replaces your judgment or your students' analysis. The goal is to cut the hours spent on formatting, structuring, and writing up — so more of your students' time goes to the lawyering, and more clients get served.
>
> I'll ask for materials along the way — handbook, filing guides, tribunal/court rules, intake forms, example case files, sample skeleton arguments, sample client care letters. Ten to twenty documents across the interview is the target. More is better. If you share fewer than ten, I'll flag the practice profile as LIMITED DATA — the plugin still works, but `/legal-clinic-uk:ramp` is thinner, `/legal-clinic-uk:draft` falls back to generic procedure defaults instead of your local formatting, and `/legal-clinic-uk:client-letter` uses generic templates instead of matching your voice.

### Part 1: The clinic (2-3 min)

**What kind of clinic?** (Practice area feeds `/legal-clinic-uk:client-intake` and `/legal-clinic-uk:draft` — each area has its own intake template and document templates.)
- Clinic name and school
- Practice area(s): housing, immigration/asylum, family law, employment, consumer, criminal defence, civil rights, benefits, debt, other? (Can be multiple)

   **Practices that don't fit the boxes.** If the clinic's practice doesn't match the options (appellate-only, public law, environmental law, social welfare, mediation, transactional/charity law), offer: "Tell me about it in your own words — what the clinic does, who it serves, what jurisdictions and forums, what the work looks like — and I'll build your clinic profile from that instead of forcing it into boxes that don't fit."

- How many students this term? How many active cases at a time, roughly?
- How many supervising solicitors / barristers?

**Who are the clients?**
- Typical client situations — who walks in, what are they facing?
- Languages spoken beyond English? Welsh? Other languages?
- Common referral sources (Citizens Advice, law centres, HMCTS self-help centres, community organisations, housing charities)?

### Part 2: Jurisdiction (1-2 min)

(This feeds `/legal-clinic-uk:draft`, `/legal-clinic-uk:research-start`, `/legal-clinic-uk:memo`, and `/legal-clinic-uk:deadlines` — jurisdiction determines procedure, limitation periods, and court/tribunal formats.)

- **Primary jurisdiction:** England & Wales, Scotland, or Northern Ireland? Or does the clinic cover multiple?
  - *England & Wales:* SRA / BSB jurisdiction; CPR 1998; County Court / High Court / Employment Tribunal / First-tier Tribunal; Limitation Act 1980.
  - *Scotland:* Law Society of Scotland / Faculty of Advocates; Sheriff Court / Court of Session; Prescription and Limitation (Scotland) Act 1973; Scottish Civil Justice Council Rules.
  - *Northern Ireland:* Law Society of NI / Bar of NI; County Court NI; Limitation (NI) Order 1989.
- Primary court(s) / tribunal(s): which courts or tribunals do cases land in most often? County Court, Magistrates', Employment Tribunal, First-tier Tribunal (Immigration and Asylum)?
- Any practice directions, standing orders, or tribunal practice guidance that diverge from defaults?

### Part 3: Supervision style (2-3 min — this is the key design question)

> UK law school clinics vary a lot in how tightly student work is reviewed before it goes out. Some want every draft in a formal review queue — student submits, supervisor approves, then it goes. Others are lighter-touch — students check in, supervisor signs off informally. What's your model? (This feeds `/legal-clinic-uk:supervisor-review-queue` and the flag-triggering logic across `/legal-clinic-uk:draft`, `/legal-clinic-uk:client-letter`, and `/legal-clinic-uk:status`.)
>
> Note: under the SRA Code of Conduct 2019 and BSB Handbook, you as the supervising solicitor or barrister remain responsible for the student work product. Any model you choose should be consistent with your SRA/BSB supervision obligations. `[SRA-CODE]` `[BSB-HANDBOOK]`

Three options:

**Formal review queue:** Student output that's client-facing or tribunal/court-bound goes into a queue. Supervisor reviews, approves or edits, then it releases. Every approval logged. (`supervisor-review-queue` turns on.)

**Configurable flags, informal review:** Certain triggers (deadlines, sensitive topics, tribunal filings, immigration status) flag the output with "CHECK WITH [SUPERVISOR] BEFORE SENDING" — but no formal queue. Student is responsible for checking in.

**Lighter-touch:** Outputs carry the standard AI-assisted label and verification prompts, but no additional review gates. Supervisor supervises through the clinic's existing structure (case rounds, one-on-ones).

> There's no right answer — it depends on your students' experience level, your caseload, and how you already run supervision. You can change this later by editing CLAUDE.md.

Capture the choice and, if formal queue or configurable flags: what should trigger a flag? (Tribunal filings always? Any deadline mention — especially ET 3-month rule? Topics like DV, immigration status, criminal exposure, benefits entitlement disputes?)

**Pedagogy dial.** After the supervision choice is captured, ask:

> **How much should the skills do?** Three options:
>
> - **Guide (default):** The skill produces structure; students fill in substance; the skill gives feedback. Balanced — most clinics start here.
> - **Assist:** The skill produces work product; students review, edit, and learn by seeing. Fastest. Good for high-volume clinics.
> - **Teach:** The skill doesn't produce work product — students draft, the skill asks Socratic questions and gives feedback, only shows a model after two attempts. Most pedagogical.
>
> You can set this per document type later with `/legal-clinic-uk:build-guide`. For now, pick a default.

Write the answer to the practice profile as `pedagogy_default: assist | guide | teach` (default `guide` if the supervisor doesn't pick).

### Part 4: Seed documents (3-4 min)

> Three things, as many as you have.
>
> 1. **Your clinic handbook or procedures doc.** Whatever you give students on day one. I'll use it to build the `/legal-clinic-uk:ramp` onboarding.
>
> 2. **Filing guides, tribunal practice directions, and local court rules.** Anything that tells students how to format a claim form or an ET1, where to file, what the tribunal expects. These feed `/legal-clinic-uk:draft`.
>
> 3. **Your intake form, and if you have one, a scrubbed example case file.** The intake form becomes the backbone of `/legal-clinic-uk:client-intake`.

**From the handbook:** Clinic procedures, case management conventions, student expectations, SRA/BSB-related ethical reminders, client care obligations.

**From filing guides/tribunal rules:** CPR form requirements, ET1 / ET3 formats, First-tier Tribunal procedures, Housing Possession Court guidance, service requirements. This is what `/legal-clinic-uk:draft` will apply.

**From the intake form:** Practice-area-specific fields. If the clinic has separate intake forms per practice area, take all of them.

### Part 5: Practice-area templates (1-2 min)

For each practice area the clinic handles: what are the 3-5 documents students draft most often?

| Practice area | Common documents |
|---|---|
| Housing | Possession defence, disrepair letter, deposit dispute letter, housing benefit appeal |
| Immigration / Asylum | Asylum statement of evidence, representations to the Home Office, appeal skeleton argument, FOIA to Home Office |
| Employment | ET1 claim narrative, grievance letter, appeal against dismissal, subject access request |
| Family | Non-molestation order application, occupation order application, child arrangements statement |
| Consumer / Debt | Debt validation letter, FCA complaint, response to statutory demand |
| Benefits | Mandatory reconsideration request, First-tier Tribunal appeal, DWP correspondence |

These become the template set for `/legal-clinic-uk:draft`. If the supervisor has existing templates, ingest them. If not, note which ones to build.

**If the supervisor didn't upload a handbook or intake form:** offer: "Want me to draft a starter clinic handbook and intake form from what you told me?"

## Before writing — re-read

Before committing the practice profile to the plugin config, re-read every captured answer in order. Catch:
1. **Contradictions** — e.g., "formal review queue" in supervision but "lighter-touch" in describing practice.
2. **Drifted specifics** — confirm jurisdiction, practising certificate details, court/tribunal references.
3. **Skipped gaps worth naming** — practice areas without templates, handbook promised but not uploaded.

## Writing the practice profile

Per the CLAUDE.md template. Key sections:

- **Clinic profile** — name, school, practice areas, jurisdiction (E&W / Scotland / NI), student count
- **Supervision style** — which of the three models, and flag triggers if applicable; confirm SRA/BSB compliance
- **Practice-area templates** — intake templates and document templates per area
- **Jurisdiction** — jurisdiction(s), primary courts/tribunals, court rules ingested
- **Semester/Term** — when do students turn over (so `/legal-clinic-uk:ramp` knows when it'll be needed, and `/legal-clinic-uk:semester-handoff` knows when it'll be triggered)
- **Handbook path** — where the ingested handbook lives, for `/legal-clinic-uk:ramp` to read

**LIMITED DATA flag:** if fewer than 10 materials were shared, add a `> LIMITED DATA` note at the top of CLAUDE.md.

## Built-in safeguard framing

Write into the plugin config the safeguard standards every skill will apply:

```markdown
## Output safeguards (applied by every skill)

Every output includes:
- **AI-assisted label:** "[AI-ASSISTED DRAFT — requires student analysis and supervising solicitor/barrister review]"
- **Confidence indicators:** Where the skill is uncertain, it says so explicitly
- **Verification prompts:** Specific things the student should fact-check before relying on the output
- **Ethical reminders calibrated to task:** SRA Code of Conduct 2019 and BSB Handbook supervision requirements apply. Students are not solicitors or barristers and cannot give formal legal advice without supervision.

These are not optional and not configurable. They're the baseline.
```

## After writing

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list:

> **Here's what I'm good at in UK law school clinic practice:**
>
> - **Student intake on a new case** — structured intake with red-flag spotting and conflict checks. Try: `/legal-clinic-uk:client-intake`
> - **Draft a client care letter at plain-English level** — produces an appointment confirm or status update; student edits and supervisor approves. Try: `/legal-clinic-uk:client-letter`
> - **Build an IRAC memo scaffold with OSCOLA citation starts** — gives a student the structure and research-gap list for a case memo. Try: `/legal-clinic-uk:memo`
> - **Track deadlines across the active caseload** — see what's due in the next 14 / 7 / 3 / 1 days. Note: Employment Tribunal 3-month rule has plausibility checks built in. Try: `/legal-clinic-uk:deadlines`
> - **Ramp up a new cohort** — onboard this term's students to the clinic's procedures, tools, and case-handling norms. Try: `/legal-clinic-uk:ramp`
> - **Term handoff** — build per-case transition memos for the incoming cohort. Try: `/legal-clinic-uk:semester-handoff`
>
> **My suggestion for your first one:** Run `/legal-clinic-uk:ramp` yourself first so you see what your students will see at the start of term.

1. **Show the supervision style choice.** "You picked [formal queue / flags / lighter-touch]. That means [what it means in practice]. Consistent with your SRA/BSB obligations?"

2. **Show the practice-area templates table.** "These are the documents `/legal-clinic-uk:draft` will know how to start. Missing anything?"

3. **Offer a `/legal-clinic-uk:ramp` preview.** "Want to see what a student's onboarding will look like?"

4. **Note what wasn't provided.** If no handbook: "`/legal-clinic-uk:ramp` will be thin until you upload a handbook." If no tribunal/court rules: "`/legal-clinic-uk:draft` will use generic CPR/ET defaults — upload rules when you have them."

5. **Before your first case review, connect a research tool.** "Before your first case review or memo: confirm the uk-legal and govuk MCPs are connected. Without them, I'll flag every citation as unverified."

6. **Close with the "you can change anything later" note:**

> Done. Your clinic's configuration is at `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` — a plain text file you can read and edit directly.
>
> - Edit the file directly for a quick change
> - Run `/legal-clinic-uk:cold-start-interview --redo` for a full re-interview
> - Run `/legal-clinic-uk:cold-start-interview --check-integrations` to re-check what's connected
>
> The things clinics most commonly tweak later: practice areas (when the clinic takes on a new one), supervision style, and jurisdiction / local court and tribunal rules.

## Your practice profile learns

> **Your practice profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
> - You can always say "update my playbook to prefer X" or "change my escalation threshold to Y" and the relevant skill will write the change.
> - Run `/legal-clinic-uk:cold-start-interview --redo <section>` to re-interview one part, or edit the config file directly.

## What this does NOT do

- **Make supervision decisions.** The supervision style is the solicitor's/barrister's call; this interview just asks and records. Your SRA/BSB obligations on supervision remain yours regardless of what model you choose.
- **Replace the clinic's existing case management.** If the clinic uses Clio, LEAP, or Osprey, this plugin works alongside it.
- **Onboard students.** That's `/legal-clinic-uk:ramp`. This is the supervisor's one-time setup.
