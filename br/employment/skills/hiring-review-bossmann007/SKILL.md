---
name: hiring-review-bossmann007
title: 'Hiring review'
description: Revisa uma carta-proposta/contrato de trabalho e qualquer cláusula restritiva (não-concorrência, não-aliciamento) — com checagem de base territorial/CCT incluída. Regras substantivas (exigibilidade de cláusula restritiva, piso salarial da categoria, enquadramento no art. 62 CLT) são pesquisadas por contratação, não armazenadas. Use quando o usuário disser "revisa essa proposta", "podemos usar não-concorrência aqui", "confere essa carta-proposta", "contratação em [estado/categoria]", ou anexar uma proposta.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/employment-legal/skills/hiring-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: pt
---

# /hiring-review

1. Carregar `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → abrangência territorial, gatilhos de revisão de contratação, política de cláusula restritiva.
2. Usar o workflow abaixo.
3. Verificar: base territorial/CCT, enquadramento (art. 62 CLT), cláusulas restritivas, conformidade de verificação de antecedentes (LGPD).
4. Sinalizar qualquer item que acione a tabela de escalonamento por base/CCT.

---

## Matter context

**Matter context.** Verificar `## Matter workspaces` no CLAUDE.md de nível prática. Se `Enabled` for `✗` (padrão para in-house), pular o resto deste parágrafo — os skills usam contexto de nível prática e a mecânica de matéria fica invisível. Se habilitado e não houver matéria ativa, perguntar: "Para qual matéria é isso? Rode `/employment-legal:matter-workspace switch <slug>` ou diga `practice-level`." Carregar o `matter.md` da matéria ativa para contexto e overrides específicos. Gravar outputs na pasta da matéria em `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Nunca ler arquivos de outra matéria a menos que `Cross-matter context` esteja `on`.

---

## Purpose

Carta-proposta é, na maior parte, boilerplate até não ser. A checagem de base
territorial/CCT e a checagem de cláusula restritiva são onde este skill se paga.
O skill não afirma a lei — toda regra específica de categoria/base territorial é
pesquisada e citada no momento da revisão.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → abrangência territorial, gatilhos de revisão de contratação, política de cláusula restritiva, local do modelo de carta-proposta.

## Output header

Antepor o cabeçalho de sigilo profissional de `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Outputs` (difere por papel do usuário — ver `## Who's using this`).

## Workflow

### Step 1: Base territorial e categoria

Onde essa pessoa vai efetivamente trabalhar? Não onde fica a sede — onde *ela*
está.

Se remoto/home office (CLT art. 75-A a 75-E): a base territorial de onde o
empregado presta serviço define o sindicato/CCT aplicável, salvo previsão
diversa no contrato. Se híbrido: geralmente a base do local de trabalho
habitual.

Verificar a tabela de base/CCT em `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. Se não estiver na tabela — nova base territorial —
sinalizar: "Primeira contratação nessa base/categoria. A tabela não cobre isso.
Pesquisa necessária antes de enviar a proposta — inclusive qual sindicato/CCT
se aplica e se há piso salarial diferenciado."

### Step 2: Enquadramento (CLT art. 62)

O cargo se enquadra na exceção de controle de jornada (art. 62, I — atividade
externa incompatível com controle; art. 62, II — cargo de gestão/confiança) ou
está sujeito a controle de jornada e, portanto, a horas extras?

| Teste | Verificar |
|---|---|
| Cargo de gestão/confiança (art. 62, II) | Tem poder de gestão, representa o empregador, recebe gratificação de função (mínimo 40% do salário, entendimento consolidado)? |
| Atividade externa incompatível (art. 62, I) | A função é efetivamente externa e sem possibilidade de controle de horário, com anotação em CTPS/contrato? |
| Salário e gratificação | O valor pago sustenta o enquadramento alegado, ou é usado apenas para escapar de horas extras? |

> **Pesquisar antes de afirmar o enquadramento.** Identificar o piso salarial da
> categoria/CCT aplicável e a jurisprudência recente do TST sobre o
> enquadramento pretendido para a função — o entendimento sobre "cargo de
> confiança" é revisitado com frequência (ex.: bancários, supervisores,
> "gerentes" sem poder de gestão real). Citar fontes primárias. Verificar
> atualidade.

Se a proposta diz "cargo de confiança" mas a descrição da função não sustenta
poder de gestão real — sinalizar. Enquadramento incorreto gera passivo de horas
extras retroativo com reflexos (FGTS, 13º, férias, INSS).

### Step 3: Cláusulas restritivas

Se a proposta inclui não-concorrência, não-aliciamento de clientes,
não-aliciamento de empregados, ou confidencialidade/cessão de propriedade
intelectual:

> **Pesquisar exigibilidade antes de aconselhar.** Para a base territorial do
> empregado, identificar o entendimento atualmente operante sobre cada
> cláusula restritiva na proposta. No Brasil não há lei federal específica
> sobre não-concorrência pós-contratual — o entendimento é construído por
> jurisprudência do TST e doutrina, exigindo tipicamente: (a) limitação
> territorial razoável, (b) limitação temporal razoável (jurisprudência tende a
> aceitar até ~2 anos), (c) **indenização compensatória durante a vigência da
> restrição** (sem contrapartida financeira, a cláusula tende a ser
> considerada abusiva/inexigível) e (d) proteção a interesse legítimo
> (segredo de negócio, clientela, não mera limitação à liberdade de trabalho,
> CF art. 5º, XIII). Não presumir exigibilidade sem checar esses quatro
> elementos. Observar também:
> - O tipo específico de cláusula (não-concorrência, não-aliciamento de
>   clientes, não-aliciamento de empregados, confidencialidade/segredo
>   industrial, cessão de PI conforme Lei 9.279/1996) — cada uma com regras
>   próprias.
> - Se há contrapartida financeira prevista e se o valor é minimamente
>   compatível com a restrição imposta.
> - Prazo, forma de pagamento da indenização e eventual cláusula penal.
> - Compatibilidade com a CCT da categoria (algumas convenções vedam ou
>   limitam cláusulas de não-concorrência).
> Citar fontes primárias. Verificar atualidade.

Conforme a política de cláusula restritiva em `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`: essa contratação
recebe cláusula restritiva? Algumas empresas usam seletivamente. Aplicar a
política interna primeiro, depois sobrepor a pesquisa de base territorial/CCT.

> **Sem suplemento silencioso.** Se uma pesquisa na ferramenta de pesquisa
> jurídica configurada retornar poucos ou nenhum resultado para o piso da
> categoria, regras de cláusula restritiva, ou qualquer outro item em
> pesquisa, reportar o que foi encontrado e parar. NÃO preencher a lacuna com
> busca web ou conhecimento do modelo sem perguntar. Dizer: "A busca retornou
> [N] resultados de [ferramenta]. Cobertura parece rasa para [base/tópico].
> Opções: (1) ampliar a busca, (2) tentar outra ferramenta de pesquisa, (3)
> buscar na web — resultados marcados `[busca web — verificar]` e devem ser
> checados contra fonte primária antes de confiar, ou (4) sinalizar como não
> verificado e parar. Qual você prefere?" O advogado decide se aceita fontes
> de confiança menor.
>
> **Atribuição de fonte.** Marcar cada citação na revisão com sua origem:
> `[JusBrasil]`, `[TST]`, ou o nome da ferramenta MCP para citações obtidas de
> conector de pesquisa jurídica; `[busca web — verificar]` para citações de
> busca web; `[conhecimento do modelo — verificar]` para citações lembradas do
> treinamento; `[fornecido pelo usuário]` para citações que o usuário forneceu.
> Citações marcadas `verificar` carregam maior risco de fabricação e devem ser
> checadas primeiro. Nunca remova ou colapse as tags.

### Step 4: Exigências específicas da base territorial/CCT

Verificar a tabela em `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` para essa base/categoria. Categorias comuns
a pesquisar em cada contratação:

- **Igualdade salarial e transparência (Lei 14.611/2023)** — a empresa está no
  grupo obrigado a publicar relatório de transparência salarial e de critérios
  remuneratórios (empresas com 100+ empregados)? Essa proposta é consistente
  com a política salarial e o plano de cargos publicados?
- **Verificação de antecedentes** — dado de antecedente criminal é dado
  pessoal sensível (LGPD art. 5º, II se ligado a origem racial/convicção etc.,
  ou tratado como dado pessoal comum sensível ao contexto); exige base legal
  específica (cumprimento de obrigação legal/regulatória, ou legítimo
  interesse com finalidade estritamente necessária ao cargo) e não pode ser
  genérica para toda contratação.
- **Cotas legais (PCD, aprendiz)** — a empresa está sujeita à cota de pessoas
  com deficiência (Lei 8.213/1991 art. 93) ou de aprendizes (CLT art. 429)? Essa
  contratação impacta o cumprimento da cota?
- **Avisos/registros obrigatórios na admissão** — registro no eSocial dentro do
  prazo legal, exame médico admissional (NR-7 PCMSO), assinatura de CTPS
  digital.

Citar fontes primárias. Verificar atualidade.

### Step 5: Conteúdo da carta-proposta/contrato

Ler o documento. Verificar:

**Não existe "at-will" no Brasil.** A CLT não permite dispensa sem aviso
prévio e sem verbas rescisórias — mesmo em contrato por prazo indeterminado,
a dispensa exige aviso prévio (Lei 12.506/2011, proporcional ao tempo de [verified: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12506.htm]
serviço) e pagamento das verbas legais. Nunca recomende linguagem de "at-will"
em um contrato brasileiro — é juridicamente sem efeito aqui e sinaliza para o
advogado do empregado que quem redigiu não entende a CLT.

Em vez disso, verificar:
- Tipo de contrato (prazo indeterminado / prazo determinado conforme CLT art.
  443 / experiência, limitado a 90 dias conforme CLT art. 445, parágrafo único)
- Período de experiência e suas prorrogações (respeitando o limite legal)
- Jornada, salário, função, local de trabalho declarados
- Benefícios (VR/VA, plano de saúde, PLR se houver) consistentes com a política
  e com a CCT aplicável
- Cláusula de confidencialidade e cessão de PI compatível com Lei 9.279/1996 e
  Lei 9.610/1998 (se envolver criação de software/obra)
- Cláusula integradora para que a proposta seja o acordo completo

## Output

> **Premissa de base territorial.** Esta revisão aplica as regras da base
> territorial/categoria do empregado identificada no Step 1. Exigibilidade de
> cláusulas restritivas, enquadramento no art. 62 CLT, piso salarial da
> categoria e avisos obrigatórios variam materialmente por base/CCT e alguns
> mudaram recentemente. Se o local de trabalho do candidato mudar, ou a função
> abranger mais de uma base, esta revisão pode não valer como redigida.

```markdown
[CABEÇALHO DE SIGILO PROFISSIONAL — conforme config do plugin ## Outputs — difere por papel; ver `## Who's using this`]

## Revisão de Contratação: [Candidato] — [Função] — [Base territorial/CCT]

**Geral:** [Liberado para enviar | Ajustes necessários | Escalar]

### Base territorial/CCT: [Estado/Categoria]
[Entrada da tabela de base/CCT. Gatilhos de escalonamento automático que dispararam.]

### Enquadramento (art. 62 CLT)
[Chamada de enquadramento, fundamentada em piso pesquisado e jurisprudência.
Quaisquer flags.]

### Cláusulas restritivas
[Se houver. Chamada de exigibilidade conforme regras de base territorial
pesquisadas, com citações pontuais e nota de atualidade. Mudanças sugeridas.]

### Exigências específicas de base/CCT
[Transparência salarial, cotas, avisos obrigatórios, etc. — cada um pesquisado
e citado, ou sinalizado como necessitando pesquisa.]

### Carta-proposta/contrato
[Quaisquer problemas com o documento em si]

### Itens de ação
- [ ] [mudança específica necessária antes de enviar]
```

## Consequential-action gate (fazer uma proposta)

**Antes de produzir uma recomendação "Liberado para enviar" ou uma
carta-proposta final para assinatura:** ler `## Who's using this` em
`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. Se o Papel for **Não-advogado**:

> Fazer uma proposta tem consequências jurídicas — a carta é um contrato, e
> cláusulas restritivas, enquadramento e exigências de base territorial são
> difíceis de desfazer depois de enviadas. Você revisou essa proposta com um
> advogado? Se sim, prossiga. Se não, aqui está um resumo para levar a ele:
>
> - Candidato, função, base territorial (onde vai efetivamente trabalhar)
> - Chamada de enquadramento (art. 62 CLT) e por quê
> - Cláusulas restritivas na proposta e a análise de exigibilidade
> - Exigências específicas de base/categoria que se aplicam (transparência
>   salarial, cotas, avisos obrigatórios)
> - Perguntas em aberto e o que está sem resolver
> - O que pode dar errado (passivo de horas extras por enquadramento errado,
>   cláusula de não-concorrência inexigível por falta de indenização
>   compensatória, aviso obrigatório faltando)
> - O que perguntar ao advogado (esse é o modelo certo para essa base/CCT;
>   podemos usar nossa cláusula de não-concorrência padrão aqui; quais avisos
>   precisam acompanhar a carta)
>
> Se precisar encontrar um advogado: use o serviço de indicação da OAB da sua
> seccional.

Não produza um output "Liberado para enviar" além deste gate sem um "sim"
explícito. Um rascunho marcado como DRAFT sinalizado para revisão do advogado
está ok.

---

## Close with the next-steps decision tree

Encerrar com a árvore de decisão de próximos passos conforme CLAUDE.md
`## Outputs`. Customizar as opções para o que este skill acabou de produzir —
os cinco ramos padrão (rascunhar X, escalar, buscar mais fatos, aguardar e
observar, outra coisa) são um ponto de partida, não uma obrigação. A árvore é
o output; o advogado escolhe.

## What this skill does not do

- Redigir a carta-proposta — revisa ela.
- Tomar a decisão de contratar — verifica o papelório.
- Afirmar regras de cláusula restritiva ou enquadramento de memória — toda
  chamada específica de base territorial se baseia em fontes pesquisadas,
  citadas e verificadas quanto à atualidade.
- Pesquisar uma nova base territorial/categoria em profundidade sozinho —
  sinaliza que pesquisa é necessária, e usa `wage-hour-qa` ou advogado externo
  para preencher.
