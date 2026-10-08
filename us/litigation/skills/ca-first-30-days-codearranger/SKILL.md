---
name: ca-first-30-days-codearranger
title: California — First 30 Days After Service
description: 'Use when a California defendant has just been served with a summons and complaint. Triggers include "I was just served", "I got served with a summons", "how much time to respond", "deadline to answer a California complaint", "30 days to answer", "first steps after being sued", "should I file a demurrer", "motion to strike California", "anti-SLAPP motion", "affirmative defenses", "cross-complaint", "default California". Covers the from-service-through-response window: CCP § 412.20(a)(3) 30-day response (plus 10 days for mail); response options (Answer, Demurrer under § 430.10, Motion to Strike under § 435, Anti-SLAPP under § 425.16, Motion to Quash under § 418.10, Cross-Complaint under §§ 426.10–426.50); mandatory meet-and-confer; affirmative defenses; default procedures under § 585.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# California — First 30 Days After Service

When a defendant in a California civil case is served with a
summons and complaint, **Code Civ. Proc., § 412.20(a)(3)**
gives them **30 calendar days** from the date of service to
file a response. This skill covers the matter-neutral workflow
for that window.

> **NOT LEGAL ADVICE.** This is a procedural framework, not a
> case strategy. The strategic decisions (defend on the merits?
> attack by demurrer? negotiate? settle?) depend on the specific
> facts and law.

## The 30-day clock

The 30 days starts on **the date of service** (the day of actual
delivery for personal service — Code Civ. Proc., § 413.10 et seq.)
and runs 30 calendar days.

**Service by mail (NORF method)**: if the defendant was served by
mail under Code Civ. Proc., § 415.30(c) with a "Notice and
Acknowledgment of Receipt" form, the 30-day period does not start
until the defendant signs and returns the acknowledgment. If the
defendant never signs, personal service must be accomplished.

**Extension by mail**: if any subsequent paper is served by mail,
add 5 calendar days for service within California (Code Civ.
Proc., § 1013(a)), 10 days for out-of-state, and 20 days for
outside the U.S.

**Extension for electronic service**: add 2 court days (Code Civ.
Proc., § 1010.6(a)(3)(B)).

If the 30th day falls on a weekend or court holiday, the deadline
extends to the next court day (Code Civ. Proc., § 12).

Compute the precise deadline using `ca-deadlines` and
`scripts/case-calendar.py`.

## Response options

The defendant must choose one or more responses within 30 days:

| Response | Authority | Effect |
|---|---|---|
| Answer | Code Civ. Proc., § 431.30 | Joins issue on the merits |
| General Demurrer | §§ 430.10(e), (f) | Attacks legal sufficiency — tolls answer |
| Motion to Strike | § 435 | Attacks irrelevant/improper matter — tolls answer |
| Motion to Quash Service | § 418.10 | Attacks service; tolls answer until ruling |
| Anti-SLAPP Motion | § 425.16 | Special motion for protected activity; fee-shifting |
| Cross-Complaint | §§ 426.10–426.50 | Compulsory (related) or permissive claims |
| Stipulated Extension | Party agreement | Extends deadline |

Failure to respond results in **default** entered by the clerk
under Code Civ. Proc., § 585(a). Once default is entered, the
defendant cannot appear in the action without first setting aside
the default under § 473 (see `ca-post-judgment`).

## Step-by-step workflow

### Day 1 — Triage

**Same day or next day after service.**

- **Photograph the summons, complaint, and envelope** — preserve
  postmark and method of service.
- **Note the date and method of service** (personal delivery,
  substitute service, mail) — this determines the deadline.
- **Calendar the 30-day deadline** using `ca-deadlines`.
- **Calendar a working buffer at day 22** — aim to file by then.
- **Identify the court** (superior court, county, department).
- **Read the complaint carefully** — what causes of action, what
  damages, what relief?
- **Verify proper service** — personal service requires delivery
  to the defendant, or to a person of suitable age at the
  defendant's dwelling or business, with a follow-up mailing
  (Code Civ. Proc., § 415.20(b)).

### Days 2–7 — Defenses inventory

Make a checklist of potential defenses. California demurrers and
motions to quash must be raised early or they may be waived.

**Demurrer grounds (Code Civ. Proc., § 430.10):**

| Ground | Code |
|---|---|
| Court lacks subject-matter jurisdiction | § 430.10(a) |
| Plaintiff lacks legal capacity to sue | § 430.10(b) |
| Suit is another action pending | § 430.10(c) |
| Defect or misjoinder of parties | § 430.10(d) |
| Complaint fails to state facts sufficient to constitute a cause of action | § 430.10(e) |
| Complaint is uncertain, ambiguous, or unintelligible | § 430.10(f) |

**Motion to quash** (Code Civ. Proc., § 418.10): challenges
personal jurisdiction, improper venue, or defective service.
Must be filed before appearing on the merits — making a general
appearance waives these defenses.

**Anti-SLAPP** (Code Civ. Proc., § 425.16): if the claims arise
from the defendant's protected speech or petitioning activity,
the defendant may file a special motion to strike within 60 days
of service of the complaint. An anti-SLAPP motion automatically
**stays all discovery** until the motion is decided. If the
anti-SLAPP motion is granted, defendant is entitled to mandatory
attorney fees and costs.

**Substantive affirmative defenses** (Code Civ. Proc., § 431.30(b)):

Affirmative defenses must be pleaded in the answer with
sufficient facts — vague boilerplate is disfavored. Common
California affirmative defenses:

- Statute of limitations (Code Civ. Proc., § 335 et seq.)
- Accord and satisfaction
- Assumption of risk (tort)
- Comparative fault (Civil Code, § 1431.2)
- Estoppel / equitable estoppel
- Failure of consideration
- Lack of standing or capacity
- Laches
- Payment (full or partial)
- Release or waiver
- Res judicata / claim preclusion
- Collateral estoppel / issue preclusion
- Statute of frauds (Civil Code, § 1624)
- Lack of privity (contract)
- Discharge in bankruptcy (11 U.S.C. § 727)
- Subject-matter-specific defenses (see `ca-consumer-debt` for
  FDCPA / Rosenthal Act defenses in debt cases)

**Verification**: if the complaint is verified (Code Civ. Proc.,
§ 446), the answer must also be verified, and denials must be
specific — a general denial of all allegations is not sufficient
against a verified complaint (Code Civ. Proc., § 431.30(d)).

### Days 7–14 — Cross-complaint planning

California's compulsory cross-complaint statute (Code Civ. Proc.,
§ 426.30):

- **Compulsory**: any related cause of action arising out of the
  same transaction or occurrence **must** be raised in a cross-
  complaint filed before or at the time of trial, or it is
  forever barred (Code Civ. Proc., § 426.30(a)).
- **Permissive**: any other claim against the plaintiff (Code
  Civ. Proc., § 428.10) may be raised in a cross-complaint or
  a separate action.

For consumer-debt defendants, potential cross-claims often include:
- Rosenthal Fair Debt Collection Practices Act (Cal. Civ. Code,
  §§ 1788–1788.33) — if the plaintiff is a debt collector.
- FDCPA (15 U.S.C. § 1692 et seq.).
- California Consumer Privacy Act violations.
- Unlicensed collection activity.

See `ca-consumer-debt` for the full cross-claim menu.

### Days 5–10 — Meet-and-confer requirements

**Before filing a demurrer** (Code Civ. Proc., § 430.41):

- The demurring party must meet and confer with the opposing
  party **in person or by telephone** at least **5 days before**
  the deadline to file the demurrer.
- The meet-and-confer must discuss each ground for the demurrer.
- A declaration describing the meet-and-confer (or explaining
  why it could not be accomplished) must be attached to the
  demurrer as a separate section.
- If the plaintiff agrees to amend on any ground after the meet-
  and-confer, the demurrer on that ground may not be filed until
  the plaintiff fails to file a timely amended complaint.

**Before filing a motion to strike** (Code Civ. Proc., § 435.5):
- Same requirement — meet and confer at least 5 days before filing.
- Declaration of meet-and-confer required.

### Days 14–22 — Draft the response

**Path A: Answer with affirmative defenses and cross-complaint**

Use when the defenses are substantive; when compulsory cross-
claims exist; when discovery should start immediately.

Structure:
1. Caption: SUPERIOR COURT OF CALIFORNIA / COUNTY OF [COUNTY]
2. Parties and case number
3. Title: "DEFENDANT [NAME]'S ANSWER TO COMPLAINT; AFFIRMATIVE
   DEFENSES; AND CROSS-COMPLAINT" (if applicable)
4. Admissions and denials (paragraph-by-paragraph for verified
   complaints; general denial permitted for unverified complaints
   per Code Civ. Proc., § 431.30(d))
5. Affirmative defenses — numbered, each with legal basis and
   a brief factual showing
6. Cross-complaint — separate numbered causes of action, each
   with elements and prayer (if applicable)
7. Prayer for relief
8. Verification (if complaint was verified)
9. Proof of service (Form POS-030)

**Path B: Demurrer (with or without motion to strike)**

Use when a legally valid ground could dispose of one or more
claims without full trial.

Demurrer packet:
1. Notice of demurrer (sets hearing date)
2. Demurrer itself (ground + code section for each count)
3. Memorandum of points and authorities (max 15 pages under Cal.
   Rules of Court, rule 3.1113(d))
4. Declaration of meet-and-confer (Code Civ. Proc., § 430.41)
5. Proposed Order
6. Proof of service

Note: filing a demurrer tolls the answer deadline. If the
demurrer is overruled, the defendant has **10 days** to file the
answer (Code Civ. Proc., § 430.30(c)).

**Path C: Motion to quash service**

Use when service was defective and personal jurisdiction is
disputed. Filing a motion to quash does not constitute a general
appearance and does not waive personal jurisdiction (Code Civ.
Proc., § 418.10(e)).

**Path D: Stipulated extension**

If plaintiff's counsel agrees, get a written stipulation
extending the response date (typically 30 days). File with the
court. Many plaintiffs grant one extension.

### Days 22–28 — QC and filing

- **Run `ca-quality-check`** against the draft.
- **Run `ca-fact-check`** to verify citations and dates.
- **Verify deadlines** with `ca-deadlines`.
- **eFile** via the county's e-filing portal (see `ca-file-packet`).
- **Serve all parties** and file a proof of service.
- **If demurrer**: reserve a hearing date per `ca-schedule-hearing`
  and include the hearing date in the notice.

## Pre-answer evidence preservation

During the 30-day window, the defendant should:

- **Preserve all communications** with the plaintiff (emails,
  letters, voicemails) — may be Rosenthal Act or FDCPA evidence.
- **Preserve business records** (bank statements, account
  agreements, monthly statements).
- **Photograph any physical evidence** that may degrade.
- **Issue a litigation-hold notice** if others hold potentially
  relevant records.

## Default avoidance

The most common pro se failure mode is missing the 30-day
deadline. Tools to prevent it:

- Calendar the deadline the day you are served.
- Calendar a buffer at day 22.
- eFile, not paper, to avoid mailing delays and clerk rejection.
- Confirm filing acceptance within 1 business day; if rejected,
  re-file before day 30.

If default has already been entered, the defendant must move to
vacate under Code Civ. Proc., § 473(b) — see `ca-post-judgment`.

## Cross-references

- `ca-deadlines` — exact date computation (CCP §§ 12, 1013, 1010.6)
- `ca-draft-motion` — demurrer, motion to strike, motion to quash
- `ca-draft-declaration` — meet-and-confer declaration
- `ca-discovery` — first RFPs / RFAs (serve with or after answer)
- `ca-consumer-debt` — debt-defense affirmative defenses and
  cross-complaints
- `ca-pro-se` — pro se procedures in California superior courts
- `ca-post-judgment` — if default already entered (CCP § 473)

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
