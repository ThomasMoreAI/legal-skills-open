---
name: lgpd-full-audit
description: Executa auditoria LGPD completa (full_audit), com todos os módulos ativos.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.8.1"
---

# LGPD Full Audit

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- stack completa (frontend, backend, banco, cloud);
- dados pessoais e dados sensíveis tratados;
- integrações de terceiros;
- contexto de DevSecOps e IA/LLM;
- existência de usuários menores de 18 anos (ECA Digital);
- intermediação de conteúdo de terceiros, anúncios/impulsionamento pagos ou IA que gera imagem/voz (plataformas digitais).

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador).

Execute no modo `full_audit` com cobertura total:
- `core`, `legal`, `eca-digital`, `plataformas-digitais`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- ler só os arquivos listados em `files` nos manifestos dos módulos ativos (`.agents/lgpd-enterprise-auditor/orchestrator/manifests/`) e avaliar todos os itens do catálogo desses módulos, cada um com o seu ID;
- não assumir conformidade sem evidência;
- aplicar severidade e score conforme `.agents/lgpd-enterprise-auditor/core/`;
- gerar saída no formato de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
