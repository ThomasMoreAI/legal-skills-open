# Task: Verifica completezza Registro trattamenti (art. 30 GDPR)

Verifica che un Registro delle attivita' di trattamento esistente contenga tutte le voci obbligatorie previste dall'art. 30 par. 1 (titolare) o par. 2 (responsabile) del GDPR.

## Obiettivo

Produrre un report che, per ciascun trattamento del Registro, indichi presenza/assenza/inadeguatezza delle 7 voci minime (titolare) o 4 voci minime (responsabile), con citazione normativa.

## Input richiesti

- Il Registro completo (in formato testuale, markdown, tabella, JSON, o altro leggibile)
- Tipologia: il Registro e' del titolare o del responsabile?
- Eventualmente: dimensione dell'organizzazione (per valutare se art. 30 par. 5 si applicherebbe)

## Fonti

Leggere prima:
- `references/estratti/gdpr-art-30.md` - 7 contenuti minimi del titolare e 4 del responsabile

## Procedura

### Passo 1 - Verifica intestazione

Per ogni Registro, l'intestazione deve contenere:
- [ ] Identificazione titolare (denominazione, CF/P.IVA, sede)
- [ ] Eventuale contitolare e accordo
- [ ] Eventuale rappresentante UE
- [ ] DPO se designato (nome + contatti)

### Passo 2 - Per ogni trattamento, verificare le 7 voci (titolare) o 4 (responsabile)

#### Per Registro del TITOLARE (art. 30 par. 1):

| Voce | Lett. | Verifica |
|------|-------|----------|
| 1 | a) | Identificazione titolare (gia' coperta in intestazione - OK) |
| 2 | b) | **Finalita'** del trattamento - deve essere specifica, non "esigenze aziendali" |
| 3 | c) | **Categorie interessati** + **categorie dati personali** - distinte |
| 4 | d) | **Categorie destinatari** - interni e esterni, con identificazione paesi terzi |
| 5 | e) | **Trasferimenti extra-UE** se applicabili - paese + garanzia (adeguatezza/SCC/BCR/deroga) |
| 6 | f) | **Termini di conservazione** - "ove possibile" significa che si fa il massimo sforzo, non si omettono se determinabili |
| 7 | g) | **Misure di sicurezza** tecniche + organizzative - rinvio art. 32 |

#### Per Registro del RESPONSABILE (art. 30 par. 2):

| Voce | Lett. | Verifica |
|------|-------|----------|
| 1 | a) | Identificazione responsabile + titolari per cui agisce + DPO se designato |
| 2 | b) | **Categorie di trattamenti** effettuati per conto di ciascun titolare |
| 3 | c) | **Trasferimenti extra-UE** con relative garanzie |
| 4 | d) | **Misure di sicurezza** tecniche e organizzative |

### Passo 3 - Pattern di problemi comuni da identificare

#### Voce b) finalita': pattern problematici
- "Gestione attivita' aziendale" - **troppo generica**
- "Per finalita' connesse al rapporto" - **non descrive cosa si fa**
- "Esigenze gestionali e organizzative" - **boilerplate**

Pattern accettabili: "Gestione del rapporto di lavoro subordinato (assunzione, busta paga, contributi)", "Invio newsletter promozionale ai clienti che hanno prestato consenso".

#### Voce c) categorie interessati e dati: pattern problematici
- "Tutti i dati necessari" - **non descrive le categorie**
- "Persone interessate" - **circolare**
- Mescolanza di categorie e finalita' - tenerle separate

Pattern accettabili: "Interessati: dipendenti, ex-dipendenti, candidati. Dati: anagrafici, contatto, fiscali, contributivi, sanitari (medicina del lavoro), ...".

#### Voce d) destinatari: pattern problematici
- "Soggetti autorizzati" - **non specifica chi**
- "Eventuali terzi" - **non utile**
- Omissione di provider cloud (sono destinatari, non strumenti)

Pattern accettabili: "Interni: HR, IT, direzione. Esterni: consulente del lavoro Studio X (responsabile), provider payroll Y (responsabile), Inps, Agenzia Entrate".

#### Voce e) trasferimenti extra-UE: pattern problematici
- Omissione totale quando il provider cloud ha datacenter fuori UE
- "Conformi al GDPR" senza indicare quale base specifica
- SCC vecchi (pre-2021) ancora citati senza aggiornamento

Pattern accettabili: "Trasferimento verso USA per provider X. Base: SCC (Decisione 2021/914 UE) + Transfer Impact Assessment. In alternativa: DPF se provider certificato".

#### Voce f) conservazione: pattern problematici
- "Per il tempo necessario" - **non utile**
- "Conformemente alle norme di legge" - **circolare**
- Tutti i dati con stesso periodo (es. "10 anni") - solitamente errato

Pattern accettabili: distinzione per categoria di dato:
- Dati anagrafici dipendenti: 10 anni post cessazione (art. 2220 c.c.)
- Buste paga: 5 anni (DPR 600/73)
- Curriculum candidati non assunti: 6-12 mesi
- Email marketing: fino a revoca consenso

#### Voce g) misure sicurezza: pattern problematici
- "Misure adeguate" - **non descrittivo**
- "Conformi all'art. 32" - **circolare**
- Solo misure tecniche senza organizzative (o viceversa)

Pattern accettabili: lista concreta:
- Tecniche: cifratura HDD AES-256, backup giornalieri offsite, MFA per accessi remoti, log di accesso 12 mesi
- Organizzative: policy NDA dipendenti, formazione GDPR annuale, gestione incidenti documentata, audit interno biennale

### Passo 4 - Verifica trigger DPIA

Per ogni trattamento del Registro, eseguire **mentalmente** i controlli di `valuta-soglia-dpia.md`:
- Rientra in una delle 12 tipologie del Provv. Garante 467/2018?
- Soddisfa 2+ criteri WP248 rev. 01?

Se si', segnalare nel report la potenziale necessita' di DPIA, e verificare se il Registro lo indica (campo "DPIA effettuata").

### Passo 5 - Output

```markdown
# Verifica completezza Registro trattamenti

**Data verifica**: [data]
**Registro analizzato**: [titolare/responsabile + identificazione]
**Numero trattamenti censiti**: N
**Versione registro**: [se dichiarata]

## Esito sintetico

[CONFORME | CONFORME CON NOTE MINORI | CARENZE SOSTANZIALI | NON CONFORME]

Trattamenti completi: X/N
Trattamenti con voci inadeguate: Y/N
Trattamenti con voci assenti: Z/N

## Verifica intestazione

- Identificazione titolare: [OK | INCOMPLETA - cosa manca]
- Contitolare: [OK | NON APPLICABILE | DA INTEGRARE]
- DPO: [presente con contatti | assente - obbligo art. 37? | facoltativo]

## Verifica per trattamento

### Trattamento 1 - [nome]

| Voce | Stato | Note |
|------|-------|------|
| b) Finalita' | OK / generica / assente | [...] |
| c) Categorie interessati | OK / generica / assente | [...] |
| c) Categorie dati | OK / generica / assente | [...] |
| d) Destinatari | OK / mancano provider | [...] |
| e) Trasferimenti extra-UE | NA / OK / da integrare | [...] |
| f) Conservazione | OK / generica / assente | [...] |
| g) Misure sicurezza | OK / solo tecniche | [...] |

DPIA potenzialmente richiesta: [SI/NO/DA VALUTARE] - perche': [riferimento a tipologia Garante o criteri WP248]

[ripetere per ciascun trattamento]

## Problemi rilevati - tabella riassuntiva

| # | Trattamento | Voce | Problema | Riferimento | Priorita' |
|---|-------------|------|----------|-------------|-----------|
| ... |

## Raccomandazioni

1. Integrare [voce X] per il trattamento Y con [...]
2. Specificare i provider cloud come destinatari (sono titolari ai fini art. 30 lett. d, anche se responsabili nominati)
3. Distinguere i tempi di conservazione per categoria di dato invece che per trattamento globale
4. ...

## Limiti di questa verifica

- Verifica formale di completezza, non legale di adeguatezza.
- Non verifica la coerenza tra le finalita' dichiarate e cio' che effettivamente si fa in azienda.
- Non valida la base giuridica scelta per ciascun trattamento (e' verifica legale).
- Non sostituisce la revisione del DPO o del consulente legale.

## Rinvio al professionista

**Il Registro e' uno strumento di accountability del titolare ex art. 5 par. 2 GDPR. Il DPO ha il compito di sorvegliare l'osservanza del Regolamento (art. 39). Questo report e' supporto operativo, non sostituisce la revisione del DPO o del consulente privacy.**

Sanzioni connesse a violazione art. 30: fino a 10M EUR o 2% del fatturato globale annuo (art. 83 par. 4).
```

## Casi limite

### Registro vuoto o solo intestazione
Segnare come **NON CONFORME** e raccomandare di partire con `draft-registro-trattamenti.md`.

### Registro senza distinzione titolare/responsabile
Segnalare come **carenza strutturale**: l'organizzazione puo' essere entrambi e serve distinzione chiara.

### Registro che cita solo "GDPR" come riferimento normativo
Insufficiente. Le voci devono essere riempite di sostanza, non rimandate.

### Registro con trattamenti che richiederebbero DPIA non segnalata
Segnalare ESPLICITAMENTE nel report. La mancata DPIA e' violazione separata da quella del Registro e ha sanzione propria.

## Limiti di questo task

- Verifica documentale, non testa la realta' dei processi.
- Non puo' verificare l'effettiva applicazione delle misure dichiarate.
- Non sostituisce ispezione del Garante o audit interno.

## Esempi

Vedi `examples/`:
- `registro-pmi-base/` - registro buono con 6 trattamenti
- (futuri) `registro-incompleto/` - registro con voci generiche
