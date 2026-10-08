# IAS 37 — Provisions, Contingent Liabilities and Contingent Assets

## 1. IAS 37 vs. CPC 25 — Equivalência e Diferenças

**IAS 37** (norma IFRS internacional) e **CPC 25** (norma brasileira) são praticamente idênticas em estrutura e finalidade. CPC 25 foi traduzido e adaptado para o contexto legal brasileiro, mas mantém os mesmos princípios.

| Aspecto | IAS 37 | CPC 25 | Nota |
|--------|--------|--------|------|
| Probabilidade mínima para provisão | >50% | >50% legalmente, >70% em prática BR | Brasil é mais conservador |
| Reconhecimento em balanço | Sim, se provável | Sim, se provável | Idêntico |
| Divulgação em nota | Sim | Sim | Idêntico |
| Desconto a valor presente | Sim (se material) | Sim (se material) | Idêntico |
| Câmbio (provisões multmoeda) | Reavaliação a cada fechamento | Reavaliação a cada fechamento | Idêntico |
| Reversão de provisão (se não ocorrer) | Sim; reduz despesa | Sim; reduz despesa | Idêntico |

---

## 2. Conceitos-chave de IAS 37

### 2.1 Provisão (Provision)

**Definição**: Passivo de prazo ou valor incerto que surge de evento passado.

**Requisitos para reconhecimento**:
1. **Obrigação presente** (legal ou construída) resultado de evento passado
2. **Saída de recurso** é provável (>50%)
3. **Estimativa confiável** do valor

**Exemplo**: Sentença condenatória transitada em julgado → obrigação legal, saída provável, valor é certo = **PROVISIÓN**.

### 2.2 Passivo Contingente (Contingent Liability)

**Definição**: Possível obrigação que depende de evento futuro incerto, OU obrigação presente onde saída é possível (não provável).

**Critério de reconhecimento**: **Não é reconhecido** no balanço. Apenas **divulgado** em nota explicativa.

**Divulgação exigida**:
- Descrição da contingência
- Estimativa financeira (se possível)
- Incertezas quanto ao valor e prazo
- Possibilidade de reembolso (seguro, terceiros)

**Exemplo**: Ação cível em 1ª instância; jurisprudência dividida; valor estimado R$ 2M = **PASSIVO CONTINGENTE** (divulgar em nota, não provisionar).

### 2.3 Ativo Contingente (Contingent Asset)

**Definição**: Possível ativo dependente de evento futuro incerto.

**Critério de reconhecimento**: **Nunca é reconhecido** (nem em balanço nem em nota detalhada). Apenas **mencionado discretamente** em nota se ingressos de benefícios são prováveis.

**Razão**: Prudência; risco de valorização indevida.

**Exemplo**: Ação trabalhista contra terceiro com sentença favorável em 1ª instância; apelação em andamento = **ATIVO CONTINGENTE** (menção discreta em nota "Há ação contra terceiro em andamento; benefício incerto").

---

## 3. Critério de Probabilidade — IAS 37

### 3.1 Escala de três níveis

IAS 37.24 a IAS 37.35 definem:

| Nível | Termo | Probabilidade | Ação |
|-------|-------|---------------|------|
| **Alto** | Probable | >50% | Reconhecer provisão |
| **Médio** | Possible | 20-50% | Divulgar em nota (passivo contingente) |
| **Baixo** | Remote | <20% | Não divulgar, salvo casos especiais |

**Nota**: IAS 37.24 usa "more likely than not" como padrão; isso significa >50%, não >70%.

### 3.2 Aplicação prática da escala

**Probable (>50%)**:
- Decisão desfavorável em instância superior
- Jurisprudência consolidada contra
- Confissão de culpa/responsabilidade
- → **Reconhecer provisão integral**

**Possible (20-50%)**:
- Processo em andamento; desfecho incerto
- Jurisprudência dividida
- Tese legal argumentável, mas não consolidada
- → **Divulgar em nota; não reconhecer no balanço**

**Remote (<20%)**:
- Jurisprudência sólida a favor
- Precedentes do STF/STJ consolidados
- → **Não divulgar; exceto exceções graves**

---

## 4. Reconhecimento de Provisão — Critérios Detalhados

### 4.1 Teste de reconhecimento (3 testes em série)

```
┌─────────────────────────────────────┐
│ Existe OBRIGAÇÃO PRESENTE?          │
│ (legal ou construída)               │
└─────────────────────────────────────┘
                 SIM → continuar
                 NÃO → Parar; não reconhecer

┌─────────────────────────────────────┐
│ Saída de RECURSO é PROVÁVEL?        │
│ (>50%)                              │
└─────────────────────────────────────┘
                 SIM → continuar
                 NÃO → Parar; divulgar como contingente

┌─────────────────────────────────────┐
│ Pode ESTIMAR o valor com            │
│ CONFIABILIDADE?                     │
└─────────────────────────────────────┘
                 SIM → RECONHECER PROVISÃO
                 NÃO → Parar; não reconhecer (impossível)
```

---

## 5. Mensuração (Measurement) — Métodos Aceitos

### 5.1 Melhor estimativa (Best Estimate)

IAS 37.36 exige usar a melhor estimativa do valor exigível.

**Opção 1: Método Único**
- Usar o valor mais provável de saída
- Apropriado quando há um desfecho claro dominante
- Exemplo: Sentença transitada de R$ 1M → provisão = R$ 1M

**Opção 2: Método do Valor Esperado (Expected Value)**
- Ponderar todos os cenários por probabilidade
- Apropriado quando há múltiplos desfechos possíveis
- Exemplo:
  - 60% chance de pagar R$ 2M
  - 40% chance de pagar R$ 500K
  - Valor esperado = (60% × 2M) + (40% × 500K) = R$ 1.4M

**Opção 3: Amplitude com ponto médio**
- Usar gama de valores; tomar ponto médio como estimativa
- Apropriado quando há grande incerteza
- Exemplo: Valor entre R$ 1M e R$ 3M → provisão ≈ R$ 2M

### 5.2 Desconto a Valor Presente (quando aplicável)

IAS 37.45-47: Se o efeito do desconto for material:
- Descontar a valor presente usando taxa apropriada (taxa sem risco ou taxa de mercado)
- Aplicável principalmente a provisões de prazo longo (>2 anos)

**Exemplo de desconto**:
- Obrigação exigível em 5 anos: R$ 10M
- Taxa de desconto: 6% a.a.
- Valor presente = R$ 10M / (1.06^5) = R$ 7.47M
- Diferença desconto = R$ 2.53M (reconhecido como receita financeira até vencimento)

**Critério para aplicar desconto**:
- Geralmente aplicar se prazo >2 anos
- Débito previdenciário de longo prazo: sempre descontar
- Processos judiciais: geralmente não descontar (prazo < 2 anos em média BR)

---

## 6. Divulgação em Notas Explicativas — Requisitos IAS 37

### 6.1 Divulgação de Provisões (reconhecidas)

Para cada classe de provisão, divulgar:

| Item | Descrição |
|------|-----------|
| Saldo inicial | Provisão no início do período |
| Adições | Novas provisões criadas no período |
| Aumentos por indexação | Ajustes por inflação, juros |
| Utilizações | Saídas caixa para liquidação |
| Reversões | Cancelamento de provisões não utilizadas |
| Saldo final | Provisão ao final do período |

**Template de divulgação**:

```
Nota X — Provisões

                                  Trabalhista  Cível  Tributária  Total
Saldo em [data anterior]           R$ 2.500    R$ 1.200  R$ 5.000  R$ 8.700
Adições                            R$ 1.200    R$ —      R$ —      R$ 1.200
Aumentos por juros/correção        R$ 150      R$ 80     R$ 300    R$ 530
Utilizações (caixa)               (R$ 800)    (R$ 50)   (R$ —)    (R$ 850)
Reversões (não utilizadas)        (R$ 100)    (R$ —)    (R$ —)    (R$ 100)
─────────────────────────────────────────────────────────────────────────
Saldo em [data atual]             R$ 2.950    R$ 1.230  R$ 5.300  R$ 9.480
═════════════════════════════════════════════════════════════════════════
```

### 6.2 Divulgação de Passivos Contingentes (não reconhecidos)

Para cada classe material:

| Item | Descrição |
|------|-----------|
| Descrição | Natureza da contingência |
| Estimativa financeira | Valor estimado (se possível) |
| Incertezas | Fatores que afetam valor/prazo |
| Reembolsos | Possibilidade de reembolso por terceiros/seguro |

**Template**:

```
Nota Y — Passivos Contingentes

A empresa é réu em ações judiciais não provisionadas:

1) Ação cível de responsabilidade civil:
   - Número CNJ: [xxx]
   - Valor estimado: R$ 2.000 a R$ 5.000 (mil)
   - Fase: 1ª instância; em instrução
   - Probabilidade: Possível (30-50%)
   - Estimativa mais provável: R$ 3.500 (mil)
   - Incerteza: Quantum danorum depende de perícia não finalizada

2) Auto de infração tributária:
   - Matéria: ICMS diferencial
   - Valor: R$ 1.200 (mil) + multa (75%)
   - Fase: Impugnação em CARF
   - Probabilidade: Possível (40-60%)
   - Incerteza: Jurisprudência dividida; tese inovadora
```

---

## 7. Diferenças IAS 37 vs. Prática Brasileira

| Aspecto | IAS 37 Puro | Prática BR (Big Four) | Razão |
|--------|-------------|----------------------|-------|
| Threshold probabilidade | >50% | >70% | Conservadorismo BR |
| Desconto a VP | Sempre, se material | Raramente (não usual BR) | Mercado BR evita VP em curto prazo |
| Jurisprudência como "provável" | Sim (após algumas decisões) | Mais cautela; requer consolidação | Sistema legal BR tende a reversões |
| Passivos trabalhistas em execução | 50-70% provável | 95%+ provável | Particularidade BR; execução muito eficaz |
| Ativos contingentes | Não reconhecer em balanço | Idem | Idêntico |
| Reversão de provisão | Reconhecida em resultado | Idem | Idêntico |

**Conclusão**: CPC 25 adota IAS 37, mas prática brasileira é mais conservadora. Ao reportar a auditores, sempre explicitar qual critério está sendo usado.

---

## 8. Exemplo Prático Completo de Divulgação

### Cenário: Empresa com 3 tipos de contingências

**Dados coletados**:
- Processo trabalhista (sentença transitada): R$ 800K
- Ação cível (em 1ª instância): R$ 2-5M
- Auto de infração (CARF): R$ 1.2M + multa (75%)

### Passo 1: Classificar cada contingência

| Tipo | Probabilidade | Ação | Valor |
|------|---------------|------|-------|
| Trabalhista | 100% (trânsito) | Reconhecer provisão | R$ 800K |
| Cível | 40% (1ª instância) | Divulgar em nota | R$ 2-5M |
| Tributária | 50% (em CARF) | Divulgar em nota | R$ 1.2-2.1M (c/ multa) |

### Passo 2: Gerar divulgação

```
Nota Z — Provisões e Passivos Contingentes

A. PROVISÕES RECONHECIDAS

                                        2025        2024
Contingências trabalhistas:
  Saldo inicial                      R$ —        R$ —
  Adições                            R$ 800      R$ —
  Utilizações                        R$ —        R$ —
  Saldo final                        R$ 800      R$ —

Total de provisões                   R$ 800      R$ —

B. PASSIVOS CONTINGENTES NÃO PROVISIONADOS

Classe: Ações Cíveis

1) Responsabilidade Civil — Atraso de Entrega
   Tribunal: TJ-SP, Vara Cível
   Número CNJ: [xxx]
   Petição inicial: 2024
   Valor reclamado: R$ 2.000 a R$ 5.000 (mil)
   Estimativa mais provável: R$ 3.500 (mil)
   Probabilidade: Possível (estimado 35-45%)

   Fundamentação: Ação em fase inicial de instrução. Jurisprudência TJ-SP favorável
   a reconhecimento de danos em 70% dos casos similares. Perícia em agendamento.
   Valor dependerá da extensão de dano comprovado.

Classe: Contingências Tributárias

2) Auto de Infração — ICMS Diferencial
   Autoridade: Secretaria da Fazenda — SP
   Número: [xxx]
   Período: 2023-2024
   Valor em discussão: R$ 1.200 (mil) débito + R$ 900 (mil) multa (75%)
   Total em risco: R$ 2.100 (mil)
   Probabilidade: Possível (estimado 45-55%)

   Fundamentação: Impugnação em trâmite na CARF (1ª câmara). Jurisprudência TRF-2ª
   favorável ao fisco em 60% dos casos. Tese da empresa baseada em jurisprudência
   internacional (Tratados). Julgamento previsto para 2026.

Exposição Total — Passivos Contingentes: R$ 5.600 (mil)
```

---

## 9. Critérios de Auditoria — Expectativas Big Four

### 9.1 Procedimentos padrão de auditoria em contingências

Auditores experientes verificam:

1. **Existência e completude**
   - ✓ Todos os processos conhecidos foram incluídos?
   - ✓ Lei de confirmação com advogados externos (carta do advogado)?
   - ✓ Relatório de gestão jurídica formalizado?

2. **Classificação correta**
   - ✓ Provável vs. Possível está bem documentado?
   - ✓ Há fundamentação legal citada (decisão, jurisprudência)?
   - ✓ Jurisprudência recente foi considerada?

3. **Mensuração adequada**
   - ✓ Valor está atualizado e fundamentado?
   - ✓ Descontos (se aplicados) usam taxa apropriada?
   - ✓ Comparação histórica: reclassificações posteriores (processo que foi "possível" e virou "provável") estão documentadas?

4. **Divulgação completa**
   - ✓ Nota explicativa foi elaborada conforme modelo?
   - ✓ Riscos e incertezas foram comunicados?
   - ✓ Reembolsos (seguro) foram identificados e divulgados?

### 9.2 Red flags comuns (sinais de alerta)

Auditores ficam atentos a:

- Reclassificação de "Possível" → "Remoto" sem fato novo documentado
- Valor de "Provável" muito abaixo do valor da causa (sem justificativa)
- Falta de carta do advogado externo confirmando análise
- Processo com sentença condenatória não provisionado como "Possível" (erro claro)
- Passivo Contingente com estimativa vaga ("R$ 1M a R$ 100M")
- Ausência de divulgação de mudanças vs. período anterior

---

## 10. Template Auditável para Divulgação de Contingências

Use este template para gerar notas que passem por auditoria externa:

```
CONTINGÊNCIAS JURÍDICAS — Nota [X]

Contexto regulatório: A empresa aplica CPC 25 / IAS 37 em conformidade com
as normas contábeis brasileiras (Lei 11.638/2007). Provisões são reconhecidas
quando existe obrigação presente resultante de evento passado, saída de recurso
é provável (>50%, com aplicação de critério conservador >70% em prática de
mercado), e o valor pode ser estimado com confiabilidade.

A. PROVISÕES RECONHECIDAS NO BALANÇO

[Tabela com saldo anterior, adições, utilizações, reversões, saldo atual]

Maior risco individual: Processo trabalhista [Descrição] - R$ [valor]
Fundamentação: Sentença transitada em julgado, obrigação legal certa.

B. PASSIVOS CONTINGENTES DIVULGADOS EM NOTA

[Tabela com descrição, valor estimado, probabilidade, fundamento]

Risco agregado — Possível: R$ [valor total]
Risco agregado — Remoto: R$ [valor total, se divulgado]

C. VARIAÇÕES E RECLASSIFICAÇÕES

[Processos que mudaram de categoria no período]

Certificação: As avaliações foram validadas por advogado externo independente
[nome, OABXXX] em [data].
```

---

## Referências Normativas

- **IAS 37** — IFRS Foundation (https://www.ifrs.org)
- **CPC 25** — Comitê de Pronunciamentos Contábeis (https://www.cpc.org.br)
- **NBC TG 25** — Norma Brasileira de Contabilidade para Auditores (IAESB)
- **CVM Instruction 457/2007** — Regulações para companhias abertas
- **Big Four Guidance**:
  - Deloitte: "Provisions, Contingent Liabilities and Contingent Assets"
  - PwC: "In Depth: IAS 37 Provisions, Contingent Liabilities and Contingent Assets"
  - EY: "IAS 37 Illustrative Examples and Application Guidance"
  - KPMG: "IAS 37 Illustrative Examples"
