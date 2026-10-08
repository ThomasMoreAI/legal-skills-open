---
name: matriz-aderencia-tese-sbroggioadv
title: MATRIZ-ADERENCIA-TESE — Julgamento sobre dado real, nunca sobre memória
description: 'MATRIZ-ADERENCIA-TESE — Camada C4 do prisma-julgador-os. Julgamento LLM sobre dado real: cruza a tese da peça com os precedentes que a varredura-jurisprudencial-orgao validou por fetch e monta a matriz de aderência — formulação da tese × o órgão já acolheu? (✅ com precedente citado) × já rejeitou? (com o fundamento da rejeição) × sem dado (declarado como sem dado, nunca extrapolado). Regra dura: célula sem precedente coletado = "sem dado do órgão" — proibido completar com tendência geral do tribunal sem rotular que veio do agregado, não do órgão. Nunca emite número/percentual (território do perfil-estatistico-orgao, com n + IC). Aciona: "matriz de aderência", "minha tese cola nesse órgão?", "o órgão aceita essa tese?", "cruza a tese com os precedentes", "essa câmara acolhe esse argumento?", ou automaticamente no pipeline /prisma após a varredura.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/prisma-julgador-os-marketplace/tree/main/prisma-julgador-os/skills/matriz-aderencia-tese
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# MATRIZ-ADERENCIA-TESE — Julgamento sobre dado real, nunca sobre memória

## 1. Papel na cadeia (C4 — Estratégia)

Primeira camada de **julgamento** do pipeline: nada aqui coleta dado novo. Cruza a(s) tese(s) da
peça com o corpus que a `varredura-jurisprudencial-orgao` validou por fetch e responde, célula a
célula: o que este órgão **já acolheu**, o que **já rejeitou** (e com qual fundamento) e onde
**não há dado** — declarado, nunca disfarçado.

> **TRAVA R2 APLICADA** (`context/travas-prisma.md`): esta skill não busca, não valida e não
> completa de memória. **Precedente que não está no corpus da varredura não existe.** Corpus
> vazio ou raso → matriz rasa e declarada. Matriz rasa honesta vale mais que matriz cheia
> inventada — é essa a proposta de valor do produto.

## 2. Entradas

- **Tese(s) da peça** — do usuário ou extraídas da peça e confirmadas com ele, 1-2 frases cada.
- **Corpus validado da varredura** — só ✅ (⚠️ entra rotulado PARCIAL, com aviso de conferência;
  🔴 e não verificados nunca entram).
- Opcional: o perfil do `perfil-estatistico-orgao` (n + IC) — apenas como **contexto citado**,
  nunca recalculado nem convertido em juízo numérico aqui.
- O rótulo da identificação (SUGERIDO/CONFIRMADO — trava R4) acompanha tudo.

## 3. A matriz (saída central)

| Formulação da tese | O órgão já acolheu? | Já rejeitou? | Sem dado |
|---|---|---|---|
| [tese como está na peça] | ✅ [precedente citado: nº + fundamento que o órgão usou] | [precedente: nº + FUNDAMENTO da rejeição] | — |
| [formulação alternativa encontrada no corpus] | ✅ [...] | — | — |
| [desdobramento sem precedente no corpus] | — | — | **SEM DADO DO ÓRGÃO** (declarado) |

### Regras de preenchimento (duras)

1. Célula "acolheu" só com precedente do corpus — **sempre citado** (nº do processo + data). Sem
   citação, a célula não existe.
2. Célula "rejeitou" exige o **fundamento da rejeição** extraído pela varredura. Se a ementa
   validada só mostra o resultado: *"rejeitou — fundamento não aferível pela ementa (inteiro teor
   não coletado)"*. Nunca deduzir o fundamento.
3. **REGRA DURA — célula sem precedente coletado = "sem dado do órgão".** É PROIBIDO completar
   com "tendência geral do tribunal", "jurisprudência dominante", "entendimento pacífico" ou
   memória do modelo. Se existir dado agregado (perfil estatístico desta vertical ou panorama do
   `jurimetria-os`), ele **pode** aparecer ao lado — **sempre rotulado**:
   *"contexto do AGREGADO (tribunal/classe), NÃO do órgão"*. A célula do órgão continua
   "sem dado". O leitor nunca confunde de onde veio cada afirmação.
4. **A matriz nunca vira número.** Nada de "chance de êxito", "acolhe em X% dos casos", score ou
   nota. Número/percentual é território exclusivo do `perfil-estatistico-orgao` — e lá só sai com
   `n` + IC (trava R1). A matriz fala em **precedente e fundamento**, não em probabilidade.

## 4. Leitura estratégica (abaixo da matriz)

Para cada tese, 3-5 linhas de julgamento explícito **sobre o dado**:

- Onde a formulação atual colide com o fundamento que o órgão já usou para rejeitar.
- Qual formulação alternativa o próprio órgão já acolheu — com o precedente que prova.
- O que é lacuna honesta: *"o corpus não mostra este órgão enfrentando essa tese"* (e o que isso
  significa: não é sinal verde nem vermelho, é ausência de dado).

Todo juízo aponta o precedente do corpus que o sustenta. Observação sem lastro no corpus sai
rotulada **"hipótese sem lastro no corpus"** — nunca em tom de padrão do órgão.

## 5. Saída final

```markdown
## Matriz de aderência — [tese(s)] × [órgão · rótulo SUGERIDO ou CONFIRMADO]
**Corpus:** [N] precedentes validados (varredura de [DD/MM/AAAA]) · **Composição verificada
em:** [data — trava R5; composição muda: padrão passado ≠ composição futura]

[matriz — §3]
[leitura estratégica — §4]

➡️ Próximo passo: `reescrita-orientada-peca` aplica esta matriz à peça (sem tocar o mérito — R6).
⚠️ A matriz mostra aderência ao padrão público do órgão; não prevê nem garante resultado.
```

## Travas desta skill

- **R2 (núcleo):** só cita o corpus da varredura; célula vazia é "sem dado do órgão", nunca
  completada por memória ou agregado sem rótulo.
- **R1 (fronteira):** não emite número/percentual — quem quantifica é o
  `perfil-estatistico-orgao`, com `n` + IC.
- **R3:** linguagem de padrão público do órgão no exercício da função; a matriz mostra aderência,
  nunca promete resultado.
- **R4:** o rótulo SUGERIDA da identificação acompanha a matriz até o usuário confirmar.
- **R5:** repete a data de verificação da composição + aviso de que composição muda e a
  distribuição pode redistribuir.
- **R7:** se o cruzamento exigir dado de autos sob segredo de justiça (art. 189 CPC), declara o
  limite e para — a análise segue apenas sobre o padrão público.

**Cross-links:** consome a `varredura-jurisprudencial-orgao` (o corpus) e o
`perfil-estatistico-orgao` (contexto rotulado) · alimenta a `reescrita-orientada-peca` e as 3
vozes (`voz-do-magistrado` · `voz-da-parte-contraria` · `suprema-corte-prisma`) · o
`relatorio-de-risco` consolida · integridade/autenticidade do documento →
`blindagem-peticao-os` (fronteira: o prisma avalia se a tese convence sob a ótica de quem julga;
a blindagem audita se o documento é íntegro — nunca duplicar).
