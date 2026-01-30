#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 2 en base de données (version=5)
Généré manuellement dans Claude Code
"""

import sys
import asyncio
from pathlib import Path

# Ajouter le dossier parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.dialects.postgresql import insert
from models.pregenerated_natal_aspect import PregeneratedNatalAspect
from config import Settings

settings = Settings()

# Les 10 aspects du Batch 2
ASPECTS = [
    {
        "planet1": "venus",
        "planet2": "mars",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Vénus - Mars

**En une phrase :** Désir et action fusionnent — ton charisme devient électrique

## L'énergie de cet aspect

Tes envies (Vénus) et ton élan d'action (Mars) ne font qu'un ce mois-ci. Quand tu veux quelque chose, tu passes à l'acte immédiatement. Ta séduction devient directe, presque audacieuse. C'est un mélange puissant : le charme de Vénus rencontre le courage de Mars, et ça donne une énergie magnétique irrésistible.

## Manifestations concrètes

- **Séduction assumée** : Tu oses faire le premier pas, déclarer tes intentions, prendre des risques en amour
- **Créativité passionnée** : Tes projets artistiques ont du feu, de l'intensité — tu crées avec audace
- **Désirs clairs** : Tu sais ce que tu veux et tu ne t'excuses pas de le poursuivre

## Conseil pratique

Profite de cette énergie pour initier ce que tu désires vraiment — relation, projet créatif, plaisir. Ton audace paie ce mois-ci.

## Attention

Gare à la pulsion brute — tu pourrais confondre désir et besoin, ou foncer trop vite sans lire les signaux de l'autre."""
    },
    {
        "planet1": "venus",
        "planet2": "mars",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Vénus - Mars

**En une phrase :** Désir contre action — l'attraction naît de la tension

## L'énergie de cet aspect

Tes envies (Vénus) et ton élan (Mars) se font face ce mois-ci, créant une polarité magnétique. Tu pourrais ressentir une tension entre séduire et conquérir, attendre et foncer. Cette opposition génère une attraction électrique — en amour comme en créativité — mais elle demande de l'équilibre.

## Manifestations concrètes

- **Tensions relationnelles** : Attirance forte mais confrontations directes, le désir passe par la friction
- **Hésitation créative** : Envie de créer quelque chose de beau versus envie d'action rapide et brute
- **Jeux de pouvoir** : Qui fait le premier pas ? Qui cède ? L'opposition crée du suspense

## Conseil pratique

Utilise la tension comme carburant : l'opposition Vénus-Mars crée de l'intensité, pas de la distance. Laisse la friction t'exciter plutôt que te bloquer.

## Attention

Attention aux conflits passionnels — si tu cherches à dominer ou à plaire à tout prix, tu rates le pont entre désir et action."""
    },
    {
        "planet1": "venus",
        "planet2": "mars",
        "aspect_type": "square",
        "content": """# □ Carré Vénus - Mars

**En une phrase :** La friction entre désir et action allume le feu

## L'énergie de cet aspect

Tes envies (Vénus) et ton action (Mars) se frottent ce mois-ci dans une tension créative. Tu pourrais ressentir une impatience : "Je veux, mais je n'ose pas" ou "J'agis, mais ça ne correspond pas vraiment à mes valeurs". Cette friction est inconfortable, mais c'est elle qui génère du mouvement.

## Manifestations concrètes

- **Impatience amoureuse** : Envie d'accélérer les choses, mais peur de gâcher la séduction
- **Créativité sous pression** : Frustration entre ce que tu veux créer et ce que tu arrives à faire
- **Actions maladroites** : Tu passes à l'acte trop vite, ou tu temporises alors que tu devrais foncer

## Conseil pratique

Accepte l'inconfort : cette friction te pousse à clarifier ce que tu veux vraiment. Agis malgré la tension, pas en l'évitant.

## Attention

Gare à l'impulsivité frustrée — tu pourrais brusquer une relation ou abandonner un projet par impatience. La friction est un carburant, pas un mur."""
    },
    {
        "planet1": "venus",
        "planet2": "mars",
        "aspect_type": "trine",
        "content": """# △ Trigone Vénus - Mars

**En une phrase :** Séduction fluide et action alignée — ton mois de grâce passionnée

## L'énergie de cet aspect

Tes envies (Vénus) et ton action (Mars) dansent ensemble ce mois-ci. Tu sais ce que tu veux, et tu as le courage d'y aller. La séduction devient naturelle, la créativité coule, les initiatives relationnelles portent leurs fruits. C'est ton mois de charisme actif : tu plais et tu agis en même temps.

## Manifestations concrètes

- **Séduction efficace** : Tes avances sont bien reçues, tu trouves le bon timing sans forcer
- **Projets créatifs réussis** : Ce que tu lances prend forme rapidement, l'esthétique et l'action s'alignent
- **Désirs satisfaits** : Tu obtiens ce que tu veux sans lutte, les portes s'ouvrent d'elles-mêmes

## Conseil pratique

Profite de cette fluidité pour initier des relations, des projets créatifs, ou des plaisirs que tu repousses. L'alignement Vénus-Mars ne dure pas éternellement.

## Attention

Attention à la facilité qui rend paresseux — ce trigone peut te faire oublier que certaines choses nécessitent quand même un effort soutenu."""
    },
    {
        "planet1": "venus",
        "planet2": "mars",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Vénus - Mars

**En une phrase :** Petit coup de pouce pour oser — le désir rencontre le courage

## L'énergie de cet aspect

Tes envies (Vénus) et ton action (Mars) collaborent ce mois-ci, mais sans automatisme. Des opportunités de séduction, de création ou de plaisir apparaissent, mais c'est à toi de saisir l'instant. Le sextile te donne le courage d'oser — à condition que tu fasses le premier geste.

## Manifestations concrètes

- **Occasions relationnelles** : Une personne qui t'attire, un compliment à faire, une invitation à lancer — mais tu dois initier
- **Projets créatifs accessibles** : Une collaboration artistique possible si tu proposes maintenant
- **Petit risque payant** : Oser porter cette tenue, dire cette phrase, proposer cette sortie — l'effet est amplifié

## Conseil pratique

Repère une envie que tu repousses par timidité et passe à l'acte ce mois-ci. Le sextile Vénus-Mars récompense l'audace douce.

## Attention

Gare à l'hésitation — si tu attends que l'autre fasse le premier pas, l'opportunité passe. Ce mois-ci, c'est toi qui dois oser."""
    },
    {
        "planet1": "sun",
        "planet2": "jupiter",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Soleil - Jupiter

**En une phrase :** Ton identité prend de l'ampleur — mois d'optimisme et d'expansion

## L'énergie de cet aspect

Ton identité (Soleil) et ton expansion (Jupiter) fusionnent ce mois-ci dans une énergie généreuse. Tu vois grand, tu te sens capable, confiant. C'est ton mois de croissance personnelle : les opportunités se multiplient, les gens te font confiance, ton optimisme est contagieux. Jupiter amplifie tout — y compris ton ego.

## Manifestations concrètes

- **Confiance débordante** : Tu te sens capable de tout, les doutes s'évaporent
- **Opportunités multiples** : Propositions, invitations, chances qui tombent du ciel
- **Générosité naturelle** : Envie de partager, d'aider, de voir large

## Conseil pratique

Lance des projets ambitieux, prends des risques calculés, dis oui aux opportunités. Jupiter amplifie ton élan — profite de cette vague.

## Attention

Gare à l'excès de confiance — Jupiter peut te faire promettre trop, voir trop grand, ou négliger les détails pratiques. L'expansion a besoin de limites."""
    },
    {
        "planet1": "sun",
        "planet2": "jupiter",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Soleil - Jupiter

**En une phrase :** Identité contre expansion — l'équilibre entre ego et générosité

## L'énergie de cet aspect

Ton identité (Soleil) et ton expansion (Jupiter) se font face ce mois-ci. Tu pourrais ressentir une tension entre rester toi-même et vouloir grandir, entre ton ego et ta générosité. Cette opposition te pousse à trouver la juste mesure : ni trop grand, ni trop petit.

## Manifestations concrètes

- **Tensions d'échelle** : Hésitation entre un projet modeste mais solide, et une ambition démesurée
- **Conflits de valeurs** : Ton identité personnelle versus les attentes sociales ou philosophiques
- **Excès compensatoire** : Osciller entre confiance excessive et doute profond

## Conseil pratique

Trouve le pont entre qui tu es et ce que tu veux devenir. L'opposition n'est pas un choix binaire — c'est une invitation à l'équilibre.

## Attention

Gare à l'inflation de l'ego ou à la fausse modestie — l'opposition Jupiter te pousse à voir clair sur ta vraie mesure."""
    },
    {
        "planet1": "sun",
        "planet2": "jupiter",
        "aspect_type": "square",
        "content": """# □ Carré Soleil - Jupiter

**En une phrase :** L'ambition frotte contre les limites — la friction fait grandir

## L'énergie de cet aspect

Ton identité (Soleil) et ton expansion (Jupiter) se challengent ce mois-ci. Tu ressens une impatience : "Je veux plus, je veux mieux, je veux maintenant." Mais quelque chose résiste — les circonstances, tes propres limites, ou la réalité qui rappelle ses droits. Cette friction est frustrante, mais elle forge ta croissance.

## Manifestations concrètes

- **Ambitions contrariées** : Projets bloqués, reconnaissance qui tarde, envie d'expansion mais obstacles
- **Impatience philosophique** : Frustration entre tes croyances et ta réalité quotidienne
- **Excès compensatoires** : Promettre trop, s'engager dans trop de directions à la fois

## Conseil pratique

Utilise la frustration comme signal : qu'est-ce qui mérite vraiment ton expansion ? Le carré Jupiter te pousse à choisir tes batailles.

## Attention

Gare à l'inflation incontrôlée — tu pourrais promettre ce que tu ne peux pas tenir, ou forcer une croissance qui n'est pas mûre. La patience n'est pas l'ennemi de l'ambition."""
    },
    {
        "planet1": "sun",
        "planet2": "jupiter",
        "aspect_type": "trine",
        "content": """# △ Trigone Soleil - Jupiter

**En une phrase :** Expansion naturelle et chance fluide — ton mois béni

## L'énergie de cet aspect

Ton identité (Soleil) et ton expansion (Jupiter) s'alignent parfaitement ce mois-ci. Les portes s'ouvrent, les gens te font confiance, la chance te sourit. C'est ton mois de croissance facile : ce que tu touches prospère, ce que tu lances prend de l'ampleur. Jupiter bénit ton identité sans effort.

## Manifestations concrètes

- **Opportunités spontanées** : Propositions qui tombent du ciel, rencontres qui changent la donne
- **Réussite naturelle** : Tes projets avancent sans résistance, les résultats dépassent tes attentes
- **Optimisme contagieux** : Ton enthousiasme attire les bonnes personnes et les bonnes situations

## Conseil pratique

Profite de cette vague pour lancer des projets ambitieux, voyager, apprendre, rencontrer. Le trigone Jupiter est rare — ne le gaspille pas en inaction.

## Attention

Attention à prendre cette chance pour acquise — même sous trigone, l'effort compte. Ne deviens pas complaisant sous prétexte que tout coule."""
    },
    {
        "planet1": "sun",
        "planet2": "jupiter",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Soleil - Jupiter

**En une phrase :** Petites portes vers l'expansion — pousse-les maintenant

## L'énergie de cet aspect

Ton identité (Soleil) et ton expansion (Jupiter) collaborent ce mois-ci, mais sans automatisme. Des opportunités de croissance apparaissent — formation, rencontre, voyage, projet — mais c'est à toi de saisir l'instant. Le sextile te donne l'élan optimiste, à toi de transformer ça en action.

## Manifestations concrètes

- **Opportunités d'apprentissage** : Une formation accessible, un livre qui tombe sous la main, une personne inspirante à contacter
- **Petits risques positifs** : Proposer une idée audacieuse, postuler à une opportunité, dire oui à une invitation
- **Expansion douce** : Pas de révolution, mais des petits pas qui élargissent ton horizon

## Conseil pratique

Identifie une opportunité de croissance que tu repousses (formation, voyage, rencontre) et saisis-la ce mois-ci. Le sextile Jupiter récompense l'initiative curieuse.

## Attention

Gare à la procrastination optimiste — "Ça va venir tout seul" est un piège. Le sextile demande que tu bouges, pas que tu attendes."""
    }
]


async def insert_batch_02():
    """Insère les 10 aspects du Batch 2 en base de données."""

    print("=== Insertion Batch 2 (10 aspects) ===\n")

    # Connexion DB
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

                # Upsert (insert ou update)
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

    # Vérifier le total en BD
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
    asyncio.run(insert_batch_02())
