---
name: redirecionamento-socios-sbroggioadv
title: redirecionamento-socios — a súmula abre, os temas delimitam, e dois deles fecham
description: 'Redirecionamento da execução fiscal contra sócio e sucessor com a rede completa, não só a porta de entrada: Súmula 435/STJ (presunção de dissolução irregular quando a empresa deixa de funcionar no domicílio fiscal sem comunicar) mais os cinco temas que a delimitam — 630 (a dissolução irregular basta), 981 (atinge quem tinha poder de administração NA DATA da dissolução, ainda que sem gerência no fato gerador) e 1.049 (sucessão por incorporação não informada permite redirecionar sem alterar a CDA), que ABREM; contra 962 (não se redireciona contra quem se retirou regularmente antes) e 97 (para atingir quem se retirou é preciso provar excesso de poderes ou infração à lei), que FECHAM. Entrega tabela cenário → cabe redirecionar? → base. Aciona: "redirecionar", "sócio-gerente", "dissolução irregular", "Súmula 435", "Tema 981", "sucessão empresarial".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/redirecionamento-socios
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# redirecionamento-socios — a súmula abre, os temas delimitam, e dois deles fecham

O erro caro aqui não é deixar de redirecionar: é pedir **com a súmula sozinha**. A Súmula 435 é a
porta; os Temas 630, 981 e 1.049 dizem **quem** cabe atingir; e os Temas 962 e 97 dizem **quem não
cabe**. Pedido que pula os dois de fechamento volta indeferido, com o custo de tempo do juízo e da
procuradoria.

Lastro integral: `context/temas-e-sumulas-fazendarios.md`. Este produto atende o **Estado**.

## 1. A porta — Súmula 435/STJ

**Sentido registrado no anexo:** presunção de **dissolução irregular** quando a empresa **deixa de
funcionar no domicílio fiscal sem comunicar** aos órgãos competentes.

Dois elementos, e os dois precisam estar demonstrados: **(a)** deixou de funcionar no domicílio
fiscal; **(b)** **sem comunicar** aos órgãos competentes. A certidão do oficial de justiça que
atesta o não funcionamento no endereço cadastrado é o meio típico — mas é o par (a)+(b) que
constitui a presunção, não a certidão isolada.

⚠️ **O número pode ir para a peça. A redação literal do enunciado deve ser conferida na fonte
(`stj.jus.br`) antes de qualquer transcrição entre aspas** — o anexo capturou o sentido, não o texto
oficial. E a súmula **nunca** é usada sozinha para atingir qualquer sócio: a rede abaixo é filtro
obrigatório.

## 2. A rede completa — os cinco temas

Todos confirmados em `stj.jus.br`; a matéria foi noticiada em **fevereiro/2024** e segue citada como
referência corrente.

| Tema | O que PERMITE | O que VEDA / exige |
|---|---|---|
| **630** | A **dissolução irregular basta** para redirecionar | — |
| **981** | Atinge quem tinha **poder de administração NA DATA da dissolução**, mesmo **sem gerência no fato gerador** | — |
| **1.049** | Sucessão por **incorporação não informada ao fisco** permite redirecionar **sem alterar a CDA** | — |
| **962** | — | **Não pode** redirecionar contra quem se retirou **regularmente** antes da dissolução |
| **97** | — | Para atingir quem se retirou, é **preciso provar excesso de poderes / infração à lei** |

**A leitura obrigatória do conjunto:** **630, 981 e 1.049 abrem; 962 e 97 fecham.** Os três primeiros
respondem "há base?"; os dois últimos respondem "contra esta pessoa, especificamente, cabe?". As
duas perguntas são distintas, e o pedido só se sustenta quando as duas foram feitas.

**O que o Tema 981 muda na prática:** desloca o marco temporal do **fato gerador** para a **data da
dissolução**. Quem administrava quando o tributo nasceu, mas já havia saído regularmente quando a
empresa fechou as portas, não é alcançado por esse fundamento — e quem entrou depois do fato gerador
mas administrava na data da dissolução, é. A pergunta certa não é "quem era sócio quando o tributo
venceu?", é **"quem tinha poder de administração na data da dissolução?"**.

**O que o Tema 1.049 dispensa:** a alteração da CDA, no caso específico de **incorporação não
informada ao fisco**. É dispensa pontual, ligada àquela hipótese — não é autorização geral para
redirecionar sem mexer no título em qualquer sucessão.

## 3. Tabela — cenário → cabe redirecionar? → base

| Cenário | Cabe? | Base |
|---|---|---|
| Empresa deixou de funcionar no domicílio fiscal **sem comunicar**; o sócio **administrava na data da dissolução** | **Sim** | Súm. 435 + Temas 630 e 981 |
| Sócio **administrava na data da dissolução**, mas **não tinha gerência no fato gerador** | **Sim** — o marco é a data da dissolução | Tema 981 |
| Sócio **se retirou regularmente antes** da dissolução | **Não**, por esse fundamento | Tema 962 |
| Sócio que se retirou, e há indício de **excesso de poderes ou infração à lei** | Só **provando** o excesso/infração — não presumido | Tema 97 |
| **Incorporação não informada ao fisco** | **Sim**, e **sem alterar a CDA** | Tema 1.049 |
| Só há certidão de não localização, sem demonstrar a **falta de comunicação** aos órgãos competentes | Presunção **incompleta** — reforce a prova antes de pedir | Súm. 435 (os dois elementos) |
| Sócio meramente **quotista, sem poder de administração** em nenhum momento | **Não** há base nos temas deste anexo | `[VERIFICAR]` — nada aqui autoriza |
| Grupo econômico, confusão patrimonial, desconsideração da personalidade | **Fora deste anexo** | `[VERIFICAR]` — não extrapolar |

## 4. Roteiro antes de peticionar (a ordem que evita o indeferimento)

1. **A dissolução irregular está demonstrada nos dois elementos** da Súmula 435 — não funcionamento
   **e** ausência de comunicação?
2. **Quem tinha poder de administração NA DATA da dissolução?** É esse o nome a incluir (Tema 981) —
   e a data da dissolução precisa estar identificada, não estimada.
3. **Essa pessoa se retirou regularmente antes?** Se sim, **pare**: o Tema 962 fecha essa porta, e
   insistir é pedir indeferimento.
4. **Se ela se retirou e ainda assim se quer atingi-la**, há **prova** de excesso de poderes ou
   infração à lei (Tema 97)? Prova, não alegação — sem ela, não se pede.
5. **Há incorporação não informada ao fisco?** Então o Tema 1.049 é o fundamento próprio, e a CDA
   não precisa ser alterada.
6. **O nome já constava do Termo de Inscrição** como co-responsável (LEF art. 2º §5º, I)? Nomear na
   origem, havendo fundamento, é o que evita boa parte desta discussão —
   `execucao-fiscal-lef`.

## 5. O limite deste anexo — dito com todas as letras

Redirecionamento é área em que a memória do modelo tem muita jurisprudência solta, e quase nada dela
está confirmado aqui. **Nenhum outro tema, súmula, REsp ou enunciado entra nesta skill.** O anexo
registra **uma súmula e cinco temas**; o que estiver fora disso — inclusive teses correntes sobre
grupo econômico, IDPJ na execução fiscal, responsabilidade do administrador não sócio, prazo do
redirecionamento — sai como `[VERIFICAR]`, com a indicação de conferir na fonte primária. Escrever
número de memória aqui é o defeito que o comprador enxerga primeiro.

E, como em todo o anexo: **número pode; ementa não.** Tema, REsp e órgão vão para a peça; a
transcrição entre aspas só depois de conferida em `stj.jus.br`.

## Travas desta skill

- **P2 — nada sem lastro (a mais exposta desta skill).** Só a Súmula 435 e os Temas 630, 981, 962,
  97 e 1.049, como `context/temas-e-sumulas-fazendarios.md` os registra. Ementa → conferir na fonte.
  Qualquer outro precedente → `[VERIFICAR]`.
- **P3 — anti-tese-superada.** Pedido apoiado só na Súmula 435, sem os dois temas de fechamento, é
  reprovado antes de sair: o gate G3 da `suprema-corte-fazendaria` roda exatamente isso.
- **Nunca extrapolar o que o anexo registra** — trava própria: o produto não cria hipótese de
  redirecionamento por analogia.
- **P1.** A rede é jurisprudência processual comum às três esferas; o crédito é de ICMS, IPVA, ITCMD e demais créditos estaduais.
- **P4.** Minuta de pedido de redirecionamento é estudo e trabalho local — a decisão de incluir uma
  pessoa no polo passivo e a responsabilidade por ela são do procurador, indelegáveis.

**Próximo passo:** o rito e a inscrição que evitam a discussão → `execucao-fiscal-lef`. O tempo que
correu enquanto se procurava o devedor → `prescricao-intercorrente`. Toda entrega fecha por
`suprema-corte-fazendaria`.
