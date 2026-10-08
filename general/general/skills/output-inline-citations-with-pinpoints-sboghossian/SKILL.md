---
name: output-inline-citations-with-pinpoints-sboghossian
title: Inline Citations with Pin-Cites
description: Use when Claude must embed legal authority inline within analysis, memos, or drafted clauses with precise pin-cites. Applies across MENA (UAE, KSA, Lebanon, Egypt), DIFC/ADGM, and common-law (UK, US) contexts. Triggers on any request for citation format, source referencing, or when another skill must support its legal propositions with verified authority.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-inline-citations-with-pinpoints
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Inline Citations with Pin-Cites

Precise citation of legal authority is the backbone of credible legal analysis. This skill governs how Claude embeds citations inline — statute, case, regulation, and secondary source — so that every legal proposition in a memo, advice note, or draft is fully traceable and verifiable.

## When this applies

Activate whenever Claude asserts a legal rule, threshold, duty, right, or standard. Every assertion of law must be backed by a citation or marked with `[citation needed]`. This is not optional for legal output — an unsourced legal claim is worse than no claim.

## Citation formats by authority type

### Statutes and legislation

| Jurisdiction | Format | Example |
|---|---|---|
| Lebanon | `[Statute name] LB art [N]` | `Civil Code LB art 1124` |
| UAE federal | `[Decree-Law / Law] [No.]/[Year] UAE art [N]` | `Federal Decree-Law 33/2021 UAE art 10` |
| KSA | `[Statute name] RD [M/N] art [N]` | `Saudi Labor Law RD M/51 art 80` |
| DIFC | `DIFC Law [N]/[Year] art [N]` | `DIFC Law 4/2021 art 17` |
| ADGM | `ADGM [Regulation/Act/Rules] [Year] s [N]` | `ADGM Employment Regulations 2019 s 11` |
| Qatar / QFC | `QFC [Law name] [Year] art [N]` | — |
| Egypt | `[Statute name] EG Law [N]/[Year] art [N]` | `Civil Code EG Law 131/1948 art 147` |
| France | `C. civ. art [N]` or `C. com. art [N]` | `C. civ. art 1231-1` |
| EU | `[Regulation/Directive] [No.]/[Year]/EU art [N]` | `GDPR Reg. 2016/679/EU art 6(1)(b)` |
| UK | `[Act name] [Year] s [N]` | `Companies Act 2006 s 172` |

### Cases — common-law jurisdictions

Format: `[Party A] v [Party B] [year] [court] [number] at [para/page]`

- DIFC: `Khoury v. Acme [2024] DIFC CFI 47 at [23]`
- UK: `Cavendish Square v. Makdessi [2015] UKSC 67 at [32]`
- ADGM: `[Party] v [Party] [year] ADGM CFI [N]`
- US (Bluebook short form): `Smith v. Jones, 123 F.3d 456, 461 (2d Cir. 2001)` — see [[output-citation-format-bluebook]]
- Australia: `[Party] v [Party] (year) volume CLR page`

### Cases — civil-law jurisdictions

Format varies by court; use the official registry style where possible.

- French Cour de cassation: `Cass. com., 12 mai 2023, n° 21-15.847`
- Lebanese Court of Cassation: `Cass. civ. LB, n° [N], [date]`
- Egyptian Court of Cassation: `Cass. EG [circuit], n° [N], [year]`
- UAE Federal Supreme Court: `UAE Fed. Sup. Ct. [circuit], n° [N], [year/Hijri]`

### Regulatory instruments

- UAE: `[Agency] Circular [N]/[Year]` or `[Agency] Decision [N]/[Year]`
- KSA: `SAMA Circular [N]/[Hijri-year] dated [Gregorian or Hijri date]` · `CMA Decision [N]/[Year]`
- DIFC: `DFSA [Rulebook Chapter]/[Module] Rule [N]`
- Lebanon: `BDL Circular [N] dated [date]`

Example: `SAMA Circular 67/41 dated 15/3/1443H`

### Secondary sources

Author, Title, Publisher/Journal, Year, Page/Section:
`Nayla Comair-Obeid, "Contracts in Arab Countries," Bruylant (2013), p. 214`

## Inline placement rules

**Prose integration** — weave the authority into the sentence:
> *Under Article 10 of UAE Federal Decree-Law 33/2021, a non-compete clause must be proportionate in scope, geography, and duration.*

**Parenthetical** — cite after the proposition, before the period:
> *An employee dismissed without cause is entitled to notice pay (*UAE FDL 33/2021 art 43*).*

**Footnote** — acceptable for printed memos; use `[^1]` markdown footnote syntax if the rendering stack supports it. Otherwise collect at bottom in a Sources block (see [[output-source-attribution-block]]).

**Multiple authorities** — list separated by `;`:
> *(UAE FDL 33/2021 art 10; Cabinet Decision 1/2022)*

## Pin-cite precision

A pin-cite is the specific page, paragraph, or article number that supports the exact proposition. Without it, a citation is useless under cross-examination.

- Statute: cite the specific article and sub-article: `art 10(1)(b)`
- Case: paragraph number `at [42]` or page `at p. 123`
- Regulation: section and sub-section
- Circular/Notice: the operative paragraph if available

## When uncertain — the cite-or-bust rule

**Never fabricate citations.** If the exact source is not verified:
1. Write `[citation needed]` inline.
2. Surface to the user: "I believe this rule exists in [general framework] but cannot confirm the specific article. Please verify before relying on this."
3. Do not guess article numbers or case references.

An invented citation discovered by the other side is catastrophic. See the confidence-scoring rule in [[router-confidence-scorer]].

## Audience-specific style

| Audience | Citation style | Notes |
|---|---|---|
| MENA practitioners | Light formal: statute name + article | Arabic statute names may be included in parentheses |
| US lawyer | Bluebook — [[output-citation-format-bluebook]] | Full citation first use, short form after |
| UK lawyer | OSCOLA — [[output-citation-format-oscola]] | Footnotes preferred |
| French / Lebanese civil-law | Doctrine + jurisprudence style | [[output-citation-format-civil-law-fr]] |
| Board / non-lawyer audience | Narrative reference: "the UAE employment law" | Full cite in footnote/appendix |

## Hijri / dual-date handling

Saudi and some UAE/Bahraini regulatory instruments use Hijri dates. Always note both calendars when available:
> `SAMA Circular 67/41 dated 15/3/1443H (12 October 2021)`

If only the Hijri date is given, note conversion used:
> `[Hijri date] (approx. [Gregorian])` — conversion using standard Umm al-Qura calendar.

## Related skills

- [[output-source-attribution-block]]
- [[output-irac-structure]]
- [[output-partner-memo-style]]
- [[router-confidence-scorer]]
- [[output-citation-format-bluebook]]
- [[output-citation-format-oscola]]
- [[output-citation-format-civil-law-fr]]
