---
name: legal-basics-bappoz
title: Legal Basics (para devs)
description: 'Noções jurídicas para desenvolvedores e founders: contratos, LGPD/GDPR, propriedade intelectual e licenças de software open-source. Orienta e sinaliza riscos — NÃO substitui advogado. Use quando o usuário mencionar: "contrato", "termos de uso", "política de privacidade", "LGPD", "GDPR", "dados pessoais", "licença", "open source", "propriedade intelectual", "posso usar este código?", "MIT vs GPL", "NDA", "compliance".'
author: Bappoz
author_url: https://github.com/Bappoz/My-Claude-Skills/tree/main/skills/domain-knowledge/legal-basics
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# Legal Basics (para devs)

Você atua como tradutor de jurídico para engenharia. Objetivo: dar **noções acionáveis** e apontar quando o risco exige um advogado de verdade. Não é aconselhamento jurídico — é alfabetização legal para não pisar em minas óbvias.

> ⚠️ **Aviso**: isto orienta e sinaliza riscos. Decisões com impacto real (contrato assinado, produto lançado, litígio) precisam de advogado licenciado na jurisdição aplicável.

## Contratos — o que ler antes de assinar

| Cláusula | Por que importa |
|---|---|
| **Objeto/escopo** | O que exatamente está sendo contratado |
| **Propriedade intelectual** | Quem fica dono do que foi criado (work-for-hire vs licença) |
| **Confidencialidade (NDA)** | O que não pode vazar, por quanto tempo |
| **Limitação de responsabilidade** | Teto de indenização; exclusões |
| **Rescisão** | Como sair, aviso prévio, o que acontece com os dados |
| **Foro/lei aplicável** | Onde e sob qual lei se resolve disputa |
| **SLA/garantias** | O que é prometido e a consequência de não cumprir |

Regra: **se não entende uma cláusula, não assine "confiando".** Ambiguidade favorece quem redigiu.

## LGPD / GDPR — proteção de dados

Aplicam-se sempre que você trata **dados pessoais** (qualquer dado que identifique alguém).

- **Base legal**: todo tratamento precisa de uma justificativa (consentimento, execução de contrato, legítimo interesse, obrigação legal…). Sem base legal = ilegal.
- **Minimização**: colete só o necessário para a finalidade declarada. Não guarde "por precaução".
- **Finalidade**: use o dado só para o que foi informado ao titular.
- **Direitos do titular**: acesso, correção, exclusão, portabilidade. Seu sistema precisa conseguir atendê-los.
- **Segurança**: medidas técnicas (cripto, acesso mínimo — ver [[security]]). Vazamento pode exigir notificação à ANPD/autoridade e aos titulares.
- **Dados sensíveis** (saúde, raça, biometria, orientação) têm proteção reforçada.
- **Transferência internacional** e **cookies/rastreamento** têm regras específicas (banner de consentimento real, não dark pattern).

Prático: tenha **Política de Privacidade** honesta, registro de tratamentos, e um caminho para exclusão de conta/dados.

## Propriedade intelectual

- **Copyright**: código/texto/arte são protegidos automaticamente ao serem criados. Usar sem permissão/licença é violação.
- **Work-for-hire**: por padrão, funcionário → obra do empregador; **freelancer/contractor → autor mantém direitos** salvo cessão escrita. Se contrata dev externo, exija cláusula de cessão de IP.
- **Marca (trademark)**: nome/logo — pesquise antes de nomear produto (evita rebrand forçado).
- **Segredo de negócio**: protegido enquanto secreto (daí o NDA).

## Licenças de software open-source (o campo minado do dev)

| Licença | Tipo | Pode usar em produto fechado? | Obrigação principal |
|---|---|---|---|
| **MIT / BSD / ISC** | Permissiva | ✅ Sim | Manter aviso de copyright |
| **Apache 2.0** | Permissiva | ✅ Sim | Aviso + concessão de patente + NOTICE |
| **LGPL** | Copyleft fraco | ✅ Se linkar dinamicamente | Alterações na lib voltam abertas |
| **GPL / AGPL** | Copyleft forte | ⚠️ Contamina: seu código pode ter de virar GPL | AGPL cobre até uso via rede (SaaS!) |
| **Sem licença** | Proprietário por padrão | ❌ Não | Nenhum direito de uso concedido |

Pontos críticos:
- **"Sem licença" ≠ livre** — sem licença explícita, o padrão é *todos os direitos reservados*. Não use.
- **AGPL** é a armadilha de SaaS: usar código AGPL no backend de um serviço web pode obrigar a abrir seu código.
- **Cheque dependências transitivas** — uma lib GPL enterrada na árvore contamina. Use scanners de licença.

## Fluxo ao avaliar risco

1. Que tipo de questão? (contrato / dados / IP / licença)
2. Aplique o checklist da seção correspondente.
3. Classifique o risco: baixo (siga com cuidado) vs alto (**pare, chame advogado**).
4. Documente a decisão e a base.

## Recursos externos

| Recurso | O que pegar |
|---|---|
| [Choose a License](https://choosealicense.com/) | Comparar licenças open-source e escolher a sua. |
| [tl;dr Legal](https://www.tldrlegal.com/) | Resumo em linguagem simples de cada licença. |
| [LGPD — texto oficial (gov.br)](https://www.gov.br/anpd/pt-br) | Lei brasileira + orientações da ANPD. |
| [GDPR.eu](https://gdpr.eu/) | Guia prático do GDPR europeu. |
| [SPDX License List](https://spdx.org/licenses/) | Identificadores padrão de licença (para SBOM/scan). |
| [Terms of Service; Didn't Read](https://tosdr.org/) | Como termos abusivos se parecem. |

## Do / Don't

| Do | Don't |
|---|---|
| Ler cláusula de IP/responsabilidade | Assinar "confiando" |
| Base legal + minimização de dados | Coletar dado "por precaução" |
| Checar licença de toda dependência | Assumir que "está no GitHub" = livre |
| Cessão de IP escrita com freelancer | Presumir que pagou = é seu |
| Chamar advogado no risco alto | Tratar orientação como parecer jurídico |

## Checklist

- [ ] Contrato: IP, responsabilidade, rescisão e foro entendidos
- [ ] Dados pessoais: base legal, minimização, direitos do titular atendíveis
- [ ] Política de Privacidade honesta + caminho de exclusão
- [ ] IP: cessão escrita com contractors; marca pesquisada
- [ ] Licenças de dependências verificadas (sem GPL/AGPL indesejada; nada "sem licença")
- [ ] Risco alto → encaminhado a advogado, decisão documentada
