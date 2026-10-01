---
name: cold-start-interview-ria-sistemas
title: /cold-start-interview — previdenciario-legal-br
description: Entrevista inicial do advogado pra popular o practice profile (CLAUDE.md) do plugin previdenciario-legal-br. Roda na primeira execucao do plugin, captura identidade OAB, JEF/TRF predominante, foco de atuacao (previdenciario puro, acidentario, assistencial), tipos de beneficio mais frequentes, perfil de cliente tipico e marcos regulatorios monitorados. Modo --quick (2-3 min) desbloqueia uso; --full (10-15 min) coleta contexto completo; --redo refaz do zero.
author: RIA-Sistemas
author_url: https://github.com/RIA-Sistemas/claude-for-legal-br/tree/main/previdenciario-legal-br/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: social-security
language: pt
sources:
- title: Beneficios Inss
  path: references/beneficios-inss.md
- title: Trf Jef
  path: references/trf-jef.md
---

# /cold-start-interview — previdenciario-legal-br

Entrevista que popula o practice profile do plugin previdenciario (CLAUDE.md). Toda skill do plugin le este arquivo antes de executar — JEF/TRF predominante, foco entre previdenciario puro vs acidentario vs assistencial, tipos de beneficio mais trabalhados, modelos preferidos. Sem o profile, as skills caem em defaults genericos e perdem precisao em area que muda jurisprudencia rapido (Reformas 2019 e 2023 + temas STF/STJ/TNU recentes).

## Quando rodar

- Primeira execucao do plugin (CLAUDE.md ainda com `[PLACEHOLDER]`)
- Advogado mudou de JEF, escritorio, ou foco de beneficio
- Pedido explicito de re-configuracao via `--redo`
- Apos a janela semestral de revisao jurisprudencial (campo "Ultima revisao jurisprudencial")

## Modos

### `--quick` (default — 2-3 min, 5 perguntas)

Coleta o minimo pra desbloquear uso:
1. Identidade (nome, OAB, escritorio, cidade/UF)
2. Foco principal (previdenciario-puro / + acidentario / + assistencial / outro)
3. JEF/TRF predominante
4. Tipos de beneficio mais frequentes (top 3)
5. Tom preferido das pecas

Demais campos ficam como `[PLACEHOLDER]` com nota de que podem ser preenchidos depois.

### `--full` (10-15 min, ~15 perguntas)

Modo quick + perguntas detalhadas sobre:
- Volume mensal de casos
- Perfil cliente tipico (rural / urbano / LOAS / servidor)
- Marcos regulatorios monitorados (EC 103/2019, Reformas 2023, IN INSS vigentes)
- Modelos seed (caminhos opcionais de pecas exemplares)
- Frequencia TNU e STJ
- Compliance pessoal (audit trail, disclaimer CFOAB)
- Volatilidade — confirma janela de revisao semestral

### `--redo`

Sobrescreve CLAUDE.md existente. Confirma antes de apagar. Util quando o advogado mudou de JEF, escritorio, ou foco majoritario de pratica.

## Antes de comecar

1. Le `~/.claude/plugins/config/claude-for-legal-br/previdenciario-legal-br/CLAUDE.md` se existir.
2. Se ja populado (sem `[PLACEHOLDER]`) e sem flag `--redo`: confirma antes de sobrescrever.
3. Se contem `<!-- SETUP PAUSADO EM: -->`: cumprimenta e retoma do ponto.
4. Se contem `[PLACEHOLDER]` mas sem comentario de pausa: oferece comecar do zero ou retomar de onde os placeholders comecam.

Preambulo (3 linhas, sem emoji):

> Este e o setup do plugin previdenciario-legal-br. Em 2-3 minutos voce desbloqueia uso pratico com modo `--quick`, ou em 10-15 minutos preenche o profile completo com `--full`. Pode rodar `--redo` quando quiser pra recomecar do zero. Pode pausar a qualquer momento dizendo "pausa" — salvo o progresso e retomo depois.
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
> Exemplo de resposta valida: "Joao Silva, OAB/SP 234.567, Silva Previdenciario, Sao Paulo/SP".

**Validacao:** OAB deve seguir formato `OAB/UF NNNNNN` (numero pode ter ponto). Se vier sem UF ou sem numero, pede pra corrigir. Se o advogado for solo, aceita "solo" ou "autonomo".

**Preenche:** `## Identidade do advogado` — campos Nome, OAB, Escritorio, Cidade / UF base.

### Pergunta 2 — Foco principal

> Voce atua mais em qual frente?
>
> 1. **previdenciario-puro** — RGPS, aposentadorias, auxilios, pensoes (Lei 8.213/91)
> 2. **previdenciario + acidentario** — inclui aposentadoria especial, auxilio-acidente, benefício por incapacidade decorrente de acidente de trabalho
> 3. **previdenciario + assistencial** — inclui BPC-LOAS e beneficios assistenciais (Lei 8.742/93)
> 4. **outro** — voce me descreve

**Validacao:** uma das quatro opcoes. Se "outro", pede descricao livre e salva como esta.

**Preenche:** `## Areas de atuacao` — campo Foco principal.

### Pergunta 3 — JEF / TRF predominante

> Em qual JEF (Juizado Especial Federal) ou TRF voce atua mais? Pode me dar o nome da secao judiciaria + cidade + qual TRF correspondente, ou so a cidade/UF que eu deduzo.
>
> Exemplos:
> - "JEF de Porto Alegre, TRF-4"
> - "JEF de Curitiba, TRF-4"
> - "JEF Civel SP Capital, TRF-3"
>
> Se nao souber qual TRF cobre sua regiao, posso te mostrar a lista.

Se o advogado pedir lista, le `references/trf-jef.md` e mostra. Se a UF base ja foi capturada na Pergunta 1, sugere o TRF correspondente como default ("Sua UF e RS, entao TRF-4 e o default — confirma a JEF de qual cidade?").

**Validacao:** TRF de 1 a 6. Se a resposta for fora desse range, mostra a lista.

**Preenche:** `## Tribunais / fora frequentes` — campos JEF predominante e TRF correspondente.

### Pergunta 4 — Tipos de beneficio mais frequentes (top 3)

> Quais sao os 3 tipos de beneficio que voce mais ve no dia a dia? Pode escolher dessa lista ou usar suas proprias categorias:
>
> - BPC-LOAS (assistencial)
> - Aposentadoria por tempo de contribuicao
> - Aposentadoria por idade
> - Aposentadoria especial
> - Aposentadoria por incapacidade permanente (antiga "por invalidez")
> - Aposentadoria do professor
> - Aposentadoria da pessoa com deficiencia
> - Auxilio por incapacidade temporaria (antigo "auxilio-doenca")
> - Auxilio-acidente
> - Pensao por morte
> - Salario-maternidade
> - Auxilio-reclusao
> - Beneficio rural / segurado especial
> - Revisao de RMI

Se quiser ver lista completa de beneficios INSS com referencias legais, le `references/beneficios-inss.md`.

**Validacao:** ate 5 (3 e o pedido, 4-5 e ok). Se listar so 1 ou 2, segue.

**Preenche:** `## Areas de atuacao` — campo Tipos de beneficio mais frequentes.

### Pergunta 5 — Tom preferido

> Qual o tom que voce prefere nas pecas que produz? Escolhe um:
>
> 1. **formal** — linguagem cerimoniosa, periodos longos, "Excelentissimo Doutor"
> 2. **direto** — tecnico mas sem floreio, periodos curtos
> 3. **tecnico-academico** — fundamentacao doutrinaria pesada, citacao de autores (Wladimir Novaes Martinez, Ivan Kertzman, etc)
> 4. **acessivel** — pra cliente entender, menos juridiques, util em parecer pre-judicial

**Validacao:** uma das quatro. Se "depende do caso", aceita e marca como `direto` por default.

**Preenche:** `## Modelos / templates preferidos` — coluna Tom.

## Roteiro — Modo --full (adicional ao --quick)

### Pergunta 6 — Volume tipico

> Quantos casos previdenciarios novos voce pega por mes em media? Numero aproximado serve.

**Validacao:** numero inteiro entre 1 e 200. Se mais que 200, confirma. "Variavel" aceita.

**Preenche:** `## Areas de atuacao` — campo Volume tipico.

### Pergunta 7 — Perfil cliente tipico

> Qual o perfil do cliente que voce mais atende? Me diz o percentual aproximado em 4 categorias (nao precisa somar 100% certinho):
>
> - Trabalhador rural / segurado especial
> - Trabalhador urbano (CLT / contribuinte individual)
> - Beneficiario LOAS / BPC (deficiente ou idoso de baixa renda)
> - Servidor publico (RPPS proprio do ente)
>
> Pode dizer "majoritariamente rural" se for o caso, sem precisao numerica.

**Validacao:** texto livre, ate 4 categorias. Aceita "majoritariamente X" sem percentual.

**Preenche:** `## Perfil do cliente tipico` — tabela.

### Pergunta 8 — Frequencia TNU

> Com que frequencia voce ajuiza incidente de uniformizacao na TNU?
>
> 1. **alta** — varios por mes
> 2. **media** — alguns por semestre
> 3. **baixa** — raramente
> 4. **nunca** — fica no TRF

**Preenche:** `## Tribunais / fora frequentes` — campo TNU frequencia.

### Pergunta 9 — Frequencia STJ

> E recurso especial pro STJ, com que frequencia?
>
> 1. **alta**
> 2. **media**
> 3. **baixa**
> 4. **nunca**

**Preenche:** `## Tribunais / fora frequentes` — campo Recurso ao STJ.

### Pergunta 10 — Marcos regulatorios monitorados

> Quais marcos regulatorios voce monitora ativamente? Marca o que aplica:
>
> 1. **EC 103/2019** — Reforma da Previdencia (default sim, fundamental)
> 2. **Pacote Trabalhista 2023** (Lei 14.611/2023, Lei 14.737/2023, etc — impacto previdenciario)
> 3. **Lei 8.213/91** — Plano de Beneficios (fundamental)
> 4. **Lei 8.742/93** — LOAS (so se atua em assistencial)
> 5. **IN INSS vigentes** — Instrucoes Normativas atualizadas (IN 128/2022 e posteriores)
> 6. **Outros** — descreva

**Validacao:** marca o que selecionou. EC 103 e Lei 8.213 vem por default mesmo se nao selecionar — alerta o advogado.

**Preenche:** `## Marcos regulatorios que monitora` — lista de checkboxes.

### Pergunta 11-14 — Modelos seed (uma pergunta por tipo)

Pra cada tipo de peca, pergunta separada:

> Voce tem um modelo seu de **peticao inicial pra BPC-LOAS** que eu poderia usar como referencia? Pode me dar caminho de arquivo, colar o conteudo, ou dizer "nao tenho" pra deixar em branco.

Repete pra:
- Peticao inicial — Aposentadoria
- Recurso administrativo CRPS
- Analise de carta de indeferimento

**Validacao:** se for caminho, valida que arquivo existe. Se nao existir, avisa e oferece nova tentativa ou pular. Se for conteudo colado, salva com nota "conteudo recebido em [data]".

**Preenche:** `## Modelos / templates preferidos` — coluna Pasta / arquivo seed.

### Pergunta 15 — Compliance pessoal e volatilidade

> Por padrao, o plugin aplica:
> - Output marcado como `RASCUNHO PARA REVISAO — Adv. [seu nome OAB]`
> - Disclaimer CFOAB Recomendacao 001/2024 no fecho de toda peca
> - Audit trail local em `~/.briefing-estudio/audit.db`
> - Janela de revisao jurisprudencial semestral (area previdenciaria muda muito rapido)
>
> Quer ajustar algum desses? E voce confirma que pode comprometer com revisao semestral, ou prefere janela diferente (3 meses, 4 meses, etc)?

**Validacao:** captura ajustes. Janela default e semestral; se o advogado preferir prazo menor, marca.

**Preenche:** `## Compliance pessoal` + `## Volatilidade — revisao semestral`.

## Ao final da entrevista

### Passo 1 — Mostrar resumo

> Capturei o seguinte. Confere?
>
> - **Nome:** [NOME]
> - **OAB:** [OAB]
> - **Escritorio:** [ESCRITORIO]
> - **Cidade/UF:** [CIDADE/UF]
> - **Foco:** [FOCO]
> - **JEF / TRF:** [JEF] / [TRF]
> - **Beneficios:** [LISTA]
> - **Tom:** [TOM]
> - **Volume:** [VOLUME ou "nao informado"]
> - **Perfil cliente:** [PERFIL ou "nao informado"]
> - **Marcos monitorados:** [LISTA]
> - **Modelos seed:** [N de N preenchidos]
> - **Janela revisao:** [PERIODO]
>
> Esta correto? Responde "sim" pra eu salvar, ou diz o que ajustar.

Espera resposta. Se "sim", escreve. Se ajuste, refaz so o campo apontado.

### Passo 2 — Escrever no CLAUDE.md

Sobrescreve `~/.claude/plugins/config/claude-for-legal-br/previdenciario-legal-br/CLAUDE.md` substituindo cada `[PLACEHOLDER]` pelas respostas capturadas. Atualiza o footer com data corrente (formato `AAAA-MM-DD`). Preenche `Ultima revisao jurisprudencial` com a data de hoje.

Campos nao preenchidos no modo `--quick`: mantem `[PLACEHOLDER — preencher depois via --full ou edicao manual]`.

### Passo 3 — Mostrar proximos passos

> Practice profile preenchido em `~/.claude/plugins/config/claude-for-legal-br/previdenciario-legal-br/CLAUDE.md`.
>
> Skills MVP do plugin que voce pode usar agora:
>
> - `/previdenciario-legal-br:triagem-bpc-loas` — triagem de elegibilidade pra BPC (renda, deficiencia, idade)
> - `/previdenciario-legal-br:analise-carta-inss` — extrai motivos do indeferimento e fundamentos contestaveis
> - `/previdenciario-legal-br:calculo-tempo-contribuicao` — calcula tempo de contribuicao a partir do CNIS
>
> Pra editar o profile depois: edita o arquivo direto, ou roda `/previdenciario-legal-br:cold-start-interview --redo` pra refazer do zero.
>
> Se rodou no modo `--quick`, completa agora com `/previdenciario-legal-br:cold-start-interview --full`.
>
> Lembrete: area previdenciaria muda rapido. Sua proxima revisao jurisprudencial cai em [DATA + 6 MESES]. O plugin vai te lembrar.

## Regras operacionais

- **Sem juridiques de adorno.** Tom de colega — "voce", direto, tecnico.
- **Sem emojis decorativos.** Nenhum emoji em pergunta ou confirmacao.
- **Sem bajulacao.** Nada de "perfeito!", "otima resposta!", "vamos la!".
- **Uma pergunta por vez.** Nunca empilha 3 perguntas. Conta subitens.
- **Pausa salva progresso.** "Pausa" → grava partial com `<!-- SETUP PAUSADO EM: [secao] — rode /previdenciario-legal-br:cold-start-interview pra retomar -->` e fields nao respondidos como `[PENDENTE]`.
- **Validacao explicita.** OAB invalida → pede correcao. TRF invalido → mostra lista. Caminho de arquivo invalido → avisa e oferece nova tentativa.
- **Nunca inventa dado.** Se faltou resposta, deixa `[PLACEHOLDER]`. Nao supoe foco "previdenciario-puro" so porque e o mais comum — pergunta.
- **Confirma antes de sobrescrever.** Se CLAUDE.md ja esta populado e sem `--redo`, pergunta antes de tocar.
- **Atencao redobrada ao Reformista.** EC 103/2019 mudou regras de transicao; Pacote 2023 alterou alguns pontos. Se o advogado nao monitora ativamente, alerta sem ser professoral: "EC 103 e fundamental — sugiro marcar como monitorada por default. Confirma?"

## Lista de referencias

- `references/trf-jef.md` — lista dos 6 TRFs com jurisdicao e principais JEFs
- `references/beneficios-inss.md` — lista de beneficios INSS com referencias legais

## Quando NAO usar esta skill

- Advogado quer fazer pergunta juridica previdenciaria (use skill MVP correspondente)
- Advogado quer atualizar so 1 campo do profile (edita o arquivo direto, mais rapido)
- Plugin ja foi configurado e nao houve mudanca real (cold-start sem `--redo` skipa quando profile esta populado)
