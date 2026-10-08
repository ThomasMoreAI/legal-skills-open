---
name: tese-juridica-validator-ma-serra
title: Tese Jurídica Validator — Análise de Solidez Argumentativa
description: 'Validador de argumentos e teses jurídicas contra a jurisprudência consolidada dos Tribunais Superiores brasileiros (STF, STJ) e tribunais estaduais. Analisa a solidez de um argumento jurídico em 5 dimensões: (1) compatibilidade com teses vinculantes e repetitivas do STF/STJ, (2) aderência ao texto normativo aplicável, (3) coerência lógico-jurídica interna, (4) probabilidade de êxito com base em precedentes, e (5) vulnerabilidades que o adversário pode explorar. Especializado em Direito Civil, Processual Civil, Consumidor, Bancário e Constitucional. Usar SEMPRE que o usuário quiser validar um argumento antes de usá-lo em petição ou sentença, precisar saber se sua tese jurídica tem respaldo nos Tribunais Superiores, quiser identificar pontos fracos de um argumento, precisar comparar teses conflitantes, ou mencionar: "minha tese é", "esse argumento procede", "tenho razão juridicamente", "pode usar esse argumento", "STJ entende assim", "validar argumento", "checar jurisprudência",
  "tese sólida", "fundamento jurídico". Previne erros de argumentação que custam processos.'
author: ma-serra
author_url: https://github.com/ma-serra/lex-intelligentia-skills/tree/main/skills/core/tese-juridica-validator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Tese Jurídica Validator — Análise de Solidez Argumentativa

## Protocolo de Validação em 5 Dimensões

Toda tese submetida é analisada nesta sequência:

```
DIMENSÃO 1 → VALIDADE NORMATIVA
              A tese está ancorada em norma vigente?

DIMENSÃO 2 → CONSISTÊNCIA JURISPRUDENCIAL  
              Os tribunais acolhem ou rejeitam este argumento?

DIMENSÃO 3 → COERÊNCIA INTERNA
              O argumento é logicamente válido e não se contradiz?

DIMENSÃO 4 → PROBABILIDADE DE ÊXITO
              Qual o percentual estimado de acolhimento em 1ª e 2ª instâncias?

DIMENSÃO 5 → VULNERABILIDADES
              Como a parte adversa vai atacar esta tese?
```

---

## DIMENSÃO 1 — Validade Normativa

### Hierarquia de Normas (Kelsen aplicado ao BR)

```
CF/1988 (topo — vincula tudo)
    ↓
Emendas Constitucionais
    ↓
Tratados Internacionais de DH (art. 5º, §2° e 3°)
    ↓
Lei Complementar
    ↓
Lei Ordinária / Lei Delegada / Medida Provisória
    ↓
Decreto / Regulamento
    ↓
Atos normativos infralegais (Portarias, Resoluções, Circulares)
```

**Checklist de validade normativa:**
- [ ] A norma invocada está em vigor na data do fato?
- [ ] Há emenda constitucional, MP ou lei posterior que a revogou?
- [ ] A norma inferior é compatível com a superior?
- [ ] A norma especial prevalece sobre a geral (lex specialis)?
- [ ] A norma posterior revogou a anterior (lex posterior)?

**Perguntas a fazer sobre a tese:**
```
1. "Qual é a base normativa desta afirmação?" [citar artigo + lei]
2. "Esta norma foi alterada nos últimos anos?" [verificar]
3. "Há norma especial que afasta a aplicação desta?" [verificar]
```

---

## DIMENSÃO 2 — Consistência Jurisprudencial

### Base de Conhecimento de Teses Consolidadas por Área

> ⚠️ PROTOCOLO ANTI-ALUCINAÇÃO: as teses abaixo são sínteses de posições 
> consolidadas. Antes de citar em peça ou sentença, SEMPRE verificar no 
> site do tribunal para confirmar o número exato e a redação atual.

#### DIREITO DO CONSUMIDOR — CDC

| Tese | Status STJ | Observação |
|------|-----------|------------|
| Responsabilidade objetiva do fornecedor por vício do produto | CONSOLIDADA | Art. 12/18 CDC; inúmeros julgados |
| Inversão do ônus da prova como regra (art. 6°, VIII, CDC) | CONSOLIDADA | Depende de verossimilhança ou hipossuficiência |
| Dano moral pela simples negativação indevida | CONSOLIDADA | Súmula 385 STJ: exclui se houver outro apontamento legítimo concomitante |
| Solidariedade de toda a cadeia de fornecimento | CONSOLIDADA | Arts. 7°, 18 e 25, CDC |
| Prazo prescricional: 5 anos para pretensões do consumidor | CONSOLIDADA | Art. 27, CDC |
| Plano de saúde não pode negar tratamento prescrito por médico | CONSOLIDADA | Inúmeras súmulas e temas do STJ |
| Abusividade de cláusula que exclui cobertura de doença preexistente após 2 anos | CONSOLIDADA | Tema STJ 952 [VERIFICAR NÚMERO] |

#### DIREITO BANCÁRIO

| Tese | Status STJ | Observação |
|------|-----------|------------|
| Capitalização mensal é lícita se expressamente pactuada | CONSOLIDADA | Súmula 541, STJ |
| Tarifas bancárias vedadas após 2011 (TAC, TEC) | CONSOLIDADA | Res. CMN 3.919/2010; Tema 958 STJ |
| Juros acima de 12% ao ano: lícitos em bancos | CONSOLIDADA | Súmula 596, STF; Súmula 539, STJ |
| Banco responde por fraude de terceiro em conta corrente | CONSOLIDADA | Teoria do risco do negócio (art. 927, CC) |
| Inscrição indevida no SPC/Serasa gera dano moral in re ipsa | CONSOLIDADA | Súmula 385 STJ — exceto se houver anotação legítima |
| Comissão de permanência não cumulável com outras verbas | CONSOLIDADA | Súmula 472, STJ |

#### DIREITO PROCESSUAL CIVIL (CPC/2015)

| Tese | Status STJ/STF | Observação |
|------|---------------|------------|
| Tutela antecipada requer fumus + periculum + reversibilidade | CONSOLIDADA | Art. 300, CPC |
| Fundamentação analítica obrigatória (art. 489, §1°, CPC) | CONSOLIDADA | Decisão genérica = nula |
| Negócio jurídico processual é válido (art. 190, CPC) | CONSOLIDADA | Desde que não vulnere garantias processuais |
| Pedido de reconsideração não interrompe prazo recursal | CONSOLIDADA | Súmula 581, STJ |
| Honorários advocatícios: fase de liquidação e execução | CONSOLIDADA | Art. 85, §§, CPC; Tema [VERIFICAR] STJ |
| Ônus da prova: regras do art. 373, CPC | CONSOLIDADA | Dinâmica do ônus em casos específicos |

#### RESPONSABILIDADE CIVIL

| Tese | Status | Observação |
|------|--------|------------|
| Teoria da perda de uma chance: ressarcível como dano autônomo | CONSOLIDADA | REsp 1.190.180 [VERIFICAR] |
| Dano moral coletivo é cabível sem lesão individual | CONSOLIDADA | Inúmeros REsp [VERIFICAR números] |
| Nexo causal: teoria da causalidade adequada | CONSOLIDADA | Excludentes: culpa exclusiva da vítima, fato de terceiro, fortuito |
| Responsabilidade dos pais por ato dos filhos menores | CONSOLIDADA | Art. 932, I, CC — objetiva |
| Dano estético e dano moral: cumuláveis | CONSOLIDADA | Súmula 387, STJ |

---

## DIMENSÃO 3 — Coerência Interna

### Mapeamento de Vícios Lógico-Jurídicos Comuns

```
VÍCIO 1 — PETIÇÃO DE PRINCÍPIO (tautologia)
Exemplo: "O réu deve indenizar pois causou dano ao autor, logo deve indenizar."
Correção: Demonstrar o nexo causal com fatos e provas específicas.

VÍCIO 2 — GENERALIZAÇÃO INDEVIDA
Exemplo: "Todo banco cobra juros abusivos, portanto o réu também cobra."
Correção: Provar especificamente a abusividade neste contrato.

VÍCIO 3 — ARGUMENTUM AD VERECUNDIAM SEM SUBSTÂNCIA
Exemplo: "Segundo a melhor doutrina, deve-se acolher o pedido."
Correção: Citar a doutrina específica com a tese que sustenta.

VÍCIO 4 — ARGUMENTO CIRCULAR
Exemplo: "A cláusula é nula porque é abusiva. É abusiva porque é nula."
Correção: Identificar o critério objetivo de abusividade (art. 51, CDC ou art. 421, CC).

VÍCIO 5 — FALSIDADE NA PREMISSA
Exemplo: Citar Súmula que foi cancelada ou superada pelo STJ.
Correção: Verificar status atual da súmula.

VÍCIO 6 — NON SEQUITUR (conclusão não decorre das premissas)
Exemplo: "O produto tinha defeito, portanto o vendedor deve ser preso."
Correção: A consequência jurídica deve decorrer logicamente da norma e do fato.
```

### Checklist de Coerência

- [ ] As premissas fáticas são sustentadas pelas provas dos autos?
- [ ] As premissas jurídicas são baseadas em normas vigentes?
- [ ] A conclusão decorre necessariamente das premissas?
- [ ] Há contradição interna entre argumentos da mesma peça?
- [ ] A tese é consistente com outras alegações do mesmo processo?

---

## DIMENSÃO 4 — Probabilidade de Êxito

### Matriz de Avaliação

```
FATORES QUE AUMENTAM A PROBABILIDADE:
✅ Há súmula vinculante do STF → quase certeza
✅ Há tese repetitiva do STJ → muito alta (>80%)
✅ Há precedentes do TJ local convergentes → alta (>60%)
✅ A prova é sólida e o direito é claro → alta
✅ O juiz da causa tem histórico favorável em casos similares → aumenta
✅ O caso se encaixa perfeitamente na jurisprudência → alta

FATORES QUE REDUZEM A PROBABILIDADE:
❌ Jurisprudência contrária no tribunal local → baixa a muito baixa
❌ Tema com divergência entre câmaras do TJ → incerta
❌ Prova frágil mesmo com direito sólido → média a baixa
❌ Pedido excessivo sem lastro nos precedentes → pode indeferir em parte
❌ Precedente antigo não atualizado → verificar se ainda vale

CLASSIFICAÇÃO DE RISCO:
🟢 SÓLIDA     → 70-95% de êxito estimado | Jurisprudência consolidada
🟡 DEBATÍVEL  → 40-70% de êxito          | Entendimento divergente
🟠 FRÁGIL     → 20-40% de êxito          | Jurisprudência contrária ou prova fraca
🔴 TEMERÁRIA  → <20% de êxito            | Contrária à súmula/tese vinculante
```

---

## DIMENSÃO 5 — Vulnerabilidades da Tese

### Análise de Contra-Argumentos Previsíveis

Para cada tese apresentada, antecipar:

```
ATAQUE 1 — DESCONSTRUÇÃO FÁTICA
"O fato não ocorreu como descrito" → como responder com provas?

ATAQUE 2 — DISTINÇÃO (DISTINGUISHING)
"Esse precedente não se aplica porque o caso é diferente em [X]"
→ Como demonstrar que o caso é análogo?

ATAQUE 3 — OVERRULING (SUPERAÇÃO)
"Esse precedente foi superado pela decisão Y"
→ Verificar se o precedente ainda é atual

ATAQUE 4 — ARGUMENTO NORMATIVO CONTRÁRIO
"Existe norma posterior que revogou essa base legal"
→ Verificar se a norma foi alterada

ATAQUE 5 — EXCEÇÃO APLICÁVEL
"A regra geral não se aplica porque há exceção para este caso"
→ Identificar exceções previstas em lei ou jurisprudência

ATAQUE 6 — PROPORCIONALIDADE
"Mesmo que procedente, o pedido é excessivo"
→ Calibrar o pedido com os precedentes de valor
```

---

## Relatório Padrão de Validação de Tese

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RELATÓRIO DE VALIDAÇÃO DE TESE JURÍDICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TESE ANALISADA:
"[transcrição da tese submetida]"

ÁREA: [área do Direito]
CONTEXTO: [autor/réu/magistrado | fase processual]

─────────────────────────────────────────────────
D1 — VALIDADE NORMATIVA: [✅ SÓLIDA | ⚠️ ATENÇÃO | ❌ PROBLEMA]
Base legal: [artigo + lei]
Vigência: [em vigor / alterada em / verificar]
Observação: [notas relevantes]

─────────────────────────────────────────────────
D2 — CONSISTÊNCIA JURISPRUDENCIAL: [✅ | ⚠️ | ❌]
STF: [posição / sem posição conhecida]
STJ: [posição — indicar se é súmula/tema/precedente / verificar]
TJ local: [tendência / sem dados]
Status: [CONSOLIDADA | DEBATIDA | CONTRÁRIA | EVOLUINDO]
[CONFIRMAR NO TRIBUNAL antes de citar em peça]

─────────────────────────────────────────────────
D3 — COERÊNCIA INTERNA: [✅ | ⚠️ | ❌]
Vícios identificados: [nenhum / lista de vícios]
Sugestão de aperfeiçoamento: [como melhorar]

─────────────────────────────────────────────────
D4 — PROBABILIDADE DE ÊXITO: [🟢 SÓLIDA | 🟡 DEBATÍVEL | 🟠 FRÁGIL | 🔴 TEMERÁRIA]
Estimativa: [%] em 1ª instância | [%] em 2ª instância
Fator decisivo: [o que vai definir o resultado]

─────────────────────────────────────────────────
D5 — PRINCIPAIS VULNERABILIDADES:
⚠ [Vulnerabilidade 1 — como prevenir]
⚠ [Vulnerabilidade 2 — como prevenir]

─────────────────────────────────────────────────
VEREDICTO FINAL:
[✅ TESE SÓLIDA — use com confiança]
[⚠️ TESE DEBATÍVEL — use com cautela e argumento robusto]
[❌ TESE ARRISCADA — considere argumento alternativo]

ARGUMENTO ALTERNATIVO RECOMENDADO (se necessário):
[como reformular a tese para melhor respaldo]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Modo Rápido — Quick Validator

Para validação rápida sem relatório completo, responder:

```
TESE: [tese em análise]

RESULTADO RÁPIDO:
Status: [🟢/🟡/🟠/🔴]
Jurisprudência: [favorável/contrária/divergente] — [nome do precedente se conhecido, senão "verificar"]
Maior risco: [em 1 linha]
Recomendação: [use / reformule / evite]
```
