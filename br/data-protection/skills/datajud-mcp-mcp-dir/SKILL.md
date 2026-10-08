---
name: datajud-mcp-mcp-dir
title: DataJud (CNJ) — REST API skill
description: 'Consulta de processos judiciais brasileiros via API Pública do CNJ/DataJud: metadados, movimentações e busca por classe/órgão/assunto. Use sempre que o usuário citar um número de processo (formato CNJ), pedir andamento/movimentações, ou buscar processos por tribunal. Grátis, sem login. Orquestra datajud_get_processo, datajud_search, datajud_movimentos e datajud_raw_query do servidor remoto em https://api.mcp.ai/p_datajud.'
author: mcp-dir
author_url: https://github.com/mcp-dir/datajud-mcp/tree/main/skills/datajud-mcp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# DataJud (CNJ) — REST API skill

Você tem acesso à **DataJud (CNJ)** REST API na MCP.AI.

> Consulta pública de processos judiciais do Brasil (metadados e movimentações) via a API Pública do CNJ/DataJud, cobrindo STJ, TST, TSE, STM, TJs, TRFs, TRTs, TREs e Justiça Militar. Grátis, sem login, hospedado pela plataforma.

## Base URL

```
https://api.mcp.ai/api/datajud
```

Todo endpoint é um **POST** na Base URL + o path abaixo. Os parâmetros vão no corpo JSON.

## Autenticação

Inclua em toda request:

```
Authorization: Bearer sk_live_...
Content-Type: application/json
```

> Gere sua chave em **https://app.mcp.ai/settings/api-keys** (workspace API key `sk_live_…`, não expira, revogável). Uma única chave serve pra todos os seus MCPs.

## Formato de resposta

```json
{ "ok": true, "tool": "<tool_id>", "result": <payload> }
```

## Exemplo cURL

```bash
curl -X POST https://api.mcp.ai/api/datajud/get/processo \
  -H "Authorization: Bearer sk_live_..." \
  -H "Content-Type: application/json" \
  -d '{"tribunal":"...","numero_processo":"..."}'
```

## Reportar problemas

Se um endpoint retornar erro, vazio ou dado inesperado, reporte (não desista calado): **POST /api/datajud/report** com `{ "message": "...", "context"?: "...", "conversation"?: [...] }`. Isso notifica o time da MCP.AI.

## Endpoints (4)

#### `datajud_get_processo`

Busca um processo pelo número único do CNJ (com ou sem máscara) em um tribunal. Retorna metadados + movimentações de cada instância encontrada. _(POST /api/datajud/get/processo)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tribunal` | string | Sim | Alias do tribunal no CNJ (índice api_publica_<alias>). Ex.: tjsp, trf1, stj, trt2, tre-sp. Obrigatório — cada tribunal é um índice separado. (tst, stj, tse, stm, trf1, trf2, trf3, trf4, trf5, trf6, tjac, tjal, tjam, tjap, tjba, tjce, tjdft, tjes, tjgo, tjma, tjmg, tjms, tjmt, tjpa, tjpb, tjpe, tjpi, tjpr, tjrj, tjrn, tjro, tjrr, tjrs, tjsc, tjse, tjsp, tjto, trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8, trt9, trt10, trt11, trt12, trt13, trt14, trt15, trt16, trt17, trt18, trt19, trt20, trt21, trt22, trt23, trt24, tre-ac, tre-al, tre-am, tre-ap, tre-ba, tre-ce, tre-df, tre-es, tre-go, tre-ma, tre-mg, tre-ms, tre-mt, tre-pa, tre-pb, tre-pe, tre-pi, tre-pr, tre-rj, tre-rn, tre-ro, tre-rr, tre-rs, tre-sc, tre-se, tre-sp, tre-to, tjmmg, tjmrs, tjmsp) |
| `numero_processo` | string | Sim | Número único do processo (CNJ), com ou sem máscara. |

#### `datajud_movimentos`

Retorna apenas a timeline de movimentações (+ metadados) de um processo — ideal pra detectar se houve movimentação nova. _(POST /api/datajud/movimentos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tribunal` | string | Sim | Alias do tribunal no CNJ (índice api_publica_<alias>). Ex.: tjsp, trf1, stj, trt2, tre-sp. Obrigatório — cada tribunal é um índice separado. (tst, stj, tse, stm, trf1, trf2, trf3, trf4, trf5, trf6, tjac, tjal, tjam, tjap, tjba, tjce, tjdft, tjes, tjgo, tjma, tjmg, tjms, tjmt, tjpa, tjpb, tjpe, tjpi, tjpr, tjrj, tjrn, tjro, tjrr, tjrs, tjsc, tjse, tjsp, tjto, trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8, trt9, trt10, trt11, trt12, trt13, trt14, trt15, trt16, trt17, trt18, trt19, trt20, trt21, trt22, trt23, trt24, tre-ac, tre-al, tre-am, tre-ap, tre-ba, tre-ce, tre-df, tre-es, tre-go, tre-ma, tre-mg, tre-ms, tre-mt, tre-pa, tre-pb, tre-pe, tre-pi, tre-pr, tre-rj, tre-rn, tre-ro, tre-rr, tre-rs, tre-sc, tre-se, tre-sp, tre-to, tjmmg, tjmrs, tjmsp) |
| `numero_processo` | string | Sim | Número único do processo (CNJ). |

#### `datajud_raw_query`

Avançado: envia um corpo de query Elasticsearch cru pro índice do tribunal (escape hatch). Use search_after pra paginar além de 10k. Resposta inclui raw_data. _(POST /api/datajud/raw/query)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tribunal` | string | Sim | Alias do tribunal no CNJ (índice api_publica_<alias>). Ex.: tjsp, trf1, stj, trt2, tre-sp. Obrigatório — cada tribunal é um índice separado. (tst, stj, tse, stm, trf1, trf2, trf3, trf4, trf5, trf6, tjac, tjal, tjam, tjap, tjba, tjce, tjdft, tjes, tjgo, tjma, tjmg, tjms, tjmt, tjpa, tjpb, tjpe, tjpi, tjpr, tjrj, tjrn, tjro, tjrr, tjrs, tjsc, tjse, tjsp, tjto, trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8, trt9, trt10, trt11, trt12, trt13, trt14, trt15, trt16, trt17, trt18, trt19, trt20, trt21, trt22, trt23, trt24, tre-ac, tre-al, tre-am, tre-ap, tre-ba, tre-ce, tre-df, tre-es, tre-go, tre-ma, tre-mg, tre-ms, tre-mt, tre-pa, tre-pb, tre-pe, tre-pi, tre-pr, tre-rj, tre-rn, tre-ro, tre-rr, tre-rs, tre-sc, tre-se, tre-sp, tre-to, tjmmg, tjmrs, tjmsp) |
| `query` | string | Sim | Objeto Elasticsearch Query DSL (ex.: { match_all: {} }). |
| `size` | integer | Não |  |
| `from` | integer | Não |  |
| `sort` | string | Não | Array de sort do Elasticsearch. |
| `search_after` | string | Não | Cursor (valor sort do último hit) pra paginação profunda. |

#### `datajud_search`

Busca processos em um tribunal por classe, órgão julgador e/ou assunto (códigos das tabelas do CNJ), paginada e ordenada por data de ajuizamento. DataJud NÃO indexa nome de parte nem OAB — pra isso us _(POST /api/datajud/search)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tribunal` | string | Sim | Alias do tribunal no CNJ (índice api_publica_<alias>). Ex.: tjsp, trf1, stj, trt2, tre-sp. Obrigatório — cada tribunal é um índice separado. (tst, stj, tse, stm, trf1, trf2, trf3, trf4, trf5, trf6, tjac, tjal, tjam, tjap, tjba, tjce, tjdft, tjes, tjgo, tjma, tjmg, tjms, tjmt, tjpa, tjpb, tjpe, tjpi, tjpr, tjrj, tjrn, tjro, tjrr, tjrs, tjsc, tjse, tjsp, tjto, trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8, trt9, trt10, trt11, trt12, trt13, trt14, trt15, trt16, trt17, trt18, trt19, trt20, trt21, trt22, trt23, trt24, tre-ac, tre-al, tre-am, tre-ap, tre-ba, tre-ce, tre-df, tre-es, tre-go, tre-ma, tre-mg, tre-ms, tre-mt, tre-pa, tre-pb, tre-pe, tre-pi, tre-pr, tre-rj, tre-rn, tre-ro, tre-rr, tre-rs, tre-sc, tre-se, tre-sp, tre-to, tjmmg, tjmrs, tjmsp) |
| `classe_codigo` | integer | Não | Código da classe processual (tabela CNJ). |
| `orgao_julgador_codigo` | integer | Não | Código do órgão julgador. |
| `assunto_codigo` | integer | Não | Código do assunto (tabela CNJ). |
| `numero_processo` | string | Não | Filtra por número de processo (dígitos). |
| `size` | integer | Não | Resultados por página (default 10, máx 100). |
| `from` | integer | Não | Offset de paginação (janela ES limitada a ~10k). |
| `sort_desc` | boolean | Não | Ordenar por dataAjuizamento decrescente (default crescente). |

---

Este MCP também funciona via **conexão MCP** (Claude / Cursor) em `https://api.mcp.ai/p_datajud` — veja o [README](../../README.md). A skill acima é pra consumir a **REST API** direto (agente próprio / código).
