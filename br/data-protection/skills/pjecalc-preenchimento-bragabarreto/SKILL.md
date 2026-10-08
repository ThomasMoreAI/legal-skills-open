---
name: pjecalc-preenchimento-bragabarreto
title: 'Skill: Preenchimento do PJE-Calc Cidadão'
description: Guia completo de preenchimento e automação do PJE-Calc Cidadão (versão desktop). Cobre todos os módulos do sistema — Dados do Cálculo, Faltas, Férias, Histórico Salarial, Verbas, Cartão de Ponto, Salário-família, Seguro-desemprego, FGTS, Contribuição Social, Previdência Privada, Pensão Alimentícia, Imposto de Renda, Multas e Indenizações, Honorários, Custas Judiciais, Correção/Juros/Multa e Operações — com instruções campo a campo, fluxos sequenciais, regras de negócio, armadilhas comuns e exemplos práticos extraídos do manual oficial do CSJT.
author: bragabarreto
author_url: https://github.com/bragabarreto/pjecalc-agente/tree/main/skills/pjecalc-preenchimento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: data-protection
language: pt
sources:
- title: 01 Parametros Calculo
  path: references/01-parametros-calculo.md
- title: 02 Verbas Catalogo
  path: references/02-verbas-catalogo.md
- title: 03 Historico Salarial
  path: references/03-historico-salarial.md
- title: 04 Fgts Contribuicao Social
  path: references/04-fgts-contribuicao-social.md
- title: 05 Correcao Juros
  path: references/05-correcao-juros.md
- title: 06 Exemplos Praticos
  path: references/06-exemplos-praticos.md
- title: 07 Automacao Playwright
  path: references/07-automacao-playwright.md
---

# Skill: Preenchimento do PJE-Calc Cidadão

## Visão Geral

O **PJE-Calc** é o sistema de cálculo trabalhista da Justiça do Trabalho, desenvolvido pelo TRT8 e distribuído pelo CSJT. A versão **Cidadão (desktop)** roda localmente via servidor Tomcat com banco H2, acessível pelo navegador em `http://localhost:8080/pje-calc` (ou porta configurada). Não requer Internet, mas exige Java 7/8 e Firefox.

Esta skill orienta o preenchimento completo de um cálculo trabalhista, do início à liquidação, e serve como base de conhecimento para automação via Playwright/Selenium.

---

## Fluxo Sequencial de Preenchimento

Execute as etapas **na ordem abaixo**. Cada etapa corresponde a uma página do menu lateral do sistema.

```
1.  Novo Cálculo → Dados do Processo (opcional)
2.  Novo Cálculo → Parâmetros do Cálculo  ← OBRIGATÓRIO
3.  Faltas                                 ← se houver faltas
4.  Férias                                 ← verificar/ajustar sugestão do sistema
5.  Histórico Salarial                     ← lançar base(s) salarial(is)
6.  Verbas                                 ← lançar verbas principais e reflexas
7.  Cartão de Ponto                        ← se houver horas extras por cartão
8.  Salário-família                        ← se deferido
9.  Seguro-desemprego                      ← se deferido
10. FGTS                                   ← conferir/ajustar parâmetros
11. Contribuição Social                    ← conferir/ajustar parâmetros
12. Previdência Privada                    ← se deferida
13. Pensão Alimentícia                     ← se deferida
14. Imposto de Renda                       ← conferir/ajustar parâmetros
15. Multas e Indenizações                  ← se houver multas/indenizações
16. Honorários                             ← se houver honorários
17. Custas Judiciais                       ← se houver custas
18. Correção, Juros e Multa                ← conferir índices (padrão já sugerido)
19. **Regerar Ocorrências** (aba Verbas)   ← se houve alterações nos parâmetros
20. Operações → Liquidar
21. Operações → Imprimir / Exportar
```

> **Regra de ouro:** Clicar **Salvar** após CADA página. Sair sem salvar = **PERDA TOTAL** dos dados preenchidos. Aguardar mensagem "Operação realizada com sucesso" antes de navegar.

---

## Fluxo Condicional: Criar vs. Abrir Cálculo

```
Existe cálculo já salvo?
├── SIM → Aba Cálculo → Buscar Cálculo → ícone Abrir (ou Duplicar)
└── NÃO → Aba Cálculo → Novo → preencher Parâmetros do Cálculo → Salvar
```

---

## 1. Dados do Processo (aba opcional)

**Quando usar:** Vincular o cálculo a um processo trabalhista específico.

| Campo | Tipo | Instrução |
|---|---|---|
| Modo de preenchimento | Seleção | `Manualmente` (digitar) ou `Obter do PJe` (busca automática) |
| Número do processo | Texto | Numeração única CNJ (somente em "Obter do PJe") |
| Reclamante | Texto | Nome e CPF/CNPJ do autor |
| Reclamado | Texto | Nome e CPF/CNPJ do réu |
| Advogados | Texto | Nome e OAB (opcional) |
| Inverter Partes | Checkbox | Marcar se Autor = Reclamado e Réu = Reclamante |

---

## 2. Parâmetros do Cálculo (OBRIGATÓRIO)

Campos com `*` são obrigatórios.

| Campo | Obrig. | Instrução |
|---|---|---|
| Estado `*` | Sim | UF do local de trabalho |
| Município `*` | Sim | Município do local de trabalho |
| Admissão `*` | Sim | Data de admissão (dd/mm/aaaa) |
| Ajuizamento `*` | Sim | Data do ajuizamento (ou data pretendida) |
| Demissão | Cond. | Obrigatório se não houver Data Final |
| Data Inicial | Não | Limita o início do período de cálculo |
| Data Final | Cond. | Obrigatório se não houver Demissão |
| Maior Remuneração | Não | Necessário para Aviso Prévio e Multa Art. 477 |
| Última Remuneração | Não | Cria histórico salarial automático com incidência em CS |
| Regime de Trabalho | Seleção | `Tempo Integral` (30 dias férias) ou `Tempo Parcial` (18 dias) |
| Prazo do Aviso Prévio | Seleção | `Não Apurar` / `Calculado` (Lei 12.506/2011) / `Informado` |
| Projetar Aviso Prévio Indenizado | Checkbox | Projeta avos de férias/13º com base no aviso |
| Limitar Avos ao Período | Checkbox | Exclui avos vencidos antes da prescrição/data inicial |
| Prescrição Quinquenal | Checkbox | Aplica prescrição de 5 anos às verbas |
| Prescrição FGTS | Checkbox | Aplica prescrição específica ao FGTS |
| Zerar Valor Negativo | Checkbox | Zera ocorrências negativas (padrão: desmarcado) |
| Considerar Feriado Estadual | Checkbox | Para verbas com divisor "Dias Úteis" |
| Considerar Feriado Municipal | Checkbox | Para verbas com divisor "Dias Úteis" |
| Sábado como Dia Útil | Checkbox | Padrão: marcado |
| Carga Horária | Número | Padrão: 220h/mês |
| Comentários | Texto | Até 255 caracteres (aparece no Resumo do Cálculo). **Justiça Gratuita:** quando deferida a qualquer parte, inserir: "Honorários advocatícios devidos [parte(s)] com exigibilidade suspensa, ante a gratuidade judiciária deferida, nos termos do art. 791-A, parágrafo 4o, da CLT." |

**Após preencher → clicar em Salvar.**

---

## 3. Faltas

Acessível pelo menu lateral após salvar os Parâmetros do Cálculo.

| Campo | Instrução |
|---|---|
| Data Inicial | Primeiro dia da falta (dd/mm/aaaa) |
| Data Final | Último dia da falta (dd/mm/aaaa) |
| Falta Justificada | Marcar se a falta for justificada (ex.: doação de sangue) |
| Justificativa da Falta | Texto descritivo (somente se justificada) |
| Ação | Clicar no ícone **Salvar** após cada lançamento |

> Lançar cada período de falta separadamente. O sistema desconta as faltas não justificadas no prazo de férias e na proporcionalidade das verbas.

---

## 4. Férias

O sistema **sugere automaticamente** os períodos aquisitivos e concessivos. O usuário deve verificar e ajustar quando necessário.

| Campo | Instrução |
|---|---|
| Período Aquisitivo | Calculado automaticamente (Admissão + 12 meses) |
| Situação | `Gozadas` ou `Indenizadas` — ajustar conforme sentença |
| Período de Gozo | Datas de início e fim do gozo (somente se Gozadas) |
| Prazo (dias) | Calculado pelo sistema (30 ou 24 dias, conforme faltas) |

> **Atenção:** Se as férias foram gozadas em período diferente do sugerido, altere o campo "Período de Gozo" antes de salvar. O sistema usa essa informação para calcular a base da Contribuição Social e excluir o período das verbas mensais.

---

## 5. Histórico Salarial

Armazena todas as bases de cálculo usadas nas verbas, FGTS e contribuições sociais.

### 5.1 Criar nova base

Clicar em **Novo** e preencher:

| Campo | Instrução |
|---|---|
| Nome | Identificador da base (ex.: "Salário Pago", "Adicional Noturno Pago") |
| Incidência no FGTS | Marcar se a base deve compor o FGTS |
| Incidência na CS | Marcar se a base deve compor a Contribuição Social |
| Tipo de Valor | `Informado` (digitar mês a mês) ou `Calculado` (salário mínimo/piso) |

### 5.2 Base Informada

- Informar Competência Inicial, Competência Final e Valor (mês integral, mesmo em meses proporcionais).
- Exceção: bases variáveis pagas pelo número de horas (HE, adicional noturno) — informar o valor efetivamente pago.
- Se já houve recolhimento de FGTS/CS sobre o valor, marcar os checkboxes correspondentes.
- Clicar em **Gerar Ocorrências** → verificar → clicar em **Salvar**.

### 5.3 Base Calculada

- Informar Quantidade e selecionar Base de Referência: `Salário Mínimo` ou `Piso Salarial` (+ Categoria).
- Clicar em **Gerar Ocorrências** → verificar → clicar em **Salvar**.

### 5.4 Grade de Ocorrências

- Clicar no ícone **Grade de Ocorrências** para editar todos os históricos simultaneamente.
- Útil para ajustar valores de meses específicos (ex.: mês de férias gozadas).

> **Regra importante:** Lançar o valor do mês **integral**, mesmo que o trabalhador tenha trabalhado apenas parte do mês. O sistema proporcionaliza automaticamente conforme as faltas e o período.

---

## 6. Verbas

### 6.1 Lançamento Expresso (recomendado para verbas padrão)

1. Clicar em **Expresso**.
2. Marcar os checkboxes das verbas principais desejadas.
3. Clicar em **Salvar**.
4. O sistema lista as verbas na coluna **Verba Principal**.

### 6.2 Lançamento Manual (para verbas customizadas)

Clicar em **Manual** e preencher:

| Campo | Instrução |
|---|---|
| Nome | Até 50 caracteres |
| Assunto CNJ | Selecionar na tabela processual unificada |
| Valor | `Calculado` (pelo sistema) ou `Informado` (pelo usuário) |
| Incidência | Marcar: FGTS, IRPF, CS, Previdência Privada, Pensão Alimentícia |
| Característica | `Comum`, `13º Salário`, `Aviso Prévio` ou `Férias` |
| Ocorrência de Pagamento | `Mensal`, `Dezembro`, `Período Aquisitivo` ou `Desligamento` |
| Juros a partir do Ajuizamento | `Ocorrências Vencidas` (padrão) ou `Vencidas e Vincendas` |
| Tipo | `Principal` ou `Reflexa` |
| Gerar Verba Reflexa | `Devido` ou `Diferença` |
| Compor Principal | `Sim` (padrão) ou `Não` |
| Zerar Valor Negativo | Conforme padrão ou ajuste por verba |

### 6.3 Parâmetros do Valor Devido (Calculado)

Parâmetros disponíveis conforme a combinação Característica × Ocorrência × Tipo:

| Parâmetro | Instrução |
|---|---|
| Período | Sugerido pelo sistema; ajustar se necessário |
| Base de Cálculo | Histórico Salarial, Maior Remuneração, Piso Salarial, Salário Mínimo, Vale Transporte, Verba |
| Multiplicador | Percentual ou fração (ex.: 0,5 para 50%) |
| Divisor | `Carga Horária`, `Dias Úteis`, `Dias Corridos`, `Informado` |
| Quantidade | `Avos` (automático), `Informada` (fixo) ou `Importada do Cartão de Ponto` |
| Dobra | Marcar para dobrar o valor calculado |
| Proporcionalizar | Sim/Não para meses incompletos |

### 6.4 Verbas Reflexas

- Clicar no ícone **Exibir** ao lado de cada verba principal.
- Marcar os checkboxes das verbas reflexas deferidas (ex.: Aviso Prévio sobre HE, 13º sobre HE).
- **Atenção:** O FGTS + 40% não aparece como verba reflexa — é configurado diretamente na página FGTS via campo "incidência no FGTS" dos Parâmetros da Verba.
- **Multa Art. 467 CLT:** Aparece como **reflexa automática** sob cada verba principal (ex: "MULTA DO ARTIGO 467 DA CLT SOBRE SALDO DE SALÁRIO", "... SOBRE FÉRIAS + 1/3", "... SOBRE AVISO PRÉVIO"). Essas reflexas são geradas automaticamente quando o checkbox `multaDoArtigo467` está marcado na aba FGTS. **NÃO criar Multa 467 como verba Expresso nem Manual** — ela não existe no catálogo Expresso.

### 6.5 Parâmetros da Verba (ajuste pós-lançamento)

Clicar no ícone **Parâmetros da Verba** para ajustar:
- Base de cálculo (selecionar histórico salarial específico).
- Valor Pago (para apurar diferença salarial).
- Integralizar/Proporcionalizar reflexos.
- Após alterar, o sistema sinaliza necessidade de **Regerar** as ocorrências.

### 6.6 Ocorrências da Verba

Clicar no ícone **Ocorrências** para visualizar/editar mês a mês:
- Usar **Alteração em Lote** para ajustes em série.
- Editar diretamente na grade para ajustes pontuais.
- Ao regerar, optar entre **Manter** ou **Sobrescrever** alterações manuais.

---

## 7. Cartão de Ponto

Usado para calcular horas extras, intervalos e adicional noturno a partir de jornadas registradas.

**Pré-requisitos OBRIGATÓRIOS (antes de criar cartão):**
1. **Dados do Cálculo** salvos: admissão, demissão, prescrição
2. **`valorCargaHorariaPadrao`** salvo em Parâmetros do Cálculo (220h, 180h, 150h mensal). Sem ele, clicar "Novo" causa HTTP 500 (NPE).
3. Histórico Salarial preenchido (recomendável)

**DISTINÇÃO CRÍTICA — Jornada Padrão vs Praticada:**
- **"Jornada de Trabalho Padrão"** (campos `valorJornadaSegunda` a `Dom`) = jornada **CONTRATUAL** (ex: 8h/dia CLT). Serve como referência para cálculo de HE.
- **"Grade de Ocorrências"** = jornada **EFETIVAMENTE PRATICADA** (ex: 10h/dia). Preenchida via Programação Semanal, Escala ou Livre.
- **HE = praticada − padrão**. Se preencher padrão com praticada → HE = 0 (ERRO!)

**Fórmulas (NÃO confundir):**
- `valorCargaHorariaPadrao` (Parâmetros do Cálculo) = `semanal × 5` (ex: 44h→220)
- `qtJornadaMensal` (Cartão de Ponto, "Jornada Mensal Média") = `semanal / 7 × 30` (ex: 44h→188,57)

| Campo | Instrução |
|---|---|
| Critérios de Apuração | Data Inicial/Final do período, critério mais favorável |
| Jornada de Trabalho Padrão | Preencher com jornada **CONTRATUAL** (NÃO a praticada!) |
| Intervalos | Marcar checkboxes de Intrajornada e Interjornadas se deferidos |
| Programação Semanal | Preencher grade com horários de entrada e saída por dia da semana |
| Dia do Fechamento Mensal | Informar o dia de fechamento do cartão (ex.: 20) |
| Apurar Cartão de Ponto | Clicar para gerar as quantidades mensais |

Após apurar, acessar **Parâmetros da Verba** de cada verba e selecionar `Importada do Cartão de Ponto` no campo Quantidade.

**Importação via CSV:**
- Formato: coluna 1 = mês/ano (mm/aaaa), demais colunas = quantidades (até 4 casas decimais).
- Máximo de 16 colunas; sem limite de linhas.

---

## 8. Salário-família

| Campo | Instrução |
|---|---|
| Apurar Salário-família | Marcar checkbox para habilitar |
| Compor Principal | `Sim` (padrão) ou `Não` |
| Competências | Período de apuração (padrão: período do cálculo) |
| Remuneração Mensal (Salários Pagos) | `Nenhum`, `Maior Remuneração` ou `Histórico Salarial` |
| Remuneração Mensal (Salários Devidos) | Selecionar verbas que compõem a base |
| Quantidade de Filhos < 14 anos | Informar quantidade; adicionar variações com data de início |

Clicar em **Salvar**.

---

## 9. Seguro-desemprego

| Campo | Instrução |
|---|---|
| Apurar Seguro-desemprego | Marcar checkbox para habilitar |
| Compor Principal | `Sim` (padrão) ou `Não` |
| Quantidade de Parcelas | Calculada pelo sistema; ajustar se necessário |
| Tipo de Solicitação | `Primeira`, `Segunda` ou `Demais` (para demissões a partir de 01/03/2015) |
| Remuneração Mensal | Igual ao Salário-família |

Clicar em **Salvar**.

---

## 10. FGTS

| Campo | Instrução |
|---|---|
| Destino | `Pagar ao reclamante` ou `Recolher em conta vinculada` |
| Compor Principal | `Sim` (padrão) ou `Não` |
| Multa (checkbox) | Marcar para habilitar seção de multa. **AGUARDAR AJAX** após marcar (onchange re-renderiza campos dependentes). Só depois preencher tipo e percentual. |
| Tipo do Valor da Multa | `Calculada` (20% ou 40%) ou `Informada`. **Selecionar ANTES do percentual** (o radio multaDoFgts só aparece quando tipo=CALCULADA). Aguardar AJAX. |
| Percentual (multaDoFgts) | `QUARENTA_POR_CENTO` (padrão demissão sem justa causa) ou `VINTE_POR_CENTO` (estabilidade provisória: CIPA, gestante, acidentário). Na extração, quando sentença determina 20%, preencher `fgts.multa_40=true` (habilita seção) **E** `fgts.multa_20=true` (seleciona 20%). |
| Base da Multa | `Devido`, `Diferença`, `Saldo e/ou Saque`, `Devido (-) Saldo`, `Devido (+) Saldo` |
| Multa Art. 467 CLT | Checkbox `multaDoArtigo467`. **Dependente do checkbox `multa` estar marcado** (disabled se multa=false). Ao marcar, o sistema gera reflexas automáticas na aba Verbas: "MULTA DO ARTIGO 467 DA CLT SOBRE [verba principal]" para cada verba. NÃO é verba Expresso. |
| Pensão Alimentícia sobre FGTS | Marcar se a pensão deve incidir sobre o FGTS |
| Saldo e/ou Saque | Informar Data e Valor; clicar em Adicionar; marcar `Deduzir do FGTS` se aplicável |
| Contribuição Social LC 110/2001 | Marcar 10% e/ou 0,5% se devidas |

**Ocorrências do FGTS:**
- Clicar em **Ocorrências** para editar base mês a mês.
- Ajustar manualmente meses com 13º salário pago ou férias gozadas + 1/3 (acrescentar esses valores à base do mês correspondente).
- Para regerar: clicar em **Regerar** → alterar Data Inicial/Final e Alíquota → optar entre Manter/Sobrescrever → Confirmar.

> **FAQ — FGTS sobre Férias + 1/3 indenizadas:** O sistema só apura incidências de Férias + 1/3 (período aquisitivo) para ocorrências anteriores à demissão. Para férias indenizadas, acesse Ocorrências do FGTS, acrescente o valor de Férias + 1/3 à base da ocorrência da demissão e salve. Depois reliquide.

Clicar em **Salvar**.

---

## 11. Contribuição Social

| Campo | Instrução |
|---|---|
| Apurar CS sobre Salários Devidos | Padrão: marcado |
| Apurar CS sobre Salários Pagos | Marcar quando houver salários pagos a abater |
| Alíquota Segurado Empregado | `Fixa` (padrão) ou `Por Atividade Econômica` |
| Alíquota Empregador | `Fixa` 20% (padrão) ou `Por Atividade Econômica` |
| SAT | 3% (padrão); ajustar conforme atividade |
| Terceiros | Padrão: não apurar |
| Cobrar do Reclamante | Padrão: marcado (desconta do crédito do reclamante) |

**Ocorrências da CS:**
- Clicar em **Ocorrências** → **Regerar** para ajustar parâmetros.
- Ajustar manualmente a coluna `Salários Pagos (Histórico)` quando necessário (ex.: acrescentar férias gozadas + 1/3 pagas no contracheque).

> **Atividade Econômica:** Para alterar a alíquota do empregador por atividade, selecionar `Por Atividade Econômica`, digitar palavra-chave no campo, selecionar a categoria e confirmar.

Clicar em **Salvar**.

---

## 12. Previdência Privada

| Campo | Instrução |
|---|---|
| Apurar Previdência Privada | Marcar checkbox para habilitar |
| Alíquota | Informar percentual (ex.: 12,00) |
| Competência Inicial / Final | Para múltiplas alíquotas em períodos distintos |
| Ação | Clicar em **Adicionar** para cada período → **Salvar** |

> A base é definida nos Parâmetros das Verbas (checkbox "Incidência Previdência Privada").

---

## 13. Pensão Alimentícia

| Campo | Instrução |
|---|---|
| Apurar Pensão Alimentícia | Marcar checkbox para habilitar |
| Alíquota | Percentual a aplicar sobre a base |
| Incidir sobre Juros | Marcar se a pensão deve incidir sobre os juros de mora |

> A base é definida nos Parâmetros das Verbas (checkbox "Incidência Pensão Alimentícia") e nas opções da página FGTS.

Clicar em **Salvar**.

---

## 14. Imposto de Renda

| Campo | Instrução |
|---|---|
| Apurar Imposto de Renda | Marcar checkbox para habilitar |
| Incidir sobre Juros de Mora | Marcar para incluir juros na base do IR |
| Cobrar do Reclamado | Marcar quando o reclamado for responsável pelo recolhimento |
| Tributação Exclusiva | Apura IR separadamente sobre verbas com característica 13º Salário |
| Tributação em Separado | Apura IR separadamente sobre verbas com característica Férias |
| Deduzir da Base do IR | Selecionar: CS devida pelo Reclamante, Previdência Privada, Pensão Alimentícia, Honorários devidos pelo Reclamante |
| Aposentado Maior de 65 anos | Marcar para aplicar dedução correspondente |
| Dependentes | Marcar e informar quantidade |

> O sistema aplica automaticamente o Art. 12-A da Lei 7.713/1988 para liquidações a partir de 28/07/2010 (tabela progressiva acumulada para anos anteriores + tabela mensal para o ano da liquidação).

Clicar em **Salvar**.

---

## 15. Multas e Indenizações

Para cada multa/indenização, clicar em **Novo** e preencher:

| Campo | Instrução |
|---|---|
| Descrição | Até 60 caracteres |
| Credor/Devedor | Par: `Reclamante/Reclamado`, `Reclamado/Reclamante`, `Terceiro/Reclamante`, `Terceiro/Reclamado` |
| Terceiro | Nome do terceiro (se credor for Terceiro) |
| Valor | `Calculado` (sobre a condenação) ou `Informado` |
| Base (se Calculado) | `Principal`, `Principal (-) CS`, `Principal (-) CS (-) PP` |
| Alíquota (se Calculado) | Percentual |
| Vencimento (se Informado) | Data de vencimento do valor |
| Valor (se Informado) | Montante monetário |
| Índice de Correção | `Índice Trabalhista` ou `Outro Índice` |
| Juros | Marcar se incidem juros de mora |
| Identificação | ID do documento judicial (para fase de atualização) |

Clicar em **Salvar** após cada lançamento.

---

## 16. Honorários

Para cada honorário, clicar em **Novo** e preencher:

| Campo | Instrução |
|---|---|
| Tipo de Honorário | `Honorários Advocatícios` (padrão) ou `Honorários Periciais - Contador/Engenheiro/Médico` |
| Descrição | Até 60 caracteres |
| Devedor | `Reclamante` ou `Reclamado` |
| Cobrar do Reclamante | Checkbox (somente se Devedor = Reclamante) |
| Tipo de Valor | `Calculado` ou `Informado` |
| Alíquota (se Calculado) | Percentual |
| Base (se Calculado) | `Bruto`, `Bruto (-) CS`, `Bruto (-) CS (-) PP` |
| Vencimento (se Informado) | Data de vencimento |
| Valor (se Informado) | Montante monetário |
| Índice de Correção | `Índice Trabalhista` ou `Outro Índice` |
| Aplicar Juros | Marcar se incidem juros de mora |
| Nome Completo do Credor | Nome do advogado/perito |
| Tipo de Documento Fiscal | `CPF`, `CNPJ` ou `CEI` |
| Número do Documento | CPF/CNPJ/CEI do credor |
| Apurar Imposto de Renda | Marcar se houver IR sobre honorários |
| Tipo IR | `IRPF` (tabela progressiva) ou `IRPJ` (1,5% fixo) |
| Incidir sobre Juros (IR) | Marcar para incluir juros na base do IR dos honorários |
| Identificação | ID do documento judicial |

Clicar em **Salvar** após cada lançamento.

---

## 17. Custas Judiciais

### Aba Custas Devidas

| Campo | Instrução |
|---|---|
| Base das Custas de Conhecimento e Liquidação | `Bruto Devido ao Reclamante` ou `Bruto + Outros Débitos da Reclamada` |
| Custas do Reclamante - Conhecimento | `Não se aplica` (padrão), `Calculada 2%` ou `Informada` |
| Custas do Reclamado - Conhecimento | `Calculada 2%` (padrão), `Informada` ou `Não se aplica` |
| Custas do Reclamado - Liquidação | `Não se aplica` (padrão), `Calculada 0,5%` ou `Informada` |
| Custas Fixas (Reclamado) | Informar Vencimento e quantidade de cada incidente: Atos OJ Urbana/Rural, Agravo de Instrumento/Petição, Impugnação, Embargos à Execução/Arrematação/Terceiros, Recurso de Revista |
| Autos (Reclamado) | Tipo: `Adjudicação`, `Arrematação` ou `Remissão`; Vencimento; Valor do Bem → Adicionar |
| Armazenamento (Reclamado) | Data Início, Valor do Bem → Adicionar; Data Término (opcional) |
| Identificação das Custas | ID do documento judicial |

> Mínimo de custas de conhecimento: R$ 10,64. Máximo de custas de liquidação: R$ 638,46.

### Aba Custas Recolhidas

| Campo | Instrução |
|---|---|
| Vencimento | Data do recolhimento |
| Valor | Montante recolhido |
| Ação | Clicar em **Adicionar** para cada recolhimento |

Clicar em **Salvar**.

---

## 18. Correção, Juros e Multa

### Aba Dados Gerais

| Campo | Instrução |
|---|---|
| Índice Trabalhista | `Tabela Única JT Diário` (padrão), `Tabela Única JT Mensal`, `TR`, `IGP-M`, `INPC`, `IPC`, `IPCA`, `IPCA-E`, `IPCA-E/TR` |
| Combinar com Outro Índice | Marcar + selecionar segundo índice + informar data de início |
| Ignorar Taxa Negativa | Marcar para excluir taxas negativas do índice |
| Juros de Mora | `Juros Padrão` (padrão): 0,5% a.m. até 26/02/1987, 1% capitalizado até 03/03/1991, 1% simples a partir de 04/03/1991 |
| Fazenda Pública | Marcar + informar data inicial para juros de 0,5% a.m. (limitado a 70% SELIC a partir de 04/05/2012) |
| Não Aplicar Juros | Marcar para suprimir juros de mora |

### Aba Dados Específicos

| Campo | Instrução |
|---|---|
| Base de Juros | `Verba` (padrão), `Verba (-) CS`, `Verba (-) CS (-) PP` |
| FGTS | `Utilizar Índice Trabalhista` (padrão) ou `Utilizar Índice JAM` |
| Previdência Privada | `Utilizar Índice Trabalhista` (padrão) ou `Utilizar Outro Índice` + checkbox Juros |
| Custas Judiciais | Padrão: sem atualização; marcar `Índice Trabalhista` ou `Outro Índice` + checkbox Juros |
| CS Salários Devidos / Pagos - Atualização | `Trabalhista` (correção somente, juros a partir do dia 2 do mês seguinte à liquidação) ou `Previdenciária` (UFIR + SELIC desde a prestação do serviço) ou ambas |
| Multa Previdenciária | `Urbana`/`Rural` + `Integral`/`Reduzido` (somente com Atualização Previdenciária) |

Clicar em **Salvar**.

---

## 19. Regerar Ocorrências (se aplicável)

**Quando:** Após alterar qualquer parâmetro que afeta as ocorrências (período, carga horária, prescrição, base de cálculo, divisor, multiplicador). **Obrigatório antes de liquidar** quando houve alterações nos parâmetros.

1. Navegar para aba **Verbas** (listagem principal).
2. Na seção "Regeração de Ocorrências", selecionar **"Manter alterações realizadas nas ocorrências"** (padrão seguro) ou **"Sobrescrever"** (resetar tudo).
3. Clicar em **Regerar** (`formulario:regerarOcorrencias`).
4. Confirmar no `window.confirm` que aparece.
5. Aguardar AJAX completar a regeneração.

> **Armadilha:** Não regerar após alterações estruturais → ocorrências antigas permanecem ativas com valores desatualizados → liquidação com valores incorretos.

---

## 20. Operações → Liquidar

1. Clicar em **Operações** → **Liquidar**.
2. Informar a **Data da Liquidação**.
3. Selecionar critério de **Acumulação dos Índices de Correção**:
   - A partir do mês subsequente ao vencimento (todas as verbas).
   - A partir do mês de vencimento (todas as verbas).
   - Misto: subsequente para verbas mensais + mês de vencimento para anuais/rescisórias.
4. Verificar **Pendências do Cálculo**:
   - **Alerta** (ícone laranja): não impede liquidação, mas deve ser avaliado.
   - **Erro** (ícone vermelho): impede liquidação; clicar na pendência para ir à página correspondente e corrigir.
5. Clicar em **Liquidar**.

---

## 20. Operações → Imprimir

1. Clicar em **Operações** → **Imprimir**.
2. Selecionar os relatórios desejados (padrão: todos marcados):
   - Resumo de Cálculo
   - Critério de Cálculo e Fundamentação Legal
   - Dados do Cálculo, Faltas e Férias, Histórico Salarial
   - Verbas, Juros sobre Verbas
   - Salário-família, Seguro-desemprego, FGTS
   - Contribuição Social, Previdência Privada, Pensão Alimentícia, Imposto de Renda
   - Multas/Indenizações, Honorários, Custas Judiciais
3. Clicar em **Imprimir**.

---

## Outras Operações

| Operação | Instrução |
|---|---|
| **Fechar** | Fecha o cálculo sem excluir (Operações → Fechar ou ícone na página Dados do Cálculo) |
| **Excluir** | Exclui permanentemente o cálculo aberto (pede confirmação) |
| **Exportar** | Gera arquivo XML do cálculo para backup ou importação em outra instância |
| **Importar** | Importa arquivo XML exportado pelo PJe-Calc (Aba Cálculo → Importar Cálculo) |
| **Validar** | Exclusivo da versão online: torna o arquivo disponível para download no PJe-JT |
| **Duplicar** | Cria cópia do cálculo (Aba Cálculo → Buscar → ícone Duplicar) |

---

## Fase de Atualização (pós-liquidação)

Após liquidar, o menu lateral exibe a aba **Atualização** com as seguintes subpáginas:

| Subpágina | Uso |
|---|---|
| Pensão Alimentícia | Incluir pensão determinada após a liquidação original |
| Dados do Pagamento | Registrar pagamentos parciais liberados ao reclamante |
| Multas e Indenizações | Incluir novas multas/indenizações determinadas na fase de execução |
| Honorários | Incluir novos honorários determinados na fase de execução |
| Custas Judiciais | Acrescentar custas de atos processuais ocorridos após a liquidação |
| Liquidar Atualização | Informar nova data de liquidação e ID do cálculo → Liquidar |
| Imprimir Atualização | Imprimir relatórios da atualização |

---

## Dúvidas Frequentes (FAQ)

### Como calcular a média da quantidade para verbas reflexas?

O sistema transforma os valores Devidos ou Diferenças da verba principal em quantidades e apura a média duodecimal. O período da média depende da ocorrência de pagamento da verba reflexa:
- **Desligamento:** últimos 12 meses do contrato.
- **Dezembro:** ano civil.
- **Período Aquisitivo:** período aquisitivo.

Tratamento de meses incompletos: `Manter` | `Integralizar` | `Desprezar` | `Desprezar < 15 dias`.

### Como informar valores devidos diretamente nas ocorrências?

1. Parâmetros da Verba → alterar Valor para `Informado` → informar valor → Salvar.
2. Na lista de verbas, clicar em **Regerar**.
3. Para valores variáveis: clicar em **Ocorrências** → editar mês a mês ou via **Alteração em Lote**.

### Como incluir verbas com vencimento após a data da demissão?

1. Dados do Cálculo → Parâmetros → informar a data do vencimento no campo **Data Final** → Salvar.
2. Verbas → Expresso → marcar a verba → Salvar.
3. Parâmetros da Verba → alterar Ocorrência de Pagamento para `Mensal` → informar período igual à data de vencimento → desmarcar Proporcionar → Salvar.
4. Regerar as ocorrências.

### Como apurar FGTS sobre Férias + 1/3 indenizadas?

O sistema não apura automaticamente. Solução:
1. FGTS → Ocorrências → acrescentar o valor de Férias + 1/3 à base da ocorrência da demissão → Salvar.
2. Reliquidar o cálculo.

---

## Referências

- `references/01-parametros-calculo.md` — Detalhamento completo dos Parâmetros do Cálculo
- `references/02-verbas-catalogo.md` — Catálogo de verbas padrão e seus parâmetros
- `references/03-historico-salarial.md` — Regras de lançamento do Histórico Salarial
- `references/04-fgts-contribuicao-social.md` — FGTS e Contribuição Social em detalhe
- `references/05-correcao-juros.md` — Índices de correção e tabelas de juros
- `references/06-exemplos-praticos.md` — 10 exemplos resolvidos do tutorial oficial
- `references/07-automacao-playwright.md` — Seletores CSS/XPath e estratégias de automação
