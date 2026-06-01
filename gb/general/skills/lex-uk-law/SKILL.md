---
name: lex-uk-law
title: UK Legal Research with Lex API
description: UK legal research using the Lex API. Use this skill whenever the user asks about UK law, legislation, statutory instruments, Acts of Parliament, legal provisions, amendments, or anything that could benefit from searching authoritative UK legal sources. Also use when the user mentions specific UK Acts (e.g. "the Data Protection Act"), asks about legal requirements, or needs to understand how legislation has changed over time. Even if the user doesn't explicitly say "search legislation", if they're asking a question that UK law could answer, use this skill.
author: i-dot-ai
author_url: https://github.com/i-dot-ai/lex/tree/main/skills/lex-uk-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# UK Legal Research with Lex API

You have access to the complete corpus of UK legislation from The National Archives via MCP tools. This skill teaches you how to conduct thorough legal research — not just which tools exist, but how to use them together effectively.

## Research Workflows

Different questions need different approaches. Choose the right workflow for the task.

### "What law covers X?" — Topic Research

When the user asks about a legal topic (e.g. "unfair dismissal", "data protection for AI"):

1. **Search for Acts first** using `search_for_legislation_acts` with a natural language query. Set `include_text: false` for speed — you only need titles and IDs at this stage.
2. **Drill into sections** using `search_for_legislation_sections` for each relevant Act found. Pass the `legislation_id` to scope your search. This is where the substantive law lives. Use `include_text: true` when you need to verify a result is genuinely relevant — title matches can be misleading for generic section titles like "Interpretation" or "Extent".
3. **Check amendments** using `search_amendments` on key Acts — legislation may have been significantly amended or even partially repealed since enactment. This is easy to miss and important.
4. **Read explanatory notes** using `get_explanatory_note_by_legislation` or `get_explanatory_note_by_section` to understand Parliament's intent. Not all Acts have explanatory notes — they're generally available for post-1999 legislation, but even some recent Acts lack them.
5. **Try multiple search phrasings** for broad topics. Semantic search activates different results for different phrasings — "employment tribunal dismissal" and "unfair dismissal workplace rights" may surface different Acts. Cast a wide net rather than relying on a single query.

The goal is to present a complete picture: what the law says, how it has changed, and what Parliament intended.

### "What does section X of Y say?" — Specific Lookup

When the user asks about a specific provision:

1. **Look up the Act** using `lookup_legislation` with `legislation_type`, `year`, and `number`.
2. **Get the section** using `search_for_legislation_sections` with the `legislation_id` and an empty query to retrieve by filter.
3. **Check amendments** to that section using `search_amendment_sections` with the `provision_id` (e.g. "ukpga/1998/42/section/3"), then also `search_amendments` at the Act level. Section-level search finds textual amendments; Act-level search catches disapplications by later Acts. Both are needed for a complete picture.
4. **Get the explanatory note** using `get_explanatory_note_by_section` for context on what the provision means.

### "How has X been amended?" — Amendment Research

When the user asks about changes to legislation:

1. **For section-level amendments**: use `search_amendment_sections` with the `provision_id` (e.g. "ukpga/1998/42/section/3"). The provision_id must include the section path, not just the Act ID.
2. **Always also check Act-level amendments**: use `search_amendments` with the `legislation_id`. This catches amendments that section-level search may miss — particularly disapplications, where a later Act limits where the provision applies without changing its text. Disapplications are enacted by *other* Acts and may not appear in section-level amendment results.
3. **If both return nothing, search for referencing legislation**: use `search_for_legislation_sections` with a query like "amends [Act name]" or "section [N] [Act name]". Other Acts may reference or modify the provision's effect without being recorded as formal amendments. This fallback is particularly important for pre-2001 legislation, where structured amendment data is sparse.
4. **Distinguish amendment types**: textual amendments change the wording; disapplications limit where the provision applies without changing its text; repeals remove it entirely. Disapplications are easy to miss because the original text looks unchanged — always check for them explicitly.

### "What was the intent behind X?" — Parliamentary Intent

1. **Get explanatory notes** using `get_explanatory_note_by_legislation` for an overview of the whole Act, or `get_explanatory_note_by_section` for a specific provision.
2. **Search notes by topic** using `search_explanatory_note` with a natural language query if you don't know which Act is relevant.
3. **Filter by note type**: use `note_type` to focus on specific sections of the explanatory material (overview, policy_background, legal_background, extent, provisions, commencement, related_documents).

### Historical Legislation (pre-1900)

The database contains ~85,000 Acts from 1267 onwards, including major public general Acts. When researching historical legislation:

1. **Use year filters**: `year_from` and `year_to` work reliably across the full date range. Use them to narrow results to the relevant period.
2. **Expect different structure**: Pre-1963 legislation was ingested from PDFs, so section numbering and titles may be inconsistent. The text is there but may lack the clean structure of modern Acts.
3. **Try both Act and section search**: Historical Acts are discoverable via semantic search. If Act-level search finds something relevant, drill into sections with `search_for_legislation_sections` using the `legislation_id` and `include_text: true` to read the actual provisions.
4. **Regnal year citations**: Pre-1963 legislation uses regnal year URIs (e.g. `ukpga/Vict/8-9/20` for 8 & 9 Vict. c. 20). These work as `legislation_id` values in all tools.
5. **Amendment data will be sparse**: Structured amendment records largely begin from ~2002. For historical Acts, use the referencing search fallback (search section text for "amends [Act name]") rather than relying on amendment tools.

## Common Mistakes to Avoid

- **Searching Acts when you need sections**: `search_for_legislation_acts` returns whole Acts ranked by relevance. If the user wants specific provisions, use `search_for_legislation_sections` instead — or use Acts search first, then sections search to drill in.
- **Not checking amendments**: Always check amendments for key provisions. Legislation from even a few years ago may have been substantially changed.
- **Only checking section-level amendments**: `search_amendment_sections` finds direct textual amendments but can miss disapplications enacted by other Acts. Always also run `search_amendments` at the Act level — this is how you find provisions like the Victims and Prisoners Act 2024 disapplying HRA s.3 in specific contexts.
- **Repeating the same search**: If a search returns poor results, try different terms rather than the same query again. The search is semantic — rephrase your query to explore different parts of the embedding space.
- **Trusting title matches blindly**: A result with a high relevance score may match on title only. Use `include_text: true` and read the actual provision before citing it — especially for sections with generic titles.
- **Forgetting explanatory notes**: When the user asks "why" or "what was the intent", explanatory notes are the answer. They're published by the government alongside the Act and explain the purpose of each provision. Not every Act has them, but when available they're invaluable.
- **Using full URLs as IDs**: Use short form IDs like "ukpga/1998/42", not "http://www.legislation.gov.uk/id/ukpga/1998/42".

## Tool Reference

### Legislation Search
- `search_for_legislation_acts` — find Acts/SIs by topic. Key params: `query`, `legislation_type`, `year_from`/`year_to`, `include_text`, `limit`.
- `search_for_legislation_sections` — find provisions within legislation. Key params: `query`, `legislation_id`, `legislation_type`, `legislation_category`, `year_from`/`year_to`, `size`, `include_text`.

### Legislation Retrieval
- `lookup_legislation` — get a specific Act by type/year/number.
- `get_legislation_sections` — list all sections of an Act by `legislation_id`.
- `get_legislation_full_text` — complete text. Set `include_schedules: true` only if specifically needed.
- `proxy_legislation_data` — enriched metadata from legislation.gov.uk.

### Explanatory Notes
- `search_explanatory_note` — search note content. Key params: `query`, `legislation_id`, `note_type`, `section_type`.
- `get_explanatory_note_by_legislation` — all notes for an Act.
- `get_explanatory_note_by_section` — note for a specific section number.

### Amendments
- `search_amendments` — Act-level amendments. Key params: `legislation_id`, `search_amended`.
- `search_amendment_sections` — section-level amendments. Key params: `provision_id`, `search_amended`.

## Output Guidelines

When presenting legal research:
- **Cite precisely**: include Act name, year, section number, and legislation ID.
- **Structure by Act**: group findings under each relevant Act with clear headings.
- **Distinguish current from historical**: note if provisions have been amended, repealed, or disapplied.
- **Quote sparingly**: short quotes from the legislation text are useful; long block quotes are not.
- **Include a sources table**: list the Acts consulted with their legislation IDs at the end.

## Data Coverage

- **Legislation**: ~85,000 Acts from 1267–present. Complete structured coverage from 1963; pre-1963 from PDF extraction. 99.8% of sections have year metadata enabling year-filtered search across the full range.
- **Explanatory Notes**: Generally available for post-1999 legislation, though not every Act has them. Pre-1999 Acts have no explanatory notes in any digital source.
- **Amendments**: Comprehensive from ~2002 onwards (892,000+ records). Pre-2001 amendment data is sparse — this is a source limitation from legislation.gov.uk, not a gap in Lex. For older legislation, search section text for referencing Acts as a fallback.
- **Sources**: The National Archives / legislation.gov.uk. All content is verbatim from the source — the API does not summarise or modify legislation text.
