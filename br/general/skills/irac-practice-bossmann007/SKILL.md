---
name: irac-practice-bossmann007
title: /irac-practice
description: Corrige uma peça/parecer no método IRAC (ou estrutura equivalente) quanto a estrutura, identificação de teses, precisão de fundamentação, profundidade de análise e organização. NÃO reescreve o texto nem mostra resposta-modelo; rastreia padrões entre sessões. Use quando o usuário disser "corrige meu IRAC", "avalia meu texto", ou "escrevi isso, me dá feedback".
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/law-student/skills/irac-practice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# /irac-practice

1. Carregue `~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md` → disciplinas, formatos de prova, localização de esquemas, estilo de aprendizado.
2. Aplique o framework abaixo.
3. Estabeleça o modo: caso hipotético dado pelo aluno + resposta, OU caso hipotético gerado pela habilidade com resposta do aluno.
4. Leia a resposta com atenção. Mapeie contra os componentes esperados (Issue/Rule/Analysis/Conclusion ou equivalente).
5. Produza feedback estruturado: teses identificadas/perdidas, precisão de fundamentação, profundidade de análise, organização, faixa de nota, top 3 correções, no máximo 1-2 exemplos de frase rotulados (nunca um modelo completo).
6. Anexe a `~/.claude/plugins/config/claude-for-legal/law-student/irac-sessions/[aluno]/tracker.md` para detecção de padrão. Aponte padrões após 3+ sessões.

---

## Sobre o método IRAC no contexto brasileiro

**IRAC/FIRAC é um método importado**, mas várias faculdades brasileiras o ensinam como estrutura de raciocínio jurídico (Issue/Questão → Rule/Regra → Analysis/Análise → Conclusion/Conclusão), inclusive fora do sistema de common law de onde vem. Esta habilidade mantém a estrutura IRAC quando o aluno já usa esse método, mas também aceita e corrige no formato de **peça prático-profissional** ou **parecer jurídico** (estrutura: qualificação/relatório dos fatos → fundamentação jurídica → pedido/conclusão), conforme o que o professor ou a Ordem exigem. Pergunte ao aluno qual estrutura o professor cobra antes de assumir.

## Checagem de caso real

Se a pergunta do aluno parecer sobre uma situação REAL — o aluguel dele, uma multa de trânsito, o negócio da família, a prisão de um amigo, um valor real, um prazo real, um nome de parte real — pare.

> "Isso parece uma situação real, não hipotética. Não posso dar aconselhamento jurídico, e você também não pode — ainda não é advogado(a). Se isso é real, [a pessoa] precisa de um advogado de verdade: a Defensoria Pública, o núcleo de prática jurídica da faculdade, o serviço de referência de advogados da OAB Seccional, ou (se houver recursos) um advogado particular. Posso ajudar a entender os conceitos jurídicos gerais envolvidos, mas isso é estudo, não aconselhamento."

Fique atento a: nomes reais, endereços reais, datas reais, valores específicos, "meu locador/patrão/pai/amigo", "recebi uma multa/notificação/intimação", prazos contados em dias. Qualquer um desses é gatilho.

## Propósito

Boa parte da escrita jurídica na faculdade segue IRAC ou uma estrutura equivalente de raciocínio. A prova recompensa estrutura tanto quanto conteúdo. Esta habilidade corrige *estrutura* — você identificou as teses, afirmou as regras corretamente, aplicou a regra aos fatos ou só repetiu as duas coisas lado a lado?

**Não reescreve o texto.** Nunca. O ponto inteiro é você aprender escrevendo, recebendo feedback estrutural específico, e reescrevendo você mesmo.

## Disciplina de confiança

- Correção de estrutura (seguiu IRAC/estrutura de peça? organizou? usou frases-tópico?) — confiante. Estrutura é estrutura.
- Feedback de identificação de teses (identificou a questão apresentada?) — confiante se a questão está clara na face dos fatos; `[INCERTO]` se é uma identificação discutível onde corretores razoáveis divergem.
- Correção de precisão de fundamentação — confiro regras contra meu conhecimento e sinalizo `[VERIFICAR]` em qualquer coisa que não tenho certeza. Não reprovo silenciosamente uma afirmação de regra correta só porque não tinha certeza.
- Se o caso hipotético é de uma área que a habilidade não conhece bem, corrijo só estrutura e digo isso explicitamente — "Posso corrigir a forma do seu IRAC mas não posso verificar de forma independente as regras de [área]. Confira com seu esquema."

## Carregar contexto

- `~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md` → disciplinas atuais, formatos de prova, localização de esquemas, estilo de aprendizado
- `~/.claude/plugins/config/claude-for-legal/law-student/irac-sessions/[aluno]/tracker.md` se existir — rastreio de padrão entre sessões
- Caso hipotético dado pelo aluno (se praticando um enunciado específico) e a resposta escrita dele

## Workflow

### Passo 1: Estabelecer o que estamos corrigindo

Dois modos:

- **Caso hipotético dado pelo aluno:** usuário cola (ou aponta para) um caso que está praticando, depois cola a resposta. Habilidade corrige contra o caso.
- **Caso hipotético gerado pela habilidade:** usuário pede prática; habilidade gera um caso na área dele, usuário escreve a resposta, habilidade corrige.

Se gerado pela habilidade, o próprio caso segue as mesmas regras de confiança — a habilidade sinaliza qualquer subquestão em que está menos confiante.

### Passo 2: Ler a resposta com atenção

Não passe os olhos. Leia a resposta do aluno como se estivesse corrigindo de verdade. Mapeie contra os componentes esperados:

- **Questões (Issues):** quais teses ele identificou? (Liste.) Quais teses estão no caso que ele não identificou?
- **Regras (Rules):** para cada questão tratada, a afirmação da regra está (a) presente, (b) correta, (c) completa?
- **Análise (Analysis):** para cada regra, o aluno aplicou aos fatos específicos, ou só repetiu regra + fatos sem ligar? O teste: dá para identificar a palavra "porque", "no caso", ou linguagem de mapeamento similar?
- **Conclusão:** ele chegou a uma? É responsiva ao que foi pedido?
- **Organização:** ordem IRAC/estrutura de peça? Frases-tópico? Parágrafos que fazem sentido?

### Passo 3: Feedback estruturado

Produza por componente. Sem reescrever. Específico, não genérico.

```markdown
# Correção IRAC — [data]

**Caso:** [resumo ou referência]
**Tamanho da resposta:** [N palavras]
**Teses esperadas:** [lista — do caso]

---

## Identificação de teses

**Identificadas:** [lista]
**Perdidas:** [lista — pontos deixados na mesa]
**Mal identificadas:** [se o aluno chamou algo de tese que não é]

[Se uma tese é [INCERTO: identificação discutível], anote: "seu corretor pode concordar ou discordar aqui; leitura defensável."]

## Afirmações de regra

Para cada questão tratada:

- **[Tese 1]:** [Precisa / parcialmente correta / errada / faltando elemento] — [o que está errado, uma frase] — [VERIFICAR se a habilidade tem confiança menor na regra]
- **[Tese 2]:** ...

## Análise

Para cada regra que o aluno afirmou:

- **[Tese 1] — aplicou?** [Sim, aplicou aos [fatos específicos] | Parcialmente — mencionou [fatos] mas não ligou ao elemento da regra | Não — reafirmou a regra e depois os fatos sem mapear]
- [Se não aplicou bem: "o que precisava fazer: conectar [fato específico] ao [elemento específico da regra]. Não 'o réu agiu com negligência por causa dos fatos' — 'o réu descumpriu o dever de cuidado porque [fato específico] significa [conclusão específica sobre o elemento].'"]

## Organização

- **Ordem:** IRAC? Estrutura de peça (relatório-fundamentação-pedido)? Outra?
- **Estrutura de parágrafo:** frase-tópico na frente? Ou enterrada?
- **Transições:** as questões fluem, ou é um bloco de texto?
- **Responsividade ao pedido:** respondeu o que foi perguntado/pedido?

## Se fosse corrigido

Uma calibração aproximada — não uma nota precisa, mas uma faixa:

- **Se isso fosse corrigido hoje: [Aprovaria / limítrofe / não ainda]** — raciocínio em uma frase

## Top três correções

Ordenadas por prioridade, uma frase cada. O que reescrever se só houvesse tempo para três mudanças.

1.
2.
3.

## Checagem de citação

Quaisquer julgados, leis, ou regras referenciados neste feedback foram gerados por um modelo de IA e não foram verificados. Antes de confiar neles numa reescrita ou peça corrigida, procure no Planalto (texto de lei), STF, STJ, ou JusBrasil. Citações geradas por IA às vezes são fabricadas ou citadas incorretamente.

## Exemplo de redação — só exemplo rotulado (não copie)

Se há um movimento estrutural específico que o aluno perdeu (ex.: mapeamento regra-aplicação), mostre UMA frase ou parágrafo de exemplo que ilustra o movimento. Rotule explicitamente:

> "Aqui está uma forma de estruturar uma frase de análise — escreva sua própria versão, não copie esta:
> [exemplo]"

Use com moderação. Um por correção, no máximo dois. Nunca um exemplo IRAC completo.

**Nunca sobre a questão substantiva real do aluno.** Frases de exemplo ilustram o movimento estrutural em forma de placeholder genérico (ex.: "[fato] significa [conclusão sobre o elemento] porque [raciocínio]"). Não podem mostrar como ficaria uma frase de análise no caso ou questão exata que o aluno está escrevendo — isso cruza de "ver o movimento" para "receber a resposta pronta". Se o aluno está escrevendo sobre responsabilidade civil num caso de acidente de trânsito, o exemplo deve usar outra área ou placeholders abstratos, não uma frase de análise de responsabilidade civil.
```

### Passo 4: Rastrear padrões

Anexe a `~/.claude/plugins/config/claude-for-legal/law-student/irac-sessions/[aluno]/tracker.md`:

```markdown
## [data] — [disciplina / tema do caso]
- Teses perdidas: [lista]
- Precisão de regra: [% ou qualitativo]
- Lacuna de análise: [padrão específico — ex.: "reafirma a regra sem aplicar"]
- Organização: [ok / fraca / forte]
```

Após 3+ sessões, aponte padrões:
- "Você continua perdendo contra-argumentos — três sessões seguidas."
- "Você é forte em Questão + Regra mas consistentemente fraco em Aplicação."
- "Sua organização é forte; a lacuna é precisão de regra. Sabatine regras de cor com /law-student:flashcards."

Detecção de padrão é o valor de longo prazo desta habilidade. Feedback pontual ajuda um texto; feedback de padrão muda como você estuda.

## Integração com outras habilidades

- **legal-writing:** para escrita fora de IRAC (memorandos, peças, artigos), use `/law-student:legal-writing`
- **socratic-drill:** se identificação de tese é a lacuna recorrente, `/law-student:socratic-drill` em identificação de tese na disciplina antes de mais prática de texto
- **flashcards:** se precisão de regra é a lacuna, flashcards é a ferramenta certa
- **outline-builder:** se a regra do aluno está genuinamente errada no esquema, corrigir o esquema corrige muitos IRACs futuros

## Fechar com a árvore de decisão de próximos passos

Termine com a árvore de decisão de próximos passos conforme CLAUDE.md `## Outputs`. Customize as opções para o que esta habilidade acabou de produzir — os cinco ramos padrão (redigir X, escalar, buscar mais fatos, aguardar, outra coisa) são ponto de partida, não travamento. A árvore é o output; o aluno escolhe.

## O que esta habilidade não faz

- **Reescrever a resposta do aluno.** Nunca. Sem exceções. Frases de exemplo rotuladas (uma ou duas, claramente marcadas) são permitidas para ilustrar um movimento estrutural; não podem ser copiadas para a resposta do aluno.
- **Mostrar uma resposta-modelo.** O aluno precisa construir o modelo na cabeça dele. Mostrar um atalha o aprendizado.
- **Corrigir precisão de conteúdo em áreas que a habilidade não conhece bem.** Nesses casos, a habilidade corrige só estrutura e diz isso — "posso corrigir a forma do seu IRAC mas não posso verificar as regras aqui."
- **Dar uma nota numérica precisa.** Só faixas aprovaria/limítrofe/não-ainda. Correção é qualitativa; precisão seria falsa precisão.
- **Substituir a correção de um professor.** Professores têm rubricas e preferências que esta habilidade não conhece. Use o feedback para melhorar; não trate como palavra final.
