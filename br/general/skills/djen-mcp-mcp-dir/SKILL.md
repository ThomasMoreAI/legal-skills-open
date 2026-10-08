---
name: djen-mcp-mcp-dir
title: DJEN (Diário de Justiça) — REST API skill
description: 'Skill da REST API do DJEN (Diário de Justiça) na MCP.AI: 3 endpoints em /api/djen. Diário de Justiça Eletrônico Nacional (CNJ), publicações e intimações judiciais. Busca por OAB, nome de advogado, número de processo, tribunal e data; cada resultado traz o texto completo e o link da certidão. Sem credencial; hospedado pela plataforma. (Diário de Justiça, não é base de jurisprudência/ementas.) Autentique com workspace API key (sk_live) gerada em app.mcp.ai/settings/api-keys. Use quando o usuário pedir algo coberto pelos endpoints.'
author: mcp-dir
author_url: https://github.com/mcp-dir/djen-mcp/tree/main/skills/djen-mcp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# DJEN (Diário de Justiça) — REST API skill

Você tem acesso à **DJEN (Diário de Justiça)** REST API na MCP.AI.

> Diário de Justiça Eletrônico Nacional (CNJ), publicações e intimações judiciais. Busca por OAB, nome de advogado, número de processo, tribunal e data; cada resultado traz o texto completo e o link da certidão. Sem credencial; hospedado pela plataforma. (Diário de Justiça, não é base de jurisprudência/ementas.)

## Base URL

```
https://api.mcp.ai/api/djen
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
curl -X POST https://api.mcp.ai/api/djen/get/certidao \
  -H "Authorization: Bearer sk_live_..." \
  -H "Content-Type: application/json" \
  -d '{"hash":"..."}'
```

## Reportar problemas

Se um endpoint retornar erro, vazio ou dado inesperado, reporte (não desista calado): **POST /api/djen/report** com `{ "message": "...", "context"?: "...", "conversation"?: [...] }`. Isso notifica o time da MCP.AI.

## Endpoints (3)

#### `djen_get_certidao`

Retorna a URL da certidão (PDF) de uma comunicação do DJEN pelo seu hash (campo `hash` retornado na busca). _(POST /api/djen/get/certidao)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `hash` | string | Sim | Hash da comunicação (campo hash da busca). |

#### `djen_processos_por_parte`

DESCOBERTA por NOME de parte (grátis, sem captcha): busca o DJEN por quem figura no processo e agrupa por número — devolve a lista de processos da pessoa/empresa, com partes e tribunal. _(POST /api/djen/processos/por/parte)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome_parte` | string | Sim | Nome da parte (pessoa ou razão social) a procurar. |
| `sigla_tribunal` | string | Não | Restringe a um tribunal (ex.: TJSP). |
| `data_inicio` | string | Não | Data inicial (AAAA-MM-DD). |
| `data_fim` | string | Não | Data final (AAAA-MM-DD). |
| `itens_por_pagina` | integer | Não | Comunicações a varrer por página (default 100). |
| `pagina` | integer | Não | Página (default 1). |

#### `djen_search_comunicacoes`

Busca publicações/intimações no Diário de Justiça Eletrônico Nacional (DJEN) por OAB, nome de advogado, número de processo, tribunal e data. _(POST /api/djen/search/comunicacoes)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `numero_oab` | string | Não | Número da OAB (ex.: 21076). |
| `uf_oab` | string | Não | UF da OAB (ex.: SP). |
| `nome_advogado` | string | Não | Nome do advogado. |
| `nome_parte` | string | Não | Nome da PARTE (pessoa ou empresa) — busca por quem figura no processo, não pelo advogado. Use para descobrir processos de alguém pelo nome. |
| `numero_processo` | string | Não | Número do processo (dígitos). |
| `sigla_tribunal` | string | Não | Sigla do tribunal (ex.: TJSP, TRT5, TST, CJF). |
| `data_inicio` | string | Não | Data de disponibilização inicial (AAAA-MM-DD). |
| `data_fim` | string | Não | Data de disponibilização final (AAAA-MM-DD). |
| `meio` | string | Não | Meio: "D" (Diário) ou "E" (Edital). |
| `texto` | string | Não | Busca por termo no texto. |
| `pagina` | integer | Não | Página (default 1). |
| `itens_por_pagina` | integer | Não | Itens por página (default ~100; mín. efetivo 5). |

---

Este MCP também funciona via **conexão MCP** (Claude / Cursor) em `https://api.mcp.ai/p_djen` — veja o [README](../../README.md). A skill acima é pra consumir a **REST API** direto (agente próprio / código).
