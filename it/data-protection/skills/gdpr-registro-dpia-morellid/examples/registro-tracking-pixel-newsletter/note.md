# Note di dominio - caso `registro-tracking-pixel-newsletter`

## Cosa stiamo testando

Che il modulo `tasks/tracking-pixel-email.md` (introdotto dopo le Linee guida Garante
provv. 284/2026) sappia: (1) classificare correttamente le finalita' del pixel rispetto
alle deroghe dell'art. 122 del Codice; (2) produrre una scheda di Registro art. 30 con
le categorie di dati effettivamente generate dal pixel; (3) concludere correttamente la
soglia DPIA; (4) elencare i GAP di adeguamento con la scadenza del 29/10/2026.

## Scelte progettuali del caso

- **Pixel univoco per destinatario, senza anonimizzazione**: esclude la deroga
  statistica del par. 5, caso 1 - il caso deve finire nella colonna "consenso".
- **Tre usi in escalation** (misurazione individuale, sospensione invii per
  disinteresse, profilazione con incrocio CRM): tutti e tre citati testualmente al
  par. 6 delle Linee guida come casi che richiedono consenso preventivo.
- **Trattamento gia' in corso al 29/04/2026**: attiva il regime transitorio del
  par. 6 (informativa con primo invio utile + revoca granulare ad alta visibilita').
- **Solo link "disiscriviti"**: GAP tipico - manca la revoca del solo tracciamento,
  che le Linee guida richiedono espressamente (par. 6).
- **45.000 iscritti + incrocio con storico acquisti**: porta la soglia DPIA a
  OBBLIGATORIA via tipologia 1 e 3 Allegato 1 Provv. 467/2018 e 4 criteri WP248.
  Contrasto voluto con il caso "newsletter mensile clienti (consenso)" della tabella di
  `tasks/valuta-soglia-dpia.md`, che senza profilazione individuale resta
  "DPIA NON RICHIESTA": e' la profilazione tramite pixel a cambiare l'esito, non la
  newsletter in se'.

## Cose che la skill DOVREBBE fare

- Negare l'applicabilita' della deroga statistica motivando con l'univocita' del pixel
  e l'assenza di anonimizzazione.
- Elencare tra le categorie di dati quelle indicate al par. 1 delle Linee guida
  (apertura, IP, dispositivo, tempo di consultazione, numero aperture, identificativi).
- Non attribuire alle Linee guida un obbligo di DPIA: l'esito DPIA discende da
  Allegato 1/WP248, non dal provvedimento 284/2026.
- Citare il termine del 29/10/2026 (sei mesi dalla pubblicazione in GU n. 98 del
  29/04/2026).

## Cose che la skill NON dovrebbe fare

- **Falso negativo sulla deroga**: concludere che basta la "statistica" perche' il
  marketing guarda anche i tassi aggregati - l'uso individuale prevale.
- Suggerire di eliminare la newsletter: il rifiuto del tracciamento deve lasciare
  piena fruibilita' del servizio (par. 6), quindi newsletter senza pixel.
- Dare per scontato che il fornitore SaaS sia gia' responsabile art. 28 senza
  verificare contratto e configurazione.

## Fonte della struttura

Caso fittizio. I riferimenti normativi citati sono tratti da
`references/estratti/garante-prov284-2026-tracking-pixel.md`,
`references/estratti/garante-allegato1-prov467-2018.md` e
`references/estratti/wp248-criteri.md`.
