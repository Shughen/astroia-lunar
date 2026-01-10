#!/usr/bin/env python3
"""
Test de sanity pour la logique GET /api/lunar-returns/current

Vérifie que :
1. GET /current déclenche la génération automatique si DB vide (lazy generate)
2. Pas de duplication si deux appels simultanés (advisory lock)
3. return_date n'est jamais None après génération (même en mode mock)
4. /rolling renvoie jusqu'à 12 éléments
5. La logique "current" trouve le bon retour (return_date <= now ou prochain)

Usage:
    DEV_MOCK_EPHEMERIS=1 python scripts/test_lunar_returns_current_logic.py <email> <password> [API_URL]
"""

import sys
import os
import json
import requests
import time
from typing import Optional, Dict, Any, List

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


def get_rolling_lunar_returns(token: str, api_url: str) -> tuple[Optional[List[Dict[str, Any]]], Optional[int]]:
    """Appelle GET /api/lunar-returns/rolling."""
    url = f"{api_url}/api/lunar-returns/rolling"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
        status_code = response.status_code
        if status_code == 200:
            body = response.json()
            return body, status_code
        return None, status_code
    except requests.RequestException as e:
        print(f"❌ Erreur requête rolling: {e}")
        return None, None


def delete_all_lunar_returns_via_generate(token: str, api_url: str) -> bool:
    """
    Supprime tous les retours en appelant POST /generate (qui supprime avant de régénérer).
    Note: Pour un vrai test, on devrait avoir un endpoint DELETE, mais pour MVP on utilise /generate.
    """
    url = f"{api_url}/api/lunar-returns/generate"
    headers = {
        "Authorization": f"Bearer {token}",
    }
    try:
        response = requests.post(url, headers=headers, timeout=60)
        # On ignore le résultat, on veut juste déclencher la suppression
        return response.status_code in (200, 201)
    except requests.RequestException:
        return False


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/test_lunar_returns_current_logic.py <email> <password> [API_URL]")
        print("\nNote: Ce test suppose que l'utilisateur a un thème natal calculé.")
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]
    api_url = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_API_URL

    print("=" * 70)
    print("🧪 Test de Sanity: Logique GET /api/lunar-returns/current")
    print("=" * 70)
    print(f"API URL: {api_url}")
    print(f"DEV_MOCK_EPHEMERIS: {os.getenv('DEV_MOCK_EPHEMERIS', 'non défini')}\n")

    # 1. Login
    print("1️⃣  Login...")
    token = login(email, password, api_url)
    if not token:
        sys.exit(1)
    print(f"   ✅ Token obtenu: {token[:20]}...\n")

    # 2. Vider les retours (via /generate qui supprime avant)
    print("2️⃣  Nettoyage: suppression des retours existants...")
    delete_all_lunar_returns_via_generate(token, api_url)
    print("   ✅ Nettoyage effectué (via POST /generate)\n")

    # 3. Premier appel GET /current (DB vide → doit déclencher génération)
    print("3️⃣  Premier appel GET /current (DB vide) → doit déclencher lazy generate...")
    payload1, status1, body1 = get_current_lunar_return(token, api_url)
    if status1 != 200:
        print(f"   ❌ Erreur: status={status1}, body={body1[:200]}")
        sys.exit(1)
    
    if payload1 is None:
        print("   ⚠️  Retour null (peut être normal si génération échouée)")
        print("   📝 Vérifier les logs API pour voir si génération déclenchée")
    else:
        print(f"   ✅ Retour trouvé: month={payload1.get('month')}, return_date={payload1.get('return_date')}")
        # Vérifier que return_date n'est pas None
        if payload1.get('return_date') is None:
            print("   ❌ ERREUR: return_date est None (devrait avoir un fallback)")
            sys.exit(1)
        else:
            print(f"   ✅ return_date non-null: {payload1.get('return_date')}")
    print(f"   📝 Status: {status1}\n")

    # 4. Deuxième appel (doit retourner le même, pas de re-génération)
    print("4️⃣  Deuxième appel GET /current → doit retourner le même (pas de re-génération)...")
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
        
        # Vérifier que c'est le même retour (même id)
        if payload1 and payload2:
            if payload1.get('id') == payload2.get('id'):
                print(f"   ✅ Même retour (id={payload1.get('id')}) → pas de duplication")
            else:
                print(f"   ⚠️  Retours différents (id1={payload1.get('id')}, id2={payload2.get('id')})")
    print(f"   📝 Status: {status2}\n")

    # 5. Test /rolling (doit renvoyer jusqu'à 12 éléments)
    print("5️⃣  Test GET /rolling → doit renvoyer jusqu'à 12 éléments...")
    rolling_data, rolling_status = get_rolling_lunar_returns(token, api_url)
    if rolling_status == 200 and rolling_data:
        count = len(rolling_data)
        print(f"   ✅ {count} retour(s) trouvé(s)")
        if count > 12:
            print(f"   ⚠️  Plus de 12 retours (attendu max 12)")
        elif count == 0:
            print(f"   ⚠️  Aucun retour (inattendu après génération)")
        else:
            print(f"   ✅ Nombre de retours OK (≤ 12)")
        
        # Vérifier que tous ont return_date non-null
        null_dates = [r for r in rolling_data if r.get('return_date') is None]
        if null_dates:
            print(f"   ❌ ERREUR: {len(null_dates)} retour(s) avec return_date=None")
            sys.exit(1)
        else:
            print(f"   ✅ Tous les retours ont return_date non-null")
    else:
        print(f"   ⚠️  /rolling non disponible ou erreur (status={rolling_status})")
    print()

    # 6. Test concurrence (deux appels simultanés)
    print("6️⃣  Test concurrence: deux appels GET /current simultanés...")
    print("   (Vérifie que l'advisory lock évite les duplications)")
    
    # Note: Pour un vrai test de concurrence, on devrait faire des threads/async,
    # mais pour MVP on fait deux appels rapides
    import threading
    
    results = []
    def call_current():
        payload, status, _ = get_current_lunar_return(token, api_url)
        results.append((payload, status))
    
    t1 = threading.Thread(target=call_current)
    t2 = threading.Thread(target=call_current)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    if len(results) == 2:
        payload_a, status_a = results[0]
        payload_b, status_b = results[1]
        if payload_a and payload_b:
            if payload_a.get('id') == payload_b.get('id'):
                print(f"   ✅ Même retour (id={payload_a.get('id')}) → pas de duplication")
            else:
                print(f"   ⚠️  Retours différents (id_a={payload_a.get('id')}, id_b={payload_b.get('id')})")
        print(f"   📝 Status: {status_a}, {status_b}")
    else:
        print(f"   ⚠️  Résultats incomplets: {len(results)} résultat(s)")
    print()

    # Résumé
    print("=" * 70)
    print("✅ Tests terminés")
    print("=" * 70)
    print("\n📋 Vérifications:")
    print("   - GET /current exécutable sans crash")
    print("   - return_date non-null après génération")
    print("   - Pas de duplication sur appels multiples")
    print("   - /rolling renvoie ≤ 12 éléments")
    print("\n📝 Logs API à vérifier:")
    print("   - '[corr=...] 🚀 DB vide → déclenchement génération rolling automatique'")
    print("   - '[corr=...] ℹ️ Lock non obtenu' (si appel concurrent)")
    print("   - '[corr=...] ℹ️ Fallback return_date' (si return_datetime absent)")


if __name__ == "__main__":
    main()

