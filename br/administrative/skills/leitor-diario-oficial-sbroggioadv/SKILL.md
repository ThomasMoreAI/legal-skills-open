---
name: leitor-diario-oficial-sbroggioadv
title: leitor-diario-oficial — extrai os atos que importam
description: 'Extrai do diário oficial já localizado os atos publicados que interessam à fiscalização — camada de suporte C2 do opositor-os (o produto é o roteamento, não a varredura). Lê e separa: portarias de nomeação, extratos de contrato e de dispensa/inexigibilidade, avisos e editais de licitação, termos aditivos, portarias de diárias, e RGF/RREO (LRF). De CADA ato guarda o lastro mínimo — URL + data + página/seção — que é a base das travas P1 (lastro) e P5 (fonte em toda alegação); sem esse lastro o ato não segue adiante. Não classifica vício (isso é do catalogador-vicios) nem roteia órgão (C3): entrega os atos crus e rastreados. Aciona: quando a fonte do diário já foi resolvida pelo localizador-diario-oficial e é preciso extrair os atos publicados relevantes para análise.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/leitor-diario-oficial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# leitor-diario-oficial — extrai os atos que importam

Com a fonte já resolvida pelo `localizador-diario-oficial`, esta skill **lê o diário e separa os atos
relevantes**, cada um com o lastro que o resto do produto exige. É **camada de suporte** (C2): não diz
se há vício (é o `catalogador-vicios`) nem para onde vai (é o `roteador-vicio-orgao` em C3). O que ela
garante é que **todo ato extraído já nasce rastreado** — sem isso, nenhuma peça pode ser gerada (P1/P5).

## Quando esta skill entra

- O `localizador-diario-oficial` já devolveu uma fonte concreta (URL, PDF ou seção).
- É preciso varrer uma edição (ou um intervalo) do diário e puxar os atos que interessam à fiscalização.
- O usuário colou o texto/PDF de um diário e quer que os atos relevantes sejam separados.

## O que é "ato relevante" — a grade de extração

Extraia e rotule cada ocorrência destes tipos (pesquisa §2.2 e §2.3). Cada tipo aponta para um vício
possível, checado depois pelo `catalogador-vicios`:

| Tipo de ato no diário | Como costuma aparecer | Aponta para (checar em `catalogador-vicios`) |
|---|---|---|
| **Portaria de nomeação** | "Nomeia FULANO para o cargo de..." | Nomeação sem concurso · nepotismo |
| **Extrato de contrato** | "Extrato de Contrato nº .../ano — Contratante/Contratado/objeto/valor" | Base de análise contratual |
| **Extrato/termo de dispensa ou inexigibilidade** | "Dispensa de Licitação nº..." / "Inexigibilidade nº..." | Dispensa/inexigibilidade fora de hipótese |
| **Aviso ou edital de licitação** | "Aviso de Licitação — Pregão/Concorrência nº..., abertura em DD/MM" | Edital restritivo — **atenção ao prazo fatal do art. 164** (abaixo) |
| **Termo aditivo** | "Extrato do 1º Termo Aditivo ao Contrato nº..." | Aditivo acima do limite legal |
| **Portaria de concessão de diárias** | "Concede X diárias a FULANO para viagem a..." | Diária/verba atípica |
| **RGF — Relatório de Gestão Fiscal** | Publicação **quadrimestral** obrigatória (LRF art. 54) | Estouro de gasto com pessoal (LRF arts. 19-20) |
| **RREO — Relatório Resumido da Execução Orçamentária** | Publicação **bimestral**, até 30 dias após o bimestre (LRF art. 52) | Ausência/atraso de publicação (LRF art. 48) |

**A ausência também é um dado.** Se o RREO ou o RGF **não** aparecem na edição/prazo esperado, isso é
um achado — a própria não-publicação é o vício (LRF art. 48). Registre a ausência com a mesma
disciplina de um ato presente: qual relatório, qual prazo legal, qual a janela verificada.

## Alerta de prazo — editais de licitação (não deixe o relógio correr)

Quando extrair um **aviso/edital de licitação**, capture **a data de abertura do certame** de forma
destacada. A única peça do catálogo com prazo **fatal e pré-clusivo** é a impugnação de edital: **até
3 (três) dias úteis ANTES da abertura** (Lei 14.133/2021, art. 164 — verbatim em
`context/lei-14133-recorte-fiscalizador.md`; TV5). Se a abertura está próxima, sinalize **imediatamente**
para o `opositor-master` disparar o `gerador-impugnacao-edital` — não espere a próxima rodada de análise.

## O lastro mínimo de cada ato (P1 e P5 — inegociável)

De **cada** ato extraído, guarde e devolva:

- **URL** da edição (ou "sem URL — PDF/mural", herdado do localizador);
- **data** da publicação;
- **página/seção** onde o ato consta;
- o **trecho literal** do ato (não parafraseie o número do contrato, o nome nomeado, o valor);
- o **ente** e o **tipo** de ato.

Esse conjunto é a base do lastro documental (P1) e do registro de fonte em toda alegação (P5): mais
adiante, nenhuma frase factual entra numa peça sem carregar essa referência. Ato sem os campos acima
segue marcado `[LASTRO INCOMPLETO]` — não é descartado, mas **não pode virar peça** até completar.

## Travas / limites

- **Não classifica vício.** Extrai e rotula o tipo de ato; se aquilo **é** vício e qual norma viola é
  do `catalogador-vicios`; para onde vai é do `roteador-vicio-orgao` (C3).
- **Não parafraseie o que é lastro.** Número de contrato, nome nomeado, valor, data de abertura — copie
  literal; erro aqui contamina a peça inteira.
- **Ato sem URL/data/página** → `[LASTRO INCOMPLETO]` (P1/P5): entra na fila, mas não gera peça.
- **Prazo de edital é fatal** — capture a data de abertura em destaque e sinalize na hora (TV5); os
  demais vícios não têm prazo de dias, o que empurra para monitoramento contínuo, não análise pontual.
- **Cobertura é parcial** (herda a limitação do `localizador-diario-oficial`): o que a fonte não
  alcança, não é lido — declare, não finja.
- Autoria "IA Combativa". Camada de suporte, não o produto: o produto é o roteamento com as travas de C4.
