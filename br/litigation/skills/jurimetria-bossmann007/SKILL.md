---
name: jurimetria-bossmann007
title: /jurimetria
description: 'Estrutura um protocolo de pesquisa de jurimetria: dada uma tese jurídica + tribunal/vara/relator, produz um plano de pesquisa para DataJud (API pública CNJ) / JusBrasil / Escavador a estimar taxa de procedência, tempo médio de tramitação, faixa de condenação, tendências de relator/câmara. Planeja e estrutura a query; interpreta resultados que o advogado cola de volta. Não inventa estatísticas. Saída orienta precificação de acordo / avaliação de risco.'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/litigation-legal/skills/jurimetria
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# /jurimetria

Jurimetria é análise quantitativa de jurisprudência para modelar risco processual. Esta skill estrutura a pesquisa — não a executa. Você roda as queries; essa skill interpreta os números que você cola de volta e marca o que não pode ser aferido.

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → case theory, side, core jurisdictions.
2. Ask the user for: tese jurídica (uma frase), tribunal/vara (ou comarca), e relator (se aplicável).
3. Produce: structured query plan + interpretation framework + flags for uncertainty.
4. When the user pastes results, interpret: taxa de procedência, faixa de condenação, tempo de tramitação, outliers.
5. Frame as input to pricing a settlement, assessing odds, or calibrating reserves.

---

# Jurimetria — Protocol Design

## Matter context

Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/litigation-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` — especially the case theory, side, jurisdiction (comarca / vara), and phase. If the practice profile `## Core jurisdictions` lists specific fora, preload them as search options. Write outputs to the matter folder if a matter is active; otherwise to the practice-level `jurimetria/` folder.

---

## Purpose

Jurimetry answers: "Given my thesis and this tribunal, what does the historical case law tell me about my odds?" The output is a **research plan** — a structured set of queries you'll run in DataJud / JusBrasil / Escavador and a framework for interpreting what you get back.

**Se o conector DataJud estiver instalado** (`connectors/datajud/` — ferramentas `datajud_pesquisar` e `datajud_buscar_processo`), esta skill pode puxar os metadados **diretamente**, sem você colar resultados: use `datajud_pesquisar` com filtros (`classe_codigo`, `assunto_codigo`, `orgao_julgador`, `data_ajuizamento_de/ate`, `tribunal`) e `agregacoes` (aggregations Elasticsearch) para computar contagens — ex.: distribuição por órgão julgador, volume por classe/assunto, série temporal por ano de ajuizamento. **Limite crítico:** o DataJud traz *metadados e movimentos*, não o *resultado de mérito* — não há campo "procedente/improcedente". Taxa de procedência real só sai de leitura de dispositivos (JusBrasil/Escavador ou leitura manual). Use o DataJud para volume, tempo de tramitação (diferença entre movimentos de distribuição e baixa/arquivamento) e distribuição por órgão; para taxa de êxito, combine com pesquisa de teor. Nunca reporte procedência inferida de metadados como se fosse aferida. Sem o conector, a skill apenas monta o plano de queries que você roda manualmente e interpreta o que você cola de volta.

This produces strategic facts: **taxa de procedência** (plaintiff success rate), **tempo médio de tramitação** (how long it takes), **faixa de condenação** (typical award range), and **relator / câmara tendencies** (does this judge or appellate chamber tend to rule for or against your side on claims like yours). These inform: settlement pricing, litigation risk modeling, reserve estimates, and the decision to settle vs. fight.

---

## Jurisdiction assumption / Premissa de jurisdição (Brasil)

Brasil: jurimetria é prática relativamente recente (últimos ~10 anos), baseada no acesso crescente a decisões digitalizadas via CNJ (DataJud [model knowledge — verify]) e plataformas privadas (JusBrasil, Escavador). Não é uma ciência — é análise de padrões em amostras históricas que podem não repetir no seu caso específico. O resultado é **sempre indicativo, nunca conclusivo** `[model knowledge — verify]`.

**Dados públicos:**
- **DataJud (API da CNJ)** `[model knowledge — verify]` — acesso público a decisões da Justiça Estadual, Justiça Federal, Tribunais Superiores. Inclui decisões proferidas desde ~2015-2016, dependendo do tribunal. Cobertura aumentou significativamente; ainda há gaps por tribunal e período.
- **JusBrasil, Escavador** — plataformas privadas com agrups de decisões; incluem casos anteriores a 2015 em alguns tribunais. Modelos de acesso: acesso básico (títulos e ementas), acesso premium (texto completo).

**Limitações estruturais:**
- Decisões monocráticas (despachos, decisões de juiz singular) podem não estar digitalizadas ou indexadas de maneira searchable — isso enviesará a amostra em favor de acórdãos (decisões de colegiado).
- Casos resolvidos por acordo / homologação de transação podem não gerar decisão no mérito, subestimando a "procedência real."
- O prazo médio reflete a amostra dos casos julgados, não a distribuição real de casos (alguns são para sentença rápida; outros pegam anos).
- Jurimetria funciona melhor em temas recorrentes com jurisprudência cristalizada (p. ex., ação revocatória contra doação, cobrança de duplicata). Funciona pior em temas novel ou em questões de interpretação contratual altamente factuais (aí os números não capturam o que importa).

---

## Load the playbook / Load context

- `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md` → risk calibration, case theory, side, core jurisdictions
- Active matter's `matter.md` — the case thesis, the side (plaintiff / defendant), the jurisdiction and forum, the phase (pleadings / discovery / trial)
- If the practice profile has `## Frequent fora` listed, offer those as quick-start options

If `CLAUDE.md` has `[PLACEHOLDER]` markers, DON'T bounce and wait — run in provisional mode **by default, immediately**, and tell the user once at the top:

> ⚠️ Rodando contra defaults genéricos (Justiça Estadual, risco médio, critérios de procedência generalizados) — seu perfil de prática ainda não foi configurado. Rode `/litigation-legal:cold-start-interview` (2 min) para calibrar à SUA prática (sua avaliação de risco, sua paisagem local, seu estilo). Resultado abaixo tagueado `[PROVISIONAL]`.

Não espere o usuário pedir — o valor tem que aparecer no primeiro run. A entrevista melhora, não desbloqueia.

### Provisional mode

Run the jurimetry using generic defaults: Justiça Estadual in their core jurisdiction(s) if listed, generic risk thresholds, no practice-level playbook. Tag the methodology line and the final output with `[PROVISIONAL]`. At the end, append:

> "Esse foi um run genérico contra defaults. Rode `/litigation-legal:cold-start-interview` para output calibrado à SUA prática — sua avaliação de risco, sua paisagem jurisprudencial local, seu estilo. 2 minutos."

---

## Workflow

### Step 1: Intake — the thesis and the forum

Ask:

> **Qual é sua tese jurídica?** (Uma frase — p. ex., "ação de cobrança de duplicata contra sacador e avalista" ou "ação indenizatória por inadimplemento contratual com cláusula penal.")

> **Qual tribunal / vara / comarca?** (P. ex., "TJSP 1ª Vara Empresarial da Capital", "TRT-2 (Trabalho)", "Justiça Federal Seção SP", ou apenas "meu tribunal padrão" se estiver no `## Frequent fora` do CLAUDE.md.)

> **Você é autor ou réu?** (Isso inverte o viés da amostra — se você está vendo "taxa de procedência 60%", significa que 60% dos autores em seus temas ganham; para o réu, é 40% de derrota.)

> **Relator ou câmara específica?** (Opcional — se houver um relator/câmara conhecido por tendência em seu tribunal, ajuda a refinar.)

> **Qual é seu threshold de risco?** Ou aceitamos "padrão da prática" — geralmente: >70% procedência = baixo risco para autor / baixa exposição para réu; 40–70% = risco moderado; <40% = risco alto / exposição alta. (Isso varia por jurisdição, por tipo de case, por asset da empresa. Confirme com você.)

---

### Step 2: Map the research

Produce a structured **query plan** with:

**A. Claim / cause of action (mapped to searchable terms in DataJud / JusBrasil)**

| Query | Example |
|---|---|
| **Base search** | `"ação de cobrança" AND "duplicata" AND tribunal:[TJSP]` ou equivalente na plataforma |
| **Date range** | Last 3–5 years (adjust if you want older precedent or recent shifts) |
| **Filters** | Judgment on the merits only (exclude dismissals, procedural defaults) |
| **Scope** | Monocratic decisions (judge) + collegiate decisions (chamber)? |

**B. Outcome variable (what counts as "success" for your side)**

- **For plaintiff (tese é do autor):** "Success" = sentença de procedência total ou parcial (condenação). Partial procedência counts. Partial dismissal counts as mixed.
- **For defendant (tese é do réu):** "Success" = sentença de improcedência. Dismissals on procedure do NOT count as success on merits — they're removed from the sample.
- **State the benchmark:** "70% or higher = favorable odds for settlement; <40% = expect to fight."

**C. Variables to extract from the sample**

| Variable | Why it matters | How to measure |
|---|---|---|
| **Taxa de procedência** | Raw plaintiff success rate | (Procedent cases / Total merit decisions) × 100 |
| **Tempo médio** | Case duration | Median (or mean) months from filing to judgment |
| **Faixa de condenação (se quantificável)** | Award range | Min, median, max (e.g., min R$ 10K, median R$ 250K, max R$ 5M) |
| **Câmara / Relator tendência** | Does your judge/chamber lean one way? | (Procedent cases from this judge / Total decisions by this judge) — flag if n < 10 (small sample = unreliable) |
| **Outliers / reversals on appeal** | What percent reverse at appellate level? | (Reversed at TJ/TST / Total appellate decisions) × 100 — flag if appeal rate is low (may indicate rare appeals or strong trial judgments) |

---

### Step 3: Guidance on running the search

**No silent supplement.** This skill does NOT run DataJud / JusBrasil for you. Instead, it tells you what to search for and how to interpret what comes back. You paste the results; I flag statistical artifacts and what they mean.

**For DataJud (CNJ API)** `[model knowledge — verify]`:
- Public API; free access. Covers Justiça Estadual, Federal, some Tribunais Superiores from ~2015–2016 onward.
- Query syntax varies by tribunal. Suggest consulting the CNJ's documentation for your specific tribunal's API (`[model knowledge — verify]`).
- Return datasets often large; filter by class of action, date, outcome before exporting.

**For JusBrasil / Escavador:**
- Proprietary platforms; may require paid subscription for full-text search and bulk export.
- Interface-based searching (type in the query, filter by tribunal/date/outcome) is more user-friendly than API for one-off queries.
- Both have heuristic ranking — top results are not the same as a representative sample. If you export results, you're getting the "best match" results, not a random sample. **This biases the statistics upward** in favor of cases the platform thinks are similar to your search terms.

**Search discipline to avoid bias:**
- If the platform lets you export all matches (not just top-10), do that.
- If exporting by outcome separately (all "procedent" cases, then all "improcedent"), make sure you're dividing into the same denominator pool.
- Small sample warning: if your query returns <20 decisions on the merits over the past 3 years, flag that the statistics are unreliable. (Rule of thumb: n < 30 = caution; n < 10 = nearly meaningless.)

---

### Step 4: Intake the results — when you paste the data back

When the user returns with search results (pasted, exported, or linked), ask:

> **What did you get?** (Paste the summary, or tell me the counts: how many decisions, how many for plaintiff, how many for defendant, how many reversed on appeal, what's the date range, what tribunal, what chamber if available.)

Then I'll interpret:

**A. Calculate the base rate**

```
Taxa de procedência = (Decisões de procedência / Decisões no mérito) × 100
```

Compare to your threshold. Example:
- "You got 45 decisões no mérito. 24 procedent for plaintiff, 21 improcedent. That's 53% procedência for plaintiffs — just above the swing point. For you as plaintiff, that's moderate risk: slightly favorable odds, but you're in a coin-flip zone where settlement looks attractive to risk-averse clients."
- "You got 37 decisions. 8 procedent, 29 improcedent. That's 22% procedência — very adverse. If you're the plaintiff, this thesis is uphill. If you're defending, you're in a strong position."

**B. Flag statistical artifacts and caveats**

- **Sample size.** If n < 20, note: "This is a small sample — statistical noise is high. Every case moves the rate by ~5%. Treat as a directional flag, not a precise estimate."
- **Selection bias.** "This search returned the top-matching cases from JusBrasil. That's not a random sample of all cases in the category — the platform ranked them by similarity to your search, which biases toward high-profile or frequently-cited cases. True procedência rate may be different."
- **Dismissal vs. merit.** "Your sample includes [N] cases dismissed on procedure (failure to state a claim, etc.). Those don't count toward procedência on the merits — I've excluded them. If you want to include them, that changes the base rate to [X]%."
- **Partial success.** "The search returned [N] cases with partial procedência — plaintiff won on some claims, lost on others. I counted those as 'procedent.' If you want to weight partial wins at 50%, the rate drops to [Y]%."

**C. Faixa de condenação (if the search included award amounts)**

Extract:
- **Minimum award** (among cases where condenação is quantified)
- **Median** (50th percentile)
- **Maximum** (outlier cap, or 95th percentile to exclude the extreme tail)
- **Standard deviation or IQR** (to note how spread-out the awards are)

Flag:
- "Half the cases awarded between R$ [X] and R$ [Y]. That's the 'typical' range for your thesis in this tribunal."
- "Awards are highly variable — IQR spans [X]–[Y], but outliers go up to [Z]. Suggests the judge / chamber has discretion on quantum; outcome depends on case-specific factors."
- "Inflation adjustment:** Older decisions may not be inflation-adjusted. If your sample spans 2015–2024, note that an R$ 100K award in 2015 is worth ~R$ 200K+ today in real terms. Did JusBrasil / Escavador adjust for inflation, or are these nominal values?"

**D. Tempo médio de tramitação**

Calculate:
- **Median case duration** (from filing to judgment)
- **95th percentile** (the slow-moving outliers)
- **Any outlier notes:** Cases that took 8+ years suggest that some subset gets stuck in appeal or procedural loops

Flag:
- "Half your cases resolved in [X] months (median). 95% resolved within [Y] months. Expect a typical case in this forum to take ~[X] months."
- "Note: this includes only decided cases. Many cases settle before judgment and don't appear in this data. True 'time to resolution' (including settlements) is probably shorter."

**E. Relator / câmara tendencies (if searchable)**

If the user searched by relator or chamber and got case counts:

| Relator / Chamber | Procedent cases | Total cases | Rate | Sample size |
|---|---|---|---|---|
| Relator A | 8 | 12 | 67% | Small (n=12) |
| Relator B | 3 | 15 | 20% | Moderate (n=15) |
| Chamber 1 | 22 | 35 | 63% | Adequate (n=35) |

Flag:
- "Relator A has a 67% procedência rate on your thesis type — favorable. But that's based on n=12, so a few reversals at TJ would change it."
- "Relator B is 20% — very adverse. If you can avoid this relator (rare; random assignment), you'd want to."
- "Chamber tendencies matter more than individual judges in appellate review. Chamber 1 is 63% procedent — note that on appeal, cases are reversed ~[X]% of the time, so even a Chamber 1 victory isn't final."

**F. Reversal / appeal rate (if available)**

If the sample includes appellate decisions on cases that went to trial:

- (Cases reversed at TJ / Cases appealed from trial) = reversal rate
- Flag: "Of [N] cases appealed, [M] were reversed at the Tribunal. That's [X]% reversal — moderately high. Victory at trial is not the same as victory at appeal. Settlement before appeal looks attractive here."

---

### Step 5: Advise — frame the output for decision-making

Close with a **summary readout calibrated to the user's role and risk appetite:**

**If plaintiff's thesis (author):**

> **Você é autor nessa tese.**
>
> Jurimetria diz: [X]% de taxa de procedência em [tribunal] nos últimos [Y] anos para ações como a sua. Seus concorrentes (outros autores em teses similares) ganham [X]% das vezes.
>
> **Risco vs. Reward:**
> - Taxa >70% = seu risco é baixo. Litigar é atrativo; acordo deve ser gen generoso para valer a pena aceitar.
> - Taxa 40–70% = risco moderado. Litigar é 50/50; acordo justo no meio da faixa estimada reduz incerteza.
> - Taxa <40% = risco alto. Você provavelmente perde. Acordo agressivo é mais atrativo que jogo.
>
> Faixa de condenação estimada: R$ [X] a R$ [Y] (mediana [Z]). Se você vai pedir R$ [amount], saiba que fica [acima / no meio / abaixo] da faixa histórica.

**If defendant's thesis (réu):**

> **Você é réu nessa tese.**
>
> Jurimetria diz: [X]% dos autores ganham em teses como essa em [tribunal]. Dito de outro jeito: você tem [100–X]% de chance de ganhar (improcedência).
>
> **Risco vs. Reward:**
> - Chance de ganhar >70% = você está em posição forte. Negocie um acordo mais conservador (mais baixo).
> - Chance de ganhar 40–70% = risco moderado nos dois lados. Um acordo no meio da faixa de condenação estimada divide o risco.
> - Chance de ganhar <40% = você provavelmente perde. Acordo agressivo (perto do máximo) mitiga a exposição de ir a julgamento.
>
> Faixa de exposição estimada (condenações típicas): R$ [X] a R$ [Y] (mediana [Z]). Se o autor pedir R$ [amount], saiba que fica [acima / no meio / abaixo] do que a jurisprudência sugere.

---

### Step 6: Caveats — what jurimetry can't tell you

**No silent supplement.** If a research result is thin, thin, or the search returned data you can't interpret, stop and say so:

> A busca retornou poucos resultados ([N] decisões). Com n < 20, a taxa de procedência é estatisticamente ruidosa — cada caso muda a taxa por ~5%. Não recomendo usar isso para pricing sem (a) uma amostra maior de um período mais longo, ou (b) apoio em jurisprudência conhecida (STJ / TJ súmulas).

> Os dados retornados não incluem informação de quando cada caso foi resolvido. Sem saber se é 2015 vs. 2024, eu não consigo detectar mudanças jurisprudenciais — essa taxa pode ter sido 80% em 2015 e 40% em 2024.

> JusBrasil retornou só os top 10 resultados. Isso não é uma amostra representativa — é os casos que o algoritmo acha mais similares ao seu. Se exportar todos os resultados, posso calcular a taxa real. Quer tentar?

---

## Consequential-action gate

Jurimetria **informa** decisões sobre preço de acordo, avaliação de risco, e estimativa de reserva. Ela não **faz** essas decisões.

A saída desta skill é: "Aqui está o que a jurisprudência diz que casos como seu ganham / perdem com tal frequência e por tal faixa de valor."

A decisão de aceitar um acordo, calipar uma sentença condicional de risco, ou mover um valor de reserva é do advogado + cliente (ou do CFO se a empresa é in-house e há uma política de reserve).

Se o usuário disser "Eu acreditei na sua taxa de procedência 45% e fiz um acordo por R$ 500K" e depois perdeu em julgamento por condenação de R$ 5M, a jurimetria era uma ferramenta — não uma previsão. O advogado assumiu um risco calculado com informação imperfeita. Jurimetria melhora a qualidade da informação, não elimina o risco.

---

## What this skill does not do

- **Não acessa DataJud / JusBrasil.** Você acessa; essa skill interpreta os números que você cola de volta.
- **Não conclui sobre caso específico.** Jurimetria é sobre histórico agregado. Seu caso pode ser um outlier — fatos únicos, juiz com viés peculiar, ou uma tese que o tribunal nunca viu antes.
- **Não inventa estatísticas.** Se a busca retorna números escassos, flaggo. Se o resultado é ambíguo, peço clarificação. Não extrapolou do "esperado."
- **Não é previsão.** É "aqui está o que acontecia nos últimos [N] anos." O futuro pode divergir (jurisprudência muda, tribunal muda, legislação muda, seu juiz é incomum).
- **Não substitui advogado experiente.** Um advogado que conhece pessoalmente o tribunal, o juiz, a câmara, e a história de um relator tem informação melhor que jurimetria agregada. Use os dois — advogado afinado + números agregados = melhor risco calipar.
- **Não calibra quantum punitivo ou honorários.** Faixa de condenação é danos (compensatórios + morais + lucros cessantes conforme o caso). Honorários advocatícios são uma linha separada (geralmente 10–20% da condenação, CPC art. 85) — não incluo isso na faixa. Não incluo custas e despesas. Não incluo multas ou indenizações punitivas específicas de um estatuto (p. ex., multa por infração ao CDC). [model knowledge — verify]

---

## Relationship to other skills

- `litigation-legal:matter-intake` — jurimetria é um input a matter intake. Quando você cria uma matéria, jurimetria ajuda a calibrar a "case value" e o "settlement threshold" no `matter.md`.
- `litigation-legal:claim-chart` — once you've mapped your elements via claim-chart, jurimetria tells you: "Em [tribunal], as pessoas que provam [elemento] ganham com tal frequência."
- `litigation-legal:demand-draft` — jurimetria informa o preço de abertura de uma demand letter.
- `litigation-legal:reserve-memo` — jurimetria informa o intervalo de estimação para uma reserve (ASC 450 in-house, ou exposure assessment for defense counsel).

---

## Next steps decision tree

**What next? Pick one and I'll help you build it out:**

1. **Run the research.** You hand me the raw data (counts by outcome, faixa de condenação, timing, relator data), and I'll calculate and interpret the statistics with caveats for sample size, bias, and uncertainty.
2. **Refine the search.** We iteratively narrow the query (different court, different time period, different aspect of the thesis) until you get a sample size and specificity you trust.
3. **Escalate to outside counsel.** You want an expert in the tribunal (someone who litigates there regularly and knows the judges) to sense-check the jurimetry and add anecdotal "this judge is really [X]" flavor.
4. **Map to pricing / settlement.** I'll help draft a settlement recommendation (or a reserve memo if in-house) using these numbers as a framework — "Here's the range, here's the reasoning."
5. **Something else** — tell me what you'd do with this.

---

*Last updated: [DATE]*
