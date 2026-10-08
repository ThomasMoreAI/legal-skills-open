# Núcleo — contratos do auditor

## Objetivo
Estabelecer os contratos canônicos da auditoria LGPD Enterprise, garantindo consistência entre módulos especialistas, scoring e relatórios.

## Princípios obrigatórios
- Não assumir conformidade sem evidência.
- Exigir base legal válida para cada operação de tratamento.
- Priorizar minimização, segurança, rastreabilidade e privacy by design/default.
- Avaliar impacto técnico, jurídico, operacional e reputacional.

## Contratos canônicos

### `finding`
Estrutura mínima para cada não conformidade. Todo `check_item` com status `NAO_CONFORME` **ou** `PARCIAL` gera um `finding`: no `NAO_CONFORME`, a severidade é a `criticality` do item; no `PARCIAL`, é **um nível abaixo** da `criticality` (`CRITICO` → `ALTO`, `ALTO` → `MEDIO`, `MEDIO` → `BAIXO`, `BAIXO` → `BAIXO`), sem escolha caso a caso.
- `id`: identificador único.
- `module`: módulo origem (ex.: `cloud`, `ai-llm`).
- `title`: título objetivo.
- `problem`: descrição objetiva do problema.
- `severity`: `CRITICO | ALTO | MEDIO | BAIXO`.
- `lgpd_article`: artigo(s) aplicáveis da LGPD.
- `evidence_type`: grau de comprovação do controle - `ENCONTRADA | PARCIAL | AUSENTE` (um único grau por achado).
- `evidence_source`: origem da evidência - `TECNICA | DOCUMENTAL`; um achado pode ter as duas origens (`TECNICA + DOCUMENTAL`).
- `evidence`: uma ou mais evidências observadas, cada uma com sua origem e descrição rastreável.
- `evidence_confidence`: confiança da evidência - `ALTA | MEDIA | BAIXA` (`core/evidence-engine.md`).
- `technical_impact`: impacto técnico.
- `legal_impact`: impacto jurídico/regulatório.
- `recommendation`: ação recomendada.
- `owner`: responsável sugerido.
- `deadline_suggestion`: `IMEDIATO | 30_DIAS | 90_DIAS | 180_DIAS` (`IMEDIATO` = até 7 dias). Prazo máximo pela severidade: `CRITICO` → `IMEDIATO`; `ALTO` → `30_DIAS`; `MEDIO` → `90_DIAS`; `BAIXO` → `180_DIAS`. Pode ser mais curto quando a correção é a mesma de um achado mais urgente; nunca mais longo. O aceite de risco não muda este campo (o novo prazo vai em `accepted_deadline`).
- `effort`: esforço estimado da correção - `P | M | G` (P: até 1 dia; M: até 1 semana; G: mais de 1 semana).
- `severity_modulation` (opcional): quando a severidade foi modulada por porte e exposição (`core/severity-model.md`) - severidade original, severidade aplicada e justificativa.
- `risk_acceptance` (opcional): quando o controlador decidiu aceitar o risco - `accepted_by` (nome e papel de quem aceitou), `accepted_at` (data), `justification`, `review_at` (data de revisão, no máximo 12 meses depois) e, se o aceite adiar a correção, `accepted_deadline` (novo prazo, mantido também o `deadline_suggestion` original). O aceite **não** altera status, severidade nem score.

### `check_item`
Estrutura mínima de checklist. Os itens vêm do catálogo dos módulos (`core/scoring-engine.md`, "Catálogo de itens"): a auditoria avalia todos os itens de cada módulo ativo.
- `id`: ID do item no catálogo (ex.: `SE-03`); item extra, fora do catálogo, usa `EX-nn`.
- `domain`: domínio de auditoria, pelo código do catálogo (`BL` ou `1` a `17`, mapa em `core/scoring-engine.md`).
- `score_area`: área de score em que o item pontua - exatamente uma, definida pelo domínio (mapa em `core/scoring-engine.md`).
- `criticality`: severidade que o item teria se não conforme - `CRITICO | ALTO | MEDIO | BAIXO`; define o peso do item no score. É a criticidade do catálogo, alterada só pelo agravante ou atenuante escrito na linha do item ou pela modulação por porte.
- `control_type`: natureza do controle - `TECNICO` (código, configuração, infraestrutura) ou `DOCUMENTAL` (política, contrato, registro, processo). Item que exige os dois é classificado por onde o controle é executado: em sistema, `TECNICO`; por ato formal, `DOCUMENTAL`.
- `item`: requisito validado, com o texto do catálogo.
- `applicability`: `APLICAVEL | NAO_APLICAVEL | NAO_VERIFICADO` (regras em `core/scoring-engine.md`). Só item `APLICAVEL` tem `status` e entra no score.
- `status`: `CONFORME | PARCIAL | NAO_CONFORME` (apenas para item `APLICAVEL`).
- `evidence`: uma ou mais evidências, cada uma com sua origem e descrição rastreável.
- `evidence_type`: `ENCONTRADA | PARCIAL | AUSENTE` (um único grau por item).
- `evidence_source`: `TECNICA | DOCUMENTAL`; um item pode ter as duas origens (`TECNICA + DOCUMENTAL`).
- `evidence_confidence`: `ALTA | MEDIA | BAIXA` (`core/evidence-engine.md`).
- `impact`: impacto caso falha.
- `recommendation`: correção sugerida.

### `module_output`
Resultado padrão por módulo:
- `module`: nome do módulo.
- `coverage`: cobertura do módulo - itens com `status` ÷ (itens com `status` + itens `NAO_VERIFICADO`), em percentual.
- `check_items`: lista de `check_item`.
- `findings`: lista de `finding`.
- `gaps`: itens obrigatórios ausentes.
- `recommendations`: recomendações priorizadas.

O módulo não calcula score: o score é sempre por área, feito pelo núcleo a partir dos `check_items` de todos os módulos (`core/scoring-engine.md`).

## Fluxo mínimo de execução
1. Levantar o contexto: primeiro ler o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependência e de infraestrutura); apresentar o contexto inferido e perguntar só o que faltar, incluindo a natureza do agente de tratamento (entradas de `orchestrator/router.md`) e o formato de saída do relatório (`core/reporting-engine.md`).
2. Ativar módulos por contexto via orquestrador.
3. Executar o checklist: avaliar todos os itens do catálogo de cada módulo ativo, com evidência obrigatória.
4. Classificar achados por severidade.
5. Calcular score por área e score global, aplicar o teto de classificação e registrar o escopo do score.
6. Gerar relatório com formato obrigatório.

## Cobertura completa
O modo `full_audit` ativa todos os módulos e cobre os 17 domínios de auditoria definidos em `orchestrator/full-audit.md`, os mesmos da skill (`SKILL.md`).
