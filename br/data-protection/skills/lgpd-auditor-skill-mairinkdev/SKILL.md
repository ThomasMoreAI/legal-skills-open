---
name: lgpd-auditor-skill-mairinkdev
title: LGPD Auditor
description: 'Auditoria LGPD para SaaS, microSaaS e sistemas: mapeia dados pessoais, bases legais, cookies, consentimento, segurança, direitos do titular, retenção, logs, terceiros, incidentes e regras de negócio em código. Use quando houver pedido de revisar compliance LGPD, privacidade, termos, cookies, dados sensíveis, autenticação, logs ou fluxos com dados pessoais.'
author: mairinkdev
author_url: https://github.com/mairinkdev/lgpd-auditor-skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
sources:
- title: Lgpd Control Matrix
  path: references/lgpd-control-matrix.md
---

# LGPD Auditor

Atue como auditor técnico de privacidade/LGPD para SaaS, microSaaS e sistemas web/mobile. Entregue achados acionáveis por arquivo/linha, sem afirmar “compliance 100% garantido”. Separe: **correção técnica**, **requisito funcional**, **risco jurídico para revisão humana**.

## Regra obrigatória de atualização

Antes de concluir qualquer interpretação legal, verificar fontes oficiais quando houver ferramenta de web disponível. Use primeiro:

- Lei compilada no Planalto: `https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm`
- ANPD — Materiais educativos/publicações: `https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes`
- ANPD — Regulamentações vigentes: `https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd`
- ANPD — Comunicação de Incidente de Segurança: `https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis`
- Diário Oficial/IN.gov.br quando a ANPD apontar resolução oficial.

Se não houver web: declare que a revisão legal foi feita com base no conhecimento disponível e marque como pendência: **“validar contra fontes oficiais ANPD/Planalto antes de produção”**. Não invente prazos, resoluções ou obrigações.

## Modo econômico de tokens

1. Comece com inventário, não leia tudo de uma vez.
2. Ignore `node_modules`, `.next`, `dist`, `build`, `.turbo`, coverage, lockfiles grandes e assets.
3. Para revisão de feature/diff, leia apenas `git diff`, arquivos alterados e dependências diretas.
4. Para auditoria completa, faça varredura por camadas: rotas, schemas, migrations, auth, integrações, logs, políticas e testes.
5. Carregue referência detalhada só quando necessário:
   - Matriz completa: `references/lgpd-control-matrix.md`
   - Template de relatório: `templates/relatorio-lgpd.md`
   - Template de plano: `templates/plano-correcao.md`
6. Use `scripts/lgpd_scan.sh` se quiser uma varredura inicial estática sem ler o repo inteiro.

## Classificação de severidade

- **P0 Bloqueador**: risco direto de vazamento, segredo exposto, ausência de autenticação/autorização em dados pessoais, logs com dados sensíveis, exclusão/exportação inexistente quando o produto exige, incidente sem fluxo, base legal/consentimento claramente incompatível, uso de dados sensíveis/crianças sem proteção específica.
- **P1 Alto**: falta de retenção/deleção, consentimento/cookies incompletos, terceiros sem contrato/base documentada, política divergente do sistema, IA recebendo dados pessoais sem minimização, analytics antes de consentimento quando aplicável.
- **P2 Médio**: transparência insuficiente, mensagens ruins, falta de testes de privacidade, auditoria incompleta, excesso de dados coletados.
- **P3 Baixo**: nomenclatura, documentação, melhoria de UX, refino de copy e evidências.

## Procedimento por tipo de tarefa

### `/lgpd-auditor auditoria-rapida`

Objetivo: achar riscos óbvios rápido.

1. Mapear stack, apps, APIs e bancos.
2. Rodar/listar buscas por PII, cookies, logs, auth, analytics, pagamentos, IA e storage.
3. Revisar rotas críticas: cadastro/login, perfil, integrações, checkout, webhooks, admin, export/delete account.
4. Entregar top 10 achados com arquivo/linha, impacto e correção.

### `/lgpd-auditor auditoria-completa`

Objetivo: gerar diagnóstico técnico + funcional + jurídico-operacional.

1. Identificar se o sistema atua como controlador, operador ou ambos por fluxo.
2. Criar inventário de dados:
   - dado pessoal comum;
   - dado sensível;
   - dado de criança/adolescente;
   - dado financeiro/pagamento;
   - dado de autenticação;
   - dado de localização;
   - logs, eventos, analytics e observabilidade;
   - dados enviados a IA/terceiros.
3. Mapear finalidades, bases legais candidatas, retenção e origem/destino de dados.
4. Auditar frontend, backend, banco, filas, webhooks, emails, IA, analytics, storage, backups, admin e documentação pública.
5. Validar direitos do titular:
   - confirmação/acesso;
   - correção;
   - exportação/portabilidade quando aplicável;
   - anonimização/bloqueio/eliminação quando aplicável;
   - revogação de consentimento;
   - informações sobre compartilhamento;
   - canal de contato/encarregado quando aplicável.
6. Validar segurança:
   - autenticação, sessões, cookies, CSRF, CORS;
   - RBAC/ABAC;
   - rate limit;
   - criptografia em trânsito;
   - hashing de senhas/tokens;
   - mascaramento/redação de logs;
   - segregação tenant/user;
   - webhooks assinados;
   - backup/restore;
   - monitoramento e resposta a incidentes.
7. Validar documentos:
   - política de privacidade;
   - termos de uso;
   - política/banner de cookies;
   - contratos com operadores/suboperadores;
   - registro de tratamento interno;
   - plano de resposta a incidentes;
   - política de retenção.
8. Entregar relatório completo no formato de `templates/relatorio-lgpd.md`.

### `/lgpd-auditor feature`

Objetivo: revisar uma feature antes/depois da implementação.

1. Entender finalidade e dados pessoais envolvidos.
2. Exigir minimização: coletar só o necessário.
3. Verificar base legal candidata e transparência.
4. Verificar consentimento quando a base depender dele.
5. Verificar logs, eventos, analytics e IA.
6. Adicionar testes de privacidade quando possível.
7. Não bloquear por burocracia se não houver tratamento de dados pessoais, mas registrar evidência.

### `/lgpd-auditor diff`

Objetivo: revisar mudanças atuais.

1. Ler `git diff --stat`, `git diff --name-only`, depois diffs relevantes.
2. Priorizar arquivos que mexem em:
   - auth/sessão;
   - user/profile/account;
   - payments/webhooks;
   - analytics/tracking;
   - AI/prompts/providers;
   - logs/telemetry;
   - database/migrations/schemas;
   - admin/RBAC;
   - exports/deletion/retention;
   - policies/legal pages.
3. Entregar achados com patch sugerido quando seguro.

### `/lgpd-auditor politicas`

Objetivo: revisar textos públicos.

1. Conferir se política/termos/cookies refletem o sistema real.
2. Procurar promessas que o código não cumpre.
3. Marcar lacunas: finalidades, bases, terceiros, retenção, direitos, contato, incidentes, crianças/adolescentes, transferências internacionais, analytics/cookies.
4. Sugerir copy clara, sem juridiquês desnecessário, e marcar pontos que precisam de advogado.

## Buscas úteis no código

Use `rg`/`grep` de forma direcionada:

- PII comum: `email|phone|telefone|cpf|cnpj|document|rg|passport|birth|nascimento|address|endereco|cep|pix|bank|account`
- Sensíveis: `health|saude|medical|religion|religiao|politic|politica|race|racial|biometric|biometria|sexual|genetic|genetico`
- Auth/session: `password|hash|token|jwt|session|cookie|csrf|oauth|refresh`
- Logs: `console.log|logger|debug|print|Sentry|captureException|captureMessage`
- Cookies/storage: `localStorage|sessionStorage|document.cookie|Set-Cookie|cookies|consent`
- Analytics: `gtag|GA4|posthog|mixpanel|hotjar|clarity|pixel|Meta Pixel|TikTok`
- IA: `openai|anthropic|claude|gemini|llm|prompt|embedding|vector`
- Direitos titular: `deleteAccount|exportData|privacy|consent|retention|anonymize|erase|portability|lgpd`
- Terceiros: `resend|stripe|mercado pago|mercadopago|pluggy|sentry|discord|webhook|storage|s3|cloudinary`

## Regras de análise

- Nunca aceite “tem política de privacidade” como suficiente: compare com código real.
- Nunca considere consentimento válido se ele for obrigatório para tudo sem alternativa, salvo quando for realmente necessário ao serviço.
- Diferencie cookies essenciais de analytics/marketing.
- Não envie dados pessoais para IA sem minimização, transparência e controle.
- Dados pessoais em logs são achado automático; dados sensíveis/financeiros em logs são P0/P1.
- Admin deve ter RBAC, trilha de auditoria e mínimo privilégio.
- SaaS multi-tenant deve provar isolamento por `userId`, `tenantId` ou equivalente em todas as consultas.
- Webhook de pagamento/Open Finance/email deve ter assinatura/idempotência e não deve vazar payload sensível em log.
- Exportação/deleção de conta deve respeitar obrigações legais, fiscais, antifraude e retenção mínima; quando não puder apagar, justificar bloqueio, anonimização ou retenção legal.
- Política pública deve refletir fornecedores reais: pagamentos, email, analytics, IA, hospedagem, observabilidade, banco e storage.
- Para menores/crianças, dados sensíveis, saúde, biometria, crédito, Open Finance ou grande volume, elevar rigor e sugerir RIPD/DPIA.

## Formato de saída obrigatório

Comece com:

1. **Veredito**: `Bloqueado para produção`, `Pode ir para beta fechado com restrições`, `Aprovado com ressalvas`, ou `Sem achados relevantes no escopo`.
2. **Escopo analisado**: arquivos, fluxos e fontes oficiais consultadas.
3. **Resumo executivo**: até 8 bullets.
4. **Achados por severidade**:
   - ID
   - severidade
   - arquivo:linha
   - evidência
   - risco LGPD
   - correção técnica
   - requisito funcional/regra de negócio
   - teste recomendado
   - dono sugerido: frontend/backend/devops/produto/jurídico
5. **Mapa de dados pessoais**.
6. **Checklist de produção LGPD**.
7. **Pendências jurídicas**.
8. **Próximos commits recomendados**.

Se não conseguir verificar algo, escreva `Não verificado` e diga exatamente o que falta.
