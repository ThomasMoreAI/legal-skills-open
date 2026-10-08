---
name: 2-1-diagnosticar-emidio-trancoso
title: Diagnosticar — Forças e Fragilidades do Caso
description: Análise honesta e adversarial das forças e fragilidades de um caso ou matéria — fáticas, jurídicas, probatórias, argumentativas e lógicas — tanto da sua posição quanto da contrária, produzindo o DIAGNOSTICO.md.
author: emidio-trancoso
author_url: https://github.com/emidio-trancoso/advocacia-aberta/tree/main/.agents/skills/2.1-diagnosticar
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Diagnosticar — Forças e Fragilidades do Caso

Esta skill faz um diagnóstico honesto e adversarial de uma matéria jurídica: mapeia, lado a lado, as **forças** e as **fragilidades** da sua posição e da posição contrária (quando houver). Funciona para um litígio, mas também para avaliar a viabilidade de uma tese, os riscos de um contrato ou os pontos fracos de um parecer.

O coração da skill é o espírito **red-team**: atacar a própria posição como se você fosse o adversário. É desconfortável, e é exatamente por isso que dá valor — você descobre os furos antes que a parte contrária (ou o juiz, ou o cliente) os descubra. Cada ponto forte vira algo a blindar com fundamentação; cada ponto fraco vira algo a corrigir ou contornar.

A skill lê o `SUMARIO.md` do caso (produzido pela skill `organizar-caso`) e os
documentos relevantes, e produz o `DIAGNOSTICO.md`.

## Instrução

Esta skill funciona em dois modos, conforme o que você tem em mãos. Escolha pelo que o
usuário forneceu; na dúvida, pergunte.

- **Modo repositório** — você trabalha sobre a pasta de um caso no espaço de trabalho
  aberto no agente. Lê `casos/<caso>/analise/SUMARIO.md` e os documentos relevantes, e
  grava `casos/<caso>/analise/DIAGNOSTICO.md`. Use quando o usuário indicar um
  `<caminho-do-caso>` ou já existir uma pasta `casos/`.
- **Modo conversa** — não há pasta do caso: o `SUMARIO.md` e os documentos foram
  anexados na conversa (ou o sumário foi gerado antes, na própria conversa, pela skill
  `organizar-caso`). Use-os como entrada e, ao final, entregue o `DIAGNOSTICO.md` como
  arquivo para download. Use quando o usuário apenas anexar material.

Em ambos os modos, se ainda não houver um `SUMARIO.md`, execute primeiro a skill
`organizar-caso`.

### Modo repositório

Considere `<caminho-do-caso>` o caminho relativo informado pelo usuário (ex.:
`casos/contrato-prestacao-servicos` ou `casos/0001234-56`). Se não tiver sido
informado, peça-o antes de continuar. Os caminhos abaixo são todos relativos à raiz do
projeto aberta no agente.

### Modo conversa

Não há estrutura de pastas. Onde os passos citam `<caminho-do-caso>/analise/SUMARIO.md`,
leia o sumário anexado (ou gerado na conversa); onde citam a leitura de documentos, use
os anexos; e no Passo 6, em vez de gravar em `casos/<caso>/analise/`, produza o
`DIAGNOSTICO.md` e entregue-o como arquivo para download.

---

### Passo 1 — Ler o SUMARIO.md

Leia `<caminho-do-caso>/analise/SUMARIO.md`.

Identifique:

- Qual é a **sua posição** na matéria (ex.: o polo que você representa num litígio; o lado que você defende numa tese; quem contrata ou quem é contratado num contrato; o objetivo do parecer).
- Existe uma **posição contrária** explícita? Em litígio, sim (a outra parte). Numa tese ou parecer, a "posição contrária" é a interpretação ou o argumento que pode ser oposto à sua.
- A lista completa de documentos disponíveis.

---

### Passo 2 — Ler os documentos relevantes na íntegra

Leia cada documento relevante por inteiro — não pule páginas. A ordem de prioridade muda conforme o tipo de trabalho:

- **Litígio:** petição inicial, contestação, impugnação, ata/termo de audiência, transcrições, manifestações finais, e os documentos de prova centrais (contratos, notas, declarações, prints).
- **Avaliação de tese:** os fatos do caso, a base normativa que sustenta a tese e a base que a contraria, e as decisões/precedentes em ambos os sentidos.
- **Análise de contrato:** o contrato e seus anexos, a correspondência entre as partes, e a regulação aplicável.
- **Crítica a um parecer:** o parecer, as fontes que ele cita e as fontes que ele deixou de citar.

Se existir `analise/PROVA_ORAL.md` (produzido pela skill `transcrever` e pela análise
da audiência), leia-o primeiro — ele já consolida a síntese por depoente.

#### Cuidados na leitura de transcrições de depoimentos

Transcrições (automáticas ou manuais) exigem atenção redobrada:

- **Identifique quem fala antes de extrair qualquer trecho.** Transcrições automáticas costumam usar marcadores genéricos ("Falante 1", "Falante 2"). Cruze com a ata/termo de audiência, que lista os presentes e a ordem das oitivas.
- **Distinga o tipo de declarante:** parte (declaração com valor confessório), testemunha (sob compromisso de dizer a verdade), informante (sem compromisso). Uma confissão da parte pesa mais que a fala de um informante.
- **Identifique quem fez a pergunta.** A mesma resposta tem peso diferente se foi dada ao juiz, ao advogado da própria parte (pergunta possivelmente ensaiada) ou ao advogado contrário (contraditório real).
- **Anote hesitações e contradições.** Respostas evasivas, pausas longas, falas que começam negando e terminam admitindo ("não foi apresentado antes, mas ela sempre estava com pressa...") são confissões qualificadas — registre o trecho exato.
- **Transcrições automáticas têm erros**, sobretudo em vocabulário técnico-jurídico. Em caso de dúvida sobre o trecho, marque `[transcrição incerta]` em vez de citar como fato.

#### Cuidados na leitura de provas conversacionais (WhatsApp, e-mail, prints)

Antes de extrair qualquer trecho ou atribuir uma declaração, confirme:

- **Quem enviou cada mensagem** — em prints, o balão à direita costuma ser de quem juntou o print; o da esquerda, do interlocutor. Se não houver indicação visual, infira pelo contexto.
- **Nome ou número de cada interlocutor** — verifique o cabeçalho do chat; se não houver, cruze com o número ou o contexto.
- **Data e hora de cada mensagem** — a ordem cronológica pode mudar completamente o sentido de uma sequência.
- **Quem juntou o print aos autos** — quem juntou escolheu quais trechos mostrar. Procure saltos na numeração, horários inexplicados ou mensagens aparentemente faltando.
- **Documentos não assinados:** registre a ausência de assinatura e por qual lado foram juntados.
- **Laudos e declarações de terceiros:** identifique quem os contratou e se há conflito de interesse.

---

### Passo 3 — Análise das forças e fragilidades

Avalie a matéria por cinco dimensões. Em cada uma, examine **a sua posição** e a **posição contrária** (quando houver). Seja honesto: anote tanto o que está sólido quanto o que está vulnerável.

#### 3a. Dimensão Fática

A força dos fatos e da prova que os sustenta.

Perguntas-guia:

- Quais fatos estão bem provados e quais foram apenas alegados sem suporte?
- Algum documento contradiz um fato afirmado?
- A cronologia faz sentido?
- Houve omissão estratégica de algo que só veio à tona depois?
- A prova conversacional foi atribuída ao interlocutor correto?

#### 3b. Dimensão Jurídica

A solidez da base normativa.

Perguntas-guia:

- A norma aplicada é a correta para o contexto?
- Há norma específica que deveria ser invocada e não foi?
- A subsunção (fato → norma → consequência) se sustenta?
- Existe jurisprudência consolidada a favor? E contra?

#### 3c. Dimensão Probatória

A qualidade e a suficiência das provas para o que se quer demonstrar.

Perguntas-guia:

- A prova existente é suficiente para o ônus que recai sobre cada lado?
- Há prova conclusiva ou apenas indiciária apresentada como conclusiva?
- Que prova falta, e quem teria de produzi-la?
- Alguma prova é frágil quanto à autenticidade, à autoria ou ao contexto?

#### 3d. Dimensão Argumentativa

A coerência interna do raciocínio.

Perguntas-guia:

- Algum lado afirmou X em um ponto e o contrário de X em outro?
- Um argumento usado para atacar o outro lado poderia voltar-se contra quem o fez?
- Há teses incompatíveis defendidas pelo mesmo lado?
- Quem depõe a favor tem isenção ou tem vínculo com a parte?

#### 3e. Dimensão Lógica

A validade das deduções.

Perguntas-guia:

- A conclusão segue necessariamente das premissas?
- Houve inversão de ônus sem base?
- Há silêncio eloquente — um argumento importante ficou sem resposta?
- Alguma premissa é falsa ou apenas presumida?

---

### Passo 4 — Mapear a munição disponível

Liste os cruzamentos mais poderosos a favor da sua posição: trecho/confissão A + documento B = conclusão Z. Cada item deve ter fonte precisa (arquivo + página ou trecho).

---

### Passo 5 — Red-team da sua posição

Vista a roupa do adversário e ataque a sua própria posição. Identifique os 3 a 5 pontos mais vulneráveis e como o outro lado provavelmente vai explorá-los. Nesta seção **não há defesa** — só o ataque. A defesa virá depois, na fundamentação e na peça.

---

### Passo 6 — Escrever o DIAGNOSTICO.md

**Antes de escrever:** dentro de cada seção, ordene os itens do mais impactante para o menos impactante. O item ⭐⭐⭐ mais decisivo vem primeiro. Não misture impactos: todos os ⭐⭐⭐ antes dos ⭐⭐, todos os ⭐⭐ antes dos ⭐.

Escreva `<caminho-do-caso>/analise/DIAGNOSTICO.md` (crie a pasta `analise/` se não
existir):

```markdown
---
caso: [nome da pasta do caso]
sua_posicao: [descreva sua posição na matéria]
gerado_em: [data]
documentos_analisados: [lista dos documentos lidos]
---

# DIAGNÓSTICO — [nome do caso]

> Análise honesta das forças e fragilidades — fáticas, jurídicas, probatórias, argumentativas e lógicas.
> Cada seção é ordenada do mais ao menos impactante. ⭐⭐⭐ alto · ⭐⭐ médio · ⭐ baixo

---

## 1. Forças da Nossa Posição
*(ordenadas da mais decisiva à mais periférica)*

**[Título do ponto forte mais decisivo]** ⭐⭐⭐
- **O quê:** [descrição]
- **Fonte:** [documento, trecho ou página]
- **Como sustentar:** [o que blinda ou amplifica este ponto]

---

## 2. Fragilidades da Posição Contrária
*(omitir se não houver posição contrária identificável)*

### 2.1 Fáticas
**[Título]** ⭐⭐⭐
- **O quê:** [descrição]
- **Fonte:** [documento, trecho ou página]
- **Como usar:** [argumento ou pedido que isto sustenta]

### 2.2 Jurídicas
[mesmo formato]

### 2.3 Probatórias
[mesmo formato]

### 2.4 Argumentativas
[mesmo formato]

### 2.5 Lógicas
[mesmo formato]

---

## 3. Munição Disponível
*(ordenada pelo poder do cruzamento — do mais decisivo ao mais periférico)*

**[Título do cruzamento mais poderoso]** ⭐⭐⭐
- **Elemento A:** [fonte + interlocutor identificado, se for conversa]
- **Elemento B:** [fonte]
- **Conclusão:** [o que este cruzamento demonstra]

---

## 4. Pontos Fracos da Nossa Posição (Red-team)
*(ordenados do mais vulnerável ao menos vulnerável)*

**[Ponto mais vulnerável]** ⭐⭐⭐
- **Ataque provável:** [como o outro lado vai explorar]
- **Impacto se não enfrentado:** [consequência]

---

## 5. Questões em Aberto

- [ ] [o que precisa ser investigado, confirmado com o cliente ou produzido como prova]
```

---

### Passo 7 — Confirmar e indicar o próximo passo

Informe ao usuário:
- Quantas forças e quantas fragilidades foram mapeadas, por dimensão.
- Os 3 pontos mais críticos (⭐⭐⭐), de ambos os lados.
- Que o diagnóstico alimenta os próximos passos:
  - `buscar-fontes` — para fundamentar os pontos fortes e blindar os fracos com legislação, súmulas e jurisprudência.
  - `redigir-peca` — para transformar o diagnóstico na peça (petição, contrato, parecer ou o que a matéria pedir).
