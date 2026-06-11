---
name: determining-pl-request-regime
title: determining-pl-request-regime
description: "Use when choosing the Polish legal regime for letters, requests, applications, complaints, petitions, public-information requests, KPA filings, PPSA complaints, RODO access requests, registry extracts, court-file access, tax/ZUS/cudzoziemcy/USC procedures, or professional lawyer letters. Prevents mixing UDIP, KPA, PPSA, RODO, registry, special-procedure, and advocate/radca letter regimes."
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/plugins/pl/skills/determining-pl-request-regime
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: pl
---

# determining-pl-request-regime

Ten skill ustala, w jakim trybie prawnym przygotować pismo do organu, sądu, urzędu, rejestru, administratora danych, ZUS, KAS, USC, urzędu wojewódzkiego albo innego adresata. Obejmuje także akta sądowe, rejestry publiczne i pismo adwokata / radcy.

## Główna zasada

**jedno pismo = jeden tryb prawny**.

Nie łącz w jednym piśmie UDIP, skargi z KPA, petycji, żądania z RODO, dostępu do akt, wniosku rejestrowego i groźby skargi do WSA tylko po to, żeby tekst wyglądał mocniej. Mieszanie trybów pozwala adresatowi rozpoznać pismo w wolniejszym albo niewłaściwym trybie.

## Styl po wyborze trybu

Prawidłowy tryb nie jest powodem do przeładowania pisma. Po wyborze trybu odzwierciedlaj go minimum: tytułem pisma, kluczową podstawą prawną i konkretnymi punktami żądania.

Nie dodawaj defensywnych, pouczających ani grożących zdań tylko po to, żeby adresatowi trudniej było pominąć wybrany tryb. Jeżeli potrzebna jest skarga, odpowiedzialność urzędnika albo sądowa kontrola bezczynności, to jest osobne następne pismo po odpowiedzi, odmowie albo upływie terminu.

Jeżeli użytkownik chce jednocześnie ustalić fakty, uzyskać kopie, złożyć skargę, żądać kary i wszcząć sprawę administracyjną, podziel pracę na etapy:

1. Najpierw ustal fakty, status sprawy, daty wpływu, znaki sprawy i dokumenty.
2. Następnie, po odpowiedzi, odmowie albo bezczynności, przygotuj skargę, ponaglenie, odwołanie lub skargę do WSA.

## Szybki router

| Sytuacja | Tryb | Podstawa | Typowy termin |
|---|---|---|---|
| Osoba chce istniejącej informacji o sprawach publicznych od podmiotu zobowiązanego, a nie jest to dostęp strony do akt ani specjalny rejestr | **Wniosek o udostępnienie informacji publicznej** | UDIP art. 1, 2, 4, 6, 10, 13 | bez zbędnej zwłoki, nie później niż 14 dni; przedłużenie do 2 miesięcy |
| Osoba chce wszcząć albo załatwić indywidualną sprawę administracyjną | **Podanie / wniosek w indywidualnej sprawie administracyjnej** | art. 63 KPA + ustawa szczególna | termin z ustawy szczególnej albo KPA |
| Strona postępowania administracyjnego chce wglądu w akta, kopii, odpisów albo uwierzytelnienia | **Dostęp strony do akt administracyjnych** | art. 73 KPA, art. 74 KPA | bez zbędnej zwłoki w toku sprawy |
| Osoba chce urzędowego potwierdzenia faktu albo stanu prawnego | **Zaświadczenie** | art. 217-220 KPA | bez zbędnej zwłoki, nie później niż 7 dni |
| Osoba skarży działalność organu lub urzędnika poza odwołaniem od decyzji | **Skarga z działu VIII KPA** | art. 227 KPA, art. 237 KPA | zwykle miesiąc |
| Osoba proponuje usprawnienie, zapobieganie nadużyciom albo wzmocnienie praworządności | **Wniosek z działu VIII KPA** | art. 241 KPA, art. 244 KPA | zwykle miesiąc |
| Osoba żąda działania w interesie publicznym, zmiany prawa, polityki lub praktyki organu | **Petycja** | ustawa o petycjach | bez zbędnej zwłoki, nie później niż 3 miesiące |
| Osoba skarży decyzję administracyjną, postanowienie, bezczynność albo przewlekłość do sądu administracyjnego | **Skarga do WSA / PPSA** | PPSA art. 3, 50, 52-54 | zwykle 30 dni od doręczenia aktu albo po wyczerpaniu środków zaskarżenia |
| Strona albo pełnomocnik chce akta sprawy sądowej | **Dostęp do akt sądowych** | KPC art. 9, KPK art. 156, PPSA i regulaminy sądowe | według procedury sądu |
| Osoba wykonuje prawa do własnych danych osobowych | **Żądanie z RODO** | RODO art. 12, 15-22; UODO | zwykle 1 miesiąc |
| Osoba chce odpis, wyciąg, zaświadczenie lub informację z rejestru | **Rejestr publiczny / ewidencja** | przepisy KRS, KW/EKW, CEIDG, REGON, PESEL, ASC albo innego rejestru | termin rejestru albo e-usługi |
| Sprawa dotyczy podatków, interpretacji, zaświadczeń podatkowych, ulg, kontroli, odwołania albo KAS | **Procedura podatkowa** | Ordynacja podatkowa i ustawy podatkowe | termin z OP albo ustawy szczególnej |
| Sprawa dotyczy składek, świadczeń, ulg, decyzji albo odwołania od ZUS | **Procedura ZUS** | ustawy ubezpieczeniowe, KPA tylko pomocniczo, KPC dla odwołań | termin z procedury ZUS |
| Sprawa dotyczy pobytu, pracy, zaproszeń, obywatelstwa albo UdSC | **Procedura cudzoziemców** | ustawa o cudzoziemcach i przepisy szczególne | termin z ustawy szczególnej |
| Sprawa dotyczy aktów stanu cywilnego, transkrypcji, odpisów, imienia, nazwiska albo małżeństwa | **Procedura USC / ASC** | Prawo o aktach stanu cywilnego i KPA | termin z procedury USC |
| Pismo wysyła adwokat albo radca prawny dla klienta | **Pismo adwokata / radcy prawnego** | konkretna podstawa materialna albo procesowa; nie jest ukraińskim adwokatskim zapytem | termin z podstawy żądania albo wyznaczony rozsądnie |

## Jak wybrać tryb

1. Ustal, czy użytkownik chce informacji już istniejącej, nowego rozstrzygnięcia, dostępu do akt, zaświadczenia, danych osobowych, wpisu/odpisu z rejestru, skargi, petycji albo specjalnej procedury.
2. Ustal status użytkownika: każda osoba, strona postępowania, pełnomocnik, adwokat/radca, podmiot danych, podatnik, ubezpieczony, cudzoziemiec, wnioskodawca w USC.
3. Ustal adresata: podmiot zobowiązany z UDIP, organ administracji, sąd, administrator danych, rejestr, KAS/US, ZUS, wojewoda, Szef UdSC, USC, podmiot prywatny.
4. Wybierz jeden tryb i nazwij go wprost.
5. Jeżeli cele są mieszane, zaproponuj osobne pisma albo kolejność działań.

Jeżeli tryb pozostaje niejasny, zadaj jedno krótkie pytanie: kto składa pismo, czego dokładnie chce, czy istnieje konkretna sprawa/decyzja/akta, kto jest adresatem i czy użytkownik działa jako strona postępowania.

## Typowe markery

| Sformułowanie użytkownika | Wybierz |
|---|---|
| „czy urząd otrzymał”, „data wpływu”, „znak sprawy”, „kopię pisma”, „status dokumentu” | UDIP, jeżeli chodzi o sprawy publiczne i brak statusu strony; art. 73 KPA albo podanie KPA, jeżeli chodzi o własną sprawę administracyjną |
| „jestem stroną postępowania, chcę akta” | art. 73 KPA |
| „proszę wydać zaświadczenie” | art. 217-220 KPA |
| „chcę złożyć wniosek o wydanie decyzji/zezwolenia” | art. 63 KPA + ustawa szczególna |
| „urzędnik źle działa”, „skarga na pracownika”, „organ mnie ignoruje” | skarga z art. 227 KPA albo ponaglenie/skarga PPSA, zależnie od sprawy i etapu |
| „zmieńcie przepisy”, „podjęcie działań w interesie publicznym” | petycja |
| „decyzja jest niezgodna z prawem”, „skarga do WSA”, „bezczynność organu” | PPSA, zwykle po wyczerpaniu właściwych środków |
| „jakie moje dane przetwarzacie”, „usuńcie moje dane”, „sprostujcie dane” | RODO |
| „odpis KRS”, „wydruk KW”, „zaświadczenie CEIDG”, „odpis aktu urodzenia” | rejestr albo procedura USC, nie UDIP |
| „ulga podatkowa”, „interpretacja indywidualna”, „zaświadczenie o niezaleganiu” | procedura podatkowa |
| „świadczenie ZUS”, „decyzja ZUS”, „PUE ZUS” | procedura ZUS |
| „karta pobytu”, „zezwolenie na pracę”, „UdSC” | procedura cudzoziemców |

## Czego nie robić

- Nie nazywaj wniosku o informację publiczną petycją, skargą ani podaniem z KPA.
- Nie dodawaj do UDIP żądania ukarania urzędnika, ogólnej skargi ani groźby odpowiedzialności karnej jako elementu głównego żądania.
- Nie używaj UDIP do dostępu strony do akt administracyjnych, gdy właściwy jest art. 73 KPA.
- Nie używaj UDIP jako obejścia specjalnego rejestru, jeżeli ustawa przewiduje odpis, wyciąg, zaświadczenie albo e-usługę.
- Nie twórz polskiego „adwokackiego zapytania” na wzór ukraiński. Pismo adwokata / radcy musi mieć konkretną podstawę: umowę, przepis materialny, postępowanie sądowe, wniosek dowodowy, UDIP albo inną procedurę.
- Nie składaj skargi do WSA, zanim ustalisz etap sprawy, doręczenie aktu, bezczynność, przewlekłość i wyczerpanie środków zaskarżenia.

## Handoff do innych agentów i skilli

- Do sporządzenia pisma po wyborze trybu użyj `request-drafter`.
- Dla podatków użyj `applying-skarbowy-procedures`.
- Dla ZUS użyj `applying-zus-procedures`.
- Dla cudzoziemców użyj `applying-cudzoziemcy-procedures`.
- Dla USC użyj `applying-usc-procedures`.
- Dla RODO użyj `applying-rodo` albo `rodo-compliance`.
- Dla skargi do WSA, apelacji, zażalenia, skargi kasacyjnej albo środka sądowego użyj `appeal-drafter` lub `claim-drafter`, zależnie od rodzaju sprawy.
- Dla dokładnych cytatów ustaw użyj `fetching-isap-sejm` i `citing-polish-law`.
