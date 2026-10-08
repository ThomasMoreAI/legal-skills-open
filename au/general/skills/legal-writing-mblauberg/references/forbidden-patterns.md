# Forbidden Patterns

Use this as a scrub list before filing-facing work or correspondence leaves the workspace. This file is the
legal overlay on the hub taxonomy owned by the `natural-writing` skill.
It lists only the filing-facing hard bans, affidavit-specific overreach, quotation integrity, and the
legal-register carve-outs the hub's general list would otherwise misclassify as tells (`reasonably arguable`,
formal connectives, correct passives).

The deterministic lint in `scripts/lint_legal_style.py` enforces only a subset
of this list as hard failures, including em dashes, US legalese, internal
markers, internal-path leaks and unsupported safety-instrument overstatement.
It flags style and affidavit risks as warnings. Treat this reference as the
standard and the lint as a partial check; it cannot verify sources, document
function, forum rules or most structural writing defects.

For repair procedures, use `legal-concision-and-anti-ai.md`. This file identifies patterns; the concision
reference tells agents how to fix them without losing legal precision.

## Hard Bans In Filing-Facing Text

- Em dash character U+2014, anywhere in workspace output. The en dash U+2013 is allowed but used sparingly (see `australian-english-house-style.md`); it is a lint warning, not a ban.
- Internal markers: `TODO`, `TBD`, `TBC`, `FIXME`, `drafting note`, `agent note`, `AI`, `generated`, `hallucination`.
- Source paths: `.work/`, `docs/audits/`, OCR scratch, render outputs.
- Internal leak tokens hidden in HTML comments (`<!-- ... -->`): run-dir/audit paths (`docs/audits/`),
  scratch or build paths (`.work/`, `review_set/`, scratchpad), absolute repo paths (`/Users/...`),
  internal task ids (`TASK-<AREA>-<n>`) or a superseded section-letter map. pandoc strips comments, so
  these never render but still ship in the source; the lint FAILs a comment that carries one. Editor
  notes belong in `<!-- -->` (not `>` blockquotes) and are fine when they carry no leak token.
- US date style: `May 25, 2026` or `05/25/2026`.
- US legalese: `COMES NOW`, `wherefore`, `herein`, `therein`, `heretofore`, `aforementioned`, `the undersigned`, `respectfully prays`, `Honorable Court`, `pro se`, `esq.`.

## Affidavit Overreach

Remove or relocate to submissions unless quoting a source:

- `jurisdictional error`;
- `plainly wrong`;
- `bad faith`;
- `abuse of process`;
- `dishonest`;
- `coercive control was proven` where no authorised finding or source supports it;
- `the tribunal had no jurisdiction`;
- `the Court should find`;
- `is an error` or `is wrong` applied to another court or tribunal's order (collateral attack; use `disputed`, `under appeal`, `unable to reconcile`);
- `cannot be calculated` and similar conclusions about a contested figure (state `I have been unable to reconcile it`);
- relief or renewed requests in the body (`I renew that request`, `I seek`, `I ask the Court to`): relief belongs in the orders;
- self-diagnosis such as `trauma response` or `PTSD` where no medical evidence is relied on (swear the experience in lay terms);
- `can be produced if required` repeated on individual paragraphs: state producibility once as a blanket in the purpose section.

## Quotation Integrity (Contiguous Verbatim)

Quotation marks (single or double) assert that the words inside them appear in the source in that
order, unbroken. Verify every quoted span against the source before filing:

- The words must be contiguous in the source. Never fuse two non-adjacent passages, two findings or
  two paragraphs inside one set of quotation marks: that manufactures a verbatim the source does not
  contain, even where each fragment is accurate alone. This is the false-verbatim tell - quote marks
  around what is really a paraphrase.
- Mark every elision with an ellipsis and every inserted or changed word with square brackets; an
  unmarked join reads as continuous text. If the elision crosses a sentence boundary or a pinpoint,
  quote the passages separately, each with its own pinpoint.
- If the words are not contiguous verbatim, drop the quotation marks and paraphrase. A paraphrase
  carries no verbatim warranty and is the honest form for a synthesis of two findings; keep the
  pinpoint to each source.

The lint cannot check contiguity against a source it cannot see, so this is a drafting discipline,
not a lint rule. On review, treat a single-quoted span that fuses two pinpoints or crosses a
sentence boundary as the signal to re-open the source.

## AI Writing Tells

Run the hub taxonomy's Tier 1/2/3 sweep (chatbot framing, throat-clearing, markup and tool residue, puffery,
inflation vocabulary, copula avoidance, formulaic contrast, metronome rhythm, over-signposting, hollow topic
sentences, recap endings, evenly weighted lists, participle synthesis, template sections, uniform confidence,
unanchored claims). Formal legal register legitimately uses many flagged words, so calibrate on density and
clustering, never a lone word; the same three-tier discipline (remove artefacts, cap density, police structure
hardest) applies.

Legal-specific additions the hub does not cover:

- agent, build or workspace process language in filing-facing text: `agent summary`, `review set`,
  `render check`, `manifest proves`, `router status`, `gate fired`, `source pack`, or `audit found`. Translate
  to the legal act or cite the actual source;
- the leave-stage register marker `reasonably arguable` is the required standard, not a tell: never strip it to
  satisfy this list (see `legal-concision-and-anti-ai.md`, Register Discipline);
- legal noun towers such as `multi-forum procedural consequence context`, `source-boundary filing-facing
  assertion risk`, or `family-violence safety-context material`. Keep the defined legal term, then move
  qualifiers into a clause (see Legal Noun Stacks in `legal-concision-and-anti-ai.md`);
- rule-of-three triads as default cadence: one genuine triad per document is rhetoric; a triad in every
  paragraph is machine rhythm;
- formal connectives generally (`accordingly`, `thus`, `however`, `moreover`) are proper legal register: govern
  by density (never three successive paragraphs opening the same way), not prohibition;
- the legal-specific hollowness pair: authority recited with no sentence applying it to these facts, and
  factual assertions with no record anchor. Polish without record engagement is the core tell judges name in
  AI-drafted filings; pinpoints and application are the strongest human signals available.

### Guardrails

Do not use anti-AI editing to casualise legal documents. Keep correct passive voice, repeated defined terms,
accepted affidavit language, forum labels and exact source cues where they serve precision or compliance.
Contractions, chattiness and anecdote are the wrong fixes for court prose; every register-safe fix is a
substance fix (anchors, application, variance, calibration, cuts).

Do not edit to satisfy an AI detector. Disciplined formal legal prose sits inside detector false-positive
zones (standardised terms, formulaic connectives, proper passives), so a careful submission can trip a naive
detector; the repair is specificity and varied rhythm within the register, never informality. A detector score
is not source evidence, and detector-chasing must never weaken source anchors, legal status, redaction or forum
wording.

## Meta-Discourse And Absence Statements

Cut statements that only narrate the drafting process, such as `this section will address` or `as requested`.
See Absence tombstones in the hub taxonomy for the general test (would the sentence exist if no one had asked to
remove anything?). The legal form of a genuine, author-owned exception is broader than most domains: keep
absence, non-reliance, non-admission, no-concession, no-finding and no-order statements where they define legal
status, evidentiary scope, procedural position, safety framing or the boundary of relief sought.

## Email And Correspondence Tells

Remove or replace unless exact context requires the phrase:

- `I trust this email finds you well`;
- `for the avoidance of doubt`;
- `we reserve all rights` or `all rights are reserved`;
- `please be advised`;
- `kindly`;
- `as previously stated`;
- `we note with concern`;
- `your failure to`;
- `without prejudice` unless the legal effect is intended and user-instructed;
- long recitations of procedural history before the request.

## Dated Or Over-Formal Wording

Prefer current plain wording unless the older word is part of an exact quotation, statute or rule title,
official form field, defined term, case name, document title or source extract. The canonical
prefer/avoid table is `australian-english-house-style.md` (*Current Plain Terms*); the lint warns on the
common offenders (`pursuant to`, `prior to`, `whilst`, `utilise`, `hereby`/`thereof`, `the said`).

## Cross-Forum Drift

Check for:

- another forum's labels, powers, forms, deadlines, address conventions or
  service rules copied into the present document;
- relief sought from a decision-maker who cannot grant it;
- a pleading, submission or allegation from one proceeding stated as proof in
  another;
- a subsisting order characterised as wrong without a verified procedural and
  legal basis, especially while review or appeal is pending;
- a protective, police-issued or interim safety instrument framed as a final
  finding; and
- internal analysis, unresolved instructions or verification notes left in
  filing-facing text.

## Safer Replacements

| Risk phrase | Prefer |
|---|---|
| `clearly` | omit or state the fact |
| `obviously` | omit |
| `bad faith` | conduct described by date and source |
| `abuse` | alleged conduct, unless supported by source and forum strategy |
| `proved family violence` | `[SAFETY SOURCE] dated [DATE] records ...`, at the source's true status |
| `currently` | as at [date] |
| `recent` | dated [date] |
| `for the avoidance of doubt` | state the precise ambiguity, or omit |
| `we reserve all rights` | state the next procedural step, or omit unless instructed |
| `please be advised` | say the point directly |
