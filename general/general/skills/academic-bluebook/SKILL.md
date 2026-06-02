---
name: academic-bluebook
title: Academic Bluebook Citation Skill
description: Citation formatting rules for law review articles using The Bluebook (21st ed.) academic style
author: diegosouzapw
author_url: https://github.com/diegosouzapw/awesome-omni-skill/tree/main/skills/development/academic-bluebook
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Academic Bluebook Citation Skill

**Domain:** Legal citation formatting
**Version:** 1.0.0
**Last Updated:** 2025-12-15

## Overview

This skill provides rules for formatting citations in Academic Bluebook style (law review format), as distinguished from practitioner format. Law reviews use footnotes rather than inline citations and have specific conventions for typeface, signals, and short forms.

## Key Differences: Academic vs. Practitioner

| Element | Academic (Law Review) | Practitioner |
|---------|----------------------|--------------|
| Citations | Footnotes | Inline |
| Case names | *Italicized* | Not italicized |
| Book titles | SMALL CAPS | Not small caps |
| Article titles | *Italicized* | Not italicized |
| Signals | Required per Rule 1.2 | Often omitted |

## Core Citation Forms

### Law Review Articles (Rule 16)

**Full citation:**
```
Author First Last, *Article Title*, Vol. J. Abbr. First Page, Pincite (Year).
```

**Examples:**
```
John Smith, *The Prosecutor's Discretion*, 100 Harv. L. Rev. 1, 15 (2020).
Jane Doe & John Roe, *Joint Authorship*, 50 Yale L.J. 100 (2021).
```

**Short form:**
```
Smith, supra note 5, at 20.
```

### Books (Rule 15)

**Full citation:**
```
Author First Last, Title Page (ed. Year).
```

**Examples:**
```
Ronald Dworkin, Law's Empire 45 (1986).
John Rawls, A Theory of Justice 15-20 (rev. ed. 1999).
```

**Short form:**
```
Dworkin, supra note 3, at 50.
```

### Cases (Rule 10)

**Full citation:**
```
Case Name, Vol. Reporter First Page, Pincite (Court Year).
```

**Examples:**
```
Brown v. Board of Education, 347 U.S. 483, 495 (1954).
People v. Smith, 123 N.E.2d 456, 460 (N.Y. 2020).
```

**Short form:**
```
Brown, 347 U.S. at 490.
```

### Statutes (Rule 12)

**Examples:**
```
42 U.S.C. § 1983 (2018).
Cal. Penal Code § 187 (West 2020).
```

### Constitutions (Rule 11)

**Examples:**
```
U.S. Const. art. I, § 8, cl. 3.
U.S. Const. amend. XIV, § 1.
```

## Signals (Rule 1.2)

Use signals to show relationship between citation and proposition:

| Signal | Meaning |
|--------|---------|
| [no signal] | Direct support |
| *See* | Implicit support |
| *See also* | Additional support |
| *Cf.* | Analogous support |
| *Compare...with* | Comparison illuminates |
| *See generally* | Background |
| *E.g.* | One of many examples |
| *But see* | Contradicts |
| *Contra* | Directly contradicts |

**Order of signals:** Supportive → Comparative → Contradictory → Background

## Id. and Supra (Rules 4.1, 4.2)

### Id.
Use when citing the immediately preceding authority:
```
¹ Smith, supra note 5, at 20.
² Id. at 25.
³ Id.
```

**Rules:**
- *Id.* replaces the entire previous citation
- Add pincite if different: *Id. at 30*
- Cannot use after a footnote citing multiple sources
- Italicize *Id.*

### Supra
Use for non-case authorities after full citation:
```
Smith, supra note 5, at 30.
```

**Rules:**
- Include "note X" reference to original full citation
- Never use *supra* for cases (repeat short form instead)
- Italicize *supra*

## Hereinafter (Rule 4.2(b))

For long titles, establish short form:
```
¹ Model Penal Code § 2.02 (Am. L. Inst. 1962) [hereinafter MPC].
...
¹⁵ MPC, supra note 1, § 2.03.
```

## Parentheticals (Rule 1.5)

Add explanatory information after citation:
```
Smith v. Jones, 500 U.S. 100, 105 (2000) (holding that...).
Doe, supra note 3, at 50 (arguing that...).
```

**Common parenthetical starters:**
- (holding that...)
- (arguing that...)
- (noting that...)
- (explaining that...)
- (quoting Source)
- (citing Source)
- (emphasis added)
- (alteration in original)

## String Citations (Rule 1.4)

Separate with semicolons, order by:
1. Constitutions
2. Statutes
3. Treaties
4. Cases (by court hierarchy, then reverse chronological)
5. Secondary sources (by type, then alphabetical)

```
See U.S. Const. amend. IV; 18 U.S.C. § 2511 (2018); Katz v. United States, 389 U.S. 347 (1967); Smith, supra note 5, at 20.
```

## Common Journal Abbreviations

| Journal | Abbreviation |
|---------|-------------|
| Harvard Law Review | Harv. L. Rev. |
| Yale Law Journal | Yale L.J. |
| Stanford Law Review | Stan. L. Rev. |
| Columbia Law Review | Colum. L. Rev. |
| Michigan Law Review | Mich. L. Rev. |
| Virginia Law Review | Va. L. Rev. |
| California Law Review | Calif. L. Rev. |
| Georgetown Law Journal | Geo. L.J. |

## Available Workflows

- `workflows/format-citation.md` - Format a single citation
- `workflows/check-citation-order.md` - Verify string citation ordering
- `workflows/generate-bibliography.md` - Create bibliography from footnotes

## Common Errors to Avoid

1. **Using practitioner format** - Remember: italics, footnotes, signals
2. **Incorrect Id. usage** - Only for immediately preceding single source
3. **Supra for cases** - Never; use short case form instead
4. **Missing signals** - Every citation needs appropriate signal or no signal
5. **Wrong parenthetical tense** - Use present participle (holding, arguing)
6. **Inconsistent short forms** - Establish and maintain throughout

## Quick Reference Card

```
ARTICLES:    Author, *Title*, Vol. J. Abbr. Page, Pin (Year).
BOOKS:       Author, Title Page (ed. Year).
CASES:       Name, Vol. Rep. Page, Pin (Ct. Year).
STATUTES:    Title U.S.C. § Sec (Year).

SHORT FORMS:
  Id. / Id. at Pin          (same source, immediately prior)
  Author, supra note X      (articles, books - not cases)
  Name, Vol. Rep. at Pin    (cases)

SIGNALS:  [none] | See | See also | Cf. | But see | See generally
```

---

*Academic Bluebook style is the standard for legal scholarship.*
