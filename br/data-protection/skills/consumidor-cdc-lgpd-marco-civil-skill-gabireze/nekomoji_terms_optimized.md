# Política de Privacidade e Termos de Uso do NekoMoji
*Última atualização: 3 de julho de 2026*

---

## Resumo rápido (para humanos, não advogados):
- Não mantemos armazenamento permanente das suas fotos, vídeos ou GIFs.
- Usamos só o necessário para limite diário e Premium.
- O chat passa pela API oficial do WhatsApp (Meta) — não somos a Meta.
- App Meta com permissões `whatsapp_business_messaging`, `whatsapp_business_management` e `public_profile`.
- Pagamentos e dados de cartão ficam com o Mercado Pago.
- LGPD: você pode pedir cópia dos seus dados ou exclusão da conta por e-mail; enviamos comprovação do apagamento (ver seção 5 da Política de Privacidade).

O NekoMoji leva sua privacidade a sério. Esta política descreve como coletamos, usamos e protegemos seus dados, buscando observar a LGPD (Lei Geral de Proteção de Dados - Lei 13.709/2018) e aplicar boas práticas de minimização, segurança e transparência.

O NekoMoji é um serviço digital independente operado por desenvolvedor pessoa física. Para fins de transparência, identificação e contato para quaisquer solicitações comerciais ou de privacidade, disponibilizamos o canal direto por meio do e-mail **contato@nekomoji.chat**.

---

## PARTE I - POLÍTICA DE PRIVACIDADE

### 1. Dados Coletados
Coletamos apenas o mínimo necessário para funcionamento do serviço:
- **Identificador WhatsApp:** Número, JID ou identificador tratado em formato minimizado, pseudonimizado ou hasheado, conforme a finalidade técnica, usado para controlar limites, plano Premium e funcionamento do bot.
- **Uso do serviço:** Contagem de figurinhas criadas e data da última atividade para controle de limite de 24h.
- **Preferências:** Configurações mínimas do bot (ex: se o aviso de processamento já foi exibido), armazenadas como booleanos simples, sem conteúdo pessoal.
- **Dados de pagamento:** Histórico de transações (apenas ID da transação, valor, data e status) para controle de Premium. Dados de cartão são processados exclusivamente pelo Mercado Pago.
- **Programa de indicação (opcional):** Se você usar o recurso, podemos tratar código de indicação, vínculo entre contas (identificadores de telefone no formato utilizado pelo serviço), datas de vínculo e informações necessárias para calcular e registrar bônus de Premium — conforme descrito na página do programa e nos Termos de Uso (item 5.3).

### 2. Mídias Enviadas
Não mantemos armazenamento permanente das suas fotos, vídeos ou GIFs. Todo conteúdo enviado (imagens, vídeos, GIFs, links do Instagram, Twitter/X, Pinterest, TikTok, Tenor, Giphy e KLIPY) é usado apenas pelo tempo necessário para conversão e envio da figurinha. As mídias podem passar por processamento temporário em memória ou arquivos transitórios, que são descartados após a conclusão do processamento. Não mantemos armazenamento permanente das mídias enviadas em banco de dados ou repositórios de arquivos.

### 3. Proteção de Dados Pessoais
Implementamos múltiplas camadas de segurança:
- **Sanitização automática:** Todos os logs são automaticamente mascarados (ex: `+5519920062836` vira `+5519****36`).
- **Firestore Security Rules:** Acesso negado por padrão - apenas servidor com credenciais administrativas pode acessar dados.
- **Criptografia:** Dados em trânsito via HTTPS/TLS 1.3 e em repouso via AES-256 (Firebase).
- **Cache limitado:** Dados de premium ficam em cache por apenas 5 minutos.
- Em caso de incidente de segurança que possa acarretar risco ou dano relevante aos titulares, adotaremos as medidas técnicas e administrativas cabíveis e realizaremos as comunicações exigidas pela LGPD e pela regulamentação aplicável.

### 4. Compartilhamento de Dados
Não vendemos, alugamos ou compartilhamos seus dados com terceiros para marketing. Compartilhamento ocorre apenas com:
- **Meta Platforms, Inc. (WhatsApp):** O NekoMoji utiliza a WhatsApp Business Platform (Cloud API), serviço oficial da Meta, para receber e enviar mensagens. Dados necessários ao funcionamento do chat (incluindo identificadores de conversa e metadados exigidos pela plataforma) são tratados também conforme as políticas e termos do WhatsApp aplicáveis a usuários e empresas. Isso nos permite operar de forma alinhada às regras oficiais da rede.
- **Google Firebase:** Hospedagem do banco de dados (criptografado).
- **Mercado Pago:** Processamento de pagamentos Premium.
- **Google Analytics e Google Ads:** Medição de acesso e conversão nas landing pages somente após consentimento, para entender desempenho de campanhas e páginas públicas.
- **Autoridades:** Mediante ordem judicial ou obrigação legal.

Esses provedores podem tratar dados em infraestrutura fora do Brasil. Quando houver transferência internacional de dados, ela ocorrerá apenas na medida necessária para operação do serviço, hospedagem, mensageria, pagamentos, segurança ou análise de desempenho, observadas as hipóteses legais da LGPD e as salvaguardas contratuais e técnicas aplicáveis.

O NekoMoji utiliza um aplicativo registrado no Meta for Developers com as permissões abaixo, alinhadas à documentação oficial da Meta. Elas servem apenas para operar o bot, a conta WhatsApp Business vinculada e a infraestrutura de mensagens — não vendemos nem repassamos esses acessos a terceiros:
- **whatsapp_business_messaging:** permite enviar e receber mensagens do WhatsApp com quem conversa com o número do bot, carregar e obter mídias necessárias ao processamento (ex.: figurinhas), e usar recursos ligados ao perfil comercial no WhatsApp conforme previsto na plataforma. Uso permitido no app: experiências de mensagem iniciadas pelo cliente (você nos escreve) ou pela empresa (respostas e entrega do serviço). É a permissão central do funcionamento do NekoMoji.
- **whatsapp_business_management:** permite ler e/ou gerenciar ativos da conta WhatsApp Business que utilizamos (conta comercial, número do bot, assinatura de webhook, modelos de mensagem quando aplicável, etc.). Uso: manter o serviço configurado, receber eventos de forma segura e administrar o que a Meta exige para a Cloud API.
- **public_profile:** autorização padrão da Meta para campos de perfil público no nó do usuário, em contextos de aplicativo. Uso permitido: autenticação e experiência no app, quando esse fluxo existir; no dia a dia do bot no WhatsApp, o foco do tratamento de dados é o intercâmbio de mensagens e mídias via permissões de negócios acima — não utilizamos public_profile para montar campanhas de marketing com dados identificáveis dos usuários do chat.

A Meta também descreve usos analíticos agregados ou anônimos para aprimorar o app; quando aplicável, seguimos esse tipo de dado apenas na forma em que a plataforma disponibiliza, sem remontar identidade para publicidade externa ao escopo do serviço.

### 5. Seus direitos (LGPD Art. 18) — acesso, cópia dos dados e exclusão
Além do que você consulta no próprio chat (`!status` etc.), a LGPD garante direitos sobre dados pessoais. Abaixo estão os pedidos formais (com confirmação por escrito), tratados pelo e-mail **privacidade@nekomoji.chat**.

#### 5.1 Confirmação de identidade e canal oficial
Para acesso ampliado, portabilidade ou exclusão, o titular deve enviar solicitação por e-mail (canal que permite guardar registro da data e do conteúdo do pedido). Inclua nome completo e o número de celular no formato internacional completo (ex.: +5511999998888) vinculado à conta que deseja consultar ou apagar — é o mesmo número com o qual você usa o bot no WhatsApp. Pedidos vagos ou sem meios de comprovar titularidade podem exigir informações adicionais razoáveis antes de prosseguirmos.

#### 5.2 Acesso e cópia dos dados que temos sobre você
Você pode solicitar a confirmação da existência de tratamento, o acesso aos dados e, quando aplicável, a portabilidade em formato estruturado (por exemplo JSON ou relatório legível).
Como solicitar: envie e-mail para **privacidade@nekomoji.chat** com assunto sugerido “LGPD — Acesso e cópia dos dados”, seu nome completo, o número de telefone (E.164) da conta e um texto formalizando o pedido com base no art. 18 da LGPD.
Prazo: responderemos dentro dos prazos previstos na LGPD e na regulamentação aplicável. Quando o pedido exigir validação adicional, complexidade técnica ou depender de terceiros, informaremos o titular sobre o andamento e eventual necessidade de prazo adicional, quando juridicamente cabível.

#### 5.3 Exclusão da conta e apagamento dos dados (encerramento do tratamento)
Você pode solicitar a eliminação dos dados pessoais tratados pelo NekoMoji nos sistemas sob nosso controle, exceto nas hipóteses em que a lei ou medidas de segurança legitimem a manutenção (ver item 5.4).
Como solicitar: envie e-mail para **privacidade@nekomoji.chat** com assunto sugerido “LGPD — Exclusão de conta e dados”, contendo:
- Nome completo do titular;
- Número de celular completo (com DDI, ex.: +55…) que deve ser excluído e que identifica sua conta no serviço;
- Texto claro pedindo a exclusão de todos os dados pessoais que a NekoMoji trata em relação a essa conta, com base no art. 18, VI da LGPD.

Após validar o pedido, procederemos ao apagamento nos bancos e sistemas que controlamos e responderemos ao mesmo e-mail com comprovação do atendimento, descrevendo de forma objetiva o que foi eliminado (por exemplo: remoção de documentos no Firestore, caches invalidados, backups conforme política de retenção abaixo). Se for inviável certificar item a item em anexo, indicaremos as ações realizadas de forma suficiente para demonstrar o cumprimento do pedido.

#### 5.4 Mercado Pago, medidas de segurança e retenções legais
Os dados de pagamento (cartão, titularidade bancária, etc.) são tratados diretamente pelo Mercado Pago, conforme a política deles. Não temos capacidade técnica nem autoridade para apagar ou alterar esses registros no ambiente do Mercado Pago em seu nome. Para direitos sobre esses dados (acesso, correção, exclusão), o titular deve utilizar os canais do próprio Mercado Pago.

O que mantemos do nosso lado: apenas registros mínimos de transação (identificador da transação, valor, data, status) necessários para comprovar pagamentos e plano Premium. Por medida de segurança, auditoria e obrigação legal (incluindo prazos fiscais e comprovação de relação comercial), esses metadados de pagamento não são excluíveis na totalidade enquanto a lei exigir guarda — mesmo após pedido de exclusão da “conta” do bot, quando aplicável.

Artefatos operacionais de atendimento LGPD: quando você solicita acesso, cópia ou exclusão, podemos gerar exportações e relatórios técnicos temporários para comprovar o atendimento. Esses arquivos ficam em área interna com acesso restrito, usam nomes sem identificador bruto do titular e entram em limpeza automática conforme a política operacional operacional vigente.

Resumo: apagamos o que estiver sob nosso controle e permitido pela lei; o que estiver exclusivamente no Mercado Pago ou que deva ser retido por obrigação legal seguirá as regras do terceiro ou do ordenamento jurídico.

#### 5.5 Outros direitos e correções
- **Correção de dados inexatos:** use o e-mail **privacidade@nekomoji.chat** descrevendo o ajuste necessário.
- **Revogação de consentimento ou oposição:** quando o tratamento depender dessas bases, mediante solicitação pelo e-mail indicado, avaliaremos o pedido e as consequências para o uso do serviço.

### 6. Retenção de Dados
- **Dados de uso (conta do bot):** Mantidos enquanto a conta estiver ativa. Contas inativas por mais de 90 dias podem ser removidas automaticamente. Após solicitação válida de exclusão (seção 5.3), eliminamos o que couber, salvo exceções da seção 5.4.
- **Histórico mínimo de pagamentos (NekoMoji):** Metadados de transação podem ser retidos pelo prazo necessário às obrigações legais e de segurança (em geral até 5 anos após a última transação, conforme prática fiscal no Brasil), ainda que você solicite exclusão de outros dados.
- **Mercado Pago:** retenção e exclusão de dados no provedor de pagamento seguem as políticas do Mercado Pago e não dependem da NekoMoji.
- **Backups:** Rotação automática — apenas os últimos backups são mantidos; exclusões refletem nos ciclos de backup subsequentes.
- **Artefatos LGPD:** exportações e relatórios técnicos usados para atender pedidos de acesso, exclusão e retenção ficam retidos por prazo curto, com limpeza automática, apenas para demonstrar o atendimento e auditar a operação.

### 7. Cookies e Rastreamento
As landing pages públicas do NekoMoji podem usar medição de acesso e com o Google Analytics e Google Ads somente após sua autorização no banner de privacidade. Sem esse aceite, não carregamos essas tags para fins analíticos.
Guardamos apenas a sua escolha de consentimento neste navegador para não perguntar novamente a cada visita. Não usamos esse armazenamento para login, cadastro ou perfil comportamental fora do escopo de medição da própria landing page.
Você pode recusar o banner, revogar a escolha depois pelo botão de privacidade da página e interromper novas coletas analíticas nesse navegador. Dados já enviados ao Google antes da revogação continuam sujeitos às políticas de retenção e exclusão do próprio provedor.

### 8. Contato
Para pedidos formais LGPD (acesso, cópia dos dados, exclusão, correção), use preferencialmente o e-mail abaixo. Para dúvidas gerais, você também pode chamar no WhatsApp.
- 📧 **Email (LGPD e privacidade):** privacidade@nekomoji.chat
- 💬 **WhatsApp:** +55 19 92006-2836 (https://nekomoji.chat?text=Privacidade)

---

## PARTE II - TERMOS DE USO

### Resumo rápido dos termos:
- Serviço via API oficial do WhatsApp (Meta). NekoMoji não é Meta nem WhatsApp.
- Não use o bot para conteúdo ilegal, de ódio ou explícito.
- Limites grátis: 3 figurinhas por janela de 24h + atraso de 5–10s por figurinha.
- Premium: figurinhas ilimitadas, Instagram, Twitter/X, Pinterest, TikTok, Tenor, Giphy, KLIPY e processamento instantâneo.
- Premium é pré-pago, sem renovação automática.
- LGPD: acesso e cópia dos dados, exclusão da conta e comprovações — por e-mail; limites para dados no Mercado Pago (ver Política de Privacidade, seção 5.4).
- Programa de indicação: regras de bônus, vínculo único por conta e uso do comando `!indicar` — ver página de regras e item 5.3 abaixo.

### 1. Aceitação dos Termos
Ao utilizar o NekoMoji no WhatsApp (+55 19 92006-2836), especialmente ao contratar um plano Premium, você declara estar ciente destes Termos de Uso e da Política de Privacidade. Se não concordar, não utilize o serviço.

### 2. Descrição do Serviço
O NekoMoji é um bot automatizado que converte imagens, GIFs, vídeos e links do Instagram, Twitter/X, Pinterest, TikTok, Tenor, Giphy e KLIPY em figurinhas para WhatsApp. O serviço funciona via mensagens diretas no WhatsApp.
O uso do NekoMoji pressupõe que o usuário possa utilizar o WhatsApp conforme os Termos do próprio WhatsApp. Usuários menores de idade devem utilizar o serviço com ciência e supervisão de seus pais ou responsáveis, especialmente antes de qualquer contratação paga.

**WhatsApp (API oficial da Meta):**
Utilizamos a WhatsApp Business Platform (Cloud API), oferecida pela Meta Platforms, Inc., para receber as mensagens que você envia ao nosso número e devolver as figurinhas e respostas do bot. Essa é a via oficial e suportada pela Meta para integrações empresariais, o que contribui para segurança, conformidade com as regras da plataforma e estabilidade do serviço.
O NekoMoji não é afiliado, patrocinado ou endossado pela Meta ou pelo WhatsApp. Somos um serviço independente que contrata o uso da infraestrutura oficial da Meta para entregar o bot a você.
O aplicativo de desenvolvedor na Meta utiliza as permissões `whatsapp_business_messaging`, `whatsapp_business_management` e `public_profile`; a finalidade de cada uma está detalhada na Política de Privacidade (seção 4).

- **Plano Gratuito:** 3 figurinhas a cada janela de 24 horas (resetadas 24h após o primeiro uso). O processamento de cada figurinha pode ter um atraso de 5 a 10 segundos para manter a estabilidade do servidor.
- **Plano Premium:** Figurinhas ilimitadas + download do Instagram, Twitter/X, Pinterest, TikTok, Tenor, Giphy e KLIPY + processamento instantâneo (sem atraso), mediante pagamento. Os preços vigentes são exibidos no bot, na página de preços e no link de pagamento antes da confirmação da compra.

### 3. Uso Responsável e Proibições
Você é inteiramente responsável pelo conteúdo que envia. É proibido usar o NekoMoji para criar, processar ou distribuir figurinhas contendo:
- Pornografia ou conteúdo sexual explícito (especialmente envolvendo menores)
- Violação de direitos autorais, marcas registradas ou propriedade intelectual
- Discurso de ódio, racismo, homofobia, xenofobia ou qualquer discriminação
- Violência gráfica, gore ou incitação ao crime
- Informações falsas ou enganosas (fake news)
- Spam, correntes ou esquemas fraudulentos

Violações graves podem resultar em suspensão imediata ou banimento. Quando houver plano Premium ativo, eventual reembolso ou manutenção do bloqueio será analisado conforme a gravidade da violação, evidências disponíveis, uso já realizado e legislação aplicável. Em casos de risco legal, abuso, fraude ou ordem de autoridade competente, a suspensão poderá ocorrer sem aviso prévio.

### 4. Limites Técnicos
- **Imagens:** Qualquer formato (JPG, PNG, GIF) - ajustamos automaticamente.
- **Vídeos:** Máximo 20MB e até 30 segundos por arquivo; a figurinha final poderá ter duração menor (hoje limitada a 10s).
- **Atraso de processamento (plano gratuito):** Para garantir a estabilidade do servidor, usuários do plano gratuito aguardam entre 5 e 10 segundos antes do processamento de cada figurinha. Usuários premium têm processamento instantâneo.
- **Rate limiting:** Máximo 15 mensagens por minuto e 300 por hora (anti-spam).

### 5. Pagamentos, Preços e Plano Premium
- **Processamento:** Pagamentos via Mercado Pago, conforme os meios disponíveis no link de pagamento — ativação automática após confirmação pelo processador de pagamento.
- **Comandos:** `!diario`, `!semanal` ou `!mensal` para receber o link de pagamento.
- **Não renovável:** Sem cobrança automática ou recorrente. Quando o período contratado expirar, o acesso retorna ao plano gratuito automaticamente.
- **Alteração de preços:** Os preços podem ser alterados para novas compras, mas o valor aplicável será sempre informado antes da confirmação do pagamento. Planos já pagos serão mantidos pelo prazo contratado, sem cobrança adicional. Links de pagamento podem expirar ou refletir o preço vigorante no momento da geração ou confirmação, conforme informado ao usuário.
- **Cancelamento e reembolso (Direito de Arrependimento e Uso Abusivo):**
  - **Plano Diário (24h):** Por possuir duração inferior ao prazo geral de arrependimento e ter seu objeto exaurido de imediato, uma vez decorrido o prazo de 24 horas da ativação, o serviço é considerado integralmente prestado e consumido, inviabilizando o direito de arrependimento (perda do objeto).
  - **Planos Semanal e Mensal:** O reembolso de cancelamentos efetuados dentro do prazo de **7 (sete) dias corridos** da ativação será integral. No entanto, para coibir a prática de má-fé e o enriquecimento sem causa (Art. 884 do Código Civil), caso seja constatado o uso abusivo do serviço na janela pré-cancelamento (como a criação em massa de figurinhas em volume flagrantemente desproporcional ao uso pessoal comum de um consumidor, visando a apropriação indevida dos recursos do plano ilimitado antes do pedido de estorno), o NekoMoji reserva-se o direito de reter o valor proporcional correspondente à prestação já usufruída ou recusar o reembolso integral mediante comprovação do abuso de direito (Art. 187 do Código Civil).
  - Após o prazo de 7 dias, cancelamentos e estornos não serão elegíveis, salvo em caso de falha técnica persistente e sem resolução comprovada por nossa equipe.

**Como solicitar cancelamento, arrependimento ou reembolso:**
Envie e-mail para **contato@nekomoji.chat** com o número de WhatsApp usado no bot, comprovante ou identificador do pagamento, data da compra e o pedido de estorno. Em falha técnica comprovada do nosso lado, como não ativação do Premium após pagamento confirmado, o período será creditado, reprocessado ou reembolsado conforme o caso.

### 5.2 Encerramento do serviço e Responsabilidade
O NekoMoji é um projeto pessoal mantido por uma pessoa física. A continuidade do serviço depende de fatores que podem estar fora do nosso controle, incluindo, sem limitação: mudanças na política de preços ou de uso da Meta (WhatsApp Business Platform), inviabilidade econômica de manutenção da operação, problemas de saúde, força maior ou qualquer outra circunstância relevante.
- **Direito de encerrar:** Reservamo-nos o direito de encerrar ou suspender a atividade do bot NekoMoji a qualquer momento, temporária ou permanentemente, especialmente caso as novas políticas tarifárias de mensagens de serviço da Meta (WhatsApp Business Platform) vigentes a partir de outubro de 2026 inviabilizem financeiramente a operação do bot.
- **Reembolso Pro-Rata em caso de encerramento:** Caso o serviço seja encerrado definitivamente, os usuários com planos Premium ativos (semanal ou mensal) vigentes na data do encerramento serão notificados e farão jus à devolução proporcional (*pro-rata*) do valor pago, correspondente estritamente aos dias restantes não utilizados até o término do plano contratado. A responsabilidade máxima do NekoMoji e do desenvolvedor em caso de interrupção ou descontinuidade das atividades fica contratualmente limitada à devolução desse saldo pro-rata, excluindo-se quaisquer outras multas contratuais, perdas e danos ou lucros cessantes.
- **Migração de dados:** Em caso de encerramento, faremos o melhor esforço para comunicar com antecedência e orientar sobre exportação de dados pessoais disponíveis nos sistemas sob nosso controle.
- **Responsabilidade:** Na máxima extensão permitida pela legislação aplicável, a responsabilidade do NekoMoji e eventuais indenizações decorrentes de falhas técnicas do serviço são regidas e limitadas de acordo com as normas imperativas do Código de Defesa do Consumidor (CDC). O serviço não se responsabiliza por perdas, danos ou instabilidades oriundas diretamente da infraestrutura de terceiros fora de seu controle razoável (como mudanças unilaterais ou indisponibilidade na WhatsApp Business Platform administrada pela Meta).

**📌 Contexto atual (julho de 2026)**
Em razão das novas cobranças da Meta para service messages a partir de outubro de 2026, o NekoMoji está ajustando seus preços de forma gradual e transparente. O objetivo é manter o serviço vivo e sustentável. Caso o cenário mude e a operação se torne inviável, comunicaremos os usuários com a maior antecedência possível.

### 5.3 Programa de indicação
O NekoMoji pode oferecer um programa de indicação por meio do comando `!indicar` e de links no domínio `nekomoji.chat`. Ao participar, você aceita as regras vigentes descritas de forma resumida abaixo e em detalhe na página Programa de indicação — regras e bônus (a qual integra estes termos por referência).
- **Indicado:** pode receber dias extras de Premium na primeira compra qualificada, conforme o plano pago, quando vinculado a um código de indicação válido antes ou no momento previsto pelo fluxo do bot.
- **Indicador:** pode receber dias extras de Premium quando um indicado vinculado realizar pagamentos qualificados; em regra, o bônus do indicador pode incidir sobre cada compra do indicado, nos termos exibidos pelo serviço.
- **Quando o indicado pode não receber boas-vindas:** o bônus de primeira compra obedece ao fluxo técnico do bot (por exemplo, segunda compra em diante não repete o extra; vínculo feito depois de já haver comprado Premium pode excluir o bônus de boas-vindas ao indicado, sem afetar o direito do indicador ao bônus nas compras seguintes do indicado, quando aplicável).
- **Códigos e canal:** códigos inválidos, tentativa de uso do próprio código, vínculo duplicado ou uso em contexto não suportado podem impedir o vínculo ou o bônus, conforme mensagens do bot.
- **Vínculo único:** cada conta de usuário pode ficar associada a um único código de indicação como indicado; não é permitido trocar de indicador após o vínculo, salvo quando o próprio serviço permitir expressamente em hipótese excepcional documentada.
- **Sem transferência de valor:** bônus são creditados como tempo de Premium no próprio serviço; não constituem saldo em dinheiro, não são negociáveis e dependem de confirmação de pagamento pelo processador (Mercado Pago).
- **Notificações e limites técnicos:** avisos no WhatsApp sobre bônus podem não ser entregues fora da janela de interação permitida pela plataforma; o registro do crédito no serviço prevalece sobre a notificação imediata. Falhas pontuais na gravação do bônus de indicação não devem, em regra, impedir a ativação do Premium correspondente ao pagamento principal.
- **Abuso e fraude:** contas falsas, manipulação de pagamentos, uso incompatível com estes termos ou com a legislação podem resultar em suspensão de bônus, do programa para o usuário ou de acesso ao serviço, sem prejuízo de medidas cabíveis.
- **Alterações:** valores de planos, tabelas de bônus, disponibilidade do programa e canais de comunicação podem ser alterados; continuam válidas as disposições da seção 10 (modificações) e comunicações pelo bot quando aplicável.

### 6. Disponibilidade do Serviço
O NekoMoji é operado em regime de melhor esforço e não garante disponibilidade ininterrupta ou livre de falhas. Interrupções podem ocorrer por manutenção programada, instabilidades ou mudanças na WhatsApp Business Platform / infraestrutura da Meta, infraestrutura própria, segurança, atualizações técnicas ou força maior, sem prejuízo dos direitos legais do consumidor em caso de falha comprovada do serviço.

### 7. Propriedade Intelectual
Você mantém os direitos que já possui sobre o conteúdo enviado. O NekoMoji apenas realiza a conversão técnica da mídia em figurinha e não reivindica propriedade sobre as mídias processadas.

### 8. Isenção de Responsabilidade e Conteúdo de Terceiros
- O NekoMoji é uma ferramenta automatizada - não monitoramos conteúdo privado de conversas.
- **Marco Civil da Internet (Artigo 19 da Lei nº 12.965/2014):** O NekoMoji atua como provedor de aplicação de internet intermediário para o processamento automatizado de mídias. O serviço não é responsável por danos decorrentes de conteúdo gerado por terceiros, mas cooperará ativamente com autoridades competentes mediante ordem judicial válida ou notificação em conformidade com as leis vigentes de direitos autorais para a remoção de materiais infringentes.
- O usuário é de sua exclusiva responsabilidade assegurar que possui as autorizações necessárias para uso e conversão técnica das figurinhas criadas, sem prejuízo das responsabilidades legais aplicáveis ao NekoMoji em caso de falha comprovada do serviço.

### 9. LGPD: acesso aos dados, exclusão da conta e comprovações
O tratamento de dados pessoais obedece à Lei Geral de Proteção de Dados (Lei 13.709/2018). Você pode solicitar confirmação de tratamento, acesso e cópia dos dados que mantemos sobre você, bem como a exclusão da conta e dos dados nos sistemas que controlamos, mediante e-mail formal para **privacidade@nekomoji.chat**, informando o número de celular completo (com DDI) associado ao uso do bot e o texto do pedido, conforme Política de Privacidade — seções 5.1 a 5.5.
Responderemos no prazo legal, e nas exclusões forneceremos comprovação do apagamento dos dados sob nossa gestão, na forma descrita na política. Dados de pagamento tratados exclusivamente pelo Mercado Pago, bem como retenções mínimas exigidas por lei ou segurança (ex.: metadados de transação), podem permanecer ou depender exclusivamente do provedor de pagamento — vide seção 5.4 da Política de Privacidade.

### 10. Modificações nos Termos
Podemos atualizar estes termos para refletir mudanças no serviço, em exigências legais ou em políticas de plataformas integradas. Sempre que houver modificações significativas (como mudanças relevantes em preços, suspensões ou nos limites operacionais do serviço), faremos o melhor esforço para notificar os usuários com aviso prévio mínimo de **15 (quinze) dias**, por meio de mensagem no bot ou destaque nas páginas oficiais. 
- O usuário de plano Premium ativo que discordar das novas regras poderá solicitar o cancelamento e obter reembolso proporcional pelo período restante contratado. 
- O uso continuado do serviço após a entrada em vigor dos novos termos configurará aceitação das alterações.

### 11. Independência, Marcas e Plataformas Externas
O NekoMoji é um serviço independente. Não somos a Meta, não somos o WhatsApp, não somos o Instagram, não representamos o X/Twitter, o Pinterest, o Tenor, o Giphy, a KLIPY.COM nem a KIKLIKO, Inc. Não há vínculo societário, franquia, parceria comercial oficial de marca ou endosso mutuo com nenhuma dessas empresas.
Ao usar o NekoMoji no WhatsApp, você também deve observar os Termos e Políticas do WhatsApp e demais regras da Meta aplicáveis a usuários do aplicativo.

**Instagram, X/Twitter, Pinterest, TikTok, Tenor, Giphy e KLIPY — uso de dados públicos:**
O recurso de download de mídia do Instagram, X/Twitter, Pinterest, TikTok, Tenor, Giphy e KLIPY acessa exclusivamente conteúdo publicamente disponível nessas plataformas — ou seja, publicações visíveis a qualquer pessoa sem autenticação. O NekoMoji não armazena credenciais, tokens ou dados privados dessas plataformas, e não mantém cópia permanente do conteúdo baixado: após a conversão em figurinha e o envio ao usuário, o arquivo é descartado da memória.
O NekoMoji não é afiliado, patrocinado nem endossado pela Meta (Instagram), pela X Corp, pela Pinterest, Inc., pelo Tenor (Google), pelo Giphy (Shutterstock), pela KLIPY.COM ou pela KIKLIKO, Inc. Utilizamos apenas o acesso público às URLs compartilhadas pelos próprios usuários, da mesma forma que qualquer navegador faria ao abrir o link.

Não possuímos afiliação, patrocínio ou endosso de:
- WhatsApp LLC / Meta Platforms, Inc. (exceto na qualidade de cliente dos serviços de API, conforme acima) — incluindo Instagram
- X Corp (Twitter / X)
- Pinterest, Inc.
- Tenor (Google LLC), Giphy (Shutterstock, Inc.) e KLIPY.COM / KIKLIKO, Inc.
- Mercado Pago S.A.

WhatsApp e Instagram são marcas da Meta Platforms, Inc. X e Twitter são marcas registradas da X Corp. Pinterest é marca registrada da Pinterest, Inc. TikTok é marca registrada da ByteDance Ltd. Tenor é marca da Google LLC. Giphy é marca da Shutterstock, Inc. KLIPY/KLIPY.COM é serviço da KIKLIKO, Inc. Mercado Pago é marca do Mercado Pago S.A. Todas as demais marcas citadas pertencem aos respectivos titulares.

### 12. Foro de Eleição
Para dirimir quaisquer controvérsias decorrentes da interpretação ou aplicação destes Termos de Uso e da Política de Privacidade ou do uso do serviço NekoMoji, fica eleito o foro da comarca de **Campinas, Estado de São Paulo**, com expressa exclusão de qualquer outro foro, por mais privilegiado que seja, aplicando-se integralmente a legislação da República Federativa do Brasil.

---
**Dúvidas sobre privacidade ou termos?**
- 📧 **Email geral e suporte:** contato@nekomoji.chat
- 📧 **Email de privacidade (DPO/Encarregado):** privacidade@nekomoji.chat
