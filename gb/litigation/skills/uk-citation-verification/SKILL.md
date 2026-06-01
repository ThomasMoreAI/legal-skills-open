---
name: uk-citation-verification
title: uk-citation-verification
description: Use when users say "verify these UK citations", "check this skeleton for hallucinated cases", "BAILII/FCL check", "is this EWCA citation real", or need UK authorities, paragraph references, case names, or quotations checked against public sources.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/uk-citation-verification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
tags: [citation, uk, bailii, find-case-law, hallucination-detection]
---

# uk-citation-verification

## When to Use

- A draft cites UK cases and needs a pre-filing citation audit.
- AI-generated legal text may contain hallucinated authorities.
- A user wants to verify neutral citations, party names, report citations, or quoted passages.
- A cited proposition needs to be tied back to the authority actually retrieved.

This skill verifies existence and citation integrity. It does not decide the merits of the case.

For Scotland, Northern Ireland, tribunal-specific, or devolved materials, identify the applicable official source before treating the citation as verified.

## Audience and Work Shape

Audience: UK litigators, trainees, paralegals, and legal researchers checking draft legal text before lawyer review or filing.

Work shape: pattern-matched verification. The skill resolves and classifies citations; it does not decide whether the authority supports a proposition.

## Legal Failure Modes

- Legal support, not legal advice: citation existence and integrity checks do not decide merits or legal propositions.
- Privilege/confidentiality: drafts may be privileged or confidential. Use only approved environments or user-supplied/public sources; do not send client drafts to unapproved services.
- Accountability: unresolved, ambiguous, traditional, or lower-confidence authorities remain for lawyer/researcher review.

## Access Modes

This skill works in three modes:

1. **Live source mode** - use browser, web search, MCP, API, or other configured access to retrieve public authority sources.
2. **User-supplied source mode** - use judgment PDFs, HTML, text, screenshots, exports, URLs, or pasted source material supplied by the user.
3. **No-source mode** - extract citations and prepare a verification queue, but do not mark citations as verified.

If the source cannot be retrieved or supplied, do not verify from model memory. Mark the item `unverified-source-unavailable` and ask for a source, URL, export, or connector.

## How It Works

### 1. Extract citations

Parse the text for:

- Neutral citations, such as `[2024] UKSC 1`, `[2023] EWCA Civ 10`, `[2022] EWHC 123 (KB)`.
- Traditional law report citations where present.
- Case names adjacent to citations.
- Paragraph references and quoted passages tied to a citation.

Keep each citation's location in the source document.

### 2. Resolve against public sources

Check each authority using available sources, in this order where possible:

1. The National Archives Find Case Law.
2. BAILII.
3. Court or tribunal source pages.
4. Other sources may be used only to locate leads.

Do not classify an authority as `verified` from search snippets, summaries, commentary, unofficial mirrors, or model memory. If only unofficial material is available, classify it as `unverified-source-unavailable` or `lower-confidence-lead`. If no live source, database export, or user-supplied authority text is available, stop verification and say what access is missing.

### 3. Classify each citation

Use these statuses:

- `verified` - citation and case identity match a retrieved source.
- `case-name-mismatch` - citation exists but party names differ materially.
- `citation-not-found` - search found no matching authority.
- `paragraph-not-found` - authority exists but cited paragraph was not found.
- `quote-mismatch` - quoted words differ from retrieved text.
- `unverified-source-unavailable` - source could not be checked.
- `duplicate-or-ambiguous-match` - search returns multiple plausible authorities.
- `lower-confidence-lead` - unofficial material suggests a possible match, but no verification-grade source was retrieved.

Use `citation-not-found` only after recording the sources and queries searched. If the search could not be run, use `unverified-source-unavailable`.

## Confidence Bands

- High: direct public/official source match with retrieved text and matching citation/case name.
- Medium: existence appears confirmed but text, party names, paragraph, or quote still needs checking.
- Low: indirect mention, ambiguous match, traditional citation without primary text, or unofficial/source-limited lead.

### 4. Check quotation and paragraph integrity

For direct quotes:

- Compare the quotation against retrieved text.
- Flag ellipses, substitutions, or changed emphasis.
- Distinguish harmless punctuation differences from substantive wording changes.

For paragraph references:

- Confirm paragraph number exists.
- Confirm the cited paragraph appears to support the proposition only if the user asks for proposition checking.

### 5. Report with evidence

Output a table:

| Field | Meaning |
|---|---|
| `citation` | cited authority |
| `document_location` | where it appears |
| `retrieved_case_name` | case name from the matched source |
| `retrieved_citation` | citation from the matched source |
| `retrieved_court_date` | court and judgment date from the matched source |
| `status` | classification |
| `matched_source` | URL or source name |
| `sources_searched` | sources and search queries used |
| `date_checked` | date verification was performed |
| `source_type` | official, public database, court/tribunal page, subscription, user-supplied, or unofficial |
| `issue` | what is wrong, if anything |
| `suggested_next_step` | verify, correct, replace, or research manually |

Keep unresolved authorities unresolved. A false negative is annoying; a false positive is dangerous.

## Escalation

Stop and ask when the citation appears Scottish, Northern Irish, tribunal-specific, devolved, non-UK, or otherwise outside the available public-source path and the correct official source cannot be identified. Do not fall back to BAILII or model memory as if it were verification-grade for those sources.

## Example

```text
Check the citations in this skeleton argument. Verify UK neutral citations against Find Case Law or BAILII, flag any case-name mismatches, and do not summarize cases that cannot be retrieved.
```

For a compact output pattern, see `examples/output.md`.
For resolution states, match quality, and source hierarchy, see `references/citation-resolution-model.md`.

## Limitations

- Not every UK judgment is available in public databases.
- Traditional report citations may require subscription databases or manual checking.
- Citation existence does not prove that the cited proposition is correct.
- Tribunal and older authorities may need specialist sources.
