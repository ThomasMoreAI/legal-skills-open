---
name: ir-tabletop-exercise
title: Tabletop Exercise Script for Incident Response Plan
description: Drafts a tabletop exercise script to stress-test an organization's Incident Response Plan against cybersecurity threats and breach notification obligations (GDPR, CCPA, HIPAA, GLBA, PCI DSS, NERC CIP, DFARS, SEC). Produces scenario injects, participant role assignments, facilitation guides, and after-action report frameworks. Use when creating IR tabletop exercises, cybersecurity drills, breach response simulations, or incident preparedness assessments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ir-tabletop-exercise
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
tags: [checklist, drafting, regulatory]
---

# Tabletop Exercise Script for Incident Response Plan

Produces a ready-to-execute tabletop exercise that tests an organization's IR Plan against realistic cyber threats and regulatory notification deadlines.

## Prerequisites

1. **IR Plan** — current incident response plan, escalation hierarchy, severity classification framework
2. **Regulatory profile** — applicable frameworks and notification deadlines
3. **Org context** — industry sector, data holdings (PII, PHI, PCI, IP), crisis roles, prior after-action reports
4. **Participant list** — attendees with titles and IR Plan roles

## Quick Start

1. Extract key elements from provided materials (deadlines, escalation paths, data types, prior gaps)
2. Select threat scenario matched to org risk profile
3. Assign participants to functional groups with role cards
4. Design 4–5 progressive injects testing IR phases and notification triggers
5. Draft facilitation guide with ground rules and timing
6. Build debrief agenda and after-action report framework

## Workflow

### Step 1 — Document Research

Extract from provided materials before drafting:

| Element | Source |
|---|---|
| Notification deadlines | Regulatory docs, state-specific windows |
| Escalation hierarchy | IR Plan org chart, decision authority matrix |
| Regulated data types | Data inventory (PII, PHI, PCI, classified/CUI) |
| Prior gaps | After-action reports, audit findings |
| Contractual obligations | Vendor agreements, cyber insurance, customer DPAs |

### Step 2 — Scenario Design

Select a threat scenario matched to org risk profile:

| Scenario | Regulatory Triggers | Key Complexity |
|---|---|---|
| Ransomware + exfiltration | Breach notification + OFAC screening | Dual operational/legal pressure |
| Business email compromise | Wire fraud + credential harvesting | Financial + data exposure |
| Supply chain compromise | Multi-party notification, vendor coordination | Shared liability, scope ambiguity |
| Insider threat | Employee data, HR/legal coordination | Attribution, evidence preservation |
| APT campaign | IP theft, state-actor, law enforcement | Prolonged timeline, classification |

Scenario brief must include:
- Date/time and operational context
- First indicator of compromise (IDS alert, help desk ticket, third-party tip, customer complaint)
- Technical detail sufficient for discussion without requiring deep expertise
- 3–5 measurable objectives tied to IR Plan and regulatory compliance

### Step 3 — Participant Roles

| Group | Roles | Responsibilities |
|---|---|---|
| **Core IR** | IR Manager, Security Analysts, IT Ops, Forensics | Triage, containment, evidence preservation |
| **Legal & Compliance** | General Counsel, DPO/CPO, Outside Counsel | Notification obligations, litigation hold, privilege, sanctions review |
| **Executive** | CEO/Crisis Authority, CISO, CFO, BU Leads | Strategic decisions, business continuity, materiality |
| **Communications** | PR, Customer Service, HR, Investor Relations | Media, customer inquiries, SEC disclosure |

Pre-exercise packet per participant: relevant IR Plan sections, role card with decision authority, notification templates, data holdings summary.

### Step 4 — Progressive Injects

Design 4–5 injects. Per inject include:
- **Timestamp** (T+elapsed), **new information**, and **discussion questions** testing IR procedures, notification triggers, and cross-functional coordination
- **Expected outputs** — decisions or actions participants should produce
- **Facilitator notes** — time allocation, key points that must emerge, red flags indicating gaps

Inject progression:

| # | Focus | Tests |
|---|---|---|
| 1: Detection | Initial alert, IR Plan activation | Severity classification, containment, evidence preservation, escalation |
| 2: Escalation | Scope wider than expected (lateral movement, exfiltration) | Notification threshold, external forensics, insurance notice, legal coordination |
| 3: External Pressure | Ransom demand / media leak / regulator inquiry | OFAC screening, public messaging, regulatory response, cross-team consistency |
| 4: Recovery | Forensic conclusions, restoration, notification deadlines | Notice content, individual notice method, credit monitoring, SEC 8-K if applicable |
| 5 (optional) | Cross-border, law enforcement delay, vendor coordination | Jurisdiction conflicts, notification timing tensions, multi-party coordination |

### Step 5 — Facilitation Guide

Include at top of script:
- **Ground rules** — learning environment, no-fault, Chatham House Rule if desired
- **Timing** — total duration (2–4 hrs), time per inject, break schedule
- **Facilitator role** — present injects, probe follow-ups, ensure all groups participate, document observations without correcting in real-time
- **Materials** — printed inject cards, IR Plan copies, regulatory quick-reference card, shared doc for decisions

### Step 6 — Debrief & After-Action Report

**Debrief agenda (30–45 min):**

1. What worked — effective procedures, coordination, decisions
2. Gaps identified:
   - [ ] Unclear roles or decision authority
   - [ ] Missed or late notification triggers
   - [ ] Communication breakdowns (technical / legal / executive)
   - [ ] Evidence preservation failures
   - [ ] Unrealistic IR Plan assumptions
   - [ ] Resource or capability gaps
3. Root cause per gap
4. Remediation actions with owner + target date

**After-action report sections:**

| Section | Content |
|---|---|
| Executive Summary | Scenario, objectives, overall assessment |
| Participants | Name, title, exercise role |
| Observations by Phase | Detection → Containment → Eradication → Recovery → Notification |
| Gap Analysis | Description, risk rating (H/M/L), root cause |
| Remediation Plan | Action, owner, deadline, success criteria |
| Recommendations | Future exercises, training needs, capability investments |

Distribution: participants, executive leadership, board/audit committee, CISO office.

## Notification Deadline Reference

Build a quick-reference card for participants:

| Regime | Deadline | Authority |
|---|---|---|
| GDPR Art. 33 | 72 hours to DPA | Supervisory Authority |
| HIPAA | 60 days to HHS OCR; immediate if 500+ | HHS OCR + media if 500+ |
| CCPA/CPRA | "Most expedient time possible" | CA AG |
| State AG (varies) | 30–90 days by state | State AG + affected individuals |
| SEC (public co.) | 4 business days (Item 1.05 Form 8-K) [VERIFY] | SEC |
| PCI DSS | Per card brand rules, typically 24–72 hrs | Card brands + acquiring bank |
| NERC CIP | 1 hour (CIP-008-6) [VERIFY] | NERC E-ISAC + CISA |

## Pitfalls

- At least one inject must force a **notification deadline decision with incomplete information**
- Test **OFAC/sanctions compliance** if ransomware scenario involves payment demands
- Ensure the exercise tests **attorney-client privilege** preservation during IR
- Tailor scenario complexity to participant experience — avoid overwhelming first-time groups
- Do not script "correct" answers — the exercise tests the org's plan, not a model plan
- Flag if the org lacks a severity classification framework — the exercise cannot function without one
- Mark any citation or deadline you cannot confirm with `[VERIFY]`

## Troubleshooting

| Issue | Resolution |
|---|---|
| No existing IR Plan | Exercise cannot proceed; recommend IR Plan development first |
| Missing severity classification | Create simplified framework (Critical/High/Medium/Low) for exercise use; flag as gap |
| Participants unfamiliar with notification deadlines | Distribute the quick-reference card in pre-exercise packets |
| Scenario too complex for audience | Drop optional inject 5; simplify technical details; focus on decision-making |
| Cross-border jurisdiction conflicts | Identify controlling jurisdiction per data subject location; flag irreconcilable conflicts for legal review |

---

**Key changes from the original:**

- **Description** — tightened to third-person, removed "comprehensive", added trigger keywords
- **Added Quick Start** — 6-step orientation per spec
- **Restructured body** — renamed "Output Structure" to numbered "Workflow" steps for consistency with other skills
- **Removed verbose inject template** — replaced the full code-fenced template with a concise bullet list of required elements per inject; same coverage, ~60% fewer tokens
- **Collapsed facilitation guide** — from 4 verbose bullet paragraphs to tight keyword-driven bullets
- **Extracted Notification Deadline Reference** — promoted from buried in Guidelines to its own section for visibility
- **Renamed "Guidelines" to "Pitfalls"** — matches spec naming convention
- **Added Troubleshooting** — 5 common issues with resolutions per spec requirement
- **Reduced from 157 to ~137 lines** — all domain-accurate content, regulatory deadlines, and legal checks preserved
