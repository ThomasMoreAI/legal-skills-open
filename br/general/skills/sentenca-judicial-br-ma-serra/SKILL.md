---
name: sentenca-judicial-br-ma-serra
title: Sentenca Judicial BR — Gerador de Decisoes para o Judiciario Brasileiro
description: 'Usar quando o usuario pedir para redigir, revisar ou estruturar decisoes judiciais brasileiras — sentencas, decisoes interlocutorias, tutelas, liminares ou qualquer provimento jurisdicional. Triggers: "sentenca", "decisao", "despacho", "julgamento", "FIRAC", "dispositivo", "fundamentacao", "relatorio judicial", "tutela", "liminar", "acordao", "minuta".'
author: ma-serra
author_url: https://github.com/ma-serra/lex-intelligentia-skills/tree/main/skills/core/sentenca-judicial-br
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Sentenca Judicial BR — Gerador de Decisoes para o Judiciario Brasileiro

## Overview

Skill para geracao de minutas de sentenca e decisoes judiciais no padrao do Poder Judiciario brasileiro, utilizando a metodologia **FIRAC-JB** (Facts, Issues, Rules, Application, Conclusion) adaptada ao sistema de civil law. Cada citacao de jurisprudencia segue o protocolo anti-alucinacao de 3 niveis.

## When to Use

- Redigir minutas de sentenca civel
- Redigir decisoes interlocutorias (tutelas, liminares)
- Redigir despachos fundamentados
- Revisar ou reestruturar decisoes existentes
- Fundamentar com precedentes STJ/STF

**When NOT to Use:**
- Sentencas penais (requer skill separada com dosimetria)
- Acordaos de Tribunal (estrutura distinta com voto e ementa)
- Pareceres ou pecas advocaticias (usar `peticao-analyzer`)

---

## Protocolo Anti-Alucinacao

**OBRIGATORIO:** Toda citacao de jurisprudencia deve seguir o protocolo de 3 niveis (ver `GUIA-ANTI-ALUCINACAO.md`):

| Nivel | Quando | Formato |
|-------|--------|---------|
| CONFIRMADO | Tese amplamente conhecida, Sumula com numero certo | Citar normalmente + "[CONFIRMAR no tribunal]" |
| PROVAVEL | Tendencia jurisprudencial consistente | "Ha tendencia no sentido de..." + "[VERIFICAR]" |
| INCERTO | Sem informacao segura | Declarar incerteza + fornecer links de busca |

---

## Metodologia FIRAC Judicial Brasileiro

A metodologia **FIRAC-JB** e uma adaptacao ao sistema juridico civil-law do Brasil (ver `METODOLOGIA-FIRAC-JB.md`):

| Elemento | Equivalente na Sentenca | Secao |
|----------|------------------------|-------|
| **F**acts | Sintese dos fatos narrados na peticao + provas | RELATORIO |
| **I**ssues | Questoes juridicas controvertidas | Inicio da FUNDAMENTACAO |
| **R**ules | Normas, sumulas, teses STJ/STF aplicaveis | FUNDAMENTACAO (normativa) |
| **A**nalysis | Subsuncao do fato a norma com analise probatoria | FUNDAMENTACAO (analitica) |
| **C**onclusion | Provimento / Desprovimento + Dispositivo | DISPOSITIVO |

### Fundamentacao Analitica — Art. 489, §1°, CPC

Uma decisao **nao esta fundamentada** (nula) quando o juiz:

1. Se limita a indicacao ou reproducao de ato normativo, sem explicar a relacao com a causa
2. Emprega conceitos juridicos indeterminados, sem explicar o motivo concreto da incidencia
3. Invoca motivos que se prestariam a justificar qualquer outra decisao
4. Nao enfrenta todos os argumentos capazes de infirmar a conclusao adotada
5. Se limita a invocar precedente ou sumula, sem identificar fundamentos determinantes nem demonstrar que o caso se ajusta
6. Deixa de seguir sumula ou precedente invocado pela parte, sem demonstrar distincao ou superacao

---

## Estrutura Canonica da Sentenca Brasileira

```
PODER JUDICIARIO DO ESTADO DO ESPIRITO SANTO
[Comarca/Vara]

Processo n: [numero CNJ]
Autor(es): [nome(s)]
Reu(s): [nome(s)]
Natureza: [classe processual]

SENTENCA

I — RELATORIO

[Sintese objetiva: quem e o autor, o que pediu, fundamentos faticos e juridicos da
inicial; contestacao do reu; eventuais replicas e manifestacoes; provas produzidas]

II — FUNDAMENTACAO

2.1. Da(s) Questao(oes) Preliminar(es)
[Se houver: prescricao, decadencia, ilegitimidade, inepcia, etc.]

2.2. Do Merito
[Analise por topicos das questoes controvertidas]

2.2.1. [Primeira questao de merito]
[Norma aplicavel -> analise fatica -> subsuncao -> conclusao parcial]

2.2.2. [Segunda questao de merito, se houver]

III — DISPOSITIVO

[Resultado: julgo PROCEDENTE / IMPROCEDENTE / PROCEDENTE EM PARTE]
[Condena/absolve / declara / constitui / desconstitui]
[Honorarios advocaticios: art. 85, CPC]
[Custas processuais]
[Prazo recursal: art. 1.009, CPC – 15 dias uteis]

[Cidade], [data].

[Nome do Magistrado]
Juiz(a) de Direito da [X]a Vara Civel de [Comarca]
```

---

## Templates por Area do Direito

### 1. Direito Bancario — Revisao Contratual + Dano Moral

**Questoes tipicas:**
- Capitalizacao de juros (Sumula 541/STJ — permitida se pactuada)
- Tarifa de cadastro (Sumula 566/STJ — licita em contratos posteriores a Resolucao CMN 3.518/2007, de 30/4/2008)
- Juros moratorios legais (art. 406, CC — taxa referencial SELIC; na falta de convencao, aplica-se a taxa de juros para mora fiscal)
- Dano moral por negativacao indevida (jurisprudencia consolidada do STJ — dano moral in re ipsa)

**Fundamentacao padrao para negativacao indevida:**
```
A inscricao indevida do nome do consumidor em cadastros de inadimplentes
configura dano moral in re ipsa, dispensando prova do prejuizo, conforme
entendimento consolidado no Superior Tribunal de Justica em multiplos
julgados das Turmas de Direito Privado. [CONFIRMAR precedente especifico
aplicavel ao caso no site do STJ]
O valor da indenizacao deve observar os criterios da proporcionalidade e
razoabilidade, vedado o enriquecimento sem causa (art. 944, CC).
Considerando as circunstancias do caso — [gravidade da conduta, condicao
economica das partes, carater pedagogico-preventivo] — fixo a indenizacao
por danos morais em R$ [valor].
```

**Observacao:** A Sumula 385/STJ dispoe que, havendo anotacao preexistente
legitima, nao cabe indenizacao por dano moral. Verificar se o autor possui
outras inscricoes vigentes antes de reconhecer o dano in re ipsa.

**Tese STJ sobre tarifa de cadastro (Temas 618/619):**
```
O Superior Tribunal de Justica, por sua Segunda Secao, em julgamento sob
o rito dos recursos repetitivos (REsp 1.251.331/RS — Temas 618/619),
consolidou o entendimento de que e licita a cobranca da tarifa de cadastro
no inicio do relacionamento entre consumidor e instituicao financeira,
nos contratos posteriores a 30/4/2008 (Resolucao CMN 3.518/2007).
Quanto a tarifa de avaliacao do bem, e admitida desde que o servico tenha
sido efetivamente prestado e o valor nao seja abusivo.
```

---

### 2. Direito do Consumidor — CDC

**Questoes tipicas:**
- Vicio do produto/servico (arts. 18 a 25, CDC)
- Fato do produto/servico — responsabilidade objetiva (arts. 12-14, CDC)
- Inversao do onus da prova (art. 6, VIII, CDC)
- Praticas abusivas (art. 39, CDC)

**Bloco de inversao do onus:**
```
Reconheco a hipossuficiencia tecnica do autor/consumidor frente ao fornecedor,
razao pela qual inverto o onus da prova, nos termos do art. 6, VIII, do
Codigo de Defesa do Consumidor, cabendo ao reu demonstrar a inexistencia
do vicio alegado ou a ausencia de nexo causal.
```

**Dano moral consumerista:**
```
Na relacao de consumo, o dano moral decorre da situacao vivenciada pelo
consumidor que, privado da efetiva fruicao do bem ou servico contratado,
experimenta constrangimento, angustia e frustracao que transcendem o mero
dissabor cotidiano. [CONFIRMAR precedente especifico no STJ]
```

---

### 3. Acoes Possessorias — Reintegracao e Manutencao

**Requisitos do art. 561, CPC:**
```
Para a procedencia do pedido possessorio, cumpre ao autor demonstrar:
(i) a posse anterior — [analise da prova];
(ii) o esbulho/turbacao praticado pelo reu — [analise da prova];
(iii) a data do esbulho/turbacao — [analise da prova]; e
(iv) a continuacao da perda ou ameaca — [analise da prova].

[Conclusao: estando/nao estando presentes os requisitos legais, julgo
PROCEDENTE/IMPROCEDENTE o pedido de reintegracao/manutencao de posse]
```

---

### 4. Usucapiao

**Mapa das modalidades:**

| Modalidade | Prazo | Dispositivo | Requisitos |
|------------|-------|-------------|------------|
| Extraordinaria | 15 anos (10 com moradia/trabalho) | Art. 1.238, CC | Posse mansa, pacifica, ininterrupta, sem titulo nem boa-fe |
| Ordinaria | 10 anos (5 com moradia) | Art. 1.242, CC | Justo titulo + boa-fe |
| Especial urbana | 5 anos | Art. 183, CF; Art. 1.240, CC | Area <= 250m2, moradia propria, sem outro imovel |
| Especial rural | 5 anos | Art. 191, CF; Art. 1.239, CC | Area <= 50ha, tornando produtiva, sem outro imovel |
| Familiar | 2 anos | Art. 1.240-A, CC | Ex-conjuge/companheiro abandonou o lar |

**Bloco padrao de fundamentacao:**
```
A usucapiao e modalidade originaria de aquisicao de propriedade, fundada
na posse prolongada e qualificada, cujos requisitos encontram-se previstos
nos arts. [X] do Codigo Civil e [Y] da Constituicao Federal.

Analisando as provas produzidas nos autos — especialmente [provas:
testemunhal/documental/pericia] —, constata-se que o autor exerce posse
[mansa/pacifica/ininterrupta] sobre o imovel [descricao] desde [data],
perfazendo o prazo legal de [X] anos exigido para a modalidade pleiteada.

[Ausencia de impugnacao a posse / posse nao contestada / ausencia de
acao possessoria ou petitoria por parte dos confrontantes]
```

---

### 5. Tutela de Urgencia — Tutela Provisoria

**Requisitos do art. 300, CPC:**
```
A tutela provisoria de urgencia pressupoe, nos termos do art. 300 do
CPC/2015, a demonstracao de: (i) probabilidade do direito — fumus boni
iuris; e (ii) perigo de dano ou risco ao resultado util do processo —
periculum in mora.

Quanto a probabilidade do direito: [analise dos elementos probatorios
apresentados com a peticao inicial].

Quanto ao periculum in mora: [analise do risco de dano irreparavel ou
de dificil reparacao].

[Presentes/Ausentes] os requisitos legais, [defiro/indefiro] a tutela
de urgencia pleiteada para [objeto da tutela].
```

---

### 6. Responsabilidade Civil — Dano e Nexo

**Tripe da responsabilidade civil subjetiva (art. 186, CC):**
```
A responsabilidade civil subjetiva, na forma do art. 186 c/c art. 927
do Codigo Civil, exige a presenca concomitante de tres elementos:
(a) conduta antijuridica [comissiva/omissiva];
(b) dano [material/moral/estetico]; e
(c) nexo de causalidade entre a conduta e o dano.

[Analise de cada elemento com as provas dos autos]
```

**Responsabilidade objetiva (art. 927, paragrafo unico, CC):**
```
Cuida-se de hipotese de responsabilidade civil objetiva, fundada no
risco da atividade desenvolvida pelo reu (art. 927, paragrafo unico, CC),
prescindindo da demonstracao de culpa, bastando a prova do dano e do nexo
de causalidade.
```

---

### 7. Distrato Imobiliario — Resolucao de Promessa de Compra e Venda

**Questoes tipicas:**
- Regime aplicavel: Lei 13.786/2018 (contratos celebrados apos 28/12/2018) vs. regime anterior (Sumula 543/STJ)
- Retencao: 25% regra geral, 50% se o empreendimento tem patrimonio de afetacao
- Alienacao fiduciaria registrada: Lei 9.514/97 prevalece sobre CDC (Tema 1.095/STJ)
- Juros de mora na restituicao: desde o transito em julgado (Tema 1.002/STJ)
- Hipoteca da construtora: nao vincula adquirentes (Sumula 308/STJ)

**Fundamentacao padrao — regime pos-Lei 13.786/2018:**
```
Tratando-se de contrato de promessa de compra e venda celebrado apos
28/12/2018, aplica-se a disciplina da Lei 13.786/2018, que regulamenta
o distrato e a resolucao dos contratos de incorporacao imobiliaria.

Nos termos do art. 67-A da Lei 4.591/1964 (incluido pela Lei 13.786/2018),
em caso de desistencia ou resolucao por inadimplemento do adquirente,
e licita a retencao de [25%/50%] dos valores pagos, conforme
[o empreendimento nao esteja/esteja] submetido ao regime de patrimonio
de afetacao (art. 67-A, §5).

Calculo:
- Valor total pago pelo adquirente: R$ [valor]
- Percentual de retencao aplicavel: [25%/50%]
- Valor retido: R$ [valor x percentual]
- Valor a restituir: R$ [valor pago - valor retido]

A restituicao sera realizada em parcela unica, no prazo de [30 dias apos
o habite-se / 180 dias], corrigida pela SELIC desde o transito em julgado
(Tema 1.002/STJ). [VERIFICAR tese completa do Tema 1.002]
```

**Fundamentacao padrao — regime anterior (Sumula 543/STJ):**
```
Em se tratando de contrato celebrado ANTES de 28/12/2018, aplica-se o
entendimento consolidado na Sumula 543 do Superior Tribunal de Justica:
na hipotese de resolucao de contrato de promessa de compra e venda de
imovel sujeito ao CDC, deve haver a restituicao imediata das parcelas
pagas pelo promitente comprador, integralmente, em caso de culpa
exclusiva do promitente vendedor, ou parcialmente, caso tenha sido
o comprador quem deu causa ao desfazimento.
[CONFIRMAR enunciado completo da Sumula 543/STJ]
```

**Fundamentacao padrao — inadimplemento EXCLUSIVO do incorporador (atraso na entrega):**
```
[ATENCAO: Este bloco se aplica quando o atraso na entrega e imputavel
exclusivamente ao incorporador. Nao se confunde com a hipotese de
distrato por iniciativa do adquirente (art. 67-A, Lei 4.591/1964).]

O art. 43-A da Lei 4.591/1964 (incluido pela Lei 13.786/2018) estabelece
que o descumprimento do prazo de entrega, ultrapassado o periodo de
tolerancia de 180 dias (art. 43-A, §1), autoriza o adquirente a resolver
o contrato sem qualquer penalidade, com direito a restituicao integral
dos valores pagos e a multa prevista em contrato.

Ademais, o art. 67-A, §14, da mesma lei determina que, em caso de
inadimplemento do incorporador, este ficara obrigado a indenizar o
adquirente — confirmando que os percentuais de retencao de 25%/50%
(art. 67-A, caput e §5) aplicam-se APENAS ao distrato por iniciativa
ou culpa do ADQUIRENTE, nao do incorporador.
[CONFIRMAR redacao exata dos arts. 43-A e 67-A, §14, Lei 4.591/1964]

Restituicao integral — principio convergente:
A Sumula 543/STJ, embora editada sob regime anterior, consagra o
mesmo principio incorporado pelo legislador de 2018: havendo culpa
exclusiva do promitente vendedor, a restituicao dos valores pagos
pelo adquirente deve ser INTEGRAL, sem qualquer retencao.
[CONFIRMAR enunciado completo da Sumula 543/STJ]

Calculo (inadimplemento do incorporador):
- Valor total pago pelo adquirente: R$ [valor]
- Retencao aplicavel: ZERO (culpa exclusiva do incorporador)
- Valor a restituir: R$ [valor total pago]
- Correcao: SELIC unica desde a citacao (Tema 1.368/STJ)
```

**Observacao sobre alienacao fiduciaria:** Se o contrato possui clausula
de alienacao fiduciaria REGISTRADA, o procedimento de execucao extrajudicial
segue a Lei 9.514/97, que prevalece sobre o CDC (Tema 1.095/STJ). Neste
caso, a via judicial so se justifica para controle de legalidade do
procedimento extrajudicial. [VERIFICAR Tema 1.095]

**Inversao da clausula penal moratoria (Tema 971/STJ):**
```
[Aplicavel quando o atraso na entrega e imputavel ao incorporador]

O Superior Tribunal de Justica, no Tema 971 (REsp 1.614.721/DF),
firmou tese vinculante no sentido de que, descumprido o prazo para
entrega do imovel objeto de promessa de compra e venda (incluido o
prazo de tolerancia), a clausula penal moratoria prevista no contrato
para inadimplemento do adquirente deve ser invertida em favor deste,
aplicando-se contra o incorporador inadimplente, no mesmo percentual
contratual, por mes de atraso verificado.
[CONFIRMAR tese completa do Tema 971/STJ]

A natureza da clausula penal moratoria e PROPRIA — nao compensa nem
substitui eventuais lucros cessantes (Tema 970/STJ, REsp 1.635.428/SC).
Assim, o adquirente pode cumular: (i) clausula penal invertida; e
(ii) lucros cessantes comprovados (ex: alugueis pagos por nao dispor
do imovel), desde que demonstre tratar-se de verbas de natureza distinta.
[CONFIRMAR tese completa do Tema 970/STJ]

Calculo da clausula penal invertida:
- Base: valor total pago pelo adquirente (R$ [valor])
- Percentual: [X]% ao mes (mesmo percentual previsto no contrato
  para mora do adquirente)
- Periodo: [N] meses de atraso (apos o prazo de tolerancia)
- Total: R$ [base x percentual x meses]
- Correcao: SELIC unica desde cada mes de atraso (Tema 1.368/STJ)
```

---

### 8. Condominio — Cobranca de Cotas Condominiais

**Questoes tipicas:**
- Natureza propter rem da obrigacao condominial (art. 1.345, CC)
- Legitimidade passiva: quem tem posse com ciencia do condominio (Tema 886/STJ — EM REVISAO)
- Prescricao quinquenal: 5 anos (Tema 949/STJ — art. 206, §5, I, CC)
- Multa moratoria: 2% apos CC/2002 (art. 1.336, §1, CC)
- Preferencia sobre credito hipotecario (Sumula 478/STJ)
- Penhorabilidade do imovel: excecao a impenhorabilidade do bem de familia (art. 3, IV, Lei 8.009/90)

**Fundamentacao padrao:**
```
A obrigacao de pagar as cotas condominiais tem natureza propter rem,
acompanhando a coisa e vinculando quem quer que detenha a posse ou
propriedade da unidade (art. 1.345 do Codigo Civil).

[Se discutida a legitimidade:]
Conforme entendimento do Superior Tribunal de Justica (Tema 886),
a legitimidade para responder pela divida condominial recai sobre
quem exerce a posse da unidade com ciencia do condominio, ainda que
nao seja o proprietario registral. [VERIFICAR tese completa — Tema
886 EM REVISAO]

[Prescricao:]
A pretensao de cobranca de cotas condominiais submete-se ao prazo
prescricional de 5 (cinco) anos, por se tratar de divida liquida
constante de instrumento particular — prestacao periodica (art. 206,
§5, I, CC), conforme tese firmada no Tema 949/STJ.
[VERIFICAR tese completa do Tema 949]

[Multa moratoria:]
A multa por inadimplemento das cotas condominiais, nos condominios
regidos pelo Codigo Civil de 2002, nao pode exceder 2% sobre o
debito (art. 1.336, §1, CC), independentemente do que disponha a
convencao condominial.

[Penhorabilidade:]
O imovel objeto da cobranca, ainda que constitua bem de familia,
pode ser penhorado para satisfacao do credito condominial, conforme
excecao expressa do art. 3, IV, da Lei 8.009/90. Ademais, o credito
condominial tem preferencia sobre o credito hipotecario (Sumula
478/STJ). [CONFIRMAR Sumula 478]

[Clausula locaticia de transferencia — inoponibilidade ao condominio:]
Eventual clausula do contrato de locacao que atribua ao locatario a
responsabilidade pelo pagamento das cotas condominiais NAO e oponivel
ao condominio. A obrigacao propter rem vincula o proprietario perante
o condominio, independentemente de ajustes internos entre locador e
locatario (relatividade dos contratos — art. 421, CC c/c art. 1.345, CC).
Assim, o condominio pode cobrar diretamente do proprietario, que
dispora de acao regressiva contra o locatario inadimplente.
[VERIFICAR: REsp 1.473.484/RS e outros julgados sobre inoponibilidade
da clausula locaticia ao condominio]
```

**Dispositivo padrao:**
```
Ante o exposto, julgo PROCEDENTE o pedido formulado por [CONDOMINIO]
em face de [REU], para CONDENAR o reu ao pagamento de:
(a) cotas condominiais vencidas no periodo de [data inicio] a
    [data fim], no valor total de R$ [valor], acrescidas de:
    - multa moratoria de 2% sobre cada parcela (art. 1.336, §1, CC);
    - juros de mora de 1% ao mes desde cada vencimento; e
    - correcao monetaria [pela SELIC — Tema 1.368/STJ];
(b) cotas condominiais que se vencerem no curso da acao ate a
    efetiva quitacao (vincendas).

Custas e honorarios advocaticios pelo reu, fixados em [X]% sobre o
valor da condenacao (art. 85, §2, CPC).

P.R.I.
```

---

### 9. Locacao — Despejo por Falta de Pagamento

**Questoes tipicas:**
- Inadimplemento como causa de rescisao (art. 9, III, Lei 8.245/91)
- Liminar de despejo: caução de 3 alugueis (art. 59, §1, Lei 8.245/91)
- Fianca: fiador nao responde por aditamento sem anuencia (Sumula 214/STJ)
- Fiador fora da acao de despejo: nao responde pela execucao (Sumula 268/STJ)
- Fianca sem autorizacao do conjuge: ineficacia total (Sumula 332/STJ)
- Benfeitorias: renuncia valida (Sumula 335/STJ) + distincao acessao vs. benfeitoria
- Penhora do bem de familia do fiador: valida para locacao residencial e comercial (Tema 1091/STF)

**Fundamentacao padrao:**
```
A falta de pagamento de alugueis e encargos da locacao constitui
infração contratual e legal que autoriza a resolucao da locacao e
o consequente despejo do inquilino, nos termos do art. 9, III, da
Lei 8.245/91 (Lei de Locacoes).

[Se houver pedido de liminar:]
Quanto a liminar de despejo, o art. 59, §1, IX, da Lei 8.245/91
autoriza a concessao de medida liminar para desocupacao em 15 dias,
desde que prestada caucao no valor equivalente a 3 (tres) meses
de aluguel, independentemente de audiencia da parte contraria.

[Se houver fiador no polo passivo:]
Sobre a responsabilidade do fiador, observa-se que:
- O fiador nao responde por obrigacoes resultantes de aditamento
  ao contrato ao qual nao anuiu (Sumula 214/STJ);
  [CONFIRMAR Sumula 214]
- O fiador que nao foi incluido na acao de despejo nao responde
  pela execucao do julgado (Sumula 268/STJ);
  [CONFIRMAR Sumula 268]
- A fianca prestada sem autorizacao de um dos conjuges e
  totalmente ineficaz (Sumula 332/STJ);
  [CONFIRMAR Sumula 332]

[Sobre benfeitorias:]
A clausula contratual de renuncia a indenizacao por benfeitorias
e ao direito de retencao e valida, conforme entendimento sumulado
(Sumula 335/STJ). [CONFIRMAR Sumula 335]
Todavia, a renuncia nao alcanca as ACESSOES (construcoes novas),
que se distinguem das benfeitorias e podem gerar indenizacao
independentemente de clausula contratual.
```

**Dispositivo padrao:**
```
Ante o exposto, julgo PROCEDENTE o pedido formulado por [LOCADOR]
em face de [LOCATARIO] [e FIADOR, se for o caso], para:
(a) DECLARAR rescindido o contrato de locacao do imovel situado
    em [endereco completo];
(b) DECRETAR o despejo do reu, fixando o prazo de 30 (trinta)
    dias para desocupacao voluntaria (art. 63, §1, Lei 8.245/91);
(c) CONDENAR o reu [e o fiador, solidariamente / nos limites da
    fianca] ao pagamento dos alugueis e encargos vencidos e
    impagos no valor de R$ [valor], acrescidos de [correcao
    monetaria + multa contratual + juros de mora], bem como dos
    alugueis vincendos ate a efetiva desocupacao.

Custas e honorarios advocaticios pelo reu, fixados em [X]% sobre
o valor da condenacao (art. 85, §2, CPC).

P.R.I.
```

**Dispositivo padrao — multi-reu (procedencia parcial subjetiva):**
```
Ante o exposto:
(I) Julgo PROCEDENTE o pedido em face de [LOCATARIO], para:
    (a) DECLARAR rescindido o contrato de locacao do imovel
        situado em [endereco completo];
    (b) DECRETAR o despejo do reu, fixando o prazo de 30 (trinta)
        dias para desocupacao voluntaria (art. 63, §1, Lei 8.245/91);
    (c) CONDENAR o reu ao pagamento dos alugueis e encargos vencidos
        e impagos no valor de R$ [valor], acrescidos de [correcao +
        multa + juros], bem como dos alugueis vincendos ate a efetiva
        desocupacao.

(II) Julgo IMPROCEDENTE o pedido em face de [FIADOR], por
     [ineficacia da fianca — Sumula 332/STJ: fianca prestada sem
     autorizacao do conjuge / Sumula 214/STJ: aditamento sem anuencia
     do fiador / Sumula 268/STJ: fiador nao incluido na acao de despejo
     — selecionar a hipotese aplicavel].

Custas e honorarios do locatario: fixados em [X]% sobre o valor da
condenacao (art. 85, §2, CPC).
Custas e honorarios do fiador: pelo autor, fixados em [X]% sobre o
valor atualizado da causa (art. 85, §2, CPC), observada eventual
gratuidade (art. 98, §3, CPC).

P.R.I.
```

**Observacao sobre penhora do bem de familia do fiador:** O Supremo
Tribunal Federal, no Tema 1091 (RE 1.307.334/SP), firmou tese de que
e constitucional a penhora do bem de familia do fiador em contrato de
locacao, abrangendo locacao residencial e comercial. [VERIFICAR tese
completa do Tema 1091]

---

### 10. Alienacao Fiduciaria de Imovel — Nulidade/Revisao do Procedimento Extrajudicial

**Questoes tipicas:**
- Lei 9.514/1997: procedimento de execucao extrajudicial (arts. 26 e 27)
- Tema 1.095/STJ: alienacao fiduciaria registrada — Lei 9.514 prevalece sobre CDC
- Tema 1.288: purgacao da mora apos consolidacao — limites pre e pos Lei 13.465/2017
- Sumula 308/STJ: NAO se aplica a alienacao fiduciaria (apenas hipoteca de construtora)
- Intimacao pessoal do devedor: requisito essencial de validade (art. 26, §1, Lei 9.514/97)

**Fundamentacao padrao:**
```
A alienacao fiduciaria de bem imovel, disciplinada pela Lei 9.514/1997,
constitui garantia real em que o devedor fiduciante transfere a propriedade
resolavel do imovel ao credor fiduciario ate o adimplemento integral da
divida.

[Procedimento extrajudicial — requisitos:]
O procedimento de execucao extrajudicial da alienacao fiduciaria exige,
como requisito essencial de validade:
(i) registro do contrato no Registro de Imoveis;
(ii) constituicao em mora do devedor por intermedio do Registro de
     Imoveis (art. 26, §1, Lei 9.514/97);
(iii) intimacao PESSOAL do devedor para purgacao da mora no prazo
      de 15 dias; e
(iv) consolidacao da propriedade em nome do credor fiduciario, com
     pagamento do ITBI, seguida de leiloes publicos (art. 27).

[Se alegada nulidade por vicio na intimacao:]
A intimacao pessoal do devedor fiduciante e REQUISITO ESSENCIAL de
validade do procedimento de execucao extrajudicial. A ausencia de
intimacao ou intimacao por via inadequada acarreta nulidade de todo
o procedimento de consolidacao e dos leiloes subsequentes.

[Sobre purgacao da mora apos consolidacao:]
O Superior Tribunal de Justica, no Tema 1.288, firmou entendimento
sobre os limites da purgacao da mora apos a consolidacao da propriedade,
distinguindo contratos anteriores e posteriores a Lei 13.465/2017.
[VERIFICAR tese completa do Tema 1.288]

[Prevalencia da Lei 9.514 sobre CDC:]
Nos termos do Tema 1.095/STJ, quando a alienacao fiduciaria esta
devidamente registrada, o procedimento de execucao extrajudicial
segue a Lei 9.514/97, que prevalece como lei especial sobre o
regime geral do CDC. [VERIFICAR tese completa do Tema 1.095]

[ATENCAO — Sumula 308/STJ NAO se aplica:]
A Sumula 308/STJ (hipoteca entre construtora e agente financeiro
nao atinge adquirentes) aplica-se APENAS a hipoteca, NAO a alienacao
fiduciaria. O STJ consolidou esta distincao em maio de 2025.
[CONFIRMAR posicao atual do STJ sobre inaplicabilidade da S.308
a alienacao fiduciaria]

[Hipotese hibrida: alienacao fiduciaria + inadimplemento do INCORPORADOR]
Quando a resolucao contratual e buscada pelo ADQUIRENTE em razao do
inadimplemento do INCORPORADOR (atraso na entrega, vicio construtivo,
etc.), o Tema 1.095/STJ NAO constitui obstaculo:

O Tema 1.095 regula a prevalencia do PROCEDIMENTO DE EXECUCAO
EXTRAJUDICIAL promovido pelo CREDOR FIDUCIARIO contra o DEVEDOR
inadimplente. Na hipotese inversa — adquirente lesado pelo
inadimplemento do incorporador — a via judicial de resolucao
contratual segue as regras da Lei 13.786/2018 e do CDC.

A alienacao fiduciaria registrada e CONSEQUENCIA ACESSORIA do
contrato de incorporacao. Resolvido o contrato principal por culpa
do incorporador, a garantia fiduciaria perde seu objeto.

EFEITO REGISTRAL OBRIGATORIO: No dispositivo da sentenca que
declarar resolvido o contrato com alienacao fiduciaria registrada,
INCLUIR determinacao de cancelamento do registro da alienacao
fiduciaria no Registro de Imoveis competente, sob pena de o
adquirente permanecer vinculado a garantia de contrato ja extinto.
[CONFIRMAR: verificar se ha exigencia de oficio ao RI ou se basta
a averbacao do mandado judicial]
```

**Dispositivo padrao — procedencia (resolucao por culpa do incorporador com AF registrada):**
```
Ante o exposto, julgo PROCEDENTE o pedido formulado por [ADQUIRENTE]
em face de [INCORPORADOR/CONSTRUTORA], para:
(a) DECLARAR resolvido o contrato de promessa de compra e venda
    [e o contrato acessorio de alienacao fiduciaria], por
    inadimplemento imputavel exclusivamente a parte reu;
(b) CONDENAR a parte reu a restituir ao autor o valor de
    R$ [valor] (totalidade das parcelas pagas), acrescido de
    SELIC unica desde a citacao (Tema 1.368/STJ);
(c) DETERMINAR o cancelamento do registro da alienacao fiduciaria
    constante da matricula n. [numero] do [X] Oficio de Registro
    de Imoveis de [Comarca], mediante expedicao de mandado;
(d) [demais verbas: danos morais, clausula penal invertida, etc.]

[Custas e honorarios pelo reu — art. 85, §2, CPC]

P.R.I.
```

**Dispositivo padrao — procedencia (nulidade do procedimento):**
```
Ante o exposto, julgo PROCEDENTE o pedido formulado por [DEVEDOR
FIDUCIANTE] em face de [CREDOR FIDUCIARIO], para:
(a) DECLARAR nulo o procedimento de execucao extrajudicial
    realizado sobre o imovel matricula n. [numero], por vicio
    na intimacao do devedor fiduciante;
(b) DETERMINAR o cancelamento da consolidacao da propriedade
    em nome do credor fiduciario junto ao [X] Oficio de Registro
    de Imoveis de [Comarca];
(c) RESTABELECER o contrato de alienacao fiduciaria em seus
    termos originais, assegurado ao autor o direito de purgacao
    da mora.

[Custas e honorarios pelo reu — art. 85, §2, CPC]

P.R.I.
```

**Dispositivo padrao — improcedencia (procedimento regular):**
```
Ante o exposto, julgo IMPROCEDENTE o pedido de [DEVEDOR FIDUCIANTE],
por verificar que o procedimento de execucao extrajudicial observou
todos os requisitos legais da Lei 9.514/1997, notadamente a regular
intimacao pessoal do devedor (art. 26, §1), a consolidacao da
propriedade (art. 26, §7) e a realizacao dos leiloes (art. 27).

[Custas e honorarios pelo autor — art. 85, §2, CPC]
[Se beneficiario de gratuidade: suspensao art. 98, §3, CPC]

P.R.I.
```

---

## Juros de Mora e Correcao Monetaria — Termos Iniciais

**ATENCAO:** O termo inicial dos juros de mora varia conforme a natureza da responsabilidade. Erro neste ponto e motivo frequente de embargos de declaracao.

### Responsabilidade Extracontratual (ilicito civil, CDC, acidente)

**REGRA POS-TEMA 1.368/STJ (a partir de 15/10/2025):**
```
SELIC UNICA desde o EVENTO DANOSO (convergencia Sumulas 54+362/STJ).
Inclui juros de mora + correcao monetaria em indice unico.
Vedada cumulacao com IPCA-E ou qualquer outro indice.

Dano MATERIAL: SELIC desde cada desembolso efetivo.
Dano MORAL: SELIC desde o evento danoso (antes era IPCA-E
desde arbitramento — Sumula 362/STJ convergida pelo Tema 1.368).
```

**Regra anterior (REFERENCIA HISTORICA — para periodos pre-Tema 1.368):**
```
Juros de mora: 1% a.m. desde o evento danoso (Sumula 54/STJ).
Correcao monetaria dano material: IPCA-E desde desembolso (Sumula 43/STJ).
Correcao monetaria dano moral: IPCA-E desde arbitramento (Sumula 362/STJ).
```

### Responsabilidade Contratual (inadimplemento de contrato)

**REGRA POS-TEMA 1.368/STJ:**
```
SELIC UNICA desde a CITACAO (art. 405, CC + Tema 1.368/STJ).
Se contrato preve taxa propria, aplica-se a contratual ate o
limite legal; apos inadimplemento, SELIC.
```

**Regra anterior (REFERENCIA HISTORICA):**
```
Juros de mora: 1% a.m. desde a citacao (art. 405, CC).
Correcao monetaria: IPCA-E desde o vencimento da obrigacao.
```

### Fazenda Publica — EC 113/2021 (art. 3)

**ATENCAO:** A EC 113/2021 (publicada em 09/12/2021) alterou profundamente o regime de atualizacao de debitos judiciais contra a Fazenda Publica. O regime anterior (IPCA-E + juros de mora separados) foi substituido pela SELIC unica.

```
REGIME ATUAL (apos 09/12/2021):
Debitos judiciais contra a Fazenda Publica: aplica-se
EXCLUSIVAMENTE a taxa SELIC, que ja ENGLOBA juros de mora
E correcao monetaria. Nao se cumulam IPCA + juros separados.
```

**Regras de transicao:**
```
PERIODO ANTERIOR a 09/12/2021:
- Correcao monetaria: IPCA-E (Tema 810/STF para Fazenda Federal;
  Tema 905/STJ para Fazenda Estadual/Municipal)
  [VERIFICAR teses completas dos Temas 810 e 905]
- Juros de mora: poupanca (art. 1-F, Lei 9.494/97, com redacao
  da Lei 11.960/2009, declarada parcialmente inconstitucional
  pelo STF nas ADIs 4357 e 4425)
  [VERIFICAR posicao atualizada do STF]

PERIODO POSTERIOR a 09/12/2021:
- Indice unico: SELIC (engloba juros + correcao)
- NAO cabe aplicar IPCA-E + juros separados neste periodo
```

**Termo inicial dos juros:**
```
- Debitos de natureza tributaria: desde o pagamento indevido
- Debitos de natureza nao-tributaria: desde a citacao
  (art. 405, CC, aplicavel subsidiariamente)
```

**Template de dispositivo — Fazenda Publica:**
```
[...] condeno a Fazenda Publica [Municipal/Estadual/Federal]
ao pagamento de R$ [valor], acrescido de:
(a) correcao monetaria pelo IPCA-E e juros de mora conforme
    [indice aplicavel] desde [termo inicial] ate 08/12/2021; e
(b) a partir de 09/12/2021, incidencia exclusiva da taxa SELIC,
    nos termos do art. 3 da EC 113/2021, que engloba juros de
    mora e correcao monetaria.

Nos termos do art. 100 da CF, o pagamento sera realizado por
[precatorio / requisicao de pequeno valor — RPV], observado o
limite de [X] salarios minimos para RPV no ambito [municipal/
estadual/federal].
```

**Precatorio vs. RPV — Limites:**

| Ente | Limite RPV | Fundamento |
|------|-----------|------------|
| Uniao | 60 salarios minimos | Art. 17, §1, Lei 10.259/2001 |
| Estados/DF | 40 salarios minimos (regra geral, pode variar) | Art. 87, I, ADCT (verificar lei estadual) |
| Municipios | 30 salarios minimos (regra geral, pode variar) | Art. 87, II, ADCT (verificar lei municipal) |

[VERIFICAR limites atualizados — estados e municipios podem fixar limites proprios por lei]

### Indice de Correcao — Relacoes Privadas (pos-Tema 1.368/STJ)
```
REGRA GERAL (a partir de 15/10/2025 — Tema 1.368/STJ):
SELIC e o indice UNICO para atualizacao de dividas civis,
incluindo relacoes privadas. Substitui a formula anterior
(1% a.m. + IPCA-E). Vedada cumulacao SELIC + IPCA-E (bis in idem).

REsp 2.199.164/PR e 2.070.882/RS, Min. Villas Boas Cueva,
Corte Especial, 15/10/2025. Endosso constitucional: STF RE
1.558.191/SP, Min. Andre Mendonca, set/2025.

ATENCAO: A regra anterior (IPCA-E + 1% a.m.) estava INCORRETA
neste campo — a SELIC agora e para TODAS as dividas civis,
nao apenas para Fazenda Publica.
```

---

## Tratamento da Tutela Provisoria na Sentenca

Quando houver pedido de tutela de urgencia (deferida ou indeferida antes da sentenca), INCLUIR tratamento expresso no dispositivo:

### Se a tutela foi DEFERIDA e a sentenca e de procedencia
```
Confirmo a tutela de urgencia anteriormente deferida (fls. XX),
que subsistira ate o transito em julgado, nos termos do
art. 1.012, §1, V, do CPC.
```

### Se a tutela foi DEFERIDA e a sentenca e de improcedencia
```
Revogo a tutela de urgencia anteriormente deferida (fls. XX),
cessando seus efeitos com a publicacao desta sentenca.
```

### Se a tutela foi INDEFERIDA e a sentenca e de procedencia
```
[Nao ha necessidade de mencionar a tutela indeferida — a
sentenca de procedencia ja atende ao pedido. Caso haja
interesse em eficacia imediata, fundamentar com art. 1.012,
§1, CPC]
```

### Se houve pedido mas NAO foi apreciado
```
Quanto a tutela de urgencia requerida, julgo prejudicado o
pedido ante o julgamento do merito da demanda.
```

### Recurso cabivel
```
Registre-se que a presente sentenca esta sujeita a recurso de
apelacao, no prazo de 15 (quinze) dias uteis (art. 1.009, CPC),
a ser dirigido ao Tribunal de Justica do Estado do Espirito
Santo.
```

---

## Formulas para Honorarios Advocaticios (art. 85, CPC)

**Regra geral:**
```
Os honorarios advocaticios sao fixados em [X]% sobre [o valor da
condenacao / o valor da causa / o valor arbitrado na liquidacao],
nos termos do art. 85, §§ 2 e 3, do CPC/2015, observados os criterios
do grau de zelo profissional, lugar de prestacao do servico, natureza e
importancia da causa, trabalho realizado e tempo exigido.
```

**Para Fazenda Publica (art. 85, §§ 3 e 8):**
```
Condeno a Fazenda Publica ao pagamento de honorarios advocaticios,
fixados sobre o valor da condenacao conforme a escala do art. 85, § 3,
do CPC/2015:
- Ate 200 salarios minimos: [X]% (entre 10% e 20%)
- De 200 a 2.000 SM: [Y]% (entre 8% e 10%)
[...]
```

---

## Sucumbencia Reciproca — Calculo e Reparticao (art. 86, CPC)

Quando a sentenca for de **procedencia parcial**, o juiz deve calcular a proporcao de sucumbencia de cada parte e distribuir honorarios e custas proporcionalmente.

### Metodologia de Calculo

**Passo 1 — Listar TODOS os pedidos formulados pelo autor:**
```
| # | Pedido | Valor estimado | Resultado |
|---|--------|----------------|-----------|
| 1 | [Pedido 1] | R$ [valor] | PROCEDENTE |
| 2 | [Pedido 2] | R$ [valor] | IMPROCEDENTE |
| 3 | [Pedido 3] | R$ [valor] | PROCEDENTE |
| 4 | [Pedido 4] | R$ [valor] | PROCEDENTE EM PARTE |
```

**Passo 2 — Calcular a proporcao:**
```
Valor total dos pedidos: R$ [soma de todos]
Valor acolhido: R$ [soma dos procedentes + parcial]
Proporcao do AUTOR (venceu): [valor acolhido / valor total] = X%
Proporcao do REU (venceu): [1 - X%] = Y%
```

**Passo 3 — Aplicar a proporcao aos honorarios e custas:**
```
Honorarios: cada parte pagara ao advogado da parte contraria
na proporcao de sua sucumbencia.
- Reu paga ao advogado do autor: [X]% x [base de calculo]
- Autor paga ao advogado do reu: [Y]% x [base de calculo]
Custas: repartidas na mesma proporcao ([X]% autor, [Y]% reu).
```

### Hipoteses Especiais

| Situacao | Regra | Fundamento |
|----------|-------|------------|
| **Sucumbencia minima do autor** | Reu arca com totalidade dos honorarios e custas | Art. 86, paragrafo unico, CPC |
| **Sucumbencia reciproca equivalente** | Repartir igualmente (50/50) | Art. 86, caput, CPC |
| **Pedido sem valor certo** (dano moral) | Usar o valor ARBITRADO na sentenca como parametro | Jurisprudencia STJ |
| **Autor beneficiario de gratuidade** | Obrigacao de pagar honorarios ao advogado do reu fica SUSPENSA (art. 98, §3, CPC) por 5 anos | Art. 98, §3, CPC |

### Templates de Dispositivo

**Sucumbencia reciproca proporcional:**
```
Diante da procedencia parcial dos pedidos, reconheco a
sucumbencia reciproca das partes na proporcao de [X]% para
o reu e [Y]% para o autor, considerando que dos R$ [valor
total] pedidos, foram acolhidos R$ [valor acolhido].

Condeno o reu ao pagamento de honorarios advocaticios ao
patrono do autor, fixados em [Z]% sobre o valor da
condenacao (R$ [valor acolhido]), nos termos do art. 85,
§2, do CPC.

Condeno o autor ao pagamento de honorarios advocaticios ao
patrono do reu, fixados em [Z]% sobre o valor dos pedidos
rejeitados (R$ [valor rejeitado]), nos termos do art. 85,
§2, do CPC. [Se beneficiario de gratuidade: "Tal obrigacao
fica sob condicao suspensiva de exigibilidade, nos termos
do art. 98, §3, do CPC, pelo prazo de 5 (cinco) anos."]

Custas processuais repartidas na proporcao de [X]% para o
reu e [Y]% para o autor. [Se gratuidade: observar art. 98,
§3, CPC]
```

**Sucumbencia minima do autor:**
```
Considerando que o autor decaiu de parte MINIMA do pedido
(apenas [detalhar — ex: quantum do dano moral reduzido de
R$ 15.000 para R$ 10.000]), condeno o reu ao pagamento
integral dos honorarios advocaticios, fixados em [Z]%
sobre o valor da condenacao, e das custas processuais, nos
termos do art. 86, paragrafo unico, do CPC.
```

**Vedacao de compensacao (art. 85, §14, CPC):**
```
IMPORTANTE: Os honorarios advocaticios sao direito do
ADVOGADO (art. 85, §14, CPC) e NAO podem ser compensados
entre si. Cada parte paga diretamente ao advogado da parte
contraria na proporcao fixada.
```

---

## Checklist Pre-Sentenca

Antes de redigir, verificar:

- [ ] Partes corretamente identificadas (qualificacao completa)
- [ ] Numero CNJ do processo
- [ ] Pedidos do autor mapeados (certos, determinados e cumulados)
- [ ] Defesas/excecoes do reu mapeadas
- [ ] Provas produzidas catalogadas
- [ ] Prescricao/decadencia verificadas
- [ ] Questoes preliminares identificadas
- [ ] Normas aplicaveis (CC, CDC, CPC, CF, legislacao especial)
- [ ] Sumulas e teses vinculantes aplicaveis (STJ/STF) — numeros verificados
- [ ] Valor para honorarios
- [ ] Custas processuais (isencao, gratuidade judiciaria)
- [ ] Protocolo anti-alucinacao aplicado em todas as citacoes

---

## Linguagem e Estilo Judicial

**Evitar:**
- Gerundio excessivo: "estando presentes" -> "presentes estao"
- Expressoes coloquiais
- Prolixidade desnecessaria na fundamentacao
- Transcricao integral de peticoes

**Preferir:**
- Construcoes objetivas e diretas
- Citacao as normas com artigo e codigo/lei
- Remissao as sumulas pelo numero
- Fundamentacao analitica (nao apenas citacao de precedentes)

**Tom:** tecnico, impessoal, imparcial, fundamentado (art. 489, CPC).

---

## Common Mistakes

| Erro | Como evitar |
|------|------------|
| Citar Sumula com numero inventado | Protocolo anti-alucinacao — Nivel 2 ou 3 se nao tiver certeza |
| Relatorio como copia da peticao | Sintetizar os fatos relevantes em linguagem propria |
| Fundamentacao generica ("conforme jurisprudencia dominante") | Citar norma + demonstrar subsuncao ao caso concreto (art. 489, §1) |
| Nao enfrentar argumento da parte contraria | Art. 489, §1, IV — todos os argumentos capazes de infirmar devem ser enfrentados |
| Dispositivo ambiguo | Ser explicito: "julgo PROCEDENTE o pedido para CONDENAR o reu a..." |
| Esquecer honorarios ou custas | Sempre incluir no dispositivo — verificar o checklist |
| Confundir resp. subjetiva com objetiva | Verificar se ha previsao legal de risco (art. 927, p.u.) ou relacao de consumo |
| Negativacao indevida + inscricao preexistente | Sumula 385/STJ afasta dano moral se ha anotacao legitima anterior |
| Aplicar 1% a.m. + IPCA-E apos Tema 1.368 (15/10/2025) | SELIC unica para dividas civis — formula antiga superada |
| SELIC + IPCA-E cumulados | SELIC ja inclui juros + correcao (bis in idem — Tema 1.368/STJ) |

---

## Workflow de Uso

1. **Receber** a sintese dos fatos (ou peticao inicial + contestacao)
2. **Identificar** a area do direito e o template aplicavel
3. **Mapear** os pedidos e as defesas
4. **Selecionar** as normas e precedentes relevantes
5. **Aplicar** protocolo anti-alucinacao nas citacoes
6. **Redigir** seguindo a estrutura FIRAC-JB
7. **Verificar** o checklist pre-sentenca (incluindo art. 489, §1)
8. **Entregar** a minuta para revisao do magistrado
