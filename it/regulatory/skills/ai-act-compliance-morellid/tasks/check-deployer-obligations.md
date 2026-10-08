# Task: Verifica obblighi deployer (art. 26-27 incluso FRIA)

Per un deployer di sistema AI high-risk, verifica gli obblighi specifici (art. 26) e quando applicabile la FRIA (art. 27).

## Obiettivo

Produrre una checklist conforme degli obblighi del deployer + valutare se serve il FRIA (Fundamental Rights Impact Assessment) e in caso strutturarlo.

## Input richiesti

- Descrizione sistema usato (gia' classificato high-risk via `classifica-sistema.md`)
- Identita' del deployer (organismo pubblico? privato che fornisce servizi pubblici? privato standard?)
- Settore Allegato III in cui ricade
- Persone fisiche interessate (categorie, vulnerabili?)
- Provider che fornisce il sistema (per richiamare istruzioni d'uso art. 13)

## Fonti

Leggere prima: `references/estratti/ai-act-art-26-27-deployer-fria.md`

## Procedura - Obblighi art. 26

### Par. 1 - Uso conforme a istruzioni
- [ ] Misure tecniche e organizzative per garantire uso conforme a istruzioni d'uso
- [ ] Sistema usato per finalita' previste

### Par. 2 - Sorveglianza umana
- [ ] Persone fisiche specificamente designate alla sorveglianza umana
- [ ] Possesso di competenza, formazione, autorita'
- [ ] Risorse di supporto
- [ ] Italia: l'omissione intenzionale della sorveglianza umana da parte dell'utilizzatore professionale di un sistema ad alto rischio è reato (art. 437-bis c.4 c.p., D.Lgs. 160/2026) se ne deriva pericolo per vita o incolumità; vedi `check-profili-nazionali-italia.md`

### Par. 4 - Dati di input (se controllati dal deployer)
- [ ] Rilevanza e rappresentativita' rispetto alla finalita'

### Par. 5 - Monitoraggio funzionamento
- [ ] Monitoraggio attivo sul funzionamento secondo istruzioni
- [ ] Procedura per informare il provider in caso di anomalie (art. 72)
- [ ] Sospensione uso e notifica autorita' in caso di rischio per salute/sicurezza/diritti

### Par. 6 - Conservazione log
- [ ] Log automatici conservati per periodo adeguato, **almeno 6 mesi**

### Par. 7 - Lavoratori (se uso in luogo di lavoro)
- [ ] Informazione preventiva ai rappresentanti dei lavoratori
- [ ] Informazione preventiva ai lavoratori interessati

### Par. 8 - Registrazione banca dati UE (solo per PA e istituzioni UE)
- [ ] Se deployer e' autorita' pubblica o istituzione/organo/organismo UE: registrazione banca dati UE art. 49
- [ ] Verifica che il sistema sia registrato prima dell'uso

### Par. 9 - DPIA GDPR
- [ ] Uso delle informazioni art. 13 per la DPIA quando trattati dati personali

### Par. 11 - Informazione persone fisiche interessate
- [ ] Informazione che sono soggette al sistema high-risk per decisioni o assistenza decisioni

### Par. 12 - Cooperazione autorita'
- [ ] Disponibilita' a cooperare con autorita' competenti

## Procedura - FRIA art. 27 (quando applicabile)

### Quando e' obbligatorio

Il FRIA e' obbligatorio per i deployer che siano:
- Organismi di diritto pubblico
- Enti privati che forniscono servizi pubblici
- Deployer di sistemi Allegato III par. 5 lett. b) (credit scoring) e c) (insurance pricing)

Esclusi dall'obbligo FRIA: solo i sistemi per il settore **Allegato III punto 2 (infrastrutture critiche)** sono esplicitamente esclusi dal testo dell'art. 27 par. 1. I deployer pubblici di sistemi per contrasto (pt. 6) o migrazione/asilo/frontiere (pt. 7) che rientrano nella definizione di "organismo di diritto pubblico" sono soggetti all'obbligo.

### Contenuti minimi (par. 1 lett. a-f)

- [ ] Descrizione processi del deployer in cui il sistema sara' usato
- [ ] Periodo e frequenza d'uso
- [ ] Categorie persone fisiche e gruppi interessati
- [ ] Rischi specifici di danno alle categorie identificate
- [ ] Misure di sorveglianza umana per il caso d'uso del deployer
- [ ] Misure in caso di materializzazione dei rischi (governance, reclamo)

### Sinergia con DPIA (par. 4)

Se gli obblighi FRIA sono gia' soddisfatti da DPIA GDPR (art. 35) o LED (art. 27), il FRIA **integra** la DPIA. In pratica: documento unico con sezioni dedicate.

### Notifica autorita' (par. 3)

Risultati FRIA da notificare via modello standardizzato dall'AI Office (in via di sviluppo).

## Output strutturato

```markdown
# Verifica obblighi deployer high-risk - [contesto]

**Data verifica**: [data]
**Sistema usato**: [descrizione + classificazione + provider]
**Deployer**: [organizzazione + ruolo - pubblico/servizi pubblici/privato standard]
**Settore Allegato III**: [par. X lett. Y]

## Esito sintetico

**Status compliance**: [CONFORME / CONFORME CON GAP / GAP SOSTANZIALI / NON CONFORME]

**FRIA richiesto**: [SI / NO]
**FRIA stato**: [Effettuato / In corso / Da fare / N/A]

## Verifica obblighi art. 26

| Par. | Obbligo | Stato | Note |
|------|---------|-------|------|
| 1 | Uso conforme istruzioni | ... | ... |
| 2 | Sorveglianza umana - persone designate | ... | ... |
| 4 | Dati input (se controllati dal deployer) | ... | ... |
| 5 | Monitoraggio funzionamento + escalation | ... | ... |
| 6 | Log >= 6 mesi | ... | ... |
| 7 | Informazione lavoratori (se uso in luogo di lavoro) | ... | ... |
| 8 | Registrazione banca dati UE (se PA/ist. UE) | ... | ... |
| 9 | DPIA GDPR (se dati personali) | ... | ... |
| 11 | Informazione persone fisiche interessate | ... | ... |
| 12 | Cooperazione autorita' | ... | ... |

## FRIA - se applicabile

[Sezione separata con i 6 contenuti minimi par. 1 lett. a-f]

| Lett. | Contenuto | Stato | Note |
|-------|-----------|-------|------|
| a | Descrizione processi del deployer | ... | ... |
| b | Periodo e frequenza d'uso | ... | ... |
| c | Categorie persone interessate | ... | ... |
| d | Rischi specifici di danno | ... | ... |
| e | Misure sorveglianza umana | ... | ... |
| f | Misure in caso di materializzazione rischi | ... | ... |

Sinergia con DPIA: [Si - documento integrato / No - separati]

## Gap principali

[Lista per priorita']

## Raccomandazioni

[Roadmap]

## Sinergia con altre normative

- GDPR art. 30 (Registro) + 35 (DPIA): vedi skill `gdpr-registro-dpia`
- LED (D.Lgs. 51/2018): per autorita' di contrasto
- D.Lgs. 196/2003 art. 154-bis: per DPO settore pubblico
- D.Lgs. 160/2026: reato 437-bis c.p., 231 art. 25-vicies, accesso alle prove e presunzione del nesso causale nelle azioni di risarcimento; per le Forze di polizia revisione umana qualificata e tracciata degli output (art. 3 c.4). Vedi `check-profili-nazionali-italia.md`

## Limiti

- Verifica documentale, non sul reale uso del sistema
- Non sostituisce parere del DPO o consulente legale specializzato
- Modello FRIA standardizzato dell'AI Office in via di pubblicazione

## Rinvio

**Per deployer di sistemi high-risk + dati personali**, e' necessaria una valutazione integrata che coinvolga:
- DPO (sempre per DPIA, fortemente consigliato per FRIA)
- Consulente legale specializzato
- Esperti tecnici (per misure sorveglianza umana e log)
- Stakeholder interni (HR, IT, sicurezza, business)

Sanzioni: fino a 15M EUR o 3% del fatturato globale annuo (art. 99 par. 4).
```

## Casi tipici

### PA italiana che usa sistema AI per assistenza pubblica (Allegato III par. 5 lett. a)
- Deployer **organismo pubblico**
- Tutti gli obblighi art. 26 + FRIA art. 27 obbligatorio
- Sinergia con AgID (linee guida PA)

### Banca italiana che usa credit scoring fornito da terzo (Allegato III par. 5 lett. b)
- Deployer **privato** ma **soggetto a FRIA obbligatorio** (per il caso specifico par. 5 lett. b)
- Sinergia con normativa Banca d'Italia + Codice deontologia centrali rischi

### Azienda manifatturiera che usa sistema HR di reclutamento AI (Allegato III par. 4)
- Deployer privato, **non obbligato a FRIA** (non e' organismo pubblico ne' privato che fornisce servizi pubblici, e Allegato III par. 4 non rientra tra le categorie art. 27 par. 1)
- Obblighi art. 26 si applicano (sorveglianza umana, informazione lavoratori, DPIA GDPR per dati personali)

### Comune che usa sistema biometrico controllo accessi dipendenti (Allegato III par. 1 lett. b)
- Deployer pubblico
- FRIA + DPIA obbligatori (sinergia)
- Anche art. 4 dello Statuto dei Lavoratori per controllo a distanza
- Tipologia 5 Provv. Garante 467/2018 -> conferma DPIA obbligatoria

## Limiti

- Lista non esaustiva: norme nazionali italiane possono aggiungere obblighi
- Modello FRIA standardizzato in attesa di pubblicazione AI Office
- Linee guida Commissione su FRIA in preparazione

## Esempi

Vedi `examples/`:
- `deployer-pa-assistenza/` - PA che usa AI per ammissibilita' assistenza pubblica (FRIA obbligatorio)
