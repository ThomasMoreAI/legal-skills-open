# Módulo DevSecOps — CI/CD e cadeia de suprimentos

## Escopo
Auditar pipeline CI/CD, cadeia de dependências e segurança de containers.

## Checklist atômico
Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`. Sem pipeline, sem containers ou sem infraestrutura como código, os itens correspondentes ficam `NAO_APLICAVEL`, com a evidência.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `DS-01` | Os segredos do pipeline estão protegidos (cofre do CI) e não aparecem em logs nem em artefatos? | 10 | `CRITICO` | — | `TECNICO` | art. 46 |
| `DS-02` | Há varredura de dependências no pipeline e política de atualização? | 10 | `MEDIO` | `ALTO` se o pipeline não tiver nenhuma varredura de segurança | `TECNICO` | art. 46 |
| `DS-03` | O SBOM é gerado e armazenado? | 10 | `BAIXO` | — | `TECNICO` | art. 46 |
| `DS-04` | As imagens Docker passam por varredura de vulnerabilidades? | 10 | `MEDIO` | — | `TECNICO` | art. 46 |
| `DS-05` | A infraestrutura como código (Terraform, CloudFormation, Helm etc.) passa por varredura de configuração? | 10 | `MEDIO` | — | `TECNICO` | art. 46 |
| `DS-06` | O ambiente Kubernetes segue controles de RBAC e hardening? | 10 | `MEDIO` | — | `TECNICO` | art. 46 |
| `DS-07` | SAST e DAST são executados em estágio apropriado do pipeline? | 10 | `MEDIO` | — | `TECNICO` | art. 46 |
| `DS-08` | Há varredura de segredos no repositório e no histórico do git, com rotação do que já foi exposto? | 10 | `ALTO` | `CRITICO` com credencial válida exposta | `TECNICO` | art. 46 |
| `DS-09` | O token do pipeline tem permissões mínimas, e as actions ou imagens de terceiros usadas nele estão fixadas por versão imutável (hash)? | 10 | `MEDIO` | — | `TECNICO` | art. 46 |
| `DS-10` | A branch de produção é protegida, com revisão obrigatória antes do deploy? | 10 | `MEDIO` | — | `TECNICO` | arts. 46 e 50 |
| `DS-11` | Ambientes de teste, homologação e CI usam dados sintéticos ou mascarados, sem cópia de dados pessoais reais de produção? | 10 | `ALTO` | — | `TECNICO` | arts. 6º, I e III, e 46 |

## Critérios de evidência
- configuração de CI/CD com controles de segredo;
- histórico de scans (dependência, SAST, DAST);
- artefatos SBOM;
- relatórios de segurança de imagem/container;
- políticas RBAC e segurança de cluster;
- resultado da varredura de segredos no repositório e no histórico;
- permissões do token do pipeline e versões fixadas das actions;
- regras de proteção da branch de produção;
- origem dos dados usados em teste, homologação e CI.

## Mapeamento para severidade e score
- Segredo exposto em pipeline/artefato público: `CRITICO`.
- Ausência total de varredura de segurança: `ALTO`.
- Cobertura parcial de scanning e hardening: `MEDIO`.
- Dados pessoais reais de produção em ambiente de teste ou no CI: `ALTO`.
- Segredo no histórico do git: `ALTO`; `CRITICO` com credencial ainda válida.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `seguranca` (domínio 10) para todos os itens deste módulo. A criticidade de cada item está na tabela do checklist.
