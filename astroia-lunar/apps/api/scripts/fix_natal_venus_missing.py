#!/usr/bin/env python3
"""
Script pour corriger les 96 interprétations VENUS manquantes (maisons 2,3,5,6,8,9,11,12)
Format natal V2 avec: En une phrase / Ton moteur / Ton défi / Maison X / Micro-rituel
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import update
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

# Interprétations VENUS format V2 - Maisons 2,3,5,6,8,9,11,12 pour les 12 signes
VENUS_INTERPRETATIONS = {
    # ARIES
    ('aries', 2): """# ♀️ Vénus en Bélier

**En une phrase :** Tu trouves la beauté dans l'action et tes valeurs sont liées à l'indépendance et à la conquête.

## Ton moteur
Ta façon d'aimer les choses matérielles est directe et passionnée. Tu es attiré par ce qui est nouveau, audacieux, pionnier. Tu aimes acquérir rapidement.

## Ton défi
Éviter les achats impulsifs ou l'attachement à des possessions qui symbolisent ta victoire plutôt que ta vraie valeur.

## Maison 2 en Bélier
Tu abordes l'argent et les ressources avec une énergie de conquérant. Tu veux gagner par toi-même, vite et avec panache.

## Micro-rituel du jour (2 min)
- Pense à un achat récent fait par impulsion
- Respire et demande-toi s'il reflète vraiment tes valeurs profondes
- Note une façon de valoriser ce que tu as déjà aujourd'hui""",

    ('aries', 3): """# ♀️ Vénus en Bélier

**En une phrase :** Tu communiques ton affection de façon directe et spontanée, sans détour ni hésitation.

## Ton moteur
Ta façon d'exprimer l'amour est franche et enthousiaste. Tu charmes par ton énergie, ta vivacité, ta capacité à prendre l'initiative dans les échanges.

## Ton défi
Éviter d'être trop brusque dans tes déclarations ou d'oublier que les autres ont besoin de douceur et de patience.

## Maison 3 en Bélier
Tu communiques ton amour avec fougue. Tes échanges affectifs avec l'entourage sont directs, stimulants, parfois vifs.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as été trop direct dans une déclaration affectueuse
- Respire et trouve une façon plus douce de dire la même chose
- Note une attention délicate à offrir à quelqu'un de proche aujourd'hui""",

    ('aries', 5): """# ♀️ Vénus en Bélier

**En une phrase :** Tu aimes avec passion et ta créativité s'exprime dans l'action spontanée et audacieuse.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est intense et conquérante. Tu aimes la nouveauté, l'excitation, le frisson de la poursuite.

## Ton défi
Éviter de te lasser trop vite des relations ou de confondre passion et amour durable. L'enthousiasme initial doit trouver un second souffle.

## Maison 5 en Bélier
Tu abordes les romances et la créativité avec feu. Tes amours sont des aventures, ta créativité est impulsive et énergique.

## Micro-rituel du jour (2 min)
- Pense à une relation que tu as abandonnée quand l'excitation est retombée
- Respire et trouve ce qui pourrait raviver la flamme différemment
- Note une façon de créer ou d'aimer avec patience aujourd'hui""",

    ('aries', 6): """# ♀️ Vénus en Bélier

**En une phrase :** Tu apportes de la beauté et de l'harmonie au quotidien par l'action et l'initiative.

## Ton moteur
Ta façon de rendre le travail agréable est d'y mettre de l'énergie et du dynamisme. Tu aimes les environnements actifs, stimulants.

## Ton défi
Éviter de créer des tensions par impatience ou de négliger les aspects relationnels du travail au profit de l'efficacité.

## Maison 6 en Bélier
Tu abordes le service et la routine avec enthousiasme. Tu veux que le quotidien soit vivant, pas monotone.

## Micro-rituel du jour (2 min)
- Identifie une relation de travail que tu négliges par focus sur l'action
- Respire et trouve un geste de connexion
- Note une façon d'embellir ton quotidien avec douceur aujourd'hui""",

    ('aries', 8): """# ♀️ Vénus en Bélier

**En une phrase :** Tu vis l'intimité avec intensité et ton amour se révèle pleinement dans la passion et la transformation.

## Ton moteur
Ta façon d'aimer en profondeur est directe et courageuse. Tu n'as pas peur de l'intensité, tu plonges tête la première dans les eaux profondes.

## Ton défi
Éviter de confondre passion brûlante et intimité durable, ou de fuir quand l'intensité demande de la vulnérabilité.

## Maison 8 en Bélier
Tu abordes les ressources partagées et l'intimité avec courage. Les discussions financières avec ton partenaire sont directes.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as fui l'intimité quand elle devenait trop vulnérable
- Respire et accueille cette vulnérabilité
- Note une façon de montrer ton amour par la présence plutôt que l'action aujourd'hui""",

    ('aries', 9): """# ♀️ Vénus en Bélier

**En une phrase :** Tu trouves la beauté dans l'aventure et tes valeurs sont liées à la liberté et à l'exploration.

## Ton moteur
Ta façon d'aimer les grandes idées est passionnée et engagée. Tu es attiré par les visions audacieuses, les voyages qui t'excitent.

## Ton défi
Éviter de chercher toujours plus loin au lieu d'approfondir ou de confondre mouvement et évolution.

## Maison 9 en Bélier
Tu abordes les voyages et la philosophie avec enthousiasme. Ta spiritualité aime l'aventure et les nouvelles frontières.

## Micro-rituel du jour (2 min)
- Pense à une croyance ou un lieu que tu n'as pas approfondi car déjà attiré ailleurs
- Respire et trouve la beauté dans l'exploration verticale
- Note une façon d'aimer ce qui est proche aujourd'hui""",

    ('aries', 11): """# ♀️ Vénus en Bélier

**En une phrase :** Tu apportes charme et énergie aux groupes et tes amitiés sont vivantes et stimulantes.

## Ton moteur
Ta façon d'être ami est dynamique et enthousiaste. Tu initie les sorties, tu crées l'élan, tu charmes par ton énergie.

## Ton défi
Éviter de vouloir toujours mener les activités de groupe ou de te lasser des amitiés qui ne t'excitent plus.

## Maison 11 en Bélier
Tu abordes les amitiés et projets collectifs avec feu. Tes amis apprécient ton dynamisme, tes idéaux sont ambitieux.

## Micro-rituel du jour (2 min)
- Pense à un ami dont tu te rapproches moins car "moins excitant"
- Respire et trouve une qualité à apprécier chez lui
- Note une façon de soutenir un ami sans prendre les devants aujourd'hui""",

    ('aries', 12): """# ♀️ Vénus en Bélier

**En une phrase :** Tu trouves la beauté dans les combats intérieurs et ton amour de soi se révèle dans le courage de l'ombre.

## Ton moteur
Ta façon d'aimer l'invisible est active et courageuse. Tu affrontes tes zones d'ombre avec détermination, tu transformes la souffrance en force.

## Ton défi
Éviter de fuir l'introspection par l'hyperactivité ou de combattre des démons qui demandent plutôt de l'acceptation.

## Maison 12 en Bélier
Tu abordes le monde intérieur avec courage. Tes retraites spirituelles sont actives, ta compassion est directe.

## Micro-rituel du jour (2 min)
- Identifie une part de toi que tu combats au lieu de l'aimer
- Respire et envoie-lui de la tendresse
- Note une façon de t'aimer dans ta vulnérabilité aujourd'hui""",

    # TAURUS
    ('taurus', 2): """# ♀️ Vénus en Taureau

**En une phrase :** Tu trouves la beauté dans la stabilité et tes valeurs sont ancrées dans le plaisir sensoriel et la sécurité.

## Ton moteur
Ta façon d'aimer les choses matérielles est profonde et sensuelle. Tu apprécies la qualité, la durabilité, le confort tangible.

## Ton défi
Éviter l'attachement excessif aux possessions ou la peur du changement qui t'enferme dans le confort connu.

## Maison 2 en Taureau
Position renforcée : ton rapport à l'argent et aux ressources est naturellement harmonieux, sensoriel et stable.

## Micro-rituel du jour (2 min)
- Pense à un objet auquel tu t'accroches par peur du manque
- Respire et reconnais que ta valeur ne dépend pas de tes possessions
- Note une façon de te sentir riche par les sens aujourd'hui""",

    ('taurus', 3): """# ♀️ Vénus en Taureau

**En une phrase :** Tu communiques ton affection avec douceur et tes mots portent la chaleur du confort et de la fidélité.

## Ton moteur
Ta façon d'exprimer l'amour est stable et rassurante. Tu charmes par ta présence apaisante, ta voix, ta constance dans les échanges.

## Ton défi
Éviter de t'entêter dans tes expressions affectives ou de résister aux nouvelles façons de communiquer l'amour.

## Maison 3 en Taureau
Tu communiques ton affection avec lenteur et profondeur. Tes échanges avec l'entourage sont chaleureux et fiables.

## Micro-rituel du jour (2 min)
- Pense à une nouvelle façon d'exprimer ton affection que tu résistes à essayer
- Respire et ouvre-toi à cette possibilité
- Note une façon de dire "je t'aime" autrement aujourd'hui""",

    ('taurus', 5): """# ♀️ Vénus en Taureau

**En une phrase :** Tu aimes avec constance et ta créativité s'exprime dans la beauté tangible et sensuelle.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est profonde et patiente. Tu construis des romances durables, tu crées des œuvres qui se touchent.

## Ton défi
Éviter de t'accrocher à des relations par confort ou de bloquer ta créativité par trop de perfectionnisme sensoriel.

## Maison 5 en Taureau
Tu abordes les romances et la créativité avec sensualité. Tes amours sont fidèles, ta créativité est artisanale et belle.

## Micro-rituel du jour (2 min)
- Pense à une création que tu n'as pas terminée car "pas assez parfaite"
- Respire et accepte une beauté imparfaite
- Note une façon de créer avec tes mains aujourd'hui""",

    ('taurus', 6): """# ♀️ Vénus en Taureau

**En une phrase :** Tu apportes de la beauté au quotidien par le confort, la qualité et l'attention aux plaisirs simples.

## Ton moteur
Ta façon de rendre le travail agréable est d'y créer du confort et de la stabilité. Tu aimes les environnements beaux et apaisants.

## Ton défi
Éviter de t'enliser dans des routines confortables qui ne te font plus grandir ou de résister aux changements nécessaires.

## Maison 6 en Taureau
Tu abordes le service et la routine avec sensualité. Tu veux que le quotidien soit beau, stable et agréable aux sens.

## Micro-rituel du jour (2 min)
- Identifie une routine que tu gardes par confort mais qui ne te nourrit plus
- Respire et ose un petit changement
- Note une façon d'embellir ton espace de travail aujourd'hui""",

    ('taurus', 8): """# ♀️ Vénus en Taureau

**En une phrase :** Tu vis l'intimité avec profondeur sensorielle et ton amour se révèle dans la présence corporelle et la constance.

## Ton moteur
Ta façon d'aimer en profondeur est ancrée et tactile. Tu construis l'intimité lentement, avec patience et présence physique.

## Ton défi
Éviter de t'accrocher aux formes anciennes de l'intimité ou de résister aux transformations que demande l'amour profond.

## Maison 8 en Taureau
Tu abordes les ressources partagées et l'intimité avec stabilité. Les discussions financières communes sont concrètes et prudentes.

## Micro-rituel du jour (2 min)
- Pense à une transformation dans ta vie intime que tu résistes à accueillir
- Respire et accepte que l'amour profond change
- Note une façon de montrer ton amour par la présence physique aujourd'hui""",

    ('taurus', 9): """# ♀️ Vénus en Taureau

**En une phrase :** Tu trouves la beauté dans les vérités ancrées et tes valeurs spirituelles sont liées à la nature et au tangible.

## Ton moteur
Ta façon d'aimer les grandes idées est concrète et sensorielle. Tu préfères les sagesses qui s'incarnent, les philosophies qui se vivent.

## Ton défi
Éviter de rejeter les idées abstraites ou de t'enfermer dans des croyances confortables qui ne te font plus évoluer.

## Maison 9 en Taureau
Tu abordes les voyages et la philosophie avec sensualité. Ta spiritualité aime la nature, tes voyages sont gourmands.

## Micro-rituel du jour (2 min)
- Pense à une idée spirituelle abstraite que tu rejettes
- Respire et trouve comment elle pourrait s'incarner
- Note une façon de vivre ta spiritualité dans le corps aujourd'hui""",

    ('taurus', 11): """# ♀️ Vénus en Taureau

**En une phrase :** Tu apportes stabilité et chaleur aux groupes et tes amitiés sont durables et nourrissantes.

## Ton moteur
Ta façon d'être ami est fidèle et généreuse. Tu es là pour la durée, tu nourris tes amis, tu crées des liens solides.

## Ton défi
Éviter de t'accrocher à des amitiés par habitude ou de résister aux nouveaux amis qui pourraient t'enrichir.

## Maison 11 en Taureau
Tu abordes les amitiés et projets collectifs avec constance. Tes amis sont peu nombreux mais solides, tes idéaux sont concrets.

## Micro-rituel du jour (2 min)
- Pense à une nouvelle amitié potentielle que tu négliges par confort avec l'ancien cercle
- Respire et ouvre une porte
- Note une façon de nourrir une amitié existante aujourd'hui""",

    ('taurus', 12): """# ♀️ Vénus en Taureau

**En une phrase :** Tu trouves la beauté dans le silence sensoriel et ton amour de soi se révèle dans l'ancrage et la paix intérieure.

## Ton moteur
Ta façon d'aimer l'invisible est incarnée et paisible. Tu médites mieux dans la nature, tu trouves le sacré dans les sensations.

## Ton défi
Éviter de fuir l'introspection dans le confort matériel ou de t'attacher à des formes de spiritualité rassurantes mais limitantes.

## Maison 12 en Taureau
Tu abordes le monde intérieur avec sensualité. Tes retraites sont confortables, ta compassion est terrestre et nourrissante.

## Micro-rituel du jour (2 min)
- Identifie une fuite dans le confort matériel quand l'âme demande attention
- Respire et accorde-toi un moment d'intériorité sensorielle
- Note une façon de méditer dans le corps aujourd'hui""",

    # GEMINI
    ('gemini', 2): """# ♀️ Vénus en Gémeaux

**En une phrase :** Tu trouves la beauté dans la variété et tes valeurs sont liées à la curiosité et à la légèreté.

## Ton moteur
Ta façon d'aimer les choses matérielles est changeante et ludique. Tu aimes la diversité, les petits plaisirs multiples plutôt que les grands investissements.

## Ton défi
Éviter la dispersion financière ou l'incapacité à t'attacher durablement à ce que tu possèdes.

## Maison 2 en Gémeaux
Tu abordes l'argent avec curiosité et adaptabilité. Tes revenus peuvent venir de plusieurs sources, ton rapport aux possessions est léger.

## Micro-rituel du jour (2 min)
- Pense à tes différentes façons de générer ou dépenser de l'argent
- Respire et choisis une priorité
- Note une façon de simplifier ton rapport aux ressources aujourd'hui""",

    ('gemini', 3): """# ♀️ Vénus en Gémeaux

**En une phrase :** Tu communiques ton affection avec esprit et légèreté, charmant par tes mots et ta vivacité.

## Ton moteur
Ta façon d'exprimer l'amour est verbale et joueuse. Tu charmes par la conversation, l'humour, les échanges stimulants.

## Ton défi
Éviter de rester en surface dans les expressions affectives ou de fuir les émotions profondes dans le bavardage.

## Maison 3 en Gémeaux
Position renforcée : tu es un communicant de l'amour, charmeur et léger. Tes échanges affectifs sont vifs et multiples.

## Micro-rituel du jour (2 min)
- Pense à un sentiment profond que tu n'as exprimé qu'avec des mots légers
- Respire et trouve les mots du cœur
- Note une façon de dire quelque chose de vraiment intime aujourd'hui""",

    ('gemini', 5): """# ♀️ Vénus en Gémeaux

**En une phrase :** Tu aimes avec curiosité et ta créativité s'exprime par les mots, les jeux d'esprit et la variété.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est légère et multiple. Tu aimes la conversation, le flirt intellectuel, les plaisirs variés.

## Ton défi
Éviter de papillonner entre les amours sans approfondir ou de confondre stimulation intellectuelle et connexion émotionnelle.

## Maison 5 en Gémeaux
Tu abordes les romances et la créativité avec esprit. Tes amours sont cérébrales, ta créativité est verbale et joueuse.

## Micro-rituel du jour (2 min)
- Pense à une relation que tu as survolée au lieu d'approfondir
- Respire et trouve ce qui pourrait la rendre plus profonde
- Note une façon de créer avec les mots aujourd'hui""",

    ('gemini', 6): """# ♀️ Vénus en Gémeaux

**En une phrase :** Tu apportes de la beauté au quotidien par la variété, la communication et la légèreté.

## Ton moteur
Ta façon de rendre le travail agréable est d'y mettre de la diversité et des échanges. Tu aimes les environnements stimulants et communicatifs.

## Ton défi
Éviter de te disperser dans trop de tâches agréables ou de négliger les aspects routiniers au profit de la nouveauté.

## Maison 6 en Gémeaux
Tu abordes le service et la routine avec adaptabilité. Tu veux que le quotidien soit varié et intellectuellement stimulant.

## Micro-rituel du jour (2 min)
- Identifie une tâche routinière que tu négliges car pas assez stimulante
- Respire et trouve une façon de la rendre intéressante
- Note une façon d'apprécier la routine avec un œil neuf aujourd'hui""",

    ('gemini', 8): """# ♀️ Vénus en Gémeaux

**En une phrase :** Tu vis l'intimité par le dialogue et ton amour se révèle dans les échanges profonds et les confidences.

## Ton moteur
Ta façon d'aimer en profondeur passe par les mots et la compréhension. Tu construis l'intimité par la conversation, le partage des secrets.

## Ton défi
Éviter de fuir l'intensité émotionnelle dans l'analyse ou de rationaliser les transformations au lieu de les vivre.

## Maison 8 en Gémeaux
Tu abordes les ressources partagées et l'intimité avec curiosité. Les discussions sur les sujets tabous te fascinent.

## Micro-rituel du jour (2 min)
- Pense à une émotion intense que tu as analysée au lieu de ressentir
- Respire et laisse-la simplement être
- Note une façon de vivre l'intimité au-delà des mots aujourd'hui""",

    ('gemini', 9): """# ♀️ Vénus en Gémeaux

**En une phrase :** Tu trouves la beauté dans la diversité des idées et tes valeurs spirituelles sont ouvertes et curieuses.

## Ton moteur
Ta façon d'aimer les grandes idées est éclectique et joueuse. Tu papillonnes entre les philosophies, tu voyages pour les échanges.

## Ton défi
Éviter de survoler trop de systèmes de pensée ou de confondre accumulation d'idées et sagesse intégrée.

## Maison 9 en Gémeaux
Tu abordes les voyages et la philosophie avec curiosité. Ta spiritualité aime apprendre, comparer, explorer intellectuellement.

## Micro-rituel du jour (2 min)
- Pense à une croyance que tu as explorée sans l'intégrer vraiment
- Respire et choisis d'approfondir
- Note une façon de vivre ta spiritualité au-delà des livres aujourd'hui""",

    ('gemini', 11): """# ♀️ Vénus en Gémeaux

**En une phrase :** Tu apportes légèreté et connexion aux groupes et tes amitiés sont nombreuses et stimulantes.

## Ton moteur
Ta façon d'être ami est sociale et communicative. Tu connectes les gens, tu animes les conversations, tu charmes par ton esprit.

## Ton défi
Éviter d'avoir trop d'amis superficiels ou de négliger les amitiés qui demandent plus de profondeur.

## Maison 11 en Gémeaux
Tu abordes les amitiés et projets collectifs avec légèreté. Tes amis sont variés, tes idéaux sont intellectuels et multiples.

## Micro-rituel du jour (2 min)
- Pense à un ami avec qui tu échanges beaucoup mais sans profondeur
- Respire et trouve une question plus intime à lui poser
- Note une façon d'approfondir une amitié aujourd'hui""",

    ('gemini', 12): """# ♀️ Vénus en Gémeaux

**En une phrase :** Tu trouves la beauté dans les pensées intérieures et ton amour de soi se révèle dans la curiosité envers ton inconscient.

## Ton moteur
Ta façon d'aimer l'invisible est intellectuelle et exploratoire. Tu médites en questionnant, tu explores tes rêves avec curiosité.

## Ton défi
Éviter de fuir l'introspection dans la dispersion mentale ou d'analyser ton monde intérieur au lieu de le ressentir.

## Maison 12 en Gémeaux
Tu abordes le monde intérieur avec curiosité. Tes retraites sont studieuses, ta compassion passe par la compréhension.

## Micro-rituel du jour (2 min)
- Identifie une question intérieure que tu analyses au lieu de la vivre
- Respire et laisse la réponse venir sans mots
- Note une façon de te connecter à ton âme sans réfléchir aujourd'hui""",

    # CANCER
    ('cancer', 2): """# ♀️ Vénus en Cancer

**En une phrase :** Tu trouves la beauté dans la sécurité émotionnelle et tes valeurs sont liées à la famille et à la protection.

## Ton moteur
Ta façon d'aimer les choses matérielles est émotionnelle et nostalgique. Tu aimes ce qui a une histoire, ce qui te rappelle un foyer.

## Ton défi
Éviter de t'accrocher aux possessions par sentimentalité ou de lier ta sécurité financière à ton état émotionnel.

## Maison 2 en Cancer
Tu abordes l'argent avec sensibilité. Tes valeurs sont familiales, ton rapport aux ressources est protecteur et émotionnel.

## Micro-rituel du jour (2 min)
- Pense à un objet que tu gardes par nostalgie mais qui t'encombre
- Respire et demande-toi si tu peux garder le souvenir sans l'objet
- Note une façon de te sentir en sécurité financière sans attachement aujourd'hui""",

    ('cancer', 3): """# ♀️ Vénus en Cancer

**En une phrase :** Tu communiques ton affection avec tendresse et tes mots portent la chaleur du foyer et de la protection.

## Ton moteur
Ta façon d'exprimer l'amour est nourrissante et émotionnelle. Tu charmes par ton écoute, ta douceur, ta capacité à créer un espace sûr.

## Ton défi
Éviter de te fermer quand tu te sens blessé ou d'exprimer l'amour de façon trop indirecte par peur du rejet.

## Maison 3 en Cancer
Tu communiques ton affection avec sensibilité. Tes échanges avec l'entourage sont nourrissants, tes mots portent l'émotion.

## Micro-rituel du jour (2 min)
- Pense à un sentiment affectueux que tu n'as pas exprimé par peur
- Respire et trouve le courage de la tendresse
- Note une façon de dire "je tiens à toi" avec douceur aujourd'hui""",

    ('cancer', 5): """# ♀️ Vénus en Cancer

**En une phrase :** Tu aimes avec dévotion et ta créativité s'exprime dans la création d'un nid, d'un foyer, d'un espace d'amour.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est profonde et protectrice. Tu veux des romances qui ressemblent à un foyer, des plaisirs en famille.

## Ton défi
Éviter de t'accrocher aux relations par besoin de sécurité ou de projeter tes besoins familiaux sur tes amours romantiques.

## Maison 5 en Cancer
Tu abordes les romances et la créativité avec émotion. Tes amours cherchent un nid, ta créativité est nourrissante et intime.

## Micro-rituel du jour (2 min)
- Pense à une attente familiale que tu projettes sur une relation romantique
- Respire et sépare les deux besoins
- Note une façon de créer de la beauté pour nourrir les autres aujourd'hui""",

    ('cancer', 6): """# ♀️ Vénus en Cancer

**En une phrase :** Tu apportes de la beauté au quotidien par le soin, la nourriture et l'attention émotionnelle.

## Ton moteur
Ta façon de rendre le travail agréable est d'y créer un environnement familial et protecteur. Tu prends soin de tes collègues.

## Ton défi
Éviter de te laisser submerger par les besoins émotionnels des autres au travail ou de mélanger vie personnelle et professionnelle.

## Maison 6 en Cancer
Tu abordes le service et la routine avec sensibilité. Tu veux que le quotidien soit comme un foyer, chaleureux et nourrissant.

## Micro-rituel du jour (2 min)
- Identifie un moment où tu as trop pris en charge les émotions de collègues
- Respire et définis tes limites avec douceur
- Note une façon de prendre soin de toi au travail aujourd'hui""",

    ('cancer', 8): """# ♀️ Vénus en Cancer

**En une phrase :** Tu vis l'intimité avec profondeur émotionnelle et ton amour se révèle dans la vulnérabilité partagée et la fusion des âmes.

## Ton moteur
Ta façon d'aimer en profondeur est totale et fusionnelle. Tu construis l'intimité par l'émotion partagée, la confiance absolue.

## Ton défi
Éviter de fusionner au point de te perdre ou de te refermer comme une coquille quand tu te sens blessé.

## Maison 8 en Cancer
Tu abordes les ressources partagées et l'intimité avec émotion. Les discussions profondes touchent au cœur et aux racines.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu t'es fermé par peur d'être blessé dans l'intimité
- Respire et trouve la force de rester ouvert
- Note une façon de partager ta vulnérabilité avec quelqu'un de confiance aujourd'hui""",

    ('cancer', 9): """# ♀️ Vénus en Cancer

**En une phrase :** Tu trouves la beauté dans les racines et tes valeurs spirituelles sont liées à la mémoire, aux ancêtres et au foyer sacré.

## Ton moteur
Ta façon d'aimer les grandes idées est émotionnelle et ancestrale. Tu préfères les sagesses qui te rappellent la maison, les traditions familiales.

## Ton défi
Éviter de rejeter les spiritualités qui ne résonnent pas émotionnellement ou de t'enfermer dans les croyances familiales.

## Maison 9 en Cancer
Tu abordes les voyages et la philosophie avec le cœur. Ta spiritualité cherche un "chez soi" universel, tes voyages te rapprochent des racines.

## Micro-rituel du jour (2 min)
- Pense à une sagesse nouvelle qui ne résonne pas avec ton éducation
- Respire et donne-lui une chance
- Note une façon d'honorer tes racines tout en t'ouvrant au monde aujourd'hui""",

    ('cancer', 11): """# ♀️ Vénus en Cancer

**En une phrase :** Tu apportes chaleur et protection aux groupes et tes amitiés deviennent une famille choisie.

## Ton moteur
Ta façon d'être ami est maternante et loyale. Tu crées des cercles intimes, tu nourris tes amis, tu les accueilles comme une famille.

## Ton défi
Éviter de projeter tes besoins familiaux sur tes amis ou de te replier quand le groupe ne te nourrit pas assez.

## Maison 11 en Cancer
Tu abordes les amitiés et projets collectifs avec émotion. Tes amis sont ta tribu, tes idéaux visent le bien-être collectif.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu te sens déçu car pas assez "famille"
- Respire et ajuste tes attentes
- Note une façon de nourrir ton cercle d'amis sans t'épuiser aujourd'hui""",

    ('cancer', 12): """# ♀️ Vénus en Cancer

**En une phrase :** Tu trouves la beauté dans les profondeurs de l'âme et ton amour de soi se révèle dans la compassion et l'accueil inconditionnel.

## Ton moteur
Ta façon d'aimer l'invisible est maternelle et intuitive. Tu médites pour te retrouver, tu accueilles toutes les parts de toi avec tendresse.

## Ton défi
Éviter de te perdre dans les émotions inconscientes ou de confondre apitoiement et compassion vraie.

## Maison 12 en Cancer
Tu abordes le monde intérieur avec sensibilité. Tes retraites sont comme un retour au ventre maternel, ta spiritualité est intuitive.

## Micro-rituel du jour (2 min)
- Identifie une émotion inconsciente qui te submerge régulièrement
- Respire et accueille-la comme un enfant intérieur
- Note une façon de te materner toi-même aujourd'hui""",

    # LEO
    ('leo', 2): """# ♀️ Vénus en Lion

**En une phrase :** Tu trouves la beauté dans ce qui brille et tes valeurs sont liées à la générosité et à la reconnaissance.

## Ton moteur
Ta façon d'aimer les choses matérielles est grandiose et généreuse. Tu aimes ce qui est beau, noble, digne d'admiration.

## Ton défi
Éviter les dépenses ostentatoires ou l'attachement aux possessions qui nourrissent ton ego plutôt que ton cœur.

## Maison 2 en Lion
Tu abordes l'argent avec générosité et fierté. Tes valeurs sont nobles, ton rapport aux ressources est lié à ton besoin de briller.

## Micro-rituel du jour (2 min)
- Pense à une dépense récente faite pour impressionner
- Respire et demande-toi ce qui t'aurait vraiment nourri
- Note une façon de te sentir riche sans briller aux yeux des autres aujourd'hui""",

    ('leo', 3): """# ♀️ Vénus en Lion

**En une phrase :** Tu communiques ton affection avec chaleur et générosité, charmant par ta lumière et ta présence.

## Ton moteur
Ta façon d'exprimer l'amour est dramatique et chaleureuse. Tu déclares ta flamme avec panache, tu charmes en rayonnant.

## Ton défi
Éviter de monopoliser l'attention dans les échanges affectifs ou d'avoir besoin d'être admiré pour te sentir aimé.

## Maison 3 en Lion
Tu communiques ton affection avec éclat. Tes échanges avec l'entourage sont chaleureux et généreux, tes mots brillent.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as cherché l'admiration dans une déclaration d'amour
- Respire et trouve une façon de donner sans attendre d'applaudissements
- Note une façon de célébrer quelqu'un d'autre avec tes mots aujourd'hui""",

    ('leo', 5): """# ♀️ Vénus en Lion

**En une phrase :** Tu aimes avec passion et ta créativité rayonne, cherchant la scène et la célébration.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est flamboyante et théâtrale. Tu veux des romances dignes d'un film, une créativité applaudie.

## Ton défi
Éviter de chercher la validation constante en amour ou de ne créer que pour être admiré plutôt que pour l'amour de l'art.

## Maison 5 en Lion
Position renforcée : tu es un amoureux passionné et un créateur né. Tes romances sont des épopées, ta créativité brille.

## Micro-rituel du jour (2 min)
- Pense à une création que tu n'as pas partagée car pas assez "parfaite" pour être applaudie
- Respire et crée pour la joie de créer
- Note une façon de t'exprimer sans chercher de validation aujourd'hui""",

    ('leo', 6): """# ♀️ Vénus en Lion

**En une phrase :** Tu apportes de la beauté au quotidien par la générosité, la chaleur et le désir de rendre le travail noble.

## Ton moteur
Ta façon de rendre le travail agréable est d'y apporter ton cœur et ta fierté. Tu veux que ton travail soit reconnu et admirable.

## Ton défi
Éviter de chercher les compliments au travail ou de négliger les tâches humbles qui ne te mettent pas en valeur.

## Maison 6 en Lion
Tu abordes le service et la routine avec noblesse. Tu veux que le quotidien soit digne, que ton travail brille.

## Micro-rituel du jour (2 min)
- Identifie une tâche que tu négliges car elle ne te met pas en valeur
- Respire et trouve la noblesse dans le service humble
- Note une façon de donner au travail sans chercher de reconnaissance aujourd'hui""",

    ('leo', 8): """# ♀️ Vénus en Lion

**En une phrase :** Tu vis l'intimité avec intensité dramatique et ton amour se révèle dans la passion généreuse et la loyauté totale.

## Ton moteur
Ta façon d'aimer en profondeur est flamboyante et totale. Tu donnes tout ton cœur, tu veux être l'unique amour de l'autre.

## Ton défi
Éviter de dramatiser les transformations ou d'avoir besoin d'être le héros de toutes les crises intimes.

## Maison 8 en Lion
Tu abordes les ressources partagées et l'intimité avec générosité. Les discussions profondes sont intenses et passionnées.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as voulu être au centre d'une crise relationnelle
- Respire et accepte d'être un acteur parmi d'autres
- Note une façon d'aimer profondément sans chercher à briller aujourd'hui""",

    ('leo', 9): """# ♀️ Vénus en Lion

**En une phrase :** Tu trouves la beauté dans les grandes visions et tes valeurs spirituelles sont liées à la générosité et à la joie de vivre.

## Ton moteur
Ta façon d'aimer les grandes idées est enthousiaste et généreuse. Tu veux partager ta lumière, inspirer par ta foi joyeuse.

## Ton défi
Éviter l'orgueil spirituel ou la croyance que ta vision est supérieure aux autres.

## Maison 9 en Lion
Tu abordes les voyages et la philosophie avec générosité. Ta spiritualité rayonne, tes convictions sont portées avec fierté.

## Micro-rituel du jour (2 min)
- Pense à une conviction spirituelle que tu portes avec orgueil
- Respire et trouve l'humilité dans ta foi
- Note une façon d'inspirer sans prêcher aujourd'hui""",

    ('leo', 11): """# ♀️ Vénus en Lion

**En une phrase :** Tu apportes lumière et générosité aux groupes et tes amitiés sont des scènes où chacun peut briller.

## Ton moteur
Ta façon d'être ami est loyale et chaleureuse. Tu organises les fêtes, tu célèbres tes amis, tu crées des moments mémorables.

## Ton défi
Éviter de vouloir être la star du groupe ou de te sentir blessé si tu n'es pas au centre de l'attention sociale.

## Maison 11 en Lion
Tu abordes les amitiés et projets collectifs avec cœur. Tes amis t'admirent, tes idéaux sont généreux et inspirants.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu voudrais être plus au centre
- Respire et trouve la joie à célébrer les autres
- Note une façon de mettre un ami en lumière aujourd'hui""",

    ('leo', 12): """# ♀️ Vénus en Lion

**En une phrase :** Tu trouves la beauté dans la lumière intérieure et ton amour de soi se révèle dans la compassion royale et la générosité de l'âme.

## Ton moteur
Ta façon d'aimer l'invisible est lumineuse et généreuse. Tu médites pour trouver ta lumière intérieure, tu transformes l'ombre en or.

## Ton défi
Éviter de vouloir briller même dans ta vie spirituelle ou de fuir l'humilité que demande l'invisible.

## Maison 12 en Lion
Tu abordes le monde intérieur avec noblesse. Tes retraites sont créatives, ta spiritualité cherche à faire rayonner l'âme.

## Micro-rituel du jour (2 min)
- Identifie une part de toi que tu caches car elle ne brille pas
- Respire et envoie-lui de l'amour
- Note une façon de t'aimer dans l'ombre aujourd'hui""",

    # VIRGO
    ('virgo', 2): """# ♀️ Vénus en Vierge

**En une phrase :** Tu trouves la beauté dans l'utile et tes valeurs sont liées à la qualité, la précision et le service.

## Ton moteur
Ta façon d'aimer les choses matérielles est pratique et discrète. Tu apprécies ce qui est bien fait, utile, de qualité sans ostentation.

## Ton défi
Éviter d'être trop critique envers ce que tu possèdes ou de ne jamais te sentir satisfait de tes ressources.

## Maison 2 en Vierge
Tu abordes l'argent avec analyse et discernement. Tes valeurs sont pratiques, ton rapport aux ressources est organisé.

## Micro-rituel du jour (2 min)
- Pense à quelque chose que tu possèdes et que tu critiques régulièrement
- Respire et trouve sa valeur telle qu'elle est
- Note une façon d'apprécier ce que tu as sans chercher à améliorer aujourd'hui""",

    ('virgo', 3): """# ♀️ Vénus en Vierge

**En une phrase :** Tu communiques ton affection par les gestes concrets et les attentions pratiques plutôt que par les grandes déclarations.

## Ton moteur
Ta façon d'exprimer l'amour est serviable et attentive. Tu charmes par ton aide, ta fiabilité, ton souci du détail.

## Ton défi
Éviter de critiquer ceux que tu aimes pour les améliorer ou d'exprimer ton amour uniquement par le service.

## Maison 3 en Vierge
Tu communiques ton affection avec précision et discrétion. Tes échanges sont utiles, tes mots d'amour sont concrets.

## Micro-rituel du jour (2 min)
- Pense à quelqu'un que tu aimes et que tu critiques souvent "pour son bien"
- Respire et trouve un compliment sincère à lui faire
- Note une façon de dire "je t'aime" sans conseil ni critique aujourd'hui""",

    ('virgo', 5): """# ♀️ Vénus en Vierge

**En une phrase :** Tu aimes avec attention et ta créativité s'exprime dans la perfection du détail et l'artisanat dévoué.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est discrète et serviable. Tu aimes prendre soin, améliorer, créer avec minutie.

## Ton défi
Éviter le perfectionnisme qui bloque la créativité ou la critique qui empoisonne les romances.

## Maison 5 en Vierge
Tu abordes les romances et la créativité avec discernement. Tes amours sont pratiques, ta créativité est artisanale et soignée.

## Micro-rituel du jour (2 min)
- Pense à une création "pas assez parfaite" que tu n'as pas terminée
- Respire et accepte son imperfection comme beauté
- Note une façon de créer sans viser la perfection aujourd'hui""",

    ('virgo', 6): """# ♀️ Vénus en Vierge

**En une phrase :** Tu apportes de la beauté au quotidien par l'ordre, le soin et le dévouement au travail bien fait.

## Ton moteur
Ta façon de rendre le travail agréable est d'y exceller et d'aider. Tu aimes les environnements propres, organisés, efficaces.

## Ton défi
Éviter le workaholisme déguisé en dévouement ou la critique constante de l'environnement de travail.

## Maison 6 en Vierge
Position renforcée : tu es naturellement douée pour le service, la routine et l'amélioration continue du quotidien.

## Micro-rituel du jour (2 min)
- Identifie un aspect de ton travail que tu critiques sans cesse
- Respire et accepte qu'il est suffisant pour aujourd'hui
- Note une façon de trouver de la beauté dans l'imperfection professionnelle aujourd'hui""",

    ('virgo', 8): """# ♀️ Vénus en Vierge

**En une phrase :** Tu vis l'intimité avec attention et ton amour se révèle dans le service discret et le soin des détails.

## Ton moteur
Ta façon d'aimer en profondeur est pratique et dévouée. Tu construis l'intimité par l'aide concrète, l'attention aux besoins.

## Ton défi
Éviter de fuir l'intensité émotionnelle dans le service ou de critiquer les défauts de l'autre au lieu d'accepter.

## Maison 8 en Vierge
Tu abordes les ressources partagées et l'intimité avec analyse. Les discussions profondes sont pratiques et orientées solutions.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as aidé au lieu de ressentir dans l'intimité
- Respire et permets-toi de juste être présent
- Note une façon d'accepter l'imperfection de l'autre dans l'intime aujourd'hui""",

    ('virgo', 9): """# ♀️ Vénus en Vierge

**En une phrase :** Tu trouves la beauté dans la sagesse pratique et tes valeurs spirituelles sont liées au service et à l'amélioration.

## Ton moteur
Ta façon d'aimer les grandes idées est concrète et critique. Tu préfères les philosophies qui s'appliquent, les spiritualités qui se vivent au quotidien.

## Ton défi
Éviter de rejeter les spiritualités qui ne te semblent pas utiles ou de critiquer les croyances des autres.

## Maison 9 en Vierge
Tu abordes les voyages et la philosophie avec discernement. Ta spiritualité est pratique et orientée service.

## Micro-rituel du jour (2 min)
- Pense à une croyance que tu as rejetée car "pas pratique"
- Respire et trouve ce qu'elle pourrait t'apporter
- Note une façon de vivre ta spiritualité concrètement aujourd'hui""",

    ('virgo', 11): """# ♀️ Vénus en Vierge

**En une phrase :** Tu apportes aide et discernement aux groupes et tes amitiés sont utiles et fiables.

## Ton moteur
Ta façon d'être ami est serviable et attentive. Tu aides tes amis concrètement, tu remarques leurs besoins, tu es là dans les détails.

## Ton défi
Éviter de critiquer tes amis "pour leur bien" ou de te sentir supérieur car tu vois ce qui ne va pas.

## Maison 11 en Vierge
Tu abordes les amitiés et projets collectifs avec sens pratique. Tes amis apprécient ton aide, tes idéaux visent l'amélioration concrète.

## Micro-rituel du jour (2 min)
- Pense à un ami que tu critiques souvent mentalement
- Respire et trouve trois qualités chez lui
- Note une façon d'aider sans corriger aujourd'hui""",

    ('virgo', 12): """# ♀️ Vénus en Vierge

**En une phrase :** Tu trouves la beauté dans le service silencieux et ton amour de soi se révèle dans l'acceptation de ton imperfection.

## Ton moteur
Ta façon d'aimer l'invisible est pratique et guérissante. Tu médites pour t'améliorer, tu sers les autres discrètement.

## Ton défi
Éviter de critiquer ta vie intérieure ou de vouloir réparer ton âme comme on répare un mécanisme.

## Maison 12 en Vierge
Tu abordes le monde intérieur avec discernement. Tes retraites sont ordonnées, ta spiritualité est orientée guérison et purification.

## Micro-rituel du jour (2 min)
- Identifie une part de toi que tu essaies constamment de réparer
- Respire et accepte-la telle qu'elle est
- Note une façon de t'aimer sans t'améliorer aujourd'hui""",

    # LIBRA
    ('libra', 2): """# ♀️ Vénus en Balance

**En une phrase :** Tu trouves la beauté dans l'harmonie et tes valeurs sont liées à l'équilibre, la justice et l'esthétique.

## Ton moteur
Ta façon d'aimer les choses matérielles est esthétique et relationnelle. Tu aimes ce qui est beau, équilibré, partagé.

## Ton défi
Éviter de dépendre des autres pour tes ressources ou d'être indécis face aux choix financiers.

## Maison 2 en Balance
Tu abordes l'argent avec sens de l'esthétique et du partage. Tes valeurs sont relationnelles, ton rapport aux ressources est équilibré.

## Micro-rituel du jour (2 min)
- Pense à une décision financière que tu repousses par indécision
- Respire et choisis, même imparfaitement
- Note une façon de valoriser ce que tu as indépendamment des autres aujourd'hui""",

    ('libra', 3): """# ♀️ Vénus en Balance

**En une phrase :** Tu communiques ton affection avec grâce et diplomatie, charmant par ton élégance verbale.

## Ton moteur
Ta façon d'exprimer l'amour est harmonieuse et équilibrée. Tu charmes par tes mots doux, ta capacité à voir les deux côtés, ton tact.

## Ton défi
Éviter de dire ce que l'autre veut entendre plutôt que ta vérité ou de fuir les conversations difficiles pour garder la paix.

## Maison 3 en Balance
Tu communiques ton affection avec élégance. Tes échanges avec l'entourage sont harmonieux, tes mots cherchent l'équilibre.

## Micro-rituel du jour (2 min)
- Pense à une vérité affectueuse que tu n'as pas dite pour ne pas créer de vagues
- Respire et trouve une façon élégante de l'exprimer
- Note une conversation vraie à avoir avec quelqu'un de proche aujourd'hui""",

    ('libra', 5): """# ♀️ Vénus en Balance

**En une phrase :** Tu aimes avec grâce et ta créativité s'exprime dans la recherche de la beauté et de l'harmonie parfaite.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est élégante et relationnelle. Tu veux des romances équilibrées, une créativité qui embellit.

## Ton défi
Éviter de te perdre dans le partenaire ou de ne pas créer tant que tu n'as pas trouvé l'harmonie parfaite.

## Maison 5 en Balance
Tu abordes les romances et la créativité avec grâce. Tes amours cherchent l'équilibre, ta créativité vise la beauté.

## Micro-rituel du jour (2 min)
- Pense à une relation où tu t'es perdu dans l'autre
- Respire et retrouve ton centre
- Note une façon de créer quelque chose de beau par toi-même aujourd'hui""",

    ('libra', 6): """# ♀️ Vénus en Balance

**En une phrase :** Tu apportes de la beauté au quotidien par l'harmonie, la diplomatie et l'esthétique de l'environnement.

## Ton moteur
Ta façon de rendre le travail agréable est d'y créer de l'harmonie et de la beauté. Tu aimes les environnements esthétiques et les relations fluides.

## Ton défi
Éviter de t'épuiser à maintenir la paix au travail ou de ne pas t'affirmer pour éviter les conflits.

## Maison 6 en Balance
Tu abordes le service et la routine avec sens de l'harmonie. Tu veux que le quotidien soit beau et les relations professionnelles équilibrées.

## Micro-rituel du jour (2 min)
- Identifie un conflit au travail que tu évites au détriment de ta vérité
- Respire et trouve une façon diplomatique de t'affirmer
- Note une façon d'embellir ton espace de travail aujourd'hui""",

    ('libra', 8): """# ♀️ Vénus en Balance

**En une phrase :** Tu vis l'intimité avec équilibre et ton amour se révèle dans le partenariat profond et le partage équitable.

## Ton moteur
Ta façon d'aimer en profondeur est relationnelle et équilibrée. Tu construis l'intimité par le partenariat, l'équité, la beauté partagée.

## Ton défi
Éviter de fuir l'intensité des transformations pour maintenir l'harmonie ou de dépendre de l'autre pour traverser les crises.

## Maison 8 en Balance
Tu abordes les ressources partagées et l'intimité avec sens de l'équité. Les discussions profondes cherchent le consensus.

## Micro-rituel du jour (2 min)
- Pense à une tension intime que tu évites pour garder la paix
- Respire et trouve une façon de l'aborder avec grâce
- Note une façon d'affronter la profondeur sans perdre l'harmonie aujourd'hui""",

    ('libra', 9): """# ♀️ Vénus en Balance

**En une phrase :** Tu trouves la beauté dans l'équilibre des perspectives et tes valeurs spirituelles cherchent l'harmonie universelle.

## Ton moteur
Ta façon d'aimer les grandes idées est diplomatique et comparative. Tu vois la valeur dans différentes visions, tu cherches la synthèse.

## Ton défi
Éviter de ne jamais choisir une voie ou de relativiser toutes les croyances au point de n'avoir aucune conviction.

## Maison 9 en Balance
Tu abordes les voyages et la philosophie avec sens de l'équilibre. Ta spiritualité cherche l'harmonie entre les traditions.

## Micro-rituel du jour (2 min)
- Pense à une conviction que tu refuses de défendre par souci d'équilibre
- Respire et ose prendre position
- Note une façon de croire avec grâce mais fermeté aujourd'hui""",

    ('libra', 11): """# ♀️ Vénus en Balance

**En une phrase :** Tu apportes harmonie et beauté aux groupes et tes amitiés sont élégantes et équilibrées.

## Ton moteur
Ta façon d'être ami est diplomatique et gracieuse. Tu crées de l'harmonie dans les groupes, tu es le lien entre les gens.

## Ton défi
Éviter de t'épuiser à maintenir la paix dans le groupe ou de ne pas défendre tes idées pour éviter les conflits.

## Maison 11 en Balance
Tu abordes les amitiés et projets collectifs avec sens de l'harmonie. Tes amis apprécient ta diplomatie, tes idéaux visent la beauté collective.

## Micro-rituel du jour (2 min)
- Pense à une opinion que tu ne partages pas avec ton groupe par souci d'harmonie
- Respire et trouve une façon élégante de l'exprimer
- Note une façon de contribuer au groupe avec ta vraie voix aujourd'hui""",

    ('libra', 12): """# ♀️ Vénus en Balance

**En une phrase :** Tu trouves la beauté dans l'équilibre intérieur et ton amour de soi se révèle dans l'harmonie entre toutes tes parts.

## Ton moteur
Ta façon d'aimer l'invisible est esthétique et harmonieuse. Tu médites pour trouver la paix, tu embellis ton monde intérieur.

## Ton défi
Éviter de fuir les parts sombres de toi pour maintenir une façade harmonieuse ou de dépendre des autres pour ta paix intérieure.

## Maison 12 en Balance
Tu abordes le monde intérieur avec sens de l'harmonie. Tes retraites sont belles, ta spiritualité cherche l'équilibre de l'âme.

## Micro-rituel du jour (2 min)
- Identifie une part de toi que tu caches car elle brise ton image harmonieuse
- Respire et intègre-la avec grâce
- Note une façon de faire la paix avec ton ombre aujourd'hui""",

    # SCORPIO
    ('scorpio', 2): """# ♀️ Vénus en Scorpion

**En une phrase :** Tu trouves la beauté dans l'intensité et tes valeurs sont liées au pouvoir, à la transformation et à l'authenticité profonde.

## Ton moteur
Ta façon d'aimer les choses matérielles est intense et stratégique. Tu veux des ressources qui te donnent du pouvoir, pas du clinquant.

## Ton défi
Éviter l'obsession du contrôle financier ou l'attachement aux possessions qui symbolisent ta puissance.

## Maison 2 en Scorpion
Tu abordes l'argent avec intensité et stratégie. Tes valeurs sont profondes, ton rapport aux ressources est transformatif.

## Micro-rituel du jour (2 min)
- Pense à une peur liée à l'argent qui t'obsède
- Respire et identifie ce que tu contrôles vraiment
- Note une façon de valoriser ta richesse intérieure aujourd'hui""",

    ('scorpio', 3): """# ♀️ Vénus en Scorpion

**En une phrase :** Tu communiques ton affection avec intensité et tes mots portent la puissance de la vérité et du désir.

## Ton moteur
Ta façon d'exprimer l'amour est profonde et magnétique. Tu charmes par ton regard, ton intensité, ta capacité à dire l'indicible.

## Ton défi
Éviter la manipulation verbale ou les tests constants pour vérifier l'amour de l'autre.

## Maison 3 en Scorpion
Tu communiques ton affection avec profondeur. Tes échanges avec l'entourage sont intenses, tes mots touchent l'essentiel.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as testé quelqu'un au lieu de lui faire confiance
- Respire et choisis la confiance
- Note une façon de communiquer ton amour avec vulnérabilité aujourd'hui""",

    ('scorpio', 5): """# ♀️ Vénus en Scorpion

**En une phrase :** Tu aimes avec passion dévorante et ta créativité explore les profondeurs de l'âme et du désir.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est totale et transformative. Tu veux des romances qui te changent, une créativité qui exorcise.

## Ton défi
Éviter les passions destructrices ou la jalousie qui empoisonne les relations.

## Maison 5 en Scorpion
Tu abordes les romances et la créativité avec intensité. Tes amours sont passionnées et transformatives, ta créativité est cathartique.

## Micro-rituel du jour (2 min)
- Pense à une jalousie qui a assombri une de tes relations
- Respire et transforme cette énergie en confiance
- Note une façon de créer à partir de tes émotions intenses aujourd'hui""",

    ('scorpio', 6): """# ♀️ Vénus en Scorpion

**En une phrase :** Tu apportes de la beauté au quotidien par la transformation, l'intensité et la capacité à voir au-delà des apparences.

## Ton moteur
Ta façon de rendre le travail agréable est d'y apporter de la profondeur et du sens. Tu aimes les environnements où l'on peut creuser.

## Ton défi
Éviter les dynamiques de pouvoir au travail ou l'intensité qui épuise tes collègues.

## Maison 6 en Scorpion
Tu abordes le service et la routine avec intensité. Tu veux que le quotidien ait du sens profond, pas de superficialité.

## Micro-rituel du jour (2 min)
- Identifie une dynamique de pouvoir au travail qui te consume
- Respire et lâche le besoin de contrôler
- Note une façon de transformer positivement ton quotidien aujourd'hui""",

    ('scorpio', 8): """# ♀️ Vénus en Scorpion

**En une phrase :** Tu vis l'intimité avec une intensité naturelle et ton amour se révèle dans la fusion totale et la transformation mutuelle.

## Ton moteur
Ta façon d'aimer en profondeur est ton élément natif. Tu n'as pas peur des ténèbres, tu t'y épanouis, tu transformes par l'amour.

## Ton défi
Éviter de te perdre dans l'intensité ou de confondre passion destructrice et amour véritable.

## Maison 8 en Scorpion
Position renforcée : tu es naturellement à l'aise avec l'intimité profonde, la transformation, les ressources partagées.

## Micro-rituel du jour (2 min)
- Pense à un moment où l'intensité est devenue destructrice
- Respire et trouve l'équilibre entre profondeur et légèreté
- Note une façon d'aimer profondément avec douceur aujourd'hui""",

    ('scorpio', 9): """# ♀️ Vénus en Scorpion

**En une phrase :** Tu trouves la beauté dans les vérités cachées et tes valeurs spirituelles plongent dans les mystères de l'existence.

## Ton moteur
Ta façon d'aimer les grandes idées est radicale et transformative. Tu cherches les sagesses qui changent, pas celles qui rassurent.

## Ton défi
Éviter le fanatisme spirituel ou le rejet de ce qui ne passe pas ton test de profondeur.

## Maison 9 en Scorpion
Tu abordes les voyages et la philosophie avec intensité. Ta spiritualité explore les mystères, tes convictions sont profondes.

## Micro-rituel du jour (2 min)
- Pense à une spiritualité que tu rejettes car trop légère
- Respire et trouve ce qu'elle pourrait t'apprendre
- Note une façon de croire avec intensité mais ouverture aujourd'hui""",

    ('scorpio', 11): """# ♀️ Vénus en Scorpion

**En une phrase :** Tu apportes profondeur et loyauté aux groupes et tes amitiés sont intenses et transformatives.

## Ton moteur
Ta façon d'être ami est totale et loyale. Tes amitiés sont peu nombreuses mais profondes, tes engagements collectifs sont passionnés.

## Ton défi
Éviter la jalousie entre amis ou les dynamiques de pouvoir qui empoisonnent les groupes.

## Maison 11 en Scorpion
Tu abordes les amitiés et projets collectifs avec intensité. Tes amis sont comme des frères d'âme, tes idéaux visent la transformation.

## Micro-rituel du jour (2 min)
- Pense à une amitié où la jalousie ou le pouvoir s'est infiltré
- Respire et choisis la confiance
- Note une façon de soutenir un ami sans attente aujourd'hui""",

    ('scorpio', 12): """# ♀️ Vénus en Scorpion

**En une phrase :** Tu trouves la beauté dans les abysses de l'âme et ton amour de soi se révèle dans l'accueil total de ton ombre.

## Ton moteur
Ta façon d'aimer l'invisible est naturelle et courageuse. Tu plonges dans ton inconscient sans peur, tu transmutes les ténèbres en lumière.

## Ton défi
Éviter de te complaire dans les profondeurs ou de t'identifier à ton ombre au point d'oublier ta lumière.

## Maison 12 en Scorpion
Tu abordes le monde intérieur avec intensité naturelle. Tes retraites sont transformatives, ta spiritualité est alchimique.

## Micro-rituel du jour (2 min)
- Identifie une fascination pour ton ombre qui devient obsession
- Respire et accueille aussi ta lumière
- Note une façon d'aimer toutes tes parts aujourd'hui""",

    # SAGITTARIUS
    ('sagittarius', 2): """# ♀️ Vénus en Sagittaire

**En une phrase :** Tu trouves la beauté dans l'abondance et tes valeurs sont liées à la liberté, l'aventure et la générosité.

## Ton moteur
Ta façon d'aimer les choses matérielles est expansive et optimiste. Tu crois en l'abondance, tu donnes et dépenses avec générosité.

## Ton défi
Éviter les excès financiers par optimisme ou la négligence des détails pratiques de la gestion.

## Maison 2 en Sagittaire
Tu abordes l'argent avec optimisme et foi. Tes valeurs sont expansives, ton rapport aux ressources est généreux.

## Micro-rituel du jour (2 min)
- Pense à une dépense excessive faite par optimisme
- Respire et trouve l'équilibre entre générosité et sagesse
- Note une façon d'apprécier l'abondance que tu as déjà aujourd'hui""",

    ('sagittarius', 3): """# ♀️ Vénus en Sagittaire

**En une phrase :** Tu communiques ton affection avec enthousiasme et tes mots portent des visions inspirantes et joyeuses.

## Ton moteur
Ta façon d'exprimer l'amour est expansive et aventureuse. Tu charmes par ton optimisme, tes histoires, ta capacité à inspirer.

## Ton défi
Éviter de promettre plus que tu ne peux tenir ou de négliger les besoins quotidiens de l'autre au profit des grandes visions.

## Maison 3 en Sagittaire
Tu communiques ton affection avec enthousiasme. Tes échanges avec l'entourage sont inspirants et aventuriers.

## Micro-rituel du jour (2 min)
- Pense à une promesse affectueuse que tu n'as pas tenue
- Respire et trouve une façon de l'honorer ou de clarifier
- Note une façon de montrer ton amour dans le quotidien aujourd'hui""",

    ('sagittarius', 5): """# ♀️ Vénus en Sagittaire

**En une phrase :** Tu aimes avec joie et ta créativité s'exprime dans l'aventure, l'exploration et la célébration de la vie.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est joyeuse et libre. Tu veux des romances qui t'expansent, une créativité sans limite.

## Ton défi
Éviter de fuir l'engagement pour garder ta liberté ou de te lasser quand l'aventure devient routine.

## Maison 5 en Sagittaire
Tu abordes les romances et la créativité avec enthousiasme. Tes amours sont des aventures, ta créativité est expansive.

## Micro-rituel du jour (2 min)
- Pense à une relation que tu as fuie quand elle devenait trop quotidienne
- Respire et trouve l'aventure dans l'engagement
- Note une façon de créer quelque chose de joyeux aujourd'hui""",

    ('sagittarius', 6): """# ♀️ Vénus en Sagittaire

**En une phrase :** Tu apportes de la beauté au quotidien par l'optimisme, le sens et la joie de servir une cause plus grande.

## Ton moteur
Ta façon de rendre le travail agréable est d'y trouver un sens plus grand. Tu aimes quand le quotidien sert une vision.

## Ton défi
Éviter de négliger les tâches routinières ou de t'ennuyer quand le travail n'est pas inspirant.

## Maison 6 en Sagittaire
Tu abordes le service et la routine avec optimisme. Tu veux que le quotidien ait un sens, que le travail serve une mission.

## Micro-rituel du jour (2 min)
- Identifie une tâche quotidienne que tu négliges car "pas assez inspirante"
- Respire et trouve le sens caché dans cette tâche
- Note une façon d'apporter de la joie à ton travail aujourd'hui""",

    ('sagittarius', 8): """# ♀️ Vénus en Sagittaire

**En une phrase :** Tu vis l'intimité avec foi et ton amour se révèle dans la confiance et le partage des grandes visions.

## Ton moteur
Ta façon d'aimer en profondeur est optimiste et confiante. Tu crois que l'amour peut tout transformer, tu donnes ta confiance.

## Ton défi
Éviter de fuir les profondeurs dans l'optimisme ou de minimiser la souffrance par la philosophie.

## Maison 8 en Sagittaire
Tu abordes les ressources partagées et l'intimité avec foi. Les discussions profondes cherchent le sens et la croissance.

## Micro-rituel du jour (2 min)
- Pense à une douleur intime que tu as minimisée par l'optimisme
- Respire et accorde-lui sa place
- Note une façon d'être présent à la profondeur avec foi aujourd'hui""",

    ('sagittarius', 9): """# ♀️ Vénus en Sagittaire

**En une phrase :** Tu trouves la beauté dans la quête de sens et tes valeurs spirituelles sont liées à l'expansion et à la liberté.

## Ton moteur
Ta façon d'aimer les grandes idées est ton élément naturel. Tu es une chercheuse de sens née, une amoureuse de la sagesse.

## Ton défi
Éviter de survoler trop de philosophies ou de croire avoir trouvé LA vérité à chaque nouvelle découverte.

## Maison 9 en Sagittaire
Position renforcée : tu es naturellement spirituelle, voyageuse de l'esprit, en quête de sens et de liberté.

## Micro-rituel du jour (2 min)
- Pense à une croyance récente que tu as adoptée avec enthousiasme
- Respire et questionne-la avec la même curiosité
- Note une façon d'approfondir ta sagesse plutôt que de l'élargir aujourd'hui""",

    ('sagittarius', 11): """# ♀️ Vénus en Sagittaire

**En une phrase :** Tu apportes joie et inspiration aux groupes et tes amitiés sont des aventures partagées.

## Ton moteur
Ta façon d'être ami est généreuse et enthousiaste. Tu organises les aventures, tu inspires le groupe, tu crois en tes amis.

## Ton défi
Éviter de promettre au groupe plus que tu ne peux donner ou de t'ennuyer dans les amitiés qui manquent d'aventure.

## Maison 11 en Sagittaire
Tu abordes les amitiés et projets collectifs avec optimisme. Tes amis sont des compagnons d'aventure, tes idéaux sont mondiaux.

## Micro-rituel du jour (2 min)
- Pense à une amitié que tu négliges car moins aventureuse
- Respire et trouve la richesse dans la stabilité
- Note une façon de célébrer un ami simplement aujourd'hui""",

    ('sagittarius', 12): """# ♀️ Vénus en Sagittaire

**En une phrase :** Tu trouves la beauté dans l'expansion spirituelle et ton amour de soi se révèle dans la foi et la quête intérieure.

## Ton moteur
Ta façon d'aimer l'invisible est joyeuse et expansive. Tu médites pour t'expanser, tu trouves le sacré dans l'aventure intérieure.

## Ton défi
Éviter de fuir l'introspection dans la quête spirituelle ou de négliger ton ombre par excès d'optimisme.

## Maison 12 en Sagittaire
Tu abordes le monde intérieur avec foi et optimisme. Tes retraites sont des voyages, ta spiritualité est joyeuse.

## Micro-rituel du jour (2 min)
- Identifie une part sombre de toi que tu évites par l'optimisme spirituel
- Respire et accueille-la avec la même bienveillance
- Note une façon d'intégrer ton ombre dans ta quête de lumière aujourd'hui""",

    # CAPRICORN
    ('capricorn', 2): """# ♀️ Vénus en Capricorne

**En une phrase :** Tu trouves la beauté dans ce qui dure et tes valeurs sont liées à la qualité, la tradition et la réussite.

## Ton moteur
Ta façon d'aimer les choses matérielles est pragmatique et ambitieuse. Tu apprécies ce qui est construit pour durer, le classique plutôt que la mode.

## Ton défi
Éviter la rigidité financière ou l'association de ta valeur personnelle à ta réussite matérielle.

## Maison 2 en Capricorne
Tu abordes l'argent avec sérieux et stratégie. Tes valeurs sont traditionnelles, ton rapport aux ressources est responsable.

## Micro-rituel du jour (2 min)
- Pense à une croyance que ta valeur dépend de tes possessions
- Respire et reconnais ta valeur intrinsèque
- Note une façon de te sentir riche indépendamment de tes biens aujourd'hui""",

    ('capricorn', 3): """# ♀️ Vénus en Capricorne

**En une phrase :** Tu communiques ton affection avec réserve et fidélité, charmant par ta fiabilité et ta constance.

## Ton moteur
Ta façon d'exprimer l'amour est discrète et durable. Tu charmes par ta stabilité, ton engagement, ta capacité à tenir tes promesses.

## Ton défi
Éviter la froideur émotionnelle ou la difficulté à exprimer la tendresse spontanément.

## Maison 3 en Capricorne
Tu communiques ton affection avec retenue. Tes échanges avec l'entourage sont fiables, tes mots d'amour sont mesurés mais sincères.

## Micro-rituel du jour (2 min)
- Pense à un sentiment tendre que tu n'exprimes pas par retenue
- Respire et trouve le courage de la douceur
- Note une façon de dire "je t'aime" même si c'est difficile aujourd'hui""",

    ('capricorn', 5): """# ♀️ Vénus en Capricorne

**En une phrase :** Tu aimes avec sérieux et ta créativité s'exprime dans la maîtrise, l'ambition et la construction durable.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est mature et réfléchie. Tu veux des romances qui construisent, une créativité qui laisse une trace.

## Ton défi
Éviter de transformer l'amour en devoir ou de bloquer ta créativité par trop de sérieux.

## Maison 5 en Capricorne
Tu abordes les romances et la créativité avec maturité. Tes amours sont construites pour durer, ta créativité est ambitieuse.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as rendu l'amour ou la créativité trop sérieux
- Respire et trouve la légèreté dans l'engagement
- Note une façon de jouer sans objectif aujourd'hui""",

    ('capricorn', 6): """# ♀️ Vénus en Capricorne

**En une phrase :** Tu apportes de la beauté au quotidien par la qualité, la discipline et l'excellence professionnelle.

## Ton moteur
Ta façon de rendre le travail agréable est d'y exceller avec intégrité. Tu aimes les environnements professionnels et structurés.

## Ton défi
Éviter le workaholisme ou la négation des plaisirs au profit du devoir.

## Maison 6 en Capricorne
Tu abordes le service et la routine avec professionnalisme. Tu veux que le quotidien soit efficace et que ton travail soit respecté.

## Micro-rituel du jour (2 min)
- Identifie un plaisir quotidien que tu sacrifies au travail
- Respire et accorde-toi ce plaisir
- Note une façon de te récompenser pour ton travail aujourd'hui""",

    ('capricorn', 8): """# ♀️ Vénus en Capricorne

**En une phrase :** Tu vis l'intimité avec profondeur et engagement, construisant des liens qui traversent le temps.

## Ton moteur
Ta façon d'aimer en profondeur est sérieuse et totale. Tu construis l'intimité lentement mais solidement, pour la vie.

## Ton défi
Éviter la peur de la vulnérabilité ou le contrôle excessif des transformations.

## Maison 8 en Capricorne
Tu abordes les ressources partagées et l'intimité avec stratégie. Les discussions profondes sont pratiques et orientées vers le long terme.

## Micro-rituel du jour (2 min)
- Pense à une vulnérabilité que tu caches derrière la force
- Respire et laisse-la s'exprimer avec quelqu'un de confiance
- Note une façon de t'abandonner dans l'intimité aujourd'hui""",

    ('capricorn', 9): """# ♀️ Vénus en Capricorne

**En une phrase :** Tu trouves la beauté dans la sagesse éprouvée et tes valeurs spirituelles sont liées à la tradition et au respect des anciens.

## Ton moteur
Ta façon d'aimer les grandes idées est réaliste et respectueuse. Tu préfères les philosophies qui ont fait leurs preuves, les traditions sages.

## Ton défi
Éviter le cynisme face aux nouvelles idées ou l'attachement rigide aux traditions dépassées.

## Maison 9 en Capricorne
Tu abordes les voyages et la philosophie avec sérieux. Ta spiritualité est structurée et disciplinée.

## Micro-rituel du jour (2 min)
- Pense à une idée nouvelle que tu rejettes par conservatisme
- Respire et donne-lui une chance
- Note une façon d'honorer la tradition tout en t'ouvrant aujourd'hui""",

    ('capricorn', 11): """# ♀️ Vénus en Capricorne

**En une phrase :** Tu apportes stabilité et structure aux groupes et tes amitiés sont basées sur le respect et la durée.

## Ton moteur
Ta façon d'être ami est fiable et respectueuse. Tu es là pour la longue durée, tu apportes de la structure aux projets collectifs.

## Ton défi
Éviter la distance émotionnelle avec les amis ou de ne valoriser que les amitiés utiles.

## Maison 11 en Capricorne
Tu abordes les amitiés et projets collectifs avec sérieux. Tes amis sont souvent liés à ta carrière, tes idéaux sont réalistes.

## Micro-rituel du jour (2 min)
- Pense à une amitié que tu négliges car "pas utile"
- Respire et reconnais sa valeur en soi
- Note une façon de te connecter émotionnellement à un ami aujourd'hui""",

    ('capricorn', 12): """# ♀️ Vénus en Capricorne

**En une phrase :** Tu trouves la beauté dans la discipline intérieure et ton amour de soi se révèle dans la maîtrise de l'âme.

## Ton moteur
Ta façon d'aimer l'invisible est structurée et disciplinée. Tu médites avec méthode, tu construis ta vie intérieure comme un édifice.

## Ton défi
Éviter de transformer la spiritualité en devoir ou de fuir l'intériorité dans le travail.

## Maison 12 en Capricorne
Tu abordes le monde intérieur avec sérieux. Tes retraites sont disciplinées, ta spiritualité est orientée vers la maîtrise.

## Micro-rituel du jour (2 min)
- Identifie un aspect de ta vie spirituelle devenu une obligation
- Respire et retrouve la grâce dans la pratique
- Note une façon de méditer par amour plutôt que par devoir aujourd'hui""",

    # AQUARIUS
    ('aquarius', 2): """# ♀️ Vénus en Verseau

**En une phrase :** Tu trouves la beauté dans l'originalité et tes valeurs sont liées à la liberté, l'innovation et l'humanité.

## Ton moteur
Ta façon d'aimer les choses matérielles est non-conventionnelle et détachée. Tu apprécies ce qui est unique, innovant, pas mainstream.

## Ton défi
Éviter l'instabilité financière par rejet des méthodes traditionnelles ou le détachement excessif du matériel.

## Maison 2 en Verseau
Tu abordes l'argent avec originalité et détachement. Tes valeurs sont progressistes, ton rapport aux ressources est libre.

## Micro-rituel du jour (2 min)
- Pense à une méthode financière traditionnelle que tu rejettes par principe
- Respire et trouve ce qu'elle pourrait t'apporter
- Note une façon d'être innovant tout en restant ancré aujourd'hui""",

    ('aquarius', 3): """# ♀️ Vénus en Verseau

**En une phrase :** Tu communiques ton affection avec originalité et tes mots portent une vision d'amitié universelle.

## Ton moteur
Ta façon d'exprimer l'amour est amicale et libre. Tu charmes par ton originalité, ta vision unique, ton refus des conventions.

## Ton défi
Éviter la froideur émotionnelle ou la difficulté à exprimer l'amour de façon intime et personnelle.

## Maison 3 en Verseau
Tu communiques ton affection avec originalité. Tes échanges avec l'entourage sont stimulants et non-conventionnels.

## Micro-rituel du jour (2 min)
- Pense à un moment où ton originalité a créé de la distance émotionnelle
- Respire et trouve une façon plus intime de te connecter
- Note une façon de dire "je t'aime" de manière personnelle aujourd'hui""",

    ('aquarius', 5): """# ♀️ Vénus en Verseau

**En une phrase :** Tu aimes avec liberté et ta créativité s'exprime dans l'innovation, l'expérimentation et la vision du futur.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est libre et originale. Tu veux des romances sans cage, une créativité d'avant-garde.

## Ton défi
Éviter le détachement émotionnel ou la peur de l'engagement qui masque une peur de l'intimité.

## Maison 5 en Verseau
Tu abordes les romances et la créativité avec liberté. Tes amours sont amicales et libres, ta créativité est inventive.

## Micro-rituel du jour (2 min)
- Pense à une relation où tu as fui l'engagement par besoin de liberté
- Respire et trouve la liberté dans l'engagement
- Note une façon de créer quelque chose d'innovant aujourd'hui""",

    ('aquarius', 6): """# ♀️ Vénus en Verseau

**En une phrase :** Tu apportes de la beauté au quotidien par l'innovation, la vision collective et le refus de la routine banale.

## Ton moteur
Ta façon de rendre le travail agréable est d'y apporter de l'innovation et une vision humaniste. Tu veux changer le système.

## Ton défi
Éviter le détachement des collègues ou le rejet des méthodes établies juste par principe.

## Maison 6 en Verseau
Tu abordes le service et la routine avec originalité. Tu veux que le quotidien soit innovant et au service de l'humanité.

## Micro-rituel du jour (2 min)
- Identifie une routine de travail que tu rejettes par anticonformisme
- Respire et trouve ce qu'elle a de bon
- Note une façon d'améliorer le système avec pragmatisme aujourd'hui""",

    ('aquarius', 8): """# ♀️ Vénus en Verseau

**En une phrase :** Tu vis l'intimité avec liberté et ton amour se révèle dans la connexion des esprits et le respect de l'indépendance.

## Ton moteur
Ta façon d'aimer en profondeur est amicale et libre. Tu construis l'intimité par la connexion intellectuelle et le respect de l'espace.

## Ton défi
Éviter le détachement émotionnel face à l'intensité ou la peur de la fusion qui te fait fuir.

## Maison 8 en Verseau
Tu abordes les ressources partagées et l'intimité avec détachement. Les discussions profondes sont innovantes et intellectuelles.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as fui l'intensité émotionnelle par besoin de distance
- Respire et permets-toi de te rapprocher
- Note une façon de vivre l'intimité sans perdre ta liberté aujourd'hui""",

    ('aquarius', 9): """# ♀️ Vénus en Verseau

**En une phrase :** Tu trouves la beauté dans les visions progressistes et tes valeurs spirituelles sont liées à l'humanité et au futur.

## Ton moteur
Ta façon d'aimer les grandes idées est visionnaire et humaniste. Tu crois en l'évolution de l'humanité, en un futur meilleur.

## Ton défi
Éviter de rejeter les traditions ou de confondre nouveauté et progrès véritable.

## Maison 9 en Verseau
Tu abordes les voyages et la philosophie avec une vision progressiste. Ta spiritualité est universelle et tournée vers l'avenir.

## Micro-rituel du jour (2 min)
- Pense à une sagesse traditionnelle que tu rejettes par modernisme
- Respire et trouve ce qu'elle a de valable
- Note une façon d'honorer le passé dans ta vision du futur aujourd'hui""",

    ('aquarius', 11): """# ♀️ Vénus en Verseau

**En une phrase :** Tu apportes originalité et vision aux groupes et tes amitiés sont basées sur la liberté et les idéaux partagés.

## Ton moteur
Ta façon d'être ami est égalitaire et visionnaire. Tu crées des cercles où chacun est libre, tu rassembles autour d'idéaux.

## Ton défi
Éviter de rester distant même dans les amitiés proches ou de préférer l'humanité en général aux amis en particulier.

## Maison 11 en Verseau
Position renforcée : tu es naturellement douée pour les amitiés, les réseaux et les projets collectifs innovants.

## Micro-rituel du jour (2 min)
- Pense à un ami proche que tu traites comme un membre du collectif
- Respire et trouve ce qui le rend unique pour toi
- Note une façon de te connecter intimement à un ami aujourd'hui""",

    ('aquarius', 12): """# ♀️ Vénus en Verseau

**En une phrase :** Tu trouves la beauté dans la conscience cosmique et ton amour de soi se révèle dans la connexion à l'humanité entière.

## Ton moteur
Ta façon d'aimer l'invisible est universelle et détachée. Tu médites pour te connecter au collectif, tu trouves le sacré dans l'humanité.

## Ton défi
Éviter de te perdre dans l'universel au détriment de ton intimité personnelle ou de fuir l'introspection dans les grandes causes.

## Maison 12 en Verseau
Tu abordes le monde intérieur avec une vision cosmique. Tes retraites sont innovantes, ta spiritualité est universelle.

## Micro-rituel du jour (2 min)
- Identifie une fuite dans les grandes causes qui évite ton intimité propre
- Respire et reviens à toi
- Note une façon de t'aimer toi avant d'aimer l'humanité aujourd'hui""",

    # PISCES
    ('pisces', 2): """# ♀️ Vénus en Poissons

**En une phrase :** Tu trouves la beauté dans la transcendance et tes valeurs sont liées à la compassion, l'art et le sacrifice.

## Ton moteur
Ta façon d'aimer les choses matérielles est fluide et détachée. Tu donnes facilement, tu ne t'accroches pas, tu fais confiance à l'univers.

## Ton défi
Éviter la naïveté financière ou le sacrifice de tes ressources pour les autres au détriment de tes besoins.

## Maison 2 en Poissons
Tu abordes l'argent avec fluidité et foi. Tes valeurs sont spirituelles, ton rapport aux ressources est généreux et détaché.

## Micro-rituel du jour (2 min)
- Pense à une situation où tu as donné au détriment de tes besoins
- Respire et définis des limites avec amour
- Note une façon de te valoriser toi-même aujourd'hui""",

    ('pisces', 3): """# ♀️ Vénus en Poissons

**En une phrase :** Tu communiques ton affection avec poésie et tes mots portent la douceur des rêves et de l'invisible.

## Ton moteur
Ta façon d'exprimer l'amour est romantique et intuitive. Tu charmes par ta sensibilité, ta créativité verbale, ton écoute compassionnée.

## Ton défi
Éviter le flou dans tes expressions affectives ou la tendance à idéaliser plutôt qu'à voir clairement.

## Maison 3 en Poissons
Tu communiques ton affection avec poésie. Tes échanges avec l'entourage sont empathiques et intuitifs.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as idéalisé au lieu de voir clairement
- Respire et trouve la beauté dans le réel
- Note une façon de communiquer ton amour avec clarté et douceur aujourd'hui""",

    ('pisces', 5): """# ♀️ Vénus en Poissons

**En une phrase :** Tu aimes avec dévotion et ta créativité s'exprime dans l'art, l'imaginaire et la connexion au sacré.

## Ton moteur
Ta façon de vivre l'amour et les plaisirs est romantique et idéaliste. Tu veux des romances de conte de fées, une créativité inspirée.

## Ton défi
Éviter de te perdre dans des amours impossibles ou de fuir la réalité dans les fantasmes.

## Maison 5 en Poissons
Tu abordes les romances et la créativité avec rêve. Tes amours sont idéalisées, ta créativité est inspirée et transcendante.

## Micro-rituel du jour (2 min)
- Pense à un amour ou un projet créatif que tu as idéalisé au point de le rendre impossible
- Respire et trouve la beauté dans le possible
- Note une façon de créer ou d'aimer dans le réel aujourd'hui""",

    ('pisces', 6): """# ♀️ Vénus en Poissons

**En une phrase :** Tu apportes de la beauté au quotidien par la compassion, le service désintéressé et la guérison.

## Ton moteur
Ta façon de rendre le travail agréable est d'y apporter de la compassion et du sens sacré. Tu veux servir, guérir, transcender.

## Ton défi
Éviter de te sacrifier au travail ou de ne pas poser de limites claires avec ceux que tu aides.

## Maison 6 en Poissons
Tu abordes le service et la routine avec compassion. Tu veux que le quotidien soit au service de quelque chose de plus grand.

## Micro-rituel du jour (2 min)
- Identifie un moment où tu te sacrifies au travail
- Respire et pose une limite avec amour
- Note une façon de servir tout en te protégeant aujourd'hui""",

    ('pisces', 8): """# ♀️ Vénus en Poissons

**En une phrase :** Tu vis l'intimité avec fusion et ton amour se révèle dans la dissolution des frontières et l'union des âmes.

## Ton moteur
Ta façon d'aimer en profondeur est totale et transcendante. Tu veux fusionner complètement, te dissoudre dans l'autre.

## Ton défi
Éviter de te perdre dans l'autre ou de confondre sacrifice et amour véritable.

## Maison 8 en Poissons
Tu abordes les ressources partagées et l'intimité avec fluidité. Les discussions profondes sont mystiques et fusionnelles.

## Micro-rituel du jour (2 min)
- Pense à une relation où tu t'es perdu dans l'autre
- Respire et retrouve ton centre
- Note une façon d'aimer profondément tout en restant toi aujourd'hui""",

    ('pisces', 9): """# ♀️ Vénus en Poissons

**En une phrase :** Tu trouves la beauté dans la transcendance et tes valeurs spirituelles sont liées à l'unité et à la compassion universelle.

## Ton moteur
Ta façon d'aimer les grandes idées est mystique et unifiante. Tu sens l'unité de tout, tu aimes sans frontières.

## Ton défi
Éviter de te perdre dans les illusions spirituelles ou de confondre fuite et transcendance.

## Maison 9 en Poissons
Tu abordes les voyages et la philosophie avec mysticisme. Ta spiritualité est intuitive et universelle.

## Micro-rituel du jour (2 min)
- Pense à une croyance qui pourrait être une fuite plutôt qu'une sagesse
- Respire et passe-la au filtre du discernement
- Note une façon de vivre ta spiritualité avec les pieds sur terre aujourd'hui""",

    ('pisces', 11): """# ♀️ Vénus en Poissons

**En une phrase :** Tu apportes compassion et rêve aux groupes et tes amitiés sont des sanctuaires d'amour inconditionnel.

## Ton moteur
Ta façon d'être ami est aimante et sans jugement. Tu accueilles tous, tu pardonnes tout, tu crées des cercles de guérison.

## Ton défi
Éviter de te sacrifier pour le groupe ou d'attirer des amis qui profitent de ta générosité.

## Maison 11 en Poissons
Tu abordes les amitiés et projets collectifs avec compassion. Tes amis sont comme une famille spirituelle, tes idéaux visent la guérison.

## Micro-rituel du jour (2 min)
- Pense à un ami qui profite peut-être de ta générosité
- Respire et pose des limites avec amour
- Note une façon de contribuer au groupe tout en te protégeant aujourd'hui""",

    ('pisces', 12): """# ♀️ Vénus en Poissons

**En une phrase :** Tu trouves la beauté dans la dissolution de l'ego et ton amour de soi se révèle dans l'union avec le tout.

## Ton moteur
Ta façon d'aimer l'invisible est ton élément naturel. Tu médites pour te dissoudre, tu aimes sans frontières, tu es une avec l'univers.

## Ton défi
Éviter de fuir la réalité dans les rêves ou de te perdre tellement que tu oublies de prendre soin de toi.

## Maison 12 en Poissons
Position renforcée : tu es naturellement connectée à l'invisible, au rêve, à la transcendance. Ta vie intérieure est infinie.

## Micro-rituel du jour (2 min)
- Identifie une fuite dans le rêve qui évite une responsabilité terrestre
- Respire et reviens dans ton corps
- Note une façon de vivre la transcendance dans le quotidien aujourd'hui""",
}


async def main():
    async with AsyncSessionLocal() as db:
        count = 0
        for (sign, house), content in VENUS_INTERPRETATIONS.items():
            result = await db.execute(
                update(PregeneratedNatalInterpretation)
                .where(
                    PregeneratedNatalInterpretation.subject == 'venus',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house
                )
                .values(content=content)
            )
            if result.rowcount > 0:
                count += result.rowcount

        await db.commit()
        print(f"Done: {count} venus interpretations updated")


if __name__ == "__main__":
    asyncio.run(main())
