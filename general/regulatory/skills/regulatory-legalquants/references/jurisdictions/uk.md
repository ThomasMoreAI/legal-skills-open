# United Kingdom — legislation.gov.uk

```json
{
  "code": "UK",
  "name": "United Kingdom",
  "publisher": "legislation.gov.uk",
  "publisher_name": "The National Archives, on behalf of HM Government",
  "consolidated_text": "yes — 'revised', and revision runs behind the law (see below)",
  "authentic_languages": ["English", "Welsh for Acts of Senedd Cymru — both texts equally authentic"],
  "citation_format": "Online Safety Act 2023 (c. 50), s. 12",
  "preferred_url_form": "https://www.legislation.gov.uk/{type}/{year}/{number}  (latest revised)  |  .../enacted  (as enacted)  |  .../{yyyy-mm-dd}  (point in time)",
  "markers": [
    {
      "name": "as-enacted-text",
      "severity": "superseded",
      "pattern": "Status:\\s*This is the original version \\(as it was originally enacted\\)",
      "note": "You are on the /enacted page. This is the Act as passed, and it says nothing about what has happened to it since. Refetch the base URL without /enacted."
    },
    {
      "name": "changes-yet-to-be-applied",
      "severity": "incomplete",
      "pattern": "Changes and effects yet to be applied to",
      "note": "Amendments that are IN FORCE but not yet written into the words on this page. The text you are reading is out of date by exactly this list. Read the list."
    },
    {
      "name": "revised-to-date",
      "severity": "info",
      "pattern": "is up to date with all changes known to be in force on or before\\s+(\\d{1,2} [A-Za-z]+ \\d{4})",
      "note": "The revision date. It moves daily, so it is a fact about today's fetch and must be dated in the note."
    },
    {
      "name": "prospective-provisions",
      "severity": "info",
      "pattern": "Status:\\s*This version of this Act contains provisions that are prospective",
      "note": "Some provisions shown are NOT in force. They are printed in full, tagged 'Prospective' above the heading. Check that tag on any section you quote."
    },
    {
      "name": "revised-may-not-be-current",
      "severity": "info",
      "pattern": "Revised legislation carried on this site may not be fully up to date",
      "note": "The publisher's standing disclaimer on revised text. Carry it into the note when the analysis rests on revised wording."
    }
  ]
}
```

## Revised is not the same as current

legislation.gov.uk will tell you a statute *"is up to date with all changes known
to be in force on or before 23 August 2026"* and, further down the same page,
list under **"Changes and effects yet to be applied"** a set of amendments that
are already in force and are **not** in the text above.

Both statements are true. The editorial team applies amendments by hand, and the
backlog is public. So the revised text is the law as far as it has been typed up.
The gap is the list, and the list is on the page.

That is why `changes-yet-to-be-applied` stops the run. It is the only UK marker
that means the words you just read are wrong.

## Prospective provisions are printed as though they were law

Where an Act contains provisions not yet commenced, the revised page shows them
in full, in place, with the word **Prospective** on its own line above the
heading. Nothing about the section's own text says it is inert.

This is the UK's version of the recital trap: an ordinary-looking, numbered,
operative-sounding provision that imposes no duty on anyone today. Before
quoting a section, look at the line above its heading.

## Commencement is per-section, and the page tells you

UK Acts commence in pieces, by statutory instrument, sometimes years apart. The
revised text prints the history under each section as **Commencement
Information**:

    I27  S. 17 not in force at Royal Assent, see s. 240(1)
    I28  S. 17 in force at 10.1.2024 by S.I. 2023/1420, reg. 2(e)

Read it. "The Act is in force" is not a fact about an Act; it is a fact about a
section on a date. An answer that treats Royal Assent as the operative date is
wrong more often than it is right.

## Extent

Each provision carries a geographical extent — E, W, S, NI, in any combination —
and they differ within a single Act. A provision that binds in England and Wales
may not bind in Scotland. Where a client operates across the UK, extent is a
question the text answers per section and the note must state.

Devolved legislation is on the same site under its own types: `asp` (Scottish
Parliament), `asc`/`anaw`/`mwa` (Senedd Cymru), `nia` (Northern Ireland
Assembly). Acts of Senedd Cymru are enacted in Welsh and English, both texts
equally authentic.

## URL forms

All four verified against this publisher:

    /ukpga/2023/50                        latest revised text
    /ukpga/2023/50/enacted                as enacted, frozen at Royal Assent
    /ukpga/2023/50/2024-06-01             the text as it stood on that date
    /ukpga/2023/50/section/12             one section
    /ukpga/2023/50/section/12/data.xml    the same section as XML

`{type}` is `ukpga` for a UK Public General Act, `uksi` for a statutory
instrument, plus the devolved types above. Point-in-time addressing is the
answer to "what did this say when the client did the thing" — a question that
comes up constantly in enforcement work and that no secondary source can answer.

## A trap: the page names the versions it is not

Both the revised page and the as-enacted page carry the strings *"Original (As
enacted)"* and *"Original (As Enacted or Made): The original version of the
legislation as it stood when it was enacted or made."* Those are the version
switcher and its help text — they appear whichever version you are looking at.

The only string that actually tells you where you are is the `Status:` line. A
model skim-reading for "as enacted" will conclude it is on the as-enacted page
roughly half the time it is not. This is precisely why the version check is a
regex over saved bytes and not a reading.

## Also worth knowing

- **Correction slips** are the UK analogue of a corrigendum, listed on the page
  under "More Resources" with a date. They change the text without an amending
  instrument.
- **Statutory instruments carry most of the operative detail.** An Act that says
  the Secretary of State "may by regulations specify" has told you nothing about
  the threshold; the SI has. Find it.
- **Explanatory Notes are not law.** They are useful, they are published by the
  department, and they are not evidence of what the Act means. Do not quote them
  in an operative position.
- **Retained/assimilated EU law** still sits under UK law with its own amendment
  history. If the instrument began life in Brussels, check what the Retained EU
  Law (Revocation and Reform) Act 2023 did to it before relying on the text.
