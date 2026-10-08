# Relatório em HTML

> Visualização do relatório canônico definido em `core/reporting-engine.md`. Traz as mesmas 8 seções, na mesma ordem. Quando o `.md` também é gerado, os dois têm os mesmos dados; havendo divergência, vale o `.md`.
> Como o relatório canônico, é **confidencial**: o modelo já traz a marcação `CONFIDENCIAL — uso interno` e o aviso legal de `core/reporting-engine.md`.

## O que é
Um arquivo `.html` único, para leitura no navegador por quem decide e por quem corrige: score com medidor, áreas, checklist e não conformidades com filtro e busca, plano por prazo, tema claro e escuro e versão para impressão ou PDF.

O arquivo é gerado a partir do modelo `reports/html-report-template.html`. O modelo tem o estilo e o comportamento prontos; a auditoria preenche **apenas um bloco de dados em JSON**. O arquivo funciona offline e não carrega nenhum recurso externo (fontes, scripts, imagens), então abrir o relatório não envia dados a terceiros.

## Quando gerar
Quando o usuário escolher o formato `.md` e `.html` ou só `.html` (pergunta obrigatória de `core/reporting-engine.md`, "Arquivos gerados"):
- `.md` e `.html`: os dois arquivos com o mesmo nome base, na mesma pasta (`auditoria-lgpd-AAAA-MM-<cenario>.md` e `.html`);
- só `.html`: o JSON é escrito direto a partir dos resultados da auditoria, sem gerar o `.md`.

## Como gerar
1. **Copiar** `.agents/lgpd-enterprise-auditor/reports/html-report-template.html` para o destino, com o nome do relatório. Copiar o arquivo (ex.: `cp`), sem ler nem reescrever o conteúdo do modelo.
2. No arquivo copiado, **substituir a linha** `{"_modelo": true}`, que fica dentro de `<script type="application/json" id="lgpd-dados">`, pelo JSON descrito abaixo. O JSON pode ocupar várias linhas. Usar a ferramenta de edição de arquivos ou um script; evitar `sed`, que tropeça em `&`, `/` e `\` do texto.
3. **Não alterar mais nada.** Estilo, script, marcação de confidencialidade e aviso legal são fixos.
4. **Conferir.** Se houver shell, validar a sintaxe do JSON antes de inserir (ex.: gravar o JSON num arquivo temporário e passar por `python3 -m json.tool`). Quem tiver o repositório do projeto pode ir além com `scripts/validate-report.py <relatorio.html>`, que confere enums, IDs do catálogo, a relação entre itens e achados e o cálculo. Ao abrir o arquivo, o modelo avisa se o JSON for inválido e mostra o alerta "Conferir o cálculo" quando o score, a cobertura ou o score de uma área declarados diferem do recálculo feito a partir do checklist. Havendo alerta, corrigir os dados (também no `.md`, se ele foi gerado) antes de entregar.

## Regras do JSON
- JSON válido: aspas duplas, sem vírgula sobrando, sem comentários; quebra de linha dentro de texto como `\n`.
- Em todo o JSON, escrever o caractere "menor que" (`<`) como a sequência `\u003c`: por exemplo, `<head>` vira `\u003chead>`. Assim um trecho de código citado na evidência não encerra o bloco de dados.
- Valores de enum sempre na forma canônica de `core/auditor-core.md` (`NAO_CONFORME`, `CRITICO`, `30_DIAS`, `TECNICA + DOCUMENTAL`). O modelo exibe a forma legível ("Não conforme") e mantém o valor canônico.
- O conteúdo é o do relatório canônico: tudo o que as 8 seções exigem, com dado pessoal real mascarado. Quando o `.md` também é gerado, os dois trazem os mesmos dados, inclusive prazos e responsáveis de cada ação.
- Números com ponto decimal. `score` global é inteiro de 0 a 100; score de área e subtotais têm uma casa; `coverage`, `weight` e `adjusted_weight` são percentuais de 0 a 100 (peso ajustado com duas casas). A conferência tolera diferença de até 0,05.
- Enum citado dentro de um texto aparece como foi escrito: usar a forma canônica entre crases (ex.: `` `NAO_CONFORME` ``).
- Campos de texto aceitam marcação leve: `**negrito**`, `` `código` ``, listas (`- ` e `1. `), tabelas, títulos (`###`), citação (`> `) e bloco de código entre cercas. HTML não é interpretado: aparece como texto.
- O ID de um item do checklist citado em qualquer texto (ex.: `OP-02`) vira link para a não conformidade ou para o item.
- Campo sem informação pode ser omitido; a seção correspondente aparece como "Sem registros".

## Estrutura do JSON
As chaves das seções são os IDs canônicos de `core/reporting-engine.md`. Os campos de `checklist_conformidade` e `nao_conformidades` são os de `check_item` e `finding` (`core/auditor-core.md`).

| Chave | Conteúdo |
|---|---|
| `meta` | `audited` (nome do auditado), `subtitle`, `date` (`AAAA-MM-DD`), `command`, `scenario`, `modules` (lista de IDs dos módulos ativos), `framework_version` (a `metadata.version` do comando ou da skill em uso), `method` (texto simples, sem marcação) e `notice` (aviso opcional no topo) |
| `context` | texto: contexto inferido, escopo, módulos ativados, escopo excluído e limitações |
| `resumo_executivo` | `overview` (nível geral de conformidade), `strengths` (pontos fortes), `accepted_risks` (frase de destaque sobre riscos aceitos; a tabela de riscos aceitos é montada pelo modelo) e `actions`: "o que fazer agora", lista de `{ action, why, effort, deadline, items }` |
| `score_lgpd` | `score`, `classification` (já com o teto de classificação aplicado), `coverage`, `score_tecnico`, `score_documental`, `agent_nature`, `agent_role`, `severity_modulation`, `areas`, `pending_checks` e `out_of_scope` |
| `score_lgpd.out_of_scope` | lista de textos: todo domínio cujo módulo não foi ativado, com o motivo em poucas palavras, inclusive aqueles cujo objeto não existe (vazia ou omitida no `full_audit`) |
| `score_lgpd.areas` | uma entrada por área: `{ id, score, weight, adjusted_weight, coverage }`; área não aplicável: `{ id, weight, applicability: "NAO_APLICAVEL", justification }`; área aplicável sem nenhum item avaliado (cobertura insuficiente): `{ id, weight, coverage: 0, justification }`, sem `score` |
| `score_lgpd.pending_checks` | itens cujo status ou severidade dependem de verificação: `{ item, current, may_change, check }`; `item` é um ID ou uma lista de IDs e pode ser omitido quando a pendência não é de um item (ex.: confirmar o enquadramento de alto risco). Os itens `NAO_VERIFICADO` não entram aqui: o modelo os lista a partir do checklist |
| `checklist_conformidade` | todos os itens do catálogo dos módulos ativos, um `check_item` por item: `id` (o ID do catálogo, ex.: `SE-03`; item extra usa `EX-nn` e traz `justification`), `domain`, `score_area`, `criticality`, `control_type`, `item`, `applicability`, `status`, `evidence`, `evidence_type`, `evidence_source`, `evidence_confidence`, `impact`, `recommendation`. Item `NAO_APLICAVEL` ou `NAO_VERIFICADO` não tem `status` nem campos de evidência: traz só `justification`, que no `NAO_APLICAVEL` inclui o rastro da evidência de inexistência (arquivo e linha) e no `NAO_VERIFICADO`, o que impediu a verificação e o acesso necessário |
| `nao_conformidades` | todos os `finding`: `id`, `item_id` (ID do `check_item` que o gerou), `module`, `title`, `problem`, `severity`, `severity_note` (por que essa severidade), `lgpd_article`, `evidence`, `evidence_type`, `evidence_source`, `evidence_confidence`, `technical_impact`, `legal_impact`, `recommendation`, `owner`, `deadline_suggestion`, `effort` e, quando houver, `severity_modulation` (`original`, `applied`, `justification`) e `risk_acceptance` (`accepted_by`, `accepted_at`, `justification`, `review_at`, `accepted_deadline`) |
| `itens_obrigatorios_ausentes` | lista de `{ requirement, norm, items }` |
| `riscos_identificados` | `tecnicos`, `juridicos`, `operacionais` e `reputacionais`: listas de texto |
| `plano_adequacao` | lista de `{ action, items, owner, effort, deadline }`, na ordem de execução |
| `recomendacoes_tecnicas` | texto, com blocos de código quando houver |
| `glossary` | lista de `{ term, definition }` |
| `notes` | opcional: texto extra ao fim de uma seção, com o ID da seção como chave (qualquer uma das 8; ex.: `notes.score_lgpd` para as regras aplicadas e a memória de cálculo) |

Os campos sem enum são texto livre (`agent_nature`, `agent_role`, `severity_modulation`, `norm`, `owner`, `justification`). `domain` é o código do domínio no catálogo (`BL` ou `1` a `17`) e `module` é o ID do módulo (`appsec`, `legal`); os dois são opcionais. `item`, `score_area`, `criticality` e `control_type` vêm da linha do item no catálogo; a `criticality` só difere do padrão pelo agravante ou atenuante da linha ou pela modulação por porte, e a evidência diz qual foi aplicado. `score_tecnico` e `score_documental` usam a fórmula do score de área, aplicada a todos os itens de cada `control_type`.

`evidence` é um texto ou uma lista de textos (uma por evidência). `items` é uma lista de IDs do checklist. `effort` é `P`, `M` ou `G`; `deadline` e `deadline_suggestion` são `IMEDIATO`, `30_DIAS`, `90_DIAS` ou `180_DIAS`.

Exemplo reduzido, só para mostrar a forma (dois itens de uma única área: 2 de 5 pontos, score 40; um relatório real traz todos os itens do catálogo dos módulos ativos):

```json
{
  "meta": { "audited": "Exemplo Ltda.", "date": "2026-10-03", "command": "/lgpd-web", "scenario": "web_site", "framework_version": "1.8.1" },
  "resumo_executivo": {
    "overview": "Score 40/100, `CRITICO`. O principal risco é o rastreamento sem consentimento (CK-02).",
    "actions": [
      { "action": "Carregar o pixel só depois do aceite.", "why": "Hoje todo visitante é rastreado.", "effort": "P", "deadline": "IMEDIATO", "items": ["CK-02"] }
    ]
  },
  "score_lgpd": {
    "score": 40, "classification": "CRITICO", "coverage": 100,
    "areas": [ { "id": "bases_legais", "score": 40.0, "weight": 12, "adjusted_weight": 100, "coverage": 100 } ],
    "out_of_scope": ["8. Mobile security", "10. DevSecOps", "12. IA/LLM", "16. ECA Digital", "17. Plataformas digitais"]
  },
  "checklist_conformidade": [
    { "id": "CK-01", "score_area": "bases_legais", "criticality": "MEDIO", "control_type": "TECNICO",
      "item": "Rejeitar está disponível na primeira camada do banner, com o mesmo destaque de aceitar?", "applicability": "APLICAVEL", "status": "CONFORME",
      "evidence_type": "ENCONTRADA", "evidence_source": "TECNICA", "evidence_confidence": "ALTA",
      "evidence": "Botões lado a lado, com o mesmo estilo (`public/index.html:41-45`)", "recommendation": "Manter" },
    { "id": "CK-02", "score_area": "bases_legais", "criticality": "ALTO", "control_type": "TECNICO",
      "item": "Cookies e scripts não essenciais ficam bloqueados até o aceite?", "applicability": "APLICAVEL", "status": "NAO_CONFORME",
      "evidence_type": "AUSENTE", "evidence_source": "TECNICA", "evidence_confidence": "ALTA",
      "evidence": "`public/index.html:8-15` carrega o pixel no `\u003chead>`, antes do banner",
      "impact": "Rastreamento sem consentimento válido", "recommendation": "Carregar rastreadores só após o aceite" }
  ],
  "nao_conformidades": [
    { "id": "NC-01", "item_id": "CK-02", "module": "appsec", "title": "Pixel disparado antes do consentimento",
      "problem": "O pixel envia `PageView` antes de o banner aparecer.", "severity": "ALTO", "lgpd_article": "art. 7º, I; art. 8º",
      "evidence_type": "AUSENTE", "evidence_source": "TECNICA", "evidence_confidence": "ALTA", "evidence": "`public/index.html:8-15`",
      "technical_impact": "Cookie gravado em toda visita.", "legal_impact": "Tratamento sem base legal.",
      "recommendation": "Carregar o script só depois de \"Aceitar\".", "owner": "CTO", "deadline_suggestion": "IMEDIATO", "effort": "P" }
  ]
}
```

## O que o modelo monta sozinho
Não repetir no JSON o que o modelo deriva dos dados:
- contagem de não conformidades por severidade e de itens por status;
- a marca **classificação limitada por achado crítico** (quando há `finding` `CRITICO` e o score cairia numa faixa acima de `PARCIALMENTE_CONFORME`) e a marca **escopo direcionado** (quando `meta.scenario` não é `full_audit`);
- itens fora do cálculo e lista de itens `NAO_VERIFICADO` entre as verificações pendentes;
- riscos aceitos (a partir de `risk_acceptance` de cada achado);
- plano separado em curto, médio e longo prazo (a partir de `deadline`);
- conferência do score global, do score por área, da cobertura, da classificação e dos subtotais técnico e documental, pela fórmula de `core/scoring-engine.md`.

Um exemplo completo está em `examples/saas-demo/relatorio-auditoria-lgpd.html`, no repositório do projeto.
