---
name: tutela-urgencia-cobertura-saude-sbroggioadv
title: Tutela de urgência — cobertura de saúde suplementar
description: 'Estrutura o pedido de tutela de urgência (CPC art. 300) em ação de negativa de cobertura de saúde suplementar — probabilidade do direito ancorada nos cinco requisitos da ADI 7265/STF, perigo de dano tempo-dependente, reversibilidade e astreintes. Peça processual do módulo consumidor, distinta da tutela-urgencia-plano-saude do direito-medico-adv-os (que é modelo processual reutilizável das ações Tier-5 do médico). Aciona: liminar em plano de saúde, tutela de urgência cobertura, urgência médica negada, pedido de liminar contra operadora, tratamento negado com risco de vida.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/tutela-urgencia-cobertura-saude
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# Tutela de urgência — cobertura de saúde suplementar

## Quando esta skill entra

Sempre que a demora do trâmite ordinário coloca em risco a saúde ou a vida do beneficiário
diante de negativa (ou demora/omissão) de cobertura — o pedido de liminar acopla à ação de
`negativa-cobertura-saude-suplementar`, não a substitui.

## Base normativa

- **CPC, art. 300**: tutela de urgência concedida quando houver elementos que evidenciem a
  **probabilidade do direito** e o **perigo de dano** ou o **risco ao resultado útil do
  processo**.
- **CPC, art. 373**: ônus da prova de quem alega — mitigado pela inversão do CDC, art. 6º,
  VIII, quando cabível.
- **Súmula 597/STJ**: é abusiva a cláusula que prevê carência para urgência/emergência além
  de **24 horas** contadas da contratação — reforça o fumus quando o caso é de urgência
  contratual recente.

## O teste — probabilidade do direito ancorada na ADI 7265/STF

A cognição é sumária, mas a probabilidade do direito **hoje** se mede pelos mesmos cinco
requisitos cumulativos fixados pelo STF na ADI 7265 (Pleno, 18/09/2025), reafirmados em
abril/2026 ("cobertura fora do rol exige prova técnica") — só que em juízo de
verossimilhança, não de prova plena:

1. Prescrição do médico/odontólogo assistente (junte o relatório/laudo).
2. Inexistência de negativa expressa da ANS ou de PAR pendente sobre o item.
3. Ausência de alternativa terapêutica adequada já prevista no rol.
4. Indício de eficácia e segurança por evidência científica de alto grau ou ATS.
5. Indício de registro na Anvisa.

**Perigo de dano** é tempo-dependente: junte documento datado que mostre a janela clínica
(prazo até a piora previsível, urgência da cirurgia, risco de progressão da doença) — não
basta alegar urgência em tese.

**Reversibilidade**: avalie se a medida é reversível; se não for (ex.: cirurgia), reforce a
prova dos cinco requisitos e, se o juízo exigir, ofereça caução idônea (CPC, art. 300, § 1º).

**Efetivação**: peça multa diária (astreintes, CPC art. 537) fixada em valor que
efetivamente pressione a operadora, e prazo curto para cumprimento (autorização em 24-48h,
compatível com a urgência alegada).

## Tese do beneficiário × tese da operadora

**Beneficiário**: reforça o fumus com os cinco requisitos + prova da urgência
tempo-dependente; pede efetivação imediata com astreintes; se o caso for urgência/emergência
contratual recente, soma a Súmula 597 ao teste da ADI 7265.

**Operadora**: ataca o fumus alegando ausência de um ou mais dos cinco requisitos — hoje é
a linha de defesa mais forte pós-ADI 7265 (existe alternativa no rol, falta evidência de alto
grau, item está em PAR pendente); pode arguir irreversibilidade para pedir caução ou
suspensão da liminar.

## Armadilhas

- **T3** — não fundamentar o fumus só na leitura "ou" do § 13 da Lei 9.656. Em cognição
  sumária, os cinco requisitos da ADI 7265 continuam sendo a régua — a diferença é o grau
  de prova exigido (indício, não prova plena).
- **T5** — não hardcodar o número da RN do Anexo do rol ao afastar a "alternativa
  terapêutica adequada" alegada pela operadora; confirme o Anexo vigente na data do caso.

## Fronteira

- A ação de fundo é `negativa-cobertura-saude-suplementar` — esta skill é só a peça de
  urgência.
- Mérito clínico-oncológico/TEA/OPME/home care: skills correspondentes do
  `direito-medico-adv-os` (ver Fronteira em `negativa-cobertura-saude-suplementar`).
- O `direito-medico-adv-os` tem sua própria `tutela-urgencia-plano-saude` (modelo
  processual reutilizável das ações Tier-5 dele) — não é a mesma peça; não confundir os
  dois nomes.
