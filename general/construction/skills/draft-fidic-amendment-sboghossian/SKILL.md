---
name: draft-fidic-amendment-sboghossian
title: FIDIC Contract Amendment — Particular Conditions
description: Use when drafting FIDIC contract amendments (Particular Conditions) to override or supplement the General Conditions in the FIDIC Rainbow Suite (Red, Yellow, Silver, Pink, Green, Gold, Emerald — 2017 editions). Covers the four principal books, the key sub-clauses modified in MENA government and infrastructure projects, dispute resolution (DAAB → ICC/DIAC arbitration), limitation of liability, force majeure expansion, local-content requirements (KSA Vision 2030, UAE Emiratization), and language requirements for government contracts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-fidic-amendment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: construction
language: en
---

# FIDIC Contract Amendment — Particular Conditions

## When to use this

FIDIC (Fédération Internationale des Ingénieurs-Conseils) contracts are the dominant framework for major construction, infrastructure, and EPC projects in MENA and internationally. The **General Conditions (GC)** are the standard published terms; the **Particular Conditions (PC)** are the project-specific variations that employers and contractors negotiate.

Use this skill when:
- A project is being structured on a FIDIC basis and you need to draft the Particular Conditions Schedule.
- An existing FIDIC contract is being amended mid-project (Variation Order / Contract Amendment).
- You are reviewing a Particular Conditions draft and need to identify the deviations from the published standard and their commercial/legal implications.
- A government employer in MENA is procuring under FIDIC and needs to add local-content, language, and Sharia-compliant payment clauses.

**Reference the correct edition and book** before drafting — the 2017 editions introduced significant changes from 1999 editions, particularly on dispute resolution (DAAB replaces DAB) and time-bar requirements.

## FIDIC Rainbow Suite — which book applies

| Book | Colour | Contract structure | Typical use |
|------|--------|--------------------|-------------|
| **Conditions of Contract for Construction** | Red | Employer designs; Contractor builds | Traditional build contracts; infrastructure; civil works |
| **Conditions of Contract for Plant and Design-Build** | Yellow | Contractor designs and builds | Power plants; process plant; design-build |
| **Conditions of Contract for EPC/Turnkey Projects** | Silver | Contractor takes full design-build-handover risk | EPC power; petrochemical; major infrastructure |
| **Conditions of Contract for MDB Harmonised Construction** | Pink | Based on Red Book; adapted for multilateral development bank projects | World Bank / ADB / IDB-funded projects |
| **Short Form** | Green | Simple, lower-value projects | Works below ~USD 500K |
| **Design, Build and Operate** | Gold | DBO including operations phase | Utilities; PFI projects |
| **Emerald** | Emerald | FIDIC + Joint Ventures | Consortium/JV construction |

## Key Particular Conditions topics

### 1. Currency of payment and exchange-rate mechanism

MENA government projects frequently require payment in local currency (SAR, AED, EGP) even where the contract is denominated in USD. PC should address:
- Specification of contract currency/currencies.
- Exchange rate for conversion (Central Bank rate; date of invoice; date of payment).
- Risk allocation: who bears FX risk between invoice date and payment date.
- Multi-currency payment provisions for international contractor procurement costs.

> "Clause 14.1 [amended]: The Contract Price shall be denominated in [SAR/AED/USD] and all payments under this Contract shall be made in [SAR/AED]. Where the Contractor has incurred costs in a currency other than the payment currency, the conversion rate shall be the [SAMA/UAE Central Bank] official rate on the date of the relevant invoice."

### 2. Local language requirements

KSA and UAE government contracts:
- Arabic version of the contract is the controlling version; English is for reference only.
- All site documentation, safety signage, and technical submittals must be in Arabic (or bilingual).
- All official notices and Engineer's instructions must be in Arabic.

> "Sub-Clause 1.4 [amended]: The governing language of this Contract is Arabic. Notices, certificates, approvals, instructions, and other communications required or permitted under this Contract shall be given in Arabic. An English translation may be provided for convenience but the Arabic text shall prevail."

### 3. Dispute Avoidance and Adjudication Board (DAAB)

The 2017 FIDIC editions replaced the DAB (Dispute Adjudication Board) with the DAAB, which has a proactive dispute-avoidance function. Key amendments commonly made in MENA contracts:

- **DAAB size**: 1-member vs. 3-member (cost vs. expertise). 1-member boards common for projects below USD 50M.
- **DAAB selection mechanism**: if parties cannot agree, who appoints? FIDIC standard: FIDIC appointing authority. MENA: often replaced with DIAC, ICC, or local engineering body.
- **DAAB fees**: employer sometimes pushes for each party to bear its own share independently.
- **Time-bar for DAAB reference** (Sub-Clause 20.2.1): the 84-day time bar for referring a dispute to DAAB is one of the most litigated clauses. Consider whether to preserve it or extend.

> "Sub-Clause 21.1 [amended]: The Dispute Avoidance/Adjudication Board shall consist of [one / three] member(s) agreed by the parties within [28] days of the Commencement Date. If the parties cannot agree, the appointing authority shall be [DIAC / ICC / [local engineering body]] whose decision shall be final."

### 4. Arbitration clause

FIDIC standard: ICC arbitration (Sub-Clause 21.6). MENA modifications:

| Jurisdiction | Common seat | Common rules | Notes |
|---|---|---|---|
| UAE government | Dubai or Abu Dhabi | DIAC (Dubai International Arbitration Centre) | Common; DIAC 2022 rules |
| KSA government | Riyadh | SCCA (Saudi Center for Commercial Arbitration) | KSA Arbitration Law (Royal Decree M/34 2012) |
| Multi-national | Paris | ICC | Standard for international EPC |
| DIFC/ADGM | London or Dubai (DIAC/DIFC-LCIA) | LCIA; ICC | International disputes |
| Egypt | Cairo | CRCICA (Cairo Regional Centre) | Egypt projects |

> "Sub-Clause 21.6 [amended]: Any dispute not resolved by the DAAB shall be finally settled by arbitration under the Rules of the [DIAC / SCCA / ICC], with the seat of arbitration being [Dubai / Riyadh / Paris]. The number of arbitrators shall be [one / three]. The language of the arbitration shall be [Arabic / English / both]."

### 5. Claims procedure and time-bar

FIDIC 2017 Sub-Clause 20.2 has a 28-day time bar for initial notice of claim (Contractor) and 84 days for fully detailed claim. Failure to comply with the time bar can result in the claim being barred.

MENA employers often push to make the time bar a condition precedent to payment (already the FIDIC 2017 standard). Contractors push to soften this to a rebuttable presumption or give courts discretion.

Commonly amended provisions:
- Extension of 28-day initial-notice period to [42 / 60] days.
- Softening the consequence of missing the time bar from automatic bar to reduction in entitlement.
- Addition of an "extension for good cause" mechanism.

### 6. Retention

FIDIC standard: 5–10% retention, released in two tranches (practical completion + defects liability). MENA government projects often require:
- Retention bond alternative to cash retention (performance security + retention bond model).
- Deferred release schedule (50% at practical completion; 50% on defects certificate).
- Interest on delayed retention release.

> "Sub-Clause 14.3 [amended]: The Employer may retain [5]% of each Interim Payment Certificate up to a maximum of [5]% of the Contract Price ('Retention'). The Contractor may substitute cash Retention with an unconditional on-demand Retention Bond in the form of Schedule [X] at any time after [50%] of the Contract Price has been certified."

### 7. Performance security

FIDIC standard: on-demand performance bank guarantee for 10% of Contract Price. MENA modifications:
- Amount: often 5–10%; Saudi Aramco and major GCC clients push for 10%.
- Call mechanism: FIDIC standard is on-demand unconditional guarantee; courts in some MENA jurisdictions allow resistance to calls on fraud grounds.
- Duration: performance security should be extended if practical completion is delayed; include auto-extension obligation.

### 8. Limitation of liability

**FIDIC General Conditions do not limit the Contractor's aggregate liability** (unusual compared to most major commercial contracts). This is a standard modification:

> "Sub-Clause 1.15 [added]: The Contractor's aggregate liability to the Employer under or in connection with this Contract shall not exceed [150% / 200%] of the Contract Price [except for liability for death or personal injury, fraud, or wilful default]."

**Delay damages (liquidated damages):** FIDIC includes delay damages; the PC should specify the rate. A liquidated damages clause must be a genuine pre-estimate of loss to be enforceable in common-law jurisdictions; in civil-law jurisdictions (UAE, KSA, LB), courts may adjust penalty clauses that are disproportionate.

### 9. Local content and nationalization

**KSA — Vision 2030 / IKTVA (In-Kingdom Total Value Add):**
- ARAMCO contracts require specific IKTVA percentages.
- Ministry of Commerce / MISA contracts require minimum Saudi subcontracting ratios.
- Include IKTVA reporting obligations; compliance mechanism; consequences of shortfall.

**UAE — Emiratization:**
- Some infrastructure contracts require minimum UAE-national employment ratios.
- Include compliance reporting and attestation mechanism.

### 10. Force majeure expansion

FIDIC standard force majeure (now "Exceptional Events" in 2017 edition) lists: war, hostilities, civil disturbance, natural catastrophe. MENA additions:

> "Sub-Clause 18.1 [expanded definition]: Exceptional Events shall also include: (a) pandemics or epidemics declared by a recognised national or international health authority affecting the Site; (b) government-imposed economic sanctions or embargoes; (c) cyber attacks on the Parties' critical systems materially impacting performance; (d) sudden and material supply-chain disruptions caused by third-country export controls affecting key plant or materials; (e) port closures or maritime route disruptions materially affecting the supply of Materials."

Specify the notice period (28 days FIDIC standard) and the consequence: extension of time with no additional cost (events that affect time only) vs. extension of time + cost (events attributable to Employer or neutral events).

## Output format

Produce Particular Conditions as a numbered schedule referencing the amended Sub-Clause by number:

```
SCHEDULE [X] — PARTICULAR CONDITIONS

These Particular Conditions supplement, amend, or replace the provisions of the General Conditions of the
[FIDIC Conditions of Contract for [Book Name], [Year] Edition].

Sub-Clause [X.X] — [Title]
[Amended text or deletion instruction]

Rationale: [One to three sentences explaining the commercial/legal purpose of the amendment]
```

Include a tracked-changes version showing original GC text → PC amendment. Annotate each PC with the rationale (standard commercial modification / government requirement / local law requirement) to assist contract negotiation.

## Common mistakes

1. **Wrong book** — using Red Book for an EPC turnkey project (should be Silver); the risk allocation differs fundamentally.
2. **PC contradicts GC without priority clause** — include a "in case of conflict between PC and GC, PC prevails" clause (FIDIC includes this by default; confirm it is present).
3. **Time-bar not addressed** — the 28-day notice requirement in Sub-Clause 20.2 catches contractors off-guard; confirm the contractor's project management team knows the requirement.
4. **Unlimited liability** — FIDIC's default unlimited liability regime is impractical for large contracts; the PC cap is a standard market modification.
5. **DAAB not constituted** — many MENA projects proceed without constituting the DAAB; when a dispute arises, parties must first constitute the DAAB before going to arbitration under 2017 rules, causing delays.
6. **Liquidated damages set too high** — courts in UAE and KSA will reduce LDs they regard as penal; base the rate on a documented estimate of the employer's loss from delay.

## Related skills

- [[draft-construction-contract]] — full construction contract for simpler projects not using FIDIC
- [[draft-guarantee]] — performance security and retention bonds referenced in FIDIC PC
- [[review-construction-contract]] — reviewing an existing FIDIC contract for risk allocation
- [[kb-construction-mena]] — construction law reference pack for UAE, KSA, Qatar, and LB
