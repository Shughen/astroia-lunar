#!/usr/bin/env python3
"""Script d'insertion des interprétations Saturn/Aries et Saturn/Taurus en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

SATURN_INTERPRETATIONS = {
    # ARIES
    ('aries', 1): """# ♄ Saturne en Bélier
**En une phrase :** Tu apprends à affirmer ton identité avec discipline — l'impulsivité se transforme en force maîtrisée.

## Ton moteur
Saturne en Bélier en Maison 1 te confronte au défi de l'affirmation de soi. Tu peux ressentir une retenue ou une inhibition dans ton élan vital. Mais cette configuration, une fois travaillée, te donne une autorité naturelle et une force de caractère exceptionnelle.

## Ton défi
Le piège : te retenir d'agir par peur de l'échec, confondre prudence et paralysie, retourner ta colère contre toi-même. Le travail de Saturne est d'apprendre à agir avec maturité, pas à s'empêcher d'agir.

## Maison 1 en Bélier
Saturne structure ton expression personnelle. Tu peux paraître plus réservé que tu ne l'es vraiment. Avec le temps, tu développes une présence de leader mature et respecté.

## Micro-rituel du jour (2 min)
- Identifier une action que tu repousses par peur et faire un premier pas
- Trois respirations en te connectant à ta force intérieure
- Journal : « Quelle peur surmontée m'a récemment rendu plus fort ? »""",

    ('aries', 2): """# ♄ Saturne en Bélier
**En une phrase :** Tu construis ta sécurité financière par des initiatives courageuses mais réfléchies — l'audace devient stratégie.

## Ton moteur
Saturne en Bélier en Maison 2 te demande de développer ta confiance en tes capacités de gagner par toi-même. Tu peux avoir des blocages autour de la prise de risque financière. Le travail de Saturne est d'apprendre à oser avec sagesse.

## Ton défi
Le piège : être trop prudent financièrement par manque de confiance, te bloquer dans l'inaction, ou à l'inverse prendre des risques inconsidérés pour prouver quelque chose. L'équilibre se trouve dans l'action réfléchie.

## Maison 2 en Bélier
Saturne structure ton rapport à l'argent et aux valeurs. Tu apprends à valoriser ton indépendance financière. Tes ressources augmentent quand tu oses prendre des initiatives calculées.

## Micro-rituel du jour (2 min)
- Identifier une initiative financière que tu repousses et noter un premier pas
- Trois respirations en renforçant ta confiance en tes capacités
- Journal : « Quelle action courageuse a amélioré ma situation matérielle ? »""",

    ('aries', 3): """# ♄ Saturne en Bélier
**En une phrase :** Tu apprends à communiquer avec force et précision — les mots deviennent des actes de courage réfléchi.

## Ton moteur
Saturne en Bélier en Maison 3 te confronte à l'affirmation de tes idées. Tu peux avoir du mal à prendre la parole avec assurance ou à défendre tes opinions. Le travail de Saturne est de développer une communication qui combine audace et réflexion.

## Ton défi
Le piège : te taire quand tu devrais parler, communiquer de façon trop agressive par frustration accumulée, ou te sentir incompris. L'équilibre se trouve dans l'expression mesurée mais directe.

## Maison 3 en Bélier
Saturne structure tes apprentissages et ta communication. Tu apprends lentement mais profondément. Avec le temps, ta parole gagne en autorité et en impact.

## Micro-rituel du jour (2 min)
- Exprimer une opinion que tu gardais pour toi, de façon claire et calme
- Trois respirations en préparant ta voix à être entendue
- Journal : « Quelle idée ai-je osé exprimer récemment malgré ma réserve ? »""",

    ('aries', 4): """# ♄ Saturne en Bélier
**En une phrase :** Tu construis un foyer qui te donne la force d'affronter le monde — les racines deviennent un tremplin.

## Ton moteur
Saturne en Bélier en Maison 4 te demande de bâtir ta sécurité intérieure par toi-même. Tu as peut-être grandi avec le sentiment de devoir te battre pour ta place dans la famille. Le travail de Saturne est de créer ton propre territoire sûr.

## Ton défi
Le piège : confondre le foyer avec un champ de bataille, avoir du mal à te sentir en sécurité chez toi, couper les liens familiaux par besoin d'indépendance. L'équilibre se trouve dans un foyer qui soutient ton élan sans t'étouffer.

## Maison 4 en Bélier
Saturne structure ta vie privée et familiale. Tu apprends à créer un chez-toi qui respecte ton besoin d'autonomie. Avec le temps, tu deviens le pilier de ta propre famille.

## Micro-rituel du jour (2 min)
- Faire quelque chose qui renforce ton sentiment de sécurité chez toi
- Trois respirations en te connectant à tes racines comme source de force
- Journal : « Comment mon foyer soutient-il mon courage d'affronter le monde ? »""",

    ('aries', 5): """# ♄ Saturne en Bélier
**En une phrase :** Tu apprends à créer et à aimer avec maturité — la passion se canalise en expression durable.

## Ton moteur
Saturne en Bélier en Maison 5 te confronte à tes inhibitions dans la créativité et l'amour. Tu peux avoir du mal à te lâcher dans le plaisir ou à exprimer ta flamme. Le travail de Saturne est d'apprendre à jouer sérieusement.

## Ton défi
Le piège : bloquer ta créativité par peur du jugement, avoir des difficultés dans les relations amoureuses par pudeur ou retenue, prendre les plaisirs trop au sérieux. L'équilibre se trouve dans une joie disciplinée mais libre.

## Maison 5 en Bélier
Saturne structure ton expression créative et tes amours. Les plaisirs mûrissent avec le temps. Tu développes une créativité qui a du caractère et des relations amoureuses profondes.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir ou un moment créatif malgré ta tendance à te retenir
- Trois respirations en autorisant la joie à exister
- Journal : « Comment puis-je m'autoriser plus de légèreté dans mes plaisirs ? »""",

    ('aries', 6): """# ♄ Saturne en Bélier
**En une phrase :** Tu travailles avec une discipline de guerrier — l'effort quotidien forge ta force et ta résilience.

## Ton moteur
Saturne en Bélier en Maison 6 te demande de canaliser ton énergie dans un travail structuré. Tu peux osciller entre hyperactivité et épuisement. Le travail de Saturne est d'apprendre un rythme d'effort soutenable.

## Ton défi
Le piège : t'épuiser en voulant tout faire trop vite, frustration face aux routines, problèmes de santé liés à l'inflammation ou au surmenage. L'équilibre se trouve dans l'effort mesuré et constant.

## Maison 6 en Bélier
Saturne structure ton quotidien et ta santé. Tu apprends à canaliser ton énergie au lieu de la disperser. Avec le temps, tu développes une efficacité remarquable et une santé robuste.

## Micro-rituel du jour (2 min)
- Identifier une tâche que tu peux accomplir de façon constante plutôt qu'intense
- Trois respirations en acceptant un rythme soutenable
- Journal : « Comment puis-je être efficace sans m'épuiser ? »""",

    ('aries', 7): """# ♄ Saturne en Bélier
**En une phrase :** Tu apprends les partenariats par l'équilibre entre indépendance et engagement — le couple devient école de maturité.

## Ton moteur
Saturne en Bélier en Maison 7 te confronte au défi de l'équilibre dans les relations. Tu peux attirer des partenaires qui testent ton indépendance ou te sentir limité par l'engagement. Le travail de Saturne est d'apprendre à être toi-même dans le couple.

## Ton défi
Le piège : fuir l'engagement par peur de perdre ton autonomie, ou attirer des partenaires dominants qui te frustrent. L'équilibre se trouve dans des relations qui respectent les deux individualités.

## Maison 7 en Bélier
Saturne structure tes partenariats. Les relations mûrissent avec le temps. Tu apprends à trouver des partenaires qui valorisent ton indépendance et te permettent de grandir.

## Micro-rituel du jour (2 min)
- Identifier un équilibre à trouver entre ton besoin d'autonomie et de connexion
- Trois respirations en acceptant la danse entre indépendance et intimité
- Journal : « Comment mes relations m'apprennent-elles à être plus mature ? »""",

    ('aries', 8): """# ♄ Saturne en Bélier
**En une phrase :** Tu traverses les transformations avec courage discipliné — les crises deviennent des épreuves qui forgent ta force.

## Ton moteur
Saturne en Bélier en Maison 8 te demande de faire face aux profondeurs avec courage. Tu peux résister aux transformations nécessaires par peur de perdre le contrôle. Le travail de Saturne est d'apprendre à se transformer avec maturité.

## Ton défi
Le piège : bloquer les processus de transformation par peur, retenir ta puissance par crainte de faire mal, ou affronter les crises de façon trop brutale. L'équilibre se trouve dans le courage mesuré.

## Maison 8 en Bélier
Saturne structure ton rapport aux crises et aux ressources partagées. Tu apprends à naviguer les transformations avec force et sagesse. Les héritages ou investissements demandent de la prudence.

## Micro-rituel du jour (2 min)
- Identifier une peur profonde et faire un petit pas courageux vers elle
- Trois respirations en acceptant le processus de transformation
- Journal : « Quelle transformation ai-je traversée avec plus de maturité récemment ? »""",

    ('aries', 9): """# ♄ Saturne en Bélier
**En une phrase :** Tu forges ta philosophie par l'expérience directe — les croyances se gagnent au combat avec le réel.

## Ton moteur
Saturne en Bélier en Maison 9 te demande de construire ta vision du monde par toi-même. Tu peux avoir du mal à adhérer aux systèmes de croyances établis. Le travail de Saturne est de forger une philosophie personnelle solide.

## Ton défi
Le piège : rejeter toutes les traditions par besoin d'indépendance, avoir du mal à t'engager dans des études longues, ou être trop rigide dans tes convictions. L'équilibre se trouve dans une ouverture disciplinée.

## Maison 9 en Bélier
Saturne structure ta quête de sens. Tu apprends à travers l'expérience directe plutôt que les livres. Avec le temps, tu développes une sagesse basée sur tes propres explorations.

## Micro-rituel du jour (2 min)
- Identifier une croyance que tu as forgée par l'expérience et la reconnaître
- Trois respirations en honorant ton propre chemin de sagesse
- Journal : « Quelle conviction personnelle s'est renforcée récemment ? »""",

    ('aries', 10): """# ♄ Saturne en Bélier
**En une phrase :** Tu construis ta carrière en leader solitaire — l'ambition se réalise par l'initiative maîtrisée.

## Ton moteur
Saturne en Bélier en Maison 10 te demande de créer ta propre voie professionnelle. Tu peux ressentir des blocages dans l'affirmation de tes ambitions. Le travail de Saturne est d'apprendre à diriger avec maturité et courage.

## Ton défi
Le piège : te retenir de prendre des initiatives par peur de l'échec, frustration face aux hiérarchies, ou imposer ton autorité de façon trop abrupte. L'équilibre se trouve dans un leadership mesuré mais audacieux.

## Maison 10 en Bélier
Saturne structure ta carrière et ta réputation. Le succès vient avec le temps et la persévérance. Tu es destiné à des positions de leadership où tu peux exprimer ton indépendance.

## Micro-rituel du jour (2 min)
- Identifier une initiative professionnelle à prendre malgré les résistances
- Trois respirations en renforçant ta confiance en ton leadership
- Journal : « Comment puis-je avancer dans ma carrière avec plus d'audace maîtrisée ? »""",

    ('aries', 11): """# ♄ Saturne en Bélier
**En une phrase :** Tu construis des amitiés et des projets par l'action concrète — les idéaux deviennent des réalisations.

## Ton moteur
Saturne en Bélier en Maison 11 te demande de contribuer aux groupes de façon active et responsable. Tu peux avoir du mal à trouver ta place dans les collectifs ou te sentir frustré par l'inaction des autres. Le travail de Saturne est de devenir un moteur pour les causes qui te tiennent à cœur.

## Ton défi
Le piège : vouloir tout faire seul dans les projets collectifs, avoir des amitiés difficiles par excès d'indépendance, ou te décourager face à la lenteur des changements sociaux. L'équilibre se trouve dans la patience active.

## Maison 11 en Bélier
Saturne structure tes amitiés et tes projets collectifs. Tu apprends à créer des alliances durables basées sur l'action concrète. Avec le temps, tu deviens un leader dans les causes que tu défends.

## Micro-rituel du jour (2 min)
- Identifier une contribution concrète que tu peux apporter à un groupe ou une cause
- Trois respirations en acceptant le rythme du changement collectif
- Journal : « Comment mon action individuelle peut-elle servir un projet collectif ? »""",

    ('aries', 12): """# ♄ Saturne en Bélier
**En une phrase :** Tu affrontes tes peurs avec discipline — l'inconscient devient un terrain de courage intérieur.

## Ton moteur
Saturne en Bélier en Maison 12 te confronte à tes limitations cachées et à tes peurs profondes autour de l'affirmation de soi. Tu peux saboter inconsciemment tes initiatives. Le travail de Saturne est de libérer la force retenue dans l'ombre.

## Ton défi
Le piège : te sentir bloqué sans comprendre pourquoi, retourner ton énergie contre toi-même, ou fuir dans l'isolement plutôt que d'affronter tes peurs. L'équilibre se trouve dans l'exploration courageuse de l'inconscient.

## Maison 12 en Bélier
Saturne structure ton monde intérieur. Tu apprends à faire face à tes démons avec méthode. Avec le temps, tu libères une force intérieure considérable.

## Micro-rituel du jour (2 min)
- Identifier une peur cachée qui limite ton action et la regarder en face
- Trois respirations en accueillant ce qui est refoulé
- Journal : « Quelle peur inconsciente ai-je commencé à apprivoiser ? »""",

    # TAURUS
    ('taurus', 1): """# ♄ Saturne en Taureau
**En une phrase :** Tu construis une présence stable et durable — la patience devient ta plus grande force.

## Ton moteur
Saturne en Taureau en Maison 1 te demande de développer une confiance solide en toi-même et en tes ressources. Tu peux te sentir limité dans l'expression de ta valeur personnelle. Le travail de Saturne est de construire une estime de soi inébranlable.

## Ton défi
Le piège : douter de ta valeur, te montrer trop rigide ou inflexible, accumuler par peur de manquer. L'équilibre se trouve dans une confiance patiente en toi-même.

## Maison 1 en Taureau
Saturne structure ton image de toi. Tu apprends à t'apprécier pour ce que tu es vraiment. Avec le temps, ta présence inspire la fiabilité et le respect.

## Micro-rituel du jour (2 min)
- Identifier une qualité durable en toi et la reconnaître
- Trois respirations en te connectant à ta valeur intrinsèque
- Journal : « Quelle force stable en moi mérite d'être célébrée ? »""",

    ('taurus', 2): """# ♄ Saturne en Taureau
**En une phrase :** Tu bâtis ta sécurité financière pierre par pierre — la prudence devient prospérité durable.

## Ton moteur
Saturne en Taureau en Maison 2 te confronte à tes peurs autour de l'argent et de la sécurité matérielle. Tu peux avoir vécu des restrictions ou développer une relation anxieuse avec les finances. Le travail de Saturne est de construire une vraie sécurité par l'effort patient.

## Ton défi
Le piège : être trop avare par peur de manquer, ou à l'inverse dépenser compulsivement pour te rassurer. L'équilibre se trouve dans une gestion sage et sereine.

## Maison 2 en Taureau
Saturne amplifie ici les thèmes de sécurité et de valeur. Tu apprends que la vraie richesse se construit avec le temps. Tes ressources augmentent à mesure que ta confiance grandit.

## Micro-rituel du jour (2 min)
- Identifier une ressource que tu as patiemment construite et la célébrer
- Trois respirations en relâchant l'anxiété autour de l'argent
- Journal : « Comment ma patience a-t-elle amélioré ma situation matérielle ? »""",

    ('taurus', 3): """# ♄ Saturne en Taureau
**En une phrase :** Tu communiques avec poids et réflexion — les mots lents portent plus loin.

## Ton moteur
Saturne en Taureau en Maison 3 te demande de développer une communication posée et substantielle. Tu peux avoir du mal à t'exprimer rapidement ou te sentir lent dans les apprentissages. Le travail de Saturne est de valoriser la profondeur sur la vitesse.

## Ton défi
Le piège : te taire par peur de ne pas avoir les bons mots, apprendre trop lentement à ton goût, ou te montrer têtu dans tes idées. L'équilibre se trouve dans la patience intellectuelle.

## Maison 3 en Taureau
Saturne structure ta façon de penser et d'apprendre. Tu retiens ce que tu apprends vraiment. Avec le temps, ta parole gagne en crédibilité et en impact.

## Micro-rituel du jour (2 min)
- Prendre le temps de formuler une pensée importante avec soin
- Trois respirations en acceptant ton rythme d'apprentissage
- Journal : « Quelle idée a gagné en profondeur par ma réflexion patiente ? »""",

    ('taurus', 4): """# ♄ Saturne en Taureau
**En une phrase :** Tu construis un foyer solide comme un roc — la stabilité domestique devient ton ancrage vital.

## Ton moteur
Saturne en Taureau en Maison 4 te demande de créer des fondations familiales durables. Tu peux avoir vécu des insécurités dans ton enfance ou ressentir le besoin de construire ce qui t'a manqué. Le travail de Saturne est de bâtir un sanctuaire stable.

## Ton défi
Le piège : t'accrocher au passé, résister aux changements dans la vie familiale, ou compenser le manque par l'accumulation matérielle. L'équilibre se trouve dans un enracinement serein.

## Maison 4 en Taureau
Saturne structure ta vie privée et tes racines. Tu construis ton foyer avec patience et détermination. Avec le temps, ta maison devient un havre de stabilité pour toi et les tiens.

## Micro-rituel du jour (2 min)
- Faire quelque chose qui renforce la stabilité de ton foyer
- Trois respirations en te connectant à tes racines avec gratitude
- Journal : « Comment mon foyer est-il devenu plus stable avec le temps ? »""",

    ('taurus', 5): """# ♄ Saturne en Taureau
**En une phrase :** Tu crées avec patience et méthode — la joie se cultive comme un jardin.

## Ton moteur
Saturne en Taureau en Maison 5 te confronte à tes blocages dans le plaisir et la créativité. Tu peux avoir du mal à te lâcher ou à profiter sans culpabilité. Le travail de Saturne est d'apprendre que la joie aussi se mérite par la patience.

## Ton défi
Le piège : te priver de plaisirs par austérité, avoir des relations amoureuses trop sérieuses trop vite, ou bloquer ta créativité par perfectionnisme. L'équilibre se trouve dans une joie cultivée avec soin.

## Maison 5 en Taureau
Saturne structure tes plaisirs et ta créativité. Tu développes des talents durables plutôt que des feux de paille. Avec le temps, tes amours et tes créations gagnent en profondeur.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir simple sans te sentir coupable
- Trois respirations en autorisant la joie à exister sans condition
- Journal : « Comment puis-je cultiver plus de plaisir durable dans ma vie ? »""",

    ('taurus', 6): """# ♄ Saturne en Taureau
**En une phrase :** Tu travailles avec constance et fiabilité — l'effort patient construit l'excellence.

## Ton moteur
Saturne en Taureau en Maison 6 te demande de développer des routines solides et efficaces. Tu peux avoir tendance à l'excès de travail ou à la rigidité dans tes méthodes. Le travail de Saturne est d'apprendre un rythme de productivité soutenable.

## Ton défi
Le piège : t'enliser dans des routines qui ne servent plus, négliger ta santé par excès de travail, ou résister aux changements nécessaires. L'équilibre se trouve dans une constance adaptable.

## Maison 6 en Taureau
Saturne structure ton quotidien et ta santé. Tu apprends à travailler de façon durable et efficace. Avec le temps, ta fiabilité devient ta plus grande qualité professionnelle.

## Micro-rituel du jour (2 min)
- Identifier une routine bénéfique que tu maintiens avec constance
- Trois respirations en remerciant ton corps pour sa fiabilité
- Journal : « Quelle habitude de travail me sert vraiment bien ? »""",

    ('taurus', 7): """# ♄ Saturne en Taureau
**En une phrase :** Tu construis des partenariats durables — l'engagement patient crée des liens indestructibles.

## Ton moteur
Saturne en Taureau en Maison 7 te demande de prendre les relations au sérieux et de les construire dans la durée. Tu peux avoir des difficultés à t'engager ou attirer des partenaires qui testent ta patience. Le travail de Saturne est d'apprendre la fidélité mature.

## Ton défi
Le piège : rester dans des relations par confort plutôt que par amour, être trop possessif, ou avoir du mal à évoluer avec ton partenaire. L'équilibre se trouve dans un engagement qui grandit avec le temps.

## Maison 7 en Taureau
Saturne structure tes partenariats. Les relations mûrissent lentement mais durent longtemps. Avec le temps, tu développes des partenariats solides basés sur la confiance mutuelle.

## Micro-rituel du jour (2 min)
- Exprimer ta gratitude pour la stabilité d'une relation importante
- Trois respirations en cultivant la patience dans tes partenariats
- Journal : « Comment mes relations ont-elles gagné en solidité avec le temps ? »""",

    ('taurus', 8): """# ♄ Saturne en Taureau
**En une phrase :** Tu traverses les transformations avec solidité — les crises renforcent tes fondations.

## Ton moteur
Saturne en Taureau en Maison 8 te confronte à tes résistances face au changement profond. Tu peux avoir du mal à lâcher prise sur ce que tu possèdes ou à accepter les transformations nécessaires. Le travail de Saturne est d'apprendre que la vraie sécurité survit aux pertes.

## Ton défi
Le piège : t'accrocher à ce qui doit partir, bloquer les processus de transformation par peur, ou confondre stabilité et rigidité. L'équilibre se trouve dans une transformation qui respecte ton rythme.

## Maison 8 en Taureau
Saturne structure ton rapport aux crises et aux ressources partagées. Tu apprends à naviguer les transformations avec patience. Les héritages ou investissements demandent une gestion prudente.

## Micro-rituel du jour (2 min)
- Identifier quelque chose que tu dois laisser partir et faire un pas vers le lâcher-prise
- Trois respirations en faisant confiance à ta capacité de reconstruire
- Journal : « Quelle transformation m'a finalement rendu plus fort ? »""",

    ('taurus', 9): """# ♄ Saturne en Taureau
**En une phrase :** Tu construis ta sagesse sur des fondations solides — la philosophie se vérifie par l'expérience concrète.

## Ton moteur
Saturne en Taureau en Maison 9 te demande de bâtir ta vision du monde sur des bases pratiques. Tu peux avoir du mal avec les philosophies trop abstraites ou les voyages trop lointains. Le travail de Saturne est de trouver le sens dans le concret.

## Ton défi
Le piège : rejeter ce qui n'est pas prouvable, limiter ton horizon par besoin de sécurité, ou t'accrocher à des croyances rigides. L'équilibre se trouve dans une ouverture ancrée.

## Maison 9 en Taureau
Saturne structure ta quête de sens. Tu apprends à travers l'expérience tangible plutôt que la théorie. Avec le temps, tu développes une sagesse pratique et fiable.

## Micro-rituel du jour (2 min)
- Identifier une croyance que tu as vérifiée par l'expérience
- Trois respirations en t'ouvrant à une perspective nouvelle mais réaliste
- Journal : « Quelle sagesse concrète guide mes décisions importantes ? »""",

    ('taurus', 10): """# ♄ Saturne en Taureau
**En une phrase :** Tu bâtis ta carrière avec patience et solidité — le succès durable se construit pierre par pierre.

## Ton moteur
Saturne en Taureau en Maison 10 te demande de construire ta réputation professionnelle sur des bases solides. Tu peux avoir une ambition patiente mais tenace. Le travail de Saturne est de mériter le succès par l'effort constant.

## Ton défi
Le piège : progresser trop lentement par excès de prudence, te satisfaire d'une sécurité professionnelle médiocre, ou confondre réussite et accumulation. L'équilibre se trouve dans une ambition patiente mais réelle.

## Maison 10 en Taureau
Saturne structure ta carrière et ta réputation. Le succès vient tardivement mais dure longtemps. Tu es destiné à des positions de stabilité et de fiabilité.

## Micro-rituel du jour (2 min)
- Identifier une étape de ta construction professionnelle et la célébrer
- Trois respirations en faisant confiance à ton rythme de progression
- Journal : « Comment ma patience a-t-elle servi ma carrière ? »""",

    ('taurus', 11): """# ♄ Saturne en Taureau
**En une phrase :** Tu construis des réseaux durables — les amitiés de qualité se cultivent avec le temps.

## Ton moteur
Saturne en Taureau en Maison 11 te demande de développer des amitiés et des projets collectifs sur des bases solides. Tu peux avoir peu d'amis mais des liens profonds. Le travail de Saturne est de contribuer de façon concrète aux causes que tu défends.

## Ton défi
Le piège : avoir du mal à t'intégrer aux groupes par besoin de sécurité, préférer l'inaction à l'incertitude collective, ou te montrer trop rigide dans tes idéaux. L'équilibre se trouve dans un engagement patient et concret.

## Maison 11 en Taureau
Saturne structure tes amitiés et tes projets collectifs. Tu apprends à construire des réseaux fiables et durables. Avec le temps, tu deviens un pilier pour les causes qui te tiennent à cœur.

## Micro-rituel du jour (2 min)
- Entretenir une amitié de longue date par un geste concret
- Trois respirations en appréciant la qualité sur la quantité dans tes relations
- Journal : « Quelle amitié durable m'apporte le plus de stabilité ? »""",

    ('taurus', 12): """# ♄ Saturne en Taureau
**En une phrase :** Tu apprivoises tes peurs matérielles — l'inconscient révèle des trésors de sécurité intérieure.

## Ton moteur
Saturne en Taureau en Maison 12 te confronte à tes angoisses cachées autour de la sécurité et de la valeur personnelle. Tu peux saboter inconsciemment ta prospérité. Le travail de Saturne est de libérer la confiance retenue dans l'ombre.

## Ton défi
Le piège : t'auto-saboter dans le domaine matériel, porter des peurs ancestrales autour de la pauvreté, ou fuir dans l'isolement plutôt que d'affronter tes insécurités. L'équilibre se trouve dans l'exploration patiente de l'inconscient.

## Maison 12 en Taureau
Saturne structure ton monde intérieur autour des thèmes de valeur et de sécurité. Tu apprends à trouver la vraie sécurité en toi. Avec le temps, tu libères une confiance profonde.

## Micro-rituel du jour (2 min)
- Identifier une peur cachée autour de la sécurité et la regarder avec compassion
- Trois respirations en te connectant à une sécurité intérieure inépuisable
- Journal : « Quelle peur matérielle ai-je commencé à dépasser ? »""",
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
