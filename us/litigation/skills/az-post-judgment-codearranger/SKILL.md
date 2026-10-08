---
name: az-post-judgment-codearranger
title: Arizona Post-Judgment Procedure
description: Use when navigating post-judgment procedure in an Arizona civil case. Triggers include "Arizona garnishment", "writ of garnishment Arizona", "garnishment of earnings Arizona A.R.S. 12-1598", "non-earnings garnishment Arizona", "set aside Arizona judgment Rule 60", "vacate Arizona judgment", "relief from judgment Arizona", "motion for new trial Arizona Rule 59", "alter or amend judgment Arizona", "Arizona exemptions A.R.S. 33-1101 homestead", "personal property exemptions Arizona A.R.S. 33-1121", "judgment renewal Arizona", "renew Arizona judgment by affidavit", "writ of execution Arizona", "judgment lien Arizona A.R.S. 33-961", "debtor exam Arizona", "satisfaction of judgment Arizona". Covers post-judgment motions, enforcement of money judgments (garnishment, execution, judgment liens, debtor's examination, renewal), the A.R.S. Title 33 exemption framework, and satisfaction of judgment.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arizona Post-Judgment Procedure

> **NOT LEGAL ADVICE.** This skill addresses procedure once an Arizona
> judgment has been entered. Verify every step — and every dollar figure
> and day count — against current law before filing or responding.

Use this skill alongside `az-statewide-format` when the case is **past
judgment** — whether you are attacking the judgment, defending against
collection, or collecting on it.

## Two paths after judgment

1. **Attack the judgment** — a motion for new trial or to alter/amend
   (Ariz. R. Civ. P. 59) or relief from judgment (Ariz. R. Civ. P. 60).
2. **Collect or resist collection** — garnishment (A.R.S. § 12-1598 et
   seq. earnings; § 12-1570 et seq. non-earnings), writ of execution
   (A.R.S. § 12-1551 et seq.), judgment liens (A.R.S. § 33-961 et seq.),
   debtor's examination, renewal (A.R.S. §§ 12-1611/-1612), exemptions
   (A.R.S. § 33-1101 / § 33-1121 et seq.), and satisfaction.

## Attacking the judgment

### New trial / alter or amend — Ariz. R. Civ. P. 59

After trial, move for a **new trial** under **Rule 59(a)** (grounds
include irregularity in the proceedings, jury or attorney misconduct,
excessive or insufficient damages, a verdict against the weight of the
evidence, newly discovered evidence, and error of law). A motion to
**alter or amend the judgment** runs under **Rule 59(d)**.

> ⚠ **Timing.** A Rule 59 motion for new trial or to alter or amend is
> due a fixed number of days **after entry of judgment**, and the window
> is **not extendable**. Confirm the current day count in the corpus and
> calendar it the moment judgment is entered — see `az-deadlines`.

### Relief from judgment — Ariz. R. Civ. P. 60

**Rule 60** is Arizona's FRCP-60 analog. Grounds under **Rule 60(b)**:
(1) mistake, inadvertence, surprise, or excusable neglect; (2) newly
discovered evidence; (3) fraud, misrepresentation, or other misconduct
of an opposing party; (4) the judgment is **void**; (5)
satisfied/released or no longer equitable to apply prospectively; (6)
any other reason justifying relief. Rule 60(c) governs the timing of a
Rule 60(b) motion (see below); Rule 60(d) preserves other powers to
grant relief (e.g., independent actions, relief from a void judgment).

> **Timing.** A Rule 60(b) motion must be made within a **reasonable
> time**, and for grounds **(1)-(3)** **no more than the rule's outer
> limit** (a set number of days after entry). Confirm the current outer
> limit and the reasonable-time case law in the corpus.

- **Setting aside a default / default judgment** is the most common use,
  especially in consumer debt-buyer cases with defective service. A
  movant generally must show **good cause** and a **meritorious
  defense**; a void-for-defective-service attack (Rule 60(b)(4)) does
  not need the meritorious-defense showing. Pair with the substantive
  defense — chain of title, statute of limitations — see
  `az-consumer-debt`.

## Collecting / resisting collection

### Garnishment — earnings (A.R.S. § 12-1598 et seq.)

A judgment creditor reaches a debtor's **wages** held by a third-party
garnishee (the employer) via a **writ of garnishment of earnings** under
**A.R.S. § 12-1598 et seq.**:

- The creditor applies for the writ; it is served on the garnishee
  employer with notice to the judgment debtor.
- The garnishee files an **answer** disclosing the debtor's earnings;
  the debtor may file a **written objection / request for hearing**
  within the period the papers specify.
- Withholding is capped per pay period. The federal CCPA garnishment cap
  (15 U.S.C. §§ 1671-1677) sets a wage-protection floor; Arizona's
  earnings-garnishment limit and any head-of-household / hardship
  reduction live in the corpus — **verify the current cap and the
  objection deadline**.

### Garnishment — non-earnings (A.R.S. § 12-1570 et seq.)

A **non-earnings writ** under **A.R.S. § 12-1570 et seq.** reaches
**bank accounts** and other non-wage monies or property held by a
garnishee for the debtor. The garnishee answers; the debtor may object
and claim exemptions within the window. Verify the service mechanics,
answer deadline, and objection window in the corpus.

### Writ of execution — A.R.S. § 12-1551 et seq.

A **writ of execution** under **A.R.S. § 12-1551 et seq.** directs the
sheriff to levy on and sell the debtor's **non-exempt** property to
satisfy the judgment. Note that the writ must issue while the judgment
remains enforceable — see renewal below.

### Judgment liens on real property — A.R.S. § 33-961 et seq.

Recording a **certified copy of the judgment** (or a statutorily
prescribed information statement) with the county recorder creates a
**judgment lien on the debtor's real property** in that county under
**A.R.S. § 33-961 et seq.** The lien's **duration and renewal** track
the judgment's life; the **homestead exemption** (below) carves out
protected equity. Verify the recording requirements and lien term in the
corpus.

### Debtor's examination / supplemental proceedings

To **locate assets**, the creditor may compel the judgment debtor (or a
third party) to appear and answer under oath about income, property, and
accounts — a **debtor's examination**. Failure to appear after proper
service can expose the debtor to **contempt**. Confirm the current
procedure and notice requirement in the corpus.

### Renewal of judgment — A.R.S. §§ 12-1611 / 12-1612

An Arizona judgment is enforceable for a **statutory term** (point to
the corpus for the current number of years), after which it must be
**renewed** to remain collectible:

- **A.R.S. § 12-1611** — renewal **by action** within the statutory
  term.
- **A.R.S. § 12-1612** — renewal **by affidavit**: the creditor records
  and files an **affidavit of renewal** within the window before the
  judgment expires, restarting the enforcement clock.

> ⚠ **Verify the current judgment term and the renewal window.** Missing
> the renewal deadline lets the judgment **expire** and become
> unenforceable. Conversely, a debtor facing collection on an **old,
> un-renewed** judgment should check whether it lapsed. Confirm the
> current term and timing in the corpus — see `az-deadlines`.

### Exemptions from execution — A.R.S. § 33-1101 / § 33-1121 et seq.

A debtor may protect property through statutory **exemptions**:

- **Homestead** in the residence — **A.R.S. § 33-1101**. The exemption
  amount was **recently increased** and is **annually adjusted**; the
  homestead attaches to certain proceeds and interacts with recorded
  judgment liens.
- **Personal-property** exemptions — **A.R.S. § 33-1121 et seq.**
  (household furnishings, clothing, tools of the trade, a motor-vehicle
  value, certain bank-account funds, and prescribed benefits).
- **Earnings-garnishment limits** (above) and categorically protected
  funds — **Social Security** (42 U.S.C. § 407), certain public
  benefits and retirement accounts.

> ⚠ **Do not rely on an exemption dollar amount from memory.** Arizona's
> homestead figure (A.R.S. § 33-1101) and the § 33-1121-series
> personal-property amounts are set and **periodically adjusted by
> statute**. **Look up the current amounts in the corpus** before
> asserting them.

To claim an exemption, the debtor files the written **objection / claim
of exemption** with the issuing court within the period the garnishment
or levy papers specify; the court then resolves it. Act promptly — see
`az-deadlines`.

### Satisfaction of judgment

When a judgment is paid in full, the **satisfaction** should be entered
of record. The creditor ordinarily files and (where a lien was recorded)
records a **satisfaction of judgment**; if the creditor refuses after
payment, the debtor may move the court to enter satisfaction with proof.
Verify any statutory duty/penalty for failure to acknowledge
satisfaction after demand in the corpus.

## Common pro se scenarios

1. **Debt-buyer default judgment** — Rule 60(b) motion to set aside on
   defective service / excusable neglect plus a meritorious defense
   (chain of title, SOL). See `az-consumer-debt`.
2. **Bank account holding Social Security garnished** — assert the 42
   U.S.C. § 407 exemption and any A.R.S. § 33-1121-series exemption;
   file the objection within the non-earnings-writ window.
3. **Wage garnishment** — confirm withholding is within the CCPA cap and
   the current A.R.S. § 12-1598 earnings limit; raise head-of-household
   / hardship where available.
4. **Old judgment surfaces** — check whether it was **renewed** under
   A.R.S. § 12-1611 / § 12-1612 within the statutory term, or whether it
   has **expired**.
5. **Creditor demands a debtor exam** — appear and answer to avoid
   contempt.

## Composition

- Format baseline: `az-statewide-format`
- Drafting the motion / supporting declaration: `az-draft-motion`,
  `az-draft-declaration`
- Debt-buyer defenses: `az-consumer-debt`
- Deadline arithmetic (Rule 59 window, garnishment objection clock,
  renewal deadline): `az-deadlines`
- Venue: `az-maricopa`, `az-pima`, `az-superior-courts`,
  `az-justice-courts`

## References

- `references/post-judgment-motions.md` — Ariz. R. Civ. P. 59, Rule 60
- `references/garnishment.md` — earnings (A.R.S. § 12-1598 et seq.) +
  non-earnings (A.R.S. § 12-1570 et seq.)
- `references/execution-and-liens.md` — writ of execution (A.R.S.
  § 12-1551 et seq.), judgment liens (A.R.S. § 33-961 et seq.)
- `references/renewal.md` — A.R.S. §§ 12-1611 / 12-1612 (verify term)
- `references/exemptions.md` — A.R.S. § 33-1101 homestead + § 33-1121
  et seq. (verify figures)
- `references/satisfaction-of-judgment.md` — entering satisfaction
