# Estratto: AI Act Allegato III - Sistemi di IA ad alto rischio (art. 6 par. 2)

**Fonte**: `sources.yaml` id `ai-act-it-eurlex`
**Data consultazione**: 2026-04-25
**Hash SHA256**: a61b61706aee6676e3988ab696162d71d759c3debd48b2ecccac3555207f2b0c

---

L'Allegato III definisce 8 settori di applicazione + sotto-categorie per cui un sistema di IA e' considerato **ad alto rischio** ex art. 6 par. 2. Lista esaustiva ma modificabile dalla Commissione (atti delegati art. 7).

## 1. Biometria (nei limiti del diritto UE/nazionale)

- **a)** Sistemi di **identificazione biometrica remota**.
  *Esclusi*: sistemi per la sola **verifica biometrica** (1:1) per confermare identita'.
- **b)** Sistemi di **categorizzazione biometrica** basata su attributi/caratteristiche sensibili dedotti.
- **c)** Sistemi di **riconoscimento delle emozioni**.

## 2. Infrastrutture critiche

Sistemi destinati a **componenti di sicurezza** nella gestione di:
- Infrastrutture digitali critiche
- Traffico stradale
- Fornitura di acqua, gas, riscaldamento, elettricita'

## 3. Istruzione e formazione professionale

- **a)** Determinazione **accesso/ammissione/assegnazione** alle istituzioni
- **b)** Valutazione **risultati apprendimento** (anche per orientare percorsi)
- **c)** Valutazione **livello di istruzione adeguato** ricevuto/accessibile
- **d)** **Monitoraggio comportamenti vietati** durante prove (proctoring)

## 4. Occupazione, gestione lavoratori, accesso al lavoro autonomo

- **a)** **Reclutamento/selezione**: annunci mirati, analisi/filtraggio candidature, valutazione candidati
- **b)** Decisioni su:
  - Condizioni rapporti di lavoro
  - Promozione/cessazione rapporti
  - Assegnazione compiti basata su comportamento o caratteristiche personali
  - Monitoraggio e valutazione prestazioni/comportamento

> **Nota commerciale**: e' uno dei settori piu' rilevanti per Italian SaaS/HR-tech.

## 5. Accesso a servizi privati essenziali e a prestazioni/servizi pubblici essenziali

- **a)** **Servizi pubblici essenziali**: ammissibilita' a prestazioni di assistenza pubblica essenziali (anche sanitaria), con poteri di concessione/riduzione/revoca/recupero
- **b)** **Credit scoring**: valutazione affidabilita' creditizia o merito di credito (escluso solo se finalita' antifrode)
- **c)** **Pricing assicurazioni** vita e sanitarie (valutazione rischi e determinazione prezzi)
- **d)** **Triage emergenze**: valutazione/classificazione chiamate, dispatching, priorita' per polizia/VVF/medica + selezione pazienti

## 6. Attivita' di contrasto (law enforcement) - nei limiti del diritto applicabile

- **a)** Determinazione rischio di **diventare vittima** di reati
- **b)** Poligrafi e strumenti analoghi
- **c)** Valutazione **affidabilita' elementi probatori**
- **d)** Determinazione rischio di **commissione reato/recidiva** (non solo profilazione, anche valutazione tratti personalita' o comportamento criminale pregresso)
- **e)** **Profilazione** persone fisiche durante indagini/perseguimento

## 7. Migrazione, asilo, gestione frontiere - nei limiti del diritto applicabile

- **a)** Poligrafi/analoghi
- **b)** Valutazione **rischio** (sicurezza, migrazione irregolare, salute)
- **c)** Assistenza esame **domande** asilo/visto/soggiorno + valutazione affidabilita' elementi probatori
- **d)** **Identificazione di persone fisiche** in migrazione/asilo/frontiere (esclusa verifica documenti viaggio)

## 8. Amministrazione della giustizia e processi democratici

- **a)** Assistenza **autorita' giudiziaria** in ricerca/interpretazione fatti e diritto, applicazione legge, ADR
- **b)** Sistemi per **influenzare l'esito di elezioni/referendum** o il comportamento di voto
  *Esclusi*: strumenti per organizzare/strutturare campagne politiche da un punto di vista logistico

---

## Note operative per ingegneri

### Sistemi tipici che ricadono in Allegato III

| Settore | Esempio sistema | Sotto-categoria |
|---------|----------------|------------------|
| 4 - HR | ATS con AI scoring CV, video interview AI | 4.a, 4.b |
| 5 - Credit | Modello ML credit scoring | 5.b |
| 5 - Insurance | Pricing assicurazioni vita | 5.c |
| 1 - Biometria | Riconoscimento emozioni in retail/uffici | 1.c |
| 3 - EdTech | Proctoring sistema d'esame | 3.d |
| 2 - Critica | Sistema controllo flusso traffico autostrade | 2 |
| 8 - Giustizia | Tool AI per analisi sentenze (giudici) | 8.a |

### NON in Allegato III (e tipicamente non high-risk)

- ChatBot generico assistenza clienti (rischio limitato art. 50)
- Generazione contenuti creativi (rischio limitato art. 50)
- Antifrode bancario (escluso esplicitamente da 5.b se solo per frodi)
- Verifica biometrica 1:1 (esclusa esplicitamente da 1.a)
- Filtri spam, antimalware (rischio minimo)

### Eccezione "low-risk in Allegato III" art. 6 par. 3

Anche un sistema **elencato in Allegato III** puo' essere classificato non-alto-rischio se rientra in una delle 4 condizioni del par. 3 (compito procedurale limitato, migliora attivita' completata, rileva schemi/deviazioni senza sostituire, prepara valutazione) **E** non effettua profilazione.

In tal caso:
- Documentare la valutazione
- Registrare nella banca dati UE (art. 49 par. 2)
- Mettere a disposizione documentazione su richiesta autorita'
