# PROCESSO ESTRUTURADO

## Metadados

- Arquivo: `{{source_name}}`
- SHA-256: `{{sha256}}`
- Páginas: `{{pages_total}}`
- Cobertura textual: `{{coverage_percent}}%`
- Elementos visuais: `{{visual_elements}}`

## Página PDF {{pdf_page}}

Use este bloco para **todas** as páginas, inclusive páginas vazias, escaneadas ou ilegíveis. Nunca remova uma página por falta de texto.

- Folha indicada nos autos: `{{court_page_or_not_identified}}`
- Peça/segmento: `{{piece}}`
- Documento ID: `{{document_id}}`
- Qualidade/fonte: `{{quality}}` / `{{source}}`
- Âncora: `PDF p. {{pdf_page}}`{{court_anchor}}

### Processamento por camada

- Texto nativo: `{{native_text_status}}`
- Renderização: `{{render_status}}`
- Inspeção técnica: `{{render_check_status}}`
- Visão semântica: `{{semantic_vision_status}}`
- OCR: `{{ocr_status}}`
- Consolidação: `{{consolidation_status}}`
- Status: `{{page_status}}`

### Resumo semântico e localização rápida

{{summary}}

- Termos-chave: {{keywords}}
- Entidades: {{entities}}

### Blocos, títulos e tabelas

{{content_blocks_or_not_identified}}

### Imagens e elementos visuais ({{visual_count}})

Para cada elemento:

- ID: `{{image_id}}`
- Tipo e localização: `{{kind}}` — `{{location}}`
- Arquivo: `images/{{filename_or_not_generated}}`
- Formato/dimensões/hash: `{{format}}`, `{{width}}×{{height}} px`, `{{sha256}}`
- Descrição semântica: `{{semantic_description_or_explicit_visual_review_pending}}`
- Texto visível/OCR: `{{visible_text_or_not_identified}}`
- Objetos, pessoas, tabelas/gráficos: `{{objects}}` / `{{people}}` / `{{tables}}`
- Confiança/origem: `{{confidence}}` / `{{description_source}}`

Se não houver visual: `Nenhuma imagem ou elemento visual foi extraído nesta página; se for um scan, requer OCR/visão.`

### Texto integral extraído

{{page_text_or_[ILEGÍVEL]}}

### Observações e pendências

{{warnings_or_none}}
