---
name: legal-research-joaoguirunas
title: Legal Research — fonte primária, artigo e data, ou não é achado
description: Método de pesquisa jurídica com fonte primária — hierarquia de fontes, citação padrão com artigo e data de consulta, conferência de vigência, separação entre achado, leitura e recomendação, regra 'não é parecer' e biblioteca viva de fontes. Use ao levantar base legal para cláusula, postura, obrigação ou disputa e ao validar afirmação jurídica antes de entrar em minuta ou notificação.
author: joaoguirunas
author_url: https://github.com/joaoguirunas/team-os/tree/main/.claude/skills/legal-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Legal Research — fonte primária, artigo e data, ou não é achado

Afirmação jurídica sem fonte é opinião com aparência de lei. Blog resume, resumo distorce, lei muda. Esta skill existe para que **tudo o que a squad afirma sobre direito tenha uma fonte primária localizável, com artigo ou número e data** — e para que quem lê saiba o que a fonte diz, o que a pesquisadora leu nela e o que ninguém aqui recomenda, porque recomendação é da strategist e parecer é do advogado inscrito da empresa.

## 1. Princípios

1. **Fonte primária ou nada.** Lei com artigo/inciso; acórdão com tribunal, número e data de julgamento; doutrina com autor, obra e ano. Fonte secundária (blog, resumo, notícia, resposta de IA) é pista para achar a primária — nunca entra como fonte.
2. **Toda fonte tem data de consulta e vigência conferida.** Lei revogada é histórico, não base. Fonte com mais de 12 meses ou norma alterada desde a consulta → reconsultar e datar de novo.
3. **Achado ≠ leitura ≠ recomendação.** Achado é o que a fonte diz. Leitura é interpretação, marcada como tal. Recomendação não existe neste artefato.
4. **Isto não é parecer.** Todo research termina com a frase. O advogado inscrito da empresa valida antes de qualquer decisão.
5. **Lacuna declarada vale mais que resposta inventada.** O que não foi encontrado sai como `[A LEVANTAR: pergunta exata]`.
6. **Método independente de país.** Hierarquia e citação valem em qualquer jurisdição declarada em `legal-context.md`; onde buscar no Brasil está em `reference/fontes-brasil.md`.

## 2. Hierarquia de fontes

| Nível | Fonte | Peso | Quando usar |
|---|---|---|---|
| 1 | Constituição | máximo | direitos fundamentais, competência, limite a qualquer norma abaixo |
| 2 | Lei (complementar, ordinária, código) | vinculante | regra geral da relação: contrato, dados, trabalho, consumidor |
| 3 | Decreto e regulamento | vinculante, dentro da lei | detalhe operacional: prazos, procedimentos, órgão competente |
| 4 | Norma de agência/regulador | vinculante no setor | obrigações regulatórias, sanções, formulários |
| 5 | Jurisprudência (súmula, repetitivo, acórdão) | orienta; vincula quando a própria fonte diz | como o tribunal aplica a regra; risco em disputa |
| 6 | Doutrina | argumentativa | conceito e interpretação quando a lei é aberta |
| — | Blog, resumo, IA, notícia | zero | só pista para achar o nível 1–6 |

Conflito entre níveis: superior prevalece; especial sobre geral no mesmo nível; posterior sobre anterior — e a leitura desse conflito é marcada como **leitura**, não como achado.

## 3. Citação padrão

```
Lei:            {Lei/Decreto/Código} nº {número}/{ano}, art. {N}, {§ | inciso | alínea} — consultado em {AAAA-MM-DD} em {fonte oficial} — vigência: {vigente | alterado por … | revogado por …}
Jurisprudência: {Tribunal}, {classe} {número}, {órgão julgador}, j. {AAAA-MM-DD}, pub. {AAAA-MM-DD} — {vinculante | orientativo | superado}
Regulador:      {Órgão}, {tipo de ato} nº {número}/{ano}, art. {N} — consultado em {data} — vigência
Doutrina:       {Autor}, {Obra}, {edição}, {editora}, {ano}, p. {N}
Interno:        {tipo de documento} · {contraparte por alias} · cláusula {N} · {data de assinatura} · {#K do registro}
```

Sem um destes campos a fonte fica `[FONTE INCOMPLETA]` e o achado não entra em cláusula, postura ou notificação. Nunca transcrever o artigo: citar o número, resumir o comando em uma frase e mandar conferir na fonte.

## 4. Vigência e alterações

| Situação | O que fazer |
|---|---|
| Norma consultada há > 12 meses | reconsultar, datar de novo, registrar se mudou |
| Norma com alteração posterior | citar a redação vigente e a norma alteradora, com data da mudança |
| Norma revogada | mover para "histórico" no research; nunca base de cláusula nova |
| Norma em vacatio legis | citar data de entrada em vigor; marcar `[VIGÊNCIA FUTURA]` |
| Jurisprudência superada (nova súmula, overruling) | marcar `[SUPERADA em {data}]` e citar a decisão que superou |
| Divergência entre tribunais | registrar as duas linhas com número; a escolha entre elas é leitura |

## 5. Achado, leitura e recomendação

| Camada | Marca no texto | Quem produz | Exemplo |
|---|---|---|---|
| Achado | `[ACHADO]` + citação §3 | VERITAS | "Art. N da Lei X exige comunicação ao regulador em prazo definido (conferir na fonte)." |
| Leitura | `[LEITURA]` + achados que sustentam | VERITAS, marcada | "Lido com o art. M, o prazo parece contar do conhecimento, não do evento." |
| Recomendação | não existe aqui | PRUDENTIA (postura) · advogado (parecer) | — |

Pergunta do usuário do tipo "o que eu faço?" → responder com achados e leituras e encaminhar a PRUDENTIA. Proibido no research: "recomendo", "deve", "é seguro", "pode assinar".

## 6. Método

```
1. Pergunta fechada       → "Que norma rege X na relação Y?" — nunca "pesquisar sobre X"
2. Hipóteses de fonte     → níveis §2 prováveis; onde buscar (reference/fontes-brasil.md ou equivalente da jurisdição)
3. Coleta                 → fonte primária, citação completa §3, vigência §4
4. Achados                → um por linha, citação ao lado
5. Leituras               → marcadas, separadas dos achados
6. Precedentes internos   → o que a empresa já assinou/negociou sobre o tema (§7)
7. Lacunas                → [A LEVANTAR: …] com a pergunta pronta para o advogado ou para nova busca
8. Fecho                  → "Isto não é parecer; o advogado inscrito da empresa valida."
```

`/deep-research` para a varredura; `/dev-defuddle` para extrair texto limpo de páginas oficiais. Tempo esgotado sem fonte primária → lacuna, não resposta.

## 7. Precedentes internos

`agents/research/precedentes-internos.md`: por tema, o que a empresa já assinou ou negociou — tipo de documento, contraparte **por alias**, cláusula, o que foi cedido ou mantido, `#K` do registro de FIDES quando existir. Nunca CPF/CNPJ completo, endereço residencial, dado de saúde ou credencial — alias sempre. Precedente interno mostra prática, não licitude: não substitui fonte legal.

## 8. Biblioteca de fontes

`agents/research/fontes.md` — nota viva, uma linha por fonte: tema · citação §3 · link oficial · data de consulta · vigência · research que a usou. Fonte usada em duas pesquisas entra uma vez e é referenciada. Revisão trimestral: reconsultar tudo com > 12 meses.

## 9. Checklist antes de entregar

| # | Verificação | Como |
|---|---|---|
| 1 | Toda afirmação tem citação completa §3 | `[ACHADO]` sem "art." ou sem número → falha |
| 2 | Toda fonte tem data de consulta ≤ 12 meses | coluna data |
| 3 | Vigência conferida e escrita | coluna vigência vazia → falha |
| 4 | Leitura marcada `[LEITURA]`, separada dos achados | leitura das seções |
| 5 | Zero "recomendo", "deve", "é seguro", "pode assinar" | grep |
| 6 | Lacunas com pergunta pronta | seção `[A LEVANTAR]` |
| 7 | Frase "Isto não é parecer" presente | grep |
| 8 | Zero dado sensível de terceiro | leitura; alias em todo nome |

## 10. Templates e referência

- `templates/legal-research.md` — pergunta, fontes, achados, leituras, precedentes internos, lacunas, fecho "não é parecer"
- `reference/fontes-brasil.md` — onde buscar no Brasil e o que cada fonte oferece; regra "conferir vigência na data"

## 11. Contrato com o resto da squad

- **Produz:** VERITAS (legal-analyst) — research por tema, `fontes.md`, `precedentes-internos.md`.
- **Consome:** PRUDENTIA lê o research inteiro antes de escrever ou aprovar postura; CONCORDIA cita a base legal na matriz de desvios (coluna `origem` = citação §3); FIDES cadastra obrigação regulatória e prazo de titular só com fonte daqui; CLEMENTIA usa prazo prescricional só com citação §3; LEX abre story de minuta só depois do research da relação.
- **Cruza:** IUSTITIA confere que toda cláusula com base legal aponta para citação completa e vigente — research sem `[ACHADO]` datado = NÃO VERIFICÁVEL.
