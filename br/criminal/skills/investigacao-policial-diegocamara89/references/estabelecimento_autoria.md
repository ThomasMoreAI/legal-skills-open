# Estabelecimento de Autoria — Modelo de Convergencia

Referencia para determinar a autoria de crimes digitais/fraudes usando o modelo de convergencia de fontes independentes.

## Sumario

1. [Principio da Convergencia](#1-principio-da-convergencia)
2. [Fontes de Prova para Autoria](#2-fontes-de-prova)
3. [Modelo de Convergencia](#3-modelo-de-convergencia)
4. [Criterios para Operador Direto](#4-operador-direto)
5. [Criterios para Laranja Ativo](#5-laranja-ativo)
6. [Checklist Pre-Indiciamento](#6-checklist-pre-indiciamento)
7. [Armadilhas na Atribuicao de Autoria](#7-armadilhas)

---

## 1. Principio da Convergencia

Autoria em crimes digitais **nao se prova com uma unica fonte**. Uma unica evidencia (um IP, um cadastro, um acesso) pode ter explicacoes alternativas: NAT compartilhado, WiFi publica, conta hackeada, intermediario.

A autoria e estabelecida quando **multiplas fontes independentes** apontam para o **mesmo individuo** de forma consistente. Quanto mais fontes convergem, maior a confianca.

| Fontes convergentes | Nivel de confianca |
|--------------------|-------------------|
| 1 fonte | Insuficiente — apenas indicio |
| 2 fontes | Indicio moderado — necessita corroboracao |
| 3+ fontes | Indicio robusto — base solida para indiciamento |
| 4+ fontes com biometria | Muito forte — convergencia plena |

---

## 2. Fontes de Prova para Autoria

Cada fonte fornece um tipo de dado que, isoladamente, indica quem estava no controle de um sistema naquele momento:

| Fonte | Dado Obtido | O que Prova |
|-------|-------------|-------------|
| Meta/WhatsApp | IP + horario de acesso a conta usada no golpe | Quem operava o WhatsApp no momento da fraude |
| Banco | IP + horario da transacao fraudulenta | Quem operava a conta bancaria no momento do Pix/TED |
| TJRN/PJe | IP + horario da consulta processual | Quem acessou o processo judicial (fonte de dados para o golpe) |
| Operadora | Titular do IP + IMEI | Quem era o assinante da conexao de internet |
| Operadora | Linhas vinculadas ao IMEI | Quais linhas telefonicas usaram o mesmo aparelho |
| Banco | Selfie biometrica na abertura da conta | Quem fisicamente abriu a conta destino |
| Banco | Historico de reclamacoes | Se o titular contestou o uso da conta |
| Google/Microsoft | IP + telefone vinculado ao email | Quem controlava o email usado na fraude |

---

## 3. Modelo de Convergencia

O modelo funciona como uma piramide invertida: cada fonte independente aponta para o mesmo individuo por caminhos diferentes.

```
Fonte 1: IP do WhatsApp → operadora → IMEI → linha → [NOME]
Fonte 2: IP do banco    → operadora → IMEI → linha → [NOME]
Fonte 3: IP do TJRN     → operadora → IMEI → linha → [NOME]
Fonte 4: Selfie biometrica na abertura da conta   → [NOME]
Fonte 5: Linha pos-paga antiga com registro       → [NOME]
```

**Se todas (ou a maioria) das fontes convergem no mesmo [NOME]**: indicio robusto de autoria.

**Se ha divergencia** (ex: Fonte 1 aponta para A, Fonte 2 aponta para B):
- Investigar se ha mais de um autor (organizacao criminosa)
- Verificar se um dos nomes e "laranja"
- Verificar se houve troca de chip/aparelho durante o periodo

---

## 4. Criterios para Operador Direto

O individuo e considerado **operador direto** quando:

1. O IP no momento exato do crime (comunicacao WhatsApp, transacao bancaria, acesso ao PJe) vincula **inequivocamente** a pessoa ao terminal
2. O IMEI do aparelho esta vinculado a uma linha registrada em nome da pessoa
3. Nao ha indicios de que o aparelho/linha estivesse em posse de terceiro

### Evidencias que reforcam

- Mesmo IP em multiplas fontes no mesmo periodo
- Modelo do aparelho consistente entre fontes
- Padrao de uso (horarios, frequencia) compativel com uma unica pessoa
- Geolocalizacao (ERBs) compativel com endereco conhecido do suspeito

---

## 5. Criterios para Laranja Ativo

"Laranja" e a pessoa em cujo nome a conta bancaria destino esta registrada, mas que alega nao ter participado da fraude.

O laranja e considerado **ativo** (e portanto passivel de indiciamento) quando:

| Criterio | Verificacao |
|----------|------------|
| Abriu a conta pessoalmente | Dados de abertura no banco confirmam |
| Forneceu selfie biometrica | Banco tem a selfie armazenada |
| Manteve a conta ativa | Conta nao foi encerrada ou bloqueada pelo titular |
| Nunca reclamou ao banco | Nao ha registro de contestacao, reclamacao ou pedido de bloqueio |

**Raciocinio**: mesmo que o titular alegue que nao usava a conta no momento da fraude, ao nao informar ao banco sobre possivel furto/extravio, presume-se conivencia ou consentimento.

### Evidencias que reforcam o "laranja ativo"

- Conta aberta recentemente (pouco antes da fraude)
- Multiplas fraudes usando a mesma conta
- Titular tem antecedentes por crimes semelhantes
- Titular tem vinculos (familiares, empresariais) com o operador direto

### Evidencias que enfraquecem (possivel laranja passivo/vitima)

- Titular registrou BO sobre furto/perda de documentos antes da fraude
- Titular solicitou bloqueio da conta ao banco antes da fraude ser investigada
- Ha indicio de coacao ou engano (ex: "emprego falso" que pedia conta bancaria)

---

## 6. Checklist Pre-Indiciamento

Antes de concluir sobre a autoria e recomendar indiciamento, verificar **obrigatoriamente**:

- [ ] Convergencia de pelo menos 3 fontes independentes apontando para o mesmo individuo
- [ ] Consulta a bancos de dados policiais (INFOSEG, base estadual)
- [ ] Verificacao de antecedentes e outros BOs envolvendo o suspeito
- [ ] Solicitacao ao banco do historico de reclamacoes/bloqueios da conta
- [ ] Verificacao de documentos de abertura da conta (selfie, CPF)
- [ ] Analise se o suspeito e operador direto ou laranja
- [ ] Descarte de hipoteses alternativas (NAT, WiFi publica, aparelho compartilhado)
- [ ] Documentacao de cada convergencia com fonte, timestamp e metodo

---

## 7. Armadilhas na Atribuicao de Autoria

### 7.1 — Acesso ao PJe ≠ Autoria do Golpe

O terceiro identificado no acesso ao processo judicial **nem sempre e o fraudador**. Pode ser:
- Um intermediario que vendeu os dados
- Um funcionario de escritorio que acessou legitimamente
- Alguem que recebeu login/senha de terceiro

**Regra**: nunca indiciar com base exclusivamente no acesso ao PJe. Sempre cruzar com outras fontes.

### 7.2 — IPv4 sem Porta ≠ Individuo

Um IPv4 sem porta logica pode estar sendo compartilhado por centenas de usuarios via NAT. Atribuir autoria com base em IPv4 sem porta e arriscado.

### 7.3 — Cadastro da Linha ≠ Posse do Aparelho

A linha pode estar em nome de A, mas o aparelho (IMEI) pode estar em posse de B. Sempre verificar se ha cruzamento entre titular da linha e usuario do IMEI.

### 7.4 — Conta Bancaria em Nome de A ≠ A Operou

A pode ter aberto a conta a pedido de terceiro (emprego falso, favor familiar, coacao). Verificar os criterios de laranja ativo vs. passivo antes de concluir.

### 7.5 — Cuidado com Wifi Publica e Corporativa

IPs de redes corporativas ou publicas (shopping, aeroporto, coworking) podem gerar falsos positivos. Verificar se o IP corresponde a:
- Provedor residencial (mais confiavel)
- Rede corporativa (pode ser qualquer funcionario)
- WiFi publica (qualquer pessoa)
