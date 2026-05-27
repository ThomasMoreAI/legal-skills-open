---
name: statement-of-information
title: Statement of Information
description: Drafts a U.S. Statement of Information for periodic Secretary of State filing. Validates corporate name, officers, directors, registered agent, and addresses against source records. Triggers on annual/biennial compliance filings, officer or address updates, or good-standing maintenance tasks.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/statement-of-information
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [drafting, summary]
---

# Statement of Information

Prepares a jurisdiction-compliant Statement of Information for periodic Secretary of State filing to maintain corporate good standing.

## Prerequisites

1. **Corporate ID** — exact legal name (with designator: Inc., Corp., Co.) and SOS entity/file number
2. **Prior filing or articles** — for cross-reference and change detection
3. **Officer/director roster** — full legal names, titles, addresses; confirmed by board resolutions
4. **Registered agent** — name, physical street address in filing state, confirmed consent to serve
5. **Principal business address** — physical street address (PO boxes generally prohibited)
6. **Filing state and deadline** — drives form selection, frequency, signature rules, and penalty exposure

## Workflow

### 1. Corporation Identification

| Field | Requirement |
|---|---|
| Legal name | Exact match to SOS record including punctuation and designator |
| Entity/file number | As assigned by SOS |
| State of incorporation | Domestic domicile; foreign corps also provide qualification certificate number |
| Filing jurisdiction | State where SOI is being submitted |

### 2. Principal Office Address

- Physical street address (number, street, suite, city, state, ZIP)
- PO boxes prohibited in most states — confirm exception before using
- Separate mailing address if different from principal office

### 3. Officers

Minimum required in most states:

| Title | Role |
|---|---|
| CEO / President | Primary executive; common authorized signer |
| Secretary | Corporate records and governance |
| CFO / Treasurer | Financial operations |

- One individual may hold multiple titles — list all
- Full legal name + complete address per officer
- Verify appointment against board resolutions or minutes

### 4. Directors

- All current board members with full legal name and address
- Reflect current membership — do not carry forward outdated rosters
- Confirm filing state's rule: all directors vs. minimum count
- Residence addresses become public record — advise client

### 5. Registered Agent

| Field | Requirement |
|---|---|
| Agent name | State resident or commercial agent (exact registered name) |
| Address | Physical street address in filing state — no PO boxes |
| Availability | Staffed during business hours for service of process |
| Consent | Agent must have agreed to serve |

### 6. Business Description

- Specific description of primary commercial activity
- Never use "general business purposes" or similar boilerplate
- Align with corporate purpose clause in Articles of Incorporation

### 7. Certification and Execution

| Field | Requirement |
|---|---|
| Authorized signer | Current officer or as state permits |
| Declaration | Information is true, correct, and complete |
| Perjury clause | Required in some jurisdictions — verify |
| Notarization | Required in some jurisdictions — verify |
| Execution date | Must be current; file promptly after signing |

## Pitfalls

- **Filing frequency** — annual in most states, biennial in others; confirm per entity type and jurisdiction
- **Late filing** — triggers penalties; sustained non-compliance may cause suspension or administrative dissolution
- **Foreign corps** — distinguish incorporation state from qualification state; file under foreign classification with qualification number
- **Name exactness** — any deviation in punctuation, spacing, or abbreviation risks rejection
- **Address currency** — confirm all addresses are current, especially after relocation or remote-operations transition
- **Consistency check** — cross-reference all fields against bylaws, resolutions, and prior filings before finalizing

---

**Key changes made:**

- **Frontmatter `description`**: Condensed from 3 sentences of verbose explanation to a tight 3-clause summary with clear trigger guidance
- **Section rename**: "Output Structure" → "Workflow" (action-oriented); "Guidelines" → "Pitfalls" (scannable, warns-first)
- **Prerequisites**: Tightened labels and removed redundant phrasing (e.g., "SOS" abbreviation reused consistently)
- **Tables**: Trimmed cell text to essential requirements only (e.g., "Current officer or as state permits" instead of longer enumeration)
- **Bullets**: Cut filler words throughout; removed the example line in Business Description (unnecessary for agent instruction)
- **Overall**: ~25% token reduction while preserving every compliance requirement and legal distinction
