"""
Modèles SQLAlchemy pour les Transits (P2)
- TransitsOverview: Vue d'ensemble des transits par mois/utilisateur
- TransitsEvent: Aspects clés et événements de transit
"""

from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Index, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class TransitsOverview(Base):
    """
    Vue d'ensemble des transits pour un utilisateur et un mois donné.
    Stocke un résumé et les aspects majeurs du mois.
    """
    __tablename__ = "transits_overview"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    month = Column(String, nullable=False, index=True)  # Format: YYYY-MM
    summary = Column(JSONB, nullable=False)  # Résumé avec insights
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relation vers User
    user = relationship("User", back_populates="transits_overviews")
    
    # Index composite pour requêtes optimisées
    __table_args__ = (
        Index('ix_transits_overview_user_month', 'user_id', 'month'),
    )
    
    def __repr__(self):
        return f"<TransitsOverview user_id={self.user_id} month={self.month}>"


class TransitsEvent(Base):
    """
    Événement de transit significatif (aspect majeur).
    Stocke les aspects clés entre planètes en transit et positions natales.
    """
    __tablename__ = "transits_events"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False, index=True)  # Date de l'aspect exact
    transit_planet = Column(String, nullable=False)   # Ex: "Jupiter"
    natal_point = Column(String, nullable=False)      # Ex: "Sun", "MC", "Ascendant"
    aspect_type = Column(String, nullable=False)      # Ex: "trine", "square", "conjunction"
    orb = Column(Integer, nullable=False)             # Orbe en degrés * 100 (ex: 150 = 1.5°)
    interpretation = Column(Text, nullable=True)      # Interprétation textuelle
    raw_data = Column(JSONB, nullable=True)          # Données brutes du provider
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relation vers User
    user = relationship("User", back_populates="transits_events")
    
    # Index composite pour requêtes optimisées
    __table_args__ = (
        Index('ix_transits_events_user_date', 'user_id', 'date'),
        Index('ix_transits_events_planet_aspect', 'transit_planet', 'aspect_type'),
    )
    
    def __repr__(self):
        return f"<TransitsEvent {self.transit_planet} {self.aspect_type} {self.natal_point} on {self.date}>"

