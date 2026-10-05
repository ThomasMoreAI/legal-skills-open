# Israeli Investment Deal Terms Reference

Deal-term parameters and what is market in Israel, so a founder can understand and
negotiate a round and brief their lawyer. These are commercial terms, not contract
language: preparing the actual SAFE, note, share purchase agreement or articles is
work for a licensed Israeli lawyer.

## Israeli SAFE (Simple Agreement for Future Equity)

### Key Commercial Terms

| Term | What it sets | Israeli market note |
|---|---|---|
| Investment amount | Size of the cheque, and the currency it is denominated in | USD or NIS both common |
| Valuation cap | Ceiling on the conversion valuation | Post-money is now the standard; pre-money still appears in older paper. They are not interchangeable |
| Discount rate | Discount to the next round's price | 15-25% typical, 20% common |
| Conversion mechanics | How cap and discount combine | Converts at the lower of (Cap / fully-diluted shares) or (Price x (1 - Discount)); new shares in the same class as the lead investor |
| Conversion trigger | The equity financing size that forces conversion | Set as a threshold amount |
| MFN | Most-favoured-nation: this investor inherits better terms given later | Yes / No |
| Pro-rata rights | Right to participate in the next round | Yes / No |
| Information rights | Reporting the investor receives | Annual financials, or quarterly updates |
| Governing law and forum | Which law applies and where disputes go | Israeli law; courts of Tel Aviv-Jaffa |
| Language | Execution language | Hebrew, English, or both |

**Israeli-specific points to raise with counsel**
- IIA notification, if the company has taken Innovation Authority grants
- Which securities-law exemption the round relies on, and the offeree count under
  it (see the securities discussion in SKILL.md)
- Tax withholding on conversion, per ITA requirements, and on whom it falls
- Anti-money-laundering identification of the investor

### Israeli SAFE vs Y Combinator SAFE

| Aspect | YC SAFE | Israeli SAFE |
|--------|---------|-------------|
| Governing law | Delaware/California | Israeli law |
| Dispute resolution | US courts/arbitration | Tel Aviv courts |
| Tax treatment | US tax rules | Israeli tax withholding |
| Securities exemption | Reg D | Israeli private placement |
| IIA provisions | N/A | Required if IIA-funded |
| Language | English | Hebrew and/or English |
| Currency | USD | USD or NIS |

## Convertible Note

### Key Commercial Terms

A convertible note is debt, so unlike a SAFE it can become repayable and can put
the company into default. That asymmetry is the main reason to choose one over the
other.

| Term | What it sets | Israeli market note |
|---|---|---|
| Principal | Amount lent | USD or NIS |
| Interest rate | Accrues until conversion or repayment | 5-8% per annum typical |
| Maturity | When the note falls due if it has not converted | 12-24 months from issuance |
| Automatic conversion | Converts on a qualified financing above a set threshold | |
| Optional conversion | Investor may elect to convert at maturity | |
| Discount and cap | Same mechanics as a SAFE | Discount 15-25% |
| Repayment at maturity | If no conversion: principal plus accrued interest, payable on demand | This is the limb a SAFE does not have |
| Security | Whether the note is secured against company assets | Unsecured, or secured |

**Israeli tax points**
- Interest is taxed annually, with withholding at source, which is a live cash cost
  a SAFE does not carry
- Conversion is generally not an immediate tax event, subject to an ITA ruling on
  the specific facts

## Priced Round (Series A)

### Document Set
1. **Term Sheet** - Non-binding summary of key terms
2. **Share Purchase Agreement (SPA)** - Binding purchase terms
3. **Investors Rights Agreement** - Protective provisions
4. **Articles Amendment** - New share class definition
5. **Shareholders Agreement** - Governance and rights

### Standard Series A Terms (Israeli Market)

```
Investment: [Amount] USD
Pre-money Valuation: [Valuation] USD
Share Class: Series A Preferred
Price Per Share: [Price]

Liquidation Preference:
  - 1x non-participating preferred (standard)
  - Participating preferred (less common, more investor-friendly)

Anti-dilution:
  - Broad-based weighted average (standard)
  - Full ratchet (rare, very investor-friendly)

Board Composition:
  - [2] Founders / Common
  - [1] Series A Investor
  - [1] Independent (mutually agreed)
  - [1] Observer seat (optional)

Protective Provisions (require investor consent):
  - New share class issuance
  - Change of articles
  - M&A / sale of company
  - Increase in option pool
  - Related party transactions
  - Debt above [threshold]

Information Rights:
  - Monthly management report
  - Quarterly financial statements
  - Annual audited financials
  - Annual budget and operating plan

Registration Rights: [Demand / Piggyback]
Right of First Refusal: Company then investors
Co-sale Rights: Tag-along with founders
Drag-along: [Majority percentage] of preferred

Founder Vesting:
  - Reverse vesting on founder shares
  - 4-year schedule, credit for time served
  - Single trigger acceleration: [None / Partial]
  - Double trigger acceleration: [12 months]

ESOP:
  - Expand option pool to [15-20]% post-money
  - Option 102 capital gains track

IIA Provisions:
  - Represent grant obligations
  - Indemnification for IP transfer restrictions
```

## Due Diligence Checklist (Israeli Startup)

```
Corporate:
  - Company registration certificate (Rasham HaChavarot)
  - Current articles of association
  - Shareholder register
  - Board resolutions
  - Cap table (fully diluted)

IP:
  - Patent applications/grants
  - IP assignment agreements from founders/employees
  - IIA grant agreements and IP restrictions
  - Open source usage audit

Financial:
  - Audited/reviewed financial statements
  - Tax returns (corporate, VAT)
  - IIA royalty obligations
  - Outstanding debts and commitments

Employment:
  - Employment agreements
  - Option 102 plan and trustee agreement
  - Pension and severance (Bituach Menahalim)
  - Non-compete/non-solicit agreements

Regulatory:
  - IIA grants and conditions
  - Privacy/data protection compliance
  - Industry-specific licenses
  - International sanctions compliance
```
