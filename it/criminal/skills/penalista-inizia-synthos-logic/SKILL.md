---
name: penalista-inizia-synthos-logic
title: Skill — Primo avvio guidato
description: 'Onboarding guidato del kit Penalista Italia per il primo avvio e per ogni utente nuovo. ATTIVARE SEMPRE quando l''utente dice: ''iniziamo'', ''primi passi'', ''sono nuovo'', ''come funziona il kit'', ''da dove comincio'', ''configura il kit'', ''primo avvio'', ''aiutami a partire'', o quando dal contesto risulta che il kit non e'' mai stato configurato (CLAUDE.md con campi placeholder, nessun fascicolo presente, INDEX.md assente). Attivare anche se l''utente sembra perso, chiede cosa puo'' fare il kit, o usa il kit per la prima volta su un caso reale.'
author: Synthos-Logic
author_url: https://github.com/Synthos-Logic/penalista-italia/tree/main/skills/penalista-inizia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: criminal
language: it
---

# Skill — Primo avvio guidato

Questa skill accompagna l'avvocato dal primo messaggio al primo fascicolo operativo. Obiettivo: **operativo in 15 minuti, su un caso vero**, senza che debba leggere documentazione.

## Principi di conduzione (vincolanti)

1. **Linguaggio piano.** Mai termini come "wikilink", "frontmatter", "markdown", "token", "repository". Parla di "fascicolo", "collegamenti", "scadenziario", "il sistema".
2. **Una domanda alla volta.** L'avvocato non compila form: conversa.
3. **Il sistema lavora, l'avvocato decide.** Ogni operazione tecnica (cartelle, file, collegamenti, indici) la fai tu, senza chiedere come — chiedi solo i contenuti (dati del caso, scadenze, nomi).
4. **Sempre su un caso reale.** La demo astratta annoia; il primo fascicolo vero convince. Se l'avvocato non ha un caso da inserire subito, usa il FASCICOLO_SIMULATO come esempio, ma proponi comunque di aprire il primo fascicolo reale alla fine.

## FASE 1 — Verifica configurazione studio

Leggi `CLAUDE.md` nella cartella di lavoro.

- **Se i campi "Dati dello studio" sono compilati:** saluta l'avvocato per nome ("Buongiorno Avvocato [Cognome]") e passa alla Fase 2.
- **Se contengono ancora i placeholder** (`[es. Avv. Mario Rossi]` ecc.): chiedi in un'unica domanda i dati essenziali — nome, foro, tribunale di riferimento, se è cassazionista — e **aggiorna tu il file CLAUDE.md**. Spiega in una riga a cosa servono: "li userò nelle intestazioni di ogni atto".

## FASE 2 — Verifica struttura di lavoro

Controlla che esistano: `INDEX.md`, `SCADENZIARIO.md` (in `penalista-scadenze/` o nella radice), le cartelle di lavoro. **Crea tu ciò che manca**, senza chiedere il permesso per ogni file — riassumi a cose fatte: "Ho preparato l'indice dello studio e lo scadenziario: sono i due file che terrò aggiornati per te."

## FASE 3 — Il primo fascicolo

Chiedi: *"Ha un caso sul tavolo da cui partire? Mi basta il nome del cliente e di cosa è accusato — al resto penso io."*

- **Se sì:** attiva il flusso di apertura fascicolo (vedi skill `penalista-strategia` e comando `/fascicolo`): crea il file, compila i dati, aggiorna INDEX e SCADENZIARIO. Se l'avvocato ha il capo di imputazione, proponi subito l'analisi strategica.
- **Se no:** mostra il caso simulato (FASCICOLO_SIMULATO — Mario Rossi, truffa aggravata) e percorri in 2 minuti cosa il kit sa fare su quel caso.

## FASE 4 — Orientamento sulla fase processuale

In base alla fase del caso inserito, indica il percorso giusto (senza elencare tutto il kit):

| Situazione del cliente | Cosa proporre subito |
|---|---|
| Indagini / avviso 415-bis ricevuto | Calcolo del termine di risposta + analisi del capo di imputazione |
| Misura cautelare in corso | ⚠️ PRIMA DI TUTTO verifica dei termini di fase (skill `penalista-cautelare`) |
| Sentenza da impugnare | Termine per l'appello + analisi dei vizi della sentenza |
| Condanna definitiva | Calcolo pena e requisiti per le misure alternative |

## FASE 5 — La routine (chiusura dell'onboarding)

Spiega la routine in tre righe:
- Ogni sessione si apre con *"Lavoriamo sul fascicolo [nome]"* — al resto pensa il sistema.
- Ogni sessione si chiude con l'aggiornamento di fascicolo e scadenziario — proponilo tu attivamente a fine sessione.
- Le scadenze stanno tutte in un posto solo: lo scadenziario.

**Proposta finale (facoltativa):** se l'ambiente lo consente, offri di impostare un controllo automatico quotidiano dello scadenziario ("ogni mattina controllo le scadenze e ti segnalo i termini entro 15 giorni"). Se l'utente accetta, crea l'attività pianificata.

## Regola di uscita

Chiudi sempre l'onboarding con una frase operativa, non celebrativa: *"Il fascicolo [nome] è aperto e le scadenze sono tracciate. Quando vuole riprenderlo, basta scrivermi 'lavoriamo sul fascicolo [nome]'."*
