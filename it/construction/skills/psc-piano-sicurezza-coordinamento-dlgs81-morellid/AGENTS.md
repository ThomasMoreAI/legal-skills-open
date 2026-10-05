# AGENTS.md - psc-piano-sicurezza-coordinamento-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **coordinatore per la sicurezza in fase di progettazione (CSP)** e al **coordinatore per
l'esecuzione (CSE)** per la **redazione** e la **verifica di completezza** del **Piano di Sicurezza e Coordinamento
(PSC)** nei cantieri temporanei o mobili secondo il **D.Lgs 81/2008**, **art. 100** e **Allegato XV** (punto 1
definizioni, punto 2 contenuti minimi del PSC, punto 4 stima dei costi della sicurezza).

**È una skill documentale per il tecnico**: inquadra i contenuti minimi del PSC e la stima dei costi; **non** redige
il piano al posto del coordinatore né esegue la valutazione dei rischi del cantiere.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Copre i **contenuti minimi del PSC** (Allegato XV, punto 2) e la **stima dei costi
della sicurezza** (punto 4). È **distinta** da:
- `pos-allegato-xv-checker` (POS, Allegato XV punto 3.2, redatto dal datore di lavoro dell'impresa esecutrice): il PSC
  è il piano del **coordinatore**;
- `coordinatori-sicurezza-cantieri-dlgs81` (ruoli e obblighi di CSP/CSE, artt. 89-92): questa skill entra nel
  **contenuto** del PSC.
Condivide la fonte (Testo coordinato INL del D.Lgs 81/2008) con `pos-allegato-xv-checker`.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-consolidato-inl-2025-01**: Testo coordinato del D.Lgs 81/2008 — Edizione gennaio 2025 (INL), SHA256
  `f593e18...` (doppio download riproducibile, stesso file usato da `pos-allegato-xv-checker`). Art. 100 e Allegato XV
  estratti con `pdftotext -layout` (testo legale in prosa, senza costanti numeriche/formule da verificare su
  immagine). Edizione INL non ufficiale: per uso autoritativo cross-checkare su Normattiva/Gazzetta Ufficiale.

Trascrizione in `references/fonti/dlgs-81-2008-art-100-allegato-xv.md`; estratto operativo in
`references/estratti/psc-checklist.md`.

## Punti chiave (dal testo di legge)

- **Obbligo/titolarità**: cantiere con **più imprese anche non contemporanea** → nomina CSP/CSE (art. 90 c.3-4); il
  **CSP redige** il PSC (art. 91), il **CSE verifica e adegua** (art. 92).
- **Art. 100**: PSC = relazione tecnica + prescrizioni + **stima costi** (punto 4 All. XV) + **tavole** (planimetria);
  **parte integrante del contratto**; copia agli **RLS 10 giorni prima**.
- **Allegato XV, 2.1.2**: contenuti minimi lett. a)-l) (opera, soggetti, valutazione rischi, scelte/procedure/misure
  per area/organizzazione/lavorazioni, prescrizioni per interferenze, misure di coordinamento, cooperazione, pronto
  soccorso/antincendio, cronoprogramma e **uomini-giorno**, stima costi). Punti 2.2 e 2.3 (aree, organizzazione,
  lavorazioni, interferenze).
- **Allegato XV, 4.1**: stima costi (apprestamenti, DPI interferenze, impianti terra/antincendio/evacuazione fumi,
  protezione collettiva, procedure, sfasamento, coordinamento); **congrua e analitica**; **non soggetta a ribasso**;
  liquidata dal **DL su approvazione CSE**.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il PSC al posto del coordinatore né eseguire la **valutazione dei rischi** del cantiere; non
  calcolare i costi.
- Non trattare il **POS** (Allegato XV punto 3.2), i **ruoli** di CSP/CSE (artt. 89-92), il **fascicolo dell'opera**
  (Allegato XVI) né la **notifica preliminare** (art. 99): rinvia alle skill/norme dedicate.
- Non inventare contenuti: ogni elemento deve essere rintracciabile in
  `references/fonti/dlgs-81-2008-art-100-allegato-xv.md`.

### Cosa fare
- Fornire la checklist dei contenuti minimi del PSC (2.1.2, 2.2, 2.3) e delle voci di costo (4.1), con rinvio
  all'articolo/punto dell'Allegato XV; segnalare la titolarità (CSP/CSE) e la regola del non-ribasso dei costi.

## Aggiornamento delle fonti

D.Lgs 81/2008: se esce una nuova edizione coordinata INL o cambia l'Allegato XV/art. 100 (modifiche legislative),
riscaricare il PDF, ricalcolare l'hash con doppio download e riestrarre art. 100 e Allegato XV; cross-checkare su
Normattiva.

## Validatori

- Non ancora assegnato (Livello 2 con coordinatore per la sicurezza CSP/CSE abilitato).

## Stato attuale

- Versione: 0.1.0-alpha (closes #478)
- Task files: 2 (`verifica-contenuti-minimi-psc.md`, `imposta-stima-costi-sicurezza.md`)
- Esempi: 2 (verifica di completezza dei contenuti minimi di un PSC; impostazione della stima dei costi della
  sicurezza non soggetti a ribasso)
