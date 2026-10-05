# Singapore — Singapore Statutes Online

```json
{
  "code": "SG",
  "name": "Singapore",
  "publisher": "sso.agc.gov.sg",
  "publisher_name": "Legislation Division, Attorney-General's Chambers of Singapore",
  "consolidated_text": "yes — SSO serves the text in force on a date you choose, with every earlier version addressable",
  "authentic_languages": ["English"],
  "citation_format": "Personal Data Protection Act 2012 (2020 Rev Ed), s 2(1)",
  "preferred_url_form": "https://sso.agc.gov.sg/Act/{ShortName}{Year}  (in force today)  |  https://sso.agc.gov.sg/Act/{ShortName}{Year}/Historical/{yyyymmdd}?DocDate={yyyymmdd}&ValidDate={yyyymmdd}  (point in time)",
  "markers": [
    {
      "name": "not-current-version",
      "severity": "superseded",
      "pattern": "Status:\\s*Not current version \\(effective from (\\d{1,2} [A-Z][a-z]{2} \\d{4}) to (\\d{1,2} [A-Z][a-z]{2} \\d{4})\\)",
      "note": "A historical version, and the page names the window it governed. Fine if you asked for it — that window is the answer to 'what did this say when the client did the thing'. Otherwise refetch the base URL."
    },
    {
      "name": "current-version-as-at",
      "severity": "info",
      "pattern": "Status:\\s*Current version as at (\\d{1,2} [A-Z][a-z]{2} \\d{4})",
      "note": "The text in force on the day you fetched, and the date is today's. It is a fact about the fetch, not about the Act, so it must be dated in the note."
    },
    {
      "name": "revised-edition",
      "severity": "info",
      "pattern": "(\\d{4}) REVISED EDITION",
      "note": "You are in a Revised Edition. Revised Editions restyle and renumber. A citation written against an earlier edition may not resolve here — see below."
    },
    {
      "name": "revised-edition-scope",
      "severity": "info",
      "pattern": "This revised edition incorporates all amendments up to and including (\\d{1,2} [A-Z][a-z]+ \\d{4})",
      "note": "This dates the EDITION, not the text on the page. Later amendments are woven in and this line does not move. Do not read it as a staleness warning."
    }
  ]
}
```

## The line that looks like a staleness warning and is not

Fetch the Personal Data Protection Act 2012 today and the page says two things
at once:

> Status: Current version as at 24 Aug 2026

and, at the head of the Act itself:

> 2020 REVISED EDITION
> This revised edition incorporates all amendments up to and including
> 1 December 2021 and comes into operation on 31 December 2021

A reader who finds the second line concludes the text is four and a half years
stale. It is not. The Revised Edition is the **base** the text is built on;
amendments since — for the PDPA, Act 25 of 2021, Act 40 of 2020 and Act 19 of
2025 — are already written in. The line dates the edition and never moves.

This is the inverse of the UK trap. legislation.gov.uk tells you it is current
and then lists what is missing. SSO tells you what edition it is and lets you
mistake that for currency. Both mistakes are made by reading one line.

The line that actually answers the question is `Status:`.

## Revised Editions restyle, and citations written against the old one break

Verified on the PDPA, comparing the version in force on 2 October 2016 with
today's:

    2016:  PART I PRELIMINARY
    2026:  PART 1 PRELIMINARY

The 2020 Revised Edition moved Part numbering from Roman to Arabic across the
statute book. Section numbers within the PDPA survived — s 2 is still s 2 — but
that is a fact about this Act, not a rule. How far a Revised Edition renumbers
varies by Act, and the only way to know is to look.

So a citation from a 2019 memo, an old contract's compliance schedule, or a
counterparty's policy may point at a provision label that no longer exists or
that now holds something else. Check the label against the current text before
relying on it, and when a client hands you a citation, ask which edition it was
written against.

## Point-in-time addressing, and the timeline

Every version SSO has ever served is addressable:

    /Act/PDPA2012                                    in force today
    /Act/PDPA2012/Historical/20161002?DocDate=20160929&ValidDate=20161002

`ValidDate` is the date the text was in force; `DocDate` is the date of the
document SSO is serving. They are usually different and both are needed — the
links on the Act's own timeline carry the right pair, so take them from the page
rather than constructing them.

The timeline itself is on the page and is worth reading before quoting anything.
It lists every commencement and every amending instrument with its date:

    02 Jan 2021  Amended by Act 40 of 2019
    31 Dec 2021  2020 RevEd
    05 Dec 2025  Amended by Act 19 of 2025

That column is where you see whether the provision you care about moved recently
enough that the client's file predates it.

## Commencement is per-provision and is printed at the front

Singapore Acts commence in pieces, and the Act's head note says which pieces:

> [2 January 2013: Parts I, II, VIII, IX (except sections 36 to 38, 41 and 43 to
> 48) and X (except section 67(1)), and the First, Seventh and Ninth Schedules ;
> 2 December 2013: Sections 36, 37, 38 and 41 ; 2 January 2014: Sections 43 to 48
> and 67(1) and the Eighth Schedule ; 2 July 2014: Parts III to VII, and the
> Second to Sixth Schedules ]

Read it against the provisions you are relying on, not against the Act. The PDPA
took eighteen months to come fully into force and the data protection obligations
were last.

SSO also browses statutes by status — Current, Repealed/Spent, Uncommenced — so
an Act that has passed and not started is findable and is clearly marked as such.

## Getting the bytes

SSO refuses a bare product-token User-Agent with **HTTP 403**. The
`Mozilla/5.0 (compatible; ...)` form `fetch_source.py` now sends is accepted.
If you get a 403 anyway, report it — do not fall back to a law firm's copy of
the Act, of which there are many and all of which look fine.

Subsidiary legislation is on the same site under `/SL/`, and for most regulated
activity it is where the operative detail lives.

## Also worth knowing

- **Singapore legislation is enacted in English.** There is no second authentic
  language and no translation problem.
- **Amendment Acts are separate instruments with their own numbers** (Act 40 of
  2020), and the timeline names them. When a point turns on wording, the
  amending Act is the thing that changed it.
- **The PDPC, MAS and other regulators publish advisory guidelines** that are
  detailed, influential and not law. They are excellent for understanding
  expectations and must never be quoted in an operative position.
