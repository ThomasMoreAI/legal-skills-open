---
name: foreign-corporation-registration
title: Foreign Corporation Registration
description: 'Drafts a foreign corporation registration (Certificate of Authority) package to qualify a U.S. corporation for business in a new state. Extracts corporate identity, capital structure, officers, and registered agent details from uploaded records, then produces a jurisdiction-specific application with cover letter, document checklist, and filing instructions. Use when a corporation expands across state lines, opens offices or employs workers in a new state, or needs foreign qualification. Triggers: foreign qualification, certificate of authority, doing business, multi-state expansion.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/foreign-corporation-registration
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Foreign Corporation Registration

Drafts a state-compliant Certificate of Authority application package for a corporation to lawfully conduct business outside its home state.

## Prerequisites

Gather before drafting. If target state is unspecified, request it first — it controls all downstream requirements.

1. **Target state**
2. **Articles of incorporation** + all amendments, bylaws
3. **Certificate of Good Standing** from home state (within 30–90 days; verify target state's recency window)
4. **Officer/director roster** — full legal names, titles, addresses
5. **Registered agent in target state** — name, physical street address (no PO boxes), consent to serve
6. **Capital structure** — authorized shares, classes, par values
7. **Planned business activities** in target state

## Workflow

```
- [ ] Collect prerequisites
- [ ] Resolve name availability in target state
- [ ] Draft application sections
- [ ] Compile supporting document checklist
- [ ] Prepare cover letter and filing instructions
- [ ] Flag any missing info with legal explanation
```

## Application Sections

### 1. Header

State-specific title, corporation's exact legal name (from articles), incorporation date/state, target state, form number if applicable.

### 2. Name Availability

| Scenario | Resolution |
|---|---|
| Available as-is | Use exact legal name |
| Unavailable/conflicting | Assumed name / DBA registration |
| Missing required designator | Add Inc./Corp. per target state rules |
| Name reserved | Attach reservation certificate |

### 3. Corporate Identity

Incorporation date, home state file number, principal office address, EIN, fiscal year end, authorized capital (shares, classes, par values, preferences). Reflect all amendments with certified copies.

### 4. Officers & Directors

Full legal name, title, business address for each. Must match home state records exactly — inconsistencies cause rejection.

### 5. Registered Agent

Physical street address in target state (no PO boxes). Include written consent to serve using state's official form or notarized statement. Must be a resident individual, authorized entity, or licensed agent service.

### 6. "Doing Business" Analysis

**Triggers registration:** office/warehouse/retail space, employing in-state workers, owning/leasing real property, maintaining inventory, regular in-state commercial transactions.

**Common exemptions (verify per state):** bank accounts, board meetings, transfer agencies, acquiring debt, isolated transactions (typically 30 days or fewer), defending lawsuits.

Draft concise analysis showing activities exceed exemption thresholds.

### 7. Supporting Documents

- [ ] Certificate of Good Standing (within target state's recency window)
- [ ] Certified articles + amendments (official seal from home state)
- [ ] Registered agent consent
- [ ] Name reservation / DBA registration (if needed)
- [ ] Corporate resolution (if signatory is not a listed officer)
- [ ] Cover letter itemizing enclosures

### 8. Filing Instructions

Include method (mail / in-person / online / expedited), expected timeline, fees, accepted payment methods, state office contact, and whether originals or copies are accepted.

### 9. Execution Block

Signatory per bylaws (president, VP, secretary, treasurer, or authorized officer). Include notary block if target state requires notarization. Add certification language (e.g., "under penalty of perjury") if required.

## Critical Checks

- **Name matching** — any variation across application, articles, and good standing certificate causes rejection
- **Good standing recency** — most states require 30–90 days; verify target state's specific window
- **Registered agent** — must be physical street address; PO boxes rejected
- **Amendments** — all post-incorporation amendments must be reflected and included as certified copies
- **Authentication** — some states require apostilles for out-of-state documents; verify
- **Interstate commerce** — purely interstate transactions may be exempt; analyze before recommending registration
- **Non-compliance penalties** — inability to sue in state courts, back taxes, fines, personal officer/director liability
- **Missing info** — flag with specific explanation of legal requirement and how to obtain it
