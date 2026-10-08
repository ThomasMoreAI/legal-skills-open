---
name: revelia-e-contestacao-jec-sbroggioadv
title: Revelia e contestação no JEC
description: 'Trata da revelia no JEC — que não é automática, mesmo com ausência do réu — e da contestação oral ou escrita. Cobre a revelia da pessoa jurídica que contesta mas não comparece, a vedação de reconvenção com a alternativa do pedido contraposto, e a vedação de intervenção de terceiro e de assistência, que impede a denunciação da lide. Aciona: avaliar se a ausência do fornecedor gera revelia, redigir contestação no JEC, formular pedido contraposto, avaliar se cabe trazer terceiro (fabricante, seguradora) ao processo.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/revelia-e-contestacao-jec
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# Revelia e contestação no JEC

## Quando esta skill entra
Quando o réu não comparece ou não contesta, ou quando se avalia se cabe reconvenção, pedido
contraposto ou trazer terceiro ao processo.

## Base normativa
Lei 9.099/1995, arts. 10, 20, 30 e 31 (anexo `context/lei-9099-jec.md`); FONAJE, Enunciados 11,
27, 31, 78, 167, 173 (anexo `context/jec-fonaje-e-recursos.md`).

## Revelia não é automática
Art. 20: "Não comparecendo o demandado à sessão de conciliação ou à audiência de instrução e
julgamento, reputar-se-ão verdadeiros os fatos alegados no pedido inicial, **salvo se o contrário
resultar da convicção do Juiz**." A presunção de veracidade é relativa — o juiz pode afastá-la se
os elementos dos autos convencerem em sentido contrário, mesmo sem manifestação do réu ausente.

## Revelia da pessoa jurídica
Não há enunciado do FONAJE que trate a revelia de pessoa jurídica como categoria distinta da
revelia de pessoa física — os Enunciados 11 e 78 são gerais e valem para qualquer réu, incluída a
PJ. O que muda para a PJ é o **modo** de evitar a revelia: como o art. 9º, §4º permite
representação por preposto (ver `preposto-e-representacao-jec`), a PJ evita revelia comparecendo
com preposto credenciado e contestando — mas duas obrigações são **cumulativas**, não alternativas:

| Enunciado | Regra |
|---|---|
| 11 | Nas causas de valor superior a 20 salários mínimos, a ausência de contestação — escrita ou oral —, mesmo com o réu presente, implica revelia. |
| 78 | O oferecimento de resposta, oral ou escrita, não dispensa o comparecimento pessoal da parte, ensejando os efeitos da revelia. |
| 167 | Não se aplica ao JEC a necessidade de publicação no Diário Eletrônico quando o réu for revel (art. 346 do CPC). |

Ou seja: para evitar revelia em causa acima de 20 SM, não basta comparecer — é preciso contestar
(Enunciado 11); e para evitar em qualquer valor, não basta contestar por escrito — é preciso
comparecer, pessoalmente ou por preposto (Enunciado 78). Fornecedor que só protocola contestação
sem comparecer à audiência (preposto ausente) sofre revelia mesmo com a peça de defesa nos autos.

## Contestação
Art. 30: a contestação, oral ou escrita, contém toda a matéria de defesa, exceto arguição de
suspeição ou impedimento do juiz, que segue a legislação em vigor (processada à parte).

## Não cabe reconvenção — cabe pedido contraposto
Art. 31: "Não se admitirá a reconvenção. É lícito ao réu, na contestação, formular pedido em seu
favor, nos limites do art. 3º desta Lei, desde que fundado nos mesmos fatos que constituem objeto
da controvérsia." O autor responde ao pedido contraposto na própria audiência ou pede nova data,
desde logo fixada (parágrafo único).

| Enunciado | Regra |
|---|---|
| 27 | Em pedido de até 20 SM, é admitido pedido contraposto em valor superior ao da inicial, até 40 SM, com assistência obrigatória de advogados às duas partes. |
| 31 | É admissível pedido contraposto quando a parte ré é pessoa jurídica. |
| 173 | A extinção ou desistência da ação originária prejudica a apreciação do pedido contraposto. |

## Não cabe intervenção de terceiro nem assistência
Art. 10: "Não se admitirá, no processo, qualquer forma de intervenção de terceiro nem de
assistência. Admitir-se-á o litisconsórcio." Isso **mata a denunciação da lide** — o fornecedor
réu não pode trazer o fabricante, a seguradora ou outro corresponsável ao processo depois de
citado; só é admitido o litisconsórcio de partes que já nascem no polo desde o início.

## Tese do consumidor
Se o fornecedor comparece sem contestar (causa acima de 20 SM) ou contesta por escrito mas não
comparece à audiência, requerer a decretação de revelia com base nos Enunciados 11 e 78 — a
presença de peça de defesa nos autos não afasta o efeito. Se o réu tentar "reconvir" cobrando algo
do consumidor no mesmo processo, apontar que a via correta é o pedido contraposto (art. 31), não a
reconvenção, que é vedada. Se o consumidor desistir da ação original, o pedido contraposto do
fornecedor cai junto (Enunciado 173) — ferramenta útil de negociação.

## Tese do fornecedor
Mesmo sendo pessoa jurídica, pode formular pedido contraposto (Enunciado 31), inclusive em valor
maior que o pedido do consumidor, até 40 SM, desde que a causa original seja de até 20 SM e as
duas partes estejam assistidas por advogado (Enunciado 27) — sem advogado nos autos, o pedido
contraposto de valor superior não é admissível nessa forma ampliada. Se quiser trazer o fabricante
ou a seguradora ao processo por denunciação da lide, não há como — art. 10 veda; a alternativa é
discutir o ressarcimento em ação autônoma, fora do JEC.

## Armadilhas
Não confundir pedido contraposto com reconvenção — são institutos distintos e só o primeiro cabe.
Revelia da PJ segue as regras gerais (11 e 78); não existe regime FONAJE específico de revelia de
pessoa jurídica.

## Fronteira
Perícia e complexidade que afastam a competência → `competencia-jec-x-comum`. Rito e prazos →
`rito-jec-consumidor`. Recurso da sentença → `recurso-inominado-turma-recursal`.
