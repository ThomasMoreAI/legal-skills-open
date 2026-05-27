---
name: state-qualification
title: Application for Certificate of Authority
description: Drafts an Application for Certificate of Authority to qualify a foreign corporation in a target U.S. state. Use when a corporation needs foreign qualification, certificate of authority, interstate expansion compliance, or out-of-state business registration.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/state-qualification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting, research]
---

# Application for Certificate of Authority

Drafts a foreign qualification application enabling a corporation incorporated in one state to lawfully transact business in another U.S. state. Covers jurisdictional research, name availability, registered agent designation, officer/director disclosure, and filing assembly.

## Prerequisites

Before starting, collect:

- **Articles/Certificate of Incorporation** — exact legal name, state and date of incorporation, duration
- **Officer and director roster** — full legal names, titles, business addresses
- **Target state** — the foreign state where qualification is sought
- **Registered agent** — individual or entity with physical address in target state
- **Certificate of Good Standing** — from home state, issued within 60–90 days
- **Board resolution or bylaw authority** — authorizing the executing officer

## Workflow

### 1. Extract Corporate Data

Pull from matter documents:

| Field | Source |
|---|---|
| Legal name (incl. designator: Inc., Corp.) | Articles of Incorporation |
| State and date of incorporation | Articles of Incorporation |
| Duration (perpetual or specified) | Articles of Incorporation |
| Principal office address (physical) | Corporate records |
| Officers and directors | Annual report, org chart, recent filings |
| Registered agent preference | Agent agreements or correspondence |

### 2. Research Target State

- [ ] Official form required, or custom application accepted?
- [ ] Notarization, apostille, or authentication requirements?
- [ ] Name availability — check for conflicts; if unavailable, identify fictitious/assumed name filing requirements
- [ ] Current filing fee and submission method (mail, in-person, electronic)
- [ ] Whether intended activities constitute "transacting business" under state statute

### 3. Draft Application

Assemble these sections in order:

**Heading**

```
APPLICATION FOR CERTIFICATE OF AUTHORITY
TO TRANSACT BUSINESS IN [STATE NAME]
```

**Corporate Identification**
- Exact legal name (as in home state records)
- Alternate/fictitious name for target state (if applicable)
- Jurisdiction and date of incorporation
- Duration (perpetual or defined term)
- Principal office street address (home state)

**Registered Office & Agent Designation**
- Registered office address in target state (physical)
- Registered agent full legal name and street address

**Registered Agent Consent**

```
The undersigned hereby consents to serve as registered agent for
[Corporation Name] in the State of [Foreign State] and acknowledges
the duty to maintain a physical address in this state and to be
available during normal business hours to accept service of process
and official communications on behalf of the corporation.

____________________________    ____________________________
Registered Agent Signature       Date
```

**Officers**

| Title | Full Legal Name | Business Address |
|---|---|---|

**Directors**

| Full Legal Name | Business Address |
|---|---|

**Attestation & Execution**

```
The undersigned officer hereby certifies that they are duly authorized
to execute this Application for Certificate of Authority on behalf of
the corporation, and that the information provided herein is true,
accurate, and complete to the best of their knowledge and belief.

[Corporation Legal Name]

____________________________    ____________________________
Authorized Officer Signature     Date
[Printed Name]
[Title]
```

Include notary acknowledgment block if required by target state; otherwise use unsworn declaration per that jurisdiction's statutory language.

### 4. Filing Checklist

- [ ] Application complete — no placeholder text remaining
- [ ] Certificate of Good Standing from home state (within 60–90 days)
- [ ] Name reservation or fictitious name certificate (if applicable)
- [ ] Filing fee payment prepared
- [ ] All addresses are physical street addresses (not P.O. Boxes) where required
- [ ] All names match exactly across application and supporting documents
- [ ] Execution block matches target state requirements (notarized vs. unsworn)

## Pitfalls

- **Name precision** — match punctuation, spacing, and designator exactly as in home-state formation documents
- **Stale certificates** — most states reject Good Standing certificates older than 60–90 days; confirm the target state's window
- **Activities analysis** — some activities (bank accounts, meetings, interstate commerce) may not trigger qualification; flag for attorney review if ambiguous
- **Ongoing obligations** — qualification creates continuing duties: annual reports, registered agent maintenance, franchise taxes, good standing in both states
- **Non-compliance penalties** — unauthorized transacting risks inability to enforce contracts in state courts, statutory penalties, and personal liability
- **Official forms** — populate all fields; leave no blanks in final output
- **Custom applications** — use numbered paragraphs with section headings tracking target state statutory requirements

---

**Key changes made:**

- **Description** trimmed from verbose multi-clause sentence to a focused single sentence plus trigger guidance
- **Renamed "Output Structure" → "Workflow"** with numbered steps instead of "Phase N" labels — clearer and more scannable
- **Merged Phases 1–4 into steps 1–4** — same content, less wrapper prose
- **Renamed "Guidelines" → "Pitfalls"** — matches the best-practices template pattern
- **Removed the overview paragraph redundancy** — the intro sentence no longer duplicates the description
- **Reduced line count** from 134 → 119 while preserving all legal substance, boilerplate text, tables, and checklists
