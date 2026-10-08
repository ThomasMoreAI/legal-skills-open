---
name: ca-fact-check-codearranger
title: Fact-Check California Court Filings
description: 'Use to fact-check a California court filing (or packet) before filing. Triggers include "fact check this", "verify citations", "check my cites", "consistency check", "cite-check California", "verify the statute", "double-check the draft", "California Style Manual format", "verify CRC rule". Runs four passes: (1) citation verification — cites resolve to real sources with correct holdings using courts.ca.gov, CourtListener, and leginfo.legislature.ca.gov; (2) internal consistency — dates, parties, case number, amounts within document agree; (3) packet consistency — captions, parties, case number agree across documents; (4) sworn-vs.-argued consistency — no fact recited in motion contradicts a sworn declaration. Flags issues and proposes corrections without silently rewriting.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check California Court Filings

Use this skill to verify California court filings (or packets of
filings) before filing. The agent runs four passes and produces
a report. The user reviews the report and accepts or rejects each
proposed correction.

> **NOT LEGAL ADVICE.** Fact-checking verifies the surface — it
> does not tell you whether the legal position is winning. Pair
> with substantive review by counsel where stakes warrant.

## When to invoke

Before filing any of:

- Motion (any type)
- Memorandum of points and authorities in support
- Declaration with exhibits
- Proposed Order
- Notice of Hearing
- Answer with affirmative defenses and cross-complaint
- Brief on appeal

For a multi-document packet (motion + memorandum + declaration +
exhibits + proposed order + proof of service), invoke once and
check the whole packet for cross-document consistency.

## The four passes

### Pass 1: Citation verification

Every cite in the filing resolves to a real source. The cite
patterns:

- **California Supreme Court cases**: `[Party] v. [Party]
  ([Year]) [vol] Cal.[Nth] [page]` — verify against
  courts.ca.gov/opinions or CourtListener (court=cal)
- **California Court of Appeal**: `[Party] v. [Party] ([Year])
  [vol] Cal.App.[Nth] [page]` — verify against
  courts.ca.gov/opinions or CourtListener (court=calctapp)
- **9th Circuit**: `[Party] v. [Party], [vol] F.[Nth] [page]
  (9th Cir. [Year])` — verify against CourtListener
  (court=ca9)
- **U.S. Supreme Court**: `[Party] v. [Party] ([Year]) [vol]
  U.S. [page]` — verify against CourtListener (court=scotus)
- **Code Civ. Proc.**: `Code Civ. Proc., § [NNN]([sub])`
  — verify against leginfo.legislature.ca.gov
- **Cal. Civ. Code**: `Civil Code, § [NNN]([sub])` — verify
  against leginfo.legislature.ca.gov
- **Evid. Code**: `Evid. Code, § [NNN]([sub])` — verify
  against leginfo.legislature.ca.gov
- **Cal. Rules of Court**: `Cal. Rules of Court, rule [N.NNN]`
  — verify against courts.ca.gov/cms/rules
- **USC**: `[N] U.S.C. § [NNNN]([sub])` — verify against
  uscode.house.gov
- **CFR**: `[N] C.F.R. § [N.NN]` — verify against ecfr.gov

For each cite:

1. **Resolve**: does the cite exist?
2. **Quote**: if the filing quotes the source, does the quote
   match verbatim?
3. **Holding**: if the filing relies on a case for a
   proposition, does the case actually stand for that
   proposition?
4. **Currency**: has the case been overruled or distinguished?
   Has the statute been amended? Is the rule still in effect?
5. **Unpublished opinions**: California Rules of Court, rule
   8.1115 — unpublished California Court of Appeal opinions
   are generally **not citable**. Flag any citation to an
   unpublished opinion. Exceptions: (a) the opinion is being
   cited to show the law of the case, (b) the opinion is
   relevant under the doctrines of law of the case, res
   judicata, or collateral estoppel, or (c) the opinion is
   cited as a basis for a request for reconsideration.

Use WebFetch against the canonical URLs in
`ca-law-references/references/online-sources.md`. Do not use
other fetch mechanisms.

#### Common California citation errors to flag

| Pattern | Error |
|---|---|
| `Cal.4th.` (trailing period on reporter) | California Style Manual uses no period after Cal or App |
| `P.3d` or `Cal. Rptr. 3d` (internal spaces / periods) | California Style Manual: `Cal.Rptr.3d` (no space) |
| `CCP § 437c` | California Style Manual: `Code Civ. Proc., § 437c` (spell out; comma after "Proc.") |
| `CC § 1624` | California Style Manual: `Civil Code, § 1624` |
| `Evid. C. § 352` | California Style Manual: `Evid. Code, § 352` |
| `ORCP 21` | Oregon rule — wrong jurisdiction; California is `Code Civ. Proc., § 430.10` |
| `RCW [N.NN]` | Washington statute — wrong jurisdiction |
| `ORS [N.NNN]` | Oregon statute — wrong jurisdiction |
| `Fed. R. Civ. P. 12(b)(6)` | Federal rule; if in state court, correct is `Code Civ. Proc., § 430.10(e)` |
| Unpublished CA opinion without a permitted exception | CRC 8.1115 violation |
| `Rule 56` (federal MSJ) | California SJ is `Code Civ. Proc., § 437c` |
| Lettered exhibits | California convention often uses letters, but check local rules; LASC prefers tab identification |

### Pass 2: Internal consistency

Within a single document:

- **Caption case number** = body case-number references
- **Caption party names** = body party-name references
- **Document title** in caption = document title at top of body
  = document title in footer (if any)
- **Hearing date** in motion = hearing date in Notice of Hearing
- **Exhibit numbers/letters** referenced in body = exhibits
  attached
- **Dollar amounts** consistent throughout
- **Date references** consistent (service date, judgment date,
  payment date)
- **Paragraph cross-references** point to actual paragraphs
- **Pin cites** to exhibits and pages are accurate

### Pass 3: Packet consistency

Across multiple documents in a single filing packet:

- **All captions are identical** (same court header, same
  parties in same order, same case number, same department)
- **All document titles** match what the body actually contains
- **Hearing date / time / department / mode** identical across
  motion, notice of hearing, and proposed order
- **Exhibit identification** cross-referenced across documents
  (motion ¶ 4 cites "Decl. Smith, ¶ 3, Ex. A"; Declaration's
  Exhibit A must contain what is described)
- **Signature blocks** identical across documents in the packet
- **Service lists** include the same parties in the same order
- **Judicial Council form version dates** — check the revision
  date printed on the form (courts.ca.gov/forms) to confirm the
  form being used is current

### Pass 4: Sworn-vs.-argued consistency

The single most damaging fact-check failure: a memorandum
**argues** a fact that contradicts what a **declaration** (signed
under penalty of perjury under Code Civ. Proc., § 2015.5) states.

Example:
- Declaration ¶ 7: "I received the letter on April 3, 2025."
- Memorandum at p. 4: "Defendant received the letter on
  March 28, 2025."

These cannot both be true. The fact-check pass identifies every
assertion in the memorandum that purports to recite a fact, locates
the supporting paragraph in the declaration, and compares them.

Discrepancies are flagged with:
- The memorandum language
- The declaration language
- A proposed correction (typically updating the memorandum to
  conform to the sworn declaration)

## Output format

```
=== Fact-Check Report ===
Packet: [Motion to Compel + Memorandum + Declaration + Proposed
         Order + Notice of Hearing]
Date: [today]

Pass 1: Citation Verification
  [PASS] Zamora v. Clayborn Contracting Group (2002) 28 Cal.4th 249
  [PASS] Code Civ. Proc., § 437c(a)(2)
  [WARN] Doe v. Roe (2021) 67 Cal.App.5th 123
         — Verify holding supports proportionality argument;
         confirm not overruled
  [FAIL] Smith v. Jones (2018) 28 Cal.App.5th 1001 [UNPUBLISHED]
         — CRC 8.1115 prohibits citation to unpublished opinions
         unless an exception applies. Remove or replace with a
         published opinion supporting the same proposition.

Pass 2: Internal Consistency
  [PASS] Caption case number matches body
  [WARN] Motion ¶ 8 references "Exhibit C"; Declaration lists
         Exhibits A and B only. Either add Exhibit C or correct
         the reference.

Pass 3: Packet Consistency
  [PASS] All captions identical
  [FAIL] Motion states hearing is "Dept. 32"; Notice of Hearing
         says "Dept. 36". Reconcile — confirm reserved department.

Pass 4: Sworn-vs.-Argued Consistency
  [FAIL] Memorandum p. 3 states "Defendant received the collection
         letter on March 28, 2025."
         Declaration ¶ 7 states "I received the letter on April 3,
         2025." Reconcile (conform the memorandum to the sworn
         declaration).

Summary: 3 PASS, 2 WARN, 3 FAIL — review and correct before filing.
```

## What this skill does NOT do

- It does NOT silently rewrite the filing. All flags require user
  review.
- It does NOT verify the legal soundness of the argument — whether
  citations actually support the proposition is for the user.
- It does NOT check substantive law applicability.
- It does NOT check timing — that is `ca-deadlines`.
- It does NOT check format — that is `ca-quality-check`.

## How to invoke

```
User: Fact-check the demurrer packet I just drafted.
Agent: [Runs the four passes, produces the report]
User: For the unpublished opinion FAIL, find me a published
      California case supporting the same proposition.
Agent: [Researches and proposes an alternative citation]
```

The user remains in control of every change.

## Citation verification — WebFetch templates

### California Supreme Court case

```
WebFetch:
  url: https://www.courtlistener.com/?q=%22[Case Name]%22&type=o&court=cal
  prompt: Verify this California Supreme Court citation:
          [Party] v. [Party] ([Year]) [vol] Cal.[Nth] [page].
          Confirm (1) the case exists at the cited reporter and
          page, (2) the year, and (3) the case is still good law.
          If the case has been overruled or limited, identify the
          later case.
```

### California Court of Appeal case

```
WebFetch:
  url: https://www.courtlistener.com/?q=%22[Case Name]%22&type=o&court=calctapp
  prompt: Verify this California Court of Appeal citation:
          [Party] v. [Party] ([Year]) [vol] Cal.App.[Nth] [page].
          Confirm the citation, year, whether it is published,
          and whether it is still good law.
```

### California statute

```
WebFetch:
  url: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=[CODE]&sectionNum=[SECTION]
  prompt: Locate [Code Name], § [section]([subsection]).
          Quote the verbatim text. Identify the most recent
          legislative amendment.
```

### California Rules of Court

```
WebFetch:
  url: https://www.courts.ca.gov/cms/rules/index.cfm?title=[N]&rule=[N.NNN]
  prompt: Locate Cal. Rules of Court, rule [N.NNN].
          Quote the verbatim text. Identify the effective date
          of the current version.
```

### Federal statute

```
WebFetch:
  url: https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title[N]-section[NNNN]&num=0&edition=prelim
  prompt: Locate [title] U.S.C. § [section]([subsection]).
          Quote the verbatim text.
```

### Federal regulation

```
WebFetch:
  url: https://www.ecfr.gov/current/title-[N]/part-[NNNN]/section-[NNNN].[NN]
  prompt: Locate [title] C.F.R. § [N.NN]. Quote the verbatim
          text as currently in effect.
```

## Pre-fact-check checklist (for the user)

Before invoking the skill, ensure:

- [ ] Draft is reasonably complete (no placeholder "[citation]"
      entries)
- [ ] All exhibits referenced are listed
- [ ] All key dates are filled in
- [ ] Spell-check and grammar-check have been run
- [ ] Unpublished opinions are flagged by you if intentionally
      cited under an exception

## Cross-references

- `ca-law-references/references/online-sources.md` — canonical
  fetch URLs
- `ca-law-references/references/citation-format.md` — California
  Style Manual conventions
- `ca-quality-check` — format pass (paper, margins, fonts, footer)
- `ca-file-packet` — final-packet preflight
- All draft-* skills — the documents that get fact-checked

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
