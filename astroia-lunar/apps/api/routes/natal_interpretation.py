"""
Route pour interprétations de placements du thème natal
Génère via Claude (Anthropic) avec cache intelligent
Version 2 - Prompt refondé, Sonnet + fallback Haiku
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
import logging

from database import get_db
from models.natal_interpretation import NatalInterpretation
from models.user import User
from schemas.natal_interpretation import (
    NatalInterpretationRequest,
    NatalInterpretationResponse
)
from services.natal_interpretation_service import (
    generate_with_sonnet_fallback_haiku,
    PROMPT_VERSION
)
from routes.auth import get_current_user

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/interpretation", response_model=NatalInterpretationResponse, status_code=status.HTTP_200_OK)
async def generate_natal_interpretation(
    request: NatalInterpretationRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Génère ou récupère une interprétation de placement natal (v2)

    Stratégie de cache:
    - Vérifie si existe en DB pour (user_id, chart_id, subject, lang, version=2)
    - Si oui → retourne depuis cache (instant)
    - Si non → appelle Claude Sonnet (fallback Haiku), puis sauvegarde

    Args:
        request: Données du chart + sujet à interpréter

    Returns:
        NatalInterpretationResponse avec texte et flag cached

    Raises:
        HTTPException 500: Si erreur génération ou DB
    """
    # 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
    user_id = int(current_user.id)

    # Validation: Lilith non supportée en v3+ (versions senior)
    if PROMPT_VERSION >= 3 and request.subject == 'lilith':
        logger.warning(f"⚠️ Lilith non supportée en v{PROMPT_VERSION} (version senior)")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Lilith n'est pas supportée en version {PROMPT_VERSION} (prompt senior professionnel). Utilisez la version 2 pour Lilith."
        )

    logger.info(
        f"📖 Demande interprétation v{PROMPT_VERSION} - user={user_id}, "
        f"chart={request.chart_id}, subject={request.subject}, lang={request.lang}"
    )

    # Version du prompt (v2)
    version = PROMPT_VERSION

    # Toujours chercher en cache (même si force_refresh=True, pour pouvoir supprimer l'ancienne)
    existing_interpretation: Optional[NatalInterpretation] = None

    try:
        user_id_int = int(user_id) if isinstance(user_id, str) else user_id
        result = await db.execute(
            select(NatalInterpretation).where(
                NatalInterpretation.user_id == user_id_int,
                NatalInterpretation.chart_id == request.chart_id,
                NatalInterpretation.subject == request.subject,
                NatalInterpretation.lang == request.lang,
                NatalInterpretation.version == version
            )
        )
        existing_interpretation = result.scalar_one_or_none()
    except Exception as db_err:
        logger.error(f"❌ Erreur DB cache lookup: {db_err}")
        raise

    # Si trouvé en cache ET pas de force_refresh → retourner immédiatement
    if existing_interpretation and not request.force_refresh:
        logger.info(f"✅ Interprétation v{version} trouvée en cache (id={existing_interpretation.id})")

        return NatalInterpretationResponse(
            id=str(existing_interpretation.id),
            text=existing_interpretation.output_text,
            cached=True,
            subject=existing_interpretation.subject,
            chart_id=existing_interpretation.chart_id,
            version=existing_interpretation.version,
            created_at=existing_interpretation.created_at
        )

    # Pas en cache → générer via Claude
    logger.info(f"🌐 Pas en cache → génération via Claude Sonnet (fallback Haiku)")
    
    # #region agent log
    import json
    import time
    try:
        log_data = {
            "location": "natal_interpretation.py:98",
            "message": "Before Claude generation",
            "data": {
                "subject": request.subject,
                "chart_payload_keys": list(request.chart_payload.model_dump().keys()),
                "chart_payload": request.chart_payload.model_dump()
            },
            "timestamp": int(time.time() * 1000),
            "sessionId": "debug-session",
            "runId": "run1",
            "hypothesisId": "A"
        }
        with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
            f.write(json.dumps(log_data) + "\n")
    except Exception as log_err:
        logger.warning(f"Erreur écriture log debug: {log_err}")
    # #endregion

    try:
        # Appeler Claude pour générer l'interprétation (Sonnet + fallback Haiku)
        # Passer la session DB pour charger interprétations pré-générées
        interpretation_text, model_used = await generate_with_sonnet_fallback_haiku(
            subject=request.subject,
            chart_payload=request.chart_payload.model_dump(),
            db=db
        )
        
        # #region agent log
        import json
        import time
        try:
            log_data = {
                "location": "natal_interpretation.py:129",
                "message": "After generate_with_sonnet_fallback_haiku",
                "data": {
                    "model_used": model_used,
                    "interpretation_length": len(interpretation_text) if interpretation_text else 0,
                    "has_text": bool(interpretation_text)
                },
                "timestamp": int(time.time() * 1000),
                "sessionId": "debug-session",
                "runId": "run1",
                "hypothesisId": "O"
            }
            with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                f.write(json.dumps(log_data) + "\n")
        except Exception as log_err:
            logger.warning(f"Erreur écriture log debug: {log_err}")
        # #endregion

        logger.info(f"✅ Interprétation générée avec {model_used} ({len(interpretation_text)} chars)")

        # Si force_refresh et qu'une interprétation existe, la supprimer avant d'insérer
        if request.force_refresh and existing_interpretation:
            logger.info(f"🗑️ Suppression ancienne interprétation (id={existing_interpretation.id}) pour régénération")
            await db.delete(existing_interpretation)
            await db.commit()
            # Réinitialiser existing_interpretation pour éviter les conflits
            existing_interpretation = None

        # Sauvegarder en DB (INSERT ou UPDATE selon si existe déjà)
        user_id_int = int(user_id) if isinstance(user_id, str) else user_id
        
        # #region agent log
        try:
            log_data = {
                "location": "natal_interpretation.py:163",
                "message": "Before DB save",
                "data": {
                    "user_id_int": user_id_int,
                    "has_existing": bool(existing_interpretation),
                    "interpretation_length": len(interpretation_text) if interpretation_text else 0,
                    "chart_id": request.chart_id,
                    "subject": request.subject
                },
                "timestamp": int(time.time() * 1000),
                "sessionId": "debug-session",
                "runId": "run1",
                "hypothesisId": "P"
            }
            with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                f.write(json.dumps(log_data) + "\n")
        except Exception as log_err:
            logger.warning(f"Erreur écriture log debug: {log_err}")
        # #endregion
        
        try:
            if existing_interpretation:
                # Mise à jour de l'interprétation existante
                existing_interpretation.input_json = request.chart_payload.model_dump()
                existing_interpretation.output_text = interpretation_text
                await db.commit()
                await db.refresh(existing_interpretation)
                new_interpretation = existing_interpretation
            else:
                # Nouvelle interprétation
                # #region agent log
                try:
                    log_data = {
                        "location": "natal_interpretation.py:195",
                        "message": "Creating new NatalInterpretation object",
                        "data": {
                            "user_id_int": user_id_int,
                            "chart_id": request.chart_id,
                            "subject": request.subject,
                            "lang": request.lang,
                            "version": version
                        },
                        "timestamp": int(time.time() * 1000),
                        "sessionId": "debug-session",
                        "runId": "run1",
                        "hypothesisId": "R"
                    }
                    with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps(log_data) + "\n")
                except Exception as log_err:
                    logger.warning(f"Erreur écriture log debug: {log_err}")
                # #endregion
                
                new_interpretation = NatalInterpretation(
                    user_id=user_id_int,
                    chart_id=request.chart_id,
                    subject=request.subject,
                    lang=request.lang,
                    version=version,
                    input_json=request.chart_payload.model_dump(),
                    output_text=interpretation_text
                )
                
                # #region agent log
                try:
                    log_data = {
                        "location": "natal_interpretation.py:220",
                        "message": "Before db.add",
                        "data": {
                            "interpretation_created": bool(new_interpretation),
                            "has_id": hasattr(new_interpretation, 'id')
                        },
                        "timestamp": int(time.time() * 1000),
                        "sessionId": "debug-session",
                        "runId": "run1",
                        "hypothesisId": "S"
                    }
                    with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps(log_data) + "\n")
                except Exception as log_err:
                    logger.warning(f"Erreur écriture log debug: {log_err}")
                # #endregion
                
                db.add(new_interpretation)
                
                # #region agent log
                try:
                    log_data = {
                        "location": "natal_interpretation.py:235",
                        "message": "Before db.commit",
                        "data": {},
                        "timestamp": int(time.time() * 1000),
                        "sessionId": "debug-session",
                        "runId": "run1",
                        "hypothesisId": "T"
                    }
                    with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps(log_data) + "\n")
                except Exception as log_err:
                    logger.warning(f"Erreur écriture log debug: {log_err}")
                # #endregion
                
                await db.commit()
                
                # #region agent log
                try:
                    log_data = {
                        "location": "natal_interpretation.py:248",
                        "message": "After db.commit, before db.refresh",
                        "data": {},
                        "timestamp": int(time.time() * 1000),
                        "sessionId": "debug-session",
                        "runId": "run1",
                        "hypothesisId": "U"
                    }
                    with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps(log_data) + "\n")
                except Exception as log_err:
                    logger.warning(f"Erreur écriture log debug: {log_err}")
                # #endregion
                
                await db.refresh(new_interpretation)
        except Exception as db_err:
            # #region agent log
            try:
                import traceback
                log_data = {
                    "location": "natal_interpretation.py:260",
                    "message": "DB save error",
                    "data": {
                        "error": str(db_err),
                        "error_type": type(db_err).__name__,
                        "traceback": traceback.format_exc()[:1000]
                    },
                    "timestamp": int(time.time() * 1000),
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "V"
                }
                with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps(log_data) + "\n")
            except Exception as log_err:
                logger.warning(f"Erreur écriture log debug: {log_err}")
            # #endregion
            logger.error(f"❌ Erreur DB lors de la sauvegarde: {db_err}", exc_info=True)
            await db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erreur lors de la sauvegarde de l'interprétation: {str(db_err)}"
            )
        
        # #region agent log
        try:
            log_data = {
                "location": "natal_interpretation.py:280",
                "message": "After DB save",
                "data": {
                    "interpretation_id": str(new_interpretation.id) if new_interpretation and hasattr(new_interpretation, 'id') else None,
                    "saved_successfully": bool(new_interpretation)
                },
                "timestamp": int(time.time() * 1000),
                "sessionId": "debug-session",
                "runId": "run1",
                "hypothesisId": "Q"
            }
            with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                f.write(json.dumps(log_data) + "\n")
        except Exception as log_err:
            logger.warning(f"Erreur écriture log debug: {log_err}")
        # #endregion

        logger.info(f"✅ Interprétation v{version} sauvegardée (id={new_interpretation.id}, model={model_used})")

        return NatalInterpretationResponse(
            id=str(new_interpretation.id),
            text=interpretation_text,
            cached=False,
            subject=new_interpretation.subject,
            chart_id=new_interpretation.chart_id,
            version=new_interpretation.version,
            created_at=new_interpretation.created_at
        )

    except Exception as e:
        logger.error(f"❌ Erreur génération interprétation: {str(e)}")
        await db.rollback()

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.delete("/interpretation/{chart_id}/{subject}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_natal_interpretation(
    chart_id: str,
    subject: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Supprime une interprétation (pour forcer une régénération)

    Args:
        chart_id: ID du chart
        subject: Objet céleste (ex: 'sun', 'moon')

    Returns:
        204 No Content
    """
    # 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
    user_id = int(current_user.id)

    result = await db.execute(
        select(NatalInterpretation).where(
            NatalInterpretation.user_id == user_id,
            NatalInterpretation.chart_id == chart_id,
            NatalInterpretation.subject == subject
        )
    )
    interpretation = result.scalar_one_or_none()

    if interpretation:
        await db.delete(interpretation)
        await db.commit()
        logger.info(f"🗑️ Interprétation supprimée: {chart_id}/{subject}")

    return None
