---
name: cold-start-interview-law-student-uk-uk-agents
title: /law-student-uk:cold-start-interview
description: About-you interview and materials intake — modules, qualification route (LLB/GDL/SQE/BPTC/CILEx/DPLP), learning style (drill-me vs explain-to-me), past outlines, graded essays, old exams, SQE1 practice sets, module guides, papers. Use on a fresh install, when the user says "set up" or "get started", or with --check-integrations to re-probe connectors.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/law-student-uk/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /law-student-uk:cold-start-interview

1. Check `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md`. If already populated and no `--redo`, confirm before overwriting. If a populated config (no `[PLACEHOLDER]` markers) exists at `~/.claude/plugins/cache/uk-legal-plugins/law-student-uk/*/CLAUDE.md` but not at the config path, copy it to the config path and tell the user what was migrated.
2. Apply the interview workflow below.
3. Walk Part 0 (who's using / what's connected — student vs. grad vs. other; document storage availability), Part 1 (where you are), Part 2 (how you learn — drill-me vs explain-to-me), Part 3 (strong/shaky/avoid), Part 4 (materials intake — target 10-20 items).
4. Re-read captured answers. Catch contradictions, drifted specifics, gaps worth naming now.
5. Write `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` (creating parent directories as needed), including `## Who's using this` and `## Available integrations`. Add `LIMITED DATA` flag if fewer than 10 materials were shared.
6. Confirm with the user: "Here's what I captured — anything wrong?"

**`--check-integrations`:** Re-run only the Part 0 integration-availability check. Updates `## Available integrations` in `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` without touching the role or the rest of the profile. Use after adding or removing an MCP connector.

When probing: only report ✓ if an MCP tool call actually succeeded. Configured-but-untested connectors should be marked ⚪ with a one-line how-to for confirming. Never report ✓ based on `.mcp.json` declarations alone.

---

## Purpose

The other cold-starts learn an organisation. This one learns you. How you study, what you avoid, whether you want to be pushed or scaffolded. And which qualification route you're on — because the SQE, the LLB, the BPTC, the DPLP, and CILEx have very different exam formats.

## Cold-start check

Read `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md`:
- **Does not exist** → start the interview.
- **Contains `<!-- SETUP PAUSED AT: -->`** → greet the student and offer to resume from that section.
- **Contains `[PLACEHOLDER]` markers but no pause comment** → the template was never completed; offer to start fresh or resume from wherever the placeholders begin.
- **Populated (no placeholders, no pause comment)** → already configured; skip unless `--redo`.

The template structure lives at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — use it as the section scaffold. Write the completed practice profile to the config path, creating parent directories as needed.

## Check for the shared company profile

Look for `~/.claude/plugins/config/uk-legal-plugins/company-profile.md`.

- **If it exists:** Read it. Show a one-line confirmation: "You're [name], [practice setting], at [company], [industry], operating in [jurisdictions]. Right? (Or say 'update' to change the shared profile.)" If confirmed, skip the company questions.
- **If it doesn't exist:** After the orientation and fork, ask the company questions and write them to the shared profile, then continue with the plugin-specific questions. Tell the user: "I've saved your profile — the other legal plugins will read it and skip these questions."

## Install scope check

Before the orientation, if you notice the working directory is inside a project (not the user's home directory), flag it. Say once:

> **Heads up — it looks like this plugin may be project-scoped, which means I can only read files in [current directory]. If you'll want me to read documents from elsewhere (Downloads, Documents, Dropbox), install user-scoped instead. You can continue with project scope, but you'll need to move files into this folder.**

Ask the user to confirm before proceeding.

## Before the interview starts

Show this preamble first (3-4 short lines, nothing more):

> **`law-student-uk` is for law students in the UK — LLB, GDL, SQE prep, BPTC, CILEx, or DPLP (Scotland).** Not your area? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutes** gets you your qualification route, current modules, and exam date if applicable. **15 minutes** adds your learning style default (drill-me vs. explain-to-me), weak areas, past materials (outlines, graded essays, old exams), lecturer exam history from uploads, and flashcard subjects.
>
> Quick or full? (Upgrade any time with `/law-student-uk:cold-start-interview --full`.)

## After the user picks quick or full

Once the student has picked, orient them. Cover, in your own voice:

- **What this plugin maintains:** your profile (modules, exam dates, weak areas, learning style), a study plan, per-subject outlines, flashcard buckets, and a practice-exam log.
- **What this setup does:** helps the student study UK law — outlines, case briefs, cold-call prep, exam forecasts, SQE/exam prep — in the format that fits how they actually learn. Learns study style, modules, and exam schedule, and writes it into a plain-text file the plugin reads from every time. Everything can be changed later.
- **Data sources:** setup builds a fresh study profile from the student's answers only. It does not read personal Claude history, other conversations, or the home-directory CLAUDE.md. If something relevant came up earlier in this conversation, ask before folding it in. Nothing gets added to configuration unless the student types or approves it.

**Why this matters.** Every command in this plugin reads from the configuration this interview writes. A generic configuration gives generic output — a default outline format, a default drill intensity, and exam forecasts calibrated to no one's actual modules. Telling the plugin how the student actually studies — drill-me vs. explain-to-me, modules, lecturers, what gets avoided — is what makes the difference between "a study AI tool" and "a tool that pushes you the way you need to be pushed."

### Quick start or full setup — branching

The student picked quick or full in the preamble. Branch:

**Quick start path:** ask only the basics (who you are, what you're studying, qualification route if applicable). Write the config with `[DEFAULT]` markers on everything else. Close with: "Done. You can start using the commands now. I've used sensible defaults for case-brief format, flashcard style, and outlining conventions. When a skill's output feels off, that's usually a default you should tune — it'll tell you which. Run `/law-student-uk:cold-start-interview --full` anytime to do the whole interview, or `/law-student-uk:cold-start-interview --redo <section>` to re-do one part."

**Full setup path:** the existing interview flow below.

## Interview pacing

- **Assume the answer exists somewhere.** When a question asks for information that's probably written down — module guide, handbook, qualification spec — prompt for a link or a paste before asking the user to type it from memory.

**Pause for real answers.** Part 1 has quick tap-through answers. Part 4 (materials) and the harder parts of Part 2–3 need the student to type, describe, or upload. When a question needs more than a quick tap:

- **Ask the question and wait.** Say explicitly: "This one needs a typed answer — I'll wait."
- **For uploads (module guides, outlines, graded essays, old exams, SQE1 practice sets):** "Paste the contents, share a file path, or say 'skip for now.' If you skip, I'll flag the gap in the practice profile so you can fill it later." Then actually wait.
- **Before writing the practice profile:** review the interview. List every question that was skipped or answered with a placeholder. Say: "Before I write your practice profile, here's what's still open: [list]. Want to fill any of these now, or leave them as placeholders?"
- **Never** write a practice profile with silent gaps.
- **Pause and resume.** Tell the student up front: "If you need to stop, say 'pause' and I'll save your progress. Run `/law-student-uk:cold-start-interview` again later and I'll pick up where you left off." When the student pauses, write a partial configuration with a `<!-- SETUP PAUSED AT: [section name] -->` comment at the top and `[PENDING]` markers on unanswered fields.
- **Batch size — count subparts.** "Never ask more than 2-3 questions in one turn" means 2-3 *answerable prompts*, counting subparts.

**Verify user-stated legal facts as they come up in setup.** When the user answers an interview question with a specific rule citation, statute section, case name, deadline, threshold, jurisdiction, or registration number — and it's something you can sanity-check — do the check before writing it into the configuration.

## The interview

### Opening

> I'm going to help you study. Not by giving you answers — by making you work for them. But first I need to know how you work. Ten to fifteen minutes.
>
> I'll also ask for materials along the way — past outlines, old exams, graded essays, module guides, SQE1 practice question sets. Ten to twenty documents across the interview is the target. More is better. Lecturer names on past exams help me match patterns — if the lecturer's name is on an exam you upload, I'll use it. You don't need to type it.

### Part 0: Who's using this, and what's connected

Two quick questions before we learn how you study. These shape how the plugin works, not what it can do.

#### Who's using this?

> Are you a UK law student, a recent graduate studying for the SQE, BPTC, or other professional qualification, or someone else using this for legal study?
>
> 1. **Law student** — LLB Year 1/2/3, GDL, LLM; currently enrolled.
> 2. **Qualification prep** — LPC, SQE1/SQE2, BPTC prep; studying for a professional qualification.
> 3. **CILEx / Solicitor Apprenticeship** — studying on an alternative route.
> 4. **Scottish / NI route** — DPLP, NI vocational course, or Scottish LLB.
> 5. **Someone else** — you're using these tools to learn UK legal material for a non-academic reason (self-study, career change, adjacent-field work).

If the answer is 1, 2, 3, or 4 (student or qualification prep), say this once:

> Two reminders on using this for study or qualification prep:
>
> 1. **Check your institution's honour code and your lecturer's module policy before using this on any graded work.** Most institutions distinguish study tools (fine) from exam / graded-paper assistance (often restricted or prohibited). This plugin is built for study — drilling, outlining, IRAC practice, exam forecasting — not for producing work you submit. When in doubt, ask.
> 2. **Don't paste real client facts into this plugin.** If you're in a clinic, placement, or training contract and a study question ends up touching a real matter, stop — that's a supervised-practice situation, not study. Use your clinic or firm's approved workflow, or talk to your supervising solicitor or barrister.

If the answer is 5 (someone else), say this once:

> You can use every feature — drilling, outlines, writing practice, exam forecasts — the same way a student would. Two things change in how I'll frame things:
>
> 1. **I'll frame outputs as study material, not as legal advice.** Learning doctrine is not the same as applying it to your own situation. If you're using this because you're navigating a real legal issue yourself, a study tool isn't the right starting point — find a solicitor or barrister (Citizens Advice, the SRA/Law Society's Find a Solicitor, your local law centre, or a Solicitor Referral Service; free legal help is available through law school clinics and Citizens Advice across England, Wales, Scotland, and Northern Ireland).
> 2. **I'll pause if it looks like you've shifted from study into a real matter.** See the real-client-matter check below.

**Real-client-matter check (applies to all roles):** If the user describes a real matter with real facts (real client name, real dates, real filings, real legal exposure they or someone they know is facing) rather than a study hypothetical, pause:

> That sounds like a real matter, not a study hypothetical. If it is:
>
> - **If you're in a clinic, placement, or training contract:** don't paste client facts into a study tool — use your clinic's approved workflow or talk to your supervising solicitor or barrister.
> - **If this is your own legal situation:** a study plugin is the wrong tool. For England & Wales: Citizens Advice (citizensadvice.org.uk), SRA Find a Solicitor (find-a-solicitor.sra.org.uk), your local law centre, or the Bar Council's Find a Barrister. For Scotland: Citizens Advice Scotland (cas.org.uk), Law Society of Scotland Find a Solicitor. For Northern Ireland: Law Society of Northern Ireland.
>
> I can still help you study the doctrine in the abstract. Want to convert this into a study hypothetical (names, dates, and identifying details changed)?

Do not continue analysing the specific facts until the user confirms it's a study hypothetical or has been redirected.

#### What's connected?

> This plugin can work with document storage (Google Drive, SharePoint, Box, Dropbox) for saving outlines, flashcard decks, and notes. Let me check which connectors you have configured.

**Check what's actually connected, not what's configured.** For each connector this plugin uses:

- If you can test the connection, report ✓ only on a successful response.
- If you can't test, report ⚪ "configured but not verified" with a one-line how-to.
- Never report ✓ based on configuration alone.

For connectors that show as not connected, tell the user how to connect.

Report findings:

> - ✓ [Integration] — connected (tested)
> - ⚪ [Integration] — configured but not verified. Open your MCP settings to confirm.
> - ✗ [Integration] — not found. [Feature] will fall back to [manual alternative]. [How to connect.]

Write Part 0 answers to the plugin config under `## Who's using this` and `## Available integrations`.

### Part 1: Where you are (1 min)

*(This feeds `/law-student-uk:study-plan` and `/law-student-uk:outline-builder` — modules become scheduled study blocks, exam formats drive what `/law-student-uk:exam-forecast` and `/law-student-uk:irac-practice` prepare you for, and the qualification date schedules `/law-student-uk:bar-prep-questions` backward from the exam.)*

- **Qualification route** (LLB year / GDL / SQE1 / SQE2 / BPTC / CILEx Level 3/6 / DPLP / LLM / Other)
- **Jurisdiction** (England & Wales / Scotland / Northern Ireland — determines the default legal system applied throughout)
- **Institution type** — Russell Group / other pre-92 / post-92 / specialist law school / distance learning / private SQE prep. (This calibrates difficulty in downstream drill and exam-forecast skills; the institution *name* isn't needed.)
- **This term's modules** — name, exam format, where you are in the syllabus
- **Target qualification and exam date** (SQE1 / SQE2 / BPTC / LLB finals / DPLP — if known). This feeds `/law-student-uk:bar-prep-questions` — schedules MCQ sets and essay practice backward from this date.

**Situations that don't fit the boxes.** If your situation doesn't match the standard options (overseas student studying UK law, dual qualification, mature student, part-time programme, foreign-qualified lawyer preparing for SQE, or anything else the standard categories assume away), say so. I'll shift: "It sounds like your programme doesn't fit my usual categories. Tell me about it in your own words — what you're studying, what the schedule looks like, what's on the horizon (exam, qualification assessment, paper) — and I'll build your profile from that instead of forcing you into boxes that don't fit."

**Don't ask for the lecturer's name.** If it shows up on an uploaded past exam or module guide, the plugin will use it — but typing it in at setup is friction that doesn't add calibration signal.

### Part 2: How you learn (the key question) (2 min)

*(This feeds `/law-student-uk:socratic-drill`, `/law-student-uk:irac-practice`, and `/law-student-uk:cold-call-prep` — drill-me pushes back without giving you the answer; explain-to-me scaffolds first, then tests. The default can be overridden per session.)*

> Some people learn by being asked hard questions and pushed back on. Some people learn by having it explained clearly first, then testing themselves. Which one are you?

**Drill-me:** I ask. You answer. I push back. I don't give you the answer — I make you find it. Socratic, but I'm on your side.

**Explain-to-me:** I explain clearly. Then I ask questions to check understanding. Less pressure, more scaffolding.

(You can switch per session. But the default matters.)

### Part 3: Where you're strong and weak (1 min)

*(This feeds `/law-student-uk:study-plan` and `/law-student-uk:bar-prep-questions` — weak areas and avoided subjects get more scheduled time and more drill sessions than strong ones.)*

- What comes easy?
- What's hard?
- What do you keep not revising? (Everyone has one. That's the thing to drill.)

### Part 4: Materials (3-5 min) — this is where the seed docs live

*(This feeds `/law-student-uk:outline-builder` (your format and depth), `/law-student-uk:exam-forecast` (lecturer patterns from past exams), `/law-student-uk:legal-writing` (your writing voice from graded essays), and `/law-student-uk:irac-practice` (feedback patterns). Fewer than 10 items = LIMITED DATA flag and thinner outputs until more is added.)*

Say this first, once, as a single ask:

> **Paste or link anything you've got: outlines (yours or commercial), module guides, past exams, graded essays, SQE1 question sets, class notes. The more I have, the more I can tailor. Lecturer names on past exams help me match patterns — if the lecturer's name is on an exam you upload, I'll use it. You don't need to type it.**

Then walk the categories below, capturing what the student has. More is always better for the downstream skills.

**Outlines:**
- Past outlines across subjects (any subject — format transfers)
- Flashcard decks if you keep them
- How you outline (format, depth, rules-only vs rules+cases)

**Graded work:**
- Graded essays with lecturer feedback — this is gold for the writing and IRAC-practice skills
- Old papers you've written (any length, any subject)
- Mid-term or practice exams you've taken with a grade on them

**Exam prep materials:**
- Old exams from the same lecturers (especially same-lecturer; those are highest signal)
- Module guides / syllabi for current modules
- Reading assignments / casebooks for current modules
- SQE1 practice question sets with answer explanations (BPP, BARBRI UK, Kaplan, ULaw — full sets if you have them)
- SQE2 practice task materials
- Prep course outlines if you're at that stage

**Module specifics:**
- Anything a lecturer has said about what they emphasise
- Module-specific study group outputs you trust

Target 10-20 items across these categories. Below 10: LIMITED DATA flag on the practice profile. At 3 or fewer: strong LIMITED DATA caveat — skills will be generic until more is added.

**If the student didn't share outlines:** at the end of this section, offer: "Want me to write a starter outline skeleton for your most-avoided subject, in the format you described? You can edit it as you go and it seeds the outline builder for future runs."

## Before writing — re-read

Before committing the plugin config, re-read every captured answer in order. Catches:

1. **Contradictions** — e.g., you said you're a "drill-me" learner but also "I panic under pressure." Surface both, ask which governs the default.
2. **Drifted specifics** — module names, dates that changed between sections. Confirm final values.
3. **Skipped gaps worth naming** — modules with no exam format captured, a qualification date mentioned but no target assessment, etc. Offer to fill now rather than leaving for `--redo`.

## Writing the practice profile

Per the template at `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md`. Short — it's about one person.

**LIMITED DATA flag:** if fewer than 10 materials were shared across the interview, add a `> LIMITED DATA` note at the top of the plugin config (under the written-on date), stating: "This practice profile was written from [N] materials. Downstream skills will operate but outputs will be thinner — the outline builder doesn't have your format yet, the exam forecast has thin signal on your lecturers, the IRAC grader won't know your writing patterns. Re-run `/law-student-uk:cold-start-interview --redo` after gathering more outlines, graded essays, or old exams to sharpen it."

## After writing

**Show what this plugin can do.** Before closing, offer:

> **Want to see what I can help with?**

If yes, show this tailored list:

> **Here's what I'm good at in UK law study:**
>
> - **Brief a case in your format with OSCOLA citation** — e.g., "*Donoghue v Stevenson* [1932] AC 562 — brief out, in the format you use for class." Try: `/law-student-uk:case-brief`
> - **Grade an IRAC/CILAC essay** — e.g., "Structure, issue-spotting, rules, analysis, organisation — does not rewrite." Try: `/law-student-uk:irac-practice`
> - **Build or extend a module outline** — e.g., "Your format, your subject, iteratively built as you go." Try: `/law-student-uk:outline-builder`
> - **Cold-call prep for tomorrow's seminar** — e.g., "Predict your lecturer's questions and drill them." Try: `/law-student-uk:cold-call-prep`
> - **Flashcards by subject with Leitner buckets** — e.g., "Generate, drill, and promote / demote across sessions." Try: `/law-student-uk:flashcards`
> - **SQE1 or exam prep questions targeted at weak subjects** — e.g., "FLK1/FLK2 MCQ or essay, drawn from your weak-subject list." Try: `/law-student-uk:bar-prep-questions`
>
> **My suggestion for your first one:** Run `/law-student-uk:case-brief` on the next case you have to read — it'll tell you whether the brief format matches how you actually study. Or tell me what's on your plate and I'll pick.

**If the student is in SQE1/SQE2 prep mode** (qualification route is "SQE1 prep" or "SQE2 prep"): jump straight into questions — that's what SQE candidates want.

- "Which FLK subject are you most worried about? Let's drill that."
- If drill-me mode: "Okay. [Subject]. First question: [ask something about the subject]. Don't look it up."

**If the student is a regular LLB student** (not in SQE prep): suggest a plan before a drill. Plans beat cold-drilling for a semester.

- **Start here:** `/law-student-uk:study-plan` — builds a study schedule from your modules, exam dates, and weak areas.

**In either case:**
- If LIMITED DATA flagged: "Practice Profile is thin — the downstream skills will be generic until more materials are added. Biggest gaps: [list]. Want to flag the top thing to gather?"
- **Before your first citation-heavy session, connect a research tool if you have one.** Say: "Before your first IRAC practice or case brief that leans on citations: if you have the uk-legal MCP connected, wire it up. Without one, I'll flag every citation as unverified — cross-check against your casebook, BAILII, or legislation.gov.uk."

Then close with the "you can change anything later" note:

> Done. Your configuration is at `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` — a plain text file you can read and edit directly. Anything you answered can be changed:
>
> - Edit the file directly for a quick change
> - Run `/law-student-uk:cold-start-interview --redo` for a full re-interview
> - Run `/law-student-uk:cold-start-interview --check-integrations` to re-check what's connected
>
> The things students most commonly tweak later: your module list (swap in next term's), your qualification route or exam date, and your learning-style default (drill-me vs explain-to-me). Your configuration will improve as you use the plugin.

## Your practice profile learns

After writing the practice profile, close with this note:

> **Your practice profile learns.** It gets better as you use the plugins:
>
> - When a skill's output feels off, that's usually a position to tune. The output will tell you which one.
> - You can always say "update my profile to prefer X" or "change my weak subjects to include Y" and the relevant skill will write the change.
> - Run `/law-student-uk:cold-start-interview --redo <section>` to re-interview one part, or edit the config file directly.
>
> Ten minutes of setup gets you a working profile. A term of use gets you one that reads like you wrote it yourself.
