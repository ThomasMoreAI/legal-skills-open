---
name: mapa-de-gaps-da-tese-sbroggioadv
title: Mapa de gaps da tese
description: 'Análise estratégica da peça recebida da parte contrária: mapeia o que ela alegou sem apontar prova, o que citou sem nexo com o próprio pedido (citação real, mas fora de contexto — a skill não julga se a citação é boa, só se sustenta o que a peça diz que sustenta), pedido sem causa de pedir correspondente, contradições internas e o que a peça NÃO enfrentou (documento juntado que ignora, tese óbvia não atacada). É o mapa dos gaps que a redação adversária — humana ou por IA — deixou abertos, para a defesa explorar. Análise de consistência INTERNA, nunca prognóstico de convencimento nem leitura do julgador (isso é prisma-julgador). Saída rotulada "análise estratégica — não é achado de integridade", separada no dossiê (seção D). Aciona: quando o usuário quer "os gaps da peça", "o que eles não enfrentaram", "pontos fracos da contestação", "o que está fora de contexto" ou "por onde atacar a peça".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/blindagem-peticao-os-marketplace/tree/main/blindagem-peticao-os/skills/mapa-de-gaps-da-tese
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Mapa de gaps da tese

## Quando esta skill entra

Depois (ou independentemente) das varreduras de integridade, quando o usuário quer a leitura
estratégica da peça recebida: o que a redação da parte contrária — humana ou por IA — deixou
aberto. É o quinto uso do produto: os gaps que a IA adversária não soube montar, para a defesa
explorar na própria peça de resposta.

## Natureza da saída (rotulagem obrigatória)

Tudo o que sai daqui é **análise estratégica**, não achado de integridade. Toda saída abre com o
rótulo literal:

> **ANÁLISE ESTRATÉGICA — não é achado de integridade. Entra separada no dossiê (seção D).**

Gap não é indício de má-fé, não fundamenta pedido de multa e não entra no
`gerador-topico-impugnacao` (que exige achado confirmado de integridade). Gap alimenta a SUA
peça de resposta: é onde a defesa concentra o ataque.

## Os 5 eixos da análise

A skill lê a peça inteira e mapeia, eixo a eixo:

| Eixo | O que procura | Exemplo de achado |
|---|---|---|
| **(a) Fato sem prova apontada** | Alegação de fato relevante sem referência a documento, testemunha ou perícia nos autos | "Alega pagamento (item 12) sem apontar comprovante" |
| **(b) Fundamento sem nexo com o pedido** | Citação REAL (lei, súmula, julgado) que não sustenta o que a peça diz que sustenta — fora de contexto | "O julgado citado trata de relação de consumo; o caso é contrato civil entre empresas" |
| **(c) Pedido sem causa de pedir** | Pedido no rol final que nenhum tópico da fundamentação constrói | "Pede danos morais; nenhum parágrafo narra o dano" |
| **(d) Contradição interna** | A peça afirma X num tópico e não-X em outro | "Nega a entrega no item 8; no item 23 discute a qualidade do que foi entregue" |
| **(e) O que a peça NÃO enfrentou** | Documento juntado que ela ignora; tese óbvia que não atacou; pedido da inicial sem impugnação específica | "Silêncio total sobre o laudo de fls. 88" |

O eixo **(e)** costuma ser o mais valioso: silêncio sobre documento ou tese central é o gap que a
defesa explora com maior rendimento.

## O que o eixo (b) faz — e o que ele NUNCA faz

No eixo (b), a skill **não julga se a citação é boa, forte ou persuasiva**. Julga uma coisa só:
**a citação sustenta o que a peça afirma que ela sustenta?** É análise de nexo (encaixe
citação-tese), não de mérito.

- Citação real e pertinente, mas "fraca" → **não é gap**. Avaliar força é mérito.
- Citação real e impertinente (decide outra hipótese) → gap de eixo (b), com o descolamento
  descrito: o que a peça diz × o que a citação de fato decide.
- Citação possivelmente **inexistente ou deturpada** → não é assunto desta skill: roteia para
  `citacoes-da-peca-recebida` / `dispositivos-da-peca-recebida` (veredito por evidência, com
  WebFetch/fonte oficial — nunca por leitura do LLM).

## Fronteira T6 — rígida e sem exceção

Esta skill analisa a **consistência interna** da peça. Ela **nunca**:

- estima probabilidade de êxito ou de convencimento ("o juiz não vai aceitar isso");
- avalia o julgador, o histórico da vara ou "como esse juiz decide";
- opina se a tese adversária "convence" ou se a citação real é "boa".

Pergunta de convencimento/julgador → resposta padrão: *"Isso é análise de persuasão/julgador —
fora do escopo da blindagem (integridade × mérito). Ferramenta indicada: `prisma-julgador`."*
Sem exceção, mesmo se o usuário insistir.

## Formato de saída

Um mapa por peça, com o rótulo obrigatório no topo e, por gap:

1. **Eixo** (a–e) e **localização** na peça (item/parágrafo/página).
2. **O gap em uma frase** — factual, sem adjetivar a intenção da parte contrária.
3. **O que a defesa pode explorar** — a sugestão de enfrentamento na peça de resposta (ex.:
   impugnação específica ao fato sem prova, destaque do silêncio sobre o documento,
   demonstração do descolamento da citação fora de contexto).
4. **Relevância estratégica** — alta / média / baixa, pelo peso do ponto na controvérsia
   (nunca por prognóstico de resultado).

Ordenado por relevância, eixo (e) sinalizado. Fecho: aviso de conferência humana (T5).

## Travas / limites

- **Rotulagem obrigatória** em toda saída — sem o rótulo, a análise não é entregue.
- **T6**: consistência interna, nunca persuasão/julgador → `prisma-julgador`.
- **Gap ≠ achado de integridade**: não fundamenta multa nem entra no
  `gerador-topico-impugnacao`; no dossiê, só na seção D, separada.
- **Citação suspeita de inexistir** → `citacoes-da-peca-recebida` (T2); dispositivo suspeito →
  `dispositivos-da-peca-recebida`. Esta skill não sela ✅/🔴.
- **T5**: conferência humana do advogado em toda entrega.
