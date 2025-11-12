"""
Schémas Pydantic pour le Calendrier Lunaire (P3)
"""

from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List
from datetime import date, datetime


class LunarPhasesRequest(BaseModel):
    """Requête pour obtenir les phases lunaires"""
    start_date: str = Field(..., description="Date de début (YYYY-MM-DD)")
    end_date: str = Field(..., description="Date de fin (YYYY-MM-DD)")
    latitude: Optional[float] = Field(None, description="Latitude (pour heure locale)")
    longitude: Optional[float] = Field(None, description="Longitude")
    timezone: Optional[str] = Field("Europe/Paris", description="Timezone")
    
    class Config:
        extra = "allow"


class LunarEventsRequest(BaseModel):
    """Requête pour obtenir les événements lunaires spéciaux"""
    start_date: str = Field(..., description="Date de début (YYYY-MM-DD)")
    end_date: str = Field(..., description="Date de fin (YYYY-MM-DD)")
    latitude: Optional[float] = Field(None, description="Latitude")
    longitude: Optional[float] = Field(None, description="Longitude")
    event_types: Optional[List[str]] = Field(None, description="Types d'événements à filtrer")
    
    class Config:
        extra = "allow"


class LunarCalendarYearRequest(BaseModel):
    """Requête pour obtenir le calendrier lunaire annuel"""
    year: int = Field(..., description="Année (ex: 2025)")
    latitude: Optional[float] = Field(None, description="Latitude")
    longitude: Optional[float] = Field(None, description="Longitude")
    timezone: Optional[str] = Field("Europe/Paris", description="Timezone")
    
    class Config:
        extra = "allow"


class MonthlyCalendarRequest(BaseModel):
    """Requête pour obtenir le calendrier mensuel combiné"""
    year: int = Field(..., description="Année (ex: 2025)")
    month: int = Field(..., description="Mois (1-12)", ge=1, le=12)
    latitude: Optional[float] = Field(48.8566, description="Latitude (Paris par défaut)")
    longitude: Optional[float] = Field(2.3522, description="Longitude")
    timezone: Optional[str] = Field("Europe/Paris", description="Timezone")


class CalendarDayInfo(BaseModel):
    """Information pour un jour du calendrier"""
    date: str
    day_of_week: str
    phases: List[str] = Field(default_factory=list)
    mansion: Optional[Dict[str, Any]] = None
    events: List[str] = Field(default_factory=list)
    lunar_day: Optional[int] = None


class MonthlyCalendarResponse(BaseModel):
    """Réponse du calendrier mensuel combiné"""
    year: int
    month: int
    days: List[CalendarDayInfo]
    summary: Dict[str, int]
    
    class Config:
        json_schema_extra = {
            "example": {
                "year": 2025,
                "month": 1,
                "days": [
                    {
                        "date": "2025-01-15",
                        "day_of_week": "Wednesday",
                        "phases": ["new_moon"],
                        "mansion": {"id": 7, "name": "Al-Dhira"},
                        "events": ["supermoon"],
                        "lunar_day": 1
                    }
                ],
                "summary": {
                    "new_moons": 1,
                    "full_moons": 1,
                    "eclipses": 0,
                    "special_events": 2
                }
            }
        }


class CalendarResponse(BaseModel):
    """Réponse standardisée pour les endpoints calendrier"""
    provider: str = Field(default="rapidapi")
    kind: str = Field(..., description="Type: lunar_phases, lunar_events, lunar_calendar_year")
    data: Dict[str, Any]
    cached: bool = Field(default=False)


class LunarEventDB(BaseModel):
    """Schéma pour les événements lunaires en DB"""
    id: int
    date: date
    time: Optional[str]
    event_type: str
    title: str
    description: Optional[str]
    meta: Optional[Dict[str, Any]]
    created_at: datetime
    
    class Config:
        from_attributes = True


class LunarPhaseDB(BaseModel):
    """Schéma pour les phases lunaires en DB"""
    id: int
    date: date
    time: str
    phase_type: str
    illumination: int
    meta: Optional[Dict[str, Any]]
    created_at: datetime
    
    class Config:
        from_attributes = True

