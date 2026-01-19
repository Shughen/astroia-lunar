#!/usr/bin/env python3
"""Script d'insertion des interprétations Saturn/Gemini et Saturn/Cancer en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

SATURN_INTERPRETATIONS = {
    # GEMINI - 12 maisons
    ('gemini', 1): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu apprends à communiquer avec précision et profondeur — les mots deviennent des outils de construction.

## Ton moteur
Saturne en Gémeaux en Maison 1 te demande de développer une pensée structurée et une communication sérieuse. Tu peux te sentir limité dans l'expression ou avoir peur de mal t'exprimer. Le travail de Saturne est de maîtriser l'art de la parole pesée.

## Ton défi
Le piège : te retenir de parler par peur du jugement, avoir une pensée trop rigide, ou te disperser par anxiété mentale. L'équilibre se trouve dans une expression réfléchie mais fluide.

## Maison 1 en Gémeaux
Saturne structure ta présence et ta communication. Tu apprends à peser tes mots. Avec le temps, ta parole gagne en autorité et en crédibilité.

## Micro-rituel du jour (2 min)
- Formuler une idée importante avec précision et clarté
- Trois respirations en calmant le flux mental
- Journal : « Comment ma communication a-t-elle gagné en maturité récemment ? »""",

    ('gemini', 2): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu construis ta valeur par les compétences intellectuelles — le savoir devient richesse.

## Ton moteur
Saturne en Gémeaux en Maison 2 te demande de développer des ressources par l'apprentissage et la communication. Tu peux douter de la valeur de tes idées. Le travail de Saturne est de monétiser ton intelligence avec méthode.

## Ton défi
Le piège : éparpiller tes compétences sans les valoriser, douter de tes capacités intellectuelles, ou confondre quantité d'informations et vraie expertise. L'équilibre se trouve dans un savoir approfondi.

## Maison 2 en Gémeaux
Saturne structure ton rapport à l'argent et aux compétences. Tu apprends à transformer ton savoir en ressources tangibles. Avec le temps, ton expertise devient une source de revenus stable.

## Micro-rituel du jour (2 min)
- Identifier une compétence intellectuelle que tu pourrais mieux valoriser
- Trois respirations en reconnaissant la valeur de ce que tu sais
- Journal : « Quel savoir ai-je développé qui mérite d'être mieux rémunéré ? »""",

    ('gemini', 3): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu maîtrises l'art de la communication structurée — la pensée disciplinée devient ton superpouvoir.

## Ton moteur
Saturne en Gémeaux en Maison 3 amplifie les thèmes de communication et d'apprentissage. Tu peux avoir vécu des difficultés scolaires ou des blocages dans l'expression. Le travail de Saturne est de développer une maîtrise intellectuelle profonde.

## Ton défi
Le piège : te sentir lent ou inadéquat intellectuellement, avoir des relations difficiles avec l'entourage proche, ou sur-analyser au point de bloquer. L'équilibre se trouve dans une rigueur intellectuelle bienveillante.

## Maison 3 en Gémeaux
Saturne intensifie ici le besoin de maîtrise mentale. Tu apprends lentement mais profondément. Avec le temps, tu deviens un communicateur respecté et crédible.

## Micro-rituel du jour (2 min)
- Approfondir un sujet plutôt que de survoler plusieurs
- Trois respirations en accueillant ta façon d'apprendre
- Journal : « Quelle maîtrise intellectuelle ai-je développée avec le temps ? »""",

    ('gemini', 4): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu construis un foyer où la communication a du poids — les échanges familiaux deviennent structurants.

## Ton moteur
Saturne en Gémeaux en Maison 4 te demande de bâtir des fondations familiales sur la communication claire. Tu as peut-être grandi dans un foyer où les échanges étaient limités ou difficiles. Le travail de Saturne est de créer un dialogue familial mature.

## Ton défi
Le piège : le silence ou les malentendus dans la famille, un sentiment d'isolement intellectuel chez toi, ou des difficultés à exprimer tes émotions. L'équilibre se trouve dans une communication familiale structurée mais chaleureuse.

## Maison 4 en Gémeaux
Saturne structure ta vie privée autour des échanges. Tu apprends à communiquer avec ta famille de façon constructive. Avec le temps, ton foyer devient un lieu d'échanges nourrissants.

## Micro-rituel du jour (2 min)
- Initier une conversation significative avec un membre de ta famille
- Trois respirations en ouvrant le cœur à l'échange
- Journal : « Comment la communication dans ma famille a-t-elle évolué ? »""",

    ('gemini', 5): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu crées avec méthode et réflexion — l'expression créative devient un art maîtrisé.

## Ton moteur
Saturne en Gémeaux en Maison 5 te confronte à tes blocages dans l'expression créative et ludique. Tu peux avoir du mal à jouer avec légèreté ou à exprimer tes sentiments amoureux. Le travail de Saturne est d'apprendre à créer et aimer avec maturité.

## Ton défi
Le piège : intellectualiser les émotions au lieu de les vivre, avoir des relations amoureuses marquées par la communication difficile, ou bloquer ta créativité par perfectionnisme. L'équilibre se trouve dans une expression structurée mais joyeuse.

## Maison 5 en Gémeaux
Saturne structure tes plaisirs et ta créativité. Tu développes des talents d'écriture ou de communication créative. Avec le temps, tu apprends à jouer sérieusement et à aimer intelligemment.

## Micro-rituel du jour (2 min)
- T'autoriser un moment de création légère sans le sur-analyser
- Trois respirations en connectant tête et cœur
- Journal : « Comment puis-je exprimer ma joie avec plus de fluidité ? »""",

    ('gemini', 6): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu travailles avec méthode et précision mentale — l'efficacité naît de la communication organisée.

## Ton moteur
Saturne en Gémeaux en Maison 6 te demande de développer des routines de travail basées sur une communication claire et des processus structurés. Tu peux avoir tendance à la nervosité ou au surmenage mental. Le travail de Saturne est de canaliser ton énergie mentale.

## Ton défi
Le piège : la dispersion au travail, le stress lié à la surcharge d'informations, ou des problèmes de santé liés au système nerveux. L'équilibre se trouve dans une organisation mentale saine.

## Maison 6 en Gémeaux
Saturne structure ton quotidien autour de la communication et de l'apprentissage. Tu apprends à travailler de façon méthodique. Avec le temps, ta précision devient un atout professionnel majeur.

## Micro-rituel du jour (2 min)
- Organiser tes pensées et tes tâches avec méthode
- Trois respirations en calmant le système nerveux
- Journal : « Comment une meilleure organisation mentale améliore-t-elle mon travail ? »""",

    ('gemini', 7): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu construis des partenariats basés sur la communication mature — le dialogue devient le ciment du couple.

## Ton moteur
Saturne en Gémeaux en Maison 7 te demande de développer une communication solide dans les partenariats. Tu peux attirer des partenaires avec qui les échanges sont difficiles ou structurés. Le travail de Saturne est d'apprendre le dialogue de couple mature.

## Ton défi
Le piège : des malentendus récurrents dans les relations, un partenaire trop sérieux ou critique, ou des difficultés à exprimer tes besoins. L'équilibre se trouve dans une communication relationnelle construite avec soin.

## Maison 7 en Gémeaux
Saturne structure tes partenariats autour de l'échange intellectuel. Tu apprends à communiquer avec maturité en couple. Avec le temps, tes relations gagnent en profondeur et en clarté.

## Micro-rituel du jour (2 min)
- Exprimer un besoin ou un ressenti à un partenaire de façon claire et calme
- Trois respirations en préparant une communication bienveillante
- Journal : « Comment la communication dans mes relations a-t-elle mûri ? »""",

    ('gemini', 8): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu traverses les crises avec lucidité — les transformations se comprennent avant de se vivre.

## Ton moteur
Saturne en Gémeaux en Maison 8 te demande d'affronter les profondeurs avec ton intelligence. Tu peux intellectualiser les émotions profondes ou avoir du mal à parler de sujets tabous. Le travail de Saturne est de mettre des mots sur l'indicible.

## Ton défi
Le piège : analyser les crises sans les traverser émotionnellement, des blocages dans l'intimité liés à la communication, ou des difficultés à partager les ressources. L'équilibre se trouve dans une compréhension qui n'évite pas le ressenti.

## Maison 8 en Gémeaux
Saturne structure ton rapport aux transformations et aux échanges profonds. Tu apprends à parler de ce qui fait peur. Avec le temps, ta capacité à communiquer sur les sujets difficiles devient une force.

## Micro-rituel du jour (2 min)
- Mettre des mots sur une émotion profonde que tu évites habituellement
- Trois respirations en accueillant ce qui veut être dit
- Journal : « Quelle vérité difficile ai-je osé formuler récemment ? »""",

    ('gemini', 9): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu construis ta sagesse par l'étude rigoureuse — la philosophie devient une discipline.

## Ton moteur
Saturne en Gémeaux en Maison 9 te demande de développer une pensée philosophique structurée. Tu peux avoir du mal avec les croyances non prouvables ou les études supérieures. Le travail de Saturne est de bâtir une vision du monde solide par l'étude patiente.

## Ton défi
Le piège : rejeter ce qui ne se prouve pas logiquement, des études difficiles ou retardées, ou un scepticisme qui ferme l'esprit. L'équilibre se trouve dans une ouverture intellectuelle disciplinée.

## Maison 9 en Gémeaux
Saturne structure ta quête de sens autour de l'apprentissage. Tu développes une sagesse basée sur la connaissance vérifiée. Avec le temps, tu peux devenir enseignant ou penseur respecté.

## Micro-rituel du jour (2 min)
- Approfondir une idée philosophique ou spirituelle avec rigueur
- Trois respirations en t'ouvrant à ce qui dépasse la logique
- Journal : « Quelle sagesse ai-je construite par l'étude patiente ? »""",

    ('gemini', 10): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu bâtis ta carrière sur tes compétences en communication — la maîtrise des mots devient pouvoir.

## Ton moteur
Saturne en Gémeaux en Maison 10 te demande de développer une expertise en communication pour réussir professionnellement. Tu peux avoir des blocages dans l'expression publique ou des difficultés à te faire entendre. Le travail de Saturne est de devenir un communicateur d'autorité.

## Ton défi
Le piège : peur de parler en public, réputation de froideur intellectuelle, ou carrière bloquée par des problèmes de communication. L'équilibre se trouve dans une parole professionnelle maîtrisée.

## Maison 10 en Gémeaux
Saturne structure ta carrière autour de la communication. Tu apprends à peser tes mots professionnellement. Avec le temps, tu peux atteindre des positions où ta parole compte vraiment.

## Micro-rituel du jour (2 min)
- Travailler une communication professionnelle importante
- Trois respirations en préparant ta voix d'autorité
- Journal : « Comment mes compétences en communication servent-elles ma carrière ? »""",

    ('gemini', 11): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu construis des réseaux basés sur l'échange intellectuel solide — les idées partagées créent des liens durables.

## Ton moteur
Saturne en Gémeaux en Maison 11 te demande de développer des amitiés et des projets collectifs basés sur des échanges de qualité. Tu peux avoir peu d'amis mais des connexions intellectuelles profondes. Le travail de Saturne est de créer des réseaux de pensée constructifs.

## Ton défi
Le piège : l'isolement intellectuel, des groupes où la communication est difficile, ou des projets collectifs bloqués par des malentendus. L'équilibre se trouve dans des échanges de groupe structurés mais ouverts.

## Maison 11 en Gémeaux
Saturne structure tes réseaux autour de l'échange d'idées. Tu apprends à communiquer efficacement en groupe. Avec le temps, tu deviens un pont entre des personnes et des idées différentes.

## Micro-rituel du jour (2 min)
- Initier un échange intellectuel de qualité avec un ami ou un groupe
- Trois respirations en valorisant la communication constructive
- Journal : « Comment mes échanges d'idées créent-ils des liens durables ? »""",

    ('gemini', 12): """# ♄ Saturne en Gémeaux
**En une phrase :** Tu apprivoises tes peurs mentales — l'inconscient livre ses secrets par les mots.

## Ton moteur
Saturne en Gémeaux en Maison 12 te confronte à tes blocages cachés dans la communication et la pensée. Tu peux avoir des pensées anxieuses ou des difficultés à exprimer ce qui reste dans l'ombre. Le travail de Saturne est de mettre en mots l'inconscient.

## Ton défi
Le piège : ruminations mentales, pensées autodestructrices, ou incapacité à exprimer des vérités profondes. L'équilibre se trouve dans une exploration mentale de l'inconscient avec bienveillance.

## Maison 12 en Gémeaux
Saturne structure ton monde intérieur mental. Tu apprends à observer tes pensées sans t'y identifier. Avec le temps, tu développes une sagesse mentale qui transcende les mots.

## Micro-rituel du jour (2 min)
- Observer une pensée récurrente avec détachement bienveillant
- Trois respirations en laissant le silence apaiser le mental
- Journal : « Quelle pensée inconsciente ai-je réussi à mettre en lumière ? »""",

    # CANCER - 12 maisons
    ('cancer', 1): """# ♄ Saturne en Cancer
**En une phrase :** Tu apprends à protéger sans t'enfermer — la sensibilité devient force quand elle est maîtrisée.

## Ton moteur
Saturne en Cancer en Maison 1 te demande de développer une confiance émotionnelle stable. Tu peux te sentir vulnérable ou avoir du mal à montrer tes sentiments. Le travail de Saturne est de construire une carapace saine sans te couper de tes émotions.

## Ton défi
Le piège : te fermer émotionnellement pour te protéger, paraître froid alors que tu ressens intensément, ou t'accrocher au passé. L'équilibre se trouve dans une sensibilité exprimée avec maturité.

## Maison 1 en Cancer
Saturne structure ta présence émotionnelle. Tu apprends à montrer ta sensibilité de façon mesurée. Avec le temps, ta capacité à protéger et nourrir devient une force reconnue.

## Micro-rituel du jour (2 min)
- Exprimer une émotion de façon authentique et mesurée
- Trois respirations en te connectant à ta sensibilité sans la juger
- Journal : « Comment ai-je montré ma sensibilité de façon mature récemment ? »""",

    ('cancer', 2): """# ♄ Saturne en Cancer
**En une phrase :** Tu construis ta sécurité matérielle pour protéger ceux que tu aimes — l'abondance devient nid.

## Ton moteur
Saturne en Cancer en Maison 2 te demande de bâtir des ressources qui nourrissent ta sécurité émotionnelle et celle de tes proches. Tu peux avoir des peurs autour de la sécurité financière liée au foyer. Le travail de Saturne est de construire une stabilité matérielle rassurante.

## Ton défi
Le piège : l'insécurité financière liée à l'anxiété émotionnelle, l'attachement excessif aux biens par besoin de sécurité, ou confondre confort matériel et sécurité émotionnelle. L'équilibre se trouve dans une abondance qui nourrit vraiment.

## Maison 2 en Cancer
Saturne structure ton rapport à l'argent autour de la protection. Tu apprends à créer une sécurité matérielle stable. Avec le temps, tes ressources deviennent un cocon pour toi et les tiens.

## Micro-rituel du jour (2 min)
- Identifier une ressource qui nourrit vraiment ton sentiment de sécurité
- Trois respirations en distinguant sécurité matérielle et émotionnelle
- Journal : « Comment mes ressources soutiennent-elles ma sécurité intérieure ? »""",

    ('cancer', 3): """# ♄ Saturne en Cancer
**En une phrase :** Tu communiques avec le cœur et la prudence — les mots portent le poids des émotions.

## Ton moteur
Saturne en Cancer en Maison 3 te demande de développer une communication qui intègre sensibilité et structure. Tu peux avoir du mal à exprimer tes émotions ou te sentir incompris. Le travail de Saturne est d'apprendre à parler avec le cœur de façon claire.

## Ton défi
Le piège : garder tes sentiments pour toi, des relations difficiles avec l'entourage proche, ou une communication teintée de susceptibilité. L'équilibre se trouve dans une expression émotionnelle structurée.

## Maison 3 en Cancer
Saturne structure ta communication autour de l'émotion. Tu apprends à exprimer tes sentiments de façon constructive. Avec le temps, ta parole émotionnelle gagne en profondeur et en impact.

## Micro-rituel du jour (2 min)
- Exprimer un ressenti à quelqu'un de proche de façon claire
- Trois respirations en ouvrant le cœur à la communication
- Journal : « Comment ai-je mieux exprimé mes émotions récemment ? »""",

    ('cancer', 4): """# ♄ Saturne en Cancer
**En une phrase :** Tu construis un foyer solide malgré les blessures — les racines se renforcent par le travail intérieur.

## Ton moteur
Saturne en Cancer en Maison 4 amplifie les défis autour du foyer et de la sécurité émotionnelle. Tu as peut-être vécu des limitations dans l'enfance ou un sentiment de manque affectif. Le travail de Saturne est de créer le foyer que tu n'as peut-être pas eu.

## Ton défi
Le piège : des blessures familiales non guéries, difficulté à créer un chez-toi chaleureux, ou attachement excessif au passé. L'équilibre se trouve dans la construction patiente d'une sécurité intérieure.

## Maison 4 en Cancer
Saturne intensifie ici les thèmes de foyer et de racines. Tu apprends à créer ta propre sécurité émotionnelle. Avec le temps, tu deviens le pilier stable de ta famille.

## Micro-rituel du jour (2 min)
- Faire quelque chose qui renforce ton sentiment de foyer intérieur
- Trois respirations en te connectant à une sécurité qui ne dépend pas de l'extérieur
- Journal : « Quelle blessure familiale ai-je transformée en force ? »""",

    ('cancer', 5): """# ♄ Saturne en Cancer
**En une phrase :** Tu apprends à aimer et créer sans te perdre — l'expression devient protection.

## Ton moteur
Saturne en Cancer en Maison 5 te confronte à tes blocages dans l'expression de l'amour et de la créativité. Tu peux avoir peur de montrer ta vulnérabilité ou de t'ouvrir dans les relations amoureuses. Le travail de Saturne est d'apprendre à aimer avec maturité.

## Ton défi
Le piège : te protéger au point de ne pas profiter, des relations amoureuses marquées par la peur de l'abandon, ou une créativité bridée par l'insécurité. L'équilibre se trouve dans une joie qui accepte la vulnérabilité.

## Maison 5 en Cancer
Saturne structure tes plaisirs et tes amours autour de la sécurité émotionnelle. Tu apprends à t'ouvrir progressivement. Avec le temps, tes relations et créations gagnent en profondeur.

## Micro-rituel du jour (2 min)
- T'autoriser un moment de joie vulnérable sans te protéger
- Trois respirations en acceptant que l'amour demande du risque
- Journal : « Comment ai-je ouvert mon cœur malgré ma peur récemment ? »""",

    ('cancer', 6): """# ♄ Saturne en Cancer
**En une phrase :** Tu travailles avec soin et protection — le service devient une forme de nourriture.

## Ton moteur
Saturne en Cancer en Maison 6 te demande de développer un travail quotidien qui nourrit et protège. Tu peux avoir tendance à trop donner au travail ou à négliger ta santé émotionnelle. Le travail de Saturne est de trouver un équilibre entre servir et te préserver.

## Ton défi
Le piège : t'épuiser à prendre soin des autres au travail, des problèmes de santé liés au stress émotionnel, ou un quotidien qui manque de chaleur. L'équilibre se trouve dans un service qui te nourrit aussi.

## Maison 6 en Cancer
Saturne structure ton quotidien autour du soin. Tu apprends à travailler de façon nourrissante. Avec le temps, tu développes un environnement de travail protecteur et efficace.

## Micro-rituel du jour (2 min)
- Intégrer un geste de soin pour toi dans ta routine de travail
- Trois respirations en équilibrant donner et recevoir
- Journal : « Comment prendre soin de moi améliore-t-il mon travail ? »""",

    ('cancer', 7): """# ♄ Saturne en Cancer
**En une phrase :** Tu construis des partenariats protecteurs — l'engagement devient un cocon partagé.

## Ton moteur
Saturne en Cancer en Maison 7 te demande de bâtir des relations durables basées sur la sécurité émotionnelle mutuelle. Tu peux attirer des partenaires avec lesquels tu dois travailler les thèmes de protection et de dépendance. Le travail de Saturne est d'apprendre à créer des liens sécurisants.

## Ton défi
Le piège : des relations marquées par la peur de l'abandon, des partenaires qui étouffent ou qui manquent de chaleur, ou un attachement excessif au couple. L'équilibre se trouve dans une interdépendance mature.

## Maison 7 en Cancer
Saturne structure tes partenariats autour de la sécurité émotionnelle. Tu apprends à créer des liens protecteurs sans étouffer. Avec le temps, tes relations deviennent des havres de stabilité.

## Micro-rituel du jour (2 min)
- Exprimer un besoin de sécurité à un partenaire de façon claire
- Trois respirations en cultivant la confiance dans la relation
- Journal : « Comment mes partenariats sont-ils devenus plus sécurisants ? »""",

    ('cancer', 8): """# ♄ Saturne en Cancer
**En une phrase :** Tu traverses les crises en protégeant ce qui compte — les transformations renforcent tes fondations.

## Ton moteur
Saturne en Cancer en Maison 8 te demande d'affronter les pertes et les transformations tout en préservant ta sécurité intérieure. Tu peux avoir des peurs profondes liées à l'abandon ou à la perte. Le travail de Saturne est d'apprendre que la vraie sécurité survit aux crises.

## Ton défi
Le piège : s'accrocher au passé par peur du changement, des difficultés à partager les ressources émotionnelles, ou des deuils non résolus. L'équilibre se trouve dans une transformation qui protège l'essentiel.

## Maison 8 en Cancer
Saturne structure ton rapport aux crises autour de la protection. Tu apprends à traverser les transformations sans perdre ton ancrage. Avec le temps, ta résilience émotionnelle devient remarquable.

## Micro-rituel du jour (2 min)
- Identifier ce qui reste stable en toi malgré les changements
- Trois respirations en faisant confiance à ta capacité de rebondir
- Journal : « Quelle transformation m'a finalement rendu plus sécurisé intérieurement ? »""",

    ('cancer', 9): """# ♄ Saturne en Cancer
**En une phrase :** Tu construis ta sagesse sur des fondations émotionnelles — la philosophie devient foyer.

## Ton moteur
Saturne en Cancer en Maison 9 te demande de développer une vision du monde qui te sécurise. Tu peux avoir besoin de croyances qui te font sentir chez toi dans l'univers. Le travail de Saturne est de trouver une sagesse qui nourrit.

## Ton défi
Le piège : des croyances rigides par besoin de sécurité, difficulté à voyager loin de chez toi, ou une philosophie qui isole plutôt qu'elle n'ouvre. L'équilibre se trouve dans une ouverture qui rassure.

## Maison 9 en Cancer
Saturne structure ta quête de sens autour de l'appartenance. Tu apprends à trouver un foyer philosophique. Avec le temps, ta sagesse devient un refuge pour toi et les autres.

## Micro-rituel du jour (2 min)
- Explorer une croyance qui te fait te sentir chez toi dans le monde
- Trois respirations en t'ouvrant à l'inconnu avec confiance
- Journal : « Quelle sagesse me donne un sentiment de sécurité universelle ? »""",

    ('cancer', 10): """# ♄ Saturne en Cancer
**En une phrase :** Tu bâtis ta carrière sur ta capacité à protéger et nourrir — le leadership devient maternel.

## Ton moteur
Saturne en Cancer en Maison 10 te demande de développer une carrière qui intègre tes qualités de soin et de protection. Tu peux avoir des blocages entre vie professionnelle et vie familiale. Le travail de Saturne est de trouver un succès qui ne sacrifie pas l'essentiel.

## Ton défi
Le piège : sacrifier la famille pour la carrière ou l'inverse, une réputation de froideur qui cache une grande sensibilité, ou des difficultés à s'affirmer professionnellement. L'équilibre se trouve dans un leadership nourrissant.

## Maison 10 en Cancer
Saturne structure ta carrière autour des thèmes de protection et de soin. Tu apprends à réussir sans trahir tes valeurs familiales. Avec le temps, tu deviens un leader qui prend soin de son équipe.

## Micro-rituel du jour (2 min)
- Identifier comment ta capacité de protection peut servir ta carrière
- Trois respirations en unifiant ambition et valeurs familiales
- Journal : « Comment puis-je réussir tout en nourrissant ce qui compte vraiment ? »""",

    ('cancer', 11): """# ♄ Saturne en Cancer
**En une phrase :** Tu crées des communautés protectrices — les amitiés deviennent des familles choisies.

## Ton moteur
Saturne en Cancer en Maison 11 te demande de développer des amitiés et des projets collectifs qui offrent un sentiment d'appartenance. Tu peux avoir du mal à trouver ta place dans les groupes ou chercher la sécurité dans les amitiés. Le travail de Saturne est de créer des liens qui nourrissent.

## Ton défi
Le piège : des amitiés décevantes par manque de chaleur, difficulté à s'ouvrir aux groupes, ou attentes familiales projetées sur les amis. L'équilibre se trouve dans des communautés qui respectent les besoins émotionnels.

## Maison 11 en Cancer
Saturne structure tes réseaux autour de l'appartenance. Tu apprends à créer des cercles protecteurs. Avec le temps, tes amitiés deviennent des sources de sécurité durable.

## Micro-rituel du jour (2 min)
- Entretenir une amitié qui te fait te sentir en famille
- Trois respirations en appréciant les liens qui te nourrissent
- Journal : « Quelle amitié me donne un sentiment de famille choisie ? »""",

    ('cancer', 12): """# ♄ Saturne en Cancer
**En une phrase :** Tu apprivoises tes blessures d'enfance — l'inconscient libère ses mémoires protectrices.

## Ton moteur
Saturne en Cancer en Maison 12 te confronte à tes blessures émotionnelles profondes et aux mémoires familiales cachées. Tu peux porter des fardeaux ancestraux ou avoir des peurs inconscientes liées à l'abandon. Le travail de Saturne est de guérir les racines invisibles.

## Ton défi
Le piège : des schémas répétitifs liés aux blessures d'enfance, l'isolement pour se protéger, ou des peurs irrationnelles autour de la sécurité. L'équilibre se trouve dans une exploration bienveillante de l'inconscient familial.

## Maison 12 en Cancer
Saturne structure ton monde intérieur autour des mémoires émotionnelles. Tu apprends à guérir les blessures cachées. Avec le temps, tu transformes les fardeaux ancestraux en sagesse.

## Micro-rituel du jour (2 min)
- Accueillir une émotion ancienne avec compassion
- Trois respirations en te connectant à une guérison intérieure
- Journal : « Quelle blessure d'enfance ai-je commencé à transformer ? »""",
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
