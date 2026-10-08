---
name: tjsc-mcp-mcp-dir
title: Jurisprudência TJSC — REST API skill
description: 'Pesquisa de jurisprudência do Tribunal de Justiça de Santa Catarina (TJSC) e de mais 16 tribunais brasileiros: acórdãos, decisões e súmulas por termo ou tese, com o trecho que casou a busca, o link oficial e leitura do inteiro teor quando disponível. Use sempre que o usuário pedir precedente, jurisprudência, súmula ou entendimento de tribunal. Restrinja com tribunais:["TJSC"] quando ele indicar TJSC, e compare com as cortes superiores quando a pergunta pedir. Zero resultado costuma ser vocabulário, não ausência: tente os termos alternativos que a resposta sugere antes de afirmar que a tese não existe, e nunca trate aviso de indisponibilidade como inexistência. Grátis, sem login. Orquestra jurisprudencia_buscar, jurisprudencia_sumulas e jurisprudencia_documento em https://api.mcp.ai/p_tjsc.'
author: mcp-dir
author_url: https://github.com/mcp-dir/tjsc-mcp/tree/main/skills/tjsc-mcp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: criminal
language: pt
---

# Jurisprudência TJSC — REST API skill

Você tem acesso à **Jurisprudência TJSC** REST API na MCP.AI.

> Pesquise jurisprudência do TJSC direto do Claude, ChatGPT ou do seu agente. Cada decisão traz órgão julgador, relator, data, o trecho que casou a busca e o link no site oficial. Decisão em segredo de justiça aparece com a ementa anonimizada, como o próprio tribunal publica. A mesma conexão alcança outros 16 tribunais. Grátis, sem login.

## Base URL

```
https://api.mcp.ai/api/jurisprudencia
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
curl -X POST https://api.mcp.ai/api/jurisprudencia/buscar \
  -H "Authorization: Bearer sk_live_..." \
  -H "Content-Type: application/json" \
  -d '{"termo":"..."}'
```

## Reportar problemas

Se um endpoint retornar erro, vazio ou dado inesperado, reporte (não desista calado): **POST /api/jurisprudencia/report** com `{ "message": "...", "context"?: "...", "conversation"?: [...] }`. Isso notifica o time da MCP.AI.

## Endpoints (3)

#### `jurisprudencia_buscar`

Busca jurisprudência (acórdãos, súmulas, orientações jurisprudenciais, temas) por termo ou tese. _(POST /api/jurisprudencia/buscar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Sim | Termo, tese ou assunto (ex.: 'dano moral assédio', "horas extras" -sumula). |
| `tipo` | string | Não | Filtra por tipo de documento (ex.: "Acórdão", "Súmula", "Orientação Jurisprudencial"). |
| `tribunais` | string[] | Não | Siglas de tribunal para restringir a busca no acervo próprio (ex.: ["TST"]). |
| `data_de` | string | Não | Publicação a partir de (AAAA-MM-DD). |
| `data_ate` | string | Não | Publicação até (AAAA-MM-DD). |
| `ordenar` | string | Não | Ordem do acervo próprio (default relevancia). (relevancia, recencia) |
| `max` | integer | Não | Resultados (default 10, máx 30). |

#### `jurisprudencia_documento`

Lê o INTEIRO TEOR de uma decisão do acervo próprio (texto completo do acórdão, não o resumo). _(POST /api/jurisprudencia/documento)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `id` | string | Não | Campo `id` do resultado de jurisprudencia_buscar (origem=indice). |
| `numeracao` | string | Não | Número CNJ do processo (ex.: 0020620-65.2022.5.04.0021). |
| `tribunal` | string | Não | Sigla do tribunal, para desambiguar quando busca por numeração. |
| `ids` | string[] | Não | Bulk mode: multiple values for id |

#### `jurisprudencia_sumulas`

Busca SÚMULAS (incluindo vinculantes) por termo. _(POST /api/jurisprudencia/sumulas)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Sim | Termo/assunto da súmula. |
| `max` | integer | Não | Resultados (default 10, máx 30). |

---

Este MCP também funciona via **conexão MCP** (Claude / Cursor) em `https://api.mcp.ai/p_tjsc` — veja o [README](../../README.md). A skill acima é pra consumir a **REST API** direto (agente próprio / código).
