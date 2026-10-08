---
name: output-citation-format-oscola-sboghossian
title: OSCOLA Citation Format (UK / DIFC / ADGM)
description: Use when formatting legal citations for a UK-trained audience, or for common-law jurisdictions that follow UK legal culture — including DIFC and ADGM. OSCOLA (Oxford Standard for the Citation of Legal Authorities) uses footnotes rather than in-text parenthetical citations, and differs structurally from Bluebook in case name formatting, year-in-brackets convention, and statutory citation style.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-citation-format-oscola
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# OSCOLA Citation Format (UK / DIFC / ADGM)

## When to use this

Apply OSCOLA format when:
- The output is for a UK-trained reader or will be used in a UK legal context.
- The document will be used in DIFC or ADGM proceedings, which apply English common law and UK-style citation conventions.
- The document will be filed in or presented to an English-language common-law court in the MENA region (DIFC Courts, ADGM Courts).
- The output is a legal opinion or memo citing English, DIFC, or ADGM case law or statute.

Do **not** apply OSCOLA for purely US outputs (use Bluebook), purely French-law outputs (use civil-law French format), or MENA-law outputs in Arabic (use MENA conventions).

## Key structural differences from Bluebook

- OSCOLA uses **footnotes** exclusively for citations — never in-text parenthetical.
- Case names are italicized but court abbreviations are in brackets, not in parentheses.
- Year is in **square brackets** `[1932]` when the year is needed to identify the volume; in **round brackets** `(1932)` when it is supplementary information.
- No period at the end of a citation (unlike Bluebook's trailing period).

## Citation formats

### Cases

```
Donoghue v Stevenson [1932] AC 562 (HL) 580
```

Components:
1. **Case name** (italicized): *Donoghue v Stevenson* — note: `v` not `v.` in OSCOLA
2. **Year in brackets** `[1932]` — square brackets when the year identifies the volume
3. **Volume** (if any) — omit if the year already identifies the volume
4. **Reporter abbreviation**: AC (Appeal Cases), All ER, WLR, QB, Ch, etc.
5. **First page** of the case
6. **Court in brackets** `(HL)` — only include if not obvious from the reporter
7. **Pin-cite** (specific page referenced)

**Common reporter abbreviations**:
| Reporter | Abbreviation |
|----------|-------------|
| Appeal Cases | AC |
| All England Law Reports | All ER |
| Weekly Law Reports | WLR |
| Queen's/King's Bench | QB / KB |
| Chancery Division | Ch |
| Neutral citation (UKSC) | [2023] UKSC 14 |

**Neutral citations** (post-2001): use the neutral citation alone when no traditional reporter is available:
```
R (Miller) v Secretary of State for Exiting the European Union [2017] UKSC 5
```

### DIFC and ADGM cases

DIFC Court judgments use a neutral citation system:
```
Corinth Pipeworks SA v Barclays Bank plc [2011] DIFC CA 002
```

ADGM Court judgments:
```
Re IQ EQ Consulting [2023] ADGMCFI 0001
```

### Statutes

```
Companies Act 2006, s 172
```

Components: Statute name (not italicized), year, section abbreviation.

No comma between the statute name and year. Section is abbreviated `s` (not `§` or `sec.`).

For schedules and paragraphs:
```
Companies Act 2006, Sch 7, para 3
```

### Statutory instruments

```
Insolvency Rules 2016, SI 2016/1024, r 7.1
```

Format: SI Year/Number, rule abbreviation.

### DIFC and ADGM legislation

DIFC laws use a numbered system:
```
DIFC Law No 2 of 2019 (DIFC Contract Law)
```

ADGM regulations:
```
ADGM Financial Services and Markets Regulations 2015, reg 15
```

### Books

```
Andrew Burrows, English Private Law (3rd edn, OUP 2013) 145
```

Components: Author Surname, *Title* (edition, Publisher Year) Page — no comma between the closing parenthesis and the page number.

### Articles

```
Roderick Bagshaw, 'The Pleading of Negligence' (2019) 135 LQR 459, 465
```

Components: Author Surname, 'Article title in single quotes' (Year) Volume Journal-Abbreviation First-Page, Pin-Cite.

Note: article titles are in single quotes, not italics.

**Common journal abbreviations**:
| Journal | Abbreviation |
|---------|-------------|
| Law Quarterly Review | LQR |
| Modern Law Review | MLR |
| Cambridge Law Journal | CLJ |
| Oxford Journal of Legal Studies | OJLS |

## Subsequent references (short forms)

| Situation | Form | Example |
|-----------|------|---------|
| Immediately preceding footnote, same source | ibid | ibid |
| Immediately preceding, different page | ibid 580 | ibid 580 |
| Not immediately preceding, same case | *[Party name]* (n [footnote number]) | *Donoghue* (n 3) |
| Not immediately preceding, same book | Author (n [footnote number]) page | Burrows (n 7) 150 |

Note: OSCOLA uses `ibid` (not `id.`); no period after `ibid`.

## Footnote placement

In academic and formal practitioner documents following OSCOLA:
- Footnotes are placed at the bottom of the page or the end of the document.
- Every citation appears in a footnote, numbered consecutively.
- The body text contains no parenthetical citations.

In-text parenthetical citations (as in Bluebook memos) are not OSCOLA practice.

## Common mistakes

| Mistake | Correct |
|---------|---------|
| `Donoghue v. Stevenson` | `Donoghue v Stevenson` (no period after `v`) |
| `(1932) AC 562` | `[1932] AC 562` (square brackets for year as volume identifier) |
| `Companies Act 2006, §172` | `Companies Act 2006, s 172` |
| Using `id.` | Use `ibid` |
| In-text parenthetical citation | Footnote only in OSCOLA |

## Related skills

- [[output-citation-format-bluebook]] — for US-trained audiences
- [[output-citation-format-civil-law-fr]] — for French-law audiences
- [[output-citation-mena-conventions]] — for MENA-specific statutory citations
- [[output-creac-structure]] — the legal memo structure that uses these citations
