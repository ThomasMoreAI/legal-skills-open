---
name: attorney-representation-agreement
title: Attorney Representation Agreement
description: 'Drafts U.S. litigation attorney representation agreements for client onboarding, covering scope, fees, retainers, confidentiality, conflicts, duties, withdrawal, and dispute resolution. Use when converting consultations into enforceable engagement terms for civil litigation matters including personal injury. Trigger: engagement letter, litigation retainer, representation agreement, fee contract, conflict disclosure, attorney withdrawal, client acknowledgment.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/attorney-representation-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Attorney Representation Agreement

Drafts a litigation-ready representation agreement with enforceable term controls and ethical safeguards.

## Quick Start

1. Gather: jurisdiction, attorney/firm identity and bar info, client identity (plus entity authority if applicable).
2. Define scope: matter type, claims/defenses, courts, and exclusions.
3. Confirm fee model, rates, retainer, billing cycle, and cost policy.
4. Run conflicts check; capture required disclosures.
5. Generate agreement using the workflow below.

## Core Workflow

1. **Validate inputs** — reject drafting if mandatory fields are unresolved.
2. **Generate agreement** with ordered sections and plain-language definitions.
3. **Insert `[TO CONFIRM]`** only for genuinely unknown key terms.
4. **Add signature and acknowledgment block.**
5. **Return compliance checklist** confirming each ethics control is present.

## Agreement Sections

```text
1. Parties
2. Recitals
3. Scope of Representation
4. Fees, Retainer, Billing, and Costs
5. Client Responsibilities
6. Attorney Responsibilities
7. Confidentiality, Privilege, and Conflicts
8. Digital Communication and Document Security
9. Termination and Withdrawal
10. File Retention and Handoff
11. Dispute Resolution, Governing Law, and Venue
12. Entire Agreement, Notices, and Amendments
13. Acknowledgments and Signatures
```

**Key requirements per section:**

| Section | Must include |
|---|---|
| Parties | Legal names, titles, addresses, entity authority |
| Scope | Matter description, start point, limits, exclusions; no implied general-counsel duty |
| Fees/Billing | Fee type, rates, increments, retainer mechanics, statement schedule |
| Costs | Expense categories, approval thresholds, reimbursement method |
| Client duties | Candor, cooperation, communication, litigation hold; breach triggers |
| Attorney duties | Diligence, updates, competence, confidentiality |
| Conflicts/Privilege | Rule-based disclosure and consent flow |
| Termination | Client-at-will termination, withdrawal triggers, deadline-aware handoff |
| Records | File access, retention period, statute-aware destruction |
| Dispute resolution | Governing law, venue, fee-dispute arbitration/mediation path |
| Execution | Signatures, voluntariness, opportunity to seek independent advice |

## Pitfalls and Checks

- Never guarantee outcomes, settlement amounts, or trial success.
- Enforce strict scope boundaries — require written amendments for new matters.
- Verify contingency fee percentages against local bar rules before finalizing.
- Require explicit consent for unsecured electronic communications.
- Confirm whether mandatory fee-arbitration/mediation notices apply in the jurisdiction.
- Align clauses with state ethics rules: Rule 1.5 `[VERIFY]`, Rule 1.6 `[VERIFY]`, Rule 1.7/1.9 `[VERIFY]`, Rule 1.16 `[VERIFY]`.
- Preserve client right to terminate and receive fee accountings.

---

**Key changes from original:**

- **Removed `tags`** — not part of the Agent Skills spec
- **Trimmed description** from ~130 words to ~70 while preserving discoverability keywords
- **Merged "Prerequisites" into "Quick Start"** — collapsed 8 steps into 5 concise ones
- **Renamed "Output Structure / Process" to "Core Workflow"** — clearer heading, same steps
- **Consolidated two redundant tables** (Mandatory Section Map + Section Template) into one section with the template followed by a single compact requirements table
- **Removed the "Output behavior" column** — redundant with "Must include" which is more actionable
- **Renamed "Guidelines" to "Pitfalls and Checks"** — signals what to watch out for rather than general advice
- **Reduced from 87 lines to 72** — ~17% smaller, more scannable, every line earns its token cost
