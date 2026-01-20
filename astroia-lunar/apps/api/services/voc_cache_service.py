"""
Service de cache optimisé pour Void of Course (VoC) Status
- Cache en mémoire avec TTL configurable
- Retry logic pour requêtes DB
- Prévention des doublons
- Performance optimisée pour requêtes fréquentes
"""

import logging
import time
import asyncio
from datetime import datetime, timedelta, timezone
from typing import Dict, Any, Optional, List
from functools import wraps

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from sqlalchemy.exc import SQLAlchemyError

from models.lunar_pack import LunarVocWindow

logger = logging.getLogger(__name__)

# Configuration cache
VOC_STATUS_CACHE_TTL = 120  # 2 minutes (VoC change peu fréquemment)
VOC_CURRENT_CACHE_TTL = 60   # 1 minute

# Configuration retry logic
MAX_DB_RETRIES = 3
BASE_DB_BACKOFF = 0.2  # secondes
MAX_DB_BACKOFF = 2.0   # secondes

# Cache global avec timestamp
_VOC_STATUS_CACHE: Dict[str, Any] = {
    "data": None,
    "timestamp": 0,
    "ttl": VOC_STATUS_CACHE_TTL
}

_VOC_CURRENT_CACHE: Dict[str, Any] = {
    "data": None,
    "timestamp": 0,
    "ttl": VOC_CURRENT_CACHE_TTL
}


def _with_db_retry(max_retries: int = MAX_DB_RETRIES):
    """
    Décorateur pour ajouter retry logic aux requêtes DB avec exponential backoff.

    Args:
        max_retries: Nombre maximum de tentatives

    Returns:
        Décorateur pour fonction async
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)

                except SQLAlchemyError as e:
                    if attempt < max_retries - 1:
                        # Calcul du backoff avec jitter
                        backoff = min(BASE_DB_BACKOFF * (2 ** attempt), MAX_DB_BACKOFF)
                        jitter = backoff * 0.3
                        wait_time = backoff + jitter

                        logger.warning(
                            f"⚠️  DB error in {func.__name__}, "
                            f"retry {attempt + 1}/{max_retries} in {wait_time:.2f}s: {str(e)}"
                        )
                        await asyncio.sleep(wait_time)
                        continue
                    else:
                        # Dernière tentative échouée
                        logger.error(
                            f"❌ DB error in {func.__name__} after {max_retries} attempts: {str(e)}",
                            exc_info=True
                        )
                        raise

                except Exception as e:
                    # Autres erreurs non-SQL (ne pas retry)
                    logger.error(
                        f"❌ Unexpected error in {func.__name__}: {str(e)}",
                        exc_info=True
                    )
                    raise

            # Normalement inaccessible
            raise Exception(f"Unexpected retry loop exit in {func.__name__}")

        return wrapper
    return decorator


@_with_db_retry()
async def _fetch_current_voc_from_db(db: AsyncSession) -> Optional[LunarVocWindow]:
    """
    Récupère la fenêtre VoC active actuellement depuis la DB avec retry logic.

    Args:
        db: Session DB async

    Returns:
        LunarVocWindow active ou None

    Raises:
        SQLAlchemyError: Si échec après retries
    """
    now = datetime.now(timezone.utc)

    stmt = select(LunarVocWindow).where(
        and_(
            LunarVocWindow.start_at <= now,
            LunarVocWindow.end_at >= now
        )
    ).order_by(LunarVocWindow.start_at.asc()).limit(1)
    result = await db.execute(stmt)
    return result.scalars().first()


@_with_db_retry()
async def _fetch_next_voc_from_db(db: AsyncSession) -> Optional[LunarVocWindow]:
    """
    Récupère la prochaine fenêtre VoC depuis la DB avec retry logic.

    Args:
        db: Session DB async

    Returns:
        Prochaine LunarVocWindow ou None

    Raises:
        SQLAlchemyError: Si échec après retries
    """
    now = datetime.now(timezone.utc)

    stmt = select(LunarVocWindow).where(
        LunarVocWindow.start_at > now
    ).order_by(LunarVocWindow.start_at.asc()).limit(1)

    result = await db.execute(stmt)
    return result.scalar_one_or_none()


@_with_db_retry()
async def _fetch_upcoming_voc_from_db(
    db: AsyncSession,
    hours: int = 48,
    limit: int = 3
) -> List[LunarVocWindow]:
    """
    Récupère les prochaines fenêtres VoC dans les N heures avec retry logic.

    Args:
        db: Session DB async
        hours: Nombre d'heures à regarder en avant
        limit: Nombre maximum de fenêtres à retourner

    Returns:
        Liste de LunarVocWindow

    Raises:
        SQLAlchemyError: Si échec après retries
    """
    now = datetime.now(timezone.utc)
    future_limit = now + timedelta(hours=hours)

    stmt = select(LunarVocWindow).where(
        and_(
            LunarVocWindow.start_at > now,
            LunarVocWindow.start_at <= future_limit
        )
    ).order_by(LunarVocWindow.start_at.asc()).limit(limit)

    result = await db.execute(stmt)
    return result.scalars().all()


async def get_voc_status_cached(db: AsyncSession) -> Dict[str, Any]:
    """
    Récupère le VoC status complet (current, next, upcoming) avec cache.

    Cache TTL: 2 minutes (VoC change peu fréquemment)

    Args:
        db: Session DB async

    Returns:
        {
            "now": {"is_active": bool, "start_at": str, "end_at": str} | None,
            "next": {"start_at": str, "end_at": str} | None,
            "upcoming": [{"start_at": str, "end_at": str}]
        }

    Raises:
        Exception: Si erreur DB après retries
    """
    global _VOC_STATUS_CACHE

    # Vérifier le cache
    current_time = time.time()
    if (
        _VOC_STATUS_CACHE["data"] is not None
        and (current_time - _VOC_STATUS_CACHE["timestamp"]) < _VOC_STATUS_CACHE["ttl"]
    ):
        cache_age = int(current_time - _VOC_STATUS_CACHE["timestamp"])
        logger.info(f"[VoCStatus] ✅ Cache hit (age: {cache_age}s)")
        return _VOC_STATUS_CACHE["data"]

    # Cache miss - fetch from DB
    logger.info("[VoCStatus] 🔄 Cache miss, fetching from DB")

    try:
        # Fetch en parallèle pour optimiser performance
        current_voc, next_voc, upcoming_vocs = await asyncio.gather(
            _fetch_current_voc_from_db(db),
            _fetch_next_voc_from_db(db),
            _fetch_upcoming_voc_from_db(db, hours=48, limit=3)
        )

        # Construire current_window
        current_window = None
        if current_voc:
            current_window = {
                "is_active": True,
                "start_at": current_voc.start_at.isoformat(),
                "end_at": current_voc.end_at.isoformat()
            }

        # Construire next_window
        next_window = None
        if next_voc:
            next_window = {
                "start_at": next_voc.start_at.isoformat(),
                "end_at": next_voc.end_at.isoformat()
            }

        # Construire upcoming_windows
        upcoming_windows = [
            {
                "start_at": voc.start_at.isoformat(),
                "end_at": voc.end_at.isoformat()
            }
            for voc in upcoming_vocs
        ]

        # Construire réponse
        result = {
            "now": current_window,
            "next": next_window,
            "upcoming": upcoming_windows
        }

        # Mettre à jour le cache
        _VOC_STATUS_CACHE["data"] = result
        _VOC_STATUS_CACHE["timestamp"] = current_time

        logger.info(f"[VoCStatus] 💾 Cache updated (current: {current_window is not None}, next: {next_window is not None})")

        return result

    except Exception as e:
        logger.error(f"[VoCStatus] ❌ Error fetching VoC status: {str(e)}", exc_info=True)
        # Si cache existe (même expiré), le retourner en fallback
        if _VOC_STATUS_CACHE["data"] is not None:
            logger.warning("[VoCStatus] ⚠️  Returning stale cache as fallback")
            return _VOC_STATUS_CACHE["data"]
        raise


async def get_current_voc_cached(db: AsyncSession) -> Dict[str, Any]:
    """
    Récupère le VoC actuel uniquement avec cache court (1 minute).

    Args:
        db: Session DB async

    Returns:
        {
            "is_active": bool,
            "start_at": str | None,
            "end_at": str | None,
            "source": dict | None
        }

    Raises:
        Exception: Si erreur DB après retries
    """
    global _VOC_CURRENT_CACHE

    # Vérifier le cache
    current_time = time.time()
    if (
        _VOC_CURRENT_CACHE["data"] is not None
        and (current_time - _VOC_CURRENT_CACHE["timestamp"]) < _VOC_CURRENT_CACHE["ttl"]
    ):
        cache_age = int(current_time - _VOC_CURRENT_CACHE["timestamp"])
        logger.info(f"[VoCCurrent] ✅ Cache hit (age: {cache_age}s)")
        return _VOC_CURRENT_CACHE["data"]

    # Cache miss - fetch from DB
    logger.info("[VoCCurrent] 🔄 Cache miss, fetching from DB")

    try:
        active_voc = await _fetch_current_voc_from_db(db)

        if active_voc:
            result = {
                "is_active": True,
                "start_at": active_voc.start_at.isoformat(),
                "end_at": active_voc.end_at.isoformat(),
                "source": active_voc.source
            }
        else:
            result = {
                "is_active": False,
                "start_at": None,
                "end_at": None,
                "source": None
            }

        # Mettre à jour le cache
        _VOC_CURRENT_CACHE["data"] = result
        _VOC_CURRENT_CACHE["timestamp"] = current_time

        logger.info(f"[VoCCurrent] 💾 Cache updated (is_active: {result['is_active']})")

        return result

    except Exception as e:
        logger.error(f"[VoCCurrent] ❌ Error fetching current VoC: {str(e)}", exc_info=True)
        # Si cache existe (même expiré), le retourner en fallback
        if _VOC_CURRENT_CACHE["data"] is not None:
            logger.warning("[VoCCurrent] ⚠️  Returning stale cache as fallback")
            return _VOC_CURRENT_CACHE["data"]
        raise


@_with_db_retry()
async def save_voc_window_safe(
    db: AsyncSession,
    start_at: datetime,
    end_at: datetime,
    source: Dict[str, Any]
) -> Optional[LunarVocWindow]:
    """
    Sauvegarde une fenêtre VoC en évitant les doublons.

    Stratégie anti-doublons:
    - Vérifier si une fenêtre existe déjà avec les mêmes start_at/end_at
    - Si oui, mettre à jour plutôt que créer

    Args:
        db: Session DB async
        start_at: Début de la fenêtre VoC (timezone aware)
        end_at: Fin de la fenêtre VoC (timezone aware)
        source: Données brutes du provider

    Returns:
        LunarVocWindow créé ou mis à jour, ou None si erreur

    Raises:
        SQLAlchemyError: Si échec après retries
    """
    try:
        # Vérifier si une fenêtre identique existe déjà
        stmt = select(LunarVocWindow).where(
            and_(
                LunarVocWindow.start_at == start_at,
                LunarVocWindow.end_at == end_at
            )
        )
        result = await db.execute(stmt)
        existing_window = result.scalar_one_or_none()

        if existing_window:
            # Fenêtre existe déjà - mettre à jour source si différent
            if existing_window.source != source:
                existing_window.source = source
                await db.flush()
                await db.commit()
                logger.info(f"♻️  VoC window updated: {start_at} -> {end_at}")
            else:
                logger.info(f"✅ VoC window already exists (no change): {start_at} -> {end_at}")
            return existing_window
        else:
            # Créer nouvelle fenêtre
            voc_window = LunarVocWindow(
                start_at=start_at,
                end_at=end_at,
                source=source
            )
            db.add(voc_window)
            await db.flush()
            await db.commit()
            logger.info(f"💾 New VoC window saved: {start_at} -> {end_at}")

            # Invalider le cache après insertion
            clear_cache()

            return voc_window

    except Exception as e:
        logger.error(f"❌ Error saving VoC window: {str(e)}", exc_info=True)
        try:
            await db.rollback()
        except Exception:
            pass
        raise


def clear_cache():
    """Invalide tous les caches VoC (utile après mise à jour DB ou pour tests)"""
    global _VOC_STATUS_CACHE, _VOC_CURRENT_CACHE

    _VOC_STATUS_CACHE["data"] = None
    _VOC_STATUS_CACHE["timestamp"] = 0

    _VOC_CURRENT_CACHE["data"] = None
    _VOC_CURRENT_CACHE["timestamp"] = 0

    logger.info("[VoCCache] 🗑️  All caches cleared")


def get_cache_stats() -> Dict[str, Any]:
    """
    Retourne les statistiques des caches VoC (pour monitoring).

    Returns:
        {
            "voc_status": {"has_data": bool, "age_seconds": int, "ttl": int},
            "voc_current": {"has_data": bool, "age_seconds": int, "ttl": int}
        }
    """
    current_time = time.time()

    return {
        "voc_status": {
            "has_data": _VOC_STATUS_CACHE["data"] is not None,
            "age_seconds": int(current_time - _VOC_STATUS_CACHE["timestamp"])
                if _VOC_STATUS_CACHE["timestamp"] > 0 else None,
            "ttl": _VOC_STATUS_CACHE["ttl"]
        },
        "voc_current": {
            "has_data": _VOC_CURRENT_CACHE["data"] is not None,
            "age_seconds": int(current_time - _VOC_CURRENT_CACHE["timestamp"])
                if _VOC_CURRENT_CACHE["timestamp"] > 0 else None,
            "ttl": _VOC_CURRENT_CACHE["ttl"]
        }
    }
