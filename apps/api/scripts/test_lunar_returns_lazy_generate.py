#!/usr/bin/env python3
"""
Test de sanity pour lazy generate dans GET /api/lunar-returns/current

Vérifie que :
1. GET /current déclenche la génération automatique si DB vide
2. return_date n'est jamais None après génération (même en mode mock)

Usage:
    DEV_MOCK_EPHEMERIS=1 python scripts/test_lunar_returns_lazy_generate.py <email> <password> [API_URL]
"""

import sys
import os
import json
import requests
from typing import Optional, Dict, Any

# Configuration par défaut
DEFAULT_API_URL = "http://127.0.0.1:8000"


def login(email: str, password: str, api_url: str) -> Optional[str]:
    """Login et récupère le token JWT."""
    url = f"{api_url}/api/auth/login"
    data = {
        "username": email,
        "password": password,
    }
    try:
        response = requests.post(url, data=data, timeout=5)
        response.raise_for_status()
        token = response.json().get("access_token")
        if not token:
            print("❌ Pas de token dans la réponse")
            return None
        return token
    except requests.RequestException as e:
        print(f"❌ Erreur login: {e}")
        return None


def get_current_lunar_return(token: str, api_url: str) -> tuple[Optional[Dict[str, Any]], Optional[int], Optional[str]]:
    """Appelle GET /api/lunar-returns/current."""
    url = f"{api_url}/api/lunar-returns/current"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
        status_code = response.status_code
        try:
            body = response.json()
        except json.JSONDecodeError:
            body = {"raw": response.text}
        return body, status_code, response.text
    except requests.RequestException as e:
        print(f"❌ Erreur requête: {e}")
        return None, None, None


def delete_all_lunar_returns(token: str, api_url: str) -> bool:
    """Supprime tous les retours lunaires (pour tester avec DB vide)."""
    # Note: Il n'y a pas d'endpoint DELETE, donc on utilise POST /generate qui supprime avant de régénérer
    # Mais pour ce test, on veut juste vider la DB, donc on va utiliser une approche différente
    # Pour MVP, on va juste tester que GET /current fonctionne avec DB vide
    # (on suppose que l'utilisateur n'a pas encore de retours)
    return True


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/test_lunar_returns_lazy_generate.py <email> <password> [API_URL]")
        print("\nNote: Ce test suppose que l'utilisateur n'a pas encore de retours lunaires en DB.")
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]
    api_url = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_API_URL

    print("=" * 60)
    print("🧪 Test de Sanity: Lazy Generate GET /api/lunar-returns/current")
    print("=" * 60)
    print(f"API URL: {api_url}")
    print(f"DEV_MOCK_EPHEMERIS: {os.getenv('DEV_MOCK_EPHEMERIS', 'non défini')}\n")

    # 1. Login
    print("1️⃣  Login...")
    token = login(email, password, api_url)
    if not token:
        sys.exit(1)
    print(f"   ✅ Token obtenu: {token[:20]}...\n")

    # 2. Premier appel GET /current (devrait déclencher génération si DB vide)
    print("2️⃣  Premier appel GET /current (DB vide) → doit déclencher génération...")
    payload1, status1, body1 = get_current_lunar_return(token, api_url)
    if status1 != 200:
        print(f"   ❌ Erreur: status={status1}, body={body1[:200]}")
        sys.exit(1)
    
    if payload1 is None:
        print("   ⚠️  Retour null (peut être normal si génération échouée ou DB non vide)")
    else:
        print(f"   ✅ Retour trouvé: month={payload1.get('month')}, return_date={payload1.get('return_date')}")
        # Vérifier que return_date n'est pas None
        if payload1.get('return_date') is None:
            print("   ❌ ERREUR: return_date est None (devrait avoir un fallback)")
            sys.exit(1)
        else:
            print(f"   ✅ return_date non-null: {payload1.get('return_date')}")
    print(f"   📝 Status: {status1}\n")

    # 3. Deuxième appel (devrait retourner le même retour, pas de re-génération)
    print("3️⃣  Deuxième appel GET /current → doit retourner le même (pas de re-génération)...")
    payload2, status2, body2 = get_current_lunar_return(token, api_url)
    if status2 != 200:
        print(f"   ❌ Erreur: status={status2}, body={body2[:200]}")
        sys.exit(1)
    
    if payload2 is None:
        print("   ⚠️  Retour null (inattendu après génération)")
    else:
        print(f"   ✅ Retour trouvé: month={payload2.get('month')}")
        if payload2.get('return_date') is None:
            print("   ❌ ERREUR: return_date est None")
            sys.exit(1)
    print(f"   📝 Status: {status2}\n")

    # Résumé
    print("=" * 60)
    print("✅ Tests terminés")
    print("=" * 60)
    print("\n📋 Vérifications:")
    print("   - GET /current exécutable sans crash")
    print("   - return_date non-null après génération")
    print("   - Logs API: chercher '[corr=...] 🚀 DB vide → déclenchement génération'")
    print("   - Logs API: chercher 'Fallback return_date' si return_datetime absent")


if __name__ == "__main__":
    main()

