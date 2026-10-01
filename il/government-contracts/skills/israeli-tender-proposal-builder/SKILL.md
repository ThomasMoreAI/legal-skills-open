---
name: israeli-tender-proposal-builder
title: Israeli Tender Proposal Builder
description: Builds a complete Hebrew proposal package for Israeli government and public sector tenders (michrazim). Parses the tender document, extracts threshold conditions, produces a compliance checklist, and drafts every proposal section per Chok Chovat HaMichrazim 5752-1992 and Takanot 5753-1993 (declarations, past experience table, pricing worksheet). Use when responding to an open tender (michraz pumbi), closed (sagur), framework (misgeret), or a local authority tender, and when researching historical procurement contracts via BudgetKey or IL Budget MCP to benchmark pricing. Prevents disqualification on technical defects. Do NOT use for Israeli Land Authority (RMI) land allocation tenders (use israeli-land-tenders), for challenging a tender committee decision (disqualification or award) by administrative petition, or for private commercial RFPs not subject to the Mandatory Tenders Law.
author: skills-il
author_url: https://github.com/skills-il/legal-tech/tree/master/israeli-tender-proposal-builder
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: il
practice: government-contracts
language: en
sources:
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Mandatory Declarations
  path: references/mandatory-declarations.md
- title: Tender Types
  path: references/tender-types.md
- title: Threshold Conditions
  path: references/threshold-conditions.md
---

# Israeli Tender Proposal Builder

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


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

**Local-authority tenders are a separate rulebook, identify them first.** A city tender is governed by
תקנות העיריות (מכרזים), התשמ"ח-1987 under the Municipalities Ordinance, and local and regional councils
by parallel orders. The state rules in Steps 2 and 7 (Takana 6, the state מכרז זוטא track, the mr.gov.il
electronic box) do not apply as written. Three municipal rules change what you draft:
key municipal amounts, including the exemption and zuta thresholds, are CPI-linked (reg 2)
and move every month, so compute the current figure instead of quoting a remembered one; a bid with a fundamental reservation or a basic
change is disqualified outright (reg 20(ג)); and after the final decision every participant may inspect
the decision and the winning bid (reg 22(ט)). Those regulation numbers are the city regulations; council
orders number the same rules differently. Use the authority's own tender pack and templates.

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
3. **טבלת ניסיון קודם (Past experience table)** - One row per relevant past contract: client, subject matter, contract value in shekels, period, contact person for reference. Only include contracts that genuinely match the discretionary experience condition. Padding with irrelevant entries is a red flag for the committee.
4. **מענה מקצועי (Professional response)** - Your technical approach: methodology, team, work plan, milestones, risks and mitigations. Map each requirement in the tender's professional chapter to a specific paragraph in your response.
5. **הצעה כספית (Price offer)** - In a separate sealed envelope (מעטפה נפרדת) if the tender is two envelope. Price structure must exactly match the template the tender provides. Never add line items, never remove line items.
6. **הצהרות ותצהירים (Declarations and affidavits)** - The block of mandatory declarations (see Step 5).
7. **נספחים (Appendices)** - Licenses, certificates, proof of insurance, bank guarantee, and any other attachment required by the tender.

**Mark trade secrets now, not after the award.** Losing bidders may inspect the winning bid (state reg
21(ה)(1), within 30 days of notice; municipal reg 22(ט)). Parts whose disclosure may reveal a trade or
professional secret can be withheld, but the committee decides, and a bidder who marks nothing
weakens its own position. Mark specific passages with a one-line reason; marking the whole bid is not
credible.

Draft each section in natural, direct Israeli Hebrew. Avoid the over formal government register. The committee reads dozens of proposals and prefers clarity over pomp.

### Step 5: Assemble the Mandatory Declarations Block

Every Israeli public tender requires a standardized set of declarations. Missing any one of them is a disqualification event. Prepare these as separate documents.

A תצהיר (sworn affidavit) is not just a signed statement. It must be **sworn before a lawyer** (or another authorized person), the lawyer must warn the declarant of the criminal liability for a false declaration and confirm the declarant understood it, and the lawyer's verification block must be completed and signed. The תצהיר must also be **dated on or before the submission deadline**, never after. A declaration that is merely signed by the bidder without the lawyer's sworn-before-me verification, or that is undated or dated after submission, is defective.

| Declaration | Hebrew | Legal basis | When required |
|-------------|--------|-------------|---------------|
| Proper bookkeeping and no debts to tax authority | אישור ניהול ספרים וניכוי מס במקור | חוק עסקאות גופים ציבוריים | Every tender |
| Fair employment and minimum wage compliance | תצהיר לפי חוק עסקאות גופים ציבוריים (שכר מינימום והעסקת עובדים זרים כדין) | חוק עסקאות גופים ציבוריים, סעיף 2ב: the supplier and a related party were not convicted of more than two offences, or enough time has passed since the last one (for service contracts, three years) | Every tender |
| Adequate representation of people with disabilities | תצהיר לפי סעיף 2ב1 (ייצוג הולם לאנשים עם מוגבלות) | חוק עסקאות גופים ציבוריים, סעיף 2ב1 | Requested in every tender; what the bidder declares depends on its employee headcount, so fill in the Finance Ministry template accordingly |
| No bid coordination | תצהיר היעדר תיאום מכרז | Tender document; agreeing bid prices with a competitor is a restrictive arrangement under חוק התחרות הכלכלית (a restraint on the price to be offered), and being party to an unapproved one is a criminal offence | Usually required |
| Workers' rights compliance | תצהיר בדבר קיום חובות המציע בעניין שמירת זכויות עובדים | תקנה 6(א)(4) | Labor intensive contracts |
| No conflict of interest | תצהיר העדר ניגוד עניינים | Tender document | Usually required |
| Bribery and fraud disclosure | תצהיר היעדר הרשעות | Tender document | Usually required |
| Corporate authorization to sign | אישור עורך דין / רו\"ח על זכויות חתימה | Tender document | Every corporate bidder |

For each declaration, confirm:
- The text matches the template in the tender document exactly (do not redraft).
- Every signatory listed in the template has signed.
- The lawyer or accountant verification is attached if required.
- The declaration is dated within the validity window the tender specifies.

### Step 6: Handle the Bid Guarantee and the Preference Regimes

Two recurring elements decide tenders before the substance is even read: the bid guarantee, and the statutory preference regimes (Israeli-product, women-controlled business, and reserve-service business).

**Bid guarantee (ערבות מכרז).**

Most public tenders require the bidder to attach a bid guarantee with the offer, as proof of seriousness. Get every one of these right, because each is a known disqualification trap:

- **Amount**: the tender states an exact guarantee amount (a fixed NIS sum, or a percentage of the offer). Submit that exact amount. A guarantee for less than the required amount is disqualified, and an unexplained guarantee for more can also draw scrutiny.
- **Type**: the tender almost always demands an **autonomous bank guarantee** (ערבות בנקאית אוטונומית), meaning the issuing body can call it on demand without the bank asking questions or the bidder being able to block payment. A personal guarantee, an insurance-company guarantee, or a conditional guarantee does not satisfy an autonomous-guarantee requirement.
- **Validity period**: the guarantee must be valid through at least the date the tender specifies (often the submission deadline plus 90 days, sometimes extendable on the committee's request). A guarantee that expires too early is disqualified.
- **Exact wording**: the tender usually annexes a guarantee template. The bank must issue the guarantee in that wording. Israeli case law is strict here. A deviation in the guarantee text, the wrong beneficiary, the wrong tender number, or a missing indexation clause has repeatedly been treated as grounds for disqualification, even when the deviation looks minor.

Treat the guarantee like a threshold condition: wrong amount, expired validity, non-autonomous type, or off-template wording is, in practice, automatic disqualification. Verify the bank issued exactly what the template requires before you submit.

**The three preference regimes.**

Three statutory preferences run side by side. The first works on price; the other two are identical-score tie-breakers. Know which ones the bidder can claim and attach the proof up front.

| Regime | Hebrew | Legal basis | How it works |
|--------|--------|-------------|--------------|
| Israeli-product preference | העדפת תוצרת הארץ | תקנות חובת המכרזים (העדפת תוצרת הארץ), תשנ"ה-1995 | Price preference: an Israeli-made-goods offer wins the price criterion as long as its price is not more than 15% above the competing imported-goods offer. The committee divides the Israeli offer's price by 1.15 for the comparison. |
| Women-controlled business | העדפת עסק בשליטת אישה | חוק חובת המכרזים, תשנ"ב-1992, סעיף 2ב (עידוד נשים בעסקים) | Identical-score tie-breaker: when two or more offers tie on the highest weighted score, an offer from a business controlled by a woman wins, provided the bidder attached the required affidavit and accountant's certificate at the time of submission. |
| Reserve-service business | העדפת עסק בשליטת משרת מילואים פעיל | חוק חובת המכרזים, תשנ"ב-1992, סעיף 2ד (עידוד משרתי מילואים בעסקים זעירים, קטנים או בינוניים) | Identical-score tie-breaker for a micro, small or medium business: when offers tie on the highest weighted score, an offer from a business 50% or more controlled by an active reserve servicemember wins, provided the required declaration was attached to the bid. |

**Israeli-product preference (העדפת תוצרת הארץ), 5755-1995.** A tender for goods gives a price preference to Israeli-made goods. The preference works through the price comparison, not by adding points: an Israeli-product offer wins the price criterion as long as its price is not more than 15% above the competing imported-goods offer. In practice the committee re-scores by dividing the Israeli offer's price by 1.15 for the price comparison, so an Israeli offer priced up to about 15% higher than an import can still come out ahead on price.

- If your offer qualifies as Israeli-made goods, say so explicitly and attach whatever proof of Israeli origin the tender requires. Do not leave the committee to guess.
- If you are bidding imported goods against a likely Israeli competitor, build the 15% preference into your expectations. Your nominal price has to beat the Israeli competitor's price divided by 1.15, not just their raw price.
- 15% is only one row of the table. The same regulations set 20% for goods from the Gaza envelope area (a temporary provision until 1.9.2028),
  10% where the buyer is a government company or unit that exports at least 30% of its output, and 50%
  for Israeli textiles in specified security-body tenders. In a splittable goods tender above 30 million
  NIS, the buyer may cut a winning foreign supplier to 50% of the contract at the same price. Identify
  which row applies before pricing.

**Women-controlled business (העדפת עסק בשליטת אישה), סעיף 2ב.** This is a tie-breaker, not a price discount. When two or more offers receive an identical weighted score that is the highest score, and one of them is from a business controlled by a woman, that offer wins. To claim it the bidder must attach, with the offer itself, an accountant's certificate confirming a woman holds control of the business plus an affidavit by the controlling woman to the same effect. Control here means holding, alone or together with other women, directly or indirectly, more than 50% of any class of the means of control in the business. No certificate, no preference.

**Reserve-service business (העדפת עסק בשליטת משרת מילואים פעיל), סעיף 2ד.** The Mandatory Tenders Law adds a parallel identical-score tie-breaker for micro, small and medium businesses controlled by active reserve servicemembers, in the same mould as the women-controlled preference. When offers tie on the highest weighted score and one is from a qualifying reserve-service business, that offer wins.

- Eligibility: the business must be a micro, small or medium business in which an active reserve servicemember (משרת מילואים פעיל) who is an officer of the business holds, alone or together with other active reserve servicemembers, directly or indirectly, 50% or more of any class of the means of control. That person must have served at least 20 days of reserve duty in the 12 months before the final date for submitting offers.
- The declaration must be attached at submission and must state all three of: the holder is serving active reserve duty at the time of the offer, the business is controlled by an active reserve servicemember, and the offer is not that of a subsidiary of a large business (a business employing more than 100 employees or with annual turnover above 100 million NIS).
- Verify the exact eligibility thresholds and the precise documentation against the current statute and the specific tender document before relying on them, and have a lawyer confirm eligibility where the award turns on it.
- The law does not yet resolve what happens when tying offers include both a women-controlled business and a reserve-service business. Flag this to the user rather than guessing the order of priority.

Always confirm the current preference percentages and mechanics against the regulations and the specific tender document, since the tender will also restate the rules that apply to that procurement.

### Step 7: Calculate the Submission Timeline

Tenders have multiple overlapping deadlines. Build a timeline and share it with the user.

| Milestone | Typical window | What to do |
|-----------|----------------|------------|
| Publication date | Day 0 | Download all tender documents, register as a bidder if required |
| Site visit (סיור קבלנים) | If required, usually days 5 to 10 | Attend, record every statement made, preserve the minutes |
| Clarification questions (שאלות הבהרה) | Specified in the tender, often one week before submission | Submit written questions in the format the tender requires. Do not call and ask verbally. |
| Clarification answers published | A few days after the question deadline | Re-read the answers carefully. They are binding and amend the tender document. |
| Submission deadline (מועד הגשה) | The hard gate | Submit by the method the tender specifies, before the stated hour. Late is late. Confirm whether this tender uses the electronic tender box or physical submission (see the submission-path note below) and never assume. |
| Opening of offers | Usually within days after submission | Some tenders permit bidder attendance at the opening |
| Clarifications and presentations | Committee initiated | Respond within the window the committee sets |
| Award notice | Variable | Inspect the protocol and winning bid (state: within 30 days of notice). A challenge is an administrative petition to the district court sitting as administrative court, filed without delay and, absent another deadline, no later than 45 days after notice. Treat 45 days as a ceiling: the court may dismiss a petition for delay even when it is filed within the deadline (reg 4), and the inspection window runs at the same time. Raise any objection to the tender's own terms before submitting; a bidder who bids without objecting may find a later challenge to those terms harder. Route to a lawyer at once. |

Always read the exact dates in the tender document. The generic windows above are orientation, not substitutes for the published schedule.

**Submission path: the electronic tender box.** Central-government tenders are increasingly submitted through the electronic tender box rather than a physical box. The Government Procurement Administration (מינהל הרכש הממשלתי) runs the government procurement portal (mr.gov.il), and its upgraded "Yahalom" (יהלום) system, built on the Merkava (מרכבה) platform, includes a digital tender box (תיבה דיגיטלית) for online submission. When the tender routes through the electronic tender box:
- Register on the portal early. Account setup, vendor verification, and any digital-certificate enrollment take time and cannot be rushed in the final hour.
- The תצהיר (sworn affidavit) workflow is affected. A physically signed and lawyer-verified affidavit usually has to be scanned and uploaded, and some electronic submissions require a digital certificate or qualified e-signature on the upload itself. Confirm in the tender document whether a scanned wet-ink affidavit is accepted or whether an electronic-signature certificate is mandatory, and leave time to obtain the certificate if it is.
- Upload well before the cutoff. The system timestamps submission, and a connection problem at the deadline is still a late submission.

Some tenders, especially local-authority ones, still require physical submission into a tender box at a stated address with an exact number of copies. Always confirm which path applies before finalizing.

A note on thresholds: the financial threshold that separates an open tender (מכרז פומבי) from a closed "zuta" tender (מכרז זוטא), and the mandatory-tender floor below which a tender is not required at all, are under active reform, including devolution of exemption authority toward ministry tender committees and a reported rise in the mandatory-tender floor. Do not classify a tender from a remembered threshold number. Verify the current NIS thresholds on the Government Procurement Administration portal (mr.gov.il) or in the regulations before deciding which track a procurement falls into.

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
3. **Local authority tenders are a different regime.** Chok Chovat HaMichrazim covers state bodies. City tenders are governed by the municipal tender regulations, and local and regional councils by parallel orders. The structure is similar but the rules and their numbering differ. Call it out (see Step 1).
4. **Two envelope tenders mean two sealed envelopes.** If the tender specifies two envelopes (מעטפה א for qualifications, מעטפה ב for price), putting the price anywhere in the qualifications envelope is an automatic disqualification. Check twice before finalizing.
5. **Clarification answers override the tender document.** Once the committee publishes written answers, those answers amend the tender. Any draft written from the original document alone is stale. Always re-read the published clarifications before submission.
6. **Never attach a reservation or a condition.** Agents like to "protect" the bidder with "subject to", "our
   price assumes", or a rewritten clause. In a municipal tender a fundamental reservation or basic change
   disqualifies the bid outright (reg 20(ג)). The state regulations have no equivalent rule, but state tender documents commonly reserve the right to disqualify such a bid or to ignore the reservation, so read yours. Put every doubt
   into a clarification question before the deadline instead.
7. **Exact arithmetic.** Agents are sloppy with pricing worksheets. Every line total, subtotal, VAT line, and grand total must reconcile to the agora. A one-shekel mismatch between subtotal and total has been used as a ground for disqualification.

## Reference Links

Authoritative sources used to verify the facts in this skill:

| Source | URL | What to check |
|--------|-----|---------------|
| תקנות חובת המכרזים, תשנ"ג-1993 (Nevo) | https://www.nevo.co.il/law_html/law01/242_002.htm | Current text of the regulations, including Takana 6 |
| חוק חובת המכרזים, תשנ"ב-1992 (Nevo) | https://www.nevo.co.il/law_html/law01/242_001.htm | Current text of the Mandatory Tenders Law: covered bodies and the public-tender duty, סעיף 2ב women-controlled preference, סעיף 2ד reserve-service preference |
| חוק חובת המכרזים (כל זכות) | https://www.kolzchut.org.il/he/חוק_חובת_המכרזים | Plain-language explanation of the Mandatory Tenders Law, covered bodies, and Takana 6 threshold conditions |
| תקנות העדפת תוצרת הארץ, תשנ"ה-1995 (Nevo) | https://www.nevo.co.il/law_html/law00/72502.htm | Current text of the Israeli-product preference regulations and the 15% mechanism |
| תקנות העיריות (מכרזים) (Wikisource) | https://he.wikisource.org/wiki/%D7%AA%D7%A7%D7%A0%D7%95%D7%AA_%D7%94%D7%A2%D7%99%D7%A8%D7%99%D7%95%D7%AA_(%D7%9E%D7%9B%D7%A8%D7%96%D7%99%D7%9D) | Municipal regime: CPI linkage, reg 20(ג) reservations, reg 22(ט) inspection |
| מינהל הרכש הממשלתי | mr.gov.il | Government Procurement Administration portal, Yahalom electronic tender box, current tender thresholds |
| BudgetKey MCP on skills-il | https://agentskills.co.il/en/mcp/budgetkey | Reference for pairing MCP for procurement contract queries |
| IL Budget MCP on skills-il | https://agentskills.co.il/en/mcp/il-budget | Reference for pairing MCP for OpenBudget contract queries |

## Troubleshooting

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| The threshold conditions in the tender are vague | Some tenders phrase discretionary conditions loosely on purpose | Submit a clarification question in writing. The committee must answer in writing. |
| The price template is a PDF, not a spreadsheet | Common in old tenders | Rebuild the template in a spreadsheet with identical line labels, calculate, then transcribe back to the PDF form |
| The bidder cannot meet one statutory condition | Blocker | Stop. You cannot cure a Takana 6(a) deficiency by writing better prose. |
| The tender was amended after you started drafting | Clarification answers published | Redo Step 3, compare the new version to your checklist, and update any affected sections before submission |
| The user wants to challenge the award | Out of scope, but time-critical | This skill builds offers, not petitions. Tell the user the route is an administrative petition to the district court, that the clock usually runs from the notice (45 days absent another deadline, reg 3(ב) of the administrative-courts procedure regulations), and route them to an administrative law attorney the same day. |
