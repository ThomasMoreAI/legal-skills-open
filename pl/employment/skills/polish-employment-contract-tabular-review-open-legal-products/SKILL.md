---
name: polish-employment-contract-tabular-review-open-legal-products
title: Przegląd tabelaryczny polskich umów o pracę
description: Use this workflow to review Polish employment contracts (umowa o pracę) under the Labour Code (Kodeks pracy, Act of 26 June 1974) and extract structured information into the tabular review columns defined in table-columns.yaml.
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/tabular-review-workflows/polish-law-pack/polish-employment-contract-tabular-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: employment
language: en
---

# Przegląd tabelaryczny polskich umów o pracę

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Wskazówki przeglądu

- Umowy o pracę podlegają Kodeksowi pracy (ustawa z dnia 26 czerwca 1974 r.). Kodeks chroni jednostronnie: pracownika. Postanowienie mniej dla niego korzystne niż przepis prawa pracy jest nieważne, a w jego miejsce wchodzi ten przepis (art. 18 § 1 i § 2 k.p.). Odnotowuj takie postanowienia. O nieważności nie przesądzaj - to ocena prawnika.
- Dyscyplina źródłowa: każda komórka wskazuje jednostkę redakcyjną umowy, z której pochodzi wartość (np. "§ 4 ust. 2", "załącznik nr 1"). Jeśli umowa milczy w danej sprawie, wpisz "Nie wskazano" - nie zostawiaj komórki pustej i nie uzupełniaj jej regułą ustawową bez oznaczenia. Gdy podajesz regułę ustawową, oddziel ją wyraźnie od treści umowy (np. "Nie wskazano - reguła ustawowa: ...").
- Postanowienia sporne cytuj dosłownie, zwłaszcza zakaz konkurencji, podstawę zawarcia umowy terminowej i klauzule o jednostronnej zmianie warunków. Nie parafrazuj miejsc niejednoznacznych.
- Strony identyfikuj w polskiej konwencji: pełna firma pracodawcy z formą prawną (sp. z o.o., S.A.) oraz numer KRS lub NIP. Przy pracowniku wyłącznie dane wskazane w umowie. Nic ponadto.
- Sygnały ryzyka warte odnotowania: umowa na czas określony bez podstawy przy przekroczeniu limitu z art. 25[1] k.p., zakaz konkurencji po ustaniu zatrudnienia bez odszkodowania albo poniżej ustawowego minimum (art. 101[2] § 3 k.p.), skrócenie okresu wypowiedzenia poniżej art. 36 k.p. na niekorzyść pracownika, wynagrodzenie poniżej minimalnego, jednostronne prawo pracodawcy do zmiany warunków bez wypowiedzenia zmieniającego.
- Odwołania do przepisów, których nie potwierdzasz w treści dokumentu ani we własnej wiedzy, oznaczaj jako [do weryfikacji]. Tabela pokazuje, co w umowach zapisano. Czy postanowienie jest ważne i skuteczne, rozstrzyga prawnik w odrębnej analizie - wynik tego przeglądu jest roboczym zestawieniem do sprawdzenia przez człowieka, nie poradą prawną.
