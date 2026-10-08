---
name: ga-post-judgment-codearranger
title: Georgia Post-Judgment Procedure
description: This skill should be used when navigating post-judgment procedure in a Georgia civil case. Triggers include "set aside a default judgment in Georgia", "open default 15 days", "motion to set aside Georgia", "wage garnishment Georgia", "claim exemption garnishment", "Georgia bank levy", "traverse garnishment", "continuing garnishment Georgia", "Georgia exemptions O.C.G.A. 44-13-100", "judgment dormant", "revive a Georgia judgment", "new trial Georgia", "JNOV Georgia". Covers opening or setting aside default under O.C.G.A. § 9-11-55, motions to set aside under § 9-11-60(d), post-trial motions (new trial § 5-5-40, JNOV § 9-11-50(b), appeal § 5-6-38), the post-2016 garnishment regime (O.C.G.A. §§ 18-4-1 to 18-4-90) and the defendant's claim/traverse, property exemptions under § 44-13-100, and judgment dormancy and revival under §§ 9-12-60 and 9-12-61.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia Post-Judgment Procedure

> **NOT LEGAL ADVICE.** This skill addresses procedure once a Georgia
> judgment has been entered. Verify every step, deadline, and dollar
> figure against current law before filing or responding. Pair with
> substantive review by counsel where stakes warrant.

Use this skill in addition to `ga-statewide-format` when the case is
**past judgment** — whether you are attacking the judgment, defending
against collection, or collecting on it.

## Two paths after judgment

1. **Attack the judgment** — open or set aside a default under
   O.C.G.A. § 9-11-55, set aside under § 9-11-60(d), move for new
   trial under § 5-5-40, move for JNOV under § 9-11-50(b), or appeal
   under § 5-6-38.
2. **Defend collection or collect** — respond to and challenge
   garnishment under O.C.G.A. §§ 18-4-1 to 18-4-90, assert exemptions
   under § 44-13-100, and track the dormancy and revival clock under
   §§ 9-12-60 and 9-12-61.

## Attacking the judgment

### Opening a default — O.C.G.A. § 9-11-55

When the defendant has not answered, the case goes into default.
Georgia gives two distinct windows:

- **As a matter of right within 15 days** — under § 9-11-55(a), the
  defendant may **open the default as of right** at any time within
  **15 days** of the day of default, **on payment of costs**. No
  excuse, affidavit, or showing of a defense is required in this
  window; paying the accrued costs is the price of entry. This is the
  single most important post-default deadline — calendar it the moment
  default is suspected.
- **After 15 days — only on a showing under § 9-11-55(b)** — once the
  15-day right has lapsed, the court may open the default **only** on
  one of three statutory grounds:
  1. **providential cause** preventing the answer,
  2. **excusable neglect**, or
  3. a **"proper case."**

  And the movant must satisfy **four mandatory conditions**: (a) the
  showing must be made **under oath**; (b) the movant must offer to
  **plead instanter**; (c) the movant must **announce ready** to
  proceed with trial; and (d) the movant must **set up a meritorious
  defense**. Missing any one of the four defeats the motion regardless
  of the ground asserted.
- **The "proper case" prong** — the Georgia Supreme Court in *Bowen v.
  Savoy*, 308 Ga. 204 (2020), addressed the "proper case" ground,
  holding that it is the broadest of the three and does **not** require
  the movant to furnish a reasonable explanation for the failure to
  answer. The "proper case" analysis looks to whether opening the
  default serves the ends of justice on the whole record. (Verify the
  pincite and current treatment before relying on it.)

### Motion to set aside — O.C.G.A. § 9-11-60(d)

A judgment that is **not** a mere default — or a default attacked after
the § 9-11-55 windows close — is reached under § 9-11-60(d). Grounds
include:

- a **non-amendable defect** appearing on the face of the record or
  pleadings (§ 9-11-60(d)(3));
- **lack of jurisdiction** over the person or the subject matter
  (§ 9-11-60(d)(1)); and
- **fraud, accident, or mistake**, or the acts of the adverse party
  unmixed with the movant's own negligence (§ 9-11-60(d)(2)).

**Timing**: under § 9-11-60(f), a motion to set aside generally must be
brought **within three years** of entry of the judgment complained of.
There is **no time limit for a void judgment** — a judgment void for
lack of personal or subject-matter jurisdiction may be attacked at any
time. Lack of service (a frequent issue in consumer debt-buyer default
cases) is the classic void-judgment basis. See `ga-consumer-debt` for
the default-judgment attack template.

### Post-trial motions and appeal

- **Motion for new trial — O.C.G.A. § 5-5-40**: file **within 30 days**
  of entry of the judgment. Grounds are stated in O.C.G.A. Title 5,
  Chapter 5 (verdict contrary to evidence, error of law, newly
  discovered evidence, etc.).
- **Motion for judgment notwithstanding the verdict (JNOV) —
  O.C.G.A. § 9-11-50(b)**: file **within 30 days** of entry of
  judgment, predicated on a prior motion for directed verdict.
- **Notice of appeal — O.C.G.A. § 5-6-38**: file **within 30 days**
  of entry of the judgment, or within 30 days of the order disposing
  of a timely motion for new trial or JNOV. Track whether the appeal
  is a direct appeal or requires an application (discretionary or
  interlocutory).

## Defending collection — garnishment

Georgia's garnishment chapter was **rewritten in 2016** following
*Strickland v. Alexander*, N.D. Ga. (2015), which held the prior
scheme unconstitutional for inadequate notice and exemption
procedures. The old section numbers are gone; the current chapter
spans **O.C.G.A. §§ 18-4-1 to 18-4-90**. Always work from the current
chapter — older forms and citations are unreliable.

### Process and garnishee answer — O.C.G.A. § 18-4-4

The garnishment summons is served on the garnishee (employer or bank).
For a **bank/financial-institution garnishee**, the garnishee's answer
is due in the window set by § 18-4-4 — generally **not sooner than 5
nor later than 15 days** after service. The answer reports what funds
or property the garnishee holds. (Verify the exact day-count against
current § 18-4-4.)

### Wage limit — O.C.G.A. § 18-4-5

Earnings subject to garnishment are capped at the **lesser of**:

- **25% of disposable earnings** for the week, or
- the amount by which disposable earnings **exceed 30 times the
  federal minimum wage** per week.

At a $7.25 federal minimum wage, the 30× floor protects roughly
**$217.50 per week** — if disposable weekly earnings are **at or below**
that floor, **nothing is garnishable**. This tracks the federal CCPA
(15 U.S.C. § 1673). Treat the dollar figure as illustrative and
**verify the current federal minimum wage and § 18-4-5 text** before
relying on the number.

### Continuing garnishment — O.C.G.A. § 18-4-20 et seq.

A **continuing garnishment** reaches future earnings over a fixed
period — currently a **1,095-day** period — under § 18-4-20 et seq.,
with the per-pay-period wage limit in **§ 18-4-53** mirroring the
§ 18-4-5 cap. The garnishee files periodic answers over the life of
the writ.

### Exemptions inside the garnishment — O.C.G.A. § 18-4-6

Section 18-4-6 lists property **not subject to garnishment**,
including funds in **IRAs, pensions, and other retirement accounts**,
and funds that are **federally exempt** — **Social Security, SSI,
Veterans' benefits, unemployment compensation, workers' compensation,
and disability** payments. These remain exempt even after deposit;
the burden is on the defendant to identify and trace them.

### The defendant's claim / traverse — O.C.G.A. § 18-4-15

The defendant is not automatically a party to the garnishment. Under
**§ 18-4-15**, the defendant **becomes a party by filing a claim**
(the practical "traverse") that asserts the exemption basis or
otherwise contests the garnishment — and must do so **before the
funds are subject to judgment, disbursement, or distribution**. Once
distributed, the money is gone.

**Timing — O.C.G.A. § 18-4-93**: file the claim **promptly**. The
practical window is short — generally **within about 20 days after the
garnishee's answer** (verify the exact period against current
§ 18-4-93). Do not wait: the controlling event is distribution of the
funds, so a late claim can be worthless even if technically permitted.

## Property exemptions — O.C.G.A. § 44-13-100

**Georgia is an opt-out state.** Under **§ 44-13-100(b)**, a Georgia
debtor **may not use the federal bankruptcy exemptions** and must use
the **state exemptions** set out in § 44-13-100(a). Key categories
(amounts change — **verify current § 44-13-100 amounts** before
relying on any figure):

- **Homestead** — § 44-13-100(a)(1): equity in the debtor's
  residence.
- **Motor vehicle** — § 44-13-100(a)(3).
- **Household goods, furnishings, apparel, appliances** —
  § 44-13-100(a)(4) (per-item and aggregate caps).
- **Jewelry** — § 44-13-100(a)(5).
- **Wildcard** — § 44-13-100(a)(6): a flat amount **plus any
  unused-homestead spillover**, applicable to any property.
- **Tools of the trade / implements / books** —
  § 44-13-100(a)(7).
- **Health aids, life insurance, personal-injury and wrongful-death
  recoveries, support, and retirement funds** — § 44-13-100(a)(2)
  and (a)(8)–(a)(11).

The unused-homestead spillover into the wildcard is the most useful
planning feature for a debtor with little or no home equity.

## Judgment lifespan — dormancy and revival

- **Dormancy — O.C.G.A. § 9-12-60**: a Georgia judgment becomes
  **dormant** if **seven years** pass without enforcement — i.e.,
  unless a **writ of execution (fi. fa.)** is issued and entered/
  recorded on the **General Execution Docket (GED)** of the county,
  with that activity refreshing the clock. A dormant judgment cannot
  be enforced until revived.
- **Revival — O.C.G.A. § 9-12-61**: a dormant judgment may be
  **revived within three years** of the date it became dormant
  (by scire facias or by action). Miss that three-year revival window
  on top of dormancy and enforcement is barred.

For a debtor, the dormancy/revival clock is a defense: an old judgment
that went dormant and was never timely revived is unenforceable.

## Common pro se post-judgment scenarios

1. **Default just entered** — calendar the **15-day** § 9-11-55(a)
   right to open as of right on payment of costs; this is the
   cheapest and surest path. After 15 days, pivot to § 9-11-55(b)
   (ground + four mandatory conditions, all under oath).
2. **Default in a debt-buyer case with bad service** — attack as a
   **void judgment** under § 9-11-60(d)(1) for lack of personal
   jurisdiction (no time limit). See `ga-consumer-debt`.
3. **Bank account garnished holding Social Security** — file the
   § 18-4-15 claim/traverse **promptly** (watch the § 18-4-93 window),
   asserting the § 18-4-6 federal exemption before the funds are
   disbursed.
4. **Wage garnishment, low earner** — check the § 18-4-5 floor; if
   disposable weekly earnings are at or below ~30× the federal
   minimum wage, nothing is garnishable.
5. **Old judgment surfaces** — check the § 9-12-60 seven-year dormancy
   clock and whether it was revived within the § 9-12-61 three-year
   window; if not, it is unenforceable.

## Composition

- For statewide format: `ga-statewide-format`
- For drafting the motion to open/set aside or the garnishment
  claim/traverse: `ga-draft-motion`
- For the supporting sworn showing / affidavit (required under
  § 9-11-55(b)): `ga-draft-declaration`
- For a proposed order opening default or sustaining a claim:
  `ga-draft-order`
- For deadline computation (15-day open-default, 30-day post-trial,
  dormancy/revival clocks): `ga-deadlines`
- For debt-buyer-specific defenses behind the default attack:
  `ga-consumer-debt`
- For venue mechanics: `ga-state-court`, `ga-magistrate`
- For citation verification: `ga-fact-check`

## References

- `references/open-default-9-11-55.md` — O.C.G.A. § 9-11-55: the
  15-day right (a), the post-15-day grounds and four mandatory
  conditions (b), and the *Bowen v. Savoy* "proper case" analysis
- `references/set-aside-9-11-60.md` — § 9-11-60(d) grounds, the
  § 9-11-60(f) three-year limit, and the no-limit rule for void
  judgments
- `references/garnishment-defense.md` — the post-2016 chapter
  (§§ 18-4-1 to 18-4-90): process/answer § 18-4-4, wage limit
  § 18-4-5, continuing garnishment § 18-4-20 et seq. / § 18-4-53,
  the § 18-4-15 claim/traverse and § 18-4-93 timing, with the
  *Strickland v. Alexander* background
- `references/ga-exemptions.md` — § 44-13-100 opt-out exemption
  schedule with the unused-homestead spillover into the wildcard
- `references/judgment-dormancy-revival.md` — § 9-12-60 dormancy,
  the GED/fi. fa. refresh, and § 9-12-61 revival
