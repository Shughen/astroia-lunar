---
description: Scaffolder une nouvelle route FastAPI
---

# Objectif

Créer une nouvelle route API FastAPI en suivant les patterns établis du projet Astroia. Génère le fichier route + fichier test associé.

# Contexte à Charger

- `apps/api/routes/lunar_returns.py` — Pattern de référence (route complète)
- `apps/api/main.py:1-50` — Registration des routers
- `apps/api/docs/CONTRIBUTING.md` — Conventions coding

# Rôle

Tu es un architecte FastAPI. Tu crées des routes suivant strictement les patterns établis du projet.

# Pattern Route Standard

```python
"""
Route description.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import Optional
import structlog

from database import get_db
from routes.auth import get_current_user
from models.user import User

logger = structlog.get_logger(__name__)

router = APIRouter(prefix="/new-route", tags=["new-route"])


class ItemCreate(BaseModel):
    """Request schema."""
    name: str
    description: Optional[str] = None


class ItemResponse(BaseModel):
    """Response schema."""
    id: int
    name: str

    class Config:
        from_attributes = True


@router.get("/", response_model=list[ItemResponse])
async def get_items(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get all items for current user."""
    logger.info("get_items", user_id=current_user.id)
    # Implementation
    return []


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(
    item: ItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Create a new item."""
    logger.info("create_item", user_id=current_user.id, item_name=item.name)
    # Implementation
    pass
```

# Contraintes

- TOUJOURS : Auth JWT via `Depends(get_current_user)`
- TOUJOURS : Logging structlog
- TOUJOURS : Type hints complets
- TOUJOURS : Docstrings sur chaque endpoint
- TOUJOURS : Pydantic schemas pour request/response
- TOUJOURS : Créer test associé `tests/test_<name>.py`
- TOUJOURS : Ajouter router dans `main.py`

# Workflow

1. Demander nom de la route et endpoints souhaités
2. Créer `apps/api/routes/<name>.py` avec pattern
3. Créer `apps/api/tests/test_<name>.py`
4. Ajouter import + include_router dans `main.py`
5. Exécuter `pytest tests/test_<name>.py -v`

# Exemples d'Utilisation

```
/api:route notifications    → Créer routes/notifications.py
/api:route user-settings    → Créer routes/user_settings.py
```

# v1.0 - 2026-01-25
