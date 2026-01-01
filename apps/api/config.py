"""
Configuration centralisée (Pydantic Settings)
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    """Configuration app via .env"""
    
    # Database
    # IMPORTANT: Pour Supabase, utiliser le rôle "postgres" (pas "user")
    # Format: postgresql://postgres:[MOT_DE_PASSE]@[HOST]:5432/postgres
    DATABASE_URL: str = Field(default="postgresql://postgres:password@localhost:5432/astroia_lunar")
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
    
    # Mode DEV Mock (pour tester sans clé API)
    DEV_MOCK_EPHEMERIS: bool = Field(default=False, description="Mode mock DEV : génère des données fake si clé API manquante")
    DEV_AUTH_BYPASS: bool = Field(default=False, description="Mode DEV: bypass JWT avec header X-Dev-User-Id (uniquement en development)")
    DEV_USER_ID: Optional[str] = Field(default=None, description="Mode DEV: ID utilisateur par défaut si X-Dev-User-Id absent (UUID ou integer)")
    
    # Supabase
    supabase_url: Optional[str] = Field(default=None, validation_alias="SUPABASE_URL")
    supabase_anon_key: Optional[str] = Field(default=None, validation_alias="SUPABASE_ANON_KEY")

    # Anthropic (Claude AI)
    ANTHROPIC_API_KEY: str = Field(default="", description="Clé API Anthropic pour génération interprétations")
    NATAL_INTERPRETATION_VERSION: int = Field(default=2, description="Version du prompt d'interprétation (2=moderne avec micro-rituel, 3=senior expérimental déprécié, 4=senior professionnel structuré)")

    # Aspect Explanations (v4)
    ASPECT_COPY_ENGINE: str = Field(default="template", description="Moteur de génération copy aspects: 'template' (déterministe) ou 'ai' (Haiku)")
    ASPECTS_VERSION: int = Field(default=4, description="Version du filtrage aspects (4=types majeurs, orbe ≤6°, exclure Lilith)")

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()

