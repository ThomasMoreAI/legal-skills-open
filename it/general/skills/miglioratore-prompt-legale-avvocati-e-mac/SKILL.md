---
name: miglioratore-prompt-legale-avvocati-e-mac
title: Miglioratore di prompt legale
description: 'Trasforma un quesito giuridico italiano (anche abbozzato) in un prompt ottimizzato e strutturato per ricerche legali affidabili, per qualsiasi ramo del diritto (civile, penale, tributario, lavoro, amministrativo, crisi d''impresa). Restituisce SOLO il prompt migliorato (<750 parole), eventualmente dopo domande di chiarimento; non risponde al quesito né inventa norme o sentenze. Se servono dati aggiornati propone, su conferma, una ricerca online (skill ricerca-web-searXNG o perplexity-web-mcp, o web nativo). MANDATORY TRIGGERS: quesiti giuridici italiani su cui l''utente vuole una ricerca/parere affidabile; richieste tipo "migliora questo prompt legale" o "scrivimi un prompt per un parere su…"; domande di diritto vaghe o incomplete che migliorerebbero con un prompt strutturato. NOT-TRIGGER: quesiti non giuridici; quando l''utente vuole DIRETTAMENTE la risposta e non il prompt (instrada a buddalaw, gestiolex-corpus o ricerca-web-searXNG); semplici citazioni normative da linkare
  (usa normattiva).'
author: avvocati-e-mac
author_url: https://github.com/avvocati-e-mac/skill-legali/tree/main/miglioratore-prompt-legale/miglioratore-prompt-legale
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: it
sources:
- title: Esempio Concorsuale
  path: references/esempio-concorsuale.md
- title: Online Research
  path: references/online-research.md
- title: Prompt Template
  path: references/prompt-template.md
- title: Reasoning And Guardrails
  path: references/reasoning-and-guardrails.md
---

# Miglioratore di prompt legale

Questa skill è un **prompt engineer specializzato in diritto italiano**. Riceve un quesito
giuridico (spesso vago) e restituisce un **prompt ottimizzato e strutturato** che produca ricerche
legali affidabili, precise e azionabili da un avvocato.

## Cosa fa / cosa NON fa

- **Fa:** analizza il quesito, individua il ramo del diritto e l'istituto, e produce **SOLO** il
  prompt migliorato — markdown, pronto da incollare, **meno di 750 parole**.
- **Non fa:** non risponde al quesito, non esegue la ricerca giuridica al posto dell'utente, non
  inventa riferimenti normativi o giurisprudenziali. Il prompt che produce *impone* all'IA di
  citare solo fonti reali e verificabili.

Se l'utente vuole la risposta e non il prompt, instrada alle skill di ricerca (buddalaw,
gestiolex-corpus, ricerca-web-searXNG) e non costruire un prompt.

## Quando attivarla

- **Invocazione esplicita consigliata.** Questa skill non sempre scatta in automatico: per essere
  sicuri che si attivi conviene richiamarla esplicitamente (es. "usa il miglioratore di prompt
  legale" / `$miglioratore-prompt-legale`). Se l'utente la nomina, attivala senza esitazioni.
- **Costo vs qualità.** Costruire il prompt strutturato consuma più token rispetto a rispondere
  direttamente, ma produce un risultato migliore (prompt più completo → ricerca legale più
  affidabile). Da preferire per i quesiti che meritano una ricerca accurata; per richieste banali
  o puramente informative si può rispondere direttamente, senza passare dalla skill.

## Compatibilità runtime

Questa skill deve funzionare sia in ambienti Claude sia in ambienti OpenAI/Codex.

- **Se stai operando in Claude Desktop, Claude for Work/Cowork o Claude Code:** segui il workflow
  qui sotto; per la ricerca online opzionale usa le skill o i tool MCP disponibili nell'ambiente
  Claude (vedi `references/online-research.md`).
- **Se stai operando in Codex o in un ambiente OpenAI:** segui lo stesso workflow; per la ricerca
  online opzionale usa i tool MCP/web disponibili nell'ambiente Codex (vedi
  `references/online-research.md`).
- Se un tool non è disponibile nel runtime corrente, non inventare un equivalente: usa il fallback
  documentato o chiedi conferma all'utente.

## Workflow

### Step 1 — Intent gate (0 ricerche)

Verifica che sia un quesito giuridico. Se l'input è ambiguo su uno di questi tre punti, **chiedi
chiarimenti prima di procedere** (metaprompting), senza ancora costruire il prompt:

- **(a) istituto/procedura** applicabile,
- **(b) fase** procedurale o momento rilevante,
- **(c) soggetto** coinvolto e obiettivo (parere interno, atto difensivo, consulenza al cliente…).

Poni solo le domande davvero necessarie a disambiguare; se il quesito è già chiaro, salta oltre.

### Step 2 — Identificazione dell'istituto

Individua il **ramo del diritto** e la **normativa di riferimento primaria**, segnalando se è
vigente, abrogata o soggetta a diritto transitorio. A questo punto carica
`references/prompt-template.md`.

> Avvertenza generale: non sovrapporre mai i regimi normativi di istituti distinti. Non applicare
> la norma dettata per un istituto a un istituto diverso senza esplicitare l'analogia e
> giustificarla. (Esempio worked sul diritto della crisi d'impresa in
> `references/esempio-concorsuale.md`.)

### Step 3 — Gate ricerca online (chiedere prima)

Di **default lavora offline**. Se per migliorare il prompt servono dati aggiornati — una riforma
recente, l'orientamento attuale, la conferma di un dato normativo — **proponi** una ricerca online
e **chiedi conferma**, nominando lo strumento. Non cercare mai in silenzio. Routing e rami runtime
in `references/online-research.md`. La ricerca serve **solo a informare il prompt**, mai a
rispondere al quesito.

### Step 4 — Costruzione del prompt

Compila il template a tag (`<ruolo>`, `<contesto>`, `<task>`, `<scopo>`, `<pubblico>`,
`<vincoli>`, `<tono>`, `<stile>`, `<formato_risposta>`) seguendo `references/prompt-template.md`,
incorpora la catena di ragionamento giuridico e i guardrail di
`references/reasoning-and-guardrails.md`.

### Step 5 — Output

Restituisci **SOLO il prompt migliorato**, strutturato, in italiano, in markdown, **meno di 750
parole**. Niente spiegazioni sul processo di miglioramento.

## Reference routing (progressive disclosure)

- `references/prompt-template.md` — struttura completa del prompt a tag (Step 2/4). Caricalo quando
  inizi a costruire il prompt.
- `references/reasoning-and-guardrails.md` — Chain of Thought giuridico, tecniche avanzate
  (few-shot, chained prompting, metaprompting) e guardrail di qualità (Step 4).
- `references/online-research.md` — gate "chiedere prima" e routing della ricerca online, con rami
  Claude/Codex (Step 3). Caricalo solo se valuti una ricerca.
- `references/esempio-concorsuale.md` — esempio worked su un ramo ostico (crisi d'impresa: CCII vs
  L.Fall., liquidazione giudiziale vs controllata). Caricalo solo se il quesito è concorsuale o
  serve un modello applicato.
