---
name: intake-triage-stubbi
title: Intake Triage
description: Receive an incoming matter, classify it (practice area, urgency, scope), and route to the right specialist.
author: stubbi
author_url: https://github.com/stubbi/companies/tree/main/legal-services/skills/intake-triage
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Intake Triage

> **Port-original skill.** Hand-authored for this Agent Company; not from upstream `anthropics/claude-for-legal`. Owned by the CEO role.

## When to fire

Any new matter that arrives without an explicit practice-area assignment. This is the first skill the CEO runs on incoming items — before any specialist is dispatched.

## Inputs

- The raw request: an inbound email, a ticket, a Slack message, a forwarded contract, a counterparty demand, a regulator letter, a journalist inquiry, or any free-text task.
- Optional context: requester role, deadline, related matter ID, attachments.

## Outputs

A triage decision, written back as a short note on the matter, with these fields:

```yaml
team: commercial-transactions | regulatory-compliance | ip-disputes | academy-tooling | escalate
primary_agent: <agent-slug>
secondary_agents: [<agent-slug>, ...]   # for multi-practice matters; the CEO then runs cross-practice-coordination
priority: P0 | P1 | P2 | P3
deadline: <ISO date | "asap" | "best-effort">
jurisdiction_known: yes | no | partial    # call out if the controlling jurisdiction is unclear
privilege_posture: privileged | not-privileged | unclear
boundaries: [<note>, ...]                 # call out anything that requires attorney sign-off
```

## How to triage (decision tree)

1. **Contract review, NDA, MSA, vendor agreement, renewal, amendment?** → `commercial-transactions` / `commercial-legal`.
2. **M&A diligence, board consent, closing checklist, entity compliance, integration?** → `commercial-transactions` / `corporate-legal`.
3. **Hire, termination, worker classification, leave tracking, internal investigation, policy / handbook update, international expansion?** → `commercial-transactions` / `employment-legal`.
4. **DSAR, PIA, DPA review, processing-activity triage, privacy policy drift?** → `regulatory-compliance` / `privacy-legal`.
5. **AI use case triage, AIA, vendor-AI review, AI regulation diff, AI policy drift?** → `regulatory-compliance` / `ai-governance-legal`.
6. **Regulatory feed monitoring, policy diff, gap tracking, NPRM comment, policy redraft?** → `regulatory-compliance` / `regulatory-legal`.
7. **Product launch review, "is this a problem?" question, marketing-claims check?** → `regulatory-compliance` / `product-legal`.
8. **Trademark clearance, FTO triage, C&D, DMCA takedown, OSS license review, IP clauses, IP portfolio?** → `ip-disputes` / `ip-legal`.
9. **Litigation matter, demand letter (drafting or received), subpoena, chronology, deposition prep, brief, privilege log, legal hold?** → `ip-disputes` / `litigation-legal`.
10. **Law-school study work — case briefs, IRAC, outlines, bar prep, Socratic drill?** → `academy-tooling` / `law-student`.
11. **Clinic operations — student onboarding, structured intake, deadline tracking, supervisor-review queue?** → `academy-tooling` / `legal-clinic`.
12. **Discovering or evaluating a community legal skill before installation?** → `academy-tooling` / `legal-builder-hub`.
13. **Multi-practice (M&A diligence touching IP + employment + privacy; product launch touching privacy + AI governance + regulatory; investigation touching employment + litigation + privacy):** pick the practice that owns the *deliverable*, list the others in `secondary_agents`, then enqueue `cross-practice-coordination`.
14. **Escalate immediately to a human attorney** when any of the following is true:
    - The matter has criminal exposure, regulator-imposed deadlines under 72 hours, or active enforcement.
    - The matter requires a fiduciary, ethical, or conflict-of-interest decision the agents cannot make.
    - The matter requires authority to file, send, sign, or settle on the firm's behalf.
    - The jurisdictional analysis is unclear and the answer depends materially on the choice of jurisdiction.
    - The privilege posture is unclear and the next action could waive privilege.

## Boundaries

- The CEO does not perform the triaged work — only classifies and routes it.
- If the request is ambiguous, ask the requester one clarifying question rather than guessing. Don't over-interpret.
- The CEO never renders a legal opinion, never pre-decides a jurisdictional question, and never decides whether something is privileged. Those calls belong to a licensed attorney.
- When a matter could be characterized two ways (privacy + AI governance both touch the same processing activity, for instance), pick the practice that owns the *resulting artifact* and list the other as a secondary.

## Output protocol

Write the triage decision as a comment / note on the matter, and tag the primary agent for pickup. If `cross-practice-coordination` is needed, enqueue that skill on yourself before the specialists start. Record the triage decision in the matter's audit log — the choice itself becomes evidence if the matter is later subject to discovery or regulator review.
