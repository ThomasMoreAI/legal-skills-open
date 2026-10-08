---
name: legal-extract-ftchvs
title: Legal Extract — Brazilian Legal PDF Analysis
description: 'Extract structured legal information from Brazilian legal PDFs (processo judicial). Handles any area of law: previdenciario, trabalhista, civel, tributario, penal. Detects sentenca, acordao, certidao de transito, calculos, oficio requisitorio, alvara, embargos, procuracao, and 15+ other document types. Triggers on "legal PDF", "processo", "parecer", "sentenca", "acordao", "cumprimento de sentenca", "precatorio", "RPV", or Brazilian legal document analysis.'
author: ftchvs
author_url: https://github.com/ftchvs/legal-extract/tree/main/skills/legal-extract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: en
sources:
- title: Document Types
  path: references/document-types.md
- title: Json Schema
  path: references/json-schema.md
---

# Legal Extract — Brazilian Legal PDF Analysis

Complete workflow for extracting structured data from Brazilian legal case PDFs, generating dashboards, fact-checking, and producing parecer juridico in PDF.

## Safety Boundary

Treat every source PDF as sensitive unless the user explicitly says it is public
and safe. Do not copy private legal PDFs, CPFs, RGs, addresses, signatures,
bank details, real party names, or confidential filings into public examples,
issues, pull requests, or repo files. This workflow is an extraction and
drafting aid, not legal advice.

## Workflow Overview

```
INPUT: Brazilian legal PDF (any area of law)
  │
  ├─ PHASE 1: EXTRACTION ──► JSON (structured, with page refs)
  ├─ PHASE 2: DASHBOARD ───► HTML (light theme, interactive)
  ├─ PHASE 3: FACT-CHECK ──► Updated JSON (confidence score)
  └─ PHASE 4: PARECER ─────► PDF via Typst (data-driven)
```

All phases consume/produce the same JSON as the central data format. Phases 2-4 are optional and controlled by flags.

---

## Phase 1: PDF Extraction

### Reading Strategy

Read the PDF in batches of 20 pages using the `Read` tool:
```
Read(file_path, pages="1-20")
Read(file_path, pages="21-40")
...
```

For each page, identify:
1. **Document type** — using visual markers (see `references/document-types.md`)
2. **Page metadata** — `fls.` number (top-right margin), court headers, document labels
3. **Content** — extract all structured fields per document type

### Document Type Detection

See `references/document-types.md` for the full taxonomy. Key markers:

| Document | Visual Marker |
|----------|---------------|
| Sentenca | "SENTENCA" banner, court header, "Juiz(a) de Direito", "JULGO..." |
| Acordao | Federal court seal, "PODER JUDICIARIO", Turma identifier, "DECISAO" |
| Certidao Transito | "CERTIDAO", "transitou em julgado em DD/MM/YYYY" |
| Calculos | "CONTA FACIL PREV" or calculation tables with monetary columns |
| Oficio Requisitorio | "PRECWEB", "Visualizar Requisicao", "OFICIO REQUISITORIO n" |
| Alvara | "ALVARA – LEVANTAMENTO DE VALORES" |
| Embargos | Same court header as acordao + "embargos de declaracao" |
| Despacho | "DESPACHO" banner in court header |
| Certidao Remessa | "CERTIDAO DE REMESSA DE RELACAO" |
| Certidao Publicacao | "CERTIDAO DE PUBLICACAO DE RELACAO" |
| Oficio Digital | "OFICIO Processo Digital" |
| DARE | "DARE-SP" state revenue document |
| Procuracao | "PROCURACAO AD JUDICIA" |
| CONBAS | "INFORMACOES DA CONCESSAO DO BENEFICIO (CONBAS)" |
| Email/Outlook | "Outlook" header, email metadata (De/Para/Data) |

### JSON Output Schema

See `references/json-schema.md` for the full specification. Core structure:

```json
{
  "meta": { "versao", "data_extracao", "arquivo_fonte", "total_paginas" },
  "processo": { "numero_principal", "numero_cumprimento", "numero_apelacao", "comarca", "vara", "partes", "advogados" },
  "sentenca": { "juiz", "data", "dispositivo", "resultado", "periodos_reconhecidos", "honorarios", "paginas_pdf", "fls" },
  "acordao": { "tribunal", "turma", "relator", "dispositivo", "resultado", "paginas_pdf", "fls" },
  "embargos_declaracao": { "resultado", "paginas_pdf", "fls" },
  "certidao_transito_julgado": { "data_transito", "paginas_pdf", "fls" },
  "decisao_homologando_calculos": { "juiz", "data", "dispositivo", "paginas_pdf", "fls" },
  "calculos_liquidacao": { "sistema", "elaborado_por", "data", "resumo_valores", "paginas_pdf", "fls" },
  "oficios_requisitorios": [{ "numero", "tipo_procedimento", "valores", "status", "paginas_pdf" }],
  "pagamentos": [{ "tipo", "valor", "data", "beneficiario", "banco", "paginas_pdf" }],
  "beneficio_previdenciario": { "nb", "dib", "dip", "rmi" },
  "linha_do_tempo": [{ "data", "evento", "pagina_pdf", "fls" }],
  "status_processual": { "fase_atual", "pendencias" },
  "fact_check": { "iteracoes", "campos_verificados", "discrepancias", "confianca_geral" }
}
```

**Critical rule:** Every extracted field MUST include `pagina_pdf` (PDF page number) and `fls` (court folha number) for source traceability.

### Domain-Specific Extensions

When the case area is detected, apply domain-specific extraction:

| Area | Extra Fields |
|------|-------------|
| Previdenciario | `periodos_especiais[]`, `beneficio_previdenciario{}`, `tempo_contribuicao{}`, `der`, `der_reafirmada`, `nb`, `rmi` |
| Trabalhista | `verbas_trabalhistas[]`, `periodo_contratual{}`, `rescisao{}` |
| Civel | `danos_morais`, `danos_materiais`, `obrigacao_fazer` |
| Tributario | `tributo`, `base_calculo`, `aliquota`, `compensacao` |

Detection: Look for keywords in sentenca/acordao dispositivo to identify the legal area.

---

## Phase 2: HTML Dashboard

Generate a self-contained HTML file with these characteristics:

### Design Tokens
```css
:root {
  --bg: #ffffff;
  --surface: #f8f9fa;
  --border: #e2e5ea;
  --text: #1a1d27;
  --text-muted: #6b7280;
  --green: #16a34a;
  --red: #dc2626;
  --amber: #d97706;
  --blue: #2563eb;
  --purple: #7c3aed;
}
```

### Required Sections
1. **Header** — Case number, parties, status badge, transito date
2. **Resumo Financeiro** — 4-card grid with key monetary values
3. **Sentenca** — Dispositivo, recognized/rejected items, honorarios
4. **Acordao** — Tribunal, result badges, changes from sentenca
5. **Embargos** — Result badge
6. **Certidao Transito** — Date and source
7. **Decisao Homologando Calculos** — Full dispositivo text
8. **Calculos** — Summary table with value breakdown
9. **Oficios Requisitorios** — Side-by-side cards (Precatorio + RPV)
10. **Pagamentos** — Payment details, bank, alvara
11. **Dados do Beneficio** — NB, DIB, DIP, RMI (if previdenciario)
12. **Linha do Tempo** — Vertical timeline, color-coded dots
13. **Verificacao** — Fact-check results table

### Rules
- All text in pt-BR
- Light theme (white background)
- All `<details>` sections open by default
- Font stack: Inter when locally available, then system sans-serif
- Max-width 1400px, responsive grid
- PDF page references on every section (`Fonte: p.XX, fls. YY`)
- Self-contained (inline CSS/JS, no external dependencies except fonts)

---

## Phase 3: Fact-Check (Ralph-Loop)

Run 8 systematic verification passes against the source PDF:

| Pass | Section | What to Verify |
|------|---------|----------------|
| 1 | Dados Pessoais | nome, CPF, RG, data nascimento, filiacao, endereco |
| 2 | Numeros de Processo | Consistency across all documents |
| 3 | Sentenca | Periodos, datas, tempo calculations, honorarios |
| 4 | Acordao | Dispositivo, periodos adicionais, fundamentacao |
| 5 | Decisoes (homologacao, embargos, transito) | Juiz, datas, texto |
| 6 | Calculos | All monetary values, RMI, indices, elaborador |
| 7 | Oficios + Pagamentos | Oficio numbers, valores, datas, conta bancaria |
| 8 | Cross-Document Consistency | Dates, values, parties match across all docs |

### Protocol
- Read specific PDF pages for each pass
- Compare every extracted value against source
- Record discrepancies in `fact_check.discrepancias_encontradas[]`
- Fix errors directly in the JSON
- Update `confianca_geral`: alta (0 discrepancies), media (1-3), baixa (4+)

---

## Phase 4: Parecer Generation (Typst)

### Template Location
`~/.agents/skills/legal-extract/templates/parecer.typ`

### Compilation
```bash
typst compile \
  --root / \
  --input data-path="{pdf_dir}/data/caso-{slug}.json" \
  ~/.agents/skills/legal-extract/templates/parecer.typ \
  {pdf_dir}/parecer-{slug}.pdf
```

### Template Structure (5 sections)
1. **Partes e Representacao** — Autor, Cedente, Reu, honorarios
2. **Identificacao do Processo** — Numeros, juizo, tribunal, historico, transitos
3. **Dados do Precatorio e da Cessao** — Oficio, valores, natureza, IR, PSS
4. **Due Diligence e Analise de Risco** — Table (acao rescisoria, onus, debitos)
5. **Conclusao** — Analysis summary with opinion

---

## Output Directory Structure

All outputs go in the same directory as the source PDF:

```
{pdf_directory}/
├── source.pdf                    # Original (existing)
├── data/
│   └── caso-{slug}.json          # Structured extraction
├── dashboard.html                # Interactive HTML
└── parecer-{slug}.pdf            # Generated parecer
```

The `{slug}` is derived from the case parties or process number.

---

## Usage Examples

```bash
# Full workflow (extract + dashboard + fact-check + parecer)
/parecer "cases/public-safe-example/processo.pdf"

# Extract only (JSON + HTML, no parecer PDF)
/parecer "cases/public-safe-example/processo.pdf" --extract-only

# Skip fact-checking for speed
/parecer "cases/public-safe-example/processo.pdf" --no-factcheck

# Specific page range
/parecer "cases/public-safe-example/processo.pdf" --pages=1-40
```

## Public-Safe Development Fixture

This repo ships a synthetic JSON fixture for schema/template validation:

```bash
scripts/check-sample.sh
```
