# Bank, tax and company identifiers

Authoritative basis: ISO 13616 (IBAN) via the SWIFT IBAN Registry; the EU VIES service (`ec.europa.eu/taxation_customs/vies/rest-api/`, probed live 2026-08-05); the Australian Business Register (`abr.business.gov.au/Help/AbnFormat`). IBAN lengths below were read from `ibantools` 4.5.4, whose country table is derived from the IBAN Registry — regenerate them from the registry itself before shipping.

**A checksum proves the format. Only a registry proves existence.** Every algorithm here catches typos and transpositions. None of them tells you the account is open, the company trades, or the VAT number entitles anyone to a zero-rated invoice. Do not describe a checksum pass to the user as "verified".

## IBAN — ISO 13616

Structure: two-letter ISO 3166-1 country code, two check digits, then the country's BBAN. Length is **fixed per country**, maximum 34 characters overall. The check is ISO 7064 MOD-97-10: move the first four characters to the end, replace each letter with its position value (`A`=10 … `Z`=35), and the resulting integer modulo 97 must equal 1.

```js
const IBAN_LENGTH = {
  AD:24, AE:23, AT:20, BE:16, BG:22, BR:29, CH:21, CR:22, CY:28, CZ:24,
  DE:22, DK:18, EE:20, EG:29, ES:24, FI:18, FR:27, GB:22, GR:27, HR:21,
  HU:28, IE:22, IL:23, IS:26, IT:27, LI:21, LT:20, LU:20, LV:21, MC:27,
  MT:31, NL:18, NO:15, PL:28, PT:25, RO:24, SA:24, SE:24, SI:19, SK:24,
  SM:27, TR:26, UA:29, XK:20,
};

function mod97(digits) {                    // string of digits, arbitrary length
  let r = 0;
  for (const ch of digits) r = (r * 10 + Number(ch)) % 97;
  return r;
}

export function isValidIBAN(input) {
  // strip spaces (incl. NBSP and narrow NBSP) and hyphens, upper-case
  const iban = input.replace(/[\s  -]/g, '').toUpperCase();
  if (!/^[A-Z]{2}\d{2}[A-Z0-9]+$/.test(iban)) return false;
  if (iban.length < 15 || iban.length > 34) return false;
  const expected = IBAN_LENGTH[iban.slice(0, 2)];
  if (expected && iban.length !== expected) return false;
  const rearranged = iban.slice(4) + iban.slice(0, 4);
  const numeric = [...rearranged]
    .map(c => (/\d/.test(c) ? c : String(c.charCodeAt(0) - 55)))
    .join('');
  return mod97(numeric) === 1;
}
```

Verified against `AT611904300234573201`, `DE89370400440532013000`, `CH9300762011623852957`, `GB82WEST12345698765432`, `FR1420041010050500013M02606`, `NL91ABNA0417164300`, `IT60X0542811101000000123456`, `MT84MALT011000012345MTLCAST001S`, `NO9386011117947` (all pass) and against single-digit mutations of each (all fail).

Non-European countries are in the registry too — Brazil (29), Saudi Arabia (24), UAE (23), Türkiye (26), Israel (23), Ukraine (29), Egypt (29), Costa Rica (22), Kosovo (20) — and none of those is in SEPA. Registry membership and SEPA reachability are different questions; if the IBAN is for a SEPA direct debit, check SEPA membership separately.

Storage: `text`, upper-case, no spaces. Display in groups of four. Never store the grouped form. Never store an IBAN in a column narrower than 34 characters.

## BIC — ISO 9362

Eight or eleven characters: four-character institution code (letters), two-character ISO 3166-1 country code, two-character location code, and an optional three-character branch code. `[[UNVERIFIED: the current ISO 9362 edition and the exact character-class restrictions on the location code were not confirmed against a primary source; treat the structural check below as a format hint only]]`

For SEPA payments inside the EEA the BIC is generally not required — IBAN-only is the norm. Do not make BIC a mandatory field for a European payer.

## VAT identification numbers and VIES

The European Commission states only that "each EU country uses its own format of VAT identification number" and that it "begins with the code of the country concerned followed by a block of digits or characters" (`taxation-customs.ec.europa.eu/vat-identification-numbers_en`, checked 2026-08-05); the per-state structure table is no longer published on that page. `[[UNVERIFIED: any per-Member-State VAT format table you write — the Commission no longer publishes one in HTML. Use format only as an input hint, never as a rejection.]]`

Two country-code traps, both verified live against the VIES API on 2026-08-05:

- **Greece is `EL`, not `GR`,** in VIES and on invoices. ISO 3166-1 says `GR`. A form that sends `GR` gets a rejection that looks like an invalid VAT number.
- **Northern Ireland is `XI`,** a separate VIES participant from `GB`, which is not a participant at all.

Austria's VAT number carries a fixed literal `U` after the country code (`ATU12345675`) — the only Member State whose identifier contains a fixed letter in that position.

### The VIES REST API

Verified live 2026-08-05.

```
POST https://ec.europa.eu/taxation_customs/vies/rest-api/check-vat-number
Content-Type: application/json
{"countryCode":"IE","vatNumber":"6388047V"}

→ {"countryCode":"IE","vatNumber":"6388047V","requestDate":"2026-08-05T…Z",
   "valid":true,"requestIdentifier":"",
   "name":"GOOGLE IRELAND LIMITED",
   "address":"3RD FLOOR, GORDON HOUSE, BARROW STREET, DUBLIN 4",
   "traderName":"---", "traderNameMatch":"NOT_PROCESSED", …}
```

```
GET  https://ec.europa.eu/taxation_customs/vies/rest-api/check-status
  → { "vow": {"available": true}, "countries": [{"countryCode":"AT","availability":"Available"}, …] }

GET  https://ec.europa.eu/taxation_customs/vies/rest-api/countries
  → per country: { approxMatching, hasName, hasAddress, hasCompanyType }
```

What the responses actually tell you, verified:

- **Name and address are not returned by every Member State.** `DE811569869` came back `valid: true` with `name` and `address` both `"---"`. `IE6388047V` came back with the full company name and address. Germany deliberately returns nothing. Any UI that shows "we could not confirm the company name" as a failure will be wrong for every German customer.
- **`valid: false` does not distinguish a malformed number from an unassigned one.** Probing every Member State with deliberately wrong-length numbers returned plain `valid: false` in each case with no format-specific error. You cannot use VIES to learn the format.
- **The service rate-limits per Member State.** A burst of probes returned `{"errorWrappers":[{"error":"MS_MAX_CONCURRENT_REQ"}]}` with `valid: null`. Treat a null `valid` as "unknown, retry later", never as invalid.
- **Member States go offline.** `check-status` exists because individual national systems become unavailable. Cache a positive result and fall back to it during an outage; blocking a checkout on a VIES timeout costs you the order.
- **`approxMatching` is available for very few Member States** — of the 28 participants (27 plus `XI`), only `ES` reported `approxMatching: true` on 2026-08-05. The trader-name matching fields exist in every response but come back `NOT_PROCESSED` unless the Member State supports it.

Store the `requestDate` and, where the API returns one, the `requestIdentifier` (the consultation number) as evidence that the check was made. That record is what an audit asks for.

## National company and tax identifiers

| Country | Identifier | Shape | Offline checksum? |
|---|---|---|---|
| AT | Firmenbuchnummer | `FN 123456a` — digits plus one check letter | `[[UNVERIFIED: check-letter algorithm not publicly documented in a source I could confirm]]` |
| AT | GISA-Zahl | trade-register number | no |
| AT | UID | `ATU` + 8 digits | `[[UNVERIFIED]]`; use VIES |
| DE | HRA / HRB | court-scoped, e.g. `HRB 12345 B`, Amtsgericht München | no — the court is part of the identity |
| DE | USt-IdNr. | `DE` + 9 digits | `[[UNVERIFIED]]`; use VIES |
| DE | W-IdNr. | `[[UNVERIFIED: format and rollout status as at 2026 not confirmed against BZSt]]` | — |
| FR | SIREN / SIRET | 9 / 14 digits | **yes** — Luhn |
| FR | n° TVA | `FR` + 2-char key + SIREN | key formula below |
| IT | Partita IVA | 11 digits | **yes** — Luhn-style |
| IT | Codice fiscale | 16 alphanumeric | yes, own check character |
| CH | UID | `CHE-123.456.789` (+ `MWST`/`TVA`/`IVA` suffix) | **yes** — mod-11, weights 5,4,3,2,7,6,5,4 |
| GB | Company number | 8 characters, optional `SC`/`NI`/`OC` prefix | no |
| US | EIN | `12-3456789` | no |
| AU | ABN | 11 digits | **yes** — mod-89 |
| AU | ACN | 9 digits | **yes** — mod-10 |

### Working implementations

```js
// France: SIREN and SIRET are Luhn. SIRET 356 000 000 xxxxx (La Poste) is the
// documented exception and fails a plain Luhn check.
function luhn(s) {
  let sum = 0, dbl = false;
  for (let i = s.length - 1; i >= 0; i--) {
    let d = +s[i];
    if (dbl) { d *= 2; if (d > 9) d -= 9; }
    sum += d; dbl = !dbl;
  }
  return sum % 10 === 0;
}
export const isValidSIREN = s => /^\d{9}$/.test(s) && luhn(s);
export const isValidSIRET = s => /^\d{14}$/.test(s) && (luhn(s) || s.startsWith('35600000'));

// French VAT key. [[UNVERIFIED: formula not confirmed against a DGFiP publication;
// it produces self-consistent keys but has not been checked against a primary source]]
export const frenchVatKey = siren =>
  String((12 + 3 * (Number(siren) % 97)) % 97).padStart(2, '0');
// frenchVatKey('552081317') === '03'  ->  FR03552081317

// Switzerland: UID mod-11. Remainder 10 means the number is invalid, not zero.
export function isValidCHE(uid) {
  const d = uid.replace(/\D/g, '');
  if (d.length !== 9) return false;
  const w = [5, 4, 3, 2, 7, 6, 5, 4];
  const sum = w.reduce((a, wi, i) => a + wi * +d[i], 0);
  const r = 11 - (sum % 11);
  if (r === 10) return false;
  return (r === 11 ? 0 : r) === +d[8];
}
// isValidCHE('CHE-116.281.710') === true

// Australia: ABN. Algorithm as published by the ABR:
// subtract 1 from the first digit, apply the weights, sum, mod 89 must be 0.
const ABN_WEIGHTS = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
export function isValidABN(abn) {
  const d = abn.replace(/\s/g, '');
  if (!/^\d{11}$/.test(d)) return false;
  const n = [...d].map(Number);
  n[0] -= 1;
  return n.reduce((a, x, i) => a + x * ABN_WEIGHTS[i], 0) % 89 === 0;
}
// isValidABN('51 824 753 556') === true

// Australia: ACN, weights 8..1, check digit is the mod-10 complement.
export function isValidACN(acn) {
  const d = acn.replace(/\s/g, '');
  if (!/^\d{9}$/.test(d)) return false;
  const w = [8, 7, 6, 5, 4, 3, 2, 1];
  const s = w.reduce((a, wi, i) => a + wi * +d[i], 0);
  return (10 - (s % 10)) % 10 === +d[8];
}

// Italy: partita IVA, Luhn variant doubling the odd-indexed positions.
// [[UNVERIFIED: not confirmed against an Agenzia delle Entrate publication;
// validates known-good values]]
export function isValidPartitaIVA(p) {
  if (!/^\d{11}$/.test(p)) return false;
  let s = 0;
  for (let i = 0; i < 11; i++) {
    let n = +p[i];
    if (i % 2 === 1) { n *= 2; if (n > 9) n -= 9; }
    s += n;
  }
  return s % 10 === 0;
}
```

All of the above were executed on Node 22 and pass their stated known-good values and fail single-digit mutations.

## Rules for using any of this

- **Normalise before checking.** Strip spaces, non-breaking spaces, dots and hyphens; upper-case. `CHE-116.281.710`, `CHE 116281710` and `che116281710` are the same identifier.
- **Store the canonical form, display the punctuated form.** One column, no formatting in it.
- **A failed checksum is a warning, not a wall,** unless the value goes straight to a system that will reject it (a payment file, a tax return). Say what failed: "This IBAN's check digits do not match — one character is probably mistyped."
- **Never log a full IBAN or a full tax number** at info level. They are identifying and, for IBAN, directly financially useful.
- **Country identifiers are court-, region- or authority-scoped in Germany and Austria.** A German HRB number without its Amtsgericht is not an identifier; store the court alongside it.

## Checkpoints

- [ ] IBAN stored upper-case without spaces in a column of at least 34 characters
- [ ] IBAN checked with mod-97 **and** the per-country length table
- [ ] IBAN length table regenerated from the IBAN Registry, not copied from a blog post
- [ ] BIC not required for SEPA payments
- [ ] VAT numbers checked against VIES, not against a hand-written per-country regex
- [ ] Greece sent as `EL`, Northern Ireland as `XI`, and `GB` not sent to VIES at all
- [ ] Missing `name`/`address` in a VIES response is not treated as a failure (Germany returns `"---"`)
- [ ] `valid: null` plus an `errorWrappers` entry treated as "unknown, retry", not as invalid
- [ ] VIES `requestDate` and consultation identifier stored as evidence
- [ ] A VIES outage falls back to a cached positive result instead of blocking checkout
- [ ] Every identifier normalised before checking and stored canonically
- [ ] German and Austrian register numbers stored with their court or authority
- [ ] Full IBANs and tax numbers absent from application logs
- [ ] No checksum pass described to the user as "verified"
