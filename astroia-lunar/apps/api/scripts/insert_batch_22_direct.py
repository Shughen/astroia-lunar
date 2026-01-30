#!/usr/bin/env python3
"""
Insertion directe des 15 aspects du Batch 22 en base de données (version=5)
Généré manuellement - Paires: uranus-neptune (5) + uranus-pluto (5) + neptune-pluto (5)
Extension : aspects secondaires 8/8 - FINAL
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

# Les 15 derniers aspects du Batch 22
ASPECTS = [
    # === URANUS-NEPTUNE (5 aspects) ===
    {
        "planet1": "uranus",
        "planet2": "neptune",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Uranus - Neptune

**En une phrase :** Tu veux l'utopie totale — tu casses tout pour un rêve flou

## L'énergie de cet aspect

Ton besoin de rupture (Uranus) fusionne avec ton imaginaire (Neptune) ce mois-ci. Tu veux une révolution spirituelle. Tu rejettes le vieux monde pour un idéal incertain. C'est visionnaire, c'est confus, c'est dangereux.

## Manifestations concrètes

- **Vision utopique** : Tu vois un futur parfait que personne ne voit
- **Ruptures mystiques** : Tu quittes tout pour suivre une intuition
- **Confusion révolutionnaire** : Tu veux changer le monde sans savoir comment

## Conseil pratique

Ancre ta vision dans une action concrète — un rêve sans acte n'est qu'évasion.

## Attention

Gare aux gourous — Uranus-Neptune attire ceux qui promettent l'éveil par la destruction."""
    },
    {
        "planet1": "uranus",
        "planet2": "neptune",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Uranus - Neptune

**En une phrase :** Tu veux te libérer mais tu te perds — chaque rupture t'éloigne de toi

## L'énergie de cet aspect

Ton besoin d'indépendance (Uranus) s'oppose à ton besoin de fusion (Neptune) ce mois-ci. Tu veux être libre mais tu ne sais plus qui tu es. Tu te bats contre les illusions en créant d'autres illusions. Cette tension crée de la désorientation.

## Manifestations concrètes

- **Perte d'identité** : Plus tu te libères, moins tu sais qui tu es
- **Rébellion floue** : Tu te bats sans savoir contre quoi ni pour quoi
- **Évasion par rupture** : Tu quittes tout mais tu fuis juste toi-même

## Conseil pratique

Arrête-toi et demande-toi : de quoi est-ce que je veux vraiment me libérer ?

## Attention

Attention à la fuite — Uranus-Neptune peut te faire errer sans jamais te trouver."""
    },
    {
        "planet1": "uranus",
        "planet2": "neptune",
        "aspect_type": "square",
        "content": """# □ Carré Uranus - Neptune

**En une phrase :** Tu casses tout sans savoir pourquoi — tu détruis par confusion

## L'énergie de cet aspect

Ton besoin de rupture (Uranus) entre en conflit avec tes illusions (Neptune) ce mois-ci. Tu crois te rebeller mais tu fuis. Tu penses innover mais tu te perds. Cette guerre crée du chaos, de l'errance, parfois de l'addiction.

## Manifestations concrètes

- **Ruptures impulsives** : Tu quittes tout par confusion, pas par choix
- **Rébellion destructrice** : Tu casses sans construire
- **Addictions libératrices** : Drogue, alcool, mysticisme — tu cherches la liberté dans la dissolution

## Conseil pratique

Identifie une vraie contrainte à briser et une vraie vision à suivre — sinon tu détruis dans le vide.

## Attention

Gare à la perdition — Uranus-Neptune peut te faire tout perdre sans te libérer."""
    },
    {
        "planet1": "uranus",
        "planet2": "neptune",
        "aspect_type": "trine",
        "content": """# △ Trigone Uranus - Neptune

**En une phrase :** Tu incarnes l'impossible — ton rêve devient innovation

## L'énergie de cet aspect

Ton besoin de liberté (Uranus) et ton imaginaire (Neptune) s'harmonisent ce mois-ci. Tu arrives à matérialiser des visions. Ton art change les gens. Ta spiritualité libère. C'est rare, c'est puissant.

## Manifestations concrètes

- **Art visionnaire** : Tu crées quelque chose qui n'existait pas, qui touche l'âme
- **Libération spirituelle** : Ta quête t'affranchit vraiment
- **Innovation subtile** : Tu inventes dans l'invisible, dans le symbolique

## Conseil pratique

Crée une œuvre qui porte ta vision — film, musique, mouvement — tu peux changer la conscience collective.

## Attention

Attention au détachement — même libéré, il faut rester incarné."""
    },
    {
        "planet1": "uranus",
        "planet2": "neptune",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Uranus - Neptune

**En une phrase :** Tu explores l'inconnu avec confiance — chaque intuition te libère

## L'énergie de cet aspect

Ton besoin de nouveauté (Uranus) et ton intuition (Neptune) se complètent ce mois-ci. Tu oses suivre des signes. Tu explores des voies mystérieuses. Tu te libères en suivant ton ressenti.

## Manifestations concrètes

- **Intuitions libératrices** : Tes pressentiments te montrent des sorties
- **Créativité décalée** : Tu inventes des formes nouvelles, poétiques
- **Spiritualité authentique** : Ta quête ne suit aucune règle, juste ton cœur

## Conseil pratique

Suis une intuition qui te sort de ta zone de confort — ton instinct sait où aller.

## Attention

Gare à l'évasion douce — Neptune peut déguiser la fuite en libération."""
    },

    # === URANUS-PLUTO (5 aspects) ===
    {
        "planet1": "uranus",
        "planet2": "pluto",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Uranus - Pluton

**En une phrase :** Tu veux tout détruire pour tout recréer — révolution totale

## L'énergie de cet aspect

Ton besoin de rupture (Uranus) fusionne avec ton besoin de transformation (Pluton) ce mois-ci. Tu veux tout raser pour reconstruire. Ton pouvoir de changement est colossal. Tu peux être révolutionnaire ou destructeur.

## Manifestations concrètes

- **Transformations radicales** : Tu changes tout d'un coup, brutalement
- **Pouvoir disruptif** : Ton impact révolutionne ce que tu touches
- **Rage révolutionnaire** : Tu veux détruire l'ancien monde

## Conseil pratique

Canalise ce pouvoir vers une vraie révolution — sociale, créative, personnelle — pas vers la destruction gratuite.

## Attention

Gare au chaos — Uranus-Pluton peut tout détruire, toi y compris."""
    },
    {
        "planet1": "uranus",
        "planet2": "pluto",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Uranus - Pluton

**En une phrase :** Tu luttes contre ton propre pouvoir — tu as peur de ta force

## L'énergie de cet aspect

Ton besoin de liberté (Uranus) s'oppose à ton besoin de contrôle (Pluton) ce mois-ci. Tu veux te libérer mais tu as peur de ce que tu pourrais faire libre. Cette tension crée des sabotages, des explosions.

## Manifestations concrètes

- **Peur de son pouvoir** : Tu bloques ta force par peur de ce qu'elle ferait
- **Conflits violents** : Tes ruptures deviennent guerres
- **Auto-sabotage explosif** : Tu détruis ce que tu crées par peur de devenir trop puissant

## Conseil pratique

Identifie ce qui te fait peur dans ta puissance — puis demande-toi si cette peur est réelle.

## Attention

Attention à la violence — Uranus-Pluton peut exploser de façon irréversible."""
    },
    {
        "planet1": "uranus",
        "planet2": "pluto",
        "aspect_type": "square",
        "content": """# □ Carré Uranus - Pluton

**En une phrase :** Tu exploses sans prévenir — ta rage détruit tout sur son passage

## L'énergie de cet aspect

Ton besoin de rupture (Uranus) entre en guerre avec ton ombre (Pluton) ce mois-ci. Tu accumules la rage puis tu exploses. Tes révolutions deviennent destructions. Cette guerre crée des dégâts permanents.

## Manifestations concrètes

- **Colère révolutionnaire** : Ta rage devient violence politique, personnelle, totale
- **Destruction compulsive** : Tu casses tout par besoin de libération
- **Gestes irréversibles** : Tu fais des choses que tu ne pourras jamais défaire

## Conseil pratique

Trouve un exutoire pour ta rage — boxe, art violent, combat politique — évacue avant d'exploser.

## Attention

Gare aux actes irréversibles — Uranus-Pluton peut créer des catastrophes."""
    },
    {
        "planet1": "uranus",
        "planet2": "pluto",
        "aspect_type": "trine",
        "content": """# △ Trigone Uranus - Pluton

**En une phrase :** Tu transformes en libérant — ton pouvoir révolutionne en profondeur

## L'énergie de cet aspect

Ton besoin de liberté (Uranus) et ton pouvoir de transformation (Pluton) collaborent ce mois-ci. Tu arrives à changer les choses radicalement sans détruire. Ton impact est profond, révolutionnaire, libérateur.

## Manifestations concrètes

- **Révolutions réussies** : Ce que tu changes tient dans le temps
- **Pouvoir transformant** : Ton influence libère les autres profondément
- **Innovation radicale** : Tu inventes des formes qui changent tout

## Conseil pratique

Lance une révolution qui compte — mouvement social, art disruptif, transformation systémique — tu as ce pouvoir.

## Attention

Attention à l'ivresse révolutionnaire — même juste, le pouvoir peut corrompre."""
    },
    {
        "planet1": "uranus",
        "planet2": "pluto",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Uranus - Pluton

**En une phrase :** Tu découvres ton pouvoir de rupture — chaque libération te transforme

## L'énergie de cet aspect

Ton besoin de liberté (Uranus) et ta capacité de transformation (Pluton) se stimulent ce mois-ci. Tu oses rompre avec ce qui te bride. Chaque rupture te révèle ta puissance. Tu grandis en te libérant.

## Manifestations concrètes

- **Libérations progressives** : Tu te libères étape par étape, sans tout casser
- **Transformations audacieuses** : Tu changes profondément en osant
- **Pouvoir authentique** : Tu découvres ta vraie force en brisant tes chaînes

## Conseil pratique

Libère-toi d'une contrainte qui t'étouffe — teste ton pouvoir de rupture.

## Attention

Gare à la fascination pour la destruction — briser n'est pas toujours libérer."""
    },

    # === NEPTUNE-PLUTO (5 aspects) ===
    {
        "planet1": "neptune",
        "planet2": "pluto",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Neptune - Pluton

**En une phrase :** Ton rêve devient obsession — tu cherches la transcendance totale

## L'énergie de cet aspect

Ton imaginaire (Neptune) fusionne avec ton besoin de transformation (Pluton) ce mois-ci. Tu veux mourir pour renaître. Tu cherches la dissolution totale, la transcendance absolue. C'est mystique, c'est dangereux.

## Manifestations concrètes

- **Quête spirituelle obsessionnelle** : Tu veux l'éveil total, maintenant
- **Dissolution identitaire** : Tu veux perdre ton ego pour trouver l'absolu
- **Addictions transformatrices** : Drogues, mysticisme extrême — tu veux dissoudre la réalité

## Conseil pratique

Cherche la transcendance dans l'art, pas dans la destruction — crée au lieu de te perdre.

## Attention

Gare à la perdition — Neptune-Pluton peut te faire tout dissoudre, toi y compris."""
    },
    {
        "planet1": "neptune",
        "planet2": "pluto",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Neptune - Pluton

**En une phrase :** Tu veux fusionner mais tu as peur de disparaître — tu ne lâches rien

## L'énergie de cet aspect

Ton besoin de dissolution (Neptune) s'oppose à ton besoin de contrôle (Pluton) ce mois-ci. Tu veux te fondre dans l'absolu mais tu as peur de perdre ton pouvoir. Cette tension crée de la paranoïa spirituelle.

## Manifestations concrètes

- **Contrôle spirituel** : Tu veux maîtriser le mystère, c'est impossible
- **Paranoïa mystique** : Tu vois des forces obscures partout
- **Peur de la dissolution** : Tu rejettes ce qui pourrait te transformer

## Conseil pratique

Lâche prise sur une chose — prouve-toi que perdre le contrôle ne te détruit pas.

## Attention

Attention aux sectes — Neptune-Pluton attire ceux qui promettent le pouvoir par la dissolution."""
    },
    {
        "planet1": "neptune",
        "planet2": "pluto",
        "aspect_type": "square",
        "content": """# □ Carré Neptune - Pluton

**En une phrase :** Tu te noies dans ton ombre — tes peurs deviennent cauchemars

## L'énergie de cet aspect

Ton imaginaire (Neptune) entre en guerre avec tes terreurs (Pluton) ce mois-ci. Tes rêves deviennent noirs. Tes peurs prennent des formes monstrueuses. Cette guerre crée de l'angoisse existentielle, parfois de la folie.

## Manifestations concrètes

- **Cauchemars obsédants** : Tes nuits deviennent terreur
- **Paranoïa spirituelle** : Tu vois le mal partout, dans l'invisible
- **Dépression mystique** : Tu perds foi en tout, même en toi

## Conseil pratique

Nomme ta peur la plus profonde — donne-lui une forme, sors-la du flou, affronte-la.

## Attention

Gare à la psychose — Neptune-Pluton peut brouiller la frontière entre réel et imaginaire."""
    },
    {
        "planet1": "neptune",
        "planet2": "pluto",
        "aspect_type": "trine",
        "content": """# △ Trigone Neptune - Pluton

**En une phrase :** Tu touches l'absolu — ta spiritualité transforme en profondeur

## L'énergie de cet aspect

Ton imaginaire (Neptune) et ta capacité de transformation (Pluton) s'harmonisent ce mois-ci. Tu arrives à vivre la transcendance sans te perdre. Ton art touche l'âme. Ta spiritualité guérit. C'est rare, c'est sacré.

## Manifestations concrètes

- **Guérison spirituelle** : Tu touches les blessures profondes par l'art, la présence, la prière
- **Art transcendant** : Ce que tu crées change les gens en profondeur
- **Transformation mystique** : Tu meurs et renais sans te détruire

## Conseil pratique

Crée une œuvre ou une pratique qui touche l'invisible — tu as ce pouvoir de guérison.

## Attention

Attention à l'isolement — même connecté à l'absolu, il faut rester humain."""
    },
    {
        "planet1": "neptune",
        "planet2": "pluto",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Neptune - Pluton

**En une phrase :** Tu explores ton ombre avec douceur — chaque mystère te transforme

## L'énergie de cet aspect

Ton intuition (Neptune) et ta capacité à voir en profondeur (Pluton) se complètent ce mois-ci. Tu explores tes zones sombres sans te détruire. Tu comprends le mystère progressivement. Tu guéris en douceur.

## Manifestations concrètes

- **Guérison progressive** : Tu soignes tes blessures par le symbolique, le rêve, l'art
- **Compréhension profonde** : Tu captes ce qui est caché sans forcer
- **Transformation douce** : Tu changes en profondeur sans violence

## Conseil pratique

Explore ton ombre par l'art ou le rêve — dessine tes peurs, écris tes cauchemars, transforme-les.

## Attention

Gare à l'évasion — Neptune peut te faire fuir ton ombre au lieu de la traverser."""
    }
]


async def insert_batch_22():
    """Insère les 15 derniers aspects du Batch 22 en base de données."""

    print(f"=== Insertion Batch 22 - DERNIER BATCH FINAL ({len(ASPECTS)} aspects) ===\n")

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

    if count >= 210:
        print(f"\n🎉🎉🎉 TOUS LES 210 ASPECTS SONT GÉNÉRÉS ET INSÉRÉS ! 🎉🎉🎉")
        print(f"✨ Aspects prioritaires : 130 aspects (100%)")
        print(f"✨ Aspects secondaires : 80 aspects (100%)")
        print(f"✨ Refonte aspects v5 COMPLÈTE - $0 USD dépensé ✨")


if __name__ == '__main__':
    asyncio.run(insert_batch_22())
