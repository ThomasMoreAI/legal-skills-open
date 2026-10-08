#!/usr/bin/env python3
"""
C5-REAL LEGALTECH FALSIFIER & DETERMINISTIC AUDITOR (PoC)
Sustrato de Falsación en Silicio (Autodidact-Ω · Fase 5)

Implementa la arquitectura de dos fases:
1. Validador de punteros de citas jurisprudenciales (Fail-Closed ante alucinaciones).
2. Verificador SMT (Z3) de prescripción procesal (Art. 1964 CC).
3. Evaluador formal de Playbook Contractual (Liability Cap / Jurisdicción).
4. Generador de Recibo de Atestación Causal (SHA3-256).
"""

import sys
import re
import json
import hashlib
from datetime import datetime, timezone
import z3

# ==============================================================================
# 1. BASE DE GROUND TRUTH OFICIAL (Simulador de Registro CENDOJ / BOE)
# ==============================================================================
OFFICIAL_CENDOJ_REGISTRY = {
    "STS 1234/2023": {
        "ecli": "ECLI:ES:TS:2023:1234",
        "date": "2023-04-18",
        "chamber": "Sala Primera (Civil)",
        "subject": "Cláusulas abusivas en contratos bancarios",
        "valid": True
    },
    "STS 567/2024": {
        "ecli": "ECLI:ES:TS:2024:567",
        "date": "2024-02-12",
        "chamber": "Sala Primera (Civil)",
        "subject": "Interrupción de la prescripción civil",
        "valid": True
    }
}

# ==============================================================================
# 2. MÓDULO 1: AUDITOR DETERMINISTA DE CITAS (ANTI-ALUCINACIÓN)
# ==============================================================================
def audit_legal_citations(legal_text: str) -> dict:
    """
    Escanea el texto generado buscando referencias STS y valida su existencia
    empírica en el registro oficial. Fail-Closed absoluto ante citas sintéticas.
    """
    # Regex para extraer sentencias del Tribunal Supremo (STS XXXX/YYYY)
    sts_pattern = re.compile(r"STS\s+(\d+/\d{4})", re.IGNORECASE)
    matches = sts_pattern.findall(legal_text)
    
    citations_found = []
    tainted_citations = []
    
    for match in matches:
        full_ref = f"STS {match}"
        citations_found.append(full_ref)
        if full_ref not in OFFICIAL_CENDOJ_REGISTRY:
            tainted_citations.append(full_ref)
            
    if tainted_citations:
        return {
            "status": "FAIL_CLOSED_TAINT",
            "error_code": "0xDEAD_6060:CORTEX-TAINT:FORGED-CITATION",
            "detail": f"Cita jurisprudencial alucinada o no indexada: {tainted_citations}",
            "citations_found": citations_found,
            "passed": False
        }
        
    return {
        "status": "VERIFIED",
        "citations_found": citations_found,
        "verified_count": len(citations_found),
        "passed": True
    }

# ==============================================================================
# 3. MÓDULO 2: VERIFICADOR SMT (Z3) DE PRESCRIPCIÓN PROCESAL (Art. 1964 CC)
# ==============================================================================
def verify_prescription_smt(days_elapsed: int, interruption_day: int | None = None) -> dict:
    """
    Modela con Z3 si una acción personal civil está formalmente prescrita (> 5 años = 1825 días).
    """
    solver = z3.Solver()
    
    t_hecho = z3.Int('t_hecho')
    t_demanda = z3.Int('t_demanda')
    t_interrup = z3.Int('t_interrup')
    prescrito = z3.Bool('prescrito')
    
    # Modelo del artículo 1964 del Código Civil
    # Prescribe si la diferencia supera 1825 días y no hubo interrupción intermedia válida
    solver.add(t_hecho == 0)
    solver.add(t_demanda == days_elapsed)
    
    if interruption_day is not None and 0 < interruption_day < days_elapsed:
        solver.add(t_interrup == interruption_day)
        # Con interrupción, el cómputo se reinicia desde t_interrup
        solver.add(prescrito == ((t_demanda - t_interrup) > 1825))
    else:
        solver.add(t_interrup == 0)
        solver.add(prescrito == (t_demanda > 1825))
        
    # Consultar si está prescrito
    solver.push()
    solver.add(prescrito == True)
    is_prescribed = (solver.check() == z3.sat)
    solver.pop()
    
    return {
        "days_elapsed": days_elapsed,
        "interruption_day": interruption_day,
        "prescribed": is_prescribed,
        "smt_status": "SAT" if is_prescribed else "UNSAT_NON_PRESCRIBED"
    }

# ==============================================================================
# 4. MÓDULO 3: VALIDADOR DE PLAYBOOK CONTRACTUAL
# ==============================================================================
class ContractPlaybook:
    def __init__(self, max_liability_pct: int, allowed_jurisdictions: set[str], allow_unilateral: bool):
        self.max_liability_pct = max_liability_pct
        self.allowed_jurisdictions = allowed_jurisdictions
        self.allow_unilateral = allow_unilateral

def evaluate_clause_compliance(clause: dict, playbook: ContractPlaybook) -> dict:
    """
    Aplica el lema formal de conformidad de cláusulas frente al playbook del bufete.
    """
    violations = []
    
    if clause.get("liability_cap_percent", 0) > playbook.max_liability_pct:
        violations.append(
            f"Liability cap {clause['liability_cap_percent']}% supera el máximo admisible ({playbook.max_liability_pct}%)"
        )
        
    jurisdiction = clause.get("governing_law", "")
    if jurisdiction not in playbook.allowed_jurisdictions:
        violations.append(
            f"Jurisdicción '{jurisdiction}' no autorizada. Permitidas: {playbook.allowed_jurisdictions}"
        )
        
    if clause.get("unilateral_termination", False) and not playbook.allow_unilateral:
        violations.append("Cláusula de rescisión unilateral no admitida por la política del despacho")
        
    return {
        "clause_id": clause.get("id", "UNKNOWN"),
        "compliant": len(violations) == 0,
        "violations": violations
    }

# ==============================================================================
# 5. PIPELINE PRINCIPAL DE PRUEBA DE ESTRÉS
# ==============================================================================
def run_stress_test():
    print("=" * 80)
    print("C5-REAL LEGALTECH DETERMINISTIC AUDITOR · EJECUCIÓN EN SILICIO (PoC)")
    print("=" * 80)
    
    # TEST 1: Detección de Alucinación Jurisprudencial (Caso Negativo / LLM Hallucination)
    print("\n[TEST 1] Ingesta de Borrador con Cita Falsa (Simulación Alucinación LLM):")
    tainted_draft = """
    Conforme a la doctrina fijada en la STS 9999/2023, la responsabilidad extracontractual
    queda exenta de fianza previa, reiterando el criterio de la STS 1234/2023.
    """
    result_t1 = audit_legal_citations(tainted_draft)
    print(f"  Resultado: {result_t1['status']}")
    print(f"  Detalle:   {result_t1.get('detail', 'N/A')}")
    assert result_t1["passed"] is False, "ERROR: La cita falsa no fue bloqueada!"
    print("  -> Veredicto: [SUPERADO] Fail-Closed activado. CORTEX-TAINT registrado.")

    # TEST 2: Ingesta de Borrador Válido (Caso Positivo)
    print("\n[TEST 2] Ingesta de Borrador con Cita Auténtica Verificada:")
    valid_draft = "El régimen de prescripción civil se rige por la STS 1234/2023."
    result_t2 = audit_legal_citations(valid_draft)
    print(f"  Resultado: {result_t2['status']} (Citas verificadas: {result_t2['verified_count']})")
    assert result_t2["passed"] is True, "ERROR: La cita legítima fue rechazada!"
    print("  -> Veredicto: [SUPERADO] Puntero formal CENDOJ validado en 0(1).")

    # TEST 3: Verificación SMT Z3 de Prescripción (Art. 1964 CC)
    print("\n[TEST 3] Verificación SMT de Prescripción Procesal:")
    # Caso 3a: 2000 días sin interrupción (> 1825) -> PRESCRIBED
    res_smt_1 = verify_prescription_smt(days_elapsed=2000, interruption_day=None)
    print(f"  Caso 3a (2000 días sin interrupción): Prescrito = {res_smt_1['prescribed']} ({res_smt_1['smt_status']})")
    assert res_smt_1["prescribed"] is True
    
    # Caso 3b: 2000 días con burofax interruptivo en día 1000 (delta restante 1000 < 1825) -> VIVA
    res_smt_2 = verify_prescription_smt(days_elapsed=2000, interruption_day=1000)
    print(f"  Caso 3b (2000 días con interrupción en d=1000): Prescrito = {res_smt_2['prescribed']} ({res_smt_2['smt_status']})")
    assert res_smt_2["prescribed"] is False
    print("  -> Veredicto: [SUPERADO] Deducción matemática por resolvedor Z3 formalmente exacta.")

    # TEST 4: Evaluación de Playbook Contractual
    print("\n[TEST 4] Auditoría de Cláusulas frente a Playbook:")
    playbook = ContractPlaybook(
        max_liability_pct=100,
        allowed_jurisdictions={"España", "UE-Bruselas"},
        allow_unilateral=False
    )
    
    bad_clause = {
        "id": "CLAUSE-SEC-8.2",
        "liability_cap_percent": 250, # Violación
        "governing_law": "Delaware, USA", # Violación
        "unilateral_termination": True # Violación
    }
    eval_bad = evaluate_clause_compliance(bad_clause, playbook)
    print(f"  Cláusula infractora: Conforme = {eval_bad['compliant']}")
    for v in eval_bad["violations"]:
        print(f"    - Flag: {v}")
    assert eval_bad["compliant"] is False
    print("  -> Veredicto: [SUPERADO] Triple violación detectada deterministamente.")

    # GENERACIÓN DE RECIBO FINAL SCITT-COMPLIANT
    telemetry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "audit_pipeline": "C5-REAL-LEGALTECH-FALSIFIER-v1.0",
        "tests_executed": 4,
        "all_invariants_held": True,
        "z3_kernel_version": list(z3.get_version()),
        "falsification_result": "SUCCESS"
    }
    serialized = json.dumps(telemetry, sort_keys=True)
    receipt_hash = hashlib.sha3_256(serialized.encode('utf-8')).hexdigest()
    
    print("\n" + "=" * 80)
    print("ATESTACIÓN DE SILICIO FINAL:")
    print(f"  Receipt SHA3-256: {receipt_hash}")
    print(f"  Invariantes Verificadas: 100% | Falsación Popperiana Completada.")
    print("=" * 80)
    return receipt_hash

if __name__ == "__main__":
    run_stress_test()
