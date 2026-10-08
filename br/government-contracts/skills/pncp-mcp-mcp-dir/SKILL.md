---
name: pncp-mcp-mcp-dir
title: PNCP — REST API skill
description: 'Skill da REST API do PNCP na MCP.AI: 13 endpoints em /api/pncp. Consulta de licitações e contratações públicas no Brasil (PNCP): busca de editais e pregões por palavra-chave, estado e modalidade, oportunidades com filtro de faixa de valor, detalhe da contratação com itens e preços, documentos do edital (link do PDF e texto), contratos, atas de registro de preços e planejamento anual. Hospedado pela plataforma, sem credenciais. Autentique com workspace API key (sk_live) gerada em app.mcp.ai/settings/api-keys. Use quando o usuário pedir algo coberto pelos endpoints.'
author: mcp-dir
author_url: https://github.com/mcp-dir/pncp-mcp/tree/main/skills/pncp-mcp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: government-contracts
language: pt
---

# PNCP — REST API skill

Você tem acesso à **PNCP** REST API na MCP.AI.

> Consulta de licitações e contratações públicas no Brasil (PNCP): busca de editais e pregões por palavra-chave, estado e modalidade, oportunidades com filtro de faixa de valor, detalhe da contratação com itens e preços, documentos do edital (link do PDF e texto), contratos, atas de registro de preços e planejamento anual. Hospedado pela plataforma, sem credenciais.

## Base URL

```
https://api.mcp.ai/api/pncp
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
curl -X POST https://api.mcp.ai/api/pncp/arquivos \
  -H "Authorization: Bearer sk_live_..." \
  -H "Content-Type: application/json" \
  -d '{"cnpj":"...","ano":"...","sequencial":"..."}'
```

## Reportar problemas

Se um endpoint retornar erro, vazio ou dado inesperado, reporte (não desista calado): **POST /api/pncp/report** com `{ "message": "...", "context"?: "...", "conversation"?: [...] }`. Isso notifica o time da MCP.AI.

## Endpoints (13)

#### `pncp_arquivos`

Documentos de uma licitação/edital (edital, termo de referência, anexos) com o LINK de download de cada arquivo (em geral PDF). _(POST /api/pncp/arquivos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ do órgão (com ou sem máscara). |
| `ano` | string | Sim | Ano da contratação (ex.: 2026). |
| `sequencial` | string | Sim | Número sequencial da contratação no órgão. |

#### `pncp_atas`

Lista atas de registro de preços vigentes num período (referência de preços praticados pelo governo), opcionalmente por órgão (CNPJ). _(POST /api/pncp/atas)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `data_inicial` | string | Sim | Data inicial (AAAA-MM-DD). |
| `data_final` | string | Sim | Data final (AAAA-MM-DD). |
| `cnpj` | string | Não | CNPJ do órgão. Opcional. |
| `pagina` | integer | Não | Página (default 1). |
| `tamanho_pagina` | integer | Não | Itens por página (default 20, máx 50). |

#### `pncp_buscar`

Busca licitações por PALAVRA-CHAVE no objeto (cobertura NACIONAL ampla, índice full-text), em editais, atas ou contratos. _(POST /api/pncp/buscar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Não | Palavra-chave do objeto (ex.: 'material de informática', 'merenda escolar'). Use isto OU `termos[]`. |
| `termos` | string[] | Não | VÁRIAS palavras-chave: cada uma vira uma busca full-text independente, disparadas com um pequeno intervalo entre si (evita rate limit da fonte) e os resultados são fundidos e deduplicados. Ex.: ['notebook','ultrabook','laptop']. Prefira isto a repetir a tool termo a termo. |
| `tipo` | string | Não | Tipo de documento a buscar. Default edital. (edital, ata, contrato) |
| `ordenacao` | string | Não | Ordenação (ex.: '-data' mais recentes primeiro, 'data' mais antigos). Default '-data'. |
| `status` | string | Não | Filtro de situação (ex.: 'todos', 'recebendo_proposta', 'encerradas'). Default 'todos'. |
| `pagina` | integer | Não | Página (default 1). |
| `tam_pagina` | integer | Não | Itens por página (default 20, máx 50). |

#### `pncp_contratos`

Lista contratos públicos firmados num período, opcionalmente filtrando por órgão (CNPJ). _(POST /api/pncp/contratos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `data_inicial` | string | Sim | Data inicial (AAAA-MM-DD). |
| `data_final` | string | Sim | Data final (AAAA-MM-DD). |
| `cnpj_orgao` | string | Não | CNPJ do órgão. Opcional. |
| `pagina` | integer | Não | Página (default 1). |
| `tamanho_pagina` | integer | Não | Itens por página (default 20, máx 50). |

#### `pncp_detalhe`

Detalhe completo de uma licitação/contratação a partir de cnpj+ano+sequencial (a referência devolvida pela pncp_buscar). _(POST /api/pncp/detalhe)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ do órgão (com ou sem máscara). |
| `ano` | string | Sim | Ano da contratação (ex.: 2026). |
| `sequencial` | string | Sim | Número sequencial da contratação no órgão. |
| `itens` | boolean | Não | Se true, também traz os itens com preços. Default false. |
| `resultado` | boolean | Não | Se true, anexa o bloco `resultado` com o(s) vencedor(es) homologado(s) (CNPJ, valor real, natureza jurídica, porte). Default false. Ou use pncp_resultado direto. |

#### `pncp_historico`

Arquivo histórico de licitações: consulta editais que a plataforma acumulou ao longo do tempo (inclusive os que já encerraram ou saíram do ar), por PALAVRA-CHAVE no objeto, estado (UF), modalidade, si _(POST /api/pncp/historico)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Não | Palavra-chave no objeto (ex.: 'software'). Opcional. |
| `uf` | string | Não | Sigla do estado (ex.: SP). Opcional. |
| `modalidade` | string | Não | Modalidade (ex.: 'Pregão'). Opcional. |
| `situacao` | string | Não | Situação (ex.: 'Divulgada'). Opcional. |
| `valor_min` | number | Não | Valor estimado MÍNIMO em R$ (opcional). |
| `valor_max` | number | Não | Valor estimado MÁXIMO em R$ (opcional). |
| `desde` | string | Não | Publicação a partir de (AAAA-MM-DD). Opcional. |
| `ate` | string | Não | Publicação até (AAAA-MM-DD). Opcional. |
| `pagina` | integer | Não | Página (default 1). |
| `tam_pagina` | integer | Não | Itens por página (default 20, máx 100). |

#### `pncp_listar`

Busca PRINCIPAL de licitações abertas por palavra-chave, faixa de VALOR, estado, modalidade e período. _(POST /api/pncp/listar)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termos` | string[] | Não | Palavras-chave/frases no objeto (casa QUALQUER uma = OR). SEMPRE expanda o conceito em VÁRIOS sinônimos, NUNCA um termo só. Ex.: pra 'software' use ['software','saas','licença de uso','licenciamento de software','sistema de informação','aplicativo','software como serviço']. PREFIRA termos específicos/frases curtas pra não casar boilerplate (evite 'sistema' sozinho). |
| `data_inicial` | string | Não | Data inicial (AAAA-MM-DD). Opcional (default: 7 dias atrás). |
| `data_final` | string | Não | Data final (AAAA-MM-DD). Opcional (default: hoje). |
| `modalidade` | integer | Não | Código da modalidade (ex.: 6 = Pregão Eletrônico). Opcional: omita pra varrer as comuns. |
| `apenas_abertas` | boolean | Não | Se true, só licitações ainda recebendo proposta (abertas pra participar). |
| `uf` | string | Não | Sigla do estado (ex.: SP, MG). |
| `municipio` | string | Não | Código IBGE do município (7 dígitos). Opcional. |
| `cnpj` | string | Não | CNPJ do órgão. |
| `valor_min` | number | Não | Valor estimado MÍNIMO em R$. |
| `valor_max` | number | Não | Valor estimado MÁXIMO em R$. |
| `ordenacao` | string | Não | Ordenar por: data (recentes 1º) ou prazo (fecha 1º). Por padrão já vem ranqueado por VALOR (maior 1º) quando incluir_valor está ligado. (data, valor, prazo) |
| `tamanho_pagina` | integer | Não | Quantos retornar (default 20, máx 50). |
| `pagina` | integer | Não | Página (1-based, 20 por página). Default 1. A resposta traz `total_paginas`; chame de novo com pagina=2, 3... pra pegar mais. |
| `incluir_valor` | boolean | Não | Enriquecer cada item com o VALOR estimado e ranquear por valor (default TRUE). Passe false pra uma lista mais rápida/barata sem valor. |
| `expandir` | boolean | Não | Expandir os termos em sinônimos automaticamente (default TRUE). Passe false pra buscar só os termos exatos que você mandou. |

#### `pncp_oportunidades`

Busca de OPORTUNIDADES de licitação (editais/pregões) com filtros ricos por palavra-chave, FAIXA DE VALOR da compra, UFs, modalidades, portais, registro de preço, participação exclusiva ME/EPP e super _(POST /api/pncp/oportunidades)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termos` | string[] | Não | Palavras-chave/frases no objeto (casa QUALQUER uma = OR). SEMPRE expanda em VÁRIOS sinônimos, NUNCA um só. Ex.: pra 'software' use ['software','saas','licença de uso','licenciamento de software','sistema de informação','software como serviço']. Mesmo formato de pncp_listar. |
| `termo` | string | Não | Alternativa a `termos`: palavra(s)-chave numa string só (separe várias por ';'). Opcional. |
| `excluir` | string | Não | Palavras-chave a EXCLUIR do resultado. Opcional. |
| `data_inicial` | string | Não | Data inicial do período (AAAA-MM-DD). Opcional. |
| `data_final` | string | Não | Data final do período (AAAA-MM-DD). Opcional. |
| `tipo_periodo` | string | Não | A qual data o período se refere. Default 'abertura'. (abertura, publicacao, encerramento) |
| `valor_min` | number | Não | Valor MÍNIMO estimado da compra em R$ (0 = sem mínimo). |
| `valor_max` | number | Não | Valor MÁXIMO estimado da compra em R$ (0 = sem máximo). |
| `ufs` | string[] | Não | Estados (siglas, ex.: ['SP','MG']). Vazio = todos. |
| `modalidades` | integer[] | Não | Códigos de modalidade (ex.: 6 = Pregão Eletrônico). Vazio = todas. |
| `portais` | string[] | Não | Filtra por portais específicos. Opcional. |
| `superoportunidades` | boolean | Não | Se true, só as marcadas como superoportunidade. |
| `participacao_exclusiva` | boolean | Não | Se true, só licitações exclusivas para ME/EPP. |
| `excluir_registro_preco` | boolean | Não | Se true, exclui licitações de registro de preço. |
| `somente_sigilosos` | boolean | Não | Se true, só com valores sigilosos. |
| `itens_desertos` | boolean | Não | Se true, inclui itens desertos. |
| `tipo_item` | string | Não | Filtra por tipo de item. Opcional. (, MATERIAL, SERVICO) |
| `pesquisa_ampla` | boolean | Não | Busca ampla no objeto (default true). |
| `expandir` | boolean | Não | Expandir os termos em sinônimos automaticamente (default TRUE). false = só os termos exatos. |
| `pagina` | integer | Não | Página (1-based, 20 por página). Default 1. |

#### `pncp_orgaos`

Busca de ÓRGÃOS/entidades compradoras por nome, UF e/ou portal. _(POST /api/pncp/orgaos)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `termo` | string | Não | Nome (parte) do órgão. Termo amplo demais falha, refine. Use isto OU `termos[]`. |
| `termos` | string[] | Não | Vários nomes de órgão: cada um vira uma busca independente, disparadas com um intervalo entre si (evita rate limit da fonte), resultados fundidos e deduplicados. Opcional. |
| `uf` | string | Não | Sigla do estado (ex.: SP). Opcional. |
| `portais` | string[] | Não | Portais (ex.: ['CN']). Opcional. |
| `antecipagov` | boolean | Não | Se true, consulta a base do AntecipaGov (hierarquia órgão superior). |
| `pagina` | integer | Não | Página (1-based). Default 1. |

#### `pncp_pca`

Plano anual de contratações (PCA) por ano e classificação superior do catálogo: o que os órgãos planejam contratar no ano. _(POST /api/pncp/pca)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `ano_pca` | integer | Sim | Ano do PCA (ex.: 2026). |
| `codigo_classificacao_superior` | integer | Sim | Código da classificação superior do item no catálogo. |
| `pagina` | integer | Não | Página (default 1). |
| `tamanho_pagina` | integer | Não | Itens por página (default 20, máx 50). |

#### `pncp_processo`

Detalhe de oportunidade(s) por `id` (de pncp_listar/pncp_oportunidades). _(POST /api/pncp/processo)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `id` | string | Não | id de UMA oportunidade → detalhe completo com itens. Use `id` OU `ids`. |
| `ids` | string[] | Não | LOTE: vários `id` (de pncp_listar/pncp_oportunidades). Detalha todos numa chamada e devolve RANKING por valor (maior 1º). Ideal pra 'ranquear por valor'. Máx 50. |

#### `pncp_resultado`

Quem GANHOU a licitação: o(s) fornecedor(es) vencedor(es) homologado(s) a partir de cnpj+ano+sequencial (a referência da pncp_buscar). _(POST /api/pncp/resultado)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ do órgão (com ou sem máscara). |
| `ano` | string | Sim | Ano da contratação (ex.: 2026). |
| `sequencial` | string | Sim | Número sequencial da contratação no órgão. |
| `numero_item` | integer | Não | Número de um item específico. Omita pra agregar todos os itens da compra. |

#### `pncp_texto`

Texto INTEIRO do edital em markdown (com marcadores '## Página N'), pra você RESUMIR ou ler o documento todo. _(POST /api/pncp/texto)_

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `cnpj` | string | Sim | CNPJ do órgão (com ou sem máscara). |
| `ano` | string | Sim | Ano da contratação (ex.: 2026). |
| `sequencial` | string | Sim | Número sequencial da contratação no órgão. |
| `documento` | string | Não | Sequencial de um anexo específico. Default: o edital principal. |
| `de_pagina` | integer | Não | Página inicial (pra editais grandes). Opcional. |
| `ate_pagina` | integer | Não | Página final. Opcional. |

---

Este MCP também funciona via **conexão MCP** (Claude / Cursor) em `https://api.mcp.ai/p_pncp` — veja o [README](../../README.md). A skill acima é pra consumir a **REST API** direto (agente próprio / código).
