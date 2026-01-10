"""
Service de génération du rapport mensuel de Révolution Lunaire (v4)

Architecture template-first (pas d'IA) :
- Templates déterministes basés sur moon_sign + moon_house + lunar_ascendant
- Réutilisation de enrich_aspects_v4() pour les aspects majeurs
- Tone v4 : senior professionnel, structuré, concret

Scope MVP :
- Climat général du mois (2-3 phrases)
- Axes dominants (2-3 axes de vie)
- Aspects majeurs du cycle (max 5)
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

# === TEMPLATES CLIMAT GÉNÉRAL ===

# Templates par combinaison (moon_sign, moon_house)
# Format : (signe, maison) -> texte climat
CLIMATE_TEMPLATES: Dict[tuple, str] = {
    # Lune en Bélier
    ('Aries', 1): "Mois d'impulsion identitaire forte. Besoin d'affirmer ton individualité, d'initier des projets personnels. Attention à l'impatience et à l'impulsivité.",
    ('Aries', 2): "Énergie tournée vers l'acquisition de ressources et la sécurité matérielle. Action directe pour construire, mais attention aux dépenses impulsives.",
    ('Aries', 3): "Communication intense et directe. Besoin de parler, d'échanger, de bouger dans ton environnement proche. Mental actif, parfois agité.",
    ('Aries', 4): "Impulsion domestique : besoin de rénover, transformer ton espace de vie. Tensions possibles dans la sphère familiale, affirmation de tes besoins émotionnels.",
    ('Aries', 5): "Créativité débordante, besoin d'expression personnelle et de plaisir. Prends des risques créatifs, lance-toi, mais attention à la dispersion.",
    ('Aries', 6): "Action dans le quotidien : réorganise ta routine, améliore ta santé, optimise ton travail. Énergie mise au service de l'efficacité.",
    ('Aries', 7): "Dynamique relationnelle intense. Besoin d'affirmation dans les partenariats, risque de conflits directs. Apprends à négocier sans agressivité.",
    ('Aries', 8): "Transformation profonde en cours. Besoin de contrôle sur les ressources partagées, gestion de l'intimité. Intensité émotionnelle, crises possibles.",
    ('Aries', 9): "Expansion mentale et géographique. Besoin d'aventure, de découverte, d'apprentissages nouveaux. Optimisme conquérant, attention à la sur-extension.",
    ('Aries', 10): "Ambition professionnelle activée. Besoin de visibilité, de reconnaissance, d'accomplissement. Initiative dans la carrière, mais attention aux coups de tête.",
    ('Aries', 11): "Projets collectifs dynamisés. Besoin d'agir pour tes idéaux, de fédérer autour de causes. Attention aux conflits dans les groupes.",
    ('Aries', 12): "Impulsion intérieure : besoin de solitude active, de méditation en mouvement. Lutte interne entre action et lâcher-prise.",

    # Lune en Taureau
    ('Taurus', 1): "Mois centré sur l'ancrage identitaire. Besoin de stabilité, de sécurité, de construire une base solide. Lenteur assumée, résistance au changement.",
    ('Taurus', 2): "Consolidation matérielle : gestion des finances, acquisition de biens, sécurisation des ressources. Pragmatisme et patience au service de la stabilité.",
    ('Taurus', 3): "Communication posée et concrète. Besoin d'échanger sur le tangible, de parler avec lenteur. Attention à la rigidité mentale.",
    ('Taurus', 4): "Enracinement familial et domestique. Besoin de confort à la maison, de traditions, de sécurité émotionnelle. Construction d'un nid stable.",
    ('Taurus', 5): "Plaisir sensuel et créativité matérielle. Besoin de créer avec les mains, de profiter des plaisirs simples. Art, cuisine, jardinage favorisés.",
    ('Taurus', 6): "Routine stable et productive. Organisation du quotidien, santé par l'alimentation et le corps. Travail méthodique, attention à l'inertie.",
    ('Taurus', 7): "Relations stables et loyales. Besoin de sécurité affective, de partenariats durables. Possessivité à surveiller.",
    ('Taurus', 8): "Gestion prudente des ressources partagées. Besoin de contrôle sur l'argent commun, l'héritage. Transformation lente mais profonde.",
    ('Taurus', 9): "Expansion concrète : voyages pour la beauté, apprentissages pratiques. Besoin de philosophie incarnée, de sens tangible.",
    ('Taurus', 10): "Carrière orientée vers la stabilité et la reconnaissance matérielle. Construction patiente d'un statut solide. Résistance aux changements professionnels.",
    ('Taurus', 11): "Projets collectifs concrets et durables. Besoin d'idéaux incarnés, de communautés stables. Attention à la résistance aux nouvelles idées.",
    ('Taurus', 12): "Besoin de solitude sensorielle : nature, silence, repos. Lâcher-prise par le corps, méditation incarnée.",

    # Lune en Gémeaux
    ('Gemini', 1): "Mois d'identité multiple et curieuse. Besoin d'explorer différentes facettes de toi-même, de parler, d'apprendre. Dispersion identitaire possible.",
    ('Gemini', 2): "Ressources gérées avec souplesse. Besoin de diversifier les sources de revenus, de communiquer sur tes valeurs. Attention à la dispersion financière.",
    ('Gemini', 3): "Communication intense et multidirectionnelle. Besoin d'échanger, d'apprendre, de bouger dans ton environnement. Mental hyperactif, attention à la saturation.",
    ('Gemini', 4): "Foyer en mouvement : discussions familiales, déplacements domestiques. Besoin de légèreté émotionnelle, d'adapter ton espace de vie.",
    ('Gemini', 5): "Créativité ludique et intellectuelle. Besoin de jouer avec les idées, de multiplier les projets créatifs. Dispersion possible, manque de profondeur.",
    ('Gemini', 6): "Routine flexible et variée. Besoin de changer de tâches, de diversifier ton travail. Attention à la dispersion dans le quotidien.",
    ('Gemini', 7): "Relations légères et communicatives. Besoin d'échanges verbaux, de partenariats intellectuels. Attention à l'évitement émotionnel.",
    ('Gemini', 8): "Transformation par la communication. Besoin de parler de l'intimité, de comprendre les crises. Intellectualisation des émotions profondes.",
    ('Gemini', 9): "Expansion intellectuelle : voyages, études, découvertes multiples. Besoin de comprendre le monde, d'apprendre sans cesse.",
    ('Gemini', 10): "Carrière orientée vers la communication et la diversité. Besoin de flexibilité professionnelle, de multiplier les casquettes.",
    ('Gemini', 11): "Projets collectifs variés et communicatifs. Besoin de réseauter, d'échanger des idées, de fédérer par la parole.",
    ('Gemini', 12): "Besoin de solitude mentale : écriture, lecture, réflexion. Lâcher-prise par l'intellect, méditation sur les pensées.",

    # Fallback générique par signe (si maison non mappée)
    ('Aries', None): "Mois dynamique et impulsif. Besoin d'action, d'initiative, d'affirmation personnelle. Attention à l'impatience.",
    ('Taurus', None): "Mois stable et ancré. Besoin de sécurité, de construction, de plaisirs sensoriels. Attention à l'inertie.",
    ('Gemini', None): "Mois communicatif et curieux. Besoin d'échanger, d'apprendre, de bouger. Attention à la dispersion.",
    ('Cancer', None): "Mois émotionnel et protecteur. Besoin de sécurité affective, de foyer, de lien familial. Attention aux fluctuations émotionnelles.",
    ('Leo', None): "Mois créatif et rayonnant. Besoin d'expression personnelle, de reconnaissance, de générosité. Attention à l'ego.",
    ('Virgo', None): "Mois organisé et analytique. Besoin d'ordre, de service, de perfectionnement. Attention au perfectionnisme paralysant.",
    ('Libra', None): "Mois relationnel et harmonieux. Besoin d'équilibre, de partenariats, d'esthétique. Attention à l'indécision.",
    ('Scorpio', None): "Mois intense et transformateur. Besoin de profondeur, de contrôle, de régénération. Attention aux crises émotionnelles.",
    ('Sagittarius', None): "Mois expansif et optimiste. Besoin d'aventure, de sens, de liberté. Attention à la sur-extension.",
    ('Capricorn', None): "Mois structuré et ambitieux. Besoin d'accomplissement, de responsabilité, de discipline. Attention à la rigidité.",
    ('Aquarius', None): "Mois innovant et collectif. Besoin de liberté, de projets originaux, d'indépendance. Attention au détachement émotionnel.",
    ('Pisces', None): "Mois fluide et empathique. Besoin de dissolution, de spiritualité, de compassion. Attention à la confusion.",
}


# === MAPPING MAISONS → AXES DE VIE ===

HOUSE_AXES: Dict[int, str] = {
    1: "Identité, apparence, initiatives personnelles",
    2: "Ressources, valeurs, sécurité matérielle",
    3: "Communication, apprentissages, environnement proche",
    4: "Foyer, famille, racines, sécurité émotionnelle",
    5: "Créativité, plaisir, expression personnelle",
    6: "Quotidien, santé, service, organisation",
    7: "Relations, partenariats, altérité",
    8: "Transformation, intimité, ressources partagées",
    9: "Expansion, philosophie, voyages, quête de sens",
    10: "Carrière, accomplissement, visibilité sociale",
    11: "Projets collectifs, amitiés, idéaux",
    12: "Spiritualité, introspection, lâcher-prise"
}


# === FONCTION PRINCIPALE ===

def build_lunar_report_v4(lunar_return: Any) -> Dict[str, Any]:
    """
    Construit le rapport mensuel de la révolution lunaire (v4)

    Args:
        lunar_return: Objet LunarReturn de la DB

    Returns:
        {
            'header': {...},
            'general_climate': str,
            'dominant_axes': List[str],
            'major_aspects': List[Dict]
        }
    """
    logger.info(f"[LunarReportBuilder] Construction rapport v4 pour month={lunar_return.month}")

    # 1. HEADER (factuel)
    header = _build_header(lunar_return)

    # 2. CLIMAT GÉNÉRAL (template)
    general_climate = _build_general_climate(lunar_return)

    # 3. AXES DOMINANTS (logique simple)
    dominant_axes = _build_dominant_axes(lunar_return)

    # 4. ASPECTS MAJEURS (réutiliser enrich_aspects_v4)
    major_aspects = _build_major_aspects(lunar_return)

    report = {
        'header': header,
        'general_climate': general_climate,
        'dominant_axes': dominant_axes,
        'major_aspects': major_aspects
    }

    logger.info(f"[LunarReportBuilder] ✅ Rapport construit - climate_len={len(general_climate)}, axes_count={len(dominant_axes)}, aspects_count={len(major_aspects)}")

    return report


def _build_header(lunar_return: Any) -> Dict[str, Any]:
    """Construit le header du rapport (factuel)"""
    return_date = lunar_return.return_date

    # Calculer date de fin (return_date + 1 mois)
    from datetime import timedelta
    from dateutil.relativedelta import relativedelta

    end_date = return_date + relativedelta(months=1)

    # Format mois (ex: "Janvier 2025")
    month_name = return_date.strftime('%B %Y')

    # Format dates (ex: "Du 15 jan au 12 fév")
    start_str = return_date.strftime('%-d %b')
    end_str = end_date.strftime('%-d %b')

    return {
        'month': month_name.capitalize(),
        'dates': f"Du {start_str} au {end_str}",
        'moon_sign': lunar_return.moon_sign or 'N/A',
        'moon_house': lunar_return.moon_house,
        'lunar_ascendant': lunar_return.lunar_ascendant or 'N/A'
    }


def _build_general_climate(lunar_return: Any) -> str:
    """Construit le climat général du mois via templates"""
    moon_sign = lunar_return.moon_sign
    moon_house = lunar_return.moon_house

    # Lookup template (signe, maison)
    template_key = (moon_sign, moon_house)

    if template_key in CLIMATE_TEMPLATES:
        climate = CLIMATE_TEMPLATES[template_key]
    else:
        # Fallback : template par signe uniquement
        fallback_key = (moon_sign, None)
        climate = CLIMATE_TEMPLATES.get(fallback_key, "Mois de révolution lunaire en cours.")

    # Ajouter mention de l'ascendant si présent
    if lunar_return.lunar_ascendant:
        climate += f" Ascendant {lunar_return.lunar_ascendant} : coloration du filtre perceptif ce mois-ci."

    return climate


def _build_dominant_axes(lunar_return: Any) -> List[str]:
    """Identifie 2-3 axes dominants du mois"""
    axes = []

    # 1. Axe de la maison de la Lune (toujours présent)
    if lunar_return.moon_house:
        moon_axis = HOUSE_AXES.get(lunar_return.moon_house, "Domaine de vie non défini")
        axes.append(f"Maison {lunar_return.moon_house} : {moon_axis}")

    # 2. Analyser aspects pour identifier maisons activées
    # Logique simple : prendre les maisons des planètes impliquées dans aspects serrés (orbe <= 3)
    aspects = lunar_return.aspects or []
    planets_data = lunar_return.planets or {}

    activated_houses = set()
    for aspect in aspects:
        orb = abs(aspect.get('orb', 999))
        if orb <= 3:  # Aspect serré
            planet1 = aspect.get('planet1', '').lower()
            planet2 = aspect.get('planet2', '').lower()

            # Récupérer maisons des planètes
            for planet_key, planet_data in planets_data.items():
                if isinstance(planet_data, dict):
                    if planet_key.lower() == planet1 or planet_key.lower() == planet2:
                        house = planet_data.get('house')
                        if house:
                            activated_houses.add(house)

    # Ajouter max 2 axes supplémentaires (hors maison de la Lune)
    for house in sorted(activated_houses):
        if house != lunar_return.moon_house and len(axes) < 3:
            house_axis = HOUSE_AXES.get(house, "Domaine de vie")
            axes.append(f"Maison {house} : {house_axis}")

    # Si moins de 2 axes, compléter avec fallback
    if len(axes) < 2:
        axes.append("Période centrée sur l'intégration du cycle lunaire en cours")

    return axes[:3]  # Max 3 axes


def _build_major_aspects(lunar_return: Any) -> List[Dict[str, Any]]:
    """Enrichit les aspects majeurs du cycle via enrich_aspects_v4"""
    aspects = lunar_return.aspects or []
    planets_data = lunar_return.planets or {}

    if not aspects:
        logger.warning("[LunarReportBuilder] Aucun aspect trouvé pour ce cycle")
        return []

    # Réutiliser enrich_aspects_v4
    try:
        from services.aspect_explanation_service import enrich_aspects_v4

        enriched = enrich_aspects_v4(aspects, planets_data, limit=5)
        logger.info(f"[LunarReportBuilder] ✅ {len(enriched)} aspects enrichis v4")
        return enriched

    except Exception as e:
        logger.error(f"[LunarReportBuilder] ❌ Erreur enrichissement aspects: {e}", exc_info=True)
        return []
