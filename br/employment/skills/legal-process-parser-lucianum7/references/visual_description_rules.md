# Protocolo de descrição semântica visual

Este protocolo orienta uma revisão humana ou multimodal para preencher `--image-descriptions`. Ele não autoriza inferências jurídicas, autenticação documental ou identificação biométrica.

## 1. Identificação e localização

Use o `image_id` produzido pelo pipeline (`P0001-I001` para imagem incorporada ou `P0001-SCAN` para scan integral). Informe a página PDF, a folha processual quando conhecida e a região aproximada: cabeçalho, centro, rodapé, margem esquerda/direita ou página integral.

## 2. Descrição objetiva

Descreva somente elementos observáveis: tipo aparente de documento, orientação, cores/contraste relevantes, carimbos, selos, assinaturas, rubricas, tabelas, gráficos, fotografias, mapas, códigos de barras/QR e estado de legibilidade. Diga “não identificado” quando não for possível observar com segurança.

## 3. Texto visível e OCR

Transcreva apenas o que estiver legível. Preserve números, datas, moedas e identificadores exatamente como aparecem; marque lacunas como `[ilegível]`. O OCR é uma pista, não prova: registre em `visible_text` e mantenha o texto bruto em `ocr_text` quando produzido automaticamente.

## 4. Pessoas e objetos

Liste pessoas apenas como “pessoa não identificada”, salvo nome explicitamente legível no próprio documento. Não conclua idade, gênero, raça, intenção, autoria, autenticidade ou estado emocional. Liste objetos e itens de tabela sem atribuir significado jurídico.

## 5. Confiança e origem

Use `high`, `medium` ou `low` em `confidence`. Use `human_review` para conferência humana, `vision_model` para modelo multimodal autorizado, `external_review` para fonte revisada e `technical_inventory`/`page_scan_fallback` quando houver apenas metadados técnicos. Descrições de fallback devem declarar a necessidade de revisão visual.

## 6. Exemplo mínimo

```json
{
  "images": [
    {
      "image_id": "P0001-I001",
      "semantic_description": "Imagem em retrato com recibo e tabela de valores; cabeçalho legível, parte inferior parcialmente ilegível.",
      "visible_text": "RECIBO ... [ilegível]",
      "objects": ["recibo", "tabela"],
      "people": [],
      "tables": ["itens e total"],
      "location": "centro da página PDF 1",
      "confidence": "medium",
      "description_source": "human_review"
    }
  ]
}
```
