# Krajowy Rejestr Sądowy (KRS) — Field Reference and Legal Guide

## API Overview

The Polish Ministry of Justice (*Ministerstwo Sprawiedliwości*) provides the official public API for the National Court Register at `https://api-krs.ms.gov.pl/`.

KRS maintains two main registers:
- **Rejestr Przedsiębiorców (P):** Commercial companies (Sp. z o.o., S.A., P.S.A., Spółka jawna, partnerska, komandytowa).
- **Rejestr Stowarzyszeń, Innych Organizacji Społecznych i Zawodowych, Fundacji oraz Samodzielnych Publicznych Zakładów Opieki Zdrowotnej (S):** Foundations, associations, trade unions, public healthcare units.

---

## Representation & Signing Authority (Legal Context)

Under the Polish Commercial Companies Code (*Kodeks spółek handlowych - KSH*):

1. **Sposób reprezentacji:** The articles of association determine who is legally authorized to enter into contracts and commit obligations on behalf of the company.
   - *Jednoosobowa:* Any single board member can sign.
   - *Łączna:* Requires two board members acting together, or one board member acting jointly with a commercial proxy (*prokurent*).
2. **Nieważność umów:** Signing a contract without required corporate representation may render the contract invalid under Art. 39 of the Polish Civil Code (*Kodeks cywilny*).
3. **Prokura:** A special commercial power of attorney that must be officially disclosed in the KRS register.

---

## Output Fields

### Company Summary (`info <krs>`)

| Field | Type | Description |
|---|---|---|
| `krs` | string | 10-digit padded KRS number (e.g. `0000006865`) |
| `rejestr` | string | Register description: `Przedsiębiorcy (P)` or `Stowarzyszenia/Fundacje (S)` |
| `rejestrKod` | string | Register code: `P` or `S` |
| `stanWpisu` | string | Entry status (e.g. `Aktualny`) |
| `nazwa` | string | Official registered legal name |
| `formaPrawna` | string | Legal form (e.g. `SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ`, `SPÓŁKA AKCYJNA`, `FUNDACJA`) |
| `nip` | string \| null | 10-digit Tax Identification Number |
| `regon` | string \| null | Statistical number REGON |
| `siedziba` | string | Seat city / municipality |
| `adres` | object | Address breakdown: `ulica`, `miasto`, `kodPocztowy`, `pelny` |
| `email` | string \| null | Registered electronic correspondence address |
| `stronaWww` | string \| null | Registered website URL |
| `kapitalZakladowy` | string \| null | Stated share capital with currency (e.g. `5000,00 PLN`) |
| `sposobReprezentacji` | string | Mandatory legal representation formula |
| `zarzad` | array | List of board members: `[{funkcja, nazwisko}]` |
| `zarzadLiczbaOsob` | integer | Total count of active board members |
| `prokurenci` | array | List of active proxies: `[{rodzaj, nazwisko}]` |
| `radaNadzorcza` | array | List of supervisory council members |
| `czyWLikwidacji` | boolean | `true` if entity is in liquidation |
| `czyWUpadlosci` | boolean | `true` if entity is in bankruptcy proceedings |

### Representation Check (`repr <krs>`)

| Field | Type | Description |
|---|---|---|
| `krs` | string | Checked KRS number |
| `nazwa` | string | Company name |
| `formaPrawna` | string | Company legal form |
| `sposobReprezentacji` | string | Authorized signing method |
| `zarzad` | array | Authorized board members |
| `prokurenci` | array | Authorized commercial proxies |
| `wazneZasady` | string | Reminder about representation verification |
