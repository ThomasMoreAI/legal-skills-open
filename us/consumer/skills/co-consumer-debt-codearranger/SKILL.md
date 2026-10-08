---
name: co-consumer-debt-codearranger
title: Colorado Consumer-Debt Defense
description: 'Use when defending a Colorado consumer-debt case — debt-buyer suits, collection actions. Covers **FDCPA + Reg F**, **Colorado Fair Debt Collection Practices Act (CFDCPA — C.R.S. art. 16 of title 5)** with **licensure requirement** (C.R.S. § 5-16-115), **Colorado Consumer Protection Act (CCPA — C.R.S. art. 1 of title 6)** with **treble damages**, **UCCC (C.R.S. art. 1-9 of title 5)**, **chain of title under Colorado UCC Article 9**, and **6-year SOL on credit-card debt**. Triggers: "Colorado debt-buyer lawsuit", "Midland Credit Colorado", "CFDCPA", "Colorado consumer protection", "chain of title Colorado".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
---

# Colorado Consumer-Debt Defense

> **NOT LEGAL ADVICE.** This skill provides drafting and analytical
> support for defending consumer-debt suits. Consult a licensed
> Colorado attorney about your specific case.

Use this subject-matter bundle when a Colorado consumer has been
sued by a **debt collector** — typically a **debt buyer** (Midland
Credit Management, Portfolio Recovery Associates, Cavalry SPV, LVNV
Funding, Unifin, etc.) or a **debt collection agency** acting for
an original creditor.

## The Colorado consumer-debt landscape

Colorado has a layered framework regulating debt collection:

### Federal layer

- **FDCPA** (Fair Debt Collection Practices Act), 15 U.S.C. §§ 1692-1692p
- **FCRA** (Fair Credit Reporting Act), 15 U.S.C. § 1681
- **TILA** (Truth in Lending Act), 15 U.S.C. § 1601
- **Reg F** (12 C.F.R. pt. 1006), effective November 30, 2021;
  CFPB-promulgated regulation interpreting FDCPA
- **Reg V** (12 C.F.R. pt. 1022), FCRA implementation

### Colorado state layer

- **Colorado Fair Debt Collection Practices Act (CFDCPA)** —
  formerly C.R.S. art. 16 of title 12, **recodified in 2022 at
  C.R.S. art. 16 of title 5** as part of the Uniform Consumer Credit
  Code consolidation. The Colorado AG's Collection Agency Board
  enforces.
- **Colorado Consumer Protection Act (CCPA)** — C.R.S. art. 1 of
  title 6. Treble damages plus attorneys' fees on certain claims.
- **Uniform Consumer Credit Code (UCCC)** — C.R.S. art. 1-9 of
  title 5. Caps on rates and fees; administered by the Colorado AG.
- **Colorado Uniform Commercial Code** — C.R.S. art. 1-11 of title 4.
  Article 9 governs assignments and security interests.

> **Recodification note**: Effective July 1, 2022, the Colorado
> legislature moved the Colorado FDCPA from Title 12 to Title 5
> (HB22-1024 / SB22-013). Many older cases and resources cite the
> old C.R.S. art. 14 of title 12 numbers. The substantive provisions
> are largely unchanged but the section numbers are different. When
> citing, use the **current** Title 5 sections.

## The five fact patterns

Most Colorado consumer-debt-buyer cases fall into one of five
fact patterns. The defense strategy varies by pattern.

### Pattern 1 — Stale credit-card debt by an out-of-state debt buyer

A debt buyer (e.g., Midland Credit Management, headquartered in
California) sues a Colorado consumer in Colorado county court on a
credit-card account where the last payment was made 4-6+ years ago.

- **SOL**: The credit-card account is on the cusp of the 6-year SOL
  under C.R.S. § 13-80-103.5(1)(a). Verify the date of last
  payment.
- **Chain of title**: The debt was originated by Bank of America
  → sold to a Tier-1 buyer → sold to Tier-2 → sued by Tier-2 or
  Tier-3. Each transfer requires Article 9 documentation. Defense:
  request the Bill of Sale, Assignment, and account-level data
  proving Plaintiff owns this specific account.
- **CFDCPA licensure**: Under C.R.S. § 5-16-115, a collection
  agency must be **licensed** in Colorado to collect consumer
  debts. Verify on the Colorado AG's collection-agency licensee
  list. Unlicensed collection = void collection.

### Pattern 2 — Debt buyer suing on the original creditor's contract

Same as Pattern 1 but Plaintiff attaches the **original creditor's
cardholder agreement** to the complaint. Defense:

- **Standing**: Plaintiff is not the original creditor. The
  cardholder agreement does not establish Plaintiff's standing.
- **Article 9**: Plaintiff must prove assignment under C.R.S.
  § 4-9-201 et seq.

### Pattern 3 — Collection lawsuit on a medical debt

A collection agency sues for medical debt. Layered considerations:

- **NSA (No Surprises Act)** — federal law (effective 2022) bars
  certain billing practices and may render the debt unenforceable.
- **HIPAA disclosure** — the FDCPA and CFDCPA limit disclosure of
  health information.
- **Colorado-specific medical-debt protections** — HB23-1126
  (effective 2023) places caps on medical-debt collection actions.

### Pattern 4 — Default judgment already entered

Consumer was sued, never properly served, and a default judgment was
entered against them. Discovery (often through garnishment notice).

- **C.R.C.P. 60(b)(1)** — within 182 days, motion to set aside for
  excusable neglect plus meritorious defense
- **C.R.C.P. 60(b)(4)** — no time limit if judgment is **void**
  (e.g., never served, no jurisdiction)
- **Meritorious defense** — chain of title, SOL, CFDCPA violations

### Pattern 5 — Counterclaim under FDCPA / CCPA / CFDCPA

Consumer was sued; defenses + counterclaims include:

- **FDCPA** — federal counterclaim for violation of § 1692e
  (misleading representations), § 1692f (unfair practices),
  § 1692g (validation notice)
- **CFDCPA** — Colorado counterclaim under C.R.S. § 5-16-113 (one-
  year SOL)
- **CCPA** — Colorado counterclaim with treble damages under C.R.S.
  § 6-1-113 if a "significant public impact" can be shown

## The CFDCPA — Colorado's analog to the FDCPA

The CFDCPA (C.R.S. art. 16 of title 5) parallels the federal FDCPA
with **Colorado-specific** features:

| Provision | Federal FDCPA | Colorado CFDCPA |
|---|---|---|
| Validation notice | § 1692g — 30 days | C.R.S. § 5-16-109 — 30 days |
| Communication restrictions | § 1692c | C.R.S. § 5-16-105 |
| Harassment | § 1692d | C.R.S. § 5-16-106 |
| False or misleading representations | § 1692e | C.R.S. § 5-16-107 |
| Unfair practices | § 1692f | C.R.S. § 5-16-108 |
| Licensure requirement | NONE — federal law has no licensure | **Required** — C.R.S. § 5-16-115 |
| Private right of action | § 1692k | C.R.S. § 5-16-113 |
| Statute of limitations | 1 year | 1 year |
| Damages | Up to $1,000 statutory + actual + fees | Up to $1,000 statutory + actual + fees |
| Class actions | Yes (1% of net worth, capped) | Yes (similar cap) |

The **licensure requirement** is Colorado's main distinctive. Under
C.R.S. § 5-16-115, a collection agency must be licensed by the
Colorado Administrator of the UCCC (operating through the AG's
Collection Agency Board) to collect consumer debts in Colorado.
Unlicensed collection is per se a CFDCPA violation and arguably
voids the underlying collection attempts.

## The CCPA — broader consumer protection

The Colorado Consumer Protection Act, C.R.S. art. 1 of title 6,
prohibits **deceptive trade practices**, including (per C.R.S.
§ 6-1-105(1)(u)) **failing to provide accurate or complete
information** in a consumer transaction.

CCPA features that matter in debt-collection cases:

- **Standing** — private right of action under C.R.S. § 6-1-113
- **Damages** — **3x actual damages or $500 (whichever is greater)**
  under C.R.S. § 6-1-113(2)(a)
- **Attorneys' fees** — mandatory to prevailing consumer under
  C.R.S. § 6-1-113(2)(b)
- **SOL** — 3 years from accrual under C.R.S. § 6-1-115
- **"Significant public impact" requirement** — *Hall v. Walter*,
  969 P.2d 224 (Colo. 1998), requires the consumer to show that
  the practice **significantly impacts the public** beyond a single
  transaction. This is a real hurdle in single-plaintiff cases —
  often defeated by showing the defendant's pattern across many
  consumers.

## SOL on credit-card debt — 6 years

**Colorado SOL on credit-card debt = 6 years** under C.R.S.
§ 13-80-103.5(1)(a) ("any liquidated debt or any unliquidated,
determinable amount of money"). This was settled by *Hassler v.
Account Brokers of Larimer Cnty., Inc.*, 2012 CO 24 (post-2003
amendment moved most consumer credit obligations to the 6-year
provision).

**Watch for revival**: a written acknowledgment of the debt or a
partial payment **restarts** the 6-year clock under C.R.S.
§ 13-80-113. Debt buyers often try to revive stale debts by
soliciting a small payment ("Pay just $25 today"). The 6-year clock
resets only with a written acknowledgment that is **specific to the
debt** — not a generic settlement letter.

## Chain of title — Colorado UCC Article 9

Colorado's UCC Article 9 (C.R.S. art. 9 of title 4) governs
assignments of accounts. A debt buyer must trace the chain of title
from the original creditor through every intermediate buyer to
itself with:

- **Bill of Sale** for each transfer
- **Assignment** specifically identifying the account (account number
  or unique identifier)
- **Account-level data** matching the specific consumer's account

A bill of sale that references "an attached portfolio" but does not
attach the portfolio is **insufficient**. A bill of sale that refers
to "all accounts purchased on [date]" without specifically tying to
this consumer's account is **insufficient**. See *Mercer v. JPMorgan
Chase Bank, N.A.*, 2018 COA 13, and similar Colorado authority on
the standing burden.

The **RFP bank** in `references/rfp-debt-buyer.md` targets each
link in the chain.

## Affirmative defenses — Colorado debt-buyer answer

In the answer, plead all that apply:

1. **Failure to state a claim** (C.R.C.P. 12(b)(5)) — pleading
   inadequate to allege chain of title or specific account terms
2. **Statute of limitations** (C.R.S. § 13-80-103.5(1)(a)) — 6 years
   from date of default
3. **Lack of standing** — debt buyer cannot prove ownership of this
   specific account
4. **CFDCPA licensure** (C.R.S. § 5-16-115) — Plaintiff is not a
   licensed Colorado collection agency
5. **Account stated** — no agreed accounting between this
   Plaintiff and Defendant
6. **Lack of consideration / failure of consideration**
7. **Lack of privity** between Plaintiff and Defendant
8. **Estoppel / waiver** — based on creditor conduct
9. **Payment / accord and satisfaction**
10. **Identity theft** (if applicable) — FCRA § 605B
11. **Discharge in bankruptcy** (if applicable)
12. **CCPA violation** (raised as counterclaim, but also affirmative)

See `references/affirmative-defenses.md` for the annotated catalog.

## Discovery strategy

The discovery-and-MTC playbook in a Colorado debt-buyer case
(filed in **county court** — see `co-discovery` for county-court
limitations):

1. **First Set of RFAs** — admissions on the elements (no
   contract, no assignment, no statement of account, etc.)
2. **First Set of Interrogatories** — chain of title, custodian,
   account-level data
3. **First Set of RFPs** — bills of sale, assignments, original
   contract, statements, account-level data, electronic records
4. **Subpoena to original creditor** — verifying chain of title
5. **Meet-and-confer** — formal letter when responses are deficient
6. **Motion to Compel** with C.R.C.P. 37(a)(5) fees

The full RFP / RFA / Interrogatory banks live in the references.

## Counterclaim package

Where the facts support it, file a counterclaim alleging:

- **FDCPA** violation (federal claim, 1-year SOL from violation)
- **CFDCPA** violation (state claim, 1-year SOL)
- **CCPA** violation (state claim, 3-year SOL; 3x damages + fees)
- **Common-law claims** if applicable (abuse of process, malicious
  prosecution — high bar)

Counterclaims are typically **compulsory** under C.R.C.P. 13(a)
when they arise from the same transaction — file them at the time of
answer to avoid waiver.

## Composition

- For statewide format: `co-statewide-format`
- For drafting the answer: `co-draft-motion`,
  `co-first-30-days`
- For drafting the declaration: `co-draft-declaration`
- For drafting the proposed order: `co-draft-order`
- For motion-to-compel mechanics: `co-discovery`, `co-draft-motion`
- For court overlay (typically **county court** at this dollar
  amount): `co-county-courts`
- For setting aside default: `co-post-judgment`
- For deadlines: `co-deadlines`
- For QC: `co-quality-check`, `co-fact-check`

## References

- `references/fdcpa.md` — FDCPA § 1692 et seq. annotated
- `references/reg-f.md` — Regulation F at 12 C.F.R. pt. 1006
- `references/co-cfdcpa.md` — Colorado FDCPA (C.R.S. art. 16 of
  title 5)
- `references/co-ccpa.md` — Colorado CPA (C.R.S. art. 1 of title 6)
- `references/co-uccc.md` — Colorado UCCC (C.R.S. art. 1-9 of
  title 5)
- `references/co-collection-agency-licensure.md` — C.R.S. § 5-16-115
  licensing requirement
- `references/co-statutes-of-limitations.md` — Colorado SOL on debt
- `references/chain-of-title.md` — Article 9 doctrine in Colorado
- `references/evidence-debt-buyer.md` — CRE 803(6) / 902(11)
  foundation in Colorado courts
- `references/rfp-debt-buyer.md` — Request for Production bank
- `references/rfa-debt-buyer.md` — Request for Admission bank
- `references/interrogatories-debt-buyer.md` — Interrogatory bank
- `references/meet-and-confer-debt-buyer.md` — M&C letter templates
- `references/affirmative-defenses.md` — annotated catalog
- `references/key-cases.md` — Colorado debt-buyer case law
- `references/recent-decisions.md` — recent decisions to track
- `references/fees-consumer-debt.md` — fee mechanics in debt cases
- `references/ucc-article-9.md` — Colorado UCC Article 9 enactment
- `references/online-sources-consumer-debt.md` — canonical URLs
