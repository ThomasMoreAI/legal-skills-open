# Content structure for the employment-law dashboard

The dashboard always has the same skeleton. What changes from topic to topic is the substance, not the structure. This reference walks through each section, what goes in it, and how to think about it.

## Top-level structure

```
[Masthead]
  ├─ Eyebrow
  ├─ Title
  ├─ Subtitle (one short sentence)
  ├─ Updated [date]
  └─ Meta strip (3-6 stats)

[Top tabs] — US Overview | [Deep-dive 1] | [Deep-dive 2] | ...

US Overview tab:
  ├─ TL;DR (collapsible items)
  ├─ Multi-state trackers
  ├─ Recent articles (split: enacted laws / pending bills)
  └─ Comparison table (tabbed: AI definition / Notice / Disparate impact / Enforcement; jurisdiction filter)

Deep-dive tab (one per jurisdiction the user picked):
  ├─ Title + statute citations
  ├─ Lede (one short paragraph)
  ├─ Field rows (effective date, covered employers, covered decisions, AI definition...)
  └─ Compliance requirements section (numbered subsections)

[Footer]
  ├─ Footnotes (if any)
  └─ "For practitioner use only, not legal advice."
```

## Masthead

- **Eyebrow:** "The Brief On" in mono uppercase.
- **Title:** the topic, framed as the subject of regulation. "U.S. AI Employment Laws", "U.S. Pay Transparency Laws", "U.S. Non-Compete Restrictions". Sentence case for "U.S." but not for the topic.
- **Subtitle:** one short sentence starting with a preposition or article. "On laws regulating use of AI tools in the workplace." Don't write it as a meta-description ("A dashboard for monitoring...") — write it as if you're explaining the *topic* to a reader.
- **Updated [date]:** mono, no period.
- **Meta strip:** 3-6 stats. Pick stats that actually matter to the topic. For an AI law dashboard: state laws, city laws, in effect, states with pending bills, federal statutes. For a pay transparency dashboard: state laws, city laws, in effect, salary range required, states with pending bills. Tailor to substance.

If a stat is sourced to a tracker (e.g., "25+ states with pending bills"), add a small footnote indicator and put the citation in the footer.

## TL;DR

3-4 collapsible items. Each item:
- Heading visible by default (the "headline").
- Body expands on click and gives the supporting detail.

Choose headlines that capture the genuinely surprising or load-bearing observations. Bad: "Background." Good: "No federal statute or preemption." or "Five enacted laws, three already live."

Do **not** include a TL;DR item that's just "you should comply" or other practitioner advice — TL;DR items are observations, not recommendations.

## Multi-state trackers

2-4 reputable trackers. For each entry:
- Source name (org or firm).
- Update cadence (e.g., "Updated quarterly", "Rolling updates", "Live").
- Title (linked).
- One-paragraph description of what the tracker does and why a practitioner cares.

Keep the title clean — strip the publisher's name from the title if it's already shown above ("Littler 50-State AI Employment Legislation Survey" → "50-State AI Employment Legislation Survey").

## Recent articles

Split into two columns side-by-side: **Enacted laws** (left) and **Pending bills** (right). Hairline divider in the middle.

For each article:
- Source name + date.
- Title (linked, may be truncated to fit).
- Two-sentence description of why a practitioner would read it.

The format for the date metadata is consistent: "Source · Date" (e.g., "Cooley · April 24, 2026"). Don't include the publisher's tagline (e.g., "Privacy + Cyber + AI") — just the firm or publication name.

## Comparison table

The single most important component. This is where the topic actually gets compared across jurisdictions.

**Structure:**
- 4 tabs (typical): AI definition / Notice requirements / Disparate impact / Enforcement & remedies. Adjust tab names to topic — for pay transparency, tabs might be "Coverage / Required disclosures / Recordkeeping / Enforcement". Pick 3-5 tabs that segment the obligations cleanly.
- Multi-select state filter dropdown to the right of the tab strip. Default = "All". User can pick multiple jurisdictions.
- Each tab has its own table.
- Every row has `data-state="il|nyc|co|ca|tx"` (or whatever 2-3 letter code corresponds to the jurisdiction) so the filter works.
- First two columns are static across tabs: **Jurisdiction** (just the state/city name) and **Law** (law name + citation row underneath linking to statute, regs, official agency guidance).
- Each subsequent cell ends with a `<span class="cell-cite">` linking to the specific statutory section the claim rests on.

**Source rules for table cells:** PRIMARY SOURCES ONLY. Statute, regulation, official agency guidance on a `.gov` domain. No law firm summaries, even if accurate. See `references/source-policies.md`.

**Naming:**
- Use plain jurisdiction names ("Illinois", "New York City", "Colorado", "California", "Texas") — not "Illinois HB 3773".
- The "Law" column shows the law's name (e.g., "HB 3773", "Local Law 144", "AI Act (SB 24-205)") and a citation row.

## Deep dive (one or more)

The dashboard supports any number of deep-dive top-tabs — one per jurisdiction the user wants treated in detail. The skill explicitly asks the user which states to deep-dive on before building. Default to one (the most stringent or most-litigated regime), but accommodate as many as the user requests.

Each deep-dive tab follows the same internal structure:

- Card title: just the jurisdiction's law name (e.g., "Illinois HB 3773").
- Citations directly under the title (no divider line).
- Lede: one short paragraph in plain language summarizing what the law does.
- Field rows for the structural facts: effective date, covered employers, covered decisions, AI definition.
- "Compliance requirements" subhead, then numbered field rows (1. Notice requirements, 2. Audit / anti-discrimination, etc.) with the actual obligations.

Be ruthless about cutting words. The deep dive is supposed to be skimmable. Bullets > paragraphs where possible, but don't bullet-fragment a sentence that reads better as prose.

**HTML pattern for multiple deep-dive tabs:** the template has one `<div class="top-panel" id="illinois-panel">` containing one `<div class="il-card">`. To add more, duplicate the entire panel block, change the `id` (e.g., `id="california-panel"`), update the matching top-tab button's label and `data-target`, and fill in the new jurisdiction's content. The `il-card` CSS class is generic — keep it as-is on every deep-dive card regardless of jurisdiction.

## Footer

- Numbered footnotes (e.g., for the "25+ states" tracker citation).
- Closer line: "For practitioner use only, not legal advice." No em dash.

## What NOT to do

- Don't add a "Sources" mega-section at the bottom listing every link on the page. Citations live where the claims live.
- Don't add a "How to use this dashboard" intro. The structure should be self-explanatory.
- Don't add a recommendation column. The dashboard reports what the law says; it doesn't tell employers what to do.
- Don't use em dashes (`—`) in body content. Use periods, semicolons, colons, parentheses, or hyphens.
- Don't introduce abbreviations without expanding them on first use within a cell.
