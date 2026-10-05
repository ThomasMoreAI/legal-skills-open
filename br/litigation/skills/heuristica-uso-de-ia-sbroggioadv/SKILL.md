---
name: heuristica-uso-de-ia-sbroggioadv
title: HEURÍSTICA-USO-DE-IA — Sinais honestos, nunca prova
description: 'HEURÍSTICA-USO-DE-IA — Responde "foi usada IA nesta peça?" com honestidade radical: abre declarando que não existe detector confiável de "texto de IA" (a marca d''água da Anthropic só marca Claude pós-02/08/2026 e a API não é pública; a OpenAI descontinuou o próprio detector) e então lista os sinais que PODEM ser apontados, por força de evidência — FORTE: citação inventada ou dispositivo inexistente confirmados por fetch real; MÉDIO: comando de prompt injection achado por parser; FRACO e rotulado como fraco: padrões estilísticos. A síntese sai sem número, sem score e sem "detectamos" — sempre "sinal heurístico, nunca prova de autoria por IA" — e fecha com o disclaimer verbatim do anexo watermark. Nunca emite %, nunca "confirmamos a marca d''água", nunca "não é IA". Aciona: "essa peça foi feita por IA?", "dá pra provar que usaram ChatGPT/Claude?", pedido de indício de uso de IA, roteamento do blindagem-master.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/blindagem-peticao-os-marketplace/tree/main/blindagem-peticao-os/skills/heuristica-uso-de-ia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# HEURÍSTICA-USO-DE-IA — Sinais honestos, nunca prova

## 1. ABERTURA OBRIGATÓRIA — o enquadramento antes de qualquer sinal

Toda execução desta skill **começa** com este enquadramento (base:
`context/watermark-anthropic-limites.md`):

> **Não existe detector confiável de "texto de IA".** A marca d'água da Anthropic (anunciada em
> 12/08/2026) marca apenas texto de modelos **Claude** lançados a partir de **02/08/2026** — não
> detecta ChatGPT, Gemini, Copilot ou qualquer outro modelo — e a **API de detecção para
> terceiros não está disponível** (anunciada, sem data, sem acesso). A própria OpenAI
> **descontinuou o seu classificador** em 2023 por baixa acurácia, sem substituto. Detectores
> comerciais reportam números inconsistentes entre estudos — a dispersão é, em si, o achado.
> O que esta skill entrega são **sinais heurísticos com evidência anexa — nunca prova de
> autoria**.

Detecção via marca d'água é item de roadmap **v0.2, rotulada e condicionada à existência da API
pública** — não é feature desta versão, e nenhuma entrega pode sugerir o contrário.

## 2. SINAIS — hierarquia por força de evidência

A skill **não caça sinais soltos**: ela consolida o que as outras camadas já provaram, na ordem
de força abaixo.

### 🟥 FORTES (evidência documentada — o que os tribunais usaram nos casos reais)

| Sinal | De onde vem | Por que é forte |
|---|---|---|
| **Citação de jurisprudência inventada, confirmada** | 🔴 da `citacoes-da-peca-recebida` (busca ativa documentada + fetch real que não encontrou) | É o indício central dos casos reais de uso de IA sem revisão — foi o que os tribunais apontaram nos casos-âncora (TST, TJ/PR, TJSC, TSE — `context/casos-ancora-sancoes.md`) |
| **Dispositivo legal inexistente ou com teor deturpado, confirmado** | 🔴/⚠️ deturpado da `dispositivos-da-peca-recebida` (fonte oficial aberta) | Mesmo padrão: "base de lei criada" é a assinatura documentada de texto gerado sem conferência |

Sinal forte só entra aqui **com o selo confirmado pelas skills de origem** — nunca por suspeita
própria desta skill.

### 🟨 MÉDIO

| Sinal | De onde vem | Por que é médio |
|---|---|---|
| **Comando de prompt injection achado e classificado** | Parser da C1 + `classificador-prompt-injection` (🎯 COMANDO) | Pressupõe que o **autor da peça esperava leitura por IA** — indício de contexto de uso de IA no fluxo, não de autoria do texto |

### ⬜ FRACOS — sempre rotulados como fracos

Padrões estilísticos (uniformidade incomum, estruturas repetitivas, vocabulário genérico,
formatação típica de saída de modelo). **Nunca decisivos, nunca listados como "prova"**, nunca
promovidos a médio/forte por acumulação — dez sinais fracos continuam fracos. Pesquisa
documentada no anexo mostra que texto humano levemente editado é rotineiramente classificado
errado por detectores — estilo não separa autor de revisor.

## 3. SAÍDA — formato fixo da síntese

Um **parágrafo de síntese**, SEM número de probabilidade, SEM score, SEM "detectamos":

> **Síntese heurística:** há **N indícios fortes** (com evidência anexa: [listar — ex.: 2
> citações 🔴 confirmadas, 1 dispositivo inexistente]), **M médios** ([listar]) e sinais fracos
> registrados apenas como observação de estilo. **Isso é sinal heurístico, nunca prova de
> autoria por IA.** A força do achado está na evidência documentada de cada indício — não em
> qualquer inferência sobre "quem escreveu".

Regras do formato:

- N e M são **contagens de indícios com evidência**, nunca probabilidade;
- cada indício forte/médio referencia a evidência da skill de origem (fetch, queries, saída de
  parser);
- sinais fracos aparecem em lista separada, com o rótulo literal "fraco — não decisivo";
- **zero sinais não vira "não é IA"** — a síntese nesse caso diz: "nenhum indício forte ou
  médio foi encontrado; a ausência de sinal **não prova** ausência de uso de IA".

## 4. BLOCO FINAL OBRIGATÓRIO — disclaimer verbatim do anexo watermark

Reproduza ao final de toda entrega, sem edição (fonte:
`context/watermark-anthropic-limites.md`, §5):

> **PODE dizer, honestamente:**
>
> "sinal heurístico probabilístico, nunca prova"
>
> **NUNCA pode dizer:**
>
> - "detectamos que isto foi escrito por IA";
> - "score de X% de probabilidade de IA" com precisão implícita;
> - "confirmamos a marca d'água da Anthropic" (a API não existe publicamente ainda).

## 5. Proibições explícitas (T3 — sem exceção, sem versão "resumida")

1. **Nunca** porcentagem, score ou número de probabilidade — em nenhum formato, nem "informal".
2. **Nunca** "detectamos que foi escrito por IA" nem sinônimos ("identificamos autoria por IA",
   "a peça foi gerada por IA").
3. **Nunca** "confirmamos a marca d'água" — a API de detecção não é pública; qualquer menção à
   marca d'água repete os limites do anexo, nunca os inventa.
4. **Nunca** "não é IA" / "descartamos uso de IA" — ausência de sinal não prova nada (limitação
   1 do anexo: modelos que não o Claude passam sem sinal nenhum).
5. A heurística **repete o anexo, nunca o extrapola**: se a informação não está em
   `context/watermark-anthropic-limites.md`, ela não sai daqui.

## Travas desta skill

- **T3 (a trava central):** sinal heurístico rotulado como tal, sempre — nunca score, nunca
  "detectamos", nunca "confirmamos a marca d'água"; as 5 proibições do §5 são parte da saída.
- **T5:** toda entrega fecha com o aviso: *análise assistida por IA — a avaliação final do
  conjunto de indícios e qualquer uso processual são responsabilidade exclusiva do advogado.*

**Cross-links:** consolidação no `dossie-de-integridade` · indícios fortes vêm de
`citacoes-da-peca-recebida` e `dispositivos-da-peca-recebida` · indício médio vem do
`classificador-prompt-injection` · base técnica: `context/watermark-anthropic-limites.md` ·
casos reais: `context/casos-ancora-sancoes.md`.
