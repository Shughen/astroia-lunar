#!/usr/bin/env python3
"""
Script pour corriger les 96 interprétations MERCURY manquantes (maisons 2,3,5,6,8,9,11,12)
Format natal V2 avec: En une phrase / Ton moteur / Ton défi / Maison X / Micro-rituel
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import update
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

# Interprétations MERCURY format V2 - Maisons 2,3,5,6,8,9,11,12 pour les 12 signes
MERCURY_INTERPRETATIONS = {
    # ARIES
    ('aries', 2): """# ☿️ Mercure en Bélier

**En une phrase :** Tu penses à l'argent de façon directe et impulsive, avec une intelligence tournée vers l'action financière immédiate.

## Ton moteur
Ta façon de réfléchir aux ressources est rapide et orientée vers les opportunités. Tu as des idées innovantes pour gagner de l'argent et tu n'hésites pas à les exprimer.

## Ton défi
Éviter les décisions financières trop hâtives ou les négociations où tu vas trop vite. Ta communication autour de l'argent peut être perçue comme agressive.

## Maison 2 en Bélier
Tes valeurs sont directes, ton rapport à l'argent est actif. Tu penses en termes de conquête et d'indépendance matérielle.

## Micro-rituel du jour (2 min)
- Pense à une décision financière récente prise trop vite
- Respire et identifie ce qui t'a poussé à agir
- Note une réflexion à approfondir avant d'agir aujourd'hui""",

    ('aries', 3): """# ☿️ Mercure en Bélier

**En une phrase :** Tu penses et communiques avec rapidité et franchise, ton esprit est vif comme l'éclair.

## Ton moteur
Ta façon de réfléchir est directe et spontanée. Tu as des idées qui jaillissent, tu parles sans filtrer, tu apprends en faisant. L'échange intellectuel te stimule quand il est dynamique.

## Ton défi
Éviter de couper la parole, de t'impatienter face aux esprits plus lents, ou de blesser par des mots trop directs. Ton mental rapide peut manquer de nuance.

## Maison 3 en Bélier
Double activation : tu es un communicant-né, direct et stimulant. Tes échanges avec l'entourage sont vifs, tes apprentissages rapides.

## Micro-rituel du jour (2 min)
- Identifie un moment où tu as parlé trop vite récemment
- Respire et reformule mentalement avec plus de douceur
- Note une intention d'écoute active pour aujourd'hui""",

    ('aries', 5): """# ☿️ Mercure en Bélier

**En une phrase :** Tu exprimes ta créativité avec audace et tes idées ludiques fusent spontanément.

## Ton moteur
Ta façon de réfléchir à la créativité est dynamique et compétitive. Tu as des idées originales pour t'amuser, créer, jouer. L'expression créative passe par l'action.

## Ton défi
Éviter de te lasser trop vite de tes projets créatifs ou de transformer le jeu en compétition intellectuelle. La patience créative n'est pas ton fort.

## Maison 5 en Bélier
Tu abordes les plaisirs et la créativité avec énergie mentale. Tes romances commencent par des échanges vifs et stimulants.

## Micro-rituel du jour (2 min)
- Pense à un projet créatif abandonné par impatience
- Respire et reconnecte-toi à l'idée initiale
- Note une façon de jouer avec les mots aujourd'hui""",

    ('aries', 6): """# ☿️ Mercure en Bélier

**En une phrase :** Tu analyses ton quotidien avec efficacité et tu communiques au travail de façon directe et énergique.

## Ton moteur
Ta façon de réfléchir au travail est orientée solution. Tu identifies vite les problèmes et proposes des actions immédiates. L'efficacité mentale te caractérise.

## Ton défi
Éviter d'être trop brusque avec tes collègues ou de stresser face aux tâches qui demandent patience et minutie. Ton mental rapide supporte mal la répétition.

## Maison 6 en Bélier
Tu abordes le travail quotidien avec dynamisme intellectuel. Ta routine a besoin de défis mentaux, tes méthodes sont actives.

## Micro-rituel du jour (2 min)
- Identifie une tâche répétitive qui t'agace
- Respire et trouve une façon de la rendre plus stimulante
- Note une communication professionnelle à adoucir aujourd'hui""",

    ('aries', 8): """# ☿️ Mercure en Bélier

**En une phrase :** Tu réfléchis aux transformations profondes avec courage et tu n'as pas peur d'aborder les sujets tabous.

## Ton moteur
Ta façon de penser les crises est directe et combative. Tu analyses les situations de pouvoir avec lucidité, tu parles de ce que les autres évitent.

## Ton défi
Éviter d'être trop frontal sur les sujets sensibles ou de provoquer des conflits par ton franc-parler. Les nuances psychologiques t'échappent parfois.

## Maison 8 en Bélier
Tu abordes les transformations et l'intimité avec un mental actif. Les discussions sur l'argent partagé, la sexualité, la mort sont directes.

## Micro-rituel du jour (2 min)
- Pense à une vérité que tu as dite trop brutalement
- Respire et trouve une façon plus subtile de l'exprimer
- Note un sujet profond à explorer avec nuance aujourd'hui""",

    ('aries', 9): """# ☿️ Mercure en Bélier

**En une phrase :** Tu explores les grandes idées avec passion et tu défends tes convictions avec fougue intellectuelle.

## Ton moteur
Ta façon de penser les questions philosophiques est engagée et directe. Tu aimes les débats d'idées, les voyages intellectuels, l'apprentissage par l'aventure.

## Ton défi
Éviter d'imposer tes opinions ou de débattre de façon trop agressive. L'écoute des autres visions du monde demande patience.

## Maison 9 en Bélier
Tu abordes les études supérieures, les voyages et la spiritualité avec un mental aventurier. Tes convictions sont fortes et tu les défends.

## Micro-rituel du jour (2 min)
- Identifie une opinion que tu défends avec trop de vigueur
- Respire et imagine le point de vue opposé
- Note une façon d'apprendre quelque chose de nouveau aujourd'hui""",

    ('aries', 11): """# ☿️ Mercure en Bélier

**En une phrase :** Tu communiques dans les groupes avec leadership et tes idées innovantes inspirent tes amis.

## Ton moteur
Ta façon de penser les projets collectifs est pionnière. Tu proposes des idées audacieuses, tu communiques avec dynamisme, tu stimules le groupe.

## Ton défi
Éviter de monopoliser la parole ou de t'impatienter face aux décisions collectives lentes. Tes idées ont besoin d'être entendues, pas imposées.

## Maison 11 en Bélier
Tu abordes les amitiés et réseaux avec un mental de leader. Tes amis apprécient tes idées mais peuvent trouver ta communication trop directive.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu parles plus que tu n'écoutes
- Respire et visualise-toi en mode écoute
- Note une question à poser à un ami aujourd'hui (plutôt qu'une opinion)""",

    ('aries', 12): """# ☿️ Mercure en Bélier

**En une phrase :** Tu explores ton monde intérieur avec courage et ton mental combat activement tes peurs inconscientes.

## Ton moteur
Ta façon de penser la spiritualité est active et directe. Tu affrontes tes zones d'ombre avec un mental combatif, tu médites en mouvement.

## Ton défi
Éviter de fuir l'introspection par hyperactivité mentale ou de rationaliser tes émotions profondes plutôt que de les vivre.

## Maison 12 en Bélier
Tu abordes le monde invisible avec courage intellectuel. Tes retraites sont actives, ta spiritualité est dynamique.

## Micro-rituel du jour (2 min)
- Identifie une pensée récurrente que tu évites
- Respire et accueille-la sans la combattre
- Note une façon de ralentir ton mental aujourd'hui""",

    # TAURUS
    ('taurus', 2): """# ☿️ Mercure en Taureau

**En une phrase :** Tu réfléchis à l'argent avec pragmatisme et tes idées financières sont solides et durables.

## Ton moteur
Ta façon de penser les ressources est concrète et sécurisante. Tu analyses lentement mais sûrement, tes décisions financières sont réfléchies.

## Ton défi
Éviter de t'entêter dans des stratégies financières dépassées ou de résister aux nouvelles idées par confort mental.

## Maison 2 en Taureau
Double signature taurine : ton rapport mental à l'argent est profondément ancré dans le besoin de sécurité et de stabilité.

## Micro-rituel du jour (2 min)
- Pense à une idée financière nouvelle que tu as rejetée
- Respire et donne-lui une chance mentale
- Note une façon de penser "abondance" plutôt que "manque" aujourd'hui""",

    ('taurus', 3): """# ☿️ Mercure en Taureau

**En une phrase :** Tu communiques avec lenteur et profondeur, chaque mot est pesé et durable.

## Ton moteur
Ta façon de réfléchir est méthodique et sensorielle. Tu apprends par la pratique, tu parles quand tu es sûr, tu écoutes avec présence.

## Ton défi
Éviter la rigidité mentale ou la lenteur excessive qui frustre les autres. Ta pensée peut devenir trop fixe.

## Maison 3 en Taureau
Tu abordes la communication avec stabilité. Tes échanges avec l'entourage sont fiables, tes apprentissages concrets.

## Micro-rituel du jour (2 min)
- Identifie une idée à laquelle tu t'accroches depuis longtemps
- Respire et demande-toi si elle est encore valide
- Note une conversation à avoir sans te presser aujourd'hui""",

    ('taurus', 5): """# ☿️ Mercure en Taureau

**En une phrase :** Tu exprimes ta créativité avec sensualité et tes idées artistiques prennent forme concrète.

## Ton moteur
Ta façon de penser la créativité est pratique et esthétique. Tu as des idées qui se touchent, se goûtent, se concrétisent lentement mais sûrement.

## Ton défi
Éviter de bloquer ta créativité par perfectionnisme ou de rejeter les idées qui ne semblent pas immédiatement réalisables.

## Maison 5 en Taureau
Tu abordes les plaisirs et l'expression créative avec un mental sensoriel. Tes romances commencent par des échanges doux et concrets.

## Micro-rituel du jour (2 min)
- Pense à une idée créative que tu n'as pas concrétisée
- Respire et visualise un premier pas concret
- Note une façon de jouer avec tes sens aujourd'hui""",

    ('taurus', 6): """# ☿️ Mercure en Taureau

**En une phrase :** Tu organises ton quotidien avec méthode et tes routines de travail sont stables et fiables.

## Ton moteur
Ta façon de penser le travail est concrète et efficace. Tu analyses les problèmes avec patience, tu trouves des solutions durables.

## Ton défi
Éviter de t'enliser dans des routines dépassées ou de résister aux changements de méthodes par confort mental.

## Maison 6 en Taureau
Tu abordes le travail quotidien avec stabilité mentale. Tes méthodes sont éprouvées, ta communication professionnelle est fiable.

## Micro-rituel du jour (2 min)
- Identifie une routine de travail que tu n'as pas questionnée depuis longtemps
- Respire et demande-toi si elle est optimale
- Note une amélioration concrète possible aujourd'hui""",

    ('taurus', 8): """# ☿️ Mercure en Taureau

**En une phrase :** Tu réfléchis aux transformations profondes avec pragmatisme et tu ancres les changements dans la durée.

## Ton moteur
Ta façon de penser les crises est stabilisante. Tu analyses les situations de pouvoir avec réalisme, tu parles des sujets difficiles avec calme.

## Ton défi
Éviter de résister aux transformations nécessaires par peur du changement ou de t'accrocher à des possessions partagées par sécurité.

## Maison 8 en Taureau
Tu abordes l'intimité et les ressources partagées avec un mental pragmatique. Les discussions financières communes sont concrètes.

## Micro-rituel du jour (2 min)
- Pense à un changement profond que tu repousses mentalement
- Respire et identifie un bénéfice concret de cette transformation
- Note un sujet "tabou" à aborder avec calme aujourd'hui""",

    ('taurus', 9): """# ☿️ Mercure en Taureau

**En une phrase :** Tu explores les grandes questions avec pragmatisme et tes convictions sont ancrées dans l'expérience concrète.

## Ton moteur
Ta façon de penser la philosophie est pratique. Tu apprends par l'expérience directe, tu voyages pour toucher et goûter, pas seulement voir.

## Ton défi
Éviter de rejeter les idées abstraites par préférence pour le concret ou de t'enfermer dans des croyances matérialistes.

## Maison 9 en Taureau
Tu abordes les études supérieures et les voyages avec un mental sensoriel. Ta spiritualité a besoin de s'incarner dans le corps.

## Micro-rituel du jour (2 min)
- Identifie une idée abstraite que tu as du mal à accepter
- Respire et cherche comment elle pourrait se concrétiser
- Note une façon d'apprendre par les sens aujourd'hui""",

    ('taurus', 11): """# ☿️ Mercure en Taureau

**En une phrase :** Tu communiques dans les groupes avec fiabilité et tes idées pour le collectif sont pragmatiques et durables.

## Ton moteur
Ta façon de penser les projets collectifs est réaliste. Tu proposes des idées concrètes, tu construis des amitiés stables par des échanges réguliers.

## Ton défi
Éviter de freiner les innovations du groupe par prudence excessive ou de t'accrocher à des amitiés qui ne te nourrissent plus.

## Maison 11 en Taureau
Tu abordes les réseaux et amitiés avec un mental stable. Tes amis apprécient ta fiabilité mais peuvent souhaiter plus de spontanéité.

## Micro-rituel du jour (2 min)
- Pense à une idée de groupe que tu as freinée par prudence
- Respire et trouve un aspect positif de cette innovation
- Note une façon de contribuer concrètement à un projet collectif aujourd'hui""",

    ('taurus', 12): """# ☿️ Mercure en Taureau

**En une phrase :** Tu explores ton monde intérieur avec ancrage et ton mental trouve le calme dans la présence sensorielle.

## Ton moteur
Ta façon de penser la spiritualité est incarnée. Tu médites mieux avec le corps, tu trouves le sacré dans la nature et les sensations.

## Ton défi
Éviter de fuir l'introspection par le confort matériel ou de rationaliser le mystère plutôt que de le vivre.

## Maison 12 en Taureau
Tu abordes le monde invisible avec un mental ancré. Tes retraites sont sensorielles, ta spiritualité est terrestre.

## Micro-rituel du jour (2 min)
- Identifie une anxiété que tu calmes par la consommation
- Respire et trouve une façon sensorielle saine de t'apaiser
- Note une pratique spirituelle incarnée pour aujourd'hui""",

    # GEMINI
    ('gemini', 2): """# ☿️ Mercure en Gémeaux

**En une phrase :** Tu penses à l'argent avec agilité et tu multiplies les sources de revenus grâce à ta polyvalence.

## Ton moteur
Ta façon de réfléchir aux ressources est vive et adaptable. Tu as mille idées pour gagner de l'argent, tu communiques facilement autour des finances.

## Ton défi
Éviter la dispersion financière ou les changements de stratégie trop fréquents. Ta polyvalence peut devenir instabilité.

## Maison 2 en Gémeaux
Tu abordes l'argent avec curiosité mentale. Tes revenus peuvent venir de plusieurs sources, ton rapport aux possessions est léger.

## Micro-rituel du jour (2 min)
- Pense à tes différentes sources de revenus ou idées financières
- Respire et choisis une priorité pour aujourd'hui
- Note une façon de simplifier ton rapport à l'argent""",

    ('gemini', 3): """# ☿️ Mercure en Gémeaux

**En une phrase :** Tu penses et communiques avec une vivacité exceptionnelle, ton esprit est un papillon brillant.

## Ton moteur
Ta façon de réfléchir est rapide, curieuse et multiple. Tu as besoin de stimulation intellectuelle constante, d'échanges variés, d'apprendre sans cesse.

## Ton défi
Éviter la superficialité ou l'éparpillement mental. Ta curiosité peut te disperser dans trop de directions à la fois.

## Maison 3 en Gémeaux
Position renforcée : tu es un communicant exceptionnel, curieux de tout, toujours en train d'apprendre et d'échanger.

## Micro-rituel du jour (2 min)
- Identifie les sujets qui occupent ton esprit en ce moment
- Respire et choisis celui qui mérite ton attention aujourd'hui
- Note une façon d'approfondir plutôt que de survoler""",

    ('gemini', 5): """# ☿️ Mercure en Gémeaux

**En une phrase :** Tu exprimes ta créativité par les mots et les jeux d'esprit, ton art est intellectuel et ludique.

## Ton moteur
Ta façon de penser la créativité est verbale et multiple. Tu as des idées qui s'enchaînent, tu joues avec les concepts, tu t'amuses avec le langage.

## Ton défi
Éviter de rester dans le mental au détriment de la création concrète ou de te lasser trop vite de tes projets créatifs.

## Maison 5 en Gémeaux
Tu abordes les plaisirs et la créativité avec un mental joueur. Tes romances commencent par des conversations brillantes.

## Micro-rituel du jour (2 min)
- Pense à un projet créatif que tu as laissé au stade de l'idée
- Respire et trouve un premier pas concret
- Note un jeu de mots ou une phrase créative aujourd'hui""",

    ('gemini', 6): """# ☿️ Mercure en Gémeaux

**En une phrase :** Tu organises ton quotidien avec flexibilité et ta communication au travail est agile et polyvalente.

## Ton moteur
Ta façon de penser le travail est adaptable et curieuse. Tu as besoin de variété dans tes tâches, d'échanges multiples avec tes collègues.

## Ton défi
Éviter de papillonner d'une tâche à l'autre sans en finir aucune ou de te disperser dans trop de communications simultanées.

## Maison 6 en Gémeaux
Tu abordes le travail quotidien avec agilité mentale. Tes méthodes sont variées, ta communication professionnelle est fluide.

## Micro-rituel du jour (2 min)
- Identifie les tâches en cours que tu n'as pas terminées
- Respire et choisis celle à finaliser aujourd'hui
- Note une façon de te concentrer malgré les distractions""",

    ('gemini', 8): """# ☿️ Mercure en Gémeaux

**En une phrase :** Tu réfléchis aux transformations profondes avec curiosité et tu explores les mystères avec légèreté.

## Ton moteur
Ta façon de penser les crises est analytique et détachée. Tu poses des questions sur les tabous, tu explores les zones d'ombre avec curiosité intellectuelle.

## Ton défi
Éviter de rester en surface des transformations ou de rationaliser l'intensité émotionnelle plutôt que de la vivre.

## Maison 8 en Gémeaux
Tu abordes l'intimité et les ressources partagées avec un mental curieux. Les discussions profondes sont nombreuses mais parfois superficielles.

## Micro-rituel du jour (2 min)
- Pense à un sujet profond que tu analyses sans le ressentir
- Respire et laisse l'émotion associée émerger
- Note une question profonde à explorer au-delà des mots aujourd'hui""",

    ('gemini', 9): """# ☿️ Mercure en Gémeaux

**En une phrase :** Tu explores les grandes questions avec curiosité insatiable et tu collectes les visions du monde comme des trésors.

## Ton moteur
Ta façon de penser la philosophie est éclectique et ouverte. Tu aimes comparer les idées, les religions, les cultures. L'apprentissage est ton voyage.

## Ton défi
Éviter de survoler trop de systèmes de pensée sans en approfondir aucun ou de confondre accumulation d'informations et sagesse.

## Maison 9 en Gémeaux
Tu abordes les études supérieures et les voyages avec un mental d'explorateur intellectuel. Ta spiritualité est curieuse de tout.

## Micro-rituel du jour (2 min)
- Identifie une croyance ou philosophie que tu connais superficiellement
- Respire et choisis de l'approfondir vraiment
- Note une façon d'apprendre en profondeur aujourd'hui""",

    ('gemini', 11): """# ☿️ Mercure en Gémeaux

**En une phrase :** Tu communiques dans les groupes avec brio et ton réseau est vaste grâce à ta sociabilité intellectuelle.

## Ton moteur
Ta façon de penser les projets collectifs est connectée et multiple. Tu as des idées pour tous, tu fais le lien entre les personnes, tu animes les échanges.

## Ton défi
Éviter de t'éparpiller dans trop de groupes ou de relations superficielles. La qualité des amitiés compte autant que la quantité.

## Maison 11 en Gémeaux
Tu abordes les amitiés et réseaux avec un mental de connecteur. Tes amis sont variés, tes projets collectifs nombreux.

## Micro-rituel du jour (2 min)
- Pense à tes différents cercles d'amis et projets
- Respire et identifie celui qui mérite plus d'attention
- Note une façon d'approfondir une amitié plutôt que d'en multiplier d'autres""",

    ('gemini', 12): """# ☿️ Mercure en Gémeaux

**En une phrase :** Tu explores ton monde intérieur avec curiosité et ton mental navigue entre les dimensions avec légèreté.

## Ton moteur
Ta façon de penser la spiritualité est exploratoire et multiple. Tu médites en questionnant, tu explores différentes pratiques, tu écris pour comprendre.

## Ton défi
Éviter de rester en surface de ta vie intérieure ou de rationaliser le mystère plutôt que de le laisser être.

## Maison 12 en Gémeaux
Tu abordes le monde invisible avec un mental de chercheur. Tes retraites sont studieuses, ta spiritualité est intellectuelle.

## Micro-rituel du jour (2 min)
- Identifie une question spirituelle que tu analyses sans fin
- Respire et laisse la réponse venir sans mots
- Note un moment de silence mental prévu pour aujourd'hui""",

    # CANCER
    ('cancer', 2): """# ☿️ Mercure en Cancer

**En une phrase :** Tu penses à l'argent de façon émotionnelle et tes ressources sont liées à ton sentiment de sécurité intérieure.

## Ton moteur
Ta façon de réfléchir aux finances est intuitive et protectrice. Tu as besoin de te sentir en sécurité pour penser clairement à l'argent.

## Ton défi
Éviter de laisser tes humeurs influencer tes décisions financières ou de t'accrocher aux possessions par besoin émotionnel.

## Maison 2 en Cancer
Tu abordes l'argent avec un mental protecteur. Tes valeurs sont familiales, ton rapport aux ressources est émotionnel.

## Micro-rituel du jour (2 min)
- Pense à une décision financière influencée par une émotion
- Respire et sépare le besoin réel de la peur
- Note une façon de te sentir en sécurité sans acheter aujourd'hui""",

    ('cancer', 3): """# ☿️ Mercure en Cancer

**En une phrase :** Tu communiques avec sensibilité et tes mots portent la mémoire du cœur.

## Ton moteur
Ta façon de réfléchir est intuitive et émotionnelle. Tu apprends mieux quand tu te sens en sécurité, tu communiques avec empathie et douceur.

## Ton défi
Éviter de te fermer quand tu te sens incompris ou de communiquer de façon trop indirecte par peur du rejet.

## Maison 3 en Cancer
Tu abordes la communication avec sensibilité. Tes échanges avec l'entourage sont nourrissants, tes apprentissages liés aux émotions.

## Micro-rituel du jour (2 min)
- Identifie un moment où tu n'as pas osé exprimer ta pensée
- Respire et trouve les mots justes dans ton cœur
- Note une conversation bienveillante à avoir aujourd'hui""",

    ('cancer', 5): """# ☿️ Mercure en Cancer

**En une phrase :** Tu exprimes ta créativité avec émotion et tes créations portent la mémoire de ton histoire.

## Ton moteur
Ta façon de penser la créativité est nostalgique et intime. Tu as des idées qui viennent du cœur, tu crées pour transmettre et nourrir.

## Ton défi
Éviter de bloquer ta créativité par trop de sensibilité au jugement ou de te replier sur des formes d'expression trop personnelles.

## Maison 5 en Cancer
Tu abordes les plaisirs et la créativité avec un mental émotionnel. Tes romances commencent par une connexion intuitive.

## Micro-rituel du jour (2 min)
- Pense à une création que tu n'as pas partagée par peur
- Respire et visualise un cercle bienveillant qui l'accueille
- Note une façon de créer à partir de tes émotions aujourd'hui""",

    ('cancer', 6): """# ☿️ Mercure en Cancer

**En une phrase :** Tu organises ton quotidien avec attention et ta communication au travail est empathique et protectrice.

## Ton moteur
Ta façon de penser le travail est intuitive et attentive aux autres. Tu sens les besoins de l'équipe, tu prends soin par tes mots.

## Ton défi
Éviter de te laisser submerger par les émotions au travail ou de prendre personnellement les critiques professionnelles.

## Maison 6 en Cancer
Tu abordes le travail quotidien avec sensibilité. Tes méthodes sont intuitives, ta communication professionnelle est bienveillante.

## Micro-rituel du jour (2 min)
- Identifie une situation de travail qui t'affecte émotionnellement
- Respire et sépare tes émotions du contexte professionnel
- Note une façon de prendre soin de toi au travail aujourd'hui""",

    ('cancer', 8): """# ☿️ Mercure en Cancer

**En une phrase :** Tu réfléchis aux transformations profondes avec intuition et tu explores les mystères avec le cœur.

## Ton moteur
Ta façon de penser les crises est empathique et profonde. Tu sens les non-dits, tu accueilles les émotions difficiles des autres.

## Ton défi
Éviter de te perdre dans les profondeurs émotionnelles ou de porter les transformations des autres comme les tiennes.

## Maison 8 en Cancer
Tu abordes l'intimité et les ressources partagées avec un mental émotionnel. Les discussions profondes sont intuitives et nourrissantes.

## Micro-rituel du jour (2 min)
- Pense à une émotion profonde que tu portes pour quelqu'un d'autre
- Respire et rends-lui ce qui lui appartient
- Note une limite émotionnelle à poser aujourd'hui""",

    ('cancer', 9): """# ☿️ Mercure en Cancer

**En une phrase :** Tu explores les grandes questions avec le cœur et ta sagesse vient de l'intuition et de la mémoire.

## Ton moteur
Ta façon de penser la philosophie est intime et ancestrale. Tu apprends par résonance émotionnelle, ta spiritualité est liée à tes racines.

## Ton défi
Éviter de rejeter les idées qui ne résonnent pas émotionnellement ou de confondre familiarité et vérité.

## Maison 9 en Cancer
Tu abordes les études supérieures et les voyages avec un mental qui cherche un "chez soi" partout. Ta spiritualité est nourrissante.

## Micro-rituel du jour (2 min)
- Identifie une croyance héritée de ta famille
- Respire et demande-toi si elle est vraiment tienne
- Note une façon d'explorer avec ouverture tout en honorant tes racines""",

    ('cancer', 11): """# ☿️ Mercure en Cancer

**En une phrase :** Tu communiques dans les groupes avec chaleur et tes amis deviennent une famille de cœur.

## Ton moteur
Ta façon de penser les projets collectifs est protectrice et nourrissante. Tu crées des espaces où chacun se sent accueilli.

## Ton défi
Éviter de te replier quand le groupe ne te nourrit pas assez ou de projeter tes besoins familiaux sur tes amitiés.

## Maison 11 en Cancer
Tu abordes les amitiés et réseaux avec un mental familial. Tes amis sont comme une tribu, tes projets collectifs visent le bien-être de tous.

## Micro-rituel du jour (2 min)
- Pense à un ami qui aurait besoin d'une attention particulière
- Respire et envoie-lui mentalement de la chaleur
- Note une façon de nourrir ton cercle d'amis aujourd'hui""",

    ('cancer', 12): """# ☿️ Mercure en Cancer

**En une phrase :** Tu explores ton monde intérieur avec sensibilité et ton mental trouve refuge dans l'imaginaire et les rêves.

## Ton moteur
Ta façon de penser la spiritualité est intime et symbolique. Tu médites en te connectant à tes ancêtres, tu rêves de façon significative.

## Ton défi
Éviter de te perdre dans la nostalgie ou l'imaginaire au détriment du présent, ou de fuir dans tes rêves quand la réalité est difficile.

## Maison 12 en Cancer
Tu abordes le monde invisible avec un mental maternel. Tes retraites sont cocooning, ta spiritualité est intuitive et protectrice.

## Micro-rituel du jour (2 min)
- Identifie un rêve récent ou une image qui te revient
- Respire et laisse son message émerger
- Note une façon d'honorer ton intuition aujourd'hui""",

    # LEO
    ('leo', 2): """# ☿️ Mercure en Lion

**En une phrase :** Tu penses à l'argent avec générosité et tes idées financières sont grandes et confiantes.

## Ton moteur
Ta façon de réfléchir aux ressources est créative et ambitieuse. Tu as des visions grandioses, tu communiques sur l'argent avec assurance.

## Ton défi
Éviter les dépenses ostentatoires pour impressionner ou l'orgueil qui t'empêche de demander de l'aide financière.

## Maison 2 en Lion
Tu abordes l'argent avec un mental généreux et fier. Tes valeurs sont nobles, ton rapport aux ressources est lié à ton image.

## Micro-rituel du jour (2 min)
- Pense à une dépense récente faite pour impressionner
- Respire et reconnais ton besoin de reconnaissance
- Note une façon de te sentir riche intérieurement aujourd'hui""",

    ('leo', 3): """# ☿️ Mercure en Lion

**En une phrase :** Tu communiques avec prestance et tes mots portent la lumière de ta confiance.

## Ton moteur
Ta façon de réfléchir est créative et expressive. Tu parles avec conviction, tu as besoin qu'on t'écoute, tes idées veulent briller.

## Ton défi
Éviter de monopoliser l'attention dans les échanges ou de ne pas écouter les autres par excès de confiance en tes idées.

## Maison 3 en Lion
Tu abordes la communication avec charisme. Tes échanges avec l'entourage sont chaleureux, tes apprentissages passent par l'expression.

## Micro-rituel du jour (2 min)
- Identifie une conversation où tu as trop parlé de toi
- Respire et trouve une question à poser à l'autre
- Note une façon de faire briller quelqu'un d'autre par tes mots aujourd'hui""",

    ('leo', 5): """# ☿️ Mercure en Lion

**En une phrase :** Tu exprimes ta créativité avec éclat et tes idées artistiques veulent être vues et célébrées.

## Ton moteur
Ta façon de penser la créativité est flamboyante et personnelle. Tu as des idées qui veulent la scène, tu crées pour être reconnu.

## Ton défi
Éviter de bloquer ta créativité si elle n'est pas applaudie ou de chercher la validation au détriment de l'authenticité.

## Maison 5 en Lion
Position renforcée : tu es un créateur né, tes idées brillent, tes romances sont des histoires dignes d'un film.

## Micro-rituel du jour (2 min)
- Pense à une création que tu n'as pas partagée par peur de ne pas être applaudi
- Respire et crée pour la joie de créer
- Note une façon d'exprimer ta créativité sans attendre de retour aujourd'hui""",

    ('leo', 6): """# ☿️ Mercure en Lion

**En une phrase :** Tu organises ton quotidien avec style et ta communication au travail rayonne de confiance.

## Ton moteur
Ta façon de penser le travail est ambitieuse et créative. Tu veux que ton travail soit reconnu, tu communiques avec autorité naturelle.

## Ton défi
Éviter de vouloir toujours avoir raison au travail ou de prendre mal les critiques qui touchent ton orgueil.

## Maison 6 en Lion
Tu abordes le travail quotidien avec prestance. Tes méthodes sont personnelles, ta communication professionnelle est charismatique.

## Micro-rituel du jour (2 min)
- Identifie une critique professionnelle qui t'a blessé
- Respire et trouve ce qu'elle peut t'apprendre
- Note une façon de briller au travail avec humilité aujourd'hui""",

    ('leo', 8): """# ☿️ Mercure en Lion

**En une phrase :** Tu réfléchis aux transformations profondes avec courage et tu éclaires les zones d'ombre avec ta lumière.

## Ton moteur
Ta façon de penser les crises est dramatique et théâtrale. Tu affrontes les ténèbres avec panache, tu parles de l'indicible avec force.

## Ton défi
Éviter de dramatiser les transformations ou de vouloir être le héros de toutes les crises, y compris celles des autres.

## Maison 8 en Lion
Tu abordes l'intimité et les ressources partagées avec un mental noble. Les discussions profondes sont intenses et pleines de feu.

## Micro-rituel du jour (2 min)
- Pense à une crise où tu as voulu être au centre
- Respire et accepte de n'être qu'un acteur parmi d'autres
- Note une façon d'éclairer sans dominer aujourd'hui""",

    ('leo', 9): """# ☿️ Mercure en Lion

**En une phrase :** Tu explores les grandes questions avec conviction et tes croyances sont portées avec fierté.

## Ton moteur
Ta façon de penser la philosophie est généreuse et confiante. Tu as une vision du monde que tu veux partager, tu enseignes avec charisme.

## Ton défi
Éviter de croire que ta vérité est la seule ou d'imposer tes convictions avec arrogance.

## Maison 9 en Lion
Tu abordes les études supérieures et les voyages avec un mental de roi. Ta spiritualité est généreuse et rayonnante.

## Micro-rituel du jour (2 min)
- Identifie une conviction que tu défends avec trop d'orgueil
- Respire et trouve l'humilité de douter
- Note une façon d'apprendre d'une autre vision du monde aujourd'hui""",

    ('leo', 11): """# ☿️ Mercure en Lion

**En une phrase :** Tu communiques dans les groupes avec charisme et tes idées collectives sont inspirantes.

## Ton moteur
Ta façon de penser les projets collectifs est visionnaire et généreuse. Tu veux que le groupe brille, tu motives par ta confiance.

## Ton défi
Éviter de vouloir être le leader de chaque groupe ou de te sentir blessé si tes idées ne sont pas célébrées.

## Maison 11 en Lion
Tu abordes les amitiés et réseaux avec un mental de star. Tes amis t'admirent, tes projets collectifs sont ambitieux.

## Micro-rituel du jour (2 min)
- Pense à un projet de groupe où tu voulais être au centre
- Respire et visualise le succès collectif sans toi au premier plan
- Note une façon de célébrer un ami aujourd'hui""",

    ('leo', 12): """# ☿️ Mercure en Lion

**En une phrase :** Tu explores ton monde intérieur avec courage et ton mental veut faire briller même l'invisible.

## Ton moteur
Ta façon de penser la spiritualité est créative et lumineuse. Tu médites en cherchant ta lumière intérieure, tu transformes les ombres en or.

## Ton défi
Éviter de vouloir être reconnu même dans ta vie spirituelle ou de fuir l'humilité que demande l'invisible.

## Maison 12 en Lion
Tu abordes le monde invisible avec un mental royal. Tes retraites sont créatives, ta spiritualité cherche à faire briller l'âme.

## Micro-rituel du jour (2 min)
- Identifie une part de toi que tu caches par honte
- Respire et envoie-lui de la lumière
- Note une façon d'être en paix avec ton ombre aujourd'hui""",

    # VIRGO
    ('virgo', 2): """# ☿️ Mercure en Vierge

**En une phrase :** Tu penses à l'argent avec méthode et tes analyses financières sont précises et pragmatiques.

## Ton moteur
Ta façon de réfléchir aux ressources est détaillée et efficace. Tu calcules, tu compares, tu optimises. L'argent est un outil à gérer intelligemment.

## Ton défi
Éviter l'anxiété financière liée au perfectionnisme ou de te perdre dans les détails au détriment de la vision globale.

## Maison 2 en Vierge
Tu abordes l'argent avec un mental analytique. Tes valeurs sont pratiques, ton rapport aux ressources est organisé.

## Micro-rituel du jour (2 min)
- Pense à une anxiété financière qui te préoccupe
- Respire et demande-toi si elle est proportionnelle au risque réel
- Note une action concrète et simple pour te rassurer aujourd'hui""",

    ('virgo', 3): """# ☿️ Mercure en Vierge

**En une phrase :** Tu communiques avec précision et tes analyses sont détaillées et utiles.

## Ton moteur
Ta façon de réfléchir est méthodique et orientée service. Tu analyses les informations avec minutie, tu communiques pour aider et clarifier.

## Ton défi
Éviter la critique excessive ou le perfectionnisme verbal qui peut blesser. Tes corrections ne sont pas toujours bienvenues.

## Maison 3 en Vierge
Position renforcée : tu es un communicant précis et serviable. Tes échanges visent l'utilité, tes apprentissages sont méthodiques.

## Micro-rituel du jour (2 min)
- Identifie une critique que tu as faite récemment
- Respire et trouve une façon plus encourageante de dire la même chose
- Note une façon d'aider par tes mots plutôt que de corriger""",

    ('virgo', 5): """# ☿️ Mercure en Vierge

**En une phrase :** Tu exprimes ta créativité avec technique et tes idées artistiques sont peaufinées dans les moindres détails.

## Ton moteur
Ta façon de penser la créativité est artisanale et perfectionniste. Tu crées avec méthode, tu peaufines, tu améliores sans cesse.

## Ton défi
Éviter de ne jamais finir par perfectionnisme ou de critiquer ta créativité au point de la bloquer.

## Maison 5 en Vierge
Tu abordes les plaisirs et la créativité avec un mental technique. Tes romances sont analysées, ta créativité est travaillée.

## Micro-rituel du jour (2 min)
- Pense à un projet créatif bloqué par perfectionnisme
- Respire et accepte une version "suffisamment bonne"
- Note une façon de créer sans viser la perfection aujourd'hui""",

    ('virgo', 6): """# ☿️ Mercure en Vierge

**En une phrase :** Tu organises ton quotidien avec efficacité maximale et ta communication au travail vise l'amélioration continue.

## Ton moteur
Ta façon de penser le travail est orientée optimisation. Tu vois ce qui peut être amélioré, tu crées des systèmes efficaces.

## Ton défi
Éviter de t'épuiser à tout optimiser ou de critiquer le travail des autres par excès de standards élevés.

## Maison 6 en Vierge
Position renforcée : tu es un travailleur méthodique et dévoué. Ta routine est optimisée, ta communication professionnelle est précise.

## Micro-rituel du jour (2 min)
- Identifie un aspect de ton travail que tu veux encore améliorer
- Respire et accepte qu'il soit suffisant pour aujourd'hui
- Note une façon de te féliciter pour ce qui est déjà bien fait""",

    ('virgo', 8): """# ☿️ Mercure en Vierge

**En une phrase :** Tu réfléchis aux transformations profondes avec analyse et tu décortiques les mystères avec méthode.

## Ton moteur
Ta façon de penser les crises est rationnelle et utile. Tu analyses les situations complexes, tu trouves des solutions pratiques aux problèmes profonds.

## Ton défi
Éviter de vouloir tout comprendre rationnellement ou de fuir l'intensité émotionnelle dans l'analyse.

## Maison 8 en Vierge
Tu abordes l'intimité et les ressources partagées avec un mental analytique. Les discussions profondes sont pratiques et orientées solutions.

## Micro-rituel du jour (2 min)
- Pense à une transformation que tu essaies de contrôler par l'analyse
- Respire et laisse le mystère être mystère
- Note une façon d'accueillir l'intensité sans la disséquer aujourd'hui""",

    ('virgo', 9): """# ☿️ Mercure en Vierge

**En une phrase :** Tu explores les grandes questions avec méthode et ta sagesse est pratique et applicable.

## Ton moteur
Ta façon de penser la philosophie est concrète et critique. Tu analyses les systèmes de pensée, tu gardes ce qui est utile.

## Ton défi
Éviter de rejeter les visions du monde qui ne sont pas "pratiques" ou de critiquer les croyances des autres.

## Maison 9 en Vierge
Tu abordes les études supérieures et les voyages avec un mental analytique. Ta spiritualité est orientée service et amélioration de soi.

## Micro-rituel du jour (2 min)
- Identifie une croyance que tu rejettes car "pas pratique"
- Respire et trouve ce qu'elle pourrait t'apporter
- Note une façon d'appliquer concrètement une sagesse abstraite aujourd'hui""",

    ('virgo', 11): """# ☿️ Mercure en Vierge

**En une phrase :** Tu communiques dans les groupes avec précision et tes idées collectives visent l'amélioration concrète.

## Ton moteur
Ta façon de penser les projets collectifs est analytique et serviable. Tu vois ce qui peut être amélioré, tu proposes des solutions pratiques.

## Ton défi
Éviter de critiquer le groupe ou de te sentir frustré quand les autres ne visent pas l'efficacité.

## Maison 11 en Vierge
Tu abordes les amitiés et réseaux avec un mental de service. Tes amis apprécient tes conseils, mais attention à ne pas devenir le critique de chacun.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu joues le rôle du "correcteur"
- Respire et trouve ce qui va bien sans chercher à améliorer
- Note une façon d'apprécier tes amis tels qu'ils sont aujourd'hui""",

    ('virgo', 12): """# ☿️ Mercure en Vierge

**En une phrase :** Tu explores ton monde intérieur avec méthode et ton mental cherche à organiser même l'invisible.

## Ton moteur
Ta façon de penser la spiritualité est pratique et orientée guérison. Tu médites pour t'améliorer, tu analyses tes rêves pour comprendre.

## Ton défi
Éviter de vouloir tout comprendre et contrôler dans ta vie intérieure ou de critiquer ta pratique spirituelle.

## Maison 12 en Vierge
Tu abordes le monde invisible avec un mental de guérisseur. Tes retraites sont pratiques, ta spiritualité vise l'amélioration de l'âme.

## Micro-rituel du jour (2 min)
- Identifie un aspect de ta vie intérieure que tu veux "réparer"
- Respire et accepte-le tel qu'il est, parfaitement imparfait
- Note une façon de méditer sans agenda d'amélioration aujourd'hui""",

    # LIBRA
    ('libra', 2): """# ☿️ Mercure en Balance

**En une phrase :** Tu penses à l'argent avec équilibre et tes décisions financières cherchent l'harmonie et le partage équitable.

## Ton moteur
Ta façon de réfléchir aux ressources est relationnelle et esthétique. Tu penses à l'argent en termes de partenariat, de beauté, d'équité.

## Ton défi
Éviter l'indécision financière ou la tendance à dépendre des autres pour les décisions matérielles importantes.

## Maison 2 en Balance
Tu abordes l'argent avec un mental diplomatique. Tes valeurs sont orientées vers l'harmonie, ton rapport aux ressources est partagé.

## Micro-rituel du jour (2 min)
- Pense à une décision financière que tu repousses par indécision
- Respire et choisis, même imparfaitement
- Note une façon de prendre une décision matérielle par toi-même aujourd'hui""",

    ('libra', 3): """# ☿️ Mercure en Balance

**En une phrase :** Tu communiques avec diplomatie et tes mots cherchent toujours l'équilibre et l'harmonie.

## Ton moteur
Ta façon de réfléchir est relationnelle et équilibrée. Tu vois les deux côtés de chaque question, tu communiques avec tact et élégance.

## Ton défi
Éviter de ne jamais trancher ou de dire ce que les autres veulent entendre au lieu de ta vérité.

## Maison 3 en Balance
Tu abordes la communication avec grâce. Tes échanges avec l'entourage sont harmonieux, tes apprentissages passent par le dialogue.

## Micro-rituel du jour (2 min)
- Identifie une opinion que tu n'oses pas exprimer pour garder la paix
- Respire et trouve une façon élégante de la partager
- Note une vérité à dire avec diplomatie aujourd'hui""",

    ('libra', 5): """# ☿️ Mercure en Balance

**En une phrase :** Tu exprimes ta créativité avec élégance et tes idées artistiques visent la beauté et l'harmonie.

## Ton moteur
Ta façon de penser la créativité est esthétique et collaborative. Tu crées pour embellir, tu partages facilement tes idées artistiques.

## Ton défi
Éviter de dépendre de l'avis des autres pour valider ta créativité ou de ne créer que ce qui plaît.

## Maison 5 en Balance
Tu abordes les plaisirs et la créativité avec un mental esthétique. Tes romances sont élégantes et équilibrées.

## Micro-rituel du jour (2 min)
- Pense à une création que tu modifies pour plaire aux autres
- Respire et trouve ton expression authentique
- Note une façon de créer pour toi-même aujourd'hui""",

    ('libra', 6): """# ☿️ Mercure en Balance

**En une phrase :** Tu organises ton quotidien avec harmonie et ta communication au travail est diplomatique et collaborative.

## Ton moteur
Ta façon de penser le travail est orientée équipe et esthétique. Tu veux que l'environnement de travail soit agréable, les relations fluides.

## Ton défi
Éviter de t'épuiser à gérer les conflits des autres ou de ne pas t'affirmer assez dans tes méthodes de travail.

## Maison 6 en Balance
Tu abordes le travail quotidien avec diplomatie. Tes méthodes sont collaboratives, ta communication professionnelle est harmonieuse.

## Micro-rituel du jour (2 min)
- Identifie un conflit au travail que tu essaies de résoudre pour les autres
- Respire et définis ce qui est ta responsabilité et ce qui ne l'est pas
- Note une façon de préserver ton équilibre au travail aujourd'hui""",

    ('libra', 8): """# ☿️ Mercure en Balance

**En une phrase :** Tu réfléchis aux transformations profondes avec équilibre et tu explores les mystères en cherchant l'harmonie.

## Ton moteur
Ta façon de penser les crises est relationnelle et équilibrée. Tu analyses les dynamiques de pouvoir avec diplomatie.

## Ton défi
Éviter de fuir l'intensité des transformations pour maintenir une apparence d'harmonie ou de dépendre de l'autre pour traverser les crises.

## Maison 8 en Balance
Tu abordes l'intimité et les ressources partagées avec un mental de partenariat. Les discussions profondes cherchent l'équité.

## Micro-rituel du jour (2 min)
- Pense à une tension profonde que tu évites pour garder la paix
- Respire et trouve une façon de l'aborder avec diplomatie
- Note un sujet délicat à évoquer avec tact aujourd'hui""",

    ('libra', 9): """# ☿️ Mercure en Balance

**En une phrase :** Tu explores les grandes questions avec ouverture et ta sagesse cherche à réconcilier les points de vue.

## Ton moteur
Ta façon de penser la philosophie est comparative et harmonisante. Tu vois la valeur dans différentes visions du monde, tu cherches les ponts.

## Ton défi
Éviter de ne jamais choisir une voie ou de relativiser toutes les croyances au point de n'en avoir aucune.

## Maison 9 en Balance
Tu abordes les études supérieures et les voyages avec un mental de diplomate. Ta spiritualité cherche l'équilibre et l'harmonie universelle.

## Micro-rituel du jour (2 min)
- Identifie une conviction que tu n'oses pas défendre par souci d'équilibre
- Respire et assume cette croyance
- Note une façon de prendre position avec grâce aujourd'hui""",

    ('libra', 11): """# ☿️ Mercure en Balance

**En une phrase :** Tu communiques dans les groupes avec diplomatie et tes idées collectives visent l'harmonie de tous.

## Ton moteur
Ta façon de penser les projets collectifs est relationnelle et équitable. Tu fais le lien entre les personnes, tu facilites les échanges harmonieux.

## Ton défi
Éviter de t'épuiser à maintenir la paix du groupe ou de ne pas défendre tes propres idées pour éviter les conflits.

## Maison 11 en Balance
Tu abordes les amitiés et réseaux avec un mental de médiateur. Tes amis apprécient ta diplomatie, mais elle peut masquer tes vrais avis.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu joues le médiateur au détriment de toi
- Respire et définis ta propre position
- Note une façon de contribuer au groupe avec ton opinion vraie aujourd'hui""",

    ('libra', 12): """# ☿️ Mercure en Balance

**En une phrase :** Tu explores ton monde intérieur avec équilibre et ton mental cherche l'harmonie entre conscient et inconscient.

## Ton moteur
Ta façon de penser la spiritualité est relationnelle et esthétique. Tu médites pour trouver la paix, tu explores l'invisible avec grâce.

## Ton défi
Éviter de fuir les aspects sombres de toi-même pour maintenir une image harmonieuse ou de dépendre des autres pour ta vie intérieure.

## Maison 12 en Balance
Tu abordes le monde invisible avec un mental de paix. Tes retraites sont belles et harmonieuses, ta spiritualité cherche l'équilibre.

## Micro-rituel du jour (2 min)
- Identifie une part de toi que tu caches car elle te semble "pas belle"
- Respire et accueille-la avec la même grâce que le reste
- Note une façon de faire la paix avec ton ombre aujourd'hui""",

    # SCORPIO
    ('scorpio', 2): """# ☿️ Mercure en Scorpion

**En une phrase :** Tu penses à l'argent avec intensité et ton regard sur les ressources va au-delà des apparences.

## Ton moteur
Ta façon de réfléchir aux finances est stratégique et profonde. Tu vois les enjeux de pouvoir cachés, tu analyses les motivations réelles.

## Ton défi
Éviter la méfiance excessive ou l'obsession du contrôle financier. Tes ressources ne sont pas un champ de bataille.

## Maison 2 en Scorpion
Tu abordes l'argent avec un mental d'investigateur. Tes valeurs sont intenses, ton rapport aux possessions est transformatif.

## Micro-rituel du jour (2 min)
- Pense à une peur financière qui t'obsède
- Respire et identifie ce que tu contrôles vraiment
- Note une façon de détendre ton rapport à l'argent aujourd'hui""",

    ('scorpio', 3): """# ☿️ Mercure en Scorpion

**En une phrase :** Tu communiques avec profondeur et tes mots vont droit à l'essentiel, sans tabou.

## Ton moteur
Ta façon de réfléchir est pénétrante et stratégique. Tu vois ce que les autres cachent, tu poses les questions qui dérangent.

## Ton défi
Éviter la manipulation verbale ou la tendance à blesser par des vérités trop directes. Tout le monde n'est pas prêt pour ta profondeur.

## Maison 3 en Scorpion
Tu abordes la communication avec intensité. Tes échanges avec l'entourage sont profonds, tes apprentissages transformatifs.

## Micro-rituel du jour (2 min)
- Identifie une vérité que tu pourrais utiliser pour blesser
- Respire et trouve une façon de la dire avec compassion, ou de la garder
- Note une façon d'utiliser ta perspicacité pour aider aujourd'hui""",

    ('scorpio', 5): """# ☿️ Mercure en Scorpion

**En une phrase :** Tu exprimes ta créativité avec intensité et tes idées artistiques explorent les profondeurs de l'âme.

## Ton moteur
Ta façon de penser la créativité est transformative et cathartique. Tu crées pour exorciser, révéler, transformer.

## Ton défi
Éviter de te perdre dans les ténèbres créatives ou de repousser ceux qui ne comprennent pas ta profondeur.

## Maison 5 en Scorpion
Tu abordes les plaisirs et la créativité avec un mental intense. Tes romances sont passionnées et transformatives.

## Micro-rituel du jour (2 min)
- Pense à une émotion profonde que tu n'as pas encore exprimée créativement
- Respire et laisse-la trouver une forme
- Note une façon de créer à partir de ta profondeur aujourd'hui""",

    ('scorpio', 6): """# ☿️ Mercure en Scorpion

**En une phrase :** Tu organises ton quotidien avec stratégie et ta communication au travail va au cœur des problèmes.

## Ton moteur
Ta façon de penser le travail est analytique et transformative. Tu vois ce qui ne fonctionne pas, tu proposes des changements profonds.

## Ton défi
Éviter de créer des tensions par des vérités trop crues ou de te méfier excessivement de tes collègues.

## Maison 6 en Scorpion
Tu abordes le travail quotidien avec intensité. Tes méthodes sont stratégiques, ta communication professionnelle est directe.

## Micro-rituel du jour (2 min)
- Identifie une dynamique de travail qui te paraît malsaine
- Respire et demande-toi comment la transformer positivement
- Note une façon de contribuer à l'amélioration sans confrontation inutile""",

    ('scorpio', 8): """# ☿️ Mercure en Scorpion

**En une phrase :** Tu réfléchis aux transformations profondes avec une intensité naturelle, tu es chez toi dans les mystères.

## Ton moteur
Ta façon de penser les crises est courageuse et pénétrante. Tu n'as pas peur des ténèbres, tu comprends les tabous de l'intérieur.

## Ton défi
Éviter de te complaire dans les profondeurs ou de ne voir que les ombres là où il y a aussi de la lumière.

## Maison 8 en Scorpion
Position renforcée : tu es naturellement à l'aise avec les sujets profonds, l'intimité intense, les ressources partagées.

## Micro-rituel du jour (2 min)
- Pense à un aspect lumineux que tu négliges par fascination pour l'ombre
- Respire et accueille aussi la légèreté
- Note une façon d'équilibrer profondeur et lumière aujourd'hui""",

    ('scorpio', 9): """# ☿️ Mercure en Scorpion

**En une phrase :** Tu explores les grandes questions avec intensité et ta quête de vérité est radicale et sans compromis.

## Ton moteur
Ta façon de penser la philosophie est transformative et profonde. Tu cherches la vérité absolue, tu déconstruis les croyances superficielles.

## Ton défi
Éviter le fanatisme ou le rejet radical de ce qui ne passe pas ton test de profondeur. La sagesse inclut aussi la légèreté.

## Maison 9 en Scorpion
Tu abordes les études supérieures et les voyages avec un mental d'explorateur des profondeurs. Ta spiritualité est intense et transformative.

## Micro-rituel du jour (2 min)
- Identifie une croyance que tu rejettes car "trop superficielle"
- Respire et trouve ce qu'elle pourrait t'apprendre
- Note une façon d'être sage sans être trop sérieux aujourd'hui""",

    ('scorpio', 11): """# ☿️ Mercure en Scorpion

**En une phrase :** Tu communiques dans les groupes avec intensité et tes idées collectives visent la transformation profonde.

## Ton moteur
Ta façon de penser les projets collectifs est stratégique et engagée. Tu veux changer les choses en profondeur, pas en surface.

## Ton défi
Éviter de te méfier de tous dans le groupe ou de vouloir contrôler les dynamiques collectives par la manipulation.

## Maison 11 en Scorpion
Tu abordes les amitiés et réseaux avec un mental intense. Tes amis sont peu nombreux mais profonds, tes projets visent la transformation.

## Micro-rituel du jour (2 min)
- Pense à une amitié où tu te méfies secrètement
- Respire et choisis la confiance ou la clarification
- Note une façon de contribuer au groupe avec authenticité aujourd'hui""",

    ('scorpio', 12): """# ☿️ Mercure en Scorpion

**En une phrase :** Tu explores ton monde intérieur avec courage et ton mental n'a pas peur de descendre dans les profondeurs de l'inconscient.

## Ton moteur
Ta façon de penser la spiritualité est radicale et transformative. Tu médites pour mourir et renaître, tu explores tes ombres sans peur.

## Ton défi
Éviter de te perdre dans les abysses intérieurs ou de devenir obsédé par tes zones sombres au détriment de ta vie quotidienne.

## Maison 12 en Scorpion
Tu abordes le monde invisible avec un mental de chaman. Tes retraites sont transformatives, ta spiritualité est intense.

## Micro-rituel du jour (2 min)
- Identifie une obsession intérieure qui te consume
- Respire et laisse-la se transformer sans t'y accrocher
- Note une façon d'honorer ta profondeur avec légèreté aujourd'hui""",

    # SAGITTARIUS
    ('sagittarius', 2): """# ☿️ Mercure en Sagittaire

**En une phrase :** Tu penses à l'argent avec optimisme et tes idées financières sont généreuses et expansives.

## Ton moteur
Ta façon de réfléchir aux ressources est visionnaire et abondante. Tu vois grand, tu crois en la générosité de la vie.

## Ton défi
Éviter les risques financiers par excès d'optimisme ou la négligence des détails pratiques dans ta gestion.

## Maison 2 en Sagittaire
Tu abordes l'argent avec un mental d'aventurier. Tes valeurs sont expansives, ton rapport aux ressources est généreux.

## Micro-rituel du jour (2 min)
- Pense à un risque financier pris par excès d'optimisme
- Respire et identifie les détails que tu as négligés
- Note une façon d'allier vision large et gestion pratique aujourd'hui""",

    ('sagittarius', 3): """# ☿️ Mercure en Sagittaire

**En une phrase :** Tu communiques avec enthousiasme et tes mots portent des visions inspirantes du monde.

## Ton moteur
Ta façon de réfléchir est globale et philosophique. Tu vois le sens général, tu inspires par tes idées, tu parles de grands horizons.

## Ton défi
Éviter de promettre plus que tu ne peux tenir ou de négliger les détails au profit de la vision d'ensemble.

## Maison 3 en Sagittaire
Tu abordes la communication avec enthousiasme. Tes échanges avec l'entourage sont inspirants, tes apprentissages exploratoires.

## Micro-rituel du jour (2 min)
- Identifie une promesse que tu as faite sans mesurer les détails
- Respire et trouve comment l'honorer concrètement ou la renégocier
- Note une façon d'inspirer tout en restant réaliste aujourd'hui""",

    ('sagittarius', 5): """# ☿️ Mercure en Sagittaire

**En une phrase :** Tu exprimes ta créativité avec ampleur et tes idées artistiques ont une portée universelle.

## Ton moteur
Ta façon de penser la créativité est visionnaire et joyeuse. Tu crées pour inspirer, tes idées veulent toucher un large public.

## Ton défi
Éviter de te disperser dans trop de projets créatifs ou de négliger le travail de finition par impatience.

## Maison 5 en Sagittaire
Tu abordes les plaisirs et la créativité avec un mental d'explorateur. Tes romances sont des aventures, ta créativité est expansive.

## Micro-rituel du jour (2 min)
- Pense à un projet créatif laissé inachevé par impatience
- Respire et trouve la joie dans les finitions
- Note une façon de terminer quelque chose de créatif aujourd'hui""",

    ('sagittarius', 6): """# ☿️ Mercure en Sagittaire

**En une phrase :** Tu organises ton quotidien avec flexibilité et ta communication au travail inspire et motive.

## Ton moteur
Ta façon de penser le travail est orientée sens et mission. Tu veux que ton travail quotidien contribue à quelque chose de plus grand.

## Ton défi
Éviter de négliger les tâches routinières par manque d'intérêt ou de promettre plus que tu ne peux livrer.

## Maison 6 en Sagittaire
Tu abordes le travail quotidien avec une vision large. Tes méthodes sont flexibles, ta communication professionnelle est inspirante.

## Micro-rituel du jour (2 min)
- Identifie une tâche routinière que tu négliges
- Respire et trouve un sens plus large à cette tâche
- Note une façon de rendre ton quotidien plus aligné avec ta mission aujourd'hui""",

    ('sagittarius', 8): """# ☿️ Mercure en Sagittaire

**En une phrase :** Tu réfléchis aux transformations profondes avec foi et tu vois la croissance possible dans chaque crise.

## Ton moteur
Ta façon de penser les crises est optimiste et philosophique. Tu cherches le sens dans les épreuves, tu crois en la renaissance.

## Ton défi
Éviter de minimiser la souffrance par excès d'optimisme ou de fuir les profondeurs dans la quête de sens.

## Maison 8 en Sagittaire
Tu abordes l'intimité et les ressources partagées avec un mental de philosophe. Les discussions profondes cherchent le sens.

## Micro-rituel du jour (2 min)
- Pense à une épreuve dont tu minimises la difficulté
- Respire et accueille sa part de souffrance sans chercher à la transcender immédiatement
- Note une façon d'être présent à la douleur avec espoir aujourd'hui""",

    ('sagittarius', 9): """# ☿️ Mercure en Sagittaire

**En une phrase :** Tu explores les grandes questions avec passion native et ta quête de sens est le moteur de ta vie.

## Ton moteur
Ta façon de penser la philosophie est joyeuse et expansive. Tu veux tout explorer, tout comprendre, tout relier.

## Ton défi
Éviter de survoler trop de systèmes de pensée ou de croire avoir trouvé LA vérité à chaque nouvelle découverte.

## Maison 9 en Sagittaire
Position renforcée : tu es un chercheur de sens né, un voyageur de l'esprit, un philosophe enthousiaste.

## Micro-rituel du jour (2 min)
- Identifie une croyance que tu as adoptée avec enthousiasme récemment
- Respire et questionne-la avec la même curiosité que les autres
- Note une façon d'approfondir ta sagesse plutôt que de l'élargir aujourd'hui""",

    ('sagittarius', 11): """# ☿️ Mercure en Sagittaire

**En une phrase :** Tu communiques dans les groupes avec enthousiasme et tes idées collectives ont une vision mondiale.

## Ton moteur
Ta façon de penser les projets collectifs est visionnaire et inclusive. Tu veux que le groupe contribue à quelque chose de grand.

## Ton défi
Éviter de promettre au groupe plus que ce qui est réalisable ou de t'ennuyer quand les détails pratiques s'imposent.

## Maison 11 en Sagittaire
Tu abordes les amitiés et réseaux avec un mental d'explorateur social. Tes amis viennent de partout, tes projets sont internationaux.

## Micro-rituel du jour (2 min)
- Pense à un projet collectif trop ambitieux qui s'essouffle
- Respire et trouve une prochaine étape réaliste
- Note une façon de servir le groupe avec pragmatisme aujourd'hui""",

    ('sagittarius', 12): """# ☿️ Mercure en Sagittaire

**En une phrase :** Tu explores ton monde intérieur avec foi et ton mental cherche le sens même dans l'invisible.

## Ton moteur
Ta façon de penser la spiritualité est optimiste et exploratoire. Tu médites pour t'expanser, tu cherches la sagesse partout.

## Ton défi
Éviter de fuir l'introspection profonde dans une quête spirituelle toujours nouvelle ou de négliger les ombres.

## Maison 12 en Sagittaire
Tu abordes le monde invisible avec un mental de chercheur spirituel. Tes retraites sont des voyages, ta spiritualité est joyeuse.

## Micro-rituel du jour (2 min)
- Identifie une part sombre de toi que tu évites par la quête de lumière
- Respire et accueille cette ombre avec la même curiosité
- Note une façon d'intégrer l'ombre dans ta spiritualité aujourd'hui""",

    # CAPRICORN
    ('capricorn', 2): """# ☿️ Mercure en Capricorne

**En une phrase :** Tu penses à l'argent avec sérieux et tes stratégies financières sont construites pour durer.

## Ton moteur
Ta façon de réfléchir aux ressources est pragmatique et ambitieuse. Tu planifies à long terme, tu construis pas à pas.

## Ton défi
Éviter l'anxiété liée à l'argent ou la rigidité qui t'empêche de saisir les opportunités imprévues.

## Maison 2 en Capricorne
Tu abordes l'argent avec un mental de bâtisseur. Tes valeurs sont solides, ton rapport aux ressources est responsable.

## Micro-rituel du jour (2 min)
- Pense à une opportunité financière que tu as ignorée par prudence excessive
- Respire et évalue si le risque était vraiment trop grand
- Note une façon d'allier sécurité et ouverture aujourd'hui""",

    ('capricorn', 3): """# ☿️ Mercure en Capricorne

**En une phrase :** Tu communiques avec autorité et tes mots sont mesurés, structurés et efficaces.

## Ton moteur
Ta façon de réfléchir est méthodique et orientée résultats. Tu parles quand c'est utile, tu apprends avec discipline.

## Ton défi
Éviter la froideur dans la communication ou le pessimisme qui décourage les autres. Tes mots peuvent sembler durs.

## Maison 3 en Capricorne
Tu abordes la communication avec sérieux. Tes échanges avec l'entourage sont structurés, tes apprentissages méthodiques.

## Micro-rituel du jour (2 min)
- Identifie une communication récente perçue comme froide
- Respire et trouve une façon d'ajouter de la chaleur à ton propos
- Note une façon de communiquer avec fermeté ET bienveillance aujourd'hui""",

    ('capricorn', 5): """# ☿️ Mercure en Capricorne

**En une phrase :** Tu exprimes ta créativité avec structure et tes idées artistiques ont une ambition professionnelle.

## Ton moteur
Ta façon de penser la créativité est disciplinée et orientée maîtrise. Tu travailles ton art avec patience, tu vises l'excellence.

## Ton défi
Éviter de tuer la spontanéité créative par excès de sérieux ou de ne valoriser que la créativité "utile".

## Maison 5 en Capricorne
Tu abordes les plaisirs et la créativité avec un mental sérieux. Tes romances sont réfléchies, ta créativité est ambitieuse.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as jugé ta créativité "pas assez sérieuse"
- Respire et autorise-toi à créer pour le plaisir
- Note une façon de jouer sans objectif aujourd'hui""",

    ('capricorn', 6): """# ☿️ Mercure en Capricorne

**En une phrase :** Tu organises ton quotidien avec discipline et ta communication au travail est professionnelle et efficace.

## Ton moteur
Ta façon de penser le travail est structurée et ambitieuse. Tu vises l'efficacité, tu respectes les processus, tu construis ta carrière.

## Ton défi
Éviter le workaholisme mental ou la difficulté à déléguer par manque de confiance envers les autres.

## Maison 6 en Capricorne
Tu abordes le travail quotidien avec sérieux et professionnalisme. Tes méthodes sont éprouvées, ta communication est formelle.

## Micro-rituel du jour (2 min)
- Identifie une tâche que tu refuses de déléguer
- Respire et trouve quelqu'un à qui la confier
- Note une façon de te reposer mentalement au travail aujourd'hui""",

    ('capricorn', 8): """# ☿️ Mercure en Capricorne

**En une phrase :** Tu réfléchis aux transformations profondes avec réalisme et tu traverses les crises avec stratégie.

## Ton moteur
Ta façon de penser les crises est pragmatique et résiliente. Tu analyses froidement, tu planifies la renaissance.

## Ton défi
Éviter de contrôler les transformations au point de les bloquer ou de réprimer les émotions au profit de la stratégie.

## Maison 8 en Capricorne
Tu abordes l'intimité et les ressources partagées avec un mental de gestionnaire. Les discussions profondes sont structurées.

## Micro-rituel du jour (2 min)
- Pense à une transformation que tu essaies de contrôler entièrement
- Respire et accepte la part d'inconnu
- Note une façon de lâcher prise dans une situation intense aujourd'hui""",

    ('capricorn', 9): """# ☿️ Mercure en Capricorne

**En une phrase :** Tu explores les grandes questions avec méthode et ta sagesse est construite sur l'expérience et la tradition.

## Ton moteur
Ta façon de penser la philosophie est réaliste et respectueuse des traditions. Tu préfères les sagesses éprouvées aux modes spirituelles.

## Ton défi
Éviter le cynisme face aux nouvelles idées ou la fermeture à ce qui ne semble pas "sérieux" ou "traditionnel".

## Maison 9 en Capricorne
Tu abordes les études supérieures et les voyages avec un mental structuré. Ta spiritualité est sérieuse et disciplinée.

## Micro-rituel du jour (2 min)
- Identifie une nouvelle idée spirituelle que tu rejettes car "pas sérieuse"
- Respire et explore-la avec curiosité
- Note une façon d'être sage sans être rigide aujourd'hui""",

    ('capricorn', 11): """# ☿️ Mercure en Capricorne

**En une phrase :** Tu communiques dans les groupes avec autorité et tes idées collectives sont réalistes et structurées.

## Ton moteur
Ta façon de penser les projets collectifs est organisatrice et ambitieuse. Tu veux que le groupe réussisse concrètement.

## Ton défi
Éviter de devenir trop directif ou de décourager les idées "irréalistes" des autres qui pourraient enrichir le groupe.

## Maison 11 en Capricorne
Tu abordes les amitiés et réseaux avec un mental professionnel. Tes amis sont souvent liés à ta carrière, tes projets sont ambitieux.

## Micro-rituel du jour (2 min)
- Pense à une idée de groupe que tu as jugée "irréaliste"
- Respire et trouve un aspect qui pourrait fonctionner
- Note une façon d'encourager plutôt que de tempérer aujourd'hui""",

    ('capricorn', 12): """# ☿️ Mercure en Capricorne

**En une phrase :** Tu explores ton monde intérieur avec discipline et ton mental cherche à structurer même l'invisible.

## Ton moteur
Ta façon de penser la spiritualité est sérieuse et pratique. Tu médites avec discipline, ta vie intérieure est organisée.

## Ton défi
Éviter de fuir l'introspection dans le travail ou de vouloir "réussir" ta vie spirituelle comme une carrière.

## Maison 12 en Capricorne
Tu abordes le monde invisible avec un mental de constructeur. Tes retraites sont disciplinées, ta spiritualité est sérieuse.

## Micro-rituel du jour (2 min)
- Identifie un objectif spirituel que tu traites comme un projet professionnel
- Respire et laisse ta vie intérieure simplement être
- Note une façon de méditer sans but aujourd'hui""",

    # AQUARIUS
    ('aquarius', 2): """# ☿️ Mercure en Verseau

**En une phrase :** Tu penses à l'argent de façon originale et tes idées financières sont innovantes et anticonformistes.

## Ton moteur
Ta façon de réfléchir aux ressources est progressiste et indépendante. Tu explores les nouvelles façons de gagner et d'utiliser l'argent.

## Ton défi
Éviter l'instabilité financière par rejet des méthodes traditionnelles ou le détachement excessif vis-à-vis des besoins matériels.

## Maison 2 en Verseau
Tu abordes l'argent avec un mental d'innovateur. Tes valeurs sont progressistes, ton rapport aux ressources est libre.

## Micro-rituel du jour (2 min)
- Pense à une méthode financière traditionnelle que tu rejettes
- Respire et trouve ce qu'elle pourrait t'apporter
- Note une façon d'innover tout en restant ancré aujourd'hui""",

    ('aquarius', 3): """# ☿️ Mercure en Verseau

**En une phrase :** Tu communiques avec originalité et tes idées sont en avance sur leur temps.

## Ton moteur
Ta façon de réfléchir est non-conventionnelle et visionnaire. Tu vois les systèmes, les réseaux, les possibilités futures.

## Ton défi
Éviter de paraître trop détaché ou bizarre dans ta communication, ou de rejeter les idées "ordinaires" par principe.

## Maison 3 en Verseau
Tu abordes la communication avec originalité. Tes échanges avec l'entourage sont stimulants, tes apprentissages innovants.

## Micro-rituel du jour (2 min)
- Identifie une idée "ordinaire" que tu as rejetée trop vite
- Respire et trouve sa valeur
- Note une façon de connecter innovation et tradition aujourd'hui""",

    ('aquarius', 5): """# ☿️ Mercure en Verseau

**En une phrase :** Tu exprimes ta créativité avec originalité et tes idées artistiques défient les conventions.

## Ton moteur
Ta façon de penser la créativité est expérimentale et libre. Tu crées pour innover, pour choquer, pour faire avancer les idées.

## Ton défi
Éviter de créer uniquement pour être différent ou de rejeter les formes créatives classiques par principe.

## Maison 5 en Verseau
Tu abordes les plaisirs et la créativité avec un mental d'avant-garde. Tes romances sont libres, ta créativité est inventive.

## Micro-rituel du jour (2 min)
- Pense à une forme d'art classique que tu négliges
- Respire et explore-la avec curiosité
- Note une façon de créer en honorant le passé et le futur aujourd'hui""",

    ('aquarius', 6): """# ☿️ Mercure en Verseau

**En une phrase :** Tu organises ton quotidien de façon non-conventionnelle et ta communication au travail est innovante.

## Ton moteur
Ta façon de penser le travail est orientée systèmes et amélioration. Tu vois comment optimiser, automatiser, révolutionner.

## Ton défi
Éviter de rejeter les méthodes de travail établies par principe ou de te déconnecter émotionnellement de ton équipe.

## Maison 6 en Verseau
Tu abordes le travail quotidien avec un mental d'innovateur. Tes méthodes sont originales, ta communication professionnelle est progressiste.

## Micro-rituel du jour (2 min)
- Identifie une routine de travail "traditionnelle" que tu rejettes
- Respire et trouve ce qu'elle a de bon
- Note une façon d'améliorer le système avec pragmatisme aujourd'hui""",

    ('aquarius', 8): """# ☿️ Mercure en Verseau

**En une phrase :** Tu réfléchis aux transformations profondes avec détachement et tu explores les mystères avec curiosité scientifique.

## Ton moteur
Ta façon de penser les crises est analytique et progressiste. Tu vois les transformations comme des opportunités d'évolution.

## Ton défi
Éviter le détachement excessif face à l'intensité émotionnelle ou l'intellectualisation des expériences profondes.

## Maison 8 en Verseau
Tu abordes l'intimité et les ressources partagées avec un mental libre. Les discussions profondes sont originales et détachées.

## Micro-rituel du jour (2 min)
- Pense à une émotion intense que tu as rationalisée
- Respire et laisse-toi la ressentir pleinement
- Note une façon de vivre l'intensité sans la disséquer aujourd'hui""",

    ('aquarius', 9): """# ☿️ Mercure en Verseau

**En une phrase :** Tu explores les grandes questions avec originalité et ta vision du monde est progressiste et humaniste.

## Ton moteur
Ta façon de penser la philosophie est universaliste et tournée vers le futur. Tu crois au progrès, à l'humanité, à l'évolution.

## Ton défi
Éviter de rejeter toutes les traditions spirituelles ou de confondre nouveauté et vérité.

## Maison 9 en Verseau
Tu abordes les études supérieures et les voyages avec un mental de visionnaire. Ta spiritualité est universelle et progressiste.

## Micro-rituel du jour (2 min)
- Identifie une tradition spirituelle que tu rejettes car "dépassée"
- Respire et trouve la sagesse qu'elle contient
- Note une façon d'honorer le passé tout en regardant vers l'avenir aujourd'hui""",

    ('aquarius', 11): """# ☿️ Mercure en Verseau

**En une phrase :** Tu communiques dans les groupes avec brillance et tes idées collectives visent le progrès de l'humanité.

## Ton moteur
Ta façon de penser les projets collectifs est visionnaire et réseau. Tu connectes les idées, les personnes, les possibilités.

## Ton défi
Éviter de te perdre dans les grandes idées au détriment des relations humaines concrètes ou de paraître trop distant.

## Maison 11 en Verseau
Position renforcée : tu es un connecteur social, un visionnaire collectif, un innovateur au service du groupe.

## Micro-rituel du jour (2 min)
- Pense à un ami avec qui tu partages des idées mais peu d'émotions
- Respire et trouve une façon de te connecter humainement
- Note une façon d'allier vision et présence relationnelle aujourd'hui""",

    ('aquarius', 12): """# ☿️ Mercure en Verseau

**En une phrase :** Tu explores ton monde intérieur avec curiosité et ton mental découvre l'inconscient collectif.

## Ton moteur
Ta façon de penser la spiritualité est universelle et non-conventionnelle. Tu médites pour te connecter à plus grand, tu explores les états de conscience.

## Ton défi
Éviter de fuir dans les concepts spirituels abstraits ou de te détacher de ta vie intérieure personnelle.

## Maison 12 en Verseau
Tu abordes le monde invisible avec un mental d'explorateur cosmique. Tes retraites sont originales, ta spiritualité est universelle.

## Micro-rituel du jour (2 min)
- Identifie une pratique spirituelle personnelle que tu négliges au profit de l'universel
- Respire et reconnecte-toi à ton chemin unique
- Note une façon d'honorer ton inconscient personnel aujourd'hui""",

    # PISCES
    ('pisces', 2): """# ☿️ Mercure en Poissons

**En une phrase :** Tu penses à l'argent de façon intuitive et tes ressources sont liées à ta foi et ta compassion.

## Ton moteur
Ta façon de réfléchir aux finances est fluide et généreuse. Tu donnes facilement, tu fais confiance à l'univers pour tes besoins.

## Ton défi
Éviter le flou financier ou la naïveté qui te rend vulnérable aux abus. Les limites matérielles sont importantes.

## Maison 2 en Poissons
Tu abordes l'argent avec un mental intuitif et généreux. Tes valeurs sont spirituelles, ton rapport aux ressources est fluide.

## Micro-rituel du jour (2 min)
- Pense à une situation financière où tu as été trop confiant
- Respire et identifie les limites nécessaires
- Note une façon d'allier générosité et discernement aujourd'hui""",

    ('pisces', 3): """# ☿️ Mercure en Poissons

**En une phrase :** Tu communiques avec poésie et tes mots portent l'invisible et l'indicible.

## Ton moteur
Ta façon de réfléchir est intuitive et symbolique. Tu captes les ambiances, tu parles par images, tu comprends au-delà des mots.

## Ton défi
Éviter le flou dans ta communication ou la difficulté à être concret et direct quand c'est nécessaire.

## Maison 3 en Poissons
Tu abordes la communication avec sensibilité poétique. Tes échanges avec l'entourage sont empathiques, tes apprentissages intuitifs.

## Micro-rituel du jour (2 min)
- Identifie une communication qui a été mal comprise car trop floue
- Respire et trouve des mots plus concrets
- Note une façon d'être poétique ET clair aujourd'hui""",

    ('pisces', 5): """# ☿️ Mercure en Poissons

**En une phrase :** Tu exprimes ta créativité avec fluidité et tes idées artistiques viennent d'un ailleurs mystérieux.

## Ton moteur
Ta façon de penser la créativité est inspirée et transcendante. Tu crées comme on canalise, tu es un véhicule pour quelque chose de plus grand.

## Ton défi
Éviter de te perdre dans les rêves créatifs sans jamais concrétiser ou de douter de ton inspiration car "pas rationnelle".

## Maison 5 en Poissons
Tu abordes les plaisirs et la créativité avec un mental de rêveur. Tes romances sont idéalisées, ta créativité est inspirée.

## Micro-rituel du jour (2 min)
- Pense à une inspiration créative que tu as ignorée car pas "logique"
- Respire et laisse-la s'exprimer
- Note une façon de créer à partir de tes rêves aujourd'hui""",

    ('pisces', 6): """# ☿️ Mercure en Poissons

**En une phrase :** Tu organises ton quotidien avec fluidité et ta communication au travail est empathique et intuitive.

## Ton moteur
Ta façon de penser le travail est orientée service et compassion. Tu sens les besoins des autres, tu t'adaptes avec fluidité.

## Ton défi
Éviter le chaos organisationnel ou la tendance à absorber les problèmes des autres au travail.

## Maison 6 en Poissons
Tu abordes le travail quotidien avec un mental de guérisseur. Tes méthodes sont intuitives, ta communication professionnelle est compatissante.

## Micro-rituel du jour (2 min)
- Identifie un problème de collègue que tu portes comme le tien
- Respire et rends-lui ce qui lui appartient
- Note une limite à poser au travail aujourd'hui""",

    ('pisces', 8): """# ☿️ Mercure en Poissons

**En une phrase :** Tu réfléchis aux transformations profondes avec intuition et tu navigues dans les mystères avec fluidité.

## Ton moteur
Ta façon de penser les crises est mystique et acceptante. Tu sens ce qui doit mourir, tu accueilles la renaissance avec foi.

## Ton défi
Éviter de te perdre dans les abysses émotionnels ou de fusionner avec la souffrance au point de t'y noyer.

## Maison 8 en Poissons
Tu abordes l'intimité et les ressources partagées avec un mental intuitif. Les discussions profondes sont mystiques et transcendantes.

## Micro-rituel du jour (2 min)
- Pense à une souffrance dans laquelle tu te noies
- Respire et trouve la rive, le sol sous tes pieds
- Note une façon de traverser les eaux profondes avec un ancrage aujourd'hui""",

    ('pisces', 9): """# ☿️ Mercure en Poissons

**En une phrase :** Tu explores les grandes questions avec mysticisme et ta sagesse vient de sources invisibles.

## Ton moteur
Ta façon de penser la philosophie est intuitive et unitaire. Tu sens l'unité de tout, tu comprends au-delà de la raison.

## Ton défi
Éviter la confusion spirituelle ou la difficulté à discerner entre vraie sagesse et illusion.

## Maison 9 en Poissons
Tu abordes les études supérieures et les voyages avec un mental de mystique. Ta spiritualité est intuitive et universelle.

## Micro-rituel du jour (2 min)
- Identifie une croyance que tu n'as jamais vraiment questionnée
- Respire et passe-la au filtre du discernement
- Note une façon d'allier foi et clarté aujourd'hui""",

    ('pisces', 11): """# ☿️ Mercure en Poissons

**En une phrase :** Tu communiques dans les groupes avec empathie et tes idées collectives visent la compassion universelle.

## Ton moteur
Ta façon de penser les projets collectifs est inclusive et compatissante. Tu sens les besoins du groupe, tu inspires par ta sensibilité.

## Ton défi
Éviter de te perdre dans les idéaux collectifs irréalistes ou d'absorber les émotions du groupe au détriment de toi.

## Maison 11 en Poissons
Tu abordes les amitiés et réseaux avec un mental de rêveur. Tes amis sont des âmes sœurs, tes projets visent la guérison collective.

## Micro-rituel du jour (2 min)
- Pense à un projet de groupe où tu as porté les émotions de tous
- Respire et définis ce qui est ta responsabilité
- Note une façon de contribuer au groupe sans t'y dissoudre aujourd'hui""",

    ('pisces', 12): """# ☿️ Mercure en Poissons

**En une phrase :** Tu explores ton monde intérieur avec fluidité native et ton mental navigue naturellement entre les dimensions.

## Ton moteur
Ta façon de penser la spiritualité est transcendante et unitaire. Tu médites pour dissoudre les frontières, tu rêves de façon significative.

## Ton défi
Éviter de fuir la réalité dans les mondes intérieurs ou de perdre ton ancrage dans le quotidien.

## Maison 12 en Poissons
Position renforcée : tu es naturellement connecté à l'invisible, au rêve, à la transcendance. Ta vie intérieure est ton vrai foyer.

## Micro-rituel du jour (2 min)
- Identifie un moment où tu as fui la réalité dans tes rêves
- Respire et trouve une façon de ramener la magie dans le concret
- Note une façon d'être ancré tout en restant connecté à l'invisible aujourd'hui""",
}


async def main():
    async with AsyncSessionLocal() as db:
        count = 0
        for (sign, house), content in MERCURY_INTERPRETATIONS.items():
            result = await db.execute(
                update(PregeneratedNatalInterpretation)
                .where(
                    PregeneratedNatalInterpretation.subject == 'mercury',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house
                )
                .values(content=content)
            )
            if result.rowcount > 0:
                count += result.rowcount

        await db.commit()
        print(f"Done: {count} mercury interpretations updated")


if __name__ == "__main__":
    asyncio.run(main())
