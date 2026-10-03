---
name: djen-watcher
title: /djen-watcher
description: 'Varre o DJEN (Diário de Justiça Eletrônico Nacional) por novas intimações da(s) OAB(s) do escritório, deduplica contra o que já foi visto, calcula o prazo de cada uma (dias úteis, CPC art. 219) e produz um resumo diário acionável: intimação → tipo de ato → data-limite → tarefa. Use no início do dia, ou quando quiser checar publicações novas. Requer o conector DJEN (`connectors/djen/`).'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/djen-watcher
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# /djen-watcher

Watcher de intimações do DJEN. Puxa publicações novas, calcula prazos, entrega a lista do dia. **Não protocola nem dá ciência** — só surface + calcula. A ciência e a resposta são decisão do advogado.

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → OAB(s) do escritório, tribunais frequentes, dono do controle de prazos.
2. Consulta o DJEN via `djen_consultar` (por `numeroOab`+`ufOab`, janela de datas). Sem o conector, PARE e diga como instalá-lo (`connectors/djen/README.md`).
3. Deduplica contra a lista de vistos (`intimacoes-vistas.yaml` — abaixo).
4. Para cada intimação **nova**, calcula o prazo com a lógica de `/litigation-legal:prazos-cpc`.
5. Produz o resumo diário e registra as novas como vistas.

---

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (default in-house), skip — the watcher runs practice-level. Se habilitado, as intimações podem cair em matters diferentes; roteie cada uma para o matter correspondente pelo número do processo quando houver correspondência, senão liste em "não roteadas".

---

## Premissa de jurisdição (Brasil)

A **data de disponibilização** no DJEN inicia a contagem: a publicação considera-se feita no **primeiro dia útil seguinte** à disponibilização, e o prazo começa a correr no dia útil seguinte a esse (Lei 11.419/2006, art. 4º §§3º-4º `[verified: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11419.htm]`). A contagem é em **dias úteis** para prazos processuais (CPC art. 219 `[verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]`), com as ressalvas de recesso, feriados forenses e dobra que a skill `/litigation-legal:prazos-cpc` trata. O tipo de ato (contestar, manifestar, recorrer, cumprir) define o prazo aplicável — confirme o prazo de cada ato; o DJEN traz o texto, não o prazo calculado.

---

## Como funciona

**Fonte.** `djen_consultar` (conector DJEN). Parâmetros a partir do perfil: `numeroOab`, `ufOab`, `dataInicio`, `dataFim`. Se `--oab` / `--de` / `--ate` forem passados, sobrepõem. Padrão de janela: da última varredura (ver `intimacoes-vistas.yaml`) até hoje; se nunca rodou, os últimos 7 dias.

**Dedup.** Cada comunicação tem um `id`/`hash` do DJEN. Mantém-se uma lista dos já vistos em:

`~/.claude/plugins/config/claude-for-legal/litigation-legal/intimacoes-vistas.yaml`

```yaml
ultima_varredura: "2026-07-02"      # YYYY-MM-DD da última execução
vistas:
  - id: "<hash-djen>"
    processo: "0001234-56.2024.8.16.0001"
    data_disponibilizacao: "2026-06-30"
    tipo: "Intimação"
    prazo_limite: "2026-07-21"       # data-limite calculada (dias úteis)
    status: "pendente"               # pendente | ciente | respondida | perdida
```

Intimações cujo `id` já está em `vistas` não reaparecem no resumo (a não ser com `--todas`). Só as novas são processadas e anexadas.

**LGPD — este arquivo é um data store de dados pessoais.** `intimacoes-vistas.yaml` guarda números de processo, datas e partes — dado pessoal sob a LGPD. Consequências práticas:
- **Retenção:** purgue entradas com `status: respondida` ou `perdida` há mais de 12 meses — não acumule indefinidamente (LGPD art. 15-16, fim do tratamento). O watcher deve oferecer essa limpeza ao rodar. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]
- **Registro de tratamento:** este arquivo entra no registro de operações de tratamento do escritório (LGPD art. 37). Documente-o lá.
- **Local, não em nuvem compartilhada:** mantenha em disco local do escritório; já está no `.gitignore` da raiz para não ser versionado por acidente.
- **Sem sigiloso:** processos em segredo de justiça não vêm da API pública, então não caem aqui — mas se um número sensível for adicionado manualmente, trate-o com o mesmo cuidado.

**Cálculo de prazo.** Para cada nova intimação, aplica a lógica de `/litigation-legal:prazos-cpc`: identifica o tipo de ato no texto, o prazo aplicável (em dias úteis), o termo inicial (dia útil seguinte à disponibilização), e a data-limite — sinalizando recesso/feriado/dobra quando aplicável. Todo prazo calculado é **rascunho**; a tabela de feriados forenses é específica do tribunal e deve ser confirmada (calibração — ver `prazos-cpc`).

## Resumo diário

```markdown
## Intimações DJEN — [data] · OAB [n/UF]

**Novas nesta varredura:** [N]  ·  **Prazo vencendo em ≤3 dias úteis:** [N]

### 🔴 Urgente (prazo ≤3 dias úteis)
| Processo | Tribunal | Ato | Disponibilizado | Data-limite | Dias úteis restantes |
|---|---|---|---|---|---|
| [nº] | [TJ] | [contestar/manifestar/recorrer] | [data] | [data] `[verify]` | [N] |

### 🟡 Nesta semana
[mesma tabela]

### 🟢 Prazo folgado / sem prazo (ciência)
[mesma tabela]

---
**Cada data-limite é rascunho — confirme a tabela de feriados do tribunal e o tipo de ato antes de confiar.**
```

## Consequential-action gate

Este watcher **não dá ciência nem protocola** — ele lê o DJEN e calcula. Marcar uma intimação como "ciente" na `intimacoes-vistas.yaml` é controle interno, não dá ciência oficial no sistema do tribunal. **Perder um prazo é irreversível.** Se o Role em `## Who's using this` for **Non-lawyer**: apresente o resumo mas não deixe fechar nenhuma intimação como resolvida sem confirmação de advogado(a) — e reforce que a ciência/resposta oficial se dá no PJe/Domicílio Judicial Eletrônico, não aqui.

---

## What this skill does not do

- Não dá ciência oficial nem protocola resposta (isso é no PJe / Domicílio Judicial Eletrônico).
- Não decide o prazo — calcula um rascunho a partir do texto e das regras do CPC; o advogado confirma o tipo de ato e a tabela de feriados do tribunal.
- Não monitora processos sigilosos (não aparecem na API pública do DJEN).
- Não substitui o controle de prazos oficial do escritório — é uma rede de segurança adicional, não a fonte da verdade.
