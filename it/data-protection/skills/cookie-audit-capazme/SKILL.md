---
name: cookie-audit-capazme
title: Cookie Audit — analisi forense dei cookie di un sito
description: Usa questa skill quando l'utente chiede un'analisi o audit dei cookie di un sito web — es. «analisi cookie», «fai un'analisi cookie approfondita di [sito]», «che cookie usa questo sito», «analizza il banner/consenso cookie», «verifica la conformità cookie/GDPR del sito», «quali tracker carica questa pagina», «cookie compliance». Esegue un audit forense in browser (stato pre e post-consenso in un contesto pulito), identifica la CMP e i tracker di terze parti, ispeziona il container Google Tag Manager reale lato server per bypassare gli ad-blocker, redige la tabella cookie completa, valuta la conformità (Provvedimento Garante 10 giugno 2021 · GDPR · art. 122 Codice Privacy · Direttiva ePrivacy 2002/58/CE), esporta un report Word e propone la remediation (bozza di cookie policy corretta + checklist di adeguamento). Usala anche quando l'utente nomina un sito e chiede genericamente «i cookie», «il banner» o «la privacy dei cookie», anche senza dire esplicitamente «audit».
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/cookie-audit
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: data-protection
language: it
sources:
- title: Browser Probes
  path: references/browser-probes.md
- title: Cmp Tracker Fingerprints
  path: references/cmp-tracker-fingerprints.md
- title: Compliance Checklist
  path: references/compliance-checklist.md
---

# Cookie Audit — analisi forense dei cookie di un sito

Produce un'analisi tecnico-legale dei cookie e degli strumenti di tracciamento di un sito pubblico, con la stessa rigorosità di un accertamento privacy: non ci si limita a leggere la cookie policy dichiarata (spesso auto-generata e imprecisa), ma si **osserva il comportamento reale del sito nel browser**, distinguendo ciò che accade **prima** e **dopo** il consenso.

## Cosa produce
1. **Tabella cookie unica** — nome · fornitore/dominio · finalità · durata · categoria · stato (osservato / atteso / condizionale).
2. **Inventario tracker** — CMP usata, container GTM, ID di misurazione/conversione reali (GA4, Ads, Meta, LinkedIn…).
3. **Valutazione di conformità** — contro il Provvedimento del Garante 10.6.2021, il GDPR e l'art. 122 Cod. Privacy (vedi `references/compliance-checklist.md`).
4. **Report Word** su richiesta (`scripts/generate_report.js`).
5. **Remediation** su richiesta — bozza di cookie policy allineata allo stack reale + checklist di adeguamento.

## Principio cardine
Il test decisivo del diritto italiano/UE è: **nessun cookie non tecnico (né chiamata a terze parti non necessarie) prima di un consenso libero e specifico** (art. 122 Cod. Privacy, che recepisce l'art. 5(3) Dir. ePrivacy). Tutto il metodo ruota attorno a verificare empiricamente questo.

---

## Metodo

### Setup del browser
Serve un MCP browser che sappia (a) navigare, (b) eseguire JavaScript nella pagina, (c) leggere le richieste di rete. Vanno bene **chrome-devtools** (`mcp__chrome-devtools__*`) o **claude-in-chrome** (`mcp__claude-in-chrome__*`); carica i tool via `ToolSearch` se sono deferred. Preferire chrome-devtools quando disponibile (contesto isolato + lettura rete più semplice).

Apri il sito in un **contesto isolato/pulito** (nessun cookie pregresso) — es. `new_page({url, isolatedContext:"cookieaudit"})`. Un contesto sporco falsa la Fase 1.

⚠️ **Caveat ad-blocker (leggi sempre).** Molti browser hanno uBlock Origin o simili. Un ad-blocker: blocca il CSS `cookieblocker`, nasconde cosmeticamente il banner (`display:none`), **sostituisce `gtm.js`/`gtag/js` con uno stub** e blocca gli endpoint analytics. Sintomi: `_ga` non compare dopo il consenso, `gtm.js` pesa pochi KB, richieste `net::ERR_BLOCKED_BY_CLIENT`. In tal caso le osservazioni **pre-consenso restano valide**, ma per l'inventario reale **non fidarti del browser**: usa la Fase 3-bis (container GTM lato server). Dichiara sempre questo caveat nel report e marca le voci non osservate come «Atteso».

I frammenti JavaScript esatti da incollare nel tool «evaluate script» sono in **`references/browser-probes.md`**.

### Fase 1 — Stato PRE-consenso (il test cardine)
Subito dopo il caricamento, **prima di toccare il banner**, esegui la probe pre-consenso (`browser-probes.md` §1) e la lista delle richieste di rete. Raccogli:
- `document.cookie`, `localStorage`, `sessionStorage`;
- richieste verso **domini di terze parti** (tutto ciò che non è il dominio del sito);
- globali dei tracker (`gtag`, `ga`, `fbq`, `_linkedin_data_partner_ids`, `hj`, `clarity`, `_hsq`).

**Valuta:** ci sono cookie di analytics/marketing prima del consenso? Ci sono hit verso `google-analytics.com/collect`, Meta, LinkedIn, DoubleClick? Anche il solo caricamento di `gtm.js` comunica l'IP a Google: è una zona grigia da segnalare (vedi checklist).

### Fase 2 — CMP e banner
Identifica la **Consent Management Platform** dai prefissi cookie / globali JS / selettori (tabella in `references/cmp-tracker-fingerprints.md`). Poi ispeziona il DOM del banner (`browser-probes.md` §2) — se l'ad-blocker lo nasconde, leggilo comunque dal DOM. Verifica i punti del Garante:
- **parità Accetta/Rifiuta** sul primo livello (stesso peso grafico: colore, dimensione, posizione)?
- pulsante di **rifiuto** presente subito, senza livelli aggiuntivi?
- **granularità** (categorie) e link a cookie/privacy policy?
- **no scroll-acceptance**, no cookie wall?
- consenso reso **nella lingua** dell'utente?
- eventuale **IAB TCF** attivo (gestione vendor)?

### Fase 3 — Stato POST-consenso
Concedi il consenso completo (procedura per CMP in `browser-probes.md` §3), attendi ~2s, ri-esegui la probe. Registra i cookie/tracker che si aggiungono e i segnali **Google Consent Mode v2** (`ad_storage`, `ad_user_data`, `ad_personalization`, `analytics_storage`) se presenti.

### Fase 3-bis — Inventario reale via container GTM (bypassa l'ad-blocker)
Se il sito usa GTM (container `GTM-XXXXXXX`), **scarica il container lato server** con `curl` (nessun ad-blocker) ed estrai gli ID reali dei tag. È la fonte più affidabile per sapere *cosa* il sito installa davvero:
```
bash "${CLAUDE_PLUGIN_ROOT}/skills/cookie-audit/scripts/inspect_container.sh" GTM-XXXXXXX
```
Lo script recupera `gtm.js`, verifica che sia il container reale (non uno stub) e cerca: GA4 (`G-`), Google Ads (`AW-`), Floodlight (`DC-`), Universal Analytics legacy (`UA-`), Meta, LinkedIn, Hotjar, Clarity, e i flag Consent Mode. Interpreta i risultati con la tabella in `cmp-tracker-fingerprints.md` (§ pattern ID e § boilerplate GA4).

### Fase 3-ter — Inventario dichiarato
Apri la **cookie policy** del sito (di norma linkata nel footer / nel banner) ed estrai la tabella dei cookie dichiarati. Confronta col reale: le policy auto-scansionate spesso elencano cookie di **CMP diverse** (es. `OptanonConsent` di OneTrust, `CookieConsent` di Cookiebot) o plugin **non in uso** (Elementor, WPML) → sono voci **spurie** da segnalare come difetto di trasparenza (art. 13 GDPR).

### Fase 4 — Sintesi, tabella e valutazione
Consolida tutto in **una tabella unica** (vedi «Formato tabella»). Poi redigi la valutazione di conformità seguendo `references/compliance-checklist.md`. **Verifica le norme citate con `cite_law()`** (plugin legal-it) prima di finalizzare — es. `art. 13 GDPR`, `art. 5 GDPR`, `art. 122 D.Lgs. 196/2003`; segnala come fuori copertura la Dir. ePrivacy e il Provvedimento del Garante (soft law, non recuperabili).

---

## Formato tabella (unica)
Colonne, in quest'ordine: **Nome cookie · Fornitore / Dominio · Finalità · Durata · Categoria · Stato**.
Categorie: *Tecnico/necessario · Preferenze · Statistica · Marketing · Sicurezza*.
Stato con legenda esplicita:
- **Osservato** — realmente presente nel browser durante il test;
- **Atteso (post-consenso)** — non comparso per via dell'ad-blocker ma confermato dal container reale / policy: presente per l'utente comune;
- **Condizionale** — solo su certe pagine (form, checkout, sottodomini).

Escludi (o segnala esplicitamente come spurie) le voci della policy che non trovano riscontro nel comportamento reale.

## Report Word (su richiesta)
Prepara un JSON con la struttura descritta in cima a `scripts/generate_report.js`, poi:
```
NODE_PATH="$(npm root -g)" node "${CLAUDE_PLUGIN_ROOT}/skills/cookie-audit/scripts/generate_report.js" audit.json "/percorso/Desktop/Analisi-cookie-<sito>-<data>.docx"
```
Richiede il pacchetto npm globale `docx` (`npm i -g docx`) — la stessa dipendenza di `esporta-documento`. Lo script stampa su stdout il path assoluto del file: riportalo sempre all'utente. La validazione del `.docx` è opzionale; se è installata la skill `docx` di Anthropic puoi usare `python ~/.claude/skills/docx/scripts/office/validate.py <file>`, altrimenti l'apertura del file conferma la buona formazione. In alternativa, per un report discorsivo in stile SAPG, scrivi il contenuto in markdown e passalo alla skill `esporta-documento`.

## Remediation (su richiesta)
Quando emergono criticità, produci — vedi `references/compliance-checklist.md` § Remediation:
1. **Bozza di cookie policy corretta** allineata allo stack reale (puoi usare `genera_informativa_cookie` del plugin legal-it come base, poi correggere l'inventario coi dati raccolti).
2. **Checklist di adeguamento** al Provvedimento del Garante, prioritizzata per gravità.

## Onestà del risultato
Distingui sempre osservato vs desunto. Se l'ad-blocker ha limitato la Fase 3, dillo e offri di ripetere in un browser pulito. Non dichiarare durate di scadenza «esatte» se sono state desunte dalla config della CMP e non lette dal browser: `document.cookie` non espone la scadenza.
