---
name: appeal-document-summary
title: Appeal Document Summary
description: 'Produces structured U.S. appellate document summaries mapping procedural posture, issues on appeal, standards of review, and competing arguments into memo-ready format. Use when summarizing appellate briefs, notices of appeal, records on appeal, or preparing for oral argument. Triggers: appeal, appellate, notice of appeal, standard of review, cross-appeal, appellate brief intake, record on appeal synthesis.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/appeal-document-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [summarization, summary]
---

# Appeal Document Summary

Generates a record-grounded, issue-driven appellate summary with standard-of-review analysis for each issue on appeal.

## Prerequisites

Collect before starting:

1. **Record set** — lower court orders/judgment, briefs, transcripts, docket, exhibits
2. **Party posture** — appellant/appellee, cross-appeals, consolidated matters
3. **Procedural timeline** — judgment date, notice of appeal, briefing schedule
4. **Jurisdictional context** — appellate court, originating court, applicable rules

## Quick Start

Build the memo in this order. Cite the record for every factual assertion or mark the gap explicitly.

1. Identify parties, courts, and appeal type
2. Map procedural posture and jurisdictional basis
3. List each issue on appeal with its standard of review
4. Summarize record-bound facts (disputed facts labeled)
5. Present each side's arguments with authorities
6. Assess dispositive issues and risk
7. Note related proceedings, pending motions, and deadlines
8. Flag research gaps and record supplement needs

## Memo Structure

### Section Outline

1. Case Caption and Courts — parties, originating court, appellate court, appeal type (as of right / discretionary / interlocutory)
2. Procedural Posture and Jurisdiction — judgment/order on appeal, notice of appeal date, timeliness, jurisdictional basis, preservation status
3. Issues on Appeal and Standards of Review — use Table 1
4. Factual Background (Record-Bound) — chronology, key record cites, disputed facts
5. Arguments and Authorities — appellant position, appellee position, conflicts or issues of first impression
6. Dispositive Issues and Risk Assessment — strongest/weakest points, standard-of-review sensitivity
7. Related Proceedings and Collateral Effects — prior appeals, parallel cases, preclusion risks, amicus/public interest
8. Pending Motions and Deadlines — motions, briefing schedule, oral argument date
9. Next Steps and Research Gaps — research tasks, record supplement needs

### Required Tables

**Table 1 — Issues and Standards**

| Issue | Appellant Claim of Error | Appellee Response | Standard of Review | Record Support | Dispositive? |
|-------|--------------------------|-------------------|--------------------|----------------|--------------|

**Table 2 — Key Orders and Rulings**

| Date | Court | Order/Ruling | Impact on Appeal | Record Cite |
|------|-------|--------------|------------------|-------------|

**Table 3 — Authorities Map**

| Issue | Primary Authorities | Opposing Authorities | Conflicts/Novelty |
|-------|---------------------|----------------------|-------------------|

**Table 4 — Record Gaps**

| Topic | Missing/Weak Record Support | Risk | Suggested Remedy |
|-------|----------------------------|------|------------------|

## Pitfalls and Checks

- **Record-binding**: Every fact must cite the record. If unsupported or disputed, label it — never infer facts not in the record.
- **Preservation**: Flag preservation defects and waiver risks in Section 2; these can be dispositive.
- **Jurisdictional defects**: Surface timeliness and jurisdictional issues early — they moot all other analysis.
- **Standard-of-review impact**: For each issue, state the standard and explain in one sentence how it affects the outcome.
- **Relief beyond record**: Note any requested relief that exceeds what the record or standard of review supports.
- **Tone**: Neutral and analytic — assess both sides without advocacy.

---

Key changes from the original:

- **Description** tightened — third-person, includes clear trigger keywords, removed redundant keyword list
- **Eliminated the full markdown template** — the section outline + tables convey the same structure at ~40% of the tokens. The template was largely a repetition of the outline with blank fields.
- **Collapsed "Narrative Rules" and "Guidelines" into "Pitfalls and Checks"** — single section, no repeated advice
- **Added "Quick Start"** — gives the core workflow as an ordered checklist per best practices
- **Overview sentence** kept to one line — Claude already knows what appellate summaries are
- **Total line count** dropped from ~123 to ~73 while preserving all domain-critical content (tables, section structure, record-binding rules, preservation/jurisdictional flags)

It looks like the file write permission was denied. Would you like to approve the write so I can save this to disk?
