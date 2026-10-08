---
name: transicao-iss-ibs-sbroggioadv
title: transicao-iss-ibs — o ISS tem data de extinção, e isso não invalida a cobrança de hoje
description: 'O cronograma da EC 132/2023 e da LC 214/2025 aplicado ao ISS, com os anos e percentuais exatos do anexo e com o dispositivo que opera a queda dentro da própria LC 116: o art. 8º-B, incluído pela LC 214/2025, que reduz as alíquotas do imposto em 10, 20, 30 e 40 por cento das vigentes em 31 de dezembro de 2028, nos exercícios de 2029 a 2032, com os benefícios fiscais reduzidos na mesma proporção. Responde as três perguntas que o procurador municipal faz: o que muda no lançamento de hoje (nada — 2026 é ano-teste e o ISS segue exigível), o que acontece com a dívida ativa de ISS já constituída (segue exigível e executável, o estoque não evapora com a extinção do tributo) e o que o Município precisa observar na transição, de benefício com prazo longo a contrato com cláusula tributária. Aciona: "reforma tributária", "ISS vai acabar?", "IBS", "cronograma da transição", "2033", "benefício de ISS depois de 2029", "a dívida ativa de ISS continua valendo?".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/procurador-municipal-os-marketplace/tree/main/procurador-municipal-os/skills/transicao-iss-ibs
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: tax
language: pt
---

# transicao-iss-ibs — o ISS tem data de extinção, e isso não invalida a cobrança de hoje

O ISS está em extinção programada. A frase assusta e é mal usada dos dois lados: contribuinte que
lê "o imposto vai acabar" e para de recolher, e procurador que escreve parecer como se o tributo
fosse permanente. Nenhum dos dois está certo. Esta skill fixa o cronograma com os números exatos do
anexo e separa o que muda **agora** do que muda **depois**.

Este produto atende o **Município**.

## Quando esta skill entra

- Sempre que qualquer entrega de ISS precisar do aviso da transição (trava **P6**).
- Em parecer que projete receita, conceda benefício ou fixe prazo que atravesse 2029.
- Quando o contribuinte alega que o imposto "está sendo extinto" para resistir ao lançamento.
- No planejamento da carteira de dívida ativa de ISS com horizonte longo.

## 1. O cronograma — a tabela do anexo, sem arredondamento

Fonte: `context/reforma-tributaria-transicao.md` (**EC 132/2023** + **LC 214/2025**).

| Ano | Situação |
|---|---|
| **2026** | **Ano-teste:** CBS 0,9% + IBS 0,1%, compensados com PIS/COFINS — **o ISS segue cobrado normalmente** |
| **2027-2028** | CBS à alíquota de referência reduzida em **0,1 p.p.**; IBS **0,1%**; extinção de PIS/COFINS |
| **2029** | Participação IBS **10%**; participação ICMS/ISS **90%** |
| **2030** | Participação IBS **20%**; participação ICMS/ISS **80%** |
| **2031** | Participação IBS **30%**; participação ICMS/ISS **70%** |
| **2032** | Participação IBS **40%**; participação ICMS/ISS **60%** |
| **2033** | **Extinção do ISS** |

O **IBS** — Imposto sobre Bens e Serviços — é de competência **estadual/municipal**; a **CBS**,
federal. É o IBS que substitui o ISS na arrecadação do Município.

**Fontes registradas pela pesquisa:** portal da Receita Federal sobre a reforma tributária do consumo
(atualizado em **03/07/2026**) e LC 214/2025, arts. 344 e 347. Parecer que projeta receita cita a
fonte, não "a reforma".

## 2. O dispositivo que opera a queda no ISS — LC 116, art. 8º-B

O cronograma acima é o horizonte; a **redução da alíquota do ISS já está escrita na própria LC 116**,
no art. 8º-B, **incluído pela LC 214/2025** (`context/lc-116-iss.md`):

> "Em relação aos fatos geradores ocorridos de 1º de janeiro de 2029 a 31 de dezembro de 2032, as
> alíquotas do imposto serão reduzidas nas seguintes proporções das alíquotas previstas nas
> legislações dos Municípios ou do Distrito Federal, **vigentes em 31 de dezembro de 2028**:"

| Inciso | Redução | Exercício |
|---|---|---|
| I | **10%** | 2029 |
| II | **20%** | 2030 |
| III | **30%** | 2031 |
| IV | **40%** | 2032 |

Três leituras que o texto impõe, e que quase todo resumo erra:

- **A referência é congelada.** A redução incide sobre a alíquota prevista na legislação municipal
  **vigente em 31/12/2028** — não sobre a do exercício corrente. A lei municipal que estiver em vigor
  naquela data vira a base de comparação de todo o período.
- **A redução é dos percentuais dos incisos**, aplicada às alíquotas — transcreva os incisos, não
  descreva "cai 10 pontos ao ano".
- **Os benefícios caem junto.** **§1º:** no período, "os benefícios ou os incentivos fiscais ou
  financeiros relativos ao imposto serão reduzidos na mesma proporção da redução das alíquotas". O
  **§2º** manda reduzir na mesma proporção os percentuais e parâmetros usados para calcular esses
  benefícios; o **§3º** afasta essa aplicação quando o benefício já tiver sido reduzido
  proporcionalmente por força do caput.

O compilado da LC 116 marca esses dispositivos com a nota **"Produção de efeitos"**, e o cabeçalho
da lei traz **"(Vide Lei Complementar nº 214, de 2025)"** — sinal de que a eficácia é diferida e
segue o calendário do §1. Confira a nota no anexo antes de afirmar vigência imediata de qualquer
inciso.

## 3. O que **não** muda: 2026, o lançamento e a execução

Hoje é o **ano-teste**. O ISS é exigível, o lançamento é válido, a inscrição em dívida ativa é
regular e a execução fiscal corre normalmente. O aviso da transição é de **horizonte, não de
invalidade** — confundir os dois é errar contra o próprio ente.

Três consequências diretas:

- **Resistência ao lançamento com base na reforma não tem amparo.** A extinção é em 2033; o fato
  gerador de 2026 se rege pela lei de 2026.
- **A dívida ativa de ISS já constituída não evapora com a extinção do tributo.** O crédito nasceu
  sob a lei vigente ao tempo do fato gerador; a esteira de cobrança segue por
  `divida-ativa-municipal` e `execucao-fiscal-lef`. O estoque inscrito é ativo do Município e
  atravessa a transição.
- **A prescrição não muda por causa da reforma.** Os marcos continuam sendo os de sempre — art. 2º,
  §3º da LEF, art. 40 e os **Temas 566-571/STJ**. Regra de transição específica sobre prazos na LC 214/2025
  → `[VERIFICAR]`: a pesquisa confirmou o cronograma, não capturou artigos.

## 4. O que o Município precisa observar na transição

| Frente | O que conferir |
|---|---|
| **Benefícios de ISS com prazo longo** | Benefício ou incentivo que atravesse 2029 será reduzido na mesma proporção da alíquota (art. 8º-B, §§1º-2º). Concessão nova com prazo além de 2028 tem de declarar isso no ato |
| **A lei municipal vigente em 31/12/2028** | É a referência congelada do art. 8º-B. Alteração de alíquota até lá define a base de todo o período de transição — decisão de política fiscal, não de gabinete |
| **Contratos e concessões com cláusula tributária** | Reequilíbrio e repactuação que suponham o ISS permanente nascem defasados. O consultivo entra por `parecer-consultivo`, com o regime de transição do art. 23 da LINDB (`lindb-como-metodo`) |
| **Projeção de receita e planejamento da carteira** | Só com os números desta tabela e a fonte citada. Projeção com número não medido é `[VERIFICAR]` |
| **Piso e teto do ISS enquanto ele existe** | As alíquotas mínima de 2% e máxima de 5% seguem valendo até a extinção — `iss-conteudo-e-lista` |

## 5. O que este produto **não** afirma sobre a reforma

A pesquisa confirmou a existência das normas e o cronograma. **Não** capturou artigos da LC 214/2025
nem os números seguintes — que, portanto, **não existem para o produto** e entram como `[VERIFICAR]`:

- alíquota final ou de referência do IBS;
- trava de teto, split payment e mecânica de repartição;
- regra de crédito e de compensação no período de transição;
- qualquer "art. X da LC 214/2025" — citar dispositivo dessa lei sem conferir na fonte é violação de
  **P2**, mesmo quando a afirmação parece óbvia.

Fora da tabela do §1 e do art. 8º-B da LC 116, nenhum ano, percentual ou dispositivo é escrito de
memória.

## Travas desta skill

- **P6 (a desta skill).** É esta a skill dona do cronograma. Toda entrega de ISS do produto fecha com
  ele; conteúdo de ISS sem o aviso nasce desatualizado por design.
- **P2.** Anos, percentuais e incisos vêm de `context/reforma-tributaria-transicao.md` e de
  `context/lc-116-iss.md`. Número fora deles → `[VERIFICAR]`.
- **TV3.** O ISS **não** é tributo permanente, e também **não** é tributo extinto: em 2026 é
  exigível, com data marcada. Texto que trate qualquer das duas pontas como absoluta é recusado pelo
  `validador-fazendario-vigente`.
- **P1.** Aqui se trata do efeito da reforma sobre o **ISS**, o tributo do Município. O IBS aparece
  como o que o substitui; a CBS, só como contraparte do cronograma. Tributo de outra esfera não entra
  — `procurador-estadual-os` e `procurador-federal-os` cobrem as suas.
- **P4.** Projeção e parecer aqui são estudo; a decisão de política fiscal e a assinatura do parecer
  são do procurador e do gestor, indelegáveis.

**Próximo passo:** conteúdo substantivo do imposto → `iss-conteudo-e-lista`. Estoque inscrito →
`divida-ativa-municipal`. Parecer sobre benefício ou contrato que atravessa a transição →
`parecer-consultivo` com `lindb-como-metodo`. Toda entrega fecha por `suprema-corte-fazendaria`.
