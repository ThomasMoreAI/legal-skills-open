---
name: judgment-summary
title: Judgment Summary
description: Produces structured U.S. litigation judgment summaries from court opinions or final orders. Use when summarizing a judgment, opinion, final decision, post-trial ruling, appeal outcome, or case disposition brief. Covers caption, procedural history, facts, issues, standards of review, holdings, precedent treatment, concurrences/dissents, disposition, and practical implications with pinpoint citations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/judgment-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Judgment Summary

Citation-ready summary of a final judgment or opinion — holdings, standards of review, precedent treatment, and practical impact.

## Prerequisites

1. Full opinion or judgment text with page/paragraph numbering.
2. Case citation details: court, docket number, decision date, judge/panel.
3. Procedural posture and any relevant lower court rulings.

## Quick Start

1. Extract case metadata; confirm jurisdiction.
2. Identify issues, standards of review, and holdings with pinpoint cites.
3. Separate background, material, and disputed facts.
4. Track precedent treatment and circuit-split implications.
5. Capture disposition, remand instructions, and deadlines.
6. Translate holdings into practical implications — no advocacy.

Fill every section below. If a field is missing, write `Not stated`.

## Template

```
CASE CAPTION
- Case name:
- Court:
- Docket no.:
- Decision date:
- Judge/Panel:
- Jurisdiction:
- Prior history:

SYNOPSIS (<=150 words)
- Core holding:
- Practical significance:

PROCEDURAL HISTORY
- Lower court decisions:
- Basis for appeal/review:
- Standard(s) of review:
- Scope of review:

FACTS
- Background facts:
- Material facts:
- Disputed facts:

ISSUES AND HOLDINGS
| Issue | Legal Standard | Rule/Reasoning | Holding | Pin Cite |
| --- | --- | --- | --- | --- |

PRECEDENT TREATMENT
| Case | Treatment (Followed/Distinguished/Overruled/Questioned) | Point of Use | Pin Cite |
| --- | --- | --- | --- |
- Circuit split or split resolution: Yes/No + brief note

CONCURRENCE / DISSENT
- Author(s):
- Key departures:
- Implications:

DISPOSITION
- Result (affirmed/reversed/vacated/remanded):
- Remand instructions:
- Costs/fees:
- Deadlines or conditions:

PRACTICAL IMPLICATIONS
- Litigation impact:
- Transactional/compliance impact:
- Evidence/procedure impact:
- Risk posture or strategy notes:

KEY CITATIONS
- Holdings:
- Critical facts:
- Notable reasoning:
```

Target length: 1,500–3,000 words unless the decision is unusually short.

## Pitfalls

- **Holdings vs. dicta**: Distinguish explicitly; never elevate dicta to holding status.
- **Neutral tone**: No advocacy or editorial framing.
- **Court terminology**: Preserve the court's exact language for standards and tests.
- **Uncertain citations**: Mark with `[VERIFY]`.
- **No inference**: Do not infer facts or procedural steps absent from the opinion.
- **Non-U.S. courts**: Note deviations from U.S. practice in the Synopsis.
- **Pinpoint cites required**: Every holding and every court-labeled material fact needs one.

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not in spec), tightened `description` to be third-person with clear trigger keywords while staying under 1024 chars.
- **Overview**: Condensed to a single line with em-dash for scannability.
- **Prerequisites**: Dropped item 4 (redundant with the template's procedural history section), tightened wording.
- **Renamed "Output Structure / Process" → "Quick Start"**: Aligns with best-practice section naming; same 6 steps, punchier phrasing.
- **Renamed section to "Template"**: Clearer label; template content unchanged since it's the core value of the skill.
- **Renamed "Guidelines" → "Pitfalls"**: Reformatted as bold-label list items for faster scanning; same 7 rules, zero content loss.
- **Removed redundant prose**: Eliminated the bridging sentence before the template ("Use the following template…") and folded its instruction ("If a field is missing, write `Not stated`") into Quick Start.
