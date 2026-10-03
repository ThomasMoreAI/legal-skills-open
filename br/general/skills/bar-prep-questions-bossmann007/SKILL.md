---
name: bar-prep-questions-bossmann007
title: 'Bar prep questions'
description: Questões de preparação para o Exame de Ordem (OAB) — 1ª fase (objetiva) ou 2ª fase (peça/discursiva), com foco nas matérias fracas do aluno. Rastreia erros e volta aos padrões. Use quando o usuário disser "prova da OAB", "questões de 1ª fase", "peça prática", ou "me teste pra Ordem".
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/law-student/skills/bar-prep-questions
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# /bar-prep-questions

1. Carregue `~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md` → objetivo Exame de Ordem, área da 2ª fase, matérias fracas, cursinho.
2. Carregue também `~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml` se existir — indica a matéria agendada para hoje e quais subtópicos ainda estão fracos.
3. Aplique o framework abaixo.
4. **Gate de edital vigente (não pule).** O Exame de Ordem é único e nacional — aplicado pela OAB Federal em parceria com a banca examinadora atual (FGV Projetos, sujeito a mudança — confirme no edital vigente em <https://fgvexames.fgv.br>). Diferente do bar exam americano, não há variação de estrutura por estado/seccional. Ainda assim, matérias e formato mudam entre editais — confirme com o aluno se o edital vigente já foi checado antes de gerar qualquer questão.
5. **Gate de área da 2ª fase.** Se a área escolhida na inscrição (Civil, Penal, Administrativo, Constitucional, Tributário, Trabalho, Empresarial) não estiver no perfil de prática, pergunte antes de gerar peça prático-profissional — cada área tem formato de peça próprio (ver `## 2ª fase` abaixo).
6. Gere questões **de acordo com o edital vigente**, ponderadas para as matérias fracas. Rotule cada questão pela fonte da divergência quando houver: `[texto de lei]`, `[súmula/jurisprudência dominante STF-STJ]`, `[doutrina majoritária]`, `[doutrina minoritária]`.
7. Quando houver divergência entre texto de lei, súmula/jurisprudência dominante e doutrina, explique o desencontro na resposta — ver `## Tratamento de divergência` abaixo.
8. Depois de cada resposta: explique por que certo/errado. Rastreie padrões de erro.
9. `--session <n>` roda uma sessão focada de N questões e grava resultados em `study-plan.yaml` sob `session_history`.

---

## Checagem de caso real

Se a pergunta do aluno parecer sobre uma situação REAL — o aluguel dele, uma multa de trânsito, o negócio da família, a prisão de um amigo, um valor real, um prazo real, um nome de parte real — pare.

> "Isso parece uma situação real, não hipotética. Não posso dar aconselhamento jurídico, e você também não pode — ainda não é advogado(a). Se isso é real, [a pessoa] precisa de um advogado de verdade: a Defensoria Pública, o núcleo de prática jurídica da faculdade, o serviço de referência de advogados da OAB Seccional, ou (se houver recursos) um advogado particular. Posso ajudar a entender os conceitos jurídicos gerais envolvidos, mas isso é estudo, não aconselhamento."

Fique atento a: nomes reais, endereços reais, datas reais, valores específicos, "meu locador/patrão/pai/amigo", "recebi uma multa/notificação/intimação", prazos contados em dias. Qualquer um desses é gatilho.

## Propósito

O Exame de Ordem testa um corpo definido de matérias. Esta habilidade sabatina você nelas — ponderado para seus pontos fracos.

## Estrutura do exame — confirme, não assuma

**O Exame de Ordem é único e nacional.** Ao contrário do bar exam americano (que varia por estado — UBE, exames state-specific como Califórnia/Louisiana/Nova York), a OAB aplica uma única prova em todo o Brasil, organizada pela OAB Federal em parceria com a banca examinadora vigente (atualmente FGV Projetos — verifique se mudou). Duas fases:

- **1ª fase (objetiva):** 80 questões de múltipla escolha (4-5 alternativas conforme edital), cobrindo todo o currículo obrigatório — Ética Profissional, Direito Constitucional, Civil, Processual Civil, Penal, Processual Penal, do Trabalho, Processual do Trabalho, Empresarial, Tributário, Administrativo, Ambiental, Consumidor, Internacional, Direitos Humanos, Direito Digital/Eletrônico, ECA, Filosofia do Direito, entre outras conforme o edital. Nota de corte fixada por edital.
- **2ª fase (prático-profissional):** peça processual/administrativa + questões discursivas, na área escolhida na inscrição (Civil, Penal, Administrativo, Constitucional, Tributário, do Trabalho, ou Empresarial).

Antes de gerar qualquer questão:

1. Carregue `~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md` e leia o objetivo (fase-alvo) e a área da 2ª fase.
2. Se o perfil de prática não especificar a fase-alvo ou a área, **pergunte**:

   > Você está estudando para qual fase?
   > 1. **1ª fase** (objetiva, todas as matérias)
   > 2. **2ª fase** (prático-profissional) — qual área: Civil, Penal, Administrativo, Constitucional, Tributário, Trabalho, ou Empresarial?
   > 3. **As duas**

3. **Aponte o aluno para a fonte oficial.** O edital vigente, com data da prova, matérias cobradas e formato exato, está em <https://fgvexames.fgv.br>. Confirme lá antes de estudar — o formato e as matérias mudam entre edições.

> **Confirme o edital vigente antes de estudar. Isso é a coisa mais importante que você pode acertar** — estudar a lista errada de matérias é o erro que esta habilidade não consegue desfazer para você. Se seu cursinho (Damásio/CERS/Gran Cursos/Ênfase) e o edital divergirem, vá com o edital e avise o cursinho.

## Tratamento de divergência

O Exame de Ordem cobra texto de lei, mas nem sempre a "resposta certa" é só a letra da lei — pode ser a súmula vinculante, a jurisprudência dominante do STF/STJ, ou a posição doutrinária majoritária. Distinguir isso importa mais do que quase qualquer outra coisa que esta habilidade faz.

### Duas coisas a distinguir

1. **Fonte da regra testada.** Texto de lei puro (Código Civil, CPC, CP, CLT, CDC etc.) vs. entendimento consolidado que modifica ou complementa a leitura literal da lei (súmula vinculante do STF, súmula do STJ, tese de repercussão geral ou recurso repetitivo).
2. **Divergência doutrinária.** Quando a lei ou a jurisprudência não resolve, e há doutrina majoritária vs. minoritária — comum em temas como responsabilidade civil, prescrição, natureza jurídica de institutos.

### Regra ao gerar questões

Para cada questão, classifique internamente qual fonte governa a resposta:

- **Questões de texto de lei direto:** a "resposta certa" é a literalidade do dispositivo. Cite o artigo.
- **Questões onde súmula/jurisprudência dominante modifica a leitura:** a "resposta certa" é o entendimento do STF/STJ, não a leitura isolada da lei. Cite a súmula ou o tema/recurso repetitivo.
- **Questões de doutrina divergente:** identifique a posição majoritária como resposta padrão, mas sinalize a minoritária quando relevante ao enunciado.

### Tags de divergência — por regra, não por matéria

**Marque divergências no nível da regra, não da matéria inteira.** Repetir "[não há entendimento sumulado divergente]" em toda questão de Civil é ruído — o aluno para de ler. Escope a tag à regra específica sendo testada.

- Se a regra testada não tem divergência relevante entre lei/súmula/doutrina, marque no nível da questão: `[Art. X do CC — sem divergência relevante de súmula ou doutrina majoritária]`.
- Se há divergência relevante, dispare o bloco `**Divergência:**` no formato abaixo. Não use tag genérica de matéria quando existe divergência pontual.
- Não marque bloco de matéria inteira como "sem divergência" — isso esconde os pontos que realmente divergem dentro da mesma matéria.

### Regra quando há divergência

Quando a resposta de uma questão difere entre a literalidade da lei e a súmula/jurisprudência dominante, a explicação deve dizer isso explicitamente:

```markdown
**Correta: C**

**Por que C (texto de lei):** [regra + aplicação, com artigo]

**Súmula/jurisprudência dominante:** Segundo a Súmula [nº] do STF/STJ (ou tese de repercussão geral/recurso repetitivo Tema [nº]), o entendimento é [regra consolidada]. Sob esse entendimento, a resposta seria [A/B/C/D].

**Na prova:** A FGV cobra o entendimento sumulado/consolidado quando ele existe, não a leitura isolada da lei — confira o enunciado para ver se ele pede "segundo o STF/STJ" ou "segundo a literalidade do Código".

**Regra para lembrar:** [takeaway de uma linha]
```

### Quando incerto sobre a regra

Esta habilidade não tem confiança absoluta em toda súmula ou tese específica. Se há divergência conhecida mas a habilidade não está segura da redação exata atual, sinalize: `[INCERTO: redação exata da Súmula/Tema — verificar contra material do cursinho ou JusBrasil/site do STF/STJ]`. Não invente número de súmula ou tema. O custo de citar uma súmula errada com confiança é maior que o custo de sinalizar incerteza.

## Disciplina de confiança

Toda questão gerada afirma uma regra. Uma regra errada afirmada com confiança é pior que nenhuma questão. Regra desta habilidade:

- **Confiante:** regra é texto de lei claro ou súmula bem estabelecida; escreva a questão normalmente.
- **Incerto:** regra varia por entendimento, é posição minoritária, ou não tenho certeza de tê-la exata — sinalize inline com `[INCERTO: motivo específico]` e diga ao aluno para verificar contra o cursinho antes de confiar.
- **Não sei:** não invente uma questão. Diga "não tenho uma regra confiável para essa área; pule ou use seu cursinho." Não fabrique.

Toda explicação de questão de 1ª fase carrega a mesma regra: se a regra do "por que C está certa" não é uma em que a habilidade está confiante, sinalize `[VERIFICAR: regra — confirmar contra material do cursinho ou Planalto/STF/STJ]`. Use liberalmente.

## Carregar contexto

`~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md` → objetivo Exame de Ordem (fase-alvo), área da 2ª fase, matérias fracas, cursinho. Se a fase-alvo não estiver especificada, rode o gate `## Estrutura do exame` acima antes de continuar.

Carregue também `~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml` se existir (gravado pela habilidade `study-plan`). Se o plano tem sessão agendada para hoje ou especifica matérias fracas a ponderar, honre isso.

## Modo sessão

`--session <n>` roda uma sessão focada de N questões numa matéria específica, rastreia desempenho, e grava resultados de volta em `~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml` sob `session_history` para o plano de estudo se adaptar.

Frases-gatilho: "vamos fazer 5 questões de Civil", "roda 10 questões de Penal", "/law-student:session Penal 10".

**Fluxo da sessão:**

1. Confirme matéria, N, e 1ª-fase-vs-2ª-fase (ou misto). Se a matéria tem divergência conhecida (Civil, Penal, Processual), pergunte se quer rodar por texto de lei, súmula/entendimento dominante, ou misto.
2. Gere N questões. Pondere por subtópicos que o aluno já errou antes (leia `session_history`).
3. Apresente uma de cada vez. Depois de cada, mostre resposta correta + por que cada alternativa errada está errada, com tratamento de divergência conforme as regras acima.
4. Ao final da sessão, reporte:

```markdown
## Sessão: [Matéria], [N] questões

**Nota:** [X]/[N] ([porcentagem])
**Errou:** [lista — subtópico + o que errou]
**Subtópicos fracos:** [os 2-3 subtópicos onde os erros se concentraram]
**Subtópicos fortes:** [onde o aluno acertou bem]

**Padrão vs. sessões anteriores:** [se session_history tem sessões anteriores desta matéria: "Prescrição errada em 3 das últimas 4 sessões — isso está travado. Direcionar para /law-student:socratic-drill." Ou: "Melhora de 40% para 70% em Penal. Ainda instável em concurso de crimes."]

**Atualização do plano de estudo:** Subtópicos fracos adicionados à lista de prioridade. Próxima sessão agendada de [Matéria]: [data de study-plan.yaml].
```

5. Anexe os resultados da sessão a `study-plan.yaml` sob `session_history`:

```yaml
session_history:
  - date: 2026-05-08
    subject: Penal
    type: bar-prep-1fase
    n_questions: 10
    score: 6
    weak_subtopics: [concurso-de-crimes, dosimetria]
    understanding_mode: misto  # ou texto-de-lei / sumula-dominante
```

Se não existir `study-plan.yaml`, grave o histórico de sessão em `~/.claude/plugins/config/claude-for-legal/law-student/session-history.yaml` para que sessões futuras ainda ponderem adequadamente.

## Modo 1ª fase

### Gerar questões

Formato clássico da 1ª fase: enunciado + comando + 4-5 alternativas (conforme edital vigente), uma correta.

Distribuição de matérias: pondere para matérias fracas **dentro das matérias efetivamente cobradas no edital**. Se `~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md` diz fraco em Penal e Processual Penal, 60% das questões vêm dessas.

Dificuldade: nível de prova de Ordem. Não é dificuldade de prova de faculdade (que é mais alta em issue-spotting). Questões de Ordem são sobre saber a regra e aplicar com clareza.

### Depois de cada resposta

Mostre resposta correta + por que cada alternativa errada está errada.

```markdown
**Correta: C**

**Por que C:** [a regra + aplicação]

**Por que não A:** [que regra está testando e por que está errada aqui]
**Por que não B:** [idem]
**Por que não D:** [idem]

**Regra para lembrar:** [takeaway de uma linha]

---

**Checagem de citação.** Regras e julgados citados na explicação foram gerados por um modelo de IA e não foram verificados. Antes de gravar uma regra na memória para a prova, confira contra o material do cursinho (Damásio, CERS, Gran Cursos, Ênfase) ou fonte primária (Planalto, STF, STJ, JusBrasil). Afirmações de regra geradas por IA às vezes erram elementos ou confundem entendimentos.
```

### Rastrear padrões

Mantenha uma contagem corrente: quais matérias, quais subtópicos, quais pegadinhas de alternativa. Depois de uma sessão:

> "Você errou 3 de 5 questões de Penal, todas em concurso de crimes. Isso é padrão. Vamos sabatinar concurso de crimes especificamente."

## Modo 2ª fase

### Gerar um enunciado

Formato de peça prático-profissional para a área escolhida:

- **Civil:** petição inicial, contestação, recurso (apelação, agravo).
- **Penal:** habeas corpus, resposta à acusação, recurso em sentido estrito, apelação criminal.
- **Trabalho:** reclamação trabalhista, contestação, recurso ordinário.
- **Tributário:** mandado de segurança, embargos à execução fiscal, ação anulatória.
- **Administrativo:** mandado de segurança, ação popular, ação de improbidade.
- **Constitucional:** mandado de segurança, ação civil pública, ação direta de inconstitucionalidade (conforme edital).
- **Empresarial:** petição de recuperação judicial, ação de dissolução parcial de sociedade, ação cambial.

Matéria conforme as áreas fracas ou escolha do aluno — **restrita à área escolhida na inscrição para a 2ª fase**.

### Corrigir

Depois que o aluno escrever:

- Identificação de teses: o que ele identificou, o que deixou passar
- Fundamentação legal: precisa, completa? Artigos corretos citados?
- Análise: aplicou a lei aos fatos, ou só listou lei e fatos separadamente?
- Estrutura formal: endereçamento, qualificação das partes, pedidos, requerimentos — todos presentes e na ordem certa da peça?

Correção de 2ª fase é sobre competência técnica e estrutura formal, não brilhantismo. Uma peça completa, bem estruturada e tecnicamente correta passa. Uma peça brilhante mas incompleta ou com erro de estrutura, não.

```markdown
## Feedback da peça

**Teses identificadas:** [X] de [Y]
**Deixou passar:** [lista — pontos perdidos]

**Fundamentação legal:** [Precisa / próxima / errada — para cada tese]

**Estrutura formal:** [Completa / faltando elemento — endereçamento, qualificação, pedidos, valor da causa, etc.]

**Análise:** [Aplicou de fato, ou só listou lei + fatos?]

**Se isso fosse corrigido pela banca:** [Aprovaria / limítrofe / não ainda — com o que ajustar]
```

## Integração com cronograma

Se o aluno tem um cronograma de estudo: pondere questões para o que está agendado nesta semana. Material recente é sabatinado.

## O que esta habilidade não faz

- Substituir um cursinho. Damásio/CERS/Gran Cursos/Ênfase têm o currículo completo. Isso é reforço complementar.
- Prever a prova. Ninguém pode. Estude tudo.
- Passar na Ordem por você. Obviamente.
- **Afirmar regras sem confiança sem sinalizar.** Se não tenho certeza da regra, você verá `[INCERTO]` ou `[VERIFICAR]` — confira a regra citada contra seu cursinho antes de confiar na questão. Uma regra errada afirmada com confiança é uma sessão de estudo pior do que uma que eu pulo.
