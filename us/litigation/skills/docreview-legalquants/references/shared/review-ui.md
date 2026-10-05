# DocReview lawyer-facing review UI contract

Use this contract for `review-setup.html`, `review-test-results.html`, and
`crosswalk.html`. These pages are deterministic offline legal-review surfaces,
not generated client presentations. They share stable presentation rules with
`/legaldesign`, but DocReview does not invoke `/legaldesign` at runtime and does not
depend on its host utilities, network resources, or conversation-only APIs.
`/legaldesign` may consume an approved DocReview result later when the lawyer
separately asks for a client-facing explainer.

The rendered contract identifier is `lq-lawyer-review-v1`.

## Reading order and language

- Lead with the lawyer's decision, what it authorizes, and what it does not.
  Keep implementation names, stable IDs, hashes, framework versions, and
  runner mechanics in a collapsed receipt or Audit area.
- Write visible instructions in ordinary legal-review language. Internal
  execution terms such as **call**, **bundle**, **batch**, and **staged** may
  appear in collapsed technical receipts, but never as the label for a lawyer
  decision or next action.
- Use one status vocabulary everywhere: **Responsive**, **Nothing found**,
  **Needs a decision**, and **Needs rendering**. Pair every status color with its text;
  color is never the only signal.
- “Not found” remains scoped to the supplied visible text in the identified
  review unit. It never implies corpus-wide or real-world absence.
- Amber is reserved for a discrete item requiring attention. Do not turn the
  whole page yellow merely because one item needs a decision.
- Use progressive disclosure for evidence detail and technical receipts. Do
  not hide the decision, the source identity, or a stop condition.
- When the framework lists separate discovery sets that were outside the
  current comparison, label the section **Scope of this page**. State that no
  positive or negative result was made for those sets; do not display an
  unexplained count of “staged” or “not checked” requests.
- For scanned or image-only files, tell the lawyer to review every page and the
  proposed matches and non-matches before marking **Page review complete**.
  Never ask the lawyer to “confirm calls” or an “image-based bundle.”

## Portable brand system

- Use the semantic `--lq-*` tokens emitted by `scripts/review_ui.py`; do not
  create a page-specific palette. Every foreground, surface, border, focus,
  status, and interactive color must have both light and dark values.
- The warm-paper background, quiet white/charcoal surfaces, deep green primary
  action, and restrained amber/red status colors are the LQ lawyer-review
  presentation. Keep the chrome quiet so the evidence remains dominant.
- Use system fonts only. Body text is sans-serif; a restrained legal serif may
  be used for principal headings and quoted agreement language; monospace is
  limited to receipts and stable identifiers. Use only weights `400` and `500`.
  Secondary text must remain at least 11px.
- Use one `LQ · Document Review` masthead. Avoid nested-card dashboards,
  decorative shadows, ornamental borders, oversized icons, and redundant KPI
  panels. A bounded card must explain a real decision or evidence unit.

## Accessibility and responsive behavior

- Support 320px through desktop widths. Stack or wrap before content clips;
  horizontal scrolling is limited to tables whose columns genuinely cannot
  fit. Do not use fixed viewport-height layouts or an internally scrolling
  page shell.
- Use semantic headings, links, details, tables, and native form controls.
  Preserve native tab order, visible `:focus-visible` treatment, a skip link,
  and concise accessible names. Use `aria-live="polite"` for dynamic status and
  `role="alert"` for a blocker.
- Tabs expose `tablist`, `tab`, and `tabpanel` roles and support click plus
  arrow-key navigation. Search, filters, clear actions, and theme controls must
  be exercised, not merely displayed.
- Honor `prefers-reduced-motion`. The first render must be useful without any
  interaction.

## Offline and deterministic operation

- The output is deterministic offline HTML: same approved inputs, same bytes.
  Inline the CSS and JavaScript required for the review. Do not load external
  fonts, styles, scripts, images, APIs, host globals, or CDNs; do not call
  `fetch`, XHR, WebSocket, or a conversation runtime.
- Durable output contains no timestamps, machine names, or absolute paths.
  Local source and review-copy links use validated relative paths.
- Presentation code cannot mutate the manifest, framework, findings, maker or
  checker proposals, quote receipts, checker receipts, or lawyer rulings.

## Source-review and renderability gate

The original file is provenance; a raw-file link alone is not a sufficient
lawyer review experience. Every in-scope reviewed document and separately
reviewable attachment needs an in-page representation bound to the same source
ID and content hash.

Use this cascade:

1. a safe built-in offline preview for ordinary text, EML headers/body and
   attachment inventory, and common images;
2. a browser-native or receipted open-source render, such as Poppler for PDF or
   LibreOffice for supported Office files; and
3. a firm-selected native or legal-grade renderer when required.

A derivative remains labeled **review copy**. Record its source ID and source
hash, renderer and version, page order, and each output hash. It never receives
a new finding or replaces the evidence original. A stale source hash, missing
page, failed conversion, or unsupported format goes to a visible **Needs
rendering** queue and stops approval for every dependent review result.

`scripts/shared/review_copies.py` owns this layer. Build `review-copies.json` and its
content-addressed bundle after the manifest is final, using `--mode auto` for a
real run or `--mode text` for deterministic stdlib-only evals. The sidecar
binds the canonical manifest digest, each full source hash and byte count,
each separately reviewable email attachment, every derivative hash, and the
exact set of files in the bundle. It contains no timestamp, URL, or absolute
path. The builder copies no conclusions into the sidecar.

Every lawyer-facing renderer must receive both `--review-copies` and
`--document-root`, revalidate the sidecar against the current manifest and
source bytes, and refuse all embeds on any integrity error. The HTML output and
sidecar must share a directory because bundle references are deliberately
relative to the sidecar. A valid sidecar may still have status
`needs-rendering`; in that case, render the affected item and reason, disable
or fail the dependent approval, and keep all unaffected copies reviewable.
Never turn a rendering failure into `Not found` or alter a finding, framework,
quote receipt, checker receipt, proposal, or lawyer ruling.

Render each source once per page. Findings link to that same-page copy; the
original file is a secondary provenance link. Text and EML derivatives use a
sandboxed iframe, common images use an image element, and verified PDFs use a
browser PDF object with a fallback link. Office documents always receive a
safe visible-text derivative when their OOXML package is readable; optional
LibreOffice/Poppler availability may add receipted page images without making
the core rendering path nondeterministic.
