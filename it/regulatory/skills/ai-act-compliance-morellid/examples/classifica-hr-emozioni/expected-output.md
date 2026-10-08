# Output atteso - classifica-sistema

# Classificazione AI Act - "TalentMatchPro"

**Data valutazione**: 2026-04-25
**Sistema valutato**: piattaforma video-interview AI con scoring linguistico + emotion recognition (facial + audio)
**Organizzazione**: TalentTech Srl (provider)

## Esito sintetico

**Classificazione**: **VIETATO (art. 5 par. 1 lett. f)** per la componente di riconoscimento emozioni in selezione del personale.

**ATTENZIONE**: il sistema **NON puo' essere immesso sul mercato** ne' messo in servizio nella sua configurazione attuale. La componente di riconoscimento emozioni in contesto di selezione del lavoro ricade nelle pratiche vietate.

**Possibili percorsi alternativi**: rimuovere la componente di riconoscimento emozioni e mantenere solo lo scoring linguistico.

## Motivazione

### In scope dell'AI Act?
**SI**. Sistema basato su ML che deduce output (score) da input (video, audio, testo).

### Pratica vietata art. 5?

**SI - lett. f) Riconoscimento emozioni in selezione del lavoro**

Testo art. 5 par. 1 lett. f:
> *"l'immissione sul mercato, la messa in servizio per tale finalita' specifica o l'uso di sistemi di IA per inferire le emozioni di una persona fisica nell'ambito del **luogo di lavoro** e degli istituti di istruzione, tranne laddove l'uso del sistema di IA sia destinato a essere messo in funzione o immesso sul mercato per motivi medici o di sicurezza"*

Analisi del caso:
- Il sistema **rileva emozioni** (entusiasmo, calma, tensione, fiducia, ansia, energia) dalla video-analisi facciale e dal tono di voce -> **inferenza di emozioni**
- Il contesto e' **selezione del personale**, che rientra nel "luogo di lavoro" inteso in senso ampio (la giurisprudenza e dottrina consolidate lo intendono includendo il processo di assunzione, non solo l'esercizio del rapporto)
- **Non si applicano le eccezioni**: motivi medici o sicurezza non sono in gioco

> **Cons. 44** dell'AI Act: *"L'uso di sistemi di IA per inferire le emozioni di persone fisiche sul luogo di lavoro e nell'ambito degli istituti di istruzione e' particolarmente preoccupante, dato lo squilibrio di potere..."*. Il considerando conferma l'interpretazione restrittiva.

**Conclusione**: la componente di emotion recognition (sia facciale sia da voce) rende il sistema VIETATO ex art. 5 par. 1 lett. f.

### GPAI?
N/A. Sistema specializzato.

### High-risk?
Non rilevante perche' la classificazione si ferma a "vietato" (art. 5 prevale). Tuttavia, se si rimuovesse la componente emozioni e si mantenesse solo lo scoring linguistico:
- Il sistema rientrerebbe in **Allegato III par. 4 lett. a** (sistemi destinati al reclutamento/selezione del personale)
- Sarebbe **HIGH-RISK** con tutti gli obblighi del provider art. 8-22

### Trasparenza art. 50?
N/A perche' il sistema e' vietato. (Anche se, se non vietato, ricadrebbe almeno in cat. C deployer per emotion recognition - ma il vietato vince.)

### Ruolo organizzazione
- TalentTech Srl: **provider** del sistema (lo sviluppa e lo immette sul mercato sotto proprio nome)

## Sanzioni applicabili in caso di violazione

Pratiche vietate art. 5: sanzione fino a **35 milioni EUR o 7% del fatturato globale annuo**, a seconda di quale sia maggiore (art. 99 par. 3).

Inoltre:
- Possibili azioni civili da parte di candidati discriminati
- Reputazionale grave
- Rischio di azioni concertate da autorita' di tutela dati e contrasto all'IA

## Percorsi di rimedio

### Opzione 1 - Rimozione componente emozioni
- Rimuovere completamente facial emotion recognition + voice emotion analysis
- Mantenere solo trascrizione + scoring linguistico delle risposte
- Il sistema risultante NON e' piu' vietato
- Diventa **HIGH-RISK** (Allegato III par. 4 lett. a)
- Tutti gli obblighi provider high-risk si applicano (vedi task `check-high-risk-provider.md`)
  - Sistema gestione rischi art. 9
  - Data governance art. 10 (anti-bias, fairness)
  - Documentazione tecnica art. 11
  - Conformity assessment art. 43
  - Marcatura CE
  - Iscrizione banca dati UE
  - Etc.

### Opzione 2 - Cambiare il contesto d'uso (NON consigliato)
Inferire emozioni e' vietato in lavoro/istruzione, ma non in altri settori. Tuttavia il riposizionamento "non per HR" lascia il rischio di uso improprio dei clienti -> rischio di violazione attribuibile al provider per design.

**Non raccomandato** salvo cambiamento profondo della finalita' di mercato e segregazione tecnica.

### Opzione 3 - Limitare a finalita' di sicurezza
Possibile solo se l'azienda dimostra che il sistema e' messo sul mercato per "motivi di sicurezza" (eccezione art. 5 par. 1 lett. f). Per HR non e' praticabile.

## Sinergie con altre normative

### GDPR
Anche se il sistema fosse non vietato, il trattamento dati biometrici (emozioni facciali) costituirebbe trattamento di **categorie particolari art. 9 GDPR**. Servirebbero:
- Base giuridica art. 9 par. 2 (rara da trovare per HR ordinaria)
- DPIA obbligatoria (tipologia 1, 2, 6, 7 Garante 467/2018)
- Provv. Garante 2018 su biometria potrebbe aggiungere prescrizioni

### Statuto dei Lavoratori (L. 300/1970)
Art. 4: divieto di controllo a distanza dei lavoratori, salvo accordo sindacale o autorizzazione INL. Per il pre-assunzione il divieto non si applica direttamente, ma per uso post-assunzione si.

### Direttiva (UE) 2019/1152 (condizioni di lavoro trasparenti) e D.Lgs. 104/2022
Obbligo di informazione del candidato sui sistemi automatizzati di selezione. Anche se sistema vietato, l'obbligo informativo sussiste.

### Codice di Deontologia Privacy in materia di lavoro
Il Garante ha emanato provvedimenti specifici sulla privacy nei rapporti di lavoro che possono aggiungere prescrizioni.

## Limiti di questa classificazione

- **Forte certezza** sull'applicabilita' della lett. f) art. 5 nel caso analisi emozioni in selezione del personale.
- Lievemente meno certezza sul perimetro esatto di "luogo di lavoro" - ma la prassi consolidata include selezione/pre-assunzione.
- Le linee guida Commissione su pratiche vietate (febbraio 2025) confermano l'interpretazione restrittiva.

## Rinvio al consulente legale

**E' altamente raccomandato un parere legale specialistico immediato prima di:**
- Continuare lo sviluppo della componente emozioni
- Effettuare investimenti commerciali sulla configurazione attuale
- Comunicare il prodotto al mercato

**Suggerimento operativo per TalentTech Srl**:
1. **STOP allo sviluppo** della componente emozioni
2. Validare la riprogettazione (Opzione 1) con consulente legale + DPO
3. Pivot strategico: sistema "compliant" focalizzato su scoring linguistico + competenze tecniche, marketed come AI ethics-first
4. La compliance high-risk Allegato III sara' obbligatoria entro **02/12/2027** (rinvio Digital Omnibus provvisorio, era 02/08/2026) -> piu' tempo per implementare i requisiti, ma riconfermare alla pubblicazione GUUE

**Sanzioni in caso di violazione delle pratiche vietate**: fino a 35M EUR o 7% del fatturato globale.
