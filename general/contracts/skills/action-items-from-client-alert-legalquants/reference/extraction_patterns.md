# Extraction Patterns

This reference helps the skill identify action items, deadlines, and applicability conditions in alert text. Pattern-matching is heuristic, not exhaustive — alerts vary in style, structure, and explicitness.

## Identifying mandatory action items

Mandatory action items are things the user (or organizations like the user) is required to do. Linguistic patterns that signal mandatory items:

- **"Must," "shall," "required to," "obligated to"** — strong mandate language. High confidence.
- **"By [date], [organizations] [must / will need to] ..."** — mandate plus deadline. High confidence.
- **"Effective [date], [provision] applies to ..."** — new requirement with effective date. High confidence; the action is to comply by the effective date.
- **"Deadline:" or "Effective date:"** — alerts often call out deadlines explicitly. High confidence.
- **"Filing requirement," "disclosure requirement," "notification requirement"** — references to specific regulatory mechanisms. High confidence.
- **"In order to comply with [regulation], [organizations] need to ..."** — compliance language. High confidence.
- **"[Statute/regulation] requires ..."** — direct reference to legal requirement. High confidence.

Lower-confidence patterns that may still be mandatory:

- **"Companies will need to consider ..."** — soft mandate language. Read the surrounding text for whether the requirement is mandatory or recommended.
- **"Affected entities should ensure ..."** — could be mandate or recommendation; check the underlying source.
- **"The new rule means ..."** — implication of action; extract the implied action.

When the alert is ambiguous between mandatory and recommended, default to **mandatory** if the alert references a statute, regulation, or rule that has the force of law; default to **recommended** if the alert describes guidance, best practice, or industry expectation without legal force.

## Identifying recommended action items

Recommended action items are best practices the alert suggests without legal compulsion. Linguistic patterns:

- **"Should consider," "may want to," "prudent companies will," "it is advisable to"** — recommendation language. High confidence.
- **"Best practice is to," "industry practice has moved toward"** — best-practice framing. High confidence.
- **"We recommend," "the law firm recommends," "compliance professionals advise"** — explicit recommendation. High confidence.
- **"To prepare for [regulatory development], companies might ..."** — preparation suggestion. High confidence.

Recommendations sometimes shade into mandates as enforcement matures. An alert from 2023 about a 2025 regulation might frame items as recommended; in 2026, the same items are likely mandatory. The skill extracts as the alert states; the user assesses currency.

## Identifying informational items

Informational items provide context without requiring action. Linguistic patterns:

- **"In a recent enforcement action, [agency] ..."** — enforcement reporting; useful context.
- **"The agency's posture toward [topic] has shifted ..."** — agency-trends commentary; useful context.
- **"This is consistent with [trend]" / "This follows [prior development]"** — connective tissue; useful context.
- **"For background on [related topic], see ..."** — pure background.

Informational items are the section to be most aggressive about pruning. Many alerts have substantial informational content that doesn't translate to action; the user can read the alert if they want context. The action-item extraction should focus on action items.

## Identifying deadlines

Deadlines come in several forms:

### Specific dates

- **"By March 31, 2026"** — clear deadline.
- **"On or before [date]"** — clear deadline.
- **"Effective [date]"** — effective date is typically also the compliance deadline.
- **"Compliance deadline: [date]"** — explicit deadline label.

### Relative deadlines

- **"Within 30 days of [trigger event]"** — relative; capture the trigger and duration.
- **"No later than 6 months after [event]"** — relative; capture trigger and duration.
- **"Annually" / "Quarterly" / "Within 30 days of each quarter end"** — periodic obligations.

### Phased deadlines

- **"Effective for fiscal years beginning after [date]"** — capture the date and the trigger condition.
- **"Phased implementation: [milestone 1] by [date]; [milestone 2] by [date]"** — multiple deadlines for staged compliance.
- **"Different deadlines for different organization sizes"** — capture each tier's deadline.

### Pending deadlines

- **"Final rule expected by [date]"** — the rule has a target date but is not final.
- **"Comments due [date]"** — comment deadline rather than compliance deadline.
- **"Effective date to be determined"** — no deadline yet; informational.

For relative or pending deadlines, the skill captures the structure (relative to what; pending what) rather than producing a calendar date.

## Identifying applicability conditions

Action items often apply only to specific organizations, transactions, or circumstances. Linguistic patterns for conditions:

- **"For organizations [meeting threshold] ..."** — size-based applicability (revenue, headcount, market cap).
- **"For entities that [conduct activity] ..."** — activity-based applicability.
- **"For companies with operations in [jurisdiction] ..."** — geographic applicability.
- **"If you have [specific data type] ..."** — data-type applicability.
- **"For publicly-traded companies" / "for SEC registrants"** — entity-type applicability.
- **"In transactions involving [counterparty type]"** — transaction-type applicability.

Capture the condition in the action-item entry. Where the user's `organization_context` provides the relevant facts, the skill can assess applicability; where the user has not provided facts, the skill flags applicability uncertainty.

## Extracting "owner" / functional ownership

The skill suggests typical functional owners when the alert provides hints. Common functional ownership patterns:

- **Privacy / data protection** — Privacy Officer, DPO, Legal (privacy team), CISO depending on the issue.
- **Securities / disclosure** — CFO, Legal (corporate / securities), Investor Relations.
- **Employment / labor** — HR, Legal (employment).
- **Tax** — Tax / Finance.
- **Antitrust / competition** — Legal (regulatory).
- **Anti-corruption** — Compliance, Legal, Internal Audit.
- **Cybersecurity** — CISO, IT Security, Legal (privacy, regulatory).
- **Environmental / ESG** — Sustainability, Legal (environmental), Operations.
- **Consumer protection** — Legal (regulatory), Marketing.

If the alert doesn't specify and the area is ambiguous, mark "Owner: TBD" rather than guessing.

## Items not to extract

Some content in alerts should not be extracted as action items:

- **Marketing content** ("Please contact our team for a deeper discussion") — extracted as informational only if relevant.
- **Generic disclaimers** ("This alert is for general information only and is not legal advice") — not extracted.
- **Bibliographic references** ("See our prior alert dated [date]" pointing to an unprovided document) — captured under "Source references and follow-ups" rather than as actions.
- **Speculation about future developments** ("The agency may issue further guidance in 2026") — informational only; not actionable until further guidance arrives.

## Multi-step actions

Some action items have natural sub-steps. The skill captures the top-level item and notes natural sub-steps where they're explicit in the alert; it does not invent sub-steps the alert doesn't support.

Example:
- **Alert says:** "Companies must (a) update privacy policies; (b) train sales staff; and (c) confirm vendor contracts align by [date]."
- **Skill extracts:** the top-level item ("comply with new disclosure rule by [date]") plus the three sub-steps as the alert listed them.
- **Skill does not extract:** additional sub-steps the alert didn't mention (e.g., "update CRM templates," "review marketing materials") even if those would be obvious implementation work.

The user knows implementation; the skill provides the trigger.

## When extraction requires interpretation

Some alerts require interpretation to extract. Examples:

- **Implicit deadlines** — "The new rule applies to fiscal years beginning after [date]" → the deadline is the start of the next applicable fiscal year, which depends on the user's fiscal year end. The skill notes the implicit calculation.
- **Conditional triggers** — "If you receive a Subject Access Request..." → the deadline is "30 days after the request is received," which depends on when (and whether) requests come in. The skill notes the conditional structure.
- **Aggregate effects** — "The combined effect of these changes is that companies must..." → the skill extracts the aggregate effect as a single action item rather than separately extracting each precursor.

When extraction requires meaningful interpretation, the skill notes it in "Notes on this extraction" so the user knows the extraction is not purely mechanical.
