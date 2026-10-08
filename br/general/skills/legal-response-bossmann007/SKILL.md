---
name: legal-response-bossmann007
title: /legal-response -- Gerar Resposta a partir de Templates
description: Gera resposta a uma dúvida jurídica recorrente usando templates configurados, com checagem embutida de gatilhos de escalonamento para situações que não devem usar resposta padronizada. Use ao responder solicitações de titulares de dados (LGPD), avisos de preservação de provas, dúvidas jurídicas de fornecedor, pedidos de NDA de times de negócio, ou intimações/ofícios judiciais.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/skills/legal-response
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# /legal-response -- Gerar Resposta a partir de Templates

> Se você encontrar placeholders desconhecidos ou precisar checar quais ferramentas estão conectadas, veja [CONNECTORS.md](../../CONNECTORS.md).

Gera resposta a uma dúvida jurídica recorrente usando templates configurados. Customiza a resposta com detalhes específicos e inclui gatilhos de escalonamento para situações que não devem usar resposta padronizada.

**Importante**: Este comando auxilia em fluxos jurídicos mas não substitui aconselhamento jurídico. Respostas geradas devem ser revisadas por profissional habilitado (OAB) antes de envio, especialmente em comunicações regulatórias.

## Invocação

```
/legal-response [tipo-de-solicitacao]
```

Tipos comuns de solicitação:
- `dsr` ou `solicitacao-titular` -- Solicitação de acesso/eliminação/correção de dados (LGPD, art. 18)
- `hold` ou `preservacao-provas` -- Aviso de preservação de provas/documentos
- `vendor` ou `duvida-fornecedor` -- Dúvida jurídica de fornecedor
- `nda` ou `solicitacao-nda` -- Pedido de NDA de time de negócio
- `privacidade` ou `duvida-privacidade` -- Dúvida relacionada a privacidade/LGPD
- `intimacao` -- Resposta a intimação, ofício ou notificação judicial/extrajudicial
- `seguro` -- Comunicação de sinistro a seguradora
- `custom` -- Usar um template customizado

Se nenhum tipo for informado, pergunte ao usuário qual tipo de resposta ele precisa e mostre as categorias disponíveis.

## Workflow

### Etapa 1: Identificar o Tipo de Solicitação

Aceite o tipo informado pelo usuário. Se ambíguo, mostre as categorias disponíveis e peça esclarecimento.

### Etapa 2: Carregar Template

Procure templates nas configurações locais (ex.: `legal.local.md` ou diretório de templates).

**Se há templates configurados:**
- Carregue o template adequado ao tipo de solicitação
- Identifique variáveis obrigatórias (nome do solicitante, datas, detalhes específicos)

**Se não há templates configurados:**
- Informe ao usuário que nenhum template foi encontrado para este tipo
- Ofereça ajuda para criar um template (veja Guia de Criação de Template abaixo)
- Forneça estrutura de resposta padrão razoável conforme o tipo de solicitação

### Etapa 3: Checar Gatilhos de Escalonamento

Antes de gerar qualquer resposta, avalie se a situação tem características que NÃO devem usar resposta padronizada.

#### Gatilhos Universais de Escalonamento (Todas as Categorias)
- A questão envolve potencial litígio ou investigação regulatória
- A solicitação vem de órgão regulador (ANPD, Procon, etc.), agência governamental ou autoridade policial/judicial
- A resposta pode criar compromisso jurídico vinculante ou renúncia de direito
- A questão envolve potencial responsabilidade criminal
- Há atenção da mídia, envolvida ou provável
- Situação inédita (sem precedente de tratamento pelo time)
- Múltiplas jurisdições envolvidas com exigências conflitantes
- A questão envolve liderança executiva ou membros do conselho

#### Gatilhos de Escalonamento — Solicitação de Titular de Dados (LGPD)
- Solicitação envolve dados de menor de idade, ou é feita por/em nome de menor
- Solicitação vem de autoridade reguladora (ANPD), não de pessoa física
- Solicitação envolve dados sujeitos a preservação de provas (litígio em curso)
- Solicitante é funcionário atual ou ex-funcionário com disputa ativa ou questão trabalhista (CLT)
- Escopo da solicitação é incomumente amplo ou parece "expedição de pesca"
- Solicitação envolve dados tratados em jurisdição com exigências específicas (transferência internacional, art. 33 LGPD)
- Solicitação envolve dado pessoal sensível (saúde, biométrico, genético — art. 5º, II LGPD)

#### Gatilhos de Escalonamento — Preservação de Provas
- A questão envolve potencial responsabilidade criminal
- O escopo da preservação é incerto, contestado ou potencialmente amplo demais
- Há dúvida sobre se determinado dado está dentro do escopo
- Existem preservações anteriores para a mesma questão ou questão relacionada
- A preservação pode afetar significativamente operações do negócio
- Preservação conflita com obrigação regulatória de eliminação de dados (LGPD)
- Custodiante questiona o escopo da preservação

#### Gatilhos de Escalonamento — Dúvida de Fornecedor
- A questão envolve disputa ou potencial inadimplemento contratual
- O fornecedor ameaça litígio ou rescisão
- A questão envolve compliance regulatório (não apenas termos contratuais)
- A resposta pode criar compromisso vinculante ou renúncia de direito
- A resposta pode afetar negociação em curso

#### Gatilhos de Escalonamento — Solicitação de NDA
- A contraparte é concorrente
- O NDA envolve informação sigilosa governamental
- O contexto de negócio sugere que o NDA é para potencial operação de M&A
- A solicitação envolve objeto incomum (dados de treinamento de IA, dados biométricos, etc.)

#### Gatilhos de Escalonamento — Intimação / Ofício / Notificação Judicial
- **SEMPRE exige revisão de advogado** (templates são apenas ponto de partida)
- Identificados problemas de sigilo profissional (Lei 8.906/1994, art. 7º)
- Dados de terceiros envolvidos
- Questões de produção de prova transfronteiriça
- Prazo exíguo/irrazoável

**Quando um gatilho de escalonamento é detectado:**
1. **Pare**: Não gere resposta padronizada
2. **Alerte**: Informe ao usuário que um gatilho de escalonamento foi detectado
3. **Explique**: Descreva qual gatilho foi detectado e por que importa
4. **Recomende**: Sugira o caminho de escalonamento adequado (advogado sênior, escritório externo, membro específico do time)
5. **Ofereça**: Forneça um rascunho para revisão jurídica (claramente marcado como "MINUTA — APENAS PARA REVISÃO JURÍDICA"), não uma resposta final

### Etapa 4: Levantar Detalhes Específicos

Pergunte ao usuário os detalhes necessários para customizar a resposta:

**Solicitação de Titular de Dados (LGPD):**
- Nome e contato do solicitante
- Tipo de solicitação (acesso, eliminação, correção, portabilidade, revogação de consentimento)
- Quais dados estão envolvidos
- Base legal aplicável (LGPD, art. 7º/11)
- Prazo de resposta (art. 19, II — declaração completa em até 15 dias; o §4º permite à ANPD dispor de prazos diferenciados) [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm]

**Preservação de Provas:**
- Nome e número de referência da questão
- Custodiantes (quem precisa preservar)
- Escopo da preservação (período, tipos de dado, sistemas)
- Contato do escritório externo
- Data de vigência

**Dúvida de Fornecedor:**
- Nome do fornecedor
- Contrato de referência (se aplicável)
- Questão específica a ser respondida
- Cláusulas contratuais relevantes

**Solicitação de NDA:**
- Time de negócio solicitante e contato
- Nome da contraparte
- Finalidade do NDA
- Mútuo ou unilateral
- Requisitos especiais

### Etapa 5: Gerar Resposta

Preencha o template com os detalhes levantados. Garanta que a resposta:
- Use tom adequado (profissional, claro, não excessivamente "juridiquês" para público de negócio)
- Inclua todos os elementos jurídicos exigidos para o tipo de resposta
- Referencie datas, prazos e obrigações específicas
- Forneça próximos passos claros ao destinatário
- Inclua ressalvas ou avisos apropriados

Apresente a minuta ao usuário para revisão antes do envio.

#### Diretrizes de Customização

**Customização obrigatória** — Toda resposta padronizada DEVE ser customizada com:
- Nomes, datas e números de referência corretos
- Fatos específicos da situação
- Jurisdição e base legal aplicável
- Prazos de resposta corretos conforme a data de recebimento da solicitação
- Bloco de assinatura e dados de contato adequados

**Ajuste de tom** — Ajuste conforme:
- **Público**: Interno vs. externo, negócio vs. jurídico, pessoa física vs. autoridade reguladora
- **Relacionamento**: Nova contraparte vs. parceiro existente vs. parte adversa
- **Sensibilidade**: Solicitação rotineira vs. questão controversa vs. investigação regulatória
- **Urgência**: Prazo padrão vs. necessidade de resposta acelerada

**Ajustes específicos de jurisdição:**
- Verifique se a base legal citada está correta para a jurisdição do solicitante
- Ajuste prazos conforme a lei aplicável
- Inclua informação de direitos específica da jurisdição
- Use terminologia jurídica adequada à jurisdição

### Etapa 6: Criação de Template (Se Não Existir)

Se o usuário quiser criar um novo template, siga o Guia de Criação de Template (abaixo) e apresente o template finalizado para revisão. Sugira que o usuário salve o template aprovado nas configurações locais para uso futuro.

## Categorias de Resposta

### 1. Solicitações de Titular de Dados (LGPD)

**Subcategorias**:
- Confirmação de recebimento
- Solicitação de verificação de identidade
- Resposta de atendimento (acesso, eliminação, correção)
- Negativa parcial com justificativa
- Negativa total com justificativa
- Notificação de prorrogação de prazo

**Elementos-chave do template**:
- Referência à base legal aplicável (LGPD, Lei 13.709/2018)
- Prazo específico de resposta (art. 19, §3º)
- Requisitos de verificação de identidade
- Direitos do titular (incluindo direito de reclamar à ANPD)
- Dados de contato para acompanhamento

**Estrutura de exemplo**:
```
Assunto: Sua Solicitação de [Acesso/Eliminação/Correção] de Dados - Referência {{request_id}}

Prezado(a) {{requester_name}},

Recebemos sua solicitação datada de {{request_date}} para [acessar/eliminar/corrigir] seus dados pessoais nos termos da LGPD (Lei 13.709/2018).

[Confirmação / pedido de verificação / detalhes do atendimento / fundamento da negativa]

Responderemos de forma substantiva até {{response_deadline}}.

[Dados de contato]
[Informação sobre direitos do titular]
```

### 2. Preservação de Provas

**Subcategorias**:
- Aviso inicial de preservação aos custodiantes
- Lembrete / reafirmação periódica
- Modificação de escopo da preservação
- Liberação da preservação

**Elementos-chave do template**:
- Nome e número de referência da questão
- Obrigações claras de preservação
- Escopo da preservação (período, tipos de dado, sistemas, tipos de comunicação)
- Proibição de destruição de provas
- Contato para dúvidas
- Exigência de confirmação de recebimento

**Estrutura de exemplo**:
```
Assunto: AVISO DE PRESERVAÇÃO DE PROVAS - {{matter_name}} - Ação Necessária

SIGILOSO E CONFIDENCIAL
COMUNICAÇÃO PROTEGIDA POR SIGILO PROFISSIONAL (Lei 8.906/1994, art. 7º)

Prezado(a) {{custodian_name}},

Você recebe este aviso porque pode estar de posse de documentos, comunicações ou dados relevantes para a questão referenciada acima.

OBRIGAÇÃO DE PRESERVAÇÃO:
A partir de agora, você deve preservar todos os documentos e informações armazenadas eletronicamente relativos a:
- Objeto: {{hold_scope}}
- Período: {{start_date}} até o presente
- Tipos de documento: {{document_types}}

NÃO exclua, destrua, modifique ou descarte qualquer material potencialmente relevante.

[Instruções específicas para sistemas, e-mail, chat, arquivos locais]

Favor confirmar o recebimento deste aviso até {{acknowledgment_deadline}}.

Contate {{legal_contact}} em caso de dúvidas.
```

### 3. Dúvidas de Privacidade (LGPD)

**Subcategorias**:
- Resposta a dúvida sobre cookies/rastreamento
- Dúvida sobre política de privacidade
- Dúvida sobre prática de compartilhamento de dados
- Dúvida sobre dados de crianças e adolescentes (ECA + LGPD art. 14)
- Dúvida sobre transferência internacional de dados (LGPD art. 33)

**Elementos-chave do template**:
- Referência ao aviso de privacidade da organização
- Respostas específicas baseadas nas práticas atuais
- Links para documentação de privacidade relevante
- Dados de contato do encarregado de dados (DPO)

### 4. Dúvidas Jurídicas de Fornecedor

**Subcategorias**:
- Resposta a dúvida sobre status contratual
- Resposta a pedido de aditivo
- Pedidos de certificação de compliance
- Respostas a pedido de auditoria
- Pedidos de apólice de seguro

**Elementos-chave do template**:
- Referência ao contrato aplicável
- Resposta específica à dúvida do fornecedor
- Ressalvas ou limitações necessárias
- Próximos passos e prazo

### 5. Solicitações de NDA

**Subcategorias**:
- Envio do NDA padrão da organização
- Aceite do NDA da contraparte (com redline)
- Recusa de solicitação de NDA com justificativa
- Renovação ou extensão de NDA

**Elementos-chave do template**:
- Finalidade do NDA
- Resumo dos termos padrão
- Instruções de assinatura
- Expectativa de prazo

### 6. Intimação / Ofício / Notificação Judicial

**Subcategorias**:
- Confirmação de recebimento
- Carta de impugnação/objeção
- Pedido de prorrogação de prazo
- Carta de encaminhamento do cumprimento

**Elementos-chave do template**:
- Número do processo e foro/vara
- Objeções específicas (se houver)
- Confirmação de preservação de provas
- Prazo para cumprimento
- Referência a eventual sigilo profissional invocado

**Nota crítica**: Respostas a intimação/ofício judicial quase sempre exigem revisão individualizada de advogado. Templates servem apenas como estrutura inicial, não como resposta final.

### 7. Comunicações a Seguradora

**Subcategorias**:
- Comunicação inicial de sinistro
- Informação complementar
- Resposta a reserva de direitos da seguradora

**Elementos-chave do template**:
- Número da apólice e período de cobertura
- Descrição da questão ou incidente
- Cronologia dos eventos
- Confirmação de cobertura solicitada

## Metodologia de Gestão de Templates

### Organização de Templates

Templates devem ser organizados por categoria e mantidos nas configurações locais do time. Cada template deve incluir:

1. **Categoria**: Tipo de solicitação que o template endereça
2. **Nome do template**: Identificador descritivo
3. **Caso de uso**: Quando este template é adequado
4. **Gatilhos de escalonamento**: Quando este template NÃO deve ser usado
5. **Variáveis obrigatórias**: Informação que deve ser customizada a cada uso
6. **Corpo do template**: Texto da resposta com placeholders de variável
7. **Ações de acompanhamento**: Passos padrão após o envio
8. **Data da última revisão**: Quando o template foi verificado pela última vez

### Ciclo de Vida do Template

1. **Criação**: Minuta baseada em boas práticas e input do time
2. **Revisão**: Revisão e aprovação jurídica do conteúdo
3. **Publicação**: Adição à biblioteca de templates com metadados
4. **Uso**: Geração de respostas usando o template
5. **Feedback**: Acompanhamento de modificações feitas durante o uso, para identificar melhorias
6. **Atualização**: Revisão de templates quando leis, políticas ou boas práticas mudam
7. **Desativação**: Arquivamento de templates não mais aplicáveis

## Guia de Criação de Template

Ao ajudar usuários a criar novos templates:

### 1. Defina o Caso de Uso
- Que tipo de solicitação este template endereça?
- Com que frequência isso ocorre?
- Quem é o público típico?
- Qual o nível de urgência típico?

### 2. Identifique Elementos Obrigatórios
- Que informação deve constar em toda resposta?
- Quais exigências regulatórias se aplicam?
- Quais políticas da organização regem este tipo de resposta?

### 3. Defina Variáveis
- O que muda a cada uso? (nomes, datas, especificidades)
- O que permanece igual? (exigências legais, linguagem padrão)
- Use nomes de variável claros: `{{requester_name}}`, `{{response_deadline}}`, `{{matter_reference}}`

### 4. Redija o Template
- Escreva em linguagem clara e profissional
- Evite "juridiquês" desnecessário para público de negócio
- Inclua todos os elementos legalmente exigidos
- Adicione placeholders para todo conteúdo variável
- Inclua template de assunto, se for para uso por e-mail

### 5. Defina Gatilhos de Escalonamento
- Quais situações NÃO devem usar este template?
- Quais características indicam que a questão exige atenção individualizada?
- Seja específico: gatilhos vagos não são úteis

### 6. Adicione Metadados
- Nome e categoria do template
- Número de versão e data da última revisão
- Autor e aprovador
- Checklist de ações de acompanhamento

### Formato de Template

```markdown
## Template: {{template_name}}
**Categoria**: {{category}}
**Versão**: {{version}} | **Última Revisão**: {{date}}
**Aprovado por**: {{approver}}

### Usar Quando
- [Condição 1]
- [Condição 2]

### NÃO Usar Quando (Gatilhos de Escalonamento)
- [Gatilho 1]
- [Gatilho 2]

### Variáveis
| Variável | Descrição | Exemplo |
|---|---|---|
| {{var1}} | [o que é] | [valor de exemplo] |
| {{var2}} | [o que é] | [valor de exemplo] |

### Assunto
[Template de assunto com {{variáveis}}]

### Corpo
[Corpo da resposta com {{variáveis}}]

### Ações de Acompanhamento
1. [Ação 1]
2. [Ação 2]

### Observações
[Instruções especiais para usuários deste template]
```

## Formato de Saída

```
## Resposta Gerada: [Tipo de Solicitação]

**Para**: [destinatário]
**Assunto**: [assunto]

---

[Corpo da resposta]

---

### Checagem de Escalonamento
[Confirmação de que nenhum gatilho de escalonamento foi detectado, OU gatilhos sinalizados com recomendações]

### Ações de Acompanhamento
1. [Ações pós-envio]
2. [Lembretes de agenda a configurar]
3. [Requisitos de rastreamento ou registro]
```

## Observações

- Sempre apresente a minuta para revisão do usuário antes de sugerir o envio
- Se conectado a e-mail via MCP, ofereça criar rascunho de e-mail com a resposta
- Acompanhe prazos de resposta e ofereça configurar lembretes de agenda
- Para respostas regulatórias (solicitações LGPD, intimações), sempre indique o prazo aplicável e as exigências regulatórias
- Templates devem ser documentos vivos; sugira atualizações quando o usuário modificar uma resposta padronizada, para que o template melhore ao longo do tempo
