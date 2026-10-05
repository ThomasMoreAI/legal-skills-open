# European Union — EUR-Lex

```json
{
  "code": "EU",
  "name": "European Union",
  "publisher": "eur-lex.europa.eu",
  "publisher_name": "EUR-Lex, Publications Office of the European Union",
  "consolidated_text": "yes — but formally without legal effect (see below)",
  "authentic_languages": ["all 24 official languages, equally authentic"],
  "citation_format": "Regulation (EU) 2024/1689 ... (Artificial Intelligence Act), OJ L, 2024/1689, 12.7.2024",
  "preferred_url_form": "https://eur-lex.europa.eu/eli/{type}/{year}/{number}/oj  (original)  |  .../{year}/{number}/{yyyy-mm-dd}  (consolidated)",
  "markers": [
    {
      "name": "superseded-by-consolidation",
      "severity": "superseded",
      "pattern": "Current consolidated version:\\s*(\\d{2}/\\d{2}/\\d{4})",
      "note": "You are reading the original OJ text. A later consolidation exists at the date captured — refetch it before quoting anything operative."
    },
    {
      "name": "act-has-been-changed",
      "severity": "superseded",
      "pattern": "In force:\\s*This act has been changed",
      "note": "EUR-Lex is telling you this text has been amended since publication."
    },
    {
      "name": "consolidated-no-legal-effect",
      "severity": "info",
      "pattern": "This text is meant purely as a documentation tool and has no legal effect",
      "note": "Correct version to READ. Not the version to CITE as authority — see the two-text problem below."
    }
  ]
}
```

## The two-text problem

This is the thing to get right, and it catches people who have practised EU law
for years.

- The **OJ text** is authentic. It is also frozen at publication, so for any
  amended instrument it is usually **not what is in force**.
- The **consolidated text** is what is in force. EUR-Lex prints on it, verbatim:
  *"This text is meant purely as a documentation tool and has no legal effect.
  The Union's institutions do not assume any liability for its contents. The
  authentic versions of the relevant acts, including their preambles, are those
  published in the Official Journal of the European Union."*

So neither text alone is both current and authoritative. Read the consolidated
version to know what the law says today. Cite the OJ text of the base act plus
the amending acts for authority. If a point turns on exact wording and money is
riding on it, check the wording in the OJ text of the amending act itself — the
consolidation is an editorial product and carries no guarantee.

A note that quotes the consolidated version without saying so is quoting a
document its own publisher says has no legal effect.

### The consolidated text has no recitals

Verified on the AI Act, 2026-08-23. The OJ text carries 180 recitals; the
consolidated text at `02024R1689-20260727` carries **none** — it opens at the
title block and goes straight to Chapter I, Article 1.

So the division of labour is forced, not optional:

- Reading what the law **says** today → consolidated.
- Reading what the law **means** — purpose, context, the reasoning the CJEU will
  reach for → the OJ text, because that is the only place the recitals exist.

A run that fetches only the consolidated version has silently dropped the entire
interpretive apparatus. If a question turns on purpose rather than wording, you
need both texts open.

### What the gap actually looks like

Same instrument, same day, two addresses. The OJ text has 113 Articles and 13
Annexes. The consolidated text has 119 Articles and 14 Annexes. The six that do
not exist at the canonical address:

    Article 4a
    Article 60a
    Article 75a   Supervisory and enforcement powers of the AI Office
    Article 75b   Commitments
    Article 75c   Non-compliance, fines and periodic penalty payments
    Article 75d   Safeguards and further specification

A lawyer advising on enforcement exposure from `eli/reg/2024/1689/oj` would not
find the enforcement articles, and nothing on the page would tell them they were
looking at an incomplete instrument except the banner they did not come to read.
This is the case the skill exists for.

The six new Articles are the visible part. Of the 113 Articles the two texts
share, **48 differ in wording** — including Article 3 (Definitions) and Article
5 (Prohibited AI practices). So the risk is not only citing a provision that was
superseded wholesale. It is quoting Article 5 accurately, from the instrument's
own canonical address, and having the wrong words.

### The consolidated text is marked up, and the markup is not wording

EUR-Lex prints consolidated texts with the amending act shown inline: `▼B` opens
material from the basic act, `▼M1` material from the first amendment, and
`►C1 ... ◄` brackets a corrigendum. It is genuinely useful — it tells you which
instrument put a sentence where it is — and `extract_provisions.py` keeps it in
the text it stores.

It is stripped before hashing, because it appears in every Article of a
consolidated text and in none of an OJ text. Left in, the comparison above
reports all 113 shared Articles as changed, which buries the 48 that are. Read
that way the two-text problem looks like total divergence, and a tool that
reports everything as changed is one the lawyer stops reading.

## URL forms, and a trap that looks like a dead link

The **ELI path form works** with a plain HTTP client:

    https://eur-lex.europa.eu/eli/reg/2024/1689/oj            original OJ text
    https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27    consolidated at that date

The **query-string forms** (`/legal-content/EN/TXT/?uri=CELEX:...`) answer
**HTTP 202 with an empty body** when no `Accept` header is sent. That reads as a
dead document and is not one. `fetch_source.py` sends the right headers; if you
ever fetch EUR-Lex by another route and get nothing back, this is why. Do not
conclude the text is unavailable, and do not fall back to a secondary source.

Consolidated versions are addressed by CELEX as `0{YEAR}{TYPE}{NUMBER}-{YYYYMMDD}`
— e.g. `02024R1689-20260727` is the AI Act consolidated to 27 July 2026. The
original page links to every consolidation it has; that link is how you learn
the date to ask for.

## Language

All 24 language versions are equally authentic. English has no priority, and
since Brexit it is nobody's sole national language in the Union. Where a point
turns on a single word, a cross-check against at least the French and German
texts is proportionate — divergences between language versions are a real and
litigated phenomenon, and the CJEU resolves them by purpose rather than by
picking a favourite.

Say in the note which language version was read.

## What is operative

Recitals are numbered and precede the Articles. They are **not operative**. They
are used to interpret the Articles and the Court leans on them heavily, but a
duty never lives in a recital. Quoting a recital as though it imposed an
obligation is the single most common error in EU regulatory writing.

Annexes are operative and are frequently where the thresholds, the lists and the
technical criteria actually sit — the Article often does nothing but point at
one. Never treat an Annex as an appendix.

## Also worth knowing

- **Corrigenda** are published in the OJ and silently folded into consolidated
  texts. If a point turns on wording that seems odd, check whether a corrigendum
  moved it.
- Regulations apply directly; Directives require national transposition, so a
  Directive on its own never answers whether a client is caught in a given
  member state. If the instrument is a Directive, the transposing national
  measure is the operative text and the EU instrument is only the frame.
- Commission implementing and delegated acts carry much of the operative detail
  and are separate instruments with their own dates.
