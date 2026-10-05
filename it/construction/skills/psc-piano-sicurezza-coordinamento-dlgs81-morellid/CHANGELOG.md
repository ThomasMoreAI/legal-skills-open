# CHANGELOG - psc-piano-sicurezza-coordinamento-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-25

### Added (closes #478)
- Prima versione della skill di supporto al **coordinatore per la sicurezza (CSP/CSE)** per la **redazione** e la
  **verifica di completezza** del **Piano di Sicurezza e Coordinamento (PSC)** nei cantieri temporanei o mobili
  secondo il **D.Lgs 81/2008**, **art. 100** e **Allegato XV** (punto 2 contenuti minimi; punto 4 stima dei costi),
  nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs 9 aprile 2008 n. 81** - Testo coordinato Edizione gennaio 2025 (INL) - SHA256
    f593e1806de920dc16def37920c5623cda2450075ed56051852f2caf6045899a (doppio download riproducibile, stesso file
    usato dalla skill pos-allegato-xv-checker).
  - Art. 100 e Allegato XV (punto 1 definizioni, punto 2 contenuti minimi del PSC, punto 4 stima dei costi) estratti
    con `pdftotext -layout` (testo legale in prosa) e trascritti in
    `references/fonti/dlgs-81-2008-art-100-allegato-xv.md`.
- Estratto operativo `references/estratti/psc-checklist.md`.
- Due task: `verifica-contenuti-minimi-psc.md` e `imposta-stima-costi-sicurezza.md`.
- Due esempi: verifica di completezza dei contenuti minimi di un PSC; impostazione della stima dei costi della
  sicurezza non soggetti a ribasso.

### Contenuto ancorato al testo
- Obbligo/titolarità: nei cantieri con più imprese anche non contemporanea il committente nomina CSP e CSE (art. 90
  c.3-4); il CSP redige il PSC (art. 91 c.1 lett. a); il CSE verifica e adegua il PSC (art. 92 c.1). Art. 100: il PSC è
  relazione tecnica + prescrizioni + stima dei costi (punto 4 All. XV), corredato da tavole (almeno una planimetria);
  è parte integrante del contratto; copia agli RLS almeno 10 giorni prima; l'impresa può proporre integrazioni senza
  modifica dei prezzi; non si applica ai lavori urgenti. Allegato XV punto 2.1.2: contenuti minimi lett. a)-l)
  (identificazione opera; soggetti con compiti di sicurezza; relazione analisi/valutazione rischi; scelte/procedure/
  misure per area/organizzazione/lavorazioni; prescrizioni operative e DPI per interferenze; misure di coordinamento
  uso comune; cooperazione/coordinamento; pronto soccorso/antincendio/evacuazione; durata e cronoprogramma, entità in
  uomini-giorno; stima dei costi); tavole esplicative (2.1.4). Punti 2.2 (area, organizzazione, lavorazioni) e 2.3
  (interferenze, cronoprogramma, sfasamento spazio-temporale). Allegato XV punto 4.1: stima dei costi della sicurezza
  (apprestamenti; misure/DPI interferenze; impianti terra/scariche atmosferiche/antincendio/evacuazione fumi; mezzi di
  protezione collettiva; procedure; interventi di sfasamento; misure di coordinamento); stima congrua e analitica per
  voci singole; costi non soggetti a ribasso (4.1.4); liquidati dal direttore dei lavori su approvazione del CSE (4.1.6).

### Scope e limiti
- Non redige il PSC al posto del coordinatore né esegue la valutazione dei rischi del cantiere; non calcola i costi.
  Non tratta il POS (Allegato XV punto 3.2), i ruoli/obblighi CSP/CSE (artt. 89-92), il fascicolo dell'opera (Allegato
  XVI) né la notifica preliminare (art. 99). Non sostituisce il coordinatore firmatario.

### Note di sviluppo
- Distinta da `pos-allegato-xv-checker` (POS) e da `coordinatori-sicurezza-cantieri-dlgs81` (artt. 89-92). Condivide la
  fonte (Testo coordinato INL del D.Lgs 81/2008) con `pos-allegato-xv-checker`. Validazione Livello 2 con coordinatore
  per la sicurezza CSP/CSE abilitato.
