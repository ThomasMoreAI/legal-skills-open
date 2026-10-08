---
name: output-citation-format-bluebook-sboghossian
title: Bluebook Citation Format (US)
description: Use when formatting legal citations for a US-trained audience using the Bluebook system (Harvard citation style). Covers case citations, statutes, regulations, Restatements, law review articles, and books — including short-form and id. conventions. Apply only when the reader is US-trained; for UK/DIFC audiences use OSCOLA, and for MENA civil-law jurisdictions use the civil-law or MENA citation formats.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-citation-format-bluebook
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# Bluebook Citation Format (US)

## When to use this

Apply Bluebook format when:
- The output is a US legal memo, brief, or law review article.
- The reader is US-trained (US law school graduate, US-qualified lawyer, or a document governed by US law).
- The document will be filed in a US court or submitted to a US legal publication.

Do **not** apply Bluebook in MENA, UK, or EU contexts — those jurisdictions use different citation standards (see [[output-citation-format-oscola]], [[output-citation-format-civil-law-fr]], [[output-citation-mena-conventions]]).

## Core rules

Bluebook uses two styles:
- **Law Review style** (academic): case names in large and small caps, heavy italics use.
- **Practitioner style** (briefs, memos): case names in ordinary italics or plain text depending on the context.

The examples below use practitioner style, which is the default for legal AI outputs.

## Citation formats

### Cases

```
Smith v. Jones, 595 F.3d 1233, 1240 (5th Cir. 2010).
```

Components:
1. **Case name** (italicized): first party v. second party
2. **Volume number**: the volume of the reporter
3. **Reporter abbreviation**: F.3d (Federal Reporter, Third Series), U.S., S. Ct., etc.
4. **First page** of the case
5. **Pin-cite** (the specific page cited): after a comma
6. **Parenthetical**: (Court abbreviation Year) — include court only if not obvious from the reporter
7. **Period** at end

Common reporter abbreviations:
| Reporter | Abbreviation |
|----------|-------------|
| United States Reports | U.S. |
| Supreme Court Reporter | S. Ct. |
| Federal Reporter (2d/3d) | F.2d / F.3d |
| Federal Supplement (2d/3d) | F. Supp. 2d / F. Supp. 3d |
| State reporters | Varies by state |

### Statutes

```
17 U.S.C. § 107 (2018).
```

Components: Title number, Code abbreviation (U.S.C. = United States Code), section symbol, section number, (year of code edition).

For codified state statutes:
```
Cal. Civ. Code § 1542 (West 2023).
```

### Regulations

```
17 C.F.R. § 240.10b-5 (2024).
```

C.F.R. = Code of Federal Regulations. Format: title, C.F.R., section.

For the Federal Register:
```
Securities Act Release No. 33-11216, 88 Fed. Reg. 44485 (July 12, 2023).
```

### Restatements

```
Restatement (Second) of Contracts § 90 (Am. L. Inst. 1981).
```

Components: Restatement (Edition) of Subject, section, (American Law Institute year).

### Law review articles

```
John Smith, The Article Title, 100 Harv. L. Rev. 1, 5 (2020).
```

In law review style, the title is in large and small caps. In practitioner style, the title is in regular text (or italicized, per local rules). Author name is not italicized.

Components: Author, *Title*, Volume Journal-Abbreviation First-Page, Pin-Cite (Year).

Common journal abbreviations: Harv. L. Rev., Yale L.J., Stan. L. Rev., Colum. L. Rev., N.Y.U. L. Rev.

### Books

```
John Smith, The Book Title 25 (3d ed. 2019).
```

Components: Author, *Title* Page (edition year). In practitioner style, title is italicized; in law review style, it is in large and small caps.

## Short forms

After a full citation has been given, subsequent citations to the same source use abbreviated forms:

| Situation | Form | Example |
|-----------|------|---------|
| Immediately preceding source, same page | *Id.* | *Id.* |
| Immediately preceding source, different page | *Id.* at [page] | *Id.* at 1245 |
| Same case, not immediately preceding | *[Party name]*, [vol.] [reporter] at [page] | *Smith*, 595 F.3d at 1245 |
| Same statute, not immediately preceding | § [section] | § 107 |

*Id.* is always italicized and always has a period. Use only when the preceding citation is unambiguous — do not use *id.* if the preceding footnote cites multiple sources.

## Footnotes vs in-text

- **Law review articles**: citations go in footnotes only (not in-text).
- **Briefs and memos**: citations go in-text (not footnotes), unless local court rules require footnotes.

## Common mistakes

| Mistake | Correct form |
|---------|-------------|
| `Smith v. Jones (5th Cir. 2010)` | `Smith v. Jones, 595 F.3d 1233, 1240 (5th Cir. 2010).` |
| `17 USC 107` | `17 U.S.C. § 107 (2018).` |
| Using *id.* after a string cite | Use the short form instead |
| Forgetting the pin-cite | Always pin-cite; a first-page cite is not sufficient for a specific proposition |

## Related skills

- [[output-citation-format-oscola]] — UK/DIFC/common-law citation format
- [[output-citation-format-civil-law-fr]] — French-style civil-law citation format
- [[output-citation-mena-conventions]] — MENA jurisdiction citation conventions
- [[output-creac-structure]] — the CREAC structure that uses these citations in legal memos
