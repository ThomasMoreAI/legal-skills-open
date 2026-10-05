---
name: prerrogativas-processuais-sbroggioadv
title: prerrogativas-processuais — o dobro que não é automático e o reexame que nem sempre sobe
description: 'As duas prerrogativas processuais que mais se perdem por serem tratadas como automáticas, viradas em método: CPC 183 (prazo em dobro contado da intimação pessoal, na forma do §1º — carga, remessa ou meio eletrônico) com a trava P7 em destaque, porque o §2º afasta o dobro sempre que lei específica fixar prazo próprio para o ente; e CPC 496 (remessa necessária) com os três degraus exatos de dispensa do §3º — 1.000 salários-mínimos para a União e suas autarquias/fundações, 500 para Estados, DF, respectivas autarquias/fundações e Municípios que sejam capitais, 100 para todos os demais Municípios — mais as quatro hipóteses do §4º, que dispensam independentemente do valor, incluída a orientação vinculante do próprio ente (inciso IV). Entrega tabela prática situação → prazo/remessa → base, com o texto verbatim do anexo. Aciona: "tenho prazo em dobro?", "quando cabe remessa necessária", "isso sobe por reexame?", "prazo da Fazenda", "intimação pessoal", "dispensa do duplo grau", "o
  prazo é próprio ou dobra?".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/prerrogativas-processuais
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# prerrogativas-processuais — o dobro que não é automático e o reexame que nem sempre sobe

Prerrogativa da Fazenda não é presente: é regra com condição. As duas que este produto trata aqui
são as que mais se perdem na prática — o prazo em dobro afirmado sem checar a exceção, e a remessa
necessária invocada (ou dispensada) sem conferir o degrau. Texto verbatim em
`context/prerrogativas-cpc.md`; nada aqui sai de memória.

Este produto atende o **Estado**.

## Quando esta skill entra

- Antes de afirmar tempestividade de qualquer manifestação do ente.
- Quando a sentença é contrária ao ente e a pergunta é "sobe sozinha ou preciso apelar?".
- Quando a sentença é favorável ao ente e a parte contrária alega que o reexame é obrigatório.
- Quando se discute a partir de quando o prazo correu — publicação ou intimação pessoal.

## 1. CPC 183 — o dobro, o termo inicial e a trava P7

**Caput (verbatim):** "A União, os Estados, o Distrito Federal, os Municípios e suas respectivas
autarquias e fundações de direito público gozarão de prazo em dobro para todas as suas manifestações
processuais, cuja contagem terá início a partir da intimação pessoal."

Três leituras que o texto impõe:

- **Quem tem** — o ente e suas **autarquias e fundações de direito público**. A prerrogativa é do
  ente e das entidades que o caput nomeia, não de qualquer pessoa jurídica ligada à administração.
- **Para o quê** — "todas as suas manifestações processuais". É amplo, e é por isso que a exceção
  do §2º importa tanto: sem ela, a leitura viraria automatismo.
- **A partir de quando** — da **intimação pessoal**, não da publicação. O §1º define a forma: "A
  intimação pessoal far-se-á por carga, remessa ou meio eletrônico." Contar da publicação, num
  processo em que a intimação pessoal se deu depois, é errar o termo inicial mesmo acertando o
  dobro.

### ⚠️ A trava P7 — o §2º, em destaque

**Texto verbatim:** "§ 2º Não se aplica o benefício da contagem em dobro quando a lei estabelecer,
de forma expressa, prazo próprio para o ente público."

Esta é **a** trava desta skill, e ela morde em toda menção a prazo. A pergunta obrigatória, antes de
qualquer afirmação de tempestividade:

> **Existe lei específica fixando prazo próprio para o ente neste procedimento?**
> Se existe → **o dobro não incide**. Se não existe → o dobro é a regra do caput.

O exemplo que o próprio chassi carrega está na LEF (`context/lef-6830.md`): a Lei 6.830/80 fixa
prazos próprios no rito da execução fiscal — **5 dias** para pagar ou garantir (art. 8º, caput),
**30 dias** para embargos do executado (art. 16, caput) e **30 dias** para a **Fazenda impugnar os
embargos** (art. 17, caput). Prazo fixado em lei específica é prazo próprio, e a contagem em dobro
**não é automática** ali. Nunca escreva "prazo em dobro" sobre um procedimento regido por lei
especial sem antes ler o prazo dessa lei.

Onde a checagem não puder ser feita — porque o procedimento é regido por lei que não está nos anexos
— o resultado é `[VERIFICAR]` com a pergunta explícita, jamais a afirmação do dobro por default.

## 2. Intimação pessoal — a prerrogativa que aparece duas vezes na esteira fiscal

Além do CPC 183 §1º, a LEF traz a intimação pessoal do representante judicial em dois pontos
(`context/lef-6830.md`): **art. 25** — "qualquer intimação ao representante judicial da Fazenda
Pública será feita pessoalmente", com o parágrafo único admitindo vista dos autos com remessa
imediata; e **art. 22 §2º** — intimação pessoal da realização do **leilão**, com a antecedência do
§1º (entre 10 e 30 dias da publicação do edital). Intimação de leilão feita só por publicação é
vício alegável; o produto registra o fato, não presume o resultado.

## 3. CPC 496 — remessa necessária, e as duas portas de dispensa

**Caput:** está sujeita ao duplo grau, **não produzindo efeito senão depois de confirmada pelo
tribunal**, a sentença **(I)** proferida contra a União, Estados, DF, Municípios e respectivas
autarquias e fundações de direito público; e **(II)** que **julgar procedentes, no todo ou em parte,
os embargos à execução fiscal**.

O **inciso II** é o de maior volume na esteira fiscal e não depende de o ente ser réu — aqui ele é o
**exequente**. Embargos julgados procedentes, ainda que em parte, sobem.

**§§1º e 2º:** não interposta a apelação no prazo, o juiz ordena a remessa; se não o fizer, o
presidente do tribunal avoca. O tribunal julgará a remessa.

### Porta 1 — dispensa por valor (§3º): os três degraus

Não se aplica a remessa quando a condenação ou o proveito econômico for de **valor certo e líquido**
inferior a:

| Degrau | Ente | Quem é |
|---|---|---|
| **1.000 salários-mínimos** | União e as respectivas autarquias e fundações de direito público | inciso I |
| **500 salários-mínimos** | Estados, DF, as respectivas autarquias/fundações **e os Municípios que constituam capitais dos Estados** | inciso II |
| **100 salários-mínimos** | **todos os demais Municípios** e respectivas autarquias/fundações | inciso III |

Duas leituras que o anexo obriga:

- **O degrau é definido pelo ente, não pelo valor isoladamente.** Um Município do interior está no
  piso de 100 SM; a capital do mesmo Estado está em 500 SM. Antes de aplicar o degrau, confirme
  **qual ente** é parte — e confirme em qual linha o ente atendido por este produto se enquadra
  (Estado), porque errar o degrau inverte a conclusão.
- **A dispensa exige valor certo e líquido.** Condenação **ilíquida não dispensa** a remessa, por
  maior que seja a expectativa de que ficaria abaixo do degrau. Sem liquidez, não há degrau a
  aplicar.

### Porta 2 — dispensa por fundamento (§4º): independe do valor

Também não se aplica quando a sentença estiver fundada em: **I** — súmula de tribunal superior;
**II** — acórdão do STF ou do STJ em julgamento de **recursos repetitivos**; **III** — entendimento
firmado em **IRDR** ou em assunção de competência; **IV** — entendimento **coincidente com
orientação vinculante firmada no âmbito administrativo do próprio ente público**, consolidada em
manifestação, parecer ou súmula administrativa.

O **inciso IV** é o dispositivo que liga a remessa necessária ao trabalho consultivo da própria
procuradoria: a súmula administrativa do ente, editada nos termos do **art. 30 da LINDB**
(`context/lindb-20-30.md`, parágrafo único: caráter vinculante em relação ao órgão até ulterior
revisão), dispensa o reexame quando a sentença coincide com ela. Consultivo bem feito reduz acervo
recursal — a ponte está em `lindb-como-metodo`.

## 4. Tabela prática — situação → prazo/remessa → base

| Situação | Resposta | Base (anexo) |
|---|---|---|
| Manifestação processual do ente, procedimento sem lei especial | Prazo em dobro, contado da intimação pessoal | CPC 183, caput e §1º |
| Procedimento regido por lei que fixa prazo próprio (ex.: LEF, arts. 8º, 16 e 17) | **Dobro não incide** — prazo é o da lei especial | CPC 183 §2º + LEF |
| Não se sabe se há lei especial no procedimento | `[VERIFICAR]` com a pergunta — nunca afirmar o dobro | P7 |
| Intimação do representante judicial na execução fiscal | Pessoalmente (admitida vista com remessa imediata) | LEF art. 25 |
| Intimação do leilão | Pessoal, com 10 a 30 dias de antecedência | LEF art. 22, §§1º-2º |
| Sentença contra o ente ou autarquia/fundação | Sujeita a remessa necessária | CPC 496, I |
| Embargos à execução fiscal julgados procedentes, no todo ou em parte | Sujeita a remessa necessária | CPC 496, II |
| Condenação **líquida** abaixo do degrau do ente (1.000 / 500 / 100 SM) | Dispensada | CPC 496 §3º, I-III |
| Condenação **ilíquida**, ainda que de valor aparentemente baixo | **Não** dispensa | CPC 496 §3º (exige valor certo e líquido) |
| Sentença fundada em súmula de tribunal superior, repetitivo, IRDR/assunção | Dispensada, **independentemente do valor** | CPC 496 §4º, I-III |
| Sentença coincidente com súmula/parecer vinculante do próprio ente | Dispensada, independentemente do valor | CPC 496 §4º, IV |

## Travas desta skill

- **P7 (a desta skill).** Nenhuma frase afirma prazo em dobro sem a checagem do §2º. É a
  prerrogativa que mais se perde por ser tratada como automática.
- **P2 — nada sem lastro.** Todo dispositivo citado aqui está em `context/prerrogativas-cpc.md` ou
  `context/lef-6830.md`. Prazo, degrau ou hipótese fora dos anexos → `[VERIFICAR]`, nunca de
  memória. Transcrição entre aspas de ementa exige conferência em fonte primária.
- **P1.** Prerrogativa é **lei federal e comum às três esferas** — o que varia por esfera é qual
  degrau do §3º se aplica ao ente, nunca a regra. Matéria tributária não entra nesta skill.
- **P5.** Se o ente tiver lei própria fixando prazo ou rito específico, o produto **pergunta pelo
  texto local** — não presume, não aplica por analogia o regime de outro ente.
- **P4.** Contagem de prazo aqui é estudo; a conferência da tempestividade nos autos e a
  responsabilidade pelo protocolo são do procurador, indelegáveis.

**Próximo passo:** honorários da mesma sentença → `honorarios-da-fazenda`. Sentença que veio de
embargos à execução fiscal → volte à esteira por `execucao-fiscal-lef`. Toda entrega fecha por
`suprema-corte-fazendaria` (o gate G6 confere justamente a checagem do §2º).
