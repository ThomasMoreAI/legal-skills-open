---
name: id-first-30-days-codearranger
title: Idaho — First 30 Days After Service
description: 'Use when an Idaho defendant has just been served with a civil complaint or summons. Triggers: "I got served Idaho", "answer an Idaho complaint", "I was sued in Idaho", "served with a summons in Idaho", "21 days to answer Idaho", "Idaho answer deadline", "affirmative defenses Idaho Rule 8(c)", "motion to dismiss Idaho Rule 12(b)", "set aside default Idaho Rule 55", "entry of default Idaho", "counterclaim Idaho Rule 13", "first 30 days after being sued in Idaho". Covers the I.R.C.P. 12(a)(1)(A) answer window (21 days), the Rule 8 answer with admissions/denials, Rule 8(c) affirmative defenses (WAIVER RISK if omitted), Rule 12(b) motion-to-dismiss grounds, Rule 13 counterclaims, and Rule 55 default entry / set-aside.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Affirmative Defense Catalog
  path: references/affirmative-defense-catalog.md
- title: Answer Template
  path: references/answer-template.md
- title: Default And Set Aside
  path: references/default-and-set-aside.md
- title: Motion To Dismiss Grounds
  path: references/motion-to-dismiss-grounds.md
---

# Idaho — First 30 Days After Service

> **NOT LEGAL ADVICE.** Time is short. This skill helps a defendant
> sketch a response and surface the most important deadlines, but consult
> a licensed Idaho attorney about substantive defenses when possible.

Use this skill when the defendant has **just been served** with a civil
summons and complaint in **District Court** or the **Magistrate
Division**. It frames the response window: the time in which the
defendant must answer, move to dismiss, or risk default. Pull verbatim
rule text from `../id-law-references/references/court-rules/`.

## The clock — I.R.C.P. 12(a)(1)(A)

> **★ 21 days.** A defendant served with a summons and complaint must
> serve an **answer within 21 days after service** (**I.R.C.P.
> 12(a)(1)(A)**).

Confirm against the current Rule 12(a) (it sets sub-deadlines by service
mode and posture) and compute the actual due date with `id-deadlines`
(I.R.C.P. 2.2 time computation + the 3-day mail add-on where the period
runs from service by mail). A timely pre-answer Rule 12(b) motion alters
the time to file a responsive pleading.

> ⚠ **Default risk.** If the defendant neither answers nor moves within
> the 21-day window, the plaintiff may apply for **entry of default**
> under Rule 55(a) and then seek a **default judgment** under Rule 55(b).
> Setting a default aside later is hard — see the Rule 55 section below
> and `id-post-judgment`.

## Playbook

### Days 0-3 — read the complaint, check the summons

- **Read every numbered paragraph.** Note who is suing, on what claims,
  for what relief, and what contracts / accounts / events are alleged.
- **Note the court, county, and case number** — these go on every filing
  (`id-statewide-format` caption).
- **Confirm the court level.** Civil claims of **$5,000 or less** are
  heard in the **Magistrate Division** (Idaho Code § 1-2208); claims
  **over $5,000** go to the **District Court**. Small Claims handles
  matters up to $5,000 (Idaho Code § 1-2301). The Magistrate Division
  also hears eviction, probate, and all family-law matters.
- **Check service** and the summons. Defective service / lack of personal
  jurisdiction is a defense — preserve it (Rule 12(b)(2), (4), (5)).
  Confirm the plaintiff served the summons within the **182-day** filing
  window (I.R.C.P. 4(b)(2)).

### Days 3-10 — choose the response strategy

Three principal paths: (1) **Answer** under Rule 8 — admit, deny, or
plead lack of knowledge per paragraph (Rule 8(b)), state affirmative
defenses (Rule 8(c)), assert counterclaims (Rule 13); (2) **Motion to
Dismiss** under Rule 12(b), in lieu of an answer (grounds below); (3)
**Motion for a More Definite Statement** (Rule 12(e)) — disfavored.

> ⚠ **Plead affirmative defenses — Rule 8(c).** Idaho requires a party to
> **affirmatively state** any avoidance or affirmative defense in the
> responsive pleading; defenses omitted from the answer can be **waived**.
> This includes statute of limitations, release, payment, accord and
> satisfaction, statute of frauds, res judicata, and lack of standing /
> chain of title. **Plead all that may apply.** Verify Rule 8(c) and the
> waiver consequences before filing.

### Motion to dismiss — Rule 12(b)

The Rule 12(b) grounds, raised by motion before or with the answer:

| Subrule | Ground |
|---|---|
| **(b)(1)** | lack of subject-matter jurisdiction |
| **(b)(2)** | lack of personal jurisdiction |
| **(b)(3)** | improper venue |
| **(b)(4)** | insufficient process |
| **(b)(5)** | insufficient service of process |
| **(b)(6)** | **failure to state a claim** upon which relief can be granted |
| **(b)(7)** | failure to join a party under Rule 19 |

> **Rule 12(b)(6) — tested on the pleadings; conversion to Rule 56.** A
> 12(b)(6) motion tests the legal sufficiency of the complaint on the
> **pleadings alone**, accepting well-pleaded allegations as true. **If
> matters outside the pleadings are presented and not excluded, the
> motion is treated as one for summary judgment under Rule 56** with a
> reasonable opportunity to present Rule 56 material. Do not attach
> evidence to a 12(b)(6) motion unless you intend conversion; if a fact
> dispute matters, move under Rule 56. The summary-judgment standard and
> its 28-day / 14-day briefing timeline live in `id-draft-motion` and
> `id-deadlines`.

> **Preserve the threatened defenses.** Lack of personal jurisdiction,
> improper venue, insufficient process, and insufficient service can be
> **waived** if not raised in the first Rule 12 motion or the answer.
> Raise them at the first opportunity; verify the waiver rule in the
> corpus.

### Days 10-30 — draft the answer (or the motion)

#### Answer structure (Rule 8)

```
                              ANSWER,
                AFFIRMATIVE DEFENSES, AND COUNTERCLAIM

   Defendant [Name] answers Plaintiff's Complaint as follows:

                              ANSWER
   1. Defendant admits the allegations in paragraph 1.
   2. Defendant denies the allegations in paragraph 2.
   3. Defendant lacks knowledge or information sufficient to form a
      belief about the truth of paragraph 3, which has the effect of a
      denial.
   [...]

                       AFFIRMATIVE DEFENSES
                   (Rule 8(c) — omission may waive)
   1. Plaintiff's claims are barred by the statute of limitations.
   2. Plaintiff lacks standing / chain of title to the alleged debt.
   3. [Release / payment / accord & satisfaction / statute of frauds /
      res judicata / failure to state a claim / etc.]

                            COUNTERCLAIM
   [If asserting one, plead it complaint-style with numbered factual
   allegations and named counts — Rule 13.]
```

#### Affirmative-defense catalog — Rule 8(c)

Plead **all** that may apply. Common Idaho defenses:

- Statute of limitations (very common — verify the period against
  `id-deadlines` / the relevant subject bundle: written contract 5 years
  (Idaho Code § 5-216); oral / open account 4 years (§ 5-217))
- Payment / accord and satisfaction / release
- Discharge in bankruptcy
- Statute of frauds
- Estoppel / waiver / laches
- Failure of consideration / fraud / illegality
- Res judicata / collateral estoppel (prior judgment)
- Lack of standing / chain of title (debt-buyer cases — see
  `id-consumer-debt`)
- Failure to state a claim (Rule 12(b)(6))

### Counterclaims and cross-claims — Rule 13

- **Rule 13(a) — compulsory counterclaim.** A pleader must state any
  counterclaim against the opposing party arising out of the
  **transaction or occurrence** that is the subject of the opposing
  party's claim, or the claim may be **barred** in later litigation.
  Plead all known related counterclaims with the answer.
- **Rule 13(b)** — permissive counterclaim (unrelated claims); **cross-
  claims** against co-parties are also governed by Rule 13. Verify the
  current text and scope of the bar.

### Entry of default and setting it aside — Rule 55

- **Rule 55(a) — entry of default.** When a defendant fails to plead or
  otherwise defend within the 21-day window, the plaintiff may apply for
  entry of default. **Treat any application for default as a hard signal
  to file the answer at once.**
- **Rule 55(b)** — default judgment entered after default.
- **Rule 55(c)** — setting aside an entry of default for **good cause**.
- **Setting aside a default *judgment*** is governed by **Rule 60(b)** and
  is a demanding standard — not a fallback for missing the answer window.
  Vacatur is developed in `id-post-judgment`.

## Filing the answer / motion

- **File** with the clerk of the District Court or Magistrate Division in
  the caption (e-file through **iCourt / Odyssey File & Serve
  (I.R.E.F.S.)** — mandatory for attorneys (Rule 4(a)), optional for
  self-represented filers (Rule 4(b))).
- **Serve** all parties under I.R.C.P. 5 with a certificate of service.
- **Sign** under Rule 11 (certifies the pleading is well-grounded;
  sanctions attach to violations).

## Composition

- Format / caption: `id-statewide-format`
- Drafting + the summary-judgment standard: `id-draft-motion`,
  `id-draft-declaration`
- Filing court: `id-ada`, `id-bonneville`, `id-county-courts`
- Deadline arithmetic: `id-deadlines`; default vacatur:
  `id-post-judgment`
- Matter-specific defenses: `id-consumer-debt`, `id-family-law`
- Noticing any motion for hearing: `id-schedule-hearing`, `id-hearings`

## References

- `references/answer-template.md` — full Rule 8 answer scaffold with the
  Rule 8(c) affirmative-defenses section
- `references/motion-to-dismiss-grounds.md` — Rule 12(b)(1)-(7)
  annotated, with the 12(b)(6) → Rule 56 conversion note
- `references/affirmative-defense-catalog.md` — annotated, keyed to the
  Rule 8(c) statement requirement
- `references/default-and-set-aside.md` — Rule 55 entry / good cause +
  Rule 60(b) default-judgment vacatur
