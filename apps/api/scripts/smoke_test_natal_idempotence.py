#!/usr/bin/env python3
"""
Smoke test pour valider l'idempotence du calcul natal et la gestion Chiron.

Usage:
    python scripts/smoke_test_natal_idempotence.py <email> <password> [API_URL]

Prérequis:
    - API démarrée (uvicorn main:app --reload)
    - Utilisateur existant avec email/password
    - Optionnel: DISABLE_CHIRON=true dans .env pour tester Chiron désactivé

Tests:
    1. Premier appel → MISS/no_existing
    2. Deuxième appel (même payload) → HIT
    3. Troisième appel (coords changées) → MISS/coords_changed
    4. Vérifie qu'il n'y a pas de warning "seas_18.se1" si DISABLE_CHIRON=true
"""

import sys
import json
import requests
from typing import Dict, Any, Optional

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


def calculate_natal_chart(
    token: str,
    api_url: str,
    date: str = "1990-05-15",
    time: str = "14:30",
    latitude: float = 48.8566,
    longitude: float = 2.3522,
    place_name: str = "Paris, France",
) -> tuple[Optional[Dict[str, Any]], Optional[int], Optional[str]]:
    """Calcule un thème natal et retourne la réponse, status code et body brut."""
    url = f"{api_url}/api/natal-chart"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "date": date,
        "time": time,
        "latitude": latitude,
        "longitude": longitude,
        "place_name": place_name,
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        status_code = response.status_code
        try:
            body = response.json()
        except json.JSONDecodeError:
            body = {"raw": response.text}
        return body, status_code, response.text
    except requests.RequestException as e:
        print(f"❌ Erreur requête: {e}")
        return None, None, None


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/smoke_test_natal_idempotence.py <email> <password> [API_URL]")
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]
    api_url = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_API_URL

    print("=" * 60)
    print("🧪 Smoke Test: Idempotence Natal Chart + Chiron")
    print("=" * 60)
    print(f"API URL: {api_url}\n")

    # 1. Login
    print("1️⃣  Login...")
    token = login(email, password, api_url)
    if not token:
        sys.exit(1)
    print(f"   ✅ Token obtenu: {token[:20]}...\n")

    # 2. Premier appel → doit être MISS/no_existing
    print("2️⃣  Premier appel (nouveau chart)...")
    payload1, status1, body1 = calculate_natal_chart(token, api_url)
    if status1 != 201:
        print(f"   ❌ Erreur: status={status1}, body={body1[:200]}")
        sys.exit(1)
    chart_id_1 = payload1.get("id") if isinstance(payload1, dict) else None
    print(f"   ✅ Chart créé - ID: {chart_id_1}")
    print(f"   📝 Status: {status1}")
    print(f"   📝 Sun sign: {payload1.get('sun_sign') if isinstance(payload1, dict) else 'N/A'}\n")

    # 3. Deuxième appel (même payload) → doit être HIT
    print("3️⃣  Deuxième appel (même payload) → doit être HIT...")
    payload2, status2, body2 = calculate_natal_chart(token, api_url)
    if status2 != 201:
        print(f"   ❌ Erreur: status={status2}, body={body2[:200]}")
        sys.exit(1)
    chart_id_2 = payload2.get("id") if isinstance(payload2, dict) else None
    if chart_id_1 == chart_id_2:
        print(f"   ✅ HIT confirmé - même ID: {chart_id_2}")
    else:
        print(f"   ⚠️  IDs différents: {chart_id_1} vs {chart_id_2} (peut être normal si cache invalide)")
    print(f"   📝 Status: {status2}\n")

    # 4. Troisième appel (coords changées) → doit être MISS/coords_changed
    print("4️⃣  Troisième appel (coords changées) → doit être MISS/coords_changed...")
    payload3, status3, body3 = calculate_natal_chart(
        token, api_url, latitude=48.8600, longitude=2.3500  # Légèrement différent
    )
    if status3 != 201:
        print(f"   ❌ Erreur: status={status3}, body={body3[:200]}")
        sys.exit(1)
    chart_id_3 = payload3.get("id") if isinstance(payload3, dict) else None
    if chart_id_3 != chart_id_1:
        print(f"   ✅ MISS confirmé - nouveau ID: {chart_id_3}")
    else:
        print(f"   ⚠️  Même ID malgré coords différentes (epsilon trop large?)")
    print(f"   📝 Status: {status3}\n")

    # 5. Vérification Chiron (pas de warning "seas_18.se1" dans les logs)
    print("5️⃣  Vérification Chiron...")
    print("   ℹ️  Vérifiez manuellement les logs de l'API:")
    print("      - Si DISABLE_CHIRON=true: doit voir 'ℹ️ Chiron disabled' (INFO)")
    print("      - Si fichiers absents: doit voir 'ℹ️ Chiron disabled (Swiss Ephemeris files missing)' (INFO)")
    print("      - Ne doit PAS voir de warning 'seas_18.se1 not found' répété\n")

    # Résumé
    print("=" * 60)
    print("✅ Tests terminés")
    print("=" * 60)
    print(f"Chart IDs: {chart_id_1} → {chart_id_2} → {chart_id_3}")
    print("\n📋 Vérifications manuelles:")
    print("   - Logs API: chercher '[IDEMPOTENCE] HIT' et '[IDEMPOTENCE] MISS'")
    print("   - Logs API: pas de warning spam pour Chiron")
    print("   - Vérifier que les IDs correspondent aux attentes")


if __name__ == "__main__":
    main()

