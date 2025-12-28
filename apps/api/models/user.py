"""Modèle User"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship, foreign
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Données de naissance
    birth_date = Column(String, nullable=True)  # YYYY-MM-DD
    birth_time = Column(String, nullable=True)  # HH:MM
    birth_latitude = Column(String, nullable=True)
    birth_longitude = Column(String, nullable=True)
    birth_place_name = Column(String, nullable=True)
    birth_timezone = Column(String, default="Europe/Paris")
    
    # Metadata
    is_active = Column(Boolean, default=True)
    is_premium = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    natal_chart = relationship(
        "NatalChart",
        back_populates="user",
        uselist=False,
        foreign_keys="[NatalChart.user_id]"
    )
    lunar_returns = relationship("LunarReturn", back_populates="user", cascade="all, delete-orphan")
    lunar_reports = relationship("LunarReport", back_populates="user", cascade="all, delete-orphan")
    # Note: transits_overviews et transits_events ne sont plus en relation car
    # user_id pointe vers auth.users.id (UUID Supabase) et non vers users.id (Integer FastAPI)
    # Les RLS policies gèrent l'accès basé sur auth.uid()
    
    def __repr__(self):
        return f"<User {self.email}>"

