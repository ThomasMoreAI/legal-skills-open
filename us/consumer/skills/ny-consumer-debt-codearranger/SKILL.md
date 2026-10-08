---
name: ny-consumer-debt-codearranger
title: New York Consumer-Debt Defense
description: Subject-matter bundle for New York consumer-debt defense. Triggers include 'defending a debt-collection lawsuit in New York', 'NYC Civil Court debt case', 'sued for credit card debt in NY', 'CPLR 213(a) 3-year SOL', 'Consumer Credit Fairness Act', 'CCFA 2022 New York', 'GBL § 349 deceptive practices', 'NY GBL § 600 collection agency', 'debt buyer', 'chain of title', 'sewer service', 'FDCPA in New York'. Covers **FDCPA + Regulation F**, **2022 Consumer Credit Fairness Act** (3-year SOL at CPLR 213(a), CPLR 3015(e) heightened pleading, 22 NYCRR § 202.27-a heightened default-judgment evidence, CPLR 308(six) additional mailing), **NY GBL § 600** collection-agency licensing, **GBL § 349** deceptive acts, **CPLR 4544** small-print contracts, **chain of title** under NY UCC Article 9, fact-pattern triage, and RFP/RFA banks.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
---

# New York Consumer-Debt Defense

> **NOT LEGAL ADVICE.** Consumer-debt defense is a specialty
> with high stakes; this bundle is a drafting aid for pro se
> defendants. Verify every statute and rule before filing.

## The New York consumer-debt landscape

Three filing forums:

1. **Civil Court of the City of New York** — under $50,000;
   the **largest consumer-debt forum in the state** by case
   count. Covered by `ny-county-courts`.
2. **Supreme Court** — over $50,000 (rare for pure consumer
   debt; common for mixed claims or judgment-revival). The
   five flagship counties.
3. **Nassau / Suffolk District Court + upstate City
   Courts** — long-tail jurisdictions for smaller debts.

## The 2022 Consumer Credit Fairness Act (CCFA)

L 2021, ch 593, effective April 7, 2022. The most
significant consumer-debt reform in NY in decades. Four key
provisions:

### CCFA § 1 — CPLR 213(a) — 3-year SOL on consumer credit

**Before**: 6 years (CPLR 213(2) general contract SOL)
**After**: **3 years** (new CPLR 213(a)) on any "action
arising out of a consumer credit transaction where a
purchaser, borrower or debtor is a defendant"

The SOL runs from **the default date** — the first missed
payment that triggered acceleration (case law: *Costa v.
Deutsche Bank*, 22 NY3d 159 (2013); *Lubonty v. U.S. Bank*,
34 NY3d 250 (2019)). Once the SOL runs, **revival is
limited to written acknowledgment** under N.Y. GOL § 17-101;
partial payment does NOT revive (*Lew Morris Demolition Co.
v. Bd. of Educ.*, 40 NY2d 516 (1976)).

**Practice point**: For any complaint filed on/after April
7, 2022 on a debt that defaulted **3+ years earlier**, file
a CPLR 3211(a)(5) motion to dismiss on SOL grounds.

### CCFA § 2 — CPLR 3015(e) — heightened pleading

The complaint in any consumer-credit action must allege:

- (a) The complete chain of title from the original
  creditor to the plaintiff
- (b) The date and substance of any account agreement
- (c) The account number (last 4 digits OK)
- (d) The date of default and the amount due as of charge-
  off
- (e) An itemization of fees/charges/interest added since
  charge-off
- (f) A statement of the date of the last payment received
  if any

Missing any of these is grounds for CPLR 3211(a)(7) motion
to dismiss.

### CCFA § 3 — 22 NYCRR § 202.27-a — heightened default-judgment

In any consumer-credit case (as defined at CPLR 105(f)):

- The plaintiff must submit **specific evidence** with the
  default application — not just an affidavit of merit
- **Required documents**:
  - The chain-of-title documents
  - The original creditor's records
  - The bill of sale and assignment
- **Required affidavits**:
  - The affidavit of merit from a person with personal
    knowledge — not a robo-signer
  - The CPLR 3215(g)(3) additional-notice mailing affidavit

Default judgments entered without compliance are routinely
vacated under CPLR 5015(a)(4) (lack of jurisdiction over the
person — defective service or process) **or** under (a)(1)
(excusable default + meritorious defense — easy to show
when § 202.27-a was not satisfied).

### CCFA § 4 — CPLR 308(six) — additional notice mailing

In consumer-credit actions, the plaintiff must mail an
additional notice to the defendant under CPLR 308(six) (the
provision was renumbered; originally CPLR 308(5)). The
notice must be in plain language and identify the original
creditor + the assignor chain.

## Substantive defenses checklist

| Defense | Authority |
|---------|-----------|
| **Statute of limitations** | CPLR 213(a) (3 yrs); CPLR 3211(a)(5) |
| **Failure to state a cause of action** (no CCFA pleading) | CPLR 3015(e); CPLR 3211(a)(7) |
| **Lack of standing / chain of title** | N.Y. UCC § 9-203; case law |
| **Sewer service** | CPLR 308; CPLR 3211(a)(8); CPLR 5015(a)(4) |
| **Lack of capacity to sue** | N.Y. GBL § 601-a (NYC license); CPLR 3211(a)(3) |
| **Account stated — no agreement to account** | CPLR 3018(b) |
| **Payment / accord and satisfaction** | CPLR 3018(b) |
| **Small-print contract** | CPLR 4544 (8-pt type) |
| **Usury** | Penal Law § 190.40 (criminal); GOL § 5-501 (civil 16%) |
| **TILA violation** (in original transaction) | 15 USC § 1640 |
| **FDCPA violation by collector** | 15 USC § 1692 — see references |
| **Reg F violation by collector** | 12 CFR § 1006 — see references |

## Counterclaims checklist

| Counterclaim | Authority |
|---|---|
| FDCPA (federal — $1,000 cap + actual + atty fees) | 15 USC § 1692k |
| GBL § 349 (NY deceptive acts — $50 min; $1,000 cap on willful) | N.Y. GBL §§ 349, 350 |
| GBL § 600 et seq. (collection-agency licensing) | N.Y. GBL §§ 600-606 |
| Common-law abuse of process | NY common law |
| Common-law malicious prosecution (post-dismissal) | NY common law |
| Defamation (if reported to credit bureau falsely after dispute) | CPLR 215(3) — 1-year SOL |

## Fact-pattern triage

The table below describes recurring fact patterns in New York consumer-debt
practice and the procedural mechanisms the CPLR makes available for each.
It is **not** a recommendation that any particular litigant pursue any
particular motion — the choice of pleading, motion, or response belongs to
the litigant (and any counsel the litigant retains). Use the table as a
map of options, not as a prescription.

| # | Pattern | Procedural mechanisms commonly considered |
|---|---|---|
| **1** | Stale credit-card debt (charge-off > 3 yrs before filing) | CPLR 3211(a)(5) motion to dismiss on SOL grounds |
| **2** | Debt buyer plaintiff missing chain-of-title docs | CPLR 3211(a)(7) motion (non-compliance with CPLR 3015(e)) |
| **3** | Default judgment entered, never served (or sewer service) | CPLR 5015(a)(4) motion to vacate |
| **4** | Default judgment entered post-CCFA without § 202.27-a evidence | CPLR 5015(a)(1) motion to vacate (excusable default + meritorious defense) |
| **5** | Active case, debt-collector calls violate Reg F | Verified answer; FDCPA / GBL § 349 counterclaim |

## Reference files

- `references/fdcpa.md` — NY-specific framing for the FDCPA
  (verbatim text in
  `ny-law-references/references/federal-debt-laws/FDCPA.md`
  symlinked to the shared plugin)
- `references/reg-f.md` — NY-specific framing for Reg F
- `references/ccfa.md` — Consumer Credit Fairness Act 2022
  text + commentary
- `references/cplr-213a.md` — 3-year SOL deep dive
- `references/cplr-3015e.md` — heightened pleading deep dive
- `references/202-27-a.md` — heightened default-judgment
  rule deep dive
- `references/gbl-349.md` — NY deceptive-acts statute
- `references/gbl-600.md` — collection-agency licensing
- `references/cplr-4544.md` — small-print contracts
- `references/chain-of-title.md` — N.Y. UCC Article 9 +
  bill-of-sale-and-assignment foundation
- `references/evidence-debt-buyer.md` — CPLR 4518 business-
  records foundation under *People v. Kennedy*, 68 NY2d
  569 (1986) and *Bank of NY Mellon v. Gordon*, 171 AD3d
  197 (2d Dept 2019)
- `references/ny-sols.md` — NY SOLs by claim type
- `references/key-cases.md` — controlling precedents
- `references/recent-decisions.md` — post-2022 CCFA case law
- `references/fees-consumer-debt.md` — fee shifting in NY
  consumer-debt (FDCPA mandatory + GBL § 349 discretionary)
- `references/rfp-debt-buyer.md` — RFP bank targeting chain
  of title
- `references/rfa-debt-buyer.md` — Notice to Admit bank
- `references/interrogatories-debt-buyer.md` — 25-interrogatory
  bank targeting chain of title (CPLR 3130 / 3133(b))
- `references/meet-and-confer-debt-buyer.md` — 22 NYCRR §
  202.20-f conferral templates
- `references/ucc-article-9.md` — N.Y. UCC Article 9
- `references/online-sources-consumer-debt.md` — canonical
  URLs

## Composition with other ny- skills

- `ny-statewide-format` — format baseline
- `ny-first-30-days` — answer triage on a consumer-debt
  complaint
- `ny-discovery` — RFP/RFA/Interrogatory drafting
- `ny-post-judgment` — CPLR 5015 vacate + Article 52 defense
- `ny-deadlines` — CPLR 213(a) 3-year SOL clock
- `ny-county-courts` — NYC Civil Court is the primary forum
- `ny-kings` / `ny-bronx` / `ny-queens` — high-volume
  Supreme Court consumer-debt counties (especially mortgage-
  foreclosure cases)
