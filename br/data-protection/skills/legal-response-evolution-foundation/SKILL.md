---
name: legal-response-evolution-foundation
title: legal-response — Gerar Resposta a partir de Templates
description: Gerar uma resposta a uma consulta jurídica comum usando templates configurados, com verificações de escalação para situações que não devem usar resposta padronizada. Use ao responder a solicitações de titulares de dados (LGPD), avisos de hold judicial, questões jurídicas de fornecedores, solicitações de NDA de equipes de negócios ou intimações/ofícios.
author: evolution-foundation
author_url: https://github.com/evolution-foundation/evo-nexus/tree/main/.claude/skills/legal-response
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# legal-response — Gerar Resposta a partir de Templates

> **Este documento não constitui aconselhamento jurídico — consulte o assessor jurídico habilitado antes de enviar qualquer resposta jurídica.**
> Contatos legais: **Thaís Menezes** (contratos Brius/Etus) | **Vitor Lacerda** (jurídico Etus)

Gerar uma resposta a uma consulta jurídica comum usando templates configurados. Personalizar a resposta com detalhes específicos e incluir gatilhos de escalação para situações que não devem usar uma resposta padronizada.

As respostas geradas devem ser revisadas por profissionais jurídicos qualificados antes de serem enviadas, especialmente para comunicações reguladas.

## Acionamento

User executa `/legal-response [tipo-de-consulta]` ou solicita redigir resposta a consulta jurídica.

Tipos de consulta comuns:
- `titular` ou `solicitacao-titular` — Solicitações de acesso/exclusão/correção de titular de dados (LGPD)
- `hold` ou `hold-judicial` — Avisos de hold judicial / preservação de evidências
- `fornecedor` ou `questao-fornecedor` — Questões jurídicas de fornecedores
- `nda` ou `solicitacao-nda` — Solicitações de NDA de equipes de negócios
- `privacidade` ou `consulta-privacidade` — Questões relacionadas à privacidade
- `intimacao` — Respostas a intimações, ofícios ou ordens judiciais
- `seguro` — Notificações de sinistro de seguro
- `personalizado` — Usar um template personalizado

Se nenhum tipo de consulta for fornecido, perguntar ao usuário que tipo de resposta precisa e mostrar as categorias disponíveis.

## Fluxo de Trabalho

### Passo 1: Identificar o Tipo de Consulta

Aceitar o tipo de consulta do usuário. Se o tipo for ambíguo, mostrar as categorias disponíveis e pedir esclarecimento.

### Passo 2: Carregar Template

Buscar templates nas configurações locais (ex: `legal.local.md` ou diretório de templates).

**Se templates estiverem configurados:**
- Carregar o template adequado para o tipo de consulta
- Identificar variáveis obrigatórias (nome do destinatário, datas, detalhes específicos)

**Se nenhum template estiver configurado:**
- Informar ao usuário que nenhum template foi encontrado para este tipo de consulta
- Oferecer ajuda para criar um template (ver Guia de Criação de Templates abaixo)
- Fornecer uma estrutura de resposta padrão razoável com base no tipo de consulta

### Passo 3: Verificar Gatilhos de Escalação

Antes de gerar qualquer resposta, avaliar se esta situação tem características que NÃO devem usar uma resposta padronizada.

#### Gatilhos Universais de Escalação (Aplicam-se a Todas as Categorias)
- A questão envolve litígio potencial ou investigação regulatória
- A consulta é de um regulador (ANPD, PROCON, Ministério Público, Receita Federal, TCU, etc.)
- A resposta poderia criar compromisso legal vinculante ou renúncia
- A questão envolve responsabilidade criminal potencial
- Atenção da mídia está envolvida ou é provável
- A situação é sem precedente (sem tratamento anterior pela equipe)
- Múltiplas jurisdições estão envolvidas com requisitos conflitantes
- A questão envolve liderança executiva ou membros do conselho

#### Gatilhos de Escalação para Solicitações de Titulares (LGPD)
- Solicitação envolve dados de menor de idade, ou é de/em nome de menor
- Solicitação é de autoridade regulatória (não de indivíduo)
- Solicitação envolve dados sujeitos a hold judicial
- Solicitante é funcionário atual ou ex-funcionário com disputa trabalhista ativa ou questão de RH
- Escopo da solicitação é incomumente amplo ou parece uma "pesca" de informações
- Solicitação envolve dados processados em jurisdição com requisitos únicos
- Solicitação envolve dados pessoais sensíveis (saúde, biométrico, genético, religioso, político — art. 11 LGPD)

#### Gatilhos de Escalação para Hold Judicial
- A questão envolve responsabilidade criminal potencial
- O escopo de preservação é incerto, disputado ou potencialmente excessivo
- Há questões sobre se certos dados estão no escopo
- Holds anteriores para a mesma questão ou questão relacionada existem
- O hold pode afetar significativamente as operações de negócios em curso
- Hold conflita com requisitos regulatórios de exclusão (LGPD)
- Custodiante se opõe ao escopo do hold

#### Gatilhos de Escalação para Questões de Fornecedores
- A questão envolve disputa ou potencial violação
- O fornecedor está ameaçando litígio ou rescisão
- A questão envolve conformidade regulatória (não apenas termos contratuais)
- A resposta poderia criar compromisso vinculante ou renúncia
- Resposta pode afetar negociação em curso

#### Gatilhos de Escalação para Solicitações de NDA
- A contraparte é um concorrente
- O NDA envolve informações classificadas do governo
- O contexto de negócios sugere que o NDA é para uma potencial transação de M&A
- A solicitação envolve objeto incomum (dados de treinamento de IA, dados biométricos, etc.)

#### Gatilhos de Escalação para Intimações / Processo Legal
- **SEMPRE requer revisão de assessoria** (templates são pontos de partida apenas)
- Questões de privilégio identificadas
- Dados de terceiros envolvidos
- Questões de produção transfronteiriça
- Prazo irrazoável

**Quando um gatilho de escalação for detectado:**
1. **Parar**: Não gerar resposta padronizada
2. **Alertar**: Informar ao usuário que um gatilho de escalação foi detectado
3. **Explicar**: Descrever qual gatilho foi detectado e por que importa
4. **Recomendar**: Sugerir o caminho de escalação adequado — Thaís Menezes, Vitor Lacerda, ou advogado externo
5. **Oferecer**: Fornecer rascunho para revisão de assessoria (claramente marcado como "RASCUNHO — APENAS PARA REVISÃO DE ASSESSORIA")

### Passo 4: Coletar Detalhes Específicos

Solicitar ao usuário os detalhes necessários para personalizar a resposta:

**Solicitação de Titular de Dados (LGPD):**
- Nome e informações de contato do solicitante
- Tipo de solicitação (acesso, exclusão, correção, portabilidade, revogação de consentimento)
- Quais dados estão envolvidos
- Prazo de resposta (LGPD: 15 dias)

**Hold Judicial:**
- Nome da ação e número de referência
- Custodiantes (quem precisa preservar)
- Escopo de preservação (intervalo de datas, tipos de dados, sistemas)
- Contato do advogado externo (se aplicável — Thaís/Vitor)
- Data efetiva

**Questão de Fornecedor:**
- Nome do fornecedor
- Acordo de referência (se aplicável)
- Questão específica sendo abordada
- Disposições contratuais relevantes

**Solicitação de NDA:**
- Equipe e contato de negócios solicitante
- Nome da contraparte
- Finalidade do NDA
- Mútuo ou unilateral
- Requisitos especiais

### Passo 5: Gerar Resposta

Preencher o template com os detalhes coletados. Garantir que a resposta:
- Use tom adequado (profissional, claro, não excessivamente jurídico para públicos de negócios)
- Inclua todos os elementos jurídicos exigidos para o tipo de resposta
- Referencie datas, prazos e obrigações específicos
- Forneça próximos passos claros para o destinatário
- Inclua avisos ou ressalvas adequados

Apresentar o rascunho de resposta ao usuário para revisão antes de enviar.

#### Diretrizes de Personalização

**Personalização obrigatória** — Cada resposta padronizada DEVE ser personalizada com:
- Nomes, datas e números de referência corretos
- Fatos específicos da situação
- Jurisdição aplicável e regulamentação
- Prazos de resposta corretos com base em quando a consulta foi recebida
- Bloco de assinatura e informações de contato adequados

**Ajuste de tom** — Ajustar tom com base em:
- **Público**: Interno vs. externo, negócios vs. jurídico, indivíduo vs. autoridade regulatória
- **Relacionamento**: Nova contraparte vs. parceiro existente vs. parte adversária
- **Sensibilidade**: Consulta rotineira vs. questão contenciosa vs. investigação regulatória
- **Urgência**: Prazo padrão vs. resposta urgente necessária

**Ajustes específicos por jurisdição (foco no Brasil):**
- Verificar que as regulamentações citadas são corretas para a jurisdição do solicitante
- Ajustar prazos para corresponder à lei aplicável brasileira
- Incluir informações sobre direitos específicos da LGPD quando aplicável
- Usar terminologia jurídica brasileira adequada

### Passo 6: Criação de Templates (Se Nenhum Template Existir)

Se o usuário quiser criar um novo template, percorrer o Guia de Criação de Templates abaixo e apresentar o template finalizado para revisão. Sugerir que o usuário salve o template aprovado nas configurações locais para uso futuro.

## Categorias de Resposta

### 1. Solicitações de Titulares de Dados (LGPD)

**Subcategorias**:
- Confirmação de recebimento
- Solicitação de verificação de identidade
- Resposta de atendimento (acesso, exclusão, correção)
- Negação parcial com explicação
- Negação total com explicação
- Notificação de extensão de prazo

**Elementos obrigatórios do template**:
- Referência à regulamentação aplicável (LGPD, Lei 13.709/2018)
- Prazo específico para resposta (15 dias corridos, art. 18 LGPD)
- Requisitos de verificação de identidade
- Direitos do titular de dados (incluindo direito de peticionar à ANPD)
- Informações de contato para acompanhamento

**Estrutura de template de exemplo**:
```
Assunto: Sua Solicitação de [Acesso/Exclusão/Correção] de Dados — Protocolo {{numero_protocolo}}

Prezado(a) {{nome_solicitante}},

Recebemos sua solicitação datada de {{data_solicitacao}} para [acessar/excluir/corrigir] seus dados pessoais nos termos da Lei Geral de Proteção de Dados (LGPD — Lei 13.709/2018).

[Confirmação / solicitação de verificação de identidade / detalhes de atendimento / base de negação]

Responderemos substancialmente até {{prazo_resposta}} (15 dias corridos).

[Informações de contato]
[Informações sobre direitos — incluindo direito de peticionar à ANPD: www.gov.br/anpd]
```

### 2. Holds Judiciais (Preservação de Evidências)

**Subcategorias**:
- Aviso inicial de hold para custodiantes
- Lembrete / reafirmação periódica de hold
- Modificação de hold (alteração de escopo)
- Liberação de hold

**Elementos obrigatórios do template**:
- Nome da ação e número de referência
- Obrigações de preservação claras
- Escopo de preservação (intervalo de datas, tipos de dados, sistemas, tipos de comunicação)
- Proibição de spoliation (destruição de evidências)
- Contato para dúvidas
- Requisito de confirmação de recebimento

**Estrutura de template de exemplo**:
```
Assunto: AVISO DE PRESERVAÇÃO LEGAL — {{nome_acao}} — Ação Imediata Necessária

PRIVILEGIADO E CONFIDENCIAL
COMUNICAÇÃO ADVOGADO-CLIENTE

Prezado(a) {{nome_custodiante}},

Você está recebendo este aviso porque pode estar de posse de documentos, comunicações ou dados relevantes para a questão referenciada acima.

OBRIGAÇÃO DE PRESERVAÇÃO:
Com efeito imediato, você deve preservar todos os documentos e informações armazenadas eletronicamente (ESI) relacionadas a:
- Objeto: {{escopo_hold}}
- Intervalo de datas: {{data_inicio}} até o presente
- Tipos de documentos: {{tipos_documentos}}

NÃO exclua, destrua, modifique ou descarte nenhum material potencialmente relevante.

[Instruções específicas para sistemas, email, Discord/chat, arquivos locais]

Por favor, confirme o recebimento deste aviso até {{prazo_confirmacao}}.

Contate {{contato_juridico}} com quaisquer dúvidas.
```

### 3. Consultas de Privacidade

**Subcategorias**:
- Respostas sobre cookies/rastreamento
- Questões sobre política de privacidade
- Consultas sobre práticas de compartilhamento de dados
- Questões sobre dados de crianças e adolescentes
- Questões sobre transferência internacional de dados

**Elementos obrigatórios do template**:
- Referência ao aviso de privacidade da organização
- Respostas específicas com base nas práticas atuais
- Links para documentação de privacidade relevante
- Informações de contato para o encarregado de dados (DPO)

### 4. Questões Jurídicas de Fornecedores

**Subcategorias**:
- Resposta a consulta sobre status de contrato
- Resposta a solicitação de aditivo
- Solicitações de certificação de conformidade
- Respostas a solicitações de auditoria
- Solicitações de certificado de seguro

**Elementos obrigatórios do template**:
- Referência ao acordo aplicável
- Resposta específica à questão do fornecedor
- Quaisquer ressalvas ou limitações necessárias
- Próximos passos e cronograma

### 5. Solicitações de NDA

**Subcategorias**:
- Envio do formulário padrão de NDA da organização
- Aceite do NDA da contraparte (com markup)
- Recusa de solicitação de NDA com explicação
- Renovação ou extensão de NDA

**Elementos obrigatórios do template**:
- Finalidade do NDA
- Resumo dos termos padrão
- Instruções de execução (DocuSign ou outro método)
- Expectativas de cronograma

### 6. Intimações / Processo Legal

**Subcategorias**:
- Confirmação de recebimento
- Carta de objeção
- Solicitação de extensão de prazo
- Carta de cobertura de cumprimento

**Elementos obrigatórios do template**:
- Referência da ação e jurisdição (vara/tribunal)
- Objeções específicas (se houver)
- Confirmação de preservação
- Cronograma para cumprimento
- Referência ao log de privilégio (se aplicável)

**Nota crítica**: Respostas a intimações/ofícios quase sempre requerem revisão individualizada de Thaís Menezes ou Vitor Lacerda. Templates servem como frameworks iniciais, não como respostas finais.

### 7. Notificações de Seguro

**Subcategorias**:
- Notificação inicial de sinistro
- Informações suplementares
- Resposta a reserva de direitos

**Elementos obrigatórios do template**:
- Número da apólice e período de cobertura
- Descrição da questão ou incidente
- Linha do tempo dos eventos
- Confirmação de cobertura solicitada

## Metodologia de Gestão de Templates

### Organização de Templates

Templates devem ser organizados por categoria e mantidos nas configurações locais. Cada template deve incluir:

1. **Categoria**: O tipo de consulta que o template aborda
2. **Nome do template**: Um identificador descritivo
3. **Caso de uso**: Quando este template é adequado
4. **Gatilhos de escalação**: Quando este template NÃO deve ser usado
5. **Variáveis obrigatórias**: Informações que devem ser personalizadas para cada uso
6. **Corpo do template**: O texto de resposta com placeholders de variáveis
7. **Ações de acompanhamento**: Passos padrão após o envio da resposta
8. **Data da última revisão**: Quando o template foi verificado por último quanto à precisão

### Ciclo de Vida do Template

1. **Criação**: Rascunho baseado em melhores práticas e contribuição da equipe
2. **Revisão**: Revisão e aprovação por Thaís Menezes ou Vitor Lacerda
3. **Publicação**: Adicionar à biblioteca de templates com metadados
4. **Uso**: Gerar respostas usando o template
5. **Feedback**: Rastrear quando templates são modificados durante o uso para identificar oportunidades de melhoria
6. **Atualização**: Revisar templates quando leis, políticas ou melhores práticas mudarem
7. **Aposentadoria**: Arquivar templates que não são mais aplicáveis

## Guia de Criação de Templates

Ao ajudar usuários a criar novos templates:

### 1. Definir o Caso de Uso
- Que tipo de consulta isso aborda?
- Com que frequência isso aparece?
- Qual é o público típico?
- Qual é o nível típico de urgência?

### 2. Identificar Elementos Obrigatórios
- Que informações devem estar incluídas em cada resposta?
- Quais requisitos regulatórios se aplicam (LGPD, CLT, etc.)?
- Quais políticas organizacionais regem este tipo de resposta?

### 3. Definir Variáveis
- O que muda com cada uso? (nomes, datas, especificidades)
- O que permanece igual? (requisitos legais, linguagem padrão)
- Usar nomes de variáveis claros: `{{nome_solicitante}}`, `{{prazo_resposta}}`, `{{referencia_acao}}`

### 4. Rascunhar o Template
- Escrever em linguagem clara e profissional
- Evitar jargão jurídico desnecessário para públicos de negócios
- Incluir todos os elementos legalmente obrigatórios
- Adicionar placeholders para todo o conteúdo variável
- Incluir template de linha de assunto se for para uso por email

### 5. Definir Gatilhos de Escalação
- Quais situações NÃO devem usar este template?
- Quais características indicam que a questão precisa de atenção individualizada?

### 6. Adicionar Metadados
- Nome e categoria do template
- Número de versão e data da última revisão
- Autor e aprovador (Thaís ou Vitor)
- Checklist de ações de acompanhamento

### Formato de Template

```markdown
## Template: {{nome_template}}
**Categoria**: {{categoria}}
**Versão**: {{versao}} | **Última Revisão**: {{data}}
**Aprovado Por**: {{aprovador}}

### Usar Quando
- [Condição 1]
- [Condição 2]

### NÃO Usar Quando (Gatilhos de Escalação)
- [Gatilho 1]
- [Gatilho 2]

### Variáveis
| Variável | Descrição | Exemplo |
|---|---|---|
| {{var1}} | [o que é] | [valor exemplo] |
| {{var2}} | [o que é] | [valor exemplo] |

### Linha de Assunto
[Template de assunto com {{variáveis}}]

### Corpo
[Corpo da resposta com {{variáveis}}]

### Ações de Acompanhamento
1. [Ação 1]
2. [Ação 2]

### Notas
[Quaisquer instruções especiais para usuários deste template]
```

## Formato de Saída

```
## Resposta Gerada: [Tipo de Consulta]

**Para**: [destinatário]
**Assunto**: [linha de assunto]

---

[Corpo da resposta]

---

### Verificação de Escalação
[Confirmação de que nenhum gatilho de escalação foi detectado, OU gatilhos sinalizados com recomendações]

### Ações de Acompanhamento
1. [Ações pós-envio]
2. [Lembretes de calendário a configurar no Google Calendar]
3. [Requisitos de rastreamento ou registro]
```

## Notas

- Sempre apresentar o rascunho de resposta para revisão do usuário antes de sugerir envio
- Se conectado ao Gmail via MCP, oferecer criar rascunho de email com a resposta
- Rastrear prazos de resposta e oferecer configurar lembretes no Google Calendar
- Para respostas reguladas (solicitações de titulares LGPD, intimações), sempre registrar o prazo aplicável e os requisitos regulatórios
- Templates devem ser documentos vivos; sugerir atualizações quando o usuário modifica uma resposta padronizada, para que o template possa ser melhorado ao longo do tempo
- **Este documento não constitui aconselhamento jurídico.** Contatos: Thaís Menezes | Vitor Lacerda
