# Task: Valutazione soglia DPIA (art. 35 GDPR + Provv. Garante 467/2018)

Determina se un trattamento richiede una Valutazione d'Impatto sulla protezione dei dati (DPIA), incrociando le previsioni dell'art. 35 GDPR, l'Allegato 1 al Provvedimento Garante n. 467/2018 (12 tipologie italiane), e i 9 criteri WP248 rev. 01 dell'EDPB.

## Obiettivo

Produrre una valutazione strutturata che concluda con uno dei 4 esiti:
- **DPIA OBBLIGATORIA** - rientra in una tipologia esplicita o soddisfa 2+ criteri WP248
- **DPIA RACCOMANDATA** - soddisfa 1 criterio + dubbi su categorie particolari o larga scala
- **DPIA NON RICHIESTA** - non rientra in alcuna tipologia, < 2 criteri, low-risk
- **DPIA GIA' COPERTA** - art. 35 par. 10 (DPIA gia' fatta in fase di adozione base giuridica)

## Input richiesti

Per ogni trattamento da valutare:
- Nome / descrizione finalita'
- Categorie di interessati (dipendenti? minori? pazienti? soggetti vulnerabili?)
- Categorie di dati (comuni? particolari art. 9? condanne art. 10? biometrici? genetici?)
- Volume / scala (numero interessati, ambito geografico)
- Modalita' tecniche (profilazione? AI? IoT? videosorveglianza? tracking?)
- Decisioni automatizzate con effetti giuridici/significativi?
- Base giuridica (art. 6) - alcune basi giuridiche escludono o presumono DPIA

## Fonti

Leggere prima:
- `references/estratti/gdpr-art-35-36.md` - testo art. 35 + 9 criteri WP248
- `references/estratti/garante-allegato1-prov467-2018.md` - 12 tipologie italiane

## Procedura

### Passo 1 - Verifica delle 12 tipologie italiane (Provv. Garante 467/2018)

Per ogni tipologia, valutare se il trattamento vi rientra (anche solo potenzialmente):

| # | Tipologia | Rientra? |
|---|-----------|----------|
| 1 | Scoring/profilazione su larga scala (rendimento, salute, preferenze, ubicazione) | [SI/NO/DUBBIO] |
| 2 | Decisioni automatizzate con effetti giuridici o analoghi (screening, antifrode...) | [SI/NO/DUBBIO] |
| 3 | Monitoraggio sistematico online/app, identificativi univoci, metadati | [SI/NO/DUBBIO] |
| 4 | Dati estremamente personali su larga scala (comunicazioni, ubicazione, finanziari) | [SI/NO/DUBBIO] |
| 5 | Controllo a distanza dipendenti (videosorveglianza, geolocalizzazione veicoli) | [SI/NO/DUBBIO] |
| 6 | Soggetti vulnerabili (minori, disabili, anziani, pazienti, asilo) | [SI/NO/DUBBIO] |
| 7 | Tecnologie innovative (IoT, AI, assistenti vocali, wearable, wi-fi tracking) + 1 altro criterio WP248 | [SI/NO/DUBBIO] |
| 8 | Scambio dati su larga scala telematicamente tra titolari | [SI/NO/DUBBIO] |
| 9 | Interconnessione/raffronto/incrocio (mobile payment + consumo digitale) | [SI/NO/DUBBIO] |
| 10 | Categorie particolari art. 9 o condanne art. 10 interconnesse con altri dati raccolti per finalita' diverse | [SI/NO/DUBBIO] |
| 11 | Dati biometrici sistematici (volume, durata, persistenza) | [SI/NO/DUBBIO] |
| 12 | Dati genetici sistematici (volume, durata, persistenza) | [SI/NO/DUBBIO] |

**Se ANCHE 1 SOLA TIPOLOGIA = SI** -> DPIA OBBLIGATORIA in Italia (presunzione iuris tantum del Garante).

### Passo 2 - Verifica dei 9 criteri WP248 rev. 01

Per ogni criterio:

| # | Criterio WP248 | Soddisfatto? |
|---|----------------|---------------|
| 1 | Valutazione/scoring (anche profilazione, predizione comportamento) | [SI/NO] |
| 2 | Decisioni automatizzate con effetti giuridici o analoghi significativi | [SI/NO] |
| 3 | Monitoraggio sistematico (anche tramite reti pubbliche, app, online) | [SI/NO] |
| 4 | Dati sensibili o di natura altamente personale | [SI/NO] |
| 5 | Trattamenti su larga scala (ampio numero interessati, volume, durata, geografia) | [SI/NO] |
| 6 | Combinazione/raffronto di dataset (incrocio, interconnessione) | [SI/NO] |
| 7 | Interessati vulnerabili (minori, dipendenti, pazienti, anziani, ...) | [SI/NO] |
| 8 | Uso innovativo o nuove tecnologie organizzative (AI, IoT, biometria, ...) | [SI/NO] |
| 9 | Trattamenti che impediscono esercizio diritto/uso servizio/contratto | [SI/NO] |

**Soglie WP248 rev. 01**:
- **2 o piu' criteri** = trattamento ad alto rischio, DPIA RICHIESTA
- **1 criterio** = trattamento che il titolare puo' considerare ad alto rischio se altri elementi suggeriscono, DPIA RACCOMANDATA
- **0 criteri** = generalmente DPIA NON RICHIESTA, ma valutare caso per caso

### Passo 3 - Verifica art. 35 par. 3 (casi espliciti GDPR)

L'art. 35 par. 3 GDPR cita 3 casi in cui DPIA e' RICHIESTA:

a) Valutazione sistematica e globale di aspetti personali, basata su trattamento automatizzato (profilazione), su cui si fondano decisioni con effetti giuridici/analoghi.
b) Trattamento su larga scala di categorie particolari art. 9 o di condanne art. 10.
c) Sorveglianza sistematica su larga scala di zona accessibile al pubblico.

Se rientra in uno di questi 3 casi -> DPIA OBBLIGATORIA.

### Passo 4 - Verifica esenzioni art. 35 par. 10

Se il trattamento si fonda su:
- Art. 6 par. 1 lett. c) (obbligo legale)
- Art. 6 par. 1 lett. e) (interesse pubblico/esercizio di poteri pubblici)

E una DPIA e' gia' stata effettuata nell'ambito dell'**adozione della base giuridica** (es. legge che impone il trattamento), allora i par. 1-7 non si applicano (salvo diversa previsione dello Stato membro).

In Italia: questa esenzione e' raramente operativa nei casi privati. Per la PA puo' applicarsi quando c'e' una norma specifica che ha gia' regolato la valutazione.

### Passo 5 - Sintesi e output

```markdown
# Valutazione soglia DPIA - [nome trattamento]

**Data valutazione**: [data]
**Trattamento valutato**: [descrizione sintetica]
**Titolare**: [...]

## Esito

**[DPIA OBBLIGATORIA | DPIA RACCOMANDATA | DPIA NON RICHIESTA | DPIA GIA' COPERTA]**

## Motivazione

### Tipologie italiane Provv. Garante 467/2018
[Lista delle tipologie applicabili. Se anche 1 -> DPIA obbligatoria]

### Criteri WP248 rev. 01
[Lista dei criteri soddisfatti. 2+ -> DPIA richiesta]

### Casi espliciti art. 35 par. 3
[Se rientra in a/b/c]

### Esenzioni art. 35 par. 10
[Applicabile? Note]

## Raccomandazione

[Se DPIA OBBLIGATORIA o RACCOMANDATA]
- Procedere con DPIA strutturata: vedi task `draft-dpia.md` o usa template DPIA
- Coinvolgere il DPO (consulta obbligatoria art. 35 par. 2)
- Tempi: completare DPIA prima dell'inizio del trattamento

[Se DPIA NON RICHIESTA]
- Documentare la decisione (motivazione tracciata, parte dell'accountability art. 5 par. 2)
- Riesaminare la decisione in caso di variazioni (art. 35 par. 11)

## Limiti di questa valutazione

- Si basa sulle informazioni fornite. Una sotto-stima della scala o delle categorie cambia l'esito.
- L'identificazione delle "tecnologie innovative" o "larga scala" richiede contestualizzazione settoriale.
- Il giudizio finale spetta al titolare consultato il DPO.

## Rinvio al DPO

**La consultazione del DPO e' obbligatoria** quando il titolare svolge una DPIA (art. 35 par. 2). La presente valutazione di soglia e' di supporto, non sostituisce la valutazione del DPO o consulente privacy.
```

## Casi tipici per ingegneri / sviluppatori (esempi di trigger DPIA)

| Caso | Tipologia/Criterio | Esito |
|------|---------------------|-------|
| App di tracking GPS dipendenti per logistica | Tipologia 5 + criterio 7 (vulnerabili) | DPIA OBBLIGATORIA |
| Sistema di videosorveglianza luoghi pubblici | Art. 35 par. 3 lett. c) + tipologia 3 | DPIA OBBLIGATORIA |
| Algoritmo ML scoring affidabilita' clienti | Tipologia 1+2 + criteri 1+2+5 | DPIA OBBLIGATORIA |
| IoT raccolta dati ambientali domestici | Tipologia 7 + 1 altro criterio (es. larga scala) | DPIA OBBLIGATORIA |
| Sistema biometrico controllo accessi azienda | Tipologia 11 + criterio 4 | DPIA OBBLIGATORIA |
| App fitness senza profilazione, no medical | Criterio 5 (larga scala) ma altri no | DPIA RACCOMANDATA |
| Newsletter mensile clienti (consenso) | Nessun criterio applicabile in genere | DPIA NON RICHIESTA |
| Sistema HR base (anagrafica, busta paga) | Categorie particolari (sanitarie da medicina del lavoro) ma criteri solo 1-2 | DPIA RACCOMANDATA per cautela |

## Limiti di questo task

- Decisione di soglia, non DPIA effettiva.
- Non sostituisce il giudizio del DPO o del consulente legale.
- Le 12 tipologie del Garante sono soggette ad aggiornamento - verificare data di consultazione e provvedimenti successivi.

## Esempi

Vedi `examples/`:
- `dpia-richiesta-app-profilazione/` - sistema di scoring clienti = DPIA obbligatoria
