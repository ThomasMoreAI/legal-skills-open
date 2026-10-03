---
name: bluebook
title: Bluebook Citation (22nd edition; 21st still reachable)
description: ALWAYS use for ANY legal citation question, even if the user never says 'Bluebook' - 'cite this case', 'how do I cite a statute', 'is this footnote formatted right', 'id. or supra here', 'cite a law review article', 'what signal goes here', 'format these footnotes', 'short form for this cite', 'block quote this', 'where does the ellipsis go', 'is this quote altered right', or writing or checking any citation or quotation in a legal manuscript. NOT for auditing a whole manuscript's footnotes (use bluebook-audit) and NOT for rendering these rules in Typst (use docx-typst).
author: edwinhu
author_url: https://github.com/edwinhu/workflows/tree/main/skills/bluebook
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: general
language: en
sources:
- title: Abbreviations
  path: references/abbreviations.md
- title: Audit patterns
  path: references/audit-patterns.md
- title: Cases
  path: references/cases.md
- title: Editions 21 to 22
  path: references/editions-21-to-22.md
- title: Quotations
  path: references/quotations.md
- title: Secondary sources
  path: references/secondary-sources.md
- title: Short forms
  path: references/short-forms.md
- title: Signals parentheticals
  path: references/signals-parentheticals.md
- title: Statutes
  path: references/statutes.md
---

# Bluebook Citation (22nd edition; 21st still reachable)

**What this skill carries** — grep `references/` for any subject the names below miss:
!`d=${CLAUDE_SKILL_DIR}; command -v skill-toc >/dev/null 2>&1 && exec skill-toc "$d"; s=$HOME/.claude/skills/plugin-utils/bin/skill-toc; [ -x "$s" ] && exec "$s" "$d"; echo "(skill-toc unavailable: references and scripts are NOT listed here — install the plugin-utils plugin, or start a new session so its bin/ reaches PATH)"`

Citation formatting for law reviews and legal scholarship per *The Bluebook: A Uniform System of Citation* (21st ed. 2020).

**Announce:** "I’m using the bluebook skill for citation formatting."

## When to Use

Invoke this skill for:
- Formatting case citations (federal, state, foreign)
- Statutory and regulatory citations
- Secondary sources (books, articles, treatises)
- Short form citations (id., supra, hereinafter)
- Introductory signals and parentheticals
- Citation sentences vs. citation clauses

**For legal writing style**: Use `/writing-legal` skill (Volokh)
**For general writing**: Use `/writing` skill (Strunk & White)

**To RENDER these rules in a Typst manuscript**: this skill states the rules; it does
not implement them. `docx-typst` carries the implementation — `assets/bluebook.typ` is a
`#show cite:` rule supplying the three things typst's built-in bibliography cannot
(`supra note N`, small-caps reporters, `shortjournal` → `container-title-short`), because
hayagriva is statically linked into the typst binary and renders none of them. Reach for
it whenever a Typst document needs the short forms in `references/short-forms.md` to
renumber themselves rather than be typed by hand.

<EXTREMELY-IMPORTANT>
## IRON LAW #1: NO CITATION WITHOUT VERIFICATION

**If you haven’t verified EVERY element of a citation, DO NOT write it.**

Before writing ANY citation:
1. Verify case name spelling and procedural posture
2. Verify reporter volume and page numbers
3. Verify court and year
4. Verify pinpoint page exists

**Guessing reporter volumes or page numbers is NOT HELPFUL — the user publishes with wrong citations that fail verification. Period.**
</EXTREMELY-IMPORTANT>

<EXTREMELY-IMPORTANT>
## IRON LAW #2: NO SHORT FORMS WITHOUT FULL CITATION FIRST

**Id., supra, and hereinafter REQUIRE a preceding full citation.**

Before using ANY short form:
1. Locate the full citation in the document
2. Verify no intervening citations (for id.)
3. Verify the supra reference is unambiguous

**Using id. after intervening citations creates ambiguity. Delete and cite in full.**
</EXTREMELY-IMPORTANT>

<EXTREMELY-IMPORTANT>
## IRON LAW #3: FOOTNOTE VS. TEXT CITATION FORMAT

**Law review citations use footnote format (Rule 1). Court documents use text format (Bluepages).**

```
FOOTNOTE (law reviews):    Smith v. Jones, 500 U.S. 1, 5 (1991).
TEXT (court documents):    Smith v. Jones, 500 U.S. 1, 5 (1991)

FOOTNOTE (statutes):       18 U.S.C. § 1001 (2018).
TEXT (statutes):           18 U.S.C. § 1001 (2018)
```

**If writing for a law review and using text format conventions, DELETE and reformat.**
</EXTREMELY-IMPORTANT>

## The Gate Function

Before writing ANY citation:

```
1. IDENTIFY → What type of source? (case, statute, article, book)
2. LOCATE   → Find the correct rule in Bluebook
3. VERIFY   → Confirm ALL elements (volume, page, court, year)
4. FORMAT   → Apply correct typeface and punctuation
5. CHECK    → Does this match examples in the rule?
6. WRITE    → Only after steps 1-5
```

**Skipping any step produces unreliable citations.**

## Citation Facts

- An intervening citation breaks *id.* — *id.* after an intervening cite is ambiguous and must become a full short form. *Supra* only works when the full citation it points to actually exists earlier in the document.
- Signals are checked against Rule 1.2 examples, not intuition — a wrong signal misleads the reader about how the source supports the proposition.
- Parentheticals explain the source's relevance; pinpoints prove the specific claim. A cite deferred ("I'll add the pinpoint later") ships without one.
- Typeface (Rule 2) is mandatory, not stylistic. Abbreviations come from tables T6, T10, T12 — "common" or "obvious" abbreviations that don't match the tables fail cite-check.
- "Pretty sure" about a reporter volume or page number means unverified — a guessed element presented as a citation is an unverified claim, and exact pinpoints are required.

## Quick Reference: Common Citation Forms

### Cases (Rule 10)

```
Full citation:
Brown v. Board of Education, 347 U.S. 483, 495 (1954).

Short form (same footnote or five footnotes with no intervening):
Id. at 496.

Short form (different footnote, no intervening):
Brown, 347 U.S. at 497.

Short form (intervening citations):
Brown v. Board of Education, 347 U.S. at 498.
```

### Statutes (Rule 12)

```
Full citation:
42 U.S.C. § 1983 (2018).

Multiple sections:
42 U.S.C. §§ 1983-1985 (2018).

Short form:
§ 1983 or id. § 1984
```

### Law Review Articles (Rule 16)

```
Full citation:
Cass R. Sunstein, *On the Expressive Function of Law*, 144 U. Pa. L. Rev. 2021, 2030 (1996).

Short form:
Sunstein, supra note 12, at 2035.
```

### Books (Rule 15)

```
Full citation:
Richard A. Posner, Economic Analysis of Law 45 (9th ed. 2014).

Short form:
Posner, supra note 5, at 52.
```

## Typeface Rules (Rule 2)

| Source Type | Law Review Format |
|-------------|-------------------|
| Case names | Italics: *Brown v. Board* |
| Book titles | Small caps: ECONOMIC ANALYSIS OF LAW |
| Article titles | Italics: *On the Expressive Function* |
| Journal names | Small caps: U. PA. L. REV. |
| Periodical names (non-consecutively paginated) | Italics: *N.Y. Times* |
| Statutes | Roman: 42 U.S.C. § 1983 |

## Introductory Signals (Rule 1.2)

| Signal | Meaning | Use When |
|--------|---------|----------|
| [no signal] | Direct support | Source directly states proposition |
| *See* | Implicit support | Source supports but doesn’t directly state |
| *See, e.g.,* | One of several | Multiple sources support; citing representative |
| *Cf.* | Analogous support | Source supports by analogy |
| *Compare* ... *with* | Comparison | Sources illustrate through contrast |
| *See generally* | Background | Source provides helpful background |
| *But see* | Contradiction | Source contradicts proposition |
| *Contra* | Direct contradiction | Source directly contradicts |

### Signal Order (Rule 1.3)

Within a single citation sentence, signals appear in this order:
1. [no signal]
2. *E.g.,*
3. *Accord*
4. *See*
5. *See also*
6. *Cf.*
7. *Compare*
8. *Contra*
9. *But see*
10. *But cf.*
11. *See generally*

## Common Errors Checklist

### Case Citations

- [ ] Party names shortened properly (omit "Inc.", "Ltd." unless only identifier)
- [ ] "United States" abbreviated to "U.S." (as party, not "United States of America")
- [ ] Reporter abbreviation matches T1
- [ ] Court identifier included unless obvious from reporter
- [ ] Year is decision year, not argument year
- [ ] Pinpoint included for specific propositions

### Statutory Citations

- [ ] Current official code used (not session laws for current statutes)
- [ ] Section symbol (§) used, not "Section"
- [ ] Space between § and number
- [ ] Year is code edition year, not enactment year
- [ ] Supplements cited when applicable

### Short Forms

- [ ] Full citation appears earlier in same document
- [ ] Id. used only when no intervening citation
- [ ] Supra refers to footnote number where full cite appears
- [ ] Hereinafter defined in first full citation

## Progressive Disclosure

For detailed rules, consult:

### Reference Files

- **`references/cases.md`** - Complete case citation rules (R. 10)
- **`references/statutes.md`** - Statutory and regulatory citations (R. 12-14)
- **`references/secondary-sources.md`** - Books, articles, treatises (R. 15-17)
- **`references/short-forms.md`** - Id., supra, hereinafter rules (R. 4)
- **`references/quotations.md`** - Block quotes, alterations, ellipses (R. 5)
- **`references/signals-parentheticals.md`** - Signals, parentheticals, order (R. 1)
- **`references/audit-patterns.md`** - Citation audit patterns and validation
- **`references/abbreviations.md`** - Bluebook abbreviation tables
- **`references/editions-21-to-22.md`** - What changed in the 22nd edition, from the publisher's preface plus rule-by-rule checks

**Every reference file below is checked against the rule text.** `editions-21-to-22.md` is
not in the table because it is the SOURCE that verification was done against, not a subject
of it.

| file | rules | status |
|---|---|---|
| `quotations.md` | 5 | verified vs 21e scan AND 22e; 6 errors corrected |
| `signals-parentheticals.md` | 1 | rebuilt from 22e; carries the new `contrast` signal |
| `short-forms.md` | 4 | rebuilt from 22e |
| `cases.md` | 10 | rebuilt from 22e |
| `statutes.md` | 12 (13-14 NOT in corpus) | rebuilt from 22e; 13-14 flagged in place |
| `secondary-sources.md` | 15, 16, 17 | rebuilt from 22e |
| `abbreviations.md` | 10.2.2, 15.1(e), 16.1, T6 | rebuilt from 22e; T6 reproduced from the capture, table gaps flagged in place |
| `audit-patterns.md` | cross-cutting (1, 4, 10, 12, 15-18, T6) | rebuilt from 22e; every check names its rule, untraceable checks marked in place |

Five were then **adversarially re-verified** by separate agents against the same corpus, with
instructions to find errors rather than agree: `signals-parentheticals.md` and `short-forms.md`
came back with **zero contradictions** (every imperative traced to a governing sentence);
`cases.md`, `statutes.md` and `secondary-sources.md` each had defects, all now corrected.
`quotations.md`, `abbreviations.md` and `audit-patterns.md` had no second pass. Reports:
`scratch/bb22/verify/`.

All eight were checked against subsection pages extracted verbatim from the official Bluebook
Online 22nd edition; page cites in them are **22e** pages. Claims the corpus did not cover are
marked UNVERIFIED in place rather than left looking checked. Per-file reports:
`scratch/bb22/reports/`. Rule 5 verdicts: `scratch/bluebook-verify/REPORT.md`.

**What is still unchecked, and why.** "Rebuilt from 22e" means every claim traces to the extracted
corpus or is marked in place — it does not mean the whole rule surface was available. These gaps
are real and are flagged inside the files rather than papered over:

| gap | state of the capture | consequence |
|---|---|---|
| **Table T10** (geographical terms) | **captured in full** — T10.1 (22e pp. 340-42), T10.2 and T10.3 as separate subtable pages | its values may be stated |
| **Table T13** (institutional names in periodical titles, 22e pp. 346-48) | **captured in full** — the earlier empty capture used a wrong slug (`t13-institutional-names-...` rather than `t13-periodicals`) | its values may be stated |
| Tables T1, T7, T11, T12 and the rest | never fetched | cross-references to them are reported; their contents are not |
| Rules 6, 7, 8, 9, 11, 19 | never fetched | checks resting on them are marked, not asserted. Rules 3, 5, 20, 21 and 23 have since been extracted |

Nothing from these gaps has been filled from training knowledge. A claim depending on one is
either absent or carries a marker within a line of itself.

### Looking a rule up in the actual book

**Best source: the official Bluebook Online, 22nd edition.** UVA Law provides institutional
access and the browser on CDP 9222 is already signed in. This is live publisher text — no OCR, no
auth expiry, no retrieval tricks — and it is the source of record.

```
https://www.legalbluebook.com/bluebook/v22/rules/<n>-<slug>
https://www.legalbluebook.com/bluebook/v22/rules/<n>-<slug>/<n>-<m>-<slug>

e.g. /bluebook/v22/rules/5-quotations/5-2-alterations-and-quotations-within-quotations
```

Swap `v22` for `v21` to read the 21st edition; the site's own dropdown does the same. Drive it
with the `browser-automation` skill (Linux → `mcp__chrome-devtools__*` on 9222). If that MCP
server is not connected this session, raw CDP over `http://127.0.0.1:9222/json/list` works — and
**open a new tab rather than navigating the user's**.

**EDITION MATTERS, IN TWO WAYS.** The 22nd is now live and is the default.

**`references/editions-21-to-22.md` is the guide** — the publisher's preface (which names changes
in rules 1.2, 10.8.3, 12.4(f), 14.4, 15.1(d), 15.8, 18, 20.2.4, new 22 and 23, and tables T1.3,
T1.5, T2, T6, T10) plus the rule-by-rule differences verified here. Read it before trusting
anything in this skill against a 22e manuscript. Three things that bite immediately:

- **Rules 22 and 23 are NEW**; the 21st stops at 21. Rules 1-21 keep their numbers.
- **Pagination moved** — Rule 5 is 22e pp. 87-91 against 21e-scan pp. 103-108. A bare page cite is
  ambiguous; name the edition.
- **The preface's list is partial.** Rule 5.1(a)(i) gained "single spaced" in the 22nd and the
  preface never mentions it. Absence from the preface is not evidence a rule is unchanged.

### Pinpoint — the 21st edition, full scan



**Pinpoint holds the full 21st edition — use it.** A complete 394-page scan is in the `Bluebook`
collection (`b7425c3f3368f9c9`), OCR'd by Google, searchable to the page. This is the authoritative
lookup for any rule in this skill, and it is what `references/quotations.md` was finally verified
against.

```bash
pinpoint search Bluebook "<terms>" --pages --order density --limit 60
pinpoint generate ask Bluebook "<question>"       # locates fast; do NOT quote its paraphrase
```

Four things learned the hard way, all of which cost a pass:

- **`--order density`, not the default.** Document order means a bounded run stops early — Rule 5
  sits at scan pp. 103-108 and a default-ordered run never reached past p. 71.
- **It OR-matches; a quoted phrase returns zero.** Cast wide and filter locally with `awk`.
- **`--no-dedupe` when a page you know exists will not come back.** Rule 1.5(b) at p. 86 returned
  nothing across four term sets at limits up to 120; `--no-dedupe --limit 200` returned it in full.
- **Quote from `--pages`, never from `generate ask`.** It locates well and paraphrases
  confidently — it produced a fluent synthesis of a capitalization test that no line in the book
  supports.

Auth expires within the hour (`API error 7 (PermissionDenied)`); `pinpoint auth` re-lifts the
session from the CDP browser. Re-auth and retry — do not read an auth failure as "the rule is not
in the book."

### NotebookLM — narrow, and mostly superseded

The notebook (`f70a9976-b443-43d5-b5fd-43ff86b2b700`) holds a **53-page excerpt**, not the book.
Verified 2026-08-23: the only full rule text is **Rule 1 and 1.1-1.4** (pp. 51, 53) plus the Quick
Reference tables. Everything else is cover scans and cropped strips of the printed book's **thumb
tabs** — so "rule 10", "rule 12" appear as tab labels with nothing behind them, and a model asked
what the PDF contains will read those tabs and name rules it cannot quote. It did exactly that
before retracting under stricter questioning. It cannot answer on Rule 5 at all.

**Refuse its web-research offer.** On a rule it does not hold it replies "Would you like me to
perform some web research?" — observed three times. Accepting turns a web search into something
formatted as a source-grounded answer, which is how an unverified reference file gets written by
an author who believes they consulted the book.

Prefer Pinpoint above. Reach for the notebook only for Rule 1 or the Quick Reference tables:

**When to query the notebook:**
- Rule wording is ambiguous in reference files
- Formatting international or specialized materials
- Checking obscure abbreviations not in quick reference
- Resolving conflicts between rules
- Understanding historical changes from previous editions

### When to Load References

Load the specific reference when:
- Formatting an unfamiliar source type
- Encountering edge cases (unpublished cases, foreign sources)
- Checking state-specific reporter requirements
- Working with complex statutory schemes
- Formatting international materials

## Integration

Use with `/writing-legal` for complete legal scholarship workflow:
1. `/bluebook` formats citations correctly
2. `/writing-legal` ensures argument structure and evidence handling
3. `/ai-anti-patterns` catches AI writing indicators before submission

## Delete & Restart Pattern

**When to delete and restart:**

1. **Citation uses guessed page numbers** → Delete, verify source, cite with real numbers
2. **Id. follows intervening citation** → Delete id., use full short form
3. **Wrong signal used** → Delete, reread Rule 1.2, apply correct signal
4. **Typeface incorrect** → Delete, apply Rule 2 typeface
5. **Abbreviation doesn’t match Bluebook tables** → Delete, use table abbreviation

**How to restart:**

```
Old: See Smith v. Jones, 500 U.S. at 15. Id. at 20. [intervening cite] Id. at 25.
New: See Smith v. Jones, 500 U.S. at 15. Id. at 20. [intervening cite] Smith, 500 U.S. at 25.
```

The third cite cannot use id. after an intervening citation.
