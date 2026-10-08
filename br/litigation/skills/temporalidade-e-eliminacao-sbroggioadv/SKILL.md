---
name: temporalidade-e-eliminacao-sbroggioadv
title: Temporalidade e eliminação
description: Aplica a Tabela de Temporalidade do Provimento CNJ 50/2015, a alteração do Provimento 185/2024 e os controles de eliminação, distinguindo guarda permanente, prazo cumprido e digitalização com valor legal. Esta skill deve ser usada quando o pedido mencionar descarte, inutilização, incineração, retenção, guarda, livro, firma, DOI, documentos de escritura ou redução de arquivo físico.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/temporalidade-e-eliminacao
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Temporalidade e eliminação

## Três invioláveis

1. Nada do acervo sai sem anonimização irreversível prévia.
2. Nada alimenta treinamento: nem entrada, nem saída, nem dado inferido.
3. Nada produzido pelo plugin é ato notarial ou registral nem pode parecer ato dotado de fé pública.

Aplicar **IMUTABILIDADE, RASTREABILIDADE e RETENÇÃO MÍNIMA** em toda automação. Base normativa atualizada até 25/08/2026.

Tratar o acervo como patrimônio funcional **do serviço**, não do titular; tudo que esta skill gerar deve ser extraível em formato não proprietário, sem anuência de fornecedor. Separar a camada administrativa da camada de fé pública: nesta última, leitura autorizada pode ocorrer, mas saída com aparência de ato nunca.

## Anexos e skills obrigatórios

- `context/prov-cnj-50-2015-temporalidade-notas.md` — tabela compilada e descarte;
- `context/decreto-10278-2020.md` — digitalização com valor legal;
- `context/travas-defasagem.md` — travas T-110 a T-113;
- `conformidade-de-digitalizacao`, `plano-de-metadados` e `diagnostico-do-acervo`.

## Regra absoluta

**Livro de notas não se elimina, nem digitalizado.** A Tabela de Temporalidade do Provimento CNJ 50/2015, classe 3-5-1, atribui guarda permanente ao protocolo de livros, testamentos públicos, aprovações de testamentos cerrados, livros de escrituras, livros de procurações e substabelecimentos, índices e demais livros auxiliares; o CNN art. 196 manda adotar essa tabela.

## Tabela operacional de Notas

- **Permanente:** todos os livros e índices acima.
- **10 anos:** certidões de distribuidores, interdições e tutelas; controles de distribuição; outros documentos que instruíram escritura ou procuração.
- **5 anos:** comprovante de emissão de DOI.
- **5 anos, condicionados à digitalização com valor legal:** depósitos de firmas, reconhecimentos de firma por autenticidade e fichas de depósito, após a alteração do Provimento CNJ 185/2024.

Não usar o triênio civil do art. 22 da Lei 8.935/1994 como prazo de guarda. A tabela conserva por dez anos os documentos instrutórios que podem constituir prova da qualificação.

## Fluxo de eliminação

1. Identificar espécie, código da tabela, suporte e termo inicial.
2. Confirmar que o prazo venceu e que não existe litígio, investigação, preservação, incidente ou regra especial.
3. Validar a digitalização com valor legal quando ela for condição do descarte.
4. Confirmar que o item não pertence a livro ou classe permanente.
5. Aprovar lista e evidência por responsável competente.
6. Comunicar a eliminação **semestralmente ao juízo competente**, conforme art. 3º do Provimento 50.
7. Desfigurar ou destruir de forma que informação, identidade e assinatura não possam ser recuperadas.
8. Registrar lote, fundamento, data, método, responsáveis e prova da destruição.

Eliminar o papel não elimina os deveres da LGPD sobre índices, classificadores, banco de dados, cópias de segurança e outros resíduos. Tratar a camada administrativa e a de fé pública separadamente.

## Limites

- Não criar política de retenção de backup: o Provimento CNJ 213/2026 não fixa retenção do backup em si.
- Não eliminar em massa por idade aparente, nome de pasta ou espaço disponível.
- Não antecipar prazo por mudança de titular; o acervo continua pertencendo ao serviço e deve ser transferido ao sucessor.
- Não terceirizar destruição sem cadeia de custódia e prova de irreversibilidade.

## Saída

Entregar tabela item a item com classe, fundamento, termo inicial, prazo, digitalização, bloqueios, decisão, comunicação, destruição e resíduos LGPD. Separar “manter”, “eliminável após condição”, “eliminável agora” e “não identificado”.

## Reprovação automática

- eliminar livro de notas ou índice permanente;
- equiparar digitalização a autorização automática de descarte;
- aplicar três anos a documentos instrutórios;
- esquecer a comunicação semestral;
- permitir reconstrução de dados eliminados;
- declarar prazo de retenção do backup que a norma não fixou.
