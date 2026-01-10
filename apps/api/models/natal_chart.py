"""Modèle NatalChart"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class NatalChart(Base):
    __tablename__ = "natal_charts"
    
    # PK: UUID (généré par la DB avec gen_random_uuid())
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid(), index=True)
    
    # FK vers users.id (INTEGER) avec CASCADE
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    
    # Note: Les données de naissance (birth_date, birth_time, latitude, longitude, timezone)
    # sont stockées dans la table users, pas dans natal_charts.
    # Le schéma DB réel (inspecté) contient: user_id, sun_sign, moon_sign, ascendant, planets, houses, 
    # aspects, raw_data, calculated_at, id, positions
    
    # Colonnes legacy (existent en DB mais peuvent être NULL)
    sun_sign = Column(String, nullable=True)
    moon_sign = Column(String, nullable=True)
    ascendant = Column(String, nullable=True)
    planets = Column(JSON, nullable=True)  # JSON (pas JSONB)
    houses = Column(JSON, nullable=True)  # JSON (pas JSONB)
    aspects = Column(JSON, nullable=True)  # JSON (pas JSONB)
    raw_data = Column(JSON, nullable=True)  # JSON (pas JSONB)
    
    # Données astrologiques (source de vérité : positions JSONB)
    # positions (JSONB) - contient toutes les données astrologiques :
    #   - Big3 (sun, moon, ascendant) directement
    #   - planets, houses, aspects dans des clés séparées
    # Note: nullable=True temporairement pour permettre migration depuis raw_data
    # Après migration complète, peut être rendu NOT NULL
    positions = Column(JSONB, nullable=True)  # JSONB nullable (sera NOT NULL après migration)
    
    # Metadata
    # Note: La DB utilise calculated_at, pas computed_at
    calculated_at = Column(DateTime(timezone=True), server_default=func.now())  # calculated_at en DB
    
    # Relations
    user = relationship("User", back_populates="natal_chart", foreign_keys=[user_id])
    
    def __repr__(self):
        return f"<NatalChart user_id={self.user_id} id={self.id}>"
