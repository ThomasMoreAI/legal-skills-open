# Sejm RP CLI — Output and Data Schema Reference

All commands return structured JSON on standard output (`stdout`), and errors on `stderr`.
Missing values are returned as `null`, and empty collections as `[]`.

---

## 1. `mps` (or `mp`)

Fetches the database of MPs of the Sejm RP (default: X kadencja, 10th term).

### Search / list:
`python3 scripts/sejm.py mps [--search <surname>] [--club <club>] [--district <district>]`

| Field | Type | Description |
|---|---|---|
| `id` | int | Unique MP identifier in the Sejm RP database |
| `firstLastName` | string | MP's first and last name (e.g. `"Szymon Hołownia"`) |
| `club` | string | Abbreviation of the parliamentary club (klub) or circle (koło) (e.g. `"PiS"`, `"KO"`, `"Polska2050"`, `"PSL-TD"`, `"Konfederacja"`, `"Lewica"`, `"Razem"`, `"niez."`) |
| `districtName` | string | Seat of the district electoral commission (e.g. `"Białystok"`, `"Gdańsk"`, `"Warszawa"`) |
| `districtNum` | int | Electoral district number |
| `voivodeship` | string | Voivodeship (województwo) |
| `email` | string | Official e-mail address in the `@sejm.pl` domain |
| `active` | bool | Whether the MP's mandate is active |
| `profession` | string | Profession declared by the MP |

### MP details and committees:
`python3 scripts/sejm.py mps --id <id>`

Additional fields:
- `birthDate`, `birthLocation`, `educationLevel`, `numberOfVotes`, `oathDate`
- `committees`: list of Sejm committees the MP sits on, with the role held (`"przewodniczący"`, `"zastępca przewodniczącego"`, `"członek"`).

---

## 2. `voting`

Fetches detailed results of a single voting, the per-club summary and a specific MP's vote.

`python3 scripts/sejm.py voting <sitting> <voting> [--mp <surname_or_id>]`

| Field | Type | Description |
|---|---|---|
| `term` | int | Term (kadencja) number (e.g. `10`) |
| `sitting` | int | Sejm sitting (posiedzenie) number |
| `votingNumber` | int | Voting number within the sitting |
| `date` | string | Exact date and time of the voting, ISO-8601 |
| `title` | string | Full official voting title (e.g. agenda item, print number) |
| `topic` | string | Voting topic / short description |
| `totalVoted` | int | Number of MPs who took part in the voting |
| `majorityVotes` | int | Required majority of votes |
| `majorityType` | string | Majority type (e.g. `"SIMPLE_MAJORITY"`, `"ABSOLUTE_MAJORITY"`) |
| `results` | object | Overall results: `yes`, `no`, `abstain`, `notParticipating` |
| `clubSummary` | object | Aggregated results for each club: `{ "PiS": {"total": 194, "yes": 192, "absent": 2}, ... }` |
| `mpVote` | object \| null | Vote of the specified MP: `{ "id": 133, "name": "...", "club": "...", "vote": "YES" }` |

MP vote values (`vote`):
- `YES` — for
- `NO` — against
- `ABSTAIN` — abstained
- `ABSENT` / `NOT_PARTICIPATING` — absent / did not participate

---

## 3. `votings`

Overview of votings at a given Sejm sitting.

`python3 scripts/sejm.py votings [--sitting <no>] [--search <phrase>]`

---

## 4. `prints` (or `print`)

Search and retrieve druki sejmowe (Sejm prints: bills, draft resolutions, committee reports, motions).

`python3 scripts/sejm.py prints [--number <no>] [--search <phrase>]`

| Field | Type | Description |
|---|---|---|
| `number` | string | Druk sejmowy (Sejm print) number |
| `title` | string | Official print title |
| `documentDate` | string | Date the document was drawn up |
| `deliveryDate` | string | Date of receipt / delivery to the Sejm |
| `attachments` | string[] | PDF attachment files available in the API |
| `processPrint` | string[] | Related print numbers in the legislative process |

---

## 5. `process`

Tracking the stages of the legislative process for a given print / bill.

`python3 scripts/sejm.py process <print_number>`

| Field | Type | Description |
|---|---|---|
| `number` | string | Print number |
| `title` | string | Title of the bill or draft resolution |
| `titleFinal` | string \| null | Final title of the adopted legal act |
| `documentType` | string | Document type (e.g. `"projekt ustawy"`, `"projekt uchwały"`) |
| `processStartDate` | string | Date processing started in the Sejm |
| `closureDate` | string \| null | Date work in the Sejm was completed |
| `passed` | bool | Whether the act / resolution was passed by the Sejm |
| `displayAddress` | string \| null | Entry in the Dziennik Ustaw or Monitor Polski (official journals) |
| `stages` | list | Chronological list of work stages: `{ "date", "stageName", "stageType", "sitting" }` |
| `links` | list | Links to ISAP, ELI and the text of the act |

---

## 6. `interpellations`

Search interpelacje poselskie (MPs' interpellations) and ministries' replies.

`python3 scripts/sejm.py interpellations [--number <no>] [--search <phrase>] [--mp-id <id>]`

| Field | Type | Description |
|---|---|---|
| `number` | int | Interpellation number |
| `title` | string | Interpellation title |
| `receiptDate` | string | Date of receipt by the Marszałek Sejmu (Speaker of the Sejm) |
| `sentDate` | string | Date forwarded to the competent ministry |
| `fromMpIds` | string[] | Identifiers of the submitting MPs |
| `toRecipients` | string[] | Recipients (e.g. `"minister finansów"`, `"minister infrastruktury"`) |
| `replies` | list | Ministries' replies: reply author, receipt date, modification date |

---

## 7. `terms`

Catalog of Sejm RP terms (kadencje I to X). Works 100% offline.

---

## Exit Codes

| Code | Meaning | Agent Action |
|---|---|---|
| `0` | Success | Read the result from the JSON on `stdout` |
| `2` | Not found | MP, voting, print or process does not exist |
| `64` | Validation / argument error | Check the command parameters |
| `69` | Sejm RP server / network error | Temporary Sejm API error; retry shortly |

---

## Neutrality and Copyright

The data comes from the official Open API of the Sejm Rzeczypospolitej Polskiej (`https://api.sejm.gov.pl/`). Under Polish copyright law, official materials, documents and parliamentary materials are not subject to copyright (art. 4 of the ustawa o prawie autorskim i prawach pokrewnych — Act on Copyright and Related Rights). Responses should always cite the data source: **Kancelaria Sejmu RP**, and clearly specify the term (kadencja) and the case identifier.
