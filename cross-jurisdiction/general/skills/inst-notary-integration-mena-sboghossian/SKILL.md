---
name: inst-notary-integration-mena-sboghossian
title: Inst — MENA Notary Integration
description: Use when a matter requires notarization, authentication, or apostille of a legal document across MENA jurisdictions (LB, KSA, UAE, EG). Covers Lebanese Notaires Publics, Saudi MOJ notary services, UAE federal and emirate-level notaries, Egyptian notarization offices, cross-border Tawqi3i e-notarization, and Hague Apostille procedures. Surfaces notary requirements for specific document types, helps practitioners identify the correct notarial authority, and generates pre-notarization checklists.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/inst/inst-notary-integration-mena
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Inst — MENA Notary Integration

## Purpose

Notarization is a critical formality across MENA civil-law jurisdictions — required for powers of attorney, real estate transfers, company incorporation, marriage contracts, wills, and many commercial agreements. This skill surfaces the correct notarial authority for each jurisdiction, explains the applicable requirements, generates pre-notarization document checklists, and connects to electronic notarization services where available (including Tawqi3i for Lebanese cross-border use).

---

## When to use this

- A document requires notarial certification before it can be used in a MENA court or registry
- A power of attorney drafted by Louis needs to be executed before a notary
- A real estate or commercial transaction requires notarized documents under local law
- A foreign document must be authenticated / apostilled for use in a MENA jurisdiction
- A Lebanese document must be legalized for use in KSA, UAE, or EG (or vice versa)
- User asks about Tawqi3i or e-notarization validity across jurisdictions

---

## Notary systems by jurisdiction

### Lebanon

**Civil law notariat** (Notaires Publics):
- Notaries are judicial officers appointed by the Ministry of Justice
- Organized by district (Beirut, Mount Lebanon, North, South, Bekaa)
- Mandatory for: real estate contracts, company articles (SA/SARL), marriage contracts (civil optional; family law typically confessional), wills
- Process: parties appear in person (or via PoA); notary authenticates identity; document signed in notary's presence; notary register entry
- Fees: regulated tariff; calculated on transaction value for real estate; fixed for other instruments
- **Tawqi3i** (توقيعي): Lebanese Ministry of Interior e-notarization platform for cross-border document authentication — see [[inst-tawqi3i-esignature-bridge]]
- Post-2019 crisis: many notary offices have reduced capacity; verify office hours and availability

### Saudi Arabia (KSA)

**MOJ Notary Public (كاتب العدل)**:
- Notaries are MOJ employees attached to courts
- Services: authenticated powers of attorney, affidavits, commercial document certification, company establishment documents
- E-notarization: expanding via **Absher** (individual) and **Maroof** (business) platforms
- Foreign documents: must be authenticated by Saudi Embassy in country of origin, then Ministry of Foreign Affairs in KSA (chain legalization), unless Apostille Convention applies
- Apostille: KSA is a party to the Hague Apostille Convention (joined 2012) — apostilled foreign documents accepted without further legalization

### UAE

**Federal MOJ Notary + Emirate-Level:**
- Federal notary offices exist in each emirate
- Additional notarial services: DIFC Wills Service (for non-Muslims; common-law wills), Abu Dhabi Judicial Department, Dubai Courts Notary
- E-notarization: **Bashr** (Abu Dhabi), Dubai Courts online notarial services
- Common uses: real estate PoA (mandatory for off-plan sales), company resolutions, wills (non-Muslims)
- Foreign documents: UAE is a party to the Apostille Convention (joined 2021) — significant simplification for document legalization

### Egypt

**Egyptian Notarization Offices (Shaher Aqari + Tawtheeq)**:
- Two parallel systems: **Tawtheeq** (general notarization — contracts, PoA, affidavits) and **Shaher Aqari** (real estate registration)
- Both under the Egyptian Real Estate Publicity Department and Ministry of Justice
- Fees: government-set tariff; land registration fees calculated on cadastral value
- E-services: expanding via Ministry of Justice digital portal; some document types available online
- Foreign documents: Egypt is not a full Apostille Convention member for all document types — check by document type; otherwise chain legalization via Egyptian Embassy

---

## Apostille and chain legalization

| Route | Applicable when | Process |
|---|---|---|
| Hague Apostille (direct) | Both countries are Apostille Convention members | Single-page apostille certificate from competent authority in issuing country; no further embassy step needed |
| Chain legalization | Non-Apostille-Convention country involved | (1) Notarize locally → (2) Ministry of Foreign Affairs in issuing country → (3) Embassy of destination country → (4) Ministry of Foreign Affairs in destination country |
| Tawqi3i (LB) | Lebanese document destined for cross-border use | Electronic authentication via Lebanese Ministry of Interior portal; recognized by participating countries |

**Convention membership (MENA):**
| Country | Apostille Convention member | Joined |
|---|---|---|
| KSA | Yes | 2012 |
| UAE | Yes | 2021 |
| LB | No | — |
| EG | No (selectively) | — |
| Bahrain | Yes | 2013 |
| Jordan | Yes | 2016 |

Lebanon and Egypt not being full members means chain legalization is still required for documents from/to those countries unless specific bilateral agreements apply.

---

## Pre-notarization checklist (generated per document type)

The skill generates a checklist based on: jurisdiction + document type + parties' nationalities.

Example for **KSA Power of Attorney** for a Lebanese grantor:
- [ ] Draft PoA in Arabic (bilingual Arabic/English acceptable; Arabic governs)
- [ ] Principal's passport (original + copy)
- [ ] Principal's Iqama or visitor visa (if in KSA) or equivalent
- [ ] Agent's passport or Saudi national ID
- [ ] Notary appointment booked via Absher or walk-in at Katatab office
- [ ] Document printed on A4, no corrections or white-out
- [ ] If signing outside KSA: authenticate at Saudi Embassy in Lebanon + Saudi MOFA after arrival

---

## Common mistakes

- **Unsigned drafts to notary**: notary cannot certify a document signed before the appointment — parties must sign in the notary's presence (or the notary notarizes a previously signed document as "certified copy", which is different)
- **Wrong notarial office**: real estate notarization in some jurisdictions must occur in the district where the property is located
- **Missing chain step**: skipping the Ministry of Foreign Affairs step in chain legalization invalidates the whole chain
- **Language mismatch**: some MENA countries require Arabic-language documents; bilingual versions must be internally consistent

---

## Related skills

- [[inst-tawqi3i-esignature-bridge]]
- [[inst-ksa-moj-integration]]
- [[inst-uae-moj-integration]]
- [[inst-lb-bar-association-integration]]
- [[draft-power-of-attorney]]
- [[draft-company-articles-mena]]
