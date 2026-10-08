---
name: draft-sow-sboghossian
title: Statement of Work (SOW)
description: Use when drafting a Statement of Work — the project-specific order form that incorporates by reference into a Master Services Agreement (MSA). Defines scope, deliverables with acceptance criteria, timeline with milestones, fees, and team composition. The most common source of services disputes is a vague SOW; this skill enforces scope discipline and objective acceptance standards. Applies across professional services, technology projects, consulting, legal process outsourcing, and any services structured under an MSA framework.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-sow
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Statement of Work (SOW)

A Statement of Work is the operative project document in a services relationship governed by a Master Services Agreement. The MSA sets the legal rules (IP ownership, liability, confidentiality, dispute resolution); the SOW sets the commercial specifics — what is being done, by whom, by when, and for how much. Most disputes in services relationships trace back not to the MSA but to a poorly drafted SOW.

## When to use this

- Kicking off a new project under an existing MSA framework
- Engaging a consultant, developer, law firm, or other professional services provider for a defined engagement
- Documenting a change to scope, timeline, or fees (use a Change Order, which follows the same structure)
- Any situation where "scope creep" is a real risk and clear boundaries need to be set before work starts

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Service Provider (named, consistent with MSA) | Party undertaking the work; consistency with MSA avoids dispute about which entity is performing | Must provide |
| Client (named, consistent with MSA) | Party paying and receiving deliverables | Must provide |
| SOW number and title | Identifies this SOW within the MSA relationship; needed for invoicing and correspondence | Must provide |
| Reference to MSA (date + parties) | Links to the governing legal framework | Must provide |
| Scope of services (in-scope and out-of-scope) | Defines the work boundaries; explicit out-of-scope list is as important as in-scope | Must provide |
| Deliverables (with acceptance criteria) | Defines what the Provider must produce and how success is measured | Must provide |
| Timeline (milestones with dates) | Creates accountability and triggers milestone-based payments | Must provide |
| Fees (amount, structure, payment schedule) | The commercial core | Must provide |
| Key personnel | Named individuals whose participation the Client is relying on | List or describe role-level minimum |

## Optional inputs

- Client dependencies (information, access, approvals that Client must provide; delays relieve Provider)
- Sub-contractor consent process
- Expenses policy (reimbursable expenses cap; pre-approval requirement)
- Intellectual property ownership for deliverables (default in MSA; SOW may deviate for bespoke work-product)
- Deviations from MSA standard terms (these must be explicit)

## Document Structure

### Header Block
```
STATEMENT OF WORK NO. [X]
[Project Title]

This Statement of Work ("SOW") is entered into as of [Effective Date] and
is incorporated into and forms part of the Master Services Agreement dated
[MSA Date] between [Provider] and [Client] (the "MSA"). Capitalized terms
used but not defined in this SOW have the meanings given in the MSA.
```

### 1. Background
One paragraph describing the Client's business need and why this engagement was initiated. This provides context for scope interpretation — if a dispute arises about whether something is in-scope, the background sets the interpretive frame.

### 2. Scope of Services

Two lists — both are required:

**In-scope:**
- Numbered list of specific activities and services
- Use precise action verbs: "design," "develop," "deliver," "train," "configure," "test" — not "assist with" or "support"
- For technology projects: identify specific modules, APIs, environments (dev/staging/production), platforms

**Explicitly out-of-scope:**
- List activities that could reasonably be assumed to be included but are not
- Example: "Support for legacy system X is out of scope; integration testing beyond the UAT phase is out of scope; ongoing maintenance post-go-live is out of scope under this SOW"

### 3. Deliverables Table

| ID | Deliverable | Description | Format | Acceptance criteria | Target delivery date |
|---|---|---|---|---|---|
| D1 | Requirements Document | Documented business and technical requirements | Word/PDF | Client written approval within 5 business days of delivery | [Date] |
| D2 | Prototype | Functional prototype meeting requirements D1 | Live URL | Client acceptance testing passes >95% of agreed test cases | [Date] |
| D3 | Final Software | Production-ready system | Deployed code + documentation | Passes full UAT; all P1/P2 bugs resolved | [Date] |

**Acceptance criteria rules:**
- Objective tests only: "passes 95% of agreed test cases," "meets specifications in Exhibit A," "compliant with ISO standard X" — not "to Client's satisfaction" or "meets Client's requirements" (too subjective)
- Acceptance period: Client has [5–10] business days from delivery to accept or reject with reasons; silence after [10] business days = deemed acceptance
- Rejection must be in writing with specific reasons; Provider has [5] business days to cure and re-deliver; second rejection triggers dispute resolution

### 4. Timeline and Milestones

| Milestone | Description | Target date | Dependencies on Client | Payment trigger |
|---|---|---|---|---|
| M1 | Kick-off meeting + requirements workshop | [Date] | Client designates project sponsor and technical contact | 20% of fixed fee |
| M2 | Requirements Document (D1) approved | [Date] | Client approval of D1 within 5 business days | 20% of fixed fee |
| M3 | Prototype accepted (D2) | [Date] | Client test environment access | 30% of fixed fee |
| M4 | Final delivery and go-live (D3) | [Date] | Client production environment access; data migration by Client | 30% of fixed fee |

**Client dependency discipline**: if Client fails to deliver on a dependency (e.g., approvals, data, environment access), the milestone date adjusts by the same number of business days as the delay. Provider must give prompt written notice of a dependency delay to preserve timeline adjustment rights.

### 5. Team and Roles

| Role | Name (if specified) | Time commitment | Consent required for replacement? |
|---|---|---|---|
| Project Manager | [Name or "Senior PM"] | Full-time for phases 1–3 | Yes — Client written consent |
| Lead Developer | [Name or "Senior Developer"] | Full-time for phases 2–3 | Yes |
| QA Lead | [Role only] | Part-time | No — functional equivalent |
| Client Project Sponsor | [Name] | 2 hours/week | N/A — Client's resource |

If specific named individuals are key to the Client's decision to engage the Provider, name them and require written consent for any replacement during the engagement.

### 6. Fees and Invoicing

State the fee structure and payment schedule clearly:

**Fixed fee example:**
- Total fee: [Amount]
- Invoice on milestone achievement as per the milestones table
- Invoice due: [Net 30 / Net 45] days from invoice date
- Late payment interest: [base rate + 2% p.a. / as per MSA]

**Time-and-materials example:**
- Hourly rates by role: Partner [rate], Senior Associate [rate], Associate [rate], Analyst [rate]
- Monthly invoicing based on actual hours; time entries in [1/10 of hour / 15-minute] increments
- Estimated total: [range]; Provider will notify Client when 80% of estimate is consumed before exceeding it
- Hard cap (if applicable): Provider will not exceed [hard cap] without written authorization

Include: which party bears travel and expense costs; expense pre-approval threshold; third-party expenses (court fees, filing fees, expert fees — these should be pass-through at cost).

### 7. Project-Specific Terms
Any deviations from the MSA standard terms must be stated explicitly here:
- "Notwithstanding Section X of the MSA, the IP in all deliverables under this SOW shall vest in Client on full payment."
- "The limitation of liability in Section Y of the MSA is increased to [2x fees] for this SOW."

### 8. Conflict of Terms Clause
"In the event of any conflict between this SOW and the MSA, the MSA controls except where this SOW expressly states that it is varying a specific provision of the MSA."

### 9. Signature Block

## Why SOWs Matter

The MSA sets the rules; the SOW sets the specifics. A well-drafted MSA with a vague SOW gives the Client nothing to enforce. Concrete acceptance criteria, explicit out-of-scope lists, and named dependencies are the three elements that most often prevent or resolve disputes.

## Anti-Patterns

| Pattern | Why it fails |
|---|---|
| "Scope: as discussed in our kickoff meeting" | Unenforceable; no written record of the meeting content |
| Acceptance: "to Client's satisfaction" | Too subjective; turns the Client into an arbitrary judge |
| Timeline: "best efforts" | Not measurable; no consequences for missing |
| "Deliverables: TBD" | Postpone signing; do not sign a SOW with undefined deliverables |
| All fees tied to final delivery | Misaligns incentives; use milestone payments tied to intermediate deliverables |
| No Client dependency provisions | Provider cannot protect its timeline without documented Client obligations |

## Related skills

- [[draft-msa]]
- [[draft-sla]]
- [[draft-sow-extension]]
- [[draft-schedule-annex-builder]]
- [[review-msa-client-side]]
