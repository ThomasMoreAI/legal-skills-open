---
name: mi-employment-codearranger
title: Michigan Employment Law
description: 'Subject-matter bundle for Michigan employment matters: discrimination, harassment, retaliation, wage-and-hour, whistleblower, non-compete, and workers''-compensation exclusive remedy. Triggers include "Michigan employment discrimination", "Elliott-Larsen ELCRA MCL 37.2101", "PWDCRA MCL 37.1101", "MCL 15.361" whistleblower, "Michigan minimum wage", "MCL 408.471" Payment of Wages Act, "Mothering Justice", "MARA MCL 445.774a" non-compete, "MCL 418.131" workers'' comp exclusive remedy. Covers ELCRA (1+ employee; 2023 amendment adding sexual orientation/gender identity); PWDCRA; WPA (90-day SOL); Payment of Wages and Fringe Benefits Act; minimum wage and Earned Sick Time Act (as amended Feb. 21, 2025 by Mothering Justice); Toussaint legitimate-expectations at-will exception; MARA non-compete reasonableness; workers''-compensation exclusive remedy with intentional-tort exception.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-employment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Michigan Employment Law

> **NOT LEGAL ADVICE.** Michigan employment claims are
> deadline- and forum-sensitive, and several governing
> statutes changed recently. The Whistleblowers' Protection
> Act carries an unusually short **90-day** SOL; the minimum-
> wage and paid-sick-leave regimes were rewritten by the
> Michigan Supreme Court in *Mothering Justice* and then
> amended by the Legislature effective **February 21, 2025**,
> so current wage rates and sick-time mechanics are moving
> targets. Verify SOLs, employer-coverage thresholds, current
> wage/sick-time figures, and forum selection against the
> current MCL and the reference corpus before drafting, and
> consult a licensed Michigan attorney about your specific
> case.

Use this subject-matter bundle for Michigan employment civil
actions — discrimination/harassment/retaliation, unpaid wages,
whistleblower, non-compete enforcement, and tort-overlay claims
against the workers'-compensation exclusive remedy.

## At a glance

- **At-will baseline**, but the *Toussaint* **legitimate-
  expectations** doctrine and express-contract promises can
  convert at-will status to just-cause.
- **Broadest discrimination coverage in the country**: ELCRA
  reaches employers with **1 or more employees** (MCL 37.2201) —
  far below Title VII's 15.
- **Recently expanded protected classes**: per 2023 PA 6 (and
  *Rouch World, LLC v. Department of Civil Rights*, 510 Mich.
  398 (2022)), ELCRA expressly covers **sexual orientation and
  gender identity**.
- **Minimum wage + paid sick leave in flux**: the 2024
  *Mothering Justice* decision reinstated the original ballot-
  initiative minimum-wage and Earned Sick Time statutes
  effective Feb. 21, 2025; the Legislature amended both the same
  day. Treat all dollar/hour figures as **corpus-driven**.
- **Enforcement agencies**: Michigan Dept. of Civil Rights
  (MDCR) for ELCRA/PWDCRA; Michigan Dept. of Labor and Economic
  Opportunity (LEO) Wage and Hour Division for wage/sick-time
  claims; the Workers' Disability Compensation Agency / Board of
  Magistrates for workers'-comp; EEOC and U.S. DOL for the
  federal overlay.

## SOL catalog (the most-used)

| Claim | SOL | Citation |
|---|---|---|
| **ELCRA / PWDCRA** | **3 years** | MCL 600.5805; *Garg*, 472 Mich. 263 (2005) |
| **Whistleblowers' Protection Act** | **90 days** | MCL 15.363(1) |
| **Payment of Wages / Fringe Benefits Act** | **3 years** | MCL 408.481 et seq. |
| **Public-policy wrongful discharge** | **3 years** | MCL 600.5805 |
| **Breach of employment contract (incl. *Toussaint*)** | **6 years** | MCL 600.5807(9) |
| **Title VII / ADA / ADEA (federal in MI)** | **300 days** to EEOC (deferral state) | 42 U.S.C. § 2000e-5(e) |
| **FLSA / FMLA (federal)** | **2 yr / 3 yr** willful | 29 U.S.C. §§ 255, 2617(c) |

The **90-day WPA clock is the trap** — far shorter than the
3-year discrimination period and **not** tolled by an
administrative charge. Verify current day counts and tolling
carve-outs against the corpus (`mi-statutes-debt/` or the
canonical MCL where the corpus is stubbed).

## The principal Michigan statutes

### 1. Elliott-Larsen Civil Rights Act (ELCRA) — MCL 37.2101 et seq.

Michigan's core anti-discrimination statute and the most
plaintiff-friendly state civil-rights act in the country.

- **Coverage**: 1 or more employees — MCL 37.2201(a). No
  small-employer escape hatch.
- **Protected classes** (MCL 37.2202): religion, race, color,
  national origin, age, sex, **height, weight** (Michigan-
  distinctive — no federal analog), and marital status — plus
  **sexual orientation and gender identity or expression**, added
  by 2023 PA 6 as separate enumerated categories (not merely by
  redefining "sex"), codifying and extending *Rouch World, LLC v.
  Dep't of Civil Rights*, 510 Mich. 398 (2022). (Familial status
  is a protected class under MCL 37.2102's general declaration and
  in housing, but is not enumerated in the MCL 37.2202 employer
  list.)
- **Tracks**: complaint to MDCR / Michigan Civil Rights
  Commission under MCL 37.2602 **or** a direct Circuit Court
  civil action — exhaustion is **not** required; SOL is the
  general **3-year** personal-injury period (*Garg*).
- **Damages**: actual damages **with no statutory cap**, plus
  **exemplary damages** for injury to feelings, plus reasonable
  attorney's fees and costs to a prevailing plaintiff (MCL
  37.2802). Jury trial available.

### 2. Persons with Disabilities Civil Rights Act (PWDCRA) — MCL 37.1101 et seq.

Michigan's state disability-discrimination analog to the ADA;
1+ employee coverage, tracking ELCRA.

- **Disability** (MCL 37.1103): a determinable physical/mental
  characteristic that substantially limits a major life activity
  and is unrelated to job ability, plus perceived- and record-of
  prongs.
- **Reasonable accommodation**: required absent undue hardship;
  the employee must give **written notice** of the need within
  **182 days** under MCL 37.1210(18) — a Michigan-specific trap.
- **Remedies / SOL** track ELCRA (3 years; actual + exemplary +
  fees under MCL 37.1606).

### 3. Whistleblowers' Protection Act (WPA) — MCL 15.361 et seq.

Protects an employee who **reports or is about to report** a
suspected violation of law/regulation/rule to a **public body**,
or participates in a public-body investigation or hearing (MCL
15.362). Purely internal reports not "about to" reach a public
body fall outside the WPA (though they may support a
*Suchodolski*-style public-policy tort).

- **SOL**: **90 days** after the alleged violation — MCL
  15.363(1). A hard, short deadline.
- **Remedies**: injunctive relief, actual damages, or both;
  reinstatement, back pay, reasonable attorney + witness fees
  (MCL 15.363–15.364); plus a civil fine on the employer (MCL
  15.365).
- **Exclusivity caution**: where the WPA covers the conduct it
  is generally the **exclusive remedy**, displacing a parallel
  public-policy claim (*Dudewicz v. Norris-Schmid, Inc.*, 443
  Mich. 68 (1993), as later refined). Verify current case law.

### 4. Wages — Payment Act + Minimum Wage + Earned Sick Time

**Payment of Wages and Fringe Benefits Act — MCL 408.471 et seq.**
Wages due on regular paydays (MCL 408.472); on quit/discharge,
all earned wages due by the regularly scheduled payday — no
immediate-payment rule (MCL 408.475); no deduction without the
employee's **written consent** or statutory authority (MCL
408.477); fringe benefits payable per written policy/contract
(MCL 408.473). Enforce via LEO Wage and Hour or a private civil
action; **3-year** SOL.

**Improved Workforce Opportunity Wage Act (minimum wage) — MCL 408.931 et seq.**

> **VERIFY — recently changed.** In *Mothering Justice v.
> Attorney General*, 515 Mich. ___ (2024), the Michigan Supreme
> Court struck down the Legislature's 2018 "adopt-and-amend"
> maneuver and reinstated the original ballot-initiative minimum-
> wage and sick-time statutes effective **February 21, 2025**.
> The Legislature then amended both statutes the same day
> (2025 PA 1 / 2025 PA 2). The amended minimum-wage schedule is
> **$12.48 (eff. Feb. 21, 2025) → $13.73 (Jan. 1, 2026) → $15.00
> (Jan. 1, 2027)**, with later years indexed for inflation, and a
> revised tipped-credit phase-down.

- **Confirm the current rate, tipped-credit percentage, and
  next scheduled increase against the corpus** — these figures
  drift annually and were re-set by the 2025 amendments. Point
  to `mi-statutes-debt/` (the IWOWA MCL 408.931 chapter) or the
  LEO Wage and Hour minimum-wage page for the live number.
- **Overtime**: Michigan tracks the FLSA 40-hour threshold; the
  state has no separate daily-overtime rule.

**Earned Sick Time Act (ESTA) — reinstated by *Mothering Justice***

> **VERIFY — recently changed.** ESTA (the reinstated ballot
> initiative, as amended Feb. 21, 2025) replaced the prior Paid
> Medical Leave Act. General rule: accrual of **1 hour of paid
> sick time per 30 hours worked**. Annual usage may be capped
> (the 2025 amendment set roughly **72 hours** for larger
> employers and **40 hours** for small businesses), with a
> small-business exemption phased through **Oct. 1, 2025**.

- **Confirm the current accrual rate, usage cap, small-business
  threshold, frontloading option, and effective dates against
  the corpus** — every figure here was set by the 2025
  amendments and is subject to change.

### 5. Workers' Disability Compensation — MCL 418.101 et seq.

Workers'-comp is the **exclusive remedy** for personal injury or
death arising out of and in the course of employment — **MCL
418.131(1)** — adjudicated by the **Board of Magistrates** within
the Workers' Disability Compensation Agency (review to the
Michigan Compensation Appellate Commission, then the Court of
Appeals), **not** in Circuit Court. The bar extends to co-
employees acting in the course of employment. The narrow
**intentional-tort exception** (MCL 418.131(1)) lets a tort suit
proceed only where the employer had **actual knowledge** an
injury was certain to occur and **willfully disregarded** it;
*Travis v. Dreis & Krump Mfg. Co.*, 453 Mich. 149 (1996) — mere
negligence, recklessness, or knowledge of a general risk is
insufficient.

## At-will employment and its exceptions

Michigan is an at-will state, with three exceptions: (1)
**express contract** — a written or oral just-cause/for-cause
promise; (2) the **legitimate-expectations (*Toussaint*)
doctrine** — *Toussaint v. Blue Cross & Blue Shield of Michigan*,
408 Mich. 579 (1980): employer policy statements (handbooks,
manuals, oral assurances) can create an enforceable just-cause
expectation absent a formal contract, routinely defeated by a
conspicuous **at-will disclaimer** (*Lytle v. Malady*, 458 Mich.
153 (1998)); and (3) the **public-policy exception** — discharge
for refusing to break the law, exercising a statutory right, or
reporting a violation (where not displaced by the WPA),
*Suchodolski v. Mich. Consol. Gas Co.*, 412 Mich. 692 (1982). A
*Toussaint*/express-contract claim sounds in **contract** (6-year
SOL, MCL 600.5807(9)); the public-policy tort sounds in tort
(3-year SOL).

## Non-compete and restrictive covenants — MARA

Non-compete enforceability is governed by the **Michigan
Antitrust Reform Act (MARA)** at **MCL 445.774a**, not common
law alone. An employer may obtain an agreement protecting
"reasonable competitive business interests" that is reasonable
as to **duration**, **geographical area**, and **type of
employment / line of business** (MCL 445.774a(1)). If
unreasonable in any respect, "a court **may limit the agreement
to render it reasonable** ... and specifically enforce the
agreement as limited" — Michigan courts thus **blue-pencil /
reform** overbroad covenants rather than voiding them. A bare
desire to suppress ordinary competition is not protectable.
Trade-secret claims track the **Michigan Uniform Trade Secrets
Act (MUTSA)**, MCL 445.1901 et seq. (see `mi-commercial-
disputes`). Watch current FTC non-compete rulemaking and confirm
enforceability against the live MCL.

## Federal overlay — the deferral-state framework

The MDCR is an EEOC **work-share agency**: a charge filed with
either MDCR or EEOC is dual-filed, and the federal **300-day**
SOL applies to Title VII / ADA / ADEA / GINA (rather than the
180-day non-deferral baseline). Each federal statute has a state
parallel — Title VII (15+) → ELCRA (1+); ADA (15+) → PWDCRA (1+);
ADEA (20+) → ELCRA age provision (1+); *Bostock* sexual-
orientation/gender-identity → ELCRA (2023 PA 6 / *Rouch World*) —
except GINA and the FMLA, which have no state analog. ELCRA's
**3-year** judicial SOL and the **90-day** EEOC right-to-sue
clock are separate, independently-running deadlines.

## Forum strategy

| Claim | Forum | Notes |
|---|---|---|
| ELCRA / PWDCRA | **Circuit Court** | General jurisdiction; jury trial; no exhaustion required |
| WPA | Circuit Court | 90-day SOL — calendar immediately |
| Public-policy wrongful discharge | Circuit Court | 3-year tort SOL |
| Wage / fringe-benefit claim | LEO Wage & Hour complaint **or** Circuit / District Court (District if ≤ $25,000) | 3-year SOL |
| Minimum wage / ESTA | LEO Wage & Hour **or** civil action | Confirm current private-action mechanics in corpus |
| Non-compete enforcement | **Circuit Court** | TRO / preliminary injunction is the standard ask; verified complaint + bond (MCR 3.310) |
| Workers' Compensation | **Board of Magistrates (WDCA)** | Administrative; **not** Circuit Court |
| Federal claims (Title VII / FLSA / FMLA) | **U.S. District Court** (E.D. or W.D. Mich.) | Removal possible; supplemental jurisdiction over parallel ELCRA claim |

## Drafting checklist

- [ ] Calendar the **WPA 90-day SOL** the moment a whistleblower
      claim is on the table — it is the shortest deadline in the
      bundle and is not tolled by an agency filing.
- [ ] Confirm employer-coverage thresholds — ELCRA/PWDCRA reach
      **1+ employee**; do not assume a Title VII-style 15-employee
      floor applies.
- [ ] For discrimination claims, decide **MDCR vs. direct Circuit
      Court suit** — exhaustion is not required; the 3-year
      judicial clock runs from the discriminatory act (*Garg*).
- [ ] For PWDCRA accommodation claims, confirm the employee gave
      **written notice within 182 days** (MCL 37.1210(18)).
- [ ] For minimum-wage / ESTA claims, **pull the current rate,
      accrual rate, usage cap, and small-business threshold from
      the corpus** — these were re-set by *Mothering Justice* and
      the Feb. 21, 2025 amendments and change over time.
- [ ] For *Toussaint* claims, plead in **contract** (6-year SOL)
      and identify the specific policy statement / oral assurance;
      anticipate an at-will-disclaimer defense.
- [ ] For non-compete enforcement, plead the **MARA** reasonableness
      factors (duration / geography / line of business) and the
      protectable interest; for defense, identify which factor
      fails and note the court's **blue-pencil** reform power.
- [ ] For workers'-comp tort-overlay suits, plead the narrow
      **intentional-tort** standard (actual knowledge + willful
      disregard; *Travis*) — ordinary negligence is barred by
      MCL 418.131(1).

## Damages and remedies

**ELCRA / PWDCRA**: actual damages (no cap) + exemplary damages
for injury to feelings + mandatory fees to a prevailing plaintiff
(MCL 37.2802 / 37.1606). **WPA**: actual damages + reinstatement
+ reasonable attorney/witness fees (MCL 15.364). **Wages Act**:
unpaid wages/fringe benefits per statute or contract.
**Public-policy tort**: compensatory + punitive (American Rule on
fees). **FLSA**: unpaid wages + 100% liquidated (good-faith
defense) + mandatory fees (29 U.S.C. § 216(b)). **Title VII**:
compensatory + punitive on a size-graded cap + mandatory fees.

## Composition

- For statewide format and caption: `mi-statewide-format`
- For Circuit Court venue mechanics: the appropriate county
  venue skill or `mi-circuit-courts`
- For first responsive pleading: `mi-first-30-days`
- For drafting motions / declarations / orders: `mi-draft-motion`,
  `mi-draft-declaration`, `mi-draft-order`
- For SOL / limitations arithmetic (esp. the WPA 90-day clock):
  `mi-deadlines`
- For commercial / trade-secret overlap (MUTSA, fiduciary duty,
  tortious interference): `mi-commercial-disputes`
- For garnishment of an unpaid-wage judgment: `mi-post-judgment`

## References

- `mi-law-references` — MCL, Michigan Court Rules, and
  federal-debt-laws (FLSA / ADA / Title VII overlay) symlinked
  from `claude-legal-federal-laws`
- MCL ch. 37 (ELCRA § 37.2101; PWDCRA § 37.1101); ch. 15 (WPA
  § 15.361); ch. 408 (Wages Act § 408.471; IWOWA minimum wage
  § 408.931; Earned Sick Time Act); ch. 445 (MARA § 445.774a;
  MUTSA § 445.1901); ch. 418 (Worker's Disability Compensation —
  exclusive remedy + intentional-tort exception § 418.131)
- *Rouch World*, 510 Mich. 398 (2022); *Mothering Justice v.
  Attorney General*, 515 Mich. ___ (2024); *Toussaint*, 408
  Mich. 579 (1980); *Lytle v. Malady*, 458 Mich. 153 (1998);
  *Garg*, 472 Mich. 263 (2005); *Travis v. Dreis & Krump*, 453
  Mich. 149 (1996); *Suchodolski*, 412 Mich. 692 (1982)
- Michigan Dept. of Civil Rights: https://www.michigan.gov/mdcr
- LEO Wage and Hour: https://www.michigan.gov/leo/bureaus-agencies/ber/wage-and-hour
