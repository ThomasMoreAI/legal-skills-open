---
name: varredura-jurisprudencial-pre-tese-sbroggioadv
title: Varredura Jurisprudencial Pré-Tese
description: 'Gate de processo obrigatório antes de redigir qualquer peça — varre o entendimento atual do tribunal de destino, confere se a súmula/tema citado está vivo (não cancelado, não superado por embargos, não pendente sem declaração), aplica as 13 travas de defasagem T1-T13 do corpus e manda consultar o juris-adv-os para validar citações fora deste plugin. Não decide mérito, só impede que a peça saia com número morto ou inventado. Aciona: sempre, antes de redigir inicial, contestação, recurso ou parecer que cite súmula, tema repetitivo, resolução ou precedente.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/varredura-jurisprudencial-pre-tese
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Varredura Jurisprudencial Pré-Tese

## Quando esta skill entra
**Sempre, antes de redigir qualquer peça** — inicial, contestação, recurso, parecer — que cite
súmula, tema repetitivo, artigo de lei ou precedente. É um gate de **processo**, não de mérito:
não decide qual tese é melhor, decide se a peça está prestes a citar algo morto, cancelado,
superado ou pendente sem declarar a pendência.

## O teste / o passo a passo
1. **Toda citação de súmula/tema/artigo na peça passa por esta lista antes de ir para o papel.**
   Se o número não estiver confirmado nos anexos deste `context/`, a resposta é
   `[VERIFICAR — não confirmado no corpus]` — nunca completar de memória.
2. **Confira as 13 travas de defasagem (T1-T13, `context/travas-defasagem.md`) uma a uma** contra
   o tema da peça — a lista abaixo resume as que mais aparecem em petição real:
   - **T1** — Súmula 469/STJ está CANCELADA (2018); a vigente é a **608** (CDC aplicável a plano
     de saúde, salvo autogestão).
   - **T2** — "Súmula 194/STJ" para corte de serviço público por débito pretérito **não existe** —
     é jurisprudência reiterada, não sumulada; o Tema 699/STJ cobre só fraude no medidor.
   - **T3** — cobertura fora do rol da ANS exige os 5 requisitos cumulativos da ADI 7265/STF.
   - **T4** — Tema 987/STF (responsabilidade de plataforma) vale na redação **pós-embargos de
     17/06/2026** — responsabilidade solidária, presunção relativa de culpa.
   - **T5** — não hardcodar número de RN do rol da ANS; a base é a RN 465/2021, o Anexo muda.
   - **T6** — repetição em dobro (Tema 929) tem modulação: só dispensa má-fé para cobranças a
     partir de **30/03/2021**.
   - **T7** — Reclamação ao STJ contra acórdão de Turma Recursal **não cabe** desde 2016; do JEC,
     RE cabe, REsp não cabe.
   - **T8** — demanda predatória é a Recomendação CNJ **159/2024** + Tema 1.198/STJ, não a
     127/2022.
   - **T9** — prazo de defesa no PROCON: conferir o vigente, **não** é mais 10 dias por padrão.
   - **T10** — adesão do fornecedor privado ao consumidor.gov.br é **voluntária**; Tema 1.396/STJ
     está afetado, não resolvido.
   - **T11** — Convenção de Montreal/Varsóvia limita só dano **material** (Tema 210/STF); dano
     moral segue o CDC.
   - **T12** — no JEC: prazos em dias úteis, MEI/ME/EPP podem propor, embargos interrompem prazo,
     sem reconvenção/intervenção de terceiro/rescisória, preparo em 48h.
   - **T13** — normalizar espaço em branco ao comparar citação contra o `context/` (o HTML do
     Planalto quebra linha no meio da frase).
3. **Verifique se a súmula/tema ainda está vivo** — cancelada, superada por embargos, ou pendente
   de julgamento (🟡 nos anexos)? Se pendente, a peça **declara a divergência**, não escolhe um
   lado escondendo o outro (regra de ouro do `CONTRATO-DE-BUILD.md`).
4. **Consulte o `juris-adv-os`** quando precisar validar uma citação que não está nos anexos deste
   plugin — ele confirma se a URL resolve e se o trecho da ementa está na página, antes de a
   citação ir para a peça.
5. Só depois de 1-4 concluídos, redigir.

## Tese do consumidor × Tese do fornecedor
Gate de processo — aplica-se **igualmente** aos dois lados. Uma tese do consumidor fundada em
súmula cancelada perde a mesma força que uma tese do fornecedor fundada em número inventado: nos
dois casos, o adversário que checar a fonte desmonta a peça em uma linha.

## Armadilhas
- Confiar na memória de treino do modelo para número de súmula/tema — o corte de conhecimento é
  anterior a boa parte da jurisprudência deste corpus (capturado 18/08/2026); a fonte sempre vence
  a memória.
- Aceitar citação de fonte secundária (blog jurídico, Jusbrasil) sem confirmação em fonte oficial
  — o corpus já registrou um caso real de citação errada ("Súmula 194") se propagando entre
  fontes secundárias.
- Tratar um achado 🟡 (divergência/pendente) como resolvido só porque é mais conveniente para a
  tese.

## Fronteira
Validação técnica de uma citação específica (WebFetch na URL, conferência do trecho da ementa):
`juris-adv-os`. Liquidação/cálculo que dependa de índice ou tabela: `calculosjudiciais-adv-os`.
