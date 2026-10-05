# NSW legislation method

## Source hierarchy

1. Use the [official NSW legislation website](https://legislation.nsw.gov.au/),
   managed by the NSW Parliamentary Counsel's Office, for identity, collection,
   status, point-in-time text and legislative history.
2. Use the title's Status Information and Legislative history pages to select
   and explain the applicable version.
3. Use the official HTML or PDF text for the requested provision. Use the
   official XML export for reproducible inspection when useful.
4. Use original and amending legislation plus the recorded commencement
   information to resolve exact historical or provision-level questions.
5. Treat search engines and secondary services only as discovery aids. Do not
   use them to establish identity, currency or text when the official site is
   available.

## Collections and identifiers

The workflow covers the In force and Repealed collections for:

- Acts: identifiers such as `act-1987-015`.
- Statutory instruments: identifiers beginning `sl-`.
- Environmental planning instruments: identifiers beginning `epi-`.

Match the identifier to the title, type, year and number shown on the official
page. Do not infer an identifier from a title and treat it as verified.

## Official URL structure

Checked 2026-08-26: most `/view/...` routes return HTTP 403 to non-browser
clients (`/lh` and the help pages return 200). Treat the browser fallback
described below as the normal path, not the exception.

Keep the title's present collection separate from the route for the selected
version. For an established `{id}`:

- Present title page: `https://legislation.nsw.gov.au/view/html/{present-collection}/current/{id}`
- Selected historical status page: `https://legislation.nsw.gov.au/view/html/inforce/{YYYY-MM-DD}/{id}`
- Selected whole HTML: replace `/view/html/` with `/view/whole/html/`.
- Selected whole PDF: replace `/view/html/` with `/view/whole/pdf/`.
- Legislative history: append `/lh` to the relevant status-page URL.
- XML export: append `/xml` to the selected status-page URL.

For example, a title now in the Repealed collection can have an applicable
historical version at an `inforce/<date>` URL. The date requests a point in
time; neither the route nor the date proves that the title operated then.
Confirm the resulting version and its effective range from the page. Do not
cite an unopened generated URL as evidence. If an exact-date URL cannot be
opened, an accessible official page for the identical displayed version and
the official table of versions can establish its date range when the fallback
is disclosed.

## Rules that prevent false confidence

- Present collection and historical operation are different. A title now in
  the Repealed collection can have an applicable historical version.
- The timeline and table of versions provide point-in-time access. Confirm the
  selected page's Current or Historical label and effective date range.
- Read the Provisions in force statement. A title can display provisions that
  have not all commenced.
- Read every Status Information note relevant to the request. In particular,
  distinguish an amendment excluded because it has not commenced from a Bill
  appearing under "See also".
- The site describes an update lag after a change (the exact wording was
  not located on the help pages on 26 August 2026; confirm it there).
  Recent commencement or amendment activity can therefore
  prevent an unqualified current-status result.
- Legislative history contains the table of versions, original and amending
  legislation, commencement information, history notes and creation history.
  Use the relevant part rather than assuming the latest text answers a
  historical question.
- A point-in-time title-level check does not establish that a particular
  provision commenced, applied without transition, or had the asserted legal
  effect.

## Authorisation boundary

The official authorisation guidance states that HTML and PDF versions of all
titles in the In force and Repealed collections, including historical
versions, are authorised under section 45C of the Interpretation Act 1987
(NSW). The same page also authorises as-made PDFs from 2000 and Government
Gazette PDFs from 2001, which this workflow does not use.

Do not extend that statement to content the guidance excludes, including:

- Bills.
- PDF versions of as-made titles before 2000.
- Maps associated with environmental planning instruments.
- Documents adopted by reference in NSW legislation.

This workflow deliberately excludes Bills, Gazettes and as-made-only checks in
version 0.1. If the requested proposition depends on excluded content, report
the boundary and obtain an appropriate source rather than implying that the
title's authorisation covers it.

## Additional limitations to disclose when relevant

- This workflow does not determine judicial interpretation, constitutional
  validity, application to facts, transitional or savings provisions, or the
  legal effect of incorporated external documents.
- Environmental planning instruments can depend materially on maps that are
  outside the site's authorised-content statement.
- A current title can flag future or uncommenced amendments. Those flags do not
  themselves establish when or how the amendments will affect the request.
- Website interfaces, metadata and historical coverage can change. Recheck the
  live official pages whenever the workflow is used.

## Official method sources

- [Authorisation](https://legislation.nsw.gov.au/help/authorisation)
- [Historical versions](https://legislation.nsw.gov.au/help/historical-versions)
- [Legislative history](https://legislation.nsw.gov.au/help/legislative-history)
- [Terminology](https://legislation.nsw.gov.au/help/terminology)
- [XML export](https://legislation.nsw.gov.au/help/export)

Recheck these live sources when the workflow is used.
