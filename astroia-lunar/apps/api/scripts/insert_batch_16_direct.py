#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 16 en base de données (version=5)
Généré manuellement - Paires: mercury-neptune (5 aspects) + mercury-pluto (5 aspects)
Extension : aspects secondaires 2/8
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

# Les 10 aspects du Batch 16
ASPECTS = [
    # === MERCURY-NEPTUNE (5 aspects) ===
    {
        "planet1": "mercury",
        "planet2": "neptune",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mercure - Neptune

**En une phrase :** Ton esprit se dissout — tu penses en poésie, en rêves, en flou

## L'énergie de cet aspect

Ton intellect (Mercure) fusionne avec ton imaginaire (Neptune) ce mois-ci. Tes pensées perdent leur netteté mais gagnent en profondeur. Tu comprends sans mots, tu ressens sans logique. Ton esprit devient poreux, intuitif, parfois confus.

## Manifestations concrètes

- **Intuition accrue** : Tu sais des choses sans savoir comment tu les sais
- **Communication poétique** : Tes mots deviennent images, métaphores, évocations
- **Confusion mentale** : Tu ne distingues plus le réel de l'imaginaire

## Conseil pratique

Écris tes rêves, tes intuitions, tes visions — ton esprit capte du subtil maintenant.

## Attention

Gare au mensonge — Neptune peut te faire confondre ce que tu souhaites avec ce qui est."""
    },
    {
        "planet1": "mercury",
        "planet2": "neptune",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mercure - Neptune

**En une phrase :** Ta tête se noie — tu ne sais plus ce qui est vrai

## L'énergie de cet aspect

Ton besoin de clarté (Mercure) s'oppose à ton besoin de rêve (Neptune) ce mois-ci. Soit tu analyses tout et tu perds la magie, soit tu rêves tout et tu perds le réel. Cette tension crée de la confusion, parfois du déni.

## Manifestations concrètes

- **Réalité floue** : Tu ne sais plus distinguer vérité et mensonge
- **Communication ambiguë** : Ce que tu dis n'est jamais clair, ni pour toi ni pour les autres
- **Mensonges involontaires** : Tu crois ce que tu inventes

## Conseil pratique

Vérifie tes infos à deux fois — Neptune brouille tout, relis, redemande, confirme.

## Attention

Attention aux manipulations — Neptune peut te faire croire n'importe quoi si tu veux y croire."""
    },
    {
        "planet1": "mercury",
        "planet2": "neptune",
        "aspect_type": "square",
        "content": """# □ Carré Mercure - Neptune

**En une phrase :** Ton esprit t'échappe — chaque pensée glisse, rien ne reste clair

## L'énergie de cet aspect

Ton intellect (Mercure) se frotte à ton imaginaire (Neptune) ce mois-ci. Tu veux comprendre mais tout se dissout. Tes pensées partent dans tous les sens, tes mots ne disent pas ce que tu veux dire. Cette friction crée de l'anxiété mentale, parfois de la paranoïa.

## Manifestations concrètes

- **Confusion chronique** : Tu te perds dans tes propres pensées
- **Communication ratée** : Personne ne te comprend, même toi tu ne te comprends pas
- **Paranoïa** : Tu interprètes tout, tu vois des signaux partout

## Conseil pratique

Écris tout ce qui te traverse la tête pour l'ancrer dans le réel — sinon ça s'évapore.

## Attention

Gare aux addictions intellectuelles — Neptune peut te faire fuir dans les théories conspirationnistes."""
    },
    {
        "planet1": "mercury",
        "planet2": "neptune",
        "aspect_type": "trine",
        "content": """# △ Trigone Mercure - Neptune

**En une phrase :** Ton esprit devient art — tu penses avec ton âme

## L'énergie de cet aspect

Ton intellect (Mercure) et ton imaginaire (Neptune) s'harmonisent ce mois-ci. Tes idées ont de la profondeur, de la poésie. Tu comprends l'invisible. Ta communication devient inspirante, touchante.

## Manifestations concrètes

- **Intuition claire** : Tu captes le non-dit avec précision
- **Écriture inspirée** : Si tu écris, c'est beau, profond, touchant
- **Empathie mentale** : Tu comprends les gens sans qu'ils parlent

## Conseil pratique

Crée quelque chose — écris, peins, compose — ton esprit peut donner forme au subtil.

## Attention

Attention à l'évasion — Neptune peut te faire fuir le réel dans l'imaginaire."""
    },
    {
        "planet1": "mercury",
        "planet2": "neptune",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mercure - Neptune

**En une phrase :** Tu comprends l'invisible — tes pensées touchent le mystère

## L'énergie de cet aspect

Ton intellect (Mercure) et ton intuition (Neptune) se stimulent ce mois-ci. Tu apprends sur le subtil. Tes conversations deviennent profondes. Tu comprends ce qui ne se dit pas.

## Manifestations concrètes

- **Apprentissages spirituels** : Tu explores des sujets mystiques, psychologiques, symboliques
- **Communication sensible** : Tu trouves les mots pour ce qui n'a pas de mots
- **Intuition mesurée** : Tu fais confiance à ton ressenti sans perdre ton esprit critique

## Conseil pratique

Étudie un sujet qui t'intrigue sur le plan spirituel — ton esprit peut maintenant comprendre le mystère.

## Attention

Gare à la naïveté — Neptune peut te faire croire des choses fausses juste parce qu'elles sont belles."""
    },

    # === MERCURY-PLUTO (5 aspects) ===
    {
        "planet1": "mercury",
        "planet2": "pluto",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mercure - Pluton

**En une phrase :** Ton esprit creuse — tu vois ce que les autres cachent

## L'énergie de cet aspect

Ton intellect (Mercure) fusionne avec ton besoin de vérité (Pluton) ce mois-ci. Tu ne te contentes plus des apparences. Tu cherches ce qui se cache derrière les mots, les sourires, les façades. Ton esprit devient détective, obsessionnel.

## Manifestations concrètes

- **Pensée profonde** : Tu creuses jusqu'à la racine de chaque question
- **Communication intense** : Tes mots percent les défenses, tu dis ce qui ne doit pas être dit
- **Obsessions mentales** : Une idée te hante, tu ne peux plus t'arrêter d'y penser

## Conseil pratique

Enquête sur un sujet qui t'obsède — ton esprit peut maintenant aller au fond des choses.

## Attention

Gare à la paranoïa — Pluton peut te faire voir des complots partout."""
    },
    {
        "planet1": "mercury",
        "planet2": "pluto",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mercure - Pluton

**En une phrase :** Tes mots deviennent armes — chaque phrase peut détruire

## L'énergie de cet aspect

Ton besoin de communiquer (Mercure) s'oppose à ton besoin de contrôle (Pluton) ce mois-ci. Tu veux dire la vérité mais elle sort de façon brutale, destructrice. Les autres te trouvent manipulateur même si tu ne l'es pas. Cette tension crée des conflits violents.

## Manifestations concrètes

- **Communication toxique** : Tes mots blessent même si ce n'est pas ton intention
- **Manipulation perçue** : Les autres te reprochent de vouloir les contrôler
- **Conflits verbaux** : Les disputes deviennent guerres psychologiques

## Conseil pratique

Compte jusqu'à 10 avant de dire ce que tu penses — la vérité peut être dite sans détruire.

## Attention

Attention au harcèlement — Pluton peut transformer ta communication en violence psychologique."""
    },
    {
        "planet1": "mercury",
        "planet2": "pluto",
        "aspect_type": "square",
        "content": """# □ Carré Mercure - Pluton

**En une phrase :** Ton esprit t'obsède — chaque pensée devient fixation

## L'énergie de cet aspect

Ton intellect (Mercure) entre en guerre avec ton besoin de contrôle (Pluton) ce mois-ci. Tu rumines des pensées noires. Tu ne lâches rien mentalement. Cette guerre intérieure crée de l'anxiété obsessionnelle, parfois de la paranoïa.

## Manifestations concrètes

- **Rumination obsessionnelle** : Tu tournes en boucle sur les mêmes pensées sombres
- **Communication manipulatrice** : Tu utilises les mots pour contrôler sans t'en rendre compte
- **Pensées intrusives** : Des idées violentes, dérangeantes, que tu ne veux pas

## Conseil pratique

Écris tes pensées obsessionnelles puis brûle le papier — libère ton esprit de cette emprise.

## Attention

Gare à l'autodestruction mentale — Pluton peut transformer tes pensées en torture."""
    },
    {
        "planet1": "mercury",
        "planet2": "pluto",
        "aspect_type": "trine",
        "content": """# △ Trigone Mercure - Pluton

**En une phrase :** Ton esprit devient laser — tu perces tout mensonge

## L'énergie de cet aspect

Ton intellect (Mercure) et ta capacité à voir en profondeur (Pluton) collaborent ce mois-ci. Tu comprends les non-dits, les motivations cachées, les vérités enfouies. Ta communication devient puissante, transformatrice.

## Manifestations concrètes

- **Perspicacité redoutable** : Tu vois à travers les apparences, les mensonges
- **Communication transformante** : Tes mots changent les gens, ils touchent profond
- **Recherche approfondie** : Tu arrives au fond des sujets complexes, obscurs

## Conseil pratique

Utilise ton regard perçant pour aider les autres à voir leur vérité — tu as ce pouvoir maintenant.

## Attention

Attention à devenir cynique — voir la vérité partout peut te faire perdre l'innocence."""
    },
    {
        "planet1": "mercury",
        "planet2": "pluto",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mercure - Pluton

**En une phrase :** Tu apprends les secrets — chaque mystère t'appelle

## L'énergie de cet aspect

Ton intellect (Mercure) et ton besoin de profondeur (Pluton) se stimulent ce mois-ci. Tu explores ce qui est caché, tabou, interdit. Tes conversations deviennent intenses. Tu veux comprendre ce que personne ne dit.

## Manifestations concrètes

- **Curiosité profonde** : Tu t'intéresses aux sujets sombres, psychologiques, interdits
- **Communication directe** : Tu oses dire ce que les autres n'osent pas
- **Apprentissages transformants** : Ce que tu apprends change ta vision du monde

## Conseil pratique

Explore un sujet tabou qui t'intrigue — psychologie, mort, sexualité, pouvoir — ton esprit peut encaisser.

## Attention

Gare à l'obsession — Pluton peut te faire perdre dans les profondeurs sans retour."""
    }
]


async def insert_batch_16():
    """Insère les 10 aspects du Batch 16 en base de données."""

    print(f"=== Insertion Batch 16 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_16())
