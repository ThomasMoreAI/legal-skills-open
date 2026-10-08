---
name: oh-personal-injury-codearranger
title: Ohio Personal Injury — Substantive Framework
description: 'Use for Ohio personal-injury / tort matters — negligence, auto, product liability, med-mal, wrongful death, government tort. Covers **modified comparative negligence** (R.C. 2315.33 — **51% bar**), **several vs. joint liability** (R.C. 2307.22), **2005 S.B. 80 damages caps** (noneconomic **R.C. 2315.18**, punitive **R.C. 2315.21**), **med-mal** (**1-year SOL** with **180-day letter**, **4-year repose**, **affidavit of merit**), **OPLA product liability** (R.C. 2307.71, **10-year repose**), **wrongful death** (**R.C. Chapter 2125**), **political-subdivision immunity** (R.C. Chapter 2744), **dog-bite strict liability** (R.C. 955.28). Triggers: "Ohio personal injury", "R.C. 2315.33", "Ohio damages cap", "Ohio product liability".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-personal-injury
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Ohio Personal Injury — Substantive Framework

> **NOT LEGAL ADVICE.** Verify every cite against current
> R.C. text and current case law before filing. Personal-
> injury outcomes can be significant and the deadlines are
> short and unforgiving — strongly recommend consulting a
> licensed Ohio attorney for any serious-injury, death,
> medical-malpractice, or government-defendant matter.

Ohio tort law was reshaped by the **2005 S.B. 80 tort-reform
package** (damages caps, several liability, the OPLA
codification). The framework below describes the structure;
point at the references corpus for current text, dollar
thresholds, and subsection detail rather than relying on the
numbers memorized here.

## Modified comparative negligence — the 51% bar

Ohio is a **modified comparative-negligence** state.

- **R.C. 2315.33** — the plaintiff's contributory fault does
  **not** bar recovery so long as it was **not greater than**
  the combined tortious conduct of all other persons (those
  the plaintiff sues AND those it does not). In practice this
  is a **51% bar**: a plaintiff who is 50% at fault still
  recovers; a plaintiff 51% or more at fault recovers
  nothing.
- **R.C. 2315.34 / R.C. 2315.35** — recoverable damages are
  **diminished** in proportion to the plaintiff's percentage
  of fault. The trier of fact makes the percentage findings
  (economic vs. noneconomic split + each party's share).
- **R.C. 2315.32** — contributory fault is pleaded as an
  **affirmative defense**, but it is **not** available
  against an **intentional-tort** claim.
- **R.C. 2315.36** — apportionment of liability among the
  parties once contributory fault is established, tying back
  into the R.C. 2307.22 joint/several framework.

See
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2315.md`.

## Several vs. joint liability — R.C. 2307.22 / 2307.23

Ohio's 2005 reform split economic and noneconomic damages:

- **Noneconomic damages are SEVERAL only** (R.C. 2307.22(C)):
  each defendant pays only its own proportionate share of
  noneconomic loss, calculated from its percentage of
  tortious conduct.
- **Economic damages are joint-and-several only against a
  defendant found MORE THAN 50% at fault** (R.C.
  2307.22(A)(1)). A defendant **50% or less** at fault pays
  only its proportionate share of economic loss (R.C.
  2307.22(A)(2) / (B)). Intentional-tort defendants are an
  exception — joint-and-several for economic loss regardless
  of percentage (R.C. 2307.22(A)(3)).
- **R.C. 2307.23** — the percentage-of-tortious-conduct
  findings (including the empty-chair / nonparty-fault
  affirmative defense; percentages must sum to 100%).

### Contribution among joint tortfeasors

- **R.C. 2307.25** — the right of contribution.
- **R.C. 2307.26 / 2307.27** — enforcing contribution and
  apportioning the judgment.
- **R.C. 2307.28** — effect of a release or covenant not to
  sue on contribution rights.

See
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2307.md`.

## Damages caps — the 2005 S.B. 80 tort reform

### Noneconomic cap — R.C. 2315.18

- **No cap on economic loss** (R.C. 2315.18(B)(1)) — lost
  wages, medical bills, and other pecuniary loss are
  uncapped.
- **Noneconomic loss cap** (R.C. 2315.18(B)(2)): the greater
  of **$250,000 or 3× economic loss**, to a maximum of
  **$350,000 per plaintiff** or **$500,000 per occurrence**.
- **Catastrophic-injury exception** (R.C. 2315.18(B)(3)) —
  **no cap** where the noneconomic loss is for (a) permanent
  and substantial physical deformity, loss of use of a limb,
  or loss of a bodily organ system, or (b) permanent physical
  functional injury that permanently prevents independent
  self-care and life-sustaining activities.
- The cap does **not** apply to wrongful-death actions (R.C.
  2315.18(H)(3)) or to political-subdivision actions, which
  use the R.C. 2744.05 limits (R.C. 2315.18(H)(2)). The jury
  is **not** told the cap; the court applies it post-verdict.

### Punitive / exemplary cap — R.C. 2315.21

- Punitive damages require **malice or aggravated/egregious
  fraud**, proven by **clear and convincing evidence** (R.C.
  2315.21(C)/(D)(4)), and a bifurcated trial on motion (R.C.
  2315.21(B)).
- **General cap**: punitive damages may not exceed **2× the
  compensatory damages** awarded against that defendant (R.C.
  2315.21(D)(2)(a)).
- **Small-employer / individual sub-cap** (R.C.
  2315.21(D)(2)(b)): the lesser of 2× compensatory or **10%
  of net worth up to $350,000** ("small employer" defined at
  R.C. 2315.21(A)(5) — generally ≤100 employees, ≤500 in
  manufacturing).

See
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2315.md`.

## Medical malpractice

Med-mal ("medical claim") is statutorily distinct from
ordinary negligence — different SOL, different cap section,
and a court-rule pleading requirement.

### SOL + repose — R.C. 2305.113

- **R.C. 2305.113(A)** — **1-year** SOL on a medical, dental,
  optometric, or chiropractic claim, running from accrual.
- **R.C. 2305.113(B)** — the **180-day letter**: a written
  pre-suit notice (certified mail, return receipt) given
  before the 1-year period expires extends the deadline by
  **180 days**.
- **R.C. 2305.113(C)** — the **4-year statute of repose**:
  no med-mal action may be commenced more than 4 years after
  the act or omission, regardless of discovery (subject to
  the narrow minor / foreign-object / unsound-mind
  exceptions in (C)/(D)).

### Med-mal noneconomic cap — R.C. 2323.43

A parallel noneconomic cap applies specifically to medical
claims: the greater of **$250,000 or 3× economic loss**, to
**$350,000/plaintiff** or **$500,000/occurrence** (R.C.
2323.43(A)(2)), with a **catastrophic-injury exception** that
— unlike R.C. 2315.18 — does not fully remove the cap but
**raises it to $500,000/plaintiff and $1,000,000/occurrence**
(R.C. 2323.43(A)(3)). Economic loss is uncapped (R.C.
2323.43(A)(1)).

### Affidavit of merit — Civ. R. 10(D)(2) (a court RULE)

The **affidavit of merit** is **not** a statute — it is a
**Civil Rule** requirement. A complaint stating a medical
claim must be accompanied by an affidavit of merit from an
expert who has reviewed the records and opines that the
standard of care was breached. Failure to attach one (or to
secure an extension) is grounds for dismissal. See the rule
text at
`oh-law-references/references/court-rules/CivilProcedure.md`
(Civ. R. 10(D)(2)).

See
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2305.md`
and
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2323.md`.

## Product liability — the OPLA

The **Ohio Products Liability Act** (R.C. 2307.71 to
2307.80) is the exclusive framework for product claims.

- **Abrogation** — R.C. 2307.71(B) declares the sections are
  "intended to abrogate all common law product liability
  claims," and R.C. 2307.72 confirms recovery of compensatory
  damages on a product-liability claim is governed by the
  Act. Plead under the OPLA, not common-law strict liability.
- **Theories of defect** — manufacturing defect (R.C.
  2307.74), design/formulation defect (R.C. 2307.75),
  inadequate warning (R.C. 2307.76), and nonconformance with
  representation (R.C. 2307.77); supplier liability at R.C.
  2307.78. Enterprise / market-share liability is **rejected**
  (R.C. 2307.73(C)).
- **10-year statute of repose** — R.C. 2305.10(C): no
  product-liability claim accrues against a manufacturer or
  supplier later than **10 years** from delivery to the
  first purchaser/lessee, subject to the fraud, express-
  long-warranty, and exposure exceptions in (C)(2)-(7). The
  ordinary 2-year injury SOL (R.C. 2305.10(A)) still applies
  within the repose window.

See
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2307.md`
and
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2305.md`.

## Wrongful death — R.C. Chapter 2125

- **Who sues** — the action is brought **in the name of the
  personal representative** of the decedent (R.C. 2125.02(A))
  for the **exclusive benefit** of the surviving spouse,
  children, parents, and other next of kin, who are
  rebuttably presumed to have suffered damages.
- **Damages** — R.C. 2125.02(D): loss of support, loss of
  services, loss of society/consortium, loss of prospective
  inheritance, and mental anguish; plus reasonable funeral
  and burial expenses.
- **SOL** — **2 years** from the date of death (R.C.
  2125.02(F)(1)), with a 10-year product-liability repose
  overlay for death-by-product claims (R.C. 2125.02(F)(2)).
- **No cap** — the R.C. 2315.18 noneconomic cap does **not**
  apply to wrongful-death actions.
- **Distribution** through the probate court (R.C. 2125.03).

See
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2125.md`.

## Suing a government

Ohio splits sovereign immunity by defendant type.

### Political subdivisions — R.C. Chapter 2744 (three tiers)

When the defendant is a city, county, township, school
district, or other political subdivision, run the three-tier
analysis:

1. **General immunity** — R.C. 2744.02(A): a political
   subdivision is **not liable** for injury caused by an act
   or omission in connection with a governmental or
   proprietary function.
2. **Enumerated exceptions** — R.C. 2744.02(B): immunity is
   stripped only in the listed categories — negligent
   operation of a motor vehicle (B)(1), negligent performance
   of **proprietary** functions (B)(2), negligent failure to
   keep public roads in repair (B)(3), physical defects on
   the grounds of buildings used for a governmental function
   (B)(4), and where another R.C. section expressly imposes
   liability (B)(5).
3. **Defenses / restored immunity** — R.C. 2744.03: even if
   an exception applies, the subdivision (or employee) may
   reassert immunity (e.g., discretionary policy-making
   under (A)(3)/(A)(5); the employee is generally immune
   absent malice, bad faith, or wanton/reckless conduct
   under (A)(6)).

**Damages limits** — R.C. 2744.05: **no punitive damages**
against a political subdivision (R.C. 2744.05(A)); collateral
benefits are **deducted** (R.C. 2744.05(B)); and noneconomic
("non-actual-loss") damages are **capped at $250,000 per
person** (R.C. 2744.05(C)), with actual/economic loss
uncapped. The **SOL is 2 years** (R.C. 2744.04(A)), and the
complaint must **not specify a dollar amount** in the demand
(R.C. 2744.04(B)).

See
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2744.md`.

### The State itself — Court of Claims (R.C. Chapter 2743)

Suits against **the State of Ohio** (state agencies, state
universities) do **not** go to Common Pleas — they go to the
**Ohio Court of Claims** under **R.C. Chapter 2743** (the
State's limited waiver of sovereign immunity, with its own
filing rules, no jury, and a determination on personal
immunity of state employees). R.C. Chapter 2743 was not
pulled into the statutes corpus; see the rule/jurisdiction
summary at
`oh-law-references/references/court-rules/CourtOfClaims.md`.

## Dog-bite — R.C. 955.28(B)

Ohio gives an injured person **two parallel theories**:

- **Statutory strict liability** — R.C. 955.28(B): the
  **owner, keeper, or harborer** is liable in damages for any
  injury, death, or loss caused by the dog, with **no
  scienter requirement** (no need to prove the dog's prior
  viciousness). The statute carves out injuries to
  trespassers, those committing a non-minor-misdemeanor
  criminal offense, and those teasing/tormenting/abusing the
  dog.
- **Common-law action** — the traditional scienter-based
  ("one free bite") cause of action survives alongside the
  statute and can reach punitive damages where the statutory
  claim cannot.

See
`oh-law-references/references/oh-statutes-debt/RC-Chapter-955.md`.

## SOL quick table

| Claim | SOL | Statute |
|---|---|---|
| Bodily injury / personal injury | 2 yr | R.C. 2305.10(A) |
| Product liability (injury) | 2 yr (10-yr repose) | R.C. 2305.10(A), (C) |
| Assault / battery, libel / slander, false imprisonment, malicious prosecution | 1 yr | R.C. 2305.11(A) |
| Medical / dental / optometric / chiropractic claim | 1 yr (180-day-letter ext.; 4-yr repose) | R.C. 2305.113 |
| Wrongful death | 2 yr | R.C. 2125.02(F)(1) |
| Tort against a political subdivision | 2 yr | R.C. 2744.04(A) |

Always confirm accrual + tolling (minority/unsound-mind
under R.C. 2305.16; the discovery rule where it applies)
before relying on a bare year count.

## Frivolous-conduct sanctions — a two-way risk

Tort litigation carries sanction exposure on **both** sides:

- **R.C. 2323.51** — **frivolous conduct** in a civil action
  (conduct that merely harasses, is not warranted under
  existing law, or asserts factual contentions with no
  evidentiary support) can be sanctioned with **attorney's
  fees and costs** against the offending party or counsel.
- **Civ. R. 11** — the signature/certification rule, a
  parallel sanction route. See
  `oh-law-references/references/court-rules/CivilProcedure.md`.

Screen the complaint (and any answer/defense) against both
before filing.

See
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2323.md`.

## Composition with other oh- skills

- `oh-statewide-format` — Ohio Civ. R. 10 caption + filing
  format (PI cases use the `CV` Common Pleas case-number
  prefix)
- `oh-first-30-days` — answer / Civ. R. 12(B)(6) triage /
  affirmative defenses (contributory fault, immunity, SOL)
- `oh-discovery` — discovery mechanics (Civ. R. 33 40-
  interrogatory cap; expert disclosure)
- `oh-hearings` — motion practice + oral argument
- `oh-deadlines` — Civ. R. 6 computation; the short tort /
  med-mal / wrongful-death / R.C. 2744.04 clocks
- `oh-post-judgment` — Civ. R. 60(B) / judgment enforcement
- `oh-pro-se` — pro-se drafting framework
- `oh-fact-check` — Ohio public-domain citation format +
  cite verification
- Flagship venue skills — `oh-cuya` (Cuyahoga / Cleveland),
  `oh-frank` (Franklin / Columbus), `oh-hamil` (Hamilton /
  Cincinnati), `oh-summit`, `oh-montgomery`, `oh-lucas`,
  `oh-stark`, `oh-butler` — and the `oh-county-courts`
  roll-up for the other 80 counties
