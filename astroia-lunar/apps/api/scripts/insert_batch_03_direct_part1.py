#!/usr/bin/env python3
"""
Insertion directe des 15 aspects du Batch 3 en base de données (version=5)
Partie 1: Moon-Uranus (5 aspects)
Généré manuellement dans Claude Code
"""

import sys
import asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.dialects.postgresql import insert
from models.pregenerated_natal_aspect import PregeneratedNatalAspect
from config import Settings

settings = Settings()

# Aspects moon-uranus (5 aspects)
ASPECTS_MOON_URANUS = [
    ("conjunction", """# ☌ Conjonction Lune - Uranus

**En une phrase :** Tes émotions deviennent électriques — instabilité créative

## L'énergie de cet aspect

Tes besoins émotionnels (Lune) et ton besoin de liberté (Uranus) fusionnent ce mois-ci. Résultat : une hypersensibilité aux changements, des réactions imprévisibles, et une envie soudaine de tout réinventer. Tu passes de l'excitation à l'anxiété en un claquement de doigts. Cette énergie est créative mais instable — elle demande un ancrage.

## Manifestations concrètes

- **Humeurs changeantes** : Le matin tu es zen, l'après-midi tu as besoin de fuir et de tout changer
- **Intuitions fulgurantes** : Des insights émotionnels qui arrivent comme l'éclair et bouleversent ta vision
- **Besoin de rupture** : Envie de couper avec les routines émotionnelles, les habitudes sécurisantes

## Conseil pratique

Note tes intuitions soudaines mais attends 24h avant d'agir. L'électricité émotionnelle est juste, mais le timing peut être erratique.

## Attention

Gare à saboter tes bases émotionnelles juste parce que tu t'ennuies. L'agitation intérieure n'est pas toujours un signal de danger."""),
]

# Suite dans insert_batch_03_direct_part2.py
