---
name: compliance-check-bossmann007
title: /compliance-check -- Revisão de Compliance
description: Realiza uma verificação de compliance sobre uma ação proposta, funcionalidade de produto ou iniciativa de negócio, identificando regulações aplicáveis, aprovações necessárias e áreas de risco. Use ao lançar uma funcionalidade que envolve dados pessoais, quando marketing ou produto propõe algo com implicações regulatórias, ou quando você precisa saber quais aprovações e exigências (LGPD, CLT, CDC, Lei 14.133/2021) se aplicam antes de prosseguir.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/skills/compliance-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# /compliance-check -- Revisão de Compliance

> Se você ver placeholders desconhecidos ou precisar verificar quais ferramentas estão conectadas, veja [CONNECTORS.md](../../CONNECTORS.md).

Realiza uma verificação de compliance sobre uma ação proposta, funcionalidade de produto, campanha de marketing ou iniciativa de negócio.

**Importante**: Este comando auxilia em fluxos de trabalho jurídicos, mas não fornece consultoria jurídica. As avaliações de compliance devem ser revisadas por profissionais de direito qualificados. As exigências regulatórias mudam com frequência; sempre verifique os requisitos atuais em fontes oficiais (ANPD, órgãos reguladores setoriais).

## Uso

```
/compliance-check $ARGUMENTS
```

## O Que Preciso de Você

Descreva o que você está planejando fazer. Exemplos:
- "Queremos lançar um programa de indicação com recompensa em dinheiro"
- "Estamos adicionando autenticação biométrica ao nosso aplicativo"
- "Precisamos processar dados de clientes europeus em nosso data center no Brasil"
- "O marketing quer usar depoimentos de clientes em anúncios"

## Saída

```markdown
## Verificação de Compliance: [Iniciativa]

### Resumo
[Avaliação rápida: Pode prosseguir / Pode prosseguir com condições / Requer revisão adicional]

### Regulações e Políticas Aplicáveis
| Regulação/Política | Relevância | Exigências-Chave |
|-------------------|-----------|-----------------|
| [LGPD / CDC / CLT / Lei 14.133/2021 / etc.] | [Como se aplica] | [O que precisa ser feito] |

### Requisitos
| # | Requisito | Status | Ação Necessária |
|---|-------------|--------|---------------|
| 1 | [Requisito] | [Atendido / Não Atendido / Desconhecido] | [O que fazer] |

### Áreas de Risco
| Risco | Severidade | Mitigação |
|------|----------|------------|
| [Risco] | [Alto/Médio/Baixo] | [Como tratar] |

### Ações Recomendadas
1. [Ação mais importante]
2. [Segunda prioridade]
3. [Terceira prioridade]

### Aprovações Necessárias
| Aprovador | Por Quê | Status |
|----------|-----|--------|
| [Pessoa/Time] | [Razão] | [Pendente] |

### Revisão Adicional Recomendada
[Áreas em que se recomenda revisão por advogado externo ou especialista]
```

## Panorama das Regulações de Privacidade e Compliance no Brasil

### LGPD (Lei Geral de Proteção de Dados — Lei 13.709/2018)

**Escopo**: Aplica-se a qualquer operação de tratamento de dados pessoais realizada por pessoa natural ou jurídica, de direito público ou privado, no território nacional — independentemente do meio, do país de sede ou do país onde estejam localizados os dados — desde que a atividade de tratamento ocorra no Brasil, a operação tenha por objetivo oferta ou fornecimento de bens/serviços a pessoas no território nacional, ou os dados pessoais tratados tenham sido coletados no Brasil.

**Obrigações-Chave para o Jurídico Interno**:
- **Base legal**: Identificar e documentar a base legal para cada atividade de tratamento (consentimento, cumprimento de obrigação legal/regulatória, execução de contrato, legítimo interesse, proteção da vida, exercício regular de direitos em processo, entre outras do art. 7º)
- **Direitos dos titulares**: Responder a solicitações de acesso, retificação, eliminação, portabilidade, anonimização, informação sobre compartilhamento e revogação de consentimento (arts. 17-22)
- **Relatório de Impacto à Proteção de Dados Pessoais (RIPD)**: Pode ser exigido pela ANPD para operações de tratamento que apresentem risco às liberdades civis e aos direitos fundamentais
- **Notificação de incidente**: Comunicar à ANPD e ao titular a ocorrência de incidente de segurança que possa acarretar risco ou dano relevante, em prazo razoável (a LGPD não fixa prazo numérico fixo; observar regulamentação da ANPD)
- **Registro das operações de tratamento**: Manter registro das operações de tratamento de dados pessoais realizadas, especialmente quando baseado no legítimo interesse
- **Transferências internacionais**: Garantir salvaguardas adequadas para transferência de dados para fora do Brasil (cláusulas-padrão contratuais, decisão de adequação da ANPD, normas corporativas globais, selos/certificados)
- **Encarregado (DPO)**: Indicar encarregado pelo tratamento de dados pessoais (art. 41), com identidade e informações de contato divulgadas publicamente

**Pontos de Contato Comuns do Jurídico Interno**:
- Revisar contratos de operação de dados de fornecedores (operadores) quanto à conformidade com a LGPD
- Orientar times de produto sobre privacy by design e privacy by default
- Responder a ofícios e notificações da ANPD
- Gerenciar mecanismos de transferência internacional de dados
- Revisar mecanismos de consentimento e avisos de privacidade

### CDC (Código de Defesa do Consumidor — Lei 8.078/1990)

**Escopo**: Aplica-se a relações de consumo entre fornecedores e consumidores (pessoas físicas ou jurídicas que adquirem produtos/serviços como destinatários finais).

**Obrigações-Chave**:
- **Informação clara e adequada**: Dever de informar sobre características, riscos e condições de produtos e serviços
- **Vedação à publicidade enganosa e abusiva**: Toda comunicação de marketing deve ser verificável e não induzir o consumidor a erro
- **Direito de arrependimento**: 7 dias para desistência em compras fora do estabelecimento comercial (ex.: e-commerce), com devolução integral dos valores
- **Responsabilidade objetiva**: Fornecedores respondem independentemente de culpa por danos causados por defeitos de produtos/serviços
- **Cláusulas abusivas**: Nulas de pleno direito (art. 51) — vedado, por exemplo, transferir responsabilidades ao consumidor de forma iníqua
- **Garantia legal**: 30 dias (bens não duráveis) ou 90 dias (bens duráveis) para reclamar de vícios aparentes

**Prazos de Resposta Típicos**:
- Atendimento ao SAC: imediato a razoável, conforme regulamentação setorial
- Procon: prazos variam por estado, geralmente 10 dias úteis para resposta inicial

### CLT (Consolidação das Leis do Trabalho) — Quando Há Componente Trabalhista

**Escopo**: Aplica-se a relações de emprego regidas pela legislação trabalhista brasileira.

**Obrigações-Chave**:
- **Registro e documentação**: Carteira de trabalho digital, contrato de trabalho, jornada
- **Direitos trabalhistas**: Férias, 13º salário, FGTS, aviso prévio, horas extras
- **Compliance em rescisões**: Verbas rescisórias, homologação quando aplicável
- **Terceirização**: Observar Lei 13.429/2017 e Súmula 331 do TST quanto a responsabilidade subsidiária

### Lei 14.133/2021 (Nova Lei de Licitações) — Quando Há Componente de Contratação Pública

**Escopo**: Aplica-se a contratações públicas e licitações com a Administração Pública.

**Obrigações-Chave**:
- Modalidades de licitação (pregão, concorrência, diálogo competitivo, etc.)
- Exigências de habilitação jurídica, fiscal, técnica e econômico-financeira
- Vedações a conflito de interesse e nepotismo
- Regras de execução e fiscalização contratual

### Outras Regulações Relevantes a Monitorar

| Regulação | Âmbito | Principais Diferenciais |
|---|---|---|
| **Marco Civil da Internet** (Lei 12.965/2014) | Brasil | Neutralidade de rede, guarda de registros de conexão e acesso, responsabilidade de provedores |
| **GDPR** (UE) | Europa | Referência comparativa para empresas com operação na UE; exige DPO e SCCs para transferência |
| **CCPA/CPRA** (EUA, Califórnia) | EUA | Relevante para empresas com clientes/usuários californianos |
| **Lei do Cadastro Positivo** (Lei 12.414/2011) | Brasil | Regras específicas para tratamento de dados de crédito |
| **Resoluções do Banco Central / CVM** | Brasil | Relevante para empresas do setor financeiro |
| **ANVISA** | Brasil | Relevante para produtos de saúde, cosméticos, alimentos |

## Checklist de Revisão de Contrato de Operação de Dados (LGPD)

Ao revisar um Contrato ou Adendo de Tratamento/Operação de Dados, verifique os seguintes pontos:

### Elementos Obrigatórios (alinhados ao art. 39 da LGPD e boas práticas)

- [ ] **Objeto e duração**: Escopo e prazo do tratamento claramente definidos
- [ ] **Natureza e finalidade**: Descrição específica de que tratamento ocorrerá e por quê
- [ ] **Tipo de dado pessoal**: Categorias de dados pessoais tratados (incluindo dados sensíveis, se houver)
- [ ] **Categorias de titulares**: De quem são os dados pessoais tratados
- [ ] **Obrigações e direitos do controlador**: Instruções e direitos de fiscalização do controlador

### Obrigações do Operador

- [ ] **Tratar apenas conforme instruções documentadas**: O operador se compromete a tratar os dados apenas conforme as instruções do controlador (com exceção para exigências legais)
- [ ] **Confidencialidade**: Pessoal autorizado a tratar os dados firmou compromisso de confidencialidade
- [ ] **Medidas de segurança**: Medidas técnicas e administrativas adequadas descritas (referência ao art. 46 da LGPD)
- [ ] **Exigências de suboperador**:
  - [ ] Exigência de autorização por escrito (geral ou específica)
  - [ ] Se autorização geral: notificação de mudanças com oportunidade de objeção
  - [ ] Suboperadores vinculados às mesmas obrigações via contrato escrito
  - [ ] Operador permanece responsável pela atuação do suboperador
- [ ] **Apoio aos direitos dos titulares**: O operador apoiará o controlador em responder solicitações de titulares
- [ ] **Apoio em segurança e incidentes**: O operador apoiará nas obrigações de segurança, notificação de incidente e RIPD, quando aplicável
- [ ] **Eliminação ou devolução**: Ao término, eliminar ou devolver todos os dados pessoais (à escolha do controlador) e eliminar cópias existentes, salvo retenção legal exigida
- [ ] **Direitos de auditoria**: Controlador tem direito de realizar auditorias e inspeções (ou aceitar relatórios de auditoria de terceiros)
- [ ] **Notificação de incidente**: O operador notificará o controlador sobre incidentes de segurança sem demora indevida (idealmente em 24-48h, para permitir que o controlador cumpra seu próprio dever de comunicação à ANPD)

### Transferências Internacionais

- [ ] **Mecanismo de transferência identificado**: Cláusulas-padrão contratuais, decisão de adequação da ANPD, normas corporativas globais, certificação, selo, ou outro mecanismo válido (art. 33 da LGPD)
- [ ] **Avaliação de impacto da transferência**: Concluída quando a transferência for para país sem decisão de adequação
- [ ] **Medidas suplementares**: Medidas técnicas, organizacionais ou contratuais para tratar lacunas identificadas na avaliação
- [ ] **Coerência com GDPR/SCCs**, se o fornecedor também opera na UE (uso de cláusulas-padrão da UE de 2021, quando aplicável)

### Considerações Práticas

- [ ] **Responsabilidade civil**: As disposições de responsabilidade no contrato de dados estão alinhadas (ou não conflitam) com o contrato principal de serviços
- [ ] **Alinhamento de prazo**: O prazo do contrato de dados está alinhado ao contrato de serviços
- [ ] **Localização dos dados**: Locais de processamento especificados e aceitáveis
- [ ] **Padrões de segurança**: Padrões ou certificações de segurança específicos exigidos (SOC 2, ISO 27001, ISO 27701, etc.)
- [ ] **Seguro**: Cobertura de seguro adequada para atividades de tratamento de dados

### Problemas Comuns em Contratos de Operação de Dados

| Problema | Risco | Posição Padrão |
|---|---|---|
| Autorização genérica de suboperador sem notificação | Perda de controle sobre a cadeia de tratamento | Exigir notificação com direito de objeção |
| Prazo de notificação de incidente muito longo | Pode impedir comunicação tempestiva à ANPD | Exigir notificação em 24-48h |
| Ausência de direitos de auditoria (ou só via relatórios de terceiros) | Impossibilidade de verificar conformidade | Aceitar SOC 2 Tipo II + direito de auditoria mediante causa |
| Prazo de eliminação de dados não especificado | Dados retidos indefinidamente | Exigir eliminação em 30-90 dias após o término |
| Locais de processamento não especificados | Dados podem ser processados em qualquer lugar | Exigir divulgação dos locais de processamento |
| Ausência de previsão de transferência internacional | Mecanismo de transferência inválido | Exigir cláusulas-padrão ou outro mecanismo do art. 33 da LGPD |

## Atendimento a Solicitações de Titulares de Dados (LGPD)

### Recebimento da Solicitação

Ao receber uma solicitação de titular de dados:

1. **Identifique o tipo de solicitação**:
   - Acesso (cópia dos dados pessoais)
   - Retificação (correção de dados desatualizados ou incorretos)
   - Eliminação / anonimização de dados desnecessários ou excessivos
   - Portabilidade (formato estruturado e interoperável)
   - Informação sobre compartilhamento de dados com terceiros
   - Revogação do consentimento
   - Oposição a tratamento realizado com base em hipótese irregular de tratamento

2. **Identifique a regulação aplicável**:
   - Onde o titular está localizado?
   - A LGPD se aplica com base na presença e nas atividades da organização?
   - Outra regulação concorre (ex.: GDPR para titulares na UE)?

3. **Verifique a identidade**:
   - Confirme que o solicitante é quem afirma ser
   - Use medidas de verificação razoáveis e proporcionais à sensibilidade dos dados
   - Não exija documentação excessiva

4. **Registre a solicitação**:
   - Data de recebimento
   - Tipo de solicitação
   - Identidade do solicitante
   - Regulação aplicável
   - Prazo de resposta
   - Responsável designado

### Prazos de Resposta

| Regulação | Confirmação Inicial | Resposta Substantiva | Prorrogação |
|---|---|---|---|
| LGPD | Imediata (boa prática) | 15 dias (art. 19, §3º, para confirmação de existência de tratamento) | Possível, mediante justificativa |
| GDPR (se aplicável) | Não especificado (boa prática: prontamente) | 30 dias | +60 dias (com aviso) |

### Isenções e Exceções

Antes de atender a uma solicitação, verifique se há isenções aplicáveis:

**Isenções comuns sob a LGPD**:
- Cumprimento de obrigação legal ou regulatória pelo controlador
- Exercício regular de direitos em processo judicial, administrativo ou arbitral
- Proteção da vida ou da incidência física do titular ou de terceiro
- Tutela da saúde, em procedimento realizado por profissionais de saúde
- Garantia da prevenção à fraude e à segurança do titular

**Considerações específicas da organização**:
- Retenção para defesa em processo: dados sujeitos a obrigação de retenção para defesa em processo judicial não podem ser eliminados
- Retenção regulatória: registros financeiros, trabalhistas e outras categorias podem ter prazos de retenção obrigatórios
- Direitos de terceiros: atender à solicitação pode afetar adversamente direitos de terceiros

### Processo de Resposta

1. Reúna todos os dados pessoais do solicitante em todos os sistemas
2. Aplique quaisquer isenções e documente a base legal
3. Prepare a resposta: atenda à solicitação ou explique por que (no todo ou em parte) ela não pode ser atendida
4. Em caso de negativa (total ou parcial): cite a base legal específica para a negativa
5. Informe ao solicitante seu direito de peticionar à ANPD
6. Documente a resposta e mantenha registros da solicitação e da resposta

## Fundamentos de Monitoramento Regulatório

### O Que Monitorar

Mantenha-se atualizado sobre desenvolvimentos em:
- **Orientações regulatórias**: Novos ou atualizados guias de órgãos reguladores (ANPD, Procons, Banco Central, CVM, ANVISA, agências setoriais)
- **Ações de fiscalização**: Multas, autuações e acordos que sinalizam prioridades regulatórias (especialmente decisões da ANPD)
- **Mudanças legislativas**: Novas leis de privacidade/consumidor/trabalhista, emendas a leis existentes, regulamentações infralegais
- **Padrões da indústria**: Atualizações em ISO 27001, ISO 27701, frameworks setoriais
- **Desenvolvimentos sobre transferência internacional**: Decisões de adequação, atualizações de cláusulas-padrão, exigências de localização de dados

### Abordagem de Monitoramento

1. **Inscreva-se em comunicações de órgãos reguladores** (newsletters, RSS, comunicados oficiais da ANPD)
2. **Acompanhe publicações jurídicas relevantes** para análise de novos desenvolvimentos (Migalhas, JOTA, Conjur)
3. **Revise atualizações de associações setoriais** para orientação específica do setor
4. **Mantenha um calendário regulatório** com prazos conhecidos, datas de vigência e marcos de compliance
5. **Informe a equipe jurídica** sobre desenvolvimentos materiais que afetem as atividades de tratamento da organização

### Critérios de Escalonamento

Escale desenvolvimentos regulatórios para a consultoria sênior ou liderança quando:
- Uma nova regulação ou orientação afeta diretamente as atividades-core do negócio
- Uma ação de fiscalização no setor da organização sinaliza maior escrutínio regulatório
- Um prazo de compliance está se aproximando e exige mudanças organizacionais
- Um mecanismo de transferência de dados em que a organização confia é contestado ou invalidado
- A ANPD ou outro órgão regulador inicia uma consulta ou investigação envolvendo a organização

## Dicas

1. **Seja específico** — "Queremos enviar e-mail para todos os usuários" é melhor que "campanha de marketing".
2. **Inclua a geografia** — As exigências de compliance variam por jurisdição (estado, país).
3. **Mencione os dados** — Quais dados pessoais estão envolvidos? Isso direciona a maior parte das exigências de compliance.
