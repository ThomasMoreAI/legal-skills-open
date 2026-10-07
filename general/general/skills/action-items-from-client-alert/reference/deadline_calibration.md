# Deadline Calibration

This reference guides the skill in categorizing deadlines into the report sections (past-deadline, imminent, near-term, future) and handling edge cases.

## Categorization framework

Deadlines are categorized relative to the date of the review (today, when the user is running the skill), not the date of the alert. This matters because alerts arrive at varying intervals after publication, and what counted as "near-term" when the alert was written may be "imminent" or "past" by the time the user reviews it.

The skill needs the alert date (from the document or `alert_date` input) and the review date (today). Categories:

### Past-deadline

Deadlines that have already passed at the time of the review.

These items still warrant action in many cases:
- **Compliance lookback:** if non-compliance is detected, remediation may still be possible.
- **Ongoing obligations triggered by past deadlines:** an effective date may have passed, but the obligation continues.
- **Statute of limitations consideration:** non-compliance during a past period may still be subject to enforcement.

The report should not bury past-deadline items at the bottom; they go in their own section, prominently displayed, because the user needs to know what they may have missed.

### Imminent (within 30 days)

Deadlines within 30 days of review.

These items warrant immediate attention. The report should call them out clearly. If the alert covers many imminent items, the bottom-line summary should note that the alert is largely time-critical.

### Near-term (30 days to 6 months)

Deadlines 30 days to 6 months out.

These items warrant near-term planning but not immediate action. Allow time for organizational response.

### Future (beyond 6 months)

Deadlines more than 6 months out.

These items warrant tracking and longer-term planning. Often reflect regulations with phased implementation or future effective dates.

### Ongoing obligations

Items without specific deadlines that represent continuing requirements (e.g., "maintain records of all data subject access requests"; "annually train staff on data protection"; "monitor sub-processor compliance").

These items don't fit the deadline timeline but are still actionable. The report's separate section makes them visible.

### Recommended (no deadline)

Best-practice items the alert recommends without imposing a deadline. The user can prioritize based on resources and risk appetite.

## Edge cases

### Deadlines that vary by organization

Many regulations have different deadlines for different organization sizes:

- **Phased compliance:** large organizations comply by Date A; medium by Date B; small by Date C.
- **Activity-based deadlines:** organizations engaged in Activity X comply by Date A; others have no deadline.
- **Geographic-based deadlines:** California organizations comply by Date A; others have no California-specific deadline.

The skill captures all tiers and flags which one applies based on `organization_context`. If `organization_context` is not provided, the skill notes the tiered structure and flags applicability uncertainty.

### Trigger-based deadlines

Some deadlines are relative to a trigger event rather than a calendar date:

- **"Within 30 days of receiving a request"** — depends on when (and whether) requests arrive.
- **"No later than 90 days after the close of the fiscal year"** — depends on the user's fiscal year end.
- **"Within 72 hours of becoming aware of a breach"** — depends on (hopefully not) breach occurrence.

The skill captures the structure rather than producing a calendar date. The report describes the trigger and the duration.

### Pending or uncertain deadlines

Some deadlines are pending finalization:

- **"Final rule expected in Q2 2026"** — the rule isn't final; the deadline isn't fixed.
- **"Effective date to be determined upon publication"** — no deadline yet.
- **"Comment period closes [date]"** — that's the comment deadline, not a compliance deadline.

The skill notes that the deadline is pending and provides what's known. These items are typically informational rather than actionable until the deadline crystallizes.

### Deadlines that have shifted

Sometimes alerts publish before regulations are finalized; the regulation's deadline may shift after publication. Without the user telling the skill, the skill cannot detect this. If the user notes a deadline has shifted, the skill should flag the discrepancy and use the current deadline.

### Deadlines that have passed but are subject to extensions

Some regulatory deadlines have official or de facto extensions (FDA enforcement discretion; SEC delay of effective date; phased rollout that pushes back de facto deadlines). The skill extracts the alert's stated deadline; if the user is aware of an extension, the user supplements.

### Deadlines that are aspirational

Some "deadlines" in client alerts are not legal deadlines but rather "by then you'll want to be ready" benchmarks set by the law firm. The skill should distinguish:

- **Legal deadline:** "[Regulation] effective March 1, 2026."
- **Practical preparation deadline:** "Companies should aim to have new procedures in place by Q1 2026 to allow for testing before the March 1 effective date."

Both go into the report; the legal deadline is mandatory, the practical preparation is recommended.

## Calibrating "imminent" thresholds

The 30-day threshold for "imminent" is a default. For some regulatory regimes, shorter or longer thresholds make sense:

- **Tax filing deadlines** — "imminent" might be 14 days, since tax filings have inflexible deadlines and require pre-filing preparation.
- **SEC disclosure deadlines** — "imminent" might be 60-90 days, since disclosure requirements often involve coordination across multiple functions.
- **Routine compliance certifications** — "imminent" might be 14-21 days.

The skill uses 30 days as the default and notes when a different threshold might apply.

## Output formatting for deadlines

Each action item entry should clearly state the deadline:

- **For specific dates:** "By [date] (XX days from review date)."
- **For relative deadlines:** "Within [duration] of [trigger event]."
- **For periodic obligations:** "[Periodicity], starting [date]."
- **For pending deadlines:** "Pending finalization; current expectation is [date]."

The "(XX days from review date)" calculation helps the user assess imminence at a glance.

## When deadlines are absent or unclear

Some alerts describe regulatory developments without imposing specific deadlines:

- **Enforcement priorities** — agency announces it will focus on a particular area; no deadline, just heightened risk.
- **Industry guidance** — agency publishes non-binding guidance; no deadline, but practitioners may want to align.
- **Pending litigation** — alert describes ongoing litigation that may produce future requirements.

For these, the report's "Recommended" or "Informational" sections capture the items. The skill should not invent deadlines.

## When the alert itself is dated

If the alert is more than a year old, the skill notes this in "Notes on this extraction." Old alerts can be useful (regulatory development that's still relevant) but warrant caution — deadlines may have shifted, the underlying regulation may have been amended, and additional guidance may have been issued.

Recommendation: for alerts over a year old, the skill suggests the user check whether more recent alerts cover the same regulation.
