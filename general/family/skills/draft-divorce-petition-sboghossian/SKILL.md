---
name: draft-divorce-petition-sboghossian
title: Divorce Petition
description: 'Use when drafting a divorce petition or dissolution application. Highly jurisdiction-sensitive: in MENA, the applicable court, grounds, and procedure are determined by the parties'' religion/confession and domicile — Lebanon''s 18 confessional courts, KSA Sharia courts (talaq/khula/faskh), UAE Sharia for Muslims and Federal Law 41/2022 civil regime for non-Muslims, and Egypt Family Courts. Also covers EU civil-law petitions (Brussels IIb, no-fault divorce) and flags critical cross-border recognition traps.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-divorce-petition
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: family
language: en
---

# Divorce Petition

## When to use this

Personal-status law is the most fragmented area of MENA law. The applicable legal system — which court has jurisdiction, which rules apply, and what grounds for divorce exist — is determined by a matrix of:

1. The **religion / confession** of the parties (in MENA, each recognized religious community applies its own law).
2. The **domicile and habitual residence** of the parties and any children.
3. The **type of marriage** (religious / civil / mixed).
4. The **nationality** of the parties.

Before drafting a single clause, **confirm the applicable legal system**. Drafting under the wrong system wastes the client's time and may file in the wrong court entirely.

**Always recommend local counsel for divorce proceedings.** This skill supports drafting and checklist work; it does not substitute for local family-law specialists in high-conflict matters.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Petitioner full name, nationality, religion/confession, and residence | Jurisdictional + applicable-law determination | — |
| Respondent full name, nationality, religion/confession, and last known residence | Service requirements; jurisdiction | — |
| Marriage details (date, place, type, witnesses, registration) | Determines dissolution route and court | — |
| Children (names, dates of birth, nationalities, current habitual residence) | Child-related orders follow child's habitual residence | — |
| Grounds for divorce sought | Jurisdiction-specific; see matrix below | — |
| Property and financial situation | Assets, debts, income of both parties | — |
| Desired relief (custody, support, property division) | Determines what the petition must plead | — |

## Jurisdiction and religious matrix

### Lebanon — 18 confessional courts

Lebanon has no civil personal-status law for Lebanese nationals. The applicable court is determined by the religion of the respondent (or petitioner, depending on the confession's rules):

| Community | Court system | Divorce type | Notes |
|-----------|-------------|--------------|-------|
| Sunni Muslim | Sunni Sharia Court (Dar al-Ifta) | Talaq, khula, faskh | Husband-initiated talaq; wife-initiated khula (with financial renunciation); judicial dissolution on specific grounds |
| Shia Muslim | Jaafari Sharia Court | Similar framework | Jaafari doctrinal nuances apply |
| Druze | Druze Personal Status Court | Special Druze law | Divorce is irrevocable under Druze law; reconciliation period rules differ |
| Maronite Catholic | Maronite Patriarchate Court | Annulment (not divorce) | Catholic canon law: no divorce; only declaration of nullity |
| Greek Orthodox | Greek Orthodox Patriarchate Court | Divorce recognized | Orthodox canon law permits divorce on limited grounds |
| Armenian / Syriac / etc. | Respective ecclesiastical courts | Varies by denomination | — |
| Civil (foreign civil marriage) | Lebanese civil courts (limited) | Applied by comity | Lebanese courts may decline to apply foreign law for LB nationals |

**Key traps:**
- Lebanese nationals who married abroad under civil law and return to Lebanon cannot obtain a civil divorce in Lebanese courts — they must use a foreign court or their confessional court.
- Mixed-confession marriages require determining which court has jurisdiction (typically the respondent's community court).
- A Lebanese Sunni wife seeking khula must typically return the mahr (dower) and any gifts received. Confirm financial implications before proceeding.
- Foreign divorce decrees affecting Lebanese nationals may not be automatically recognized by Lebanese courts; an exequatur (recognition) proceeding is often required.

### KSA — Sharia courts

All personal-status matters for Saudi nationals and Muslim residents are handled by the Sharia courts under the Family Court system.

**Types of divorce available:**

| Type | Who initiates | Mechanism | Financial consequence |
|------|--------------|-----------|----------------------|
| **Talaq** | Husband | Pronouncement in court; must be registered with Najiz | Wife retains mahr (unless negotiated); 3-month iddah waiting period |
| **Khula** | Wife (by agreement) | Wife returns mahr; husband releases divorce | Wife pays agreed consideration; no alimony after khula |
| **Faskh** (judicial divorce) | Wife (court-ordered) | Petition to court; grounds required | Based on harm, desertion, failure to maintain, imprisonment |

**Filing requirements:**
- Personal appearance at the Family Court (mahkama al-usra).
- National ID / Iqama for both parties.
- Marriage certificate (عقد الزواج) certified.
- Najiz platform now handles many personal-status registrations.

**Children:** hadanah (custody) and wilayah (guardianship) allocation follows classical Islamic jurisprudence as applied by courts; see [[draft-custody-agreement]] for detail.

### UAE

**For Muslims:** Sharia Personal Status Courts apply Federal Personal Status Law (and applicable Emirati school of Islamic law). Broadly similar to KSA framework.

**For non-Muslims:** Federal Law 41/2022 on Personal Status for Non-Muslim Foreigners introduced a civil personal-status regime in UAE courts (initially pioneered through Abu Dhabi's ADJD Civil Family Court established 2021). Key features:
- Divorce by mutual consent possible without stated grounds.
- Joint custody approach closer to civil-law models.
- Assets divided equally on divorce (unless parties agree otherwise).
- This regime applies to non-Muslim foreigners; some Emiratis may opt in under specific provisions.
- DIFC Wills and Probate Registry handles succession for non-Muslims; not divorce.

**Residency requirement:** at least one party must be a UAE resident for UAE courts to accept jurisdiction.

### Egypt — Family Courts

Law 10/2004 established specialized Family Courts with exclusive jurisdiction over personal-status matters.

**For Muslims:** personal-status governed by Islamic family law as codified in Egyptian Personal Status Law. Grounds: talaq (husband), khula (wife — Law 1/2000 introduced judicial khula without grounds), judicial divorce on specific grounds (Law 25/1929 as amended by Law 100/1985).

**For non-Muslims:** Christian confessional courts continue to apply (Coptic Orthodox, Catholic, etc.).

**Filing:** must file in family court in the governorate where either party resides.

### France / EU

- No-fault divorce widely available (Law of 26 May 2004, codified in Code Civil).
- **Divorce by mutual consent** (divorce par consentement mutuel): fastest route; requires a convention signed by both parties and attorneys, deposited with a notaire.
- **Divorce for breakdown** (divorce pour altération définitive du lien conjugal): one party files; 1-year separation required.
- **Divorce for fault** (divorce pour faute): requires serious and repeated grounds.
- **Brussels IIb** (Council Regulation 2019/1111, effective 1 August 2022) governs cross-border jurisdiction and recognition of divorce decrees within the EU. Habitual residence is the primary connecting factor.
- **Rome III Regulation**: allows parties to choose the applicable law for divorce (within limits).

## Petition structure

The following structure applies broadly; adapt to the specific court's prescribed form requirements.

1. **Court / tribunal identification** — full name, address, and jurisdiction of the court where filing.
2. **Parties** — Petitioner: full name, nationality, religion/confession, address, residency status. Respondent: same.
3. **Jurisdictional basis** — why this court has jurisdiction (Petitioner's habitual residence; domicile; place of marriage; children's residence; confession of parties).
4. **Marriage details** — date, place of marriage; type (religious / civil); marriage certificate reference; witnesses where relevant.
5. **Children** — name, date of birth, nationality, current residence. State the custody arrangement sought.
6. **Grounds for divorce** — cite the applicable statutory or canonical ground(s).
7. **Property situation** — joint assets and debts; property division sought.
8. **Custody and child support** — if children, state the arrangement sought. Cross-reference to full custody agreement if prepared separately.
9. **Spousal maintenance** — whether claimed; quantum; duration.
10. **Interim relief** — emergency orders sought pending final judgment: residence order, financial support, travel restriction (if risk of child removal).
11. **Final relief sought** — dissolution of marriage; custody order; property division; support orders.
12. **Annexed documents** — marriage certificate, ID documents, birth certificates of children, financial disclosure, prior court orders.
13. **Service on Respondent** — method and address; notarization requirements.

## Critical cross-border traps

1. **Jurisdiction shopping** — in multi-national families, multiple jurisdictions may have concurrent jurisdiction. The first-filed rule (Brussels IIb in EU; first-seized principle in MENA) generally applies. File strategically.

2. **Foreign divorce recognition** — a divorce decree from one country may not be automatically recognized in another. Lebanese nationals divorced abroad under civil law face recognition challenges in Lebanon. UAE divorce decrees require recognition proceedings in some foreign jurisdictions.

3. **Religious vs. civil divorce** — in some jurisdictions, a religious divorce (talaq) does not automatically constitute a civil divorce recognized by a foreign civil-law state. A Lebanese Sunni man who pronounces talaq before the Sharia court may need a separate civil recognition for countries that do not recognize talaq.

4. **Children and the Hague Convention** — the 1980 Hague Convention on the Civil Aspects of International Child Abduction applies between signatory states. MENA jurisdictions are largely non-signatories (KSA, UAE, LB are not parties). Risk of child removal to a non-signatory MENA jurisdiction must be flagged in cross-border families.

5. **Apostille and translation** — documents filed in a foreign jurisdiction must be apostilled (if the country is a Hague Convention signatory) or legalized (if not) and translated into the court language.

## Drafting standards

- **Tone**: petitions are formal court pleadings; they must be factual, measured, and avoid inflammatory characterizations.
- **Grounds specificity**: vague grounds ("irreconcilable differences" may be accepted in US no-fault proceedings but not in a Jaafari Sharia court). Research and cite the specific statutory or canonical ground.
- **Bilingual**: in MENA, the filing language is Arabic. English translation may be filed concurrently for the practitioner's working record but does not control.
- **Always recommend local counsel**: this skill provides structure and analysis; divorce proceedings require local personal-status specialists who know the relevant court's practices.

## Common mistakes

1. **Filing in the wrong court** — misidentifying which confessional court has jurisdiction in Lebanon.
2. **Wrong type of divorce procedure** — applying for talaq when the client needs a judicial faskh (which requires a court hearing and proof of grounds).
3. **No conflict-of-laws analysis** — multi-national parties need an analysis before filing; the habitual residence of children governs most international child custody orders.
4. **Failing to secure interim orders** — in international families, failure to get an emergency travel ban allows the other parent to remove children to a non-convention country before the case is decided.
5. **Mahr / dower not addressed** — in Islamic-law divorces, the wife's right to mahr (prompt and deferred portions) must be addressed in the petition and in any settlement.

## Related skills

- [[draft-custody-agreement]] — child custody arrangement following divorce
- [[draft-guardianship]] — appointment of guardian in cases involving minors or incapacitated persons
- [[draft-prenuptial-agreement]] — pre-marital agreement that may govern property division
- [[review-personal-status]] — review of existing orders for enforceability and cross-border recognition
- [[kb-personal-status-mena]] — reference pack on personal-status law across MENA jurisdictions
