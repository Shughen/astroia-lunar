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
    # Note: user_id supprimé pour sécurité - toujours utiliser l'utilisateur authentifié
    month: Optional[str] = Field(None, description="Mois au format YYYY-MM pour indexation")


class VoidOfCourseRequest(LunarRequestBase):
    """Requête spécifique pour Void of Course - Format FLAT"""

    class Config:
        json_schema_extra = {
            "example": {
                "date": "2025-12-31",
                "time": "12:00",
                "latitude": 48.8566,
                "longitude": 2.3522,
                "timezone": "Europe/Paris"
            }
        }


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


class LunarMansionRequest(LunarRequestBase):
    """Requête spécifique pour Lunar Mansions - Format FLAT (comme VoC)"""
    system: Optional[str] = Field(default="arabian_tropical", description="Système de mansions (arabian_tropical, vedic, etc.)")
    days_ahead: Optional[int] = Field(default=28, description="Nombre de jours à calculer")

    class Config:
        json_schema_extra = {
            "example": {
                "date": "2025-12-31",
                "time": "14:30",
                "latitude": 48.8566,
                "longitude": 2.3522,
                "timezone": "Europe/Paris",
                "system": "arabian_tropical",
                "days_ahead": 28
            }
        }


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
            "examples": [
                {
                    "provider": "rapidapi",
                    "kind": "lunar_return_report",
                    "data": {
                        "moon": {"sign": "Taurus", "house": 2},
                        "interpretation": "Mois favorable aux finances..."
                    },
                    "cached": False
                },
                {
                    "provider": "rapidapi",
                    "kind": "void_of_course",
                    "data": {
                        "is_void": True,
                        "void_of_course": {
                            "start": "2025-12-31T10:30:00",
                            "end": "2025-12-31T14:45:00"
                        },
                        "moon_sign": "Gemini"
                    },
                    "cached": False
                },
                {
                    "provider": "rapidapi",
                    "kind": "lunar_mansion",
                    "data": {
                        "mansion": {
                            "number": 14,
                            "name": "Al-Simak",
                            "interpretation": "Favorable aux nouveaux projets"
                        },
                        "upcoming_changes": [
                            {
                                "change_time": "2025-12-31T15:30:00",
                                "from_mansion": {"number": 14, "name": "Al-Simak"},
                                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
                            }
                        ],
                        "calendar_summary": {
                            "significant_periods": [
                                {
                                    "change_time": "2025-12-31T15:30:00",
                                    "from_mansion": {"number": 14, "name": "Al-Simak"},
                                    "to_mansion": {"number": 15, "name": "Al-Ghafr"}
                                }
                            ]
                        }
                    },
                    "cached": False
                }
            ]
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


class RegenerateInterpretationRequest(BaseModel):
    """Requête pour forcer la régénération d'une interprétation lunaire"""
    lunar_return_id: int = Field(..., description="ID de la révolution lunaire")
    subject: str = Field(default='full', description="Type d'interprétation (full, climate, focus, approach)")

    class Config:
        json_schema_extra = {
            "example": {
                "lunar_return_id": 123,
                "subject": "full"
            }
        }


class InterpretationMetadata(BaseModel):
    """Métadonnées d'une interprétation générée"""
    source: str = Field(..., description="Source: db_temporal, claude, db_template, hardcoded")
    model_used: Optional[str] = Field(None, description="Modèle utilisé (ex: claude-opus-4-5)")
    subject: str = Field(..., description="Type d'interprétation")
    regenerated_at: str = Field(..., description="Timestamp de régénération (ISO 8601)")
    forced: bool = Field(..., description="True si régénération forcée")


class RegenerateInterpretationResponse(BaseModel):
    """Réponse après régénération d'une interprétation"""
    interpretation: str = Field(..., description="Texte de l'interprétation générée")
    weekly_advice: Optional[Dict[str, Any]] = Field(None, description="Conseils hebdomadaires structurés")
    metadata: InterpretationMetadata = Field(..., description="Métadonnées de génération")

