#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 20 en base de données (version=5)
Généré manuellement - Paires: jupiter-neptune (5 aspects) + jupiter-pluto (5 aspects)
Extension : aspects secondaires 6/8
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

# Les 10 aspects du Batch 20
ASPECTS = [
    # === JUPITER-NEPTUNE (5 aspects) ===
    {
        "planet1": "jupiter",
        "planet2": "neptune",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Jupiter - Neptune

**En une phrase :** Tu crois en l'impossible — tes rêves n'ont plus de limites

## L'énergie de cet aspect

Ton optimisme (Jupiter) fusionne avec ton imaginaire (Neptune) ce mois-ci. Tu crois que tout est possible. Tes visions sont vastes, spirituelles, parfois utopiques. Tu vois le divin partout, ou tu ne vois que des illusions.

## Manifestations concrètes

- **Foi infinie** : Tu crois en des choses que personne ne croit
- **Visions inspirées** : Tes rêves te montrent des possibilités réelles
- **Naïveté dangereuse** : Tu te fais avoir parce que tu veux trop croire

## Conseil pratique

Mets ton idéalisme au service d'une cause — humanitaire, spirituelle, artistique — tu as la foi pour changer le monde.

## Attention

Gare aux illusions — Jupiter-Neptune peut te faire croire n'importe quoi."""
    },
    {
        "planet1": "jupiter",
        "planet2": "neptune",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Jupiter - Neptune

**En une phrase :** Tu veux croire mais tu te mens — impossible de savoir ce qui est vrai

## L'énergie de cet aspect

Ton besoin de sens (Jupiter) s'oppose à tes illusions (Neptune) ce mois-ci. Tu cherches la vérité mais tu te noies dans les croyances. Tu veux grandir mais tu fuis dans le rêve. Cette tension crée de la confusion, parfois de l'évasion.

## Manifestations concrètes

- **Croyances contradictoires** : Tu ne sais plus ce qui est vrai
- **Fuite spirituelle** : Tu utilises la spiritualité pour échapper au réel
- **Générosité naïve** : Tu donnes à ceux qui profitent de toi

## Conseil pratique

Vérifie tes croyances — demande-toi : est-ce que j'y crois parce que c'est vrai ou parce que je veux y croire ?

## Attention

Attention aux gourous — Neptune attire ceux qui profitent de ta foi."""
    },
    {
        "planet1": "jupiter",
        "planet2": "neptune",
        "aspect_type": "square",
        "content": """# □ Carré Jupiter - Neptune

**En une phrase :** Tu promets l'impossible puis tu disparais — personne ne te fait confiance

## L'énergie de cet aspect

Ton optimisme (Jupiter) entre en conflit avec tes illusions (Neptune) ce mois-ci. Tu t'engages dans des projets irréalistes. Tu promets ce que tu ne peux pas tenir. Cette guerre intérieure crée des déceptions, des mensonges.

## Manifestations concrètes

- **Promesses vides** : Tu dis que tu vas faire puis tu ne fais pas
- **Projets utopiques** : Tes idées sont belles mais impossibles
- **Mensonges pieux** : Tu te mens à toi-même pour rester positif

## Conseil pratique

Avant de promettre quoi que ce soit, demande-toi : est-ce que je peux vraiment le faire ?

## Attention

Gare à la crédibilité — à force de promettre sans tenir, plus personne ne te croira."""
    },
    {
        "planet1": "jupiter",
        "planet2": "neptune",
        "aspect_type": "trine",
        "content": """# △ Trigone Jupiter - Neptune

**En une phrase :** Ta foi devient magie — tu crées l'impossible avec grâce

## L'énergie de cet aspect

Ton optimisme (Jupiter) et ton imaginaire (Neptune) s'harmonisent ce mois-ci. Tu crois en tes rêves ET tu sais les matérialiser. Ta vision inspire les autres. Ton art touche l'âme. Tu vis ta spiritualité.

## Manifestations concrètes

- **Foi créatrice** : Ce que tu imagines se manifeste naturellement
- **Inspiration contagieuse** : Tes visions élèvent les autres
- **Spiritualité vivante** : Ta foi n'est pas dogme, elle est expérience

## Conseil pratique

Crée une œuvre qui porte ta vision — film, livre, mouvement — tu peux inspirer le monde.

## Attention

Attention au détachement — parfois il faut aussi rester dans le réel."""
    },
    {
        "planet1": "jupiter",
        "planet2": "neptune",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Jupiter - Neptune

**En une phrase :** Tu explores le mystère avec confiance — chaque intuition t'ouvre

## L'énergie de cet aspect

Ton besoin de sens (Jupiter) et ton intuition (Neptune) se complètent ce mois-ci. Tu comprends ce qui dépasse la raison. Tes croyances s'enrichissent d'expériences. Tu grandis spirituellement.

## Manifestations concrètes

- **Foi éclairée** : Tu crois sans dogmatisme, tu explores sans te perdre
- **Générosité inspirée** : Tu aides les autres avec discernement
- **Visions justes** : Tes intuitions sur l'avenir se confirment

## Conseil pratique

Explore une pratique spirituelle qui te parle — méditation, rituels, art sacré — ta foi peut s'incarner.

## Attention

Gare à l'évasion douce — Neptune peut te faire fuir le réel au nom de la spiritualité."""
    },

    # === JUPITER-PLUTO (5 aspects) ===
    {
        "planet1": "jupiter",
        "planet2": "pluto",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Jupiter - Pluton

**En une phrase :** Ton ambition devient obsession — tu veux le pouvoir total

## L'énergie de cet aspect

Ton besoin d'expansion (Jupiter) fusionne avec ton besoin de pouvoir (Pluton) ce mois-ci. Tu veux réussir, dominer, transformer le monde. Ton ambition est démesurée. Tu peux créer quelque chose d'énorme ou tout détruire par hubris.

## Manifestations concrètes

- **Ambition démesurée** : Tu vises le sommet, rien de moins
- **Pouvoir magnétique** : Les gens sentent ta puissance, ils te suivent ou te craignent
- **Transformation radicale** : Ce que tu touches change profondément

## Conseil pratique

Utilise ce pouvoir pour transformer en grand — entreprise, mouvement, révolution — tu as la force pour changer le monde.

## Attention

Gare à l'hubris — Jupiter-Pluton peut te faire croire que tu es invincible."""
    },
    {
        "planet1": "jupiter",
        "planet2": "pluto",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Jupiter - Pluton

**En une phrase :** Tu veux le pouvoir mais tu le crains — tu sabottes ta propre réussite

## L'énergie de cet aspect

Ton désir de grandeur (Jupiter) s'oppose à ta peur du pouvoir (Pluton) ce mois-ci. Tu veux réussir mais tu as peur de ce que ça implique. Dès que tu grandis, tu te sabotes. Cette tension crée de l'auto-sabotage, de la paranoïa.

## Manifestations concrètes

- **Réussite sabotée** : Tu détruis tes succès par peur d'être trop puissant
- **Paranoïa du pouvoir** : Tu crois que les autres veulent te détruire
- **Conflits avec l'autorité** : Tu te bats contre ceux qui ont le pouvoir

## Conseil pratique

Identifie ce qui te fait peur dans le pouvoir — puis demande-toi si cette peur est fondée.

## Attention

Attention à l'autodestruction — Jupiter-Pluton peut te faire détruire ton propre succès."""
    },
    {
        "planet1": "jupiter",
        "planet2": "pluto",
        "aspect_type": "square",
        "content": """# □ Carré Jupiter - Pluton

**En une phrase :** Tu veux tout avoir maintenant — ton avidité te perd

## L'énergie de cet aspect

Ton ambition (Jupiter) entre en conflit avec ton besoin de contrôle (Pluton) ce mois-ci. Tu ne supportes pas d'attendre. Tu veux tout, tout de suite, à tout prix. Cette guerre crée de l'avidité, parfois de la corruption.

## Manifestations concrètes

- **Avidité excessive** : Tu en veux toujours plus, jamais satisfait
- **Manipulation pour réussir** : Tu utilises les autres pour grandir
- **Burn-out d'ambition** : Tu te pousses jusqu'à t'épuiser

## Conseil pratique

Demande-toi : qu'est-ce que j'essaie de prouver ? À qui ? Puis accepte que tu as déjà assez de valeur.

## Attention

Gare à la corruption — Jupiter-Pluton peut te faire perdre ton intégrité pour le pouvoir."""
    },
    {
        "planet1": "jupiter",
        "planet2": "pluto",
        "aspect_type": "trine",
        "content": """# △ Trigone Jupiter - Pluton

**En une phrase :** Ton ambition devient transformation — tu réussis en profondeur

## L'énergie de cet aspect

Ton besoin de grandeur (Jupiter) et ton pouvoir de transformation (Pluton) collaborent ce mois-ci. Tu arrives à changer les choses en grand. Ton succès a un impact profond. Tu deviens influent naturellement.

## Manifestations concrètes

- **Réussite transformante** : Ce que tu construis change vraiment les choses
- **Leadership naturel** : Les gens te suivent, tu inspires confiance
- **Croissance puissante** : Tu grandis sans te trahir

## Conseil pratique

Lance un projet qui transforme en profondeur — entreprise sociale, mouvement, art engagé — tu peux vraiment changer le monde.

## Attention

Attention à l'ivresse du pouvoir — même harmonieux, Pluton peut corrompre."""
    },
    {
        "planet1": "jupiter",
        "planet2": "pluto",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Jupiter - Pluton

**En une phrase :** Tu découvres ton pouvoir — chaque réussite révèle ta force

## L'énergie de cet aspect

Ton ambition (Jupiter) et ton pouvoir profond (Pluton) se stimulent ce mois-ci. Tu oses viser plus haut. Tu comprends que tu as plus de pouvoir que tu ne pensais. Tu grandis en assumant ta puissance.

## Manifestations concrètes

- **Ambition mesurée** : Tu vises haut sans te perdre
- **Influence progressive** : Ton impact grandit naturellement
- **Résilience accrue** : Les obstacles te renforcent au lieu de t'arrêter

## Conseil pratique

Engage-toi dans un projet ambitieux qui te fait peur — teste ta vraie capacité de transformation.

## Attention

Gare à l'obsession du succès — la réussite n'est pas tout."""
    }
]


async def insert_batch_20():
    """Insère les 10 aspects du Batch 20 en base de données."""

    print(f"=== Insertion Batch 20 ({len(ASPECTS)} aspects) ===\n")

    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    inserted_count = 0

    async with async_session() as session:
        async with session.begin():
            for aspect in ASPECTS:
                planet1 = aspect['planet1']
                planet2 = aspect['planet2']
                aspect_type = aspect['aspect_type']
                content = aspect['content']

                # Normaliser en ordre alphabétique
                p1_norm = planet1.lower().strip()
                p2_norm = planet2.lower().strip()
                if p1_norm > p2_norm:
                    p1_norm, p2_norm = p2_norm, p1_norm

                # Upsert
                stmt = insert(PregeneratedNatalAspect).values(
                    planet1=p1_norm,
                    planet2=p2_norm,
                    aspect_type=aspect_type.lower(),
                    version=5,
                    lang='fr',
                    content=content,
                    length=len(content)
                )

                stmt = stmt.on_conflict_do_update(
                    index_elements=['planet1', 'planet2', 'aspect_type', 'version', 'lang'],
                    set_={
                        'content': stmt.excluded.content,
                        'length': stmt.excluded.length,
                    }
                )

                await session.execute(stmt)
                inserted_count += 1

                print(f"  ✓ {p1_norm} {aspect_type} {p2_norm}")

    await engine.dispose()

    print(f"\n✅ {inserted_count} aspects insérés (version=5, lang=fr)")

    # Vérifier le total
    await check_total_in_db()


async def check_total_in_db():
    """Vérifie le nombre total d'aspects v5 en BD."""
    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        from sqlalchemy import select, func
        result = await session.execute(
            select(func.count()).select_from(PregeneratedNatalAspect).where(
                PregeneratedNatalAspect.version == 5,
                PregeneratedNatalAspect.lang == 'fr'
            )
        )
        count = result.scalar()

    await engine.dispose()

    print(f"🔍 Vérification BD : {count} aspects version=5 lang=fr")
    print(f"📊 Progression aspects secondaires : {count - 130}/80 aspects ({round((count - 130)/80*100, 1)}%)")


if __name__ == '__main__':
    asyncio.run(insert_batch_20())
