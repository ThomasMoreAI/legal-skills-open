# Task: Verifica obblighi provider sistemi high-risk (art. 8-22)

Per un provider (fornitore) di un sistema AI classificato come high-risk, verifica la conformita' agli obblighi della Sezione 2 e 3 del Capo III dell'AI Act.

## Obiettivo

Produrre una gap analysis strutturata che indichi, per ciascun obbligo del provider high-risk, se e' soddisfatto / parzialmente / non soddisfatto, con riferimento normativo preciso e raccomandazioni.

Pre-requisito: classificazione confermata via `classifica-sistema.md` (sistema high-risk + ruolo provider).

## Input richiesti

- Descrizione del sistema (vedi classifica-sistema)
- Stato della documentazione tecnica
- Stato del sistema gestione rischi
- Stato del QMS (Quality Management System)
- Stato della valutazione di conformita'
- Marcatura CE applicata? Banca dati UE registrata?
- Sistema di sorveglianza post-market

## Fonti

Leggere prima:
- `references/estratti/ai-act-art-6-9-classificazione-high-risk.md` - art. 6, 9
- L'estratto NON include art. 10-22 (data governance, doc tecnica, log, trasparenza, sorveglianza umana, accuratezza, QMS, conservazione doc, conformity assessment, marcatura CE, registrazione). Questi sono nella PDF originale (`not_in_repo/ai-act-it-eurlex.pdf`) - per la skill richiamarli per riferimento e citare gli articoli precisi.

## Procedura - Checklist obblighi provider

### Sezione 2 - Requisiti tecnici (art. 8-15)

#### Art. 8 - Conformita' generale
- [ ] I requisiti della Sezione 2 sono soddisfatti tenendo conto della finalita' del sistema e dello stato dell'arte

#### Art. 9 - Sistema di gestione dei rischi
- [ ] Sistema istituito, attuato, documentato, mantenuto
- [ ] Processo iterativo continuo coprendo l'intero ciclo di vita
- [ ] Identificazione/analisi/stima rischi noti e prevedibili
- [ ] Misure mirate di gestione rischio basate su stato dell'arte
- [ ] Test in condizioni rappresentative
- [ ] Considerazioni speciali per gruppi vulnerabili e minori

#### Art. 10 - Dati e governance dei dati
- [ ] Dataset di training, validation e test soggetti a pratiche di governance dei dati
- [ ] Esame di scelte progettuali, raccolta dati, elaborazione, ipotesi
- [ ] Pertinenza, rappresentativita', assenza di errori, completezza
- [ ] Bias mitigation
- [ ] Trattamento di categorie particolari per la mitigazione di bias (par. 5 - eccezione GDPR specifica)

#### Art. 11 - Documentazione tecnica
- [ ] Documentazione tecnica redatta prima dell'immissione sul mercato
- [ ] Tenuta aggiornata
- [ ] Conformita' Allegato IV
- [ ] Per PMI/start-up: forma semplificata possibile (par. 1)

#### Art. 12 - Conservazione dei log
- [ ] Sistema progettato per registrare automaticamente gli eventi (log)
- [ ] Log assicurano un livello adeguato di tracciabilita'
- [ ] Per identificazione biometrica remota Allegato III par. 1 lett. a: minimi specifici (par. 3)

#### Art. 13 - Trasparenza e fornitura di informazioni ai deployer
- [ ] Sistema progettato per essere comprensibile dal deployer
- [ ] Istruzioni d'uso conformi al par. 3 (caratteristiche, finalita', accuratezza, sorveglianza umana, ciclo di vita, mantenimento, etc.)

#### Art. 14 - Sorveglianza umana
- [ ] Sistema progettato per essere effettivamente sorvegliato
- [ ] Misure proporzionate ai rischi, all'autonomia, al contesto d'uso
- [ ] Capacita' di "human in the loop" o "human on the loop" come applicabile
- [ ] Sistemi alto rischio Allegato III par. 1 lett. a (identificazione biometrica): doppia verifica umana (par. 5)
- [ ] Italia: omettere le misure di sicurezza o di sorveglianza umana previste per la progettazione e l'immissione sul mercato è reato (art. 437-bis c.p., D.Lgs. 160/2026) se ne deriva pericolo per vita o incolumità; i parametri di sorveglianza umana sono tra i documenti che il giudice civile può ordinare di esibire (art. 17). Vedi `check-profili-nazionali-italia.md`

#### Art. 15 - Accuratezza, robustezza, cybersicurezza
- [ ] Livelli adeguati di accuratezza, robustezza e cybersicurezza
- [ ] Coerenza durante tutto il ciclo di vita
- [ ] Resilienza a errori, guasti, incoerenze
- [ ] Misure tecniche/organizzative per resilienza a cyber attacchi
- [ ] Robustezza vs **adversarial inputs**, **data poisoning**, **model evasion**

### Sezione 3 - Obblighi del provider (art. 16-22)

#### Art. 16 - Obblighi generali del provider
Conformita' a tutta la Sezione 2 + responsabilita' attribuibili al provider.

#### Art. 17 - Sistema di gestione della qualita' (QMS)
- [ ] QMS istituito, documentato, attuato in proporzione alla dimensione dell'organizzazione
- [ ] Strategie regolatorie incluse: identificazione, attuazione di norme armonizzate
- [ ] Tecniche, procedure e azioni sistematiche per progettazione/sviluppo
- [ ] Esame, prova, validazione (artt. 9, 10, 11, 13, 14, 15)
- [ ] Procedure tecniche e di sicurezza dati
- [ ] Sistema di reporting incidenti gravi
- [ ] Per PMI: conformita' QMS in forma semplificata possibile (par. 4)

#### Art. 18 - Conservazione della documentazione
- [ ] Documentazione tecnica conservata per **10 anni** dall'immissione sul mercato/messa in servizio
- [ ] Disponibile per le autorita'

#### Art. 19 - Log generati automaticamente
- [ ] Log conservati per periodo adeguato alla finalita' (almeno **6 mesi** salvo diversa norma)

#### Art. 20 - Misure correttive e dovere di informazione
- [ ] Procedura per ritiro/richiamo/disabilitazione in caso di non conformita' rilevata
- [ ] Informazione immediata distributori, deployer, autorizzato rappresentante, importatore

#### Art. 21 - Cooperazione con le autorita' competenti
- [ ] Risposta a richieste autorita' su sistema e conformita'

#### Art. 22 - Rappresentante autorizzato (per provider extra-UE)
- [ ] Provider stabiliti fuori UE: nominano rappresentante autorizzato in UE
- [ ] Mandato scritto

### Capo III Sezione 4 - Conformity Assessment + post-market

#### Art. 43 - Procedura di valutazione della conformita'
- [ ] Selezione procedura corretta:
  - **Allegato VI** (controllo interno): valida per la maggior parte high-risk Allegato III, salvo Allegato III par. 1 (biometria)
  - **Allegato VII** (notifica organismo per QMS + valutazione doc tecnica): obbligatoria per Allegato III par. 1 (biometria) + alcuni casi specifici
  - Per high-risk Allegato I (componenti sicurezza): conformity assessment del prodotto principale (es. dispositivi medici - MDR), con AI Act integrato

#### Art. 47 - Dichiarazione di conformita' UE
- [ ] DoC redatta, in italiano + lingua del mercato
- [ ] Conservata 10 anni

#### Art. 48 - Marcatura CE
- [ ] Marcatura CE applicata visibilmente, leggibilmente, in modo indelebile
- [ ] Per sistemi solo digitali: marcatura CE digitale

#### Art. 49 - Registrazione nella banca dati UE
- [ ] Provider iscritto nella banca dati UE
- [ ] Sistema iscritto prima dell'immissione sul mercato/messa in servizio

#### Art. 72 - Sorveglianza post-market
- [ ] Sistema di post-market monitoring documentato
- [ ] Raccolta dati su uso reale, problemi, performance
- [ ] Trigger per azioni correttive

#### Art. 73 - Reporting di incidenti gravi
- [ ] Notifica all'autorita' di vigilanza nazionale **entro 15 giorni** da consapevolezza
- [ ] Per incidenti che risultano in morte: **entro 10 giorni**

## Output strutturato

```markdown
# Verifica obblighi provider high-risk - [nome sistema]

**Data verifica**: [data]
**Sistema**: [descrizione]
**Provider**: [organizzazione]
**Classificazione**: HIGH-RISK [via 1 / via 2 - settore Allegato III]

## Sintesi

- Obblighi verificati: 18+
- Soddisfatti: X
- Parzialmente: Y
- Non soddisfatti: Z

**Esito**: [CONFORME | CONFORME CON GAP MINORI | GAP SOSTANZIALI | NON CONFORME]

## Sezione 2 - Requisiti tecnici

| Art. | Requisito | Stato | Note |
|------|-----------|-------|------|
| 9 | Sistema gestione rischi | OK / Gap | ... |
| 10 | Data governance | ... | ... |
| 11 | Documentazione tecnica (Allegato IV) | ... | ... |
| 12 | Log automatici | ... | ... |
| 13 | Trasparenza ai deployer (istruzioni) | ... | ... |
| 14 | Sorveglianza umana | ... | ... |
| 15 | Accuratezza/robustezza/cybersicurezza | ... | ... |

## Sezione 3 - Obblighi provider

| Art. | Requisito | Stato | Note |
|------|-----------|-------|------|
| 17 | QMS | ... | ... |
| 18 | Conservazione doc 10 anni | ... | ... |
| 19 | Log min 6 mesi | ... | ... |
| 20 | Misure correttive | ... | ... |
| 21 | Cooperazione autorita' | ... | ... |
| 22 | Rappresentante autorizzato (se extra-UE) | ... | ... |

## Conformity assessment + marcatura CE + registrazione

| Art. | Requisito | Stato | Note |
|------|-----------|-------|------|
| 43 | Procedura conformity assessment | ... | ... |
| 47 | Dichiarazione di conformita' | ... | ... |
| 48 | Marcatura CE | ... | ... |
| 49 | Registrazione banca dati UE | ... | ... |
| 72 | Post-market monitoring | ... | ... |
| 73 | Reporting incidenti gravi | ... | ... |

## Gap principali rilevati

| # | Articolo | Gap | Priorita' | Tempi previsti |
|---|----------|-----|-----------|-----------------|
| 1 | Art. 9 | Sistema gestione rischi non documentato formalmente | **Alta** | Pre-mercato |
| ... |

## Raccomandazioni

[Lista per priorita']

## Roadmap di compliance suggerita

### Fase 1 (entro **2 dicembre 2027** per Allegato III, era 2 agosto 2026 - rinvio Digital Omnibus provvisorio; per Allegato I entro **2 agosto 2028**, era 2 agosto 2027)
- Documentazione tecnica art. 11 + Allegato IV
- Sistema gestione rischi art. 9
- QMS art. 17
- Data governance art. 10

### Fase 2
- Conformity assessment
- Marcatura CE
- Registrazione banca dati

### Fase 3 (continua)
- Post-market monitoring
- Reporting incidenti

## Sinergia con altre normative

- **GDPR**: dati personali nel sistema -> Registro art. 30 + DPIA art. 35 (e per deployer servizi essenziali, FRIA integrato art. 27)
- **MDR/IVDR** (dispositivi medici): integrazione con conformity assessment esistente
- **NIS2** per cybersicurezza enterprise: integrazione con misure art. 15
- **Codice Privacy italiano** D.Lgs. 196/2003: norme nazionali
- **D.Lgs. 160/2026**: reato 437-bis c.p., 231 art. 25-vicies, regole civili (esibizione di log, risk management, documentazione tecnica e parametri di sorveglianza umana; nesso causale presunto; conformità certificata non esimente). Vedi `check-profili-nazionali-italia.md`

## Limiti

- Verifica documentale, non testa il sistema in funzione
- Non sostituisce conformity assessment dell'organismo notificato (art. 43)
- Le norme armonizzate ETSI/CEN-CENELEC sono in sviluppo - skill non aggiornata in tempo reale

## Rinvio

**La conformita' AI Act per high-risk e' processo complesso che richiede:**
- Consulente legale specializzato in diritto digitale UE
- Per Allegato III par. 1 (biometria) + Allegato I: organismo notificato
- DPO se trattamento dati personali
- Esperti tecnici di AI/ML su data governance, robustezza, cybersicurezza
- Revisione interna di QMS

**Sanzioni**: fino a 15M EUR o 3% del fatturato globale annuo per violazioni high-risk.
```

## Casi limite

### Provider che non ha mai immesso sistemi high-risk
Roadmap completa da zero. Suggerire:
1. Ingaggio consulente legale + ufficio compliance
2. Mappatura ciclo di vita prodotto
3. Implementazione QMS prima di tutto
4. Documentazione tecnica strutturata in parallelo a sviluppo

### Sistema gia' sul mercato pre-AI Act
Tempistiche transitorie applicabili per sistemi gia' immessi. Verificare art. 111 (transitional provisions) e adattare roadmap.

### Modifiche sostanziali (art. 25)
Un deployer/distributore che modifica sostanzialmente il sistema o lo rebrand diventa **provider** ai sensi del regolamento. Tutti gli obblighi del provider si applicano.

## Limiti di questo task

- Solo lato provider, deployer separato (vedi `check-deployer-obligations.md`)
- Norme armonizzate ETSI/CEN-CENELEC sono in sviluppo - va monitorato
- Linee guida Commissione su classificazione e operativita' in via di pubblicazione

## Esempi

Vedi `examples/`:
- `provider-credit-scoring-gap/` - provider sistema credit scoring (Allegato III par. 5 lett. b) con gap multipli su QMS e doc tecnica
