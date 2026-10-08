---
name: kb-shariah-finance-aaoifi-sboghossian
title: Knowledge Pack — Shariah Finance and AAOIFI Standards
description: Use when a matter involves Sharia-compliant financial products, Islamic banking structures, sukuk issuance, takaful, or the use of AAOIFI standards. Covers the major Islamic finance structures (murabaha, ijara, mudaraba, musharaka, sukuk, tawarruq, wakala, salam, istisna), compliance markers for drafting, AAOIFI and IFSB standard-setting roles, Sharia Supervisory Board requirements, and the DIFC/ADGM Islamic finance overlay. Relevant for any transaction involving KSA or UAE onshore parties, Islamic banks, halal investment funds, or Sharia certification. Triggers on Islamic finance, sukuk, murabaha, AAOIFI, Sharia-compliant, takaful, halal investment, or Islamic banking questions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-shariah-finance-aaoifi
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Knowledge Pack — Shariah Finance and AAOIFI Standards

## What Is Shariah-Compliant Finance

Islamic finance is the practice of structuring financial transactions in accordance with Islamic Sharia principles. The core prohibitions are:

| Prohibition | Arabic Term | Meaning |
|---|---|---|
| Interest | **Riba** | Any predetermined return on a loan; applies to both charged and received interest |
| Excessive uncertainty | **Gharar** | Contractual uncertainty; ambiguity about subject matter, price, or delivery |
| Speculation | **Maisir** | Gambling or highly speculative transactions |
| Prohibited industries | **Haram** | Alcohol, pork, conventional insurance (with interest), weapons of mass destruction, adult entertainment, conventional financial services |

The affirmative principles:
- **Profit-and-loss sharing**: both parties share upside and downside risk.
- **Asset backing**: financial transactions must be backed by real assets or services.
- **No money for money**: money is a medium of exchange, not a tradeable commodity.

---

## Standard-Setting Bodies

| Body | Headquartered | Role |
|---|---|---|
| **AAOIFI** | Bahrain | Accounting and Auditing Organization for Islamic Financial Institutions; issues Sharia Standards (88+), accounting standards, governance standards; voluntary adoption; KSA, Bahrain, UAE make AAOIFI standards mandatory or reference |
| **IFSB** | Kuala Lumpur | Islamic Financial Services Board; prudential standards for banking, insurance (takaful), capital markets; adopted by regulators |
| **Higher Shariah Authority (UAE)** | Abu Dhabi | UAE Central Bank (CBUAE) national Sharia authority for UAE Islamic finance |
| **SAMA Sharia Committee** | Riyadh | SAMA's Sharia oversight for KSA banking and financial products |
| **Sharia Supervisory Boards (SSBs)** | Institution-level | Each Islamic bank and financial institution; individual scholars; issue fatwas (religious opinions) certifying products |

---

## Key Islamic Finance Structures

### 1. Murabaha (Cost-Plus Sale)

**How it works**:
- Bank purchases the asset (commodity, property, equipment) from a third-party supplier.
- Bank sells the asset to the customer at **cost + agreed profit margin** (the margin is disclosed).
- Customer pays the purchase price in **deferred installments**.

**Sharia compliance**: the bank must actually acquire and own the asset before selling it (even briefly). A "back-to-back" or "reverse murabaha" that is only notional is Sharia-questionable.

**Use cases**: home finance, vehicle finance, trade finance (commodity murabaha), working capital lending.

**Drafting**: replace "interest rate" with "profit margin" or "murabaha profit"; document the commodity purchase leg with transfer documentation.

---

### 2. Ijara (Lease)

**How it works**:
- Bank purchases the asset and **leases it** to the customer for a rental payment.
- Optional: at the end of the lease term, ownership transferred to customer (Ijara wa Iqtina — lease ending in ownership transfer, by gift or nominal sale).
- Equivalent to: conventional finance lease.

**Sharia compliance**: bank must bear ownership risk during the lease (e.g., responsibility for major maintenance, insurance). Rental must relate to the actual use of the asset.

**Use cases**: property finance, equipment leasing, aircraft finance, vessel finance.

---

### 3. Mudaraba (Profit-Sharing Partnership)

**How it works**:
- **Rabb al-mal** (investor): provides all the capital.
- **Mudarib** (manager): provides expertise and management.
- **Profits** split per pre-agreed ratio (e.g., 70/30).
- **Losses**: borne exclusively by the investor (rabb al-mal); the mudarib loses only time and effort.

**Use cases**: investment funds, Islamic deposit accounts (depositors = investors; bank = mudarib), sukuk structuring.

---

### 4. Musharaka (Partnership / Joint Venture)

**How it works**:
- Both parties contribute **capital and management**.
- Profits and losses shared proportionately to capital contribution (or per agreed ratio, within Sharia limits).
- All partners may participate in management.

**Diminishing Musharaka (Musharaka Mutanaqisa)**:
- Bank and customer co-own property.
- Customer gradually buys the bank's share over time.
- Rental payments from customer to bank for use of bank's share reduce as customer's ownership increases.
- Ends with customer owning 100%.
- Widely used for home finance in KSA, UAE, Malaysia.

---

### 5. Sukuk (Islamic Bond / Certificates)

**Definition**: asset-backed or asset-based certificates evidencing ownership of or a claim over an underlying asset/pool. Returns paid from the underlying asset's revenues, not from interest.

**Key structures**:

| Sukuk Type | Structure | Cash Flow Source |
|---|---|---|
| Ijara sukuk | Sukuk holders own the underlying asset; it is leased back to originator | Rental payments |
| Murabaha sukuk | Sukuk evidences entitlement to murabaha receivables | Murabaha profit margin installments |
| Mudaraba sukuk | Sukuk holders are investors in a mudaraba | Share of mudaraba profits |
| Wakala sukuk | Sukuk holders appoint a wakeel (agent) to invest on their behalf | Returns on invested pool |
| Musharaka sukuk | Sukuk holders are musharaka partners | Share of musharaka profits and losses |

**AAOIFI Sharia Standard 17 (Investment Sukuk)** governs sukuk structures globally.

**Sovereign sukuk**: KSA, UAE, Bahrain, and international sovereigns issue sukuk regularly as an alternative to bonds.

**Corporate sukuk**: real estate companies, banks, and conglomerates issue sukuk for capital raising.

**Tradability**: sukuk must be structured on asset-ownership basis (not pure debt) for secondary market trading to be Sharia-permissible.

---

### 6. Tawarruq (Commodity Murabaha)

**How it works**:
- Customer needs cash.
- Bank arranges commodity purchase on behalf of customer (at cost).
- Bank immediately sells the commodity to a third-party broker.
- Customer receives cash proceeds.
- Customer owes the bank the commodity price on deferred terms (cash + profit margin).

**Use cases**: personal loans, working capital, Islamic credit facilities, term deposits (reverse tawarruq).

**Sharia controversy**: some scholars (notably AAOIFI minority view) are uncomfortable with organized tawarruq because the commodity transaction is often notional. AAOIFI Sharia Standard 30 permits "organised tawarruq" with specific conditions; some scholars disagree. Disclose if SSB has reviewed.

---

### 7. Wakala (Agency)

**How it works**:
- Investor appoints a bank or fund manager as **wakeel** (agent) to invest funds.
- Wakeel earns a management fee (not a share of profit — distinguishes from mudaraba).
- Investment profit passed to investor; losses borne by investor.

**Use cases**: Islamic asset management, sukuk proceeds management, insurance (takaful) fund management.

---

### 8. Salam (Advance Payment Sale)

- Buyer pays full price **in advance** for goods to be delivered in the future.
- Price, quantity, quality, and delivery date must be precisely specified.
- **Use case**: agricultural finance (payment for future crop harvest); some trade finance.
- **Restriction**: gold and silver may not be subject to salam (riba concern).

### 9. Istisna (Construction Sale / Manufacture Contract)

- Contract for construction or manufacture of a specified asset.
- Payment in stages as construction progresses (or in advance, or on delivery — flexible).
- **Use case**: project finance, construction finance, aircraft/vessel construction.
- Closely related to Ijara (often combined: Istisna to construct; Ijara for the completed asset).

---

## Compliance Markers in Drafting

When drafting or reviewing Islamic finance documents:

| Issue | Islamic Finance Standard |
|---|---|
| "Interest" / "interest rate" | Replace with "profit margin", "fee", "rental payment", "murabaha profit" |
| Late-payment penalty going to lender | Not permissible (would be riba); restructure as charitable donation or as pre-agreed "incentive" for early payment |
| Guarantee of return | Pure capital guarantee not permissible in mudaraba (investor bears loss risk) |
| Asset backing | Every transaction must identify the underlying asset; document the transfer of asset ownership |
| SSB approval | Products must have a fatwa from a qualified SSB; include compliance certification in deal documents |
| Commodity murabaha | Document commodity purchase and sale steps (even if synthetic) per AAOIFI Standard 30 |
| Sukuk principal | At maturity, principal should come from the underlying asset proceeds, not from a guaranteed repurchase at face value — AAOIFI Sharia Standard 17 guidance |

---

## When Islamic Finance Is Relevant

| Situation | Islamic Finance Impact |
|---|---|
| KSA onshore parties | All banking products must be Sharia-compliant in KSA |
| UAE Islamic banks (Emirates NBD Islamic, DIB, ADIB) | Products structured per AAOIFI; separate SSB certifies each product |
| Sukuk issuance (KSA, UAE, GCC) | Transaction documentation requires SSB sign-off; AAOIFI standards reference |
| Halal investment funds | Fund structure must avoid haram industries; investment screening required |
| Real estate finance with Islamic bank | Murabaha or diminishing musharaka for home/commercial finance |
| Family wealth structures | Sharia-compliant wills and estate planning (fara'id; limited bequest) |
| DIFC / ADGM Islamic finance | DIFC Regulatory Authority has Islamic finance guidelines; ADGM FSRA similarly |

---

## AAOIFI Standards Reference

| Standard No. | Topic |
|---|---|
| No. 2 | Murabaha |
| No. 7 | Mudaraba |
| No. 12 | Musharaka |
| No. 17 | Investment Sukuk |
| No. 26 | Takaful |
| No. 30 | Tawarruq |
| No. 31 | Wakala |
| No. 59 | Sale of Debt |

AAOIFI publishes 88 Sharia standards; all are available for purchase from AAOIFI. Some are freely summarized on AAOIFI's website.

---

## Caveats & Currency

Sharia standards are evolving — AAOIFI regularly updates its standards and issues new ones. Individual Sharia Supervisory Boards may issue opinions that differ from AAOIFI positions. For any specific Islamic finance transaction, obtain a fatwa from the relevant institution's SSB — general knowledge of structures does not substitute for product-specific Sharia certification. The Sharia-compliance status of certain structures (e.g., organized tawarruq, returns-linked sukuk) is actively debated among Islamic scholars. This pack reflects well-established, majority scholarly positions.

## Related Skills

- [[kb-fintech-licensing-cma-ksa]]
- [[kb-fintech-licensing-difc]]
- [[kb-insurance-takaful-mena]]
- [[kb-real-estate-ksa]]
- [[kb-family-law-ksa]]
