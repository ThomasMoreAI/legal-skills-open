---
name: emolumentos-a-base-nunca-o-valor-sbroggioadv
title: Emolumentos — a base, nunca o valor
description: 'Fundação segura de emolumentos: identifica UF, lei, índice, ato e tabela aplicável, classifica ato com ou sem conteúdo financeiro e explica somente a base/faixa, nunca o valor em reais. Aplica Lei 10.169/2000, veda percentual sobre o negócio, usa a tabela temporalmente correta e reconhece a lei federal do DF. Esta skill deve ser usada quando o pedido mencionar emolumentos, custas do cartório, quanto custa, base de cálculo, valor declarado ou venal, ITBI, tabela, faixa, índice, TFJ, fundos, selo, acréscimos ou data da cobrança.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/emolumentos-a-base-nunca-o-valor
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Emolumentos — a base, nunca o valor

> Camada C1. Explicar arquitetura e base normativa. Não informar quantia em reais nem substituir a tabela vigente.

## Anexos obrigatórios

- `context/emolumentos-norma-por-uf.md`;
- `context/uf-matriz-27.md`;
- `context/escritura-corpus-federal.md` quando houver imóvel;
- `context/travas-defasagem.md`.

## Entradas bloqueantes

Exigir:

1. UF;
2. espécie do ato;
3. data juridicamente relevante da prática/protocolo;
4. existência ou não de conteúdo financeiro;
5. bases documentadas disponíveis: declarado, avaliação fiscal/venal, base tributária ou outra prevista na lei local.

Sem UF ou data, não escolher tabela. Sem documento para a base, não estimar.

## Piso da Lei 10.169/2000

- Estados e DF fixam emolumentos conforme tabela e custo efetivo do serviço.
- Ato sem conteúdo financeiro recebe valor por espécie.
- Ato com conteúdo financeiro usa faixa entre limites, conforme a lei local.
- Percentual sobre o valor do negócio é vedado pelo art. 3º, II.
- Cobrar retificação/refazimento por erro do próprio serviço é vedado.
- Recibo e indicação da cobrança são obrigatórios.
- Vale a tabela temporalmente aplicável ao ato, conforme art. 6º.

O único percentual federal identificado nessa matéria é teto de crédito rural; não convertê-lo em fórmula geral de cobrança.

## Algoritmo

### 1. Identificar a arquitetura da UF

Abrir `emolumentos-norma-por-uf.md` e localizar:

- lei-base;
- índice/mecanismo de atualização;
- ato vigente no período;
- tabela de Notas;
- notas explicativas;
- fundos, taxas, selo, ISS e parcelas destacadas.

No DF, usar a Lei **federal** 14.756/2023. Ato fora da tabela é gratuito, inclusive por analogia, paridade ou extensão.

### 2. Fixar a temporalidade

Determinar qual evento escolhe a tabela na UF e no ato. Não presumir “tabela de hoje”. Considerar transições:

- PB muda de regime a partir de 2027;
- GO pode ter várias versões no mesmo ano;
- RR opera sob lei suspensa/lei anterior aplicável;
- SP atualiza diretamente pela UFESP;
- MT preserva atos protocolizados antes da nova tabela;
- SC distingue lavratura notarial e apresentação registral.

### 3. Classificar a espécie

Identificar item tabelado e presença de conteúdo financeiro. Não enquadrar por analogia criativa. Se o ato não estiver tabelado, aplicar a regra local sobre omissão; no DF, reconhecer gratuidade.

### 4. Determinar a base

Comparar as bases que a lei da UF efetivamente manda considerar. Quando a arquitetura local adotar a maior, demonstrar:

```text
base normativa = maior valor documentado entre
declarado × venal/tributário × base do ITBI/avaliação legal aplicável
```

Não transformar essa fórmula em regra nacional sem a norma estadual. Se houver avaliação judicial ou fiscal exigida por lei, aplicar o art. 2º, §1º da Lei 10.169/2000.

### 5. Separar parcelas

Listar sem valores:

- emolumento;
- taxa de fiscalização;
- fundo(s);
- selo;
- ISS, quando destacado;
- gratuidade/isenção aplicável.

Não dizer que “emolumento” é o total pago. RR, RN, SE, MG, SC e ES demonstram arquiteturas com parcelas externas.

## Saída segura

Entregar:

| Campo | Resultado |
|---|---|
| UF e data do ato | |
| lei, índice e ato de atualização | |
| item/tabela de Notas | |
| espécie com/sem conteúdo financeiro | |
| bases comparadas | |
| base normativa escolhida e fundamento | |
| parcelas externas | |
| pendência de tabela atual | |

Encerrar com: **“Este resultado explica a base e a arquitetura; consulte a tabela oficial vigente para obter a quantia.”**

## Reprovação automática

- valor em reais;
- percentual sobre o negócio;
- tabela sem UF/data;
- tabela de listagem antiga usada contra ato novo;
- lei judicial usada como extrajudicial;
- item inexistente criado por analogia;
- retificação por erro do serviço cobrada;
- fundos/taxas ocultados do total;
- base máxima afirmada sem regra estadual.

## Guard

Não fazer orçamento nem cache de valores. Não calcular tributo, ITBI ou ITCMD. Não informar alíquota. Se o ato/índice de 2026 estiver 🔴 no anexo, declarar a lacuna e exigir consulta oficial antes de qualquer cobrança.
