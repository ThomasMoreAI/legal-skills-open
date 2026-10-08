---
name: lgpd-mobile
description: Executa auditoria LGPD direcionada para aplicações mobile.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.8.1"
---

# LGPD Mobile App

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- plataforma mobile (iOS, Android, Flutter, React Native);
- uso de Firebase e serviços cloud;
- SDKs de tracking/analytics;
- dados pessoais/sensíveis tratados no app.

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador).

Ative o cenário `mobile_app`:
- `core`, `legal`, `governance`, `mobile`, `appsec`, `cloud`.

Adicione `eca-digital` se o app for classificado para faixa etária inferior a 18 anos nas lojas ou tiver usuários menores (gatilho normativo do router — ECA Digital, Lei nº 15.211/2025).

Adicione `plataformas-digitais` se o app intermediar conteúdo de terceiros com difusão pública, oferecer anúncios/impulsionamento pagos ou gerar/alterar imagem ou som de pessoas (gatilho normativo do router — Decretos nº 12.975/2026 e nº 12.976/2026).

Adicione `ai-llm` se houver chamada a provedor ou SDK de LLM ou de IA generativa, modelo próprio, embeddings, RAG ou fine-tuning (gatilho técnico do router).

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- ler só os arquivos listados em `files` nos manifestos dos módulos ativos (`.agents/lgpd-enterprise-auditor/orchestrator/manifests/`) e avaliar todos os itens do catálogo desses módulos, cada um com o seu ID;
- validar permissões, storage local e tracking;
- exigir evidência por requisito;
- consolidar score e relatório final padrão;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
