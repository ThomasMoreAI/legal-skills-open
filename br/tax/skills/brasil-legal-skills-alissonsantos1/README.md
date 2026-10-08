<div align="center">

# 🇧🇷 Brasil Legal Skills

### O seu advogado, contador e consultor tributário com IA — disponível 24h, em português, sem cobrar por hora.

[![License: MIT](https://img.shields.io/github/license/AlissonSantos1/brasil-legal-skills?style=for-the-badge&color=yellow)](LICENSE)
[![Release](https://img.shields.io/github/v/release/AlissonSantos1/brasil-legal-skills?style=for-the-badge&color=brightgreen)](https://github.com/AlissonSantos1/brasil-legal-skills/releases)
[![Stars](https://img.shields.io/github/stars/AlissonSantos1/brasil-legal-skills?style=for-the-badge&color=gold)](https://github.com/AlissonSantos1/brasil-legal-skills/stargazers)
[![Forks](https://img.shields.io/github/forks/AlissonSantos1/brasil-legal-skills?style=for-the-badge&color=blue)](https://github.com/AlissonSantos1/brasil-legal-skills/forks)
[![Modules](https://img.shields.io/badge/módulos-9-blue?style=for-the-badge)]()
[![Scripts](https://img.shields.io/badge/calculadoras-13+-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/idioma-Português-009c3b?style=for-the-badge)]()
[![Made in Brazil](https://img.shields.io/badge/feito_no-Brasil-002776?style=for-the-badge)]()

**A skill mais completa de Direito Brasileiro para Claude Code.**
IRPF · Simples Nacional · CLT · Abertura de Empresa · CDC · LGPD · Licitações · Previdência · e muito mais.

> ⚠️ **Aviso importante:** Esta skill é **consultiva e educativa**. Não substitui a consulta
> a um **advogado (OAB)**, **contador (CRC)** ou qualquer outro profissional habilitado.
> Use para orientação geral — decisões importantes exigem um especialista.

[🚀 Instalar agora](#-instalação) · [📖 Como usar](#-como-usar) · [🧮 Calculadoras](#-calculadoras-python) · [🤝 Contribuir](#-contribuindo)

</div>

---

## 😤 Você já passou por isso?

> *"Quanto vou pagar de imposto esse ano?"*
> *"Tenho direito a rescisão? Quanto recebo?"*
> *"Devo abrir MEI ou LTDA?"*
> *"Posso deduzir isso no IRPF?"*
> *"A empresa não devolveu meu dinheiro — o que faço?"*
> *"Quando posso me aposentar?"*

E aí você:
- ❌ Ligou pro contador — ele te cobrou consulta
- ❌ Perguntou no Google — achou 47 artigos contraditórios de 2019
- ❌ Perguntou pro ChatGPT — ele inventou lei que não existe
- ❌ Entrou no site da Receita Federal — saiu com mais dúvidas do que entrou

**Isso acaba aqui.**

---

## ✅ O que esta skill faz por você

```
"Calcula minha rescisão após 3 anos, salário de R$ 4.500"
→ Resposta completa em segundos. Com os cálculos certos. Baseada na CLT.

"Quanto pago de DAS no Simples Nacional com R$ 25k/mês no Anexo III?"
→ Alíquota efetiva calculada. Comparação com outros regimes. Pronto.

"Quais deduções posso usar no IRPF 2026?"
→ Lista completa, limites atualizados, comparação simplificado vs. completo.

"Tenho um produto com defeito — a empresa recusa trocar. O que faço?"
→ Passo a passo: SAC → consumidor.gov.br → Procon → JEC.

"Quando posso me aposentar? Qual regra é mais vantajosa pra mim?"
→ Análise das 4 regras de transição 2026 com base na sua situação.
```

---

## 📦 9 Módulos. Uma skill. Tudo em português.

### 🧾 IRPF — Declaração Guiada Passo a Passo
> *"Como se um contador estivesse do seu lado durante toda a declaração"*

- **Fluxo guiado em 8 etapas** — do zero ao envio
- Análise da **declaração pré-preenchida** — avalia o que está correto, o que falta e o que pode ser adicionado
- Tabela progressiva **2026 atualizada** (Lei 15.270/2025)
- Comparação automática: modelo **simplificado vs. completo**
- Novidades 2026: apostas esportivas, REVAR, investimentos exterior
- Destinação de até **3% do IR** para fundos sociais
- Parser de arquivos **.DBK** do programa oficial da Receita

### 🏛️ Tributário — Simples Nacional, MEI, Reforma Tributária e Split Payment
> *"Pare de pagar mais imposto do que deve — e entenda o que vem aí"*

- **`/reforma`** — Slash command completo: CBS, IBS, Imposto Seletivo e **Split Payment**
- **Split Payment** — Como o fracionamento automático afeta seu fluxo de caixa canal a canal (Pix, cartão, boleto) com simulador Python
- Cronograma 2026–2033 com impacto por regime (MEI, Simples, Presumido, Real)
- **PIS/COFINS atualizado** — mudanças na alíquota zero 2026
- **MEI:** como abrir CNPJ, escolher CNAE, emitir nota, obrigações
- **Simples Nacional** — 6 Anexos, cálculo de alíquota efetiva
- **Emissão de Nota Fiscal** — NF-e e NFS-e passo a passo
- Comparação de regimes: Simples × Presumido × Real

### 👷 Trabalhista — Da CLT à Aposentadoria
> *"Conheça seus direitos. Todos eles."*

- Calculadora de **salário líquido** (INSS + IR + VT)
- Calculadora **CLT vs PJ** — qual realmente compensa
- Calculadora de **valor por hora**
- Rescisão completa (sem justa causa, com justa causa, pedido, acordo)
- Calculadora de **INSS progressivo**
- Estimativa de **aposentadoria** com regras de transição 2026
- **Orientação jurídica trabalhista** — análise de provas, prazos, foro
- Referência: [CLT completa](https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm)

### 🏢 Societário — Abrir, Gerir e Proteger sua Empresa
> *"Do zero ao CNPJ, sem enrolação"*

- Análise: **vale a pena ter sócio?** (perguntas certas antes de decidir)
- Comparativo: MEI · SLU · LTDA · SA — qual escolher
- **Direitos e deveres dos sócios** — o que o Código Civil diz
- **Resolução de conflitos** — mediação, arbitragem ou judiciário
- **Geração de contratos** — Social, Acordo de Sócios, Distrato
- Cláusulas inteligentes: drag-along, tag-along, vesting, buy-or-sell
- **Alvarás e licenças** — checklist por tipo de negócio
- **Certidões negativas** — quais, onde e quando tirar

### 🛡️ Consumidor — CDC Completo
> *"Você tem mais direitos do que imagina"*

- Prazo de **arrependimento (7 dias)** — compras online
- **Garantia legal vs. contratual** — diferenças e como usar
- Como reclamar: SAC → consumidor.gov.br → Procon → JEC
- **Juizado Especial** — quando ir, o que levar, quanto custa
- Práticas abusivas — o que é ilegal e como denunciar

### 🔐 Direito Digital — LGPD e Marco Civil
> *"Proteja seus dados e os da sua empresa"*

- **Checklist de adequação LGPD** para empresas
- Bases legais, direitos dos titulares, multas (até R$ 50 mi por infração)
- **Cookies e consentimento** — como fazer corretamente
- Marco Civil — responsabilidade de plataformas, neutralidade da rede
- Resposta a **vazamentos de dados**

### 📄 Contratos — Modelos Práticos
> *"Contratos que protegem você de verdade"*

- **Locação** (residencial e comercial) — Lei 8.245/91
- **Prestação de Serviços** — com kill fee, rodadas de revisão, IP
- **Compra e Venda** — à vista, a prazo, com condição suspensiva
- Assinatura digital — ICP-Brasil, DocuSign, ClickSign

### 🏛️ Licitações — Como Vender para o Governo
> *"O maior comprador do Brasil quer comprar de você"*

- **Lei 14.133/2021** — Nova Lei de Licitações
- Passo a passo para o **primeiro pregão eletrônico**
- Cadastro no **SICAF** e **PNCP**
- Vantagens de **ME e EPP** em licitações (empate ficto, exclusividade)
- Checklist de habilitação — certidões, atestados, documentos

### 💊 Previdência Social — INSS e Aposentadoria
> *"Planeje sua aposentadoria agora, enquanto dá tempo"*

- **4 regras de transição 2026** — qual é mais vantajosa para você
- Cálculo da **contribuição INSS** (tabela progressiva)
- Estimativa de **valor da aposentadoria**
- Benefícios: auxílio-doença, salário-maternidade, pensão por morte, BPC
- [Regras oficiais INSS 2026](https://www.gov.br/inss/pt-br/direitos-e-deveres/aposentadorias/regras-de-aposentadorias)

---

## 🚀 Instalação

### Opção 1 — Clone direto (recomendado)
```bash
git clone https://github.com/AlissonSantos1/brasil-legal-skills.git \
  ~/.claude/skills/brasil-legal-skills
```
Reinicie o Claude Code. Pronto. ✅

### Opção 2 — Agent Skills CLI
```bash
npx agent-skills-cli add AlissonSantos1/brasil-legal-skills
```

> **Compatível com:** Claude Code · Cursor · OpenCode · Gemini CLI · Windsurf · Codex

---

## 💬 Como usar

Após instalar, basta perguntar naturalmente em português:

```
# IRPF guiado
"Quero declarar meu imposto de renda — me guia pelo processo"
"Tenho a declaração pré-preenchida, posso compartilhar os dados?"

# Trabalhista
"Fui demitido após 4 anos de empresa. Quanto tenho direito?"
"Vale mais a pena ser CLT de R$ 8.000 ou PJ de R$ 12.000?"
"Quando posso me aposentar? Sou homem, 45 anos, contribuindo há 22 anos"

# Tributário
"Como abro um MEI para desenvolvimento de software?"
"O que muda para minha empresa com a Reforma Tributária 2026?"
"Como o split payment vai afetar meu fluxo de caixa?"
/reforma split          # foco no split payment
/reforma cronograma     # linha do tempo 2026–2033
/reforma simples        # impacto específico para Simples Nacional

# Societário
"Quero abrir empresa com um sócio — o que devo incluir no contrato?"
"Meu sócio não está cumprindo o combinado — quais são meus direitos?"

# Consumidor
"Comprei um produto online há 5 dias e quero devolver"
"A empresa não me reembolsou — qual o próximo passo?"

# Previdência
"Qual regra de aposentadoria é melhor para mim?"
"Quanto preciso contribuir como autônomo para garantir minha aposentadoria?"
```

---

## 🧮 Calculadoras Python

Todas usam **stdlib apenas** — zero dependências, zero instalação.

```bash
# IRPF 2026 — tabela atualizada (Lei 15.270/2025)
python3 irpf/scripts/calcular_imposto.py \
  --renda 72000 --dependentes 2 --saude 12000 --inss 7500

# Rescisão CLT
python3 trabalhista/scripts/rescisao_calculator.py \
  --salario 4500 --meses 36 --tipo sem_justa_causa --fgts 15000

# Simples Nacional — alíquota efetiva
python3 tributario/scripts/simples_nacional.py \
  --receita 25000 --anexo 3

# CLT vs PJ — qual compensa mais
python3 trabalhista/scripts/clt_vs_pj.py \
  --clt 8000 --beneficios 1500 --pj 12000

# Estimativa de aposentadoria
python3 previdencia/scripts/aposentadoria_estimativa.py \
  --idade 45 --contribuicoes 22 --salario_medio 6000 --sexo masculino

# Split payment — impacto no fluxo de caixa (Reforma Tributária EC 132/2023)
python3 tributario/scripts/split_payment_simulator.py \
  --faturamento 50000 --regime simples --anexo 3 \
  --pix 60 --cartao 30 --boleto 5 --dinheiro 5
```

---

## 📚 Base Legislativa

| Área | Legislação |
|------|-----------|
| IRPF | Decreto 9.580/2018 · IN RFB 2.255/2025 · Lei 15.270/2025 |
| Simples Nacional | LC 123/2006 · Resoluções CGSN |
| Reforma Tributária | EC 132/2023 · LC 214/2025 (CBS/IBS/IS) |
| CLT | Decreto-Lei 5.452/1943 · Lei 13.467/2017 |
| Previdência | EC 103/2019 · Lei 8.213/1991 |
| Consumidor | Lei 8.078/1990 (CDC) |
| LGPD | Lei 13.709/2018 |
| Marco Civil | Lei 12.965/2014 |
| Licitações | Lei 14.133/2021 |
| Contratos | Lei 10.406/2002 (CC) |

---

## 🗺️ Roadmap

- [x] v1.0 — IRPF, Tributário, Trabalhista, Societário
- [x] v2.0 — CDC, LGPD, Contratos, Licitações, Previdência + declaração guiada + Reforma Tributária 2026
- [x] v2.1 — Calculadoras completas: CLT vs PJ, aposentadoria INSS, INSS progressivo, salário líquido
- [x] v2.2 — Parser de arquivo .DBK/.REC da Receita Federal (extrai dados da declaração)
- [x] v2.3 — Previdência avançada: planejamento de carreira contributiva, PGBL vs VGBL, estratégias por perfil
- [x] v3.0 — 5 slash commands especializados: `/irpf`, `/rescisao`, `/simples`, `/clt-pj`, `/aposentadoria`
- [x] v2.4 — `/reforma`: Reforma Tributária completa (CBS/IBS/IS) + Split Payment com simulador de fluxo de caixa por canal de pagamento (Pix, cartão, boleto) e projeção 2026–2033
- [ ] v4.0 — Ecossistema Brasil Legal (ver seção abaixo)

## 🔭 Além do v3 — Ecossistema Brasil Legal

### Novos plugins (projetos independentes)
- [ ] **`brasil-imobiliario-skills`** — Compra, venda, financiamento CEF, ITBI, registro, usucapião, REURB
- [ ] **`brasil-familiar-skills`** — Divórcio, pensão alimentícia, guarda, herança, inventário, ITCMD
- [ ] **`brasil-empreendedor-skills`** — Jornada MEI → ME → EPP: DAS, nota fiscal, limite, transição de regime
- [ ] **`brasil-concursos-skills`** — Servidor público: estabilidade, remuneração, progressão, PAD

### Ferramentas
- [ ] **CLI standalone** — Pacote npm/pip `brasil-legal` para rodar calculadoras sem Claude Code
- [ ] **Web app** — Interface leve (FastAPI + HTML) para democratizar acesso sem IDE
- [ ] **MCP Server** — Servidor MCP dedicado para integrar as calculadoras diretamente no Claude

### Integrações
- [ ] **Integração Receita Federal** — Conectar com API pública da RF para consulta de CNPJ, situação fiscal
- [ ] **Calendário tributário** — Alertas de vencimentos: DAS, DARF, DCTF, GFIP, obrigações mensais

---

## 🤝 Contribuindo

Este projeto nasceu de uma **lacuna real**: o Brasil tem a legislação tributária mais
complexa do mundo, e não existia uma skill completa de Direito Brasileiro para Claude Code.

**Como contribuir:**
- 🐛 Reporte erros de legislação via [Issues](https://github.com/AlissonSantos1/brasil-legal-skills/issues)
- 📖 Melhore a documentação e exemplos
- 🧮 Adicione novas calculadoras
- 🌎 Expanda módulos existentes
- ⭐ Deixe uma estrela se foi útil!

---

## ⚠️ Aviso Legal

Esta skill fornece **informações educativas e orientações gerais** baseadas na legislação
brasileira vigente. **Não substitui** a consulta a:

- **Advogado** habilitado na **OAB** — para questões jurídicas e processos
- **Contador** registrado no **CRC** — para declarações e planejamento tributário
- **Advogado Previdenciarista** — para aposentadoria e benefícios INSS
- Qualquer outro profissional habilitado para sua situação específica

As calculadoras fornecem **estimativas** — sempre valide com um profissional
e no programa oficial da Receita Federal.

---

<div align="center">

**Feito com ❤️ para a comunidade brasileira**

Se esta skill economizou seu tempo ou dinheiro, considere deixar uma ⭐

**Criado por Alisson Santos · [@AlissonSantos1](https://github.com/AlissonSantos1) · [LinkedIn](https://www.linkedin.com/in/alissonsantos1/) · Brasil · 2026**

*Copyright (c) 2026 Alisson Santos — Licença MIT · [Ver ATTRIBUTION.md](ATTRIBUTION.md)*

*Compartilhe com quem você conhece que precisa entender os próprios direitos — porque a lei vale para todo mundo. 🇧🇷*

</div>
