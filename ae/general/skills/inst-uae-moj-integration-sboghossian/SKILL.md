---
name: inst-uae-moj-integration-sboghossian
title: Inst — UAE Ministry of Justice Integration
description: Use when a matter or query involves the UAE Ministry of Justice, emirate-level court systems (Dubai Courts, Abu Dhabi Judicial Department, Sharjah Courts), electronic filing portals, government legal document templates, or notarial services in the UAE. Covers both onshore UAE courts (civil law framework under Federal Decree-Law) and offshore financial center courts (DIFC Courts, ADGM Courts — common law). Relevant for practitioners working on UAE-seated matters, e-filing, court judgment enforcement, or document authentication.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/inst/inst-uae-moj-integration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: general
language: en
---

# Inst — UAE Ministry of Justice Integration

## Purpose

The UAE operates a dual court structure: **onshore UAE courts** applying UAE federal and emirate laws (civil law framework), and **offshore financial center courts** (DIFC Courts and ADGM Courts) applying English common law. This skill bridges Louis to both systems: federal MOJ services, emirate-level court portals, notarial services, and the electronic filing infrastructure across the UAE.

---

## When to use this

- A user has a matter before UAE courts — federal, emirate, DIFC, or ADGM
- A practitioner needs to file documents via UAE e-court systems
- A user requests UAE government legal document templates (PoA, court petitions, company resolutions)
- A foreign judgment needs to be enforced in the UAE
- A UAE document requires notarization or authentication for use abroad
- A user asks about court jurisdiction allocation in the UAE (which court hears what)

---

## UAE dual court structure

### Onshore UAE courts

| Court level | Jurisdiction | Electronic portal |
|---|---|---|
| Courts of First Instance | Original civil, commercial, personal status, criminal | Emirate-specific portals |
| Courts of Appeal | Appeals from Courts of First Instance | Emirate-specific portals |
| Federal Supreme Court | Final appeals; constitutional matters; disputes between emirates | Federal MOJ portal |

**Emirate-level portals:**
- **Dubai**: Smart Courts (Dubai Courts website + Dubai Courts app); integrated with UAE Pass
- **Abu Dhabi**: Abu Dhabi Judicial Department (ADJD) e-portal; integrated with UAE Pass + Tamm
- **Sharjah, Ras Al Khaimah, etc.**: MOJ national e-court portal covers non-Dubai/AD emirates

### Offshore financial center courts

| Court | Governing law | Jurisdiction |
|---|---|---|
| DIFC Courts | English common law | DIFC-seated matters; parties may opt in by agreement (Art. 5 DIFC Courts Law) |
| ADGM Courts | English common law | ADGM-seated matters; opt-in available |

DIFC and ADGM courts have a **small claims tribunal** track (DIFC SCT: claims up to USD 200,000 / employment up to AED 500,000) with simplified procedure.

---

## Electronic filing

### Dubai Smart Courts
- Full e-filing for civil, commercial, and family matters
- Document upload in PDF (Arabic-language documents required; bilingual acceptable)
- Fee payment: integrated with various UAE payment methods
- Case tracking: real-time status via Smart Courts app
- Hearing reminders: SMS/email notifications
- **Requirements**: UAE Pass authentication (residents); Power of Attorney for non-residents filing through lawyer

### Abu Dhabi (ADJD)
- ADJD Mahakim app + web portal
- Integrated with Tamm (Abu Dhabi government digital platform)
- Case filing, fee payment, judgment download
- Execution (enforcement) applications filed electronically

### Federal MOJ portal
- Covers non-Abu Dhabi / non-Dubai emirates
- Apostille applications (UAE joined Hague Apostille Convention 2021 — significant simplification)
- Legal aid applications (federal MOJ scheme)
- Notary appointment booking

---

## Notarial services in UAE

| Service | Provider | Platform |
|---|---|---|
| General notarization | Federal MOJ notary offices + emirate courts | Walk-in; some online booking |
| Real estate PoA | Dubai Land Department or Abu Dhabi courts | DLD portal (for Dubai real estate) |
| DIFC Wills Service | DIFC Courts | Online registration for non-Muslim wills; enforceable within UAE |
| ADGM Wills | ADGM Courts | Equivalent service for Abu Dhabi-based non-Muslims |
| Company resolutions | Emirate-level courts + company authority | Notarization requirements vary by company type |

**Apostille**: Since 2021 UAE joined the Hague Convention — apostilled documents from member states accepted without embassy legalization. UAE-issued documents can receive apostille from the federal MOJ.

---

## Legal framework reference

| Instrument | Subject |
|---|---|
| Federal Law No. 11 of 1992 (Civil Procedure Law) | Onshore UAE courts procedure |
| Federal Decree-Law No. 32 of 2021 (Commercial Companies Law) | Company governance |
| Federal Decree-Law No. 45 of 2021 (Personal Data Protection Law) | Data privacy |
| Federal Decree-Law No. 33 of 2021 (Labor Law) | Employment — Labour Court jurisdiction |
| DIFC Law No. 10 of 2004 (DIFC Courts Law, as amended) | DIFC Courts jurisdiction |
| Federal Law No. 6 of 2018 (Public Procurement) | Government contracting |
| UAE Arbitration Law (Federal Law No. 6 of 2018, amended 2019) | Arbitration — UNCITRAL based |

---

## Judgment enforcement

### UAE onshore judgments
- Apply to execution court (Mahakim al-Tanfidh) at emirate where defendant has assets
- Attach bank accounts, real estate, or salary (salary garnishment available in UAE)
- Foreign judgment enforcement: onshore courts enforce on reciprocity basis + treaty; process through Court of First Instance

### DIFC/ADGM judgments
- DIFC judgment → recognized within DIFC; enforcement onshore via DIFC-Dubai agreement (Protocol 2009) allows direct enforcement in Dubai Courts
- ADGM judgment → ADGM-Abu Dhabi enforcement protocol
- DIFC/ADGM judgments recognized in other common-law jurisdictions with fewer barriers than onshore UAE judgments

---

## Common mistakes

- **DIFC opt-in misuse**: parties cannot simply write "DIFC Courts" in a contract if neither party has DIFC nexus — jurisdiction requires DIFC connection or Article 5(A)(2) opt-in meeting requirements
- **Language**: onshore courts require Arabic pleadings; certified translation mandatory for exhibits in other languages
- **Notarial PoA for property**: DLD requires PoA notarized by Dubai Courts or attested by UAE Embassy abroad — not all notarizations accepted
- **Limitation periods**: UAE Civil Transactions Law sets 15-year general limitation; specific periods for commercial claims (10 years), labor claims (1 year)

---

## Related skills

- [[inst-ksa-moj-integration]]
- [[inst-om-moj-integration]]
- [[inst-notary-integration-mena]]
- [[inst-tawqi3i-esignature-bridge]]
- [[kb-uae-commercial-law]]
- [[kb-difc-contract-law]]
