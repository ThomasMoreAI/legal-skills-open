# Federal Register method

## Source hierarchy

1. Use the [Federal Register of Legislation](https://www.legislation.gov.au/)
   title, point-in-time, All versions, Interactions and Downloads pages.
2. Use the [Register API](https://api.prod.legislation.gov.au/v1/) for
   reproducible metadata. The API is free and requires no key, but the Register
   says it remains subject to change.
3. Use legislation endnotes, amendment histories and commencement provisions
   to resolve exact historical or provision-level questions.
4. Treat search engines and secondary services only as discovery aids. Do not
   use them to establish identity, currency or text when the Register is
   available.

## Stable links

- `https://www.legislation.gov.au/<TitleID>` — latest title page.
- `https://www.legislation.gov.au/<TitleID>/<YYYY-MM-DD>` — version selected
  for a point in time.
- `https://www.legislation.gov.au/<TitleID>/versions` — series and versions.

Prefer these page links over direct document-download URLs because the page
shows whether material has been superseded, replaced or rectified.

## Rules that prevent false confidence

- A Title ID identifies the law's series. A compilation Register ID identifies
  one version. Record both.
- `InForce` title status does not prove that every provision has commenced. The
  Register can list made but uncommenced legislation as in force.
- For an as-made Act, the effective date is Royal Assent; for an as-made
  instrument, it is registration. Neither is necessarily commencement.
- Compilation periods guide version selection. For an exact proposition,
  inspect the compilation endnotes and relevant commencement material.
- A current title can have commenced but unincorporated amendments. If so, the
  displayed compilation is not a complete statement of the amended text.
- Known future amendments and amendments with an unknown future commencement
  are different. Check All versions and Interactions.
- Historical Register coverage is incomplete in some periods. Do not infer
  that a missing compilation means no law existed.
- An authorised version is an official PDF bearing the relevant authorisation
  wording. HTML and altered copies are not automatically authorised versions.
- Check the Downloads page for a replacement or rectification before relying
  on a previously downloaded document.

## Additional limitations to disclose when relevant

- This workflow does not determine judicial interpretation, constitutional
  validity, application to facts, transitional or savings provisions, or the
  legal effect of incorporated external documents.
- Legislative and notifiable instruments can also raise disallowance,
  sunsetting, enabling-law and incorporation-by-reference issues.
- A provision-level check requires the exact selected version; quoting the
  latest text does not answer a historical question.

## Official method sources

- [About the Register and authorised versions](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/about-the-federal-register-of-legislation)
- [Point-in-time search](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/how-to-use-browse-search-and-advanced-search)
- [Status, effective dates and unincorporated amendments](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/frequently-asked-questions)
- [Reading compilations and commencement](https://www.legislation.gov.au/help-and-resources/understanding-legislation/reading-legislation)
- [Stable linking and downloads](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/linking-and-downloads)
- [API and reuse](https://www.legislation.gov.au/help-and-resources/using-the-legislation-register/data-share-and-reuse)

Recheck these live sources when the workflow is used. Register interfaces,
metadata and available historical material can change.
