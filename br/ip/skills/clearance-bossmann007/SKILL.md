---
name: clearance-bossmann007
title: /clearance
description: Primeira passada de colidência de marca — checagem de anterioridade + marcas semelhantes gerando lista de flags, não um parecer de colidência. Use quando uma nova marca é proposta, quando perguntado se uma marca está disponível ou para rodar busca de anterioridade, ou ao avaliar fatores de risco de confusão antes de busca profissional completa. Este skill nunca conclui que uma marca está livre.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/ip-legal/skills/clearance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: ip
language: pt
---

# /clearance

**Isto é triagem, não parecer de colidência.** Um parecer de colidência de
marca exige busca profissional completa e o julgamento de um advogado de
marcas registrado. Um resultado "sem conflito óbvio" significa que a triagem
não encontrou nada — não significa que a marca está livre. Clientes já foram
processados por marcas que passaram numa busca de anterioridade.

## Instructions

1. Leia `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Se
   contém `[PLACEHOLDER]`, pare e direcione para `/ip-legal:cold-start-interview`.
2. Siga o workflow abaixo.
3. Rode o intake (marca, produtos/serviços, classes NCL, jurisdições, estilização visual).
4. Checagem de anterioridade para óbices intrínsecos — genérico, descritivo,
   enganoso, geográfico, sobrenome, reprodução/imitação de símbolo oficial,
   contrariedade à moral/bons costumes, marca de alto renome de terceiro.
5. Busca de marcas semelhantes contra o que estiver conectado (Solve
   Intelligence, JusBrasil, ou qualquer MCP disponível). Se nada estiver
   conectado, diga isso no output e prossiga só com a análise de fatores.
6. Percorra os fatores de risco de confusão aplicáveis à doutrina brasileira
   de colidência marcária. Sinalize cada um; nunca conclua.
7. Escreva o memorando de triagem na pasta da matéria (se houver matéria ativa)
   ou na pasta de outputs da prática. Aplique o cabeçalho de sigilo por papel.
8. Termine com próximos passos recomendados e o gate de não-advogado se o
   papel for não-advogado.

Este skill nunca conclui que uma marca está livre. Se incerto, sinaliza — o
advogado decide.

## Examples

```
/ip-legal:clearance "APEXLEAF para linha de vestuário outdoor, lançamento previsto Brasil + Mercosul"
```

```
/ip-legal:clearance
```

(E o skill vai perguntar pela marca, produtos, classes e jurisdições.)

---

## THIS IS A FIRST PASS, NOT A CLEARANCE OPINION

**Diga isto no topo de todo output. Não corte. Não suavize.**

> **Esta é uma primeira passada, não um parecer de colidência.** Um parecer de
> colidência de marca exige busca profissional completa (base do INPI, marcas
> notoriamente conhecidas fora do Brasil sob a Convenção da União de Paris
> art. 6º bis, nomes de domínio, redes sociais, trade dress) e julgamento do
> advogado sobre risco de confusão, que depende de fatores que uma triagem
> estruturada não consegue avaliar por completo. Um resultado "sem conflito
> óbvio" desta triagem significa que ela não encontrou nada — não significa
> que a marca está livre. Clientes já foram processados por marcas que
> passaram numa busca de anterioridade. Um advogado especializado em marcas
> avalia antes de qualquer adoção, depósito ou investimento nesta marca.

Este é o guardrail mais alto do plugin. Deixar de sinalizar um conflito é
porta de uma via só — uma logo em caminhões, produto lançado, pedido de
registro depositado no INPI, tudo com um problema por baixo. Sinalizar demais
é porta de duas vias — o advogado reduz a lista na revisão. Fique do lado da
porta de duas vias.

---

## Matter context

**Contexto de matéria.** Verifique `## Matter workspaces` no CLAUDE.md de
nível prática. Se `Enabled` é `✗` (padrão para usuários in-house), pule o
resto deste parágrafo — skills usam contexto de nível prática e a máquina de
matérias fica invisível. Se habilitado e não há matéria ativa, pergunte:
"Para qual matéria é isso? Rode `/ip-legal:matter-workspace switch <slug>` ou
diga `practice-level`." Carregue o `matter.md` da matéria ativa para contexto
e overrides específicos. Escreva outputs na pasta da matéria em
`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/`.
Nunca leia arquivos de outra matéria a menos que `Cross-matter context` esteja
`on`.

---

## Load the practice profile first

Antes de rodar a colidência, leia
`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`. Extraia:

- **Papel** de `## Who's using this` (advogado(a) vs. agente da propriedade
  industrial vs. não-advogado muda o cabeçalho de trabalho e o gate de
  não-advogado abaixo).
- **Registrado em** e **onde faz enforcement** de `## Perfil de prática (PI)`
  e `## Postura de enforcement` (jurisdições padrão se o usuário não
  especificar).
- **Integrações** de `## Available integrations` (JusBrasil / Solve
  Intelligence — cada uma determina quais buscas estão disponíveis, qual o
  fallback, e o que é atribuído no output).
- **Postura de decisão** de `## Decision posture on subjective legal calls` —
  este skill nunca conclui "sem risco de confusão".

Se `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` contém
`[PLACEHOLDER]` ou `[Nome da sua empresa]`, apresente este desvio:

> Notei que você ainda não configurou seu perfil de prática — é ele que
> calibra postura, jurisdições e cadeia de aprovação para sua prática.
>
> **Duas opções:**
> - Rode `/ip-legal:cold-start-interview` (2 minutos) para configurar seu
>   perfil, e eu rodo isto calibrado para SUA prática.
> - Diga **"provisório"** e eu rodo contra padrões genéricos — jurisdição
>   Brasil, apetite de risco médio, papel advogado, sem playbook — e marco
>   todo output `[PROVISÓRIO — configure seu perfil para output calibrado]`
>   para você ver o que eu faço antes de se comprometer.

### Provisional mode

Se o usuário disser "provisório", rode a colidência normalmente usando estes
padrões genéricos: apetite de risco médio, papel advogado, jurisdição Brasil
(INPI + uso anterior de boa-fé), sem playbook (faça a análise completa em vez
de comparar com lista de posições). Marque a nota de revisão e cada bloco de
achado com `[PROVISÓRIO]`. No final do output, adicione:

> "Essa foi uma execução genérica contra premissas padrão. Rode
> `/ip-legal:cold-start-interview` para ter output calibrado para SUA prática —
> seu playbook, sua jurisdição, seu apetite de risco. 2 minutos."

---

## Intake

Pergunte de uma vez, em lote único (não arraste um trabalho rápido):

> Algumas perguntas antes de rodar a triagem:
>
> 1. **Marca proposta.** Grafia exata, estilização, e se é marca nominativa,
>    figurativa ou mista.
> 2. **Produtos ou serviços.** O que efetivamente é vendido ou oferecido sob
>    a marca. Uma ou duas frases — eu mapeio para as classes de Nice/NCL.
> 3. **Classes.** Se já souber as classes NCL, liste. Senão descreva os
>    produtos/serviços e eu sugiro as classes prováveis e confirmo com você
>    antes de rodar a busca.
> 4. **Jurisdições.** Onde planeja usar, registrar ou fazer enforcement?
>    (Brasil / Mercosul / via Protocolo de Madri / países específicos — eu
>    assumo `Registrado em` do seu perfil de prática se você não disser.)
> 5. **Como vai aparecer em uso.** Slogans, nomes de produtos adjacentes,
>    trade dress ou elementos de design que apareceriam junto no mercado.

Espere a resposta. Se a descrição for vaga ("ferramenta de IA", "plataforma"),
insista uma vez:

> Me dá a coisa real que o cliente vê — é app móvel de consumo, API
> corporativa, produto físico, serviço? As classes dependem disso.

---

## Knockout check

Antes de qualquer busca em base de dados, rode os problemas intrínsecos que
matam uma marca independente de registros anteriores. Para cada um, avalie
com clareza e sinalize. Não racionalize um problema evidente.

| Óbice | O que significa | Sinalize quando |
|---|---|---|
| **Genérico** | O termo É a categoria (ex.: "Sabão" para sabão) — Lei 9.279/1996 art. 124, VI | A marca nomeia o que a coisa é | [verified: https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]
| **Descritivo** | Descreve diretamente característica, função, qualidade ou ingrediente — art. 124, VI | Consumidor lê a marca e sabe o que o produto faz sem esforço imaginativo |
| **Enganoso** | Falsa indicação de procedência, natureza, qualidade ou utilidade — art. 124, X | Marca sugere qualidade que o produto não tem e essa qualidade importaria |
| **Indicação geográfica** | Reprodução/imitação de indicação geográfica ou nome geográfico que induza falsa procedência — art. 124, IX e X | Marca = local + genérico; ou local + produto onde consumidor assumiria origem |
| **Sobrenome/nome civil de terceiro** | Reprodução de nome civil ou pseudônimo de terceiro sem autorização — art. 124, XV | Marca reproduz nome/assinatura/imagem de terceiro identificável |
| **Reprodução/imitação de símbolo oficial** | Brasão, armas, medalha, bandeira, emblema, monumento oficial — art. 124, I | Marca contém elemento oficial protegido |
| **Sinal contrário à moral e aos bons costumes** | Ofensivo, atenta contra liberdade de consciência, crença, culto religioso ou ideia de defesa nacional — art. 124, III | Marca é ofensiva ou atenta contra esses valores | [verified: https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]
| **Marca de alto renome de terceiro** | Proteção especial em todos os ramos de atividade — art. 125 | Marca colide com marca reconhecidamente de alto renome, mesmo em classe distinta |
| **Marca notoriamente conhecida de terceiro (CUP art. 6º bis)** | Proteção independente de registro no Brasil, no mesmo ramo de atividade | Marca colide com marca estrangeira notoriamente conhecida no mesmo ramo |
| **Forma necessária/funcional (para marca tridimensional)** | Forma necessária, comum, vulgar, ou decorrente de função técnica — art. 124, XXI | Marca tridimensional — e a forma tem função técnica |

Nota sobre marca de alto renome (art. 125) e marca notoriamente conhecida
(art. 126, incorporando CUP art. 6º bis): são regimes distintos. A marca de [verified: https://www.planalto.gov.br/ccivil_03/leis/l9279.htm]
alto renome tem registro no Brasil e proteção estendida a todas as classes,
reconhecida em processo específico perante o INPI. A marca notoriamente
conhecida pode não ter registro no Brasil e ainda assim ter proteção no
mesmo ramo de atividade. Não confunda os dois na análise.

**Output:** para cada categoria de óbice, ou "nenhum problema identificado"
ou uma sinalização específica com motivo em uma linha. Não produza tabela em
branco de aprovações.

---

## Similar marks check

O objetivo aqui é **encontrar marcas anteriores potencialmente colidentes**,
não decidir se a confusão é provável. Essa é a decisão do advogado.

### O que o usuário conectou

Leia `## Available integrations` em
`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`:

- **Se um conector de busca de marca estiver disponível** (Solve
  Intelligence, ou qualquer MCP expondo busca na base do INPI): rode busca
  preliminar nas classes e jurisdições relevantes. Atribua todo resultado à
  sua fonte. Anote a data da busca e o escopo (base INPI, classes,
  correspondência exata vs. fonética, busca figurativa ou não).
- **Se um conector de pesquisa jurídica estiver disponível** (JusBrasil para
  jurisprudência e decisões do INPI/TRF): varra por disputas relatadas
  envolvendo a marca ou variante próxima. Mesma regra de atribuição.
- **Se nenhum conector de busca estiver disponível:** diga isso,
  explicitamente, no output. Não infira resultados do conhecimento do modelo
  e os apresente como achados de busca.

### Fallback when no database access exists

Escreva, no output, esta declaração exata:

> **Nenhuma busca em base de dados foi realizada.** Esta triagem não
> consultou a base do INPI, Solve Intelligence, JusBrasil, registros de nomes
> de domínio (registro.br), redes sociais, ou qualquer fonte de uso anterior
> não registrado. Uma busca de anterioridade completa nessas bases é exigida
> antes de qualquer conclusão sobre disponibilidade. A triagem abaixo se
> limita à análise de óbices intrínsecos e fatores estruturados de confusão
> contra marcas que o usuário identificou ou que surgiram na conversa.

Depois prossiga — as checagens intrínsecas e a análise de fatores ainda são
úteis, só rotuladas com honestidade.

### For each similar mark found (or supplied)

Capture:

- **Marca** (caracteres exatos, estilização)
- **Fonte** (nº de processo INPI, designação Madrid, registro estadual/outro
  país, citação de decisão, domínio, handle de rede social — o que for)
- **Classes / especificação de produtos-serviços** do registro
- **Titular**
- **Situação** (registrada / em análise / arquivada / extinta — uma marca
  extinta não é óbice mas pode ser relevante para fama e para direitos de um
  predecessor)
- **Data de depósito/primeiro uso se disponível**

**Não complemente silenciosamente.** Se você cita um número de processo INPI,
ele veio da busca que você rodou; se descreve uma marca que o usuário
mencionou, diga isso. Nunca invente um número de processo e nunca "preencha"
um detalhe que o registro não sustenta. Se a busca não retornou data de
depósito, escreva "data de depósito não disponível no resultado da busca" —
não chute.

### Adjacent families sweep (required before concluding)

Uma colidência que só checa correspondências exatas e quase-exatas perde as
marcas que um concorrente adotou *porque* a sua estava indisponível. Antes de
concluir, identifique 3–5 famílias de palavras adjacentes que o praticante
deveria também varrer, e peça ao usuário para confirmar ou complementar a
lista.

Famílias adjacentes são substitutos convencionais da categoria que um
concorrente razoável consideraria quando a marca direta está indisponível.
Para uma marca como `NEXUS CASA` no espaço de hub doméstico inteligente, as
famílias adjacentes incluem no mínimo:

- **Sinônimos de categoria** para NEXUS: `HUB`, `NINHO`, `NÚCLEO`, `LINK`,
  `CONECTA`, `PONTE`, `CENTRAL`, `PORTAL`.
- **Nomes estilo assistente** na mesma categoria de produto: `ALEXA`, `ECHO`,
  `SIRI`, `GOOGLE HOME`, `CORTANA`.
- **Variantes CASA / LAR / SMART**: `SMART HOME`, `LAR`, `CASA INTELIGENTE`,
  `MORADA`, `DOM`.
- **Gêmeos fonéticos** na raiz: `NEXIS`, `NEKSUS`, `NEXXUS`, `NECTIS`,
  `KNOXUS` (dependendo de como a palavra soa no mercado brasileiro).

O skill deve produzir um bloco de famílias adjacentes na seção de Marcas
Semelhantes com um prompt de confirmação:

> **Famílias adjacentes para varrer (confirme ou adicione):**
>
> - [família 1 — ex.: HUB / NINHO / LINK / CONECTA]
> - [família 2 — ex.: nomes estilo assistente]
> - [família 3 — ex.: variantes CASA / LAR / SMART]
> - [família 4 — gêmeos fonéticos na raiz]
>
> Uma colidência que só checa correspondências exatas e quase-exatas perde as
> marcas que um concorrente adotou porque a sua estava indisponível. Confirme
> se esta lista está completa para a categoria antes de eu continuar.

> **Quando jurisdições de língua não portuguesa estão em escopo,** a varredura
> fonética só em português perde a fonte mais comum de conflito
> transfronteiriço. Adicione:
> - **Equivalentes de tradução.** A marca traduzida para os idiomas
>   relevantes. Doutrina de equivalente estrangeiro trata tradução como a
>   mesma marca para fins de confusão.
> - **Transliteração.** A marca escrita na grafia relevante (cirílico,
>   chinês/japonês/coreano, árabe, hangul). Equivalência fonética entre
>   grafias é base reconhecida de conflito.
> - **Variações de grafia.** Marcas registradas em grafia não latina que soam
>   como a sua quando romanizadas.
>
> Se você não consegue fazer análise cross-language, diga isso: "Análise
> fonética e de equivalente-de-tradução cross-language não realizada — esta é
> a fonte mais comum de conflito transfronteiriço. Uma busca de colidência em
> [jurisdição] deveria incluí-la."

Se o praticante tem ferramenta de busca de marca conectada, rode de novo a
varredura contra cada família adjacente confirmada (exata + fonética +
tradução-de-equivalente-estrangeiro onde relevante) e adicione os resultados
à tabela de Marcas Semelhantes com a fonte `Família adjacente` anotada. Se
nenhum conector estiver disponível, diga isso, e liste as famílias como
input explícito de próximo passo para busca profissional completa — não pule
a varredura silenciosamente.

---

## Likelihood-of-confusion factors

> **A doutrina de risco de confusão é a doutrina brasileira, não um transplante
> do direito americano.** O critério central no Brasil é a possibilidade de
> confusão ou associação (Lei 9.279/1996 art. 124, XIX), avaliada pelo INPI e
> pelos tribunais (TRF-2, competente para recursos de decisões do INPI, e
> STJ) através da regra da especialidade — marcas idênticas ou semelhantes
> só colidem se identificarem produtos/serviços idênticos, semelhantes ou
> afins, salvo marca de alto renome (proteção em todas as classes) ou marca
> notoriamente conhecida (proteção no mesmo ramo, mesmo sem registro no
> Brasil).

Cite a base que se aplica: Lei 9.279/1996 art. 124, XIX (colidência com marca
registrada anterior — regra da especialidade); art. 125 (marca de alto
renome — todas as classes); art. 126 (marca notoriamente conhecida, CUP
art. 6º bis — mesmo ramo, independente de registro no Brasil); art. 129
(direito de uso exclusivo em todo território nacional ao titular do
registro).

Para cada fator, produza uma **sinalização**, não um veredito. Cada fator
deve dizer o que pesa para cada lado e onde está a incerteza:

- **Semelhança gráfica, fonética e ideológica das marcas.** Grafia, som,
  significado/conotação, impressão de conjunto — considerados em conjunto,
  como o INPI e os tribunais brasileiros fazem.
- **Afinidade entre produtos ou serviços (regra da especialidade).** Não se
  os produtos são idênticos — se consumidores esperariam que viessem da
  mesma fonte, ou se pertencem ao mesmo segmento mercadológico.
- **Canais de comercialização.** Onde cada lado efetivamente vende (ou
  venderia). Mesmos pontos de venda? Mesma distribuição? Mesmas feiras?
  Só online?
- **Grau de atenção do consumidor.** Compra por impulso em farmácia vs.
  compra corporativa ponderada muda o padrão de cuidado esperado.
- **Distintividade da marca anterior encontrada.** Fantasiosa / arbitrária /
  evocativa / descritiva com secondary meaning / genérica, e evidência de
  fama se houver. Marca anterior forte recebe proteção mais ampla.
- **Intenção.** Evidência de intenção de aproveitamento parasitário — uma
  quase-cópia com trade dress semelhante em classe adjacente é diferente de
  uma criação independente.
- **Confusão efetiva.** Qualquer evidência (reclamações direcionadas
  erroneamente, pesquisas, avaliações, posts em redes sociais).
- **Possibilidade de expansão.** Se o titular da marca anterior tende a
  expandir para o ramo da marca posterior, e vice-versa.

Per a postura de decisão em
`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md`:

- **Nunca conclua "sem risco de confusão".**
- Se incerto, escreva: "Marcas semelhantes encontradas — avaliação de
  confusão exigida antes da adoção." Ou: "Fatores pesam nos dois sentidos;
  julgamento do advogado necessário."
- Espaço livre para "nenhuma marca semelhante encontrada nas bases
  pesquisadas" só é adequado *se* uma busca real foi realizada; veja o
  fallback de não-busca acima caso contrário.

---

## Recommended next steps

Todo output de colidência termina com próximos passos concretos, agrupados
pelo que a triagem encontrou:

- **Se óbices de anterioridade encontrados:** reformule a marca, ou aceite o
  óbice de descritividade e planeje a construção de significado secundário ao
  longo do tempo; encaminhe para revisão do advogado antes de adotar.
- **Se marcas semelhantes encontradas nas bases pesquisadas:** revisão do
  advogado é exigida antes de adotar, depositar ou usar em marketing.
  Frequentemente o próximo passo é busca profissional completa para
  encontrar o que a triagem perdeu.
- **Se nenhuma marca semelhante encontrada mas nenhuma busca em base rodou:**
  busca completa é exigida antes da adoção. Nomeie as bases que precisam ser
  consultadas.
- **Se marcas semelhantes encontradas e a marca anterior é fraca, antiga, em
  classe diferente, ou extinta:** sinalize para revisão do advogado — a
  triagem não vai fazer essa chamada.
- **Sempre:** um parecer de colidência completo de advogado de marcas
  registrado, escalado ao investimento que a marca vai carregar. Uma marca
  que vai numa linha de produto e campanha nacional carrega mais peso que
  uma marca para um pop-up isolado.

---

## Output format

Prefixe o cabeçalho de trabalho de
`~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` `## Outputs`.

```markdown
[CABEÇALHO DE TRABALHO]

# Colidência de Marca — Primeira Passada (NÃO É PARECER)

**Esta é uma primeira passada, não um parecer de colidência.** Um parecer de
colidência exige busca profissional completa e julgamento do advogado. Um
resultado "sem conflito óbvio" aqui significa que a triagem não encontrou
nada — não significa que a marca está livre. Um advogado de marcas
registrado avalia antes de qualquer adoção, depósito ou investimento nesta
marca.

**Resultado da triagem:** [VERDE / AMARELO / VERMELHO — uma frase do porquê]

## Marca proposta

- **Marca:** [texto exato, estilização anotada]
- **Tipo de marca:** [nominativa / figurativa / mista]
- **Produtos / serviços:** [descrição]
- **Classes:** [números de classe NCL com descrição em uma linha]
- **Jurisdições:** [Brasil / Mercosul / via Madri / países específicos]
- **Base de confusão aplicada:** [art. 124, XIX / art. 125 / art. 126 — com o
  motivo de ser a correta]

## Óbices de anterioridade

| Óbice | Sinalizado | Nota |
|---|---|---|
| Genérico / descritivo / enganoso / geográfico / sobrenome / símbolo oficial / moral e bons costumes / alto renome / notoriamente conhecida / forma necessária | [nenhum / sinalizado] | [uma linha se sinalizado] |

## Similar marks check

**Fontes pesquisadas:** [bases consultadas, com datas — ou "nenhuma busca em
base rodou; ver nota de escopo abaixo."]
**Escopo:** [classes, jurisdições, exata-vs-fonética, busca figurativa ou não]

**Famílias adjacentes varridas (confirmadas com o usuário):**
- [família 1 — ex.: HUB / NINHO / LINK / CONECTA / PONTE / PORTAL]
- [família 2 — ex.: nomes estilo assistente]
- [família 3 — ex.: variantes CASA / LAR / SMART]
- [família 4 — gêmeos fonéticos na raiz]

*Uma colidência que só checa correspondências exatas e quase-exatas perde as
marcas que um concorrente adotou porque a sua estava indisponível. Se alguma
família não foi varrida (sem conector, tempo indisponível), ela é listada
explicitamente como input de próximo passo para a busca profissional
completa — não pulada silenciosamente.*

| Marca | Fonte | Classes / P&S | Titular | Situação | Depósito/uso | Nota |
|---|---|---|---|---|---|---|
| [exata] | [nº de processo INPI / citação / URL] | [lista de classes] | [titular do registro] | [registrada/em análise/arquivada/extinta] | [data ou "não disponível"] | [por que importa — correspondência exata / família adjacente] |

*Se nenhuma busca foi rodada:* **Nenhuma busca em base de dados foi
realizada.** Esta triagem não consultou a base do INPI, Solve Intelligence,
JusBrasil, registro.br, redes sociais, ou qualquer fonte de uso anterior não
registrado. Uma busca de anterioridade completa nessas bases é exigida antes
de qualquer conclusão sobre disponibilidade.

## Confusion factors — flags for attorney review

Para cada fator sob a base aplicada, uma sinalização de uma linha anotando o
que pesa para cada lado.

| Fator | Sinalização | Direção |
|---|---|---|
| Semelhança gráfica/fonética/ideológica | [nota] | [pesa a favor / contra conflito / misto] |
| Afinidade entre produtos ou serviços | [nota] | [direção] |
| Canais de comercialização | [nota] | [direção] |
| Grau de atenção do consumidor | [nota] | [direção] |
| Distintividade da marca anterior | [nota] | [direção] |
| Intenção | [nota] | [direção] |
| Confusão efetiva | [nota ou "nenhuma evidência surgida"] | [direção] |
| Possibilidade de expansão | [nota] | [direção] |

**Conclusão sobre confusão:** *Este skill não conclui.* Ou:
- "Marcas semelhantes encontradas; avaliação de confusão do advogado exigida
  antes da adoção."
- "Nenhuma marca semelhante encontrada nas bases pesquisadas; busca completa
  exigida antes da adoção."
- "Fatores pesam nos dois sentidos; julgamento do advogado necessário."

## Recommended next steps

- [próximo passo específico 1 — ex.: "Busca profissional completa na base do
  INPI, registro.br e fontes de uso anterior antes da adoção"]
- [próximo passo específico 2 — ex.: "Revisão de design-around da marca
  `APEXLEAF` na classe 25 se a intenção for prosseguir"]
- [próximo passo específico 3 — ex.: "Reformular a marca — forma atual é
  descritiva e exigirá significado secundário"]
- [roteamento per
  `~/.claude/plugins/config/claude-for-legal/ip-legal/CLAUDE.md` — OC de
  marcas ou advogado(a) de PI in-house nomeado no perfil de prática]

## Citation verification

Todo processo, número de registro, lei e resultado de base de dados neste
memorando deve ser verificado contra a fonte autoritativa antes de qualquer
confiança. Números de processo INPI, classes e datas de depósito são os
locais mais comuns de erro. Não cite um resultado que você não consegue
abrir.
```

---

## Non-lawyer gate

Antes de emitir o output, leia `## Who's using this`. Se o Papel é
Não-advogado (incluindo Agente da Propriedade Industrial fora de processo
INPI):

> Este output é uma triagem de pesquisa, não parecer jurídico. Adotar,
> depositar, ou investir nesta marca com base só nesta triagem tem
> consequências legais — inclusive ser processado por infração sobre uma
> marca que "passou" nesta checagem. Um advogado de marcas registrado precisa
> avaliar antes de você avançar.
>
> Aqui está um briefing para levar a um advogado — vai reduzir o tempo da
> conversa:
>
> [Gere um resumo de 1 página: a marca proposta, produtos/serviços e classes,
> os óbices de anterioridade (se houver), as marcas semelhantes encontradas
> (se houver), o que foi e não foi pesquisado, e as três perguntas para fazer
> ao advogado.]
>
> Se precisar encontrar advogado de marcas registrado: a OAB (seccional do seu
> estado) mantém serviço de indicação. A ABPI (Associação Brasileira da
> Propriedade Intelectual) mantém diretório de profissionais especializados
> em PI.

Entregue o memorando de triagem completo junto com o briefing. Não retenha a
análise.

---

## Output location

Se workspaces de matéria estão habilitados e há matéria ativa, escreva o
output em
`~/.claude/plugins/config/claude-for-legal/ip-legal/matters/<matter-slug>/outputs/colidencia-<marca-slug>-YYYY-MM-DD.md`.
Caso contrário escreva em
`~/.claude/plugins/config/claude-for-legal/ip-legal/outputs/colidencia-<marca-slug>-YYYY-MM-DD.md`
e apresente o caminho ao usuário.

Adicione uma entrada de uma linha ao `history.md` da matéria se houver
matéria ativa.

---

## Close with the next-steps decision tree

Termine com a árvore de decisão de próximos passos per CLAUDE.md
`## Outputs`. Customize as opções para o que este skill acabou de produzir —
os cinco ramos padrão (redigir o X, escalar, buscar mais fatos, aguardar,
algo mais) são um ponto de partida, não uma amarra. A árvore é o output, o
advogado escolhe.

## What this skill does not do

- **Concluir que uma marca está livre.** Nunca. O guardrail mais alto do
  plugin.
- **Substituir busca na base do INPI, registro.br, fontes de uso anterior
  não registrado, checagem de serviço de monitoramento, ou busca de marca
  figurativa/tridimensional.**
- **Depositar pedido de registro de marca.** Depósito é tarefa do advogado ou
  agente da propriedade industrial; este skill informa a decisão de
  depositar.
- **Avaliar trade dress, diluição de marca, ou reivindicação de alto renome**
  além de sinalização preliminar. Reconhecimento de alto renome exige
  processo administrativo específico perante o INPI que este skill não
  tenta substituir.
- **Endereçar óbices de direito estrangeiro local** (ex.: padrões de
  semelhança fonética no Japão, doutrina de equivalente estrangeiro na UE)
  além de sinalizar que análise estrangeira é exigida quando jurisdição
  estrangeira está em escopo.
- **Citar outputs a clientes, contrapartes, ou imprensa.** Isto é pesquisa
  interna. Sigiloso se o cabeçalho no topo se aplicar.

---

## Tone

Direto, concreto, honesto sobre escopo. O advogado lendo este output deve
saber em dez segundos o que a triagem encontrou, o que não encontrou, e o
que precisa acontecer antes de qualquer adoção da marca. Sem prosa de
hedging. O guardrail no topo e a linha "este skill não conclui" sobre
confusão fazem o trabalho de escopo.
