---
name: risposta-diritti-interessato-pixari
title: Risposta diritti interessato (GDPR)
description: 'Workflow completo per richieste interessato GDPR (artt. 15-22): classificazione, verifica identità, mappatura sistemi, esenzioni, bozza lettera e log decisioni. Usare quando arriva accesso, cancellazione, portabilità, rettifica, opposizione o limitazione. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/privacy-gdpr/skills/risposta-diritti-interessato
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
---

# Risposta diritti interessato (GDPR)

> **Bozza — non consulenza legale.** Verificare termini art. 12 Reg. UE 2016/679, d.lgs. 196/2003 e linee Garante. Coordinare con DPO prima dell'invio.

## Prima di iniziare

1. Leggi `CLAUDE.md` del plugin → sezione **Processo DSAR** (sistemi, verifica identità, SLA, escalation).
2. Apri con disclaimer bozza (`/diritto-italiano-hub:avvertenze-legali` se necessario).
3. **Non inviare** risposte in autonomia: output per revisione legale/DPO.
4. La richiesta contiene dati personali: non salvare nomi in filename; rispetta policy interne.

```
/privacy-gdpr:risposta-diritti-interessato
[incolla email o PEC della richiesta]
```

---

## Step 1 — Classificare la richiesta

Identifica il diritto esercitato (può essere combinato):

| Diritto | Art. GDPR | Output tipico |
| --- | --- | --- |
| Accesso | 15 | Copia dati + informazioni sul trattamento |
| Rettifica | 16 | Correzione dati inesatti |
| Cancellazione | 17 | Erasure (con eccezioni art. 17(3)) |
| Limitazione | 18 | Sospensione parziale del trattamento |
| Portabilità | 20 | Formato strutturato, uso comune |
| Opposizione | 21 | Cessazione per interesse legittimo / marketing |
| Opposizione decisioni automatizzate | 22 | `[da verificare]` profilo e garanzie |

**Combinazioni frequenti:** "cancellate account e mandate prima i dati" = portabilità + cancellazione (due filoni collegati).

Per ogni diritto: indica base normativa con `[da verificare]` se non da fonte live (art. + comma, d.lgs. 196/2003 ove integrativo).

---

## Step 2 — Verifica identità

Usa il metodo in `CLAUDE.md` → **Verifica identità**.

| Metodo | Quando | Rischio |
| --- | --- | --- |
| Sessione autenticata | Richiesta da area riservata | Basso |
| Email/PEC in archivio | Coerenza con anagrafica cliente/dipendente | Medio |
| Documento aggiuntivo | Cancellazione, dati sensibili, account ad alto valore | Richiesto |

**Se identità non verificata** — bozza risposta sospensiva (entro pochi giorni, non a scadenza):

```markdown
Non siamo in grado di verificare che la richiesta provenga dall'interessato i cui
dati sono in questione. Per procedere, La preghiamo di [passo verifica].
Non possiamo fornire dati personali senza verifica adeguata.
```

Argomento pausa termini: documentare in log interno; verificare su testo vigente `[da verificare]`.

**Responsabile vs titolare:** se sei **responsabile** art. 28, verifica se la richiesta va inoltrata al **titolare** (spesso previsto nel DPA).

---

## Step 3 — Mappatura sistemi

Percorri l'elenco sistemi in `CLAUDE.md`. Per ciascuno:

| Sistema | Interrogato? | Dati trovati? | Note |
| --- | --- | --- | --- |
| CRM / gestionale | | | |
| HR / payroll | | | |
| Email / ticketing | | | |
| Marketing / analytics | | | |
| Log / backup | | | Backup: spesso eccezione cancellazione |
| Sub-responsabili | | | Notifica per cancellazione se previsto |

Se l'elenco è vuoto o obsoleto → **flag bloccante** prima di rispondere al merito.

---

## Step 4 — Analisi esenzioni e limiti

### Accesso (art. 15)

Informazioni obbligatorie: finalità, categorie, destinatari, conservazione, fonte, logiche automatizzate rilevanti, trasferimenti, garanzie `[da verificare]`.

### Cancellazione (art. 17)

Valuta eccezioni art. 17(3): obblighi legali, contenzioso, libertà di espressione, archiviazione pubblica, salute, interesse pubblico, accertamento/esercizio diritti `[da verificare]`.

### Portabilità (art. 20)

Solo trattamenti basati su consenso o contratto + automatizzati. Formato interoperabile.

### Opposizione (art. 21)

Distingui marketing diretto (stop immediato se applicabile) vs interesse legittimo (bilanciamento documentato).

### Rifiuto parziale/totale

Per ogni dato/ambito rifiutato: motivazione + riferimento normativo `[da verificare]`.

---

## Step 5 — Bozza lettera

Struttura consigliata:

1. **Intestazione** — titolare/responsabile, riferimento protocollo, data ricezione
2. **Oggetto** — diritto esercitato
3. **Esito verifica identità** — confermata / in attesa
4. **Risposta al merito** — per sistema o per categoria dati
5. **Allegati** — elenco file forniti (senza dati sensibili in bozza se identità incerta)
6. **Rifiuti motivati** — tabella se parziale
7. **Diritti ulteriori** — reclamo Garante art. 77, contatto DPO
8. **Chiusura** — bozza, firma autorizzata

### Tabella riepilogo decisioni (interna + opzionale in allegato)

| Ambito | Esito | Base | Revisore |
| --- | --- | --- | --- |
| CRM | Fornito / Negato | art. … | DPO |

---

## Step 6 — Log e follow-up

Registra in fascicolo interno (cartella mandato se usi `/diritto-italiano-hub:fascicolo-mandato`):

- Data ricezione, data invio risposta
- Termine calcolato `[da verificare]` art. 12
- Sistemi consultati, sub-responsabili notificati
- Escalation (vedi sotto)

### Escalation — fermati e segnala se:

- Richiesta su minori / dati particolari su larga scala
- Possibile data breach collegato
- Contenzioso pendente o conservazione obbligatoria contestata
- Trasferimento extra-SEE non documentato
- Richiesta da autorità o procuratore senza titolo chiaro

---

## Coordinate italiane

- Reg. UE 2016/679 + d.lgs. 196/2003 (Codice privacy) `[da verificare]` coordinamento
- Provvedimenti Garante privacy italiano — verificare su [garanteprivacy.it](https://www.garanteprivacy.it) `[da verificare]`
- Non sostituisce DPIA/LIA del trattamento sottostante

## Appendice — Tabella diritti (promemoria operativo)

| Diritto | Art. | Elementi risposta chiave |
| --- | --- | --- |
| Accesso | 15 | Copia, finalità, destinatari, conservazione, fonti |
| Rettifica | 16 | Correzione o integrazione |
| Cancellazione | 17 | Eccezioni 17(3) documentate |
| Limitazione | 18 | Sospensione trattamento contestato |
| Portabilità | 20 | Formato strutturato, base contratto/consenso |
| Opposizione | 21 | Marketing vs legittimo interesse |
| Opposizione automatizzato | 22 | `[da verificare]` garanzie |

## Appendice — Template log DSAR interno

| Campo | Valore |
| --- | --- |
| ID pratica | |
| Data ricezione | |
| Termine calcolato | `[da verificare]` |
| Verifica identità | |
| Sistemi interrogati | |
| Esito | |
| Revisore DPO | |

## Divieti

- Non confermare in bozza l'esistenza di dati sensibili se identità non verificata
- Non citare sentenze o numeri di articolo senza `[da verificare]` se non da fonte utente
- Non inviare senza revisione DPO/legale

## Appendice — Checklist finale sessione

- [ ] Output inizia con disclaimer bozza / non consulenza
- [ ] Norme e sentenze non verificate: `[da verificare]`
- [ ] Escalation documentata se applicabile
- [ ] Prossimi passi con responsabile (legale, DPO, HR)
- [ ] Nessun dato reale di mandato in Issue/PR pubbliche

## Appendice — Workflow collegati

| Esigenza | Comando |
| --- | --- |
| Profilo studio | `/diritto-italiano-hub:cold-start-interview` |
| Metodo e citazioni | `/diritto-italiano-hub:metodo-giuridico`, `citazione-italiana` |
| Avvertenze | `/diritto-italiano-hub:avvertenze-legali` |
| Fascicolo | `/diritto-italiano-hub:fascicolo-mandato` |

## Appendice — Fonti (non in repo)

Verificare su: Normattiva, EUR-Lex, garanteprivacy.it, database giuridici dello studio.

## Appendice — Test

Fascicoli fittizi in `testatti/` — personaggi inventati.

## Appendice — Revisione umana

Ogni bozza richiede revisione da professionista abilitato prima di invio, deposito o firma.
