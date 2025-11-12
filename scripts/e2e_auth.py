#!/usr/bin/env python3
"""
Script E2E pour tester le flux d'authentification complet
Génère un email aléatoire, s'inscrit, se connecte, et récupère le profil
"""

import sys
import httpx
import random
import string
from datetime import datetime


API_URL = "http://localhost:8000"
TIMEOUT = 10.0

def generate_random_email():
    """Génère un email aléatoire pour les tests"""
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test-{random_string}@example.com"


def print_step(step: str, success: bool, details: str = ""):
    """Affiche le résultat d'une étape"""
    icon = "✅" if success else "❌"
    print(f"{icon} {step}")
    if details:
        print(f"   {details}")


def main():
    print("=" * 60)
    print("🧪 Astroia Lunar - E2E Auth Test")
    print("=" * 60)
    print(f"🔗 API: {API_URL}")
    print(f"⏰ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Générer un email de test
    test_email = generate_random_email()
    test_password = "test123456"
    print(f"📧 Test email: {test_email}")
    print(f"🔑 Test password: {test_password}")
    print()
    
    results = {
        'register': False,
        'login': False,
        'getMe': False,
    }
    
    try:
        with httpx.Client(timeout=TIMEOUT) as client:
            
            # ÉTAPE 1: Register
            print("1️⃣ Testing POST /api/auth/register...")
            try:
                response = client.post(
                    f"{API_URL}/api/auth/register",
                    json={
                        "email": test_email,
                        "password": test_password,
                        "birth_date": "1990-01-01",
                        "birth_time": "12:00",
                        "birth_latitude": "48.8566",
                        "birth_longitude": "2.3522",
                        "birth_place_name": "Paris",
                        "birth_timezone": "Europe/Paris",
                    }
                )
                
                if response.status_code in [200, 201]:
                    data = response.json()
                    access_token = data.get('access_token')
                    if access_token:
                        print_step("Register", True, f"Token reçu: {access_token[:30]}...")
                        results['register'] = True
                    else:
                        print_step("Register", False, "Pas de token dans la réponse")
                else:
                    print_step("Register", False, f"HTTP {response.status_code}: {response.text[:100]}")
            except Exception as e:
                print_step("Register", False, f"Exception: {str(e)}")
            
            print()
            
            # ÉTAPE 2: Login
            print("2️⃣ Testing POST /api/auth/login (form-encoded)...")
            try:
                response = client.post(
                    f"{API_URL}/api/auth/login",
                    data={
                        "username": test_email,
                        "password": test_password,
                    },
                    headers={
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    access_token = data.get('access_token')
                    token_type = data.get('token_type')
                    
                    if access_token and token_type:
                        print_step("Login", True, f"Token: {access_token[:30]}..., Type: {token_type}")
                        results['login'] = True
                        
                        # ÉTAPE 3: Get Me
                        print()
                        print("3️⃣ Testing GET /api/auth/me (with Bearer token)...")
                        try:
                            response = client.get(
                                f"{API_URL}/api/auth/me",
                                headers={
                                    "Authorization": f"Bearer {access_token}"
                                }
                            )
                            
                            if response.status_code == 200:
                                user_data = response.json()
                                user_email = user_data.get('email')
                                user_id = user_data.get('id')
                                
                                if user_email == test_email:
                                    print_step("Get Me", True, f"User ID: {user_id}, Email: {user_email}")
                                    results['getMe'] = True
                                else:
                                    print_step("Get Me", False, f"Email mismatch: {user_email} != {test_email}")
                            else:
                                print_step("Get Me", False, f"HTTP {response.status_code}: {response.text[:100]}")
                        except Exception as e:
                            print_step("Get Me", False, f"Exception: {str(e)}")
                    else:
                        print_step("Login", False, "Pas de token ou token_type dans la réponse")
                else:
                    print_step("Login", False, f"HTTP {response.status_code}: {response.text[:100]}")
            except Exception as e:
                print_step("Login", False, f"Exception: {str(e)}")
    
    except Exception as e:
        print(f"❌ Erreur générale: {str(e)}")
    
    # Récapitulatif
    print()
    print("=" * 60)
    print("📊 RÉSULTATS")
    print("=" * 60)
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    
    for test_name, success in results.items():
        icon = "✅" if success else "❌"
        print(f"{icon} {test_name}")
    
    print()
    print(f"🎯 Score: {passed}/{total} tests passés")
    
    if passed == total:
        print("🎉 TOUS LES TESTS SONT PASSÉS !")
        print("=" * 60)
        return 0
    else:
        print(f"⚠️  {total - passed} test(s) ont échoué")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())

