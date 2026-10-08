---
name: calculadora-processual-ma-serra
title: Calculadora Processual — Tabelas de Referencia para Calculos Judiciais
description: 'Tabelas de referencia para calculos judiciais — juros moratorios e compensatorios, correcao monetaria (IPCA-E, SELIC, INPC), honorarios advocaticios (art. 85 CPC), custas processuais, multas e astreintes. Cada tabela indica formula, indice, termo inicial, fundamentacao e erros comuns. NAO e uma calculadora automatica — e um guia estruturado para o magistrado e gabinete aplicarem a formula correta. Usar quando o usuario precisar consultar indices de correcao, calcular juros, definir honorarios, verificar multas, consultar tabela de custas, calcular astreintes ou fundamentar correcao monetaria em sentenca. Triggers: "juros", "correcao monetaria", "IPCA", "SELIC", "honorarios", "custas", "multa", "astreintes", "calculos judiciais", "liquidacao", "RPV", "precatorio", "art. 85", "art. 523", "art. 537".'
author: ma-serra
author_url: https://github.com/ma-serra/lex-intelligentia-skills/tree/main/skills/core/calculadora-processual
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Calculadora Processual — Tabelas de Referencia para Calculos Judiciais

## Overview

Skill de referencia estruturada para calculos em decisoes judiciais. Contem tabelas com indice correto, termo inicial, formula e fundamentacao legal para cada tipo de calculo. Nao realiza calculos automaticos — fornece ao magistrado e gabinete a informacao necessaria para aplicar a formula correta na sentenca ou decisao.

## When to Use

- Definir juros e correcao monetaria em sentenca
- Fixar honorarios advocaticios
- Consultar tabela de custas
- Fundamentar multas processuais
- Verificar parametros para RPV/Precatorio

**When NOT to Use:**
- Liquidacao complexa com pericia contabil (requer perito)
- Calculos trabalhistas (indices e regras proprios)
- Calculos tributarios (legislacao especifica)

---

## 1. Juros Moratorios

### REGRA PRINCIPAL — Tema 1.368/STJ (a partir de 15/10/2025)

**Tema Repetitivo 1.368/STJ** (REsp 2.199.164/PR e 2.070.882/RS, Min. Villas Boas Cueva, Corte Especial, 15/10/2025; endosso constitucional: STF RE 1.558.191/SP, Min. Andre Mendonca, set/2025):

**SELIC e o indice UNICO para atualizacao de dividas civis.** Substitui a formula anterior (1% a.m. + IPCA-E). Vedacao expressa de cumulacao SELIC + IPCA-E (bis in idem).

### Tabela de Juros por Tipo de Obrigacao (pos-Tema 1.368)

| Tipo | Indice | Termo Inicial | Fundamentacao | Observacao |
|------|--------|---------------|---------------|------------|
| Responsabilidade extracontratual | SELIC | Evento danoso (Sumulas 54+362/STJ convergidas) | Tema 1.368/STJ + Sumula 54/STJ | SELIC unica desde o evento — inclui juros + correcao |
| Responsabilidade contratual | SELIC (ou taxa contratual) | Citacao valida (art. 405, CC) | Tema 1.368/STJ + Art. 405, CC | Se contrato preve taxa propria, aplica-se a contratual ate o limite legal |
| Dano moral | SELIC | Evento danoso | Tema 1.368 (convergencia Sumulas 54+362) | Antes: IPCA-E desde arbitramento. Agora: SELIC desde o evento |
| Alimentos | SELIC | Citacao | Tema 1.368 + Art. 405, CC | Cada parcela vence no dia fixado |
| Repeticao de indebito | SELIC | Cada pagamento indevido | Tema 1.368 + arts. 876 e 405, CC | Sumula 188/STJ mantida quanto ao termo inicial |
| Fazenda Publica (pos-EC 113) | SELIC | 09/12/2021 em diante | Art. 3, EC 113/2021 | Ja era SELIC unica — Tema 1.368 confirma |
| Fazenda Publica (pre-EC 113) | IPCA-E + 1% a.m. ate 09/12/2021 | Citacao (ou evento danoso) | Art. 1-F, Lei 9.494/97 | Periodo anterior: manter formula antiga |

**ATENCAO — Convergencia Sumulas 54 + 362 (N2 — em consolidacao):**
O Tema 1.368 indica SELIC desde o evento danoso para dano moral extracontratual, convergindo Sumula 54 (juros desde o evento) com Sumula 362 (correcao desde o arbitramento) em um unico indice. Consolidacao pelas turmas do STJ ainda em curso — monitorar. [VERIFICAR periodicamente]

### Regra da SELIC como Indice Unico

**SELIC = juros + correcao monetaria.** Quando se aplica SELIC, **NUNCA** cumular com IPCA-E, INPC ou qualquer outro indice de correcao. Fazer isso e bis in idem (Tema 1.368/STJ, expressamente).

---

## 2. Correcao Monetaria

### Tabela de Indices por Contexto (pos-Tema 1.368)

**Regra geral para dividas civis: SELIC unica (Tema 1.368/STJ).** Indices separados (IPCA-E, INPC) permanecem apenas para contextos especificos.

| Contexto | Indice | Termo Inicial | Fundamentacao | Observacao |
|----------|--------|---------------|---------------|------------|
| Dividas civis em geral | SELIC (unica) | Conforme tipo (ver tabela juros) | Tema 1.368/STJ | Regra principal pos-15/10/2025 |
| Dano moral extracontratual | SELIC | Evento danoso | Tema 1.368 (convergencia S.54+S.362) | Antes: IPCA-E desde arbitramento |
| Dano material | SELIC | Desembolso efetivo / vencimento | Tema 1.368 + art. 389, CC | Antes: IPCA-E |
| Repeticao de indebito | SELIC | Cada pagamento indevido | Tema 1.368 + art. 876, CC | Antes: IPCA-E desde desembolso |
| Contratos bancarios | SELIC (ou indice contratual) | Vencimento da obrigacao | Tema 1.368 + contrato | Indice contratual prevalece se valido |
| Fazenda Publica pre-EC 113 | IPCA-E + juros separados | Dano ou citacao | Lei 9.494/97, art. 1-F | Periodo ATE 09/12/2021 |
| Fazenda Publica pos-EC 113 | SELIC (unica) | 09/12/2021 em diante | Art. 3, EC 113/2021 | Ja era SELIC — Tema 1.368 confirma |
| Salarios e beneficios previdenciarios | INPC | Competencia devida | Legislacao previdenciaria | Regime proprio — nao afetado |
| Alugueis | IGP-M ou IPCA | Vencimento | Contrato (Lei 8.245/91) | Indice contratual prevalece |
| Depositos judiciais | SELIC | Deposito | Lei 9.703/98 | Ja era SELIC |

### Template para Sentenca — Bloco Correcao (pos-Tema 1.368)

```
[REGRA GERAL — DIVIDAS CIVIS:]
Atualizacao monetaria pelo indice SELIC, que inclui juros e correcao monetaria
(Tema Repetitivo 1.368/STJ), a contar de [TERMO INICIAL — evento danoso / citacao /
desembolso / arbitramento, conforme o tipo].
Vedada a cumulacao com qualquer outro indice de correcao (IPCA-E, INPC).

[SE FAZENDA PUBLICA — PERIODO DUAL:]
(a) Ate 09/12/2021: correcao pelo IPCA-E + juros de [TAXA] a contar de [TERMO];
(b) A partir de 09/12/2021: SELIC unica (art. 3, EC 113/2021).

[SE CONTRATO COM INDICE PROPRIO:]
Indice contratual de [ESPECIFICAR] ate o vencimento/inadimplemento;
apos, SELIC nos termos do Tema 1.368/STJ.
```

---

## 3. Honorarios Advocaticios

### Art. 85, CPC — Tabela de Parametros

| Situacao | Faixa | Base de Calculo | Dispositivo |
|----------|-------|-----------------|-------------|
| Regra geral | 10% a 20% | Valor da condenacao, proveito economico ou valor da causa | Art. 85, §2, CPC |
| Fazenda Publica | Escalonado (vide §3) | Valor da condenacao ou proveito economico | Art. 85, §3, CPC |
| Causa de valor inestimavel/irrisorio | Equidade | Apreciacao equitativa | Art. 85, §8, CPC |
| Cumprimento de sentenca | 10% | Valor do debito | Art. 523, §1, CPC |
| Recurso improvido | Majoracao | Observar limite total | Art. 85, §11, CPC |
| Sucumbencia reciproca | Proporcional | Exito de cada parte | Art. 86, CPC |

### Escalonamento Fazenda Publica (art. 85, §3)

| Faixa de Valor (em SM) | Percentual |
|-------------------------|------------|
| Ate 200 SM | 10% a 20% |
| 200 a 2.000 SM | 8% a 10% |
| 2.000 a 20.000 SM | 5% a 8% |
| 20.000 a 100.000 SM | 3% a 5% |
| Acima de 100.000 SM | 1% a 3% |

**Regras importantes:**
- Percentuais sao cumulativos por faixa (como IR)
- Vedacao de compensacao (art. 85, §14) — honorarios sao direito autonomo do advogado
- Majoracao em grau recursal limitada ao teto da faixa (art. 85, §11)
- Gratuidade nao isenta de honorarios — suspende exigibilidade por 5 anos (art. 98, §3)

### Criterios de Fixacao (art. 85, §2)

Para definir o percentual dentro da faixa, considerar:
1. Grau de zelo do profissional
2. Lugar de prestacao do servico
3. Natureza e importancia da causa
4. Trabalho realizado e tempo exigido

---

## 4. Multas Processuais

### Tabela de Multas mais Comuns

| Multa | Percentual/Valor | Base | Dispositivo | Quando Aplica |
|-------|-------------------|------|-------------|---------------|
| Nao pagamento voluntario | 10% | Valor do debito | Art. 523, §1, CPC | Cumprimento de sentença — prazo 15 dias |
| Litigancia de ma-fe | Ate 10% | Valor da causa | Art. 81, CPC | Dolo processual comprovado |
| Ato atentatório (execucao) | Ate 20% | Valor atualizado do debito | Art. 774, p.u., CPC | Fraude, resistencia, embaraco |
| Ausencia injustificada (conciliacao) | Ate 2% | Valor da causa | Art. 334, §8, CPC | Nao comparecimento sem justificativa |
| Embargos protetorios | 2% (1a) + ate 10% (reincidencia) | Valor da causa | Art. 1.026, §§2-3, CPC | Embargos manifestamente protetorios |
| Contempt of court | Ate R$ 100.000 | Valor fixo | Art. 77, §2, CPC | Descumprimento de ordem judicial |

---

## 5. Astreintes (art. 537, CPC)

### Parametros de Fixacao

```
TEMPLATE — FIXACAO DE ASTREINTES

Fixo multa diaria/periodica de R$ [VALOR] por [DIA / SEMANA / MES / DESCUMPRIMENTO],
em caso de descumprimento da obrigacao de [FAZER / NAO FAZER / ENTREGAR],
com termo inicial em [DATA / INTIMACAO / TRANSITO EM JULGADO],
limitada ao valor total de R$ [TETO] (ou sem limite).

Fundamentacao: Art. 537, CPC.
```

**Criterios para definir valor:**
- Proporcionalidade com a obrigacao
- Capacidade economica do devedor
- Suficiencia para coagir (nao pode ser irrisoria)
- Limitacao total (recomendada para evitar enriquecimento sem causa)
- Possibilidade de revisao a qualquer tempo (art. 537, §1)

**Destinatario:** A multa reverte ao CREDOR (nao ao Estado).

---

## 6. Custas e Despesas Processuais

### Tabela de Referencia — Justica Estadual (modelo ES)

| Item | Valor | Base | Observacao |
|------|-------|------|------------|
| Custas iniciais | % sobre valor da causa | Regimento de Custas estadual | Varia por UF |
| Preparo de recurso | % sobre valor da causa ou da condenacao | Art. 1.007, CPC | Complementar em 5 dias se insuficiente |
| Diligencias oficiais de justica | Tabela do Tribunal | Por diligencia | Orcamento previo |
| Pericia judicial | Fixado no despacho | Arbitrado pelo juiz | Art. 465, §2, CPC |
| Atos notariais e de registro | Tabela de emolumentos | Lei estadual | Varia por UF |

### Isencoes e Gratuidade

| Situacao | Isencao | Fundamento |
|----------|---------|------------|
| Gratuidade deferida | Total (suspensa por 5 anos) | Art. 98, CPC |
| Fazenda Publica | Custas ao final | Art. 91, CPC |
| MP como parte | Isento | Art. 128, §5, II, "a", CF |
| Embargos de declaracao | Sem preparo | Art. 1.023, CPC |
| Agravo interno | Sem preparo (maioria dos TJs) | Regimento interno |

### Honorarios Periciais em AJG — TJES (Ato 008/2021)

**Norma:** Ato Normativo Conjunto 008/2021-PRES/TJES (revogou OS 004/2016).

**4 hipoteses matriciais:**

| Hipotese | Regime | Base normativa |
|----------|--------|----------------|
| (a) Nenhuma parte tem AJG | Requerente da prova adianta integralmente | Art. 95, caput, CPC |
| (b) Autora tem AJG, so reu requereu | Reu adianta integralmente; AJG da autora nao repercute | Art. 95, caput, CPC |
| (c) Autora com AJG deve ratear | Cota da autora → Estado via SEI (Secretaria Judiciaria); excedente ao teto CNJ suspenso 5 anos | Art. 95, §3, II + Ato 008/2021 + Res. CNJ 232/2016 |
| (d) Reu PJ alega AJG | PJ deve COMPROVAR insuficiencia (presuncao e so para pessoa natural) | Art. 99, §§2 e 3, CPC |

**Procedimento TJES (via SEI):**
1. Decisao de AJG transitada em julgado
2. Nomeacao do perito com enquadramento na tabela
3. CND do perito
4. Oficio a Secretaria Judiciaria via SEI
5. Intimacao previa da PGE — condicao de procedibilidade para pagamento

**Tabelas de referencia:**
- Pericias medicas: Resolucao TJES 06/2021 + convenio PGE
- Demais pericias: tabela CNJ 232/2016 (TJES nao editou tabela propria — art. 17, Ato 008/2021)
- Ressarcimento ao erario: art. 15 do Ato 008/2021

**Em qualquer hipotese:** AJG nao afasta responsabilidade pela sucumbencia (art. 98, §2, CPC); exigibilidade suspensa por 5 anos (art. 98, §3).

---

## 7. RPV e Precatorio

### Limites RPV (Requisicao de Pequeno Valor)

| Ente Federativo | Limite RPV | Fundamentacao |
|-----------------|------------|---------------|
| Uniao Federal | 60 salarios minimos | Art. 17, §1, Lei 10.259/01 |
| Estados (regra geral) | 40 salarios minimos | Art. 87, ADCT (exceto se lei propria) |
| Municipios (regra geral) | 30 salarios minimos | Art. 87, ADCT (exceto se lei propria) |

**Regra:** Valor total da condenacao por beneficiario. Vedado fracionar (Sumula 100/CNJ).

---

## Erros Comuns a Evitar

| Erro | Correto |
|------|---------|
| SELIC + IPCA-E (bis in idem) | SELIC ja inclui correcao — usar sozinha |
| Correcao desde a citacao para dano moral | SELIC desde o EVENTO DANOSO (Tema 1.368 — convergencia S.54+S.362) |
| Honorarios sobre valor da causa quando ha condenacao | Base = valor da condenacao (art. 85, §2) |
| Multa do art. 523 contra Fazenda Publica | Fazenda se sujeita ao art. 535, nao ao 523 |
| Astreintes sem teto maximo | Recomendavel fixar limite total |
| Fracionar precatorio em RPVs | Vedado — Sumula 100/CNJ |
| Juros de 1% + SELIC simultaneos | SELIC = juros + correcao |
| Fazenda pos-EC 113 com IPCA-E + juros separados | SELIC unica desde 09/12/2021 |
| Aplicar 1% a.m. + IPCA-E apos 15/10/2025 | Tema 1.368: SELIC unica para dividas civis — formula antiga superada |
| Honorarios periciais AJG sem intimacao da PGE | Intimacao previa da PGE e condicao de procedibilidade (Ato 008/2021-TJES) |

---

## Integracao no Ecossistema

- **Referenciado por:** `sentenca-judicial-br` (blocos de juros/correcao/honorarios no dispositivo)
- **Referenciado por:** `checklist-saneamento` (honorarios periciais na nomeacao)
- **Referenciado por:** `despacho-generator` (multas, custas, preparo)
- **Complementa:** `peticao-analyzer` (verificar se pedidos de juros/correcao estao corretos)
