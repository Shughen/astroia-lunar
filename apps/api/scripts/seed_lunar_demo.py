#!/usr/bin/env python3
"""
Script de démo pour tester tous les endpoints Luna Pack / Transits / Calendar
Utilise des payloads réalistes (Paris) pour valider l'intégration
"""

import asyncio
import httpx
from datetime import datetime

API_URL = "http://localhost:8000"

# Payload réaliste (Paris, coordonnées réelles)
PARIS_COORDS = {
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
}

DEMO_PAYLOAD = {
    "birth_date": "1989-04-15",
    "birth_time": "17:55",
    **PARIS_COORDS
}


async def test_health():
    """Test du health check"""
    print("\n🏥 Test Health Check...")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/health")
        print(f"   Status: {response.status_code}")
        print(f"   Data: {response.json()}")
        return response.status_code == 200


async def test_lunar_return_report():
    """Test Luna Pack - Lunar Return Report"""
    print("\n🌙 Test Lunar Return Report...")
    payload = {
        **DEMO_PAYLOAD,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "month": datetime.now().strftime("%Y-%m"),
        "user_id": 1
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                f"{API_URL}/api/lunar/return/report",
                json=payload
            )
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Kind: {data.get('kind')}")
                print(f"   Provider: {data.get('provider')}")
                return True
            else:
                print(f"   Error: {response.text[:200]}")
                return False
        except Exception as e:
            print(f"   Exception: {str(e)}")
            return False


async def test_void_of_course():
    """Test Luna Pack - Void of Course"""
    print("\n🌑 Test Void of Course...")
    payload = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M"),
        **PARIS_COORDS
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                f"{API_URL}/api/lunar/voc",
                json=payload
            )
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Kind: {data.get('kind')}")
                return True
            else:
                print(f"   Error: {response.text[:200]}")
                return False
        except Exception as e:
            print(f"   Exception: {str(e)}")
            return False


async def test_lunar_mansions():
    """Test Luna Pack - Lunar Mansions"""
    print("\n🏰 Test Lunar Mansions...")
    payload = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        **PARIS_COORDS
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                f"{API_URL}/api/lunar/mansion",
                json=payload
            )
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Kind: {data.get('kind')}")
                return True
            else:
                print(f"   Error: {response.text[:200]}")
                return False
        except Exception as e:
            print(f"   Exception: {str(e)}")
            return False


async def test_natal_transits():
    """Test Transits - Natal Transits"""
    print("\n🔄 Test Natal Transits...")
    payload = {
        **DEMO_PAYLOAD,
        "transit_date": datetime.now().strftime("%Y-%m-%d"),
        "user_id": 1
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                f"{API_URL}/api/transits/natal",
                json=payload
            )
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Kind: {data.get('kind')}")
                print(f"   Insights: {len(data.get('insights', {}).get('insights', []))} found")
                return True
            else:
                print(f"   Error: {response.text[:200]}")
                return False
        except Exception as e:
            print(f"   Exception: {str(e)}")
            return False


async def test_lunar_phases():
    """Test Calendar - Lunar Phases"""
    print("\n🌓 Test Lunar Phases...")
    now = datetime.now()
    payload = {
        "start_date": f"{now.year}-{now.month:02d}-01",
        "end_date": f"{now.year}-{now.month:02d}-{now.day:02d}",
        **PARIS_COORDS
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                f"{API_URL}/api/calendar/phases",
                json=payload
            )
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Kind: {data.get('kind')}")
                return True
            else:
                print(f"   Error: {response.text[:200]}")
                return False
        except Exception as e:
            print(f"   Exception: {str(e)}")
            return False


async def test_lunar_calendar_year():
    """Test Calendar - Lunar Calendar Year"""
    print("\n📅 Test Lunar Calendar Year...")
    payload = {
        "year": datetime.now().year,
        **PARIS_COORDS
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(
                f"{API_URL}/api/calendar/year",
                json=payload
            )
            print(f"   Status: {response.status_code}")
            if response.status_code == 200:
                data = response.json()
                print(f"   Kind: {data.get('kind')}")
                return True
            else:
                print(f"   Error: {response.text[:200]}")
                return False
        except Exception as e:
            print(f"   Exception: {str(e)}")
            return False


async def main():
    """Exécute tous les tests de démo"""
    print("=" * 60)
    print("🌙 ASTROIA LUNAR - Script de Démo des Endpoints")
    print("=" * 60)
    print(f"\n📡 API URL: {API_URL}")
    print(f"🗓️  Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"📍 Coordonnées: Paris ({PARIS_COORDS['latitude']}, {PARIS_COORDS['longitude']})")
    
    results = {}
    
    # Test Health Check
    results['health'] = await test_health()
    
    # Test Luna Pack
    results['lunar_return_report'] = await test_lunar_return_report()
    results['void_of_course'] = await test_void_of_course()
    results['lunar_mansions'] = await test_lunar_mansions()
    
    # Test Transits
    results['natal_transits'] = await test_natal_transits()
    
    # Test Calendar
    results['lunar_phases'] = await test_lunar_phases()
    results['lunar_calendar_year'] = await test_lunar_calendar_year()
    
    # Récapitulatif
    print("\n" + "=" * 60)
    print("📊 RÉCAPITULATIF")
    print("=" * 60)
    
    success_count = sum(1 for v in results.values() if v)
    total_count = len(results)
    
    for test_name, success in results.items():
        status = "✅" if success else "❌"
        print(f"   {status} {test_name}")
    
    print(f"\n🎯 Résultat: {success_count}/{total_count} tests réussis")
    
    if success_count == total_count:
        print("\n🎉 Tous les tests ont réussi !")
    elif success_count > 0:
        print(f"\n⚠️  {total_count - success_count} tests ont échoué")
        print("   Vérifiez que l'API est démarrée et que la DB est configurée.")
        print("   Les échecs sont normaux si RAPIDAPI_KEY n'est pas configurée.")
    else:
        print("\n❌ Tous les tests ont échoué")
        print("   L'API est-elle démarrée ? Vérifiez http://localhost:8000/health")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    asyncio.run(main())

