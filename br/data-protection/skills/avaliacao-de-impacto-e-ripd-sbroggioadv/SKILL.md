---
name: avaliacao-de-impacto-e-ripd-sbroggioadv
title: Avaliação de impacto e RIPD
description: Estrutura avaliação de impacto e RIPD para solução de IA em serventia, documentando tratamento de dados, necessidade, proporcionalidade, decisões automatizadas, riscos, salvaguardas, incidentes e revisão humana. Esta skill deve ser usada quando o pedido mencionar avaliação de impacto, RIPD, impacto algorítmico, dados pessoais em IA, decisão automatizada, LGPD, alto risco, relatório técnico, titular de dados ou contratação de solução de IA.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/avaliacao-de-impacto-e-ripd
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Avaliação de impacto e RIPD

> Camada C6. Diferenciar avaliação de impacto no tratamento de dados, RIPD da LGPD e referência de impacto algorítmico do Judiciário.

## Anexos e skills obrigatórios

- `context/ia-por-uf.md` — obrigações e limites estaduais;
- `context/prov-cnj-213-2026-e-anexos.md` — piso federal de tratamento e segurança;
- `context/res-cnj-615-2025-recorte-dados.md` — referência não diretamente vinculante;
- `context/travas-defasagem.md` — escopo e endereços;
- `analise-previa-de-risco-de-solucao-de-ia`, `regime-de-ia-da-uf` e `qualificacao-notarial-transversal`.

## Endereço normativo correto

No MT, produzir a avaliação antes de contratar ou utilizar, pelo Provimento 1/2026-GAB-CGJ, art. 7º, II, acompanhada de verificação de conformidade e relatório técnico sucinto dos incisos III e IV. Não citar “Prov. CNJ 213/2026, art. 7º, II”: esse inciso não existe; o art. 7º federal estabelece deveres gerais de LGPD.

No MA, exigir relatório de impacto para sistemas com decisões automatizadas de efeitos jurídicos relevantes, conforme art. 172, V. Preservar que nenhuma decisão automatizada substitui análise humana em manifestação de vontade ou validação jurídica. No AM, mapear riscos e impactos no inventário e na governança, sem dizer que a auditoria semestral da CGJ é um RIPD produzido pela serventia. No PI, aplicar LGPD e validação de eficácia e segurança sem inventar dispositivo local nominando RIPD.

Nas outras 23 UFs, classificar o documento conforme sua base federal e necessidade concreta, ou como boa prática antecipatória; não atribuir obrigação estadual inexistente. A Resolução CNJ 615/2025 rege o Judiciário e só chega à serventia por remissão ou como referência voluntária.

## Gate de admissibilidade

Executar primeiro `regime-de-ia-da-uf`. Interromper a avaliação como rota de aprovação se a função for proibida ou, no AM, se faltar homologação prévia comprovada. Um RIPD favorável não cura proibição normativa.

## Estrutura mínima do documento

1. identificar controlador, operadores por função, solução, versão e finalidade;
2. descrever operações, fontes, categorias, titulares, volume, frequência, fluxos e destinos;
3. registrar base jurídica, necessidade, adequação, proporcionalidade e minimização;
4. separar dados administrativos do acervo dotado de fé pública;
5. identificar decisões automatizadas, efeitos, contestação e revisão humana;
6. avaliar confidencialidade, integridade, disponibilidade, autenticidade e rastreabilidade;
7. verificar retenção, treinamento, inferências, compartilhamentos e transferências;
8. documentar riscos a titulares, fé pública, não discriminação e continuidade;
9. associar salvaguardas, responsáveis, prazos e evidências;
10. indicar risco residual, consulta necessária e ciclo de revisão.

Não inserir no artefato dados reais de partes, prompts, documentos ou resultados do acervo. Usar categorias e fluxos abstratos.

## Relação com o relatório técnico do MT

Anexar conclusão sucinta que indique finalidade, arquitetura de segurança, conformidade verificada, limitações, controles, risco residual e decisão humana. Manter separadas:

- análise de risco do art. 7º, I;
- avaliação de impacto do inciso II;
- verificação de conformidade do inciso III;
- relatório técnico do inciso IV.

Não condensar os quatro gates em uma declaração genérica.

## Saída

Entregar RIPD versionado, matriz de tratamentos, impactos e salvaguardas, parecer de admissibilidade, relatório técnico sucinto quando MT, pendências, responsáveis e data de revisão. Marcar o documento como preliminar sob revisão humana e jurídica.

## Reprovação automática

- inventar inciso II no art. 7º do Provimento 213;
- usar RIPD para autorizar função proibida;
- tratar auditoria da CGJ/AM como documento da serventia;
- aplicar MA art. 172, V sem efeito jurídico relevante;
- chamar a Resolução 615 de norma direta do cartório;
- omitir inferências, saídas ou acesso do fornecedor;
- incluir PII ou conteúdo de acervo;
- afirmar que o relatório substitui parecer.
