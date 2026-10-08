# 14: Analytics, Tracking, Telemetria: comparação e escolhas privacy-first

> Comparação ferramenta-a-ferramenta do que cada uma coleta, base legal LGPD, DPA, e o **default recomendado** (escolhas privacy-first que funcionam pra qualquer app novo). Atualizado pra cenário pós-Resolução CD/ANPD nº 32/2026 (UE = país adequado).

## Contexto regulatório que muda tudo (2025-2026)

Três fatos reorganizam o jogo:

1. **Cláusulas-padrão obrigatórias desde 23/08/2025.** Res. 19/2024 da ANPD encerrou período de graça. Transferência baseada em cláusula contratual precisa usar **SCC-ANPD**, ou equivalente reconhecido (SCC-EU), ou BCR, ou exceção. **Vendor sem DPA atualizado pós-2025 = risco direto.**

2. **EU agora é "país adequado"** (Resolução CD/ANPD nº 32/2026). Transferir dado pra processador hospedado na UE **dispensa SCC**. Favorece Plausible, Crisp, Sentry-EU, Mixpanel-EU, etc.

3. **Guia de Cookies ANPD (rev. jan/2025)** diferencia:
   - **Necessários** → legítimo interesse (com direito de oposição informado)
   - **Funcionais/Publicidade** → **consentimento obrigatório**
   - **Analíticos** → admite legítimo interesse **se** coleta for proporcional, anonimizada, titular informado com opt-out. **Não é cheque em branco**: GA4 padrão **não** se enquadra; Plausible/Matomo bem configurados, sim.

E o precedente externo que pesa: **CNIL declarou GA4 incompatível com GDPR** em 2022 (reafirmou 2025). Não vincula ANPD, mas é cenário base que processos BR vão citar.

---

## 1. Analytics web/produto

### 1.1 Google Analytics 4 (GA4)

| | |
|---|---|
| **Coleta** | Cookies `_ga`, `_ga_<container>`, `_gid`; IP (anonimizável); `client_id`; UA; eventos custom; sessão; geo (cidade); referrer; demographics inferidas (se ativado). Aceita `user_id` opcional → PII direta |
| **Sensibilidade** | **Alta** (default). Média/baixa só com server-side + anonimização agressiva |
| **Base legal** | **Consentimento** (art. 7º I). ANPD trata cookies analíticos GA4 como categoria que exige consentimento, dado cruzamento com Google Ads |
| **DPA + SCC** | Google Ads Data Processing Terms. SCCs-EU adicionadas; **SCC-ANPD ainda não referenciadas no DPA padrão** (verificar versão): **risco** |
| **Categoria cookie** | Analytics + (de fato) Marketing |
| **Alternativa privacy-first** | Plausible, Matomo (self-host), Umami, Fathom, Simple Analytics |
| **Mitigações** | Server-side GA4 via GTM Server Container em região BR/UE; reduzir retenção pra 2 meses; desativar Google Signals; Consent Mode v2 estrito; **não** passar `user_id` se evitável |

### 1.2 Plausible Analytics ⭐ default recomendado

| | |
|---|---|
| **Coleta** | Pageview, referrer, país (via IP que é descartado), device type, browser. **Sem cookie, sem fingerprint persistente**, hash diário de IP+UA+domínio rolando a cada 24h |
| **Sensibilidade** | **Baixa** |
| **Base legal** | **Legítimo interesse** (art. 7º IX), defensável, alinhado ao Guia ANPD jan/2025 |
| **DPA + SCC** | Estoniana, hospedagem UE (Hetzner). Pós-Res. 32/2026, **dispensa SCC**. DPA assinável |
| **Categoria cookie** | **Nenhum cookie.** Não entra no banner |
| **Mitigações** | Self-host se quiser zero transferência internacional |

**Nota:** debate sobre processamento transiente de IP: EDPB 2023 sugere que ainda assim caberia base legal. Conclusão prática: **não precisa banner de cookie**, mas precisa **menção na política** com direito de oposição.

### 1.3 PostHog ⭐ default recomendado pra product analytics

| | |
|---|---|
| **Coleta** | Eventos custom, autocaptura de clicks/forms (configurável), pessoas com `distinct_id`, propriedades, **session replay**, feature flags, surveys |
| **Sensibilidade** | **Alta** com replay; **média** sem replay; **baixa** em modo agregado |
| **Base legal** | Consentimento se replay/identify ligados. Legítimo interesse só pra eventos agregados anônimos |
| **DPA + SCC** | DPA disponível. Cloud UE (Frankfurt) **ou** US: **escolher UE** pra projetos BR. Self-host possível |
| **Categoria cookie** | Analytics + Funcional (session replay) |
| **Mitigações** | `mask_all_inputs: true` e `mask_all_text: true` no replay; classe `ph-no-capture` em divs sensíveis; `sanitize_properties` ou `before_send` pra scrub de PII; **nunca** chamar `posthog.identify(email)` sem hash, use ID interno; desligar autocapture em rotas autenticadas |

### 1.4 Mixpanel

| | |
|---|---|
| **Coleta** | Eventos + propriedades, `distinct_id`, perfil (People), funis, cohorts |
| **Base legal** | Consentimento (uso típico). Legítimo interesse só em modo agregado/anônimo (Mixpanel Lite) |
| **DPA + SCC** | DPA com SCCs-EU. **EU Data Residency** (GCP europe-west4, Holanda), ativo pós-Res. 32, dispensa SCC. US ainda usa DPF |
| **Mitigações** | Ativar **EU residency** no signup (não dá pra migrar depois); `opt_out_tracking_by_default: true`; APIs `/delete` e `/engage` prontas pra direitos do titular |

### 1.5 Amplitude
Perfil idêntico ao Mixpanel. **EU Data Center** (Frankfurt). APIs `/userdelete` e `/userexport`.

### 1.6 Hotjar / Microsoft Clarity ⚠️

| | |
|---|---|
| **Coleta** | **Session recording** (mouse, scroll, clicks, inputs), heatmaps, funnels, surveys. Captura DOM completo, pode pegar PII trivialmente |
| **Sensibilidade** | **CRÍTICA.** Tratar como categoria especial |
| **Base legal** | **Consentimento explícito** sem exceção. Banner com toggle dedicado "gravação de sessão" |
| **DPA + SCC** | Hotjar (Contentsquare, francesa): DPA com SCC-EU. **Bom pós-Res. 32**. Clarity (Microsoft): DPA Microsoft Online Services |
| **Alternativa privacy-first** | OpenReplay (self-host). PostHog session replay com masking estrito |
| **Mitigações** | Clarity: modo `strict` masking; Hotjar: `data-hj-suppress` em PII; **bloquear gravação em telas autenticadas** com dados sensíveis (financeiro, saúde) |

---

## 2. Error tracking

### 2.1 Sentry ⭐ default recomendado

| | |
|---|---|
| **Coleta** | Stack trace, exception, breadcrumbs (requests, console, navigation), contexto (user, tags, extras), source maps. **PII vaza fácil**: Authorization headers, body de POST, query strings com email/CPF |
| **Sensibilidade** | Alta se não saneado. Baixa-média com scrubbing |
| **Base legal** | **Legítimo interesse** (art. 7º IX), segurança e correção. Não exige consentimento se PII for ativamente removida. Documentar em ROPA |
| **DPA + SCC** | DPA público. **EU region (Frankfurt)** em planos pagos, ativar pra projetos BR |
| **Alternativa privacy-first** | GlitchTip (fork open-source, self-host), Sentry self-hosted |
| **Mitigações** | `sendDefaultPii: false`; `beforeSend(event)` removendo email/cpf/token/password/body; `denyUrls`, `ignoreErrors`; Server-side Relay; Advanced Data Scrubbing com regex pra CPF/CNPJ/cartão; retenção mínima (30-90d) |

### 2.2 Bugsnag / Rollbar / Honeybadger
Bugsnag (SmartBear, US): EU region. Rollbar, `transform` hook ≈ `beforeSend`. Honeybadger: US-only, desvantagem hoje.

---

## 3. Logs e observabilidade

| Ferramenta | EU region | Notas |
|---|---|---|
| Datadog | `datadoghq.eu` (Frankfurt) | Maduro, caro |
| New Relic | EU region | Bom APM |
| Grafana Cloud | EU instance (Frankfurt/Dublin) | ⭐ default recomendado (open-source friendly) |
| BetterStack | UE-only | Bom UX, mais barato |
| Logflare | US (Cloudflare) | Desvantagem hoje |

**Regra geral:** logger com redactor de PII (Pino `redact`, Winston format); nunca logar request body autenticado; hashear ID em log; retenção curta (30d hot, arquivo morto sem PII); RBAC restrito na UI.

---

## 4. Marketing / CRM / E-mail

### 4.1 E-mail transacional

| Ferramenta | EU region | Notas |
|---|---|---|
| **Postmark** | DPA com SCCs-EU | ⭐ default recomendado (transacional limpo) |
| SendGrid (Twilio) | DPA + SCCs + DPF; EU opção | Mais comum, ok |
| Mailgun | EU (Frankfurt) | OK |
| **Resend** | DPA disponível; UE region (Dublin) | ⭐ default recomendado (DX excelente; novo, ler DPA com lupa) |

**Mitigações:** desligar open/click tracking em transacional autenticado (token de reset não precisa rastrear); suprimir lista de bounce; DPA antes do go-live; BIMI/DMARC pra reduzir spoofing.

### 4.2 CRM/Marketing

| Ferramenta | Notas |
|---|---|
| HubSpot | DPA com SCCs-EU + DPF; UE region disponível |
| **RD Station (TOTVS)** ⭐ | **Brasileira**: DPA já incorpora cláusulas-padrão **ANPD Res. 19/2024**, vantagem regulatória clara |
| ActiveCampaign | US + EU region |

**Mitigações:** formulários com checkbox de consentimento granular (newsletter vs contato); double opt-in; integração com CMP pra desligar tracking script pré-consentimento.

### 4.3 Pixel de publicidade ⚠️

Meta Pixel, Google Ads Tag, TikTok Pixel, LinkedIn Insight Tag.

- **Coleta:** eventos de conversão, page view, custom audiences, retargeting. Cookies 3rd party agressivos. Email/phone hash via Advanced Matching/CAPI
- **Sensibilidade:** **CRÍTICA**
- **Base legal:** **consentimento explícito e granular** sem exceção
- **Server-side variants:** Meta Conversions API (CAPI), Google Enhanced Conversions, TikTok Events API, LinkedIn Conversions API. **Server-side não dispensa consentimento**, só controla entrega
- **Mitigações:** bloquear até consentimento via **Consent Mode v2** (Google) / Meta Consent Mode; hash SHA-256 obrigatório em email/phone antes do CAPI; excluir páginas sensíveis (saúde, financeiro); revisar audiences custom semestralmente

---

## 5. Push e in-app messaging

### 5.1 OneSignal / FCM / APNs

| | |
|---|---|
| **Coleta** | Token de dispositivo (PII per ANPD), opt-in status, segmentos, conteúdo, métrica de abertura |
| **Base legal** | Consentimento (permissão SO = ato consentimento; vínculo user_id no backend = consentimento adicional pra perfilamento) |
| **DPA** | OneSignal: DPA + SCCs + DPF (US). FCM (Google): DPA Google Cloud, EU regions disponíveis. APNs: contrato Apple Developer |
| **Mitigações** | `setConsentRequired(true)` no SDK até aceitar; **nunca** mandar PII no payload (push é cacheado em intermediários); endpoint de revogação de token; FCM data-only pra controle |

### 5.2 Chat ao vivo

| Ferramenta | Notas |
|---|---|
| **Crisp** ⭐ | Francesa, hospedagem exclusiva Amsterdam → ouro pós-Res. 32 |
| Intercom | DPA com SCCs novos, EU region disponível |
| Zendesk | DPA, EU data residency adicional |
| **Chatwoot** | Open-source, self-host pra controle total |

**Mitigações:** retenção curta (90-180d); treinar atendentes a **não** registrar CPF/cartão; deleção em massa por usuário; desativar tracking de página fora de URLs de suporte.

---

## 6. Integração com banner de cookies

**Princípios do Guia ANPD jan/2025:**

1. **Granularidade obrigatória.** "Aceitar todos" sem equivalente "Rejeitar todos" no mesmo nível = dark pattern, sancionável
2. **Categorias mínimas:** Necessários (always-on), Funcionais, Analytics, Marketing, cada categoria opt-out independente
3. **Pré-marcação proibida** em não-essenciais
4. **Revogação tão fácil quanto consentir**, botão persistente no rodapé
5. **Log de consentimento auditável**, timestamp, versão do banner, categorias aceitas, hash de IP, UA

**Padrão SSR-friendly:**

```
1. SSR/edge renderiza HTML "frio" sem script de tracking
2. CMP injeta banner inline
3. CMP emite evento (`CustomEvent('consent-update', {...})`)
4. Script loader (próprio ou GTM) escuta e injeta tags condicionalmente
5. Google Consent Mode v2: `gtag('consent', 'default', {...denied})` antes; `gtag('consent', 'update', {...})` após escolha
6. Persistir consent_log no backend com correlation id
```

**CMPs com presença BR:** GoAdopt (nacional, Consent Mode v2 + cláusulas ANPD no log), Cookiebot (Cybot/Usercentrics, EU), OneTrust (US, enterprise), Iubenda (italiana). Open-source: `klaro!`, `cookieconsent` (Orest Bida).

O banner em `templates/banner-cookies.tsx` da Fase A já implementa o padrão.

---

## 7. Lista pública de processadores: template

Publicar em `/transparencia/terceiros`. Coluna obrigatória (art. 9º LGPD + art. 37):

| Processador | Finalidade | Dados | Hospedagem | Transferência | Base legal | DPA |
|---|---|---|---|---|---|---|
| Plausible Analytics OÜ | Métricas anônimas | URL, referrer, país | UE (Hetzner DE) | UE, adequação ANPD Res. 32/2026 | Legítimo interesse | [Link DPA] |
| Sentry (Functional Software) | Monitoramento de erros | Stack trace, contexto sem PII | UE (Frankfurt) | UE, adequação ANPD Res. 32/2026 | Legítimo interesse | [Link DPA] |
| Resend | E-mail transacional | E-mail destinatário, conteúdo | UE (Dublin) | UE, adequação ANPD Res. 32/2026 | Execução de contrato | [Link DPA] |
| Vercel Inc. | Hospedagem | Logs HTTP, IP | Global (FRA recomendado) | EUA: DPF + SCC | Execução de contrato | [Link DPA] |
| Supabase | Banco de dados | Conteúdo da aplicação | Configurável (UE recomendado) | varia | Execução de contrato | [Link DPA] |

Versionar com data de atualização. Revisar trimestralmente. Template completo em `templates/transparencia/terceiros.yaml`.

---

## 8. Auditoria periódica de tracking

**Trimestral, no mínimo:**

1. **DevTools auditoria manual:** Network em aba anônima, navegar 5 fluxos críticos (home, signup, checkout, área logada, contato), exportar HAR, identificar hosts third-party
2. **Scanners automatizados:**
   - **Cookiebot scanner** (free tier mensal), varre, classifica, gera relatório
   - **OneTrust Cookie Compliance** (pago, profundo)
   - **Blacklight da The Markup** (free, ótimo pra screenshot pro DPO)
   - **PrivacyScore** (open-source)
   - **`webbkoll.dataskydd.net`** (sueco, free)
3. **CSP report-only** com `report-to` pra endpoint próprio detecta scripts novos
4. **CI check:** lint de `package.json` contra lista negra de SDKs de tracking não-aprovados
5. **Diff trimestral** da lista de processadores vs scan, qualquer host novo precisa DPA antes de prod
6. **Revisar `beforeSend` / `sanitize`** a cada release que adicione campo novo no DOM
7. **Testar fluxo "rejeitar todos"**, nenhum script third-party pode disparar. Idem "revogar consentimento"

---

## 9. Stack default recomendado (resumo executivo)

Pra projeto novo, default privacy-first:

| Categoria | Escolha default | Por quê |
|---|---|---|
| Analytics web | **Plausible** | Sem cookie, sem consentimento de cookie, hospedagem UE, legítimo interesse defensável |
| Product analytics | **PostHog EU** sem replay (default) | Self-host opcional, masking forte, residência UE |
| Error tracking | **Sentry EU** com `beforeSend` agressivo | EU region + DPF, scrubbing maduro |
| Logs/APM | **Grafana Cloud EU** ou **BetterStack** | UE-first, retenção configurável |
| E-mail transacional | **Postmark** ou **Resend EU** | DPA limpos, UE region |
| CRM/marketing | **RD Station** | Brasileira, cláusulas ANPD nativas |
| Push | **OneSignal** com `requireConsent` | DPA + opt-in gateado |
| Chat | **Crisp** | França + hospedagem exclusiva Amsterdam |
| CMP | **GoAdopt** (BR) ou **klaro** (open-source) | Consent Mode v2 + log auditável |

**Se já está rodando GA4 + Hotjar + Intercom-US:** caminho de menor risco:
1. Ativar **EU regions** onde existirem
2. Implementar Consent Mode v2 estrito
3. Substituir Hotjar por Clarity em `strict` ou PostHog Replay com masking
4. Renegociar DPAs em ciclo até 2026Q3 com cláusulas-ANPD

## Referências externas

- [Resolução CD/ANPD nº 19/2024 (Transferência Internacional)](https://www.gov.br/anpd/pt-br/assuntos/noticias/resolucao-normatiza-transferencia-internacional-de-dados)
- [Guia Orientativo Cookies (rev. jan/2025) (PDF ANPD)](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf)
- [CNIL Decision on Google Analytics (Trilateral Research)](https://trilateralresearch.com/data-governance/cnil-decision-on-the-use-of-google-analytics-and-recommended-alternatives)
- [Plausible Data Policy](https://plausible.io/data-policy)
- [PostHog Privacy Controls](https://posthog.com/docs/privacy/data-collection)
- [Mixpanel EU Data Residency](https://mixpanel.com/legal/eu-data-residency/)
- [Sentry GDPR Best Practices](https://sentry.io/trust/privacy/gdpr-best-practices/)
- [Postmark DPA](https://postmarkapp.com/dpa)
- [RD Station DPA (cita ANPD Res. 19/2024)](https://www.rdstation.com/legal-e-privacidade/dpa/)
- [Google Consent Mode v2](https://developers.google.com/tag-platform/security/guides/consent)
