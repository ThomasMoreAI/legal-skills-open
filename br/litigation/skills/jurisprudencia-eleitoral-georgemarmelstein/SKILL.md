---
name: jurisprudencia-eleitoral-georgemarmelstein
title: Jurisprudencia eleitoral georgemarmelstein
description: 'Busca precedentes da Justiça Eleitoral — TSE e os 27 TREs — no portal SJUR do TSE, via Chrome MCP (o site exige hCaptcha invisível a cada busca, então usa o navegador real para gerar o token). Retorna acórdãos/resoluções com ementa, relator, classe, PDF do inteiro teor e link. Use quando o usuário pedir jurisprudência eleitoral, precedente do TSE ou de TRE, pesquisa de acórdão eleitoral, propaganda/inelegibilidade/registro de candidatura, ou citar decisão da Justiça Eleitoral. Palavras-chave: jurisprudência eleitoral, TSE, TRE, precedente eleitoral, acórdão eleitoral, buscar jurisprudência TSE.'
author: georgemarmelstein
author_url: https://github.com/georgemarmelstein/superjurista-dev/tree/main/scaffold/skills/jurisprudencia-eleitoral
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
sources:
- title: Engenharia Reversa
  path: references/engenharia-reversa.md
- title: Sintaxe Booleana
  path: references/sintaxe-booleana.md
---

<identidade>
  <papel>Pesquisador de jurisprudência da Justiça Eleitoral (TSE + 27 TREs)</papel>
  <dominio>Direito eleitoral; busca em Elasticsearch via portal SJUR do TSE</dominio>
</identidade>

<proposito>
  <objetivo>Buscar e reportar precedentes eleitorais do TSE e dos TREs com ementa,
  metadados e link do inteiro teor</objetivo>
  <razao>A API de busca exige um token hCaptcha invisível de uso único por requisição —
  impossível gerar em Python puro. Um navegador real (Chrome MCP) gera o token
  silenciosamente, tornando a busca viável e confiável.</razao>
</proposito>

<quando_usar>
  <ativar_quando>
    - Usuário pede "jurisprudência eleitoral", "precedente do TSE", "acórdão de TRE"
    - Usuário quer decisões sobre temas eleitorais (propaganda, inelegibilidade,
      registro de candidatura, prestação de contas, AIJE, captação ilícita de sufrágio)
    - Usuário quer citar/verificar uma decisão da Justiça Eleitoral
    - Um pipeline de sentença/decisão precisa de precedente eleitoral
  </ativar_quando>
  <nao_usar_quando>
    - Jurisprudência NÃO eleitoral → usar bnp-api, cjf-jurisprudencia, julia-trf5, tjsc-eproc
    - Chrome MCP indisponível → avisar que a busca depende do navegador (ver casos de borda)
    - Baixar processo do PJE → usar pje-download
  </nao_usar_quando>
</quando_usar>

<instrucoes>
  <passo numero="0" nome="Preparar navegador e injetar o motor">
    1. `mcp__claude-in-chrome__tabs_context_mcp` (createIfEmpty: true) para obter/abrir aba.
    2. Se nenhuma aba tiver o portal SJUR, `navigate` para
       `https://jurisprudencia.tse.jus.br/#/jurisprudencia/pesquisa?expressaoLivre=teste&params=s`
       e aguardar ~8s (`computer` action wait) — o SPA precisa carregar `window.hcaptcha`.
       Uma aba SÓ já atende TSE **e** TREs (o token vale para os dois tenants).
    3. Verificar prontidão via `javascript_tool`: `({hc: !!window.hcaptcha})`.
       Se `false`, esperar mais 5s e repetir uma vez.
    4. Injetar o motor: `Read` de `references/engine.js` e colar TODO o conteúdo em UM
       `javascript_tool` (define `window.__jeSearch`). Confirmar retorno `'engine pronto'`.
  </passo>

  <passo numero="1" nome="Interpretar o pedido → montar opts">
    Traduza o pedido do usuário para o objeto `opts` (ver `<conhecimento>` p/ campos):
    - `query`: a expressão. Pode manter E/OU/NÃO (o motor normaliza para AND/OR/NOT).
    - `tribunais`: `'tse'` (só TSE) | `'tres'` (todos os TREs) | `'ambos'` (TSE + TREs).
      Regra: TRE específico ⇒ `tribunais:'tres'` + `tribunal:'TRE-XX'`.
    - `tribunal`/`uf`/`ordenacao`/`pagina`/`tamanho`/`ementaCompleta` conforme o caso.
  </passo>

  <passo numero="2" nome="Executar a busca">
    Rodar em UM `javascript_tool`:
    `JSON.stringify(await window.__jeSearch({ ...opts }))`
    O motor gera um token novo por chamada (com `hcaptcha.reset()` + retry até 3x) e
    limpa HTML/realce dos textos; devolve `{consulta, total, itens[]}` (ou `{tse, tres}`
    quando `tribunais:'ambos'`). Se `total` alto, pagine com `pagina`/`tamanho` conforme
    a necessidade — não despeje centenas de itens.
  </passo>

  <passo numero="3" nome="Formatar a saída (modo)">
    Escolha o modo conforme o pedido:
    - **buscar** (padrão): XML `<jurisprudencia_eleitoral>` (ver formato em conhecimento).
    - **gerar_relatorio**: Markdown legível (cabeçalho por tribunal, item numerado,
      ementa/resumo, relator, data, classe, link do PDF).
    - **listar_filtros**: escopos, códigos dos 27 TREs, ordenações e tabela de operadores
      (de `references/sintaxe-booleana.md`); opcionalmente classes via `/pesquisa/classes`.
    Sempre incluir o link do inteiro teor quando `temPDF` (campo `pdf`). Se `resumo` veio
    da decisão (`fonteResumo:'decisao'`), sinalizar "(sem ementa; trecho da decisão)".
  </passo>

  <passo numero="4" nome="Retorno conciso">
    Retornar só o essencial: consulta efetiva, total por tenant, os itens formatados e,
    se aplicável, o caminho do arquivo salvo. Não retornar o JSON cru nem logs do browser.
  </passo>
</instrucoes>

<conhecimento>
  <topico nome="Arquitetura e endpoints">
    Portais (SPA Angular) sobre um backend Elasticsearch:
    - TSE:  front `jurisprudencia.tse.jus.br`  → tenant `/tse/`
    - TREs: front `jurisprudencia-tres.tse.jus.br` → tenant `/tres/` (federa os 27 TREs)
    - Busca: `POST https://sjur-pesquisa-api.tse.jus.br/{tse|tres}/sjur-pesquisa-backend/rest/public/pesquisa`
    - Inteiro teor (ABERTO, sem captcha): `GET https://sjur-servicos.tse.jus.br/sjur-servicos/rest/download/pdf/{codigoDecisao}`
    Detalhes completos em `references/engenharia-reversa.md`.
  </topico>
  <topico nome="hCaptcha (o motivo da skill)">
    Toda busca exige `captchaToken` (hCaptcha invisível, sitekey 755c2e18-…), de USO ÚNICO.
    O motor gera um novo por chamada via `window.hcaptcha.execute({async:true})` na página.
    Token não é hostname-bound: minerado em qualquer um dos dois portais, vale para os dois
    tenants (comprovado). Nunca logar/gravar o token.
  </topico>
  <topico nome="opts do motor window.__jeSearch">
    `query` (str) · `tribunais` ('tse'|'tres'|'ambos', pad. 'tse') · `tribunal` ('TRE-XX')
    · `uf` ('CE'…) · `relator` (nome/sobrenome — filtro `relatores.nome`) · `parte`
    (nome da parte — filtro `partes.nomeParte`) · `sinonimos` (bool — usa o dicionário de
    sinônimos do portal, analyzer `meu_sinonimos`) · `dataInicio`/`dataFim` (dd/mm/aaaa →
    filtro DATD) · `incluirInteiroTeor` (bool, adiciona campo INTE) · `ordenacao`
    ('dj_desc' pad.|'dj_asc'|'dtj_desc'|'score') · `pagina` (0…) · `tamanho` (pad. 25) ·
    `ementaCompleta` (bool) · `incluirDecisao` (bool). Item devolvido: `id, tribunal, uf,
    municipio, processo, numeroUnico, classe, classeDesc, tipoDecisao, data, anoEleicao,
    relator, temPDF, pdf, temEmenta, fonteResumo, resumo, ementa`.
    Origem de relator/parte/sinonimos: minerados do bundle do front (templates do form
    avançado — ver engenharia-reversa.md §8). Se um desses filtros zerar resultados de
    forma inesperada, validar por contagens (com × sem o filtro) antes de confiar.
  </topico>
  <topico nome="Sintaxe booleana (resumo)">
    Elasticsearch query_string. Operadores: `AND OR NOT` (ou `&&`/`||`/`+`/`-`), frase
    `"..."`, proximidade `"..."~N`, curinga `*` e `?`, fuzzy `~`, campo `campo:termo`,
    grupo `()`. `E/OU/NÃO` em português são normalizados pelo motor. Tabela completa e
    filtros por campo em `references/sintaxe-booleana.md`.
  </topico>
  <topico nome="Formato XML de saída (modo buscar)">
    ```xml
    <jurisprudencia_eleitoral escopo="ambos" total="N">
      <item indice="1" tribunal="TRE-CE">
        <classe>REl — Recurso Eleitoral</classe>
        <processo>0600511-87</processo>
        <relator>Des. Maria Iraneide Moura Silva</relator>
        <data>07/07/2026</data>
        <resumo>...</resumo>
        <inteiro_teor>https://sjur-servicos.tse.jus.br/.../download/pdf/3523184</inteiro_teor>
      </item>
    </jurisprudencia_eleitoral>
    ```
  </topico>
</conhecimento>

<exemplos>
  <exemplo cenario="Precedente do TSE sobre propaganda antecipada">
    <entrada>Ache no TSE acórdãos sobre "propaganda eleitoral antecipada" nas redes sociais</entrada>
    <saida>
      opts = { query:'"propaganda eleitoral antecipada" E ("redes sociais" OU internet)',
               tribunais:'tse', tamanho:10 }
      → XML com os acórdãos, relator, data e link do PDF.
    </saida>
  </exemplo>
  <exemplo cenario="Um TRE específico">
    <entrada>Jurisprudência do TRE-CE sobre inelegibilidade da LC 64/90</entrada>
    <saida>
      opts = { query:'inelegibilidade E "Lei Complementar 64"', tribunais:'tres',
               tribunal:'TRE-CE', tamanho:10 } → relatório Markdown.
    </saida>
  </exemplo>
  <exemplo cenario="TSE + todos os TREs">
    <entrada>Compare TSE e TREs sobre captação ilícita de sufrágio (art. 41-A)</entrada>
    <saida>
      opts = { query:'"captação ilícita de sufrágio" OU "art. 41-A"', tribunais:'ambos' }
      → totais por tenant + itens de cada.
    </saida>
  </exemplo>
  <exemplo cenario="Decisões de um relator específico">
    <entrada>Acórdãos da relatora Cármen Lúcia no TSE sobre fraude à cota de gênero</entrada>
    <saida>
      opts = { query:'"cota de gênero" E fraude', tribunais:'tse',
               relator:'Cármen Lúcia', tamanho:10 } → XML com os acórdãos da relatora.
    </saida>
  </exemplo>
</exemplos>

<casos_de_borda>
  <caso nome="Chrome MCP indisponível">
    <problema>tabs_context_mcp falha ou extensão desconectada.</problema>
    <solucao>Avisar que esta busca depende do navegador real (por causa do hCaptcha) e
    pedir para abrir o Chrome com a extensão claude-in-chrome. Não há fallback em Python.</solucao>
  </caso>
  <caso nome="Falha ao validar o HCaptcha">
    <problema>Resposta com `erro: "Falha ao validar o HCaptcha."`. O widget "esfria"
    quando a aba fica ociosa entre buscas e a 1ª chamada falha.</problema>
    <solucao>O motor já faz `hcaptcha.reset()` + regenera o token e re-tenta até 3x por
    chamada (`opts.tentativas`). Se AINDA assim vier `erro`, a página perdeu o widget:
    recarregar o portal (navigate + wait 8s), reinjetar `engine.js` e repetir a busca.
    Se só um tenant falhar, abrir o portal correspondente (tse ou tres) e repetir.</solucao>
  </caso>
  <caso nome="Ementa vazia (comum em TRE)">
    <problema>`textoEmenta` vazio em vários acórdãos de TRE.</problema>
    <solucao>O motor já cai para o texto da decisão (`fonteResumo:'decisao'`). Sinalizar
    isso no output e lembrar que o inteiro teor está no PDF.</solucao>
  </caso>
  <caso nome="Muitos resultados">
    <problema>`total` na casa dos milhares.</problema>
    <solucao>Refinar a query (frase exata, filtro por tribunal/UF/classe/ano, ou recorte de
    data via `dataInicio`/`dataFim`) e paginar; nunca despejar tudo. Reportar o total e
    mostrar os primeiros N mais recentes.</solucao>
  </caso>

  <caso nome="Tradução automática do navegador">
    <problema>As Dicas oficiais alertam: tradução automática (navegador/Google Tradutor)
    pode quebrar o funcionamento do SPA.</problema>
    <solucao>Não acionar tradução automática na aba do portal; manter em português.</solucao>
  </caso>
</casos_de_borda>

<referencias>
  - [references/engine.js](references/engine.js) - Motor in-page (mint + busca + parse)
  - [references/sintaxe-booleana.md](references/sintaxe-booleana.md) - Operadores, filtros, escopos
  - [references/engenharia-reversa.md](references/engenharia-reversa.md) - API, contrato, HAR, PDF
</referencias>

<pre_requisitos>
  - Chrome MCP (extensão claude-in-chrome) ativo e conectado ao Chrome do usuário
  - Acesso a jurisprudencia.tse.jus.br e jurisprudencia-tres.tse.jus.br
</pre_requisitos>
