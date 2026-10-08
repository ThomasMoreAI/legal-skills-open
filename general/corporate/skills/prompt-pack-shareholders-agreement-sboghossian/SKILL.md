---
name: prompt-pack-shareholders-agreement-sboghossian
title: Shareholders Agreement
description: Use when drafting a full shareholders' agreement for a company with multiple shareholders, covering board composition, reserved matters, share transfer restrictions (ROFR, tag-along, drag-along), dividend policy, deadlock resolution, and exit mechanisms. Builds on the key terms agreed in prompt-pack-shareholder-agreement-key-terms into a full legal instrument. MENA-specific guidance addresses UAE onshore LLC, DIFC, ADGM, and KSA company law requirements, notarization needs, and enforceability of transfer and governance provisions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-shareholders-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Shareholders Agreement

## When to use this

Use this skill when:
- The commercial key terms have been agreed (see [[prompt-pack-shareholder-agreement-key-terms]]) and a full legal instrument is needed.
- A company has two or more shareholders and needs a legally binding governance document.
- A joint venture between two companies is being formalized in a company structure.
- A private equity or venture capital investor requires a SHA as a condition of investment.
- A company is preparing for external investment and needs to establish a governance framework.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Company name, jurisdiction, and entity type** | Determines governing law and structural constraints | Ask |
| **Shareholders, their shareholdings, and proportions** | Core of the SHA | Ask; state percentages and share classes |
| **Board composition agreement** | Who appoints directors; total board size | Ask; refer to agreed key terms |
| **Transfer restriction mechanics** | ROFR / ROFO / tag / drag parameters agreed | Ask; use [[prompt-pack-shareholder-agreement-key-terms]] to settle these first |
| **Exit mechanics** | IPO / trade sale / put-call parameters | Ask |
| **Governing law** | Determines enforceability of specific provisions | Ask; key choice: UAE onshore / DIFC / ADGM / KSA |

## Document structure

1. **Parties and recitals**
   - Names and jurisdictions of all shareholders.
   - Name and jurisdiction of the company.
   - Brief commercial context of the arrangement.

2. **Definitions and interpretation** — comprehensive; reference key-terms definitions; define:
   - Shareholders, Founders, Investors, Company.
   - Board, Directors, Chairperson.
   - Permitted Transfer, Change of Control, Encumbrance.
   - Transfer Mechanics defined terms (ROFR/ROFO Price, Tag Price, Drag Notice).
   - Reserved Matters, Deadlock, Deadlock Notice.
   - Material Adverse Change, Fair Market Value.
   - Exit Event, IPO, Trade Sale, Completion.

3. **Corporate governance**

   **3.1 Board composition:**
   - Total number of directors: [X].
   - Each Shareholder's board appointment right tied to their percentage holding (include a table: e.g., 15%+ → 1 seat; 30%+ → 2 seats; majority → number of seats that gives majority of board).
   - Appointment and removal: each shareholder may appoint and remove the director(s) they are entitled to nominate.
   - Independent directors: [number and appointment process].
   - Chairperson: appointed by [majority shareholder / by rotation / elected by board].
   - Casting vote: chairperson has a casting vote on deadlocked board resolutions except Reserved Matters.
   - Alternate directors: allowed or prohibited.

   **3.2 Board meetings:**
   - Frequency: at least [4] times per year.
   - Notice: [7/14] days before each meeting; emergency meetings with [48 hours'] notice.
   - Quorum: minimum [X] directors, including at least [1] director appointed by each shareholder holding above [Y%].
   - Voting: decisions by simple majority of directors present and voting, except Reserved Matters.
   - Written resolutions: permitted by unanimous written consent.

   **3.3 Reserved matters:**
   - Full list of matters requiring approval beyond a simple board majority.
   - Threshold per matter: supermajority board vote (e.g., 75%), unanimous board, or shareholder approval.
   - Practical guidance: divide the reserved matters list into three tiers:
     - Tier 1 (unanimous shareholder approval): change of business, change of constitutional documents, liquidation.
     - Tier 2 (shareholder supermajority, e.g., 75%): major acquisitions, debt above threshold, IPO.
     - Tier 3 (minority investor veto): related-party transactions, changes to dividend policy, CEO appointment/removal.

4. **Financial matters**

   **4.1 Business plan and annual budget:**
   - Board approves annual business plan and budget within [60/90] days before each financial year-end.
   - Material deviation from the approved budget triggers a Reserved Matter.

   **4.2 Dividend policy:**
   - Dividends distributed at the discretion of the board (or: minimum distribution of [X%] of net profit if distributable).
   - Preferred dividend for [Investor]: [X%] per annum cumulative (or non-cumulative), paid before any ordinary dividend.

   **4.3 Financing:**
   - New debt or equity financing above [threshold] requires Reserved Matter approval.
   - Pre-emption rights on new share issuances: each shareholder has the right to subscribe pro-rata to maintain their percentage holding.

5. **Transfer of shares**

   **5.1 Lock-up:** No shareholder may transfer any shares for [18/24/36] months from the date of this Agreement, except to Permitted Transferees.

   **5.2 Permitted transfers:** Transfers to affiliates (wholly owned subsidiaries, holding companies) and to the shareholder's estate on death; subject to the transferee executing a Deed of Adherence.

   **5.3 Right of first refusal (ROFR):**
   - If a shareholder (Offeror) wishes to transfer shares, it must first serve a Transfer Notice on all other shareholders stating the price and terms.
   - Other shareholders may elect to purchase the offered shares pro-rata within [30] days.
   - If not all offered shares are taken up, the remaining shareholders may elect to acquire the balance.
   - If not fully taken up within [60] days, Offeror may sell to the proposed third-party buyer on terms no more favorable than those in the Transfer Notice.

   **5.4 Tag-along rights:**
   - If any shareholder (Selling Shareholder) proposes to sell shares representing [X%] or more of the issued share capital, the other shareholders may elect to tag-along and sell their shares to the same buyer on the same price per share and terms.
   - Tag notice must be given within [20] days of receiving the Selling Shareholder's notice.
   - If the buyer is unwilling to acquire the tagged shares, the Selling Shareholder may not proceed with the sale.

   **5.5 Drag-along rights:**
   - If shareholders holding [75%] or more of the shares agree to sell to a bona fide third-party buyer in an arm's-length transaction, they may require all other shareholders to sell their shares to the same buyer at the same price per share.
   - Drag conditions: (a) price is at or above [agreed minimum or a return multiple]; (b) drag-along exercised in good faith; (c) all shareholders treated equally per share.
   - Dragged shareholders may contest the price by requesting an independent valuation; if the independent valuation confirms fair value, they must sell.

   **5.6 Change of control:**
   - If a shareholder undergoes a change of control (a third party acquires more than 50% of that shareholder's voting rights), the remaining shareholders have the right to purchase that shareholder's shares at FMV.

6. **Deadlock**
   - Deadlock defined: any Board or Shareholder matter where no resolution can be passed within [30/60] days despite good-faith efforts.
   - Escalation: CEOs to meet within [15] days; senior principals to meet within [30] days.
   - If unresolved: either party may serve a Deadlock Notice.
   - Mechanism: [choose: Texas Shootout / Russian Roulette / Expert Determination / Windup] — per agreed key terms.
   - Deadlock on Reserved Matters only: some SHAs restrict deadlock mechanisms to Reserved Matters only; ordinary board matters resolved by casting vote.

7. **Exit provisions**

   **7.1 IPO:**
   - If shareholders holding [majority] approve an IPO, all shareholders must support and cooperate.
   - Post-IPO lock-up: [180 days / 12 months] for founders; [90 days / 6 months] for investors.
   - Listing venue: [agreed exchange or "major international exchange"].

   **7.2 Trade sale:**
   - Any shareholder holding above [X%] may initiate a sale process; the Company appoints an investment bank to run a process.
   - All shareholders must cooperate with due diligence, management presentations, and finalizing sale documentation.

   **7.3 Investor put option:**
   - If no IPO or Trade Sale is completed by [date], [Investor] may put its shares to [Founders / Company] at [Cost + IRR / FMV / formula price].
   - Exercise period: [6 months] following the trigger date.

8. **Information rights**
   - Monthly management accounts: within [15] days of month-end.
   - Quarterly financial reports: within [30] days of quarter-end.
   - Annual audited accounts: within [90/120] days of year-end.
   - Board papers: circulated [7] days before board meeting.
   - Access rights: [Investor] may inspect the books and records of the Company on [X] Business Days' notice, no more than twice per year.

9. **Confidentiality**
   - Each shareholder agrees to keep the terms of this Agreement and the company's business information confidential.
   - Permitted disclosures: regulatory filings, lenders (confidentiality basis), tax advisors.
   - Duration: 2 years post-termination.

10. **Representations and warranties**
    - Each party represents: capacity to enter; shares owned free and clear; no other shareholder agreements in relation to the shares.

11. **Termination**
    - This Agreement terminates on: (a) unanimous agreement; (b) completion of a Trade Sale or IPO; (c) winding-up of the Company.
    - Individual shareholder ceases to be a party on transfer of all their shares.

12. **Governing law and dispute resolution**
    - State clearly; for UAE onshore: UAE law; for DIFC: DIFC law; for KSA: Saudi law.
    - Arbitration: [Institution] Rules, seat [City].

13. **Miscellaneous** — entire agreement; amendments in writing; no waiver; severability; counterparts; assignment (no assignment without consent, except to Permitted Transferee).

14. **Schedule: Deed of Adherence** — template for new shareholders to adhere to the SHA on joining.

## Jurisdictional notes

### UAE — onshore LLC
- The SHA operates alongside the notarized MOA/AOA; where they conflict, UAE courts may give primacy to the notarized constitutional documents.
- Key SHA provisions (especially transfer restrictions) should be incorporated into or referenced in the notarized MOA to be fully enforceable against third parties.
- Reserved matters that require MOA amendments (e.g., changes to capital, changes to management structure) must go through notarization.

### DIFC
- SHA is a straightforward contract; DIFC Contract Law applies.
- Can be paired with DIFC Articles of Association that incorporate or mirror key SHA provisions (especially transfer restrictions).
- No notarization required; electronic signatures recognized.

### KSA
- Saudi LLC: key SHA terms should be incorporated into the company's articles to the extent possible, as the articles govern the company-law aspects; the SHA governs inter-shareholder obligations.
- Articles amendments require notarization and MISA registration.

## Drafting standards

- Resolve all key terms (use [[prompt-pack-shareholder-agreement-key-terms]]) before drafting the full SHA — this avoids renegotiating in the middle of drafting.
- Use a Deed of Adherence schedule — any new shareholder must execute it to be bound.
- For the Reserved Matters list: over-inclusiveness is better than under-inclusiveness; a Reserved Matter that is never invoked costs nothing; a missing Reserved Matter can cause a governance crisis.
- Include a Shareholder Representative designation if the SHA involves multiple individual co-investors in the same shareholder bloc; this avoids the need to get all their signatures on every consent.

## Common mistakes

- **SHA conflicts with MOA.** If the SHA says "no share transfer without board approval" but the MOA allows free transfer, a buyer may be able to transfer in breach of the SHA but in compliance with the MOA; ensure consistency.
- **No drag-along price floor.** A drag without a price floor allows the majority to drag at a nominal price; include a minimum value protection.
- **Reserved matters list too broad.** If every ordinary business decision requires shareholder approval, the company is ungovernable; calibrate thresholds to the company's size and deal profile.
- **Exit mechanics without funding.** A put option requiring founders to buy out an investor at a multi-million dollar price is unenforceable if the founders do not have the funds; pair with a funding mechanism or acceptance that company redemption is the backstop.

## Related skills

- [[prompt-pack-shareholder-agreement-key-terms]]
- [[prompt-pack-share-purchase-agreement]]
- [[prompt-pack-shareholders-resolution]]
- [[prompt-pack-related-party-transaction-policy]]
- [[heuristic-always-state-jurisdiction-first]]
