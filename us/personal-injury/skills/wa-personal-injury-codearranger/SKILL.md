---
name: wa-personal-injury-codearranger
title: Washington Personal Injury — Subject-Matter Bundle
description: 'Use when handling a Washington personal-injury matter — negligence (pure comparative fault, no plaintiff-fault bar), wrongful death, product liability (WPLA at RCW 7.72), medical malpractice (RCW 7.70), 1986 Reform Act''s several-liability rule (with enumerated joint-liability carve-outs), and Notice of Tort Claim prerequisite for state (RCW 4.92) or local government (RCW 4.96) suits. Substantive framework: RCW Title 4 (Civil Procedure, comparative fault, wrongful death, limitations) + RCW Chapters 7.70 / 7.72. Triggers include "personal injury", "car accident", "medical malpractice", "WPLA", "product liability", "comparative fault", "wrongful death", "Notice of Tort Claim".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-personal-injury
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Washington Personal Injury — Subject-Matter Bundle

> **NOT LEGAL ADVICE.** Personal-injury statutes have been
> amended materially over time. This skill names the
> controlling chapters and describes doctrinal frameworks;
> **current SOL day counts, statutes of repose, notice-of-
> claim periods, joint-liability carve-outs, and damages
> caps live in the references corpus** at `wa-law-
> references/references/wa-rcw-debt/`. Verify against the
> current chapter file before relying on any specific
> figure.

## At a glance — Washington's PI doctrinal architecture

- **Comparative fault**: Washington applies **pure
  comparative fault** — plaintiff recovers reduced by her
  own fault even at 99% at fault. This places WA in the
  minority of ~12 pure-comparative-fault states.
- **Joint vs. several liability**: **several liability is
  the general rule** post-1986 Reform Act, with narrow
  joint-liability carve-outs (concert of action, agency,
  vicarious liability, non-delegable duty, intentional
  conduct, plaintiff-not-at-fault scenarios).
- **Notice of Claim** is a pre-suit prerequisite for suits
  against the state (RCW 4.92) or local governments
  (RCW 4.96).
- **WPLA** at RCW 7.72 is the exclusive remedy for
  manufactured-product injury; common-law strict-product-
  liability claims are preempted.
- **Medical malpractice** at RCW 7.70 has its own SOL,
  notice-of-intent, and mediation framework.

## Chapter pointers

| Topic | Chapter | Reference file |
|---|---|---|
| Comparative fault + apportionment | RCW 4.22 | `RCW-4_22.md` |
| Limitation of actions (SOL) | RCW 4.16 | `RCW-4_16.md` |
| Wrongful death + survival | RCW 4.20 | `RCW-4_20.md` |
| Special rights / immunities | RCW 4.24 | `RCW-4_24.md` |
| Claims against the state | RCW 4.92 | `RCW-4_92.md` |
| Claims against local government | RCW 4.96 | `RCW-4_96.md` |
| Medical malpractice | RCW 7.70 | `RCW-7_70.md` |
| Product liability (WPLA) | RCW 7.72 | `RCW-7_72.md` |

For SOLs, statutes of repose, notice-of-claim contents,
useful-safe-life presumption, and the joint-liability
carve-out enumeration, **read the relevant chapter file**.

## Comparative fault — doctrinal framework

### Pure comparative fault

Plaintiff's fault reduces recovery proportionally; it
does not bar recovery. This contrasts with:

- **Modified comparative fault** (50% or 51% bar — most
  states)
- **Pure contributory negligence** (any plaintiff fault
  bars recovery — DC, MD, NC, VA, AL)

### Apportionment among defendants

Each defendant pays only their proportional share unless
a carve-out applies. The 1986 Reform Act shifted
substantial risk to plaintiffs — under-insured / judgment-
proof co-defendants leave plaintiff bearing that share.
For the carve-out enumeration, see `RCW-4_22.md`.

### Empty-chair defense

Defendants commonly attempt to allocate fault to:

- Settling co-defendants (reasonable-settlement reduction)
- Non-parties / absent tortfeasors (named in answer +
  supported by evidence)
- Plaintiff herself (comparative-fault reduction)

Plaintiff must defend against all of these allocations or
lose recovery to "empty chairs."

## Wrongful death + survival — doctrinal framework

### Wrongful death (RCW 4.20.010-020)

Statute identifies the beneficiary class and the
recoverable elements (economic loss; loss of consortium /
companionship; for some beneficiaries, general damages).
The beneficiary class was expanded by reform in recent
years. For the current beneficiary categories and the
recoverable-elements list, see `RCW-4_20.md`.

### Survival actions

The decedent's PI claim survives to the estate.
Recoverable elements: pre-death medical, lost earnings,
pain and suffering. Recent reform allowed general-damages
survival without dependents. See `RCW-4_20.md`.

### SOL nuance

Wrongful-death SOL runs from **death**, not from the
injury that later caused death — a common pitfall when
the injury and death are temporally separated. Day-count
in `RCW-4_16.md`.

## Medical malpractice — doctrinal framework

### Causes of action

RCW 7.70.030 enumerates three grounds:

1. Negligence — failure to follow accepted standard of
   care
2. Promise of result not fulfilled
3. Lack of informed consent

### SOL + statute of repose

The med-mal SOL combines a "discovery rule" tail with a
hard outer cap (statute of repose). For current day
counts on each prong and the narrow exceptions to the
outer cap, **read `RCW-4_16.md`** (the SOL chapter)
together with `RCW-7_70.md` (the substantive cause-of-
action chapter).

### Pre-suit notice of intent

Plaintiff must serve a written notice of intent to sue
some period before filing. Filing without notice =
dismissal without prejudice (refile after notice
satisfied). See `RCW-7_70.md`.

### Mandatory mediation

For med-mal claims, mediation is mandatory before trial.
Either party can demand; if neither demands, mediation
may be ordered by the court.

### Informed consent

To prove lack of informed consent, plaintiff must
establish a material risk involved, non-disclosure of
that risk, the risk materialized as injury, and that
plaintiff would not have consented if disclosed. See
`RCW-7_70.md`.

### Certificate of merit

A 2006-era certificate-of-merit prerequisite was struck
down by the Washington Supreme Court on right-to-jury-
trial grounds. Do NOT cite that requirement as still
operative. (Case: *Putman v. Wenatchee Valley Med. Ctr.*)

## Product liability (WPLA) — doctrinal framework

### Coverage

WPLA at RCW 7.72 (1981) is the exclusive remedy for
manufactured-product injury. Common-law strict-product-
liability claims are preempted (per *Washington State
Phys. Ins. Exch.*).

### Three defect theories

RCW 7.72.030(1) recognizes:

1. **Construction defect** — the product was unreasonably
   safe in construction
2. **Design defect** — unreasonably safe in design;
   Washington applies a hybrid consumer-expectations +
   risk-utility test
3. **Failure to warn** — adequate warning would have
   prevented harm

### SOL + useful-safe-life presumption

The WPLA SOL applies a discovery rule. Separately, there
is a rebuttable presumption that harm caused outside the
product's "useful safe life" occurred outside the life —
a limitation on liability that can be rebutted by
preponderance of evidence, with narrow statutory
exceptions for warranty of longer safe use, intentional
misrepresentation, and pre-life exposure with delayed
manifestation.

For the current SOL day count, the useful-safe-life
presumption period, and the exception enumeration, see
`RCW-7_72.md`.

### Defenses

- Useful safe life expired (subject to exceptions)
- Alteration after sale
- Misuse
- State-of-the-art (risk-utility analysis)
- Comparative fault

## Notice of Tort Claim — pre-suit prerequisite

### Against the State

Suits against the State of Washington require a written
Notice of Tort Claim filed with the Office of Risk
Management a fixed period before suit, with mandatory
contents (claimant identification, incident date / time /
place, description of incident + cause, damages
description, damages amount, claimant verification). The
notice tolls the SOL. Substantial compliance excused;
missing required elements is fatal. See `RCW-4_92.md`.

### Against Local Governments

The parallel requirement against cities, counties, school
districts, and other local entities sits in `RCW-4_96.md`.
Same notice period, same content requirements.

## Damages

### Economic vs. non-economic

Economic damages (medical, lost earnings, future
earnings, future medical, property damage) — joint and
several among co-defendants per fault allocation.
Non-economic damages (pain and suffering, emotional
distress, loss of consortium) — **several only** under
the Reform Act's carve-out for non-economic damages.
Collateral-source rule applies.

### Punitive damages

Washington does NOT recognize punitive damages at common
law. Allowed only by statute (e.g., RCW 19.86 CPA treble
damages; RCW 49.60 WLAD; some federal claims).

### Caps

Washington does NOT have a general PI damages cap.

## Composition with other wa- skills

- `wa-statewide-format` — caption + GR 14
- `wa-discovery` — RFP / interrogatories / RFA / deps
- `wa-first-30-days` — answer + affirmative defenses
- `wa-deadlines` — SOL computation + Notice of Claim
- `wa-fact-check` — citation verification
