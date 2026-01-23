"""
Test de l'endpoint /metrics Prometheus (Task 5.1 - Vague 5)
"""
import pytest
from fastapi.testclient import TestClient


def test_metrics_endpoint_exists():
    """Vérifie que l'endpoint /metrics est monté dans l'app."""
    from main import app

    # Vérifier que l'endpoint /metrics existe dans les routes
    routes = [route.path for route in app.routes]
    assert "/metrics" in routes, "Endpoint /metrics non trouvé dans les routes"


def test_metrics_endpoint_returns_200():
    """Vérifie que l'endpoint /metrics retourne 200 OK."""
    from main import app

    client = TestClient(app)
    response = client.get("/metrics")

    assert response.status_code == 200, f"Status code incorrect: {response.status_code}"


def test_metrics_endpoint_content_type():
    """Vérifie que l'endpoint /metrics retourne le bon Content-Type."""
    from main import app

    client = TestClient(app)
    response = client.get("/metrics")

    content_type = response.headers.get("content-type", "")
    # Prometheus metrics peuvent être text/plain ou text/plain; version=0.0.4
    assert "text/plain" in content_type, f"Content-Type incorrect: {content_type}"


def test_metrics_endpoint_contains_lunar_metrics():
    """Vérifie que l'endpoint /metrics contient les métriques lunaires."""
    from main import app

    client = TestClient(app)
    response = client.get("/metrics")

    text = response.text

    # Métriques attendues (définies dans lunar_interpretation_generator.py)
    expected_metrics = [
        "lunar_interpretation_generated_total",
        "lunar_interpretation_cache_hit_total",
        "lunar_interpretation_fallback_total",
        "lunar_interpretation_duration_seconds",
        "lunar_active_generations"
    ]

    for metric in expected_metrics:
        assert metric in text, f"Métrique manquante: {metric}"


def test_metrics_endpoint_contains_migration_info():
    """Vérifie que l'endpoint /metrics contient la métrique migration_info."""
    from main import app

    client = TestClient(app)
    response = client.get("/metrics")

    text = response.text

    # Métrique Info créée dans main.py
    assert "lunar_migration_info" in text, "Métrique lunar_migration_info manquante"

    # Vérifier les labels de la métrique Info
    assert 'version="2.0"' in text or 'version="2"' in text, "Label version manquant"
    assert 'templates_count="1728"' in text, "Label templates_count manquant"
    assert 'migration_date="2026-01-23"' in text, "Label migration_date manquant"
    assert 'architecture="4_layers"' in text, "Label architecture manquant"


def test_metrics_endpoint_prometheus_format():
    """Vérifie que le format de sortie est bien Prometheus text format."""
    from main import app

    client = TestClient(app)
    response = client.get("/metrics")

    text = response.text

    # Format Prometheus: lignes HELP et TYPE avant les métriques
    assert "# HELP" in text, "Format Prometheus invalide: # HELP manquant"
    assert "# TYPE" in text, "Format Prometheus invalide: # TYPE manquant"

    # Vérifier qu'il y a bien des valeurs de métriques
    lines = [line for line in text.split('\n') if line and not line.startswith('#')]
    assert len(lines) > 0, "Aucune métrique exposée"


@pytest.mark.parametrize("metric_name,metric_type", [
    ("lunar_interpretation_generated_total", "counter"),
    ("lunar_interpretation_cache_hit_total", "counter"),
    ("lunar_interpretation_fallback_total", "counter"),
    ("lunar_interpretation_duration_seconds", "histogram"),
    ("lunar_active_generations", "gauge"),
])
def test_metrics_types(metric_name, metric_type):
    """Vérifie que les métriques ont le bon type Prometheus."""
    from main import app

    client = TestClient(app)
    response = client.get("/metrics")

    text = response.text

    # Chercher la ligne TYPE pour cette métrique
    expected_type_line = f"# TYPE {metric_name} {metric_type}"
    assert expected_type_line in text, f"Type incorrect pour {metric_name}: attendu {metric_type}"
