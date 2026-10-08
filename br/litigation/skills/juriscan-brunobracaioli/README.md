<p align="center">
  <img src="assets/banner.svg" alt="JuriScan — Análise forense de processos judiciais brasileiros" width="900"/>
</p>

<p align="center">
  <a href="https://github.com/brunobracaioli/juriscan/actions/workflows/ci.yml"><img src="https://github.com/brunobracaioli/juriscan/actions/workflows/ci.yml/badge.svg" alt="CI"/></a>
  <a href="#instalação"><img src="https://img.shields.io/badge/plug--and--play-Claude_Code_Skill-blue?style=for-the-badge" alt="Claude Code Skill"/></a>
  <img src="https://img.shields.io/badge/python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"/>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="MIT License"/></a>
</p>

<p align="center">
  Skill para <a href="https://claude.ai/code">Claude Code</a> de análise forense de processos judiciais brasileiros.<br/>
  Extrai PDFs, divide por peça processual, detecta contradições, calcula prazos CPC,<br/>
  rastreia argumentos entre instâncias e exporta para Obsidian.
</p>

---

## O que é?

Um processo judicial pode ter centenas de páginas: petição, contestação, réplica, sentença, recurso... Um advogado levaria dias lendo tudo, cruzando informações e procurando inconsistências.

O **JuriScan** faz isso em minutos. Você joga o PDF do processo e recebe:

- **Separação automática** de cada peça processual (27 tipos detectados)
- **Mapa de contradições** entre o que autor e réu disseram
- **Prazos calculados** com feriados forenses e recesso (CPC Art. 219-232)
- **Rastreamento de argumentos** — o que foi aceito, rejeitado ou reformado em cada instância
- **Nota de risco** do caso (processual, mérito e exposição monetária)
- **Vault Obsidian** navegável com links entre peças, leis e jurisprudência

### Para quem é (e para quem não é)

**Sweet spot:**

| Perfil | Ganho típico |
|---|---|
| **Advogado solo / small-firm (contencioso cível ou trabalhista)** | Lê um processo de 100-200 páginas em 5-10 min; recebe alertas de art. 942 CPC, Lei 14.905/2024 e prazos urgentes; ganha 3-6 recomendações estratégicas por polo com citações verbatim |
| **Associado de escritório médio** | Triagem de case intake: REPORT.md em 5 min substitui 30-60 min de leitura inicial |
| **Estudante / pesquisador** | Estudo estruturado de processos reais, dataset anotado |

**Fora do escopo:**

- ❌ **Análise de contrato** (ferramenta diferente — juriscan foi desenhado para peças processuais, não cláusulas contratuais)
- ❌ **Processo penal** (estrutura CPP e nulidades específicas não cobertas — foco é CPC cível/trabalhista)
- ❌ **Consultivo (M&A, tributário, regulatório)** sem litígio ativo
- ❌ **Advogado sênior de big-firm** que já tem paralegal/júnior para esse trabalho

### Requisitos

- **Claude Code** instalado ([claude.com/code](https://claude.com/code))
- Plano **Claude Max** ou **API com billing** — a skill usa a sua sessão Claude Code, então o uso da LLM é cobrado via sua assinatura. Não há chave de API separada.
- Python 3.10+
- Linux, macOS ou WSL

---

## Status & Pipelines

O JuriScan tem **dois pipelines de análise** que coexistem durante a transição para a arquitetura híbrida:

| Pipeline | Status | Quando usar | Como ativar |
|---|---|---|---|
| **Legacy** | ✅ Estável (default) | Uso em produção, validado em campo | `/juriscan <pdf>` ou `/juriscan --pipeline=legacy <pdf>` |
| **Agents** | 🧪 Beta (opt-in) | Casos que precisam de detecção semântica avançada (art. 942 CPC, dialética adversarial autor × réu × auditor, verificação web de jurisprudência) | `/juriscan --pipeline=agents <pdf>` |

O pipeline **legacy** é determinístico, rápido e tem cobertura de teste end-to-end com PDFs reais. É o caminho recomendado para a maioria dos casos.

O pipeline **agents** adiciona uma camada de raciocínio semântico via 8 subagents nativos do Claude Code (segmenter, parser, advogado-autor, advogado-reu, auditor-processual, verificador, sintetizador). A infraestrutura está completa, mas a validação end-to-end com PDFs reais ainda está em andamento — ver [issue de validação](https://github.com/brunobracaioli/juriscan/issues). O flip de default para `agents` está previsto para versão futura, após validação.

Desde **v3.1.0-legacy** até **v3.1.4**, o pipeline legacy ganhou:

- 📝 **Relatório executivo único** (`REPORT.md`) — markdown consolidado com caixas de alerta (Art. 942 CPC, Lei 14.905/2024, prazos urgentes), tabela cronológica de peças, contradições com citações verbatim, risk assessment e recomendações estratégicas por polo
- 🧩 **Padrão per-chunk file** — Claude faz um `Write chunks/NN.analysis.json` por peça (sem helper scripts hardcoded), com schema strict e merge determinístico
- ✂️ **Split-semantic com herança de data** — quando o chunker regex agrupa várias peças num arquivo físico, cada peça vira uma entrada separada em `analyzed.chunks[]` com seu próprio `primary_date`
- 🎯 **Recomendações estratégicas por polo** (`recommendations.json`) — 3-5 ações por polo com `evidence_quote` verbatim obrigatória e fundamentação legal
- 💰 **Recálculo Lei 14.905/2024 automático** — detecta condenações cruzando o marco de 30/08/2024
- 🔁 **Merge idempotente** (v3.1.4) — retry loop do Step 4 funciona sem reset manual
- 🎯 **Instância atual inferida** (v3.1.4) — header do relatório deduz a instância corrente da última peça cronológica

Detalhes técnicos: [`docs/architecture.md`](docs/architecture.md) · contratos por subagent: [`docs/subagents.md`](docs/subagents.md)

---

## Instalação

### Instalação automática via Claude Code (recomendada)

Abra o Claude Code em qualquer pasta e cole o prompt abaixo:

```
Clone o repositório https://github.com/brunobracaioli/juriscan.git em ~/.claude/skills/juriscan e rode o ./install.sh para instalar a skill. Se as dependências de sistema (poppler-utils, tesseract-ocr, tesseract-ocr-por) não estiverem instaladas, instale-as também.
```

O Claude vai executar todos os passos automaticamente. Quando terminar:

1. **Saia do Claude Code** (digite `/exit` ou `Ctrl+C`)
2. **Reabra o Claude Code** na pasta onde estão seus PDFs
3. Digite `/juriscan processo.pdf` e pronto

> **Por que precisa reiniciar?** O Claude Code descobre skills disponíveis ao iniciar a sessão. A skill recém-instalada só aparece na próxima sessão.

### Instalação manual (alternativa)

```bash
git clone https://github.com/brunobracaioli/juriscan.git ~/.claude/skills/juriscan
cd ~/.claude/skills/juriscan
./install.sh
cd -   # volta para o diretório anterior — NÃO rode o claude de dentro da skill
```

> **Importante:** depois de instalar, **saia do diretório da skill**. Skills do Claude Code ficam disponíveis globalmente — você roda `claude` na pasta do **seu projeto** (onde estão os PDFs), não dentro de `~/.claude/skills/juriscan`. Se você iniciar o Claude dentro da pasta da skill, ele não vai enxergar os arquivos do seu projeto.

<details>
<summary><b>Opção alternativa:</b> clonar em qualquer lugar</summary>

```bash
git clone https://github.com/brunobracaioli/juriscan.git
cd juriscan
./install.sh    # cria symlink para ~/.claude/skills/ e instala dependências
```

</details>

<details>
<summary><b>Dependências de sistema</b> (opcionais mas recomendadas)</summary>

```bash
# Ubuntu/Debian
sudo apt-get install poppler-utils tesseract-ocr tesseract-ocr-por

# macOS
brew install poppler tesseract tesseract-lang
```

Sem `poppler-utils`, a extração usa `pypdf` como fallback. Sem `tesseract`, PDFs escaneados não terão OCR.

</details>

---

## Uso

### Quick Run (um comando)

No Claude Code, com o PDF em qualquer pasta:

```
/juriscan ~/Downloads/processo.pdf
```

O Claude executa o pipeline completo automaticamente (extração → chunking → análise → contradições → prazos → risco → Obsidian) e apresenta o resultado.

### Linguagem natural

A skill também ativa quando você pede naturalmente:

> *"Analise este processo e mapeie as contradições"*
>
> *"Calcule os prazos deste processo"*
>
> *"Quais argumentos foram reformados em segunda instância?"*

### Via linha de comando

<details>
<summary>Ver todos os comandos</summary>

```bash
# Extrair e dividir PDF por peça processual
python3 scripts/extract_and_chunk.py --input processo.pdf --output ./analise/

# Verificar integridade (OCR quality, anomalias)
python3 scripts/integrity_check.py --input ./analise/

# Criar skeleton analyzed.json (Step 3a do fluxo per-chunk)
python3 scripts/analyzed_init.py --index ./analise/index.json --output ./analise/analyzed.json

# Consolidar arquivos per-chunk (chunks/NN.analysis.json) → analyzed.json (Step 3c)
python3 scripts/merge_chunk_analysis.py --analyzed ./analise/analyzed.json --chunks-dir ./analise/chunks/ --output ./analise/analyzed.json

# Validar schema + quality check com plano de retry per-chunk
python3 scripts/schema_validator.py --input ./analise/analyzed.json
python3 scripts/content_quality_check.py --input ./analise/analyzed.json --strict --per-chunk-retry-plan

# Calcular prazos CPC
python3 scripts/prazo_calculator.py --date 2025-03-15 --tipo contestação --state SP

# Rastrear argumentos entre instâncias
python3 scripts/instance_tracker.py --analysis ./analise/analyzed.json --output ./analise/instances.json

# Detectar contradições (legacy)
python3 scripts/legacy/contradiction_report.py --analysis ./analise/analyzed.json --output ./analise/contradictions.json

# Avaliar risco litigioso (legacy)
python3 scripts/legacy/risk_scorer.py --analysis ./analise/analyzed.json --output ./analise/risk.json

# Aplicar recálculo Lei 14.905/2024 (Step 8.5, in-place)
python3 scripts/finalize_legacy.py --input ./analise/analyzed.json --inplace

# Exportar para Obsidian
python3 scripts/obsidian_export.py --analysis ./analise/analyzed.json --output ./analise/obsidian/

# Gerar relatório executivo consolidado (REPORT.md — o "uau")
python3 scripts/generate_report.py \
  --analyzed ./analise/analyzed.json \
  --contradictions ./analise/contradictions.json \
  --prazos ./analise/prazos.json \
  --risk ./analise/risk.json \
  --recommendations ./analise/recommendations.json \
  --output ./analise/REPORT.md
```

</details>

---

## Pipeline

```
PDF(s)
 │
 ▼
[1]  Extração ─────────── pdftotext → pypdf → OCR
[2]  Integridade ──────── OCR confidence, anomalias, lacunas
[3]  Chunking ─────────── 27 tipos de peça processual detectados
[4]  Análise por chunk ── Claude: extração estruturada + citation grounding
[5]  Validação ────────── JSON Schema v2
[6]  Síntese cruzada ──── contradições + instâncias + precedentes vinculantes
[7]  Prazos CPC ───────── Art. 219-232, feriados, recesso forense
[8]  Scoring de risco ─── processual + mérito + exposição monetária
[9]  Output ───────────── JSON consolidado
[10] Obsidian ─────────── 7 views + peças + legislação + jurisprudência
```

---

## Vault Obsidian

A exportação gera um vault completo com backlinks automáticos:

```
processo-NNNNNNN/
├── _INDEX.md            Resumo executivo
├── _TIMELINE.md         Cronologia com Mermaid
├── _CONTRADIÇÕES.md     Mapa de contradições
├── _ENTIDADES.md        Partes, advogados, juízes
├── _RISCO.md            Avaliação de risco
├── _INSTÂNCIAS.md       Evolução de argumentos por instância
├── _PRAZOS.md           Dashboard de prazos
├── peças/               Uma nota por peça processual
├── legislação/          Stubs dos artigos citados
├── jurisprudência/      Stubs dos precedentes citados
└── diagramas/           Mermaid (timeline, grafo de referências)
```

---

## Funcionalidades

| Feature | Status |
|---|:---:|
| Extração PDF (text + OCR fallback) | :white_check_mark: |
| Chunking por peça processual (27 tipos) | :white_check_mark: |
| OCR confidence scoring | :white_check_mark: |
| Parsing de datas BR (DD/MM/YYYY, extenso, ISO) | :white_check_mark: |
| Parsing/validação de número CNJ | :white_check_mark: |
| Normalização monetária BRL | :white_check_mark: |
| Calculadora de prazos CPC (dias úteis, feriados, recesso) | :white_check_mark: |
| Detecção de contradições (valores, datas, fatos, jurisprudência) | :white_check_mark: |
| Rastreamento multi-instância (1ª inst → TJ → STJ → STF) | :white_check_mark: |
| Parsing tripartite de acórdão (ementa/relatório/voto) | :white_check_mark: |
| Detecção de precedentes vinculantes (SV, IRDR, IAC, RG) | :white_check_mark: |
| Citation grounding (afirmações com trecho fonte) | :white_check_mark: |
| Scoring de risco litigioso | :white_check_mark: |
| Exportação Obsidian (7 views) | :white_check_mark: |
| Validação de schema JSON | :white_check_mark: |

---

## Limitações conhecidas

Lista honesta para evitar surpresas — use o tool sabendo o que ele **não** faz:

- 🧪 **Pipeline `agents` ainda não foi validado end-to-end com PDFs reais.** A infraestrutura (8 subagents, schemas, audit trail, golden fixtures sintéticas) está completa e os testes Python passam, mas a validação iterativa com processos reais ainda não aconteceu. Use `--pipeline=legacy` (default) para qualquer uso prático. Ver [issue Phase F](https://github.com/brunobracaioli/juriscan/issues).
- 🔪 **Chunker regex (legacy) às vezes agrupa peças distintas** quando o layout do PDF é incomum. Mitigação atual: Claude detecta durante análise e usa o padrão split-semantic (`chunks/02a.analysis.json`, `02b`, `02c`). O `juriscan-segmenter` resolveria isso de forma mais limpa quando o pipeline agents for ativado.
- ⚠️ **`contradiction_report.py` pode emitir falso positivo em split-semantic.** Quando múltiplas peças semânticas estão num mesmo arquivo físico, o detector pode atribuir um valor à peça errada. Workaround: tratar contradições `VALOR_INCONSISTENTE` entre peças decisórias (SENTENÇA/ACÓRDÃO) com ceticismo — verificar manualmente se é reforma parcial legítima antes de acionar recurso.
- 🌐 **Zero verificação de jurisprudência** no pipeline legacy. Se o acórdão cita `REsp 1.234.567/SP`, o juriscan **não confere** se o precedente existe ou se foi corretamente aplicado. Revisão humana obrigatória em citações. (O pipeline agents tem `juriscan-verificador` para isso, mas ainda não foi validado.)
- 📊 **Risk score é heurístico, não atuarial.** `BAIXO (8.8/10)` não significa 88% de chance de ganhar — é uma agregação de fatores estruturais. Não use como prognóstico.
- ⏱️ **Prazos não são cientes de `process_state`.** O tool calcula prazos recursais mesmo em processo arquivado ou em cumprimento. Verifique o status real antes de agir em qualquer prazo sugerido.
- 📂 **Sem integração com PJe / e-SAJ / e-proc.** Você precisa baixar o PDF manualmente. O tool lê arquivo local, não tribunal online.
- 🤖 **Análise é assistida por IA** — sempre requer revisão profissional. Não substitui parecer jurídico nem produz peça vinculante.
- 📷 **OCR depende da qualidade do PDF original.** Documentos escaneados antigos ou de baixa resolução podem ter recall baixo. Sem tesseract instalado, PDFs escaneados falham silenciosamente.
- 🇧🇷 **Português brasileiro + CPC cível/trabalhista apenas.** Processo penal (CPP), tributário administrativo (CARF), arbitragem, e jurisdição não-brasileira não são cobertos.
- 💰 **Requer assinatura Claude Max** ou billing de API ativo. O uso da LLM é cobrado via sua sessão Claude Code, não há chave separada.

---

## Feedback & contribuições

O JuriScan está em **release público (v3.1.4)** e procura feedback de usuários reais:

- 🐛 **Achou um bug ou um falso positivo?** Abra uma [issue](https://github.com/brunobracaioli/juriscan/issues/new) descrevendo o comportamento esperado × observado. Se possível, inclua um PDF anonimizado que reproduza o problema.
- 💡 **Rodou em processo real e tem sugestão?** Use a [discussão de feedback v3.1.4](https://github.com/brunobracaioli/juriscan/issues) para contar o que funcionou, o que não funcionou, e o que faltou.
- 🧪 **Quer ajudar a validar o pipeline `agents`?** O caminho é adicionar PDFs reais anonimizados em `tests/golden/` seguindo o checklist em [`docs/fixture_anonymization.md`](docs/fixture_anonymization.md) (quando disponível).
- 🔀 **Pull requests** são bem-vindos — especialmente para novos tipos de peça, novos detectores de risco, fixtures de teste e correções no chunker regex.

**LGPD:** qualquer PDF enviado em issues ou PRs **deve** estar anonimizado (partes, CPFs, CNJ, valores sensíveis). Não compartilhe dados reais em issues públicas.

---

## Testes

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

```
============================= 443 passed in 7.35s ==============================
```

---

<p align="center">
  Feito para advogados brasileiros que precisam de análise forense séria.<br/>
  <sub>MIT License · v3.1.4</sub>
</p>
