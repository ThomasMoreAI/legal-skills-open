# Foreign-currency account — practical guide for Tunisian freelancers

## Why open a foreign-currency account

The dedicated banking instrument is the **PPR Devises** account (Resident Individual Foreign-Currency Account, *Compte Personne Physique Résidente en devises*) or a Convertible Dinar account.

**Important context (May 2026):** the December 2025 forex law promised that freelancers would be able to **receive and hold** foreign currency without forced conversion. However, **no application decrees have been published in JORT yet**, so the old regime is still in force in practice. Operate under the old rules until the decrees land.

Benefits of having a PPR Devises today, even under the old regime:
- Receive USD or EUR while avoiding the worst auto-conversion spread.
- Hold a working balance for international payments (SaaS, cloud, foreign platforms) within current limits.
- Convert at a chosen moment, at the daily rate.
- A small buffer against TND depreciation.

## PPR Devises — features

[src: bna.tn — *compte-personne-physique-residente-en-devises-ou-en-dinars-convertibles*]

| Feature | Value |
|---|---|
| Who can open it | Any Tunisian resident (individual) |
| Accepted currencies | USD, EUR, GBP, other convertible currencies |
| Allowed source of funds | Service-export income, foreign income, family remittances, etc. |
| Outbound convertibility | Yes, under BCT conditions (justified purpose) |
| Conversion to TND | On request, at the daily interbank rate |
| Account fees | Vary by bank (often 10–50 TND per quarter) |
| Linked card | International card possible (the technological card for online payments) |

## Banks offering PPR Devises

| Bank | Product URL | Note |
|---|---|---|
| BNA | http://www.bna.tn/fr/compte-personne-physique-residente-en-devises-ou-en-dinars-convertibles.755.html | Canonical reference found |
| BIAT | biat.com.tn (search "compte devises") | [REQUIRES VERIFICATION] |
| Attijari Bank | attijaribank.com.tn | [REQUIRES VERIFICATION] |
| ATB | atb.tn | [REQUIRES VERIFICATION] |
| Amen Bank | amenbank.com.tn | [REQUIRES VERIFICATION] |
| BTK | btknet.com | [REQUIRES VERIFICATION] |

> Comparison tip: call 2 or 3 banks before opening to compare **maintenance fees + incoming-transfer commissions + conversion grid (spread vs interbank)**.

## How to open one

1. Book an appointment with a bank advisor.
2. Bring:
   - National ID card + proof of address
   - RNE registration certificate (patente or company)
   - Expected source of income (freelance contract, client attestation, platform statement)
   - For a SUARL: articles of association + RNE extract + the appointment minutes of the manager
3. Initial deposit (often symbolic: 100 EUR / USD).
4. Sign the account agreement and activate.
5. Timing: 7–15 business days.

## Technological card

[REQUIRES MANUAL LEGAL VERIFICATION: 2026 technological-card annual cap for freelancers — historically around 6 000 TND, but it has moved]

- A card linked to the account, used for online payments in foreign currency.
- Use cases: SaaS subscriptions, AWS / cloud, foreign software purchases.
- Annual cap is set by the BCT and varies by profile.
- If the source is a TND account, conversion happens automatically at the daily rate.

## Freelance payment platforms — recommended workflow

### Option A — Payoneer (most used by TN freelancers)

1. Create a free Payoneer account.
2. Link it to Upwork / Fiverr / other platforms → receive USD.
3. Request a Payoneer payout to your Tunisian **PPR Devises** account.
4. Fees: about 3 USD per transfer + a 1–2% spread.
5. Timing: 2–5 business days.

### Option B — Wise (formerly TransferWise)

- Multi-currency accounts are not available to TN residents (Wise limits this).
- Wise can still be used to **receive** SWIFT transfers directly into your PPR Devises.
- Sometimes cheaper than Payoneer.

### Option C — Direct SWIFT

- The client pays directly to your PPR Devises via SWIFT.
- Fees: 25–50 EUR per incoming transfer + the bank's spread.
- Timing: 2–7 business days.
- **The cleanest option** for a BCT or tax audit.

### Option D — Deel / Remote / other EORs

- "Employer of Record" platforms paying in USD / EUR.
- Same workflow as Payoneer.
- Bonus: an auto-generated employment contract and source-side tax compliance.

### Option E — Stripe

- **Not available to TN-resident freelancers** as of May 2026 [REQUIRES MANUAL LEGAL VERIFICATION: confirm current Stripe TN status].
- Workarounds exist (e.g. Stripe Atlas with a US entity), but they create tax complications.

## Tax compliance — declaring foreign-currency income

⚠️ **Receiving in foreign currency does NOT exempt you from IRPP / IS.**

- Convert the gross amount to TND at the daily rate on the transaction date.
- Declare it in the annual IRPP return (real regime) or IS return (SUARL).
- Keep all supporting documents for 10 years.

## BCT audit — a real risk

- The BCT can ask the licensed intermediary (your bank) to justify the origin of incoming funds.
- The bank then asks you to produce the documents (contract, invoice, etc.) within 10–30 days.
- If the justification is insufficient: the account can be blocked until cleared, or the funds returned to the sender.

**Best practice:**

1. Open the PPR Devises account at the start of your activity, not after the first payment lands.
2. Tell the bank what your activity is (freelance dev, service export).
3. Keep invoices and contracts organized by client.
4. Convert periodically rather than accumulating huge foreign-currency balances that attract attention.

## Sources

- `data/sources.json` → `bna-compte-devises-ppr`, `tunisia-forex-deregulation-dec-2025-announcement`
- `data/bct_circulars.json` → `compte_devises_ppr`
- `bct-circulaires.md` (regulatory framework)
