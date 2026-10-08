# Schemas de Comunicacao Inter-Agente

Contratos JSON rigidos para comunicacao entre extratores, agente principal e validador. Todos os agentes DEVEM seguir estes schemas — dados fora do formato sao rejeitados.

## Sumario

1. [Schema de Dado Extraido (Extrator → Principal)](#1-dado-extraido)
2. [Schema de Lote de Extracao (envelope do extrator)](#2-lote-de-extracao)
3. [Schema de Conclusao (Principal → Validador)](#3-conclusao)
4. [Schema de Validacao (Validador → Principal)](#4-validacao)

---

## 1. Dado Extraido

Cada dado individual extraido por um subagente extrator. A referencia exata e obrigatoria — sem ela, o dado e descartado.

```json
{
  "dado": "187.34.56.78",
  "campo": "ip_acesso",
  "arquivo_fonte": "resposta_meta_20250315.pdf",
  "pagina": 4,
  "linha_ou_celula": "linha 23",
  "texto_original": "Access IP: 187.34.56.78 at 2025-03-15 14:32:17 BRT",
  "fuso_horario_original": "BRT (UTC-3)",
  "tipo_dado": "ip",
  "metadados": {}
}
```

### Campos obrigatorios

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `dado` | string | O valor extraido (IP, telefone, nome, IMEI, valor monetario, etc.) |
| `campo` | string | Classificacao semantica (ver tabela abaixo) |
| `arquivo_fonte` | string | Nome exato do arquivo de origem |
| `pagina` | int ou null | Numero da pagina (1-indexed). Null para CSV/TXT |
| `linha_ou_celula` | string | Localizacao dentro da pagina ("linha 23", "celula B7", "paragrafo 3") |
| `texto_original` | string | Trecho literal do documento que contem o dado (copiar ipsis litteris) |
| `tipo_dado` | string | Um dos tipos padrao (ver tabela abaixo) |

### Campos opcionais

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `fuso_horario_original` | string | Fuso como aparece no documento. NUNCA converter |
| `metadados` | object | Campos extras dependendo do tipo_dado |
| `aba_planilha` | string | Nome da aba (apenas para XLSX) |

### Valores validos para `campo`

| campo | Quando usar |
|-------|-------------|
| `ip_acesso` | Endereco IP de acesso a sistema (WhatsApp, banco, PJe) |
| `ip_transacao` | IP no momento de transacao financeira |
| `telefone` | Numero de telefone |
| `imei` | Codigo IMEI de aparelho |
| `nome_titular` | Nome de pessoa (titular de conta, linha, IP) |
| `cpf` | CPF |
| `conta_bancaria` | Dados de conta (banco + agencia + conta) |
| `chave_pix` | Chave Pix (telefone, email, CPF ou aleatoria) |
| `valor_transacao` | Valor monetario de transacao |
| `data_evento` | Data/hora de evento relevante |
| `modelo_dispositivo` | Modelo de aparelho (Samsung Galaxy A54, iPhone 13, etc.) |
| `endereco` | Endereco fisico |
| `email` | Endereco de email |
| `oab` | Numero OAB |
| `outro` | Qualquer dado que nao se encaixe acima |

### Valores validos para `tipo_dado`

`ip` | `telefone` | `imei` | `pessoa` | `financeiro` | `dispositivo` | `localizacao` | `documento` | `outro`

---

## 2. Lote de Extracao

Envelope retornado por cada subagente extrator. Contem todos os dados extraidos de um lote de documentos.

```json
{
  "extrator_id": "extrator_bancario_01",
  "status": "OK",
  "arquivos_processados": [
    {
      "arquivo": "extrato_bradesco_20250301_20250315.pdf",
      "total_paginas": 12,
      "metodo_extracao": "pdfplumber",
      "paginas_com_falha": []
    }
  ],
  "dados_extraidos": [
    {
      "dado": "187.34.56.78",
      "campo": "ip_transacao",
      "arquivo_fonte": "extrato_bradesco_20250301_20250315.pdf",
      "pagina": 3,
      "linha_ou_celula": "linha 15",
      "texto_original": "IP Origem: 187.34.56.78 | 05/03/2025 14:35:02 | PIX Enviado R$ 3.500,00",
      "fuso_horario_original": "BRT",
      "tipo_dado": "ip",
      "metadados": {}
    }
  ],
  "alertas": [
    "Pagina 7 do arquivo extrato_bradesco teve extracao por OCR (qualidade media)"
  ],
  "total_dados": 1
}
```

### Campos obrigatorios do envelope

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `extrator_id` | string | Identificador unico do extrator (ex: "extrator_bancario_01") |
| `status` | string | "OK" ou "ERRO" |
| `arquivos_processados` | array | Lista de arquivos com metadados de processamento |
| `dados_extraidos` | array | Lista de dados no schema da secao 1 |
| `alertas` | array de string | Problemas encontrados (OCR baixa qualidade, paginas inacessiveis) |
| `total_dados` | int | Contagem para verificacao |

---

## 3. Conclusao

Produzida pelo agente principal apos cruzamento. Cada conclusao carrega todas as referencias que a sustentam.

```json
{
  "conclusoes": [
    {
      "id": 1,
      "tipo": "convergencia_ip",
      "afirmacao": "O IP 187.34.56.78 aparece no acesso ao WhatsApp (14:32:17 BRT) e na transacao bancaria (14:35:02 BRT) do dia 05/03/2025, com intervalo de 2min45s, indicando que a mesma conexao de internet foi usada para ambas as acoes",
      "grau_confianca": "forte",
      "referencias": [
        {
          "arquivo": "resposta_meta_20250315.pdf",
          "pagina": 4,
          "linha_ou_celula": "linha 23",
          "dado_citado": "187.34.56.78 14:32:17 BRT",
          "extrator_id": "extrator_provedores_01"
        },
        {
          "arquivo": "extrato_bradesco_20250301_20250315.pdf",
          "pagina": 3,
          "linha_ou_celula": "linha 15",
          "dado_citado": "187.34.56.78 14:35:02 BRT",
          "extrator_id": "extrator_bancario_01"
        }
      ],
      "validacao": null
    }
  ],
  "caso_id": "IP-2025-00123",
  "data_analise": "2025-03-20"
}
```

### Campos obrigatorios da conclusao

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `id` | int | Sequencial unico |
| `tipo` | string | Classificacao (ver tabela abaixo) |
| `afirmacao` | string | Texto completo da conclusao, factual e preciso |
| `grau_confianca` | string | "forte" / "moderado" / "fraco" |
| `referencias` | array | Pelo menos 1 referencia com localizacao exata |
| `validacao` | object ou null | Preenchido pelo validador |

### Valores validos para `tipo`

| tipo | Descricao |
|------|-----------|
| `convergencia_ip` | Mesmo IP em fontes diferentes |
| `convergencia_imei` | Mesmo IMEI em fontes diferentes |
| `convergencia_dispositivo` | Mesmo modelo de aparelho em fontes diferentes |
| `convergencia_nome` | Mesmo nome aparecendo em fontes independentes |
| `vinculo_financeiro` | Conexao entre contas/transacoes |
| `vinculo_telefone` | Conexao entre linhas/chips |
| `identificacao_titular` | Titular identificado via operadora |
| `identificacao_laranja` | Indicios de conta laranja |
| `padrao_temporal` | Padrao de horarios/datas entre fontes |
| `materialidade` | Elemento que prova que o crime ocorreu |
| `outro` | Qualquer conclusao que nao se encaixe acima |

### Campos obrigatorios de cada referencia

| Campo | Tipo | Descricao |
|-------|------|-----------|
| `arquivo` | string | Nome exato do arquivo |
| `pagina` | int ou null | Pagina (1-indexed) |
| `linha_ou_celula` | string | Localizacao exata |
| `dado_citado` | string | O dado especifico que sustenta esta conclusao |
| `extrator_id` | string | Qual extrator forneceu este dado |

---

## 4. Validacao

Retornada pelo subagente validador apos verificar cada referencia contra o documento bruto.

```json
{
  "validacoes": [
    {
      "conclusao_id": 1,
      "veredicto_geral": "VERIFICADO",
      "detalhes": [
        {
          "arquivo": "resposta_meta_20250315.pdf",
          "pagina": 4,
          "linha_ou_celula": "linha 23",
          "dado_citado": "187.34.56.78 14:32:17 BRT",
          "status": "VERIFICADO",
          "texto_encontrado": "Access IP: 187.34.56.78 at 2025-03-15 14:32:17 BRT",
          "metodo_extracao": "pdfplumber",
          "match_exato": true,
          "observacao": ""
        },
        {
          "arquivo": "extrato_bradesco_20250301_20250315.pdf",
          "pagina": 3,
          "linha_ou_celula": "linha 15",
          "dado_citado": "187.34.56.78 14:35:02 BRT",
          "status": "VERIFICADO",
          "texto_encontrado": "IP Origem: 187.34.56.78 | 05/03/2025 14:35:02 | PIX Enviado R$ 3.500,00",
          "metodo_extracao": "pdfplumber",
          "match_exato": true,
          "observacao": ""
        }
      ]
    }
  ],
  "resumo": {
    "total_conclusoes": 1,
    "verificadas": 1,
    "contraditas": 0,
    "ambiguas": 0
  },
  "validador_id": "validador_01",
  "data_validacao": "2025-03-20"
}
```

### Veredictos possiveis por referencia

| status | Significado | Acao do agente principal |
|--------|-------------|--------------------------|
| `VERIFICADO` | Texto encontrado confirma o dado citado | Manter conclusao |
| `CONTRADITO` | Texto encontrado contradiz o dado citado | Remover conclusao |
| `AMBIGUO` | Texto encontrado e inconclusivo ou extracao falhou | Investigar manualmente |
| `EXTRACAO_FALHOU` | Script nao conseguiu extrair o trecho | Reportar como AMBIGUO |

### Veredicto geral da conclusao

- Se TODAS as referencias sao VERIFICADO → veredicto geral = `VERIFICADO`
- Se QUALQUER referencia e CONTRADITO → veredicto geral = `CONTRADITO`
- Se nenhuma e CONTRADITO mas alguma e AMBIGUO → veredicto geral = `AMBIGUO`

---

## Regras de Uso

1. **Extratores**: produzir APENAS dados no schema da secao 1, dentro do envelope da secao 2. NUNCA produzir conclusoes (secao 3).
2. **Agente principal**: consumir dados da secao 2, produzir conclusoes na secao 3. NUNCA relatar conclusoes antes de submetelas ao validador.
3. **Validador**: consumir conclusoes da secao 3, produzir validacoes na secao 4. NUNCA alterar as conclusoes — apenas verificar.
4. **Fuso horario**: NUNCA converter. Preservar exatamente como aparece no documento original.
5. **Referencia incompleta**: se o extrator nao consegue preencher `pagina` ou `linha_ou_celula`, deve preencher com o maximo de precisao possivel e adicionar alerta.
