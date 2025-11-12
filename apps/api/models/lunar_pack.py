"""
Modèles SQLAlchemy pour le Luna Pack (P1)
- Lunar Return Reports
- Void of Course Windows  
- Lunar Mansions Daily
"""

from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, Index
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class LunarReport(Base):
    """
    Rapport mensuel de révolution lunaire généré par l'API.
    Stocke le rapport complet prêt à afficher.
    """
    __tablename__ = "lunar_reports"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    month = Column(String, nullable=False, index=True)  # Format: YYYY-MM
    report = Column(JSONB, nullable=False)  # Réponse brute du provider
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relation vers User
    user = relationship("User", back_populates="lunar_reports")
    
    # Index composite pour requêtes optimisées
    __table_args__ = (
        Index('ix_lunar_reports_user_month', 'user_id', 'month'),
    )
    
    def __repr__(self):
        return f"<LunarReport user_id={self.user_id} month={self.month}>"


class LunarVocWindow(Base):
    """
    Fenêtre Void of Course (VoC) de la Lune.
    Période où la Lune ne fait plus d'aspects majeurs avant de changer de signe.
    """
    __tablename__ = "lunar_voc_windows"
    
    id = Column(Integer, primary_key=True, index=True)
    start_at = Column(DateTime(timezone=True), nullable=False, index=True)
    end_at = Column(DateTime(timezone=True), nullable=False, index=True)
    source = Column(JSONB, nullable=False)  # Données brutes du provider
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Index pour rechercher les fenêtres actives
    __table_args__ = (
        Index('ix_lunar_voc_windows_range', 'start_at', 'end_at'),
    )
    
    def __repr__(self):
        return f"<LunarVocWindow {self.start_at} -> {self.end_at}>"


class LunarMansionDaily(Base):
    """
    Mansion lunaire du jour (système des 28 mansions).
    Une mansion par jour, avec interprétation associée.
    """
    __tablename__ = "lunar_mansions_daily"
    
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, unique=True, index=True)  # Date du jour
    mansion_id = Column(Integer, nullable=False)  # Numéro de la mansion (1-28)
    data = Column(JSONB, nullable=False)  # Données complètes du provider
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<LunarMansionDaily date={self.date} mansion={self.mansion_id}>"

