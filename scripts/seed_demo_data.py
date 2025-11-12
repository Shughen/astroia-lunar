#!/usr/bin/env python3
"""
Script pour créer des données de démo (thème natal + révolutions lunaires)
À utiliser quand RapidAPI n'est pas configurée
"""

import asyncio
import sys
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, text

# Import des modèles
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')
from database import AsyncSessionLocal
from models.user import User
from models.natal_chart import NatalChart
from models.lunar_return import LunarReturn


async def seed_demo_data(user_email: str):
    """Crée des données de démo pour un utilisateur"""
    
    async with AsyncSessionLocal() as db:
        # Trouver l'utilisateur
        result = await db.execute(select(User).where(User.email == user_email))
        user = result.scalar_one_or_none()
        
        if not user:
            print(f"❌ Utilisateur {user_email} non trouvé")
            return False
        
        print(f"✅ Utilisateur trouvé: {user.email} (ID: {user.id})")
        
        # 1. Créer un thème natal de démo
        print("\n1️⃣ Création du thème natal de démo...")
        
        # Vérifier si existe déjà
        existing_natal = await db.execute(select(NatalChart).where(NatalChart.user_id == user.id))
        if existing_natal.scalar_one_or_none():
            print("   ℹ️  Thème natal déjà existant, suppression...")
            await db.execute(delete(NatalChart).where(NatalChart.user_id == user.id))
        
        natal_chart = NatalChart(
            user_id=user.id,
            sun_sign="Bélier",
            moon_sign="Cancer",
            ascendant="Lion",
            planets={
                "Sun": {"sign": "Aries", "degree": 25.3, "house": 9},
                "Moon": {"sign": "Cancer", "degree": 12.7, "house": 12},
                "Mercury": {"sign": "Aries", "degree": 18.4, "house": 9},
                "Venus": {"sign": "Taurus", "degree": 3.2, "house": 10},
                "Mars": {"sign": "Gemini", "degree": 29.1, "house": 11},
            },
            houses={
                "1": {"sign": "Leo", "degree": 15.0},
                "2": {"sign": "Virgo", "degree": 10.5},
                "3": {"sign": "Libra", "degree": 8.2},
            },
            aspects={
                "Sun_Moon": {"type": "square", "orb": 1.2},
                "Venus_Mars": {"type": "sextile", "orb": 0.8},
            }
        )
        db.add(natal_chart)
        await db.commit()
        print("   ✅ Thème natal créé")
        
        # 2. Créer 12 révolutions lunaires
        print("\n2️⃣ Création des 12 révolutions lunaires...")
        
        # Supprimer les existantes
        await db.execute(delete(LunarReturn).where(LunarReturn.user_id == user.id))
        
        start_date = datetime.now()
        months_data = [
            {"asc": "Bélier", "house": 1, "moon_sign": "Bélier", "interp": "Mois d'initiative et de nouveaux départs"},
            {"asc": "Taureau", "house": 2, "moon_sign": "Taureau", "interp": "Focus sur la stabilité financière"},
            {"asc": "Gémeaux", "house": 3, "moon_sign": "Gémeaux", "interp": "Communication et apprentissage"},
            {"asc": "Cancer", "house": 4, "moon_sign": "Cancer", "interp": "Retour aux sources familiales"},
            {"asc": "Lion", "house": 5, "moon_sign": "Lion", "interp": "Créativité et expression personnelle"},
            {"asc": "Vierge", "house": 6, "moon_sign": "Vierge", "interp": "Organisation et santé"},
            {"asc": "Balance", "house": 7, "moon_sign": "Balance", "interp": "Relations et partenariats"},
            {"asc": "Scorpion", "house": 8, "moon_sign": "Scorpion", "interp": "Transformation profonde"},
            {"asc": "Sagittaire", "house": 9, "moon_sign": "Sagittaire", "interp": "Expansion et philosophie"},
            {"asc": "Capricorne", "house": 10, "moon_sign": "Capricorne", "interp": "Carrière et ambitions"},
            {"asc": "Verseau", "house": 11, "moon_sign": "Verseau", "interp": "Innovation et communauté"},
            {"asc": "Poissons", "house": 12, "moon_sign": "Poissons", "interp": "Spiritualité et introspection"},
        ]
        
        for i, month_data in enumerate(months_data):
            month_date = start_date + timedelta(days=28 * i)
            month_str = month_date.strftime("%Y-%m")
            return_date_str = month_date.strftime("%Y-%m-%d")
            
            lunar_return = LunarReturn(
                user_id=user.id,
                month=month_str,
                return_date=return_date_str,
                lunar_ascendant=month_data["asc"],
                moon_house=month_data["house"],
                moon_sign=month_data["moon_sign"],
                interpretation=month_data["interp"],
                aspects=[
                    {"planet": "Sun", "aspect": "trine", "orb": 2.1},
                    {"planet": "Venus", "aspect": "sextile", "orb": 1.5}
                ],
                planets={},
                houses={}
            )
            db.add(lunar_return)
        
        await db.commit()
        print(f"   ✅ 12 révolutions lunaires créées")
        
        print("\n✅ Données de démo créées avec succès !")
        print(f"\n📱 Rechargez l'app mobile (appuyez sur 'r' dans Expo)")
        print(f"   Vous devriez maintenant voir 12 mois à sélectionner !")
        
        return True


async def main():
    print("=" * 60)
    print("🌙 Astroia Lunar - Génération de Données de Démo")
    print("=" * 60)
    print()
    
    user_email = "remi.beaurain@gmail.com"
    success = await seed_demo_data(user_email)
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 TERMINÉ !")
        print("=" * 60)
        return 0
    else:
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

