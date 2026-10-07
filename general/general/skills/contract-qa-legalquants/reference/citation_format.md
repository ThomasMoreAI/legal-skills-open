# Citation Conventions for Contract QA

Citations are how the user verifies the answer. This reference establishes the conventions Contract QA uses for citing into a contract.

## Why citation conventions matter

Contract QA's output is only useful if the user can verify it. A correct answer with a missing or wrong citation is functionally a wrong answer — the user has to re-read the contract to confirm. Strong citation conventions reduce verification cost to near zero.

The Citation Engine (PRD §3.3) produces verbatim quotes with character-level fidelity and bbox-overlay highlighting in the side-panel viewer. Contract QA outputs the citations that drive that viewer.

## Citation format

Cite using bracket notation with the section/clause reference and (when available) the page reference:

- `[§4.2(b)]` — section reference only
- `[§4.2(b), p. 7]` — section reference with page
- `[Schedule A, ¶3]` — non-section reference (schedules, exhibits, recitals)
- `[Recital C]` — recital reference
- `[Annex II §1.4]` — nested reference to a section within an annex

When a citation supports a verbatim quote, the citation goes after the quote on its own line:

```
> "The Receiving Party shall maintain the confidentiality of all
> Confidential Information for a period of three (3) years from
> the date of disclosure."

[§3.1, p. 4]
```

When a citation supports a paraphrase or interpretation, the citation goes inline at the end of the relevant sentence:

```
The confidentiality obligation lasts three years from disclosure [§3.1].
```

## When to use verbatim quotes vs. paraphrases

**Use a verbatim quote when:**
- The exact words matter for the user's question (interpretation, comparison, scenario analysis).
- The user asked "what does the contract say about X" or similar.
- The quote is short enough to be readable inline (typically under 60 words).

**Use a paraphrase when:**
- The relevant content is too long to quote (e.g., an entire indemnification section).
- The user's question is about location ("where is X addressed") more than content.
- The relevant content is scattered across multiple short clauses; paraphrase the combined effect, then cite each.

When paraphrasing, name the paraphrase explicitly: *"The clause provides, in substance, that..."* — this signals to the user that the words are mine, not the contract's.

## Citing multiple clauses

When an answer depends on multiple clauses, cite each:

```
The IP assignment in §6.1 is qualified by the reservation of the
Receiving Party's pre-existing IP in §6.2 and the explicit feedback
carve-out in §6.3.

[§6.1, §6.2, §6.3]
```

When the clauses operate in sequence (one triggers, another responds), present them in operative order:

```
A material breach triggers the cure period in §11.2(a), which gives
the breaching party thirty (30) days to cure [§11.2(a)]. If the breach
is not cured, the non-breaching party may terminate under §11.2(b)
[§11.2(b)]. Termination triggers the wind-down provisions in §11.3
[§11.3].
```

## Page numbers

Include page numbers when the document has them and the citation engine has them available. Page numbers significantly aid verification, especially for long contracts. Format: `[§4.2, p. 7]`.

For documents that lack natural page numbers (web-pasted text, Word documents without page breaks), omit the page reference. Do not invent page numbers.

## Citing across the document structure

Most contracts have a hierarchical structure. Use the appropriate level:

- **Article / Part** — `[Article 5]`. Use only when the answer references the whole article.
- **Section** — `[§5.2]`. The most common citation level.
- **Subsection** — `[§5.2(b)]`. Use when the answer turns on a specific subsection.
- **Sub-subsection** — `[§5.2(b)(iii)]`. Use when the answer turns on a specific element.

Cite at the most specific level that supports the answer. Citing `[Article 5]` when the answer turns on `[§5.2(b)(iii)]` makes the user re-read more than they need to.

## Citing across documents

Contract QA v1.0.0 operates against a single document. When citing within that document, no document identifier is needed. (Multi-document Q&A is deferred to v2; when it lands, citations will need a document identifier prefix.)

If the contract incorporates other documents by reference (a master agreement referencing schedules, an MSA referencing SOWs), cite them by their identifying name:

- `[MSA §4.2]`
- `[SOW-3 §2.1]`
- `[DPA Annex II §1.4]`

If the referenced document is not in scope (the user has uploaded the MSA but not the SOWs), note that explicitly: *"The MSA at §7.1 references SOW-specific obligations; the SOWs are not in this review."*

## Quote accuracy

Verbatim quotes must be exact, including punctuation, capitalization, and original errors. Do not silently fix typos in the contract. If the contract contains an error that affects meaning, quote the error and note it: *"The clause says 'twenty (30) days' (the contract uses both 'twenty' and '30' for this period; the inconsistency is unresolved by the document)."*

Do not normalize formatting in quotes (e.g., changing all-caps headings to title case, changing numbered lists to bullets). The contract's formatting is part of the contract.

When a quote spans a page break, that's fine; quote across the break naturally and cite the section, not the pages.

## When the document is hard to cite

Some documents resist clean citation:

- **Unstructured contracts** (no section numbers, just paragraphs). Cite by paragraph index or by the first few words: `[paragraph beginning "The Parties acknowledge..."]`.
- **Tables.** Cite the table location and the cell or row: `[Pricing Table, row 3]` or `[Annex I, table titled 'Service Levels', column 'Penalty']`.
- **Figures or diagrams.** Describe the location: `[Figure 2, p. 14]`. If the figure's content matters to the answer, describe the figure rather than relying on visual reference.
- **Footnotes.** Cite as: `[§4.2 footnote 3]`.

When a contract is genuinely difficult to cite (poor scan quality, unstructured prose, missing section numbers throughout), note the limitation: *"This contract is not cleanly structured; citations reference the closest identifiable location but may require the user to navigate the document for verification."*

## Side-panel viewer behavior

When the user clicks a citation in the rendered output, the application opens the side-panel PDF.js viewer (PRD §3.3) at the cited location with bbox highlighting. The skill itself does not control this UX; it produces citations that the application uses.

For the citations to drive the viewer correctly, the citation engine needs the chunk metadata (chunk_id, page, char_start, char_end, bbox). Contract QA produces citations in the human-readable format above; the application maps these to the underlying CitableChunk metadata.

If the citation is to content that the citation engine could not resolve to a specific chunk (e.g., the structural reference is ambiguous), the skill should note this: *"Cited as §4.2 based on the document's structure; the citation engine may not resolve this to a precise location if the document's section numbering is unclear."*
