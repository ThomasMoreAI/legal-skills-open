---
name: or-consumer-debt-codearranger
title: Oregon Consumer-Debt Defense
description: Use this skill for Oregon consumer-debt defense — debt-buyer suits and collection cases turning on FDCPA, Regulation F, ORS 697 (Collection Agency Registration Act), or Oregon UTPA (ORS 646.605 et seq.). Triggers include "debt buyer", "collection agency sued me", "FDCPA", "1692e", "1692f", "1692g", "validation notice", "Regulation F", "UTPA", "ORS 697", "time- barred debt", "zombie debt", "re-aged debt", "chain of title", "bill of sale", "assignment schedule", "cardholder agreement", "unlicensed collection agency", "DCBS registration". Subject- matter bundle covering FDCPA / Reg F / Oregon UTPA / ORS 697 substantive law, chain-of-title doctrine, and RFP/RFA banks for debt-defense litigation. Composes with or-statewide-format, or-multcc / or-wccc / or-county-courts, or-pro-se, or-law-references, or-discovery, or-first-30-days, or-fact-check, or-deadlines, or-post-judgment, and draft-* skills.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
sources:
- title: Chain Of Title
  path: references/chain-of-title.md
- title: Evidence Debt Buyer
  path: references/evidence-debt-buyer.md
- title: Fact Patterns
  path: references/fact-patterns.md
- title: Fdcpa
  path: references/fdcpa.md
- title: Fees Consumer Debt
  path: references/fees-consumer-debt.md
- title: Interrogatories Debt Buyer
  path: references/interrogatories-debt-buyer.md
- title: Key Cases
  path: references/key-cases.md
- title: Meet And Confer Debt Buyer
  path: references/meet-and-confer-debt-buyer.md
- title: Online Sources Consumer Debt
  path: references/online-sources-consumer-debt.md
- title: Or Statutes Of Limitations
  path: references/or-statutes-of-limitations.md
- title: Ors 697
  path: references/ors-697.md
- title: Recent Decisions
  path: references/recent-decisions.md
- title: Reg F
  path: references/reg-f.md
- title: Rfa Debt Buyer
  path: references/rfa-debt-buyer.md
- title: Rfp Debt Buyer
  path: references/rfp-debt-buyer.md
- title: Ucc Article 9
  path: references/ucc-article-9.md
- title: Utpa
  path: references/utpa.md
---

# Oregon Consumer-Debt Defense

This skill is the **subject-matter bundle** for Oregon
consumer-debt litigation: debt-buyer cases, original-creditor
collection actions, and any matter turning on FDCPA / Reg F /
Oregon UTPA / ORS 697.

It assumes the procedural framework is already in place via the
matter-neutral skills. This skill adds:

- **Substantive law**: FDCPA, Reg F, Oregon UTPA, ORS 697
  Collection Agency Registration Act
- **Chain-of-title doctrine**: what a debt-buyer plaintiff
  must prove to recover
- **Evidence patterns**: business-records foundation (OEC
  803(6) / 902(11)) and authentication (OEC 901)
- **Fact-pattern triage**: 5 common debt-defense scenarios
  and the matching defenses / counterclaims
- **Discovery banks**: pre-built RFPs and RFAs targeting the
  weak spots of a debt-buyer's case
- **Example filings**: synthetic answers, declarations,
  motions, and orders for a debt-buyer-defense fact pattern

> **NOT LEGAL ADVICE.** Consumer-debt defense is fact-specific
> and outcome-dependent. This skill provides a procedural and
> substantive framework — not strategic advice for any specific
> case.

## Five common Oregon debt-defense fact patterns

### Pattern 1: Debt-buyer suit on an unfamiliar account

Defendant doesn't recognize the account, the account number,
or sometimes the original creditor. Plaintiff is a debt buyer
that purchased a pool of charged-off accounts.

**Defenses commonly raised in this pattern**:

- **Lack of standing** — Plaintiff cannot prove chain of
  title from the original creditor to itself
- **Statute of limitations** — ORS 12.080 6-year SOL may have
  run on the open account
- **Lack of registration** — Plaintiff (if a debt buyer) may
  not be registered with DCBS as required by ORS 697.015
- **OEC 803(6) / 902(11) foundation** — Plaintiff cannot
  authenticate the original creditor's records

**Counterclaims commonly considered in this pattern**:

- **FDCPA** (1692e, 1692f, 1692g) — false representations,
  unfair practices, failure to provide validation
- **Oregon UTPA** (ORS 646.605 et seq.) — equivalent state-law
  claims, often with broader remedies
- **ORS 697.085** — if plaintiff is unregistered

### Pattern 2: Original creditor collection on a known account

Defendant recognizes the account but disputes the amount, the
charges, or the validity of certain transactions.

**Defenses commonly raised in this pattern**:

- **Account stated / objection** — defendant timely disputed
  the account
- **Statute of frauds** (ORS 41.580) — for accounts requiring
  written agreement
- **Fraudulent transactions** — identity theft, unauthorized
  use
- **Statute of limitations** — ORS 12.080
- **Failure of consideration** — for goods/services not
  received

**Counterclaims**:

- **Defamation** — if creditor made false statements to
  credit bureaus
- **FCRA** (15 USC § 1681s-2) — willful or negligent
  furnishing of inaccurate information
- **Oregon UTPA** — for unfair or deceptive collection
  practices

### Pattern 3: Time-barred debt (zombie debt) revival attempt

Plaintiff is suing on a debt that is past the 6-year SOL but
claims a partial payment or written acknowledgment re-started
the clock.

**Defenses commonly raised in this pattern**:

- **Statute of limitations**, with detailed factual analysis
  of when the SOL ran
- **No revival** — under ORS 12.230, a payment alone does not
  re-start the SOL on most debts; only a **written promise to
  pay** can revive

**Counterclaims**:

- **FDCPA** (1692e(2), 1692e(5), 1692f(1)) — suing on a
  time-barred debt is misleading and unfair
- **Oregon UTPA** — equivalent

### Pattern 4: Default judgment entered improperly

Defendant didn't answer; default judgment entered. Now in
collection.

**Approach**:

- **Motion to vacate under ORCP 71** — see `or-post-judgment`
- **Exemption claims on garnishment** under ORS 18.700+
- **FDCPA / UTPA claims** for continued collection on a
  fraudulent judgment

### Pattern 5: Unauthorized debt collection

Plaintiff is a collection agency that is NOT registered with
the Oregon Department of Consumer and Business Services
(DCBS) as required by ORS 697.015.

**Defenses**:

- **Lack of capacity to sue** — unregistered collection
  agencies cannot maintain an action (ORS 697.105)
- **Motion to dismiss under ORCP 21**

**Counterclaims**:

- **ORS 697.085** — private right of action for unregistered
  collection
- **Oregon UTPA** — unregistered collection is an unfair
  practice

## Substantive law — quick reference

### FDCPA (15 USC § 1692 et seq.)

The federal Fair Debt Collection Practices Act. Applies to
**debt collectors** (not original creditors) collecting
**consumer** debt.

| Section | Subject |
|---------|---------|
| 1692c | Communication restrictions |
| 1692d | Harassment / abuse |
| 1692e | False or misleading representations |
| 1692f | Unfair practices |
| 1692g | Validation notices |
| 1692k | Civil liability ($1,000 statutory + actual + fees) |
| 1692k(d) | 1-year SOL |

See `references/fdcpa.md` for the full annotated FDCPA.

### Regulation F (12 CFR pt 1006)

The CFPB's implementing regulation, effective November 30,
2021. Implements and supplements FDCPA. Key provisions:

| Section | Subject |
|---------|---------|
| § 1006.6 | Communication with consumers |
| § 1006.18 | False or misleading representations |
| § 1006.22 | Unfair or unconscionable practices |
| § 1006.26 | Time-barred debt |
| § 1006.30 | Notice requirements (replaces FDCPA validation) |
| § 1006.34 | Validation information |

See `references/reg-f.md` for the full annotated Reg F.

### Oregon UTPA (ORS 646.605–646.656)

Oregon's consumer-protection statute. Broader than FDCPA in
some respects:

- Applies to ALL persons collecting consumer debt, not just
  "debt collectors"
- No $1,000 cap; actual damages, $200 statutory minimum,
  punitive damages, injunctive relief
- Prevailing-party fees mandatory under ORS 646.638(3)
- 1-year SOL from discovery; 6-year repose under ORS
  646.638(6)

Key sections:

- **ORS 646.607** — unconscionable tactics list
- **ORS 646.608** — unlawful trade practices catalog
- **ORS 646.638** — private right of action

See `references/utpa.md` for the full annotated UTPA.

### Oregon Collection Agency Registration Act (ORS 697)

Regulates **collection agencies** (debt collectors) in
Oregon.

- **ORS 697.005** — definitions; "collection agency" includes
  debt buyers
- **ORS 697.015** — registration required with DCBS
- **ORS 697.058** — prohibited practices
- **ORS 697.085** — private right of action; actual damages,
  $200 statutory minimum, attorney fees
- **ORS 697.105** — registration is condition of capacity to
  sue (unregistered agency cannot bring an action in Oregon
  courts)

See `references/ors-697.md` for the full annotated ORS 697.

### Chain of title

A debt buyer must prove every link in the chain from original
creditor to itself. Typical chain:

```
Original Creditor (Bank of America)
       ↓ Bulk Sale Agreement, Bill of Sale, Assignment
Debt Pool Purchaser 1 (e.g., Asset Acceptance)
       ↓ Bulk Sale Agreement, etc.
Debt Pool Purchaser 2 (e.g., Velocity Investments)
       ↓ Sale to current Plaintiff
Plaintiff (LVNV Funding, LLC)
```

Each link requires:

- **Bill of Sale** — the document evidencing the sale
- **Assignment Schedule** — the inventory listing the specific
  accounts assigned
- **Authentication** — under OEC 901 / 902(11), the bill of
  sale must be authenticated by a witness from the assigning
  entity

Debt buyers often produce only a **summary** bill of sale and
a **redacted** assignment schedule. The defendant's
discovery target: the **un-redacted** versions, plus the
**cardholder agreement** between defendant and original
creditor.

See `references/chain-of-title.md` for the full doctrine.

## Discovery banks (subject-matter-specific)

Pre-built request banks for debt-defense discovery. These
plug into the procedural framework in `or-discovery`:

- **`references/rfp-debt-buyer.md`** — First Requests for
  Production targeting chain of title, original-creditor
  records, plaintiff's records of the account, communications,
  collection history
- **`references/rfa-debt-buyer.md`** — Requests for Admission
  locking in foundational facts (plaintiff's corporate form,
  registration status, dates of acquisition)
- **`references/interrogatories-debt-buyer.md`** —
  Interrogatories in mandatory arbitration (where allowed by
  arbitrator) — **Oregon does NOT have written interrogatories
  in standard ORCP discovery**
- **`references/meet-and-confer-debt-buyer.md`** — Sample
  meet-and-confer letters and follow-up emails

## Evidence patterns

The OEC 803(6) / 902(11) foundation question is the critical
evidentiary battleground in Oregon debt-buyer cases. The
plaintiff's typical declaration:

> "I am the custodian of records for [Plaintiff Debt Buyer].
> Plaintiff maintains records of accounts in the ordinary
> course of business. Account number ending XXXX was assigned
> to Plaintiff on [date] by [Original Creditor]. Plaintiff's
> records show a balance of $[amount] owing on the account.
> True and correct copies of the records are attached."

This declaration typically **fails** as foundation because:

1. The declarant is the **debt buyer's** custodian, not the
   original creditor's
2. The original creditor's records are hearsay — the
   declarant cannot attest that they were made in the regular
   course of the original creditor's business
3. The "remote custodian" doctrine — the debt buyer cannot
   speak to the trustworthiness of records it didn't create

See `references/evidence-debt-buyer.md` for the doctrine and
the specific objection language.

## Key cases — Oregon and 9th Circuit

### Oregon

- *Phillips v. Beaverton Aluminum Co.*, 314 Or App 257, 498
  P3d 814 (2021) — ORCP 46 fee-shifting in discovery
  disputes
- *Denson v. Ron Tonkin Gran Turismo*, [verify cite] — UTPA
  standing in consumer transactions
- *Pearson v. Philip Morris*, 358 Or 88, 361 P3d 3 (2015) —
  UTPA class certification standards
- *Ziegler v. Hill* and similar trial-court decisions on
  business-records foundation in debt cases (look for recent
  Oregon Court of Appeals decisions)

### 9th Circuit / federal

- *Henson v. Santander Consumer USA, Inc.*, 582 US 79, 137
  S Ct 1718 (2017) — definition of "debt collector"
- *Heintz v. Jenkins*, 514 US 291 (1995) — attorneys as
  debt collectors
- *Sheriff v. Gillie*, 578 US 317 (2016) — state actors
- *Marx v. General Revenue Corp.*, 568 US 371 (2013) —
  attorney-fee shifting under § 1692k

See `references/key-cases.md` for full citations and
holdings.

## Companion procedural skills

This subject-matter bundle composes with:

- **`or-statewide-format`** — UTCR 2.010 formatting
- **The relevant court skill** — `or-multcc` / `or-wccc` /
  `or-county-courts`
- **`or-pro-se`** — pro-se drafting framework
- **`or-law-references`** — citation conventions, online
  sources
- **`or-discovery`** — discovery framework; layer the
  debt-buyer-specific banks on top
- **`or-first-30-days`** — initial response (affirmative
  defenses + counterclaims selection)
- **`or-deadlines`** — SOL computation (ORS 12.080 6 years;
  FDCPA 1 year; UTPA 1 year/6 years)
- **`or-fact-check`** — citation verification
- **`or-quality-check`** — format pass
- **`or-draft-*`** — drafting the specific filings
- **`or-post-judgment`** — if default judgment already entered

## References

- `references/fdcpa.md` — FDCPA section-by-section
- `references/reg-f.md` — Regulation F annotated
- `references/utpa.md` — Oregon UTPA (ORS 646.605 et seq.)
- `references/ors-697.md` — Oregon Collection Agency
  Registration Act
- `references/or-statutes-of-limitations.md` — Oregon SOLs
  for debt and consumer-protection claims
- `references/chain-of-title.md` — chain-of-title doctrine
- `references/evidence-debt-buyer.md` — OEC 803(6) / 902(11)
  foundation in debt cases
- `references/fact-patterns.md` — five common debt-defense
  fact patterns
- `references/key-cases.md` — Oregon and federal decisions
- `references/recent-decisions.md` — recent Oregon Court of
  Appeals and 9th Circuit opinions
- `references/fees-consumer-debt.md` — fee-shifting in
  debt-defense cases
- `references/rfp-debt-buyer.md` — RFPs targeting chain of
  title
- `references/rfa-debt-buyer.md` — RFAs locking in basics
- `references/interrogatories-debt-buyer.md` —
  interrogatories (only available in arbitration)
- `references/meet-and-confer-debt-buyer.md` — sample
  meet-and-confer correspondence
- `references/ucc-article-9.md` — UCC Article 9 (ORS 79)
  on secured transactions in debt-buyer chain-of-title
- `references/online-sources-consumer-debt.md` —
  authoritative URLs for debt-related research
