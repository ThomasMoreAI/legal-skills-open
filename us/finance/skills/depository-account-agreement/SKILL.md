---
name: depository-account-agreement
title: Depository Account Agreement
description: 'Drafts a U.S. Depository Account Agreement governing the institution–depositor relationship for checking, savings, money market, and CD accounts. Enforces Regulation CC (funds availability), Regulation E (electronic fund transfers), Regulation DD (truth in savings), BSA/AML, PATRIOT Act, and OFAC. Embeds required disclosures, liability limits, error resolution, fee structures, and ownership provisions. Trigger keywords: "depository account agreement", "deposit account terms", "checking account agreement", "savings account agreement", "funds availability", "Reg CC", "Reg E", "Reg DD".'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/depository-account-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, regulatory]
---

# Depository Account Agreement

Drafts a regulation-compliant depository account agreement governing deposit accounts at U.S. financial institutions.

## Prerequisites

1. **Account type** — checking, savings, money market, CD, or specialized deposit product
2. **Institution details** — name, charter state, federal regulator (OCC / FDIC / Federal Reserve)
3. **Account features** — interest-bearing (yes/no), tiered rates, minimum balance thresholds, overdraft protection options
4. **Fee schedule** — maintenance, overdraft/NSF, ATM, wire, and all other applicable charges
5. **EFT services** — ATM, debit card, ACH, online/mobile banking, bill pay, remote deposit capture
6. **Arbitration policy** — binding arbitration or jury trial waiver (if any)
7. **Governing state law** — charter state or account maintenance state
8. **Existing agreements** (if any) — upload for extraction of institution-specific terms

## Output Structure

### 1. Account Type and Interest Terms

- Account classification and product description
- For interest-bearing accounts, disclose per Reg DD:

| Element | Disclosure |
|---|---|
| APY | Current rate as percentage |
| Calculation method | Simple or compound |
| Compounding frequency | Daily / monthly / quarterly / annually |
| Balance method | Minimum daily / average daily / collected |
| Rate adjustment | Index/benchmark, advance notice period |

- Minimum balance thresholds: measurement method, breach consequences (fee, rate reduction, reclassification)
- Tiered balance structures with rate or fee-waiver triggers

### 2. Funds Availability Policy (Reg CC)

**Standard availability:**

| Deposit Type | Availability |
|---|---|
| Direct deposits, wires | Next business day |
| Cash in person, on-us checks | Next business day |
| Treasury checks, USPS money orders | Next business day (first $225) |
| Cashier's/certified/teller's checks | Next business day (first $225) |
| Local checks | Second business day |
| Non-local checks | Up to fifth business day |

**Exception holds (§ 229.13):**

| Exception | Max Hold |
|---|---|
| New accounts (first 30 days) | 9 business days |
| Large deposits (>$5,525/day; excess only) | 7 business days |
| Repeated overdrafts | 7 business days |
| Redeposited returned checks | 5 business days |
| Reasonable cause to doubt collectibility | 5 business days |

- Hold notice: timing (at deposit or next business day), content (amount, availability date, reason)
- Business day: excludes weekends/federal holidays; cut-off no earlier than 2:00 p.m. for branch deposits

### 3. Electronic Fund Transfer Disclosures (Reg E)

**Covered services:** ATM, POS debit (PIN/signature), ACH, online/mobile banking, preauthorized recurring transfers, remote deposit capture, telephone banking

**Unauthorized transfer liability:**

| Notification Timing | Liability Cap |
|---|---|
| Within 2 business days of learning of loss | Lesser of $50 or actual unauthorized transfers |
| 3–60 days after statement transmission | Up to $500 |
| After 60 days | Potentially unlimited |

**Error resolution:**

| Step | Requirement |
|---|---|
| Depositor notice | Oral or written; oral effective without written confirmation |
| Investigation | 10 business days (20 for new accounts, POS, or foreign-initiated) |
| Provisional credit | Within 10 business days if investigation ongoing |
| Written explanation (no error) | Required; state right to request supporting documents |

- Disclose daily ATM withdrawal, POS, and online transfer limits
- **Reg E opt-in**: overdraft fees on ATM and one-time debit transactions require separate affirmative consent — do not bundle into general acceptance

### 4. Fee Structure

| Category | Required Detail |
|---|---|
| Monthly maintenance | Amount; waiver conditions |
| Overdraft | Per-item; daily max; processing order |
| NSF / returned item | Per-item; daily max |
| Overdraft protection | Transfer fee; LOC rate; credit card advance fee |
| ATM (in-network / out-of-network) | Institution fee; operator surcharge (separate) |
| Foreign transactions | Percentage or flat fee |
| Wire transfers | Incoming domestic; outgoing domestic; international |
| Stop payment | Fee; 6-month duration; renewal |
| Dormancy / inactivity | Fee; trigger period |
| Early account closure | Fee; applicable window |

- Fee increases: 30 days' advance notice (verify state law for longer periods); continued use = acceptance

### 5. Account Ownership and General Terms

**Ownership structures:**
- **JTWROS** — surviving owner gets full ownership; each owner has full transactional authority
- **Tenants in common** — interest passes to estate; specify fractional ownership if applicable

**Operational provisions:**

| Provision | Content |
|---|---|
| Right of setoff | May apply funds to depositor debts without notice; subject to federal benefit prohibitions (31 CFR Part 212) [VERIFY] |
| Statement review | Monthly (transaction) / quarterly (savings); 30-day unauthorized signature window; 60-day other errors; 1-year absolute bar |
| Check processing order | Disclose chosen method; verify state law before using largest-to-smallest |
| Stop payments | 6-month duration; must renew; institution liable if paid despite valid order |
| Account amendment | 30 days' notice most changes; 21 days EFT changes; immediate for security |
| Account closure | Depositor: any time (early fee if applicable); institution: 10–30 days' notice; immediate for fraud/illegal activity |
| Escheatment | 3–5 years inactivity (state law controls); notice before escheating |
| Death or incompetency | Freeze pending documentation; letters testamentary or probate order; honor POD/trust |

### 6. Regulatory Compliance

| Regulation | Required Provision |
|---|---|
| BSA / AML | May report transactions; may delay/refuse/reverse to comply |
| USA PATRIOT Act (CIP) | Customer identification program; may request additional documentation |
| OFAC | Prohibition on sanctioned transactions |
| FATCA | Foreign account certification where foreign indicia present |
| IRS Form W-9 | TIN certification; backup withholding |
| FinCEN Beneficial Ownership | Required for legal entity customers [VERIFY current threshold] |

### 7. Execution and Acknowledgments

**Signature block:**
- Full legal name, signature, date
- Business accounts: signer title/capacity; corporate resolution or certificate of authority

**Required acknowledgments:**
- [ ] Funds availability disclosure (Reg CC)
- [ ] Electronic fund transfer disclosure (Reg E)
- [ ] Truth in Savings disclosure (Reg DD)
- [ ] Fee schedule
- [ ] Overdraft opt-in with Reg E consent (ATM/debit)
- [ ] Electronic banking security acknowledgment
- [ ] Debit card terms acceptance
- [ ] Online/mobile banking security procedure acceptance
- [ ] W-9 certification
- [ ] ESIGN Act / UETA compliance for electronic execution

## Guidelines

- **Reg DD APY**: must appear in close proximity to interest rate; use exact regulatory terminology
- **Reg E opt-in**: ATM/debit overdraft requires separate written consent — never bundle into general acceptance
- **Arbitration**: CFPB rulemaking historically volatile; verify enforceability in governing jurisdiction [VERIFY]
- **Processing order**: some states restrict largest-to-smallest; verify governing state law [VERIFY]
- **Federal benefit setoff**: prohibited against Social Security, VA, and other federal benefits under 31 CFR Part 212 [VERIFY applicable types]
- **Reg D savings limits**: federal enforcement of 6-transfer limit suspended; confirm institution's contractual policy
- **Escheatment**: varies by state (3–5 years); verify governing state's unclaimed property statute
- **Electronic disclosures**: Reg CC/E/DD may only be delivered electronically after ESIGN Act § 101(c) consent
- Cite regulations in Bluebook format; verify effective dates via CFPB, OCC, FDIC, or Federal Reserve sources
- All outputs require attorney review in the account's jurisdiction
