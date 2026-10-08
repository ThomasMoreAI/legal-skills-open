# Registro de Operações de Tratamento de Dados Pessoais (ROPA)

**Controlador**: {razão social} | **CNPJ**: {nº} | **Endereço**: {endereço}
**Encarregado (DPO)**: {nome} | **Contato**: {e-mail / telefone}
**Versão**: v{N} | **Data**: {data} | **Próxima revisão**: {data + 6 meses}

## Changelog

- v1.0 ({data}): publicação inicial
- v1.1 ({data}): {alteração}

---

## I. Atividades como Controlador

### A001 — {nome da atividade}

| Campo | Conteúdo |
|---|---|
| **Finalidade** | {específica, determinada, explícita} |
| **Base legal** | Art. {7º/11}, inciso {N} |
| **Categorias de titulares** | Usuários adultos, adolescentes (flag), crianças (flag) |
| **Categorias de dados — comuns** | nome, e-mail, telefone, IP, device ID |
| **Categorias de dados — sensíveis** | nenhum / {listar} |
| **Fonte dos dados** | coletado do titular / observado / inferido / terceiro |
| **Compartilhamento interno** | {times/empresas do grupo} |
| **Compartilhamento externo (operadores)** | {AWS, Datadog, ...} |
| **Transferência internacional?** | Não / Sim — ver `.lgpd/transfers/{vendor}.md` |
| **Período de armazenamento** | {prazo} — critério: {legal/contratual/anonimização} |
| **Medidas de segurança** | TLS 1.3, TDE, RBAC, audit log, MFA, backup criptografado |
| **Decisão automatizada?** | Não / Sim — ver `.lgpd/RIPD/ripd-a001.md` |
| **Alto risco?** | Não / Sim — RIPD: `.lgpd/RIPD/ripd-a001.md` |
| **Observações** | {qualquer informação relevante} |

### A002 — ...

(Repetir para cada atividade)

---

## II. Atividades como Operador

### O001 — {nome da atividade}

| Campo | Conteúdo |
|---|---|
| **Controlador** | {nome do cliente / parceiro} |
| **Contrato/DPA** | `.lgpd/vendors/{controlador}.md` |
| **Finalidade (do controlador)** | {qual finalidade nos foi instruída} |
| **Categorias de dados** | {recebidas do controlador} |
| **Medidas de segurança aplicadas** | {idem} |
| **Sub-operadores autorizados** | {lista — Art. 39, § 1º} |
| **Devolução/eliminação ao fim** | {previsão contratual} |

---

## III. Resumo executivo

- **Total de atividades como controlador**: {N}
- **Total como operador**: {M}
- **Atividades com dados sensíveis**: {N}
- **Atividades com menores**: {N} (avaliação ECA Digital: ver `.lgpd/eca-digital.md`)
- **Atividades de alto risco com RIPD**: {N}
- **Transferências internacionais ativas**: {N}
- **Operadores ativos com DPA assinado**: {N}/{M total}

## IV. Anexos

- Política de privacidade vigente: `.lgpd/policies/privacy-policy-v{N}.md`
- LIAs: `.lgpd/lia/`
- RIPDs: `.lgpd/RIPD/`
- DPAs: `.lgpd/vendors/`
- Cláusulas-padrão Res. 19/2024: `.lgpd/transfers/`
