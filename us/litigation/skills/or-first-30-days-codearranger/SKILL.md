---
name: or-first-30-days-codearranger
title: Oregon — First 30 Days After Service
description: Use this skill when an Oregon defendant is served with a summons and complaint. Triggers include "I was just served", "summons and complaint", "what do I do first", "deadline to answer", "answer the complaint", "affirmative defenses checklist", "counterclaim planning", "ORCP 21", "motion to dismiss or answer", "plead counterclaims". Covers ORCP 7 C(2) 30-day deadline, ORCP 21 motion-to-dismiss triage, affirmative-defenses checklist, counterclaim mechanics (ORCP 22), evidence preservation, and discovery planning. For subject-matter fact patterns and counterclaim menus, compose with relevant subject-matter skill (e.g., or-consumer-debt). Composes with or-deadlines, or-draft- motion, or-draft-declaration, or-discovery, or-law-references, or-fact-check, or-file-packet, and (if default entered) or- post-judgment.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Oregon — First 30 Days After Service

When a defendant in an Oregon civil case is served with a
summons and complaint, **ORCP 7 C(2)** gives them 30 calendar
days to respond. This skill covers the matter-neutral
workflow for that window — what to do, in what order, to
preserve all rights and put the defendant in the strongest
position before answering.

> **NOT LEGAL ADVICE.** This is a procedural framework, not a
> case strategy. The strategic decisions (defend on the merits?
> attack jurisdiction? negotiate? settle?) depend on the
> specific facts and law.

## The 30-day clock

The 30-day clock starts on the **day after service** and runs
30 calendar days under ORCP 10 A. If day 30 falls on a weekend
or legal holiday (ORS 187.010), the deadline extends to the
next business day.

For service by mail (rare for initial process, but happens with
ORCP 7 D(2)(d) consensual mail service), add 3 days under ORCP
10 C.

For service by publication (ORCP 7 D(6)), the 30 days starts
from the date of last publication.

Use `or-deadlines` and `scripts/case-calendar.py` to compute
the precise deadline.

## Three response options

The defendant must do one of three things within 30 days:

1. **File an Answer** (the merits response)
2. **File an ORCP 21 motion to dismiss** (or other ORCP 21
   defense raised as a motion) — this tolls the answer deadline
3. **Reach an agreed extension** with plaintiff (typically a
   written stipulation filed with the court)

Failure to do one of these results in **default** under ORCP
69. The defendant's defenses on the merits are lost; only
ORCP 71 vacation can re-open the case.

## Step-by-step workflow

### Day 1 — Triage

**Same day or next day after service.**

- **Photograph the summons, complaint, and any envelope** —
  preserve the postmark and method of service
- **Note the date and method of service** — these affect the
  deadline computation
- **Calendar the 30-day deadline** using `or-deadlines`
- **Calendar a working buffer at day 23** — file by then if
  possible
- **Identify the court** — circuit court, county, case number
- **Read the complaint carefully** — what claims, what
  damages, what relief?

### Days 2–5 — Defenses inventory

Make a checklist of potential defenses. The ORCP 21 defenses
are jurisdictional or procedural and **must be raised first**
(via ORCP 21 motion OR in the answer) or they are waived
(ORCP 21 G):

| Defense | ORCP | When waived |
|---------|------|-------------|
| Lack of subject-matter jurisdiction | 21 A(1) | Never |
| Lack of personal jurisdiction | 21 A(2) | If not raised by motion or in first responsive pleading |
| Improper venue | 21 A(3) | Same |
| Insufficient service of summons | 21 A(4) | Same |
| Insufficient service of process | 21 A(5) | Same |
| Not the real party in interest | 21 A(6) | If not raised by motion or in first responsive pleading |
| Failure to join party | 21 A(7) | At any time |
| Failure to state ultimate facts | 21 A(8) | At any time (but raised promptly) |
| Pendency of another action | 21 A(9) | If not raised by motion or in first responsive pleading |
| More definite statement | 21 B | If not raised by motion before responsive pleading |
| Motion to strike | 21 E | If not raised by motion before responsive pleading |

Also consider substantive affirmative defenses (these go in the
answer, not the ORCP 21 motion):

- Statute of limitations (ORS 12 — verify SOL for each claim)
- Statute of frauds (ORS 41.580)
- Lack of capacity / standing
- Failure of consideration
- Accord and satisfaction
- Estoppel / waiver / laches
- Comparative fault (ORS 31.600)
- Set-off
- Discharge in bankruptcy (11 USC § 727)
- Federal preemption
- Anti-SLAPP (ORS 31.150)
- Subject-matter-specific defenses (see relevant subject-matter
  skill)

### Days 5–10 — Counterclaims inventory

ORCP 22 governs counterclaims:

- **Compulsory counterclaim** (ORCP 22 A): any claim arising
  out of the same transaction or occurrence. **Must be raised
  in the answer or it's waived** for future actions.
- **Permissive counterclaim** (ORCP 22 B): any other claim
  against the plaintiff. Can be raised in the answer or in a
  separate action.

For a debt-collection defendant, potential counterclaims often
include:

- FDCPA (15 USC § 1692k) — if a debt collector or collection
  attorney is the plaintiff
- Oregon UTPA (ORS 646.605) — broader than FDCPA
- ORS 697 (Collection Agency) — if plaintiff is not registered
- Defamation, intentional interference, etc. — fact-specific

See `or-consumer-debt` for the full debt-defense counterclaim
menu. For other case types, consult the relevant subject-
matter skill or general civil-defense practice.

### Days 10–15 — Discovery planning

While the answer is being drafted, plan initial discovery:

- **First RFPs**: target the plaintiff's foundational
  evidence — contract, chain of title, accounting,
  authorization to sue, registration to do business
- **First RFAs**: lock in basic facts that should be
  uncontroverted (corporate form, identity, dates)
- **Depositions**: typically not until after answer; identify
  potential deponents (plaintiff's PMK, document custodian)
- **Subpoenas to non-parties** (original creditor, banks):
  plan but don't issue until after answer

Serve discovery **with the answer or shortly thereafter** —
discovery is often the bottleneck and starting early creates
leverage.

### Days 15–23 — Draft the response

Choose the path:

#### Path A: Answer with affirmative defenses + counterclaims

Use this when:

- The defenses are substantive (SOL, lack of standing, etc.)
- You want to start discovery immediately
- Counterclaims should be pled now

Structure:

1. Caption (court header, parties, case number, title:
   "DEFENDANT'S ANSWER, AFFIRMATIVE DEFENSES, AND
   COUNTERCLAIMS")
2. Admissions and denials — paragraph-by-paragraph response to
   the complaint
3. Affirmative defenses — numbered, each with the legal basis
   and a brief factual showing
4. Counterclaims — numbered, each with elements and prayer for
   relief
5. Prayer for relief on counterclaims
6. Signature block (with "Defendant, pro se" if applicable)
7. Certificate of Service

#### Path B: ORCP 21 motion to dismiss

Use this when:

- A jurisdictional or service defect could end the case
- Failure to state ultimate facts (ORCP 21 A(8)) — the
  complaint, accepting allegations as true, doesn't entitle
  plaintiff to relief
- You want to delay the merits while pursuing the procedural
  issue

Structure (see `or-draft-motion`):

1. Caption ("DEFENDANT'S MOTION TO DISMISS UNDER ORCP 21
   A(8)")
2. Motion
3. Memorandum — facts, issues, evidence, authorities, argument
4. Conclusion

ORCP 21 motions toll the answer deadline. If denied, the
defendant has **10 days** to file the answer (ORCP 21 D —
verify current rule).

#### Path C: Stipulated extension

If the parties agree, file a Stipulation for Extension of
Time signed by all counsel/parties. The court routinely grants
modest extensions (14–30 days) on stipulation.

Some Oregon judges have specific extension protocols in their
standing orders — check first.

### Day 23–25 — QC and filing

- **Run `or-quality-check`** against the draft
- **Run `or-fact-check`** to verify citations and dates
- **Verify deadlines** with `or-deadlines`
- **eFile via File and Serve** with the correct UTCR 2.110
  document code
- **Serve all parties** under ORCP 9 / UTCR 21.100
- **File a Notice of Hearing** if the response is an ORCP 21
  motion that needs a hearing date

## Pre-answer evidence preservation

Before, during, and after the 30-day window, the defendant
should:

- **Preserve all communications** with plaintiff (emails,
  letters, voicemails) — these may be FDCPA or UTPA evidence
- **Preserve relevant business records** — bank statements,
  cardholder agreement, monthly statements (if not destroyed
  in the ordinary course)
- **Photograph any physical evidence** that may degrade
- **Issue a litigation-hold notice** to anyone in custody of
  potentially relevant documents (in a pro se context, this
  is often informal — "please don't destroy the email
  archive")

## Pre-answer settlement

Consider whether to attempt settlement before answering:

- **Pro**: avoids the cost of litigation; some plaintiffs
  settle for pennies on the dollar before discovery
- **Con**: the defendant gives up the leverage of an answer
  with counterclaims; the plaintiff may interpret a pre-
  answer settlement offer as weakness

For debt cases, sending a debt-validation request (ORS 697 /
FDCPA) during the 30-day window is often a procedurally
parallel move — it forces the plaintiff to produce
authentication documents while the answer is being drafted.

## Default avoidance

The single biggest pro se failure mode is **missing the
30-day deadline**. Tools to prevent it:

- **Calendar the deadline immediately** upon service
- **Calendar a buffer at day 23** so a late file is still
  on time
- **eFile, not paper** — paper risks clerk rejection
- **Confirm filing acceptance** within 2 business days; if
  rejected, re-file before day 30

If default has already been entered, the defendant must move
to vacate under ORCP 71 B — see `or-post-judgment`.

## Pro se considerations

A pro se defendant in the first 30 days should:

- **Save every paper document** the plaintiff has sent
- **Save every email and voicemail** — even spam-folder
  ones from the plaintiff
- **Photograph the envelope** of the summons before
  opening (to preserve postmark)
- **Sleep on the response** before filing — initial drafts
  are often emotionally loaded
- **Consider getting an attorney consultation** even for
  pro se cases — many Oregon attorneys offer flat-fee
  consultations under the OSB Modest Means program

## Step summary

1. **Day 1**: triage, photograph, calendar
2. **Days 2–5**: defenses inventory
3. **Days 5–10**: counterclaims inventory
4. **Days 10–15**: discovery planning
5. **Days 15–23**: draft answer + counterclaims OR ORCP 21
   motion
6. **Days 23–25**: QC, fact-check, eFile, serve

Build the buffer at day 23. Aim for day 25 filing, with day 30
as the absolute deadline. Anything later is a default-risk
race.

## Cross-references

- `or-deadlines` — exact date computation
- `or-draft-motion` — ORCP 21 motion structure
- `or-draft-declaration` — supporting declaration form
- `or-discovery` — first RFPs / RFAs
- `or-law-references/references/civil-rules.md` — ORCP 7, 10,
  21, 22 verbatim
- `or-consumer-debt` — debt-defense-specific affirmative
  defenses and counterclaims
- `or-pro-se` — pro-se drafting framework for the response
- `or-post-judgment` — if default has already been entered,
  motion to vacate under ORCP 71
