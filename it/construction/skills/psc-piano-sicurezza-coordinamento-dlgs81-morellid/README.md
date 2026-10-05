# psc-piano-sicurezza-coordinamento-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con coordinatore per la sicurezza CSP/CSE abilitato da completare)

Skill di **supporto documentale** al **coordinatore per la sicurezza in fase di progettazione (CSP)** e al
**coordinatore per l'esecuzione (CSE)** per la **redazione** e la **verifica di completezza** del **Piano di Sicurezza
e Coordinamento (PSC)** nei cantieri temporanei o mobili secondo il **D.Lgs 81/2008**, **art. 100** e **Allegato XV**
(contenuti minimi del PSC — punto 2; stima dei costi della sicurezza — punto 4).

**Non redige** il PSC al posto del coordinatore né esegue la valutazione dei rischi del cantiere e **non sostituisce**
il coordinatore firmatario: inquadra i contenuti minimi e la stima dei costi. È **distinta** da `pos-allegato-xv-checker`
(POS, redatto dal datore dell'impresa esecutrice) e da `coordinatori-sicurezza-cantieri-dlgs81` (ruoli/obblighi CSP/CSE).

## Target

Coordinatori per la sicurezza (CSP/CSE) che devono redigere o verificare la completezza di un PSC secondo il D.Lgs
81/2008 art. 100 e Allegato XV.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-contenuti-minimi-psc` | Obbligo/titolarità (artt. 90-92, 100) e contenuti minimi del PSC: punto 2.1.2 lett. a)-l), aree/organizzazione/lavorazioni (2.2), interferenze e cronoprogramma (2.3) |
| `imposta-stima-costi-sicurezza` | Stima dei costi della sicurezza (Allegato XV punto 4.1): voci, stima congrua/analitica, costi non soggetti a ribasso, liquidazione |

Nucleo: il **CSP redige** il PSC e il **CSE lo verifica/adegua** (artt. 90-92); **art. 100** (relazione tecnica +
prescrizioni + tavole, parte del contratto, copia RLS 10 giorni prima); **contenuti minimi** 2.1.2 (opera, soggetti,
valutazione rischi, misure per area/organizzazione/lavorazioni, interferenze, pronto soccorso, cronoprogramma,
uomini-giorno, stima costi); **stima dei costi** (4.1) **non soggetti a ribasso**.

## Relazione con altre skill

- Copre i **contenuti minimi del PSC** (Allegato XV punto 2) e la **stima dei costi** (punto 4). **Distinta** da
  `pos-allegato-xv-checker` (POS, punto 3.2) e da `coordinatori-sicurezza-cantieri-dlgs81` (artt. 89-92). Condivide la
  fonte (Testo coordinato INL del D.Lgs 81/2008) con `pos-allegato-xv-checker`.

## Fonti consultate

- **D.Lgs 9 aprile 2008 n. 81** - **art. 100 e Allegato XV** - Testo coordinato Edizione gennaio 2025 (INL), SHA256
  `f593e18...`, estratto con `pdftotext`. Edizione INL non ufficiale: per uso autoritativo cross-checkare su
  Normattiva/Gazzetta Ufficiale.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** il PSC al posto del coordinatore né esegue la **valutazione dei rischi** del cantiere; non calcola i
  costi.
- **Non tratta** il **POS** (Allegato XV punto 3.2, → skill `pos-allegato-xv-checker`), i **ruoli/obblighi** di CSP/CSE
  (artt. 89-92, → skill `coordinatori-sicurezza-cantieri-dlgs81`), il **fascicolo dell'opera** (Allegato XVI) né la
  **notifica preliminare** (art. 99); non sostituisce il coordinatore firmatario.

**La skill è un supporto documentale: non sostituisce il coordinatore per la sicurezza firmatario del PSC né la lettura dell'art. 100 e dell'Allegato XV del D.Lgs 81/2008.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
