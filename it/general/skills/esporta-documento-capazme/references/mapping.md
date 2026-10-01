# Mappatura markdown → docx/pdf — esporta-documento

Riferimento per `render_legal_docx.js` (Word) e `render_legal_pdf.py` (PDF). Entrambi gli
script usano un tokenizer di blocchi a righe (line-based): non e' un parser markdown completo,
ma copre i blocchi usati nei deliverable legali.

## Blocchi supportati

| Markdown | Tokenizzato come | Word (.docx) — canone SAPG | Word (.docx) — fallback plain | PDF (.pdf) |
|---|---|---|---|---|
| `# Titolo` | `heading` livello 1 | stile `SAPGHeading1`, numerato `1.`, bold, sinistra | `HEADING_1`, bold, Times New Roman | Helvetica bold 13 pt |
| `## Titolo` | `heading` livello 2 | stile `SAPGHeading2`, numerato `1.1`, bold | `HEADING_2`, bold | Helvetica bold 12 pt |
| `### Titolo` (e oltre) | `heading` livello ≤3 | stile `SAPGHeading3`, numerato `1.1.1`, bold | `HEADING_3`, bold | Helvetica bold 11 pt |
| testo libero | `paragraph` | stile `SAPGBody`: giustificato, rientro 0,5 cm, interlinea 1,5 | giustificato, rientro 0,5 cm, interlinea 1,5 | Helvetica 10 pt |
| `- voce` / `* voce` / `+ voce` | `list` non ordinata | `SAPGBody` + numbering `sapg-bullets` (•) | bullet docx-js | riga `- voce` |
| `1. voce` / `1) voce` | `list` ordinata | `SAPGBody` + numbering `sapg-numbers` (1.) | numbering `plain-numbers` | riga `1. voce` |
| `> citazione` | `quote` (righe `>` consecutive unite) | stile `SAPGQuote`: corsivo, rientro 1 cm bilaterale | corsivo, rientro bilaterale | Helvetica corsivo 10 pt, rientrato |
| tabella GFM (header + riga `---`) | `table` | `Table` docx 100% larghezza, bordi grigi, header in bold | idem | righe con celle separate da `  \|  ` |
| `---` / `***` / `___` | `spacer` (docx) / linea orizzontale (pdf) | paragrafo vuoto | paragrafo vuoto | linea orizzontale |
| riga vuota | confine di paragrafo | flush del paragrafo corrente | idem | `ln(3)` |

## Inline (emfasi)

Riconosciuti dentro ogni blocco testuale:

| Markdown | docx | pdf |
|---|---|---|
| `**testo**` / `__testo__` | `TextRun` bold | marker rimosso, testo conservato |
| `*testo*` / `_testo_` | `TextRun` corsivo | marker rimosso, testo conservato |
| `` `codice` `` | `TextRun` font Courier New / Courier | marker rimosso, testo conservato |

Nel PDF gli inline sono **spogliati** (font built-in fpdf2 senza grassetto/corsivo per-run):
si conserva il contenuto, non la formattazione. Nel Word la formattazione inline e' resa.

## Continuazione di paragrafo

Righe di testo consecutive senza riga vuota in mezzo vengono **unite** in un unico paragrafo
(join con spazio). Per andare a capo come paragrafo distinto, lasciare una riga vuota.

## Note sulle tabelle

- Una tabella e' riconosciuta SOLO se la riga successiva all'header e' una riga separatore
  (`| --- | --- |`). Senza separatore, le righe con `|` sono trattate come testo normale.
- Nel Word le tabelle sono `Table` reali con bordi; nel PDF sono linearizzate (le celle di una
  riga su una singola riga di testo, separate da `  |  `) perche' fpdf2 con font built-in non
  rende bene tabelle complesse.

## Titolo del documento

Derivato in quest'ordine: `--title` esplicito → primo blocco `heading` del markdown →
`"Documento"`. Nel Word diventa il metadato `title`; nel PDF e' la prima riga in grande (bold).

## Regole di slug (nome file)

Lo slug determina il nome del file (`<slug>.docx` / `<slug>.pdf`). Derivazione, in ordine:

1. `--slug` esplicito;
2. altrimenti dal titolo (vedi sopra).

Trasformazione:

- minuscolo;
- normalizzazione NFKD + rimozione accenti (`à` → `a`, `è` → `e`, ...);
- ogni sequenza di caratteri non `[a-z0-9]` → un singolo trattino `-`;
- trattini iniziali/finali rimossi;
- troncato a 80 caratteri;
- se vuoto → `documento`.

Esempi:

| Titolo / slug richiesto | File |
|---|---|
| `Parere — Responsabilità medica` | `parere-responsabilita-medica.docx` |
| `Informativa Privacy art. 13 GDPR` | `informativa-privacy-art-13-gdpr.docx` |
| `DPA Studio Rossi / DATRIX` | `dpa-studio-rossi-datrix.docx` |
| (nessuno) | `documento.docx` |

## Regole di cartella attiva (active folder)

- Default: **directory di lavoro del processo** (`process.cwd()` per il JS, `os.getcwd()` per
  il Python). In Cowork corrisponde alla cartella attiva della sessione.
- Override: `--dir <percorso>` (relativo o assoluto; viene risolto in path assoluto).
- La cartella viene creata se non esiste.
- Il path assoluto del file generato e' stampato su **stdout** (unica riga): va riportato
  all'utente come conferma di consegna.

## Errori

- Input vuoto (ne' `--input` ne' stdin con contenuto) → messaggio `FAIL: ...` su **stderr** ed
  exit code **1**. Lo skill deve segnalarlo all'utente, non silenziarlo.
