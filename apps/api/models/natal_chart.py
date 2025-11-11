"""Modèle NatalChart"""

from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class NatalChart(Base):
    __tablename__ = "natal_charts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # Données calculées
    sun_sign = Column(String)  # Soleil
    moon_sign = Column(String)  # Lune
    ascendant = Column(String)  # Ascendant
    
    # Positions planètes (JSON)
    planets = Column(JSON)  # { "Sun": { "sign": "Taurus", "degree": 15.3, ... }, ... }
    houses = Column(JSON)    # { "1": { "sign": "Leo", "degree": 0 }, ... }
    aspects = Column(JSON)   # [ { "planet1": "Sun", "planet2": "Moon", "type": "trine", ... }, ... ]
    
    # Raw API response (debug/backup)
    raw_data = Column(JSON)
    
    # Metadata
    calculated_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relations
    user = relationship("User", back_populates="natal_chart")
    
    def __repr__(self):
        return f"<NatalChart user_id={self.user_id} sun={self.sun_sign} moon={self.moon_sign} asc={self.ascendant}>"

