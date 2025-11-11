"""Routes pour révolutions lunaires"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import List
from datetime import datetime, timedelta

from database import get_db
from models.user import User
from models.natal_chart import NatalChart
from models.lunar_return import LunarReturn
from routes.auth import get_current_user
from services.ephemeris import ephemeris_client
from services.interpretations import generate_lunar_return_interpretation

router = APIRouter()


# === SCHEMAS ===
class LunarReturnResponse(BaseModel):
    id: int
    month: str
    return_date: str
    lunar_ascendant: str
    moon_house: int
    moon_sign: str
    aspects: list
    interpretation: str


# === ROUTES ===
@router.post("/generate", status_code=status.HTTP_201_CREATED)
async def generate_lunar_returns(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Génère les 12 révolutions lunaires de l'année en cours
    Nécessite un thème natal calculé au préalable
    """
    
    # Vérifier que le thème natal existe
    result = await db.execute(
        select(NatalChart).where(NatalChart.user_id == current_user.id)
    )
    natal_chart = result.scalar_one_or_none()
    
    if not natal_chart:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Thème natal manquant. Calculez-le d'abord via POST /api/natal-chart"
        )
    
    if not current_user.birth_latitude or not current_user.birth_longitude:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Coordonnées de naissance manquantes"
        )
    
    # Extraire position natale de la Lune
    moon_data = natal_chart.planets.get("Moon", {})
    natal_moon_degree = moon_data.get("degree", 0)
    natal_moon_sign = natal_chart.moon_sign
    
    # Générer les 12 mois de l'année en cours
    current_year = datetime.now().year
    months = [f"{current_year}-{str(m).zfill(2)}" for m in range(1, 13)]
    
    generated_count = 0
    
    for month in months:
        # Vérifier si déjà calculé
        result = await db.execute(
            select(LunarReturn).where(
                LunarReturn.user_id == current_user.id,
                LunarReturn.month == month
            )
        )
        existing = result.scalar_one_or_none()
        
        if existing:
            continue  # Skip si déjà calculé
        
        # Calculer via Ephemeris API
        try:
            raw_data = await ephemeris_client.calculate_lunar_return(
                natal_moon_degree=natal_moon_degree,
                natal_moon_sign=natal_moon_sign,
                target_month=month,
                birth_latitude=float(current_user.birth_latitude),
                birth_longitude=float(current_user.birth_longitude),
                timezone=current_user.birth_timezone
            )
        except Exception as e:
            # Log l'erreur mais continue pour les autres mois
            print(f"❌ Erreur calcul révolution lunaire {month}: {e}")
            continue
        
        # Parser les données
        lunar_ascendant = raw_data.get("ascendant", {}).get("sign", "Unknown")
        moon_house = raw_data.get("moon", {}).get("house", 1)
        moon_sign = raw_data.get("moon", {}).get("sign", natal_moon_sign)
        aspects = raw_data.get("aspects", [])
        return_date = raw_data.get("return_datetime", f"{month}-15T12:00:00")
        
        # Générer l'interprétation
        interpretation = generate_lunar_return_interpretation(
            lunar_ascendant=lunar_ascendant,
            moon_house=moon_house,
            aspects=aspects
        )
        
        # Créer l'entrée
        lunar_return = LunarReturn(
            user_id=current_user.id,
            month=month,
            return_date=return_date,
            lunar_ascendant=lunar_ascendant,
            moon_house=moon_house,
            moon_sign=moon_sign,
            aspects=aspects,
            planets=raw_data.get("planets", {}),
            houses=raw_data.get("houses", {}),
            interpretation=interpretation,
            raw_data=raw_data
        )
        
        db.add(lunar_return)
        generated_count += 1
    
    await db.commit()
    
    return {
        "message": f"{generated_count} révolution(s) lunaire(s) générée(s)",
        "year": current_year
    }


@router.get("/", response_model=List[LunarReturnResponse])
async def get_all_lunar_returns(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Récupère toutes les révolutions lunaires de l'utilisateur"""
    
    result = await db.execute(
        select(LunarReturn)
        .where(LunarReturn.user_id == current_user.id)
        .order_by(LunarReturn.month)
    )
    returns = result.scalars().all()
    
    if not returns:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Aucune révolution lunaire calculée. Utilisez POST /api/lunar-returns/generate"
        )
    
    return returns


@router.get("/{month}", response_model=LunarReturnResponse)
async def get_lunar_return_by_month(
    month: str,  # Format: YYYY-MM
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Récupère une révolution lunaire spécifique par mois"""
    
    result = await db.execute(
        select(LunarReturn).where(
            LunarReturn.user_id == current_user.id,
            LunarReturn.month == month
        )
    )
    lunar_return = result.scalar_one_or_none()
    
    if not lunar_return:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Révolution lunaire pour {month} non trouvée"
        )
    
    return lunar_return

