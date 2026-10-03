# Citation Resolution Model

Use this reference when a task requires UK citation checking, hallucination screening, or authority triage.

## Three Different Questions

Keep these separate:

1. **Existence** - does the cited authority appear to exist?
2. **Text access** - can the judgment/source text be retrieved?
3. **Use in argument** - does the source support the proposition or quotation?

This skill answers the first two and flags quote/paragraph integrity where text is available. Proposition support belongs to a proposition-checking workflow.

## Citation Classes

| Class | Example | Handling |
|---|---|---|
| Neutral citation | `[2024] EWCA Civ 641` | Usually suitable for public-source resolution |
| Court abbreviation with number | `UKSC`, `EWCA Civ`, `EWHC Ch` | Try official/public source path first |
| Traditional law report | `[2017] AC 1173` | Often manual or subscription-source check |
| Case name only | `Wood v Capita` | Search lead, not verification by itself |
| Paragraph reference | `[46]` | Check only after judgment text is retrieved |
| Direct quotation | quoted text | Compare against retrieved text; preserve mismatch |

## Resolution States

Use these states:

- `resolved_with_text` - authority exists and judgment/source text was retrieved.
- `resolved_no_text` - existence confirmed but text not available.
- `not_found` - searched named sources and no match found.
- `ambiguous` - multiple plausible matches or uncertain party/citation match.
- `traditional_manual_only` - traditional citation needs manual/subscription checking.
- `indirect_mention_only` - source appears only as a reference in another judgment or index.
- `unverified-source-unavailable` - no source access available.

Do not upgrade `indirect_mention_only` to `resolved_with_text`.

## Match Quality

Record how the match was made:

- `direct_url` - constructed or retrieved direct judgment page/PDF.
- `official_search_result` - official/public database search result.
- `title_match` - title matches but citation needs checking.
- `full_text_hit` - citation appears in another document.
- `user_supplied_text` - user provided the source.
- `subscription_reported` - user reports a subscription result; source not independently retrieved.

## Source Hierarchy

Prefer:

1. Find Case Law / National Archives for available UK judgments.
2. BAILII for public judgments not available on FCL or where FCL unavailable.
3. Court, tribunal, or official source pages.
4. User-supplied primary material.
5. Unofficial summaries only as leads.

Search snippets, commentary, and model memory are never verification-grade.

## Output Requirements

For every citation, include:

- cited text and source location in the draft,
- citation class,
- resolution state,
- match quality,
- sources searched and queries,
- retrieved case name and citation where available,
- date checked,
- next step.

## Failure Modes

- Correct case name with wrong neutral citation.
- Real citation with wrong party names.
- Case exists but paragraph reference does not.
- Case exists but quote is altered or omits a material qualification.
- Traditional citation treated as verified without primary text.
- Search result mentions the citation but is not the judgment.
