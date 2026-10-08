---
name: oh-consumer-debt-codearranger
title: Ohio Consumer Debt — Statutory + Common-Law Defenses
description: 'Use for Ohio consumer-debt defense — debt-buyer suits, collection actions. Covers **Ohio Consumer Sales Practices Act (R.C. Chapter 1345)** with **treble damages + mandatory fees**, **2-year CSPA SOL**, **FDCPA + Reg F** overlays, **chain-of-title doctrine**, **Ohio UCC Article 9** (R.C. Chapter 1309), and **6-year SOL on written contracts** (R.C. 2305.06). **NO collection-agency licensure in Ohio** — defenses lean on chain-of-title and FDCPA. Triggers: "Ohio consumer debt", "Ohio CSPA", "R.C. 1345 treble damages", "Ohio chain of title", "Ohio debt buyer", "medical debt Ohio".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
---

# Ohio Consumer Debt — Statutory + Common-Law Defenses

> **NOT LEGAL ADVICE.** Verify every cite against current
> R.C. text and current case law before filing. The Ohio
> CSPA has been amended materially in 2012, 2021, and 2023.

## Five fact-pattern triage

When a consumer-debt complaint arrives, triage to one of
these patterns. Each maps to a defense playbook.

### 1. Debt-buyer (post-charge-off) action

Plaintiff is **Midland Funding LLC**, **LVNV Funding LLC**,
**Portfolio Recovery Associates**, **Cavalry SPV I**,
**Crown Asset Management**, **Unifund CCR LLC**, or similar.
Plaintiff is **not** the original creditor (which would be
Citibank, Capital One, Synchrony, Discover, Chase, etc.).

**Core defenses:**
- **Chain of title** — plaintiff must prove every assignment
  from original creditor through any intermediate
  purchasers. Ohio's UCC at R.C. 1309.406 governs the
  rights of an assignee.
- **Account-stated foundation** — plaintiff usually pleads
  "account stated" because it lacks the underlying signed
  contract. Force them to produce the original card-member
  agreement under R.C. 1303.31 (UCC Article 3 negotiable-
  instrument requirements) or via Civ. R. 1002 best-evidence.
- **Authentication** — affidavits of "custodian" employed
  by the debt buyer (not the original creditor) routinely
  fail Civ. R. 803(6) / 901 foundation. *LVNV Funding, LLC
  v. Henderson*, 2018-Ohio-3535 (1st Dist.) is the leading
  cite for affidavit-of-debt failures in Ohio.
- **FDCPA counterclaim** — 15 U.S.C. § 1692e (false
  representations) and § 1692f (unfair practices) are
  routine counterclaim grounds.

### 2. Original-creditor action

Plaintiff is the bank that issued the card or made the
loan (Capital One, Discover Bank, etc.) — not a debt buyer.

**Core defenses:**
- **SOL** — 6 years on written contracts under R.C.
  2305.06; 4 years on Ohio UCC Article 3 negotiable-
  instruments suits under R.C. 1303.16.
- **Account-stated** — original creditor's monthly
  statements can establish account-stated if undisputed for
  reasonable time.
- **TILA / Reg Z** — billing-error disputes raised within
  60 days under 15 U.S.C. § 1666 must be honored.
- **Choice of law** — many card agreements choose
  Delaware, South Dakota, or Virginia. Choice-of-law clause
  may shift the controlling SOL and interest cap.

### 3. Medical debt action

Plaintiff is a hospital system or its assignee.

**Core defenses:**
- **No-Surprises Act** — federal NSA limits balance-billing
  for out-of-network emergency care.
- **R.C. 1751.60** — Ohio prohibits HMO-contracted
  providers from billing enrollees beyond copays.
- **Reasonable-value challenge** — medical debt is contract
  for services; charges must reflect reasonable value if no
  agreed price.
- **R.C. Chapter 3727** hospital-debt rules.

### 4. Auto-deficiency action

Plaintiff is auto-finance company after repossession.

**Core defenses:**
- **Commercially reasonable sale** — UCC R.C. 1309.610(B)
  requires commercially reasonable disposition. *Coxson v.
  Commonwealth Bank*, 43 Ohio App.3d 31, is leading cite.
- **Notice of disposition** — R.C. 1309.611 requires pre-
  sale notice to debtor; failure to give notice bars or
  reduces deficiency under R.C. 1309.626.
- **Retail Installment Sales Act** — R.C. Chapter 1317
  (`oh-law-references/references/oh-statutes-debt/RC-Chapter-1317.md`):
  most auto financing is a retail installment contract, so
  RISA's contract-form and notice/cure requirements apply on
  top of Article 9.
- **Lien perfection on the title** — R.C. Chapter 4505
  (`RC-Chapter-4505.md`); the security interest is perfected
  by notation on the certificate of title (R.C. 4505.13).
  Test whether the plaintiff actually holds a perfected,
  properly assigned interest.
- **Insurance / GAP credit** — verify any GAP insurance was
  applied before deficiency calculated.

### 5. Garnishment / supplemental proceedings

Default judgment already entered; plaintiff is now
collecting via wage garnishment, bank attachment, or
debtor exam.

**Core defenses:**
- **R.C. 2329.66 exemptions** — Ohio personal property
  exemption is generous (wildcard $1,475; tools of trade
  $2,800; household goods $13,400; homestead $161,375 as
  of 2024 adjustment). Ohio uses state exemptions, not
  federal Bankruptcy Code exemptions.
- **CCPA garnishment cap** — 15 U.S.C. § 1673 caps wage
  garnishment at 25% of disposable earnings or amount above
  30x federal minimum wage.
- **R.C. 2329.07** — judgment dormant after 5 years if not
  executed upon; revival required.

## Ohio CSPA — the centerpiece counterclaim

The **Ohio Consumer Sales Practices Act** (R.C. Chapter
1345) is the Ohio analog of the federal FDCPA + Washington's
CPA and is **substantially more powerful** than the federal
FDCPA on its own.

### Coverage

- **R.C. 1345.01(A)** defines "consumer transaction" — sale
  / lease / assignment / award / other transfer of an
  item / service to an individual for personal / family /
  household use.
- **R.C. 1345.01(C)** defines "supplier" — a seller,
  lessor, assignor, or other person engaged in the business
  of effecting consumer transactions. **Debt collectors and
  debt buyers are "suppliers" within the CSPA** per *Brown
  v. Liberty Clubs, Inc.*, 45 Ohio St.3d 191 (1989), and
  *Celebrezze v. United Research, Inc.*, 19 Ohio App.3d 49.

### Prohibited acts

- **R.C. 1345.02** — unfair / deceptive acts in connection
  with a consumer transaction.
- **R.C. 1345.03** — unconscionable acts.
- **OAC 109:4-3-XX** — Attorney General's substantive
  regulations adding per-industry prohibitions; debt-
  collection-specific rules at **OAC 109:4-3-11**.

### Damages

- **R.C. 1345.09(A)** — actual damages.
- **R.C. 1345.09(B)** — election of remedy: (1) triple
  actual damages, OR (2) $200 per violation. **Three times
  damages with no cap is the headline.**
- **R.C. 1345.09(F)** — **attorney's fees are mandatory**
  on prevailing-consumer CSPA judgments where supplier
  acted knowingly. *Bittner v. Tri-County Toyota*, 58 Ohio
  St.3d 143 (1991) is the leading fee-award standard
  (lodestar with Ohio modifications).

### SOL

- **R.C. 1345.10(C)** — 2 years from occurrence of
  violation OR from rescission becoming impossible /
  inapplicable.
- This is **2-year, not 6-year** — common pitfall.

## Federal overlays

The federal layer applies in parallel:

- **FDCPA** (15 U.S.C. §§ 1692-1692p) — applies to all
  third-party debt collectors (debt buyers, collection
  agencies, attorneys collecting consumer debt). Original
  creditors collecting their own debt are excluded.
- **Reg F** (12 C.F.R. Part 1006) — CFPB's 2021 codified
  rules: 7-7-7 contact limit, validation notice, time-of-
  day restrictions.
- **FCRA** (15 U.S.C. §§ 1681-1681x) — credit-report
  furnisher rules; § 1681s-2(b) provides private right of
  action after dispute via CRA.
- **TCPA** (47 U.S.C. § 227) — robocall + autodialed-text
  restrictions; collection calls within scope.

Verbatim text for all federal sources lives in
`oh-law-references/references/federal-debt-laws/` (symlinked
into the shared `claude-legal-federal-laws` plugin).

## Chain of title — debt-buyer defense backbone

Every debt-buyer plaintiff must prove unbroken chain from
original creditor. Build the discovery plan around:

### What to demand

1. Original cardmember agreement signed by consumer.
2. All monthly statements covering the account life.
3. Each Assignment / Bill of Sale in the chain (typically:
   original creditor → debt-buyer-warehouse → plaintiff;
   sometimes 3-4 hops).
4. Account-level data file accompanying each Bill of Sale
   (the actual transaction record proving THIS account was
   in the portfolio sold).
5. Affidavit of seller-side custodian at each hop (not just
   buyer's custodian).
6. Power-of-attorney chains where applicable.

### Common failures

- **Generic Bill of Sale** without account-level data file.
- **Custodian affidavit from buyer** purporting to
  authenticate seller's records — fails Civ. R. 803(6) /
  901.
- **Missing intermediate assignment** (Citibank → CCS Inc.
  → LVNV → Resurgent, but only CCS→LVNV produced).
- **Account-level data with discrepancy** in charge-off
  date, charge-off balance, or last-payment date.

## Discovery playbook

The `oh-discovery` skill covers the procedural framework.
Subject-specific:

- **RFP bank for debt buyers** — request the chain
  components above.
- **RFA bank** — request admissions on each foundation
  element (authenticity, custody, completeness).
- **Interrogatories** — Ohio Civ. R. 33(A) caps at 40
  including subparts; allocate carefully.
- **Motion to compel** — Civ. R. 37; require meet-and-
  confer per Civ. R. 37(E).

## Composition with other oh- skills

- `oh-first-30-days` — answer / Civ. R. 12(B)(6) triage
- `oh-discovery` — discovery mechanics
- `oh-draft-motion` — Civ. R. 56 / Civ. R. 12(B)(6) /
  Civ. R. 60(B) frameworks
- `oh-post-judgment` — exemptions + garnishment defense
- `oh-fact-check` — Ohio public-domain citation format
- `oh-statewide-format` — Civ. R. 10 caption + filing

## Critical SOLs in one place

| Claim | SOL | Statute |
|---|---|---|
| Written contract | 6 yr | R.C. 2305.06 |
| Oral contract | 6 yr | R.C. 2305.07 |
| Account stated | 6 yr | R.C. 2305.07 |
| UCC negotiable instrument | 4 yr | R.C. 1303.16 |
| Tort (personal injury) | 2 yr | R.C. 2305.10 |
| Libel / slander | 1 yr | R.C. 2305.11 |
| **Ohio CSPA** | **2 yr** | **R.C. 1345.10** |
| FDCPA | 1 yr | 15 U.S.C. § 1692k(d) |
| FCRA | 2 yr (discovery rule) | 15 U.S.C. § 1681p |
| Judgment enforcement | 5 yr (renewable) | R.C. 2329.07 |
