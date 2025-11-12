"""
Schémas Pydantic pour le Luna Pack
Validation des requêtes et réponses des endpoints lunaires
"""

from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import date, datetime


class LunarRequestBase(BaseModel):
    """
    Schéma de base pour les requêtes lunaires.
    Les payloads RapidAPI varient, on garde une structure flexible.
    """
    date: Optional[str] = Field(None, description="Date au format YYYY-MM-DD")
    time: Optional[str] = Field(None, description="Heure au format HH:MM")
    latitude: Optional[float] = Field(None, description="Latitude du lieu")
    longitude: Optional[float] = Field(None, description="Longitude du lieu")
    timezone: Optional[str] = Field(None, description="Fuseau horaire (ex: Europe/Paris)")
    
    # Champs additionnels pour flexibilité
    birth_date: Optional[str] = None
    birth_time: Optional[str] = None
    
    # Permet d'accepter d'autres champs non définis
    class Config:
        extra = "allow"


class LunarReturnReportRequest(LunarRequestBase):
    """Requête spécifique pour le Lunar Return Report"""
    user_id: Optional[int] = Field(None, description="ID utilisateur pour sauvegarde en DB")
    month: Optional[str] = Field(None, description="Mois au format YYYY-MM pour indexation")


class VoidOfCourseRequest(LunarRequestBase):
    """Requête spécifique pour Void of Course"""
    pass


class DateTimeLocation(BaseModel):
    """Objet datetime_location pour RapidAPI"""
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int = Field(default=0)
    city: str = Field(default="Paris")
    country_code: str = Field(default="FR")


class LunarMansionRequest(BaseModel):
    """Requête spécifique pour Lunar Mansions - Format RapidAPI"""
    datetime_location: DateTimeLocation
    system: str = Field(default="arabian_tropical", description="Système de mansions (arabian_tropical, vedic, etc.)")
    days_ahead: int = Field(default=28, description="Nombre de jours à calculer")


class LunarResponse(BaseModel):
    """
    Réponse standardisée pour tous les endpoints lunaires.
    Encapsule la réponse du provider avec métadonnées.
    """
    provider: str = Field(default="rapidapi", description="Source des données")
    kind: str = Field(..., description="Type de données: lunar_return_report, void_of_course, lunar_mansion")
    data: Dict[str, Any] = Field(..., description="Données brutes du provider")
    cached: bool = Field(default=False, description="Données provenant du cache DB")
    
    class Config:
        json_schema_extra = {
            "example": {
                "provider": "rapidapi",
                "kind": "lunar_return_report",
                "data": {
                    "moon": {"sign": "Taurus", "house": 2},
                    "interpretation": "Mois favorable aux finances..."
                },
                "cached": False
            }
        }


class LunarReportDB(BaseModel):
    """Schéma pour les rapports lunaires en DB"""
    id: int
    user_id: int
    month: str
    report: Dict[str, Any]
    created_at: datetime
    
    class Config:
        from_attributes = True


class LunarVocWindowDB(BaseModel):
    """Schéma pour les fenêtres VoC en DB"""
    id: int
    start_at: datetime
    end_at: datetime
    source: Dict[str, Any]
    created_at: datetime
    
    class Config:
        from_attributes = True


class LunarMansionDB(BaseModel):
    """Schéma pour les mansions lunaires en DB"""
    id: int
    date: date
    mansion_id: int
    data: Dict[str, Any]
    created_at: datetime
    
    class Config:
        from_attributes = True

