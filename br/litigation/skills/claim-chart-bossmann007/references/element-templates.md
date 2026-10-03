# Cause-of-Action Element Templates (Brazilian Civil Law)

Baseline element lists for common Brazilian civil causes of action and defenses. **These are a baseline, not the controlling law.** The elements as codified in the Código Civil (CC), Código de Defesa do Consumidor (CDC), Consolidação das Leis do Trabalho (CLT), Lei da Propriedade Industrial (LPI, Lei 9.279/1996), Lei de Direitos Autorais (LDA, Lei 9.610/1998), Lei de Defesa da Concorrência (Lei 12.529/2011), or the applicable Código de Processo Civil (CPC) provision — as read by the STJ (Superior Tribunal de Justiça, the uniformizing court for federal civil law) and the competent Tribunal — control. Always confirm before mapping.

**Structural note for a common-law-trained reader:** Brazil is a civil-law jurisdiction. Causes of action are not "torts" recognized incrementally by courts stacking precedent on a Restatement; they are elements of a codified *ato ilícito* (unlawful act, CC art. 186) or a specific statutory claim, which courts then interpret. There is no jury pattern instruction (CACI/NYPJI) — the "baseline" here is the statute or code article itself, glossed by consolidated STJ case law (súmulas, temas repetitivos) where it exists. Where a US cause of action has no real Brazilian equivalent (e.g., tortious interference as a standalone tort, promissory estoppel, laches), this file says so rather than forcing a false cognate — mapping a non-existent claim onto Brazilian facts produces a chart with no cause of action to prove.

Every template here says which code/law the baseline came from. The `_elements` sheet in the chart should record which template was used and the jurisdiction-specific (tribunal/súmula) source the user confirmed.

---

## How to use

1. Pick the template that matches the pleaded count (pedido / causa de pedir).
2. Confirm with the user: "Alguma súmula ou entendimento consolidado do tribunal competente adiciona, remove ou reformula algum desses elementos?"
3. If yes, edit the list before mapping.
4. Record on the `_elements` sheet: template used, código/lei consultado, any tribunal-specific (STJ súmula, TJ/TRT entendimento) modifications, and whether the underlying doctrine is codified or purely jurisprudencial (judge-made) — that distinction matters more in a civil-law system than it does in a common-law one, because a purely jurisprudencial doctrine can shift without a legislative act.

A count not in this library — map from the code article, statute, or petição inicial (complaint) allegations directly. This library is not exhaustive; it covers the recurring ones.

---

## Contract (Direito Civil — Obrigações e Contratos)

### Inadimplemento contratual (breach of contract)

**Elements (baseline — CC arts. 389, 395, 396, 475):**
1. Existência de obrigação contratual válida
2. Inadimplemento pelo devedor — absoluto (art. 389, quando a prestação se tornou impossível ou inútil ao credor) ou mora (art. 395, atraso culposo no cumprimento)
3. Nexo de causalidade entre o inadimplemento e o dano
4. Dano (perdas e danos — danos emergentes e lucros cessantes, art. 402)
5. *Se o pedido for resolução do contrato* (art. 475): o credor pode exigir o cumprimento forçado ou pedir a resolução, cumulável com indenização por perdas e danos em qualquer dos dois casos

*Caveat: o CC não separa formação do contrato (oferta, aceitação) da fase de execução como elementos autônomos da pretensão de inadimplemento — a validade do contrato é normalmente pressuposto, discutida em ação própria (anulação/nulidade) se controvertida. Cláusula penal (arts. 408-416) pode fixar a indenização previamente, dispensando prova do dano quando compensatória. Mora do credor (art. 400) e exceção de contrato não cumprido (art. 476) são defesas típicas, não elementos do pedido.*

### Boa-fé objetiva na execução do contrato (implied covenant of good faith and fair dealing)

**Não é uma causa de pedir autônoma no Direito brasileiro.** A boa-fé objetiva (CC art. 422 — "os contratantes são obrigados a guardar, assim na conclusão do contrato, como em sua execução, os princípios de probidade e boa-fé") é uma **cláusula geral interpretativa e integrativa**, não um tipo de ação distinto de inadimplemento contratual. Ela opera por meio de doutrinas derivadas que podem fundamentar um pedido quando combinadas com dano:

1. **Função integrativa** — impõe deveres anexos (informação, cooperação, cuidado, sigilo) não escritos no contrato; violação de dever anexo é inadimplemento (mesma estrutura de elementos acima).
2. **Função de controle** — veda o **abuso de direito** (CC art. 187 — "também comete ato ilícito o titular de um direito que, ao exercê-lo, excede manifestamente os limites impostos pelo seu fim econômico ou social, pela boa-fé ou pelos bons costumes"), que é ato ilícito equiparado ao art. 186 e gera responsabilidade civil (art. 927).
3. **Doutrinas derivadas mais invocadas em juízo:** *venire contra factum proprium* (vedação ao comportamento contraditório), *supressio* (perda de direito não exercido por longo período gerando expectativa legítima), *surrectio* (surgimento de direito pela prática reiterada), *tu quoque* (vedação a quem descumpriu invocar a mesma cláusula contra a outra parte).

Se o usuário pede um "chart" para violação de boa-fé objetiva isolada, mapear como **abuso de direito (art. 187) + ato ilícito (art. 186) + dano (art. 927)**, citando a doutrina derivada específica invocada, e não como pedido autônomo.

### Culpa in contrahendo / responsabilidade pré-contratual (closest analog to promissory estoppel)

**O Direito brasileiro não tem "promissory estoppel" como instituto autônomo.** O equivalente funcional mais próximo é a **responsabilidade pré-contratual por violação da boa-fé objetiva nas tratativas** (CC art. 422 aplicado à fase pré-contratual, construção doutrinária e jurisprudencial — não há artigo específico do CC para a fase de tratativas, mas o STJ reconhece o dever de boa-fé desde as negociações preliminares).

**Elements (baseline — jurisprudência do STJ construída sobre CC art. 422 e art. 187):**
1. Existência de negociações preliminares sérias, gerando expectativa legítima de conclusão do contrato
2. Ruptura injustificada e contrária à boa-fé das tratativas por uma das partes
3. Confiança depositada pela outra parte, razoável e objetivamente demonstrável (não mera expectativa subjetiva)
4. Dano decorrente da ruptura — tipicamente **interesse negativo** (o que a parte gastou ou deixou de fazer confiando na conclusão do negócio), não o interesse positivo de cumprimento do contrato que nunca se formou

*Caveat: esta é uma construção jurisprudencial, não uma pretensão codificada com elementos fixos — a jurisprudência do STJ é mais fluida do que uma pattern instruction americana. Confirmar precedentes recentes do STJ (não há súmula consolidada específica) antes de estruturar o chart; sinalizar `[jurisprudência — verificar precedentes atuais]`.*

### Enriquecimento sem causa (unjust enrichment)

**Elements (baseline — CC arts. 884-886):**
1. Enriquecimento (vantagem patrimonial) de uma parte
2. Empobrecimento correspondente da outra parte
3. Nexo de causalidade entre o enriquecimento e o empobrecimento
4. Ausência de causa jurídica que justifique o deslocamento patrimonial
5. **Subsidiariedade** (art. 886) — a ação de enriquecimento sem causa só é cabível se o prejudicado não dispuser de outra ação específica prevista em lei para se ressarcir (ex.: se cabe ação de cobrança contratual, não cabe enriquecimento sem causa)

*Caveat: a subsidiariedade do art. 886 é frequentemente o ponto que derruba a pretensão — verificar sempre se existe ação típica disponível antes de basear o chart nesta causa de pedir.*

---

## Responsabilidade civil extracontratual — culpa (tort — negligence and related)

### Responsabilidade civil por ato ilícito culposo (negligence)

**Elements (baseline — CC arts. 186, 927, caput):**
1. Conduta (ação ou omissão) do agente
2. Culpa (negligência, imprudência ou imperícia) ou dolo
3. Nexo de causalidade entre a conduta e o dano
4. Dano (patrimonial e/ou moral)

*Caveat: o CC unifica sob "responsabilidade civil" o que o common law separa em negligence/intentional torts distintos — a diferença central no Brasil é entre **responsabilidade subjetiva** (exige prova de culpa, art. 186) e **responsabilidade objetiva** (dispensa culpa, exige apenas risco da atividade — art. 927, parágrafo único: "quando a atividade normalmente desenvolvida pelo autor do dano implicar, por sua natureza, risco para os direitos de outrem"). Confirmar qual regime se aplica antes de montar o chart — a diferença muda o elemento 2 inteiro. Se a relação for de consumo, aplica-se o CDC (art. 14, responsabilidade objetiva do fornecedor por defeito no serviço), não o CC.*

### Culpa contra a legalidade (negligence per se)

**Não é doutrina autônoma codificada, mas construção aceita pela jurisprudência** dentro do art. 186: a violação de norma regulamentar ou legal específica (portaria, resolução, regulamento de trânsito, norma técnica) é tratada como evidência forte (por vezes presunção) de culpa, dispensando prova detalhada do padrão de cuidado abstrato.

**Elements (baseline):**
1. Violação de norma legal, regulamentar ou técnica específica pelo réu
2. A violação causou o dano (nexo de causalidade)
3. O autor está dentro do círculo de pessoas que a norma visava proteger
4. O dano é do tipo que a norma buscava prevenir

*Caveat: isto não dispensa a demonstração do nexo causal e do dano (elementos do art. 186) — apenas facilita a prova da culpa. Não presumir automaticamente responsabilidade objetiva a partir da violação normativa.*

### Culpa grave (gross negligence)

**O CC não gradua formalmente a culpa para fins de responsabilidade civil geral** como o common law faz (negligence vs. gross negligence vs. recklessness) — a antiga tripartição romana (culpa levíssima, leve, grave) não tem efeito autônomo na responsabilidade extracontratual comum. Onde a gradação da culpa importa no Direito brasileiro:

1. **Cláusulas de limitação/exclusão de responsabilidade** — a jurisprudência (e o art. 424 do CC em contratos de adesão) tende a considerar nula a cláusula que exclui responsabilidade por dolo ou culpa grave, equiparando-a ao dolo para esse efeito específico.
2. **Dano moral — critério de gravidade da conduta** — usado para calibrar o *quantum* indenizatório (não para caracterizar um elemento distinto da pretensão).
3. **Não há "danos punitivos" no Direito brasileiro** — a indenização é compensatória (arts. 944-945), não punitiva; a chamada "função pedagógica/dissuasória" do dano moral é um fator de cálculo do valor compensatório, não uma categoria de dano distinta, e o STJ resiste a importar punitive damages diretamente.

*Não usar "gross negligence" como causa de pedir autônoma no chart — mapear como responsabilidade civil comum (art. 186/927) com nota sobre gravidade da conduta relevante para o quantum, e checar se há cláusula de limitação de responsabilidade em jogo.*

---

## Responsabilidade civil por conduta dolosa (tort — intentional)

### Fraude / dolo (fraud / intentional misrepresentation)

Duas trilhas distintas no Direito brasileiro — não confundir:

**(a) Dolo como vício do consentimento** (para anular o negócio jurídico — CC arts. 145-150):
1. Declaração ou conduta dolosa (artifício ou artimanha, art. 146: "dolo acidental")
2. Dolo substancial — sem ele o negócio não se realizaria (art. 145)
3. Induzimento a erro da outra parte
4. *Consequência:* anulabilidade do negócio jurídico (art. 171, II), com prazo decadencial de 4 anos (art. 178, II)

**(b) Ato ilícito doloso gerando dever de indenizar** (dano decorrente de fraude — CC arts. 186, 927):
1. Declaração falsa de fato relevante (ou omissão dolosa — art. 147)
2. Conhecimento da falsidade pelo agente (dolo)
3. Indução da vítima à confiança/erro
4. Nexo de causalidade entre a fraude e o dano
5. Dano (patrimonial e/ou moral) decorrente da confiança depositada

*Caveat: a fraude pode configurar também o crime de estelionato (Código Penal art. 171), que corre em esfera própria (ação penal) e não substitui a ação civil de indenização — as esferas são independentes (CC art. 935), embora a sentença penal condenatória faça coisa julgada quanto ao dever de indenizar. O CPC não tem um padrão de "pleading with particularity" equivalente à FRCP 9(b), mas a petição inicial deve narrar os fatos com precisão suficiente para viabilizar o contraditório (CPC art. 319, III).*

### Informação inexata prestada sem o devido cuidado (negligent misrepresentation)

**Elements (baseline — CC art. 186, ou CDC art. 14 se relação de consumo):**
1. Informação falsa ou inexata prestada pelo réu
2. Ausência de cuidado razoável na verificação da veracidade (culpa, não dolo)
3. Confiança justificada da vítima na informação
4. Nexo de causalidade e dano decorrente

*Caveat: se a informação foi prestada no contexto de uma relação de consumo (CDC arts. 2º-3º), a responsabilidade é objetiva por defeito na prestação de informação (CDC art. 14) — não exige prova de culpa. Fora de relação de consumo, aplica-se a responsabilidade subjetiva comum do CC.*

### Omissão dolosa (fraudulent concealment)

**Elements (baseline — CC art. 147: "nos negócios jurídicos bilaterais, o silêncio intencional de uma das partes a respeito de fato ou qualidade que a outra parte haja ignorado, constitui omissão dolosa, provando-se que sem ela o negócio não se teria celebrado"):**
1. Silêncio intencional sobre fato ou qualidade relevante
2. A outra parte ignorava o fato
3. Sem a omissão, o negócio não teria sido celebrado (nexo entre a omissão e a formação do negócio)
4. Dano decorrente

*Caveat: distinta do dolo positivo (declaração ativa falsa, art. 145-146) — aqui o vício está no silêncio. Se não houver dever legal ou contratual de informar, a omissão pode não ser dolosa; verificar se existe dever de informação (frequente em relações de consumo, CDC art. 6º, III).*

### Interferência em relação contratual alheia (tortious interference with contract)

**Não existe, no Direito brasileiro, um tipo autônomo e codificado equivalente a "tortious interference with contract" do common law.** O caminho funcional mais próximo combina duas cláusulas gerais:

**Elements (baseline — construção a partir de CC arts. 186 e 187):**
1. Existência de contrato válido entre o autor e um terceiro
2. Conhecimento do réu sobre esse contrato
3. Conduta do réu que constitui **abuso de direito** (art. 187 — exercício de um direito próprio que excede manifestamente os limites da boa-fé, dos bons costumes, ou da finalidade econômica/social) OU **ato ilícito comum** (art. 186) direcionado a induzir o rompimento
4. Ruptura ou perturbação efetiva do contrato
5. Dano decorrente

*Caveat: esta é uma reconstrução, não uma pretensão nomeada no Código — menos codificada como causa de pedir autônoma no Brasil do que nos EUA. Em contexto empresarial/concorrencial, verificar se os fatos configuram **concorrência desleal** (Lei 9.279/1996 art. 195, que tipifica condutas específicas, algumas como crime) — se sim, prefira essa tipificação mais específica à reconstrução genérica de abuso de direito.*

### Interferência em expectativa de vantagem econômica futura (tortious interference with prospective economic advantage)

**Também sem tipo autônomo codificado.** Mapear pela mesma lógica do item acima (abuso de direito + ato ilícito), com atenção adicional à **concorrência desleal** quando o contexto é empresarial:

**Elements (baseline):**
1. Existência de relação econômica com probabilidade real de benefício futuro
2. Conhecimento do réu sobre essa relação
3. Conduta abusiva ou ilícita do réu direcionada a perturbar a relação — se configurar hipótese do art. 195 da LPI (concorrência desleal: uso de meio fraudulento para desviar clientela, divulgação de informação falsa em detrimento de concorrente, etc.), tipificar especificamente
4. Perturbação efetiva
5. Dano

*Caveat: quanto mais o caso se aproxima de concorrência entre empresas, mais provável que a LPI art. 195 (que lista condutas específicas de concorrência desleal, com sanção penal e civil) seja a via correta em vez da reconstrução genérica via CC.*

### Dano à honra e à imagem (defamation — libel/slander)

**O Direito brasileiro não distingue libel (escrito) de slander (oral) como categorias jurídicas diferentes** — ambos se enquadram na mesma responsabilidade civil por violação a direito da personalidade, independentemente do meio.

**Elements (baseline — CC arts. 11-21 (direitos da personalidade), 186, 927; CF/88 art. 5º, V e X):**
1. Afirmação ou divulgação de fato ofensivo à honra, imagem ou reputação (ou opinião com intenção de ofender — a distinção fato/opinião importa para a ponderação com liberdade de expressão, mas não é elemento estanque como no common law)
2. Divulgação a terceiro (publicidade)
3. Nexo de causalidade
4. Dano moral — em muitos casos **presumido** (dano moral *in re ipsa*) quando a ofensa à honra é objetivamente grave, dispensando prova específica do abalo psíquico

*Caveat: não há distinção per se/per quod do common law. A ponderação central no Brasil é **liberdade de expressão/imprensa (CF art. 5º, IV e IX) vs. direitos da personalidade (CF art. 5º, X)** — jurisprudência do STF e STJ sobre limites da crítica jornalística, humor e opinião é o campo de disputa real, não um teste de "actual malice" à la *New York Times v. Sullivan* (que não foi recepcionado no Direito brasileiro; a responsabilidade da imprensa segue responsabilidade civil comum, sem o standard americano de malícia real para figuras públicas, embora a jurisprudência dê mais latitude à crítica de agentes públicos).*

### Apropriação indevida de bem móvel (closest analog to conversion)

**Sem tipo civil autônomo chamado "conversion".** O caminho no Direito brasileiro passa por:

**Elements (baseline — combinação de CC art. 1.228 (propriedade), ações possessórias CPC arts. 560-566, e responsabilidade civil arts. 186/927):**
1. Direito de propriedade ou posse do autor sobre o bem móvel
2. Ato do réu que exerce domínio sobre o bem incompatível com o direito do autor (esbulho, apropriação, recusa de devolução)
3. Dano — perda do bem, seu valor, ou privação do uso

*Caveat: a via processual difere conforme o pedido — **ação de reintegração de posse** (CPC art. 560, se houver esbulho possessório) busca a restituição do bem; **ação de indenização** (CC 186/927) busca o equivalente em dinheiro se o bem não puder ser restituído. Se a apropriação for por funcionário/terceiro com abuso de confiança, pode configurar também apropriação indébita (crime, Código Penal art. 168), esfera penal independente da civil.*

### Turbação/interferência no uso de bem móvel (closest analog to trespass to chattels)

**Também sem tipo autônomo.** Mapear como turbação de posse (CC art. 1.210, ações possessórias) quando há mera interferência sem privação total, ou dano a bem móvel (CC arts. 186/927) quando há dano ao bem em si.

**Elements (baseline):**
1. Posse ou direito de uso do autor sobre o bem móvel
2. Interferência intencional do réu no uso ou posse do bem
3. Dano efetivo (privação do uso, dano ao estado do bem)

### Dano moral por conduta grave e ofensiva (closest analog to intentional infliction of emotional distress)

**Sem tipo autônomo equivalente a IIED.** Mapeia-se dentro da responsabilidade civil comum por dano moral (CC arts. 186, 927, 11-21), com o critério de **gravidade da conduta** funcionando como fator de ponderação do dano, não como elemento autônomo estruturado como no Restatement § 46.

**Elements (baseline):**
1. Conduta do réu objetivamente grave e reprovável
2. Dolo ou culpa (ou, em relação de consumo/trabalho, responsabilidade objetiva conforme o regime aplicável)
3. Dano moral efetivo — sofrimento, humilhação, abalo psíquico com repercussão que ultrapassa o mero aborrecimento cotidiano (limiar reiteradamente exigido pela jurisprudência do STJ para não banalizar o dano moral)
4. Nexo de causalidade

*Caveat: o STJ é enfático em distinguir dano moral indenizável de "mero dissabor" — mapear a gravidade da conduta e do resultado com cuidado; muitos pedidos de dano moral são rejeitados por não superarem esse limiar.*

---

## Fiduciário / societário (fiduciary / corporate)

### Violação de dever fiduciário (breach of fiduciary duty)

O equivalente brasileiro depende do vínculo:

**(a) Administradores de sociedade anônima** (Lei 6.404/1976 — LSA):
1. Existência do dever — **dever de diligência** (art. 153: "o administrador da companhia deve empregar, no exercício de suas funções, o cuidado e diligência que todo homem ativo e probo costuma empregar na administração dos seus próprios negócios"), **dever de lealdade** (art. 155, incluindo vedação ao uso de informação privilegiada e de oportunidades da companhia), **dever de informar** (art. 157)
2. Violação do dever
3. Nexo de causalidade
4. Dano à companhia ou aos acionistas (art. 159 — ação social de responsabilidade)

*Caveat: a **business judgment rule** não é codificada no Brasil como presunção formal (diferente de Delaware), mas a jurisprudência e a CVM tendem a dar deferência a decisões negociais tomadas de boa-fé, informadas e sem conflito de interesse — é um fator de análise, não uma presunção estruturada com o mesmo peso doutrinário do Direito societário de Delaware. **Legitimidade para a ação** (individual do acionista vs. ação social, art. 159 e parágrafos) é pressuposto processual relevante, análogo — mas não idêntico — às regras de demand futility/derivative standing americanas.*

**(b) Mandato/administração de bens de terceiros (CC):**
1. Existência de relação de mandato (arts. 653 e ss.) ou administração fiduciária
2. Violação de dever de boa administração, incluindo o **dever de prestar contas** (art. 668)
3. Nexo de causalidade e dano

### Participação de terceiro na violação do dever fiduciário (aiding and abetting breach of fiduciary duty)

**Elements (baseline — CC art. 942: "os bens do responsável pela ofensa ou violação de direito de outrem ficam sujeitos à reparação do dano causado; e, se a ofensa tiver mais de um autor, todos responderão solidariamente pela reparação"):**
1. Existência de dever fiduciário e sua violação pelo fiduciário
2. Participação consciente do terceiro na violação (conluio, ciência da ilicitude e colaboração ativa)
3. Dano decorrente

*Caveat: a solidariedade do art. 942 é o mecanismo central — não há um tipo autônomo de "aiding and abetting" civil separado; o terceiro coautor responde solidariamente pelo mesmo ato ilícito.*

---

## Mercado de capitais (securities)

### Fraude no mercado de valores mobiliários / uso indevido de informação privilegiada

**Elements (baseline — Lei 6.385/1976 art. 27-D (insider trading, crime); Instruções Normativas da CVM sobre manipulação de mercado e informações; LSA art. 245 (responsabilidade do administrador por atos com terceiros)):**
1. Divulgação de informação falsa, incompleta ou enganosa relevante ao mercado (ou uso indevido de informação privilegiada não divulgada)
2. Conexão com negociação de valor mobiliário
3. Dolo ou, no mínimo, negligência grave do agente (para a esfera civil; a esfera penal do art. 27-D exige dolo)
4. Nexo de causalidade entre a informação/conduta e o dano ao investidor
5. Dano — perda patrimonial do investidor

*Caveat: há trilha administrativa (CVM, com poder de multa e inabilitação), trilha penal (Lei 6.385/1976 arts. 27-C a 27-D) e trilha civil (ação de indenização por danos), correndo em paralelo e com padrões de prova distintos. O CDC pode se aplicar a fundos e produtos ofertados a investidores pessoa física, dependendo da caracterização como consumidor.*

### Responsabilidade por prospecto de oferta pública (closest analog to §11 Securities Act)

**Elements (baseline — Instrução CVM 400 (oferta pública de distribuição de valores mobiliários), arts. 56 e 200 da LSA):**
1. Oferta pública com prospecto contendo informação falsa, incompleta ou enganosa
2. Nexo entre a falha do prospecto e a decisão de investimento
3. Dano ao investidor
4. Responsabilidade solidária de emissor, ofertante e instituições coordenadoras/underwriters pela veracidade das informações do prospecto (regime que se aproxima de responsabilidade objetiva/estrita para o emissor)

*Caveat: verificar se a oferta é registrada na CVM (oferta pública) ou dispensada de registro (oferta com esforços restritos, Instrução CVM 476) — o regime de responsabilidade e o rol de responsáveis solidários varia conforme o tipo de oferta.*

---

## Concorrência (antitrust)

### Infração à ordem econômica (cartel/acordo restritivo — closest analog to Sherman Act § 1)

**Elements (baseline — Lei 12.529/2011 (Lei de Defesa da Concorrência) art. 36, caput e §3º):**
1. Ato praticado, independentemente de culpa (art. 36, caput — responsabilidade objetiva na esfera administrativa perante o CADE), que tenha por objeto ou possa produzir os efeitos de: limitar, falsear ou prejudicar a livre concorrência ou a livre iniciativa; dominar mercado relevante; aumentar arbitrariamente os lucros; ou exercer de forma abusiva posição dominante
2. Conduta tipificada no rol exemplificativo do §3º (ex.: acordo entre concorrentes para fixar preços, dividir mercados, limitar produção)
3. Potencialidade de efeito anticoncorrencial no mercado relevante (não exige efeito consumado)
4. *Para ação civil de indenização* (art. 47): dano ao terceiro prejudicado, nexo causal com a infração

*Caveat: a apuração da infração corre primariamente na esfera administrativa perante o **CADE** (Conselho Administrativo de Defesa Econômica); a ação civil de indenização do art. 47 pode ser proposta independentemente ou após decisão do CADE (que, se condenatória, facilita a prova da ilicitude na ação civil). Não há distinção per se illegal / rule of reason formalmente estruturada como no Direito antitruste americano, embora a análise de efeitos e a Guia de análise de atos de concentração do CADE cumpram função análoga.*

### Abuso de posição dominante (closest analog to Sherman Act § 2 monopolization)

**Elements (baseline — Lei 12.529/2011 art. 36, §§2º-3º):**
1. Posição dominante no mercado relevante (presumida quando a empresa detém 20% ou mais do mercado, art. 36 §2º — presunção relativa)
2. Exercício abusivo dessa posição, com objeto ou efeito de prejudicar a concorrência (não a mera existência de posição dominante, que não é ilícita per se)
3. Potencialidade ou efeito anticoncorrencial
4. *Para ação civil*: dano e nexo causal

*Caveat: dominância de mercado não é ilícita em si — o abuso é que se pune, distinção equivalente à americana entre "growth as a consequence of a superior product" e "willful acquisition or maintenance" da posição. A definição de mercado relevante (produto + geográfico) é o ponto técnico mais disputado, igual ao Direito americano.*

---

## Trabalhista (employment — CLT, não Título VII/ADEA/FLSA)

**Nota estrutural:** o Brasil não tem um "Título VII" único — a proteção contra discriminação no trabalho vem da CF/88 art. 7º, XXX (proibição de diferença de salários, funções e critério de admissão por sexo, idade, cor ou estado civil) combinada com a **Lei 9.029/1995** (proíbe práticas discriminatórias para efeito de acesso ou manutenção da relação de trabalho) e o **art. 373-A da CLT**. Não existe o burden-shifting *McDonnell Douglas* como estrutura processual formal — o ônus da prova segue as regras gerais do CPC/CLT (art. 818 CLT c/c art. 373 CPC), com inversão possível em casos de discriminação presumida (ex.: Súmula 443 do TST).

### Dispensa discriminatória (closest analog to Title VII disparate treatment)

**Elements (baseline — Lei 9.029/1995 arts. 1º e 4º; CF art. 7º, XXX; Súmula 443 do TST):**
1. Pertencimento do empregado a grupo ou característica protegida (sexo, raça, idade, orientação sexual, deficiência, portador de doença grave que suscite estigma ou preconceito, estado de gravidez, etc.)
2. Ato de dispensa (ou não contratação/promoção) pelo empregador
3. Nexo entre a característica protegida e o ato — a **Súmula 443 do TST** cria presunção de dispensa discriminatória para empregado portador de doença grave que suscite estigma ou preconceito (ex.: HIV, câncer), invertendo o ônus para o empregador provar motivo diverso
4. Consequência: nulidade da dispensa com direito a reintegração ou indenização em dobro do período de afastamento (Lei 9.029/1995 art. 4º)

*Caveat: fora das hipóteses de presunção (Súmula 443 e correlatas), o ônus de provar a motivação discriminatória é, em regra, do empregado — não há burden-shifting formal em três etapas como no McDonnell Douglas.*

### Assédio moral / ambiente de trabalho hostil (closest analog to hostile work environment)

**Sem tipificação legal específica — construção jurisprudencial do TST** sobre a responsabilidade civil comum (CC arts. 186, 927) aplicada ao ambiente de trabalho, combinada com a rescisão indireta (CLT art. 483).

**Elements (baseline):**
1. Conduta reiterada e sistemática do empregador, superior hierárquico ou colegas (com tolerância do empregador) que expõe o trabalhador a situações humilhantes e constrangedoras
2. Repetição e sistematicidade (episódio isolado, em regra, não configura assédio moral, distinto de dano moral pontual)
3. Nexo com o ambiente de trabalho
4. Dano psíquico/moral ao trabalhador
5. *Se o empregado pedir rescisão indireta* (CLT art. 483, "e" — exigência de serviços superiores às forças do empregado ou que constituam ato lesivo à honra e boa fama): equivale ao empregado se demitir "com justa causa do empregador", mantendo os mesmos direitos de dispensa sem justa causa

*Caveat: cada TRT regional tem parâmetros próprios de gravidade e quantum até uniformização pelo TST — sinalizar variação regional (ver SKILL.md, tabela de divergências regionais).*

### Retaliação por denúncia ou reclamação (closest analog to Title VII retaliation)

**Elements (baseline — construção a partir da vedação geral a atos discriminatórios (Lei 9.029/1995) e da proteção a denunciantes em normas setoriais específicas, quando aplicáveis):**
1. Atividade protegida do empregado (reclamação de direitos, denúncia de irregularidade, participação em processo administrativo ou judicial)
2. Ato adverso do empregador (dispensa, rebaixamento, perseguição) após a atividade protegida
3. Nexo causal entre a atividade protegida e o ato adverso

*Caveat: menos codificado que a proteção americana pós-Burlington Northern — no Brasil, a proteção contra retaliação trabalhista é mais fragmentada, dependendo de normas setoriais (ex.: proteção a dirigente sindical, CF art. 8º, VIII; estabilidade da CIPA, CLT art. 165) ou da reconstrução via dano moral/dispensa discriminatória geral quando não há norma específica aplicável.*

### Discriminação por idade (closest analog to ADEA)

**Sem estatuto específico equivalente ao ADEA.** Mapear pela mesma via de dispensa discriminatória (CF art. 7º, XXX; Lei 9.029/1995), com o critério protegido sendo idade.

**Elements (baseline):**
1. Idade do empregado (sem piso etário formal equivalente aos "40 anos ou mais" do ADEA — a proteção constitucional não fixa faixa etária mínima)
2. Ato adverso do empregador
3. Nexo entre a idade e o ato adverso

### Horas extras (FLSA overtime claim → CLT overtime)

**Elements (baseline — CLT arts. 3º, 58, 59; CF art. 7º, XVI):**
1. **Vínculo empregatício caracterizado** (CLT art. 3º) — presença cumulativa de subordinação, não-eventualidade, onerosidade e pessoalidade na prestação de serviço
2. Horas trabalhadas além da 8ª diária ou da 44ª semanal (CLT art. 58, caput)
3. Ausência de pagamento do adicional de horas extras — mínimo de 50% sobre o valor da hora normal (CF art. 7º, XVI), ou 100% quando trabalhadas em domingos e feriados sem compensação
4. **Prazo prescricional** (CF art. 7º, XXIX): 5 anos contados da prestação do serviço, limitado a 2 anos após a extinção do contrato de trabalho — créditos anteriores a esse período estão prescritos

*Nota: não há aqui equivalente ao "Tameny formulation" californiano — esse é um conceito de wrongful termination do Direito americano, sem correspondência com horas extras; a estrutura acima é a pretensão trabalhista de horas extras isolada, tal como codificada na CLT, sem necessidade de importar conceito estranho.*

### Dispensa arbitrária ou discriminatória (closest analog to wrongful termination in violation of public policy)

**O Brasil não reconhece "wrongful termination in violation of public policy" como tort autônomo** — o regime geral é de dispensa sem justa causa livre (com pagamento de verbas rescisórias e multa de 40% do FGTS, Lei 8.036/1990 art. 18, §1º), salvo hipóteses específicas de **estabilidade** (gestante, CIPA, dirigente sindical, acidentado) ou **dispensa discriminatória** (ver acima, Lei 9.029/1995).

**Elements (baseline, quando aplicável):**
1. Relação de emprego
2. Dispensa (ou dispensa disfarçada/constructive discharge via rescisão indireta, CLT art. 483)
3. A dispensa viola estabilidade legal específica OU configura discriminação (Lei 9.029/1995) OU é arbitrária no contexto de dispensa coletiva sem motivação (jurisprudência exige, em alguns casos, negociação coletiva prévia para dispensa em massa — Tema de repercussão geral do STF sobre dispensa coletiva)
4. Consequência: reintegração (se estabilidade) ou indenização substitutiva; dobra do FGTS (se discriminatória, Lei 9.029/1995 art. 4º)

*Caveat: não force o conceito de "public policy tort" americano sobre fatos brasileiros — identifique primeiro se há estabilidade legal específica, depois se há discriminação, e só então trate como dispensa arbitrária genérica (regime residual e mais fraco de proteção).*

---

## Propriedade intelectual (trade secret / IP civil)

### Violação de segredo industrial / concorrência desleal (trade secret misappropriation — DTSA/UTSA)

**Elements (baseline — Lei 9.279/1996 (LPI) art. 195, incisos XI e XII (concorrência desleal — segredo de negócio/indústria); CC arts. 186/927 para a ação de indenização):**
1. A informação constitui segredo de negócio ou industrial — não é de conhecimento público e tem valor econômico exatamente por não ser conhecida
2. O titular adotou medidas razoáveis para manter o sigilo
3. Obtenção, uso ou divulgação indevida por meio desleal (ex-empregado, ex-sócio, espionagem industrial, quebra de acordo de confidencialidade) — LPI art. 195, XI ("divulga, explora ou utiliza-se, sem autorização, de conhecimentos, informações ou dados confidenciais, utilizáveis na indústria, comércio ou prestação de serviços, obtidos por meios ilícitos ou a que teve acesso mediante fraude") e XII (mesma conduta por ex-empregado)

*Caveat: a LPI tipifica a conduta como **crime** (art. 195, com pena de detenção) além de gerar responsabilidade civil (art. 209 — perdas e danos por atos de violação de direitos de propriedade industrial e atos de concorrência desleal). Não há uma lei-modelo única como a UTSA americana; o regime brasileiro é integrado na própria LPI. Confirmar se há acordo de confidencialidade (NDA) contratual, que reforça a pretensão pela via contratual (inadimplemento) cumulada com a via da LPI.*

### Violação de direito autoral (copyright infringement)

**Elements (baseline — Lei 9.610/1998 (LDA) arts. 7º, 22, 29, 102-110):**
1. Titularidade de direito autoral válido — a obra deve ser originalidade (art. 7º: criação do espírito, expressa por qualquer meio ou fixada em qualquer suporte) — **não há exigência de registro para a proteção nascer** (a proteção autoral no Brasil surge com a criação da obra; o registro no órgão competente — ex.: Biblioteca Nacional para obras literárias — é meramente declaratório/facultativo, ao contrário do modelo americano pós-*Fourth Estate* que exige registro antes de ajuizar ação)
2. Utilização não autorizada de elementos protegidos da obra — reprodução, distribuição, comunicação ao público, ou outra modalidade do rol do art. 29 (que exige autorização prévia e expressa do autor para qualquer forma de utilização)
3. Ausência de exceção legal aplicável (limitações do art. 46 — uso para fins didáticos limitados, citação com indicação de fonte, paródia, etc.)

*Caveat: diferente do Direito americano, **o registro não é pré-requisito processual** para propor a ação — isso muda a análise de "standing" completamente. A análise de similaridade substancial não segue um teste único uniforme como nos circuitos americanos, mas critérios doutrinários e jurisprudenciais de originalidade e contrafação.*

### Violação de marca (trademark infringement — Lanham Act § 32/§ 43(a))

**Elements (baseline — Lei 9.279/1996 (LPI) arts. 129, 189, 190, 209):**
1. Titularidade de registro válido perante o **INPI** — no Brasil, ao contrário do sistema americano, a proteção da marca depende do **registro constitutivo** no INPI (art. 129: "a propriedade da marca adquire-se pelo registro validamente expedido"); não há proteção equivalente robusta ao "common law trademark" americano por mero uso não registrado, salvo a **marca de alto renome** (art. 125) e a proteção limitada ao "usuário de boa-fé" preexistente ao pedido de registro de terceiro (art. 129, §1º)
2. Uso pelo réu, no comércio, de marca idêntica ou semelhante para produtos/serviços idênticos, semelhantes ou afins
3. Possibilidade de confusão, associação indevida ou aproveitamento parasitário da reputação alheia entre os consumidores relevantes — a jurisprudência do STJ usa critérios multifatoriais análogos (grau de distintividade da marca, semelhança gráfica/fonética/ideológica, afinidade mercadológica) mas sem um teste único nomeado por circuito como Sleekcraft/Polaroid/du Pont

*Caveat: **o registro no INPI é constitutivo do direito**, não meramente declaratório como no copyright — isso é a inversão mais importante frente ao Direito americano, onde o uso no comércio já gera direitos de common law antes do registro federal. Para infração de **patente**, direcionar ao modo patente deste skill (não ao modo civil). Ações de nulidade de registro (art. 175) exigem o INPI como litisconsorte necessário — ver nota de jurisdição/foro no SKILL.md.*

---

## Propriedade (property)

### Esbulho / turbação de posse (trespass to land)

**Elements (baseline — CC art. 1.210 (proteção possessória); CPC arts. 554-568 (ações possessórias)):**
1. Posse do autor sobre o imóvel
2. Ato de esbulho (privação total da posse) ou turbação (perturbação sem privação total) pelo réu, sem consentimento ou justificativa jurídica
3. *Elemento processual adicional*: a ação possessória exige demonstração da posse, da data do esbulho/turbação e da perda/perturbação da posse (CPC art. 561) — regime de tutela mais célere (interdito possessório) do que a ação reivindicatória fundada em propriedade (CC art. 1.228)

*Caveat: distinguir a ação possessória (protege a posse em si, mais rápida) da ação reivindicatória (protege a propriedade, exige prova do domínio — CC art. 1.228) — são pedidos e provas distintos, apesar de os fatos poderem se sobrepor.*

### Direito de vizinhança (private nuisance)

**Elements (baseline — CC art. 1.277: "o proprietário ou o possuidor de um prédio tem o direito de fazer cessar as interferências prejudiciais à segurança, ao sossego e à saúde dos que o habitam, provocadas pela utilização de propriedade vizinha"):**
1. Interesse do autor no uso e gozo do imóvel (proprietário ou possuidor)
2. Interferência substancial e prejudicial (à segurança, sossego ou saúde) proveniente do imóvel vizinho
3. A interferência decorre de uso anormal da propriedade vizinha (o parágrafo único do art. 1.277 remete à "natureza da utilização, localização do prédio, atendidas as normas que distribuem as edificações em zonas, e os limites ordinários de tolerância dos moradores da vizinhança")
4. Dano ou risco de dano

*Caveat: o CC brasileiro codifica o "direito de vizinhança" como capítulo próprio (arts. 1.277-1.281, incluindo regras específicas de árvores limítrofes, passagem de cabos e tubulações, e direito de construir) — mais estruturado como regime de vizinhança do que a doutrina de nuisance do common law, com critério de tolerância normal (uso "anormal" da propriedade) como pedra angular.*

---

## Prescrição e defesas (affirmative defenses)

Defesas têm seus próprios elementos, que a parte que as alega geralmente deve provar. Mapear do mesmo modo que causas de pedir — elementos, evidência, gap list. **Nota importante:** o Direito brasileiro não tem a divisão law/equity do common law — não existem "equitable defenses" como categoria formal; as defesas abaixo marcadas como "sem correspondência direta" são construções doutrinárias/jurisprudenciais dentro do sistema unificado de civil law, geralmente ancoradas na boa-fé objetiva (CC art. 422).

### Prescrição (statute of limitations)

**Elements (baseline — CC arts. 189, 205, 206; distinção crucial com decadência, arts. 207-211):**
1. Prazo prescricional aplicável à pretensão — regra geral de **10 anos** (art. 205) quando a lei não fixar prazo menor; prazos específicos do art. 206 (ex.: 3 anos para pretensão de reparação civil, art. 206 §3º, V; 1 ano para pretensão do segurado contra o segurador, art. 206 §1º)
2. A pretensão nasceu (violação do direito, art. 189: "violado o direito, nasce para o titular a pretensão, a qual se extingue, pela prescrição") em data específica — com análise de eventual **teoria da actio nata** (o prazo só corre a partir do conhecimento da lesão, em certas hipóteses) e causas de suspensão/interrupção (arts. 197-204)
3. A ação foi ajuizada após o decurso do prazo

*Caveat: prescrição (perda da pretensão, exceção que pode ser alegada mas também reconhecida de ofício em certos casos, art. 332 §1º CPC) é distinta de **decadência** (perda do próprio direito potestativo, prazos do art. 178 e outros específicos, em regra não se suspende nem se interrompe, art. 207) — confirmar qual regime se aplica, pois o tratamento processual é diferente.*

### "Laches" — sem correspondência direta (equitable delay defense)

**O Brasil não tem laches como instituto autônomo** (não há divisão law/equity). O funcional mais próximo é a **supressio** — doutrina derivada da boa-fé objetiva (CC art. 422): a inércia do titular de um direito, por período longo, pode gerar no outro contratante a legítima expectativa de que aquele direito não será mais exercido, tornando abusivo seu exercício tardio (CC art. 187 — abuso de direito).

**Elements (baseline — construção jurisprudencial):**
1. Inércia prolongada e objetivamente significativa do titular do direito
2. Comportamento da outra parte que gerou expectativa legítima de não exercício
3. Exercício tardio do direito que, à luz da boa-fé, se torna abusivo

*Caveat: isto não é uma prescrição (que tem prazo legal fixo) nem uma defesa codificada com elementos estáveis — é doutrina jurisprudencial mais maleável; sinalizar `[jurisprudência — sem prazo legal fixo, verificar precedentes]`. Não equiparar automaticamente ao prazo de laches americano.*

### Venire contra factum proprium (closest analog to equitable estoppel)

**Elements (baseline — doutrina derivada de CC art. 422, boa-fé objetiva — "doutrina dos atos próprios"):**
1. Conduta ou declaração inicial do réu (factum proprium)
2. Confiança da outra parte nessa conduta inicial
3. Comportamento contraditório posterior do réu, incompatível com a conduta inicial
4. Prejuízo ou injustiça decorrente da contradição, se admitida

*Caveat: mais próxima de estoppel do que "equitable" no sentido técnico americano — é aplicação da boa-fé objetiva, não uma categoria processual distinta de "law" (não há essa distinção no Brasil).*

### Renúncia (waiver)

**Elements (baseline — CC art. 191 (renúncia da prescrição, só admitida após a consumação e sem prejuízo de terceiro) e regra geral de interpretação restritiva da renúncia, art. 114 por analogia a negócios jurídicos benéficos):**
1. Existência de direito conhecido pelo titular
2. Manifestação de vontade, expressa ou tácita, de abrir mão desse direito — mas a **renúncia se interpreta restritivamente**; não se presume

*Caveat: renúncia à prescrição (art. 191) só é válida se a prescrição já se consumou — renúncia prévia (antes de consumada) é nula. Verificar se o caso trata de renúncia a prescrição especificamente (regime próprio) ou renúncia a outro direito (regime geral).*

### "Unclean hands" — sem correspondência direta

**O Brasil não tem "unclean hands" como defesa equitativa autônoma** (de novo, sem divisão law/equity). Os institutos mais próximos:

1. **Exceção de contrato não cumprido** (CC art. 476 — "nos contratos bilaterais, nenhum dos contratantes, antes de cumprida a sua obrigação, pode exigir o implemento da do outro") — específica de contratos bilaterais, não uma defesa geral de conduta reprovável do autor.
2. **Vedação ao enriquecimento sem causa por ato ilícito ou imoral** (CC art. 883 — "não terá direito à repetição do que pagou aquele que recebeu por dívida de jogo ou de aposta, mas o que se paga para obter fim ilícito, imoral, ou proibido por lei, não pode ser repetido" — aplicação da máxima *nemo auditur propriam turpitudinem allegans*, quem alega a própria torpeza não é ouvido).

**Elements (baseline, quando aplicável ao contexto de contrato bilateral — art. 476):**
1. Contrato bilateral com obrigações recíprocas
2. O autor não cumpriu sua própria obrigação
3. Por isso, não pode exigir o cumprimento da obrigação do réu

*Caveat: não generalizar como defesa ampla contra "conduta reprovável do autor" fora desses institutos específicos — o Direito brasileiro não reconhece unclean hands como princípio geral de defesa.*

### Quitação / transação (closest analog to release)

**Elements (baseline — CC arts. 320 (quitação) e 840-850 (transação)):**
1. Existência de acordo válido de quitação ou transação
2. Abrangência das pretensões em discussão (a transação interpreta-se restritivamente, art. 843 — "só quanto às pessoas e coisas compreendidas, permanecendo em vigor todas as cláusulas não expressamente atacadas")
3. Onerosidade/consideração (concessões recíprocas, elemento típico da transação) — a quitação simples (recibo de pagamento) não exige concessões recíprocas, apenas prova do pagamento
4. Celebração por parte com poderes para tanto (capacidade e, se representante, procuração com poderes específicos)

### Transação (accord and satisfaction)

**No Direito brasileiro, "accord and satisfaction" se funde com a transação (CC arts. 840-850)** — não há distinção formal entre os dois institutos como no common law.

**Elements (baseline — CC arts. 840-850; dação em pagamento, art. 356, se a prestação for diversa da originalmente devida):**
1. Disputa de boa-fé sobre obrigação controvertida ou duvidosa
2. Acordo entre as partes com concessões mútuas para extinguir a disputa (transação, art. 840) — ou, se a extinção se dá pela aceitação de prestação diversa da devida, **dação em pagamento** (art. 356)
3. Cumprimento efetivo do acordado
4. Aceitação da prestação pela parte credora

### Dever de mitigar o próprio prejuízo (closest analog to failure to mitigate damages)

**Não codificado expressamente no CC, mas adotado pela jurisprudência do STJ** como decorrência da boa-fé objetiva (CC art. 422) — o chamado "duty to mitigate the loss".

**Elements (baseline — construção jurisprudencial do STJ):**
1. O credor/vítima poderia ter reduzido o dano por esforço razoável
2. O credor/vítima deixou de adotar essa medida razoável
3. O valor pelo qual o dano poderia ter sido reduzido

*Caveat: isto é importação jurisprudencial (não há artigo do CC nomeando o "dever de mitigar"), então tratar como `[jurisprudência — verificar precedentes atuais do STJ]` antes de usar como defesa consolidada — é doutrina relativamente recente na prática brasileira comparada à tradição consolidada americana.*

### Culpa concorrente da vítima (comparative fault / contributory negligence)

**Elements (baseline — CC art. 945: "se a vítima tiver concorrido culposamente para o evento danoso, a sua indenização será fixada tendo-se em conta a gravidade de sua culpa em confronto com a do autor do dano"):**
1. Conduta culposa da própria vítima
2. Nexo causal entre essa conduta e o próprio dano sofrido
3. Ponderação proporcional da gravidade da culpa de cada parte para fixar o valor da indenização

*Caveat: o Brasil adota, por padrão e uniformemente, o regime de **culpa concorrente proporcional** (redução proporcional da indenização) — não existe a distinção americana entre pure comparative, modified comparative (50%/51% bar) e pure contributory (barreira total) que varia por estado; no Brasil o regime é único e nacional (art. 945), sem a barreira total de recuperação que ainda existe em alguns estados americanos.*

### "Assumption of risk" — sem correspondência direta codificada

**Sem doutrina autônoma equivalente.** Em contextos de responsabilidade objetiva por atividade de risco (CC art. 927, parágrafo único) ou atividades esportivas/perigosas, a jurisprudência por vezes reduz ou afasta a indenização considerando que a vítima **aceitou o risco inerente** à atividade (ex.: esportes de risco, participação voluntária em atividade perigosa conhecida) — mas isso é fator de ponderação dentro da análise de nexo causal e culpa concorrente (art. 945), não uma defesa autônoma com elementos próprios codificados.

**Elements (baseline, como fator de ponderação, não defesa estanque):**
1. Conhecimento efetivo do risco pela vítima
2. Aceitação voluntária de participar da atividade que gerou o risco
3. O dano decorreu exatamente do risco conhecido e aceito (e não de conduta adicional do réu que extrapola o risco normal da atividade)

*Caveat: não tratar como defesa completa e autônoma — é argumento que informa a análise de nexo causal/culpa concorrente; sinalizar como tal no chart, não como elemento de defesa nomeada e independente.*

### Esgotamento de vias administrativas (failure to exhaust administrative remedies)

**No Brasil, a regra é o inverso da americana: CF/88 art. 5º, XXXV consagra a inafastabilidade da jurisdição — "a lei não excluirá da apreciação do Poder Judiciário lesão ou ameaça a direito"** — de modo que, em regra, **não se exige esgotamento da via administrativa** como condição para acesso ao Judiciário.

**Exceções constitucionais específicas (rol restrito, não analogia geral):**
1. **Justiça Desportiva** (CF art. 217, §1º) — o Judiciário só admite ações relativas à disciplina e às competições desportivas após esgotadas as instâncias da Justiça Desportiva, observado o prazo máximo de 60 dias para proferir decisão final
2. **Habeas data** (Lei 9.507/1997 art. 8º, parágrafo único) — exige prova de recusa ou decurso de prazo no pedido administrativo prévio de acesso ou retificação de informação

**Elements (baseline, apenas nas hipóteses excepcionais acima):**
1. Norma constitucional ou legal excepcional exige esgotamento administrativo prévio para esta matéria específica (não presumir — o rol é restrito)
2. O autor não completou o processo administrativo exigido
3. Nenhuma exceção (urgência, risco de dano irreparável) afasta a exigência

*Caveat: **não aplicar esta defesa por analogia geral** — fora das hipóteses constitucionais específicas acima (Justiça Desportiva, habeas data) e de raras previsões legais setoriais, o esgotamento administrativo NÃO é exigível no Brasil, ao contrário da prática comum americana. Levantar esta defesa fora dessas hipóteses é, em regra, incorreto e deve ser flagado `[review — verificar se há exceção legal específica aplicável, pois a regra geral é a inafastabilidade da jurisdição]`.*

---

## Adicionando um template

Esta biblioteca não é exaustiva. Quando surgir nova causa de pedir ou defesa:
1. Mapear os elementos a partir do código, lei ou entendimento jurisprudencial consolidado (súmula do STJ/STF, tema repetitivo).
2. Se o template tende a se repetir entre casos, adicioná-lo aqui com a citação.
3. Registrar a divergência regional/tribunal — onde os elementos variam por tribunal (TJ estadual, TRT regional), dizer isso e dar uma formulação representativa alternativa.
4. Sinalizar explicitamente quando a causa de pedir americana não tem correspondência codificada direta no Brasil — não forçar um cognato falso; é melhor reconstruir a partir das cláusulas gerais (arts. 186, 187, 422 do CC) e dizer que é reconstrução, do que apresentar como se fosse pretensão nomeada e consolidada.

Templates são uma base, não uma autoridade. O código, a lei ou o entendimento jurisprudencial consolidado sempre controla.
