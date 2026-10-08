---
name: analise-previa-de-risco-de-solucao-de-ia-sbroggioadv
title: Análise prévia de risco de solução de IA
description: Produz análise prévia de risco de solução de IA antes da contratação ou uso, confrontando finalidade, regime da UF, dados, fornecedor, arquitetura, supervisão, logs, incidentes e reversibilidade. Esta skill deve ser usada quando o pedido mencionar análise de risco de IA, contratar ferramenta, validar fornecedor, piloto de IA, mapa de riscos, uso permitido, dados do acervo, anonimização, risco à fé pública ou dossiê para a Corregedoria.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/analise-previa-de-risco-de-solucao-de-ia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# Análise prévia de risco de solução de IA

> Camada C6. Analisar antes de contratar ou utilizar. A análise organiza decisão humana; não autoriza função proibida.

## Anexos e skills obrigatórios

- `context/ia-por-uf.md` — permissões, proibições e contradições estaduais;
- `context/prov-cnj-213-2026-e-anexos.md` — piso federal de segurança, acervo e continuidade;
- `context/res-cnj-615-2025-recorte-dados.md` — referência indireta quando houver remissão;
- `context/travas-defasagem.md` — endereços e lacunas;
- `regime-de-ia-da-uf`, `diagnostico-de-conformidade-de-ia` e `clausulas-contratuais-de-fornecedor-de-ia`.

## Endereço normativo correto

No MT, exigir análise de risco **antes da contratação ou utilização** pelo Provimento 1/2026-GAB-CGJ, art. 7º, I. Não atribuir esse inciso ao Provimento CN 213/2026: seu art. 7º não possui incisos I e II e estabelece o piso federal de conformidade com a LGPD, registro das operações, encarregado quando aplicável e comunicação de incidentes.

No AM, integrar a análise ao inventário do art. 165, com solução, fabricante, versão, fornecedor, fluxo completo dos dados, controles e riscos, atualizado semestralmente. No MA, aplicar os arts. 172, 176 e 177 aos riscos de dados, auditabilidade e mitigação. No PI, documentar a validação periódica de eficácia e segurança do art. 103, II, sem inventar uma análise prévia nominada.

Nas outras 23 UFs, tratar o artefato como boa prática antecipatória apoiada no piso federal, não como obrigação estadual de IA. A Resolução 615/2025 não vincula a serventia por força própria.

## Entradas mínimas

Coletar sem dados pessoais de caso:

- UF, classe, situação da delegação e data;
- solução, versão, fabricante, fornecedor e modelo de contratação;
- finalidade e função concreta;
- origem, natureza, categoria, destino e fluxo dos dados;
- retenção, treinamento, compartilhamento e acesso do fornecedor;
- arquitetura local, externa, nuvem ou híbrida;
- usuários, supervisão e decisão humana;
- logs, auditoria, resposta a incidentes, reversibilidade e portabilidade.

Bloquear a conclusão se a finalidade estiver vaga, o fluxo de dados for desconhecido ou o fornecedor não provar as condições contratuais.

## Teste de admissibilidade antes da pontuação

1. Rotear a UF.
2. Comparar a função com o rol permitido e as vedações locais.
3. Bloquear função proibida sem tentar compensá-la com controle técnico.
4. No AM, bloquear solução sem homologação prévia comprovada.
5. No MT, bloquear qualificação, interpretação, enquadramento, sugestão decisória, treinamento com acervo e processamento externo de dados não anonimizados.
6. No MA, limitar aos cinco usos do art. 171 e exigir cumulativamente as condições do fornecedor.

Somente avaliar risco residual depois de superar o gate jurídico. Risco baixo não transforma uso proibido em permitido.

## Matriz de risco

Classificar e justificar, com evidência:

| Eixo | Pergunta de controle |
|---|---|
| função e fé pública | a ferramenta cria aparência de ato ou influencia decisão reservada? |
| dados | há minimização, base, anonimização e segregação comprováveis? |
| treinamento e retenção | entradas, saídas ou inferências alimentam modelo ou permanecem no fornecedor? |
| fornecedor | há auditabilidade, suporte, histórico e conformidade documentada? |
| segurança | criptografia, acesso, logs e resposta a incidentes atendem à classe? |
| supervisão | existe revisão humana integral e responsável identificado? |
| continuidade | RPO, RTO, backup e restauração são demonstráveis? |
| saída | portabilidade integral e reversibilidade independem da anuência do fornecedor? |
| vieses e erros | há teste, contestação, correção e rastreabilidade? |

Registrar probabilidade, impacto, evidência, controle, risco residual, responsável e decisão. Não gerar escore sem explicar a escala nem substituir decisão do titular.

## Artefato de saída

Entregar identificação da solução e versão, regime aplicável, usos permitidos/proibidos, mapa de dados, matriz de riscos, controles exigidos, risco residual, lacunas, decisão humana `aprovar | aprovar com condições | rejeitar | bloqueado` e data de revisão. No AM, incluir a atualização semestral do inventário.

## Reprovação automática

- citar “Prov. CNJ 213, art. 7º, I”;
- analisar depois da contratação no MT;
- pontuar risco antes de testar legalidade do uso;
- autorizar função proibida por ter risco baixo;
- omitir versão ou fluxo de dados no AM;
- tratar a Resolução 615 como vínculo direto;
- usar dados reais do acervo no teste;
- declarar certificado de conformidade.
