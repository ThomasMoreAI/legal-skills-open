---
name: meturgaman-oranburg
title: Meturgaman
description: Answer questions about Jewish law, thought and practice from fetched primary sources, and retrieve modern Israeli legislation in Hebrew with its English translations ranked by authority. Locate where the tradition works a question, fetch Hebrew, Aramaic and Yiddish texts from Sefaria with their editions and licences, walk sugyot and commentary chains, explain terms, romanize under any of eight published standards, tell which standard a text already uses, and hear a passage read aloud. For Israeli statutes, fetch the consolidated Hebrew with its revision id, name where an authorized English text can be had, parse a delivered translation into sections, pair Hebrew to English on the section number, and reconcile competing witnesses. Use whenever someone asks what Jewish texts say about a topic, wants a passage or dispute explained, needs Jewish primary sources retrieved, quoted, transliterated or checked, or needs an Israeli statute, its official English translation, or a bilingual
  statutory page.
author: Oranburg
author_url: https://github.com/Oranburg/meturgaman/tree/main/skills/meturgaman
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: general
language: en
---

# Meturgaman

A *meturgaman* is the person who stood beside the reader and rendered the text
for the congregation. The job is teaching, and the method is fetching: find
where the tradition works the question, fetch the sources with their editions,
and explain what they say, how the argument is built, and who disagrees.

Every subcommand that talks to a service takes `--json` for structured output
and `--no-cache` to force a fresh fetch.

## The rule that governs everything else

**Never supply a Hebrew text from memory.** Fetch it. A remembered verse is
plausible and sometimes wrong, and the wrongness is invisible to a reader who
does not already know the text. Every passage this produces has a citation, an
edition, and a licence attached.

The same applies to vowels. Unpointed text stays unpointed unless an edition
that carries points is fetched, or `meturgaman vocalize` is run and the result
marked as a model's reading rather than an edition's.

Four disciplines that exist because answers without them failed audits:

- **No census without an enumeration.** Do not say a work does something "in
  nine places" unless you counted the places from data.
  `meturgaman anchors "Work Title"` prints every populated anchor with its
  segment count; run it before any sentence that counts.
- **No dressing your reading in the tool's authority.** Report what a command
  returned; argue your interpretation as your interpretation.
- **Copy references exactly as fetched.** Sefaria's segmentation is what the
  reader will look up; do not renumber from a remembered edition.
- **A search snippet is a lead, not a source.** Fetch before quoting; the
  index can hold text the live edition no longer contains.

Structure, framing and comparison are the job, not a violation of it. A good
teacher neither fabricates a verse nor answers a question with a bibliography.

## Answering a question about a subject

1. Topics beat search for anything anyone has thought about before:

       meturgaman topics charity          # find the slug: `tzedakah`, not `charity`
       meturgaman sources tzedakah --text # the curated passages, with their text
       meturgaman search "ribbit" --filter Halakhah   # only when no topic fits

2. Fetch each source properly, so it arrives with its edition:

       meturgaman text "Bava Metzia 75a:3-75b:12" --full

3. Walk the transmission. The link graph knows what was built on a passage:

       meturgaman chain "Mishnah Bava Metzia 5:11"   # the whole shelf, in order
       meturgaman links "Bava Metzia 75b:2" --category Commentary
       meturgaman related "Bava Metzia 75b"          # counts, topics, sheets

   A halakhic question runs Torah, Mishnah, Gemara, Rishonim, the codes, then
   responsa; reading the chain down shows where a Gemara's law lands, reading
   it up shows where a code's ruling began. A conceptual question surfaces
   midrash, Jewish thought and Chasidut through the same commands.

4. Name the disagreement. Say who holds what, on what grounds, and what turns
   on it. Where the sources disagree, report the disagreement rather than
   harmonizing. Where you found nothing, say you found nothing.

## Modern Israeli law

The classical library and the Israeli statute book are the same problem in
different clothes. There, the risk is a Hebrew text supplied from memory. Here,
the Hebrew is usually the easy part and the English is the trap, because an
unattributed web copy of a statute reads exactly like an authorized translation
and nothing on its face separates them.

    meturgaman law statutes                    # the registry
    meturgaman law tiers                       # the authority ladder
    meturgaman law sources remedies-1970       # where an English text can be had
    meturgaman law hebrew remedies-1970        # consolidated Hebrew, with its revision id
    meturgaman law amendments remedies-1970     # which sections were amended, and by what

**Never translate a statute yourself and print it as the law.** Get the
authorized translation. The rule that governs Hebrew governs English:

> Never supply a translation from memory, and never produce one silently. A
> translation carries the authority of whoever made it, and that authority has
> to travel with the words.

### The ladder, best first

| Tier | What it is |
|---|---|
| `enacted` | The English is law, or authentic treaty text. The CISG's English is authentic under its own Art. 101. |
| `authorized` | *Laws of the State of Israel* (L.S.I.), the Ministry of Justice's own English. Authorized and **not binding**; the Hebrew governs. |
| `government` | An Israeli government body's English with no translator named. |
| `commercial` | A named publisher. A.G. Publications (Arye Greenfield), Nevo, Halachot. |
| `scholarly` | A translation printed in a law review or treatise, translator named. |
| `unattributed` | A copy on the open web with no translator. A lead, not a source. |
| `assistant` | Produced by a model. Marked as such, and never printed as the law. |

Only `enacted` and `authorized` print as the law. `commercial` and `scholarly`
print with the translator named on the page. `unattributed` is good for
confirming a section number and for deciding whether a trip to the library is
worth making, and for nothing else. A hole that stays a hole is a good outcome.

### Where the authorized English actually is

L.S.I. covers volumes 1 to 45, roughly 1948 to 1989, so a statute enacted after
that has no authorized English at all and the registry says so rather than
sending anyone to a volume that does not exist.

**HeinOnline does not hold the series**, checked inside it on an institutional
subscription 2026-08-09 by browsing rather than searching: its database picker
offers one Israeli database, Israel Law Reports, and the Foreign & International
Law Resources Database title index carries no L.S.I. among its 5,943 titles. A
print volume in a law library is the remaining route. Say that plainly instead
of fetching something weaker and letting it pass.

**What does work is the law reviews.** The *Israel Law Review* reprinted the
English of selected statutes in its Legislation section, sometimes as its own
item and sometimes appended to a commentary, and HeinOnline's Law Journal
Library holds all of it. That is how the Remedies Law (8 Isr. L. Rev. 135) and
the Contracts (General Part) Law (9 Isr. L. Rev. 282, behind Shalev's commentary
at 274) were obtained. **Browse the volume tables of contents; do not search.**
HeinOnline's full-text search silently drops the collection scope and returns
286,505 results for a phrase that has 4, while
`Page?handle=hein.journals/israel<VOL>&id=1` returns a reliable TOC every time.

**Check drift against the source, never against a guess.** `law amendments`
reads the amendment stamps the consolidated Hebrew already carries, so "the
interest amendment probably only touched damages" becomes a list. On the
Remedies Law it is § 11 alone; on the Contracts (General Part) Law it is § 25
alone, and § 25 is the interpretation section, amended three times since 1974,
so its old English and its current Hebrew are two different rules.

**Finding a law is a separate job from finding its English.** `law sources`
prints both registries. The Knesset's OData service at
`knesset.gov.il/Odata/ParliamentInfo.svc/` and the CKAN catalogue at
data.gov.il are keyless, live, and Hebrew only: fast for establishing which
instrument amended what, and no help at all with translation. Israel publishes
its legislation as structured open data and publishes no translation of it.

### The trap that costs the most

**L.S.I. prints the statute as enacted. A consolidated Hebrew text is current.**
Set a 1970 translation beside Hebrew amended in 2024 and the page prints two
different laws and calls one a translation of the other. Check every section
against the amending instruments before pairing it. Where a section has drifted,
print it with a dated note or leave it Hebrew only.

### When a machine translation is permitted, and what it costs

Almost never, and never quietly. `assistant` is the bottom of the ladder and it
does not print as the law under any circumstance. But refusing absolutely is not
the same as refusing well: where the authorized English genuinely cannot be had
and a lecturer would otherwise teach from a text he cannot read, a labelled
machine translation is better than a blank, **provided every one of these holds**:

1. The authorized text was actually searched for, and the search is recorded:
   what was looked in, what was found, and what was not.
2. A named human authorizes it. Not an inference from convenience.
3. It is recorded at tier `assistant`, with `printableAsLaw: false`.
4. It carries a disclaimer naming it as a language model's work, with its date.
5. It carries a display label, and every page showing the text shows the label.
6. It states which Hebrew it translated, by revision id, because a translation
   of a consolidated current text and a translation of the enacted text are
   different documents.

`scripts/merge-israeli-english.mjs` in the K repository enforces 3 through 6 by
refusing to write without `--machine-translation`, `--disclaimer` and
`--display-label` together, and `check-israeli-english.mjs` fails the build if
any of them is later dropped. Three deliberate flags, because this is the one
tier where a slip puts invented English on a page as somebody's law.

**Translate as statute, not as prose.** Name every term of art you chose and the
alternatives you rejected; the reader has to be able to argue with your
vocabulary. Flag every ambiguity rather than resolving it silently. Do not
smooth knotty drafting into readable English, because a statute's awkwardness is
usually the drafter's precision. A confident translation with hidden guesses is
worse than an honest one with flagged holes.

### Pairing, and reconciling

    meturgaman law parse delivery.txt --json
    meturgaman law align --hebrew numbers.txt --english delivery.txt
    meturgaman law reconcile --witness lsi=authorized:a.txt --witness web=unattributed:b.txt

`align` joins on the section number and exits non-zero on any section without a
counterpart. Pairing by position is how one short row shifts every later row
with nothing on the page to show it. `reconcile` classifies each section as
confirmed by two independent witnesses, held by one only, or disputed, and
prints both texts of a dispute rather than choosing. Two mirrors of one file are
one witness, not two.

Two shapes of Israeli statute defeat a naive read, and both are handled:

- A section's **marginal heading** is typeset in its own column, so flattening
  the columns drops it somewhere a naive read will misfile it. It is reported as
  a candidate and never merged into the text.
- A **spent provision** carries a heading and an editorial note where its body
  used to be, because a repealing or amending section's text is folded into the
  statute it changed and the consolidation then drops it. Remedies § 23 and Sale
  § 35 are both like this. The English will have text where the consolidated
  Hebrew has none, and that is correct rather than a gap.

## Walking a sugya

    meturgaman sugya "Bava Metzia 75b:2"    # the mapped passage boundary

A page is a physical unit, not an argument, and the boundary often crosses the
page. Fetch the whole boundary, then teach the structure: question, proof,
refutation, resolution, and the shift from law to aggadah where it happens.
Cite segment anchors so the reader can follow.

## Words and terms

    meturgaman word אסמכתא                  # dictionary entries, with citations

For a term of art, give the senses, show a fetched example of each, and tell
the reader how to recognize which sense is in front of them.

## Romanizing

    meturgaman romanize "כָּל־הָאָרֶץ"                 # kol-ha-’arets
    meturgaman romanize "חָכְמָה" --scheme sbl-academic

`sbl-general` is the default and the right choice for most writing. The others
exist because different venues want different things:

| Scheme | Use it when |
|---|---|
| `sbl-general` | general scholarly writing. The default. |
| `sbl-academic` | the romanization is itself the object of study and must be reversible |
| `ala-lc` | the result has to match a library catalogue record |
| `bgn-pcgn` | Israeli place names, or anything official |
| `encyclopaedia-judaica-general` | matching how a Jewish Studies reader expects to see a word |
| `encyclopaedia-judaica-scientific` | comparative Semitics. Check its output; several of its cells are alternatives |
| `yivo` | Yiddish, and the closest published thing to Ashkenazi Hebrew |
| `ala-lc-yiddish` | Yiddish for a catalogue record |

## Read the flags. They are the point.

The engine prints its output to stdout and its uncertainties to stderr. **A
flag is not a warning to dismiss.** It is the tool saying it made a decision
that orthography alone does not settle.

    qamats-may-be-short     read long, the commoner reading; a few words take short here
    sheva-after-qamats      read as vocal; some words take a silent sheva here
    sheva-undecided         cannot tell whether this sheva is pronounced
    unpointed               no vowels are written and none can be recovered
    shin-undotted           shin and sin cannot be told apart here
    script-mismatch         a Yiddish scheme was used on Hebrew, or the reverse
    source-gap              the scheme's source prints no row for this
    distinction-not-in-scheme  the scheme cannot express a distinction the text makes
    established-form        English already spells this word a settled way

When a flag fires, say so in the output. "The tool prints `qaneya`, but it
flags the sheva as undecidable from the spelling, and the received Aramaic
reading is `kanya`" is a useful sentence. Silently passing along `qaneya` is
not. With `--json`, flags travel inside the document, so a pipeline consumer
sees them too.

## Romanization as evidence about a text

    meturgaman detect "Shabbos and halachah"     # which standard
    meturgaman register "Shabbos and halachah"   # which community

- **Shabbos, Akeidas, mitzvos, halachah** are Ashkenazi. The writer is probably
  Orthodox, and probably writing for a Jewish readership rather than an academic
  one.
- **Underdotted `ḥ` with circumflexed vowels** is SBL academic. The piece is
  going to a scholarly venue with a style sheet.
- **Chanukah, Hanukkah, Ḥanukah** are three different publishing worlds looking
  at the same word.

## Never flatten someone's register

`meturgaman romanize` refuses to rewrite Ashkenazi spelling as Sephardi and
prints its evidence. This refusal exists because it happened: a folder of notes
using *Shabbos* nineteen times had *shaliach* rewritten as *shaliaḥ* throughout.
That is a change of the author's voice, not a correction.

If someone genuinely wants it, `--force` does it. Do not reach for `--force`
without being asked.

## Hearing a passage

    meturgaman audio "Genesis 1:1"          # human cantillation where it exists
    meturgaman audio "Berakhot 2a" --synth  # the local synthesizer otherwise

Recorded chanting exists for the Torah, through PocketTorah, licensed CC-BY-SA
and timestamped to the verse. It does not exist for the Talmud, and the tool
says so rather than substituting a synthesizer without mentioning it. Say which
one the listener is getting.

## Comparing editions

    meturgaman compare "Berakhot 2a"

Comparison runs on the consonantal skeleton. Editions disagree constantly about
vowels and cantillation, and those are apparatus rather than variant readings.
Report the substantive differences and leave the rest alone.

## Study files

    meturgaman study "Genesis 1:1" --tier file --output DIR
    meturgaman study "Bava Metzia 75b:11" --sugya      # expand to the mapped passage
    meturgaman study "Mishneh Torah, Foundations of the Torah 2:2" --paired
    meturgaman study "..." --vocalize                  # needs the dicta extra

`--paired` appends companion passages: `rules/pairings.md` names the pairs
and the link graph supplies the passage-level connections, with absence
reported as absence. `--vocalize` points unpointed Hebrew locally and stamps
the output as a model's reading rather than an edition's.

## Checking a draft

    meturgaman verify chapter.md

Finds every citation with Sefaria's reference finder, validates each, and
checks every Hebrew quotation of three or more words against the passages
cited in its paragraph, on the consonantal skeleton. "Not found" is a flag
to investigate, never proof of fabrication: the quoted edition may differ,
or the citation may sit in a different paragraph than the quotation.

## Calendar and daily learning

    meturgaman day --date 2026-08-08 --register a
    meturgaman calendars                    # the learning cycles
    meturgaman daf                          # today's daf yomi, fetched
    meturgaman leyning --date 2026-08-08 --triennial
    meturgaman yahrzeit 2020-03-15          # anniversaries from a death date
    meturgaman zmanim --zip 20902 --elevation 150

`--register a` gives Ashkenazi forms of the holiday names, so a writer working
in Ashkenazi register can keep the calendar in register too. Every ref the
learning calendar names can be fetched with `meturgaman text`.

## Refusing well

Refuse, and say why, when:

- A citation does not resolve. Run `meturgaman candidates "..."` and offer the
  list. Do not guess at which one was meant; the top hit is often wrong.
- The text is unpointed and someone wants it romanized precisely. Offer to fetch
  a pointed edition, and name one.
- A licence is restrictive and the request is to quote at length. The tool
  reports each edition's licence; pass that on.
- Someone asks what a passage says and it cannot be fetched. Say that, rather
  than answering from memory.

## Where the tables live

`schemes/` holds one markdown file per standard. Each carries its citation, the
grid, and a section recording every place it departs from what its source prints
and why. When output looks wrong, read the scheme file first: the tables are
documents on purpose, so that checking one means reading a page rather than
reading code.
