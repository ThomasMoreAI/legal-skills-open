# Cite-check judgment rubric

Use this rubric for every citation row. The assigned unit is the only reporting scope. Surrounding units, the anchored body unit for a footnote, and the full prepared brief are context for resolving meaning and antecedents; a citation reported by the worker must appear in the assigned unit.

The supplied authority files are the complete evidence universe for the three accuracy fields. Confirm identity and meaning from readable source content and stable locators. Do not substitute memory, a similar case, a filename, a URL, or an unsaved public lookup. When a source is not supplied or cannot be read, use the corresponding `source_not_found_*` accuracy value and leave source fields null.

A reporter-coordinate collision — the cited reporter coordinates belong to a different case in the supplied set — is positive evidence of an identity problem. An exact citation that could not be located after a bounded external search can support a fabrication concern when the search was available and recorded. A fuzzy caption mismatch, a low name-similarity score, or mere absence from CourtListener's United States case-law collections is not enough, especially for administrative decisions, statutes, rules, regulations, and other authorities CourtListener does not index. State positive findings in `fabrication_indicators`, `colliding_source_id`, `source_resolution`, and `existence_check_notes`. They are not a professional-conduct conclusion.

Do not invent a proposition for a heading, label, list-only citation, or citation that only supplies a citation chain; use `proposition: null` unless the assigned text states a legal claim. In “X, citing Y,” evaluate Y only for the proposition expressly attributed to Y. Do not project X's whole proposition onto Y.

## Source characterization

Judge `accuracy_of_source_characterization` holistically across the assigned sentence, citation, parenthetical, footnote, and relevant source context. The characterization is fair when it is accurate or stays within the boundaries of fair argument, even if the brief emphasizes a favorable inference or distinguishes an adverse case. It is potentially unfair or unreasonable when the words overstate, omit a material qualification, or create a misleading impression without making the source's actual meaning objectively false. It is objectively false or unreasonable when the supplied source affirmatively conflicts with the characterization or the wording cannot fairly be defended from the source.

A statement that a case **held** a point is a strong assertion. It is fair only when the case directly states or fairly implies that the point was part of how the case resolved at least one legal issue. No exact verbal formula is required, but the case must clearly support the holding; review “held” claims somewhat strictly.

A statement that a case merely **noted**, **observed**, or **implies** something is weaker. It may be fair even when the case did not definitively resolve that point, provided the source supports the more limited description and the brief does not turn it into a holding.

Cases cited affirmatively for the first time in the brief must be accurately stated. When the context shows that the brief is distinguishing or responding to a case cited by the adversary, the statement must still be accurate, but the characterization may be fair even when the distinction was not central to the original case's reasoning. Advocacy permits selection and emphasis; it does not permit a materially false or misleading account.

## Pinpoints

Use `pincite_accuracy` only for the locator claimed by that citation. `NA_no_pincite_for_this_citation` applies when the citation claims no separate locator. A reporter's starting page is citation identity metadata, not a pincite by itself. Use `pincite_confirmed_accurate` when the claimed page, paragraph, line, or other locator reaches the relevant source material, even when that material ultimately contradicts the brief. Use `pincite_inaccurate` when it does not. If the source cannot be found or inspected, use `source_not_found_unable_to_check_pincite`.

## Direct quotations

Use `accuracy_of_direct_quotation` only when the assigned unit presents a direct quotation as a quotation from the cited source. `NA_no_direct_quotation_for_this_citation` applies otherwise. A quotation is confirmed only when the supplied source supports the words and the surrounding context makes the use fair. Use `quotation_technically_accurate_but_misleading_or_unfair` when the words appear in the source but material context or a limiting phrase is omitted. Use `quotation_objectively_inaccurate` when the supplied source does not contain the quoted words as represented. If the source cannot be found or inspected, use `source_not_found_unable_to_check_quotation`.

## Source evidence and uncertainty

When `matched_source_id` is not null and an accuracy field is not a `source_not_found_*` value, provide a short verbatim `source_excerpt` and stable `source_locator`. Missing evidence is a warning that the citation is claimed but unverified; it is not a reason to invent evidence or fail the unit. Preserve ambiguity about `Id.`, `supra`, short forms, procedural posture, currentness, jurisdiction, and source identity in the recommended change or the report's caveats.

The source set does not establish Shepard's, KeyCite, later history, amendment status, overruling, vacatur, or comprehensive currentness unless treatment evidence is supplied. A source/candor concern is not a professional-conduct conclusion. Distinguish objective source mismatch, incomplete coverage, fair advocacy, and jurisdiction-specific ethics questions; route the last category to the reviewing lawyer.

Use the exact row-level enum values in [unit-review-prompt.md](unit-review-prompt.md), and keep worker output to the defined result object.
