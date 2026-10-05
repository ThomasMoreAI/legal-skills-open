# collaudo-verifica-conformita-dlgs36

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con RUP / collaudatore / esperto di contratti pubblici da completare)

Skill di **supporto documentale** al **collaudo dei lavori** e alla **verifica di
conformità** di servizi e forniture nei contratti pubblici, secondo il **D.Lgs.
36/2023, art. 116**.

**Non redige** il certificato di collaudo/CRE, **non riproduce** l'allegato II.14, **non
nomina** i collaudatori e **non sostituisce** la stazione appaltante, il RUP o l'organo
di collaudo: inquadra funzione, termini, collaudatori e incompatibilità.

## Target

Ingegneri/architetti (RUP, collaudatori, direttori dei lavori/esecuzione), stazioni
appaltanti e operatori economici.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-collaudo-termini` | Distingue collaudo/verifica di conformità e ricostruisce i termini e la natura del certificato (provvisorio/definitivo), con la responsabilità dell'appaltatore (art. 116 cc. 1-3, 7) |
| `verifica-collaudatori-incompatibilita` | Inquadra la nomina dei collaudatori/verificatori (numero, requisiti) e i casi di incompatibilità (art. 116 cc. 4-6) |

Nucleo: **funzione** collaudo/verifica (c. 1); **termini** 6 mesi/1 anno e certificato
provvisorio→definitivo a 2 anni (c. 2); **responsabilità appaltatore** (c. 3);
**collaudatori** 1-3 e **incompatibilità** (cc. 4-6); **RUP/DEC** (c. 5); rinvio
all'**allegato II.14** per il **CRE** (c. 7).

## Fonti consultate

- **D.Lgs. 31/3/2023 n. 36** (Codice dei contratti pubblici) - art. 116 - testo vigente
  su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 23G00044)
- **L. 7 agosto 2026, n. 152** (conversione del D.L. 26 giugno 2026, n. 107) - **art.
  1-bis**, sospensione temporanea del recupero dell'anticipazione nei lavori pubblici,
  e testo dell'**art. 125 D.Lgs. 36/2023** riportato nei "Riferimenti normativi" - GU
  Serie generale n. 192 del 20/8/2026 (codice 26G00165). **Deroga a termine: scade il
  31 dicembre 2026**; esclusi gli interventi finanziati anche solo in parte con
  risorse PNRR.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** il **certificato di collaudo/verifica** né il **CRE**.
- **Non riproduce** l'**allegato II.14** (modalità tecniche, tempi, CRE, compensi) né
  l'**allegato II.15** (costi accertamenti di laboratorio): sono citati.
- **Non nomina** i collaudatori né valuta in concreto requisiti/conflitto di interesse
  (art. 16).
- **Non tratta** il **collaudo statico** strutturale (DPR 380 art. 67): coperto da
  `denuncia-opere-strutturali-l1086`.
- **Non sostituisce** la stazione appaltante, il RUP o l'organo di collaudo.

**La skill è un supporto documentale: non sostituisce la stazione appaltante, il RUP né
l'organo di collaudo, né la lettura dell'art. 116 del D.Lgs. 36/2023.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
