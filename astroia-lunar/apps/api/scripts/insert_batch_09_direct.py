#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 9 en base de données (version=5)
Généré manuellement - Paires: moon-neptune (5 aspects) + moon-pluto (5 aspects)
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

# Les 10 aspects du Batch 9
ASPECTS = [
    # === MOON-NEPTUNE (5 aspects) ===
    {
        "planet1": "moon",
        "planet2": "neptune",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Lune - Neptune

**En une phrase :** Tes frontières émotionnelles se dissolvent — tu ressens tout, même ce qui n'est pas à toi

## L'énergie de cet aspect

Tes émotions (Lune) fusionnent avec ton imaginaire (Neptune) ce mois-ci. Tu captes les ambiances, les non-dits, les émotions des autres comme une éponge. Ta sensibilité devient presque psychique. Tu rêves beaucoup, tu te perds facilement dans tes pensées.

## Manifestations concrètes

- **Empathie extrême** : Tu pleures aux films, tu ressens la peine des autres comme la tienne
- **Confusion émotionnelle** : Tu ne sais plus si c'est ton émotion ou celle de quelqu'un d'autre
- **Créativité intuitive** : Ton art, ta musique, tes mots touchent sans que tu saches pourquoi

## Conseil pratique

Crée un rituel de protection énergétique — méditation, eau, nature — pour ne pas te perdre dans les émotions des autres.

## Attention

Gare à fuir dans l'imaginaire — Neptune peut te faire éviter la réalité en rêvant ta vie."""
    },
    {
        "planet1": "moon",
        "planet2": "neptune",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Lune - Neptune

**En une phrase :** Tu idéalises ce dont tu as besoin — la réalité te déçoit toujours

## L'énergie de cet aspect

Tes besoins réels (Lune) s'opposent à ce que tu rêves de recevoir (Neptune) ce mois-ci. Tu attends que les autres devinent, qu'ils te sauvent, qu'ils soient parfaits. Mais personne n'est à la hauteur. Cette tension crée de la désillusion, parfois du ressentiment.

## Manifestations concrètes

- **Déception relationnelle** : Les gens ne sont jamais ce que tu espérais
- **Besoin de sauvetage** : Tu attends qu'on vienne te chercher plutôt que de demander
- **Sacrifice martyr** : Tu te donnes en espérant qu'on te rende la pareille, mais ça n'arrive jamais

## Conseil pratique

Nomme un besoin concret et demande-le clairement — arrête d'attendre qu'on devine.

## Attention

Attention à jouer la victime — Neptune peut te faire croire que tu es impuissant alors que tu as du pouvoir."""
    },
    {
        "planet1": "moon",
        "planet2": "neptune",
        "aspect_type": "square",
        "content": """# □ Carré Lune - Neptune

**En une phrase :** Tes émotions te noient — tu ne sais plus où est le rivage

## L'énergie de cet aspect

Tes besoins (Lune) et ta confusion (Neptune) s'entrechoquent ce mois-ci. Tu ne sais plus ce que tu ressens vraiment. Tout est flou, trop intense, insaisissable. Tu peux te sentir submergé, perdu, parfois même dissocié.

## Manifestations concrètes

- **Émotions incontrôlables** : Tu pleures sans savoir pourquoi, tu te sens vidé
- **Addictions émotionnelles** : Tu cherches des échappatoires — écrans, substances, fantasmes
- **Dépendances toxiques** : Tu t'accroches à des gens qui te font du mal par peur du vide

## Conseil pratique

Ancre-toi dans le corps — sport, marche, respiration — pour revenir au réel.

## Attention

Gare aux fuites — Neptune offre des illusions qui soulagent sur le moment mais détruisent à long terme."""
    },
    {
        "planet1": "moon",
        "planet2": "neptune",
        "aspect_type": "trine",
        "content": """# △ Trigone Lune - Neptune

**En une phrase :** Ta sensibilité devient un don — tu touches les cœurs sans effort

## L'énergie de cet aspect

Tes émotions (Lune) et ton intuition (Neptune) collaborent ce mois-ci. Tu ressens ce que les autres vivent sans qu'ils aient à parler. Ta présence apaise, ton art touche, ta compassion guérit. Tu es un canal pour quelque chose de plus grand.

## Manifestations concrètes

- **Intuition juste** : Tu sens les choses avant qu'elles arrivent
- **Art inspiré** : Ce que tu crées vient d'ailleurs, ça te traverse
- **Compassion profonde** : Tu comprends la souffrance des autres sans juger

## Conseil pratique

Offre ta présence à quelqu'un qui souffre — ton écoute peut être un baume.

## Attention

Attention à te dissoudre dans les autres — même avec ce don, tes limites comptent."""
    },
    {
        "planet1": "moon",
        "planet2": "neptune",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Lune - Neptune

**En une phrase :** Ton cœur s'ouvre doucement — tu laisses entrer la magie

## L'énergie de cet aspect

Tes besoins (Lune) et ton imaginaire (Neptune) se stimulent ce mois-ci. Tu te permets de rêver sans te perdre. Ta sensibilité devient un atout, pas un fardeau. Tu te connectes à ton intuition sans lâcher le réel.

## Manifestations concrètes

- **Rêves porteurs** : Tes songes te parlent, tu écoutes sans t'y noyer
- **Créativité fluide** : Tu exprimes ta sensibilité dans l'art, l'écriture, la musique
- **Empathie mesurée** : Tu ressens les autres sans absorber leur douleur

## Conseil pratique

Tiens un journal de rêves — ils contiennent des messages subtils pour toi.

## Attention

Gare à fuir le concret — Neptune peut te faire préférer l'imaginaire au réel."""
    },

    # === MOON-PLUTO (5 aspects) ===
    {
        "planet1": "moon",
        "planet2": "pluto",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Lune - Pluton

**En une phrase :** Tes émotions deviennent volcaniques — tout est intense, rien n'est léger

## L'énergie de cet aspect

Tes besoins (Lune) fusionnent avec ton pouvoir de transformation (Pluton) ce mois-ci. Tes émotions sont extrêmes, obsessionnelles, presque violentes. Tu ressens tout à 100%. Rien n'est neutre, tout est une question de vie ou de mort.

## Manifestations concrètes

- **Intensité émotionnelle** : Quand tu aimes, c'est total. Quand tu détestes, c'est viscéral.
- **Besoin de contrôle** : Tu veux tout maîtriser par peur de te perdre
- **Transformations profondes** : Tes émotions te forcent à changer radicalement

## Conseil pratique

Plonge dans ce qui fait peur — thérapie, journal, confrontation — ta puissance peut te libérer.

## Attention

Gare aux obsessions — Pluton peut transformer un besoin en fixation toxique."""
    },
    {
        "planet1": "moon",
        "planet2": "pluto",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Lune - Pluton

**En une phrase :** Tu as peur de perdre ce dont tu as besoin — alors tu contrôles, tu étouffes

## L'énergie de cet aspect

Ton besoin de sécurité (Lune) s'oppose à ta peur de l'abandon (Pluton) ce mois-ci. Tu veux qu'on t'aime mais tu ne fais pas confiance. Tu te montres possessif, jaloux, parfois manipulateur. Cette tension crée des crises émotionnelles intenses.

## Manifestations concrètes

- **Jalousie toxique** : Tu surveilles, tu questionnes, tu ne lâches pas
- **Manipulations émotionnelles** : Tu utilises la culpabilité pour garder les gens
- **Crises de pouvoir** : Les conflits deviennent des batailles pour le contrôle

## Conseil pratique

Demande-toi : qu'est-ce que j'ai si peur de perdre ? Puis explore cette peur sans agir dessus.

## Attention

Attention à devenir ce que tu crains — à force de contrôler, tu provoques l'abandon que tu redoutes."""
    },
    {
        "planet1": "moon",
        "planet2": "pluto",
        "aspect_type": "square",
        "content": """# □ Carré Lune - Pluton

**En une phrase :** Tes émotions te terrorisent — tu préfères tout détruire que de les sentir

## L'énergie de cet aspect

Tes besoins (Lune) entrent en guerre avec ta peur du vide (Pluton) ce mois-ci. Plutôt que de ressentir ta vulnérabilité, tu sabotes. Tu détruis ce qui te fait du bien avant que ça ne te détruise. Cette autodestruction crée du chaos émotionnel.

## Manifestations concrètes

- **Autodestruction relationnelle** : Tu pousses les gens à bout pour confirmer qu'ils partiront
- **Émotions explosives** : Ta colère sort de façon disproportionnée, tu détruis sans réfléchir
- **Obsessions noires** : Tu rumines sur ce qui te fait mal, tu creuses la blessure

## Conseil pratique

Nomme la peur sous la colère — qu'est-ce qui te terrifie vraiment dans ce besoin ?

## Attention

Gare à retourner ta rage contre toi — Pluton peut te faire croire que tu mérites la souffrance."""
    },
    {
        "planet1": "moon",
        "planet2": "pluto",
        "aspect_type": "trine",
        "content": """# △ Trigone Lune - Pluton

**En une phrase :** Tu traverses tes abysses — ta profondeur devient ta force

## L'énergie de cet aspect

Tes émotions (Lune) et ta capacité de transformation (Pluton) s'allient ce mois-ci. Tu n'as plus peur de ressentir. Tu plonges dans tes zones d'ombre et tu en ressors plus fort. Tes besoins profonds te guident vers la guérison.

## Manifestations concrètes

- **Guérison émotionnelle** : Tu touches des blessures anciennes et elles se libèrent
- **Pouvoir émotionnel** : Ta vulnérabilité devient une force, pas une faiblesse
- **Transformation naturelle** : Tu lâches ce qui ne sert plus sans résister

## Conseil pratique

Engage un travail thérapeutique profond — tu as la force de descendre et de remonter.

## Attention

Attention à sous-estimer l'impact de ton intensité — tu peux écraser les autres sans le vouloir."""
    },
    {
        "planet1": "moon",
        "planet2": "pluto",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Lune - Pluton

**En une phrase :** Tu découvres ta puissance émotionnelle — couche après couche, tu te libères

## L'énergie de cet aspect

Tes besoins (Lune) et ton pouvoir de transformation (Pluton) se stimulent ce mois-ci. Tu es prêt à explorer ce que tu cachais. Les conversations profondes t'attirent. Tu veux comprendre tes mécanismes, tes blessures, tes patterns.

## Manifestations concrètes

- **Introspection fructueuse** : Tu explores tes émotions sans te perdre
- **Libérations progressives** : Tu lâches de vieux schémas émotionnels, un à un
- **Pouvoir assumé** : Tu reconnais ta force sans en avoir peur

## Conseil pratique

Commence un journal émotionnel — écris ce que tu ressens vraiment, sans censure.

## Attention

Gare à l'obsession de la profondeur — parfois la légèreté est aussi une forme de guérison."""
    }
]


async def insert_batch_09():
    """Insère les 10 aspects du Batch 9 en base de données."""

    print(f"=== Insertion Batch 9 ({len(ASPECTS)} aspects) ===\n")

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


if __name__ == '__main__':
    asyncio.run(insert_batch_09())
