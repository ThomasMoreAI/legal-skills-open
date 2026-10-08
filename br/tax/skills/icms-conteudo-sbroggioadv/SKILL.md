---
name: icms-conteudo-sbroggioadv
title: icms-conteudo — o imposto do Estado, artigo por artigo, com o horizonte declarado
description: 'O ICMS pela ótica do fisco estadual, com cada dispositivo lido no anexo verbatim da Lei Kandir (LC 87/1996): incidência e não-incidência (arts. 1º-3º), contribuinte e responsável (arts. 4º-6º), substituição tributária com a base do art. 8º, o acordo interestadual do art. 9º e a restituição do fato gerador presumido não realizado (art. 10), local, momento e base (arts. 11-13) e o crédito (arts. 19, 20 e 23). Traz as duas armadilhas que decidem caso: a transferência entre estabelecimentos do mesmo titular deixou de ser fato gerador (ADC 49 + LC 204/2023) e o compilado do Planalto marca o revogado como omitido. Fecha com o aviso obrigatório da transição — o ICMS se extingue em 2033. Aciona: "fato gerador do ICMS", "quem é contribuinte", "substituição tributária", "local da operação", "base de cálculo do ICMS", "crédito de ICMS", "transferência entre filiais".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-estadual-os-marketplace/tree/main/procurador-estadual-os/skills/icms-conteudo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# icms-conteudo — o imposto do Estado, artigo por artigo, com o horizonte declarado

Esta skill trata o ICMS **pela ótica de quem
exige**: onde a lei complementar autoriza cobrar, quem responde e onde o texto fecha a porta. Tudo
sai de `context/lc-87-kandir.md` (Planalto, 19/08/2026). Este produto atende o **Estado**.

**Quando entra:** antes de inscrever, exigir ou defender crédito de ICMS; quando o contribuinte
ataca o lançamento no fato gerador, no local ou na base; na substituição tributária; antes de glosar
crédito.

## ⚠️ Duas armadilhas

**1. O anexo é compilado, e o revogado sai marcado.** Dispositivo sem vigência aparece como
`[dispositivo revogado — omitido]`, seguido da nota da lei que o revogou (LCP 102/2000, LCP
114/2002, LC 190/2022, LC 201/2023, LC 204/2023, LC 214/2025). Duas consequências: um artigo que se
lembra com mais palavras pode ter perdido parte delas; e uma linha de omissão logo **antes** de um
inciso avisa que o texto ali é o **novo**. Ler o bloco inteiro com a nota antes de citar.

**2. Transferência entre estabelecimentos do mesmo titular não é fato gerador.** É a tese que o
Estado perdeu, e o anexo registra a derrota em três camadas: o art. 11, §3º, II ("é autônomo cada
estabelecimento do mesmo titular") traz a remissão **"(Vide ADC 49)"**; o art. 12, I aparece com
**redação dada pela LC 204/2023** — "da saída de mercadoria de estabelecimento de contribuinte" —,
precedido da linha de omissão do texto anterior; e o art. 13, §4º, que dava a base dessa
transferência, consta **omitido, revogado pela LC 204/2023**. Em troca, o art. 12, §4º disciplina a
**transferência do crédito** e o §5º faculta **equiparar** a transferência a operação tributada.

## 1. Competência, incidência e não-incidência — arts. 1º a 3º

**Art. 1º:** compete aos **Estados e ao DF** instituir o imposto sobre operações relativas à
circulação de mercadorias e sobre prestações de transporte **interestadual e intermunicipal** e de
**comunicação**, ainda que iniciadas no exterior.

**Art. 2º — incide sobre:** I circulação de mercadorias, inclusive alimentação e bebidas em bares e
restaurantes · II transporte interestadual e intermunicipal · III prestações **onerosas** de
serviços de comunicação · IV fornecimento de mercadorias com serviços **não compreendidos** na
competência tributária dos Municípios · V fornecimento com serviços **da competência municipal**,
quando a lei complementar aplicável expressamente sujeitar a operação à incidência estadual. **§1º — incide também** na entrada de mercadoria ou bem **importados** por
pessoa física ou jurídica, "**ainda que não seja contribuinte habitual do imposto, qualquer que seja
a sua finalidade**" (redação da LCP 114/2002); no serviço iniciado no exterior; e na entrada, no
Estado destinatário, de petróleo, derivados e energia **fora da comercialização ou
industrialização**, cabendo o imposto ao Estado do adquirente. **§2º:** o fato gerador **independe
da natureza jurídica da operação**.

**Art. 3º — não incide sobre:** livros, jornais e o papel de impressão (I) · **exportação** (II) ·
interestaduais com energia e petróleo/derivados destinados a industrialização ou comercialização
(III) · ouro como ativo financeiro (IV) · mercadorias usadas pelo próprio autor da saída em serviço
de competência municipal (V) · transferência de **estabelecimento** (VI) · alienação fiduciária
(VII) · arrendamento mercantil, salvo a venda ao arrendatário (VIII). Os incisos IV-V do art. 2º e o
V do art. 3º marcam a fronteira com a competência **municipal** — ali o produto para: esse tributo é
do `procurador-municipal-os` (P1).

## 2. Contribuinte, responsável e substituto — arts. 4º a 7º

**Art. 4º — contribuinte** é quem realiza operações **com habitualidade ou em volume que caracterize
intuito comercial**. O §1º (transformado do parágrafo único pela LC 190/2022) alcança quem, **mesmo
sem habitualidade ou intuito comercial**, importa bens do exterior, recebe serviço iniciado no
exterior, adquire em licitação bens apreendidos, ou adquire combustíveis e energia de outro Estado
fora da comercialização/industrialização. O **§2º** trata do **diferencial de alíquota**
a consumidor final em outro Estado: contribuinte é o **destinatário**, se contribuinte do imposto
(I); senão, o **remetente/prestador** (II).

**Art. 5º:** lei pode atribuir a **terceiros** a responsabilidade quando seus atos ou omissões
concorram para o não recolhimento. **Art. 6º (LCP 114/2002):** **lei estadual** pode atribuir a
contribuinte ou depositário a responsabilidade, "hipótese em que assumirá a condição de **substituto
tributário**" — §1º: alcança operações antecedentes, concomitantes ou subsequentes; §2º: só sobre
bens ou serviços **previstos em lei de cada Estado**. **Art. 7º:** na ST, inclui-se como fato gerador
a **entrada** no estabelecimento do adquirente.

## 3. Substituição tributária — arts. 8º a 10

- **Art. 8º — base.** Nas **antecedentes ou concomitantes**, o valor praticado pelo substituído (I).
  Nas **subsequentes**, a soma do valor da operação própria do substituto, seguro, frete, demais
  encargos e margem (II).
- **Art. 9º — a trava interestadual.** A adoção do regime **em operações interestaduais depende de
  acordo específico celebrado pelos Estados interessados**: é a condição que o Estado precisa provar
  ao exigir ST de remetente de outra unidade. O §2º — só para petróleo/derivados e energia (§1º,
  I-II) — manda o imposto ao **Estado do adquirente**, pago pelo remetente, quando o destinatário é
  consumidor final.
- **Art. 10 — restituição.** Assegurada ao substituído quanto ao **fato gerador presumido que não se
  realizar**. §1º: sem deliberação em **90 dias**, o contribuinte **se credita** na escrita fiscal.
  §2º: decisão contrária irrecorrível → estorno em **15 dias**. Prazo perdido
  vira crédito lançado — gerir o estoque de pedidos é matéria de procuradoria.

## 4. Local, momento e base — arts. 11-13

| Hipótese | Local (art. 11) | Momento (art. 12) | Base (art. 13) |
|---|---|---|---|
| Mercadoria | onde se encontre no fato gerador (I, a); irregular, onde estiver (b) | **saída** do estabelecimento de contribuinte (I — LC 204/2023) | valor da operação (I) |
| Importação | **entrada física** (I, d) | ler no anexo | documentos (art. 14) + II + IPI + IOF-câmbio + **quaisquer outros impostos, taxas, contribuições e despesas aduaneiras** (V, a-e) |
| Transporte | onde **tenha início** (II, a) | **início** da prestação (V) | preço do serviço (III) |
| Energia/combustíveis interestaduais | Estado do **adquirente** (I, g) | anexo | anexo |

## 5. Não-cumulatividade e crédito — arts. 19, 20, 23

**Art. 19:** o imposto **é não-cumulativo**, compensando-se o devido em cada operação com **o
montante cobrado nas anteriores pelo mesmo ou por outro Estado**. **Art. 20:** o sujeito passivo
pode creditar-se do imposto anteriormente cobrado nas entradas de mercadoria, **real ou simbólica**,
inclusive as de uso, consumo ou ativo permanente, e no recebimento de transporte ou comunicação.
**§1º — a porta de glosa: não dão direito a crédito** as
entradas de operações **isentas ou não tributadas**, nem as de bens ou serviços **alheios à
atividade** do estabelecimento; o §2º presume alheios, salvo prova em contrário, os itens que o
anexo enumera — ler antes de glosar.

**Art. 23:** o crédito depende da **idoneidade da documentação** e da escrituração nos prazos da
legislação. **Parágrafo único: o direito de utilizar o crédito extingue-se depois de decorridos
cinco anos contados da data de emissão do documento** — prazo de lei complementar, oponível
independentemente de norma estadual.

## 6. O que não se sustenta

Incidência na transferência entre filiais do mesmo titular (**art. 12, §4º**, LC
204/2023, + ADC 49) · ST interestadual sem acordo entre os Estados (o acordo é condição legal —
art. 9º, caput) · crédito de documento com mais de 5 anos tratado como vivo (o direito
**extinguiu-se** — art. 23, par. único).

## ⏳ P6 — o aviso da transição (obrigatório)

**A EC 132/2023 e a LC 214/2025 puseram o ICMS em extinção programada**
(`context/reforma-tributaria-transicao.md`): **2026** ano-teste (CBS 0,9% + IBS 0,1%, compensados
com PIS/COFINS — **o ICMS segue cobrado normalmente**) · **2027-2028** CBS à alíquota de referência
reduzida em 0,1 p.p. e IBS 0,1% · **2029-2032** participações IBS/ICMS-ISS de
**10/90, 20/80, 30/70 e 40/60** · **2033 extinção**.

É aviso de **horizonte, não de invalidade**: em 2026 o imposto é exigível e a execução corre
normalmente. Tratar o ICMS como permanente é o que a **TV3** recusa. Alíquota final do IBS, alíquota
de referência, trava de teto e split payment **não** estão no anexo → `[VERIFICAR]`.

## Travas desta skill

- **P1.** Este plugin trata ICMS, IPVA e ITCMD. A fronteira dos arts. 2º, IV-V e 3º, V entra como
  **limite da incidência estadual**; o tributo do Município é do `procurador-municipal-os`, a
  matéria federal, do `procurador-federal-os`.
- **P2.** Todo dispositivo acima está em `context/lc-87-kandir.md`. Alíquota, MVA, convênio,
  regulamento e ementa **não** estão → `[VERIFICAR]`.
- **P3.** A transferência entre filiais do mesmo titular é o exemplo vivo: dispositivo revogado,
  tese perdida. Toda tese de incidência passa por `suprema-corte-fazendaria`.
- **P5.** Alíquotas, regime de apuração (art. 24, que remete à legislação estadual) e
  lista de ST (art. 6º §2º) são direito local — sem o texto, o produto pergunta.
- **P6** o aviso da transição é obrigatório; **P4** isto é estudo e minutação local — a conferência
  nos autos e o protocolo são do procurador, indelegáveis.

**Próximo passo:** crédito constituído → `divida-ativa-estadual`; custo de cobrança →
`triagem-baixo-valor`; rito → `execucao-fiscal-lef`; benefício e CONFAZ →
`guerra-fiscal-e-beneficios`; cronograma → `transicao-icms-ibs`. Fecha por `suprema-corte-fazendaria`.
