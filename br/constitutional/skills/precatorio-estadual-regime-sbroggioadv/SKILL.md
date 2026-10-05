---
name: precatorio-estadual-regime-sbroggioadv
title: precatorio-estadual-regime — o pagamento do Estado sob teto, com a ressalva de atualização
description: 'O art. 100 da Constituição aplicado ao Estado, com o texto verbatim do anexo: ordem cronológica e a vedação de designar casos ou pessoas (caput), as duas preferências — a alimentar, **na redação nova da EC 136/2025**, e a de 60 anos, doença grave ou deficiência, até o triplo do teto de pequeno valor (§§1º-2º) —, a RPV estadual com o piso do maior benefício do RGPS e a vedação de fracionamento (§§3º-4º e 8º), o calendário de apresentação **deslocado para 1º de fevereiro pela EC 136/2025** (§5º) e a compensação com débitos inscritos em dívida ativa (§9º). O núcleo é o **§23**, incluído pela EC 136/2025: os nove degraus de limite de pagamento, de 1% a 5% da receita corrente líquida conforme o estoque em mora — com a **TV2 obrigatória**: aplicação imediata segundo o Provimento CNJ 207/2025, ressalvadas ulterior regulamentação e decisão do STF. Aciona: "precatório", "RPV", "ordem cronológica", "preferência alimentar", "limite de pagamento", "EC 136", "plano anual".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/precatorio-estadual-regime
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: constitutional
language: pt
---

# precatorio-estadual-regime — o pagamento do Estado sob teto, com a ressalva de atualização

O chassi trata o precatório como prerrogativa e regime geral (`precatorios-e-rpv`). Esta skill trata
do que é **do Estado**: os limites do §23, o calendário, os regimes especiais e as sanções. Todo
dispositivo sai de `context/precatorios-cf100-ecs.md`. Este produto atende o **Estado**.

**Quando entra:** ao organizar o pagamento e o plano anual; na impugnação por preterimento; ao
avaliar acordo direto; ao instruir o abatimento de dívida ativa; e sempre que a pergunta envolver
**quanto** o Estado precisa pagar no exercício.

## ⚠️ A TV2 — obrigatória em toda menção ao §23

> O **§23, incluído pela EC 136/2025**, é o dispositivo central desta skill. O **Provimento CNJ
> 207/2025**, art. 5º, atribui aplicação imediata aos seus limites e admite revisão dos planos de
> 2025 a requerimento do ente; pelo art. 1º, vale até ulterior atualização da Res. CNJ 303 e/ou
> decisão do STF.

O **Parecer FONAPREC 65/2026**, no PP público **0008461-14.2025.2.00.0000**, é fonte complementar,
não decisão final. A saída aplica o Provimento e mantém sua ressalva expressa
(`context/travas-defasagem.md`, TV2).

## 1. A ordem e as duas preferências

**Caput (EC 62/2009):** os pagamentos devidos pelas Fazendas "far-se-ão **exclusivamente na ordem
cronológica de apresentação dos precatórios** e à conta dos créditos respectivos, **proibida a
designação de casos ou de pessoas** nas dotações orçamentárias e nos créditos adicionais abertos
para este fim". O anexo traz aqui "(Vide ADI 4425)" → `[VERIFICAR]` antes de tese sobre a EC 62 (P3).

**§1º — natureza alimentícia, na redação da EC 136/2025.** Compreende os débitos "decorrentes da
**relação laboral ou previdenciária, independentemente da sua natureza tributária**, inclusive os
oriundos de **repetição de indébito incidente sobre remuneração ou proventos de aposentadoria**", e
as indenizações por morte ou invalidez fundadas em responsabilidade civil; pagos com preferência
sobre todos os demais, exceto os do §2º. **É redação nova**, e mais ampla que a anterior (EC
62/2009), que listava verbas nominadas — classificar pela lista antiga é erro de defasagem.

**§2º (EC 94/2016) — a superpreferência.** Titulares **de débito alimentar**, originários ou por
sucessão hereditária, com **60 anos**, **doença grave** ou **deficiência**, na forma da lei: até o **triplo**
do fixado para o §3º, **admitido o fracionamento**; o restante segue a ordem cronológica.

## 2. RPV estadual — §§3º, 4º e 8º

**§3º:** a exigência de precatório **não se aplica** às obrigações definidas **em leis** como de
**pequeno valor**. **§4º:** esses valores são fixados **por leis próprias**, distintos por entidade
"segundo as diferentes capacidades econômicas", **sendo o mínimo igual ao valor do maior benefício
do regime geral de previdência social**.

Duas leituras: o teto de RPV é **lei do Estado** — sem ela, `[VERIFICAR]` (P5); e tem **piso
constitucional**, o maior benefício do RGPS. Lei estadual abaixo desse piso é o primeiro ponto a
conferir quando o credor questiona o enquadramento.

**§8º:** é **vedada** a expedição de precatório complementar ou suplementar de valor pago, "bem como
o **fracionamento, repartição ou quebra** do valor da execução para fins de enquadramento de parcela
do total ao que dispõe o §3º" — o fracionamento só cabe no §2º.

## 3. O calendário — §5º, na redação da EC 136/2025

É obrigatória a inclusão no orçamento de verba para os precatórios **apresentados até 1º de
fevereiro**, com pagamento **até o final do exercício seguinte**, atualizados monetariamente.

**Anti-defasagem:** a data mudou duas vezes — **1º de julho** (EC 62/2009) → **2 de abril** (EC
114/2021) → **1º de fevereiro** (EC 136/2025). Citar as duas primeiras hoje é errar o próprio
calendário de provisionamento do Estado.

## 4. ⭐ O §23 — os nove degraus do limite (EC 136/2025)

Os pagamentos de precatórios pelos **Estados**, DF e Municípios, nas administrações direta e
indireta, "estão limitados, observado o disposto nos §§ 24, 25, 26 e 28", a um percentual da
**receita corrente líquida apurada no exercício anterior**, definido pela razão entre o **estoque de
precatórios em mora** (atualizado e com juros moratórios, **em 1º de janeiro**) e essa receita:

**I — 1%:** sem estoque, ou estoque **até 15%** · **II — 1,5%:** > 15% e ≤ 25% · **III — 2%:** > 25%
e ≤ 35% · **IV — 2,5%:** > 35% e ≤ 45% · **V — 3%:** > 45% e ≤ 55% · **VI — 3,5%:** > 55% e ≤ 65% ·
**VII — 4%:** > 65% e ≤ 75% · **VIII — 4,5%:** > 75% e ≤ 85% · **IX — 5%:** > 85%.

**§24:** esses limites **serão majorados** em **0,5 ponto percentual**, de forma fixa para o decênio,
**a partir de 1º de janeiro de 2036** e a cada **10 anos**, se houver estoque em mora.

**§25:** **toda medida efetiva de redução de estoque** promovida pelo Estado "deverá ser
contabilizada para fins de apuração do cumprimento do respectivo **plano anual de pagamento**".
**§26:** os pagamentos dos §§11 e 21 **não** contam para os limites. **§28:** o Estado pode,
**mediante dotação orçamentária específica**, pagar **acima** dos limites do §23.

## 5. O que acontece se os recursos não forem liberados — §27

Não liberados tempestivamente os recursos observados os limites do §23: **I** — os limites **ficam
suspensos**; **II** — o **Presidente do Tribunal de Justiça local determina o sequestro**, até o
valor devido, das contas do ente inadimplente; **III** — o **Governador** responde na forma da
legislação de **responsabilidade fiscal e de improbidade administrativa**; **IV** — o ente fica
**impedido de receber transferências voluntárias** enquanto perdurar a omissão.

Some-se o **§6º** (sequestro por **preterimento** da precedência **ou por não alocação
orçamentária**) e o **§7º** (o Presidente do Tribunal que retardar ou frustrar a liquidação incorre
em **crime de responsabilidade** e responde perante o **CNJ**). O §23 não é só teto: seu
descumprimento aciona sequestro e responsabilização pessoal do Chefe do Executivo.

## 6. Saídas: acordos, regime especial e compensação

- **§20 (EC 94/2016) — o precatório de grande porte.** Precatório superior a **15%** do montante dos
  apresentados nos termos do §5º: **15%** dele pagos até o final do exercício seguinte e o restante
  em **cinco parcelas** iguais, com juros e correção — **ou** acordo direto, perante Juízos
  Auxiliares de Conciliação, com **redução máxima de 40%** do crédito atualizado, desde que não penda
  recurso e observada a regulamentação do ente.
- **§29 (EC 136/2025) — o acordo do credor não pago.** O credor não pago em razão dos §§20 ou 23
  pode optar por **acordo direto** perante Juízos Auxiliares de Conciliação, **em parcela única, até
  o final do exercício seguinte, com renúncia de parcela do crédito**.
- **§15:** **lei complementar** pode estabelecer **regime especial** de pagamento para Estados, DF e
  Municípios, com vinculações à receita corrente líquida e forma e prazo de liquidação. **§16:** a
  União pode **assumir e refinanciar** esses débitos, a seu critério e na forma de lei.
- **§§9º e 10 — a ponte com a dívida ativa, com prazo fatal.** Pelo **§9º (EC 113/2021)**, "sem que
  haja interrupção no pagamento", o valor dos "**eventuais débitos inscritos em dívida ativa** contra
  o credor do requisitório e seus substituídos" é **depositado à conta do juízo responsável pela ação
  de cobrança**, que decide seu destino. O **§10** é o que a procuradoria não pode perder: **antes**
  da expedição, o Tribunal solicita à Fazenda devedora, "para resposta em até **30 (trinta) dias**,
  **sob pena de perda do direito de abatimento**", informação sobre esses débitos. Prazo perdido é
  abatimento perdido — levantamento com `divida-ativa-estadual`. As remissões **"(Vide ADI
  7047/7064)"** no §9º e **"(Vide ADI 4425)"** no §10 → `[VERIFICAR]` antes de tese sobre o
  mecanismo (P3).
- **§11 (EC 113/2021):** **conforme lei do ente devedor**, o credor pode ofertar o crédito para
  **quitar débitos parcelados ou inscritos em dívida ativa** do ente (I) e **comprar imóveis
  públicos** dele (II) — e isso **não conta** para os limites (§26).

## Travas desta skill

- **TV2 — a trava desta skill.** Toda menção ao §23 declara a disputa no CNJ (PP
  0008461-14.2025.2.00.0000). Nunca "pacificado", "consolidado" ou "vigente desde a promulgação"
  como fato.
- **P2.** Caput e §§1º-11, 15, 16 e 20-29 estão em `context/precatorios-cf100-ecs.md`. Valor do maior
  benefício do RGPS, teto de RPV do Estado, ementa de ADI e ato do CNJ **não** estão →
  `[VERIFICAR]`.
- **P5.** Teto de RPV e regulamentação dos acordos são **lei do Estado** — sem o texto, o produto
  pergunta; a Constituição garante só o **piso** do §4º.
- **P3.** As remissões a ADI no anexo e a disputa do §23 vão ao gate `suprema-corte-fazendaria`
  antes de qualquer tese sobre o regime de pagamento.
- **P1.** Regime de pagamento do **Estado** — o do Município é do `procurador-municipal-os` e o da
  União, do `procurador-federal-os`; o §23 alcança Estados, DF e Municípios, não a União.
- **P4.** Dado de credor é pessoal e fica no ambiente do órgão; a decisão de pagamento e a
  responsabilidade são do procurador e do gestor, indelegáveis.

**Próximo passo:** regime geral e RPV → `precatorios-e-rpv`; passivo do credor →
`divida-ativa-estadual`; condenação de origem → `defesa-do-ente-contestacao`; consequência para o
gestor → `defesa-no-tce-estadual`. Fecha por `suprema-corte-fazendaria`, com o
`validador-fazendario-vigente` antes.
