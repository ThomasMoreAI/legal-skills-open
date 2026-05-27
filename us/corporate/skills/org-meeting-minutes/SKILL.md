---
name: org-meeting-minutes
title: Organizational Meeting Minutes
description: Drafts organizational meeting minutes for newly formed corporations or LLCs, covering quorum, bylaws/OA adoption, elections, capitalization, banking, and tax elections. Use when forming a new entity, drafting initial board minutes, or completing corporate organization post-filing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/org-meeting-minutes
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [drafting, memo]
---

# Organizational Meeting Minutes

Produces corporate-book-ready minutes of an entity's initial organizational meeting, compliant with state formation requirements.

## Prerequisites

Collect before drafting:

1. **Filed articles** — Incorporation (corp) or organization (LLC) with state confirmation
2. **Bylaws or operating agreement** — Draft or adopted version
3. **Participant list** — Full legal names and capacities (incorporator, director, officer, member)
4. **Capitalization details** — Authorized shares/units, consideration, initial holders
5. **Banking preferences** — Bank, authorized signatories, signing limits
6. **Tax elections** — S-corp (Form 2553), fiscal year end, other elections
7. **State quorum rules** — Applicable corporate/LLC statute requirements

## Quick Start

Draft minutes in four sections: Header, Attendance & Quorum, Organizational Resolutions, Adjournment.

Each resolution uses a formal "RESOLVED" block with voting record: "motion by [Name], seconded by [Name], unanimously approved."

## Output Structure

### 1. Header

| Field | Content |
|-------|---------|
| Title | "Minutes of the Organizational Meeting of [Full Legal Entity Name]" |
| Date/Time | Exact date and time |
| Location | Physical address, or virtual platform (confirm all could hear/communicate) |
| Purpose | "To complete the organization of the [corporation/LLC] and take all actions necessary to commence business operations" |

### 2. Attendance & Quorum

- List each attendee: full legal name + capacity
- State quorum with statutory basis:
  - **Corp**: majority of directors, or incorporator(s) if board not yet seated
  - **LLC**: per state statute and operating agreement
- Record notice given or waivers obtained
- Record election of chairperson and secretary (nomination, second, vote)

### 3. Organizational Resolutions

Draft each as a formal "RESOLVED" block. Include all applicable:

**Governance**
- [ ] Adopt bylaws (corp) or operating agreement (LLC) — note copies reviewed
- [ ] Elect directors — name, term for each
- [ ] Elect officers — name, title (President, Secretary, Treasurer, VPs)
- [ ] Designate principal office address
- [ ] Adopt corporate seal (if applicable)
- [ ] Approve fiscal year end
- [ ] Adopt stock/membership certificate forms
- [ ] Set regular board meeting schedule

**Capitalization**
- [ ] Authorize share/unit issuance — number, class, consideration, recipients
- [ ] Approve equity incentive plans (if immediately contemplated)

**Banking & Finance**
- [ ] Authorize bank accounts — institution, account type
- [ ] Designate authorized signatories with signing limits
- [ ] Authorize reimbursement of incorporator organizational expenses (itemize)

**Tax & Regulatory**
- [ ] Tax elections (S-corp Form 2553, etc.) — authorize officer to execute
- [ ] Authorize foreign state qualification (if needed)

**Ratifications & Contracts**
- [ ] Ratify pre-formation agreements — date, parties, subject
- [ ] Approve third-party contracts (lease, counsel, accountants)
- [ ] Indemnification provisions beyond bylaws

### 4. Adjournment & Authentication

Include adjournment motion, signature blocks for Secretary and Chairperson, and board approval date line.

## Pitfalls

- **Conflicts of interest** — If disclosed, document the disclosure and any recusal from related votes
- **Privileged material** — Never include attorney-client privileged discussions or sensitive strategy
- **State variation** — Quorum rules, officer requirements, and notice provisions vary by state; confirm against the applicable business corporation act or LLC act
- **Due diligence readiness** — These minutes are routinely requested in financing, M&A, and audit; maintain formality throughout

---

**Key changes made:**

- **Description** — Tightened to stay under 1024 chars while preserving trigger guidance
- **Added Quick Start** — Two-sentence orientation for the most common workflow
- **Removed verbose adjournment code block** — Replaced with a concise one-liner; the agent can generate the boilerplate from context
- **Shortened checklist items** — Trimmed wording ("Authorization of" → "Authorize", "Adoption of" → "Adopt") for token efficiency
- **Renamed "Guidelines" → "Pitfalls"** — Aligns with best-practice section naming; dropped the two items that were self-evident ("voting format" already covered in Quick Start, "record book" is implicit)
- **Overall** — ~30% token reduction while preserving all domain-critical legal content
