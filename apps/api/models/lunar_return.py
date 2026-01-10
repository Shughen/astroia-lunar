"""Modèle LunarReturn (révolution lunaire)"""

from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class LunarReturn(Base):
    __tablename__ = "lunar_returns"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Période
    month = Column(String, nullable=False, index=True)  # YYYY-MM (legacy, pour compatibilité)
    return_date = Column(DateTime(timezone=True), nullable=False, index=True)  # Date exacte de la révolution lunaire (timestamptz, UTC, NOT NULL, indexé)
    
    # Données calculées
    lunar_ascendant = Column(String)  # Ascendant de la révolution lunaire
    moon_house = Column(Integer)       # Maison de la Lune
    moon_sign = Column(String)         # Signe de la Lune
    
    # Aspects et positions (JSON)
    aspects = Column(JSON)    # Aspects majeurs de la Lune
    planets = Column(JSON)    # Positions des planètes à la révolution
    houses = Column(JSON)     # Cuspides des maisons
    
    # Interprétation textuelle (générée)
    interpretation = Column(String)
    
    # Raw API response
    raw_data = Column(JSON)
    
    # Metadata
    calculated_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relations
    user = relationship("User", back_populates="lunar_returns")
    
    def __repr__(self):
        return f"<LunarReturn user_id={self.user_id} month={self.month} asc={self.lunar_ascendant}>"

