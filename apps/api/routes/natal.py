"""Routes pour thème natal"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional, Dict, Any
import httpx

from database import get_db
from models.user import User
from models.natal_chart import NatalChart
from routes.auth import get_current_user
from services.ephemeris import ephemeris_client
from services.ephemeris_rapidapi import create_natal_chart

router = APIRouter()


# === SCHEMAS ===
class NatalChartRequest(BaseModel):
    date: str  # YYYY-MM-DD
    time: str  # HH:MM
    latitude: float
    longitude: float
    place_name: str
    timezone: str = "Europe/Paris"


class NatalChartResponse(BaseModel):
    id: int
    sun_sign: str
    moon_sign: str
    ascendant: str
    planets: dict
    houses: dict
    aspects: list


# === ROUTES ===
@router.post("/natal-chart", response_model=NatalChartResponse, status_code=status.HTTP_201_CREATED)
async def calculate_natal_chart(
    data: NatalChartRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Calcule le thème natal et le sauvegarde
    Si un thème existe déjà, il sera écrasé
    """
    
    # Calculer via Ephemeris API
    try:
        raw_data = await ephemeris_client.calculate_natal_chart(
            date=data.date,
            time=data.time,
            latitude=data.latitude,
            longitude=data.longitude,
            timezone=data.timezone
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur calcul thème natal: {str(e)}"
        )
    
    # Parser les données (adapter selon la réponse réelle de l'API)
    sun_sign = raw_data.get("sun", {}).get("sign", "Unknown")
    moon_sign = raw_data.get("moon", {}).get("sign", "Unknown")
    ascendant = raw_data.get("ascendant", {}).get("sign", "Unknown")
    
    # Vérifier si un thème existe déjà
    result = await db.execute(
        select(NatalChart).where(NatalChart.user_id == current_user.id)
    )
    existing_chart = result.scalar_one_or_none()
    
    if existing_chart:
        # Mise à jour
        existing_chart.sun_sign = sun_sign
        existing_chart.moon_sign = moon_sign
        existing_chart.ascendant = ascendant
        existing_chart.planets = raw_data.get("planets", {})
        existing_chart.houses = raw_data.get("houses", {})
        existing_chart.aspects = raw_data.get("aspects", [])
        existing_chart.raw_data = raw_data
        chart = existing_chart
    else:
        # Création
        chart = NatalChart(
            user_id=current_user.id,
            sun_sign=sun_sign,
            moon_sign=moon_sign,
            ascendant=ascendant,
            planets=raw_data.get("planets", {}),
            houses=raw_data.get("houses", {}),
            aspects=raw_data.get("aspects", []),
            raw_data=raw_data
        )
        db.add(chart)
    
    # Mettre à jour les infos de naissance du user
    current_user.birth_date = data.date
    current_user.birth_time = data.time
    current_user.birth_latitude = str(data.latitude)
    current_user.birth_longitude = str(data.longitude)
    current_user.birth_place_name = data.place_name
    current_user.birth_timezone = data.timezone
    
    await db.commit()
    await db.refresh(chart)
    
    return chart


@router.get("/natal-chart", response_model=NatalChartResponse)
async def get_natal_chart(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Récupère le thème natal de l'utilisateur"""
    
    result = await db.execute(
        select(NatalChart).where(NatalChart.user_id == current_user.id)
    )
    chart = result.scalar_one_or_none()
    
    if not chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thème natal non calculé. Utilisez POST /api/natal-chart d'abord."
        )
    
    return chart


# === RAPIDAPI PASS-THROUGH ===
@router.post("/natal-chart/external")
async def calculate_natal_chart_external(
    payload: Dict[str, Any]
):
    """
    Endpoint pass-through vers RapidAPI pour calculer un thème natal.
    Accepte n'importe quel payload JSON et le transmet directement à RapidAPI.
    
    Exemple de payload:
    {
        "name": "John Doe",
        "date": "1990-05-15",
        "time": "14:30",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }
    """
    try:
        # Appel à RapidAPI via le service
        rapidapi_response = await create_natal_chart(payload)
        
        # Retour structuré
        return {
            "provider": "rapidapi",
            "endpoint": "chart_natal",
            "data": rapidapi_response
        }
        
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Ephemeris error: {e.response.status_code} - {e.response.text}"
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Ephemeris error: Unable to connect - {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ephemeris error: {str(e)}"
        )

