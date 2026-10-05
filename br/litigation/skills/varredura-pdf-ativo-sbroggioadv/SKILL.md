---
name: varredura-pdf-ativo-sbroggioadv
title: VARREDURA-PDF-ATIVO — o que o PDF faz, além do que ele mostra
description: 'VARREDURA-PDF-ATIVO — Camada 1 do motor de integridade estrutural. Executa o parser local pdf_integridade.py e reporta conteúdo ativo embutido no PDF da peça: /OpenAction e /AA (ações automáticas ao abrir/interagir), /JS e /JavaScript (código embutido), /Launch (execução de programa externo) e /EmbeddedFile (arquivo dentro do arquivo). Classe de ameaça madura em segurança da informação, sem caso ofensivo documentado dentro de processo judicial brasileiro — camada de higiene preventiva, apresentada como tal. Achado = alerta técnico com a chave encontrada + recomendação de não abrir o PDF em visualizador com JavaScript habilitado até avaliar. Sinaliza — nunca conclui fraude. Aciona: "pdf com javascript", "conteúdo ativo no pdf", "openaction", "pdf executa algo", "arquivo embutido no pdf", "varredura de pdf ativo", "esse pdf é seguro".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/blindagem-peticao-os-marketplace/tree/main/blindagem-peticao-os/skills/varredura-pdf-ativo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# VARREDURA-PDF-ATIVO — o que o PDF faz, além do que ele mostra

## 1. Escopo

PDF não é só página estática: o formato permite embutir **comportamento**. Esta
skill roda o parser determinístico e reporta as chaves de conteúdo ativo no
dicionário de objetos do arquivo:

| Chave | O que faz |
|---|---|
| `/OpenAction` | Ação executada automaticamente ao abrir o documento |
| `/AA` | Additional Actions — gatilhos automáticos (abrir/fechar página, mouse) |
| `/JS` · `/JavaScript` | Código JavaScript embutido no documento |
| `/Launch` | Tenta executar um programa externo na máquina do leitor |
| `/EmbeddedFile` | Arquivo embutido dentro do PDF |

**Usos legítimos existem** — formulário interativo usa JavaScript; PDF/A-3
embute arquivo por design (ex.: XML de NF-e); `/OpenAction` pode só posicionar a
primeira página. Por isso todo achado é **alerta técnico**, nunca veredito.

**Quem decide é o parser** (`scripts/pdf_integridade.py`) — nunca a impressão
de leitura do LLM.

## 2. Honestidade obrigatória — o estágio real deste vetor

PDF malicioso é **classe de ameaça madura em segurança da informação** (vetor
clássico de ataque por e-mail e download há mais de uma década). Mas **não há
caso ofensivo documentado DENTRO de processo judicial brasileiro** até esta
versão. A apresentação correta é: **camada de higiene preventiva** — o advogado
recebe dezenas de PDFs de origem adversa por semana e não tem por que abri-los
às cegas com execução de script habilitada. Nunca vender como "isso já
aconteceu no seu tribunal".

## 3. Input

| Campo | Obrigatório | Observação |
|---|---|---|
| `arquivo` | sim | Caminho local do PDF |
| Origem do arquivo | desejável | Peça/anexo recebido × arquivo próprio — muda o framing |

## 4. Processamento

### Passo 1 — Executar o parser (do root do plugin)

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/pdf_integridade.py" <arquivo.pdf>
```

Retorno em JSON no stdout: `parser`, `versao`, `arquivo`, `status`,
`motor_usado`, `achados[]` (`tipo`, `gravidade`, `evidencia`, `localizacao`),
`resumo.total_achados`, `dependency_hint`.

### Passo 2 — Tratar o status (regra T1, sem exceção)

| `status` | Conduta |
|---|---|
| `ok` | Prosseguir para o Passo 3 |
| `missing_dependency` | DECLARAR: "varredura estrutural não executada" + exibir o `dependency_hint`. NUNCA improvisar ("esse PDF parece seguro/perigoso") |
| `error` | Reportar o erro literal do parser |
| `formato_nao_suportado` | Informar que esta varredura cobre PDF |

Se `motor_usado: "raw"`, declarar: **"cobertura limitada a streams não
comprimidos"** — ausência de achado nesse modo NÃO atesta ausência de conteúdo
ativo.

### Passo 3 — Focar os achados de conteúdo ativo

Desta execução interessam os achados de chave ativa (`/OpenAction`, `/AA`,
`/JS`, `/JavaScript`, `/Launch`, `/EmbeddedFile`). Achados de **texto oculto**
(mesma execução do parser) pertencem à skill irmã `varredura-texto-oculto` —
apontar, sem duplicar.

### Passo 4 — Alerta técnico + recomendação prática

Para CADA achado:

1. **Anexar a evidência bruta**: a chave encontrada, o conteúdo/trecho que o
   parser extraiu (`evidencia`) e a localização no arquivo.
2. **Classificar a leitura em hipóteses**, sem veredito: uso legítimo provável
   (formulário, PDF/A-3) × sem função aparente numa peça processual (ex.:
   `/Launch` não tem uso legítimo esperado em petição).
3. **Recomendação prática imediata:** não abrir o PDF em visualizador com
   JavaScript habilitado até avaliar o achado — usar leitor com JS desabilitado
   e não aceitar prompts de execução do leitor. Isso é higiene, não acusação.

## 5. Output

```markdown
## 🔍 Varredura de conteúdo ativo — {{arquivo}}

**Parser:** pdf_integridade.py v{{versao}} · **Motor:** {{motor_usado}}
**Status:** {{status}} · **Achados de conteúdo ativo:** {{n}}

| # | Chave | Evidência extraída | Localização | Leitura |
|---|---|---|---|---|
| 1 | /JS | [trecho do código/conteúdo] | objeto N | Sem função aparente em petição |

### Recomendação imediata

- ⚠️ Não abrir este PDF em visualizador com JavaScript habilitado até avaliar
  os achados acima. Preferir leitor com JS desabilitado; recusar prompts de
  execução.

### Leitura

- Alerta técnico com evidência — **não** é veredito de arquivo malicioso: há
  usos legítimos documentados para várias dessas chaves (formulários, PDF/A-3).

➡️ Todo achado segue para o `dossie-de-integridade`.

> ⚠️ Conferência humana final é do advogado. Esta varredura sinaliza; não conclui.
```

Sem achados: reportar "0 achados de conteúdo ativo" + motor usado + ressalva do
modo `raw` quando aplicável.

## 6. O que esta skill nunca faz

1. Nunca declara conteúdo ativo sem o parser ter retornado a chave + evidência (T1).
2. Nunca conclui "PDF malicioso" ou "tentativa de ataque" — alerta técnico com hipóteses; a conclusão é do advogado/perito (T4).
3. Nunca executa, extrai ou abre o conteúdo ativo encontrado — reporta a existência.
4. Nunca apresenta o vetor como "documentado em processo brasileiro" — a honestidade do §2 é parte da skill.

## 7. Travas desta skill

| Trava | Aplicação aqui |
|---|---|
| **T1** | Achado só existe com o parser rodado + chave/evidência anexadas; `missing_dependency` → "varredura estrutural não executada" + `dependency_hint` |
| **T4** | Chave ativa achada = alerta técnico com hipóteses legítimas ao lado; "malicioso" é conclusão pericial, não desta skill |
| **T5** | ⚠️ Conferência humana final é do advogado — todo relatório sai com este aviso |

## 8. Integração

- **Upstream:** `blindagem-master` · `blindagem-pre-protocolo`
- **Downstream:** **`dossie-de-integridade` — todo achado termina lá**
- **Irmã:** `varredura-texto-oculto` (mesmo parser, foco em texto invisível)
