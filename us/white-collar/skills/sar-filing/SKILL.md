---
name: sar-filing
title: SAR Filing
description: Drafts FinCEN Suspicious Activity Reports (Form 111) for BSA/AML regulatory filing. Compiles subject identification, transaction timelines, red-flag analysis, and activity classifications. Use when a financial institution detects suspicious transactions requiring mandatory SAR filing, continuing activity reports, or BSA compliance documentation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/sar-filing
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: white-collar
language: en
---

# SAR Filing

Drafts a FinCEN-ready SAR (Form 111) from transaction records, investigation files, and institutional data.

## Prerequisites

Gather before drafting:

1. **Transaction records** — amounts, dates, account numbers, instrument types
2. **CIP/KYC documentation** — government IDs, SSN/TIN, beneficial ownership
3. **Investigation file** — alerts, internal notes, employee observations
4. **Filer details** — institution legal name, EIN, LEI, regulator, SAR contact
5. **Prior SAR history** (continuing filings) — BSA IDs, filing dates

## Quick Start

1. Determine filing type: Initial / Continuing / Corrective
2. Verify thresholds: ≥$5,000 (subject identified) or ≥$25,000 (no subject)
3. Confirm deadline: 30 days from detection (60 if no subject identified)
4. Draft sections in order below
5. Run compliance checklist before submission

## SAR Sections

### 1. Filing Header

| Field | Detail |
|---|---|
| Filing type | Initial / Continuing / Corrective |
| Institution | Legal name, EIN/LEI |
| Regulator | OCC / Fed / FDIC / NCUA / State |
| SAR contact | Name, title, phone, secure email |
| Detection date | When activity first identified |
| Filing deadline | 30 days (60 if no subject) |
| Prior BSA ID | If continuing: reference number + new trigger |

### 2. Subject Identification

Classify each party: Subject, Purchaser/Sender, Payee/Receiver, Other.

**Individuals:** Legal name, aliases, DOB, SSN/ITIN, address, government ID (type/number/jurisdiction/expiration). Foreign nationals: passport, citizenship, visa, high-risk jurisdiction nexus.

**Entities:** Legal name, DBAs, EIN, formation state/date, business nature, beneficial owners (≥25% ownership or substantial control).

**Relationships:** Document familial, business, signatory, nominee, or intermediary connections between parties.

### 3. Account Detail

For each account: number, type, open date, status (active/closed/restricted/frozen), holders/signers, stated purpose, baseline activity profile, and deviations triggering concern.

Include: branch contacts, prior compliance concerns, correspondent/MSB/processor relationships with fund-flow tracing, CIP/CDD/EDD procedures performed, closure details if applicable.

### 4. Activity Classification

Select FinCEN categories:

| Category | Examples |
|---|---|
| Structuring | Below CTR thresholds |
| Money laundering | Layering, integration, funnel accounts |
| Terrorist financing | OFAC/SDN nexus |
| Fraud | Check kiting, wire fraud, elder exploitation |
| Identity crimes | Synthetic ID, stolen credentials |
| Cyber | Account takeover, intrusion-related transfers |
| Sanctions evasion | Sanctioned jurisdictions/persons |
| Other | Unlicensed MSB, trade-based ML, human trafficking |

**Thresholds:** ≥$5,000 (subject identified) / ≥$25,000 (no subject). For blocked/attempted transactions, explain why filing is warranted. Confirm no exemption applies and filing is not duplicative.

State total dollar amount, currency, and complete time period.

### 5. Narrative

Address Who/What/When/Where/Why/How chronologically:

1. **Detection** — How identified (alert, referral, LE inquiry, audit); specific trigger; why not false positive
2. **Timeline** — Each significant transaction: date, type, amount, source→destination, stated purpose, unusual characteristics
3. **Red flags** — Map facts to indicators: reluctance to provide info, no economic purpose, rapid in/out movement, structuring, shell companies, high-risk jurisdictions, profile inconsistencies. Cite FFIEC BSA/AML Manual or FinCEN advisories where applicable.
4. **Investigation** — Customer contact attempts and responses, why insufficient, public records research, prior SARs (BSA IDs and dates)
5. **Conclusion** — Factual basis for filing. Objective tone only — no conclusions about criminal intent.

### 6. Supporting Documentation

Index attachments by category: transaction records, customer ID docs, correspondence, monitoring system output, investigation memos, inter-institution communications. Label each with title and narrative relevance.

## Compliance Checklist

- [ ] Filed within 30-day deadline (60-day if no subject)
- [ ] All mandatory Form 111 fields completed
- [ ] Narrative addresses Who/What/When/Where/Why/How
- [ ] Dollar amounts accurate and aggregated
- [ ] All dates, account numbers, IDs verified
- [ ] Senior management/board notified per policy
- [ ] Legal counsel consulted if civil liability or non-BSA issues
- [ ] Reviewing/approving officers documented
- [ ] Filed via BSA E-Filing; confirmation + BSA ID retained
- [ ] File stored separately, access restricted to need-to-know
- [ ] 5-year retention initiated from filing date
- [ ] **No disclosure** to any subject (31 U.S.C. § 5318(g)(2))
- [ ] No inadvertent tipping via closure letters or communications
- [ ] Immediate LE notification assessed

## Critical Rules

- **Confidentiality is absolute.** SAR disclosure prohibition (31 U.S.C. § 5318(g)(2)) carries criminal penalties. Never reference SAR existence in customer-facing communications.
- **Objectivity only.** State facts and observations. Never conclude criminal guilt or legal violations.
- **Over-include.** FinCEN prefers detailed narratives.
- **Standalone.** Must be comprehensible without access to underlying bank records.
- **Continuing filings** must reference prior BSA IDs and identify what is new.
- **Safe harbor** (31 U.S.C. § 5318(g)(3)) applies to good-faith filings — document investigative process thoroughly.
