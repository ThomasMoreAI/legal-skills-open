# English Linguistic Patterns — Reference

Loaded when the audit reaches Step 3 and the document language is English.

This file inventories the patterns that legal-design practice (after Wydick, Garner, Kimble, Tiersma, Adler) treats as drafting debt. The job is to **detect**, **count**, and **score** — not to rewrite.

## Patterns to detect

### 1. Archaic legalese

Words and phrases that survive in legal English without doing legal work. The drafter could remove them with no loss of meaning. Flag each occurrence.

- **Here-words.** *herein, hereinafter, hereto, herewith, hereunder, hereinabove, hereinbefore, heretofore.*
- **There-words.** *therein, thereof, thereto, thereafter, theretofore, thereunder, therewith.*
- **Where-words.** *whereas (outside the recitals position where it has a conventional function — only flag when used midstream), whereof, whereby, wherein.*
- **Said / aforesaid / aforementioned.** Used as a definite article surrogate. Flag every occurrence.
- **Witnesseth.** Recital-block survival from medieval drafting. Flag.
- **Such (used as a definite article).** "Such Party shall…" where "the Party" or "that Party" would do. Flag clause-by-clause; not every "such" is wrong, only the determiner-substitute use.
- **Provided that / provided however.** Often used to introduce material limitations on the operative clause. Not always wrong, but high-frequency use is a signal of poor structure. Count occurrences.
- **Notwithstanding.** Permitted in moderation; flag if the document uses it more than once per ~1,500 words.
- **Subject to / without prejudice to.** Same — moderation, not absence, is the standard.
- **Doublets and triplets.** *null and void; cease and desist; aid and abet; give, devise and bequeath; covenant and agree; alter, modify or amend; any and all; full force and effect; final and binding; terms and conditions.* Each survival of redundancy is a drafting debt.
- **Latin and law-French survivals outside terms of art.** *inter alia, mutatis mutandis, ipso facto, force majeure* — *force majeure* and *mutatis mutandis* have genuinely no English equivalent and are usually fine; *inter alia* and *ipso facto* almost always have plain alternatives ("including", "automatically"). Flag the latter category.

**Counting.** Compute an Archaism Density = (occurrences of flagged items) / (total words) × 1,000. Interpretive bands:

| Archaism Density (per 1,000 words) | Band |
| --- | --- |
| 0–2 | Green |
| 3–5 | Yellow |
| 6–9 | Amber |
| 10+ | Red |

### 2. Passive voice

Passive voice is not categorically wrong, but its **density** is a reliable signal of bureaucratic drafting. Count every finite passive construction (auxiliary "be" + past participle: "shall be deemed", "is hereby agreed", "was notified", "has been served").

Exclude:
- True agentless passives where the agent is unknown or irrelevant (e.g., "the document was signed in 1995").
- "Be" as a copula with an adjective ("shall be liable", "is responsible"). Those are stative, not agentive passives.

Compute Passive Density = (finite passive constructions) / (total finite verbs) × 100, expressed as a percentage.

| Passive Density | Band |
| --- | --- |
| 0–10% | Green |
| 11–20% | Yellow |
| 21–30% | Amber |
| 31%+ | Red |

For B2B sophisticated-party contracts, shift each band threshold up by 5 percentage points (passives are genre-typical).

### 3. Nominalization

Nominalization is the conversion of a verb into a noun phrase: "the determination of" instead of "to determine", "the imposition of liability" instead of "imposing liability", "make payment of" instead of "pay", "give consideration to" instead of "consider". Heavily nominalized prose forces the reader to reconstruct the action.

Detection signals (count instances):

- Noun-phrase verbs in *-tion, -ment, -ance, -ence, -al, -ity, -ure, -age* following empty verbs ("make", "give", "provide", "effect", "perform", "undertake", "have", "be"). Examples: *make a determination, give notification, provide indemnification, effect cancellation, perform the calculation, undertake the assessment, have an obligation, be in receipt of.*
- "The X of Y" structures where X is a derived noun and Y is the natural agent or object: *the resolution of the dispute, the execution of this Agreement, the termination of the relationship.*

Compute Nominalization Density = (flagged constructions) / (total words) × 1,000.

| Nominalization Density (per 1,000 words) | Band |
| --- | --- |
| 0–4 | Green |
| 5–9 | Yellow |
| 10–14 | Amber |
| 15+ | Red |

### 4. Sentence length

Long sentences are the single highest-impact problem. Compute:

- Mean sentence length in words.
- Median sentence length in words.
- Number of sentences over 40 words ("long sentences").
- Number of sentences over 60 words ("very long sentences").
- The longest sentence in the document, with its location.

| Mean sentence length | Band |
| --- | --- |
| 0–18 | Green |
| 19–24 | Yellow |
| 25–32 | Amber |
| 33+ | Red |

Note: mean and median should be reported together. A median of 18 with a mean of 32 indicates a few very long sentences dragging the average — that is itself a structural problem and should be flagged.

### 5. Doubled negatives and "not unless" constructions

*"No Party shall not, except in circumstances where it is not unreasonable to do so, fail to provide notification..."* Each layer of negation increases comprehension cost roughly linearly. Detect:

- "not un-" prefixes used as a hedge.
- "no … shall not", "shall not … unless".
- Triple-negative chains (rare but devastating).

Count per 1,000 words. Even one chain is usually Amber; two or more is Red.

### 6. Word and phrase length

Per Wydick's longstanding heuristic, prefer the shorter word where it conveys the same meaning. Flag the high-frequency offenders:

- *utilise / utilisation* → use.
- *prior to* → before.
- *subsequent to* → after.
- *in the event that / in the event of* → if.
- *for the purpose of* → for.
- *in order to* → to.
- *with respect to / with regard to / in relation to* → about / on / for.
- *due to the fact that / by reason of / by virtue of* → because.
- *at the present time* → now.
- *in the absence of* → without.
- *commence / commencement* → begin / start.
- *terminate / termination* → end (where context allows).
- *furnish* → provide / give.
- *render* → make / give.
- *endeavour* → try.

Count occurrences and present as a "low-hanging fruit" table; this feeds into the linguistic-patterns score as one of the inputs but is also useful in the prioritised attention list.

### 7. Cross-reference density

Count internal cross-references ("as defined in clause 4.2", "as set forth in Schedule B", "subject to clauses 7 through 11"). Cross-references are unavoidable in long contracts but become a navigation burden past a threshold:

- Cross-references per 1,000 words: 0–5 Green; 6–10 Yellow; 11–18 Amber; 19+ Red.

Flag specifically:
- Chains (a cross-reference to a clause that itself cross-references onward).
- Cross-references to schedules or appendices that are not attached or not provided.

## Pillar score for Linguistic Patterns (English)

Combine the seven sub-scores using equal weights, then map to 0–100:

1. Archaism Density
2. Passive Density
3. Nominalization Density
4. Sentence length (mean)
5. Doubled negatives
6. Word/phrase length (Wydick offenders, normalised per 1,000 words)
7. Cross-reference density

Each sub-score is converted to a 0–100 component:

- Green band of that metric → 90.
- Yellow → 70.
- Amber → 45.
- Red → 20.

Pillar score = mean of the seven components. Round to integer.

## What you report in the pillar table

Per flagged passage, include:

| # | Pattern | Quote (verbatim) | Location | Severity | Note |
| --- | --- | --- | --- | --- | --- |
| 3.1 | Archaic legalese | "Whereas the Parties have heretofore entered into…" | Recital A | Yellow | "heretofore" supplies no legal work; "previously" suffices. |
| 3.2 | Long sentence (78 words) | "[full text]" | Clause 12.3 | Red | Single sentence with 4 subordinations; consider splitting into 3. |
| 3.3 | Passive density 34% | — | document-wide | Red | See aggregate count in summary; clause 8 alone has 7 passives in 11 finite verbs. |

Verbatim quotes are mandatory. If a quote would exceed 25 words, truncate with "…" but keep enough context that the reader can locate it.

## Sources informing this reference

- Wydick, Bryan A. *Plain English for Lawyers* (current edition).
- Garner, Bryan A. *Garner's Modern English Usage*; *The Redbook: A Manual on Legal Style*.
- Kimble, Joseph. *Lifting the Fog of Legalese*.
- Tiersma, Peter M. *Legal Language*.
- Adler, Mark. *Clarity for Lawyers*.

You do not need to cite these in the report; they support the standard, not the finding.
