---
name: saos-orzecznictwo-matematicsolutions
title: SAOS - Polish Case Law Search
description: Search and retrieve Polish court judgments via the SAOS REST API (System Analizy Orzeczen Sadowych, Fundacja ePanstwo). Use this skill whenever the user wants to find Polish case law - orzeczenia, wyroki, postanowienia - from sady powszechne, Sad Najwyzszy, Trybunal Konstytucyjny or Krajowa Izba Odwolawcza; search by case number (sygnatura), date range, court, judge, keyword, legal basis or referenced regulation; fetch full judgment text; or bulk-download the judgment corpus. Also trigger on "orzecznictwo PL", "SAOS", "szukaj wyroku", "sygnatura akt", "baza orzeczen". Companion to eu-sparql-search (which covers EU law / CJEU).
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-pl/tree/main/orzecznictwo-zrodla/skills/saos-orzecznictwo
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: contracts
language: pt
sources:
- title: Api
  path: references/api.md
---

# SAOS - Polish Case Law Search

Polski konektor orzecznictwa dla projektu legal AI MateMatic. Komplementarny do
`eu-sparql-search` (CJEU / prawo UE): SAOS pokrywa sady krajowe RP.

## Endpoint

```
https://www.saos.org.pl/api
```

Publiczne, otwarte REST API. **Bez klucza, bez autoryzacji.** Zwraca JSON.

API ma trzy czesci:

| Czesc | Sciezka | Do czego |
|---|---|---|
| **Search API** | `/api/search/judgments` | przeszukiwanie wg kryteriow, zwraca skroty + `textContent` |
| **Browse API** | `/api/judgments/{id}` | pelny obiekt pojedynczego orzeczenia |
| **Dump API** | `/api/dump/judgments` | hurtowe pobranie calej bazy + synchronizacja |

Pelna referencja parametrow, pol odpowiedzi i enumeracji → [references/api.md](references/api.md)

## Zakres bazy (co SAOS faktycznie indeksuje)

| courtType | Sad | Status |
|---|---|---|
| `COMMON` | sady powszechne (rejonowe, okregowe, apelacyjne) | pelny |
| `SUPREME` | Sad Najwyzszy | pelny |
| `CONSTITUTIONAL_TRIBUNAL` | Trybunal Konstytucyjny | pelny |
| `NATIONAL_APPEAL_CHAMBER` | Krajowa Izba Odwolawcza (zamowienia publiczne) | pelny |
| `ADMINISTRATIVE` | sady administracyjne (WSA/NSA) | **PUSTY** - uzyj orzeczenia.nsa.gov.pl |

> ⚠️ **Zakres SAOS (zweryfikowane na zywym API 2026-05-19).** SAOS zawiera
> orzecznictwo biezace (~17 tys. z 2024, ~14 tys. z 2025+). Pokrycie nierowne
> wg typu sadu. Realne ograniczenia: brak WSA/NSA i artefakty OCR w datach.

## Jak wykonywac zapytania

### Metoda preferowana: helper Python

Skrypt `scripts/saos.py` w tym skillu owija API. Z bash_tool:

```bash
python ~/.claude/skills/saos-orzecznictwo/scripts/saos.py search \
  --all "RODO" --court SUPREME --from 2023-01-01 --size 10
python ~/.claude/skills/saos-orzecznictwo/scripts/saos.py get 352475
python ~/.claude/skills/saos-orzecznictwo/scripts/saos.py case "I ACa 772/13"
```

Przyklad inline Python bez zaleznosci → [references/api.md](references/api.md#przyklad-inline-python)

> **WAZNE:** Uzywaj `urllib` w bash_tool, NIE `web_fetch` - URL-e SAOS z zapytan
> programowych beda odrzucone przez ograniczenia narzedzia `web_fetch`.

## Workflow

1. **Ustal intencje** - czego szuka uzytkownik: sygnatura, temat, sad, sedzia, data?
2. **Zmapuj na parametry** Search API - patrz [references/api.md](references/api.md).
   Sygnatura → `caseNumber`; temat → `all` lub `keywords`; akt → `referencedRegulation`.
3. **Wykonaj** przez `scripts/saos.py` lub inline Python. Zacznij `pageSize=10`.
4. **Pokaz wyniki** jako czytelna tabela: sygnatura, sad, data, typ, fragment.
5. **Pobierz pelna tresc** przez Browse API, gdy uzytkownik chce konkretne orzeczenie.
6. **ZAWSZE cytuj zrodlo** - klikalny link (sekcja nizej).
7. **Zaproponuj dalej** - kolejna strona, szerszy zakres dat, inny sad, dump lokalny.

## Cytowania - zawsze weryfikowalny link

Kazda odpowiedz oparta na tresci orzeczenia MUSI konczyc sie zrodlem. Bez tego
uzytkownik nie odroznia realnego cytatu od halucynacji.

Format bloku zrodla na koncu odpowiedzi:

```
**Zrodlo:** Sad Apelacyjny w Lodzi, wyrok z 4.12.2013, sygn. I ACa 772/13
- SAOS: https://www.saos.org.pl/judgments/31345
- Oryginal sadu: http://api.orzeczenia.wroclaw.sa.gov.pl/...
```

## Reguly i pulapki

- API jest **publiczne, bez auth**. Nie wymyslaj kluczy.
- `pageSize` ma **twardy dolny limit 10** (`400 WRONG REQUEST PARAMETER` dla < 10).
  Nie da sie pobrac 1 wyniku - bierz 10 i tnij.
- `courtType=ADMINISTRATIVE` zwraca **pustke**. Dla WSA/NSA odeslij do `orzeczenia.nsa.gov.pl`.
- **Artefakty OCR** w datach (`judgmentDate:"3013-12-04"`, `"2101-04-14"`).
  Sortowanie DESC wypycha te rekordy na gore. Filtruj jawnie `judgmentDateTo=<dzis>`.
- **`textContent` zawiera znaczniki HTML** (`<p>`, `<em>` wokol trafien). Zdejmij
  znaczniki przed cytowaniem (`html.parser` / regex).
- API **nie ma operatorow boolowskich** w `all` - proste wyszukiwanie pelnotekstowe.
  Zlozone zapytania rozbijaj na kilka wywolan.
- **Brak listowania sadow** (`/api/commonCourts` bez id → `404`). Id sadu bierz
  z pola `division` w wynikach orzeczen.
- Wartosci tekstowe parametrow URL-encoduj (`urllib.parse.urlencode` robi to sam).

## Miejsce w architekturze

Ten skill to warstwa **live query** dla SAOS. Komplementarny do:

- **`legal-data-hunter-pl`** - warstwa harvestu/katalogu. Uzywa tylko Dump API
  (hurtowe archiwum do lokalnego korpusu RODO-safe).
- **`eu-sparql-search`** - prawo UE / orzecznictwo CJEU.

Realna luka: orzecznictwo sadow administracyjnych (WSA/NSA) - SAOS nie indeksuje.
Potrzebny osobny konektor do `orzeczenia.nsa.gov.pl`.

## Historia zmian

- **2026-05-19** - korekta zakresu. Stare ustalenie "SAOS to archiwum historyczne
  zatrzymane ~2018" BLEDNE. Weryfikacja na zywym API: 17k orzeczen z 2024, 14k z 2025+.
  Realne ograniczenia to brak WSA/NSA i artefakty OCR w datach. Ten sam blad
  poprawiony rownolegle w serwerze MCP `mcp-saos` (6 disclaimerow + filtr judgmentDateTo).
