# LGPD Enterprise Auditor

<p align="center">
  <img src="./assets/logo-lgpd-enterprise-auditor.webp" alt="Logo LGPD Enterprise Auditor" width="355" />
</p>

<p align="center">
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/stargazers"><img src="https://img.shields.io/github/stars/BrunoLagoa/lgpd-enterprise-auditor?style=social" alt="GitHub stars" /></a>
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/latest"><img src="https://img.shields.io/github/v/release/BrunoLagoa/lgpd-enterprise-auditor" alt="Release" /></a>
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/actions/workflows/install.yml"><img src="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/actions/workflows/install.yml/badge.svg" alt="CI" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License MIT" /></a>
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor"><img src="https://hits.sh/github.com/BrunoLagoa/lgpd-enterprise-auditor.svg?label=Project%20views&color=f1c40f" alt="Project views" /></a>
</p>

<!-- README-I18N:START -->

**Português (Brasil)** | [English](./README.en.md)

<!-- README-I18N:END -->

Framework de auditoria LGPD orientado a evidências, com foco em segurança, governança e uso de IA em engenharia de software.

Este projeto foi desenhado para funcionar como um sistema auditável e modular, pronto para ser reutilizado em diferentes produtos e times.

**Em resumo:** você instala o auditor no seu projeto com um comando, roda `/lgpd-saas` (ou outro cenário) no seu assistente de IA e recebe um relatório com score de 0 a 100, não conformidades com o artigo da LGPD e a evidência de cada uma, e um plano de adequação com prazos e esforço. Funciona com Claude Code, Cursor, VS Code + GitHub Copilot, OpenCode, Codex e Gemini CLI.

Você escolhe o formato do relatório no início da auditoria: `.md` (texto completo, bom para versionar e comparar), `.html` (para ler no navegador, com o score em destaque, filtros, busca e versão para impressão) ou os dois. O `.html` é um arquivo único, funciona offline e não carrega nada de fora.

Veja um relatório de exemplo, gerado sobre um SaaS fictício, nos dois formatos:

- [Relatório em Markdown (`.md`)](./examples/saas-demo/relatorio-auditoria-lgpd.md): abre aqui mesmo, no GitHub.
- [Relatório em HTML (`.html`)](./examples/saas-demo/relatorio-auditoria-lgpd.html): baixe o arquivo e abra no navegador. A imagem abaixo mostra o topo dele.

[![Relatório de exemplo em HTML: score 20 de 100, classificação, não conformidades por severidade e resumo executivo](./examples/saas-demo/relatorio-auditoria-lgpd.png)](./examples/saas-demo/relatorio-auditoria-lgpd.html)

## O que é este projeto

O `lgpd-enterprise-auditor` é um framework que combina:

- auditoria jurídica (LGPD + ANPD);
- auditoria técnica (appsec, cloud, mobile, devsecops, IA/LLM);
- modelo de severidade e score;
- formato de relatório padronizado;
- comandos práticos para execução por cenário.

Na prática, ele permite rodar auditorias completas ou direcionadas com consistência de critérios, evidências e plano de adequação.

## Instalação

Um único comando interativo, executado na raiz do projeto que você quer auditar. Ele pergunta qual ferramenta de IA você usa e se quer instalar também a skill, mostra um resumo e instala tudo **localmente, dentro desse projeto** (não existe instalação global).

**macOS / Linux / WSL / Git Bash**

```bash
curl -fsSL https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/latest/download/install.sh | bash -s -- install
```

**Windows (PowerShell)**

```powershell
powershell -ExecutionPolicy Bypass -Command "iwr https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/latest/download/install.ps1 -OutFile $env:TEMP\lgpd-install.ps1; & $env:TEMP\lgpd-install.ps1 install"
```

Prefere ler o script antes de rodar? Baixe (`curl -fsSL <url> -o install.sh`), revise e depois execute `bash install.sh install`.

Os comandos acima baixam o instalador da última release, a mesma versão do framework que ele instala. O instalador usa a última versão publicada. Se não conseguir consultá-la (sem rede ou limite da API do GitHub), ele avisa e não instala a branch `main` por conta própria: no modo interativo pergunta antes; com `--non-interactive`, para e pede `--version`.

**Conferir a integridade.** As releases a partir da v1.6.0 publicam `install.sh`, `install.ps1` e `SHA256SUMS`. Para instalar uma versão exata e conferir o arquivo antes de rodar:

```bash
V=vX.Y.Z   # a versão desejada
curl -fsSLO "https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/download/${V}/install.sh"
curl -fsSLO "https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/download/${V}/SHA256SUMS"
shasum -a 256 --ignore-missing -c SHA256SUMS   # no Linux: sha256sum --ignore-missing -c SHA256SUMS
bash install.sh install --version "$V"
```

### Onde os arquivos ficam

O framework (`.agents/lgpd-enterprise-auditor/`) é o mesmo para todas as ferramentas; só os comandos e a skill opcional mudam de lugar:

| Ferramenta (`--target`) | Comandos | Skill (opcional) |
|---|---|---|
| `claude` — Claude Code | `.claude/commands/lgpd-*.md` | `.claude/skills/lgpd-enterprise-auditor/` |
| `cursor` — Cursor | `.cursor/commands/lgpd-*.md` | `.agents/skills/lgpd-enterprise-auditor/` |
| `vscode` — VS Code + GitHub Copilot | `.github/prompts/lgpd-*.prompt.md` | `.agents/skills/lgpd-enterprise-auditor/` |
| `opencode` — OpenCode | `.opencode/commands/lgpd-*.md` | `.agents/skills/lgpd-enterprise-auditor/` |
| `agents` — Codex, Gemini CLI e similares | — (sem slash commands) | `.agents/skills/lgpd-enterprise-auditor/` (sempre instalada) |

- **Sem a skill (padrão):** a auditoria é acionada pelos slash commands (`/lgpd-saas`, `/lgpd-full-audit`…), que executam o framework modular (`.agents/lgpd-enterprise-auditor/`).
- **Com a skill:** o assistente também pode iniciar a auditoria a partir de um pedido em linguagem natural ("faça uma auditoria LGPD deste projeto"), carregando a skill autocontida (`SKILL.md`).
- Várias ferramentas no mesmo projeto são suportadas: rode o instalador uma vez por ferramenta. Elas compartilham a pasta do framework.

### Atualizar, verificar e desinstalar

| Ação | Comando (bash) | PowerShell |
|---|---|---|
| Atualizar todas as ferramentas instaladas | `… \| bash -s -- update` | `… install.ps1 update` |
| Verificar a instalação | `… \| bash -s -- check` | `… install.ps1 check` |
| Desinstalar | `… \| bash -s -- uninstall` | `… install.ps1 uninstall` |

`…` representa o mesmo prefixo `curl …/install.sh` ou `iwr …/install.ps1` usado na instalação.

Uso em scripts / CI (sem perguntas):

```bash
curl -fsSL https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/latest/download/install.sh \
  | bash -s -- install --non-interactive --target cursor --with-skill
```

| Opção (bash) | PowerShell | Descrição |
|---|---|---|
| `--target <ferramenta>` | `-Target` | `claude`, `cursor`, `vscode`, `opencode` ou `agents` (obrigatória com `--non-interactive`) |
| `--with-skill` / `--no-skill` | `-WithSkill` / `-NoSkill` | Instala ou não a skill (padrão: não) |
| `--project-dir <dir>` | `-ProjectDir` | Projeto de destino (padrão: raiz git do diretório atual) |
| `--version <ref>` | `-Version` | Tag ou branch (padrão: última tag publicada) |
| `--non-interactive` | `-NonInteractive` | Executa sem perguntas |

Cada instalação registra um manifesto em `.agents/lgpd-enterprise-auditor/.install/<ferramenta>.json`; `update`, `check` e `uninstall` se baseiam nele e nunca mexem em arquivos que não sejam do framework.

Se você aceitar o backup oferecido na reinstalação, a cópia vai para `.lgpd-auditor-backup/` no seu projeto — adicione essa pasta ao `.gitignore`:

```gitignore
.lgpd-auditor-backup/
```

As notas de cada versão estão no [CHANGELOG](./CHANGELOG.md).

### Instalação manual

Copie `.agents/lgpd-enterprise-auditor/` para a raiz do seu projeto e os arquivos de `commands/` para a pasta de comandos da sua ferramenta (tabela acima). Para a skill, copie `SKILL.md` para `<pasta de skills>/lgpd-enterprise-auditor/SKILL.md`.

## Base legal e atualização

Este framework usa como referência principal a **Lei Geral de Proteção de Dados (LGPD)**:

- **Texto oficial (Planalto):** [Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- **Órgão regulador:** [ANPD](https://www.gov.br/anpd/) — desde a **Lei nº 15.352/2026**, denominada **Agência** Nacional de Proteção de Dados e submetida ao regime das agências reguladoras da Lei nº 13.848/2019 (art. 55-A da LGPD).
- **Norma correlata:** [ECA Digital — Lei nº 15.211/2025](https://www.gov.br/anpd/pt-br/assuntos/eca-digital), em vigor desde 17/03/2026, regulamentada pelo Decreto nº 12.880/2026 e fiscalizada pela ANPD.
- **Plataformas digitais:** [Decreto nº 12.975/2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/D12975.htm) (atualiza a regulamentação do Marco Civil da Internet — dever de cuidado, notificação e remoção, anúncios, guarda de registros de acesso) e [Decreto nº 12.976/2026](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/D12976.htm) (proteção de mulheres na internet), em vigor desde 20/07/2026 e fiscalizados pela ANPD.

Regulamentos da ANPD considerados pelo framework:

| Resolução | Assunto |
|---|---|
| CD/ANPD nº 1/2021 | Processo de fiscalização e processo administrativo sancionador |
| CD/ANPD nº 2/2022 | Agentes de tratamento de pequeno porte |
| CD/ANPD nº 4/2023 | Dosimetria e aplicação de sanções |
| CD/ANPD nº 15/2024 | Comunicação de incidente de segurança (3 dias úteis) |
| CD/ANPD nº 18/2024 | Atuação do encarregado (DPO) |
| CD/ANPD nº 19/2024 | Transferência internacional e cláusulas-padrão contratuais |
| CD/ANPD nº 30/2025 | Mapa de Temas Prioritários de fiscalização 2026-2027 |
| CD/ANPD nº 31/2025 | Agenda Regulatória 2025-2026 |
| CD/ANPD nº 32/2026 | União Europeia reconhecida como grau adequado de proteção |

| Item | Valor |
|------|--------|
| Última sincronização | `2026-10` |

## Como o projeto está organizado

```text
.
├── SKILL.md
├── scripts/
│   ├── install.sh
│   ├── install.ps1
│   ├── validate-report.py
│   └── tests/
├── commands/
│   ├── lgpd-full-audit.md
│   ├── lgpd-saas.md
│   ├── lgpd-web.md
│   ├── lgpd-mobile.md
│   ├── lgpd-ai-llm.md
│   ├── lgpd-devsecops.md
│   ├── lgpd-eca-digital.md
│   └── lgpd-plataformas-digitais.md
└── .agents/
    └── lgpd-enterprise-auditor/
        ├── core/
        ├── legal/
        ├── governance/
        ├── cloud/
        ├── appsec/
        ├── mobile/
        ├── devsecops/
        ├── ai-llm/
        ├── orchestrator/
        ├── templates/
        ├── reports/
        └── validation/
```

### Fonte canônica

O caminho base canônico do framework modular é:

`.agents/lgpd-enterprise-auditor/`

Esse é o padrão esperado para projetos que adotarem a mesma estrutura.

## Como funciona

O fluxo da auditoria segue 5 passos:

1. **Contexto do projeto**: stack, dados tratados, integrações e operação.
2. **Roteamento inteligente**: o orquestrador ativa módulos por cenário.
3. **Checklist com evidência**: todos os itens do catálogo dos módulos ativos são avaliados, cada um com ID fixo e peso definido; nada é marcado como conforme sem comprovação.
4. **Consolidação**: severidade, score e classificação final. Com achado crítico aberto, a classificação não passa de `PARCIALMENTE_CONFORME`; em cenário direcionado, o relatório sai com a marca **escopo direcionado** e a lista dos domínios não auditados.
5. **Saída padronizada**: relatório executivo/técnico/compliance + plano de adequação, gravado em `.md`, em `.html` ou nos dois.

O relatório, em qualquer formato, descreve falhas que podem estar abertas e é **confidencial**: guarde-o fora de repositórios públicos (por exemplo, numa pasta listada no `.gitignore`).

Para conferir um relatório gerado (IDs do catálogo, valores permitidos, relação entre itens e achados e o cálculo do score), rode `python3 scripts/validate-report.py <relatorio.html>` a partir de um clone deste repositório.

## Modos de uso

### 1) Auditoria completa

Use quando quiser cobertura total:

- comando: `commands/lgpd-full-audit.md`
- cenário: `full_audit`

Módulos acionados: `core`, `legal`, `eca-digital`, `plataformas-digitais`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

### 2) Auditoria por cenário

Use para escopo focado:

- `lgpd-saas` -> SaaS web
- `lgpd-web` -> sites e landing pages
- `lgpd-mobile` -> app mobile
- `lgpd-ai-llm` -> sistemas com IA/LLM
- `lgpd-devsecops` -> pipelines e supply chain
- `lgpd-eca-digital` -> plataformas acessadas por crianças e adolescentes (LGPD art. 14 + ECA Digital)
- `lgpd-plataformas-digitais` -> provedores de aplicações com conteúdo de terceiros, anúncios pagos ou IA que gera imagem/voz (Decretos nº 12.975/2026 e 12.976/2026)

## Comandos disponíveis

Os comandos em `commands/` são atalhos de execução para o agente.

Todos incluem:

- metadados (`name`, `description`, `license`, `author`, `version`);
- coleta de contexto mínimo quando não mapeado;
- regras obrigatórias de evidência e consistência com o framework modular.

## Contratos de auditoria (resumo)

Os contratos centrais estão em `.agents/lgpd-enterprise-auditor/core/`:

- `auditor-core.md`: estruturas canônicas (`finding`, `check_item`, `module_output`);
- `evidence-engine.md`: regras de evidência;
- `severity-model.md`: classificação de severidade;
- `scoring-engine.md`: cálculo de score, catálogo de itens, teto de classificação e escopo do score;
- `reporting-engine.md`: formato obrigatório da saída e arquivos gerados (`.md`, `.html` ou os dois).

## Para quem este projeto é útil

- times de engenharia e plataforma;
- segurança da informação e AppSec;
- compliance e privacidade;
- consultorias de adequação LGPD;
- squads com uso de IA generativa em produção.

## Boas práticas de adoção

- manter `.agents/lgpd-enterprise-auditor/` versionado junto ao produto;
- adaptar comandos por domínio, sem quebrar contratos do core;
- registrar evidências técnicas e documentais por item;
- revisar score e não conformidades por release;
- tratar auditoria como processo contínuo, não evento isolado.

## Roadmap sugerido

- templates mais ricos por setor (healthtech, fintech, gov);
- automação de coleta de evidências;
- geração de matriz de risco por ambiente;
- relatórios comparativos entre releases;
- integração com pipelines CI/CD.

## Pessoas por trás do LGPD Enterprise Auditor

Este projeto evolui com contribuições de pessoas que acreditam em engenharia de software com IA de forma disciplinada, prática e auditável.

<p align="left">
  <a href="https://github.com/BrunoLagoa/lgpd-enterprise-auditor/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=BrunoLagoa/lgpd-enterprise-auditor&max=100" alt="Contribuidores do projeto" width="45" />
  </a>
</p>

Quer aparecer aqui também? Abra uma issue, sugira melhorias ou envie um PR.

## Suporte e contribuição

- Dúvidas: use as [Discussions](https://github.com/BrunoLagoa/lgpd-enterprise-auditor/discussions).
- Bugs, melhorias e **atualizações normativas**: abra uma [issue](https://github.com/BrunoLagoa/lgpd-enterprise-auditor/issues/new/choose).
- Para contribuir, leia o [guia de contribuição](./CONTRIBUTING.md) e o [código de conduta](./CODE_OF_CONDUCT.md). Vulnerabilidades: siga a [política de segurança](./SECURITY.md).
- Notas de cada versão: [CHANGELOG](./CHANGELOG.md).

## Aviso legal

O LGPD Enterprise Auditor apoia auditorias de conformidade com a LGPD, mas **não substitui** a avaliação do encarregado (DPO) nem a assessoria jurídica especializada. Os relatórios são gerados com apoio de IA, a partir das evidências disponíveis, e as conclusões dependem da completude e da atualidade dessas evidências.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo [`LICENSE`](LICENSE) para os termos completos.
