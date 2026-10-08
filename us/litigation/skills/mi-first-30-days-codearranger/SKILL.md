---
name: mi-first-30-days-codearranger
title: Michigan — First 30 Days After Service
description: Use when a Michigan defendant is served with a civil complaint. Triggers include "I got served Michigan", "answer Michigan complaint", "I was sued", "21 days to answer Michigan", "MCR 2.108 answer deadline", "motion for summary disposition MCR 2.116", "set aside default Michigan MCR 2.603", "affirmative defenses Michigan", "counterclaim Michigan", "jury demand Michigan". Covers MCR 2.108 answer window (21 days personal / 28 days mail/out-of-state); MCR 2.111 answer form with MCR 2.111(F) affirmative- defenses-separately-or-waived rule; summary disposition (MCR 2.116); MCR 2.603 default and set-aside standard; MCR 2.203 joinder and compulsory- claim rule; MCR 2.508 jury demand timing.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Michigan — First 30 Days After Service

> **NOT LEGAL ADVICE.** Time is short. This skill helps a defendant
> sketch a response and surface the most important deadlines, but
> consult a licensed Michigan attorney about substantive defenses when
> possible.

Use this skill when the defendant has **just been served** with a
civil summons and complaint in a Michigan **circuit court** or
**district court**. It frames the response window — the time in which
the defendant must answer, move for summary disposition, or risk
default.

## The clock — MCR 2.108

| Event | Deadline | Authority |
|---|---|---|
| Answer — personally served within Michigan | **21 days** after service | MCR 2.108(A)(1) |
| Answer — served by mail, or served outside Michigan | **28 days** after service | MCR 2.108(A) |
| Answer to a counterclaim / cross-claim | **21 days** after service | MCR 2.108(A) |
| Responsive pleading after the court rules on a motion | per the order; default **21 days** after notice if no time set | MCR 2.108(C) |

These are the **stable** statutory-style day counts; still confirm
against the current MCR 2.108 (the rule sets several sub-deadlines by
service mode), and compute the actual due date with `mi-deadlines`
(MCR 1.108 time computation + MCR 2.107(C)(3) mail add-on).

> ⚠ **Default risk.** If the defendant neither answers nor moves
> within the window, the plaintiff may take the defendant's **default**
> under MCR 2.603 and then seek a **default judgment**. Setting a
> default aside later is hard — see the MCR 2.603 standard below and
> `mi-post-judgment`.

## Day-by-day playbook

### Days 0-3 — read the complaint, check the summons

- **Read every numbered paragraph.** Note who is suing, on what
  claims, for what relief, and what contracts / accounts / events are
  alleged.
- **Note the court, county, and case number** — these go on every
  filing (`mi-statewide-format` caption).
- **Check the summons expiration** (MCR 2.102(D)) and **check service**
  under MCR 2.105. Defective service is a defense — preserve it (the
  MCR 2.116(C)(1)-(C)(3) grounds below).
- **Note the court level**: circuit court (general civil, over
  $25,000) vs. district court (up to $25,000; small claims division).

### Days 3-10 — choose the response strategy

Three principal paths:

1. **Answer** — admit, deny, or plead lack of knowledge for each
   numbered paragraph (MCR 2.111(C)-(D)); **state affirmative defenses
   in a separate, clearly designated section** (MCR 2.111(F) — see the
   trap below); assert any counterclaims (MCR 2.203).
2. **Motion for Summary Disposition** under MCR 2.116 — may be filed
   in lieu of or together with an answer; see the grounds below.
3. **Motion for More Definite Statement** (MCR 2.115(A)) — when the
   pleading is too vague to answer. Disfavored; rarely granted.

> ⚠ **MICHIGAN AFFIRMATIVE-DEFENSE TRAP — MCR 2.111(F).** In Michigan,
> affirmative defenses must be **stated in a separate, clearly labeled
> section of a responsive pleading** (and a defense raised by a
> responsive pleading is **deemed waived if not stated**). Burying a
> defense in the body of denials, or omitting it entirely, **waives**
> it. This includes statute of limitations, release, payment, statute
> of frauds, lack of standing / chain of title, and the other
> MCR 2.111(F)(3) defenses. **Always plead affirmative defenses under
> their own heading**, even where they overlap with summary-disposition
> grounds. Verify the current text of MCR 2.111(F) before filing.

### Summary disposition — MCR 2.116

Michigan does not use a "motion to dismiss" / "motion for summary
judgment" split. **Both** are folded into one motion for **summary
disposition** under MCR 2.116(C), with the ground identified by
subrule:

| Subrule | Ground |
|---|---|
| **(C)(1)** | lack of subject-matter jurisdiction |
| **(C)(2)** | lack of personal jurisdiction |
| **(C)(3)** | insufficiency of process / service of process |
| **(C)(4)** | claim within another tribunal's exclusive jurisdiction (verify) |
| **(C)(5)** | party lacks legal capacity to sue |
| **(C)(6)** | another action pending between the same parties on the same claim |
| **(C)(7)** | claim barred — **statute of limitations, release, prior judgment / res judicata, immunity, payment, statute of frauds, infancy/disability**, etc. |
| **(C)(8)** | **failure to state a claim** on which relief can be granted — tested on the **pleadings alone** |
| **(C)(9)** | failure to state a valid defense |
| **(C)(10)** | **no genuine issue of material fact** — tested on **documentary evidence**, the rough analog to federal summary judgment |

> **(C)(8) vs. (C)(10) — different records.** A **(C)(8)** motion tests
> the legal sufficiency of the complaint on the **pleadings alone**;
> the court accepts the well-pleaded allegations as true and may not
> consider outside evidence. A **(C)(10)** motion is decided on
> **affidavits, depositions, admissions, and other documentary
> evidence**, viewed in the light most favorable to the non-moving
> party. The governing standard is set out in *Maiden v Rozwood*, 461
> Mich 109 (1999) — **verify the citation and holding** before relying
> on it. Do not attach evidence to a (C)(8) motion; if a fact dispute
> matters, move under (C)(10). The standards and timing are developed
> in `mi-draft-motion`; this skill flags them at a pointer level.

> **Preserve the threatened defenses.** Lack of personal jurisdiction,
> improper process, and improper service ((C)(1)-(C)(3) grounds) can be
> **waived** if not raised at the first opportunity — raise them by
> motion under MCR 2.116 **or** plead them, consistent with
> MCR 2.116(D). Verify the current waiver rule.

### Days 10-28 — draft the answer (or the motion)

#### Answer structure (MCR 2.111)

```
                              ANSWER,
                AFFIRMATIVE DEFENSES, AND COUNTERCLAIM

   Defendant [Name] answers Plaintiff's Complaint as follows:

                              ANSWER
   1. Defendant admits the allegations in paragraph 1.
   2. Defendant denies the allegations in paragraph 2.
   3. Defendant lacks knowledge or information sufficient to form a
      belief as to paragraph 3 and leaves Plaintiff to its proofs.
   [...]

                       AFFIRMATIVE DEFENSES
            (separate section — MCR 2.111(F); omission waives)
   1. Plaintiff's claims are barred by the statute of limitations.
   2. Plaintiff lacks standing / chain of title to the alleged debt.
   3. [Release / payment / accord & satisfaction / statute of frauds /
      failure to state a claim / etc.]

                            COUNTERCLAIM
   [If asserting one, plead it complaint-style with numbered factual
   allegations and named counts — MCR 2.203.]

                       DEMAND FOR JURY TRIAL
   Defendant demands a trial by jury on all issues so triable.
```

#### Affirmative-defense catalog — MCR 2.111(F)

Plead **all** that may apply, each in the **separate** defenses
section. Common Michigan defenses:

- Statute of limitations (very common — verify the period against
  `mi-statutes-debt` / the relevant subject bundle)
- Payment / accord and satisfaction / release
- Discharge in bankruptcy
- Statute of frauds
- Estoppel / waiver / laches
- Failure of consideration / fraud / illegality
- Res judicata / collateral estoppel (prior judgment)
- Lack of standing / chain of title (debt-buyer cases — see
  `mi-consumer-debt`)
- Failure to state a claim (MCR 2.116(C)(8))
- Governmental immunity (claims against public actors)

### Counterclaims, cross-claims, joinder — MCR 2.203

- **MCR 2.203(A) — compulsory joinder of claims.** A pleader must join
  every claim it has against the opposing party that arises out of the
  **transaction or occurrence** that is the subject of the action, or
  the claim may be **barred**. Plead all known related counterclaims
  with the answer.
- **MCR 2.203(B)** — permissive joinder of unrelated claims.
- **Cross-claims** against co-parties are also governed by MCR 2.203.
- Verify the current MCR 2.203 text and the scope of the bar.

### Demand for jury — MCR 2.508

A party who wants a jury must **file and serve a written demand**
within the time fixed by MCR 2.508(B) (tied to the close of pleadings)
and pay the jury fee. **Failure to demand within the window waives the
jury right.** Include the demand in the answer (as above) or file it
separately within the rule's window; confirm the current timing in
MCR 2.508.

### Setting aside a default — MCR 2.603

If a default has already entered, MCR 2.603(D) allows it to be set
aside only on a showing of **good cause** *and* a **verified statement
of facts showing a meritorious defense** (except for a defect in personal
jurisdiction). The motion must be timely. This is a demanding standard
— do not rely on it as a fallback for missing the answer window.
Default-judgment vacatur is developed in `mi-post-judgment`.

## Filing the answer / motion

- **File** with the clerk of the circuit or district court named in
  the caption (confirm the court's e-filing platform — MiFILE /
  TrueFiling where mandated; otherwise paper).
- **Serve** all parties under MCR 2.107 and include proof of service.
- **Sign** under MCR 1.109(E) (signature certifies the pleading is
  well-grounded; sanctions attach to violations).

## Composition

- Format / caption: `mi-statewide-format`
- Drafting + the *Maiden v Rozwood* summary-disposition standard:
  `mi-draft-motion`, `mi-draft-declaration`
- Filing court: `mi-wayne`, `mi-oakland`, `mi-36th-district`,
  `mi-circuit-courts`, `mi-district-courts`
- Deadline arithmetic: `mi-deadlines`; default vacatur: `mi-post-judgment`
- Matter-specific defenses: `mi-consumer-debt`, `mi-family-law`,
  `mi-landlord-tenant`, `mi-personal-injury`, `mi-employment`

## References

- `references/answer-template.md` — full MCR 2.111 answer scaffold with
  the separate affirmative-defenses section
- `references/summary-disposition-grounds.md` — MCR 2.116(C)(1)-(10)
  annotated, with the (C)(8) vs. (C)(10) record distinction
- `references/affirmative-defense-catalog.md` — annotated, keyed to the
  MCR 2.111(F) waiver rule
- `references/set-aside-default.md` — MCR 2.603 good cause + verified
  statement of facts showing a meritorious defense
- `references/service-defects.md` — MCR 2.105 / MCR 2.116(C)(1)-(3)
  analysis
