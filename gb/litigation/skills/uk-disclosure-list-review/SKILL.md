---
name: uk-disclosure-list-review
title: uk-disclosure-list-review
description: Use when users say "review this disclosure list", "QC disclosure", "check privilege descriptions", "inspection objections", "missing custodians", "adverse documents", or need England and Wales disclosure checked for issue coverage, gaps, privilege, redactions, and inspection risk.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/uk-disclosure-list-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
tags: [disclosure, cpr, privilege, england-and-wales, documents]
---

# uk-disclosure-list-review

## When to Use

- A user has a draft disclosure list, disclosure review export, or document schedule.
- The team needs to check whether obvious sources, custodians, adverse documents, or inspection objections are missing.
- Privilege, confidentiality, redaction, or inspection wording needs first-pass review.
- The matter is in England and Wales civil litigation.

This skill is a quality-control workflow. It does not make final privilege calls or certify disclosure compliance.

## Audience and Work Shape

Audience: England and Wales litigation associates, paralegals, and disclosure-support teams preparing a disclosure list or QC report for solicitor/partner review.

Work shape: pattern-matched review with accretive judgment elements. The skill maps coverage and flags privilege/adverse-document issues; it does not certify disclosure compliance.

## Legal Failure Modes

- Legal support, not legal advice: the report is a QC aid, not a certification of compliance or privilege.
- Privilege/confidentiality: disclosure review may itself be privileged work product. Keep outputs inside the privilege group unless a responsible lawyer approves circulation.
- Accountability: the responsible solicitor decides privilege, inspection, adverse-document significance, and whether the list is adequate.

## Access Modes

This skill works in three modes:

1. **Live source mode** - use browser, web search, MCP, API, or other configured access to retrieve rules, orders, filings, document lists, or repository exports.
2. **User-supplied source mode** - use uploaded or pasted disclosure lists, pleadings, chronologies, witness statements, search records, document schedules, rules, or orders supplied by the user.
3. **No-source mode** - prepare a disclosure QC checklist and source-request list, but do not state that coverage, privilege, inspection, or adverse-document issues exist.

If the disclosure list, source documents, search record, or governing order cannot be retrieved or supplied, mark the relevant issue `source_missing` or `verify_current_rule`. Do not infer disclosure defects from model memory.

## How It Works

### 1. Confirm disclosure context

Identify:

- Court, track, procedural stage, and applicable disclosure regime or order.
- Issues for disclosure or pleaded issues.
- Custodians, repositories, date ranges, and search terms used.
- Whether the list is standard disclosure, issue-based disclosure, specific disclosure, pre-action disclosure, or another ordered exercise.
- Whether privileged material is listed, withheld, redacted, or omitted under the relevant approach.

If the governing order or rule is unavailable, mark rule conclusions `verify_current_rule`.

### 2. Inventory the list

For each entry or category, capture:

- Document id or range.
- Date.
- Document type.
- Author, sender, recipient, or custodian where available.
- Description.
- Issue tag.
- Inspection status.
- Privilege or confidentiality claim.
- Redaction status.

Preserve original identifiers. Do not renumber in a way that breaks the user's list.

For every gap, concern, or label, cite the source that supports it: list row/document id, pleading paragraph, witness statement reference, chronology entry, correspondence thread, search record, or order term. If the source is not available, mark `source_missing`.

### 3. Check coverage

Compare the list against:

- Pleaded issues.
- Chronology.
- Key correspondence threads.
- Known custodians and repositories.
- Expected document classes, such as contracts, notices, board minutes, invoices, complaints, expert material, or meeting notes.

Flag:

- Missing time periods.
- Missing custodians.
- Missing repositories.
- One-sided productions where adverse documents would be expected.
- Documents referenced in pleadings or witness statements but absent from the list.
- Duplicates, superseded drafts, or unclear families.

### 4. Check inspection and privilege flags

For withheld, redacted, or non-inspectable documents, flag:

- No basis stated.
- Privilege description too vague.
- Business document labelled privileged because a lawyer is copied.
- Attachment treated the same as covering email without separate review.
- Confidentiality used where a confidentiality ring or redaction may be the issue.
- Redactions with no reason or scope.

Keep close privilege calls as `needs_lawyer_review`. Under-calling privilege can waive rights; over-flagging can be corrected.

### 5. Identify adverse and helpful documents

Mark documents as:

- `potentially_adverse`
- `potentially_supportive`
- `neutral`
- `unclear`

This is a triage label, not a legal conclusion. Cite the description, issue tag, or source text that caused the label.

### 6. Produce the QC report

Recommended sections:

1. Coverage summary.
2. Missing sources and custodians.
3. Documents referenced elsewhere but absent.
4. Inspection, privilege, and redaction issues.
5. Potentially adverse document flags.
6. Rule/order points needing verification.
7. Questions for the responsible lawyer or legal reviewer.

## Confidence Bands

- High: issue is directly supported by a list row, order term, pleading paragraph, or supplied document.
- Medium: issue is inferred from a pleaded issue, chronology entry, or witness reference and needs source confirmation.
- Low: source is missing, search record absent, privilege basis unclear, or inspection requires document-level review.

## Escalation

Stop and route to the responsible solicitor when the disclosure order conflicts with the list, foreign-law privilege is implicated, a custodian is also a key witness, an inspection challenge is imminent, privilege basis is uncertain on material documents, or the source/search record is too incomplete to assess coverage.

## Example

```text
Review this draft disclosure list against the pleadings and chronology. Flag missing custodians, documents referenced elsewhere but absent, weak privilege descriptions, inspection objections, and potentially adverse documents.
```

For a compact output pattern, see `examples/output.md`.
For coverage mapping, privilege/inspection flags, and adverse-document triage, see `references/disclosure-review-playbook.md`.

## Limitations

- Current CPR, Practice Direction, disclosure pilot/order terms, and court directions must be verified.
- The skill cannot know what searches were actually run unless the user provides that record.
- Privilege decisions require lawyer review.
- Adverse-document labels are investigative leads, not admissions.
