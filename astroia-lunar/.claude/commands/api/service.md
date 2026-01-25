---
description: Scaffolder un nouveau service backend
---

# Objectif

Créer un nouveau service backend en suivant les patterns du projet. Les services encapsulent la logique métier, séparée des routes.

# Contexte à Charger

- `apps/api/services/lunar_returns_service.py` — Pattern service complet
- `apps/api/services/lunar_interpretation_generator.py` — Pattern avec dépendances externes
- `apps/api/docs/CONTRIBUTING.md` — Conventions

# Rôle

Tu es un architecte backend. Tu crées des services découplés, testables, avec injection de dépendances.

# Pattern Service Standard

```python
"""
Service description.

This service handles [domain] logic.
"""
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import structlog

from models.user import User

logger = structlog.get_logger(__name__)


class MyService:
    """Service for handling [domain] operations."""

    def __init__(self, db: AsyncSession):
        """Initialize service with database session."""
        self.db = db

    async def get_item(self, item_id: int, user_id: int) -> Optional[dict]:
        """
        Get item by ID for a specific user.

        Args:
            item_id: The item identifier
            user_id: The user identifier

        Returns:
            Item data or None if not found
        """
        logger.info("get_item", item_id=item_id, user_id=user_id)
        # Implementation
        return None

    async def create_item(self, user_id: int, data: dict) -> dict:
        """
        Create a new item.

        Args:
            user_id: The user identifier
            data: Item data

        Returns:
            Created item data
        """
        logger.info("create_item", user_id=user_id)
        # Implementation
        return {}


# Factory function for dependency injection
def get_my_service(db: AsyncSession) -> MyService:
    """Factory function for FastAPI dependency injection."""
    return MyService(db)
```

# Contraintes

- TOUJOURS : Injection DB via constructeur
- TOUJOURS : Logging structlog avec contexte
- TOUJOURS : Type hints + docstrings Google style
- TOUJOURS : Méthodes async
- TOUJOURS : Factory function pour DI FastAPI
- JAMAIS : Import circulaire avec routes

# Workflow

1. Demander nom du service et responsabilités
2. Créer `apps/api/services/<name>_service.py`
3. Créer test `apps/api/tests/test_<name>_service.py`
4. Exécuter tests

# Exemples d'Utilisation

```
/api:service notification   → Créer services/notification_service.py
/api:service analytics      → Créer services/analytics_service.py
```

# v1.0 - 2026-01-25
