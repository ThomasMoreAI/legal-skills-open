# Run format

What a run puts on the screen, how it quotes, and what it leaves on disk.

`version-check.md` governs which text you may use. `construction-rubric.md`
governs how you read it and what you may say about it. This file governs the
artefact.

The quoting rules below are not a style preference. `verify_quotes.py` enforces
them mechanically, without a model in the loop, and a run that fails them is not
delivered.

## The note

The ordinary deliverable has two clearly labelled levels, in this order:

**Your answer.** Normally 150–250 words answering the actual question, with
essential citations, assumptions and qualifications. State the duties and their
connection to supplied facts. If a point is unresolved, name it and what would
resolve it. For genuinely broader questions, briefly explain any length exception.
The initial chat must surface this answer, not just link to a research file.

**Supporting analysis.** Relevant provisions and necessary quotations, their
connection to facts, competing interpretations, material historical findings and
outstanding questions. Explain the reasoning without repeating the answer.
Separate law, official guidance and additional contractual terms. Reserve
unresolved timing standards, disputed facts and dispute outcomes for judgment.

Version history leads only when it changes or prevents an answer; otherwise keep
its qualification brief. Store hashes, receipts, extraction diagnostics and full
amendment history in the verification record. Do not repeat the same issue as an
application row, outstanding question and concluding trap.

Before sending, check the actual chat and note for answer placement, length,
usefulness and verification coverage independently of research coverage. If the
source gate fails, label the affected answer **provisional and unverified** and
state the missing evidence. Never hide that status in the record or a footnote.

That label goes once, next to the answer it qualifies, and it names four things:
the source actually checked, the edition it supports, what was not verified, and
the missing fact that would change the answer. Repeated in every section it stops
being read and gives the lawyer nothing to act on. Keep separate questions
separate — whether a text is official, whether it is in force, and whether an
exception applies are three answers, not one qualification. **"Not verified as in
force" does not mean "not in force,"** and a note that lets those blur has
overstated its own uncertainty, which costs a lawyer as much as understating it.

## The comparison

`compare` starts with Your answer, then a Supporting analysis table. One row per test, one column
per jurisdiction.

The version line under each column heading is not decoration. Two jurisdictions
are never current to the same date, and a table that hides that invites the
reader to treat a stale cell and a fresh one as equally settled.

```
                        EU                          Singapore
                        consolidated 27/07/2026     in force 24 Aug 2026

Who is caught           Art. 2(1) — providers       s 4(1) — organisations
                        placing on the Union        collecting personal data
                        market                      in Singapore

Threshold               none                        none
```

Three rules, and they are the ones that get broken:

- **Never merge two jurisdictions into one statement.** "Both require notice
  within 72 hours" is a sentence about neither instrument. Each cell cites its
  own provision, from its own fetch, at its own version.
- **Never let the first jurisdiction set the frame.** If you fetch the EU first,
  the rows become EU concepts and the other columns get scored on whether they
  have them. Derive the rows from the question the lawyer asked.
- **A cell with no provision says so.** "Not addressed" and "no equivalent
  concept" are different findings, and both are more useful than an empty cell.

Each column's quotes are checked against that jurisdiction's own
`provisions.json`. A comparison is *n* runs of the spine and *n* verifications,
not one of each.

## The check note

`check` adds two things to the note, and is not deliverable without them:

- **The discovery coverage receipt** — the table from `references/discovery.md`,
  in the Supporting analysis, with its method version line (`discovery/v1`) and
  an access date for every dynamic source consulted. Unworked branches say
  **unresolved**; a first-pass receipt with nothing unresolved deserves
  suspicion, not celebration.
- **Classified negatives.** Every "nothing" names its kind: expressly excluded
  (exclusion quoted and verified like any quote), test not met (missing element
  named), nothing found after the searches the receipt lists, or not
  investigated. Mandatory refresh dates for volatile sources sit with the
  answer, not in a footnote.

## Sources

**Every run ends with the links.** Not on request, not in the saved package
only, not "available if you want them" — in the note, every time, including when
the note is only going on screen. Cites name provisions; they do not tell a
reader where to go and read one. The addresses are already in the fetch
receipts, so this is transcription, and making the reader ask for it — even
once, even cheaply — spends their time to save none of yours.

`verify_quotes.py` fails a note that does not carry the address its text was
fetched from. That check covers the official half only, because it is the half a
receipt can prove.

```
## Sources

**Official**

- Widget Safety Act 2024 — https://official.example/widget-act
  consolidated to 27/07/2026, retrieved 2026-09-06

**Also consulted**

- Ruritanian Ministry of Trade, guidance note on placing (not law; used to
  locate the Act) — https://ministry.example/guidance
- https://official.example/widget-act/part-3 — fetched first; holds Part 3 only,
  and Article 4 is in Part 2. Refetched at the address above.
```

Three rules:

- **The two lists stay separate.** The governing rule of this skill is that
  secondary sources tell you an instrument exists and only the publisher tells
  you what it says. A flat list of links says the opposite — that everything
  here is equally good — and it is the reader who pays for that, because they
  cannot tell which link they are allowed to rely on.
- **A link is the address the bytes came from.** Take it from `fetch.json`, not
  from memory and not from the search result that led you there. A retyped URL
  is a citation to a page you did not read.
- **Dead ends are listed.** The fetch that returned a real statute which did not
  contain the provision is the most useful line in the section: it is the one
  that stops the next person repeating it, and its absence is what makes a wrong
  first attempt look like it never happened.

For `compare`, each jurisdiction's sources sit under its own subheading. A
merged list re-creates in the sources exactly the confusion the table's separate
columns exist to prevent.

For `check`, the discovery receipt's evidence cells carry their own dated links.
The Sources section still lists every official fetch, so there is one place to
look, and the receipt is not silently doing two jobs.

## Quoting

### Every quotation of the instrument is a blockquote with a cite line

```
> Where a widget is found to be non-conforming, the surveillance authority may
> require its withdrawal from the market.
> — Article 4(2), consolidated to 27/07/2026
```

The cite line is the last line of the blockquote and starts with an em dash. It
opens with the provision, and then anything else you want to say — version, date,
consolidation.

Cite the provision by its label and number. House abbreviations are fine (`Art.
4(2)`, `s. 12`, `§ 1798.140`); the number is what has to be right.

### The quote must be in the fetched bytes

Not from a search result, not from a web-fetch rendering, not from memory. A
web-fetch rendering is a model's version of the page, and a paraphrase of a
statutory provision reads exactly as well as the provision. That is the whole
reason this check is mechanical.

Trailing spaces, line wrapping and the publisher's amendment markers (`▼M1`,
`►C1`) are ignored on both sides. Words are not.

### Mark every cut with an ellipsis

```
> A surveillance authority may require an economic operator to provide the
> technical documentation … within 14 days of a request.
> — Article 4(1)
```

Each fragment is checked, in order, against the cited provision. Unmarked
elision fails, which is the point: quoting a duty and silently dropping "subject
to Article 12" is a misquote in which every word is accurate.

### The cite must name the provision the words actually live in

Checked against `provisions.json`. Paragraph/subparagraph attribution is checked
only where explicit, unambiguous subdivision markers can be located; otherwise
the checker returns attribution-unverified and requires a separate check.
A match at article level alone must never be called paragraph verification. This is the error that survives review, because both
halves look right on their own.

### Recitals are cited as recitals

If the words live in a recital or the preamble, the cite says so — `Recital (2)`,
`Preamble`. A recital quoted under an article number is a duty invented in a
formatting step. `construction-rubric.md` explains why courts will not enforce
one.

### Inline quotes count

Double-quoted runs of five words or more are treated as instrument text and
checked the same way, including the cite: the paragraph they sit in has to name
the provision.

So use double quotes only for the instrument's own words. Defined terms take
single quotes — 'non-conforming widget' — and are not checked. Your own summary
of a provision takes no quote marks at all; the checker cannot tell a paraphrase
from a misquote, and will call it a misquote.

### The instrument's words never leave quotation marks

A code span, bold, or a bare run of five words or more lifted from the
instrument is a quotation with the marks taken off. `verify_quotes.py` scans
code spans and reports `unquoted-instrument-text` when the words turn out to be
the instrument's own, in either edition.

This is a rule about repair, not about typography. A quotation that fails is
fixed or cut; restyling it does neither, and it is worse than leaving the
failure in place, because the run then exits 0 over fewer checked quotations
than it began with and nothing anywhere says the coverage fell.

### A refresh quotes two editions, and says which is which

```
> permit the person, the person's legal guardian, or an attorney who presents a
> signed written authorization made by the person
> — § 1347.08(B)(2), as it read before the amendment
```

Pass the earlier run so both editions can be checked:

    python3 scripts/verify_quotes.py <later>/note.md <later>/provisions.json \
        --earlier <earlier>/provisions.json

The cite has to mark superseded text — *as it read*, *former*, *before the
amendment*, *repealed*, *previously*. Words that live only in the earlier run
and are cited without one of those fail as `superseded-as-current`. Repealed
words presented as current law are worse than a misquote: every word is genuine,
so nothing about them reads wrong.

Without `--earlier` the same quotation fails as `not-in-text` — the words are
real and the checker has only been shown one edition of the instrument. That
message is wrong, and it is the one that invites the note to be reshaped rather
than the check to be run properly.

## Verifying

    python3 scripts/verify_quotes.py <note.md> <dir>/provisions.json \
        --manifest <dir>/run.json

Exit 0 means every quote is verbatim, cited, and cited to the right place. Exit 1
lists what failed and where.

Run it on the note before the note goes to the lawyer — including when the note
is only going on screen. A quote that cannot be verified is deleted or fixed, not
caveated — and not restyled, not weakened to a vaguer pinpoint, and not moved
out of quotation marks. Those all end the complaint without touching the
problem, and they end it silently.

## What gets saved

Temporary verification uses a workspace run folder. Retain the package only
when the user asks or agrees; otherwise remove temporary files after delivery
and disclose that the package has not been retained.

When it is saved, one folder per instrument, inside the lawyer's own repo:

```
<instrument>/
  source.html        the publisher's bytes, exactly as served
  fetch.json         URL, publisher, HTTP date, retrieval time, sha256
  transformation.json  optional publisher-bytes to derived-text receipt
  version.json       the markers found and what they mean
  provisions.json    provisions, classes, hashes, defined terms, provenance
  note.md            the note as delivered
  run.json           the manifest — which provisions the note rests on
```

## The manifest

`run.json` is written by `verify_quotes.py --manifest`, and only from a note in
which every quote and the complete source lineage verified. It records the
complete preserved provision set, the provisions actually quoted, and the
unquoted semantic dependencies supplied with `--depends-on id=reason`.

`refresh` assesses the complete preserved provision set, then highlights quoted
and dependency provisions. It refuses different instrument identities and does
not claim that unchanged quotations preserve the earlier legal conclusion.

A quotation verified against the earlier run is not reliance on the later one,
so it is left out of the manifest. The manifest records what the note rests on
as current law, and a later `refresh` filtered by it would otherwise re-check
provisions this note only ever quoted in the past tense.

`source.html` is never edited. It is the thing every later claim is checked
against, and an edited copy is worth less than no copy.

Fetch again into a new dated folder rather than overwriting; `refresh` compares the
two, and it can only compare what is still there.

For derived text, `transformation.json` uses integrity schema
`regulatory-integrity/v1` and records `publisher_bytes_sha256`,
`derived_text_sha256`, `derived_name`, `method`, and the exact tool/version used.
The receipt binds the conversion; it does not claim the derivative is identical
to the publisher file.
