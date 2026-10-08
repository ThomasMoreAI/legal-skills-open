# Estratto: AI Act Art. 5 - Pratiche di IA vietate

**Fonte**: `sources.yaml` id `ai-act-it-eurlex`
**Documento**: Reg. UE 2024/1689 - AI Act - testo italiano OJ
**Data consultazione**: 2026-04-25
**Hash SHA256**: a61b61706aee6676e3988ab696162d71d759c3debd48b2ecccac3555207f2b0c
**Licenza**: regolamento UE in pubblico dominio.

---

## Articolo 5 - Pratiche di IA vietate

**Data di applicazione**: 2 febbraio 2025 (gia' in vigore al momento della consultazione) per le 8 pratiche originarie lett. a-h.

**Nuova pratica vietata da Digital Omnibus (accordo provvisorio 7 maggio 2026)**: sistemi di IA per la generazione di immagini intime non consensuali ("nudifier"), di materiale pedopornografico (CSAM) e di deepfake sessualmente espliciti. **Data di adeguamento: 2 dicembre 2026**. Accordo non ancora pubblicato in GUUE - testo definitivo e lettera (probabile lett. i) da confermare.

**Sanzione**: fino a **35 milioni EUR o 7% del fatturato globale annuo** (art. 99 par. 3) - la piu' severa del regolamento.

### Le 8 pratiche vietate (par. 1 lett. a-h)

**a) Tecniche subliminali / manipolative / ingannevoli**
Sistemi che utilizzano tecniche subliminali oltre la coscienza di una persona, o tecniche volutamente manipolative o ingannevoli, aventi lo scopo o l'effetto di **distorcere materialmente il comportamento** di una persona o di un gruppo, pregiudicandone la capacita' di prendere una decisione informata, in modo da provocare o poter ragionevolmente provocare **un danno significativo**.

**b) Sfruttamento di vulnerabilita'**
Sistemi che sfruttano le vulnerabilita' di una persona o di uno specifico gruppo dovute ad **eta', disabilita', situazione sociale o economica**, con l'obiettivo o l'effetto di distorcerne materialmente il comportamento e provocare un **danno significativo**.

**c) Social scoring**
Sistemi per la valutazione o classificazione di persone fisiche o gruppi sulla base del loro **comportamento sociale** o di caratteristiche personali, in cui il punteggio sociale comporti:
- i) trattamento pregiudizievole/sfavorevole in **contesti scollegati** da quelli in cui i dati sono stati originariamente raccolti, oppure
- ii) trattamento pregiudizievole **ingiustificato o sproporzionato** rispetto al comportamento sociale o alla sua gravita'.

**d) Predictive policing su singoli (basato su personalita')**
Sistemi per valutare/prevedere il rischio che una persona fisica commetta un reato **basati esclusivamente** su profilazione o valutazione di tratti/caratteristiche di personalita'. **Eccezione**: sistemi che supportano la valutazione umana **basati su fatti oggettivi e verificabili** direttamente connessi a un'attivita' criminosa.

**e) Scraping facciale per riconoscimento**
Sistemi che creano o ampliano banche dati di riconoscimento facciale tramite **scraping non mirato** di immagini da internet o filmati CCTV.

**f) Riconoscimento emozioni in lavoro/istruzione**
Sistemi per inferire emozioni di persone fisiche **nei luoghi di lavoro e istituti di istruzione**. **Eccezione**: motivi medici o di sicurezza.

**g) Categorizzazione biometrica per dati sensibili**
Sistemi di categorizzazione biometrica che classificano individualmente persone sulla base di dati biometrici per dedurre **razza, opinioni politiche, appartenenza sindacale, convinzioni religiose o filosofiche, vita sessuale o orientamento sessuale**. **Eccezione**: etichettatura/filtraggio di dataset biometrici nel contesto delle attivita' di contrasto.

**h) Identificazione biometrica remota in tempo reale in spazi pubblici (per attivita' di contrasto)**
Vietato salvo eccezioni strettissime (par. 1 lett. h):
- i) ricerca mirata vittime sottrazione/tratta/sfruttamento sessuale o persone scomparse
- ii) prevenzione di minaccia specifica, sostanziale e imminente per la vita o di attacco terroristico
- iii) localizzazione/identificazione di sospetti di reati gravi (Allegato II, pena >= 4 anni)

**Salvaguardie rigorose (par. 2-7)**:
- Autorizzazione preventiva di autorita' giudiziaria o amministrativa indipendente
- FRIA preventivo (art. 27)
- Registrazione nella banca dati UE (art. 49)
- Limitazioni temporali, geografiche, personali

### Nuova pratica vietata da Digital Omnibus (provvisorio, non ancora in GUUE)

**Generazione di immagini intime non consensuali, CSAM, deepfake sessuali espliciti**
Sistemi di IA progettati o impiegati per generare immagini, video o audio che rappresentano:
- materiale pedopornografico (CSAM)
- atti sessuali che coinvolgono persone reali senza il loro consenso (deepfake sessuali non consensuali, app "nudifier")

**Stato**: introdotto dall'accordo provvisorio Digital Omnibus del 7 maggio 2026. Non ancora pubblicato in GUUE. La lettera definitiva (probabile lett. i) e i confini esatti del divieto saranno fissati dal testo finale. **Adeguamento entro 2 dicembre 2026** secondo l'accordo politico.

---

## Note interpretative

- Le pratiche **a) e b)** richiedono entrambi requisiti: "tecnica/sfruttamento" + "distorsione materiale comportamento" + "danno significativo o ragionevolmente probabile". Non basta la tecnica di per se'.
- La **c) social scoring** vieta scoring pubblico/privato di persone fisiche. **Non** vieta credit scoring (che pero' e' high-risk Allegato III par. 5 lett. b).
- La **f) emozioni in lavoro** e' particolarmente rilevante per software HR (es. video interview con sentiment analysis). Vietato indipendentemente dal consenso.
- La **g) categorizzazione biometrica per dati sensibili** non vieta la verifica biometrica (1:1) ne' la categorizzazione per attributi non sensibili (es. eta', genere se non per inferire orientamento).

## Linee guida Commissione

La Commissione ha pubblicato linee guida specifiche sulle pratiche vietate (febbraio 2025). Da consultare per casi di confine.

## Esempi tipici per ingegneri (mappatura rapida)

| Caso | Lettera | Vietato? |
|------|---------|----------|
| Software HR con AI per video-interview che valuta entusiasmo/credibilita' candidato | f) emozioni in selezione | **VIETATO** |
| Sistema di analytics web con dark patterns per indurre acquisti | a) manipolazione | Borderline - serve LIA + valutazione |
| App fitness per minori con gamification "competitiva" | b) sfruttamento eta' | Borderline |
| Credit score basato su comportamento social media (scraping social) | c) social scoring | **VIETATO** se trattamento pregiudizievole in contesti diversi |
| Antifrode bancario su transazioni | d) predictive policing | **NON vietato** (basato su fatti oggettivi, non profilazione personalita') |
| App scraping volti per app di "ritrova persone" | e) scraping facciale | **VIETATO** |
| Sistema sicurezza scuola che rileva aggressivita' studenti (emozioni) | f) emozioni in istruzione | **VIETATO** salvo motivi sicurezza specifici |
| Categorizzazione foto per "trova persone simili" basato su tratti somatici | g) biometrica sensibile | Borderline - dipende da attributi inferiti |
| App "nudifier" / generazione deepfake sessuali non consensuali | nuovo divieto Omnibus (provvisorio) | **VIETATO** dal 2 dicembre 2026 (subordinato a pubblicazione GUUE) |
