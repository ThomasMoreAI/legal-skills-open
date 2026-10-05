# Construction rubric

How this skill reads an instrument, and what it may say about what it read.

The sourcing half of the job — the right text, the right version — is governed by
`version-check.md`. This file governs everything after that: what the words mean,
which words are operative, and the line the skill does not cross.

## The answer and judgment boundary

Explain what the verified law requires and connect it to established facts or
explicit assumptions. Answer legal-requirements questions directly. A duty can
be stated even when whether particular conduct complied with it remains open.
Distinguish statutory duties, non-binding official guidance and additional
contractual obligations; identify the source of each.

Do not decide disputed facts, resolve genuinely competing interpretations by
assertion, or supply a verdict on an evaluative standard. Name the judgment and
what evidence would resolve it. Questions are for unresolved points, not facts
already supplied. The answer must not require the lawyer to synthesise a pile
of quotations before discovering the duty.

## Reading rules

These are the habits that separate a lawyer reading an instrument from a
competent reader of English reading an instrument. Apply all of them, every run.

### Recitals are not operative

Recitals are numbered, they are written in the same register as the Articles,
and they are frequently the clearest statement of what the instrument is trying
to do. A duty never lives in one. Courts lean on them to interpret the Articles
and will not enforce them.

`extract_provisions.py` classes every provision, so this is mechanically
checkable: **nothing classed `recital` may be quoted in an operative position.**
Quote a recital to say what the instrument is *for*; never to say what someone
must *do*. When you cite one, say it is a recital in the same breath.

The UK analogue is a provision tagged **Prospective** — it looks operative, it is
printed in place, and it binds nobody. Same rule, same reason.

### Defined terms are not plain English

This is the most reliable way to be confidently wrong. Instruments define
ordinary-looking words — "provider", "undertaking", "service", "establishment",
"processing", "control" — and the defined meaning routinely excludes things the
English word plainly covers, or includes things it plainly does not.

`provisions.json` carries a `defined_terms` index: every term the instrument
defines and where. Use it. **Before relying on any word in a provision, check
whether the instrument defines it.** If it does, the definition is the operative
text and the provision you were reading is a pointer to it.

Two follow-ons that catch people:

- A term may be defined **for one Part only**. "In this Chapter, X means..."
  does not travel.
- A term may be defined **by another instrument entirely**, by reference. That
  reference is a dependency: the definition can be amended without this
  instrument changing a character. Say so when it happens.

### Annexes and schedules are operative

The Article often does nothing but point at one. The thresholds, the lists, the
technical criteria and the categories usually sit in the Annex or the Schedule,
and that is where amendments land, because amending an Annex is procedurally
easier than amending the body. Never treat one as an appendix.

### "Subject to" and "notwithstanding" reorder everything

A provision that reads as an unqualified duty is regularly gutted by four words
at its start, or by an exemption forty articles away that never appears in a
search for the duty. Read the whole of any provision you quote, including the
opening words, and look for the exemptions before reporting the obligation.

Where a provision is qualified, the qualification is part of the quote. Quoting
the duty and omitting "subject to Article 12" is a misquote even though every
word is accurate.

### Commencement and application dates are per-provision

An instrument is not in force; provisions are, on dates, sometimes years apart,
and often on a staggered schedule inside a single instrument. Establish the date
for the provisions you are actually relying on. "The Act came into force in 2023"
is not an answer to anything.

### Scope is architectural, not local

What an instrument catches is almost never in one place. It is assembled from a
subject-matter article, a definitions article, a territorial article, an
exclusions article, a threshold in an Annex, and a transitional provision — and
any one of them can decide the question on its own. Reporting the first one you
find as though it were the test is the standard failure.

## What counts as a question worth putting

Put a question to the lawyer where:

1. **The instrument decides it.** It comes from the text and you can point at the
   exact provision. A question the instrument does not ask is not one of these,
   however sensible it is.
2. **The answer changes the outcome.** If both answers lead to the same place, it
   is background.
3. **It turns on a fact, not on taste.** Every question names the one fact the
   lawyer has to establish. If you cannot write that fact down in a sentence, the
   question is not ready.

Not these: what the client should do about it; how likely enforcement is;
whether the risk is worth taking; what a peer firm decided. Those are the
lawyer's, and some of them are the client's.

## The three kinds

File every question as exactly one. The kind tells the lawyer how much of the
work the text has already done for them.

**bright-line** — facts alone settle it. A threshold, a date, a listed category,
a named entity type, a jurisdictional trigger. Two lawyers with the same facts
and the same text get the same answer.

> *Did the undertaking's total annual turnover exceed EUR 50 million in the last
> financial year?* — the fact is the turnover figure; the text supplies the rest.

Bright-line describes the *test*, not the difficulty of the fact. A turnover
figure can be brutal to establish across a group; that difficulty belongs with
the fact, not with the kind.

**standard** — the instrument states the trigger in terms with no truth value
until a human applies judgment. "Appropriate technical and organisational
measures." "Reasonable steps." "Material effect." "By way of business."

A standard must carry a note saying **what judgment is being asked for, and
against what** — "this turns on whether the measures are proportionate to the
risk, judged against the state of the art and the cost of implementation, both of
which the provision names." Never how it comes out.

Presenting a standard as a plain yes/no question is the worst failure available
here: it manufactures certainty at exactly the provisions where the instrument
declined to give any, and it does it invisibly.

**definition-dependent** — the question bottoms out in a term defined elsewhere,
or borrowed from another instrument. Name the terms and where each is defined: a
provision id in this instrument, or a full citation to the instrument that
defines it. If a term is defined by something you have not fetched, say so. A
dangling definition that is labelled dangling is honest; an unlabelled one is a
silent hole the lawyer will never learn about.

Where a question is both, file it as a standard and name the terms anyway.

## How to phrase a question

**Put it to the lawyer, not to yourself.** "Does the client process personal data
of individuals in the Union?" — not "The client appears to process personal data
of Union individuals."

**End it with a question mark.** A cheap mechanical check that catches the drift
from question to position early, before it hardens.

**Do not build the answer into the phrasing.** "Is the client established in the
UK?" is neutral. "Is the client established in the UK, as it appears to be?" is
not. Neither is "Is the client *merely* a processor?" — the adverb is doing
argument.

**One fact per question.** If answering needs two independent facts, it is two
questions.

**Ask the narrowest question that decides the point.** "Is the client a financial
institution?" is too broad to answer. "Does the client accept deposits from the
public in the course of its business?" is the question the text actually asks.

**Use the instrument's own words for the operative terms**, even where plainer
words exist. If the provision says "undertaking", ask about the undertaking. The
lawyer needs to see the seam between the question and the text.

## Citing

Every question cites the provisions that **decide** it — not everything nearby.

Over-citing is worse than under-citing. Each citation is a tripwire at re-run
time, and a citation to a provision the question does not really turn on produces
a change the lawyer investigates and finds nothing in. A few of those and they
stop trusting the re-check, which is the product.

If a question genuinely turns on a definition in another provision, cite it. That
is a real dependency and the lawyer should be told when it moves.

Quote verbatim from the fetched text, never from a rendering of it, and never
from memory. Give the provision, and give the version the quote came from.

## Bias rule

When you cannot tell whether something is a question worth putting, **put it and
say why you are unsure.** An unnecessary question costs the lawyer a minute. A
missing one costs them the point.

This runs opposite to `/read-redline`'s bias, for the same reason: there, surfacing a
borderline change beats hiding it; here, surfacing a borderline question beats
hiding it. In both cases the human decides, and they can only decide about things
they can see.

Do not use the bias rule to pad. Ten sharp questions beat forty where thirty are
"and does anything else here apply?".

## When the instrument is genuinely unclear

Say so, in the same sentence as what makes it unclear. "The provision does not
say whether the turnover test is applied at entity or group level, and Article 4
does not define undertaking for this purpose."

Do not resolve the ambiguity by picking a reading. Do not resolve it by picking
the cautious reading either — the cautious reading is still a position, and it is
one the client may be paying a great deal not to take.

## What the first delivery must say

Give the answer first, with essential citations, assumptions and material
limitations. Supporting analysis explains the provisions' connection to the
facts, competing readings, historical findings and unanswered questions. Keep
full verification records separately. Never turn an unresolved application
judgment into either a confident verdict or a refusal to explain the duty.
