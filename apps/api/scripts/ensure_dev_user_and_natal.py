#!/usr/bin/env python3
"""
Script pour s'assurer qu'un user DEV et son natal chart existent
Idempotent: peut être exécuté plusieurs fois sans effet de bord
"""
import os
import sys
import asyncio
import json
from datetime import datetime, timezone
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Charger DATABASE_URL depuis .env
script_dir = os.path.dirname(os.path.abspath(__file__))
api_dir = os.path.dirname(script_dir)
env_path = os.path.join(api_dir, ".env")

if os.path.exists(env_path):
    from dotenv import load_dotenv
    load_dotenv(env_path)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("❌ DATABASE_URL non définie", file=sys.stderr)
    sys.exit(1)

# DEV_USER_ID depuis env ou fallback
DEV_USER_ID = int(os.getenv("DEV_USER_ID", os.getenv("EXPO_PUBLIC_DEV_USER_ID", "1")))

# Convertir postgresql:// en postgresql+asyncpg://
if DATABASE_URL.startswith("postgresql://"):
    ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
else:
    ASYNC_DATABASE_URL = DATABASE_URL

# Données mock pour le natal chart (compatible avec le code existant)
MOCK_NATAL_DATA = {
    "sun": {
        "sign": "Taurus",
        "degree": 15.5,
        "absolute_longitude": 45.5,
        "house": 1
    },
    "moon": {
        "sign": "Pisces",
        "degree": 28.1,
        "absolute_longitude": 328.1,
        "house": 4
    },
    "ascendant": {
        "sign": "Leo",
        "degree": 5.2,
        "absolute_longitude": 125.2
    },
    "planets": {
        "Sun": {"sign": "Taurus", "degree": 15.5, "house": 1},
        "Moon": {"sign": "Pisces", "degree": 28.1, "house": 4},
        "Mercury": {"sign": "Taurus", "degree": 20.0, "house": 1},
        "Venus": {"sign": "Gemini", "degree": 10.0, "house": 2},
        "Mars": {"sign": "Aries", "degree": 25.0, "house": 12},
        "Jupiter": {"sign": "Sagittarius", "degree": 18.0, "house": 7},
        "Saturn": {"sign": "Capricorn", "degree": 12.0, "house": 8},
        "Uranus": {"sign": "Aquarius", "degree": 8.0, "house": 9},
        "Neptune": {"sign": "Pisces", "degree": 22.0, "house": 10}
    },
    "houses": {
        "1": {"sign": "Leo", "degree": 5.2},
        "2": {"sign": "Virgo", "degree": 8.5},
        "3": {"sign": "Libra", "degree": 12.0},
        "4": {"sign": "Scorpio", "degree": 15.0},
        "5": {"sign": "Sagittarius", "degree": 18.0},
        "6": {"sign": "Capricorn", "degree": 20.0},
        "7": {"sign": "Aquarius", "degree": 5.2},
        "8": {"sign": "Pisces", "degree": 8.5},
        "9": {"sign": "Aries", "degree": 12.0},
        "10": {"sign": "Taurus", "degree": 15.0},
        "11": {"sign": "Gemini", "degree": 18.0},
        "12": {"sign": "Cancer", "degree": 20.0}
    },
    "aspects": [
        {"from": "Sun", "to": "Moon", "aspect": "trine", "orb": 2.5},
        {"from": "Moon", "to": "Venus", "aspect": "sextile", "orb": 1.8}
    ]
}

async def ensure_dev_user_and_natal():
    engine = create_async_engine(ASYNC_DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    async with async_session() as session:
        try:
            # 1. Vérifier/Créer le user DEV
            query = text("SELECT id, email, birth_latitude, birth_longitude, birth_timezone FROM users WHERE id = :user_id")
            result = await session.execute(query, {"user_id": DEV_USER_ID})
            user = result.fetchone()
            
            if not user:
                print(f"📝 Création du user DEV (id={DEV_USER_ID})...")
                # Créer le user avec colonnes NOT NULL minimales
                insert_user = text("""
                    INSERT INTO users (id, email, hashed_password, birth_date, birth_time, birth_latitude, birth_longitude, birth_place_name, birth_timezone)
                    VALUES (:id, :email, :password, :birth_date, :birth_time, :lat, :lon, :place, :tz)
                    ON CONFLICT (id) DO UPDATE SET
                        email = EXCLUDED.email,
                        birth_latitude = COALESCE(users.birth_latitude, EXCLUDED.birth_latitude),
                        birth_longitude = COALESCE(users.birth_longitude, EXCLUDED.birth_longitude),
                        birth_timezone = COALESCE(users.birth_timezone, EXCLUDED.birth_timezone)
                """)
                await session.execute(insert_user, {
                    "id": DEV_USER_ID,
                    "email": f"dev_user_{DEV_USER_ID}@test.local",
                    "password": "$2b$12$dummy_hash_for_dev",  # Hash bcrypt dummy
                    "birth_date": "1990-05-15",
                    "birth_time": "14:30",
                    "lat": "48.8566",  # Paris
                    "lon": "2.3522",
                    "place": "Paris, France",
                    "tz": "Europe/Paris"
                })
                await session.commit()
                print(f"✅ User DEV créé (id={DEV_USER_ID})")
            else:
                print(f"✅ User DEV existe déjà (id={DEV_USER_ID}, email={user.email})")
                # S'assurer que les coordonnées sont présentes
                if not user.birth_latitude or not user.birth_longitude or not user.birth_timezone:
                    print(f"📝 Mise à jour des coordonnées de naissance...")
                    update_user = text("""
                        UPDATE users 
                        SET birth_date = COALESCE(birth_date, '1990-05-15'),
                            birth_time = COALESCE(birth_time, '14:30'),
                            birth_latitude = COALESCE(birth_latitude, '48.8566'),
                            birth_longitude = COALESCE(birth_longitude, '2.3522'),
                            birth_place_name = COALESCE(birth_place_name, 'Paris, France'),
                            birth_timezone = COALESCE(birth_timezone, 'Europe/Paris')
                        WHERE id = :user_id
                    """)
                    await session.execute(update_user, {"user_id": DEV_USER_ID})
                    await session.commit()
                    print(f"✅ Coordonnées de naissance mises à jour")
            
            # 2. Vérifier/Créer le natal chart
            query_chart = text("SELECT id, user_id, positions, raw_data FROM natal_charts WHERE user_id = :user_id")
            result_chart = await session.execute(query_chart, {"user_id": DEV_USER_ID})
            chart = result_chart.fetchone()
            
            if not chart:
                print(f"📝 Création du natal chart pour user {DEV_USER_ID}...")
                # Créer le natal chart avec positions JSONB
                # id est UUID généré par gen_random_uuid() (default de la DB)
                insert_chart = text("""
                    INSERT INTO natal_charts (id, user_id, positions, raw_data, sun_sign, moon_sign, ascendant, planets, houses, aspects)
                    VALUES (
                        gen_random_uuid(),
                        :user_id,
                        CAST(:positions AS jsonb),
                        CAST(:raw_data AS json),
                        :sun_sign,
                        :moon_sign,
                        :ascendant,
                        CAST(:planets AS json),
                        CAST(:houses AS json),
                        CAST(:aspects AS json)
                    )
                """)
                await session.execute(insert_chart, {
                    "user_id": DEV_USER_ID,
                    "positions": json.dumps(MOCK_NATAL_DATA),
                    "raw_data": json.dumps(MOCK_NATAL_DATA),
                    "sun_sign": MOCK_NATAL_DATA["sun"]["sign"],
                    "moon_sign": MOCK_NATAL_DATA["moon"]["sign"],
                    "ascendant": MOCK_NATAL_DATA["ascendant"]["sign"],
                    "planets": json.dumps(MOCK_NATAL_DATA["planets"]),
                    "houses": json.dumps(MOCK_NATAL_DATA["houses"]),
                    "aspects": json.dumps(MOCK_NATAL_DATA["aspects"])
                })
                await session.commit()
                print(f"✅ Natal chart créé pour user {DEV_USER_ID}")
            else:
                print(f"✅ Natal chart existe déjà pour user {DEV_USER_ID} (id={chart.id})")
                # S'assurer que positions est rempli
                if not chart.positions:
                    print(f"📝 Mise à jour de positions dans natal chart...")
                    update_chart = text("""
                        UPDATE natal_charts 
                        SET positions = CAST(:positions AS jsonb),
                            raw_data = COALESCE(raw_data, CAST(:raw_data AS json)),
                            sun_sign = COALESCE(sun_sign, :sun_sign),
                            moon_sign = COALESCE(moon_sign, :moon_sign),
                            ascendant = COALESCE(ascendant, :ascendant)
                        WHERE user_id = :user_id
                    """)
                    await session.execute(update_chart, {
                        "user_id": DEV_USER_ID,
                        "positions": json.dumps(MOCK_NATAL_DATA),
                        "raw_data": json.dumps(MOCK_NATAL_DATA),
                        "sun_sign": MOCK_NATAL_DATA["sun"]["sign"],
                        "moon_sign": MOCK_NATAL_DATA["moon"]["sign"],
                        "ascendant": MOCK_NATAL_DATA["ascendant"]["sign"]
                    })
                    await session.commit()
                    print(f"✅ Positions mises à jour dans natal chart")
            
            print(f"\n✅ Provisioning terminé: user {DEV_USER_ID} et natal chart prêts")
            return 0
            
        except Exception as e:
            print(f"❌ Erreur lors du provisioning: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            await session.rollback()
            return 1
        finally:
            await engine.dispose()

if __name__ == "__main__":
    exit_code = asyncio.run(ensure_dev_user_and_natal())
    sys.exit(exit_code)

