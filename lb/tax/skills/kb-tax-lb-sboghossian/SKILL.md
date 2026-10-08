---
name: kb-tax-lb-sboghossian
title: Knowledge Pack — Lebanese Tax Law
description: Use when a user asks about Lebanese tax law, income tax, VAT, withholding obligations, stamp duty, or tax compliance for individuals or entities operating in Lebanon. Covers the Lebanese Income Tax Law, Built Property Tax, VAT regime, withholding tax on cross-border payments, and the practical realities of compliance in an economy operating under severe fiscal and monetary constraints since 2019.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-tax-lb
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: lb
practice: tax
language: en
---

# Knowledge Pack — Lebanese Tax Law

## Scope

This pack covers the core Lebanese tax framework administered by the Ministry of Finance (MoF) and its Revenue Department. Lebanon's tax system is codified primarily in the Income Tax Law (Legislative Decree 144/1959 as amended) and supplemented by the VAT Law (Law 379/2001). In practice, tax compliance is complicated by the ongoing banking and monetary crisis (since 2019), exchange-rate instability, and intermittent MoF circulars adjusting for lollar/fresh dollar distinctions. Always verify the current MoF rate tables and circulars before advising.

---

## Governing Authorities

- **Ministry of Finance (MoF) — Revenue Department (Direction des Revenus)**: primary tax authority; issues assessments and rulings
- **Ministry of Finance — VAT Directorate**: VAT registration, returns, and audits
- **Order of Accountants**: licensed auditors must certify financial statements underlying tax filings

---

## Corporate Income Tax (CIT)

| Parameter | Detail |
|-----------|--------|
| Rate | 17% flat on net taxable profit of legal entities (SAL, SARL, partnerships) |
| Legal basis | Income Tax Law (Decree 144/1959) as amended, particularly by Law 64/2017 |
| Resident scope | Lebanese-registered companies taxed on Lebanon-source profits |
| Non-resident | Taxed only on Lebanese-source income; branch taxation at 17% on attributed profits |
| Advance payments | Quarterly advance payments on prior-year liability |
| Filing deadline | Annual return filed within 5 months of fiscal year-end (typically 31 May for calendar-year filers) |

**Practical trap — currency:** Lebanon operates a dual/multi-tier exchange rate. The MoF has issued circulars requiring translation of foreign-currency transactions at Sayrafa or official rates. Tax computations, especially for companies receiving USD revenues, must follow current MoF guidance or face reassessment.

---

## Tax on Salaries, Wages, and Pensions

| Rate band | Monthly taxable income (LBP or fresh USD equivalent) |
|-----------|------------------------------------------------------|
| 2% | First bracket |
| 4% | Second bracket |
| 7% | Third bracket |
| 11% | Fourth bracket |
| 15% | Fifth bracket |
| 20% | Top bracket |

- Employer withholds at source (PAYE equivalent) monthly
- Annual reconciliation by employer
- National Social Security Fund (NSSF) contributions are separate (employer: ~23.5%; employee: ~3%) and deductible for CIT purposes

---

## Tax on Profits of Liberal Professions and Non-Commercial Activities

- Rate: 10% flat on net income for individuals carrying on a liberal profession (lawyers, doctors, engineers, accountants)
- Filing: annual, based on actual receipts/disbursements or deemed profit depending on profession
- Deemed-profit regimes apply where MoF prescribes flat percentages of gross receipts

---

## Built Property Tax (Tax on Rental Income)

| Tenant situation | Rate |
|------------------|------|
| Leased to commercial tenants (non-Old Rent Law) | 4%–14% progressive on annual rental value |
| Owner-occupied residential | Deemed annual value; lower progressive rates |

- Administered by the Directorate General of Property
- Separate from CIT — property held by companies is still subject to this regime in addition to CIT

---

## Value Added Tax (VAT)

| Parameter | Detail |
|-----------|--------|
| Standard rate | 11% |
| Legal basis | Law 379/2001 and amendments |
| Registration threshold | LBP 100 million annual turnover (verify current MoF circular — threshold has been adjusted periodically) |
| Filing | Monthly or quarterly depending on turnover category |
| Zero-rated | Exports of goods and services, international transport |
| Exempt | Education, healthcare, certain financial services, sale/lease of residential buildings, agricultural inputs |

**Currency trap:** VAT returns must now account for the exchange rate on which the transaction was denominated — a critical point for businesses invoicing in USD or receiving USD payments. MoF circulars 521–525 (and subsequent) address the treatment; always check the most recent guidance.

---

## Withholding Tax (WHT) on Cross-Border Payments

| Payment type | Rate |
|--------------|------|
| Technical / managerial services to non-residents | 7.5% of gross (deemed 50% taxable × 15% rate) |
| Royalties to non-residents | 7.5% |
| Dividends to non-residents | 10% (under Distribution Tax — see below) |
| Interest to non-residents on bonds / deposits | 10% (standard) |
| Rental payments to non-residents | 7.5% |

**Filing:** Withholder files and remits monthly to MoF; late payment attracts penalties.

---

## Distribution (Dividend) Tax

- **Rate:** 10% on profits distributed to shareholders (both resident and non-resident)
- Applies when a SAL or SARL declares dividends
- Closely held companies often retain profits; retained earnings taxed at 10% if later distributed
- Companies capitalising profits (by issuing bonus shares) may defer distribution tax

---

## Capital Gains Tax

- **Immovable property:** Capital gains on sale of real property by companies are included in CIT base (17%). Individuals pay a separate Real Estate Gains Tax at rates graduated by holding period.
- **Movable property / shares:** Gains on disposal of shares in Lebanese companies are generally exempt for individuals; companies include in CIT base.
- **Listed securities:** Gains on LSE-listed shares are generally exempt.

---

## Stamp Duty

- **0.3%** on most commercial contracts presented for registration or enforcement in Lebanon
- Applies to contracts, commercial instruments, lease agreements, and court filings
- Critical for cross-border contracts: any contract referencing Lebanese law or signed in Lebanon may attract stamp duty if ever produced before a Lebanese court or notary

---

## Transfer Pricing

Lebanon has no comprehensive TP framework equivalent to OECD guidelines. Related-party transactions are reviewed under general anti-avoidance principles; the MoF may challenge transactions lacking arm's-length pricing on an ad hoc basis. Multinational groups with Lebanese subsidiaries typically prepare informal TP documentation to mitigate audit risk.

---

## Double Tax Treaties (DTTs)

Lebanon has treaties with roughly 30+ countries, including the UAE, France, Egypt, Cyprus, and several Eastern European and North African jurisdictions. Treaties generally reduce WHT rates on dividends, interest, and royalties. Verify treaty status — some are under renegotiation, and the economic crisis has affected bilateral discussions.

---

## Practical Compliance Realities (Post-2019)

The Lebanese economic and banking crisis creates unique compliance complications:

1. **Exchange rate chaos:** Tax calculations denominated in LBP must follow MoF-issued rates (Sayrafa or Banque du Liban official rate), which diverge sharply from the parallel market. Misapplication is a common audit trigger.
2. **Payment of taxes in fresh USD:** Some MoF obligations must now be settled in fresh USD (cash or foreign transfers) per more recent legislation — verify current requirements.
3. **NSSF contributions:** NSSF is severely underfunded; payments in LBP have been treated as partial settlement. Obtain formal NSSF compliance certificates before M&A closings.
4. **Latent liabilities:** Many Lebanese companies have unresolved prior-year MoF assessments. Due diligence on Lebanese targets must include a thorough tax liability review going back to at least 2015.

---

## How to Use This Pack

Load this pack when the user's query involves:
- Lebanese corporate tax compliance or structuring
- Salary tax or NSSF obligations for Lebanese-headquartered entities
- VAT registration and return preparation in Lebanon
- WHT on cross-border payments involving Lebanese entities
- M&A due diligence on Lebanese companies (tax exposure)
- Comparison of Lebanese tax burden vs UAE/KSA alternatives

Pair with [[kb-corporate-lb]] for entity structure context and [[kb-tax-uae]] / [[kb-tax-ksa]] for cross-border MENA structuring.

---

## Caveats & Currency

Lebanese tax law and administrative practice are unusually fluid. MoF circulars issued in response to the economic crisis have modified rate bases, currency treatments, and filing deadlines repeatedly since 2019. This pack reflects the general statutory framework; always confirm:
1. Current MoF circulars on currency translation
2. Up-to-date registration thresholds (VAT, NSSF)
3. Treaty status for any cross-border payments
4. NSSF certificate requirements for M&A

This pack does not constitute tax advice. Engage a Lebanese-licensed tax adviser or certified accountant for specific positions.

---

## Related skills

- [[kb-tax-uae]]
- [[kb-tax-ksa]]
- [[kb-corporate-lb]]
- [[kb-employment-lb]]
- [[review-contract-lb]]
