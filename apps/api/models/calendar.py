"""
Modèles SQLAlchemy pour le Calendrier Lunaire (P3)
- LunarEvent: Événements lunaires spéciaux (éclipses, superlunes, etc.)
- LunarPhase: Phases lunaires (nouvelles/pleines lunes, quartiers)
"""

from sqlalchemy import Column, Integer, String, DateTime, Date, Index, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from database import Base


class LunarEvent(Base):
    """
    Événement lunaire spécial (éclipse, superlune, microlune, etc.).
    Stocke les événements astronomiques remarquables.
    """
    __tablename__ = "lunar_events"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, index=True)  # Date de l'événement
    time = Column(String, nullable=True)  # Heure (HH:MM) si applicable
    event_type = Column(String, nullable=False, index=True)  # Type: eclipse, supermoon, etc.
    title = Column(String, nullable=False)  # Titre descriptif
    description = Column(Text, nullable=True)  # Description détaillée
    meta = Column(JSONB, nullable=True)  # Métadonnées (magnitude, visibilité, etc.)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Index pour recherches par date et type
    __table_args__ = (
        Index('ix_lunar_events_date_type', 'date', 'event_type'),
    )
    
    def __repr__(self):
        return f"<LunarEvent {self.event_type} on {self.date}>"


class LunarPhase(Base):
    """
    Phase lunaire (nouvelle lune, pleine lune, quartiers).
    Stocke les dates et heures exactes des phases principales.
    """
    __tablename__ = "lunar_phases"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, index=True)  # Date de la phase
    time = Column(String, nullable=False)  # Heure exacte (HH:MM:SS)
    phase_type = Column(String, nullable=False, index=True)  # new_moon, full_moon, first_quarter, last_quarter
    illumination = Column(Integer, nullable=False)  # Pourcentage * 100 (ex: 5000 = 50%)
    meta = Column(JSONB, nullable=True)  # Métadonnées (distance, magnitude, etc.)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Index composite pour requêtes optimisées
    __table_args__ = (
        Index('ix_lunar_phases_date_type', 'date', 'phase_type'),
    )
    
    def __repr__(self):
        return f"<LunarPhase {self.phase_type} on {self.date} at {self.time}>"

