---
name: aia-generation-bossmann007
title: /aia-generation
description: Roda uma avaliação de impacto de sistema de IA (AIA) — intake estruturado, análise de risco, classificação regulatória por regime aplicável (LGPD Art. 20, PL 2338/2023, regulação setorial BCB/Anvisa/CVM), diff de consistência com a política e recomendação com condições. Usa a estrutura house-style aprendida da avaliação-semente em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. Use quando o usuário disser "avaliação de impacto para", "avalia esse caso de uso de IA", "roda uma AIA", "gera uma AIA", "precisamos documentar esse sistema de IA", "avaliação de risco de IA para X", ou após um resultado condicional de triagem.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/ai-governance-legal/skills/aia-generation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# /aia-generation

1. Ler `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. Confirmar que o house style de avaliação de impacto está preenchido.
2. Determinar trilha de risco (rápida ou completa) a partir do nível de governança e das características do caso de uso, usando o framework abaixo.
3. Rodar intake — conversacional, não formulário.
4. Classificação regulatória para cada regime no escopo — nível de risco, exposição a prática proibida, e obrigações aplicáveis; citar fontes primárias.
5. Escrever avaliação no house style (da avaliação-semente, ou padrão se nenhuma foi capturada).
6. Diff de política contra os compromissos de IA em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`.
7. Output: documento de avaliação + lista de condições + flags de handoff (RIPD de privacidade, revisão de fornecedor se necessário).

```
/ai-governance-legal:aia-generation "Triagem de currículo por IA para RH"
```

---

## Contexto de matéria

**Contexto de matéria.** Verificar `## Matter workspaces` no CLAUDE.md de prática. Se `Enabled` for `✗` (padrão para usuários in-house), pular o resto deste parágrafo — skills usam contexto de nível de prática e a máquina de matters é invisível. Se habilitado e não há matter ativo, perguntar: "Para qual matter é isso? Rode `/ai-governance-legal:matter-workspace switch <slug>` ou diga `practice-level`." Carregar o `matter.md` do matter ativo para contexto e overrides específicos. Escrever outputs na pasta do matter em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/matters/<matter-slug>/`. Nunca ler arquivos de outro matter a menos que `Cross-matter context` esteja `on`.

---

## Propósito

Uma AIA (avaliação de impacto de sistema de IA) é uma decisão documentada, não um
formulário. Responde: o que esse sistema de IA faz, como chega às suas saídas, quem
é afetado se errar, qual a supervisão, e se está OK implantar. Essa skill estrutura
essa conversa e escreve o output no formato deste time — o aprendido da
avaliação-semente durante o cold-start.

Uma AIA não é o mesmo que uma RIPD (Relatório de Impacto à Proteção de Dados
Pessoais, LGPD Art. 38). A RIPD descreve os tipos de dados coletados, a metodologia de coleta e de segurança, e a análise das medidas de mitigação de risco; a ANPD pode determinar ao controlador que a elabore. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm] A
AIA pergunta se o sistema de IA é projetado e implantado de forma responsável.
Frequentemente precisam rodar em paralelo; não são substitutas uma da outra. Se o
sistema envolve dado pessoal, a RIPD é obrigatória sob a LGPD **independentemente**
do destino do PL 2338/2023 — trate a RIPD como piso mínimo, não como bônus.

## Carregar house style

Ler `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` → `## Impact assessment house style`. Isso tem:
- O que dispara uma avaliação de impacto nesta empresa
- O template de estrutura extraído da avaliação-semente
- Profundidade típica
- Quem assina

Se a estrutura-semente está em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`, **use-a**. O objetivo é que essa avaliação
se pareça com as outras avaliações que esse time produz.

**Escopo jurisdicional.** Esta avaliação aplica os regimes regulatórios listados em `## Regulatory footprint` em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` — tipicamente LGPD (nacional, sempre aplicável quando há dado pessoal), PL 2338/2023 (se/quando sancionado — status legislativo instável), e regulação setorial (Res. CMN/BCB 4.658 para instituições financeiras, RDC Anvisa 657/2022 para SaMD, regras CVM para robo-advisors). Se este sistema é (ou será) implantado fora desse escopo — por exemplo, com transferência internacional de dados ou operação em outro país — ou há questão de conflito de leis em jogo, esta análise pode não se aplicar como está — re-rodar ou expandir o escopo.

---

## Passo 0: Uma avaliação de impacto é necessária?

Verificar os critérios de gatilho em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`.

**Verificar também isso, independentemente:**
- Essa IA toma ou influencia materialmente uma decisão que afeta uma pessoa
  (emprego, crédito, acesso, precificação, moderação de conteúdo)?
- Essa IA trata dado pessoal sobre indivíduos? (Se sim → LGPD Art. 20 se aplica
  independentemente do PL 2338/2023.)
- É um sistema de IA voltado a cliente, não puramente interno?
- Essa IA usa modelo de terceiro onde a empresa é operadora/implementadora?
- O caso de uso está no nível de governança elevado ou alto por `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`?

Se nenhum dos itens acima e o gatilho da casa não é atendido:
> "Não parece que isso precise de uma AIA completa. Aqui vai um registro de um
> parágrafo pro arquivo explicando por quê — caso alguém pergunte depois."

---

## Passo 1: Trilha de risco

Antes do intake, determinar qual trilha rodar. As definições de nível e os critérios de trilha rápida vêm de `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` (`## Use case registry` e `## Governance tiers`), não de um framework hardcoded de um regime específico.

Pesquisar o framework de classificação de risco aplicável para cada regime no escopo regulatório do usuário:
- **LGPD Art. 20** — direito à revisão de decisões tomadas **unicamente** com base em tratamento automatizado de dados pessoais que afetem os interesses do titular (incluídas as destinadas a definir perfil pessoal, profissional, de consumo e de crédito). O requisito legal é que a decisão seja tomada *unicamente* de forma automatizada — não basta ser "automatizada". [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm]
- **PL 2338/2023** — propõe taxonomia de risco (excessivo/proibido, alto risco, risco geral), similar em espírito ao AI Act europeu mas com texto ainda em tramitação. `[verificar status atual — pode ter sido sancionado, alterado, ou ainda pendente de votação]`.
- **Setorial** — Res. CMN/BCB 4.658 trata gestão de risco em instituições financeiras (inclui scoring de crédito por IA); RDC Anvisa 657/2022 classifica SaMD por classe de risco; CVM tem regras específicas para robo-advisors.

Não presumir que sistema só-interno está fora de escopo — LGPD trata dado de
empregado como dado pessoal, e monitoramento de empregado é consequencial. Verificar
a regra específica (CLT + LGPD).

> **Sem suplementação silenciosa.** Se uma consulta à ferramenta de pesquisa jurídica configurada (site do Planalto, ANPD, BCB, Anvisa, CVM, ou plataforma do escritório) retornar poucos ou nenhum resultado para os níveis de risco ou gatilhos de um regime, reportar o que foi encontrado e parar. NÃO preencher a lacuna com busca web ou conhecimento do modelo sem perguntar. Dizer: "A busca retornou [N] resultados de [ferramenta]. Cobertura parece rasa para [regime/tópico]. Opções: (1) ampliar a query, (2) tentar outra ferramenta de pesquisa, (3) buscar na web — resultados serão marcados `[busca web — verificar]` e devem ser checados contra a autoridade emissora antes de confiar, ou (4) marcar como não verificado e parar. Qual você prefere?" O advogado decide se aceita fontes de confiança mais baixa.
>
> **Tiering de atribuição de fonte.** Marcar toda citação na AIA — texto regulatório, resolução, guia, norma técnica — com sua fonte. Para citações de conhecimento do modelo, usar um dos três níveis:
>
> - `[consolidado]` — referências estatutárias/regulatórias estáveis e bem conhecidas, com baixa chance de mudança (ex.: LGPD Art. 20 como conceito, existência da Lei 8.906/1994). Ainda verificar antes de certificar, mas prioridade menor.
> - `[verificar]` — citações de conhecimento do modelo reais mas que devem ser verificadas: resoluções específicas de BCB/CMN, guias da ANPD, dispositivos do PL 2338/2023, normas ABNT, e qualquer coisa pós-2023.
> - `[verificar-pinpoint]` — citações pinpoint (número de artigo específico, referência de anexo, subseção) carregam o maior risco de fabricação e devem SEMPRE ser verificadas contra fonte primária. Números de artigo do PL 2338/2023 em particular mudam a cada substitutivo — verificar toda citação pinpoint contra o texto mais recente tramitando na Câmara/Senado.
>
> Citações vindas de ferramenta mantêm sua tag de fonte (`[ANPD]`, `[Planalto]`, `[site do regulador]`, ou o nome da ferramenta MCP); citações de busca web permanecem `[busca web — verificar]`; citações fornecidas pelo usuário permanecem `[fornecido pelo usuário]`. Nunca remover ou colapsar as tags.
>
> **Para usuários não-advogados, datas incertas vão em lista de confirmação, não inline.** Ler `## Who's using this` em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. Se Role é **Não-advogado** e uma data, prazo, ou threshold é incerto (carregaria `[verificar]` ou `[verificar-pinpoint]` inline), substituir a afirmação inline por "data de vigência: confirmar com advogado(a)" e coletar todos os itens incertos numa seção final da AIA titulada:
>
> > **Coisas que não tenho certeza — peça para seu advogado(a) confirmar antes de confiar nisto:**
>
> Listar cada item incerto com (1) o que eu disse, (2) do que não tenho certeza, (3) por que importa para a avaliação. Usuários com role Advogado recebem o tratamento `[verificar]` inline — eles sabem o que a tag significa.

**Trilha rápida vs. avaliação completa:** `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` define o que qualifica para tratamento abreviado. Se não define critérios de trilha rápida, default para avaliação completa e perguntar ao usuário quais critérios ele quer capturar para a próxima vez.

Na dúvida, rodar a avaliação completa. Uma trilha rápida que se prova errada é
pior que uma avaliação completa em algo de baixo risco.

---

## Passo 2: Intake

Antes de escrever qualquer coisa, obter respostas para isso. Conversacional está
bom — isso não é formulário para enviar.

### O sistema

- O que a IA faz? Descrever em linguagem simples, não copy de marketing.
- Qual modelo ou fornecedor potencializa isso? Fine-tuned ou pronto de fábrica?
- Onde fica no fluxo de trabalho — é assistiva (humano revisa output), aumentativa
  (humano pode sobrepor mas geralmente não faz), ou automatizada (sem humano no
  loop)?
- Qual é o output — texto gerado, uma pontuação, uma classificação, uma
  recomendação, uma ação?

### Quem é afetado

- Sobre quem age o output da IA — empregados, clientes, terceiros?
- Se a IA produz um erro (falso positivo, falso negativo, alucinação), quem sofre
  o dano e qual o pior caso realista?
- Algum grupo vulnerável está desproporcionalmente no escopo — menores, candidatos
  a emprego, pessoas em dificuldade financeira, pacientes?

### Entradas e dados

- Que dado a IA recebe?
- Recebe dado pessoal? De quem?
- O modelo foi treinado com dado desta empresa, ou é modelo de fundação sem
  treino específico da empresa?
- Para onde vai o dado de entrada — sai do perímetro para API de modelo de
  terceiro?

### Decisões e supervisão

- O output da IA dispara uma ação automaticamente, ou um humano decide o que
  fazer com o output?
- Se há revisão humana: com que frequência o humano de fato muda o output da IA?
  (Se a resposta é "raramente" — o humano não está revisando de verdade; está
  carimbando.)
- Há processo de recurso ou correção para pessoas afetadas pelos outputs da IA?
  (LGPD Art. 20 garante isso quando a decisão é tomada unicamente com base em tratamento automatizado e afeta interesses do titular.) [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm]
- Quem é responsável pelos outputs do sistema de IA — há um dono nomeado?

### Acurácia e falha

- Qual a taxa de erro conhecida ou estimada? Que teste foi feito?
- O que acontece quando a IA erra — o erro é exposto, logado, corrigido?
- Foi feito teste de viés? Contra quais grupos demográficos?

### Estágio de implantação e escala

Perguntar:
- **Estágio:** "Esse sistema está (a) proposto e ainda não construído, (b) em piloto,
  (c) vivo em produção, ou (d) vivo e escalado?"
- **Escala:** "Aproximadamente quantos indivíduos são afetados por [mês/ano]? Há
  quanto tempo está rodando?"
- **Histórico:** "Já foi avaliado antes? Já produziu decisões contestadas,
  recorridas, ou revertidas?"

Estágio muda a avaliação: sistema proposto recebe revisão de design (dá pra
construir com segurança?). Piloto recebe revisão de design mais um gate "antes de
escalar". Sistema vivo recebe checagem retrospectiva de impacto (já causou dano?)
E revisão prospectiva. Sistema vivo e escalado recebe tudo isso mais um plano de
remediação se problemas forem achados, porque não dá simplesmente para desligar.

---

## Passo 3: Classificação regulatória

**Pré-checagem do Passo 3 — atualidade do escopo.** Antes de iterar sobre o `## Regulatory footprint` capturado, comparar a população afetada e o tipo de decisão do caso de uso (do Passo 2) contra o escopo como está escrito. O escopo foi definido no cold-start, com base na postura operacional da empresa naquele momento. Se o caso de uso introduz uma população afetada (ex.: menores, empregados em novo estado, titulares de dados fora do Brasil) ou um tipo de decisão (ex.: contratação, crédito, diagnóstico de saúde, infraestrutura crítica) que o escopo não contempla, **re-derivar os regimes aplicáveis em vez de iterar sobre a lista desatualizada.**

Dizer ao usuário:

> "O escopo regulatório do perfil de prática foi definido para [populações afetadas / tipos de decisão capturados no cold-start]. Esse caso de uso afeta **[nova população ou tipo de decisão — ex.: empregados, menores, decisão de crédito, identificação biométrica]**, que não está no escopo capturado. Vou re-derivar os regimes aplicáveis a partir das jurisdições operacionais da empresa e do tipo de decisão deste caso de uso, em vez de usar o escopo desatualizado. Se este caso de uso é representativo de trabalho que você espera ver mais, atualize `## Regulatory footprint` ao fim desta rodada para a próxima AIA não precisar re-derivar."

Um erro comum: o escopo lista LGPD + PL 2338/2023, e o caso de uso é um sistema de
contratação com componente biométrico (reconhecimento facial em entrevista). O
escopo não tem entrada para dado biométrico, então iterar sobre ele silenciosamente
perde a qualificação de dado biométrico como dado sensível (LGPD Art. 5º, II) com
regras de tratamento mais rígidas, e possível sobreposição com CLT sobre
monitoramento de empregado.

Um segundo erro: o escopo foi definido antes de um regime que agora importa existir
ou entrar em vigor (ex.: PL 2338/2023 sancionado após o cold-start). Se a
re-derivação revela um regime fora do escopo, sinalizar na seção de recomendação
do output, citar a autoridade, e recomendar atualizar o escopo.

Para cada regime em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` → `## Regulatory footprint` que se aplica a esse sistema — **mais qualquer regime revelado pela re-derivação acima** — pesquisar o framework de classificação de risco atualmente vigente e determinar onde o sistema se enquadra.

Tarefas de pesquisa:
- Qual a taxonomia de nível do próprio regime (ex.: excessivo/proibido, alto risco,
  risco geral para PL 2338/2023; decisão automatizada para LGPD Art. 20; classe de
  risco para RDC Anvisa)?
- Quais os critérios de cada nível? Citar fontes primárias com referência pinpoint.
- Em qual nível esse sistema se enquadra dada sua função, partes afetadas, e
  consequencialidade da decisão?
- Há práticas proibidas que o sistema possa tocar (ex.: scoring social, manipulação
  subliminar, exploração de vulnerabilidade)? Tratar qualquer possível
  correspondência como crítica — sinalizar imediatamente.
- Há obrigações de transparência que se aplicam independente do nível (aviso de
  que o usuário interage com IA, rotulagem de conteúdo gerado por IA, notificação
  a pessoas sujeitas a decisão automatizada — LGPD Art. 20 § único)?
- Se a empresa é fornecedora/desenvolvedora de modelo de propósito geral, que
  obrigações de nível-fornecedor se aplicam (documentação técnica, transparência
  de dado de treino, conformidade de direito autoral)?
- **Algum regime no escopo exige avaliação de impacto de direitos fundamentais
  separada?** Verificar se o PL 2338/2023, na versão em tramitação, mantém
  exigência equivalente ao FRIA do AI Act europeu para certos usos de alto risco.
  Se sim, sinalizar como entregável separado na recomendação e condições — não
  tratar esta AIA como substituta.
- **A RIPD (LGPD Art. 38) é exigida em paralelo?** Sempre que há dado pessoal
  envolvido, sim — independente do resultado da classificação de risco de IA.

Não presumir que sistema só-interno está fora de escopo — LGPD trata dado de
empregado como dado pessoal, e monitoramento de empregado é consequencial.
Verificar a regra específica.

**Split fornecedor-vs-operador (quando `AI role: Both`).** Se `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` → `## Company profile` → `AI role` for `Both` (a empresa é fornecedora/desenvolvedora E operadora/implementadora), a Seção 6 DEVE incluir uma tabela de mapeamento fornecedor-vs-operador por regime. A maioria dos regimes impõe obrigações materialmente diferentes para fornecedores versus operadores — colapsar em uma lista única perde obrigações e confunde riscos. Produzir, por regime:

| Obrigação | Como fornecedor | Como operador |
|---|---|---|
| [obrigação específica, citação pinpoint] | [o que se aplica / não se aplica / com que ressalvas] | [o que se aplica / não se aplica / com que ressalvas] |

**Se uma classificação de alto risco (ou equivalente) se aplicar:**
Sinalizar na avaliação, citando o dispositivo e regime específicos. Notar que esta
AIA documenta a revisão interna mas não substitui nenhuma avaliação formal de
conformidade que o regime exija. Recomendar revisão jurídica externa antes de
implantação.

Capturar a classificação e a autoridade citada no output da avaliação.

---

## Passo 4: Escrever a avaliação

**Usar a estrutura-semente de `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`.** Se nenhuma foi capturada, usar este padrão:

```markdown
[CABEÇALHO DE PRODUTO DE TRABALHO — conforme config do plugin ## Outputs — difere por role; ver `## Who's using this`]

# Avaliação de Impacto de IA: [Nome do Sistema/Funcionalidade]

**Preparado por:** [nome] | **Data:** [data] | **Status:** RASCUNHO / APROVADO
**Dono do sistema:** [nome] | **Revisor de governança de IA:** [nome]
**Nível de governança:** [Padrão / Elevado / Alto]
**Trilha:** [Rápida / Avaliação completa]

---

## Resumo executivo

[Duas frases: o que essa IA faz e se está OK implantar. Ex.: "Este sistema usa
LLM de terceiro para redigir respostas iniciais a tickets de suporte antes de
revisão por agente humano. Tratamento consistente com a política de IA da
empresa; três condições exigidas antes de implantação em produção."]

**Risco geral:** 🟢 Baixo / 🟡 Médio / 🟠 Alto / 🔴 Muito alto

---

## 1. Descrição do sistema

**O que faz:** [português simples — não marketing]
**Modelo / fornecedor:** [quem fornece a IA]
**Modo de implantação:** [Assistiva / Aumentativa / Automatizada]
**Tipo de output:** [texto / pontuação / classificação / recomendação / ação]
**Status:** [Não iniciado / Piloto / Produção]

---

## 2. Partes afetadas

**Sobre quem age:** [empregados / clientes / terceiros]
**Escala:** [quantas pessoas, com que frequência]
**Dano se errado:** [pior caso mais realista — específico, não genérico]
**Grupos vulneráveis no escopo:** [sim — [quem] / não]

---

## 3. Entradas de dados

**Categorias de dado usadas:** [campos específicos, não "dado de usuário"]
**Dado pessoal:** [sim — [de quem] / não]
**Dado sensível (LGPD Art. 5º, II)?** [sim — [qual categoria] / não]
**Dado sai do perímetro?** [sim — para [fornecedor] / não]
**Treino do modelo:** [dado da empresa usado / modelo de fundação / fine-tuned em [dataset]]

---

## 4. Tomada de decisão e supervisão

**Humano no loop:** [Sempre / Nominalmente (risco de carimbo) / Não]
**Mecanismo de override:** [como humano pode intervir ou corrigir]
**Recurso / correção para partes afetadas (LGPD Art. 20):** [sim — [como] / não]
**Dono nomeado:** [nome ou cargo]

---

## 5. Acurácia e viés

**Taxa de erro:** [conhecida / estimada / não testada]
**Modo de falha:** [o que acontece quando erra — exposto? logado? corrigido?]
**Teste de viés:** [feito — [resultados] / não feito / não aplicável]

---

## 6. Classificação regulatória

*[Uma subseção por regime no escopo regulatório aplicável a este sistema.]*

**Regime:** [nome — ex.: LGPD, PL 2338/2023, Res. CMN/BCB 4.658, RDC Anvisa 657/2022]
**Classificação sob esse regime:** [nível, com citação pinpoint ao dispositivo controlador]
**Práticas proibidas acionadas:** [nenhuma identificada / [dispositivo específico e por quê]]
**Obrigações aplicáveis:** [lista pesquisada com citações — transparência, documentação, supervisão humana, teste, registro, etc.]
**RIPD (LGPD Art. 38) exigida em paralelo?** [Sim / Não]
**Avaliação de impacto de direitos fundamentais exigida?** [Sim — regime equivalente / Não / Não aplicável. Se sim, entregável separado, não subsumido por esta AIA.]
**Data de vigência / fiscalização:** [data(s)]
**Ambiguidade ou interpretação aberta:** [sinalizar qualquer coisa ainda não assentada]

**Split de obrigação fornecedor-vs-operador (obrigatório se `AI role: Both`):**

| Obrigação | Como fornecedor | Como operador |
|---|---|---|
| [obrigação específica + citação pinpoint] | [o que se aplica / não se aplica] | [o que se aplica / não se aplica] |

---

## 7. Consistência com a política de IA

| Compromisso de política | Consistente? | Notas |
|---|---|---|
| [compromisso da seção de política de IA em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`] | 🟢 / 🟡 / 🟠 / 🔴 | |

[Se algum item é 🟡 ou pior: atualização de política necessária antes da
implantação, ou o design precisa mudar. Um dos dois tem que mudar — não os dois
sinalizados e deixados em aberto.]

---

## 8. Riscos e mitigações

| # | Risco | Probabilidade | Impacto | Mitigação | Status | Dono |
|---|---|---|---|---|---|---|
| 1 | [risco específico atrelado a este design — não "alucinação de IA" genericamente] | B/M/A | B/M/A | [controle específico] | Feito / Planejado / Gap | [nome] |

**Risco residual após mitigações:** [avaliação]

---

## 9. Recomendação

**[APROVADO / APROVADO COM CONDIÇÕES / MUDANÇAS EXIGIDAS / NÃO APROVADO]**

**Condições (se houver):**
- [ ] [ação específica antes da implantação — dono, prazo]

**Revisão de privacidade exigida?** [Sim — rodar `/privacy-legal:pia-generation` (RIPD), se o plugin estiver instalado / Não]

**Assinatura:** [nome, data]

---

## Checagem de citação

Citações regulatórias na Seção 6 (e em qualquer outra) foram geradas por modelo de
IA e não foram verificadas contra fontes primárias. Antes da avaliação ser
certificada ou usada como base, rodar uma verificação contra ferramenta de pesquisa
jurídica (site do Planalto, ANPD, BCB, Anvisa, CVM, ou plataforma do escritório)
para cada dispositivo citado — confirmar pinpoint, vigência, e qualquer resolução
ou instrução normativa complementar. O cenário regulatório de IA no Brasil muda
rápido (PL 2338/2023 ainda em tramitação) — verificar antes de aconselhar. Tags de
fonte em cada citação (ex.: `[ANPD]`, `[busca web — verificar]`) mostram de onde
veio; tags `verificar` carregam risco de fabricação maior e devem ser checadas
primeiro.
```

**Antes de certificar a AIA (o passo de Assinatura, marcando Status: APROVADO):** Ler `## Who's using this` em `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`. Se o Role é Não-advogado:

> Certificar esta AIA tem consequências jurídicas — vira o registro que a empresa
> usa se um regulador (ANPD) ou parte afetada perguntar como esse caso de uso foi
> avaliado. Você revisou isso com advogado(a)? Se sim, prosseguir. Se não, aqui vai
> um resumo para levar a ele(a):
>
> [Gerar resumo de 1 página: o sistema, a classificação regulatória, os riscos
> identificados, as mitigações em vigor, risco residual, questões em aberto, o que
> perguntar ao(à) advogado(a) antes de certificar.]
>
> Se precisar encontrar advogado(a): o serviço de indicação da OAB da sua seccional
> é o ponto de partida mais rápido.

Não prosseguir além desse gate sem um sim explícito. Avaliações RASCUNHO para
revisão de advogado não exigem o gate — a certificação sim.

---

## Padrões de qualidade de risco

Mesmo padrão da skill de RIPD/PIA — riscos devem ser **específicos e atrelados ao
design**.

| Risco ruim | Por que é ruim | Melhor |
|---|---|---|
| "Alucinação de IA" | Se aplica a qualquer LLM; não diz nada | "Modelo pode gerar citações jurídicas plausíveis mas incorretas — agentes de suporte não têm passo de verificação atual antes de enviar ao cliente" |
| "Viés" | Vago demais | "Modelo de scoring de currículo treinado em contratações históricas; se coorte histórica era demograficamente homogênea, candidatos sub-representados podem ser sistematicamente pontuados mais baixo" |
| "Risco de fornecedor" | Circular | "Termos do fornecedor permitem treino com inputs da API por padrão; a menos que o opt-out esteja confirmado no contrato, mensagens de suporte ao cliente podem ser usadas para treinar o modelo" |

Buscar 2-5 riscos reais, não 12 preenchidos por preenchimento.

---

## Diff de política de IA

Toda avaliação deve cruzar contra os compromissos de política de IA em
`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`.
Desvio comum:

- Política proíbe uso de IA em [categoria] — este caso de uso é essa categoria. Parar.
- Política exige revisão humana — esta implantação não tem passo humano. Design precisa mudar.
- Política exige divulgação às partes afetadas — mecanismo de divulgação não foi construído.
- Lista de fornecedores aprovados existe — este fornecedor não está nela. Passo de
  procurement exigido.

Sinalizar todo desalinhamento. Um dos dois tem que mudar antes da implantação.

---

## Handoffs

- **Para produto / engenharia:** Lista de condições com donos e prazos. Não "adicionar
  supervisão" — "adicionar passo de revisão humana antes de qualquer e-mail
  automatizado ser enviado, dono: [líder de produto], antes do lançamento."
- **Para privacidade:** Se dado pessoal está envolvido, sinalizar: "Rodar
  `/privacy-legal:pia-generation [nome do sistema]` em paralelo, se o plugin
  estiver instalado — a AIA não substitui a RIPD."
- **Para vendor-ai-review:** Se um novo fornecedor está envolvido, sinalizar: "Se
  não há aditivo de IA revisado para [fornecedor], rodar
  `/ai-governance-legal:vendor-ai-review` antes de produção."
- **Para reg-gap-analysis:** Se novas obrigações regulatórias surgiram (PL 2338/2023
  sancionado, nova regra setorial), essa skill rastreia o gap.

---

## Fechar com a árvore de decisão de próximos passos

Terminar com a árvore de decisão de próximos passos conforme CLAUDE.md `## Outputs`.
Customizar as opções para o que essa skill acabou de produzir — os cinco ramos
padrão (rascunhar o X, escalar, buscar mais fatos, aguardar e observar, outra
coisa) são ponto de partida, não travamento. A árvore é o output; o(a) advogado(a)
escolhe.

## O que esta skill não faz

- Não aprova a implantação. Um humano assina a avaliação.
- Não constitui nenhuma avaliação formal de conformidade regulatória — onde um
  regime (ex.: PL 2338/2023, se sancionado) exigir avaliação formal de
  conformidade, isso é exercício separado exigindo revisão jurídica externa e
  documentação técnica além do que está aqui.
- Não desenha as mitigações. Descreve o que precisa mitigar; engenharia desenha
  o conserto.
- Não substitui a RIPD quando dado pessoal está envolvido. Rodar as duas.
