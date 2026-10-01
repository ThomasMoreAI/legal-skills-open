# Rilevamento della fase processuale

La quotazione corretta dipende dalla fase in cui si trova la posizione, non dal solo
valore del credito. Classificare OGNI posizione prima di generare i documenti.

## Regole di classificazione

Esaminare, nell'ordine, le colonne/informazioni di stato della posizione (es. in un
foglio di controllo: "Esecutorietà", "Note", "Azione"):

| Segnale | Fase | tipo per genera_quotazione_docx |
|---------|------|--------------------------------|
| Decreto dichiarato esecutivo (es. Esecutorietà = "V"), cartella "Esecuzione Forzata" in fascicolo, precetto notificato | Esecuzione forzata | `esecuzione` |
| Note tipo "decreto ingiuntivo opposto" (anche "opposto ma non ancora notificato"), atto di opposizione in fascicolo | Opposizione a D.I. (art. 645 c.p.c.) | `opposizione` |
| Azione "Ricorso per decreto ingiuntivo" senza i segnali precedenti | Monitorio | `monitorio` |
| Azione diversa (giudizio civile ordinario, sola diffida stragiudiziale) | Fuori perimetro | escludere e segnalare |

Note operative:

- "Richiesta Depositata" nella colonna esecutorietà indica che l'istanza è pendente:
  la posizione resta `monitorio` finché il decreto non è dichiarato esecutivo.
- Una posizione può avere sia il decreto sia l'opposizione: l'opposizione prevale
  (il giudizio di merito assorbe la fase monitoria).
- In caso di dubbio chiedere all'utente: un preventivo con la fase sbagliata è
  strutturalmente errato (fase unica monitoria ≠ due fasi esecutive ≠ quattro fasi
  di cognizione), non solo impreciso.

## Tabelle usate dai tool (D.M. 55/2014 agg. D.M. 147/2022)

Compenso tabellare — procedimenti monitori, fase unica (il minimo pubblicato è il
medio ridotto del 50% ex art. 4, co. 1, arrotondato — per i primi scaglioni il
medio è dispari, quindi minimo × 2 NON restituisce il medio ministeriale):

| Scaglione | Minimo | Medio |
|-----------|--------|-------|
| fino a € 5.200 | € 237,00 | € 473,00 |
| € 5.201 – € 26.000 | € 284,00 | € 567,00 |
| € 26.001 – € 52.000 | € 685,00 | € 1.370,00 |
| € 52.001 – € 260.000 | € 1.121,00 | € 2.242,00 |
| € 260.001 – € 520.000 | € 2.197,00 | € 4.394,00 |

Esecuzione forzata: i default del tool (fase introduttiva € 166,00 + trattazione e
conclusiva € 284,00) sono i MINIMI dello scaglione fino a € 5.200. Per valori causa
superiori o per una quotazione a valori medi il tool rifiuta i default: passare i
compensi dello scaglione corretto con `compenso_fase_introduttiva` /
`compenso_fase_trattazione` (tabella esecuzioni mobiliari D.M. 55/2014).

Opposizione a decreto ingiuntivo: quattro fasi del contenzioso civile
(studio, introduttiva, istruttoria, decisionale) dalle tabelle ministeriali già
presenti nel server (le stesse di `legal-it:parcella_avvocato_civile`).

Contributo unificato automatico:

- monitorio: metà degli importi DPR 115/2002 (art. 13, co. 3), letta dalla tabella
  canonica del server (`data/contributo_unificato.json`) — € 21,50 / € 49,00 /
  € 118,50 / € 259,00 / € 379,50 / € 607,00 fino a € 520.000, € 843,00 oltre;
- esecuzione: € 139,00 (+ € 27,00 marca + € 120,00 spese forfettarie; il tool
  aggiunge la nota su € 200,00 per deposito pignoramento e trasferta);
- opposizione: non quotato — a carico della parte opponente (il tool inserisce la
  nota in lettera).

Catena di calcolo del prospetto (validata): tabellare → +30% PCT (art. 4, co. 1-bis;
solo monitorio e opposizione) → spese generali 15% → CPA 4% → IVA 22% → ipotesi di
compenso liquidabile → ritenuta d'acconto 20% su compenso e spese imponibili →
totale documento (l'esecuzione si ferma al liquidabile, senza PCT e senza ritenuta).
