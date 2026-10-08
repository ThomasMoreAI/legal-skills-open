---
name: tn-employment-codearranger
title: Tennessee Employment Law
description: Subject-matter bundle for Tennessee employment matters — discrimination, harassment, retaliation, wage-and-hour, whistleblower, non-compete, and workers'-compensation. Covers THRA (§ 4-21-101 et seq.; 8+ employee; 1-year judicial SOL); TDA (§ 8-50-103); TPPA whistleblower (§ 50-1-304) with strict "sole reason" element per Williams v. City of Burns; Wage Regulation Act (§ 50-2-101 et seq.; no state minimum — FLSA $7.25; treble damages on willful nonpayment); right-to-work (§ 50-1-201 et seq.; constitutionalized Nov. 2022); non-compete reasonableness per Murfreesboro Medical v. Udom; at-will employment (Stein v. Davidson Hotel); workers'-compensation exclusive remedy (§ 50-6-108) with post-7/1/14 Court of Workers' Compensation Claims forum split (§ 50-6-237).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-employment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Tennessee Employment Law

> **NOT LEGAL ADVICE.** Tennessee employment claims are
> short-fused and forum-strategy-sensitive. The THRA 1-year
> judicial SOL is shorter than most peer states; the TPPA's
> "sole reason" element is unusually narrow; the workers'-
> compensation forum split between pre-7/1/14 Chancery
> jurisdiction and post-7/1/14 Court of Workers' Compensation
> Claims jurisdiction trips even experienced practitioners.
> Verify SOLs, employer-coverage thresholds, and forum
> selection against the current Tenn. Code Ann. before
> drafting, and consult a licensed Tennessee attorney about
> your specific case.

Use this subject-matter bundle for Tennessee employment civil
actions — discrimination/harassment/retaliation, unpaid wages,
whistleblower, non-compete enforcement, and tort-overlay claims
against the workers'-compensation exclusive remedy.

## At a glance

- **At-will baseline**: Tennessee is firmly an at-will state.
  *Stein v. Davidson Hotel*, 945 S.W.2d 714 (Tenn. 1997).
  Public-policy exception is narrow and largely codified in
  the TPPA.
- **Right-to-work**: Constitutionalized Nov. 2022 (Tenn. Const.
  art. XI § 21); previously statutory at Tenn. Code Ann.
  § 50-1-201 et seq. Compelled union-membership agreements
  are void.
- **No state minimum wage**: FLSA's $7.25/hr federal floor
  controls. Tennessee has no state overtime law; FLSA's
  40-hour threshold applies.
- **Enforcement agencies**: Tennessee Human Rights Commission
  (THRC) for THRA; Tennessee Department of Labor & Workforce
  Development (Wage Regulations Division) for wage claims; the
  **Court of Workers' Compensation Claims (CWCC)** for post-
  7/1/14 workers'-comp matters under § 50-6-237; EEOC and DOL
  for the federal overlay.

## SOL catalog (the most-used)

| Claim | SOL | Citation |
|---|---|---|
| **THRA (judicial)** | **1 year** from discriminatory act | Tenn. Code Ann. § 4-21-311(d) |
| **THRA (administrative)** | **180 days** to THRC | Tenn. Code Ann. § 4-21-302(a) |
| **TDA (state disability)** | tracks THRA — 1 year | § 8-50-103 + § 4-21-311 |
| **TPPA whistleblower** | **1 year** (personal action) | Tenn. Code Ann. § 28-3-104(a)(1) |
| **Common-law retaliatory discharge** | **1 year** | § 28-3-104(a)(1) |
| **Tennessee Wage Regulation Act (private claim)** | **1 year** treated as personal action; **6 years** if pleaded as breach of contract | § 28-3-104 / § 28-3-109 |
| **Workers' Compensation (PTD/PPD claim to CWCC)** | **1 year** from injury or last voluntary benefit | Tenn. Code Ann. § 50-6-203 |
| **Title VII / ADA / ADEA (federal in TN)** | **300 days** to EEOC (deferral state via THRC work-share) | 42 U.S.C. § 2000e-5(e); 29 U.S.C. § 626(d) |
| **FLSA (federal)** | **2 years** / **3 years** willful | 29 U.S.C. § 255 |
| **FMLA (federal)** | **2 years** / **3 years** willful | 29 U.S.C. § 2617(c) |

Current SOL day counts and any one-time tolling carve-outs
should be verified against the current `tn-statutes-debt/Tenn-Code-T28-Ch3.md`
and `tn-statutes-debt/Tenn-Code-T4-Ch21.md` corpus files (or the
canonical Tenn. Code Ann. where the corpus is stubbed).

## The five principal Tennessee statutes

### 1. Tennessee Human Rights Act (THRA) — Tenn. Code Ann. § 4-21-101 et seq.

The THRA mirrors federal Title VII / ADEA / ADA in substantive
prohibitions (race, color, religion, sex, age 40+, national
origin, retaliation) but operates on a **lower employer-size
floor and a shorter judicial SOL**.

- **Coverage**: 8+ employees under § 4-21-102(5) (compare
  Title VII's 15+ and ADEA's 20+).
- **Administrative complaint**: 180 days to the Tennessee
  Human Rights Commission under § 4-21-302(a). Filing with
  THRC starts an investigative track; the parallel federal
  charge is filed via THRC's work-share with the EEOC.
- **Judicial complaint**: 1 year from the discriminatory act
  under § 4-21-311(d). The judicial track is **independent of
  the administrative track**; filing in Chancery / Circuit
  does **not** require exhaustion at THRC, but filing at THRC
  and litigating to a final order may bar a subsequent
  judicial action (election of remedies). See
  *Hoyle v. NAEYC*, 2010 Tenn. App. LEXIS 122.
- **Damages**: compensatory; punitives available; mandatory
  attorney's fees on prevailing-plaintiff under § 4-21-311(b).
- **Jury trial**: yes under § 4-21-311(a).
- **Forum**: Chancery or Circuit (concurrent subject-matter
  jurisdiction); General Sessions has no THRA jurisdiction.

### 2. Tennessee Disability Act (TDA) — Tenn. Code Ann. § 8-50-103

State analog to the ADA with the same 8+ employer-coverage
threshold as the THRA. Procedural framework runs through
§ 4-21-311 (the THRA's enforcement section); SOL and remedies
track the THRA.

The 2024 amendment confirmed coverage of "associational
discrimination" claims (adverse action against an employee
because of the disability of a family member).

### 3. Tennessee Public Protection Act (TPPA) — Tenn. Code Ann. § 50-1-304

The TPPA is the principal **statutory whistleblower** tool.
It is *not* a generic anti-retaliation statute — it requires:

1. The employee **refused to participate in** or **refused to
   remain silent about** an illegal activity;
2. The illegal activity was a violation of statute, regulation,
   or rule;
3. Discharge **solely** because of the protected activity
   (the "**sole reason**" element).

The "sole reason" element is critical and has defeated many
TPPA claims. *Williams v. City of Burns*, 465 S.W.3d 96 (Tenn.
2015), modified the burden-shifting framework but retained the
sole-causation requirement: the employee must show the
protected activity was the only reason, with mixed-motive
defenses unavailable to plaintiffs.

The TPPA largely codifies the narrow common-law retaliatory-
discharge tort recognized in *Chism v. Mid-South Milling Co.*,
762 S.W.2d 552 (Tenn. 1988). For protected activity falling
**outside** the TPPA (e.g., refusal to do something legal but
unwise; reporting that is not a clear statutory violation), the
common-law tort may still be available but the **public-policy**
hook must be tied to a constitution, statute, or regulation.
*Crews v. Buckman Labs. Int'l, Inc.*, 78 S.W.3d 852 (Tenn.
2002), recognized the right of in-house counsel to bring such a
claim.

The TPPA also protects **lawful off-duty tobacco use** under
§ 50-1-304(d)(3) — Tennessee's "smoker-protection" provision.

### 4. Tennessee Wage Regulation Act — Tenn. Code Ann. § 50-2-101 et seq.

- **Frequency of pay (§ 50-2-103)**: private employers with
  5+ employees must pay **semi-monthly**; certain industries
  may pay monthly. The first half of the month's wages must
  be paid by the 20th of the same month; the second half by
  the 5th of the succeeding month.
- **Final wages**: must be paid by the next regular payday
  following separation **or within 21 days**, whichever is
  later (§ 50-2-103(g)). Tennessee does **not** require
  immediate payment on discharge.
- **Treble damages on willful nonpayment**: the
  Commissioner may assess civil penalties; an employee
  bringing a private action may recover the unpaid wages
  plus reasonable attorney's fees and, where the employer
  acted willfully, statutory liquidated damages. See
  § 50-2-101(a)(2).
- **No state minimum wage**: FLSA $7.25/hr federal floor
  controls. § 50-2-201 expressly does not set a state
  minimum.

For unpaid-wage claims pleaded as breach of contract the
**6-year SOL at § 28-3-109** applies; for the bare statutory
remedy treat the SOL as **1 year** under § 28-3-104.

### 5. Workers' Compensation — Tenn. Code Ann. § 50-6-101 et seq.

Tennessee's workers'-compensation regime is the **exclusive
remedy** for accidental injuries arising out of and in the
course of employment (§ 50-6-108). The intentional-tort
carve-out is narrow — the employer must have acted with
**actual intent** to injure, not mere knowledge of risk;
*Valencia v. Freeland & Lemm Constr. Co.*, 108 S.W.3d 239
(Tenn. 2003).

**Critical forum split** (post-2013 reform):

- **Injuries on or after July 1, 2014**: adjudicated by the
  **Court of Workers' Compensation Claims (CWCC)** under
  § 50-6-237 — an administrative trial court within the
  Bureau of Workers' Compensation, with appeals to the
  Workers' Compensation Appeals Board and ultimately the
  Tennessee Supreme Court.
- **Injuries before July 1, 2014**: adjudicated by the
  **Chancery Court** of the appropriate county.

Petitions for Benefit Determination (PBDs) and Petitions for
Benefit Review (PBRs) drive the CWCC track; the BWC
mediation step (Mediation and Ombudsman Services of
Tennessee — MOST) is required before judicial intervention.

The **exclusive-remedy bar** also limits tort suits against
**co-employees** (§ 50-6-108(b)), with a narrow carve-out
for willful injury.

## Right-to-work and union mechanics

- Tennessee is a **right-to-work** state. Compelled union-
  membership agreements are void under Tenn. Code Ann.
  § 50-1-201 et seq. and, since the November 2022
  ratification of Amendment 1, under **Tenn. Const. art.
  XI § 21**.
- Constitutionalization elevated the protection beyond
  ordinary statutory repeal; legislative weakening of the
  protection now requires a constitutional amendment.
- Right-to-work does **not** bar collective bargaining or
  union recognition — only compelled membership as a
  condition of employment.

## Non-compete and restrictive covenants

Tennessee has **no statewide salary-threshold reform**
(contrast Washington's RCW 49.62 and California's near-total
ban). Non-compete enforceability is governed by **common law**
under *Murfreesboro Medical Clinic, P.A. v. Udom*, 166 S.W.3d
674 (Tenn. 2005) — the **reasonableness test**:

1. **Protectable interest** — confidential information,
   trade secrets, customer relationships, specialized
   training. Mere desire to suppress competition is not
   protectable.
2. **Reasonable in time** — typically 1–2 years; longer
   periods require a strong showing of necessity.
3. **Reasonable in geographic scope** — tied to the
   territory where the employer actually competes.
4. **Reasonable as to scope of restricted activity** —
   restrictions on activities the employee did not perform
   for the employer are vulnerable.

The court applies a **rule of reason** and may **blue-pencil**
or "reasonably alter" an overbroad covenant rather than
voiding it entirely — *Allright Auto Parks v. Berry*, 219
Tenn. 280 (1966) — though aggressive judicial rewriting is
disfavored.

**Physician non-competes** are independently regulated by
**Tenn. Code Ann. § 63-1-148**, which caps duration and
limits geographic scope; non-conforming physician non-
competes are unenforceable.

**Trade-secret claims** track the **Tennessee Uniform Trade
Secrets Act (TUTSA)** at § 47-25-1701 et seq. — see
`tn-commercial-disputes` for litigation framework.

## Federal overlay — the deferral-state framework

The THRC is an EEOC **work-share agency**. A complaint filed
with either THRC or EEOC is dual-filed, and the federal
**300-day** SOL applies to Title VII / ADA / ADEA / GINA in
Tennessee (rather than the 180-day non-deferral baseline).

| Claim | Federal track | TN parallel |
|---|---|---|
| Race/sex/religion/national origin | Title VII (15+) | THRA (8+) |
| Disability | ADA (15+) | TDA (8+) |
| Age 40+ | ADEA (20+) | THRA age provision (8+) |
| Pregnancy | PDA / PWFA | THRA sex |
| Genetic info | GINA | (no state analog) |
| Equal pay | EPA / Title VII | THRA |
| FMLA | FMLA (50+ in 75-mi) | (no state analog) |

The **5-year THRC charge** and the federal **180-/300-day
EEOC** clocks run independently for the substantive merits
window — but the THRA 1-year **judicial** SOL is a hard
deadline once a plaintiff elects the judicial track.

## Forum strategy

| Claim | Forum | Notes |
|---|---|---|
| THRA / TDA | Chancery or Circuit | Concurrent; Chancery often preferred for equitable relief (reinstatement, injunction) |
| TPPA / common-law retaliatory discharge | Chancery or Circuit | Jury trial available; § 50-1-304(d) |
| Wage Regulation Act | Chancery or Circuit; **General Sessions** if amount in controversy is ≤ $25,000 | General Sessions allows the small claim track + 10-day de novo appeal |
| Non-compete enforcement | **Chancery** (TRO/preliminary injunction is the standard ask) | Equity forum; verified complaint + bond |
| Workers' Compensation (≥ 7/1/14 injury) | **Court of Workers' Compensation Claims** | Administrative trial court; PBD/PBR; mediation required |
| Workers' Compensation (< 7/1/14 injury) | **Chancery** of the injury / residence / employer county | Legacy regime |
| Federal claims (Title VII / FLSA / FMLA) | **U.S. District Court** (Eastern, Middle, or Western District of Tennessee) | Removal possible from state court if federal cause of action pleaded; supplemental jurisdiction for parallel THRA claim |

## Drafting checklist

- [ ] Verify employer-size coverage threshold for each pleaded
      statute (THRA 8+, Title VII 15+, ADEA 20+, FMLA 50+
      within 75 miles).
- [ ] Confirm the **THRA 1-year judicial SOL** — calendar from
      the last discriminatory act (or last act in a continuing
      violation; *Booker v. Boeing Co.*, 188 S.W.3d 639 (Tenn.
      2006)).
- [ ] If filing a federal Title VII / ADA / ADEA charge first,
      preserve the **EEOC Right-to-Sue 90-day** clock and the
      independent THRA 1-year clock — they run **separately**.
- [ ] For TPPA: plead the **sole-causation** element
      affirmatively and identify the **specific statute,
      regulation, or rule** the employer was violating.
- [ ] For wage claims pleaded under § 50-2-101 alone, treat the
      SOL as 1 year; for breach-of-employment-contract claims
      use the **6-year SOL** at § 28-3-109 and plead the
      contract elements.
- [ ] For workers'-comp matters: confirm the injury date — pre-
      vs. post-July 1, 2014 — and route to Chancery or CWCC
      accordingly; **do not file the post-2014 claim in
      Chancery**.
- [ ] For non-compete enforcement: verified complaint + motion
      for TRO + bond (Tenn. R. Civ. P. 65.04); plead the
      *Udom* factors; identify the **protectable interest**
      with specificity.
- [ ] For non-compete defense: identify which *Udom* factor
      fails; consider whether the **physician-specific**
      § 63-1-148 cap applies.

## Damages and remedies

| Statute | Compensatory | Punitive | Liquidated / multiplier | Attorney's fees |
|---|---|---|---|---|
| THRA / TDA | Yes (no cap) | Yes (no cap) | — | Mandatory to prevailing plaintiff (§ 4-21-311(b)) |
| TPPA | Yes | Yes | — | Discretionary (§ 50-1-304(d)(2)) |
| Wage Reg. Act | Unpaid wages | — | Liquidated damages where willful | Reasonable attorney's fees (§ 50-2-101) |
| Common-law retaliatory discharge | Yes | Yes (heightened *Chism* showing) | — | American Rule |
| FLSA | Unpaid wages | — | Liquidated 100% (good-faith defense) | Mandatory under 29 U.S.C. § 216(b) |
| Title VII | Yes (capped sliding by size) | Yes (capped) | — | Mandatory to prevailing plaintiff |

## Composition

- For statewide format and caption: `tn-statewide-format`
- For Chancery / Circuit venue mechanics: `tn-davidson`,
  `tn-shelby`, `tn-knox`, `tn-hamilton`, or `tn-county-courts`
- For General Sessions wage-claim track (≤ $25k): `tn-general-sessions`
- For first responsive pleading: `tn-first-30-days`
- For drafting motions / declarations / orders: `tn-draft-motion`,
  `tn-draft-declaration`, `tn-draft-order`
- For SOL/limitations arithmetic: `tn-deadlines`
- For commercial / trade-secret overlap (TUTSA, fiduciary
  duty, tortious interference): `tn-commercial-disputes`
- For consumer-debt overlap (garnishment of unpaid-wage
  judgments): `tn-consumer-debt` + `tn-post-judgment`

## References

- `tn-law-references` — Tenn. Code Ann., Tenn. R. Civ. P., and
  federal-debt-laws (FLSA / ADA / Title VII overlay) symlinked
  from `claude-legal-federal-laws`
- Tenn. Code Ann. Title 4 ch. 21 (THRA — when corpus is
  populated)
- Tenn. Code Ann. Title 50 chs. 1 (TPPA / right-to-work),
  2 (Wage Regulation), 6 (Workers' Comp), 9 (Drug-Free
  Workplace)
- Tenn. Code Ann. Title 8 ch. 50 (TDA)
- *Murfreesboro Medical Clinic, P.A. v. Udom*, 166 S.W.3d 674
  (Tenn. 2005)
- *Williams v. City of Burns*, 465 S.W.3d 96 (Tenn. 2015)
- *Stein v. Davidson Hotel Co.*, 945 S.W.2d 714 (Tenn. 1997)
- *Chism v. Mid-South Milling Co.*, 762 S.W.2d 552 (Tenn. 1988)
- *Crews v. Buckman Labs. Int'l, Inc.*, 78 S.W.3d 852 (Tenn. 2002)
- *Valencia v. Freeland & Lemm Constr. Co.*, 108 S.W.3d 239
  (Tenn. 2003)
- Court of Workers' Compensation Claims:
  https://www.tn.gov/workforce/injuries-at-work/court-of-workers--compensation-claims.html
- Tennessee Human Rights Commission: https://www.tn.gov/humanrights.html
