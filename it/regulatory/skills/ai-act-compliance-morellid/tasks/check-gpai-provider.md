# Task: Verifica obblighi provider GPAI (art. 53-55)

Per un fornitore (provider) di un modello GPAI (General Purpose AI), verifica gli obblighi standard art. 53 e gli aggiuntivi art. 55 se rischio sistemico.

## Obiettivo

Checklist conforme degli obblighi GPAI provider + identificazione del livello (standard / rischio sistemico) + raccomandazioni operative.

## Input richiesti

- Descrizione del modello (architettura, capacita', mercati di uso a valle)
- FLOP di addestramento (per soglia rischio sistemico 10^25)
- Licenza (open-source vs proprietario)
- Dati di addestramento (sintesi pubblica gia' fatta?)
- Documentazione tecnica disponibile
- Politica copyright e gestione data scraping

## Fonti

Leggere prima: `references/estratti/ai-act-art-51-55-gpai.md`

## Procedura

### Passo 1 - Conferma natura GPAI

Il modello qualifica come GPAI (art. 3 par. 63) se:
- Significativa generalita'
- Esegue competentemente un'**ampia gamma di compiti distinti** indipendentemente da come e' immesso sul mercato
- Puo' essere integrato in vari sistemi/applicazioni a valle

Esempi: GPT-4/5, Claude, Gemini, Llama, Mistral.

NON GPAI: modelli specializzati single-purpose (es. classificatore binario, modello di riconoscimento facciale specifico).

### Passo 2 - Determina rischio sistemico (art. 51)

| Criterio | Risultato | Conseguenza |
|----------|-----------|-------------|
| FLOP > 10^25 | Si / No | Presunzione rischio sistemico |
| Designazione Commissione | Si / No | Rischio sistemico per atto formale |

Se rischio sistemico = SI -> applicano sia art. 53 sia art. 55.

### Passo 3 - Verifica obblighi base art. 53 (tutti i provider GPAI)

#### Par. 1 lett. a) - Documentazione tecnica
- [ ] Documentazione tecnica del modello redatta e tenuta aggiornata
- [ ] Include processo addestramento e prova
- [ ] Include risultati valutazione
- [ ] Conformita' Allegato XI (informazioni minime)
- [ ] Disponibile per AI Office / autorita' nazionali su richiesta

#### Par. 1 lett. b) - Informazioni a fornitori a valle
- [ ] Documentazione/informazioni rese disponibili ai fornitori che integrano il modello
- [ ] Conformita' Allegato XII (informazioni per integratori)
- [ ] Sufficiente per comprendere capacita' e limitazioni

#### Par. 1 lett. c) - Politica copyright
- [ ] Politica scritta di rispetto del diritto d'autore UE
- [ ] In particolare attuazione della **riserva di diritti art. 4 par. 3 dir. 2019/790** (DSM Directive) tramite tecnologie all'avanguardia
- [ ] Identificazione e attuazione del rights reservation (es. robots.txt + meccanismi machine-readable per opt-out)

#### Par. 1 lett. d) - Sintesi pubblica training data
- [ ] Sintesi pubblica del materiale di addestramento
- [ ] Sufficiente dettaglio
- [ ] Conforme al modello pubblicato dall'AI Office

#### Par. 2 - Eccezione open-source
Se il modello e' rilasciato come open-source con accesso/uso/modifica/distribuzione + pesi pubblici:
- Esenzione lett. a) e b)
- **Eccezione all'eccezione**: se ha rischio sistemico, gli obblighi si applicano comunque
- Lett. c) (copyright) e d) (sintesi training): si applicano sempre

### Passo 4 - Se rischio sistemico: obblighi aggiuntivi art. 55

#### Par. 1 lett. a) - Valutazione del modello
- [ ] Valutazione secondo protocolli/strumenti standardizzati
- [ ] Inclusione di **adversarial testing** (red teaming)
- [ ] Documentazione risultati

#### Par. 1 lett. b) - Valutazione e mitigazione rischi sistemici
- [ ] Identificazione fonti di rischio
- [ ] Misure per attenuare rischi sistemici a livello UE
- [ ] Documentazione del processo

#### Par. 1 lett. c) - Reporting incidenti gravi
- [ ] Procedura tracciamento incidenti
- [ ] Documentazione
- [ ] Reporting all'AI Office (e autorita' nazionali se del caso) **senza indebito ritardo**

#### Par. 1 lett. d) - Cybersicurezza
- [ ] Protezione cybersicurezza adeguata del modello
- [ ] Protezione dell'**infrastruttura fisica** (datacenter, training infra, model serving)

#### Par. 2 - Codici di condotta
- [ ] Eventuale adesione al Code of Practice GPAI dell'AI Office (in via di sviluppo)

### Passo 5 - Notifica art. 51 par. 1 lett. a

- [ ] Notifica alla Commissione **entro 2 settimane** dal raggiungimento della soglia FLOP o conoscenza che la raggiungera'

## Output strutturato

```markdown
# Verifica obblighi provider GPAI - [nome modello]

**Data verifica**: [data]
**Modello**: [nome + caratteristiche]
**Provider**: [organizzazione]

## Classificazione

**Tipo**: GPAI [standard / con rischio sistemico]
**Soglia FLOP**: [stima] [sopra/sotto 10^25]
**Open-source**: [Si / No / Open-weights con restrizioni]
**Eccezione open-source applicabile (art. 53 par. 2)**: [Si / No / Parziale]

## Verifica obblighi art. 53 (tutti)

| Lett. | Obbligo | Stato | Note |
|-------|---------|-------|------|
| a | Documentazione tecnica + Allegato XI | ... | ... |
| b | Informazioni a fornitori a valle + Allegato XII | ... | ... |
| c | Politica copyright + opt-out art. 4 DSM | ... | ... |
| d | Sintesi pubblica training data | ... | ... |

Eccezione open-source applicata: [SI/NO + motivazione]

## Verifica obblighi art. 55 (solo se rischio sistemico)

| Lett. | Obbligo | Stato | Note |
|-------|---------|-------|------|
| a | Valutazione modello + adversarial testing | ... | ... |
| b | Valutazione e mitigazione rischi sistemici UE | ... | ... |
| c | Reporting incidenti gravi all'AI Office | ... | ... |
| d | Cybersicurezza modello + infrastruttura | ... | ... |

## Notifica art. 51 par. 1 lett. a

- Notifica Commissione entro 2 settimane: [Effettuata / Da fare / N/A]

## Gap rilevati

[Lista per priorita']

## Raccomandazioni

[Roadmap di compliance]

## Roadmap di compliance suggerita

### Fase 1 - documentazione base (immediata se non gia' fatta)
- Documentazione tecnica art. 53 lett. a)
- Sintesi pubblica training data art. 53 lett. d)
- Politica copyright art. 53 lett. c)

### Fase 2 - integrazione a valle
- Documentazione per fornitori a valle art. 53 lett. b) (Allegato XII)

### Fase 3 - se rischio sistemico
- Valutazione modello + adversarial testing
- Valutazione rischi sistemici
- Procedura reporting incidenti
- Misure cybersicurezza
- Adesione Code of Practice (se utile)

## Sinergia altri obblighi

- **AI Act high-risk a valle**: se il GPAI e' integrato in sistema high-risk, il fornitore del sistema (deployer del GPAI) ha obblighi propri
- **Trasparenza art. 50 par. 2**: per modelli che generano contenuti sintetici, marcatura machine-readable (anche per GPAI)
- **GDPR**: training data spesso include dati personali -> rilevanza politica copyright e basi giuridiche

## Limiti

- Code of Practice GPAI in via di pubblicazione - skill da aggiornare
- Modello standard sintesi training data ancora in via di rilascio AI Office
- Linee guida Commissione su soglia FLOP (art. 51 par. 2) potrebbero affinare la metodologia di calcolo

## Sanzioni

- Violazione obblighi art. 53/55: fino a **15 milioni EUR o 3% del fatturato globale** (art. 101)
```

## Casi tipici

### Provider proprietario di LLM ~10^25 FLOP
- GPAI con rischio sistemico
- Tutti gli obblighi art. 53 + 55
- Notifica Commissione entro 2 settimane dalla soglia
- Tipico: aderire al Code of Practice quando disponibile

### Provider di modello open-source ~10^24 FLOP
- GPAI standard, open-source -> eccezione lett. a) e b)
- Si applicano comunque lett. c) copyright + lett. d) sintesi training

### Provider di modello specializzato (NON GPAI)
- Non sono provider GPAI, non si applica art. 53/55
- Possono essere provider di sistema high-risk se integrato in casi Allegato III

### Integratore italiano di Llama (Meta) per ChatBot enterprise
- L'integratore NON e' provider GPAI (Meta lo e')
- L'integratore e' provider di sistema (high-risk se Allegato III, altrimenti trasparenza/minimo)
- Documentazione che riceve dal Meta (Allegato XII) e' input per gli obblighi propri

## Limiti del task

- Norme dettagliate Allegato XI/XII non riprodotte negli estratti - serve consultare PDF originale
- Code of Practice GPAI in via di sviluppo
- Linee guida Commissione attese 2025-2026

## Esempi

(Da costruire in iterazioni successive - per ora la skill copre la procedura strutturale)
