# Note di dominio - caso `profili-nazionali-triage-pronto-soccorso`

## Cosa stiamo testando

Che la skill colleghi i gap AI Act di un deployer italiano alle conseguenze nazionali del D.Lgs. 160/2026 (437-bis c.p.,
231, artt. 17-20) e dia azioni con scadenze concrete, a partire dal termine di 30 giorni dell'art. 20.

## Scelte progettuali del caso

- **Alto rischio certo** (Allegato III punto 5 lett. d): il 437-bis si applica solo a sistemi ad alto rischio, quindi
  il caso non si ferma sulla classificazione.
- **Pericolo per vita o incolumità plausibile**: nel triage l'errore di priorità mette a rischio la salute. Il reato
  richiede questo pericolo, non la sola non conformità.
- **Circolare che scoraggia le modifiche**: rende discutibile l'intenzionalità richiesta dal c.4 per l'utilizzatore
  professionale.
- **Log cancellati e lettera già ricevuta**: mettono alla prova l'art. 17 c.5 (fatti ritenuti ammessi) e l'art. 20
  (risposta entro 30 giorni).

## Output atteso

Esposizione ALTA su penale, 231 e civile; azioni immediate su risposta all'assicurazione, conservazione dei log,
sorveglianza umana e modello 231.

## Cose che la skill DEVE catturare

- Che la **marcatura CE del fornitore non protegge il deployer** (art. 19).
- Che il termine di **30 giorni** dell'art. 20 riguarda la comunicazione sulla polizza, non un termine di prescrizione
  né un'entrata in vigore.
- Che "utilizzatore professionale" **non è definito**: l'accostamento al deployer va segnalato come interpretazione.
- Che la presunzione dell'art. 18 non è limitata al fornitore: vale per il convenuto a cui si imputa la violazione.

## Cose che la skill NON dovrebbe fare

- Dare per certa la condanna penale: l'intenzionalità e la qualificazione del fatto spettano al penalista.
- Inventare la data di entrata in vigore del decreto: il testo non la fissa.
- Descrivere la fattispecie del 612-quater c.p.: il decreto la richiama senza descriverla.

## Fonte della struttura

Caso fittizio. Nessun riferimento a strutture o fornitori reali.
