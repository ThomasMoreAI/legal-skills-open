# Validation Checklists

## Reference Map

`legal-concision-and-anti-ai.md` loads for all prose. Add only what the task
needs:

| Task/mode or content | Load |
|---|---|
| submissions / written advocacy | `argument-structure-and-paragraphing.md` |
| forms, affidavits, orders, annexures | `forum-and-document-recipes.md` |
| statutory declarations, or choosing between a declaration, an affidavit and a witness statement | `statutory-declarations.md` |
| deeds, agreements, releases, guarantees, variations | `deeds-and-agreements.md` |
| tribunal work and merits review | `tribunals-and-merits-review.md` |
| correspondence | `legal-correspondence-style.md` |
| letters of demand, pre-action letters, settlement offers | `demands-and-pre-action-correspondence.md` |
| AGLC citation in academic work, advices and research memoranda | `aglc4-citation.md` |
| non-filing legal decision overview | `decision-overviews.md` |
| family-violence or redaction-sensitive material | `family-violence-and-redaction.md` |
| house style questions | `australian-english-house-style.md` |
| source anchors and citations | `source-boundary-and-citations.md` |
| banned phrasing/patterns | `forbidden-patterns.md` |
| checking the finished draft | this file (`validation-checklists.md`) |
| current-source and user-authority gates | `verification-and-escalation.md` |

Run the checks the task needs, not all of them:

| Task/mode | Run |
|---|---|
| any filing-facing text | Lint Workflow first (it owns the mechanical bans), then Filing-Facing Style + Source |
| `draft` / `rewrite` submissions | Concision + Argument Structure + Integrity |
| `condense` / `final-scrub` | Concision + Integrity (condense gate) + Naturalising |
| affidavit work | Affidavit + Source + Safety |
| orders/minutes | Document Function + the Orders cut-list in `forum-and-document-recipes.md` |
| correspondence | Correspondence + Filing-Facing Style |
| letter of demand or pre-action letter | Correspondence + Source + the checks in `demands-and-pre-action-correspondence.md` |
| statutory declaration | Source + Safety + the regime and execution checks in `statutory-declarations.md` |
| deed or agreement | Document Function + the review pass in `deeds-and-agreements.md` |
| tribunal application, contentions or submissions | Concision + Argument Structure + the completion gate in `tribunals-and-merits-review.md` |
| legal decision overview | Decision Overview + Source |

## Decision Overview Check

For a non-filing legal decision overview, apply
[decision-overviews.md](decision-overviews.md). Check that each issue keeps the
shared position, source support and remaining decision or professional
confirmation distinct. Open options retain their material legal consequences.

## Filing-Facing Style Check

The lint owns the mechanical bans (em dashes, US legalese, internal markers, agent/AI process language,
banned evidence paths, US dates): run it rather than eyeballing those. Then check what the lint cannot see:

- Australian English spelling.
- Dates use day-month-year style, for example `25 May 2025`.
- En dashes only where genuinely appropriate (number, date or page ranges), used sparingly.
- No unresolved placeholders unless the file is deliberately a draft and the build profile permits them.
- Headings are stable and useful.
- Paragraphs are numbered where the forum expects numbered paragraphs.
- Long paragraphs are split where possible.
- Australian spelling specifics are correct (`-ise`, `-our`, `defence`, the noun `licence` / `practice`, `program`, `judgment`).
- Quotation marks are consistent (single quotes preferred); quote styles are not mixed.
- Case names and legislation titles are italicised.
- Defined terms are capitalised and used consistently.
- Money and competing figures are exact and not silently rounded.
- A self-represented party is described as `self-represented litigant` or `litigant in person`, never `pro se`.
- Every markdown heading has a blank line before it (the pandoc `blank_before_header` render rule: a
  heading glued to the previous line renders as body text, silently demoting a whole Part). The lint
  fails on this; still verify the rendered heading on any changed page.
- Every table column heading is true of every row beneath it. A row that fits the table's purpose but
  not its column head miscategorises itself; retitle the column (or split the table) before filing,
  and prefer the retitle when other documents cite the table's rows by number.

## Concision Check

- The first paragraph states the relief, request, answer, issue or practical next step.
- Each paragraph has one topic or small factual cluster.
- Each paragraph has a legal function: relief, procedural step, source-backed fact, rule, contention,
  consequence, safety limit, request or deadline.
- Any added sentence supplies a missing legal function. If a condense, rewrite or final-scrub pass is longer
  than the original, the added words are justified by source, safety, correspondence protection, enforceability
  or necessary qualification.
- Long procedural history has been shortened, moved to chronology, or removed.
- Active voice is used unless passive voice serves a legal or evidentiary purpose.
- Concrete actors, dates, amounts, document names and source anchors replace vague summary.
- Throat-clearing, inflated adjectives, repeated background and AI-polished transitions have been removed.
- Additive transitions have been replaced with the real relation or removed.
- Dense legal noun stacks have been unpacked without deleting defined terms.
- Brevity has not removed legal accuracy, redaction, forum wording or source anchors.
- There is no percentage cut target. Stop when the next cut would remove a date, amount, party label,
  filing/service status, source cue, exhibit/annexure label, paragraph/page/line reference, redaction qualifier,
  procedural caveat, honest legal negative or forum-required wording.
- For longer drafts, reverse-outline each paragraph in one phrase. If a paragraph has no legal function, cut it.
  If it has two unrelated functions, split it.

## Argument Structure Check

For submissions and written advocacy; see `references/argument-structure-and-paragraphing.md`.

- A fresh reader recovers relief, grounds and reasons from the headings and the first sentence of each paragraph
  alone; the opening states the upshot within about 90 seconds.
- Each argument-bearing heading is a one-sentence conclusion, not a topic label; the heading list read alone
  states the case (structural or umbrella sections excepted).
- Each paragraph opens with its contention, develops one point, and ends on its conclusion, not on a trailing
  citation or a new sub-point.
- Each shared premise, rule, figure and chronology appears in full once; later sections cite it by name. A
  restatement survives only at a primacy point and only if it carries new evidence or stakes.
- The grounds run are the strongest, not every available one; every retained passage can be justified as moving
  the tribunal toward the relief sought.
- Sentences average about 20 words; any over about 24 words or carrying three or more list items is a
  split-or-tabulate prompt; authorities are not strung for a settled proposition.
- One register for the stage, held for the document: a leave/threshold document argues `reasonably arguable`
  and does not flip to `is established` mid-paragraph; a merits document may assert what the record carries.
- Adverse authority is disclosed and met (distinguished on the facts first); the obvious weakness is confronted
  with one located concession, not side-stepped; a reply answers every distinct contention without re-arguing
  the case-in-chief.

## Integrity Check

- Every cited authority is in the project's verified authority register or was
  opened and pinpoint-verified against an authorised primary source for this
  task; no authority was introduced that cannot be located.
- Holdings are stated at their true fact-specific altitude; no narrow ruling inflated into sweeping support.
- No instrument, declaration, order term or finding appears that the baseline record does not contain; no rule
  title, statute name or decision-maker label was altered in paraphrase.
- Any condense/relocation pass passed the deterministic token check (figures, dates, pinpoints, exhibit labels,
  authorities, defined terms set-diffed against the before-text) AND an independent qualitative pass (no
  ground, particular, qualifier or honest negative weakened, unowned or unlocatable).
- Nothing confidential, suppressed or privileged was sent to an external tool; court AI-practice requirements
  for the forum were checked (see `source-boundary-and-citations.md`, Citation And Content Integrity).

## Naturalising Check

- The draft sounds like plain Australian legal writing, not a generic AI template.
- Each paragraph serves a legal request, source-backed fact, contention, rule, procedural step, limitation,
  consequence or necessary transition.
- Actors, actions, dates, documents and source cues remain close together where possible.
- No legal term of art, source anchor, qualification, redaction, protected-address limit or forum label was
  removed to improve flow.
- Affidavit text remains first-person evidence; submissions remain argument; orders remain commands;
  correspondence remains practical.
- Wrong-home material was moved, not polished in place.
- Duplicated material has one home. Forms, affidavits, submissions and orders match without restating each other.
- Any retained formal phrase has a legal, source, forum or safety reason.
- Final self-audit: name the single concrete remaining defect, if any: overclaim, missing source, wrong
  document home, unsafe disclosure, machine rhythm, noun stack, false transition, unsupported legal conclusion
  or broad fairness closer. If no concrete defect can be named, stop.

## Source Check

- Every factual assertion has a source.
- Every cited document exists in the workspace.
- No fact is inferred from a filename.
- No `.work/`, `docs/audits/`, OCR scratch, render output or internal note is cited as evidence.
- Conflicting figures are preserved and attributed.
- Procedural statements relying on current forms, fees, rules or filing methods have been checked against official sources.

## Document Function Check

- Orders contain orders, not argument.
- Affidavits contain facts, not submissions.
- Submissions contain issues, law, argument and relief.
- Chronologies contain date, event, source and relevance.
- Correspondence states the request and deadline.
- Proposed orders have been classified before cutting: order, undertaking, notation/recital or reason.
- Solicitor notes remain internal.
- Annexure and exhibit indexes match the document labels.

## Correspondence Check

- Subject line names the matter/file, action and date or deadline where useful.
- Recipient, `Cc`, attachments and protected-address handling are correct.
- The first paragraph states the request, filing/service action, attachment list or response position.
- Protective labels, offer terms, non-admission or non-waiver wording, rights reservations, response deadlines
  and attachment/service statements have not been cut as mere style.
- Only necessary background is included.
- Tone is courteous, firm, practical and annexure-safe.
- No unsupported accusation, concession, undertaking, settlement offer, service admission or rights reservation has been added.
- Sign-off matches the salutation and formality.

## Affidavit Check

- Each person is introduced once by full name with a bracketed short form and relationship, then referred to consistently by the short form; the full name is not re-introduced later.
- The deponent swears experience, not self-diagnosis, where no medical evidence is relied on.
- No relief, renewed request, argument, or characterisation of another forum's order as wrong; disputed liability is framed as disputed / not admitted / under appeal / unable to reconcile.
- Direct personal-knowledge facts are preserved or quarantined for corroboration; they are not deleted merely
  because no external document is attached.
- Producibility is stated once as a blanket; conditional reserves are deliberate, not repeated filler.
- The affidavit or witness statement satisfies the current verified form,
  length, layout and signing requirements; paragraph cross-references still
  resolve after editing and rendering.

## Safety Check

- Protective, police-issued, interim and final safety material is named at its
  exact source status; allegation, order and finding are not conflated.
- Sensitive material is targeted and proportionate.
- Residential address and unsafe contact details are excluded or handled under the forum rules.
- Medical, reproductive-health, third-party and broad message-history material is not filed unless necessary and settled.

## Lint Workflow

Run the lint with explicit project paths. It has no implicit project directories:

```bash
python3 "$(provenant root)/skills/legal-writing/scripts/lint_legal_style.py" path/to/source path/to/correspondence
```

Project build tooling should pass its filing-facing source, correspondence and annexure paths explicitly.

To scan this skill's own reference files, add `--allow-quoted-examples` so quoted bad examples are not treated as filing-facing prose:

```bash
python3 "$(provenant root)/skills/legal-writing/scripts/lint_legal_style.py" \
  "$(provenant root)/skills/legal-writing" --include-readme --allow-quoted-examples
```

Treat failures as blockers for filing-facing documents. Treat warnings as review prompts.
