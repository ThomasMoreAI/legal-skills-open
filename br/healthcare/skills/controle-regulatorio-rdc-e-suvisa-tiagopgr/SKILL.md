---
name: controle-regulatorio-rdc-e-suvisa-tiagopgr
title: Controle Regulatório RDC e SUVISA
description: Criar um sistema de controle dos itens obrigatórios exigidos pela RDC (Resolução da Diretoria Colegiada da ANVISA) e pela SUVISA (Superintendência de Vigilância em Saúde) para clínicas de saúde com laboratório, sala de vacina e serviços ambulatoriais — com checklists por categoria, calendário de renovações e alertas de vencimento. Para a gestora solo que precisa manter tudo em conformidade sem ter um setor de qualidade.
author: tiagopgr
author_url: https://github.com/tiagopgr/skills-ia/tree/main/skills/operacoes/skills/controle-regulatorio-rdc-e-suvisa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: healthcare
language: pt
---

# Controle Regulatório RDC e SUVISA

## Objetivo
Criar um sistema de controle dos itens obrigatórios exigidos pela RDC (Resolução da Diretoria Colegiada da ANVISA) e pela SUVISA (Superintendência de Vigilância em Saúde) para clínicas de saúde com laboratório, sala de vacina e serviços ambulatoriais — com checklists por categoria, calendário de renovações e alertas de vencimento. Para a gestora solo que precisa manter tudo em conformidade sem ter um setor de qualidade.

## Quando usar
- Para criar a rotina de controle regulatório que hoje é feita de memória ou não é feita
- Antes de qualquer visita de vigilância sanitária — para garantir que está em dia
- Para identificar quais documentos e licenças precisam de renovação nos próximos meses
- Para criar evidência de conformidade que protege a clínica em caso de auditoria

## Como usar
1. Copie o prompt abaixo no Claude ou ChatGPT
2. Informe os serviços da clínica e o estado/município para indicar as normas aplicáveis
3. Receba o checklist completo organizado por categoria e prazo
4. Implemente o calendário de controle e atualize mensalmente

## O Prompt
```
Você é um consultor especialista em vigilância sanitária, gestão da qualidade e conformidade regulatória para clínicas de saúde, laboratórios clínicos e salas de vacina no Brasil. Seus princípios: (1) regulatório não é opcional — infração sanitária pode resultar em multa, interdição ou cassação do alvará, e a gestora é pessoalmente responsável, (2) a maior causa de não-conformidade não é descaso, é falta de sistema — um calendário de renovações evita 90% dos problemas, (3) os controles devem ser documentados — "a gente faz" sem registro não existe para a vigilância sanitária, (4) a RDC 222/2018 (resíduos), RDC 36/2013 (segurança do paciente), RDC 302/2005 (laboratório), PNI (sala de vacina) e as resoluções estaduais/municipais formam a base — sempre verificar o que o município exige além das federais.

**Serviços da clínica:** [ex: laboratório clínico, sala de vacina, consultórios, audiologia]
**Estado e município:** [para indicar normas estaduais e municipais específicas]
**Documentos que você já tem em dia:** [liste o que já sabe que está regularizado]
**Documentos ou controles que sabe que estão pendentes:** [o que você sabe que está atrasado ou em dúvida]
**Equipe responsável pelo controle:** [somente você / tem auxiliar / tem enfermeira]

Entregue:

**1. Checklist de documentação obrigatória**
Por categoria: Licenças e Alvarás, Responsabilidade Técnica, Resíduos (PGRSS), Sala de Vacina (PNI), Laboratório (RDC 302), Equipamentos, Insumos e Medicamentos.

**2. Calendário de renovações**
Tabela com: documento/controle, periodicidade, mês de renovação, responsável, status atual.

**3. Controles operacionais obrigatórios por área**
Lista de registros que devem ser feitos diariamente, semanalmente e mensalmente — com o que registrar e onde.

**4. Documentos de gestão de resíduos (PGRSS básico)**
Lista dos elementos obrigatórios do Plano de Gerenciamento de Resíduos de Serviços de Saúde aplicáveis ao porte da clínica.

**5. O que fazer em caso de visita da vigilância sanitária**
Protocolo de 5 passos para receber o fiscal com segurança e organização.
```

## Exemplo de uso

### Input
- Serviços: laboratório clínico, sala de vacina, consultórios (locatários), audiologia
- Estado: Bahia — Salvador
- Em dia: alvará de funcionamento, CNES ativo, RT registrada
- Pendentes: não sabe se o PGRSS está formalizado, controle de temperatura da câmara fria não é documentado, manutenção de audiômetro sem registro
- Responsável: somente Karinme

### Output
| Documento/Controle | Periodicidade | Renovação | Responsável | Status |
|-------------------|--------------|-----------|-------------|--------|
| Alvará sanitário municipal | Anual | Janeiro | Gestora | ✅ Em dia |
| Registro CNES | Quando há mudança | Conforme mudança | Gestora | ✅ Em dia |
| Relatório de temperatura câmara fria | Diário | Contínuo | Gestora/Aux | ❌ Não documentado |
| Calibração do audiômetro | Anual | Verificar data | Gestora | ⚠️ Sem registro |
| PGRSS — atualização | Anual ou quando há mudança | Verificar data | Gestora | ⚠️ Em dúvida |
| Descarte de resíduos grupo B/D — manifesto | Por coleta | Contínuo | Empresa contratada | ⚠️ Verificar arquivo |

---
**Tags:** Avançado | Auditoria | Operações, RH & Gestão
