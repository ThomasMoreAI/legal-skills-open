---
name: resposta-titular-roldaobatista
title: resposta-titular
description: Gera resposta padronizada a direito exercido por titular LGPD (Art. 18) — acesso, exclusao, portabilidade, revisao. Use ao processar pedido recebido pelo canal do DPO.
author: roldaobatista
author_url: https://github.com/roldaobatista/roldao-method/tree/main/addons/lgpd-compliance/.claude/skills/resposta-titular
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# resposta-titular

Templates de resposta pra cada direito do Art. 18 LGPD. Mantém consistência, garante SLA, gera trilha de auditoria.

## Direito 1 — Confirmação + Acesso (Art. 18 I, II)

```
Olá, {nome},

Protocolo: DPO-{ano}-{numero}
Data da solicitação: {data}

Confirmamos que **tratamos** seus dados pessoais em nossa plataforma.
Abaixo, os dados que mantemos sobre você:

## Dados cadastrais
- Nome: {nome}
- CPF: {cpf}
- Email: {email}
- Telefone: {telefone}
- Endereço: {endereco}

## Histórico de uso (resumo)
- Data de cadastro: {data}
- Última atividade: {data}
- Total de transações: {N}

## Compartilhamento
Seus dados foram compartilhados com:
- {Operador 1}: {finalidade}
- {Operador 2}: {finalidade}

## Bases legais
- Cadastro: execução de contrato (Art. 7 V)
- Histórico de transação: cumprimento de obrigação legal (Art. 7 II — escrituração fiscal)
- Newsletter: consentimento (Art. 7 I) — revogável

## Seus outros direitos
Você pode também solicitar: correção, exclusão, portabilidade, revogação de consentimento, etc.
Detalhes em: https://suaempresa.com.br/privacidade/dpo

Atenciosamente,
DPO — {Nome da Empresa}
```

## Direito 2 — Correção (Art. 18 III)

```
Olá, {nome},

Protocolo: DPO-{ano}-{numero}

Seu pedido de correção foi processado em {data}.

**Alteração realizada:**
- Campo: {campo}
- Valor anterior: {valor_antigo}
- Valor novo: {valor_novo}

A alteração já está refletida em todos os nossos sistemas. Operadores foram
notificados conforme cabível.

Caso precise de outras correções, responda este email.

Atenciosamente,
DPO — {Nome da Empresa}
```

## Direito 3 — Exclusão (Art. 18 IV ou VI)

```
Olá, {nome},

Protocolo: DPO-{ano}-{numero}

Processamos sua solicitação de exclusão em {data}.

## Dados excluídos
- {dado 1}
- {dado 2}

## Dados retidos por obrigação legal
Alguns dados precisam ser mantidos por exigência legal:

- **Notas fiscais e dados de transação:** retidos por 5 anos (Receita Federal).
- **Logs de auditoria:** retidos por 6 meses (segurança).

Esses dados ficam **isolados**, com acesso restrito e não são usados pra outras
finalidades. Após o prazo legal, serão eliminados.

## Operadores notificados
- {operador 1}: confirmado em {data}
- {operador 2}: confirmado em {data}

Sua conta foi desativada. Caso queira voltar a usar o serviço, será necessário
novo cadastro.

Atenciosamente,
DPO — {Nome da Empresa}
```

## Direito 4 — Portabilidade (Art. 18 V)

```
Olá, {nome},

Protocolo: DPO-{ano}-{numero}

Seu pedido de portabilidade foi processado em {data}.

**Anexamos arquivo no formato JSON** com os dados que mantemos sobre você.
Estrutura padronizada (Resolução ANPD em consulta) que permite que outro
fornecedor importe seus dados.

Caso prefira outro formato (CSV, XML), responda este email.

Atenciosamente,
DPO — {Nome da Empresa}

[anexo: dados-{cpf-mascarado}-{data}.json]
```

## Direito 5 — Revogação de consentimento (Art. 18 IX)

```
Olá, {nome},

Protocolo: DPO-{ano}-{numero}

Sua revogação de consentimento foi registrada em {data}.

## Tratamentos afetados (cessados)
- Marketing por email
- Compartilhamento com parceiros para ofertas
- {outros}

## Tratamentos não afetados (continuam por outras bases legais)
- Execução do contrato de serviço (Art. 7 V)
- Cumprimento de obrigação legal — fiscal/contábil (Art. 7 II)

Você pode reativar o consentimento a qualquer momento no painel de privacidade
do seu cadastro.

Atenciosamente,
DPO — {Nome da Empresa}
```

## Direito 6 — Revisão de decisão automatizada (Art. 20)

```
Olá, {nome},

Protocolo: DPO-{ano}-{numero}

Sua solicitação de revisão da decisão automatizada {referencia} foi processada
por um analista humano em {data}.

## Decisão original (automatizada)
- Resultado: {original}
- Critérios usados: {critérios em linguagem clara}

## Análise humana
- Analista: {função, não nome individual}
- Data: {data}
- Resultado: {confirmado / revertido / ajustado}
- Justificativa: {motivo claro}

{Se revertido: explicar a mudança e impacto.}
{Se confirmado: explicar por que a decisão original se mantém.}

Caso discorde, pode:
- Reclamar à ANPD: https://www.gov.br/anpd
- Buscar judicialmente seus direitos.

Atenciosamente,
DPO — {Nome da Empresa}
```

## Direito 7 — Recusa fundamentada

Se o pedido **não pode** ser atendido (ex: dado retido por obrigação legal):

```
Olá, {nome},

Protocolo: DPO-{ano}-{numero}

Recebemos seu pedido de {tipo de pedido} em {data}. Após análise:

**Atendido parcialmente / não pôde ser atendido**

## Motivo
{Fundamentação técnico-legal clara:
- "A exclusão completa não é possível porque os dados de transação devem ser
  mantidos por 5 anos para cumprimento de obrigação fiscal (Art. 7 II LGPD +
  Decreto 9.580/2018 RIR)."
- "Os dados ficam restritos a acesso por fiscalização e não são usados para
  outras finalidades."
}

## O que foi feito
- {dado X foi excluído}
- {dado Y foi anonimizado}
- {dado Z permanece restrito até {data}}

## Próximos passos
- Após {data}, dados retidos serão eliminados.
- Você pode acompanhar em {link}.
- Se discordar, ANPD: https://www.gov.br/anpd.

Atenciosamente,
DPO — {Nome da Empresa}
```

## Checklist por resposta

- [ ] Identidade do titular confirmada (CPF + email do cadastro batem).
- [ ] Direito corretamente classificado.
- [ ] Resposta no prazo: acesso completo em até 15 dias (Art. 19, II); confirmação/acesso simplificado imediato (Art. 19, I); demais direitos do Art. 18 sem prazo legal fixo — 15 dias como SLA interno.
- [ ] Linguagem clara, sem juridiquês.
- [ ] Protocolo numerado e rastreável.
- [ ] Trilha completa no sistema de ticket.
- [ ] Operadores notificados quando aplicável.
- [ ] Resposta assinada (DPO).

## Anti-padrões

❌ Resposta-padrão sem personalização (titular percebe que é genérico).
❌ Linguagem em legalês (titular não entende).
❌ Resposta após o SLA sem justificativa formal.
❌ Negar pedido sem fundamentar em artigo específico.
❌ Pedir documentação excessiva pra "validar" o titular (CPF + email do cadastro são suficientes na maioria dos casos).
❌ Esquecer de notificar operadores que receberam o dado.
