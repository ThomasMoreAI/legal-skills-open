---
name: co-post-judgment-codearranger
title: Colorado Post-Judgment Procedure
description: This skill should be used when navigating post-judgment procedure in a Colorado civil case. Triggers include "C.R.C.P. 60", "vacate judgment in Colorado", "set aside default judgment", "Colorado garnishment", "writ of continuing garnishment", "claim of exemption", "supplemental proceedings", "debtor exam Colorado", "satisfaction of judgment Colorado", "motion to revive judgment", "judgment lien Colorado". Covers C.R.C.P. 60 relief, Colorado's garnishment regime under C.R.S. art. 54.5 of title 13, the exemption framework under C.R.S. art. 54 of title 13, supplemental proceedings under C.R.C.P. 69, judgment lien recording, judgment satisfaction and revival under C.R.S. § 13-52.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Colorado Post-Judgment Procedure

> **NOT LEGAL ADVICE.** This skill addresses procedure once a
> Colorado judgment has been entered. Verify every step against
> current law before filing or responding.

Use this skill in addition to `co-statewide-format` when the case is
**past judgment** — whether you are attacking the judgment, defending
against collection, or collecting on it.

## Two paths after judgment

1. **Attack the judgment** — motions for new trial under C.R.C.P.
   59, relief from judgment under C.R.C.P. 60, appeal under C.A.R.
   3 and 4.
2. **Collect or resist collection** — supplemental proceedings under
   C.R.C.P. 69, garnishment under C.R.S. § 13-54.5, exemptions
   under C.R.S. § 13-54, debtor exam, judgment lien, eventual
   satisfaction or expiration.

## Attacking the judgment

### C.R.C.P. 59 — Motion for new trial / amend findings

- **Deadline**: 14 days after entry of judgment (C.R.C.P. 59(a))
- **Grounds**: error in law, irregularity in proceedings, newly
  discovered evidence, surprise, jury misconduct, etc.
- **Effect on appeal**: a timely C.R.C.P. 59 motion **tolls** the
  appeal deadline (C.A.R. 4(a)(2))

### C.R.C.P. 60(b) — Relief from final judgment

- **Deadlines**:
  - 60(b)(1) **mistake, inadvertence, surprise, excusable neglect**:
    within a reasonable time, **not more than 182 days** (≈ 6 months)
  - 60(b)(2) **newly discovered evidence**: same 182-day cap
  - 60(b)(3) **fraud, misrepresentation, misconduct**: same 182-day
    cap
  - 60(b)(4) **void judgment** (lack of jurisdiction, due process):
    no time limit
  - 60(b)(5) **judgment satisfied, released, or no longer equitable**:
    reasonable time
- **Most common use**: setting aside **default judgments** —
  particularly in consumer debt-buyer cases where the defendant was
  not properly served. *See* `co-consumer-debt` for the
  default-judgment attack template.
- **Standard for default**: "good cause" plus a meritorious defense;
  see *Goodman Assocs., LLC v. WP Mountain Props., LLC*, 222 P.3d 310
  (Colo. 2010)

### Notice of Appeal — C.A.R. 3 and 4

- **Deadline**: **49 days** from entry of judgment (C.A.R. 4(a)) —
  or 49 days from disposition of a timely C.R.C.P. 59 motion
- **Where to file**: Colorado Court of Appeals (state appeals);
  Colorado Supreme Court if direct review applies
- **Fees**: filing fee plus transcript and record fees
- **Pro se appeals**: JDF 1402 (limited jurisdiction); the
  Colorado Appellate Practice Guide is the leading reference

## Collecting / resisting collection

### Judgment lien — automatic on real estate

Under **C.R.S. § 13-52-102**, a judgment of a Colorado court
automatically becomes a **lien on the judgment debtor's real
property** in the county where the judgment is recorded with the
county clerk and recorder. Steps:

1. Obtain a **certified copy of the judgment** from the clerk
2. **Record** with the county clerk and recorder of any county where
   the debtor owns or might acquire real estate
3. The lien is good for **6 years** from the date of judgment and may
   be revived (see below)

### Writ of Continuing Garnishment — C.R.S. § 13-54.5-104

Wage garnishment is by **Writ of Continuing Garnishment**, which
attaches to **future earnings** for up to **6 months** at a time
before requiring renewal.

- **Form**: JDF 82 (Writ of Continuing Garnishment)
- **Amount**: up to **25% of disposable earnings per week** or **the
  amount by which weekly earnings exceed 40 × Colorado minimum
  wage**, whichever is less (C.R.S. § 13-54.5-101.5; mirrors federal
  CCPA but with Colorado-specific minimum-wage anchor)
- **Service**: serve on the **employer (garnishee)**; serve the
  **judgment debtor** by mail within 7 days
- **Garnishee's answer**: due within **7 days** of receipt (C.R.S.
  § 13-54.5-106(2))
- **Debtor's objection / claim of exemption**: within **14 days** of
  receipt of the writ

### Writ of Garnishment with Notice of Exemption — non-wage assets

For bank accounts and other non-wage assets, use the **Writ of
Garnishment** with the notice-of-exemption form (JDF 84). The debtor
has **14 days** to file a Claim of Exemption.

### Colorado exemptions — C.R.S. art. 54 of title 13

Colorado has a robust state-law exemption framework. Key exemptions:

| Item | Amount / scope | Statute |
|---|---|---|
| Homestead | **$250,000** equity (or $350,000 if owner is 60+, disabled, or homestead for an elderly / disabled family member) | C.R.S. § 38-41-201 |
| Motor vehicle | $7,500 ($12,500 if owner is 60+ or disabled) | C.R.S. § 13-54-102(1)(j) |
| Household goods | $7,500 | C.R.S. § 13-54-102(1)(e) |
| Wearing apparel | $3,000 | C.R.S. § 13-54-102(1)(a) |
| Watches and jewelry | $2,500 (pieces total) | C.R.S. § 13-54-102(1)(b) |
| Library, books, family pictures | $3,000 | C.R.S. § 13-54-102(1)(c) |
| Tools of trade | $30,000 | C.R.S. § 13-54-102(1)(i) |
| Public benefits (TANF, SSI, unemployment) | Fully exempt | C.R.S. § 13-54-102(1)(n) |
| Social Security | Fully exempt | C.R.S. § 13-54-102(1)(l); 42 U.S.C. § 407 |
| Earnings (after garnishment cap) | 75% disposable per week | C.R.S. § 13-54-104 |
| ERISA pension / 401(k) / IRA | Fully exempt | C.R.S. § 13-54-102(1)(s); 29 U.S.C. § 1056 |
| Health-savings account | Fully exempt | C.R.S. § 13-54-102(1)(u) |
| Personal-injury settlements | Variable | C.R.S. § 13-54-102(1)(n)(II) |

The exemption amounts above reflect the 2022 SB22-086 expansion
("Increasing Protections for Colorado Consumers"); they are
adjusted periodically for inflation.

**Claim of Exemption** procedure (C.R.S. § 13-54.5-108):

1. Within 14 days of garnishment notice, file written **Claim of
   Exemption** (JDF 84) with the issuing court
2. Court holds a hearing within 14 days
3. Garnishee must hold the funds pending the hearing

### Supplemental proceedings — C.R.C.P. 69

- **Debtor's exam**: judgment creditor may compel the debtor to
  appear and answer questions about assets (C.R.C.P. 69)
- **Order to appear**: use JDF 90 (Citation to Appear) — debtor must
  appear at the time and place stated
- **Failure to appear**: contempt; bench warrant possible
- **Document subpoena**: creditor may subpoena bank records and other
  documents

### Satisfaction of judgment — C.R.S. § 13-52-110

When the judgment is paid in full, the creditor must file a
**Satisfaction of Judgment** with the court within **21 days** of
the debtor's written demand. Failure to do so timely subjects the
creditor to a $100 statutory penalty plus actual damages plus
attorneys' fees.

If the creditor refuses, the debtor may file a **Motion for Entry
of Satisfaction** with proof of payment.

### Judgment revival — C.R.S. § 13-52-102

A Colorado judgment is good for **6 years** and may be revived by
**Scire Facias** filed before expiration. After revival, the
judgment is enforceable for another 6 years. After 20 years from
the original entry, the judgment is conclusively presumed paid.

## Common pro se post-judgment scenarios

1. **Default judgment in a debt-buyer case** — file C.R.C.P. 60(b)(1)
   motion to set aside within 182 days, asserting lack of service or
   excusable neglect plus a meritorious defense (chain of title, SOL,
   licensure under CFDCPA, etc.). See `co-consumer-debt`.
2. **Garnishment of bank account containing Social Security** —
   file Claim of Exemption (JDF 84) within 14 days; the SSA funds are
   fully exempt under 42 U.S.C. § 407.
3. **Wage garnishment when debtor is sole earner with dependents** —
   the 25% cap or 30-times-minimum-wage floor applies; if debtor
   qualifies, the **head-of-household** exemption may also apply
   under C.R.S. § 13-54-104.
4. **Old judgment** — check the 6-year revival clock; if not revived
   timely, the judgment is unenforceable.

## Composition

- For statewide format: `co-statewide-format`
- For drafting the motion to set aside default: `co-draft-motion`
- For supporting affidavits / declarations: `co-draft-declaration`
- For debt-buyer-specific defenses: `co-consumer-debt`
- For deadlines: `co-deadlines`

## References

- `references/crcp-59-60.md` — full text of C.R.C.P. 59 and 60 with
  notes
- `references/garnishment.md` — Colorado's two writs (continuing /
  non-continuing); JDF 82 / 83 / 84 forms
- `references/exemptions.md` — full table of Colorado exemptions with
  case authority
- `references/supplemental-proceedings.md` — C.R.C.P. 69 debtor exam
  workflow
- `references/judgment-liens.md` — recording, duration, revival,
  satisfaction
- `references/appellate-procedure.md` — Notice of Appeal timing,
  designation of record, briefing schedule
