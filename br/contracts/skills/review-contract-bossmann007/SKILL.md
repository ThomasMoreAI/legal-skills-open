---
name: review-contract-bossmann007
title: /review-contract -- Revisão Contratual contra o Playbook
description: Revisa um contrato contra o playbook de negociação da organização — sinaliza desvios, gera redlines, fornece análise de impacto no negócio. Use ao revisar contratos de fornecedor ou cliente, quando precisar de análise cláusula a cláusula contra posições padrão, ou ao preparar estratégia de negociação com redlines priorizados e posições de fallback.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/skills/review-contract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# /review-contract -- Revisão Contratual contra o Playbook

> Se você encontrar placeholders desconhecidos ou precisar checar quais ferramentas estão conectadas, veja [CONNECTORS.md](../../CONNECTORS.md).

Revise um contrato contra o playbook de negociação da organização. Analise cada cláusula, sinalize desvios, gere sugestões de redline e forneça análise de impacto no negócio.

**Importante**: você auxilia em fluxos jurídicos mas não fornece aconselhamento jurídico. Toda análise deve ser revisada por advogado antes de embasar decisões.

## Invocação

```
/review-contract <arquivo ou URL do contrato>
```

Revise o contrato: @$1

## Fluxo

### Etapa 1: Receber o Contrato

Aceite o contrato em qualquer um destes formatos:
- **Upload de arquivo**: PDF, DOCX ou outro formato
- **URL**: link para um contrato no seu CLM, armazenamento em nuvem (Box, Egnyte, SharePoint) ou outro sistema de documentos
- **Texto colado**: texto do contrato colado diretamente na conversa

Se nenhum contrato for fornecido, peça ao usuário que envie um.

### Etapa 2: Levantar o Contexto

Pergunte ao usuário antes de começar a revisão:

1. **De que lado você está?** (fornecedor, cliente/comprador, licenciante, licenciado, parceiro -- ou outro)
2. **Prazo**: quando isso precisa ser finalizado? (afeta a priorização dos problemas)
3. **Pontos de atenção**: alguma preocupação específica? (ex.: "proteção de dados é crítica", "precisamos de flexibilidade no prazo", "titularidade de PI é o ponto-chave")
4. **Contexto do negócio**: algum contexto comercial relevante? (porte do negócio, importância estratégica, relação existente)

Se o usuário fornecer contexto parcial, prossiga com o que tiver e registre as premissas.

### Etapa 3: Carregar o Playbook

Procure o playbook de revisão contratual da organização nas configurações locais (ex.: `legal.local.md` ou arquivo de configuração similar).

O playbook deve definir:
- **Posições padrão**: os termos preferidos da organização para cada tipo de cláusula
- **Faixas aceitáveis**: termos que podem ser aceitos sem escalonamento
- **Gatilhos de escalonamento**: termos que exigem revisão jurídica sênior ou envolvimento de advogado externo

**Se nenhum playbook estiver configurado:**
- Informe ao usuário que nenhum playbook foi encontrado
- Ofereça duas opções:
  1. Ajudar o usuário a montar o playbook (passando por posições para cláusulas-chave)
  2. Prosseguir com revisão genérica usando padrões comerciais amplamente aceitos no Brasil como base
- Se prosseguir genericamente, deixe claro que a revisão é baseada em padrões comerciais gerais, não nas posições específicas da organização

### Etapa 4: Análise Cláusula a Cláusula

Aplique o seguinte processo de revisão:

1. **Identifique o tipo de contrato**: SaaS, prestação de serviços, licença, parceria, fornecimento etc. O tipo de contrato afeta quais cláusulas são mais relevantes.
2. **Determine o lado do usuário**: fornecedor, cliente, licenciante, licenciado, parceiro. Isso muda fundamentalmente a análise (ex.: proteções de limitação de responsabilidade favorecem partes diferentes).
3. **Leia o contrato inteiro** antes de sinalizar problemas. Cláusulas interagem entre si (ex.: indenização sem teto pode ser parcialmente mitigada por ampla limitação de responsabilidade).
4. **Analise cada cláusula relevante** contra a posição do playbook.
5. **Considere o contrato de forma holística**: a alocação geral de risco e os termos comerciais estão equilibrados?

Analise o contrato sistematicamente, cobrindo no mínimo:

| Categoria de Cláusula | Pontos-Chave de Revisão |
|----------------|-------------------|
| **Limitação de Responsabilidade** | Valor do teto, exceções, mútua vs. unilateral, danos indiretos |
| **Indenização** | Escopo, mútua vs. unilateral, teto, violação de PI, vazamento de dados |
| **Titularidade de PI** | PI pré-existente, PI desenvolvida, cessão, licenças, work-for-hire |
| **Proteção de Dados (LGPD)** | Exigência de Acordo de Tratamento de Dados, termos de tratamento, suboperadores, notificação de incidente, transferência internacional |
| **Confidencialidade** | Escopo, prazo, exceções, obrigações de devolução/destruição |
| **Declarações e Garantias** | Escopo, ressalvas, prazo de sobrevivência |
| **Prazo e Rescisão** | Duração, renovação, rescisão por conveniência, rescisão por justa causa, transição |
| **Lei Aplicável e Solução de Controvérsias** | Foro, comarca, arbitragem vs. litígio judicial |
| **Seguro** | Exigências de cobertura, valores mínimos, comprovação |
| **Cessão** | Exigência de consentimento, mudança de controle, exceções |
| **Caso Fortuito e Força Maior** | Escopo, notificação, direitos de rescisão |
| **Condições de Pagamento** | Prazos, multa por atraso, tributos, reajuste de preço |

Para cada cláusula, avalie contra o playbook (ou padrões genéricos) e registre se está presente, ausente ou incomum.

#### Orientação Detalhada por Cláusula

##### Limitação de Responsabilidade

**Elementos-chave a revisar:**
- Valor do teto (valor fixo, múltiplo de honorários, ou sem teto)
- Se o teto é mútuo ou aplica-se de forma diferente a cada parte
- Exceções ao teto (quais responsabilidades ficam sem limite)
- Se danos indiretos, especiais ou punitivos são excluídos
- Se a exclusão é mútua
- Exceções à exclusão de danos indiretos
- Se o teto aplica-se por reclamação, por ano, ou de forma agregada

**Problemas comuns:**
- Teto fixado em fração dos honorários pagos (ex.: "honorários dos últimos 3 meses" em contrato de baixo valor)
- Exceções assimétricas favorecendo quem redigiu
- Exceções amplas que na prática eliminam o teto (ex.: "qualquer violação da Seção X" cobrindo a maioria das obrigações)
- Sem exclusão de danos indiretos para violações de uma das partes

##### Indenização

**Elementos-chave a revisar:**
- Se a indenização é mútua ou unilateral
- Escopo: o que gera a obrigação de indenizar (violação de PI, vazamento de dados — LGPD, dano pessoal, violação de declarações e garantias)
- Se a indenização tem teto (frequentemente sujeita ao teto geral de responsabilidade, às vezes sem teto)
- Procedimento: exigências de notificação, direito de conduzir a defesa, direito de transigir
- Se o indenizado deve mitigar o dano
- Relação entre a indenização e a cláusula de limitação de responsabilidade

**Problemas comuns:**
- Indenização unilateral por violação de PI quando ambas as partes contribuem com PI
- Indenização para "qualquer violação" (escopo amplo demais; na prática converte o teto em responsabilidade ilimitada)
- Sem direito de conduzir a defesa de reclamações
- Obrigações de indenização que sobrevivem indefinidamente à rescisão

##### Propriedade Intelectual

**Elementos-chave a revisar:**
- Titularidade de PI pré-existente (cada parte deve manter a sua)
- Titularidade de PI desenvolvida durante a relação
- Cláusulas de work-for-hire e seu escopo (no Brasil, atenção à Lei 9.610/1998 — direitos autorais — e Lei 9.279/1996 — propriedade industrial)
- Concessão de licença: escopo, exclusividade, território, sublicenciamento
- Considerações sobre software livre/open source
- Cláusulas de feedback (cessão sobre sugestões ou melhorias)

**Problemas comuns:**
- Cessão ampla de PI que poderia abranger a PI pré-existente do cliente
- Cláusulas de work-for-hire que extrapolam os entregáveis
- Cláusulas de feedback irrestritas concedendo licença perpétua e irrevogável
- Escopo de licença mais amplo do que necessário para a relação comercial

##### Proteção de Dados (LGPD)

**Elementos-chave a revisar:**
- Se é exigido Acordo/Termo de Tratamento de Dados
- Classificação como controlador vs. operador (LGPD, art. 5º)
- Direitos e obrigações de notificação de suboperadores
- Prazo de notificação de incidente de segurança (a LGPD não fixa prazo numérico, mas exige comunicação à ANPD e ao titular em "prazo razoável" — recomenda-se alinhar contratualmente a 24-72h)
- Mecanismos de transferência internacional de dados (LGPD, art. 33 — adequação, cláusulas-padrão contratuais, garantias)
- Obrigações de eliminação ou devolução de dados ao término
- Exigências de segurança de dados e direitos de auditoria
- Limitação de finalidade no tratamento de dados

**Problemas comuns:**
- Sem Acordo de Tratamento de Dados quando há tratamento de dado pessoal
- Autorização genérica para suboperadores sem notificação
- Prazo de notificação de incidente maior do que o razoável/regulatório
- Sem proteções para transferência internacional quando os dados saem do Brasil
- Cláusulas de eliminação de dados inadequadas

##### Prazo e Rescisão

**Elementos-chave a revisar:**
- Prazo inicial e termos de renovação
- Cláusulas de renovação automática e prazos de aviso
- Rescisão por conveniência: disponível? prazo de aviso? multa por rescisão antecipada?
- Rescisão por justa causa: prazo de cura? o que configura justa causa?
- Efeitos da rescisão: devolução de dados, assistência na transição, cláusulas de sobrevivência
- Período e obrigações de transição (wind-down)

**Problemas comuns:**
- Prazos iniciais longos sem rescisão por conveniência
- Renovação automática com janela de aviso curta (ex.: 30 dias para renovação anual)
- Sem prazo de cura para rescisão por justa causa
- Cláusulas de assistência na transição inadequadas
- Cláusulas de sobrevivência que na prática estendem o contrato indefinidamente

##### Lei Aplicável e Solução de Controvérsias

**Elementos-chave a revisar:**
- Lei aplicável (em regra, lei brasileira para contratos executados no Brasil — Código Civil, Lei 10.406/2002)
- Mecanismo de solução de controvérsias (litígio judicial, arbitragem, mediação prévia)
- Foro/comarca para litígio
- Regras e sede da arbitragem (se aplicável — Lei 9.307/1996)
- Cláusulas herdadas de minutas estrangeiras (renúncia a júri, etc.) — não aplicáveis no processo civil brasileiro, remover/ajustar
- Cláusula de ação coletiva
- Honorários de sucumbência

**Problemas comuns:**
- Foro desfavorável (comarca incomum ou distante)
- Arbitragem obrigatória com regras favoráveis a quem redigiu
- Cláusulas herdadas de minutas estrangeiras incompatíveis com o sistema processual brasileiro
- Sem processo de escalonamento antes da solução formal de controvérsias

### Etapa 5: Sinalizar Desvios

Classifique cada desvio do playbook usando um sistema de três níveis:

#### VERDE -- Aceitável

A cláusula está alinhada com a posição padrão da organização, ou é melhor que ela. Variações menores comercialmente razoáveis que não aumentam o risco materialmente.

**Exemplos:**
- Teto de responsabilidade em 18 meses de honorários quando o padrão é 12 meses (melhor para o cliente)
- Prazo de NDA mútuo de 2 anos quando o padrão é 3 anos (mais curto mas razoável)
- Lei aplicável em comarca comercial bem estabelecida próxima da preferida

**Ação**: registrar para conhecimento. Sem necessidade de negociação.

#### AMARELO -- Negociar

A cláusula está fora da posição padrão mas dentro de uma faixa negociável. O termo é comum no mercado mas não é a preferência da organização. Exige atenção e provável negociação, mas não escalonamento.

**Exemplos:**
- Teto de responsabilidade em 6 meses de honorários quando o padrão é 12 meses (abaixo do padrão mas negociável)
- Indenização unilateral por violação de PI quando o padrão é mútua (posição comum no mercado mas não preferida)
- Renovação automática com aviso de 60 dias quando o padrão é 90 dias
- Lei aplicável em jurisdição aceitável mas não preferida

**Ação**: gerar linguagem de redline específica. Fornecer posição de fallback. Estimar o impacto de aceitar vs. negociar.
- **Incluir**: redação específica de redline para trazer o termo de volta à posição padrão
- **Incluir**: posição de fallback se a contraparte resistir
- **Incluir**: impacto no negócio de aceitar como está vs. negociar

#### VERMELHO -- Escalar

A cláusula está fora da faixa aceitável, dispara um critério de escalonamento definido, ou apresenta risco material. Exige revisão jurídica sênior, envolvimento de advogado externo, ou aprovação de tomador de decisão de negócio.

**Exemplos:**
- Responsabilidade sem teto ou ausência de cláusula de limitação de responsabilidade
- Indenização ampla unilateral sem teto
- Cessão de PI pré-existente
- Sem Acordo de Tratamento de Dados quando há tratamento de dado pessoal (risco LGPD/ANPD)
- Cláusulas de não concorrência ou exclusividade irrazoáveis
- Lei aplicável e foro problemáticos com arbitragem obrigatória

**Ação**: explicar o risco específico. Fornecer linguagem alternativa de padrão de mercado. Estimar exposição. Recomendar caminho de escalonamento.
- **Incluir**: por que isso é uma sinalização VERMELHA (risco específico)
- **Incluir**: como é a posição padrão de mercado
- **Incluir**: impacto no negócio e exposição potencial
- **Incluir**: caminho de escalonamento recomendado

### Etapa 6: Gerar Sugestões de Redline

Para cada desvio AMARELO e VERMELHO, forneça:
- **Linguagem atual**: cite o texto relevante do contrato
- **Redline sugerido**: linguagem alternativa específica
- **Justificativa**: explicação breve adequada para compartilhar com a contraparte
- **Prioridade**: se é indispensável ou desejável na negociação

#### Boas Práticas para Geração de Redlines

Ao gerar sugestões de redline:

1. **Seja específico**: forneça linguagem exata, não orientação vaga. O redline deve estar pronto para inserir.
2. **Seja equilibrado**: proponha linguagem firme nos pontos críticos mas comercialmente razoável. Redlines excessivamente agressivos atrasam negociações.
3. **Explique a justificativa**: inclua justificativa breve e profissional, adequada para compartilhar com o jurídico da contraparte.
4. **Forneça posições de fallback**: para itens AMARELO, inclua posição de fallback caso o pedido principal seja rejeitado.
5. **Priorize**: nem todo redline tem o mesmo peso. Indique quais são indispensáveis e quais são desejáveis.
6. **Considere a relação**: ajuste tom e abordagem conforme se trate de novo fornecedor, parceiro estratégico ou fornecedor de commodity.

#### Formato de Redline

Para cada redline:
```
**Cláusula**: [referência da seção e nome da cláusula]
**Linguagem atual**: "[citação exata do contrato]"
**Redline proposto**: "[linguagem alternativa específica, com adições destacadas e exclusões riscadas conceitualmente]"
**Justificativa**: [1-2 frases explicando o porquê, adequadas para compartilhamento externo]
**Prioridade**: [Indispensável / Desejável / Bom ter]
**Fallback**: [posição alternativa se o redline principal for rejeitado]
```

### Etapa 7: Resumo de Impacto no Negócio

Forneça uma seção de resumo cobrindo:
- **Avaliação geral de risco**: visão de alto nível do perfil de risco do contrato
- **Top 3 problemas**: os itens mais importantes a tratar
- **Estratégia de negociação**: abordagem recomendada (quais problemas liderar, o que ceder)
- **Considerações de prazo**: fatores de urgência que afetam a abordagem de negociação

#### Framework de Prioridade de Negociação

Ao apresentar redlines, organize por prioridade de negociação:

**Nível 1 -- Indispensáveis (Quebra de Negócio)**
Itens em que a organização não pode prosseguir sem resolução:
- Proteções de responsabilidade sem teto ou materialmente insuficientes
- Exigências de proteção de dados ausentes para dados regulados
- Cláusulas de PI que poderiam comprometer ativos centrais
- Termos que conflitam com obrigações regulatórias (LGPD, CLT, setoriais)

**Nível 2 -- Desejáveis (Preferências Fortes)**
Itens que afetam materialmente o risco mas têm espaço de negociação:
- Ajustes no teto de responsabilidade dentro da faixa
- Escopo e mutualidade da indenização
- Flexibilidade de rescisão
- Direitos de auditoria e compliance

**Nível 3 -- Bons de Ter (Candidatos a Concessão)**
Itens que melhoram a posição mas podem ser cedidos estrategicamente:
- Lei aplicável preferida (se a alternativa for aceitável)
- Preferências de prazo de aviso
- Melhorias definicionais menores
- Exigências de comprovação de seguro

**Estratégia de negociação**: lidere com itens de Nível 1. Troque concessões de Nível 3 para garantir vitórias de Nível 2. Nunca ceda em Nível 1 sem escalonamento.

### Etapa 8: Encaminhamento via CLM (Se Conectado)

Se um sistema de Gestão do Ciclo de Vida de Contratos estiver conectado via MCP:
- Recomende o fluxo de aprovação apropriado conforme o tipo de contrato e o nível de risco
- Sugira o caminho de encaminhamento correto (ex.: aprovação padrão, jurídico sênior, advogado externo)
- Registre aprovações exigidas conforme valor do contrato ou sinalizações de risco

Se nenhum CLM estiver conectado, pule esta etapa.

## Formato de Saída

Estruture a saída como:

```
## Resumo da Revisão Contratual

**Documento**: [nome/identificador do contrato]
**Partes**: [nomes e papéis das partes]
**Seu Lado**: [fornecedor/cliente/etc.]
**Prazo**: [se fornecido]
**Base da Revisão**: [Playbook / Padrões Genéricos]

## Principais Achados

[Top 3-5 problemas com sinalizações de severidade]

## Análise Cláusula a Cláusula

### [Categoria de Cláusula] -- [VERDE/AMARELO/VERMELHO]
**O contrato diz**: [resumo da disposição]
**Posição do playbook**: [seu padrão]
**Desvio**: [descrição da lacuna]
**Impacto no negócio**: [o que isso significa na prática]
**Sugestão de redline**: [linguagem específica, se AMARELO ou VERMELHO]

[Repita para cada cláusula relevante]

## Estratégia de Negociação

[Abordagem recomendada, prioridades, candidatos a concessão]

## Próximos Passos

[Ações específicas a tomar]
```

## Observações

- Se o contrato estiver em idioma diferente do português, registre isso e pergunte se o usuário quer tradução ou revisão no idioma original
- Para contratos muito longos (50+ páginas), ofereça focar primeiro nas seções mais relevantes e depois fazer revisão completa
- Sempre lembre o usuário que esta análise deve ser revisada por advogado habilitado antes de embasar decisões jurídicas
