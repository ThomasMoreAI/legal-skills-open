# Task: inquadra-compenso

Dato l'incarico di CTU/ausiliario, individua le spettanze, il tipo di onorario e
gli aumenti/riduzioni applicabili ai sensi del DPR 115/2002. Supporto documentale:
non calcola l'importo (tabelle DM 30/5/2002).

## Input

- Tipo di incarico (perizia, consulenza tecnica, stima, custodia, commissario ad
  acta), materia, complessita', durata.
- Eventuali provvedimenti del magistrato (urgenza, proroghe, collegio).

## Procedura

1. **Spettanze (art. 49)**: onorario + indennita'/spese di viaggio + rimborso spese.
2. **Tipo di onorario (art. 50)**:
   - **fisso** (importo da tabella DM);
   - **variabile** (tra min e max di tabella, secondo **difficolta', completezza,
     pregio** - art. 51 c. 1);
   - **a tempo / vacazioni** (compenso orario da tabella; distinzione prima ora /
     successive; **numero massimo di ore giornaliere** - art. 50 c. 3).
3. **Aumenti**:
   - **urgenza** dichiarata con decreto motivato: +fino al **20%** (art. 51 c. 2);
   - **eccezionale importanza/complessita'/difficolta'**: +fino al **doppio** (art.
     52 c. 1);
   - **incarico collegiale**: compenso del singolo **+40% per ciascun altro
     componente** (art. 53), salvo incarico integrale a ciascuno.
4. **Riduzioni**: mancato completamento nei termini per fatti imputabili (art. 52 c.
   2): onorari a tempo non computati oltre il termine, altri onorari ridotti.
5. **Rinvio agli importi**: le cifre (vacazione, onorari, scaglioni %) sono nelle
   tabelle del **DM 30/5/2002** (adeguate ISTAT ogni 3 anni, art. 54) - la skill
   NON le fornisce.

## Output

- Elenco delle spettanze e del tipo di onorario applicabile, con gli aumenti/
  riduzioni pertinenti e i relativi articoli.
- Nota che l'importo va determinato sulle tabelle vigenti del DM.

## Avvertenze

- La qualificazione (variabile vs a tempo), la difficolta' e la liquidazione sono
  valutazioni del **magistrato**.
- Solo **ausiliari del magistrato** (non CTP di parte).
