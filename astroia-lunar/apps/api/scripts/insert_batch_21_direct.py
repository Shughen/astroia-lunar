#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 21 en base de données (version=5)
Généré manuellement - Paires: saturn-uranus (5 aspects) + saturn-pluto (5 aspects)
Extension : aspects secondaires 7/8
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

# Les 10 aspects du Batch 21
ASPECTS = [
    # === SATURN-URANUS (5 aspects) ===
    {
        "planet1": "saturn",
        "planet2": "uranus",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Saturne - Uranus

**En une phrase :** Ton ordre explose — tu détruis tes propres structures

## L'énergie de cet aspect

Ta structure (Saturne) fusionne avec ton besoin de liberté (Uranus) ce mois-ci. Tu veux casser tes propres limites. Ce que tu as construit patiemment, tu veux le détruire maintenant. Cette fusion crée du chaos, mais aussi des révolutions personnelles.

## Manifestations concrètes

- **Remise en question radicale** : Tu questionnes tout ce que tu croyais stable
- **Ruptures structurelles** : Tu casses tes habitudes, tes règles, tes cadres
- **Innovation contrainte** : Tu inventes dans les limites, tu crées sous pression

## Conseil pratique

Réforme une structure qui t'étouffe — travail, routine, relation — garde ce qui fonctionne, change le reste.

## Attention

Gare à tout casser — Uranus peut te faire détruire ce qui méritait juste d'être ajusté."""
    },
    {
        "planet1": "saturn",
        "planet2": "uranus",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Saturne - Uranus

**En une phrase :** Tu veux la sécurité et la liberté — impossible d'avoir les deux

## L'énergie de cet aspect

Ton besoin de structure (Saturne) s'oppose à ton besoin d'indépendance (Uranus) ce mois-ci. Dès que tu construis quelque chose, tu veux t'en libérer. Dès que tu es libre, tu as peur du vide. Cette tension crée de l'instabilité chronique.

## Manifestations concrètes

- **Instabilité professionnelle** : Tu quittes des jobs stables pour être libre, puis tu paniques
- **Peur de l'engagement** : Tu veux une structure mais tu fuis dès qu'elle arrive
- **Conflits autorité/autonomie** : Tu te bats contre les règles puis tu les regrettes

## Conseil pratique

Crée une structure flexible — un cadre qui laisse de la place à l'imprévu, une sécurité qui permet la liberté.

## Attention

Attention à la fuite — Uranus peut te faire détruire toute sécurité par peur d'être piégé."""
    },
    {
        "planet1": "saturn",
        "planet2": "uranus",
        "aspect_type": "square",
        "content": """# □ Carré Saturne - Uranus

**En une phrase :** Ta peur te pousse à tout casser — puis tu paniques d'avoir tout cassé

## L'énergie de cet aspect

Ton besoin de contrôle (Saturne) entre en guerre avec ton besoin de rupture (Uranus) ce mois-ci. Tu sabotes tes propres structures par anxiété. Tu veux te libérer mais tu as peur du vide. Cette guerre crée du chaos, de la paralysie.

## Manifestations concrètes

- **Auto-sabotage structurel** : Tu détruis tes bases de sécurité par peur d'être enfermé
- **Anxiété chronique** : La peur de l'enfermement ET la peur du vide te paralysent
- **Ruptures impulsives** : Tu quittes tout brutalement, puis tu regrettes

## Conseil pratique

Identifie une vraie contrainte qui t'étouffe et une vraie liberté que tu veux — agis sur ça, pas sur tout.

## Attention

Gare à la destruction par panique — Uranus-Saturne peut te faire tout perdre par peur de tout perdre."""
    },
    {
        "planet1": "saturn",
        "planet2": "uranus",
        "aspect_type": "trine",
        "content": """# △ Trigone Saturne - Uranus

**En une phrase :** Tu structures ta liberté — tu crées un ordre qui te libère

## L'énergie de cet aspect

Ton besoin de structure (Saturne) et ton besoin d'innovation (Uranus) collaborent ce mois-ci. Tu inventes de nouvelles façons de t'organiser. Tu crées des cadres qui libèrent au lieu d'enfermer. Tu es stable sans être rigide.

## Manifestations concrètes

- **Structures innovantes** : Tu organises ta vie d'une façon unique, efficace, libre
- **Discipline flexible** : Tu as des règles mais tu les adaptes intelligemment
- **Sécurité autonome** : Tu construis une base solide qui permet l'imprévu

## Conseil pratique

Crée un système personnel — routine, méthode, organisation — qui te correspond vraiment, pas qui imite les autres.

## Attention

Attention à l'isolement — trop d'originalité peut te couper des autres."""
    },
    {
        "planet1": "saturn",
        "planet2": "uranus",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Saturne - Uranus

**En une phrase :** Tu testes de nouvelles structures — chaque expérience t'apprend

## L'énergie de cet aspect

Ton besoin de stabilité (Saturne) et ton besoin de nouveauté (Uranus) se stimulent ce mois-ci. Tu oses changer tes habitudes progressivement. Tu testes de nouvelles façons de t'organiser. Tu évolues sans tout casser.

## Manifestations concrètes

- **Réformes mesurées** : Tu changes ce qui ne marche plus sans détruire le reste
- **Innovation pragmatique** : Tu inventes mais tu gardes les pieds sur terre
- **Flexibilité structurée** : Tu acceptes l'imprévu sans perdre ton cadre

## Conseil pratique

Change une habitude par mois — prouve-toi que tu peux évoluer sans tout détruire.

## Attention

Gare à la prudence excessive — parfois il faut aussi oser le grand saut."""
    },

    # === SATURN-PLUTO (5 aspects) ===
    {
        "planet1": "saturn",
        "planet2": "pluto",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Saturne - Pluton

**En une phrase :** Tes limites deviennent prison — tu sens le poids de tout

## L'énergie de cet aspect

Ta structure (Saturne) fusionne avec tes peurs profondes (Pluton) ce mois-ci. Chaque limite devient insurmontable. Tu portes le poids du monde. Tout semble sombre, lourd, impossible. Mais dans cette nuit, tu peux forger du diamant.

## Manifestations concrètes

- **Pression extrême** : Tu sens que tout repose sur toi, c'est écrasant
- **Transformation forcée** : La vie te pousse à changer, tu n'as pas le choix
- **Endurance totale** : Tu découvres que tu peux tenir l'insoutenable

## Conseil pratique

Traverse l'épreuve sans fuir — c'est dans cette pression que tu deviens indestructible.

## Attention

Gare à la dépression — Saturne-Pluton peut transformer la force en désespoir."""
    },
    {
        "planet1": "saturn",
        "planet2": "pluto",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Saturne - Pluton

**En une phrase :** Tu luttes contre ton ombre — chaque limite révèle ta peur

## L'énergie de cet aspect

Ton besoin de contrôle (Saturne) s'oppose à tes terreurs profondes (Pluton) ce mois-ci. Plus tu essaies de te protéger, plus tu te sens menacé. Cette tension crée de la paranoïa, de la rigidité extrême.

## Manifestations concrètes

- **Paranoïa structurelle** : Tu te blindes contre des menaces imaginaires
- **Contrôle obsessionnel** : Tu veux tout maîtriser pour te sentir en sécurité
- **Peurs anciennes** : Tes limites cachent des terreurs d'enfance

## Conseil pratique

Identifie ta peur la plus profonde — puis demande-toi : est-ce qu'elle est encore réelle aujourd'hui ?

## Attention

Attention à la tyrannie — Saturne-Pluton peut te transformer en geôlier de toi-même."""
    },
    {
        "planet1": "saturn",
        "planet2": "pluto",
        "aspect_type": "square",
        "content": """# □ Carré Saturne - Pluton

**En une phrase :** Tes limites te détruisent — tu te punis pour exister

## L'énergie de cet aspect

Ton exigence (Saturne) entre en guerre avec ta culpabilité (Pluton) ce mois-ci. Tu te juges impitoyablement. Chaque erreur devient preuve de ton indignité. Cette guerre intérieure crée de l'auto-punition, de l'isolement.

## Manifestations concrètes

- **Auto-punition** : Tu te prives de tout pour te sentir digne
- **Culpabilité existentielle** : Tu te sens coupable d'exister
- **Isolement volontaire** : Tu te retires pour ne blesser personne

## Conseil pratique

Pardonne-toi une erreur ancienne — prouve à ton ombre que tu mérites de vivre.

## Attention

Gare à l'autodestruction — Saturne-Pluton peut te pousser à te punir jusqu'à te perdre."""
    },
    {
        "planet1": "saturn",
        "planet2": "pluto",
        "aspect_type": "trine",
        "content": """# △ Trigone Saturne - Pluton

**En une phrase :** Tes limites deviennent force — tu construis l'indestructible

## L'énergie de cet aspect

Ton endurance (Saturne) et ta profondeur (Pluton) s'harmonisent ce mois-ci. Ce que tu construis tient dans le temps. Tes structures ont des fondations dans le roc. Tu deviens inébranlable.

## Manifestations concrètes

- **Résilience totale** : Rien ne te détruit, tu encaisses tout
- **Structures profondes** : Ce que tu bâtis a des racines dans l'ombre
- **Pouvoir tranquille** : Ta force est discrète mais absolue

## Conseil pratique

Engage-toi dans un projet qui demande de tenir dans la durée — tu as cette force de roc.

## Attention

Attention à la dureté — même fort, il faut rester humain."""
    },
    {
        "planet1": "saturn",
        "planet2": "pluto",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Saturne - Pluton

**En une phrase :** Tu transformes tes limites — chaque contrainte devient levier

## L'énergie de cet aspect

Ton endurance (Saturne) et ta capacité de transformation (Pluton) se complètent ce mois-ci. Tu utilises tes limites pour te renforcer. Tes contraintes deviennent des outils. Tu grandis à travers l'adversité.

## Manifestations concrètes

- **Transformation patiente** : Tu changes en profondeur, lentement mais sûrement
- **Limites créatives** : Tes contraintes t'obligent à innover
- **Résilience progressive** : Chaque épreuve te rend plus fort

## Conseil pratique

Transforme une limitation en atout — utilise ce qui te freine comme ce qui te propulse.

## Attention

Gare à la glorification de la souffrance — l'épreuve n'est pas nécessaire pour grandir."""
    }
]


async def insert_batch_21():
    """Insère les 10 aspects du Batch 21 en base de données."""

    print(f"=== Insertion Batch 21 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_21())
