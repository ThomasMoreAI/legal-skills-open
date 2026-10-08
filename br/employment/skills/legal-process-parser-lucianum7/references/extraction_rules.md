# Regras de extração

1. Calcule SHA-256 e copie o original para uma área de trabalho somente leitura; nunca escreva sobre a fonte.
2. Para PDF, tente texto nativo por página. Classifique como `needs_ocr_or_vision` quando a página estiver vazia ou abaixo do limiar de qualidade.
3. OCR/visão é condicional: não aplique OCR em texto nativo de boa qualidade. Se a ferramenta não existir, registre a limitação e preserve `[ILEGÍVEL]`.
4. Use `pdf_page` para a posição física do arquivo e `court_page` para a folha impressa nos autos. Nunca iguale os dois por presunção.
5. Gere checkpoints após cada bloco. Uma página com erro não deve interromper as posteriores.
6. Preserve tabelas como tabelas Markdown quando a estrutura for confiável; caso contrário, descreva a perda de estrutura e não preencha células ausentes.
7. Normalize datas somente quando inequívocas; preserve sempre a forma textual encontrada.
8. O parser incluído é deliberadamente conservador e heurístico. Classificação de peça, área e qualidade requer conferência humana em processos reais.

## OCR opcional

O comando `ingest_document.py --ocr` rasteriza somente páginas sem texto nativo útil e chama Tesseract por meio de `pdf2image`/`pytesseract`. A execução é explícita, local e registrada no manifesto. Se qualquer dependência ou binário estiver indisponível, mantenha a página pendente e reporte a limitação.

## Dependências opcionais

- `pypdf` (preferencial) ou `PyPDF2` para camada textual de PDF.
- `pdf2image`, `pytesseract`, Pillow, Tesseract e Poppler para OCR local.
- A skill não baixa binários automaticamente nem envia autos para terceiros.
## Política visual estrita

Para PDFs, a política padrão é `--vision-mode always`: renderização e visão semântica são requisitos separados para conversão integral. Texto nativo não elimina a necessidade de inspeção visual; OCR permanece complementar. Quando `pdf2image`/Poppler ou uma descrição semântica revisada não estiverem disponíveis, o manifesto registra a limitação e a página não pode ser `COMPLETE`.
