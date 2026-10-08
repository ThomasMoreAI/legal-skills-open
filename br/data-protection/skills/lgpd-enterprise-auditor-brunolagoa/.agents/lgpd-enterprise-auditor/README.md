# LGPD Enterprise Auditor — framework modular

## Visão geral
O framework organiza a auditoria em camadas para facilitar manutenção, escalabilidade e especialização, com cobertura equivalente à da skill (`SKILL.md`).

## Estrutura
- `core/`: contratos canônicos (evidência, severidade, score, relatório).
- `legal/`: base normativa LGPD/ANPD, bases legais, ECA Digital (`legal/eca-digital.md`, módulo `eca-digital`) e deveres de plataformas digitais (`legal/plataformas-digitais.md`, módulo `plataformas-digitais`).
- `governance/`: governança, DPO, RIPD e terceiros.
- `cloud/`: postura cloud e exposição de infraestrutura.
- `appsec/`: segurança de aplicações e APIs.
- `mobile/`: segurança/privacidade mobile.
- `devsecops/`: CI/CD, supply chain, containers e Kubernetes.
- `ai-llm/`: riscos de IA generativa, RAG e retenção.
- `orchestrator/`: roteamento de módulos por cenário, cobertura do `full_audit` (`full-audit.md`) e manifestos, que listam em `files` os arquivos de cada módulo.
- `templates/`: modelos de políticas e artefatos de conformidade (política de privacidade e de cookies, registro das operações, teste de legítimo interesse, ato de indicação do encarregado, política de retenção, RIPD, DPA, resposta a incidentes, ECA Digital).
- `reports/`: formatos de relatório por público e modelo do relatório em HTML (`html-report.md` e `html-report-template.html`).
- `validation/`: checklist de paridade com a skill e matriz de rastreabilidade dos domínios.

## Fluxo de execução
1. Capturar contexto do projeto (stack, dados, integrações).
2. Orquestrador ativa módulos aplicáveis e lê só os arquivos listados no manifesto de cada um.
3. Cada módulo ativo tem todos os itens do seu catálogo avaliados, com evidência obrigatória.
4. Core consolida severidade, score e classificação, com o teto por achado crítico e a marca de escopo.
5. Reporting engine gera relatório final.

## Modo de uso
- Modo direcionado: ativação por cenário (`saas_web`, `web_site`, `mobile_app`, `ai_llm_system`, `devsecops_pipeline`, `eca_digital_platform`, `digital_platform`). O relatório sai com a marca **escopo direcionado** e a lista dos domínios não auditados.
- Auditoria completa (`full_audit`): ativa todos os módulos e cobre os 17 domínios de auditoria.

## Catálogo de itens
Os itens do checklist são fixos. Cada módulo traz, na seção "Checklist atômico", a tabela dos seus itens, com ID estável (ex.: `SE-03`), domínio, criticidade, agravante ou atenuante, tipo de controle e fundamento. A auditoria avalia todos os itens dos módulos ativos; a criticidade só muda pelo agravante da linha do item ou pela modulação por porte. As regras estão em `core/scoring-engine.md`.

## Convenções de nomenclatura
- Módulos: kebab-case (ex.: `ai-llm`, `eca-digital`, `plataformas-digitais`).
- Áreas de score: snake_case (ex.: `ai_llm`, `eca_digital`, `plataformas_digitais`).
- Itens do catálogo: prefixo de duas ou três letras e número (ex.: `GV-08`); item extra, fora do catálogo, usa `EX-nn`.
- Essa separação evita ambiguidade entre roteamento e cálculo de score.

## Cenários rápidos
- SaaS (React/Node/Postgres/AWS): `core`, `legal`, `governance`, `cloud`, `appsec`, `devsecops`.
- Site institucional ou landing page: `core`, `legal`, `governance`, `appsec`, `cloud`.
- IA/LLM (RAG): `core`, `legal`, `governance`, `ai-llm`, `appsec`.
- Mobile (Flutter/Firebase): `core`, `legal`, `governance`, `mobile`, `cloud`, `appsec`.
- Pipeline (GitHub Actions/Docker/K8s): `core`, `legal`, `devsecops`, `cloud`, `appsec`.
- Plataforma com público infantojuvenil (ECA Digital): `core`, `legal`, `eca-digital`, `governance`, `appsec`, `mobile`.
- Plataforma digital com conteúdo de terceiros (Decretos nº 12.975 e 12.976/2026): `core`, `legal`, `plataformas-digitais`, `governance`, `appsec`, `cloud`.
- Auditoria completa (`full_audit`): `core`, `legal`, `eca-digital`, `plataformas-digitais`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

## Norma vigente x norma em monitoramento
- Só gera `finding` e `check_item` com status `NAO_CONFORME` a norma **vigente**.
- Normas em tramitação (ex.: PL nº 2338/2023 — Marco Legal da IA) e guias da ANPD em tomada de subsídios ficam em seções "Em monitoramento" nos módulos e só alimentam `recomendacoes_tecnicas` no relatório.
