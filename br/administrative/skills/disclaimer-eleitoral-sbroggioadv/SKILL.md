---
name: disclaimer-eleitoral-sbroggioadv
title: DISCLAIMER ELEITORAL — a fronteira (trava P6)
description: 'Trava P6 do opositor-os — a fronteira eleitoral. Dispara, por gatilhos objetivos, o disclaimer literal ANTES de gerar ou sugerir publicar qualquer peça de fiscalização. Gatilho A (tempo): janela 20/07–25/10/2026, ou o usuário se declara pré-candidato/candidato 2026 na triagem. Gatilho B (alvo): o ato fiscalizado tem por titular alguém que é candidato/pré-candidato 2026 — o produto PERGUNTA (identificação sugerida ≠ confirmada). Qualquer um dispara o texto literal do disclaimer, que cobre também a DIVULGAÇÃO (Código Eleitoral art. 326-A § 3º pune quem só compartilha sabendo da inocência), não apenas a geração. Lista as 4 recusas expressas (não gera nem com confirmação) e roteia tudo que é eleitoral próprio para eleitoral-adv-os. O opositor NUNCA redige peça eleitoral. Carrega SEMPRE — referenciada por toda a Camada 3. Aciona: quando uma skill de C3 vai gerar/publicar e um dos dois gatilhos está ativo.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/opositor-os-marketplace/tree/main/opositor-os/skills/disclaimer-eleitoral
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: administrative
language: pt
---

# DISCLAIMER ELEITORAL — a fronteira (trava P6)

> **Carrega SEMPRE.** Transversal à Camada 3. Roda antes de gerar **e** antes de
> sugerir publicar. O opositor **nunca** redige peça eleitoral — gera só a peça de
> fiscalização e, quando a conversa migra para campanha/processo, para e roteia.

## Quando esta skill entra
Antes de qualquer skill de C3 gerar/publicar, sempre que um dos gatilhos abaixo
dispara. É o passo P6 das 7 travas de postura.

## Anexo obrigatório (context/)
- `context/eleitoral-fronteira.md` — gatilhos, disclaimer literal (§2), recusas
  (§3) e tabela de cross-link (§4) — grep + faixa.
- `context/freios-penais.md` — CE 326-A (o § 3º da divulgação) e CE 324.

## Gatilhos de ativação (dois, objetivos — nada depende de "sentir")
- **Gatilho A — janela de tempo:** entre **20/07/2026** (abertura das convenções) e
  **25/10/2026** (2º turno), **ou** a qualquer momento em que o usuário se identifique
  como pré-candidato/candidato 2026 na triagem.
- **Gatilho B — natureza do alvo:** quando o ato fiscalizado tem por titular alguém
  que é, ele mesmo, pré-candidato/candidato registrado em 2026. O produto **pergunta**
  — identificação sugerida ≠ confirmada.

Qualquer um dos dois dispara o texto abaixo **antes** de gerar ou sugerir publicação.

## Texto do disclaimer (literal — o produto exibe verbatim)

```
⚠️ VOCÊ ESTÁ NA JANELA ELEITORAL DE 2026

Fiscalizar um ato público é sempre livre. A lei protege quem divulga crítica e
posicionamento político sem pedir voto no mesmo conteúdo (Lei 9.504/97, art. 36-A,
V — ou, depois de 16/08/2026, a propaganda eleitoral regular). Mas três coisas mudam
de figura quando há eleição:

1. NUNCA misture fiscalização com pedido de voto no mesmo conteúdo. Elogiar ou
   criticar um ato público é livre; somar "vote em mim" (ou "vote no candidato X")
   na MESMA peça já é propaganda eleitoral — regras de identificação e
   financiamento entram em jogo, e impulsionar (pagar) esse conteúdo só pode ser
   feito pelo próprio candidato/partido/coligação (Lei 9.504/97, art. 57-C).

2. NUNCA afirme como certo um fato que ainda não foi apurado. Se o alvo da sua
   fiscalização é candidato ou pré-candidato em 2026, publicar como certa uma
   acusação que você sabe (ou deveria saber) inverídica pode configurar, ao
   mesmo tempo: calúnia eleitoral (Código Eleitoral, art. 324) e — se você deu
   causa a investigação/processo contra quem sabe inocente, com finalidade
   eleitoral — o crime do art. 326-A do Código Eleitoral (reclusão de 2 a 8 anos),
   somado ao que já vale o ano inteiro: denunciação caluniosa (CP, art. 339) e o
   crime do art. 19 da Lei 8.429/92. Compartilhar/republicar sabendo que é falso
   também é crime (art. 326-A, §3º), mesmo que você não tenha escrito o texto.

3. Quem você cita pode pedir resposta rápida. A partir do momento em que o alvo
   é candidato registrado, ele pode pedir à Justiça Eleitoral direito de resposta
   a qualquer tempo enquanto o conteúdo estiver no ar na internet (Lei 9.504/97,
   art. 58, §1º, IV) — decidido em até 72 horas.

Este produto redige toda peça como pedido de apuração, nunca como acusação
fechada, e não redige texto de campanha, propaganda, AIJE/AIME/RCED ou defesa
penal-eleitoral — isso é escopo do eleitoral-adv-os.

Confirme: os fatos narrados são verdadeiros e documentados, e este conteúdo NÃO
pede voto, para continuar.
```

O ponto **2** cobre a **divulgação** (CE 326-A § 3º): compartilhar sabendo que é
falso já é crime, mesmo sem ter escrito o texto. A trava não olha só a geração.

## Recusas expressas (não gera, mesmo com confirmação do usuário)
1. Texto que combine, na mesma peça, **fiscalização + pedido explícito de
   voto/apoio** → é propaganda → roteia para `eleitoral-adv-os`.
2. Peça de **AIJE, AIME, RCED, impugnação de registro (AIRC)** ou representação por
   **abuso de poder** contra candidato → ação eleitoral própria → `eleitoral-adv-os`.
3. **Defesa** contra direito de resposta, calúnia/difamação/injúria eleitoral ou
   denunciação caluniosa (CP 339 / CE 326-A) **recebida** pelo usuário →
   `eleitoral-adv-os`.
4. Orientar **impulsionamento pago** do conteúdo por quem não é
   candidato/partido/coligação → **vedado** (art. 57-C); o produto avisa e não gera
   estratégia para isso.

## Cross-link — o que o opositor faz × o que roteia (§4)
- Vício em ato do Executivo, **alvo não é** candidato 2026 → varre, roteia, **gera**
  a peça de apuração (regime CP 339 / Lei 8.429 art. 19).
- Vício em ato do Executivo, **alvo é** candidato 2026 → **gera** a peça de apuração,
  **mas dispara o disclaimer antes**.
- Usuário quer **usar o achado para pedir voto / propaganda paga** → entrega o
  **dossiê factual** (fonte + norma); a peça de campanha é `eleitoral-adv-os`.
- Usuário quer **ação eleitoral própria** (AIJE/AIME/RCED) → **não gera** →
  `eleitoral-adv-os`.
- Usuário/alvo **recebeu** direito de resposta (art. 58) → **não defende** →
  `eleitoral-adv-os`.
- Usuário é **acusado** de calúnia/326-A por ter usado o produto → **não defende** →
  `eleitoral-adv-os`.

## Travas / limites
- **Regra de desenho:** o opositor **nunca** redige peça eleitoral. Gera só a peça de
  fiscalização (representação/denúncia/impugnação/LAI); quando migra para campanha ou
  processo eleitoral, para e aponta para `eleitoral-adv-os`.
- **Gatilho B pergunta, não deduz.** Identificação sugerida de que o alvo é candidato
  ≠ confirmada — o produto pergunta antes de tratar como eleitoral.
- **Fora da janela e sem alvo candidato**, esta trava não dispara; vale o regime do
  ano inteiro (CP 339 + Lei 8.429 art. 19, via `aviso-cp339-art19-e-ce326a`).
- **Não abranda P1/P2/P3.** O disclaimer é além delas, não no lugar delas.
