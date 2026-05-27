---
name: security-agreement
title: Security Agreement (Granting Lien)
description: Drafts UCC Article 9 security agreements granting first-priority liens on specified collateral. Covers party identification, collateral descriptions, representations/warranties, default/remedies, and perfection requirements. Use when drafting security agreements, granting liens, creating collateral pledges, or documenting secured financing transactions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/security-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# Security Agreement (Granting Lien)

Drafts an enforceable security agreement creating a first-priority security interest under UCC Article 9. Ensures collateral descriptions satisfy § 9-108 and support UCC-1 filing.

## Prerequisites

Gather before drafting:

- **Loan documents** — agreement/note/facility with principal, rate, maturity
- **Party identification** — exact legal names per Secretary of State, entity type, jurisdiction, principal address
- **Collateral details** — asset descriptions, serial numbers, locations, account numbers
- **Corporate authority** — organizational documents confirming signatory authority
- **Lien search** — UCC search results showing prior filings against debtor

## Quick Start

1. Confirm debtor's exact legal name against Secretary of State records
2. Map collateral to UCC Article 9 classifications
3. Draft using the 10-section structure below
4. Verify collateral description works for both the agreement and UCC-1 financing statement
5. Cross-check all defined terms and cross-references for internal consistency

## Output Structure

### 1. Preamble & Parties

- **Debtor**: exact legal name per SoS records (Inc. vs. Incorporated matters for perfection)
- **Secured Party**: full legal name, entity type, jurisdiction
- **Individual debtors**: include last-4 SSN or DL number for filing
- **Entity debtors**: organizational ID, jurisdiction of organization
- Include principal place of business for each party

### 2. Recitals

Reference underlying obligation (date, type, principal amount). State voluntary grant, confirm UCC Article 9 governance, establish consideration and intent.

### 3. Grant of Security Interest

Granting clause: "Debtor hereby grants to Secured Party a continuing security interest in all of the Debtor's right, title, and interest in and to the Collateral described below."

**"Obligations" definition must cover:** current principal; accrued/future interest, fees, costs, attorneys' fees; modifications, extensions, renewals, refinancings; future advances (if intended — note subordination risk with intervening lienholders).

### 4. Collateral Description

Must "reasonably identify" collateral per UCC § 9-108. Use UCC classifications plus specific identifiers:

| Collateral Type | Required Detail |
|---|---|
| Equipment | Make, model, serial number, location |
| Inventory | Type, location; state after-acquired if floating lien |
| Accounts receivable | Nature; include proceeds, collections, supporting obligations |
| Investment property | Securities, account numbers, issuing entities |
| General intangibles | IP registrations, contract rights, licenses |

**Always include proceeds clause:** "All proceeds, products, offspring, rents, profits, accessions, substitutions, and replacements of and to the Collateral, and all insurance proceeds and claims relating thereto."

**After-acquired property** (if intended): "whether now owned or hereafter acquired by Debtor."

- Avoid "all personal property" unless genuine blanket lien; supplement with specific categories even then
- Description must work for both the agreement and UCC-1 financing statement

### 5. Representations & Warranties

**General:** good/marketable title free of liens (except scheduled permitted liens); duly organized, validly existing, in good standing; full authority to grant security interest; no violation of existing agreements/laws; legal name, org ID, jurisdiction accurate.

**Collateral-specific:** Equipment — condition, operability, compliance. Accounts — genuine, enforceable, no defenses/offsets, bona fide transactions.

### 6. Covenants

**Affirmative:** maintain collateral condition; insure (name Secured Party as loss payee); pay taxes; maintain legal existence; deliver periodic financial statements and collateral reports.

**Negative:** no sale/transfer/encumbrance without consent; no name/structure/jurisdiction changes without notice; no collateral relocation without consent; no action diminishing value.

Tailor to collateral type: inventory → minimum levels + regular reports; equipment → maintenance schedules + usage restrictions.

### 7. Events of Default

| Default Type | Cure Period |
|---|---|
| Payment default | Immediate |
| Rep/warranty breach | Immediate |
| Covenant breach (technical) | 10–30 days after notice |
| Bankruptcy/insolvency | Immediate |
| Cross-default | Per underlying agreement |
| Material adverse change | Immediate |
| Judgment exceeding threshold | Per negotiated threshold |
| Loss/damage to collateral | Immediate |

### 8. Remedies

Upon default, Secured Party may: **accelerate** all obligations; **possess** collateral by self-help (no breach of peace) or judicial process; **dispose** at public/private sale (commercially reasonable per UCC Art. 9); **collect** accounts directly from account debtors.

**Application of proceeds:** (1) collection/disposition expenses including attorneys' fees → (2) secured obligations → (3) surplus to debtor. Debtor liable for deficiency. Remedies are cumulative.

### 9. Governing Law & Administrative Provisions

- **Governing law (contract):** party-selected state law
- **Governing law (security interest):** UCC as adopted in debtor's location state (governs perfection/priority)
- **Jurisdiction:** exclusive; debtor consents to personal jurisdiction, waives inconvenient forum
- Include: jury waiver, severability, written-amendments-only, notice provisions, waiver (no waiver by delay), assignment (debtor restricted / Secured Party may assign), entire agreement merger clause, counterparts, further assurances (debtor must execute UCC-1s, amendments, continuations)

### 10. Execution

| Party Type | Requirements |
|---|---|
| Corporation | Authorized officer with title |
| LLC | Manager or authorized member per operating agreement |
| Partnership | General partner with binding authority |
| Individual | Simple signature; consider spousal signature for marital property |
| Notarization | Required only if collateral includes fixtures or filed in real property records |

## Critical Checks

- [ ] Debtor legal name matches Secretary of State records exactly — minor variations defeat perfection
- [ ] Collateral description matches schedules/exhibits and underlying term sheet
- [ ] Description sufficient for both security agreement and UCC-1 filing
- [ ] All defined terms, cross-references, and party names internally consistent
- [ ] No gaps in debtor name, collateral specifics, or obligation terms
- [ ] Terms reconciled against term sheet or commitment letter
- [ ] UCC citations verified against applicable state's adopted version
