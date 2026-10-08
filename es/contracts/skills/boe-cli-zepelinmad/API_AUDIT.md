# BOE API Audit — What We Have vs What's Available

*Generated: 2026-03-25*

## API Endpoints — Full Inventory

### 1. Legislación Consolidada (12,228+ normas)

| # | Endpoint | Description | Our CLI | Status |
|---|----------|-------------|---------|--------|
| 1 | `GET /legislacion-consolidada` | List/search norms | ✅ `search` | Full |
| 2 | `GET /legislacion-consolidada/id/{id}` | Full document (XML) | ⚠️ Partial | Only via `texto` |
| 3 | `GET /legislacion-consolidada/id/{id}/metadatos` | Metadata (JSON) | ✅ `metadata` | Full |
| 4 | `GET /legislacion-consolidada/id/{id}/analisis` | Analysis/references | ✅ `analysis` | Full |
| 5 | `GET /legislacion-consolidada/id/{id}/metadata-eli` | ELI metadata (RDF/XML) | ❌ Missing | **NEW** |
| 6 | `GET /legislacion-consolidada/id/{id}/texto` | Full consolidated text (XML) | ⚠️ Partial | Only via blocks |
| 7 | `GET /legislacion-consolidada/id/{id}/texto/indice` | Index of blocks | ✅ `index` | Full |
| 8 | `GET /legislacion-consolidada/id/{id}/texto/bloque/{bloque}` | Single block/article | ✅ `article` | Full |

### 2. BOE Diario (Sumarios)

| # | Endpoint | Description | Our CLI | Status |
|---|----------|-------------|---------|--------|
| 9 | `GET /boe/sumario/{fecha}` | Daily BOE summary | ✅ `today` | Full |

### 3. BORME (Boletín Oficial del Registro Mercantil)

| # | Endpoint | Description | Our CLI | Status |
|---|----------|-------------|---------|--------|
| 10 | `GET /borme/sumario/{fecha}` | BORME summary | ✅ `borme` | Full |

---

## Gap Analysis — What We're Missing

### ❌ GAP 1: ELI Metadata (`metadata-eli`)

**What it gives us:** European Legislation Identifier (ELI) data in RDF format:
- `eli:jurisdiction` — jurisdicción
- `eli:type_document` — tipo de documento codificado
- `eli:date_document` — fecha del documento
- `eli:is_about` — materias/temas (URLs codificadas)
- `eli:has_member` — versiones/consolidaciones
- `eli:publisher` — organismo publicador
- Relations between versions (amendments, consolidations)

**Value for M&A:** Las materias codificadas del ELI son machine-readable y podrían mejorar el semantic search (añadir topics al index).

**Implementation effort:** Bajo — XML-only endpoint, parsear con Go's xml package.

**Priority:** 🟡 Medium — useful for enrichment but not critical.

### ❌ GAP 2: Full Text Download (`texto` completo)

**What we have:** Individual blocks via `texto/bloque/{id}`.
**What we're missing:** Download the ENTIRE consolidated text in one request.

**Why it matters:**
- Export a full law to PDF/text for offline use
- Full-text search across a single law (currently must fetch block by block)
- Feed entire laws to LLMs for analysis
- The full text endpoint returns XML with all `<bloque>` elements and version history

**Implementation effort:** Medium — need XML parsing + text extraction. LSC = 1.2MB XML.

**Priority:** 🟢 High — very useful for agents and offline work.

### ❌ GAP 3: Advanced Search Parameters (partially missing)

**The API supports these search fields we DON'T expose:**

| Field | Description | Exposed? |
|-------|-------------|----------|
| `titulo:` | Search in title | ✅ Yes (via `titulo:`) |
| `texto:` | Full-text search | ✅ Yes (default) |
| `ambito@codigo:` | Scope (1=Estatal, 2=Autonómico) | ❌ No |
| `departamento@codigo:` | Department/Ministry code | ❌ No |
| `rango@codigo:` | Type of norm (Ley=1300, RDL=1310, etc.) | ❌ No |
| `materia@codigo:` | Subject matter code | ❌ No |
| `fecha_disposicion` | Enactment date | ❌ No (only via raw query) |
| `numero_oficial` | Official number | ❌ No |
| `vigencia_agotada` | Still in force? S/N | ❌ No (but we filter in scoring) |
| `estado_consolidacion@codigo` | Consolidation state | ❌ No |
| Date ranges (`from`/`to`) | Filter by update date | ❌ No |
| `sort` | Custom sort order | ❌ No |

**Value:** Power users could filter by jurisdiction (only estatal laws), type (only Leyes, not Reales Decretos), or active/repealed status.

**Priority:** 🟡 Medium — useful for power users.

### ❌ GAP 4: Cross-Reference Navigation

**The analysis endpoint returns:**
- `referencias/anteriores` — laws THIS law deroga/modifica
- `referencias/posteriores` — laws that modifica/deroga THIS law
- Each reference has: `id_norma`, `relacion` (code + text), `texto`

**We expose this via `analysis` command but don't make it navigable.**

Missing features:
- `refs BOE-A-2010-10544` → show who deroga/modifica this law
- `history BOE-A-2010-10544` → show modification timeline
- Click-to-navigate: from analysis, jump to the referenced law

**Priority:** 🟢 High — very useful for M&A lawyers doing due diligence.

### ❌ GAP 5: BORME Deep Dive

**Current `borme` command:** Shows daily summary only.
**Missing:**
- Parse the BORME sections (Sección A: actos inscritos, Sección B: otros actos)
- Extract company names, CIF, actos (nombramientos, ceses, ampliaciones de capital, etc.)
- BORME items have PDF links but no JSON/XML for individual items

**Reality check:** The BORME API is very limited — it only gives the summary with PDF links. Individual BORME items are NOT available as structured data via the API. Would need PDF parsing.

**Priority:** 🟠 Low-Medium — limited by API capabilities.

### ❌ GAP 6: Materias Vocabulary

**The API uses coded "materia" values** (e.g., 6691 = "Sociedades de Responsabilidad Limitada") but doesn't have a standalone vocabulary endpoint.

The analysis endpoint returns materias per law. We could:
- Build a materias index from all analysis responses
- Use materias to improve search (filter by legal area)
- Add materias to enriched embeddings

**Priority:** 🟡 Medium — enrichment value.

---

## What We ALREADY Have Right (Features Working Well)

1. ✅ **SmartSearch** — 6-layer intelligent search (alias → synonym → fuzzy → partial → title → texto)
2. ✅ **90+ aliases** — instant lookup for common law names
3. ✅ **Synonyms** — colloquial → legal term mapping
4. ✅ **Fuzzy matching** — typo tolerance with Levenshtein
5. ✅ **Semantic search** — enriched embeddings v2 (92% accuracy)
6. ✅ **REPL** — interactive shell with autocomplete
7. ✅ **Block navigation** — index → select → read specific articles
8. ✅ **BOE diario** — today's publications
9. ✅ **BORME** — daily mercantile bulletin
10. ✅ **Analysis** — materias, notas, referencias

---

## Recommended Priorities

### Phase 1 — Quick Wins (1-2 days)
1. **Full text download** — `boe law BOE-A-XXXX --full` → download entire text
2. **Cross-reference navigation** — `boe refs BOE-A-XXXX` → show amendments/derogations
3. **Filter by vigencia** — `boe search --vigente` to exclude derogated laws
4. **Date filters** — `boe search --from 20200101 --to 20260101`

### Phase 2 — Power Features (3-5 days)
5. **ELI metadata** — `boe eli BOE-A-XXXX` for European identifiers
6. **Filter by type** — `boe search --rango ley` (only Leyes, not RD)
7. **Filter by scope** — `boe search --ambito estatal` (exclude autonómicas)
8. **Sort control** — `boe search --sort fecha_publicacion:desc`

### Phase 3 — Advanced (1 week)
9. **Materias index** — build vocabulary, add to search filters
10. **Modification timeline** — `boe history BOE-A-XXXX` → visual timeline
11. **BORME parsing** — extract company data from PDF summaries
12. **Export** — `boe export BOE-A-XXXX --format md` → markdown/PDF export

---

## API Technical Notes

- **Rate limits:** No documented rate limits, but be nice (0.1-0.3s delay between requests)
- **Response formats:** JSON for most endpoints; XML-only for `texto`, `metadata-eli`, and `bloque`
- **Pagination:** `offset` + `limit` (default 50, max with `limit=-1`)
- **Authentication:** None required (open data)
- **CORS:** Not applicable (server-side only)
- **Full list:** `limit=-1` returns ALL 12,228+ entries (large response, ~6MB JSON)
