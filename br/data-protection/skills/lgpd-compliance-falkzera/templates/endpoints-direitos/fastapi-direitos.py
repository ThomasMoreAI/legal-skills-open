"""
FastAPI, endpoints de direitos do titular (LGPD art. 18)
==========================================================
Stack: FastAPI + SQLAlchemy + Pydantic. Compatível com Postgres
(schema em consent-log-schema.sql).

Cole em: app/routers/legal.py
Registre no main: app.include_router(legal.router, prefix="/api/legal")

Endpoints:
  GET    /api/legal/me         , confirmação simplificada (art. 18 I)
  GET    /api/legal/export     , portabilidade + acesso (art. 18 II e V)
  POST   /api/legal/consent    , registrar/revogar consentimento (art. 8º)
  DELETE /api/legal/account    , exclusão de conta (art. 18 VI + art. 16)
  POST   /api/legal/correction , pedido de correção (art. 18 III)
  POST   /api/legal/dsr        , abrir DSR genérico
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session

from app.deps import get_current_user, get_db, send_email
from app.models import (
    User,
    ConsentLog,
    DSRRequest,
    AuditLog,
    RetentionPolicy,
)
from app.security import verify_password
from app.settings import settings


router = APIRouter(tags=["legal"])


# === Helpers ==============================================================

def _truncate_ip(ip: str | None) -> str | None:
    if not ip:
        return None
    if ":" in ip:  # IPv6
        return ":".join(ip.split(":")[:4]) + "::"
    parts = ip.split(".")
    if len(parts) == 4:
        return ".".join(parts[:3]) + ".0"
    return ip


def _log_audit(
    db: Session,
    *,
    actor_type: str,
    actor_id: str | None,
    target_user_id: str | None,
    action: str,
    entity: str,
    metadata: dict | None = None,
    request: Request | None = None,
) -> None:
    entry = AuditLog(
        actor_type=actor_type,
        actor_id=actor_id,
        target_user_id=target_user_id,
        action=action,
        entity=entity,
        metadata=metadata or {},
        ip_truncated=_truncate_ip(
            request.headers.get("x-forwarded-for") if request else None
        ),
        user_agent=request.headers.get("user-agent") if request else None,
    )
    db.add(entry)
    db.commit()


# === 1. Confirmação simplificada (art. 18 I) ==============================

@router.get("/me")
def confirm_treatment(
    user: User = Depends(get_current_user),
) -> dict:
    return {
        "treatment_exists": True,
        "controller": settings.CONTROLLER_NAME,
        "dpo_contact": settings.DPO_CONTACT,
        "rights_url": f"{settings.APP_URL}/privacidade",
    }


# === 2. Acesso + Portabilidade (art. 18 II e V) ==========================

@router.get("/export")
def export_data(
    request: Request,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
) -> Response:
    consents = (
        db.query(ConsentLog)
        .filter(ConsentLog.user_id == user.id)
        .order_by(ConsentLog.created_at.desc())
        .all()
    )

    payload = {
        "$schema": "https://example.com/schemas/lgpd-export/v1.json",
        "$generated_at": datetime.now(timezone.utc).isoformat(),
        "$about": {
            "controller": settings.CONTROLLER_NAME,
            "controller_doc": settings.CONTROLLER_DOC,
            "dpo_contact": settings.DPO_CONTACT,
            "legal_basis": "LGPD art. 18 II (acesso) e V (portabilidade)",
            "scope": (
                "Inclui dados que você forneceu e que coletamos objetivamente. "
                "NÃO inclui inferências algorítmicas (segredo industrial)."
            ),
        },
        "profile": {
            "id": str(user.id),
            "email": user.email,
            "name": user.name,
            "phone": user.phone,
            "created_at": user.created_at.isoformat(),
        },
        "consents": [
            {
                "purpose": c.purpose,
                "granted": c.granted,
                "policy_version": c.policy_version,
                "collected_via": c.collected_via,
                "created_at": c.created_at.isoformat(),
            }
            for c in consents
        ],
        # adicionar outras seções relevantes ao seu app
    }

    _log_audit(
        db,
        actor_type="titular",
        actor_id=str(user.id),
        target_user_id=str(user.id),
        action="data_export",
        entity="lgpd_export",
        request=request,
    )

    import json
    body = json.dumps(payload, indent=2, ensure_ascii=False, default=str)
    return Response(
        content=body,
        media_type="application/json; charset=utf-8",
        headers={
            "Content-Disposition": (
                f'attachment; filename="meus-dados-{user.id}-'
                f'{datetime.now(timezone.utc).date().isoformat()}.json"'
            ),
            "Cache-Control": "no-store",
        },
    )


# === 3. Consentimento (art. 8º) =========================================

class ConsentEvent(BaseModel):
    purpose: str = Field(..., examples=["newsletter", "cookies_analytics"])
    granted: bool
    policy_version: str
    collected_via: Literal[
        "cookie_banner", "checkbox_signup", "settings_page", "api"
    ]


@router.post("/consent")
def record_consent(
    event: ConsentEvent,
    request: Request,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
) -> dict:
    entry = ConsentLog(
        user_id=user.id,
        purpose=event.purpose,
        granted=event.granted,
        policy_version=event.policy_version,
        collected_via=event.collected_via,
        ip_truncated=_truncate_ip(request.headers.get("x-forwarded-for")),
        user_agent=request.headers.get("user-agent"),
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return {"id": str(entry.id), "recorded_at": entry.created_at.isoformat()}


# === 4. Exclusão de conta (art. 18 VI + art. 16) ========================

class DeletionRequest(BaseModel):
    confirm: Literal["EXCLUIR PERMANENTEMENTE"]
    password: str


@router.delete("/account")
def delete_account(
    body: DeletionRequest,
    request: Request,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
) -> dict:
    if not verify_password(body.password, user.password_hash):
        raise HTTPException(401, detail="wrong_password")

    dsr = DSRRequest(
        user_id=user.id,
        requester_email=user.email,
        request_type="deletion",
        status="in_progress",
        due_at=datetime.now(timezone.utc)
        + timedelta(days=30 if settings.IS_ATPP else 15),
    )
    db.add(dsr)
    db.flush()

    policies = db.query(RetentionPolicy).all()
    report: list[dict] = []

    for p in policies:
        if p.on_delete_action == "hard_delete":
            _delete_category(db, p.data_category, user.id)
            action = "deleted"
        elif p.on_delete_action == "anonymize":
            _anonymize_category(db, p.data_category, user.id)
            action = "anonymized"
        else:  # retain_with_basis
            _flag_retention(db, p.data_category, user.id)
            action = "retained"
        report.append(
            {"category": p.data_category, "action": action, "reason": p.justification}
        )

    # Pseudonimizar conta
    user.is_deleted = True
    user.deleted_at = datetime.now(timezone.utc)
    user.email = f"deleted-{user.id}@deleted.invalid"
    user.name = "[excluído]"
    user.phone = None
    user.cpf = None

    dsr.status = (
        "partially_completed"
        if any(r["action"] == "retained" for r in report)
        else "completed"
    )
    dsr.completed_at = datetime.now(timezone.utc)
    dsr.response = str(report)
    db.commit()

    _log_audit(
        db,
        actor_type="titular",
        actor_id=str(user.id),
        target_user_id=str(user.id),
        action="data_deletion",
        entity="user_account",
        metadata={"report": report},
        request=request,
    )

    send_email(
        to=user.email,
        subject="Confirmação de exclusão de conta",
        body=_render_deletion_receipt(report),
    )

    return {
        "status": "ok",
        "message": "Sua conta foi excluída. Verifique seu e-mail.",
        "report": report,
    }


def _delete_category(_db: Session, _category: str, _user_id: str) -> None:
    """Mapear categoria → tabela(s) e executar DELETE."""
    ...


def _anonymize_category(_db: Session, _category: str, _user_id: str) -> None:
    """UPDATE setando hash/nulls em identificadores."""
    ...


def _flag_retention(_db: Session, _category: str, _user_id: str) -> None:
    """Marca dados como retidos por dever legal."""
    ...


def _render_deletion_receipt(report: list[dict]) -> str:
    lines = ["Sua conta em " + settings.APP_NAME + " foi excluída.", ""]
    deleted = [r for r in report if r["action"] != "retained"]
    retained = [r for r in report if r["action"] == "retained"]

    if deleted:
        lines += ["Dados eliminados ou anonimizados:"]
        lines += [f"  - {r['category']}" for r in deleted]
        lines += [""]
    if retained:
        lines += ["Dados retidos por obrigação legal:"]
        lines += [f"  - {r['category']}: {r['reason']}" for r in retained]
        lines += [""]
    lines += [f"Dúvidas: {settings.DPO_CONTACT}"]
    return "\n".join(lines)


# === 5. Pedido de correção (art. 18 III) ================================

class CorrectionRequest(BaseModel):
    field: str
    new_value: str
    justification: str | None = None


@router.post("/correction")
def request_correction(
    body: CorrectionRequest,
    request: Request,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
) -> dict:
    dsr = DSRRequest(
        user_id=user.id,
        requester_email=user.email,
        request_type="correction",
        status="received",
        notes=f"Field: {body.field}\nNew: {body.new_value}\nWhy: {body.justification}",
        due_at=datetime.now(timezone.utc)
        + timedelta(days=30 if settings.IS_ATPP else 15),
    )
    db.add(dsr)
    db.commit()
    db.refresh(dsr)
    return {"id": str(dsr.id), "status": dsr.status, "due_at": dsr.due_at.isoformat()}


# === 6. DSR genérico ===================================================

class GenericDSR(BaseModel):
    requester_email: EmailStr
    request_type: str
    notes: str | None = None


@router.post("/dsr")
def open_dsr(
    body: GenericDSR,
    db: Session = Depends(get_db),
    user: User | None = Depends(get_current_user, use_cache=False),
) -> dict:
    dsr = DSRRequest(
        user_id=user.id if user else None,
        requester_email=body.requester_email,
        request_type=body.request_type,
        status="received",
        notes=body.notes,
        due_at=datetime.now(timezone.utc)
        + timedelta(days=30 if settings.IS_ATPP else 15),
    )
    db.add(dsr)
    db.commit()
    db.refresh(dsr)
    return {"id": str(dsr.id), "status": dsr.status}
