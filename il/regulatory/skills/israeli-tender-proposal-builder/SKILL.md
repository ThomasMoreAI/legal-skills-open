---
name: israeli-tender-proposal-builder
title: Israeli Tender Proposal Builder
description: Builds a complete Hebrew proposal package for Israeli government and public sector tenders (michrazim). Parses the tender document, extracts threshold conditions, produces a compliance checklist, and drafts every proposal section per Chok Chovat HaMichrazim 5752-1992 and Takanot 5753-1993 (declarations, past experience table, pricing worksheet). Use when responding to an open tender (michraz pumbi), closed (sagur), framework (misgeret), or a local authority tender, and when researching historical procurement contracts via BudgetKey or IL Budget MCP to benchmark pricing. Prevents disqualification on technical defects. Do NOT use for Israeli Land Authority (RMI) land allocation tenders (use israeli-land-tenders), for filing a petition to the tenders committee, or for private commercial RFPs not subject to the Mandatory Tenders Law.
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-tender-proposal-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: regulatory
language: en
---

# Israeli Tender Proposal Builder

## Problem

Responding to an Israeli government tender is a high stakes, highly formal process. A single missing declaration, an arithmetic error in the pricing worksheet, or a threshold condition you failed to notice in the small print will get your offer disqualified on technical grounds (פסילה על פגמים טכניים) without the tender committee ever looking at the substance. Most businesses bid blind, without any view into what the state paid for similar work in past contracts, so they either price too high and lose, or price too low and bleed on execution.

## Instructions

### Step 1: Identify the Legal Framework

Before drafting anything, confirm which statute governs the tender and what kind of tender it is. The rules change based on the answer.

| Question | Why it matters |
|----------|----------------|
| Is the issuer a public body covered by the Mandatory Tenders Law? | The law applies to public bodies, government ministries, statutory corporations, government companies, and health funds. Local authorities follow the parallel municipal tender regulations. Private companies are not bound by this law. |
| Is it an open tender (מכרז פומבי), closed (מכרז סגור), framework (מכרז מסגרת), or a case of exemption (פטור ממכרז)? | The regulations define roughly 30 cases where a full public tender is not required. Know which track you are on. |
| What year are the regulations? | The operative text is Takanot Chovat HaMichrazim, 5753-1993, as amended. Always read the tender document itself for any special conditions that override the defaults. |

If the issuer is Rashut Mekarkei Yisrael (RMI) and the subject is a land allocation, stop and route to the `israeli-land-tenders` skill instead. This skill is for supply, services, works, and framework tenders.

### Step 2: Parse the Tender Document and Extract Threshold Conditions

The single most important section of any tender document is the threshold conditions (תנאי סף). If your offer does not prove compliance with every single one, it will be rejected before the price envelope is even opened. Takana 6 splits threshold conditions into two buckets.

**Bucket A: Statutory conditions (Takana 6(a)) - mandatory in every tender.**

| Condition (Hebrew) | What to attach |
|--------------------|----------------|
| רישום במרשמים הנדרשים על פי דין | Registration certificate from every registry required for the contract subject (corporate registry, professional license registry, etc.), plus proof that licenses are valid and current |
| עמידה בתקן ישראלי רשמי | Proof of compliance with any official Israeli standard that applies to the goods or service |
| אישורים ותצהירים לפי חוק עסקאות גופים ציבוריים | Proper bookkeeping certificate from the tax authority (אישור ניהול ספרים) and a declaration under the Public Bodies Transactions Law regarding fair employment practices |
| תצהיר שמירת זכויות עובדים (למכרזי כוח אדם) | For labor intensive contracts, a written declaration by the bidder and related parties regarding the bidder's compliance with workers' rights obligations |

**Bucket B: Discretionary conditions (Takana 6(b)) - set by the issuing body.**

These vary by tender and typically include:
- Minimum past experience (one equivalent contract, or several partial contracts totaling a threshold volume)
- Minimum annual turnover or cash flow over a defined period
- Specific certifications (ISO, security clearance, niche licenses)
- Minimum headcount or team composition

For every discretionary condition, extract the exact wording from the tender document into your checklist. Do not paraphrase. Do not assume the condition means what similar tenders meant last year.

### Step 3: Build the Compliance Checklist

Produce a single table with every threshold condition, the evidence document you will attach, where you will obtain it, and its status. Present it to the user for review before drafting anything else.

| # | Condition (verbatim from tender) | Statutory or Discretionary | Evidence to attach | Source | Status |
|---|----------------------------------|-----------------------------|---------------------|--------|--------|
| 1 | ... | 6(a) / 6(b) | ... | ... | Ready / Needs work / Blocker |

Rule of thumb: if any row is a Blocker, stop and flag it. Do not continue drafting a proposal for a tender you cannot qualify for. The user needs to know now, not after three days of work.

### Step 4: Draft the Proposal Sections in Hebrew

Work section by section. Match the order and numbering required by the tender document (mismatched section numbering is a common reason for disqualification). A typical Israeli tender response has these sections:

1. **מכתב נלווה (Cover letter)** - Bidder details, tender reference number, statement of intent to bid, list of enclosed documents.
2. **פרופיל החברה (Company profile)** - Legal name, HP/Teudat Zehut number, registered address, year established, ownership structure, core activities. Keep it tight and tender relevant.
3. **טבלת ניסיון קודם (Past experience table)** - One row per relevant past contract: client, subject matter, scope in NIS, period, contact person for reference. Only include contracts that genuinely match the discretionary experience condition. Padding with irrelevant entries is a red flag for the committee.
4. **מענה מקצועי (Professional response)** - Your technical approach: methodology, team, work plan, milestones, risks and mitigations. Map each requirement in the tender's professional chapter to a specific paragraph in your response.
5. **הצעה כספית (Price offer)** - In a separate sealed envelope (מעטפה נפרדת) if the tender is two envelope. Price structure must exactly match the template the tender provides. Never add line items, never remove line items.
6. **הצהרות ותצהירים (Declarations and affidavits)** - The block of mandatory declarations (see Step 5).
7. **נספחים (Appendices)** - Licenses, certificates, proof of insurance, bank guarantee, and any other attachment required by the tender.

Draft each section in natural, direct Israeli Hebrew. Avoid the over formal government register. The committee reads dozens of proposals and prefers clarity over pomp.

### Step 5: Assemble the Mandatory Declarations Block

Every Israeli public tender requires a standardized set of declarations. Missing any one of them is a disqualification event. Prepare these as separate documents.

A תצהיר (sworn affidavit) is not just a signed statement. It must be **sworn before a lawyer** (or another authorized person), the lawyer must warn the declarant of the criminal liability for a false declaration and confirm the declarant understood it, and the lawyer's verification block must be completed and signed. The תצהיר must also be **dated on or before the submission deadline**, never after. A declaration that is merely signed by the bidder without the lawyer's sworn-before-me verification, or that is undated or dated after submission, is defective.

| Declaration | Hebrew | Legal basis | When required |
|-------------|--------|-------------|---------------|
| Proper bookkeeping and no debts to tax authority | אישור ניהול ספרים וניכוי מס במקור | חוק עסקאות גופים ציבוריים | Every tender |
| Fair employment and minimum wage compliance | תצהיר לפי חוק עסקאות גופים ציבוריים (שכר מינימום והעסקת עובדים זרים כדין) | חוק עסקאות גופים ציבוריים | Every tender |
| Workers' rights compliance | תצהיר בדבר קיום חובות המציע בעניין שמירת זכויות עובדים | תקנה 6(א)(4) | Labor intensive contracts |
| No conflict of interest | תצהיר העדר ניגוד עניינים | Tender document | Usually required |
| Bribery and fraud disclosure | תצהיר היעדר הרשעות | Tender document | Usually required |
| Corporate authorization to sign | אישור עורך דין / רו\"ח על זכויות חתימה | Tender document | Every corporate bidder |

For each declaration, confirm:
- The text matches the template in the tender document exactly (do not redraft).
- Every signatory listed in the template has signed.
- The lawyer or accountant verification is attached if required.
- The declaration is dated within the validity window the tender specifies.

### Step 6: Handle the Bid Guarantee and Israeli-Product Preference

Two recurring elements decide tenders before the substance is even read: the bid guarantee, and the Israeli-product price preference.

**Bid guarantee (ערבות מכרז).**

Most public tenders require the bidder to attach a bid guarantee with the offer, as proof of seriousness. Get every one of these right, because each is a known disqualification trap:

- **Amount**: the tender states an exact guarantee amount (a fixed NIS sum, or a percentage of the offer). Submit that exact amount. A guarantee for less than the required amount is disqualified, and an unexplained guarantee for more can also draw scrutiny.
- **Type**: the tender almost always demands an **autonomous bank guarantee** (ערבות בנקאית אוטונומית), meaning the issuing body can call it on demand without the bank asking questions or the bidder being able to block payment. A personal guarantee, an insurance-company guarantee, or a conditional guarantee does not satisfy an autonomous-guarantee requirement.
- **Validity period**: the guarantee must be valid through at least the date the tender specifies (often the submission deadline plus 90 days, sometimes extendable on the committee's request). A guarantee that expires too early is disqualified.
- **Exact wording**: the tender usually annexes a guarantee template. The bank must issue the guarantee in that wording. Israeli case law is strict here. A deviation in the guarantee text, the wrong beneficiary, the wrong tender number, or a missing indexation clause has repeatedly been treated as grounds for disqualification, even when the deviation looks minor.

Treat the guarantee like a threshold condition: wrong amount, expired validity, non-autonomous type, or off-template wording is, in practice, automatic disqualification. Verify the bank issued exactly what the template requires before you submit.

**Israeli-product preference (העדפת תוצרת הארץ).**

Under the Mandatory Tenders Regulations (Israeli-Product Preference), 5755-1995, a tender for goods gives a price preference to Israeli-made goods. The preference works through the price comparison, not by adding points: an Israeli-product offer wins the price criterion as long as its price is not more than 15% above the competing imported-goods offer. In practice the committee re-scores by dividing the Israeli offer's price by 1.15 for the price comparison, so an Israeli offer priced up to about 15% higher than an import can still come out ahead on price.

What this means for the bidder:
- If your offer qualifies as Israeli-made goods, say so explicitly and attach whatever proof of Israeli origin the tender requires. Do not leave the committee to guess.
- If you are bidding imported goods against a likely Israeli competitor, build the 15% preference into your expectations. Your nominal price has to beat the Israeli competitor's price divided by 1.15, not just their raw price.
- Separate, additional preference regimes exist for goods from national-priority areas. If the tender mentions אזורי עדיפות לאומית, check those regulations too, as they stack differently.

Always confirm the current preference percentage and mechanics against the regulations, since the tender document itself will also restate the rule that applies to that specific procurement.

### Step 7: Calculate the Submission Timeline

Tenders have multiple overlapping deadlines. Build a timeline and share it with the user.

| Milestone | Typical window | What to do |
|-----------|----------------|------------|
| Publication date | Day 0 | Download all tender documents, register as a bidder if required |
| Site visit (סיור קבלנים) | If required, usually days 5 to 10 | Attend, record every statement made, preserve the minutes |
| Clarification questions (שאלות הבהרה) | Specified in the tender, often one week before submission | Submit written questions in the format the tender requires. Do not call and ask verbally. |
| Clarification answers published | A few days after the question deadline | Re-read the answers carefully. They are binding and amend the tender document. |
| Submission deadline (מועד הגשה) | The hard gate | Submit by the method the tender specifies, before the stated hour. Late is late. Some tenders still require physical submission into a tender box at a stated address with an exact number of copies; many government tenders now use a digital tender box (for example the "Yahalom" digital submission system on mr.gov.il). Confirm which method this tender uses and never assume. |
| Opening of offers | Usually within days after submission | Some tenders permit bidder attendance at the opening |
| Clarifications and presentations | Committee initiated | Respond within the window the committee sets |
| Award notice | Variable | Losing bidders have a short window to request materials and file a challenge |

Always read the exact dates in the tender document. The generic windows above are orientation, not substitutes for the published schedule.

### Step 8: Price Intelligence via MCP Servers

If the user wants to benchmark their price offer, pair this skill with the BudgetKey MCP or IL Budget MCP to query historical procurement contracts. Both MCPs expose Israel's State Budget data including procurement contracts, and neither requires a local setup.

Useful queries:
- Find past contracts in the same subject category (for example "שירותי ניקיון", "פיתוח תוכנה", "ייעוץ ארגוני")
- Surface the typical contract size range for the same issuing body
- Identify repeat winners to understand the competitive field
- Spot which budget item the current tender will be drawn from

Frame findings as intelligence, not price advice. The user decides the final price. A skill that tells someone exactly what to bid is a skill that gets them disqualified for collusion.

## Recommended MCP Servers

Pairs with these MCP servers from the skills-il directory for live Israeli state budget and procurement data:

| MCP | What it gives you |
|-----|-------------------|
| [BudgetKey](https://agentskills.co.il/en/mcp/budgetkey) | Historical procurement contracts (1997 onward), support payments, budget book line items, government entities. Hebrew and English text search. |
| [IL Budget](https://agentskills.co.il/en/mcp/il-budget) | OpenBudget API access to the full governmental budget tree, procurement contracts, and support payments. Good for drilling into specific budget items. |

Neither MCP requires local installation. Both are HTTP hosted.

## Gotchas

Domain specific failure modes an AI agent is likely to hit if not explicitly warned:

1. **Do not paraphrase threshold conditions.** Agents tend to rewrite a clumsy Hebrew sentence to sound better. In a tender, the exact wording is the gate. Paraphrasing the threshold in the checklist creates a false positive where you tick a box you actually failed to meet.
2. **Do not invent declaration text.** Every mandatory declaration has a template in the tender document or in the annexes. The bidder must copy the template verbatim and sign. Do not draft original declaration language from scratch. If the template is missing from the tender pack, tell the user and stop.
3. **Local authority tenders are a different regime.** Chok Chovat HaMichrazim covers state bodies. Municipal tenders are governed by parallel regulations under the Municipalities Ordinance. If the issuer is a city, a regional council, or a local authority, the structure is similar but specific clauses differ. Call it out.
4. **Two envelope tenders mean two sealed envelopes.** If the tender specifies two envelopes (מעטפה א for qualifications, מעטפה ב for price), putting the price anywhere in the qualifications envelope is an automatic disqualification. Check twice before finalizing.
5. **Clarification answers override the tender document.** Once the committee publishes written answers, those answers amend the tender. Any draft written from the original document alone is stale. Always re-read the published clarifications before submission.
6. **Exact arithmetic.** Agents are sloppy with pricing worksheets. Every line total, subtotal, VAT line, and grand total must reconcile to the agora. A 1 NIS mismatch between subtotal and total has been used as a ground for disqualification.

## Reference Links

Authoritative sources used to verify the facts in this skill:

| Source | URL | What to check |
|--------|-----|---------------|
| תקנות חובת המכרזים, תשנ"ג-1993 (Nevo) | https://www.nevo.co.il/law_html/law01/242_002.htm | Current text of the regulations, including Takana 6 |
| מכרז - ויקיפדיה | https://he.wikipedia.org/wiki/%D7%9E%D7%9B%D7%A8%D7%96 | Overview of Chok Chovat HaMichrazim scope, covered bodies, exemption categories |
| חוק חובת המכרזים (כל זכות) | https://www.kolzchut.org.il/he/%D7%97%D7%95%D7%A7_%D7%97%D7%95%D7%91%D7%AA_%D7%94%D7%9E%D7%9B%D7%A8%D7%96%D7%99%D7%9D | Plain-language explanation of the Mandatory Tenders Law, covered bodies, and Takana 6 threshold conditions |
| תקנות העדפת תוצרת הארץ, תשנ"ה-1995 (Nevo) | https://www.nevo.co.il/law_html/law00/72502.htm | Current text of the Israeli-product preference regulations and the 15% mechanism |
| מינהל הרכש הממשלתי (gov.il) | https://www.gov.il/he/departments/ministry_of_finance/govunits/accountant_general_department/about | Government Procurement Administration under the Accountant General |
| BudgetKey MCP on skills-il | https://agentskills.co.il/en/mcp/budgetkey | Reference for pairing MCP for procurement contract queries |
| IL Budget MCP on skills-il | https://agentskills.co.il/en/mcp/il-budget | Reference for pairing MCP for OpenBudget contract queries |

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| The threshold conditions in the tender are vague | Some tenders phrase discretionary conditions loosely on purpose | Submit a clarification question in writing. The committee must answer in writing. |
| The price template is a PDF, not a spreadsheet | Common in old tenders | Rebuild the template in a spreadsheet with identical line labels, calculate, then transcribe back to the PDF form |
| The bidder cannot meet one statutory condition | Blocker | Stop. You cannot cure a Takana 6(a) deficiency by writing better prose. |
| The tender was amended after you started drafting | Clarification answers published | Redo Step 3, compare the new version to your checklist, and update any affected sections before submission |
| The user wants advice on filing a post-award challenge | Out of scope | This skill builds offers, not appeals. Route to an administrative law attorney. |
