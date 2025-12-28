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


# === SCHEMAS ===
class NatalChartRequest(BaseModel):
    date: str  # YYYY-MM-DD
    time: Optional[str] = None  # HH:MM (optionnel, fallback à "12:00" si manquant)
    latitude: float
    longitude: float
    place_name: str
    timezone: str = "Europe/Paris"


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
    Si un thème existe déjà, il sera écrasé
    """
    # Fallback birth_time à "12:00" (midi) si manquant (comme dans l'ancienne app)
    birth_time = data.time if data.time else "12:00"
    
    logger.info(f"📊 Calcul thème natal - user_id={current_user.id}, email={current_user.email}, date={data.date} {birth_time}")
    
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
            "timezone": data.timezone
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
            
            if name == "sun":
                sun_data = {
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
            elif name == "ascendant":
                ascendant_data = {
                    "sign": sign_full,
                    "degree": pos.get("degree", 0.0)
                }
            elif name not in ["ascendant", "medium_coeli", "mean_node", "chiron"]:
                # Ajouter les planètes (pas les angles)
                planets_dict[name] = {
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
    
    # Vérifier si un thème existe déjà (utiliser user_id INTEGER)
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
    
    # Convertir les strings en types Date/Time pour SQLAlchemy
    try:
        birth_date_obj = date.fromisoformat(data.date)  # String "YYYY-MM-DD" -> date
        # Parser time: supporte "HH:MM" et "HH:MM:SS" (utiliser birth_time avec fallback)
        time_str = birth_time
        if len(time_str.split(":")) == 2:
            # "HH:MM" -> time(HH, MM)
            hour, minute = map(int, time_str.split(":"))
            birth_time_obj = time(hour, minute)
        else:
            # "HH:MM:SS" -> time.fromisoformat()
            birth_time_obj = time.fromisoformat(time_str)
    except (ValueError, AttributeError) as e:
        logger.error(f"❌ Erreur parsing date/time: date={data.date}, time={birth_time}, error={e}")
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Format de date/heure invalide. Date attendu: YYYY-MM-DD, Time attendu: HH:MM ou HH:MM:SS"
        )
    
    if existing_chart:
        # Mise à jour
        existing_chart.positions = positions  # Tout dans positions JSONB
        existing_chart.birth_date = birth_date_obj
        existing_chart.birth_time = birth_time_obj
        existing_chart.birth_place = data.place_name  # Mapper place_name -> birth_place
        existing_chart.latitude = data.latitude
        existing_chart.longitude = data.longitude
        existing_chart.timezone = data.timezone
        chart = existing_chart
        logger.debug(f"💾 Thème natal mis à jour - natal_chart_id={chart.id}")
    else:
        # Création
        chart = NatalChart(
            user_id=current_user.id,  # Utiliser user_id INTEGER
            birth_date=birth_date_obj,
            birth_time=birth_time_obj,
            birth_place=data.place_name,  # Mapper place_name -> birth_place
            latitude=data.latitude,
            longitude=data.longitude,
            timezone=data.timezone,
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
    current_user.birth_timezone = data.timezone
    
    # Log clair avant commit avec tous les champs qui vont en DB
    logger.info(f"💾 Sauvegarde DB natal_chart - user_id={chart.user_id}, birth_date={chart.birth_date}, "
                f"birth_time={chart.birth_time}, birth_place={chart.birth_place}, "
                f"latitude={chart.latitude}, longitude={chart.longitude}, "
                f"timezone={chart.timezone}, positions_keys={list(positions.keys())[:5]}...")
    
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
    positions_data = chart.positions or {}
    planets = positions_data.get("planets", {})
    houses = positions_data.get("houses", {})
    aspects = positions_data.get("aspects", [])
    
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
                birth_timezone=data.timezone,
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
    aspects = positions_data.get("aspects", [])
    
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

