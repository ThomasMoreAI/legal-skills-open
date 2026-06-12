---
name: citing-polish-law
title: citing-polish-law
description: Use when formatting citations to Polish legislation, court rulings, Constitutional Tribunal decisions, EU law, or international human rights judgments in legal memos, briefs, or analytical notes — requiring consistent format with article/paragraph/point, act name, redaction date, and source URL
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/skills/pl/law-pl-citing-polish-law
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: general
language: pl
---

# citing-polish-law

Standardowy format cytowania czyni stanowiska prawne weryfikowalnymi, czytelnymi i odtwarzalnymi.

## Odesłanie do aktu normatywnego

**Pierwsze (pełne) przywołanie**:
```
art. 117 § 1 ustawy z dnia 23 kwietnia 1964 r. — Kodeks cywilny
(Dz.U. 1964 nr 16 poz. 93, t.j. Dz.U. 2024 poz. ___)
```

**Powtórne w tym samym dokumencie**:
```
art. 117 § 1 KC
```

**Cytat dosłowny** (obowiązkowo w cudzysłowie):
```
„Roszczenia majątkowe ulegają przedawnieniu, z zastrzeżeniem wyjątków
przewidzianych w ustawie."
(art. 117 § 1 KC, brzmienie obowiązujące od dd.mm.rrrr).
```

## Hierarchia jednostek redakcyjnych

Polskie akty prawne mają strukturę jednostek redakcyjnych w określonej hierarchii:

Od najwyższej do najniższej:
- **część** (część pierwsza, druga…)
- **księga** (księga pierwsza…)
- **tytuł** (tytuł I, II…)
- **dział** (dział I, II…)
- **rozdział**
- **oddział**
- **artykuł** (art.)
- **paragraf** (§) — w niektórych aktach (KC, KPC, KPA — tak; w innych ustawach — często ust.)
- **ustęp** (ust.) — w wielu ustawach zamiast §
- **punkt** (pkt)
- **litera** (lit.)
- **tiret** (—)

**Przykład złożony**: `art. 22 § 1 pkt 3 lit. b KC`.

**Uwaga na różnicę KC/KPC vs ustawy szczególne**:
- KC, KPC, KPA — używają § (paragraf).
- Większość ustaw szczególnych — używa ust. (ustęp).
- Przykład: `art. 6 ust. 1 pkt 3 RODO` (rozporządzenie UE — używa ust. po polsku).

## Kolejność elementów w odesłaniu

Polska konwencja: **od najmniejszej do większej**:
- pkt → ust. (lub §) → art.

**Przykład**: `lit. b pkt 3 ust. 1 art. 22 KC`.

W praktyce częściej spotyka się porządek odwrotny (zaczynający od artykułu) i jest dopuszczalny.

## Skróty kodeksów i ustaw

| Pełna nazwa | Skrót |
|---|---|
| Konstytucja Rzeczypospolitej Polskiej | Konstytucja RP |
| Kodeks cywilny | KC |
| Kodeks postępowania cywilnego | KPC |
| Kodeks postępowania administracyjnego | KPA |
| Prawo o postępowaniu przed sądami administracyjnymi | PPSA |
| Kodeks karny | KK |
| Kodeks postępowania karnego | KPK |
| Kodeks wykroczeń | KW |
| Kodeks postępowania w sprawach o wykroczenia | KPW |
| Kodeks pracy | KP |
| Kodeks rodzinny i opiekuńczy | KRO |
| Kodeks spółek handlowych | KSH |
| Kodeks karny wykonawczy | KKW |
| Ordynacja podatkowa | OrdU / o.p. |
| Prawo o adwokaturze | PoA |
| Ustawa o radcach prawnych | URP |
| Ustawa o dostępie do informacji publicznej | UDIP |
| Ustawa o kosztach sądowych w sprawach cywilnych | UKSC |
| Ustawa o komornikach sądowych | UKomS |
| Ustawa o ochronie danych osobowych | UODO |
| Rozporządzenie UE 2016/679 (RODO) | RODO |
| Prawo bankowe | PB |
| Prawo upadłościowe | PU |
| Prawo restrukturyzacyjne | PR |

Ustawy nazywać pełną oficjalną nazwą za pierwszym razem; dalej — skrót w nawiasie przy pierwszym przywołaniu: *ustawa z dnia 6 września 2001 r. o dostępie do informacji publicznej (dalej: UDIP)*.

## Cytowanie publikatora

**Format**: `Dz.U. {rok} nr {nr_dz_u} poz. {pozycja}` (dla starszych aktów) lub `Dz.U. {rok} poz. {pozycja}` (od 2012 r. — bez numeru dziennika).

**Tekst jednolity**: dodać `t.j. Dz.U. {rok} poz. {pozycja}` — wskazuje konsolidację po wszystkich zmianach do określonej daty.

**Z późniejszymi zmianami**: `z późn. zm.` — informuje, że po publikacji były nowelizacje.

**Przykład pełny**:
```
ustawa z dnia 23 kwietnia 1964 r. — Kodeks cywilny
(Dz.U. 1964 nr 16 poz. 93, t.j. Dz.U. 2024 poz. ___ z późn. zm.)
```

## Orzecznictwo

### Wyrok Sądu Najwyższego

```
Wyrok Sądu Najwyższego z dnia 15.03.2023 r., sygn. I CSK 123/22
(opubl. www.sn.pl, OSNC 2023/4/45).
```

### Uchwała SN (z mocą zasady prawnej)

```
Uchwała Sądu Najwyższego (skład 7 sędziów) z dnia 15.03.2023 r.,
sygn. III CZP 12/22 (OSNC 2023/5/56).
```

### Wyrok / postanowienie Trybunału Konstytucyjnego

```
Wyrok Trybunału Konstytucyjnego z dnia 15.03.2023 r.,
sygn. K 12/22 (OTK Seria A 2023/3/45, Dz.U. 2023 poz. ___).
```

### Wyrok Naczelnego Sądu Administracyjnego

```
Wyrok NSA z dnia 15.03.2023 r., sygn. II OSK 567/22 (CBOSA).
```

### Wyrok wojewódzkiego sądu administracyjnego

```
Wyrok WSA w Warszawie z dnia 15.03.2023 r., sygn. II SA/Wa 1234/22 (CBOSA).
```

### Wyrok TSUE

```
Wyrok TSUE z dnia 15.03.2023 r., C-123/22, ECLI:EU:C:2023:123,
[Strony postępowania].
```

### Wyrok ETPCz

```
Wyrok ETPCz z dnia 15.03.2023 r., skarga nr 12345/20,
[Strony] przeciwko Polsce.
```

### Postanowienie / wyrok sądu powszechnego

```
Wyrok Sądu Apelacyjnego w Warszawie z dnia 15.03.2023 r.,
sygn. I ACa 567/22 (Portal Orzeczeń SP).
```

## Cytowanie aktów UE

### Rozporządzenie

```
Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia
2016 r. w sprawie ochrony osób fizycznych w związku z przetwarzaniem danych
osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy
95/46/WE (ogólne rozporządzenie o ochronie danych) — RODO
(Dz.Urz. UE L 119 z 04.05.2016, s. 1).
```

### Dyrektywa

```
Dyrektywa Parlamentu Europejskiego i Rady 2011/83/UE z dnia 25 października 2011 r.
w sprawie praw konsumentów (Dz.Urz. UE L 304 z 22.11.2011, s. 64).
```

### Traktat

```
Traktat o funkcjonowaniu Unii Europejskiej (TFUE) — wersja skonsolidowana
(Dz.Urz. UE C 202 z 07.06.2016).
```

## Cytowanie aktów wewnętrznych i wytycznych

### Rozporządzenie ministra

```
Rozporządzenie Ministra Sprawiedliwości z dnia [data] r. w sprawie [tytuł]
(Dz.U. {rok} poz. {pozycja}).
```

### Obwieszczenie

```
Obwieszczenie Prezesa Rady Ministrów z dnia [data] r. w sprawie ogłoszenia
jednolitego tekstu ustawy [...] (Dz.U. {rok} poz. {pozycja}).
```

### Uchwała Sejmu / Senatu

```
Uchwała Sejmu RP z dnia [data] r. w sprawie [...] (M.P. {rok} poz. {pozycja}).
```

## Najczęstsze błędy

- **Odesłanie bez brzmienia.** Norma mogła się zmieniać — cytat bez daty brzmienia jest niepewny.
- **Mylenie § z ust.** KC, KPC, KPA — § (paragraf). Większość pozostałych ustaw — ust. (ustęp). Mylenie sygnalizuje brak weryfikacji.
- **Niepełna sygnatura akt SN.** Sygnatura SN ma 4 elementy: izba (litera), tryb (litera), numer, rok — np. `III CZP 12/22`. Bez izby — nieprecyzyjne.
- **Brak symbolu ECLI w wyrokach TSUE.** Standardowy identyfikator europejskiego orzecznictwa — ECLI:EU:C:rok:numer.
- **Cytowanie niepublikowanych orzeczeń jako autorytetów.** Wyroki sądów powszechnych dostępne w Portalu Orzeczeń mogą być uzasadnieniem, ale nie tworzą wiążącej linii orzeczniczej.
- **Mylenie zbiorów urzędowych.** OSNC (Cywilna), OSNK (Karna), OSNP (Pracy), OTK (Trybunału Konstytucyjnego), ONSAiWSA (sądów administracyjnych).
- **Brak wskazania, że uchwała ma moc zasady prawnej.** Wskazać skład: pełnoskładowa / izba / 7 sędziów / 3 sędziów.
- **„Według literatury…" bez konkretu.** Komentarze są pomocne (np. komentarz do KC pod red. K. Pietrzykowskiego, komentarz do KPC pod red. T. Erecińskiego), ale wymagają oznaczenia: autor, tytuł, wydanie, miejsce, rok, strona.
- **Mylenie aktów wewnętrznych z ustawami.** Uchwały Sejmu / Senatu — Monitor Polski (M.P.); ustawy — Dziennik Ustaw (Dz.U.).
- **Nieaktualny tekst jednolity.** Po obwieszczeniu o tekście jednolitym mogły być dalsze nowelizacje — sprawdzać.
