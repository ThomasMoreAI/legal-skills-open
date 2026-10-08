---
name: memo-legale-strutturato-avvocati-e-mac
title: Memo legale strutturato
description: 'Redige memo legali italiani chiari, sintetici e operativi per uso interno dell''avvocato o dello studio, con quesiti, risposta breve, fatti rilevanti, istituti applicabili, fonti, rischi, opzioni e piano d''azione. Vale per diritto civile, lavoro, amministrativo, tributario, penale e altre materie italiane. MANDATORY TRIGGERS: richieste di memo legale, memorandum, parere interno, nota per avvocato, case assessment, legal risk assessment, strategia precontenziosa/processuale, analisi di documenti per decidere una linea legale, oppure trasformazione di ricerche/fonti in un memo operativo.'
author: avvocati-e-mac
author_url: https://github.com/avvocati-e-mac/skill-legali/tree/main/memo-legale-strutturato/memo-legale-strutturato
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: it
sources:
- title: Adattamento Diritto Italiano
  path: references/adattamento-diritto-italiano.md
- title: Modelli Memo
  path: references/modelli-memo.md
- title: Tooling Installazione
  path: references/tooling-installazione.md
---

# Memo legale strutturato

Skill per produrre memo legali italiani efficienti: abbastanza completi per
decidere, abbastanza brevi per essere letti.

## Principio guida

Scrivere per l'avvocato che deve prendere una decisione professionale. Il memo
non e' un manuale: ogni sezione deve aiutare a capire fatto, diritto, rischio o
prossima azione.

## Progressive disclosure

Non caricare reference di routine. Usa questo file come workflow base e apri i
reference solo se servono:

- `references/modelli-memo.md`: quando serve scegliere template, indice,
  tabelle o livello di dettaglio.
- `references/adattamento-diritto-italiano.md`: quando il memo riguarda una
  materia specifica o devi adattare modelli IRAC/CRAC/CREAC al contesto
  italiano.
- `references/tooling-installazione.md`: solo se mancano BuddaLaw/Perplexity o
  l'utente chiede setup/installazione.

## Compatibilita' runtime

- **Claude Desktop, Claude for Work/Cowork o Claude Code:** usa skill, MCP,
  subagenti e file disponibili nell'ambiente Claude.
- **Codex/OpenAI:** usa tool MCP, shell, browser o subagenti disponibili,
  rispettando permessi e privacy del runtime.
- **Tool mancanti:** non inventare equivalenti. Procedi con i fallback qui
  sotto e segnala i limiti nel memo.

## Gate strumenti

All'inizio della prima esecuzione utile nella sessione, verifica in modo
leggero cosa e' disponibile:

1. **BuddaLaw**: skill presente, MCP/tool disponibili, oppure comandi/namespaces
   equivalenti del runtime. Se disponibile, usalo per sentenze, prassi,
   provvedimenti, contratti e atti processuali italiani. Se la skill BuddaLaw
   richiede `check_access`, chiamalo una sola volta per sessione.
2. **Perplexity**: skill `perplexity-web-mcp`, MCP `pplx_*` o CLI `pwm`. Se
   disponibile, usalo solo per ricerche web, dottrina, contesto aggiornato o
   struttura; controlla la quota prima della prima query.
3. **Normattiva/GestioLex**: se disponibili, usali per norme e orientamento
   normativo/giurisprudenziale secondo le rispettive skill.

Se BuddaLaw o Perplexity mancano, non interrompere il lavoro. Solo al primo lancio
della skill in quell'ambiente, chiedi se l'utente ha gli abbonamenti e se vuole
installare skill/MCP; poi apri `references/tooling-installazione.md`.

## Fonti e verifiche

- Non citare sentenze, ordinanze o provvedimenti specifici dalla memoria:
  verifica con BuddaLaw/GestioLex o con fonte fornita e segnalata.
- Non lasciare riferimenti normativi italiani nudi: usa Normattiva quando
  disponibile o marca il punto da linkare.
- Distingui sempre:
  - fonti di **struttura** del memo (template, legal writing);
  - fonti di **diritto applicabile** (norme, giurisprudenza, prassi, dottrina
    qualificata).
- Se gli strumenti live mancano, intitola o marca il documento come bozza da
  verificare e inserisci una sezione "Punti da verificare".

## Scelta del formato

Scegli il formato piu' breve sufficiente:

- **Memo rapido**: una questione, 1-2 pagine, nessuna tabella salvo necessita'.
- **Memo standard**: default; 3-8 pagine; quesiti, fatti, fonti, rischi,
  raccomandazione e azioni.
- **Memo complesso**: solo se richiesto o necessario; aggiunge indice
  navigabile, timeline, evidence map, risk matrix, authorities table e action
  plan.

Usa un indice navigabile solo se il memo supera circa 1.500 parole o contiene
almeno 3 questioni. Le tabelle sono opzionali: inseriscile solo se riducono
ambiguita' o accelerano la decisione.

## Struttura di default

1. **Oggetto e perimetro**: materia, documento/fascicolo, scopo, limiti.
2. **Risposta breve**: conclusione operativa in 5-12 righe.
3. **Quesiti**: domande giuridiche numerate e leggibili.
4. **Fatti rilevanti**: solo fatti decisivi, separati da incertezze e lacune.
5. **Istituti e principi applicabili**: regole essenziali, non trattazione.
6. **Analisi per questione**: conclusione, fonte, applicazione, controargomento,
   rischio residuo.
7. **Opzioni e rischi**: scenari pratici, non percentuali fittizie.
8. **Raccomandazione e azioni**: cosa fare, cosa acquisire, cosa evitare.
9. **Fonti e punti da verificare**: data ricerca, banche dati, limiti.

## Adattamento italiano

Usa IRAC/CRAC/CREAC solo come schema interno. Nell'output scrivi in italiano:
"questione", "principio", "applicazione", "conclusione", "rischio",
"indicazione operativa".

Se la materia incide sul formato, apri
`references/adattamento-diritto-italiano.md` e applica solo la sezione
pertinente.

## Stile

- Frasi brevi, titoli parlanti, conclusione prima della trattazione.
- Niente giurisprudenza decorativa: ogni fonte deve avere un uso nel caso.
- Indicare controargomenti seri e orientamenti contrari rilevanti.
- Evitare previsioni perentorie; preferire "tesi forte/debole", "rischio
  alto/medio/basso", "da verificare".
- Non includere dati personali non necessari; mantenere pseudonimi se presenti.
- Non allungare per completezza astratta: se un punto non cambia la decisione,
  taglialo o spostalo tra i punti da verificare.

## Output minimo obbligatorio

Ogni memo deve contenere almeno:

- risposta breve;
- fatti rilevanti e lacune;
- principi/istituti applicabili;
- applicazione al caso;
- rischi o controargomenti;
- raccomandazione operativa;
- fonti usate o fonti da verificare.
