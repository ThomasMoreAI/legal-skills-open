---
name: oscola-build-citation-uk-agents
title: /oscola-build-citation
description: Construct an OSCOLA citation for a UK case, statute, or Hansard reference AFTER verifying the source exists via uk-legal MCP. Use whenever the user asks to "cite <source> in OSCOLA", "give me the OSCOLA citation for", "format this as OSCOLA", or pastes a partial citation. This skill verifies first and formats second — preventing the most common citation fabrication route where an agent formats plausible-looking fields without confirming the source actually exists.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/law-student-uk/skills/oscola-build-citation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /oscola-build-citation

1. Identify the source type: case / statute / SI / Hansard / journal article.
2. Verify first: `citations_resolve(input=...)` with the identifier the user gave.
3. If `not_found`, stop — tell the user; do not format an unverified citation.
4. If resolved, build OSCOLA from the authoritative fields in the result.
5. Tag `[uk-legal MCP — verified]`; note any discrepancy with the user's input.

---

## Purpose

Construct a correctly formatted OSCOLA citation for a UK legal source — after
verifying that the source exists in the UK legal record. The failure mode this
prevents: an agent formatting plausible-looking OSCOLA fields (correct year bracket
style, court abbreviation, report reference) for a source that does not exist, or
that differs in key details from what the user provided. Verification before
formatting is the discipline.

## Workflow

> **Source discipline:** If a `uk-legal MCP` tool returns empty or errored (status: `empty` / `not_found` / `upstream_validation` / etc.), do NOT supplement from training data or web search. Report the empty result to the user with the tool's `next_steps` / `detail` field surfaced, and ask for clarifying information (different spelling of a name, a date range, the source URL) rather than fabricating a plausible-looking answer. Empty results are HONEST signal — not a failure mode to paper over.

### Step 1 — Identify the source type

Determine which source type the user is asking to cite:

| Type | Examples |
|---|---|
| Case | *R v Brown*, *Donoghue v Stevenson*, a neutral citation |
| Statute | Housing Act 1988, Equality Act 2010, a section reference |
| SI | SI 2021/1234, a short title |
| Hansard | HL Deb vol N col M, a member's speech reference |
| Journal article | Author, title, journal, volume |

If the source type is ambiguous from the user's request, ask before proceeding.

### Step 2 — Verify first

Call `citations_resolve(input=...)` with whatever identifier the user provided: a
neutral citation, statute short title, SI number, Hansard column reference, or URI.

- For a Hansard source described rather than precisely cited (e.g. "Lord Pannick's
  speech on the Renters' Rights Bill"), use `parliament_search_hansard` followed by
  `parliament_get_debate_contributions` (as in `/find-member-contribution`) to locate
  the specific contribution first, then format from the returned fields.
- The resolved record provides the authoritative fields for formatting.

### Step 3 — Refuse if not resolved

If `citations_resolve` returns `not_found`:

- Do NOT proceed to format a citation.
- Tell the user: "I can't verify [input] exists in the UK legal record. Could you
  share the source URL, or check the citation for typos?"
- Do NOT produce a best-guess OSCOLA format for an unresolved source.

If `citations_resolve` returns `ambiguous`, list the candidates and ask the user
to confirm which one before formatting.

### Step 4 — Format from authoritative fields

Build the OSCOLA citation using the resolved source's authoritative fields — NOT
the user's input fields. If the user gave year 1993 and the resolved record says
1994, use 1994 and note the discrepancy explicitly.

Apply the following OSCOLA formats:

**Case:**
> *Party v Party* [Year] Court Report, pinpoint if applicable
> (Neutral citation from the resolved record)

**Statute:**
> Short Title Year (jurisdiction abbreviation if not England & Wales)
> Examples: Equality Act 2010; Requirements of Writing (Scotland) Act 1995

**SI:**
> SI Year/Number (Short Title Year)
> Example: SI 2021/1234 (Short Title 2021)

**Hansard:**
> HC/HL Deb, vol N, col M (Date)
> Example: HL Deb, vol 825, col 462 (14 October 2025)

**Journal article** (not MCP-verified — flag accordingly):
> Author, 'Title' (Year) Vol Journal StartPage
> `[model knowledge — verify]`

### Step 5 — Tag and note discrepancies

- Tag every output citation `[uk-legal MCP — verified]`
- Include the resolved source URI for traceability
- If the resolved record differs from what the user provided (e.g. different year,
  different court abbreviation, different party name spelling), note each discrepancy
  explicitly before the formatted citation

**Source attribution.** A citation may only carry `[uk-legal MCP — verified]` if
`citations_resolve` returned a confirmed result in this session. Journal article
citations (not in the MCP corpus) carry `[model knowledge — verify]` and must be
checked manually by the user before use in a submission or assessed work.

## Output

Surface to the user:

- **Source type:** confirmed
- **Verification status:** Verified via `citations_resolve` / Not resolved — do not cite
- **OSCOLA citation** (if verified):

  > *formatted citation* `[uk-legal MCP — verified]`
  > Source URI: [resolved URI]

- **Discrepancies** (if any): list what the user provided vs. what the resolved
  record shows, before the formatted citation
- **Suggested next steps:** for a case citation, offer to retrieve specific paragraphs
  via `judgment_get_paragraph`; for a Hansard citation, offer to retrieve the full
  contribution via `/find-member-contribution`

**Test prompts:**
- "Format this as OSCOLA: R v Brown, 1993, House of Lords, [1994] 1 AC 212."
- "Give me the OSCOLA citation for section 21 of the Housing Act 1988."
- "Cite Lord Pannick's contribution to the Renters' Rights Bill Lords debate in OSCOLA."
