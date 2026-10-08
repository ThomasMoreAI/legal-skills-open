# Australian English House Style (legal overlay)

Use this reference for prose-level editing. Use the verified forum adapter for
law, procedure, forms, fees, deadlines, layout and filing method. Load the
`natural-writing` skill first for its hub default on general spelling,
punctuation, numbers, dates and terminology
mechanics. This file adds only the legal-specific overlay: forum labels,
citation and defined-term conventions, document structure, tone, and the
lint-enforced rules the hub does not know about.

This reference follows mainstream Australian usage (the Australian Government
Style Manual, the Macquarie Dictionary and the current *Australian Guide to
Legal Citation* (AGLC)) except where a rule is marked **(skill default)**. A skill
default is a drafting convention, not a national standard or a claim of forum
compliance. Project instructions, current official requirements and the supplied
form or template override it.

## Baseline

- Write in Australian English.
- Use day-month-year order for dates in prose, for example `25 May 2025`.
- Use exact times where they matter, for example `4:00 pm on 9 June 2025`.
- Use jurisdiction abbreviations and `s`, `ss`, `r`, `rr`, `para`, `paras`,
  `p`, `pp` only where ordinary Australian legal citation style and the forum
  permit them.
- Use `judgment`, not `judgement`, when referring to a court judgment.
- Use `filed`, `served`, `lodged`, `affirmed`, `sworn`, `annexure`, `exhibit`, `applicant`, `respondent`, `plaintiff`, `defendant`, `enforcement creditor`, and `enforcement debtor` only where the forum or form uses those labels.
- For a party acting without a lawyer, use the current term adopted by the
  forum, commonly `self-represented litigant` or `litigant in person`. Never
  substitute the American `pro se` unless it appears in quoted source text.

## Current Plain Terms

Use current, ordinary words where they do the same legal work. Keep an older term only when it is part of an
exact quotation, statute or rule title, official form field, defined term, case name, document title or source
extract.

| Prefer | Avoid in new drafting | Note |
|---|---|---|
| `phone` | `telephone` | Use `phone` in requests, orders and correspondence. Preserve `telephone` only in exact rule titles or quoted source text. |
| `under` | `pursuant to` | `under r [NUMBER]` is shorter and still legally precise. |
| `before` | `prior to` | Keep `prior` only where it is part of a defined legal phrase or source title. |
| `after` | `subsequent to` | Prefer the ordinary time word. |
| `use` | `utilise` | Prefer the direct verb. |
| `send`, `give` or `provide` | `furnish` | Match the rule or form if it uses a specific verb. |
| `about` or `for` | `in relation to` | Use the precise legal relationship if `about` is too broad. |

## Punctuation (legal-specific enforcement)

The `natural-writing` skill's hub default sets the general em-dash ban, en-dash-for-ranges
rule, semicolon and quotation-mark conventions. This skill's overlay:

- The em-dash ban is **lint-enforced** here (`scripts/lint_legal_style.py`
  fails on U+2014); the en dash is a lint warning only, not a ban.
- In a document title, follow the verified template or use a spaced hyphen
  (`Orders Sought - Extension and Directions`) as a house default.
- The **spaced hyphen** (` - `) is **not** caught by the lint. Use it only
  where the governing template or sibling-title convention requires it.
  Avoid it as a clause separator in body prose, section headings or
  paragraph labels; prefer a colon for a label gloss (`B. The requested
  direction: opposed`).
- Single quotation marks are the AGLC convention as well as the hub default;
  set a long quotation (more than about three lines) as an indented block
  without quotation marks.

## Spelling

Use the hub default. The one legal-specific note: preserve spelling in exact
quotations, official document titles, form fields, filenames and source
extracts even where it differs from house style, and verify any uncertain
term against the Macquarie Dictionary.

## Capitalisation And Defined Terms

- Capitalise a defined party or instrument and then use it consistently: `the
  Applicant`, `the Respondent`, `the Tribunal`, `the Court`, `the Act`, `the
  Agreement`.
- Define a short form once in parentheses, for example *[Act title]*
  ([jurisdiction]) (`the Act`), then use it consistently.
- Introduce a person the same way, with single quotes and not bold: `the respondent, [FULL NAME] ('[SHORT FORM]')`, then use the defined short form in plain text. Where two people share a surname, distinguish by given name or defined short form and keep it consistent. Do not bold a party short-form in running text (see *Headings, Numbering And Document Structure*).
- Do not capitalise a generic reference (`a tribunal member`, `the parties`, `a court of competent jurisdiction`).

## Citations And Emphasis In Running Text

- Italicise case names and legislation titles: *[CASE NAME] v [CASE NAME]* and
  *[Act title]* ([jurisdiction]).
- Keep the jurisdiction tag and pinpoint outside the italics: *[Act title]*
  ([jurisdiction]) s [section].
- Use the current AGLC edition where a formal authority citation is needed and
  the forum has not prescribed another style; see
  `source-boundary-and-citations.md`.
- Use italics only for citation and genuine emphasis. Do not use bold or capitals to argue a point.

## Numbers, Money And Dates

The hub sets the general day-month-year and numeral conventions. Legal
specifics:

- Use figures for money, with a thousands separator and two decimals where
  exactness matters: `$14,132.18`, `$1,800`.
- Preserve competing figures exactly. Do not silently round or normalise an
  amount.
- A date entered into an official form field follows that form's required
  format (for example `dd/mm/yyyy`); do not reformat a form-field value to
  match prose style.

## Headings, Numbering And Document Structure

The following are neutral drafting defaults only. They do not establish that one
shape is compliant across Australian forums. Before applying them, inspect the
current official form, rules, practice directions and filing specification. If
the forum is silent, use a stable, readable structure and record that the choice
is a house-style default.

- **Headings**: use short, stable, descriptive headings. Lettered topic headings (`A. Purpose`,
  `B. Background`: letter, full stop, space, then Title Case) are the skill default for affidavits and
  submissions. The heading letter is a label only; it never resets paragraph numbering.
- **Paragraph numbering**: if the forum or form requires numbered paragraphs,
  follow its scheme exactly. If it is silent, continuously number substantive
  affidavit, witness-statement or submission paragraphs `1` to `N` and do not
  restart under headings **(skill default)**. Keep one proposition or small
  factual cluster per numbered paragraph.
- **Sub-paragraphs**: one hierarchy only: `(a)`, `(b)`, `(c)`, then `(i)`, `(ii)`, `(iii)`. Use **block**
  sub-paragraphs (each on its own indented line) when a paragraph enumerates three or more discrete items,
  sets out relief or orders, or lists anything that will be cross-referenced. Keep a brief two-item aside
  **inline** in the sentence (`to address (a) X and (b) Y`). In Markdown source, write the literal marker
  `(a)` (not `a.`) and indent the sub-list four spaces so it renders as `(a)`.
- **Bolding**: follow the official form or template. If it is silent, use bold
  for headings only **(skill default)**. Do not bold party short forms, money or
  argumentative words in running text.
- **Cross-references**: if prose cites a paragraph number (`paragraph 66`), remember the rendered number is
  the continuous one. Adding or removing a whole paragraph shifts every later number and breaks the
  reference: prefer sentence-level edits, or keep the paragraph count fixed, or fix every reference.
- **Template precedence**: an official template may impose numbering, hanging
  indents, typography, labels or emphasis that differs from these defaults. The
  template governs. Verify the rendered result rather than assuming Markdown
  source shape survives conversion.

## Sentence Style

For the full legal concision and anti-AI procedure, use `legal-concision-and-anti-ai.md`.

- Put the answer, issue, request or relief before background.
- Prefer active voice: `Ms Lee filed the application`, not `the application was filed by Ms Lee`.
- Passive voice is acceptable where the actor is unknown, irrelevant or legally less important than the thing done.
- Keep related words together. Put the actor, action and object close to each other.
- Avoid double negatives.
- Avoid long openings before the main verb.
- Use concrete dates, amounts, document names and exhibit labels.
- Aim for short, scannable sentences: average around 20 words, and treat any sentence over about 24 words or
  carrying three or more list items as a split-or-tabulate prompt. This is an editing prompt, not a hard
  filing rule (canonical statement; the argument-structure and validation references apply it). Legal accuracy
  and pinpoint source anchors come first.
- Write positive sentences where possible: state what is sought, proved or disputed rather than building
  the sentence around what is not being said.
- Keep honest legal negatives where the absence is the fact: non-service, non-filing, non-payment,
  non-admission, no order, no finding, no concession, inability to reconcile or an issue under appeal.
- Vary sentence length where it helps the reader. Use a short sentence for the operative request, consequence
  or qualification. Do not add roughness, warmth or drama just to avoid a polished rhythm.

## Natural Legal Prose

- Write like a careful person making a record: formal enough for court, direct enough to understand quickly.
- Prefer concrete legal and evidentiary verbs: `filed`, `served`, `lodged`, `affirmed`, `sworn`, `paid`,
  `received`, `observed`, `recorded`, `annexed`, `exhibited`, `disputed`, `admitted`, `refused`.
- Keep the human actor in view where it is accurate: `Ms Lee filed`, `Mr Lee wrote`, `the registry sealed`.
  Passive voice is still proper where the document, step or result matters more than the actor.
- Keep defined terms, party labels, form labels, statutory language and accepted affidavit/submission formulae.
  Do not vary them for rhythm.
- Do not over-smooth a source-backed fact into a generic summary. Keep the date, amount, document name, exhibit
  label or visible source cue that makes the fact provable.
- Do not flatten uncertainty. Keep `alleged`, `disputed`, `not admitted`, `under appeal`, `unable to reconcile`
  and similar limits where they define the legal status.
- Repair dense noun piles by moving qualifiers into clauses. Keep the defined legal term, but avoid stacking
  several defined terms before an abstract noun.

## Paragraph Style

- Use one topic per paragraph.
- Start a paragraph with the proposition the reader needs, then support it.
- In affidavits and witness statements, use one fact or small factual cluster per numbered paragraph.
- In submissions, start each section with the proposition the reader must decide.
- In correspondence, state the request, deadline and practical next step early.
- Split long procedural history into a chronology or annexure table rather than carrying it in prose.

## Tone

- Formal, restrained and direct.
- Do not sound promotional, theatrical, sarcastic, soulless, over-formal, chatty or American.
- Do not overstate. Say what the document proves and what remains alleged, disputed or for source-backed analysis and user instruction.
- Prefer `the Applicant submits` in submissions and `I say` or `I observed` in affidavit evidence where appropriate.
- In correspondence, sound like a careful person writing for a record: courteous, practical and specific.
