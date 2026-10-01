---
name: conversation-intake-will-sboghossian
title: Intake — Will / Testament
description: Use when a user wants to draft a will or testament and Claude must gather the testator's personal details, asset picture, family structure, religious regime applicability, and jurisdictional exposure before producing a drafting strategy. Triggers on requests to prepare a last will and testament, estate plan, or succession instrument. Sensitive intake — handle with care. Covers Sharia forced-heirship rules (KSA, UAE, LB, EG), DIFC/ADGM Wills for non-Muslim UAE asset-holders, and civil-law forced-heirship (France, Lebanon).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-will
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: trusts-and-estates
language: en
---

# Intake — Will / Testament

## When this applies

Activate when a user wants to draft a will (last will and testament, wasiyya), set up an estate plan, or seek guidance on succession planning. This intake is uniquely sensitive: users are contemplating their own mortality or that of a close family member, often under emotional stress. Handle with care: be warm but efficient; do not belabor formalities unnecessarily; complete the intake in as few turns as possible.

This skill is also triggered by questions about DIFC/ADGM Wills, multi-jurisdiction estate planning, Sharia inheritance planning, and guardianship designations.

## Behavior

Multi-turn intake (two to three turns). Acknowledge the sensitive nature without making it awkward. Ask in a logical, human sequence (testator → family → assets → wishes → execution logistics). Flag the single most consequential jurisdictional issue immediately: if the testator is Muslim, Sharia mandatory share rules (fara'id) may significantly constrain testamentary freedom and must be flagged before any drafting begins.

## Required fields

### 1. Testator

- Full name (as it appears on passport/national ID — this is the name in the will header).
- Age and date of birth.
- Nationality.
- Jurisdiction(s) of residence (current domicile) and any additional jurisdictions where the testator spends significant time.
- Religion: Muslim / Christian / Jewish / other / not religious. This is material — Sharia mandatory inheritance rules apply automatically under UAE Federal Personal Status Law and KSA law to Muslim testators; a Muslim testator cannot freely distribute their estate by will in most MENA jurisdictions without Sharia compliance.
- Testamentary capacity: is the testator currently of sound mind? (You are not diagnosing — but if the user mentions cognitive decline, flag the need for capacity confirmation before witnessing the will.)

### 2. Family

List all immediate family members who may have legal inheritance rights:
- **Spouse(s)**: full name, nationality, marriage date, jurisdiction of marriage, current separation status. Multiple spouses under Islamic law: each has inheritance rights.
- **Children**: full names, ages, whether from current marriage or prior relationship. Minor children: note guardianship needs.
- **Parents**: alive? Jurisdiction of residence?
- **Siblings**: relevant if testator has no spouse or children.
- **Prior relationships**: any children from prior relationships who may have legitimate inheritance claims (Sharia or statutory)?

### 3. Assets

List assets by jurisdiction — each asset is governed by the law of the place where it is situated (lex situs for real estate; lex domicilii for movables in many systems):

| Asset type | Key information needed |
|---|---|
| Real estate | Address, title deed number, jurisdiction, estimated value, mortgage (if any), sole or co-ownership |
| UAE real estate | Also note whether in a free zone (DIFC: registrable in DIFC Wills Service; onshore: subject to UAE Personal Status Law) |
| Financial accounts | Bank name, jurisdiction, account type, approximate balance, sole or joint |
| Business interests | Company name, jurisdiction of incorporation, share percentage, any SHA provisions that restrict succession |
| Life insurance | Policy number, insurer, beneficiary designations (note: life insurance beneficiary designations may override the will) |
| Pension / retirement | Jurisdiction, scheme type, nomination of beneficiary form status |
| Digital assets | Cryptocurrency (confirm wallet access arrangements), digital IP, domain names |
| Jewelry, art, personal property | Estimated value, location |
| Debts | Mortgages, loans, personal guarantees (debts reduce the net estate; in Sharia, debts and funeral expenses are paid before any distribution) |

### 4. Wishes

What does the testator want to happen to their estate?
- **Specific bequests**: named items or amounts to named beneficiaries (e.g., "my apartment in Beirut to my daughter Sarah").
- **Residuary estate**: who receives the balance after specific bequests and debts are paid?
- **Conditional bequests**: "to [beneficiary] if they survive me by 30 days" — survival conditions reduce complexity in tandem deaths.
- **Charitable bequests / waqf**: in Islamic estates, voluntary bequests (wasiyya) to non-heirs or charities are capped at one-third of the estate after debts.
- **Trust**: does the testator want assets held in trust for minor children until a specified age?

### 5. Guardian for minor children

If the testator has minor children:
- Named guardian(s) for each child.
- Alternative guardian in case the primary guardian is unable or unwilling to act.
- In Islamic law jurisdictions (UAE, KSA): guardianship (wilaya) and custody (hadana) are legally distinct. The will appoints a financial guardian; physical custody follows court-determined rules under Islamic law (typically mothers for young children; reverts to father or paternal family later).
- DIFC/ADGM Wills: guardianship designations are legally binding for non-Muslims under UAE law (Wills and Probate Registry under Cabinet Resolution No. 16/2023 for non-Muslims).

### 6. Executor

- Named executor(s): individual(s) or professional trustee / fiduciary company.
- Substitute executor.
- Powers of the executor: standard powers (collect assets, pay debts, distribute estate) or enhanced powers (run a business, sell real estate, make investment decisions for a trust).

### 7. Sharia-applicable assets and forced-heirship

**This is the most consequential flag for MENA estates — always address it.**

**Muslim testators in Islamic law jurisdictions (UAE onshore, KSA, most of MENA)**:

- The mandatory Sharia inheritance rules (fara'id) allocate fixed fractional shares of the estate to specified heirs (spouse, children, parents, siblings) based on the school of Islamic jurisprudence applicable.
- **The testator may only freely dispose of up to one-third (1/3) of their net estate** by will to non-heirs or charities (the wasiyya). The remaining two-thirds must be distributed per fara'id.
- Major Sunni schools differ on edge cases (e.g., Hanafi vs Maliki vs Shafi'i vs Hanbali treatment of grandchildren when a child predeceases; orphaned grandchildren clause); KSA follows Hanbali; UAE onshore courts apply the majority school or testator's school.
- **Shia inheritance** (applicable to Shia Muslim testators in some jurisdictions): different fixed-share rules; consult specialist.
- **Practical implication**: if a Muslim testator in UAE wants to leave more than 1/3 to a non-heir (e.g., a business partner), this requires either (a) living arrangements (lifetime gift, structuring), not a will provision, or (b) DIFC/ADGM will if the assets are in those free zones.

**Civil-law forced heirship (France, Lebanon)**:

- French Civil Code (Code Civil): "réserve héréditaire" — forced share for children:
  - 1 child: 1/2 of estate.
  - 2 children: 2/3 of estate.
  - 3+ children: 3/4 of estate.
  - Spouse: the surviving spouse's forced-share rights (from 2001) apply alongside children's shares.
- Lebanese succession law: similar forced heirship based on the religious community's rules for personal status (Sunni, Shia, Druze, Christian, Jewish courts each apply different inheritance rules). Lebanon has no unified secular succession law.

### 8. DIFC/ADGM Wills for UAE non-Muslim asset-holders

**Critical for non-Muslim expatriates in the UAE**:

- **Problem**: under UAE Federal Personal Status Law, non-Muslim expatriates who die without a will recognized under UAE law may have their estates distributed under their home-country law OR under UAE Islamic law by default (courts apply lex domicilii, but in practice this has been inconsistent).
- **Solution**: the DIFC Wills and Probate Registry (now expanded to cover all UAE as "Non-Muslim Wills" under the UAE Non-Muslims Personal Status Law Federal Decree-Law No. 41/2022 and Cabinet Resolution No. 16/2023) allows non-Muslim expatriates to register a will governing their UAE assets, guaranteed to be enforced as written.
- The DIFC Wills Service provides a simple, standardized process; wills are registered confidentially and activated on death.
- **Who should use it**: any non-Muslim with significant UAE assets (real estate, bank accounts, company shares) who wants to ensure those assets pass to their chosen beneficiaries.
- **ADGM**: separate ADGM Wills and Probate Registry for ADGM-situated assets.

### 9. Single will vs multiple jurisdiction-specific wills

Recommend based on asset picture:

| Scenario | Recommendation |
|---|---|
| All assets in one jurisdiction | Single will governed by that jurisdiction's law |
| UAE assets + home-country assets (non-Muslim) | DIFC/ADGM Will for UAE assets + separate home-country will for other assets |
| Muslim with UAE + international assets | UAE will (Sharia-compliant) + separate legal advice for non-Sharia jurisdictions where different rules apply |
| France / Lebanon assets | Separate will under French / Lebanese law accounting for forced heirship; consider a legal reserve planning strategy |
| Multiple MENA countries | Jurisdiction-specific wills per country recommended (LB, KSA, UAE each apply lex situs to real estate) |
| Business interests in multiple jurisdictions | Consider restructuring to centralize equity in one holding company before drafting |

## Output

At the end of intake, produce:

1. A structured intake summary covering all nine fields and outstanding items.
2. A jurisdiction analysis: which rules govern which assets, and whether forced heirship or Sharia mandatory shares constrain testamentary freedom.
3. A recommendation: single will or multiple jurisdiction-specific wills (with brief rationale).
4. A routing instruction to [[draft-will]] with the completed intake data, specifying any DIFC/ADGM Will pathway if applicable.
5. A sensitive-handling note: if the session suggests urgency (terminal illness, imminent travel, recent family bereavement), prioritize the most critical assets first and offer to complete the rest in a subsequent session.

## Do not

- Ask about the testator's religion clinically or insensitively — frame as "which legal regime applies to your estate?" if the context calls for more distance.
- Draft a will distributing assets in a way that violates Sharia mandatory shares for a Muslim testator in an Islamic-law jurisdiction, without explicitly flagging that the provision will be unenforceable.
- Treat a DIFC Will as covering onshore UAE property automatically — confirm current scope of the Non-Muslims Personal Status Law and verify whether the specific property is covered.
- Give specific Sharia jurisprudence rulings — Islamic inheritance calculation is a specialist function; flag and recommend a specialized Islamic estate attorney or sharia judge consultation.

## Related skills

- [[draft-will]]
- [[kb-succession-law-mena]]
- [[kb-islamic-inheritance]]
- [[conversation-intake-power-of-attorney]]
- [[conversation-uncertainty-language]]
- [[conversation-refusal-policy]]
