# Terminy — Rules, Legal Basis and Output Reference

All rules were checked against the texts of the acts in ISAP (via the `prawo` skill) on the date in
`rulesVerified` (2026-09-28). The script works offline and makes no network requests.

---

## Rules and legal basis

| Rule | Legal basis |
|---|---|
| Statutory days off: 1 Jan, 6 Jan, Easter Sunday and Monday, 1 May, 3 May, Pentecost Sunday, Corpus Christi, 15 Aug, 1 Nov, 11 Nov, 25–26 Dec, and all Sundays | art. 1 ustawy z 18 stycznia 1951 r. o dniach wolnych od pracy |
| 24 December (Wigilia) is a day off from 2025 | Dz.U. 2024 poz. 1965 (in force 2025-02-01) |
| Easter date | Gregorian computus (Meeus/Jones/Butcher); Pentecost = Easter + 49 days, Corpus Christi = Easter + 60 days |
| Working day | Monday–Friday that is not a statutory holiday |
| Working-time norm = 8 h × Mon–Fri days in the period − 8 h × each holiday not on a Sunday | art. 130 § 1–2 Kodeksu pracy |
| A tax or social-security deadline on a Saturday or holiday moves to the next working day | art. 12 § 5 Ordynacji podatkowej |
| A civil-law term ending on a Saturday or holiday ends on the next working day | art. 115 Kodeksu cywilnego |
| The starting day of a term counted in days is not counted | art. 111 § 2 Kodeksu cywilnego |

### Monthly deadlines (day of the month after the settlement month)

| ID | Day | Obligation | Legal basis |
|---|---|---|---|
| `zus-jednostki-budzetowe` | 5 | ZUS contributions, budget units | art. 47 ust. 1 pkt 2 ustawy o systemie ubezpieczeń społecznych |
| `zus-osoby-prawne` | 15 | ZUS contributions, payers with legal personality | art. 47 ust. 1 pkt 3 ustawy o sus |
| `ppk` | 15 | PPK contributions | art. 28 ust. 4 ustawy o PPK |
| `zus-pozostali` | 20 | ZUS contributions, other payers (JDG, partnerships) | art. 47 ust. 1 pkt 4 ustawy o sus |
| `pit-zaliczka` | 20 | Monthly PIT advance of a taxpayer | art. 44 ust. 6 ustawy o PIT |
| `pit-platnik` | 20 | PIT advances withheld by a payer (e.g. from salaries) | art. 38 ust. 1 ustawy o PIT |
| `cit-zaliczka` | 20 | Monthly CIT advance | art. 25 ust. 1a ustawy o CIT |
| `vat` | 25 | VAT return (JPK_V7M) and VAT payment | art. 99 ust. 1 i art. 103 ust. 1 ustawy o VAT |

---

## Output fields

### `month <RRRR-MM>`

| Field | Type | Description |
|---|---|---|
| `workingDays` | int | Working days (Mon–Fri without holidays) |
| `workingTimeNormHours` / `workingTimeNormDays` | int | Working-time norm for a full-time employee |
| `holidays` | array | Holidays in the month (`date`, `weekday`, `name`) |
| `saturdayHolidays` | array | Holidays on a Saturday (they reduce the norm) |
| `calculation` | string | The arithmetic behind the norm |

### `deadlines <RRRR-MM>`

`deadlines[]` items: `id`, `obligation`, `nominalDate` (day before shifting), `deadline` (final),
`weekday`, `shifted`, `shiftReason` (holiday name or weekday), `legalBasis`.

### `add <date> <N>`

Calendar days: `nominalEnd`, `deadline`, `shifted`, `rule`. With `--workdays`: `result`.

### `workdays`, `holidays`, `day`

Self-describing: `workingDays`, `calendarDays`, `holidays[]`; `isWorkingDay`, `holiday`, `nextWorkingDay`.

Every response includes `rulesVerified`.
