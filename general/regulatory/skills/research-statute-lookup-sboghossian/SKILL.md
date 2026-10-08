---
name: research-statute-lookup-sboghossian
title: Statute Lookup
description: 'Use when a user needs the current text of a specific statute, article, or regulation — not a summary or paraphrase, but the actual verbatim text with citation, effective date, and authoritative source link. MENA-primary: covers Lebanon (Official Gazette), KSA (Bureau of Experts), UAE federal (MOJ), DIFC (Laws portal), ADGM (Legislation portal), with secondary EU (EUR-Lex), France (Légifrance), and general access. Always quotes verbatim — never paraphrases article text. Pairs with recent-amendments-tracker because MENA databases lag the official gazette.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-statute-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Statute Lookup

Retrieve the current verbatim text of a statute, article, or regulation from its authoritative source. This skill quotes the text exactly as enacted — it never paraphrases. It also provides the citation, effective date, amendment history, and a link to the authoritative source so the reader can verify.

## When to use this

- A lawyer drafting a legal opinion needs to quote the exact statutory text
- A contract drafter needs to verify that a compliance clause correctly reflects the applicable law
- A court submission requires a verbatim statutory quotation with citation
- A compliance team is building a control framework anchored to specific statutory articles
- A researcher needs the original instrument before analyzing regulator guidance or case law that interprets it

**Do not use this** when you need regulator interpretation — that is [[research-regulator-guidance-lookup]]. Do not use this when you need recent changes — pair this with [[research-recent-amendments-tracker]].

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Statute or law name | The instrument to look up | Required — or provide subject area if name not known |
| Specific article(s) | Retrieves targeted text; avoid returning the entire law if only 1–2 articles are needed | Provide if known |
| Jurisdiction | Different jurisdictions have different sources | Required |
| Effective date / version date | For historical analysis or dispute about what law applied at a past date | Default: current consolidated version |
| Language preference | Many MENA instruments exist in Arabic only; English translation may be unofficial | Note Arabic-only instruments |

## Sources by jurisdiction

### Lebanon (LB)

**Official Gazette** (الجريدة الرسمية / Al-Jarida Al-Rasmiya):
- The sole authoritative source for enacted laws and decree-laws in Lebanon
- Published by the Ministry of Information; accessible via the official gazette portal (gazette.gov.lb) and the Lebanese Parliament's digital archive (lp.gov.lb)
- Available in Arabic and French (many foundational laws are in French from the Mandate period)

**Key Lebanese statutes frequently referenced**:
- Code of Obligations and Contracts (Code des Obligations et des Contrats, Decree-Law of 9 March 1932)
- Commercial Code (Code de commerce, Legislative Decree No. 304 of 24 December 1942)
- Labor Law (Legislative Decree No. 124 of 23 September 1946, as amended)
- Law No. 3 of 1956 — Banking Secrecy
- Code of Civil Procedure (Decree-Law No. 90 of 16 September 1983)
- Company Law (Law No. 126 of 19 May 2019 for offshore companies; SAL provisions in Code of Commerce)

**Access via**: [[connector-legal-data-hunter]] for consolidated Lebanese law texts.

### KSA (Saudi Arabia)

**Bureau of Experts at the Council of Ministers (BOE)**:
- The authoritative consolidated source for Royal Decrees and Council of Ministers decisions
- Maintained at bureau.gov.sa; Arabic language
- BOE consolidates amendments into the base text — the most reliable source for current law

**Official Gazette** (أم القرى / Umm Al-Qura):
- Primary promulgation vehicle; published weekly
- Hijri calendar dates — convert to Gregorian when citing

**Key KSA statutes frequently referenced**:
- Commercial Register Law (Royal Decree M/1 of 1423 AH / 2002 AD)
- Labor Law (Royal Decree M/51 of 1426 AH / 2005 AD, as amended)
- Companies Law (Royal Decree M/132 of 1443 AH / 2022 AD — new law replacing 2015 version)
- Capital Market Law (Royal Decree M/30 of 1424 AH)
- Anti-Money Laundering Law (Royal Decree M/20 of 1424 AH / 2003 AD)
- Real Estate Development Law (Royal Decree M/43 of 1442 AH)

**Access via**: [[connector-legal-data-hunter]] for KSA law; BOE portal for primary source.

### UAE Federal

**Ministry of Justice (MOJ) website** (moj.gov.ae):
- Consolidated UAE federal laws in Arabic; some in English
- Federal Decree-Laws, Federal Laws, Cabinet Resolutions

**UAE Federal Official Gazette** (الجريدة الرسمية الاتحادية):
- Authoritative; Arabic; published officially

**Key UAE federal statutes frequently referenced**:
- Federal Decree-Law No. 32 of 2021 — Commercial Companies Law (CCL)
- Federal Decree-Law No. 33 of 2021 — Regulation of Employment Relations in the Private Sector (Labor Law)
- Federal Decree-Law No. 34 of 2021 — Combating Rumours and Cybercrime
- Federal Decree-Law No. 45 of 2021 — Personal Data Protection Law (PDPL)
- Federal Law No. 5 of 1985 — Civil Transactions Law (Civil Code), as amended
- Federal Law No. 11 of 1992 — Civil Procedure Code, as amended by Federal Decree-Law No. 42 of 2022
- Cabinet Decision No. 1 of 2022 — Implementing Regulation of the Labor Law
- Cabinet Decision No. 58 of 2020 — Beneficial Ownership Procedures Regulation

### DIFC

**DIFC Laws portal** (difclaw.ae):
- The authoritative, version-controlled portal for all DIFC legislation
- Consolidated texts with amendment history visible; notes the "as at" date

**Key DIFC laws frequently referenced**:
- DIFC Law No. 3 of 2004 — Contract Law (as amended, incorporating 2017 and later amendments)
- DIFC Law No. 5 of 2005 — Companies Law (as amended)
- DIFC Law No. 2 of 2019 — Employment Law
- DIFC Law No. 1 of 2008 — Arbitration Law (as amended 2013)
- DIFC Law No. 4 of 2004 — Strata Title Law
- DFSA Rulebook modules (not technically "statutes" but have statutory effect): GEN, COB, PIB, AML, etc.

### ADGM

**ADGM Legislation portal** (legislation.adgm.com):
- Authoritative portal for ADGM Regulations and Rules
- Well-maintained and current; includes "table of amendments"

### EU

**EUR-Lex** (eur-lex.europa.eu):
- All EU Regulations (directly applicable), Directives, Decisions
- Search by CELEX number (e.g., 32016R0679 = GDPR), by keyword, or by OJ reference
- "Consolidated" versions incorporate amendments — verify the "consolidated on" date

**Key EU instruments frequently referenced in MENA practice**:
- GDPR — Regulation (EU) 2016/679
- AML Directive 6 — Directive (EU) 2021/1237
- MiFID II — Directive 2014/65/EU
- EU Sanctions Regulations (various programs)

### France (FR)

**Légifrance** (legifrance.gouv.fr):
- Authoritative source for all French laws and regulations
- Code civil, Code de commerce, Code du travail, etc.
- Use "version en vigueur au [date]" filter for historical versions
- Available via [[connector-legifrance]]

## Output structure

```
## [Statute Name]

**Jurisdiction**: [jurisdiction]
**Citation**: [full citation — decree/law number, date]
**Effective date**: [date law entered into force]
**Last amended**: [date; consolidated to [date] if consolidated version]
**Authoritative source**: [URL or reference to official portal]
**Language(s)**: [Arabic | French | English | Arabic + English]
**Status**: In force | Repealed | Superseded by [instrument name]

---

### Article [X] — [Article heading if available]

> [Verbatim text of the article, in original language]

**English translation** *(unofficial — original controls)*:
[Translation if the original is Arabic or French and no official English version exists]

**Notes**: [Any amendment to this article since enactment; version differences]

---
```

## The verbatim rule

**Never paraphrase article text.** A paraphrase, however careful, risks:
- Omitting a condition or exception that is legally material ("unless" clauses are frequently paraphrased out)
- Changing the meaning of a term of art (Arabic legal terms frequently have specific jurisprudential meanings that are lost in casual translation)
- Creating a misstatement that could mislead a client or court

If a verbatim quote is too long to reproduce in full, quote the specific sub-articles or paragraphs that are directly relevant, and note the omission.

## Caution on MENA database lag

MENA legal databases — including commercial and official portals — frequently lag the official gazette publication by days to weeks. For laws enacted or amended within the last 3 months:
1. Explicitly flag the lag risk in the output
2. Run [[research-recent-amendments-tracker]] to check whether a more recent version exists
3. Recommend the user obtain a certified extract from the official gazette for mission-critical reliance

**Hijri vs Gregorian dates**: KSA instruments use Hijri calendar in the official citation. Always specify both when citing a KSA instrument (e.g., "Royal Decree M/51 of 1426 AH (2005 AD)"). Ambiguity in the calendar can cause a party to reference a completely different instrument.

## Related skills

- [[research-recent-amendments-tracker]]
- [[research-regulation-lookup]]
- [[research-regulator-guidance-lookup]]
- [[research-case-law-search]]
- [[research-deep-research-orchestrator]]
