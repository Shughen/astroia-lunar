#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Gemini en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_GEMINI = {
    ('gemini', 1): """# ♃ Jupiter en Gémeaux
**En une phrase :** Tu incarnes une curiosité contagieuse — ta présence stimule l'esprit des autres et ouvre mille portes de conversation.

## Ton moteur
Jupiter en Gémeaux en Maison 1 te donne une aura de vivacité intellectuelle. Tu parles avec les mains, tu changes de sujet rapidement, tu captes l'attention par ta variété. Cette configuration amplifie ton besoin de mouvement mental et physique : rester immobile t'ennuie.

## Ton défi
Le piège : te disperser dans trop de directions, parler sans écouter, surcharger les autres d'informations. La vraie intelligence sait aussi se concentrer et faire silence.

## Maison 1 en Gémeaux
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un de vif, adaptable, plein de ressources. Ton corps exprime ton mental — gestuelle rapide, regard mobile, énergie nerveuse.

## Micro-rituel du jour (2 min)
- Apprendre un mot nouveau ou un fait surprenant et le partager avec quelqu'un
- Trois respirations en calmant le flux des pensées, juste observer
- Journal : « Quelle nouvelle idée m'a captivé aujourd'hui ? »""",

    ('gemini', 2): """# ♃ Jupiter en Gémeaux
**En une phrase :** Tu multiplies les sources de revenus avec agilité — ta valeur réside dans ta capacité à connecter les idées et les gens.

## Ton moteur
Jupiter en Gémeaux en Maison 2 te donne un talent pour monétiser l'information et la communication. Tu peux avoir plusieurs activités en parallèle, écrire, conseiller, former. L'argent circule vite dans ta vie — il arrive et repart avec la même fluidité.

## Ton défi
Le piège : éparpiller tes ressources dans trop de projets, ne pas approfondir suffisamment pour créer une vraie valeur, confondre quantité et qualité. La prospérité durable demande aussi de la concentration.

## Maison 2 en Gémeaux
Jupiter amplifie ton besoin de diversité dans tes sources de revenus. Tu t'ennuies vite avec une seule activité. Tes valeurs sont liées à l'apprentissage, l'échange, la transmission du savoir.

## Micro-rituel du jour (2 min)
- Identifier une compétence que tu pourrais transformer en source de revenus secondaire
- Trois respirations en visualisant l'abondance comme un flux d'idées
- Journal : « Quelle information précieuse ai-je à partager ? »""",

    ('gemini', 3): """# ♃ Jupiter en Gémeaux
**En une phrase :** Ta communication est ton super-pouvoir — tu connectes les idées, les personnes et les mondes avec une facilité naturelle.

## Ton moteur
Jupiter en Gémeaux en Maison 3 amplifie ton génie de la communication. Tu apprends vite, tu parles plusieurs langages (au sens propre comme figuré), tu fais circuler l'information comme personne. Cette configuration est idéale pour l'écriture, le journalisme, l'enseignement, le commerce.

## Ton défi
Le piège : surcharger d'informations sans vérifier leur véracité, papillonner sans approfondir, confondre bavardage et vraie communication. La parole gagne en puissance quand elle est choisie.

## Maison 3 en Gémeaux
Jupiter amplifie naturellement ce domaine. Ton entourage proche est stimulant intellectuellement. Tu as peut-être des frères et sœurs nombreux ou des relations de voisinage très actives. Les déplacements courts nourrissent ta curiosité.

## Micro-rituel du jour (2 min)
- Envoyer un message à quelqu'un pour partager une découverte ou poser une question
- Trois respirations en visualisant des ponts qui se créent entre les idées
- Journal : « Quelle conversation récente a changé ma façon de voir quelque chose ? »""",

    ('gemini', 4): """# ♃ Jupiter en Gémeaux
**En une phrase :** Ton foyer est un carrefour d'idées — ta maison bruisse de conversations, de livres et de projets en gestation.

## Ton moteur
Jupiter en Gémeaux en Maison 4 transforme ton chez-toi en bibliothèque vivante. Tu as besoin d'un environnement qui stimule l'esprit : des livres partout, un bon wifi, des espaces pour écrire ou discuter. Ta famille d'origine t'a transmis la curiosité ou le goût des mots.

## Ton défi
Le piège : avoir du mal à te poser vraiment chez toi, transformer ton foyer en bureau permanent, manquer de calme pour te ressourcer. Le chez-soi a aussi besoin de silence.

## Maison 4 en Gémeaux
Jupiter amplifie le mouvement dans ta vie privée. Tu as peut-être déménagé souvent ou grandi dans un foyer où l'on parlait beaucoup. Tes racines sont dans les mots, les histoires, les échanges familiaux.

## Micro-rituel du jour (2 min)
- Ranger ou réorganiser un espace de lecture ou de travail à la maison
- Trois respirations en laissant les pensées se déposer comme des livres sur une étagère
- Journal : « Quelle idée ou histoire de ma famille continue de m'influencer ? »""",

    ('gemini', 5): """# ♃ Jupiter en Gémeaux
**En une phrase :** Tu joues avec les mots et les idées — ta créativité est intellectuelle, ludique, pleine de surprises et de rebondissements.

## Ton moteur
Jupiter en Gémeaux en Maison 5 te donne un talent pour l'expression créative verbale. Écriture, théâtre, jeux d'esprit, humour — tu brilles quand tu peux jouer avec le langage. En amour, tu cherches des partenaires qui stimulent ta curiosité et te font rire.

## Ton défi
Le piège : multiplier les flirts sans approfondir, préférer le jeu mental à l'engagement émotionnel, intellectualiser tes sentiments au lieu de les vivre. L'amour demande parfois de poser les mots.

## Maison 5 en Gémeaux
Jupiter amplifie ton besoin de stimulation dans les plaisirs. Tu t'ennuies vite si les activités se répètent. Avec les enfants, tu es un excellent conteur et un compagnon de jeu curieux de tout.

## Micro-rituel du jour (2 min)
- T'amuser avec les mots : jeu de mots, écriture spontanée, conversation improbable
- Trois respirations en laissant ton esprit jouer librement
- Journal : « Qu'est-ce qui m'a fait rire ou m'a surpris récemment ? »""",

    ('gemini', 6): """# ♃ Jupiter en Gémeaux
**En une phrase :** Tu optimises ton quotidien par l'information — ton efficacité vient de ta capacité à apprendre et adapter constamment tes méthodes.

## Ton moteur
Jupiter en Gémeaux en Maison 6 te donne un talent pour améliorer les processus et les routines. Tu aimes tester de nouvelles méthodes, de nouveaux outils, de nouvelles façons de travailler. Cette configuration favorise les métiers de communication, d'écriture, ou de formation.

## Ton défi
Le piège : changer de méthode avant d'avoir maîtrisé la précédente, surcharger ton quotidien d'informations, négliger ton corps en te concentrant sur le mental. La santé demande aussi de la régularité.

## Maison 6 en Gémeaux
Jupiter amplifie ta nervosité naturelle. Tu as besoin de variété dans ton travail quotidien. Ta santé peut être sensible au stress mental — les mains, les poumons, le système nerveux demandent attention.

## Micro-rituel du jour (2 min)
- Apprendre une technique ou un outil qui améliore ton efficacité quotidienne
- Trois respirations en relâchant les tensions dans les épaules et les mains
- Journal : « Quelle nouvelle méthode a récemment simplifié ma vie ? »""",

    ('gemini', 7): """# ♃ Jupiter en Gémeaux
**En une phrase :** Tes relations sont des conversations sans fin — tu cherches des partenaires qui stimulent ton esprit et élargissent ton monde.

## Ton moteur
Jupiter en Gémeaux en Maison 7 te pousse vers des partenariats basés sur l'échange intellectuel. Tu as besoin de pouvoir parler de tout avec ton partenaire, de débattre, de découvrir ensemble. Tu peux attirer des personnes plus jeunes ou celles qui travaillent dans la communication.

## Ton défi
Le piège : fuir l'intimité émotionnelle par le bavardage, avoir du mal à choisir un seul partenaire, intellectualiser les conflits au lieu de les traverser. Les relations demandent aussi du silence partagé.

## Maison 7 en Gémeaux
Jupiter amplifie ton besoin de variété relationnelle. Tu peux avoir plusieurs partenariats importants en parallèle (amoureux et professionnels). Tes contrats et associations bénéficient de ta capacité à négocier et communiquer.

## Micro-rituel du jour (2 min)
- Proposer une conversation sur un sujet nouveau à un partenaire
- Trois respirations en visualisant les mots comme des ponts vers l'autre
- Journal : « Quelle idée nouvelle un partenaire m'a-t-il apportée récemment ? »""",

    ('gemini', 8): """# ♃ Jupiter en Gémeaux
**En une phrase :** Tu explores les profondeurs avec ta curiosité — les tabous deviennent des sujets d'étude, les crises des occasions d'apprendre.

## Ton moteur
Jupiter en Gémeaux en Maison 8 te donne une capacité à parler de ce que les autres taisent. Mort, sexe, argent, psychologie des profondeurs — tu as besoin de comprendre et de mettre des mots sur l'indicible. Cette configuration favorise les métiers de recherche, de psychologie, ou de gestion financière.

## Ton défi
Le piège : intellectualiser ce qui demande d'être vécu, accumuler des informations sur les sujets profonds sans les intégrer, parler des transformations sans les traverser. Les profondeurs demandent aussi du silence.

## Maison 8 en Gémeaux
Jupiter amplifie ta curiosité pour les mystères. Tu peux avoir un talent pour la communication autour de sujets sensibles. Les ressources partagées peuvent venir de plusieurs sources ou fluctuer rapidement.

## Micro-rituel du jour (2 min)
- Lire ou écouter quelque chose sur un sujet que tu évites habituellement
- Trois respirations en laissant les questions sans réponse exister
- Journal : « Quelle transformation en cours mériterait d'être mise en mots ? »""",

    ('gemini', 9): """# ♃ Jupiter en Gémeaux
**En une phrase :** Ta quête de sens passe par les mots et les échanges — tu construis ta philosophie en écoutant toutes les voix du monde.

## Ton moteur
Jupiter en Gémeaux en Maison 9 te donne une soif insatiable de connaissances diverses. Tu ne cherches pas une seule vérité mais un dialogue entre plusieurs. Cette configuration favorise les langues étrangères, les voyages de découverte, l'enseignement, l'édition.

## Ton défi
Le piège : accumuler des savoirs superficiels sans vision d'ensemble, changer de conviction au gré des lectures, confondre érudition et sagesse. La vraie philosophie demande aussi de la cohérence.

## Maison 9 en Gémeaux
Jupiter amplifie ton rapport à l'étranger et aux grandes idées. Tu apprends en comparant les cultures, les philosophies, les points de vue. Tu pourrais écrire, enseigner ou voyager pour transmettre ce que tu découvres.

## Micro-rituel du jour (2 min)
- Écouter ou lire un point de vue opposé au tien sur un sujet important
- Trois respirations en visualisant des horizons qui s'ouvrent à travers les mots
- Journal : « Quelle idée étrangère a récemment enrichi ma pensée ? »""",

    ('gemini', 10): """# ♃ Jupiter en Gémeaux
**En une phrase :** Ta carrière s'appuie sur ta capacité à communiquer — tu peux exceller dans tous les métiers où les mots et les idées circulent.

## Ton moteur
Jupiter en Gémeaux en Maison 10 te pousse vers des professions liées à l'information et l'échange. Journalisme, marketing, enseignement, commerce, conseil — tu brilles quand tu peux utiliser ton intelligence verbale. Tu peux avoir plusieurs carrières successives ou parallèles.

## Ton défi
Le piège : te disperser professionnellement sans construire d'expertise durable, promettre plus que tu ne peux tenir, confondre visibilité et crédibilité. La réputation se construit aussi sur la profondeur.

## Maison 10 en Gémeaux
Jupiter amplifie ta réputation de communicant. On te remarque pour ta vivacité, ton adaptabilité, ta capacité à simplifier le complexe. Ton parcours professionnel peut sembler chaotique vu de l'extérieur mais suit une logique de curiosité.

## Micro-rituel du jour (2 min)
- Identifier une compétence de communication à développer pour ta carrière
- Trois respirations en visualisant ta parole qui porte loin et haut
- Journal : « Comment mes talents de communication peuvent-ils mieux servir mes ambitions ? »""",

    ('gemini', 11): """# ♃ Jupiter en Gémeaux
**En une phrase :** Tu tisses des réseaux par la conversation — tes amitiés sont des échanges d'idées qui nourrissent tes projets et tes rêves.

## Ton moteur
Jupiter en Gémeaux en Maison 11 te donne un talent pour connecter les gens et faire circuler l'information dans les groupes. Tu es souvent celui qui présente les uns aux autres, qui partage les bonnes nouvelles, qui fait le lien entre des mondes différents.

## Ton défi
Le piège : avoir des contacts nombreux mais superficiels, préférer les réseaux aux vraies amitiés, t'éparpiller dans trop de projets collectifs. Les meilleures causes demandent aussi de la fidélité.

## Maison 11 en Gémeaux
Jupiter amplifie ton influence dans les réseaux. Tu peux attirer des amis de tous horizons, souvent plus jeunes ou issus du monde de la communication. Tes projets humanitaires passent par l'éducation, l'information, la mise en lien.

## Micro-rituel du jour (2 min)
- Présenter deux personnes de ton réseau qui pourraient s'enrichir mutuellement
- Trois respirations en visualisant les fils qui relient les membres de ta communauté
- Journal : « Quelle connexion récente a ouvert de nouvelles possibilités ? »""",

    ('gemini', 12): """# ♃ Jupiter en Gémeaux
**En une phrase :** Tu explores l'inconscient par les mots — écrire, rêver, méditer te permet de donner forme à l'invisible.

## Ton moteur
Jupiter en Gémeaux en Maison 12 crée un pont entre ta rationalité et le monde subtil. Tu as peut-être un talent pour l'écriture automatique, la poésie, ou la transcription de tes rêves. Les messages de l'inconscient te viennent souvent sous forme verbale.

## Ton défi
Le piège : intellectualiser les expériences spirituelles au lieu de les vivre, rester dans le mental quand il faut lâcher prise, confondre bavardage intérieur et intuition. Le silence est parfois le meilleur langage.

## Maison 12 en Gémeaux
Jupiter amplifie ton activité mentale inconsciente. Tu peux avoir des pensées qui semblent venir d'ailleurs, des intuitions sous forme de phrases. Les retraites qui incluent l'écriture ou la parole guidée te conviennent particulièrement.

## Micro-rituel du jour (2 min)
- Écrire sans réfléchir pendant 2 minutes et observer ce qui émerge
- Trois respirations en laissant les pensées devenir des nuages qui passent
- Journal : « Quel message de l'inconscient ai-je reçu récemment sous forme de mots ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_GEMINI.items():
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
