<!--
TEMPLATE: TERMOS DE USO
==========================
Skill: lgpd-compliance
Cobertura: CDC (Lei 8.078/1990) + Marco Civil (Lei 12.965/2014, com STF Tema 987/2025) +
           LGPD (Lei 13.709/2018) + CC (Lei 10.406/2002) + Lei de Direitos Autorais
           (Lei 9.610/1998) + Lei do Software (Lei 9.609/1998).
Modelo: B2C neutro (sem cap monetário de responsabilidade, defensável no Brasil).

Placeholders a preencher:
  {{APP_NOME}}                 nome do app/serviço
  {{APP_URL}}                  URL pública
  {{CONTROLADOR_NOME}}         razão social ou nome civil
  {{CONTROLADOR_DOC}}          CNPJ ou CPF mascarado
  {{CONTROLADOR_ENDERECO}}     endereço completo
  {{CONTROLADOR_EMAIL}}        e-mail principal
  {{DPO_CONTATO}}              e-mail/URL do canal de privacidade
  {{DATA_ATUALIZACAO}}         AAAA-MM-DD
  {{DATA_VIGENCIA}}            AAAA-MM-DD (pode ser igual ou posterior à atualização)
  {{VERSAO}}                   ex: 1.0 ou 2026-05-24
  {{IS_B2C}}                   true|false
  {{COBRA}}                    true|false  (afeta seções 6 e 16)
  {{TEM_UGC}}                  true|false  (afeta seções 8 e adiciona notice & takedown)
  {{IDADE_MINIMA}}             padrão 18; se < 18, adiciona consentimento parental
  {{VERTICAL}}                 generico|fintech|healthtech|edtech|govtech (adiciona cláusulas setoriais)
  {{DESCRICAO_SERVICO}}        uma frase descrevendo o que o app faz
  {{DISCLAIMER_ESCOPO}}        "não substitui consulta médica/jurídica/etc"
-->

# Termos de Uso: {{APP_NOME}}

**Última atualização:** {{DATA_ATUALIZACAO}}
**Versão:** {{VERSAO}}
**Em vigor desde:** {{DATA_VIGENCIA}}

---

## Aviso de leitura rápida

Estes Termos regulam o uso do **{{APP_NOME}}**. Em uma página:

- **Quem somos:** {{CONTROLADOR_NOME}} ({{CONTROLADOR_DOC}}). Contato: {{CONTROLADOR_EMAIL}}.
- **O que oferecemos:** {{DESCRICAO_SERVICO}}.
- **O que você pode esperar:** o serviço como descrito, sob nossa responsabilidade legal, com as garantias do **Código de Defesa do Consumidor** preservadas.
- **O que esperamos de você:** uso lícito, sem fraude, sem abuso, sem violar direitos de terceiros.
- **Como cancelar:** a qualquer momento, em "Configurações > Conta", com o mesmo número de cliques do cadastro.
- **Privacidade:** tratamos seus dados conforme nossa [Política de Privacidade](/legal/privacidade), documento separado.

*Este resumo é informativo. Em caso de divergência, prevalece o texto completo abaixo.*

---

## 1. Aceitação destes Termos

Ao marcar a caixa **"Li e concordo com os Termos de Uso"** e clicar em "Criar conta" (ou equivalente), você declara ter lido, compreendido e aceitado integralmente estas condições, formando-se **contrato vinculante** entre você (doravante "**Usuário**") e a **{{CONTROLADOR_NOME}}** (doravante "**Nós**" ou "{{APP_NOME}}").

Registramos seu aceite com timestamp, IP truncado, versão dos Termos e identificador único, conforme nossa Política de Privacidade.

## 2. Definições

Para fins destes Termos:

- **Usuário**, pessoa, natural ou jurídica, cadastrada que utiliza o Serviço.
- **Conta**, perfil único e intransferível associado a um endereço de e-mail.
- **Plataforma** ou **Serviço**, o aplicativo web disponível em {{APP_URL}} e suas funcionalidades.
- **Conteúdo do Usuário**, todo dado, texto, imagem, áudio, vídeo ou arquivo enviado pelo Usuário à Plataforma.
- **Conteúdo da Plataforma**, todo material disponibilizado por nós (marca, logo, código, design, textos institucionais).
- **Plano**, modalidade de assinatura ou aquisição do Serviço.

## 3. Quem somos

| | |
|---|---|
| **Razão Social** | {{CONTROLADOR_NOME}} |
| **CNPJ / CPF** | {{CONTROLADOR_DOC}} |
| **Endereço** | {{CONTROLADOR_ENDERECO}} |
| **Contato** | {{CONTROLADOR_EMAIL}} |
| **Canal de Privacidade (LGPD)** | {{DPO_CONTATO}} |

Somos provedor de aplicação de internet nos termos do art. 5º, VII, da Lei 12.965/2014 (Marco Civil da Internet).

## 4. O que o Serviço faz

{{DESCRICAO_SERVICO}}

**Limites importantes:** {{DISCLAIMER_ESCOPO}}. O Serviço não substitui aconselhamento profissional especializado quando a decisão exigir.

## 5. Cadastro, conta e idade mínima

### 5.1. Quem pode usar
Para criar uma Conta, você deve ter no mínimo **{{IDADE_MINIMA}} anos completos**.

{{#IF IDADE_MINIMA < 18}}
Adolescentes entre {{IDADE_MINIMA}} e 17 anos podem utilizar o Serviço mediante **consentimento específico e em destaque** de pelo menos um dos pais ou responsável legal, nos termos do art. 14 da LGPD. Crianças menores de 13 anos exigem verificação reforçada do consentimento parental.
{{/IF}}

### 5.2. Veracidade
Você é responsável pelas informações fornecidas no cadastro. Dados falsos podem resultar em suspensão da Conta. A inserção dolosa de informações falsas pode caracterizar crime (CP art. 299).

### 5.3. Segurança da Conta
Você é responsável por manter a confidencialidade de sua senha e por toda atividade realizada em sua Conta, **ressalvadas hipóteses de falha de segurança imputáveis à Plataforma**. Recomendamos fortemente a ativação de autenticação em dois fatores (2FA).

### 5.4. Uma Conta por pessoa
A Conta é pessoal e intransferível. Você não pode compartilhar credenciais nem criar múltiplas contas para o mesmo titular, salvo autorização expressa.

{{#IF COBRA}}

## 6. Planos, pagamento e cobrança

### 6.1. Preço e cobrança
Os planos pagos do {{APP_NOME}} estão descritos em {{APP_URL}}/precos. O preço é cobrado conforme a periodicidade escolhida (mensal, anual), por meio das formas de pagamento disponíveis.

### 6.2. Renovação automática
Planos com periodicidade são **renovados automaticamente** ao final de cada ciclo, salvo cancelamento antes da renovação. Avisaremos por e-mail com antecedência mínima de **7 dias** antes da renovação.

### 6.3. Direito de arrependimento (CDC art. 49)
Nos termos do **art. 49 do Código de Defesa do Consumidor**, você pode exercer o direito de arrependimento em até **7 (sete) dias corridos** contados da contratação ou da renovação, com **reembolso integral e imediato** dos valores pagos, monetariamente atualizados, **sem qualquer ônus**.

### 6.4. Reajuste de preço
Eventuais reajustes obedecem ao prazo mínimo legal de 12 meses (Lei 10.192/2001) e seguem índice objetivo divulgado previamente. Comunicaremos qualquer reajuste com antecedência mínima de **30 dias**, e você poderá rescindir sem ônus se discordar.

### 6.5. Inadimplência
Em caso de inadimplência, a Conta será **suspensa após [10] dias** da data do vencimento, e seus dados serão preservados por **[30] dias adicionais** antes de exclusão definitiva, durante os quais você poderá regularizar e retomar o serviço, ou exportar seus dados pelo recurso de portabilidade.

### 6.6. Cancelamento
Você pode cancelar a qualquer momento em **Configurações > Assinatura**, sem necessidade de contato adicional. O cancelamento entra em vigor ao final do ciclo já pago, ressalvado o direito de arrependimento (6.3).

{{/IF}}

## 7. Uso permitido e proibido

### 7.1. O que você pode fazer
Utilizar o Serviço para os fins descritos na seção 4, dentro dos limites técnicos e do Plano contratado.

### 7.2. O que **é vedado** ao Usuário

- Utilizar o Serviço para fins **ilícitos** ou contrários à legislação aplicável.
- Realizar **engenharia reversa**, descompilar, desmontar ou tentar extrair o código-fonte da Plataforma.
- **Coletar dados** de outros Usuários por meios automatizados (scraping, crawlers) sem autorização escrita.
- Burlar **limites técnicos**, criar múltiplas contas para abuso de promoções, ou compartilhar credenciais comercialmente.
- Publicar, transmitir ou armazenar conteúdo que **viole direitos de terceiros** (propriedade intelectual, intimidade, honra).
- Praticar **discurso de ódio**, racismo, misoginia, apologia a atos antidemocráticos, terrorismo, indução ao suicídio, abuso ou exploração sexual de crianças e adolescentes, tráfico de pessoas.
- Realizar **ataques** à infraestrutura (invasão, DoS, exploração de vulnerabilidades), vedados pela Lei 12.737/2012.
- **Personificar** outros Usuários, criar contas falsas ou manipular métricas.
- Fazer **uso comercial** do Serviço fora do plano contratado.

### 7.3. Consequências
Violações poderão resultar, conforme a gravidade e observado contraditório quando cabível, em **advertência → suspensão temporária → encerramento** da Conta. Para condutas graves do art. 14.3 (rol "dever de cuidado" do Marco Civil pós-STF/2025), poderemos remover conteúdo e suspender a Conta **imediatamente**, sem prévio aviso, comunicando a você posteriormente.

{{#IF TEM_UGC}}

## 8. Conteúdo do Usuário

### 8.1. Propriedade
Você **mantém integralmente a titularidade** sobre o Conteúdo do Usuário que envia à Plataforma.

### 8.2. Licença concedida a nós
Ao publicar Conteúdo do Usuário, você concede à {{CONTROLADOR_NOME}} uma licença **mundial, não exclusiva, gratuita, sublicenciável (apenas quando necessário à prestação do serviço: CDN, processadores, infraestrutura) e revogável mediante exclusão do conteúdo**, para hospedar, armazenar, exibir, distribuir, reproduzir, adaptar tecnicamente (transcoding, redimensionamento), indexar e disponibilizar o Conteúdo do Usuário **exclusivamente** na medida necessária à operação e melhoria do Serviço.

Esta licença **não inclui** uso do Conteúdo para treinamento de modelos de inteligência artificial ou finalidades distintas da prestação do Serviço, salvo consentimento específico e destacado obtido em momento próprio.

### 8.3. Direitos morais
Em conformidade com o art. 27 da Lei 9.610/1998, os **direitos morais** sobre suas obras são **inalienáveis e irrenunciáveis**, nenhuma cláusula destes Termos transfere ou restringe tais direitos.

### 8.4. Responsabilidade
Você declara **possuir todos os direitos** necessários sobre o Conteúdo do Usuário enviado e responde, em caráter exclusivo, por sua legalidade e respeito a direitos de terceiros.

### 8.5. Remoção e moderação
Poderemos remover Conteúdo do Usuário que viole estes Termos ou a legislação aplicável, mediante notificação ao publicador (salvo urgência ou conteúdo do rol "dever de cuidado" da seção 7.3). Você poderá apresentar contraditório em até **7 dias úteis**.

### 8.6. Notificação de conteúdo infringente
Disponibilizamos canal específico para notificação extrajudicial em **[denuncia@{{APP_URL}}]** ou formulário em **{{APP_URL}}/legal/denuncia**, conforme procedimento detalhado em {{APP_URL}}/legal/notice-takedown. Notificações serão analisadas em até **72 horas úteis** para casos gerais e **imediatamente** para conteúdo do rol "dever de cuidado".

{{/IF}}

## 9. Propriedade intelectual da Plataforma

Todos os direitos de propriedade intelectual sobre a Plataforma, incluindo **código-fonte** (protegido pela Lei 9.609/1998), layout, marcas, logotipos, textos institucionais e bases de dados (Lei 9.610/1998 e Lei 9.279/1996), pertencem à **{{CONTROLADOR_NOME}}** ou a seus licenciantes.

Concedemos a você uma licença **pessoal, limitada, revogável, intransferível e não-exclusiva** para utilizar o Serviço estritamente conforme estes Termos. É vedado reproduzir, modificar, criar obras derivadas, distribuir ou explorar comercialmente qualquer elemento da Plataforma sem autorização prévia e escrita.

## 10. Privacidade

O tratamento de dados pessoais realizado em decorrência destes Termos é regido pela [**Política de Privacidade**](/legal/privacidade), que integra este instrumento para todos os fins, em conformidade com a **Lei 13.709/2018 (LGPD)** e com o **Marco Civil da Internet**.

## 11. Disponibilidade, manutenção e modificações no serviço

Empregamos esforços comercialmente razoáveis para manter o Serviço disponível 24/7, ressalvadas:
- **Janelas de manutenção programada**, com aviso prévio de pelo menos 48 horas.
- **Manutenções emergenciais** quando necessárias à segurança ou estabilidade.
- Eventos de **caso fortuito ou força maior** (CC art. 393).

Poderemos modificar, evoluir ou descontinuar funcionalidades, comunicando o Usuário com antecedência de no mínimo **30 dias** quando se tratar de funcionalidade essencial de plano pago, oferecendo **reembolso proporcional** se aplicável.

## 12. Limitação de responsabilidade

Na máxima extensão permitida pela legislação aplicável, e **sem prejuízo das garantias legais asseguradas ao consumidor pelo Código de Defesa do Consumidor**, a {{CONTROLADOR_NOME}} responde pelos **danos diretos** comprovadamente decorrentes de falha imputável ao Serviço, ficando excluídos lucros cessantes e danos indiretos quando a exclusão for legalmente cabível.

Esta limitação **não se aplica** a:
- casos de **dolo ou culpa grave**;
- danos a **direitos da personalidade** (vida, integridade, intimidade, honra);
- hipóteses de **responsabilidade objetiva** legalmente atribuídas;
- **vícios e defeitos** do serviço perante consumidor (CDC arts. 24 e 25, garantia legal irrenunciável);
- reparação por **vazamento de dados** decorrente de falha imputável à nós (LGPD arts. 42-45).

## 13. Suspensão e encerramento da Conta

### 13.1. Pelo Usuário
Você pode encerrar sua Conta a qualquer momento em **Configurações > Conta > Encerrar conta**, sem necessidade de justificativa. O encerramento é efetivado em até **24 horas** e enseja reembolso proporcional dos valores pagos referentes a período não usufruído de plano vigente.

### 13.2. Por nós
A Conta poderá ser suspensa ou encerrada nas seguintes hipóteses:
- **(a)** Violação destes Termos ou da legislação aplicável.
- **(b)** Inatividade superior a **24 meses**, mediante aviso prévio de 30 dias.
- **(c)** Ordem judicial ou administrativa.
- **(d)** Solicitação do próprio Usuário (item 13.1).

### 13.3. Contraditório
Em caso de encerramento por nossa iniciativa (13.2 a), será assegurado ao Usuário, **sempre que possível e proporcional à gravidade**, prazo de **5 dias úteis** para apresentar manifestação. Para condutas do rol "dever de cuidado" (item 7.3), o encerramento pode ser imediato, com contraditório posterior.

### 13.4. Exportação de dados antes da exclusão
Antes da exclusão definitiva, você poderá exportar seus dados pelo recurso de portabilidade disponível em **Configurações > Privacidade**, conforme art. 18, V, da LGPD.

### 13.5. Retenção pós-encerramento
Após o encerramento, seus dados serão eliminados em até **30 dias**, ressalvadas hipóteses legais de guarda obrigatória (Marco Civil art. 15, registros de acesso por 6 meses; Decreto 7.212/2010, fiscal por 5 anos; demais obrigações aplicáveis).

## 14. Alteração destes Termos

Poderemos atualizar estes Termos a qualquer tempo, comunicando o Usuário por:
- **E-mail cadastrado**, com antecedência mínima de **30 dias** da entrada em vigor;
- **Aviso destacado na Plataforma** (banner persistente).

Para **alterações materiais** (preço, escopo, política de cancelamento, foro, limitação de responsabilidade, base legal de tratamento de dados), exigiremos **novo aceite ativo** em modal específico antes de continuar usando o Serviço.

O Usuário que **não concordar** com a nova versão poderá rescindir o contrato sem ônus antes da entrada em vigor, com reembolso proporcional do período não usufruído de plano pago.

## 15. Foro e lei aplicável

Estes Termos são regidos pelas **leis da República Federativa do Brasil**.

{{#IF IS_B2C}}
Para Usuários **consumidores** (pessoa física), fica eleito o foro do **domicílio do consumidor**, nos termos do art. 101, I, do CDC. Cláusula de eleição de foro diversa, em prejuízo do consumidor, é nula (CPC art. 63 §3º).

A arbitragem **não é compulsória** para Usuários consumidores. Eventual instituição de arbitragem dependerá de iniciativa ou concordância expressa pós-conflito do consumidor, nos termos do art. 4º §2º da Lei 9.307/1996.
{{ELSE}}
Para Usuários corporativos (pessoa jurídica não-vulnerável), fica eleito o foro da Comarca de **[Cidade/UF]**.
{{/IF}}

## 16. Disposições finais

- **Invalidade parcial.** Se qualquer disposição destes Termos for declarada nula ou inexequível, as demais permanecem em pleno vigor.
- **Tolerância.** A eventual tolerância de uma das partes ao descumprimento de qualquer obrigação pela outra não significa novação nem renúncia ao direito de exigir o cumprimento.
- **Comunicações.** Comunicações entre as partes serão consideradas válidas quando feitas para os endereços eletrônicos cadastrados na Conta. É obrigação do Usuário mantê-los atualizados.
- **Integralidade.** Estes Termos, em conjunto com a Política de Privacidade e demais documentos linkados, constituem o **acordo integral** entre as partes, substituindo entendimentos anteriores.
- **Cessão.** Você não pode ceder estes Termos a terceiro sem nossa autorização prévia. Nós poderemos ceder em caso de sucessão empresarial (M&A), mediante comunicação prévia.

## 17. Histórico de versões

| Versão | Data | Resumo das mudanças |
|---|---|---|
| {{VERSAO}} | {{DATA_ATUALIZACAO}} | Versão em vigor |

Versões anteriores: {{APP_URL}}/legal/termos/historico

---

*Estes Termos foram redigidos em conformidade com o Código de Defesa do Consumidor (Lei 8.078/1990), o Marco Civil da Internet (Lei 12.965/2014) com a interpretação do STF no Tema 987 (2025), a LGPD (Lei 13.709/2018), o Código Civil (Lei 10.406/2002) e demais normas brasileiras aplicáveis.*

*Em caso de dúvida sobre estes Termos: {{CONTROLADOR_EMAIL}}.*
*Em caso de dúvida sobre proteção de dados: {{DPO_CONTATO}}.*
