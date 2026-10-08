---
name: ny-post-judgment-codearranger
title: New York Post-Judgment Procedure
description: Navigate post-judgment procedure in a New York civil case. Triggers include 'motion to vacate default in NY', 'CPLR 5015(a)', 'vacate judgment', 'wage garnishment New York', 'income execution', 'CPLR 5231', 'restraining notice', 'CPLR 5222', 'levy', 'CPLR 5232', 'CPLR 5230 sheriff levy', 'exemption claim form', 'NY EIPA', 'Exempt Income Protection Act', 'turnover proceeding', 'CPLR 5225 / 5227', 'subpoena duces tecum to bank', 'satisfaction of judgment', 'NY judgment lien', 'docketing a judgment'. Covers CPLR 5015 (vacate); CPLR Article 52 (enforcement of money judgments) including restraining notice (5222), income execution (5231), property execution (5232), the Exempt Income Protection Act (CPLR 5222-a), Form EJ-FOC-1 exemption notice, turnover proceedings (5225/5227), satisfaction of judgment (5020), and NY's 20-year SOL on money judgments (CPLR 211).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-post-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# New York Post-Judgment Procedure

> **NOT LEGAL ADVICE.** Post-judgment enforcement and
> debtor-protection rules are heavily statute-driven in NY.
> Verify the current text of every CPLR Article 52 section
> before relying.

## Motion to vacate a judgment — CPLR 5015(a)

The principal post-judgment relief mechanism. CPLR 5015(a)
allows vacatur on these grounds:

| Ground | Authority | Time limit |
|--------|-----------|-----------|
| Excusable default | CPLR 5015(a)(1) | 1 year from notice of entry |
| Newly discovered evidence | CPLR 5015(a)(2) | Reasonable time |
| Fraud / misrepresentation | CPLR 5015(a)(3) | Reasonable time |
| Lack of jurisdiction | CPLR 5015(a)(4) | No time limit |
| Reversal / modification of prior order | CPLR 5015(a)(5) | Reasonable time |

The most-litigated ground in consumer-debt cases:

### (a)(1) — Excusable default

Must show **both**:

1. **Reasonable excuse** for the default (e.g., never
   served; service was defective; medical emergency)
2. **Meritorious defense** to the underlying claim

The 1-year window runs from receipt of notice of entry, not
from the judgment date. Pro se defendants in consumer-debt
cases often miss it; the **22 NYCRR § 202.27-a** (CCFA)
heightened-evidence rule for default judgments now creates
additional grounds for vacatur where the original default
application was inadequate.

### (a)(4) — Lack of jurisdiction

If service was defective (no service, wrong address,
defective substitute service under CPLR 308) — **no time
limit** to vacate. A common pro se motion in NY Civil Court
debt-collection cases where the process server filed a
"sewer service" affidavit.

## CPLR Article 52 — Enforcement of money judgments

### Restraining Notice — CPLR 5222

A judgment creditor can serve a Restraining Notice on:

- The judgment debtor — restrains transfer of any property
  except as permitted (exemptions, periodic exempt income)
- A garnishee (bank, employer, tenant) — restrains transfer
  of money/property owed to the debtor

**Duration**: 1 year (CPLR 5222(b)).

**Limit**: A bank served with a restraining notice cannot
restrain more than **twice the amount of the judgment** in
a single account; cannot freeze more than the judgment
amount.

### Income Execution (Wage Garnishment) — CPLR 5231

10% gross wages cap; 25% disposable income cap under federal
law (CCPA, 15 USC § 1673). Process:

1. **Income execution served on judgment debtor first**
   (CPLR 5231(d)) — debtor has 20 days to pay
2. **If unpaid**, served on employer
3. Employer remits per pay period

### Property Execution / Levy — CPLR 5232

Sheriff levies on property; bank accounts, autos, etc.
**Exempt** property cannot be seized (CPLR 5205, 5206).

### Exempt Income Protection Act (EIPA) — CPLR 5222-a

A 2008 reform protecting exempt income from bank-account
restraint. When a Restraining Notice is served on a bank:

1. The bank must give the debtor a **CPLR 5222-a notice +
   exemption claim form** (EJ-FOC-1)
2. The first **$3,090** (adjusted; 2024 figure) of an
   account containing exempt income (Social Security, SSI,
   VA benefits, public assistance, alimony, child support,
   workers' comp, unemployment) is **automatically
   protected**
3. The debtor can claim additional exemption by completing
   the form

Pro se debtors should immediately complete the EJ-FOC-1 if
their account contains exempt income.

### Exemptions — CPLR 5205, 5206

Personal property exemptions (CPLR 5205):

- Necessary household furniture / appliances / clothing
- Bibles, school books, pictures (limited values)
- A wedding ring
- One motor vehicle worth ≤ **$5,275** (2024 adjustment;
  CPLR 5205(a)(8))
- Tools of trade worth ≤ **$3,825**
- Cash exemption: lesser of **$2,750** or amount available
  if no homestead claimed

Homestead exemption (CPLR 5206):

- **NYC, Nassau, Suffolk, Rockland, Westchester, Putnam:
  $165,550** (2024)
- **Albany, Columbia, Dutchess, Orange, Saratoga, Ulster:
  $137,950**
- **Rest of state: $82,775**

### Subpoena to bank / Information subpoena — CPLR 5224

Creditor can serve an information subpoena on a bank to
discover the debtor's accounts. Debtor has **7 days** to
move to quash.

### Turnover proceeding — CPLR 5225 / 5227

Special proceeding to compel a third party (bank, employer)
to turn over specific property. CPLR 5225(b) requires a
**notice of motion** in a special proceeding format
(commenced under CPLR 403).

### Satisfaction of Judgment — CPLR 5020

When the judgment is paid, the creditor **must** file a
satisfaction. Failure to do so within 20 days of debtor's
written demand exposes the creditor to **$100 + costs +
attorney's fees** under CPLR 5020(c).

## NY 20-year SOL on money judgments — CPLR 211(b)

Money judgments in NY are enforceable for **20 years** from
entry (CPLR 211(b)). Compare WA (10 years) / OR (10 years) /
CA (10 years renewable). NY's 20-year window is the longest
in the U.S. — relevant when an old judgment surfaces.

## Information subpoena practice

A common post-judgment device: serve an information subpoena
(plus questionnaire) on the debtor or a garnishee to discover
assets. Debtor must respond within 7 days; failure is
contempt (CPLR 5251).

## Composition with other ny- skills

- `ny-statewide-format` — format for the motion to vacate
  papers
- `ny-draft-motion` + `ny-draft-declaration` — scaffold the
  motion to vacate
- `ny-deadlines` — CPLR 5015(a)(1) 1-year clock
- `ny-consumer-debt` — debt-buyer cases (default vacatur is
  the most common pro se motion type)
