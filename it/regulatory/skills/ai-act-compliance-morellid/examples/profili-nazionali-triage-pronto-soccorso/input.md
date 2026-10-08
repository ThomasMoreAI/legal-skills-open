# Esempio - input per check-profili-nazionali-italia (triage di pronto soccorso)

> Sintetico, fittizio. Test su deployer italiano di sistema ad alto rischio con gap sulla sorveglianza umana.

## Organizzazione

**Casa di Cura San Lorenzo Srl** (Italia), struttura privata con pronto soccorso. Società di capitali, con modello
organizzativo 231 adottato nel 2022 e mai aggiornato sui sistemi di IA.

## Sistema

**"TriageAssist"**, fornito da MedAlgo Srl con marcatura CE e dichiarazione di conformità AI Act. Il sistema assegna il
codice di priorità ai pazienti in arrivo al pronto soccorso (parametri vitali, sintomi dichiarati, età).

La classificazione è già stata fatta con `classifica-sistema.md`: **alto rischio, Allegato III punto 5 lett. d**
(selezione dei pazienti per l'assistenza sanitaria di emergenza).

## Come è usato

- Il codice proposto da TriageAssist viene applicato direttamente dal personale di accettazione, a cui una circolare
  interna chiede di "non modificare la priorità salvo casi eccezionali, per non rallentare il flusso".
- Nessuna persona è formalmente designata alla sorveglianza umana; nessuna formazione specifica sul sistema.
- I log del sistema sono cancellati automaticamente dopo 30 giorni per contenere i costi di storage.
- La polizza RC professionale della struttura non menziona sistemi di IA; massimale 2 milioni EUR.

## Evento

Un paziente con dolore toracico ha ricevuto un codice di bassa priorità e ha atteso quattro ore; ha subito un danno.
L'avvocato del paziente ha inviato una lettera che chiede se la struttura sia assicurata per questo danno e preannuncia
un'azione di risarcimento. La lettera è arrivata 10 giorni fa. I log dell'accesso sono già stati cancellati.

## Domanda

Quali sono le conseguenze in Italia, oltre alle sanzioni AI Act? Cosa dobbiamo fare subito?
