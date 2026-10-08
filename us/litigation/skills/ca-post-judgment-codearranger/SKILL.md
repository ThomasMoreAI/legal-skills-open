---
name: ca-post-judgment-codearranger
title: California Post-Judgment Procedure
description: Use to navigate post-judgment procedures in California. Triggers include "I got a default judgment entered against me", "how do I vacate a default", "motion to vacate judgment", "wage garnishment California", "claim of exemption", "EJ-160", "WG-006", "judgment debtor exam", "satisfaction of judgment", "EJ-100", "writ of execution California", "renew a judgment", "new trial motion", "CCP 473", "CCP 657", "CCP 663". Covers Code of Civil Procedure §§ 473 (relief from default/order — 6-month window), 657 (new trial), 663 (vacate non-jury judgment), 685.010–685.030 (enforcement), 695–697 (judgment lien), 706–708 (wage garnishment and levy), 724.010–724.260 (satisfaction of judgment including 15-day demand).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Exemptions
  path: references/exemptions.md
- title: Garnishment Response
  path: references/garnishment-response.md
- title: Motion To Vacate
  path: references/motion-to-vacate.md
- title: Satisfaction Of Judgment
  path: references/satisfaction-of-judgment.md
- title: Supplemental Proceedings
  path: references/supplemental-proceedings.md
---

# California Post-Judgment Procedure

When a judgment has been entered in a California civil case, a
separate body of rules governs what happens next. This skill
covers two angles:

1. **A judgment was entered against the defendant** — and they
   want to vacate it or seek a new trial.
2. **A judgment creditor is collecting** — garnishment, bank levy,
   supplemental proceedings — and the debtor needs to know their
   rights and exemptions.

> **NOT LEGAL ADVICE.** Post-judgment timing is unforgiving.
> Verify each deadline and consult a licensed attorney where the
> stakes are significant.

## Core principles

1. **Relief from default has a 6-month hard cap** — Code Civ.
   Proc., § 473(b) mandatory relief requires an attorney's sworn
   affidavit of fault; discretionary relief requires a showing of
   mistake, inadvertence, surprise, or excusable neglect. Both are
   cut off at 6 months from entry of order or dismissal.
2. **Exemptions must be claimed promptly** — most exemption claims
   under Code Civ. Proc., § 703.510 et seq. must be filed within
   10 days of service of the notice of levy or the enforcement
   officer's instructions to the third-party garnishee.
3. **Debtor exam responses are mandatory** — a judgment-debtor
   examination (Code Civ. Proc., § 708.110) is a court order;
   failure to appear can result in a bench warrant and contempt.
4. **A California judgment lasts 10 years** (Code Civ. Proc.,
   § 683.020) and can be renewed for successive 10-year periods
   under §§ 683.110–683.220. Interest accrues at 10% per annum
   under Code Civ. Proc., § 685.010.
5. **Satisfaction must be acknowledged** — once paid in full, the
   creditor must file an acknowledgment of satisfaction of judgment
   (Form EJ-100) within 15 days of a written demand (Code Civ.
   Proc., § 724.050(d)).

## Relief from judgment or default

### Code Civ. Proc., § 473 — the main relief statute

Section 473 has two distinct branches:

#### Mandatory relief — § 473(b) attorney-fault affidavit

If the default or dismissal resulted from the attorney's mistake,
inadvertence, surprise, or neglect, the court **must** vacate the
default or dismissal if the attorney files a sworn affidavit of
fault (and provides relief no later than 6 months after entry of
judgment, dismissal, order, or other proceeding). The defendant
must also pay any fees the court determines are appropriate.

Key cases:
- *Zamora v. Clayborn Contracting Group, Inc.* (2002) 28 Cal.4th
  249 — mandatory relief under § 473(b) is available for orders
  of dismissal entered after attorney's failure to appear; the
  word "default" in the statute encompasses the equivalent of a
  default for failure to respond.
- *SJP Limited Partnership v. City of Los Angeles* (2006) 136
  Cal.App.4th 511 — the attorney affidavit of fault must be sworn
  and unambiguous about the nature of the attorney's mistake.

#### Discretionary relief — § 473(b)

On motion made within 6 months after entry of judgment, the court
**may**, in its discretion, relieve a party from a judgment,
dismissal, order, or other proceeding taken against the party
through:

- **Mistake** (of law or fact)
- **Inadvertence**
- **Surprise**
- **Excusable neglect**

The motion must be accompanied by a copy of the answer or other
pleading proposed to be filed (Code Civ. Proc., § 473(b)).

**6-month deadline**: the 6-month limit runs from the date the
order, judgment, or dismissal was entered. It is jurisdictional
for discretionary relief.

Pro se defendants who missed the response deadline because they
did not understand the deadline or could not read English have
obtained relief under the "excusable neglect" prong, but the
showing must be supported by a detailed declaration. See
`references/motion-to-vacate.md`.

### Code Civ. Proc., § 473(d) — void judgment

A void judgment may be set aside at any time — there is no
6-month cap. Grounds for voidness include lack of personal
jurisdiction (defective service), lack of subject-matter
jurisdiction, or a judgment that exceeds the court's power.
The statute of limitations does not run on a motion to vacate a
void judgment.

### Code Civ. Proc., § 663 — motion to vacate after non-jury trial

After a non-jury trial, the court may vacate the statement of
decision and judgment and enter a different judgment if the
decision fails to express or misapplies the law. The motion must
be filed within 15 days after service of written notice of entry
of judgment (Code Civ. Proc., § 663a). This is a narrow remedy
— it does not allow re-trial of factual questions, only
correction of legal error.

### Code Civ. Proc., § 657 — new trial

A party may move for a new trial on any or all issues on the
following grounds: (1) irregularity in the proceedings; (2)
misconduct of jury; (3) accident or surprise; (4) newly
discovered evidence; (5) excessive or inadequate damages;
(6) insufficiency of evidence to justify verdict; (7) error in
law. The motion must be filed within 15 days after service of
notice of entry of judgment (Code Civ. Proc., § 659).

### Stay of execution pending motion

Filing a motion to vacate does NOT automatically stay
enforcement. To stop collection while the motion is pending,
file a **motion for stay** (Code Civ. Proc., § 918) with a
showing of likely success on the merits and balance of hardships.
Or post a supersedeas bond.

## Enforcement of judgments

### Interest on judgment — Code Civ. Proc., § 685.010

Interest accrues at **10% per year** on any money judgment in
California, starting from the date of entry of judgment. This
cannot be waived by the debtor's inaction; the clock runs from
entry.

### Judgment lien — Code Civ. Proc., §§ 697.310–697.410

An abstract of judgment (Form EJ-001) recorded in the county
recorder's office of any county creates a lien on real property
the debtor owns in that county. The lien attaches automatically
to real property acquired thereafter as well. The lien lasts as
long as the judgment is enforceable (i.e., 10 years, renewable).

### Writ of execution — Code Civ. Proc., § 699.510

The judgment creditor obtains a writ of execution (Form EJ-130)
from the clerk. The writ directs the levying officer (sheriff or
marshal) to enforce the judgment against the debtor's property.

## Wage garnishment

### Earnings withholding order — Code Civ. Proc., § 706.010 et seq.

An earnings withholding order (Form EJ-150) is served on the
debtor's employer. The employer must withhold a portion of each
paycheck and pay it to the levying officer. The limits:

- **25% of disposable earnings** per pay period, OR
- The amount by which disposable earnings exceed **30 times the
  federal minimum wage** per week, whichever is LESS.
  (Code Civ. Proc., § 706.050; aligned with CCPA / 15 U.S.C.
  § 1673.)
- "Disposable earnings" = gross pay minus legally required
  deductions (FICA, state income tax, SDI, etc.).

**Claim of Exemption — Earnings (Form WG-006)**: the debtor
files the claim of exemption plus a financial statement
(Form WG-007) within **10 days** of service of the earnings
withholding order. The court then schedules a hearing.

### Bank levy

The writ is served on the debtor's financial institution. The
bank must withhold (freeze) funds in accounts. The debtor has
10 days to claim an exemption by filing Form EJ-160 (Claim of
Exemption — Property Levy).

Federal benefits protected under 31 C.F.R. § 212 (bank must
protect 2 months of direct-deposited federal benefits from
garnishment automatically).

See `references/garnishment-response.md` for step-by-step
procedure and form checklist.

## Supplemental proceedings

### Judgment-debtor examination — Code Civ. Proc., § 708.110

After judgment, the creditor may obtain a court order requiring
the judgment debtor to appear and answer questions about assets,
income, and sources of payment. Steps:

1. Creditor files an application (typically an ex parte order
   on Form SC-134 or a noticed motion).
2. Court issues the order to appear (served personally on
   the debtor — at least **10 days** notice).
3. Debtor appears, is sworn, and answers questions under penalty
   of perjury.
4. Creditor may also subpoena documents (bank statements,
   pay stubs, tax returns) under Code Civ. Proc., § 708.130.
5. Failure to appear subjects the debtor to **contempt** and a
   bench warrant.

The debtor may claim exemptions during the exam on the record
— name the property and the statutory basis.

### Third-party examination — Code Civ. Proc., § 708.120

The creditor may also examine a third party (e.g., the debtor's
bank or employer) believed to hold assets belonging to the debtor.

### Assignment order — Code Civ. Proc., § 708.510

The court may order the debtor to assign to the creditor rights
to receive money from a third party (e.g., a contract payment,
rent, royalties). The assignment order acts like a continuing
levy on future income streams.

### Turnover order — Code Civ. Proc., § 708.205

The court may order the debtor to deliver specific personal
property to the levying officer for enforcement.

See `references/supplemental-proceedings.md` for the full guide.

## Exemption catalog

### Homestead exemption

Under Cal. Civ. Code §§ 704.710–704.850 (as amended by AB 1885,
effective January 1, 2021):

- **$300,000 to $600,000** of equity in the debtor's principal
  residence, depending on the county median home price.
- In high-cost counties (most of the Bay Area and Southern
  California), the exemption is commonly at or near $600,000.
- The amount adjusts annually based on the California median
  home price published by the Department of Housing and Community
  Development.
- Applicable only to the debtor's principal residence.

### Personal property exemptions — Code Civ. Proc., § 704.010 et seq.

| Category | Exemption amount | Code Civ. Proc. |
|---|---|---|
| Motor vehicle | $3,625 | § 704.010 |
| Household furnishings, appliances, clothing | $9,525 aggregate | § 704.020 |
| Materials / goods for home use | Reasonable amount | § 704.020 |
| Health aids (wheelchair, hearing aid) | Unlimited | § 704.050 |
| Tools of trade / business | $8,725 | § 704.060 |
| Professional library / instruments | $8,725 | § 704.060 |
| One commercial vehicle for trade | $4,850 | § 704.060 |
| Jewelry, heirlooms, art | $9,525 | § 704.040 |
| Bank account (wages deposited — 30 days) | $1,826 | § 704.080 |
| Retirement accounts (IRAs, 401k, etc.) | Unlimited if ERISA-qualified | § 704.115 |
| Social Security / SSI / veterans benefits | Unlimited (federal preemption) | Federal law |
| Workers' compensation | Unlimited | § 704.160 |
| Unemployment compensation | Unlimited | § 704.120 |
| Disability / health insurance benefits | Unlimited | § 704.130 |
| Public assistance (SNAP, CALWORKS, etc.) | Unlimited | § 704.170 |

Note: California does not allow debtors to choose between the
"California system" (Code Civ. Proc., § 704.010 et seq.) and
the federal bankruptcy exemptions (11 U.S.C. § 522(d)) — in
California courts, only the California system applies. The
Code Civ. Proc., § 703.140 "bankruptcy" exemptions apply only
when the debtor is in a federal bankruptcy case.

See `references/exemptions.md` for the full annotated list.

## Satisfaction of judgment

When a judgment has been paid in full, the creditor must
acknowledge satisfaction:

1. **Demand letter**: the debtor (or their attorney) sends a
   written demand under Code Civ. Proc., § 724.050 requiring
   the creditor to file an acknowledgment of satisfaction.
2. **15-day deadline**: within 15 days of the demand (and after
   full payment), the creditor must execute and file Form EJ-100
   (Acknowledgment of Satisfaction of Judgment) in the court
   that entered the judgment.
3. **Penalty for failure**: if the creditor fails to file within
   the 15-day period after demand, the debtor may recover
   $100 statutory damages plus actual damages (Code Civ. Proc.,
   § 724.080).
4. **Court order**: if the creditor refuses, the debtor may
   move the court for an order requiring the creditor to file the
   satisfaction (Code Civ. Proc., § 724.050(e)).
5. **Partial satisfaction** (Form EJ-100 also covers partial
   satisfaction): filed when part of the judgment has been paid.

See `references/satisfaction-of-judgment.md` for the demand
letter template and Form EJ-100 instructions.

## Judgment renewal — Code Civ. Proc., §§ 683.110–683.220

A money judgment is enforceable for **10 years** from the date
of entry (Code Civ. Proc., § 683.020). To extend enforcement,
the judgment creditor must file an application for renewal of
judgment (Form EJ-190) **before** the 10-year period expires.
Once renewed, the judgment is enforceable for 10 more years
from the date of renewal. Multiple renewals are permitted.

For the debtor: if the creditor never renewed, the judgment is
unenforceable after 10 years. Verify the entry date and check
whether a renewal was ever filed in the case docket.

## Pro se post-judgment checklist

After receiving any post-judgment paper:

- [ ] **Identify the type** (earnings withholding order, writ of
      execution, application for debtor exam, demand for
      satisfaction, etc.)
- [ ] **Photograph the document and the envelope** — preserve
      the postmark and method of service
- [ ] **Calendar all deadlines** (10 days for earnings
      exemption claim; 10 days for bank levy exemption; 6
      months for § 473 motion to vacate; debtor exam date)
- [ ] **Identify which skill applies** — vacate? garnishment?
      exam? satisfaction?
- [ ] **Pull the relevant reference** from `references/`
- [ ] **Draft the response** using the corresponding form or
      motion template
- [ ] **eFile** via the county's e-filing system
- [ ] **Serve the creditor** with a proof of service (Form
      POS-030)
- [ ] **Attend any scheduled hearing** — see `ca-hearings`

## Cross-references

- `references/motion-to-vacate.md` — CCP § 473(b) motion,
  checklist and template
- `references/garnishment-response.md` — earnings withholding
  order response; bank levy; Forms EJ-150, WG-006, EJ-160
- `references/exemptions.md` — full California exemption catalog
  with CCP citations
- `references/supplemental-proceedings.md` — debtor exam
  preparation
- `references/satisfaction-of-judgment.md` — Form EJ-100 and
  the § 724.050 demand procedure
- `ca-deadlines` — exact date computation
- `ca-draft-motion` — motion structure
- `ca-draft-declaration` — supporting declaration
- `ca-quality-check` — pre-filing format check
- `ca-file-packet` — final packet assembly

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
