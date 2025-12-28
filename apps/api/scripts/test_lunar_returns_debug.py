#!/usr/bin/env python3
"""
Script de debug pour reproduire l'erreur 500 sur POST /api/lunar-returns/generate
Capture l'exception exacte et affiche la stacktrace complète
"""

import asyncio
import sys
import traceback
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import select
from config import settings
from models.user import User
from models.natal_chart import NatalChart
from models.lunar_return import LunarReturn
from services.ephemeris import ephemeris_client
from services.interpretations import generate_lunar_return_interpretation
from utils.natal_chart_helpers import extract_moon_data_from_positions
from datetime import datetime

# Convertir postgresql:// en postgresql+asyncpg://
DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Engine async
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def test_generate_lunar_returns():
    """Reproduit le flow de generate_lunar_returns pour capturer l'erreur"""
    
    async with AsyncSessionLocal() as db:
        # 1. Récupérer un user (premier disponible)
        result = await db.execute(select(User).limit(1))
        user = result.scalar_one_or_none()
        
        if not user:
            print("❌ Aucun utilisateur trouvé en DB")
            return
        
        print(f"✅ User trouvé: id={user.id}, email={user.email}")
        
        # 2. Récupérer le natal_chart
        result = await db.execute(
            select(NatalChart).where(NatalChart.user_id == user.id)
        )
        natal_chart = result.scalar_one_or_none()
        
        if not natal_chart:
            print("❌ Aucun natal_chart trouvé pour cet utilisateur")
            return
        
        print(f"✅ Natal chart trouvé: id={natal_chart.id}, user_id={natal_chart.user_id}")
        print(f"   positions type: {type(natal_chart.positions)}")
        print(f"   positions keys: {list(natal_chart.positions.keys()) if isinstance(natal_chart.positions, dict) else 'N/A'}")
        
        # 3. Extraire les coordonnées
        birth_latitude = float(natal_chart.latitude) if natal_chart.latitude is not None else None
        birth_longitude = float(natal_chart.longitude) if natal_chart.longitude is not None else None
        birth_timezone = str(natal_chart.timezone) if natal_chart.timezone else None
        
        print(f"   Coordonnées: lat={birth_latitude}, lon={birth_longitude}, tz={birth_timezone}")
        
        # 4. Extraire la Lune
        positions = natal_chart.positions or {}
        moon_data = extract_moon_data_from_positions(positions)
        natal_moon_degree = moon_data.get("degree", 0)
        natal_moon_sign = moon_data.get("sign")
        
        print(f"   Lune: sign={natal_moon_sign}, degree={natal_moon_degree}")
        
        # 5. Générer un seul mois (2025-01) pour tester
        month = "2025-01"
        print(f"\n🔄 Test génération pour {month}...")
        
        # 6. Calculer via Ephemeris (mock)
        try:
            raw_data = await ephemeris_client.calculate_lunar_return(
                natal_moon_degree=natal_moon_degree,
                natal_moon_sign=natal_moon_sign,
                target_month=month,
                birth_latitude=birth_latitude,
                birth_longitude=birth_longitude,
                timezone=birth_timezone,
            )
            print(f"✅ Calcul réussi: {list(raw_data.keys())}")
        except Exception as e:
            print(f"❌ Erreur calcul: {e}")
            traceback.print_exc()
            return
        
        # 7. Parser les données
        lunar_ascendant = raw_data.get("ascendant", {}).get("sign", "Unknown")
        moon_house = raw_data.get("moon", {}).get("house", 1)
        moon_sign = raw_data.get("moon", {}).get("sign", natal_moon_sign)
        aspects = raw_data.get("aspects", [])
        return_date = raw_data.get("return_datetime", f"{month}-15T12:00:00")
        
        print(f"   Parsed: asc={lunar_ascendant}, moon_house={moon_house}, moon_sign={moon_sign}")
        
        # 8. Générer l'interprétation
        interpretation = generate_lunar_return_interpretation(
            lunar_ascendant=lunar_ascendant,
            moon_house=moon_house,
            aspects=aspects,
        )
        
        # 9. Créer l'objet LunarReturn
        print(f"\n💾 Création objet LunarReturn...")
        lunar_return = LunarReturn(
            user_id=user.id,
            month=month,
            return_date=return_date,
            lunar_ascendant=lunar_ascendant,
            moon_house=moon_house,
            moon_sign=moon_sign,
            aspects=aspects,
            planets=raw_data.get("planets", {}),
            houses=raw_data.get("houses", {}),
            interpretation=interpretation,
            raw_data=raw_data,
        )
        
        print(f"   Objet créé: {lunar_return}")
        
        # 10. Ajouter à la session
        print(f"\n➕ Ajout à la session DB...")
        db.add(lunar_return)
        
        # 11. Commit (c'est ici que ça devrait casser si problème de schéma)
        print(f"\n💾 Commit DB...")
        try:
            await db.commit()
            print("✅ Commit réussi!")
        except Exception as e:
            print(f"❌ ERREUR AU COMMIT:")
            print(f"   Type: {type(e).__name__}")
            print(f"   Message: {str(e)}")
            print(f"\n   Stacktrace complète:")
            traceback.print_exc()
            
            # Rollback
            await db.rollback()
            print("\n   Rollback effectué")


if __name__ == "__main__":
    asyncio.run(test_generate_lunar_returns())

