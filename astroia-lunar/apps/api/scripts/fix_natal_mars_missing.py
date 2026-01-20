#!/usr/bin/env python3
"""
Script pour corriger les 96 interprétations MARS manquantes (maisons 2,3,5,6,8,9,11,12)
Format natal V2 avec: En une phrase / Ton moteur / Ton défi / Maison X / Micro-rituel
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import update
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

# Interprétations MARS format V2 - Maisons 2,3,5,6,8,9,11,12 pour les 12 signes
MARS_INTERPRETATIONS = {
    # ARIES
    ('aries', 2): """# ♂️ Mars en Bélier

**En une phrase :** Tu agis pour conquérir tes ressources avec audace, rapidité et indépendance totale.

## Ton moteur
Ta façon de passer à l'action pour l'argent est directe et compétitive. Tu veux gagner vite, par toi-même, avec énergie.

## Ton défi
Éviter les décisions financières impulsives ou l'agressivité quand tes ressources sont menacées.

## Maison 2 en Bélier
Tu agis sur tes valeurs et tes ressources avec feu et initiative. Tu es un conquérant financier, rapide et audacieux.

## Micro-rituel du jour (2 min)
- Pense à une action financière impulsive récente
- Respire et identifie l'émotion derrière l'impulsion
- Note une façon de canaliser ton énergie financière aujourd'hui""",

    ('aries', 3): """# ♂️ Mars en Bélier

**En une phrase :** Tu communiques avec fougue et tes mots sont des flèches qui vont droit au but.

## Ton moteur
Ta façon de passer à l'action dans la communication est directe et percutante. Tu dis ce que tu penses, immédiatement.

## Ton défi
Éviter de blesser par des mots trop directs ou de déclencher des conflits par impatience verbale.

## Maison 3 en Bélier
Tu agis dans la communication avec énergie. Tu défends tes idées avec passion, parfois avec agressivité.

## Micro-rituel du jour (2 min)
- Pense à une parole récente qui a blessé par sa franchise
- Respire et trouve une reformulation plus douce
- Note une façon de t'exprimer avec force mais sans violence aujourd'hui""",

    ('aries', 5): """# ♂️ Mars en Bélier

**En une phrase :** Tu crées et aimes avec passion brûlante, cherchant l'excitation et la conquête.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est fougueuse et compétitive. Tu veux être le premier, le meilleur.

## Ton défi
Éviter de transformer le jeu en compétition ou de te lasser quand la conquête est faite.

## Maison 5 en Bélier
Tu agis dans la créativité et les plaisirs avec feu. Tes romances sont des aventures, ta créativité est impulsive.

## Micro-rituel du jour (2 min)
- Pense à un projet créatif ou une relation abandonnée après la phase de conquête
- Respire et trouve l'énergie pour le second souffle
- Note une façon de créer ou aimer avec patience aujourd'hui""",

    ('aries', 6): """# ♂️ Mars en Bélier

**En une phrase :** Tu travailles avec énergie explosive et tu veux des résultats immédiats dans tout ce que tu fais.

## Ton moteur
Ta façon de passer à l'action au quotidien est efficace et directe. Tu attaques les problèmes de front, tu veux de l'action.

## Ton défi
Éviter l'épuisement par hyperactivité ou l'impatience face aux tâches qui demandent du temps.

## Maison 6 en Bélier
Tu agis dans le travail quotidien avec dynamisme. Tu veux que les choses avancent, vite et bien.

## Micro-rituel du jour (2 min)
- Identifie une tâche que tu bâcles par impatience
- Respire et accorde-lui l'attention qu'elle mérite
- Note une façon de travailler efficacement sans te brûler aujourd'hui""",

    ('aries', 8): """# ♂️ Mars en Bélier

**En une phrase :** Tu affrontes les crises avec courage et tu transformes les obstacles en terrain de conquête.

## Ton moteur
Ta façon de passer à l'action face aux transformations est courageuse et directe. Tu fonces dans les ténèbres sans peur.

## Ton défi
Éviter de provoquer des crises par impatience ou de fuir la vulnérabilité dans l'action agressive.

## Maison 8 en Bélier
Tu agis dans les transformations avec courage. Tu affrontes les tabous, les peurs, la mort avec énergie combative.

## Micro-rituel du jour (2 min)
- Pense à une crise que tu as provoquée par impatience
- Respire et identifie ce que la patience aurait permis
- Note une façon d'affronter les profondeurs sans combattre aujourd'hui""",

    ('aries', 9): """# ♂️ Mars en Bélier

**En une phrase :** Tu poursuis la vérité avec passion et tu défends tes convictions comme un guerrier.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est ardente et combative. Tu explores avec fougue, tu débats avec feu.

## Ton défi
Éviter d'imposer tes vérités ou de transformer les discussions philosophiques en batailles.

## Maison 9 en Bélier
Tu agis dans la quête de sens avec énergie. Tes voyages sont des aventures, tes convictions sont défendues avec passion.

## Micro-rituel du jour (2 min)
- Pense à un débat où tu as voulu gagner plutôt que comprendre
- Respire et trouve la curiosité derrière la conviction
- Note une façon de défendre tes idées avec ouverture aujourd'hui""",

    ('aries', 11): """# ♂️ Mars en Bélier

**En une phrase :** Tu prends l'initiative dans les groupes et tu mènes tes amis vers l'action.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de leader. Tu initie, tu motive, tu entraînes le groupe.

## Ton défi
Éviter de vouloir toujours mener ou de t'impatienter face aux décisions collectives lentes.

## Maison 11 en Bélier
Tu agis dans les groupes et amitiés avec énergie de pionnier. Tu es celui qui lance les projets, qui motive les autres.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu as voulu trop mener
- Respire et trouve la joie de suivre parfois
- Note une façon de soutenir sans diriger aujourd'hui""",

    ('aries', 12): """# ♂️ Mars en Bélier

**En une phrase :** Tu combats tes démons intérieurs avec courage et tu transformes l'ombre en force.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est courageuse et directe. Tu affrontes tes peurs de front.

## Ton défi
Éviter de combattre des parts de toi qui demandent acceptation ou de fuir l'introspection dans l'hyperactivité.

## Maison 12 en Bélier
Tu agis dans le monde invisible avec courage. Tes retraites sont actives, ta spiritualité est combative.

## Micro-rituel du jour (2 min)
- Identifie une peur intérieure que tu combats au lieu d'accueillir
- Respire et offre-lui de la compassion
- Note une façon de faire la paix avec ton ombre aujourd'hui""",

    # TAURUS
    ('taurus', 2): """# ♂️ Mars en Taureau

**En une phrase :** Tu agis pour construire ta sécurité avec patience, persévérance et détermination inébranlable.

## Ton moteur
Ta façon de passer à l'action pour l'argent est méthodique et tenace. Tu construis lentement mais solidement.

## Ton défi
Éviter l'entêtement qui bloque les opportunités ou la lenteur excessive face aux situations urgentes.

## Maison 2 en Taureau
Position renforcée : tu agis sur tes ressources avec une détermination naturelle et une patience qui porte ses fruits.

## Micro-rituel du jour (2 min)
- Pense à une opportunité financière que tu as manquée par lenteur
- Respire et trouve l'équilibre entre prudence et réactivité
- Note une action concrète pour tes ressources aujourd'hui""",

    ('taurus', 3): """# ♂️ Mars en Taureau

**En une phrase :** Tu communiques avec constance et tes mots ont le poids de la terre et de la conviction.

## Ton moteur
Ta façon de passer à l'action dans la communication est posée et déterminée. Tu dis peu mais avec impact.

## Ton défi
Éviter l'entêtement dans tes positions ou la lenteur qui frustre ceux qui attendent une réponse.

## Maison 3 en Taureau
Tu agis dans la communication avec stabilité. Tu défends tes idées avec ténacité, parfois avec obstination.

## Micro-rituel du jour (2 min)
- Pense à une opinion à laquelle tu t'accroches par habitude
- Respire et questionne-la honnêtement
- Note une façon de communiquer avec fermeté mais flexibilité aujourd'hui""",

    ('taurus', 5): """# ♂️ Mars en Taureau

**En une phrase :** Tu crées et aimes avec sensualité et constance, cherchant la durabilité plutôt que l'excitation.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est patiente et sensorielle. Tu construis pour durer.

## Ton défi
Éviter la possessivité en amour ou l'entêtement créatif qui bloque l'évolution.

## Maison 5 en Taureau
Tu agis dans la créativité et les plaisirs avec sensualité. Tes romances sont fidèles, ta créativité est artisanale.

## Micro-rituel du jour (2 min)
- Pense à une possessivité qui a pu nuire à une relation ou création
- Respire et trouve la sécurité intérieure
- Note une façon de créer ou aimer avec confiance sans posséder aujourd'hui""",

    ('taurus', 6): """# ♂️ Mars en Taureau

**En une phrase :** Tu travailles avec endurance et méthode, préférant la qualité à la vitesse.

## Ton moteur
Ta façon de passer à l'action au quotidien est méthodique et fiable. Tu avances à ton rythme, avec résultats durables.

## Ton défi
Éviter l'enlisement dans les routines ou la résistance aux changements nécessaires dans le travail.

## Maison 6 en Taureau
Tu agis dans le travail quotidien avec constance. Tu es fiable, productif, mais parfois résistant aux nouvelles méthodes.

## Micro-rituel du jour (2 min)
- Identifie une méthode de travail que tu gardes par habitude
- Respire et questionne son efficacité actuelle
- Note une amélioration à essayer dans ta routine aujourd'hui""",

    ('taurus', 8): """# ♂️ Mars en Taureau

**En une phrase :** Tu traverses les transformations avec endurance et tu ancres les changements dans la durée.

## Ton moteur
Ta façon de passer à l'action face aux transformations est patiente et résiliente. Tu changes lentement mais profondément.

## Ton défi
Éviter de résister aux transformations nécessaires ou de s'accrocher à ce qui doit mourir.

## Maison 8 en Taureau
Tu agis dans les transformations avec ténacité. Tu traverses les crises avec endurance, mais tu peux résister au changement.

## Micro-rituel du jour (2 min)
- Pense à un changement profond auquel tu résistes
- Respire et trouve un premier pas vers l'acceptation
- Note une façon de te transformer avec douceur aujourd'hui""",

    ('taurus', 9): """# ♂️ Mars en Taureau

**En une phrase :** Tu poursuis la vérité avec pragmatisme et tu ancres tes convictions dans l'expérience concrète.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est pratique et persévérante. Tu préfères vivre ta philosophie qu'en débattre.

## Ton défi
Éviter de t'entêter dans des croyances dépassées ou de rejeter les idées qui ne semblent pas pratiques.

## Maison 9 en Taureau
Tu agis dans la quête de sens avec constance. Tes voyages sont gourmands, tes convictions sont ancrées dans le vécu.

## Micro-rituel du jour (2 min)
- Pense à une croyance que tu gardes par habitude sans l'avoir questionnée
- Respire et examine-la avec fraîcheur
- Note une façon de vivre ta philosophie concrètement aujourd'hui""",

    ('taurus', 11): """# ♂️ Mars en Taureau

**En une phrase :** Tu apportes stabilité et persévérance aux groupes et tu concrétises les projets collectifs.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de bâtisseur. Tu concrétises, tu stabilises, tu fais durer.

## Ton défi
Éviter de freiner les innovations du groupe ou de t'entêter dans des méthodes dépassées.

## Maison 11 en Taureau
Tu agis dans les groupes et amitiés avec constance. Tu es le pilier fiable, celui qui construit vraiment.

## Micro-rituel du jour (2 min)
- Pense à une idée de groupe que tu as freinée par prudence
- Respire et trouve ce qu'elle pourrait apporter
- Note une façon de contribuer à l'innovation collective aujourd'hui""",

    ('taurus', 12): """# ♂️ Mars en Taureau

**En une phrase :** Tu travailles sur ton monde intérieur avec patience et tu ancres ta spiritualité dans le corps.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est incarnée et persévérante. Tu médites dans le corps.

## Ton défi
Éviter de fuir l'introspection dans le confort matériel ou de résister aux transformations spirituelles.

## Maison 12 en Taureau
Tu agis dans le monde invisible avec ancrage. Tes retraites sont sensuelles, ta spiritualité est terrestre.

## Micro-rituel du jour (2 min)
- Identifie une fuite dans le confort qui évite une introspection nécessaire
- Respire et accorde-toi un moment d'intériorité
- Note une façon de méditer dans le corps aujourd'hui""",

    # GEMINI
    ('gemini', 2): """# ♂️ Mars en Gémeaux

**En une phrase :** Tu agis pour tes ressources avec agilité, multipliant les stratégies et les sources de revenus.

## Ton moteur
Ta façon de passer à l'action pour l'argent est vive et adaptable. Tu as plusieurs idées en même temps, tu t'adaptes vite.

## Ton défi
Éviter la dispersion financière ou les changements de stratégie trop fréquents qui empêchent les résultats.

## Maison 2 en Gémeaux
Tu agis sur tes ressources avec intelligence et polyvalence. Tu sais jongler avec plusieurs sources de revenus.

## Micro-rituel du jour (2 min)
- Pense à une stratégie financière que tu as abandonnée trop vite
- Respire et évalue si elle méritait plus de temps
- Note une action financière à mener jusqu'au bout aujourd'hui""",

    ('gemini', 3): """# ♂️ Mars en Gémeaux

**En une phrase :** Tu communiques avec vivacité et tu excelles dans les débats, les négociations et les joutes verbales.

## Ton moteur
Ta façon de passer à l'action dans la communication est rapide et percutante. Tu as la répartie, tu penses vite.

## Ton défi
Éviter la dispersion verbale ou les conflits créés par des mots lancés trop vite.

## Maison 3 en Gémeaux
Position renforcée : tu agis dans la communication avec une agilité exceptionnelle. Tu es le maître des mots et des idées.

## Micro-rituel du jour (2 min)
- Pense à une parole lancée trop vite qui a créé un conflit
- Respire et trouve une façon de réparer
- Note une intention de parler avec plus de conscience aujourd'hui""",

    ('gemini', 5): """# ♂️ Mars en Gémeaux

**En une phrase :** Tu crées et aimes avec esprit, cherchant la stimulation intellectuelle et la variété.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est cérébrale et joueuse. Tu aimes le flirt des mots.

## Ton défi
Éviter de rester en surface ou de papillonner sans jamais approfondir les connexions.

## Maison 5 en Gémeaux
Tu agis dans la créativité et les plaisirs avec légèreté. Tes romances sont cérébrales, ta créativité est verbale.

## Micro-rituel du jour (2 min)
- Pense à une relation ou création que tu as survolée
- Respire et trouve ce qui pourrait l'approfondir
- Note une façon de créer ou aimer avec plus de profondeur aujourd'hui""",

    ('gemini', 6): """# ♂️ Mars en Gémeaux

**En une phrase :** Tu travailles avec agilité mentale, jonglant avec plusieurs tâches et adaptant tes méthodes.

## Ton moteur
Ta façon de passer à l'action au quotidien est flexible et intellectuelle. Tu aimes la variété, le multitâche.

## Ton défi
Éviter la dispersion ou l'incapacité à terminer une tâche avant d'en commencer une autre.

## Maison 6 en Gémeaux
Tu agis dans le travail quotidien avec adaptabilité. Tu gères bien plusieurs projets, mais finis-tu vraiment ?

## Micro-rituel du jour (2 min)
- Identifie une tâche en cours que tu n'as pas terminée
- Respire et engage-toi à la finir
- Note une façon de te concentrer sur une chose à la fois aujourd'hui""",

    ('gemini', 8): """# ♂️ Mars en Gémeaux

**En une phrase :** Tu traverses les transformations en les analysant et en les exprimant par les mots.

## Ton moteur
Ta façon de passer à l'action face aux transformations est intellectuelle et communicative. Tu parles pour comprendre.

## Ton défi
Éviter de rationaliser les profondeurs au lieu de les vivre ou de fuir l'intensité dans le bavardage.

## Maison 8 en Gémeaux
Tu agis dans les transformations avec curiosité. Tu explores les tabous par la pensée, tu analyses les crises.

## Micro-rituel du jour (2 min)
- Pense à une émotion profonde que tu as analysée au lieu de vivre
- Respire et laisse-la simplement être
- Note une façon de traverser l'intensité au-delà des mots aujourd'hui""",

    ('gemini', 9): """# ♂️ Mars en Gémeaux

**En une phrase :** Tu poursuis la vérité en explorant toutes les perspectives et en débattant avec passion.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est curieuse et dialectique. Tu aimes comparer, débattre, nuancer.

## Ton défi
Éviter de survoler trop de systèmes de pensée ou de préférer le débat à l'intégration de la sagesse.

## Maison 9 en Gémeaux
Tu agis dans la quête de sens avec curiosité. Tes voyages sont intellectuels, tes convictions sont multiples.

## Micro-rituel du jour (2 min)
- Pense à une sagesse que tu connais mais n'as pas intégrée
- Respire et trouve une façon de la vivre
- Note une croyance à approfondir au lieu d'en explorer une nouvelle aujourd'hui""",

    ('gemini', 11): """# ♂️ Mars en Gémeaux

**En une phrase :** Tu animes les groupes avec ton énergie communicative et tu connectes les idées et les personnes.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de connecteur. Tu fais circuler l'information, tu stimules les échanges.

## Ton défi
Éviter de t'éparpiller dans trop de groupes ou de créer des conflits par des mots mal choisis.

## Maison 11 en Gémeaux
Tu agis dans les groupes et amitiés avec vivacité. Tu es celui qui anime, qui connecte, qui fait circuler les idées.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu parles plus que tu n'écoutes
- Respire et trouve la valeur du silence
- Note une façon de contribuer au groupe par l'écoute aujourd'hui""",

    ('gemini', 12): """# ♂️ Mars en Gémeaux

**En une phrase :** Tu explores ton monde intérieur par la pensée et tu transformes l'inconscient par les mots.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est intellectuelle et exploratoire. Tu médites en questionnant.

## Ton défi
Éviter de rester en surface de ton âme ou de rationaliser le mystère au lieu de le vivre.

## Maison 12 en Gémeaux
Tu agis dans le monde invisible avec curiosité. Tes retraites sont studieuses, ta spiritualité est intellectuelle.

## Micro-rituel du jour (2 min)
- Identifie une question intérieure que tu analyses sans fin
- Respire et laisse le silence répondre
- Note une façon de méditer au-delà de la pensée aujourd'hui""",

    # CANCER
    ('cancer', 2): """# ♂️ Mars en Cancer

**En une phrase :** Tu agis pour ta sécurité avec une énergie protectrice, défendant ce qui te nourrit et te rassure.

## Ton moteur
Ta façon de passer à l'action pour l'argent est émotionnelle et protectrice. Tu défends tes ressources comme un nid.

## Ton défi
Éviter l'agressivité passive quand tu te sens menacé financièrement ou les décisions impulsives sous l'émotion.

## Maison 2 en Cancer
Tu agis sur tes ressources avec une énergie de protection. Tu veux sécuriser ta famille, ton foyer, ton confort.

## Micro-rituel du jour (2 min)
- Pense à une réaction financière influencée par la peur
- Respire et sépare l'émotion de la décision
- Note une action financière réfléchie à poser aujourd'hui""",

    ('cancer', 3): """# ♂️ Mars en Cancer

**En une phrase :** Tu communiques avec passion émotionnelle et tu défends ceux que tu aimes avec tes mots.

## Ton moteur
Ta façon de passer à l'action dans la communication est protectrice et intuitive. Tu sens ce qu'il faut dire.

## Ton défi
Éviter l'agressivité passive ou la tendance à blesser par rancune quand tu te sens mal compris.

## Maison 3 en Cancer
Tu agis dans la communication avec émotion. Tu défends ta famille, tes proches, avec la force de tes mots.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as blessé par rancune
- Respire et trouve une façon de communiquer directement
- Note une intention d'expression émotionnelle saine aujourd'hui""",

    ('cancer', 5): """# ♂️ Mars en Cancer

**En une phrase :** Tu crées et aimes avec dévotion, investissant ton énergie dans la protection et la nourriture affective.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est maternante et dévouée. Tu crées pour protéger.

## Ton défi
Éviter la possessivité émotionnelle ou l'agressivité quand tu te sens rejeté en amour.

## Maison 5 en Cancer
Tu agis dans la créativité et les plaisirs avec émotion. Tes romances sont protectrices, ta créativité est nourrissante.

## Micro-rituel du jour (2 min)
- Pense à une réaction excessive face à un rejet en amour ou créativité
- Respire et trouve la sécurité en toi
- Note une façon de créer ou aimer sans dépendance émotionnelle aujourd'hui""",

    ('cancer', 6): """# ♂️ Mars en Cancer

**En une phrase :** Tu travailles avec une énergie protectrice, prenant soin de ton équipe et de ton environnement.

## Ton moteur
Ta façon de passer à l'action au quotidien est intuitive et attentionnée. Tu sens ce dont les autres ont besoin.

## Ton défi
Éviter de te laisser submerger par les émotions au travail ou de réagir de façon passive-agressive.

## Maison 6 en Cancer
Tu agis dans le travail quotidien avec sensibilité. Tu prends soin des autres, mais attention à ne pas t'épuiser.

## Micro-rituel du jour (2 min)
- Identifie une situation de travail qui t'affecte émotionnellement
- Respire et pose des limites protectrices
- Note une façon de travailler sans absorber les émotions des autres aujourd'hui""",

    ('cancer', 8): """# ♂️ Mars en Cancer

**En une phrase :** Tu traverses les transformations avec une force émotionnelle profonde, protégeant et nourrissant à travers les crises.

## Ton moteur
Ta façon de passer à l'action face aux transformations est protectrice et intuitive. Tu sens les courants souterrains.

## Ton défi
Éviter de te replier dans ta coquille face à l'intensité ou de manipuler par les émotions.

## Maison 8 en Cancer
Tu agis dans les transformations avec émotion. Tu traverses les crises en protégeant, mais parfois tu te fermes.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu t'es fermé face à une transformation nécessaire
- Respire et trouve le courage de rester ouvert
- Note une façon de traverser l'intensité avec le cœur ouvert aujourd'hui""",

    ('cancer', 9): """# ♂️ Mars en Cancer

**En une phrase :** Tu poursuis la vérité avec une passion émotionnelle, cherchant des croyances qui te nourrissent.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est intuitive et protectrice. Tu défends les traditions qui te rassurent.

## Ton défi
Éviter de rejeter les idées qui ne résonnent pas émotionnellement ou de s'accrocher aux croyances familiales sans les questionner.

## Maison 9 en Cancer
Tu agis dans la quête de sens avec émotion. Tes voyages cherchent un "chez soi", ta spiritualité est ancestrale.

## Micro-rituel du jour (2 min)
- Pense à une croyance familiale que tu n'as jamais questionnée
- Respire et examine-la avec amour mais honnêteté
- Note une façon d'explorer de nouvelles sagesses tout en honorant tes racines aujourd'hui""",

    ('cancer', 11): """# ♂️ Mars en Cancer

**En une phrase :** Tu apportes une énergie protectrice aux groupes et tu défends tes amis comme une famille.

## Ton moteur
Ta façon de passer à l'action dans le collectif est maternante et loyale. Tu protèges le groupe, tu en fais un foyer.

## Ton défi
Éviter de projeter tes besoins familiaux sur le groupe ou de te replier si tu ne te sens pas assez nourri.

## Maison 11 en Cancer
Tu agis dans les groupes et amitiés avec émotion. Tes amis sont ta famille, tu les défends avec passion.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu attends trop en retour
- Respire et ajuste tes attentes
- Note une façon de contribuer au groupe sans condition aujourd'hui""",

    ('cancer', 12): """# ♂️ Mars en Cancer

**En une phrase :** Tu travailles sur ton monde intérieur avec une énergie de protection, guérissant les blessures de l'âme.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est intuitive et nourrissante. Tu médites pour te guérir.

## Ton défi
Éviter de te perdre dans les émotions inconscientes ou de fuir le présent dans la nostalgie.

## Maison 12 en Cancer
Tu agis dans le monde invisible avec sensibilité. Tes retraites sont comme un retour au berceau, ta spiritualité est intuitive.

## Micro-rituel du jour (2 min)
- Identifie une émotion inconsciente qui te submerge régulièrement
- Respire et accueille-la comme un enfant intérieur
- Note une façon de te materner toi-même aujourd'hui""",

    # LEO
    ('leo', 2): """# ♂️ Mars en Lion

**En une phrase :** Tu agis pour tes ressources avec fierté et générosité, voulant briller par ce que tu possèdes.

## Ton moteur
Ta façon de passer à l'action pour l'argent est ambitieuse et noble. Tu veux gagner pour partager, pour impressionner.

## Ton défi
Éviter les dépenses ostentatoires ou l'orgueil blessé quand tes ressources ne te permettent pas de briller.

## Maison 2 en Lion
Tu agis sur tes ressources avec générosité et fierté. Tu veux que ton argent reflète ta grandeur.

## Micro-rituel du jour (2 min)
- Pense à une dépense récente faite pour impressionner
- Respire et trouve ta valeur indépendamment de tes biens
- Note une façon de te sentir noble sans dépenser aujourd'hui""",

    ('leo', 3): """# ♂️ Mars en Lion

**En une phrase :** Tu communiques avec charisme et autorité, tes mots portent la puissance du soleil.

## Ton moteur
Ta façon de passer à l'action dans la communication est confiante et théâtrale. Tu veux être entendu et admiré.

## Ton défi
Éviter de monopoliser la parole ou de réagir avec orgueil quand on ne t'écoute pas.

## Maison 3 en Lion
Tu agis dans la communication avec charisme. Tu parles pour briller, tu défends tes idées avec noblesse.

## Micro-rituel du jour (2 min)
- Pense à un moment où ton besoin d'attention a nui à la communication
- Respire et trouve la joie de faire briller les autres
- Note une façon de communiquer avec humilité aujourd'hui""",

    ('leo', 5): """# ♂️ Mars en Lion

**En une phrase :** Tu crées et aimes avec passion flamboyante, cherchant la scène et les applaudissements.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est royale et généreuse. Tu donnes tout sur scène.

## Ton défi
Éviter de créer ou aimer pour être admiré plutôt que pour la joie pure de l'expression.

## Maison 5 en Lion
Position renforcée : tu agis dans la créativité et les plaisirs avec une énergie solaire. Tu es né pour briller.

## Micro-rituel du jour (2 min)
- Pense à une création ou un amour où tu as cherché plus d'admiration que de connexion
- Respire et trouve la joie intrinsèque
- Note une façon de créer ou aimer pour le plaisir pur aujourd'hui""",

    ('leo', 6): """# ♂️ Mars en Lion

**En une phrase :** Tu travailles avec générosité et leadership, voulant que ton travail soit reconnu et admiré.

## Ton moteur
Ta façon de passer à l'action au quotidien est ambitieuse et inspirante. Tu mènes par l'exemple.

## Ton défi
Éviter de chercher la reconnaissance au détriment du travail ou de mal vivre les critiques.

## Maison 6 en Lion
Tu agis dans le travail quotidien avec fierté. Tu veux exceller, être reconnu, inspirer les autres.

## Micro-rituel du jour (2 min)
- Identifie une tâche que tu négliges car elle ne te met pas en valeur
- Respire et trouve la noblesse dans le service humble
- Note une façon de travailler sans chercher de reconnaissance aujourd'hui""",

    ('leo', 8): """# ♂️ Mars en Lion

**En une phrase :** Tu traverses les transformations avec courage dramatique, illuminant les ténèbres de ta lumière.

## Ton moteur
Ta façon de passer à l'action face aux transformations est courageuse et théâtrale. Tu affrontes l'ombre avec panache.

## Ton défi
Éviter de dramatiser les crises ou de vouloir être le héros de toutes les transformations.

## Maison 8 en Lion
Tu agis dans les transformations avec courage. Tu éclaires les profondeurs, mais parfois tu en fais trop.

## Micro-rituel du jour (2 min)
- Pense à une crise où tu as voulu être au centre
- Respire et accepte d'être un acteur parmi d'autres
- Note une façon de traverser l'intensité sans en faire un spectacle aujourd'hui""",

    ('leo', 9): """# ♂️ Mars en Lion

**En une phrase :** Tu poursuis la vérité avec passion généreuse, voulant partager ta lumière avec le monde.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est inspirante et confiante. Tu veux enseigner, guider, inspirer.

## Ton défi
Éviter l'orgueil spirituel ou la croyance que ta vérité est la seule lumière.

## Maison 9 en Lion
Tu agis dans la quête de sens avec générosité. Tes voyages sont grandioses, tes convictions rayonnent.

## Micro-rituel du jour (2 min)
- Pense à une conviction que tu défends avec trop d'orgueil
- Respire et trouve l'humilité dans ta foi
- Note une façon d'inspirer sans prêcher aujourd'hui""",

    ('leo', 11): """# ♂️ Mars en Lion

**En une phrase :** Tu mènes les groupes avec charisme et générosité, voulant que le collectif brille.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de leader généreux. Tu motives, tu inspires, tu donnes.

## Ton défi
Éviter de vouloir toujours mener ou de te sentir blessé si le groupe ne t'acclame pas.

## Maison 11 en Lion
Tu agis dans les groupes et amitiés avec noblesse. Tu veux que tes amis brillent, mais toi aussi.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu voudrais être plus reconnu
- Respire et trouve la joie de voir les autres briller
- Note une façon de célébrer un ami aujourd'hui""",

    ('leo', 12): """# ♂️ Mars en Lion

**En une phrase :** Tu travailles sur ton monde intérieur avec courage, cherchant à faire briller même ton ombre.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est lumineuse et créative. Tu transformes l'ombre en or.

## Ton défi
Éviter de vouloir briller même dans l'invisible ou de fuir l'humilité que demande l'âme.

## Maison 12 en Lion
Tu agis dans le monde invisible avec courage créatif. Tes retraites sont artistiques, ta spiritualité veut rayonner.

## Micro-rituel du jour (2 min)
- Identifie une part de toi que tu caches car elle ne brille pas
- Respire et accueille-la avec compassion
- Note une façon d'aimer ton ombre aujourd'hui""",

    # VIRGO
    ('virgo', 2): """# ♂️ Mars en Vierge

**En une phrase :** Tu agis pour tes ressources avec méthode et précision, optimisant chaque aspect de ta gestion.

## Ton moteur
Ta façon de passer à l'action pour l'argent est analytique et efficace. Tu planifies, tu optimises, tu améliores.

## Ton défi
Éviter l'anxiété financière ou la paralysie par excès d'analyse.

## Maison 2 en Vierge
Tu agis sur tes ressources avec rigueur et discernement. Tu es un gestionnaire méticuleux.

## Micro-rituel du jour (2 min)
- Pense à une décision financière que tu repousses par excès d'analyse
- Respire et choisis d'agir
- Note une action financière simple à accomplir aujourd'hui""",

    ('virgo', 3): """# ♂️ Mars en Vierge

**En une phrase :** Tu communiques avec précision et efficacité, tes mots visent l'amélioration et le service.

## Ton moteur
Ta façon de passer à l'action dans la communication est analytique et utile. Tu parles pour aider, corriger, améliorer.

## Ton défi
Éviter la critique excessive ou les remarques qui blessent au lieu d'aider.

## Maison 3 en Vierge
Tu agis dans la communication avec précision. Tu analyses, tu corriges, parfois tu critiques trop.

## Micro-rituel du jour (2 min)
- Pense à une critique récente qui a pu blesser
- Respire et trouve une reformulation plus encourageante
- Note une façon d'aider par tes mots sans corriger aujourd'hui""",

    ('virgo', 5): """# ♂️ Mars en Vierge

**En une phrase :** Tu crées et aimes avec attention au détail, perfectionnant chaque aspect de ton expression.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est méticuleuse et dévouée. Tu travailles ton art.

## Ton défi
Éviter le perfectionnisme qui bloque la création ou la critique qui tue la romance.

## Maison 5 en Vierge
Tu agis dans la créativité et les plaisirs avec rigueur. Tes romances sont serviables, ta créativité est artisanale.

## Micro-rituel du jour (2 min)
- Pense à une création bloquée par perfectionnisme
- Respire et accepte l'imperfection comme beauté
- Note une façon de créer ou aimer sans viser la perfection aujourd'hui""",

    ('virgo', 6): """# ♂️ Mars en Vierge

**En une phrase :** Tu travailles avec efficacité maximale, optimisant chaque processus et servant avec dévouement.

## Ton moteur
Ta façon de passer à l'action au quotidien est méthodique et perfectionniste. Tu veux l'excellence dans chaque détail.

## Ton défi
Éviter le workaholisme ou la critique constante de ton propre travail et de celui des autres.

## Maison 6 en Vierge
Position renforcée : tu agis dans le travail quotidien avec une efficacité naturelle. Tu es le maître de l'optimisation.

## Micro-rituel du jour (2 min)
- Identifie une tâche que tu recommences sans fin car jamais assez parfaite
- Respire et accepte qu'elle est suffisante
- Note une façon de te féliciter pour ton travail aujourd'hui""",

    ('virgo', 8): """# ♂️ Mars en Vierge

**En une phrase :** Tu traverses les transformations avec méthode, analysant et optimisant le processus de changement.

## Ton moteur
Ta façon de passer à l'action face aux transformations est analytique et pratique. Tu gères les crises avec méthode.

## Ton défi
Éviter de vouloir contrôler les transformations ou de rationaliser l'intensité au lieu de la vivre.

## Maison 8 en Vierge
Tu agis dans les transformations avec discernement. Tu analyses les crises, parfois au lieu de les traverser.

## Micro-rituel du jour (2 min)
- Pense à une transformation que tu essaies de contrôler par l'analyse
- Respire et laisse le mystère être
- Note une façon d'accueillir l'intensité sans la disséquer aujourd'hui""",

    ('virgo', 9): """# ♂️ Mars en Vierge

**En une phrase :** Tu poursuis la vérité avec méthode, vérifiant et analysant chaque croyance.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est critique et pratique. Tu veux des sagesses qui fonctionnent.

## Ton défi
Éviter de rejeter les croyances qui ne semblent pas utiles ou de critiquer les foi des autres.

## Maison 9 en Vierge
Tu agis dans la quête de sens avec discernement. Tes voyages sont bien organisés, ta spiritualité est pratique.

## Micro-rituel du jour (2 min)
- Pense à une croyance que tu rejettes car pas assez pratique
- Respire et trouve ce qu'elle pourrait t'apporter
- Note une façon de vivre ta spiritualité concrètement aujourd'hui""",

    ('virgo', 11): """# ♂️ Mars en Vierge

**En une phrase :** Tu apportes efficacité et service aux groupes, optimisant les projets collectifs.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de perfectionniste utile. Tu améliores, tu organises, tu sers.

## Ton défi
Éviter de critiquer le groupe ou de te sentir frustré quand les autres ne visent pas l'excellence.

## Maison 11 en Vierge
Tu agis dans les groupes et amitiés avec sens du service. Tu aides tes amis concrètement, tu améliores les projets.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu joues le rôle du correcteur
- Respire et trouve ce qui va bien sans chercher à améliorer
- Note une façon d'apprécier tes amis tels qu'ils sont aujourd'hui""",

    ('virgo', 12): """# ♂️ Mars en Vierge

**En une phrase :** Tu travailles sur ton monde intérieur avec méthode, cherchant à purifier et améliorer ton âme.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est analytique et guérissante. Tu médites pour t'améliorer.

## Ton défi
Éviter de critiquer ta vie intérieure ou de vouloir réparer ton âme comme un mécanisme.

## Maison 12 en Vierge
Tu agis dans le monde invisible avec discernement. Tes retraites sont ordonnées, ta spiritualité vise la purification.

## Micro-rituel du jour (2 min)
- Identifie un aspect de ta vie intérieure que tu veux constamment réparer
- Respire et accepte-le tel qu'il est
- Note une façon de méditer sans agenda d'amélioration aujourd'hui""",

    # LIBRA
    ('libra', 2): """# ♂️ Mars en Balance

**En une phrase :** Tu agis pour tes ressources avec diplomatie, cherchant l'équilibre et le partage équitable.

## Ton moteur
Ta façon de passer à l'action pour l'argent est relationnelle et esthétique. Tu négocies, tu équilibres, tu partages.

## Ton défi
Éviter l'indécision financière ou la dépendance aux autres pour les questions matérielles.

## Maison 2 en Balance
Tu agis sur tes ressources avec sens de l'équité et de l'esthétique. Tu veux que l'argent soit beau et partagé.

## Micro-rituel du jour (2 min)
- Pense à une décision financière que tu repousses par indécision
- Respire et choisis, même imparfaitement
- Note une action financière à prendre par toi-même aujourd'hui""",

    ('libra', 3): """# ♂️ Mars en Balance

**En une phrase :** Tu communiques avec diplomatie et charme, cherchant le consensus et l'harmonie.

## Ton moteur
Ta façon de passer à l'action dans la communication est équilibrée et élégante. Tu négocies, tu charmes, tu harmonises.

## Ton défi
Éviter de dire ce que les autres veulent entendre ou de fuir les conflits nécessaires.

## Maison 3 en Balance
Tu agis dans la communication avec diplomatie. Tu négocies, tu équilibres les points de vue, parfois tu évites le conflit.

## Micro-rituel du jour (2 min)
- Pense à une vérité que tu n'oses pas exprimer pour garder la paix
- Respire et trouve une façon élégante de l'énoncer
- Note une conversation vraie à avoir aujourd'hui""",

    ('libra', 5): """# ♂️ Mars en Balance

**En une phrase :** Tu crées et aimes avec grâce, cherchant la beauté et l'harmonie dans tes expressions.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est esthétique et relationnelle. Tu crées la beauté.

## Ton défi
Éviter de dépendre de l'autre pour agir ou de ne rien créer tant que l'harmonie n'est pas parfaite.

## Maison 5 en Balance
Tu agis dans la créativité et les plaisirs avec grâce. Tes romances sont équilibrées, ta créativité vise la beauté.

## Micro-rituel du jour (2 min)
- Pense à un projet créatif ou une relation où tu attends l'autre pour agir
- Respire et trouve ton élan propre
- Note une façon de créer ou aimer par toi-même aujourd'hui""",

    ('libra', 6): """# ♂️ Mars en Balance

**En une phrase :** Tu travailles avec diplomatie et élégance, cherchant l'harmonie dans l'environnement professionnel.

## Ton moteur
Ta façon de passer à l'action au quotidien est collaborative et équilibrée. Tu travailles mieux en partenariat.

## Ton défi
Éviter l'indécision au travail ou la tendance à dépendre des autres pour avancer.

## Maison 6 en Balance
Tu agis dans le travail quotidien avec sens de l'harmonie. Tu veux un environnement beau et des relations fluides.

## Micro-rituel du jour (2 min)
- Identifie une décision de travail que tu délègues par indécision
- Respire et prends-la toi-même
- Note une action professionnelle indépendante à accomplir aujourd'hui""",

    ('libra', 8): """# ♂️ Mars en Balance

**En une phrase :** Tu traverses les transformations en cherchant l'équilibre et le partenariat dans les profondeurs.

## Ton moteur
Ta façon de passer à l'action face aux transformations est relationnelle et équilibrée. Tu transformes à deux.

## Ton défi
Éviter de fuir l'intensité pour maintenir l'harmonie ou de dépendre de l'autre pour traverser les crises.

## Maison 8 en Balance
Tu agis dans les transformations avec sens du partenariat. Tu veux traverser les crises ensemble, équitablement.

## Micro-rituel du jour (2 min)
- Pense à une tension profonde que tu évites pour garder la paix
- Respire et trouve le courage de l'aborder
- Note une façon d'affronter l'intensité avec grâce aujourd'hui""",

    ('libra', 9): """# ♂️ Mars en Balance

**En une phrase :** Tu poursuis la vérité avec équilibre, pesant les différentes perspectives avant de croire.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est diplomatique et comparative. Tu vois la valeur dans différentes visions.

## Ton défi
Éviter l'indécision spirituelle ou le refus de prendre position par souci d'équilibre.

## Maison 9 en Balance
Tu agis dans la quête de sens avec équilibre. Tes voyages cherchent l'harmonie, tes convictions balancent les perspectives.

## Micro-rituel du jour (2 min)
- Pense à une conviction que tu refuses de défendre par souci d'équilibre
- Respire et ose prendre position
- Note une croyance à assumer aujourd'hui""",

    ('libra', 11): """# ♂️ Mars en Balance

**En une phrase :** Tu agis dans les groupes avec diplomatie, créant l'harmonie et facilitant le consensus.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de médiateur élégant. Tu facilites, tu harmonises, tu équilibres.

## Ton défi
Éviter de t'épuiser à maintenir la paix ou de ne pas défendre tes propres idées.

## Maison 11 en Balance
Tu agis dans les groupes et amitiés avec sens de l'harmonie. Tu crées des liens, tu facilites les échanges.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu joues trop le médiateur au détriment de toi
- Respire et définis ta propre position
- Note une façon de contribuer au groupe avec ta vraie voix aujourd'hui""",

    ('libra', 12): """# ♂️ Mars en Balance

**En une phrase :** Tu travailles sur ton monde intérieur en cherchant l'équilibre entre lumière et ombre.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est harmonieuse et équilibrée. Tu médites pour la paix.

## Ton défi
Éviter de fuir les aspects sombres pour maintenir une façade harmonieuse ou de dépendre des autres pour ta paix intérieure.

## Maison 12 en Balance
Tu agis dans le monde invisible avec sens de l'équilibre. Tes retraites sont belles, ta spiritualité cherche l'harmonie.

## Micro-rituel du jour (2 min)
- Identifie une part de toi que tu caches car elle brise l'harmonie
- Respire et intègre-la
- Note une façon de faire la paix avec ton ombre aujourd'hui""",

    # SCORPIO
    ('scorpio', 2): """# ♂️ Mars en Scorpion

**En une phrase :** Tu agis pour tes ressources avec intensité et stratégie, voulant le pouvoir et le contrôle.

## Ton moteur
Ta façon de passer à l'action pour l'argent est profonde et stratégique. Tu veux des ressources qui te donnent du pouvoir.

## Ton défi
Éviter l'obsession du contrôle financier ou les manœuvres souterraines pour les ressources.

## Maison 2 en Scorpion
Tu agis sur tes ressources avec intensité et détermination. Tu veux la sécurité absolue, le contrôle total.

## Micro-rituel du jour (2 min)
- Pense à une obsession financière qui te consume
- Respire et lâche le besoin de contrôle absolu
- Note une façon de te sentir en sécurité sans tout contrôler aujourd'hui""",

    ('scorpio', 3): """# ♂️ Mars en Scorpion

**En une phrase :** Tu communiques avec profondeur et puissance, tes mots vont droit au cœur des choses.

## Ton moteur
Ta façon de passer à l'action dans la communication est pénétrante et stratégique. Tu sais où frapper.

## Ton défi
Éviter la manipulation verbale ou les mots qui blessent pour gagner.

## Maison 3 en Scorpion
Tu agis dans la communication avec intensité. Tu parles pour transformer, parfois pour détruire.

## Micro-rituel du jour (2 min)
- Pense à des mots que tu as utilisés comme armes
- Respire et trouve une façon plus constructive de communiquer
- Note une intention de parler pour guérir plutôt que blesser aujourd'hui""",

    ('scorpio', 5): """# ♂️ Mars en Scorpion

**En une phrase :** Tu crées et aimes avec passion totale, cherchant la fusion et la transformation.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est intense et transformative. Tu crées pour exorciser.

## Ton défi
Éviter les passions destructrices ou la jalousie qui empoisonne les relations.

## Maison 5 en Scorpion
Tu agis dans la créativité et les plaisirs avec intensité. Tes romances sont passionnées, ta créativité est cathartique.

## Micro-rituel du jour (2 min)
- Pense à une passion qui est devenue destructrice
- Respire et transforme cette énergie en création
- Note une façon de créer ou aimer avec intensité mais sans destruction aujourd'hui""",

    ('scorpio', 6): """# ♂️ Mars en Scorpion

**En une phrase :** Tu travailles avec détermination et profondeur, voulant transformer chaque aspect du quotidien.

## Ton moteur
Ta façon de passer à l'action au quotidien est stratégique et intense. Tu veux aller au fond des problèmes.

## Ton défi
Éviter les dynamiques de pouvoir au travail ou l'épuisement par intensité constante.

## Maison 6 en Scorpion
Tu agis dans le travail quotidien avec intensité. Tu veux transformer, améliorer profondément, pas superficiellement.

## Micro-rituel du jour (2 min)
- Identifie une dynamique de pouvoir au travail qui te consume
- Respire et lâche le besoin de contrôler
- Note une façon de travailler avec intensité mais sans conflit aujourd'hui""",

    ('scorpio', 8): """# ♂️ Mars en Scorpion

**En une phrase :** Tu traverses les transformations avec une puissance naturelle, tu es chez toi dans les profondeurs.

## Ton moteur
Ta façon de passer à l'action face aux transformations est ton élément natif. Tu n'as pas peur des ténèbres.

## Ton défi
Éviter de te complaire dans l'intensité ou de provoquer des crises pour te sentir vivant.

## Maison 8 en Scorpion
Position renforcée : tu agis dans les transformations avec une puissance naturelle. Tu es le phénix.

## Micro-rituel du jour (2 min)
- Pense à une crise que tu as provoquée par besoin d'intensité
- Respire et trouve l'intensité dans la paix
- Note une façon de vivre pleinement sans drame aujourd'hui""",

    ('scorpio', 9): """# ♂️ Mars en Scorpion

**En une phrase :** Tu poursuis la vérité avec une intensité radicale, cherchant ce qui transforme vraiment.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est profonde et sans compromis. Tu veux la vérité absolue.

## Ton défi
Éviter le fanatisme ou le rejet de ce qui ne passe pas ton test de profondeur.

## Maison 9 en Scorpion
Tu agis dans la quête de sens avec intensité. Tes voyages sont transformatifs, tes convictions sont radicales.

## Micro-rituel du jour (2 min)
- Pense à une croyance que tu rejettes car trop légère
- Respire et trouve sa sagesse cachée
- Note une façon d'être profond sans être rigide aujourd'hui""",

    ('scorpio', 11): """# ♂️ Mars en Scorpion

**En une phrase :** Tu apportes intensité et transformation aux groupes, cherchant des liens profonds et loyaux.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de transformateur intense. Tu veux des amitiés vraies.

## Ton défi
Éviter les dynamiques de pouvoir dans les groupes ou la jalousie entre amis.

## Maison 11 en Scorpion
Tu agis dans les groupes et amitiés avec intensité. Tes amis sont peu nombreux mais les liens sont profonds.

## Micro-rituel du jour (2 min)
- Pense à une dynamique de pouvoir ou jalousie dans un groupe
- Respire et choisis la confiance
- Note une façon de contribuer au groupe sans contrôler aujourd'hui""",

    ('scorpio', 12): """# ♂️ Mars en Scorpion

**En une phrase :** Tu travailles sur ton monde intérieur avec puissance, plongeant sans peur dans les abysses de l'âme.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est naturelle et courageuse. Tu explores tes ombres sans peur.

## Ton défi
Éviter de te perdre dans les abysses ou de devenir obsédé par ton monde intérieur.

## Maison 12 en Scorpion
Tu agis dans le monde invisible avec puissance. Tes retraites sont transformatives, ta spiritualité est alchimique.

## Micro-rituel du jour (2 min)
- Identifie une obsession intérieure qui te consume
- Respire et laisse-la se transformer sans t'y accrocher
- Note une façon d'explorer tes profondeurs avec légèreté aujourd'hui""",

    # SAGITTARIUS
    ('sagittarius', 2): """# ♂️ Mars en Sagittaire

**En une phrase :** Tu agis pour tes ressources avec optimisme et aventure, croyant en l'abondance.

## Ton moteur
Ta façon de passer à l'action pour l'argent est expansive et confiante. Tu prends des risques, tu vois grand.

## Ton défi
Éviter les risques financiers excessifs ou la négligence des détails pratiques.

## Maison 2 en Sagittaire
Tu agis sur tes ressources avec optimisme. Tu crois en l'abondance, tu donnes et dépenses généreusement.

## Micro-rituel du jour (2 min)
- Pense à un risque financier pris par excès d'optimisme
- Respire et trouve l'équilibre entre vision et prudence
- Note une action financière réfléchie mais audacieuse aujourd'hui""",

    ('sagittarius', 3): """# ♂️ Mars en Sagittaire

**En une phrase :** Tu communiques avec enthousiasme et conviction, tes mots portent des visions inspirantes.

## Ton moteur
Ta façon de passer à l'action dans la communication est passionnée et expansive. Tu veux inspirer, convaincre.

## Ton défi
Éviter l'exagération ou les promesses que tu ne pourras pas tenir.

## Maison 3 en Sagittaire
Tu agis dans la communication avec feu et vision. Tu inspires, mais parfois tu en fais trop.

## Micro-rituel du jour (2 min)
- Pense à une promesse faite dans l'enthousiasme que tu peines à tenir
- Respire et trouve une façon de l'honorer ou de clarifier
- Note une intention de parler avec enthousiasme mais réalisme aujourd'hui""",

    ('sagittarius', 5): """# ♂️ Mars en Sagittaire

**En une phrase :** Tu crées et aimes avec joie et aventure, cherchant l'expansion et la liberté.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est joyeuse et libre. Tu veux des aventures.

## Ton défi
Éviter de fuir l'engagement ou de te lasser quand l'aventure devient routine.

## Maison 5 en Sagittaire
Tu agis dans la créativité et les plaisirs avec joie. Tes romances sont des aventures, ta créativité est expansive.

## Micro-rituel du jour (2 min)
- Pense à une relation ou création abandonnée quand elle devenait routinière
- Respire et trouve l'aventure dans l'engagement
- Note une façon de créer ou aimer avec joie et constance aujourd'hui""",

    ('sagittarius', 6): """# ♂️ Mars en Sagittaire

**En une phrase :** Tu travailles avec enthousiasme quand le sens est là, cherchant à servir une vision plus grande.

## Ton moteur
Ta façon de passer à l'action au quotidien est inspirée par le sens. Tu veux que ton travail compte.

## Ton défi
Éviter de négliger les tâches routinières ou de t'ennuyer quand le travail n'est pas inspirant.

## Maison 6 en Sagittaire
Tu agis dans le travail quotidien avec une vision large. Tu veux que la routine serve une mission.

## Micro-rituel du jour (2 min)
- Identifie une tâche que tu négliges car pas assez inspirante
- Respire et trouve son sens caché
- Note une façon d'apporter de la joie à ton travail quotidien aujourd'hui""",

    ('sagittarius', 8): """# ♂️ Mars en Sagittaire

**En une phrase :** Tu traverses les transformations avec foi, voyant la croissance possible dans chaque crise.

## Ton moteur
Ta façon de passer à l'action face aux transformations est optimiste et philosophique. Tu crois en la renaissance.

## Ton défi
Éviter de minimiser la souffrance par optimisme ou de fuir les profondeurs dans la quête de sens.

## Maison 8 en Sagittaire
Tu agis dans les transformations avec foi. Tu cherches le sens dans les crises, parfois tu les survoles.

## Micro-rituel du jour (2 min)
- Pense à une épreuve dont tu minimises la difficulté
- Respire et accorde-lui sa profondeur
- Note une façon de traverser l'intensité avec foi mais présence aujourd'hui""",

    ('sagittarius', 9): """# ♂️ Mars en Sagittaire

**En une phrase :** Tu poursuis la vérité avec passion native, explorateur infatigable des horizons de la pensée.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est ton élément naturel. Tu es né pour chercher le sens.

## Ton défi
Éviter de survoler trop de philosophies ou de croire avoir trouvé LA vérité à chaque découverte.

## Maison 9 en Sagittaire
Position renforcée : tu agis dans la quête de sens avec une énergie naturelle. Tu es le chercheur de vérité.

## Micro-rituel du jour (2 min)
- Pense à une croyance récemment adoptée avec enthousiasme
- Respire et questionne-la avec la même curiosité
- Note une façon d'approfondir plutôt que d'explorer ailleurs aujourd'hui""",

    ('sagittarius', 11): """# ♂️ Mars en Sagittaire

**En une phrase :** Tu inspires les groupes avec ta vision et ton enthousiasme, voulant que le collectif vise haut.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de visionnaire enthousiaste. Tu motives, tu inspires, tu vises grand.

## Ton défi
Éviter de promettre au groupe plus que possible ou de t'ennuyer quand les détails s'imposent.

## Maison 11 en Sagittaire
Tu agis dans les groupes et amitiés avec vision. Tes amis sont des compagnons d'aventure, tes idéaux sont mondiaux.

## Micro-rituel du jour (2 min)
- Pense à un projet de groupe trop ambitieux qui s'essouffle
- Respire et trouve une prochaine étape réaliste
- Note une façon de servir le groupe avec pragmatisme aujourd'hui""",

    ('sagittarius', 12): """# ♂️ Mars en Sagittaire

**En une phrase :** Tu travailles sur ton monde intérieur avec foi, explorant les vastes espaces de l'âme.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est joyeuse et exploratoire. Tu médites pour t'expanser.

## Ton défi
Éviter de fuir l'introspection dans la quête spirituelle ou de négliger ton ombre.

## Maison 12 en Sagittaire
Tu agis dans le monde invisible avec foi et optimisme. Tes retraites sont des voyages, ta spiritualité est joyeuse.

## Micro-rituel du jour (2 min)
- Identifie une part sombre de toi que tu évites par la quête de lumière
- Respire et accueille-la
- Note une façon d'intégrer ton ombre dans ta spiritualité aujourd'hui""",

    # CAPRICORN
    ('capricorn', 2): """# ♂️ Mars en Capricorne

**En une phrase :** Tu agis pour tes ressources avec discipline et ambition, construisant patiemment ta sécurité.

## Ton moteur
Ta façon de passer à l'action pour l'argent est stratégique et déterminée. Tu construis sur le long terme.

## Ton défi
Éviter le workaholisme pour l'argent ou la rigidité qui manque les opportunités.

## Maison 2 en Capricorne
Tu agis sur tes ressources avec rigueur et ambition. Tu construis ta sécurité pierre par pierre.

## Micro-rituel du jour (2 min)
- Pense à une opportunité que tu as manquée par excès de prudence
- Respire et trouve l'équilibre entre sécurité et ouverture
- Note une action financière stratégique à poser aujourd'hui""",

    ('capricorn', 3): """# ♂️ Mars en Capricorne

**En une phrase :** Tu communiques avec autorité et structure, tes mots portent le poids de l'expérience.

## Ton moteur
Ta façon de passer à l'action dans la communication est mesurée et efficace. Tu parles peu mais avec impact.

## Ton défi
Éviter la froideur ou la rigidité qui coupe la connexion émotionnelle.

## Maison 3 en Capricorne
Tu agis dans la communication avec autorité. Tu parles avec poids, parfois avec trop de sérieux.

## Micro-rituel du jour (2 min)
- Pense à une communication perçue comme froide
- Respire et trouve une façon d'ajouter de la chaleur
- Note une intention de communiquer avec fermeté et chaleur aujourd'hui""",

    ('capricorn', 5): """# ♂️ Mars en Capricorne

**En une phrase :** Tu crées et aimes avec ambition et discipline, cherchant l'excellence et la durée.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est sérieuse et ambitieuse. Tu veux que ça dure.

## Ton défi
Éviter de transformer l'amour ou la créativité en devoir ou de bloquer la spontanéité par excès de sérieux.

## Maison 5 en Capricorne
Tu agis dans la créativité et les plaisirs avec discipline. Tes romances sont construites, ta créativité est ambitieuse.

## Micro-rituel du jour (2 min)
- Pense à un moment où tu as rendu l'amour ou la création trop sérieux
- Respire et trouve la légèreté
- Note une façon de jouer sans objectif aujourd'hui""",

    ('capricorn', 6): """# ♂️ Mars en Capricorne

**En une phrase :** Tu travailles avec excellence et discipline, visant la maîtrise et la reconnaissance.

## Ton moteur
Ta façon de passer à l'action au quotidien est structurée et ambitieuse. Tu veux être le meilleur.

## Ton défi
Éviter le workaholisme ou la difficulté à déléguer par manque de confiance.

## Maison 6 en Capricorne
Tu agis dans le travail quotidien avec excellence. Tu es professionnel, efficace, parfois trop exigeant.

## Micro-rituel du jour (2 min)
- Identifie une tâche que tu refuses de déléguer
- Respire et fais confiance
- Note une façon de te reposer malgré les responsabilités aujourd'hui""",

    ('capricorn', 8): """# ♂️ Mars en Capricorne

**En une phrase :** Tu traverses les transformations avec stratégie et endurance, construisant à travers les crises.

## Ton moteur
Ta façon de passer à l'action face aux transformations est pragmatique et résiliente. Tu sais traverser les tempêtes.

## Ton défi
Éviter de contrôler les transformations ou de réprimer les émotions au profit de la stratégie.

## Maison 8 en Capricorne
Tu agis dans les transformations avec discipline. Tu gères les crises avec maîtrise, parfois avec trop de contrôle.

## Micro-rituel du jour (2 min)
- Pense à une transformation que tu essaies de contrôler entièrement
- Respire et accepte la part d'inconnu
- Note une façon de lâcher prise dans une situation intense aujourd'hui""",

    ('capricorn', 9): """# ♂️ Mars en Capricorne

**En une phrase :** Tu poursuis la vérité avec méthode et respect de la tradition, cherchant des sagesses éprouvées.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est disciplinée et respectueuse. Tu préfères les sagesses qui ont fait leurs preuves.

## Ton défi
Éviter le cynisme face aux nouvelles idées ou l'attachement rigide aux traditions dépassées.

## Maison 9 en Capricorne
Tu agis dans la quête de sens avec rigueur. Tes voyages sont organisés, ta spiritualité est structurée.

## Micro-rituel du jour (2 min)
- Pense à une idée nouvelle que tu rejettes par conservatisme
- Respire et donne-lui une chance
- Note une façon d'être sage sans être rigide aujourd'hui""",

    ('capricorn', 11): """# ♂️ Mars en Capricorne

**En une phrase :** Tu apportes structure et ambition aux groupes, concrétisant les projets collectifs.

## Ton moteur
Ta façon de passer à l'action dans le collectif est d'organisateur ambitieux. Tu construis, tu structures, tu réalises.

## Ton défi
Éviter de devenir trop directif ou de décourager les rêves des autres par réalisme excessif.

## Maison 11 en Capricorne
Tu agis dans les groupes et amitiés avec professionnalisme. Tu es le pilier qui construit vraiment.

## Micro-rituel du jour (2 min)
- Pense à une idée de groupe que tu as jugée irréaliste
- Respire et trouve un aspect réalisable
- Note une façon d'encourager plutôt que de tempérer aujourd'hui""",

    ('capricorn', 12): """# ♂️ Mars en Capricorne

**En une phrase :** Tu travailles sur ton monde intérieur avec discipline, construisant ton âme comme un édifice.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est structurée et persévérante. Tu médites avec discipline.

## Ton défi
Éviter de fuir l'introspection dans le travail ou de traiter ta vie spirituelle comme une carrière.

## Maison 12 en Capricorne
Tu agis dans le monde invisible avec rigueur. Tes retraites sont disciplinées, ta spiritualité est sérieuse.

## Micro-rituel du jour (2 min)
- Identifie un aspect de ta vie spirituelle devenu une obligation
- Respire et retrouve la grâce
- Note une façon de méditer par amour plutôt que par devoir aujourd'hui""",

    # AQUARIUS
    ('aquarius', 2): """# ♂️ Mars en Verseau

**En une phrase :** Tu agis pour tes ressources de façon originale, cherchant des méthodes innovantes et indépendantes.

## Ton moteur
Ta façon de passer à l'action pour l'argent est non-conventionnelle et visionnaire. Tu inventes tes propres règles.

## Ton défi
Éviter l'instabilité financière par rejet des méthodes éprouvées ou le détachement excessif du matériel.

## Maison 2 en Verseau
Tu agis sur tes ressources avec originalité. Tu explores de nouvelles façons de gagner et de valoriser.

## Micro-rituel du jour (2 min)
- Pense à une méthode financière traditionnelle que tu rejettes par principe
- Respire et trouve ce qu'elle pourrait t'apporter
- Note une action financière innovante mais ancrée aujourd'hui""",

    ('aquarius', 3): """# ♂️ Mars en Verseau

**En une phrase :** Tu communiques avec originalité et vision, tes idées sont en avance sur leur temps.

## Ton moteur
Ta façon de passer à l'action dans la communication est inventive et progressiste. Tu penses différemment.

## Ton défi
Éviter de paraître trop détaché ou de rejeter les idées ordinaires par principe.

## Maison 3 en Verseau
Tu agis dans la communication avec originalité. Tu inspires par ta vision unique, parfois tu déroutes.

## Micro-rituel du jour (2 min)
- Pense à une idée ordinaire que tu as rejetée par anticonformisme
- Respire et trouve sa valeur
- Note une façon de connecter innovation et tradition aujourd'hui""",

    ('aquarius', 5): """# ♂️ Mars en Verseau

**En une phrase :** Tu crées et aimes avec liberté et originalité, défiant les conventions.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est expérimentale et libre. Tu inventes tes propres formes.

## Ton défi
Éviter le détachement émotionnel ou la peur de l'engagement déguisée en besoin de liberté.

## Maison 5 en Verseau
Tu agis dans la créativité et les plaisirs avec originalité. Tes romances sont libres, ta créativité est d'avant-garde.

## Micro-rituel du jour (2 min)
- Pense à une relation où tu as fui l'engagement par besoin de liberté
- Respire et trouve la liberté dans la connexion
- Note une façon de créer ou aimer avec profondeur et liberté aujourd'hui""",

    ('aquarius', 6): """# ♂️ Mars en Verseau

**En une phrase :** Tu travailles avec innovation et vision collective, voulant révolutionner les méthodes.

## Ton moteur
Ta façon de passer à l'action au quotidien est orientée systèmes et amélioration. Tu vois comment révolutionner.

## Ton défi
Éviter de rejeter les méthodes établies par principe ou de te déconnecter de tes collègues.

## Maison 6 en Verseau
Tu agis dans le travail quotidien avec innovation. Tu veux améliorer les systèmes, parfois tu rejettes trop vite.

## Micro-rituel du jour (2 min)
- Identifie une méthode de travail que tu rejettes par anticonformisme
- Respire et trouve ce qu'elle a de bon
- Note une amélioration réaliste à proposer aujourd'hui""",

    ('aquarius', 8): """# ♂️ Mars en Verseau

**En une phrase :** Tu traverses les transformations avec détachement et vision, cherchant l'évolution collective.

## Ton moteur
Ta façon de passer à l'action face aux transformations est analytique et visionnaire. Tu vois le tableau d'ensemble.

## Ton défi
Éviter le détachement émotionnel face à l'intensité ou l'intellectualisation des profondeurs.

## Maison 8 en Verseau
Tu agis dans les transformations avec originalité. Tu vois les crises comme des opportunités d'évolution.

## Micro-rituel du jour (2 min)
- Pense à une émotion intense que tu as rationalisée
- Respire et laisse-toi la ressentir
- Note une façon de vivre l'intensité sans la disséquer aujourd'hui""",

    ('aquarius', 9): """# ♂️ Mars en Verseau

**En une phrase :** Tu poursuis la vérité avec une vision progressiste, cherchant les sagesses qui font évoluer l'humanité.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est visionnaire et humaniste. Tu crois en l'évolution.

## Ton défi
Éviter de rejeter les traditions ou de confondre nouveauté et progrès véritable.

## Maison 9 en Verseau
Tu agis dans la quête de sens avec une vision futuriste. Ta spiritualité est progressiste et universelle.

## Micro-rituel du jour (2 min)
- Pense à une tradition spirituelle que tu rejettes car dépassée
- Respire et trouve sa sagesse intemporelle
- Note une façon d'honorer le passé dans ta vision du futur aujourd'hui""",

    ('aquarius', 11): """# ♂️ Mars en Verseau

**En une phrase :** Tu agis dans les groupes avec vision et originalité, connectant les idées et les personnes pour le progrès.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de visionnaire connecteur. Tu rassembles pour l'innovation.

## Ton défi
Éviter de te perdre dans les grandes idées au détriment des relations humaines ou de paraître trop distant.

## Maison 11 en Verseau
Position renforcée : tu agis dans les groupes avec une énergie naturelle de révolutionnaire et de connecteur.

## Micro-rituel du jour (2 min)
- Pense à un ami avec qui tu partages des idées mais peu d'émotions
- Respire et trouve une façon de te connecter humainement
- Note une action pour approfondir une amitié au-delà des idées aujourd'hui""",

    ('aquarius', 12): """# ♂️ Mars en Verseau

**En une phrase :** Tu travailles sur ton monde intérieur avec originalité, explorant les dimensions collectives de l'inconscient.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est expérimentale et connectée au collectif. Tu explores les états de conscience.

## Ton défi
Éviter de fuir dans les concepts spirituels ou de négliger ta vie intérieure personnelle.

## Maison 12 en Verseau
Tu agis dans le monde invisible avec une vision cosmique. Tes retraites sont originales, ta spiritualité est universelle.

## Micro-rituel du jour (2 min)
- Identifie une fuite dans les grandes idées qui évite ton intimité propre
- Respire et reviens à toi
- Note une façon de te connecter à ton inconscient personnel aujourd'hui""",

    # PISCES
    ('pisces', 2): """# ♂️ Mars en Poissons

**En une phrase :** Tu agis pour tes ressources avec fluidité et foi, faisant confiance à l'univers pour tes besoins.

## Ton moteur
Ta façon de passer à l'action pour l'argent est intuitive et généreuse. Tu donnes, tu fais confiance, tu lâches prise.

## Ton défi
Éviter la naïveté financière ou le manque de limites qui te rend vulnérable.

## Maison 2 en Poissons
Tu agis sur tes ressources avec fluidité. Tu crois en l'abondance universelle, parfois au détriment de ta sécurité.

## Micro-rituel du jour (2 min)
- Pense à une situation où tu as donné au détriment de tes besoins
- Respire et pose des limites avec amour
- Note une action pour ta sécurité financière aujourd'hui""",

    ('pisces', 3): """# ♂️ Mars en Poissons

**En une phrase :** Tu communiques avec poésie et intuition, tes mots touchent l'âme plus que la raison.

## Ton moteur
Ta façon de passer à l'action dans la communication est intuitive et symbolique. Tu parles par images.

## Ton défi
Éviter le flou dans ta communication ou la difficulté à être direct quand c'est nécessaire.

## Maison 3 en Poissons
Tu agis dans la communication avec sensibilité. Tu touches les cœurs, parfois tu manques de clarté.

## Micro-rituel du jour (2 min)
- Pense à une communication qui a été mal comprise car trop floue
- Respire et trouve des mots plus concrets
- Note une intention de communiquer avec poésie et clarté aujourd'hui""",

    ('pisces', 5): """# ♂️ Mars en Poissons

**En une phrase :** Tu crées et aimes avec dévotion et inspiration, canalisant des forces qui te dépassent.

## Ton moteur
Ta façon de passer à l'action dans la créativité et l'amour est inspirée et transcendante. Tu es un canal.

## Ton défi
Éviter de te perdre dans les rêves ou les amours impossibles qui te déconnectent de la réalité.

## Maison 5 en Poissons
Tu agis dans la créativité et les plaisirs avec inspiration. Tes romances sont idéalisées, ta créativité est transcendante.

## Micro-rituel du jour (2 min)
- Pense à une création ou un amour que tu as idéalisé au point de le rendre impossible
- Respire et trouve la beauté dans le possible
- Note une façon de créer ou aimer dans le réel aujourd'hui""",

    ('pisces', 6): """# ♂️ Mars en Poissons

**En une phrase :** Tu travailles avec compassion et dévouement, servant les autres avec une énergie de guérison.

## Ton moteur
Ta façon de passer à l'action au quotidien est intuitive et serviable. Tu sens ce dont les autres ont besoin.

## Ton défi
Éviter de te sacrifier au travail ou de ne pas poser de limites avec ceux que tu aides.

## Maison 6 en Poissons
Tu agis dans le travail quotidien avec compassion. Tu sers, tu guéris, parfois tu t'épuises pour les autres.

## Micro-rituel du jour (2 min)
- Identifie un moment où tu te sacrifies au travail
- Respire et pose une limite avec amour
- Note une façon de servir tout en te protégeant aujourd'hui""",

    ('pisces', 8): """# ♂️ Mars en Poissons

**En une phrase :** Tu traverses les transformations avec foi et abandon, te laissant porter par les courants profonds.

## Ton moteur
Ta façon de passer à l'action face aux transformations est intuitive et acceptante. Tu te laisses transformer.

## Ton défi
Éviter de te noyer dans les émotions ou de fuir l'intensité dans les rêves.

## Maison 8 en Poissons
Tu agis dans les transformations avec fluidité. Tu sens les courants souterrains, parfois tu t'y perds.

## Micro-rituel du jour (2 min)
- Pense à une situation intense où tu t'es senti submergé
- Respire et trouve ton ancrage
- Note une façon de traverser les profondeurs avec les pieds sur terre aujourd'hui""",

    ('pisces', 9): """# ♂️ Mars en Poissons

**En une phrase :** Tu poursuis la vérité avec mysticisme, cherchant l'unité au-delà de toutes les divisions.

## Ton moteur
Ta façon de passer à l'action pour tes croyances est intuitive et unifiante. Tu sens l'unité de tout.

## Ton défi
Éviter la confusion spirituelle ou la difficulté à discerner entre vraie sagesse et illusion.

## Maison 9 en Poissons
Tu agis dans la quête de sens avec intuition. Ta spiritualité est mystique et universelle.

## Micro-rituel du jour (2 min)
- Pense à une croyance que tu n'as jamais vraiment questionnée
- Respire et passe-la au filtre du discernement
- Note une façon d'allier foi et clarté aujourd'hui""",

    ('pisces', 11): """# ♂️ Mars en Poissons

**En une phrase :** Tu apportes compassion et vision aux groupes, servant les idéaux avec dévouement.

## Ton moteur
Ta façon de passer à l'action dans le collectif est de serviteur inspiré. Tu donnes, tu guéris, tu unifie.

## Ton défi
Éviter de te perdre dans les idéaux collectifs ou d'absorber les problèmes du groupe.

## Maison 11 en Poissons
Tu agis dans les groupes et amitiés avec compassion. Tes amis sont comme une famille spirituelle.

## Micro-rituel du jour (2 min)
- Pense à un groupe dont tu portes trop les problèmes
- Respire et définis ce qui est ta responsabilité
- Note une façon de contribuer au groupe sans t'y dissoudre aujourd'hui""",

    ('pisces', 12): """# ♂️ Mars en Poissons

**En une phrase :** Tu travailles sur ton monde intérieur avec une fluidité naturelle, navigant entre les dimensions.

## Ton moteur
Ta façon de passer à l'action dans le monde intérieur est ton élément natif. Tu médites pour te dissoudre et renaître.

## Ton défi
Éviter de fuir la réalité dans les rêves ou de te perdre dans l'invisible au point d'oublier le quotidien.

## Maison 12 en Poissons
Position renforcée : tu agis dans le monde invisible avec une aisance naturelle. Tu es chez toi dans les profondeurs.

## Micro-rituel du jour (2 min)
- Identifie une fuite dans le rêve qui évite une responsabilité terrestre
- Respire et reviens dans ton corps
- Note une façon de vivre le sacré dans le quotidien aujourd'hui""",
}


async def main():
    async with AsyncSessionLocal() as db:
        count = 0
        for (sign, house), content in MARS_INTERPRETATIONS.items():
            result = await db.execute(
                update(PregeneratedNatalInterpretation)
                .where(
                    PregeneratedNatalInterpretation.subject == 'mars',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house
                )
                .values(content=content)
            )
            if result.rowcount > 0:
                count += result.rowcount

        await db.commit()
        print(f"Done: {count} mars interpretations updated")


if __name__ == "__main__":
    asyncio.run(main())
