---
name: proposition-checking
title: proposition-checking
description: Use when users say "does this authority support the point", "check propositions", "fact-check this argument", "verify record support", or need cited cases, statutes, exhibits, transcripts, emails, or pleadings checked against legal or factual propositions.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/proposition-checking
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [briefs, citations, factual-record, proposition-checking, hallucination-detection]
---

# proposition-checking

## When to Use

- A brief, skeleton argument, motion, memo, advice note, or witness statement makes propositions tied to citations.
- The user wants to know whether cited cases, statutes, exhibits, or witness evidence actually support the statement made.
- A citation exists, but the concern is misuse rather than fabrication.
- The user asks whether a quotation, paraphrase, or record reference is accurate.

This skill checks support. It does not predict who wins and does not replace legal judgment.

## Audience and Work Shape

Audience: litigators, legal researchers, trainees, and paralegals checking draft arguments or evidence summaries for lawyer review.

Work shape: pattern-matched source checking with accretive judgment. The skill maps propositions to sources and grades support; it does not make the legal argument for the user.

## Legal Failure Modes

- Legal support, not legal advice: support classification is a verification aid, not a merits opinion.
- Privilege/confidentiality: drafts, exhibits, transcripts, and advice notes may be privileged or confidential; use approved environments and mark source limitations.
- Accountability: the responsible lawyer decides whether to keep, narrow, replace, or abandon the proposition.

## Access Modes

This skill works in three modes:

1. **Live source mode** - use browser, web search, MCP, API, or other configured access to retrieve authorities, statutes, rules, or public records.
2. **User-supplied source mode** - use uploaded or pasted judgments, statutes, exhibits, pleadings, transcripts, correspondence, witness statements, or record bundles.
3. **No-source mode** - extract propositions and citations, then prepare a verification queue. Do not classify support as `supported`, `unsupported`, or `contradicted`.

If the source cannot be retrieved or supplied, mark the proposition `unverified-source-unavailable`. Do not assess source support from model memory.

## How It Works

### 1. Separate propositions from citations

For each paragraph, extract:

- The proposition being asserted.
- Whether it is legal, factual, procedural, evidential, or mixed.
- The citation or record reference offered in support.
- Any direct quotation.

Do not treat a string citation as support until the proposition it supposedly supports is identified.

### 2. Retrieve or read the source

Use supplied source text first:

- Case text, statute, regulation, pleading, exhibit, transcript, witness statement, expert report, or correspondence.
- Public sources or research tools only if available and approved.

If the source cannot be retrieved, classify the proposition as `unverified`, not unsupported.

For every source used, record the source type, URL or document identifier, access date, and pinpoint. Do not assess support from model memory.

## Confidence Bands

- High: source text is available, pinpointed, and directly supports or contradicts the proposition.
- Medium: source text is available but the proposition depends on interpretation, context, admissibility, or legal characterization.
- Low: source unavailable, quote incomplete, conflicting sources, or `needs_review` / `unverified_source_unavailable`.

### 3. Compare proposition to source

Classify each proposition:

- `supported` - source directly supports the proposition.
- `partially-supported` - source supports part of it, but the draft overstates or omits a condition.
- `unsupported` - source does not support the proposition.
- `contradicted` - source cuts the other way.
- `quote-inaccurate` - direct quotation is materially wrong.
- `unverified` - source unavailable or insufficient.

For legal propositions, distinguish:

- Existence of authority.
- Accuracy of the holding.
- Applicability to the jurisdiction, court level, facts, and procedural posture.

For factual propositions, distinguish:

- The source says the fact.
- Whether admissibility, competence, hearsay, privilege, or procedural use appears to require lawyer review under the governing rules.
- The fact is disputed elsewhere in the supplied record.

### 4. Report with traceability

Output:

| Field | Meaning |
|---|---|
| `paragraph` | source paragraph or location |
| `proposition` | claim being checked |
| `citation` | authority or record cite |
| `status` | support classification |
| `source_location` | page, paragraph, Bates, section, exhibit, or other pinpoint |
| `source_excerpt` | exact supporting or contradicting text |
| `problem` | overstatement, mismatch, missing source, etc. |
| `suggested_fix` | narrow, replace cite, add source, or remove |

Use short excerpts. The goal is fast lawyer verification, not a replacement brief.

### 5. Identify dependency risk

After checking individual propositions, summarize:

- Arguments that depend on unsupported propositions.
- Citations repeatedly misused for the same point.
- Facts contradicted by the record.
- Authorities that exist but are cited for the wrong doctrine.
- Unverified sources that need manual research.

## Escalation

Stop and route to the responsible lawyer when a key proposition is contradicted, an authority appears fabricated, a quote is materially inaccurate, admissibility/privilege controls the answer, or the user asks for merits advice rather than source support.

## Example

```text
Check whether each cited authority in this draft actually supports the proposition it is cited for. Separate citation existence problems from misuse problems.
```

For a compact output pattern, see `examples/output.md`.
For proposition types, support states, and argument dependency mapping, see `references/proposition-checking-model.md`.

## Limitations

- A source may support a proposition legally only after jurisdiction-specific research.
- The skill cannot assess undisclosed record material.
- `unverified` is not a merits conclusion.
- Admissibility and evidential competence concerns should be flagged for lawyer review unless the user supplies the governing rule and enough context to apply it.
- Privileged or sealed materials require an approved processing environment.
