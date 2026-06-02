---
name: intake-triage
title: Intake Triage
description: Classify an incoming legal-work request and route it to the right team.
author: stubbi
author_url: https://github.com/stubbi/companies-legal/tree/main/legal-and-contracts/skills/intake-triage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Intake Triage

> **Port-original skill.** Hand-authored for Legal & Contracts. Owned by the CEO role.

## When to fire

Any new work request arriving without an explicit team / agent assignment. This is the first skill the CEO runs on incoming items — a partner's email, a Slack ping from product, a board chair's request, or an inbound issue.

## Inputs

- The raw request: an email, a meeting note, a Slack message, an issue body.
- Optional context: requester role (founder, GC, partner, paralegal), deadline, matter / client name, attachments (counterparty paper, board materials, etc.), jurisdiction.

## Outputs

A triage decision written back as a short note on the request:

```yaml
team: contracts | corporate | research-review | escalate
primary_agent: <agent-slug>
secondary_agents: [<agent-slug>, ...]   # for cross-team work; CEO coordinates via cross-team-coordination
priority: P0 | P1 | P2 | P3
deadline: <ISO date or "asap" or "best-effort">
attorney_owner: <name of supervising attorney>   # who signs off before output leaves the firm
boundaries: [<note>, ...]                        # call out anything that requires human sign-off beyond the default
```

## How to triage (decision tree)

1. **Is this a contract draft or redline?** → `contracts`.
   - Drafting NDA / MSA / SOW / offer / vendor agreement → `contract-drafter`.
   - Reviewing counterparty paper → `redline-reviewer`.
   - Adding a new clause / updating the playbook → `clause-library-curator`.
2. **Is this corporate / governance / cap-table?** → `corporate`.
   - Cap-table update (grant, exercise, transfer, financing) → `cap-table-maintainer`.
   - Board / shareholder consent or formation doc → `board-consent-drafter`.
3. **Is this legal research, regulatory work, or engagement-letter drafting?** → `research-review`.
   - Case-law / statute / regulatory summary → `case-summarizer`.
   - Engagement / intake letter → `intake-letter-drafter`.
4. **Does it span 2+ teams?** Pick the team that owns the *output* and list the others in `secondary_agents`. Then enqueue `cross-team-coordination`. Typical patterns: a financing needs board consent + cap-table update + investor NDA; a new client engagement needs an engagement letter + intake conflict check + first NDA.
5. **Does it ask for legal advice the agents can't give?** → `escalate`. Examples: "Should we settle this dispute?", "Is this clause enforceable in California?", "Can we ignore the auditor's request?" Triage as escalate and route to the named supervising attorney; do not assign to a specialist who might try to answer.

## Boundaries

- The CEO does not perform the triaged work — only routes it.
- If the request is ambiguous, ask the requester one clarifying question rather than guessing. Don't over-interpret a one-line message.
- Every triage decision must name the `attorney_owner`. Unsigned work product never leaves the firm; the attorney owner is the person who will sign off.
- Anything that smells like substantive legal advice, a regulatory interpretation, or a litigation strategy decision escalates immediately, even if the request looks routine.

- **UPL line.** This skill is designed against the unauthorized-practice-of-law line. Output may not be delivered to a recipient, and the agent may not be held out to anyone, until a licensed attorney admitted in the recipient's jurisdiction has reviewed and signed off. The agent does not hold itself out as a lawyer, does not form an attorney–client relationship, and refuses requests that would cross that line. UPL is determined by the recipient's jurisdiction, not the operator's — when in doubt, route to `escalation-routing`.

## Output protocol

Write the triage decision as a comment / note on the work item, tag the primary agent for pickup, and (if cross-team) enqueue `cross-team-coordination` on yourself before any specialist starts.
