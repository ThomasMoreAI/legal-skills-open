# direito-familiar-imobiliario

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made for Claude Code](https://img.shields.io/badge/Made_for-Claude_Code-d97757)](https://docs.claude.com/en/docs/claude-code)
[![Skill](https://img.shields.io/badge/Type-Skill-6a9bcc)](https://docs.claude.com/en/docs/agents/skills)
[![Language](https://img.shields.io/badge/Language-pt--BR-009b3a)](#)
[![Jurisdiction](https://img.shields.io/badge/Jurisdição-🇧🇷_Brasil-ffdf00)](#)
[![Legislation](https://img.shields.io/badge/Legislação-Maio%2F2026-blue)](references/legislacao.md)
[![GitHub last commit](https://img.shields.io/github/last-commit/maiconfuhr/direito-familiar-imobiliario)](https://github.com/maiconfuhr/direito-familiar-imobiliario/commits/main)
[![GitHub stars](https://img.shields.io/github/stars/maiconfuhr/direito-familiar-imobiliario?style=social)](https://github.com/maiconfuhr/direito-familiar-imobiliario/stargazers)

> Skill para Claude Code que orienta pessoas leigas em casos brasileiros de **direito imobiliário** (regularização, usucapião, REURB, retificação de matrícula) e **direito de família e sucessões** (divórcio, partilha, meação, inventário, herança, ITCMD).

Legislação atualizada até **maio/2026** — inclui Resolução CNJ 571/2024 (inventário e divórcio extrajudicial com menores e testamento), Provimento CNJ 149/2023 (Código Nacional de Normas), LC 227/2026 (ITCMD progressivo), Lei 14.711/2023 (Marco Legal das Garantias), Lei 14.620/2023 (REURB/MCMV) e Lei 14.382/2022 (SERP).

---

## ⚠️ AVISO LEGAL IMPORTANTE

**Esta skill não é, e não substitui, aconselhamento jurídico profissional.**

- **Não é parecer, não é peça processual, não é representação legal.** É uma ferramenta de orientação para pessoas leigas se prepararem melhor antes e durante o trabalho com um advogado.
- **Conteúdo educativo e organizativo.** Ajuda a entender procedimentos, separar documentos, dimensionar custos e fazer perguntas direcionadas.
- **Procure sempre um(a) advogado(a) inscrito(a) na OAB** para conduzir seu caso. Em situações de baixa renda, recorra à Defensoria Pública Estadual.
- **Legislação muda.** A base é maio/2026. Mudanças posteriores podem alterar regras, alíquotas e procedimentos. Sempre confirme com profissional atualizado.
- **Estimativas de custos são FAIXAS.** Valores reais variam por município, estado, cartório e perfil do caso.
- **Os autores e contribuidores não se responsabilizam** pelo uso, decisões tomadas a partir do conteúdo, ou eventuais perdas decorrentes. Use por sua conta e risco.
- **Casos de violência doméstica** exigem atendimento especializado imediato. Procure DEAM, Defensoria Pública ou denuncie pelo 180.

---

## Por que esta skill existe

Pesquisamos o ecossistema de skills jurídicas para Claude Code em maio/2026 e identificamos um gap importante: existem skills para advogados (geração de peças, jurisprudência), existem produtos comerciais e há MCPs de infraestrutura (DataJud, jurisprudência), mas **não havia skill para pessoas leigas** orientando casos práticos sob direito brasileiro.

Isso é um problema real: alguém que está num divórcio com filhos, um inventário aberto após perda de um parente, ou tentando regularizar um imóvel antigo precisa **chegar preparado ao escritório de advocacia** — entender o que vai acontecer, separar documentos certos, dimensionar custos, fazer perguntas inteligentes. Sem esse preparo, paga-se mais, demora mais e se aceita acordos piores.

Esta skill foi construída pra preencher esse gap.

---

## O que cobre

### 🏠 Direito Imobiliário
- Regularização de imóvel sem matrícula
- Retificação de matrícula (área, confrontantes)
- Averbação de construção (habite-se, CND)
- Usucapião — extrajudicial (Prov. CNJ 149/2023, arts. 440-460) e judicial
- REURB-S e REURB-E (Lei 13.465/2017 + Lei 14.620/2023)
- Adjudicação compulsória — extrajudicial (Prov. CNJ 150/2023, hoje no CNN) e judicial
- Particularidades de imóvel rural (CCIR, ITR, CAR, georreferenciamento)
- Imóvel financiado com alienação fiduciária

### 👨‍👩‍👧 Direito de Família
- Regimes de bens (comunhão parcial, universal, separação total, participação final, separação obrigatória)
- **Meação vs. herança** — diferença crítica
- Divórcio extrajudicial (com menores via Res. CNJ 571/2024), consensual judicial, litigioso
- Partilha de bens (incluindo imóveis financiados, empresas, previdência privada)
- Guarda compartilhada (Lei 13.058/2014) e visitação
- Pensão alimentícia
- União estável (dissolução)
- Casos sensíveis (violência doméstica, alienação parental, bens no exterior)

### ⚱️ Sucessões
- Vocação hereditária (art. 1.829 CC) — quem herda
- Legítima e parte disponível
- Inventário extrajudicial (com menores e testamento via Res. CNJ 571/2024)
- Inventário judicial (arrolamento sumário, comum, comum)
- ITCMD — alíquotas por UF + impacto da LC 227/2026 (progressividade obrigatória a partir de 2027)
- Testamento (público, cerrado, particular)
- Renúncia (abdicativa vs. translativa)
- Cessão de direitos hereditários
- Partilha em vida e planejamento sucessório
- Casos especiais (companheiro, herdeiro desaparecido, sonegados, herança no exterior)

### 💰 Custos e tributos
- ITBI (municipal, 2-3% típico)
- ITCMD (estadual, 2-8% — tabela por UF)
- Emolumentos cartoriais (tabela TJ estadual)
- Custas judiciais
- Honorários advocatícios (faixas referenciais)
- Custos profissionais (engenheiro, contador, georreferenciamento)
- Tributos relacionados (IPTU, ITR, IR sobre ganho de capital)
- **Calculadora interativa** em Python

### 📚 Referência rápida
- Glossário com ~150 termos técnicos em linguagem clara
- Quadro consolidado da legislação vigente em maio/2026
- Checklists de documentos por tipo de caso
- 75+ perguntas direcionadas para o(a) advogado(a)
- Red flags (sinais de alerta no caso, no profissional, na contraparte)

---

## Instalação

### Pré-requisito
Claude Code (`claude-code`) instalado. Veja [docs.claude.com](https://docs.claude.com/en/docs/claude-code).

### Instalação manual (recomendada)

```bash
git clone https://github.com/maiconfuhr/direito-familiar-imobiliario.git \
  ~/.claude/skills/direito-familiar-imobiliario
```

Isso instala a skill no seu diretório global de skills. Ela será carregada automaticamente em qualquer sessão do Claude Code.

### Verificação

Abra uma nova sessão do Claude Code e pergunte:

> "Comprei um imóvel há 20 anos sem escritura e quero regularizar"

Ou:

> "Como funciona inventário extrajudicial com filho menor?"

A skill `direito-familiar-imobiliario` deve disparar automaticamente.

---

## Como usar

A skill foi desenhada pra **disparar sozinha** quando você (ou alguém na sessão) mencionar termos como:

- "regularizar imóvel", "matrícula", "escritura"
- "divórcio", "separação", "partilha", "meação", "regime de bens"
- "inventário", "herança", "ITCMD", "testamento"
- "usucapião", "REURB", "ITBI"

Ou descrever situações sem usar termos técnicos:

- "minha mãe morreu e deixou uma casa"
- "vou me separar e a gente tem uma chácara"
- "comprei um terreno sem escritura há 20 anos"
- "o imóvel está no nome da minha avó falecida"

### Workflow

A skill executa um workflow de **8 passos**:

1. **Escuta sem jargão** — peça pro usuário contar a história naturalmente
2. **Triagem por área** — identifica imobiliário, família ou sucessões (ou combinação)
3. **Diagnóstico em linguagem comum** — traduz o caso
4. **Procedimento esperado** — caminho mais provável, prazo, profissionais envolvidos
5. **Checklist de documentos** — específico do caso
6. **Estimativa de custos** — via referência ou calculadora Python interativa
7. **Perguntas pro advogado** — roteiro direcionado
8. **Red flags** — verificação de sinais de alerta

### Calculadora de custos

```bash
python ~/.claude/skills/direito-familiar-imobiliario/scripts/calc_custos.py
```

Menu interativo cobre: compra/venda, doação, inventário (extrajudicial/judicial), divórcio (3 modalidades), usucapião, retificação de matrícula, REURB-E.

---

## Estrutura

```
direito-familiar-imobiliario/
├── SKILL.md                              # Triagem + workflow (entry point)
├── README.md                             # Este arquivo
├── LICENSE                               # MIT
├── references/
│   ├── imobiliario.md                    # Regularização, usucapião, REURB
│   ├── familia.md                        # Divórcio, regime de bens, partilha
│   ├── sucessoes.md                      # Inventário, herança, ITCMD
│   ├── custos-tributos.md                # ITBI, ITCMD, emolumentos
│   ├── legislacao.md                     # Quadro consolidado maio/2026
│   └── glossario.md                      # ~150 termos técnicos
├── assets/
│   ├── checklists.md                     # Documentos por tipo de caso
│   ├── perguntas-advogado.md             # ~75 perguntas direcionadas
│   └── red-flags.md                      # Sinais de alerta
└── scripts/
    └── calc_custos.py                    # Calculadora interativa
```

---

## Contribuindo

Contribuições são muito bem-vindas, especialmente:

- **Atualizações legislativas** — quando leis mudarem ou jurisprudência consolidar nova interpretação
- **Particularidades estaduais** — ITCMD, normas de CGJ, tabelas de emolumentos
- **Correções factuais** — qualquer erro identificado
- **Novos checklists** — casos não cobertos
- **Traduções para inglês/espanhol** — se útil para diáspora brasileira

Pra contribuir:

1. Faça fork do repositório
2. Crie uma branch (`git checkout -b atualizacao-itcmd-sp`)
3. Commit com mensagem clara (`git commit -m "Atualiza alíquota ITCMD SP após Lei XYZ/2027"`)
4. **Sempre cite a fonte oficial** da alteração (planalto.gov.br, cnj.jus.br, lei estadual, etc.)
5. Abra Pull Request

Atualizações puramente factuais (lei mudou, alíquota nova, novo provimento) são aceitas sem maiores discussões. Mudanças de abordagem, escopo ou opinião jurídica passam por discussão prévia em Issue.

### Diretrizes

- **Linguagem clara**: a skill é para leigos. Cada termo técnico explicado entre parênteses na primeira ocorrência.
- **Citar fontes**: leis com link pro planalto.gov.br; provimentos pro atos.cnj.jus.br; jurisprudência pro STF/STJ.
- **Custos sempre como FAIXA**, nunca valor exato.
- **Não dar conselho jurídico definitivo**: a skill orienta, não decide.

---

## Roadmap

Ideias bem-vindas em Issues. Algumas direções:

- [ ] Integração com [mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) para consulta DataJud em tempo real
- [ ] Integração com [brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server) para jurisprudência
- [ ] Modelos de petição (sob orientação de advogados contribuidores)
- [ ] Calculadora de pensão alimentícia
- [ ] Calculadora de partilha por regime de bens
- [ ] Versão simplificada para crianças/adolescentes (entender divórcio dos pais, herança)
- [ ] Versão para advogados iniciantes (com mais profundidade técnica)
- [ ] Tradução para espanhol (uso em diáspora brasileira)

---

## Skills/MCPs relacionados

| Recurso | Para quê |
|---|---|
| [mcp-brasil](https://github.com/Mcp-Brasil/mcp-brasil) | MCP server com 533 tools — DataJud, SPU, BrasilAPI |
| [brlaw_mcp_server](https://github.com/pdmtt/brlaw_mcp_server) | MCP server pra busca de jurisprudência STF/STJ/TST |
| [Chat Jurídico](https://chatjuridico.com.br/claude/skills/) | Skills comerciais para advogados (geração de peças) |
| [anthropic-skills](https://github.com/anthropics/skills) | Skills oficiais Anthropic |

Esta skill é complementar — orienta o cliente leigo; aquelas atendem o profissional.

---

## Créditos

Criada por **Maicon Fuhr** ([@maiconfuhr](https://github.com/maiconfuhr)).

Construída com auxílio do Claude Code (Anthropic) usando a skill `skill-creator`, com pesquisa de legislação verificada em fontes oficiais (planalto.gov.br, atos.cnj.jus.br) em maio/2026.

Agradecimento à comunidade brasileira de LegalTech, à OAB, ao CNJ e a todos que mantêm a legislação acessível publicamente.

---

## Licença

MIT — ver [LICENSE](LICENSE).

Resumindo: use livremente, modifique livremente, compartilhe livremente. Mantenha o crédito original e o aviso legal.
