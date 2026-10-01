# Checklist di conformità e remediation

## Quadro normativo di riferimento
- **Art. 122 Codice Privacy** (D.Lgs. 196/2003) — consenso per archiviazione/accesso a informazioni nel terminale, salvo cookie tecnici. È il perno; recepisce l'**art. 5(3) Direttiva ePrivacy 2002/58/CE**.
- **GDPR (Reg. UE 2016/679)** — art. 5 (principi: minimizzazione, limitazione conservazione), art. 6 (liceità), art. 7 (condizioni del consenso: libero, specifico, informato, revocabile con pari facilità), art. 13 (informativa trasparente e accurata).
- **Provvedimento del Garante 10 giugno 2021, «Linee guida cookie e altri strumenti di tracciamento»** [doc. web 9677876, reg. n. 231] — soft law che detta i requisiti operativi del banner.
- **Trasferimenti USA**: dopo Schrems II, i tool Google (GA4, Ads) implicano trasferimento a Google LLC (USA); base attuale = **EU-US Data Privacy Framework** (decisione di adeguatezza 10.7.2023), di cui Google LLC è certificata. Da dichiarare in informativa.

> **Verifica delle citazioni**: prima di finalizzare, richiama `cite_law()` (plugin legal-it) per gli articoli citati come norme di legge (es. `art. 13 GDPR`, `art. 5 GDPR`, `art. 122 D.Lgs. 196/2003`). La Direttiva ePrivacy e il Provvedimento del Garante sono **fuori copertura** di `cite_law()` (direttiva UE / atto amministrativo): segnalali esplicitamente come tali.

## Checklist del banner (Provv. Garante 231/2021)
Per ciascun punto: Conforme / Non conforme / Da verificare, con evidenza osservata.

1. **Nessun cookie non tecnico prima del consenso** — dalla Fase 1. È il requisito più importante: la sua violazione è la contestazione tipica del Garante.
2. **Parità Accetta/Rifiuta** — il pulsante di rifiuto ha pari evidenza grafica (colore, dimensione, posizione) di quello di accettazione, sul primo livello.
3. **Rifiuto immediato** — «Rifiuta»/«Continua senza accettare» raggiungibile al primo livello, senza obbligare a entrare nelle preferenze.
4. **Chiusura (X) ≠ consenso** — chiudere il banner con la X equivale al rifiuto/mantenimento delle sole tecniche, non ad accettare.
5. **No scroll-acceptance, no cookie wall** — lo scroll non vale come consenso; l'accesso al sito non è subordinato all'accettazione (salvo alternative legittime, es. pay-or-consent, che vanno valutate a parte).
6. **Granularità** — categorie selezionabili separatamente (statistica, marketing, preferenze…).
7. **Consenso specifico e informato** — link a cookie policy e privacy policy dal banner; finalità chiare.
8. **Revocabilità** — modo semplice e sempre disponibile per modificare/revocare (widget/riapertura banner), con pari facilità della concessione (art. 7 GDPR).
9. **Lingua** — banner e informativa nella lingua dell'utente/della versione del sito.
10. **Durata della scelta** — la ri-riproposizione del banner rispetta i tempi delle linee guida (di norma non prima di 6 mesi, salvo cambi di condizioni).

## Checklist dell'informativa cookie (art. 13 GDPR)
- **Accuratezza**: l'inventario dichiarato corrisponde ai cookie/tracker realmente installati? (Confronto Fase 3 vs 3-ter.) Voci spurie (CMP diverse, plugin non usati, cookie legacy) = difetto.
- Titolare e, se presente, DPO; finalità e **base giuridica** per ciascuna categoria.
- **Terze parti** nominate, con link alle loro policy; **durate** di conservazione; diritti dell'interessato e reclamo al Garante.
- **Trasferimenti extra-UE** (Google/Meta/LinkedIn = USA) con la base (DPF/SCC).

## Punti di attenzione ricorrenti (con inquadramento)
- **GTM caricato pre-consenso** — anche solo `gtm.js` comunica l'IP a Google prima del consenso: zona grigia. Difendibile se GTM non setta cookie e i tag sono gattati da Consent Mode, ma la lettura rigorosa lo considera già un trattamento. Molte CMP permettono di bloccarlo finché manca il consenso «statistico»: raccomandare la valutazione.
- **GA4 come «marketing» o «statistica»** — con Google Signals attivo sconfina nel marketing; coerenza tra categoria dichiarata, comportamento e consenso raccolto.
- **Durata `_ga` 2 anni** — standard Google; valutare in ottica di minimizzazione (art. 5 GDPR), accettabile ma segnalabile.
- **reCAPTCHA «necessario»** — comporta trattamento Google; classificazione da motivare.

## Remediation (quando richiesta)

### 1. Bozza di cookie policy corretta
Genera una base con `genera_informativa_cookie` (plugin legal-it), poi **sostituisci l'inventario** con i cookie realmente rilevati (tabella della Fase 4), rimuovendo le voci spurie e allineando durate/terze parti/categorie al comportamento osservato. L'informativa deve riflettere lo stack reale (CMP, tema, analytics), non un template generico.

### 2. Checklist di adeguamento (prioritizzata)
Ordina gli interventi per gravità:
- **Alta**: cookie non tecnici prima del consenso; assenza di parità Accetta/Rifiuta; informativa materialmente errata.
- **Media**: GTM pre-consenso da bloccare; policy con voci spurie; lingua del banner; classificazione GA4/Signals da chiarire; trasferimenti USA da dichiarare.
- **Bassa**: durate lunghe da rivalutare; rifinitura testi.
Per ogni voce: cosa cambiare, dove (CMP/GTM/informativa), e il riferimento normativo.

> Ambito: la skill diagnostica e propone; non sostituisce la validazione formale del titolare/DPO. Indicarlo nel report.
