---
name: inst-om-moj-integration-sboghossian
title: Inst — Omani Ministry of Justice & Legal Affairs Integration
description: Use when a matter or query involves the Omani Ministry of Justice and Legal Affairs (MJLA), the Omani court system, e-justice portal services, Omani government document templates, or lawyer registration and regulation in the Sultanate of Oman. Covers Omani court hierarchy and jurisdiction, electronic filing through Taqneen/e-justice systems, notarial services, and the legal framework governing professional practice in Oman. Relevant for GCC practitioners working on Oman-seated matters or clients navigating Omani judicial institutions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/inst/inst-om-moj-integration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Inst — Omani Ministry of Justice & Legal Affairs Integration

## Purpose

Oman's **Ministry of Justice and Legal Affairs (MJLA)** (وزارة العدل والشؤون القانونية) oversees the Omani court system, notarial services, legal profession licensing, and the national e-justice infrastructure. This institutional skill bridges Louis to MJLA services: court case lookups, e-filing guidance, official document templates, notarial service routing, and the regulatory framework governing lawyers practicing in Oman.

---

## When to use this

- A user has a matter before Omani courts (commercial, civil, personal status, administrative, labor)
- A practitioner needs to file documents electronically through Oman's e-justice system
- A user requests an official Omani legal document template (power of attorney, notarized affidavit)
- A lawyer's registration with the Omani Bar Association (OBA) needs verification
- A foreign company needs to authenticate documents for use in Oman
- A matter involves enforcement of a foreign judgment in Oman

---

## Omani court hierarchy

| Court | Jurisdiction | Notes |
|---|---|---|
| Magistrate Courts (Mahakim al-Jaza') | Summary criminal offenses; minor civil (up to OMR 5,000) | First instance |
| Primary Courts (Mahakim al-Ibtidaiya) | Most civil, commercial, criminal first-instance | Main trial courts |
| Court of Appeal (Mahakim al-Isti'naf) | Appeals from Primary Courts | Muscat + Salalah |
| Supreme Court (al-Mahkama al-Uliya) | Final appeals; cassation | Legal questions of law |
| Administrative Court | Disputes against government entities | Under Council of State |
| Commercial Courts | Major commercial disputes (Muscat + other major cities) | Specialist panel |

---

## E-justice and digital services

Oman has invested in digitalizing its justice infrastructure through:

### Taqneen platform
- Official legal database: legislation, regulations, royal decrees
- Full text of laws in Arabic; some translated to English
- Updated regularly by MJLA

### E-justice portal (Manzooma al-Qada al-Electroni)
- Case status lookup by case number or party name
- Electronic submission of pleadings and documents (civil + commercial courts)
- Payment of court fees via integrated payment gateway
- Judgment text access (published decisions)
- Appointment scheduling with court registries

### Nafath integration
- Oman's national digital identity (equivalent to UAE's UAE Pass / KSA's Absher)
- Required for authenticated e-justice portal access
- Lawyers must link Nafath + OBA registration to file electronically

---

## Lawyer registration and regulation

- **Omani Bar Association (OBA)**: mandatory registration for all practicing lawyers in Oman
- Governing law: Law on the Legal Profession (Royal Decree No. 108/1996 and subsequent amendments)
- Requirements: Omani law degree or equivalent recognized qualification; Arabic language proficiency; good standing declaration
- Foreign lawyers: permitted to practice in association with a licensed Omani lawyer; cannot appear in court as principal advocate without specific authorization
- Verification: OBA member register (accessible via OBA website or MOJ portal)

---

## Notarial services

- Omani notaries operate under the MOJ
- Located at Primary Court buildings across governorates
- Standard notarized documents: powers of attorney, affidavits, company resolutions, real estate contracts (supplemental to land registration)
- E-notarization: limited; expansion underway as of 2024-2025
- Foreign documents for use in Oman: Oman is a party to the **Hague Apostille Convention** (joined 2012) — apostilled documents from member states accepted without further chain legalization

---

## Key legal instruments

| Instrument | Subject |
|---|---|
| Royal Decree No. 29/2002 (Civil and Commercial Procedure Law) | Court procedure — civil and commercial |
| Sultani Decree No. 55/2019 (Commercial Companies Law) | Company formation and governance |
| Royal Decree No. 35/2004 (Labor Law, as amended) | Employment — Labor Court jurisdiction |
| Royal Decree No. 47/1997 (Arbitration Law) | Commercial arbitration — based on UNCITRAL Model Law |
| Royal Decree No. 114/2008 (Electronic Transactions Law) | E-signatures and electronic documents |
| Royal Decree No. 108/1996 (Legal Profession Law) | Lawyer licensing and conduct |

---

## Practical considerations

- **Arabic-language requirement**: Omani courts require Arabic-language pleadings; bilingual documents acceptable with Arabic prevailing
- **GCC movement**: Omani lawyers can practice in other GCC states under GCC professionals mobility arrangements (subject to bilateral conditions)
- **Foreign judgment enforcement**: Oman enforces foreign judgments through the Primary Courts on reciprocity basis; New York Convention applies for foreign arbitral awards (Oman is a signatory since 1999)
- **PDL privacy**: Oman's Personal Data Protection Law (Royal Decree No. 6/2022) requires careful handling of personal data submitted through e-justice systems
- **Court fees**: calculated as percentage of claim value; exact rates on MOJ fee schedule; fees waived for legal aid matters

---

## Related skills

- [[inst-ksa-moj-integration]]
- [[inst-uae-moj-integration]]
- [[inst-notary-integration-mena]]
- [[kb-om-commercial-law]]
- [[kb-gcc-arbitration]]
