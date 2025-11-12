"""
Route pour lectures complètes de thèmes natals
Optimisé avec cache pour limiter les appels API
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql import func
from typing import Optional

from database import get_db
from models.natal_reading import NatalReading
from schemas.natal_reading import (
    NatalReadingRequest,
    NatalReadingResponse,
    BirthData,
    NatalReadingOptions
)
from services.natal_reading_service import (
    generate_natal_reading,
    generate_cache_key
)
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/reading", response_model=NatalReadingResponse, status_code=status.HTTP_200_OK)
async def create_natal_reading(
    request: NatalReadingRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Génère ou récupère une lecture complète de thème natal
    
    Stratégie de cache:
    - Génère une clé unique basée sur birth_data
    - Si existe en DB et < 30 jours → retourne depuis cache
    - Sinon → appelle RapidAPI (3-4 appels) et sauvegarde
    
    Coût API:
    - Premier appel: 3-4 requêtes RapidAPI
    - Appels suivants: 0 requête (cache)
    """
    
    # Générer la clé de cache
    cache_key = generate_cache_key(request.birth_data.model_dump())
    
    logger.info(f"📖 Demande lecture natal - cache_key: {cache_key}")
    
    # Vérifier force_refresh
    force_refresh = request.options.force_refresh if request.options else False
    
    if force_refresh:
        logger.info("🔄 force_refresh=True → bypass du cache")
        existing_reading = None
    else:
        # Chercher en cache
        result = await db.execute(
            select(NatalReading).where(NatalReading.cache_key == cache_key)
        )
        existing_reading = result.scalar_one_or_none()
    
    if existing_reading and not force_refresh:
        logger.info(f"✅ Lecture trouvée en cache (id={existing_reading.id})")
        
        # Préparer la réponse AVANT le commit (éviter greenlet issues)
        response_data = {
            'id': existing_reading.id,
            'subject_name': request.birth_data.city,
            'birth_data': request.birth_data,
            'positions': existing_reading.reading['positions'],
            'aspects': existing_reading.reading['aspects'],
            'lunar': existing_reading.reading['lunar'],
            'summary': existing_reading.reading['summary'],
            'full_report_text': existing_reading.reading.get('full_report_text'),
            'source': "cache",
            'api_calls_count': 0,
            'created_at': existing_reading.created_at,
            'last_accessed_at': existing_reading.last_accessed_at
        }
        
        # Mettre à jour last_accessed_at (exécution SQL directe)
        from sqlalchemy import update
        stmt = update(NatalReading).where(NatalReading.id == existing_reading.id).values(last_accessed_at=func.now())
        await db.execute(stmt)
        await db.commit()
        
        # Retourner depuis le cache
        return NatalReadingResponse(**response_data)
    
    # Pas en cache → générer via API
    logger.info("🌐 Pas en cache → génération via RapidAPI")
    
    try:
        result_data = await generate_natal_reading(
            birth_data=request.birth_data.model_dump(),
            options=request.options.model_dump() if request.options else {}
        )
        
        # Sauvegarder en DB
        new_reading = NatalReading(
            cache_key=cache_key,
            birth_data=request.birth_data.model_dump(),
            reading=result_data['reading'],
            source="api",
            api_calls_count=result_data['api_calls_count'],
            language=request.options.language if request.options else "fr",
            includes_full_report=request.options.include_full_report if request.options else False
        )
        
        db.add(new_reading)
        await db.commit()
        await db.refresh(new_reading)
        
        logger.info(f"✅ Lecture sauvegardée (id={new_reading.id}, API calls={result_data['api_calls_count']})")
        
        return NatalReadingResponse(
            id=new_reading.id,
            subject_name=request.birth_data.city,
            birth_data=request.birth_data,
            positions=new_reading.reading['positions'],
            aspects=new_reading.reading['aspects'],
            lunar=new_reading.reading['lunar'],
            summary=new_reading.reading['summary'],
            full_report_text=new_reading.reading.get('full_report_text'),
            source="api",
            api_calls_count=result_data['api_calls_count'],
            created_at=new_reading.created_at,
            last_accessed_at=new_reading.last_accessed_at
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur génération lecture: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur lors de la génération du thème natal: {str(e)}"
        )


@router.get("/reading/{cache_key}", response_model=NatalReadingResponse)
async def get_natal_reading_by_key(
    cache_key: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Récupère une lecture existante par sa clé de cache
    """
    result = await db.execute(
        select(NatalReading).where(NatalReading.cache_key == cache_key)
    )
    reading = result.scalar_one_or_none()
    
    if not reading:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lecture non trouvée"
        )
    
    # Mettre à jour last_accessed_at
    from sqlalchemy.sql import func
    reading.last_accessed_at = func.now()
    await db.commit()
    
    return NatalReadingResponse(
        id=reading.id,
        subject_name=reading.birth_data.get('city'),
        birth_data=BirthData(**reading.birth_data),
        positions=reading.reading['positions'],
        aspects=reading.reading['aspects'],
        lunar=reading.reading['lunar'],
        summary=reading.reading['summary'],
        full_report_text=reading.reading.get('full_report_text'),
        source="cache",
        api_calls_count=0,
        created_at=reading.created_at,
        last_accessed_at=reading.last_accessed_at
    )


@router.delete("/reading/{cache_key}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_natal_reading(
    cache_key: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Supprime une lecture (pour forcer une régénération)
    """
    result = await db.execute(
        select(NatalReading).where(NatalReading.cache_key == cache_key)
    )
    reading = result.scalar_one_or_none()
    
    if reading:
        await db.delete(reading)
        await db.commit()
        logger.info(f"🗑️ Lecture supprimée: {cache_key}")
    
    return None

