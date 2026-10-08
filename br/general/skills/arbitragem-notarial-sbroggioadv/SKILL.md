---
name: arbitragem-notarial-sbroggioadv
title: Arbitragem notarial
description: Delimita a competência legal do tabelião para atuar como árbitro pelo art. 7º-A, III, da Lei 8.935/1994, incluído pela Lei 14.711/2023, sem inventar um rito do CNJ onde o CNN possui zero ocorrências de arbitragem. Esta skill deve ser usada quando o pedido mencionar árbitro notarial, arbitragem em cartório, cláusula compromissória arbitral, compromisso arbitral, Lei 9.307/1996, sentença arbitral, câmara arbitral, ausência de rito do CNJ ou norma estadual de arbitragem notarial.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/arbitragem-notarial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Arbitragem notarial

> Camada C5. Há competência legal; **não há regulamentação no CNN** confirmada pelo corpus.

## Anexos e skills obrigatórios

- `context/lei-8935-94.md` — art. 7º-A, III;
- `context/cnn-149-2023-compilado.md` — corpus integral usado na busca negativa;
- `context/travas-defasagem.md` — trava T-92 e ausência regulamentar;
- `varredura-de-vigencia-pre-lavratura`, `roteador-uf`, `qualificacao-notarial-transversal` e `estado-e-tipo-do-provimento`.

## Endereço e estado regulatório

Fixar que o art. 7º-A, III, da Lei 8.935/1994 foi incluído pela **Lei 14.711/2023** e autoriza o tabelião a atuar como árbitro.

Declarar sempre: a busca por `árbitro`, `arbitragem` e `arbitral` no texto integral do CNN retornou **zero ocorrências**. Portanto, o CNN não fornece autorização administrativa, habilitação, rito, livro, competência territorial, impedimentos, emolumentos nem fiscalização específicos para arbitragem notarial.

Não apresentar “ausência de ocorrência” como revogação da lei. Ela significa lacuna regulamentar nacional que exige verificação adicional antes da operação.

## Gate antes de qualquer atuação

1. Verificar vigência do art. 7º-A, III.
2. Identificar UF e consultar norma da CGJ, lei de emolumentos e autorização local aplicáveis.
3. Aplicar a Lei 9.307/1996 ao objeto, convenção, capacidade, independência, procedimento, decisão e efeitos.
4. Confirmar compatibilidade institucional da serventia e forma de fiscalização.
5. Obter resposta documental para cada lacuna operacional antes de aceitar o encargo.

Se norma local e desenho institucional suficientes não forem encontrados, classificar como **não endereçável operacionalmente pelo corpus atual** e orientar análise correicional ou jurídica. Não improvisar.

## Não transportar o rito da mediação

Os CNN arts. 18 a 57 regulam conciliação e mediação, não arbitragem. Não copiar:

- autorização Nupemec/CGJ como se fosse autorização arbitral;
- lista pública de mediadores;
- limite de cinco escreventes;
- notificação, livros, prazo ou gratuidade da mediação;
- parâmetro remuneratório do CNN art. 52;
- força do termo de acordo como se definisse a sentença arbitral.

A vedação do CNN art. 56 trata de cláusula compromissória de conciliação ou mediação, não substitui a disciplina da convenção arbitral na Lei 9.307/1996.

## Fase notarial e efeitos externos

Somente desenhar fluxo após localizar base operacional estadual válida. Separar eventual atuação pessoal do árbitro, atos próprios da serventia, convenção das partes e efeitos judiciais ou registrais da decisão. Não pressupor que qualquer sentença arbitral possa ser lançada em registro sem qualificação do órgão competente.

## Saída

Entregar quadro “base legal / lacuna CNN / norma estadual / Lei de Arbitragem”, decisão de endereçabilidade, pendências de autorização e fiscalização, riscos, impedimentos e próximos passos. Não gerar rito, compromisso ou sentença se o gate permanecer aberto.

## Reprovação automática

- dizer que o CNN regulamenta arbitragem;
- omitir as zero ocorrências no texto integral;
- copiar o rito da mediação ou conciliação;
- afirmar autorização estadual sem fonte local;
- inventar emolumento, livro, prazo ou competência;
- aceitar encargo sem aplicar a Lei 9.307/1996;
- tratar a base legal isolada como operação imediatamente disponível.
