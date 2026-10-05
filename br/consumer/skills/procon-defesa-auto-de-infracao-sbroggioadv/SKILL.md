---
name: procon-defesa-auto-de-infracao-sbroggioadv
title: PROCON — auto de infração e defesa administrativa
description: 'Estrutura a defesa administrativa do fornecedor autuado pelo PROCON (instauração, auto de infração, requisitos formais, prazo de impugnação) e explica ao consumidor como funciona a reclamação administrativa que pode originar o processo. Base: Decreto 2.181/1997 (SNDC), redação vigente dada pelo Decreto 10.887/2021. Trava crítica: o prazo de defesa NÃO é mais 10 dias, é 20 dias. Aciona: montar defesa/ impugnação de auto de infração PROCON, orientar consumidor sobre reclamação no PROCON, avaliar requisitos formais do auto de infração, decidir sobre averiguação preliminar, calcular prazo de notificação e defesa administrativa.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/procon-defesa-auto-de-infracao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# PROCON — auto de infração e defesa administrativa

## Quando esta skill entra
Quando o fornecedor recebe auto de infração ou notificação de instauração de processo
administrativo sancionador (PAS) do PROCON e precisa montar a defesa; ou quando o
consumidor quer entender como funciona sua reclamação no órgão. Skill DUAL.

## Base normativa
Decreto 2.181/1997 (SNDC), redação vigente dada pelo **Decreto 10.887/2021** — arts.
33 a 45 (`context/decreto-2181-sndc-sancoes.md`, capturado do Planalto em 18/08/2026).

## O passo a passo administrativo

**1. Instauração (art. 33).** Por ato escrito da autoridade competente ou lavratura de
auto de infração — desde 2021 a "reclamação" deixou de ser, por si só, forma autônoma
de instauração (inciso III do art. 33 foi revogado); a reclamação do consumidor (art.
34) hoje **orienta a implementação de políticas públicas** e pode desencadear
averiguação preliminar ou instauração de ofício, mas não abre PAS automaticamente.

**2. Averiguação preliminar (arts. 33-A e 33-B), quando os indícios ainda não bastam**
para abrir PAS direto — procedimento inquisitorial que resulta em instauração de PAS
ou arquivamento. Arquivamento pode ser avocado pelo superior hierárquico em até 20
dias da publicação.

**3. Auto de infração (art. 35, I)** deve conter, sob pena de vício: local/data/hora;
identificação do autuado; descrição do fato/ato constitutivo; dispositivo legal
infringido; determinação da exigência e intimação para cumprir ou impugnar no prazo
do art. 42; identificação e assinatura do agente autuante; designação do órgão
julgador; assinatura do autuado; e cientificação para especificar provas, inclusive
até 3 testemunhas qualificadas.

**4. Notificação (art. 42, redação 2021).** "A autoridade competente expedirá
notificação ao infrator e fixará prazo de **vinte dias**, contado da data de seu
recebimento pelo infrator, para apresentação de defesa" (Decreto 2.181/1997, art. 42,
redação dada pelo Decreto 10.887/2021). Formas: carta registrada com AR; outro meio
físico/eletrônico que assegure a certeza da ciência; mecanismos de cooperação
internacional. O comparecimento espontâneo do representado supre falta ou nulidade da
notificação (art. 42, §3º) — e a partir dele começa a contar o prazo de defesa.

**5. Defesa/impugnação (art. 44).** No mesmo prazo de 20 dias, indicando: autoridade
decisória; qualificação do impugnante; razões de fato e de direito; e as provas que
pretende produzir, com qualificação completa de até 3 testemunhas.

**6. Classificação da infração (art. 17).** Leve = só circunstâncias atenuantes.
Grave = há circunstância agravante. Os catálogos de conduta estão nos arts. 12, 13,
19, 20 e 22 (cláusula abusiva) do próprio decreto.

**7. Fiscalização orientadora e dupla visita (art. 38-A).** Para atividade de risco
leve/irrelevante/inexistente (Lei 13.874/2019), a fiscalização deve ser
prioritariamente orientadora, com critério de **dupla visita antes de lavrar auto de
infração** — exceto reincidência, fraude, resistência ou embaraço à fiscalização. A
inobservância da dupla visita **anula o auto de infração** (art. 38-A, §2º).

## Tese do consumidor (como funciona a reclamação)
A reclamação pode ser apresentada pessoalmente ou por telegrama, carta, fac-símile ou
qualquer outro meio de comunicação físico ou eletrônico, a qualquer órgão do SNDC
(art. 34). Ela não gera, por si, instauração automática de processo sancionador
(regime pós-2021) — mas alimenta a política do órgão e pode desencadear averiguação
preliminar de ofício. Se a investigação preliminar não resultar em PAS, o consumidor
deve ser informado das razões do arquivamento.

## Tese do fornecedor (a defesa)
Atacar, na ordem: (a) requisitos formais do auto (art. 35, I) — enquadramento legal
genérico ou dispositivo mal identificado é vício; (b) validade e forma da notificação;
(c) se atividade de risco leve, se houve dupla visita antes da autuação — ausência
anula o auto (art. 38-A, §2º); (d) mérito da prática infrativa, com provas e até 3
testemunhas. Cuidado: comparecer espontaneamente sem impugnar formalmente sana
qualquer vício de notificação e já dispara o prazo de defesa.

## Armadilhas
- **T9 — o prazo de defesa NÃO é 10 dias, é 20 dias** desde o Decreto 10.887/2021.
  Qualquer defesa fundada em "10 dias" está citando texto revogado.
- Dupla visita é causa de **nulidade**, não recomendação, quando a atividade é de
  risco leve — tese de defesa pouco explorada e forte.
- T13 — ao conferir citação contra `context/decreto-2181-sndc-sancoes.md`, normalizar
  o espaço em branco antes de comparar (o HTML do Planalto quebra linha no meio da
  frase); grep de frase literal pode dar falso negativo.

## Fronteira
Dosimetria da multa, recurso administrativo e teses de anulação judicial →
`procon-dosimetria-e-anulacao` (não duplicar aqui). Consumidor.gov.br como
atenuante/alavanca pré-processual → `consumidor-gov-br-e-pre-processual`.
