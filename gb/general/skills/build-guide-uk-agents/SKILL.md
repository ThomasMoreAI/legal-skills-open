---
name: build-guide-uk-agents
title: /legal-clinic-uk:build-guide
description: Help a UK clinic supervisor author a practice-area guide that configures how student-facing skills behave — intake questions, pedagogy posture (assist / guide / teach), review gates, cross-plugin checks, and local court/tribunal rules. Use when a supervising solicitor or barrister wants to build or revise a per-practice-area guide, tune how the clinic skills behave for their clinic type, or set their teaching philosophy as plugin configuration.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/legal-clinic-uk/skills/build-guide
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /legal-clinic-uk:build-guide

1. Load `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → role (must be Supervising solicitor or barrister), practice areas, jurisdiction (E&W / Scotland / NI).
2. Use the workflow below.
3. If the user is not the supervising solicitor or barrister, stop and redirect (students run `/legal-clinic-uk:ramp`).
4. Walk through: practice area → intake questions → pedagogy posture → review gates → cross-plugin checks → local court/tribunal rules.
5. Write `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/guides/<practice-area>.md`. Create the `guides/` directory if needed.
6. Offer a test run — run `/legal-clinic-uk:draft` under the configured posture so the supervisor sees what a student sees.

```
/legal-clinic-uk:build-guide
```

Multiple guides are fine — one per practice area. Re-run this command to revise. Edit the guide file directly for quick changes.

---

# Build Guide: Supervisor-Authored Practice-Area Guide

## Purpose

The supervisor guide is the dial that turns student-facing skills from "get the work done" into "teach the student to do the work." Every student-facing skill in this plugin reads the guide before producing output: intake asks the questions the supervisor wants asked, drafting skills pick a pedagogy posture (assist / guide / teach), review gates route to the supervisor on the items the supervisor cares about, and cross-plugin checks wrap other-plugin skills in a supervision layer.

This skill helps a supervisor author that guide in 5-10 minutes per practice area. The guide is plain markdown at a well-known path — edit it by hand anytime.

**Audience: the supervising solicitor or barrister.** Not students. Students run `/legal-clinic-uk:ramp` and then the student-facing skills; they don't author guides.

## Work-product header

Every output from this skill is a supervisor-facing configuration artifact, not student work product. Do NOT prepend `[AI-ASSISTED DRAFT — requires student analysis and supervising solicitor/barrister review]` to the output of this skill — that label is for student outputs. The guide file this skill writes is a supervisor configuration document; it sits next to CLAUDE.md in the plugin config directory.

## Key things your guide should address

Offer this as a checklist the supervisor can skip through or use as the table of contents for the interview:

- What does a student need to know before they touch a case? (SRA/BSB supervision obligations, confidentiality, their scope of authority as a student)
- What are the 3-5 most common mistakes students make in this practice area, and how should the skill catch them?
- When must the student stop and get your sign-off? (Tribunal/court filing, sending to a client, making a representation, advising on strategy) — per your SRA/BSB obligations `[SRA-CODE]` `[BSB-HANDBOOK]`
- What's the reading level for client communications? (Plain English / 6th-grade equivalent is the usual target for a legal aid / advice clinic context)
- What local court or tribunal rules, forms, or deadlines should every student know? — including any jurisdiction-specific differences between E&W, Scotland, or NI `[CPR-RULE]`
- When should the skill teach vs. do? (Per document type)

## Workflow

### Step 1: Check role

Read `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/CLAUDE.md` → `## Who's using this` → Role. If the role is not "Supervising solicitor" or "Supervising barrister," say:

> This skill is for supervisors — it configures how the student-facing skills behave. If you're the supervisor, make sure your practice profile role is set correctly in `/legal-clinic-uk:cold-start-interview`. If you're a student, this isn't the right skill for you — run `/legal-clinic-uk:ramp` to onboard, or ask your supervisor to author a guide for your clinic.

Stop if the role is not a supervising solicitor or barrister.

### Step 2: Which practice area?

> What clinic is this guide for? (Housing / Employment / Immigration & Asylum / Family / Consumer & Debt / Benefits / Criminal Defence / Other)

If the answer is "Other," ask for a short name — that name becomes the filename (lowercase, hyphenated: `housing-disrepair.md`, `employment-discrimination.md`, etc.).

Check the practice areas listed in `CLAUDE.md` → `## Clinic profile` → Practice areas. If the chosen practice area is not listed there, note it: "I'll write this guide, but your practice profile doesn't list [area] as one of your clinic's practice areas. Add it via `/legal-clinic-uk:cold-start-interview --redo` — but the student-facing skills won't route intakes to this area until the profile lists it."

If a guide already exists at `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/guides/<practice-area>.md`, offer: "A guide for [area] already exists at [path]. Do you want to (a) revise it section-by-section, (b) start fresh and overwrite, or (c) see what's there first?"

### Step 3: Intake questions

> What should students ask a new client for this clinic type? I'll start with a generic intake for [practice area] — tell me what to add, remove, or change. What red flags should students look for? What makes a case a good fit for your clinic vs. a referral out?

Show the generic intake defaults for the practice area — use the same defaults that `client-intake` uses (Housing: housing type, notice type, deposit, disrepair, court date; Employment: status, ACAS EC cert, nature of claim, dates, internal proceedings; Immigration: status, entry, prior applications, country conditions, timeline urgency; Family: relationship, issue, children, safety, orders; Consumer/Debt: debt type, creditor, documentation, court claim; Benefits: benefit type, decision, stage, dates). For practice areas outside these, ask the supervisor to describe the intake from scratch.

Capture: questions to add, questions to remove, questions to rephrase, red flags (a list), good-fit criteria (what makes this a case the clinic takes vs. refers out), referral destinations for out-of-scope matters (Citizens Advice, Shelter, Law Centres Network, specialist legal aid providers).

### Step 4: Pedagogy posture

> How much should the skills do vs. how much should the student do?
>
> - **Guide (default):** The skill produces structure; students fill in substance; the skill gives feedback. Balanced — most clinics start here.
> - **Assist:** The skill produces work product; students review and learn by editing. Fastest. Good for high-volume clinics or when tribunal deadlines are tight.
> - **Teach:** The skill doesn't produce work product — students draft, the skill gives Socratic feedback and only shows models after two attempts. Most pedagogical.
>
> You can set this per document type (e.g., teach for client letters, assist for tribunal claim narratives when the ET1 window is tight).

Capture the default posture for the practice area, and any per-document overrides.

- `pedagogy_posture_default: assist | guide | teach`
- `pedagogy_posture_client_letter: [override]`
- `pedagogy_posture_memo: [override]`
- `pedagogy_posture_draft: [override]`

### Step 5: Review gates

> Which work product needs your sign-off before it goes to a client? Which can students send directly? Under your SRA/BSB obligations as the supervising solicitor/barrister, you're responsible for the work done under your supervision. `[SRA-CODE]` `[BSB-HANDBOOK]`

Present the options as a table:

| Work product | Gate |
|---|---|
| Intake summary | [student writes; supervisor reviews at case rounds / supervisor reviews before client sees / student keeps] |
| Memo (internal) | [supervisor reviews / student keeps] |
| Client letter (appointment / doc request / brief status) | [supervisor reviews / student sends directly] |
| Client letter (substantive advice / bad news) | [always supervisor — cannot override] |
| Draft filing (tribunal / court) | [always supervisor — cannot override] |
| Status update to tribunal or court | [always supervisor — cannot override] |
| Research-start roadmap | [student works from it directly] |

Non-negotiable gates: client letters that give substantive advice, tribunal/court filings, and status to courts/tribunals always route through the supervisor. These cannot be overridden — they are a requirement of the SRA/BSB supervision framework. The configurable gates are the routine ones.

### Step 6: Cross-plugin checks

> Do you want students to use skills from other plugins? I can wrap them in supervision — the student runs the check, the output flags uncertainty for your review, nothing goes out without your sign-off.

Concrete examples tied to UK clinical practice:

- **Housing clinic:** `commercial-legal:review` for tenancy agreement review, flagged for supervisor before going to the client.
- **Employment clinic:** `litigation-legal:chronology` for building a timeline from client documents, flagged for supervisor before it feeds an ET1.
- **Immigration clinic:** `litigation-legal:witness-statement-check` for asylum statement review, wrapped so the supervisor signs off before a statement is submitted.
- **Any clinic:** privacy / data protection check if the student is handling any matter where client data is shared outside the clinic.

If the supervisor names a cross-plugin skill they want, record: skill name, when students should use it, what supervision wrapper applies.

### Step 7: Local rules and jurisdiction

> What court(s) and tribunal(s) does your clinic practice in? Any specific rules, forms, or practice directions students need to use?

Check `CLAUDE.md` → `## Jurisdiction` — the jurisdiction is already set at cold-start. This step is for practice-area-specific court and tribunal rules (e.g., "HMCTS Housing Possession Court guidance," "Employment Tribunal presidential guidance for [region]," "First-tier Tribunal (Immigration) practice statements," "County Court Bulk Centre for possession claims over N units").

Note any jurisdiction-specific differences between E&W, Scotland, and NI where they affect this practice area. These differences are material and the skill should flag them for the student.

### Step 8: Write the guide

Write to `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/guides/<practice-area>.md`. Create the `guides/` directory if it doesn't exist. Use this structure:

```markdown
# Practice-area guide: [Practice area]

*Authored by the supervising solicitor/barrister via `/legal-clinic-uk:build-guide`. Student-facing skills read this before producing output. Edit directly anytime.*

**Last updated:** [date]
**Authored by:** [supervising solicitor/barrister name from CLAUDE.md]

---

## Intake

**Questions to ask** (supplement/replace the generic defaults):
- [question 1]
- [question 2]

**Red flags** (surface these in the intake summary if present):
- [flag 1 — e.g., "ET1 window expiring within 4 weeks — escalate to supervisor immediately"]
- [flag 2]

**Good-fit criteria** (cases this clinic takes):
- [criterion 1]
- [criterion 2]

**Refer-out criteria** (cases this clinic does not take):
- [criterion 1 — e.g., "criminal proceedings — refer to duty solicitor scheme"]
- [refer-out destinations — Citizens Advice, Shelter, Law Centres Network, relevant specialist provider]

---

## Pedagogy posture

`pedagogy_posture_default: [assist | guide | teach]`

Per-document overrides (optional):
- `pedagogy_posture_client_letter: [assist | guide | teach]`
- `pedagogy_posture_memo: [assist | guide | teach]`
- `pedagogy_posture_draft: [assist | guide | teach]`

**Rationale:** [one or two sentences from the supervisor on why this posture]

---

## Review gates

| Work product | Gate |
|---|---|
| Intake summary | [gate] |
| Memo (internal) | [gate] |
| Client letter — routine | [gate] |
| Client letter — substantive | supervisor (fixed — SRA/BSB requirement) |
| Draft filing (tribunal/court) | supervisor (fixed — SRA/BSB requirement) |
| Tribunal/court-facing status | supervisor (fixed — SRA/BSB requirement) |
| Research roadmap | [gate] |

---

## Cross-plugin checks

| Skill | When students use it | Supervision wrapper |
|---|---|---|
| [plugin:skill] | [situation] | [wrapper] |

---

## Local rules and jurisdiction

**Court(s) / Tribunal(s):** [from CLAUDE.md or additional courts/tribunals for this practice area]
**Jurisdiction-specific differences to flag:**
- [E&W vs Scotland vs NI differences that affect this practice area]

**Practice-area-specific rules, forms, and pointers:**
- [pointer 1 — e.g., "ET1 submitted via MyHMCTS; form guidance at [link]"]
- [pointer 2]
```

Fill every section from the supervisor's answers. Leave a section empty only if the supervisor said so — do not invent content.

Then tell the supervisor:

> Your guide is at `~/.claude/plugins/config/uk-legal-plugins/legal-clinic-uk/guides/<practice-area>.md`. Every student who uses the clinic plugin for [practice area] will have skills that follow it. Edit the file directly to change anything, or re-run `/legal-clinic-uk:build-guide` to revise a section. You can have multiple guides — one per practice area.

### Step 9: Offer a test run

> Want to see how the pedagogy posture changes the experience? I'll run `/legal-clinic-uk:draft` with a sample scenario under [posture] — you'll see what the student sees.

If the supervisor says yes, simulate the drafting skill reading the guide they just wrote and producing output under the configured posture.

## Output

After writing, show a brief confirmation:

> **Guide written.** `[practice-area]` is now configured:
>
> - Intake: [N] custom questions, [N] red flags, [N] refer-out criteria
> - Pedagogy: [posture default], with overrides for [list if any]
> - Review gates: [summary of what routes to supervisor vs. student]
> - Cross-plugin: [N] skills wired in
>
> Students will see these changes the next time they run a clinic command for this practice area.

## What this skill does NOT do

- **Configure the plugin globally.** The guide is per-practice-area. For plugin-wide config, that's `/legal-clinic-uk:cold-start-interview`.
- **Author student work product.** This is supervisor-facing configuration, not a draft for a client.
- **Override the supervision style from cold-start.** The supervision model is set at setup. Review gates in the guide refine that model; they don't replace it.
- **Reduce SRA/BSB supervision obligations.** The non-negotiable review gates (substantive client letters, court/tribunal filings, court-facing status) cannot be overridden by any posture or guide setting.
