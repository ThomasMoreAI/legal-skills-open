---
name: wage-hour-qa-bossmann007
title: /wage-hour-qa
description: Q&A de jornada/remuneração sensível à base territorial/CCT — enquadramento, horas extras, intervalos, licenças, verbas rescisórias — respondido para a base territorial/categoria específica com a regra controladora pesquisada e citada, não recitada de memória. Use quando o usuário perguntar qualquer questão trabalhista, ou disser "qual a regra da CCT de", "isso é enquadrável no art. 62", ou "temos que pagar hora extra para".
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/employment-legal/skills/wage-hour-qa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: pt
---

# /wage-hour-qa

1. Carregar `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → abrangência territorial.
2. Usar o workflow abaixo.
3. Identificar a base territorial/categoria/CCT a que a pergunta se refere. Se não especificada, perguntar.
4. Responder conforme a regra dessa base/CCT. Citar. Sinalizar se for caso de fronteira ou lei em mudança.

---

## Matter context

**Matter context.** Verificar `## Matter workspaces` no CLAUDE.md de prática. Se `Enabled` for `✗` (padrão para usuários in-house), pular o resto deste parágrafo — skills usam contexto de prática e a máquina de matéria fica invisível. Se habilitado e não houver matéria ativa, perguntar: "Para qual matéria é isso? Rode `/employment-legal:matter-workspace switch <slug>` ou diga `practice-level`." Carregar `matter.md` da matéria ativa para contexto e overrides específicos. Gravar outputs na pasta da matéria em `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Nunca ler arquivos de outra matéria a menos que `Cross-matter context` esteja `on`.

---

## Purpose

"Depende" é verdade mas inútil. Este skill produz uma resposta específica à base
territorial/categoria, fundamentada em fontes primárias pesquisadas e citadas — e
sinaliza quando a pergunta é fronteiriça o bastante para exigir julgamento humano.
Não recita regras de memória: pisos salariais por CCT, entendimento de estabilidade,
e prazos de rescisão mudam com frequência e variam materialmente por convenção
coletiva.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → abrangência
territorial. Se a pergunta não especificar base/categoria, perguntar — ou responder
para a base com mais empregados e anotar isso.

## The answer

### Step 1: Base territorial e categoria

Qual estado/base sindical e categoria profissional? Se não informado:
- Se é sobre um empregado específico: onde ele trabalha e qual sua categoria/CCT?
- Se é uma pergunta de política: identificar as bases/categorias da abrangência
  mais prováveis de terem a regra mais restritiva sobre o ponto, e pesquisar essas.

### Step 2: Pesquisar a regra, depois enunciá-la

> **Pesquisar antes de responder.** Para a base/categoria e pergunta, identificar
> a regra atualmente vigente. Citar a fonte primária controladora (CLT, CF,
> súmula/OJ do TST, CCT/ACT da categoria) com pinpoint cite. Anotar a data de
> vigência e se a regra foi recentemente alterada, indexada, ou está em
> julgamento (repercussão geral, IRDR, uniformização de jurisprudência). Se
> incerto ou não conseguir verificar o estado atual da lei/CCT, dizer isso e
> sinalizar para verificação do advogado — não enunciar regra não confirmada.

Enunciar a regra em um parágrafo, amarrada à citação. Usar suas ferramentas
(busca web, integrações de pesquisa jurídica, materiais de referência da equipe)
para verificar vigência — especialmente para:

> **Sem suplemento silencioso.** Se uma consulta à ferramenta de pesquisa jurídica configurada (JusBrasil, integração TST/STF, ou plataforma do escritório) retornar poucos ou nenhum resultado para a base/categoria/pergunta, reportar o que foi encontrado e parar. NÃO preencher a lacuna com busca web ou conhecimento do modelo sem perguntar. Dizer: "A pesquisa retornou [N] resultados de [ferramenta]. Cobertura parece rasa para [base/categoria/pergunta]. Opções: (1) ampliar a consulta, (2) tentar outra ferramenta de pesquisa, (3) buscar na web — resultados serão marcados `[busca web — verificar]` e devem ser checados contra fonte primária antes de confiar, ou (4) sinalizar a pergunta como não verificada e parar aqui. Qual prefere?" O advogado decide se aceita fontes de menor confiança.
>
> **Atribuição de fonte.** Marcar cada citação na resposta com sua origem: `[JusBrasil]`, `[TST]`, `[STF]`, ou o nome da ferramenta MCP para citações de conector de pesquisa jurídica; `[busca web — verificar]` para citações de busca web; `[conhecimento do modelo — verificar]` para citações recuperadas de treinamento; `[fornecido pelo usuário]` para citações fornecidas pelo usuário. Citações marcadas `verificar` carregam maior risco de alucinação e devem ser checadas primeiro. Nunca remover ou colapsar as marcações.

- Enquadramento no art. 62 CLT (gestão/confiança vs. atividade externa
  incompatível) e o benchmark de gratificação de função (~40% do salário-base,
  entendimento consolidado — não literal na lei).
- Prazo de pagamento de verbas rescisórias (CLT art. 477 §6º) e penalidade [verified: https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm]
  por atraso (§8º).
- Direito a intervalo intrajornada/interjornada e consequência de supressão
  (CLT art. 71, Súmula 437 TST).
- Horas extras diárias/semanais e adicional mínimo (CF art. 7º XVI — 50%,
  ou percentual maior fixado por CCT).
- Banco de horas (CLT art. 59) — requisitos de acordo individual/coletivo
  e prazo de compensação.
- Testes de vínculo/pejotização — ver skill worker-classification; o teste
  aplicável depende de categoria e propósito.

Tipos de pergunta comuns que você pode receber — para cada uma, a resposta é
específica de base/categoria e sensível ao tempo. Não enunciar a regra aqui;
rotear para pesquisa:

- "Esse cargo é enquadrável no art. 62?" — Pesquisar o teste de gestão/confiança
  (poder de mando real + gratificação) ou atividade externa incompatível,
  e jurisprudência do TST sobre o cargo específico.
- "Temos que pagar hora extra para X?" — Pesquisar CF art. 7º XVI, CLT art. 59,
  e adicional específico da CCT da categoria (pode ser >50%).
- "Temos que conceder intervalo?" — Pesquisar CLT art. 71 (intrajornada) e
  art. 66 (interjornada), e consequência de supressão total/parcial
  (Súmula 437 TST — pagamento como extra, não apenas indenizatório).
- "Quando a rescisão é devida?" — Pesquisar CLT art. 477 §6º (10 dias corridos
  do término do contrato, ambas as modalidades) e penalidade do §8º.
- "Temos que homologar/ter assistência sindical?" — Pesquisar se a CCT da
  categoria exige assistência sindical na rescisão (não é mais exigência
  legal geral desde a Lei 13.467/2017, mas pode ser cláusula de CCT).
- "Podemos classificar essa pessoa como PJ?" — Rotear para
  `/employment-legal:worker-classification` se os fatos não estiverem claros.

### Step 2a: Cálculo de horas extras e reflexos

Quando a pergunta for um cálculo de horas extras retroativas, diferença de
adicional, ou qualquer questão que gire em torno da "base de cálculo" da hora
extra, usar este roteiro. Não responder a partir do salário-hora nu × horas
extras; esse é o erro mais comum que este skill existe para pegar.

**A base de cálculo NÃO é só o salário-hora.** A remuneração-base para hora
extra integra comissões, prêmios habituais, adicionais de periculosidade/
insalubridade, e demais parcelas de natureza salarial habitualmente pagas —
excluídas parcelas indenizatórias (ex.: ajuda de custo, diárias ≤50% do
salário) e parcelas de natureza eventual/discricionária.

1. **Comissões e prêmios habituais integram a base.** Se pagos com
   habitualidade, dividir o valor pelo número de horas do período para achar
   o acréscimo por hora à base de cálculo. Prêmio verdadeiramente eventual
   (sem habitualidade, sem expectativa) é categoria estreita.
2. **Reflexos em outras verbas.** Hora extra habitual gera reflexo em DSR
   (descanso semanal remunerado), 13º salário, férias + 1/3, e FGTS. Se a
   pergunta for sobre retroativo, computar os reflexos — não apenas o valor
   bruto da hora extra.
3. **Mostrar a conta.** Imprimir a fórmula e os insumos explicitamente:
   ```
   Base de cálculo = (salário-base + comissões/prêmios habituais + adicionais
                       de natureza salarial) ÷ horas mensais contratuais
   Hora extra devida = base de cálculo × 1,5 (ou percentual da CCT) × horas extras
   Reflexo em DSR      = hora extra devida ÷ dias úteis × dias de repouso
   Reflexo em 13º/férias/FGTS = sobre a soma (base + hora extra + reflexo DSR)
   ```
   Um número sem a fórmula não é utilizável por advogado trabalhista.
4. **Prescrição.** Quinquenal (últimos 5 anos, contados retroativamente da
   propositura) e bienal (2 anos do fim do contrato para propor a ação) —
   CF art. 7º XXIX. Declarar o marco temporal explicitamente e computar os
   dois limites, salvo se o usuário já tiver estabelecido as datas.
5. **Overlay de CCT.** Muitas categorias têm adicional de hora extra acima
   dos 50% mínimos (60%, 75%, 100% em domingos/feriados), e piso salarial
   próprio que muda a base de cálculo. Checar a CCT da categoria contra a
   base territorial do Step 1 e sinalizar onde a norma coletiva é mais
   benéfica que a CLT (princípio da norma mais favorável).
6. **Anexar a marca de verificação ao número.** Qualquer valor retroativo
   produzido por este skill carrega `[verificar — consultar advogado
   trabalhista antes de afirmar ou pagar]` na linha em que o número aparece.
   O cálculo é trabalho de especialista; o skill é roteiro, não parecer.

Se a pergunta for um cálculo retroativo e faltar algum destes insumos
(detalhamento de comissões/prêmios, CCT aplicável, período/prescrição,
jornada contratual), **perguntar antes de calcular**. Um número errado e
confiante é o pior output que este skill pode produzir.

### Step 3: O sinal

Isso é um caso de fronteira? Ser honesto.

- Se a resposta é clara pela regra pesquisada: dizer isso. "Enquadrável no
  art. 62 II — atende gestão real + gratificação acima do benchmark de ~40%."
- Se é fronteiriço: dizer isso. "O poder de mando é discutível — esse cargo
  pode ir para qualquer lado. Recomendo tratar como não enquadrado (controle
  de ponto) para segurança, ou buscar parecer formal."
- Se a lei/CCT está em mudança: dizer isso. "Essa CCT foi renegociada
  recentemente — a versão atual vigora a partir de [data]. Confirmar data
  de vigência antes de confiar nesta resposta."
- Se não foi possível verificar vigência: dizer isso. Não adivinhar.

## Output format

Conversacional. Isso é Q&A, não memorando.

> **Pre-flight de conector de pesquisa.** Antes de emitir a resposta, checar se um conector de pesquisa jurídica está acessível nesta sessão — JusBrasil, integração TST/STF, ou qualquer MCP de pesquisa configurado pelo escritório. Coletar isso na nota de revisão per CLAUDE.md `## Outputs`: se nenhum conector retornar resultados no Step 2 (ou nenhum estiver configurado em tempo de execução), registrar na linha **Fontes:** da nota de revisão — ex.: `não conectado — citações de conhecimento de treinamento; pinpoint cites (súmula/OJ/artigo) carregam maior risco de alucinação, checar essas primeiro`. Marcações `[conhecimento do modelo — verificar]` por citação permanecem inline. Não emitir banner isolado acima do output.

> **Pressuposto de base/categoria.** Respostas se aplicam apenas à base territorial/categoria identificada. Regras de jornada/remuneração, pisos e prazos de rescisão variam materialmente por CCT, e muitas regras são renegociadas anualmente. Se o empregado está em outra base/categoria, ou a pergunta foi respondida para a base/categoria padrão da abrangência, esta resposta pode não se aplicar como escrita.

```
**[Base territorial/categoria]:** [A regra pesquisada, um parágrafo, com
pinpoint cite e nota de vigência.]

[Se caso de fronteira ou lei/CCT em mudança: o sinal.]

[Se a resposta difere em outras bases/categorias da abrangência: uma linha
anotando isso, e se as diferenças são materiais.]
```

> **Verificar citações.** Qualquer julgado, súmula, OJ, artigo de lei, ou cláusula de CCT acima foi gerado com assistência de IA. Antes de confiar em uma citação, checar contra JusBrasil, o site do TST/STF, o texto da CCT vigente, ou a ferramenta de pesquisa do seu escritório quanto a exatidão, vigência e histórico posterior. Citações fabricadas ou incorretas em petições ou pareceres formais já resultaram em sanções.

## Close with the next-steps decision tree

Encerrar com a árvore de decisão de próximos passos per CLAUDE.md `## Outputs`.
Customizar as opções para o que este skill acabou de produzir — os cinco ramos
padrão (rascunhar X, escalonar, buscar mais fatos, aguardar, algo mais) são
ponto de partida, não trava. A árvore é o output; o advogado escolhe.

## What this skill does not do

- Enunciar a regra de memória — toda resposta é fundamentada em fonte primária
  pesquisada e citada, verificada quanto a vigência.
- Tomar decisões de enquadramento/classificação em casos de fronteira. Enuncia
  a regra e sinaliza o caso de fronteira. Humano decide.
- Dar um levantamento de todas as CCTs da abrangência a menos que solicitado.
  Responde para a(s) base(s)/categoria(s) relevante(s).
- Rastrear quando a resposta muda. Se pisos/adicionais são renegociados ou a
  lei muda, a resposta fica desatualizada. Perguntar de novo para a atual.
