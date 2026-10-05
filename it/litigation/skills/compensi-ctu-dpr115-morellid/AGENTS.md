# AGENTS.md - compensi-ctu-dpr115

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **liquidazione dei compensi** del **CTU / ausiliario del
magistrato** ai sensi del **Testo Unico spese di giustizia (D.P.R. 115/2002, Parte
III)**. Target: ingegneri iscritti all'albo dei CTU e, in genere, ausiliari del
magistrato.

**E' una skill documentale di dominio forense**: non calcola gli importi (tabelle
DM), non redige il decreto di pagamento (magistrato) e non tratta il CTP di parte.

## Nota sull'area di catalogo

Skill nell'area **forense** (CTU & ingegneria forense), aggiunta ad `areas.yaml` su
indicazione esplicita del maintainer. L'area parte con 2 skill (#42 compensi, #41
relazione peritale), in deroga consapevole alla soglia di 3 skill indicata in
`areas.yaml`, con l'intento di crescere.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-115-2002**: D.P.R. 115/2002, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash 8fc7d98b...). Artt. 49-58, 168, 170 caricati via AJAX
  (caricaArticolo) e trascritti verbatim in `references/fonti/dpr-115-2002.md`.

Estratto operativo: `references/estratti/compensi-ctu-checklist.md`.

## Punti chiave (verificati sul testo)

- **Spettanze** (art. 49): onorario, indennita'/spese di viaggio, rimborso spese.
- **Onorari** (art. 50): fissi, variabili, a tempo; **misura nelle tabelle del DM**
  (importi non nel DPR). L'a tempo (c. 3) definisce compenso orario, prima/successive,
  % urgenza, max ore/die.
- **Variabili** (art. 51): difficolta'/completezza/pregio; +20% per urgenza.
- **Aumento/riduzione** (art. 52): fino al doppio (eccezionale); riduzione per
  mancato completamento. **Collegiale** (art. 53): +40% per componente.
- **Adeguamento** triennale ISTAT (art. 54). **Indennita'/spese** (artt. 55-56).
  **Custodia** (art. 58). **Commissario ad acta** (art. 57).
- **Liquidazione** (art. 168): decreto di pagamento motivato, titolo provv.
  esecutivo. **Opposizione** (art. 170) ex art. 15 D.Lgs 150/2011.

## LIMITE DI FONTE (importante)

Le **tabelle tariffarie numeriche** (importo vacazione, onorari, scaglioni %) sono
delegate al **DM 30/5/2002** (art. 50) e **non risultano su Normattiva** (URN ->
atto non trovato). Gli **importi NON sono riprodotti**: la skill copre il quadro e
la procedura, **non il calcolo numerico**. Se in futuro il DM diventa reperibile su
host in allowlist (o viene fornito), si potra' aggiungere il modulo di calcolo.

## Convenzioni specifiche

### Cosa NON fare
- Non **inventare importi** (vacazione, onorari, scaglioni): sono nel DM, non letto.
- Non redigere il **decreto di pagamento** ne' l'opposizione.
- Non trattare i **compensi del CTP** (di parte, a contratto).

### Cosa fare
- Inquadrare spettanze, tipo di onorario e aumenti/riduzioni (artt. 49-53).
- Strutturare l'istanza di liquidazione e richiamare la procedura (artt. 55-56, 168,
  170), rinviando alle tabelle DM per gli importi.

## Aggiornamento delle fonti

Normattiva: riscaricare la pagina indice pinnata a un nuovo `!vig=` (nuovo hash) e
rileggere gli artt. 49-58 e 168/170. Verificare l'eventuale reperibilita' del DM
30/5/2002 (adeguamenti ISTAT ex art. 54) per aggiungere il calcolo.

## Validatori

- Non ancora assegnato (Livello 2 con CTU/avvocato esperto di liquidazioni).

## Stato attuale

- Versione: 0.1.0-alpha (closes #42)
- Task files: 2 (`inquadra-compenso.md`, `prepara-istanza-liquidazione.md`)
- Esempi: 2 (onorario a tempo/vacazioni con urgenza; incarico collegiale +
  eccezionale complessita')
