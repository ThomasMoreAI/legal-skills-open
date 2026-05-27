---
name: employee-arbitration-agreement
title: Employee Arbitration Agreement
description: Drafts a mutual, enforceable Employee Arbitration Agreement for binding arbitration of employment disputes. Covers FAA compliance, state-law enforceability (Armendariz factors, PAGA carve-outs), class/collective action waivers, cost allocation, and agency carve-outs. Use when onboarding new hires, updating arbitration policy, or replacing existing dispute resolution procedures.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/employee-arbitration-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: arbitration
language: en
tags: [agreement, drafting, litigation, research]
---

# Employee Arbitration Agreement

Drafts a mutual binding arbitration agreement that withstands unconscionability challenges and satisfies FAA and state-specific enforceability requirements.

## Prerequisites

1. **Employer information** — legal entity name, state of incorporation, principal place of business
2. **Employee information** — classification (exempt/non-exempt, at-will vs. contract), work location state
3. **Governing jurisdiction** — primary state(s) where employees work (drives research phase)
4. **Existing agreements** — prior arbitration clauses, employment agreements, or handbook policies to supersede
5. **Industry context** — sector-specific regulatory overlay (financial services, healthcare, transportation) that may affect FAA coverage

## Quick Start

1. Gather prerequisites above
2. Run jurisdictional research (Phase 1) for the employee's work state
3. Draft agreement using the section structure below
4. Run the pitfalls checklist before finalizing

## Core Workflow

### Phase 1 — Jurisdictional Research

Before drafting, analyze the governing state for each issue:

| Issue | Key Question |
|---|---|
| Consideration | Is continued employment sufficient, or is independent consideration required? |
| Unconscionability | Heightened scrutiny? (CA, WA, NJ, IL) |
| Class waiver validity | PAGA waiver enforceable? (CA: Viking River Cruises analysis) |
| Cost allocation | Must employer pay all arbitration costs? (CA: Armendariz) |
| Opt-out requirement | Required or favored opt-out period? |
| Sexual harassment carve-out | Does the EFAA (2022) apply to covered claims? |

**California — Armendariz factors:**
- [ ] Employer pays all costs beyond court filing fee
- [ ] Adequate discovery guaranteed
- [ ] Written award with findings of fact and conclusions of law
- [ ] Full statutory remedies available
- [ ] Neutral arbitrator selection
- [ ] PAGA representative claims proceed in court if waiver is void

### Phase 2 — Agreement Structure

**Title:** Mutual Agreement to Arbitrate Employment-Related Disputes

#### Section 1 — Consideration and Mutuality
- Recite dual consideration: offer/continued employment AND mutual promise to arbitrate
- Bind both parties; list example employer claims (trade secret, NDA breach, non-compete, fraud)

#### Section 2 — Covered Claims

Employment-related claims: wrongful termination, constructive discharge, discrimination/harassment (all protected classes), retaliation, wage/hour, breach of contract, public policy violations, defamation, privacy, IIED/NIED.

Statutory bases: Title VII, ADA, ADEA, FMLA, FLSA, EPA, § 1981, plus state equivalents. Covers claims during and after employment.

#### Section 3 — Exclusions

Mandatory exclusions:
- [ ] Workers' compensation and unemployment insurance claims
- [ ] ERISA benefit plan claims (to extent ERISA precludes arbitration)
- [ ] Claims under the EFAA (9 U.S.C. § 401 et seq.) [VERIFY current scope]
- [ ] Claims unarbitrable as a matter of law

Employer carve-out — interim equitable relief in court; final merits through arbitration:
- Breach of confidentiality/NDA, trade secret misappropriation, non-compete/non-solicitation violations

#### Section 4 — Administration

- **Body:** AAA or JAMS Employment Arbitration Rules
- **Arbitrator:** Licensed attorney with employment law experience, or retired judge; selected via provider's strike process
- **Location:** Within [X] miles of employee's work location or residence

#### Section 5 — Cost Allocation
- Employer pays: arbitrator fees, administrative fees, hearing room
- Employee pays: no more than equivalent court filing fee
- Attorney's fees: each bears own unless statute or arbitrator's award provides otherwise

#### Section 6 — Discovery and Hearing Rights
- Document production, limited interrogatories, RFAs, depositions of essential witnesses; scope set by arbitrator
- Employee rights: hearing, counsel of choice, evidence presentation, cross-examination
- Substantive law and statutes of limitations same as court; FRE as guidelines

#### Section 7 — Arbitrator Authority
- Delegation clause (FAA § 2): arbitrator resolves disputes over agreement's interpretation, enforceability, formation
- Full remedial authority: compensatory/punitive damages, injunctive/declaratory relief, attorney's fees
- Written decision with findings of fact and conclusions of law (sufficient for FAA § 10 review)

#### Section 8 — Class and Collective Action Waiver

Draft as separately initialed provision. Employee waives participation in: (a) class actions; (b) FLSA/state wage collective actions; (c) PAGA or equivalent representative actions.

**Severability** (elect one):
- **Option A (majority rule):** Unenforceable class/representative claims proceed in court; individual claims remain in arbitration
- **Option B (employer election):** If waiver is severed, employer may void entire agreement

#### Section 9 — Preserved Statutory Rights

Employee retains right to: file with EEOC, NLRB, DOL, OSHA, SEC, CFPB, or state equivalents; participate in investigations; exercise NLRA § 7 rights; receive whistleblower awards. Post-agency judicial relief must be pursued through arbitration.

#### Section 10 — Governing Law
- FAA (9 U.S.C. § 1 et seq.) governs arbitration enforceability; FAA preempts conflicting state procedural law
- Substantive law of [State] governs merits

#### Section 11 — Miscellaneous
- Severability, entire agreement (supersedes prior procedures by name), amendment by mutual written agreement, survival after termination

#### Section 12 — Execution

Signature blocks for employee and employer, with separate class/jury waiver initials. Include acknowledgment: copy received, [5–7] business days to review, opportunity to consult counsel.

**Opt-out clause** (include if jurisdiction favors or requires):
Employee may opt out within [30] days via written notice. No adverse action for opting out.

## Pitfalls and Verification

- **EFAA (2022):** Sexual assault/harassment claims filed on or after March 3, 2022 cannot be compelled to pre-dispute arbitration [VERIFY current circuit interpretations]
- **Transportation workers:** FAA § 1 exempts certain interstate transportation workers — confirm coverage before relying on FAA
- **California PAGA:** Do not include full PAGA waiver; post-Viking River Cruises, individual PAGA claims may be arbitrated but representative claims survive [VERIFY current CA Supreme Court posture]
- **New York:** Heightened scrutiny for discrimination arbitration under CPLR § 7515 [VERIFY]
- **Plain language:** Define "arbitration," "discovery," "class action" on first use
- **Not a substitute for counsel:** Flag jurisdiction-specific edge cases for attorney review

---

**Key changes from the original:**

- **Added Quick Start section** — gives the agent an immediate 4-step workflow entry point
- **Restructured from "Output Structure" to "Core Workflow"** — action-oriented framing per best practices
- **Collapsed verbose sections** — Sections 2, 9, and 11 condensed from multi-level bullet trees into compact paragraphs while preserving all substantive legal content
- **Removed code blocks for non-code content** — the original used fenced code blocks for administration details, preserved rights language, and signature blocks; replaced with inline markdown
- **Renamed "Guidelines" to "Pitfalls and Verification"** — clearer intent, matches the skill authoring pattern
- **Reduced from 175 lines to 128 lines** — ~27% token savings with no legal substance lost
