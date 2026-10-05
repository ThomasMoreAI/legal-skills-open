# Bounded statutory citation verification

Use for statute, regulation or rule units referred by a citation-review workflow.
This is the receiving contract; enabling automatic routing in cite-check is a
separate change for that skill's maintainer. No worker runtime is required.

## Inputs and gate

Accept the unit id, citation (including pinpoint), quoted text if any,
jurisdiction, relevant as-of date, and supplied-source match result. Run when
no supplied statutory source matched and the user has selected official-source
verification, or explicitly asks Regulatory to verify the unit. Do not send
client facts or the whole document to a retrieval service. If the date or
instrument identity is ambiguous, ask only for that missing selector.

A matched supplied source remains checked only to the supplied version unless
separately version-verified; this handoff does not silently upgrade that result.
Case law is outside this interface. Unavailable case sources retain separate
existence and substance coverage, never a statutory verification status.

## Work and bounded cost

Dedupe by jurisdiction + stable instrument id + requested date + provision;
share one publisher retrieval/version record across provisions of that same
instrument, date and language. Do not merge different dates or instruments.
Keep the run-local cache in the workspace and remove it on completion unless
retention is requested. Retry at most two alternative official endpoints per
source after a failed fetch. No full research memo, broad research fan-out or
case-law investigation is needed.

Run the ordinary spine and gates for the distinct units. Check existence in the
correct dated text, not merely whether a URL resolves. Fetch definitions or
commencement provisions when needed to establish version or scope. Preserve
exact pinpoint attribution coverage; a wording match against an article does
not establish a paragraph citation.

## Return one record per original unit

Return `unit_id`, `canonical_instrument_id`, `requested_date`, `provision`,
`existence` (confirmed / not-found-in-verified-scope / unresolved), `version`
(confirmed-for-date / wrong-date / unresolved), `quotation` (matched /
mismatch / attribution-unverified / not-requested), `coverage`, `source_url`,
`evidence_paths`, and `unresolved_reason` where applicable. Link duplicate units
to the shared evidence, retaining each original unit id.

A failed fetch or partial extraction is unresolved, never evidence a section
was fabricated. Reserve not-found-in-verified-scope for a complete, verified
search of the relevant instrument/date; state that scope. A stale or fabricated
pinpoint must not receive a green result merely because its article exists.
The calling workflow incorporates the bounded result and its limitations.
