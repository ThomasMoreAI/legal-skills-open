---
name: ny-personal-injury-codearranger
title: New York Personal-Injury Practice
description: Use when drafting or filing a personal-injury action — motor vehicle accident, slip and fall, medical malpractice, construction-site injury, wrongful death, sex-abuse revival claims. Triggers include 'personal injury New York', 'NY PI', 'no-fault Insurance Law 51', 'serious injury threshold', 'Labor Law 240', 'Labor Law 241(6)', 'Article 14-A comparative fault', 'Article 16 several liability', 'GML 50-e Notice of Claim 90 days'. Covers **Insurance Law Article 51** no-fault + serious injury threshold (§ 5102(d)); **CPLR 1411** pure comparative fault; **CPLR Article 16** several-liability cap for non-economic damages; **Labor Law §§ 200/240/241** construction-site (absolute liability under § 240(1) "scaffold law"); med-mal **CPLR 214-a** 30-month SOL; **CPLR 214-c** toxic-tort discovery rule; **wrongful death** under EPTL § 5-4.1; **GML § 50-e** 90-day Notice of Claim; and bill-of-particulars practice.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-personal-injury
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# New York Personal-Injury Practice

> **NOT LEGAL ADVICE.** PI practice in NY is highly
> deadline-sensitive; verify every SOL and predicate-notice
> clock against the canonical CPLR / Insurance Law / EPTL
> sources before relying on this skill.

## SOL catalog (the most-used)

| Claim | SOL | Citation |
|---|---|---|
| **General negligence / strict liability** | **3 years** | CPLR 214(5) |
| **Defamation / libel / slander** | **1 year** | CPLR 215(3) |
| **Battery / assault / false imprisonment** | **1 year** | CPLR 215(3) |
| **Medical / dental malpractice** | **2 years 6 months (30 months)** | CPLR 214-a; continuous-treatment toll under *Borgia v. City of New York* |
| **Foreign-object medical malpractice** | **1 year from discovery** (with 30-month cap from action) | CPLR 214-a |
| **Toxic substance / latent injury** | **3 years from discovery** (CPLR 214-c "discovery rule") | CPLR 214-c |
| **Asbestos / environmental hazard** | CPLR 214-c discovery rule | |
| **Wrongful death** | **2 years from death** | EPTL § 5-4.1 |
| **Loss of consortium** | derivative — tracks the underlying claim's SOL | |
| **Negligent infliction of emotional distress** | 3 years CPLR 214(5) | |
| **Intentional infliction of emotional distress** | 1 year CPLR 215(3) | |
| **Action against state / municipality** | **1 year + 90 days** after accrual (after the GML § 50-e 90-day Notice of Claim) | CPLR 217-a / GML § 50-i |

### Revival windows — historic

- **Child Victims Act** (CPLR 214-g, L 2019 ch 11; revival window expired August 14, 2021): one-time revival of sex-abuse claims occurring while the survivor was a minor.
- **Adult Survivors Act** (CPLR 214-j, L 2022 ch 203; revival window expired November 23, 2023): one-time revival of sex-abuse claims occurring while the survivor was 18+.

The revival windows have closed — but cases filed within
the windows continue under the normal NY procedural
framework.

## No-fault threshold for MVA

Insurance Law **Article 51** (the No-Fault Law) governs
motor-vehicle-accident PI. A plaintiff cannot maintain a
common-law negligence action against the at-fault driver
**unless** the injury crosses the **"serious injury"
threshold** at Insurance Law § 5102(d):

- Death
- Dismemberment
- Significant disfigurement
- A fracture
- Loss of a fetus
- Permanent loss of use of a body organ, member, function or system
- Permanent consequential limitation of use of a body organ or member
- Significant limitation of use of a body function or system
- A medically determined injury or impairment of a non-permanent nature which prevents the injured person from performing substantially all of the material acts which constitute such person's usual and customary daily activities for not less than ninety days during the one hundred eighty days immediately following the occurrence of the injury or impairment

The serious-injury threshold is the most-litigated PI issue
in NY. Defense counsel routinely move for summary judgment
under CPLR 3212 alleging the plaintiff doesn't satisfy any
of the nine categories.

### First-party PIP benefits

Independent of the threshold, the **no-fault insurer**
provides **PIP (Personal Injury Protection)** benefits up to
$50,000 to the injured person (passenger or pedestrian) —
medical, lost wages (80% up to $2,000/month), funeral
expenses ($2,000), other reasonable expenses ($25/day).
Claim notice under 11 NYCRR § 65-1.1 must be made within
**30 days** of accident.

## CPLR 1411 + Article 16 — fault apportionment

### Pure comparative fault (CPLR 1411 / Article 14-A)

NY follows **pure comparative fault**. The plaintiff's
recovery is reduced by their percentage of fault — even if
the plaintiff was 99% at fault, they still recover 1%. No
contributory-negligence bar.

### Article 16 — limited several liability for non-economic

CPLR Article 16 (§§ 1600-1603) **limits joint-and-several
liability** for non-economic damages (pain and suffering).
A defendant who is found 50% or less at fault is liable for
only their proportionate share of non-economic damages —
not the full joint-and-several amount. Economic damages
(medical bills, lost wages) remain joint-and-several.

Exceptions (the Article 16 "carve-outs" — joint and
several still applies):

- Motor-vehicle defendants (CPLR 1602(6))
- Defendants who acted with intent or actual knowledge
- Hazardous-substance defendants
- Construction Labor Law § 240/241(6) defendants
- Concurrent-tortfeasors-by-statute defendants

## Labor Law §§ 200, 240, 241

The principal **construction-site liability** statutes:

### Labor Law § 200 — common-law negligence codified

Owners, contractors, and agents have a duty to provide a
reasonably safe place to work. Plaintiff must prove the
defendant had **notice** of the dangerous condition + the
**authority to control** the work.

### Labor Law § 240(1) — absolute liability (the "scaffold law")

Owners and contractors are **strictly liable** for elevation-
related injuries from a defective or absent safety device:

- Scaffolds, ladders, hoists, slings, blocks, pulleys, ropes
- Plaintiff need not prove notice or negligence
- "Sole proximate cause" defense available only if the
  worker's own conduct was the *exclusive* cause (rare)
- Comparative-fault reduction does NOT apply

The scaffold law is the most plaintiff-favorable
construction-site statute in the country.

### Labor Law § 241(6) — Industrial Code violation

Owners and contractors must comply with specific Industrial
Code (12 NYCRR Part 23) regulations. A plaintiff must
identify a **specific code provision** that was violated and
that was a substantial factor causing the injury.
Comparative-fault reduction DOES apply.

## Notice of Claim — GML § 50-e

Actions against the State, City of New York, school
districts, public hospitals, and other municipal defendants
require a **Notice of Claim** filed within **90 days** of
the accrual of the cause of action (GML § 50-e). The claim
must include:

- Name + post-office address of claimant + attorney
- Nature of the claim
- Time, place, and manner of occurrence
- Items of damage / injury

**Late Notice of Claim** is available by court order under
GML § 50-e(5) — discretionary, considers the public actor's
actual knowledge of the essential facts, prejudice, and the
reason for delay. Petition must be filed within **1 year +
90 days** of accrual.

The 1-year + 90-day SOL under GML § 50-i runs from accrual
for the action itself.

## Bill of Particulars — NY-unique PI practice

NY personal-injury practice features the **Bill of
Particulars** at CPLR § 3041-3043 — a pleading-amplification
document that the plaintiff serves to specify:

- Negligent acts alleged
- Injuries claimed
- Special damages (medical bills, lost wages)
- Lost-time periods
- Future-damages claims

A defective Bill of Particulars limits the plaintiff at
trial. The standard NY PI defense playbook: serve a
**Demand for Bill of Particulars**, then move to preclude
under CPLR 3042 if responses are inadequate.

## Wrongful death — EPTL Article 5 Part 4

EPTL § 5-4.1 governs wrongful-death actions:

- **Personal representative** of the decedent is the proper
  plaintiff (administrator or executor)
- **Distributees** entitled to recovery (the spouse +
  children + parents in priority)
- **2-year SOL** from date of death
- Damages: pecuniary loss only — not pain and suffering
  pre-death (a separate **survival action** under EPTL
  § 11-3.2 covers conscious pain and suffering)

## Composition with other ny- skills

- `ny-statewide-format` — caption + Notice of Motion format
- `ny-discovery` — CPLR Article 31 disclosure (PI cases
  typically aggressive disclosure; both parties exchange
  medical records under HIPAA-compliant authorizations)
- `ny-first-30-days` — Answer + affirmative defenses
- `ny-hearings` — Motion-day practice
- `ny-deadlines` — SOL + Notice-of-Claim arithmetic
- `ny-fact-check` — *Buckley v. City of NY* and other
  citation patterns
- `ny-nyco` / `ny-kings` / `ny-bronx` etc. — venue routing
  (PI cases route to Supreme Court when over $25,000;
  Bronx + Brooklyn historically have plaintiff-favorable
  juries)

## High-yield PI checks

1. **MVA?** Threshold + PIP benefits + no-fault arbitration?
2. **Government defendant?** GML § 50-e 90-day clock + late-
   notice analysis?
3. **Construction site?** Labor Law 240 vs. 241(6) vs. 200
   triage?
4. **Medical malpractice?** Continuous-treatment toll +
   CPLR 214-a 30-month math?
5. **Toxic / latent?** CPLR 214-c discovery rule?
6. **Wrongful death?** EPTL 5-4.1 personal rep + 2-year SOL?
7. **Article 16 applicability?** Carve-outs for MVA, hazmat,
   Labor Law 240?
8. **Workers' comp interplay?** WCL § 11 election + § 29
   subrogation lien?
9. **Sex-abuse claim?** CVA or ASA revival window applies
   (now closed for new filings but in-progress filings
   continue)?

## Pro-se resources

- **NYS OCA Court Help** — PI section at
  `nycourts.gov/courthelp/`
- **Pro Bono Net** — PI referral network
- **NY State Bar Association Lawyer Referral**:
  800-342-3661
- **NYC Lawyer Referral**: 212-626-7373
