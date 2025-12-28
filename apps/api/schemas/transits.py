"""
Schémas Pydantic pour les Transits (P2)
Validation des requêtes et réponses des endpoints transits
"""

from pydantic import BaseModel, Field, model_serializer
from typing import Dict, Any, Optional, List
from datetime import date, datetime
from uuid import UUID


class NatalTransitsRequest(BaseModel):
    """Requête pour calculer les transits sur le thème natal"""
    birth_date: str = Field(..., description="Date de naissance (YYYY-MM-DD)")
    birth_time: str = Field(..., description="Heure de naissance (HH:MM)")
    birth_latitude: float = Field(..., description="Latitude du lieu de naissance")
    birth_longitude: float = Field(..., description="Longitude du lieu de naissance")
    birth_timezone: str = Field(default="Europe/Paris", description="Timezone de naissance")
    
    transit_date: str = Field(..., description="Date du transit (YYYY-MM-DD)")
    transit_time: Optional[str] = Field(None, description="Heure du transit (HH:MM)")
    orb: Optional[float] = Field(5.0, description="Orbe des aspects en degrés")
    
    user_id: Optional[UUID] = Field(None, description="ID utilisateur (UUID) pour sauvegarde en DB")
    
    class Config:
        extra = "allow"


class LunarReturnTransitsRequest(BaseModel):
    """Requête pour calculer les transits sur une révolution lunaire"""
    birth_date: str = Field(..., description="Date de naissance (YYYY-MM-DD)")
    birth_time: str = Field(..., description="Heure de naissance (HH:MM)")
    birth_latitude: float = Field(..., description="Latitude du lieu de naissance")
    birth_longitude: float = Field(..., description="Longitude du lieu de naissance")
    birth_timezone: str = Field(default="Europe/Paris", description="Timezone de naissance")
    
    lunar_return_date: str = Field(..., description="Date de la révolution lunaire (YYYY-MM-DD)")
    transit_date: str = Field(..., description="Date du transit actuel (YYYY-MM-DD)")
    orb: Optional[float] = Field(5.0, description="Orbe des aspects en degrés")
    
    user_id: Optional[UUID] = Field(None, description="ID utilisateur (UUID) pour sauvegarde en DB")
    month: Optional[str] = Field(None, description="Mois au format YYYY-MM")
    
    class Config:
        extra = "allow"


class AspectInfo(BaseModel):
    """Information sur un aspect de transit"""
    transit_planet: str
    natal_planet: str
    aspect: str
    orb: float
    interpretation: Optional[str] = None


class TransitsInsights(BaseModel):
    """Insights générés à partir des transits"""
    insights: List[str] = Field(default_factory=list, description="3-5 bullet points clés")
    major_aspects: List[AspectInfo] = Field(default_factory=list, description="Aspects majeurs")
    energy_level: str = Field(default="medium", description="Niveau d'énergie: low, medium, high")
    themes: List[str] = Field(default_factory=list, description="Thèmes principaux du mois")


class TransitsResponse(BaseModel):
    """Réponse standardisée pour les endpoints transits"""
    provider: str = Field(default="rapidapi", description="Source des données")
    kind: str = Field(..., description="Type: natal_transits ou lunar_return_transits")
    data: Dict[str, Any] = Field(..., description="Données brutes du provider")
    insights: Optional[TransitsInsights] = Field(None, description="Insights générés")
    cached: bool = Field(default=False, description="Données du cache DB")
    
    class Config:
        json_schema_extra = {
            "example": {
                "provider": "rapidapi",
                "kind": "natal_transits",
                "data": {
                    "aspects": [
                        {
                            "planet1": "Jupiter",
                            "planet2": "Sun",
                            "aspect": "trine",
                            "orb": 1.2
                        }
                    ]
                },
                "insights": {
                    "insights": ["Jupiter forme un trigone avec votre Soleil natal"],
                    "major_aspects": [],
                    "energy_level": "high",
                    "themes": ["expansion", "optimisme"]
                },
                "cached": False
            }
        }


class TransitsOverviewDB(BaseModel):
    """Schéma pour les transits overview en DB"""
    id: int
    user_id: UUID
    month: str
    overview: Dict[str, Any]
    created_at: datetime
    
    class Config:
        from_attributes = True
    
    @model_serializer(mode='wrap')
    def serialize_model(self, serializer, info):
        """
        Sérialise le modèle en incluant 'overview' et 'summary' (alias pour compatibilité).
        """
        data = serializer(self)
        data['summary'] = data['overview']  # Alias de compatibilité pour le mobile
        return data


class TransitsEventDB(BaseModel):
    """Schéma pour les événements de transit en DB"""
    id: int
    user_id: UUID
    date: date
    transit_planet: str
    natal_point: str
    aspect_type: str
    orb: int
    interpretation: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

