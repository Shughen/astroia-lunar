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
from typing import Dict, Any, List, Optional, Tuple
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


# === TEMPLATES ENRICHIS POUR CLIMAT GÉNÉRAL (V5 - ton accessible) ===

# A. Phrases d'accroche par signe lunaire (ton chaleureux, 1-2 phrases)
MOON_SIGN_INTRO: Dict[str, str] = {
    'Aries': "Ce mois-ci, tu ressens une envie d'agir, de bouger, de lancer de nouvelles choses. L'énergie est vive, parfois impatiente — c'est normal, c'est le moment d'initier.",
    'Taurus': "Ce mois-ci, tu cherches la stabilité et le confort. Besoin de te poser, de construire quelque chose de concret, de prendre soin de toi à ton rythme.",
    'Gemini': "Ce mois-ci, ton esprit est en ébullition : envie de parler, d'apprendre, de papillonner. La curiosité est ton moteur, même si tu peux te sentir un peu dispersé(e).",
    'Cancer': "Ce mois-ci, tes émotions sont au premier plan. Besoin de cocooning, de liens familiaux, de te sentir en sécurité affective. Écoute ce que ton cœur te dit.",
    'Leo': "Ce mois-ci, tu as besoin de briller et d'exprimer qui tu es vraiment. Créativité, générosité, envie de reconnaissance — assume ta lumière.",
    'Virgo': "Ce mois-ci, tu ressens le besoin de mettre de l'ordre dans ta vie. Organisation, santé, amélioration du quotidien : les détails comptent.",
    'Libra': "Ce mois-ci, l'harmonie relationnelle est ta priorité. Envie d'équilibre, de beauté, de partage. Les autres jouent un rôle important dans ton bien-être.",
    'Scorpio': "Ce mois-ci, tu vas en profondeur. Émotions intenses, besoin de vérité, envie de transformer ce qui ne fonctionne plus. Période puissante.",
    'Sagittarius': "Ce mois-ci, tu as soif d'aventure et de sens. Envie de voyager (physiquement ou mentalement), d'apprendre, de voir plus grand.",
    'Capricorn': "Ce mois-ci, tu es focalisé(e) sur tes objectifs. Ambition, discipline, envie de construire quelque chose de durable. Le travail paie.",
    'Aquarius': "Ce mois-ci, tu aspires à plus de liberté et d'originalité. Besoin de faire les choses à ta façon, de t'investir dans des causes qui te parlent.",
    'Pisces': "Ce mois-ci, ta sensibilité est décuplée. Intuition forte, besoin de calme et de rêverie. Accorde-toi des moments de pause et d'évasion.",
}

# A-bis. Anciens templates techniques (conservés pour compatibilité)
MOON_SIGN_BASE_TONES: Dict[str, str] = {
    'Aries': "Cycle lunaire sous signe de Feu cardinal : impulsion directe, action immédiate, besoin d'initier nouvelles dynamiques. Réactions émotionnelles rapides et spontanées, impatience structurelle marquée. Initiative personnelle comme mode d'expression privilégié ce mois-ci.",
    'Taurus': "Cycle lunaire sous signe de Terre fixe : ancrage matériel, stabilité recherchée, besoin de sécurité tangible et durable. Réactions émotionnelles lentes et posées, résistance au changement prononcée. Construction patiente comme mode d'expression ce mois-ci.",
    'Gemini': "Cycle lunaire sous signe d'Air mutable : curiosité intellectuelle, communication multiple, besoin de variété et d'échanges constants. Réactions émotionnelles rapides mais superficielles, dispersion mentale marquée. Échange verbal comme mode d'expression privilégié ce mois-ci.",
    'Cancer': "Cycle lunaire sous signe d'Eau cardinal : protection instinctive, émotivité profonde, besoin de sécurité affective absolue. Réactions émotionnelles intenses et fluctuantes, humeur changeante selon environnement. Nourrir et être nourri comme mode d'expression privilégié ce mois-ci.",
    'Leo': "Cycle lunaire sous signe de Feu fixe : rayonnement personnel, créativité généreuse, besoin de reconnaissance et d'admiration. Réactions émotionnelles dramatiques et théâtrales, fierté prononcée et sensible. Expression personnelle généreuse comme mode privilégié ce mois-ci.",
    'Virgo': "Cycle lunaire sous signe de Terre mutable : analyse détaillée, service méthodique, besoin d'ordre et de perfectionnement constant. Réactions émotionnelles contrôlées et mesurées, perfectionnisme émotionnel marqué. Organisation méthodique comme mode d'expression ce mois-ci.",
    'Libra': "Cycle lunaire sous signe d'Air cardinal : harmonie recherchée, relation prioritaire, besoin d'équilibre et de justice esthétique. Réactions émotionnelles pondérées et diplomatiques, indécision structurelle marquée. Médiation et esthétique comme modes privilégiés ce mois-ci.",
    'Scorpio': "Cycle lunaire sous signe d'Eau fixe : intensité magnétique, transformation radicale, besoin de profondeur et de vérité absolue. Réactions émotionnelles puissantes et concentrées, contrôle rigoureux des affects. Régénération et fusion comme modes d'expression ce mois-ci.",
    'Sagittarius': "Cycle lunaire sous signe de Feu mutable : expansion optimiste, philosophie aventureuse, besoin de sens et de liberté totale. Réactions émotionnelles enthousiastes et généreuses, sur-extension possible et fréquente. Exploration et quête comme modes d'expression ce mois-ci.",
    'Capricorn': "Cycle lunaire sous signe de Terre cardinal : structure rigoureuse, ambition pragmatique, besoin d'accomplissement et de reconnaissance sociale. Réactions émotionnelles retenues et contrôlées, discipline affective stricte. Responsabilité et construction comme modes d'expression ce mois-ci.",
    'Aquarius': "Cycle lunaire sous signe d'Air fixe : innovation collective, indépendance absolue, besoin de liberté et d'originalité assumée. Réactions émotionnelles détachées et rationalisées, intellectualisation marquée des affects. Originalité collective comme mode d'expression ce mois-ci.",
    'Pisces': "Cycle lunaire sous signe d'Eau mutable : fluidité émotionnelle, empathie fusionnelle, besoin de dissolution des frontières et de transcendance. Réactions émotionnelles diffuses et poreuses, sensibilité extrême à l'environnement. Compassion imaginative comme mode d'expression ce mois-ci.",
}

# B. Snippets aspects lunaires pour climat (40 mots chacun)
ASPECT_CLIMATE_SNIPPETS: Dict[Tuple[str, str, str], str] = {
    # Moon-Sun aspects
    ('Moon', 'Sun', 'conjunction'): "Lune-Soleil fusionnées : besoins émotionnels et identité alignés. Mois d'unification interne, cohérence entre volonté et ressenti. Concrètement : actions portées par les émotions, expression directe des besoins. Difficulté à dissocier ce que tu veux de ce dont tu as besoin.",
    ('Moon', 'Sun', 'opposition'): "Lune-Soleil en miroir : tension entre besoins émotionnels et volonté identitaire. Négociation constante entre ce que tu ressens et ce que tu veux affirmer. Concrètement : tiraillements entre sécurité et expression, entre nourrir et briller. Intégration des polarités nécessaire.",
    ('Moon', 'Sun', 'square'): "Lune-Soleil en friction : besoins émotionnels contrarient l'expression identitaire. Inconfort productif entre sécurité et affirmation. Concrètement : frustrations entre attentes familiales et ambitions personnelles, ajustements constants. Cette tension force la croissance.",
    ('Moon', 'Sun', 'trine'): "Lune-Soleil en harmonie : besoins émotionnels et identité fluides. Facilité naturelle à exprimer tes émotions, cohérence spontanée. Concrètement : confiance émotionnelle, authenticité sans effort. Attention à la complaisance : cette aisance nécessite activation consciente.",

    # Moon-Mercury aspects
    ('Moon', 'Mercury', 'conjunction'): "Lune-Mercure fusionnées : émotions et intellect indissociables. Pensée teintée d'affect, communication émotionnelle intense. Concrètement : besoin de verbaliser tes ressentis, subjectivité assumée dans l'analyse. Difficulté à séparer fait et ressenti.",
    ('Moon', 'Mercury', 'opposition'): "Lune-Mercure en miroir : tension entre ressenti et raisonnement. Dialogue interne entre cœur et tête, négociation constante. Concrètement : difficulté à choisir entre logique et intuition, besoin d'intégrer les deux registres. Équilibre à construire.",
    ('Moon', 'Mercury', 'square'): "Lune-Mercure en friction : émotions parasitent la clarté mentale. Inconfort entre besoin de sécurité et nécessité d'analyser. Concrètement : rumination émotionnelle, difficulté à rationaliser les affects. Cette tension force la lucidité.",
    ('Moon', 'Mercury', 'trine'): "Lune-Mercure en harmonie : émotions et intellect s'enrichissent mutuellement. Intelligence émotionnelle fluide, communication des ressentis aisée. Concrètement : talent naturel pour nommer les affects, empathie verbale. Vigilance sur intellectualisation excessive.",

    # Moon-Venus aspects
    ('Moon', 'Venus', 'conjunction'): "Lune-Vénus fusionnées : besoins émotionnels et affectifs alignés. Attachement rapide, émotions esthétisées. Concrètement : besoin de beauté et de confort fusionnés, affection spontanée. Difficulté à distinguer affection et dépendance affective.",
    ('Moon', 'Venus', 'opposition'): "Lune-Vénus en miroir : tension entre besoins de sécurité et désirs affectifs. Négociation entre ce dont tu as besoin et ce que tu désires. Concrètement : oscillation entre autonomie émotionnelle et fusion affective. Équilibre relationnel à trouver.",
    ('Moon', 'Venus', 'square'): "Lune-Vénus en friction : besoins émotionnels contrarient les désirs affectifs. Inconfort entre sécurité et plaisir. Concrètement : frustrations relationnelles, difficulté à obtenir satisfaction émotionnelle. Cette tension affine les valeurs affectives.",
    ('Moon', 'Venus', 'trine'): "Lune-Vénus en harmonie : besoins émotionnels et affectifs fluides. Facilité à créer du lien, charme naturel. Concrètement : relations nourrissantes sans effort, esthétique réconfortante. Attention à la passivité : cette facilité demande activation.",

    # Moon-Mars aspects
    ('Moon', 'Mars', 'conjunction'): "Lune-Mars fusionnées : réactivité émotionnelle intense, besoins traduits en action directe. Concrètement : irritabilité productive, impatience qui mobilise, urgence émotionnelle. Difficulté à séparer besoin et impulsion. Cette fusion génère du mouvement mais nécessite canalisation.",
    ('Moon', 'Mars', 'opposition'): "Lune-Mars en miroir : tension entre besoins de sécurité et pulsions d'action. Négociation entre nourrir et combattre. Concrètement : colère défensive, alternance entre retrait protecteur et offensive. Équilibre entre protection et affirmation à construire.",
    ('Moon', 'Mars', 'square'): "Lune-Mars en friction : besoins émotionnels contrarient l'action directe. Inconfort entre sécurité et affirmation. Concrètement : frustrations qui activent, colère comme signal de besoins non satisfaits. Cette tension force l'assertivité.",
    ('Moon', 'Mars', 'trine'): "Lune-Mars en harmonie : besoins émotionnels et action alignés. Dynamisme émotionnel fluide, courage instinctif. Concrètement : capacité à agir pour tes besoins sans hésitation, affirmation spontanée. Attention à l'impulsivité : cette facilité demande direction.",

    # Moon-Jupiter aspects
    ('Moon', 'Jupiter', 'conjunction'): "Lune-Jupiter fusionnées : besoins émotionnels amplifiés, générosité affective débordante. Concrètement : optimisme émotionnel, foi instinctive, excès possibles dans la recherche de confort. Difficulté à modérer les besoins. Cette fusion nourrit mais peut sur-étendre.",
    ('Moon', 'Jupiter', 'opposition'): "Lune-Jupiter en miroir : tension entre besoins de sécurité et expansion. Négociation entre prudence émotionnelle et foi. Concrètement : oscillation entre retrait protecteur et générosité excessive. Équilibre entre expansion et ancrage à trouver.",
    ('Moon', 'Jupiter', 'square'): "Lune-Jupiter en friction : besoins de sécurité contrarient l'expansion. Inconfort entre prudence et optimisme. Concrètement : sur-extension émotionnelle, promesses excessives, difficulté à poser des limites. Cette tension force la mesure.",
    ('Moon', 'Jupiter', 'trine'): "Lune-Jupiter en harmonie : besoins émotionnels et expansion fluides. Optimisme naturel, générosité spontanée. Concrètement : confiance émotionnelle, capacité à voir grand. Attention à l'excès : cette facilité peut générer complaisance ou dispersion.",

    # Moon-Saturn aspects
    ('Moon', 'Saturn', 'conjunction'): "Lune-Saturne fusionnées : besoins émotionnels structurés, retenue affective. Concrètement : maturité émotionnelle précoce, responsabilisation des affects, difficulté à exprimer les besoins. Cette fusion discipline mais peut rigidifier. Travail sur l'autorisation à ressentir.",
    ('Moon', 'Saturn', 'opposition'): "Lune-Saturne en miroir : tension entre besoins émotionnels et exigences de structure. Négociation entre spontanéité affective et discipline. Concrètement : culpabilité autour des besoins, alternance entre expression et censure. Intégration maturité-spontanéité nécessaire.",
    ('Moon', 'Saturn', 'square'): "Lune-Saturne en friction : besoins émotionnels contrariés par exigences structurelles. Inconfort entre spontanéité et retenue. Concrètement : frustrations affectives formatrices, difficulté à s'autoriser les besoins. Cette tension construit la maturité émotionnelle.",
    ('Moon', 'Saturn', 'trine'): "Lune-Saturne en harmonie : besoins émotionnels et structure compatibles. Stabilité affective naturelle, fidélité instinctive. Concrètement : capacité à construire des habitudes nourrissantes, loyauté émotionnelle. Attention à la rigidité : cette facilité peut limiter.",

    # Moon-Uranus aspects
    ('Moon', 'Uranus', 'conjunction'): "Lune-Uranus fusionnées : besoins émotionnels imprévisibles, instabilité affective créatrice. Concrètement : besoin de liberté émotionnelle, ruptures soudaines, innovation dans le réconfort. Cette fusion libère mais déstabilise. Travail sur l'ancrage dans le changement.",
    ('Moon', 'Uranus', 'opposition'): "Lune-Uranus en miroir : tension entre besoins de sécurité et pulsions de rupture. Négociation entre stabilité et innovation. Concrètement : alternance entre recherche de confort et sabotage de la routine. Équilibre entre ancrage et liberté à construire.",
    ('Moon', 'Uranus', 'square'): "Lune-Uranus en friction : besoins de sécurité contrariés par pulsions de changement. Inconfort productif entre habitude et innovation. Concrètement : instabilité émotionnelle qui force l'adaptation, besoins atypiques. Cette tension catalyse l'originalité.",
    ('Moon', 'Uranus', 'trine'): "Lune-Uranus en harmonie : besoins émotionnels et innovation fluides. Originalité affective naturelle, indépendance émotionnelle aisée. Concrètement : capacité à réinventer le réconfort, liberté dans les attachements. Attention au détachement excessif.",

    # Moon-Neptune aspects
    ('Moon', 'Neptune', 'conjunction'): "Lune-Neptune fusionnées : besoins émotionnels diffus, porosité affective marquée. Concrètement : empathie fusionnelle, confusion entre tes besoins et ceux d'autrui, besoin de transcendance. Cette fusion ouvre mais dissout les frontières. Travail sur la discrimination affective.",
    ('Moon', 'Neptune', 'opposition'): "Lune-Neptune en miroir : tension entre besoins de sécurité et dissolution des frontières. Négociation entre protection et fusion. Concrètement : oscillation entre retrait défensif et empathie excessive. Équilibre entre compassion et préservation à trouver.",
    ('Moon', 'Neptune', 'square'): "Lune-Neptune en friction : besoins émotionnels contrariés par dissolution des limites. Inconfort entre clarté affective et flou. Concrètement : confusion émotionnelle, idéalisation des besoins, désillusions nécessaires. Cette tension affine la discrimination.",
    ('Moon', 'Neptune', 'trine'): "Lune-Neptune en harmonie : besoins émotionnels et imaginaire fluides. Empathie spontanée, sensibilité artistique naturelle. Concrètement : capacité à nourrir par l'imaginaire, compassion aisée. Attention à la porosité : cette facilité nécessite frontières conscientes.",

    # Moon-Pluto aspects
    ('Moon', 'Pluto', 'conjunction'): "Lune-Pluton fusionnées : besoins émotionnels intenses, transformation affective radicale. Concrètement : crises émotionnelles régénératrices, besoin de contrôle sur la sécurité, profondeur fusionnelle. Cette fusion transforme mais peut obséder. Travail sur le lâcher-prise.",
    ('Moon', 'Pluto', 'opposition'): "Lune-Pluton en miroir : tension entre besoins de sécurité et forces de transformation. Négociation entre préservation et métamorphose. Concrètement : crises relationnelles, alternance entre fusion et pouvoir. Intégration vulnérabilité-puissance nécessaire.",
    ('Moon', 'Pluto', 'square'): "Lune-Pluton en friction : besoins émotionnels contrariés par forces de transformation. Inconfort entre sécurité et régénération. Concrètement : crises affectives formatrices, intensité émotionnelle difficile. Cette tension force la métamorphose profonde.",
    ('Moon', 'Pluto', 'trine'): "Lune-Pluton en harmonie : besoins émotionnels et transformation fluides. Profondeur affective naturelle, résilience instinctive. Concrètement : capacité à régénérer les attachements, force émotionnelle. Attention à l'intensité : cette facilité peut devenir contrôle.",

    # Moon-Ascendant aspects (si disponible)
    ('Moon', 'Ascendant', 'conjunction'): "Lune-Ascendant fusionnés : besoins émotionnels visibles, expression spontanée des affects. Concrètement : émotions lisibles, interface au monde teintée d'affect, besoin d'authenticité émotionnelle. Cette fusion rend transparent mais peut exposer.",
    ('Moon', 'Ascendant', 'opposition'): "Lune-Ascendant en miroir : besoins émotionnels projetés sur l'environnement. Tension entre vie intérieure et présentation extérieure. Concrètement : attentes émotionnelles sur autrui, masque vs authenticité. Équilibre à construire.",

    # Fallbacks par type d'aspect
    ('Moon', 'default', 'conjunction'): "Aspect lunaire serré en conjonction : fusion émotionnelle intense avec fonction planétaire activée. Besoins et expression planétaire indissociables ce mois-ci. Concrètement : amplification mutuelle, difficulté à séparer les registres. Cette symbiose concentre l'énergie émotionnelle.",
    ('Moon', 'default', 'opposition'): "Aspect lunaire en opposition : tension polarisée entre besoins émotionnels et fonction planétaire activée. Négociation entre ces deux pôles ce mois-ci. Concrètement : tiraillements, nécessité d'intégration. Équilibre à construire entre les deux registres.",
    ('Moon', 'default', 'square'): "Aspect lunaire en carré : friction productive entre besoins émotionnels et fonction planétaire activée. Inconfort qui mobilise ce mois-ci. Concrètement : ajustements constants, tension créatrice. Cette friction force l'adaptation et la résolution.",
    ('Moon', 'default', 'trine'): "Aspect lunaire en trigone : harmonie fluide entre besoins émotionnels et fonction planétaire activée. Facilité naturelle ce mois-ci. Concrètement : synergie spontanée, talent à mobiliser. Attention à la passivité : cette aisance demande activation consciente.",
}

# Fallback global si aucun aspect lunaire
ASPECT_CLIMATE_NO_MOON_FALLBACK = "Période calibration émotionnelle sans aspect lunaire majeur. Besoins manifestés de manière autonome, sans amplification ni friction particulière. Mois stabilité émotionnelle relative, ajustements mensuels selon retour Lune."

# C. Filtres ascendant lunaire (30 mots chacun)
LUNAR_ASCENDANT_FILTERS: Dict[str, str] = {
    'Aries': "Ascendant lunaire en Bélier ce mois : filtre perceptif impulsif, direct et conquérant. Tu abordes les situations nouvelles par l'action immédiate et l'initiative personnelle spontanée. Présence affirmée et dynamique, parfois impatiente. Interface au monde : conquérante et guerrière.",
    'Taurus': "Ascendant lunaire en Taureau ce mois : filtre perceptif stable, sensoriel et ancré dans le concret. Tu abordes les situations par l'ancrage physique et la matérialité tangible. Présence posée et solide, parfois inerte. Interface au monde : constructrice et patiente.",
    'Gemini': "Ascendant lunaire en Gémeaux ce mois : filtre perceptif curieux, adaptable et intellectuellement mobile. Tu abordes les situations nouvelles par l'intellect agile et la communication spontanée. Présence légère et versatile, parfois dispersée. Interface au monde : communicante et adaptable.",
    'Cancer': "Ascendant lunaire en Cancer ce mois : filtre perceptif protecteur, émotionnel et maternel. Tu abordes les situations nouvelles par le ressenti profond et la recherche de sécurité affective. Présence enveloppante et nourricière, parfois défensive. Interface au monde : protectrice et sensible.",
    'Leo': "Ascendant lunaire en Lion ce mois : filtre perceptif rayonnant, créatif et généreux. Tu abordes les situations nouvelles par l'expression personnelle théâtrale et la générosité affichée. Présence magnétique et solaire, parfois théâtrale. Interface au monde : rayonnante et créative.",
    'Virgo': "Ascendant lunaire en Vierge ce mois : filtre perceptif analytique, serviciel et perfectionniste. Tu abordes les situations nouvelles par l'organisation méthodique et le perfectionnement constant. Présence efficace et précise, parfois critique. Interface au monde : raffinée et méthodique.",
    'Libra': "Ascendant lunaire en Balance ce mois : filtre perceptif harmonieux, relationnel et diplomatique. Tu abordes les situations nouvelles par la médiation élégante et la recherche esthétique constante. Présence diplomatique et charmante, parfois indécise. Interface au monde : équilibrante et harmonieuse.",
    'Scorpio': "Ascendant lunaire en Scorpion ce mois : filtre perceptif intense, transformateur et magnétique. Tu abordes les situations nouvelles par la profondeur investigatrice et le contrôle stratégique. Présence magnétique et pénétrante, parfois méfiante. Interface au monde : transformatrice et intense.",
    'Sagittarius': "Ascendant lunaire en Sagittaire ce mois : filtre perceptif expansif, optimiste et philosophique. Tu abordes les situations nouvelles par la quête aventureuse et la vision panoramique. Présence enthousiaste et généreuse, parfois excessive. Interface au monde : exploratrice et optimiste.",
    'Capricorn': "Ascendant lunaire en Capricorne ce mois : filtre perceptif structuré, ambitieux et pragmatique. Tu abordes les situations nouvelles par la responsabilité assumée et la discipline rigoureuse. Présence sérieuse et autoritaire, parfois rigide. Interface au monde : constructrice et ambitieuse.",
    'Aquarius': "Ascendant lunaire en Verseau ce mois : filtre perceptif innovant, détaché et original. Tu abordes les situations nouvelles par l'originalité assumée et l'indépendance intellectuelle affirmée. Présence singulière et avant-gardiste, parfois distante. Interface au monde : réformatrice et innovante.",
    'Pisces': "Ascendant lunaire en Poissons ce mois : filtre perceptif fluide, empathique et imaginatif. Tu abordes les situations nouvelles par l'imaginaire créateur et la compassion fusionnelle universelle. Présence poreuse et sensible, parfois confuse. Interface au monde : dissolvante et empathique.",
}

# Fallback si pas d'ascendant lunaire
LUNAR_ASCENDANT_NO_DATA_FALLBACK = "Filtre perceptif neutre ce mois-ci : approche directe des situations, sans coloration particulière de l'interface au monde. Présence non modifiée par ascendant lunaire."

# D-bis. Focus par maison lunaire (V5 - conseils concrets)
MOON_HOUSE_FOCUS: Dict[int, str] = {
    1: "Le focus du mois porte sur toi : ton image, ta façon de te présenter au monde. C'est le moment de prendre des initiatives personnelles.",
    2: "Le focus du mois porte sur tes ressources : finances, valeurs, ce qui compte vraiment pour toi. Bon moment pour stabiliser ta situation matérielle.",
    3: "Le focus du mois porte sur la communication : échanges, apprentissages, contacts avec ton entourage proche. Parle, écris, écoute.",
    4: "Le focus du mois porte sur ton foyer et ta famille. Besoin de te ressourcer chez toi, de renforcer tes racines. Prends soin de ton espace.",
    5: "Le focus du mois porte sur la créativité et le plaisir. Loisirs, romances, projets personnels : exprime-toi et amuse-toi.",
    6: "Le focus du mois porte sur ton quotidien : travail, santé, routines. C'est le moment d'optimiser, d'organiser, de prendre soin de toi au jour le jour.",
    7: "Le focus du mois porte sur tes relations : couple, partenariats, collaborations. L'autre est au centre de tes préoccupations.",
    8: "Le focus du mois porte sur les transformations profondes : finances partagées, intimité, ce qui doit changer. Période intense mais libératrice.",
    9: "Le focus du mois porte sur l'expansion : voyages, études, quête de sens. Élargis tes horizons et explore de nouvelles perspectives.",
    10: "Le focus du mois porte sur ta carrière et tes ambitions. Visibilité professionnelle, objectifs à long terme : c'est le moment de concrétiser.",
    11: "Le focus du mois porte sur tes projets collectifs : amis, réseaux, causes qui te tiennent à cœur. Implique-toi dans ce qui dépasse l'individuel.",
    12: "Le focus du mois porte sur l'intériorité : repos, introspection, spiritualité. Accorde-toi du temps pour toi, loin du bruit du monde.",
}

# D. Preview axes par maison lunaire (20 mots chacun) - version technique
AXES_PREVIEW_TEMPLATES: Dict[Any, str] = {
    1: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe identitaire et affirmation personnelle, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    2: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe matériel et système de valeurs, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    3: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe communication et apprentissages, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    4: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe foyer, racines et sécurité affective, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    5: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe créativité et expression de plaisir, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    6: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe quotidien, service et santé, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    7: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe relationnel et construction de partenariats, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    8: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe transformation profonde et intimité, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    9: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe expansion et quête philosophique, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    10: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe carrière et accomplissement social, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    11: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe collectif, projets de groupe et idéaux, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    12: "Ces dynamiques émotionnelles mensuelles se déploient prioritairement sur l'axe spiritualité et introspection profonde, avec extensions possibles vers les domaines de vie activés ci-dessous.",
    'default': "Ces dynamiques lunaires mensuelles se déploient progressivement sur les différents domaines de vie activés ce mois-ci, détaillés ci-dessous.",
}

# E. Contextes enrichis par maison (15w context + 10w manifestation)
HOUSE_ENRICHED_CONTEXTS: Dict[Tuple[str, int], Dict[str, str]] = {
    # Moon position contexts (12 maisons)
    ('moon_position', 1): {
        'context': "Lune en Maison 1 ce mois : besoins émotionnels projetés directement sur l'identité. Période redéfinition personnelle mensuelle, ajustement image de soi.",
        'manifestation': "Concrètement : besoin changement d'apparence, d'initiative personnelle, d'affirmation visible. Émotions lisibles sur le visage."
    },
    ('moon_position', 2): {
        'context': "Lune en Maison 2 ce mois : besoins émotionnels liés aux ressources matérielles. Sécurité affective passe par stabilité financière, acquisition de biens.",
        'manifestation': "Concrètement : dépenses émotionnelles, achats réconfortants, besoin de construire sécurité matérielle. Valeurs réexaminées."
    },
    ('moon_position', 3): {
        'context': "Lune en Maison 3 ce mois : besoins émotionnels satisfaits par communication et apprentissages. Sécurité passe par échanges, mobilité mentale.",
        'manifestation': "Concrètement : besoin de parler, d'apprendre, de bouger dans environnement proche. Contacts fraternels activés."
    },
    ('moon_position', 4): {
        'context': "Lune en Maison 4 ce mois : besoins émotionnels centrés sur foyer et famille. Sécurité affective passe par ancrage domestique, racines.",
        'manifestation': "Concrètement : besoin de rester chez toi, de nourrir liens familiaux, de transformer espace de vie. Introspection domestique."
    },
    ('moon_position', 5): {
        'context': "Lune en Maison 5 ce mois : besoins émotionnels satisfaits par créativité et plaisir. Sécurité affective passe par expression personnelle, jeu.",
        'manifestation': "Concrètement : besoin de créer, de jouer, de séduire, de prendre risques créatifs. Affection généreuse."
    },
    ('moon_position', 6): {
        'context': "Lune en Maison 6 ce mois : besoins émotionnels liés à routine et santé. Sécurité affective passe par organisation quotidien, service.",
        'manifestation': "Concrètement : besoin d'optimiser routine, de prendre soin du corps, de servir efficacement. Quotidien restructuré."
    },
    ('moon_position', 7): {
        'context': "Lune en Maison 7 ce mois : besoins émotionnels projetés sur relations et partenariats. Sécurité affective dépend de l'autre, miroir relationnel.",
        'manifestation': "Concrètement : besoin de l'autre pour te sentir complet, négociations affectives, contrats relationnels activés."
    },
    ('moon_position', 8): {
        'context': "Lune en Maison 8 ce mois : besoins émotionnels liés à transformation et intimité. Sécurité affective passe par fusion, gestion ressources partagées.",
        'manifestation': "Concrètement : besoin de profondeur fusionnelle, de contrôler l'intimité, de traverser crises régénératrices. Intensité émotionnelle."
    },
    ('moon_position', 9): {
        'context': "Lune en Maison 9 ce mois : besoins émotionnels satisfaits par expansion et quête de sens. Sécurité affective passe par aventure, philosophie.",
        'manifestation': "Concrètement : besoin de voyager, d'apprendre systèmes de pensée, de trouver sens émotionnel. Optimisme expansif."
    },
    ('moon_position', 10): {
        'context': "Lune en Maison 10 ce mois : besoins émotionnels liés à accomplissement et visibilité. Sécurité affective passe par reconnaissance professionnelle, statut.",
        'manifestation': "Concrètement : besoin de réussite visible, d'accomplissement public, de responsabilités assumées. Carrière émotionnellement investie."
    },
    ('moon_position', 11): {
        'context': "Lune en Maison 11 ce mois : besoins émotionnels satisfaits par projets collectifs et amitiés. Sécurité affective passe par appartenance groupale, idéaux.",
        'manifestation': "Concrètement : besoin de fédérer, de participer à causes collectives, d'amitiés nourrissantes. Solidarité émotionnelle."
    },
    ('moon_position', 12): {
        'context': "Lune en Maison 12 ce mois : besoins émotionnels satisfaits par solitude et introspection. Sécurité affective passe par retrait, dissolution frontières.",
        'manifestation': "Concrètement : besoin d'isolement choisi, de méditation, de compassion discrète. Émotions souterraines à explorer."
    },

    # Aspect activation contexts (12 maisons)
    ('aspect_activation', 1): {
        'context': "Maison 1 activée par aspect serré : identité et apparence sollicitées intensément. Initiatives personnelles amplifiées ou contrariées selon nature aspect.",
        'manifestation': "Concrètement : changements visibles identité, affirmation personnelle dynamisée, présence au monde modifiée ce mois-ci."
    },
    ('aspect_activation', 2): {
        'context': "Maison 2 activée par aspect serré : ressources et valeurs sollicitées intensément. Sécurité matérielle amplifiée ou questionnée selon nature aspect.",
        'manifestation': "Concrètement : mouvements financiers, réévaluation valeurs personnelles, acquisitions ou pertes matérielles ce mois-ci."
    },
    ('aspect_activation', 3): {
        'context': "Maison 3 activée par aspect serré : communication et apprentissages sollicités intensément. Échanges et mobilité amplifiés ou contrariés selon aspect.",
        'manifestation': "Concrètement : conversations importantes, déplacements fréquents, apprentissages accélérés ou difficultés communicationnelles ce mois-ci."
    },
    ('aspect_activation', 4): {
        'context': "Maison 4 activée par aspect serré : foyer et famille sollicités intensément. Racines et sécurité émotionnelle amplifiées ou questionnées selon aspect.",
        'manifestation': "Concrètement : transformations domestiques, dialogues familiaux importants, ancrage ou déracinement ce mois-ci."
    },
    ('aspect_activation', 5): {
        'context': "Maison 5 activée par aspect serré : créativité et plaisir sollicités intensément. Expression personnelle amplifiée ou contrariée selon nature aspect.",
        'manifestation': "Concrètement : projets créatifs dynamisés, romances activées, prises de risques ludiques ou blocages créatifs ce mois-ci."
    },
    ('aspect_activation', 6): {
        'context': "Maison 6 activée par aspect serré : quotidien et santé sollicités intensément. Organisation et service amplifiés ou perturbés selon nature aspect.",
        'manifestation': "Concrètement : réorganisation routine, ajustements santé, efficacité accrue ou surcharge travail ce mois-ci."
    },
    ('aspect_activation', 7): {
        'context': "Maison 7 activée par aspect serré : relations et partenariats sollicités intensément. Dynamique relationnelle amplifiée ou mise en tension selon aspect.",
        'manifestation': "Concrètement : négociations relationnelles majeures, contrats signés ou rompus, miroir de l'autre intensifié ce mois-ci."
    },
    ('aspect_activation', 8): {
        'context': "Maison 8 activée par aspect serré : transformation et intimité sollicitées intensément. Profondeur fusionnelle amplifiée ou mise en crise selon aspect.",
        'manifestation': "Concrètement : gestion ressources partagées, crises régénératrices, intensité fusionnelle ou ruptures profondes ce mois-ci."
    },
    ('aspect_activation', 9): {
        'context': "Maison 9 activée par aspect serré : expansion et philosophie sollicitées intensément. Quête de sens amplifiée ou questionnée selon nature aspect.",
        'manifestation': "Concrètement : voyages décisifs, études approfondies, révisions philosophiques ou sur-extension ce mois-ci."
    },
    ('aspect_activation', 10): {
        'context': "Maison 10 activée par aspect serré : carrière et accomplissement sollicités intensément. Visibilité sociale amplifiée ou mise en tension selon aspect.",
        'manifestation': "Concrètement : opportunités professionnelles majeures, responsabilités accrues, reconnaissance ou obstacles carrière ce mois-ci."
    },
    ('aspect_activation', 11): {
        'context': "Maison 11 activée par aspect serré : projets collectifs et amitiés sollicités intensément. Dimension groupale amplifiée ou questionnée selon aspect.",
        'manifestation': "Concrètement : nouveaux réseaux, causes collectives activées, collaborations ou conflits de groupe ce mois-ci."
    },
    ('aspect_activation', 12): {
        'context': "Maison 12 activée par aspect serré : spiritualité et introspection sollicitées intensément. Dimension souterraine amplifiée ou mise en lumière selon aspect.",
        'manifestation': "Concrètement : retraites nécessaires, révélations inconscientes, méditation approfondie ou confusions ce mois-ci."
    },
}

# F. Liens inter-axes (3-5 mots)
INTER_AXIS_LINKS: Dict[Tuple[int, int], str] = {
    (1, 2): "Dialectique identité-ressources",
    (1, 3): "Dialectique identité-communication",
    (1, 4): "Dialectique identité-racines",
    (1, 5): "Dialectique identité-créativité",
    (1, 6): "Dialectique identité-service",
    (1, 7): "Dialectique identité-partenariat",
    (1, 8): "Dialectique identité-transformation",
    (1, 9): "Dialectique identité-expansion",
    (1, 10): "Dialectique identité-accomplissement",
    (1, 11): "Dialectique identité-collectif",
    (1, 12): "Dialectique identité-spiritualité",
    (2, 3): "Dialectique ressources-communication",
    (2, 4): "Dialectique ressources-foyer",
    (2, 5): "Dialectique ressources-créativité",
    (2, 6): "Dialectique ressources-quotidien",
    (2, 7): "Dialectique ressources-partenariat",
    (2, 8): "Dialectique ressources-intimité",
    (3, 4): "Dialectique communication-foyer",
    (3, 9): "Dialectique communication-philosophie",
    (4, 10): "Dialectique foyer-carrière",
    (5, 11): "Dialectique créativité-collectif",
    (6, 12): "Dialectique service-spiritualité",
    (7, 8): "Dialectique partenariat-intimité",
    'default': "Interaction domaines activés",
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


# === HELPERS POUR CLIMAT ENRICHI ===

def _normalize_planet_name_for_climate(planet_name: str) -> str:
    """
    Normalise le nom de planète pour lookup dans ASPECT_CLIMATE_SNIPPETS

    Args:
        planet_name: Nom brut (ex: "Moon", "moon", "Lune", "Mars")

    Returns:
        Nom normalisé capitalisé (ex: "Moon", "Mars", "Sun")
    """
    normalized = planet_name.strip().lower().replace('_', ' ').replace('-', ' ')

    # Mapping variantes → noms standards
    mapping = {
        'sun': 'Sun', 'soleil': 'Sun',
        'moon': 'Moon', 'lune': 'Moon',
        'mercury': 'Mercury', 'mercure': 'Mercury',
        'venus': 'Venus', 'vénus': 'Venus',
        'mars': 'Mars',
        'jupiter': 'Jupiter',
        'saturn': 'Saturn', 'saturne': 'Saturn',
        'uranus': 'Uranus',
        'neptune': 'Neptune',
        'pluto': 'Pluto', 'pluton': 'Pluto',
        'ascendant': 'Ascendant',
        'midheaven': 'Midheaven', 'mc': 'Midheaven', 'medium coeli': 'Midheaven',
        'milieu du ciel': 'Midheaven',
        'north node': 'NorthNode', 'mean node': 'NorthNode', 'true node': 'NorthNode',
        'noeud nord': 'NorthNode', 'nœud nord': 'NorthNode',
        'south node': 'SouthNode', 'noeud sud': 'SouthNode', 'nœud sud': 'SouthNode',
        'chiron': 'Chiron'
    }

    return mapping.get(normalized, planet_name.capitalize())


def _get_top_aspect_for_climate(lunar_return: Any) -> Optional[str]:
    """
    Extrait l'aspect lunaire le plus serré pour highlight climat

    Filtre les aspects impliquant la Lune, trie par orbe croissant,
    et retourne un snippet de 40 mots décrivant l'aspect principal.

    Args:
        lunar_return: Objet LunarReturn de la DB

    Returns:
        Snippet 40 mots ou None si aucun aspect lunaire
    """
    aspects = lunar_return.aspects or []
    planets_data = lunar_return.planets or {}

    if not aspects:
        return None

    # 1. Filtrer aspects lunaires uniquement
    lunar_aspects = []
    for aspect in aspects:
        planet1 = aspect.get('planet1', '').lower()
        planet2 = aspect.get('planet2', '').lower()

        # Vérifier si Moon est impliquée
        if 'moon' in planet1 or 'lune' in planet1 or 'moon' in planet2 or 'lune' in planet2:
            lunar_aspects.append(aspect)

    if not lunar_aspects:
        return None

    # 2. Trier par orbe croissant (aspects les plus serrés en premier)
    lunar_aspects.sort(key=lambda a: abs(a.get('orb', 999)))

    # 3. Prendre le top aspect
    top_aspect = lunar_aspects[0]

    # 4. Formater snippet
    snippet = _format_aspect_climate_snippet(top_aspect, planets_data)

    return snippet


def _format_aspect_climate_snippet(aspect: Dict[str, Any], planets_data: Dict[str, Any]) -> str:
    """
    Génère snippet 40 mots décrivant aspect lunaire pour climat

    Lookup dans ASPECT_CLIMATE_SNIPPETS avec fallbacks progressifs :
    1. (Moon, planet, type) exact
    2. (Moon, default, type) generic
    3. Fallback ultime

    Args:
        aspect: Aspect brut (planet1, planet2, type, orb)
        planets_data: Dict des planètes avec positions

    Returns:
        Snippet 40 mots
    """
    planet1_raw = aspect.get('planet1', '')
    planet2_raw = aspect.get('planet2', '')
    aspect_type = aspect.get('type', '').lower()

    # Normaliser noms
    planet1 = _normalize_planet_name_for_climate(planet1_raw)
    planet2 = _normalize_planet_name_for_climate(planet2_raw)

    # Identifier quelle planète est la Lune et quelle est l'autre
    if planet1 == 'Moon':
        other_planet = planet2
    elif planet2 == 'Moon':
        other_planet = planet1
    else:
        # Pas d'aspect lunaire (ne devrait pas arriver)
        logger.warning(f"[LunarReportBuilder] Aspect non lunaire passé à _format_aspect_climate_snippet: {planet1}-{planet2}")
        other_planet = 'default'

    # Construire clé de lookup
    lookup_key = ('Moon', other_planet, aspect_type)

    # Lookup avec fallbacks
    if lookup_key in ASPECT_CLIMATE_SNIPPETS:
        snippet = ASPECT_CLIMATE_SNIPPETS[lookup_key]
    else:
        # Fallback 1: (Moon, default, type)
        fallback_key = ('Moon', 'default', aspect_type)
        if fallback_key in ASPECT_CLIMATE_SNIPPETS:
            snippet = ASPECT_CLIMATE_SNIPPETS[fallback_key]
        else:
            # Fallback ultime
            snippet = ASPECT_CLIMATE_NO_MOON_FALLBACK

    return snippet


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

    # 2. CLIMAT GÉNÉRAL (template enrichi v4.1)
    general_climate = _build_general_climate_enriched(lunar_return)

    # 3. AXES DOMINANTS (enrichis v4.1)
    dominant_axes = _build_dominant_axes_enriched(lunar_return)

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
    from dateutil.relativedelta import relativedelta

    end_date = return_date + relativedelta(months=1)

    # Mapping mois français
    MOIS_FR = {
        1: 'janvier', 2: 'février', 3: 'mars', 4: 'avril',
        5: 'mai', 6: 'juin', 7: 'juillet', 8: 'août',
        9: 'septembre', 10: 'octobre', 11: 'novembre', 12: 'décembre'
    }
    MOIS_FR_ABBR = {
        1: 'jan.', 2: 'fév.', 3: 'mars', 4: 'avr.',
        5: 'mai', 6: 'juin', 7: 'juil.', 8: 'août',
        9: 'sept.', 10: 'oct.', 11: 'nov.', 12: 'déc.'
    }

    # Format mois (ex: "Janvier 2025")
    month_name = f"{MOIS_FR[return_date.month].capitalize()} {return_date.year}"

    # Format dates (ex: "Du 15 jan. au 12 fév.")
    start_str = f"{return_date.day} {MOIS_FR_ABBR[return_date.month]}"
    end_str = f"{end_date.day} {MOIS_FR_ABBR[end_date.month]}"

    return {
        'month': month_name,
        'dates': f"Du {start_str} au {end_str}",
        'moon_sign': lunar_return.moon_sign or 'N/A',
        'moon_house': lunar_return.moon_house,
        'lunar_ascendant': lunar_return.lunar_ascendant or 'N/A'
    }


def _build_general_climate_enriched(lunar_return: Any) -> str:
    """
    Construit climat général V5 (ton accessible, ~50 mots)

    Structure simplifiée en 2 parties :
    1. Intro signe (MOON_SIGN_INTRO) : énergie émotionnelle du mois
    2. Focus maison (MOON_HOUSE_FOCUS) : domaine de vie prioritaire

    Returns: Texte accessible et concret
    """
    parts = []

    # 1. Intro par signe lunaire (énergie du mois)
    moon_sign = lunar_return.moon_sign
    intro = MOON_SIGN_INTRO.get(
        moon_sign,
        "Ce mois-ci, prends le temps d'observer tes besoins émotionnels et d'y répondre avec bienveillance."
    )
    parts.append(intro)

    # 2. Focus par maison lunaire (domaine prioritaire)
    moon_house = lunar_return.moon_house
    if moon_house:
        focus = MOON_HOUSE_FOCUS.get(
            moon_house,
            "Observe les domaines de ta vie qui demandent ton attention ce mois-ci."
        )
        parts.append(focus)

    return '\n\n'.join(parts)


def _build_dominant_axes_enriched(lunar_return: Any) -> List[str]:
    """
    Construit 2-3 axes dominants enrichis (100 mots total)

    Structure par axe (33w si 3 axes, 50w si 2 axes):
    - House name + domain (5w)
    - Monthly context (15w): HOUSE_ENRICHED_CONTEXTS[(type, house)]['context']
    - Concrete manifestation (10w): HOUSE_ENRICHED_CONTEXTS[(type, house)]['manifestation']
    - [Inter-axis link (3w)] optional

    Returns: Liste axes enrichis
    """
    axes = []

    # 1. Identify activated houses (keep existing logic)
    activated = []

    # Moon house (always first)
    if lunar_return.moon_house:
        activated.append(('moon_position', lunar_return.moon_house))

    # Aspect-activated houses (tight aspects orb ≤ 3)
    aspects = lunar_return.aspects or []
    planets_data = lunar_return.planets or {}

    tight_houses = set()
    for aspect in aspects:
        orb = abs(aspect.get('orb', 999))
        if orb <= 3:
            # Extract houses from planets in this aspect
            p1 = aspect.get('planet1', '').lower()
            p2 = aspect.get('planet2', '').lower()

            for planet_key, planet_data in planets_data.items():
                if isinstance(planet_data, dict):
                    planet_key_norm = planet_key.lower().replace('_', '').replace(' ', '').replace('-', '')
                    planet1_norm = p1.replace('_', '').replace(' ', '').replace('-', '')
                    planet2_norm = p2.replace('_', '').replace(' ', '').replace('-', '')

                    if planet_key_norm == planet1_norm or planet_key_norm == planet2_norm:
                        house = planet_data.get('house')
                        if house and house != lunar_return.moon_house:
                            tight_houses.add(house)

    # Add up to 2 aspect-activated houses
    for house in sorted(tight_houses)[:2]:
        activated.append(('aspect_activation', house))

    # Ensure 2-3 axes total
    if len(activated) < 2:
        activated.append(('default', None))

    activated = activated[:3]  # Max 3

    # 2. Build enriched descriptions
    for i, (context_type, house_num) in enumerate(activated):
        if house_num is None:
            # Fallback axis (50 mots pour cohérence)
            axes.append("Période centrée sur intégration principale et approfondie du cycle lunaire mensuel actuellement en cours, sans activation majeure ni dispersion sur axes secondaires ce mois-ci. Concrètement : focus unique et soutenu sur dynamique lunaire primaire, énergie concentrée et canalisée sur le domaine principal identifié ci-dessus. Mois d'approfondissement vertical plutôt que d'extension horizontale.")
            continue

        # House name + domain
        house_label = HOUSE_AXES.get(house_num, "Domaine de vie")
        axis_text = f"Maison {house_num} : {house_label}. "

        # Context + manifestation
        context_key = (context_type, house_num)
        template = HOUSE_ENRICHED_CONTEXTS.get(
            context_key,
            {
                'context': "Axe activé ce mois-ci.",
                'manifestation': "Concrètement : situations demandant attention dans ce domaine."
            }
        )

        axis_text += template['context'] + ' '
        axis_text += template['manifestation']

        axes.append(axis_text.strip())

    # 3. Add inter-axis link if 2-3 axes
    if len(axes) >= 2 and axes[-1] != axes[0]:  # Avoid adding link to fallback
        houses = [a[1] for a in activated if a[1] is not None]
        if len(houses) >= 2:
            link_key = tuple(sorted(houses[:2]))
            link = INTER_AXIS_LINKS.get(link_key, INTER_AXIS_LINKS.get('default', ''))
            if link:
                axes[-1] += f" {link}."

    return axes


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
