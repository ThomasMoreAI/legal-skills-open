---
name: conversation-intake-shareholders-agreement-sboghossian
title: Intake — Shareholders' Agreement
description: Use when a user wants to draft a shareholders' agreement (SHA) and Claude must collect the governance, transfer, exit, and investor-rights inputs before generating the document. Triggers on requests to prepare an SHA, investment agreement, founder agreement with equity provisions, or VC term-sheet implementation. Covers MENA entity types (LLC, SAL, FZE, DIFC/ADGM Ltd) and Delaware C-Corp equivalents. Routes to draft-shareholders-agreement.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-shareholders-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Intake — Shareholders' Agreement

## When this applies

Activate when a user requests drafting of a shareholders' agreement (SHA), investment agreement, subscription and shareholders' agreement (SSA), or any instrument governing the rights and obligations of shareholders inter se and vis-à-vis the company. This skill collects the seven structural fields before routing to [[draft-shareholders-agreement]]. An SHA drafted without a complete governance and exit structure is unusable and creates disputes at the most commercially sensitive moments.

## Behavior

Multi-turn intake (typically two to three turns for VC-backed structures). The VC-specific items (item 7) are only needed if institutional investors are involved — do not ask about liquidation preference waterfall mechanics for a two-founder bootstrapped company.

## Required fields

### 1. Company

- Full legal name of the company.
- Jurisdiction of incorporation and entity type:
  - Lebanon: SAL (Société Anonyme Libanaise, public joint-stock), SARL (limited liability)
  - UAE onshore: LLC (Limited Liability Company); JSC (Joint Stock Company for larger entities)
  - DIFC: Company Limited by Shares (Ltd); Foundation for holding
  - ADGM: Private Company Limited by Shares (Ltd); SPV structures
  - KSA: LLC (Sharikat Dhat Mas'ouliyya Mahdouda); JSC (Sharikat Mosahamah)
  - Delaware: C-Corp (standard for VC-backed; S-Corp for pass-through); BVI or Cayman for offshore holding
- Share capital: authorized, issued, and paid-up capital. Current cap table (who holds what, in what class).

### 2. Shareholders

For each shareholder:
- Full legal name and entity type (individual / corporate).
- Nationality (material for foreign ownership restrictions — KSA: MISA license limits; UAE: some sectors still restrict foreign majority ownership; LB: no general foreign ownership restriction but sector-specific rules apply).
- Number and class of shares held, percentage of total equity.
- Contribution type: cash (amount and currency), in-kind assets (description and agreed valuation), services/IP (founder contribution — note tax and accounting treatment in civil-law jurisdictions where services cannot be "contributed capital" as a formal matter).
- Whether any shareholder holds under a vesting schedule — if yes, confirm the cliff (12 months standard), vesting period (4 years standard), and acceleration triggers (single-trigger vs double-trigger on change of control).

### 3. Governance

This is the core of the SHA. Confirm:

**Board composition**:
- Number of directors.
- Appointment rights: which shareholder(s) may appoint how many directors? (Common: majority shareholder appoints X; investor appoints Y; independent director(s) agreed jointly.)
- Observer seats (non-voting): VCs often take observer rights alongside or instead of a board seat pre-Series A.
- Chair: who appoints the chair? Does the chair have a casting vote? (Casting-vote clauses are common in DIFC/UK structures; avoid in civil-law contexts where they may require specific authorization.)

**Voting thresholds**:
- Simple majority (>50%) for ordinary resolutions.
- Supermajority (66.7% or 75%) for material decisions.
- Unanimity for reserved matters.

**Reserved matters list** (matters requiring investor consent or shareholder supermajority — customize, but typical list includes):
- Change of business plan / scope.
- Issue of new shares or dilutive instruments.
- M&A, merger, or disposal of material assets.
- Change of CEO / key management.
- Capital expenditure above threshold X.
- Incurring debt above threshold Y.
- Related-party transactions.
- Dividend policy / distributions.
- Winding up.

### 4. Transfer restrictions

These protect the shareholder register from unwanted parties and preserve economic alignment:

- **Right of First Refusal (ROFR)**: before a shareholder transfers shares to a third party, they must offer them to existing shareholders pro rata. Standard in virtually all SHAs.
- **Right of First Offer (ROFO)**: transferring shareholder must offer shares to existing shareholders at a stated price before marketing to third parties. Less common than ROFR.
- **Drag-along right**: majority shareholder(s) above a threshold (typically 50–75%) can compel minority shareholders to sell their shares in an M&A transaction on the same terms. Protects acquirers from minority hold-outs.
- **Tag-along right (co-sale right)**: if a majority shareholder sells, minority shareholders have the right to join the sale at the same price per share. Protects minorities from being left behind.
- **Lock-up period**: founders/key shareholders may not transfer shares for X years after signing (typically 1–3 years). Aligns founders with the company.
- **Permitted transfers**: transfers to wholly-owned subsidiaries or to family members (for estate planning) are typically permitted without triggering ROFR/ROFO. Confirm scope.
- **Change of control in a corporate shareholder**: if a shareholder is itself a company, confirm whether a change of control of that corporate shareholder triggers the ROFR — important for private equity structures.

### 5. Exit mechanics

- **IPO trigger**: what threshold of board / shareholder approval is required to initiate an IPO process?
- **Drag-along threshold and floor price**: what majority is needed to drag minorities? Is there a minimum return floor below which minority shareholders cannot be dragged (a "drag-along floor" or "minimum drag price")?
- **Put and call options**:
  - **Put option** (sell right): investor may compel the company or founders to buy their shares at a formula price in specified circumstances (investor protection on IRR floor).
  - **Call option** (buy right): founders or company may buy out investors at a formula price after a defined holding period.
- **Deadlock resolution**: what happens if the board is deadlocked on a reserved matter and cannot vote? Options: independent expert determination; shoot-out / Russian roulette (one party names a price; the other must buy or sell at that price); independent mediator; automatic dissolution (last resort).
- **Drag-along timeline**: how many days after a drag notice must closing occur?

### 6. Investor / preferred shareholder special rights

Applicable when there are institutional investors or preferred shareholders:

- **Liquidation preference**: preferred shareholders receive their investment (1x, 1.5x, or 2x non-participating) before any distribution to common shareholders on an exit or liquidation. Participating preferred: receive preference amount first, then also participate pro rata in remaining proceeds. Confirm multiplier and participation cap.
- **Anti-dilution protection**: if new shares are issued at a lower price (down round), how is the investor protected?
  - *Full ratchet*: most protective for investor — preferred converts at the new lower price.
  - *Broad-based weighted average*: most common in market practice — adjustment formula based on shares outstanding; fairly balances founder and investor interests.
  - *Narrow-based weighted average*: counts only shares in the same class; less favorable to investors than broad-based.
- **Board seat**: investor's contractual right to appoint a director (in addition to any statutory rights as a major shareholder).
- **Information rights**: investor's right to receive quarterly management accounts, annual audited financials, annual budget, and cap table within specified timeframes.
- **Pro-rata rights (participation right)**: investor's right to participate in future financing rounds to maintain their percentage ownership.
- **Most favored nation (MFN)**: investor gets terms at least as favorable as any future investor in the same round.

**VC-specific note**: Pre-money vs post-money valuation cap in the option pool. Confirm whether the employee option pool is sized pre-money (dilutes founders and investors pro rata) or post-money (dilutes only founders pre-investment). Post-money pool sizing has become standard following Y Combinator SAFE template adoption; confirm which standard applies.

### 7. Non-compete and confidentiality on shareholders

- **Non-compete**: founders or key shareholders agree not to engage in a competing business for X years after ceasing to hold shares. Duration and geographic scope: balance enforceability vs protectiveness.
  - Enforceability: UAE post-2021 labor law allows non-competes up to 2 years in same sector; KSA courts apply narrowly; UK courts apply "legitimate business interest" test; LB courts void unreasonably broad covenants.
- **Non-solicitation**: founders agree not to solicit the company's employees, clients, or suppliers for X years after ceasing to be shareholders.
- **Confidentiality**: shareholders' agreement provisions are typically confidential; each shareholder commits not to disclose the SHA terms. Exceptions: required disclosure to regulators, courts, professional advisors.

## Output

At the end of intake, produce:

1. A structured intake summary confirming all seven fields, cap table overview, and outstanding items.
2. A flag for VC-specific provisions if an institutional investor is involved.
3. A routing instruction to [[draft-shareholders-agreement]] with the completed intake data.

## Do not

- Draft a single-class equity SHA without asking whether investors or future investors need preferred shares — retrofitting preferred share mechanics into an already-signed SHA is costly.
- Apply Delaware-style preferred share mechanics directly to a Lebanese SAL or UAE LLC — civil-law entity types have mandatory governance rules (minimum board compositions, mandatory general assembly resolutions) that override contractual provisions. DIFC and ADGM are common-law and can accommodate more flexible structures.
- Omit the vesting schedule for founder shares — unvested founder shares in a multi-founder company is one of the top causes of early-stage disputes.

## Related skills

- [[draft-shareholders-agreement]]
- [[conversation-intake-incorporation]]
- [[draft-founders-agreement]]
- [[draft-term-sheet]]
- [[kb-corporate-law-mena]]
- [[conversation-uncertainty-language]]
