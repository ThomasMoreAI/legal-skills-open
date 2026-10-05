# Biała Lista Podatników VAT — Field Reference and Legal Context

## API Overview

The Polish Ministry of Finance (Ministerstwo Finansów - KAS) maintains the official White List of VAT Taxpayers (*Wykaz podatników VAT*).

Official API base: `https://wl-api.mf.gov.pl/api`

### Why verification matters (Legal Context)

1. **Split Payment & Sankcje podatkowe**: Under Polish tax law (Ustawa o VAT, art. 96b), B2B payments above 15,000 PLN gross (or in foreign currency equivalent) to active VAT taxpayers must be made to bank accounts registered on the White List.
2. **Koszty uzyskania przychodów**: Paying to an unverified bank account deprives the buyer of the ability to classify the expense as tax-deductible (*koszt uzyskania przychodów - KUP*).
3. **Solidarna odpowiedzialność**: The buyer risks joint liability (*solidarna odpowiedzialność*) for unpaid VAT up to the amount of VAT on the invoice, unless a notification (ZAW-NR) is filed with the tax office within 7 days.
4. **Identyfikator wyszukiwania (`requestId`)**: Every request to the official API returns an immutable cryptographic verification ID (`requestId`) and timestamp (`requestDateTime`). Saving this ID serves as proof of due diligence (*dowód dochowania należytej staranności*) during tax audits.

---

## Output Fields

### Entity Search (`nip`, `regon`, `account`)

| Field | Type | Description |
|---|---|---|
| `name` | string | Full legal name of company / sole proprietorship (CEIDG / KRS) |
| `nip` | string | 10-digit Tax Identification Number (raw) |
| `nipFormatted` | string | Formatted NIP (`XXX-XXX-XX-XX`) |
| `statusVat` | string | Official VAT status: `Czynny`, `Zwolniony`, `Niezarejestrowany` |
| `isVatActive` | boolean | `true` if `statusVat` equals "Czynny" |
| `regon` | string | Statistical identification number (9 or 14 digits) |
| `krs` | string \| null | National Court Register number (for companies) |
| `pesel` | string \| null | PESEL number (masked / null in public API) |
| `residenceAddress` | string \| null | Residential address (for individuals / sole proprietors) |
| `workingAddress` | string \| null | Registered business seat / office address |
| `registrationLegalDate`| string \| null | Date registered for VAT (`YYYY-MM-DD`) |
| `hasVirtualAccounts` | boolean | `true` if entity uses virtual / sub-accounts (e.g. telecom, utility, large bank) |
| `accountCount` | integer | Number of registered settlement bank accounts |
| `accounts` | array | List of bank account objects `{raw, formatted, bank}` |
| `representatives` | array | Legal representatives (Zarząd): `{firstName, lastName, pesel, nip}` |
| `authorizedClerks` | array | Commercial proxies (Prokurenci): `{firstName, lastName, pesel, nip}` |
| `partners` | array | Partners (Wspólnicy): `{firstName, lastName, pesel, nip}` |
| `removalDate` | string \| null | Date of removal from VAT register if deregistered |
| `removalBasis` | string \| null | Legal basis for VAT deregistration |
| `restorationDate` | string \| null | Date of restoration to VAT register |
| `restorationBasis` | string \| null | Legal basis for VAT restoration |
| `requestId` | string | Ministry of Finance cryptographic query token (audit proof) |
| `requestDateTime` | string | Query date and time as recorded by Ministry of Finance |

### Bank Account Verification (`check <nip> <account>`)

| Field | Type | Description |
|---|---|---|
| `nip` | string | Checked NIP |
| `nipFormatted` | string | Formatted NIP |
| `account` | string | Checked 26-digit bank account number |
| `accountFormatted` | string | Formatted account (`XX XXXX XXXX XXXX XXXX XXXX XXXX`) |
| `bank` | string | Identified bank name (based on 4-digit bank routing code) |
| `accountAssigned` | string | `"TAK"` or `"NIE"` directly from the Ministry of Finance |
| `isAssigned` | boolean | `true` if `"TAK"`, `false` if `"NIE"` |
| `date` | string | Date for which status was verified (`YYYY-MM-DD`) |
| `requestId` | string | Cryptographic verification ID (audit proof) |
| `requestDateTime` | string | Timestamp of verification |

### Offline Checksum Validation (`validate <value>`)

| Field | Type | Description |
|---|---|---|
| `input` | string | Original input string |
| `digits` | string | Digits-only stripped string |
| `length` | integer | Length of stripped string |
| `valid` | boolean | Whether mathematical checksum is valid |
| `type` | string | `"nip"`, `"regon_9"`, `"regon_14"`, `"iban_pl"`, or `"unknown"` |
| `formatted` | string \| null | Standard human-readable formatting |
| `bank` | string \| null | Bank name (for 26-digit account) |
| `message` | string | Verification message or error details |

---

## Virtual Accounts (Rachunki Wirtualne / Subkonta)

Large service providers (telecoms like Orange/Play, energy suppliers, leasing companies) issue individual **virtual payment accounts** (*rachunki wirtualne*) to each customer.

- When `hasVirtualAccounts: true`, customer-specific payment account numbers might not appear directly in the `accounts` array.
- However, the `check <nip> <account>` endpoint accurately recognizes valid virtual accounts linked to the company's master account and returns `accountAssigned: "TAK"`.
