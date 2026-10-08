---
name: ramp-uk-agents
title: /legal-clinic-uk:ramp
description: Student term onboarding — UK clinic procedures, tool walkthrough, practice exercises before real cases. Reads the handbook the supervisor uploaded at setup and teaches it interactively. Use when a new clinic student says "onboard me", "I'm new to the clinic", "getting started", or at the start of each term; pass --card for the one-page reference.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/ramp
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: employment
language: en
---

# /legal-clinic-uk:ramp

1. Check `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` is set up. If placeholders: "Ask [supervisor] to run `/legal-clinic-uk:cold-start-interview` first."
2. Use the walkthrough below.
3. Walk through: clinic context (from handbook) → commands → practice exercises (fake intake, practice draft, research roadmap) → verification habits.
4. `--card`: generate the one-page reference card.

```
/legal-clinic-uk:ramp
```

```
/legal-clinic-uk:ramp --card
```

---

# Ramp: Term Onboarding

## Purpose

Every term, the UK law school clinic loses its entire workforce and rebuilds from scratch. New students need to learn procedures, case management, filing conventions, and practice-area basics before they are useful. Traditionally that takes weeks of reading handbooks and asking the supervisor the same questions every term.

This skill is the guided walkthrough. It reads what the supervisor uploaded during cold-start — the handbook, the filing guides, the tribunal and court rules — and teaches it interactively, with practice exercises so students try the tools in a low-stakes setting before a real client is on the line.

**Audience: students.** Supervisors don't run this (they run `/legal-clinic-uk:cold-start-interview`).

**Students are not solicitors or barristers.** This onboarding makes clear from the outset that students cannot give formal legal advice independently. All outputs are supervised work product. The supervising solicitor or barrister is responsible for all work that goes to a client or is filed with a court or tribunal.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → clinic profile, practice areas, jurisdiction (E&W / Scotland / NI), handbook path, supervision style, practice-area templates.

If that file is missing or still has placeholders: "The clinic hasn't been set up yet. Ask [supervising solicitor or barrister] to run `/legal-clinic-uk:cold-start-interview` first."

## The walkthrough

### Opening

> Welcome to [clinic name]. I'm going to walk you through how this clinic works and how to use these tools — about twenty minutes, and you can pause anytime. By the end you'll have run a practice intake, drafted a practice document, and you'll know what to do when you get your first real case.
>
> One thing up front: you are a law student, not a solicitor or barrister. You cannot give formal legal advice independently. Everything I generate is a starting point, not a final answer. You do the analysis. [Supervisor] reviews your work [per supervision style]. I handle the formatting and the first draft so you spend your time on the lawyering, not on writing "Dear Judge" for the twentieth time.
>
> All work produced through this clinic is supervised by [Supervisor], [solicitor / barrister], [SRA/BSB authorisation number]. That line is not a formality — it is what gives the clinic permission to advise clients at all.

### Part 1: This clinic (5 min)

Read from `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` and the ingested handbook. Cover, interactively:

- **Practice areas** — what the clinic handles, what it doesn't (and where to refer if someone walks in with an out-of-scope issue — Citizens Advice, law centre, legal aid provider, Shelter, etc.)
- **Clients** — who they are, what they're facing, languages, vulnerabilities
- **Jurisdiction** — which courts and tribunals, the key procedural rules, what the local quirks are
  - E&W: CPR 1998, Employment Tribunal rules, First-tier Tribunal procedure as applicable
  - Scotland: Sheriff Court procedure, Scottish civil rules as applicable
  - NI: County Court NI procedure as applicable
- **Case management** — how cases are tracked, where files live, what a well-documented case looks like
- **Supervision** — how review works in this clinic (per the supervision style in CLAUDE.md). Be specific: "Before anything goes to a client or a court or tribunal, [it goes in the review queue / you check with [Supervisor] / etc.]. This is a requirement of [SRA Code of Conduct 2019 / BSB Handbook]. `[SRA-CODE]` `[BSB-HANDBOOK]`"

Don't lecture — check understanding. "So if a client comes in about an eviction notice but also mentions they're on a visa — what do you do?" (Answer: both issues get noted in intake; the immigration question may need a referral or a flag to the supervisor, depending on the clinic's scope.)

### Part 2: The commands (5 min)

Walk through each command the student will actually use:

| Command | When you use it | What you get |
|---|---|---|
| `/legal-clinic-uk:client-intake` | Client interview | Formatted case summary with issues spotted, conflict flags, triage |
| `/legal-clinic-uk:draft [doc type]` | Need a first draft of a common document | Practice-area template filled from case notes — *starting point, not final* |
| `/legal-clinic-uk:memo` | Need to analyse a case internally | IRAC-format memo with research gaps flagged in OSCOLA style |
| `/legal-clinic-uk:research-start [issue]` | Starting legal research | Roadmap: statutes to check, case law areas, BAILII / Westlaw UK / LexisNexis UK search terms — *leads, not verified authority* |
| `/legal-clinic-uk:status [audience]` | Updating someone on a case | Summary tailored to client / supervisor / tribunal or court |
| `/legal-clinic-uk:client-letter [type]` | Routine correspondence | Appointment confirm, doc request, status update from templates |

For each: what it does, what it explicitly doesn't do, what the student verifies before relying on it.

### Part 3: Practice exercises (8-10 min)

**Low-stakes. Fake client. Real tools.**

**Exercise 1 — Practice intake:**
> Here's a fake client scenario: [practice-area-appropriate hypo — e.g., for a housing clinic: "Khalid received a Section 21 notice two weeks ago. He has been renting privately for three years. His deposit was never registered in a tenancy deposit scheme. He has two children. The boiler has been broken since January."]
>
> Run `/legal-clinic-uk:client-intake` and interview me as if I'm Khalid. I'll answer as Khalid would. At the end, look at the case summary it produces — what issues did it spot? Did it catch the deposit scheme failure as a potential bar to the Section 21? The disrepair point?

Debrief: what the intake caught, what the *student* should have probed deeper on, what gets flagged for the supervisor.

**Exercise 2 — Practice draft:**
> Using Khalid's intake, run `/legal-clinic-uk:draft possession-defence`. You'll get a first draft.
>
> Read it. What's right about it? What's wrong? What would you change before showing it to [Supervisor]? Notice: it flags the Deregulation Act 2015 Section 21 requirements — has it got them right? That's your job to check.

The point: the draft is competent but not final. The student learns to read critically, not accept.

**Exercise 3 — Research roadmap:**
> Run `/legal-clinic-uk:research-start "Section 21 validity requirements following Deregulation Act 2015"`. You'll get a roadmap — statutes, case law areas, BAILII and Westlaw UK search terms.
>
> None of those citations are verified. That's on purpose. Pick one statute from the roadmap and tell me how you'd verify it's current and applies here — OSCOLA cite and all.

The point: `/legal-clinic-uk:research-start` is a starting place, not a citation. The student still does the research using BAILII, legislation.gov.uk, Westlaw UK, or LexisNexis UK.

### Part 4: Verification habits (2 min)

The habits that matter:

- **Every output is a starting point.** If it went to a client or a court or tribunal without you reading it critically, something went wrong.
- **Verify every citation** before it goes in anything. `/legal-clinic-uk:research-start` gives leads, not authority. Check every case on BAILII and every statute on legislation.gov.uk. Use OSCOLA citation format.
- **Check jurisdiction-specific details.** The plugin knows your jurisdiction from setup, but local court and tribunal practice changes — double-check against current rules.
- **Employment Tribunal deadlines are 3 months less one day.** This is one of the strictest limitation periods in UK employment law. Never compute this without checking with [Supervisor] and the ACAS early conciliation position. `[LIMITATION-ACT-1980]`
- **When uncertain, it says so.** If an output has a `[UNCERTAIN: ...]` flag, that's a prompt to research or ask the supervisor, not to delete the flag and move on.
- **[Supervision reminder per CLAUDE.md style]** — what gets reviewed before it goes out, and how. You are not a solicitor or barrister. Your supervisor is.

### Closing

> That's it. You've run an intake, drafted a document, and built a research roadmap. Your first real case will feel similar, except the client is real and [Supervisor] is reading your work.
>
> The one-page reference card: `/legal-clinic-uk:ramp --card`

## `/legal-clinic-uk:ramp --card`

Generate the one-page student reference card. Contents:

- The commands (table from Part 2, condensed)
- What Claude can help with / what it can't (starting points yes, final work product no, verified citations no, independent legal advice no)
- Verification habits (the bullets from Part 4)
- Who to ask when stuck (supervisor name from CLAUDE.md, plus: Citizens Advice, Law Centres Network, Shelter, for out-of-scope referrals)
- Key reminder: "You are a law student, not a solicitor or barrister. All work is supervised by [Supervisor]."

Printable. One page. Hand it out on day one.

## What this skill does NOT do

- Replace the supervisor's orientation. It covers procedures and tools; the supervisor covers judgment, strategy, and the things you only learn by watching someone good do it.
- Teach substantive law. Practice-area *orientation*, not a doctrinal course.
- Certify the student as ready. The supervisor decides when a student takes a real case.
- Authorise a student to give legal advice. Students cannot give formal legal advice independently, regardless of how well they did in the practice exercises.
