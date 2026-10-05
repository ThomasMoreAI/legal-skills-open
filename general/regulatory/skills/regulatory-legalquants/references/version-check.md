# The version check

Read this every run, before quoting anything.

## The thing to understand first

**No publisher gives you a single text that is both current and authoritative.**
Every one of them gives you a text that is missing one half or the other, and
says so somewhere you did not look.

The two mapped jurisdictions fail in opposite directions, which is the clearest
way to see it:

|  | Current? | Authoritative? |
|---|---|---|
| EU consolidated | yes | no — *"meant purely as a documentation tool and has no legal effect"* |
| EU OJ text | no — frozen at publication | yes |
| UK revised | no — amendments in force but not yet typed in | yes |
| UK as enacted | no | yes, of the Act as passed |

So the question is never "did I get the official text". It is **which half am I
missing, and does it matter for this question**. That is the job.

## The five questions

Put these to every retrieval. Write down the answers; they go in the output.

1. **Which version is this?** As enacted / as made, consolidated or revised, or
   the text at a past date.
2. **Current to when?** The date the publisher states, in the publisher's own
   words. Not today's date.
3. **Amended since, by what?** Name the amending instruments.
4. **Any gap between the text and the law?** In two directions —
   - in force but not written in (the text you are reading is behind), and
   - written in but not in force (printed text that binds nobody yet).
5. **Is this the authentic language?** And if there is more than one authentic
   language, does the point turn on a word.

If the page will not answer one of these, that is a finding. Record it as one.
An unanswered question is not the same as a clean answer.

## The vocabulary trap

Publishers use different words for the same thing and the same word for
different things. Translate before you rely on it.

| What you want | EU says | UK says |
|---|---|---|
| the text as passed | original, OJ text | as enacted, as made |
| the text as it stands now | consolidated | revised, latest available |
| the text on a past date | consolidated at *date* | point in time |

"In force" is the worst of them. In EU law it is usually a fact about the
instrument; in UK law it is a fact about **a section on a date**, and the same
Act will have sections in force, sections repealed and sections never commenced,
all printed identically. Never let "the Act is in force" stand as an answer.

## The five failure shapes

Name the one you found. Each has a different consequence.

**Stale** — you have an earlier version. The words are right for a date that has
passed. *Consequence: everything downstream is wrong and looks fine.*

**Incomplete** — right version, but amendments already in force have not been
written into it. *Consequence: the text is wrong by exactly the list the
publisher prints below it.*

**Not yet law** — the text is printed in full and binds nobody, because it has
not been commenced or its application date has not arrived. *Consequence: advice
about duties that do not exist yet, delivered as though they did.*

**Partial** — the version you have omits part of the instrument. EU consolidated
texts drop the recitals entirely; a section-level URL drops everything that
qualifies it. *Consequence: you conclude something is absent when you simply are
not looking at it.*

**Not the text** — a translation, a summary, an editorial copy, a law firm note,
or a model's recollection. *Consequence: the whole output is unsourced and
nothing in it shows that.*

## How to run it

Mechanically first, because a reader who came for Article 6 does not read
banners and a model reading a page can miss one:

    python3 scripts/fetch_source.py <url> <dir> --publisher <host> --label "<version>" \
        --jurisdiction <code> --profile <profile> --instrument-id <stable-id>
    python3 scripts/read_version.py <dir>/source.html --jurisdiction <code> --json <dir>/version.json

Non-zero exit means a marker says this text is not what you should be quoting.
**Refetch the version the marker names.** Do not carry on and caveat it — a
caveat on a stale quote is still a stale quote.

No marker matched is not a pass. It means the page did not carry the
markers the registry expects, which usually means the publisher moved its
furniture. Establish the version by hand and fix the registry entry.

The script records this state as `unresolved` and exits non-zero. Downstream
reliance remains blocked. A superseded version may proceed only when the dated
research question and the selected historical effective date are both recorded;
that state is `historical_selected`, not `confirmed` current law.

Then the residue, which no regex does for you:

- Read the list of amendments the page names, and decide whether any of them
  touches the provisions this question turns on. Most will not. Say which do.
- Check commencement or application dates for the specific provisions you are
  relying on, not for the instrument.
- Check whether the provisions you are quoting are tagged prospective.
- Decide whether the missing half matters here. If the question turns on
  purpose, you need the recitals and the consolidated text does not have them.

## What the output must carry

Every run states its provenance in one line per text, in this shape:

> **Text:** EU AI Act, consolidated to 27/07/2026 (`02024R1689-20260727`),
> retrieved from eur-lex.europa.eu on 2026-08-24, sha256 `afb574cf424f`.
> Recitals are not in this version; recital citations are to the OJ text,
> OJ L, 2024/1689, 12.7.2024.

In the answer, mention only version differences that change or prevent it.
Keep a non-material version qualification brief and place detailed history and
fingerprints in the supporting record.

## When you cannot complete the check

Say so, in the output, in the place the reader will see it. The honest forms:

> I could not establish which version this is. The text below is from the
> publisher but undated — treat the wording as unconfirmed.

> I could not reach the publisher for this instrument. I have not quoted from
> anything else, so there are no quotes below.

Both are real answers. A confident memo built on an unestablished text is the
specific harm this skill exists to prevent, and it is indistinguishable from a
good one at the moment it is handed over.
