# California — California Legislative Information

```json
{
  "code": "US-CA",
  "name": "California",
  "publisher": "leginfo.legislature.ca.gov",
  "publisher_name": "Office of Legislative Counsel of California",
  "also_official": [
    {"host": "govt.westlaw.com", "role": "the California Code of Regulations, published under contract to the Office of Administrative Law"}
  ],
  "consolidated_text": "yes for codes — the section as it stands today, with no point-in-time addressing",
  "authentic_languages": ["English"],
  "citation_format": "Cal. Civ. Code § 1798.140; 11 CCR § 7001 for regulations",
  "preferred_url_form": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode={CODE}&sectionNum={n}  (one section)  |  .../codes_displayText.xhtml?lawCode={CODE}&division=...&title=...&part=...&chapter=...  (a run of them)  |  .../billTextClient.xhtml?bill_id={id}  (the chaptered bill)",
  "markers": [
    {
      "name": "section-credit-statute",
      "severity": "info",
      "pattern": "\\((Amended|Added|Repealed|Renumbered)[^)]{0,40}by Stats\\. (\\d{4}), Ch\\. (\\d+)[^)]{0,80}\\)",
      "note": "The section's own version line: which session law last changed it. This is the consolidation date for a California code section, and it is per SECTION — the code around it may be older or newer."
    },
    {
      "name": "section-credit-initiative",
      "severity": "info",
      "pattern": "\\(Amended [A-Z][a-z]+ \\d{1,2}, \\d{4}, by initiative Proposition (\\d+)",
      "note": "This section was last changed by ballot initiative, not by the Legislature. Initiatives usually restrict how they may be amended, and that restriction is in the initiative, not in the code section. Check it before advising that a bill could change this."
    },
    {
      "name": "effective-differs-from-operative",
      "severity": "info",
      "pattern": "Effective ([A-Z][a-z]+ \\d{1,2}, \\d{4})\\.\\s*Operative ([A-Z][a-z]+ \\d{1,2}, \\d{4})",
      "note": "Two different dates, and the gap can be years. Effective is when the enactment took legal effect; operative is when this section starts to bite. Between them the words are law and impose nothing."
    },
    {
      "name": "section-repealed",
      "severity": "superseded",
      "pattern": "\\(Repealed[^)]{0,40}by Stats\\. (\\d{4}), Ch\\. (\\d+)",
      "note": "This section has been repealed. Whatever it says above the credit line is not the law."
    }
  ]
}
```

## The version lives at the bottom of the section, and nowhere else

California is the odd one out in this registry. There is no banner, no status
line, no "current as of" date, no disclaimer. Fetch a code section and you get
the section, followed by one line in brackets:

> (Amended by Stats. 2025, Ch. 67, Sec. 27. (AB 1170) Effective January 1, 2026.)
> — Civ. Code § 1798.140

> (Amended November 3, 2020, by initiative Proposition 24, Sec. 4. Effective
> December 16, 2020. Operative January 1, 2023, pursuant to Sec. 31 of
> Proposition 24.)
> — Civ. Code § 1798.100

Both verified on 2026-08-24. That line is the whole version story, and it means
three things worth stating plainly:

1. **Version is per section, not per instrument.** Two sections of the same Act
   can have last-changed dates years apart. There is no such thing as "the
   current version of the CCPA" — there is a current version of each section.
2. **`read_version.py` matching nothing is normal here** if you fetched anything
   other than a code section. The registry expects markers that only exist at the
   foot of a section.
3. **Nothing tells you a later amendment is pending.** A chaptered bill that
   changes this section next January does not appear on the page at all. If the
   question is forward-looking, the bill history is a separate search.

## Effective is not operative, and the gap is where advice goes wrong

Section 1798.100 was effective 16 December 2020 and operative 1 January 2023 —
two years and two weeks apart. For that whole period the words were on the page,
in the code, validly enacted, and imposed nothing on anyone.

Nothing in the section's text says so. It is one clause of one bracketed line
below it.

This is California's version of the UK's prospective-provisions trap, and it is
worse, because the UK prints the word **Prospective** above the heading where you
can see it. Here it is a second date in a credit line most readers skim as
citation furniture.

Read the credit line of every section you quote. If it carries an Operative date,
that date, not the effective date, is the one that answers "when does this
apply".

## Initiatives are not ordinary statute

`Proposition 24` in a credit line is a signal to stop and look at the initiative
itself. Measures adopted by the voters commonly limit how the Legislature may
amend them — sometimes to amendments that further the measure's purpose,
sometimes by requiring a supermajority, sometimes not at all. The restriction
lives in the initiative, not in the code section it produced.

So the ordinary reasoning "a later statute amends an earlier one" does not carry
here, and a client asking whether a bill could change this section is asking a
question the code section cannot answer.

## Regulations are somewhere else entirely, and the somewhere else is commercial

The California Code of Regulations is not on `leginfo`. It is published for the
Office of Administrative Law at `govt.westlaw.com/calregs`, a Thomson Reuters
address. That is the official CCR, on a commercial host.

This breaks the shape of the rest of the registry, so it is worth being explicit:
the publisher assertion for a CCR fetch is `govt.westlaw.com`, and that is correct
rather than a failure. Note it in the run, because a reader who sees a Westlaw
domain in a provenance record will reasonably assume someone quoted a database.

Much of what a business actually has to do in California — the CCPA regulations
are the obvious case — lives in the CCR, not the code.

## Getting the bytes

**`leginfo.legislature.ca.gov` serves a certificate that recent trust stores
reject.** The chain runs to an Entrust root; Python's bundled store and `certifi`
both refuse it, while browsers and some system stores accept it. Verified
2026-08-24: `certifi` fails, `/opt/homebrew/etc/openssl@3/cert.pem` succeeds.

    SSL_CERT_FILE=/path/to/a/bundle/that/trusts/it python3 scripts/fetch_source.py ...

`urllib` honours `SSL_CERT_FILE`, so this needs no flag and no change to the
script — which is deliberate. A tool option for relaxing certificate checking is
an option someone will eventually use to get past a warning that mattered.

If you do this, **say so in the note**. Which trust store you had to use to reach
a publisher is part of the provenance of what you fetched.

## Also worth knowing

- **Chaptered bill text is the enactment.** `billTextClient.xhtml` gives the bill
  as chaptered, which is the authentic thing the code section is a codification
  of. When wording matters, that is the document.
- **`Stats. 2025, Ch. 67` is the session law citation** and `(AB 1170)` is the
  bill it came from. Both are in the credit line; the bill number is what you
  search on for legislative history and committee analyses.
- **Codes are addressed by short code, not by Act name.** `CIV`, `GOV`, `HSC`,
  `LAB`, `PEN`, `BPC`. There is no URL that means "the CCPA" — there are URLs for
  the Civil Code sections the CCPA created.
- **California legislates fast and amends by reference.** A section can be
  amended twice in one session by different bills, and the Legislative Counsel
  reconciles them. If two bills touched the same section in the same year, read
  the credit line carefully to see which one landed.
