---
name: oh-first-30-days-codearranger
title: Ohio — First 30 Days After Service
description: Use immediately after Ohio service to triage answer + pre-answer motion options. Triggers include 'Ohio Civ. R. 12 answer', 'Ohio 28 days to answer', 'Ohio Civ. R. 12(B)(6) motion to dismiss', 'Ohio Civ. R. 12(C) judgment on the pleadings', 'Ohio counterclaim', 'Ohio default judgment Civ. R. 55'. Covers the 28-day answer clock under Civ. R. 12(A)(1), the eight Civ. R. 12(B) grounds for pre-answer motion to dismiss, the seven-day post-ruling answer rule, Civ. R. 13 counterclaims, and the *Jarboe v. Landmark* / Twombly-adjacent Ohio pleading standard.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Ohio — First 30 Days After Service

> **NOT LEGAL ADVICE.** Missing the 28-day answer clock can
> result in default judgment under Civ. R. 55. Calendar the
> deadline immediately on service.

## The 28-day answer clock

Ohio Civ. R. 12(A)(1) provides **28 days from service** to
file:

- An answer
- An answer with counterclaim
- A pre-answer Civ. R. 12(B) motion to dismiss

The clock differs from federal practice (FRCP 12(a)'s 21
days) and from many other states. Always verify the
service date on the return receipt or sheriff's return.

## Pre-answer Civ. R. 12(B) motions

Ohio Civ. R. 12(B) provides seven grounds for a pre-answer
motion to dismiss (almost identical to FRCP 12(b)):

1. **(1) Lack of subject-matter jurisdiction**
2. **(2) Lack of personal jurisdiction**
3. **(3) Improper venue**
4. **(4) Insufficient process**
5. **(5) Insufficient service of process**
6. **(6) Failure to state a claim upon which relief can be
   granted**
7. **(7) Failure to join a party under Civ. R. 19**

### Civ. R. 12(B)(6) standard

Ohio applies the *Jarboe v. Landmark* / *Twombly* / *Iqbal*
plausibility standard adopted in **State ex rel. Hanson v.
Guernsey County Board of Commissioners**, 65 Ohio St.3d
545 (1992) and refined in subsequent appellate decisions.
A complaint must allege facts that, taken as true,
plausibly entitle the plaintiff to relief.

### Civ. R. 12(B)(6) consolidation rule

Unlike NY's CPLR 3211(e) consolidation rule, **Ohio does
not require all 12(B) defenses to be raised in a single
motion**. However, Civ. R. 12(H)(1) provides that personal-
jurisdiction, venue, process, and service defenses are
waived if not raised in the first responsive pleading
(answer or first 12(B) motion).

## Post-12(B)-ruling timeline

- **If 12(B) motion denied** — Civ. R. 12(A)(2)(a) gives
  **14 days** after the ruling to file the answer
- **If 12(B) motion granted** in part — same 14-day clock
  runs from the partial denial

## Answer content (Civ. R. 8)

Required elements:

- **Admissions / denials** for each numbered paragraph of
  the complaint
- **Affirmative defenses** under Civ. R. 8(C) — at least 19
  enumerated (accord and satisfaction, arbitration and
  award, assumption of risk, contributory negligence,
  discharge in bankruptcy, duress, estoppel, failure of
  consideration, fraud, illegality, injury by fellow
  servant, laches, license, payment, release, res judicata,
  statute of frauds, statute of limitations, waiver)

A defense not raised in the answer is **waived** under Civ.
R. 12(H), except for failure to state a claim and
subject-matter jurisdiction which can be raised at any
time.

## Counterclaims — Civ. R. 13

- **Compulsory counterclaim** (Civ. R. 13(A)) — claim
  arising out of the same transaction or occurrence as the
  plaintiff's claim; MUST be pled or it is lost
- **Permissive counterclaim** (Civ. R. 13(B)) — any other
  claim against the plaintiff; may be raised

## Default judgment — Civ. R. 55

- **Civ. R. 55(A)** — default entered by clerk after 28-day
  answer clock expires
- **Civ. R. 55(C)** — judgment entered by the court after
  application + hearing on damages
- **Civ. R. 55(B)** — relief from default available under
  Civ. R. 60(B) if the defendant shows excusable neglect +
  meritorious defense

## Composition with other oh- skills

- `oh-deadlines` — Civ. R. 6 time computation for the 28-
  and 14-day clocks
- `oh-draft-motion` — Civ. R. 12(B)(6) motion scaffolder
- `oh-draft-declaration` — Civ. R. 56 affidavit support
- `oh-discovery` — pairs with the answer for early
  discovery requests
- `oh-consumer-debt` — debt-buyer pleading deficiencies
- `oh-pro-se` — pro-se signature + framing
