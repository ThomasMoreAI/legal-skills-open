---
name: legal-compliance-check
title: legal-compliance-check — Verificação de Conformidade
description: Executar uma verificação de conformidade em uma ação proposta, funcionalidade de produto ou iniciativa de negócio, identificando regulamentações aplicáveis, aprovações necessárias e áreas de risco. Use ao lançar uma funcionalidade que lida com dados pessoais, quando marketing ou produto propõe algo com implicações regulatórias, ou quando é necessário saber quais aprovações e requisitos jurisdicionais se aplicam antes de prosseguir.
author: evolution-foundation
author_url: https://github.com/evolution-foundation/evo-nexus/tree/main/.claude/skills/legal-compliance-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# legal-compliance-check — Verificação de Conformidade

> **Este documento não constitui aconselhamento jurídico — consulte o assessor jurídico habilitado antes de tomar decisões com base nesta análise.**
> Contatos legais: **Thaís Menezes** (contratos Brius/Etus) | **Vitor Lacerda** (jurídico Etus)

Executar uma verificação de conformidade em uma ação proposta, funcionalidade de produto, campanha de marketing ou iniciativa de negócio.

Os requisitos regulatórios mudam frequentemente; sempre verificar os requisitos atuais com fontes autorizadas.

## Acionamento

User executa `/legal-compliance-check` ou solicita verificar conformidade de uma ação ou iniciativa.

## O que Preciso de Você

Descreva o que você está planejando fazer. Exemplos:
- "Queremos lançar um programa de indicações com recompensas em dinheiro"
- "Estamos adicionando autenticação biométrica ao nosso aplicativo móvel"
- "Precisamos processar dados de clientes brasileiros em nosso data center no exterior"
- "Marketing quer usar depoimentos de clientes em anúncios"
- "Vamos integrar com um novo subprocessador de dados na Europa"

## Saída

```markdown
## Verificação de Conformidade: [Iniciativa]

### Resumo
[Avaliação rápida: Prosseguir / Prosseguir com condições / Requer revisão adicional]

### Regulamentações e Políticas Aplicáveis
| Regulamentação/Política | Relevância | Requisitos-chave |
|------------------------|-----------|-----------------|
| [LGPD / Marco Civil / CLT / etc.] | [Como se aplica] | [O que você precisa fazer] |

### Requisitos
| # | Requisito | Status | Ação Necessária |
|---|-----------|--------|----------------|
| 1 | [Requisito] | [Atendido / Não Atendido / Desconhecido] | [O que fazer] |

### Áreas de Risco
| Risco | Severidade | Mitigação |
|-------|-----------|-----------|
| [Risco] | [Alta/Média/Baixa] | [Como endereçar] |

### Ações Recomendadas
1. [Ação mais importante]
2. [Segunda prioridade]
3. [Terceira prioridade]

### Aprovações Necessárias
| Aprovador | Por quê | Status |
|-----------|---------|--------|
| [Pessoa/Time] | [Motivo] | [Pendente] |

### Revisão Adicional Recomendada
[Áreas onde revisão de assessoria externa ou especializada é aconselhável]
```

## Visão Geral das Regulamentações de Privacidade

### LGPD — Lei Geral de Proteção de Dados (Lei 13.709/2018) — FRAMEWORK PRIMÁRIO

**Escopo**: Aplica-se ao tratamento de dados pessoais de indivíduos no território nacional brasileiro, independentemente de onde a organização processadora está localizada. Também se aplica quando a atividade de coleta ocorre no Brasil ou quando os dados são de indivíduos localizados no Brasil.

**Obrigações Principais para Equipes Jurídicas:**
- **Base legal**: Identificar e documentar a base legal para cada atividade de tratamento (consentimento, contrato, legítimo interesse, obrigação legal, tutela da saúde, proteção ao crédito — arts. 7º e 11)
- **Direitos dos titulares**: Responder a solicitações de acesso, correção, eliminação, portabilidade, revogação de consentimento e outros dentro de 15 dias (art. 18 LGPD e orientação ANPD)
- **Relatório de Impacto à Proteção de Dados (RIPD)**: Exigido para tratamento de alto risco
- **Notificação de incidente**: Notificar a ANPD e os titulares afetados em prazo razoável (orientação ANPD: 72h para incidentes graves, art. 48)
- **Registros de tratamento**: Manter registros de atividades de tratamento
- **Transferências internacionais**: Garantir salvaguardas adequadas para transferências para fora do Brasil (arts. 33-36 LGPD — decisão de adequação da ANPD ou cláusulas contratuais padrão)
- **Encarregado de Dados (DPO)**: Nomear encarregado se exigido pela ANPD
- **Segurança**: Medidas técnicas e administrativas aptas a proteger os dados (art. 46)

**Enforcement**: ANPD (Autoridade Nacional de Proteção de Dados) — sanções de até 2% do faturamento do grupo no Brasil, limitado a R$ 50 milhões por infração

**Pontos de Contato Jurídico:**
- Revisar contratos com operadores/suboperadores para conformidade com LGPD
- Assessorar equipes de produto nos requisitos de privacidade por design
- Responder a consultas da ANPD
- Gerenciar mecanismos de transferência internacional de dados
- Revisar mecanismos de consentimento e avisos de privacidade

### Marco Civil da Internet (Lei 12.965/2014)

**Escopo**: Estabelece princípios, garantias, direitos e deveres para o uso da Internet no Brasil.

**Obrigações Principais:**
- **Neutralidade de rede**: Não discriminação no tráfego de dados
- **Proteção de dados nas comunicações**: Inviolabilidade das comunicações pela internet (exceto por ordem judicial)
- **Retenção de logs**: Provedores de conexão devem guardar logs por 1 ano; provedores de aplicações por 6 meses
- **Remoção de conteúdo**: Requisitos específicos para responsabilidade civil por conteúdo de terceiros
- **Direitos dos usuários**: Clareza sobre políticas de uso, privacidade e responsabilidade

### Código Civil Brasileiro (Lei 10.406/2002)

**Relevância para conformidade:**
- **Responsabilidade civil** (arts. 186-188, 927): Base para responsabilidade por danos
- **Obrigações contratuais** (arts. 389-420): Rescisão, inadimplemento, multas
- **Boa-fé objetiva** (art. 422): Obrigação de conduta leal nas relações contratuais
- **Limitação de responsabilidade**: Interpretação das cláusulas limitativas (art. 402)
- **Força maior** (art. 393): Excludente de responsabilidade

### CLT — Consolidação das Leis do Trabalho

**Relevância quando aplicável:**
- Relações de trabalho e categorização de trabalhadores (CLT vs. PJ/MEI)
- Proteção de dados de empregados (LGPD + CLT)
- Non-solicitation e non-compete em contratos de trabalho
- Acordos de confidencialidade com funcionários

### Outras Regulamentações a Monitorar

| Regulamentação | Jurisdição | Diferenciadores-chave |
|---|---|---|
| **GDPR** (UE) | União Europeia | Referência para parceiros europeus; base de adequação da LGPD |
| **CCPA / CPRA** (California) | Califórnia, EUA | Para clientes com operações nos EUA |
| **POPIA** (África do Sul) | África do Sul | Para parceiros sul-africanos |
| **PIPL** (China) | China | Regras rígidas de transferência transfronteiriça; localização de dados |
| **UK GDPR** | Reino Unido | Para parceiros britânicos |

## Checklist de Revisão de DPA/Contrato de Processamento

Ao revisar um Contrato ou Adendo de Processamento de Dados (conforme exigido pela LGPD), verificar:

### Elementos Obrigatórios (LGPD art. 37-40)

- [ ] **Objeto e duração**: Escopo e prazo de tratamento claramente definidos
- [ ] **Natureza e finalidade**: Descrição específica do tratamento e do porquê
- [ ] **Tipo de dados pessoais**: Categorias de dados pessoais tratados
- [ ] **Categorias de titulares**: De quem são os dados pessoais tratados
- [ ] **Obrigações e direitos do controlador**: Instruções do controlador e direitos de supervisão

### Obrigações do Operador

- [ ] **Tratar apenas conforme instruções documentadas**: Operador se compromete a tratar apenas conforme instruções do controlador
- [ ] **Confidencialidade**: Pessoal autorizado a tratar os dados se comprometeu com sigilo
- [ ] **Medidas de segurança**: Medidas técnicas e organizacionais adequadas descritas (art. 46 LGPD)
- [ ] **Requisitos para suboperadores**:
  - [ ] Requisito de autorização escrita (geral ou específica)
  - [ ] Se autorização geral: notificação de alterações com oportunidade de objeção
  - [ ] Suboperadores vinculados pelas mesmas obrigações via acordo escrito
  - [ ] Operador permanece responsável pelo desempenho do suboperador
- [ ] **Assistência nos direitos dos titulares**: Operador auxiliará o controlador em responder a solicitações dos titulares
- [ ] **Assistência em segurança e incidentes**: Operador auxiliará com obrigações de segurança, notificação de incidentes e RIPDs
- [ ] **Eliminação ou devolução**: Na rescisão, eliminar ou devolver todos os dados pessoais (conforme escolha do controlador)
- [ ] **Direitos de auditoria**: Controlador tem direito de realizar auditorias e inspeções
- [ ] **Notificação de incidente**: Operador notificará o controlador sobre incidentes de segurança sem demora injustificada (preferencialmente em 24-48h para permitir que o controlador cumpra o prazo regulatório)

### Transferências Internacionais (Arts. 33-36 LGPD)

- [ ] **Mecanismo de transferência identificado**: Decisão de adequação da ANPD, cláusulas contratuais padrão aprovadas pela ANPD, ou garantias específicas
- [ ] **Avaliação de impacto de transferência**: Concluída se transferindo para países sem decisão de adequação
- [ ] **Medidas complementares**: Técnicas, organizacionais ou contratuais para endereçar lacunas identificadas

### Considerações Práticas

- [ ] **Responsabilidade**: Disposições de responsabilidade do DPA alinhadas com o contrato principal de serviços
- [ ] **Alinhamento de vigência**: Prazo do DPA alinhado com o contrato de serviços
- [ ] **Locais de processamento**: Locais de tratamento especificados e aceitáveis
- [ ] **Padrões de segurança**: Padrões ou certificações de segurança específicas exigidas (SOC 2, ISO 27001, etc.)

## Tratamento de Solicitações de Titulares de Dados

### Recebimento da Solicitação

Quando uma solicitação de titular de dados for recebida (art. 18 LGPD):

1. **Identificar o tipo de solicitação**:
   - Acesso (cópia dos dados pessoais)
   - Retificação (correção de dados inexatos)
   - Eliminação / exclusão
   - Portabilidade (formato estruturado e legível por máquina)
   - Revogação de consentimento
   - Oposição ao tratamento
   - Informação sobre compartilhamento

2. **Identificar a(s) regulamentação(ões) aplicável(is):**
   - Onde está localizado o titular de dados?
   - Quais leis se aplicam com base na presença e atividades da organização?

3. **Verificar a identidade**:
   - Confirmar que o solicitante é quem afirma ser
   - Usar medidas razoáveis de verificação proporcionais à sensibilidade dos dados

4. **Registrar a solicitação**:
   - Data de recebimento, tipo de solicitação, identidade do solicitante, regulamentação aplicável, prazo de resposta, responsável

### Prazos de Resposta

| Regulamentação | Confirmação Inicial | Resposta Substantiva | Extensão |
|---|---|---|---|
| **LGPD** | Imediata (boa prática) | 15 dias | Limitada (com justificativa) |
| GDPR | Não especificado (boa prática: imediata) | 30 dias | +60 dias (com aviso) |
| CCPA/CPRA | 10 dias úteis | 45 dias corridos | +45 dias (com aviso) |

### Isenções e Exceções

Antes de atender uma solicitação, verificar se alguma isenção se aplica:

**Isenções comuns (LGPD art. 16):**
- Defesa em processos judiciais, administrativos ou arbitrais
- Obrigações legais de retenção
- Interesse público, pesquisa científica ou histórica
- Proteção do crédito
- Outros legítimos interesses do controlador (conforme aplicável)

**Considerações específicas da organização:**
- Hold judicial: dados sujeitos a retenção legal não podem ser eliminados
- Retenção regulatória: registros financeiros, registros trabalhistas e outras categorias podem ter prazos obrigatórios de retenção
- Direitos de terceiros: atender à solicitação pode afetar adversamente os direitos de outros

## Monitoramento Regulatório

### O que Monitorar

Manter-se atualizado sobre desenvolvimentos em:
- **Orientações regulatórias**: Novas ou atualizadas da ANPD, CGU, CADE, órgãos setoriais
- **Ações de enforcement**: Multas, ordens e acordos que sinalizam prioridades regulatórias
- **Mudanças legislativas**: Novas leis de privacidade, emendas a leis existentes
- **Padrões da indústria**: Atualizações em ISO 27001, SOC 2, frameworks de segurança setoriais
- **Desenvolvimentos de transferência internacional**: Decisões de adequação da ANPD, atualizações de cláusulas contratuais padrão

### Critérios de Escalação

Escalar para Thaís Menezes ou Vitor Lacerda quando:
- Uma nova regulamentação ou orientação afeta diretamente as atividades de negócio principais
- Uma ação de enforcement no setor da organização sinaliza maior escrutínio regulatório
- Um prazo de conformidade está se aproximando e exige mudanças organizacionais
- Um mecanismo de transferência de dados do qual a organização depende é contestado ou invalidado
- Uma autoridade regulatória inicia uma consulta ou investigação envolvendo a organização

## Dicas

1. **Seja específico** — "Queremos enviar email para todos os nossos usuários" é melhor do que "campanha de marketing."
2. **Inclua a geografia** — Os requisitos de conformidade variam por jurisdição.
3. **Mencione os dados** — Quais dados pessoais estão envolvidos? Isso determina a maioria dos requisitos de conformidade com a LGPD.

> **Este documento não constitui aconselhamento jurídico.** Consulte Thaís Menezes ou Vitor Lacerda para decisões legais.
