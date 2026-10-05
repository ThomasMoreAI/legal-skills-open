# United States (federal) — eCFR, govinfo, Federal Register

```json
{
  "code": "US-FEDERAL",
  "name": "United States (federal regulations)",
  "publisher": "www.ecfr.gov",
  "publisher_name": "Office of the Federal Register and the Government Publishing Office",
  "also_official": [
    {"host": "www.govinfo.gov", "role": "the official annual CFR, and the Federal Register as published"},
    {"host": "uscode.house.gov", "role": "the US Code, Office of the Law Revision Counsel"}
  ],
  "consolidated_text": "yes — the eCFR, current daily, and it says on itself that it is unofficial",
  "authentic_languages": ["English"],
  "citation_format": "16 CFR 312.2; 90 FR 16977 for the rule as published",
  "preferred_url_form": "https://www.ecfr.gov/current/title-{t}/part-{p}  (current)  |  https://www.ecfr.gov/on/{yyyy-mm-dd}/title-{t}/part-{p}  (point in time)  |  https://www.ecfr.gov/api/versioner/v1/full/{yyyy-mm-dd}/title-{t}.xml?part={p}  (XML)  |  https://www.govinfo.gov/link/cfr/{t}/{p}?year={yyyy}  (official annual edition)",
  "markers": [
    {
      "name": "ecfr-point-in-time",
      "severity": "superseded",
      "pattern": "Displaying the eCFR in effect on\\s+(\\d{1,2}/\\d{1,2}/\\d{4})",
      "note": "You are on a historical snapshot, not today's text. Fine if you asked for it — record --historical-effective and --research-date at the version step and say so in the note. Otherwise refetch /current/."
    },
    {
      "name": "ecfr-unofficial",
      "severity": "info",
      "pattern": "This content is from the eCFR and is authoritative but unofficial",
      "note": "The publisher's own words, on every eCFR page. This is the current text and it is not the official one. See the three-text problem below."
    },
    {
      "name": "ecfr-currency",
      "severity": "info",
      "pattern": "Displaying title (\\d+), up to date as of\\s+(\\d{1,2}/\\d{1,2}/\\d{4})",
      "note": "How current the eCFR's copy of this title is. It runs a few days behind today; date it in the note."
    },
    {
      "name": "ecfr-last-amended",
      "severity": "info",
      "pattern": "Title \\d+ was last amended\\s+(\\d{1,2}/\\d{1,2}/\\d{4})",
      "note": "The most recent amendment written into this title. Paired with ecfr-currency it brackets what you are reading."
    },
    {
      "name": "cfr-part-source",
      "severity": "info",
      "pattern": "<HED>Source:</HED>\\s*<PSPACE>\\s*([^<]*?)\\s*<",
      "note": "The part's Source credit: where it was first published in the Federal Register and where it was last amended. This is the consolidation date for a CFR part, and in the XML it is the only version fact there is. Anchored to the element so it reports the PART's credit, not the first section credit it happens to meet."
    },
    {
      "name": "cfr-annual-edition",
      "severity": "info",
      "pattern": "Revised as of ([A-Z][a-z]+ \\d{1,2}, \\d{4})",
      "note": "You have the official annual CFR. It is official and it is frozen at this date — by construction up to twelve months behind the law. Check the year is the one you meant."
    },
    {
      "name": "cfr-annual-amendments-through",
      "severity": "info",
      "pattern": "<AMDDATE>\\s*([^<]+?)\\s*</AMDDATE>",
      "note": "Amendments incorporated into the annual edition run only to this date, which is EARLIER than the 'Revised as of' date on the same title page. The two are not the same fact."
    }
  ]
}
```

## The three-text problem

The EU has two texts and neither is both current and authoritative. The US has
three, and the split runs the same way.

- The **eCFR** is current, updated daily. It prints on every page, verbatim:
  *"This content is from the eCFR and is authoritative but unofficial."*
- The **annual CFR** on govinfo is the official codification. Each title is
  revised once a year — title 16 as of 1 January — so on any given day it is up
  to twelve months out of date. Verified on the 2024 title 16 volume: it carries
  `Revised as of January 1, 2024` and, on the same title page,
  `<AMDDATE>Nov. 13, 2023</AMDDATE>`. Those are different dates and both are
  true: the edition is dated January, the amendments in it stop in November.
- The **Federal Register** notice is where the rule was actually published, and
  it is what the codified text is a codification *of*. When a point turns on
  exact wording, the FR notice is the thing to read.

So: read the eCFR to know what the rule says today. Cite the CFR section. If
money rides on the wording, pull the FR notice named in the Source credit.

"Authoritative but unofficial" is a strange phrase and it is doing real work. It
means the Office of the Federal Register stands behind the content and has not
put it through the statutory codification process. It is not a disclaimer you
can wave away, and it is not a reason to prefer a year-old text either.

## The Source credit is the only version fact that survives into the XML

This is the trap that matters most here, and it is the opposite of the UK's.

The eCFR **HTML** page carries version furniture: the unofficial banner, the
`up to date as of` date, the `last amended` date. The eCFR **XML**, which is what
you want for extraction because it is structured, carries **none of it**. Not one
date. Verified on 16 CFR part 312 at two dates — the 2024 XML and the 2026 XML
are byte-different and neither says which is which.

The one thing in the XML that changes with the version is the part's Source
credit, in `<SOURCE><HED>Source:</HED>`:

    Source: 78 FR 4008, Jan. 17, 2013, unless otherwise noted.            (2024)
    Source: 78 FR 4008, Jan. 17, 2013, as amended at 90 FR 16977,
            Apr. 22, 2025, unless otherwise noted.                        (2026)

Take it from that element and not from the first `FR` citation in the file.
Sections carry their own bracketed credits — `[78 FR 4008, Jan. 17, 2013, as
amended at 78 FR 76986, Dec. 20, 2013]` sits in both versions — and a pattern
that matches any of them reports whichever came first, which is a different fact
in each file and looks like a version difference when it is not.

So if you fetch XML, the date you asked for lives only in the URL you typed, and
the date you got lives only in that credit line. Fetch
`https://www.ecfr.gov/api/versioner/v1/titles.json` alongside it and record
`up_to_date_as_of` for the title. Without that, an eCFR XML file on disk is a
text with no provenance, which is the one thing this skill will not produce.

## Point-in-time addressing is first class

    /current/title-16/part-312          today
    /on/2024-01-01/title-16/part-312    the eCFR as it stood that day
    /api/versioner/v1/full/2024-01-01/title-16.xml?part=312

The historical page says `Displaying the eCFR in effect on 1/01/2024.` and drops
the `up to date as of` line entirely. That pair is what the markers separate, and
both were verified firing and staying silent.

This answers "what did the rule say when the client did the thing", which is the
question enforcement work actually turns on and which no secondary source can
answer.

## Getting the bytes

- **The eCFR HTML app refuses a bare product-token User-Agent.** It answers a
  redirect to `unblock.federalregister.gov`, which `fetch_source.py` catches as a
  publisher-assertion failure. The `Mozilla/5.0 (compatible; ...)` form the script
  now sends is accepted. The **API is not gated** either way.
- **govinfo answers HTTP 200 with an error page** for a package it does not hold,
  and the redirect stays on `www.govinfo.gov`, so the publisher assertion passes
  and 44 KB of Drupal lands on disk looking like a document. `fetch_source.py`
  reports the path change; read the saved bytes before quoting from them. Use the
  link service rather than guessing granule ids:
  `https://www.govinfo.gov/link/cfr/16/312?year=2024` redirects to the right PDF.
- **Bulk XML** for an annual volume:
  `https://www.govinfo.gov/bulkdata/CFR/2024/title-16/CFR-2024-title16-vol1.xml`.

## Statutes are a different system with a different trap

The US Code is published by the Office of the Law Revision Counsel at
`uscode.house.gov`, and it is the one place the positive-law distinction bites:

- Titles enacted into **positive law** are themselves the statute. Cite the Code.
- Titles that are not are **prima facie evidence** of the law. The Statutes at
  Large are the law, and where the two differ the Statutes at Large win.

So "15 U.S.C. 6501" may be a citation to the law or a citation to evidence of the
law, depending on the title. The OLRC says which on the title's front page. If a
point turns on the words of a non-positive-law title, the Statutes at Large
citation is the one to check.

`uscode.house.gov` did not respond from this machine on 2026-08-24. govinfo
carries the same material in `USCODE-` packages if it stays unreachable.

## Also worth knowing

- **The agency's rule is not always in the CFR.** Guidance, enforcement policy
  statements and no-action positions sit outside the Code entirely and are not
  law, however much everyone behaves as though they were. Do not quote them in an
  operative position.
- **Effective dates live in the FR notice, not the CFR.** The codified text says
  what the rule is; the preamble to the FR notice says when it starts and who it
  applies to during a transition. Codification drops the preamble.
- **Titles revise on different dates** — 1 January, 1 April, 1 July, 1 October by
  title group. "The current CFR" is not one date.
- **State law is not preempted by silence.** A federal rule that does not mention
  the states has not displaced them. Preemption is its own question and the
  instrument rarely answers it.
