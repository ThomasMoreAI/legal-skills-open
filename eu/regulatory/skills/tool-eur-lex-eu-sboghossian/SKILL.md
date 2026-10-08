---
name: tool-eur-lex-eu-sboghossian
title: Tool — EUR-Lex (EU Official Legal Database)
description: 'Use when looking up EU primary and secondary law — treaties, regulations, directives, decisions, CJEU case law — via EUR-Lex, the EU''s official legal database. Relevant for MENA transactions with EU regulatory exposure: GDPR, DSA/DMA, adequacy decisions, EU export controls (Reg 2021/821), and EU sanctions. Supports CELEX-number lookup and keyword search. Pair with legifrance-fr for French national implementation.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-eur-lex-eu
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# Tool — EUR-Lex (EU Official Legal Database)

## What it does

Queries EUR-Lex — the official European Union legal database — to retrieve the authoritative text of EU legal instruments: treaties, regulations, directives, decisions, CJEU and CFI judgments, legislative proposals, national implementing measures, and corrigenda.

EUR-Lex is the definitive source for EU law. It is the first tool to use whenever EU regulatory compliance, EU data-protection law, or EU export-control rules are implicated in a matter, regardless of where the matter is principally located.

## Setup / auth

- **Public access:** EUR-Lex is freely accessible at https://eur-lex.europa.eu
- **API:** EUR-Lex provides a public web services API (SPARQL endpoint and REST) for programmatic access; no API key required for basic queries
- **CELLAR:** The EU Publications Office's semantic repository underlying EUR-Lex; CELEX numbers are the stable identifiers

## Capabilities

### Search modes

| Mode | Input | Notes |
|---|---|---|
| CELEX number | `32016R0679` | Fastest; unique identifier per instrument (format: `YYYYY[NN]XXXX`) |
| Keyword search | Natural language | Full-text across all EUR-Lex documents |
| ELI (European Legislation Identifier) | URI format | Alternative stable identifier |
| Treaty article | `TFEU Art 101`, `TEU Art 50` | Direct article lookup |
| CJEU case number | `C-311/18` | Court of Justice case (Schrems II) |

### CELEX number format guide

| Prefix | Instrument type |
|---|---|
| `3` | Secondary legislation (regulations, directives, decisions) |
| `6` | CJEU and CFI case law |
| `1` | Treaties |

Examples:
- `32016R0679` — GDPR (Regulation 2016/679)
- `32022R0833` — Russia sanctions Reg 833/2014 (as amended)
- `32021R0821` — EU Dual-Use Export Control Regulation
- `62018CJ0311` — CJEU C-311/18 (Schrems II — Privacy Shield invalidation)

## EU law categories relevant to MENA matters

### Data protection — GDPR and EU AI Act

**When relevant in MENA transactions:**
- EU customer personal data processed by a MENA entity (extraterritorial reach of GDPR Art 3)
- EU subsidiary of MENA group processing data
- SaaS or cloud services offered to EU data subjects from MENA infrastructure
- Data transfers from EU to MENA: adequacy decision status, SCCs, Binding Corporate Rules

Key instruments:
- `32016R0679` — GDPR (General Data Protection Regulation)
- `32022R2065` — Digital Services Act (DSA)
- `32022R1925` — Digital Markets Act (DMA)
- `32024R1689` — EU AI Act (in force from 2024; full application 2026–2027)

Adequacy decisions for MENA: As of 2026, no MENA jurisdiction has an EU adequacy decision. Standard Contractual Clauses (SCCs) or Binding Corporate Rules are required for EU → MENA data transfers.

---

### Sanctions and export controls

**When relevant:**
- EU entity or EU-resident counterparty in a MENA transaction
- Goods with EU origin being exported to or via MENA
- Financial services involving EU banks or clearinghouses

Key instruments:
- `32014R0833` — Russia/Ukraine sectoral measures
- `32021R0821` — EU Dual-Use Export Control Regulation
- `32012R0267` — Iran nuclear sanctions

---

### Financial services (MiFID II, AML directives)

Relevant for DIFC/ADGM financial-services firms with EU clients or regulated activities:
- `32014L0065` — MiFID II (Markets in Financial Instruments Directive)
- `32015L0849` — 4AMLD (Anti-Money Laundering Directive)

---

### Competition law

For MENA businesses with EU market presence:
- `32004R0139` — EU Merger Regulation (EUMR) — notifiable transactions involving EU turnover thresholds
- TFEU Art 101 (anti-competitive agreements) and Art 102 (abuse of dominant position)

## Output schema

```json
{
  "celex": "32016R0679",
  "title": "Regulation (EU) 2016/679 of the European Parliament and of the Council (GDPR)",
  "type": "Regulation",
  "dateOfEffect": "2018-05-25",
  "ojReference": "OJ L 119, 4.5.2016, p. 1–88",
  "status": "In force",
  "consolidatedVersion": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679",
  "pdfUrl": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32016R0679",
  "nationalImplementation": [
    { "country": "FR", "instrument": "Loi Informatique et Libertés (amended 2018)" }
  ],
  "amendedBy": []
}
```

## Usage patterns

### Pattern 1 — GDPR compliance check for MENA company

A Lebanese SaaS company serves EU users. Retrieve GDPR (CELEX `32016R0679`) and:
- Check Art 3 to confirm territorial scope (likely applies)
- Check Art 44–49 for data transfer mechanisms
- Retrieve the adequacy decision list (no MENA country listed)
- Conclude: SCCs required; recommend [[research-data-privacy-gdpr]]

### Pattern 2 — Export control pre-check

A UAE company is exporting telecommunications equipment to Iran. Retrieve EU Dual-Use Regulation (CELEX `32021R0821`) to check product classification and licensing requirements before the transaction proceeds.

### Pattern 3 — CJEU precedent research

For a DIFC arbitration with EU-law arguments, retrieve relevant CJEU judgments by case number to support submissions on EU contract law or competition law issues.

## Limits

- EUR-Lex contains EU-level law only; national implementation must be checked via national databases (e.g., [[tool-legifrance-fr]] for France, legislation.gov.uk for UK post-Brexit).
- Post-Brexit, UK law is no longer in EUR-Lex; use legislation.gov.uk for UK statutory instruments.
- EUR-Lex does not include EEA (Norway, Iceland, Liechtenstein) national law; those countries implement EU directives separately.

## Pair with

- [[tool-legifrance-fr]] for France-specific implementation of EU directives
- [[tool-eu-sanctions]] for EU sanctions regime detail
- [[research-data-privacy-gdpr]] for full GDPR compliance analysis

## Related skills

- [[tool-eu-sanctions]]
- [[research-data-privacy-gdpr]]
- [[tool-courtlistener-us]]
- [[kb-eu-regulatory-law]]
