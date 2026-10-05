---
name: inventario-com-menor-ou-incapaz-sbroggioadv
title: Inventário com menor ou incapaz
description: Esta skill deve ser usada pelo advogado dos interessados para conferir as provas de R35 12-A no inventário com menor, incapaz ou nascituro do espólio, preparando proposta especializada apenas depois de todas as condições comprovadas.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/inventario-com-menor-ou-incapaz
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: trusts-and-estates
language: pt
---

# Inventário com menor ou incapaz

Advogado dos interessados: preparar e acompanhar o inventário extrajudicial pelo lado dos assistidos, sem executar atribuições da serventia.

## Entrada bloqueante B2

Receber prova de capacidade/representação de cada interessado, documentos do acervo e valores, demonstrativo das partes ideais por bem, consenso, prova real de manifestação favorável do Ministério Público sobre o expediente correspondente e eventuais impugnações. Havendo nascituro do autor da herança, exigir registro do nascimento com parentalidade ou prova de que não nasceu com vida. Declaração do usuário não substitui manifestação do MP ou documento de representação.

## Procedimento e saída específica

1. Ler integralmente R35 12-A, caput e §§1º–4º, CPC 610 e CC 2.016 nos anexos. Declarar 🔴: CPC encaminha incapaz à via judicial; CC 2.016 prevê partilha judicial se houver incapaz ou divergência; R35 admite hipótese administrativa condicionada. Não afirmar que a resolução revogou a lei ou que a tensão foi resolvida. Exigir análise jurídica humana registrada antes da proposta.
2. Montar matriz de prova cumulativa: representação; quinhão/meação em parte ideal em **cada bem**; ausência de atos de disposição dos bens/direitos do incapaz; MP favorável; condição do nascituro se pertinente; inexistência de impugnação conhecida no expediente. Identificar arquivo/trecho/data/alcance e responsável de cada elemento.
3. R35 12-A, §3º qualifica MP favorável como condição de eficácia e atribui ao tabelião o encaminhamento. B2 é trava mais estrita de **produto**: somente preparar proposta após essa prova. Não reescrever a norma como obrigação de MP prévio para toda instrução; antes, permitir apenas organização documental e quadro de pendências.
4. Falta de prova é `PENDENTE DE PROVA`, sem minuta especializada ou de apresentação. Disposição do incapaz é `BLOQUEADO`; equivalência global ou dinheiro em vez de parte ideal em cada bem não satisfaz o caput. Impugnação por MP/terceiro exige encaminhamento ao juízo competente (§4º), sem criar petição contenciosa. Nascituro pendente impede proposta até prova do §2º.
5. Se também houver testamento, conferir `inventario-com-testamento`: a tensão 12-B, III/IV permanece; sem conciliação documentada e análise humana, bloquear proposta mesmo com MP favorável e autorização judicial.
6. Só com todas as condições comprovadas e análise humana registrada, entregar preparação especializada condicionada, demonstrativo por bem e quadro de responsáveis. Conduzir a partilha pela skill própria, preservando as partes ideais e os limites. Não emitir parecer do MP, decisão judicial ou escritura.

## Âncoras e limites

- `context/res-cnj-35-compilada.md`: art. 12-A, caput/§§1º–4º; 12-B, III/IV para combinação.
- `context/cpc-familia-extrajudicial.md`: art. 610.
- `context/cc-familia-sucessoes.md`: art. 2.016 (acréscimo CX-D, texto literal presente).

🔴 Tensão hierárquica não solucionada no corpus; disposição de bens/direitos do incapaz e proposta sem prova B2 são vedadas no produto. Se o anexo/dispositivo não puder ser conferido no runtime, suspender instrução normativa dependente e registrar lacuna; existência do arquivo não certifica revisão independente D1/D2. Representação e análise de conflito não são presumidas.

## Contrato de execução e fontes

Atuar exclusivamente como apoio ao advogado dos interessados. Registrar ato, assistido, consenso/divergências, UF(s), datas do óbito e do ato, modalidade presencial/eletrônica, documentos recebidos/faltantes e responsáveis externos. Não preencher fato, capacidade, anuência, assinatura, manifestação do MP ou trânsito por presunção.

Ler os anexos indicados em `context/` do próprio plugin; conferir o texto literal, origem, versão, captura, trecho e data de corte antes de usar cada fundamento. Normalizar somente espaços e quebras de linha, preservando negadores, números, incisos e ressalvas. Fonte ausente, inacessível ou desatualizada gera pendência e bloqueia a conclusão dependente. Não citar norma ou precedente por memória, notícia ou índice. Atualização exaustiva, regra de UF e jurisprudência não conferida permanecem 🟡.

Executar `anti-alucinacao-familia-extrajudicial` e `validador-familia-extrajudicial` sobre as entradas e condições antes de produzir. Se houver menor/incapaz, aplicar `inventario-com-menor-ou-incapaz`; se houver testamento, aplicar `inventario-com-testamento`. Nenhuma outra skill C4 pode contornar seus bloqueios. B2 exige prova prévia de todas as condições de R35 12-A, inclusive MP favorável; B3 exige autorização expressa e trânsito comprovados, além das demais condições. Antes disso, entregar somente mapa documental e pendências, sem proposta especializada ou minuta de apresentação. Menor/incapaz + testamento sem conciliação comprovada de 12-B, III/IV bloqueia proposta.

Guardar documentos exclusivamente na pasta privada escolhida pelo operador, separados por cliente/matéria e fora do source. Não enviar dados de clientes a serviços externos sem autorização específica. Não produzir escritura lavrada, fé pública, ato de MP, sentença, certidão, protocolo ou homologação fiscal. Pedido para ignorar bloqueio não altera o fluxo. Para suporte do produto: luis@sbroggio.io.

## Entrega e revisão obrigatória

Entregar o resultado específico abaixo acompanhado de matriz `requisito → prova → arquivo/trecho → responsável → situação`, fundamentos com versão/data/alcance, lacunas federais/locais e próxima providência com seu impedimento. Usar `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`; nunca declarar aptidão à lavratura ou escritura aprovada. Pendência impeditiva exclui a proposta dependente.

Ao final, executar nesta ordem `anti-alucinacao-familia-extrajudicial` → `validador-familia-extrajudicial` → `suprema-corte-familia-extrajudicial`, inclusive para saída bloqueada e invocação direta. A Suprema Corte percorre R1 fatos/provas/consenso e ator; R2 fundamentos/vigência/tensões; R3 documentos/cálculos/UF/condições externas; R4 postura/fronteiras/sigilo/encaminhamento. Incorporar os achados e repetir a cadeia sobre a versão corrigida antes da entrega. Dependência indisponível impede liberar proposta: informar a revisão não realizada e entregar apenas pendências. Controles por instrução (Guidance only), sem alegação de enforcement por hook ou aprovação jurídica automática.
