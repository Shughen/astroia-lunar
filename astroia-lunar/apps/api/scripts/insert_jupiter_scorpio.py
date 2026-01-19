#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Scorpio en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_SCORPIO = {
    ('scorpio', 1): """# ♃ Jupiter en Scorpion
**En une phrase :** Tu incarnes une présence intense et magnétique qui attire les situations de transformation et les vérités cachées.

## Ton moteur
Jupiter en Scorpion en Maison 1 te donne une aura de mystère et de profondeur. On sent que tu perçois ce qui est caché, que tu n'as pas peur d'aller là où les autres n'osent pas. Cette configuration amplifie ton intensité émotionnelle et ta capacité de régénération.

## Ton défi
Le piège : intimider les autres par ton intensité, te complaire dans les zones sombres, utiliser ta perception des faiblesses d'autrui de façon manipulatrice. La vraie puissance inclut aussi la lumière.

## Maison 1 en Scorpion
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un de profond, de magnétique, parfois intimidant. Ton corps reflète ton intensité — regard pénétrant, présence qui ne passe pas inaperçue.

## Micro-rituel du jour (2 min)
- Identifier quelque chose de caché en toi ou autour de toi qui mérite d'être vu
- Trois respirations en visualisant la transformation comme une force de vie
- Journal : « Quelle vérité ai-je perçue aujourd'hui que les autres n'ont pas vue ? »""",

    ('scorpio', 2): """# ♃ Jupiter en Scorpion
**En une phrase :** Tu développes tes ressources en profondeur — ta valeur réside dans ta capacité à transformer les situations et à gérer ce que les autres évitent.

## Ton moteur
Jupiter en Scorpion en Maison 2 te pousse à générer de l'abondance à travers les domaines intenses : gestion de crise, psychologie, investigation, ressources partagées. Tu peux avoir un flair pour détecter les opportunités cachées.

## Ton défi
Le piège : te méfier de l'argent facile, avoir un rapport obsessionnel au contrôle financier, confondre pouvoir et sécurité. L'abondance véritable n'a pas besoin de tout contrôler.

## Maison 2 en Scorpion
Jupiter amplifie ton rapport intense à l'argent. Les ressources peuvent venir de façon soudaine ou par héritage. Tes valeurs sont liées à l'authenticité, à la profondeur, à la transformation des situations figées.

## Micro-rituel du jour (2 min)
- Identifier une ressource cachée (compétence, contact, opportunité) que tu n'exploites pas encore
- Trois respirations en relâchant le besoin de contrôle sur tes finances
- Journal : « Quelle ressource sous-estimée pourrait transformer ma situation ? »""",

    ('scorpio', 3): """# ♃ Jupiter en Scorpion
**En une phrase :** Tu communiques avec profondeur et intensité — tes mots percent les apparences et touchent les vérités essentielles.

## Ton moteur
Jupiter en Scorpion en Maison 3 te donne une communication pénétrante. Tu poses les questions que les autres évitent, tu devines ce qui n'est pas dit. Cette configuration favorise l'investigation, la psychologie, l'écriture qui explore les profondeurs.

## Ton défi
Le piège : utiliser tes insights pour manipuler, avoir du mal à parler de choses légères, intimider par l'intensité de tes questions. La vraie communication sait aussi être légère.

## Maison 3 en Scorpion
Jupiter amplifie ta capacité à percevoir les non-dits. Tes relations avec frères, sœurs et voisins peuvent être intenses, avec des secrets partagés ou des rivalités profondes. Tu apprends par l'immersion totale.

## Micro-rituel du jour (2 min)
- Avoir une conversation qui va au-delà des banalités, en douceur
- Trois respirations en laissant les secrets avoir leur place
- Journal : « Quelle vérité non dite ai-je perçue dans une conversation récente ? »""",

    ('scorpio', 4): """# ♃ Jupiter en Scorpion
**En une phrase :** Ton foyer est un sanctuaire de transformation — tu crées un chez-toi où les vérités peuvent émerger et les guérisons opérer.

## Ton moteur
Jupiter en Scorpion en Maison 4 te donne un rapport intense à ton espace privé. Ton foyer est un lieu de régénération profonde, peut-être un peu sombre ou mystérieux. Les secrets de famille peuvent avoir une grande importance dans ta vie.

## Ton défi
Le piège : garder trop de secrets familiaux, créer une atmosphère étouffante chez toi, utiliser l'intimité pour contrôler. Le vrai foyer a aussi besoin de légèreté et de transparence.

## Maison 4 en Scorpion
Jupiter amplifie l'intensité de ta vie privée. Tu as peut-être vécu des transformations familiales profondes. Ton foyer peut être un lieu de guérison ou de confrontation avec les ombres ancestrales.

## Micro-rituel du jour (2 min)
- Créer un espace de calme et de profondeur dans ton chez-toi
- Trois respirations en accueillant les mémoires familiales avec bienveillance
- Journal : « Quelle vérité familiale mérite d'être reconnue et honorée ? »""",

    ('scorpio', 5): """# ♃ Jupiter en Scorpion
**En une phrase :** Tu crées avec intensité et passion — tes œuvres, tes amours et tes joies plongent dans les profondeurs de l'expérience humaine.

## Ton moteur
Jupiter en Scorpion en Maison 5 te donne une créativité qui explore les tabous et les mystères. Tu n'as pas peur de l'art qui dérange, des amours qui transforment, des plaisirs qui engagent tout ton être.

## Ton défi
Le piège : rechercher l'intensité au point de fuir les joies simples, transformer les relations amoureuses en drames, confondre passion et obsession. La vraie créativité connaît aussi la légèreté.

## Maison 5 en Scorpion
Jupiter amplifie l'intensité de tes plaisirs. Tu attires des partenaires magnétiques et transformateurs. Avec les enfants ou les projets créatifs, tu transmets la capacité d'aller au fond des choses.

## Micro-rituel du jour (2 min)
- Créer quelque chose qui exprime une vérité profonde sans te soucier du confort
- Trois respirations en laissant ta passion s'exprimer pleinement
- Journal : « Quelle création me permet d'exprimer ce que je ressens vraiment ? »""",

    ('scorpio', 6): """# ♃ Jupiter en Scorpion
**En une phrase :** Tu travailles en profondeur — ton quotidien est une occasion de transformer les situations problématiques et d'aller au cœur des choses.

## Ton moteur
Jupiter en Scorpion en Maison 6 te pousse vers des métiers qui traitent ce que les autres évitent : psychologie, médecine, investigation, gestion de crise. Tu excelles quand tu peux aller au fond des problèmes.

## Ton défi
Le piège : t'épuiser dans des environnements trop intenses, avoir du mal avec les tâches superficielles, devenir obsessionnel dans ton travail. L'efficacité durable inclut aussi le détachement.

## Maison 6 en Scorpion
Jupiter amplifie ta capacité à transformer le quotidien. Tu perçois les dysfonctionnements que les autres ignorent. Ta santé peut être liée à des processus de purification ou de régénération profonde.

## Micro-rituel du jour (2 min)
- Identifier un problème récurrent au travail et aller à sa racine
- Trois respirations en relâchant l'intensité accumulée dans la journée
- Journal : « Quelle transformation ai-je apportée dans mon quotidien récemment ? »""",

    ('scorpio', 7): """# ♃ Jupiter en Scorpion
**En une phrase :** Tes relations sont des transformations mutuelles — tu cherches des partenaires avec qui plonger dans les profondeurs de l'intimité.

## Ton moteur
Jupiter en Scorpion en Maison 7 te pousse vers des partenariats intenses et transformateurs. Tu ne te satisfais pas des relations superficielles. Tu attires des personnes qui ont leur propre intensité, parfois leur part d'ombre.

## Ton défi
Le piège : transformer les relations en luttes de pouvoir, avoir du mal à lâcher prise avec un partenaire toxique, confondre intensité et amour. Les meilleures relations incluent aussi de la légèreté.

## Maison 7 en Scorpion
Jupiter amplifie l'intensité de tes partenariats. Tu peux vivre des transformations profondes à travers le mariage ou les associations. Les ressources partagées jouent un rôle important dans tes relations.

## Micro-rituel du jour (2 min)
- Partager une vérité profonde avec un partenaire, avec douceur
- Trois respirations en visualisant votre relation comme un creuset de transformation
- Journal : « Comment mon partenaire m'aide-t-il à devenir plus authentique ? »""",

    ('scorpio', 8): """# ♃ Jupiter en Scorpion
**En une phrase :** Tu navigues les crises avec maîtrise — les transformations sont ton terrain de jeu naturel, où tu révèles ta vraie puissance.

## Ton moteur
Jupiter en Scorpion en Maison 8 est une position de grande puissance pour la transformation. Tu traverses les épreuves avec une résilience remarquable, tu transformes les pertes en opportunités, tu perçois les ressources cachées que les autres ignorent.

## Ton défi
Le piège : rechercher les crises pour te sentir vivant, t'identifier à ta capacité de traverser l'ombre, négliger les aspects lumineux de l'existence. La vraie puissance sait aussi vivre en surface.

## Maison 8 en Scorpion
Jupiter amplifie au maximum ta connexion aux mystères de la vie et de la mort. Tu peux hériter de façon significative, avoir des talents psychiques, ou exceller dans la gestion des ressources partagées.

## Micro-rituel du jour (2 min)
- Honorer une transformation que tu as traversée et ce qu'elle t'a appris
- Trois respirations en visualisant ta capacité de renaissance
- Journal : « Quelle partie de moi est en train de mourir pour qu'une autre naisse ? »""",

    ('scorpio', 9): """# ♃ Jupiter en Scorpion
**En une phrase :** Ta quête de sens explore les mystères — tu cherches les vérités cachées derrière les philosophies et les sagesses officielles.

## Ton moteur
Jupiter en Scorpion en Maison 9 te donne une soif de connaissances profondes et ésotériques. Tu n'es pas satisfait par les enseignements de surface. Cette configuration favorise l'étude des traditions mystiques, la psychologie des profondeurs, les voyages initiatiques.

## Ton défi
Le piège : te perdre dans les théories du complot, rejeter les enseignements accessibles, confondre complexité et profondeur. La vraie sagesse est souvent simple.

## Maison 9 en Scorpion
Jupiter amplifie ton besoin d'aller au fond des grandes questions. Tu peux étudier l'occultisme, la psychologie, les mystères de la mort. Les voyages qui te transforment t'attirent plus que le tourisme de surface.

## Micro-rituel du jour (2 min)
- Explorer une idée ou une tradition qui touche aux mystères de l'existence
- Trois respirations en acceptant que certains mystères restent non résolus
- Journal : « Quelle vérité profonde ai-je découverte dans mes explorations récentes ? »""",

    ('scorpio', 10): """# ♃ Jupiter en Scorpion
**En une phrase :** Ta carrière explore les profondeurs — tu réussis dans les domaines où il faut aller là où les autres n'osent pas.

## Ton moteur
Jupiter en Scorpion en Maison 10 te pousse vers des professions qui traitent de l'ombre, des ressources cachées ou des transformations. Psychologie, finance, investigation, médecine — tu excelles quand il faut aller au cœur du problème.

## Ton défi
Le piège : avoir une réputation d'intensité qui effraie, confondre pouvoir professionnel et contrôle, attirer des rivalités de pouvoir. Le vrai succès sait aussi inspirer confiance.

## Maison 10 en Scorpion
Jupiter amplifie ta capacité à avoir un impact profond dans ta carrière. On te confie les missions difficiles parce qu'on sait que tu n'as pas peur. Ta réputation peut inclure une part de mystère.

## Micro-rituel du jour (2 min)
- Identifier un impact profond que tu veux avoir dans ton domaine professionnel
- Trois respirations en visualisant ta puissance professionnelle au service de la transformation
- Journal : « Comment ma carrière contribue-t-elle à transformer quelque chose de significatif ? »""",

    ('scorpio', 11): """# ♃ Jupiter en Scorpion
**En une phrase :** Tu crées des alliances profondes — tes amitiés et tes groupes sont des espaces de transformation mutuelle et de vérités partagées.

## Ton moteur
Jupiter en Scorpion en Maison 11 te donne un talent pour créer des liens intenses avec des groupes transformateurs. Tu n'aimes pas les amitiés superficielles. Tes projets collectifs touchent aux thèmes de la transformation sociale ou de la guérison.

## Ton défi
Le piège : créer des cercles fermés avec des secrets partagés, utiliser ton influence pour manipuler les groupes, avoir du mal avec les amitiés légères. Les meilleures communautés accueillent aussi la diversité.

## Maison 11 en Scorpion
Jupiter amplifie l'intensité de tes liens d'amitié. Tu peux attirer des amis thérapeutes, chercheurs ou impliqués dans des transformations sociales. Tes projets humanitaires touchent aux tabous ou aux injustices profondes.

## Micro-rituel du jour (2 min)
- Partager une vérité profonde avec un ami de confiance
- Trois respirations en visualisant ton cercle comme un creuset de transformation
- Journal : « Quelle amitié m'a récemment permis d'explorer des profondeurs ? »""",

    ('scorpio', 12): """# ♃ Jupiter en Scorpion
**En une phrase :** Tu explores l'invisible avec courage — ta spiritualité plonge dans les mystères de la mort, de la renaissance et de l'inconscient profond.

## Ton moteur
Jupiter en Scorpion en Maison 12 crée un pont puissant vers les dimensions cachées. Tu as peut-être des capacités psychiques, des rêves prophétiques, un accès aux mémoires ancestrales ou karmiques. Ta spiritualité n'a pas peur de l'ombre.

## Ton défi
Le piège : te perdre dans les dimensions sombres, utiliser tes perceptions psychiques de façon malsaine, t'identifier à ta souffrance karmique. La vraie spiritualité inclut aussi la lumière et la guérison.

## Maison 12 en Scorpion
Jupiter amplifie ta connexion aux mystères les plus profonds. Tu peux avoir un talent de guérisseur des traumatismes ou de guide dans les passages difficiles. Les retraites qui incluent un travail sur l'ombre te transforment profondément.

## Micro-rituel du jour (2 min)
- Méditer sur ce qui veut mourir et renaître en toi en ce moment
- Trois respirations en honorant les profondeurs de ton inconscient
- Journal : « Quel message de l'ombre m'a récemment éclairé sur mon chemin ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_SCORPIO.items():
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
