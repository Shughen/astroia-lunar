"""Schemas Pydantic pour LunarReturn (révolutions lunaires)"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Union
from datetime import datetime
from uuid import UUID


# === INPUT SCHEMAS ===

class LunarReturnGenerateRequest(BaseModel):
    """Request pour générer une révolution lunaire"""
    cycle_number: int = Field(..., ge=1, description="Numéro du cycle (1, 2, 3, ...)")
    user_id: Union[UUID, int] = Field(..., description="ID de l'utilisateur (UUID ou int)")


class UserProfileForLunarReturn(BaseModel):
    """Profil utilisateur nécessaire pour calculer une révolution lunaire"""
    birth_date: datetime
    birth_time: Optional[datetime] = None
    birth_place: str
    latitude: float
    longitude: float
    timezone: str = Field(default="Europe/Paris")


# === OUTPUT SCHEMAS ===

class PlanetPosition(BaseModel):
    """Position d'une planète"""
    name: str
    sign: str
    sign_fr: Optional[str] = None
    degree: float
    house: Optional[int] = None
    is_retrograde: bool = False


class Aspect(BaseModel):
    """Aspect astrologique"""
    from_planet: str
    to_planet: str
    aspect_type: str
    orb: float
    strength: Optional[str] = None


class LunarReturnBase(BaseModel):
    """Base schema pour LunarReturn"""
    cycle_number: int
    start_date: datetime
    end_date: datetime
    moon_sign: Optional[str] = None
    moon_degree: Optional[float] = None
    moon_house: Optional[int] = None
    ascendant_sign: Optional[str] = None
    ascendant_degree: Optional[float] = None
    sun_sign: Optional[str] = None
    sun_degree: Optional[float] = None


class LunarReturnCreate(LunarReturnBase):
    """Schema pour créer une LunarReturn (avec computed data)"""
    user_id: UUID
    planet_positions: Optional[Dict[str, Any]] = None
    aspects: Optional[List[Dict[str, Any]]] = None
    interpretation_keys: Optional[Dict[str, Any]] = None


class LunarReturnDB(LunarReturnBase):
    """Schema complet depuis la DB Supabase"""
    id: UUID
    user_id: UUID
    planet_positions: Optional[Dict[str, Any]] = None
    aspects: Optional[List[Dict[str, Any]]] = None
    interpretation_keys: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class LunarReturnResponse(BaseModel):
    """Response pour une révolution lunaire"""
    id: UUID
    user_id: UUID
    cycle_number: int
    start_date: datetime
    end_date: datetime
    moon_sign: Optional[str] = None
    moon_degree: Optional[float] = None
    moon_house: Optional[int] = None
    ascendant_sign: Optional[str] = None
    ascendant_degree: Optional[float] = None
    sun_sign: Optional[str] = None
    sun_degree: Optional[float] = None
    planet_positions: Optional[Dict[str, Any]] = None
    aspects: Optional[List[Dict[str, Any]]] = None
    interpretation_keys: Optional[Dict[str, Any]] = None
    created_at: datetime
    updated_at: datetime

