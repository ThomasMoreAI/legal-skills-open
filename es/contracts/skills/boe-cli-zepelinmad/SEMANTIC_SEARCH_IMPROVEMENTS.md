# BOE CLI — Semantic Search Improvements

## Current State (v0.6.0)

- **Index:** 12,228 law titles embedded with `text-embedding-3-small` (1536 dims)
- **Test score:** 22/25 (88%) on diverse queries
- **What works:** Exact/known law names (0.6+ cosine), topic-specific queries
- **What fails:** Natural language queries, abstract concepts, cross-domain queries

### Failing queries:
1. "compraventa de empresa" → No LSC/mercantile (scores ~0.42)
2. "prescripción de deudas" → No Código Civil (scores ~0.51)
3. "me han robado y quiero denunciar" → No Código Penal (scores ~0.37)

### Root cause:
**Semantic gap** between bureaucratic law titles and natural language queries.
Example: "Código Penal" title is "Ley Orgánica 10/1995, de 23 de noviembre, del Código Penal"
but user asks "me han robado" — no semantic overlap in embedding space.

---

## Improvement Strategies (ranked by impact)

### 1. ⭐ Document Enrichment (INDEX TIME) — HIGH IMPACT

**The problem:** We embed raw titles like:
> "Real Decreto Legislativo 1/2010, de 2 de julio, por el que se aprueba el texto refundido de la Ley de Sociedades de Capital"

**The solution:** Enrich each title with metadata + keywords BEFORE embedding:

```
Ley de Sociedades de Capital (LSC). Regula la constitución, organización, 
funcionamiento y disolución de sociedades anónimas (SA), sociedades limitadas (SL)
y sociedades comanditarias por acciones. Cubre: responsabilidad del administrador, 
junta general, capital social, compraventa de participaciones, pactos de socios, 
fusiones, escisiones, dividendos, impugnación de acuerdos.
Título original: Real Decreto Legislativo 1/2010...
```

**Why it works:** The enriched text embeds in the same semantic space as natural queries.

**Implementation options:**
- **A) LLM enrichment (best quality):** Use Claude/GPT to generate a 2-3 sentence description per law. 12K laws × ~100 tokens = ~1.2M tokens ≈ $1-3.
- **B) Template enrichment (cheaper):** Append `rango` + known aliases + keywords from alias table.
- **C) Hybrid:** LLM for top 500 most important laws, template for rest.

**Research backing:** 
- "Enhancing Embedding Performance through LLM-based Text Enrichment" (2024)
- "GASE: Generatively Augmented Sentence Encoding" (2024)
- Both show 15-30% improvement on short-text retrieval tasks.

### 2. ⭐ HyDE at Query Time — HIGH IMPACT

**Hypothetical Document Embeddings (HyDE):** Instead of embedding the raw query, generate a hypothetical law title that WOULD match, then embed that.

User query: "me han robado y quiero denunciar"
→ LLM generates: "Ley Orgánica del Código Penal, que regula los delitos contra el patrimonio incluyendo robo, hurto, estafa y apropiación indebida"
→ Embed the hypothetical title → much better cosine match

**Pros:** Dramatic improvement for natural language queries
**Cons:** Adds ~500ms + 1 LLM call per query (but we already call embedding API)
**When to use:** Only when alias/fuzzy/exact don't match (same as current semantic fallback)

### 3. Multi-field Embedding — MEDIUM IMPACT

Instead of just embedding the title, concatenate structured fields:

```
{rango}: {short_title}. Materia: {extracted_topic}. Fecha: {date}. Vigente: {yes/no}.
```

Example:
```
Ley Orgánica: Código Penal. Materia: derecho penal, delitos, penas, robos, estafas.
```

### 4. Query Expansion — MEDIUM IMPACT

Before embedding, expand the query with related legal terms:

"compraventa de empresa" → "compraventa de empresa, adquisición societaria, transmisión de acciones/participaciones, M&A, due diligence"

Can use a static synonym table or LLM expansion.

### 5. Dimensionality & Model — LOW IMPACT

- Current: `text-embedding-3-small` (1536 dims) — good general model
- Alternative: `text-embedding-3-large` (3072 dims) — slightly better for nuanced queries
- Alternative: Multilingual model like `multilingual-e5-large` — potentially better for Spanish
- **Verdict:** Model change alone won't fix the semantic gap. Enrichment is the lever.

### 6. Re-ranking with Cross-Encoder — LOW-MEDIUM IMPACT

After initial retrieval, re-rank with a cross-encoder model that sees query+document together. Better at nuanced matching but adds latency.

Not worth it for a CLI tool at this scale.

---

## Recommended Plan

### Phase 1: Template Enrichment (quick win, no LLM cost)

For every entry in the index, append known metadata:
- Extract "short name" from title (e.g., "Ley de Sociedades de Capital" from the full title)
- Append aliases from the alias table if they match
- Append the `rango` (tipo de norma)
- Append topic keywords extracted from title

This can be done purely in Python at index build time. Zero API cost.

### Phase 2: LLM Enrichment for Top Laws

Use Claude/GPT to generate rich descriptions for the ~200 most important laws:
- All laws in the alias table
- All vigente leyes orgánicas
- All códigos (Civil, Penal, Comercio, etc.)

Cost: ~$0.50 for 200 laws.

### Phase 3: HyDE at Query Time (optional)

Add flag `--hyde` or enable automatically when initial scores are low (<0.4).
Use the existing OPENAI_API_KEY.

---

## Test Methodology

Keep the test script (`test_semantic_np.py`) as the benchmark.
Current baseline: **22/25 (88%)**
Target: **24/25 (96%)** or better

The 3 failing queries must ALL pass:
- "compraventa de empresa" → must find LSC or Ley de Modificaciones Estructurales
- "prescripción de deudas" → must find Código Civil
- "me han robado y quiero denunciar" → must find Código Penal
