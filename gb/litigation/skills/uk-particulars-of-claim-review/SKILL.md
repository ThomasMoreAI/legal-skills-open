---
name: uk-particulars-of-claim-review
title: uk-particulars-of-claim-review
description: Use when users say "review these Particulars of Claim", "check this PoC", "pleading gaps", "CPR 16", "PD16", "limitation issue", or need England and Wales pleadings checked for elements, material facts, remedies, parties, source support, and drafting risk.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/uk-particulars-of-claim-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
tags: [particulars-of-claim, pleadings, cpr, england-and-wales, drafting]
---

# uk-particulars-of-claim-review

## When to Use

- A user has draft Particulars of Claim or a pre-action pleading outline.
- The draft needs checking before issue, service, amendment, or counsel review.
- The user wants gaps in pleaded facts, parties, remedies, limitation, or causes of action surfaced.
- The claim is in England and Wales civil litigation.

This skill reviews pleading sufficiency and structure. It does not certify merits, settle pleading strategy, sign statements of truth, or replace solicitor/counsel approval of the final pleading.

## Audience and Work Shape

Audience: England and Wales litigation solicitors, pupils/junior counsel, trainees, and paralegals preparing or checking a pleading for solicitor/counsel review.

Work shape: pattern-matched review with accretive judgment. The skill maps pleaded facts to elements and flags drafting gaps; it does not settle legal strategy or merits.

## Legal Failure Modes

- Legal support, not legal advice: the review identifies pleading gaps and verification points; it does not certify viability, merits, strategy, or limitation.
- Privilege/confidentiality: draft pleadings and advice notes are often privileged work product until filed or served. Keep review outputs internal unless a responsible lawyer approves circulation.
- Accountability: the responsible solicitor/counsel owns the final pleading, statement of truth, allegations, and relief sought.

## Access Modes

This skill works in three modes:

1. **Live source mode** - use browser, web search, MCP, API, or other configured access to retrieve public rules, protocols, authorities, filings, or source documents.
2. **User-supplied source mode** - use draft pleadings, contracts, chronology, correspondence, witness materials, counsel notes, rules, protocols, or orders supplied by the user.
3. **No-source mode** - review the draft's internal pleading structure and prepare a source/rule request list, but do not verify elements, limitation, or CPR compliance.

If governing rules, pleaded-law support, or source documents cannot be retrieved or supplied, mark the relevant item `verify_current_rule`, `verify_current_law`, or `source_missing`. Do not supply element maps or limitation conclusions from model memory as controlling law.

## How It Works

### 1. Confirm claim context

Identify:

- Court, track if known, claim value, parties, and procedural stage.
- Causes of action pleaded or intended.
- Key contracts, events, losses, and remedies.
- Limitation dates and any standstill agreements, extensions, postponement issues, or other limitation assumptions.
- Documents available to support the pleaded facts.

If the cause of action or governing rule is unclear, mark the element map `verify_law`.

### 2. Build an element map

For each cause of action, create an element checklist:

| Element | Pleaded Facts | Source | Gap |
|---|---|---|---|

Use the user's supplied law, pleadings, or research where available. If relying on general knowledge of English law, label the element list `verify_current_law` and ask for counsel confirmation before treating it as controlling.

### 3. Review pleading structure

Check whether the draft states:

- Correct parties and capacity.
- Jurisdiction, correct court/list, service basis, and allocation/track assumptions where needed.
- Material facts in chronological order.
- Contract terms, representations, duties, breaches, causation, and loss where relevant.
- Remedies sought, including interest, declarations, injunctions, delivery up, rescission, account, damages, or costs.
- Particulars for fraud, misrepresentation, professional negligence, discrimination, or other claims requiring more detail.
- Compliance with pre-action or protocol context if relevant.

Distinguish evidence from material facts. Pleadings usually need the facts relied on, not the whole proof bundle.

### 4. Surface litigation risks

Flag:

- Missing element.
- Unsupported factual allegation.
- Limitation issue.
- Wrong or missing party.
- Remedy not tied to facts.
- Overpleading evidence.
- Underparticularised allegation.
- Inconsistent chronology.
- Defined term or document mismatch.
- Allegation requiring heightened care, such as dishonesty, fraud, bad faith, conspiracy, or serious misconduct.

Do not accuse a person or company of serious wrongdoing without checking the pleaded basis and source support.

## Escalation

Stop and route to solicitor/counsel when the draft includes fraud, dishonesty, bad faith, conspiracy, professional negligence, discrimination, urgent injunctive relief, limitation uncertainty, jurisdiction/service uncertainty, or any allegation that lacks source support.

### 5. Produce the review

Recommended sections:

1. Overall pleading health.
2. Cause-of-action element maps.
3. CPR/PD16, applicable Practice Direction, pre-action protocol, and order-specific checks, with rule/source checked and date checked.
4. Limitation and party issues.
5. Remedies and interest.
6. Factual gaps and documents needed.
7. Questions for solicitor/counsel/client.

Each issue should include a paragraph reference, severity, and proposed next step.

## Confidence Bands

- High: issue is directly supported by the draft and supplied source.
- Medium: issue depends on `verify_current_law` or `verify_current_rule` but the drafting gap is visible.
- Low: source is missing, limitation facts are incomplete, or element law has not been supplied/retrieved.

## Example

```text
Review these draft Particulars of Claim. Build an element map for each pleaded claim, flag missing material facts, limitation risks, remedy gaps, and anything needing CPR/PD16 verification.
```

For a compact output pattern, see `examples/output.md`.
For element maps, sensitive allegations, and pleading gap taxonomy, see `references/pleading-review-playbook.md`.

## Limitations

- Current CPR, Practice Directions, pre-action protocols, and court orders must be verified.
- The element map depends on the pleaded cause of action and current law.
- This skill does not certify that a claim is viable or properly arguable.
- Sensitive allegations require solicitor/counsel review before filing.
