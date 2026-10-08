# Checklist: Termos de Uso (validação final)

> Validação do `termos-de-uso.md` antes de publicar. Cada item ausente é risco jurídico concreto. Cruzar com `references/08-termos-cdc.md`, `09-termos-mci-stf.md`, `10-clickwrap-aceite.md`.

## A. Identificação e formação (CDC + CC)

- [ ] **Razão social, CNPJ/CPF, endereço, e-mail** de contato funcional, todos presentes
- [ ] **Data de última atualização** + **versão** + **data de entrada em vigor** visíveis no topo
- [ ] **Aceite por clickwrap** (checkbox vazio por padrão), com botão desabilitado enquanto não marcado
- [ ] **Duas caixas separadas** para Termos e Política de Privacidade (quando consentimento LGPD)
- [ ] Para serviço de **alto risco** (financeiro, saúde): considerar **scroll-wrap** (botão só habilita após scroll completo)
- [ ] **Tabela `tos_acceptance` criada** com user_id, document_type, document_version, document_hash, accepted_at, ip_truncated, user_agent, acceptance_method
- [ ] **Hash do documento** calculado e armazenado a cada nova versão
- [ ] **URL versionada permanente** para cada versão (`/legal/termos/v3.2`)
- [ ] **Versões anteriores acessíveis** (mínimo 5 anos)

## B. Conteúdo obrigatório (19 seções)

- [ ] **1. Cabeçalho e aceitação** explícito
- [ ] **2. Definições** (glossário curto)
- [ ] **3. Identificação do prestador**
- [ ] **4. Objeto / Descrição do serviço** + **disclaimers de escopo** ("não substitui consulta médica/jurídica/etc")
- [ ] **5. Cadastro, conta e idade mínima**, compatível com LGPD art. 14
- [ ] **6. Planos, pagamento e cobrança** (se aplica), incluindo direito de arrependimento CDC art. 49
- [ ] **7. Uso permitido e proibido**, lista específica + gradação de sanção
- [ ] **8. Conteúdo do Usuário** (UGC, se aplica), propriedade, licença, notice & takedown
- [ ] **9. Propriedade intelectual da Plataforma**
- [ ] **10. Privacidade**, remissão à Política (sem duplicar conteúdo)
- [ ] **11. Disponibilidade, manutenção, modificações**
- [ ] **12. Limitação de responsabilidade**, ressalva CDC + LGPD
- [ ] **13. Suspensão e encerramento da Conta**, com contraditório
- [ ] **14. Alteração destes Termos**, 30 dias + re-aceite material
- [ ] **15. Foro e lei aplicável**: BR + domicílio do consumidor (B2C)
- [ ] **16. Disposições finais**, severability, integralidade, comunicações
- [ ] **17. Histórico de versões**

## C. Anti-cláusulas-abusivas (art. 51 CDC)

Nenhuma das cláusulas abaixo presente:

- [ ] **(I)** Exoneração total de responsabilidade por vícios (em B2C)
- [ ] **(II)** Subtração de opção de reembolso ("não reembolsamos em nenhuma hipótese")
- [ ] **(III)** Transferência de responsabilidade a terceiros quando o app intermedia
- [ ] **(IV)** Desvantagem exagerada genérica
- [ ] **(V)** Inversão do ônus da prova em prejuízo do consumidor
- [ ] **(VI/VII)** Arbitragem compulsória pra consumidor
- [ ] **(IX)** Variação unilateral de preço sem índice objetivo
- [ ] **(X)** Cancelamento unilateral sem critério objetivo e sem contraditório
- [ ] **(XI)** Ressarcimento unilateral de custos de cobrança
- [ ] **(XII)** Cláusula de "renúncia" a direitos (forma proibida)
- [ ] **(XIII)** Modificação unilateral do contrato sem aviso prévio e re-aceite material

## D. Limitação de responsabilidade

- [ ] **B2C:** sem cap monetário fechado (defensável)
- [ ] **B2B sofisticado:** cap em 12 meses pagos é admissível, com cuidado
- [ ] Em qualquer caso: ressalva expressa para **dolo, culpa grave, danos a direitos da personalidade, vícios CDC, vazamento de dados LGPD**

## E. Foro e arbitragem

- [ ] **B2C:** foro do domicílio do consumidor (CDC art. 101)
- [ ] **B2B:** foro de eleição (sede da empresa), válido
- [ ] **Arbitragem:** ausente em B2C (ou facultativa pós-conflito, conforme Lei 9.307/96 art. 4º §2º)
- [ ] **Lei aplicável:** brasileira sempre

## F. Suspensão/exclusão com contraditório (STJ 2024)

- [ ] Hipóteses de suspensão/exclusão **listadas objetivamente**
- [ ] Gradação (advertência → suspensão → exclusão)
- [ ] **Notificação prévia** ao Usuário (salvo urgência)
- [ ] **Prazo de contraditório** explícito (5-15 dias úteis)
- [ ] **Direito de exportar dados** antes da exclusão (LGPD art. 18 V)
- [ ] **Conta inativa:** prazo claro (12-24 meses) com aviso prévio
- [ ] Retenção pós-encerramento respeitando matriz de retenção LGPD

## G. UGC (se aplica)

- [ ] **Propriedade mantida pelo Usuário** (não cessão!)
- [ ] **Licença** explicitamente não-exclusiva, gratuita, sublicenciável (limitado), revogável
- [ ] **Finalidade limitada** à prestação do serviço
- [ ] **NÃO inclui** treinamento de IA salvo consentimento específico
- [ ] **Direitos morais** ressalvados (Lei 9.610/98 art. 27)
- [ ] **Canal de notice & takedown** publicado (link em `legal/notice-takedown.md`)
- [ ] Cláusula sobre **regime escalonado pós-Tema 987 STF** (rol "dever de cuidado")
- [ ] **Notificação reversa** ao publicador prevista (contraditório de 7 dias)
- [ ] Compromisso de **relatório de transparência anual**

## H. Pagamento (se aplica: CDC art. 49)

- [ ] **Preço, periodicidade, forma de cobrança** descritos
- [ ] **Renovação automática** com aviso prévio (7 dias)
- [ ] **Direito de arrependimento 7 dias** explícito
- [ ] **Reajuste:** mínimo 12 meses + índice objetivo + 30 dias aviso
- [ ] **Inadimplência:** suspensão com aviso, exclusão com prazo de regularização
- [ ] **Cancelamento self-service** em paridade com contratação (mesmo número de cliques)
- [ ] **Reembolso proporcional** do período não usufruído

## I. Alteração dos Termos (CDC art. 51 XIII)

- [ ] **E-mail 30 dias** antes da entrada em vigor
- [ ] **Banner in-app** persistente
- [ ] **Modal blocker + re-aceite ativo** para mudanças materiais
- [ ] **Direito de rescindir sem ônus** se discordar
- [ ] **Histórico de versões** mantido

## J. Privacidade: separação dos documentos

- [ ] **Documentos separados:** `termos.md` ≠ `privacidade.md`
- [ ] **Termos não duplicam** conteúdo da Política (só remissão)
- [ ] **Política não tem cláusulas contratuais** (só transparência LGPD)
- [ ] **Dois links distintos** no rodapé e no cadastro
- [ ] **Checkboxes separados** quando consentimento for base legal

## K. Idioma e linguagem (CDC art. 31)

- [ ] Documento em **PT-BR**
- [ ] Linguagem **clara**, sem juridiquês desnecessário
- [ ] Frases curtas, parágrafos curtos
- [ ] **Destaque visual** para cláusulas que limitem direitos (art. 54 §4º CDC)
- [ ] Se houver versão em outro idioma: cláusula "prevalece a versão em PT-BR"
- [ ] **Sem** termos como "o usuário renuncia ao direito de..."

## L. Setoriais (se aplica)

### Fintech
- [ ] KYC declarado (Circular BCB 3.978/2020)
- [ ] CET, prazos de liquidação, chargeback explícitos
- [ ] Comunicação ao COAF quando aplicável
- [ ] **Não usa "banco"/"bank"** sem licença BCB (proibição nov/2025)

### Healthtech / Telemedicina
- [ ] Sigilo médico expresso (CFM)
- [ ] CRM válido + registro do atendimento
- [ ] Dado sensível → LGPD art. 11 + RIPD
- [ ] Consentimento livre e esclarecido pra telessaúde **separado** dos Termos

### Edtech pra menor
- [ ] Verificação de idade robusta
- [ ] Consentimento parental verificável < 13 anos
- [ ] ECA Digital (Lei 15.211/2025), notificação parental, transparência algorítmica
- [ ] Restrição de publicidade direcionada

### Govtech
- [ ] Remissão à Lei 13.460/2017 (Código de Defesa do Usuário do Serviço Público)
- [ ] LAI (Lei 12.527/2011)
- [ ] Carta de Serviços obrigatória
- [ ] Canal de ouvidoria

## M. Output final

Quando todos os checks aplicáveis estiverem marcados:

- [ ] **Repositório:** `<projeto>/legal/termos-de-uso.md`
- [ ] **Publicação web:** rota `/termos` (Next.js: `app/(legal)/termos/page.tsx`)
- [ ] **Link no footer:** todas as páginas, ao lado da Política de Privacidade
- [ ] **Migration aplicada:** tabela `tos_acceptance` criada no banco
- [ ] **Fluxo de cadastro** atualizado: checkbox + log de aceite
- [ ] **Commit:** `chore(legal): publica Termos de Uso vYYYY-MM-DD`
