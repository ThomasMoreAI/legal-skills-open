# Matriz de Controle LGPD para SaaS, MicroSaaS e Sistemas

Use esta matriz quando a auditoria exigir profundidade. Ela é técnica e operacional; não substitui revisão jurídica.

## 1. Governança e responsabilidade

### Controles esperados
- Identificar o papel por fluxo: controlador, operador ou controlador conjunto.
- Definir responsável interno por privacidade/encarregado quando aplicável.
- Manter registro básico de operações de tratamento: dado, finalidade, base legal candidata, origem, destino, retenção, operador/suboperador, risco.
- Ter canal de contato para titulares.
- Ter processo de revisão de novas features com privacy by design.

### Evidências no código/produto
- Página pública de privacidade.
- Página/canal de contato.
- Registro de fornecedores e variáveis de ambiente.
- Issues/checklists de privacy review.
- Fluxos implementados para direitos do titular.

### Red flags
- “A gente coleta tudo porque pode ser útil depois”.
- Sem dono claro de privacidade.
- Política pública genérica que não cita integrações reais.
- Features novas com analytics/IA sem revisão.

## 2. Inventário e classificação de dados

### Categorias mínimas
- Identificação: nome, e-mail, telefone, documento.
- Conta/autenticação: senha, hash, token, sessão, OAuth.
- Financeiro: transações, pagamentos, bancos, PIX, faturas, Open Finance.
- Sensíveis: saúde, biometria, religião, opinião política, dados genéticos, vida sexual, origem racial/étnica.
- Menores: criança/adolescente.
- Localização: GPS, endereço, IP quando usado para identificação/segurança.
- Comportamental: eventos, analytics, device ID, cookies, session replay.
- Conteúdo gerado pelo usuário: mensagens, uploads, comprovantes, notas, anexos.
- Dados para IA: prompts, contexto enviado, embeddings, respostas, logs de modelo.

### Controles esperados
- Coletar apenas o necessário para finalidade concreta.
- Evitar campos opcionais invasivos.
- Separar dados sensíveis e aplicar controles adicionais.
- Mascarar dados em UI/log/admin quando não forem necessários.
- Evitar replicação desnecessária em cache, fila, analytics, logs e storage.

## 3. Bases legais candidatas e finalidade

### O que verificar
- Cada fluxo com dado pessoal deve ter finalidade clara.
- A base legal candidata deve ser coerente com finalidade.
- Consentimento deve ser específico, destacado e revogável quando usado.
- Execução de contrato pode cobrir dados necessários para prestação do serviço.
- Obrigação legal/regulatória pode justificar retenção fiscal, contábil, antifraude ou segurança.
- Legítimo interesse exige teste de balanceamento e transparência; evite usá-lo como desculpa genérica.
- Dados sensíveis têm hipóteses mais restritas e exigem rigor maior.

### Red flags
- Checkbox único para tudo.
- Consentimento pré-marcado.
- Serviço bloqueado por recusa de cookie de marketing.
- Dados coletados sem finalidade mostrada ao usuário.
- Reuso de dados para marketing/IA sem transparência.

## 4. Transparência e notices

### Frontend
- Cadastro/onboarding deve linkar política e termos.
- Telas de permissões devem explicar o motivo da coleta.
- Integrações bancárias, calendário, saúde, pagamentos ou IA precisam de explicação contextual.
- Linguagem simples.

### Backend
- Evitar respostas que vazem dados de outros usuários.
- Mensagens de erro não devem revelar tokens, segredo, CPF completo, payload de gateway ou stack trace.

### Red flags
- Política diz “não compartilhamos dados”, mas código usa Sentry/analytics/email/payment/IA.
- Política não cita provedores reais.
- Ausência de retenção e direitos do titular.

## 5. Cookies, storage e analytics

### Classificação
- Essenciais: sessão, CSRF, segurança, preferências indispensáveis.
- Funcionais: preferências não essenciais.
- Analytics: medição/telemetria.
- Marketing: ads, pixels, remarketing, cross-site tracking.

### Controles esperados
- Não disparar analytics/marketing antes da escolha quando o consentimento for necessário.
- Consentimento granular por categoria.
- Botão de recusar tão acessível quanto aceitar quando aplicável.
- Registro da escolha com versão da política.
- UI para alterar consentimento.
- Cookies com `Secure`, `HttpOnly` quando não precisam ser lidos pelo JS, `SameSite` adequado e escopo mínimo de domínio/path.

### Red flags
- `localStorage` com token sensível.
- `document.cookie` com token acessível ao JS.
- Pixels carregados no primeiro render.
- Banner falso que só informa e não controla nada.

## 6. Direitos do titular

### Funcionalidades desejáveis
- Solicitar acesso aos dados.
- Exportar dados quando aplicável.
- Corrigir dados cadastrais.
- Excluir conta ou solicitar exclusão.
- Revogar consentimentos.
- Ver compartilhamentos principais.
- Canal de privacidade.

### Regras técnicas
- Validar identidade antes de exportar/excluir.
- Exportação deve pertencer ao usuário autenticado/tenant correto.
- Deleção deve lidar com dados que não podem ser apagados por obrigação legal ou prevenção à fraude.
- Anonimização deve ser irreversível na prática.
- Criar audit trail da solicitação sem guardar dados excessivos.

### Red flags
- Endpoint `/users/:id/delete` sem checar dono/admin.
- Exportação com dados de outros tenants.
- Delete remove usuário mas mantém PII em logs, invoices, analytics e storage.
- Sem prazo/processo interno para responder solicitações.

## 7. Segurança técnica

### Autenticação e sessão
- Hash forte de senha.
- Tokens com expiração.
- Refresh token protegido.
- Cookies seguros.
- Proteção CSRF em mutations com cookie.
- Rate limit para login, reset e endpoints sensíveis.
- MFA/2FA para admin quando possível.

### Autorização
- Verificar `userId`, `tenantId`, roles e permissões no backend.
- Não confiar no frontend.
- Admin endpoints separados e auditados.

### Banco e armazenamento
- Migrations revisadas.
- Índices por tenant quando necessário.
- Soft delete/anonymization planejados.
- Backups protegidos.
- Segredos fora do repositório.
- Storage privado por padrão.

### Logs e observabilidade
- Redação/máscara para e-mail, CPF, telefone, token, payload bancário, comprovante, prompt de IA.
- Sentry/telemetria sem dados sensíveis.
- Não logar headers de Authorization/Cookie.
- Não logar body completo de webhook.

### Red flags P0/P1
- Falta de autenticação em rota de dados pessoais.
- IDOR/multi-tenant leak.
- Logs com token, CPF, extrato, comprovante, prontuário, dado de saúde.
- Webhook sem assinatura/idempotência.
- Admin sem RBAC.
- CORS permissivo com credenciais.

## 8. Retenção, deleção e anonimização

### Controles esperados
- Política de retenção por categoria.
- Jobs de limpeza quando aplicável.
- Anonimização de dados históricos que não precisam identificar o usuário.
- Backups com retenção definida.
- Exclusão de storage/anexos.
- Deleção lógica só quando houver motivo claro; senão, apagar/anonimizar.

### Perguntas obrigatórias
- Por quanto tempo guardar conta inativa?
- Por quanto tempo guardar logs?
- Dados financeiros precisam ficar por obrigação legal?
- O usuário pode apagar anexos/comprovantes?
- O que acontece com dados enviados a terceiros?

## 9. Terceiros, operadores e transferências

### Verificar fornecedores
- Hospedagem/Vercel/Railway/AWS/GCP/Azure.
- Banco gerenciado.
- Pagamentos: Stripe, Mercado Pago, Asaas, AbacatePay etc.
- Email: Resend, Sendgrid, SES etc.
- Analytics: PostHog, GA4, Mixpanel, Hotjar, Clarity.
- Observabilidade: Sentry, Datadog etc.
- IA: OpenAI, Anthropic, Google, Groq, etc.
- Storage: S3, Cloudinary, Firebase Storage.
- Open Finance/Open Banking: Pluggy e similares.

### Controles esperados
- Listar operador/suboperador.
- Conferir termos/DPA quando aplicável.
- Enviar mínimo necessário.
- Evitar dados sensíveis em fornecedores que não precisam deles.
- Informar transferência internacional quando aplicável.
- Plano de saída/remoção quando fornecedor é trocado.

## 10. Incidentes de segurança

### Controles esperados
- Runbook de incidente.
- Contatos responsáveis.
- Critério de severidade.
- Registro de data/hora de conhecimento.
- Preservação de evidências.
- Comunicação ao controlador quando o sistema for operador.
- Processo para comunicar ANPD/titulares quando exigido.
- Templates de comunicação.
- Monitoramento e alertas.

### Red flags
- Sem logs mínimos para investigar.
- Logs têm dados sensíveis demais.
- Ninguém sabe quem aciona jurídico/comunicação.
- Operador não tem obrigação contratual de notificar controlador.

## 11. IA, automações e decisões automatizadas

### Verificar
- Prompts recebem PII?
- Contexto financeiro/saúde/documentos vai para modelo externo?
- Existe opt-out/explicação?
- Há retenção pelo provedor?
- Dados são usados para treino?
- Existe revisão humana quando há impacto relevante?
- A UI deixa claro que IA pode errar?
- Logs de prompt estão mascarados?

### Red flags
- Enviar extrato completo para IA sem minimização.
- Usar IA para score/decisão sem explicação.
- Gravar prompts com dados sensíveis em analytics/log.
- Expor contexto de um usuário para outro por cache/memory.

## 12. Checklist por camada

### Frontend
- Links de privacidade/termos no cadastro.
- Consentimento granular quando aplicável.
- Preferências de cookies.
- Delete/export account.
- Mensagens claras em integrações.
- Mascaramento de dados em tela/admin.
- Sem analytics/marketing antes da autorização aplicável.
- Formulários coletam mínimo necessário.

### Backend
- Auth e RBAC por rota.
- Validação de entrada.
- Rate limit.
- Logs redigidos.
- Webhooks assinados e idempotentes.
- CORS/CSRF corretos.
- Serviços de export/delete/retention.
- Testes cobrindo isolamento de usuário/tenant.

### Banco
- Tabelas com PII identificadas.
- Separação/criptografia quando necessário.
- Retenção por tabela.
- Delete/anonymization planejado.
- Índices para queries por usuário/tenant.
- Migrações sem dados reais.

### DevOps
- Segredos fora do Git.
- Variáveis obrigatórias validadas no boot.
- Backups com retenção.
- Monitoramento de incidentes.
- Acesso mínimo aos ambientes.
- Logs centralizados com retenção curta.

### Produto/Jurídico
- Registro de tratamento.
- Políticas alinhadas ao código.
- Contratos com operadores.
- Processo de direitos do titular.
- Plano de incidente.
- Revisão de legítimo interesse quando usado.
- RIPD/DPIA para fluxos de alto risco.

## 13. Smells de código

- `console.log(req.body)`
- `logger.info({ user })`
- `JSON.stringify(payload)` em webhook.
- `select *` sem escopo de usuário/tenant.
- `where id = params.id` sem `userId`.
- `NEXT_PUBLIC_*` contendo segredo.
- `localStorage.setItem("token", ...)`
- Cookie sem `Secure`/`HttpOnly` para sessão.
- `Access-Control-Allow-Origin: *` com credenciais.
- Admin routes sem role check.
- Endpoint de delete sem autenticação forte.
- Export em CSV com dados de outro usuário.
- Analytics identificado com e-mail/CPF sem necessidade.
- Prompt de IA montado com dados brutos sem minimização.
- Storage público para comprovantes/documentos.

## 14. Evidências mínimas para “beta com restrições”

- Política de privacidade realista e visível.
- Termos básicos.
- Consent/cookies coerente com tracking real.
- Auth/RBAC revisado.
- Sem P0 conhecido.
- Logs redigidos.
- Fornecedores listados.
- Processo manual de direitos do titular.
- Processo manual de incidente.
- Backups e secrets minimamente seguros.
- Plano de correção P1 com prazo.
