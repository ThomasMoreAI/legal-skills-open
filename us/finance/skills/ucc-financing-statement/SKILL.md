---
name: ucc-financing-statement
title: UCC Financing Statement and Amendments
description: Drafts UCC-1 Financing Statements and UCC-3 Amendments to perfect security interests under Article 9 of the Uniform Commercial Code. Handles debtor identification, collateral descriptions, filing jurisdiction, continuations, terminations, and assignments. Use when drafting UCC-1 filings, UCC-3 amendments, continuation statements, or any secured transaction perfection document.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ucc-financing-statement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# UCC Financing Statement and Amendments

Produces filing-ready UCC-1 or UCC-3 documents that comply with Article 9 and state-specific filing office requirements.

## Prerequisites

Gather before drafting:

1. **Security agreement** — executed, identifying debtor, secured party, collateral
2. **Entity verification** — certificate of formation/incorporation, org ID, or individual's driver's license name
3. **Transaction documents** — loan agreement, promissory note, guaranty, subordination
4. **Collateral details** — serial numbers, account numbers, registration numbers for specific assets
5. **Filing jurisdiction** — state of organization (registered entities) or principal residence (individuals) per § 9-307

## Quick Start

1. Extract exact debtor/secured party names from organizational records or government ID
2. Determine filing office (generally Secretary of State for debtor's jurisdiction)
3. Draft collateral description using Article 9 categories
4. Assemble UCC-1 or UCC-3 with all mandatory fields
5. Run quality control checklist before filing

## Core Workflow

### 1. Extract Party Information

| Field | Individual Debtor | Organization Debtor |
|-------|-------------------|---------------------|
| Name | Exact name per driver's license / govt ID | Exact registered name per state records |
| Address | Mailing address | Mailing address |
| Jurisdiction | Principal residence state | State of organization |
| Org ID | N/A | Organizational ID number |

Cross-check debtor name against organizational documents — minor variations can render filing "seriously misleading" under § 9-506.

### 2. Determine Filing Jurisdiction

**Default**: Secretary of State for debtor's jurisdiction of organization/residence.

**Exceptions**:
- **Fixture filings** — county real estate records where fixtures located
- **As-extracted collateral** (minerals/timber) — county real estate records
- **Transmitting utilities** — state-specific procedures may apply

Confirm state-specific form requirements, e-filing availability, and current fees.

### 3. Draft Collateral Description

Use Article 9 categories: accounts, chattel paper, deposit accounts, equipment, general intangibles, instruments, inventory, investment property, letter-of-credit rights, commercial tort claims.

**Rules**:
- Must "reasonably identify" collateral per § 9-108
- Methods: specific listing, category, UCC type, quantity, formula, or other objective method
- "All assets" / "all personal property" supergeneric descriptions permitted **only in financing statements** (not security agreements) — confirm jurisdiction allows
- Specific equipment/vehicles: include make, model, year, serial/VIN
- IP: include registration numbers, application numbers
- Commercial tort claims: **must be specifically described** — category-only filing is insufficient
- Add proceeds clause if intended: "together with all proceeds and products thereof"

### 4. Assemble UCC-1

```
UCC FINANCING STATEMENT (UCC-1)

1. DEBTOR
   Name: [exact legal name]
   Address: [mailing address]
   Jurisdiction of Organization: [state]    Org ID: [number]

2. SECURED PARTY
   Name: [exact legal name]
   Address: [mailing address]

3. COLLATERAL DESCRIPTION
   [Per Step 3]

4. ADDITIONAL INFORMATION (if applicable)
   [ ] Proceeds  [ ] Products  [ ] After-acquired property
   [ ] Fixture filing (include real estate description + record owner)
   [ ] Transmitting utility
   [ ] Public-finance transaction
   [ ] Manufactured-home transaction
```

### 5. Assemble UCC-3 Amendment

Reference original filing: file number, filing date, filing office.

| Amendment Type | Requirements |
|----------------|-------------|
| **Continuation** | File within 6-month window before 5-year lapse date |
| **Termination** | Secured party must file within 20 days of demand if obligation satisfied (§ 9-513) |
| **Assignment** | Full assignee name, address; authority documentation |
| **Amendment** | Specify exactly what is added, deleted, or changed |

- Collateral amendments: state precisely what is added or released
- Party name changes: include both old and new information
- Debtor must authorize amendments that add collateral or add a debtor

## Quality Control

- [ ] Debtor name matches organizational records / government ID exactly
- [ ] Organizational ID included for registered organizations
- [ ] Collateral description covers all intended property per security agreement
- [ ] Collateral description consistent with (but need not mirror) security agreement
- [ ] Correct filing office for debtor's jurisdiction
- [ ] For UCC-3: original file number and filing date verified
- [ ] For continuations: filing within 6-month pre-lapse window confirmed
- [ ] Authorization exists (security agreement or separate authorization)
- [ ] State-specific form requirements satisfied
- [ ] Filing fee confirmed
- [ ] No common rejection triggers: wrong name, missing org ID, wrong office, incomplete fields

## Output

Produce two deliverables:

1. **Filing-ready UCC-1 or UCC-3** — formatted per the jurisdiction's accepted form, all mandatory fields completed
2. **Filing guidance memo** — filing office/method, fees, statutory citations, any state non-uniform provisions, and lapse/continuation calendar dates (5-year lapse + 6-month continuation window)

## Pitfalls

- Never assume debtor name — always verify against organizational records or government-issued ID
- Flag jurisdictions with non-uniform Article 9 amendments (e.g., states requiring tax ID, additional certifications)
- Consumer-goods transactions have additional requirements under § 9-625(c)-(d)
- When in doubt about supergeneric descriptions, use specific categories as the safer approach
- Mark any state-specific rule you cannot fully verify with `[VERIFY]`

---

**Key changes from original**:
- Removed non-spec `tags` from frontmatter
- Tightened description to stay focused on triggers
- Added **Quick Start** section for at-a-glance workflow
- Collapsed the 10-row collateral categories table into an inline list (the agent already knows what these categories mean — no need to re-explain each one)
- Removed the Tax ID row from party table (already covered by jurisdiction-specific checks)
- Renamed "Process" → "Core Workflow" and "Guidelines" → "Pitfalls" for clearer section intent
- Eliminated redundant prose throughout (e.g., "For secured party, capture full legal name..." was obvious context)
- Reduced from ~143 lines to ~113 lines while preserving every statutory citation, legal rule, and compliance requirement
