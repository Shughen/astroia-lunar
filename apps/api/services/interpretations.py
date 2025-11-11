"""
Générateur d'interprétations textuelles pour révolutions lunaires
Templates dynamiques basés sur l'ascendant, la maison et les aspects
"""

from typing import Dict, Any, List


# === INTERPRÉTATIONS PAR ASCENDANT LUNAIRE ===
ASCENDANT_INTERPRETATIONS = {
    "Bélier": "Ce mois, ton énergie est tournée vers l'action et l'initiative. C'est le moment de lancer de nouveaux projets.",
    "Taureau": "La stabilité et le confort sont tes priorités ce mois-ci. Ancre-toi dans tes sens et tes ressources.",
    "Gémeaux": "Ta curiosité intellectuelle est à son pic. Communique, échange, et reste flexible.",
    "Cancer": "Tes émotions et ton foyer sont au centre ce mois-ci. Prends soin de toi et de tes proches.",
    "Lion": "Mets-toi en avant ce mois-ci ! Ta créativité et ta confiance sont tes meilleurs atouts.",
    "Vierge": "Organisation et précision sont tes alliées. Optimise ton quotidien et ta santé.",
    "Balance": "L'harmonie dans tes relations est essentielle ce mois-ci. Recherche l'équilibre.",
    "Scorpion": "Plonge en profondeur et transforme-toi. C'est un mois d'introspection intense.",
    "Sagittaire": "Explore, apprends, voyage (physiquement ou mentalement). Élargis tes horizons.",
    "Capricorne": "Structure tes ambitions ce mois-ci. Discipline et patience sont tes forces.",
    "Verseau": "Innovation et originalité sont à l'honneur. Pense différemment et connecte-toi à ta communauté.",
    "Poissons": "Laisse parler ton intuition et ta créativité. C'est un mois spirituel et artistique."
}

# === INTERPRÉTATIONS PAR MAISON ===
HOUSE_INTERPRETATIONS = {
    1: "Ta personnalité et ton identité sont mises en lumière. C'est un renouveau personnel.",
    2: "Tes ressources matérielles et tes valeurs sont au centre. Gère tes finances et ton estime de toi.",
    3: "Communication, apprentissage et relations de proximité sont favorisés ce mois-ci.",
    4: "Ton foyer, ta famille et tes racines demandent ton attention. C'est un mois introspectif.",
    5: "Créativité, romance et plaisir sont à l'honneur. Exprime-toi librement !",
    6: "Santé, routine et service sont tes priorités. Optimise ton quotidien.",
    7: "Tes relations et partenariats sont au centre. Cherche l'équilibre avec les autres.",
    8: "Transformation profonde, intimité et ressources partagées. Un mois intense.",
    9: "Expansion, voyages et philosophie. Élargis tes horizons mentaux et physiques.",
    10: "Carrière et ambitions publiques. C'est le moment de briller professionnellement.",
    11: "Amis, communauté et projets collectifs. Connecte-toi à ton réseau.",
    12: "Spiritualité, repos et inconscient. Un mois pour te retirer et méditer."
}

# === INTERPRÉTATIONS PAR ASPECT ===
ASPECT_INTERPRETATIONS = {
    "conjunction": "fusion intense d'énergies",
    "opposition": "tension créative à équilibrer",
    "trine": "harmonie et fluidité naturelle",
    "square": "défi stimulant pour grandir",
    "sextile": "opportunité à saisir avec un peu d'effort"
}


def generate_lunar_return_interpretation(
    lunar_ascendant: str,
    moon_house: int,
    aspects: List[Dict[str, Any]]
) -> str:
    """
    Génère une interprétation textuelle complète
    
    Args:
        lunar_ascendant: Ascendant de la révolution lunaire
        moon_house: Maison où se trouve la Lune
        aspects: Liste d'aspects [ { "type": "trine", "planet": "Venus", ... }, ... ]
    
    Returns:
        Texte d'interprétation (3-5 paragraphes)
    """
    
    interpretation_parts = []
    
    # 1. Introduction générale (ascendant)
    asc_text = ASCENDANT_INTERPRETATIONS.get(
        lunar_ascendant,
        "Ce mois marque un nouveau cycle lunaire pour toi."
    )
    interpretation_parts.append(f"**Ton mois lunaire** : {asc_text}")
    
    # 2. Focus maison
    house_text = HOUSE_INTERPRETATIONS.get(
        moon_house,
        "Ta Lune éclaire un domaine important de ta vie."
    )
    interpretation_parts.append(f"**Focus du mois** : {house_text}")
    
    # 3. Aspects majeurs (si présents)
    if aspects:
        major_aspects = [a for a in aspects if a.get("type") in ASPECT_INTERPRETATIONS]
        if major_aspects:
            aspect = major_aspects[0]  # Prendre le premier aspect majeur
            aspect_type = aspect["type"]
            planet = aspect.get("planet", "une planète")
            aspect_desc = ASPECT_INTERPRETATIONS.get(aspect_type, "énergie particulière")
            
            interpretation_parts.append(
                f"**Énergie clé** : Ta Lune forme un {aspect_type} avec {planet}, "
                f"créant une {aspect_desc} ce mois-ci."
            )
    
    # 4. Conseil pratique
    practical_advice = _get_practical_advice(lunar_ascendant, moon_house)
    interpretation_parts.append(f"**Conseil pratique** : {practical_advice}")
    
    return "\n\n".join(interpretation_parts)


def _get_practical_advice(ascendant: str, house: int) -> str:
    """Génère un conseil pratique basé sur l'ascendant et la maison"""
    
    advice_map = {
        ("Bélier", 1): "Lance un projet personnel qui te tient à cœur.",
        ("Taureau", 2): "Fais un bilan de tes finances et de tes talents.",
        ("Gémeaux", 3): "Écris, communique, apprends quelque chose de nouveau.",
        ("Cancer", 4): "Passe du temps de qualité avec ta famille ou chez toi.",
        ("Lion", 5): "Exprime ta créativité sans retenue, amuse-toi !",
        ("Vierge", 6): "Mets en place une nouvelle routine bien-être.",
        ("Balance", 7): "Renforce tes relations importantes, cherche l'harmonie.",
        ("Scorpion", 8): "Explore tes émotions profondes, transforme-toi.",
        ("Sagittaire", 9): "Planifie un voyage ou inscris-toi à une formation.",
        ("Capricorne", 10): "Fixe-toi des objectifs professionnels clairs.",
        ("Verseau", 11): "Connecte-toi avec ta communauté, innove.",
        ("Poissons", 12): "Médite, repose-toi, écoute ton intuition."
    }
    
    return advice_map.get(
        (ascendant, house),
        "Reste à l'écoute de tes besoins et avance à ton rythme."
    )


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

