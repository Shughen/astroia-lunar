"""
Générateur d'interprétations textuelles pour révolutions lunaires
Templates dynamiques basés sur l'ascendant, la maison et les aspects
"""

from typing import Dict, Any, List


# === TRADUCTIONS ===
PLANET_NAMES_FR = {
    "Sun": "le Soleil",
    "Moon": "la Lune",
    "Mercury": "Mercure",
    "Venus": "Vénus",
    "Mars": "Mars",
    "Jupiter": "Jupiter",
    "Saturn": "Saturne",
    "Uranus": "Uranus",
    "Neptune": "Neptune",
    "Pluto": "Pluton"
}

ASPECT_NAMES_FR = {
    "conjunction": "conjonction",
    "opposition": "opposition",
    "trine": "trigone",
    "square": "carré",
    "sextile": "sextile"
}


# === INTERPRÉTATIONS PAR ASCENDANT LUNAIRE ===
ASCENDANT_INTERPRETATIONS = {
    "Aries": "Mois d'action et d'initiatives. Votre énergie est tournée vers le commencement, l'affirmation, la prise de décisions rapides. Période propice aux nouveaux départs.",
    "Taurus": "Mois de stabilisation et d'ancrage. Vous recherchez le confort, la sécurité matérielle, les plaisirs sensoriels. Consolidez vos acquis, savourez le présent.",
    "Gemini": "Mois de communication et de curiosité. Votre mental est stimulé, les échanges se multiplient. Période favorable aux apprentissages, aux connexions, à la flexibilité.",
    "Cancer": "Mois d'introspection émotionnelle. Votre sensibilité est accrue, le besoin de cocooning se fait sentir. Prenez soin de vous et de vos proches, écoutez vos besoins affectifs.",
    "Leo": "Mois de rayonnement et de créativité. Vous vous sentez en confiance, prêt à vous mettre en avant. Exprimez votre personnalité, osez briller, créez sans limites.",
    "Virgo": "Mois d'organisation et de perfectionnement. Vous cherchez à optimiser votre quotidien, à améliorer vos routines. Focus sur l'efficacité, la santé, les détails pratiques.",
    "Libra": "Mois d'harmonie relationnelle. Vous recherchez l'équilibre dans vos interactions, la beauté, la diplomatie. Privilégiez les collaborations, les compromis, l'esthétique.",
    "Scorpio": "Mois de transformation intérieure. Vous plongez en profondeur, questionnez l'essentiel, lâchez ce qui ne sert plus. Période d'introspection intense, de régénération.",
    "Sagittarius": "Mois d'exploration et d'expansion. Votre soif d'apprendre, de découvrir, de comprendre est à son pic. Élargissez vos horizons mentaux ou physiques, philosophez.",
    "Capricorn": "Mois de structuration et d'ambition. Vous construisez sur du solide, fixez des objectifs long terme. Discipline, patience et stratégie sont vos alliées.",
    "Aquarius": "Mois d'innovation et d'indépendance. Vous pensez différemment, vous connectez à votre communauté, vous explorez des voies alternatives. Liberté et originalité dominent.",
    "Pisces": "Mois d'intuition et de créativité. Votre sensibilité spirituelle est exacerbée, votre imaginaire foisonnant. Laissez-vous guider par vos ressentis, votre inspiration artistique.",

    # Traductions françaises (fallback)
    "Bélier": "Mois d'action et d'initiatives. Votre énergie est tournée vers le commencement, l'affirmation, la prise de décisions rapides. Période propice aux nouveaux départs.",
    "Taureau": "Mois de stabilisation et d'ancrage. Vous recherchez le confort, la sécurité matérielle, les plaisirs sensoriels. Consolidez vos acquis, savourez le présent.",
    "Gémeaux": "Mois de communication et de curiosité. Votre mental est stimulé, les échanges se multiplient. Période favorable aux apprentissages, aux connexions, à la flexibilité.",
    "Cancer": "Mois d'introspection émotionnelle. Votre sensibilité est accrue, le besoin de cocooning se fait sentir. Prenez soin de vous et de vos proches, écoutez vos besoins affectifs.",
    "Lion": "Mois de rayonnement et de créativité. Vous vous sentez en confiance, prêt à vous mettre en avant. Exprimez votre personnalité, osez briller, créez sans limites.",
    "Vierge": "Mois d'organisation et de perfectionnement. Vous cherchez à optimiser votre quotidien, à améliorer vos routines. Focus sur l'efficacité, la santé, les détails pratiques.",
    "Balance": "Mois d'harmonie relationnelle. Vous recherchez l'équilibre dans vos interactions, la beauté, la diplomatie. Privilégiez les collaborations, les compromis, l'esthétique.",
    "Scorpion": "Mois de transformation intérieure. Vous plongez en profondeur, questionnez l'essentiel, lâchez ce qui ne sert plus. Période d'introspection intense, de régénération.",
    "Sagittaire": "Mois d'exploration et d'expansion. Votre soif d'apprendre, de découvrir, de comprendre est à son pic. Élargissez vos horizons mentaux ou physiques, philosophez.",
    "Capricorne": "Mois de structuration et d'ambition. Vous construisez sur du solide, fixez des objectifs long terme. Discipline, patience et stratégie sont vos alliées.",
    "Verseau": "Mois d'innovation et d'indépendance. Vous pensez différemment, vous connectez à votre communauté, vous explorez des voies alternatives. Liberté et originalité dominent.",
    "Poissons": "Mois d'intuition et de créativité. Votre sensibilité spirituelle est exacerbée, votre imaginaire foisonnant. Laissez-vous guider par vos ressentis, votre inspiration artistique."
}


# === INTERPRÉTATIONS PAR MAISON (FOCUS LUNAIRE) ===
HOUSE_INTERPRETATIONS = {
    1: "Votre identité personnelle est au centre. Mois de renouveau où vous vous réaffirmez, redéfinissez qui vous êtes. Votre présence, votre apparence, votre initiative sont décuplées.",
    2: "Vos ressources matérielles et vos valeurs sont en lumière. Focus sur vos revenus, vos talents, votre estime personnelle. Période propice pour clarifier ce qui a de la valeur pour vous.",
    3: "Communication, apprentissages et déplacements courts dominent. Votre mental est actif, les échanges avec votre entourage proche se multiplient. Période de curiosité intellectuelle.",
    4: "Foyer, famille et racines émotionnelles appellent votre attention. Besoin de vous ressourcer chez vous, de revisiter votre passé, de renforcer vos bases affectives.",
    5: "Créativité, plaisir et expression personnelle sont à l'honneur. Votre joie de vivre, votre spontanéité, votre désir de créer ou de romancer s'expriment librement.",
    6: "Santé, travail quotidien et routines sont au cœur du mois. Vous optimisez votre quotidien, améliorez vos habitudes, vous occupez de votre bien-être physique et mental.",
    7: "Relations et partenariats sont mis en avant. Vos interactions one-to-one, vos associations, votre capacité à collaborer sont testées et affinées.",
    8: "Transformation, intimité et ressources partagées occupent votre psyché. Mois de plongée profonde dans vos émotions, vos peurs, vos attachements. Régénération nécessaire.",
    9: "Expansion mentale, voyages et quête de sens. Vous explorez de nouvelles philosophies, cultures, enseignements. Votre vision s'élargit, votre optimisme grandit.",
    10: "Carrière, ambitions publiques et reconnaissance sociale. Mois où votre image professionnelle est visible, où vos efforts peuvent porter leurs fruits en termes de statut.",
    11: "Amitiés, projets collectifs et idéaux. Votre réseau social, vos aspirations pour l'avenir, votre engagement dans des causes communes sont activés.",
    12: "Spiritualité, inconscient et besoin de retrait. Mois introspectif où vous vous reconnectez à votre dimension intérieure, méditez, lâchez prise, vous reposez."
}


# === INTERPRÉTATIONS D'ASPECTS (LUNE + PLANÈTE) ===
# Format: (aspect_type, planet) -> interprétation factuelle

ASPECT_INTERPRETATIONS_DETAILED = {
    # CONJONCTIONS
    ("conjunction", "Sun"): "La Lune fusionne avec le Soleil dans votre thème de révolution. Vos émotions et votre identité s'alignent : ce que vous ressentez correspond à qui vous êtes. Mois de cohérence intérieure, d'authenticité émotionnelle.",
    ("conjunction", "Mercury"): "La Lune fusionne avec Mercure. Vos émotions et votre mental communiquent directement : ce que vous ressentez, vous le verbalisez facilement. Période propice aux échanges émotionnels, aux discussions sincères.",
    ("conjunction", "Venus"): "La Lune fusionne avec Vénus. Vos besoins affectifs et votre désir d'harmonie s'unissent : vous recherchez le plaisir, la beauté, les connexions douces. Mois d'affection, de créativité esthétique.",
    ("conjunction", "Mars"): "La Lune fusionne avec Mars. Vos émotions et votre énergie d'action se confondent : vous réagissez impulsivement, défendez vos besoins avec force. Période d'assertivité émotionnelle, parfois de frustration à canaliser.",
    ("conjunction", "Jupiter"): "La Lune fusionne avec Jupiter. Vos émotions s'expansent, votre optimisme grandit. Vous vous sentez généreux, confiant, prêt à voir grand. Mois d'abondance émotionnelle, de foi en l'avenir.",
    ("conjunction", "Saturn"): "La Lune fusionne avec Saturne. Vos émotions rencontrent la structure, la discipline. Vous ressentez le poids des responsabilités, le besoin de maturité affective. Mois sérieux, parfois mélancolique, mais constructif.",

    # OPPOSITIONS
    ("opposition", "Sun"): "La Lune s'oppose au Soleil. Tension entre vos besoins émotionnels et votre identité consciente. Ce que vous ressentez s'oppose à ce que vous voulez montrer. Mois de polarité intérieure nécessitant un équilibrage.",
    ("opposition", "Mercury"): "La Lune s'oppose à Mercure. Tension entre ce que vous ressentez et ce que vous pensez. Vos émotions et votre logique se contredisent. Période de tiraillements intellectuels-émotionnels à réconcilier.",
    ("opposition", "Venus"): "La Lune s'oppose à Vénus. Conflit entre vos besoins affectifs personnels et vos désirs relationnels. Ce que vous voulez pour vous vs ce que veut l'autre. Mois de compromis amoureux ou esthétiques.",
    ("opposition", "Mars"): "La Lune s'oppose à Mars. Tension entre vos émotions et votre besoin d'action. Frustrations possibles, réactions impulsives face à des résistances. Canalisez l'énergie, trouvez l'équilibre entre ressentir et agir.",
    ("opposition", "Jupiter"): "La Lune s'oppose à Jupiter. Excès émotionnels possibles : vous ressentez tout en grand, oscillez entre euphorie et débordement. Modérez vos attentes, évitez la dispersion affective.",
    ("opposition", "Saturn"): "La Lune s'oppose à Saturne. Vos besoins émotionnels se heurtent à des limites, des obligations. Sentiment de restriction, de froideur extérieure. Mois exigeant, patience requise.",

    # TRIGONES
    ("trine", "Sun"): "La Lune harmonise avec le Soleil. Fluidité entre vos émotions et votre identité : vous vous sentez aligné, en paix avec vous-même. Mois d'aisance personnelle, de bien-être intérieur naturel.",
    ("trine", "Mercury"): "La Lune harmonise avec Mercure. Vos émotions et votre mental coulent ensemble sans effort. Vous communiquez ce que vous ressentez avec clarté. Période d'échanges fluides, de compréhension mutuelle.",
    ("trine", "Venus"): "La Lune harmonise avec Vénus. Douceur affective, plaisirs faciles, relations harmonieuses. Vos besoins émotionnels trouvent satisfaction sans lutte. Mois agréable, créatif, socialement épanoui.",
    ("trine", "Mars"): "La Lune harmonise avec Mars. Vos émotions et votre énergie d'action s'accordent : vous savez ce que vous voulez et agissez en conséquence. Mois d'assertivité saine, de réalisations concrètes.",
    ("trine", "Jupiter"): "La Lune harmonise avec Jupiter. Optimisme, générosité, expansion émotionnelle sans excès. Vous vous sentez bien, confiant, ouvert aux opportunités. Mois chanceux, socialement riche.",
    ("trine", "Saturn"): "La Lune harmonise avec Saturne. Maturité émotionnelle, stabilité affective. Vous gérez vos émotions avec sagesse, construisez sur du solide. Mois de responsabilité assumée sereinement.",

    # CARRÉS
    ("square", "Sun"): "La Lune défie le Soleil. Friction entre vos besoins émotionnels et votre identité : ce que vous ressentez bouscule qui vous voulez être. Mois de croissance par l'inconfort, de remise en question nécessaire.",
    ("square", "Mercury"): "La Lune défie Mercure. Vos émotions bloquent votre mental ou inversement. Difficultés à penser clairement quand les sentiments débordent. Mois de tensions intellectuelles-émotionnelles à résoudre.",
    ("square", "Venus"): "La Lune défie Vénus. Frictions dans vos relations ou vos plaisirs. Ce que vous voulez affectivement se heurte à des obstacles. Ajustements nécessaires dans l'amour, les finances ou le confort.",
    ("square", "Mars"): "La Lune défie Mars. Frustrations, impatience, réactivité excessive. Vos émotions et votre besoin d'action s'entrechoquent. Mois de tensions à canaliser, d'énergie à rediriger constructivement.",
    ("square", "Jupiter"): "La Lune défie Jupiter. Excès possibles : émotions débordantes, promesses trop grandes, attentes irréalistes. Modérez votre optimisme, ne dispersez pas votre énergie affective.",
    ("square", "Saturn"): "La Lune défie Saturne. Poids émotionnel, sentiment de restriction, devoirs qui pèsent. Vos besoins affectifs rencontrent des limites dures. Mois exigeant, patience et persévérance requises."
}


def generate_lunar_return_interpretation(
    lunar_ascendant: str,
    moon_house: int,
    aspects: List[Dict[str, Any]]
) -> str:
    """
    Génère une interprétation textuelle complète et factuelle

    Args:
        lunar_ascendant: Ascendant de la révolution lunaire
        moon_house: Maison où se trouve la Lune
        aspects: Liste d'aspects [ { "type": "trine", "planet": "Venus", ... }, ... ]

    Returns:
        Texte d'interprétation (3-5 paragraphes)
    """

    interpretation_parts = []

    # 1. Tonalité du mois (ascendant)
    asc_text = ASCENDANT_INTERPRETATIONS.get(
        lunar_ascendant,
        "Nouveau cycle lunaire s'ouvre. Observez les thèmes récurrents de ce mois, ils révèlent vos priorités émotionnelles actuelles."
    )
    interpretation_parts.append(f"**Tonalité du mois :** {asc_text}")

    # 2. Focus principal (maison lunaire)
    house_text = HOUSE_INTERPRETATIONS.get(
        moon_house,
        "Votre Lune éclaire un secteur spécifique de votre vie ce mois-ci. Observez où votre attention émotionnelle se porte naturellement."
    )
    interpretation_parts.append(f"**Focus lunaire :** {house_text}")

    # 3. Aspect majeur le plus significatif (si présent)
    if aspects:
        # Filtrer les aspects majeurs valides
        major_aspects = []
        for a in aspects:
            aspect_type = a.get("type") or a.get("aspect_type")
            planet = a.get("planet") or a.get("to_planet") or a.get("planet1") or a.get("planet2")

            # Ne garder que les aspects majeurs avec planètes connues
            if aspect_type in ASPECT_NAMES_FR and planet in PLANET_NAMES_FR:
                major_aspects.append((aspect_type, planet))

        if major_aspects:
            aspect_type, planet = major_aspects[0]  # Prendre le premier aspect majeur

            # Chercher interprétation détaillée
            aspect_key = (aspect_type, planet)
            if aspect_key in ASPECT_INTERPRETATIONS_DETAILED:
                aspect_text = ASPECT_INTERPRETATIONS_DETAILED[aspect_key]
            else:
                # Fallback générique traduit
                planet_fr = PLANET_NAMES_FR.get(planet, planet)
                aspect_fr = ASPECT_NAMES_FR.get(aspect_type, aspect_type)
                aspect_text = f"La Lune forme un {aspect_fr} avec {planet_fr} ce mois-ci, colorant votre vécu émotionnel de cette énergie planétaire."

            interpretation_parts.append(f"**Dynamique clé :** {aspect_text}")

    # 4. Conseil pratique personnalisé
    practical_advice = _get_practical_advice(lunar_ascendant, moon_house)
    interpretation_parts.append(f"**Action concrète :** {practical_advice}")

    return "\n\n".join(interpretation_parts)


def _get_practical_advice(ascendant: str, house: int) -> str:
    """Génère un conseil pratique factuel basé sur l'ascendant et la maison"""

    # Normaliser l'ascendant (anglais ou français)
    ascendant_normalized = ascendant
    ascendant_map = {
        "Aries": "Bélier", "Taurus": "Taureau", "Gemini": "Gémeaux",
        "Cancer": "Cancer", "Leo": "Lion", "Virgo": "Vierge",
        "Libra": "Balance", "Scorpio": "Scorpion", "Sagittarius": "Sagittaire",
        "Capricorn": "Capricorne", "Aquarius": "Verseau", "Pisces": "Poissons"
    }
    if ascendant in ascendant_map:
        ascendant_normalized = ascendant_map[ascendant]

    advice_map = {
        ("Bélier", 1): "Lancez un projet personnel qui vous tient à cœur. Affirmez-vous sans attendre l'approbation extérieure.",
        ("Bélier", 5): "Créez quelque chose de vos mains. Exprimez votre spontanéité sans filtre.",
        ("Taureau", 2): "Faites un bilan de vos finances et de vos talents. Valorisez ce que vous possédez déjà.",
        ("Taureau", 6): "Instaurez une routine bien-être qui ancre votre corps : yoga, cuisine, jardinage.",
        ("Gémeaux", 3): "Écrivez, échangez, apprenez. Multipliez les conversations, les lectures, les découvertes.",
        ("Gémeaux", 11): "Connectez-vous à votre réseau. Partagez vos idées, collaborez sur des projets collectifs.",
        ("Cancer", 4): "Passez du temps de qualité chez vous ou avec votre famille. Créez un cocon sécurisant.",
        ("Cancer", 12): "Accordez-vous des moments de solitude réparatrice. Écoutez votre intuition, reposez-vous.",
        ("Lion", 5): "Exprimez votre créativité sans retenue. Amusez-vous, brillez, assumez votre unicité.",
        ("Lion", 10): "Osez vous mettre en avant professionnellement. Votre confiance inspire, utilisez-la.",
        ("Vierge", 6): "Optimisez votre quotidien. Instaurez une routine efficace, prenez soin de votre santé.",
        ("Vierge", 3): "Organisez vos idées. Classez, triez, structurez votre mental et votre environnement.",
        ("Balance", 7): "Renforcez vos relations importantes. Cherchez l'harmonie, écoutez l'autre autant que vous-même.",
        ("Balance", 1): "Trouvez l'équilibre entre vos besoins et ceux d'autrui. Affirmez-vous avec diplomatie.",
        ("Scorpion", 8): "Plongez dans vos émotions profondes. Libérez ce qui stagne, transformez-vous de l'intérieur.",
        ("Scorpion", 12): "Méditez, explorez votre inconscient. Laissez mourir ce qui doit partir.",
        ("Sagittaire", 9): "Planifiez un voyage, physique ou mental. Inscrivez-vous à une formation, élargissez vos horizons.",
        ("Sagittaire", 3): "Apprenez quelque chose de totalement nouveau. Votre curiosité est un moteur puissant.",
        ("Capricorne", 10): "Fixez-vous des objectifs professionnels clairs et réalistes. Construisez méthodiquement.",
        ("Capricorne", 6): "Structurez votre quotidien avec discipline. Créez des habitudes solides.",
        ("Verseau", 11): "Engagez-vous dans votre communauté. Innovez, apportez votre vision unique.",
        ("Verseau", 1): "Assumez votre différence. Expérimentez, libérez-vous des conventions.",
        ("Poissons", 12): "Méditez, créez artistiquement, reposez-vous. Votre intuition est votre guide.",
        ("Poissons", 4): "Créez un sanctuaire chez vous. Laissez parler votre imagination, votre spiritualité."
    }

    # Chercher combinaison exacte, sinon fallback maison uniquement
    advice = advice_map.get((ascendant_normalized, house))
    if advice:
        return advice

    # Fallback par maison uniquement
    house_advice = {
        1: "Réaffirmez qui vous êtes. Prenez une décision qui reflète votre véritable identité.",
        2: "Évaluez vos ressources. Que pouvez-vous cultiver, développer, valoriser ?",
        3: "Communiquez davantage. Apprenez, échangez, bougez localement.",
        4: "Ressourcez-vous chez vous. Prenez soin de votre base émotionnelle.",
        5: "Créez, jouez, exprimez-vous. Faites quelque chose qui vous procure de la joie.",
        6: "Améliorez une routine. Prenez soin de votre corps, optimisez votre quotidien.",
        7: "Renforcez une relation clé. Écoutez, collaborez, trouvez l'équilibre.",
        8: "Libérez une émotion profonde. Transformez quelque chose d'interne.",
        9: "Élargissez votre vision. Apprenez, voyagez, explorez de nouvelles philosophies.",
        10: "Avancez sur un objectif professionnel. Construisez votre carrière stratégiquement.",
        11: "Connectez-vous à votre réseau. Partagez vos idéaux, collaborez.",
        12: "Reposez-vous. Méditez, écoutez votre intuition, lâchez prise."
    }

    return house_advice.get(house, "Observez ce qui émerge naturellement ce mois-ci. Faites confiance à votre ressenti.")


def get_moon_phase_description(phase: str) -> str:
    """Description de la phase lunaire"""

    phases = {
        "new_moon": "🌑 Nouvelle Lune : Nouveau départ, intentions fraîches",
        "waxing_crescent": "🌒 Premier croissant : Croissance et expansion",
        "first_quarter": "🌓 Premier quartier : Action et décision",
        "waxing_gibbous": "🌔 Gibbeuse croissante : Affinage et ajustement",
        "full_moon": "🌕 Pleine Lune : Culmination et révélation",
        "waning_gibbous": "🌖 Gibbeuse décroissante : Récolte et gratitude",
        "last_quarter": "🌗 Dernier quartier : Lâcher-prise et tri",
        "waning_crescent": "🌘 Dernier croissant : Repos et préparation"
    }

    return phases.get(phase, "🌙 Phase lunaire")
