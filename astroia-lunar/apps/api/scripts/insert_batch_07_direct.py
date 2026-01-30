#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 7 en base de données (version=5)
Généré manuellement - Paires: moon-venus (5 aspects) + moon-mars (5 aspects)
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

# Les 10 aspects du Batch 7
ASPECTS = [
    # === MOON-VENUS (5 aspects) ===
    {
        "planet1": "moon",
        "planet2": "venus",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Lune - Vénus

**En une phrase :** Ton cœur déborde — tu veux aimer et être aimé sans retenue

## L'énergie de cet aspect

Tes besoins émotionnels (Lune) fusionnent avec tes désirs affectifs (Vénus) ce mois-ci. Tu ressens une douceur profonde. Tout ce qui touche à l'amour, au plaisir, à la beauté te nourrit. Tu veux te sentir chéri, connecté, apprécié.

## Manifestations concrètes

- **Affection spontanée** : Tu montres ton amour facilement, tu es tendre avec les gens qui comptent
- **Besoin de douceur** : Les ambiances douces, les textures agréables, les attentions te font du bien
- **Créativité sensible** : Tu as envie de créer de la beauté qui touche le cœur

## Conseil pratique

Offre un geste d'amour à quelqu'un — un mot, un cadeau, un moment — ton cœur est généreux.

## Attention

Gare à chercher la sécurité dans l'approbation des autres — ton cœur est précieux même s'il n'est pas aimé de tous."""
    },
    {
        "planet1": "moon",
        "planet2": "venus",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Lune - Vénus

**En une phrase :** Tu donnes trop ou tu retiens — difficile de trouver l'équilibre affectif

## L'énergie de cet aspect

Tes besoins (Lune) et tes désirs relationnels (Vénus) se tirent dessus ce mois-ci. D'un côté tu veux être aimé, de l'autre tu as peur de te perdre dans la relation. Tu oscilles entre donner trop et te protéger trop.

## Manifestations concrètes

- **Dépendance affective** : Tu attends que les autres comblent ton vide émotionnel
- **Retrait défensif** : Dès qu'on te fait du bien, tu te méfies ou tu t'éloignes
- **Relations déséquilibrées** : Tu donnes beaucoup mais tu ne reçois pas assez, ou l'inverse

## Conseil pratique

Demande-toi : qu'est-ce que j'attends vraiment de l'autre ? Puis pose cette demande clairement.

## Attention

Attention à confondre amour et fusion — tu peux exister pleinement tout en aimant."""
    },
    {
        "planet1": "moon",
        "planet2": "venus",
        "aspect_type": "square",
        "content": """# □ Carré Lune - Vénus

**En une phrase :** Tes besoins et tes désirs se contredisent — tu ne sais plus ce que tu veux

## L'énergie de cet aspect

Ce dont tu as besoin (Lune) entre en conflit avec ce que tu désires (Vénus) ce mois-ci. Tu veux qu'on te rassure mais tu rejettes l'affection. Tu cherches la connexion mais tu te sens étouffé. Cette friction crée de l'inconfort relationnel.

## Manifestations concrètes

- **Ambivalence affective** : Tu veux de l'amour mais tu le repousses quand il arrive
- **Insatisfaction chronique** : Rien ne te comble vraiment, tu en veux toujours plus ou différemment
- **Tensions relationnelles** : Tes proches ne savent plus comment te faire plaisir

## Conseil pratique

Identifie un besoin émotionnel non comblé depuis l'enfance — c'est peut-être là que ça coince.

## Attention

Gare à rendre les autres responsables de ton mal-être — ils ne peuvent pas combler un vide que tu ne nommes pas."""
    },
    {
        "planet1": "moon",
        "planet2": "venus",
        "aspect_type": "trine",
        "content": """# △ Trigone Lune - Vénus

**En une phrase :** Tu te sens aimé et tu sais aimer — ton cœur est en paix

## L'énergie de cet aspect

Tes besoins (Lune) et tes capacités d'aimer (Vénus) s'harmonisent ce mois-ci. Tu te sens bien dans tes relations. Donner et recevoir se fait naturellement. Tu apprécies les petits plaisirs, les moments doux, les gens qui comptent.

## Manifestations concrètes

- **Relations apaisées** : Les échanges coulent, personne ne force rien
- **Plaisirs simples** : Un café, une musique, un sourire te remplissent vraiment
- **Générosité naturelle** : Tu donnes sans calcul, tu reçois sans culpabilité

## Conseil pratique

Organise un moment simple avec quelqu'un que tu aimes — un repas, une balade — profite de cette douceur.

## Attention

Attention à éviter les tensions par confort — parfois il faut dire non même quand tout va bien."""
    },
    {
        "planet1": "moon",
        "planet2": "venus",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Lune - Vénus

**En une phrase :** Tu crées du lien en douceur — ton affection touche juste

## L'énergie de cet aspect

Tes besoins émotionnels (Lune) et ta capacité d'aimer (Vénus) se stimulent ce mois-ci. Tu sais ce qui te fait du bien et tu oses le demander. Tu montres ton affection avec délicatesse. Les relations deviennent plus douces, plus vraies.

## Manifestations concrètes

- **Petites attentions** : Tu poses des gestes simples qui font plaisir aux autres
- **Réceptivité fine** : Tu captes ce dont l'autre a besoin sans qu'il le dise
- **Esthétique réconfortante** : Tu embellis ton quotidien, tu crées du cocon

## Conseil pratique

Dis à quelqu'un pourquoi tu l'aimes — un message simple, sincère, qui vient du cœur.

## Attention

Gare à trop adapter tes besoins à ceux des autres — ta douceur ne doit pas te faire oublier."""
    },

    # === MOON-MARS (5 aspects) ===
    {
        "planet1": "moon",
        "planet2": "mars",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Lune - Mars

**En une phrase :** Tes émotions sortent brutes — tu ressens tout et tu réagis vite

## L'énergie de cet aspect

Tes émotions (Lune) fusionnent avec ton impulsion d'action (Mars) ce mois-ci. Quand tu ressens quelque chose, ça se transforme immédiatement en acte. Tu n'as plus de filtre entre ton cœur et tes gestes. Ton intensité émotionnelle devient visible, parfois explosive.

## Manifestations concrètes

- **Réactivité émotionnelle** : Tu t'énerves vite, tu pleures vite, tu ris vite — tout est amplifié
- **Courage instinctif** : Tu défends ce qui compte pour toi sans réfléchir
- **Pulsions immédiates** : Tes besoins deviennent urgents, tu veux tout maintenant

## Conseil pratique

Utilise cette énergie pour défendre une cause qui te touche — ta colère peut servir.

## Attention

Gare aux réactions impulsives — sous le coup de l'émotion, tu peux blesser ou te mettre en danger."""
    },
    {
        "planet1": "moon",
        "planet2": "mars",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Lune - Mars

**En une phrase :** Tu es tiraillé entre la douceur et la colère — lequel choisir ?

## L'énergie de cet aspect

Tes besoins de sécurité (Lune) s'opposent à ton désir d'action (Mars) ce mois-ci. Une partie de toi veut la paix, l'autre veut se battre. Cette tension crée de l'agressivité, de l'irritabilité, parfois des conflits avec les proches.

## Manifestations concrètes

- **Colère défensive** : Tu attaques dès que tu te sens vulnérable
- **Conflits domestiques** : Les tensions explosent à la maison, avec la famille
- **Besoins contradictoires** : Tu veux qu'on te laisse tranquille et qu'on s'occupe de toi en même temps

## Conseil pratique

Trouve un exutoire physique à ta frustration — sport, danse, marche rapide — pour calmer le feu.

## Attention

Attention à blesser ceux qui t'aiment — ta colère vise souvent les mauvaises personnes."""
    },
    {
        "planet1": "moon",
        "planet2": "mars",
        "aspect_type": "square",
        "content": """# □ Carré Lune - Mars

**En une phrase :** Tes émotions te brûlent — tu t'énerves pour un rien

## L'énergie de cet aspect

Tes émotions (Lune) et ton agressivité (Mars) s'entrechoquent ce mois-ci. Tu te sens sur les nerfs. Les petites choses t'irritent. Tes besoins non comblés se transforment en colère. Tu peux devenir cassant, impulsif, parfois violent verbalement.

## Manifestations concrètes

- **Irritabilité constante** : Tout t'agace, tu perds patience facilement
- **Disputes fréquentes** : Tu t'emportes dans les échanges, tu regrettes après
- **Frustration chronique** : Tes besoins ne sont pas satisfaits et ça te met en rage

## Conseil pratique

Respire avant de réagir — compte jusqu'à trois, demande-toi ce que tu ressens vraiment sous la colère.

## Attention

Gare à la violence — verbale ou physique — Mars mal canalisé peut détruire tes relations."""
    },
    {
        "planet1": "moon",
        "planet2": "mars",
        "aspect_type": "trine",
        "content": """# △ Trigone Lune - Mars

**En une phrase :** Tes émotions te propulsent — tu agis avec cœur et courage

## L'énergie de cet aspect

Tes émotions (Lune) et ton énergie d'action (Mars) travaillent ensemble ce mois-ci. Quand tu ressens quelque chose, tu sais quoi faire. Tes besoins te donnent de la force. Tu défends ce qui compte avec naturel, sans agressivité inutile.

## Manifestations concrètes

- **Initiative émotionnelle** : Tu oses dire ce que tu ressens, demander ce dont tu as besoin
- **Protection instinctive** : Tu défends les tiens sans hésiter
- **Énergie vitale** : Ton corps se sent bien, tu as envie de bouger, d'agir

## Conseil pratique

Lance-toi dans un projet qui te tient vraiment à cœur — tu as l'énergie et le courage maintenant.

## Attention

Attention à forcer les autres à agir à ton rythme — tout le monde n'a pas ta vitesse."""
    },
    {
        "planet1": "moon",
        "planet2": "mars",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Lune - Mars

**En une phrase :** Tu sais te défendre avec justesse — tes limites sont claires

## L'énergie de cet aspect

Tes besoins (Lune) et ton affirmation (Mars) se complètent ce mois-ci. Tu poses tes limites sans agressivité. Tu exprimes tes émotions avec force mais sans violence. Tu trouves le bon équilibre entre douceur et fermeté.

## Manifestations concrètes

- **Limites saines** : Tu dis non quand il faut, oui quand tu veux vraiment
- **Courage mesuré** : Tu oses agir sans foncer tête baissée
- **Énergie canalisée** : Tu utilises ta colère pour avancer, pas pour détruire

## Conseil pratique

Pose une limite que tu repousses depuis trop longtemps — tu as la force de tenir bon.

## Attention

Gare à minimiser tes besoins pour éviter le conflit — ta douceur ne doit pas devenir soumission."""
    }
]


async def insert_batch_07():
    """Insère les 10 aspects du Batch 7 en base de données."""

    print(f"=== Insertion Batch 7 ({len(ASPECTS)} aspects) ===\n")

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
    asyncio.run(insert_batch_07())
