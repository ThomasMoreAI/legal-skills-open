---
name: firm-self-assessment
title: /firm-self-assessment
description: 'Mapeamento de conformidade LGPD do próprio escritório: dados que o escritório trata (clientes, partes, testemunhas), base legal, RIPD obrigatório, prazos de guarda de documentos do cliente, plano de resposta a incidente de dados. Inverted LGPD kit — ao invés de aconselhar cliente, escritório faz diagnóstico de si mesmo. Use quando o sócio disser "precisamos fazer compliance LGPD do escritório", "qual é nosso risco de dados de cliente", "como guardamos autos", ou "precisamos de plano de incidente".'
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/privacy-legal/skills/firm-self-assessment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: en
---

# /firm-self-assessment

1. Load `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` → firm's own LGPD position, DPA playbook, outputs.
2. Run the inverted workflow below.
3. Mapear quais dados pessoais o escritório trata (origem, categorias, titulares).
4. Identificar base legal: sigilo profissional como legítimo interesse + obrigação legal (Estatuto OAB); consentimento para além do mandato (ex.: newsletter).
5. Verificar se RIPD é obrigatória (art. 38 LGPD): tratamento em legítimo interesse, risco às liberdades civis, dados de menores, etc.
6. Mapear prazos de retenção: prescricional + dever de guarda — citado como 5 anos após fim do mandato (verificar Provimento CFOAB específico).
7. Elaborar plano de resposta a incidente de dados (art. 48 LGPD).
8. Apresentar achados + decisão árvore para próximas ações.

---

# Avaliação de Conformidade LGPD do Escritório

## Escopo e contexto

**This skill is for the firm itself, not a client.** It inverts the typical privacy-advice model: instead of a privacy-legal team advising a company-client on handling customer data, this skill helps the **law firm** audit what data it holds about clients, opposing parties, witnesses, and staff — and map the firm's own compliance obligations.

O escritório é um CONTROLADOR de dados pessoais (Art. 5º, VI LGPD) — dados de cliente (nome, e-mail, telefone, CPF, endereço, informações sensíveis sobre litígios) são coletados e processados pelo escritório no exercício do mandato. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]

Este skill NÃO substitui um DPA/encarregado — é um diagnóstico de entrada para alertar o sócio sobre o que precisa ser mapeado, regulado, e asegurado.

---

## Purpose

Most law firms have never looked at their own data footprint. They hold vast amounts of personal data about clients, opposing parties, witnesses, and employees — much of it sensitive, long-lived, and sometimes in paper form in a basement. The LGPD (Lei 13.709/2018) applies to law firms as controllers of personal data. This skill walks the firm through:

1. **What data you hold** — and why (clients, case details, invoices, timekeeping, emails with PII).
2. **Your lawful basis** — sigilo profissional (professional secrecy) does NOT substitute for a lawful basis; it complements it. You need BOTH.
3. **Retention periods** — not just Estatuto OAB rules, but LGPD's minimization duty.
4. **RIPD necessity** — when a Privacy Impact Assessment is legally mandatory.
5. **Incident response** — what you do if client data leaks.

Objective: help the firm spot gaps so it can fix them before the ANPD (Autoridade Nacional de Proteção de Dados) spots them.

---

## Premissa de jurisdição (Brasil)

A LGPD (Lei 13.709/2018) aplica-se a qualquer operação de tratamento de dados pessoais realizada por pessoa natural ou jurídica de direito privado ou público — inclui escritórios de advocacia (Art. 1º LGPD). Um escritório é um CONTROLADOR quando: [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]

- Determina as finalidades e meios do tratamento (Art. 5º, VI);
- Coleta dados de cliente, partes, testemunhas, staff e os processa.

Sigilo profissional do advogado é uma **proteção contra divulgação involuntária**, não uma base legal de tratamento. O Estatuto OAB Art. 7º, II trata da inviolabilidade de escritório, instrumentos de trabalho, correspondência e comunicações; o Art. 7º, XIX trata da recusa a depor como testemunha sobre fato ligado a cliente ou sigilo profissional. Sigilo NÃO dispensa: [verified: https://www.planalto.gov.br/ccivil_03/leis/l8906.htm]

- Uma base legal sob LGPD art. 7 (consentimento, obrigação legal, execução de contrato, legítimo interesse com teste de balanceamento, proteção de vida, tutela de saúde, pesquisa, proteção de crédito).
- Medidas de segurança (Art. 46 LGPD) — sigilo profissional + criptografia em repouso é melhor que sigilo profissional sozinho. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]
- Direitos do titular (Art. 18 LGPD) — cliente pode pedir acesso, exclusão (certos casos), portabilidade.

**Base legal típica do escritório:**
- **Execução de contrato (mandato)** — dados do cliente são necessários para executar o contrato de prestação de serviços jurídicos (Art. 7º, V LGPD). [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]
- **Obrigação legal** — Estatuto OAB, CPC, Lei 13.140 (mediação) e outras exigem que advogado mantenha registros de cliente (Art. 7º, II LGPD).
- **Legítimo interesse** — cobranças, contato para aviso de vencimento, análise de risco do cliente (se balanceado e documentado).

**Para dados ALÉM do mandato** (ex.: newsletter, marketing, comunicações promocionais), consentimento é uma base legal possível (Art. 7º, I LGPD) e pode ser revogado a qualquer tempo (Art. 8º, §5º); confirme a base legal aplicável ao fluxo concreto, pois o Art. 7º prevê outras hipóteses. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]

**RIPD obrigatória (Art. 38 LGPD)?** Sim, quando:
- Tratamento é fundado em legítimo interesse (exige teste de balanceamento documentado);
- Envolve risco às liberdades civis e direitos fundamentais (ex.: dados sensíveis de cliente, dados de menores);
- A ANPD pode exigir RIPD em procedimentos investigativos.

A RIPD de um escritório é rara mas recomendável quando: (a) guarda dados sensíveis (ex.: segredos de negócio do cliente), (b) processamento envolve larga escala de titulares (ex.: base de testemunhas em litigação coletiva), (c) novo sistema de retenção ou compartilhamento de dados.

**Prazos de retenção:** não foi confirmada na whitelist a afirmação de que o Estatuto OAB Art. 1º fixe guarda documental do cliente "enquanto durar o relacionamento e após", nem que o CPC art. 204 autorize condenação por destruição de documentos. **LGPD exige que retenção respeite finalidade/necessidade: guardar por prazo legítimo, não indefinido.** Balanço de prazo deve ser validado por política do escritório e fonte normativa específica. [verified: https://www.planalto.gov.br/ccivil_03/leis/l8906.htm; https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]

**Incidente de dados (Art. 48 LGPD):** Controlador deve comunicar à ANPD e ao titular incidente de segurança que possa acarretar risco ou dano relevante aos titulares. A ANPD informa que, conforme a Res. CD/ANPD nº 15/2024, a comunicação à ANPD e aos titulares deve ocorrer em até **3 dias úteis**, ressalvada legislação específica. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm; https://www.gov.br/anpd/pt-br/assuntos/comunicacao-de-incidentes-de-seguranca-cis]

---

## Load the playbook

Read `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` first. Check:

- **DPA playbook → quando somos operador** — o escritório trata dados de clientes como um "operador" (processor) em relação ao cliente como controlador? Não. O escritório é CONTROLADOR de seus próprios dados de cliente.
- **Escalation chain** — quem aprova plano de resposta a incidente? Geralmente GC + segurança + DPO.
- **Available integrations** — há ferramenta de gestão de documentos (Drive, SharePoint)? Contratos de processamento com fornecedores de cloud?

Se o CLAUDE.md não tiver posição sobre LGPD do próprio escritório, pergunte:

> Qual é a posição do escritório sobre retenção de dados de cliente? (5 anos após fim do mandato? Diferente por tipo de caso?) Qual é sua base legal principal (execução de contrato, obrigação legal, legítimo interesse)? Quem é o DPO ou responsável por conformidade de dados? Vou registrar a resposta no seu playbook.

---

## Intake — o que precisa ser mapeado?

Antes de fazer o diagnóstico, converse com sócio/DPO/responsável:

### 1. Que dados o escritório trata?

**Dados de cliente:**
- Nome, CPF, CNPJ, e-mail, telefone, endereço (obrigatório para mandato).
- Detalhes do caso: interesse econômico, partes adversas, fatos sensíveis (ex.: direito de família, criminal, sigilo bancário).
- Dados sensíveis (Art. 11 LGPD)? Ex.: raça, religião, saúde, origem étnica, informações genéticas, dados de condenação criminal.
- Histórico financeiro: composição de honorários, pagamentos, atrasos.

**Dados de terceiros no contexto do caso:**
- Partes adversas, testemunhas: nomes, contatos, dados processados durante investigação pré-processual.
- Dados de menores afetados pelo caso (guarda, sucessão, alimentos).

**Dados de funcionários:**
- RH: contratos, folha de pagamento, dados bancários, avaliações.
- Timekeeping: registros de quanto tempo gasto por funcionário em cada cliente (contém dados biométricos potencialmente).

**Dados em quais formatos?**
- Digitais (Drive, SharePoint, e-mail, sistema de gestão processual).
- Papel (autos físicos, correspondência, contratos impressos em cofre).
- Híbrido: pastas de cliente com documentos scaneados + originais guardados.

### 2. Onde os dados residem?

- Servidor local do escritório?
- Cloud (AWS, Google Workspace, Microsoft 365)?
- Terceiros (fornecedor de CLM — contract lifecycle management, sistema processual — PJe)?
- Backups: onde, com que frequência, criptografados?

Se há compartilhamento com terceiros (cloud, CLM, software de contabilidade), há **Termo de Processamento de Dados (DPA)** assinado conforme Art. 39-42 LGPD?

### 3. Base legal do tratamento

Para CADA finalidade de tratamento, identificar qual é a base legal:

| Finalidade | Base legal | Documentado? | Teste de balanceamento (se LI)? |
|---|---|---|---|
| Execução do mandato (servir o cliente) | Art. 7º, V (execução de contrato) | Sim (contrato de prestação) | N/A |
| Cobranças e aviso de vencimento | Art. 7º, II ou V (obrigação legal / contrato) | Sim (contrato) | N/A |
| Retenção para fins de guarda obrigatória (Estatuto OAB) | Art. 7º, II (obrigação legal) | Sim | N/A | [unverified: not found in primary source]
| Newsletter / marketing jurídico | Art. 7º, I (consentimento) | Quem deu consentimento? | N/A |
| Análise de risco do cliente (ex.: possível lavagem de dinheiro) | Art. 7º, IX (legítimo interesse) | Recomendado documentar | SIM — teste de balanceamento necessário |

### 4. Prazos de retenção — o que diz o Estatuto vs. LGPD?

- **Estatuto OAB:** Guarda "enquanto durar o relacionamento e após" (vago).
- **Jurisprudência OAB:** 5 anos após fim do mandato (recomendado, citado em Provimentos) [unverified: not found in primary source].
- **LGPD Art. 15-16:** término do tratamento e hipóteses de conservação após o término; o direito de eliminação pelo titular está no Art. 18, VI. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]
- **CPC Art. 204 e correlatos:** CPC Art. 204 não confirma obrigação geral de guarda de processos nem responsabilidade por destruição prematura. [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm]

**Política do escritório:**
- Definir: guardar 5 anos após fim do mandato (padrão defensável)?
- Exceções (maior retenção por lei setorial, ex.: direito tributário — 10 anos)?
- Exclusão: como garantir eliminação segura (trituração, apagamento criptográfico, certificado de destruição)?

### 5. Há RIPD obrigatória?

Avaliar:
- Dados sensíveis em volume significativo? (Risco: sim)
- Processamento fundado em legítimo interesse? (Risco: sim — precisa teste de balanceamento)
- Dados de menores? (Risco: sim — Art. 14 LGPD)
- Decisões automatizadas sobre cliente? (Risco: médio)

Se sim em qualquer item: RIPD é recomendada (ou exigida se ANPD chamar).

### 6. Há plano de resposta a incidente de dados?

Pergunta de entrada: qual é o plano atual se um servidor é invadido, um laptop com autos é roubado, ou um funcionário vaza dados?

- Quem notifica: sócio? DPO? ANPD?
- Prazo: em quanto tempo detecta incidente? Notifica ANPD (72h)?
- Comunicação ao cliente: como avisa o cliente que seus dados podem ter vazado?
- Remediação: que medidas toma para conter e investigar?

Se não há plano formal: é um gap crítico.

---

## Step 1: Mapear dados pessoais

Produza uma tabela de inventário de dados:

```markdown
## 1. Inventário de Dados Pessoais Tratados pelo Escritório

| Categoria | Tipo de dado | Titular | Origem | Base legal | Retenção | Localização |
|---|---|---|---|---|---|---|
| Dados do cliente | Nome, CPF, e-mail, telefone | Cliente | Contrato de prestação | Art. 7º V (contrato) | 5 anos pós-mandato | Drive + papel |
| Dados do caso | Partes, litígios, estratégia | Cliente + partes adversas | Investigação pré-processual | Art. 7º V + Art. 7º II | 5 anos pós-mandato | Drive + Sistema processual |
| Dados sensíveis de cliente | Saúde, direito de família, criminal | Cliente | Mandato | Art. 7º V + Art. 11 (se sensível) | 5 anos pós-mandato | Drive (criptografado) |
| Dados de testemunhas | Nomes, contatos, deposições | Testemunha | Investigação + audiência | Art. 7º V (execução do contrato) | 5 anos pós-mandato | Drive + autos |
| Dados de terceiros (fornecedores, peritos) | Nome, e-mail, faturas | Terceiro | Contratação para o caso | Art. 7º V | Período contratual + 5 anos | Contabilidade + Drive |
| Dados de RH (staff) | Nome, CPF, e-mail, banco, avaliações | Funcionário | HR | Art. 7º V (contrato de trabalho) + Art. 7º II (obrigação legal) | Conforme CLT + prazos tributários (até 10 anos) | Sistema RH + papel |
| Dados de cobrança | Honorários, pagamentos, atrasos | Cliente | Faturamento | Art. 7º V + Art. 7º II (obrigação contábil) | 5 anos (prazo tributário Lei 8.180) | Sistema de contabilidade |
| Dados de comunicação | E-mails, mensagens WhatsApp, atas | Cliente + partes | Correspondência | Art. 7º V (execução de contrato) | 5 anos pós-mandato | E-mail + Drive |
| [Adicione categorias específicas do seu escritório] | | | | | | |
```

---

## Step 2: Verificar base legal e documentação

Para CADA categoria acima, confirme:

1. **Há base legal clara?** Registre a hipótese do Art. 7 (ou Art. 11 se dados sensíveis).
2. **Está documentado?** (Contrato de mandato, política interna, consentimento por escrito?)
3. **Se legítimo interesse:** há teste de balanceamento documentado? [Exemplo: "Retenção de 5 anos é necessária para cumprimento de obrigação legal (Estatuto OAB) e para defesa de possíveis reclamações disciplinares. Interesse do escritório de gerenciar risco profissional supera interesse de privacidade do cliente, que é informado do contrato."]

---

## Step 3: Verificar se RIPD é obrigatória

Responda:

- [ ] O escritório processa dados sensíveis (Art. 11 LGPD) em volume significativo? (Sim = RIPD é recomendada)
- [ ] Há fundamento em legítimo interesse (Art. 7º, IX) sem documentação de teste? (Sim = risco — RIPD defende)
- [ ] Dados de menores (Art. 14 LGPD) são rotina? (Sim = RIPD é recomendada)
- [ ] Há transferência internacional de dados de cliente? (Sim = RIPD exigida — Art. 33 LGPD sobre transferência)
- [ ] O escritório usa inteligência artificial ou processamento automatizado para análises de risco do cliente? (Sim = RIPD é recomendada)

**Conclusão:** Se 2+ respostas são Sim, RIPD é obrigatória. Se 0-1 Sim, é recomendada (boa prática).

---

## Step 4: Prazos de retenção — reconciliar Estatuto OAB + LGPD

Produza tabela de retenção final:

```markdown
## 2. Política de Retenção de Dados

| Tipo de dado | Razão da retenção | Base legal | Prazo | Após prazo: eliminar ou arquivar? |
|---|---|---|---|---|
| Dados de cliente (gerais) | Obrigação legal (Estatuto OAB) + defesa de reclamações disciplinares | Art. 7º II LGPD + Art. 1º Estatuto OAB | 5 anos após fim do mandato | Eliminar (destruir com certificado) |
| Dados sensíveis (saúde, criminal, familia) | Mesmas razões, risco reputacional maior | Art. 7º II + Art. 11 LGPD | 5 anos após fim do mandato | Eliminar com segurança (criptografia antes de destruir) |
| Dados de menores | Proteção especial, possíveis litígios futuros | Art. 7º II + Art. 14 LGPD | 5 anos após maioridade OU 5 anos após fim do mandato, o que for maior | Eliminar com cuidado especial |
| Dados de RH (funcionários) | Obrigação tributária (CLT + imposto) | Art. 7º II (lei) | 10 anos (prazo tributário) | Arquivar seguro (criptografia) após período ativo |
| Dados de cobrança / faturamento | Obrigação contábil-fiscal | Art. 7º II (lei) | 5 anos (Lei 8.180 — Código Tributário) | Arquivar seguro |
| Backups de dados | Recuperação de desastres | N/A (não é "retenção" mas cópia de segurança) | Máximo 6 meses além da data de eliminação prevista | Destruir backups após prazo |
```

**Nota importante:** Após expiração do prazo, o tratamento deve ser encerrado conforme LGPD Arts. 15-16, ressalvadas as hipóteses legais de conservação; manter dados além do necessário também tensiona o princípio da necessidade. Documentar processo de eliminação (trituração de papel, apagamento seguro de dados digitais com certificado). [verified: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm]

---

## Step 5: RIPD — se necessária, estrutura básica

Se a avaliação acima indica RIPD obrigatória, aqui está template mínimo:

```markdown
## Relatório de Impacto à Proteção de Dados Pessoais (RIPD)

### Descrição do tratamento
O [Escritório de Advocacia X] trata dados pessoais de clientes, partes adversas, testemunhas e funcionários no exercício de sua atividade de prestação de serviços jurídicos. [Descrever o escopo: litigação, consultoria, ambos.]

### Base legal
Consentimento [__] | Contrato [_X_] | Obrigação legal [_X_] | Legítimo interesse [__] | Proteção de vida [__] | Tutela da saúde [__] | Pesquisa [__] | Proteção do crédito [__]

Base principal: **Execução de contrato de prestação de serviços jurídicos (Art. 7º, V LGPD)** e **obrigação legal sob Estatuto OAB e CPC (Art. 7º, II LGPD)**.

### Dados processados
- [Categoria 1: nomes, CPFs, e-mails de clientes — necessários para execução do mandato]
- [Categoria 2: dados sensíveis — [tipo] — cuja revelação ao advogado é essencial para defesa adequada do cliente]
- [Categoria N: dados de funcionários — processados sob relação de trabalho — necessários para folha, HR, timekeeping]

### Riscos às liberdades civis e direitos fundamentais

| Risco | Probabilidade | Impacto | Mitigation |
|---|---|---|---|
| Vazamento de dados sensíveis (ex.: saúde, criminal, família) se servidor é hackeado | Média | Alto — violação de privacidade, dano reputacional ao cliente | Criptografia em repouso + controle de acesso + seguro de responsabilidade |
| Roubo de laptop com autos | Baixa | Alto — mesmos danos | Criptografia de disco + senhas fortes + seguro contra roubo |
| Funcionário lê dados de cliente fora de contexto (acesso desnecessário) | Média | Médio — violação de sigilo profissional | Controle de acesso por permissão (não todos têm acesso a todos os clientes) + treinamento |
| Retenção além do necessário (ex.: guardar 10 anos em vez de 5) | Alta | Baixo — não há "dano" direto mas viola LGPD | Política de retenção clara + calendário de eliminação + auditoria anual |
| Subprocessador (fornecedor de cloud, CLM) não tem DPA ou descumpre segurança | Média | Alto — responsabilidade solidária do escritório | DPA assinado com ALL fornecedores + auditoria de SOC 2 / LGPD compliance anual |

### Medidas de segurança (Art. 46 LGPD)
- [X] Criptografia de dados em repouso (AES-256 ou equivalente)
- [X] Criptografia em trânsito (TLS 1.2+)
- [X] Controle de acesso por autenticação multifator (MFA) em sistemas críticos
- [X] Logs de auditoria de acesso a dados sensíveis
- [X] Segmentação de dados por cliente (papeletas de cliente X não vê dados de cliente Y)
- [X] Política de senha forte + rotação
- [X] Treinamento anual de funcionários em sigilo profissional + LGPD
- [X] Procedimento de eliminação segura de dados (trituração + certificado para papel; apagamento criptográfico para digital)
- [X] Seguro de responsabilidade civil por vazamento

### Direitos do titular (Art. 18 LGPD)
Cliente pode exercer:
- **Acesso:** pedido de cópia de todos os dados que o escritório tem sobre ele — prazo: 15 dias
- **Exclusão:** em casos limitados (consentimento revogado, dados não mais necessários) — prazo: 15 dias
- **Correção:** se dados estão incorretos (ex.: endereço desatualizado)
- **Portabilidade:** receber dados em formato estruturado
- **Objeção a legítimo interesse:** se discorda da base de tratamento

Procedimento: cliente envia solicitação por e-mail assinado ao [DPO ou responsável legal]. Escritório verifica identidade, coleta dados, responde em 15 dias (prorrogável por igual período com justificativa).

### Conclusão
Risco **[ALTO / MÉDIO / BAIXO]** após implementação das medidas acima. Recomendações:
- [Medida 1]
- [Medida 2]
```

---

## Step 6: Plano de resposta a incidente de dados (Art. 48 LGPD)

Produza plano de incidente:

```markdown
## 3. Plano de Resposta a Incidente de Dados

### Definição de incidente
Incidente é qualquer acesso, divulgação, alteração ou destruição não autorizada de dados pessoais (intentional ou acidental).

**Exemplos:**
- Servidor hackeado, arquivos criptografados por ransomware.
- Laptop com autos roubado.
- Funcionário envia dados de cliente para e-mail pessoal por engano.
- Drive foi compartilhado publicamente por erro.
- Fornecedor de cloud descumpre segurança e há vazamento.

### Detecção (0h)
- **Quem detecta?** Qualquer funcionário, cliente, fornecedor.
- **Como reporta?** Slack privado ao DPO / responsável de segurança, ou e-mail dedicado: [email de incidente].
- **Registro?** Abrir "Incidente #[número]" em [sistema de tickets — ex.: Jira, Asana, manualmente em doc].

### Investigação (0-24h)
- **DPO / responsável de segurança investiga:**
  - O que vazou? (qual dado, quanto, para quem?)
  - Por que? (erro de configuração, roubo, hacking, erro humano?)
  - Quando começou? (data de início, data de detecção).
  - Scope: quantos clientes afetados? Quantos registros?
- **Documentar tudo** — será base para comunicação e possível investigação regulatória.

### Comunicação à ANPD (máximo 72h)

Se incidente causa **risco aos direitos fundamentais** (dados sensíveis, muitos registros, alta probabilidade de dano):
- **Quem comunica?** GC + DPO, por formulário ANPD (gov.br/anpd — link de notificação).
- **O quê informar?**
  - Descrição do incidente.
  - Dados afetados.
  - Número de titulares afetados.
  - Medidas de mitigação já tomadas.
  - Contato do DPO.
- **Prazo:** 72 horas da detecção (lei exige "sem demora").

**Risco baixo?** (ex.: Arquivo confidencial visto por 1 pessoa autorizada por engano, sem chance de re-divulgação.) Não precisa notificar ANPD, mas documente a decisão.

### Comunicação ao cliente (máximo 72h)

Se afeta dados do cliente:
- **Quem comunica?** Sócio responsável do caso (representante do escritório), por e-mail assinado (não genérico).
- **O quê informar?**
  - Que houve incidente (detalhe controlado, sem alarmar).
  - Que dados do cliente foram potencialmente expostos.
  - Que medidas o escritório tomou para remediar.
  - Que recomendações o cliente deve seguir (ex.: monitorar cartão de crédito, trocar senhas).
  - Contato para dúvidas.
- **Exemplo de e-mail:**
```
Prezado [Cliente],

[Data], detectamos um incidente de segurança envolvendo nossos sistemas. Por transparência e dever profissional, informamos que seus dados pessoais (nome, CPF, número de contato) PODEM ter sido afetados em [escopo mínimo — ex: "acesso não autorizado a pasta compartilhada por [duração]"].

Investigamos e [tomamos medida X — ex.: "revogamos acesso, forçamos reset de senhas, ativamos 2FA"].

Recomendamos que você: [monitore cartão de crédito nos próximos 3 meses / troque senha de qualquer serviço que use o mesmo e-mail / considere congelar crédito].

Continuamos disponíveis para dúvidas. Seu caso continua sendo nossa prioridade.

[Assinatura]
```

### Remediação e follow-up (1-30 dias)

- **Tecnicamente:**
  - Patches / atualizações de segurança.
  - Rotação de chaves de criptografia.
  - Investigação forense (se hacking).
  - Teste de penetração adicional.
- **Processos:**
  - Revisão de controles de acesso.
  - Treinamento reforçado de funcionários.
  - Atualização de política de segurança.
- **Documentação:**
  - Relatório de incidente completo + lições aprendidas.
  - Ações corretivas + responsáveis + deadlines.
  - Post-mortem com time de segurança.

### Governança
- **Responsável:** [Nome, cargo, e-mail, telefone de emergência]
- **Escalação:** [Sócio sênior, GC, conselho, conforme severidade]
- **Teste do plano:** Simulação anual (tabletop exercise) com times envolvidas.
- **Revisão:** Anual ou após incidente real.
```

---

## Nota: Sigilo profissional NÃO substitui conformidade LGPD

Errado: "Somos advogados, sigilo profissional cobre tudo, LGPD não se aplica."

Correto: Sigilo profissional protege CONTRA DIVULGAÇÃO involuntária (apreensão de arquivos, interceptação). LGPD governa como o escritório PROCESSA e RETÉM dados — são camadas complementares.

- **LGPD exige:** base legal clara, medidas de segurança, direito do titular, retenção mínima, notificação de incidente.
- **Sigilo exige:** proteção contra apreensão, confidencialidade mesmo após término.

Ambas as obrigações coexistem.

---

## What this skill does NOT do

- It does not create a full Data Protection Officer (DPO) role or install one — that's a hiring/governance decision.
- It does not perform a real security audit (penetration test, vulnerability scan) — it maps policy, not technical controls.
- It does not advise tax or employment law changes (retenção de RH data tem regras tributárias separadas).
- It does not replace consultation with specialized LGPD lawyer if the firm is under ANPD investigation or has had a real breach.
- It does not address client-side LGPD obligations (that's the firm's client's problem; the firm is responsible for firm-side compliance only).

---

## Consequential-action gate

**Before presenting findings to the firm's sócio/GC:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`. If the Role is Non-lawyer:

> This is a compliance audit of the firm's own data practices — it has legal and operational consequences. Have a licensed attorney review the findings before the firm acts on them. Here's a brief for them:
>
> **Key gaps identified:**
> - [If no written policy: "No written LGPD policy — creates defense burden if ANPD investigates."]
> - [If no RIPD and should have one: "RIPD is recommended or (if criteria met) mandatory — missing RIPD is a gap."]
> - [If no incident response plan: "No formal plan — violates Art. 48 LGPD requirement to respond within 72h."]
> - [If files retained beyond 5 years without justification: "Overretention violates LGPD minimization principle."]
>
> **Scope of work:** Have the attorney confirm the findings, help the firm prioritize (which gaps are P0), and oversee implementation of remediation.

Do not proceed with firm-wide rollout without attorney sign-off.

---

## Close with the next-steps decision tree

**What next? Pick one and I'll help you build it out:**

1. **Create written LGPD policy** — I'll draft a "Data Protection Policy" for the firm covering collection, retention, rights, incident response. Non-technical, suitable for all staff.
2. **RIPD — if necessary** — I'll expand the template above into a full RIPD document for sign-off by DPO/GC.
3. **Audit compliance of current vendors** — I'll create a vendor questionnaire (DPA check, security certifications, incident procedures) you can send to [cloud provider, CLM, contabilidade, etc.].
4. **Incident response playbook — detailed version** — I'll create a step-by-step runbook (who calls whom, on-call rotation, communication templates, forensics checklist).
5. **Something else** — Tell me what you'd prioritize.

**One question I'd ask that isn't in the checklist:** Does the firm currently do annual training on sigilo profissional + LGPD for all staff, including para-professionals? If not, that's a low-cost, high-impact gap to fill — a single incident caused by employee carelessness is the most common vector, and training reduces it significantly.
