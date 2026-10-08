---
name: lgpd-compliance-alexandre-henrique-rp
title: LGPD Compliance — Engineering Playbook (v6.6.0)
description: LGPD compliance for engineering teams — SDLC, anonymization, consent, soft/hard delete, audit log, shadow AI. Mandatory when feature touches Brazilian PII.
author: alexandre-henrique-rp
author_url: https://github.com/alexandre-henrique-rp/harnes-opencode/tree/main/skills/lgpd-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# LGPD Compliance — Engineering Playbook (v6.6.0)

> Baseado no **Guia Avançado de LGPD para Engenharia de Software** (ANPD/Lei 13.709/2018)
> e nas Recomendações de Cookies e Ferramentas de Rastreamento da ANPD.
>
> Esta skill é **obrigatória** no harness para qualquer feature que
> processa dados pessoais de cidadãos brasileiros. Aplicada por:
> `backend` agent (ao implementar endpoint com PII), `lgpd-officer`
> (auditoria fim de sprint), `security` (revisão profunda).

---

## 1. Privacidade como Requisito de Engenharia (não conformidade tardia)

LGPD não é checklist ao fim do projeto. É **requisito não funcional**
desde o desenho. Art. 46: medidas técnicas + administrativas + de
segurança contra acessos não autorizados, destruição, perda, alteração,
comunicação ou tratamento inadequado.

**Implicação prática:**

- Modelagem de dados começa com **minimização** (não coleta "caso precise")
- Arquitetura é desenhada com **superfície de ataque mínima**
- Decisões de stack consideram **residência de dados** (LGPD art. 33)
- Toda feature com PII passa por **DPIA** (Relatório de Impacto à Proteção de Dados Pessoais) antes de ir pra produção

**Checklist do engenheiro antes de começar:**

- [ ] Qual a base legal dessa coleta? (consentimento, execução de contrato, legítimo interesse, etc — art. 7º)
- [ ] Os dados são estritamente necessários para a finalidade declarada?
- [ ] Por quanto tempo esses dados serão retidos? (e há alerta de inatividade?)
- [ ] Quem tem acesso (privilégio mínimo)?
- [ ] Como o titular exerce os direitos do art. 18?
- [ ] Onde os dados moram? Servidor no Brasil? Subprocessador no exterior?

---

## 2. SDLC (Secure Software Development Life Cycle) e Open Source

LGPD permeia todas as fases do SDLC. Não dá pra "adicionar segurança"
no fim.

### Integração no pipeline

```
[Desenho]  →  [Codificação]  →  [Build]  →  [Test]  →  [Deploy]  →  [Produção]
     ↓              ↓                ↓            ↓            ↓
   DPIA          SAST          SCA scan       DAST      Validação    Monitoramento
   minimização   linter        licencias     pen-test   contratos    SIEM
   base legal    secrets       vulns         OWASP      subprocess.  alertas
```

### Análise de Composição de Software (SCA)

Open source acelera entrega mas introduz riscos. **Toda dependência nova
precisa passar por SCA antes de ir pra `package.json`**.

Ferramentas recomendadas:

| Ferramenta | Tipo | O que detecta |
|---|---|---|
| **Snyk** | SaaS/self-host | CVEs em deps + license conflicts |
| **OWASP Dependency-Check** | Open source | CVEs via NVD database |
| **Trivy** | Open source | Multi-layer (deps, IaC, container) |
| **npm audit** | Built-in | CVEs em deps npm |
| **pip-audit** | Built-in Python | CVEs em deps PyPI |
| **license-checker** (npm) | Open source | Incompatibilidades de licença |

**Política de equipe:**

```bash
# Rodar em CI em todo PR
npm audit --audit-level=high
pip-audit --strict
snyk test --severity-threshold=high
npx license-checker --failOn 'GPL;AGPL;SSPL'
```

**Falha em qualquer um = PR bloqueado.** Não merge com `// @ts-ignore`
também.

### Segurança White Box

White box (ou "chapéu branco") = profissionais com acesso ao código-fonte
fazendo auditoria. Presença **obrigatória** no time se a aplicação
trata dados sensíveis (saúde, financeiro, crianças).

White box faz:

- Revisão de código focada em fluxo de dados sensíveis
- Identificação de falhas de lógica (ex: bypass de autorização)
- Modelagem de ameaças contínua (STRIDE, PASTA)
- Capacitação dos devs sobre vulnerabilidades recentes

---

## 3. Autenticação, Controle de Acesso e Sessão

Primeira linha de defesa. Parâmetros inegociáveis:

### Política de senhas (mínimo absoluto)

```yaml
senha:
  tamanho_minimo: 12 caracteres        # NIST 800-63B recomenda 8+, mas pra PII vai além
  complexidade:
    - maiusculas: 1+
    - minusculas: 1+
    - numeros: 1+
    - simbolos: 1+
  blacklist:
    - "12345678", "password", "qwerty"  # top 100 senhas vazadas
    - variações do nome do usuário
    - variações do email
  expiracao: 90 dias                   # apps normais; menos para apps críticos
  historico: nao repetir ultimas 5 senhas
  lockout: 5 tentativas em 15 min      # rate limit
  hash_algoritmo: argon2id            # NUNCA md5, sha1, bcrypt (depreciado)
  hash_params:
    memory: 64MB                       # ajuste conforme hardware
    iterations: 3
    parallelism: 4
```

### Migração de senhas em sistemas legados

❌ **Errado** (comum): "a gente importou as senhas antigas e todo mundo
terá que redefinir no primeiro login".

✅ **Certo:**

1. Senha temporária aleatória (16+ chars) gerada server-side
2. Enviada por **canal seguro** (e-mail com link de ativação, MFA, ou
   SMS confirmado)
3. Hash novo (argon2id) no momento do primeiro login — **NUNCA
   preservar hash antigo se for fraco**
4. Flags `must_change_password: true` + `password_set_at: <agora>`
5. Bloqueia features sensíveis até a troca

### Cookies e sessão

| Atributo | Valor obrigatório | Razão |
|---|---|---|
| `Secure` | `true` (sempre) | Só transmite sob HTTPS |
| `HttpOnly` | `true` (sempre) | Bloqueia acesso via JS (mitiga XSS) |
| `SameSite` | `Strict` (default) ou `Lax` | Mitiga CSRF |
| `Domain` | escopo mínimo (sem `.example.com` global) | Evita vazamento entre subdomínios |
| `Path` | escopo mínimo (ex: `/api`, não `/`) | Idem |
| `Max-Age` | <= 7 dias (e-commerce), <= 24h (crítico) | Limita janela de exposição |
| Session token | random 128+ bits (crypto.randomBytes) | Não UUID v1 (previsível) |

**Logout destrói sessão no servidor, não só no cliente.** Session store
precisa de método `revoke(sessionId)`.

### Tabela técnica completa (do guia)

| Requisito | Especificação | Impacto LGPD |
|---|---|---|
| Criptografia em trânsito | TLS 1.2+ (ideal 1.3), HSTS habilitado | Impede man-in-the-middle |
| Cookies | Secure + HttpOnly + SameSite | Mitiga XSS + CSRF |
| Escopo de cookie | Domain + Path mínimos | Evita exposição a subdomínios |
| Origin check | Aceita só origens validadas no servidor | Reduz CSRF/CORS bypass |
| Expiração | <= 7 dias (comum), <= 24h (crítico) | Limita janela de sessão orfã |
| Logout explícito | Destrói sessão no servidor + cliente | Limita rastreamento pós-uso |

---

## 4. Banners de Consentimento (Front-End)

A ANPD publicou diretrizes específicas. Resumo técnico:

### Estrutura de 2 níveis (obrigatória)

**Banner de 1º nível** (primeira visita):

```
┌─────────────────────────────────────────────────────────┐
│ Este site usa cookies                                    │
│                                                          │
│ Usamos cookies para segurança, analytics e personalização.│
│ Você pode aceitar todos, rejeitar ou gerenciar.          │
│                                                          │
│ [Aceitar Todos]  [Rejeitar Todos]  [Gerenciar Opções]   │
│                                                          │
│ Política de Cookies →                                    │
└─────────────────────────────────────────────────────────┘
```

Requisitos:

- Os 3 botões com **idêntico destaque visual** (sem hierarquia tendenciosa)
- "Rejeitar Todos" deve ser **tão fácil quanto "Aceitar Todos"** (mesmo nº de cliques)
- Link direto pra Política de Cookies
- Idioma do usuário (não só em inglês)

**Banner de 2º nível** (após clicar em "Gerenciar Opções"):

```
┌─────────────────────────────────────────────────────────┐
│ Preferências de Cookies                                  │
│                                                          │
│ ☑ Essenciais        (sempre ativos, segurança)           │
│ ☐ Analíticos        (Google Analytics, Hotjar)            │
│ ☐ Funcionais        (preferências de UI)                  │
│ ☐ Publicidade       (ads comportamentais)                 │
│                                                          │
│ [Salvar Preferências]  [Aceitar Todos]  [Rejeitar Todos]│
└─────────────────────────────────────────────────────────┘
```

Requisitos:

- **Essenciais** vêm marcados e bloqueados (não dá pra desmarcar)
- **Todos os outros** vêm **desmarcados** por padrão (privacy by default)
- Mudança requer ação afirmativa do usuário

### Dark patterns PROIBIDOS (ANPD)

❌ Cor chamativa só no botão "Aceitar"
❌ Esconder/disfarçar o botão "Rejeitar"
❌ Cookie wall (bloqueia conteúdo se rejeitar)
❌ Política em idioma estrangeiro
❌ Slider pré-posicionado em "aceitar tudo"
❌ Pré-checked boxes em analytics
❌ "Ao continuar navegando você aceita" (consentimento não é implícito)

### CMPs (Consent Management Platforms)

Recomendado usar uma CMP certificada. Líderes de mercado:

- **OneTrust** — enterprise, multi-jurisdicional
- **Cookiebot** — SaaS, bom custo-benefício
- **Osano** — open-core, foco em GDPR/LGPD
- **Iubenda** — popular em PMEs italianas/brasileiras
- **Termly** — bom para sites simples

A CMP:

- Detecta e classifica cookies automaticamente (scan periódico)
- Bloqueia tags de analytics/marketing **antes** do consentimento
- Gera log auditável de consentimento (registro legal pra ANPD)
- Suporta API padrão (IAB TCF v2.2) pra integração com adtech

**Implementação:**

```typescript
// Integração típica com CMP
import { onConsentChange } from "@cmp/sdk";

onConsentChange((consent) => {
  if (consent.analytics) enableAnalytics();
  if (consent.marketing) enableMarketingTags();
  // log auditável
  auditLogger.log({
    type: "consent.change",
    userId: hashUserId(currentUser.id),
    choices: consent,
    timestamp: new Date().toISOString(),
    ip: hashIp(req.ip),
  });
});
```

---

## 5. Anonimização vs Pseudonimização (Distinção Crítica)

**Não confunda.** ANPD é explícita: as duas têm consequências jurídicas
totalmente diferentes.

| | Anonimização | Pseudonimização |
|---|---|---|
| **Definição** | Remove **permanentemente** possibilidade de reidentificação | Substitui identificador direto por pseudônimo |
| **Dado pessoal?** | **NÃO** — sai do escopo da LGPD | **SIM** — continua sob LGPD |
| **Reversível?** | NÃO (irreversível) | SIM (com chave/tabela de mapeamento) |
| **Requisito de base legal?** | NÃO precisa de base legal (não é dado pessoal) | SIM, precisa de base legal |
| **Uso típico** | Analytics agregados, dataset de pesquisa | Logs internos, ambientes de dev/test |

### Tabela técnica completa (ANPD)

| Técnica | Tipo | Reversibilidade | Implementação |
|---|---|---|---|
| **Criptografia forte** | Pseudonimização | Reversível (com chave) | AES-256 (simétrico) ou RSA (assimétrico) |
| **Substituição de diretório** | Pseudonimização | Reversível (tabela isolada) | Substitui identificador por valor de diretório fictício, preserva estatísticas |
| **Função hash** | Pseudonimização | **Irreversível** (mas vulnerável a rainbow tables) | SHA-256 com **salt** aleatório único por usuário |
| **Mascaramento dinâmico** | Ofuscação | Reversível (runtime) | Substitui dígitos intermediários: `123.***.***-00` |
| **Generalização** | Anonimização | Irreversível | Faixas etárias (30-40), bairros → regiões |
| **Perturbação de ruído** | Anonimização | Irreversível | Adiciona variação aleatória (preserva média) |
| **Supressão** | Anonimização | Irreversível | Remove coluna inteira |
| **Pixelização** | Anonimização | Irreversível | Blur em imagem (OCR-resistant) |

### ⚠️ Hash NÃO é sinonimo de anonimização

SHA-256 sem salt é **vulnerável a ataque de dicionário** (rainbow tables
públicas cobrem bilhões de CPFs e emails). Para ser seguro:

```typescript
import { randomBytes, createHash } from "node:crypto";

// ❌ ERRADO: hash sem salt
const hash = createHash("sha256").update(cpf).digest("hex");

// ✅ CERTO: hash com salt único persistido
const salt = randomBytes(16).toString("hex");
const hash = createHash("sha256").update(salt + cpf).digest("hex");
// Armazena { salt, hash } — sem o salt, reidentificar é inviável
```

**Argumento ainda mais forte:** prefira **HMAC** com segredo do servidor
(rotacionado periodicamente), que invalida hashes antigos quando o
segredo muda.

### ⚠️ Anonimização NÃO deve ser 100% automatizada

A ANPD recomenda: **especialista humano** revisa o output do algoritmo.
Por quê? Ataques de reidentificação evoluem. Um dataset "anonimizado"
hoje pode ser reidentificável amanhã via join com data leaked em outro
vazamento.

**Protocolo:**

1. Rodar técnica automatizada (k-anonimity, l-diversity, t-closeness)
2. Especialista avalia risco residual
3. Se aceitável, certifica e versiona o dataset
4. Reavalia periodicamente (a cada 6-12 meses)

---

## 6. Ciclo de Vida dos Dados: Soft Delete, Hard Delete e Descarte

Padrão comum de **soft delete** (marcar `is_deleted=true`) **NÃO atende
LGPD art. 18, VI** (eliminação dos dados). Titular tem direito à remoção
**permanente**.

### Protocolo de 3 fases

**Fase 1 — Janela de carência (30 dias típicos)**

```sql
-- Dia 0: usuário pede exclusão
UPDATE users SET
  is_deleted = true,
  deleted_at = NOW(),
  scheduled_hard_delete_at = NOW() + INTERVAL '30 days',
  account_state = 'pending_deletion'
WHERE id = $1;
```

- Conta fica desativada, sem acesso, sem marketing
- Permite reverter em caso de arrependimento
- Email automático: "Sua conta será excluída em X dias. Cancele aqui: [link]"

**Fase 2 — Ciclo de dormência (recomendado ANPD-like)**

```
Login válido nos últimos 23 meses?  ──sim──→  OK (não toca)
                       │
                       não
                       │
                       ▼
        Enviar email de alerta de inatividade
        (link pra reativar em 30 dias)
                       │
        30 dias depois, sem reativação?
                       │
                       ▼
        Soft delete + iniciar carência de 30 dias
                       │
        30 dias de carência sem reverter?
                       │
                       ▼
        Hard delete (Fase 3)
```

**Fase 3 — Expurgo definitivo (hard delete)**

```sql
-- Após 30 dias de carência
DELETE FROM users WHERE id = $1;
DELETE FROM user_sessions WHERE user_id = $1;
DELETE FROM user_pii WHERE user_id = $1;
-- ... demais tabelas
```

**Rodar em cron job diário**, não on-demand (consistência).

### Anonimização na exclusão (preserva integridade referencial)

❌ DELETE em cascata quebra FK de tabelas analíticas/faturamento.

✅ UPDATE que substitui por valores genéricos:

```sql
-- Em vez de DELETE FROM users
UPDATE users SET
  name = 'Usuário Removido',
  email = CONCAT('removed_', id, '@deleted.local'),
  cpf = NULL,
  phone = NULL,
  -- mantém id (FK) e created_at (auditoria)
  anonymized_at = NOW()
WHERE id = $1;
```

Mantém integridade do banco + remove PII.

### Expurgo em subprocessadores e IA

**Subprocessadores** (analytics, email marketing, CRM):

```typescript
// Webhook ao subprocessador
await fetch("https://api.subprocessador.com/v1/users/delete", {
  method: "POST",
  body: JSON.stringify({ userId: hashUserId(userId) }),
  headers: { Authorization: `Bearer ${process.env.SUB_TOKEN}` },
});
```

**Modelos de ML** treinados com dados do titular:

- Botão/API de **"untrain expression"** (desfaz associação nos embeddings)
- Rerun de feature extraction excluindo o titular
- Re-treino do modelo (se a associação era crítica) — caro mas correto
- Documentar no `model-card.md` quais titulares foram excluídos

---

## 7. Logs de Auditoria — Imutabilidade e Cadeia Criptográfica

Logs em arquivo de texto mutável **não servem** como prova. Atacante
com acesso admin pode editar, deletar, alterar timestamps.

### Requisitos de infraestrutura

**Sincronismo de tempo (NTP):**

- Todos servidores sincronizam com **≥ 2 fontes NTP estáveis**
- Timestamps **sempre em UTC** (independente do fuso local)
- Drift máximo aceitável: 50ms

**Cadeia de hashes (hash chain):**

```
H_i = SHA-256(Log_i || H_{i-1})
```

Cada log inclui o hash do anterior. Qualquer adulteração **invalida a
cadeia** a partir do ponto modificado. Implementação no harness já
existe em `plugins/audit-logger.ts` (campo `prevHash`).

**Eventos críticos obrigatórios (tabela ANPD-like):**

| Evento | Detalhes registrados | Guarda |
|---|---|---|
| **Controle de acesso** | Login sucesso/falha, lockouts, troca de senha | Storage remoto (não-local), append-only |
| **Gestão de contas** | Criação, modificação, suspensão, alteração de privilégios | Envio criptografado imediato pra SIEM |
| **Acesso a PII** | Qual usuário, qual titular, data/hora exatas | Retenção ≥ 6 meses |
| **Modificação de dados** | Valores antes/depois, autor, timestamp | WORM (Write Once Read Many) |
| **Tentativa de adulterar log** | Quem tentou, quando, o o que | Alerta imediato ao SOC |

**Storage WORM** (Write Once Read Many):

- AWS S3 Object Lock (Compliance mode)
- Azure Blob Immutable Storage
- Google Cloud Storage Bucket Lock
- On-prem: NetApp SnapLock, Veeam, etc

Logs antigos com PII devem ser **eliminados** após período de retenção
(LGPD art. 16 — eliminação segura).

---

## 8. Shadow AI — O Risco Mais Novo

Engenheiros integrando LLMs (OpenAI, Anthropic, Gemini) sem aprovação
do DPO. O harness **USA LLM extensivamente**, então este risco é
**diretamente aplicável a nós**.

### 4 riscos fundamentais (do guia)

**Risco 1: Transferência internacional indevida (art. 33)**

Prompt com CPF/nome vai pra servidor nos EUA → viola LGPD mesmo se
"estamos em cloud brasileira" (telemetria global).

**Risco 2: Perda de finalidade + falta de transparência**

Provedor pode usar prompts pra retreinar modelos. Quebra a finalidade
informada ao titular.

**Risco 3: Shadow AI (sem inventário)**

Dev integra secretamente uma LLM não homologada. Multa de até **2% do
faturamento bruto anual por infração**.

**Risco 4: Explicabilidade (art. 20)**

LLM tomou decisão automatizada (negou crédito, barrou usuário) → LGPD
exige revisão clara dos critérios. Natureza probabilística complica.

### Estratégias de mitigação (do guia)

**Estratégia 1: Modelos soberanos / VPC nacional**

```yaml
infra:
  vpc: privada, em região BR
  modelo: self-hosted (Llama, Mistral) OU provider BR homologado
  telemetria: desabilitada
  logs: armazenados em storage nacional
  retention: automatizada por política
```

**Estratégia 2: Pipeline de sanitização de prompts**

Microsserviço que intercepta prompt **antes** de enviar pro LLM:

1. Detecta PII (regex + NLP local)
2. Substitui por placeholder ou hash
3. LLM processa prompt sanitizado
4. Resposta volta com placeholders
5. Reversão: substitui placeholders pelos valores reais

**Implementação de referência:** `tools/lgpd-sanitizer.ts` (neste pacote).

---

## 9. DevSecOps — Integração Contínua de Segurança

### Pipeline mínimo

```yaml
# .github/workflows/security.yml
name: Security
on: [pull_request]

jobs:
  sast:
    steps:
      - uses: github/codeql-action/analyze
      - uses: semgrep/semgrep-action

  secrets:
    steps:
      - uses: gitleaks/gitleaks-action

  deps:
    steps:
      - run: npm audit --audit-level=high
      - run: pip-audit --strict
      - uses: snyk/actions/test

  sca:
    steps:
      - run: npx license-checker --failOn 'GPL;AGPL'

  dast:
    # Roda contra staging
    - uses: zaproxy/action-baseline
```

### Ferramentas por categoria

| Categoria | Ferramenta | Quando rodar |
|---|---|---|
| SAST | CodeQL, Semgrep, SonarQube | Cada PR |
| DAST | OWASP ZAP, Burp | Antes de release |
| SCA | Snyk, OWASP DC, Trivy | Cada PR |
| Secrets | Gitleaks, TruffleHog | Cada commit |
| Container | Trivy, Clair | Build de imagem |
| IaC | tfsec, Checkov | Cada PR |
| License | license-checker, FOSSA | Cada PR |

---

## 10. Higiene Operacional do Engenheiro

Você (humano) é também vetor de ataque. LGPD considera isso.

### Política mínima (do guia)

- ❌ **Nunca** compartilhar login/senha de staging ou prod
- ❌ **Nunca** post-it com credencial na mesa
- ❌ **Nunca** deixar workstation desbloqueada (mesmo "rapidinho")
- ✅ Lock screen automático em 5 min de inatividade
- ✅ Senha única por ambiente (dev ≠ staging ≠ prod)
- ✅ MFA obrigatório em tudo que toca produção
- ✅ Phishing: reportar emails suspeitos via canal oficial
- ✅ Documentos físicos com PII: trancar em armário ou triturar

### Capacitação contínua

- OWASP Top 10 atualizado anualmente
- Treinamento de phishing simulado (trimestral)
- Revisão de incidentes recentes (post-mortem compartilhado)
- LGPD updates da ANPD (newsletter, RSS)

### Canal de relato de incidentes

Estabelecer fluxo **sem punição** pra reportar:

- Bug encontrado em código
- Suspeita de vazamento
- Comportamento anômalo observado
- Dependência vulnerável esquecida

LGPD art. 48: notificação à ANPD em **2 dias úteis** ao tomar ciência
do incidente. Quanto antes souber, antes comunica.

---

## 11. Checklist de Auto-Auditoria (rodar antes de merge)

```markdown
## LGPD Self-Audit (pre-merge)

### Privacidade desde o design
- [ ] Base legal identificada pra cada coleta (consentimento, contrato, etc)
- [ ] Dados coletados são estritamente necessários (minimização)
- [ ] DPIA atualizado (se aplicável)
- [ ] Política de privacidade reflete a feature

### Autenticação e acesso
- [ ] Senhas com política robusta (argon2id, 12+ chars, blacklist)
- [ ] Cookies Secure + HttpOnly + SameSite
- [ ] Sessão com expiração adequada
- [ ] Logout destrói sessão no servidor
- [ ] MFA habilitado pra funções sensíveis

### PII em código e logs
- [ ] Nenhum PII em log (mask aplicado)
- [ ] Nenhum secret em código (.env, package.json)
- [ ] Anonimização em ambiente de dev/test
- [ ] Criptografia em repouso pra colunas sensíveis

### Soft/hard delete
- [ ] Soft delete + carência de 30 dias
- [ ] Hard delete via cron job
- [ ] Webhook pra subprocessadores
- [ ] Untrain expression se envolve ML

### Auditoria
- [ ] Eventos críticos logados (acesso, modificação, exclusão)
- [ ] Hash chain configurado
- [ ] Storage remoto (não-local) com WORM
- [ ] Retenção definida e automatizada

### Shadow AI
- [ ] Nenhum LLM third-party sem aprovação do DPO
- [ ] Pipeline de sanitização de prompts (se LLM em uso)
- [ ] Modelo soberano OU provider BR homologado
- [ ] Telemetria de LLM desabilitada

### UI de consentimento
- [ ] Banner 1º nível: 3 botões equivalentes (aceitar/rejeitar/gerenciar)
- [ ] Banner 2º nível: preferências granulares desmarcadas por default
- [ ] Zero dark patterns (botão rejeitar visível, sem cookie wall)
- [ ] CMP integrada e funcionando
```

---

## 12. Resumo das Referências Legais e Técnicas

| Documento | Aplicação |
|---|---|
| **LGPD Lei 13.709/2018** | Lei principal |
| **Art. 7º** | Bases legais de tratamento |
| **Art. 11** | Tratamento de dados sensíveis |
| **Art. 16** | Eliminação de dados |
| **Art. 18** | Direitos do titular (acesso, correção, exclusão, portabilidade) |
| **Art. 20** | Decisões automatizadas e explicabilidade |
| **Art. 33** | Transferência internacional |
| **Art. 41** | Encarregado de dados (DPO) |
| **Art. 46** | Medidas de segurança |
| **Art. 48** | Notificação de incidentes (2 dias úteis) |
| **ANPD — Cookies e Rastreamento** | Banners e CMPs |
| **ANPD — Anonimização vs Pseudonimização** | Técnicas de tratamento |
| **OWASP Top 10** | Vulnerabilidades web |
| **NIST 800-63B** | Política de senhas e autenticação |
| **PCI DSS** | Se houver dados financeiros |
| **CLOUD Act (EUA)** | Risco de jurisdição |

---

## 13. Ferramentas Fornecidas pelo Harness

| Arquivo | Função |
|---|---|
| `tools/lgpd-sanitizer.ts` | Pipeline de sanitização de prompts (regex + NLP leve) |
| `plugins/audit-logger.ts` | Hash chain automático (imutabilidade) |
| `agents/lgpd-officer.md` | Auditor de fim de sprint |
| `agents/security.md` | Revisão profunda de segurança |
| `skills/security-audit/SKILL.md` | Checklist técnico complementar |
| `training/lgpd-engineering-advanced.md` | Onboarding pra engenheiros novos |

---

## 14. Anti-patterns (revisão rápida)

- ❌ Coletar "caso precise" (viola minimização)
- ❌ Soft delete sem hard delete posterior
- ❌ Cookie wall
- ❌ Botão "rejeitar" escondido
- ❌ Hash sem salt
- ❌ Anonimização 100% automatizada sem revisão humana
- ❌ Logs in arquivo mutável local
- ❌ LLM third-party sem aprovação do DPO
- ❌ Prompt com PII indo direto pra API global
- ❌ Compartilhar login de prod
- ❌ Hardcoded secret em código
- ❌ MFA desabilitado em produção

---

## 15. Quando Carregar Esta Skill

| Trigger | Carregar? |
|---|---|
| Backend implementando endpoint com PII | ✅ obrigatório |
| Frontend exibindo dados de usuário | ✅ obrigatório |
| Design system com novos componentes que tocam PII | ✅ recomendado |
| Documenter gerando AGENTS.md de pasta com PII | ✅ recomendado |
| Tester gerando E2E que toca PII | ✅ obrigatório |
| Code review de feature com PII | ✅ obrigatório |
| Decision log envolvendo retenção ou subprocessador | ✅ obrigatório |
| Sprint kickoff com feature de PII | ✅ no briefing inicial |

**Sempre carregue ANTES de implementar.** Prevenção é 10x mais barata
que remediação.
