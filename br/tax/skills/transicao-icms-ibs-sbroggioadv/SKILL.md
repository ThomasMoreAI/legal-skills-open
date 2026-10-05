---
name: transicao-icms-ibs-sbroggioadv
title: transicao-icms-ibs — o fim marcado do ICMS, e o que ele muda no trabalho de hoje
description: 'A skill dona do cronograma da EC 132/2023 + LC 214/2025 aplicado ao ICMS, com as duas camadas reconciliadas: 2026 ano-teste; 2027-2028 CBS à referência menos 0,1 p.p. e IBS 0,1%; em 2029-2032, participações IBS/ICMS-ISS de 10/90, 20/80, 30/70 e 40/60; **2033 extinção do ICMS**; e o texto que o executa dentro da própria Lei Kandir — o **art. 31-A, incluído pela LC 214/2025**, que reduz as alíquotas em 10%, 20%, 30% e 40% nos exercícios de 2029 a 2032 sobre as vigentes em 31/12/2028, alcança inclusive combustíveis monofásicos e as alíquotas das Resoluções 22/1989 e 13/2012 do Senado, e manda reduzir na mesma proporção os benefícios e incentivos fiscais. Responde o que acontece com a dívida ativa já constituída, o que a procuradoria precisa observar por exercício, e o que **não** foi coletado e sai como `[VERIFICAR]`. Aciona: "reforma tributária", "IBS", "CBS", "quando acaba o ICMS", "2033", "transição", "EC 132", "LC 214", "o que acontece com a execução".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/transicao-icms-ibs
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# transicao-icms-ibs — o fim marcado do ICMS, e o que ele muda no trabalho de hoje

O ICMS tem **data de extinção**. Isso não invalida nada do que se cobra em 2026 — mas muda parecer,
planejamento de carteira e qualquer projeção de receita. Esta skill é a **dona do cronograma** neste
plugin: as outras citam o aviso, aqui está o detalhe. Duas fontes, e as duas conferem entre si:
`context/reforma-tributaria-transicao.md` (o cronograma medido) e `context/lc-87-kandir.md` (o
**art. 31-A**, o texto legal que o executa).

Este produto atende o **Estado**.

**Quando entra:** em parecer que projete receita, renúncia ou contrapartida; ao opinar sobre
benefício fiscal; ao planejar a carteira de dívida ativa para os próximos exercícios; e sempre que
alguém perguntar se vale a pena discutir uma tese de ICMS que só se resolve depois de 2033.

## 1. O cronograma macro (`reforma-tributaria-transicao.md`)

A **EC 132/2023** e a **LC 214/2025** instituíram o **IBS** — competência **estadual e municipal** —
e a **CBS** — competência **federal** —, em substituição gradual ao ICMS e ao tributo municipal sobre
serviços.

| Ano | Situação |
|---|---|
| **2026** | **Ano-teste:** CBS **0,9%** + IBS **0,1%**, compensados com PIS/COFINS — **o ICMS segue cobrado normalmente** |
| **2027-2028** | CBS à alíquota de referência reduzida em **0,1 p.p.**; IBS **0,1%**; extinção de PIS/COFINS |
| **2029** | Participação IBS **10%**; participação ICMS/ISS **90%** |
| **2030** | Participação IBS **20%**; participação ICMS/ISS **80%** |
| **2031** | Participação IBS **30%**; participação ICMS/ISS **70%** |
| **2032** | Participação IBS **40%**; participação ICMS/ISS **60%** |
| **2033** | **Extinção do ICMS** |

**Fontes registradas:** `gov.br/receitafederal/.../reforma-tributaria-do-consumo/entenda`
(atualizada em **03/07/2026**) e LC 214/2025, arts. 344 e 347. Parecer que projeta receita cita a
fonte, não "a reforma".

## 2. O texto legal que executa a transição — art. 31-A da LC 87/96 (LC 214/2025)

O cronograma acima não é só política pública anunciada: a redução do ICMS **está escrita na Lei
Kandir**, e o dispositivo está no anexo verbatim.

**Caput:** "Em relação aos fatos geradores ocorridos de **1º de janeiro de 2029 a 31 de dezembro de
2032**, as alíquotas do imposto serão reduzidas nas seguintes proporções das alíquotas previstas nas
legislações dos Estados ou do Distrito Federal, **vigentes em 31 de dezembro de 2028**: I — **10%**,
em 2029; II — **20%**, em 2030; III — **30%**, em 2031; e IV — **40%**, em 2032."

**Duas leituras que o texto impõe, e que ninguém acerta de memória:**

1. **A base de referência congela em 31/12/2028.** A redução não incide sobre a alíquota do ano
   corrente: incide sobre a **vigente no último dia de 2028**. É esse o número que a Fazenda precisa
   ter documentado — e é o que faz de 2028 um exercício de registro, não só de operação.
2. **A redução é percentual da alíquota, não ponto percentual.** "Reduzidas em 10%" sobre uma
   alíquota de referência não é "menos 10 pontos". Confundir os dois erra a projeção por larga
   margem. O anexo da reforma descreve as participações macro de IBS/ICMS-ISS em **10/90, 20/80,
   30/70 e 40/60**; o art. 31-A descreve a **redução do ICMS** em proporção da própria alíquota. As duas leituras
   convivem — não se somam nem se substituem.

**§1º — o alcance é total.** Aplica-se "a todas as operações e prestações tributadas pelo imposto,
inclusive": **I** — aos combustíveis de incidência monofásica da **LC 192, de 11 de março de 2022**;
**II** — às alíquotas estabelecidas na **Resolução nº 22, de 19 de maio de 1989**, e na **Resolução
nº 13, de 25 de abril de 2012**, ambas do **Senado Federal**. Ou seja: alcança também as alíquotas
**interestaduais**.

**§§2º a 4º — os benefícios caem junto.** No período do caput, "os **benefícios ou os incentivos
fiscais ou financeiros** relativos ao imposto serão **reduzidos na mesma proporção**" (§2º); os
**percentuais e demais parâmetros** de cálculo do benefício também (§3º); e o §3º **não se aplica**
se o benefício **já tiver sido reduzido proporcionalmente** por força da redução de alíquotas (§4º —
a trava contra dupla redução).

**§§5º e 6º:** compete ao **CONFAZ** disciplinar a hipótese do §3º, com deliberações aprovadas por
**maioria simples** dos votos. **§7º:** os benefícios do **art. 3º da LC 160, de 7 de agosto de
2017**, são reduzidos **na forma deste artigo**, "não se aplicando a redução prevista no §2º-A do
art. 3º da referida Lei Complementar". Desdobramento em `guerra-fiscal-e-beneficios`.

## 3. O que acontece com a dívida ativa já constituída

Esta é a pergunta prática que mais chega, e a resposta é firme: **a extinção do tributo não extingue
o crédito**.

- O **fato gerador** rege-se pela lei do seu tempo. Crédito de ICMS constituído sobre fato gerador
  ocorrido antes da extinção continua **exigível**, e a execução fiscal corre pelo **rito da Lei
  6.830/80**, que a reforma não altera (`execucao-fiscal-lef`).
- A **CDA** continua válida, com a presunção **relativa** de certeza e liquidez do art. 3º da LEF, e
  os requisitos do art. 2º §5º (`divida-ativa-estadual`).
- O **art. 31-A é regra de alíquota do fato gerador do período**, não de anistia nem de remissão de
  crédito anterior. Nada no anexo autoriza tratar crédito antigo como reduzido pelo cronograma —
  afirmar isso seria inventar benefício.
- O que a transição **de fato** muda na carteira é o **horizonte de recuperação**: crédito que só se
  resolve em prazo longo, num tributo em extinção, entra na conta da `triagem-baixo-valor` junto com
  o custo de cobrança (**≈ R$ 9.277,00** por execução) — decisão de gestão, com números medidos.

## 4. O que a procuradoria precisa observar, por fase

| Fase | O que a procuradoria observa |
|---|---|
| **2026 (agora)** | ICMS exigível e cobrado normalmente. Todo conteúdo carrega o aviso de horizonte (P6). Estoque e carteira revisados com o cronograma à vista |
| **2027-2028** | **2028 é o exercício de registro:** documentar as alíquotas vigentes em **31/12/2028** — é a base de toda redução seguinte |
| **2029-2032** | Aplicar a redução do exercício (10/20/30/40%) e conferir se o benefício já caiu por via de alíquota (§4º). Acompanhar a disciplina do CONFAZ (§5º) |
| **2033** | ICMS **extinto**. Restam o passivo constituído, o contencioso pendente e o precatório — não a competência de exigir novos fatos geradores |

## 5. O que **não** foi coletado — sai como `[VERIFICAR]`

Nada além do que está nos dois anexos pode ser escrito de memória (P2). Em particular:

- **Alíquota final do IBS, alíquota de referência, trava de teto e split payment** — não coletados
  pela pesquisa → `[VERIFICAR]`.
- **Dispositivos da LC 214/2025** fora dos que o anexo da Kandir reproduz: a pesquisa confirmou a
  **existência** da lei e o **cronograma**, **não** capturou seu articulado. Citar "art. X da LC
  214/2025" sem conferir na fonte é violação de P2.
- **Regras de repartição de receita do IBS, comitê gestor, regimes específicos e o destino do
  contencioso administrativo estadual após 2033** → `[VERIFICAR]`.
- **A competência do IBS é estadual e municipal**, e a da CBS é federal: a CBS aparece aqui só como
  contraparte do cronograma. Conteúdo federal substantivo é do `procurador-federal-os` (P1).

## Travas desta skill

- **P6 — esta skill é a dona da trava.** As demais skills de ICMS fecham com o aviso; aqui está o
  cronograma completo. O aviso é de **horizonte, não de invalidade**: em 2026 o imposto é exigível e
  a execução corre normalmente. **TV3** recusa qualquer texto que trate o ICMS como permanente.
- **P2.** Anos, percentuais e o texto do art. 31-A estão nos anexos; tudo o mais → `[VERIFICAR]`.
  Nenhum arredondamento e nenhuma extrapolação sobre os números da tabela.
- **P1.** O cronograma aqui trata do **ICMS**. O efeito sobre o tributo do Município é do
  `procurador-municipal-os`; a CBS e a matéria federal, do `procurador-federal-os`.
- **P3.** Tese que dependa de como os tribunais vão tratar a transição não tem lastro em repetitivo
  hoje: `suprema-corte-fazendaria` antes de sustentá-la, e postura honesta sobre a incerteza.
- **P5.** As alíquotas de referência de 31/12/2028 e os benefícios a reduzir são **direito estadual**
  — o produto pergunta pelo texto local, não presume.
- **P4.** Isto é estudo e minutação local; a projeção que vai a ato de gestão e a responsabilidade
  são do procurador, indelegáveis.

**Próximo passo:** regra do imposto → `icms-conteudo`; benefício e CONFAZ →
`guerra-fiscal-e-beneficios`; carteira e crédito constituído → `divida-ativa-estadual` e
`triagem-baixo-valor`; rito → `execucao-fiscal-lef`. Fecha por `suprema-corte-fazendaria`, com o
`validador-fazendario-vigente` antes.
