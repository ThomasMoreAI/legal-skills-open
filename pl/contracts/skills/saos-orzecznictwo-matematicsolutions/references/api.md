# SAOS API - pelna referencja

Zrodlo: https://www.saos.org.pl/help/index.php/dokumentacja-api
Endpoint produkcyjny: `https://www.saos.org.pl/api`
Instancja testowa: `https://saos-test.icm.edu.pl/api`

Wszystkie odpowiedzi to JSON. Brak autoryzacji. Brak limitow zapytan opisanych
w dokumentacji (ale nie zalewaj API - paginuj rozsadnie, do hurtu jest Dump API).

---

## 1. Search API - `GET /api/search/judgments`

### Parametry zapytania

| Parametr | Typ | Uwagi |
|---|---|---|
| `all` | tekst | pelnotekstowo po calej tresci orzeczenia |
| `legalBase` | tekst | podstawa prawna |
| `referencedRegulation` | tekst | przywolany akt prawny |
| `judgeName` | tekst | nazwisko sedziego |
| `caseNumber` | tekst | sygnatura akt, np. `I ACa 772/13` |
| `courtType` | enum | `COMMON` `SUPREME` `CONSTITUTIONAL_TRIBUNAL` `NATIONAL_APPEAL_CHAMBER` `ADMINISTRATIVE`(pusty) |
| `courtName` | tekst | nazwa sadu |
| `judgmentTypes` | enum(wiele) | `DECISION` `RESOLUTION` `SENTENCE` `REGULATION` `REASONS` |
| `keywords` | tekst(wiele) | tagi tematyczne SAOS |
| `judgmentDateFrom` | data | `YYYY-MM-DD` |
| `judgmentDateTo` | data | `YYYY-MM-DD` |
| `ccCourtType` | enum | rodzaj sadu powszechnego: `APPEAL` `REGIONAL` `DISTRICT` |
| `ccCourtId` | int | id sadu powszechnego |
| `ccCourtCode` | tekst | kod sadu powszechnego |
| `ccDivisionId` | int | id wydzialu sadu powszechnego |
| `ccDivisionCode` | tekst | kod wydzialu |
| `ccIncludeDegree` | bool | uwzglednij sady nizszej instancji |
| `scCourtChamberId` | int | id izby Sadu Najwyzszego |
| `scCourtChamberName` | tekst | nazwa izby SN |
| `scCourtDivisionId` | int | id wydzialu SN |
| `scCourtDivisionsName` | tekst | nazwa wydzialu SN |
| `scPersonnelType` | enum | sklad orzekajacy SN |
| `pageSize` | int | **min 10, max 100**, domyslnie 20 |
| `pageNumber` | int | od 0 |
| `sortingField` | enum | `DATABASE_ID` `JUDGMENT_DATE` `JUDGMENT_TYPE` |
| `sortingDirection` | enum | `ASC` `DESC` |

### Odpowiedz

```json
{
  "links": [
    {"rel": "self", "href": "..."},
    {"rel": "next", "href": "..."},
    {"rel": "prev", "href": "..."}
  ],
  "items": [ /* skrocone obiekty orzeczen */ ],
  "info": {
    "totalResults": 3545,
    "pageSize": 10,
    "pageNumber": 0
  }
}
```

Skrocony obiekt orzeczenia w `items[]`: `id`, `href`, `courtType`, `courtCases`,
`judgmentType`, `judgmentDate`, `judges`, `textContent` (z tagami `<em>` wokol
trafien dla `all`), `keywords`, `division`.

---

## 2. Browse API

### `GET /api/judgments/{id}`

Zwraca `{"links": [...], "data": {...}}`. Pelny obiekt orzeczenia (`data`):

| Pole | Opis |
|---|---|
| `id` | id w bazie SAOS |
| `courtType` | typ sadu |
| `courtCases` | lista `{caseNumber}` - sygnatury |
| `judgmentType` | typ orzeczenia |
| `judgmentDate` | data orzeczenia (UWAGA: artefakty OCR) |
| `receiptDate` | data wplywu |
| `judges` | lista `{name, function, specialRoles}` |
| `courtReporters` | protokolanci |
| `source` | `{code, judgmentUrl, judgmentId, ...}` - link do oryginalu w portalu sadu |
| `decision` | sentencja |
| `summary` | streszczenie (czesto puste) |
| `textContent` | pelna tresc orzeczenia |
| `legalBases` | podstawy prawne (lista tekstow) |
| `referencedRegulations` | przywolane akty `{journalTitle, text}` |
| `referencedCourtCases` | przywolane sprawy |
| `keywords` | slowa kluczowe / tagi |
| `meansOfAppeal` | srodek zaskarzenia |
| `judgmentResult` | wynik |
| `lowerCourtJudgments` | orzeczenia sadow nizszych instancji |
| `division` | wydzial: `{id, name, code, court:{id, code, name}}` |

### Obiekty powiazane (pobierane pojedynczo po id)

- `GET /api/commonCourts/{id}` - sad powszechny
- `GET /api/ccDivisions/{id}` - wydzial sadu powszechnego
- `GET /api/scChambers/{id}` - izba Sadu Najwyzszego

> Listowanie zbiorcze (`/api/commonCourts` bez id) zwraca `404 PAGE DOES NOT
> EXIST`. Id sadu/wydzialu czytaj z pola `division` w wyniku orzeczenia.

---

## 3. Dump API - `GET /api/dump/judgments`

Hurtowe pobranie calej bazy + synchronizacja przyrostowa.

| Parametr | Opis |
|---|---|
| `pageSize` | min 10, max 100 |
| `pageNumber` | od 0 |
| `judgmentStartDate` | dolna granica daty orzeczenia |
| `judgmentEndDate` | gorna granica daty orzeczenia |
| `sinceModificationDate` | tylko rekordy zmienione po tej dacie (synchronizacja) |

Odpowiedz ma te same `links` / `items` / `info` co Search, plus `queryTemplate`.
Obiekty w dumpie sa pelne (jak Browse API).

Dump istnieje rowniez dla sadow: `GET /api/dump/courts` oraz `/api/dump/scChambers`
(w czasie testow `/api/dump/courts` zwracal blad - sprawdzic parametryzacje przy
realnym uzyciu).

**Wzorzec budowy lokalnego indeksu RODO-safe:**
1. Pierwszy zaciag: `pageNumber` 0..N po `pageSize=100` az `items` puste.
2. Zapis kazdego orzeczenia jako rekord lokalny (SQLite + vector store - patrz
   `knowledge-graph-law-firms`).
3. Synchronizacja: cyklicznie `sinceModificationDate=<data ostatniego zaciagu>`.

---

## Enumeracje

**courtType:** `COMMON`, `SUPREME`, `CONSTITUTIONAL_TRIBUNAL`,
`NATIONAL_APPEAL_CHAMBER`, `ADMINISTRATIVE` (pusty - brak danych).

**judgmentType:** `DECISION` (postanowienie), `RESOLUTION` (uchwala),
`SENTENCE` (wyrok), `REGULATION` (zarzadzenie), `REASONS` (uzasadnienie).

**ccCourtType** (sady powszechne): `APPEAL` (apelacyjny), `REGIONAL` (okregowy),
`DISTRICT` (rejonowy).

**source.code:** `COMMON_COURT`, `SUPREME_COURT`, `CONSTITUTIONAL_TRIBUNAL`,
`NATIONAL_APPEAL_CHAMBER` - skad SAOS pobral orzeczenie.

---

## Znane ograniczenia (zweryfikowane 2026-05-19)

- **Zakres** - SAOS zawiera orzecznictwo biezace (~17 tys. z 2024, ~14 tys.
  z 2025+, zweryfikowane na zywym API). Pokrycie nierowne wg typu sadu.
- **Brak sadow administracyjnych** - `courtType=ADMINISTRATIVE` zwraca pustke;
  brak merytorycznego orzecznictwa RODO (domena WSA/NSA).
- **Artefakty OCR** - bledy w tresci i datach (`3013-12-04`, `2101-04-14`).
  Sortowanie DESC po dacie wypycha takie rekordy na gore - filtruj
  `judgmentDateTo` data biezaca, by je odciac.
- **pageSize < 10** -> `400 WRONG REQUEST PARAMETER`.
- **Brak listowania sadow** - tylko dostep po id.
- **Brak operatorow boolowskich** w `all` - proste wyszukiwanie pelnotekstowe.

---

## Linki kanoniczne

| Cel | Wzorzec URL |
|---|---|
| Strona orzeczenia (czlowiek) | `https://www.saos.org.pl/judgments/{id}` |
| Surowy obiekt API | `https://www.saos.org.pl/api/judgments/{id}` |
| Oryginal w portalu sadu | pole `source.judgmentUrl` |
| Dokumentacja API | `https://www.saos.org.pl/help/index.php/dokumentacja-api` |

---

## Przyklad inline Python (bez zewnetrznych zaleznosci)

```python
import urllib.parse, urllib.request, json

def saos_search(**params):
    qs = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    url = f"https://www.saos.org.pl/api/search/judgments?{qs}"
    with urllib.request.urlopen(url, timeout=35) as r:
        return json.loads(r.read())

def saos_get(jid):
    url = f"https://www.saos.org.pl/api/judgments/{jid}"
    with urllib.request.urlopen(url, timeout=35) as r:
        return json.loads(r.read())["data"]

# Przyklady
res = saos_search(all="RODO", courtType="SUPREME", pageSize=10,
                  sortingField="JUDGMENT_DATE", sortingDirection="DESC",
                  judgmentDateTo="2026-05-27")
print(res["info"]["totalResults"])

j = saos_get(352475)
print(j["courtCases"][0]["caseNumber"], j["source"]["judgmentUrl"])
```

> Uzywaj `urllib` w bash_tool, NIE `web_fetch` - URL-e SAOS z zapytan programowych
> zostana odrzucone przez ograniczenia narzedzia `web_fetch`.
