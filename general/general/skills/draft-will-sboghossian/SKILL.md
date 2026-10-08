---
name: draft-will-sboghossian
title: Will / Testament
description: Use when drafting a will or testament for a client whose estate spans MENA jurisdictions. MENA personal-status law is heavily fragmented by religion and confession — the applicable rules for succession depend on whether the testator is Muslim (Sunni, Shia, Druze) or non-Muslim (Christian, civil), and on the jurisdiction of immovable property. Must identify the testator's religion and jurisdiction before proceeding. Flags the Sharia limitation on testamentary freedom (one-third rule), the DIFC Wills Service Centre for UAE-resident non-Muslims, and the mandatory multi-will requirement for immovables in multiple jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-will
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Will / Testament

Drafting a will in the MENA context requires more preliminary fact-finding than almost any other document type, because the applicable substantive law — including the fundamental question of whether the testator has freedom to deviate from statutory inheritance rules at all — depends on the testator's religion and confession, not merely their nationality or domicile. Getting the religion/civil-status question wrong produces a legally invalid or unenforceable will.

**Always flag the jurisdiction-religion interaction to the client before drafting. Always advise lawyer review before execution.**

## When to use this

- A UAE-resident expatriate (non-Muslim or Muslim) wants to ensure their estate is distributed according to their wishes
- A Lebanese national (any confession) wants to formalize succession arrangements
- A KSA national or resident Muslim wants to set up a valid testament within the Sharia framework
- Any individual with immovable property in multiple jurisdictions who needs coordinated wills
- Pre-planning for a client undergoing a significant transaction or life event (investment, marriage, new child)

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Testator: full name, ID/passport number | Legal identification; must match government records | Must provide |
| Religion / confession (or "civil") | Determines the applicable personal-status regime entirely | Must establish before proceeding |
| Marital status, surviving spouse, children | Affects mandatory heir shares (fara'id) and testamentary capacity | Must provide |
| Jurisdiction of habitual residence | Determines which courts have jurisdiction | Must provide |
| Jurisdiction of each immovable property | Immovables are governed by the law of the property's location (lex situs) | Must identify all real property and its location |
| Beneficiaries with intended shares | What the testator wants | Must provide; subject to applicable law constraints |
| Executor (and alternates) | Person/entity responsible for administering the estate | Must provide; alternates are essential |

## Optional inputs

- Specific bequests (jewelry, vehicles, art, digital assets)
- Guardianship appointment for minor children
- Funeral and burial instructions (advisory, not legally binding in most systems)
- Trust structures (where applicable — more common in common-law jurisdictions)

## Religion / Confession Determines Applicable Law

This is the foundational question. Do not proceed without confirming the answer with the client.

### Lebanon — 18 official confessions

Lebanon has 18 officially recognized religious communities, each with its own personal-status court and succession rules:

**Sunni and Shia Muslims:**
- Sunni: Islamic inheritance rules per the Personal Status Law for Sunni Muslims
- Shia: Shia personal status law (Ja'fari courts); similar framework with some differences in specific heir shares
- Testamentary freedom limited to **one-third (1/3)** of the estate for non-heir beneficiaries
- Bequests to heirs (persons already entitled to a Quranic share) are valid only with the consent of all other heirs

**Druze:**
- Governed by Druze personal-status rules; inheritance framework distinct from Sunni/Shia
- Testament must comply with Druze community rules

**Maronite / Greek Orthodox / Roman Catholic / Armenian / other Christian confessions:**
- Each denomination has its own ecclesiastical personal-status court (Maronite, Greek Orthodox, Greek Catholic, Syriac, Armenian, etc.)
- Generally broader testamentary freedom than Islamic rules; testator can distribute the estate freely (subject to any mandatory shares for forced heirs under applicable ecclesiastical code)
- Specific rules vary by denomination; ascertain which court has jurisdiction

**Civil residents with no recognized religious status:**
- Lebanese law currently has no codified civil personal-status regime for Lebanese nationals
- Many who have left the confessional system opt for civil marriages abroad (typically France or Cyprus) and inherit through the applicable foreign civil law mechanism
- This is a legally complex area; specialist Lebanese civil law counsel is essential

### KSA — Sharia applies to all Muslims

Saudi Arabia applies Sharia law (Sunni Hanbali school) to all succession matters for Muslims:
- Fixed shares (fara'id) for Quranic heirs (spouse, children, parents, siblings — in specific proportions)
- **Testamentary freedom limited to 1/3** of the estate; the remaining 2/3 are distributed by fara'id rules
- Bequests to existing heirs: invalid without consent of all other heirs (a bequest cannot be used to give an heir more than their Quranic share)
- Non-Muslims in KSA: foreign nationals may have succession governed by their home country's law; complex and requires specialist advice

### UAE — Dual regime since 2022

**Federal Law 41/2022 on Personal Status for Non-Muslims in the UAE:**
- Non-Muslim UAE residents can now opt into a civil personal-status regime that mirrors international civil law standards
- This includes civil-law inheritance with full testamentary freedom (no fara'id)
- Wills under this regime can be registered with the Abu Dhabi Judicial Department (ADJD) for Abu Dhabi residents or the DIFC Wills Service Centre for Dubai/Northern Emirates residents

**DIFC Wills Service Centre:**
- Non-Muslim expatriates in the UAE can register an English-law-style will with the DIFC Wills Service Centre
- DIFC wills can cover UAE-based assets (bank accounts, real estate in Dubai and other Emirates, company shares)
- The DIFC Probate Registry administers the estate on death; DIFC courts enforce the will
- Available to individuals of any nationality; not limited to UAE residents (though resident or UAE-based assets are the primary use case)
- Registration requires: testator's passport, UAE visa, a will document prepared by a DIFC-approved will draftsman

**Muslims in UAE:**
- Default to Sharia for succession unless specific non-Muslim Civil Personal Status Law applies (only for non-Muslims)
- UAE non-Muslims who are Muslim by background but do not practice or do not wish to be governed by Sharia should confirm their legal position under UAE law carefully

### Egypt
- Muslims: Sharia-based succession; fara'id apply; 1/3 testamentary rule
- Non-Muslims (Coptic Christian, other): Coptic Personal Status Law for Coptic Christians; other communities have their own laws
- Foreign nationals: nationality law may apply for movables; Egyptian law for immovables located in Egypt

## Sharia Inheritance Fundamentals (For Muslim Testators)

If the testator is Muslim in any MENA jurisdiction, the following principles apply:

**Fara'id (fixed shares):**
The Quran mandates fixed inheritance shares for specific relatives (called Quranic heirs or asab). These cannot be altered by will. Common shares include:
- Surviving spouse: 1/8 (with children) or 1/4 (without children) — wife's share; 1/4 (with children) or 1/2 (without children) — husband's share
- Daughters: 1/2 (only daughter) or 2/3 (multiple daughters) if no sons
- Sons: residual after daughters' share (principle of 'asaba / residue)
- Parents: specific shares depending on surviving children

Note: The specific shares vary between Sunni schools (Hanbali, Hanafi, Maliki, Shafi'i) and Shia schools; the applicable school depends on the testator's tradition.

**The 1/3 rule (wasiyya):**
A Muslim testator may leave up to 1/3 of their estate by will to persons who are not entitled to a Quranic share (non-heirs, charities, specific bequests). The remaining 2/3 is distributed by fara'id rules.

**Bequests to heirs:**
A bequest cannot be made to a person who is already an heir (entitled to a Quranic share) unless all other heirs consent after the testator's death. This cannot be pre-agreed in the will.

**Trusts and foundations:**
Islamic law does not have a concept of a trust in the common-law sense. Islamic finance equivalent is the waqf (endowment); a waqf can provide for ongoing distributions from income while preserving the asset. Waqfs are administered under specific rules (often by religious authorities) and are not a simple substitute for a trust.

For further detail, see [[kb-shariah-finance-aaoifi]] and [[heuristic-shariah-compliance-check-when-relevant]].

## Civil Law / Non-Muslim Framework

Broader testamentary freedom applies. The standard will:
- Identifies the testator and revokes prior wills
- Appoints an executor (and alternates)
- Makes specific bequests (named items to named people)
- Residuary clause: all remaining assets go to [named residuary beneficiaries] in [stated proportions]
- Guardianship clause (if minor children exist)
- Witness or notarial execution as required

## Form Requirements by Jurisdiction

| Jurisdiction | Muslim | Non-Muslim |
|---|---|---|
| Lebanon | Handwritten (olographe) + date + signature; or witnessed will (2 witnesses); or notarial | Same forms available; specific ecclesiastical form if required by denomination |
| UAE — DIFC | N/A (only for non-Muslims) | Registered with DIFC Wills Service Centre; must comply with DIFC Wills and Probate Registry Rules |
| UAE — onshore (Federal Law 41/2022) | Fara'id applies; wasiyya of up to 1/3 by notarized will | Abu Dhabi Judicial Department registration available |
| KSA | Notarized via Notary Public; compliant with Hanbali Sharia requirements | Foreign nationals: complex; specialist advice required |
| Egypt | Notarized; must comply with Hanafi rules (for Sunni Muslims) | Coptic and other communities: follow respective personal-status law |
| UK | Testamentary freedom; 2 witnesses present at signature | Same |
| France | Olographe (entirely handwritten + dated + signed) or notarial | Same |

## Document Structure (Standard Civil-Law / Non-Muslim Will)

1. **Identification of testator** — full name; national ID / passport number; address; religion ("I declare that I am of [denomination] and this will is made under [applicable personal-status law / civil law]")
2. **Revocation clause** — "I revoke all prior wills and testamentary dispositions made by me"
3. **Appointment of executor** — primary executor (full name, relationship, contact); alternate executor (in case primary is unable or unwilling to act); grant of authority to executor
4. **Guardianship of minor children** (if applicable) — appoint guardian with alternates; confirm consent of guardian where available
5. **Specific bequests** — itemized list of specific assets (real property by land registry description; bank accounts by account number; vehicles by registration; jewelry with description) to named beneficiaries; contingency: if beneficiary predeceases, the bequest falls into the residue or passes to an alternate beneficiary
6. **Residuary clause** — all remaining assets pass to [named beneficiaries] in [stated proportions, e.g., 50/50, or all to spouse]; contingency: if no residuary beneficiary survives, pass to [alternates / charity]
7. **Funeral / burial instructions** — advisory only in most jurisdictions (not legally binding); may express religious / cultural preferences
8. **Witness / notarization block** — signed in the presence of [two] disinterested witnesses who also sign; or before a notary; or both as required by the applicable jurisdiction

## Standard Sections for Muslim Will (Wasiyya)

1. Identification of testator + declaration of Islamic faith
2. Revocation of prior wills
3. Declaration that fara'id will apply to the estate as determined by [Sunni Hanbali / applicable school] rules
4. Wasiyya bequests (up to 1/3 of estate): specific bequests to non-heirs (charities, named persons who are not Quranic heirs)
5. Appointment of executor to carry out the wasiyya and to assist in distributing the remainder per fara'id
6. Funeral / burial wishes (according to Islamic practice)
7. Witness / notarization block (as required by applicable jurisdiction)

## Critical Flags

### Always escalate for lawyer review
This is a high-stakes document — errors are discovered only when the testator has died and cannot be corrected. Even where the AI has drafted a clean will, the client should have it reviewed by a qualified estate lawyer before execution. See [[router-escalation]].

### Multi-jurisdiction immovables require multiple coordinated wills
A testator with real estate in Lebanon, UAE, and France needs three separate wills — one for each jurisdiction governing the real property there (lex situs principle). The wills must be coordinated to:
- Not revoke each other (use jurisdiction-specific revocation: "I revoke all prior wills made in Lebanon" rather than "I revoke all prior wills")
- Be consistent about the residuary estate
- Avoid double-counting assets in more than one will's residuary clause

### Digital assets
Most wills drafted in 2024 do not address digital assets (crypto wallets, digital accounts, online businesses, NFTs). If the testator has material digital assets, address them specifically:
- Where are the private keys / access credentials held?
- How should they be valued?
- To whom do they pass?

### Beneficiary predeceasing the testator
Always include contingency clauses: if a named beneficiary dies before the testator, what happens to that share? Options: (a) pass to the beneficiary's descendants (per stirpes); (b) pass to other named beneficiaries; (c) pass to the residue. Without a contingency, the bequest lapses and may create intestacy for that portion.

## Related skills

- [[safety-medical-tax-financial-out-of-scope]]
- [[kb-family-law-lb-personal-status]]
- [[kb-shariah-finance-aaoifi]]
- [[router-escalation]]
