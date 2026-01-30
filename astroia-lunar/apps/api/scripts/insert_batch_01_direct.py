#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 1 en base de données (version=5)
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

# Les 10 aspects du Batch 1
ASPECTS = [
    {
        "planet1": "sun",
        "planet2": "venus",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Soleil - Vénus

**En une phrase :** Ton charme devient ton super-pouvoir — tu rayonnes sans effort

## L'énergie de cet aspect

Ce mois-ci, ton identité profonde (Soleil) et ce que tu aimes (Vénus) ne font qu'un. Les gens te sourient plus facilement, les conversations coulent, tu te sens dans ton élément. Ce n'est pas de la chance — c'est ton authenticité qui brille.

## Manifestations concrètes

- **Relations fluides** : Tu trouves les mots justes, les échanges sont chaleureux et sincères
- **Créativité magnétique** : Envie de créer du beau qui te ressemble — et les autres adhèrent
- **Charisme naturel** : En groupe, tu attires l'attention sans forcer, tes idées passent mieux

## Conseil pratique

Lance ce projet créatif qui te trotte dans la tête, ou dis enfin ce que tu repousses. Ton authenticité est ton meilleur atout ce mois-ci.

## Attention

Gare à vouloir plaire à tout prix — ton charme peut te faire dire oui à des choses qui ne te correspondent pas vraiment."""
    },
    {
        "planet1": "sun",
        "planet2": "venus",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Soleil - Vénus

**En une phrase :** Tiraillé entre ce que tu es et ce que tu désires — équilibre à trouver

## L'énergie de cet aspect

Ce mois-ci, ton identité profonde (Soleil) et tes désirs relationnels (Vénus) se font face. Tu pourrais ressentir une tension entre t'affirmer pleinement et maintenir l'harmonie avec les autres. C'est comme si une partie de toi voulait briller seul, tandis qu'une autre cherche l'approbation et la connexion.

## Manifestations concrètes

- **Relations en tension** : Tu oscilles entre dire ce que tu penses vraiment et adoucir pour préserver la paix
- **Choix cornéliens** : Hésitation entre un projet personnel ambitieux et une activité qui plaira à ton entourage
- **Besoin de reconnaissance** : Tu cherches la validation extérieure tout en sachant que tu devrais te suffire à toi-même

## Conseil pratique

Trouve le juste milieu : affirme-toi sans écraser, écoute les autres sans t'effacer. La tension n'est pas un problème, c'est une invitation à l'équilibre.

## Attention

Gare à sacrifier tes valeurs pour plaire, ou à l'inverse, à rejeter toute forme de compromis. L'opposition demande un pont, pas un camp."""
    },
    {
        "planet1": "sun",
        "planet2": "venus",
        "aspect_type": "square",
        "content": """# □ Carré Soleil - Vénus

**En une phrase :** Tes désirs et ton identité se frottent — l'étincelle peut créer ou brûler

## L'énergie de cet aspect

Ce mois-ci, ton identité (Soleil) et tes valeurs affectives (Vénus) se challengent mutuellement. Tu pourrais ressentir une friction interne : "Est-ce que je fais ça pour moi ou pour séduire ?" Cette tension te pousse à clarifier ce qui compte vraiment, même si c'est inconfortable.

## Manifestations concrètes

- **Choix difficiles** : Tiraillé entre un choix authentique mais risqué, et une option sûre mais fade
- **Relations challengées** : Des conversations franches mais tendues qui remettent les compteurs à zéro
- **Insatisfaction créative** : Envie de créer quelque chose qui te ressemble, mais doute sur le résultat

## Conseil pratique

Ne fuis pas l'inconfort — cette friction révèle ce qui est non négociable pour toi. Utilise la tension comme carburant, pas comme frein.

## Attention

Attention à la surcompensation : vouloir tellement prouver ton authenticité que tu deviens rigide, ou céder trop vite pour éviter le conflit."""
    },
    {
        "planet1": "sun",
        "planet2": "venus",
        "aspect_type": "trine",
        "content": """# △ Trigone Soleil - Vénus

**En une phrase :** Charme fluide et créativité facile — ton mois en mode grâce

## L'énergie de cet aspect

Ce mois-ci, ton identité (Soleil) et tes valeurs (Vénus) s'harmonisent sans effort. Tu te sens aligné : ce que tu veux coïncide naturellement avec ce que tu es. Les portes s'ouvrent, les gens sont réceptifs, ta créativité coule comme une source. C'est ton mois de grâce sociale et artistique.

## Manifestations concrètes

- **Relations fluides** : Les échanges sont légers, chaleureux, les malentendus se dissolvent d'eux-mêmes
- **Opportunités créatives** : Une idée, un projet, une collaboration tombent pile au bon moment
- **Confiance naturelle** : Tu te sens bien dans ta peau, et ça se voit — ton charisme opère en douceur

## Conseil pratique

Profite de cette fluidité pour initier des projets créatifs, renforcer tes relations ou simplement savourer ce moment de grâce. Ne le gâche pas en cherchant la petite bête.

## Attention

Attention à la facilité qui endort — ce trigone peut te rendre passif si tu ne saisis pas les opportunités qui se présentent."""
    },
    {
        "planet1": "sun",
        "planet2": "venus",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Soleil - Vénus

**En une phrase :** Des petites portes s'ouvrent — à toi de les pousser

## L'énergie de cet aspect

Ce mois-ci, ton identité (Soleil) et tes valeurs (Vénus) collaborent harmonieusement, mais sans automatisme. Des opportunités relationnelles ou créatives apparaissent, mais elles demandent un petit coup de pouce de ta part. C'est un aspect d'opportunité douce : la chance te tend la main, à toi de la saisir.

## Manifestations concrètes

- **Occasions sociales** : Une invitation, une rencontre, une conversation qui pourrait déboucher sur quelque chose
- **Projets créatifs accessibles** : Une idée réalisable si tu t'y mets maintenant, sans pression
- **Petits gestes payants** : Un compliment bien placé, un message envoyé au bon moment — l'effet est amplifié

## Conseil pratique

Repère les petites ouvertures et agis dessus sans attendre. Le sextile récompense l'initiative légère, pas la procrastination.

## Attention

Gare à laisser passer les occasions par flemme ou indécision — ce mois-ci, c'est toi qui dois faire le premier pas."""
    },
    {
        "planet1": "sun",
        "planet2": "mars",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Soleil - Mars

**En une phrase :** Ton moteur tourne à plein régime — énergie explosive à canaliser

## L'énergie de cet aspect

Ce mois-ci, ton identité (Soleil) et ton élan d'action (Mars) fusionnent dans une intensité maximale. Tu déborde d'énergie, d'envie d'agir, de foncer. C'est ton mois guerrier : courage, initiative, et une capacité à démarrer des projets qui te ressemblent vraiment. Mais attention à la surchauffe.

## Manifestations concrètes

- **Énergie débordante** : Besoin de bouger, de créer, de lancer — rester passif devient insupportable
- **Affirmation directe** : Tu dis ce que tu penses sans filtre, tu défends tes positions avec conviction
- **Projets ambitieux** : Envie de démarrer quelque chose de gros, de te lancer dans l'inconnu

## Conseil pratique

Canalise cette énergie dans un projet concret qui te tient à cœur. Lance-toi maintenant, c'est ton mois d'action — mais choisis bien ta bataille.

## Attention

Gare à l'impulsivité brûlante — tu pourrais démarrer trop vite, te disperser, ou blesser par excès de franchise. Le feu a besoin d'une direction."""
    },
    {
        "planet1": "sun",
        "planet2": "mars",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Soleil - Mars

**En une phrase :** Ton identité face à ton élan — confrontation productive ou clash stérile

## L'énergie de cet aspect

Ce mois-ci, ton identité (Soleil) et ton action (Mars) se font face dans une tension dynamique. Tu pourrais ressentir une opposition interne : "Je sais qui je suis, mais je n'arrive pas à agir en conséquence." Ou externe : conflits avec des personnes qui te challengent. Cette tension demande de l'équilibre entre affirmation et diplomatie.

## Manifestations concrètes

- **Confrontations directes** : Désaccords francs avec des proches ou collègues qui remettent tes positions en question
- **Frustration d'action** : Envie d'agir mais obstacles extérieurs, ou hésitation entre deux directions opposées
- **Énergie explosive** : Impatience, irritabilité, besoin de prouver quelque chose

## Conseil pratique

Utilise cette tension comme carburant pour clarifier tes priorités. Affirme-toi fermement sans partir en guerre — l'opposition te pousse à grandir.

## Attention

Attention aux conflits ego vs ego — si tu cherches à avoir raison plutôt qu'à avancer, tu gaspilles cette énergie puissante."""
    },
    {
        "planet1": "sun",
        "planet2": "mars",
        "aspect_type": "square",
        "content": """# □ Carré Soleil - Mars

**En une phrase :** La friction te propulse — si tu ne te brûles pas d'abord

## L'énergie de cet aspect

Ce mois-ci, ton identité (Soleil) et ton action (Mars) se frottent dans une tension électrique. Tu ressens une urgence d'agir, mais quelque chose bloque ou résiste. C'est frustrant, mais c'est aussi un carburant puissant : cette friction peut te propulser vers l'avant si tu l'utilises bien.

## Manifestations concrètes

- **Impatience chronique** : Envie que les choses avancent plus vite, irritation face aux lenteurs
- **Actions impulsives** : Tu pourrais démarrer brusquement un projet sans plan, juste pour sortir de la frustration
- **Conflits directs** : Disputes franches, mots qui dépassent, besoin de dire les choses même si ça casse

## Conseil pratique

Transforme l'irritation en action constructive : sport intense, projet ambitieux, confrontation nécessaire. Ne laisse pas la tension te ronger de l'intérieur.

## Attention

Gare à l'explosion incontrôlée — tu pourrais blesser, casser, ou démarrer quelque chose que tu regretteras. Canalise, ne gaspille pas."""
    },
    {
        "planet1": "sun",
        "planet2": "mars",
        "aspect_type": "trine",
        "content": """# △ Trigone Soleil - Mars

**En une phrase :** Ton énergie coule fluide — mois d'action naturelle et de victoires faciles

## L'énergie de cet aspect

Ce mois-ci, ton identité (Soleil) et ton action (Mars) s'alignent parfaitement. Tu sais ce que tu veux, et tu as l'énergie pour y aller. Les obstacles semblent fondre, les initiatives portent leurs fruits rapidement. C'est ton mois de performance naturelle, où l'effort devient plaisir.

## Manifestations concrètes

- **Projets qui avancent seuls** : Ce que tu lances prend forme rapidement, sans résistance majeure
- **Énergie soutenue** : Endurance physique et mentale au top, envie de te dépasser sans t'épuiser
- **Leadership naturel** : Les autres te suivent facilement, tes décisions sont claires et justes

## Conseil pratique

Profite de ce mois pour lancer des projets ambitieux, prendre des initiatives, ou concrétiser ce que tu repousses depuis des mois. L'élan est avec toi.

## Attention

Attention à l'excès de confiance — même si tout coule, garde un œil sur les détails et ne néglige pas les conseils extérieurs."""
    },
    {
        "planet1": "sun",
        "planet2": "mars",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Soleil - Mars

**En une phrase :** L'action devient accessible — à toi de saisir l'élan

## L'énergie de cet aspect

Ce mois-ci, ton identité (Soleil) et ton action (Mars) collaborent harmonieusement, mais sans automatisme. Des opportunités d'agir apparaissent, mais elles demandent que tu te lèves et que tu les saisisses. C'est un aspect d'opportunité active : la chance favorise ceux qui bougent.

## Manifestations concrètes

- **Petites victoires accessibles** : Un objectif réalisable si tu t'y mets maintenant, sans forcer
- **Initiatives bien reçues** : Tes propositions passent mieux que d'habitude, les gens te suivent
- **Énergie disponible** : Tu as les ressources pour agir, mais c'est à toi de décider de les utiliser

## Conseil pratique

Identifie une action concrète que tu repousses et fais-la ce mois-ci. Le sextile te donne l'élan, mais tu dois faire le premier pas.

## Attention

Gare à la procrastination — ce mois-ci récompense l'initiative, pas l'attente. Si tu ne bouges pas, rien ne se passera."""
    }
]


async def insert_batch_01():
    """Insère les 10 aspects du Batch 1 en base de données."""

    print("=== Insertion Batch 1 (10 aspects) ===\n")

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
    print(f"📊 Progression : {count}/130 aspects (7.7%)")


if __name__ == '__main__':
    asyncio.run(insert_batch_01())
