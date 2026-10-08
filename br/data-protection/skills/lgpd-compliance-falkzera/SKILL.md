---
name: lgpd-compliance-falkzera
title: Compliance para apps brasileiros (LGPD, ANPD, CDC, Marco Civil)
description: 'Compliance jurídico-regulatório (LGPD, ANPD, CDC, Marco Civil) para qualquer app ou sistema construído para brasileiros. Ative SEMPRE que o projeto coletar qualquer dado pessoal (nome, e-mail, telefone, CPF, geolocalização, dado do dispositivo, cookie de tracking, foto, áudio, log que identifique pessoa), OU quando o pedido envolver "LGPD", "política de privacidade", "termos de uso", "compliance", "DPO", "encarregado", "ROPA", "consentimento de cookies", "banner de cookies", "vazamento de dados", "incidente de segurança", "direito do titular", "exportar dados do usuário", "excluir conta". Esta skill AUDITA o projeto, classifica os tratamentos, e GERA os artefatos: política de privacidade, política de cookies, banner de consentimento, ROPA preenchido, RIPD quando exigível, runbook de incidente, endpoints de exercício de direitos do titular, schema de consent_log, termos de uso e portal de transparência.'
author: Falkzera
author_url: https://github.com/Falkzera/falcao-skills-open/tree/main/skills/lgpd-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
sources:
- title: 01 Lei Fundamentos
  path: references/01-lei-fundamentos.md
- title: 02 Bases Legais
  path: references/02-bases-legais.md
- title: 03 Direitos Titular
  path: references/03-direitos-titular.md
- title: 04 Matriz Retencao
  path: references/04-matriz-retencao.md
- title: 05 Incidente Runbook
  path: references/05-incidente-runbook.md
- title: 06 Cookies Guia Anpd
  path: references/06-cookies-guia-anpd.md
- title: 07 Pequeno Porte
  path: references/07-pequeno-porte.md
- title: 08 Termos Cdc
  path: references/08-termos-cdc.md
- title: 09 Termos Mci Stf
  path: references/09-termos-mci-stf.md
- title: 10 Clickwrap Aceite
  path: references/10-clickwrap-aceite.md
- title: 11 Taxonomia Dados
  path: references/11-taxonomia-dados.md
- title: 12 Transparencia Radical
  path: references/12-transparencia-radical.md
- title: 13 Ia Ml Transparencia
  path: references/13-ia-ml-transparencia.md
- title: 14 Analytics Tracking
  path: references/14-analytics-tracking.md
---

# Compliance para apps brasileiros (LGPD, ANPD, CDC, Marco Civil)

Um app feito pra **brasileiros no Brasil** é regido pela **LGPD (Lei 13.709/2018)** + regulamentos da **ANPD** + leis correlatas (Marco Civil da Internet, CDC, ECA, Lei de Acesso à Informação quando for app governamental). Esta skill é o **escudo legal** + **kit de compliance** a aplicar em todo projeto desse tipo.

> **Convenção de tom:** os artefatos jurídicos gerados por esta skill usam linguagem **neutra, clara, com fundamento jurídico**. Sem juridiquês excessivo, sem marketing infantilizado. O leitor médio entende; o regulador reconhece a fundamentação.

> **Convenção de escopo:** esta skill cobre três frentes, usáveis juntas ou isoladamente: **LGPD/proteção de dados** (§1 a §7), **Termos de Uso** (§8) e **Inventário de Dados / Portal de Transparência** (§9).

> **Aviso sobre limites:** esta skill é apoio operacional, **não substitui parecer jurídico** em casos litigiosos ou de alto risco. Em incidentes graves, contratação de DPO terceirizado, ou exposição a sanção da ANPD, recomendar consulta a advogado ou escritório especializado em proteção de dados.

---

## 1. Quando esta skill ATIVA

Gatilhos imediatos:

1. **Início de projeto novo** que vai coletar qualquer dado pessoal, antes da primeira tela de cadastro existir, esta skill audita o que vai ser coletado e gera a política.
2. **Pedido explícito**: "rodar a skill no projeto X", "gerar política de privacidade", "preciso de banner de cookies", "vou subir um app pra brasileiros".
3. **Trigger por palavra-chave** (auto-ativação): LGPD, política de privacidade, ANPD, DPO, encarregado, ROPA, consentimento, cookies, vazamento, incidente, direito do titular, exportar dados, excluir conta, dados sensíveis, dados de criança.
4. **Antes de deploy em produção** que envolva usuário real, checar checklist mínimo de `checklists/auditoria-app.md`.
5. **Mudança que afete tratamento de dados**, nova coleta, novo terceiro (analytics, e-mail marketing, IA), nova finalidade, mudança de retenção → re-auditar e atualizar política.

Não ativar pra:

- Projetos sem usuário humano (scripts de modelagem, batch jobs sobre dados já anonimizados, ETL interno sem PII).
- Trabalho acadêmico de redação (monografia, artigo). Esta skill só entra quando a pesquisa virar app público.
- CTF, exercícios e brincadeiras locais que não saem da máquina dele.

---

## 2. Fluxo de execução

```
                 ┌─────────────────────────────────────┐
                 │ 1. AUDITORIA                        │
                 │    checklists/auditoria-app.md      │
                 │    (perguntar ao responsável ou     │
                 │     inspecionar o repo)             │
                 └─────────────────┬───────────────────┘
                                   ▼
                 ┌─────────────────────────────────────┐
                 │ 2. CLASSIFICAÇÃO                    │
                 │    a) Pequeno porte? (Res. 2/2022)  │
                 │    b) Tem dado sensível?            │
                 │    c) Alto risco (IA, biometria,    │
                 │       perfilamento, criança)?       │
                 │    d) Bases legais por finalidade   │
                 │       (references/02-bases-legais)  │
                 │    e) Transferência internacional?  │
                 └─────────────────┬───────────────────┘
                                   ▼
                 ┌─────────────────────────────────────┐
                 │ 3. GERAÇÃO                          │
                 │    <projeto>/legal/                 │
                 │    ├─ politica-privacidade.md       │
                 │    ├─ politica-cookies.md           │
                 │    ├─ banner-cookies.tsx            │
                 │    ├─ ropa.csv                      │
                 │    ├─ ripd.md  (se alto risco)      │
                 │    ├─ runbook-incidente.md          │
                 │    ├─ endpoints-direitos/           │
                 │    │   ├─ next-api/                 │
                 │    │   ├─ fastapi/                  │
                 │    │   └─ schema.sql                │
                 │    └─ agent.md  (índice do que cada │
                 │                  arquivo é)         │
                 └─────────────────┬───────────────────┘
                                   ▼
                 ┌─────────────────────────────────────┐
                 │ 4. INTEGRAÇÃO                       │
                 │    - linkar política no footer      │
                 │    - colocar banner no _app/layout  │
                 │    - registrar endpoints no router  │
                 │    - rodar migration do consent_log │
                 │    - publicar e-mail do DPO/canal   │
                 └─────────────────┬───────────────────┘
                                   ▼
                 ┌─────────────────────────────────────┐
                 │ 5. CHECKLIST FINAL                  │
                 │    checklists/politica-14-itens.md  │
                 │    checklists/seguranca-minima.md   │
                 └─────────────────────────────────────┘
```

---

## 3. Auditoria: o que perguntar ao responsável (ou descobrir no repo)

Sempre rodar `checklists/auditoria-app.md` na íntegra. Resumo das perguntas-chave:

1. **Nome legal e CNPJ** do controlador (se pessoa física, anotar CPF e endereço).
2. **Quem é o DPO neste projeto?** Pessoa física, e-mail genérico, ou regime de pequeno porte com canal `privacidade@`?, perguntar caso a caso.
3. **Porte da empresa** (verificar enquadramento na Res. CD/ANPD nº 2/2022, ver `references/07-pequeno-porte.md`).
4. **Que dados coleta?** Listar item a item: nome, e-mail, telefone, CPF, foto, geolocalização, dispositivo, IP, cookies, áudio, vídeo, dados de saúde, etc. Cruzar com art. 5º I e II.
5. **Para qual finalidade cada um?** Uma linha por finalidade no ROPA. Princípio da finalidade (art. 6º I), nada de "para melhorar sua experiência".
6. **Que terceiros recebem cada dado?** AWS, Vercel, Stripe, Mailgun, Google Analytics, Meta Pixel, Sentry, OpenAI, etc. Cada um vira processador no DPA + linha no ROPA.
7. **Onde os dados são processados?** Região do data center (sa-east-1, us-east-1, eu-west). Tudo fora do BR = transferência internacional (art. 33). **UE dispensa SCC** desde Res. 32/2026; demais países exigem SCC (Res. 19/2024).
8. **Por quanto tempo?** Retenção por dado (cruzar com `references/04-matriz-retencao.md`, fiscal, Marco Civil, CLT etc.).
9. **Tem dado sensível ou de criança/adolescente?** Se sim, regime do art. 11 + art. 14.
10. **Tem decisão automatizada que afeta usuário?** (Score, anti-fraude, recomendação algorítmica, perfil de consumo.) Art. 20.
11. **Plano de incidente?** Quem detecta, quem comunica ANPD em 3 dias úteis (6 se pequeno porte).

Saída da auditoria: tabela `dado × finalidade × base legal × retenção × terceiros × destino`. Esse é o ROPA, alimenta política, cookies, ROPA.csv.

---

## 4. Decisões automáticas que a skill toma

### 4.1 Identificar pequeno porte (Res. CD/ANPD nº 2/2022)

Ativar regime simplificado **se TODOS verdadeiros**:

- Pessoa natural, MEI, ME (ate R$ 360k/ano), EPP (até R$ 4,8M/ano), startup (LC 182/2021), pessoa jurídica sem fins lucrativos, OU ente despersonalizado;
- **NÃO** integra grupo econômico cujo faturamento global ultrapasse os limites;
- **NÃO** faz tratamento de **alto risco**, assim definido (Res. 2/2022, art. 4º):
  - decisões automatizadas que afetem direitos do titular em larga escala;
  - dados sensíveis em larga escala;
  - dados de crianças, adolescentes ou idosos em larga escala;
  - vigilância ou monitoramento sistemático de área pública em larga escala;
  - uso de tecnologias emergentes/inovadoras com impacto a direitos.

Detalhe e referências em `references/07-pequeno-porte.md`.

**Efeito:** pode dispensar DPO formal (basta canal `privacidade@`), ROPA simplificado (modelo ANPD), política de segurança simplificada, **prazos em dobro** (incidente = 6 dias úteis; declaração completa a titular = 30 dias).

### 4.2 Escolher a base legal por finalidade

Mapeamento prático (detalhe em `references/02-bases-legais.md`):

| Finalidade típica | Base sugerida |
|---|---|
| Cadastro mínimo pra entregar serviço comprado | Art. 7º V (execução de contrato) |
| Emissão de nota fiscal, retenção fiscal | Art. 7º II (obrigação legal) |
| Newsletter, marketing direto, push promocional | Art. 7º I (consentimento): **opt-in obrigatório** |
| Cookies analíticos não anonimizados | Art. 7º I (consentimento) |
| Cookies estritamente necessários (sessão, carrinho) | Art. 7º V ou IX |
| Prevenção a fraude, segurança da plataforma | Art. 7º IX (legítimo interesse) + RIPD recomendado |
| Score de crédito, anti-fraude bancário | Art. 7º X (proteção do crédito) |
| Dado sensível (saúde, biometria) | Art. 11: **consentimento específico e destacado**, salvo hipóteses do inciso II |
| Pesquisa científica com microdados | Art. 7º IV + anonimização sempre que possível |
| App de emergência médica acionando SAMU | Art. 7º VII (proteção da vida) |

### 4.3 Acionar RIPD

Gerar `templates/ripd.md` **se ANY**:

- Tratamento baseado em **legítimo interesse** (formalizar teste de balanceamento, art. 10 §3º);
- **Dado sensível em larga escala** (saúde, biometria, opinião política, religião, vida sexual);
- **Decisão automatizada** que afete direitos (art. 20);
- **Dados de criança/adolescente** (art. 14);
- **Monitoramento sistemático** (geolocalização contínua, vigilância);
- **IA/ML** que produz inferência sobre o usuário.

### 4.4 Transferência internacional (art. 33 + Res. 19/2024 + Res. 32/2026)

Toda infra fora do Brasil (AWS us-east, Vercel global, OpenAI, etc.) é **transferência internacional**. Bases legais aplicáveis:

- **Decisão de adequação da ANPD**, desde a **Resolução CD/ANPD nº 32/2026**, a **União Europeia** (e EEE) tem decisão de adequação. Transferir pra processador hospedado em UE dispensa SCC. Demais países ainda **NÃO** têm decisão de adequação.
- **SCC (Cláusulas-Padrão Contratuais) da ANPD**, pra demais países (EUA, etc.); período de graça da Res. 19/2024 terminou em 23/08/2025; obrigatório no DPA do fornecedor.
- OU consentimento específico do titular (raro, ruim de operar).
- OU obrigação legal/execução de contrato com o titular (limitado).

**Implicação prática:** preferir processadores com região **UE** (Frankfurt, Dublin, Amsterdam) sempre que disponível, dispensa SCC, é o "novo verde" do compliance brasileiro. Exemplos: Plausible (UE), Sentry-EU, PostHog-EU, Mixpanel-EU, Crisp (Amsterdam), Postmark, Resend-EU.

Sempre **declarar na política** com a base usada: "Seus dados podem ser processados em [país] via [fornecedor], com base em [decisão de adequação ANPD Res. 32/2026: UE] ou [Cláusulas-Padrão Contratuais aprovadas pela ANPD]."

---

## 5. Geração de artefatos

Saída padrão em `<projeto>/legal/`. Cada arquivo abaixo tem template em `templates/` que a skill copia e preenche os `{{placeholders}}`:

| Arquivo gerado | Template fonte | Quando gerar |
|---|---|---|
| `politica-privacidade.md` | `templates/politica-privacidade.md` | **Sempre** |
| `politica-cookies.md` | `templates/politica-cookies.md` | Se for web/PWA com cookies |
| `components/CookieBanner.tsx` | `templates/banner-cookies.tsx` | Se for Next.js/React com cookies não-essenciais |
| `ropa.csv` | `templates/ropa.csv` | **Sempre** (interno, não publicar) |
| `ripd.md` | `templates/ripd.md` | Se acionado por 4.3 |
| `runbook-incidente.md` | `references/05-incidente-runbook.md` | **Sempre** (interno) |
| `endpoints-direitos/*` | `templates/endpoints-direitos/*` | Por stack (Next ou FastAPI) |
| `schema-consent-log.sql` | `templates/endpoints-direitos/consent-log-schema.sql` | **Sempre** que houver consentimento ou exclusão |
| `agent.md` | gerar inline | **Sempre** (índice de o que é cada arquivo) |

**Placeholders comuns** que a skill preenche durante geração:

```
{{CONTROLADOR_NOME}}       Razão social / nome civil
{{CONTROLADOR_CNPJ_CPF}}   CNPJ ou CPF (último 4 dígitos pra CPF)
{{CONTROLADOR_ENDERECO}}   Endereço completo
{{DPO_NOME}}               Nome do encarregado (omitir se pequeno porte sem DPO)
{{DPO_CONTATO}}            E-mail ou URL do canal
{{APP_NOME}}               Nome do app
{{APP_URL}}                URL pública
{{DATA_ATUALIZACAO}}       YYYY-MM-DD da geração
{{LISTA_DADOS}}            Tabela "dado × finalidade × base × retenção"
{{LISTA_TERCEIROS}}        Tabela de processadores
{{TRANSFERENCIAS_INT}}     Lista de transferências internacionais com base legal
```

---

## 6. Direitos do titular: o que IMPLEMENTAR no app

O art. 18 da LGPD garante 9 direitos. **Self-service no app cobre 80%**; canal do DPO cobre os 20% complexos. Detalhe completo em `references/03-direitos-titular.md`.

Mínimo viável a construir:

| Direito | Implementação técnica mínima |
|---|---|
| Confirmação de existência | Tela autenticada "Privacidade" que confirma "sim, tratamos seus dados" |
| Acesso | Tela "Meus dados" listando perfil + histórico + origem de cada campo |
| Correção | Edição de perfil; campos não-editáveis via canal do DPO + audit log |
| Anonimização/bloqueio/eliminação por excesso | Endpoint admin pra mascarar campos específicos |
| Portabilidade | **Endpoint `GET /api/legal/export`** retornando JSON estruturado |
| Eliminação (consentimento) | **Botão "Excluir minha conta"** visível, mesmo nível do "Criar conta" |
| Informação sobre compartilhamento | Lista nominal de processadores na política + log por usuário (ideal) |
| Informação sobre consequências da negativa | UX clara no momento do consentimento |
| Revogação de consentimento | Painel "Preferências de Privacidade" com toggle por finalidade |

**SLAs internos** (art. 19 + Res. 2/2022):
- Confirmação simplificada: **imediata** (regime geral) / **15 dias** (pequeno porte)
- Declaração completa: **15 dias** (geral) / **30 dias** (pequeno porte)
- Sempre **gratuita** (art. 18 §5º)

**Templates de endpoint** prontos em `templates/endpoints-direitos/` pra Next.js (App Router) e FastAPI.

---

## 7. Incidente de segurança: runbook obrigatório

Toda skill rodando em produção precisa de `runbook-incidente.md` no projeto, gerado a partir de `references/05-incidente-runbook.md`. Prazos críticos:

- **Notificar ANPD + titulares**: 3 dias úteis (6 se pequeno porte) da ciência do incidente que envolva dados pessoais com risco/dano relevante.
- **Comunicação preliminar + 20 dias úteis pra complementar** se faltar info.
- **Registro interno de TODOS os incidentes** (mesmo os não comunicados): retenção 5 anos.

Canal oficial: **SEI!ANPD** com login Gov.br, `https://sei.anpd.gov.br/`, processo "ANPD - Comunicados de Incidentes à Agência Nacional de Proteção de Dados".

Conteúdo obrigatório da notificação (Res. CD/ANPD nº 15/2024):
- natureza e categoria dos dados afetados
- número aproximado de titulares
- medidas de segurança vigentes antes do incidente
- riscos e impactos potenciais
- medidas corretivas adotadas
- data da descoberta
- contato do DPO/canal

---

## 8. Termos de Uso

Os **Termos de Uso** são o **escudo legal** do app: definem o contrato entre você (controlador/empresa) e o usuário, limites de uso, propriedade intelectual, suspensão/exclusão de conta, foro e lei aplicável.

> **Documento separado** da Política de Privacidade. Misturar os dois é erro recorrente que pode invalidar o consentimento LGPD e dificultar versionamento independente. Ver `references/08-termos-cdc.md` seção final.

### 8.1. Quando esta skill gera Termos

- App tem **conta de usuário** ou login.
- App **cobra** (mesmo trial pago).
- App tem **UGC** (qualquer conteúdo enviado por usuário: post, comentário, upload).
- App **limita comportamentos** do usuário (anti-abuso, anti-spam, anti-scraping).
- App é **B2B/SaaS** com cliente PJ.

App **estritamente informativo** (landing page, blog, ferramenta sem conta) **dispensa** Termos formais, basta a Política de Privacidade.

### 8.2. Auditoria adicional pra gerar Termos

Além do `checklists/auditoria-app.md` da parte LGPD, perguntar:

1. **B2C, B2B ou misto?** Define regime jurídico (CDC integral vs liberdade contratual).
2. **Vertical do app:** fintech, healthtech, edtech, govtech, marketplace, SaaS genérico? Cada um tem regras adicionais (ver `references/10-clickwrap-aceite.md` seção setoriais).
3. **App cobra?** Recorrente, one-time, freemium, trial. Define cláusulas de pagamento, renovação, arrependimento.
4. **Tem UGC?** Define cláusula de licença (não cessão), canal de denúncia, notice & takedown, regime do Tema 987 STF.
5. **Idade mínima:** 18+? 13+? Permite menor? Determina cláusula de capacidade + LGPD art. 14.
6. **SLA/uptime declarado?** Se sim, redigir com cuidado em B2C (não pode esvaziar art. 20 CDC).
7. **Cap de responsabilidade:** default **B2C neutro** (sem cap monetário). Mudar só se cliente confirmar que é B2B com contraparte sofisticada.
8. **Foro:** B2C = domicílio do consumidor (CDC 101). B2B = eleição válida (sede da empresa).

### 8.3. Decisões automáticas que a skill toma

| Detecção | Cláusula que entra |
|---|---|
| App B2C ou misto | Foro do consumidor + sem cap monetário + sem arbitragem compulsória |
| App B2B puro | Cap de responsabilidade (12 meses), foro de eleição, arbitragem opcional |
| Tem UGC | Cláusula de licença não-exclusiva + canal de notice & takedown + cláusula sobre Tema 987 STF |
| App cobra | Cláusula de arrependimento 7 dias (CDC art. 49) + cancelamento self-service + reembolso proporcional |
| App pra menor | Cláusula de capacidade + verificação de idade + consentimento parental verificável |
| Fintech | Cláusulas KYC + comunicação ao COAF + remissão a regulação BCB |
| Healthtech | Cláusula de sigilo médico + dado sensível LGPD art. 11 + RIPD obrigatório |
| Govtech | Remissão à Lei 13.460/2017 + LAI + Carta de Serviços |

### 8.4. Estrutura padrão dos Termos (19 seções)

Detalhe seção-a-seção com base legal, armadilhas e redação em `references/08-termos-cdc.md` + `09-termos-mci-stf.md`. Visão geral:

1. Cabeçalho e aceitação (clickwrap)
2. Definições (glossário curto)
3. Identificação do prestador
4. Objeto / Descrição do serviço (+ disclaimers de escopo)
5. Cadastro, conta e idade mínima (LGPD art. 14)
6. Planos, pagamento e cobrança (CDC art. 49)
7. Uso permitido e proibido
8. Conteúdo do usuário (UGC), propriedade, licença, denúncia
9. Propriedade intelectual do app
10. Privacidade (remissão à Política, não duplicar)
11. Disponibilidade, manutenção e modificações
12. Limitação de responsabilidade (CDC 25 + 51)
13. Indenização (B2B)
14. Suspensão e exclusão de conta (com contraditório: STJ)
15. Alteração dos Termos (30 dias + re-aceite material)
16. Rescisão pelo usuário (tão fácil quanto criar)
17. Foro e lei aplicável (BR + domicílio do consumidor)
18. Disposições finais (severability, integralidade)
19. Histórico de versões

### 8.5. Formação válida do aceite: clickwrap

> Detalhe em `references/10-clickwrap-aceite.md`.

**Padrão ouro:**

```
[ ] Li e concordo com os Termos de Uso e com a Política de Privacidade.

         [ Criar conta ]
```

- Checkbox **vazio por padrão** (não pré-marcado).
- Botão desabilitado enquanto desmarcado.
- **Duas caixas separadas** quando a base legal LGPD for consentimento.
- Pra serviço de alto risco (financeiro, saúde): **scroll-wrap** (botão só habilita após scroll completo).

**Prova do aceite, log obrigatório:**

| Campo | Por quê |
|---|---|
| `user_id` | Identifica quem aceitou |
| `document_type` | terms_of_use \| privacy_policy \| cookies |
| `document_version` | Versão exata aceita (data ISO ou semver) |
| `document_hash` | SHA-256 do documento, prova que esta versão foi vista |
| `accepted_at` | Timestamp |
| `ip_truncated` | /24 IPv4 ou /48 IPv6 (LGPD, minimização) |
| `user_agent` | Contexto |
| `acceptance_method` | clickwrap \| scrollwrap \| reaccept_modal |

Schema completo em `templates/endpoints-direitos/consent-log-schema.sql` (tabela `tos_acceptance`).

### 8.6. Tema 987 STF (junho/2025): IMPORTANTE pra apps com UGC

O STF declarou o **art. 19 MCI parcialmente inconstitucional** e criou regime escalonado:

| Nível | Tipo de conteúdo | Regime de responsabilidade |
|---|---|---|
| 1 | Crimes contra a honra (calúnia/difamação/injúria) | Art. 19 puro, só responde após **ordem judicial** específica |
| 2 | Demais ilícitos em geral | Art. 21 expandido, responde após **notificação extrajudicial** se não remover em tempo razoável |
| 3 | Rol grave: terrorismo, racismo, atos antidemocráticos, CSAM, indução a suicídio, violência contra mulher por gênero, tráfico de pessoas | **Dever de cuidado**, remoção proativa sem notificação. Omissão sistêmica gera responsabilidade |
| 4 | Conteúdo impulsionado pago / bots / rede inautêntica | **Presunção de responsabilidade** independente de notificação |

**Pra apps com UGC, os Termos devem:**
- Ter **canal claro de notice & takedown** (template em `templates/notice-takedown-form.md`).
- Declarar expressamente que a plataforma **pode remover proativamente** conteúdo do Nível 3 (proteção contra censura privada).
- Prever **notificação reversa ao publicador** com 7 dias de contraditório (salvo urgência).
- Manter **log imutável** de denúncias e ações.
- Pra apps com boost pago: **moderação prévia mais robusta**.

### 8.7. Geração de artefatos (Termos)

Saída em `<projeto>/legal/`:

| Arquivo gerado | Template fonte | Quando |
|---|---|---|
| `termos-de-uso.md` | `templates/termos-de-uso.md` | Sempre que app tem conta/cobra/UGC |
| `notice-takedown-form.md` | `templates/notice-takedown-form.md` | Se tem UGC |
| `checklist-termos.md` | `checklists/checklist-termos.md` | Sempre (validação final) |
| Atualização do schema | `templates/endpoints-direitos/consent-log-schema.sql` (tabela `tos_acceptance`) | Sempre |

### 8.8. Integração com a parte LGPD

- A política de privacidade gerada na parte LGPD vai **linkada** pelos Termos (seção "Privacidade").
- A tabela `tos_acceptance` é **extensão da mesma migration** do `consent_log`.
- O fluxo de exclusão de conta dos endpoints LGPD **respeita** as cláusulas de suspensão/exclusão dos Termos (contraditório, exportação prévia).
- Banner de cookies, runbook de incidente, RIPD, ROPA: **inalterados**.

---

## 9. Dados e Compliance: Inventário Completo (Portal de Transparência)

**Tese:** Política de Privacidade é o **piso legal**. Portal de Transparência é o **teto competitivo**. Você entrega o que o concorrente esconde.

### 9.1. Quando esta skill gera o Portal

- App **público** que coleta qualquer PII além do estritamente operacional.
- Projeto que quer **diferenciação competitiva** (Nubank, ML, Stone publicam, concorrente pequeno não publica).
- Projeto **governamental ou acadêmico** que precisa cumprir LAI/transparência ativa.
- Projeto que **publica datasets** (data cards FAIR).
- Projeto com **IA visível** ao usuário (model cards).

### 9.2. Estrutura do Portal `/transparencia`

```
/transparencia                          # hub com Nutrition Label no topo
  /inventario                           # data inventory navegável (gerado do código)
  /nutrition-label                      # versão Apple-style detalhada
  /terceiros                            # lista de operadores + DPAs + região
  /cookies                              # categorização + controles
  /ia                                   # model cards + system cards
  /retencao                             # política de retenção tabular
  /incidentes                           # histórico de incidentes (mesmo não-notificados)
  /seguranca                            # práticas + certificados
  /dados-abertos                        # data cards DCAT (se publica datasets)
  /relatorio/{ano}                      # transparency report anual
  /direitos                             # como exercer + endpoint
  /governanca                           # DPO, organograma, comitê
  /mudancas                             # changelog global de privacidade
```

### 9.3. Componentes do inventário (12 categorias canônicas)

Detalhe em `references/11-taxonomia-dados.md`. Visão geral:

| # | Categoria | Sensibilidade típica |
|---|---|---|
| 1 | Identidade e contato | Média |
| 2 | Autenticação | Crítica |
| 3 | Financeiros | Alta |
| 4 | Identificadores de dispositivo / técnicos | Média individualmente, alta combinada |
| 5 | Geolocalização | Alta (sensível por inferência) |
| 6 | Mídia e arquivos | Variável (EXIF é trap) |
| 7 | Conteúdo do usuário (UGC) | Variável |
| 8 | Comportamentais (analytics) | Média / Crítica (replay) |
| 9 | Sensíveis (LGPD art. 11) | Sempre alta |
| 10 | Inferidos por algoritmo | Alta (art. 20) |
| 11 | Metadados de comunicação | Alta por inferência |
| 12 | De terceiros sobre o titular | Alta (controlador sem consentimento prévio) |

Pra cada uma a skill cruza com código (`rg` por palavras-chave) e marca quais aplicam ao projeto.

### 9.4. Decisões automáticas

| Detecção | Ação |
|---|---|
| Schema com `health_*`, `medical_*`, `ethnicity`, `religion`, `political_party`, `sexual_orientation` | Gerar seção "Dados Sensíveis LGPD art. 11" + acionar RIPD + exigir consentimento específico |
| Uso de OpenAI/Anthropic/Gemini API | Gerar `/transparencia/ia` + model card + verificar DPA + alertar sobre região do provedor |
| Schema com `*_score`, `*_segment`, `embedding`, `vector` | Gerar seção "Decisão Automatizada" + endpoint de contestação (art. 20) + RIPD |
| Cookies não-essenciais (GA4, Meta Pixel, Hotjar) | Banner consentimento obrigatório (Parte 1 já faz) |
| Geolocalização precisa (`getCurrentPosition`, `ACCESS_FINE_LOCATION`) | Alertar consentimento + minimização (arredondar coordenadas) |
| Upload de imagem/PDF | Recomendar strip EXIF / sanitização |
| Coleta de contatos importados (lista) | Alertar: gera dado de terceiro sem consentimento → canal público pra titular não-usuário |

### 9.5. Stack default privacy-first

Pra projeto novo, escolhas que dispensam consentimento de cookie e maximizam jurisdição amigável:

| Categoria | Default | Por quê |
|---|---|---|
| Analytics web | **Plausible** | Sem cookie, UE, legítimo interesse defensável |
| Product analytics | **PostHog EU** sem replay | Self-host opcional, masking forte |
| Error tracking | **Sentry EU** com `beforeSend` | EU region + scrubbing |
| Logs/APM | **Grafana Cloud EU** ou **BetterStack** | UE-first |
| E-mail transacional | **Postmark** ou **Resend EU** | DPA limpos |
| CRM | **RD Station** | Brasileira, cláusulas ANPD nativas |
| Chat | **Crisp** | França + hospedagem Amsterdam |
| CMP | **GoAdopt (BR)** ou **klaro** | Consent Mode v2 |

Detalhe em `references/14-analytics-tracking.md`.

### 9.6. Transparência sobre IA

Quando o app usa OpenAI/Claude/Gemini API, declarar:

- Modelo + finalidade
- Quais dados saem do app (prompt pode ter PII!)
- Política de retenção/treinamento por provedor:
  - **OpenAI API:** não treina; até 30d retenção; ZDR pra Enterprise
  - **Anthropic Claude API:** **nunca treina**; 7d retenção (desde 14/09/2025)
  - **Gemini API tier pago:** não treina
  - **Gemini API free tier:** **TREINA + revisor humano** → migrar pro pago OU consentimento específico
- Sanitização aplicada (Microsoft Presidio, regex BR)
- Disclaimer "Gerado por IA" visível
- Canal de contestação (art. 20)

Detalhe em `references/13-ia-ml-transparencia.md`.

### 9.7. Geração programática (o diferencial)

**Manifesto à mão envelhece em duas sprints.** Solução: gerado pelo código.

1. **Anotação no código**, `COMMENT ON COLUMN` em Postgres ou decorator `@pii(...)` em Python/TS
2. **Script extrator** (`scripts/gerar-inventario.py`) lê anotações + `terceiros.yaml` + `finalidades.yaml` → gera `transparencia/inventario.json`
3. **CI/CD valida drift**: GitHub Action que falha PR se campo no schema sem `@pii`, ou `@compartilha=X` não está em `terceiros.yaml`
4. **Detecção de drift em runtime**, job semanal compara declarado vs egress real
5. **Endpoint vivo** `GET /api/transparencia/inventario.json`, auditor ANPD/jornalista consome
6. **Tests as documentation**, `test_lgpd_email_nao_compartilhado_com_meta` bloqueia regressão

Templates em `templates/transparencia/automation/`.

### 9.8. Geração de artefatos (Parte 3)

Saída em `<projeto>/transparencia/` (separado de `legal/`):

| Arquivo gerado | Template fonte | Quando |
|---|---|---|
| `transparencia/inventario.yaml` | `templates/transparencia/inventario.yaml` | Sempre |
| `transparencia/terceiros.yaml` | `templates/transparencia/terceiros.yaml` | Sempre |
| `transparencia/finalidades.yaml` | `templates/transparencia/finalidades.yaml` | Sempre |
| `app/(transparencia)/page.tsx` | `templates/transparencia/portal-page.tsx` | Sempre (se Next) |
| `components/NutritionLabel.tsx` | `templates/transparencia/nutrition-label.tsx` | Sempre (se Next) |
| `components/AIDisclosure.tsx` | `templates/transparencia/ai-disclosure.tsx` | Se usa IA |
| `transparencia/ia/{modelo}.md` | `templates/transparencia/model-card.md` | Por modelo de IA usado |
| `transparencia/datasets/{id}.yaml` | `templates/transparencia/data-card.yaml` | Se publica dataset |
| `transparencia/relatorios/{ano}.md` | `templates/transparencia/transparency-report.md` | Anual |
| `scripts/gerar-inventario.py` | `templates/transparencia/automation/gerar-inventario.py` | Sempre |
| `.github/workflows/transparency-check.yml` | `templates/transparencia/automation/ci-check.yml` | Sempre |
| `transparencia/PII_CONVENTION.md` | `templates/transparencia/automation/pii-convention.md` | Sempre |

### 9.9. Integração com Partes 1 e 2

- Política de Privacidade (Parte 1) **linka** o Portal: "Para detalhes técnicos, ver Portal de Transparência."
- Termos de Uso (Parte 2) referencia o Portal pra ferramentas usadas.
- ROPA gerado na Parte 1 alimenta automaticamente o `inventario.yaml`.
- Schema `consent_log` / `tos_acceptance` (Partes 1+2) feeds o `transparency-report` (quantas requisições recebidas, atendidas).

---

## 10. Como esta skill se integra ao projeto

- **Git/PR:** os artefatos gerados entram no repositório como código, versionados, revisados em PR, com changelog próprio (`legal/CHANGELOG.md`). Política de privacidade não é anexo de e-mail.
- **Banco de dados:** as migrations de `consent_log` e `tos_acceptance` seguem o mesmo fluxo de migration do resto do projeto.
- **Design system:** o banner de cookies precisa parecer parte do app, não enxerto genérico. Adapte os tokens visuais do template ao design system em uso.
- **Pesquisa interna:** projeto sem usuário real não precisa de toda a parafernália; aplique a partir do momento em que houver titular de dados de verdade.
- **Infraestrutura:** o runbook de incidente precisa citar o provedor real (acesso a logs, snapshot, isolamento de instância). Preencha com a stack do projeto.

---

## 11. Referências canônicas (sempre consultar)

Dentro desta skill:

**LGPD:**
- `references/01-lei-fundamentos.md`, texto, princípios, definições
- `references/02-bases-legais.md`, matriz das 10 + 8 hipóteses
- `references/03-direitos-titular.md`, os 9 direitos do art. 18, o que construir
- `references/04-matriz-retencao.md`, quanto tempo guardar cada dado, por lei
- `references/05-incidente-runbook.md`, passo a passo SEI!ANPD
- `references/06-cookies-guia-anpd.md`, banner, classificação, dark patterns proibidos
- `references/07-pequeno-porte.md`, regime simplificado da Res. 2/2022

**Termos de Uso:**
- `references/08-termos-cdc.md`: CDC art. 51, limitação de responsabilidade, foro, arbitragem, jurisprudência STJ
- `references/09-termos-mci-stf.md`: Marco Civil, Tema 987 STF (junho/2025), UGC, notice & takedown
- `references/10-clickwrap-aceite.md`, formação válida, versionamento, comunicação de mudanças, setoriais

**Dados e Compliance (Portal de Transparência):**
- `references/11-taxonomia-dados.md`, 12 categorias canônicas com detecção no código + minimização
- `references/12-transparencia-radical.md`: Apple Nutrition Labels, Data Cards DCAT, transparency report, geração programática
- `references/13-ia-ml-transparencia.md`, declaração de IA, art. 20 LGPD, PL 2338, EU AI Act, model cards
- `references/14-analytics-tracking.md`, comparação ferramentas + stack default privacy-first

Fontes externas (sempre validar versão antes de citar):

**LGPD:**
- [Lei 13.709/2018 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm), fonte canônica
- [Portal ANPD](https://www.gov.br/anpd/pt-br), guias, resoluções, formulários
- [SEI!ANPD](https://sei.anpd.gov.br/), notificação de incidente
- [Guia de Elaboração de Política (PPSI/Governo Digital)](https://www.gov.br/governodigital/pt-br/privacidade-e-seguranca/ppsi)
- [Modelo de ROPA simplificado (ANPD)](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes)
- [Guia Cookies (ANPD (23/01/2025))](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_orientativo_cookies_e_protecao_de_dados_pessoais)
- [Resolução CD/ANPD nº 2/2022 (Pequeno Porte)](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022)
- [Resolução CD/ANPD nº 15/2024 (Incidente)](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis)
- [Resolução CD/ANPD nº 19/2024 (Transferência Internacional)](https://www.gov.br/anpd/pt-br/assuntos/noticias/resolucao-normatiza-transferencia-internacional-de-dados)
- [Resolução CD/ANPD nº 4/2023 (Dosimetria de Sanções)](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd)

**Termos de Uso:**
- [Lei 8.078/1990 (CDC)](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm)
- [Lei 12.965/2014 (Marco Civil da Internet)](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm)
- [Lei 9.610/1998 (Direitos Autorais)](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm)
- [Lei 9.307/1996 (Arbitragem)](https://www.planalto.gov.br/ccivil_03/leis/l9307.htm)
- [Decreto 7.962/2013 (E-commerce)](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm)
- [Lei 14.063/2020 (Assinaturas eletrônicas)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14063.htm)
- [STF (Tema 987 (responsabilidade de provedor, julgamento 26/06/2025))](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=987)

---

## 12. Princípio operacional

Privacidade e compliance **não** são "documento que se faz no fim". São **decisão de produto desde o primeiro mockup**:

- Antes de adicionar campo no cadastro: cabe na finalidade declarada? qual base legal?
- Antes de integrar terceiro: tem DPA? região de processamento? SCC?
- Antes de feature de IA/ML: precisa RIPD? decisão automatizada com revisão?
- Antes de ir pra produção: política linkada? banner funcionando? endpoints de direitos publicados?

Esta skill **roda em ciclo**: toda mudança que toca dado pessoal dispara reavaliação. Construa rápido, mas construa **dentro da lei**.
