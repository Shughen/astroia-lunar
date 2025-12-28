"""Modèle NatalChart"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Time, Numeric
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
    
    # Données de naissance (NOT NULL selon schéma DB)
    birth_date = Column(Date, nullable=False)  # DATE en DB
    birth_time = Column(Time, nullable=False)  # TIME WITHOUT TIME ZONE en DB
    birth_place = Column(String, nullable=False)  # TEXT en DB
    latitude = Column(Numeric(9, 6), nullable=False)  # NUMERIC(9, 6) en DB
    longitude = Column(Numeric(9, 6), nullable=False)  # NUMERIC(9, 6) en DB
    timezone = Column(String, nullable=False)  # TEXT en DB (pas birth_timezone)
    
    # Données astrologiques (source de vérité : positions JSONB uniquement)
    # positions (JSONB) - contient toutes les données astrologiques :
    #   - Big3 (sun, moon, ascendant) directement
    #   - planets, houses, aspects dans des clés séparées
    positions = Column(JSONB, nullable=False)  # JSONB NOT NULL en DB
    
    # Metadata
    computed_at = Column(DateTime(timezone=True), server_default=func.now())  # computed_at (pas calculated_at)
    version = Column(String, server_default="v1-simplified")  # Version du schéma
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relations
    user = relationship("User", back_populates="natal_chart", foreign_keys=[user_id])
    
    def __repr__(self):
        return f"<NatalChart user_id={self.user_id} id={self.id} birth_date={self.birth_date}>"
