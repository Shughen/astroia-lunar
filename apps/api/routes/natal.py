"""Routes pour thème natal"""

import logging
from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import date, time, datetime
from uuid import UUID
import httpx

from database import get_db
from models.user import User
from models.natal_chart import NatalChart
from routes.auth import get_current_user
from services.ephemeris_rapidapi import create_natal_chart
from services.natal_reading_service import parse_positions_from_natal_chart, parse_aspects_from_natal_chart
from utils.natal_chart_helpers import extract_big3_from_positions
from services import transits_services
from schemas.transits import NatalTransitsRequest
from models.transits import TransitsOverview
from config import settings

router = APIRouter()
logger = logging.getLogger(__name__)

# Constante epsilon pour comparaison de coordonnées (tolérance float)
COORDS_EPSILON = 0.001


def _same_coords(
    existing_lat: Optional[float],
    existing_lon: Optional[float],
    lat_in: float,
    lon_in: float,
    epsilon: float = COORDS_EPSILON
) -> bool:
    """
    Compare deux paires de coordonnées avec tolérance epsilon.
    
    Args:
        existing_lat: Latitude existante (Decimal converti en float, peut être None)
        existing_lon: Longitude existante (Decimal converti en float, peut être None)
        lat_in: Latitude input (float)
        lon_in: Longitude input (float)
        epsilon: Tolérance pour comparaison (défaut: 0.001)
    
    Returns:
        True si les coordonnées sont identiques (dans la tolérance), False sinon
    """
    if existing_lat is None or existing_lon is None:
        return False
    return abs(existing_lat - lat_in) < epsilon and abs(existing_lon - lon_in) < epsilon


# === SCHEMAS ===
class NatalChartRequest(BaseModel):
    date: str  # YYYY-MM-DD
    time: Optional[str] = None  # HH:MM (optionnel, fallback à "12:00" si manquant)
    latitude: float
    longitude: float
    place_name: str
    timezone: Optional[str] = None  # Optionnel, ignoré - sera auto-détecté depuis lat/lon


class NatalChartResponse(BaseModel):
    id: str  # UUID as string
    sun_sign: str
    moon_sign: str
    ascendant: str
    planets: dict
    houses: dict
    aspects: list


# === ROUTES ===
@router.post("/natal-chart", response_model=NatalChartResponse, status_code=status.HTTP_201_CREATED)
async def calculate_natal_chart(
    data: NatalChartRequest,
    current_user: User = Depends(get_current_user),
    x_dev_user_id: Optional[str] = Header(default=None, alias="X-Dev-User-Id"),
    db: AsyncSession = Depends(get_db)
):
    """
    Calcule le thème natal et le sauvegarde
    IDEMPOTENT: Si un thème existe déjà avec les mêmes paramètres, retourne l'existant sans recalculer
    """
    # Fallback birth_time à "12:00" (midi) si manquant (comme dans l'ancienne app)
    # Normaliser le format time en HH:MM (tronquer les secondes si présentes)
    birth_time_raw = data.time if data.time else "12:00"
    birth_time = birth_time_raw[:5] if len(birth_time_raw) >= 5 else birth_time_raw  # HH:MM

    # Détecter automatiquement la timezone depuis les coordonnées GPS
    # IGNORER le timezone fourni par le client, toujours auto-détecter
    from utils.timezone_utils import guess_timezone_from_coords
    detected_timezone = guess_timezone_from_coords(
        latitude=data.latitude,
        longitude=data.longitude
    )

    logger.info(f"[TZ] auto-detected={detected_timezone} lat={data.latitude} lon={data.longitude}")

    # IDEMPOTENCE CHECK: Vérifier si un chart existe déjà avec les mêmes paramètres
    try:
        result = await db.execute(
            select(NatalChart).where(NatalChart.user_id == current_user.id)
        )
        existing_chart = result.scalar_one_or_none()

        if existing_chart:
            # Convertir birth_date/birth_time existants pour comparaison
            existing_date_str = existing_chart.birth_date.isoformat() if existing_chart.birth_date else None
            existing_time_str = existing_chart.birth_time.isoformat()[:5] if existing_chart.birth_time else None  # HH:MM

            # Convertir Decimal (NUMERIC) en float pour comparaison (gérer NULL)
            existing_lat = float(existing_chart.latitude) if existing_chart.latitude is not None else None
            existing_lon = float(existing_chart.longitude) if existing_chart.longitude is not None else None

            # Normaliser les inputs en float (sécurité)
            lat_in = float(data.latitude)
            lon_in = float(data.longitude)

            # Comparer les paramètres de naissance avec fonction utilitaire
            same_date = existing_date_str == data.date
            same_time = existing_time_str == birth_time
            same_coords = _same_coords(existing_lat, existing_lon, lat_in, lon_in)
            same_timezone = existing_chart.timezone == detected_timezone

            params_match = same_date and same_time and same_coords and same_timezone

            if params_match:
                # CACHE HIT: paramètres identiques, retourner l'existant sans recalculer
                logger.info(
                    f"[IDEMPOTENCE] HIT - natal_chart_id={existing_chart.id} user_id={current_user.id} "
                    f"reason=same_inputs (date={data.date} time={birth_time} coords=({lat_in:.4f},{lon_in:.4f}) tz={detected_timezone})"
                )

                # Extraire Big3 depuis positions pour la réponse
                big3 = extract_big3_from_positions(existing_chart.positions)

                # Extraire planets, houses, aspects depuis positions JSONB
                positions_data = existing_chart.positions or {}
                planets = positions_data.get("planets", {})
                houses = positions_data.get("houses", {})
                raw_aspects = positions_data.get("aspects", [])

                # Enrichir aspects avec métadonnées + copy v4 (si version v4 activée)
                aspects = raw_aspects
                if settings.ASPECTS_VERSION == 4:
                    try:
                        from services.aspect_explanation_service import enrich_aspects_v4
                        aspects = enrich_aspects_v4(raw_aspects, planets, limit=10)
                        logger.info(f"✅ Aspects enrichis v4: {len(aspects)} aspects avec copy")
                    except Exception as e:
                        logger.warning(f"⚠️ Erreur enrichissement aspects v4 (fallback raw aspects): {e}")
                        aspects = raw_aspects

                return {
                    "id": str(existing_chart.id),
                    "sun_sign": big3["sun_sign"] or "Unknown",
                    "moon_sign": big3["moon_sign"] or "Unknown",
                    "ascendant": big3["ascendant_sign"] or "Unknown",
                    "planets": planets,
                    "houses": houses,
                    "aspects": aspects
                }
            else:
                # CACHE MISS: paramètres différents, recalcul nécessaire
                reason_parts = []
                if not same_date:
                    reason_parts.append("date_changed")
                if not same_time:
                    reason_parts.append("time_changed")
                if not same_coords:
                    reason_parts.append("coords_changed")
                if not same_timezone:
                    reason_parts.append("timezone_changed")

                reason_str = "|".join(reason_parts) if reason_parts else "unknown"
                logger.info(
                    f"[IDEMPOTENCE] MISS - natal_chart_id={existing_chart.id} user_id={current_user.id} "
                    f"reason={reason_str}"
                )
        else:
            # Pas de chart existant
            logger.info(
                f"[IDEMPOTENCE] MISS - user_id={current_user.id} reason=no_existing"
            )
    except Exception as e:
        logger.error(f"❌ Erreur DB lors de la vérification idempotence: {e}", exc_info=True)
        # Continuer malgré l'erreur de vérification, on recalculera

    logger.info(f"📊 Calcul thème natal - user_id={current_user.id}, email={current_user.email}, date={data.date} {birth_time}, timezone={detected_timezone}")
    
    # Calculer via RapidAPI (Best Astrology API)
    try:
        # Construire le payload pour RapidAPI au format attendu
        # RapidAPI attend: { "subject": { "name": "...", "birth_data": {...} }, "options": {...} }
        # Mais create_natal_chart() attend un format simple, donc on utilise call_rapidapi_natal_chart directement
        from services.natal_reading_service import call_rapidapi_natal_chart
        
        # Format birth_data pour RapidAPI
        birth_data = {
            "year": int(data.date.split("-")[0]),
            "month": int(data.date.split("-")[1]),
            "day": int(data.date.split("-")[2]),
            "hour": int(birth_time.split(":")[0]),
            "minute": int(birth_time.split(":")[1]),
            "second": 0,
            "city": data.place_name or "Unknown",
            "country_code": "FR",  # Par défaut, peut être amélioré
            "latitude": data.latitude,
            "longitude": data.longitude,
            "timezone": detected_timezone  # Utiliser la timezone détectée
        }
        
        # Appel à RapidAPI via le service natal_reading_service
        rapidapi_response = await call_rapidapi_natal_chart(birth_data)
        logger.info(f"✅ Réponse RapidAPI reçue - clés disponibles: {list(rapidapi_response.keys())}")
        
        # Parser la réponse RapidAPI vers le format attendu
        # RapidAPI retourne: { "chart_data": { "planetary_positions": [...], "aspects": [...] } }
        chart_data = rapidapi_response.get("chart_data", {})
        if not chart_data:
            logger.error(f"❌ Pas de 'chart_data' dans la réponse RapidAPI. Keys: {list(rapidapi_response.keys())}")
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail="Format de réponse RapidAPI invalide: 'chart_data' manquant"
            )
        
        # Parser les positions et aspects depuis la réponse RapidAPI
        parsed_positions = parse_positions_from_natal_chart(rapidapi_response)
        parsed_aspects = parse_aspects_from_natal_chart(rapidapi_response)
        
        # Calculer les positions complémentaires manquantes (Uranus, Neptune, Pluton, Nœuds, Lilith, Chiron)
        # RapidAPI ne retourne que 9 positions, on complète avec Swiss Ephemeris si disponible
        try:
            from services.natal_planets_complement import calculate_complementary_positions, merge_complementary_positions
            from datetime import datetime, timezone as dt_timezone
            
            # Construire datetime de naissance en UTC
            birth_datetime = datetime(
                int(data.date.split("-")[0]),
                int(data.date.split("-")[1]),
                int(data.date.split("-")[2]),
                int(birth_time.split(":")[0]),
                int(birth_time.split(":")[1]),
                tzinfo=dt_timezone.utc
            )
            
            # Extraire les cuspides des maisons depuis chart_data pour calculer les maisons des positions complémentaires
            house_cusps = []
            houses_list = chart_data.get("house_cusps", [])
            if isinstance(houses_list, list):
                for cusp in houses_list[:12]:  # Prendre les 12 premières maisons
                    if isinstance(cusp, dict):
                        house_cusps.append(cusp.get("absolute_longitude", cusp.get("degree", 0.0)))
                    elif isinstance(cusp, (int, float)):
                        house_cusps.append(float(cusp))
            
            # Calculer positions complémentaires avec les cuspides pour déterminer les maisons
            complementary_positions = calculate_complementary_positions(
                birth_datetime,
                data.latitude,
                data.longitude,
                house_cusps if house_cusps else None
            )
            
            # Fusionner avec les positions RapidAPI
            if complementary_positions:
                parsed_positions = merge_complementary_positions(parsed_positions, complementary_positions)
                logger.info(f"✅ {len(complementary_positions)} positions complémentaires ajoutées (Uranus, Neptune, Pluton, Nœuds, Lilith, Chiron)")
        except Exception as e:
            logger.warning(f"⚠️ Impossible de calculer positions complémentaires: {e}. Continuons avec les positions RapidAPI uniquement.")
        
        # Mapping signes abrégés RapidAPI → noms complets attendus par le mobile
        sign_mapping = {
            "Ari": "Aries", "Tau": "Taurus", "Gem": "Gemini", "Can": "Cancer",
            "Leo": "Leo", "Vir": "Virgo", "Lib": "Libra", "Sco": "Scorpio",
            "Sag": "Sagittarius", "Cap": "Capricorn", "Aqu": "Aquarius", "Pis": "Pisces"
        }
        
        def map_sign(sign_abbr: str) -> str:
            """Convertit un signe abrégé en nom complet"""
            if not sign_abbr:
                return ""
            # Si déjà en format complet, retourner tel quel
            if sign_abbr in sign_mapping.values():
                return sign_abbr
            # Sinon mapper depuis l'abréviation
            return sign_mapping.get(sign_abbr, sign_abbr)
        
        # Convertir parsed_positions en format dict pour le mobile
        planets_dict = {}
        sun_data = None
        moon_data = None
        ascendant_data = None
        
        for pos in parsed_positions:
            name = pos.get("name", "").lower()
            sign_abbr = pos.get("sign", "")
            sign_full = map_sign(sign_abbr)
            
            # Extraire Big3 pour compatibilité (sun_data, moon_data, ascendant_data)
            if name == "sun":
                sun_data = {
                    "sign": sign_full,
                    "degree": pos.get("degree", 0.0),
                    "house": pos.get("house", 0)
                }
                # AUSSI ajouter dans planets_dict pour affichage complet
                planets_dict["sun"] = {
                    "sign": sign_full,
                    "degree": pos.get("degree", 0.0),
                    "house": pos.get("house", 0)
                }
            elif name == "moon":
                moon_data = {
                    "sign": sign_full,
                    "degree": pos.get("degree", 0.0),
                    "house": pos.get("house", 0)
                }
                # AUSSI ajouter dans planets_dict pour affichage complet
                planets_dict["moon"] = {
                    "sign": sign_full,
                    "degree": pos.get("degree", 0.0),
                    "house": pos.get("house", 0)
                }
            elif name == "ascendant":
                ascendant_data = {
                    "sign": sign_full,
                    "degree": pos.get("degree", 0.0)
                }
                # AUSSI ajouter dans planets_dict pour affichage complet (avec capitalisation)
                planets_dict["Ascendant"] = {  # Capitalisé pour affichage
                    "sign": sign_full,
                    "degree": pos.get("degree", 0.0),
                    "house": 1  # Ascendant = cuspide maison 1
                }
            elif name == "medium_coeli":
                # Ajouter Medium Coeli (MC) dans planets_dict avec nom français
                planets_dict["Milieu du Ciel"] = {  # Nom français pour affichage
                    "sign": sign_full,
                    "degree": pos.get("degree", 0.0),
                    "house": 10  # MC = cuspide maison 10
                }
            else:
                # Ajouter toutes les autres planètes et points (Mercure, Vénus, Mars, Jupiter, Saturne, Uranus, Neptune, Pluton, Nœuds, Lilith, Chiron, etc.)
                # Traduire mean_node/true_node en "Nœud Nord" pour affichage (unifier, éviter doublon)
                display_name = name
                if name in ["mean_node", "true_node"]:
                    # Si on a déjà "Nœud Nord", skip (éviter doublon)
                    if "Nœud Nord" in planets_dict:
                        continue
                    display_name = "Nœud Nord"
                elif name == "south_node":
                    display_name = "Nœud Sud"
                
                planets_dict[display_name] = {
                    "sign": sign_full,
                    "degree": pos.get("degree", 0.0),
                    "house": pos.get("house", 0)
                }
        
        # Parser les maisons depuis chart_data
        # RapidAPI retourne house_cusps comme array de longitudes absolues
        houses_list = chart_data.get("house_cusps", [])
        houses_dict = {}
        
        # Mapping signes depuis longitude absolue
        sign_names = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                     "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        
        if isinstance(houses_list, list):
            for i, cusp in enumerate(houses_list, 1):
                if isinstance(cusp, dict):
                    abs_long = cusp.get("absolute_longitude", cusp.get("degree", 0.0))
                    sign_idx = int(abs_long // 30) % 12
                    degree_in_sign = abs_long % 30
                    houses_dict[str(i)] = {
                        "sign": sign_names[sign_idx] if sign_idx < len(sign_names) else "",
                        "degree": round(degree_in_sign, 2)
                    }
                elif isinstance(cusp, (int, float)):
                    # Si c'est juste un nombre (longitude absolue)
                    abs_long = float(cusp)
                    sign_idx = int(abs_long // 30) % 12
                    degree_in_sign = abs_long % 30
                    houses_dict[str(i)] = {
                        "sign": sign_names[sign_idx] if sign_idx < len(sign_names) else "",
                        "degree": round(degree_in_sign, 2)
                    }
        
        # Convertir parsed_aspects en format attendu par le mobile
        aspects_list = []
        for asp in parsed_aspects:
            aspects_list.append({
                "planet1": asp.get("from", ""),
                "planet2": asp.get("to", ""),
                "type": asp.get("aspect_type", ""),
                "orb": asp.get("orb", 0.0)
            })
        
        # Construire raw_data au format attendu par le reste du code
        raw_data = {
            "sun": sun_data or {},
            "moon": moon_data or {},
            "ascendant": ascendant_data or {},
            "planets": planets_dict,
            "houses": houses_dict,
            "aspects": aspects_list
        }
        
        logger.info(f"✅ Thème natal parsé depuis RapidAPI - {len(planets_dict)} planètes, {len(houses_dict)} maisons, {len(aspects_list)} aspects")
        
    except httpx.HTTPStatusError as e:
        logger.error(f"❌ Erreur HTTP RapidAPI: {e.response.status_code} - {e.response.text}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Erreur RapidAPI (HTTP {e.response.status_code}): {e.response.text[:200]}"
        )
    except httpx.RequestError as e:
        logger.error(f"❌ Erreur requête RapidAPI: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Impossible de se connecter à RapidAPI: {str(e)}"
        )
    except Exception as e:
        logger.error(f"❌ Erreur calcul thème natal via RapidAPI: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur calcul thème natal: {str(e)}"
        )
    
    # Note: existing_chart déjà récupéré lors du check d'idempotence au début de la fonction
    # Récupérer à nouveau pour s'assurer d'avoir la dernière version (au cas où modifié entre-temps)
    try:
        result = await db.execute(
            select(NatalChart).where(NatalChart.user_id == current_user.id)
        )
        existing_chart = result.scalar_one_or_none()
    except Exception as e:
        logger.error(f"❌ Erreur DB lors de la vérification natal_chart: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de l'accès à la base de données"
        )
    
    if existing_chart:
        logger.info(f"🔄 Mise à jour thème natal existant - natal_chart_id={existing_chart.id}, user_id={current_user.id}")
    else:
        logger.info(f"✨ Création nouveau thème natal - user_id={current_user.id}")
    
    # Construire positions JSONB depuis raw_data (tout stocker dans positions)
    positions = {}
    if raw_data:
        # Extraire Big3 depuis raw_data
        if "sun" in raw_data:
            positions["sun"] = raw_data["sun"]
            logger.debug(f"📊 Sun ajouté à positions: {raw_data['sun'].get('sign', 'N/A')}")
        if "moon" in raw_data:
            positions["moon"] = raw_data["moon"]
            logger.debug(f"📊 Moon ajouté à positions: {raw_data['moon'].get('sign', 'N/A')}")
        if "ascendant" in raw_data:
            positions["ascendant"] = raw_data["ascendant"]
            logger.debug(f"📊 Ascendant ajouté à positions: {raw_data['ascendant'].get('sign', 'N/A')}")
        # Ajouter planets, houses, aspects directement dans positions
        if "planets" in raw_data:
            positions["planets"] = raw_data["planets"]
        if "houses" in raw_data:
            positions["houses"] = raw_data["houses"]
        if "aspects" in raw_data:
            positions["aspects"] = raw_data["aspects"]
        # Ajouter autres positions planétaires si disponibles
        if "planetary_positions" in raw_data:
            for pos in raw_data["planetary_positions"]:
                name = pos.get("name", "").lower()
                if name:
                    positions[name] = pos
        # Ajouter aussi les angles si présents
        if "angles" in raw_data:
            positions["angles"] = raw_data["angles"]
    
    # Compter les clés dans positions pour log
    positions_keys = list(positions.keys())
    logger.info(f"📦 Positions JSONB construit - {len(positions_keys)} clé(s): {positions_keys}")
    
    # Note: Les données de naissance (birth_date, birth_time, latitude, longitude, timezone)
    # sont stockées dans la table users, pas dans natal_charts.
    # Validation du format date/time pour s'assurer qu'elles sont valides avant stockage dans users
    try:
        # Valider le format de date (mais ne pas créer d'objet Date pour natal_charts)
        date.fromisoformat(data.date)  # String "YYYY-MM-DD" -> validation
        # Parser time: supporte "HH:MM" et "HH:MM:SS" (validation uniquement)
        time_str = birth_time
        if len(time_str.split(":")) == 2:
            # "HH:MM" -> time(HH, MM) pour validation
            hour, minute = map(int, time_str.split(":"))
            time(hour, minute)  # Validation uniquement
        else:
            # "HH:MM:SS" -> time.fromisoformat() pour validation
            time.fromisoformat(time_str)  # Validation uniquement
    except (ValueError, AttributeError) as e:
        logger.error(f"❌ Erreur parsing date/time: date={data.date}, time={birth_time}, error={e}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Format de date/heure invalide. Date attendu: YYYY-MM-DD, Time attendu: HH:MM ou HH:MM:SS"
        )
    
    if existing_chart:
        # Mise à jour
        # Note: Les données de naissance (birth_date, birth_time, latitude, longitude, timezone)
        # sont stockées dans la table users, pas dans natal_charts.
        # Le schéma DB réel de natal_charts ne contient que: id, user_id, positions, computed_at, version, created_at, updated_at
        existing_chart.positions = positions  # Tout dans positions JSONB
        chart = existing_chart
        logger.debug(f"💾 Thème natal mis à jour - natal_chart_id={chart.id}")
    else:
        # Création
        # Note: Les données de naissance (birth_date, birth_time, latitude, longitude, timezone)
        # sont stockées dans la table users, pas dans natal_charts.
        # Le schéma DB réel de natal_charts ne contient que: id, user_id, positions, computed_at, version, created_at, updated_at
        chart = NatalChart(
            user_id=current_user.id,  # Utiliser user_id INTEGER
            positions=positions  # Tout dans positions JSONB
        )
        db.add(chart)
        logger.debug(f"💾 Nouveau thème natal ajouté en session DB - user_id={current_user.id}")
    
    # Mettre à jour les infos de naissance du user (pour compatibilité)
    current_user.birth_date = data.date
    current_user.birth_time = birth_time
    current_user.birth_latitude = str(data.latitude)
    current_user.birth_longitude = str(data.longitude)
    current_user.birth_place_name = data.place_name
    current_user.birth_timezone = detected_timezone
    
    # Log clair avant commit avec tous les champs qui vont en DB
    # Note: Les données de naissance sont stockées dans users, pas dans natal_charts
    logger.info(f"💾 Sauvegarde DB natal_chart - user_id={chart.user_id}, "
                f"positions_keys={list(positions.keys())[:5]}..., "
                f"birth_data_in_users: date={data.date}, time={birth_time}, "
                f"lat={data.latitude}, lon={data.longitude}, tz={detected_timezone}")
    
    try:
        await db.commit()
        await db.refresh(chart)
        logger.info(f"✅ Thème natal sauvegardé - natal_chart_id={chart.id}, user_id={chart.user_id}")
    except Exception as e:
        await db.rollback()
        logger.error(f"❌ Erreur DB lors de la sauvegarde natal_chart: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la sauvegarde en base de données"
        )
    
    # Extraire Big3 depuis positions pour la réponse
    big3 = extract_big3_from_positions(chart.positions)
    
    logger.info(f"✨ Big3 extrait - Sun={big3['sun_sign']}, Moon={big3['moon_sign']}, Asc={big3['ascendant_sign']}")

    # Extraire planets, houses, aspects depuis positions JSONB
    # Fallback vers raw_data ou colonnes legacy si positions est NULL
    positions_data = chart.positions
    if not positions_data and hasattr(chart, 'raw_data') and chart.raw_data:
        positions_data = chart.raw_data
    if not positions_data:
        # Fallback vers colonnes legacy (planets, houses, aspects JSON)
        positions_data = {}
        if hasattr(chart, 'planets') and chart.planets:
            positions_data["planets"] = chart.planets
        if hasattr(chart, 'houses') and chart.houses:
            positions_data["houses"] = chart.houses
        if hasattr(chart, 'aspects') and chart.aspects:
            positions_data["aspects"] = chart.aspects
    positions_data = positions_data or {}
    
    planets = positions_data.get("planets", {})
    houses = positions_data.get("houses", {})
    raw_aspects = positions_data.get("aspects", [])

    # Enrichir aspects avec métadonnées + copy v4 (si version v4 activée)
    aspects = raw_aspects
    if settings.ASPECTS_VERSION == 4:
        try:
            from services.aspect_explanation_service import enrich_aspects_v4
            aspects = enrich_aspects_v4(raw_aspects, planets, limit=10)
            logger.info(f"✅ Aspects enrichis v4: {len(aspects)} aspects avec copy")
        except Exception as e:
            logger.warning(f"⚠️ Erreur enrichissement aspects v4 (fallback raw aspects): {e}")
            aspects = raw_aspects

    # Stocker chart.id AVANT toute opération qui pourrait causer un rollback
    # pour éviter l'erreur MissingGreenlet lors de l'accès après rollback
    chart_id_str = str(chart.id)
    
    # Générer automatiquement les transits pour le mois actuel si en mode DEV_AUTH_BYPASS
    # ou si un UUID est fourni dans le header
    try:
        user_uuid = None
        if settings.APP_ENV == "development" and settings.DEV_AUTH_BYPASS and x_dev_user_id:
            try:
                user_uuid = UUID(x_dev_user_id)
                logger.info(f"🔧 Génération automatique transits avec UUID du header: {user_uuid}")
            except (ValueError, TypeError):
                logger.warning(f"⚠️ UUID du header X-Dev-User-Id invalide: {x_dev_user_id}, skip génération transits")
        
        if user_uuid:
            # Date actuelle pour les transits
            today = datetime.now().date()
            transit_date = today.isoformat()  # YYYY-MM-DD
            
            # Construire la requête pour les transits
            transits_request = NatalTransitsRequest(
                birth_date=data.date,
                birth_time=birth_time,
                birth_latitude=data.latitude,
                birth_longitude=data.longitude,
                birth_timezone=detected_timezone,
                transit_date=transit_date,
                user_id=user_uuid
            )
            
            # Appel au service de transits (en arrière-plan, ne pas bloquer la réponse)
            try:
                # Exclure user_id du payload envoyé à RapidAPI (c'est juste pour notre DB)
                payload = transits_request.model_dump(exclude_none=True, exclude={"user_id"})
                
                result = await transits_services.get_natal_transits(payload)
                insights = transits_services.generate_transit_insights(result)
                
                # Sauvegarder en DB
                transit_month = transit_date[:7]  # YYYY-MM
                from sqlalchemy import and_
                stmt = select(TransitsOverview).where(
                    and_(
                        TransitsOverview.user_id == user_uuid,
                        TransitsOverview.month == transit_month
                    )
                )
                existing = await db.execute(stmt)
                existing_overview = existing.scalar_one_or_none()
                
                overview_data = {
                    "natal_transits": result,
                    "insights": insights,
                    "last_updated": datetime.now().isoformat()
                }
                
                if existing_overview:
                    existing_overview.overview = overview_data
                    logger.info(f"♻️  Transits overview mis à jour automatiquement pour {transit_month}")
                else:
                    overview = TransitsOverview(
                        user_id=user_uuid,
                        month=transit_month,
                        overview=overview_data
                    )
                    db.add(overview)
                    logger.info(f"💾 Nouveau transits overview créé automatiquement pour {transit_month}")
                
                await db.commit()
                logger.info(f"✅ Transits générés automatiquement pour user {user_uuid}, mois {transit_month}")
            except Exception as e:
                logger.warning(f"⚠️ Erreur génération automatique transits (non bloquant): {str(e)}")
                await db.rollback()
                
                await db.rollback()
                # Ne pas bloquer la réponse du thème natal si les transits échouent
    except Exception as e:
        logger.warning(f"⚠️ Erreur préparation génération transits (non bloquant): {str(e)}")
        # Ne pas bloquer la réponse du thème natal
    
    # Construire la réponse avec Big3 extrait depuis positions
    # Utiliser chart_id_str stocké avant pour éviter l'erreur MissingGreenlet
    return {
        "id": chart_id_str,  # UUID -> string (déjà converti avant)
        "sun_sign": big3["sun_sign"] or "Unknown",
        "moon_sign": big3["moon_sign"] or "Unknown",
        "ascendant": big3["ascendant_sign"] or "Unknown",
        "planets": planets,
        "houses": houses,
        "aspects": aspects
    }


@router.get("/natal-chart", response_model=NatalChartResponse)
async def get_natal_chart(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Récupère le thème natal de l'utilisateur"""
    
    try:
        result = await db.execute(
            select(NatalChart).where(NatalChart.user_id == current_user.id)
        )
        chart = result.scalar_one_or_none()
    except Exception as e:
        logger.error(f"❌ Erreur DB lors de la récupération natal_chart: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de l'accès à la base de données"
        )
    
    if not chart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Thème natal non calculé. Utilisez POST /api/natal-chart d'abord."
        )
    
    # Extraire Big3 depuis positions pour la réponse
    big3 = extract_big3_from_positions(chart.positions)

    # Extraire planets, houses, aspects depuis positions JSONB
    positions_data = chart.positions or {}
    planets = positions_data.get("planets", {})
    houses = positions_data.get("houses", {})
    raw_aspects = positions_data.get("aspects", [])

    # Enrichir aspects avec métadonnées + copy v4 (si version v4 activée)
    aspects = raw_aspects
    if settings.ASPECTS_VERSION == 4:
        try:
            from services.aspect_explanation_service import enrich_aspects_v4
            aspects = enrich_aspects_v4(raw_aspects, planets, limit=10)
            logger.info(f"✅ Aspects enrichis v4: {len(aspects)} aspects avec copy")
        except Exception as e:
            logger.warning(f"⚠️ Erreur enrichissement aspects v4 (fallback raw aspects): {e}")
            aspects = raw_aspects

    # Construire la réponse avec Big3 extrait depuis positions
    return {
        "id": str(chart.id),  # UUID -> string
        "sun_sign": big3["sun_sign"] or "Unknown",
        "moon_sign": big3["moon_sign"] or "Unknown",
        "ascendant": big3["ascendant_sign"] or "Unknown",
        "planets": planets,
        "houses": houses,
        "aspects": aspects
    }


# === RAPIDAPI PASS-THROUGH ===
@router.post("/natal-chart/external")
async def calculate_natal_chart_external(
    payload: Dict[str, Any]
):
    """
    Endpoint pass-through vers RapidAPI pour calculer un thème natal.
    Accepte n'importe quel payload JSON et le transmet directement à RapidAPI.
    
    Exemple de payload:
    {
        "name": "John Doe",
        "date": "1990-05-15",
        "time": "14:30",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }
    """
    try:
        # Appel à RapidAPI via le service
        rapidapi_response = await create_natal_chart(payload)
        
        # Retour structuré
        return {
            "provider": "rapidapi",
            "endpoint": "chart_natal",
            "data": rapidapi_response
        }
        
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Ephemeris error: {e.response.status_code} - {e.response.text}"
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Ephemeris error: Unable to connect - {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ephemeris error: {str(e)}"
        )

