#!/usr/bin/env python3
"""
Test de concurrence pour GET /api/lunar-returns/current

Vérifie que:
- Lazy generate si DB vide
- Pas de duplication (une seule génération)
- Advisory lock fonctionne (appels concurrents ne génèrent pas 2 fois)
- return_date jamais null
- 2 appels simultanés renvoient le même lunar_return (même id) après génération

Usage (JWT):
    export DEV_MOCK_EPHEMERIS=1
    export LUNAR_RETURNS_DEV_DELAY_MS=2000
    python scripts/test_lunar_returns_concurrency.py \
      --email test@example.com \
      --password password \
      --api-url http://127.0.0.1:8000 \
      [--concurrent N] [--delay-ms MS]

Usage (DEV_AUTH_BYPASS):
    export DEV_MOCK_EPHEMERIS=1
    export DEV_AUTH_BYPASS=1
    export DEV_USER_ID="dev-remi"  # UUID string, int string, ou autre
    export LUNAR_RETURNS_DEV_DELAY_MS=2000
    python scripts/test_lunar_returns_concurrency.py \
      --dev-user-id "dev-remi" \
      --api-url http://127.0.0.1:8000 \
      [--concurrent N] [--delay-ms MS]
"""

import sys
import os
import asyncio
import argparse
import json
from typing import Optional, Dict, Any, List, Tuple
import aiohttp


# Configuration par défaut
DEFAULT_API_URL = "http://127.0.0.1:8000"
DEFAULT_CONCURRENT = 10
DEFAULT_DELAY_MS = 2000


async def login(session: aiohttp.ClientSession, email: str, password: str, api_url: str) -> Optional[str]:
    """Login et récupère le token JWT."""
    url = f"{api_url}/api/auth/login"
    data = {
        "username": email,
        "password": password,
    }
    try:
        async with session.post(url, data=data, timeout=aiohttp.ClientTimeout(total=5)) as response:
            response.raise_for_status()
            result = await response.json()
            token = result.get("access_token")
            if not token:
                print("❌ Pas de token dans la réponse")
                return None
            return token
    except Exception as e:
        print(f"❌ Erreur login: {e}")
        return None


def _build_dev_headers(dev_user_id: str) -> Dict[str, str]:
    """
    Construit les headers DEV_AUTH_BYPASS selon le type de dev_user_id.
    
    Args:
        dev_user_id: UUID string, int string, ou autre string
    
    Returns:
        Dict avec les headers appropriés
    """
    headers = {}
    
    # Vérifier si c'est un UUID (format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
    import re
    uuid_pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
    
    # Vérifier si c'est strictement numérique (int)
    is_numeric = dev_user_id.isdigit()
    is_uuid = bool(uuid_pattern.match(dev_user_id))
    
    if is_uuid or not is_numeric:
        # UUID ou string non-numérique => X-Dev-External-Id
        headers["X-Dev-External-Id"] = dev_user_id
    else:
        # Strictement numérique => X-Dev-User-Id (lightweight)
        headers["X-Dev-User-Id"] = dev_user_id
    
    return headers


async def get_current_lunar_return(
    session: aiohttp.ClientSession,
    token: Optional[str],
    api_url: str,
    dev_user_id: Optional[str] = None,
    request_id: int = 0,
    verbose: bool = False
) -> Tuple[Optional[Dict[str, Any]], Optional[int], int]:
    """
    Appelle GET /api/lunar-returns/current.
    
    Args:
        dev_user_id: UUID string ou int string pour DEV_AUTH_BYPASS
        verbose: Afficher les détails de la requête
    
    Returns:
        (payload, status_code, request_id)
    """
    url = f"{api_url}/api/lunar-returns/current"
    headers = {}
    
    if token:
        headers["Authorization"] = f"Bearer {token}"
    elif dev_user_id:
        # Mode DEV_AUTH_BYPASS: construire headers selon type
        headers.update(_build_dev_headers(dev_user_id))
    
    if verbose:
        print(f"🔍 [req={request_id}] GET {url}")
        print(f"   Headers: {json.dumps(headers, indent=2)}")
    
    try:
        async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=60)) as response:
            status_code = response.status  # aiohttp utilise .status, pas .status_code
            try:
                body = await response.json()
            except:
                body = {"raw": await response.text()}
            
            if verbose or status_code != 200:
                if status_code != 200:
                    print(f"❌ [req={request_id}] HTTP {status_code}")
                    print(f"   Body: {json.dumps(body, indent=2)}")
                else:
                    lunar_id = body.get("id") if isinstance(body, dict) else None
                    print(f"✅ [req={request_id}] HTTP {status_code} → id={lunar_id}")
            
            return body, status_code, request_id
    except Exception as e:
        print(f"❌ [req={request_id}] Erreur requête: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        return None, None, request_id


async def purge_lunar_returns_dev(
    session: aiohttp.ClientSession,
    token: Optional[str],
    api_url: str,
    dev_user_id: Optional[str] = None
) -> bool:
    """
    Purge les lunar returns via route DEV (si ALLOW_DEV_PURGE=true).
    Sinon, retourne False (l'utilisateur devra purger manuellement).
    """
    url = f"{api_url}/api/lunar-returns/dev/purge"
    headers = {}
    
    if token:
        headers["Authorization"] = f"Bearer {token}"
    elif dev_user_id:
        # Mode DEV_AUTH_BYPASS: construire headers selon type
        headers.update(_build_dev_headers(dev_user_id))
    
    try:
        async with session.post(url, headers=headers, timeout=aiohttp.ClientTimeout(total=10)) as response:
            if response.status == 200:
                return True
            elif response.status == 404:
                print("   ⚠️  Route /dev/purge non disponible (ALLOW_DEV_PURGE=false ou route absente)")
                return False
            else:
                print(f"   ⚠️  Erreur purge: status={response.status}")
                return False
    except Exception as e:
        print(f"   ⚠️  Erreur purge: {e}")
        return False


async def run_concurrent_requests(
    session: aiohttp.ClientSession,
    token: Optional[str],
    api_url: str,
    dev_user_id: Optional[str],
    concurrent: int,
    verbose: bool = False
) -> List[Tuple[Optional[Dict[str, Any]], Optional[int], int]]:
    """
    Lance N requêtes concurrentes vers GET /current.
    
    Args:
        verbose: Afficher les détails de chaque requête
    
    Returns:
        Liste de (payload, status_code, request_id)
    """
    print(f"   🚀 Lancement de {concurrent} requêtes concurrentes...")
    
    tasks = [
        get_current_lunar_return(session, token, api_url, dev_user_id, i, verbose)
        for i in range(concurrent)
    ]
    
    results = await asyncio.gather(*tasks)
    return results


def analyze_results(results: List[Tuple[Optional[Dict[str, Any]], Optional[int], int]], verbose: bool = False) -> Dict[str, Any]:
    """
    Analyse les résultats et retourne un verdict.
    
    Args:
        verbose: Afficher un résumé détaillé
    
    Returns:
        {
            "ok": bool,
            "all_same_id": bool,
            "all_non_null_date": bool,
            "unique_ids": set,
            "null_dates": list,
            "errors": list,
            "summary": str,
            "success_count": int,
            "error_count": int
        }
    """
    verdict = {
        "ok": True,
        "all_same_id": True,
        "all_non_null_date": True,
        "unique_ids": set(),
        "null_dates": [],
        "errors": [],
        "summary": "",
        "success_count": 0,
        "error_count": 0
    }
    
    ids = []
    for payload, status, req_id in results:
        if status != 200:
            error_detail = f"status={status}"
            if payload and isinstance(payload, dict):
                error_detail += f", body={json.dumps(payload, indent=2)[:200]}"
            verdict["errors"].append(f"req_{req_id}: {error_detail}")
            verdict["ok"] = False
            verdict["error_count"] += 1
            continue
        
        if payload is None:
            verdict["errors"].append(f"req_{req_id}: payload null (status={status})")
            verdict["ok"] = False
            verdict["error_count"] += 1
            continue
        
        # Extraire id
        lunar_id = payload.get("id")
        if lunar_id is not None:
            ids.append(lunar_id)
            verdict["unique_ids"].add(lunar_id)
            verdict["success_count"] += 1
        else:
            verdict["errors"].append(f"req_{req_id}: id null")
            verdict["ok"] = False
            verdict["error_count"] += 1
        
        # Vérifier return_date
        return_date = payload.get("return_date")
        if return_date is None:
            verdict["null_dates"].append(f"req_{req_id}: return_date null")
            verdict["all_non_null_date"] = False
            verdict["ok"] = False
    
    # Vérifier que tous les ids sont identiques
    if len(verdict["unique_ids"]) > 1:
        verdict["all_same_id"] = False
        verdict["ok"] = False
    
    # Construire le résumé
    if verdict["ok"]:
        verdict["summary"] = f"✅ OK: {len(ids)} requêtes, même id={ids[0] if ids else 'N/A'}, return_date non-null partout"
    else:
        parts = []
        if not verdict["all_same_id"]:
            parts.append(f"❌ IDs différents: {sorted(verdict['unique_ids'])}")
        if not verdict["all_non_null_date"]:
            parts.append(f"❌ return_date null: {verdict['null_dates']}")
        if verdict["errors"]:
            parts.append(f"❌ Erreurs: {verdict['errors']}")
        verdict["summary"] = " | ".join(parts)
    
    # Résumé détaillé si verbose
    if verbose:
        print(f"\n📊 Résumé détaillé:")
        print(f"   Succès: {verdict['success_count']}/{len(results)}")
        print(f"   Erreurs: {verdict['error_count']}/{len(results)}")
        if verdict["unique_ids"]:
            print(f"   IDs uniques: {sorted(verdict['unique_ids'])}")
        if verdict["errors"]:
            print(f"   Détails erreurs: {verdict['errors']}")
    
    return verdict


async def main():
    parser = argparse.ArgumentParser(
        description="Test de concurrence pour GET /api/lunar-returns/current"
    )
    parser.add_argument("--api-url", type=str, default=DEFAULT_API_URL, help=f"URL API (défaut: {DEFAULT_API_URL})")
    parser.add_argument("--email", type=str, help="Email pour login (requis en mode JWT)")
    parser.add_argument("--password", type=str, help="Password pour login (requis en mode JWT)")
    parser.add_argument("--dev-user-id", type=str, help="User ID (UUID string ou int) pour DEV_AUTH_BYPASS")
    parser.add_argument("--concurrent", type=int, default=DEFAULT_CONCURRENT, help=f"Nombre de requêtes concurrentes (défaut: {DEFAULT_CONCURRENT})")
    parser.add_argument("--delay-ms", type=int, default=None, help="Override LUNAR_RETURNS_DEV_DELAY_MS (ms)")
    parser.add_argument("--no-purge", action="store_true", help="Ne pas purger les lunar returns avant test")
    parser.add_argument("--verbose", "-v", action="store_true", help="Mode verbose: afficher URL, headers, codes HTTP et body en cas d'erreur")
    
    args = parser.parse_args()
    
    # Détecter le mode: DEV_AUTH_BYPASS si env var truthy OU --dev-user-id fourni
    env_bypass = os.getenv("DEV_AUTH_BYPASS", "").lower() in ("1", "true", "yes", "on")
    dev_user_id = args.dev_user_id or os.getenv("DEV_USER_ID", None)
    dev_auth_bypass = env_bypass or (dev_user_id is not None)
    
    # Validation: en mode JWT, email/password requis
    if not dev_auth_bypass:
        if not args.email or not args.password:
            print("❌ Erreur: --email et --password requis en mode JWT")
            print("   Ou utilisez DEV_AUTH_BYPASS=1 avec --dev-user-id")
            sys.exit(1)
    
    # Vérifier delay
    delay_ms = args.delay_ms if args.delay_ms is not None else int(os.getenv("LUNAR_RETURNS_DEV_DELAY_MS", "0"))
    if delay_ms == 0:
        print("⚠️  LUNAR_RETURNS_DEV_DELAY_MS=0 (ou non défini)")
        print("   Pour observer le lock, définir: export LUNAR_RETURNS_DEV_DELAY_MS=2000")
        response = input("   Continuer quand même? (y/N): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    # Construire message de mode
    mode_reasons = []
    if env_bypass:
        mode_reasons.append(f"DEV_AUTH_BYPASS={os.getenv('DEV_AUTH_BYPASS')}")
    if args.dev_user_id:
        mode_reasons.append(f"--dev-user-id={args.dev_user_id}")
    elif os.getenv("DEV_USER_ID"):
        mode_reasons.append(f"DEV_USER_ID={os.getenv('DEV_USER_ID')}")
    
    mode_str = "DEV_AUTH_BYPASS"
    if mode_reasons:
        mode_str += f" ({', '.join(mode_reasons)})"
    
    print("=" * 70)
    print("🧪 Test de Concurrence: GET /api/lunar-returns/current")
    print("=" * 70)
    print(f"API URL: {args.api_url}")
    print(f"Mode: {mode_str if dev_auth_bypass else 'JWT'}")
    if dev_user_id:
        # Détecter le type pour affichage
        is_numeric = dev_user_id.isdigit()
        import re
        uuid_pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
        is_uuid = bool(uuid_pattern.match(dev_user_id))
        if is_uuid:
            dev_type = "UUID"
        elif is_numeric:
            dev_type = "int"
        else:
            dev_type = "string"
        print(f"DEV User ID: {dev_user_id} ({dev_type})")
    print(f"Concurrent requests: {args.concurrent}")
    print(f"DEV delay: {delay_ms}ms")
    print(f"DEV_MOCK_EPHEMERIS: {os.getenv('DEV_MOCK_EPHEMERIS', 'non défini')}\n")
    
    async with aiohttp.ClientSession() as session:
        # 1. Login (uniquement en mode JWT)
        token = None
        if dev_auth_bypass:
            print("1️⃣  Mode DEV_AUTH_BYPASS activé (pas de login)\n")
        else:
            print("1️⃣  Login...")
            token = await login(session, args.email, args.password, args.api_url)
            if not token:
                sys.exit(1)
            print(f"   ✅ Token obtenu: {token[:20]}...\n")
        
        # 2. Purge (optionnel)
        if not args.no_purge:
            print("2️⃣  Purge des lunar returns existants...")
            purged = await purge_lunar_returns_dev(session, token, args.api_url, dev_user_id)
            if purged:
                print("   ✅ Purge effectuée via /dev/purge\n")
            else:
                print("   ⚠️  Purge non disponible (route absente ou ALLOW_DEV_PURGE=false)")
                print("   💡 Purgez manuellement ou créez la route /dev/purge\n")
        else:
            print("2️⃣  Purge ignorée (--no-purge)\n")
        
        # 3. Premier batch concurrent (DB vide → doit déclencher génération)
        print(f"3️⃣  Premier batch: {args.concurrent} requêtes concurrentes (DB vide → lazy generate)...")
        results1 = await run_concurrent_requests(session, token, args.api_url, dev_user_id, args.concurrent, args.verbose)
        verdict1 = analyze_results(results1, args.verbose)
        print(f"   {verdict1['summary']}\n")
        
        # 4. Deuxième batch (après génération → doit retourner même id, pas de re-génération)
        print(f"4️⃣  Deuxième batch: {args.concurrent} requêtes concurrentes (après génération)...")
        await asyncio.sleep(0.5)  # Petit délai pour s'assurer que la génération est terminée
        results2 = await run_concurrent_requests(session, token, args.api_url, dev_user_id, args.concurrent, args.verbose)
        verdict2 = analyze_results(results2, args.verbose)
        print(f"   {verdict2['summary']}\n")
        
        # 5. Vérifier cohérence entre batches
        print("5️⃣  Vérification cohérence entre batches...")
        ids1 = verdict1["unique_ids"]
        ids2 = verdict2["unique_ids"]
        if ids1 and ids2 and ids1 == ids2:
            print(f"   ✅ Même id dans les deux batches: {list(ids1)[0]}")
        elif ids1 and ids2:
            print(f"   ⚠️  IDs différents: batch1={list(ids1)}, batch2={list(ids2)}")
        else:
            print(f"   ⚠️  Impossible de comparer (ids manquants)")
        print()
        
        # Résumé final
        print("=" * 70)
        success = verdict1["ok"] and verdict2["ok"] and (ids1 and ids2 and ids1 == ids2)
        if success:
            print("✅ Tests terminés: SUCCÈS")
        else:
            print("❌ Tests terminés: ÉCHEC")
        print("=" * 70)
        print("\n📋 Vérifications:")
        print(f"   - Premier batch: {'✅' if verdict1['ok'] else '❌'}")
        print(f"   - Deuxième batch: {'✅' if verdict2['ok'] else '❌'}")
        print(f"   - Même id entre batches: {'✅' if ids1 and ids2 and ids1 == ids2 else '❌'}")
        print("\n📝 Logs API à vérifier:")
        print("   - '[corr=...] 🚀 DB vide → déclenchement génération rolling automatique (lock acquis: X)'")
        print("   - '[corr=...] 🧪 DEV delay activé: Xms'")
        print("   - '[corr=...] ℹ️ Lock non obtenu (user_id=X), un autre process génère déjà → skip'")
        print("   - '[corr=...] ✅ Génération rolling automatique terminée: X retour(s)'")
        
        # Exit code: 0 si succès, 1 si échec
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    asyncio.run(main())

