#!/usr/bin/env python3
"""
Script de test pour vérifier que l'endpoint /metrics Prometheus fonctionne correctement.
"""
import asyncio
import httpx
import subprocess
import time
import sys

API_URL = "http://localhost:8000"
STARTUP_TIMEOUT = 15  # secondes


async def wait_for_api():
    """Attend que l'API soit prête à recevoir des requêtes."""
    print("⏳ Attente du démarrage de l'API...")
    start = time.time()

    async with httpx.AsyncClient() as client:
        while time.time() - start < STARTUP_TIMEOUT:
            try:
                response = await client.get(f"{API_URL}/health", timeout=2.0)
                if response.status_code == 200:
                    print(f"✅ API prête après {time.time() - start:.1f}s")
                    return True
            except (httpx.ConnectError, httpx.ReadTimeout):
                await asyncio.sleep(0.5)
                continue

    print(f"❌ API non prête après {STARTUP_TIMEOUT}s")
    return False


async def test_metrics_endpoint():
    """Teste l'endpoint /metrics Prometheus."""
    print("\n🧪 Test endpoint /metrics...")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{API_URL}/metrics", timeout=5.0)

            if response.status_code != 200:
                print(f"❌ Status code incorrect: {response.status_code}")
                print(f"Response: {response.text[:200]}")
                return False

            # Vérifier le content-type Prometheus
            content_type = response.headers.get("content-type", "")
            if "text/plain" not in content_type and "text/plain; version=0.0.4" not in content_type:
                print(f"⚠️  Content-Type inattendu: {content_type}")
                # Pas bloquant car certaines versions de prometheus_client peuvent varier

            # Vérifier présence des métriques attendues
            text = response.text

            expected_metrics = [
                "lunar_interpretation_generated_total",
                "lunar_interpretation_cache_hit_total",
                "lunar_interpretation_fallback_total",
                "lunar_interpretation_duration_seconds",
                "lunar_active_generations",
                "lunar_migration_info"
            ]

            missing_metrics = []
            for metric in expected_metrics:
                if metric not in text:
                    missing_metrics.append(metric)

            if missing_metrics:
                print(f"❌ Métriques manquantes: {missing_metrics}")
                print(f"\nContenu /metrics (200 premiers caractères):")
                print(text[:200])
                return False

            print("✅ Endpoint /metrics OK")
            print(f"✅ Toutes les métriques présentes ({len(expected_metrics)} métriques)")

            # Afficher aperçu des métriques
            print("\n📊 Aperçu des métriques exposées:")
            for line in text.split('\n')[:20]:
                if line.startswith('#') or line.strip() == '':
                    continue
                print(f"  {line}")

            return True

        except Exception as e:
            print(f"❌ Erreur lors du test: {e}")
            return False


async def main():
    """Test principal."""
    print("=" * 60)
    print("Test endpoint /metrics Prometheus (Task 5.1)")
    print("=" * 60)

    # Vérifier si l'API est déjà démarrée
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/health", timeout=2.0)
            api_running = response.status_code == 200
    except:
        api_running = False

    if api_running:
        print("ℹ️  API déjà en cours d'exécution")
        success = await test_metrics_endpoint()
    else:
        print("ℹ️  API non démarrée, démarrage manuel nécessaire")
        print("\n⚠️  Pour tester, exécutez dans un terminal séparé:")
        print("   cd apps/api && uvicorn main:app --reload")
        print("\nPuis relancez ce script.")
        success = False

    print("\n" + "=" * 60)
    if success:
        print("✅ Test RÉUSSI - Endpoint /metrics fonctionnel")
        return 0
    else:
        print("❌ Test ÉCHOUÉ - Vérifier les logs ci-dessus")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
