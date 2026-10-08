---
name: tn-personal-injury-codearranger
title: Tennessee Personal-Injury Practice
description: Subject-matter bundle for Tennessee personal-injury and tort actions. Covers McIntyre v. Balentine modified comparative fault (49% bar); SOLs (1-year personal injury § 28-3-104, 3-year property damage § 28-3-105); 2011 tort- reform damages caps (§ 29-39-102 non-economic $750k/$1M catastrophic; § 29- 39-104 punitives greater of $500k or 2x compensatory; upheld in McClay v. Airport Management Services); Governmental Tort Liability Act (§ 29-20-101; $300k/$700k caps; ~12-month SOL; bench trial); Health Care Liability Act (§ 29-26-121 60-day pre-suit notice; § 29-26-122 certificate of good faith; § 29-26-116 3-year statute of repose); Tennessee Products Liability Act (§ 29-28-103 10-year statute of repose); wrongful death (§ 20-5-106); UM/UIM (§ 56-7-1201).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-personal-injury
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Tennessee Personal-Injury Practice

> **NOT LEGAL ADVICE.** Tennessee tort practice is deadline-sensitive
> and has strict pre-suit gates (especially in health-care and
> governmental cases). Statute numbers, dollar caps, and day counts
> change — verify every SOL, cap, and predicate-notice clock against
> the current Tenn. Code Ann. before relying, and consult a licensed
> Tennessee attorney about your specific case.

Use this subject-matter bundle for Tennessee personal-injury and
tort actions — auto accidents, premises (slip-and-fall), product
and general negligence, health-care liability, wrongful death,
products, dog-bite, and claims against governmental entities.

## At a glance — the eight things that move every TN PI case

1. **1-year personal-injury SOL** at § 28-3-104 — Tennessee's
   personal-injury clock is among the shortest in the country.
   Calendar at intake.
2. **Modified comparative fault with 49% bar** under *McIntyre v.
   Balentine*, 833 S.W.2d 52 (Tenn. 1992). Plaintiff barred at
   50% or more fault.
3. **Several liability (not joint and several)** post-*McIntyre*
   for most non-economic / non-intentional torts. Identify all
   at-fault parties **and non-parties** for fault allocation;
   Tenn. R. Civ. P. 8.03 / *Brown v. Wal-Mart Stores East, L.P.*
   (E.D. Tenn. 2010).
4. **HCLA pre-suit notice (60 days) + certificate of good faith**
   under §§ 29-26-121 / -122. The two most common case-killers in
   Tennessee health-care litigation.
5. **GTLA short-fuse SOL (~12 months) + immunity removal + $300k/$700k caps**
   under § 29-20-201 to -305 + § 29-20-403. Identify governmental
   defendants at intake; the GTLA reshapes the whole case.
6. **2011 tort-reform damages caps** under §§ 29-39-102 / -104 —
   non-economic capped at $750k (most) or $1M (catastrophic);
   punitives capped at the greater of $500k or 2x compensatory.
   Upheld in *McClay v. Airport Management Services*, 596 S.W.3d
   686 (Tenn. 2020).
7. **TPLA 10-year statute of repose** under § 29-28-103 for
   products-liability actions — a hard outer limit independent
   of the SOL.
8. **Wrongful death is a survival statute** (§ 20-5-106) — the
   action survives in the decedent's name with damages
   apportioned to statutory beneficiaries.

## Statute-of-limitations catalog

| Claim | SOL | Citation |
|---|---|---|
| **Personal injury / personal torts** | **1 year** | Tenn. Code Ann. § 28-3-104(a)(1) |
| Personal injury with parallel criminal charges | up to **2 years** (extension) | § 28-3-104(a)(2) |
| **Property damage (incl. auto property)** | **3 years** | § 28-3-105 |
| **Health care liability action** | **1 year** + 120-day pre-suit-notice extension; 3-year statute of repose | § 28-3-104 + § 29-26-116 + § 29-26-121 |
| **Wrongful death** | **1 year** from death (statute of repose framework for HCL deaths) | § 28-3-104 + § 20-5-106 |
| **Products liability (TPLA)** | **1 year** SOL + **10-year statute of repose** from first purchase | § 29-28-103 |
| **Premises liability (private)** | **1 year** | § 28-3-104 |
| **Action against a governmental entity (GTLA)** | **~12 months** | § 29-20-305 |
| **Dog bite** | **1 year** (treated as personal injury) | § 28-3-104 + § 44-8-413 |
| **UM/UIM contract claim** | **6 years** (contract SOL) | § 28-3-109 |

**Notes**:

- The 1-year personal-injury SOL (§ 28-3-104) is **discovery-rule**
  tolled for latent injuries (*Foster v. Harris*, 633 S.W.2d 304
  (Tenn. 1982)).
- In an auto case the personal-injury and property-damage claims
  run on **different** clocks (1 year vs. 3 years).
- Compliant HCLA pre-suit notice **extends the SOL by 120 days**;
  the 3-year statute of repose under § 29-26-116 is NOT extended
  by pre-suit notice (a sharp trap).
- The TPLA 10-year statute of repose is **outcome-determinative**
  and runs from the **first purchase for use or consumption**, not
  from injury date.

## Comparative fault — the 49% bar and several liability

Tennessee follows **modified comparative fault with a 49% bar**,
adopted in *McIntyre v. Balentine*, 833 S.W.2d 52 (Tenn. 1992):

- Plaintiff recovers only if plaintiff's fault is **less than 50%**.
- Plaintiff who is **50% or more** at fault recovers **nothing**.
- Recovery is **reduced by the plaintiff's percentage of fault**.

*McIntyre* abolished common-law contributory negligence **and
joint-and-several liability** (for non-intentional torts).
Tennessee operates a **several-liability regime**: each defendant
pays only its allocated share. *McIntyre*'s reasoning is codified
at Tenn. Code Ann. § 29-11-107 (with exceptions).

**Identification and joinder of all potentially at-fault parties
(and non-parties for allocation)** is the central strategic
concern. The defense raises **non-party fault** under Tenn. R.
Civ. P. 8.03 by amendment to the answer, triggering the
plaintiff's right to amend within **90 days** to add the named
non-party as a defendant (*Brown v. Wal-Mart Stores East, L.P.*).
Failure to add within 90 days does not bar allocation, but bars
direct recovery against the non-party.

## Damages framework

### Non-economic damages cap — § 29-39-102 (effective Oct. 1, 2011)

Tennessee caps **non-economic damages** (pain and suffering, loss
of enjoyment, emotional distress, loss of consortium, etc.):

- **$750,000** per injured person, all defendants combined, for
  most cases.
- **$1,000,000** per injured person where the injury is
  "catastrophic" — defined as spinal-cord injury with paralysis,
  amputation, third-degree burns over 40% of body or face,
  wrongful death of a parent leaving a surviving minor child.
- **Exemptions** at § 29-39-102(c)(2): defendant acted with
  intent to inflict serious physical injury; defendant
  intentionally falsified, destroyed, or concealed evidence;
  defendant was under the influence of alcohol or drugs to the
  point that judgment was substantially impaired; defendant
  committed a felony related to the action.

**Constitutional challenge rejected**: *McClay v. Airport
Management Services, LLC*, 596 S.W.3d 686 (Tenn. 2020), upheld
§ 29-39-102 against state-constitutional challenges
(individual right to a jury trial; equal protection; due
process). The caps are firmly in place.

### Punitive damages cap — § 29-39-104

- Punitives capped at the **greater of $500,000** or **two times
  the total compensatory damages** awarded.
- **Exemptions** at § 29-39-104(a)(7): same list as the non-
  economic cap exemptions, plus a few narrower ones.
- **Hodges v. S.C. Toof & Co.**, 833 S.W.2d 896 (Tenn. 1992),
  remains the common-law standard for entitlement: the
  plaintiff must show by **clear and convincing evidence** that
  the defendant acted intentionally, fraudulently, maliciously,
  or recklessly.
- Bifurcated trial on punitives is **automatic** on request
  under § 29-39-104(a)(2) — liability/compensatory first, then
  punitives.

### Economic damages

Not capped. Wage loss, medical expenses (past + future),
out-of-pocket costs, lost earning capacity, and future medical
needs are all uncapped.

**Collateral source rule**: Tennessee continues to recognize
the collateral-source rule for tort cases — payments from
independent sources (health insurance, disability) generally do
not reduce a tortfeasor's liability (*Donnell v. Donnell*,
2009; but see § 24-5-113 for the limited medical-bill statutory
presumption of reasonableness).

## Governmental Tort Liability Act (GTLA)

Claims against the State, counties, municipalities, and other
governmental entities are governed by the **Governmental Tort
Liability Act**, Tenn. Code Ann. § 29-20-101 et seq.

**Critical mechanics**:

- **Immunity is the default**; removed only as the statute
  provides. Categories at § 29-20-202 to -205 (negligent
  operation of motor vehicles; dangerous conditions of streets
  / sidewalks / structures; certain employee negligence).
  **Work the claim into a removal category or it fails.**
- **Damages caps** under § 29-20-403:
  - **$300,000 per person**;
  - **$700,000 per occurrence**;
  - **$100,000 per occurrence** for property damage.
  (Confirm current figures; the legislature has amended these
  before.)
- **Shortened SOL** under § 29-20-305: **~12 months** from
  accrual. Do **not** assume the general 1-year personal-injury
  clock — confirm the exact accrual rule.
- **No jury trial**; GTLA cases are tried to the bench under
  § 29-20-307.
- **Discretionary-function immunity**: planning-level decisions
  are immune; operational-level negligence is actionable.
  *Bowers v. City of Chattanooga*, 826 S.W.2d 427 (Tenn. 1992).
- **Notice of claim**: GTLA does not have a separate notice-of-
  claim statute parallel to many states, but consult the
  specific governmental defendant's charter / ordinances for any
  pre-suit-notice requirement.

**Federal claims against governmental defendants** (42 U.S.C.
§ 1983; ADA; Title VI) escape the GTLA framework and run in
parallel under their own SOLs.

## Health Care Liability Act (HCLA)

Tennessee replaced "medical malpractice" with **"health care
liability action"** in 2011. Use the term.

### Pre-suit notice — 60 days (§ 29-26-121)

Written notice to each provider **at least 60 days before
filing**. Content requirements:

- Identity of claimant + relationship to person who received care
- Plaintiff's date of birth + last 4 of SSN
- The full name and address of each provider being notified
- The full name and address of each other provider also being
  notified
- HIPAA-compliant medical authorization
- A list of names and addresses of all providers being notified

**Compliant pre-suit notice extends the SOL by 120 days**. The
3-year statute of repose (§ 29-26-116) is **NOT** extended.

**Defective notice = dismissal**. *Stevens ex rel. Stevens v.
Hickman Community Health Care Services, Inc.*, 418 S.W.3d 547
(Tenn. 2013), clarified that compliance must be substantial,
not perfect, but missing one of the listed elements (especially
the HIPAA authorization) is fatal to extension and often to the
claim.

### Certificate of good faith — § 29-26-122

Where expert testimony is required (essentially always for
non-common-knowledge claims), file a certificate with the
complaint:

- Plaintiff or counsel has consulted with one or more experts;
- Each expert is qualified under § 29-26-115;
- Each expert has provided a signed written statement that
  there is a good-faith basis;
- Certificate is signed by counsel (or plaintiff if pro se).

**Failure to file** = **dismissal with prejudice** under
§ 29-26-122(c). The dismissal is generally **not curable** by
amendment.

### Expert qualifications — § 29-26-115

The **contiguous-state rule**: an expert must have practiced in
Tennessee or in a state bordering Tennessee in the year
preceding the alleged negligence. Tennessee borders Kentucky,
Virginia, North Carolina, Georgia, Alabama, Mississippi,
Arkansas, and Missouri (8 states). The contiguous-state rule
sharply limits the available expert pool.

## Tennessee Products Liability Act (TPLA) — § 29-28-101 et seq.

- **Strict liability + negligence + breach of warranty**
  unified into a single statutory framework.
- **10-year statute of repose** under § 29-28-103(a) — runs from
  the **date the product was first purchased for use or
  consumption**, not from the date of injury. Bars suit on
  injury occurring after the 10-year mark.
- **Special carve-outs**: silicone gel breast implants extended
  to 25 years; asbestos has no repose; certain implanted
  devices have extended periods.
- **Sealed-container defense** under § 29-28-106 protects
  retailers and distributors who sold the product in a sealed
  container, leaving manufacturer liable.

## Wrongful death — § 20-5-106 et seq.

Tennessee's wrongful-death statute is a **survival statute**:
the cause of action survives in the **decedent's name**, prosecuted
by the surviving spouse, children, parents (in order), or
personal representative.

- **SOL**: 1 year from death (§ 28-3-104) — runs from death, not
  from the underlying tort.
- **HCL deaths**: pre-suit notice + certificate of good faith
  apply; 3-year statute of repose under § 29-26-116 runs from
  the date of the negligent act, not death.
- **Damages catalog** under § 20-5-113:
  - Pecuniary value of life lost (lost earnings + lost
    services + funeral expenses);
  - Mental and physical suffering of decedent before death;
  - Loss of consortium to surviving spouse (separately under
    § 20-5-113(a)(1));
  - **Hancock damages** — emotional injury and grief of
    surviving beneficiaries (*Jordan v. Baptist Three Rivers
    Hospital*, 984 S.W.2d 593 (Tenn. 1999)).
- **Beneficiary apportionment** under § 20-5-107: spouse +
  children share; if neither, parents; if neither, dependents.

## Premises liability

- **Open and obvious is not an automatic bar** — *Coln v. City
  of Savannah*, 966 S.W.2d 34 (Tenn. 1998), modified the
  doctrine into a duty/foreseeability/balance-of-risk analysis
  rather than a categorical defense.
- **Status distinctions reduced** but not abolished — Tennessee
  still distinguishes invitees, licensees, and trespassers,
  but the differences are muted under the *Coln*
  foreseeability framework.
- **Mode-of-operation theory** — *Blair v. West Town Mall*, 130
  S.W.3d 761 (Tenn. 2004), recognized a limited mode-of-
  operation theory for self-service operations.
- **Constructive notice** — plaintiff must show the dangerous
  condition existed long enough for the defendant to have
  known or reasonably should have known. *Self v. Wal-Mart
  Stores, Inc.*, 885 F.2d 336 (6th Cir. 1989).

## UM / UIM motorist coverage — § 56-7-1201 et seq.

- Mandatory **UM offer** under § 56-7-1201; insured may reject
  in writing.
- **UM/UIM operates as a contract claim** with a 6-year SOL
  under § 28-3-109, but the tort SOL controls the underlying
  injury claim.
- **Notice to UM/UIM carrier**: when suing an underinsured
  defendant, serve the UM/UIM carrier under § 56-7-1206(a)
  contemporaneously with serving the defendant; the carrier
  has the right to appear and defend.
- **Subrogation**: UM/UIM carrier's subrogation rights are
  governed by the policy + § 56-7-1208.
- **Stacking**: limited; check policy language and most-recent
  case law.

## Dog bites — § 44-8-413

Tennessee uses a **dual regime**:

- **Strict liability** if the dog was in a public place or on
  the dog owner's property where the injured person was lawfully
  present **and** the dog was not on a leash / not under
  reasonable control / had previously demonstrated dangerous
  propensities.
- **One-bite + negligence** otherwise — owner liable only on a
  showing of negligence or scienter.

Statutory residential carve-out at § 44-8-413(c) limits
strict liability where the bite occurs on a residential property.

## High-yield Tennessee PI checks

1. **What's the SOL?** Personal injury 1 year (§ 28-3-104);
   property damage 3 years (§ 28-3-105) — separate clocks.
   Criminal-conduct extension under § 28-3-104(a)(2)?
2. **Governmental defendant?** GTLA immunity-removal category
   (§§ 29-20-202 to -205) + $300k/$700k caps (§ 29-20-403) +
   shortened ~12-month SOL (§ 29-20-305) + **no jury**?
3. **Health-care liability?** 60-day pre-suit notice
   (§ 29-26-121) + certificate of good faith (§ 29-26-122) +
   3-year statute of repose (§ 29-26-116) not extended by
   notice + contiguous-state expert (§ 29-26-115)?
4. **Comparative fault?** Plaintiff under 50%? Non-parties at
   fault identified? Tenn. R. Civ. P. 8.03 non-party-fault
   plead?
5. **Caps?** Non-economic capped at $750k / $1M catastrophic
   under § 29-39-102; punitive capped at greater of $500k / 2x
   compensatory under § 29-39-104; *McClay* upheld both.
6. **Products case?** TPLA 10-year statute of repose under
   § 29-28-103 — runs from first purchase, not injury.
   Sealed-container retailer defense under § 29-28-106?
7. **Wrongful death?** § 20-5-106 survival; beneficiary order
   under § 20-5-107; *Jordan*-type emotional damages.
8. **Auto case?** UM/UIM offered? Notice to UM/UIM carrier
   under § 56-7-1206 contemporaneously with serving defendant?
   Property damage separate clock?

## Drafting checklist

- [ ] Confirm the **1-year SOL** is not running out within 30
      days — file an intent-to-sue letter to preserve evidence
      and statute if it is.
- [ ] If a governmental defendant is in the case, **draft to a
      GTLA removal category** and confirm the ~12-month clock
      and the caps.
- [ ] If health-care liability, **send pre-suit notice 60+
      days before filing** with HIPAA authorization; file
      certificate of good faith with the complaint.
- [ ] Plead **all non-parties at fault** under Tenn. R. Civ. P.
      8.03 or address defense's 8.03 amendment within 90 days.
- [ ] In the damages prayer, plead non-economic damages **up
      to the cap** — pleading above the cap is hazardous;
      consider citing § 29-39-102 directly.
- [ ] For punitive damages, plead the **§ 29-39-104(a)(7)
      exemption** if applicable; otherwise prepare for the
      automatic bifurcated trial.
- [ ] Auto case: file with **service to the UM/UIM carrier**
      under § 56-7-1206.
- [ ] If filing wrongful death, **identify statutory
      beneficiaries** with specificity per § 20-5-107.

## Composition

- For statewide format and caption: `tn-statewide-format`
- For Circuit / Chancery venue: `tn-davidson`, `tn-shelby`,
  `tn-knox`, `tn-hamilton`, `tn-county-courts`
- For ≤ $25k claims: `tn-general-sessions`
- For first responsive pleading: `tn-first-30-days`
- For drafting motions / declarations / orders: `tn-draft-motion`,
  `tn-draft-declaration`, `tn-draft-order`
- For SOL / pre-suit-notice / GTLA clocks: `tn-deadlines`
- For discovery: `tn-discovery`
- For overlap with employment torts (intentional infliction,
  assault by co-employee — workers'-comp exclusive-remedy
  bar): `tn-employment`
- For QC: `tn-quality-check`, `tn-fact-check`

## References

- `tn-law-references` — Tenn. Code Ann., Tenn. R. Civ. P., Tenn.
  R. Evid., and federal symlinks
- Tenn. Code Ann. § 28-3-104 / § 28-3-105 — SOLs
- Tenn. Code Ann. § 29-11-107 — fault apportionment
- Tenn. Code Ann. §§ 29-20-101 to -407 — GTLA
- Tenn. Code Ann. §§ 29-26-101 to -122 — HCLA
- Tenn. Code Ann. §§ 29-28-101 to -108 — TPLA
- Tenn. Code Ann. §§ 29-39-101 to -104 — 2011 tort-reform caps
- Tenn. Code Ann. § 20-5-106 et seq. — wrongful death
- Tenn. Code Ann. §§ 56-7-1201 to -1209 — UM/UIM
- Tenn. Code Ann. § 44-8-413 — dog bites
- *McIntyre v. Balentine*, 833 S.W.2d 52 (Tenn. 1992)
- *McClay v. Airport Management Services, LLC*, 596 S.W.3d 686
  (Tenn. 2020) — 2011 caps upheld
- *Coln v. City of Savannah*, 966 S.W.2d 34 (Tenn. 1998) — open
  and obvious
- *Hodges v. S.C. Toof & Co.*, 833 S.W.2d 896 (Tenn. 1992) —
  punitives standard
- *Jordan v. Baptist Three Rivers Hospital*, 984 S.W.2d 593
  (Tenn. 1999) — *Jordan* emotional damages in wrongful death
- *Stevens v. Hickman Community Health Care Services, Inc.*,
  418 S.W.3d 547 (Tenn. 2013) — HCLA pre-suit notice compliance
