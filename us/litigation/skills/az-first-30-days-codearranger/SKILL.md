---
name: az-first-30-days-codearranger
title: Arizona — First 30 Days After Service
description: 'Use when an Arizona defendant has just been served with a civil complaint or summons. Triggers: "I got served Arizona", "answer an Arizona complaint", "I was sued in Arizona", "served with a summons in Arizona", "20 days to answer Arizona", "affirmative defenses Arizona Rule 8(d)", "motion to dismiss Arizona Rule 12(b)(6)", "set aside default Arizona Rule 55", "entry of default Arizona", "counterclaim Arizona Rule 13", "jury demand Arizona Rule 38", "compulsory arbitration Arizona", "first 30 days after being sued in Arizona". Covers Ariz. R. Civ. P. 12(a) answer window (20 days in-state / 30 days out-of-state), Rule 8 answer with admissions/denials, Rule 8(d) affirmative defenses (WAIVER RISK if omitted), Rule 12(b) motion-to-dismiss grounds, Rule 55 default entry / set-aside, Rule 13 counterclaims, Rule 38 jury demand, Rules 72-77 compulsory arbitration program keyed to county dollar threshold.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arizona — First 30 Days After Service

> **NOT LEGAL ADVICE.** Time is short. This skill helps a defendant
> sketch a response and surface the most important deadlines, but
> consult a licensed Arizona attorney about substantive defenses when
> possible.

Use this skill when the defendant has **just been served** with a civil
summons and complaint in an Arizona **Superior Court** (or a limited-
jurisdiction Justice Court — see `az-justice-courts`). It frames the
response window: the time in which the defendant must answer, move to
dismiss, or risk default.

## The clock — Ariz. R. Civ. P. 12(a)

| Event | Deadline | Authority |
|---|---|---|
| Answer — served **within Arizona** | **20 days** after service | Ariz. R. Civ. P. 12(a)(1)(A)(i) |
| Answer — served **outside Arizona** | **30 days** after completion of service | Ariz. R. Civ. P. 4.2(m) |
| Answer to a counterclaim / cross-claim | **20 days** after service | Ariz. R. Civ. P. 12(a)(1)(B) |
| Responsive pleading after the court denies a Rule 12 motion | **10 days** after notice of the court's action | Ariz. R. Civ. P. 12(a)(2)(A) |

The **20-day / 30-day** split is the stable, statutory-style count.
Still confirm against the current Rule 12(a) (it sets several sub-
deadlines by service mode and posture) and compute the actual due date
with `az-deadlines` (Rule 6 time computation + the mail / service add-
ons). Verify all subsection numbers against the corpus before relying on
them.

> ⚠ **Default risk.** If the defendant neither answers nor moves within
> the window, the plaintiff may apply for **entry of default** under
> Rule 55(a) and then seek a **default judgment** under Rule 55(b).
> Setting a default aside later is hard — see the Rule 55 section below
> and `az-post-judgment`.

## Playbook

### Days 0-3 — read the complaint, check the summons

- **Read every numbered paragraph.** Note who is suing, on what claims,
  for what relief, and what contracts / accounts / events are alleged.
- **Note the court, county, and case number** — these go on every filing
  (`az-statewide-format` caption).
- **Check service** and the summons. Defective service / lack of personal
  jurisdiction is a defense — preserve it (Rule 12(b)(2), (4), (5); Rule
  12(h) waiver).
- **Note the court level**: Superior Court (general civil) vs. Justice
  Court (limited jurisdiction; confirm the cap via `az-justice-courts`).

### Days 3-10 — choose the response strategy

Three principal paths: (1) **Answer** under Rule 8 — admit, deny, or
plead lack of knowledge per paragraph (Rule 8(c)), state affirmative
defenses (Rule 8(d)), assert counterclaims (Rule 13); (2) **Motion to
Dismiss** under Rule 12(b), in lieu of an answer (grounds below); (3)
**Motion for a More Definite Statement** (Rule 12(e)) — disfavored.

> ⚠ **Plead affirmative defenses — Rule 8(d).** Arizona requires a party
> to **affirmatively state** any avoidance or affirmative defense in the
> responsive pleading; defenses omitted from the answer can be **waived**.
> This includes statute of limitations, release, payment, accord and
> satisfaction, statute of frauds, res judicata, and lack of standing /
> chain of title. **Plead all that may apply.** Verify Rule 8(d) and the
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
> reasonable opportunity to present Rule 56 material (Rule 12(d) — verify
> the subsection). Do not attach evidence to a 12(b)(6) motion unless you
> intend conversion; if a fact dispute matters, move under Rule 56. The
> Arizona summary-judgment standard is *Orme School v. Reeves*, 166 Ariz.
> 301 (1990) — **verify the citation and holding**. SJ standards and
> timing live in `az-draft-motion`; this skill flags them at a pointer
> level.

> **Preserve the threatened defenses — Rule 12(h).** Lack of personal
> jurisdiction, improper venue, insufficient process, and insufficient
> service can be **waived** if not raised in the first Rule 12 motion or
> the answer. Raise them at the first opportunity; verify Rule 12(h).

> ⚠ **COMPULSORY ARBITRATION — Rules 72-77.** Arizona Superior Courts run
> a **mandatory (compulsory) arbitration program**. A civil case in which
> the amount in controversy does **not exceed the jurisdictional limit
> set by the county's Superior Court local rule** is **automatically
> assigned to a single arbitrator** and removed from the trial calendar
> until arbitration concludes — expect this for ordinary consumer-debt
> and small civil cases. Each party files a **certificate of compulsory
> arbitration** (or a controverting certificate) early in the case
> stating whether the case is subject to arbitration. An arbitration
> **award** may be **appealed for a trial de novo**, but an appealing
> party who fails to better its position can face cost / fee
> consequences. **Confirm your county's dollar threshold** and the
> certificate requirement via `az-law-references` and the local rule.
> This is a defining feature of Arizona civil practice — flag it for the
> client at the outset.

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
                   (Rule 8(d) — omission may waive)
   1. Plaintiff's claims are barred by the statute of limitations.
   2. Plaintiff lacks standing / chain of title to the alleged debt.
   3. [Release / payment / accord & satisfaction / statute of frauds /
      res judicata / failure to state a claim / etc.]

                            COUNTERCLAIM
   [If asserting one, plead it complaint-style with numbered factual
   allegations and named counts — Rule 13.]

                       DEMAND FOR JURY TRIAL
   Defendant demands a trial by jury on all issues so triable.
```

#### Affirmative-defense catalog — Rule 8(d)

Plead **all** that may apply. Common Arizona defenses:

- Statute of limitations (very common — verify the period against
  `az-statutes-debt` / the relevant subject bundle)
- Payment / accord and satisfaction / release
- Discharge in bankruptcy
- Statute of frauds
- Estoppel / waiver / laches
- Failure of consideration / fraud / illegality
- Res judicata / collateral estoppel (prior judgment)
- Lack of standing / chain of title (debt-buyer cases — see
  `az-consumer-debt`)
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

### Jury trial — Rule 38

**Arizona does not use the FRCP demand-or-waive model.** Under Rule
38(a), the right to a jury trial on any issue triable of right by a jury
is **preserved inviolate, and a party need not file a written demand or
take any other action to preserve it.** A jury right is **waived only by
an affirmative written stipulation signed by all parties who appear at
trial** (or an approved oral stipulation in open court), filed **no later
than 30 days before the trial** is scheduled to begin (Rule 38(b)).
Including a jury demand in the answer (above) is permissible belt-and-
suspenders practice but is not required to preserve the right; confirm
the current text of Rule 38.

### Entry of default and setting it aside — Rule 55

- **Rule 55(a) — application for entry of default.** The plaintiff files
  and serves an application; the default does **not** become effective
  immediately — the defendant has a short **cure window** (verify the
  current number of business days) to plead or otherwise defend. If the
  defendant pleads within it, default does not enter. **Treat an
  application for default as a hard signal to file the answer at once.**
- **Rule 55(b)** — default judgment entered after default is effective.
- **Rule 55(c)** — setting aside an entry of default for **good cause**.
- **Setting aside a default *judgment*** is governed by **Rule 60(b)/(c)**
  and is a demanding standard — not a fallback for missing the answer
  window. Vacatur is developed in `az-post-judgment`. Verify the Rule 55
  cure-window count and the Rule 60 grounds against the corpus.

## Filing the answer / motion

- **File** with the clerk of the Superior Court (or Justice Court) in the
  caption (confirm the e-filing platform — AZTurboCourt / county portal
  where mandated; otherwise paper).
- **Serve** all parties under Rule 5 with a certificate of service.
- **Sign** under Rule 11 (certifies the pleading is well-grounded;
  sanctions attach to violations).
- **File the certificate of compulsory arbitration** (Rules 72-77) where
  the county requires it.

## Composition

- Format / caption: `az-statewide-format`
- Drafting + the *Orme School* summary-judgment standard:
  `az-draft-motion`, `az-draft-declaration`
- Filing court: `az-maricopa`, `az-pima`, `az-superior-courts`,
  `az-justice-courts`
- Deadline arithmetic: `az-deadlines`; default vacatur: `az-post-judgment`
- Matter-specific defenses: `az-consumer-debt`, `az-family-law`,
  `az-landlord-tenant`, `az-personal-injury`, `az-employment`,
  `az-commercial-disputes`

## References

- `references/answer-template.md` — full Rule 8 answer scaffold with the
  Rule 8(d) affirmative-defenses section
- `references/motion-to-dismiss-grounds.md` — Rule 12(b)(1)-(7)
  annotated, with the 12(b)(6) → Rule 56 conversion note
- `references/affirmative-defense-catalog.md` — annotated, keyed to the
  Rule 8(d) statement requirement
- `references/default-and-set-aside.md` — Rule 55 entry / cure window /
  Rule 55(c) good cause + Rule 60(b) default-judgment vacatur
- `references/compulsory-arbitration.md` — Rules 72-77 track, county
  thresholds, certificate of compulsory arbitration, appeal for a trial
  de novo
