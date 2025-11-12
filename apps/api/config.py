"""
Configuration centralisée (Pydantic Settings)
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    """Configuration app via .env"""
    
    # Database
    DATABASE_URL: str = Field(default="postgresql://user:password@localhost:5432/astroia_lunar")
    DATABASE_POOL_SIZE: int = Field(default=10)
    DATABASE_MAX_OVERFLOW: int = Field(default=20)
    
    # Ephemeris API (legacy)
    EPHEMERIS_API_KEY: str = Field(default="")
    EPHEMERIS_API_URL: str = Field(default="https://api.astrology-api.io/v1")
    
    # RapidAPI - Best Astrology API
    RAPIDAPI_KEY: str = Field(default="")
    RAPIDAPI_HOST: str = Field(default="best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com")
    BASE_RAPID_URL: str = Field(default="https://best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com")
    NATAL_URL: str = Field(default="https://best-astrology-api-natal-charts-transits-synastry.p.rapidapi.com/api/v3/charts/natal")
    
    # Luna Pack endpoints (P1) - VRAIS CHEMINS VALIDÉS
    LUNAR_RETURN_REPORT_PATH: str = Field(default="/api/v3/analysis/lunar-return-report")
    VOID_OF_COURSE_PATH: str = Field(default="/api/v3/lunar/void-of-course")
    LUNAR_MANSIONS_PATH: str = Field(default="/api/v3/lunar/mansions")
    
    # Transits endpoints (P2) - VRAIS CHEMINS VALIDÉS
    NATAL_TRANSITS_PATH: str = Field(default="/api/v3/charts/natal-transits")
    LUNAR_RETURN_TRANSITS_PATH: str = Field(default="/api/v3/charts/natal-transits")  # Même endpoint
    
    # Calendar endpoints (P3) - VRAIS CHEMINS VALIDÉS
    LUNAR_PHASES_PATH: str = Field(default="/api/v3/lunar/phases")
    LUNAR_EVENTS_PATH: str = Field(default="/api/v3/lunar/events")
    LUNAR_CALENDAR_YEAR_PATH: str = Field(default="/api/v3/lunar/calendar")
    
    # API
    API_HOST: str = Field(default="0.0.0.0")
    API_PORT: int = Field(default=8000)
    API_RELOAD: bool = Field(default=True)
    APP_ENV: str = Field(default="development")
    
    # JWT
    SECRET_KEY: str = Field(default="dev-secret-key-change-in-production")
    ALGORITHM: str = Field(default="HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=10080)  # 7 jours
    
    # Frontend
    FRONTEND_URL: str = Field(default="http://localhost:8081")
    
    # Timezone
    TZ: str = Field(default="Europe/Paris")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

