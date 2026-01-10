"""Modèle NatalReading pour stocker les lectures complètes de thèmes natals"""

from sqlalchemy import Column, Integer, String, JSON, DateTime, Boolean, Index
from sqlalchemy.sql import func
from database import Base


class NatalReading(Base):
    """
    Stockage des lectures complètes de thèmes natals
    Évite de rappeler l'API pour les mêmes données de naissance
    """
    __tablename__ = "natal_readings"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Clé de cache unique basée sur les données de naissance
    cache_key = Column(String, unique=True, nullable=False, index=True)
    
    # Données de naissance (JSON)
    birth_data = Column(JSON, nullable=False)
    # {
    #   "year": 1989,
    #   "month": 11,
    #   "day": 1,
    #   "hour": 13,
    #   "minute": 20,
    #   "second": 0,
    #   "city": "Manaus",
    #   "country_code": "BR",
    #   "latitude": -3.1316,
    #   "longitude": -59.9825,
    #   "timezone": "America/Manaus"
    # }
    
    # Lecture complète (JSONB)
    reading = Column(JSON, nullable=False)
    # {
    #   "positions": [...],
    #   "aspects": [...],
    #   "lunar": {...},
    #   "summary": {...},
    #   "fullReportText": "..."
    # }
    
    # Métadonnées
    source = Column(String, default="api")  # "api" ou "cache"
    api_calls_count = Column(Integer, default=0)  # Nombre d'appels API utilisés
    language = Column(String, default="fr")
    
    # Flags
    includes_full_report = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_accessed_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Indexes pour performance
    __table_args__ = (
        Index('ix_natal_readings_cache_key', 'cache_key'),
        Index('ix_natal_readings_created_at', 'created_at'),
    )
    
    def __repr__(self):
        return f"<NatalReading cache_key={self.cache_key} calls={self.api_calls_count}>"

