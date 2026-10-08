---
name: lgpd-devsecops
description: Executa auditoria LGPD direcionada para pipelines DevSecOps.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.8.1"
---

# LGPD DevSecOps Pipeline

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- plataforma de CI/CD;
- estratégia de containers e Kubernetes;
- gestão de segredos e scans de segurança;
- fluxo de deploy e ambientes.

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador).

Ative o cenário `devsecops_pipeline`:
- `core`, `legal`, `devsecops`, `cloud`, `appsec`.

Adicione `ai-llm` se houver chamada a provedor ou SDK de LLM ou de IA generativa, modelo próprio, embeddings, RAG ou fine-tuning (gatilho técnico do router).

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- ler só os arquivos listados em `files` nos manifestos dos módulos ativos (`.agents/lgpd-enterprise-auditor/orchestrator/manifests/`) e avaliar todos os itens do catálogo desses módulos, cada um com o seu ID;
- validar segredos, supply chain e hardening de deploy;
- exigir evidência para todos os achados;
- gerar score e relatório técnico/compliance;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
