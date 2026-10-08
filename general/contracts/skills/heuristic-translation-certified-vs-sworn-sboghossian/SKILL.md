---
name: heuristic-translation-certified-vs-sworn-sboghossian
title: Certified vs Sworn Translation
description: Use whenever a user is preparing documents for court filing, government registration, cross-border authentication, or any official purpose in a MENA jurisdiction that requires translation from or into Arabic or another language. Defines the four levels of translation authority (machine, self-certified, certified, sworn), maps jurisdiction-specific requirements for LB/KSA/UAE/EU, identifies the end-use determination step, and flags the common error of commissioning the wrong translation authority level.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/heuristic/heuristic-translation-certified-vs-sworn
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Certified vs Sworn Translation

## When this applies

Surface this heuristic whenever a document is being:
- Filed with a court, tribunal, or arbitral body in a different language from the proceedings language.
- Submitted to a government authority (ministry, land registry, municipality, labor authority) in a language other than the authority's official working language.
- Used cross-border in a transaction where the receiving jurisdiction requires translation in a specific form.
- Authenticated through an apostille or consular legalization chain (translation often required alongside the notarized original).

Commissioning the wrong type of translation delays proceedings, causes rejection of filings, and in some cases requires the entire authentication chain to be restarted.

## The four levels of translation authority

### Level 1 — Machine translation

**What it is**: automated translation (Google Translate, DeepL, AI translation tools).

**Speed and cost**: immediate; near-zero cost.

**Legal status**: no legal validity. Not acceptable for any official purpose.

**Acceptable use**: internal review, comprehension of a document before instructing a translator, quick-reference during negotiations. Never for submission to any court, authority, or counterparty as a final legal document.

### Level 2 — Self-translation with signed declaration

**What it is**: the translator (who may be a bilingual individual, not a credentialed translator) certifies their own accuracy with a signed declaration.

**Legal status**: valid for some limited commercial and internal business purposes. **Not valid** for court filings, government submissions, or cross-border authentication.

**Acceptable use**: informal inter-party communication; preliminary due diligence summaries for internal use. Do not use for any document that will be filed, registered, or used in official proceedings.

### Level 3 — Certified translation

**What it is**: translation by a translator certified by a recognized translation body (national translation association, bar association, equivalent). The certification typically involves a stamp and a signed declaration of accuracy.

**Legal status**: valid for many government and commercial purposes; in some jurisdictions this is the required level for commercial transactions (not court filings).

**When sufficient**:
- Commercial contracts being translated for counterparty review (not for filing).
- Corporate documents for internal compliance purposes.
- Some government approvals (varies by authority and jurisdiction — verify).

**When not sufficient**: court filings, personal-status document submissions, cross-border authentication chains requiring sworn translation.

### Level 4 — Sworn translation

**What it is**: translation by a translator officially appointed or recognized by the court system, Ministry of Justice, or equivalent official body. The translator holds "sworn translator" or "official translator" status. The translation bears the translator's official stamp and sworn declaration.

**Legal status**: the highest translation authority level; required for formal legal proceedings and official submissions.

**Always required for**:
- Submissions to courts and tribunals.
- Personal-status documents (birth certificates, marriage certificates, divorce decrees) for official registration.
- Corporate documents for company registration or government licensing purposes.
- Documents in a cross-border authentication chain (apostille or consular legalization).
- Immigration and visa filings requiring translation.

## Jurisdiction-specific requirements

### Lebanon

- **Sworn translator**: appointed by the Ministry of Justice. Required for all court filings and for documents submitted to government ministries and official registries.
- **For cross-border use**: sworn translation + Ministry of Justice stamp + MFA legalization.
- **Certified translators**: exist for commercial purposes; not accepted for court filings.
- **Arabic as court language**: all court submissions must be in Arabic. Any foreign-language document requires sworn Arabic translation.

### KSA

- **Licensed translator**: appointed/licensed by the Ministry of Justice (MOJ). Required for all documents submitted to Saudi courts, ministries, and official bodies.
- **For international use**: translation by MOJ-licensed translator + MOJ authentication + MFA apostille (note: KSA is not an Apostille signatory — see [[heuristic-notarization-apostille-requirements]]).
- **Arabic as official language**: all official Saudi documents and submissions must be in Arabic.

### UAE (federal)

- **Federal and emirate-level sworn translators**: the UAE Ministry of Justice maintains a list of approved legal translators. Sworn translators hold a government-issued license.
- **Required for**: court submissions, MOHRE filings, land registry documents, corporate registration documents in non-Arabic, and documents submitted to most federal and emirate authorities.
- **For non-court business documents**: certified (non-sworn) translation may be accepted by some free zone authorities — verify with the specific authority.
- **Arabic as court language**: UAE courts operate in Arabic. English-language documents require certified Arabic translation; for court filings, sworn Arabic translation.
- **DIFC/ADGM exception**: proceedings in DIFC Courts and ADGM Courts are in English. Arabic translation is not required for documents filed in those courts.

### DIFC / ADGM

- **English as court language**: no Arabic translation required for DIFC or ADGM proceedings.
- **For enforcement of DIFC/ADGM judgments in UAE federal courts**: the judgment may need to be translated into Arabic by a UAE-licensed sworn translator for the enforcement proceeding.

### Egypt

- **Sworn translator**: licensed by the Ministry of Justice. Required for all court submissions and official government filings.
- **For international use**: certified translation by licensed translator + authentication by MFA.
- **Arabic as court language**: all filings must be in Arabic.

### EU (general)

- **Sworn or certified translator per member state**: each EU member state has its own system. In France, *traducteur assermenté* (sworn translator, court-appointed) is required for official submissions; in Germany, *beeidigte Übersetzung* (sworn translation) is required. Verify per member state.
- **EU regulation**: some EU documents circulating within the EU benefit from simplified translation requirements under EU regulations (e.g., multilingual standard forms for civil-status documents). This applies only within the EU.

## The end-use determination step

**Before commissioning any translation, identify the end use:**

1. **What is this translation for?** Court filing? Government registration? Counterparty review? Notarization chain?
2. **Which authority will receive it?** Which court? Which ministry? Which registrar?
3. **What level does that authority require?** Check the authority's published requirements or confirm with local counsel.
4. **Match the translation level to the end use.** Never over-specify (sworn translation for an informal document is expensive and unnecessary) but never under-specify (certified translation where sworn is required will cause rejection).

## Practical guidance

- **Budget and timeline**: sworn translation is slower and more expensive than certified translation. Factor this into transaction timelines. A sworn translation of a 50-page corporate document in a MENA jurisdiction typically takes 3–10 business days.
- **Keep originals and translations together**: when filing, always submit the original document and its translation together. Many authorities require the translator's certification to appear on the same physical document as the translation.
- **Translator selection**: use translators with experience in the specific legal domain (corporate, litigation, real estate). Legal register Arabic or French differs from general language; a general certified translator may produce a technically accurate but legally imprecise text.
- **AI-assisted translation as draft only**: AI translation (Level 1) may be used to prepare a draft for human sworn-translator review to reduce cost, but the sworn translator must review and certify; the AI draft alone does not satisfy any official purpose.

## Related skills

- [[heuristic-notarization-apostille-requirements]]
- [[heuristic-bilingual-ar-en-mirror-clauses]]
- [[heuristic-always-state-jurisdiction-first]]
- [[draft-power-of-attorney]]
