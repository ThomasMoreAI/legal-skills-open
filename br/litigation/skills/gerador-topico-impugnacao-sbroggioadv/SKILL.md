---
name: gerador-topico-impugnacao-sbroggioadv
title: Gerador de tópico de impugnação
description: 'Transforma um achado CONFIRMADO de integridade — texto oculto com o dado bruto do parser, citação de jurisprudência reprovada por WebFetch, dispositivo legal inexistente conferido na fonte — em minuta de tópico de impugnação pronta para a peça de resposta: (1) o fato técnico com a evidência anexável; (2) o direito, verbatim do anexo (CPC arts. 77, I, 80 e 81; art. 96 quando útil); (3) o precedente institucional (casos-âncora reais, cada um nos termos das suas regras de uso); (4) o pedido — sempre "requer a apuração/aplicação da multa", nunca imputação de crime (CP 299/347 só como risco/encaminhamento). Sem achado confirmado com evidência, recusa e explica — não gera tópico especulativo. Aviso de conferência humana no fim de toda minuta. Aciona: "transformar o achado em tópico", "pedir multa por litigância de má-fé", "preliminar de impugnação", "impugnar a peça com o que foi encontrado", "minuta de impugnação".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/blindagem-peticao-os-marketplace/tree/main/blindagem-peticao-os/skills/gerador-topico-impugnacao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Gerador de tópico de impugnação

## Quando esta skill entra

Quando a triagem CONFIRMOU um achado de integridade e o advogado quer transformá-lo em peça: a
preliminar/tópico de impugnação por litigância de má-fé, com pedido de aplicação de multa,
pronta para inserir na resposta. É o passo que converte o achado em munição — alerta sem
consequência processual não muda o jogo.

## Entrada mínima (gate de recusa — sem exceção)

A skill só gera com **achado confirmado + evidência anexável**:

| Achado que FUNDAMENTA | Evidência exigida |
|---|---|
| Texto oculto / comando dirigido a IA | Saída bruta do parser (RGB, tamanho de fonte, opacidade) + classificação do `classificador-prompt-injection` |
| Unicode invisível deliberado | Saída bruta do parser (codepoints) + classificação de intenção |
| Citação de jurisprudência 🔴 (reprovada) | Queries documentadas do WebFetch (bases consultadas, termos, resultado) — `citacoes-da-peca-recebida` |
| Dispositivo legal inexistente/deturpado | Lado a lado com a fonte oficial — `dispositivos-da-peca-recebida` |

O que **NÃO fundamenta** tópico:

- **Sinal heurístico de uso de IA** (T3) — heurística nunca é prova; não entra nem como reforço.
- **Hash divergente / metadado estranho sozinhos** (T4) — são alerta; o caminho é pedido de
  providência/perícia, não afirmação de má-fé. Nesse caso a skill gera, no máximo, um pedido de
  apuração/perícia — nunca o tópico de multa.
- **Gap do `mapa-de-gaps-da-tese`** — análise estratégica, não integridade.

Sem achado confirmado, a skill **recusa e explica**: "rode antes `/blindagem` (ou a skill da
camada correspondente); não gero tópico especulativo — tópico sem evidência é o mesmo vício que
este produto combate."

## Estrutura da minuta (4 blocos, nesta ordem)

### 1. O fato técnico, com a evidência

Narrativa factual do achado, sem adjetivo e sem imputar intenção: o que foi encontrado, onde
(página/trecho), como foi verificado (parser/fetch), com a evidência bruta referenciada como
documento anexável (JSON do parser, registro das queries). O comando literal achado (o caso
TRT-8 é o modelo) pode ser transcrito entre aspas.

### 2. O direito (verbatim do anexo — nunca de memória)

Texto legal copiado de `context/cpc-litigancia-ma-fe.md`:

- **CPC art. 77, I** — dever de "expor os fatos em juízo conforme a verdade";
- **CPC art. 80, II** ("alterar a verdade dos fatos") e/ou **III** ("usar do processo para
  conseguir objetivo ilegal") — conforme o vetor do achado;
- **CPC art. 81** — multa "superior a um por cento e inferior a dez por cento do valor
  corrigido da causa", mais indenização e honorários (§ 2º quando o valor da causa for
  irrisório ou inestimável);
- **CPC art. 96** — quando útil pedir expresso que o valor da multa reverta à parte contrária.

Nota do anexo (CPC art. 77, § 6º): a multa processual recai sobre a **parte**; quanto ao
**advogado**, a via é a responsabilidade disciplinar pelo órgão de classe — o tópico pede as
duas coisas nos termos certos (multa à parte + ofício à OAB).

### 3. O precedente institucional (regras de uso de `context/casos-ancora-sancoes.md`)

Casar o precedente ao vetor do achado, citando cada caso EXATAMENTE como o anexo autoriza:

- **Fonte branca / comando a IA** → TRT-8, ATOrd 0001062-55.2025.5.08.0130 (multa de 10% do
  valor da causa + ofício à OAB/PA) — com número; + STJ (inquérito de 20/05/2026, 11+
  processos) — sempre como investigação em curso, nunca como condenação.
- **Citação inventada** → TJ/PR 0108267-74.2025.8.16.0000 (2% + ofício à OAB/PR + art. 34,
  XIV, EAOAB) — com número; TST 6ª Turma (1% + OAB/MPF) e TSE (R$ 2 mil; 9 condenações, 5 com
  ofício ao MPE) — como "caso noticiado", com a fonte, ou localizar o acórdão antes de citar
  como precedente direto; TJSC — **sem número, sempre** ("caso noticiado pelo TJSC", com o
  link da nota institucional).
- Connecticut/EUA — **nunca** em peça brasileira (contexto de divulgação apenas).
- Nunca nomear na minuta os advogados sancionados nos casos-âncora.

### 4. O pedido (a linguagem que protege o usuário)

Sempre como **requerimento de apuração/aplicação** — nunca afirmação de crime:

- aplicação da multa do CPC art. 81, indenização e honorários;
- ofício à OAB quanto à conduta do procurador (CPC art. 77, § 6º);
- quando o vetor espelhar os casos-âncora: que se oficie ao Ministério Público, **como os
  tribunais têm feito** (TST → MPF; TSE → MPE). Os CP arts. 299 e 347
  (`context/cp-falsidade-fraude.md`) entram SÓ como risco/encaminhamento possível — jamais
  como imputação: "a parte cometeu falsidade/fraude" não sai desta skill; tipificar é
  conclusão do advogado e, em última instância, do Judiciário (T4);
- a palavra "fraude" nunca como afirmação do produto.

## Fecho obrigatório de toda minuta (T5)

> ⚠️ **Minuta gerada por ferramenta de triagem — conferência humana obrigatória.** Verifique a
> evidência anexada, os dispositivos citados e a pertinência dos precedentes antes de
> protocolar. A decisão de requerer, imputar ou protocolar é exclusivamente do advogado.

## Travas / limites

- **Gate de entrada**: sem achado confirmado + evidência → recusa explicada (nunca tópico
  especulativo).
- **Texto de lei verbatim** de `context/` — fora do corpus → `[VERIFICAR]`, nunca de memória.
- **Casos-âncora só nos termos das regras de uso** (número onde há número; "caso noticiado"
  onde não há; TJSC sempre sem número).
- **T4**: crime só como risco/encaminhamento; **T3**: heurística nunca fundamenta; **T5**:
  aviso no fim de toda minuta, sem versão que o omita.
- Incidente de má-fé como **peça autônoma completa** → domínio do `civel-adv-os` (cross-link);
  aqui sai o tópico/preliminar para inserir na resposta.
