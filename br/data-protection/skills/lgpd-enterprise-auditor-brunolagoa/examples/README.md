# Exemplos

Exemplos públicos de uso do LGPD Enterprise Auditor. Todos os projetos e dados desta pasta são **fictícios**.

## `saas-demo/` — AgendaFácil

Um SaaS pequeno e inventado de agendamento para clínicas (Node.js/Express, páginas estáticas, Vercel e Postgres). Ele trata dados de saúde e tem **falhas intencionais**, ao lado de controles bem feitos, para mostrar o framework em ação.

| Arquivo | O que é |
|---|---|
| [`saas-demo/README.md`](saas-demo/README.md) | Descrição do projeto fictício e contexto da empresa |
| [`saas-demo/relatorio-auditoria-lgpd.md`](saas-demo/relatorio-auditoria-lgpd.md) | Relatório completo gerado pela auditoria |
| [`saas-demo/relatorio-auditoria-lgpd.html`](saas-demo/relatorio-auditoria-lgpd.html) | O mesmo relatório na versão visual, para abrir no navegador (baixe o arquivo) |
| [`saas-demo/docs/lgpd/politica-de-privacidade.md`](saas-demo/docs/lgpd/politica-de-privacidade.md) | Política de privacidade propositalmente incompleta |

O relatório mostra:

- as 8 seções obrigatórias na ordem canônica, o glossário e o aviso legal;
- a natureza e o papel do agente: pequeno porte com tratamento de alto risco (sem modulação de severidade), operador dos dados dos pacientes e controlador das contas das clínicas e do rastreamento que ele mesmo instalou;
- o checklist com todos os itens do catálogo dos módulos ativos (109 no cenário `saas_web`), cada um com seu ID, evidências por arquivo e linha e nível de confiança, mais a tabela de itens fora do cálculo (`NAO_APLICAVEL` e `NAO_VERIFICADO`);
- o cálculo do score passo a passo (com `ai_llm`, `eca_digital` e `plataformas_digitais` como `NAO_APLICAVEL` e pesos ajustados), a cobertura por área, as verificações pendentes e os scores técnico e documental;
- a marca de **escopo direcionado**, com os domínios que o cenário não auditou, e a regra do teto de classificação por achado crítico;
- um registro de aceite de risco;
- a versão em HTML, com os mesmos dados: score com medidor, checklist e não conformidades com filtro e busca, plano por prazo e conferência automática do cálculo.

O projeto **não deve ser usado em produção** nem como base para um sistema real.

## Como o exemplo foi produzido

O relatório foi gerado com o comando `/lgpd-saas`, que ativa o cenário `saas_web` (`core`, `legal`, `governance`, `appsec`, `cloud`, `devsecops`). O agente seguiu `.agents/lgpd-enterprise-auditor/orchestrator/router.md` e os contratos de `core/`: levantou o contexto a partir dos arquivos do projeto, avaliou cada item com evidência, calculou o score com a fórmula de `core/scoring-engine.md` e montou o relatório conforme `core/reporting-engine.md`.

## Como reproduzir

A partir da raiz deste repositório:

```bash
./scripts/install.sh install --target claude --version local --project-dir examples/saas-demo
cd examples/saas-demo
claude
```

Antes de rodar, tire `relatorio-auditoria-lgpd.md` e `relatorio-auditoria-lgpd.html` da pasta (ou renomeie-os), para que o agente não use o relatório pronto como ponto de partida. No Claude Code, rode `/lgpd-saas`. Para outras ferramentas, troque `--target` (`cursor`, `vscode`, `opencode` ou `agents`). O `--version local` instala o framework a partir desta cópia do repositório, em vez da última versão publicada.

O resultado não será idêntico palavra por palavra, mas o score deve ser reproduzível: os itens e a `criticality` de cada um vêm do catálogo, então, com as mesmas evidências e o mesmo status por item, a fórmula leva ao mesmo número. Para conferir um relatório, na raiz deste repositório: `python3 scripts/validate-report.py examples/saas-demo/relatorio-auditoria-lgpd.html --md examples/saas-demo/relatorio-auditoria-lgpd.md`. Os arquivos criados pelo instalador (`.agents/`, `.claude/` etc.) estão no `.gitignore` do exemplo. Para removê-los, use `./scripts/install.sh uninstall --project-dir examples/saas-demo --non-interactive`.

## Relatórios reais são confidenciais

Este relatório é público apenas porque o projeto é fictício. Um relatório de auditoria real descreve falhas que podem estar abertas e deve:

- começar com a marcação `CONFIDENCIAL — uso interno`;
- **nunca** ser versionado em repositório público; prefira um local fora do repositório auditado ou uma pasta ignorada pelo git (ex.: `docs/lgpd/auditorias/`, listada no `.gitignore`);
- ser compartilhado só com quem precisa agir sobre os achados;
- ter nome com data e escopo, como `auditoria-lgpd-AAAA-MM-<cenario>.md` e `auditoria-lgpd-AAAA-MM-<cenario>.html`.
