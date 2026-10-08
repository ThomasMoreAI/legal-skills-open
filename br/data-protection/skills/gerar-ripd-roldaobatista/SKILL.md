---
name: gerar-ripd-roldaobatista
title: gerar-ripd
description: Gera Relatorio de Impacto a Protecao de Dados (RIPD) — Art. 38 LGPD. Use quando tratamento e de alto risco (dado sensivel em escala, decisao automatizada, monitoramento sistematico, crianca/adolescente). Saida em markdown versionavel.
author: roldaobatista
author_url: https://github.com/roldaobatista/roldao-method/tree/main/addons/lgpd-compliance/.claude/skills/gerar-ripd
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
---

# gerar-ripd

Gera template estruturado de RIPD pra documentar tratamento de alto risco. O agente preenche cada seção com base nas informações da feature/PRD.

## Quando é obrigatório

Pelo menos 1 critério (Art. 38 + Resolução ANPD 1/2021):

- [ ] Tratamento de dado sensível em larga escala (>1.000 titulares).
- [ ] Tratamento em larga escala (cobertura ampla ou volume alto).
- [ ] Decisão automatizada com efeito jurídico ou significativo no titular.
- [ ] Monitoramento sistemático e contínuo (ex: câmeras, geolocalização constante).
- [ ] Combinação de bases de dados com finalidades diferentes (data lake B2B+B2C).
- [ ] Tratamento de dado de criança/adolescente em escala.
- [ ] Tecnologia inovadora ou em uso novo (IA generativa em decisão, biometria).
- [ ] Avaliação de aspectos pessoais do titular (perfilamento, scoring).

## Template

Gerar em `docs/ripd/RIPD-NNN-<slug-tratamento>.md`:

```markdown
---
tipo: ripd
id: RIPD-NNN
versao: 1
status: draft
owner: dpo-virtual + tech-lead
revisado-em: AAAA-MM-DD
proxima-revisao: AAAA-MM-DD (12 meses)
---

# RIPD-NNN — Relatório de Impacto à Proteção de Dados

> Documento previsto no Art. 38 da LGPD. Avalia riscos do tratamento e medidas de mitigação. Versionado junto com a feature que ele descreve.

## 1. Identificação do tratamento

- **Nome do tratamento:** _(nome curto e descritivo)_
- **Finalidade:** _(o que se busca alcançar)_
- **Feature/sistema:** _(referência: PRD-NNN, módulo X)_
- **Controlador:** _(nome empresarial completo)_
- **Operadores:** _(terceiros que processam — listar)_
- **Encarregado (DPO):** _(nome / email)_

## 2. Necessidade e proporcionalidade

### 2.1 Por que esse tratamento é necessário?
_(Justificativa clara. Sem essa argumentação, falta base de necessidade — LGPD-003.)_

### 2.2 Quais alternativas foram consideradas?
- [ ] Não tratar.
- [ ] Tratar com dados anonimizados.
- [ ] Tratar com pseudonimização.
- [ ] _(...)_

### 2.3 Por que essa é a forma menos invasiva?
_(...)_

## 3. Dados pessoais tratados

| Categoria | Dados específicos | Sensível? | Origem | Base legal |
|---|---|---|---|---|
| _(Cadastro)_ | _(CPF, nome, email)_ | Não | Cliente | Art. 7 V (contrato) |
| _(Saúde)_ | _(CID, prescrição)_ | **Sim** | Médico | Art. 11 II f |

## 4. Titulares afetados

- **Quem:** _(ex: clientes adultos de SP)_
- **Quantidade estimada:** _(N titulares)_
- **Vulneráveis:** _(criança? idoso? Sim/Não — se sim, atenção redobrada)_

## 5. Operações de tratamento

- [ ] Coleta
- [ ] Armazenamento
- [ ] Compartilhamento com terceiros
- [ ] Transferência internacional
- [ ] Decisão automatizada
- [ ] Profilamento / scoring
- [ ] Monitoramento contínuo
- [ ] Combinação com outras bases
- [ ] Eliminação

## 6. Compartilhamento

| Operador / 3º | País | DPA? | Finalidade |
|---|---|---|---|
| _(ex: AWS)_ | EUA | Sim, 2024-XX | Hospedagem |
| _(ex: OpenAI)_ | EUA | Sim, 2025-YY | IA generativa em análise |

## 7. Análise de riscos

### Risco 1 — _(ex: vazamento por SQL injection)_
- **Probabilidade:** _(baixa/média/alta)_
- **Impacto ao titular:** _(baixo/médio/alto/crítico)_
- **Medidas atuais:** _(ORM com query preparada, code review)_
- **Medidas propostas:** _(WAF, pentest semestral)_
- **Risco residual:** _(baixo)_

### Risco 2 — _(ex: viés algorítmico em decisão automatizada)_
_(...)_

### Risco 3 — _(...)_

## 8. Medidas técnicas e administrativas

### Técnicas
- [ ] Criptografia em trânsito (TLS 1.2+).
- [ ] Criptografia em repouso (AES-256 ou equivalente).
- [ ] Pseudonimização / tokenização onde aplicável.
- [ ] Anonimização em relatórios.
- [ ] Trilha de acesso (LGPD-004).
- [ ] Backup com retenção definida.
- [ ] Plano de recuperação testado.

### Administrativas
- [ ] Treinamento periódico do time.
- [ ] Política de privacidade publicada.
- [ ] DPAs assinados com operadores.
- [ ] Canal do titular ativo (DPO).
- [ ] Plano de incidente testado.
- [ ] Auditoria periódica.

## 9. Direitos do titular

| Direito (Art. 18) | Como exerce | SLA |
|---|---|---|
| Confirmação + acesso | Email DPO ou self-service | 15 dias |
| Correção | Self-service | Imediato |
| Exclusão | Email DPO | 15 dias |
| Portabilidade | Self-service ou DPO | 15 dias |
| Revisão de decisão automatizada | DPO + analista humano | 15 dias |

## 10. Decisão automatizada (se aplicável)

- **O que é decidido automaticamente:** _(...)_
- **Critérios usados:** _(...)_
- **Efeito ao titular:** _(...)_
- **Possibilidade de revisão humana:** _(sim/não — Art. 20 exige sim)_
- **Explicabilidade:** _(em palavras claras)_
- **Mitigação de viés:** _(...)_

## 11. Conclusão

- **Risco residual aceitável?** _(sim/não)_
- **Tratamento pode prosseguir?** _(sim/não/com ressalvas)_
- **Ressalvas:** _(...)_
- **Próxima revisão:** AAAA-MM-DD (em 12 meses ou antes se houver mudança).

## 12. Aprovações

| Papel | Nome | Data | Assinatura |
|---|---|---|---|
| DPO | _(...)_ | _(...)_ | _(...)_ |
| Responsável técnico | _(tech-lead)_ | _(...)_ | _(...)_ |
| Responsável de produto | _(gerente-produto)_ | _(...)_ | _(...)_ |
| Conselho (se aplicável) | _(...)_ | _(...)_ | _(...)_ |

## 13. Histórico

| Data | Versão | Quem | Mudança |
|---|---|---|---|
| AAAA-MM-DD | 1 | _(dpo-virtual)_ | criação inicial |
```

## Como preencher

1. Agente `dpo-virtual` lê PRD/feature e preenche seções 1-6.
2. Tech-lead preenche seções 7-8 (riscos técnicos + medidas).
3. DPO revisa, marca riscos residuais e aprova.
4. Documento fica em `docs/ripd/` versionado no git.

## Quando atualizar

- Mudança significativa no tratamento (nova finalidade, novo dado, novo operador).
- Incidente que revelou risco novo.
- Mudança regulatória relevante (resolução ANPD).
- Revisão programada (12 meses).
