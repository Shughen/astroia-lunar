#!/usr/bin/env python3
"""
Script de population du batch 01 avec les 10 aspects sun-venus et sun-mars
Généré manuellement dans Claude Code (pas d'appel API)
"""

import json
from datetime import datetime

# Définition des 10 aspects avec leurs interprétations complètes
aspects = [
    {
        "planet1": "sun",
        "planet2": "venus",
        "aspect_type": "conjunction",
        "version_a": {
            "markdown": """# ☌ Conjonction Soleil - Vénus

**En une phrase :** Ton charme devient ton super-pouvoir — tu rayonnes sans effort

## L'énergie de cet aspect

Ce mois-ci, ton identité profonde (Soleil) et ce que tu aimes (Vénus) ne font qu'un. Les gens te sourient plus facilement, les conversations coulent, tu te sens dans ton élément. Ce n'est pas de la chance — c'est ton authenticité qui brille.

## Manifestations concrètes

- **Relations fluides** : Tu trouves les mots justes, les échanges sont chaleureux et sincères
- **Créativité magnétique** : Envie de créer du beau qui te ressemble — et les autres adhèrent
- **Charisme naturel** : En groupe, tu attires l'attention sans forcer, tes idées passent mieux

## Conseil pratique

Lance ce projet créatif qui te trotte dans la tête, ou dis enfin ce que tu repousses. Ton authenticité est ton meilleur atout ce mois-ci.

## Attention

Gare à vouloir plaire à tout prix — ton charme peut te faire dire oui à des choses qui ne te correspondent pas vraiment.""",
            "parsed": {
                "summary": "Ton charme devient ton super-pouvoir — tu rayonnes sans effort",
                "why": [
                    "Les gens te sourient plus facilement, les conversations coulent, tu te sens dans ton élément.",
                    "Ce n'est pas de la chance — c'est ton authenticité qui brille."
                ],
                "manifestation": """Ce mois-ci, ton identité profonde (Soleil) et ce que tu aimes (Vénus) ne font qu'un. Les gens te sourient plus facilement, les conversations coulent, tu te sens dans ton élément. Ce n'est pas de la chance — c'est ton authenticité qui brille.

- **Relations fluides** : Tu trouves les mots justes, les échanges sont chaleureux et sincères
- **Créativité magnétique** : Envie de créer du beau qui te ressemble — et les autres adhèrent
- **Charisme naturel** : En groupe, tu attires l'attention sans forcer, tes idées passent mieux""",
                "advice": "Lance ce projet créatif qui te trotte dans la tête, ou dis enfin ce que tu repousses. Ton authenticité est ton meilleur atout ce mois-ci.",
                "shadow": "Gare à vouloir plaire à tout prix — ton charme peut te faire dire oui à des choses qui ne te correspondent pas vraiment."
            }
        },
        "selected": "a",
        "selection_reason": "Version A avec emprunts à B - Ton engageant, structure universelle"
    },
    # Les 9 autres aspects suivront...
]

# Pour le moment, sauvegarder juste le premier aspect
batch_data = {
    "batch_number": 1,
    "generated_at": datetime.now().isoformat(),
    "pairs": ["sun-venus", "sun-mars"],
    "aspects": aspects,
    "cost_usd": 0,
    "total_tokens": 0
}

with open("data/batches/batch_01.json", "w", encoding="utf-8") as f:
    json.dump(batch_data, f, indent=2, ensure_ascii=False)

print(f"✅ Batch 01 peuplé avec {len(aspects)} aspect(s)")
