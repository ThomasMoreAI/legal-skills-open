---
name: precatorios-e-rpv-sbroggioadv
title: precatorios-e-rpv — a fila, as preferências, o teto de pagamento e a ressalva de atualização
description: 'Regime do art. 100 da CF: ordem cronológica, preferências alimentares (§§1º-2º), RPV (§§3º-4º), calendário da EC 136/2025 (§5º), sequestro (§6º), fracionamento (§8º), dívida ativa (§§9º-10) e limites do §23 por estoque em mora/RCL. TV2: o Provimento CNJ 207/2025 dá aplicação imediata aos limites, ressalvadas regulamentação e decisão do STF; o Parecer FONAPREC 65/2026 é complementar. Aciona: "precatório", "RPV", "ordem cronológica", "sequestro de verba", "EC 136", "limite de pagamento de precatório".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/precatorios-e-rpv
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: constitutional
language: pt
---

# precatorios-e-rpv — a fila, as preferências, o teto de pagamento e a ressalva de atualização

Precatório é onde a condenação vira orçamento. Esta skill trata o regime pela ótica do ente que
**paga**: o que a Constituição obriga, o que ela permite abater, e onde estão os limites novos da EC
136/2025 conforme a orientação administrativa vigente e suas ressalvas expressas.

Texto verbatim em `context/precatorios-cf100-ecs.md`. Este produto atende o **Estado**.

## ⚠️ Armadilhas de fonte, antes de qualquer citação

1. **O anexo traz só a redação vigente** e marca o que foi substituído como `[dispositivo
   revogado — omitido]`. **Nada adjacente a essa marca vira citação** — a do §5º é a da **EC
   136/2025** (**1º de fevereiro**); "1º de julho" (EC 62/2009) e "2 de abril" (EC 114/2021) são
   redações **revogadas**, cujo texto não está no anexo: como histórico, nunca como vigente.
2. **A página tem TRÊS "Art. 100"**: a de 1988 **revogada**, a vigente (esta) e a do **ADCT**.
3. **Remissões de controle** que a fonte apõe e o produto reproduz, tratando o dispositivo como
   `[VERIFICAR]` contra o julgado: **o caput**, o §10 e o §12 — **(Vide ADI 4425)**; o §9º e o
   §11 — **(Vide ADI 7047)** e **(Vide ADI 7064)**. O desfecho delas **não está** nos anexos.

## 1. A regra — caput e a fila

Os pagamentos devidos pelas Fazendas Públicas em virtude de sentença judiciária far-se-ão
**exclusivamente na ordem cronológica de apresentação dos precatórios** e à conta dos créditos
respectivos, **proibida a designação de casos ou de pessoas** nas dotações e nos créditos adicionais
abertos para esse fim. Quebrar a fila é o que autoriza o sequestro do §6º.

## 2. As duas preferências

| Preferência | Quem | Limite |
|---|---|---|
| **§1º — alimentícia** (redação da **EC 136/2025**) | débitos da **relação laboral ou previdenciária**, independentemente da natureza tributária, **inclusive repetição de indébito** sobre remuneração ou proventos, e indenizações por morte ou invalidez fundadas em responsabilidade civil, por sentença transitada em julgado | preferência sobre todos os demais, **exceto** os do §2º |
| **§2º — superpreferência** (**EC 94/2016**) | **débitos de natureza alimentícia** cujos titulares, originários ou por sucessão hereditária, tenham **60 anos**, **doença grave** ou sejam **pessoas com deficiência**, na forma da lei | até o **triplo** do valor fixado em lei para o §3º, **admitido fracionamento**; o restante segue a ordem cronológica |

A EC 136/2025 **reescreveu** a definição de crédito alimentar; o texto da redação anterior foi
omitido do anexo como revogado → `[VERIFICAR]`. Classificar pela redação velha erra a fila.

## 3. RPV — §§3º, 4º e 8º

O regime de precatório **não se aplica** às obrigações definidas **em leis** como de **pequeno
valor** (§3º). O §4º diz como esses valores nascem: **por leis próprias**, distintos por entidade
"segundo as diferentes capacidades econômicas", **sendo o mínimo igual ao valor do maior benefício
do regime geral de previdência social**.

⚠️ **P5 é literal aqui.** O teto de RPV do Estado depende de **lei do ente**, que **não está**
nos anexos: o produto **pergunta pela lei local** ou marca `[VERIFICAR]`, e nunca aplica por
analogia o teto de outro ente. Sem lei local, só se afirma o **piso constitucional** — e o valor do
maior benefício do RGPS também é `[VERIFICAR]`, por não constar do anexo.

**§8º** veda a expedição de precatório complementar ou suplementar de valor pago e o
**fracionamento, repartição ou quebra** do valor da execução para enquadrar parcela no §3º.
Fracionar para caber na RPV é exatamente o que o dispositivo proíbe.

## 4. Calendário, sequestro e responsabilidade

- **§5º (EC 136/2025):** obrigatória a inclusão no orçamento da verba dos precatórios apresentados
  **até 1º de fevereiro**, pagamento **até o final do exercício seguinte**, quando os valores são
  atualizados monetariamente. É a data que organiza o ciclo orçamentário do ente.
- **§6º:** dotações consignadas **diretamente ao Poder Judiciário**; o Presidente do Tribunal
  determina o pagamento integral e autoriza o **sequestro**, **a requerimento do credor** e só em
  dois casos — **preterimento** da precedência **ou não alocação orçamentária** do valor necessário.
- **§7º:** o Presidente do Tribunal que retardar ou **tentar frustrar** a liquidação regular incorre
  em **crime de responsabilidade** e responde perante o **CNJ**.

## 5. Abatimento de dívida ativa — §§9º e 10 (a ponte com a esteira fiscal)

O **§9º, na redação da EC 113/2021**, interessa diretamente a quem cobra: **sem interrupção no
pagamento** e **mediante comunicação da Fazenda ao Tribunal**, o valor dos débitos **inscritos em
dívida ativa** contra o credor do requisitório e seus substituídos **deverá ser depositado à conta
do juízo responsável pela ação de cobrança**, que decide o destino definitivo. Mudou a mecânica: não
é mais compensação automática na expedição, é **depósito à conta do juízo**.

O **§10** fixa o dever procedimental — o Tribunal solicita à Fazenda, **para resposta em até 30
dias, sob pena de perda do direito de abatimento**, informação sobre esses débitos. **Perder esse
prazo é perder crédito do ente**: é onde consultivo e dívida ativa têm de estar conectados.

Ainda no encontro de contas: **§11 (EC 113/2021)** — o credor pode oferecer créditos para quitar
débitos parcelados ou inscritos em dívida ativa, inclusive em transação (o caput do §11 tem
trecho omitido no anexo → `[VERIFICAR]` antes de transcrever); **§§13-14** — cessão,
eficaz só após comunicação ao Tribunal e ao ente.

## 6. ⚠️ §23 — os limites da EC 136/2025 e a trava TV2

O **§23** limita os pagamentos de precatórios **pelos Estados, pelo Distrito Federal e pelos
Municípios**, nas administrações direta e indireta, observados os §§24, 25, 26 e 28, a um percentual
da **receita corrente líquida apurada no exercício anterior**, escalonado pela razão entre o
**estoque de precatórios em mora** (atualizado e com juros, em 1º de janeiro) e essa RCL:

| Estoque em mora / RCL em 1º de janeiro | Limite |
|---|---|
| sem estoque, ou até 15% | **1%** (I) |
| acima de 15% até 25% | **1,5%** (II) |
| acima de 25% até 35% | **2%** (III) |
| acima de 35% até 45% | **2,5%** (IV) |
| acima de 45% até 55% | **3%** (V) |
| acima de 55% até 65% | **3,5%** (VI) |
| acima de 65% até 75% | **4%** (VII) |
| acima de 75% até 85% | **4,5%** (VIII) |
| acima de 85% | **5%** (IX) |

**Leia o rol do caput antes de aplicar:** o §23 nomeia **Estados, DF e Municípios**. Confira se
o Estado está literalmente nesse rol — não estando, o §23 **não é a régua** do ente atendido, e o
produto diz isso em vez de estender por analogia.

Os satélites: **§24** — majoração de **0,5 ponto percentual**, fixa para o decênio seguinte, a
partir de **1º/1/2036** e a cada 10 anos, havendo estoque em mora · **§25** — medida efetiva de
redução conta no plano anual · **§26** — pagamentos dos §§11 e 21 **não** entram no limite · **§28**
— o ente **pode pagar acima** do limite por dotação específica · **§29** — credor não pago em razão
dos §§20 ou 23 pode optar por **acordo direto** em Juízo Auxiliar de Conciliação, parcela única até
o fim do exercício seguinte, **com renúncia de parcela** · **§30** — valores aportados nas contas
especiais saem **imediatamente do estoque**, vedados juros e correção após a transferência.

**§27 — o preço de não liberar.** Não liberados tempestivamente os recursos, no todo ou em parte:
**(I)** os limites do §23 **ficam suspensos**; **(II)** o Presidente do TJ determina o **sequestro**
das contas do ente inadimplente; **(III)** o Governador ou o Prefeito responde na forma da
legislação de **responsabilidade fiscal e de improbidade administrativa**; **(IV)** o ente fica
**impedido de receber transferências voluntárias** enquanto perdurar a omissão. O §23 é teto de
pagamento, **não escudo contra a mora** — descumprir derruba o próprio teto.

### A trava TV2 — em toda saída sobre o §23, sem exceção

> O **Provimento CNJ 207/2025**, art. 5º, determina a **aplicabilidade imediata** dos limites do
> §23 e admite, a requerimento do ente, a revisão dos planos de pagamento de 2025. Pelo art. 1º,
> essa disciplina vale até ulterior regulamentação pela atualização da Resolução CNJ 303 e/ou
> decisão do STF.

O **Parecer FONAPREC 65/2026**, no PP público **0008461-14.2025.2.00.0000**, reforça a leitura de
validade e eficácia imediatas, mas é fonte complementar: não substitui o Provimento nem é decisão
final do PP. A saída aplica a orientação do Provimento e mantém a ressalva de regulamentação ou
decisão superveniente; qualquer consequência além disso recebe `[VERIFICAR]`.

## Travas desta skill

- **TV2 (a desta skill).** O §23 sai com Provimento CNJ 207/2025, aplicação imediata e ressalva de
  ulterior regulamentação/decisão do STF; o Parecer FONAPREC 65/2026 e o PP são fontes separadas.
- **P2 — nada sem lastro.** Todo dispositivo está em `context/precatorios-cf100-ecs.md`. Teto de
  RPV do ente, valor do maior benefício do RGPS, RCL e estoque do ente e desfecho das ADIs
  4425/7047/7064 **não estão** nos anexos → `[VERIFICAR]`.
- **Só o texto não marcado como revogado vale**; as remissões "(Vide ADI ...)" são reproduzidas.
- **P5.** Pequeno valor, plano anual e regime especial dependem de **lei do ente**: pergunta, nunca
  presume.
- **P1.** O art. 100 é norma constitucional comum às três esferas; nenhum tributo de esfera entra.
- **P4.** Fila, limite e cronograma aqui são estudo e minutação local — a conferência dos números do
  ente e a decisão orçamentária são do procurador e do gestor, indelegáveis.

**Próximo passo:** honorários no cumprimento que gera precatório (CPC 85 §7º) →
`honorarios-da-fazenda`. Crédito do ente contra o credor do precatório (§§9º-10) →
`execucao-fiscal-lef`. Toda entrega fecha por `suprema-corte-fazendaria`.
