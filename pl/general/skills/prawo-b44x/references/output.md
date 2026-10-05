# Prawo (ISAP / ELI) — Output Reference

Official API: `https://api.sejm.gov.pl/eli` (Chancellery of the Sejm). Acts are identified as
`<publisher>/<year>/<position>`: `DU` = Dziennik Ustaw, `MP` = Monitor Polski, e.g. `DU/1974/141`.
Before 2012 the printed reference also has an issue number (`Dz.U. 1974 nr 24 poz. 141`), but the API
uses only year and position.

---

## Documents and their text versions

| Document | What the HTML contains |
|---|---|
| Original act (e.g. `DU/1974/141`) | The wording **as published**, without any later amendments |
| Consolidated text (obwieszczenie o tekście jednolitym, e.g. `DU/2023/1465`) | The full act as amended up to the obwieszczenie date |
| Newest consolidated texts (2025+) | Often **PDF only** (`textHTML: false`) |

`article` uses the newest consolidated text that has HTML. In that document, the act itself is an
annex (bookmarks `_z1_…`). Articles with the same number in the obwieszczenie's transitional
provisions are skipped.

---

## `article <ref> <nr>`

| Field | Type | Description |
|---|---|---|
| `act` | object | `ref`, `title`, `displayAddress`, `status` of the requested act |
| `article` | string | Normalised article number (`36`, `86a`, `67^18`) |
| `text` | string | Article wording. Units are on separate lines (`§ 1.`, `1)`, `a)`); superscripts are written as `^` (`§ 1^1`) |
| `truncated` | bool | `true` if the text was cut at 8000 characters |
| `sourceDocument` | object | `ref`, `displayAddress`, `title`, `kind` (`tekst jednolity`, `tekst ogłoszony (bez zmian)`, `tekst pierwotny`), `date`, `links` |
| `upToDate` | bool | `true` only if no amendment entered into force after `sourceDocument.date` and no newer consolidated text exists |
| `amendmentsAfterSource` | object | `count` and `latest[]` (`ref`, `entryIntoForce`) of amendments in force after the source date |
| `newerConsolidatedTextsPdfOnly` | array | Newer consolidated texts available only as PDF (`ref`, `pdf`) |
| `warning` | string \| null | Human-readable caveat to pass on to the user |

## `act <ref>`

| Field | Type | Description |
|---|---|---|
| `ref`, `displayAddress`, `title`, `type` | string | Identification of the act |
| `status` | string | ISAP status, e.g. `obowiązujący`, `akt posiada tekst jednolity`, `uchylony` |
| `inForce` | string | `IN_FORCE` / `NOT_IN_FORCE` |
| `entryIntoForce`, `promulgation`, `announcementDate` | date | Key dates of the original act |
| `latestConsolidatedText` | object \| null | Newest consolidated text with `textHTML`, `textPDF` and `links.pdf` |
| `amendmentsCount` | int | Number of amending acts |
| `amendmentsAfterLatestConsolidatedText` | array | Amendments entering into force after the newest consolidated text (`ref`, `entryIntoForce`) |
| `upcomingAmendments` | array | Amendments with an entry-into-force date in the future |
| `constitutionalTribunalRulings`, `implementingActs` | int | Counts of related Constitutional Tribunal rulings and implementing acts |
| `links` | object | `eli` (API), `pdf`, `isap` (human-readable ISAP page) |

## `search <query>`

`results[]` items: `ref`, `displayAddress`, `title`, `type`, `status`, `announcementDate`,
`promulgation`, `textHTML`, `textPDF`. `totalCount` is the number of matches in ISAP.

## `codes`

Offline list of shortcuts: `code` (e.g. `kp`), `ref` (e.g. `DU/1974/141`), `name`, `aliases`.
All references were verified against the ELI API.

---

## Data terms

The texts of legal acts are not protected by copyright (art. 4 of the Polish Copyright Act).
Cite ISAP / Dziennik Ustaw as the source. The official, legally binding text is the published PDF
in Dziennik Ustaw.
