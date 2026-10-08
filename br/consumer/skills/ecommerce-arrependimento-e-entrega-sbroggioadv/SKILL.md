---
name: ecommerce-arrependimento-e-entrega-sbroggioadv
title: E-commerce — arrependimento e entrega
description: 'Estrutura a defesa e a cobrança em compra feita fora do estabelecimento comercial — e-commerce, telefone, domicílio: informação obrigatória do site (Decreto 7.962/2013), direito de arrependimento em 7 dias (art. 49 do CDC), forma de exercício, quem arca com o frete de devolução, atraso e não entrega, vinculação da oferta e a defesa de erro de preço. Aciona: cliente se arrependeu de compra online, produto não chegou ou chegou atrasado, loja recusou cumprir o preço anunciado, dúvida sobre quem paga o frete da devolução, cancelamento de compra fora da loja física.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/consumidor-adv-os-marketplace/tree/main/consumidor-adv-os/skills/ecommerce-arrependimento-e-entrega
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: consumer
language: pt
---

# E-commerce — arrependimento e entrega

## Quando esta skill entra
Compra feita **fora do estabelecimento comercial** — site, app, telefone, domicílio — com
arrependimento, atraso/não entrega, ou recusa do fornecedor em cumprir o preço ofertado.

## Base normativa
CDC (Lei 8.078/1990), arts. 30, 35 e 49 · Decreto 7.962/2013 (anexo
`context/decreto-7962-ecommerce.md`).

## Informação obrigatória no site
Art. 2º do Decreto 7.962/2013: nome empresarial + CNPJ/CPF; endereço físico e eletrônico;
características essenciais (inclusive riscos à saúde/segurança); discriminação de despesas
adicionais (frete, seguro) no preço; condições integrais da oferta; restrições de forma clara e
ostensiva. Compras coletivas (art. 3º) somam quantidade mínima para efetivação, prazo de uso e
identificação do fornecedor do site **e** do fornecedor do produto.

## Direito de arrependimento — 7 dias
Art. 49 do CDC: o consumidor pode desistir do contrato em **7 dias** a contar da assinatura ou do
recebimento do produto/serviço, sempre que a contratação ocorrer **fora do estabelecimento
comercial** — a jurisprudência consolidada enquadra a compra online nessa hipótese. Efeito
(parágrafo único): os valores pagos são devolvidos **de imediato**, monetariamente atualizados.

**Forma de exercício** (Decreto 7.962/2013, art. 5º): o fornecedor deve informar de forma clara e
ostensiva os meios para exercer o arrependimento; pode ser exercido pela mesma ferramenta usada na
contratação (§1º); rescinde os contratos acessórios **sem qualquer ônus** para o consumidor (§2º);
comunicação imediata à instituição financeira/administradora do cartão, para não lançar a
transação ou estornar se já lançada (§3º); confirmação imediata do recebimento da manifestação
(§4º).

**Frete de devolução:** o decreto não fixa expressamente "quem paga o frete". 🟡 A leitura
sistemática do §2º do art. 5º ("sem qualquer ônus para o consumidor") é a base para atribuir o
custo da devolução ao **fornecedor** quando o arrependimento é regular — apresentar como
interpretação sistemática, não como citação literal de artigo que fixe o valor.

## Atraso e não entrega
Vício de qualidade por disparidade entre a oferta e o cumprimento. O consumidor pode exigir,
alternativamente (art. 35): (I) cumprimento forçado nos termos da oferta; (II) aceitar outro
produto/serviço equivalente; (III) rescindir o contrato, com restituição do valor pago,
atualizado, e perdas e danos.

## Vinculação da oferta e erro de preço
Art. 30: toda informação/publicidade suficientemente precisa **integra o contrato** e vincula o
fornecedor. Art. 35 dá ao consumidor as três alternativas acima quando o fornecedor recusa cumprir
o preço anunciado.

**Dual — quando o fornecedor sustenta erro grosseiro:** a defesa de que o preço era manifestamente
irreal (erro de digitação, zero a menos, etc.) é construção doutrinária e jurisprudencial, não
texto expresso do CDC — `[VERIFICAR — número de precedente não confirmado no corpus]` antes de
citar um caso específico. A força da tese depende de o erro ser **objetivamente perceptível** por
qualquer consumidor médio (ex.: produto a 1% do valor de mercado) — erro de precificação dentro de
faixa plausível não afasta a vinculação do art. 30.

## Tese do consumidor
Art. 30 vincula a oferta; o exercício do arrependimento no prazo do art. 49 não exige motivo,
apenas manifestação dentro dos 7 dias; atraso/não entrega abre as três alternativas do art. 35,
inclusive rescisão com perdas e danos.

## Tese do fornecedor
Provar que a informação de preço/oferta continha erro manifesto e objetivamente perceptível (não
apenas alegar "erro" a posteriori); demonstrar cumprimento das obrigações de informação do art. 2º
do Decreto 7.962/2013 para afastar alegação de vício de informação; comprovar que a comunicação do
arrependimento chegou fora do prazo de 7 dias.

## Armadilhas
T13 — o Decreto 7.962/2013 tem quebras de linha no meio de frases no HTML capturado do Planalto;
normalizar espaço em branco antes de comparar citação literal com o anexo, sob pena de falso
negativo em grep.

## Fronteira
Responsabilidade de marketplace/plataforma por vendedor terceiro →
`marketplace-e-plataforma`. Estorno/fraude de cartão de crédito de origem bancária →
`bancario-adv-os`. Cobrança pura, título e execução → `execucao-adv-os`.
