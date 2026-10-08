# Semantic Search Improvements — BOE CLI

## Diagnóstico

### Problema actual
El semantic search embebe **solo títulos oficiales** del BOE y los compara con queries del usuario. Los títulos son largos y formales ("Real Decreto Legislativo 1/2010, de 2 de julio, por el que se aprueba el texto refundido de la Ley de Sociedades de Capital") mientras que las queries son conceptuales y coloquiales ("responsabilidad del administrador").

### Benchmark actual: 25/26 (96%) — PERO engañoso
- **Queries con nombre de ley** (ej: "ley de sociedades de capital"): 10/10 perfecto
- **Queries conceptuales** (ej: "responsabilidad del administrador"): scores de 0.25-0.46, resultados mediocres
- La LSC (la ley MÁS importante para M&A) no aparece cuando buscas conceptos que regula

### Root cause: gap semántico título↔concepto
El embedding del título "Ley de Sociedades de Capital" está lejos semánticamente de "responsabilidad del administrador", aunque la LSC es exactamente donde se regula eso (arts. 236-241bis).

---

## Resultados experimentales (25 mar 2026)

### Experimento 1: Raw vs Enriched vs HyDE
| Query | Raw | Enriched | HyDE | Mejora HyDE |
|-------|-----|----------|------|-------------|
| responsabilidad del administrador | 0.2585 | 0.2942 | 0.5543 | **+114%** |
| echar al inquilino | 0.3477 | 0.3416 | 0.7814 | **+125%** |
| despido improcedente | 0.3544 | 0.3271 | 0.5997 | **+69%** |
| fusión de sociedades | 0.4629 | 0.5327 | 0.7215 | **+56%** |

**HyDE gana 10/10**. Pero requiere LLM call por query (latencia + coste).

### Experimento 2: Index-side enrichment
| Approach | Wins/10 | Nota |
|----------|---------|------|
| Raw titles | 1/10 | Baseline |
| Combined (title + synthetic queries en 1 vector) | 0/10 | **Peor que raw** — diluye el embedding |
| Multi-vector (1 vector por synthetic query) | 9/10 | **+8% a +43% mejora** |

**Key finding**: Meter las synthetic queries en el mismo embedding EMPEORA. Hay que separarlos.

---

## Solución recomendada: Hybrid con 3 mejoras

### Mejora 1: Multi-vector Index (index-time, offline)
Para cada ley, generar 8-10 synthetic queries con LLM y embeber cada una por separado.
- **Coste único**: ~$2-3 (12K × 10 queries × gpt-4o-mini)
- **Index size**: ~740MB (10x actual) — aceptable para CLI local
- **Beneficio**: +20-40% en queries conceptuales, sin latencia extra en búsqueda
- **Build time**: ~30 min (paralelizable)

### Mejora 2: Hybrid search (BM25 + semantic)
Combinar keyword search (BM25/TF-IDF sobre títulos) con semantic search.
- Muchas queries tienen overlap parcial de palabras
- BM25 es instantáneo y cubre los casos que semantic falla
- Reciprocal Rank Fusion para combinar scores
- **Coste**: 0 (todo local)

### Mejora 3: Query-time HyDE (opcional, para queries difíciles)
Si top semantic score < 0.4, activar HyDE:
1. LLM genera título hipotético
2. Embebe ese título
3. Re-busca
- **Coste**: ~$0.001 por query activada
- **Latencia**: +500ms
- Solo se activa cuando los otros métodos fallan

---

## Plan de implementación

### Fase 1: Multi-vector index (mayor impacto, offline)
1. Nuevo script `build_index_v2.py`:
   - Descarga títulos del BOE (igual que v1)
   - Para cada título, genera 8-10 synthetic queries con gpt-4o-mini
   - Embebe título + cada synthetic query por separado
   - Nuevo formato binario: `index-v2.bin`
2. Actualizar Go index reader para v2
3. Search: cosine similarity contra TODOS los vectores, return best per law

### Fase 2: Hybrid BM25
1. Implementar BM25 scoring en Go (simple, ~100 LOC)
2. Tokenizar títulos al construir index
3. En búsqueda: BM25 score + semantic score con RRF

### Fase 3: HyDE fallback (opcional)
1. Si best score < threshold, call LLM para expandir query
2. Re-embed y re-buscar
3. Configurable: `--hyde` flag o automático

---

## Formato index-v2.bin

```
Header:
  magic: "BOE2" (4 bytes)
  version: uint32 (2)
  dimensions: uint32 (1536)
  law_count: uint32 (12228)
  total_vectors: uint32 (~122K)

Per law:
  id_len: uint32, id: bytes
  title_len: uint32, title: bytes
  vector_count: uint32 (1 title + N synthetic)
  vectors: [vector_count × dimensions × float32]
  
  // For BM25:
  token_count: uint32
  tokens: [token_count × (len: uint32, token: bytes)]
```

## Costes estimados

| Concepto | Coste |
|----------|-------|
| Build index v2 (one-time) | ~$3 (LLM) + <$0.01 (embeddings) |
| Query (sin HyDE) | <$0.0001 (1 embedding call) |
| Query (con HyDE) | ~$0.001 (1 LLM + 1 embedding) |
| Index storage | ~740MB disco |
