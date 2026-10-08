---
name: inst-ksa-moj-integration-sboghossian
title: Inst — KSA Ministry of Justice Integration
description: Use when a matter or query involves the Saudi Ministry of Justice (MOJ) digital services, the Najiz court portal, Saudi government document templates, or official legal information issued by Saudi judicial bodies. Covers court case lookup, e-filing workflows, notarization through the MOJ, government legal document standards, and lawyer registration verification under the Saudi MOJ and Justice Ministry-affiliated bodies. Relevant for practitioners working on KSA-seated matters or clients navigating the Saudi judicial system.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/inst/inst-ksa-moj-integration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: general
language: en
---

# Inst — KSA Ministry of Justice Integration

## Purpose

Saudi Arabia's Ministry of Justice (وزارة العدل) has built one of the Gulf's most comprehensive legal digitalization ecosystems, centered on the **Najiz** platform. This institutional skill bridges Louis to MOJ digital services: court case status lookups, e-filing guidance, official document templates, notarial services, and the MOJ's public-facing legal information programs.

---

## When to use this

- A user wants to check the status of a case before Saudi courts (commercial, personal status, labor, administrative)
- A practitioner needs to file documents electronically through Najiz or the e-court system
- A user requests an official Saudi legal document template (power of attorney, affidavit, notarized statement)
- A lawyer's registration or license status with the Saudi MOJ needs verification
- A user asks about Saudi court hierarchy, competence, or procedure
- A matter requires authentication/apostille of a Saudi document for use abroad

---

## Saudi MOJ digital ecosystem

### Najiz (ناجز)
The central court services platform operated by the MOJ:

| Service | Available via Najiz | Notes |
|---|---|---|
| Case status lookup | Yes | Civil, commercial, personal status, criminal (limited) |
| Document submission (e-filing) | Yes | Most courts; paper backup still available |
| Judgment text access | Partial | Published summaries; full text requires lawyer access |
| Enforcement requests | Yes | Execution of judgments through court |
| Appointment scheduling | Yes | Book court clerk / judge appointments |
| Power of attorney registration | Yes | Electronic PoA with Ministry notarization |

### Lawyer registration & verification
- Saudi lawyers must be registered with the MOJ under the Legal Profession Law (Royal Decree No. M/38 of 2001, as amended)
- Verification: by name or license number via MOJ portal
- Status: active / suspended / under investigation / revoked
- Foreign lawyers: cannot appear before Saudi courts without local sponsor unless DIFC / ADGM rules apply (separate jurisdiction)

### MOJ notarization services
- Physical notary offices (Katatat) across all regions
- E-notarization expanding via Absher platform integration
- Standard documents: powers of attorney, affidavits, authentication of commercial documents, wills (for non-Muslims, limited recognition)
- Fees: published on MOJ website; vary by document type and value

### Related bodies
| Body | Role | Relevance |
|---|---|---|
| Board of Grievances (Diwan al-Mazalem) | Administrative court system | Appeals of government decisions |
| Labor Courts | Employment disputes | Disputes under Saudi Labor Law |
| Commercial Courts | Commercial disputes | Replaced Board of Grievances for commercial since 2020 |
| Enforcement Court | Judgment execution | Civil enforcement proceedings |
| Personal Status Courts | Family, inheritance | Islamic personal status law |

---

## Integration workflow

### Case status lookup
1. Accept: case number + court identifier, or party name + NIN (National Identification Number)
2. Query Najiz API (or web scrape with appropriate rate limiting)
3. Return: case title, court, judge (if public), status (pending / decided / appealed), next hearing date
4. Flag: if case is in enforcement phase or has active travel ban associated

### E-filing guidance
1. Identify: court, case type, pleading type
2. Retrieve: Najiz submission checklist for that filing type
3. Generate: structured document with correct Arabic headings per MOJ template
4. Checklist: authentication requirements, fee payment (SADAD reference), document format (PDF/A)
5. Confirm: submission acknowledgment tracking number

### Document templates
MOJ publishes standard templates for:
- Wakala (power of attorney) — general and special
- Affidavits (Shihada) — for witnesses and parties
- Commercial agency agreements (form)
- Waiver letters (Ibra)
- Rental dispute declarations

Louis generates drafts using MOJ-standard Arabic headings; user must sign and notarize before official use.

---

## Key legal framework

| Instrument | Subject |
|---|---|
| Royal Decree No. M/38 of 2001 (as amended) | Legal Profession Law — lawyer licensing |
| Law of Civil Procedure (Royal Decree No. M/1 of 2021) | Courts of general jurisdiction procedure |
| Commercial Courts Law (Royal Decree No. M/93 of 2020) | Commercial disputes |
| Labor Law (Royal Decree No. M/51 of 2005, as amended) | Employment disputes — Labor Courts jurisdiction |
| Enforcement Law (Royal Decree No. M/53 of 2012) | Execution of judgments |
| Electronic Transactions Law (Royal Decree No. M/18 of 2007) | E-signatures, e-filing validity |

---

## Practical traps

- **Arabic-only filings**: Saudi courts require Arabic-language pleadings. Translated documents must be certified by a MOJ-licensed translator.
- **Najiz system availability**: scheduled maintenance windows (typically Friday nights KSA time) affect filing deadlines — build in buffer before deadline days.
- **Travel bans**: Saudi courts can impose travel bans on defendants — check before advising clients on travel.
- **Foreign judgment enforcement**: Saudi courts will enforce foreign judgments only through treaty (limited) or reciprocity — New York Convention applies for arbitral awards.
- **Islamic law overlay**: personal status matters, inheritance, and certain commercial disputes may be decided partly under Sharia principles even in "commercial" courts.

---

## Related skills

- [[inst-uae-moj-integration]]
- [[inst-om-moj-integration]]
- [[inst-gov-procurement-mode]]
- [[kb-ksa-commercial-law]]
- [[kb-ksa-labor-law]]
- [[kb-ksa-personal-status]]
