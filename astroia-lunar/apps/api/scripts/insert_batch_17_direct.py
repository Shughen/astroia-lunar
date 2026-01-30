#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 17 en base de données (version=5)
Généré manuellement - Paires: venus-uranus (5 aspects) + venus-neptune (5 aspects)
Extension : aspects secondaires 3/8
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

# Les 10 aspects du Batch 17
ASPECTS = [
    # === VENUS-URANUS (5 aspects) ===
    {
        "planet1": "venus",
        "planet2": "uranus",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Vénus - Uranus

**En une phrase :** Ton cœur se libère — tu aimes ce qui est différent, sans règles

## L'énergie de cet aspect

Ton désir (Vénus) fusionne avec ta soif de liberté (Uranus) ce mois-ci. Tu ne supportes plus l'amour conventionnel. Ce qui t'attire est décalé, inattendu, parfois choquant. Tu veux aimer sans cage.

## Manifestations concrètes

- **Attractions soudaines** : Tu tombes amoureux sans prévenir, souvent de l'inattendu
- **Relations non-conventionnelles** : Ce qui te plaît ne ressemble à rien de classique
- **Ruptures libératrices** : Tu quittes ce qui t'étouffe, même si c'était confortable

## Conseil pratique

Accepte que tes désirs soient étranges — ton authenticité affective passe par l'originalité maintenant.

## Attention

Gare à la fuite — Uranus peut te faire confondre liberté et impossibilité d'engagement."""
    },
    {
        "planet1": "venus",
        "planet2": "uranus",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Vénus - Uranus

**En une phrase :** Tu veux l'amour mais tu fuis dès qu'il arrive — impossible de choisir

## L'énergie de cet aspect

Ton besoin d'amour (Vénus) s'oppose à ton besoin de liberté (Uranus) ce mois-ci. Dès que tu te rapproches de quelqu'un, tu veux partir. Dès que tu es seul, tu veux qu'on t'aime. Cette tension crée de l'instabilité relationnelle.

## Manifestations concrètes

- **Ambivalence affective** : Tu veux l'engagement mais tu le sabotes
- **Relations instables** : Tu attires des gens qui partent ou tu pars toi-même
- **Peur de l'intimité** : Tu te sens piégé dès que ça devient sérieux

## Conseil pratique

Identifie ce qui te fait vraiment peur dans l'intimité — c'est ça que tu fuis, pas la personne.

## Attention

Attention à l'isolement — à force de fuir, tu te retrouves seul et tu ne sais plus pourquoi."""
    },
    {
        "planet1": "venus",
        "planet2": "uranus",
        "aspect_type": "square",
        "content": """# □ Carré Vénus - Uranus

**En une phrase :** Tu détruis ce que tu aimes — dès que c'est beau, tu casses

## L'énergie de cet aspect

Ton désir de relation (Vénus) entre en conflit avec ton besoin d'indépendance (Uranus) ce mois-ci. Tu sabotes tes relations par peur d'être piégé. Tu fuis l'amour au moment où il pourrait vraiment commencer. Cette friction crée du chaos affectif.

## Manifestations concrètes

- **Auto-sabotage amoureux** : Tu trouves toujours une raison de partir
- **Provocations** : Tu testes l'autre jusqu'à ce qu'il craque
- **Changements brutaux** : Tu passes de l'amour à l'indifférence en un instant

## Conseil pratique

Demande-toi si tu fuis la personne ou si tu fuis l'engagement — ce n'est pas pareil.

## Attention

Gare à la solitude chronique — à force de tout casser, tu ne construis jamais rien."""
    },
    {
        "planet1": "venus",
        "planet2": "uranus",
        "aspect_type": "trine",
        "content": """# △ Trigone Vénus - Uranus

**En une phrase :** Tu aimes avec liberté — tes relations sont authentiques, sans cage

## L'énergie de cet aspect

Ton désir (Vénus) et ton besoin de liberté (Uranus) s'harmonisent ce mois-ci. Tu arrives à aimer sans étouffer, à être proche sans fusionner. Tes relations deviennent fluides, honnêtes, originales.

## Manifestations concrètes

- **Relations libres** : Tu aimes sans possessivité, tu laisses l'autre respirer
- **Attractions authentiques** : Tu suis tes vrais désirs sans te forcer
- **Amitié amoureuse** : Tes relations mélangent affection et liberté

## Conseil pratique

Construis une relation basée sur la liberté mutuelle — vous êtes ensemble par choix, pas par besoin.

## Attention

Attention au détachement excessif — parfois il faut aussi oser la vulnérabilité."""
    },
    {
        "planet1": "venus",
        "planet2": "uranus",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Vénus - Uranus

**En une phrase :** Tu explores ton désir — chaque attirance te révèle qui tu es

## L'énergie de cet aspect

Ton désir (Vénus) et ton besoin d'authenticité (Uranus) se stimulent ce mois-ci. Tu oses aimer ce qui te plaît vraiment, même si c'est décalé. Tes goûts deviennent plus personnels, moins conditionnés.

## Manifestations concrètes

- **Goûts originaux** : Ce qui t'attire ne suit aucune norme
- **Expérimentations affectives** : Tu testes de nouvelles façons d'aimer
- **Honnêteté relationnelle** : Tu dis ce que tu veux vraiment, sans faux-semblants

## Conseil pratique

Essaie une forme de relation qui t'intrigue — relation à distance, amour non-exclusif, amitié profonde.

## Attention

Gare à choquer pour choquer — parfois l'originalité cache juste la peur d'être classique."""
    },

    # === VENUS-NEPTUNE (5 aspects) ===
    {
        "planet1": "venus",
        "planet2": "neptune",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Vénus - Neptune

**En une phrase :** Ton amour devient rêve — tu idéalises jusqu'à ne plus voir le réel

## L'énergie de cet aspect

Ton désir (Vénus) fusionne avec ton imaginaire (Neptune) ce mois-ci. Tu tombes amoureux d'une illusion, d'un fantasme, d'un potentiel. La personne réelle disparaît derrière ce que tu projettes. C'est beau, c'est douloureux.

## Manifestations concrètes

- **Idéalisation amoureuse** : Tu vois l'autre comme parfait, tu ignores ses défauts
- **Amour platonique** : Tu aimes l'idée de la personne plus que la personne elle-même
- **Sacrifice romantique** : Tu te donnes entièrement, tu t'oublies pour l'autre

## Conseil pratique

Demande-toi : est-ce que j'aime cette personne ou l'idée que je m'en fais ?

## Attention

Gare à la désillusion brutale — Neptune crée des mirages qui s'effondrent un jour."""
    },
    {
        "planet1": "venus",
        "planet2": "neptune",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Vénus - Neptune

**En une phrase :** Tu donnes tout, on te prend tout — tu confonds amour et sacrifice

## L'énergie de cet aspect

Ton besoin d'amour (Vénus) s'oppose à ton besoin de fusion (Neptune) ce mois-ci. Tu te perds dans les relations. Tu donnes sans limite, tu t'effaces. Les autres profitent de ta générosité sans la voir. Cette tension crée de la désillusion, parfois de la victimisation.

## Manifestations concrètes

- **Sacrifice excessif** : Tu te vides pour les autres, il ne reste rien pour toi
- **Victimisation amoureuse** : Tu te sens toujours celui qui donne, jamais celui qui reçoit
- **Attirance pour les victimes** : Tu aimes ceux qui souffrent, tu veux les sauver

## Conseil pratique

Pose une limite claire dans une relation — dire non ne tue pas l'amour, ça le rend sain.

## Attention

Attention aux manipulateurs — Neptune attire ceux qui savent profiter de ta bonté."""
    },
    {
        "planet1": "venus",
        "planet2": "neptune",
        "aspect_type": "square",
        "content": """# □ Carré Vénus - Neptune

**En une phrase :** Tu aimes des fantômes — tes relations ne reposent sur rien de réel

## L'énergie de cet aspect

Ton désir de relation (Vénus) entre en conflit avec tes illusions (Neptune) ce mois-ci. Tu tombes amoureux de personnes inaccessibles, indisponibles, inexistantes. Tes relations sont floues, sans engagement, sans substance. Cette friction crée de la souffrance, de l'errance affective.

## Manifestations concrètes

- **Amours impossibles** : Tu aimes ceux qui ne peuvent pas t'aimer
- **Relations floues** : Tu ne sais jamais où tu en es, rien n'est clair
- **Addiction affective** : Tu as besoin d'amour mais tu choisis toujours ceux qui te fuient

## Conseil pratique

Identifie un pattern : qui choisis-tu toujours ? Pourquoi cette personne ne peut jamais t'aimer ?

## Attention

Gare à l'autodestruction — Neptune peut te faire croire que souffrir c'est aimer."""
    },
    {
        "planet1": "venus",
        "planet2": "neptune",
        "aspect_type": "trine",
        "content": """# △ Trigone Vénus - Neptune

**En une phrase :** Ton amour devient art — tu aimes avec grâce, compassion, poésie

## L'énergie de cet aspect

Ton désir (Vénus) et ton imaginaire (Neptune) s'harmonisent ce mois-ci. Tu aimes avec douceur, sans violence, sans ego. Tes relations deviennent des œuvres d'art, des espaces de grâce. Tu donnes sans t'oublier.

## Manifestations concrètes

- **Amour transcendant** : Tu vois le divin dans l'autre sans l'idéaliser
- **Compassion naturelle** : Tu aimes avec empathie, sans jugement
- **Créativité affective** : Tes relations inspirent ton art, ton art nourrit tes relations

## Conseil pratique

Crée quelque chose avec ou pour quelqu'un que tu aimes — un poème, une chanson, un rituel.

## Attention

Attention à la fuite — Neptune peut te faire préférer l'art de l'amour à l'amour lui-même."""
    },
    {
        "planet1": "venus",
        "planet2": "neptune",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Vénus - Neptune

**En une phrase :** Tu aimes avec sensibilité — chaque lien devient sacré

## L'énergie de cet aspect

Ton désir (Vénus) et ton intuition (Neptune) se complètent ce mois-ci. Tu ressens les gens avant de les connaître. Tes relations ont de la profondeur, de la subtilité. Tu donnes avec discernement.

## Manifestations concrètes

- **Intuition affective** : Tu sens qui est bon pour toi, qui ne l'est pas
- **Amour spirituel** : Tes relations ont du sens au-delà du plaisir
- **Générosité mesurée** : Tu donnes sans te perdre

## Conseil pratique

Écoute ton ressenti face aux gens — Neptune te dit la vérité que Vénus ne veut pas voir.

## Attention

Gare à l'idéalisation douce — même avec Neptune harmonieux, tu peux te tromper."""
    }
]


async def insert_batch_17():
    """Insère les 10 aspects du Batch 17 en base de données."""

    print(f"=== Insertion Batch 17 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_17())
