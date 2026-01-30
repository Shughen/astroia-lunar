#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 10 en base de données (version=5)
Généré manuellement - Paires: venus-jupiter (5 aspects) + venus-saturn (5 aspects)
**DERNIER BATCH** - 90/130 aspects prioritaires complétés
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

# Les 10 derniers aspects du Batch 10
ASPECTS = [
    # === VENUS-JUPITER (5 aspects) ===
    {
        "planet1": "venus",
        "planet2": "jupiter",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Vénus - Jupiter

**En une phrase :** Ton cœur s'ouvre en grand — tu veux vivre, aimer, célébrer

## L'énergie de cet aspect

Tes désirs (Vénus) fusionnent avec ton besoin d'expansion (Jupiter) ce mois-ci. Tu te sens généreux, optimiste, confiant. Tout ce qui touche à l'amour, au plaisir, à la beauté te fait vibrer. Tu veux partager, créer du beau, profiter de la vie.

## Manifestations concrètes

- **Générosité affective** : Tu montres ton amour facilement, tu offres sans compter
- **Optimisme relationnel** : Tu crois en l'amour, tu vois le bon chez les gens
- **Plaisirs élargis** : Tu veux voyager, découvrir, vivre de nouvelles expériences

## Conseil pratique

Dis oui à une invitation, un projet créatif, une rencontre — ton cœur est ouvert au bon.

## Attention

Gare aux excès — Jupiter peut te faire promettre trop en amour ou dépenser trop pour le plaisir."""
    },
    {
        "planet1": "venus",
        "planet2": "jupiter",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Vénus - Jupiter

**En une phrase :** Tu en veux toujours plus — aucune relation ne te comble vraiment

## L'énergie de cet aspect

Tes désirs (Vénus) s'opposent à ton besoin d'expansion (Jupiter) ce mois-ci. Tu idéalises l'amour, tu attends l'extraordinaire. Mais rien n'est jamais assez, personne n'est à la hauteur. Cette tension crée de l'insatisfaction chronique.

## Manifestations concrètes

- **Idéalisation excessive** : Tu vois les gens mieux qu'ils ne sont, puis tu es déçu
- **Besoin d'être impressionné** : Les relations simples t'ennuient, tu veux du grandiose
- **Générosité déséquilibrée** : Tu donnes trop en espérant recevoir autant, mais ça ne vient jamais

## Conseil pratique

Apprécie ce qui est là plutôt que de rêver de ce qui pourrait être — la magie est dans le présent.

## Attention

Attention à fuir vers la prochaine personne dès que ça devient normal — l'amour vrai demande de l'ancrage."""
    },
    {
        "planet1": "venus",
        "planet2": "jupiter",
        "aspect_type": "square",
        "content": """# □ Carré Vénus - Jupiter

**En une phrase :** Tu confonds quantité et qualité — trop de tout, pas assez de vrai

## L'énergie de cet aspect

Tes désirs (Vénus) se frottent à ton optimisme (Jupiter) ce mois-ci. Tu veux tout, tout de suite. Tu multiplies les plaisirs mais rien ne te remplit vraiment. Cette sur-stimulation crée du vide plutôt que de la satisfaction.

## Manifestations concrètes

- **Excès affectifs** : Tu tombes amoureux trop vite, tu promets trop, tu idéalises
- **Dépenses impulsives** : Tu achètes pour combler un vide émotionnel
- **Plaisirs vides** : Tu consommes le plaisir sans le savourer, ça ne nourrit pas

## Conseil pratique

Choisis un seul plaisir et savoure-le vraiment — moins mais mieux.

## Attention

Gare à la boulimie affective — accumuler les expériences ne comble pas le manque d'être."""
    },
    {
        "planet1": "venus",
        "planet2": "jupiter",
        "aspect_type": "trine",
        "content": """# △ Trigone Vénus - Jupiter

**En une phrase :** L'amour coule naturellement — tu attires et tu rayonnes sans forcer

## L'énergie de cet aspect

Tes désirs (Vénus) et ton optimisme (Jupiter) s'harmonisent ce mois-ci. Tu te sens aimé, chanceux, inspiré. Les bonnes personnes croisent ton chemin. Les opportunités créatives se présentent. La vie te sourit et tu souris en retour.

## Manifestations concrètes

- **Magnétisme naturel** : Les gens t'apprécient, tu crées du lien facilement
- **Opportunités créatives** : Tes projets artistiques trouvent écho, se concrétisent
- **Amour fluide** : Les relations sont douces, généreuses, enrichissantes

## Conseil pratique

Crée quelque chose de beau et partage-le — ton art touche et inspire maintenant.

## Attention

Attention à tenir cette chance pour acquise — la gratitude nourrit l'abondance."""
    },
    {
        "planet1": "venus",
        "planet2": "jupiter",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Vénus - Jupiter

**En une phrase :** Tu découvres du bon — chaque rencontre, chaque plaisir t'élève

## L'énergie de cet aspect

Tes désirs (Vénus) et ton besoin de sens (Jupiter) se stimulent ce mois-ci. Tu cherches la beauté qui a du fond, l'amour qui fait grandir. Tes plaisirs deviennent des portes vers quelque chose de plus grand.

## Manifestations concrètes

- **Rencontres enrichissantes** : Les gens que tu croises t'apportent quelque chose de précieux
- **Créativité inspirée** : Ton art exprime une vision, pas juste une esthétique
- **Générosité joyeuse** : Donner te fait du bien, recevoir aussi

## Conseil pratique

Explore une nouvelle forme d'art, un voyage, une philosophie — ton cœur cherche à s'élargir.

## Attention

Gare à l'idéalisation — parfois le bon est déjà là, sans besoin de l'embellir."""
    },

    # === VENUS-SATURN (5 aspects) ===
    {
        "planet1": "venus",
        "planet2": "saturn",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Vénus - Saturne

**En une phrase :** Ton cœur se protège — l'amour devient sérieux, parfois trop lourd

## L'énergie de cet aspect

Tes désirs (Vénus) fusionnent avec tes limites (Saturne) ce mois-ci. Tu te méfies de l'amour léger, tu veux du solide. Tes relations deviennent plus sérieuses, mais aussi plus lourdes. Tu as du mal à lâcher prise, à jouer, à profiter.

## Manifestations concrètes

- **Sérieux relationnel** : Tu veux de l'engagement, pas des histoires légères
- **Affection retenue** : Tu montres difficilement ton amour, tu as peur d'être ridicule
- **Plaisirs coupables** : Tu te sens mal de profiter, tu te contrôles trop

## Conseil pratique

Autorise-toi un plaisir simple sans culpabilité — un dessert, une chanson, un moment doux.

## Attention

Gare à confondre sérieux et tristesse — l'amour peut être profond et joyeux à la fois."""
    },
    {
        "planet1": "venus",
        "planet2": "saturn",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Vénus - Saturne

**En une phrase :** Tu veux aimer mais tu as peur — alors tu rejettes avant d'être rejeté

## L'énergie de cet aspect

Ton désir de connexion (Vénus) s'oppose à ta peur du rejet (Saturne) ce mois-ci. Tu veux qu'on t'aime mais tu ne te crois pas aimable. Cette tension crée des blocages relationnels, parfois de la froideur.

## Manifestations concrètes

- **Peur de l'abandon** : Tu te retiens d'aimer pour ne pas souffrir
- **Tests relationnels** : Tu pousses l'autre à bout pour voir s'il reste
- **Solitude choisie** : Tu préfères être seul que vulnérable

## Conseil pratique

Ose dire "je t'aime" à quelqu'un qui compte — même si ça fait peur, même si tu doutes.

## Attention

Attention à créer ce que tu crains — à force de te protéger, tu éloignes ceux qui t'aiment vraiment."""
    },
    {
        "planet1": "venus",
        "planet2": "saturn",
        "aspect_type": "square",
        "content": """# □ Carré Vénus - Saturne

**En une phrase :** L'amour te fait honte — tu ne te sens pas digne d'être aimé

## L'énergie de cet aspect

Tes désirs (Vénus) entrent en conflit avec ton exigence (Saturne) ce mois-ci. Tu te juges de vouloir de l'amour, du plaisir, de la beauté. Tes envies te semblent égoïstes, superficielles. Cette guerre intérieure crée de la tristesse, de la frustration.

## Manifestations concrètes

- **Rejet de tes désirs** : Tu nies ce que tu veux vraiment pour ne pas être déçu
- **Relations austères** : Tu choisis des gens indisponibles ou critiques
- **Plaisir interdit** : Tu t'empêches de jouir de la vie par culpabilité

## Conseil pratique

Liste trois choses qui te font plaisir et permets-t'en une cette semaine — tu as le droit de vouloir.

## Attention

Gare à l'auto-sabotage — Saturne peut te faire croire que tu ne mérites pas l'amour."""
    },
    {
        "planet1": "venus",
        "planet2": "saturn",
        "aspect_type": "trine",
        "content": """# △ Trigone Vénus - Saturne

**En une phrase :** Ton amour devient fiable — tu construis du solide avec grâce

## L'énergie de cet aspect

Tes désirs (Vénus) et ta structure (Saturne) collaborent ce mois-ci. Tu veux de l'amour qui dure, du plaisir qui a du sens. Tes relations deviennent plus stables, plus vraies. Tu poses des bases pour le long terme.

## Manifestations concrètes

- **Engagement serein** : Tu choisis consciemment, tu t'engages sans peur
- **Amour mature** : Tu aimes sans attendre la perfection, tu acceptes les limites
- **Plaisirs durables** : Tu investis dans ce qui te nourrit vraiment

## Conseil pratique

Engage-toi dans une relation ou un projet créatif à long terme — tu as la maturité pour tenir.

## Attention

Attention à devenir trop sérieux — l'amour a aussi besoin de légèreté et de surprise."""
    },
    {
        "planet1": "venus",
        "planet2": "saturn",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Vénus - Saturne

**En une phrase :** Tu bâtis ton bonheur — choix par choix, tu crées du beau qui dure

## L'énergie de cet aspect

Tes désirs (Vénus) et ta capacité à structurer (Saturne) se complètent ce mois-ci. Tu sais ce qui te fait du bien et tu le protèges. Tu poses des limites saines dans l'amour. Tu investis dans ce qui compte vraiment.

## Manifestations concrètes

- **Choix conscients** : Tu sélectionnes tes relations, tu ne dis oui qu'à ce qui résonne
- **Limites affectueuses** : Tu poses des frontières sans fermer ton cœur
- **Créativité patiente** : Tu construis tes projets artistiques avec constance

## Conseil pratique

Identifie une relation toxique et pose une limite claire — ton amour mérite d'être protégé.

## Attention

Gare à trop contrôler — parfois il faut aussi laisser l'amour te surprendre."""
    }
]


async def insert_batch_10():
    """Insère les 10 derniers aspects du Batch 10 en base de données."""

    print(f"=== Insertion Batch 10 - DERNIER BATCH ({len(ASPECTS)} aspects) ===\n")

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
    print(f"📊 Progression : {count}/130 aspects ({round(count/130*100, 1)}%)")
    print(f"\n🎉 BATCHES 1-10 TERMINÉS : 90 aspects prioritaires complétés (Sun, Moon, Venus)")


if __name__ == '__main__':
    asyncio.run(insert_batch_10())
