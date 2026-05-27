---
name: fiscal-sponsorship-agreement
title: Fiscal Sponsorship Agreement
description: Drafts a Fiscal Sponsorship Agreement between a 501(c)(3) sponsor and an unincorporated or non-exempt project. Enforces IRS compliance via sponsor control, variance power, separate accounting, and donor substantiation under IRC § 170. Use when forming fiscal sponsorship arrangements, onboarding sponsored projects, or drafting charitable project funding agreements.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/fiscal-sponsorship-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
tags: [agreement, corporate, drafting, transactional]
---

# Fiscal Sponsorship Agreement

Drafts a Fiscal Sponsorship Agreement preserving the sponsor's 501(c)(3) status and donor deductibility while giving the project operational clarity.

## Prerequisites

Gather before drafting:

1. **Sponsor details** — legal name, state, EIN, determination letter date
2. **Project details** — name, mission, planned activities, authorized representative(s)
3. **Sponsorship model** — Model A (comprehensive, assets transfer to sponsor) or Model C (pre-approved grant, project retains assets). This materially affects ownership and liability provisions
4. **Financial terms** — admin fee %, disbursement approval thresholds
5. **Term** — fixed or at-will; notice period (30–90 days)
6. **IP allocation** — sponsor-owned, project-retained, or shared with license-back
7. **Fund disposition** — named successor 501(c)(3) or sponsor-selected on termination

## Quick Start

Draft in formal contract prose, numbered for cross-reference. Core sections:

1. Header & parties (names, EIN, effective date)
2. Recitals (exempt status, project mission nexus, model selection)
3. Sponsor responsibilities
4. Project responsibilities
5. Financial terms & fund management
6. Term, renewal & termination
7. Legal relationship & liability
8. Intellectual property
9. Compliance & records
10. Miscellaneous (governing law, disputes, severability, notices)
11. Signature block

## Core Provisions

### Sponsor Responsibilities

- Receive contributions into a named restricted fund with separate GAAP-compliant accounting
- Issue donor acknowledgment letters per IRC § 170(f)(8) for gifts >= $250
- Review and approve all project expenditures; retain ultimate disbursement discretion
- File required IRS and state informational returns covering project activity
- Carry general liability and D&O insurance with specified minimums

**Non-waivable retained authority:**
- Final approval over all budgets and expenditures
- Right to suspend/terminate activities jeopardizing exempt status
- Variance power to redirect funds if project purpose becomes impractical

### Project Responsibilities

- Conduct activities consistent with sponsor's exempt purposes
- Submit expense requests with invoices and charitable-purpose explanation
- Obtain written approval before contracts, hiring, or commitments above $[threshold]
- Submit quarterly financial reports and annual narrative report
- Notify sponsor immediately of legal inquiries or status-threatening events

**Prohibited activities:**
- Political campaign intervention (absolute under § 501(c)(3))
- Lobbying exceeding substantial part test or § 501(h) limits
- Private benefit or inurement transactions
- Fundraising without sponsor's prior written approval

### Financial Terms

| Item | Provision |
|---|---|
| Admin fee | [X]% of gross contributions |
| Fund ownership | Contributions become sponsor's property in restricted fund |
| Disbursement | Written request → sponsor review → payment within [X] business days |
| Variance power | Sponsor may redirect to similar-purpose § 501(c)(3) on termination or purpose failure |
| Earned income | Analyzed under IRC §§ 511–514 for unrelated business income |

### Termination & Fund Disposition

- Voluntary: [30/90]-day written notice by either party
- For cause: immediate on material breach or exempt-status threat; [X]-day cure for curable breaches
- **Funds on termination:** retained by sponsor and granted to a § 501(c)(3) with substantially similar purpose; project may recommend recipient subject to sponsor approval
- Project returns sponsor-owned assets and IP within [X] days

### Legal Relationship & Liability

- Project personnel are not employees or agents of sponsor unless separately engaged
- Sponsor not liable for project's contracts, torts, or obligations unless expressly approved
- Mutual indemnification: project indemnifies sponsor for project activities; sponsor indemnifies for own negligence/willful misconduct
- Project carries insurance naming sponsor as additional insured

### Intellectual Property

- Specify ownership of project-created IP (sponsor or project)
- Define post-termination license-back terms if project-retained
- Require prior written approval for use of sponsor's name, logo, or § 501(c)(3) status
- Publications must acknowledge fiscal sponsorship in sponsor-approved form

## Pitfalls & Checks

- **IRS control requirement** — every financial provision must reinforce sponsor's ultimate discretion; this is the linchpin of deductibility and exempt status
- **Variance power** — must be explicit and unconditional; omission risks IRS challenge to contribution deductibility
- **Model A vs. Model C** — confirm before drafting; Model A transfers assets to sponsor, Model C does not. Wrong model = wrong ownership and liability framework
- **State law** — CA, NY, and others impose additional nonprofit oversight; flag for local counsel
- **Lobbying** — if project anticipates advocacy, add § 501(h) election analysis and expenditure tracking
- **UBI exposure** — substantial earned income requires IRC §§ 511–514 analysis; flag for sponsor's tax counsel

---

**Key changes from the original:**

- **Description** trimmed to under 1024 chars while keeping trigger guidance
- **Sponsorship model** promoted to a prerequisite (was buried in recitals) since it's a gating decision
- **Output Structure** replaced with a compact **Quick Start** section listing the 11 sections
- **11 verbose subsections** with tables, blockquotes, and checkboxes consolidated into 6 tight **Core Provisions** subsections — same legal content, ~55% fewer tokens
- **Signature block** template and boilerplate miscellaneous terms removed (agent already knows standard contract boilerplate)
- **Guidelines** renamed to **Pitfalls & Checks** and tightened; added UBI as a concise line item
- Total line count reduced from 184 to ~105, well under the 500-line limit
