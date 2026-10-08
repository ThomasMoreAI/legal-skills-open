# Note di dominio - caso `classifica-hr-emozioni`

## Cosa stiamo testando

Che la skill identifichi correttamente un caso **VIETATO** (art. 5 lett. f) per riconoscimento emozioni in selezione del personale, e che proponga percorsi alternativi praticabili (Opzione 1: pivot a scoring linguistico high-risk).

## Scelte progettuali del caso

- **Caso "trappola" frequente**: video-interview con sentiment analysis e' un prodotto comune in HR-tech (esistente sul mercato pre-AI Act). Diventa vietato dal 02/02/2025.
- **Mix di tecnologie**: facial emotion + voice emotion + LLM scoring. La skill deve isolare la componente vietata (emozioni) dal resto.
- **Mercato italiano + UE**: ricade pienamente sotto AI Act.
- **Provider business**: TalentTech sviluppa e immette sul mercato -> obblighi del provider.

## Output atteso

**VIETATO** (art. 5 par. 1 lett. f).

Con:
- Citazione esatta del considerando 44 sul perche' il legislatore vieta proprio in HR/educazione
- Proposta di Opzione 1 (rimozione componente emozioni -> high-risk Allegato III par. 4 lett. a)
- Riconoscimento delle sinergie GDPR (biometria art. 9), Statuto Lavoratori, dir. 2019/1152
- Sanzione 35M EUR o 7% fatturato citata come deterrente

## Cose che la skill DEVE catturare

- **Il "luogo di lavoro" art. 5 lett. f include anche la selezione/pre-assunzione**. La skill deve riconoscerlo, non interpretarlo restrittivamente.
- **L'eccezione "motivi di sicurezza"** non si applica all'HR. La skill non deve cercare scappatoie.
- **Il pivot a high-risk Allegato III par. 4 lett. a** e' percorribile e va proposto come Opzione 1.
- **Sinergia GDPR su biometria**: anche fosse non vietato, il trattamento di emozioni facciali sarebbe categorie particolari art. 9.

## Cose che la skill NON dovrebbe fare

- **Cercare di "salvare" il sistema** suggerendo riposizionamenti dubbi.
- **Sottovalutare la severita'**: il sistema NON e' "rischioso ma fattibile con piu' compliance". E' VIETATO. Stop.
- **Confondere "limitare l'uso ai contesti non vietati"** come compliance. Il provider e' responsabile per design del proprio prodotto, non solo per l'uso del cliente.
- **Sotto-citare le sanzioni**: 35M / 7% e' la categoria piu' alta. Va detto chiaramente.

## Ambiguita' che richiede attenzione

- **"Inferire emozioni"**: la skill deve ricordare che e' la finalita' del sistema, non l'output letterale. Anche se TalentTech etichetta gli score come "energia/fiducia/ansia" piuttosto che "felice/triste", se la base computazionale e' il riconoscimento di emozioni, ricade nel divieto.
- **"Voice features" vs "voice emotion"**: tono di voce per stimare fiducia/ansia = emotion recognition. Voice features pure (lunghezza, pause) NON automaticamente emozioni - ma in questo caso il sistema esplicitamente le interpreta come emozioni.

## Cosa imparare

- L'AI Act ha un **divieto chiaro** sulle emozioni in HR. Pivot rapido o exit del prodotto.
- Per la consultancy: identificare clienti che hanno gia' lanciato/sviluppato prodotti simili e fornire **incident response** + remediation plan e' un servizio ad alto valore.
- Il momento (aprile 2026) e' critico: vietato dal febbraio 2025 -> molti prodotti sul mercato sono **gia'** non conformi (rischio enforcement).

## Fonte della struttura

Caso fittizio. Pattern reale di diversi prodotti HR-tech che esistevano sul mercato pre-AI Act e che oggi richiedono pivot. Nessun riferimento a aziende reali.

## Implicazioni commerciali per consultancy

Questo tipo di valutazione e' un servizio di alto valore:
- Cliente in difficolta' (deve prendere decisioni difficili)
- Pain altissimo (rischio sanzione + reputational + sviluppo bruciato)
- Documentazione difensiva (prova di due diligence) richiesta
- Sinergia con GDPR (sempre rilevante)

Pricing potenziale: assessment iniziale 5-15K EUR; remediation plan 30-100K EUR; ongoing compliance 5-20K/anno.
