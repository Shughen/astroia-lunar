"""
Tests unitaires pour le endpoint /health
"""

import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_health_endpoint():
    """Test du endpoint /health"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
        
        assert response.status_code == 200
        data = response.json()
        
        assert "status" in data
        assert "checks" in data
        assert data["status"] in ["healthy", "degraded"]


@pytest.mark.asyncio
async def test_root_endpoint():
    """Test du endpoint root /"""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        
        assert data["app"] == "Astroia Lunar API"
        assert data["status"] == "running"
        assert "docs" in data

