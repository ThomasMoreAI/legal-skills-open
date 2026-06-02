---
name: legal-review-contract
title: legal-review-contract — Revisão de Contrato contra Playbook
description: Revisar um contrato contra o playbook de negociação da organização — sinalizar desvios, gerar redlines e fornecer análise de impacto de negócios. Use ao revisar acordos com fornecedores ou clientes, ao precisar de análise cláusula por cláusula contra posições padrão, ou ao preparar estratégia de negociação com redlines priorizadas e posições de fallback.
author: evolution-foundation
author_url: https://github.com/evolution-foundation/evo-nexus/tree/main/.claude/skills/legal-review-contract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: pt
---

# legal-review-contract — Revisão de Contrato contra Playbook

> **Este documento não constitui aconselhamento jurídico — consulte o assessor jurídico habilitado antes de tomar decisões com base nesta análise.**
> Contatos legais: **Thaís Menezes** (contratos Brius/Etus) | **Vitor Lacerda** (jurídico Etus)

Revisar um contrato contra o playbook de negociação da organização. Analisar cada cláusula, sinalizar desvios, gerar sugestões de redline e fornecer análise de impacto de negócios.

## Acionamento

User executa `/legal-review-contract` ou solicita revisar, checar ou analisar um contrato.

## Fluxo de Trabalho

### Passo 1: Aceitar o Contrato

Aceitar o contrato em qualquer um destes formatos:
- **Upload de arquivo**: PDF, DOCX ou outro formato de documento
- **Arquivo local / Notion**: Link para o contrato em armazenamento local ou página Notion
- **Texto colado**: Texto do contrato colado diretamente na conversa

Se nenhum contrato for fornecido, solicitar ao usuário que o forneça.

### Passo 2: Coletar Contexto

Perguntar ao usuário pelo contexto antes de iniciar a revisão:

1. **Qual lado você está?** (fornecedor/prestador, cliente/comprador, licenciante, licenciado, parceiro — ou outro)
2. **Prazo**: Quando precisa ser finalizado? (Afeta a priorização de problemas)
3. **Áreas de foco**: Alguma preocupação específica? (ex: "proteção de dados é crítica", "precisamos de flexibilidade no prazo", "propriedade intelectual é a questão-chave")
4. **Contexto do negócio**: Algum contexto de negócios relevante? (ex: valor do contrato, importância estratégica, relacionamento existente)

Se o usuário fornecer contexto parcial, prosseguir com o que tiver e registrar as premissas.

### Passo 3: Carregar o Playbook

Buscar o playbook de revisão de contratos nas configurações locais (ex: `legal.local.md` ou arquivos de configuração similares).

O playbook deve definir:
- **Posições padrão**: Termos preferidos da organização para cada tipo de cláusula principal
- **Faixas aceitáveis**: Termos que podem ser acordados sem escalação
- **Gatilhos de escalação**: Termos que requerem revisão de assessoria sênior ou assessoria externa

**Se nenhum playbook estiver configurado:**
- Informar ao usuário que nenhum playbook foi encontrado
- Oferecer duas opções:
  1. Ajudar o usuário a configurar seu playbook (percorrer a definição de posições para cláusulas-chave)
  2. Prosseguir com uma revisão genérica usando padrões comerciais amplamente aceitos como baseline
- Se prosseguir genericamente, registrar claramente que a revisão é baseada em padrões comerciais gerais, não nas posições específicas da organização

### Passo 4: Análise Cláusula por Cláusula

Aplicar o seguinte processo de revisão:

1. **Identificar o tipo de contrato**: SaaS, serviços profissionais, licença, parceria, compras, etc.
2. **Determinar o lado do usuário**: Fornecedor, cliente, licenciante, licenciado, parceiro.
3. **Ler o contrato inteiro** antes de sinalizar problemas — as cláusulas interagem entre si.
4. **Analisar cada cláusula material** contra a posição do playbook.
5. **Considerar o contrato de forma holística**: O perfil de risco e os termos comerciais estão equilibrados?

Analisar o contrato sistematicamente, cobrindo no mínimo:

| Categoria de Cláusula | Pontos Principais de Revisão |
|----------------------|------------------------------|
| **Limitação de Responsabilidade** | Teto (cap), carveouts, mútua vs. unilateral, danos consequentes (art. 402 CC/BR) |
| **Indenização** | Escopo, mútua vs. unilateral, teto, violação de PI, violação de dados |
| **Propriedade Intelectual** | PI pré-existente, PI desenvolvida, work-for-hire, licenças, cessão |
| **Proteção de Dados (LGPD)** | Contrato/DPA de processamento, base legal, suboperadores, notificação de incidente, transferência internacional |
| **Confidencialidade** | Escopo, prazo, exclusões, obrigações de devolução/destruição |
| **Declarações e Garantias** | Escopo, exclusões de garantia, período de sobrevivência |
| **Vigência e Rescisão** | Duração, renovação, rescisão sem causa, rescisão por justa causa, período de transição |
| **Lei Aplicável e Resolução de Disputas** | Foro competente, arbitragem vs. litígio, câmara arbitral |
| **Seguro** | Coberturas exigidas, valores mínimos, certificado de cobertura |
| **Cessão** | Requisitos de consentimento, mudança de controle, exceções |
| **Força Maior** | Escopo (art. 393 CC/BR), notificação, direitos de rescisão |
| **Condições de Pagamento** | Prazo, multas por atraso, impostos (ISS, PIS/COFINS), reajuste de preço |

#### Orientação Detalhada por Cláusula

##### Limitação de Responsabilidade

**Elementos-chave para revisar:**
- Valor do teto (valor fixo, múltiplo das taxas pagas, ou ilimitado)
- Se o teto é mútuo ou se aplica de forma diferente a cada parte
- Carveouts do teto (quais responsabilidades ficam fora do teto)
- Se danos indiretos, especiais ou punitivos são excluídos (observar limites do art. 402 CC/BR)
- Se a exclusão é mútua
- Carveouts da exclusão de danos consequentes
- Se o teto se aplica por demanda, por ano ou de forma agregada

**Problemas comuns:**
- Teto definido como fração das taxas pagas (ex: "taxas pagas nos 3 meses anteriores" em contrato de baixo valor)
- Carveouts assimétricos favorecendo o redator
- Carveouts amplos que efetivamente eliminam o teto
- Nenhuma exclusão de danos consequentes para violações de uma das partes

##### Indenização

**Elementos-chave para revisar:**
- Se a indenização é mútua ou unilateral
- Escopo: o que aciona a obrigação de indenização (violação de PI, violação de dados, lesões corporais, violação de declarações)
- Se a indenização está sujeita ao teto de responsabilidade
- Procedimento: requisitos de notificação, direito de controlar defesa, direito de transigir
- Relação entre indenização e cláusula de limitação de responsabilidade

**Problemas comuns:**
- Indenização unilateral por violação de PI quando ambas as partes contribuem com PI
- Indenização por "qualquer violação" (muito amplo; converte efetivamente o teto em ilimitado)
- Sem direito de controlar a defesa
- Obrigações de indenização que sobrevivem indefinidamente à rescisão

##### Propriedade Intelectual

**Elementos-chave para revisar:**
- Propriedade da PI pré-existente (cada parte deve reter a sua)
- Propriedade da PI desenvolvida durante o engajamento
- Disposições de obra por encomenda e seu escopo (Lei 9.610/98)
- Concessões de licença: escopo, exclusividade, território, direitos de sublicença
- Considerações de open source
- Cláusulas de feedback (concessões sobre sugestões ou melhorias)

**Problemas comuns:**
- Cessão ampla de PI que poderia capturar PI pré-existente do cliente
- Disposições de obra por encomenda que se estendem além das entregas
- Cláusulas de feedback irrestrito concedendo licenças perpétuas e irrevogáveis
- Escopo de licença mais amplo do que necessário para a relação de negócios

##### Proteção de Dados (LGPD)

**Elementos-chave para revisar (Lei 13.709/2018 — LGPD como framework primário):**
- Se um Contrato/Adendo de Processamento de Dados é necessário
- Classificação de controlador vs. operador de dados (arts. 5º e 39 LGPD)
- Direitos e obrigações de notificação de suboperadores (art. 40 LGPD)
- Prazo de notificação de incidente de segurança (prazo razoável, art. 48 LGPD — orientação ANPD: 72h para riscos graves)
- Mecanismos de transferência internacional de dados (arts. 33-36 LGPD)
- Obrigações de exclusão ou retorno de dados na rescisão
- Requisitos de segurança e direitos de auditoria (art. 46 LGPD)
- Limitação de finalidade para o processamento de dados
- Marco Civil da Internet (Lei 12.965/2014) quando aplicável

**Referências internacionais secundárias:** GDPR (para contratos com parceiros europeus), CCPA (para parceiros com operações na Califórnia)

**Problemas comuns:**
- Nenhum Contrato de Processamento de Dados quando dados pessoais estão sendo processados
- Autorização irrestrita para suboperadores sem notificação
- Prazo de notificação de incidente mais longo do que os requisitos regulatórios
- Nenhuma proteção de transferência internacional quando dados cruzam fronteiras
- Disposições de exclusão de dados inadequadas

##### Vigência e Rescisão

**Elementos-chave para revisar:**
- Prazo inicial e termos de renovação
- Disposições de renovação automática e prazos de aviso prévio
- Rescisão sem causa (imotivada): disponível? Prazo de aviso? Multas por rescisão antecipada?
- Rescisão por justa causa: prazo para cura? O que constitui causa?
- Efeitos da rescisão: retorno de dados, assistência de transição, cláusulas de sobrevivência
- Período e obrigações de transição

**Problemas comuns:**
- Prazos iniciais longos sem rescisão imotivada
- Renovação automática com janelas curtas de aviso (ex: 30 dias para renovação anual)
- Sem período de cura para rescisão por justa causa
- Disposições de assistência de transição inadequadas
- Cláusulas de sobrevivência que efetivamente estendem o acordo indefinidamente

##### Lei Aplicável e Resolução de Disputas

**Elementos-chave para revisar:**
- Escolha da lei (jurisdição aplicável) — preferência pela lei brasileira (Código Civil, lei específica do setor)
- Mecanismo de resolução de disputas (litígio, arbitragem, mediação prévia)
- Foro (para litígio — JFSP, TJSP ou foro de eleição conforme art. 63 CPC)
- Regras de arbitragem e sede (se arbitragem — CAMARB, CAM-CCBC, ICC Brasil)
- Renúncia a tribunal do júri (não aplicável no Brasil)
- Honorários advocatícios

**Problemas comuns:**
- Jurisdição desfavorável (foro incomum ou distante)
- Arbitragem mandatória com regras favorecendo o redator
- Sem processo de escalonamento antes da resolução formal de disputas

### Passo 5: Sinalizar Desvios

Classificar cada desvio do playbook usando um sistema de três níveis:

#### VERDE — Aceitável

A cláusula está alinhada com ou é melhor do que a posição padrão da organização. Variações menores que são comercialmente razoáveis e não aumentam o risco materialmente.

**Ação**: Registrar para conhecimento. Nenhuma negociação necessária.

#### AMARELO — Negociar

A cláusula está fora da posição padrão mas dentro de uma faixa negociável. O termo é comum no mercado mas não é a preferência da organização.

**Ação**: Gerar linguagem de redline específica. Fornecer posição de fallback. Estimar impacto de negócios de aceitar vs. negociar.
- **Incluir**: Linguagem de redline específica para trazer o termo de volta à posição padrão
- **Incluir**: Posição de fallback se a contraparte pressionar
- **Incluir**: Impacto de negócios de aceitar como está vs. negociar

#### VERMELHO — Escalar

A cláusula está fora da faixa aceitável, aciona um critério de escalação definido ou representa risco material. Requer revisão de assessoria sênior, envolvimento de advogado externo ou aprovação de tomador de decisão de negócios.

**Ação**: Explicar o risco específico. Fornecer linguagem alternativa padrão de mercado. Estimar exposição. Recomendar caminho de escalação.
- **Incluir**: Por que isso é uma flag VERMELHA (risco específico)
- **Incluir**: Como é a posição padrão do mercado
- **Incluir**: Impacto de negócios e exposição potencial
- **Incluir**: Caminho de escalação recomendado — contatar Thaís Menezes ou Vitor Lacerda

### Passo 6: Gerar Sugestões de Redline

Para cada desvio AMARELO e VERMELHO, fornecer:
- **Linguagem atual**: Citar o texto relevante do contrato
- **Redline sugerido**: Linguagem alternativa específica
- **Rationale**: Breve explicação adequada para compartilhar com a contraparte
- **Prioridade**: Se é imprescindível ou desejável na negociação

#### Formato de Redline

Para cada redline:
```
**Cláusula**: [Referência da seção e nome da cláusula]
**Linguagem atual**: "[citação exata do contrato]"
**Redline proposto**: "[linguagem alternativa específica com adições em negrito e exclusões riscadas conceitualmente]"
**Rationale**: [1-2 frases explicando o porquê, adequadas para compartilhamento externo]
**Prioridade**: [Imprescindível / Importante / Desejável]
**Fallback**: [Posição alternativa se o redline principal for rejeitado]
```

### Passo 7: Resumo de Impacto de Negócios

Fornecer uma seção de resumo cobrindo:
- **Avaliação geral de risco**: Visão de alto nível do perfil de risco do contrato
- **Top 3 questões**: Os itens mais importantes a serem tratados
- **Estratégia de negociação**: Abordagem recomendada (com quais questões liderar, o que conceder)
- **Considerações de prazo**: Quaisquer fatores de urgência que afetam a abordagem de negociação

#### Framework de Prioridade de Negociação

**Tier 1 — Imprescindíveis (Dealbreakers)**
Questões nas quais a organização não pode prosseguir sem resolução:
- Proteções de responsabilidade insuficientes ou ilimitadas
- Requisitos de proteção de dados ausentes para dados regulados (LGPD, Marco Civil)
- Disposições de PI que poderiam comprometer ativos essenciais
- Termos que conflitam com obrigações regulatórias brasileiras

**Tier 2 — Importantes (Fortes Preferências)**
Questões que afetam materialmente o risco mas têm espaço de negociação:
- Ajustes de teto de responsabilidade dentro da faixa
- Escopo e mutualidade de indenização
- Flexibilidade de rescisão
- Direitos de auditoria e conformidade

**Tier 3 — Desejáveis (Candidatos a Concessão)**
Questões que melhoram a posição mas podem ser concedidas estrategicamente:
- Lei aplicável preferida (se a alternativa for aceitável)
- Preferências de prazo de aviso
- Melhorias definicionais menores
- Requisitos de certificado de seguro

**Estratégia de negociação**: Liderar com itens Tier 1. Trocar concessões Tier 3 para garantir vitórias Tier 2. Nunca ceder no Tier 1 sem escalação.

### Passo 8: Roteamento Manual (Sem CLM)

Sem um sistema CLM conectado, ao final da revisão:
- Recomendar o fluxo de aprovação adequado com base no tipo de contrato e nível de risco
- Sugerir o caminho correto de roteamento (ex: aprovação padrão, assessoria sênior, advogado externo)
- Registrar quaisquer aprovações necessárias com base no valor ou flags de risco do contrato
- Sugerir salvar o documento revisado em local/Notion com nomenclatura padronizada

## Formato de Saída

Estruturar a saída como:

```
## Resumo da Revisão do Contrato

**Documento**: [nome/identificador do contrato]
**Partes**: [nomes das partes e funções]
**Seu Lado**: [fornecedor/cliente/etc.]
**Prazo**: [se fornecido]
**Base da Revisão**: [Playbook / Padrões Genéricos]

## Principais Constatações

[Top 3-5 questões com flags de severidade]

## Análise Cláusula por Cláusula

### [Categoria da Cláusula] — [VERDE/AMARELO/VERMELHO]
**Contrato diz**: [resumo da disposição]
**Posição do playbook**: [seu padrão]
**Desvio**: [descrição da lacuna]
**Impacto de negócios**: [o que isso significa praticamente]
**Sugestão de redline**: [linguagem específica, se AMARELO ou VERMELHO]

[Repetir para cada cláusula principal]

## Estratégia de Negociação

[Abordagem recomendada, prioridades, candidatos a concessão]

## Próximos Passos

[Ações específicas a tomar — incluir encaminhamento para Thaís ou Vitor se necessário]
```

## Notas

- Se o contrato estiver em idioma diferente do português, registrar isso e perguntar se o usuário quer tradução ou revisão no idioma original
- Para contratos muito longos (50+ páginas), oferecer para focar nas seções mais materiais primeiro e depois fazer uma revisão completa
- Sempre lembrar ao usuário que esta análise deve ser revisada por assessor jurídico qualificado antes de ser usada para decisões legais
- **Este documento não constitui aconselhamento jurídico.** Contatos: Thaís Menezes (contratos) | Vitor Lacerda (jurídico Etus)
