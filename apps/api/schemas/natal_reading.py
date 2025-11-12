"""Schemas Pydantic pour NatalReading"""

from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime


# === INPUT SCHEMAS ===

class BirthData(BaseModel):
    """Données de naissance"""
    year: int = Field(..., ge=1900, le=2100)
    month: int = Field(..., ge=1, le=12)
    day: int = Field(..., ge=1, le=31)
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)
    second: int = Field(default=0, ge=0, le=59)
    city: str
    country_code: str = Field(default="FR", min_length=2, max_length=2)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    timezone: str = Field(default="Europe/Paris")


class NatalReadingOptions(BaseModel):
    """Options pour la génération du thème"""
    language: str = Field(default="fr")
    house_system: str = Field(default="P")  # Placidus
    tradition: str = Field(default="psychological")
    detail_level: str = Field(default="detailed")
    include_full_report: bool = Field(default=False)
    force_refresh: bool = Field(default=False, description="Bypass cache et force un nouvel appel API")


class NatalReadingRequest(BaseModel):
    """Request pour générer une lecture de thème natal"""
    birth_data: BirthData
    options: Optional[NatalReadingOptions] = None


# === OUTPUT SCHEMAS ===

class CorePointInterpretation(BaseModel):
    """Interprétations d'un point astrologique"""
    in_sign: Optional[str] = None
    in_house: Optional[str] = None
    dignity: Optional[str] = None


class CorePoint(BaseModel):
    """Point astrologique principal (planète, ascendant, etc.)"""
    name: str
    sign: str  # Abréviation: "Sco", "Sag", etc.
    sign_fr: str  # Nom français: "Scorpion", "Sagittaire"
    degree: float  # Position dans le signe (0-30)
    house: int  # Maison (1-12)
    is_retrograde: bool
    emoji: str
    element: str  # "Feu", "Terre", "Air", "Eau"
    interpretations: CorePointInterpretation


class Aspect(BaseModel):
    """Aspect entre deux points"""
    from_point: str = Field(..., alias="from")
    to_point: str = Field(..., alias="to")
    aspect_type: str  # "conjunction", "trine", "square", etc.
    orb: float
    strength: Literal["weak", "medium", "strong"]
    interpretation: Optional[str] = None


class LunarInfo(BaseModel):
    """Informations lunaires à la naissance"""
    phase: str
    phase_angle: Optional[float] = None
    lunar_day: Optional[int] = None
    mansion: Optional[str] = None
    void_of_course: Optional[bool] = None
    interpretation: Optional[str] = None
    emoji: Optional[str] = None


class NatalSummary(BaseModel):
    """Résumé du thème"""
    big_three: dict  # { "sun": CorePoint, "moon": CorePoint, "ascendant": CorePoint }
    personality_highlights: List[str]
    dominant_element: Optional[str] = None
    dominant_mode: Optional[str] = None


class NatalReadingResponse(BaseModel):
    """Réponse complète d'une lecture de thème natal"""
    id: int
    subject_name: Optional[str] = None
    birth_data: BirthData
    positions: List[CorePoint]
    aspects: List[Aspect]
    lunar: LunarInfo
    summary: NatalSummary
    full_report_text: Optional[str] = None
    source: Literal["api", "cache"]
    api_calls_count: int
    created_at: datetime
    last_accessed_at: datetime
    
    class Config:
        from_attributes = True

