---
name: clausulas-contratuais-de-fornecedor-de-ia-sbroggioadv
title: Cláusulas contratuais de fornecedor de IA
description: Gera checklist de cláusulas mínimas e lacunas de contrato com fornecedor de IA, combinando o núcleo de cinco cláusulas do MT, as quatro exigências do PI, os requisitos cumulativos do MA, CNN arts. 86-87 e reversibilidade do Provimento 213/2026. Esta skill deve ser usada quando o pedido mencionar contrato de IA, fornecedor, SaaS, não treinamento, retenção de inputs e outputs, LGPD, auditoria, privacy by design, território nacional, banco da serventia, reversibilidade ou portabilidade.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/clausulas-contratuais-de-fornecedor-de-ia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Cláusulas contratuais de fornecedor de IA

> Camada C6. Produzir checklist e minuta preliminar; não certificar fornecedor nem presumir que contrato cura arquitetura inadequada.

## Anexos e skills obrigatórios

- `context/ia-por-uf.md` — sobreposições e contradições estaduais;
- `context/prov-cnj-213-2026-e-anexos.md` — interoperabilidade, autonomia, reversibilidade e portabilidade;
- `context/cnn-149-2023-compilado.md` — CNN arts. 86-87;
- `context/travas-defasagem.md` — remissão morta e lacunas;
- `regime-de-ia-da-uf`, `analise-previa-de-risco-de-solucao-de-ia` e `diagnostico-de-conformidade-de-ia`.

## Entradas bloqueantes

Confirmar UF, classe, situação da delegação, solução e versão, finalidade, fornecedor, suboperadores, arquitetura, localização de desenvolvimento e armazenamento, fluxos de entrada e saída, retenção, treinamento, acesso, incidentes, término e formato de exportação. Não aceitar resposta comercial sem evidência contratual e técnica.

## Núcleo de cinco cláusulas — MT art. 8º

Conferir, separadamente:

1. proibição de usar dados da serventia para treinamento de modelos;
2. não retenção, não compartilhamento e não armazenamento de entradas e saídas;
3. conformidade com a LGPD e com a norma federal vigente de TIC;
4. mecanismos de auditoria;
5. política de privacidade clara com proteção desde a concepção e por padrão.

Corrigir a remissão estadual desatualizada ao Provimento CNJ 74/2018, revogado: reconduzir materialmente ao Provimento CN 213/2026 e alterações. Não reescrever o texto histórico como se ele já trouxesse a correção.

## Sobreposição do PI — art. 108

Exigir também: limitação do uso ao escopo contratado; proibição de compartilhamento com terceiro sem consentimento expresso; medidas técnicas e administrativas contra acesso, destruição, perda, alteração, comunicação ou tratamento indevido; notificação imediata de violação de dados.

Não substituir essas quatro cláusulas pelo núcleo do MT. Registrar correspondências e lacunas uma a uma.

## Requisitos cumulativos do MA — arts. 173-174

Antes da minuta, verificar todos os sete requisitos do fornecedor: desenvolvimento ou armazenamento exclusivamente no Brasil; segurança, inclusive referência ISO 27001, e LGPD; confidencialidade e não compartilhamento; banco integral no servidor da serventia; pertencimento integral do banco à serventia e transferência segura no término; auditoria técnica pela COGEX; uso limitado ao escopo.

Incluir no contrato: confidencialidade e proteção integral; notificação imediata de incidente ou desconformidade; medidas corretivas; transferência integral do controle do sistema e banco de dados ao cartório no encerramento. Um SaaS admissível no PI pode ser vedado no MA.

## Piso federal

Aplicar CNN arts. 86-87 à revisão contratual e à exigência de adequação do fornecedor à LGPD. Pelo Provimento 213/2026, exigir interoperabilidade, mitigação de dependência exclusiva, reversibilidade e extração integral, autônoma e documentada dos dados, configurações e registros em formato interoperável e não proprietário, sem anuência do fornecedor.

Exigir evidência prática de portabilidade; cláusula sem teste não prova autonomia estrutural. Não fixar retenção do backup, ausente na norma.

## Honestidade territorial

Aplicar exigências estaduais somente em PI, MT, MA ou AM e na UF correta. Nas outras 23 UFs, aplicar o piso federal e marcar o restante como boa prática contratual. A Resolução 615/2025 não vincula diretamente a serventia.

## Saída

Entregar tabela `cláusula | dispositivo | texto existente | lacuna | evidência | ação`, checklist por UF, cláusulas preliminares, matriz de suboperadores, plano de saída e teste de portabilidade. Submeter a minuta à revisão jurídica e técnica antes da assinatura.

## Reprovação automática

- reduzir o núcleo do MT a menos de cinco cláusulas;
- repetir o Provimento 74/2018 como vigente;
- omitir entradas, saídas ou dados inferidos;
- abrir exceção de treinamento por revisão humana;
- transportar território nacional e banco local do MA ao PI;
- aceitar portabilidade dependente do fornecedor;
- dizer que a Resolução 615 vincula diretamente;
- certificar fornecedor com base apenas no contrato.
