---
name: recusa-e-nota-de-exigencias-por-uf-sbroggioadv
title: Recusa e nota de exigências por UF
description: Resolve a qualificação negativa conforme a UF, preservando quatro regimes de forma, três verbos normativos, conteúdo taxativo da nota do RN e regras opostas sobre exigência superveniente. Esta skill deve ser usada quando o pedido mencionar recusar ato, nota de exigências, nota devolutiva, recusa escrita, fundamentação, diligência corretiva, exigência genérica, nova exigência, inconformismo do interessado ou negativa de lavratura.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/recusa-e-nota-de-exigencias-por-uf
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Recusa e nota de exigências por UF

> Camada C2. Distinguir forma, verbo, conteúdo e destino. Não existe nota devolutiva federal geral para o tabelionato de notas.

## Anexos obrigatórios

- `context/uf-matriz-27.md` — categoria e endereço do rito estadual;
- `context/sequencia-do-ato.md` — posição da qualificação negativa no ciclo;
- `context/travas-defasagem.md` — conteúdo, exceções e falsos positivos;
- `context/estado-da-norma.md` — vigência da redação estadual.

## Entradas bloqueantes

Fixar:

1. UF;
2. ato ou procedimento notarial;
3. fato concreto que impede, condiciona ou apenas recomenda a prática;
4. dispositivo local aplicável;
5. existência de pedido de formalização pela parte ou por advogado;
6. informação ou documento novo surgido após a primeira análise.

Sem UF, descrever apenas a qualificação federal e declarar: **“O esqueleto federal não tem nota de exigências notarial nominada, protocolo ou prazo de análise.”** Não fabricar forma escrita nacional.

## Algoritmo

### 1. Classificar a trava antes da recusa

Separar:

- impedimento absoluto;
- impedimento condicional sanável por ato externo;
- pendência sanável por documento ou correção;
- fato consignável que não autoriza recusa;
- matéria devolutiva que exige encaminhamento ao juízo, ao Ministério Público ou à autoridade competente.

Não emitir nota de exigências para situação consignável. Não tratar encaminhamento obrigatório como decisão negativa de mérito.

### 2. Aplicar um dos quatro regimes de forma

1. **Escrita sempre:** SP, ES, PI, MT, GO, MG, BA e RN, nos endereços e hipóteses locais.
2. **Escrita quando requerida:** RJ e SC. Em SC, conferir a regra especial da ata notarial, cuja recusa escrita é obrigatória.
3. **Escrita se solicitada pela parte ou advogado:** PE, ressalvadas as hipóteses locais incondicionais.
4. **Escrita não exigida:** PR e RS. Recomendar registro escrito apenas como prudência probatória, identificando que não se trata de comando estadual.

Para as demais UFs, ler a linha e o dispositivo específico na matriz. Não encaixar por semelhança nominal.

### 3. Preservar os três verbos

Na mesma situação de fato, distinguir:

- **dever de negar, sem comando de escrita:** AL e RS;
- **dever de negar por escrito:** SP e PE;
- **faculdade de negar, com fundamentação escrita:** CE, SE, BA, MG, MS, GO, PR e ES.

Não converter “poderá se negar” em dever. Não acrescentar “por escrito” ao dever de AL ou RS. Confirmar o ato e a hipótese antes de aplicar o verbo, pois a forma geral e a regra especial podem divergir dentro da mesma UF.

### 4. Redigir conteúdo individualizado

Estruturar a nota com três elementos de segurança:

1. dispositivo aplicável;
2. razão fática concreta e individualizada;
3. diligência ou caminho de correção, quando sanável.

Identificar essa estrutura como padrão de desenho quando a UF não a impuser literalmente. Proibir remissão genérica a “legalidade” ou “segurança jurídica” em MA, BA e PE.

No RN, cumprir o art. 94, I-IV, de modo taxativo:

- fundamentos, dispositivos legais e diligências necessárias à ultimação do ato;
- identificação do responsável pela análise;
- número da guia e do protocolo;
- informação sobre a possibilidade de requerer a suscitação de dúvida.

Manter emissão de uma só vez, arquivo cronológico e recibo quando exigidos pelo regime local.

### 5. Tratar exigência superveniente

- **PB, MA e BA:** vedar exigência posterior que deveria ter sido constatada na primeira análise.
- **PE, PI, CE e AL:** admitir somente na hipótese e nos limites de documento, elemento novo ou fundada razão descrita pela norma local; no PI, observar a renovação do prazo.
- **RN:** admitir exigência superveniente fundada em informação nova, conforme art. 94, §6º.

Nunca transportar a vedação da PB para o RN. Não usar exigência tardia para alongar artificialmente prazo.

### 6. Definir o destino do inconformismo

Acionar `duvida-notarial-por-uf` antes de prometer suscitação. Em Categoria B, indicar a via correcional localizada sem criar dúvida notarial própria. Em RO, declarar que a recusa notarial geral não foi localizada e limitar a resposta ao ponto comprovado.

## Saída

| Campo | Resultado |
|---|---|
| UF, ato e data de corte | |
| categoria da trava | A, B, C, D ou E |
| verbo normativo | dever, dever escrito ou faculdade escrita |
| regime de forma | sempre, a requerimento, se solicitado ou não exigido |
| fundamento fático e jurídico | |
| diligência corretiva | |
| exigência superveniente | vedada, condicionada, admitida ou não localizada |
| destino do inconformismo | |
| lacunas | |

## Reprovação automática

- afirmar recusa escrita como regra nacional;
- apresentar prudência probatória de PR ou RS como obrigação;
- emitir nota genérica em MA, BA ou PE;
- omitir qualquer item taxativo do RN;
- parcelar exigências para adiar prazo;
- transportar regra de exigência superveniente;
- prometer dúvida sem classificar a UF;
- recusar situação que a norma manda consignar ou encaminhar.
