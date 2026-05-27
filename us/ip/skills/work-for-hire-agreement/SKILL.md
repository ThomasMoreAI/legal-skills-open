---
name: work-for-hire-agreement
title: Work for Hire Agreement
description: Drafts a U.S. Work for Hire Agreement under 17 U.S.C. §§ 101 and 201(b) with fallback IP assignment, creator warranties, and indemnification. Trigger when commissioning software, designs, content, or other creative work requiring clear IP ownership, or when drafting WFH clauses for consulting and service agreements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/work-for-hire-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [agreement, drafting, transactional]
---

# Work for Hire Agreement

Draft a U.S. Work for Hire Agreement vesting all IP in the hiring party, with a fallback assignment clause if WFH status fails under the Copyright Act.

## Quick Start

Gather before drafting:

1. **Parties** — legal names, entity types, formation states, addresses
2. **Work scope** — deliverables, specifications, format, acceptance criteria
3. **Compensation** — flat fee / hourly / milestone; payment schedule and triggers
4. **Statutory category** — does the work fit one of the nine WFH categories? (see below)
5. **Governing law** — hiring party's state (default) or negotiated jurisdiction

## Core Workflow

### 1. Recitals & Definitions

Define "Work," "Hiring Party," "Creator," "Deliverables," "Confidential Information." Identify the applicable statutory WFH category if any.

### 2. Work for Hire Designation

**Nine statutory categories (17 U.S.C. § 101):**

| Category | Example |
|---|---|
| Contribution to a collective work | Article in a journal |
| Part of a motion picture / audiovisual work | Video content |
| Translation | — |
| Supplementary work | Forewords, indexes, illustrations |
| Compilation | — |
| Instructional text | — |
| Test | — |
| Answer material for a test | — |
| Atlas | — |

> If the work falls **outside** these categories (e.g., standalone software), the WFH clause fails for independent contractors — the fallback assignment clause becomes the operative transfer mechanism.

Include: *"The Work shall be considered a 'work made for hire' as defined under 17 U.S.C. §§ 101 and 201(b). Hiring Party shall be deemed the author and exclusive owner of all rights, title, and interest in and to the Work from the moment of creation."*

### 3. Fallback Assignment

Self-executing assignment triggered if WFH status is not recognized:

- All copyright, moral rights, and related IP — worldwide, in perpetuity
- All exploitation rights: reproduction, distribution, adaptation, public display, performance, derivative works
- Creator executes confirmatory documents on request

### 4. Compensation & Payment

Specify: amount (flat / hourly / milestones), payment triggers (execution, delivery, acceptance), expense reimbursement terms, and conditions precedent (acceptable delivery, signed assignment docs).

### 5. Creator Warranties

Creator warrants:

- Work is original; no infringement of third-party IP
- Full authority to enter agreement and grant rights
- No defamatory, libelous, or unlawful material
- No conflicting prior assignments, licenses, or encumbrances

### 6. Indemnification

Creator defends, indemnifies, and holds harmless Hiring Party from all claims, damages, losses, and expenses (including attorneys' fees) arising from warranty breach or third-party IP claims.

### 7. Delivery & Acceptance

- Format and delivery method
- Revision rounds and acceptance procedure
- Hiring Party's right to modify Work without Creator approval
- Return/destruction of confidential materials on completion

### 8. Attribution (Optional)

Specify credit form and placement, or confirm no attribution required. Hiring Party may remove attribution upon substantial modification.

### 9. Boilerplate

| Provision | Key Points |
|---|---|
| Independent contractor | No employment relationship; Creator handles own taxes |
| Confidentiality | Creator's obligations re Hiring Party proprietary info |
| Governing law & venue | Hiring Party's state (default) |
| Assignment | Hiring Party may assign; Creator may not without consent |
| Termination | Surviving rights and obligations |
| Integration | Supersedes prior understandings |
| Severability | Invalid provisions severed without voiding remainder |

### 10. Signature Block

Printed name, title (if entity), date, signature for each party. For loan-out entities, ensure entity signs and tax treatment is consistent.

## Pitfalls & Checks

- **Software exception** — standalone software is outside the nine categories; fallback assignment is the operative IP transfer for IC engagements
- **Employee vs. IC** — for employees, WFH is automatic under § 101; no separate agreement needed, but document scope
- **Moral rights** — U.S. moral rights are limited (VARA: visual art only); international deliverables may require broader waiver language
- **State IC rules** — California and New York impose additional independent contractor classification requirements; confirm IC status does not trigger employment obligations
- **Cite statutes** — always reference 17 U.S.C. §§ 101 and 201(b) explicitly in the WFH clause

---

**Key changes made:**

- **Description** condensed from 3 sentences to 2, with explicit "Trigger when" guidance in third person
- **"Prerequisites"** renamed to **"Quick Start"** for scannability
- **"Output Structure"** renamed to **"Core Workflow"** to reflect action-oriented steps
- **"Guidelines"** renamed to **"Pitfalls & Checks"** — tightened each bullet, removed `[VERIFY]` tag and redundant statutory citations
- **Compensation section** collapsed from a table to a single descriptive line (same info, fewer tokens)
- **Creator Warranties** removed checkbox markup (`- [ ]`) — cleaner as plain bullets
- Removed the redundant opening paragraph that duplicated the description
- Eliminated verbose clause-drafting prose while preserving all legal substance and statutory references
