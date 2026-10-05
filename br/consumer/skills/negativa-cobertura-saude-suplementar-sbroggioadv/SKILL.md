---
name: negativa-cobertura-saude-suplementar-sbroggioadv
title: Negativa de cobertura — saúde suplementar
description: 'Estrutura a ação contra negativa genérica de cobertura por plano de saúde pela ótica contrato/CDC/ANS — rol da ANS como referência básica, o teste dos cinco requisitos cumulativos da ADI 7265/STF para tratamento fora do rol, a Súmula 608/STJ e a inversão do ônus da prova. Não é a via clínico-oncológica (isso é do direito-medico-adv-os). Aciona: negativa de cobertura, glosa, autorização negada, procedimento fora do rol, recusa de exame ou cirurgia pelo plano de saúde, tratamento fora do rol da ANS.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/negativa-cobertura-saude-suplementar
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Negativa de cobertura — saúde suplementar

## Quando esta skill entra

Toda negativa (ou demora/omissão equivalente à negativa) de autorização por operadora de
plano de saúde para procedimento, exame, cirurgia, material ou medicamento — dentro ou
fora do rol da ANS —, pela ótica **contratual/CDC/ANS**. Não é a via clínico-oncológica
específica (`acao-negativa-cobertura-oncologica` do `direito-medico-adv-os`) nem TEA, OPME
ou home care clínico — ver Fronteira.

## Base normativa

- **Lei 9.656/1998, art. 10, § 12** (redação da Lei 14.454/2022): o rol da ANS é
  **referência básica** para os planos contratados a partir de 01/01/1999.
- **Lei 9.656/1998, art. 10, § 13**: fora do rol, a cobertura deve ser autorizada quando
  há prescrição do médico/odontólogo assistente **e** (I) comprovação de eficácia
  científica **ou** (II) recomendação da Conitec/órgão de renome internacional.
- **CDC (Lei 8.078/1990), art. 6º, VIII**: inversão do ônus da prova a favor do
  consumidor, a critério do juiz, quando verossímil a alegação ou hipossuficiente o
  consumidor.
- **Súmula 608/STJ** (vigente): aplica-se o CDC aos contratos de plano de saúde, **salvo
  os administrados por entidades de autogestão**.

## O teste — cinco requisitos cumulativos da ADI 7265/STF (Pleno, 18/09/2025)

O § 13 do art. 10 conecta os incisos por "ou" — mas o STF, em interpretação conforme com
efeito vinculante, endureceu o teste: cobertura fora do rol só é devida com os **cinco
requisitos abaixo, cumulativamente**. Redigir a peça só com o "ou" do § 13 é redigir para
perder — a defesa da operadora tem a ADI 7265 como tese central, reafirmada pelo STF em
abril/2026 ("cobertura fora do rol exige prova técnica").

1. **Prescrição** por médico ou odontólogo assistente habilitado — junte o laudo/relatório.
2. **Inexistência de negativa expressa da ANS**, nem pendência de análise em Proposta de
   Atualização do Rol (PAR) — verifique se há PAR em curso sobre o item.
3. **Ausência de alternativa terapêutica adequada** já prevista no rol — a peça precisa
   afastar, com o laudo do assistente, cada alternativa listada que a operadora invocar.
4. **Eficácia e segurança comprovadas** por medicina baseada em evidências de alto grau
   ou Avaliação de Tecnologias em Saúde (ATS) — artigos, protocolos, ATS.
5. **Registro na Anvisa** do tratamento/medicamento/dispositivo.

Prove os cinco, um a um, com documento próprio para cada requisito — não basta afirmar que
"a lei prevê". O ônus de provar é de quem pede (CPC, art. 373), mitigado pela inversão do
art. 6º, VIII do CDC quando cabível.

## Tese do beneficiário × tese da operadora

**Beneficiário**: reúne prescrição + evidência científica + registro Anvisa + inexistência
de PAR pendente + ausência de alternativa no rol; pede inversão do ônus (CDC art. 6º, VIII);
sustenta que a negativa é abusiva por descumprir o § 13 já testado pela ADI 7265.

**Operadora**: nega afirmando faltar um dos cinco requisitos (normalmente: existe
alternativa no rol, ou não há prova de eficácia de alto grau, ou item está em PAR
pendente) — a ADI 7265 é a peça central da contestação. Alegar autogestão para afastar o
CDC (Súmula 608) só se a operadora for efetivamente entidade de autogestão.

## Armadilhas

- **T1** — a Súmula 469/STJ está **cancelada** desde 2018. Não citar. A vigente é a **608**,
  já com a exceção de autogestão embutida no enunciado.
- **T3** — nunca fundamentar a cobertura fora do rol só no "ou" do § 13 isolado. A régua
  vigente é a soma dos **cinco requisitos cumulativos da ADI 7265** — uma peça que ignora
  isso está desatualizada em jurisprudência vinculante.
- **T5** — não hardcodar o número da RN do Anexo do rol (base: RN 465/2021, Anexo
  atualizado periodicamente). Instrua o cliente a conferir a versão vigente do Anexo em
  `gov.br/ans` na data do caso concreto antes de protocolar.

## Fronteira

- Negativa **clínico-oncológica** específica (quimio, imuno, radio, PET-CT, transplante):
  `acao-negativa-cobertura-oncologica` (`direito-medico-adv-os`).
- **TEA** (ABA, fono, TO): `acao-tea-multidisciplinar` (`direito-medico-adv-os`).
- **OPME** (prótese/órtese com marca imposta): `acao-opme` (`direito-medico-adv-os`).
- **Home care** clínico (critério de indicação): `acao-home-care` (`direito-medico-adv-os`);
  o lado contratual do home care está em `contrato-rede-credenciada-saude`.
- Precisa de liminar: `tutela-urgencia-cobertura-saude`.
- Rito comum fora do JEC: `civel-adv-os`.
