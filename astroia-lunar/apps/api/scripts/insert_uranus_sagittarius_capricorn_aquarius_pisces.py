#!/usr/bin/env python3
"""Script d'insertion des interprétations Uranus/Sagittarius, Capricorn, Aquarius, Pisces en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

URANUS_INTERPRETATIONS = {
    # SAGITTARIUS - 12 maisons
    ('sagittarius', 1): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu incarnes une vision révolutionnaire — ton identité se forge en explorant de nouvelles frontières de la pensée.

## Ton moteur
Uranus en Sagittaire en Maison 1 te donne une personnalité visionnaire et aventurière. Tu es naturellement attiré par ce qui est lointain, différent, inexploré. Ta philosophie de vie est ta signature.

## Ton défi
Le piège : une quête de sens dispersée, fuir la réalité dans les grandes idées, confondre liberté et irresponsabilité. La vraie vision révolutionnaire s'incarne aussi concrètement.

## Maison 1 en Sagittaire
Uranus électrise ta quête d'expansion. Tu projettes une image d'aventurier philosophique. Ton apparence peut refléter tes voyages et tes croyances.

## Micro-rituel du jour (2 min)
- Identifier une vision qui te distingue et l'affirmer
- Trois respirations en embrassant ta soif d'expansion
- Journal : « Quelle frontière ai-je envie d'explorer prochainement ? »""",

    ('sagittarius', 2): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu révolutionnes ta prospérité par l'expansion — tes ressources viennent quand tu oses voir grand.

## Ton moteur
Uranus en Sagittaire en Maison 2 crée des revenus par l'étranger, l'enseignement, l'édition, les grandes visions. Tu peux générer de l'abondance en explorant de nouvelles frontières économiques.

## Ton défi
Le piège : des finances qui fluctuent avec tes aventures, négliger le concret pour les grandes idées, confondre potentiel et réalité. La vraie prospérité visionnaire s'ancre aussi.

## Maison 2 en Sagittaire
Uranus secoue tes finances pour les étendre. Tu peux gagner de l'argent de façons internationales ou philosophiques. Tes valeurs sont liées à la liberté et au sens.

## Micro-rituel du jour (2 min)
- Identifier une opportunité d'expansion qui pourrait être lucrative
- Trois respirations en connectant abondance et vision
- Journal : « Comment ma soif d'expansion peut-elle créer de la valeur ? »""",

    ('sagittarius', 3): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu communiques avec vision — tes mots élargissent les horizons et inspirent de nouvelles perspectives.

## Ton moteur
Uranus en Sagittaire en Maison 3 te donne une communication expansive et inspirante. Tu sais présenter les grandes idées, ouvrir les esprits, créer de l'enthousiasme pour de nouvelles possibilités.

## Ton défi
Le piège : une communication qui exagère ou promet trop, avoir du mal avec les détails, confondre enthousiasme et vérité. La vraie communication visionnaire reste aussi honnête.

## Maison 3 en Sagittaire
Uranus électrise tes échanges de vision et d'expansion. Tes relations avec frères, sœurs et voisins peuvent impliquer des voyages ou des différences culturelles.

## Micro-rituel du jour (2 min)
- Partager une vision inspirante avec quelqu'un
- Trois respirations en mesurant l'impact de tes mots
- Journal : « Comment ma communication peut-elle élargir les horizons ? »""",

    ('sagittarius', 4): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu révolutionnes la famille par l'ouverture — ton foyer devient un carrefour de cultures et de philosophies.

## Ton moteur
Uranus en Sagittaire en Maison 4 crée un environnement familial ouvert sur le monde. Ton foyer peut accueillir des personnes de toutes origines, intégrer des influences culturelles diverses.

## Ton défi
Le piège : un foyer trop instable par envie d'ailleurs, avoir du mal à créer des racines, fuir les responsabilités domestiques. La vraie maison ouverte a aussi des fondations.

## Maison 4 en Sagittaire
Uranus secoue ta vie familiale pour l'ouvrir. Tu as peut-être grandi dans une famille multiculturelle ou voyageuse. Ton foyer peut être un lieu de rassemblement philosophique.

## Micro-rituel du jour (2 min)
- Créer un moment d'ouverture culturelle ou philosophique chez toi
- Trois respirations en faisant de ton foyer un pont vers le monde
- Journal : « Comment mon chez-moi peut-il refléter mon ouverture au monde ? »""",

    ('sagittarius', 5): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu crées avec vision aventurière — tes œuvres et tes amours sont des explorations de nouvelles possibilités.

## Ton moteur
Uranus en Sagittaire en Maison 5 te pousse vers une créativité qui explore et expérimente. Tu peux créer dans des domaines qui touchent à l'étranger, la philosophie, l'aventure. En amour, tu cherches des partenaires qui partagent ta soif d'exploration.

## Ton défi
Le piège : des amours qui restent superficielles par peur de l'engagement, une créativité qui s'éparpille, confondre nouveauté et profondeur. La vraie joie créative sait aussi s'approfondir.

## Maison 5 en Sagittaire
Uranus électrise tes plaisirs d'aventure et d'exploration. Tu peux avoir des attirances pour des personnes d'autres cultures. Ta créativité s'épanouit dans les grands projets.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui élargit tes horizons
- Trois respirations en laissant ta joie explorer
- Journal : « Quelle création aventurière me ferait vraiment vibrer ? »""",

    ('sagittarius', 6): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu révolutionnes le travail par la vision — ton efficacité vient quand tu peux voir le sens plus large.

## Ton moteur
Uranus en Sagittaire en Maison 6 te pousse vers des métiers qui ont du sens et de l'impact large. Tu ne supportes pas un travail sans vision — tu dois comprendre comment il sert quelque chose de plus grand.

## Ton défi
Le piège : avoir du mal avec les tâches routinières, chercher le sens au détriment de l'efficacité, changer de travail trop souvent. La vraie efficacité visionnaire inclut aussi la discipline.

## Maison 6 en Sagittaire
Uranus secoue ton quotidien pour lui donner du sens. Tu travailles mieux quand tu comprends la vision globale. Ta santé peut bénéficier de philosophies de vie ou de voyages.

## Micro-rituel du jour (2 min)
- Relier une tâche quotidienne à un sens plus large
- Trois respirations en trouvant la vision dans le quotidien
- Journal : « Comment mon travail sert-il quelque chose de plus grand ? »""",

    ('sagittarius', 7): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu révolutionnes les relations par l'aventure partagée — tes partenariats sont des voyages d'exploration commune.

## Ton moteur
Uranus en Sagittaire en Maison 7 crée des relations basées sur l'exploration et la croissance commune. Tu attires des partenaires avec qui tu peux grandir, voyager, philosopher.

## Ton défi
Le piège : fuir l'engagement par désir de liberté, des relations qui restent superficielles, confondre aventure et amour. Les meilleures relations combinent exploration et engagement.

## Maison 7 en Sagittaire
Uranus électrise tes partenariats d'aventure et de sens. Tu peux avoir des relations avec des personnes d'autres cultures. Tes contrats peuvent être internationaux.

## Micro-rituel du jour (2 min)
- Proposer une exploration ou une aventure à un partenaire
- Trois respirations en célébrant le voyage ensemble
- Journal : « Comment mes relations peuvent-elles être des aventures de croissance ? »""",

    ('sagittarius', 8): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu traverses les crises avec foi — les transformations deviennent des initiations qui élargissent ta vision.

## Ton moteur
Uranus en Sagittaire en Maison 8 te donne la capacité de trouver du sens dans les crises. Les épreuves deviennent des occasions d'approfondir ta philosophie, d'élargir ta compréhension de la vie.

## Ton défi
Le piège : philosopher sur les crises au lieu de les traverser émotionnellement, fuir l'intensité dans l'abstraction, confondre optimisme et déni. La vraie transformation visionnaire inclut la traversée.

## Maison 8 en Sagittaire
Uranus secoue ta relation aux transformations pour les éclairer de sens. Ta sexualité peut être liée à l'exploration ou au transcendant. Les ressources partagées peuvent venir de l'étranger.

## Micro-rituel du jour (2 min)
- Identifier le sens ou l'enseignement d'une crise récente
- Trois respirations en accueillant la transformation comme initiation
- Journal : « Quelle sagesse ai-je gagnée de mes épreuves ? »""",

    ('sagittarius', 9): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu révolutionnes la sagesse — ta quête de sens est une exploration radicale de nouvelles vérités.

## Ton moteur
Uranus en Sagittaire en Maison 9 amplifie au maximum ta soif de comprendre et d'explorer. Tu ne te satisfais pas des réponses toutes faites — tu dois trouver ta propre vérité. Les voyages, les études, l'enseignement sont tes voies.

## Ton défi
Le piège : une quête de sens qui s'éparpille, adhérer à des croyances excentriques, confondre originalité et vérité. La vraie sagesse révolutionnaire est aussi humble.

## Maison 9 en Sagittaire
Uranus électrise au maximum ta quête de sens. Tu es fait pour les grandes explorations philosophiques, les voyages transformateurs, l'enseignement révolutionnaire.

## Micro-rituel du jour (2 min)
- Explorer une idée qui remet en question tes croyances actuelles
- Trois respirations en t'ouvrant à de nouvelles vérités
- Journal : « Quelle vérité révolutionnaire me guide actuellement ? »""",

    ('sagittarius', 10): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu révolutionnes ta carrière par la vision — ta réussite vient quand tu portes un message qui élargit les horizons.

## Ton moteur
Uranus en Sagittaire en Maison 10 te pousse vers une carrière qui a un impact large et visionnaire. Tu peux réussir dans l'enseignement, l'édition, les voyages, tout ce qui élargit les perspectives.

## Ton défi
Le piège : une carrière trop dispersée ou utopique, avoir du mal à concrétiser ta vision, promettre plus que tu ne peux tenir. La vraie réussite visionnaire s'incarne aussi.

## Maison 10 en Sagittaire
Uranus secoue ta réputation pour la rendre plus visionnaire. On te reconnaît pour ta capacité à voir loin et à inspirer. Ta carrière peut être internationale.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière peut porter une vision plus large
- Trois respirations en alignant ambition et sens
- Journal : « Quelle vision ma carrière peut-elle servir ? »""",

    ('sagittarius', 11): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu révolutionnes l'action collective par la vision partagée — tes amitiés et tes projets sont des aventures d'exploration commune.

## Ton moteur
Uranus en Sagittaire en Maison 11 te connecte à des réseaux de visionnaires et d'explorateurs. Tes amis partagent ta soif de sens et d'aventure. Les projets collectifs ont une portée large.

## Ton défi
Le piège : des amitiés superficielles par dispersion, des projets qui restent au stade de l'idée, imposer ta vision au groupe. Les meilleures communautés honorent toutes les visions.

## Maison 11 en Sagittaire
Uranus électrise tes réseaux de vision et d'expansion. Tu es fait pour les mouvements philosophiques, les associations internationales, les projets d'éducation ou de voyage collectif.

## Micro-rituel du jour (2 min)
- Partager une vision inspirante avec un groupe
- Trois respirations en honorant la diversité des perspectives
- Journal : « Quel projet collectif visionnaire m'inspire ? »""",

    ('sagittarius', 12): """# ♅ Uranus en Sagittaire
**En une phrase :** Tu révolutionnes ta vie intérieure par l'expansion — ton inconscient est une source de visions et d'intuitions prophétiques.

## Ton moteur
Uranus en Sagittaire en Maison 12 crée des connexions entre ta quête de sens et les dimensions invisibles. Tes rêves peuvent être prophétiques, tes méditations peuvent t'emmener loin.

## Ton défi
Le piège : fuir la réalité dans des visions spirituelles, confondre intuition et illusion, avoir du mal à ancrer tes perceptions. La vraie sagesse intérieure s'incarne aussi.

## Maison 12 en Sagittaire
Uranus secoue ta connexion à l'invisible pour l'élargir. Tu peux avoir des visions qui dépassent ton expérience personnelle. Les retraites de méditation profonde te transforment.

## Micro-rituel du jour (2 min)
- Méditer en t'ouvrant à des visions au-delà de toi
- Trois respirations en ancrant tes perceptions
- Journal : « Quelle vision intérieure me guide vers l'expansion ? »""",

    # CAPRICORN - 12 maisons
    ('capricorn', 1): """# ♅ Uranus en Capricorne
**En une phrase :** Tu incarnes une révolution structurée — ton identité se forge en transformant les systèmes de l'intérieur.

## Ton moteur
Uranus en Capricorne en Maison 1 te donne une personnalité qui allie ambition et innovation. Tu ne détruis pas les structures — tu les transformes. Le changement passe par la maîtrise.

## Ton défi
Le piège : une tension entre conformisme et rébellion, avoir du mal à trouver ta place, confondre pouvoir et liberté. La vraie révolution structurée sait quand rompre et quand construire.

## Maison 1 en Capricorne
Uranus électrise ton ambition et ton sens des responsabilités. Tu projettes une image d'autorité originale. Ton apparence peut refléter ta position ou ton statut de façon unique.

## Micro-rituel du jour (2 min)
- Identifier comment tu transformes les structures autour de toi
- Trois respirations en assumant ton pouvoir de changement
- Journal : « Comment mon ambition sert-elle le changement ? »""",

    ('capricorn', 2): """# ♅ Uranus en Capricorne
**En une phrase :** Tu révolutionnes ta prospérité par la structure — tes ressources viennent quand tu innoves au sein des systèmes.

## Ton moteur
Uranus en Capricorne en Maison 2 crée des revenus par la transformation des structures économiques. Tu peux prospérer en innovant dans des domaines traditionnels, en apportant du changement aux systèmes établis.

## Ton défi
Le piège : des tensions entre sécurité et changement, des finances qui fluctuent avec les restructurations, confondre accumulation et valeur. La vraie prospérité structurée évolue aussi.

## Maison 2 en Capricorne
Uranus secoue tes finances pour les restructurer. Tu peux gagner de l'argent en transformant des organisations ou des systèmes. Tes valeurs sont liées à la responsabilité et à l'accomplissement.

## Micro-rituel du jour (2 min)
- Identifier une structure financière que tu pourrais améliorer
- Trois respirations en connectant stabilité et changement
- Journal : « Comment puis-je créer de la valeur en transformant les structures ? »""",

    ('capricorn', 3): """# ♅ Uranus en Capricorne
**En une phrase :** Tu communiques avec autorité innovante — tes mots transforment les organisations et les systèmes.

## Ton moteur
Uranus en Capricorne en Maison 3 te donne une communication qui peut changer les structures. Tu sais présenter le changement de façon crédible et professionnelle, convaincre les décideurs.

## Ton défi
Le piège : une communication trop rigide ou autoritaire, avoir du mal avec l'informel, confondre sérieux et froideur. La vraie communication transformatrice sait aussi être accessible.

## Maison 3 en Capricorne
Uranus électrise tes échanges d'autorité et de changement. Tes relations avec frères, sœurs et voisins peuvent impliquer des enjeux de responsabilité ou de transformation.

## Micro-rituel du jour (2 min)
- Communiquer un changement de façon professionnelle et inspirante
- Trois respirations en trouvant l'équilibre entre autorité et accessibilité
- Journal : « Comment ma communication peut-elle mieux servir le changement ? »""",

    ('capricorn', 4): """# ♅ Uranus en Capricorne
**En une phrase :** Tu révolutionnes la famille par la restructuration — ton foyer devient un lieu de transformation des traditions.

## Ton moteur
Uranus en Capricorne en Maison 4 crée des changements dans les structures familiales. Tu peux transformer les traditions familiales, restructurer les héritages, moderniser les fondations.

## Ton défi
Le piège : des ruptures familiales déstabilisantes, des tensions entre tradition et changement, confondre transformation et rejet des racines. La vraie restructuration familiale honore aussi le passé.

## Maison 4 en Capricorne
Uranus secoue tes fondations pour les restructurer. Tu as peut-être grandi dans une famille en transformation ou tu transformes la tienne. Ton foyer peut refléter un équilibre unique entre ancien et nouveau.

## Micro-rituel du jour (2 min)
- Identifier une tradition familiale que tu transformes positivement
- Trois respirations en honorant tes racines tout en évoluant
- Journal : « Comment ma famille évolue-t-elle tout en gardant ses fondations ? »""",

    ('capricorn', 5): """# ♅ Uranus en Capricorne
**En une phrase :** Tu crées avec ambition structurée — tes œuvres transforment les institutions et laissent une trace durable.

## Ton moteur
Uranus en Capricorne en Maison 5 te pousse vers une créativité qui a un impact sur les structures. Tu ne crées pas juste pour le plaisir — tu veux que tes œuvres changent les choses. En amour, tu cherches des partenaires ambitieux qui partagent ta vision du changement.

## Ton défi
Le piège : une créativité trop sérieuse qui oublie la joie, des amours basées sur l'ambition, confondre accomplissement et bonheur. La vraie joie créative sait aussi être légère.

## Maison 5 en Capricorne
Uranus électrise tes plaisirs d'ambition et de réalisation. Tu peux être attiré par des partenaires en position d'autorité. Ta créativité s'épanouit dans les projets d'envergure.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif simple et joyeux
- Trois respirations en laissant la joie être légère
- Journal : « Comment ma créativité peut-elle être à la fois ambitieuse et joyeuse ? »""",

    ('capricorn', 6): """# ♅ Uranus en Capricorne
**En une phrase :** Tu révolutionnes le travail par la restructuration — ton efficacité vient quand tu transformes les organisations.

## Ton moteur
Uranus en Capricorne en Maison 6 te pousse vers des métiers de transformation organisationnelle. Tu excelles dans la restructuration, l'optimisation des systèmes, le changement managérial.

## Ton défi
Le piège : un travail trop stressant par excès de restructuration, des tensions avec les hiérarchies, confondre efficacité et contrôle. La vraie efficacité transformatrice inclut aussi la flexibilité.

## Maison 6 en Capricorne
Uranus secoue ton quotidien pour le restructurer. Tu travailles mieux quand tu peux améliorer les systèmes. Ta santé peut souffrir du stress professionnel mais bénéficie de discipline.

## Micro-rituel du jour (2 min)
- Identifier une amélioration structurelle dans ton travail quotidien
- Trois respirations en équilibrant ambition et bien-être
- Journal : « Comment puis-je transformer mon travail sans m'épuiser ? »""",

    ('capricorn', 7): """# ♅ Uranus en Capricorne
**En une phrase :** Tu révolutionnes les relations par la restructuration — tes partenariats transforment les conventions.

## Ton moteur
Uranus en Capricorne en Maison 7 crée des relations qui redéfinissent les structures relationnelles. Tu attires des partenaires ambitieux avec qui tu construis des projets durables.

## Ton défi
Le piège : des relations trop basées sur l'ambition, des tensions de pouvoir dans le couple, confondre partenariat et association d'affaires. Les meilleures relations ont aussi de la tendresse.

## Maison 7 en Capricorne
Uranus électrise tes partenariats de structure et d'ambition. Tu peux avoir des relations qui transforment ta position sociale. Tes contrats sont ambitieux et transformateurs.

## Micro-rituel du jour (2 min)
- Créer un moment de tendresse simple avec un partenaire
- Trois respirations en équilibrant ambition et intimité
- Journal : « Comment mes relations peuvent-elles être ambitieuses ET tendres ? »""",

    ('capricorn', 8): """# ♅ Uranus en Capricorne
**En une phrase :** Tu traverses les crises par la restructuration — les transformations deviennent des occasions de rebâtir plus solidement.

## Ton moteur
Uranus en Capricorne en Maison 8 te donne la capacité de traverser les crises en restructurant ce qui a été détruit. Tu ne subis pas les transformations — tu les utilises pour construire quelque chose de plus solide.

## Ton défi
Le piège : des crises qui menacent tes structures de sécurité, avoir du mal à lâcher prise sur le contrôle, confondre reconstruction et rigidité. La vraie transformation structurelle sait aussi s'adapter.

## Maison 8 en Capricorne
Uranus secoue ta relation aux crises pour les structurer. Les ressources partagées peuvent être liées à des restructurations. Ta sexualité peut être liée au pouvoir ou à l'ambition.

## Micro-rituel du jour (2 min)
- Identifier comment tu peux reconstruire après une transformation
- Trois respirations en faisant confiance au processus de restructuration
- Journal : « Quelle crise m'a permis de rebâtir plus solidement ? »""",

    ('capricorn', 9): """# ♅ Uranus en Capricorne
**En une phrase :** Tu révolutionnes la sagesse par la structure — ta philosophie est une architecture de pensée qui transforme.

## Ton moteur
Uranus en Capricorne en Maison 9 te pousse vers des croyances qui structurent le changement. Tu ne te satisfais pas des idées vagues — tu veux une philosophie qui peut être appliquée, testée, améliorée.

## Ton défi
Le piège : une vision trop rigide ou dogmatique, confondre structure et vérité, avoir du mal avec le mystère. La vraie sagesse structurelle inclut aussi l'inconnu.

## Maison 9 en Capricorne
Uranus électrise ta quête de sens de structure et d'ambition. Tu peux devenir une autorité dans ton domaine. Les voyages peuvent être liés à des projets professionnels.

## Micro-rituel du jour (2 min)
- Explorer une sagesse qui structure ta vision du changement
- Trois respirations en équilibrant structure et mystère
- Journal : « Quelle philosophie guide ma transformation du monde ? »""",

    ('capricorn', 10): """# ♅ Uranus en Capricorne
**En une phrase :** Tu révolutionnes ta carrière par la transformation des systèmes — ta réussite vient quand tu changes les structures de l'intérieur.

## Ton moteur
Uranus en Capricorne en Maison 10 amplifie au maximum ta capacité à transformer les organisations. Tu peux réussir en restructurant des entreprises, des institutions, des systèmes entiers.

## Ton défi
Le piège : des carrières marquées par des restructurations déstabilisantes, des conflits avec l'autorité, confondre pouvoir et influence. La vraie réussite transformatrice sert aussi le bien commun.

## Maison 10 en Capricorne
Uranus secoue au maximum ta réputation et ta carrière. On te reconnaît pour ta capacité à transformer les systèmes. Ta carrière peut connaître des retournements spectaculaires.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière peut mieux servir la transformation positive
- Trois respirations en alignant ambition et service
- Journal : « Quelle transformation systémique ma carrière peut-elle servir ? »""",

    ('capricorn', 11): """# ♅ Uranus en Capricorne
**En une phrase :** Tu révolutionnes l'action collective par la restructuration — tes amitiés et tes projets transforment les institutions.

## Ton moteur
Uranus en Capricorne en Maison 11 te connecte à des réseaux de transformateurs organisationnels. Tes amis sont des leaders de changement. Les projets collectifs visent à restructurer des systèmes.

## Ton défi
Le piège : des amitiés trop basées sur l'ambition, des luttes de pouvoir dans les groupes, confondre networking et amitié. Les meilleures communautés ont aussi de l'humanité.

## Maison 11 en Capricorne
Uranus électrise tes réseaux de transformation et d'ambition. Tu es fait pour les organisations de changement social, les associations professionnelles innovantes.

## Micro-rituel du jour (2 min)
- Partager un moment humain avec un ami au-delà de l'ambition
- Trois respirations en honorant l'humanité dans tes réseaux
- Journal : « Comment mes réseaux peuvent-ils être ambitieux ET humains ? »""",

    ('capricorn', 12): """# ♅ Uranus en Capricorne
**En une phrase :** Tu révolutionnes ta vie intérieure par la structure — ton inconscient te guide vers une maîtrise spirituelle.

## Ton moteur
Uranus en Capricorne en Maison 12 crée des connexions entre ta discipline et les dimensions invisibles. Ta pratique spirituelle peut être structurée et transformatrice. La méditation disciplinée te mène à des percées profondes.

## Ton défi
Le piège : contrôler la vie intérieure au lieu de l'accueillir, avoir du mal avec l'abandon spirituel, confondre maîtrise et éveil. La vraie spiritualité structurée sait aussi lâcher prise.

## Maison 12 en Capricorne
Uranus secoue ta connexion à l'invisible pour la structurer. Tu peux avoir une pratique spirituelle disciplinée et transformatrice. Les retraites silencieuses te conviennent.

## Micro-rituel du jour (2 min)
- Méditer en lâchant le contrôle tout en maintenant la discipline
- Trois respirations en équilibrant structure et abandon
- Journal : « Comment ma pratique spirituelle peut-elle être structurée ET libre ? »""",

    # AQUARIUS - 12 maisons
    ('aquarius', 1): """# ♅ Uranus en Verseau
**En une phrase :** Tu incarnes la révolution pure — ton identité est celle de l'innovateur, du visionnaire, du changeur de paradigmes.

## Ton moteur
Uranus en Verseau en Maison 1 amplifie au maximum ton originalité et ton besoin de liberté. Tu es naturellement en avance sur ton temps, tu vois ce que les autres ne voient pas encore.

## Ton défi
Le piège : te définir uniquement par ta différence, être provocateur pour le plaisir, avoir du mal à créer des liens. La vraie révolution connecte aussi.

## Maison 1 en Verseau
Uranus est chez lui et électrise ta personnalité de façon maximale. Tu projettes une image d'originalité radicale. Ton apparence peut être avant-gardiste ou changer de façon imprévisible.

## Micro-rituel du jour (2 min)
- Exprimer quelque chose de radicalement unique sur toi
- Trois respirations en assumant pleinement ta différence
- Journal : « Comment mon originalité sert-elle l'évolution collective ? »""",

    ('aquarius', 2): """# ♅ Uranus en Verseau
**En une phrase :** Tu révolutionnes ta prospérité par l'innovation — tes ressources viennent de ta capacité à voir le futur.

## Ton moteur
Uranus en Verseau en Maison 2 crée des revenus par l'innovation radicale, la technologie, les idées de pointe. Tu peux prospérer en étant le premier à voir et à créer l'avenir.

## Ton défi
Le piège : des finances qui fluctuent avec tes expérimentations, avoir du mal avec la stabilité, confondre originalité et valeur. La vraie prospérité innovante est aussi durable.

## Maison 2 en Verseau
Uranus secoue tes finances pour les libérer des conventions. Tu peux gagner de l'argent de façons radicalement nouvelles. Tes valeurs sont liées à la liberté et au collectif.

## Micro-rituel du jour (2 min)
- Identifier une innovation qui pourrait devenir une source de valeur
- Trois respirations en connectant originalité et prospérité
- Journal : « Comment mon regard sur le futur peut-il créer de l'abondance ? »""",

    ('aquarius', 3): """# ♅ Uranus en Verseau
**En une phrase :** Tu communiques des idées révolutionnaires — tes mots sont des graines de futur.

## Ton moteur
Uranus en Verseau en Maison 3 amplifie ta capacité à penser et communiquer de façon innovante. Tu es un canal pour les idées du futur, un transmetteur de nouvelles possibilités.

## Ton défi
Le piège : une communication trop abstraite ou futuriste, avoir du mal à être compris, confondre originalité et pertinence. La vraie communication révolutionnaire est aussi accessible.

## Maison 3 en Verseau
Uranus électrise au maximum tes échanges d'innovation et de vision. Tes relations sont basées sur l'échange d'idées nouvelles. Tu apprends par l'expérimentation radicale.

## Micro-rituel du jour (2 min)
- Partager une idée révolutionnaire de façon accessible
- Trois respirations en servant de pont vers le futur
- Journal : « Comment puis-je mieux communiquer mes visions ? »""",

    ('aquarius', 4): """# ♅ Uranus en Verseau
**En une phrase :** Tu révolutionnes la famille par la liberté — ton foyer est un laboratoire de nouvelles façons de vivre ensemble.

## Ton moteur
Uranus en Verseau en Maison 4 crée un environnement familial radicalement non conventionnel. Tu peux expérimenter des formes de vie commune, d'habitat partagé, de famille choisie.

## Ton défi
Le piège : avoir du mal à créer des racines par excès de liberté, un foyer chaotique, confondre innovation et instabilité. La vraie liberté familiale crée aussi de la sécurité.

## Maison 4 en Verseau
Uranus secoue tes fondations pour les libérer. Tu as peut-être grandi dans une famille atypique ou tu crées la tienne de façon radicalement originale.

## Micro-rituel du jour (2 min)
- Identifier un aspect révolutionnaire de ta vie familiale qui fonctionne
- Trois respirations en ancrant la liberté dans l'appartenance
- Journal : « Comment mon foyer peut-il être libre ET sécurisant ? »""",

    ('aquarius', 5): """# ♅ Uranus en Verseau
**En une phrase :** Tu crées avec une liberté radicale — tes œuvres et tes amours brisent tous les moules.

## Ton moteur
Uranus en Verseau en Maison 5 te pousse vers une créativité qui défie toutes les conventions. Tu ne crées pas selon les règles — tu inventes les tiennes. En amour, tu cherches des partenaires qui comprennent ton besoin absolu de liberté.

## Ton défi
Le piège : des relations instables par peur de tout engagement, une créativité qui choque sans créer, confondre liberté et inconstance. La vraie joie créative sait aussi s'approfondir.

## Maison 5 en Verseau
Uranus électrise au maximum tes plaisirs et ta créativité. Tu peux avoir des relations non conventionnelles. Tes œuvres sont avant-gardistes et expérimentales.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif radicalement original
- Trois respirations en laissant ta créativité être totalement libre
- Journal : « Quelle création brise les conventions de façon joyeuse ? »""",

    ('aquarius', 6): """# ♅ Uranus en Verseau
**En une phrase :** Tu révolutionnes le travail par l'innovation radicale — ton efficacité vient quand tu peux réinventer les méthodes.

## Ton moteur
Uranus en Verseau en Maison 6 te pousse à transformer radicalement les façons de travailler. Tu excelles dans les environnements qui encouragent l'innovation totale.

## Ton défi
Le piège : avoir du mal avec toute forme de routine, résister aux structures même utiles, confondre innovation et désorganisation. La vraie efficacité innovante a aussi des repères.

## Maison 6 en Verseau
Uranus secoue ton quotidien pour le révolutionner. Tu travailles mieux avec une autonomie totale. Ta santé peut bénéficier de technologies ou d'approches de pointe.

## Micro-rituel du jour (2 min)
- Identifier une routine que tu pourrais révolutionner de façon utile
- Trois respirations en trouvant l'équilibre entre innovation et structure
- Journal : « Quelle innovation pourrait vraiment améliorer mon quotidien ? »""",

    ('aquarius', 7): """# ♅ Uranus en Verseau
**En une phrase :** Tu révolutionnes les relations — tes partenariats redéfinissent ce que signifie être ensemble.

## Ton moteur
Uranus en Verseau en Maison 7 crée des relations qui défient toutes les conventions. Tu attires des partenaires aussi originaux que toi, avec qui tu inventes de nouvelles formes d'union.

## Ton défi
Le piège : fuir tout engagement par idéalisation de la liberté, des relations qui manquent de profondeur, confondre distance et indépendance. Les meilleures relations sont libres ET profondes.

## Maison 7 en Verseau
Uranus électrise au maximum tes partenariats. Tu peux vivre des formes de relations radicalement nouvelles. Tes contrats sont innovants et flexibles.

## Micro-rituel du jour (2 min)
- Créer un moment de connexion profonde avec un partenaire
- Trois respirations en équilibrant liberté et intimité
- Journal : « Comment mes relations peuvent-elles être à la fois libres et profondes ? »""",

    ('aquarius', 8): """# ♅ Uranus en Verseau
**En une phrase :** Tu traverses les crises comme des éveils — les transformations libèrent ta conscience.

## Ton moteur
Uranus en Verseau en Maison 8 transforme les crises en occasions d'éveil et de libération. Tu vois les transformations comme des opportunités de te détacher de ce qui te limite.

## Ton défi
Le piège : te détacher émotionnellement au lieu de traverser les crises, intellectualiser les transformations, confondre détachement et éveil. La vraie libération inclut aussi le cœur.

## Maison 8 en Verseau
Uranus secoue ta relation aux transformations pour les éclairer. Ta sexualité peut être expérimentale ou liée à la libération. Les ressources partagées peuvent venir de projets innovants.

## Micro-rituel du jour (2 min)
- Identifier ce qu'une crise t'a permis de libérer
- Trois respirations en accueillant la transformation comme éveil
- Journal : « Quelle conscience nouvelle émerge de mes crises ? »""",

    ('aquarius', 9): """# ♅ Uranus en Verseau
**En une phrase :** Tu révolutionnes la sagesse — ta philosophie est une vision du futur de l'humanité.

## Ton moteur
Uranus en Verseau en Maison 9 te pousse vers des croyances qui anticipent l'évolution de l'humanité. Tu ne te satisfais pas des philosophies du passé — tu cherches celles du futur.

## Ton défi
Le piège : des croyances trop excentriques pour être partagées, rejeter toute tradition, confondre nouveauté et vérité. La vraie sagesse révolutionnaire intègre aussi le passé.

## Maison 9 en Verseau
Uranus électrise au maximum ta quête de sens. Tu es attiré par les philosophies futuristes, les sciences de pointe, les spiritualités innovantes.

## Micro-rituel du jour (2 min)
- Explorer une vision du futur qui t'inspire
- Trois respirations en intégrant passé, présent et futur
- Journal : « Quelle philosophie du futur me guide ? »""",

    ('aquarius', 10): """# ♅ Uranus en Verseau
**En une phrase :** Tu révolutionnes ta carrière par le changement de paradigme — ta réussite vient quand tu changes les règles du jeu.

## Ton moteur
Uranus en Verseau en Maison 10 te pousse vers une carrière qui change les paradigmes. Tu ne réussis pas dans le système — tu crées de nouveaux systèmes.

## Ton défi
Le piège : une carrière trop en avance pour être reconnue, des conflits avec toutes les autorités, confondre provocation et innovation. Le vrai changement de paradigme sait aussi créer des alliances.

## Maison 10 en Verseau
Uranus secoue ta réputation pour la rendre radicalement originale. On te reconnaît pour ta capacité à penser et faire différemment.

## Micro-rituel du jour (2 min)
- Identifier quel paradigme ta carrière peut contribuer à changer
- Trois respirations en assumant ton rôle de changeur de règles
- Journal : « Quel nouveau paradigme ma carrière peut-elle créer ? »""",

    ('aquarius', 11): """# ♅ Uranus en Verseau
**En une phrase :** Tu révolutionnes l'action collective — tes amitiés et tes projets créent le futur.

## Ton moteur
Uranus en Verseau en Maison 11 est la position la plus puissante pour l'innovation collective. Tu es fait pour les mouvements qui changent le monde, les communautés de pionniers, les projets de rupture.

## Ton défi
Le piège : préférer les idéaux aux personnes réelles, des amitiés trop détachées, imposer ta vision au groupe. Les meilleures communautés honorent aussi l'humanité.

## Maison 11 en Verseau
Uranus est au maximum de sa puissance dans les réseaux et les projets collectifs. Tu attires des visionnaires et des innovateurs. Tes projets ont un impact à large échelle.

## Micro-rituel du jour (2 min)
- Partager une vision de changement avec ton réseau
- Trois respirations en honorant la force du collectif visionnaire
- Journal : « Quel futur mon réseau peut-il créer ensemble ? »""",

    ('aquarius', 12): """# ♅ Uranus en Verseau
**En une phrase :** Tu révolutionnes ta vie intérieure — ton inconscient est connecté à la conscience collective de l'humanité.

## Ton moteur
Uranus en Verseau en Maison 12 crée des connexions profondes entre ton inconscient et l'évolution collective. Tu peux percevoir les courants du futur, avoir des intuitions sur l'humanité à venir.

## Ton défi
Le piège : se perdre dans des visions abstraites, fuir l'intimité personnelle dans les grandes causes, confondre détachement et spiritualité. La vraie conscience collective inclut aussi le cœur personnel.

## Maison 12 en Verseau
Uranus secoue ta connexion à l'invisible pour l'élargir à l'humanité. Tu peux avoir des visions qui concernent le collectif. Les pratiques en groupe ou connectées au cosmos te conviennent.

## Micro-rituel du jour (2 min)
- Méditer sur ta connexion à l'humanité
- Trois respirations en t'ouvrant à la conscience collective
- Journal : « Quel message pour l'humanité émerge de mon intériorité ? »""",

    # PISCES - 12 maisons
    ('pisces', 1): """# ♅ Uranus en Poissons
**En une phrase :** Tu incarnes une révolution spirituelle — ton identité dissout les frontières entre visible et invisible.

## Ton moteur
Uranus en Poissons en Maison 1 te donne une personnalité profondément intuitive et connectée aux dimensions invisibles. Tu absorbes les énergies ambiantes et tu les transformes.

## Ton défi
Le piège : une identité floue qui se perd dans les autres, être submergé par les émotions ambiantes, confondre dissolution et éveil. La vraie révolution spirituelle a aussi des limites.

## Maison 1 en Poissons
Uranus électrise ta sensibilité et ta connexion à l'invisible. Tu projettes une image de mystère et de profondeur. Ton apparence peut refléter tes états intérieurs changeants.

## Micro-rituel du jour (2 min)
- Identifier comment ta sensibilité te sert de façon unique
- Trois respirations en protégeant ton énergie
- Journal : « Comment ma connexion à l'invisible me distingue-t-elle ? »""",

    ('pisces', 2): """# ♅ Uranus en Poissons
**En une phrase :** Tu révolutionnes ta prospérité par l'intuition — tes ressources viennent de sources invisibles et mystérieuses.

## Ton moteur
Uranus en Poissons en Maison 2 crée des revenus par l'intuition, la créativité spirituelle, les arts. Tu peux recevoir de façon inattendue, attirer l'abondance par la foi.

## Ton défi
Le piège : une relation floue à l'argent, être trop généreux au détriment de toi-même, confondre abondance spirituelle et matérielle. La vraie prospérité intuitive a aussi des bases concrètes.

## Maison 2 en Poissons
Uranus secoue tes finances pour les rendre plus fluides. Tu peux gagner de l'argent par des talents artistiques ou spirituels. Tes valeurs sont liées à la compassion et à la foi.

## Micro-rituel du jour (2 min)
- Identifier une ressource qui t'est venue de façon intuitive
- Trois respirations en faisant confiance à l'abondance invisible
- Journal : « Comment mon intuition peut-elle me guider vers la prospérité ? »""",

    ('pisces', 3): """# ♅ Uranus en Poissons
**En une phrase :** Tu communiques avec l'invisible — tes mots touchent les dimensions qui échappent à la raison.

## Ton moteur
Uranus en Poissons en Maison 3 te donne une communication intuitive et poétique. Tu perçois ce qui n'est pas dit, tu exprimes ce qui échappe aux mots.

## Ton défi
Le piège : une communication trop vague ou confuse, avoir du mal à être factuel, se perdre dans les impressions. La vraie communication intuitive sait aussi être claire.

## Maison 3 en Poissons
Uranus électrise tes échanges d'intuition et de subtilité. Tu peux avoir des liens psychiques avec ton entourage. L'écriture poétique ou intuitive est une voie.

## Micro-rituel du jour (2 min)
- Exprimer quelque chose d'intuitif de façon claire
- Trois respirations en donnant forme à l'invisible
- Journal : « Comment puis-je mieux communiquer mes perceptions subtiles ? »""",

    ('pisces', 4): """# ♅ Uranus en Poissons
**En une phrase :** Tu révolutionnes la famille par la compassion — ton foyer devient un refuge spirituel.

## Ton moteur
Uranus en Poissons en Maison 4 crée un environnement familial profondément spirituel et compassionnel. Ton foyer peut être un lieu de guérison, de méditation, d'accueil inconditionnel.

## Ton défi
Le piège : absorber les problèmes de ta famille, avoir du mal à créer des limites chez toi, fuir les difficultés domestiques. Le vrai refuge a aussi des protections.

## Maison 4 en Poissons
Uranus secoue ta vie familiale pour l'ouvrir à la compassion. Tu as peut-être grandi dans une famille sensible ou mystique. Ton foyer peut inclure une dimension spirituelle.

## Micro-rituel du jour (2 min)
- Créer un moment de paix spirituelle chez toi
- Trois respirations en faisant de ton foyer un sanctuaire protégé
- Journal : « Comment mon chez-moi peut-il être un refuge qui me protège aussi ? »""",

    ('pisces', 5): """# ♅ Uranus en Poissons
**En une phrase :** Tu crées avec l'âme — tes œuvres et tes amours sont des expériences de transcendance.

## Ton moteur
Uranus en Poissons en Maison 5 te pousse vers une créativité qui touche au transcendant. Tu ne crées pas avec ta tête mais avec ton âme. En amour, tu cherches des connexions qui dépassent l'ordinaire.

## Ton défi
Le piège : idéaliser les partenaires, une créativité qui reste dans les rêves, confondre inspiration et réalisation. La vraie joie créative s'incarne aussi.

## Maison 5 en Poissons
Uranus électrise tes plaisirs de spiritualité et de transcendance. Tu peux avoir des amours qui te connectent à quelque chose de plus grand. Ta créativité est intuitive et mystique.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui nourrit ton âme
- Trois respirations en incarnant ta créativité spirituelle
- Journal : « Quelle création de l'âme me ferait vraiment vibrer ? »""",

    ('pisces', 6): """# ♅ Uranus en Poissons
**En une phrase :** Tu révolutionnes le soin — ton travail guérit les dimensions invisibles de la souffrance.

## Ton moteur
Uranus en Poissons en Maison 6 te pousse vers des métiers de guérison holistique. Tu ne traites pas les symptômes — tu touches les causes invisibles. Les thérapies alternatives, l'art-thérapie, les soins énergétiques sont tes voies.

## Ton défi
Le piège : absorber la souffrance des autres, négliger ta propre santé, confondre service et sacrifice. Le vrai soin durable inclut ta propre protection.

## Maison 6 en Poissons
Uranus secoue ton quotidien pour le rendre plus compassionnel. Tu travailles mieux dans des environnements bienveillants. Ta santé est sensible aux énergies et bénéficie d'approches holistiques.

## Micro-rituel du jour (2 min)
- Prendre soin de toi avant de prendre soin des autres
- Trois respirations en protégeant ton énergie de guérisseur
- Journal : « Comment puis-je soigner tout en me préservant ? »""",

    ('pisces', 7): """# ♅ Uranus en Poissons
**En une phrase :** Tu révolutionnes les relations par la fusion spirituelle — tes partenariats sont des connexions d'âmes.

## Ton moteur
Uranus en Poissons en Maison 7 crée des relations qui transcendent l'ordinaire. Tu attires des partenaires avec qui tu partages des liens d'âmes, des connexions qui dépassent cette vie.

## Ton défi
Le piège : te perdre dans l'autre, des relations qui manquent de limites, confondre fusion et amour. Les meilleures relations d'âmes gardent aussi deux individus distincts.

## Maison 7 en Poissons
Uranus électrise tes partenariats de profondeur spirituelle. Tu peux avoir des relations karmiques ou des connexions mystiques. Tes contrats bénéficient de ton intuition.

## Micro-rituel du jour (2 min)
- Créer une limite saine dans une relation profonde
- Trois respirations en maintenant ton centre dans la connexion
- Journal : « Comment mes relations d'âmes peuvent-elles rester saines ? »""",

    ('pisces', 8): """# ♅ Uranus en Poissons
**En une phrase :** Tu traverses les crises comme des dissolutions — les transformations te reconnectent à l'océan de la conscience.

## Ton moteur
Uranus en Poissons en Maison 8 transforme les crises en expériences de dissolution et de renaissance spirituelle. Tu lâches prise plus facilement que d'autres, tu te fonds dans le processus de transformation.

## Ton défi
Le piège : te dissoudre dans les crises au lieu de les traverser, fuir la réalité des pertes, avoir du mal à agir. La vraie transformation spirituelle inclut aussi l'action.

## Maison 8 en Poissons
Uranus secoue ta relation aux mystères pour l'approfondir. Tu peux avoir des expériences de mort et renaissance spirituelle. Ta sexualité peut être transcendante.

## Micro-rituel du jour (2 min)
- Identifier une action concrète pour traverser une transformation
- Trois respirations en alliant dissolution et incarnation
- Journal : « Comment puis-je traverser les crises avec foi ET action ? »""",

    ('pisces', 9): """# ♅ Uranus en Poissons
**En une phrase :** Tu révolutionnes la spiritualité — ta quête de sens est une immersion dans les mystères ultimes.

## Ton moteur
Uranus en Poissons en Maison 9 amplifie au maximum ta connexion aux dimensions spirituelles. Tu ne te satisfais pas des croyances ordinaires — tu veux l'expérience directe du divin.

## Ton défi
Le piège : te perdre dans des croyances floues, fuir la réalité dans la spiritualité, confondre rêverie et éveil. La vraie sagesse spirituelle s'incarne aussi.

## Maison 9 en Poissons
Uranus électrise au maximum ta quête spirituelle. Tu peux avoir des expériences mystiques profondes, des visions, des voyages intérieurs transformateurs.

## Micro-rituel du jour (2 min)
- Méditer sur ta connexion au divin
- Trois respirations en ancrant le transcendant dans ta vie
- Journal : « Comment ma spiritualité peut-elle s'incarner davantage ? »""",

    ('pisces', 10): """# ♅ Uranus en Poissons
**En une phrase :** Tu révolutionnes ta carrière par le service spirituel — ta réussite vient quand tu touches les âmes.

## Ton moteur
Uranus en Poissons en Maison 10 te pousse vers une carrière qui sert la guérison spirituelle du monde. Tu ne cherches pas la gloire — tu cherches l'impact sur les âmes.

## Ton défi
Le piège : une carrière floue par manque de structure, te sacrifier professionnellement, confondre vocation et exploitation. La vraie réussite spirituelle est aussi valorisée.

## Maison 10 en Poissons
Uranus secoue ta réputation pour la rendre plus spirituelle. On te reconnaît pour ta compassion et ta connexion à l'invisible. Ta carrière peut être dans les arts, le soin, la spiritualité.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière touche les âmes
- Trois respirations en alignant service et reconnaissance
- Journal : « Comment ma vocation peut-elle être à la fois spirituelle et reconnue ? »""",

    ('pisces', 11): """# ♅ Uranus en Poissons
**En une phrase :** Tu révolutionnes l'action collective par la compassion — tes amitiés et tes projets sont des cercles d'âmes.

## Ton moteur
Uranus en Poissons en Maison 11 te connecte à des réseaux de personnes sensibles et spirituelles. Tes amis sont des âmes sœurs. Les projets collectifs ont une dimension de guérison universelle.

## Ton défi
Le piège : te perdre dans les besoins du groupe, des amitiés qui manquent de limites, absorber les souffrances collectives. Les meilleures communautés protègent aussi leurs membres.

## Maison 11 en Poissons
Uranus électrise tes réseaux de spiritualité et de compassion. Tu es fait pour les cercles de méditation, les communautés de guérison, les projets humanitaires spirituels.

## Micro-rituel du jour (2 min)
- Partager un moment de connexion spirituelle avec un groupe
- Trois respirations en protégeant ton énergie dans le collectif
- Journal : « Comment mon cercle d'âmes peut-il me nourrir aussi ? »""",

    ('pisces', 12): """# ♅ Uranus en Poissons
**En une phrase :** Tu habites l'océan de la conscience — ta vie intérieure est une immersion dans l'infini.

## Ton moteur
Uranus en Poissons en Maison 12 est la position de connexion maximale à l'invisible. Tu as un accès naturel aux dimensions spirituelles, aux rêves prophétiques, à la conscience universelle.

## Ton défi
Le piège : te perdre dans l'infini, avoir du mal avec la vie concrète, confondre dissolution et éveil. La vraie transcendance inclut aussi le retour à la réalité.

## Maison 12 en Poissons
Uranus amplifie au maximum ta connexion au mystère. Tu peux avoir des expériences spirituelles profondes et transformatrices. Les retraites de méditation profonde sont ta voie.

## Micro-rituel du jour (2 min)
- Méditer en t'ouvrant à l'océan de la conscience
- Trois respirations en revenant doucement à la réalité
- Journal : « Comment puis-je naviguer l'infini tout en restant ancré ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in URANUS_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'uranus',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP uranus/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='uranus',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT uranus/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
