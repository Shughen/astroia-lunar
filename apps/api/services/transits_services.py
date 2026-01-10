"""
Services métier pour les Transits (P2)
Calcule les transits planétaires croisés avec thème natal et révolutions lunaires
"""

from typing import Dict, Any
from services import rapidapi_client
import logging
from fastapi import HTTPException

logger = logging.getLogger(__name__)


async def get_natal_transits(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Obtient les transits planétaires actuels croisés avec le thème natal.
    
    Analyse les aspects formés par les planètes en transit avec les positions natales,
    permettant de comprendre les influences astrologiques du moment.
    
    Args:
        payload: {
            "birth_date": "YYYY-MM-DD",
            "birth_time": "HH:MM",
            "birth_latitude": float,
            "birth_longitude": float,
            "birth_timezone": "Europe/Paris",
            "transit_date": "YYYY-MM-DD",  # Date du transit à calculer
            "transit_time": "HH:MM",        # Optionnel
            "orb": 5.0                       # Orbe des aspects (degrés)
        }
        
    Returns:
        Données JSON avec les transits et aspects significatifs
        
    Raises:
        HTTPException: 502 si erreur provider
    """
    # Default transit_date = aujourd'hui si absent
    from datetime import datetime, timezone
    if not payload.get("transit_date"):
        transit_date_default = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    else:
        transit_date_default = payload.get("transit_date", "")
    
    logger.info(f"🔄 Calcul Natal Transits pour: {transit_date_default}")
    
    # Transformer le payload au format attendu par RapidAPI (même format que natal-chart)
    # RapidAPI attend: { "subject": { "name": "...", "birth_data": {...} }, "transit_data": {...}, "options": {...} }
    birth_date = payload.get("birth_date", "")
    if not birth_date:
        raise HTTPException(
            status_code=400,
            detail="birth_date est requis"
        )
    
    birth_time = payload.get("birth_time", "12:00")
    transit_date = transit_date_default
    transit_time = payload.get("transit_time", "12:00")
    
    # Parser les dates
    birth_year, birth_month, birth_day = map(int, birth_date.split("-"))
    birth_hour, birth_minute = map(int, birth_time.split(":"))
    
    transit_year, transit_month, transit_day = map(int, transit_date.split("-"))
    transit_hour, transit_minute = map(int, transit_time.split(":"))
    
    # Construire birth_data au format RapidAPI
    birth_data = {
        "year": birth_year,
        "month": birth_month,
        "day": birth_day,
        "hour": birth_hour,
        "minute": birth_minute,
        "second": 0,
        "city": "User",  # Par défaut, peut être amélioré
        "country_code": "FR",
        "latitude": payload.get("birth_latitude", 0.0),
        "longitude": payload.get("birth_longitude", 0.0),
        "timezone": payload.get("birth_timezone", "Europe/Paris")
    }
    
    # Construire transit_data au format RapidAPI
    transit_data = {
        "year": transit_year,
        "month": transit_month,
        "day": transit_day,
        "hour": transit_hour,
        "minute": transit_minute,
        "second": 0
    }
    
    # Construire le payload final au format RapidAPI
    rapidapi_payload = {
        "subject": {
            "name": "User",
            "birth_data": birth_data
        },
        "transit_data": transit_data,
        "options": {
            "orb": payload.get("orb", 5.0),
            "aspect_types": ["major"]  # Major aspects only
        }
    }
    
    try:
        result = await rapidapi_client.post_json(rapidapi_client.NATAL_TRANSITS_PATH, rapidapi_payload)
        logger.info("✅ Natal Transits calculés avec succès")
        return result
    except HTTPException:
        # Relancer les HTTPException telles quelles
        raise


async def get_lunar_return_transits(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Obtient les transits planétaires liés à une révolution lunaire donnée.
    
    Analyse comment les planètes en transit interagissent avec la carte
    de révolution lunaire du mois, pour affiner les prévisions mensuelles.
    
    Args:
        payload: {
            "birth_date": "YYYY-MM-DD",
            "birth_time": "HH:MM",
            "birth_latitude": float,
            "birth_longitude": float,
            "lunar_return_date": "YYYY-MM-DD",  # Date de la LR
            "transit_date": "YYYY-MM-DD",        # Date actuelle
            "orb": 5.0
        }
        
    Returns:
        Données JSON avec les transits sur la révolution lunaire
        
    Raises:
        HTTPException: 502 si erreur provider
    """
    logger.info(f"🌙 Calcul Lunar Return Transits pour: {payload.get('lunar_return_date', 'N/A')}")
    result = await rapidapi_client.post_json(rapidapi_client.LUNAR_RETURN_TRANSITS_PATH, payload)
    logger.info("✅ Lunar Return Transits calculés avec succès")
    return result


def generate_transit_insights(transits_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Génère des insights lisibles à partir des données brutes de transits.
    
    Extrait les 3-5 aspects les plus significatifs et génère des bullet points.
    
    Args:
        transits_data: Données brutes retournées par le provider (format RapidAPI: {"events": [...]})
        
    Returns:
        {
            "insights": ["Insight 1", "Insight 2", ...],
            "major_aspects": [
                {
                    "transit_planet": "Jupiter",
                    "natal_planet": "Sun",
                    "aspect": "trine",
                    "orb": 1.2,
                    "interpretation": "Période d'expansion et de confiance"
                }
            ],
            "energy_level": "high" | "medium" | "low",
            "themes": ["expansion", "communication", "changement"]
        }
    """
    insights = []
    major_aspects = []
    themes = []
    
    # RapidAPI retourne {"events": [...]} où chaque événement est un transit
    events = []
    if "events" in transits_data and isinstance(transits_data["events"], list):
        events = transits_data["events"]
    elif "aspects" in transits_data and isinstance(transits_data["aspects"], list):
        # Fallback pour l'ancien format
        events = transits_data["aspects"]
    
    if events:
        # Trier par importance (orbe le plus serré en valeur absolue)
        sorted_events = sorted(
            events,
            key=lambda e: abs(e.get("orb", 10))
        )[:5]  # Top 5 aspects
        
        # Mapping des noms d'aspects RapidAPI vers format standard
        aspect_name_mapping = {
            "conjunction": "conjunction",
            "opposition": "opposition",
            "trine": "trine",
            "square": "square",
            "sextile": "sextile"
        }
        
        for event in sorted_events:
            # Support multiple formats:
            # - RapidAPI: transiting_planet, aspect_type, stationed_planet, orb
            # - Test format: planet1, planet2, aspect, orb
            transit_planet = (
                event.get("transiting_planet") or 
                event.get("planet1") or 
                event.get("transit_planet") or 
                "Unknown"
            )
            aspect_type = event.get("aspect_type") or event.get("aspect", "unknown")
            natal_planet = (
                event.get("stationed_planet") or 
                event.get("planet2") or 
                event.get("natal_point") or 
                event.get("natal_planet") or 
                "Unknown"
            )
            orb = abs(event.get("orb", 0))  # Orbe en valeur absolue
            
            # Normaliser le nom de l'aspect
            aspect_normalized = aspect_name_mapping.get(aspect_type.lower(), aspect_type.lower())
            
            # Générer une interprétation basique si absente
            interpretation = event.get("interpretation", "")
            if not interpretation:
                # Générer une interprétation basique selon l'aspect
                aspect_interpretations = {
                    "conjunction": f"Fusion puissante entre {transit_planet} et votre {natal_planet} natal",
                    "opposition": f"Tension dynamique entre {transit_planet} et votre {natal_planet} natal",
                    "trine": f"Harmonie et facilité entre {transit_planet} et votre {natal_planet} natal",
                    "square": f"Challenge et croissance entre {transit_planet} et votre {natal_planet} natal",
                    "sextile": f"Opportunité et soutien entre {transit_planet} et votre {natal_planet} natal"
                }
                interpretation = aspect_interpretations.get(aspect_normalized, f"{transit_planet} en aspect avec votre {natal_planet} natal")
            
            major_aspects.append({
                "transit_planet": transit_planet,
                "natal_planet": natal_planet,
                "aspect": aspect_normalized,
                "orb": orb,
                "interpretation": interpretation
            })
            
            # Générer un insight
            insights.append(
                f"{transit_planet} forme un {aspect_normalized} avec votre {natal_planet} natal (orbe: {orb:.2f}°)"
            )
    
    # Déterminer le niveau d'énergie (heuristique simple)
    energy_level = "medium"
    if len(major_aspects) >= 4:
        energy_level = "high"
    elif len(major_aspects) <= 1:
        energy_level = "low"
    
    return {
        "insights": insights[:5],  # Max 5 insights
        "major_aspects": major_aspects,
        "energy_level": energy_level,
        "themes": themes
    }

