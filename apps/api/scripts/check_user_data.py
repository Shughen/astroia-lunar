#!/usr/bin/env python3
"""Vérifier les données utilisateur et natal chart"""
import os
import sys
import asyncio
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("❌ DATABASE_URL non définie", file=sys.stderr)
    sys.exit(1)

if DATABASE_URL.startswith("postgresql://"):
    ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
else:
    ASYNC_DATABASE_URL = DATABASE_URL

async def check_user_data():
    engine = create_async_engine(ASYNC_DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    async with async_session() as session:
        user_id = 1  # DEV_USER_ID
        
        # Vérifier user
        query = text("SELECT id, email, birth_latitude, birth_longitude, birth_timezone FROM users WHERE id = :user_id")
        result = await session.execute(query, {"user_id": user_id})
        user = result.fetchone()
        
        if user:
            print(f"✅ User {user_id} trouvé: {user.email}")
            print(f"   birth_latitude: {user.birth_latitude}")
            print(f"   birth_longitude: {user.birth_longitude}")
            print(f"   birth_timezone: {user.birth_timezone}")
        else:
            print(f"❌ User {user_id} non trouvé")
        
        # Vérifier natal_chart
        query = text("""
            SELECT id, user_id, positions, raw_data, planets, houses, aspects
            FROM natal_charts 
            WHERE user_id = :user_id
        """)
        result = await session.execute(query, {"user_id": user_id})
        chart = result.fetchone()
        
        if chart:
            print(f"\n✅ Natal chart trouvé: id={chart.id}")
            print(f"   positions: {chart.positions is not None} (type: {type(chart.positions)})")
            print(f"   raw_data: {chart.raw_data is not None}")
            print(f"   planets: {chart.planets is not None}")
            print(f"   houses: {chart.houses is not None}")
            print(f"   aspects: {chart.aspects is not None}")
            if chart.positions:
                import json
                print(f"   positions keys: {list(chart.positions.keys())[:10] if isinstance(chart.positions, dict) else 'N/A'}")
        else:
            print(f"\n❌ Natal chart non trouvé pour user_id={user_id}")
    
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(check_user_data())

