"""
Client pour Ephemeris API (astrology-api.io)
Calculs thème natal et révolutions lunaires
"""

import httpx
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
from config import settings
import logging

logger = logging.getLogger(__name__)


class EphemerisClient:
    """Client API pour calculs astrologiques"""
    
    def __init__(self):
        self.base_url = settings.EPHEMERIS_API_URL
        self.api_key = settings.EPHEMERIS_API_KEY
        
        if not self.api_key:
            logger.warning("⚠️ EPHEMERIS_API_KEY non configurée")
    
    async def calculate_natal_chart(
        self,
        date: str,  # YYYY-MM-DD
        time: str,  # HH:MM
        latitude: float,
        longitude: float,
        timezone: str = "Europe/Paris"
    ) -> Dict[str, Any]:
        """
        Calcule le thème natal complet
        
        Returns:
            {
                "sun": { "sign": "Taurus", "degree": 15.3, ... },
                "moon": { "sign": "Pisces", "degree": 28.1, ... },
                "ascendant": { "sign": "Leo", "degree": 5.2 },
                "planets": { ... },
                "houses": { ... },
                "aspects": [ ... ]
            }
        """
        
        # Format date/heure
        birth_datetime = f"{date}T{time}:00"
        
        payload = {
            "datetime": birth_datetime,
            "latitude": latitude,
            "longitude": longitude,
            "timezone": timezone,
            "house_system": "placidus"  # Système de maisons standard
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                response = await client.post(
                    f"{self.base_url}/natal-chart",
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    }
                )
                response.raise_for_status()
                data = response.json()
                
                logger.info(f"✅ Thème natal calculé pour {birth_datetime}")
                return data
                
            except httpx.HTTPError as e:
                logger.error(f"❌ Erreur Ephemeris API: {e}")
                raise Exception(f"Erreur calcul thème natal: {str(e)}")
    
    async def calculate_lunar_return(
        self,
        natal_moon_degree: float,
        natal_moon_sign: str,
        target_month: str,  # YYYY-MM
        birth_latitude: float,
        birth_longitude: float,
        timezone: str = "Europe/Paris"
    ) -> Dict[str, Any]:
        """
        Calcule la révolution lunaire pour un mois donné
        
        La révolution lunaire = moment où la Lune revient à sa position natale
        
        Returns:
            {
                "return_datetime": "2025-11-15T14:32:00",
                "lunar_ascendant": "Taurus",
                "moon_house": 4,
                "aspects": [ ... ],
                "planets": { ... }
            }
        """
        
        # Parser le mois cible
        year, month = map(int, target_month.split("-"))
        
        # Estimation de la date de révolution (cycle lunaire = ~29.5 jours)
        # On cherche dans une fenêtre de +/- 5 jours autour du milieu du mois
        estimate_date = datetime(year, month, 15)
        
        payload = {
            "natal_moon_degree": natal_moon_degree,
            "natal_moon_sign": natal_moon_sign,
            "search_start": (estimate_date - timedelta(days=5)).isoformat(),
            "search_end": (estimate_date + timedelta(days=5)).isoformat(),
            "latitude": birth_latitude,
            "longitude": birth_longitude,
            "timezone": timezone,
            "house_system": "placidus"
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                response = await client.post(
                    f"{self.base_url}/lunar-return",
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    }
                )
                response.raise_for_status()
                data = response.json()
                
                logger.info(f"✅ Révolution lunaire calculée pour {target_month}")
                return data
                
            except httpx.HTTPError as e:
                logger.error(f"❌ Erreur Ephemeris API: {e}")
                # Fallback si l'API ne supporte pas lunar-return directement
                return await self._calculate_lunar_return_fallback(
                    estimate_date, birth_latitude, birth_longitude, timezone
                )
    
    async def _calculate_lunar_return_fallback(
        self,
        estimate_date: datetime,
        latitude: float,
        longitude: float,
        timezone: str
    ) -> Dict[str, Any]:
        """
        Fallback: calcule un thème pour le milieu du mois
        (si l'API ne supporte pas lunar-return directement)
        """
        
        logger.warning("⚠️ Utilisation du fallback (thème du 15 du mois)")
        
        payload = {
            "datetime": estimate_date.isoformat(),
            "latitude": latitude,
            "longitude": longitude,
            "timezone": timezone,
            "house_system": "placidus"
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.base_url}/chart",
                json=payload,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
            )
            response.raise_for_status()
            return response.json()
    
    async def get_moon_position(
        self,
        date: str,
        time: str,
        latitude: float,
        longitude: float
    ) -> Dict[str, Any]:
        """Récupère uniquement la position de la Lune"""
        
        payload = {
            "datetime": f"{date}T{time}:00",
            "latitude": latitude,
            "longitude": longitude,
            "planet": "Moon"
        }
        
        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.post(
                f"{self.base_url}/planet-position",
                json=payload,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
            )
            response.raise_for_status()
            return response.json()


# Instance singleton
ephemeris_client = EphemerisClient()

