---
name: conversation-intake-divorce-petition-sboghossian
title: Intake — Divorce Petition
description: Use before drafting a divorce petition or advising on family-law proceedings to gather 10 required inputs — jurisdiction, marriage details, children, assets, debts, support expectations, grounds, safety concerns, living arrangements, and available documentation. Handles the intake with appropriate sensitivity. Provides MENA-specific guidance on confessional court jurisdiction in Lebanon, religious personal status courts in UAE and KSA, and the treatment of civil marriages contracted abroad. Refuses to assist with asset-hiding strategies or fault prejudgment.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-divorce-petition
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: family
language: en
---

# Intake — Divorce Petition

## When to use this

Use this skill before producing any divorce-related document or detailed procedural advice. Divorce and family-law matters are among the most emotionally charged legal situations — apply [[conversation-empathy-b2c]] before launching into intake questions. Acknowledge the difficulty of the situation in one sentence, then proceed with the intake.

This skill covers:
- Divorce petitions (filing for divorce).
- Separation agreements (property division, custody).
- Advice on procedural options (which court, what grounds).
- Pre-divorce asset analysis.

## Sensitivity rules

This is a sensitive subject. Throughout the intake:
- Use neutral language. Say "your spouse" or "your partner," not "your husband" or "your wife," unless the user has specified.
- Do not assume the user wants the divorce — some users are researching their options, not committed to filing.
- If the user discloses abuse or safety concerns, prioritize safety resources before any legal procedure.
- Never suggest strategies that could harm the user's children or exploit a vulnerable spouse.

## The 10 required inputs

### 1. Jurisdiction

This is the most complex input in a family-law intake. Jurisdiction determines which court has authority and which substantive law governs.

Ask:
- Where do the parties currently live (and for how long)?
- Where did the marriage take place?
- What are the parties' nationalities?
- If there are children: where do the children live?

**Jurisdiction priority rules (general):**
- Most jurisdictions give their courts jurisdiction if the habitual residence of either party is there, or if the marriage was registered there.
- For MENA jurisdictions: nationality and religious affiliation often trump residence in determining which personal status court applies.
- Conflicts arise when parties live in different countries — this requires a conflict-of-laws analysis.

**Practical note for practitioners:** in MENA cross-border family matters (e.g., Lebanese nationals living in UAE), there is often a genuine choice between filing in the UAE (personal status court for UAE residents) or Lebanon (home jurisdiction). The practical consequences differ enormously and must be explained to the client.

### 2. Marriage details

- Date of marriage.
- Place of marriage (country and city).
- Type of marriage: **civil** vs **religious** (and which religious sect if applicable).
  - Lebanon: marriages are registered before one of 18 recognized religious communities; there is no civil marriage in Lebanon — Lebanese couples who want a civil marriage must marry abroad (most commonly in Cyprus) and have the marriage registered in Lebanon.
  - UAE: marriage may be a UAE-registered civil marriage (for non-Muslims) or a Muslim religious marriage before the Shari'a court; expatriates may also have a home-country marriage.
  - KSA: marriage is governed by Islamic Shari'a law through the civil court system.
  - France/UK: civil marriage is the norm; religious ceremonies are supplementary and have no legal effect.
- Has there been a prior divorce? If so, was it recognized in the current jurisdiction?

### 3. Children

- Ages and nationalities of any children.
- Current residence of children.
- Preliminary custody preference (sole / joint; primary residence with whom).
- Whether there is any existing custody or access arrangement.
- School location — this matters because courts are reluctant to order relocation that disrupts schooling.

**MENA-specific:** under most MENA Shari'a-based personal status laws, mothers have the right to custody (hadanah) of young children (ages vary by jurisdiction and school of jurisprudence), but fathers typically retain guardianship (wilaya). These concepts must be explained to clients unfamiliar with the framework.

### 4. Assets

Identify marital and individual assets:
- Real estate (location, ownership, mortgage status).
- Bank accounts (individual, joint, currency, country of bank).
- Business interests (shares, partnerships, sole proprietorships).
- Investment portfolios.
- Vehicles.
- Pension or retirement accounts.
- Foreign assets.

Note: **asset valuation** is not part of this intake — that requires a separate financial disclosure process. The intake records what assets exist and their approximate scale.

**Jurisdiction trap — community of property vs separate property:**
- France and most MENA civil-law jurisdictions: assets acquired during the marriage may be subject to community of property (communauté de biens) rules depending on the marriage contract.
- UAE: there is no community of property regime by default for non-Muslims; division is governed by the marriage contract and general principles.
- Lebanon: assets are separate unless a marriage contract establishes community.
- UK: equitable distribution — the court has broad discretion to divide assets irrespective of title.
- DIFC/ADGM: no family court; personal status matters go to UAE mainland courts.

Ask: **was a marriage contract (prenuptial / mahr / acte de mariage) signed?** If yes, what did it say about asset division?

### 5. Debts

- Joint debts (mortgages, car loans, credit cards with both names).
- Individual debts (loans in one spouse's name only).
- Business debts attributable to marital assets.

Division of debts follows similar rules to assets in most jurisdictions.

### 6. Spousal support / alimony expectations

- Does the user expect to pay or receive spousal support?
- What is each party's approximate income and assets?
- How long was the marriage?

**MENA-specific — mahr:**
Under Islamic personal status law, a wife is entitled to her deferred mahr (المهر المؤجل) upon divorce. Ask whether a mahr was agreed and, if so, the deferred amount. This is often significant — it is not negotiated down at the time of divorce but is a contractual debt.

### 7. Grounds for divorce

- **Fault-based jurisdictions:** some jurisdictions (including Lebanon for certain religious communities, and some US states) require proof of fault (adultery, abandonment, cruelty). Ask whether the user has or intends to assert fault-based grounds.
- **No-fault jurisdictions:** UAE, UK (since the Divorce, Dissolution and Separation Act 2020), France, most common-law jurisdictions — divorce is available without proving fault.
- **Khul' (women-initiated divorce in Islamic law):** in KSA, UAE, and Lebanon, a Muslim wife can seek a khul' divorce by returning the mahr; the husband's consent is not required in court proceedings if the court grants it.

**Important:** Do not prejudge which party is "at fault." The intake records the grounds the user wishes to assert, not a verdict.

### 8. History of abuse or safety concerns

This must be asked sensitively and in every intake, regardless of apparent circumstances:

> "For my records and to make sure we identify all the protections available to you — is there any history of physical, emotional, or financial abuse, or do you have any concerns about your safety or the safety of your children?"

If the answer is yes:
- Immediately provide safety resources (domestic violence helplines for the relevant jurisdiction).
- Note whether a protective order (restraining order / non-molestation order) should be sought before filing.
- Note **mandatory reporting obligations**: in some jurisdictions (including some US states), lawyers and AI-assisted platforms may have reporting obligations for disclosures of child abuse. Flag this if applicable and advise the user to consult a qualified lawyer.

**MENA context:** domestic abuse resources:
- UAE: Dubai Foundation for Women and Children (800-WOMEN / 800-96636); Abu Dhabi Social Support Authority.
- Lebanon: KAFA (enough violence & exploitation) — 01-392-220; Abaad.
- KSA: National Family Safety Program.

### 9. Current living arrangements

- Are the parties living together or separated?
- If separated: when did separation begin, and where is each party living?
- Are there concerns about one party leaving the marital home (or being forced out)?

This affects whether a home-occupancy order or non-molestation order should be sought urgently.

### 10. Documentation available

What documentation does the user have access to? Relevant documents:
- Marriage certificate (civil and/or religious).
- Marriage contract (prenuptial agreement, mahr agreement).
- Birth certificates of children.
- Bank statements and financial records.
- Property ownership documents.
- Existing court orders (from prior proceedings, if any).
- Communications documenting the breakdown (may or may not be relevant depending on jurisdiction and grounds).

If documents are not yet available, note this — gathering documents is typically an early step in the process and should be included in the next-steps advice.

## Output

After gathering the 10 inputs, produce:

1. **Intake summary** — a structured summary of the facts for lawyer review.
2. **Jurisdiction analysis** — recommended jurisdiction(s) and why; pros/cons if there is genuine choice.
3. **Grounds analysis** — available grounds in the recommended jurisdiction and the evidentiary requirements.
4. **Asset and mahr summary** — what is at stake financially.
5. **Immediate next steps** — ordered by urgency (safety first, then legal procedure).
6. **Safety resources** — always included regardless of whether abuse was disclosed.

## Hard limits

This skill will not:
- Suggest asset-hiding or asset-transfer strategies to defeat a spouse's financial claims.
- Prejudge which party is at fault before any court process.
- Advise a user to violate a custody or access order.
- Assist with child abduction or international relocation without the other parent's consent.
- Advise on how to evade child support obligations.

## MENA-specific jurisdiction notes

### Lebanon — confessional court system

Lebanon has **no unified civil personal status law**. Divorce and family law are governed by the laws of the relevant religious community:
- **Sunni Muslim:** Dar al-Ifta and Sunni Shari'a courts.
- **Shia Muslim:** Ja'fari Shari'a courts.
- **Maronite Christian:** Maronite ecclesiastical tribunal.
- **Greek Orthodox:** Greek Orthodox Patriarchal court.
- **Druze:** Druze community courts.
- And 14 other recognized communities.

The applicable religious court is determined by the parties' registered religious affiliation, not their practice. A couple of different religious sects faces a complex jurisdictional question — they may need to file in their respective community courts for separate matters (divorce vs property).

Lebanese couples who married in a **civil marriage abroad** (e.g., Cyprus) may file in Lebanon using the foreign civil marriage law as the governing law, or file abroad. This requires a choice-of-law analysis.

### UAE — expatriate family matters

UAE personal status courts handle:
- Muslim marriages: under Federal Law No. 28 of 2005 on Personal Status (Shari'a-based).
- Non-Muslim expatriates: may opt to apply the law of their country of nationality under a 2023 amendment, or apply UAE law.

Expatriates in the UAE should carefully evaluate whether to file in UAE or in their home jurisdiction. UAE judgments on asset division are generally enforceable within the UAE; enforcement abroad requires a separate procedure.

### KSA — Shari'a-governed family law

KSA applies Hanbali Shari'a principles to family law through the civil court system. Key points:
- Divorce (talaq) by the husband is unilateral and does not require a court filing, but must be registered.
- Khul' divorce by the wife requires court proceedings.
- Custody follows Hanbali hadanah rules; mothers typically have custody until ages 7 (boys) or 9 (girls), after which the father has priority under traditional rules (though courts have discretion).

## Related skills

- [[conversation-clarifying-questions]]
- [[conversation-empathy-b2c]]
- [[conversation-disclaimer]]
