# Núcleo — modelo de severidade

## Objetivo
Normalizar severidade dos achados para priorização técnica e jurídica consistente.

## Níveis canônicos

### `CRITICO`
Violação grave com alto potencial de dano ao titular, infração relevante da LGPD ou exposição sensível imediata.

Exemplos:
- ausência de base legal para tratamento sensível;
- vazamento de dados sensíveis;
- credenciais em texto puro;
- bucket público com dados pessoais.

### `ALTO`
Risco jurídico/técnico elevado, com impacto relevante e alta probabilidade de incidente.

Exemplos:
- logs com dados pessoais sem mascaramento;
- ausência de criptografia em repouso para dados críticos;
- APIs com autenticação/autorização fraca.

### `MEDIO`
Não conformidade relevante, mas sem exposição imediata crítica.

Exemplos:
- retenção sem política clara;
- gestão parcial de direitos do titular;
- consentimento pouco granular.

### `BAIXO`
Melhoria recomendada com baixo risco imediato.

Exemplos:
- ajustes de clareza documental;
- melhoria de linguagem de política;
- pequenas melhorias de UX de consentimento.

## Modulação por porte e exposição
A severidade pode ser **reduzida em um nível** (ex.: `ALTO` → `MEDIO`) quando todas as condições abaixo forem verdadeiras:
- o agente de tratamento é de **pequeno porte** nos termos da Res. CD/ANPD nº 2/2022 (microempresa, empresa de pequeno porte, startup, pessoa jurídica de direito privado, inclusive sem fins lucrativos, ou pessoa natural e ente privado despersonalizado que atue como controlador ou operador), sem as exclusões da própria resolução (como faturamento acima do limite ou grupo econômico que o ultrapasse);
- não há **tratamento de alto risco** nos critérios da mesma resolução (larga escala ou impacto significativo, combinados com tecnologia emergente, vigilância, decisão automatizada, dados sensíveis ou de crianças, adolescentes e idosos);
- não há exposição explorável confirmada.

### Como decidir se há tratamento de alto risco
A Res. CD/ANPD nº 2/2022 (art. 4º) exige, ao mesmo tempo, um critério **específico** e um critério **geral**. A resolução não fixa número de titulares para "larga escala", então a auditoria decide assim, sempre com evidência:

1. **Critério específico** — presente se houver ao menos um:
   - tecnologia emergente ou inovadora (ex.: IA generativa aplicada a dados pessoais);
   - vigilância ou controle de zonas acessíveis ao público;
   - decisão tomada unicamente por tratamento automatizado, inclusive perfilamento;
   - dado pessoal sensível (com a extensão do art. 11, §1º, descrita em `core/scoring-engine.md`) ou dado de crianças, adolescentes ou idosos.
2. **Critério geral** — presente se houver ao menos um:
   - **impacto significativo**: o tratamento pode impedir o exercício de direitos ou o uso de um serviço, ou causar dano material ou moral (discriminação, dano à integridade física, à imagem ou à reputação, fraude financeira, roubo de identidade). Posição do framework, para tornar a decisão verificável — considera-se presente quando:
     - o tratamento decide o acesso do titular a serviço, crédito, emprego ou benefício; ou
     - os dados, se expostos, permitem fraude ou roubo de identidade: documento de identificação (CPF, RG) junto com dados de contato ou financeiros, credenciais, dados bancários ou de cartão; ou
     - o dado sensível, ou que revele informação sensível, é parte da atividade-fim do serviço (ex.: sistema de clínica, de sindicato, de biometria), e não um registro incidental (ex.: o atestado de um funcionário);
   - **larga escala**: número significativo de titulares, considerados volume de dados, duração, frequência e extensão geográfica. Sem limiar numérico na norma, vale o que o auditado declarar ou o que a evidência mostrar; não se presume.
3. **Decisão:**
   - sem critério específico: não há alto risco;
   - com critério específico e critério geral: há alto risco;
   - com critério específico e sem evidência suficiente para decidir o critério geral: tratar como alto risco e registrar a dúvida como verificação pendente.

O relatório registra, na natureza do agente (`score_lgpd`), quais critérios foram encontrados e com que evidência, e recomenda confirmar o enquadramento com a assessoria jurídica.

**Exposição explorável confirmada** é a falha que permite acesso indevido a dado pessoal, evidenciada no código ou na configuração: rota sem autenticação que devolve dado pessoal, armazenamento público, credencial exposta. Não exige exploração real nem incidente ocorrido.

Nunca modular:
- achados `CRITICO` que envolvam dados sensíveis, dados de crianças e adolescentes, vazamento confirmado ou credenciais expostas;
- deveres que a própria norma não modula por porte (ex.: comunicação de incidente, prazos do titular).

Toda modulação é registrada no `finding` (`severity_modulation`: severidade original, aplicada e justificativa) e vale também para a `criticality` do item no score. Pessoa natural que trata dados para fins exclusivamente particulares e não econômicos está fora da LGPD (art. 4º, I): nesse caso, registrar a inaplicabilidade em vez de emitir achados.

## Regras de uso
- Cada `finding` deve ter um único nível de severidade.
- Quando mais de uma regra de severidade, do mesmo módulo ou de módulos diferentes, se aplicar ao mesmo achado, vale a mais específica; se forem igualmente específicas, a mais alta.
- Em dúvida entre dois níveis, usar o mais alto quando houver impacto jurídico potencial significativo.
- Achados `CRITICO` e `ALTO` devem ter plano de ação com prazo definido.
