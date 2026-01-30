#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 18 en base de données (version=5)
Généré manuellement - Paires: venus-pluto (5 aspects) + mars-neptune (5 aspects)
Extension : aspects secondaires 4/8
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

# Les 10 aspects du Batch 18
ASPECTS = [
    # === VENUS-PLUTO (5 aspects) ===
    {
        "planet1": "venus",
        "planet2": "pluto",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Vénus - Pluton

**En une phrase :** Ton amour devient obsession — tu aimes jusqu'à consumer

## L'énergie de cet aspect

Ton désir (Vénus) fusionne avec ton besoin de fusion totale (Pluton) ce mois-ci. Quand tu aimes, c'est tout ou rien. Tu veux posséder, être possédé, fusionner jusqu'à disparaître. Tes relations deviennent intenses, parfois toxiques.

## Manifestations concrètes

- **Passion dévorante** : Tu aimes avec une intensité qui fait peur
- **Jalousie extrême** : Tu ne supportes pas l'idée de partager l'autre
- **Transformation affective** : Tes relations te changent en profondeur

## Conseil pratique

Canalise cette intensité dans la création — art, sexualité sacrée, transformation personnelle.

## Attention

Gare à la possession — Pluton peut transformer l'amour en contrôle destructeur."""
    },
    {
        "planet1": "venus",
        "planet2": "pluto",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Vénus - Pluton

**En une phrase :** Tu aimes comme on se bat — chaque relation devient guerre de pouvoir

## L'énergie de cet aspect

Ton besoin d'amour (Vénus) s'oppose à ton besoin de contrôle (Pluton) ce mois-ci. Tes relations deviennent des champs de bataille. Tu veux l'amour mais tu ne supportes pas la vulnérabilité. Cette tension crée des dynamiques toxiques, des ruptures violentes.

## Manifestations concrètes

- **Jeux de pouvoir** : Qui contrôle qui ? C'est la question de chaque relation
- **Attirance pour le danger** : Tu aimes ceux qui peuvent te détruire
- **Ruptures dramatiques** : Tes séparations sont des explosions

## Conseil pratique

Identifie le pattern : est-ce que tu cherches l'amour ou le combat ?

## Attention

Attention aux relations toxiques — Pluton attire ceux qui savent utiliser l'amour comme arme."""
    },
    {
        "planet1": "venus",
        "planet2": "pluto",
        "aspect_type": "square",
        "content": """# □ Carré Vénus - Pluton

**En une phrase :** Tu détruis ce que tu aimes par peur qu'on te détruise d'abord

## L'énergie de cet aspect

Ton désir de relation (Vénus) entre en guerre avec ta peur de la trahison (Pluton) ce mois-ci. Tu aimes mais tu ne fais confiance à personne. Tu testes, tu contrôles, tu sabotes. Cette guerre intérieure détruit tes relations avant qu'elles commencent.

## Manifestations concrètes

- **Méfiance chronique** : Tu cherches la preuve qu'on va te trahir
- **Jalousie destructrice** : Tes soupçons créent ce que tu crains
- **Auto-sabotage** : Tu détruis la relation avant qu'elle te détruise

## Conseil pratique

Demande-toi : qui a détruit ma confiance ? Puis accepte que cette personne n'est pas celle d'aujourd'hui.

## Attention

Gare à la solitude — à force de te protéger, tu crées ce que tu veux éviter."""
    },
    {
        "planet1": "venus",
        "planet2": "pluto",
        "aspect_type": "trine",
        "content": """# △ Trigone Vénus - Pluton

**En une phrase :** Ton amour transforme — tu touches les gens en profondeur

## L'énergie de cet aspect

Ton désir (Vénus) et ta capacité à aller au fond (Pluton) s'harmonisent ce mois-ci. Tes relations ont une profondeur rare. Quand tu aimes, tu transformes l'autre. Ton amour guérit, révèle, libère.

## Manifestations concrètes

- **Amour guérisseur** : Ta présence aide les autres à se réparer
- **Intensité saine** : Tu aimes profondément sans possession
- **Magnétisme naturel** : Les gens sont attirés par ta profondeur

## Conseil pratique

Utilise ton amour comme outil de transformation — thérapeute, coach, artiste, amant conscient.

## Attention

Attention au sauveur — même harmonieux, Pluton peut te faire porter les blessures des autres."""
    },
    {
        "planet1": "venus",
        "planet2": "pluto",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Vénus - Pluton

**En une phrase :** Tu explores les profondeurs de l'amour — rien ne te fait peur

## L'énergie de cet aspect

Ton désir (Vénus) et ton besoin de vérité (Pluton) se stimulent ce mois-ci. Tu veux connaître l'autre vraiment, sans masque. Tes relations deviennent plus authentiques, plus intenses, plus vraies.

## Manifestations concrètes

- **Honnêteté affective** : Tu ne te contentes plus de relations superficielles
- **Sexualité profonde** : Ton désir cherche la connexion, pas juste le plaisir
- **Loyauté intense** : Quand tu aimes, c'est pour de vrai

## Conseil pratique

Engage-toi dans une relation qui demande de la profondeur — pas de faux-semblants, juste la vérité.

## Attention

Gare à l'intensité excessive — parfois il faut aussi laisser place à la légèreté."""
    },

    # === MARS-NEPTUNE (5 aspects) ===
    {
        "planet1": "mars",
        "planet2": "neptune",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mars - Neptune

**En une phrase :** Ton élan se dissout — tu ne sais plus où va ton énergie

## L'énergie de cet aspect

Ton action (Mars) fusionne avec ton imaginaire (Neptune) ce mois-ci. Tes efforts partent dans le flou. Tu veux agir mais tu ne sais pas vers quoi. Ton énergie s'évapore sans produire de résultat concret.

## Manifestations concrètes

- **Fatigue inexpliquée** : Ton énergie fuit, tu ne sais pas pourquoi
- **Actions floues** : Tu commences des choses sans les finir
- **Motivation spirituelle** : Tu agis pour des causes invisibles, idéalistes

## Conseil pratique

Canalise ton énergie dans l'art, la méditation, l'aide aux autres — Mars-Neptune brille dans le subtil.

## Attention

Gare à la passivité — Neptune peut transformer Mars en victime impuissante."""
    },
    {
        "planet1": "mars",
        "planet2": "neptune",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mars - Neptune

**En une phrase :** Tu veux agir mais tu ne sais pas comment — alors tu fuis

## L'énergie de cet aspect

Ton besoin d'action (Mars) s'oppose à ton besoin d'évasion (Neptune) ce mois-ci. Chaque fois que tu veux te battre, tu te sens coupable. Chaque fois que tu veux fuir, tu te sens lâche. Cette tension crée de la confusion, parfois des addictions.

## Manifestations concrètes

- **Fuite face aux conflits** : Tu évites au lieu d'affronter
- **Culpabilité d'agir** : Tu te sens mauvais dès que tu t'affirmes
- **Addictions** : Alcool, drogues, écrans pour échapper à ta colère

## Conseil pratique

Nomme une chose contre laquelle tu veux te battre mais que tu fuis — puis fais un pas vers elle.

## Attention

Attention aux fuites — Neptune peut te faire éviter les conflits nécessaires jusqu'à ce qu'ils explosent."""
    },
    {
        "planet1": "mars",
        "planet2": "neptune",
        "aspect_type": "square",
        "content": """# □ Carré Mars - Neptune

**En une phrase :** Ton énergie te trahit — tu agis mais dans le vide

## L'énergie de cet aspect

Ton action (Mars) entre en conflit avec tes illusions (Neptune) ce mois-ci. Tu te bats pour des causes perdues. Tu dépenses ton énergie pour rien. Cette guerre intérieure crée de l'épuisement, parfois de la désillusion totale.

## Manifestations concrètes

- **Efforts inutiles** : Tu travailles dur pour des résultats qui n'arrivent jamais
- **Victimisation active** : Tu te bats mais en te plaignant d'être impuissant
- **Colère impuissante** : Tu rages mais ça ne change rien

## Conseil pratique

Arrête-toi et demande-toi : est-ce que je me bats vraiment ou je joue à me battre ?

## Attention

Gare à l'épuisement — Mars-Neptune peut te faire croire que souffrir c'est agir."""
    },
    {
        "planet1": "mars",
        "planet2": "neptune",
        "aspect_type": "trine",
        "content": """# △ Trigone Mars - Neptune

**En une phrase :** Ton action devient art — tu agis avec grâce, inspiration, fluidité

## L'énergie de cet aspect

Ton action (Mars) et ton imaginaire (Neptune) s'harmonisent ce mois-ci. Tes gestes deviennent créatifs. Tu agis sans forcer, tu te bats sans violence. Ton énergie trouve des chemins subtils.

## Manifestations concrètes

- **Action inspirée** : Tu sais quoi faire sans réfléchir, tu suis ton intuition
- **Combat spirituel** : Tu te bats pour des causes qui dépassent ton ego
- **Créativité physique** : Danse, sport, art — ton corps devient poésie

## Conseil pratique

Engage-toi dans une cause qui te dépasse — humanitaire, spirituelle, artistique — ton action y trouvera son sens.

## Attention

Attention à la dispersion — Neptune peut te faire agir partout sans creuser nulle part."""
    },
    {
        "planet1": "mars",
        "planet2": "neptune",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mars - Neptune

**En une phrase :** Tu agis avec sensibilité — chaque geste a du sens au-delà du résultat

## L'énergie de cet aspect

Ton action (Mars) et ton intuition (Neptune) se complètent ce mois-ci. Tu agis en suivant des signes. Tes efforts ont une dimension spirituelle. Tu te bats pour ce qui en vaut la peine.

## Manifestations concrètes

- **Action guidée** : Tu sais quand agir et quand lâcher prise
- **Compassion active** : Tu aides les autres sans te sacrifier
- **Créativité mesurée** : Tes projets ont de la beauté et de la substance

## Conseil pratique

Suis une intuition dans un projet concret — fais confiance à ce ressenti sans tout miser dessus.

## Attention

Gare à la passivité spirituelle — parfois il faut aussi agir sans attendre de signe."""
    }
]


async def insert_batch_18():
    """Insère les 10 aspects du Batch 18 en base de données."""

    print(f"=== Insertion Batch 18 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_18())
