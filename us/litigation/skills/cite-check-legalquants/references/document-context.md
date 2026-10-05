# Document preparation and unit context

This reference defines host-native preparation for `/cite-check`. It does not require a particular DOCX, PDF, OCR, Markdown, or citation parser.

## Preparation boundary

Use the host's existing document-reading capability to create temporary UTF-8 Markdown or plain-text working copies. Preserve the original target and authority files. If a file cannot be read, record the limitation and ask for a readable copy when necessary; do not install a parser or silently invent extracted text.

Normalize the working copy to LF line endings and keep each extractable text container on one physical line. Preserve source order and retain source-faithful text when available. Extraction-only line breaks inside a paragraph may become spaces in the display text, but uncertain joins remain an extraction limitation. Page markers are metadata, not line-number pinpoints.

## Mechanical units

Create one unit for each extractable paragraph, list item, table cell, heading, caption, footnote, endnote, header, footer, or text box. A short heading or a visually separate container is still a unit. Record:

- stable `P####` IDs for body units and `F####` IDs for footnotes, in source order;
- the container kind, ordinal, section path, source file path, and line range;
- one-line display text and source-faithful verbatim text when available; and
- for each footnote, the body unit that anchors it when known.

The unit ID is stable within the prepared run and is copied unchanged into the assignment, terminal result, retry, aggregation, and report. It is never derived from a Markdown line number. A footnote may be the assigned unit when it contains the citation; its body unit remains context unless it independently has a citation.

Inspect every container the host exposes. If a potentially citation-bearing container cannot be represented faithfully, record the exact limitation and affected location and keep coverage visibly incomplete. Do not merge it into a nearby paragraph or silently omit it.

## Authority once-over

Record a stable source ID, workspace-relative path, readability state, and content identity cues for each supplied authority. Identity cues may include case name, reporter citation, court, date, docket, statute or regulation title, section, canonical URL, or other identifying text. Treat filenames and URLs as hints only. The parent performs one once-over for rough presence and readability; detailed source judgment happens in the assigned unit's review.

If no authority files were supplied, record that the run can search for cited cases but cannot verify what they say. Do not use model memory as source evidence. A case found through public search remains outside the substantive evidence set unless its full text is added to the workspace and assigned a source ID.

## Bounded context

The default context contains the nearest section heading or section path, the assigned unit, up to five substantive units before it, up to five substantive units after it, and attached footnotes. The window may cross a heading boundary, but the transition must remain visible.

For a footnote, include its anchored body unit and the same bounded nearby body context. The footnote remains the sole assigned scope. Provide a relative reference to the full prepared brief so a worker can resolve `Id.`, `supra`, or short-form antecedents outside the window. Full-document context is on-demand; it does not enlarge the assignment.

## Coverage and privacy

Before review begins, tell the lawyer which target and authority files were readable, which source identities were matched by content rather than filename, and which pages or units remain unreadable, ambiguous, incomplete, or missing. Do not make the lawyer set up a local runtime when the host can continue with one-unit native or sequential processing.

The report accounts for every prepared unit. A unit with no observed citation returns a terminal `no_citations_found` receipt and appears in the appendix; it is not a reason to discard the unit from accounting. A missing terminal receipt, malformed result, unreadable container, or unrepresented text container remains visible as incomplete. The main report body may omit units with no citation rows, but the appendix may not.

The same prepared units, authority universe, bounded context, prompt, and result fields apply to scripted fan-out, native workers, and one-at-a-time processing. Logs should record IDs, counts, statuses, retries, and actionable errors rather than substantive brief or authority text. The run directory persists after the report so the lawyer keeps an audit trail and enough material to retry; deleting it is the lawyer's manual decision, and no tool removes it.
