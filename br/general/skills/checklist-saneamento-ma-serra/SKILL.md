---
name: checklist-saneamento-ma-serra
title: Checklist Saneamento — Organizacao do Processo para Instrucao (Art. 357, CPC)
description: 'Checklist completo para despacho saneador conforme art. 357 do CPC/2015 — 5 incisos obrigatorios, decisao saneadora modelo, inversao de onus da prova, delimitacao de pontos controvertidos e organizacao do processo para instrucao. Integra com peticao-analyzer (CAPPD) para identificar automaticamente os pontos controvertidos. Usar quando o usuario precisar sanear processo, proferir despacho saneador, organizar processo para instrucao, delimitar pontos controvertidos, definir onus da prova, admitir provas, designar audiencia de instrucao, decidir preliminares pendentes. Triggers: "saneamento", "saneador", "sanear processo", "art. 357", "pontos controvertidos", "onus da prova", "organizacao do processo", "despacho saneador", "preliminares", "provas admitidas".'
author: ma-serra
author_url: https://github.com/ma-serra/lex-intelligentia-skills/tree/main/skills/magistrado/checklist-saneamento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Checklist Saneamento — Organizacao do Processo para Instrucao (Art. 357, CPC)

## Overview

Skill para geracao de decisao saneadora completa, cobrindo todos os 5 incisos do art. 357 do CPC/2015. Integra-se com o output da `peticao-analyzer` (framework CAPPD) para identificar automaticamente pontos controvertidos a partir da confrontacao entre peticao inicial e contestacao.

## When to Use

- Sanear processo apos fase postulatoria
- Organizar pontos controvertidos para instrucao
- Decidir sobre inversao de onus da prova
- Admitir ou indeferir provas
- Designar audiencia de instrucao e julgamento

**When NOT to Use:**
- Julgamento antecipado do merito (art. 355, CPC) — nao ha pontos controvertidos
- Extincao sem merito (art. 485, CPC) — nao ha saneamento
- Processos em Juizado Especial (procedimento simplificado, sem saneamento formal)

---

## Prerequisito: Analise CAPPD

**Antes de sanear**, executar `peticao-analyzer` com ambas as pecas (inicial + contestacao) para obter:
- **C**ausas de pedir identificadas
- **A**rgumentos de ambas as partes
- **P**edidos formulados
- **P**rovas indicadas/produzidas
- **D**efesas (preliminares e merito)

O quadro CAPPD alimenta diretamente os Incisos I a V abaixo.

---

## Checklist Art. 357 — 5 Incisos Obrigatorios

### Inciso I — Questoes Processuais Pendentes (art. 357, I)

```
1. QUESTOES PROCESSUAIS PENDENTES

[  ] Preliminar de incompetencia — Decisao: [ACOLHO/REJEITO] porque [FUNDAMENTO]
[  ] Preliminar de ilegitimidade — Decisao: [ACOLHO/REJEITO] porque [FUNDAMENTO]
[  ] Preliminar de litispendencia/coisa julgada — Decisao: [ACOLHO/REJEITO]
[  ] Impugnacao ao valor da causa — Decisao: [ACOLHO/REJEITO]. Novo valor: R$ [VALOR]
[  ] Impugnacao a gratuidade — Decisao: [MANTENHO/REVOGO] porque [FUNDAMENTO]
[  ] Conexao/continencia — Decisao: [DETERMINO REUNIAO / NAO HA CONEXAO]
[  ] Nulidade de citacao/intimacao — Decisao: [RECONHECO/REJEITO]
[  ] [OUTRA PRELIMINAR]

Resultado: [NAO HA QUESTOES PENDENTES / RESOLVIDAS CONFORME ACIMA]
```

**Regra:** Toda preliminar deve ser resolvida ANTES dos demais incisos. Se a preliminar for acolhida e resultar em extincao, nao ha saneamento.

### Inciso II — Delimitacao das Questoes de Fato e de Direito (art. 357, II)

```
2. DELIMITACAO DAS QUESTOES

2.1 FATOS INCONTROVERSOS (dispensam prova — art. 374, III, CPC):
   a) [FATO 1 — admitido por ambas as partes]
   b) [FATO 2]
   c) [FATO 3]

2.2 FATOS CONTROVERTIDOS (exigem prova):
   a) [FATO CONTROVERTIDO 1]
      - Alegado por: [AUTOR/REU]
      - Impugnado por: [PARTE CONTRARIA]
      - Prova necessaria: [DOCUMENTAL / TESTEMUNHAL / PERICIAL]
   b) [FATO CONTROVERTIDO 2]
      - Alegado por: [PARTE]
      - Impugnado por: [PARTE CONTRARIA]
      - Prova necessaria: [TIPO]
   c) [FATO CONTROVERTIDO 3]

2.3 QUESTOES DE DIREITO A RESOLVER:
   a) [QUESTAO JURIDICA 1 — ex: prescricao, decadencia, incidencia de norma]
   b) [QUESTAO JURIDICA 2 — ex: interpretacao contratual, responsabilidade]
   c) [QUESTAO JURIDICA 3]
```

**Fonte CAPPD:** Cruzar Pedidos x Defesas do `peticao-analyzer` — o que nao foi impugnado e incontroverso (art. 341, CPC), o que foi impugnado e controvertido.

**VERIFICAR ART. 356, CPC:** Se algum pedido ja esta maduro (prova exclusivamente documental + sem fatos controvertidos), considerar julgamento antecipado parcial ANTES de prosseguir ao saneamento dos demais. Ver secao "Julgamento Antecipado Parcial" abaixo.

### Inciso III — Distribuicao do Onus da Prova (art. 357, III c/c art. 373)

```
3. ONUS DA PROVA

3.1 REGRA GERAL (art. 373, CPC):
   - Autor: fato constitutivo do seu direito (inciso I)
   - Reu: fato impeditivo, modificativo ou extintivo (inciso II)

3.2 INVERSAO DO ONUS (se aplicavel):
   [  ] NAO INVERTO — aplica-se a regra geral
   [  ] INVERTO quanto a [FATO ESPECIFICO], com fundamento em:
       [  ] Art. 6, VIII, CDC — hipossuficiencia tecnica do consumidor
       [  ] Art. 373, §1, CPC — impossibilidade/excessiva dificuldade de prova
       [  ] Presuncao legal: [ESPECIFICAR — ex: art. 14, §4, CDC; art. 927, p.u., CC]

   Justificativa da inversao: [RAZAO CONCRETA — nao basta citar a lei]
   Parte que assume o onus: [QUEM]
   Fato especifico invertido: [QUAL]
```

**Erros comuns:**
- Inverter onus de forma generica ("inverto o onus da prova") sem especificar QUAL fato
- Inverter em materia que nao admite inversao (ex: fato constitutivo de direito real)
- Nao fundamentar concretamente a hipossuficiencia

### Inciso IV — Provas Admitidas (art. 357, IV)

```
4. PROVAS ADMITIDAS

4.1 DEFERIDAS:
   [  ] Prova documental: [ESPECIFICAR — ex: extratos bancarios, contrato, prontuario]
       - Prazo: [PRAZO] dias para juntada
       - Responsavel: [PARTE]
   [  ] Prova testemunhal:
       - Autor: ate [N] testemunhas
       - Reu: ate [N] testemunhas
       - Limite art. 357, §§6-7: 3 por fato, 10 no total
       - Rol: [JA APRESENTADO / Apresentar ate 15 dias antes da AIJ]
   [  ] Prova pericial: [ESPECIALIDADE]
       - Perito nomeado: [NOME], [REGISTRO]
       - Quesitos: apresentar em 15 dias (art. 465, §1, CPC)
       - Assistentes: indicar em 15 dias
       - Honorarios provisorios: R$ [VALOR]
       - Prazo do laudo: [PRAZO] dias
       - REGIME DE CUSTEIO (verificar AJG):
         ( ) Nenhuma parte tem AJG → requerente da prova adianta (art. 95, caput, CPC)
         ( ) Autora com AJG, so reu requereu → reu adianta integralmente
         ( ) Autora com AJG deve ratear → cota da autora via Estado/SEI (Ato 008/2021-TJES; tabela CNJ 232/2016)
         ( ) Reu PJ alega AJG → PJ deve COMPROVAR insuficiencia (art. 99, §§2-3, CPC)
         ATENCAO: Intimar PGE antes do pagamento (condicao de procedibilidade — Ato 008/2021-TJES)
   [  ] Depoimento pessoal de [PARTE] (art. 385, CPC)
   [  ] Inspecao judicial em [LOCAL] (art. 481, CPC)

4.2 INDEFERIDAS (art. 370, p.u., CPC):
   [  ] [PROVA] — Motivo: [IMPERTINENTE / DILATORIA / DESNECESSARIA]
   [  ] [PROVA] — Motivo: [FATO JA INCONTROVERSO / PROVA EMPRESTADA SUFICIENTE]
```

### Inciso V — Designacao de Audiencia (art. 357, V)

```
5. AUDIENCIA DE INSTRUCAO E JULGAMENTO

[  ] DESIGNO AIJ para [DATA], as [HORA], em [LOCAL / VIDEOCONFERENCIA].
    Pauta prevista:
    (a) [Depoimento pessoal do autor/reu]
    (b) [Oitiva de testemunhas — autor: N, reu: N]
    (c) [Esclarecimentos do perito — art. 477, §3, CPC]
    (d) [Debates orais — art. 364, CPC / Memoriais em [PRAZO] dias]

[  ] NAO DESIGNO audiencia — processo em condicoes de julgamento apos [pericia / prova documental].
    Conclusos para sentenca apos [EVENTO].
```

---

## Template Completo — Decisao Saneadora

```
DECISAO SANEADORA
Processo n. [CNJ]
[AUTOR] x [REU]

Vistos.

Superada a fase postulatoria, passo a sanear o processo (art. 357, CPC).

1. QUESTOES PROCESSUAIS PENDENTES (art. 357, I):
[CONTEUDO DO INCISO I]

2. QUESTOES DE FATO E DE DIREITO (art. 357, II):
[CONTEUDO DO INCISO II]

3. ONUS DA PROVA (art. 357, III):
[CONTEUDO DO INCISO III]

4. PROVAS (art. 357, IV):
[CONTEUDO DO INCISO IV]

5. AUDIENCIA (art. 357, V):
[CONTEUDO DO INCISO V]

As partes tem prazo comum de 5 (cinco) dias para requerer esclarecimentos ou ajustes a esta decisao (art. 357, §1, CPC). Nao havendo impugnacao, a delimitacao torna-se estavel (art. 357, §1, CPC).

Intimem-se.
[COMARCA], [DATA].
[MAGISTRADO]
```

---

## Saneamento Compartilhado (art. 357, §3, CPC)

Quando as partes apresentam delimitacao consensual dos pontos controvertidos:

```
Homologo a delimitacao consensual dos pontos controvertidos apresentada pelas partes (art. 357, §2, CPC), que vincula as partes e o juizo (art. 357, §2, CPC):

Pontos controvertidos consensuais:
1. [PONTO ACORDADO 1]
2. [PONTO ACORDADO 2]

Prossigo com os demais incisos do saneamento conforme template acima.
```

---

## Situacoes Especiais

### Julgamento Antecipado Parcial (art. 356, CPC)

Se um ou mais pedidos estao maduros para julgamento mas outros necessitam instrucao:

```
Verifico que o(s) pedido(s) [ESPECIFICAR] encontra(m)-se maduro(s) para julgamento antecipado parcial (art. 356, CPC).

QUANTO AO(S) PEDIDO(S) [X]: Julgo antecipadamente. [DISPOSITIVO PARCIAL]

QUANTO AO(S) PEDIDO(S) [Y]: Prossigo com o saneamento na forma abaixo.
[DECISAO SANEADORA PARA PEDIDOS REMANESCENTES]
```

### Causa de Alta Complexidade (art. 357, §9, CPC)

```
Tratando-se de causa de alta complexidade [FATO/DIREITO], designo audiencia de saneamento compartilhado (art. 357, §3, CPC) para [DATA], as [HORA].

Pauta:
(a) Delimitacao consensual dos pontos controvertidos
(b) Definicao do onus da prova
(c) Calendarizacao processual (art. 191, CPC)

Intimem-se as partes, pessoalmente ou por advogado.
```

---

## Erros Comuns a Evitar

| Erro | Correto |
|------|---------|
| Sanear sem resolver preliminares | Inciso I e PREREQUISITO dos demais |
| Nao especificar fatos controvertidos | Inciso II exige delimitacao precisa |
| "Onus conforme a lei" sem detalhar | Especificar QUAL fato e de QUEM |
| Inverter onus genericamente | Especificar o fato invertido + fundamento |
| Numero de testemunhas acima do limite | Max 3 por fato, 10 total (art. 357, §§6-7) |
| Nao fixar honorarios periciais | Art. 465, §2 — fixar na nomeacao |
| Omitir prazo do art. 357, §1 | Partes tem 5 dias para pedir esclarecimentos |
| Deferir pericia sem verificar regime AJG | Verificar se ha AJG e aplicar hipotese correta (Ato 008/2021-TJES) |
| Nao considerar art. 356 CPC antes de sanear | Se pedido ja esta maduro, julgar parcialmente antes de prosseguir |

---

## Integracao no Ecossistema

- **Consome:** `peticao-analyzer` (CAPPD — quadro Pedidos vs Defesas → pontos controvertidos)
- **Referencia:** `despacho-generator` (modelo simplificado de saneador, item 2.2)
- **Alimenta:** `sentenca-judicial-br` (delimita o ambito da sentenca)
- **Referencia cruzada:** `calculadora-processual` (honorarios periciais, custas)
