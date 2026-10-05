---
name: gerador-denuncia-camara-sbroggioadv
title: Gerador de denúncia à Câmara (DL 201, infração político-administrativa)
description: 'Gera a denúncia de infração político-administrativa de prefeito à Câmara Municipal, com base no Decreto-Lei 201/1967 arts. 4º e 5º — a via em que qualquer eleitor tem legitimidade nomeada (art. 5º, I). A peça é sempre um PEDIDO DE APURAÇÃO (P2): narra o ato publicado com fonte e a infração correspondente e requer o processamento pela Câmara, nunca afirma culpa. Registra o prazo do rito (o processo tem de concluir em 90 dias da notificação do acusado — art. 5º, VII — senão arquiva). Separa o que é infração político-administrativa (julgada pela Câmara, cassação) do que é crime de responsabilidade (DL 201 art. 1º), que vai por notícia-crime ao Ministério Público, não à Câmara. Mostra o aviso do CP 339 (P3) antes. Aciona: quando o alvo é prefeito e o vício é infração político-administrativa, ou o usuário pede "denunciar o prefeito na Câmara", "pedir cassação" ou "denúncia de vereador contra o prefeito".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/gerador-denuncia-camara
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# Gerador de denúncia à Câmara (DL 201, infração político-administrativa)

## Quando esta skill entra

Quando o alvo é **prefeito** (ou vice/substituto — DL 201 art. 3º) e o vício se enquadra
como **infração político-administrativa** do art. 4º do DL 201/1967 — julgada pela **própria
Câmara Municipal**, com pena de **cassação do mandato**. Exige lastro (P1): o ato publicado
(URL/data) e a infração do art. 4º que ele configura.

## A bifurcação que não pode errar: infração ≠ crime

O DL 201 tem **duas vias distintas** — confundi-las manda a peça ao órgão errado:

- **Infração político-administrativa (art. 4º)** → **Câmara Municipal**, rito do art. 5º,
  pena de cassação. Rol de 10 infrações: impedir o funcionamento da Câmara (I), impedir o
  exame de livros/documentos ou verificação de obras por comissão/auditoria (II), desatender
  convocações/pedidos de informação da Câmara (III), deixar de publicar leis/atos (IV), não
  apresentar a proposta orçamentária no prazo (V), descumprir o orçamento aprovado (VI),
  praticar contra lei ato de sua competência ou omitir-se (VII), negligenciar a defesa de
  bens/rendas/direitos do Município (VIII), ausentar-se além do permitido (IX), proceder de
  modo incompatível com a dignidade e o decoro do cargo (X). **Esta é a peça que esta skill
  gera.**
- **Crime de responsabilidade (art. 1º, 23 incisos)** → **Ministério Público** (ação penal
  pública), sujeito ao **Judiciário** independentemente da Câmara (art. 1º, caput; art. 2º).
  Ex.: apropriar-se/desviar rendas (I), aplicar indevidamente verbas (III), ordenar despesa
  não autorizada (V), contratar sem licitação onde exigida (XI). **Isto NÃO vai à Câmara** —
  roteia para notícia-crime ao MP via `gerador-representacao`/`consolidador-dossie`.

Se o mesmo fato configura os dois, são **peças e órgãos separados** — a Câmara não julga
crime de responsabilidade, o MP não cassa mandato. O produto não escolhe pela gravidade
retórica; escolhe pela via que a lei fixou.

## Antes de gerar — o aviso obrigatório (P3)

Não emite antes de o `aviso-cp339-art19-e-ce326a` mostrar o texto do **CP art. 339** (a
denúncia à Câmara é "processo administrativo", nomeado na redação de 2020) e o usuário
confirmar a veracidade. Se o prefeito é candidato/pré-candidato 2026 ou estamos na janela,
dispara o `disclaimer-eleitoral` (CE 326-A, e o §3º para quem divulga).

## Estrutura da denúncia (art. 5º, por qualquer eleitor)

1. **Endereçamento** — ao Presidente da Câmara Municipal de [município].
2. **Qualificação do denunciante** — o art. 5º, I permite a denúncia **por qualquer
   eleitor**, com **exposição dos fatos e indicação das provas**. (Se o denunciante for
   vereador, o art. 5º, I registra impedimentos de voto/comissão — informar, não decidir.)
3. **Dos fatos** — o ato publicado, onde e quando; cada frase com a fonte exata (P5).
4. **Do enquadramento** — a infração do art. 4º correspondente (inciso), citada do
   `context/`, **como pedido de apuração**: os fatos "aparentam configurar" a infração.
5. **Do pedido** — requer o **recebimento da denúncia** e a instauração do processo do art.
   5º para apuração, com constituição da comissão processante. Nunca "o prefeito cometeu".
6. **Provas** — documentos anexados. **Fecho**: data, local, assinatura (art. 5º exige
   denúncia **escrita**).

## O prazo do rito (registrar, não fabricar)

O art. 5º, VII: *"O processo… deverá estar concluído dentro em noventa dias, contados da
data em que se efetivar a notificação do acusado. Transcorrido o prazo sem o julgamento, o
processo será arquivado, sem prejuízo de nova denúncia…"*. A peça **informa** esse prazo ao
denunciante. O rito interno pode ser substituído por legislação estadual ("se outro não for
estabelecido pela legislação do Estado" — art. 5º, caput): onde isso não está fechado,
marca `[VERIFICAR PRAZO]` por UF (P7 / TV9), não inventa.

## Travas / limites

- **Sem lastro não gera** (P1): ato publicado + infração do art. 4º, senão `[FALTA LASTRO]`.
- **Infração (Câmara) ≠ crime de responsabilidade (MP)** — não misturar via nem órgão.
- **Pedido de apuração, nunca culpa** (P2) via `guard-para-apuracao`.
- **Aviso CP 339 antes de emitir** (P3); disclaimer eleitoral se o alvo for candidato (P6).
- **Fonte em toda alegação** (P5); **só ato de autoridade** (P4).
- **Prazo de 90 dias registrado; rito estadual/UF → `[VERIFICAR PRAZO]`** (P7).
- Só prefeito/vice (DL 201). Vereador tem rito próprio (art. 7º) — fora do fluxo padrão.
- Cita só o `context/`. Não é peça judicial: parte judicial → `consolidador-dossie`.
