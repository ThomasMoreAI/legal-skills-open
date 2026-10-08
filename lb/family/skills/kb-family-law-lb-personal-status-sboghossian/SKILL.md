---
name: kb-family-law-lb-personal-status-sboghossian
title: Knowledge Pack — Lebanon Personal Status Law
description: Use when a matter involves marriage, divorce, custody, inheritance, or personal status in Lebanon. Lebanon has no unified civil personal-status law for nationals — 18 confessional courts each apply their own rules. Covers the full confessional map, implications for practice (marriage contracts, wills, divorce petitions, custody disputes, cross-confession jurisdictional questions), the civil-marriage-abroad strategy, and the differing rules for Christian, Sunni/Shia/Alawite/Ismaili, and Druze communities. Triggers on Lebanon divorce, Lebanese will, confession jurisdiction, personal status LB, or Lebanese inheritance.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-family-law-lb-personal-status
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: lb
practice: family
language: en
---

# Knowledge Pack — Lebanon Personal Status Law

## The Unique Lebanese System

Lebanon has **no unified civil personal-status law for Lebanese nationals**. Instead, personal status matters (marriage, divorce, custody, inheritance, adoption, guardianship) are handled by **eighteen confessional courts**, each applying its own substantive rules derived from religious law.

This makes Lebanon's personal-status landscape among the most complex in the world: the applicable rules depend on the **religion/confession registered on the individual's civil record**, not on choice of the parties.

> **Critical starting point for every personal-status matter**: confirm the confession of each party before proceeding. Religion determines jurisdiction.

---

## Recognized Confessions with Personal-Status Courts

| # | Confession | Jurisdiction |
|---|---|---|
| 1 | Maronite Catholic | Maronite Archdiocese courts |
| 2 | Greek Orthodox | Antiochian Orthodox Patriarchate courts |
| 3 | Melkite Catholic (Greek Catholic) | Melkite Patriarchate courts |
| 4 | Armenian Orthodox | Armenian Apostolic courts |
| 5 | Armenian Catholic | Armenian Catholic courts |
| 6 | Syriac Orthodox | Syriac Orthodox courts |
| 7 | Syriac Catholic | Syriac Catholic courts |
| 8 | Roman Catholic | Latin Diocese courts |
| 9 | Chaldean | Chaldean Patriarchate courts |
| 10 | Assyrian | Assyrian Church of the East courts |
| 11 | Coptic Orthodox | Coptic Orthodox courts |
| 12 | Coptic Catholic | Coptic Catholic courts |
| 13 | Protestant (Evangelical) | Protestant community courts |
| 14 | Sunni Muslim | Sunni Sharia courts (Hanafi school) |
| 15 | Shia Muslim | Shia Jaafari courts (Jaafari school) |
| 16 | Alawite | Alawite courts |
| 17 | Ismaili | Ismaili courts |
| 18 | Druze | Druze Maarouf community courts |
| (Historic) | Jewish | Jewish Tribunal (minimal active presence) |

---

## Christian Communities — General Rules

### Marriage
- Ecclesiastical marriage solemnized in the applicable church.
- Requires: consent of both parties, publication of banns (for Catholics), absence of impediments, registration with the church and civil registry.
- Church marriage is the only valid form for Christians — civil marriage in Lebanon not available for nationals.

### Divorce
- **Roman Catholic and Maronite**: divorce is **not permitted** in canonical law; annulment (declaration of nullity) is the available remedy on specific canonical grounds (defect of consent, impediment not dispensed, etc.). This is a significant practical barrier.
- **Greek Orthodox**: divorce granted on broader grounds (adultery, abandonment, serious abuse, long absence, conversion, impotence, criminality).
- **Armenian, Syriac, Evangelical**: each community has its own grounds; generally more permissive than Catholic courts.
- **Protestant**: generally allow divorce on relatively broad grounds.

### Custody and Alimony
- Courts apply church rules to custody (mother preference for young children is common across Christian communities) and alimony.
- Alimony duration and amounts vary significantly by community.

### Inheritance
- Generally **more testamentary freedom** than Muslim rules — no Quranic fixed-share system.
- Testator may bequeath entire estate by will in most Christian communities.
- Succession rules in the Lebanese Civil Code also apply unless confessional rules override for specific community.
- Intestate succession rules vary — for Greek Orthodox and Maronite, civil code principles often apply supplementarily.

---

## Muslim Personal Status

### Sunni (Hanafi School — Sunni Sharia Courts)

**Marriage**:
- Islamic marriage contract (aqd al-zawaj); mahr (dower) required.
- Wali (guardian) required for bride.
- Two Muslim male witnesses.
- Registered with the Islamic court.

**Divorce**:
- **Talaq**: husband-initiated unilateral pronouncement; court registration required.
- **Khula**: wife initiates by returning mahr or agreed compensation; court-supervised.
- **Faskh**: judicial dissolution on grounds — harm, non-support, absence, impotence, disease.
- Three-pronouncement talaq: irrevocable; requires muhalil for remarriage.

**Custody (Hadana)**:
- Mother priority for young children.
- Sunni rules: boys transition to father at approximately **7–9 years**; girls at approximately **9–11 years** (subject to best-interest application by modern courts).
- Mother loses custody if she remarries a non-related man.

**Inheritance**: Quranic fixed shares (fara'id) apply in full.

### Shia (Jaafari School — Jaafari Courts)

- Similar framework to Sunni but with Jaafari-specific rules.
- **Custody**: mothers may retain custody longer under Jaafari rules compared to Hanafi.
- **Inheritance**: same fara'id system but specific Jaafari jurisprudence on shares.
- **Marriage**: temporary marriage (mut'a) is recognized in Jaafari fiqh — rarely registered officially in LB.
- **Divorce**: talaq and khula exist; procedural requirements aligned with Jaafari fiqh.

### Alawite and Ismaili

- Each community has its own personal-status court and applies its own variation of Islamic rules.
- Relatively few cases nationally; practitioners should seek specialist community guidance.

---

## Druze Personal Status

The Druze community in Lebanon operates under **distinct personal-status rules**:

| Issue | Druze Rule |
|---|---|
| Marriage | Monogamy is mandatory (unique among Muslim-origin communities in LB) |
| Divorce | Allowed, but discouraged; specific Druze community courts govern |
| Inheritance | **Significant testamentary freedom** — testator may freely bequeath by will (unique among MENA Muslim-heritage groups) |
| Fixed shares (fara'id) | **Not applied** — Druze courts do not apply Quranic fixed-share inheritance |

This means Druze individuals can, unlike Sunni/Shia Muslims, draft wills that freely allocate the entire estate.

---

## Inheritance Summary Across Communities

| Community | Testamentary Freedom | Fixed Shares Apply? |
|---|---|---|
| Catholics (Maronite, Melkite, Roman, Armenian, Syriac) | High | No |
| Orthodox (Greek, Armenian, Syriac, Coptic) | High | No |
| Protestant/Evangelical | High | No |
| Sunni Muslim | Limited — max 1/3 to non-heirs | Yes (full fara'id) |
| Shia Muslim | Limited — max 1/3 to non-heirs | Yes (Jaafari fara'id) |
| Alawite / Ismaili | Limited — max 1/3 to non-heirs | Yes |
| Druze | High (full testamentary freedom) | No |

---

## Mixed-Confession Marriages

**Intra-religious mixed marriages** (e.g., Maronite × Greek Orthodox):
- The parties must choose which confessional court has jurisdiction.
- Law 60/1936 (Decree on Communities) governs jurisdictional choice.
- Typically: jurisdiction determined by the groom's confession (for inheritance purposes); parties may petition courts on specific grounds.

**Inter-religious marriages** (e.g., Christian × Muslim):
- No Lebanese confessional court permits inter-religious marriage.
- Parties must **marry abroad** in a civil-marriage country (Cyprus, France, etc.).
- The civil marriage is **registered in the Lebanese civil registry** and recognized.
- **However**, inheritance for civilly-married Lebanese remains governed by each person's confession — civil marriage does not unify the inheritance regime.

---

## Civil Marriage Abroad Strategy

Lebanese nationals who wish to avoid confessional marriage and/or unified inheritance:
1. **Marry in Cyprus (Limassol or Nicosia)** or France — both permit civil marriages for non-residents with minimal formalities.
2. Register the foreign marriage certificate at the Lebanese Civil Status Directorate.
3. The marriage is recognized in Lebanon for civil purposes (joint property, contract signing, hospital access).
4. **Limitation**: inheritance **still governed by each spouse's confession** — only a comprehensive will strategy can override this.
5. Draft **wills in multiple jurisdictions** (LB + France + Cyprus, or wherever assets are located) to achieve desired estate distribution.

---

## Practical Drafting Rules

| Document | Key Consideration |
|---|---|
| Will (Lebanese national) | **Always confirm confession first.** Sunni/Shia: 1/3 cap on bequests to non-heirs; Christian/Druze: full testamentary freedom. Cross-reference with immovable property registered in LB (situs rules apply). |
| Pre-nuptial agreement | Not recognized as such in Lebanese confessional law; limited enforceability. For civilly-married parties: a French or Cypriot pre-nup may have effect where foreign law applies. |
| Divorce petition | Must be filed before the appropriate confessional court; confirm jurisdiction by parties' religion. Catholic annulment: requires canonical grounds; long process. |
| Custody arrangement | Court order from the relevant confessional court; enforcement via civil mechanisms. |
| Cross-border estates | Lebanese real estate: confession-based inheritance rules apply to movable and immovable assets registered in LB; foreign assets follow applicable foreign law. Coordinate wills per situs. |

---

## Unresolved Reform Debate

Lebanese civil society has long pushed for an **optional civil personal status law** for nationals who wish to opt out of the confessional system. This reform has never been enacted due to political opposition from religious communities. As of 2025, it remains aspirational — any matter involving Lebanese nationals still requires navigation of the confessional framework.

## Caveats & Currency

Confessional court decisions are not publicly reported in Lebanon — practice evolves through informal channels and court interpretations. Religious laws are interpreted differently by individual judges within each community. Cross-border recognition of Lebanese confessional-court divorces and custody orders varies significantly by foreign jurisdiction — UK courts recognize them with case-by-case analysis; French courts less consistently. Verify the current practice for any cross-border matter.

## Related Skills

- [[kb-family-law-ksa]]
- [[kb-family-law-uae-civil-personal-status]]
- [[kb-real-estate-lb]]
- [[kb-employment-law-lb]]
- [[draft-will]]
- [[draft-prenup]]
