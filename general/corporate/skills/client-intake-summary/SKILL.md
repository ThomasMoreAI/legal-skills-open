---
name: client-intake-summary
title: Client Intake Summary
description: Produces a structured corporate-client intake brief from intake forms, consultation notes, and initial communications. Use when onboarding a new corporate matter, processing an intake packet, summarizing consult notes, running a conflict check, or triaging deadlines for a corporate governance matter.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/client-intake-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Client Intake Summary

Converts raw intake materials into an evidence-tagged, team-ready brief for attorney review and matter activation.

## Prerequisites

Gather before starting:

- **Intake packet**: forms, engagement data, identity/contact details, entity structure
- **Communications**: emails, call/meeting notes, preliminary documents
- **Jurisdiction cues**: governing state, filing location, corporate governing documents
- **Conflict inputs**: firm CRM/conflict database or prior-representation list (or note that none was available)
- **Fee framework**: hourly/flat expectations, retainer status, billing constraints, payor source
- **Time-sensitive facts**: deadlines, hearings, board dates, contract expirations
- **Scope notes**: permission and confidentiality scope for each source document

## Quick Start

1. Collect and tag all source documents.
2. Run conflict/ethics check (or note gap).
3. Draft the brief using the section order and template below.
4. Mark every unknown field `Unknown` and every unverified legal point `[VERIFY]`.
5. Route to assigning attorney with urgency classification.

## Output Sections

Produce in this fixed order:

| Section | Content | Format |
|---|---|---|
| Executive Overview | 2–3 sentences: matter, client objective, urgency | Plain text |
| Client Profile | Names, roles, contacts, communication prefs, confidentiality sensitivity | Bulleted fields |
| Matter Snapshot | Type, legal issue, key parties, factual timeline, status, governing entities | Chronological table |
| Preliminary Legal Considerations | Governing law cues, implied claims, jurisdiction questions, privilege/authority risks, SOL flags | Checklist |
| Financial Notes | Fee discussion, retainer, budget constraints, funding source, billing risk | Bullets; standardize dollar amounts |
| Risks and Red Flags | Inconsistencies, credibility issues, unrealistic outcomes, complexity indicators | Risk table (Low/Med/High) |
| Conflicts and Ethics | Conflict search status, adverse-party overlap, confidentiality conflicts, privilege boundaries | Status table |
| Follow-Up Queue | Missing facts, documents, and answers needed | Numbered action list |
| Immediate Next Steps | 24h actions, 7-day actions, owner, dependency | Prioritized checklist |

### Header Template

```text
Client:
Matter ID:
Matter Type:
Jurisdiction:
Intake Sources:
Date Received:
Status: New / Pending / Urgent
```

## Core Drafting Rules

1. **Facts vs. inferences** — every `Fact` row must cite at least one source.
2. **Dates** — use `YYYY-MM-DD` throughout.
3. **Client quotes** — preserve only when materially relevant.
4. **Names** — verify spellings against source materials; do not over-edit.
5. **Uncertainty** — flag with `[VERIFY]` and list what must be checked.
6. **Order** — address conflict/confidentiality posture before legal merits.

## Pitfalls and Checks

- **No legal advice.** Tone is internal and professional; no counseling recommendations.
- **Urgency required.** Every brief must classify as `Immediate`, `This Week`, or `Routine`.
- **SOL / filing deadlines.** If mentioned, include the governing trigger rule + `[VERIFY]` for jurisdiction-specific requirements.
- **No fabricated timelines.** Missing dates go in the Follow-Up Queue, not invented.
- **Confidentiality.** Avoid unnecessary sensitive disclosures in shared summaries.
- **Corporate governance.** Capture entity authority limits, board/committee roles, and document governance references.
- **Closing line.** End with: recommended assignment owner, recommended first task, and estimated start date.
