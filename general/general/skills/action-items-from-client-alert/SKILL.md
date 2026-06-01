---
name: action-items-from-client-alert
title: Action Items from Client Alert
description: Use when the user provides a client alert, regulatory bulletin, law firm memo, or similar legal update and wants the time-sensitive action items, deadlines, and obligations extracted into a checklist organized by deadline. Distinguishes mandatory action items (effective dates of new requirements) from recommended action items (best practices) and informational items (context only). Produces a brief context summary plus deadline-organized checklist with citations to the source alert.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/action-items-from-client-alert
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Action Items from Client Alert

Extract time-sensitive action items, deadlines, and obligations from a client alert, regulatory bulletin, law firm memo, or similar legal update. Produce a deadline-organized checklist that an in-house lawyer can act on without re-reading the source document.

The skill is operational, not analytical. Action items are stated at the level of granularity the alert supports — typically high-level ("comply with new disclosure requirement by [date]"), not implementation-level ("update privacy policy section 4.2 by [date]"). The user knows their organization better than the skill does; the skill provides the trigger and deadline, not the implementation.

**Audience.** In-house counsel or compliance analyst with regulatory-intake experience who can audit the extracted checklist against the source alert. Not suitable for unsupervised non-lawyer use; the output is a reviewed working draft, not a deliverable to non-legal stakeholders without lawyer sign-off. Outside counsel and smaller orgs without an in-house team structure should treat functional-owner suggestions ("Legal", "Compliance", "IT") as placeholders and reassign per their own staffing.

## When this skill applies

Apply when the user provides a legal-update document and asks for action items, deadlines, or obligations to be extracted. Typical inputs:

- **Law firm client alerts** ("Client Alert: New SEC Cybersecurity Disclosure Rules Take Effect").
- **Regulatory bulletins** (FTC enforcement priorities; SEC staff guidance; agency Q&A documents).
- **Law firm memos** on regulatory developments or new statutes.
- **Industry association updates** distilling regulatory changes for members.
- **Internal compliance bulletins** if structured similarly to external alerts.

Do not apply when:

- **The document is the underlying regulation, statute, or rule itself.** Regulations are dense and structured for legal interpretation, not for action-item extraction. Recommend the user start with a client alert summarizing the regulation, or escalate to legal counsel for direct regulatory analysis.
- **The document is a court opinion or judicial decision.** Different shape; would warrant a case-summary skill (deferred enhancement candidate).
- **The document is a private communication or strategy memo.** Different shape; the skill is calibrated for published / shared alerts.
- **The user wants an analysis of the legal change rather than action items.** Action-item extraction is operational. If the user wants to understand the substantive legal change, recommend reading the alert directly or engaging counsel.
- **The document is too vague to extract specific actions.** Some alerts describe regulatory developments without imposing or describing specific requirements. The skill notes this and produces a "no specific action items extractable" output rather than fabricating actions.

## Inputs

The skill requires the document. Optional inputs filter and prioritize the extraction:

- **`organization_context`** affects applicability. An alert about EU AI Act obligations is highly relevant to an EU-based AI vendor and largely irrelevant to a US-only consumer-goods retailer. The skill uses the organization context to flag items as applicable, conditionally applicable, or not applicable.
- **`relevant_business_areas`** filters extraction. If the user is focused on data privacy and the alert covers privacy plus employment, the privacy items get full extraction and employment items are noted briefly with a reference to re-run for that focus.
- **`applicable_jurisdictions`** affects which items are surfaced. An alert covering federal plus multiple states' laws produces different relevance for users in different states.
- **`alert_date`** affects deadline assessment. Some alerts arrive after some deadlines have passed; the skill should flag past-deadline items separately from forward-looking ones.

When optional inputs are not provided, the skill extracts all items from the alert and flags applicability uncertainty.

## Workflow

The workflow has four steps.

### Step 1: Document orientation

Before extraction:

- Confirm the document is a client alert or similar update. If it's something else (the regulation itself, a court opinion, internal correspondence), stop and route the user.
- Identify the alert's date. If not stated, ask the user (the `alert_date` input) before proceeding — deadline assessment depends on the alert date.
- Identify the alert's subject matter (regulatory regime, agency, statute, jurisdiction).
- Identify the alert's structure: is it organized by topic, by deadline, by stakeholder? Different structures affect extraction approach.
- Note any references to the underlying regulation, prior alerts, or related materials.

### Step 2: Item extraction

Walk through the document and extract every item that meets one of these criteria:

1. **Mandatory action item:** something the user (or organizations like the user) is required to do, with a deadline. Source: the alert describes a new requirement, a compliance deadline, an effective date, a filing date, or a similar legal obligation.
2. **Recommended action item:** something the alert recommends as best practice without it being legally required. Source: the alert uses language like "should consider," "best practice," "we recommend," "prudent companies will."
3. **Informational item:** context that affects the user's understanding of the regulatory landscape but doesn't require specific action. Source: the alert describes background, agency posture, enforcement trends, or related developments without imposing requirements.
4. **Conditional action item:** action required only under specific circumstances (e.g., "if you process EU residents' data, you must..."). The skill flags the condition and the action.

For each item, capture:
- **What:** the action or obligation, stated in plain language.
- **By when:** the deadline or effective date, with explicit date if available.
- **Who within the organization:** typical functional owner if the alert suggests one (Legal, Compliance, IT, HR, etc.); otherwise marked "Owner: TBD."
- **Why / source:** the underlying legal basis (statute, regulation, agency guidance), with citation to the alert's section.
- **Conditions / applicability:** whether the item applies to all organizations or only specific ones.
- **Extraction confidence:** tag each item per the linguistic patterns graded in `reference/extraction_patterns.md`.
  - **High** — the alert states the action and deadline explicitly with mandatory language ("must", "shall", "is required to", a specified effective/compliance date).
  - **Medium** — the alert implies the action or deadline but does not state it directly (e.g., "the rule takes effect for fiscal years ending on or after [date]" requires deriving the filing date from the user's fiscal year).
  - **Low** — the alert is ambiguous, conditional on facts not in the document, or uses hedged language ("companies may need to consider…"). Item is extracted but explicitly flagged for lawyer judgment.
- **Source-fidelity tag:** mark each line in the item as either **[Extracted]** — copied or directly paraphrased from the alert with section citation — or **[Inferred]** — derived by the skill (e.g., a specific filing deadline computed from an effective date and an assumed filer class, or a functional owner inferred from the topic). Inferred lines must state the assumption and ask the reviewer to confirm.

### Step 3: Apply filters and applicability flags

For each extracted item, assess applicability based on optional inputs:

- **Applicable** — the item applies to the user's organization based on `organization_context`, `relevant_business_areas`, and `applicable_jurisdictions`.
- **Conditionally applicable** — the item applies if a specific condition is met (the user has EU users; processes children's data; engages in cross-border data transfers).
- **Not applicable** — the item does not apply to the user based on the inputs provided.
- **Applicability uncertain** — the user's optional inputs are not specific enough to assess; the skill notes the item and flags applicability for user review.

If `organization_context` is not provided, all items are flagged "applicability uncertain" and the user must assess applicability themselves.

### Step 4: Organize by deadline and produce checklist

Sort items by deadline, with separate sections for:

- **Past-deadline items** — deadlines that have already passed at the time of the review. May still warrant action (compliance lookback; remediation; ongoing obligations).
- **Imminent items** — deadlines within 30 days of the review.
- **Near-term items** — deadlines 30 days to 6 months out.
- **Future items** — deadlines beyond 6 months.
- **Ongoing obligations** — items without specific deadlines that represent continuing requirements.
- **Recommended (no deadline)** — best-practice items the alert recommends without specific deadline.
- **Informational only** — items that don't require action.

## Output

Produce the report in markdown with this structure:

```markdown
# Action Items from Client Alert: [Alert title or subject]

**Source document:** [alert title and date]
**Alert date:** [date]
**Organization context:** [user-provided, or "not specified"]
**Relevant business areas:** [user-provided, or "all"]
**Applicable jurisdictions:** [user-provided, or "not specified"]

## Context summary

[2-4 sentences. What is the alert about? What regulatory development triggered it? Why does it matter? This is to orient the user without requiring them to read the alert; the action items are below.]

## Mandatory action items

Each item lists, in addition to the substantive fields: **Extraction confidence** (High / Medium / Low) and a per-line **[Extracted]** vs **[Inferred]** tag. Inferred lines state the assumption and request reviewer confirmation.

### Past-deadline items
[If any. Each with: what, deadline (passed), source citation, applicability, recommended remediation, extraction confidence, per-line Extracted/Inferred tags.]

### Imminent (within 30 days)
[Each with: what, deadline (specific date), owner, source citation, applicability, extraction confidence, per-line Extracted/Inferred tags.]

### Near-term (30 days to 6 months)
[Each with: what, deadline, owner, source citation, applicability, extraction confidence, per-line Extracted/Inferred tags.]

### Future (beyond 6 months)
[Each with: what, deadline, owner, source citation, applicability, extraction confidence, per-line Extracted/Inferred tags.]

### Ongoing obligations
[Each with: what, periodicity if applicable, owner, source citation, applicability, extraction confidence, per-line Extracted/Inferred tags.]

## Recommended action items (no specific deadline)

[Each with: what, why recommended, owner, source citation, applicability, extraction confidence, per-line Extracted/Inferred tags.]

## Informational items

[Items the alert flags as context. Brief — usually a bulleted list of 2-5 items that affect the user's understanding without requiring action.]

## Items where applicability is unclear

[Items the skill could not assess for applicability based on the inputs provided. The user must assess these themselves.]

## Items not applicable to user's organization

[If `organization_context` was provided and any items were assessed as not applicable. Brief — these are noted for completeness so the user knows nothing was missed.]

## Source references and follow-ups

[List of: the underlying regulation/statute/guidance referenced in the alert; any prior alerts referenced; suggested follow-up actions (e.g., "obtain the underlying regulation for the legal team's review file"). Brief.]

## Notes on this extraction

[Brief — typically a sentence or two. If the alert was vague, if extraction required interpretation, if items were uncertain — note here. If everything was clear, this section can be a single sentence: "Extraction was straightforward; all items have clear deadlines and applicability."]
```

The report should match the alert's substance, not pad. A brief alert (1-2 pages, a few action items) produces a brief report. A comprehensive alert (10+ pages, dozens of action items across multiple regimes) produces a long report. Don't pad short alerts; don't truncate substantial ones.

## Edge cases and refusals

- **Alert is too vague to extract specific actions.** Produce the context summary and note in "Notes on this extraction" that the alert is informational rather than actionable. Recommend the user obtain a more specific compliance roadmap from outside counsel if the regulatory development warrants action.
- **Alert covers a regulation that's been updated since the alert was published.** If the alert is dated and the user notes the deadline has shifted, the skill should flag this. Without notification, the skill cannot detect this.
- **Alert is conditional on facts the skill cannot assess** ("if your company has more than 250 employees..."). The skill extracts the item and flags it as conditionally applicable, with the condition explicit.
- **Alert covers many jurisdictions but the user is in only one.** The skill filters by `applicable_jurisdictions` if provided; if not provided, all items are extracted with jurisdiction noted and applicability flagged uncertain.
- **Alert is duplicative of a prior alert (same regulation re-summarized).** The skill extracts items as if the alert were standalone; the user is responsible for identifying duplication with prior compliance work.
- **Action item the alert recommends seems impractical, illegal, or in conflict with other obligations.** The skill extracts the item as the alert states it but notes the concern; this is a flag for the user, not a refusal to extract.

## What this skill does not do

- **Substantive analysis of the regulatory development.** The skill extracts what the alert says; it does not opine on whether the alert is correct, whether the regulatory development is well-founded, or whether the action items are sufficient.
- **Implementation guidance.** Action items are at the level the alert supports. The user knows their organization; the skill does not.
- **Compliance certification.** Extracting an action item is not the same as confirming compliance.
- **Enforcement-risk assessment.** The skill does not opine on whether non-compliance is likely to be detected or enforced.
- **Multi-document synthesis.** The skill operates on one alert at a time. Synthesizing across multiple alerts (e.g., comparing different law firms' takes on the same regulatory development) is out of scope; deferred enhancement candidate.
- **Legal advice.** The skill produces an extracted checklist; legal advice on the user's specific circumstances is outside scope.

## Reference materials

- `reference/extraction_patterns.md` — patterns for identifying action items, deadlines, and applicability conditions in alert text.
- `reference/deadline_calibration.md` — guidance on deadline categorization (past-deadline, imminent, near-term, future) and edge cases.
- `examples/example_clear_alert.md` — worked example: well-structured alert with clear deadlines.
- `examples/example_vague_alert.md` — worked example: vague alert that produces few extractable items.
- `examples/example_multi_jurisdiction.md` — worked example: alert covering multiple jurisdictions, demonstrating jurisdiction-filtering.

## QA Remediation (LegalQuants, 2026-05)

LegalQuants added a targeted remediation pass to address SOME CONCERN gaps surfaced in QA: reconciled the frontmatter `author` field with the registry (Kevin Keller, per README); added an explicit Audience line (in-house counsel / compliance analyst with regulatory-intake experience); surfaced per-item extraction-confidence bands (High / Medium / Low) tied to the linguistic patterns already graded in `reference/extraction_patterns.md`; and introduced per-line **[Extracted]** vs **[Inferred]** source-fidelity tagging so reviewers can distinguish text copied from the alert from outputs the skill computed (e.g., filing dates derived from effective dates and assumed filer class). Original technical content — workflow steps, applicability flags, edge cases, refusals, and non-goals — is unchanged.
