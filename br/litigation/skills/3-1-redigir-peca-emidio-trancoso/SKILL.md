---
name: 3-1-redigir-peca-emidio-trancoso
title: Redigir Peça — do plano à redação
description: Planeja e redige uma peça jurídica de qualquer tipo (petição inicial, contestação, réplica, recurso, contrarrazões, parecer, contrato, notificação extrajudicial, alegações finais) a partir do SUMARIO, do DIAGNOSTICO e da fundamentação do caso. Primeiro define o silogismo central e a hierarquia das teses e apresenta o plano para validação; depois redige a peça com boa técnica (estrutura tipo CREAC, narrativa persuasiva e rebate integrado), sem inventar fatos ou citações.
author: emidio-trancoso
author_url: https://github.com/emidio-trancoso/advocacia-aberta/tree/main/.agents/skills/3.1-redigir-peca
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Redigir Peça — do plano à redação

Esta skill é o seu procedimento de escrita jurídica colocado por escrito. Ela transforma o material já organizado do caso em uma peça pronta para revisar — em **duas fases**:

1. **PLANEJAR** — decidir o que dizer: silogismo central, hierarquia das teses e estrutura da peça. O plano é apresentado a você para validação **antes** de qualquer redação.
2. **REDIGIR** — escrever a peça aplicando boa técnica, depois que você aprova o plano.

Serve para **qualquer peça**: petição inicial, contestação, réplica, recurso, contrarrazões, parecer, contrato, notificação extrajudicial, alegações finais, etc. A estrutura se adapta ao tipo.

## Regra-raiz: nunca inventar — leia antes de tudo

Esta é a regra mais importante. Violá-la é pior do que omitir um argumento.

- **Fatos:** só use o que está nos documentos do caso (autos, transcrições, SUMARIO, DIAGNOSTICO). Nunca invente datas, valores, nomes ou acontecimentos.
- **Lei:** texto de artigo só entra na peça **copiado palavra por palavra** de `fundamentacao/LEGISLACAO.md`.
- **Jurisprudência:** ementa, súmula, tema repetitivo ou trecho de acórdão só entra **copiado palavra por palavra** de `fundamentacao/JURISPRUDENCIA.md`.
- **Depoimentos:** uma aspa só existe se a frase aparecer literalmente na transcrição rotulada do caso. Nunca parafraseie como se fosse citação. Toda aspa de depoimento leva o timestamp.

Se o texto exato de uma lei, precedente ou depoimento não estiver na fonte verificada,
**não use** — escreva `[verificar na fonte]` e siga em frente. Toda lei ou precedente
deve vir das skills `buscar-fontes` ou `buscar-tjpr` e estar registrado na
fundamentação. A única escrita livre é a análise e a narrativa ao redor das citações.

## Instrução

A entrada informada pelo usuário deve trazer o caminho relativo da pasta do caso e,
opcionalmente, o tipo de peça. Exemplos:

- `casos/0001234-56.2025.8.16.0151 contestação`
- `casos/joao-silva-acidente recurso de apelação`
- `casos/0001234-56.2025.8.16.0151` (sem tipo — você infere ou pergunta no Passo 1)

Considere `<caminho-do-caso>` a pasta informada e `<tipo-de-peca>` o tipo informado
ou confirmado no Passo 1. Os caminhos são relativos à raiz do projeto aberta no agente.

### Dois modos de trabalho

- **Modo repositório** — há uma pasta `casos/<caso>/` no espaço de trabalho; os insumos e a
  saída seguem os caminhos indicados abaixo.
- **Modo conversa** — não há pasta do caso: os insumos foram anexados na conversa (ou
  gerados nela pelas skills anteriores). Trabalhe sobre os anexos e **entregue a peça como
  arquivo** ao final, em vez de gravar em `casos/<caso>/pecas/`.

Sobre a fundamentação: no modo repositório ela vem de `fundamentacao/LEGISLACAO.md` e
`fundamentacao/JURISPRUDENCIA.md`; no modo conversa, vem do que a skill `buscar-fontes`
retornou na conversa. Em ambos os casos a regra-raiz continua valendo — só entra texto de
lei ou precedente **copiado da fonte verificada**, com o link oficial. A skill `buscar-tjpr`
depende de ferramenta local e **não está disponível no ChatGPT Web hospedado**; quando ela
não existir, use apenas a `buscar-fontes` e marque `[verificar na fonte]` o que precisaria de
confirmação em tribunal específico.

---

# FASE 1 — PLANEJAR

Nesta fase você não redige a peça. Você decide a estratégia e a submete à validação.

## Passo 1 — Identificar o tipo de peça e a versão

Determine **qual peça** será redigida:

- Se o tipo veio na entrada do usuário, use-o.
- Senão, infira pelo contexto do caso (o que falta nos autos, qual o próximo movimento esperado) e **confirme com o usuário** antes de seguir. Não adivinhe em silêncio.

O tipo define a estrutura (ver Passo 6). Exemplos do que muda:

| Tipo de peça | O que ela precisa fazer |
|---|---|
| Petição inicial | Narrar os fatos, fundamentar o direito, formular pedidos, atribuir valor à causa |
| Contestação | Preliminares, impugnação dos fatos, mérito, pedido de improcedência |
| Réplica | Rebater a contestação, reafirmar a inicial, enfrentar preliminares |
| Recurso (apelação/agravo) | Demonstrar o erro da decisão, prequestionar, pedir reforma |
| Contrarrazões | Defender a sentença, apontar falhas do recurso adversário |
| Alegações finais | Sintetizar a instrução, fechar cada tese com a prova produzida |
| Parecer | Questão posta, análise fundamentada, conclusão objetiva |
| Notificação extrajudicial | Fato, exigência, prazo, consequência |
| Contrato | Partes, objeto, obrigações, condições, cláusulas de proteção |

Defina a **versão**: olhe a pasta `casos/<caso>/pecas/`. Se já existe `<nome-da-peca>-v[N].md`, a nova é `v[N+1]`; senão, é `v1`.

## Passo 2 — Verificar os insumos

Confira o que existe na pasta do caso:

| Arquivo | Caminho | Necessidade |
|---|---|---|
| SUMARIO.md | `casos/<caso>/analise/SUMARIO.md` | Obrigatório |
| DIAGNOSTICO.md | `casos/<caso>/analise/DIAGNOSTICO.md` | Obrigatório |
| LEGISLACAO.md | `casos/<caso>/fundamentacao/LEGISLACAO.md` | Obrigatório |
| JURISPRUDENCIA.md | `casos/<caso>/fundamentacao/JURISPRUDENCIA.md` | Obrigatório |
| Peças adversárias / decisão recorrida | identificar pelo SUMARIO | Obrigatório quando o tipo de peça responde a outra (contestação, réplica, recurso, contrarrazões, alegações finais) |
| Transcrições da audiência | `casos/<caso>/autos/` | Obrigatório se houve audiência |

Se faltar algo obrigatório:

- Sem SUMARIO.md → execute primeiro a skill `organizar-caso`.
- Sem DIAGNOSTICO.md → execute primeiro a skill `diagnosticar`.
- Sem fundamentação → execute primeiro as skills `buscar-fontes` e `buscar-tjpr`.
- Faltando outro insumo → avise que a peça sairá em **modo rascunho** (sem citações literais precisas nem rebate cirúrgico) e pergunte se deseja continuar mesmo assim.

## Passo 3 — Ler tudo o que importa

Leia integralmente, sem pular:

- **SUMARIO.md** — partes, linha do tempo, teses de cada lado.
- **DIAGNOSTICO.md** — fragilidades do caso, munição disponível e os riscos da própria tese (red-team).
- **LEGISLACAO.md** e **JURISPRUDENCIA.md** — o texto literal que poderá ser citado.
- **Peças do adversário ou decisão recorrida** (quando aplicável) — mapeie os argumentos dele, a ordem em que aparecem, as provas que destacou, contradições internas e o que ele **deixou de rebater** (silêncios reveladores).
- **Transcrições** (se houve audiência) — identifique cada depoente, o tipo (parte, testemunha compromissada, informante) e as frases mais fortes, copiadas exatamente como estão, com timestamp.

## Passo 4 — Construir o silogismo central

O silogismo é o coração lógico da peça: três frases que tornam a conclusão inevitável.

```text
Premissa fática:    [o fato central que está provado — uma frase]
Premissa jurídica:  [a norma ou o precedente que se aplica a esse fato — uma frase]
Conclusão / pedido: [o que se quer do juízo ou da outra parte — uma frase]
```

Derive-o do cruzamento entre a munição mais forte do DIAGNOSTICO e a fonte jurídica mais sólida da fundamentação.

## Passo 5 — Hierarquia das teses (da mais forte para a mais fraca)

Liste as teses candidatas e avalie cada uma em três eixos:

| Eixo | O que mede |
|---|---|
| **Força probatória** | Documentos + depoimentos + circunstâncias que sustentam a tese |
| **Vulnerabilidade do adversário** | Onde o outro lado é fraco, se contradiz ou silencia |
| **Sustentação jurídica** | Lei aplicável + jurisprudência direta, súmula ou tema repetitivo |

A tese forte nos três eixos abre a peça. Use no **máximo 4 ou 5 teses principais** — argumento bom demais convivendo com argumento fraco perde força. Elimine ou funda as teses que só diluem as fortes. Uma tese sem ao menos dois elementos de prova deve ser rebaixada ou fundida.

## Passo 6 — Definir a estrutura da peça (conforme o tipo)

Monte a sequência de seções adequada ao tipo identificado no Passo 1. Esqueletos de referência (ajuste ao caso concreto):

**Petição inicial**
- Endereçamento e qualificação das partes
- Dos Fatos
- Do Direito (uma subseção por tese, da mais forte para a mais fraca)
- Dos Pedidos · Do valor da causa

**Contestação**
- Endereçamento
- Das Preliminares (se houver)
- Do Mérito (impugnação dos fatos + Do Direito por tese)
- Dos Pedidos (improcedência)

**Recurso / Contrarrazões**
- Endereçamento e tempestividade
- Síntese do que foi decidido
- Das Razões (o erro a corrigir, ou a defesa da sentença, por tese)
- Do Pedido (reforma / manutenção)

**Alegações finais**
- Endereçamento
- Síntese fático-processual
- Razões de mérito (Prova documental · Prova testemunhal · Do Direito por tese)
- Dos Pedidos

**Parecer**
- A questão · A análise (por tese) · A conclusão

Regra para os títulos das subseções de "Do Direito": o título **afirma a tese**, não é rótulo neutro.

- Rótulo neutro: "Da responsabilidade do réu"
- Afirmação da tese: "O réu respondeu pelo dano porque descumpriu dever que ele mesmo reconheceu"

## Passo 7 — Apresentar o plano e aguardar validação

Mostre ao usuário, de forma enxuta:

- Tipo de peça e versão a redigir.
- O silogismo central (as três frases).
- A hierarquia das teses (uma linha por tese, da mais forte para a mais fraca).
- A estrutura proposta da peça.
- Eventuais pendências (decisão estratégica, dado a confirmar com o cliente).

**Pare aqui e peça a aprovação.** Só passe para a Fase 2 depois que o usuário validar ou ajustar o plano. Esta é a etapa que evita redigir a peça inteira na direção errada.

---

# FASE 2 — REDIGIR

Com o plano aprovado, redija a peça. A teoria do caso já está decidida — esta fase é execução.

## Passo 8 — Redigir as seções

Siga a estrutura validada no Passo 6. Para cada parte:

### Abertura / Síntese / Dos Fatos
- Apresente o silogismo central logo no início: quem lê deve saber desde o começo aonde a peça chega.
- Narre os fatos de forma persuasiva, não exaustiva.
- **Relevo:** fato favorável no início ou no fim do parágrafo; fato desfavorável no meio e contextualizado. Nunca abra nem feche com fato desfavorável.
- **Contranarrativa embutida:** a própria seleção e ordem dos fatos já refuta a versão contrária, sem precisar argumentar ainda.
- Cada fato relevante leva sua referência ao documento *(mov. X.Y, p. Z)*.

### Prova (documental e testemunhal), quando a peça a comporta
- Documento: identifique pelo movimento e página, conecte ao fato em disputa em uma frase, extraia a conclusão que ele demonstra.
- Aponte convergência: "Três fontes independentes confirmam o mesmo fato: o documento X, o depoimento Y e a circunstância Z."
- Depoimento: contexto em uma frase → a aspa literal com timestamp e tipo de declarante → conclusão em uma frase. Nunca aspa solta.
- Trate o ônus da prova: quem devia provar o quê, o que ficou incontroverso, o que o adversário deveria ter produzido e não produziu.

### Do Direito — uma subseção por tese, na ordem do plano

Para cada tese, use a estrutura **CREAC** (Conclusão → Regra → Explicação → Aplicação → Conclusão), com o rebate **integrado dentro da própria tese** — nunca num bloco solto no fim da peça:

```text
[CONCLUSÃO]   Primeira frase: o que o juízo deve decidir nesta tese.

[REGRA]       A norma (de LEGISLACAO.md) ou o precedente (de JURISPRUDENCIA.md),
              copiado literalmente. Acórdão: número, relator, data e trecho central
              entre aspas. Súmula/tema: número, tribunal e enunciado entre aspas.
              Lei: artigo e texto literal entre aspas.

[EXPLICAÇÃO]  Como os tribunais já aplicaram essa regra em casos parecidos.
              O raciocínio já foi feito por outro tribunal — peça que se repita aqui.

[APLICAÇÃO]   Ligue os fatos provados à regra:
              "No caso, [fato provado, com a prova] mais [depoimento, com timestamp]
              configuram exatamente a hipótese da [regra]."

              ↳ Rebata aqui o argumento contrário desta tese:
                "A parte contrária sustenta que [...]. Contudo, [prova/norma]
                mostra o oposto." — ou: "Ainda que assim fosse, a conclusão
                não muda, porque [...]."

              ↳ Se a tese tem um ponto fraco seu, neutralize-o aqui: mostre o
                fato em contexto, sua irrelevância jurídica, ou faça concessão
                mínima e volte de imediato ao ponto forte.

[CONCLUSÃO]   Reafirme, em uma frase, o que o juízo deve decidir.
```

Onde posicionar o rebate dentro da subseção:
- Argumento contrário ataca os fatos → rebata na APLICAÇÃO.
- Argumento contrário ataca a norma ou o precedente → rebata na REGRA ou na EXPLICAÇÃO.
- O adversário não enfrentou este ponto → aponte o silêncio na CONCLUSÃO.
- O adversário trouxe alegação nova, inexistente nas peças anteriores → aponte a inovação.

### Pedidos / Conclusão
- Lista numerada. Cada pedido com seu fundamento (artigo ou tese desenvolvida) e valor, quando houver.
- Encerre com o pedido de condenação em honorários e custas, quando cabível ao tipo de peça.

## Passo 9 — Estilo (aplicar na peça inteira)

- **Uma ideia por parágrafo.** Acabou a ideia, novo parágrafo. Máximo de 5 ou 6 linhas.
- **A primeira frase do parágrafo afirma a posição**, não o tema.
  - Fraco: "Quanto ao consentimento, cumpre analisar..."
  - Forte: "O réu não obteve o consentimento por escrito — falha admitida pela própria testemunha dele."
- **Teste da leitura em diagonal:** as primeiras frases de todos os parágrafos de uma seção, lidas em sequência, já devem formar um argumento coerente. Se não formam, reordene.
- **Voz ativa.** Troque "foi realizado" por "o réu realizou".
- **Sem arcaísmos:** "outrossim" → "além disso"; "destarte" → "portanto"; "hodiernamente" → "hoje".
- **Sem juridiquês ornamental.** Precisão não pede rebuscamento.
- **Use o nome do cliente** no corpo, não só "o autor" ou "a ré".
- Cada parágrafo precisa ganhar seu lugar: se removê-lo não enfraquece o argumento, corte-o.

## Passo 10 — Conferir antes de salvar

- [ ] O silogismo central aparece na abertura e nos pedidos.
- [ ] As teses estão na ordem do plano (da mais forte para a mais fraca).
- [ ] Cada tese tem pelo menos dois elementos de prova.
- [ ] O rebate está dentro de cada tese — não há bloco solto de rebate no fim.
- [ ] Todo argumento relevante do adversário foi absorvido em alguma tese.
- [ ] Toda lei foi copiada de LEGISLACAO.md; toda jurisprudência, de JURISPRUDENCIA.md.
- [ ] Toda aspa de depoimento é literal, com timestamp e tipo de declarante; trecho duvidoso marcado `[transcrição incerta]`.
- [ ] Nenhum fato, número ou citação inventado — onde faltou fonte, há `[verificar na fonte]`.
- [ ] Estilo: uma ideia por parágrafo, frase tópica afirma posição, voz ativa, sem arcaísmos.

## Passo 11 — Salvar e informar

Salve a peça em:

```text
casos/<caso>/pecas/<nome-da-peca>-v[N].md
```

Use um nome claro para o tipo (ex.: `contestacao-v1.md`, `apelacao-v1.md`, `alegacoes-finais-v1.md`). Crie a pasta `pecas/` se não existir.

Depois, informe ao usuário:

1. Caminho do arquivo gerado e versão.
2. Modo aplicado (completo ou rascunho) e por quê.
3. As teses desenvolvidas e a ordem adotada.
4. Onde cada argumento adversário foi rebatido.
5. **Próximos passos:**
   - `revisar-peca` — auditoria adversarial da peça (confere provas e citações, aponta pontos a corrigir).
   - `diagramar-peca` — gera o PDF final com legal design.

---

## Princípios

| Princípio | O que significa |
|---|---|
| **Plano antes de redigir** | A Fase 1 decide a estratégia e é validada por você; a Fase 2 só executa. Não se redige a peça inteira sem o plano aprovado. |
| **A peça se molda ao tipo** | A estrutura de uma contestação não é a de um recurso nem a de um contrato. Identifique o tipo e adote a forma correta. |
| **Hierarquia é decisão, não automatismo** | A skill propõe a ordem das teses; você valida. |
| **Sem fonte, sem citação** | Lei, precedente e depoimento só entram com texto literal da fonte verificada. Na dúvida, `[verificar na fonte]`. |
| **Rebate dentro da tese** | Cada argumento contrário é enfrentado onde ele ataca, não num apêndice ao final. |
