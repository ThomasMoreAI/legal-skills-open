---
name: responder-incidente-anpd-roldaobatista
title: responder-incidente-anpd
description: Gera o draft de notificação à ANPD em caso de incidente de segurança que afete dado pessoal (LGPD Art. 48, Resolução CD/ANPD 15/2024). Use no T+24 a T+72h após detecção do incidente. Saída em markdown versionável para revisão jurídica antes de submeter ao portal da ANPD.
author: roldaobatista
author_url: https://github.com/roldaobatista/roldao-method/tree/main/addons/lgpd-compliance/.claude/skills/responder-incidente-anpd
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# responder-incidente-anpd

Skill que gera o draft de **comunicado de incidente à ANPD** conforme LGPD Art. 48 e Resolução CD/ANPD nº 15/2024.

> **IMPORTANTE:** esta skill gera **draft**. A notificação oficial ao portal da ANPD precisa de revisão do DPO + jurídico antes do envio. Veja o runbook completo em `docs/runbooks/incident-response-lgpd.md`.

## Quando usar

- Incidente de segurança detectado afetando dado pessoal.
- Severidade **crítica** ou **alta** (ver runbook para critérios).
- Janela de notificação obrigatória: até **72h após ciência** do incidente.

## Argumentos esperados

A skill pede ao chamador (DPO ou tech lead via maestro):

1. **ID do incidente** — slug curto (ex: `INC-2026-05-22-vazamento-leads`).
2. **Data/hora de ciência** — UTC + horário local.
3. **Natureza dos dados** — categorias afetadas (CPF, endereço, financeiro, saúde, biometria, etc.).
4. **Quantitativo de titulares** — faixa aproximada.
5. **Causa imediata** — exfiltração, exposição, perda, acesso indevido.
6. **Medidas já tomadas** — contenção, isolamento, comunicação interna.
7. **Risco ao titular** — alto/médio/baixo + justificativa.
8. **Plano de mitigação** — ações + owner + prazo.

Se algum item faltar, peça **ao chamador**, não ao usuário final.

## Saída

Arquivo em `docs/incidentes/INC-AAAA-MM-DD-<slug>/notificacao-anpd.md` com o template preenchido:

```markdown
---
owner: dpo
revisado-em: AAAA-MM-DD
status: rascunho
incidente: INC-AAAA-MM-DD-<slug>
sla-72h: AAAA-MM-DD HH:MM
---

# Comunicado de incidente — ANPD

**Controlador:** <razão social + CNPJ>
**DPO/Encarregado:** <nome + email + telefone>
**Data do incidente:** <AAAA-MM-DD HH:MM UTC>
**Data de ciência:** <AAAA-MM-DD HH:MM UTC>
**Data deste comunicado:** <AAAA-MM-DD HH:MM UTC>

## 1. Natureza dos dados afetados

<categorias — ex: CPF, endereço, dados de transação financeira>

Dados sensíveis (Art. 11): <sim/não, quais>

## 2. Titulares afetados

Número aproximado: <faixa>
Categoria: <consumidores, funcionários, fornecedores, etc.>

## 3. Medidas técnicas e de segurança vigentes antes do incidente

<criptografia, controle de acesso, MFA, logs, monitoramento, etc.>

## 4. Causa e dinâmica do incidente

<o que aconteceu, na ordem dos fatos>

## 5. Riscos e impactos previsíveis

<alto/médio/baixo — justificar com base no tipo de dado + escala + uso provável pelo atacante>

## 6. Medidas adotadas para reverter/mitigar

Imediatas (T+0 a T+24h):
- <ação 1>
- <ação 2>

Em andamento (T+24h a T+30 dias):
- <ação + owner + prazo>

## 7. Comunicação aos titulares

Status: <feita / em curso / não aplicável>
Canal: <email, push, SMS, site>
Conteúdo: anexo em `notificacao-titulares.md`

## 8. Razão de eventual demora (se >72h após ciência)

<explicar — só se aplicável>

## 9. Contato para acompanhamento

DPO: <nome>
Email: <dpo@empresa.com.br>
Telefone: <+55...>

---

Documento gerado por skill `responder-incidente-anpd` em <data>. Revisado por: <DPO> em <data>.
```

## Checklist antes de enviar à ANPD

- [ ] DPO revisou e assinou.
- [ ] Jurídico revisou linguagem e responsabilidades.
- [ ] CEO/Diretoria ciente.
- [ ] Notificação aos titulares preparada (paralelo).
- [ ] Evidências preservadas (logs, snapshots, configs).
- [ ] Post-mortem agendado.
- [ ] Issue de mitigação aberta com owner.

## Anti-padrões

- ❌ Gerar e enviar direto sem revisão jurídica.
- ❌ Minimizar risco ("é só uma exposição interna").
- ❌ Esconder informação relevante (a ANPD pode pedir esclarecimento e descobrir).
- ❌ Notificar fora do prazo sem justificar.

## Referências

- LGPD Art. 48 — Comunicação à ANPD e aos titulares.
- Resolução CD/ANPD nº 15/2024 — diretrizes do comunicado.
- Runbook: `docs/runbooks/incident-response-lgpd.md`.
- Skills relacionadas: `gerar-ripd`, `gerar-canal-dpo`, `resposta-titular`.

---

_Framework: [ROLDAO-METHOD](https://github.com/roldaobatista/roldao-method) — addon `lgpd-compliance`._
