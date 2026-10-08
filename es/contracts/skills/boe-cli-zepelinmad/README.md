# boe-cli

Navigate Spanish legislation from the command line. Access the [BOE (Boletín Oficial del Estado)](https://www.boe.es/) open data API — consolidated legislation, daily publications, and legal analysis.

Built for AI agents and legal professionals.

## Install

```bash
# From source (requires Go 1.21+)
go install github.com/zepelinmad/boe-cli@latest

# Or clone and build
git clone https://github.com/zepelinmad/boe-cli.git
cd boe-cli
go build -o boe .
```

## Quick Start

```bash
# Search legislation
boe search "texto:compraventa participaciones" -l 5
boe search "titulo:sociedades and titulo:capital"

# Read specific articles
boe law BOE-A-1889-4763 --article art1255 --text     # Art 1255 CC (freedom of contract)
boe law BOE-A-2010-10544 --article a107 --text        # Art 107 LSC (share transfer restrictions)
boe law BOE-A-2003-23186 --article a42 --text         # Art 42 LGT (tax liability)
boe law BOE-A-2015-11430 --article a44 --text         # Art 44 ET (business succession)

# Browse law structure
boe law BOE-A-1889-4763 --index                       # Código Civil structure

# Today's BOE / BORME
boe today                                              # Today's publications
boe today --date 20260321                              # Specific date
boe today --borme                                      # Mercantile bulletin
```

## Common Law Identifiers

| ID | Law |
|---|---|
| `BOE-A-1889-4763` | Código Civil |
| `BOE-A-2010-10544` | Ley de Sociedades de Capital (LSC) |
| `BOE-A-2003-23186` | Ley General Tributaria (LGT) |
| `BOE-A-2015-11430` | Estatuto de los Trabajadores (ET) |
| `BOE-A-1885-6627` | Código de Comercio |
| `BOE-A-2023-15135` | RDL 5/2023 (Modificaciones Estructurales) |
| `BOE-A-2009-5614` | Ley 3/2009 (Modificaciones Estructurales anterior) |
| `BOE-A-2007-12946` | Ley 15/2007 (Defensa de la Competencia) |

## Commands

### `boe search`

Search consolidated legislation using BOE's advanced query syntax.

**Available fields:**
- `titulo:TEXT` — Search in law title
- `texto:TEXT` — Full-text search in law content
- `ambito@codigo:N` — Scope (1=State, 2=Autonomous)
- `departamento@codigo:N` — Department code
- `rango@codigo:N` — Legal rank code (1300=Ley, 1310=Real Decreto Legislativo, 1320=Real Decreto-ley)
- `materia@codigo:N` — Subject matter code
- `estado_consolidacion@codigo:N` — Consolidation status

Combine with: `and`, `or`, `not`, parentheses.

```bash
boe search "titulo:sociedades and titulo:capital"
boe search "texto:compraventa participaciones" --limit 10
boe search "titulo:tributaria and rango@codigo:1300"
boe search --recent --limit 5
```

### `boe law <ID>`

Access a specific law by its BOE identifier.

```bash
boe law BOE-A-1889-4763 --index              # Structure (titles, chapters, articles)
boe law BOE-A-1889-4763 --article art1255     # Specific article (JSON)
boe law BOE-A-1889-4763 --article art1255 -t  # Specific article (human-readable text)
boe law BOE-A-1889-4763 --metadata            # Law metadata
boe law BOE-A-1889-4763 --analysis            # Modifications & cross-references
```

### `boe today`

Fetch the BOE daily summary.

```bash
boe today                        # Today's BOE
boe today --date 20260321        # Specific date (YYYYMMDD)
boe today --borme                # BORME (mercantile bulletin)
```

## Output

All commands output JSON by default (agent-friendly). Use `-p` for pretty-printing and `--text`/`-t` for human-readable output on article lookups.

```bash
boe law BOE-A-2010-10544 --article a107 -p    # Pretty JSON
boe law BOE-A-2010-10544 --article a107 -t    # Human-readable text
```

## For AI Agents

This CLI is designed to be used by AI agents via bash tool execution. The structured JSON output can be parsed directly. Pair it with a SKILL.md that describes the available commands and common law identifiers.

## API

Uses the [BOE Open Data API](https://www.boe.es/datosabiertos/api/api.php) — free, no API key required, no rate limits documented.

## License

MIT
