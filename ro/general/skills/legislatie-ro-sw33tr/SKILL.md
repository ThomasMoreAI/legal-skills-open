---
name: legislatie-ro-sw33tr
title: 'Legislație RO: legislatie.just.ro'
description: Sursa implicită pentru ORICE întrebare despre legislația românească. Folosește-l înainte de a răspunde din memorie sau din căutare web. Găsește actul pe legislatie.just.ro (link, titlu, emitent, dată) și citește textul în FORMA CONSOLIDATĂ ÎN VIGOARE, cu data consolidării, notele de modificare și deciziile ÎCCJ/CCR de sub articol. Funcționează din orice mediu, pe o scară de rute (local, calculatorul utilizatorului, browser, API). Trigger pentru orice act normativ (Lege, OUG, OG, HG, Ordin, Decizie, Decret, Cod, Normă, Regulament), orice „art. X din …”, „ce prevede legea”, „e în vigoare?”, „a fost modificat/abrogat?”, „link către act”, „textul ordonanței”, „Monitorul Oficial”, „codul administrativ”, „codul muncii”, „OUG 57/2019”, „Legea 53/2003”, „HG 1336/2022”. Trigger și pentru redactarea de note, adrese, puncte de vedere sau observații care citează legislație.
author: sw33tr
author_url: https://github.com/sw33tr/claude-legislatie-ro/tree/main/skills/legislatie-ro
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: ro
practice: general
language: ro
sources:
- title: Browser
  path: references/browser.md
---

# Legislație RO: legislatie.just.ro

Acesta e drumul implicit pentru dreptul românesc. Nu cita din memorie, de pe agregatori
(lege5, avocatnet, PDF-uri instituționale) sau din rezultate web când portalul e accesibil
pe oricare dintre rutele de mai jos. Dacă totuși folosești altă sursă, spune asta explicit.

## Trei fapte despre portal

1. `DetaliiDocument/<id>` afișează **ultima consolidare** (dreptul în vigoare).
   `DetaliiDocumentAfis/<id>` afișează **forma publicată inițial**; diferența nu se vede din
   text, dar lipsesc tocmai articolele adăugate ulterior (ex. art. 485^1 din Codul administrativ).
2. Unele acte sunt doar „ambalajul” unui cod cu id propriu: Legea 53/2003 trimite la Codul
   muncii (309240). Scripturile și fragmentul JS urmează automat link-ul.
3. Portalul blochează unele rețele (IP-uri de datacenter, unele proxy-uri). Tipic, într-un mediu
   cloud (de ex. sandbox-ul de cod al Claude), **căutarea (API SOAP) merge, dar textul (https) nu**:
   serverul închide conexiunea. WebFetch e blocat la fel. Nu reîncerca și nu schimba user-agentul:
   treci la ruta următoare. De pe o conexiune obișnuită din România totul merge direct.

## Scripturi

`S="<directorul de bază al skill-ului>/scripts"`: folosește mereu calea absolută; scripturile rulează din orice director.
Necesită Python 3.6+ și doar biblioteca standard. Pe Windows, în loc de `python3` folosește `py -3` sau `python`.

- `legislatie_search.py`: căutare prin API + text în vigoare + articol. Importă `lj_core.py` din propriul director.
- `lj_core.py`: doar text în vigoare + articol după id. Folosește doar biblioteca standard și poate fi copiat oriunde.

```bash
python3 "$S/legislatie_search.py" "OUG 57/2019"                        # metadate (merge și din cloud)
python3 "$S/legislatie_search.py" "OUG 57/2019" --articol 485^1        # text în vigoare + articol
python3 "$S/legislatie_search.py" "Lege 53/2003" --grep "concediu de odihn"
python3 "$S/legislatie_search.py" --id 215925 --articol 56             # după id / link, fără căutare
python3 "$S/legislatie_search.py" --diagnostic                         # ce rută merge de aici
```

Antetul fiecărui text spune forma. Raportează-l mereu:

```
ACT:    id 215925 — https://legislatie.just.ro/Public/DetaliiDocument/215925
FORMA:  consolidată — Consolidarea din 12.09.2026
```

Coduri de ieșire: `0` ok · `2` niciun rezultat · `3` **ROUTE_BLOCKED**, treci la ruta următoare ·
`4` articol negăsit · `5` pagina fără text · `6` id greșit sau eroare de portal.

Nu afișa niciodată textul integral al unui act mare. Folosește `--articol`, `--grep` sau `grep` pe fișierul din cache.

## Scara de rute: încearcă în ordine

**Ruta 1: aici.** Rulează direct comanda. Merge oriunde există HTTPS către portal (de ex. Claude
Code pe calculatorul utilizatorului). Cu exit 3 treci la ruta 2. Căutarea poți s-o faci în
continuare aici, pentru că API-ul merge de obicei și din cloud. Dacă mesajul pomenește certificate
SSL lipsă, urmează indicația din mesaj (`pip install certifi`) și reîncearcă.

**Ruta 2: calculatorul utilizatorului.** Doar dacă ai un shell pe calculatorul lui, separat de
mediul curent. În Claude Cowork, asta înseamnă instrumentul `device_bash` și un folder conectat;
altfel sari la ruta 3. Pașii de mai jos sunt pentru Cowork:

1. Caută o instalare existentă (orice folder conectat):
   `D=$(dirname "$(ls $HOME/mnt/*/.legislatie-ro/lj_core.py 2>/dev/null | head -1)"); python3 "$D/lj_core.py" --version`
2. Dacă lipsește sau versiunea e mai mică decât `lj_core.VERSION` din `$S`, instaleaz-o: copiază ambele
   scripturi în directorul de output al sesiunii sub **nume versionate** (ex. `lj_core_6.1.0.py`), pentru că
   `device_commit_files` poate livra o încărcare anterioară cu același nume. Apoi fă commit în
   `<folder conectat>/.legislatie-ro/lj_core.py` și `…/legislatie_search.py`. Verifică cu `md5sum`.
   Spune-i utilizatorului, într-un rând, că ai creat folderul ascuns `.legislatie-ro`.
   Fără `device_commit_files`: scrie `lj_core.py` cu heredoc în `$HOME/.legislatie-ro/` (circa 13 KB).
3. Rulează acolo, de ex. `python3 "$D/legislatie_search.py" "Lege 53/2003" --articol 39`
   sau `python3 "$D/lj_core.py" 41625 --articol 39`.

Fără folder conectat, `device_bash` nu pornește; treci la ruta 3.

**Ruta 3: browser.** Folosește Claude in Chrome sau browserul integrat al aplicației. Citește
[references/browser.md](references/browser.md): deschizi `DetaliiDocument/<id>`, rulezi fragmentul
JS și citești articolul pe bucăți de ~700 de caractere.

**Ruta 4: text din API (`--api-text`).** Merge oriunde merge căutarea, dar dă **forma publicată
inițial**, marcată ca atare în antet. E acceptabilă doar pentru acte recente, nemodificate, sau
când întrebarea privește chiar forma inițială. Spune-i utilizatorului că nu e forma consolidată.

**Ruta 5: fără instrumente.** Dă link-ul `https://legislatie.just.ro/Public/DetaliiDocument/<id>`
și răspunde marcând clar că textul nu a fost verificat pe portal.

## Înainte de a cita

- Citează din forma în vigoare și menționează data consolidării („în forma consolidată la 12.09.2026”).
  Link-ul de citat e `DetaliiDocument/<id de bază>`, care arată mereu ultima formă.
- Citește blocurile `Notă` de sub articol: actul modificator și data, deciziile ÎCCJ (RIL, HP) și CCR,
  dispozițiile tranzitorii. Un articol neschimbat ca text poate fi reinterpretat obligatoriu.
- `FORMA: publicată — portalul nu listează consolidări` înseamnă fie act nemodificat, fie consolidare
  încă nepublicată. Pentru acte foarte recente sau modificate recent, verifică actele modificatoare.
- `ATENȚIE: Posibil abrogat`: verifică notele de la începutul textului înainte să aplici actul.
- Pentru forma dintr-o dată trecută, ia id-ul consolidării din istoric și rulează `--id <id> --exact`.

## Căutare: particularități

- Formate acceptate: `OUG 57/2019`, `OG 15/2025`, `Lege 53/2003`, `Legea nr. 53/2003`, `HG 1336/2022`,
  `Ordin 123/2024`, `Decizie N/AAAA`, `Decret N/AAAA`, sau text liber: `--text "codul administrativ"`.
- API-ul ignoră anul și dă câte 10 rezultate pe pagină. Scriptul paginează (`--pagini`) și filtrează local.
- Pentru HG, OUG și OG se preferă automat emitentul Guvernul. Filtru strict: `--emitent "Senatul"`.
- Anexele actelor mari (regulamente, norme, metodologii) au adesea id propriu, deseori imediat
  următor actului de aprobare. Caută-le cu `--text "REGULAMENT de organizare …"`.
