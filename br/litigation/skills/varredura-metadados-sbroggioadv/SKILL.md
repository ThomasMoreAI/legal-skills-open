---
name: varredura-metadados-sbroggioadv
title: VARREDURA-METADADOS — o que o arquivo conta sobre si mesmo
description: 'VARREDURA-METADADOS — Camada 1 do motor de integridade estrutural. Executa o parser local metadados.py sobre DOCX e PDF e reporta o que os metadados do arquivo revelam: autor real diferente do assinante da peça, lastModifiedBy, track changes não aceito, comentários internos de revisão, Company, tempo total de edição, ferramenta geradora e linha do tempo de criação/modificação. Funciona nos dois sentidos — peça recebida (inteligência sobre quem/como/quando redigiu) e a própria peça antes do protocolo (o vazamento que a perícia adversária acharia; roteia para higiene-de-metadados). Todo achado é informativo: divergência sinalizada — a conclusão é do advogado. Aciona: "metadados", "quem escreveu esse documento", "autor do arquivo", "track changes", "comentários escondidos no docx", "varredura de metadados", "propriedades do documento".'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/blindagem-peticao-os-marketplace/tree/main/blindagem-peticao-os/skills/varredura-metadados
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# VARREDURA-METADADOS — o que o arquivo conta sobre si mesmo

## 1. Escopo

Todo DOCX e todo PDF carregam metadados que ninguém vê na leitura — e que
contam a história do arquivo. Esta skill roda o parser determinístico e traduz
o que cada campo revela:

| Metadado | Onde | O que revela |
|---|---|---|
| Autor (`dc:creator` / `Author`) | DOCX + PDF | Quem criou o arquivo — **autor real ≠ assinante da peça** é o achado clássico (terceirizado, outra banca, template alheio) |
| `lastModifiedBy` | DOCX | A última pessoa que editou — pode não ser nem o autor nem o assinante |
| Track changes não aceito | DOCX | Alterações rastreadas ainda gravadas: o que foi apagado, reescrito, por quem |
| Comentários internos | DOCX | Anotações de revisão que nunca deviam sair do escritório ("conferir se isso procede", instruções internas) |
| `Company` | DOCX | Organização do licenciamento do editor — pode divergir do escritório que assina |
| Tempo total de edição | DOCX | Minutos de edição acumulados — peça extensa com poucos minutos de edição sugere montagem por template ou geração externa |
| `Application` / `Producer` | DOCX + PDF | Ferramenta que gerou o arquivo (editor, conversor, gerador) |
| Datas de criação/modificação | DOCX + PDF | Linha do tempo do arquivo — compatível ou não com a narrativa dos autos |

**Quem decide é o parser** (`scripts/metadados.py`) — nunca palpite de leitura.
E nenhum desses achados é veredito: **cada um tem explicações legítimas**
(estagiário que digitou, computador compartilhado, template do escritório,
conversor que reescreve datas). A skill sinaliza a divergência; quem conclui é
o advogado.

## 2. Os dois sentidos de uso

| Sentido | Peça | O que a varredura entrega |
|---|---|---|
| **Defesa (inteligência)** | Recebida da parte contrária | Quem de fato redigiu, quando, com que ferramenta, o que ficou de rascunho — insumo de contexto para a resposta |
| **Prevenção (vazamento)** | A própria, antes do protocolo | Exatamente o que a perícia (ou a curiosidade) adversária acharia no SEU arquivo — cross-link direto com `higiene-de-metadados` para limpar antes de protocolar |

## 3. Input

| Campo | Obrigatório | Observação |
|---|---|---|
| `arquivo` | sim | Caminho local — `.docx` ou `.pdf` |
| Sentido de uso | desejável | Recebida × própria — muda o framing (inteligência × checklist de limpeza) |
| Nome do assinante da peça | desejável | Permite apontar objetivamente `autor ≠ assinante` |

## 4. Processamento

### Passo 1 — Executar o parser (do root do plugin)

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/metadados.py" <arquivo>
```

Retorno em JSON no stdout: `parser`, `versao`, `arquivo`, `status`,
`motor_usado`, `achados[]` (`tipo`, `gravidade`, `evidencia`, `localizacao`),
`resumo.total_achados`, `dependency_hint`.

### Passo 2 — Tratar o status (regra T1, sem exceção)

| `status` | Conduta |
|---|---|
| `ok` | Prosseguir para o Passo 3 |
| `missing_dependency` | DECLARAR: "varredura estrutural não executada" + exibir o `dependency_hint`. NUNCA improvisar metadado "de memória" ou por aparência do documento |
| `error` | Reportar o erro literal do parser |
| `formato_nao_suportado` | Informar os formatos aceitos (`.docx`/`.pdf`) |

Se `motor_usado: "raw"`, declarar: **"cobertura limitada a streams não
comprimidos"** — campos podem ter escapado da leitura.

### Passo 3 — Traduzir cada achado

Para CADA achado: anexar a **evidência bruta** (campo + valor literal extraído)
e a leitura da tabela do §1 — sempre com as hipóteses legítimas junto. Nunca
transformar divergência em acusação.

### Passo 4 — Roteamento por sentido

- Peça **recebida**: achados relevantes viram contexto no dossiê (ex.: autor
  divergente + tempo de edição mínimo somam-se aos sinais da
  `heuristica-uso-de-ia`, que julga esse conjunto).
- Peça **própria**: cada achado vira item do checklist de limpeza — rotear para
  `higiene-de-metadados` ANTES do protocolo.

## 5. Output

```markdown
## 🔍 Varredura de metadados — {{arquivo}}

**Parser:** metadados.py v{{versao}} · **Status:** {{status}}
**Sentido:** [peça recebida × própria pré-protocolo] · **Achados:** {{n}}

| # | Campo | Valor extraído | O que pode indicar | Hipóteses legítimas |
|---|---|---|---|---|
| 1 | Author | "[valor literal]" | Autor real ≠ assinante | Estagiário, template, PC compartilhado |

### Leitura

- **Divergência sinalizada — a conclusão é do advogado.** Nenhum campo acima
  prova autoria, montagem ou má-fé por si só.
- [se própria] ➡️ Itens acima roteados para `higiene-de-metadados` — limpar
  antes de protocolar.
- [se recebida] ➡️ Contexto encaminhado ao `dossie-de-integridade`.

> ⚠️ Conferência humana final é do advogado. Esta varredura sinaliza; não conclui.
```

Sem achados: reportar "0 achados de metadados relevantes" + motor usado. Arquivo
"limpo" também é informação (limpeza deliberada é comum e legítima).

## 6. O que esta skill nunca faz

1. Nunca reporta metadado sem o parser ter extraído o valor literal (T1).
2. Nunca conclui "a peça não foi escrita por quem assina" — sinaliza a divergência com as hipóteses legítimas ao lado (T4).
3. Nunca usa metadado como prova de uso de IA — sinais desse tipo pertencem à `heuristica-uso-de-ia`, que os rotula como heurísticos.
4. Nunca modifica o arquivo original — a limpeza é guiada pela `higiene-de-metadados`, em cópia, por decisão do advogado.

## 7. Travas desta skill

| Trava | Aplicação aqui |
|---|---|
| **T1** | Achado só existe com o parser rodado + campo/valor literal anexados; `missing_dependency` → "varredura estrutural não executada" + `dependency_hint` |
| **T4** | Metadado estranho = **alerta informativo com hipóteses legítimas**, nunca veredito — "divergência sinalizada — a conclusão é do advogado" fecha todo achado |
| **T5** | ⚠️ Conferência humana final é do advogado — todo relatório sai com este aviso |

## 8. Integração

- **Upstream:** `blindagem-master` · `blindagem-pre-protocolo`
- **Downstream:** `higiene-de-metadados` (limpeza da própria peça) · `heuristica-uso-de-ia` (consome sinais, com rótulo heurístico) · **`dossie-de-integridade` — todo achado termina lá**
