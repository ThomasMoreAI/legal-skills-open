# 04: Matriz de Retenção de Dados

> Quando alguém clica "excluir minha conta", o que sai mesmo, o que vira anônimo, o que fica retido por obrigação legal, e por quanto tempo. **Tabela canônica** pra codificar no app como `data_retention_policy` ou similar.

## Princípio (art. 15 + art. 16 LGPD)

- **Art. 15:** o tratamento de dados pessoais será encerrado quando:
  - I, verificada a finalidade alcançada ou os dados deixarem de ser necessários ou pertinentes
  - II, pelo fim do período de tratamento
  - III, comunicação do titular (inclusive revogação de consentimento)
  - IV, determinação da ANPD por violação da lei

- **Art. 16:** dados podem ser **mantidos após o término** apenas se necessário para:
  - I, cumprimento de obrigação legal ou regulatória pelo controlador
  - II, estudo por órgão de pesquisa, com anonimização sempre que possível
  - III, transferência a terceiro (respeitados requisitos da lei)
  - IV, uso exclusivo do controlador, vedado acesso de terceiro, **desde que anonimizados**

## Matriz prática: dado × base × prazo de retenção

### Dados fiscais e contábeis

| Dado | Base legal | Prazo mínimo | Fundamento |
|---|---|---|---|
| Nota Fiscal Eletrônica (NFe) | Art. 7º II | **5 anos** após o exercício | Decreto 7.212/2010 art. 447; CTN art. 173 |
| CT-e, MDF-e | Art. 7º II | 5 anos | Idem |
| Recibos de pagamento | Art. 7º II | 5 anos | CTN |
| Dados de declaração de IR | Art. 7º II | 5 anos | RIR/2018 |
| ECF, ECD (contabilidade digital) | Art. 7º II | 10 anos | CFC NBC TG 1000 + RFB |

### Dados de conexão e aplicação (Marco Civil)

| Dado | Quem guarda | Base legal | Prazo mínimo | Fundamento |
|---|---|---|---|---|
| Logs de **conexão** (IP + timestamp de início/fim, sob sigilo) | Provedor de **conexão** (ISP/telco) | Art. 7º II | **1 ano (12 meses)** | Lei 12.965/2014 art. 13 |
| Logs de **acesso a aplicação** (data/hora de uso a partir de um IP, sob sigilo) | Provedor de **aplicação** PJ com fim econômico (qualquer SaaS, app, API) | Art. 7º II | **6 meses** | Lei 12.965/2014 art. 15 |
| Logs além desses prazos mínimos | - | Art. 7º IX (legítimo interesse) | Justificar no RIPD | LGPD art. 10 |

> **Importante:** os prazos do Marco Civil são **mínimos**, pode reter mais com base legal própria (segurança, auditoria fiscal), mas precisa documentar.
>
> **NÃO inverter:** o erro comum é trocar os dois prazos. **Conexão = 1 ano; aplicação = 6 meses.** A maioria dos apps é **provedor de aplicação**, então o prazo aplicável é **6 meses**, conforme art. 15.
>
> Autoridade policial, MP ou administrativa pode requerer guarda por prazo superior; acesso ao **conteúdo** dos logs exige **ordem judicial** (arts. 22-23). Guardar **conteúdo** das comunicações privadas como rotina viola LGPD (princípio da necessidade), só guardar o que a lei manda: **registros de acesso, não conteúdo**.

### Dados trabalhistas

| Dado | Base legal | Prazo mínimo | Fundamento |
|---|---|---|---|
| Ficha de empregado, registro CTPS | Art. 7º II | **5 anos** após desligamento (mais discutido, alguns juristas defendem 30) | CLT art. 11; Lei 5.553/1968 |
| Folha de pagamento | Art. 7º II | **10 anos** | INSS / DOU |
| FGTS, recolhimentos | Art. 7º II | **30 anos** | Lei 8.036/1990 |
| PPRA, PCMSO, LTCAT (saúde ocupacional) | Art. 11 II f | 20 anos | NR-7, NR-9 |

### Dados bancários / financeiros (Bacen)

| Dado | Base legal | Prazo mínimo | Fundamento |
|---|---|---|---|
| KYC, identificação do cliente | Art. 7º II / X | **5 anos** após encerramento | Resoluções Bacen + Lei 9.613/1998 (PLD-FT) |
| Operações financeiras suspeitas | Art. 7º II | 5 anos | Lei 9.613/1998 |
| Transações em geral | Art. 7º II | 5 anos | Bacen + CTN |
| Cadastro positivo | Art. 7º X | Enquanto válido o consentimento | Lei 12.414/2011 |

### Dados de saúde

| Dado | Base legal | Prazo mínimo | Fundamento |
|---|---|---|---|
| Prontuário do paciente | Art. 11 II f | **20 anos** após último registro | Resolução CFM 1.821/2007 |
| Receituário | Art. 7º II | 5 anos | Anvisa / vigilância sanitária |

### Dados de criança e adolescente

| Dado | Base legal | Prazo | Fundamento |
|---|---|---|---|
| Cadastro em app com criança | Art. 14 (consentimento parental) ou outra base | Limitado ao **necessário pra finalidade**; ao completar 18 anos, o titular pode revisar | ECA + LGPD art. 14 |

### Dados de uso do produto (analytics, comportamento)

| Dado | Base legal | Prazo sugerido | Observação |
|---|---|---|---|
| Analytics agregados (GA4, Plausible) | Art. 7º I (consentimento) | Conforme política do app | Anonimizar IP. GA4 default = 14 meses |
| Cookies de funcionalidade | Art. 7º V/IX | Sessão ou X dias | Documentar na política de cookies |
| Cookies de marketing | Art. 7º I (consentimento) | Até revogação ou X meses | Idem |
| Histórico de buscas internas | Art. 7º V ou IX | Até X meses pós-última interação | Anonimizar histórico antigo |

### Dados pra exercício de direito em juízo

| Dado | Base legal | Prazo | Fundamento |
|---|---|---|---|
| Contratos digitais aceitos | Art. 7º VI | **20 anos** (prescrição civil máxima) | CC art. 205; CDC art. 27 (5 anos consumo) |
| Provas de comunicação com cliente | Art. 7º VI | 5 anos (consumo) ou 3 anos (CC) | CDC + CC |
| Termos de uso aceitos pelo usuário | Art. 7º VI | Enquanto durar a relação + prescrição aplicável | Idem |

## Como codificar no app

Estrutura sugerida (Postgres / qualquer SQL):

```sql
CREATE TABLE retention_policy (
  data_category    text PRIMARY KEY,    -- ex: 'nfe', 'log_conexao', 'consent_marketing'
  legal_basis      text NOT NULL,       -- ex: 'lgpd_art7_II_obrigacao_legal'
  legal_source     text NOT NULL,       -- ex: 'Lei 12.965/2014 art. 13'
  retention_days   integer,             -- NULL = enquanto durar a relação
  on_delete_action text NOT NULL,       -- 'hard_delete' | 'anonymize' | 'retain_with_basis'
  justification    text                 -- texto pra mostrar ao titular
);
```

E uma rotina periódica (cron / pg_cron / Airflow) que purga ou anonimiza dados que ultrapassaram a retenção.

## Fluxo de "Excluir minha conta"

```
Titular clica "Excluir conta"
   │
   ▼
┌─────────────────────────────────────────────────┐
│ Pra cada tabela com dados pessoais do titular:  │
│   1. Olha retention_policy[categoria]            │
│   2. Decide ação:                                │
│      - hard_delete    → DELETE                   │
│      - anonymize      → UPDATE c/ hash + nulls   │
│      - retain         → mantém, flag is_retained │
│ Exibe ao titular: o que apagou, o que reteve     │
│ e por qual lei.                                  │
└─────────────────────────────────────────────────┘
   │
   ▼
Audit log: timestamp, titular_id, categorias_afetadas, ação
```

## Mensagem-padrão pro titular na confirmação de exclusão

```
Sua conta foi excluída em {{DATA}}.

Dados apagados:
- perfil completo (nome, e-mail, telefone)
- preferências de uso
- histórico de buscas
- consentimentos

Dados retidos por obrigação legal:
- Notas fiscais emitidas: por 5 anos (Decreto 7.212/2010)
- Logs de acesso à aplicação (IP, login): por 6 meses (Marco Civil, Lei 12.965/2014 art. 15)
- Comunicações relacionadas a transações: 5 anos (CDC)

Ao fim desses prazos, esses dados serão eliminados ou anonimizados.

Se desejar contestar a retenção ou exercer outros direitos, contate
{{DPO_CONTATO}}.
```

## Referências externas

- [LGPD Art. 15 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art15)
- [LGPD Art. 16 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art16)
- [Marco Civil da Internet (Lei 12.965/2014)](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm)
- [CTN (Lei 5.172/1966)](https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm)
- [CDC (Lei 8.078/1990)](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm)
- [Lei do FGTS (Lei 8.036/1990)](https://www.planalto.gov.br/ccivil_03/leis/l8036consol.htm)
- [PLD-FT (Lei 9.613/1998)](https://www.planalto.gov.br/ccivil_03/leis/l9613.htm)
- [Resolução CFM 1.821/2007 (prontuário)](https://sistemas.cfm.org.br/normas/visualizar/resolucoes/BR/2007/1821)
