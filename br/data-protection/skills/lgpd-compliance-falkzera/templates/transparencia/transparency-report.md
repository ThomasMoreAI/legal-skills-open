<!--
TEMPLATE: Relatório Anual de Transparência
=============================================
Skill: lgpd-compliance (Parte 3)
Saída: <projeto>/transparencia/relatorios/{ANO}.md
Renderizado em /transparencia/relatorio/{ANO}

Publicado uma vez por ano (ou semestral, se houver volume).
Inspirado em transparency reports de Google, Meta, Twitter/X, GitHub,
adaptado pro contexto LGPD/ANPD/Marco Civil.

Os números podem ser gerados a partir das tabelas consent_log, dsr_request,
audit_log, notice_takedown (Partes 1+2) por um script de relatório.
-->

# Relatório de Transparência: {{ANO}}

**{{APP_NOME}}** · Publicado em {{DATA_PUBLICACAO}} · Cobre o período de **01/01/{{ANO}} a 31/12/{{ANO}}**

---

## Sumário executivo

| Indicador | {{ANO}} | {{ANO_ANTERIOR}} |
|---|---|---|
| Usuários ativos médios | {{N1}} | {{N0}} |
| Pedidos de titular recebidos (LGPD art. 18) | {{N1}} | {{N0}} |
| Tempo médio de resposta a titulares | {{N1}}d | {{N0}}d |
| Incidentes de segurança comunicados à ANPD | {{N1}} | {{N0}} |
| Conteúdo removido por notice & takedown | {{N1}} | {{N0}} |
| Requisições de autoridades atendidas | {{N1}} | {{N0}} |
| Decisões automatizadas tomadas | {{N1}} | {{N0}} |
| Uptime do serviço | {{X}}% | {{Y}}% |

---

## 1. Requisições de autoridades

Recebemos requisições formais de autoridades públicas (Justiça, MP, Polícia, Receita) sobre dados de usuários.

| Autoridade | Recebidas | Atendidas | Recusadas | Parciais |
|---|---|---|---|---|
| Justiça (ordem judicial) | {{N}} | {{N}} | {{N}} | {{N}} |
| Ministério Público | {{N}} | {{N}} | {{N}} | {{N}} |
| Polícia (PF, PC) | {{N}} | {{N}} | {{N}} | {{N}} |
| Receita Federal | {{N}} | {{N}} | {{N}} | {{N}} |
| ANPD | {{N}} | {{N}} | {{N}} | {{N}} |
| Outras | {{N}} | {{N}} | {{N}} | {{N}} |
| **Total** | **{{N}}** | **{{N}}** | **{{N}}** | **{{N}}** |

**Titulares afetados:** aproximadamente {{N}}.

**Política:** notificamos o titular afetado, salvo selo de sigilo judicial. {{N}} titulares foram notificados em {{ANO}}.

**Recusas:** {{descrever razões agregadas, ex: pedido sem fundamento legal, escopo excessivo, fora da nossa custódia}}.

---

## 2. Exercício de direitos do titular (LGPD art. 18)

| Direito | Recebidas | Atendidas | Tempo médio | Recusadas | Motivo da recusa |
|---|---|---|---|---|---|
| Confirmação de tratamento | {{N}} | {{N}} | {{N}}d | {{N}} | - |
| Acesso aos dados | {{N}} | {{N}} | {{N}}d | {{N}} | - |
| Correção | {{N}} | {{N}} | {{N}}d | {{N}} | - |
| Anonimização/Bloqueio/Eliminação | {{N}} | {{N}} | {{N}}d | {{N}} | {{ex: litígio em curso}} |
| Portabilidade | {{N}} | {{N}} | {{N}}d | {{N}} | - |
| Eliminação (consentimento) | {{N}} | {{N}} | {{N}}d | {{N}} | - |
| Informação sobre compartilhamento | {{N}} | {{N}} | {{N}}d | {{N}} | - |
| Informação sobre não consentir | {{N}} | {{N}} | {{N}}d | {{N}} | - |
| Revogação de consentimento | {{N}} | {{N}} | <1d | {{N}} | - |
| Revisão de decisão automatizada (art. 20) | {{N}} | {{N}} | {{N}}d | {{N}} | - |
| **Total** | **{{N}}** | **{{N}}** | **{{N}}d** | **{{N}}** | - |

**SLA cumprido:** {{X}}% dos pedidos atendidos dentro do prazo (15d regime geral / 30d ATPP).

---

## 3. Incidentes de segurança

Comunicamos **todos** os incidentes de segurança identificados em {{ANO}}, mesmo aqueles que não alcançaram o limiar de notificação obrigatória à ANPD.

| # | Data | Duração | Vetor | Dados afetados | Titulares | Comunicado à ANPD | Processo |
|---|---|---|---|---|---|---|---|
| 1 | {{AAAA-MM-DD}} | {{Xh}} | {{vetor}} | {{categoria}} | ~{{N}} | Sim / Não | {{SEI/ANPD nº}} |

Pra cada um, post-mortem público em `/transparencia/incidentes/{id}`.

**Lições aprendidas e medidas implementadas:**
- {{LICAO_1}}
- {{LICAO_2}}

---

## 4. Conteúdo removido (notice & takedown)

> Se o app tem UGC. Pular se não aplica.

Recebemos {{N}} notificações extrajudiciais em {{ANO}}, conforme procedimento publicado em [/legal/notice-takedown](/legal/notice-takedown).

| Categoria | Recebidas | Removidas | Mantidas | Contranotificadas | Restauradas |
|---|---|---|---|---|---|
| Crime contra a honra (art. 19 MCI, ordem judicial) | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| Direito autoral/marca | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| Nudez não consentida (art. 21 MCI) | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| Dever de cuidado (Tema 987 STF), terrorismo/racismo/CSAM/etc | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| Outros ilícitos (art. 21 expandido) | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |
| **Total** | **{{N}}** | **{{N}}** | **{{N}}** | **{{N}}** | **{{N}}** |

**Tempo médio de resposta:**
- Casos do "dever de cuidado": {{Xh}}
- Casos gerais: {{Xh}}

---

## 5. Inteligência Artificial e decisões automatizadas

> Pular se o app não usa IA visível ao usuário.

**Modelos em uso:** {{LISTAR}}, model cards em [/transparencia/ia](/transparencia/ia).

**Decisões automatizadas tomadas:**
- {{TIPO_1}}: {{N}} decisões
- {{TIPO_2}}: {{N}} decisões

**Revisões solicitadas (LGPD art. 20):**
- Pedidos de revisão: {{N}}
- Atendidos: {{N}} ({{X}}%)
- Resultado mudou: {{N}} ({{X}}%)

**Taxa de erro estimada do modelo principal:** {{X}}% (medida em amostra auditada de {{N}} casos).

**Vieses identificados e correções aplicadas:** {{DESCREVER}}.

---

## 6. Métricas operacionais

- **Uptime do serviço:** {{X}}%
- **MTTR (Mean Time to Recovery) de incidentes:** {{X}} minutos
- **% de dependências com CVE crítica patcheada em <7 dias:** {{X}}%
- **Auditoria de segurança independente:** {{ÚLTIMA_DATA}}, [relatório]({{URL_RELATORIO}})
- **Última verificação SSL Labs:** {{NOTA}} ({{URL}})

---

## 7. Conformidade com a Resolução CD/ANPD nº 32/2026 (transferência internacional)

- **Processadores em UE (decisão de adequação):** {{LISTAR}}, dispensam SCC.
- **Processadores fora da UE (exigem SCC):** {{LISTAR}}, todos com SCC ANPD assinada.
- **Processadores em BR:** {{LISTAR}}.

---

## 8. O que muda em {{ANO+1}}

Compromissos pra próximo exercício:

- {{COMPROMISSO_1}}
- {{COMPROMISSO_2}}
- {{COMPROMISSO_3}}

---

## 9. Metodologia

**Como esses números foram gerados:**

- Tabelas `consent_log`, `dsr_request`, `audit_log`, `notice_takedown` (esquema público em [/transparencia/seguranca](/transparencia/seguranca)).
- Período exato: 2026-01-01T00:00:00-03:00 a 2026-12-31T23:59:59-03:00.
- Script de geração: [scripts/gerar-transparency-report.py]({{URL_REPO}}/scripts/gerar-transparency-report.py).
- Arredondamento: pra preservar privacidade em categorias com <5 ocorrências, valores arredondados ou suprimidos (k-anonimato k=5).

---

## 10. Contato

- **Encarregado de Dados (DPO):** {{DPO_CONTATO}}
- **Imprensa:** {{IMPRENSA}}
- **Reclamar à ANPD:** [gov.br/anpd/peticao-de-titular](https://www.gov.br/anpd/pt-br/canais_atendimento/cidadao/peticao-de-titular)

---

*Este relatório segue o modelo dos transparency reports de Google, Meta, Twitter/X e GitHub, adaptado pro contexto LGPD/ANPD/Marco Civil brasileiro. Versões anteriores em [/transparencia/relatorios](/transparencia/relatorios).*
