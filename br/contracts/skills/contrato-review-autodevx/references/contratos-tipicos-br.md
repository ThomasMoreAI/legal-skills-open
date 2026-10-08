# Contratos Típicos — Cláusulas padrão por tipo no Brasil

## 1. Prestação de Serviços

### Referência legal
- CC art. 593-609 (locação de serviços)
- Lei 8.078/1990 (CDC, se consumidor)

### Cláusulas obrigatórias

| Cláusula | Essencial? | Função |
|----------|-----------|--------|
| **Objeto e escopo** | SIM | Descrever serviço em detalhes mensuráveis |
| **Prazo de execução** | SIM | Data de início, entrega, marcos |
| **SLA / Disponibilidade** | SIM (TI) | Uptime esperado, penalidades |
| **Remuneração e forma de pagamento** | SIM | Valor, parcelamento, reajuste |
| **Propriedade Intelectual (PI)** | SIM (TI) | Quem detém direitos sobre produto/código |
| **Confidencialidade** | RECOMENDADO | Duração, definição de "confidencial" |
| **Responsabilidade por atrasos** | SIM | Multa diária ou percentual |
| **Garantia de trabalho** | RECOMENDADO | Período de correção de vícios |

### Omissões críticas

- **Falta de SLA**: Impossível cobrar por não-execução
- **PI ambígua**: Litígio sobre propriedade do código/produto
- **Sigilo indefinido**: Obrigação sem fim é questionável
- **Garantia ausente**: Risco de serviço defeituoso ficar com cliente

### Riscos típicos

1. **Escopo expansivo**: Serviço indefinido; cliente solicita mais; preço não acompanha
   - Solução: Especificar "serviço fora de escopo requer aditivo contratual"

2. **Exclusão unilateral de responsabilidade**
   - Risco: Nula se exclui culpa grave (CC art. 422)
   - Redação segura: "Responsabilidade limitada a 1x o valor mensal, exceto dolo"

3. **Alteração unilateral de preço**
   - Risco: Abusiva sem índice
   - Redação segura: "Reajuste anual por IPCA, com aviso 30 dias antes"

### Exemplo de SLA bem construído

```markdown
#### SLA (Acordo de Nível de Serviço)

- **Disponibilidade garantida**: 99,5% no mês (máx 3h36m de inatividade)
- **Tempo de resposta a incidentes**: 4 horas (críticos) / 24 horas (não-críticos)
- **Tempo de resolução**: 8 horas (críticos) / 5 dias úteis (não-críticos)
- **Crédito por não-conformidade**:
  - 99,0%-99,5%: 10% da mensalidade
  - 98,0%-99,0%: 25% da mensalidade
  - <98,0%: 50% da mensalidade
- **Exclusões**: Atos de cliente, força maior, manutenção programada (1x/mês, comunicada com 7 dias)
```

---

## 2. Compra e Venda (Mercadoria)

### Referência legal
- CC art. 481-504 (compra e venda)
- Lei 8.078/1990 (CDC, se consumidor)

### Cláusulas obrigatórias

| Cláusula | Essencial? | Função |
|----------|-----------|--------|
| **Descrição do bem** | SIM | Tipo, quantidade, qualidade |
| **Preço e condições** | SIM | Valor total, desconto, frete |
| **Entrega** | SIM | Prazo, local, risco de transporte |
| **Vício e garantia** | SIM | Prazo de denúncia, período de garantia |
| **Responsabilidade por transporte** | SIM | FOB / CIF / EXW (Incoterms) |
| **Recebimento e aceitação** | RECOMENDADO | Prazo para inspeção, aceite tácito |
| **Devolução** | RECOMENDADO | Prazo de devolução, reembolso |

### Omissões críticas

- **Sem especificação de bem**: Indefinição; litígio sobre qualidade
- **Garantia ausente**: Risco passa integralmente ao comprador
- **Responsabilidade de transporte indefinida**: Disputa sobre perdas/danos
- **Sem prazo de aceite**: Aceite tácito indefinido

### Riscos típicos

1. **Vício oculto não detectado na entrega**
   - Fundamento legal: CC art. 441 (prazo de denúncia razoável; se bem durável, 30 dias)
   - Solução: Inspeção em 7-15 dias; relatório por escrito

2. **Cláusula que exclui garantia**
   - Risco: Nula para consumidor (CDC art. 51, I); questionável entre empresas
   - Redação segura: "Produto em estado 'como se vê'; garantia de 6 meses contra vícios ocultos"

3. **Responsabilidade durante transporte**
   - Fundamento: CC art. 505 (risco passa ao comprador após entrega; durante transporte, depende de quem transporta)
   - Solução: Especificar Incoterm (FOB, CIF, EXW) e quem contrata seguro

### Exemplo de cláusula de garantia clara

```markdown
#### Garantia de Produto

**Prazo**: 6 meses a contar da entrega

**Cobertura**: Vícios aparentes e ocultos; falhas de fabricação

**Exclusões**: Danos por uso indevido, negligência do comprador, alterações não autorizadas

**Procedimento**:
1. Comprador notifica vendedor por escrito em até 7 dias do descoberta do vício
2. Vendedor inspeciona em até 5 dias úteis
3. Se confirmado: substituição (novo produto) ou devolução com reembolso total
4. Custos de devolução: por conta do vendedor se vício comprovado
```

---

## 3. Locação

### Referência legal
- **Lei 8.245/1991** (Lei de Locação Residencial e Não-Residencial)
- CC art. 565-578 (locação genérica)

### Cláusulas obrigatórias (Lei 8.245/91)

| Cláusula | Essencial? | Função |
|----------|-----------|--------|
| **Partes e qualificação** | SIM | Locador, locatário, dados completos |
| **Bem locado** | SIM | Descrição, endereço, características |
| **Prazo de locação** | SIM | Mínimo 30 dias; se residencial, presunção de renovação tácita a cada 2 anos |
| **Aluguel e reajuste** | SIM | Valor mensal, índice (IGPM, IPCA, convenção setorial) |
| **Depósito caução** | SIM | Até 3 aluguéis (residencial); até 6 aluguéis (comercial) |
| **Obrigações de locador** | SIM | Conservação do imóvel, tolerância de reforma |
| **Obrigações de locatário** | SIM | Pagamento, conservação, não-alteração estrutural |
| **Rescisão e devolução** | SIM | Aviso prévio, estado de repouso, multas |

### Omissões críticas

- **Sem cláusula de reajuste**: Problema; Lei 8.245/91 presume reajuste automático se prazo >1 ano
- **Caução indefinida**: Risco de interpretação; Lei limita a 3x aluguel (residencial)
- **Responsabilidade por obras ausente**: Disputa sobre reforma/danificação
- **Sem indicação de índice**: Reajuste indefinido

### Riscos típicos

1. **Cláusula que impede reforma/melhoria**
   - Fundamento: Lei 8.245/91 art. 23 (locador deve tolerar benfeitorias úteis; compensável)
   - Solução: "Benfeitorias necessárias: direito do locatário; compensáveis na devolução"

2. **Multa por rescisão antecipada excessiva**
   - Lei 8.245/91 art. 27: Multa não pode ser abusiva (limite sugerido: 3x aluguel)
   - Solução: Especificar "multa de 3x aluguel (estimada em danos)" ou "sem multa se com 30 dias de aviso"

3. **Caução acumulada com outras garantias**
   - Risco: Abusivo; lei limita a 3x aluguel total
   - Solução: "Caução de 3 aluguéis OU 6 aluguéis seguro-caução (escolher um)"

### Exemplo de cláusula de rescisão clara

```markdown
#### Rescisão Antecipada

**Direito**: Locatário pode rescindir com aviso prévio de 30 dias (Lei 8.245/91 art. 27)

**Multa por rescisão antecipada**:
- Antes de 6 meses: 3 aluguéis (estimativa de danos)
- Após 6 meses: 1 aluguel
- Nenhuma multa se período mínimo (12 meses) for cumprido

**Devolução**: Imóvel em "estado de repouso" (como recebido), com:
- Todas as chaves
- Contas de água/luz/gás quitadas
- Sem deixa (danos materiais à estrutura)
```

---

## 4. NDA (Non-Disclosure Agreement / Confidencialidade)

### Referência legal
- CC art. 191-194 (sigilo e direitos da personalidade)
- Lei 12.965/2014 (Marco Civil, para dados online)
- LGPD (se dados pessoais estiverem envolvidos)

### Cláusulas obrigatórias

| Cláusula | Essencial? | Função |
|----------|-----------|--------|
| **Definição de "Informação Confidencial"** | SIM | Escrito, oral, visual — deve ser declarada |
| **Exclusões** | SIM | Domínio público, pré-conhecimento, obrigação legal |
| **Prazo de sigilo** | SIM | Duração da obrigação (ex: 2-5 anos após término) |
| **Uso permitido** | SIM | Somente para fins descritos no contrato |
| **Restrição de divulgação** | SIM | Quem pode ter acesso (empregados, subcontratados?) |
| **Devolução/destruição** | SIM | Restituição ou destruição ao término |
| **Penalidade por violação** | RECOMENDADO | Multa ou indenização |
| **Lei aplicável** | SIM | Legislação brasileira presumida; especificar se outra |

### Omissões críticas

- **Sem definição clara de "confidencial"**: O que é protegido? Difícil cobrar
- **Prazo indefinido**: "Perpetuamente" é questionável; prescrição típica 2-5 anos
- **Sem exceções**: Obrigação absoluta é irreal (exigências legais existem)
- **Sem devolução/destruição**: Risco de continuação indefinida

### Riscos típicos

1. **Prazo indefinido de sigilo**
   - Risco: Nula por tempo indeterminado (CC art. 421-422, boa-fé); restringe liberdade
   - Solução: "Sigilo por 3 anos após término" OU "indefinido, mas exigência legal prevalece"

2. **Definição genérica de "Confidencial"**
   - Risco: Tudo pode ser interpretado como confidencial
   - Redação segura: "Informação escrita como 'CONFIDENCIAL' ou declarada verbalmente e confirmada por escrito em 5 dias"

3. **Exclusão de informação gerada independentemente**
   - Solução: "Sigilo não se aplica a informação que se descobre independentemente, sem acesso à confidencial"

### Exemplo de cláusula de NDA bem construída

```markdown
#### Confidencialidade

**Definição**: Informação confidencial é aquela:
- Claramente marcada como "CONFIDENCIAL" por escrito, OU
- Declarada verbalmente e confirmada por escrito em até 5 dias

**Exclusões** (não são confidenciais):
- Já conhecida antes do contato (com prova)
- Domínio público (sem culpa de receptor)
- Recebida de terceiro sem obrigação de sigilo
- Desenvolvida independentemente (com prova)
- Exigida por lei ou ordem judicial

**Prazo**: 3 anos após término do contrato

**Uso**: Somente para fins descritos; acesso restrito a colaboradores com necessidade conhecer

**Devolução**: Ao término, devolver ou destruir documentos; manter cópia somente para cumprimento legal

**Penalidade**: Violação acarreta indenização por danos, sem limite máximo de responsabilidade
```

---

## 5. Licença de Software / SaaS

### Referência legal
- CC art. 481-504 (analogia a compra e venda de direito)
- Lei 9.609/1998 (Lei de Software)
- Lei 12.965/2014 (Marco Civil)
- LGPD (dados pessoais do cliente)

### Cláusulas obrigatórias

| Cláusula | Essencial? | Função |
|----------|-----------|--------|
| **Licença vs. Propriedade** | SIM | Deixar claro: cliente NÃO é dono do software |
| **Escopo de uso** | SIM | Não-transferível, não-comercializável, 1 empresa ou múltiplas? |
| **SLA e uptime** | SIM (SaaS) | Tempo de atividade esperado; penalidades |
| **Propriedade de dados** | SIM | Quem detém dados da empresa do cliente |
| **Portabilidade/Exportação** | SIM | Direito de sair; formato de dados ao término |
| **Suporte e manutenção** | RECOMENDADO | Horário, responsividade, inclusão em preço |
| **Atualização** | RECOMENDADO | Obrigatoriedade, custo, breaking changes |
| **Limitação de responsabilidade** | SIM | Deve ser bilateral; limitar a valor contratado |
| **Rescisão** | SIM | Direito a cancelar sem multa após período mínimo |

### Omissões críticas

- **Sem SLA**: Impossível reclamar de inatividade
- **Dados presos**: Cliente não consegue sair (vendor lock-in)
- **Responsabilidade exagerada**: "Não somos responsáveis por nada" é nula
- **Licença ambígua**: Posso usar para múltiplas empresas? Revender?

### Riscos típicos

1. **SLA questionável ou ausente**
   - Solução: "99,5% de uptime mensal (máx 3h36m); crédito de 10% da mensalidade se não atingir"

2. **Limitação de responsabilidade excessiva**
   - Risco: Nula se exclui dolo ou culpa grave (CC art. 422)
   - Redação segura: "Responsabilidade limitada a 12 meses de faturamento, exceto dolo ou violação de LGPD"

3. **Exportação de dados impossível ou cara**
   - Risco: Abusiva (viola LGPD art. 50, portabilidade)
   - Solução: "Exportação em formato aberto (CSV, JSON) sem custo adicional, em até 30 dias"

4. **Atualização obrigatória com breaking changes**
   - Solução: "Atualizações não-quebrantes são obrigatórias; quebrantes permitem rejeição ou prazo de adaptação (60 dias)"

### Exemplo de cláusula de SaaS bem construída

```markdown
#### Software como Serviço (SaaS)

**Licença**: Não-transferível; uso exclusivo da empresa contratante

**Dados**: Propriedade do cliente. Fornecedor atua como Operador de Dados (LGPD)

**SLA**:
- Uptime: 99,5% mensal (máx 3h36m de inatividade)
- Crédito: 10% mensalidade se 99,0%-99,5%; 25% se <99,0%
- Exclusões: Manutenção programada (1x/mês, 7 dias de aviso)

**Portabilidade**: Cliente pode exportar dados em CSV/JSON sem custo, em até 30 dias, a qualquer tempo

**Rescisão**: Qualquer parte pode rescindir com 30 dias de aviso; dados exportáveis; reembolso proporcional se mensal

**Responsabilidade**: Limitada a 12 meses de faturamento, exceto dolo ou violação de LGPD
```

---

## 6. Contrato de Trabalho

### Referência legal
- **CLT (Decreto-Lei 5.452/1943)** — Lei do Trabalho
- CC art. 442-456 (contrato de trabalho)
- Lei 10.406/2002 (CC, em conformidade com CLT)

### Cláusulas obrigatórias (CLT)

| Cláusula | Essencial? | Função |
|----------|-----------|--------|
| **Partes e qualificação** | SIM | Empregado, empregador, CNPJ, cargo |
| **Salário** | SIM | Valor, forma de pagamento, desconto legal |
| **Jornada** | SIM | Horário de trabalho, período de descanso |
| **Função e responsabilidades** | SIM | Descrição do cargo |
| **Benefícios** | RECOMENDADO | VT, VA, seguro saúde, etc. |
| **Propriedade Intelectual** | RECOMENDADO | Quem detém direitos de criação |
| **Confidencialidade** | RECOMENDADO | Obrigação de sigilo durante e após |
| **Não-concorrência** | RECOMENDADO | Período e limitação geográfica |
| **Aviso prévio** | SIM | Prazo (CLT presume 30 dias) |

### Omissões críticas

- **Sem descrição de função**: Disputa sobre obrigações do empregado
- **PI ambígua**: Quem é dono de código/invenção criada?
- **Não-concorrência sem limite temporal/geográfico**: Nula ou questionável
- **Confidencialidade indefinida**: Risco de perpetuidade

### Riscos típicos

1. **Não-concorrência irreal**
   - Fundamento: STJ, REsp 1.252.893/SP (máx 2-3 anos, raio geográfico)
   - Redação segura: "Empregado não trabalha para concorrentes por 2 anos, em raio de 50km, em troca de 3 meses de salário"

2. **Renúncia de direitos trabalhistas**
   - Risco: Nula (CLT art. 444)
   - Solução: Nunca incluir; direitos não-renunciáveis

3. **Propriedade Intelectual genérica**
   - Solução clara: "Criações durante horário de trabalho: empresa. Criações pessoais, fora de escopo, em horário livre: empregado"

4. **Confidencialidade perpetuada**
   - Solução: "Sigilo durante emprego + 2 anos após"

### Exemplo de cláusula de PI bem construída

```markdown
#### Propriedade Intelectual

**Criações durante jornada**: Pertencem à empresa. Exemplos: código, documentação, inventos relacionados ao negócio da empresa.

**Criações fora da jornada**: Pertencem ao empregado, desde que:
- Desenvolvidas em horário livre (noites, fins de semana)
- Sem uso de infraestrutura da empresa
- Sem relação com negócio da empresa
- Não prejudiquem concorrentes da empresa

**Notificação**: Empregado comunica empresa de criação fora-jornada em até 30 dias; empresa tem 10 dias para contestar

**Cessão**: Empregado pode ceder diretos de criação dentro-jornada apenas com autorização escrita; remuneração adicional é discutida caso a caso
```

---

## Resumo de ausências críticas por tipo

| Tipo | Ausência crítica | Impacto | Solução |
|------|------------------|--------|---------|
| **Prestação de Serviços** | Sem SLA | Impossível cobrar por atraso | Especificar prazos/marcos mensuráveis |
| **Prestação de Serviços** | PI ambígua | Disputa de propriedade | Descrever "produto final pertence a [parte]" |
| **Compra e Venda** | Sem garantia | Risco todo para comprador | Lei presume 30 dias; contrato pode estender |
| **Compra e Venda** | Frete indefinido | Disputa sobre transportador | Especificar Incoterm ou quem paga |
| **Locação** | Sem reajuste | Deflação de preço real | Lei 8.245/91 presume reajuste anual |
| **Locação** | Caução acumulada | Abusivo | Lei limita a 3x aluguel |
| **NDA** | Prazo indefinido | Obrigação perpétua | Especificar 3-5 anos |
| **SaaS** | Sem portabilidade | Lock-in abusivo | Garantir exportação sem custo |
| **SaaS** | SLA inexistente | Sem proteção | Especificar 99,5% uptime mínimo |
| **Trabalho** | PI genérica | Disputa de direitos | Esclarecer jornada vs. criações livres |
| **Trabalho** | Não-concorrência ilimitada | Nula | Máx 2 anos + raio geográfico + remuneração |

---

## Checklist final de análise por tipo

### Prestação de Serviços
- [ ] Escopo é claro e mensurável?
- [ ] SLA inclui prazos e penalidades?
- [ ] PI está atribuída?
- [ ] Confidencialidade tem prazo determinado?
- [ ] Reajuste segue índice objetivo?

### Compra e Venda
- [ ] Bem é descrito com precisão?
- [ ] Garantia inclui vício oculto e prazo?
- [ ] Incoterm ou responsabilidade de transporte é claro?
- [ ] Prazo de aceite/devolução é definido?

### Locação
- [ ] Reajuste tem índice (IGPM, IPCA)?
- [ ] Caução não excede 3x aluguel?
- [ ] Multa por rescisão é razoável?
- [ ] Benfeitorias são passíveis de compensação?

### NDA
- [ ] "Confidencial" é definido operacionalmente?
- [ ] Exceções legais estão listadas?
- [ ] Prazo é determinado (3-5 anos)?
- [ ] Devolução/destruição é obrigatória?

### SaaS
- [ ] SLA é específico (99,5%+)?
- [ ] Dados são do cliente (não vendor lock-in)?
- [ ] Exportação é sem custo?
- [ ] Responsabilidade não exclui dolo?

### Trabalho
- [ ] Função é descrita?
- [ ] PI distingue jornada vs. criações livres?
- [ ] Não-concorrência tem limite (2 anos, raio, remuneração)?
- [ ] Confidencialidade tem prazo (2 anos máx)?
