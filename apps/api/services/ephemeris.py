"""
Client pour Ephemeris API (astrology-api.io)
Calculs thème natal et révolutions lunaires
"""

import httpx
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
from config import settings
import logging

from utils.api_key_validator import is_configured_api_key

logger = logging.getLogger(__name__)


class EphemerisAPIKeyError(Exception):
    """Exception levée quand la clé API Ephemeris n'est pas configurée"""
    pass


class EphemerisClient:
    """Client API pour calculs astrologiques"""
    
    def __init__(self):
        self.base_url = settings.EPHEMERIS_API_URL
        self.api_key = settings.EPHEMERIS_API_KEY
        self.is_configured = is_configured_api_key(self.api_key)
        self.mock_mode = settings.DEV_MOCK_EPHEMERIS
        
        if not self.is_configured:
            if self.mock_mode:
                logger.warning("🎭 MODE MOCK DEV activé - EPHEMERIS_API_KEY non configurée, génération de données fake")
            else:
                logger.warning("⚠️ EPHEMERIS_API_KEY non configurée ou placeholder - configurez-la ou activez DEV_MOCK_EPHEMERIS=1")
    
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
        
        Raises:
            EphemerisAPIKeyError: Si la clé API n'est pas configurée et mock mode désactivé
        """
        # Vérifier la clé API
        if not self.is_configured:
            if self.mock_mode:
                # Mode mock DEV : générer des données fake
                from utils.ephemeris_mock import generate_mock_natal_chart
                return generate_mock_natal_chart(date, time, latitude, longitude, timezone)
            else:
                # Clé manquante et mock désactivé : lever une exception propre
                raise EphemerisAPIKeyError(
                    "EPHEMERIS_API_KEY missing or placeholder. Configure it to compute natal charts, "
                    "or set DEV_MOCK_EPHEMERIS=1 for development."
                )
        
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
                
                # Normaliser le format de réponse pour garantir cohérence
                normalized_data = self._normalize_natal_chart_response(data)
                
                logger.info(f"✅ Thème natal calculé pour {birth_datetime}")
                return normalized_data
                
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
        
        Raises:
            EphemerisAPIKeyError: Si la clé API n'est pas configurée et mock mode désactivé
        """
        # Vérifier la clé API
        if not self.is_configured:
            if self.mock_mode:
                # Mode mock DEV : générer des données fake
                from utils.ephemeris_mock import generate_mock_lunar_return
                return generate_mock_lunar_return(
                    natal_moon_degree, natal_moon_sign, target_month,
                    birth_latitude, birth_longitude, timezone
                )
            else:
                # Clé manquante et mock désactivé : lever une exception propre
                raise EphemerisAPIKeyError(
                    "EPHEMERIS_API_KEY missing or placeholder. Configure it to compute lunar returns, "
                    "or set DEV_MOCK_EPHEMERIS=1 for development."
                )
        
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
    
    def _normalize_natal_chart_response(self, api_response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Normalise la réponse de l'API Ephemeris vers un format cohérent
        
        Gère différents formats possibles de l'API :
        - Format direct : {"sun": {...}, "moon": {...}, "ascendant": {...}}
        - Format avec planetary_positions : {"planetary_positions": [...]}
        - Format avec angles : {"angles": {"ascendant": {...}}}
        
        Returns:
            Format normalisé avec clés : sun, moon, ascendant, planets, houses, aspects
        """
        normalized = {}
        
        # Normaliser Sun
        if "sun" in api_response:
            normalized["sun"] = api_response["sun"]
        elif "planetary_positions" in api_response:
            # Chercher Sun dans planetary_positions
            for pos in api_response.get("planetary_positions", []):
                if isinstance(pos, dict) and pos.get("name", "").lower() == "sun":
                    normalized["sun"] = {
                        "sign": pos.get("sign") or pos.get("zodiac_sign"),
                        "degree": pos.get("degree") or pos.get("absolute_longitude", 0) % 30,
                        "absolute_longitude": pos.get("absolute_longitude"),
                        "house": pos.get("house") or pos.get("house_number")
                    }
                    break
        
        # Normaliser Moon
        if "moon" in api_response:
            normalized["moon"] = api_response["moon"]
        elif "planetary_positions" in api_response:
            # Chercher Moon dans planetary_positions
            for pos in api_response.get("planetary_positions", []):
                if isinstance(pos, dict) and pos.get("name", "").lower() == "moon":
                    normalized["moon"] = {
                        "sign": pos.get("sign") or pos.get("zodiac_sign"),
                        "degree": pos.get("degree") or pos.get("absolute_longitude", 0) % 30,
                        "absolute_longitude": pos.get("absolute_longitude"),
                        "house": pos.get("house") or pos.get("house_number")
                    }
                    break
        
        # Normaliser Ascendant
        if "ascendant" in api_response:
            normalized["ascendant"] = api_response["ascendant"]
        elif "angles" in api_response:
            angles = api_response.get("angles", {})
            if isinstance(angles, dict):
                if "ascendant" in angles:
                    normalized["ascendant"] = angles["ascendant"]
                elif "Ascendant" in angles:
                    normalized["ascendant"] = angles["Ascendant"]
        elif "planetary_positions" in api_response:
            # Chercher Ascendant dans planetary_positions
            for pos in api_response.get("planetary_positions", []):
                if isinstance(pos, dict) and pos.get("name", "").lower() in ["ascendant", "asc"]:
                    normalized["ascendant"] = {
                        "sign": pos.get("sign") or pos.get("zodiac_sign"),
                        "degree": pos.get("degree") or pos.get("absolute_longitude", 0) % 30,
                        "absolute_longitude": pos.get("absolute_longitude")
                    }
                    break
        
        # Normaliser planets (si présent en tant que dict ou array)
        if "planets" in api_response:
            normalized["planets"] = api_response["planets"]
        elif "planetary_positions" in api_response:
            # Convertir array en dict pour faciliter l'extraction
            planets_dict = {}
            for pos in api_response.get("planetary_positions", []):
                if isinstance(pos, dict):
                    name = pos.get("name", "").lower()
                    if name and name not in ["ascendant", "asc", "medium_coeli", "mean_node", "chiron"]:
                        planets_dict[name] = {
                            "sign": pos.get("sign") or pos.get("zodiac_sign"),
                            "degree": pos.get("degree") or (pos.get("absolute_longitude", 0) % 30),
                            "absolute_longitude": pos.get("absolute_longitude"),
                            "house": pos.get("house") or pos.get("house_number")
                        }
            if planets_dict:
                normalized["planets"] = planets_dict
        
        # Normaliser houses
        if "houses" in api_response:
            normalized["houses"] = api_response["houses"]
        elif "house_cusps" in api_response:
            # Convertir house_cusps en format dict si nécessaire
            normalized["houses"] = api_response.get("house_cusps", [])
        
        # Normaliser aspects
        if "aspects" in api_response:
            normalized["aspects"] = api_response["aspects"]
        
        # Conserver les autres clés si présentes
        for key in ["angles", "planetary_positions"]:
            if key in api_response and key not in normalized:
                normalized[key] = api_response[key]
        
        return normalized
    
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

