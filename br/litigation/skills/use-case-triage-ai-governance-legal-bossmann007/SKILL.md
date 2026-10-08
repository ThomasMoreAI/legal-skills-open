---
name: use-case-triage-ai-governance-legal-bossmann007
title: /use-case-triage
description: Classifica um caso de uso de IA proposto contra o registro — aprovado, condicional, ou não aprovado — e produz condições e próximos passos exigidos. Sinaliza handoffs entre plugins para privacidade ou product counsel. Use quando o usuário disser "triagem desse caso de uso", "podemos usar IA para X", "isso é aprovado", "o que precisamos fazer para usar IA para X".
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/ai-governance-legal/skills/use-case-triage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# /use-case-triage

1. Ler `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. Confirmar que o registro está preenchido — se não, parar e direcionar para setup.
2. Usar o framework abaixo. Esclarecer o caso de uso se vago.
3. Busca no registro → checagem de linha vermelha → classificar.
4. Output: classificação, raciocínio, tabela de condições (se condicional), nível de governança, handoffs entre plugins.
5. Propor atualização do registro se o caso de uso não estava nele.

```
/ai-governance-legal:use-case-triage "Time de vendas quer pontuar leads com IA automaticamente"
```

---

## Contexto de matéria

**Contexto de matéria.** Verificar `## Matter workspaces` no CLAUDE.md de prática. Se `Enabled` for `✗` (padrão para usuários in-house), pular o resto deste parágrafo — skills usam contexto de nível de prática e a máquina de matters é invisível. Se habilitado e não há matter ativo, perguntar: "Para qual matter é isso? Rode `/ai-governance-legal:matter-workspace switch <slug>` ou diga `practice-level`." Carregar o `matter.md` do matter ativo para contexto e overrides específicos. Escrever outputs na pasta do matter em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/matters/<matter-slug>/`. Nunca ler arquivos de outro matter a menos que `Cross-matter context` esteja `on`.

---

## Propósito

Parar a conversa de corredor que começa como "a gente pode simplesmente usar IA
para isso?" Dar uma resposta rápida e calibrada a partir do registro — e se a
resposta é condicional, tornar as condições concretas e o próximo passo óbvio.

A skill de triagem é um portal, não um destino. Sua função é classificar,
sinalizar o que é exigido, e rotear. A skill aia-generation faz o trabalho
profundo.

## Ler `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` primeiro

Antes de triar, sempre ler `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. O registro de casos de uso e as linhas vermelhas ali
são autoritativos. Raciocínio genérico de ética de IA não substitui o que essa
empresa de fato decidiu.

Se `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` contém `[PLACEHOLDER]`, sinalizar este desvio:

> Percebi que você ainda não configurou seu perfil de prática — é isso que
> personaliza o registro de casos de uso, linhas vermelhas, e níveis de
> governança para sua prática.
>
> **Duas opções:**
> - Rode `/ai-governance-legal:cold-start-interview` (2 minutos) para configurar
>   seu perfil, e então eu triarei calibrado para SUA prática.
> - Diga **"provisório"** e eu triarei contra padrões genéricos — jurisdição
>   brasileira nacional (LGPD como piso), apetite de risco médio, role advogado,
>   sem playbook — e marcarei todo output `[PROVISÓRIO — configure seu perfil
>   para output calibrado]` para você ver o que eu faço antes de se comprometer.

### Modo provisório

Se o usuário disser "provisório", rodar triagem normalmente usando estes padrões
genéricos: apetite de risco médio, role advogado, jurisdição Brasil (LGPD
nacional), sem registro (classificar por princípios gerais de governança de IA em
vez de comparar com entrada registrada). Marcar a nota de revisor e cada bloco de
achado com `[PROVISÓRIO]`. Ao fim do output, adicionar:

> "Essa foi uma rodada genérica contra suposições padrão. Rode
> `/ai-governance-legal:cold-start-interview` para output calibrado para SUA
> prática — seu registro, sua jurisdição, seu apetite de risco. 2 minutos."

**Escopo jurisdicional.** A triagem aplica o registro, linhas vermelhas, e níveis
de governança configurados para o escopo regulatório em
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. Regras
de IA variam materialmente por jurisdição — uma classificação APROVADO em um
escopo pode ser CONDICIONAL ou proibida em outro (ex.: setor financeiro sob Res.
CMN/BCB 4.658, saúde sob RDC Anvisa 657/2022). Se a implantação toca uma
jurisdição fora do escopo, sinalizar isso e retriar em vez de estender por
analogia.

---

## Processo de triagem

### Passo 1: Entender o caso de uso

Antes de classificar, garantir que se entende o que de fato está sendo proposto.
Se a descrição é vaga, perguntar:

- "O que a IA está fazendo, exatamente — gerando conteúdo, tomando decisão,
  mostrando recomendações, automatizando tarefa?"
- "Sobre quem ou o quê a IA age — empregados, clientes, terceiros, apenas dado
  interno?"
- "Um humano revisa o output da IA antes de qualquer coisa acontecer, ou é
  automatizado?"
- "Qual fornecedor ou ferramenta está sendo proposto?"
- "Isso é só interno, ou toca clientes ou outras partes externas?"

Não deixar "queremos usar IA para [coisa vaga]" sem triagem. Ficar específico o
bastante para classificar com precisão.

---

### Passo 2: Busca no registro

Verificar o registro de casos de uso em
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` para
correspondência direta ou próxima.

**Correspondência direta:** Se o registro tem entrada diretamente correspondente,
aplicar.

**Correspondência próxima:** Se o caso de uso é similar a uma entrada do registro
mas não idêntico, sinalizar: "Isso se parece com [caso de uso registrado] — estou
aplicando essa classificação, mas se o escopo é significativamente diferente, pode
precisar de avaliação própria."

**Sem correspondência:** Se o caso de uso não está no registro, default para
CONDICIONAL pendente de avaliação de impacto de IA. Sinalizar a leitura
preliminar de risco e rotear para a AIA.

> "Esse caso de uso ainda não está no seu registro. Default para CONDICIONAL
> pendente de avaliação de impacto (AIA). Aqui vai minha leitura preliminar de
> risco: [leitura preliminar]. Próximo passo: rodar a avaliação de impacto, e eu
> adiciono o caso de uso ao registro assim que a classificação estiver assentada."

---

### Atribuição de fonte (aplica sempre que a triagem citar regulação)

A triagem geralmente fica em alto nível, mas se a classificação depende de citar
lei, resolução, norma, ou guia — marcar a citação. Não emitir citações
regulatórias sem tag no raciocínio da triagem, na explicação de linha vermelha,
ou na lista de condições. Uma triagem que cita um gatilho de revisão automatizada sem tag é exatamente
onde uma citação pinpoint fabricada passa despercebida pelo leitor.

**Tiering de atribuição de fonte.** Para citações de conhecimento do modelo, usar
um dos três níveis:

- `[consolidado]` — referências estatutárias/regulatórias estáveis e bem
  conhecidas com baixa chance de mudança (ex.: LGPD Art. 20 como conceito,
  existência do PL 2338/2023 como projeto em tramitação). Ainda verificar antes
  de certificar, mas prioridade menor.
- `[verificar]` — citações de conhecimento do modelo reais mas que devem ser
  verificadas: resoluções específicas de BCB/CMN, guias da ANPD, normas
  técnicas, datas de vigência, thresholds, alterações pós-2023.
- `[verificar-pinpoint]` — citações pinpoint (número de artigo específico,
  referência de anexo, letra de subseção, número de parágrafo) carregam o maior
  risco de fabricação e devem SEMPRE ser verificadas contra fonte primária.
  Números de artigo do PL 2338/2023 em particular mudam a cada substitutivo —
  verificar toda citação pinpoint contra o texto mais recente tramitando.

Outras fontes mantêm suas próprias tags: `[registro]` quando extraído do registro
de casos de uso do perfil de prática; `[ANPD]`, `[Planalto]`, `[site do
regulador]`, ou o nome da ferramenta MCP quando recuperado de ferramenta de
pesquisa jurídica conectada; `[busca web — verificar]` para citações de busca
web; `[fornecido pelo usuário]` para citações fornecidas pelo usuário. Nunca
remover ou colapsar as tags.

**Para usuários não-advogados, datas e thresholds incertos vão em lista de
confirmação, não inline.** Uma tag `[verificar]` em "vigente a partir de 1º de
fevereiro de 2026" lê como fato para quem não sabe o que a tag significa. Ler
`## Who's using this` em
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. Se
Role é **Não-advogado** e uma data de vigência, prazo, ou threshold é incerto
(carregaria `[verificar]` ou `[verificar-pinpoint]` inline), substituir a
afirmação inline por "data de vigência: confirmar com advogado(a)" e coletar
todos os itens incertos numa seção final de triagem titulada: "**Coisas que não
tenho certeza — peça para seu advogado(a) confirmar antes de confiar nisto:**"
com cada item listado (o que eu disse, do que não tenho certeza, por que
importa). Usuários com role Advogado mantêm o tratamento `[verificar]` inline.

---

### Passo 3: Checagem de linha vermelha

Antes de prosseguir, verificar as linhas vermelhas em
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`.

Se o caso de uso aciona uma linha vermelha — mesmo parcialmente, mesmo numa
leitura generosa — dizer isso imediatamente.

> "Esse caso de uso toca [linha vermelha]. Suas linhas vermelhas tratam isso como
> um não automático. Se há algo diferente nessa situação, isso é conversa para
> aprovação jurídica formal — não decisão de triagem."

Não suavizar resultados de linha vermelha. Se é não, é não.

---

**Escopo jurisdicional.** Perguntar: "Quem é afetado, e onde estão? (Empregados /
clientes / público geral / grupos específicos.) Quais jurisdições? (Não só onde
sua empresa está — onde as pessoas afetadas estão, incluindo se há transferência
internacional de dados.)"

Depois verificar o caso de uso contra TODO regime no `## Regulatory footprint` do
perfil de prática, não só o principal. Sinalizar conflitos:
- "APROVADO sob LGPD isoladamente, mas dispara Res. CMN/BCB 4.658 se envolve
  scoring de crédito — confirmar se instituição financeira está no escopo."
- "Nível padrão sob seu framework de governança, mas RDC Anvisa 657/2022 exige
  classe de risco SaMD se usado em diagnóstico ou triagem clínica."
- "Baixo risco sob PL 2338/2023 como redigido hoje, mas pode virar alto risco se
  o substitutivo em tramitação classificar essa categoria como tal — reavaliar
  quando o texto avançar."

Um caso de uso que cruza jurisdições recebe o tratamento mais estrito aplicável,
não o mais conveniente.

---

### Passo 4: Classificação e output

Os buckets APROVADO / CONDICIONAL / NÃO APROVADO, as definições de linha
vermelha, e a lista de controles exigidos para CONDICIONAL vêm todos de
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` →
`## AI use case triage criteria` e `## Use case registry`. Se o playbook não
define um critério que o caso de uso aciona, perguntar ao usuário: "Seu playbook
não cobre [pergunta específica]. Qual sua posição padrão? Vou adicionar em
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` para a
próxima triagem ser consistente."

**Antes de emitir classificação APROVADO (aprovando um caso de uso de IA para
implantação):** Ler `## Who's using this` em
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. Se o
Role é Não-advogado:

> Aprovar esse caso de uso para implantação tem consequências jurídicas. Você
> revisou isso com advogado(a)? Se sim, prosseguir. Se não, aqui vai um resumo
> para levar a ele(a):
>
> [Gerar resumo de 1 página: o caso de uso e seu escopo, como se encaixa no
> registro, quais políticas ou linhas vermelhas toca, o que pode dar errado na
> implantação, o que perguntar ao(à) advogado(a) antes de aprovar.]
>
> Se precisar encontrar advogado(a): o serviço de indicação da OAB da sua
> seccional é o ponto de partida mais rápido.

Não prosseguir além desse gate sem um sim explícito. Outputs CONDICIONAL não
exigem o gate.

**Antes de emitir classificação NÃO APROVADO que corta um caso de uso proposto:**
Ler `## Who's using this` em
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. Se o
Role é Não-advogado, um gate simétrico se aplica — rejeitar erradamente um caso de
uso também é erro consequente, e o negócio vai contestar de qualquer forma:

> Isso é uma parada total para um pedido de negócio. Você revisou isso com
> advogado(a)? Se sim, prosseguir. Se não, aqui vai um resumo para levar a ele(a):
>
> [Gerar resumo de 1 página: o caso de uso e seu escopo, a linha vermelha ou
> entrada de registro específica que bloqueia, como seria uma versão mais
> restrita que poderia passar no nível elevado (se houver), o que o negócio
> provavelmente vai pedir ao(à) advogado(a), e as três perguntas a fazer antes
> de aceitar o não.]
>
> Se precisar encontrar advogado(a): o serviço de indicação da OAB da sua
> seccional é o ponto de partida mais rápido.

Não prosseguir além desse gate sem um sim explícito. Um não-advogado emitindo um
não definitivo em nome do plugin de IA, sem advogado(a) no loop, é o espelho da
falha de um não-advogado emitindo um sim definitivo.

**Formato para cada output de triagem:**

---

[CABEÇALHO DE PRODUTO DE TRABALHO — conforme config do plugin ## Outputs — difere
por role; ver `## Who's using this`]

**CASO DE USO:** [Descreva o caso de uso como você o entende]

**CLASSIFICAÇÃO:** [APROVADO / CONDICIONAL / NÃO APROVADO]

**Correspondência no registro:** [Direta / Próxima — [nome] / Nenhuma]

**Raciocínio:**
[1-3 frases sobre por que essa classificação. Se aprovado, o que torna seguro. Se
condicional, o que cria o risco que as condições gerenciam. Se não aprovado, qual
linha vermelha ou posição de política se aplica.]

**Linhas vermelhas acionadas:** [Nenhuma / Listar as que se aplicam]

---

*Se CONDICIONAL — exigido antes de prosseguir:*

| Requisito | Dono | Feito? |
|---|---|---|
| [ex.: Avaliação de impacto de IA (AIA)] | [AI governance counsel] | ☐ |
| [ex.: Revisão de privacidade / RIPD] | [Privacy counsel] | ☐ |
| [ex.: Requisito de humano no loop — sem decisão automatizada] | [Produto] | ☐ |
| [ex.: Divulgação às partes afetadas] | [Produto / Jurídico] | ☐ |
| [ex.: Apenas fornecedor específico — [nome do fornecedor aprovado]] | [Procurement] | ☐ |
| [ex.: Aprovação jurídica formal] | [GC] | ☐ |

**Nível de governança:** [Padrão / Elevado / Alto — per
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`]

**Caminho de aprovação:** [Quem precisa assinar, por nível]

**Próximo passo — oferecer continuar:**

Depois de apresentar resultado CONDICIONAL, sempre terminar com:

> "Quer que eu comece a avaliação de impacto agora? Posso rodar as perguntas de
> intake e produzir o documento de avaliação sem você precisar rodar comando
> separado."

Se disserem sim, carregar a skill `aia-generation` e continuar na mesma
conversa — sem precisar reiniciar. Passar a descrição do caso de uso e o nível
de governança já determinado.

Se disserem não (ou não responderem), o resultado da triagem fica como output
independente. A AIA pode rodar a qualquer momento com:
`/ai-governance-legal:aia-generation [caso de uso]`

---

*Se NÃO APROVADO:*

**Motivo:** [Linha vermelha específica, proibição de política, ou entrada do
registro]

**Se há uma versão disso que poderia funcionar:** [Opcional — "Uma versão mais
restrita que mantém humano no loop para toda decisão adversa pode passar no
nível elevado. Isso exigiria..."] Só incluir se genuinamente verdadeiro. Não
oferecer alternativa para todo não.

---

### Passo 5: Handoffs entre plugins

**Handoff de privacidade:** Se o caso de uso envolve dado pessoal — dado de
empregado, dado de cliente, dado comportamental — sinalizar:

> "Esse caso de uso envolve dado pessoal. Uma RIPD é provavelmente exigida além
> da avaliação de impacto de IA. Use `/privacy-legal:pia-generation [caso de
> uso]`, se o plugin estiver instalado, para rodar em paralelo."

**Handoff de product counsel:** Se isso é nova funcionalidade de produto
envolvendo IA:

> "Se esse caso de uso é parte de um lançamento de produto, envolva product
> counsel. Use `/product-legal:launch-review`, se o plugin estiver instalado —
> ele vai detectar o componente de IA e rotear para este plugin."

Só sinalizar handoffs realmente relevantes. Não anexar os dois como boilerplate
em toda triagem.

---

### Passo 6: Sugestão de atualização do registro

Se essa triagem resultou em classificação que ainda não está no registro — seja
sem correspondência ou correspondência próxima que revelou uma lacuna:

> "Sugiro adicionar isso ao seu registro de casos de uso. Entrada proposta:"

```
| [Descrição do caso de uso] | [Aprovado/Condicional/Nunca] | [Condições se houver] | [Motivo se Nunca] |
```

> "Adicionar em
> `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` →
> Registro de casos de uso. Isso significa que na próxima vez que o mesmo pedido
> surgir, a resposta está documentada e consistente."

---

## Triagem em lote

Se o usuário apresenta múltiplos casos de uso de uma vez — uma lista, um
backlog, um roadmap de produto — passar por cada um e mostrar tabela resumo
primeiro, depois expandir cada entrada condicional ou não aprovada:

| # | Caso de uso | Classificação | Condição-chave / bloqueio |
|---|---|---|---|
| 1 | [caso de uso] | 🟢 Aprovado | — |
| 2 | [caso de uso] | 🟡 Condicional | Avaliação de impacto exigida |
| 3 | [caso de uso] | 🔴 Não aprovado | Decisão adversa automatizada — linha vermelha |

Depois expandir cada linha que não é um aprovado limpo.

---

## Casos-limite e modos de falha

**Triagem "já estamos fazendo isso":**
Se alguém pede triagem retroativa — o caso de uso já está implantado — dizer isso
claramente, e antes de classificar do zero, buscar no registro entrada existente
cobrindo a versão implantada. Triagens retroativas frequentemente revelam entrada
de registro superada cujas condições derivaram da prática atual; atualizar essa
entrada geralmente é o follow-up certo em vez de adicionar nova linha.
> "Isso parece triagem retroativa. Se já está rodando sem avaliação, isso é
> lacuna a documentar, não a deixar passar. Estou buscando no registro entrada
> existente cobrindo essa implantação antes de rodar a triagem do zero. Aqui vai
> a classificação: [rodar triagem normal]. Se é condicional, essas condições
> devem ser confirmadas em vigor agora, não presumidas. Se o registro tem
> entrada existente e a versão implantada derivou, o follow-up certo é atualizar
> essa entrada em vez de adicionar uma nova."

**"É só interno" não muda a análise:**
Uso interno de IA afetando empregados (triagem, monitoramento, avaliação) é
frequentemente mais arriscado que IA voltada a cliente — CLT + LGPD tratam dado
de empregado como dado pessoal protegido. Sinalizar se o usuário implica que
escopo interno reduz risco.

**"O fornecedor diz que é seguro":**
Representações de fornecedor não substituem sua própria avaliação de impacto.
Sinalizar:
> "A posição do fornecedor não substitui sua própria avaliação — especialmente
> para qualquer coisa no nível elevado ou alto."

**"Estamos só pilotando":**
Um piloto que toca dado real de empregado ou cliente não é isento de triagem ou
avaliação de impacto. Aplicar a mesma classificação; se condições incluem
avaliação de impacto, o piloto deve ter uma também.

## Fechar com a árvore de decisão de próximos passos

Terminar com a árvore de decisão de próximos passos conforme CLAUDE.md
`## Outputs`. Customizar as opções para o que essa skill acabou de produzir — os
cinco ramos padrão (rascunhar o X, escalar, buscar mais fatos, aguardar e
observar, outra coisa) são ponto de partida, não travamento. A árvore é o
output; o(a) advogado(a) escolhe.
