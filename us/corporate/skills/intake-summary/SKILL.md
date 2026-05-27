---
name: intake-summary
title: Client Intake Summary (Corporate)
description: 'Produces a structured U.S. corporate client intake summary from intake forms, consultation notes, and initial communications. Outputs an executive overview, client profile, matter description, timeline, legal considerations, financials, risks, and follow-up questions with source mapping. Use for corporate governance intake, new matter onboarding, and client management summaries. Trigger keywords: client intake summary, intake form, consultation notes, corporate governance, new matter overview.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/intake-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [summarization, summary]
---

# Client Intake Summary (Corporate)

Convert raw intake materials into a structured, source-cited matter overview for initial attorney review.

## Prerequisites

1. Intake materials: forms, notes, emails, attachments, and any provided documents
2. Client identifiers: legal name and entity type (if available)
3. Matter scope: corporate governance or related client management issue
4. Jurisdiction signals: state(s) of formation, operations, or dispute nexus

## Output Structure / Process

Use the template below and populate with extracted facts. Every factual statement should include a source tag in the form `(Source: {doc id/page/line or email date})`. If missing, mark as `Unknown`.

```
# Executive Overview (2–3 sentences)
- [Summary of issue, client objective, and urgency with source tags.]

# Client Profile
| Field | Details | Source |
|---|---|---|
| Legal name |  |  |
| Entity type |  |  |
| Formation state |  |  |
| Primary contacts |  |  |
| Preferred communication |  |  |
| Language/access needs |  |  |
| Key stakeholders |  |  |

# Matter Description
| Topic | Details | Source |
|---|---|---|
| Issue summary |  |  |
| Key parties |  |  |
| Client objectives |  |  |
| Business context |  |  |
| Prior actions taken |  |  |
| Documents referenced |  |  |

# Timeline of Key Events
| Date | Event | Source |
|---|---|---|
|  |  |  |

# Preliminary Legal Considerations
- Area(s) implicated: 
- Jurisdiction questions:
- Governance instruments involved (bylaws, charter, operating agreement):
- Potential deadlines or time sensitivity:
- Conflicts check status:

# Financial Discussions
| Item | Details | Source |
|---|---|---|
| Fee structure discussed |  |  |
| Retainer amount |  |  |
| Budget constraints |  |  |
| Billing preferences |  |  |

# Risks / Red Flags
- Inconsistencies or credibility issues:
- Unclear authority or standing:
- Complexity indicators:
- Unrealistic expectations:

# Follow-Up Questions
- 
- 
- 

# Immediate Next Steps
- 
- 
- 

# Source Map (if multiple materials)
| Source ID | Description | Date | Notes |
|---|---|---|---|
|  |  |  |  |
```

## Guidelines

- Use clear, neutral legal tone; avoid advocacy or conclusions not supported by sources.
- Cite the exact intake source for each fact; avoid unsourced paraphrase.
- Flag missing facts with `Unknown` and surface as follow-up questions.
- Call out potential conflicts and urgency without assuming outcomes.
- Keep dates in `YYYY-MM-DD` format and verify entity spellings against source documents.
- Scope to U.S. corporate governance intake; if non-U.S. issues appear, label as jurisdictional uncertainty.
