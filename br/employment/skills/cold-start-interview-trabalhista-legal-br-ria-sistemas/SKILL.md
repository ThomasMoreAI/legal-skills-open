---
name: cold-start-interview-trabalhista-legal-br-ria-sistemas
title: /cold-start-interview — trabalhista-legal-br
description: Entrevista inicial do advogado pra popular o practice profile (CLAUDE.md) do plugin trabalhista-legal-br. Roda na primeira execucao do plugin, captura identidade OAB, jurisdicao TRT, foco de atuacao, convencoes coletivas relevantes e modelos preferidos do escritorio. Modo --quick (2-3 min) desbloqueia uso imediato; --full (10-15 min) coleta contexto completo; --redo refaz do zero.
author: RIA-Sistemas
author_url: https://github.com/RIA-Sistemas/claude-for-legal-br/tree/main/trabalhista-legal-br/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: pt
sources:
- title: Areas Trabalhistas
  path: references/areas-trabalhistas.md
- title: Trt Regioes
  path: references/trt-regioes.md
---

# /cold-start-interview — trabalhista-legal-br

Entrevista que popula o practice profile do plugin trabalhista (CLAUDE.md). Toda skill do plugin le este arquivo antes de executar — TRT predominante, foco defesa-empregador vs defesa-empregado, convencoes coletivas, tom preferido das pecas. Sem o profile preenchido, as skills caem em defaults genericos.

## Quando rodar

- Primeira execucao do plugin (CLAUDE.md ainda com `[PLACEHOLDER]`)
- Advogado mudou de TRT, escritorio, ou foco de atuacao
- Pedido explicito de re-configuracao via `--redo`

## Modos

### `--quick` (default — 2-3 min, 5 perguntas)

Coleta o minimo pra desbloquear uso:
1. Identidade (nome, OAB, escritorio, cidade/UF)
2. Foco principal (defesa-empregador / defesa-empregado / ambos)
3. TRT predominante
4. Subareas mais frequentes (3 mais usadas)
5. Tom preferido das pecas

Demais campos ficam como `[PLACEHOLDER]` com nota de que podem ser preenchidos depois via `--full` ou edicao manual.

### `--full` (10-15 min, ~15 perguntas)

Modo quick + perguntas detalhadas sobre:
- Volume mensal de casos
- Varas mais usadas e frequencia de TST
- Convencoes coletivas relevantes (ate 3 principais)
- Modelos seed (caminhos opcionais de pecas exemplares do escritorio)
- Compliance pessoal (audit trail, disclaimer CFOAB)

### `--redo`

Sobrescreve CLAUDE.md existente. Confirma antes de apagar. Util quando o advogado mudou de escritorio ou TRT.

## Antes de comecar

1. Le `~/.claude/plugins/config/claude-for-legal-br/trabalhista-legal-br/CLAUDE.md` se existir.
2. Se ja populado (sem `[PLACEHOLDER]`) e sem flag `--redo`: confirma antes de sobrescrever.
3. Se contem `<!-- SETUP PAUSADO EM: -->`: cumprimenta e retoma do ponto.
4. Se contem `[PLACEHOLDER]` mas sem comentario de pausa: oferece comecar do zero ou retomar de onde os placeholders comecam.

Preambulo (3 linhas, sem emoji):

> Este e o setup do plugin trabalhista-legal-br. Em 2-3 minutos voce desbloqueia uso pratico com modo `--quick`, ou em 10-15 minutos preenche o profile completo com `--full`. Pode rodar `--redo` quando quiser pra recomecar do zero. Pode pausar a qualquer momento dizendo "pausa" — salvo o progresso e retomo depois.
>
> Modo `--quick` ou `--full`? Default e `--quick`.

## Pacing da entrevista

- Uma pergunta por vez. Nunca empilhe 3 perguntas numa mensagem so.
- Se a resposta nao for clara, pede esclarecimento — nao assume.
- Se o advogado disser "nao sei" ou "pula essa": deixa `[PLACEHOLDER]` com nota e segue. Nao insiste.
- Tom: colega mais experiente, direto, sem subserviencia. Tratamento "voce". Sem juridiques de adorno.
- Sem emojis, sem "perfeito!", sem "que otimo!".

## Roteiro — Modo --quick

### Pergunta 1 — Identidade

> Pra te identificar nas pecas: qual seu nome completo, numero da OAB com UF, escritorio (se tiver), e cidade/UF base?
>
> Exemplo de resposta valida: "Joao Silva, OAB/SP 234.567, Silva e Advogados, Sao Paulo/SP".

**Validacao:** OAB deve seguir formato `OAB/UF NNNNNN` (numero pode ter ponto). Se vier sem UF ou sem numero, pede pra corrigir. Se o advogado nao tiver escritorio (solo), aceita "solo" ou "autonomo".

**Preenche:** `## Identidade do advogado` — campos Nome, OAB, Escritorio, Cidade / UF base.

### Pergunta 2 — Foco principal

> Voce atua mais pra defender empregador, empregado, ou os dois?
>
> 1. **defesa-empregador** — sua carteira e majoritariamente reclamadas e defesas
> 2. **defesa-empregado** — voce ajuiza reclamatorias pelo trabalhador
> 3. **ambos** — divide entre os dois lados

**Validacao:** uma das tres opcoes. Se "ambos", pergunta qual lado e o default quando o caso e ambiguo.

**Preenche:** `## Areas de atuacao` — campo Foco principal.

### Pergunta 3 — TRT predominante

> Em qual TRT voce atua mais? Pode responder o numero ou o nome do estado.
>
> Se nao souber qual TRT cobre sua regiao, posso te mostrar a lista das 24 regioes.

Se o advogado pedir lista, le `references/trt-regioes.md` e mostra. Se a UF base ja foi capturada na Pergunta 1, sugere o TRT correspondente como default ("Sua UF e RS, entao o TRT-4 e o default — confirma?").

**Validacao:** TRT-1 a TRT-24 (sem TRT-7 e TRT-21 — ja existem; sao 24 regioes ativas). Se a resposta for um numero fora desse range, mostra a lista.

**Preenche:** `## Tribunais / fora frequentes` — campo TRT predominante.

### Pergunta 4 — Subareas mais frequentes

> Me diz as 3 subareas trabalhistas que voce mais ve no dia a dia. Pode ser tipo de pedido, tipo de pretensao, ou tema. Exemplos:
>
> - verbas rescisorias
> - horas extras / banco de horas
> - dano moral trabalhista
> - acidente de trabalho / doenca ocupacional
> - terceirizacao / pejotizacao
> - equiparacao salarial
> - reconhecimento de vinculo
> - rescisao indireta
> - assedio moral / sexual
> - estabilidade (gestante, CIPA, etc)
>
> Pode escolher dessa lista ou inventar suas proprias categorias.

Se quiser ver a lista completa de categorias, le `references/areas-trabalhistas.md`. Aceita ate 5 (3 e o pedido, mais 2 e ok). Se o advogado listar so 1 ou 2, segue — nao force.

**Preenche:** `## Areas de atuacao` — campo Subareas frequentes.

### Pergunta 5 — Tom preferido

> Qual o tom que voce prefere nas pecas que produz? Escolhe um:
>
> 1. **formal** — linguagem cerimoniosa, "Excelentissimo Doutor", periodos longos
> 2. **direto** — tecnico mas sem floreio, periodos curtos
> 3. **tecnico-academico** — fundamentacao doutrinaria pesada, citacao de autores
> 4. **acessivel** — pra cliente entender ler junto, menos juridiques

**Validacao:** uma das quatro. Se "depende do caso", aceita e marca como `direto` por default mas anota a preferencia.

**Preenche:** `## Modelos / templates preferidos` — coluna Tom. Aplica o mesmo tom default em todas as linhas da tabela.

## Roteiro — Modo --full (adicional ao --quick)

Apos as 5 perguntas do quick, segue com:

### Pergunta 6 — Volume tipico

> Quantos casos trabalhistas novos voce pega por mes em media? Numero aproximado ja serve.

**Validacao:** numero inteiro entre 1 e 200. Se mais que 200, confirma ("isso e bastante volume — confirma?"). Se "varia muito", aceita e marca como "variavel".

**Preenche:** `## Areas de atuacao` — campo Volume tipico.

### Pergunta 7 — Varas mais usadas

> Quais sao as 2-3 varas do trabalho que voce mais pratica? Pode listar por numero e cidade (ex: "1a VT de Sao Paulo, 5a VT de Campinas").

**Validacao:** texto livre. Se em branco, aceita.

**Preenche:** `## Tribunais / fora frequentes` — campo Varas mais usadas.

### Pergunta 8 — Frequencia TST

> Com que frequencia voce sobe recurso de revista pro TST?
>
> 1. **alta** — varios por mes
> 2. **media** — alguns por semestre
> 3. **baixa** — raramente
> 4. **nunca** — fica no TRT

**Preenche:** `## Tribunais / fora frequentes` — campo TST recurso de revista frequencia.

### Pergunta 9 — Convencoes coletivas relevantes (top 3)

> Quais sao as 3 CCTs/ACTs que voce mais cita ou consulta no dia a dia? Pode me dar nome da categoria + numero MTE + vigencia, ou so o nome se nao souber de cabeca.
>
> Exemplos:
> - "Comerciarios de Sao Paulo, MR 2024/2025"
> - "Bancarios CCT 2023/2024"
> - "Construcao civil RS — Sintricom-RS"
>
> Pode pular essa se preferir preencher depois — fica como `[PLACEHOLDER]` na tabela.

**Validacao:** ate 3 entradas. Aceita texto livre. Se pular, marca toda a tabela como `[PLACEHOLDER — preencher quando tiver os dados]`.

**Preenche:** `## Convencoes coletivas relevantes` — tabela.

### Pergunta 10-13 — Modelos seed (uma pergunta por tipo)

Pra cada tipo de peca, pergunta separada:

> Voce tem um modelo seu de **reclamatoria trabalhista (cliente CLT)** que eu poderia usar como referencia? Pode me dar o caminho do arquivo (ex: `/Users/voce/escritorio/modelos/reclamatoria.docx`) ou colar o conteudo, ou dizer "nao tenho" / "pula" pra deixar em branco.

Repete pra:
- Defesa empregador
- Calculo de verbas rescisorias
- Notificacao extrajudicial

**Validacao:** se for caminho, valida que o arquivo existe. Se nao existir, avisa e oferece tentar de novo ou pular. Se for conteudo colado, salva referencia no profile com nota "conteudo recebido em [data]".

**Preenche:** `## Modelos / templates preferidos` — coluna Pasta / arquivo seed.

### Pergunta 14 — Compliance pessoal

> Por padrao, o plugin aplica:
> - Output marcado como `RASCUNHO PARA REVISAO — Adv. [seu nome OAB]`
> - Disclaimer CFOAB Recomendacao 001/2024 no fecho de toda peca
> - Audit trail local em `~/.briefing-estudio/audit.db`
>
> Quer ajustar algum desses? Padrao default e manter tudo ligado.

**Validacao:** aceita "manter padrao" ou ajustes especificos. Se ajustes, captura.

**Preenche:** `## Compliance pessoal` — campos correspondentes.

## Ao final da entrevista

### Passo 1 — Mostrar resumo

Mostra ao advogado:

> Capturei o seguinte. Confere?
>
> - **Nome:** [NOME]
> - **OAB:** [OAB]
> - **Escritorio:** [ESCRITORIO]
> - **Cidade/UF:** [CIDADE/UF]
> - **Foco:** [FOCO]
> - **TRT:** [TRT]
> - **Subareas:** [LISTA]
> - **Tom:** [TOM]
> - **Volume:** [VOLUME ou "nao informado"]
> - **CCTs:** [LISTA ou "nao informado"]
> - **Modelos seed:** [N de N preenchidos]
>
> Esta correto? Responde "sim" pra eu salvar, ou diz o que ajustar.

Espera resposta. Se "sim", escreve. Se ajuste, refaz so o campo apontado.

### Passo 2 — Escrever no CLAUDE.md

Sobrescreve `~/.claude/plugins/config/claude-for-legal-br/trabalhista-legal-br/CLAUDE.md` substituindo cada `[PLACEHOLDER]` pelas respostas capturadas. Atualiza o footer com a data corrente (formato `AAAA-MM-DD`).

Campos nao preenchidos no modo `--quick`: mantem `[PLACEHOLDER — preencher depois via --full ou edicao manual]`.

### Passo 3 — Mostrar proximos passos

> Practice profile preenchido em `~/.claude/plugins/config/claude-for-legal-br/trabalhista-legal-br/CLAUDE.md`.
>
> Skills MVP do plugin que voce pode usar agora:
>
> - `/trabalhista-legal-br:calculo-verbas-rescisorias` — calcula verbas por modalidade de rescisao
> - `/trabalhista-legal-br:triagem-reclamatoria` — triagem inicial de reclamatoria (defesa ou ajuizamento)
> - `/trabalhista-legal-br:analise-contrato-trabalho` — analise de contrato CLT, PJ, intermitente, MEI
>
> Pra editar o profile depois: edita o arquivo direto, ou roda `/trabalhista-legal-br:cold-start-interview --redo` pra refazer do zero.
>
> Se rodou no modo `--quick` e quer completar agora, roda `/trabalhista-legal-br:cold-start-interview --full`.

## Regras operacionais

- **Sem juridiques de adorno.** Tom de colega — "voce", direto, tecnico.
- **Sem emojis decorativos.** Nenhum emoji em nenhuma pergunta ou confirmacao.
- **Sem bajulacao.** Nada de "perfeito!", "otima resposta!", "vamos la!".
- **Uma pergunta por vez.** Nunca empilha 3 perguntas. Conta subitens — uma pergunta com 3 sub-perguntas e 3 perguntas.
- **Pausa salva progresso.** Se o advogado disser "pausa" ou "depois", grava partial com `<!-- SETUP PAUSADO EM: [secao] — rode /trabalhista-legal-br:cold-start-interview pra retomar -->` e fields nao respondidos como `[PENDENTE]`.
- **Validacao explicita.** OAB invalida → pede correcao. TRT invalido → mostra lista. Caminho de arquivo invalido → avisa e oferece nova tentativa ou pular.
- **Nunca inventa dado.** Se faltou resposta, deixa `[PLACEHOLDER]`. Nao supoe que o tom default e "formal" so porque a maioria e — pergunta.
- **Confirma antes de sobrescrever.** Se CLAUDE.md ja esta populado e nao tem `--redo`, pergunta antes de tocar.

## Lista de referencias

- `references/trt-regioes.md` — lista das 24 regioes TRT com UF, sede, e jurisdicao
- `references/areas-trabalhistas.md` — categorias de subareas trabalhistas detalhadas

## Quando NAO usar esta skill

- Advogado quer fazer pergunta juridica trabalhista (use a skill MVP correspondente, nao o cold-start)
- Advogado quer atualizar so 1 campo do profile (peca pra editar o arquivo direto, mais rapido)
- Plugin ja foi configurado e nao houve mudanca real (cold-start sem `--redo` skipa quando profile esta populado)
