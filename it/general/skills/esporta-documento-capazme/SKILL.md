---
name: esporta-documento-capazme
title: esporta-documento — Word/PDF di un deliverable legale
description: Esporta un deliverable legale (parere, informativa privacy, DPA, DPIA, registro trattamenti, parcella, atto, analisi giurisprudenziale) in un file Word (.docx) e/o PDF nella cartella attiva. Usa quando l'utente chiede di "esporta in word", "esporta in pdf", "salva il documento", "genera docx", "genera pdf", "metti in word", oppure "informativa/DPA/parere/parcella in word/pdf". Lavora sul markdown del documento gia' prodotto nella conversazione, oppure sul campo "testo" restituito da un tool (es. genera_informativa_privacy, genera_dpa).
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/esporta-documento
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: it
sources:
- title: Mapping
  path: references/mapping.md
---

# esporta-documento — Word/PDF di un deliverable legale

## Scopo

Rendere un deliverable testuale gia' prodotto (un parere, un'informativa privacy, un DPA,
una DPIA, un registro trattamenti, una parcella, un atto, una sintesi giurisprudenziale)
in un file **.docx** e/o **.pdf** salvato nella **cartella attiva**, applicando — quando
disponibile — il canone tipografico dello Studio SAPG (Times New Roman 12, interlinea 1,5,
rientro prima riga 0,5 cm, corpo giustificato).

Lo skill NON richiama alcun tool MCP: si limita a invocare due script locali via Bash.
La generazione del contenuto (il parere, l'informativa, ecc.) avviene PRIMA, con i tool o
le skill appropriate; questo skill prende quel testo e lo trasforma in un file consegnabile.

## Quando usare lo skill

- L'utente chiede esplicitamente di **esportare / salvare** un documento in Word o PDF.
- Al termine di un workflow (`/parere`, `/giurisprudenza`, `/compliance`, oppure le skill
  `parere-legale`, `analisi-giurisprudenziale`, `compliance-privacy`) quando l'utente vuole
  il deliverable come file.
- L'utente ha appena ricevuto da un tool un dict con un campo `testo`
  (es. `genera_informativa_privacy`, `genera_dpa`, `genera_dpia`,
  `genera_registro_trattamenti`, `genera_notifica_data_breach`) e vuole il file finito.

## Sorgente del contenuto

Due casi, entrambi gestiti dallo stesso flusso:

1. **Markdown dal transcript** — il documento e' gia' stato scritto nella conversazione
   come testo markdown. Riusa quel markdown tale e quale.
2. **Campo `testo` di un tool** — un tool GDPR/Privacy ha restituito un dict
   `{"testo": "...", ...}`. Estrai il valore di `testo` (e' gia' markdown/testo formattato)
   e usalo come contenuto.

In entrambi i casi: scrivi il contenuto in un file markdown temporaneo con lo strumento
`Write`, poi passalo agli script con `--input`. In alternativa puoi passarlo via stdin.

## Cartella attiva (active folder)

Il file viene scritto nella **cartella attiva**, cioe' la **directory di lavoro del processo**
(`process.cwd()` / `os.getcwd()`). L'utente puo' forzare una cartella diversa con `--dir`.
Lo script stampa su stdout il **path assoluto** del file creato: riportalo SEMPRE all'utente.

- Se l'utente non indica una cartella → si usa la cwd corrente (la "cartella attiva" di Cowork).
- Se l'utente indica una cartella (es. "salva in ~/Documenti/Clienti/Rossi") → passa `--dir <percorso>`.
- La cartella viene creata se non esiste (`mkdir -p` implicito).

## Nome del file (slug)

Il nome del file e' uno **slug**: minuscolo, accenti rimossi, spazi e simboli → trattino,
max 80 caratteri (es. "Parere — Responsabilità medica" → `parere-responsabilita-medica.docx`).
Lo slug deriva, in ordine di priorita': `--slug` esplicito → `--title` → primo titolo H1 del
markdown → `documento`. Per controllare il nome finale, passa `--slug`.

## Formato di output

- **Word (.docx)** — formato primario per la consegna allo studio/cliente; applica il canone
  SAPG (titoli numerati, corpo giustificato con rientro, tabelle, citazioni in blocco corsive).
- **PDF (.pdf)** — formato di sola lettura; resa essenziale con font built-in fpdf2.

Se l'utente non specifica il formato, **genera entrambi** (.docx + .pdf) e riporta i due path.
Se chiede solo Word o solo PDF, esegui solo lo script corrispondente.

## Esecuzione

### Word (.docx)

`docx-js` e' installato globalmente, quindi serve `NODE_PATH` puntato alle node_modules globali:

```bash
NODE_PATH=$(npm root -g) node \
  "${CLAUDE_PLUGIN_ROOT}/skills/esporta-documento/scripts/render_legal_docx.js" \
  --input /percorso/deliverable.md \
  --title "Parere — responsabilità medica" \
  --slug parere-rossi \
  --dir /cartella/attiva
```

oppure via stdin (utile per il campo `testo` di un tool, senza file temporaneo):

```bash
printf '%s' "$CONTENUTO_MARKDOWN" | NODE_PATH=$(npm root -g) node \
  "${CLAUDE_PLUGIN_ROOT}/skills/esporta-documento/scripts/render_legal_docx.js" \
  --title "Informativa Privacy art. 13 GDPR"
```

### PDF (.pdf)

Serve un Python 3.12 con `fpdf2`; il system python NON funziona. Usa `uv`, che il
plugin richiede gia' come prerequisito:

```bash
uv run --python 3.12 --with "fpdf2>=2.7" python \
  "${CLAUDE_PLUGIN_ROOT}/skills/esporta-documento/scripts/render_legal_pdf.py" \
  --input /percorso/deliverable.md \
  --title "Parere — responsabilità medica" \
  --slug parere-rossi \
  --dir /cartella/attiva
```

Entrambi gli script stampano su stdout SOLO il path assoluto del file generato (oppure
`FAIL: ...` su stderr con exit code 1 se manca il contenuto). Cattura quel path e mostralo
all'utente come conferma di consegna.

## Canone SAPG vs fallback

`render_legal_docx.js` tenta un `require` di `~/.claude/skills/docx-sapg/assets/sapg_styles.js`:

- **Modulo presente** → applica il canone SAPG completo (stili `SAPGHeading1/2/3`, `SAPGBody`,
  `SAPGQuote`, numerazione titoli multilivello 1. / 1.1 / 1.1.1, pagina A4, margini 1 inch).
- **Modulo assente** → fallback "plain" con gli stessi valori tipografici di base
  (Times New Roman 12, interlinea 1,5, rientro 0,5 cm, giustificato) ma senza la numerazione
  multilivello degli heading. Nessun errore: lo skill funziona comunque.

Il PDF non usa il canone SAPG (font built-in fpdf2 = Helvetica): e' una resa di lettura, non
il deliverable tipografico finale. Per la consegna formale usa sempre il .docx.

## Mappatura markdown → blocchi

La corrispondenza completa fra blocchi markdown e blocchi docx/pdf, le regole di slug e di
cartella attiva, e i casi limite sono in **`references/mapping.md`**.

## Dipendenze

- `node` con il pacchetto globale `docx` (`npm install -g docx`) — per il .docx.
- `uv` con `fpdf2` — per il .pdf. Senza `uv`, la venv che `start_server.sh` crea
  al primo avvio va bene: `"${MCP_CACHE_DIR:-$HOME/.cache/mcp-legal-it}/venv/bin/python"`.
- (Opzionale) `~/.claude/skills/docx-sapg/assets/sapg_styles.js` per il canone SAPG;
  in sua assenza il .docx usa il fallback plain.
- **Niente LibreOffice** (non installato): il PDF e' generato direttamente con fpdf2, non per
  conversione da .docx.

Lo skill non installa nulla. Se `docx` globale manca: `npm install -g docx`.

## Risorse

- **`scripts/render_legal_docx.js`** — markdown → .docx (canone SAPG con fallback plain).
- **`scripts/render_legal_pdf.py`** — markdown → .pdf (fpdf2, font built-in).
- **`references/mapping.md`** — mappatura blocchi markdown → docx/pdf, regole slug e cartella attiva.
