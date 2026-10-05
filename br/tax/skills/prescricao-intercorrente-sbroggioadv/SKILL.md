---
name: prescricao-intercorrente-sbroggioadv
title: prescricao-intercorrente — a linha do tempo que corre sozinha, e o que ainda dá para salvar
description: 'Art. 40 da LEF, Temas 566-571/STJ (REsp 1.340.553/RS) e Súmula 314. Monta a linha do tempo: o ano de suspensão começa da ciência da Fazenda, sem decisão expressa; depois corre o prazo aplicável. Citação efetiva, inclusive editalícia, ou constrição efetiva interrompe; mero pedido não. Para nulidade, exige prejuízo, salvo falta da intimação do termo inicial, quando é presumido. Fecha com checklist defensivo. Aciona: "prescrição intercorrente", "art. 40 da LEF", "execução arquivada", "Tema 568", "Tema 571", "Súmula 314", "prescrição de ofício".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/prescricao-intercorrente
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# prescricao-intercorrente — a linha do tempo que corre sozinha, e o que ainda dá para salvar

Esta é a skill em que **vender a verdade custa caro e vale mais**. Os Temas 566-571 são as teses que mais
derruba execução fiscal, e o papel do produto aqui é dizer ao procurador **onde o prazo já correu**
— não construir argumento para negar o que a lei e o repetitivo já resolveram. Insistir contra o
repetitivo produz a peça perdedora; identificar cedo o que prescreveu libera estrutura para cobrar o
que ainda se cobra.

Lastro: `context/lef-6830.md` (art. 40) e `context/temas-e-sumulas-fazendarios.md` (Temas 566-571 e
Súmula 314). Este produto atende o **Estado**.

## 1. O texto da lei — art. 40 da LEF, verbatim

- **Caput:** "O Juiz suspenderá o curso da execução, enquanto não for localizado o devedor ou
  encontrados bens sobre os quais possa recair a penhora, e, nesses casos, não correrá o prazo de
  prescrição."
- **§1º:** suspenso o curso, "será aberta vista dos autos ao representante judicial da Fazenda
  Pública".
- **§2º:** "Decorrido o prazo máximo de 1 (um) ano, sem que seja localizado o devedor ou encontrados
  bens penhoráveis, o Juiz ordenará o arquivamento dos autos."
- **§3º:** encontrados, a qualquer tempo, o devedor ou os bens, os autos são **desarquivados** para
  prosseguimento.
- **§4º (Lei 11.051/2004):** decorrido o prazo prescricional desde a decisão que ordenou o
  arquivamento, o juiz, **depois de ouvida a Fazenda Pública**, pode **de ofício** reconhecer a
  prescrição intercorrente e decretá-la de imediato.
- **§5º (Lei 11.960/2009):** a manifestação prévia da Fazenda do §4º é **dispensada** em cobranças
  judiciais de valor inferior ao mínimo fixado por ato do Ministro de Estado da Fazenda.

**Ler o texto sozinho não basta** — e este é o ponto que o anexo faz questão de marcar. O caput diz
"não correrá o prazo" e o §2º fala em "decorrido o prazo máximo de 1 ano", mas **quem** fixa quando
o ano começa e **o que** interrompe é o repetitivo, não a lei.

## 2. O repetitivo — Temas 566-571/STJ e Súmula 314/STJ

| Campo | Dado |
|---|---|
| Temas | **Temas 566-571/STJ** — recurso repetitivo |
| Leading case | **REsp 1.340.553/RS** |
| Relator | Min. **Mauro Campbell Marques** |
| Objeto | art. 40 e parágrafos da LEF — contagem da suspensão e da prescrição intercorrente |

**Súmula 314/STJ**, consolidada por esse repetitivo: execução fiscal paralisada por 1 ano sem
localização de bens → inicia-se o prazo **quinquenal** de prescrição intercorrente.

### Síntese operacional dos itens 4.1 a 4.5

1. **4.1:** o ano de suspensão começa automaticamente da ciência da Fazenda sobre a não localização
   do devedor ou de bens, sem depender de decisão expressa; o juiz deve declarar a suspensão. As
   sub-hipóteses dependem da natureza do crédito e do marco da LC 118/2005.
2. **4.2:** findo o ano, inicia-se automaticamente o prazo prescricional aplicável à natureza do
   crédito, com arquivamento sem baixa; ao fim, o juiz pode reconhecer a prescrição após ouvir a
   Fazenda.
3. **4.3 / Tema 568:** constrição efetiva ou citação efetiva, inclusive por edital, interrompe; mero
   requerimento não. Requerimento protocolado dentro da soma do ano de suspensão com o prazo
   prescricional deve ser processado mesmo depois: se produzir a providência efetiva, a interrupção
   **retroage à data do protocolo da petição frutífera**.
4. **4.4 / Tema 571:** a nulidade por falta de intimação exige prejuízo concreto, salvo falta da
   intimação que constitui o termo inicial, quando o prejuízo é presumido.
5. **4.5:** a decisão que reconhece a prescrição deve delimitar os marcos legais da contagem,
   inclusive o período de suspensão.

⚠️ **Regra de uso:** número dos temas, número do REsp e nome do relator **podem ir para a peça**.
A síntese pode ser referida pelo conteúdo acima. **Ementa e
teor literal do acórdão: conferir na fonte primária (`stj.jus.br`) antes de transcrever entre
aspas** — a pesquisa registrou o sentido, não a redação oficial. O mesmo vale para a Súmula 314: o
número vai, a **redação literal se confere antes**.

## 3. A linha do tempo, montada

```
ciência da Fazenda sobre não localização do devedor OU dos bens   ← marco zero (item 4.1)
        │  (não depende de despacho: o despacho é declaratório)
        ├── 1 ANO de suspensão .......................... art. 40 §§1º-2º
        │
        └── PRAZO PRESCRICIONAL APLICÁVEL ............... automático (item 4.2)
                │
                └── CITAÇÃO ou CONSTRIÇÃO EFETIVA interrompe (Tema 568)
                        citação por edital conta; mero pedido, sozinho, não
                        pedido tempestivo depois frutífero → retroage ao protocolo
```

**Como aplicar a um processo concreto**, na ordem — e cada item é uma pergunta ao procurador, não
uma presunção do produto:

1. **Qual foi a data da ciência** da Fazenda sobre a não localização (do devedor **ou** dos bens)?
   É o marco zero. Sem essa data nos autos, o produto **pergunta**; não a estima.
2. **Passou 1 ano** dessa ciência sem localizar devedor ou bens penhoráveis? → começou o prazo
   prescricional aplicável à natureza do crédito, ainda que não haja despacho de arquivamento.
3. **Dentro da soma do ano de suspensão com o prazo prescricional houve citação/constrição efetiva
   ou requerimento que depois se tornou frutífero?** Pedido infrutífero não basta; se a providência
   requerida tempestivamente se efetiva depois, a interrupção retroage ao protocolo.
4. **Esgotou-se o prazo aplicável sem providência efetiva nem requerimento tempestivo depois
   frutífero?** O juiz pode reconhecer a prescrição de ofício, depois de ouvir a Fazenda; deve
   delimitar os marcos da contagem. O prazo é o aplicável à natureza do crédito, não sempre cinco
   anos; neste produto, prazo diverso do tributário sai `[VERIFICAR]`.

## 4. A alegação de nulidade — o que o item 4.4 exige

Alegar que faltou intimação do despacho de suspensão ou de arquivamento exige, em regra, que a
Fazenda **demonstre prejuízo concreto**. A exceção do Tema 571 é a falta de intimação do **termo
inicial**, quando o prejuízo é presumido. Traduzindo em ônus:

| Alegação | Suficiente? |
|---|---|
| "Não fui intimada do despacho de arquivamento" | **Não**, sozinha |
| "Não fui intimada **e**, tivesse sido, teria indicado o bem X / o endereço Y / a diligência Z que se mostrou frutífera" | É a forma que atende ao item 4.4 — prejuízo **concreto** e nomeado |
| "Não fui intimada do termo inicial" | O prejuízo é **presumido**; identificar nos autos qual ato constituiu o termo inicial |
| "Houve nulidade porque o despacho não foi expresso" | **Não** — o item 4.1 diz que a contagem independe de decisão judicial expressa |

Se não houver prejuízo concreto a apontar, o produto **diz isso** ao procurador. É a postura P3
aplicada: avisar antes que a peça saia, não depois que o tribunal negar.

## 5. Checklist defensivo do exequente (o que ainda dá para fazer)

Onde o prazo **ainda não** se consumou, estas são as ações que a própria linha do tempo indica:

- [ ] **Protocolar e acompanhar a providência frutífera dentro do prazo.** O Tema 568 inclui citação
      efetiva, inclusive editalícia, e constrição; quando o pedido tempestivo produz resultado, a
      interrupção retroage ao protocolo. Registre pedido e resultado na linha do tempo.
- [ ] **Mapear a data de ciência** de cada execução da carteira. O marco zero é dado de gestão, não
      de peça: sem ele, não há como saber quais processos estão em risco.
- [ ] **Usar o §3º:** localizado o devedor ou o bem a qualquer tempo, requerer o **desarquivamento**
      — o arquivamento do §2º não é fim de processo.
- [ ] **Registrar o prejuízo concreto** no momento em que ele existir, para que a alegação do item 4.4
      não nasça genérica.
- [ ] **Cruzar com a triagem.** Processo em que o prazo correu **e** cujo valor está abaixo do custo
      de cobrança não é caso de recurso: é caso de reconhecer e liberar estrutura
      (`triagem-baixo-valor`). O §5º do art. 40 já dispensa a oitiva prévia nas cobranças de valor
      inferior ao mínimo — a lógica de baixo valor está dentro da própria LEF.
- [ ] **Prevenir na origem:** o que evita a intercorrente é qualificar a inscrição e o endereço
      antes de ajuizar (`execucao-fiscal-lef`, art. 2º §5º) e cobrar antes pela via extrajudicial
      (`protesto-e-cobranca-extrajudicial`).

## Travas desta skill

- **P3 — a trava desta skill.** Os Temas 566-571 são teses que trabalham contra o ente, e o produto os
  usa para **dizer onde o prazo já correu**, nunca para negá-lo. Tese superada avisada com o número,
  seguida da linha viável.
- **P2 — nada sem lastro.** Art. 40 de `context/lef-6830.md`; Temas 566-571, REsp, relator e Súmula 314
  de `context/temas-e-sumulas-fazendarios.md`. **Ementa e redação de súmula só depois de conferidas
  na fonte primária.** Valor mínimo do ato do Ministro (§5º), datas dos autos e qualquer outro
  precedente → `[VERIFICAR]`.
- **P7.** Os prazos do rito são de lei específica; o dobro do CPC 183 não é automático aqui —
  `prerrogativas-processuais`.
- **P1.** Prescrição intercorrente é matéria processual comum às três esferas; o crédito é de
  ICMS, IPVA, ITCMD e demais créditos estaduais.
- **P4.** A contagem aqui é estudo; conferir as datas nos autos e decidir o que alegar é do
  procurador, indelegável.

**Próximo passo:** o processo segue vivo → `execucao-fiscal-lef`. O devedor sumiu e há sócio →
`redirecionamento-socios`. O crédito não paga o custo de cobrar → `triagem-baixo-valor`. Toda
entrega fecha por `suprema-corte-fazendaria`.
