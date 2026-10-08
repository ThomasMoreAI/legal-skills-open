---
name: acoes-de-massa-sbroggioadv
title: acoes-de-massa — a mesma tese mil vezes
description: 'A tese repetida contra o Estado — a mesma causa de pedir chegando em centenas ou milhares de processos. Trata o fenômeno como problema de gestão institucional, não como pilha de peças isoladas: (1) identificação do padrão, com o corte que separa massa real de coincidência; (2) uniformização da defesa por dentro, usando a arma anchorada da LINDB art. 30 — súmula administrativa com efeito vinculante interno — que se conecta diretamente ao CPC 496 §4º IV e dispensa a remessa necessária; (3) IRDR e pedido de suspensão, nomeados no CPC 496 §4º III mas com rito fora dos anexos, logo [VERIFICAR]; (4) a decisão estratégica que esta skill existe para tornar dizível — desistir, reconhecer ou parar de recorrer quando a tese do ente já caiu em repetitivo ou súmula, com o cálculo do custo de insistir pelas faixas escalonadas do CPC 85 §3º e §5º. Aciona: "temos 800 ações iguais", "tese repetida contra o ente", "vale a pena continuar recorrendo?", "IRDR contra demanda de massa", "uniformizar
  a defesa do órgão".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/acoes-de-massa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# acoes-de-massa — a mesma tese mil vezes

Este produto atende o **Estado**. Massa não é volume de trabalho: é **um problema de decisão
institucional que se manifesta como volume**. Enquanto a procuradoria responde processo a processo,
paga-se N vezes o custo de uma discussão só — e, quando a tese do ente já caiu, paga-se N vezes por
uma derrota conhecida.

Esta é a skill que torna dizível a decisão mais difícil da casa: **parar**.

## Quando esta skill entra

- A mesma causa de pedir aparece em série contra o Estado.
- Existe tese institucional aplicada em bloco e ninguém revisou desde que ela foi fixada.
- Chegou proposta de IRDR, ou o procurador quer avaliar suscitá-lo.
- A pergunta na mesa é se vale continuar contestando e recorrendo.

## 1. Identificar o padrão — antes de tratar como massa

Massa exige **três coincidências simultâneas**; duas não bastam:

| Eixo | Pergunta | Por que importa |
|---|---|---|
| **Causa de pedir** | O fundamento de fato e de direito é o mesmo, ou só o pedido se parece? | Pedidos iguais com fundamentos diversos **não** se defendem com peça única |
| **Polo passivo** | É sempre o mesmo órgão ou a mesma autoridade do Estado? | Define quem uniformiza e quem decide |
| **Ato de origem** | Há um ato, norma ou prática administrativa única gerando tudo? | Se há, a solução real é administrativa, não processual |

**O achado mais valioso desta análise raramente é processual.** Quando o eixo três aponta um ato ou
uma prática do próprio ente, a saída é corrigir a origem — e aí a matéria vira `parecer-consultivo`,
não peça. Continuar litigando contra o efeito de um ato que a própria casa pode revisar é a forma
mais cara de administrar massa.

Quantifique antes de decidir: número de processos, valor médio, taxa de êxito real do ente nos
últimos julgamentos, custo de honorários já suportado. Sem esses quatro números a discussão vira
opinião.

## 2. Uniformizar por dentro — a arma que tem lastro

Aqui a base está nos anexos e é a mais subaproveitada do produto.

**LINDB art. 30** (`context/lindb-20-30.md`, verbatim): *"As autoridades públicas devem atuar para
aumentar a segurança jurídica na aplicação das normas, inclusive por meio de regulamentos, súmulas
administrativas e respostas a consultas."* E o **parágrafo único**: *"Os instrumentos previstos no
caput deste artigo terão caráter vinculante em relação ao órgão ou entidade a que se destinam, até
ulterior revisão."*

**CPC art. 496 §4º IV** (`context/prerrogativas-cpc.md`, verbatim): não se aplica a remessa
necessária quando a sentença estiver fundada em *"entendimento coincidente com orientação vinculante
firmada no âmbito administrativo do próprio ente público, consolidada em manifestação, parecer ou
súmula administrativa."*

**A conexão é o ponto.** Súmula administrativa do próprio ente não é organização interna apenas: ela
**vincula o órgão** (LINDB 30, par. único) **e produz efeito processual direto** — sentença que a
acompanhe **dispensa a remessa necessária** (CPC 496 §4º IV). Em massa, isso significa milhares de
remessas a menos, sem nenhuma alteração legislativa. É o instrumento que transforma a decisão
institucional em economia processual mensurável.

Roteiro: consolidar a tese que vem vencendo (ou o reconhecimento, quando é o caso) em **parecer ou súmula
administrativa** aprovado pela autoridade competente → distribuir internamente como orientação
vinculante → citar essa orientação nas peças e nos pedidos de dispensa de remessa. O **art. 26** da
LINDB é o par disso quando a solução passa por compromisso com os interessados, celebrado *após
oitiva do órgão jurídico* — que é a própria procuradoria.

## 3. IRDR e pedido de suspensão

O **CPC art. 496 §4º III** nomeia o **incidente de resolução de demandas repetitivas** e o de
**assunção de competência**: sentença fundada em entendimento firmado em IRDR ou IAC **dispensa a
remessa necessária**. Esse é o lastro disponível — o **nome** e o **efeito na remessa**.

⚠️ `[VERIFICAR]`, porque **não consta dos anexos**: o rito do IRDR (dispositivos, requisitos de
admissibilidade), a **legitimidade do ente para suscitá-lo**, o alcance e o procedimento da
**suspensão dos processos**, o pedido de **suspensão nacional** e os prazos de cada etapa. Nada disso
sai de memória.

Critério prático de conveniência, que independe do dispositivo: o IRDR **fixa a tese para todos**.
Suscitá-lo com tese frágil converte derrotas dispersas em derrota vinculante e definitiva. Só peça o
incidente depois de rodar a tese pelo `suprema-corte-fazendaria` — e o resultado do gate, aqui, vale
mais do que em qualquer outra skill.

## 4. Parar — a decisão que esta skill existe para tornar dizível

**Trava P3, aplicada ao volume.** Quando a tese do ente já caiu em repetitivo ou súmula, insistir
não é zelo: é despesa previsível. O produto **avisa e propõe a linha viável** — e em massa a linha
viável tem quatro nomes possíveis:

1. **Deixar de recorrer** nos casos já perdidos, preservando o recurso só onde há distinção real de
   fato (*distinguishing* documentado, não alegado).
2. **Reconhecer o pedido** onde a tese caiu e o valor é baixo — o **CPC 85 §7º** (anexo) exclui
   honorários no cumprimento de sentença **não impugnado** que enseje precatório; impugnar por
   inércia cria a verba que a lei dispensaria.
3. **Uniformizar o reconhecimento** por súmula administrativa (item 2 acima), o que interrompe a
   entrada de novos processos e dispensa remessa nos existentes.
4. **Resolver na origem**, corrigindo o ato ou a prática administrativa — quando o eixo três da
   identificação apontou para dentro.

**O cálculo que sustenta a decisão** (CPC art. 85, verbatim no anexo): as faixas do **§3º** vão de
10-20% até 1-3%, e o **§5º** manda somar por degraus — faixa inicial e, no que exceder, a
subsequente, sucessivamente. Em massa, multiplique a estimativa **pelo número de processos** e leve
o total à autoridade. Uma tese perdida em 800 processos não custa uma sucumbência: custa 800. E o
**§6º** estende os limites à improcedência e à sentença sem resolução de mérito — não há saída
barata pela porta dos fundos.

**A analogia que vale, sem duplicar a skill vizinha:** a mesma lógica de eficiência que o **Tema
1184/STF** consagrou na execução fiscal de baixo valor — não faz sentido gastar mais para cobrar do
que se cobra — vale para a defesa em massa. O tratamento da esteira fiscal é do
`triagem-baixo-valor`; aqui fica só o princípio.

## 5. O que a defesa uniforme **não** pode virar

- **Peça-modelo sem leitura do caso.** Contestação padrão que ignora o fato concreto de um processo
  específico entrega esse processo e desgasta o órgão nos demais.
- **Preliminar em bloco por hábito.** Rejeitada em série, ensina o juízo a ler as peças do ente em
  diagonal.
- **Recurso automático.** Recorrer porque "sempre se recorre" é a definição operacional do problema
  que esta skill trata.

## Travas desta skill

- **P3** — é a skill em que a trava mais pesa: tese superada em massa multiplica o prejuízo pelo
  número de processos. Roda pelo `suprema-corte-fazendaria` **antes** de qualquer estratégia de
  volume, e o resultado do gate orienta desistir, reconhecer ou seguir.
- **P2** — o rito do IRDR, o pedido de suspensão e qualquer tema, súmula ou dispositivo fora dos
  anexos saem `[VERIFICAR]`. Com lastro, aqui: LINDB arts. 26 e 30; CPC 85 §§3º, 5º, 6º e 7º; CPC 496
  §4º I-IV; Tema 1184/STF (como princípio de eficiência, com os números do anexo).
- **P1** — tese de massa sobre **ICMS, IPVA, ITCMD e demais créditos estaduais** pertence a este produto; tese de massa sobre tributo
  de outra esfera não entra nem como exemplo comparativo.
- **P5** — massa de servidores: nada por analogia com o regime de outro ente, nem sobre honorários
  do procurador.
- **P7** — prazo em dobro só depois da checagem do CPC 183 §2º, inclusive em peça padronizada — é
  onde o erro se replica em série.
- **P4** — a análise sai completa, com revisão humana obrigatória; a decisão de desistir, reconhecer
  ou transigir é da autoridade competente, e o produto diz isso.

## Cross-links

`defesa-do-ente-contestacao` (a peça individual) · `parecer-consultivo` (súmula administrativa e
correção da origem) · `lindb-como-metodo` (arts. 26 e 30) · `prerrogativas-processuais` (CPC 496 §4º)
· `honorarios-da-fazenda` (o cálculo do custo de insistir) · `triagem-baixo-valor` (a mesma lógica de
eficiência, na esteira fiscal — não duplicar) · `saude-judicializada` (a massa mais comum) ·
`conformidade-ia-institucional` · `suprema-corte-fazendaria` (**QA obrigatória no fecho**) ·
`estilo-e-fronteiras`.
Fora da casa: `prisma-julgador-os` (o padrão do órgão que julga a série) · `civel-adv-os` ·
`juris-adv-os` (validação de citação).
