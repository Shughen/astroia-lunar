"""Route debug temporaire pour diagnostiquer le natal_chart"""

from fastapi import APIRouter, Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional

from database import get_db
from models.natal_chart import NatalChart
from models.user import User
from routes.auth import get_current_user

router = APIRouter()


@router.get("/debug/natal-chart")
async def debug_natal_chart(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Endpoint DEBUG pour vérifier le contenu exact du natal_chart
    """
    result = await db.execute(
        select(NatalChart).where(NatalChart.user_id == current_user.id)
    )
    natal_chart = result.scalar_one_or_none()

    if not natal_chart:
        return {"error": "Pas de natal_chart"}

    return {
        "id": str(natal_chart.id),
        "user_id": natal_chart.user_id,
        "birth_date": str(natal_chart.birth_date) if natal_chart.birth_date else None,
        "birth_time": str(natal_chart.birth_time) if natal_chart.birth_time else None,
        "birth_place": natal_chart.birth_place,
        "latitude": natal_chart.latitude,
        "latitude_type": str(type(natal_chart.latitude)),
        "latitude_is_none": natal_chart.latitude is None,
        "longitude": natal_chart.longitude,
        "longitude_type": str(type(natal_chart.longitude)),
        "longitude_is_none": natal_chart.longitude is None,
        "timezone": natal_chart.timezone,
        "timezone_type": str(type(natal_chart.timezone)),
        "timezone_is_none": natal_chart.timezone is None,
        "has_positions": bool(natal_chart.positions),
        "created_at": str(natal_chart.created_at),
        "updated_at": str(natal_chart.updated_at),
    }
