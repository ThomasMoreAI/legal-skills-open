---
name: wa-employment-codearranger
title: Washington Employment Law — Subject-Matter Bundle
description: 'Use when handling a Washington employment matter — wage-and-hour claims, wage payment, WLAD (RCW 49.60) with no damages cap and mandatory attorney''s fees, Paid Sick Leave, PFML (RCW 50A), Equal Pay Opportunity Act, non-compete reform (RCW 49.62) invalidating non-competes below COL-adjusted salary threshold, and L&I-exclusive workers'' compensation (RCW 51) with narrow intentional-injury carve-out. Substantive framework: RCW Title 49 (Labor), Title 50A (PFML), Title 51 (Workers'' Comp). Triggers include "Washington employment", "wage theft", "WLAD", "RCW 49.60", "Paid Sick Leave", "PFML", "non-compete", "RCW 49.62", "workers compensation", "discrimination".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-employment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Washington Employment Law — Subject-Matter Bundle

> **NOT LEGAL ADVICE.** Employment statutes are amended
> frequently — minimum wage adjusts annually (Jan 1); PFML
> premium rates adjust annually; non-compete salary
> threshold adjusts annually for COL. This skill names the
> controlling chapters and describes doctrinal frameworks;
> **current dollar thresholds, damages multipliers,
> employer-coverage thresholds, and SOL day counts live in
> the references corpus** at `wa-law-references/
> references/wa-rcw-debt/`. Verify before relying on any
> figure.

## At a glance

- **Substantive code**: RCW Title 49 (Labor) +
  RCW Title 50A (PFML) + RCW Title 51 (Industrial
  Insurance / Workers' Comp)
- **Enforcement agencies**: WA Dept of Labor & Industries
  (L&I) for wage/hour + workers' comp; Washington State
  Human Rights Commission (WSHRC) for WLAD; EEOC federal
  overlay
- **WLAD breadth**: covers smaller employers than federal
  Title VII; has no statutory damages cap; mandates
  attorney's fees for prevailing plaintiffs

## Chapter pointers

| Topic | Chapter | Reference file |
|---|---|---|
| Industrial welfare (hours/conditions; family-care leave) | RCW 49.12 | `RCW-49_12.md` |
| Minimum Wage Act | RCW 49.46 | `RCW-49_46.md` |
| Wage payment + collection | RCW 49.48 | `RCW-49_48.md` |
| Wage deductions + rebates | RCW 49.52 | `RCW-49_52.md` |
| Equal Pay Opportunity Act | RCW 49.58 | (see corpus) |
| WLAD (anti-discrimination) | RCW 49.60 | `RCW-49_60.md` |
| Non-compete reform | RCW 49.62 | `RCW-49_62.md` |
| Paid Family and Medical Leave (PFML) | RCW 50A | (see corpus) |
| Industrial Insurance (workers' comp) | RCW 51.04 | `RCW-51_04.md` |
| Whistleblower (public-sector) | RCW 42.40 / 42.41 | (see corpus) |

For minimum-wage current rate, overtime threshold,
employer-size coverage threshold, damages multipliers,
WLAD protected-class enumeration, non-compete salary
threshold, and the L&I intentional-injury carve-out
standard, **read the relevant chapter file**.

## Minimum wage + overtime — doctrinal framework

Washington has a statewide minimum wage with annual
COL-indexed adjustment (effective Jan 1 each year).
Several jurisdictions (notably Seattle and SeaTac) have
higher local minimums. Washington has **no tip credit**
— tipped employees get the full minimum wage. Overtime
follows the 1.5x-over-40-hours rule. Willful violations
unlock a damages multiplier + attorney's fees.

For the current minimum, the overtime threshold, the
exempt-employee salary tests, and the damages multiplier,
see `RCW-49_46.md`.

## Wage payment + collection — doctrinal framework

Wage payment is governed at:

- **RCW 49.48** — payment timing, final paychecks,
  attorney's-fee provisions
- **RCW 49.52** — wage deductions, rebates, and the
  damages remedy for willful withholding / unauthorized
  deductions

Final paychecks are due by the end of the pay period
following termination. Willful withholding or
unauthorized deduction unlocks a damages multiplier; the
provision is in the **deductions chapter** (RCW 49.52),
not the payment-timing chapter. For the multiplier, the
unauthorized-deduction definition, and the criminal-
penalty provision, see `RCW-49_52.md`.

## WLAD — anti-discrimination doctrinal framework

### Coverage

WLAD applies to employers smaller than the federal Title
VII threshold — material practical difference for
plaintiffs working for small businesses. The chapter
also covers public accommodation, real estate, credit,
and insurance. See `RCW-49_60.md` for the current
employee-count threshold.

### Protected classes

Washington's list is broader than federal Title VII —
notably including marital status, sexual orientation,
gender identity / expression, and disability with a
broader definition than the ADA. See `RCW-49_60.md` for
the current enumeration.

### Damages

- No statutory cap
- Mandatory attorney's fees for prevailing plaintiff
- Recoverable: back pay, front pay, emotional distress,
  punitive damages where authorized

### Procedural path

- WSHRC administrative complaint, OR
- Direct civil action — no exhaustion requirement (unlike
  Title VII's EEOC charge)

The WLAD-via-direct-action SOL is the general personal-
injury SOL per *Antonius v. King County*. WSHRC filing
window is shorter.

### Hostile work environment

WA follows the Meritor / Harris federal framework with
emphasis on severe-OR-pervasive (disjunctive). Cited:
*Loeffelholz v. Univ. of Wash.*

### Retaliation

RCW 49.60.210 prohibits retaliation for opposing
WLAD-prohibited practice, filing complaint, participating
in investigation. Causation = "substantial factor" — more
plaintiff-friendly than federal Title VII (per *Allison
v. Hous. Auth. of City of Seattle*).

## Paid Sick Leave — overview

Statewide paid-sick-leave law in effect since 2018.
Accrual rate, use rules (own / family illness; safe leave;
school closures), carryover minimum, and retaliation
prohibition all set by statute. See the RCW 49.46
amendments.

## Paid Family and Medical Leave (PFML) — overview

PFML at RCW Title 50A (effective 2020) provides paid
family + medical leave funded by payroll premium (employee
+ employer share). Wage replacement is income-scaled with
a cap. Job-protected for qualifying employees. Premium
rate and benefit cap adjust annually.

For current premium rates, benefit cap, and eligibility
thresholds, consult RCW Title 50A documentation /
Employment Security Department guidance.

## Family Care Act — RCW 49.12.265-295

A separate statute (distinct from the repealed Family
Leave Act at RCW 49.78) requires employers to allow use
of accrued sick / vacation leave for family-member
illness. See `RCW-49_12.md`.

## Equal Pay Opportunity Act — RCW 49.58

Bars salary-history inquiries, requires pay-scale +
benefits disclosure in postings for employers above a
threshold, bars sex-based pay differentials for similar
work absent legitimate factors, and provides actual-plus-
liquidated damages + attorney's fees on prevailing-
plaintiff claims. For the current employer-size threshold
for posting requirements and the damages multiplier, see
the chapter file.

## Non-compete reform — RCW 49.62

The 2020 non-compete reform invalidates non-competes
below an annual-COL-adjusted salary threshold (separate
threshold for independent contractors). Other features:

- Mandatory disclosure at offer (or independent
  consideration required)
- Statutory maximum duration presumed reasonable
- Layoff-trigger invalidation when severance falls short
- Damages-for-attempted-enforcement provision with
  treble + attorney's fees

For the current salary threshold (employees and
independent contractors), maximum duration, and damages-
for-enforcement multiplier, see `RCW-49_62.md`.

## Workers' Comp — RCW 51 (L&I exclusive remedy)

### Exclusivity

Workers' compensation is the exclusive remedy for
workplace injury. Employee cannot sue employer for
negligence. Employer immunity extends to co-employees
acting in scope.

### Intentional-injury carve-out

Exclusivity does NOT bar suit against employer for
**deliberate intention** to injure. The standard is
high: employer must have actual knowledge that injury
was certain to occur and deliberately disregarded that
knowledge. Leading case: *Walston v. Boeing Co.*

### Third-party suits

Worker injured by third party (e.g., negligent vendor on
worksite) CAN sue the third party. L&I has a subrogation
lien for benefits paid.

For the deliberate-intention elements, the subrogation
mechanics, and the third-party-recovery apportionment,
see `RCW-51_04.md`.

## Whistleblower

- **Common-law wrongful discharge in violation of public
  policy** (*Thompson v. St. Regis Paper Co.*; *Cudney v.
  ALSCO*) — covers private-sector retaliation against
  protected activity
- **Public-sector whistleblower** under RCW 42.40 /
  42.41 — comprehensive procedures for state employees

Note: RCW 49.60.210 is WLAD's anti-retaliation provision,
not a general private-sector whistleblower statute.

## Composition with other wa- skills

- `wa-statewide-format` — caption + GR 14
- `wa-discovery` — discovery in employment cases
- `wa-first-30-days` — answer + affirmative defenses
- `wa-deadlines` — WLAD SOL + WSHRC clock
- `wa-fact-check` — citation verification
