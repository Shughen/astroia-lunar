"""
Schémas Pydantic pour les interprétations de thème natal
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime


# Types pour les objets célestes supportés
NatalSubject = Literal[
    'sun', 'moon', 'ascendant', 'midheaven',
    'mercury', 'venus', 'mars', 'jupiter', 'saturn',
    'uranus', 'neptune', 'pluto',
    'chiron', 'north_node', 'south_node', 'lilith'
]


class ChartPayload(BaseModel):
    """Données d'entrée pour générer une interprétation"""
    subject_label: str = Field(..., description="Nom français de l'objet (ex: 'Soleil', 'Lune')")
    sign: str = Field(..., description="Signe zodiacal en français (ex: 'Bélier', 'Taureau')")
    degree: Optional[float] = Field(None, description="Degré dans le signe (0-30)")
    house: Optional[int] = Field(None, description="Numéro de maison (1-12)")
    ascendant_sign: Optional[str] = Field(None, description="Signe de l'Ascendant (contexte global)")
    aspects: Optional[list] = Field(None, description="Liste des aspects majeurs (max 1 utilisé si orb <= 3°)")


class NatalInterpretationRequest(BaseModel):
    """Request pour générer ou récupérer une interprétation"""
    chart_id: str = Field(..., description="ID stable du thème natal (hash)")
    subject: NatalSubject = Field(..., description="Objet céleste à interpréter")
    lang: str = Field(default='fr', description="Langue de l'interprétation")
    chart_payload: ChartPayload = Field(..., description="Données du chart pour génération")
    force_refresh: bool = Field(default=False, description="Forcer la régénération même si cache existe")


class NatalInterpretationResponse(BaseModel):
    """Response contenant l'interprétation"""
    id: Optional[str] = Field(None, description="ID de l'interprétation en base")
    text: str = Field(..., description="Texte de l'interprétation (markdown)")
    cached: bool = Field(..., description="True si provient du cache, False si nouvellement généré")
    subject: NatalSubject = Field(..., description="Objet céleste interprété")
    chart_id: str = Field(..., description="ID du thème natal")
    version: int = Field(default=1, description="Version du prompt utilisé")
    created_at: Optional[datetime] = Field(None, description="Date de création")

    class Config:
        from_attributes = True
