# Custos e Tributos — Direito Imobiliário e de Família (Brasil, 2026)

Este arquivo mapeia os custos esperados em operações de regularização imobiliária, divórcio/partilha e inventário. **Todos os valores são FAIXAS — varia por município, estado, ente cartorial e perfil do caso**. Para uma estimativa numérica de um caso específico, rode `scripts/calc_custos.py`.

## Mapa rápido — quem paga o quê

| Operação | Tributos | Emolumentos | Honorários | Outros |
|---|---|---|---|---|
| Compra e venda registrada | ITBI | Tabelião + RI | Advogado (opcional) | Avaliação |
| Doação | ITCMD | Tabelião + RI | Advogado | – |
| Herança (inventário) | ITCMD | Tabelião (extra) ou custas (jud) + RI | Advogado | Avaliações, certidões |
| Partilha em divórcio | ITBI sobre torna (se houver) | Tabelião + RI | Advogados | Avaliações |
| Usucapião | – (declaratório) | Tabelião (ata) + RI | Advogado | Eng./Topógrafo, ART |
| REURB-S | Isento | Isento | Defensoria/Município | – |
| REURB-E | – | Reduzidos | Advogado | Estudo técnico |
| Retificação matrícula | – | RI | Advogado (eventual) | Eng./Topógrafo |
| Averbação construção | – | RI | – | Habite-se, CND |

## ITBI — Imposto de Transmissão de Bens Imóveis

**Competência**: municipal (art. 156, II CF).

**Fato gerador**: transmissão **onerosa** de bens imóveis entre vivos (compra e venda, permuta, dação em pagamento, integralização de capital com torna, cessão de direitos de aquisição).

**Quem paga**: por regra, o adquirente (comprador) — embora possa ser negociado.

**Alíquota**: 2-3% típico (varia por município; ex.: São Paulo 3%, Belo Horizonte 3%, Curitiba 2,7%). Algumas capitais oferecem alíquota reduzida em programa de habitação popular.

**Base de cálculo**: maior entre (a) valor da operação declarada e (b) valor venal de referência do município.

**STF (2021, Tema 1.113)**: a base de cálculo não pode ser fixada unilateralmente pelo município acima do valor de mercado — a referência do venal é máxima da publicidade legal.

**Isenções comuns** (variam por município):
- Primeira aquisição via programa habitacional popular (MCMV, etc.)
- Integralização de capital social em pessoa jurídica (com ressalvas — STF Tema 796)
- Sucessão e doação (não incide ITBI, mas ITCMD)
- Partilha em divórcio sem torna (não há transmissão onerosa)
- **Partilha em divórcio com torna**: incide ITBI proporcional ao valor da torna (quanto um cônjuge paga ao outro pra ficar com o bem)

**Reforma Tributária**: LC 214/2025 e LC 227/2026 trouxeram ajustes pontuais (alinhamento de base com valor venal de referência, regras de integralização) — ITBI permanece municipal.

**Prazo de recolhimento**: antes do registro no RI; cartório só registra com guia paga.

## ITCMD — Imposto sobre Transmissão Causa Mortis e Doação

**Competência**: estadual (art. 155, I CF).

**Fato gerador**: transmissão **gratuita** — por morte (causa mortis) ou doação (inter vivos).

**Quem paga**:
- Causa mortis: os herdeiros, proporcionalmente ao quinhão
- Doação: o donatário (quem recebe), regra geral

**Alíquota em maio/2026**:

| Estado | Alíquota vigente em 2026 | Após adaptação LC 227/2026 (2027+) |
|---|---|---|
| SP | 4% (fixa) | Progressiva obrigatória (PL em tramitação) |
| RJ | Progressiva 4-8% | Mantém progressiva |
| MG | 5% (fixa) | Progressiva (adaptação prevista) |
| RS | Progressiva 3-6% | Progressiva 4-8% |
| PR | 4% (fixa) | Adaptação prevista |
| SC | 1-8% (progressiva) | Mantém progressiva |
| BA | Progressiva 4-8% | Mantém |
| DF | 4-6% (progressiva) | Mantém/ajusta |
| GO | 2-8% | Mantém |
| Outros | Variam 2-8% | Progressiva obrigatória |

**Verificar sempre a lei estadual atualizada**. A consolidação progressiva pós-LC 227/2026 só passa a ter eficácia a partir de **01/01/2027** nos estados que editarem nova lei em 2026 (anterioridade).

**Base de cálculo**:
- Imóveis: valor venal de referência ou valor de mercado (maior)
- Móveis: avaliação
- Empresas: valor patrimonial das quotas/ações
- Bens no exterior: agora permitido (EC 132/2023) — usualmente valor declarado pelo herdeiro

**Prazo de recolhimento**:
- Causa mortis: varia por estado. Comum: 60 dias do óbito para evitar multa progressiva; pagamento antes da partilha/escritura
- Doação: antes da lavratura da escritura

**Multa por atraso**: tipicamente 10% sobre o ITCMD devido, podendo escalar até 20% ou mais conforme o estado.

**Parcelamento**: maioria dos estados permite (até 12-36 meses, com juros pela taxa Selic).

**Isenções comuns** (variam por estado):
- Imóvel residencial único de baixa renda para o cônjuge sobrevivente
- Herdeiros com patrimônio total abaixo de teto (ex.: 10.000 UFESP em SP) — varia
- Doações a entidades sem fins lucrativos certificadas
- Doação de pequenos valores (limites anuais por estado)

**ITCMD em casos sensíveis**:
- **Acumulação de doações sucessivas** (LC 227/2026): doações entre as mesmas partes em janela temporal somam-se para fins de alíquota progressiva
- **Renúncia translativa** (em favor de pessoa): dupla incidência — primeiro como herdeiro, depois como doador
- **Bens em outro estado**: cada estado tributa os bens em seu território (imóveis); móveis pelo domicílio do falecido

## Emolumentos cartoriais

Valores cobrados pelos cartórios pelos serviços. Tabela é **estadual**, fixada por lei estadual ou regimento do Tribunal de Justiça (TJ). Varia muito entre estados.

### Estrutura típica

| Ato | Como é calculado |
|---|---|
| Escritura pública (compra, doação, divórcio, inventário) | Valor por faixa de valor da operação |
| Registro de imóvel | Valor por faixa do valor declarado |
| Averbação simples (estado civil, construção) | Valor fixo + valor da matrícula |
| Certidão de matrícula | Valor por número de páginas |
| Ata notarial | Valor por folha + serviços anexos |

### Faixas indicativas (valores aproximados em 2026, podem variar 50% pra mais ou menos por estado)

| Operação | Faixa de emolumentos |
|---|---|
| Escritura de compra e venda de imóvel R$ 500.000 | R$ 3.000-8.000 |
| Registro de imóvel R$ 500.000 | R$ 2.000-5.000 |
| Escritura de divórcio | R$ 800-3.000 |
| Escritura de inventário e partilha (valor até R$ 1mi) | R$ 5.000-15.000 |
| Ata notarial para usucapião | R$ 500-2.000 |
| Certidão de matrícula | R$ 50-200 |
| Averbação de construção | R$ 200-800 |

**Consulta autorizada**: tabela do TJ estadual ou do CNJ. Cartórios são obrigados a manter a tabela visível ao público.

## Custas judiciais

Quando o caso vai para a Justiça (inventário judicial, divórcio litigioso, usucapião judicial, etc.):

- Tabela estadual de taxa judiciária (geralmente 1-2% sobre o valor da causa)
- Diligências de oficial de justiça
- Perícias técnicas (avaliação judicial)
- Honorários de inventariante (até 5% do espólio, art. 1.987 CC)

**Assistência judiciária gratuita** (Lei 1.060/1950 e art. 98 CPC): disponível para quem comprova insuficiência de recursos. Isenta de custas, perícias e honorários sucumbenciais.

## Honorários advocatícios

**Não há tabela única obrigatória**. Cada OAB estadual publica tabela mínima de honorários (referencial — pode ser negociado abaixo em casos especiais, embora a prática desfavoreça).

### Faixas indicativas

| Tipo de caso | Faixa |
|---|---|
| Consulta inicial / Hora técnica | R$ 200-1.000/hora |
| Divórcio consensual extrajudicial | R$ 3.000-15.000 (ou % sobre partilha) |
| Divórcio litigioso | R$ 10.000-50.000+ (ou 10-20% sobre partilha) |
| Inventário extrajudicial | 5-10% sobre o espólio |
| Inventário judicial | 10-15% sobre o espólio |
| Usucapião extrajudicial | R$ 5.000-20.000 |
| Usucapião judicial | R$ 8.000-30.000 |
| REURB-E individual | R$ 3.000-10.000 |
| Retificação de matrícula | R$ 2.000-8.000 |
| Adjudicação compulsória | R$ 5.000-15.000 |

**Modelos de cobrança**:
- Valor fixo
- Percentual sobre o valor do caso
- Êxito (sucesso) — comum em litigioso
- Tabela OAB
- Mensal/horária (para casos longos)

Sempre exigir **contrato escrito** com previsão clara de honorários, escopo, modalidade de cobrança e momento de pagamento.

## Custos profissionais específicos

### Engenheiro/topógrafo (regularização imobiliária)

| Serviço | Faixa |
|---|---|
| Levantamento topográfico (urbano) | R$ 1.500-5.000 |
| Levantamento topográfico (rural) | R$ 3.000-15.000+ (por área) |
| Georreferenciamento (rural — INCRA) | R$ 5.000-30.000+ |
| Projeto arquitetônico para regularização | R$ 3.000-15.000 |
| Laudo de avaliação | R$ 1.500-8.000 |
| ART/RRT | R$ 80-300 |

### Contador (averbação de construção e empresas)

| Serviço | Faixa |
|---|---|
| CND da obra (DCTFWeb, GFIP retroativa) | R$ 1.500-5.000 |
| Avaliação de quotas societárias | R$ 3.000-15.000 |
| Declaração ITCMD/ITBI (auxílio) | R$ 500-2.000 |

## Tributos relacionados — recorrentes

### IPTU (imóvel urbano)

Municipal, anual. 0,3-1,5% típico sobre valor venal. Atenção: dívidas de IPTU acompanham o imóvel (obrigação propter rem) — comprador assume débitos não quitados.

### ITR (imóvel rural)

Federal, anual. Declaração obrigatória. Alíquota progressiva pela área e produtividade (0,03% a 20%).

### Taxa de Limpeza, Iluminação, Coleta de Lixo

Municipais, variáveis. Cobradas junto ao IPTU em geral.

### Condomínio (imóvel em condomínio)

Privado, mensal. Dívidas também acompanham o imóvel (propter rem).

## Imposto de Renda — ganho de capital na alienação

Quando se vende imóvel: incide IR sobre ganho de capital (diferença entre valor de venda e valor de aquisição corrigido).

- **Alíquota**: 15% até R$ 5 mi de ganho; progressiva acima
- **Isenções**:
  - Imóvel único de até R$ 440.000 (a cada 5 anos)
  - Reinvestimento em imóvel residencial em 180 dias
  - Imóveis adquiridos antes de 1969 (com tabela de redução)

**Em inventário**: a transmissão causa mortis é isenta de IR (não há ganho). A partilha entre herdeiros também. Mas se um herdeiro recebe valor maior que sua cota e paga em dinheiro aos outros (torna), há ganho tributável.

**Em divórcio**: a partilha em si é isenta. Se houver torna em dinheiro/valor superior ao quinhão original, pode incidir IR.

## Outras taxas e despesas

| Item | Faixa |
|---|---|
| Reconhecimento de firma | R$ 5-20 cada |
| Cópia autenticada | R$ 5-15/folha |
| Certidão de nascimento/casamento/óbito (2ª via) | R$ 50-150 |
| Certidões de distribuidor (fórum) | R$ 30-100 cada |
| Certidão negativa de débitos (Receita, Estado, Município) | Gratuitas online |
| Procuração pública | R$ 200-800 |
| Tradução juramentada (documentos do exterior) | R$ 50-150/lauda |
| Apostila de Haia (documento estrangeiro) | R$ 60-150 |

## Calculadora interativa

Para estimar custos de um caso específico:

```bash
python /Users/maiconfuhr/.claude/skills/direito-familiar-imobiliario/scripts/calc_custos.py
```

O script pergunta:
- Tipo de operação (compra, divórcio, inventário, doação, usucapião)
- Valor estimado do bem
- UF do bem e do contribuinte
- Grau de parentesco (para ITCMD)

E devolve faixa estimada de ITBI/ITCMD/emolumentos/honorários.

## Princípios para usuário leigo

1. **Pegue 3 orçamentos**: advogado, cartório (se aplicável), engenheiro. Variação de 30-50% é comum.
2. **Calcule o tributo antes**: ITCMD/ITBI muitas vezes é o maior custo — surpresa ao final pode atrapalhar o caixa.
3. **Pergunte sempre se há isenção** aplicável (programa habitacional, baixa renda, primeira aquisição).
4. **Não confunda emolumentos com honorários**. Emolumento é cartório (tabela oficial). Honorário é advogado (negociável).
5. **Aproveite o desconto do recolhimento antecipado**: vários estados oferecem desconto no ITCMD se pago em 60-90 dias do óbito.
6. **Anote tudo recibido**: cada certidão, cada guia paga, cada serviço — pra IR e pra prestação de contas eventual.
