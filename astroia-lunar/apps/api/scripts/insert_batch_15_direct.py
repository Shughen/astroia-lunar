#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 15 en base de données (version=5)
Généré manuellement - Paires: mercury-venus (5 aspects) + mercury-uranus (5 aspects)
Extension : aspects secondaires 1/8
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

# Les 10 aspects du Batch 15
ASPECTS = [
    # === MERCURY-VENUS (5 aspects) ===
    {
        "planet1": "mercury",
        "planet2": "venus",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mercure - Vénus

**En une phrase :** Tes mots deviennent charmants — tu parles avec grâce, tu séduis par l'esprit

## L'énergie de cet aspect

Ton intellect (Mercure) fusionne avec ton charme (Vénus) ce mois-ci. Quand tu parles, c'est agréable à entendre. Tes idées sont élégantes, tes conversations fluides. Tu penses avec ton cœur, tu aimes avec ta tête.

## Manifestations concrètes

- **Communication séduisante** : Tes mots attirent, ton humour charme
- **Curiosité esthétique** : Tu apprends sur l'art, la beauté, les relations
- **Écriture gracieuse** : Si tu écris, c'est fluide et touchant

## Conseil pratique

Écris une lettre d'amour ou de gratitude — tes mots portent une douceur rare maintenant.

## Attention

Gare à trop enjoliver — parfois il faut dire la vérité brutale, pas juste la belle version."""
    },
    {
        "planet1": "mercury",
        "planet2": "venus",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mercure - Vénus

**En une phrase :** Ta tête critique ce que ton cœur aime — impossible de choisir

## L'énergie de cet aspect

Ton analyse (Mercure) s'oppose à tes désirs (Vénus) ce mois-ci. Quand tu aimes quelqu'un, ton esprit trouve tous ses défauts. Quand tu veux quelque chose, ta logique te dit que c'est stupide. Cette tension crée de l'indécision.

## Manifestations concrètes

- **Indécision affective** : Tu analyses tes sentiments jusqu'à ne plus rien ressentir
- **Critique relationnelle** : Tu décortiques les gens que tu aimes au lieu de les accepter
- **Plaisirs intellectualisés** : Tu réfléchis au lieu de profiter

## Conseil pratique

Arrête de penser une journée — ressens, goûte, vis sans analyser.

## Attention

Attention à tuer le désir par excès de réflexion — l'amour n'est pas une équation."""
    },
    {
        "planet1": "mercury",
        "planet2": "venus",
        "aspect_type": "square",
        "content": """# □ Carré Mercure - Vénus

**En une phrase :** Tu dis ce qu'il ne faut pas — tes mots gâchent ton charme

## L'énergie de cet aspect

Ton intellect (Mercure) entre en conflit avec ton désir de plaire (Vénus) ce mois-ci. Tu veux séduire mais tu dis des trucs maladroits. Tu veux être aimé mais tu critiques. Cette friction crée des malentendus relationnels.

## Manifestations concrètes

- **Maladresses verbales** : Tu dis l'inverse de ce que tu voulais dire en amour
- **Critique déplacée** : Tu pointes les défauts des gens que tu aimes
- **Goûts contradictoires** : Tu aimes intellectuellement ce qui te déplaît sensuellement

## Conseil pratique

Réfléchis à deux fois avant de "dire la vérité" — parfois le silence vaut mieux qu'une critique.

## Attention

Gare à blesser par maladresse — tes mots peuvent faire plus de mal que tu ne le penses."""
    },
    {
        "planet1": "mercury",
        "planet2": "venus",
        "aspect_type": "trine",
        "content": """# △ Trigone Mercure - Vénus

**En une phrase :** Tu parles avec élégance — ton esprit et ton cœur dansent ensemble

## L'énergie de cet aspect

Ton intellect (Mercure) et ton sens de la beauté (Vénus) s'harmonisent ce mois-ci. Tes mots sont justes et beaux. Tes idées ont de la grâce. Tu communiques avec style, tu penses avec amour.

## Manifestations concrètes

- **Diplomatie naturelle** : Tu trouves les mots qui apaisent et séduisent
- **Goût raffiné** : Tes choix esthétiques sont intelligents et beaux
- **Relations fluides** : Les conversations coulent, personne ne se blesse

## Conseil pratique

Négocie, médite, crée — tu as le don de rendre beau ce qui est complexe.

## Attention

Attention à éviter les conflits nécessaires — parfois il faut dire la vérité crue."""
    },
    {
        "planet1": "mercury",
        "planet2": "venus",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mercure - Vénus

**En une phrase :** Tu comprends ce que tu aimes — ton goût devient conscient

## L'énergie de cet aspect

Ton intellect (Mercure) et tes désirs (Vénus) se stimulent ce mois-ci. Tu comprends pourquoi tu aimes certaines choses. Tes choix deviennent réfléchis sans perdre leur charme. Tu apprends sur le beau.

## Manifestations concrètes

- **Goût éduqué** : Tu affines tes préférences artistiques, relationnelles
- **Conversations enrichissantes** : Les échanges te font découvrir ce que tu aimes
- **Écriture sensible** : Tu exprimes tes sentiments avec clarté

## Conseil pratique

Explore un art qui t'attire — ton esprit peut maintenant comprendre ce qui te touche.

## Attention

Gare à trop intellectualiser le plaisir — parfois il faut juste aimer sans savoir pourquoi."""
    },

    # === MERCURY-URANUS (5 aspects) ===
    {
        "planet1": "mercury",
        "planet2": "uranus",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mercure - Uranus

**En une phrase :** Ton esprit devient électrique — tu penses vite, différemment, génial

## L'énergie de cet aspect

Ton intellect (Mercure) fusionne avec ton originalité (Uranus) ce mois-ci. Tes idées sont brillantes, décalées, parfois révolutionnaires. Tu vois ce que les autres ne voient pas. Ton esprit ne suit aucune règle.

## Manifestations concrètes

- **Insights soudains** : Les idées te frappent de nulle part, lumineuses
- **Communication directe** : Tu dis ce qui doit être dit, sans détour
- **Pensée disruptive** : Tu remets tout en question, tu inventes de nouvelles façons

## Conseil pratique

Note tes idées immédiatement — elles viennent vite et repartent aussi vite.

## Attention

Gare à choquer gratuitement — ton franc-parler peut blesser sans que tu t'en rendes compte."""
    },
    {
        "planet1": "mercury",
        "planet2": "uranus",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mercure - Uranus

**En une phrase :** Ton esprit se rebelle — tu penses contre juste pour penser contre

## L'énergie de cet aspect

Ton besoin de comprendre (Mercure) s'oppose à ton rejet des normes (Uranus) ce mois-ci. Dès qu'on te dit quelque chose, tu contredis. Tu rejettes les idées conventionnelles sans forcément avoir mieux à proposer.

## Manifestations concrètes

- **Opposition systématique** : Tu contredis par principe, pas par conviction
- **Pensée instable** : Tu changes d'avis constamment, personne ne te suit
- **Communication chaotique** : Tes idées sautent dans tous les sens

## Conseil pratique

Demande-toi : est-ce que je pense vraiment ça ou je me rebelle juste pour me rebeller ?

## Attention

Attention à l'isolement intellectuel — à force de tout rejeter, tu te retrouves seul."""
    },
    {
        "planet1": "mercury",
        "planet2": "uranus",
        "aspect_type": "square",
        "content": """# □ Carré Mercure - Uranus

**En une phrase :** Ton esprit explose — trop rapide, trop dispersé, impossible à suivre

## L'énergie de cet aspect

Ton intellect (Mercure) entre en friction avec ton besoin de rupture (Uranus) ce mois-ci. Tes pensées vont trop vite. Tu ne finis pas une idée que tu passes à la suivante. Cette agitation mentale crée de l'anxiété, de la dispersion.

## Manifestations concrètes

- **Agitation mentale** : Ton esprit ne s'arrête jamais, c'est épuisant
- **Communication saccadée** : Tu sautes du coq à l'âne, personne ne comprend
- **Décisions impulsives** : Tu tranches sans réfléchir, tu regrettes après

## Conseil pratique

Écris tout ce qui te traverse la tête pour vider ton esprit — puis relis à froid.

## Attention

Gare au burn-out mental — ton cerveau a besoin de ralentir, pas d'accélérer encore."""
    },
    {
        "planet1": "mercury",
        "planet2": "uranus",
        "aspect_type": "trine",
        "content": """# △ Trigone Mercure - Uranus

**En une phrase :** Ton génie devient accessible — tu innoves en expliquant clairement

## L'énergie de cet aspect

Ton intellect (Mercure) et ton originalité (Uranus) collaborent ce mois-ci. Tu as des idées brillantes ET tu sais les communiquer. Ton esprit est rapide mais pas chaotique. Tu inventes en restant compréhensible.

## Manifestations concrètes

- **Insights clairs** : Tes éclairs de génie se formulent simplement
- **Communication innovante** : Tu exprimes des idées neuves avec clarté
- **Apprentissages rapides** : Tu captes vite, tu comprends différemment

## Conseil pratique

Lance un projet intellectuel disruptif — tu as la créativité et la clarté pour le mener.

## Attention

Attention à aller trop vite pour les autres — ralentis pour qu'ils puissent suivre."""
    },
    {
        "planet1": "mercury",
        "planet2": "uranus",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mercure - Uranus

**En une phrase :** Tu libères ton esprit — chaque idée nouvelle t'ouvre une porte

## L'énergie de cet aspect

Ton intellect (Mercure) et ton besoin de liberté (Uranus) se stimulent ce mois-ci. Tu oses penser autrement. Tes conversations deviennent stimulantes. Tu apprends par des voies inhabituelles.

## Manifestations concrètes

- **Curiosité décalée** : Tu explores des sujets que personne n'étudie
- **Échanges vivants** : Tes conversations sont surprenantes, rafraîchissantes
- **Flexibilité mentale** : Tu changes d'avis sans ego quand une meilleure idée arrive

## Conseil pratique

Lis un livre sur un sujet que tu ne connais pas du tout — ton esprit a soif de nouveauté.

## Attention

Gare à la dispersion — trop de nouveautés intellectuelles peuvent t'empêcher d'approfondir."""
    }
]


async def insert_batch_15():
    """Insère les 10 aspects du Batch 15 en base de données."""

    print(f"=== Insertion Batch 15 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_15())
