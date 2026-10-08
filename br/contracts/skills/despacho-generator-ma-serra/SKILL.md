---
name: despacho-generator-ma-serra
title: Despacho Generator — Modelos de Despachos por Fase Processual
description: 'Gerador de despachos judiciais padronizados por fase processual — inicial, saneamento, instrucao e pos-sentenca. Modelos completos com placeholders, variacoes e fundamentacao legal. Usar quando o usuario precisar gerar despacho, despachar processo, proferir decisao ordinatoria, dar andamento processual, designar audiencia, intimar parte, determinar emenda, abrir vista, converter rito, determinar citacao, designar pericia ou qualquer ato ordinatorio do juiz. Triggers: "despacho", "despachar", "cite-se", "intime-se", "emende", "audiencia designada", "vista", "pericia", "ato ordinatorio", "andamento", "impulso oficial".'
author: ma-serra
author_url: https://github.com/ma-serra/lex-intelligentia-skills/tree/main/skills/magistrado/despacho-generator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Despacho Generator — Modelos de Despachos por Fase Processual

## Overview

Skill para geracao rapida de despachos judiciais padronizados, organizados por fase processual. Cada modelo contem texto completo com placeholders `[CAMPO]`, variacoes para situacoes comuns e fundamentacao legal aplicavel. Projetado para uso diario em gabinete, cobrindo os 20+ despachos mais frequentes no juizo civel.

## When to Use

- Gerar despachos de rotina em qualquer fase processual
- Padronizar linguagem e fundamentacao do gabinete
- Acelerar o fluxo de despachos diarios
- Garantir que nenhum requisito legal seja omitido

**When NOT to Use:**
- Decisoes interlocutorias com fundamentacao complexa (usar `sentenca-judicial-br`)
- Despachos em materia penal (estrutura e prazos distintos)
- Atos do escrivao/diretor de secretaria (nao sao despachos judiciais)

---

## Fase 1 — Despachos Iniciais

### 1.1 Recebimento e Citacao (Procedimento Comum)

```
Recebo a inicial. Defiro a gratuidade de justica / Indefiro a gratuidade de justica, pois [MOTIVO].

Cite-se o(a) reu(re) [NOME_REU] para, no prazo de 15 (quinze) dias uteis, apresentar contestacao (art. 335, CPC), sob pena de revelia (art. 344, CPC).

Modo de citacao: [CORREIO / OFICIAL DE JUSTICA / EDITAL / ELETRONICO].

[SE TUTELA REQUERIDA:]
Quanto a tutela de urgencia, decido em separado / na sequencia deste despacho.

Intimem-se.
[COMARCA], [DATA].
[MAGISTRADO]
```

**Variacoes:**
- **Fazenda Publica:** prazo 30 dias (art. 183, CPC), citacao por oficial
- **Juizado Especial:** prazo 15 dias corridos, audiencia de conciliacao obrigatoria (art. 16, Lei 9.099/95)
- **Reconvencao possivel:** incluir alerta ao autor sobre prazo de 15 dias para resposta (art. 343, §1, CPC)

### 1.2 Emenda da Inicial (art. 321, CPC)

```
Verifico que a inicial apresenta as seguintes deficiencias:
[  ] Falta de [DOCUMENTO ESSENCIAL — art. 320, CPC]
[  ] Pedido generico sem enquadramento no art. 324, §1, CPC
[  ] Valor da causa incompativel com o pedido (art. 292, CPC)
[  ] Ilegitimidade aparente de parte [ATIVA/PASSIVA]
[  ] Ausencia de procuracao / procuracao irregular
[  ] [OUTRO VICIO]

Concedo ao(a) autor(a) o prazo de 15 (quinze) dias uteis para emendar a inicial (art. 321, CPC), sob pena de indeferimento e extincao sem resolucao do merito (art. 321, paragrafo unico c/c art. 485, I, CPC).

Intimem-se.
```

### 1.3 Indeferimento da Inicial (art. 330, CPC)

```
Indefiro a inicial pelos seguintes fundamentos:
[  ] Inepcia (art. 330, I c/c art. 330, §1, CPC) — [falta de pedido / falta de causa de pedir / pedido juridicamente impossivel / pedidos incompativeis]
[  ] Ilegitimidade de parte (art. 330, II, CPC)
[  ] Falta de interesse processual (art. 330, III, CPC)
[  ] Nao emendada no prazo (art. 321, paragrafo unico, CPC)

Julgo extinto o processo sem resolucao do merito (art. 485, I, CPC).

Custas pelo(a) autor(a), observada a gratuidade se deferida.
Sem honorarios (nao houve citacao).

P.R.I.
```

### 1.4 Designacao de Audiencia de Conciliacao (art. 334, CPC)

```
Designo audiencia de conciliacao/mediacao para o dia [DATA], as [HORA], [LOCAL / PLATAFORMA VIRTUAL].

Intimem-se as partes, por seus advogados, com antecedencia minima de 20 (vinte) dias (art. 334, CPC).

Advirto que:
(a) O nao comparecimento injustificado e ato atentatório a dignidade da justica, sujeito a multa de ate 2% do valor da causa (art. 334, §8, CPC);
(b) Havendo litisconsortes, o desinteresse na autocomposicao deve ser manifestado por todos (art. 334, §6, CPC);
(c) O autor pode manifestar desinteresse na audiencia na inicial; o reu, em petição com 10 dias de antecedencia (art. 334, §5, CPC).

Intimem-se.
```

---

## Fase 2 — Despachos de Saneamento e Organizacao

### 2.1 Especificacao de Provas (art. 348/349, CPC)

```
Nao sendo caso de julgamento antecipado, concedo as partes o prazo comum de 15 (quinze) dias uteis para especificarem as provas que pretendem produzir, justificando sua pertinencia (art. 348, CPC).

Advirto que requerimentos genericos serao indeferidos (art. 370, paragrafo unico, CPC).

Intimem-se.
```

### 2.2 Decisao Saneadora Simplificada (art. 357, CPC)

```
Saneio o processo nos seguintes termos:

1. QUESTOES PROCESSUAIS: [Nao ha preliminares pendentes / Rejeito a preliminar de X porque Y].
2. QUESTOES DE FATO: Os pontos controvertidos sao: [PONTO 1], [PONTO 2], [PONTO 3].
3. QUESTOES DE DIREITO: As questoes juridicas a resolver sao: [QUESTAO 1], [QUESTAO 2].
4. ONUS DA PROVA: Distribuicao na forma do art. 373, CPC. [SE INVERSAO: Inverto o onus da prova quanto a [FATO], com fundamento no art. 373, §1, CPC / CDC art. 6, VIII].
5. PROVAS: Defiro [prova testemunhal / pericial / documental complementar]. Indefiro [prova X por Y].

[SE AUDIENCIA:] Designo audiencia de instrucao para [DATA], as [HORA].
[SE PERICIA:] Nomeio perito [NOME], intimando as partes para indicar assistentes e quesitos em 15 dias (art. 465, §1, CPC).

Intimem-se.
```

**Nota:** Para saneamento completo e detalhado, usar a skill `checklist-saneamento`.

### 2.3 Nomeacao de Perito (art. 465, CPC)

```
Defiro a prova pericial requerida.

Nomeio como perito(a) o(a) Sr(a). [NOME_PERITO], [PROFISSAO/REGISTRO], cadastrado(a) no CEJUSC/Tribunal.

Intimem-se as partes para, no prazo de 15 (quinze) dias:
(a) Indicar assistente tecnico (art. 465, §1, I, CPC);
(b) Apresentar quesitos (art. 465, §1, II, CPC).

Fixo prazo de [30/60/90] dias para entrega do laudo (art. 465, §2, CPC).

Honorarios periciais provisorios: R$ [VALOR], a cargo de [PARTE REQUERENTE / AMBAS NA PROPORCAO DE 50%].

[SE GRATUIDADE:] Honorarios na forma do art. 95, §3, CPC.

Intimem-se.
```

### 2.4 Conversao de Rito (Comum → Sumario/JEC)

```
Verifico que o valor da causa e de R$ [VALOR], inferior a [40/60] salarios minimos.

Converto o rito para [JUIZADO ESPECIAL / PROCEDIMENTO SUMARIO], nos termos do art. [3, Lei 9.099/95 / art. 1.049, CPC].

Remetam-se os autos ao [JUIZADO ESPECIAL CIVEL DA COMARCA / VARA COMPETENTE].

Intimem-se.
```

---

## Fase 3 — Despachos de Instrucao

### 3.1 Designacao de Audiencia de Instrucao (art. 358, CPC)

```
Designo audiencia de instrucao e julgamento para o dia [DATA], as [HORA], [LOCAL / PLATAFORMA VIRTUAL].

Ficam intimadas as partes para comparecerem pessoalmente ou por preposto com poderes (art. 843, CLT, por analogia no civel).

Rol de testemunhas: [JA APRESENTADO / Apresentar em ate 15 dias antes da audiencia — art. 357, §4, CPC].

Numero maximo de testemunhas: [3 por fato controvertido, ate 10 no total — art. 357, §§6-7, CPC].

[SE DEPOIMENTO PESSOAL:] Expeca-se intimacao pessoal de [PARTE] para depor, sob pena de confissao (art. 385, §1, CPC).

Intimem-se.
```

### 3.2 Carta Precatoria / Rogatoria

```
Defiro a expedicao de carta [PRECATORIA / ROGATORIA / DE ORDEM] para [FINALIDADE: citacao / intimacao / oitiva de testemunha / cumprimento de diligencia].

Juizo deprecado: [VARA] — [COMARCA/ESTADO/PAIS].

Prazo para cumprimento: [30/60/90] dias.

Providencie a Secretaria a expedicao, instruindo com [DOCUMENTOS NECESSARIOS].

Intimem-se.
```

### 3.3 Manifestacao sobre Documentos (art. 437, CPC)

```
Juntados novos documentos por [PARTE], intime-se a parte contraria para manifestacao no prazo de 15 (quinze) dias uteis (art. 437, §1, CPC).

[SE DOCUMENTO EXTEMPORANEO:]
Faculto a manifestacao, ressalvada a apreciacao da admissibilidade em momento oportuno (art. 435, CPC).

Intimem-se.
```

### 3.4 Diligencias Complementares

```
Para melhor instrucao do feito, determino:
[  ] Juntada de [DOCUMENTO] pela parte [AUTORA/RE], no prazo de [PRAZO] dias (art. 396, CPC)
[  ] Expedicao de oficio a [ORGAO] requisitando [INFORMACAO] (art. 438, CPC)
[  ] Realizacao de inspeção judicial em [LOCAL] (art. 481, CPC)
[  ] Complementacao do laudo pericial quanto a [QUESITO] (art. 480, CPC)
[  ] Oitiva de [TESTEMUNHA REFERIDA / INFORMANTE] (art. 461, I, CPC)

Prazo para cumprimento: [PRAZO] dias.

Intimem-se.
```

---

## Fase 4 — Despachos Pos-Sentenca

### 4.1 Abertura de Vista para Contrarrazoes

```
Interposto recurso de [APELACAO / AGRAVO / EMBARGOS DE DECLARACAO] pela parte [AUTORA/RE]:

[SE APELACAO:] Intime-se a parte contraria para apresentar contrarrazoes no prazo de 15 (quinze) dias uteis (art. 1.010, §1, CPC).

[SE EMBARGOS:] Intime-se a parte contraria para manifestacao em 5 (cinco) dias (art. 1.023, §2, CPC), se houver efeito modificativo ou infringente.

[SE AGRAVO:] Intime-se o agravado para resposta em 15 (quinze) dias uteis (art. 1.019, II, CPC).

Intimem-se.
```

### 4.2 Juizo de Admissibilidade / Remessa ao Tribunal

```
Recebo o recurso de [APELACAO / APELACAO ADESIVA] interposto por [PARTE].

Verifico: tempestividade ([  ] sim [  ] nao), preparo ([  ] recolhido [  ] isento [  ] deserto), regularidade formal ([  ] sim [  ] nao).

[SE ADMITIDO:] Remetam-se os autos ao E. Tribunal de Justica [DO ESTADO].

[SE DESERTO:] Certifico a desercao (art. 1.007, CPC). Intime-se para recolhimento em dobro no prazo de 5 dias (art. 1.007, §4, CPC) / Declaro deserto o recurso.

Intimem-se.
```

### 4.3 Cumprimento de Sentenca (art. 523, CPC)

```
Requerido o cumprimento de sentenca por [EXEQUENTE]:

Intime-se o(a) executado(a) [NOME] para pagamento do debito no valor de R$ [VALOR], no prazo de 15 (quinze) dias uteis (art. 523, CPC), sob pena de:
(a) Multa de 10% (art. 523, §1, CPC);
(b) Honorarios de 10% (art. 523, §1, CPC).

[SE FAZENDA PUBLICA:] Intime-se a Fazenda Publica para impugnacao no prazo de 30 (trinta) dias (art. 535, CPC). Nao incide multa do art. 523.

Intimem-se.
```

### 4.4 Extincao e Arquivamento

```
[SE CUMPRIMENTO SATISFEITO:]
Certificado o cumprimento integral da obrigacao, julgo extinta a execucao nos termos do art. 924, II, CPC.
Arquivem-se os autos, observadas as formalidades legais.

[SE ABANDONO:]
Decorrido o prazo sem manifestacao do exequente, intimado pessoalmente (art. 485, §1, CPC), julgo extinto o processo por abandono (art. 485, III, CPC).
Arquivem-se.

[SE PRESCRICAO INTERCORRENTE:]
Reconheco a prescricao intercorrente (art. 924, V c/c art. 921, §§4-5, CPC), ouvidas as partes (art. 10, CPC).
Julgo extinta a execucao. Arquivem-se.

P.R.I.
```

---

## Erros Comuns a Evitar

| Erro | Correto |
|------|---------|
| Prazo de contestacao em dias corridos | 15 dias UTEIS (art. 219, CPC) |
| Citar reu sem verificar emenda necessaria | Sempre verificar art. 321 antes de citar |
| Nao advertir sobre multa na conciliacao | Art. 334, §8 — multa obrigatoria |
| Inverter onus sem fundamentar | Exige fundamento no art. 373, §1 ou CDC |
| Nao intimar pessoalmente para depoimento | Confissao so vale com intimacao pessoal (art. 385, §1) |
| Esquecer prazo diferenciado da Fazenda | Dobro para contestar (art. 183), 30 dias para impugnacao (art. 535) |
| Admitir apelacao deserta sem dar prazo para complemento | Art. 1.007, §2 — 5 dias para complementar |

---

## Integracao no Ecossistema

- **Alimentado por:** `peticao-analyzer` (identifica que tipo de despacho e necessario), `dje-monitor` (prazos e pendencias)
- **Alimenta:** `sentenca-judicial-br` (quando despacho evolui para decisao interlocutoria), `checklist-saneamento` (despacho saneador completo)
- **Referencia cruzada:** `calculadora-processual` (valores de multa, honorarios periciais)
