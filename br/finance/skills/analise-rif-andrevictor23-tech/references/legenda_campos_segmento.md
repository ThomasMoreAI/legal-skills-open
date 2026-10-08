# Legenda Oficial dos Campos de Valores (CampoA–CampoE) por CodigoSegmento

Tabela de referência com o significado dos campos de valores das comunicações COAF, por segmento comunicante. Extraída em 31/07/2026 da base curada do NexVirtus (sistema profissional de análise de RIF), que espelha a documentação oficial do COAF.

**Regra de precedência**: se o próprio CSV de Comunicações trouxer linhas de legenda (linhas não-indexadoras com o padrão `NN - Nome do segmento: CampoA = ...`), a legenda do arquivo prevalece sobre esta tabela. Esta tabela é o fallback autoritativo quando o CSV não traz legenda ou traz legenda truncada.

## Segmentos do SFN (mais frequentes em RIF)

| Segmento | CampoA | CampoB | CampoC | CampoD | CampoE |
|---|---|---|---|---|---|
| **41 — SFN Atípicas (COS)** | Total | Valor do Crédito | Valor do Débito | Valor do Provisionamento | Valor da Proposta |
| **42 — SFN Espécie (COE)** | Total | Valor do Crédito | Valor do Débito | Valor do Provisionamento | Valor da Proposta |

> **ATENÇÃO**: em versões antigas desta skill, os campos D/E de 41/42 constavam como "Crédito em Espécie"/"Débito em Espécie" — legenda **incorreta**, sem fonte. A legenda correta é Provisionamento/Proposta.

## Demais segmentos

| Segmento | CampoA | CampoB | CampoC | CampoD |
|---|---|---|---|---|
| 15 | Valor da operação ou dos ativos vendidos | Valor pago em espécie | — | — |
| 17 | Valor do Prêmio | Valor da(s) aposta(s)/arrecadação | Qtd. premiações | Valor pago em espécie |
| 19 | Valor da operação ou proposta | Valor do(s) pagamento(s) em espécie | — | — |
| 20 | Valor do Prêmio | Valor da(s) aposta(s)/arrecadação | Qtd. premiações | — |
| 21 | Valor da(s) ocorrência(s) | — | — | — |
| 22 | Valor da operação | Valor do(s) pagamento(s) | — | — |
| 23 | Valor da operação | Valor do(s) pagamento(s) em espécie | — | — |
| 24 | Valor do Imóvel objeto da operação | Valor da transação/operação | — | — |
| 36 | Total | Valor Transação(ões) Nacional(is) | Valor Transação(ões) Internacional(is) | — |
| 37 | Valor da Operação | Valor do Prêmio/Contribuição/Devolução | Quantidade | — |
| 43 | Valor da Operação/Contribuição | — | — | — |
| 44 | Valor | — | — | — |
| 45 | Valor Transportado | Valor Guardado/Custodiado | Proposta | — |
| 46 | Valor total | Valor pago em espécie | — | — |
| 47 | Valor | — | — | — |
| 48 | Valor total | Valor pago em espécie | — | — |
| 49 | Valor total | Valor pago em espécie | — | — |
| 50 | Valor | — | — | — |
| 51 | Valor total | Valor pago em espécie | — | — |
| 52 | Valor total | Valor pago em espécie | — | — |
| 53 | Valor | — | — | — |
| 54 | Valor | — | — | — |
| 55 | Valor | — | — | — |
| 56 | Valor | — | — | — |
| 57 | Valor Transação(ões) Nacional(is) | Valor Transação(ões) Internacional(is) | — | — |
| 58 | Valor da(s) operação(ões) | — | — | — |
| 59 | Valor da(s) operação(ões) | — | — | — |
| 60 | Valores sacados | Valores apostados | — | — |
| 61 | Valor do(s) prêmio(s) | Valor da(s) aposta(s) | Valor de operação de outro tipo | — |

Campos não listados (—) não têm significado definido para o segmento; se vierem preenchidos, registrar como [VERIFICAR] em vez de interpretar.
