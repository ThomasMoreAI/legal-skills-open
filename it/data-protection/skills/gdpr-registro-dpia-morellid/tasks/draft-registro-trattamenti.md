# Task: Stesura Registro delle attivita' di trattamento (art. 30 GDPR)

Costruisce un Registro delle attivita' di trattamento conforme all'art. 30 GDPR, sulla base delle informazioni fornite dall'utente sull'organizzazione e i suoi trattamenti.

## Obiettivo

Produrre un registro strutturato (formato tabellare e/o per schede) che contenga, per ciascun trattamento, le 7 voci obbligatorie del par. 1 (titolare) o le 4 del par. 2 (responsabile).

## Input richiesti

Per impostare l'intestazione (dati del titolare/responsabile):
- Ragione sociale, P.IVA, sede
- Nominativo del titolare (o legale rappresentante)
- Eventuale contitolare e accordo art. 26
- Eventuale rappresentante UE (per soggetti extra-UE)
- Nominativo e contatti del DPO se designato
- Tipologia: titolare o responsabile del trattamento

Per ogni trattamento da censire:
- Nome interno del trattamento (es. "Gestione personale dipendente", "Newsletter marketing")
- Finalita'
- Base giuridica (art. 6 + art. 9/10 se applicabile)
- Categorie di interessati
- Categorie di dati personali (dato comune, particolare art. 9, condanne art. 10)
- Categorie di destinatari (interni: ufficio HR, IT; esterni: payroll provider, cloud, ecc.)
- Trasferimenti extra-UE: paesi, garanzie applicate (decisione adeguatezza, SCC, BCR, deroga art. 49)
- Tempi di conservazione (per categoria di dati)
- Misure di sicurezza tecniche e organizzative

Se l'utente non ha questi dati, **chiedi un trattamento alla volta** in modalita' guidata invece di pretendere tutto in input.

## Fonti

Leggere prima:
- `references/estratti/gdpr-art-30.md` - testo integrale art. 30 e contenuti minimi
- Eventualmente: `references/estratti/gdpr-art-35-36.md` per cross-check con DPIA

## Procedura

### Passo 1 - Verifica applicabilita' art. 30 par. 5

L'art. 30 par. 5 esenta organizzazioni con < 250 dipendenti. Tuttavia l'esenzione **non si applica** se:
- Il trattamento puo' presentare un rischio per i diritti e le liberta' degli interessati
- Il trattamento non e' occasionale (cioe' e' strutturato)
- Include dati particolari (art. 9) o relativi a condanne (art. 10)

**Regola pratica**: in Italia praticamente tutte le organizzazioni anche piccole tengono il Registro. Conferma all'utente che, in dubbio, conviene tenerlo.

### Passo 2 - Intestazione del Registro

Compilare la sezione anagrafica del titolare/responsabile, una sola volta:

```
TITOLARE DEL TRATTAMENTO
Denominazione: [...]
P.IVA / CF: [...]
Sede legale: [...]
Email / PEC: [...]
Legale rappresentante: [...]

CONTITOLARE (se applicabile)
[stesso schema]

RAPPRESENTANTE UE (se titolare extra-UE)
[stesso schema]

DPO (se designato)
Nome: [...]
Contatti: [...]
Modalita' designazione: obbligatoria art. 37 par. 1 lett. ___ / facoltativa
```

### Passo 3 - Per ogni trattamento, costruire la scheda

Una scheda per trattamento. Schema raccomandato:

```
SCHEDA TRATTAMENTO N. [N]
Nome interno: [...]
Data prima registrazione: [YYYY-MM-DD]
Ultimo aggiornamento: [YYYY-MM-DD]

a) Identificazione: [richiamo intestazione]

b) Finalita'
[descrizione testuale]

Base giuridica (art. 6):
[ ] consenso art. 6.1.a)
[ ] contratto / pre-contrattuale art. 6.1.b)
[ ] obbligo legale art. 6.1.c) - cite la norma
[ ] tutela interessi vitali art. 6.1.d)
[ ] interesse pubblico art. 6.1.e)
[ ] legittimo interesse art. 6.1.f) - allegare bilanciamento (LIA)

Se categorie particolari (art. 9):
[ ] consenso esplicito art. 9.2.a)
[ ] obblighi diritto del lavoro art. 9.2.b)
[ ] tutela vitale art. 9.2.c)
[ ] interesse pubblico art. 9.2.g)
[ ] medicina del lavoro art. 9.2.h)
[ ] sanita' pubblica art. 9.2.i)
[ ] archivio/scientifico art. 9.2.j)

c) Categorie di interessati: dipendenti, clienti, fornitori, candidati, ...

c) Categorie di dati personali:
   - Dato comune: nome, indirizzo, e-mail, telefono, ...
   - Dato di contatto professionale: ...
   - Dato sensibile / particolare art. 9: salute, sindacale, religioso, ...
   - Dato giudiziario art. 10: condanne, reati, ...
   - Dato finanziario, biometrico, di geolocalizzazione, ...

d) Categorie di destinatari:
   - Interni: HR, IT, marketing, legale, direzione
   - Esterni Italia: payroll, commercialista, consulente del lavoro, banche, ...
   - Esterni UE: provider cloud (es. AWS Frankfurt), ...
   - Esterni extra-UE: --> richiama trasferimenti

e) Trasferimenti extra-UE:
   - Paese: [...]
   - Soggetto: [...]
   - Base giuridica trasferimento:
     [ ] Decisione adeguatezza CE (art. 45) - es. UK, Svizzera, Giappone, USA via DPF
     [ ] SCC (art. 46) - allegare moduli applicabili
     [ ] BCR (art. 47)
     [ ] Codici di condotta certificati (art. 46.2.e/f)
     [ ] Deroga art. 49 - usare con parsimonia

f) Termini di conservazione:
   - [Categoria dato 1]: [periodo + base normativa/policy]
   - [Categoria dato 2]: [periodo + base normativa/policy]
   Esempi: dati anagrafici dipendenti per 10 anni post cessazione (Civ.), buste paga 5 anni (DPR 600/73), dati clienti 10 anni (Cod. Civ.), email marketing fino a revoca consenso, biometrici 7 giorni dopo accesso.

g) Misure di sicurezza tecniche e organizzative (art. 32):
   Tecniche: cifratura at-rest e in-transit, pseudonimizzazione, MFA, log di accesso, backup, IDS/IPS, ...
   Organizzative: policy di accesso need-to-know, formazione personale annuale, NDA, audit interno, gestione incident, ...

DPIA effettuata: [SI / NO / IN VALUTAZIONE]
Riferimento DPIA: [link o ID documento]

Note: [...]
```

### Passo 4 - Formato di output

Il Registro puo' essere prodotto in due formati a scelta dell'utente:

**Formato A - Tabella sintetica** (utile per overview esecutivo):

| ID | Nome trattamento | Finalita' | Base giuridica | Cat. interessati | Cat. dati | Destinatari | Trasferim. | Conservazione | DPIA |
|----|------------------|-----------|----------------|------------------|-----------|-------------|------------|---------------|------|
| 1  | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Formato B - Schede dettagliate** (utile per audit, una per trattamento - vedi schema Passo 3).

Il Registro deve essere mantenuto in **forma scritta, anche elettronica** (art. 30 par. 3).

### Passo 5 - Auto-check di completezza

Dopo aver redatto il registro, **automaticamente eseguire** i controlli del task `check-registro-trattamenti.md` (oppure rinviare l'utente a quel task) per verificare che tutte e 7 le voci siano coperte.

### Passo 6 - Trigger DPIA

Per ogni trattamento del registro, **valuta se richiede DPIA** invocando il task `valuta-soglia-dpia.md`. Se si', evidenziarlo nel registro con marker visibile e suggerire creazione DPIA separata.

## Output atteso

Documento markdown completo con:
- Intestazione titolare/responsabile
- Schede trattamenti (formato A o B)
- Cross-reference DPIA per trattamenti ad alto rischio
- Disclaimer di responsabilita' del DPO

```markdown
# Registro delle attivita' di trattamento

**Titolare**: [...]
**Data**: [...]
**Versione**: [v1.0 - bozza per revisione DPO]

[intestazione + schede]

## Avvertenze

- Il presente Registro e' bozza redatta con strumenti di supporto. Va revisionato e validato dal DPO o dal consulente legale prima dell'adozione formale e della firma del titolare.
- Aggiornare il Registro ogni volta che cambiano: trattamenti, categorie dati, destinatari, finalita', misure tecniche.
- Tenere disponibile per richieste dell'autorita' di controllo (Garante).
```

## Casi limite

### Organizzazione molto piccola (< 250 dipendenti)
Anche se l'art. 30 par. 5 esenta, in pratica quasi sempre si applica una delle 3 condizioni che rendono comunque obbligatorio il Registro. Suggerire all'utente di tenerlo per default.

### Organizzazione complessa con molti trattamenti (>20)
Suggerire approccio per categorie di trattamenti omogenee (es. "Gestione clienti retail", "Gestione fornitori", "HR") con eventuali sottocategorie nel campo Note.

### Organizzazione con trattamenti misti (anche come responsabile)
L'organizzazione puo' essere titolare per alcuni trattamenti e responsabile per altri (es. azienda IT che processa dati di clienti finali). In questo caso servono **due registri separati** (par. 1 e par. 2).

### Trattamenti che cambiano frequentemente
Per trattamenti che cambiano spesso (es. piattaforme SaaS in fase di test), inserire un campo "Stato" (attivo/sospeso/cessato) e mantenere lo storico.

## Limiti di questo task

- Non sostituisce la valutazione legale sulla base giuridica corretta (la skill suggerisce ma non decide).
- Non valida la legittimita' dei trasferimenti extra-UE (richiede analisi caso per caso).
- Non quantifica i rischi (rinvio DPIA dove applicabile).

## Esempi

Vedi `examples/`:
- `registro-pmi-base/` - PMI 50 dipendenti, 6 trattamenti (HR, clienti, fornitori, marketing, sicurezza, web)
