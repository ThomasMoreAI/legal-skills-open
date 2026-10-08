<!--
TEMPLATE: CLÁUSULAS DE PROTEÇÃO DE DADOS (DPA) EM CONTRATO BRASILEIRO
========================================================================
Para incluir em contrato controlador↔operador (CONTROLADOR contrata OPERADOR
que processará dados pessoais em nome do CONTROLADOR), em conformidade com
a LGPD (Lei 13.709/2018).

Placeholders:
  {{CONTROLADOR_NOME}}, {{OPERADOR_NOME}}, {{OBJETO}}
  {{PRAZO_INCIDENTE}}   , 24h se quer prazo apertado; 48h padrão de mercado
  {{LISTA_SUBPROCESSADORES}}
-->

# Anexo: Cláusulas de Proteção de Dados Pessoais (LGPD)

Este Anexo integra o contrato firmado entre **{{CONTROLADOR_NOME}}** (doravante "**Controlador**") e **{{OPERADOR_NOME}}** (doravante "**Operador**"), e regula o tratamento de Dados Pessoais realizado pelo Operador em nome do Controlador no âmbito de **{{OBJETO}}**.

Em caso de conflito entre este Anexo e o corpo do Contrato, prevalecem as disposições deste Anexo no que diz respeito ao tratamento de Dados Pessoais.

## 1. Definições

Os termos aqui empregados em maiúscula seguem as definições do art. 5º da **Lei nº 13.709/2018 (LGPD)**, em especial: Dado Pessoal, Dado Pessoal Sensível, Titular, Controlador, Operador, Encarregado, Tratamento, Anonimização, ANPD, Transferência Internacional, Incidente de Segurança.

## 2. Objeto e Finalidade

2.1. O Operador realizará Tratamento de Dados Pessoais **exclusivamente** para as finalidades descritas no Contrato e nas instruções documentadas do Controlador.

2.2. Categorias de Dados Pessoais tratadas, categorias de Titulares, natureza e finalidade específica do Tratamento estão descritas no **Apêndice 1** deste Anexo.

2.3. O Operador é vedado de tratar os Dados Pessoais para finalidade própria ou diversa da contratada.

## 3. Papéis e Responsabilidades

3.1. O Controlador é o agente responsável pelas decisões referentes ao Tratamento (art. 5º, VI, LGPD).

3.2. O Operador realiza o Tratamento em nome e segundo instruções do Controlador (art. 5º, VII, LGPD).

3.3. O Operador responderá solidariamente nos termos do art. 42 §1º II da LGPD caso descumpra as obrigações da LGPD ou as instruções lícitas do Controlador.

## 4. Instruções e Confidencialidade

4.1. O Operador tratará Dados Pessoais **apenas mediante instrução documentada** do Controlador, incluindo Transferências Internacionais.

4.2. Caso entenda que uma instrução viola a LGPD, o Operador deve **comunicar imediatamente** o Controlador.

4.3. O Operador garantirá que pessoas autorizadas a tratar os Dados estejam vinculadas a **dever de confidencialidade**.

## 5. Segurança da Informação (art. 46-49 LGPD)

5.1. O Operador adotará medidas técnicas e administrativas aptas a proteger os Dados Pessoais de acesso não autorizado, situações acidentais ou ilícitas de destruição, perda, alteração, comunicação ou difusão.

5.2. Medidas mínimas obrigatórias:

- **a)** Criptografia em trânsito (TLS 1.2 ou superior) e em repouso;
- **b)** Controle de acesso baseado em menor privilégio + autenticação multifator para acessos administrativos;
- **c)** Logs de auditoria com retenção mínima de 12 meses;
- **d)** Gestão de vulnerabilidades com correção tempestiva de CVEs críticas;
- **e)** Backups regulares, criptografados, armazenados em local distinto e testados periodicamente;
- **f)** Programa documentado de gestão de incidentes;
- **g)** Treinamento regular dos colaboradores em proteção de dados.

5.3. O Operador disponibilizará, mediante solicitação razoável, evidências de conformidade (relatórios de auditoria, certificações ISO 27001 / SOC 2, resultados de pentest sanitizados).

## 6. Incidentes de Segurança (art. 48 LGPD + Res. CD/ANPD nº 15/2024)

6.1. O Operador comunicará por escrito ao Controlador **qualquer Incidente de Segurança** envolvendo Dados Pessoais tratados em nome do Controlador, em prazo **não superior a {{PRAZO_INCIDENTE}}** contado da ciência.

6.2. A comunicação conterá, no mínimo:

- natureza e categoria dos Dados afetados;
- número aproximado de Titulares;
- consequências adversas conhecidas ou potenciais;
- medidas adotadas para contenção;
- medidas planejadas para mitigação;
- ponto de contato técnico.

6.3. O Operador cooperará integralmente com o Controlador na investigação, comunicação aos Titulares e à ANPD, e nas medidas de remediação. O ônus da comunicação à ANPD é do Controlador, salvo disposição expressa em contrário.

## 7. Direitos dos Titulares (art. 18 LGPD)

7.1. O Operador auxiliará o Controlador no atendimento de requisições de Titulares, fornecendo, dentro de **5 dias úteis** da solicitação, as informações e ações técnicas necessárias.

7.2. Caso o Operador receba diretamente requisição de Titular, comunicará imediatamente o Controlador, **sem responder ao Titular** salvo orientação expressa.

## 8. Subprocessadores

8.1. O Operador poderá engajar subprocessadores para o Tratamento, mediante:

- **a)** comunicação prévia ao Controlador com pelo menos **30 dias** de antecedência da alteração da lista, exceto em casos de emergência justificada;
- **b)** vinculação dos subprocessadores às mesmas obrigações deste Anexo;
- **c)** responsabilidade do Operador pelo cumprimento das obrigações pelo subprocessador.

8.2. Lista atual de subprocessadores: **{{LISTA_SUBPROCESSADORES}}**.

8.3. O Controlador poderá se opor justificadamente a novo subprocessador. Persistindo a oposição, qualquer das partes poderá rescindir a parcela contratual impactada sem multa.

## 9. Transferência Internacional (art. 33 LGPD + Res. CD/ANPD nº 19/2024)

9.1. Caso o Tratamento envolva Transferência Internacional, esta se baseará em:

- **a)** Cláusulas-Padrão Contratuais aprovadas pela ANPD (**Apêndice 2** deste Anexo), OU
- **b)** outra garantia adequada prevista no art. 33 da LGPD, conforme aplicável.

9.2. Os países e territórios de destino estão indicados no **Apêndice 1**.

## 10. Auditoria

10.1. O Controlador, mediante aviso prévio razoável (mínimo 30 dias) e durante horário comercial, poderá auditar (diretamente ou por terceiro independente sob NDA) o cumprimento deste Anexo pelo Operador.

10.2. O Operador pode atender solicitações de auditoria mediante apresentação de certificações reconhecidas (ISO 27001, SOC 2 Tipo II, etc.) com escopo compatível, ressalvado o direito do Controlador a auditoria *on-site* em caso de Incidente confirmado.

10.3. Custos de auditoria são do Controlador, salvo se a auditoria identificar não-conformidade material, hipótese em que o Operador arcará com os custos.

## 11. Retenção e Eliminação

11.1. Ao término da prestação dos serviços, o Operador, conforme instrução do Controlador, **eliminará** ou **devolverá** todos os Dados Pessoais, em até **30 dias** do encerramento, salvo dever legal de retenção (Marco Civil, fiscal, etc.) que será comunicado ao Controlador.

11.2. O Operador fornecerá comprovante de eliminação irreversível ao Controlador.

## 12. Apoio ao Controlador

12.1. O Operador apoiará o Controlador, mediante solicitação razoável, em:

- elaboração e atualização do ROPA (art. 37);
- elaboração de RIPD/DPIA (art. 38);
- consultas e fiscalizações da ANPD;
- demonstração de conformidade exigida por terceiros.

## 13. Responsabilidade

13.1. As partes respondem civilmente, nos termos dos arts. 42 a 45 da LGPD, pelos danos causados por sua atuação.

13.2. O Operador indenizará o Controlador por prejuízos decorrentes do descumprimento deste Anexo, inclusive multas e medidas administrativas aplicadas ao Controlador por causa imputável ao Operador.

## 14. Vigência

14.1. Este Anexo permanece em vigor enquanto durar o Contrato e enquanto o Operador detiver Dados Pessoais do Controlador.

14.2. As obrigações de confidencialidade, segurança, comunicação de incidente e eliminação **sobrevivem** ao término do Contrato.

## 15. Disposições Finais

15.1. Este Anexo é regido pela legislação brasileira, em especial pela LGPD.

15.2. Foro: comarca de **{{FORO_CIDADE}}**, **{{FORO_UF}}**, com renúncia a qualquer outro.

---

## Apêndice 1: Detalhamento do Tratamento

| | |
|---|---|
| Objeto | {{OBJETO}} |
| Categorias de Dados | {{...}} |
| Categorias de Titulares | {{...}} |
| Natureza e finalidade | {{...}} |
| Duração | {{...}} |
| Locais de processamento | {{...}} |

## Apêndice 2: Cláusulas-Padrão Contratuais (SCC) da ANPD

Caso aplicável, as **Cláusulas-Padrão Contratuais** aprovadas pela ANPD para Transferência Internacional integram este Anexo por referência, conforme **Resolução CD/ANPD nº 19/2024**.

[Anexar texto integral das SCC publicadas pela ANPD ao contrato.]

---

**Assinaturas**

| | |
|---|---|
| {{CONTROLADOR_NOME}} | {{OPERADOR_NOME}} |
| _____________________ | _____________________ |
| Nome, cargo, CPF | Nome, cargo, CPF |
| Data: __/__/____ | Data: __/__/____ |
