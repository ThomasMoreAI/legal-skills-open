# Estratto: AI Act Art. 51-55 - Modelli di IA per finalita' generali (GPAI)

**Fonte**: `sources.yaml` id `ai-act-it-eurlex`
**Data consultazione**: 2026-04-25
**Hash SHA256**: a61b61706aee6676e3988ab696162d71d759c3debd48b2ecccac3555207f2b0c

**Data di applicazione**: 2 agosto 2025 (gia' in vigore al momento della consultazione).

---

## Articolo 51 - Classificazione GPAI con rischio sistemico

Un modello GPAI ha **rischio sistemico** se:
- **a)** ha capacita' di impatto elevato valutate sulla base di strumenti tecnici e metodologie appropriati (incluse le indicazioni del par. 2)
- **b)** la Commissione lo ha designato come tale, di propria iniziativa o su segnalazione dell'AI Office

### Soglia presuntiva (par. 2)

Si presume che il modello abbia **capacita' di impatto elevato** se la quantita' cumulativa di calcolo usata per il suo addestramento, misurata in **operazioni in virgola mobile (FLOP)**, e' **maggiore di 10^25**.

### Notifica (par. 1 lett. a)

Il fornitore notifica alla Commissione **entro 2 settimane** dal raggiungimento della soglia o dal momento in cui sa che il modello la raggiungera'.

---

## Articolo 53 - Obblighi dei fornitori di modelli GPAI (tutti)

Tutti i fornitori di modelli GPAI:

### Par. 1 lett. a) - Documentazione tecnica del modello

Redigono e tengono aggiornata la **documentazione tecnica** del modello, comprensiva del **processo di addestramento e prova** e dei **risultati della valutazione**, contenente almeno le informazioni elencate nell'**Allegato XI**, ai fini della messa a disposizione dell'AI Office e delle autorita' nazionali competenti su richiesta.

### Par. 1 lett. b) - Informazioni a deployer

Redigono, tengono aggiornate e **rendono disponibili informazioni e documentazione** ai fornitori di sistemi di IA che intendono integrare il modello GPAI nei propri sistemi. Tali informazioni:
- Permettono ai fornitori a valle di comprendere capacita' e limitazioni del modello
- Sono almeno conformi all'**Allegato XII**

### Par. 1 lett. c) - Politica copyright

Mettono in atto una **politica di rispetto del diritto d'autore UE**, in particolare per identificare e attuare la riserva di diritti dell'art. 4 par. 3 della direttiva (UE) 2019/790 (DSM Directive) tramite tecnologie all'avanguardia.

### Par. 1 lett. d) - Sintesi pubblica del materiale di addestramento

Redigono e rendono disponibile al pubblico una **sintesi sufficientemente dettagliata** dei contenuti utilizzati per l'addestramento del modello, secondo modello fornito dall'AI Office.

### Par. 2 - Eccezione open-source

Gli obblighi delle lett. a) e b) **non si applicano** ai fornitori di modelli **rilasciati con licenza libera e open-source** che permettono l'**accesso, l'uso, la modifica e la distribuzione** del modello, e i cui parametri (pesi, architettura, ecc.) sono **resi pubblicamente disponibili**.

**ECCEZIONE all'eccezione**: l'esenzione **non si applica** ai modelli GPAI con **rischio sistemico**.

Gli obblighi lett. c) (copyright) e d) (sintesi training) **si applicano sempre**, anche all'open-source.

---

## Articolo 55 - Obblighi aggiuntivi per i fornitori di GPAI con rischio sistemico

In aggiunta agli obblighi dell'art. 53, i fornitori di modelli GPAI con rischio sistemico:

### Par. 1 lett. a) - Valutazione del modello

Effettuano la **valutazione del modello** secondo protocolli e strumenti standardizzati che riflettono lo stato dell'arte, inclusi **adversarial testing del modello** per identificare e mitigare rischi sistemici.

### Par. 1 lett. b) - Valutazione e mitigazione dei rischi sistemici

Valutano e attenuano i possibili **rischi sistemici a livello UE**, comprese le **fonti di rischio**, che possono derivare dallo sviluppo, immissione sul mercato o uso dei modelli GPAI con rischio sistemico.

### Par. 1 lett. c) - Tracciamento, documentazione, reporting di incidenti gravi

**Tengono traccia, documentano e segnalano** all'AI Office e, se del caso, alle autorita' nazionali competenti, **senza indebito ritardo**, le informazioni pertinenti su **incidenti gravi** ed eventuali misure correttive per affrontarli.

### Par. 1 lett. d) - Cybersicurezza

Garantiscono un **livello adeguato di protezione della cybersicurezza** per il modello GPAI con rischio sistemico e l'infrastruttura fisica del modello.

### Par. 2 - Codici di condotta

I fornitori di GPAI con rischio sistemico **possono basarsi sui codici di condotta** ai sensi dell'art. 56 per dimostrare la conformita' agli obblighi del par. 1, **fino alla pubblicazione di norme armonizzate**.

---

## Note operative

### Chi e' fornitore di GPAI

Il "fornitore di un modello GPAI" e' chi sviluppa o fa sviluppare un modello GPAI e lo immette sul mercato/mette in servizio (art. 3 par. 67).

Esempi: OpenAI per GPT-4/5, Anthropic per Claude, Google per Gemini, Mistral per i loro modelli, Meta per Llama (open-source con specificita').

### Chi NON e' fornitore di GPAI

- Deployer/integratori di GPAI in applicazioni (sono fornitori di sistemi di IA a valle - art. 25 vendor liability puo' applicarsi)
- Fornitori di **modelli specializzati** non generali (es. modello specifico per riconoscimento immagini medicali = potenzialmente sistema high-risk Allegato I, non GPAI)

### Soglia GPAI rischio sistemico (10^25 FLOP)

Riferimento approssimativo:
- GPT-4 ~ 10^25 (sopra soglia)
- GPT-3.5 ~ 10^23 (sotto soglia)
- Llama 3 70B ~ 10^24 (sotto)
- Gemini Ultra ~ 10^25-10^26 (sopra)

La soglia e' indicativa, la Commissione puo' modificarla.

### Open-source (art. 53 par. 2)

Esenzione molto rilevante. Per qualificarsi:
- Licenza libera/open-source che permette accesso/uso/modifica/distribuzione
- Pesi e architettura pubblicamente disponibili

Modelli "open-weight ma non open-source" (es. Llama che ha restrizioni d'uso commerciale) sono in zona grigia. Va valutato caso per caso.

### Sanzioni GPAI

- Violazione obblighi art. 53/55: fino a **15 milioni EUR o 3% del fatturato globale** (art. 101 par. 1)
- Reincidenza: limite raddoppiato

### Code of Practice GPAI

L'AI Office sta facilitando la stesura di un **Codice di Condotta** per i fornitori GPAI (art. 56). Adesione al codice = presunzione di conformita' agli obblighi art. 53-55.
