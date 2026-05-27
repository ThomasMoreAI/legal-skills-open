---
name: citation-bluebook
title: Bluebook Citation Format
description: Formats legal citations per The Bluebook (21st ed.) using Bluepages practitioner conventions. Use when citing authority in court filings, checking citation format, drafting briefs or memoranda, or formatting a table of authorities.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/citation-bluebook
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Bluebook Citation Format

Practitioner-format citation rules (Bluepages) for cases, statutes, rules, regulations, and secondary sources.

## Quick Start

Most common pattern — full case citation with pincite:

*Smith v. Jones*, 123 F.3d 456, 458 (9th Cir. 2020)

Structure: *Party v. Party*, Vol. Reporter Pg., Pincite (Court Year)

## Cases

| Form | Pattern | Example |
|------|---------|---------|
| Full | *Party v. Party*, Vol. Reporter Pg., Pincite (Court Year) | *Smith v. Jones*, 123 F.3d 456, 458 (9th Cir. 2020) |
| Short | *Party*, Vol. Reporter at Pincite | *Smith*, 123 F.3d at 459 |
| Id. | *Id.* at Pincite | *Id.* at 460 |
| Subsequent history | Append with comma | *Smith v. Jones*, 123 F.3d 456 (9th Cir. 2020), *aff'd*, 540 U.S. 100 (2003) |

Key rules:
- Italicize case names including *v.*
- Omit "Inc.," "Ltd.," "Co." when other party-description words present (R. 10.2.1(h))
- Abbreviate court names per T.7; omit court if obvious from reporter (U.S. Reports → Supreme Court)
- *Id.* only for the immediately preceding authority

## Statutes & Constitutions

| Type | Example |
|------|---------|
| Federal statute | 42 U.S.C. § 1983 (2018) |
| State statute | Cal. Civ. Code § 1542 (West 2020) |
| U.S. Constitution | U.S. Const. amend. XIV, § 1 |
| State constitution | Cal. Const. art. I, § 7 |

- "§" (single) or "§§" (range) — always space after the symbol
- Include code year in parenthetical; cite current version unless historical version is relevant

## Rules & Regulations

| Type | Example |
|------|---------|
| Fed. R. Civ. P. | Fed. R. Civ. P. 12(b)(6) |
| Fed. R. Evid. | Fed. R. Evid. 702 |
| Fed. R. App. P. | Fed. R. App. P. 28(a) |
| C.F.R. | 29 C.F.R. § 1630.2(j) (2020) |
| Fed. Reg. | 85 Fed. Reg. 12,345 (Mar. 2, 2020) |

## Secondary Sources

| Type | Example |
|------|---------|
| Restatement | Restatement (Second) of Contracts § 90 (Am. L. Inst. 1981) |
| Treatise | 5 Wright & Miller, *Federal Practice and Procedure* § 1216 (3d ed. 2004) |
| Law review | Sunstein, *On the Expressive Function of Law*, 144 U. Pa. L. Rev. 2021, 2025 (1996) |
| A.L.R. | Annotation, *Title*, 100 A.L.R.5th 1 (2002) |
| Black's Law Dict. | *Term*, Black's Law Dictionary (12th ed. 2024) |

## Signals

| Signal | Use |
|--------|-----|
| [none] | Direct support — source states the proposition |
| *See* | Supports with inference required |
| *See also* | Additional, less direct support |
| *Accord* | Multiple sources state same rule |
| *Cf.* | Support by analogy |
| *But see* | Directly contrary |
| *But cf.* | Contrary by analogy |
| *See generally* | Background or general support |

- Italicize signals; capitalize only at the start of a citation sentence
- Order authorities within a signal per R. 1.4: constitutions → statutes → cases (by court hierarchy) → secondary sources

## Short Forms

- **Cases:** *Id.* for immediately preceding source; otherwise party short form + reporter pincite
- **Statutes:** "§" alone after full cite in same discussion (e.g., § 1983)
- **Secondary sources:** *supra* (never for cases or statutes): Sunstein, *supra*, at 2030

## Common Pitfalls

- **Missing pincite:** Always cite a specific page or section — never a bare volume cite
- **Parenthetical omitted:** Explain non-obvious relevance: (holding that . . .)
- **Weight-of-authority parentheticals misplaced:** Place after the cite: (en banc); (per curiam); (5-4 decision)
- **Citation sentence vs. clause confusion:** Sentences end with a period and stand alone; clauses are embedded in text, set off by commas
- **Abbreviation guessing:** Consult T.6 (case names), T.7 (court names), T.10 (geographical terms) rather than improvising

---

**Changes from original:**
- Removed `tags` from frontmatter (not part of the spec — only `name` and `description`)
- Tightened description to include trigger guidance without keyword-stuffing
- Added **Quick Start** section showing the most common citation pattern upfront
- Renamed table columns from "Format" to "Example" (they were examples, not format specs)
- Trimmed signal descriptions for conciseness (removed *Compare...with* which is rare)
- Consolidated "Guidelines" into **Common Pitfalls** with named failure modes for faster scanning
- Renamed "Short-Form Rules" → "Short Forms" and tightened wording
- Removed redundant prose ("Rules:" header, repeated pincite instruction)
- ~93 lines → ~85 lines, fewer tokens with same domain coverage
