"""
Services métier pour les Transits (P2)
Calcule les transits planétaires croisés avec thème natal et révolutions lunaires
"""

from typing import Dict, Any
from services import rapidapi_client
import logging

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
    logger.info(f"🔄 Calcul Natal Transits pour: {payload.get('transit_date', 'N/A')}")
    result = await rapidapi_client.post_json(rapidapi_client.NATAL_TRANSITS_PATH, payload)
    logger.info("✅ Natal Transits calculés avec succès")
    return result


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
        transits_data: Données brutes retournées par le provider
        
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
    # TODO: Implémenter la logique d'extraction d'insights
    # Pour l'instant, retourner une structure de base
    
    insights = []
    major_aspects = []
    themes = []
    
    # Extraction des aspects (logique simplifiée, à adapter selon le format du provider)
    if "aspects" in transits_data and isinstance(transits_data["aspects"], list):
        # Trier par importance (orbe le plus serré)
        sorted_aspects = sorted(
            transits_data["aspects"],
            key=lambda a: abs(a.get("orb", 10))
        )[:5]
        
        for aspect in sorted_aspects:
            major_aspects.append({
                "transit_planet": aspect.get("planet1", "Unknown"),
                "natal_planet": aspect.get("planet2", "Unknown"),
                "aspect": aspect.get("aspect", "unknown"),
                "orb": aspect.get("orb", 0),
                "interpretation": aspect.get("interpretation", "")
            })
            
            # Générer un insight
            planet1 = aspect.get("planet1", "Planète")
            planet2 = aspect.get("planet2", "Point")
            aspect_name = aspect.get("aspect", "aspect")
            insights.append(
                f"{planet1} forme un {aspect_name} avec votre {planet2} natal"
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

