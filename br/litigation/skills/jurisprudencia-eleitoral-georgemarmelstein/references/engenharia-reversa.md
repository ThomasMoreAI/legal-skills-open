# Engenharia Reversa — Jurisprudência da Justiça Eleitoral (TSE)

> Investigação empírica feita via Chrome MCP em 10/07/2026 sobre
> `https://jurisprudencia.tse.jus.br` (SPA Angular) e sua API `sjur-pesquisa`.
> Todos os números abaixo foram obtidos por chamadas reais ao endpoint.

## 1. Arquitetura do sistema

| Camada | Endereço |
|--------|----------|
| Front-end (SPA Angular) | `https://jurisprudencia.tse.jus.br` |
| API de busca | `https://sjur-pesquisa-api.tse.jus.br/tse/sjur-pesquisa-backend/rest/public/pesquisa` |
| API de serviços (PDF etc.) | `https://sjur-servicos.tse.jus.br/sjur-servicos/rest/` |
| Autenticação (área logada) | `https://autenticaje.tse.jus.br/auth/` |
| Código-fonte do front | `git.tse.jus.br/judiciaria/sedesc1/sjur-pesquisa-frontend` (repo interno) |

O front é um SPA que monta uma **query Elasticsearch** e a envia para a API. A API é
um backend Spring sobre Elasticsearch (o `termoPesquisa` é um `bool/must/query_string`
sobre ~108 campos).

## 2. BLOQUEIO CRÍTICO: hCaptcha invisível obrigatório na busca

- A busca **exige** o campo `captchaToken` no corpo. Sem ele (ou com valor vazio) →
  `{"mensagem":"Falha ao validar o HCaptcha."}` e `totalRegistros: 0`.
- É **hCaptcha invisível** (iframe `#frame=checkbox-invisible`), sitekey
  `755c2e18-4bf4-4f28-b992-8c64b77c46b8`.
- O token é **de uso único**: reenviar o mesmo token → "Falha ao validar o HCaptcha".
- **Cada busca precisa de um token novo.**

### Consequência arquitetural
Um MCP Python puro (httpx/requests), padrão da skill `criar-mcp-precedente`, **não
funciona** para a BUSCA: não há como gerar tokens hCaptcha fora de um navegador real.

### Caminho comprovado que FUNCIONA
Dentro de um navegador real, `await window.hcaptcha.execute({async:true})` gera um token
válido silenciosamente (sem desafio interativo — o score do hCaptcha invisível passa),
e a busca retorna resultados reais. Testado com mints consecutivos (dezenas de buscas
seguidas) — 100% de sucesso no Chrome real do usuário.

## 3. Contrato da API de busca

`POST https://sjur-pesquisa-api.tse.jus.br/tse/sjur-pesquisa-backend/rest/public/pesquisa`
`Content-Type: application/json`

```json
{
  "refinaTermos": [],
  "refinaData": [],
  "termoPesquisa": "<STRING com JSON de query Elasticsearch>",
  "pagina": 0,
  "tamanho": 25,
  "tribunais": ["tse"],
  "captchaToken": "<token hCaptcha de uso único>",
  "ordenacao": "dj_desc",
  "refinamento": []
}
```

- `termoPesquisa` é um **JSON serializado como string**:
  ```json
  {"bool":{"must":[{"query_string":{
     "query":"<expressão do usuário>",
     "default_operator":"AND",
     "fields":["textoEmenta","textoDecisao","textoIndexacao", ...]}}]}}
  ```
- `ordenacao`: `dj_desc` (data julgamento desc), também há asc / relevância.
- `tribunais`: **na prática é IGNORADO neste endpoint** — ver seção 5.
- `pagina` começa em 0; `tamanho` = itens por página.

### Resposta (campos úteis por item em `content[]`)
`codigoDecisao` (id p/ baixar PDF), `numeroProcesso`, `numeroUnico` (nº CNJ),
`numeroDecisao`, `dataDecisao`, `anoEleicao`, `siglaClasse`, `descricaoClasse`,
`siglaUF`, `nomeMunicipio`, `siglaTipoProcesso`, `nomeTipoProcesso`,
`siglaTribunalJE`, `temInteiroTeorPDF`, `temInteiroTeorAudio`,
`textoEmenta` (ementa completa inline!), `textoDecisao` (texto da decisão inline!),
`relatores[]` (`nome`, `autoridade`, `competencia`, `descricaoCompleta`),
`partes[]`, `publicacoes[]`, `indexacoes[]`, `assuntos[]`, `sumulas[]`, `precedentes[]`.
- `totalRegistros`: total de resultados.
- `aggs`: facetas (0=selecionada S/N, 1=tribunal, 2=classe, 3=tipoDecisão,
  4=relator, 5=ano, 6=assunto, 7=eleição, 8=legislação, 9=UF, 10/11=anotação, 12=fonte).

## 4. Sintaxe booleana (Elasticsearch `query_string`) — TESTADA EMPIRICAMENTE

A barra de operadores da UI (`E OU NÃO * ? "" ""~ ~ : ^ + - () [] {}`) é **traduzida
pelo front** para a sintaxe Lucene/Elasticsearch. Enviados crus à API, os operadores em
português (`E`/`OU`/`NÃO`) são tratados como **termos literais**, não como operadores.

**Para acesso direto à API use operadores em INGLÊS / símbolos:**

| Operador | Sintaxe que funciona na API | Prova (query base "propaganda"=45.880 / "eleitoral"=190.122) |
|----------|-----------------------------|-------------------------------------------------------------|
| AND | `AND`, `&&`, ` ` (default), `+` | `propaganda AND eleitoral` = 44.773 |
| OR | `OR`, `\|\|` | `propaganda OR eleitoral` = 191.229 |
| NOT | `NOT`, `-` | `propaganda NOT eleitoral` = `propaganda -eleitoral` = 1.107 |
| Frase exata | `"..."` | `"propaganda eleitoral"` = 36.934 |
| Proximidade | `"..."~N` | `"propaganda eleitoral"~10` = 39.224 |
| Curinga sufixo/meio | `*` | `eleitor*` = 192.867 |
| Curinga 1 caractere | `?` | `propagand?` = 45.889 |
| Fuzzy | `termo~` | `eleitorais~` = 192.185 |
| Campo específico | `campo:termo` | `textoEmenta:propaganda` = 9.972 |
| Boost | `termo^N` | (padrão Lucene) |
| Agrupamento | `( )` | `(propaganda OR outdoor) AND eleitoral` = 44.811 |
| Intervalo | `[ ]` inclusivo, `{ }` exclusivo | (padrão Lucene, p/ datas/números) |

**NÃO funcionam crus na API** (viram termo): `E`, `OU`, `NÃO`.
→ O MCP deve **normalizar** ` E `→` AND `, ` OU `→` OR `, ` NÃO `→` NOT ` antes de enviar,
para o usuário poder digitar em português como no site.

## 5. Multi-tribunal (TSE + TREs) — DOIS TENANTS no mesmo backend

O "tenant" fica no **caminho da URL**. Há **dois portais/tenants**, mesmo backend, mesmo
contrato, mesmo mecanismo de captcha:

| Tenant | Front-end | Endpoint de busca |
|--------|-----------|-------------------|
| `tse` | `jurisprudencia.tse.jus.br` | `.../tse/sjur-pesquisa-backend/rest/public/pesquisa` |
| `tres` | `jurisprudencia-tres.tse.jus.br` | `.../tres/sjur-pesquisa-backend/rest/public/pesquisa` |

- O tenant **`tres` FEDERA os 27 TREs numa única chamada** (comprovado: a faceta
  `aggs.1` lista `TRE-AC … TRE-SP`, todos os 27; "inelegibilidade" = 79.299 resultados).
  O front dos TREs manda `tribunais: ["tre-*"]` (curinga = todos).
- O portal `tse` é exclusivo do TSE (faceta só mostra `TSE`).
- **O campo `tribunais` do corpo NÃO filtra** por tribunal específico em nenhum tenant
  (enviar `["tre-sp"]` ainda retorna todos os 27). É provavelmente decorativo/legado.

### Como filtrar por um TRE específico → pelo PRÓPRIO query_string (comprovado)
Injetar o campo indexado `siglaTribunalJE` na expressão:
- `inelegibilidade AND siglaTribunalJE:"TRE-SP"` → 12.273 (todos TRE-SP)
- `inelegibilidade AND siglaTribunalJE:"TRE-CE"` → 4.411 (todos TRE-CE)
Isso permite escopo por 1 TRE, por vários (`siglaTribunalJE:("TRE-SP" OR "TRE-CE")`),
ou por UF via `siglaUF:"SP"`.

### Cobertura "TSE + 27 TREs" = 2 chamadas
Uma ao tenant `tse` + uma ao tenant `tres`, com merge dos resultados. Simples.

### hCaptcha e domínio
Ambos os fronts usam `window.hcaptcha` (mesmo sitekey provável). O token é gerado no
domínio do front. Como o token é de uso único, **cada chamada gera o seu**; para o tenant
`tse` convém gerar em `jurisprudencia.tse.jus.br` e para `tres` em
`jurisprudencia-tres.tse.jus.br` (validar em build se um domínio serve os dois).

### Códigos dos 27 TREs (para filtro `siglaTribunalJE`)
TRE-AC, TRE-AL, TRE-AP, TRE-AM, TRE-BA, TRE-CE, TRE-DF, TRE-ES, TRE-GO, TRE-MA, TRE-MG,
TRE-MS, TRE-MT, TRE-PA, TRE-PB, TRE-PR, TRE-PE, TRE-PI, TRE-RJ, TRE-RN, TRE-RS, TRE-RO,
TRE-RR, TRE-SC, TRE-SP, TRE-SE, TRE-TO.

## 5b. Endpoints auxiliares e refinamento (do HAR do usuário)

Mesmo host/tenant, todos `POST ... /rest/public/pesquisa/<sub>`:

| Sub-rota | Corpo | Retorno |
|----------|-------|---------|
| `/classes` | `[]` | lista `{siglaClasse, descricaoClasse}` (688 itens) |
| `/relatorias` | `[]` | lista de relatores/juízes |
| `/eleicoes` | `[]` | lista de eleições |
| `/normas` | `[]` | lista de legislação |
| `/pesquisaTokenValidado` | igual a `/pesquisa` | variante de busca (mesmo corpo) |

**Headers obrigatórios** (CORS): `Content-Type: application/json`,
`Accept: application/json, text/plain, */*`, `Origin`/`Referer` = domínio do portal
(`https://jurisprudencia-tres.tse.jus.br` ou `https://jurisprudencia.tse.jus.br`).
→ Um `fetch` disparado **de dentro da própria página** já satisfaz Origin/Referer
automaticamente (mesma origem). Esse é o modo usado pela skill.

### Filtro por faceta via `refinamento` (modo oficial do front, do HAR)
Além de injetar `siglaTribunalJE:"TRE-XX"` no query_string, dá para usar o array
`refinamento` (ANDado à busca):
```json
"refinamento": [{"nome":"siglaTribunalJE.keyword",
                 "buckets":[{"key":"TRE-MG","docCount":1582,"checked":true}]}]
```
Facetas conhecidas (campo `.keyword`): `siglaTribunalJE`, `siglaClasse`,
`descricaoTipoDecisao`, `nomeMinistro`/relator, `anoEleicao`, `siglaUF`, etc.
Para a skill, o caminho mais simples e comprovado é **injetar no query_string**.

### hCaptcha (do HAR)
Fluxo: `checksiteconfig` → `getcaptcha/755c2e18-4bf4-4f28-b992-8c64b77c46b8` →
`hsw.js` (proof-of-work) → token (~1740–1780 chars). Sitekey
`755c2e18-4bf4-4f28-b992-8c64b77c46b8` é **compartilhado pelos dois tenants**.

## 6. Inteiro teor (PDF) — ABERTO, sem captcha

`GET https://sjur-servicos.tse.jus.br/sjur-servicos/rest/download/pdf/{codigoDecisao}`
→ `200`. **Não exige captcha.** Testado com `codigoDecisao=3522031` (baixado e aberto:
acórdão do TSE, 3 páginas, ED no AgR no AREspE 0600856-43.2024.6.15.0002, Lucena/PB).

> ⚠️ **PEGADINHA (comprovada em 11/07/2026): o corpo NÃO é um PDF puro.** O header
> diz `Content-Type: application/pdf`, mas o body é um **envelope `multipart/form-data`**.
> Salvar a resposta crua (ex.: `Invoke-WebRequest -OutFile` ou `requests ... .content`)
> gera um arquivo que **não abre** em leitor de PDF. Estrutura real do body:
> ```
> --D_SLNZ...<boundary dinâmico>
> Content-Disposition: form-data; name="file"; filename="inteiroTeor.pdf"
> Content-Type: application/octet-stream
>
> %PDF-1.7 ...            ← o PDF de verdade começa aqui (offset ~157)
> ...%%EOF
> --D_SLNZ...--           ← boundary de fechamento
> ```
> **Para obter um PDF abrível, desembrulhar:** (1) o boundary é a 1ª linha do corpo
> (`--...` até o 1º CRLF); (2) o PDF vai do 1º `%PDF` até logo antes do CRLF que precede
> o boundary de fechamento; grave só esse recorte. Alternativa robusta: parsear como
> `multipart/form-data` e extrair a parte `file`. Validar: header `%PDF-`, trailer `%%EOF`.

- Além disso, `textoEmenta` e `textoDecisao` já voltam **inline** na resposta da busca,
  então ementa e texto da decisão não dependem do PDF.

## 7. Decisões pendentes (levadas ao usuário)

1. **Arquitetura** (por causa do hCaptcha):
   - (A) Skill orquestrada por Chrome MCP — usa o navegador real do usuário para gerar
     tokens. Confiável (comprovado), leve, no padrão de `baixar-stj`/`capturar-sessao-pje`.
     Limitação: exige Chrome aberto durante a busca; roda por comando (ex.: `/buscar-tse`),
     não como MCP de fundo chamável por subagentes.
   - (B) MCP standalone com Playwright — servidor Python que embute um Chromium próprio,
     gera tokens in-page e chama a API. É um MCP "de verdade" (registrável no `.mcp.json`,
     como `bnp-api`). Porém mais pesado (dependência de navegador) e com risco de o
     score do hCaptcha invisível cair num perfil automatizado novo (→ desafio interativo).
2. **Escopo**: só TSE, ou TSE + alguns/todos os TREs (cada TRE = trabalho adicional de
   mapear host + sitekey).

## 8. Mapeamento do formulário avançado → Elasticsearch (minerado do bundle)

> Fonte: `main.ea4e094baa3ef7779bfd.js` (bundle Angular do front TSE), baixado em
> 11/07/2026 — asset estático, servido SEM captcha. O front guarda os templates de
> query do formulário de pesquisa avançada como constantes; grep por `t.[A-Z_]*=`
> revela como cada campo da UI vira cláusula Elasticsearch.
> **Nível de evidência: bundle (forte — é o código do próprio front), ainda SEM
> prova por contagens** (Chrome MCP indisponível na sessão da mineração). Antes de
> dar por definitivo, rodar sonda diferencial: mesma query com × sem o filtro.

| Campo da UI | Cláusula ES (template do bundle) | Campo indexado |
|-------------|----------------------------------|----------------|
| Relatores | `query_string` em `fields:["relatores.nome"]` (multi = OR) | `relatores.nome` |
| Partes | `query_string` em `fields:["partes.nomeParte"]` | `partes.nomeParte` |
| Classe | `terms` | `siglaClasse.keyword` |
| Tipo de decisão | `terms` | `descricaoTipoDecisao.keyword` |
| Eleição | `terms` | `anoEleicao` |
| UF | `terms` | `siglaUF.keyword` |
| Município | `term` | `nomeMunicipio.keyword` |
| Data julgamento | `range` gte/lte | `dataDecisao` |
| Data publicação | `range` gte/lte | `publicacoes.dataPublicacao` |
| Norma (legislação) | `match_phrase` com `slop: 2` | `referenciasLegislativas.legislacao` |
| Número | `query_string`/`wildcard` | `numeroProcesso`, `numeroDecisao`, `numeroUnico`, `numeroUnicoFormatado` |
| Ementa/decisão/indexação | `query_string` | `indexacoes`, `textoEmenta`, `textoDecisao` |
| Sinônimos (checkbox) | adiciona `"analyzer": "meu_sinonimos"` ao `query_string` | — |

Consequências para o motor (`engine.js`):
- `opts.relator` → injeta `AND relatores.nome:"<nome>"` no query_string (mesmo padrão
  do filtro `siglaTribunalJE`). Idem `opts.parte` → `partes.nomeParte`.
- `opts.sinonimos` → `analyzer: "meu_sinonimos"` no `query_string` (dicionário de
  sinônimos mantido pelo próprio TSE; aumenta recall).
- Facetas `.keyword` disponíveis (grep no bundle): `siglaUF`, `siglaTribunalJE`,
  `siglaClasse`, `publicacoes.siglaFontePublicacao`, `numeroUnicoFormatado`,
  `numeroUnico`, `numeroProcesso`, `numeroDecisao`, `nomeMunicipio`,
  `etiquetas.etiqueta`, `descricaoTipoDecisao`.

Lição de método (retroalimentada na skill criar-mcp-precedente): quando o oráculo de
contagens está indisponível (captcha sem navegador), o bundle do front é documentação
de primeira — o campo `relatores.nome` foi descoberto sem UMA chamada de API.
