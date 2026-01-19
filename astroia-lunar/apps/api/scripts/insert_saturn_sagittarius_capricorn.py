#!/usr/bin/env python3
"""Script d'insertion des interprétations Saturn/Sagittarius et Capricorn (manquantes) en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

SATURN_INTERPRETATIONS = {
    # SAGITTARIUS - 12 maisons
    ('sagittarius', 1): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu apprends à structurer ta quête de sens — la liberté véritable vient d'une vision ancrée dans la réalité.

## Ton moteur
Saturne en Sagittaire en Maison 1 te demande de discipliner ton optimisme et ton besoin d'expansion. Tu dois apprendre à incarner ta philosophie de vie, pas seulement la prêcher. Cette configuration forge une sagesse qui vient de l'expérience.

## Ton défi
Le piège : osciller entre excès d'enthousiasme et pessimisme, avoir du mal à t'engager dans une direction, fuir les limitations par le voyage ou l'abstraction. La vraie liberté se construit sur des fondations solides.

## Maison 1 en Sagittaire
Saturne structure ton apparence de chercheur de vérité. Tu projettes une image de sérieux philosophique, parfois de scepticisme. Ton corps peut porter les marques de tes explorations — cicatrices de voyage, posture de marcheur.

## Micro-rituel du jour (2 min)
- Identifier une croyance que tu incarnes concrètement dans ta vie quotidienne
- Trois respirations en ancrant ta vision dans le présent
- Journal : « Comment ma philosophie s'exprime-t-elle dans mes actes aujourd'hui ? »""",

    ('sagittarius', 2): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu construis ta prospérité sur des valeurs de sens — l'abondance vient quand tu alignes ressources et vision.

## Ton moteur
Saturne en Sagittaire en Maison 2 te demande de structurer ta relation à l'argent autour d'une vision plus large. Tu ne peux pas gagner ta vie en faisant n'importe quoi — tes revenus doivent avoir du sens. Les métiers liés à l'enseignement, l'édition, les voyages peuvent être lucratifs mais demandent du temps.

## Ton défi
Le piège : négliger le concret financier pour les grandes idées, avoir des revenus irréguliers par manque de structure, confondre abondance spirituelle et matérielle. La vraie prospérité intègre les deux dimensions.

## Maison 2 en Sagittaire
Saturne structure tes finances autour du sens. Tes revenus peuvent venir de l'étranger, de l'enseignement ou de la diffusion d'idées. Tes valeurs sont liées à la liberté, mais tu apprends à les ancrer dans la réalité.

## Micro-rituel du jour (2 min)
- Identifier comment tes revenus servent une vision plus large
- Trois respirations en connectant abondance et sens
- Journal : « Quelle valeur importante guide mes choix financiers ? »""",

    ('sagittarius', 3): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu apprends à communiquer avec profondeur — tes mots gagnent en poids quand ils sont ancrés dans l'expérience.

## Ton moteur
Saturne en Sagittaire en Maison 3 te demande de discipliner ta communication enthousiaste. Tu dois apprendre à être précis, à argumenter solidement, à ne pas exagérer. Cette configuration forge une parole qui porte parce qu'elle est réfléchie.

## Ton défi
Le piège : promettre plus que tu ne peux tenir, communiquer de façon trop abstraite, avoir du mal avec les détails pratiques. La vraie éloquence sait aussi être concrète et mesurée.

## Maison 3 en Sagittaire
Saturne structure tes échanges autour de la recherche de vérité. Tes relations avec frères, sœurs et voisins peuvent impliquer des questions de croyances ou de distance. Tu apprends mieux par l'expérience que par la théorie.

## Micro-rituel du jour (2 min)
- Partager une idée de façon précise et argumentée avec quelqu'un
- Trois respirations en pesant tes mots avant de parler
- Journal : « Comment ma communication peut-elle être plus ancrée ? »""",

    ('sagittarius', 4): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu construis un foyer qui incarne tes valeurs — ta maison devient un temple de ta philosophie de vie.

## Ton moteur
Saturne en Sagittaire en Maison 4 te demande d'ancrer ta quête de sens dans tes racines. Ton foyer peut refléter tes voyages, tes études, tes croyances. Tu dois trouver l'équilibre entre l'appel du lointain et le besoin de racines.

## Ton défi
Le piège : fuir les responsabilités familiales pour l'aventure, avoir du mal à créer un chez-toi stable, projeter tes idéaux sur ta famille. Le vrai foyer accepte aussi les imperfections.

## Maison 4 en Sagittaire
Saturne structure ta vie familiale autour du sens. Tu as peut-être grandi avec des parents philosophes ou voyageurs, ou dans une famille où les croyances étaient importantes. Ton foyer peut inclure des éléments d'autres cultures.

## Micro-rituel du jour (2 min)
- Identifier comment ton foyer reflète tes valeurs profondes
- Trois respirations en te sentant chez toi dans tes croyances
- Journal : « Comment ma maison incarne-t-elle ma philosophie de vie ? »""",

    ('sagittarius', 5): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu apprends à créer avec discipline — ta joie vient quand tu incarnes ta vision dans des œuvres concrètes.

## Ton moteur
Saturne en Sagittaire en Maison 5 te demande de structurer ta créativité enthousiaste. Tu dois apprendre à finir ce que tu commences, à transformer l'inspiration en œuvre accomplie. En amour, tu cherches des partenaires qui partagent ta vision du monde.

## Ton défi
Le piège : commencer mille projets créatifs sans en finir aucun, idéaliser les relations amoureuses, avoir du mal avec la légèreté du jeu. La vraie joie créative s'ancre aussi dans la discipline.

## Maison 5 en Sagittaire
Saturne structure tes plaisirs autour du sens. Tu peux être attiré par des partenaires étrangers ou philosophiques. Ta créativité s'épanouit dans les grands projets qui ont une vision.

## Micro-rituel du jour (2 min)
- T'engager à finir un projet créatif commencé
- Trois respirations en connectant plaisir et accomplissement
- Journal : « Quelle création ai-je besoin de mener à terme ? »""",

    ('sagittarius', 6): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu travailles avec une vision — ton quotidien prend sens quand il sert quelque chose de plus grand.

## Ton moteur
Saturne en Sagittaire en Maison 6 te demande de structurer ton travail autour d'une vision plus large. Tu ne peux pas faire un travail qui n'a pas de sens pour toi. Cette configuration favorise les métiers liés à l'enseignement, l'édition, les voyages, mais demande de la discipline.

## Ton défi
Le piège : négliger les détails quotidiens pour les grandes idées, avoir du mal avec la routine, projeter du sens là où il n'y en a pas. Le vrai travail significatif inclut aussi les tâches ordinaires.

## Maison 6 en Sagittaire
Saturne structure ton quotidien autour de la quête de sens. Tu travailles mieux quand tu comprends le pourquoi. Ta santé bénéficie d'une vision positive mais réaliste.

## Micro-rituel du jour (2 min)
- Identifier le sens profond d'une tâche quotidienne
- Trois respirations en connectant routine et vision
- Journal : « Comment mon travail quotidien sert-il quelque chose de plus grand ? »""",

    ('sagittarius', 7): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu construis des partenariats sur des visions partagées — les relations durables sont celles qui grandissent ensemble.

## Ton moteur
Saturne en Sagittaire en Maison 7 te demande de bâtir des relations sur des fondations philosophiques communes. Tu as besoin de partenaires qui partagent ta vision du monde, tes valeurs, ton sens de l'aventure. Les relations mûrissent avec le temps.

## Ton défi
Le piège : imposer tes croyances à tes partenaires, fuir l'engagement par peur de perdre ta liberté, idéaliser les relations au point d'être déçu. Les meilleures relations acceptent aussi les différences de vision.

## Maison 7 en Sagittaire
Saturne structure tes partenariats autour du sens commun. Tu peux attirer des partenaires étrangers, enseignants ou philosophes. Tes contrats bénéficient d'une vision à long terme.

## Micro-rituel du jour (2 min)
- Partager une vision d'avenir avec un partenaire
- Trois respirations en honorant la liberté dans la relation
- Journal : « Quelle vision partageons-nous avec mon partenaire ? »""",

    ('sagittarius', 8): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu traverses les crises avec philosophie — les transformations deviennent des initiations qui élargissent ta vision.

## Ton moteur
Saturne en Sagittaire en Maison 8 te demande de trouver du sens dans les épreuves. Les crises deviennent des occasions d'approfondir ta compréhension de la vie. Tu apprends à lâcher prise sur tes certitudes pour accéder à une sagesse plus profonde.

## Ton défi
Le piège : philosopher sur les crises au lieu de les traverser émotionnellement, fuir l'intensité dans l'abstraction, avoir du mal avec les aspects sombres de la transformation. La vraie sagesse intègre aussi l'ombre.

## Maison 8 en Sagittaire
Saturne structure ta relation aux transformations. Les ressources partagées peuvent venir de l'étranger ou de l'enseignement. Ta sexualité est liée à la quête de sens et de transcendance.

## Micro-rituel du jour (2 min)
- Identifier ce qu'une crise récente t'a enseigné
- Trois respirations en accueillant la transformation
- Journal : « Quelle sagesse ai-je gagnée d'une épreuve passée ? »""",

    ('sagittarius', 9): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu construis ta sagesse pierre par pierre — la vraie philosophie vient de l'expérience vécue, pas des livres seuls.

## Ton moteur
Saturne en Sagittaire en Maison 9 te demande de structurer ta quête de sens avec rigueur. Tu ne te satisfais pas des croyances superficielles — tu veux une philosophie qui tient face à la réalité. Cette configuration forge un enseignant ou un guide qui parle d'expérience.

## Ton défi
Le piège : devenir dogmatique ou sceptique excessif, avoir peur de t'engager dans une voie, reporter indéfiniment les grands voyages ou les études. La vraie sagesse s'acquiert en marchant.

## Maison 9 en Sagittaire
Saturne structure au maximum ta quête de sens. Tu peux devenir un expert respecté dans ton domaine, un enseignant qui a gagné sa sagesse. Les voyages lointains peuvent être tardifs mais transformateurs.

## Micro-rituel du jour (2 min)
- Approfondir une croyance par la réflexion ou la lecture
- Trois respirations en honorant le chemin parcouru
- Journal : « Quelle sagesse ai-je gagnée par l'expérience directe ? »""",

    ('sagittarius', 10): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu construis une carrière qui a du sens — ta réussite vient quand tu incarnes publiquement ta vision du monde.

## Ton moteur
Saturne en Sagittaire en Maison 10 te pousse vers une carrière alignée avec tes valeurs. Tu ne peux pas réussir dans quelque chose qui n'a pas de sens pour toi. Cette configuration favorise les carrières dans l'enseignement, l'édition, le droit, les voyages — mais demande du temps pour s'établir.

## Ton défi
Le piège : fuir les responsabilités professionnelles pour la liberté, avoir une carrière chaotique par manque de focus, prêcher sans incarner. La vraie autorité vient de l'exemple.

## Maison 10 en Sagittaire
Saturne structure ta réputation autour de ta vision. On te reconnaît pour ta sagesse, ton éthique, ta capacité à voir loin. Ta carrière peut impliquer l'international ou la transmission de connaissances.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière sert ta vision du monde
- Trois respirations en alignant ambition et sens
- Journal : « Quelle contribution significative ai-je envie de faire dans ma carrière ? »""",

    ('sagittarius', 11): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu construis des réseaux autour d'une vision partagée — tes amitiés durables sont celles qui grandissent ensemble vers un idéal.

## Ton moteur
Saturne en Sagittaire en Maison 11 te demande de choisir tes amis et tes groupes selon des critères de sens. Tu as besoin de communautés qui partagent ta vision, tes valeurs. Les projets collectifs doivent servir quelque chose de plus grand.

## Ton défi
Le piège : imposer ta vision aux groupes, avoir du mal à tolérer des perspectives différentes, fuir l'engagement collectif par individualisme. Les meilleures communautés accueillent la diversité des visions.

## Maison 11 en Sagittaire
Saturne structure tes réseaux autour d'idéaux communs. Tes amis peuvent venir de l'étranger ou de milieux philosophiques, académiques. Tes projets humanitaires sont liés à l'éducation, la culture, l'ouverture.

## Micro-rituel du jour (2 min)
- Partager une vision inspirante avec un ami ou un groupe
- Trois respirations en honorant la diversité des perspectives
- Journal : « Quel idéal commun me relie à mes amis les plus proches ? »""",

    ('sagittarius', 12): """# ♄ Saturne en Sagittaire
**En une phrase :** Tu explores l'invisible avec rigueur — ta spiritualité se construit sur une quête authentique de vérité.

## Ton moteur
Saturne en Sagittaire en Maison 12 te demande de structurer ta vie spirituelle avec discernement. Tu ne te satisfais pas des croyances faciles — tu veux une spiritualité qui tient face au doute. Cette configuration peut créer des périodes de crise de foi qui approfondissent ta connexion au sacré.

## Ton défi
Le piège : fuir dans les croyances pour éviter la réalité, avoir des périodes de doute paralysant, confondre recherche spirituelle et évitement. La vraie spiritualité s'incarne aussi dans le quotidien.

## Maison 12 en Sagittaire
Saturne structure ta connexion à l'invisible. Tu peux avoir des guides spirituels ou des enseignants importants. Les retraites dans des lieux sacrés lointains peuvent être transformatrices mais demandent une préparation.

## Micro-rituel du jour (2 min)
- Méditer sur une question spirituelle sans chercher de réponse immédiate
- Trois respirations en accueillant le mystère
- Journal : « Quelle vérité spirituelle ai-je découverte par l'expérience ? »""",

    # CAPRICORN - seulement les maisons manquantes (M2, M3, M5, M6, M8, M9, M11, M12)
    ('capricorn', 2): """# ♄ Saturne en Capricorne
**En une phrase :** Tu construis ta prospérité avec patience et discipline — l'abondance vient de l'effort soutenu et de la gestion rigoureuse.

## Ton moteur
Saturne en Capricorne en Maison 2 est une position puissante pour bâtir une fortune durable. Tu sais que l'argent se gagne par le travail et se conserve par la prudence. Cette configuration favorise l'accumulation lente mais sûre de ressources.

## Ton défi
Le piège : être trop avare ou anxieux concernant l'argent, confondre valeur personnelle et compte en banque, négliger les plaisirs de la vie par excès d'économie. La vraie prospérité sait aussi profiter.

## Maison 2 en Capricorne
Saturne structure tes finances avec une rigueur maximale. Tu excelles dans la gestion, l'investissement à long terme, la construction de patrimoine. Tes valeurs sont liées au travail, à la responsabilité, à la durabilité.

## Micro-rituel du jour (2 min)
- Identifier une ressource que tu as construite par ton effort
- Trois respirations en appréciant ta capacité à bâtir
- Journal : « Quel investissement à long terme mérite mon attention ? »""",

    ('capricorn', 3): """# ♄ Saturne en Capricorne
**En une phrase :** Tu communiques avec autorité et précision — tes mots portent parce qu'ils sont pesés et structurés.

## Ton moteur
Saturne en Capricorne en Maison 3 te donne une communication rigoureuse et professionnelle. Tu ne parles pas pour ne rien dire — chaque mot compte. Cette configuration favorise les métiers de l'écriture technique, du droit, de l'administration.

## Ton défi
Le piège : être trop rigide ou froid dans ta communication, avoir du mal avec la légèreté, couper le contact par excès de sérieux. La vraie autorité sait aussi être accessible.

## Maison 3 en Capricorne
Saturne structure tes échanges avec méthode. Tes relations avec frères, sœurs et voisins peuvent être formelles ou distantes mais fiables. Tu apprends mieux par les méthodes structurées.

## Micro-rituel du jour (2 min)
- Communiquer quelque chose d'important de façon claire et structurée
- Trois respirations en pesant tes mots
- Journal : « Comment ma communication peut-elle être plus efficace ? »""",

    ('capricorn', 5): """# ♄ Saturne en Capricorne
**En une phrase :** Tu crées avec discipline et ambition — tes œuvres sont des constructions durables qui résistent au temps.

## Ton moteur
Saturne en Capricorne en Maison 5 te demande de prendre ta créativité au sérieux. Tu ne crées pas pour t'amuser mais pour accomplir quelque chose de durable. En amour, tu cherches des relations stables avec des partenaires responsables.

## Ton défi
Le piège : transformer le plaisir en devoir, avoir du mal à te détendre et jouer, choisir des partenaires trop par calcul. La vraie joie créative inclut aussi la spontanéité.

## Maison 5 en Capricorne
Saturne structure tes plaisirs avec sérieux. Tu peux être attiré par des partenaires plus âgés ou plus matures. Ta créativité s'épanouit dans les projets ambitieux et durables.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir simple sans chercher à être productif
- Trois respirations en laissant la joie être légère
- Journal : « Comment puis-je intégrer plus de jeu dans ma vie ? »""",

    ('capricorn', 6): """# ♄ Saturne en Capricorne
**En une phrase :** Tu travailles avec méthode et endurance — ton efficacité vient de ta discipline et de ta capacité à tenir sur la durée.

## Ton moteur
Saturne en Capricorne en Maison 6 est une position puissante pour le travail structuré. Tu excelles dans les environnements organisés, les processus clairs, les responsabilités définies. Cette configuration favorise les carrières dans l'administration, la gestion, les métiers techniques.

## Ton défi
Le piège : devenir workaholic, négliger ta santé pour le travail, être trop rigide dans tes méthodes. La vraie efficacité inclut aussi le repos et la flexibilité.

## Maison 6 en Capricorne
Saturne structure ton quotidien avec une rigueur maximale. Tu as besoin de routines claires et de responsabilités définies. Ta santé bénéficie d'une approche disciplinée mais peut souffrir du stress professionnel.

## Micro-rituel du jour (2 min)
- Identifier une routine qui soutient ta santé et la renforcer
- Trois respirations en honorant le repos comme partie du travail
- Journal : « Comment puis-je être efficace tout en prenant soin de moi ? »""",

    ('capricorn', 8): """# ♄ Saturne en Capricorne
**En une phrase :** Tu traverses les crises avec résilience — les transformations deviennent des occasions de construire quelque chose de plus solide.

## Ton moteur
Saturne en Capricorne en Maison 8 te donne une capacité à traverser les épreuves avec une force remarquable. Tu ne fuis pas les difficultés — tu les utilises pour te renforcer. Les ressources partagées sont gérées avec rigueur.

## Ton défi
Le piège : te durcir excessivement face aux crises, avoir du mal à demander de l'aide, contrôler plutôt que transformer. La vraie résilience inclut aussi la vulnérabilité.

## Maison 8 en Capricorne
Saturne structure ta relation aux transformations. Tu excelles dans la gestion des ressources partagées, les héritages, les investissements. Ta sexualité peut être liée au pouvoir et au contrôle.

## Micro-rituel du jour (2 min)
- Identifier une transformation en cours et la structurer plutôt que la subir
- Trois respirations en accueillant le changement comme allié
- Journal : « Quelle crise passée m'a rendu plus fort ? »""",

    ('capricorn', 9): """# ♄ Saturne en Capricorne
**En une phrase :** Tu construis ta sagesse avec rigueur — ta philosophie est ancrée dans l'expérience et résiste à l'épreuve du temps.

## Ton moteur
Saturne en Capricorne en Maison 9 te pousse vers une quête de sens structurée et rigoureuse. Tu ne te satisfais pas des croyances légères — tu veux une philosophie qui tient face à la réalité. Les études supérieures et les voyages sont pris au sérieux.

## Ton défi
Le piège : devenir trop sceptique ou dogmatique, rejeter les croyances qui ne sont pas "prouvées", avoir peur de l'inconnu. La vraie sagesse inclut aussi le mystère.

## Maison 9 en Capricorne
Saturne structure ta quête de sens avec méthode. Tu peux devenir une autorité dans ton domaine d'expertise. Les voyages lointains peuvent être tardifs mais significatifs, souvent liés au travail.

## Micro-rituel du jour (2 min)
- Approfondir une connaissance de façon méthodique
- Trois respirations en honorant à la fois le savoir et le mystère
- Journal : « Quelle sagesse ai-je construite par l'expérience ? »""",

    ('capricorn', 11): """# ♄ Saturne en Capricorne
**En une phrase :** Tu construis des réseaux durables — tes amitiés et tes projets collectifs sont des structures qui résistent au temps.

## Ton moteur
Saturne en Capricorne en Maison 11 te pousse à choisir tes amis et tes groupes avec discernement. Tu préfères quelques relations fiables à de nombreuses connexions superficielles. Les projets collectifs sont menés avec rigueur et professionnalisme.

## Ton défi
Le piège : être trop sélectif dans tes amitiés, avoir du mal à faire confiance aux groupes, confondre réseau professionnel et amitié. Les meilleures communautés incluent aussi la spontanéité.

## Maison 11 en Capricorne
Saturne structure tes réseaux avec sérieux. Tes amis peuvent être plus âgés ou occuper des positions d'autorité. Tes projets humanitaires sont bien organisés et visent des résultats concrets.

## Micro-rituel du jour (2 min)
- Contacter un ami fiable et renforcer ce lien
- Trois respirations en appréciant la qualité plutôt que la quantité
- Journal : « Quelle amitié solide mérite mon attention aujourd'hui ? »""",

    ('capricorn', 12): """# ♄ Saturne en Capricorne
**En une phrase :** Tu explores l'invisible avec discipline — ta spiritualité est une construction patiente qui mène à une profonde sagesse intérieure.

## Ton moteur
Saturne en Capricorne en Maison 12 te demande de structurer ta vie intérieure avec la même rigueur que ta vie extérieure. Les pratiques spirituelles régulières, la méditation disciplinée, le travail sur l'inconscient portent des fruits durables.

## Ton défi
Le piège : fuir la vie intérieure par le travail, ignorer les messages de l'inconscient, avoir peur de perdre le contrôle. La vraie maîtrise inclut aussi l'abandon.

## Maison 12 en Capricorne
Saturne structure ta connexion à l'invisible. Tu peux avoir des guides ou des mentors intérieurs stricts mais bienveillants. Les retraites silencieuses et structurées te conviennent particulièrement.

## Micro-rituel du jour (2 min)
- Méditer avec discipline, même brièvement
- Trois respirations en accueillant ce qui émerge de l'intérieur
- Journal : « Quel message de mon inconscient mérite mon attention ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in SATURN_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'saturn',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP saturn/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='saturn',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT saturn/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
