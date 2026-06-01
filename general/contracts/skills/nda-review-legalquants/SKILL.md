---
name: nda-review-legalquants
title: NDA Review
description: Use when the user uploads or pastes a non-disclosure agreement and asks for review, redline, risk assessment, or a recommendation on whether to sign. Identifies missing standard protections, one-sided or unusual provisions, and operational issues; produces a structured report with severity ratings and citations to specific clauses, calibrated to the user's perspective (discloser, recipient, or mutual).
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-ai/tree/main/skills/nda-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# NDA Review

Conduct a structured review of a non-disclosure agreement from the user's stated perspective and produce a report that an in-house lawyer can act on without redoing the analysis. The output is a draft for human review, not a final word; treat it accordingly.

## When this skill applies

Apply when the user provides an NDA (sometimes called a confidentiality agreement, CDA, or confidential disclosure agreement) and asks for review, redline guidance, risk assessment, or a recommendation. The user's perspective — discloser, recipient, or mutual — fundamentally changes the analysis; require it before proceeding if not supplied.

Do not apply this skill to:

- Confidentiality clauses inside larger agreements (MSAs, employment agreements, settlement agreements). Those clauses interact with the surrounding agreement; isolated review misleads. Tell the user a separate review of the parent agreement is needed.
- Documents that are not NDAs, even if they touch on confidentiality (data processing agreements, security addenda, BAAs). Refer the user to the appropriate skill.
- NDAs in employment contexts (employee confidentiality agreements, separation agreements with NDA components). These have employment-law overlays this skill does not cover.

## Inputs

The skill requires the NDA itself and the user's perspective. If perspective is not provided, ask:

> "Before I review, which side are you on? Discloser (you're sharing information and want strong protections on the recipient), recipient (you're receiving information and want narrow obligations on yourself), or mutual (both parties are exchanging information and you want balanced, symmetric terms)?"

If the user describes a situation that does not cleanly fit one of these (e.g., "we're sharing information but only a small amount; mostly we're receiving"), default to the perspective covering the larger exposure and note the asymmetry in the report. For mostly-receiving-with-some-sharing, treat as recipient and add a note about the discloser-side exposure.

Optional inputs (jurisdiction, deal_type, prior_agreements, standard_positions) refine the analysis if provided. Do not block on them.

The `deal_type` input materially affects severity calibration. The same provision can be material in one deal context and minor in another. Examples:

- A non-solicit clause is **material in vendor_evaluation or customer_engagement** (the parties are not contemplating organizational integration; non-solicit is unbargained-for restraint), and **minor-to-acceptable in ma_diligence or partnership** (organizational integration is on the table; non-solicit is part of standard deal-protection package).
- A standstill provision is **material/critical outside ma_diligence** (the parties are not contemplating an acquisition; standstill restricts conduct unrelated to the confidentiality purpose) and **standard-and-acceptable in ma_diligence** (it serves a legitimate deal-protection function).
- IP assignment of feedback is **critical in vendor_evaluation** (recipient gives up IP rights to evaluate a product) and **less unusual in partnership** (where reciprocal IP exchange may be in scope, though still warrants scrutiny).
- A 5-year confidentiality term is **material in general_commercial** (longer than standard) and **minor-to-standard in ma_diligence** (M&A-grade information warrants longer protection).

When `deal_type` is not provided, default to **general_commercial** and note in the report that severity calibration assumed general commercial context; calibration may differ if a specific deal type applies.

The `prior_agreements` input drives Pass 4's conflict-with-prior-agreements analysis. When provided, examine the document for:

- Express references to the named prior agreements (and whether the references are accurate).
- Integration / entire-agreement clauses that would extinguish protections in the prior agreement.
- Provisions that conflict with terms the user mentioned in the prior agreement.

When `prior_agreements` is not provided, do not speculate about prior agreements; the conflict-with-prior-agreements analysis is skipped.

## Workflow

Produce the review in five passes. Do them in this order — earlier passes inform later ones.

### Pass 1: Document orientation

Before substantive review, read the document and orient:

- Is this actually an NDA, or a different agreement type? If it's not an NDA, stop and tell the user.
- Is it mutual, unilateral toward discloser, or unilateral toward recipient? Compare this to the user's stated perspective; flag any mismatch (e.g., user says "we're recipient" but document is unilateral toward the *other* party — meaning the user has obligations the user thinks the other side has).
- Note governing law, jurisdiction, and term length at a glance.
- Estimate document length and complexity. NDAs over ~5 pages typically have non-standard provisions worth flagging on length alone.

### Pass 2: Standard-protection check

Walk through the standard NDA checklist in `reference/issue_checklist.md`. For each item, determine:

- **Present and standard:** the document has this clause and it falls within the normal range.
- **Present but unusual:** the document addresses this issue but with non-standard scope, severity, or carveouts.
- **Missing:** the document does not address this issue.
- **N/A:** this issue does not apply given the document type, perspective, or business context.

The standard checklist covers: definition of confidential information, exclusions from confidentiality, permitted uses, permitted disclosures (employees, advisors, legal compulsion), term and duration of confidentiality obligations, return/destruction of materials, residuals, no-license language, equitable remedies and injunctive relief, governing law and venue, assignment, integration and amendment, and notice requirements.

### Pass 3: Asymmetry and one-sidedness check

Specifically examine the document for asymmetry against the user's perspective. Per `reference/perspective_lens.md`, certain provisions read very differently from each side:

- **Discloser perspective:** weak definitions of confidential information, broad exclusions, short terms, narrow injunctive relief, weak return/destruction, broad permitted disclosures, residuals clauses — all favor the recipient and erode discloser protection.
- **Recipient perspective:** broad definitions, narrow exclusions, long terms (especially perpetual obligations on trade secrets in the wrong jurisdictions), broad injunctive relief, harsh return/destruction with certifications, narrow permitted disclosures (especially blocking advisor disclosure), liquidated damages — all expand recipient obligations.
- **Mutual perspective:** check that obligations and protections actually run symmetrically. Mutual NDAs that look mutual but have asymmetric exclusions, term, or remedies are a common drafting move worth flagging.

### Pass 4: Operational and red-flag check

Look for provisions that create operational risk regardless of perspective:

- **Non-solicitation clauses inside NDAs.** Common in unilateral-toward-discloser drafts. Often unenforceable in California; problematic in other states. Flag whenever present.
- **Non-competition clauses.** Same flagging — and stronger enforceability concerns. Flag as critical whenever present in an NDA outside an M&A context.
- **Non-circumvention clauses.** Common in deal-broker contexts; often vague enough to create operational restrictions the user did not bargain for.
- **No-hire clauses.** Increasingly disfavored in some jurisdictions; flag whenever present.
- **IP assignment language** purporting to assign work product or feedback. Should not be in an NDA; flag as material.
- **Most-favored-nation clauses** on confidentiality terms. Unusual; flag for context.
- **Consequential / liquidated damages** for breach. Flag.
- **Indemnification provisions.** Should not be in a standard NDA; flag as material.
- **Audit rights** (recipient permitting discloser to audit recipient's compliance). Common in regulated-data NDAs; flag for proportionality.
- **Public-statement restrictions** ("non-disparagement"). Out of scope for an NDA; flag.
- **Broad publicity restrictions** ("you may not announce that we are talking"). Common; flag for whether the restriction is mutual and reasonable.
- **Survival provisions** that cause obligations to outlive the rest of the agreement. Standard for confidentiality, but check what *else* survives.
- **Conflicts with existing agreements.** If the user provided a `prior_agreements` input, examine the document for references to those agreements, integration clauses that would extinguish prior protections, and provisions that conflict with terms in the prior agreements. Flag any potential conflicts. If `prior_agreements` was not provided, this check is skipped.

See `reference/red_flags.md` for the full list.

### Pass 5: Produce the report

The report has a fixed structure (specified in the Output section). Populate it with the findings from the prior passes. Calibrate severity using the rubric in `reference/severity_rubric.md`. Cite specific section/clause numbers for every finding so the user can navigate the document.

## Output

Produce the report in markdown with this exact structure:

```markdown
# NDA Review: [Document name or counterparty]

**Perspective:** [discloser | recipient | mutual]
**Document type:** [Mutual NDA | Unilateral NDA toward discloser | Unilateral NDA toward recipient]
**Governing law:** [jurisdiction or "not specified"]
**Term:** [duration or "perpetual" or "not specified"]

## Bottom line

[Two to four sentences. State the overall posture of the document toward the user's perspective (favorable, balanced, unfavorable, materially unfavorable). State whether it is signable as-is, signable with minor edits, requires negotiation, or should be rejected. Identify the single most important issue.]

## Critical issues

[Issues rated "critical" per the severity rubric. Each issue has its own subsection with: clause reference, what the document says, why it's a problem from the user's perspective, suggested redline language. Omit this section if there are no critical issues; do not pad.]

## Material issues

[Issues rated "material." Same subsection structure as Critical.]

## Minor issues and observations

[Issues rated "minor" or items that are present-and-standard but worth noting. May be a bulleted list rather than full subsections.]

## Missing standard protections

[Standard NDA elements that are absent and should be added. Each with suggested language or a reference to where to find it.]

## Operational red flags

[Items from Pass 4 — non-solicits, non-competes, IP assignments, indemnities, etc. Flagged whether or not they are objectionable; the user makes the business judgment.]

## Recommended next steps

[A short bulleted list. What should the user do next? Common options: sign as-is, sign with the redlines proposed above, send back with negotiation, escalate to outside counsel for a specific issue, decline to proceed.]

## Items requiring human judgment

[A short list of items the skill cannot resolve and that need the user's business judgment or jurisdiction-specific expertise. Examples: enforceability of a non-solicit in the user's actual jurisdiction; whether a particular use case falls within "permitted uses"; whether the business context warrants accepting an unfavorable term.]
```

If the perspective is **mutual**, the asymmetry analysis lives in the appropriate severity section (critical / material / minor) depending on how skewed the document is. Do not create a separate "Asymmetries" section — that buries severity signal.

If the document is signable as-is or with only minor changes, the report should be short. Do not pad. A two-page report on a clean NDA is correctly two pages, not five.

## Edge cases and refusals

- **Document is not an NDA.** Stop and tell the user. Suggest the appropriate skill if obvious (e.g., "this is a Data Processing Agreement; use the DPA Checklist Review skill").
- **Document is too short or fragmentary** (e.g., only a confidentiality clause excerpted from a larger agreement). Tell the user the review needs the full document.
- **Document is in a language the user did not flag.** If the document is not in English, flag and ask the user to confirm the language and whether translation is needed before proceeding.
- **Document contains unusual provisions outside the skill's coverage** (e.g., complex residuals language, foreign-law-specific clauses, escrow arrangements). Flag these in the "Items requiring human judgment" section rather than producing potentially-wrong analysis.
- **Perspective is "mutual" but the document is clearly unilateral.** Flag the mismatch. The user may have misidentified the document; ask before proceeding.
- **The user provides standard positions that conflict with the document.** Use the user's positions as the benchmark, not generic standards. The user knows their organization's appetite better than a generic NDA review.
- **Critical issues that require legal advice the skill cannot give.** For example, "this clause may be unenforceable in California" — note that this is a question for the user's judgment and, if material, suggest escalation. Never give a definitive enforceability opinion.

## What this skill does not do

- Give a final legal opinion. The output is a draft for human review.
- Predict enforceability with confidence. Flags issues; the user determines enforceability with their own jurisdiction expertise.
- Negotiate. Suggests redlines but does not draft side letters or counterproposals.
- Replace counsel for unusual deal structures (M&A NDAs, government NDAs, classified-information NDAs). Recommend escalation.

## Reference materials

- `reference/issue_checklist.md` — the standard NDA element checklist used in Pass 2.
- `reference/perspective_lens.md` — how to read each provision through discloser, recipient, or mutual eyes.
- `reference/red_flags.md` — the full operational and red-flag list used in Pass 4.
- `reference/severity_rubric.md` — the rubric for rating issues critical, material, minor.
- `examples/example_unilateral_recipient.md` — worked example: receiving party reviewing a unilateral NDA from a vendor.
- `examples/example_mutual.md` — worked example: mutual NDA in an early-stage acquisition discussion.
