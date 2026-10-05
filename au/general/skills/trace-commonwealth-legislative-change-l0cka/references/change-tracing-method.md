# Commonwealth legislative change-tracing method

## Source hierarchy

1. Use the Federal Register title, point-in-time and All versions pages to
   establish identity and the complete compilation interval.
2. Use the Register API for reproducible title, version and compilation-reason
   metadata. Treat its reason records as navigation evidence, not proof that a
   named provision changed.
3. Use the exact official compilation texts and endnotes to establish before,
   after and intervening text and amendment history.
4. Use the as-made amending Act or instrument and exact schedule item to
   establish what textual amendment was enacted or made.
5. Use commencement provisions, commencement instruments and relevant endnotes
   to establish timing. Use explanatory material only as context, not as the
   authority for the operative text or commencement.

Treat search engines and secondary services only as discovery aids. Do not use
them to establish identity, text, timing or currency when the Register is
available.

## Comparison semantics

- Resolve both endpoint compilations by Register ID and effective start date.
- Enumerate every compilation between the endpoint versions. An endpoint-only
  diff can miss an amendment that was later reversed.
- `TEXT CHANGED` means the exact endpoint text differs and the difference is
  evidenced from the official compilations.
- `NO NET TEXT CHANGE` means the endpoint text is identical. It does not mean
  there were no intervening changes or changes in legal operation.
- `INTERVENING CHANGES WITH NO NET CHANGE` requires evidence that the provision
  changed during the interval and returned to the endpoint text.
- A shared endpoint compilation means no compilation transition was found. It
  does not prove that commencement, application or legal operation was static.

Compare structure as well as words. Check provision labels, headings,
subsections, paragraphs, notes, definitions and cross-references. Do not treat a
renumbered or relocated provision as deleted without checking the amendment
history.

## Attribution test

Attribute a textual change to an amending law only when the evidence chain
connects:

1. The affected compilation and its amendment history.
2. The amending title and Title ID.
3. The exact schedule, item or provision.
4. The amendment instruction and affected provision.
5. The commencement source relevant to that item.

An API `reason` can identify a candidate amending title and item, but it can
describe changes elsewhere in the compilation. Confirm provision-level
relevance from the compilation endnotes and amending text.

## Commencement and incorporation

- A compilation has a compilation date and effective period; it does not itself
  commence. Reserve `commenced` for legislation, provisions and amendment items.
- Do not equate Royal Assent, making, registration, publication or compilation
  registration with commencement.
- Record item-level or provision-level commencement where amendments commence
  at different times.
- Keep commencement separate from incorporation. A commenced amendment may not
  yet appear in the latest compilation.
- Treat retrospective compilation dates and retrospective amendments as
  qualifications requiring explicit review.
- Flag application, savings and transitional provisions. A text change does not
  establish which facts or periods the amended text governs.

## Special cases

- Treat an official PDF as authorised only after confirming its authorisation
  stamp. Do not call HTML, EPUB or a modified copy an authorised version.
- For a provision absent at one endpoint, inspect the amendment instruction
  before reporting insertion, repeal, substitution, renumbering or relocation.
- For editorial changes, rectifications or replacement compilations, inspect
  the Downloads page and endnotes; do not attribute them automatically to an
  amending law.
- For incorporated external documents, report that the Register text does not
  establish the external document's content or legal effect.
- For incomplete historical holdings, report the coverage limitation rather
  than inferring that no change occurred.
- For more than 10 provisions, ask the user to narrow or batch the request.

## Official method sources

- [About the Register and authorised versions](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/about-the-federal-register-of-legislation)
- [Point-in-time search](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/how-to-use-browse-search-and-advanced-search)
- [Status, effective dates and unincorporated amendments](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/frequently-asked-questions)
- [Reading compilations and commencement](https://www.legislation.gov.au/help-and-resources/understanding-legislation/reading-legislation)
- [API and reuse](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/data-share-and-reuse)

Recheck these sources when using the workflow. The API, interfaces and available
historical material can change.
