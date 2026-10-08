# Task: Classificazione sistema AI sotto AI Act

Determina se un sistema rientra nell'AI Act, e in caso affermativo lo classifica nelle categorie del regolamento (vietato / alto rischio / rischio limitato / rischio minimo / GPAI).

## Obiettivo

Esito strutturato che indichi:
- **In scope** dell'AI Act? (definizione art. 3 par. 1)
- Se sistema specifico (non GPAI): **categoria di rischio** (vietato / alto / limitato / minimo)
- Se modello GPAI: **GPAI standard** o **GPAI con rischio sistemico**
- Ruolo dell'organizzazione: **fornitore** / **deployer** / **distributore** / **importatore**
- Date di applicazione applicabili al caso

Senza classificazione corretta, gli altri task della skill sono prematuri.

## Input richiesti

- Descrizione del sistema/modello (cosa fa, come, a chi)
- Settore di applicazione (HR, finanza, sanita', educazione, biometria, ecc.)
- Tecnologie usate (ML, regole, deep learning, GPAI integrati)
- Mercato di riferimento (UE? Italia? globale?)
- Ruolo dell'organizzazione (fornisce / acquista e usa / distribuisce)
- Per GPAI: stima FLOP di addestramento (per soglia rischio sistemico 10^25)
- Per sistemi che integrano GPAI: il modello e' di terzi o sviluppato in casa?

## Fonti

Leggere prima:
- `references/estratti/ai-act-art-5-pratiche-vietate.md` - 8 pratiche vietate
- `references/estratti/ai-act-art-6-9-classificazione-high-risk.md` - regole classificazione + sistema gestione rischi
- `references/estratti/ai-act-allegato-iii.md` - 8 settori high-risk
- `references/estratti/ai-act-art-50-trasparenza.md` - rischio limitato
- `references/estratti/ai-act-art-51-55-gpai.md` - GPAI

## Procedura

### Passo 1 - Determinare se il sistema e' "in scope"

Il sistema e' un "sistema di IA" ai sensi dell'art. 3 par. 1 se: **sistema basato su macchine progettato per operare con livelli di autonomia variabili e che, dopo l'implementazione, puo' presentare adattamento e che, per obiettivi espliciti o impliciti, deduce dall'input ricevuto come generare output (predizioni, contenuti, raccomandazioni o decisioni) che possono influenzare ambienti fisici o virtuali**.

Non sono "sistemi di IA":
- Software basati esclusivamente su regole definite da persone fisiche
- Calcolo automatizzato semplice (es. fogli Excel con formule)
- Ottimizzazione che non "deduce" output (es. solver lineari per problemi ben definiti)

Casi limite: classificatori semplici (ML), regole fuzzy, sistemi esperti -> in scope; calcoli statistici descrittivi -> generalmente non in scope.

### Passo 2 - Verificare ESCLUSIONI complete (art. 2)

Casi fuori scope AI Act:
- Sistemi sviluppati e usati esclusivamente a fini militari, difesa, sicurezza nazionale (art. 2 par. 3)
- Ricerca, prova e sviluppo scientifico (art. 2 par. 6 - ma non si applica una volta immesso sul mercato)
- Uso personale non professionale (art. 2 par. 10)
- Sistemi rilasciati con licenze libere/open-source (art. 2 par. 12) - ESCLUSIONE PARZIALE: si applica solo se non immesso sul mercato come parte di un sistema high-risk + non rientra in art. 5/50/GPAI

Se rientra in un'esclusione: documentare e fermarsi.

### Passo 3 - Verificare se PRATICA VIETATA (art. 5)

Verificare le 8 pratiche vietate (lett. a-h, in vigore dal 02/02/2025) **+ nuovo divieto Omnibus** per sistemi di generazione CSAM / deepfake sessuali non consensuali (provvisorio, adeguamento entro 02/12/2026). Se rientra anche solo in una -> **VIETATO**, non e' possibile immettere sul mercato/mettere in servizio (sanzione fino a 35M EUR o 7% fatturato).

Vedi `ai-act-art-5-pratiche-vietate.md` per dettaglio + esempi.

Pattern attenzione (frequenti nei progetti reali):
- HR con riconoscimento emozioni in video interview (lett. f vietato)
- Sistemi di inferenza orientamento sessuale/politico da immagini (lett. g vietato)
- Social scoring privati che ricadono in lett. c
- Manipolazione comportamentale in dark patterns (lett. a) - borderline, valutare con cura

### Passo 4 - Determinare se il sistema e' GPAI (art. 51, 53)

Un **modello GPAI** ha:
- Significativa generalita'
- Capacita' di eseguire competentemente un'**ampia gamma di compiti distinti**, indipendentemente da come e' immesso sul mercato
- Puo' essere integrato in una varieta' di sistemi/applicazioni a valle

Se SI: si applicano gli obblighi GPAI (art. 53). **Verifica anche rischio sistemico** (passo 5).

### Passo 5 - Per GPAI: verifica rischio sistemico (art. 51)

Soglia presuntiva: capacita' di impatto elevato (FLOP > 10^25) o designazione Commissione.

Indicativo:
- GPT-4/5, Claude Opus, Gemini Ultra: probabilmente sopra soglia (rischio sistemico)
- GPT-3.5, Llama 3 70B: sotto soglia (GPAI standard)
- Modelli specializzati piccoli: spesso non GPAI

### Passo 6 - Per sistema specifico: high-risk (art. 6)

#### Via 1 - art. 6 par. 1 (componente sicurezza prodotti Allegato I)

Verifica se il sistema:
- a) e' componente di sicurezza di un prodotto Allegato I (macchine, giocattoli, dispositivi medici, ascensori, automotive, aviazione, ecc.) **oppure** e' esso stesso il prodotto
- b) il prodotto e' soggetto a valutazione di conformita' di terzi

Se SI a entrambe -> high-risk via 1.

#### Via 2 - art. 6 par. 2 (Allegato III)

Verifica se il sistema rientra in uno degli 8 settori dell'Allegato III:
1. Biometria (identificazione remota, categorizzazione sensibile, emozioni)
2. Infrastrutture critiche
3. Istruzione e formazione professionale
4. Occupazione e gestione lavoratori
5. Servizi essenziali (assistenza pubblica, credit scoring, insurance pricing, dispatch emergenze)
6. Attivita' di contrasto
7. Migrazione, asilo, frontiere
8. Amministrazione giustizia e processi democratici

Se SI -> potenzialmente high-risk.

#### Eccezione (art. 6 par. 3)

Se il sistema rientra in Allegato III ma:
- a) compito procedurale limitato, oppure
- b) migliora attivita' umana completata, oppure
- c) rileva schemi/deviazioni senza sostituire valutazione umana, oppure
- d) compito preparatorio per valutazione

E **non** effettua profilazione di persone fisiche -> non e' high-risk.

In tal caso documentare la valutazione (par. 4) e iscriversi nella banca dati UE.

### Passo 7 - Sistema NON high-risk: trasparenza art. 50?

Se non vietato, non high-risk, non GPAI: verificare se ricade in:
- Sistema interagente con persone (chatbot) -> obblighi disclosure art. 50 par. 1 (fornitore)
- Generazione contenuti sintetici -> marcatura machine-readable art. 50 par. 2 (fornitore, anche GPAI)
- Riconoscimento emozioni / categorizzazione biometrica (non vietato) -> informativa art. 50 par. 3 (deployer)
- Deepfake -> divulgazione art. 50 par. 4 (deployer)
- Testo AI per informazione pubblica -> divulgazione art. 50 par. 4 bis (deployer)

Se rientra: classificazione **rischio limitato (trasparenza)**.

### Passo 8 - Identificazione del ruolo dell'organizzazione

Per il caso specifico, identificare:
- **Fornitore (provider)** art. 3 par. 3: chi sviluppa/fa sviluppare e immette sul mercato/mette in servizio sotto il proprio nome o marchio
- **Deployer** art. 3 par. 4: usa sistema sotto la propria autorita' nell'esercizio di attivita' professionale
- **Importatore** art. 3 par. 6: stabilito UE che immette sul mercato un sistema di un fornitore stabilito fuori UE
- **Distributore** art. 3 par. 7: nella catena di approvvigionamento, mette a disposizione

Attenzione caso art. 25 (rebranding/sostanziale modifica): un deployer/distributore che mette il proprio marchio o modifica sostanzialmente il sistema diventa **provider** ai sensi del regolamento.

### Passo 9 - Output

```markdown
# Classificazione AI Act - [nome sistema]

**Data valutazione**: [data]
**Sistema valutato**: [descrizione]
**Organizzazione**: [...]

## Esito sintetico

**Classificazione**: [VIETATO / HIGH-RISK / TRASPARENZA (rischio limitato) / RISCHIO MINIMO / GPAI / GPAI con rischio sistemico]

**Ruolo dell'organizzazione**: [Fornitore / Deployer / Importatore / Distributore]

**Date di applicazione rilevanti** (post accordo Digital Omnibus 7 maggio 2026, **provvisorio - non ancora in GUUE**):
- Pratiche vietate (art. 5 lett. a-h): 02/02/2025 ✓
- AI literacy (art. 4): 02/02/2025 ✓
- GPAI (art. 53-55): 02/08/2025 ✓
- Obblighi trasparenza art. 50 (par. 1, 3, 4, 4 bis): 02/08/2026
- Watermarking art. 50 par. 2 (output sintetici machine-readable): **02/12/2026** (rinvio Omnibus)
- Nuovo divieto Omnibus per CSAM / deepfake sessuali non consensuali: **02/12/2026**
- High-risk Allegato III + FRIA art. 27: **02/12/2027** (era 02/08/2026, rinvio Omnibus)
- High-risk Allegato I (componenti sicurezza prodotti): **02/08/2028** (era 02/08/2027, rinvio Omnibus)

## Motivazione

### In scope dell'AI Act
[SI/NO + motivazione def. art. 3 par. 1 + esclusioni art. 2]

### Pratica vietata (art. 5)?
[Verifica delle 8 lettere a-h]

### GPAI?
[Se applicabile + soglia rischio sistemico]

### High-risk?
[Via 1 art. 6 par. 1 + Allegato I, oppure Via 2 art. 6 par. 2 + Allegato III, con eccezione art. 6 par. 3]

### Trasparenza art. 50?
[Se applicabile]

### Ruolo organizzazione (art. 3, 25)
[Provider/Deployer/etc. + eventuale "rebranding" art. 25]

## Obblighi applicabili

[Bullet list degli obblighi specifici, con rinvio ai task dedicati]

- Se HIGH-RISK FORNITORE -> task `check-high-risk-provider.md`
- Se HIGH-RISK DEPLOYER -> task `check-deployer-obligations.md`
- Se GPAI -> task `check-gpai-provider.md`
- Se TRASPARENZA -> task `check-trasparenza.md`

## Sinergia con GDPR

[Se tratta dati personali: rimando a skill `gdpr-registro-dpia` per Registro art. 30 + DPIA art. 35 + FRIA integrato art. 27 AI Act]

## Limiti di questa classificazione

- Si basa sulle informazioni fornite. Cambiamenti del sistema o uso possono cambiare la classificazione.
- Le linee guida Commissione su art. 6 (in preparazione, scadenza 02/02/2026) potrebbero precisare casi di confine.
- Categorie di confine richiedono valutazione legale specialistica.

## Rinvio al consulente legale

**La classificazione AI Act ha implicazioni legali rilevanti** (sanzioni fino a 35M EUR o 7% fatturato per pratiche vietate; 15M EUR o 3% per high-risk/trasparenza/GPAI). Questa valutazione e' di supporto e va validata da consulente legale specializzato in diritto digitale UE prima di decisioni strategiche o di immissione sul mercato.
```

## Casi tipici

### Software HR con video-interview e analisi candidato
- Probabile **VIETATO** (art. 5 lett. f - emozioni in selezione del lavoro)
- Se non analizza emozioni ma solo competenze testuali (es. trascrizione + matching skill): **HIGH-RISK** (Allegato III par. 4 lett. a)

### Credit scoring ML (vedi anche esempio gdpr-registro-dpia)
- **HIGH-RISK** (Allegato III par. 5 lett. b)
- Sinergia: anche DPIA + FRIA art. 27 (deployer in servizi essenziali)

### Chatbot supporto clienti basato su GPT-4
- **TRASPARENZA art. 50** per il chatbot (fornitore del sistema = chi lo offre come prodotto)
- **GPAI con rischio sistemico** per chi sviluppa il modello sotto (OpenAI, non l'azienda che lo usa)
- L'organizzazione che integra GPT-4 in un chatbot e' **deployer del GPAI** + **fornitore del sistema chatbot**

### Sistema di recommendation per ecommerce
- Tipicamente **rischio minimo** se non rientra in profilazione/decisioni con effetti giuridici
- Trasparenza? Se interagisce direttamente con utente con conversazioni AI: si

### Image generation tool (testo -> immagine)
- **GPAI** se il modello e' generale
- **Trasparenza art. 50 par. 2** per output sintetici (marcatura machine-readable)

### Modello specifico per radiologia (ricerca tumori)
- **HIGH-RISK** via 1 art. 6 par. 1 (dispositivo medico = Allegato I + valutazione conformita' di terzi)

## Limiti di questo task

- Classificazione di alto livello, non sostituisce valutazione legale specifica.
- Le linee guida Commissione su art. 6 sono attese entro 02/02/2026 - alcuni casi di confine possono cambiare.
- Le interpretazioni nazionali (autorita' italiane) possono differire da quelle Commissione.

## Esempi

Vedi `examples/`:
- `classifica-chatbot-cs/` - chatbot customer service basato su GPAI
- `classifica-hr-screening/` - sistema HR (test edge case profilazione)
