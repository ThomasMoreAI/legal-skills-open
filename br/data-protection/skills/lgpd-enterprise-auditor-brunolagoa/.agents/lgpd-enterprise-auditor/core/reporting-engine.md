# Núcleo — formato do relatório

## Objetivo
Definir formato obrigatório e ordem de construção do relatório final.

## Estrutura obrigatória
1. `resumo_executivo`
2. `score_lgpd`
3. `checklist_conformidade`
4. `nao_conformidades`
5. `itens_obrigatorios_ausentes`
6. `riscos_identificados`
7. `plano_adequacao`
8. `recomendacoes_tecnicas`

## Antes das 8 seções
Um bloco **Contexto e escopo**, que não conta como seção: o contexto levantado e sua fonte, a natureza e o papel do agente de tratamento, a saída do roteador (módulos ativos, com a justificativa, e escopo excluído, com a evidência) e as limitações da análise (o que não pôde ser acessado). No `.html`, é o campo `context`.

## Campos mínimos por seção

### `resumo_executivo`
- nível geral de conformidade;
- síntese de riscos por severidade;
- **o que fazer agora**: as 3 a 5 ações de maior impacto, em linguagem simples, cada uma com esforço (`P | M | G`) e prazo;
- riscos aceitos de severidade `CRITICO`, quando houver, em destaque.

### `score_lgpd`
- score 0-100;
- classificação final canônica, com as marcas que couberem: **classificação limitada por achado crítico** (teto de `core/scoring-engine.md`, citando os achados que o causam) e **escopo direcionado** (cenário diferente de `full_audit`, com o ID do cenário);
- domínios fora do escopo do cenário, quando houver;
- score por área;
- áreas `NAO_APLICAVEL`, com justificativa, e pesos ajustados (regra de `core/scoring-engine.md`);
- `score_tecnico` e `score_documental` (informativos);
- cobertura global e por área; se a global for menor que 80%, marcar **score parcial** ao lado da classificação; área com cobertura menor que 50% recebe a marca **cobertura baixa**;
- verificações pendentes que podem alterar o score: itens `NAO_VERIFICADO` (com o acesso necessário) e itens cuja severidade depende de verificação ainda não feita;
- natureza do agente de tratamento e eventuais modulações de severidade por porte.

### `checklist_conformidade`
Tabela obrigatória:
`Item | Área | Status | Evidência | Impacto | Recomendação`

A coluna `Item` segue o formato `ID · criticality · control_type — texto do item` (ex.: `SE-03 · ALTO · TECNICO — …`), com os valores do catálogo: sem a `criticality`, o score não pode ser refeito a partir do relatório. Item extra (`EX-nn`) vem identificado como tal. A coluna `Área` traz a `score_area` do item (mapa de `core/scoring-engine.md`).

O checklist traz todos os itens do catálogo dos módulos ativos: os `APLICAVEL` na tabela principal e os demais na tabela de itens fora do cálculo.

Status permitidos:
- `CONFORME`
- `PARCIAL`
- `NAO_CONFORME`

A célula `Evidência` deve registrar os eixos de `core/evidence-engine.md` no formato `GRAU (ORIGEM), confiança NIVEL: descrição`, ex.: `ENCONTRADA (TECNICA), confiança ALTA: política de retenção aplicada em job de expurgo`. A origem pode ser `TECNICA`, `DOCUMENTAL` ou `TECNICA + DOCUMENTAL`; com mais de uma evidência, separar as descrições por ponto e vírgula.

A tabela principal lista só itens `APLICAVEL`. Logo abaixo, uma segunda tabela traz os itens fora do cálculo:
`Item | Área | Aplicabilidade | Justificativa ou acesso necessário`

com `NAO_APLICAVEL` (inexistência comprovada ou obrigação de outro agente) e `NAO_VERIFICADO` (o que impediu a verificação e o acesso necessário).

### `nao_conformidades`
Para cada achado:
- problema;
- severidade;
- fundamento LGPD;
- impacto técnico;
- impacto jurídico;
- evidência (com `evidence_type`, `evidence_source` e `evidence_confidence`);
- correção recomendada, com esforço (`P | M | G`);
- modulação de severidade, quando houver;
- aceite de risco, quando houver (quem aceitou, quando, justificativa e data de revisão).

### `riscos_identificados`
Separar por:
- técnicos;
- jurídicos;
- operacionais;
- reputacionais.

Listar à parte os **riscos aceitos**, com o registro de aceite de cada um.

### `plano_adequacao`
- curto prazo: 0-30 dias;
- médio prazo: 30-90 dias;
- longo prazo: 90-180 dias.

`IMEDIATO` e `30_DIAS` entram no curto prazo, `90_DIAS` no médio e `180_DIAS` no longo. Cada ação traz responsável sugerido e esforço estimado (`P`: até 1 dia; `M`: até 1 semana; `G`: mais de 1 semana).

## Após as 8 seções
- **Glossário**: termos técnicos e jurídicos usados no relatório (ex.: registro das operações de tratamento, encarregado, RIPD, varredura de dependências), em uma linha cada, para leitores de fora da área.
- **Aviso legal** (texto fixo, ao final de todo relatório):
  > Este relatório foi gerado com apoio de IA pelo LGPD Enterprise Auditor, a partir das evidências disponíveis no momento da análise. Ele apoia, mas não substitui, a avaliação do encarregado (DPO) e a assessoria jurídica especializada. As conclusões dependem da completude e da atualidade das evidências fornecidas.

Glossário e aviso legal não contam como seções e não alteram a ordem obrigatória.

## Arquivos gerados
O relatório tem três formatos de saída. Perguntar **sempre** qual o usuário quer, logo no início, na mesma rodada das perguntas do levantamento de contexto (`orchestrator/router.md`), salvo se o pedido já disser:

| Formato | O que é gravado | Para quê |
|---|---|---|
| `.md` | o relatório em Markdown | versionar, comparar auditorias, servir de entrada para outra ferramenta |
| `.md` e `.html` | os dois arquivos, com o mesmo nome base e na mesma pasta | resultado completo; os dados são escritos duas vezes, então a auditoria custa mais |
| `.html` | só a visualização para o navegador | leitura por quem decide e por quem corrige, com score em destaque, filtros, busca e impressão |

Regras:
- em qualquer formato, o relatório traz as 8 seções, na ordem obrigatória, e os anexos acima;
- o `.html` é gerado a partir do modelo `reports/html-report-template.html`, preenchendo só o bloco de dados, conforme `reports/html-report.md`; é um arquivo único, sem recursos externos, e não redefine formato, severidade nem score;
- em `.md` e `.html`, os dois arquivos trazem os mesmos dados; havendo divergência, vale o `.md`;
- sem resposta do usuário (execução sem interação), gravar o `.md`;
- com arquivo gravado, a resposta em tela traz só o resumo (score, classificação com suas marcas, cobertura, não conformidades por severidade, "o que fazer agora" e o caminho dos arquivos), sem repetir o relatório inteiro, salvo pedido do usuário;
- sem acesso de escrita a arquivos, entregar o relatório completo em texto.

## Classificação e armazenamento
O relatório, em qualquer formato, descreve falhas que podem estar abertas e é **confidencial**:
- iniciar o documento com a marcação `CONFIDENCIAL — uso interno`;
- não versionar em repositório público; preferir local fora do repositório auditado ou pasta ignorada pelo git (ex.: `docs/lgpd/auditorias/`, listada no `.gitignore`); se a pasta de destino não estiver ignorada, avisar no resumo, sem alterar o `.gitignore` por conta própria;
- compartilhar só com quem precisa agir sobre os achados;
- nomear com data e escopo (ex.: `auditoria-lgpd-AAAA-MM-<cenario>.md` ou `.html`) para permitir comparação entre auditorias.

## Regra de consistência
Todo item `NAO_CONFORME` ou `PARCIAL` do checklist deve aparecer detalhado em `nao_conformidades`.
