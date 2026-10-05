---
name: acordo-patrimonial-do-divorcio-sbroggioadv
title: Acordo patrimonial do divórcio
description: Organiza, pelo advogado dos interessados, proposta patrimonial consensual do divórcio extrajudicial, separando bens particulares, meação e transferências. Esta skill deve ser usada quando o advogado mencionar regime de bens, sub-rogação, partilha desigual, excesso de meação ou tributo sobre fração transferida no divórcio em cartório. Não homologa cálculo fiscal nem resolve disputa patrimonial.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/familia-extrajudicial-os-marketplace/tree/main/familia-extrajudicial-os/skills/acordo-patrimonial-do-divorcio
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: family
language: pt
---

# Acordo patrimonial do divórcio

Atuar como apoio ao advogado dos interessados, demonstrando premissas e proposta patrimonial para revisão humana. Não decidir partilha litigiosa, qualificar título pelo delegatário ou homologar tributo.

## Acionamento e âncoras

Usar para acordo patrimonial vinculado ao divórcio consensual; identificar antes ator, casamento e objeto. Inventário, planejamento patrimonial autônomo, litígio e atuação como tabelião são `FORA DO RECORTE`. Não transformar diferença entre vontades das partes em consenso presumido.

Ler o texto literal e os metadados de:

- `context/res-cnj-35-compilada.md`: arts. 37–39; art. 15 somente para distinguir o inventário.
- `context/cc-familia-sucessoes.md`: art. 1.581 e arts. 1.658–1.659, preservando as exceções e o contexto do bloco capturado de comunhão parcial.
- `context/lc-227-2026-itcmd.md`: art. 147, I e VI, c, e art. 151, II, f, nos limites do ITCMD e das premissas civis comprovadas.

Não aplicar comunhão parcial a todo regime; outro regime depende de seus dispositivos efetivamente capturados e validados. Conferir versão, datas relevantes, corte documental, alcance e UF com o validador. Fonte ausente/inacessível bloqueia a classificação ou afirmação dependente, mantendo possível o inventário documental. Não citar norma estadual, precedente ou regra por memória.

## Entrada

Receber interessado assistido, partes, consenso, capacidade, UF(s), datas, modalidade e pasta privada. Reunir casamento, regime comprovado, pacto se houver, títulos de aquisição, origem e data de cada bem, eventual doação/sucessão/sub-rogação, titularidade, dívidas/ônus documentados, valores com fonte/data, divisão desejada e eventual contraprestação. Não inventar preço, avaliação ou quitação.

Conferir previamente `filhos-e-condicoes-do-divorcio`: sua pendência impeditiva ou gravidez/nascituro não pode ser superada por um acordo patrimonial. Podem ser organizados os documentos dos bens, mas não produzida proposta especializada ou minuta de apresentação antes das condições familiares e da análise humana exigível.

## Procedimento

1. Montar tabela `bem/direito → título/arquivo/trecho → origem/data → regime → classificação proposta → fração civil/premissa → valor/fonte/data → atribuição pretendida → diferença → contraprestação → pendência`. Separar fatos documentados, relato e inferência jurídica.
2. Aplicar R35 37: distinguir patrimônio individual e comum segundo o regime. Na comunhão parcial, CC 1.658 tem exceções; conferir CC 1.659 por inciso. Não chamar bem anterior, doação/sucessão individual ou sub-rogação exclusivamente particular de bem comum só por estar com o casal. Não inferir origem particular apenas do nome no título; considerar o contexto civil capturado, sem ampliar a regra além do suporte.
3. Demonstrar fração civil devida e atribuição por parte com premissas rastreáveis. Somar apenas valores comparáveis e comprovados; registrar moeda, data e origem. Sem prova de valor ou natureza do bem, não emitir excesso definitivo. Título disputado ou regime incerto impede conclusão específica e proposta de partilha dependente.
4. Separar meação de transferência de patrimônio individual e excesso de atribuição. Comparar fração devida com atribuição pretendida antes de qualificar o efeito tributário. A conclusão de que uma atribuição limitada à fração civil não envolve transferência adicional é inferência do caso, não transcrição da LC227 nem isenção fiscal geral.
5. R35 38 exige comprovação do recolhimento do tributo devido sobre a fração transferida quando há transmissão do patrimônio individual ao outro cônjuge ou partilha desigual do comum. Sem prova necessária, identificar pendência tributária e bloquear a minuta de apresentação da partilha; não declarar recolhimento ou isenção sem documento/fundamento. A dispensa de prova prévia de ITCMD do art. 15 é de inventário/partilha e não afasta a regra específica do divórcio no art. 38.
6. Distinguir qualificação gratuita/onerosa e suas provas. LC227 147 define excesso e inclui excessos na disciplina da doação; art. 151, II, f delimita o fato gerador do excesso na escritura extrajudicial. Não chamar toda diferença automaticamente de ITCMD, nem todo patrimônio de base tributável. Contraprestação real/documentada exige qualificação fiscal específica; não afirmar ITBI ou isenção por analogia. Encaminhar a `itcmd-como-efeito-do-ato` com as premissas e a `lacunas-estaduais-do-procedimento` para a dependência local.
7. Sem norma oficial da UF aplicável e validada, não calcular valor tributário final, alíquota, vencimento, multa, formulário ou isenção. Entregar somente quadro federal identificado e pendências locais. A administração fiscal decide suas competências; não produzir homologação.
8. R35 39 remete às regras de partilha em inventário apenas no que couber; não importar MP, testamento ou dispensa tributária universal. CC 1.581 admite divórcio sem prévia partilha: registrar partilha diferida como opção submetida ao advogado, distinguindo o vínculo de patrimônio ainda não resolvido. Não produzir acordo patrimonial fictício nem petição judicial para sanar dissenso.

## Saída e limites

Entregar ato/ator/UF(s)/datas/modalidade, fontes/corte, documentos recebidos/faltantes, matriz `requisito → prova → arquivo/trecho → responsável → situação`, tabela dos bens, demonstrativo verificável de frações/atribuições, proposta patrimonial apenas quando permitida, efeitos tributários qualificados e próxima providência com impedimento.

Usar `PREPARAÇÃO CONDICIONADA À REVISÃO HUMANA`, `PENDENTE DE PROVA`, `BLOQUEADO` ou `FORA DO RECORTE`. Lacuna impeditiva entrega mapa documental, sem minuta de apresentação; não dizer “partilha aprovada” ou “apto à lavratura”. Encaminhar proposta permitida a `preparacao-de-divorcio-extrajudicial` e `requerimento-e-minuta-de-proposta-familiar`. Registros, recolhimentos, assinaturas e escritura são atos externos: não fabricá-los.

Preservar sigilo, dados mínimos e armazenamento privado separado por cliente/matéria; não gravar dossiê no source nem transmitir automaticamente a serviço externo.

## Revisão final obrigatória

Executar ao final, inclusive no acionamento direto e em pendências:

1. `anti-alucinacao-familia-extrajudicial`: conferir fatos, valores, cálculos e provas das transferências/pagamentos; remover ou bloquear afirmações sem suporte.
2. `validador-familia-extrajudicial`: conferir redação, vigência, alcance civil/fiscal, UF e distinção arts. 15/38; manter lacunas explícitas.
3. `suprema-corte-familia-extrajudicial`, default-on: R1 fatos/provas/consenso/ator → R2 fundamentos/vigência/tensões → R3 documentos/cálculos/UF/condições externas → R4 postura/sigilo/fronteira/encaminhamento.

Registrar achados por rodada e repetir a cadeia sobre correções. Controle indisponível ou pedido de ignorar bloqueio impede entrega especializada; manter pendências com controle faltante identificado. Não declarar teste jurídico ou revisão executados pela simples existência desta instrução. Guidance only: orientação ao agente, sem enforcement por hook nem garantia fiscal/notarial.
