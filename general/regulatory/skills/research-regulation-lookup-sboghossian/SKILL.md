---
name: research-regulation-lookup-sboghossian
title: Regulation Lookup
description: 'Use when a user needs the authoritative text of a statute, regulation, executive order, cabinet decision, or ministerial circular — not a summary, but the actual instrument with citation, full text, effective date, and consolidation status. MENA-primary: covers KSA regulations (Bureau of Experts, CMA, SAMA, ZATCA), UAE federal and emirate-level instruments, DIFC Laws and DFSA Rulebook, ADGM Regulations, Lebanese commercial and banking laws, EU instruments by CELEX number, and US USC/CFR sections. Always pairs with regulator-guidance-lookup for interpretive context.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-regulation-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Regulation Lookup

Retrieve the authoritative text of a specific statute, regulation, executive order, cabinet decision, or ministerial circular. Returns the full instrument with proper citation, effective date, and consolidation status (whether amendments have been incorporated). Covers MENA primary jurisdictions and secondary markets.

## When to use this

- A lawyer needs to quote the actual article text for a legal opinion, brief, or advice letter
- A compliance officer needs the primary regulatory text to anchor a compliance program
- A drafter needs to verify that a contractual clause accurately reflects the relevant statute
- A due-diligence team needs to confirm what law was in force at a specific historical date
- A researcher needs the full legislative instrument, not just a summary

**Note**: This skill retrieves text. For *interpretation* — what the regulator says the text means in practice — pair with [[research-regulator-guidance-lookup]]. For *changes* — whether the text has recently been amended — pair with [[research-recent-amendments-tracker]].

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Instrument name or number | Most efficient search if known | Provide if known |
| Jurisdiction | Determines which database to search | Required |
| Subject area | Used to locate instruments by topic when name/number not known | Required if name unknown |
| Specific article(s) needed | Retrieve targeted articles, not the whole instrument | Provide if known |
| As-of date | Historical versions matter for disputes about past conduct | Default: current consolidated version |

## Source library by jurisdiction

### KSA (Saudi Arabia)

| Source | What it covers | Access |
|--------|---------------|--------|
| **Bureau of Experts (BOE)** at Council of Ministers | Consolidated texts of all Royal Decrees and Council of Ministers decisions — the authoritative consolidated source | bureau.gov.sa; Arabic |
| **Umm Al-Qura** (official gazette) | The primary publication vehicle for enacted laws; search by issue number + date | Arabic; Hijri dates |
| **SAMA website** | SAMA Banking Control Law, implementing regulations, circulars on banking/insurance | sama.gov.sa |
| **CMA website** | Capital Market Law, CMA Implementing Regulations, listing rules | cma.org.sa |
| **ZATCA website** | VAT implementing regulation, excise tax, customs | zatca.gov.sa |
| **MHRSD website** | Labor Law (Royal Decree M/51 of 2005, as amended); implementing regulations | mhrsd.gov.sa |

**KSA note**: The BOE maintains the most reliable consolidated texts. Regulations published in Umm Al-Qura should be cross-checked with BOE for amendments. The BOE site is in Arabic; key instruments are increasingly available in unofficial English translation.

### UAE Federal and Emirate-level

| Source | What it covers | Access |
|--------|---------------|--------|
| **UAE Federal Government portal** (moj.gov.ae) | Federal Decree-Laws, Federal Laws, Cabinet Resolutions — consolidated texts | Arabic; some English |
| **UAE Federal Gazette** | Authoritative publication vehicle; Arabic | Print + digital |
| **Dubai Economy and Tourism (DET)** | Dubai Executive Council Resolutions affecting commercial activity in Dubai | Arabic/English |
| **Abu Dhabi Executive Council** | Abu Dhabi-level resolutions and decisions | Arabic/English |
| **MOHRE** | Federal labor law instruments, ministerial decisions | mohre.gov.ae |
| **CBUAE** | Central Bank regulations, AML framework | cbuae.gov.ae |

**UAE key instruments** (frequently referenced):
- Federal Decree-Law No. 32 of 2021 — Commercial Companies Law (CCL)
- Federal Decree-Law No. 33 of 2021 — Labor Relations in the Private Sector
- Federal Decree-Law No. 45 of 2021 — Personal Data Protection
- Cabinet Decision No. 58 of 2020 — Beneficial Ownership Procedures

### DIFC

| Source | What it covers | Access |
|--------|---------------|--------|
| **DIFC Laws portal** (difclaw.ae) | All DIFC Laws, Regulations, and Rules — version-controlled and consolidated | English; free |
| **DFSA Rulebook** (dfsa.ae) | DFSA regulatory rules organized in Modules (GEN, PIB, COBS, AML, etc.) | English; module-by-module |

**DIFC key instruments**:
- DIFC Law No. 3 of 2004 — Contract Law (as amended)
- DIFC Law No. 5 of 2005 — Companies Law (as amended)
- DIFC Law No. 2 of 2019 — Employment Law
- DIFC Law No. 1 of 2008 — Arbitration Law (as amended)
- DFSA Rulebook, relevant Modules

### ADGM

| Source | What it covers | Access |
|--------|---------------|--------|
| **ADGM Legislation portal** (legislation.adgm.com) | All ADGM Regulations, Rules, Guidance | English; free |
| **FSRA Rulebook** | Financial services regulatory rules | English |

### Lebanon

| Source | What it covers | Access |
|--------|---------------|--------|
| **Al-Jarida Al-Rasmiya** | Official gazette; all enacted laws and decrees | Arabic/French; limited digital archive |
| **Lebanese Code of Obligations and Contracts (Code des Obligations et des Contrats)** | The foundational private law instrument (Decree-Law 1932); French-language text | French text well-preserved in legal databases |
| **Law No. 3 of 1956** | Banking Secrecy Law | Referenced extensively; short instrument |
| **BDL Circulars** | Banking regulation; frequently operative where statute is unclear | BDL website |

**Lebanon note**: many Lebanese laws date from the French Mandate period (pre-1943) or the early Republic era and have been amended inconsistently. The Commercial Code (Code de commerce) and Code of Civil Procedure are French-influenced. Always check the official gazette publication date and amendment history.

### EU

| Source | What it covers | Access |
|--------|---------------|--------|
| **EUR-Lex** (eur-lex.europa.eu) | All EU Regulations (directly applicable in member states), Directives (require national transposition), Decisions, Recommendations | Free; CELEX citation system |
| **CELEX numbering** | Unique identifier for EU instruments: e.g., CELEX 32016R0679 = GDPR | Use CELEX to retrieve exact instrument |

Search EUR-Lex by CELEX number for fastest retrieval. "Consolidated" versions on EUR-Lex incorporate amendments — check the "Languages, formats and link to Official Journal" tab to confirm consolidation currency.

### US

| Source | What it covers | Access |
|--------|---------------|--------|
| **USCODE.House.gov** | United States Code (USC) — codified federal statutes | Free; cite as [Title] U.S.C. § [Section] |
| **eCFR.gov** | Code of Federal Regulations (CFR) — federal regulations | Free; electronic CFR is the current consolidated text |
| **SEC.gov** | Securities Exchange Act, Dodd-Frank, Sarbanes-Oxley + implementing rules | Free |

## Output schema

```json
{
  "instrument": {
    "name": "Full formal name of the instrument",
    "citation": "Decree/Law/Article number + date",
    "jurisdiction": "string",
    "type": "statute | regulation | executive-decision | ministerial-circular | rulebook-module",
    "effectiveDate": "ISO date",
    "consolidationFlag": "consolidated-to [date] | original-version-only | not-available",
    "linkToAuthority": "URL to official source"
  },
  "articleText": [
    {
      "articleNumber": "string",
      "text": "verbatim text of the article (Arabic + English translation if official translation available)",
      "notes": "any amendment or interpretation notes"
    }
  ],
  "asOfDate": "ISO date of the version retrieved",
  "subsequentAmendments": "see [[research-recent-amendments-tracker]] for latest amendments",
  "interpretiveGuidance": "see [[research-regulator-guidance-lookup]] for regulator interpretation"
}
```

## Verbatim rule

**Always quote article text verbatim** — never paraphrase regulatory text. A paraphrase, however careful, risks omitting a condition or qualification that is legally material. If the text is in Arabic or French and an official English translation is not available, provide the original text plus a clearly labeled unofficial translation noting that the original controls.

## Caveats

- MENA databases frequently lag the official gazette by weeks or months for recent amendments. If the asOfDate on the retrieved text is more than 3 months old, run [[research-recent-amendments-tracker]] to check for updates.
- Many KSA regulations exist in Arabic only. Unofficial English translations circulate widely but may not accurately reflect recent amendments.
- Lebanon's online legal databases are fragmentary; for critical matters, request a certified extract from the official gazette or commercial register.
- US and EU sources are the most reliably current; verify eCFR consolidation date for very recent rulemakings.

## Related skills

- [[research-regulator-guidance-lookup]]
- [[research-recent-amendments-tracker]]
- [[research-statute-lookup]]
- [[research-deep-research-orchestrator]]
