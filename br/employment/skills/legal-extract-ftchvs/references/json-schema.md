# Legal Extract — JSON Output Schema

Standard JSON schema for Brazilian legal case extraction. All downstream outputs (HTML dashboard, Typst parecer) consume this format.

## Schema Version: 1.0.0

## Core Rules

1. **Source tracking:** Every extracted field MUST include `pagina_pdf` (1-indexed PDF page) and `fls` (court folha number)
2. **Monetary values:** Store as numbers (not strings). Use Brazilian convention in display only (R$ X.XXX,XX)
3. **Dates:** Store as strings in DD/MM/YYYY format (Brazilian standard)
4. **Names:** UPPERCASE as they appear in court documents
5. **Null handling:** Use `null` for missing fields, never omit the key

## Top-Level Structure

```json
{
  "meta": {},
  "processo": {},
  "sentenca": {},
  "acordao": {},
  "embargos_declaracao": {},
  "certidao_transito_julgado": {},
  "decisao_homologando_calculos": {},
  "calculos_liquidacao": {},
  "oficios_requisitorios": [],
  "pagamentos": [],
  "beneficio_previdenciario": {},
  "linha_do_tempo": [],
  "status_processual": {},
  "fact_check": {}
}
```

## Field Specifications

### meta
```json
{
  "versao": "1.0.0",
  "data_extracao": "YYYY-MM-DDTHH:MM:SS-03:00",
  "arquivo_fonte": "filename.pdf",
  "total_paginas": 92,
  "idioma": "pt-BR",
  "elaborado_por": "Claude Code"
}
```

### processo
```json
{
  "numero_principal": "NNNNNNN-NN.NNNN.N.NN.NNNN",
  "numero_cumprimento": "NNNNNNN-NN.NNNN.N.NN.NNNN",
  "numero_apelacao": "NNNNNNN-NN.NNNN.N.NN.NNNN",
  "classe": "Procedimento Comum",
  "assunto": "string",
  "comarca": "string",
  "foro": "string",
  "vara": "string",
  "justica_gratuita": true,
  "partes": {
    "autor": {
      "nome": "UPPERCASE",
      "cpf": "NNN.NNN.NNN-NN",
      "rg": "string",
      "data_nascimento": "DD/MM/YYYY",
      "naturalidade": "Cidade-UF",
      "filiacao": { "pai": "string", "mae": "string" },
      "endereco": "string",
      "telefone": "string",
      "hipossuficiente": true,
      "fonte": { "paginas_pdf": [4, 5, 6], "fls": [8, 9, 60] }
    },
    "reu": {
      "nome": "UPPERCASE",
      "cnpj": "NN.NNN.NNN/NNNN-NN",
      "tipo": "Autarquia Federal",
      "procurador": "string",
      "fonte": { "paginas_pdf": [], "fls": [] }
    }
  },
  "advogados": [
    {
      "nome": "UPPERCASE",
      "oab": "OAB/UF NNN.NNN",
      "cpf": "NNN.NNN.NNN-NN",
      "polo": "autor|reu",
      "endereco_profissional": "string",
      "fonte": { "paginas_pdf": [], "fls": [] }
    }
  ]
}
```

### sentenca
```json
{
  "titulo": "SENTENCA",
  "tribunal": "string",
  "orgao_julgador": "string",
  "juiz": "string",
  "data": "DD/MM/YYYY",
  "paginas_pdf": [7, 8, 9, 10, 11],
  "fls": [772, 773, 774, 775, 776],
  "dispositivo": "JULGO PARCIALMENTE PROCEDENTE|PROCEDENTE|IMPROCEDENTE",
  "resultado": "procedente|parcialmente_procedente|improcedente",
  "resumo": "string (2-3 sentences)",
  "periodos_reconhecidos": [
    {
      "inicio": "DD/MM/YYYY",
      "fim": "DD/MM/YYYY",
      "agente_nocivo": "string",
      "intensidade": "string",
      "limite_tolerancia": "string",
      "empresa": "string",
      "setor": "string",
      "documento": "string (PPP Id.)",
      "fator_conversao": 1.4,
      "fonte": { "paginas_pdf": [], "fls": [] }
    }
  ],
  "periodos_nao_reconhecidos": [
    { "inicio": "DD/MM/YYYY", "fim": "DD/MM/YYYY", "motivo": "string" }
  ],
  "tempo_contribuicao": {
    "reconhecido_inss": { "anos": 0, "meses": 0, "dias": 0, "data_referencia": "DD/MM/YYYY" },
    "tempo_especial_convertido": { "anos": 0, "meses": 0, "dias": 0 },
    "total_computado": { "anos": 0, "meses": 0, "dias": 0 }
  },
  "honorarios": {
    "reu_inss": { "custas_percentual": "20%", "honorarios_patrono_autor": "R$ 300,00" },
    "autor": { "custas_percentual": "80%", "honorarios_patrono_reu": "R$ 1.200,00" }
  },
  "fundamentacao_legal": ["Art. NNN, Lei NNNN/NN"]
}
```

### acordao
```json
{
  "titulo": "DECISAO (ACORDAO)",
  "tribunal": "string",
  "orgao_julgador": "Xa Turma",
  "numero": "Apelacao Civel (NNN) N NNNNNNN-NN.NNNN.N.NN.NNNN",
  "relator": "string",
  "paginas_pdf": [],
  "fls": [],
  "dispositivo": "string (full text)",
  "resultado": "procedente|parcial_provimento_autor|negou_provimento|etc",
  "resumo": "string",
  "apelacao_inss": { "resultado": "string", "argumento": "string" },
  "apelacao_autor": { "resultado": "string", "argumento": "string" },
  "periodo_adicional_reconhecido": {
    "inicio": "DD/MM/YYYY", "fim": "DD/MM/YYYY",
    "agente_nocivo": "string", "empresa": "string"
  },
  "aposentadoria_concedida": {
    "tipo": "string", "der_original": "DD/MM/YYYY", "der_reafirmada": "DD/MM/YYYY",
    "nb": "string", "efeitos_financeiros": "string"
  },
  "honorarios_acordao": { "condenacao": "string", "base_legal": "string" },
  "correcao_monetaria": { "juros_mora": "string", "indice": "string" },
  "temas_stj_citados": [{ "numero": 422, "assunto": "string" }]
}
```

### certidao_transito_julgado
```json
{
  "data_transito": "DD/MM/YYYY",
  "data_certidao": "DD/MM/YYYY",
  "local": "string",
  "paginas_pdf": [20],
  "fls": [207],
  "texto_integral": "Certifico que a R. decisao retro transitou em julgado em DD/MM/YYYY."
}
```

### decisao_homologando_calculos
```json
{
  "juiz": "string",
  "data": "DD/MM/YYYY",
  "processo": "string",
  "paginas_pdf": [],
  "fls": [],
  "dispositivo_items": ["1. ...", "2. ...", "3. ..."],
  "texto_integral": "string",
  "concordancia_autor": { "data": "DD/MM/YYYY", "advogado": "string" }
}
```

### calculos_liquidacao
```json
{
  "sistema": "CONTA FACIL PREV",
  "elaborado_por": "string",
  "data": "DD/MM/YYYY",
  "atualizado_ate": "MM/YYYY",
  "paginas_pdf": [],
  "fls": [],
  "resumo_valores": {
    "partes": { "principal_corrigido": 0.00, "juros_moratorios": 0.00, "selic": 0.00, "total": 0.00 },
    "sucumbencias": { "principal_corrigido": 0.00, "juros_selic": 0.00, "total": 0.00 },
    "totalizacao": { "subtotal_conta": 0.00, "total_geral": 0.00 }
  },
  "periodo_parcelas": { "inicio": "MM/YYYY", "fim": "MM/YYYY", "total_meses": 0, "rmi_inicial": 0.00 }
}
```

### oficios_requisitorios[]
```json
{
  "numero": "string",
  "tipo_procedimento": "Precatorio|RPV",
  "natureza_credito": "Alimenticio|Comum",
  "valores": { "valor_total": 0.00, "valor_principal": 0.00, "juros_mora": 0.00, "juros_selic": 0.00 },
  "transito_fase_conhecimento": "DD/MM/YYYY",
  "transito_embargos": "DD/MM/YYYY",
  "status": "string",
  "paginas_pdf": [],
  "fls": []
}
```

### pagamentos[]
```json
{
  "tipo": "RPV|Precatorio|Alvara",
  "requisicao_numero": "string",
  "data_pagamento": "DD/MM/YYYY",
  "valor_pago_total": 0.00,
  "valor_pago_principal": 0.00,
  "valor_pago_juros": 0.00,
  "beneficiario": "string",
  "banco": "string",
  "agencia": "string",
  "conta": "string",
  "status": "PgTOTAL DPJUIZ|Pendente",
  "paginas_pdf": [],
  "fls": []
}
```

### linha_do_tempo[]
```json
{
  "data": "DD/MM/YYYY",
  "evento": "string (short description)",
  "pagina_pdf": 1,
  "fls": 1
}
```

### status_processual
```json
{
  "fase_atual": "string",
  "pendencias": ["string"]
}
```

### fact_check
```json
{
  "ultima_verificacao": "ISO 8601",
  "iteracoes": 8,
  "campos_verificados": 147,
  "total_campos": 150,
  "discrepancias_encontradas": [
    { "campo": "JSON path", "valor_extraido": "X", "valor_correto": "Y", "pagina_pdf": 1, "corrigido": true }
  ],
  "confianca_geral": "alta|media|baixa",
  "passes": [
    { "pass": 1, "descricao": "string", "campos_verificados": 22, "resultado": "string" }
  ]
}
```

## Sections That May Be Null

Not all cases will have all sections. Use `null` for missing sections:

| Section | When Null |
|---------|-----------|
| `acordao` | Case decided only at 1st instance (no appeal) |
| `embargos_declaracao` | No embargos filed |
| `decisao_homologando_calculos` | Calculos not yet homologated |
| `calculos_liquidacao` | Calculos not yet presented |
| `oficios_requisitorios` | Requisitorios not yet expedited |
| `pagamentos` | No payments yet |
| `beneficio_previdenciario` | Not a previdenciario case |
