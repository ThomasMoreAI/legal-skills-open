---
name: spec-contract-broomva
title: spec-contract — what must be in a design doc
description: 'The content contract for a design doc — what must be IN it, as against make-spec which owns how it LOOKS. Synthesised from five primary sources read verbatim (Lynch/Refactoring English + his worked example, Design Docs at Google, the Rust RFC template, Nygard''s original ADR post, Oxide RFD 1). The load-bearing rule is the cost of reversing a decision, not its importance: a choice fixable in an afternoon is review noise, a one-way door left unargued is the failure a design doc exists to prevent. Two layers. DETERMINISTIC — `scripts/spec_check.py` reads a markdown or HTML doc and decides 18 findings: required sections by class not by name, status resolvable and supersession pointed, >=2 alternatives with a stated reason for rejection somewhere in the section, non-goals that are declined goals rather than negated requirements, drawbacks that state a cost, acceptance that carries a number or a runnable command, and an implementation-manual detector for a doc with no trade-off
  language anywhere. JUDGMENT — `references/rubric.md` grades the five things a script cannot: whether the documented decisions are the expensive ones, whether the alternatives are real or strawmen, whether the non-goals are load-bearing, whether trade-offs are argued or merely mentioned, and whether the first screen is legible to the widest expected reader. Use when: (1) writing or reviewing a spec, plan, ADR, RFD or design doc, (2) deciding whether something warrants a design doc at all, (3) gating a doc before it goes out for review, (4) asked what belongs in a spec or why a spec is weak. Triggers on ''spec contract'', ''design doc'', ''write a spec'', ''review this spec'', ''is this spec any good'', ''what belongs in a design doc'', ''ADR'', ''RFD'', ''non-goals'', ''alternatives considered'', ''spec review'', ''spec gate'', ''design review'', ''one-way door'', ''reversal cost''.'
author: broomva
author_url: https://github.com/broomva/skills/tree/main/skills/governance/spec-contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
sources:
- title: Rubric
  path: references/rubric.md
- title: Sources
  path: references/sources.md
---

# spec-contract — what must be in a design doc

`make-spec` owns the **shell**: the theme, the tag vocabulary, the filename
convention, `<title>`/`<h1>` parity. Its self-test checks the CSS.

This skill owns the **contents**. They compose; neither replaces the other.

## The rule everything else derives from

> **What's the penalty for being wrong?**

A design doc admits a decision by the **cost of reversing it after
implementation** — not by importance, not by effort, not by how much the author
thought about it. Choosing C++ over Rails is unrecoverable at 200k lines and
belongs in the doc. A "Load more" button is fixable in an afternoon and arguing
about it in review is pure waste.

Every check below is downstream of that rule. Provenance for each, with verbatim
citations: [`references/sources.md`](references/sources.md).

## Layer 1 — deterministic (`scripts/spec_check.py`)

```bash
# one doc, profile inferred from the path
python3 scripts/spec_check.py docs/specs/2026-09-16-thing.html

# explicit profile, JSON for a gate
python3 scripts/spec_check.py docs/adrs/*.md --profile adr --json

# reversal cost becomes blocking rather than advisory
python3 scripts/spec_check.py docs/specs/thing.md --strict

# resolve every external URL (network; off by default so CI stays hermetic)
python3 scripts/spec_check.py docs/specs/thing.md --check-links
```

Exit `0` clean · `1` a required check failed · `2` bad invocation.

| Check | Fails when | Source |
|---|---|---|
| `C1-missing-section` | a **required** class for the profile has no heading | LYNCH |
| `C1-missing-recommended` | *(warn)* a recommended class is absent | LYNCH |
| `C2-no-status` | no `Status:` field — a doc with no state can never be superseded | NYGARD, OXIDE |
| `C2-dangling-supersede` | status is `superseded`/`deprecated` and names no successor | NYGARD |
| `C2-bad-status` | *(warn)* status outside the known state set | OXIDE |
| `C3-no-reversal-cost` | *(warn; `--strict` → fail)* no one-way/two-way-door declaration | LYNCH |
| `C3-vague-reversal-cost` | *(warn)* reversal cost named but not graded | LYNCH |
| `C4-negated-goal` | *(warn)* a non-goal reads as a negated requirement | GOOGLE |
| `C5-thin-alternatives` | fewer than two alternatives named | RUST, GOOGLE |
| `C5-no-rejection-reason` | no option states why it was *not* chosen | RUST |
| `C6-drawbacks-without-cost` | a drawbacks section that states no cost — blocking where the class is *required*, advisory where it is only recommended | NYGARD, RUST |
| `C7-open-question-without-next-step` | *(warn)* an open question with no resolution path | LYNCH |
| `C8-unmeasurable-acceptance` | acceptance with no number, unit or runnable command — blocking on `plan`, advisory elsewhere | LYNCH |
| `C9-implementation-manual` | **no trade-off language anywhere in the document** | GOOGLE |
| `C10-oversized` | *(warn)* beyond ~20 pages — GOOGLE's signal to split the problem | GOOGLE |
| `C10-stub` | *(warn)* under 250 words | NYGARD |
| `C11-dead-link` | *(opt-in `--check-links`)* a cited URL does not resolve | — |
| `C11-unsafe-link` | *(opt-in `--check-links`)* a cited URL resolves to a private, loopback or link-local address | — |

### Profiles

A profile is a claim about which reversal-cost axes a document type exists to
pin down. Inferred from the **path only** (`docs/adrs/` → `adr`, `docs/plans/` →
`plan`, `/rfd`|`/rfcs/` → `rfd`, else `spec`); override with `--profile`.

`note` is never inferred. An earlier cut downgraded any document under 700 words
to it, and cross-review found the consequence: a thirteen-word implementation
manual committing a one-way door exited 0, and the cheapest way to pass was to
delete words. `note` is right for a short design-bearing doc — as a choice
someone makes and a reviewer can see, not a silent property of length.

| Profile | Required | Recommended |
|---|---|---|
| `adr` | context · design · alternatives · drawbacks | objective · acceptance |
| `spec` | objective · design · non-goals · alternatives | context · goals · drawbacks · acceptance · open questions |
| `plan` | objective · goals · **acceptance** | non-goals · design · open questions |
| `rfd` | objective · design · alternatives · drawbacks | context · open questions · acceptance |
| `note` | design | objective · alternatives |

`alternatives` is required on `adr`, `spec` and `rfd` because all five sources
say so in the same words. It is **not** required on `plan` — a rollout plan
sequences work whose design decision was already taken elsewhere — nor on
`note`. `acceptance` is required on `plan` alone: a plan with no definition of
done is a wish list. `test_r1_nb1_skill_md_alternatives_claim_matches_the_table`
asserts this paragraph against `PROFILES`, because the first version of it
claimed "every profile but `note`" and the table disagreed.

**Sections resolve by class, not by name.** "Missing features", "Out of scope"
and "What this is not" are all `non_goals`. Widen a class by adding a synonym to
`SECTION_CLASSES` — the single producer — never by renaming a heading to satisfy
the checker. Renaming to pass a gate is gaming it.

## Layer 2 — judgment (`references/rubric.md`)

A doc can pass all 18 findings and be worthless: two strawman alternatives, a
non-goal nobody would have assumed, an SLO chosen because it was easy to measure.
That is not a gap in the script — it is the half that is irreducibly a judgment.

Five axes, 0-3, **pass ≥11/15 with no axis at 0**:

| Axis | Question |
|---|---|
| **R1** reversal-cost fit | are the documented decisions the expensive ones — and is any expensive one missing? |
| **R2** alternative realism | would a competent engineer actually have chosen one of these? |
| **R3** non-goal load-bearing-ness | would a reader have assumed these were in scope? |
| **R4** trade-off substance | delete the alternatives section — does the doc's meaning change? |
| **R5** legibility | is the first screen intelligible to the widest expected reader? |

Grade with a **different model than the one that wrote the doc** (P20: the writer
cannot be the final judge). `R1 = 0` — a silent one-way door — stops the doc
outright; `R2`/`R4` at 0-1 route to full cross-review, because the design is
unargued and rewriting prose will not fix it.

## When a design doc is not warranted

The honest answer is often *none*. Both Lynch and Google give a test, and they
agree: write one when the **solution is ambiguous** and the **decisions are
expensive**. Google's disqualifier is the sharper one —

> *"If a doc basically says 'This is how we are going to implement it' without
> going into trade-offs, alternatives, and explaining decision making … then it
> would probably have been a better idea to write the actual program right away."*

That is what `C9` detects mechanically. If the only honest answer to "what were
the alternatives?" is "there weren't any", the correct output is code, not a doc.

## Composition

| With | How |
|---|---|
| **`make-spec`** | This skill decides the contents; `make-spec` renders them. Run `spec_check.py` on the output before the doc goes out. |
| **`cross-review` (P20)** | The judgment layer *is* a P20 stratum applied to a design rather than a diff. An `R2`/`R4` failure escalates to the full gate. |
| **`decision-log`** | Already asks "one-way door or two-way door?" — that is `C3`'s field. A logged decision that reaches doc scale becomes an `adr`-profile doc. |
| **`bookkeeping` (P6)** | A doc that passes both layers is citable provenance for an entity page; one that fails `C9` is an implementation manual and cites nothing. |
| **`checkit`** | Supplies `R2`'s input — you cannot judge whether an alternative is real without having read what else exists. |

## Review ordering

Grading a draft and reviewing it are different disciplines. The ordering is
counterintuitive enough to state, and it is in `references/rubric.md`: **one**
preliminary reviewer on comprehension only (ten at once triggers the bystander
effect), then widen on substance, and the meeting is the **last** step with an
agenda naming only the open issues. Every answer goes back into the doc — a
reviewer's confusion resolved in a thread fixes nothing for the next reader.

## Anti-rationalization

| Excuse | Reality |
|---|---|
| "The sections are all there, so the doc is fine." | Layer 1 checks shape. Shape is necessary and nowhere near sufficient — run the rubric. |
| "I'll add non-goals if a reviewer asks." | The scope boundary is what review relitigates. Undefended scope is the cost you pay later, in the meeting. |
| "There weren't really any alternatives." | Then there was no decision, and `C9` is right: write the code. If there *was* a decision, the alternatives exist and you skipped them. |
| "I'll rename the heading so the checker passes." | Classes are synonym-matched precisely so you don't have to. Renaming to pass is gaming the gate; add a synonym, or write the section. |
| "This is just a small change." | Then use the `note` profile, which requires one section. Small is a size, not an exemption from stating what you gave up. |
| "The doc is accurate — I wrote it last month." | Staleness has no failure signal. `C2` exists so a doc can be superseded; a doc with no status silently becomes a false description of what shipped. |
| "I reviewed it myself and it reads well." | Reading well is `R5`, the cheapest axis. The writer cannot grade `R1`, `R2` or `R4` on their own work. |

## Calibration

Measured 2026-09-16.

**The corpus, defined once.** `find docs/specs docs/plans docs/adrs -maxdepth 1
-type f \( -name '*.md' -o -name '*.html' \)` → **105 documents**. Recursive
would give 110; the 5 extra live in `kinetic-orb-cinema/`, `kinetic-workspace/`
and `motor-ontologia/`, which are project subdirectories rather than design
docs. Every percentage below has 105 as its denominator. The supersession
measurement further down uses **98** — the HTML subset — and says so, because
its subject is an HTML front-matter convention.

| Corpus | Result |
|---|---|
| **Lynch's own worked example** (`little-moments-design-doc`, 2,667 lines), `--profile spec` | **zero failures** |
| This workspace's 105 `docs/specs\|plans\|adrs` documents | **1 passes** |

Section coverage across those 105, by class: design 52.4% · open questions 25.7%
· drawbacks 18.1% · objective 12.4% · context 10.5% · **non-goals 7.6% ·
alternatives 5.7%** · acceptance 5.7% · goals 1.9%. The corpus documents what
was chosen and not what was ruled out — the inverse of reversal cost, and the
reason this skill exists.

Those figures moved twice under review and the movements are the point. An
earlier version of this paragraph published `design 55.2%`; substring matching
without word boundaries was counting "Conflict resolution" as a design section,
and the corrected figure is 52.4%. `alternatives` fell 7.6% → 5.7% when bare
"rejected" stopped being a section synonym. **`non-goals` has not moved through
any parser change** — it is the one number no repair has touched.

**Supersession runs the wrong way, measured.** Dogfooding the checker against
the workspace's own HTML docs turned up the sharpest number in this file. Of the
**98 HTML documents** in `docs/specs|plans|adrs` (the subset, not the 105 above —
the convention under test is an HTML front-matter one), **38 mention superseding
or replacing another document, and 2 carry a status marking themselves as
superseded.**

The relation is recorded in the forward direction, in the new doc, where it
helps nobody: a reader who lands on the *old* document gets no signal that it
has been replaced. NYGARD's rule is the other direction — *"we will keep the old
one around, but mark it as superseded"* — and it is the only mechanism in any of
the five sources by which a design doc can stop being a false description of
what shipped. `C2` exists because of that asymmetry.

A caveat on the arithmetic: 38 − 2 = 36 is a subtraction, not a count of
documents needing a marker. The 38 forward-mentions live in the *new* documents;
the ones that need a `superseded` status are the *old* ones they point at, and
this measurement never resolves those references. The asymmetry is the finding;
36 is not a population.

**What the corpus number is not evidence for.** An earlier draft of this section
reported 1/105 and attributed the improvement to the required/recommended split.
Cross-model review challenged that attribution and re-measurement refuted it:
both the all-nine-required arm and the shipped split pass **0/105**. The split
buys zero existing documents. It is derived from the five sources — `required`
is the intersection of what all five independently call load-bearing — and the
evidence that it is not merely strict runs the other way: **a design doc written
to published best practice clears it.** A corpus pass rate says what the corpus
is like, not where the bar belongs, and reporting it as if it justified the bar
was the error.

### Re-measuring

The corpus figures live in another repository, so no test in this one can hold
them honest — and they drifted twice under review before anyone noticed. Re-run
them with:

```bash
python3 - <<'PY'
import sys, pathlib, collections
sys.path.insert(0, "scripts"); import spec_check as sc
import os
root = pathlib.Path(os.environ.get("BROOMVA_ROOT",
                    pathlib.Path.home() / "broomva"))   # override for another checkout
docs = [p for d in ("specs", "plans", "adrs")
        for p in (root / "docs" / d).glob("*.*") if p.suffix in (".md", ".html")]
have, fire, npass = collections.Counter(), collections.Counter(), 0
for d in docs:
    r = sc.check(d, None, False, False)
    npass += not r.failed
    for c in r.sections: have[c] += 1
    for f in r.findings:
        if f.severity == "fail": fire[f.check] += 1
print(f"{npass}/{len(docs)} pass")
print({k: f"{100*v/len(docs):.1f}%" for k, v in have.most_common()})
print(dict(fire.most_common()))
PY
```

The self-contained numbers — test count, mutant count, finding-id count — ARE
enforced: `tests/mutation.sh` reads its own baseline, and
`test_r1_b8_documented_check_ids_match_the_code` asserts the id set and the
prose count against the source. Those three cannot drift silently. The corpus
percentages can, and this is the command that catches it.

## Precision, per check, on live firings

A check is only worth what it is right about. Measured across the 105-document
corpus:

| Check | Firings | Precision |
|---|---|---|
| `C1-missing-section` | 331 | structural — a heading class is present or it is not |
| `C2-no-status` | 23 | **22/23**, every firing inspected |
| `C9-implementation-manual` | 13 | all 13 have **zero** trade-off expressions in prose |
| `C2-dangling-supersede` | 2 | both inspected; both name no successor |
| `C5-thin-alternatives` · `C6` | 0 · 0 blocking | `C6` demoted to advisory, below |

**Sample size is not a precision measurement.** An earlier version of this table
claimed `C2-no-status` at "10/10 on a random sample" of 36 firings. Reviewing all
36 found **14 false positives** the sample had missed — five distinct mechanisms,
four of them introduced by the fixes of the two preceding rounds. The numbers
above come from inspecting *every* firing, and the four that a crude grep
flagged as suspect turned out on reading to be true positives: `status:
FlagStatus;` is TypeScript in a code block, two more are per-item statuses in
body prose. Auditing with a proxy for the thing is how the first number was
wrong; the second was produced by looking.

**A check was deleted on this evidence.** `C5-unjustified-alternative` asked
whether each option carried prose beyond its own name. Its precision on live
firings was **0 of 2** — both were the header row of a comparison table, which
is the commonest real idiom for the section. A rule wrong on every firing it
produces is not a rule with a bug, and tuning it further would have meant
editing the corpus to fit the rule. Whether an option is argued *well* is rubric
**R2**, which is where that judgement belongs.

**Two checks are advisory because their precision could not be demonstrated.**

- `C6-drawbacks-without-cost` fired 4 times; at best 2 were true. One fires on a
  section headed *"Two structural prohibitions, not compliance costs"* — pulled
  into the class by the word "costs" in a heading that says it is not a costs
  section — and one on *"Negative / accepted trade-offs"* whose real costs
  ("far less to build than OpenRaft", "no consensus machinery to operate") are
  not in `COST_LANGUAGE`. Enumerating cost vocabulary is the same losing game as
  enumerating status vocabulary. Whether stated consequences are honest is **R4**.
- `C9`'s floor was 2 expressions and is now 1. The floor of 2 was a *second*
  defence against a hazard `body_prose` already closed, and it cost 15 false
  failures (28 → 13). All 13 remaining have literally zero trade-off vocabulary.

**Known limitation:** `C9` reads English. Two of its firings are Spanish-language
documents where it cannot see an argument that may be there. Treat a `C9` failure
on a non-English doc as unmeasured.

## Tests

```bash
python3 -m pytest tests/test_spec_check.py -q   # 162 tests
bash tests/mutation.sh                          # incl. a NULL control that must SURVIVE
```

Every check carries a **positive and a negative control**. `C4` found nothing
across all 105 real documents; that is a measured zero with a known cause — only
8 of them have a non-goals section for it to read — not an unfalsified silence,
and the four positive controls prove the rule fires.

The mutation sweep reports **killed 47/47**, and three properties of it are load-bearing
because the first version had none of them and still printed a clean score:

- **A NULL mutant must SURVIVE.** A no-op edit that fails the suite means the
  harness is broken and every other verdict it printed is void.
- **A nonzero exit is not a kill.** `PYTEST_ADDOPTS=--bogus` made the first
  version report "killed 14/14" while pytest collected nothing. A kill now
  requires the same test count as the clean baseline plus a `FAILED` line.
- **A crash is not a kill.** A mutant that dereferences `None` proves the code
  path runs, not that any assertion is sensitive to it. Those are reported
  `CRASH` and fail the run.
