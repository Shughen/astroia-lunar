#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Libra en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_LIBRA = {
    ('libra', 1): """# ♃ Jupiter en Balance
**En une phrase :** Tu incarnes une présence harmonieuse et diplomate qui crée naturellement des ponts entre les gens.

## Ton moteur
Jupiter en Balance en Maison 1 te donne une aura de grâce et d'équilibre. Tu plais naturellement, tu sais t'adapter aux autres, tu crées de l'harmonie autour de toi. Cette configuration amplifie ton besoin de beauté et de relations équilibrées.

## Ton défi
Le piège : te perdre dans le regard des autres, avoir du mal à prendre position par peur de déplaire, confondre gentillesse et soumission. L'harmonie véritable inclut aussi ta propre voix.

## Maison 1 en Balance
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un d'agréable, de raffiné, de sociable. Ton corps reflète ton souci d'esthétique — vêtements choisis, gestuelle gracieuse.

## Micro-rituel du jour (2 min)
- Créer un moment de beauté ou d'harmonie dans ton environnement immédiat
- Trois respirations en trouvant l'équilibre entre donner et recevoir
- Journal : « Comment ai-je créé de l'harmonie autour de moi aujourd'hui ? »""",

    ('libra', 2): """# ♃ Jupiter en Balance
**En une phrase :** Tu développes tes ressources par les partenariats — ta valeur se révèle dans ta capacité à créer des collaborations gagnant-gagnant.

## Ton moteur
Jupiter en Balance en Maison 2 te pousse à générer de l'abondance à travers les relations. Tu gagnes mieux en équipe qu'en solo, tu attires l'argent par ton charme et ta diplomatie. Les métiers artistiques ou liés aux partenariats te conviennent.

## Ton défi
Le piège : dépendre financièrement des autres, avoir du mal à négocier pour toi-même, dépenser trop pour plaire. La vraie abondance vient aussi de ton propre mérite.

## Maison 2 en Balance
Jupiter amplifie ton besoin de beauté dans ta gestion des ressources. Tu dépenses pour des choses esthétiques, des expériences raffinées. Tes valeurs sont liées à l'harmonie, la justice, l'équilibre.

## Micro-rituel du jour (2 min)
- Identifier une dépense récente qui a créé de l'harmonie dans ta vie
- Trois respirations en visualisant l'équilibre entre donner et recevoir
- Journal : « Comment mes ressources peuvent-elles servir plus de beauté et d'harmonie ? »""",

    ('libra', 3): """# ♃ Jupiter en Balance
**En une phrase :** Tu communiques avec diplomatie et élégance — tes mots créent des ponts, apaisent les tensions, favorisent le dialogue.

## Ton moteur
Jupiter en Balance en Maison 3 te donne un talent naturel pour la négociation et la médiation. Tu trouves les mots justes, tu présentes les choses de façon équilibrée, tu facilites la communication entre des parties opposées.

## Ton défi
Le piège : dire ce que les gens veulent entendre plutôt que ce que tu penses, avoir du mal à trancher, édulcorer les messages difficiles. La vraie communication ose aussi être directe.

## Maison 3 en Balance
Jupiter amplifie ta sociabilité dans ton entourage proche. Tes relations avec frères, sœurs et voisins sont importantes et généralement harmonieuses. Tu apprends mieux en échangeant et en débattant poliment.

## Micro-rituel du jour (2 min)
- Jouer le rôle de médiateur dans une conversation ou un échange
- Trois respirations en équilibrant écoute et expression
- Journal : « Quelle conversation récente a bénéficié de ma capacité à créer des ponts ? »""",

    ('libra', 4): """# ♃ Jupiter en Balance
**En une phrase :** Ton foyer est un écrin d'harmonie — tu crées un chez-toi beau, équilibré, propice aux rencontres et au bien-vivre.

## Ton moteur
Jupiter en Balance en Maison 4 te donne un besoin profond de beauté et d'harmonie dans ton espace de vie. Tu décores avec soin, tu reçois avec élégance, tu crées une atmosphère où les tensions s'apaisent naturellement.

## Ton défi
Le piège : éviter les conflits familiaux au point de ne jamais les résoudre, sacrifier ta paix intérieure pour maintenir l'apparence d'harmonie, être trop dépendant de l'approbation familiale. Le vrai foyer accueille aussi les désaccords.

## Maison 4 en Balance
Jupiter amplifie ton sens esthétique dans la vie privée. Tu as peut-être grandi dans une famille qui valorisait la beauté, les arts, les bonnes manières. Ton foyer peut être un lieu de rencontres et de réceptions.

## Micro-rituel du jour (2 min)
- Ajouter un élément de beauté ou réarranger quelque chose chez toi pour plus d'harmonie
- Trois respirations en visualisant ton foyer comme un havre d'équilibre
- Journal : « Qu'est-ce qui rend mon chez-moi vraiment harmonieux ? »""",

    ('libra', 5): """# ♃ Jupiter en Balance
**En une phrase :** Tu crées dans l'équilibre et la beauté — tes œuvres, tes amours et tes joies sont des duos harmonieux plutôt que des solos.

## Ton moteur
Jupiter en Balance en Maison 5 te donne une créativité qui s'épanouit dans la collaboration et l'échange. Tu préfères créer à deux, aimer en réciprocité, jouer en partenariat. Les arts visuels et la musique peuvent t'attirer particulièrement.

## Ton défi
Le piège : avoir besoin de l'approbation pour créer, te perdre dans le partenaire amoureux, éviter les plaisirs qui se vivent seul. La vraie créativité ose aussi la solitude.

## Maison 5 en Balance
Jupiter amplifie ton besoin de partenariat dans les domaines du plaisir. Tu peux attirer des partenaires raffinés et sociables. Avec les enfants, tu transmets le sens de la beauté et des relations harmonieuses.

## Micro-rituel du jour (2 min)
- Partager une activité créative ou plaisante avec quelqu'un aujourd'hui
- Trois respirations en équilibrant expression personnelle et écoute de l'autre
- Journal : « Quelle création partagée m'a récemment apporté de la joie ? »""",

    ('libra', 6): """# ♃ Jupiter en Balance
**En une phrase :** Tu travailles dans l'harmonie — ton quotidien s'organise autour de l'équilibre entre effort et repos, service et reconnaissance.

## Ton moteur
Jupiter en Balance en Maison 6 te pousse à créer un environnement de travail agréable et équilibré. Tu préfères les équipes harmonieuses aux ambiances compétitives. Cette configuration favorise les métiers artistiques, de conseil ou de médiation.

## Ton défi
Le piège : avoir du mal à travailler dans un environnement conflictuel, procrastiner par peur de mal faire, négliger les tâches ingrates. Le travail bien fait passe parfois par des efforts peu gracieux.

## Maison 6 en Balance
Jupiter amplifie ton besoin d'équilibre dans le quotidien. Tu as besoin d'un travail qui te laisse du temps pour ta vie personnelle, d'un environnement esthétique. Ta santé bénéficie d'un mode de vie harmonieux et équilibré.

## Micro-rituel du jour (2 min)
- Améliorer l'esthétique ou l'harmonie de ton espace de travail
- Trois respirations en trouvant l'équilibre entre efficacité et bien-être
- Journal : « Comment puis-je rendre mon quotidien plus harmonieux ? »""",

    ('libra', 7): """# ♃ Jupiter en Balance
**En une phrase :** Tes relations sont ta vocation — tu t'épanouis pleinement dans des partenariats équilibrés où chacun grandit grâce à l'autre.

## Ton moteur
Jupiter en Balance en Maison 7 est une position puissante pour les partenariats. Tu attires naturellement des personnes de qualité, tu sais créer des relations durables et équilibrées. Le mariage ou les associations professionnelles sont des sources d'expansion importantes.

## Ton défi
Le piège : te définir uniquement à travers tes relations, éviter la solitude à tout prix, perdre ton identité dans le couple. Les meilleures relations nourrissent deux individualités distinctes.

## Maison 7 en Balance
Jupiter amplifie naturellement ce domaine. Tu es fait pour le partenariat équilibré et raffiné. Tes contrats et mariages peuvent t'apporter chance et expansion. Tu attires des partenaires diplomates et sociables.

## Micro-rituel du jour (2 min)
- Exprimer ta gratitude à un partenaire pour l'équilibre qu'il apporte
- Trois respirations en visualisant votre relation comme une danse harmonieuse
- Journal : « Comment mes partenariats me permettent-ils de grandir ? »""",

    ('libra', 8): """# ♃ Jupiter en Balance
**En une phrase :** Tu traverses les crises avec grâce — les transformations deviennent des occasions de rééquilibrer ta vie en profondeur.

## Ton moteur
Jupiter en Balance en Maison 8 te donne une capacité à gérer les crises relationnelles avec diplomatie. Tu peux faciliter les héritages, les divorces, les partages délicats. Les ressources partagées bénéficient de ton sens de l'équité.

## Ton défi
Le piège : éviter les conflits profonds par diplomatie de surface, avoir du mal à affronter ce qui est laid ou injuste, chercher l'harmonie là où la rupture serait plus saine. La vraie transformation accepte aussi le déséquilibre.

## Maison 8 en Balance
Jupiter amplifie ton besoin d'équité dans les ressources partagées. Tu peux hériter grâce à un mariage ou un partenariat. Ta sexualité est liée à l'échange équilibré, au respect mutuel.

## Micro-rituel du jour (2 min)
- Identifier un domaine de ta vie qui a besoin d'un rééquilibrage profond
- Trois respirations en acceptant que la transformation n'est pas toujours harmonieuse
- Journal : « Quelle crise passée m'a permis de trouver un nouvel équilibre ? »""",

    ('libra', 9): """# ♃ Jupiter en Balance
**En une phrase :** Ta quête de sens passe par le dialogue — tu construis ta philosophie en écoutant tous les points de vue et en cherchant l'équilibre.

## Ton moteur
Jupiter en Balance en Maison 9 te donne une approche équilibrée des grandes questions. Tu refuses les dogmes, tu cherches à comprendre tous les côtés d'un débat. Cette configuration favorise le droit, la diplomatie internationale, l'étude comparée des cultures.

## Ton défi
Le piège : ne jamais te positionner par souci d'objectivité, relativiser au point de perdre tes convictions, confondre neutralité et sagesse. La vraie philosophie ose aussi prendre parti.

## Maison 9 en Balance
Jupiter amplifie ton besoin de dialogue dans l'exploration des grandes idées. Tu apprends mieux en débattant, en comparant les philosophies. Les voyages peuvent être liés à des partenariats ou des rencontres importantes.

## Micro-rituel du jour (2 min)
- Écouter un point de vue opposé au tien avec une vraie ouverture
- Trois respirations en cherchant l'équilibre entre tes convictions et la curiosité
- Journal : « Quelle idée différente de la mienne m'a récemment enrichi ? »""",

    ('libra', 10): """# ♃ Jupiter en Balance
**En une phrase :** Ta carrière se construit sur les relations — tu réussis en créant des partenariats stratégiques et en étant apprécié de tous.

## Ton moteur
Jupiter en Balance en Maison 10 te pousse vers des professions où les relations comptent autant que les compétences. Tu peux exceller dans la diplomatie, le droit, les arts, les ressources humaines — tout métier où la capacité à créer des liens est valorisée.

## Ton défi
Le piège : dépendre de l'approbation pour avancer, avoir du mal à prendre des décisions impopulaires, sacrifier ton ambition pour maintenir l'harmonie. Le vrai succès ose parfois déplaire.

## Maison 10 en Balance
Jupiter amplifie ta réputation de personne agréable et équitable. On te confie des rôles de représentation ou de médiation. Ta carrière peut être liée à un mariage ou un partenariat important.

## Micro-rituel du jour (2 min)
- Identifier une relation professionnelle stratégique à cultiver
- Trois respirations en équilibrant ambition personnelle et collaboration
- Journal : « Comment mes relations professionnelles soutiennent-elles ma carrière ? »""",

    ('libra', 11): """# ♃ Jupiter en Balance
**En une phrase :** Tu tisses des réseaux harmonieux — tes amitiés et tes groupes sont des espaces d'équilibre où chacun trouve sa place.

## Ton moteur
Jupiter en Balance en Maison 11 te donne un talent pour créer des communautés où règne l'harmonie. Tu facilites les liens entre les gens, tu apaises les tensions dans les groupes, tu crées des projets collectifs où chacun contribue équitablement.

## Ton défi
Le piège : éviter les conflits de groupe au détriment de la vérité, avoir des amitiés superficiellement harmonieuses, te perdre dans les relations sociales. Les vraies communautés savent aussi traverser les désaccords.

## Maison 11 en Balance
Jupiter amplifie ton influence sociale positive. Tu peux attirer des amis raffinés et sociables. Tes projets humanitaires touchent souvent aux thèmes de la justice, de l'équité, de l'harmonie sociale.

## Micro-rituel du jour (2 min)
- Jouer un rôle de facilitateur dans un groupe ou un projet collectif
- Trois respirations en visualisant ton réseau comme une toile harmonieuse
- Journal : « Comment mes amitiés créent-elles un espace d'harmonie ? »""",

    ('libra', 12): """# ♃ Jupiter en Balance
**En une phrase :** Tu trouves la paix intérieure dans l'équilibre — ta spiritualité cherche l'harmonie entre les opposés et la beauté du mystère.

## Ton moteur
Jupiter en Balance en Maison 12 crée un pont entre ton besoin d'harmonie et le monde invisible. Tu peux avoir un talent pour percevoir l'équilibre caché derrière les apparences chaotiques. Ta spiritualité cherche à réconcilier les contraires.

## Ton défi
Le piège : utiliser la spiritualité pour éviter les conflits réels, chercher une harmonie artificielle dans l'invisible, avoir du mal à accepter le chaos nécessaire à la transformation. L'équilibre profond inclut aussi le déséquilibre.

## Maison 12 en Balance
Jupiter amplifie ta quête d'harmonie dans les dimensions subtiles. Tu peux avoir des talents artistiques ou médiumniques cachés. Les retraites qui incluent la beauté, l'art ou la musique te régénèrent particulièrement.

## Micro-rituel du jour (2 min)
- Méditer sur l'équilibre entre les opposés dans ta vie intérieure
- Trois respirations en acceptant que la paix profonde inclut le mouvement
- Journal : « Quel équilibre intérieur cherche à émerger en moi ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_LIBRA.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'jupiter',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP jupiter/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='jupiter',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT jupiter/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
