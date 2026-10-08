---
name: lgpd-web
description: Executa auditoria LGPD direcionada para sites e landing pages.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.8.1"
---

# LGPD Web Site / Landing Page

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- tipo de página (site institucional, landing page, blog, portal);
- stack e hospedagem (Next.js, React, WordPress, Vercel, Netlify, etc.);
- formulários e dados coletados (nome, e-mail, telefone, empresa);
- cookies e trackers (Google Analytics, Meta Pixel, Hotjar, Google Ads);
- integrações de marketing/CRM (RD Station, HubSpot, Mailchimp);
- existência de política de privacidade e banner de cookies.

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador).

Ative o cenário `web_site`:
- `core`, `legal`, `governance`, `appsec`, `cloud`.

Adicione `eca-digital` se o site for direcionado ou provavelmente acessado por menores de 18 anos (gatilho normativo do router — ECA Digital, Lei nº 15.211/2025).

Adicione `plataformas-digitais` se o site publicar comentários ou outro conteúdo de terceiros com difusão pública, ou vender anúncios/impulsionamento (gatilho normativo do router — Decretos nº 12.975/2026 e nº 12.976/2026).

Adicione `ai-llm` se houver chamada a provedor ou SDK de LLM ou de IA generativa, modelo próprio, embeddings, RAG ou fine-tuning (gatilho técnico do router).

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- ler só os arquivos listados em `files` nos manifestos dos módulos ativos (`.agents/lgpd-enterprise-auditor/orchestrator/manifests/`) e avaliar todos os itens do catálogo desses módulos, cada um com o seu ID;
- validar base legal de captura de leads, consentimento de cookies e trackers antes do aceite, aplicando a seção de cookies de `.agents/lgpd-enterprise-auditor/appsec/owasp-api.md` e o `.agents/lgpd-enterprise-auditor/templates/cookie-policy-template.md`;
- validar minimização de dados no formulário e compartilhamento com terceiros;
- exigir evidência por requisito;
- produzir relatório conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
