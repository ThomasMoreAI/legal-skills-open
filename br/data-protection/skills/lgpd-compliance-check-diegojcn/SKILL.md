---
name: lgpd-compliance-check-diegojcn
title: Lgpd Compliance Check
description: Lgpd Compliance Check — Skill especializada para lgpd compliance check
author: diegojcn
author_url: https://github.com/diegojcn/agent-skill-pack/tree/main/juridico-compliance/lgpd-compliance-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Lgpd Compliance Check

Esta skill capacita o Claude a realizar verificações detalhadas de conformidade com a Lei Geral de Proteção de Dados Pessoais (LGPD), avaliando processos, documentos e tecnologias de uma organização.

---

## Keywords

LGPD, compliance, proteção de dados, privacidade, DPO, ANPD, tratamento de dados, consentimento, mapeamento de dados, avaliação de impacto, DPIA, revisão de contratos, incidentes de segurança, direitos do titular, termos de uso, política de privacidade.

---

## Quick Start

1.  **Inventariar Dados Pessoais Processados**: Liste todos os tipos de dados pessoais que sua organização coleta, armazena, processa e compartilha (ex: CPF, e-mail, histórico de compras).
2.  **Identificar Bases Legais**: Para cada finalidade de tratamento de dados, determine a base legal aplicável (ex: consentimento, execução de contrato, legítimo interesse).
3.  **Verificar Medidas de Segurança**: Avalie se as medidas técnicas e organizacionais de segurança da informação estão adequadas aos riscos do tratamento (ex: criptografia, controle de acesso).
4.  **Revisar Termos de Uso/Política de Privacidade**: Confirme se os documentos públicos informam de forma clara e acessível sobre o tratamento de dados e os direitos dos titulares.
5.  **Validar Processos de Atendimento a Titulares**: Assegure que existem canais e procedimentos eficazes para atender solicitações de acesso, correção ou exclusão de dados.

---

## Core Workflows

### Workflow 1: Avaliação de Conformidade para Mapeamento de Dados e Bases Legais

Este workflow guia a organização no mapeamento completo do ciclo de vida dos dados pessoais e na validação das bases legais que justificam cada tratamento, garantindo transparência e legalidade.

1.  **Levantamento de Ativos e Sistemas**:
    *   **Ação**: Crie uma lista detalhada de todos os sistemas, bancos de dados, planilhas e plataformas (CRM, ERP, e-commerce, RH) que manipulam dados pessoais.
    *   **Exemplo**: CRM (Salesforce), ERP (SAP), Plataforma de E-mail Marketing (Mailchimp), Servidor de RH (ADP), Site Institucional (WordPress).
2.  **Inventário de Dados Pessoais por Ativo**:
    *   **Ação**: Para cada ativo levantado, liste os tipos específicos de dados pessoais coletados e as finalidades de tratamento.
    *   **Exemplo**:
        *   **CRM (Salesforce)**: Nome completo, CPF, e-mail, telefone, histórico de compras, endereço de entrega. Finalidade: Gestão de relacionamento com cliente, vendas, pós-venda.
        *   **Servidor de RH (ADP)**: Nome completo, CPF, PIS, endereço, salário, dados bancários, exames médicos, histórico profissional. Finalidade: Gestão de folha de pagamento, benefícios, recrutamento.
3.  **Identificação de Agentes de Tratamento e Fluxos de Dados**:
    *   **Ação**: Determine quem é o Controlador e Operador em cada cenário e como os dados fluem entre eles e terceiros.
    *   **Exemplo**: Para dados de e-mail marketing, a empresa é o Controlador e a Mailchimp é o Operador. Os dados fluem do CRM para a Mailchimp via integração API.
4.  **Associação de Bases Legais**:
    *   **Ação**: Para cada finalidade de tratamento e tipo de dado, identifique a base legal apropriada do Art. 7º e Art. 11 da LGPD.
    *   **Exemplo**:
        *   **Finalidade**: Envio de newsletters. **Dados**: E-mail. **Base Legal**: Consentimento (Art. 7º, I).
        *   **Finalidade**: Processamento de pagamento de um produto. **Dados**: Dados bancários, CPF. **Base Legal**: Execução de contrato (Art. 7º, V).
        *   **Finalidade**: Cumprimento de obrigações fiscais. **Dados**: CPF, dados de faturamento. **Base Legal**: Cumprimento de obrigação legal ou regulatória (Art. 7º, II).
5.  **Documentação do Mapeamento**:
    *   **Ação**: Crie um registro formal do mapeamento, preferencialmente em uma planilha ou software específico, detalhando os itens acima.
    *   **Exemplo**: Planilha com colunas: "Ativo", "Dados Pessoais", "Finalidade", "Base Legal", "Agente de Tratamento", "Terceiros Envolvidos", "Local de Armazenamento".

### Workflow 2: Revisão de Contratos e Documentos Legais para LGPD

Este workflow foca na análise e adequação de contratos com terceiros (fornecedores, parceiros) e documentos públicos (termos de uso, políticas de privacidade) para garantir que refletem as exigências da LGPD.

1.  **Inventário de Contratos Relevantes**:
    *   **Ação**: Liste todos os contratos com fornecedores, clientes, parceiros e prestadores de serviço que envolvam compartilhamento ou tratamento de dados pessoais.
    *   **Exemplo**: Contrato de serviço de hospedagem de dados, contrato com agência de marketing digital, contrato com provedor de sistema de RH, termos de parceria com e-commerce.
2.  **Análise de Cláusulas de Proteção de Dados Existentes**:
    *   **Ação**: Revise cada contrato para identificar se já existem cláusulas de proteção de dados e se elas são adequadas à LGPD.
    *   **Exemplo**: Verifique se o contrato de hospedagem menciona a responsabilidade do Operador, medidas de segurança e notificação de incidentes.
3.  **Inserção ou Adequação de Cláusulas LGPD (DPA)**:
    *   **Ação**: Para contratos sem cláusulas adequadas, negocie e insira um Aditivo de Proteção de Dados (DPA) ou cláusulas específicas que contemplem as obrigações do Controlador e Operador.
    *   **Exemplo**: Adicionar cláusula que especifica a finalidade do tratamento de dados pelo Operador, a obrigação de sigilo, a adoção de medidas de segurança e a cooperação em caso de incidentes.
4.  **Revisão de Termos de Uso e Políticas de Privacidade**:
    *   **Ação**: Avalie se os Termos de Uso e a Política de Privacidade do site/aplicativo são claros, acessíveis e completos, conforme Art. 9º e Art. 18 da LGPD.
    *   **Exemplo**:
        *   **Política de Privacidade**: Verificar se informa quais dados são coletados, para quais finalidades, com quem são compartilhados, por quanto tempo são retidos e quais os direitos do titular.
        *   **Termos de Uso**: Assegurar que há link visível para a Política de Privacidade e, se aplicável, termos de consentimento para usos específicos de dados.
5.  **Verificação de Mecanismos de Consentimento**:
    *   **Ação**: Confirme se os mecanismos de obtenção de consentimento (ex: checkboxes em formulários) são livres, informados, inequívocos e revogáveis.
    *   **Exemplo**: Checkbox não pré-marcado para "Receber comunicações de marketing", com link para a política de privacidade e opção clara de descadastro.

---

## Templates

### Cláusula Contratual de Proteção de Dados (B2B - Aditivo DPA)

```
**ADITIVO DE PROTEÇÃO DE DADOS PESSOAIS**

**CLÁUSULA PRIMEIRA – OBJETO E ABRANGÊNCIA**
1.1. O presente Aditivo tem por objeto estabelecer as condições para o tratamento de dados pessoais realizado pelo **OPERADOR** em nome do **CONTROLADOR**, no âmbito do Contrato Principal de [Descrever o Contrato Principal, ex: Prestação de Serviços de Marketing Digital], com estrita observância à Lei nº 13.709/2018 – Lei Geral de Proteção de Dados Pessoais (LGPD).
1.2. Para os fins deste Aditivo, os termos "dados pessoais", "tratamento", "controlador" e "operador" terão o significado atribuído pela LGPD.

**CLÁUSULA SEGUNDA – OBRIGAÇÕES DO OPERADOR**
2.1. O OPERADOR tratará os dados pessoais fornecidos pelo CONTROLADOR exclusivamente para as finalidades especificadas no Contrato Principal e nas instruções documentadas pelo CONTROLADOR, sendo vedado o tratamento para outras finalidades.
2.2. O OPERADOR implementará e manterá medidas de segurança técnicas e administrativas aptas a proteger os dados pessoais de acessos não autorizados e de situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou qualquer forma de tratamento inadequado ou ilícito.
2.3. O OPERADOR notificará o CONTROLADOR, sem demora injustificada e, se possível, em até 24 (vinte e quatro) horas após tomar conhecimento, sobre qualquer incidente de segurança que possa implicar risco ou dano relevante aos titulares dos dados pessoais, fornecendo informações detalhadas sobre a natureza do incidente, os dados afetados e as medidas adotadas ou propostas.
2.4. O OPERADOR não compartilhará os dados pessoais com terceiros sem prévia e expressa autorização por escrito do CONTROLADOR, exceto se exigido por lei. Em caso de subcontratação, o OPERADOR garantirá que o subcontratado esteja sujeito às mesmas obrigações de proteção de dados aqui estabelecidas.
2.5. Ao término da prestação dos serviços que envolvem o tratamento de dados pessoais, o OPERADOR deverá, a critério do CONTROLADOR, eliminar ou devolver todos os dados pessoais, salvo se houver obrigação legal de retenção.

**CLÁUSULA TERCEIRA – OBRIGAÇÕES DO CONTROLADOR**
3.1. O CONTROLADOR declara e garante que possui base legal adequada, conforme a LGPD, para o tratamento dos dados pessoais que compartilha com o OPERADOR e que os dados são coletados de forma lícita e transparente.
3.2. O CONTROLADOR é o único responsável pela veracidade, exatidão e atualização dos dados pessoais fornecidos ao OPERADOR.

**CLÁUSULA QUARTA – DISPOSIÇÕES FINAIS**
4.1. Este Aditivo é parte integrante e indissociável do Contrato Principal, prevalecendo suas disposições em caso de conflito com este último no que concerne à proteção de dados pessoais.
```

### Item de Política de Privacidade (Dados Coletados e Finalidades)

```
**POLÍTICA DE PRIVACIDADE**

**1. QUAIS DADOS COLETAMOS E PARA QUAIS FINALIDADES?**

Coletamos diferentes tipos de dados pessoais, dependendo da sua interação com nossos serviços e da finalidade específica. Abaixo, detalhamos os dados que podemos coletar e os motivos:

*   **Dados de Identificação e Contato**:
    *   **Exemplos**: Nome completo, CPF, RG, endereço de e-mail, número de telefone, endereço residencial e comercial.
    *   **Finalidade**: Cadastro em nosso site/plataforma, emissão de notas fiscais, entrega de produtos/serviços, comunicação sobre seu pedido, atendimento ao cliente, envio de newsletters e comunicações de marketing (com seu consentimento).
    *   **Base Legal**: Execução de contrato, cumprimento de obrigação legal, consentimento.

*   **Dados de Pagamento**:
    *   **Exemplos**: Dados de cartão de crédito (número, validade, código de segurança – estes últimos são criptografados e não armazenados diretamente por nós), dados bancários para transferências.
    *   **Finalidade**: Processamento de pagamentos para compras de produtos ou serviços.
    *   **Base Legal**: Execução de contrato, cumprimento de obrigação legal.

*   **Dados de Navegação e Dispositivo**:
    *   **Exemplos**: Endereço IP, tipo de navegador, sistema operacional, páginas visitadas, tempo de permanência, cliques, dados de localização (se ativado).
    *   **Finalidade**: Melhoria da experiência do usuário, análise de tráfego, personalização de conteúdo, detecção e prevenção de fraudes, publicidade direcionada.
    *   **Base Legal**: Legítimo interesse, consentimento (para cookies não essenciais).

*   **Dados de Comunicação**:
    *   **Exemplos**: Conteúdo de e-mails, mensagens de chat, gravações de chamadas (quando aplicável).
    *   **Finalidade**: Atendimento ao cliente, suporte técnico, melhoria da qualidade do serviço, resolução de disputas.
    *   **Base Legal**: Legítimo interesse, execução de contrato.

*   **Dados Sensíveis (quando aplicável e com consentimento explícito)**:
    *   **Exemplos**: Dados de saúde (para seguros específicos ou programas de bem-estar), dados biométricos (para acesso a sistemas de alta segurança).
    *   **Finalidade**: Fornecimento de serviços específicos que exigem tais dados, cumprimento de exigências legais ou regulatórias.
    *   **Base Legal**: Consentimento explícito do titular ou outras bases legais do Art. 11 da LGPD.
```

---

## Checklist

- [X] Mapeamento completo dos dados pessoais coletados e processados.
- [X] Identificação e documentação das bases legais para todas as finalidades de tratamento.
- [X] Análise de riscos e implementação de medidas de segurança (técnicas e administrativas) adequadas.
- [X] Existência de Política de Privacidade e Termos de Uso claros, acessíveis e atualizados.
- [X] Mecanismos de obtenção de consentimento explícito, livre e informado, quando aplicável.
- [X] Processos definidos para atendimento às solicitações dos titulares de dados (DSARs).
- [X] Contratos com terceiros (Operadores) contendo cláusulas de proteção de dados conforme LGPD (DPA).
- [X] Designação de um Encarregado de Dados (DPO) e divulgação de seu contato.
- [X] Plano de resposta a incidentes de segurança de dados pessoais documentado e testado.
- [X] Realização de Relatório de Impacto à Proteção de Dados Pessoais (DPIA) para operações de alto risco.

---

## Métricas de Referência

| Métrica                                   | Benchmark (Médio) | Meta (Ideal) |
|-------------------------------------------|-------------------|--------------|
| Tempo médio de resposta a DSARs           | 15 dias           | 7 dias       |
| % de contratos com DPA/Cláusulas LGPD     | 80%               | 100%         |
| % de incidentes de segurança reportados à ANPD no prazo | 70%               | 95%          |
| % de colaboradores treinados em LGPD      | 90%               | 100%         |
| Frequência de Revisão da Política de Privacidade | Anual             | Semestral    |

---

## Erros Comuns

1.  **Não mapear todos os fluxos de dados**: Muitas organizações focam apenas em dados de clientes, esquecendo dados de funcionários, fornecedores ou dados coletados via cookies.
    *   **Como evitar**: Realize um levantamento abrangente, entrevistando diferentes áreas (RH, Marketing, TI, Vendas, Financeiro) e auditando todos os sistemas e planilhas, como "inventário de dados de folha de pagamento" ou "log de acesso de usuários em sistemas internos".
2.  **Coletar dados excessivos para a finalidade**: Solicitar o CPF ou endereço completo para uma simples inscrição em newsletter é um exemplo clássico de coleta desnecessária.
    *   **Como evitar**: Aplique o princípio da minimização de dados. Para uma newsletter, apenas o e-mail geralmente é suficiente. Para um orçamento, solicite apenas o essencial para a proposta (ex: nome da empresa, contato, descrição do projeto).
3.  **Não ter um DPO (Encarregado) designado ou com contato inacessível**: A LGPD exige a nomeação de um DPO e a divulgação de seu contato em local de fácil acesso (ex: site, política de privacidade).
    *   **Como evitar**: Nomeie formalmente um DPO (interno ou externo) e garanta que o e-mail "dpo@suaempresa.com.br" esteja visível no rodapé do site e na Política de Privacidade, como "Para dúvidas ou solicitações sobre seus dados pessoais, entre em contato com nosso Encarregado (DPO) através do e-mail dpo@suaempresa.com.br.".

---

## Dicas Avançadas

1.  **Implementar Privacy by Design e by Default**: Garanta que a proteção de dados seja incorporada desde o design de novos produtos, serviços ou sistemas, e que as configurações padrão sejam as mais protetivas à privacidade.
    *   **Exemplo Prático**: Ao desenvolver um novo aplicativo, projete-o para coletar o mínimo de dados necessários e ofereça opções de privacidade granular aos usuários desde o primeiro acesso, como "desativar compartilhamento de localização" ou "ocultar perfil de busca".
2.  **Gestão de Consentimento Granular**: Para situações que exigem consentimento, ofereça ao titular a possibilidade de consentir para finalidades específicas, e não apenas um "aceito tudo".
    *   **Exemplo Prático**: Em um formulário de cadastro, em vez de um único checkbox "Aceito a Política de Privacidade", ofereça: "[ ] Aceito receber newsletters", "[ ] Aceito participar de pesquisas de mercado", cada um com link para as respectivas finalidades.
3.  **Realizar DPIA (Relatório de Impacto à Proteção de Dados Pessoais) proativamente**: Para projetos que envolvam alto risco à privacidade (ex: uso de inteligência artificial com dados pessoais, monitoramento de funcionários, grande volume de dados sensíveis), realize um DPIA antes da implementação.
    *   **Exemplo Prático**: Antes de lançar um novo sistema de reconhecimento facial para controle de acesso, conduza um DPIA completo para identificar e mitigar riscos de segurança e privacidade.
4.  **Auditoria Regular de Terceiros**: Não basta ter o DPA assinado; audite periodicamente seus Operadores para garantir que eles estão cumprindo as obrigações de proteção de dados.
    *   **Exemplo Prático**: Inclua em seus contratos com fornecedores de TI a possibilidade de realizar auditorias de segurança de dados anuais e solicite relatórios de conformidade (ex: SOC 2, ISO 27001).
5.  **Simulações de Incidentes (Tabletop Exercises)**: Realize exercícios simulados de resposta a incidentes de segurança de dados para testar a eficácia do seu plano e treinar sua equipe.
    *   **Exemplo Prático**: Simule um vazamento de e-mails de clientes e avalie como a equipe de TI, jurídico e comunicação reage, desde a detecção até a comunicação com a ANPD e os titulares.
