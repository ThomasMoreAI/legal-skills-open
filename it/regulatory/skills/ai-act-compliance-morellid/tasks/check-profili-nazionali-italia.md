# Task: Profili nazionali italiani - D.Lgs. 160/2026 (penale, 231, civile, polizia)

Per un fornitore o deployer che opera in Italia, valuta le conseguenze nazionali introdotte dal D.Lgs. 9 settembre 2026,
n. 160 sopra gli obblighi del Reg. (UE) 2024/1689: reato art. 437-bis c.p., responsabilità dell'ente ex D.Lgs.
231/2001, regole processuali civili sul risarcimento e, per chi lavora con le Forze di polizia, la disciplina del Titolo I.

## Obiettivo

Produrre una mappa dei rischi nazionali (penale, 231, civile) collegata agli obblighi AI Act già verificati, con le
misure documentali che riducono l'esposizione (prova in giudizio, modello 231, polizza RC).

## Input richiesti

- Classificazione del sistema (da `classifica-sistema.md`): il reato 437-bis riguarda **solo sistemi ad alto rischio**
- Ruolo dell'organizzazione (fornitore, deployer, altro) e natura giuridica (ente soggetto al D.Lgs. 231/2001?)
- Esito di `check-high-risk-provider.md` o `check-deployer-obligations.md`, se già eseguiti (gap su artt. 9, 11, 12, 14, 15, 26)
- Contesto d'uso: il malfunzionamento o l'assenza di sorveglianza umana può creare **pericolo per la vita o
  l'incolumità** o per la sicurezza dello Stato?
- Esistenza di un modello organizzativo 231 e di una polizza RC che copra danni da sistemi IA
- Eventuale fornitura o uso per finalità di polizia (Forze di polizia, gestori di luoghi o eventi con videosorveglianza)

## Fonti

Leggere prima: `references/estratti/dlgs-160-2026-profili-nazionali.md` (testo in `references/fonti/dlgs-160-2026.md`).
Per gli obblighi richiamati: `references/estratti/ai-act-art-6-9-classificazione-high-risk.md`,
`references/estratti/ai-act-art-26-27-deployer-fria.md`.

## Procedura

### 1. Esposizione penale - art. 437-bis c.p. (art. 12 del decreto)

Applicabile solo a sistemi **ad alto rischio**. Il reato richiede che dall'omissione o alterazione **derivi un pericolo**
per la vita o l'incolumità pubblica o individuale (o per la sicurezza dello Stato).

- [ ] **Chiunque** (c.1): omette le misure tecniche di sicurezza previste per progettazione, addestramento,
      produzione, immissione sul mercato, idonee a prevenire malfunzionamenti o alterazioni (per il fornitore il rinvio
      naturale sono robustezza e cybersicurezza art. 15), **ovvero** omette misure di sorveglianza umana (art. 14 per il
      fornitore, art. 26 par. 2 per il deployer). Pena 1-5 anni (2-8 per sicurezza dello Stato); per **colpa grave**
      ridotta da un terzo a un sesto (c.3). Il soggetto non è limitato al fornitore e il c.1 non richiede
      l'intenzionalità: anche il deployer può rientrarvi.
- [ ] **Utilizzatore professionale** (c.4): ipotesi specifica di omissione **intenzionale** delle misure di sorveglianza
      umana, con le pene del c.1 (senza la riduzione per colpa grave del c.3, che richiama solo il c.1). Segnalare che "utilizzatore professionale" non è definito nel Reg. 2024/1689: l'accostamento al deployer
      (art. 26 par. 2: persone designate alla sorveglianza, con competenza, formazione e autorità) è un'interpretazione.
- [ ] **Alterazione** del sistema da parte di chiunque, fuori dai casi del c.1 (c.2): 2-6 anni (3-10 per sicurezza dello
      Stato). Rilevante per controlli di accesso e integrità di modelli e pipeline.
- [ ] Il contesto d'uso rende plausibile il pericolo per vita o incolumità? Se no, dirlo: il gap resta una violazione
      AI Act, ma il 437-bis non si configura.

### 2. Responsabilità dell'ente - art. 25-vicies D.Lgs. 231/2001 (art. 15 del decreto)

- [ ] L'ente è soggetto al D.Lgs. 231/2001? Se sì, il 437-bis è reato presupposto: sanzione pecuniaria **600-1000
      quote** più **sanzioni interdittive** art. 9 c.2 lett. b), c), d), e).
- [ ] Il 612-quater c.p. è anch'esso presupposto (200-700 quote, stesse interdittive). Il decreto non ne descrive il
      contenuto: rinviare al codice penale senza descriverlo.
- [ ] Aggiornare la mappatura dei rischi e i protocolli del modello 231 per i processi di progettazione, rilascio e
      sorveglianza umana dei sistemi ad alto rischio.

### 3. Esposizione civile - artt. 16-20 del decreto

- [ ] **Prova (art. 17)**, per **ogni** sistema IA, qualunque sia il livello di rischio: il giudice può ordinare
      l'esibizione degli elementi sul funzionamento del sistema. Se non si esibiscono **log (art. 12), documentazione
      del risk management (art. 9), documentazione tecnica (art. 11), parametri di sorveglianza umana (art. 14)**, il
      giudice ritiene ammessi i fatti allegati dal danneggiato. Verificare che questi documenti **esistano, siano
      conservati e siano reperibili** (per il deployer: log per almeno 6 mesi, art. 26 par. 6).
- [ ] **Presunzione del nesso causale (art. 18)**: se il danno deriva dalla violazione di un obbligo AI Act, il nesso è
      presunto salvo prova contraria. Ogni gap AI Act trovato nei task precedenti va letto anche come rischio
      probatorio.
- [ ] **Conformità (art. 19)**: la conformità, anche certificata, non esclude di per sé la responsabilità. Non
      presentare marcatura CE o certificazione come scudo.
- [ ] **Assicurazione (art. 20)**: il danneggiato può chiedere se esiste una polizza RC; risposta entro **30 giorni**
      (esistenza, estremi, compagnia), altrimenti argomenti di prova. Azione diretta verso l'assicuratore nei limiti del
      massimale. Verificare copertura, massimale ed esclusioni della polizza e predisporre una procedura di risposta.
- [ ] Clienti consumatori: foro alternativo di residenza o domicilio del danneggiato (art. 16 c.4).
- [ ] Restano fermi art. 82 GDPR e disciplina nazionale di recepimento della Dir. (UE) 2024/2853 (art. 16 c.3).

### 4. Forniture o usi per finalità di polizia (Titolo I, artt. 1-10, art. 21)

Solo se il sistema è usato da o per le Forze di polizia, o installato da gestori di luoghi o eventi (art. 10 c.13).

- [ ] Il Titolo I **non aggiunge obblighi** a quelli del Reg. 2024/1689 (art. 1 c.3; art. 3 c.7); disciplina però
      procedure e condizioni d'uso.
- [ ] Output usati in atti che incidono sugli interessati: prevedere **revisione umana qualificata** e la sua
      **tracciabilità** (art. 3 c.4). Il fornitore deve rendere possibile la documentazione della revisione.
- [ ] Contratti di ricerca e sviluppo con privati: clausole su dati operativi sensibili, proprietà intellettuale,
      titolarità dei modelli in capo alle Forze di polizia (art. 4).
- [ ] Identificazione biometrica remota in tempo reale (art. 8, art. 359-ter c.p.p.): banca dati di riferimento per
      singolo utilizzo e cancellabile, **nessuna banca dati da scraping non mirato**, log non modificabili conservati
      5 anni, FRIA e DPIA preventive (art. 9).
- [ ] Videosorveglianza con riconoscimento facciale a posteriori (art. 10): conservazione 7 giorni con cancellazione
      automatica, log non modificabili conservati 5 anni, nessuna decisione basata unicamente sul riconoscimento facciale.
      Gestori e organizzatori che installano: sistemi in comodato gratuito alla questura.
- [ ] Sistemi già in uso o in contratto: adeguamento al capo II del Titolo I entro **un anno** dall'entrata in vigore
      del decreto (art. 21). Il decreto non fissa la data di entrata in vigore: verificarla su Normattiva.

## Output strutturato

```markdown
# Profili nazionali D.Lgs. 160/2026 - [sistema]

**Data verifica**: [data]
**Sistema**: [descrizione + classificazione AI Act]
**Ruolo**: [fornitore / deployer (utilizzatore professionale?) / altro]
**Ente soggetto a D.Lgs. 231/2001**: [SI / NO]

## Esito sintetico

| Area | Esposizione | Motivazione |
|---|---|---|
| Penale 437-bis c.p. | [ALTA / MEDIA / BASSA / N/A] | [gap su sicurezza/sorveglianza + pericolo per vita/incolumità] |
| 231 art. 25-vicies | [...] | [modello 231 aggiornato?] |
| Civile - prova (art. 17) | [...] | [log, risk management, doc tecnica, parametri sorveglianza disponibili?] |
| Civile - presunzione (art. 18) | [...] | [gap AI Act aperti] |
| Assicurazione (art. 20) | [...] | [polizza, massimale, procedura risposta 30 gg] |
| Polizia (Titolo I) | [...] | [se applicabile] |

## Gap e azioni

[Per priorità, con articolo del decreto e articolo AI Act collegato]

## Interpretazioni da validare

- [es. qualificazione come "utilizzatore professionale"]
- [es. data di entrata in vigore da verificare su Normattiva]
```

## Limiti

- Analisi di esposizione al rischio, non parere penale: la qualificazione del fatto spetta a un penalista.
- "Utilizzatore professionale" (art. 437-bis c.4) non è definito dal decreto né dal Reg. 2024/1689.
- Il decreto non fissa la data di entrata in vigore; decreti attuativi del Titolo I (artt. 5, 9 c.5, 10 c.12) non ancora
  catalogati.
- Non copre la disciplina nazionale di recepimento della Dir. (UE) 2024/2853 né l'art. 612-quater c.p.

## Esempi

Vedi `examples/profili-nazionali-triage-pronto-soccorso/`: deployer ospedaliero di un sistema ad alto rischio con
gap sulla sorveglianza umana.
