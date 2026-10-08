<!--
TEMPLATE: POLÍTICA DE PRIVACIDADE LGPD
========================================
Skill: lgpd-compliance
Cobertura: art. 9º + 18 + 33 + 41 + 48 da Lei 13.709/2018 + boas práticas ANPD.
Modelo: 2 camadas (resumo + detalhe).

Placeholders a preencher (busque {{...}}):
  {{APP_NOME}}                 nome do app/serviço
  {{APP_URL}}                  URL pública
  {{CONTROLADOR_NOME}}         razão social ou nome civil
  {{CONTROLADOR_DOC}}          CNPJ NN.NNN.NNN/NNNN-NN ou CPF mascarado ***.***.***-NN
  {{CONTROLADOR_ENDERECO}}     endereço completo
  {{CONTROLADOR_EMAIL}}        e-mail principal
  {{DPO_NOME}}                 nome do encarregado OU "Canal de Privacidade" se ATPP
  {{DPO_CONTATO}}              e-mail/URL do canal
  {{DATA_ATUALIZACAO}}         AAAA-MM-DD
  {{VERSAO}}                   ex: 1.0
  {{IS_ATPP}}                  true|false, define prazos exibidos (15 ou 30 dias)
  {{TABELA_DADOS}}             tabela markdown gerada da auditoria
  {{TABELA_TERCEIROS}}         tabela markdown de processadores
  {{TABELA_TRANSF_INT}}        tabela markdown de transferências internacionais
  {{TEM_COOKIES}}              true|false, controla link pra política de cookies
  {{TEM_SENSIVEL}}             true|false, adiciona seção art. 11
  {{TEM_CRIANCAS}}             true|false, adiciona seção art. 14
  {{TEM_DECISAO_AUTO}}         true|false, adiciona seção art. 20
-->

# Política de Privacidade: {{APP_NOME}}

**Última atualização:** {{DATA_ATUALIZACAO}}
**Versão:** {{VERSAO}}

---

## Resumo

Este documento explica como o {{APP_NOME}} trata seus dados pessoais, em conformidade com a **Lei Geral de Proteção de Dados Pessoais (LGPD: Lei nº 13.709/2018)** e as orientações da **Autoridade Nacional de Proteção de Dados (ANPD)**.

Em poucas linhas:

- **Quem trata seus dados:** {{CONTROLADOR_NOME}} ({{CONTROLADOR_DOC}}).
- **Por quê:** para que você possa usar o {{APP_NOME}} e para cumprir obrigações legais.
- **Com quem compartilhamos:** apenas com prestadores estritamente necessários (lista abaixo).
- **Por quanto tempo:** o mínimo necessário para cada finalidade, respeitando prazos legais.
- **Seus direitos:** você pode, a qualquer momento e gratuitamente, acessar, corrigir, exportar, eliminar seus dados, revogar consentimentos. Contato: **{{DPO_CONTATO}}**.

Continue lendo para o detalhamento completo. Em caso de dúvida, escreva para nosso canal de privacidade.

---

## 1. Quem somos (Controlador)

| | |
|---|---|
| **Nome / Razão Social** | {{CONTROLADOR_NOME}} |
| **CNPJ / CPF** | {{CONTROLADOR_DOC}} |
| **Endereço** | {{CONTROLADOR_ENDERECO}} |
| **E-mail institucional** | {{CONTROLADOR_EMAIL}} |
| **App / Serviço** | {{APP_NOME}} ({{APP_URL}}) |

Somos o **Controlador** dos seus dados pessoais nos termos do art. 5º, VI, da LGPD, quem decide as finalidades e os meios do tratamento.

## 2. Encarregado de Dados (DPO)

Para qualquer questão sobre proteção de dados, fale com nosso **Encarregado de Dados (Data Protection Officer)**:

- **{{DPO_NOME}}**
- **Contato:** {{DPO_CONTATO}}

O Encarregado é o canal de comunicação entre você (titular), nós (controlador) e a ANPD, nos termos do art. 41 da LGPD.

## 3. Quais dados coletamos e por quê

Coletamos apenas os dados estritamente necessários para cada finalidade (princípio da necessidade, art. 6º, III). Cada coleta está fundamentada em uma das **bases legais** previstas no art. 7º (dados comuns) ou art. 11 (dados sensíveis) da LGPD.

{{TABELA_DADOS}}

<!--
Formato esperado da TABELA_DADOS (uma linha por finalidade):

| Categoria de dado | Finalidade | Base legal | Tempo de retenção |
|---|---|---|---|
| Nome, e-mail, senha | Criar e manter sua conta | Art. 7º V (execução de contrato) | Enquanto durar a conta + 6 meses |
| CPF, endereço | Emissão de nota fiscal | Art. 7º II (obrigação legal) | 5 anos (Decreto 7.212/2010) |
| E-mail | Envio de newsletter quinzenal | Art. 7º I (consentimento) | Até revogação |
| IP, user-agent, logs de acesso à aplicação | Segurança da plataforma + obrigação legal | Art. 7º II / IX | 6 meses (Marco Civil: Lei 12.965/2014 art. 15) |
-->

{{#IF TEM_SENSIVEL}}

### 3.1. Dados pessoais sensíveis

Tratamos as seguintes categorias de **dados sensíveis** (art. 5º, II, da LGPD), com proteção reforçada e base legal específica do art. 11:

- {{LISTAR_DADOS_SENSIVEIS}}

O tratamento de dados sensíveis exige (i) seu **consentimento específico e destacado**, ou (ii) hipóteses estritas do art. 11, II (saúde, proteção da vida, obrigação legal, segurança/prevenção a fraude). Não usamos legítimo interesse para dados sensíveis.

{{/IF}}

{{#IF TEM_CRIANCAS}}

### 3.2. Dados de crianças e adolescentes (art. 14)

Se você tem **menos de 18 anos**, tratamentos exigem o consentimento específico e em destaque de pelo menos um dos seus pais ou responsável legal, com verificação compatível com o risco do serviço. Para **crianças menores de 12 anos**, exigimos verificação reforçada do consentimento parental.

Não condicionamos sua participação no {{APP_NOME}} ao fornecimento de dados além do estritamente necessário (art. 14, §3º).

{{/IF}}

## 4. Como coletamos seus dados

Coletamos dados:

- **Diretamente de você**, quando você se cadastra, preenche formulários, envia conteúdo, contrata o serviço.
- **Automaticamente**, quando você usa o app: IP, user-agent, logs de acesso, cookies (ver Política de Cookies).
- **De terceiros**, quando você se conecta por login social (Google, Apple) ou quando recebemos dados de prestadores autorizados.

## 5. Com quem compartilhamos seus dados

Compartilhamos com **prestadores de serviço estritamente necessários (operadores)**, sob contrato com cláusulas de proteção de dados (DPA):

{{TABELA_TERCEIROS}}

<!--
Formato:

| Terceiro | Dado compartilhado | Finalidade | País de processamento |
|---|---|---|---|
| Stripe | nome, e-mail, valor | Processar pagamento | EUA (SCC ANPD) |
| Mailgun | e-mail, conteúdo | Envio transacional | EUA (SCC ANPD) |
| AWS sa-east-1 | tudo do banco | Hospedagem | Brasil |
| Sentry | logs sanitizados | Monitoramento de erro | EUA (SCC ANPD) |
-->

Não vendemos seus dados pessoais. Não compartilhamos para fins de marketing de terceiros sem seu consentimento específico.

## 6. Transferência internacional de dados

{{#IF TABELA_TRANSF_INT}}

Alguns dos prestadores acima processam dados **fora do Brasil**. Nessas hipóteses, garantimos a transferência por mecanismos previstos no art. 33 da LGPD e na **Resolução CD/ANPD nº 19/2024**, em particular **Cláusulas-Padrão Contratuais (SCC)** aprovadas pela ANPD.

{{TABELA_TRANSF_INT}}

<!--
Formato:

| Destino | Prestador | Garantia jurídica |
|---|---|---|
| Estados Unidos | Stripe, Mailgun, Sentry | Cláusulas-Padrão Contratuais (Res. CD/ANPD nº 19/2024) |
| Global (Edge) | Vercel, Cloudflare | Cláusulas-Padrão Contratuais (Res. CD/ANPD nº 19/2024) |
-->

{{ELSE}}

Atualmente todos os seus dados são processados em território nacional. Caso passemos a transferir dados ao exterior, atualizaremos esta política e comunicaremos com destaque.

{{/IF}}

## 7. Por quanto tempo guardamos seus dados

Mantemos seus dados pelo tempo **necessário ao cumprimento das finalidades** declaradas e pelo prazo determinado por obrigações legais e regulatórias. Quando você solicita exclusão, **alguns dados precisam ser retidos por exigência legal**, comunicaremos quais e por quanto tempo no momento da exclusão.

Prazos mais comuns aplicáveis:

- **Notas fiscais e dados fiscais:** 5 anos (Decreto 7.212/2010; CTN art. 173).
- **Logs de acesso à aplicação:** 6 meses (Marco Civil da Internet: Lei 12.965/2014 art. 15).
- **Logs de conexão** (caso aplicável a provedor de conexão): 1 ano (Marco Civil, art. 13).
- **Dados de cobrança e relação de consumo:** 5 anos (CDC art. 27).
- **Outras retenções legais:** conforme aplicável.

Ao fim do prazo, eliminamos ou **anonimizamos** os dados.

## 8. Como protegemos seus dados

Adotamos medidas técnicas e administrativas para proteger seus dados, em conformidade com os arts. 46-49 da LGPD:

- **Criptografia em trânsito** (HTTPS/TLS 1.2+) e **em repouso** no banco de dados.
- **Hash forte** para senhas (argon2/bcrypt), nunca armazenamos senha em texto claro.
- **Autenticação de dois fatores (2FA)** disponível e exigida em acessos administrativos.
- **Princípio do menor privilégio** em controle de acesso.
- **Logs centralizados** com retenção mínima de 90 dias.
- **Backups criptografados**, armazenados em local distinto da produção, com teste periódico de restauração.
- **Atualização regular** de dependências e correção rápida de vulnerabilidades.
- **Treinamento periódico** da equipe em proteção de dados.

Em caso de **incidente de segurança** que possa causar risco ou dano relevante, comunicaremos a ANPD e você nos prazos da **Resolução CD/ANPD nº 15/2024**.

## 9. Seus direitos como titular (art. 18 LGPD)

Você tem **9 direitos**, exercíveis a qualquer momento, gratuitamente:

1. **Confirmação** da existência de tratamento dos seus dados.
2. **Acesso** aos seus dados, com origem e finalidade.
3. **Correção** de dados incompletos, inexatos ou desatualizados.
4. **Anonimização, bloqueio ou eliminação** de dados desnecessários, excessivos ou tratados em desconformidade.
5. **Portabilidade** dos dados a outro fornecedor.
6. **Eliminação** dos dados tratados com consentimento (respeitadas hipóteses legais de retenção).
7. **Informação** sobre com quem compartilhamos seus dados.
8. **Informação** sobre a possibilidade de não fornecer consentimento e suas consequências.
9. **Revogação do consentimento**, a qualquer momento, com a mesma facilidade com que foi concedido.

### Como exercer seus direitos

- **Self-service no app**: acesse `/{{APP_URL}}/privacidade` quando logado para acessar, exportar e excluir seus dados, e gerenciar consentimentos.
- **Canal do Encarregado**: escreva para **{{DPO_CONTATO}}** com seu pedido. Pediremos comprovação de identidade.

**Prazos de resposta:**

{{#IF IS_ATPP}}

- Confirmação simplificada: até **15 dias** úteis.
- Declaração completa (acesso + origem + finalidade): até **30 dias**.
- Demais pedidos: razoável, sempre comunicando previsão.

> Operamos sob o regime de **Agente de Tratamento de Pequeno Porte** (Resolução CD/ANPD nº 2/2022), que prevê prazos em dobro do regime geral.

{{ELSE}}

- Confirmação simplificada: **imediata**.
- Declaração completa (acesso + origem + finalidade): até **15 dias**.
- Demais pedidos: prazo razoável, sempre comunicando previsão.

{{/IF}}

### Reclamação à ANPD

Se entender que não atendemos satisfatoriamente, você pode **reclamar diretamente à Autoridade Nacional de Proteção de Dados**:

- Portal: [gov.br/anpd/pt-br/canais_atendimento/cidadao/peticao-de-titular](https://www.gov.br/anpd/pt-br/canais_atendimento/cidadao/peticao-de-titular)

{{#IF TEM_DECISAO_AUTO}}

## 10. Decisões automatizadas (art. 20)

Algumas decisões no {{APP_NOME}} são tomadas com base em tratamento automatizado, incluindo:

- {{LISTAR_DECISOES_AUTOMATIZADAS}}

Você tem direito a:

- **Saber que a decisão foi automatizada**, informaremos no momento da decisão.
- **Receber informações claras e adequadas** sobre os critérios e procedimentos utilizados (resguardados segredos comercial e industrial).
- **Solicitar revisão** da decisão. Disponibilizamos canal de contestação em `/contestacao` ou via {{DPO_CONTATO}}.

{{/IF}}

{{#IF TEM_COOKIES}}

## 11. Cookies e tecnologias similares

Usamos cookies para fazer o {{APP_NOME}} funcionar corretamente e, com seu consentimento, para analisar uso e personalizar conteúdo.

Detalhes completos sobre **categorias, finalidade, retenção e como gerenciar** estão na nossa [**Política de Cookies**](/legal/cookies).

Você pode revogar consentimentos de cookies a qualquer momento clicando em "Gerenciar preferências de cookies" no rodapé.

{{/IF}}

## 12. Alterações nesta Política

Podemos atualizar esta Política para refletir mudanças no serviço, na legislação ou em decisões da ANPD. Quando a mudança for **material**, comunicaremos com destaque e antecedência razoável (mínimo 30 dias quando possível). A versão atual está sempre disponível em `{{APP_URL}}/legal/privacidade`.

## 13. Histórico de versões

| Versão | Data | Resumo das mudanças |
|---|---|---|
| {{VERSAO}} | {{DATA_ATUALIZACAO}} | Versão inicial |

---

*Esta Política é elaborada em conformidade com a Lei 13.709/2018 (LGPD), as resoluções da ANPD vigentes e demais normas brasileiras aplicáveis (Marco Civil da Internet, CDC, ECA quando aplicável).*

*Em caso de divergência de interpretação, prevalece o texto da lei e as orientações oficiais da [ANPD](https://www.gov.br/anpd/pt-br).*
