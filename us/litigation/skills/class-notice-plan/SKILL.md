---
name: class-notice-plan
title: Class Notice Communication Plan
description: Drafts a Rule 23 class notice communication plan for U.S. federal class actions, covering notice content, delivery methods, timelines, budgets, and reporting to satisfy the "best notice practicable" standard. Use after class certification or when seeking settlement approval. Trigger when user mentions class notice, notice plan, communication plan, Rule 23(c)(2)(B), claims administrator, or CAFA notice.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/class-notice-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Class Notice Communication Plan

Produces a court-ready plan for disseminating class notice under Fed. R. Civ. P. 23(c)(2)(B) and due process requirements.

## Prerequisites

Collect before drafting:

- Class certification order or proposed certification motion
- Class definition and any subclasses (verbatim from order)
- Claims, defenses, and relief sought
- Court-ordered deadlines (opt-out, objection, fairness hearing, trial)
- Available class member data sources and quality assessment
- Settlement terms affecting notice (if applicable)
- Proposed claims administrator or notice expert (if any)

## Quick Start

Generate each section below in order. Populate tables from user-supplied inputs. Mark unknowns with `[TBD]`.

## Core Sections

### 1. Case Header

Table with: case name, court/case number, judge, procedural posture, certification order date, governing rules (default: Fed. R. Civ. P. 23(c)(2)(B); due process), key deadlines.

### 2. Legal Standards

| Authority | Requirement |
|---|---|
| Fed. R. Civ. P. 23(c)(2)(B) | Best notice practicable; individual notice where feasible |
| Mullane v. Central Hanover Bank | Notice reasonably calculated to apprise interested parties |
| Eisen v. Carlisle & Jacquelin | Individual notice to identifiable class members |
| CAFA 28 U.S.C. § 1715 | Government notice for covered settlements (if applicable) |

### 3. Class Definition and Identification

Table with: class definition (verbatim), subclasses (verbatim), estimated class size, geographic/temporal limits, data sources, data gaps and remediation plan.

### 4. Required Notice Content

Every notice must include per Rule 23(c)(2)(B):

- [ ] Nature of the action
- [ ] Definition of the class
- [ ] Class claims, issues, and defenses
- [ ] Right to enter an appearance through counsel
- [ ] Right to request exclusion and method for doing so
- [ ] Time and manner for requesting exclusion
- [ ] Binding effect of a class judgment on class members

### 5. Notice Form Specifications

- **Tone**: Neutral, non-advocacy
- **Readability**: Plain language; target ~8th grade for consumer classes
- **Languages**: Translations where material class segments are non-English
- **Accessibility**: ADA-compliant; mobile-responsive web

### 6. Delivery Methods

| Channel | When Used | Key Notes |
|---|---|---|
| Direct mail | Identifiable addresses | First-class; NCOA updates; re-mail undeliverables |
| Email | Reliable email addresses | SPF/DKIM compliance; bounce tracking |
| Publication | Non-identifiable members | Targeted print/digital; market-specific |
| Digital ads | Broad or niche reach | Geo/demo targeting aligned with class |
| Settlement website | All cases | Notice, claim form, FAQs, key dates |
| Toll-free line | All cases | Live + automated; multilingual if needed |

### 7. Data Hygiene

- [ ] Run NCOA updates before initial mailing
- [ ] Track returns; skip-trace undeliverables
- [ ] Re-mail within defined window after address correction
- [ ] Maintain audit trail of all address updates

### 8. Timeline

Milestones: court approval of plan → data extraction → website/hotline live → mail/email launch → publication run → opt-out deadline → objection deadline → fairness hearing/trial → due diligence declaration filed.

Default timing guidance (when not court-ordered):
- Direct notice: 60-90 days before opt-out deadline
- Publication: 2-4 weeks aligned with direct notice
- Re-mailing: 14-21 days after return processing

### 9. Budget

Categories: claims administrator fees, data processing, printing/mail, publication, website/hosting, hotline, translation, contingency (10-20% reserve). Include basis and estimate for each.

### 10. Court Approval Package

- [ ] Proposed notice plan
- [ ] Proposed notice forms
- [ ] Declaration from notice expert or claims administrator
- [ ] Compliance statement for Rule 23 and due process
- [ ] CAFA notice plan (if applicable)

### 11. Monitoring and Reporting

| Metric | Source | Use |
|---|---|---|
| Mail sent/returned/re-mailed | Mail logs | Due diligence declaration |
| Email delivered/bounced | ESP reports | Effectiveness metrics |
| Publication insertions | Media affidavits | Compliance proof |
| Website traffic | Analytics | Reach assessment |
| Hotline volume | Call logs | Issue tracking |
| Opt-outs/objections | Administrator tracking | Court reporting |

### 12. Exhibits

List: (A) long-form notice, (B) postcard/short-form notice, (C) publication notice, (D) media plan and rate cards, (E) due diligence declaration template.

## Pitfalls and Checks

- Never disseminate notice before court approval
- Use verbatim class definitions from the certification order
- Align all deadlines with court orders; never invent dates
- CAFA notice is mandatory for covered settlements
- Avoid legalese; clarity and neutrality are required
- Flag jurisdiction-specific deviations if not in federal court
- Add `[VERIFY]` to any uncertain citation or rule

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec (only `name` and `description` are valid frontmatter fields)
- **Tightened description** — added explicit trigger guidance ("Trigger when user mentions...")
- **Collapsed empty template tables** — Sections 1, 3, and 9 now use inline prose descriptions instead of large empty-value tables that Claude can generate on its own
- **Converted checklists to task format** — Used `- [ ]` for actionable items (sections 4, 7, 10) to match workflow checklist patterns
- **Condensed timeline** — Replaced the empty milestone table with a compact arrow-chain flow plus timing defaults
- **Reduced from ~170 lines to ~120 lines** — removed token cost of empty table scaffolding while preserving all domain-critical content (legal standards, Rule 23 requirements, delivery methods, monitoring metrics)
- **Added Quick Start** section per best practices
