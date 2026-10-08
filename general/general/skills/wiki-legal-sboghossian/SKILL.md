---
name: wiki-legal-sboghossian
title: Legal Knowledge System — Overview
description: Use as the top-level entry point to the legal knowledge system — covering major practice areas, primary jurisdictions (MENA plus FR, UK, US, EU, OHADA, GCC), cross-cutting legal concepts, and navigation guidance for more specific legal skills. Reach for this skill when the user's legal question has not yet been routed to a specific practice-area or jurisdiction skill, or when a cross-cutting legal overview is needed before drilling down.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/wiki/wiki-legal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Knowledge System — Overview

## Scope

This is the master navigation pack for the legal knowledge system. It maps the major practice areas covered, the primary jurisdictions supported, and the cross-cutting concepts that span multiple areas. Use it to orient before reaching for a specific skill, or to identify which skill is most relevant for a given user query.

---

## Practice areas

### Transactional law

- **Corporate / M&A**: entity formation, share purchase agreements, mergers, due diligence, cross-border transactions. Key MENA note: foreign ownership restrictions (progressively liberalised in UAE/KSA), nominee structures, Gulf-specific corporate forms (LLC, PJSC, branch, rep office; DIFC/ADGM companies; KSA JSC/LLC).
- **Private equity and venture**: fund formation, SAFE/convertible note, term sheet negotiation, shareholder agreements. See [[wiki-fundraising]].
- **Real estate**: title, lease, mortgage, strata, development agreements. See [[wiki-real-estate]].
- **Banking and finance**: loan agreements, security, ISDA, Islamic finance (Murabaha, Ijara, Sukuk). MENA-specific: Sharia-compliance structuring is a distinct and significant practice area.
- **Project finance**: EPC, PPP, concession agreements, limited recourse financing. Active practice area in UAE/KSA infrastructure.

### Regulatory and compliance

- **Corporate governance**: board obligations, disclosure, related-party transactions. UAE Companies Law (2021), ADGM Companies Regulations, DIFC Companies Law, KSA Companies Law.
- **Data protection and privacy**: UAE PDPL, KSA PDPL, DIFC DPL 2020, ADGM DPR 2021, Egypt PDPL. See [[wiki-data]] for data infrastructure; the legal frameworks are cross-referenced in their respective skill packs.
- **AML/CFT**: FATF standards, UAE AML Law, KSA AML Law, DIFC/ADGM AML rules. See [[wiki-geopolitics]] for sanctions context.
- **Healthcare regulation**: MoH, DHA, DoH, SCFHS licensing. See [[wiki-health]].
- **Financial services**: DFSA (DIFC), FSRA (ADGM), SCA (UAE onshore), SAMA/CMA (KSA), Central Bank of Egypt.

### Employment and labour

- **Employment law**: UAE Federal Decree-Law No. 33/2021, DIFC Employment Law 2019, KSA Labour Law (Royal Decree M/51), Lebanese Labour Code, Egyptian Labour Law No. 12/2003.
- **Sponsorship/Kafala**: the traditional Gulf sponsorship system has been progressively reformed; UAE abolished the no-objection certificate requirement for job changes; KSA has also liberalised. Residency is still employer-linked for most workers. See [[wiki-hiring]] for practical implications.
- **End-of-service**: UAE Labour Law prescribes a gratuity calculation; KSA similarly. Practitioners must calculate correctly on termination.

### Dispute resolution

- **Arbitration**: DIAC (Dubai International Arbitration Centre), DIFC-LCIA (now merged with DIAC), ICC, ADCCAC, KSA Centre for Commercial Arbitration, CRCICA (Cairo). New York Convention recognition varies by jurisdiction.
- **Litigation**: UAE court system (federal + emirate civil courts), DIFC Courts (common law), ADGM Courts (common law), KSA commercial courts, Lebanese civil courts, Egyptian civil courts.
- **Enforcement**: enforcing foreign judgments and arbitral awards in MENA varies significantly; DIFC/ADGM awards enforce under New York Convention; UAE onshore enforcement of foreign judgments requires reciprocity or special treaty.

### Intellectual property

- UAE IP Law (Federal Law No. 38/2021 on copyright; Federal Decree-Law No. 44/2021 on trademarks); KSA Copyright Law, Trademark Law; DIFC IP regime.
- Patent registration in GCC: national filings plus the GCC Patent Office (Riyadh) for regional coverage.
- IP considerations for AI-generated content are actively evolving; no MENA jurisdiction has yet authoritatively addressed AI authorship.

---

## Jurisdiction reference

### UAE (onshore)

Civil law system based primarily on Egyptian civil law (which drew from French and Swiss models). Federal laws supplemented by emirate-specific legislation. Key sources: UAE Civil Code (Federal Law No. 5/1985), UAE Commercial Transactions Law, UAE Companies Law (Federal Decree-Law No. 32/2021).

### DIFC (Dubai International Financial Centre)

Common law system; DIFC Courts have common law jurisdiction. English law influences are primary. DIFC has its own company law, employment law, data protection law, and trust law. Judgments of the DIFC Courts enforce across the UAE via the DIFC-UAE Protocol.

### ADGM (Abu Dhabi Global Market)

Common law system; English law as the default common law source. Similar to DIFC but separate jurisdiction. ADGM Courts operate on common law principles. Increasingly used for fund formation and financial services.

### QFC (Qatar Financial Centre)

English law-based system; QFC Regulatory Authority. Separate from Qatar onshore (civil law). Less voluminous case law than DIFC/ADGM.

### KSA

Dual legal system: Sharia as the supreme law; positive legislation enacted by Royal Decree. Commercial matters governed by a growing body of Royal Decree legislation; Sharia courts have residual jurisdiction. Major reforms under Vision 2030 are modernising the court system and commercial law.

### Lebanon

Civil law system based on French/Egyptian civil law. Significant French mandate-era legislation still in force. The ongoing economic and political crisis has created significant legal uncertainty; currency provisions in contracts are particularly complex.

### Egypt

Civil law system. Egyptian Civil Code (Law No. 131/1948) is the model for several Arab civil codes. Active commercial court and arbitration system; CRCICA is well-regarded.

### GCC / OHADA references

GCC commercial framework: the GCC has collective institutions but most commercial law remains national. For sub-Saharan African matters: OHADA (Organisation pour l'Harmonisation en Afrique du Droit des Affaires) provides a unified commercial law framework for 17 West and Central African states.

---

## Cross-cutting concepts

### Civil law vs common law

Most MENA jurisdictions are civil law (code-based, inquisitorial courts, no binding precedent in the strict common-law sense). DIFC, ADGM, and QFC are common law enclaves. A practitioner moving between onshore UAE and DIFC work must be alert to this difference — precedent binds in DIFC Courts; it does not in the same way in UAE federal courts.

### Sharia compliance

Islamic law principles (particularly the prohibition on Riba — interest) affect banking, finance, insurance, and family law across all GCC jurisdictions and to varying degrees in Egypt, Lebanon, and OHADA states. Legal practitioners in MENA must understand the basics of Islamic finance structures even if they do not specialise in them.

### Language of contract

In many MENA jurisdictions, Arabic is the official language of legal proceedings, and contracts in foreign languages may require official translation. In UAE, a bilingual Arabic/English contract generally prevails in Arabic in case of conflict unless the parties explicitly agree otherwise. In DIFC/ADGM, English is the court language and English contracts are effective without translation.

### Notarisation and authentication

Civil law jurisdictions often require notarisation of certain documents (power of attorney, articles of association, property transfers). In UAE, Notary Public (Tawtheeq/Tawqi3i) authentication is required for many corporate and property documents. DIFC/ADGM have their own notarial equivalents. International documents may require apostille or embassy legalisation for use across borders.

---

## Navigation guide

| User query type | Recommended skill |
|---|---|
| Specific MENA legal topic | [[wiki-legal]] → identify practice area → use specific skill |
| Healthcare law | [[wiki-health]] |
| Real estate law (MENA) | [[wiki-real-estate]] |
| Startup fundraising | [[wiki-fundraising]] |
| Law firm finances | [[wiki-finance]] |
| Geopolitics / sanctions | [[wiki-geopolitics]] |
| Legal-tech market / competitive | [[wiki-legal-tech]] |

---

## Caveats & currency

This overview reflects the state of MENA law as of early 2026. The region's legal systems are undergoing rapid reform — KSA court modernisation, UAE Companies Law, data protection frameworks, and AI-in-legal regulation are all active areas of change. Verify specific statutory positions against current official sources before advising clients.

---

## Related skills

- [[wiki-haqq-product]]
- [[wiki-legal-tech]]
- [[wiki-health]]
- [[wiki-real-estate]]
- [[wiki-finance]]
- [[wiki-geopolitics]]
