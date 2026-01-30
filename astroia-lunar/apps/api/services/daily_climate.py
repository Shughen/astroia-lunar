"""
Service pour générer le Daily Lunar Climate
- Combine position lunaire actuelle (sign + phase)
- Génère un insight déterministe basé sur (date + sign + phase)
- Cache 24h pour stabilité
"""

import logging
from typing import Dict, Any
from datetime import datetime, timezone, date
import hashlib

from services.moon_position import get_current_moon_position

logger = logging.getLogger(__name__)

# Cache global avec TTL basé sur la date
_CACHE: Dict[str, Any] = {
    "date": None,  # YYYY-MM-DD
    "data": None,
}

# Mapping déterministe: (sign, phase) -> insights templates
# Chaque combinaison a plusieurs variations pour enrichir
INSIGHT_TEMPLATES = {
    # Format: (sign, phase) -> list of insights
    # Chaque insight = {"title": str, "text": str, "keywords": [str]}

    # Aries insights
    ("Aries", "Nouvelle Lune"): [
        {
            "title": "Nouveau Départ Ardent",
            "text": "La Nouvelle Lune en Bélier marque un moment propice aux initiatives audacieuses. Ta énergie est à son pic pour démarrer de nouveaux projets avec courage et détermination.",
            "keywords": ["initiative", "courage", "action", "nouveau départ"]
        },
        {
            "title": "Étincelle d'Innovation",
            "text": "Cette phase lunaire amplifie ton désir de conquête. C'est le moment idéal pour oser sortir de ta zone de confort et embrasser le changement avec confiance.",
            "keywords": ["innovation", "audace", "conquête", "transformation"]
        },
    ],
    ("Aries", "Premier Croissant"): [
        {
            "title": "Momentum Croissant",
            "text": "L'énergie du Bélier s'intensifie progressivement. Tes projets prennent de l'ampleur — maintenez ton cap avec persévérance et confiance en tes capacités.",
            "keywords": ["croissance", "persévérance", "momentum", "confiance"]
        },
    ],
    ("Aries", "Premier Quartier"): [
        {
            "title": "Défi Constructif",
            "text": "Le Premier Quartier en Bélier t'invite à surmonter les obstacles avec détermination. Les défis actuels sont des opportunités de prouver ta force intérieure.",
            "keywords": ["défi", "détermination", "force", "dépassement"]
        },
    ],
    ("Aries", "Lune Gibbeuse"): [
        {
            "title": "Affinement Passionné",
            "text": "Tes efforts prennent forme. C'est le moment d'ajuster tes stratégies avec précision tout en gardant ta flamme créative intacte.",
            "keywords": ["affinement", "stratégie", "créativité", "perfectionnement"]
        },
    ],
    ("Aries", "Pleine Lune"): [
        {
            "title": "Culmination Éclatante",
            "text": "La Pleine Lune en Bélier révèle les fruits de ta audace. Célébrez tes victoires et reconnais la puissance de ta volonté manifeste.",
            "keywords": ["culmination", "victoire", "révélation", "accomplissement"]
        },
    ],
    ("Aries", "Lune Disseminante"): [
        {
            "title": "Partage de Sagesse",
            "text": "Transmettez ta expérience et ta force aux autres. Ton courage inspire ceux qui t'entourent — partagez tes apprentissages.",
            "keywords": ["partage", "inspiration", "transmission", "sagesse"]
        },
    ],
    ("Aries", "Dernier Quartier"): [
        {
            "title": "Libération Active",
            "text": "Laisse partir ce qui ne te sert plus avec courage. Cette phase t'aide à te défaire des anciens schémas pour faire place au renouveau.",
            "keywords": ["libération", "lâcher-prise", "renouveau", "transformation"]
        },
    ],
    ("Aries", "Dernier Croissant"): [
        {
            "title": "Repos du Guerrier",
            "text": "Avant le prochain cycle, accorde-toi une pause bien méritée. Rechargez ta énergie en préparation des nouvelles aventures à venir.",
            "keywords": ["repos", "régénération", "préparation", "introspection"]
        },
    ],

    # Taurus insights
    ("Taurus", "Nouvelle Lune"): [
        {
            "title": "Fondations Solides",
            "text": "La Nouvelle Lune en Taureau favorise la construction durable. Pose des bases stables pour tes projets matériels et relationnels avec patience et pragmatisme.",
            "keywords": ["stabilité", "construction", "patience", "fondations"]
        },
    ],
    ("Taurus", "Premier Croissant"): [
        {
            "title": "Croissance Graduelle",
            "text": "Comme la nature, tes projets croissent à leur rythme. Cultive-les avec soin et constance — la richesse se bâtit pas à pas.",
            "keywords": ["croissance", "constance", "cultivation", "patience"]
        },
    ],
    ("Taurus", "Premier Quartier"): [
        {
            "title": "Persévérance Fructueuse",
            "text": "Les obstacles matériels se présentent, mais ta ténacité fera la différence. Reste ancré dans tes valeurs et poursuivez ton chemin.",
            "keywords": ["persévérance", "ténacité", "valeurs", "ancrage"]
        },
    ],
    ("Taurus", "Lune Gibbeuse"): [
        {
            "title": "Raffinement Sensoriel",
            "text": "Perfectionnez tes créations avec attention aux détails. La beauté et la qualité sont à ta portée — prends le temps de soigner chaque aspect.",
            "keywords": ["raffinement", "qualité", "beauté", "attention"]
        },
    ],
    ("Taurus", "Pleine Lune"): [
        {
            "title": "Récolte Abondante",
            "text": "La Pleine Lune en Taureau révèle l'abondance que tu as cultivée. Célébrez la richesse matérielle et émotionnelle de ta vie.",
            "keywords": ["abondance", "récolte", "richesse", "gratitude"]
        },
    ],
    ("Taurus", "Lune Disseminante"): [
        {
            "title": "Générosité Terrestre",
            "text": "Partagez ta prospérité avec générosité. Ta stabilité peut devenir un refuge pour ceux qui en ont besoin.",
            "keywords": ["générosité", "partage", "stabilité", "soutien"]
        },
    ],
    ("Taurus", "Dernier Quartier"): [
        {
            "title": "Simplification Nécessaire",
            "text": "Allège-toi du superflu. Reviens à l'essentiel et libère-toi des possessions ou attachements qui te pèsent.",
            "keywords": ["simplification", "essentiel", "libération", "détachement"]
        },
    ],
    ("Taurus", "Dernier Croissant"): [
        {
            "title": "Repos Réparateur",
            "text": "Reconnecte-toi à la terre et à ton corps. Cette phase invite au repos profond et à la régénération de tes ressources intérieures.",
            "keywords": ["repos", "régénération", "ancrage", "reconnexion"]
        },
    ],

    # Gemini insights
    ("Gemini", "Nouvelle Lune"): [
        {
            "title": "Curiosité Éveillée",
            "text": "La Nouvelle Lune en Gémeaux stimule ta soif d'apprentissage. Explore de nouvelles idées, connecte-toi aux autres et laissez ton esprit vagabonder.",
            "keywords": ["curiosité", "apprentissage", "communication", "exploration"]
        },
    ],
    ("Gemini", "Premier Croissant"): [
        {
            "title": "Connexions Fécondes",
            "text": "Tes échanges se multiplient et s'enrichissent. Cultive les conversations stimulantes qui nourrissent ton intellect et élargissent ta perspective.",
            "keywords": ["connexion", "échange", "intellect", "dialogue"]
        },
    ],
    ("Gemini", "Premier Quartier"): [
        {
            "title": "Adaptation Agile",
            "text": "Face aux défis, ta flexibilité mentale est ton atout. Trouve des solutions créatives et adapte-toi avec légèreté aux circonstances.",
            "keywords": ["adaptation", "flexibilité", "créativité", "agilité"]
        },
    ],
    ("Gemini", "Lune Gibbeuse"): [
        {
            "title": "Synthèse Brillante",
            "text": "Rassemble les informations dispersées pour créer une vision cohérente. Ta capacité à faire des liens révèle des insights précieux.",
            "keywords": ["synthèse", "cohérence", "intelligence", "clarté"]
        },
    ],
    ("Gemini", "Pleine Lune"): [
        {
            "title": "Révélation Intellectuelle",
            "text": "La Pleine Lune en Gémeaux illumine ton esprit. Des vérités cachées émergent à travers les mots et les échanges — écoutez attentivement.",
            "keywords": ["révélation", "vérité", "lucidité", "compréhension"]
        },
    ],
    ("Gemini", "Lune Disseminante"): [
        {
            "title": "Transmission de Savoirs",
            "text": "Partagez tes connaissances avec générosité. Ton rôle de messager est valorisé — enseignez, écrivez, communiquez.",
            "keywords": ["transmission", "enseignement", "communication", "partage"]
        },
    ],
    ("Gemini", "Dernier Quartier"): [
        {
            "title": "Silence Régénérateur",
            "text": "Après tant d'échanges, le silence devient nécessaire. Laissez ton mental se reposer et libère-toi du bavardage intérieur.",
            "keywords": ["silence", "repos mental", "clarté", "libération"]
        },
    ],
    ("Gemini", "Dernier Croissant"): [
        {
            "title": "Introspection Ludique",
            "text": "Explore ton monde intérieur avec la même curiosité que tu portes au monde extérieur. Que révèlent tes pensées les plus profondes ?",
            "keywords": ["introspection", "curiosité", "profondeur", "réflexion"]
        },
    ],

    # Cancer insights
    ("Cancer", "Nouvelle Lune"): [
        {
            "title": "Nid Émotionnel",
            "text": "La Nouvelle Lune en Cancer t'invite à créer un sanctuaire intérieur. Honorez tes émotions et nourris ce qui te fait te sentir en sécurité.",
            "keywords": ["sécurité", "émotions", "foyer", "nurturing"]
        },
    ],
    ("Cancer", "Premier Croissant"): [
        {
            "title": "Racines Profondes",
            "text": "Tes fondations émotionnelles se renforcent. Cultivez tes liens familiaux et tes traditions — elles sont ta source de force.",
            "keywords": ["racines", "famille", "traditions", "fondations"]
        },
    ],
    ("Cancer", "Premier Quartier"): [
        {
            "title": "Protection Sage",
            "text": "Défendez tes frontières émotionnelles avec douceur mais fermeté. Ta sensibilité est un don, pas une faiblesse — protège-la.",
            "keywords": ["protection", "frontières", "sensibilité", "sagesse"]
        },
    ],
    ("Cancer", "Lune Gibbeuse"): [
        {
            "title": "Maturité Affective",
            "text": "Tes relations atteignent un niveau de profondeur et de compréhension mutuelle. Peaufinez tes liens avec empathie et authenticité.",
            "keywords": ["maturité", "profondeur", "empathie", "authenticité"]
        },
    ],
    ("Cancer", "Pleine Lune"): [
        {
            "title": "Marée Émotionnelle",
            "text": "La Pleine Lune en Cancer révèle l'intensité de tes sentiments. Accueille cette vague émotionnelle — elle porte des messages importants.",
            "keywords": ["émotions", "intensité", "révélation", "accueil"]
        },
    ],
    ("Cancer", "Lune Disseminante"): [
        {
            "title": "Soin Partagé",
            "text": "Ta capacité à prendre soin des autres brille. Offrez ton soutien émotionnel avec générosité tout en préservant ta propre énergie.",
            "keywords": ["soin", "soutien", "générosité", "équilibre"]
        },
    ],
    ("Cancer", "Dernier Quartier"): [
        {
            "title": "Libération Douce",
            "text": "Laisse partir les douleurs anciennes avec compassion. Le pardon — envers toi et les autres — ouvre la voie à la guérison.",
            "keywords": ["libération", "pardon", "guérison", "compassion"]
        },
    ],
    ("Cancer", "Dernier Croissant"): [
        {
            "title": "Cocon Intérieur",
            "text": "Retire-toi dans ton sanctuaire personnel. Cette phase appelle au repos émotionnel et à la reconnexion avec ta essence.",
            "keywords": ["repos", "sanctuaire", "reconnexion", "essence"]
        },
    ],

    # Leo insights
    ("Leo", "Nouvelle Lune"): [
        {
            "title": "Flamme Créative",
            "text": "La Nouvelle Lune en Lion allume ton feu intérieur. Ose briller, créer et exprimer ta unicité avec confiance et authenticité.",
            "keywords": ["créativité", "authenticité", "expression", "confiance"]
        },
    ],
    ("Leo", "Premier Croissant"): [
        {
            "title": "Éclat Grandissant",
            "text": "Ta lumière s'intensifie progressivement. Continue à cultiver ta singularité et à partager tes talents avec générosité.",
            "keywords": ["éclat", "talents", "générosité", "croissance"]
        },
    ],
    ("Leo", "Premier Quartier"): [
        {
            "title": "Courage Royal",
            "text": "Face aux obstacles, ta dignité naturelle te guide. Relève les défis avec noblesse et rappelle-toi de ta valeur intrinsèque.",
            "keywords": ["courage", "dignité", "valeur", "noblesse"]
        },
    ],
    ("Leo", "Lune Gibbeuse"): [
        {
            "title": "Perfectionnement Artistique",
            "text": "Peaufinez tes créations avec le soin d'un artisan. Chaque détail compte pour magnifier l'œuvre que tu es en train de manifester.",
            "keywords": ["perfectionnement", "art", "manifestation", "excellence"]
        },
    ],
    ("Leo", "Pleine Lune"): [
        {
            "title": "Apogée Solaire",
            "text": "La Pleine Lune en Lion couronne tes efforts créatifs. Célébrez ton rayonnement et la reconnaissance que tu mérites pleinement.",
            "keywords": ["apogée", "célébration", "rayonnement", "reconnaissance"]
        },
    ],
    ("Leo", "Lune Disseminante"): [
        {
            "title": "Inspiration Contagieuse",
            "text": "Ta lumière inspire les autres à embrasser leur propre grandeur. Continue à être un phare de créativité et d'encouragement.",
            "keywords": ["inspiration", "leadership", "encouragement", "lumière"]
        },
    ],
    ("Leo", "Dernier Quartier"): [
        {
            "title": "Humilité Dorée",
            "text": "Même les rois doivent se reposer. Libère-toi du besoin de toujours briller et accepte la beauté de la vulnérabilité.",
            "keywords": ["humilité", "repos", "vulnérabilité", "acceptation"]
        },
    ],
    ("Leo", "Dernier Croissant"): [
        {
            "title": "Retraite Majestueuse",
            "text": "Avant le nouveau cycle, retire-toi pour recharger ta flamme créative. Le repos n'est pas une faiblesse mais une force.",
            "keywords": ["retraite", "régénération", "force intérieure", "préparation"]
        },
    ],

    # Virgo insights
    ("Virgo", "Nouvelle Lune"): [
        {
            "title": "Perfection Pratique",
            "text": "La Nouvelle Lune en Vierge favorise l'organisation et le raffinement. Mets de l'ordre dans ta vie avec discernement et efficacité.",
            "keywords": ["organisation", "discernement", "efficacité", "raffinement"]
        },
    ],
    ("Virgo", "Premier Croissant"): [
        {
            "title": "Amélioration Continue",
            "text": "Chaque petit pas compte. Tes efforts méthodiques portent leurs fruits — continuez à perfectionner tes systèmes et routines.",
            "keywords": ["amélioration", "méthode", "progrès", "routine"]
        },
    ],
    ("Virgo", "Premier Quartier"): [
        {
            "title": "Analyse Constructive",
            "text": "Les obstacles révèlent les points à améliorer. Utilisez ton esprit analytique pour trouver des solutions pragmatiques et efficaces.",
            "keywords": ["analyse", "solutions", "pragmatisme", "amélioration"]
        },
    ],
    ("Virgo", "Lune Gibbeuse"): [
        {
            "title": "Excellence Humble",
            "text": "Ton attention aux détails atteint son sommet. Peaufinez ton travail avec humilité et fierté — la qualité parle d'elle-même.",
            "keywords": ["excellence", "détails", "qualité", "humilité"]
        },
    ],
    ("Virgo", "Pleine Lune"): [
        {
            "title": "Service Accompli",
            "text": "La Pleine Lune en Vierge révèle l'impact de ta utilité. Célébrez ta contribution et reconnais la valeur de ton service.",
            "keywords": ["service", "utilité", "contribution", "accomplissement"]
        },
    ],
    ("Virgo", "Lune Disseminante"): [
        {
            "title": "Transmission de Savoir-faire",
            "text": "Partagez tes compétences et ta expertise avec ceux qui cherchent à apprendre. Ta précision est un don précieux.",
            "keywords": ["transmission", "expertise", "enseignement", "précision"]
        },
    ],
    ("Virgo", "Dernier Quartier"): [
        {
            "title": "Lâcher le Contrôle",
            "text": "Acceptez que l'imperfection fasse partie de la vie. Libère-toi du besoin de tout maîtriser et accueillez le flux naturel.",
            "keywords": ["lâcher-prise", "acceptation", "imperfection", "fluidité"]
        },
    ],
    ("Virgo", "Dernier Croissant"): [
        {
            "title": "Purification Douce",
            "text": "Simplifiez et purifiez avant le renouveau. Cette phase invite au nettoyage physique, mental et émotionnel.",
            "keywords": ["purification", "simplification", "nettoyage", "renouveau"]
        },
    ],

    # Libra insights
    ("Libra", "Nouvelle Lune"): [
        {
            "title": "Harmonie Naissante",
            "text": "La Nouvelle Lune en Balance t'invite à cultiver l'équilibre. Créez de la beauté et de l'harmonie dans tes relations et ton environnement.",
            "keywords": ["harmonie", "équilibre", "beauté", "relations"]
        },
    ],
    ("Libra", "Premier Croissant"): [
        {
            "title": "Connexions Élégantes",
            "text": "Tes relations se développent avec grâce. Tissez des liens basés sur le respect mutuel et l'appréciation de la différence.",
            "keywords": ["connexions", "grâce", "respect", "appréciation"]
        },
    ],
    ("Libra", "Premier Quartier"): [
        {
            "title": "Justice Équilibrée",
            "text": "Des tensions relationnelles demandent de la diplomatie. Trouvez le juste milieu entre tes besoins et ceux des autres avec sagesse.",
            "keywords": ["justice", "diplomatie", "équilibre", "sagesse"]
        },
    ],
    ("Libra", "Lune Gibbeuse"): [
        {
            "title": "Raffinement Relationnel",
            "text": "Perfectionnez l'art de la relation. Chaque interaction est une opportunité de créer plus d'harmonie et de compréhension mutuelle.",
            "keywords": ["raffinement", "harmonie", "compréhension", "art"]
        },
    ],
    ("Libra", "Pleine Lune"): [
        {
            "title": "Miroir de l'Âme",
            "text": "La Pleine Lune en Balance révèle la vérité de tes relations. Ce que tu vois chez l'autre reflète une partie de toi-même.",
            "keywords": ["miroir", "vérité", "relations", "révélation"]
        },
    ],
    ("Libra", "Lune Disseminante"): [
        {
            "title": "Médiation Bienveillante",
            "text": "Ta capacité à créer des ponts entre les gens brille. Offrez ta perspective équilibrée pour résoudre les conflits avec grâce.",
            "keywords": ["médiation", "ponts", "paix", "équilibre"]
        },
    ],
    ("Libra", "Dernier Quartier"): [
        {
            "title": "Solitude Nécessaire",
            "text": "Après tant d'attention aux autres, retrouvez ton centre. La solitude temporaire restaure ton équilibre intérieur.",
            "keywords": ["solitude", "centre", "restauration", "intériorité"]
        },
    ],
    ("Libra", "Dernier Croissant"): [
        {
            "title": "Paix Intérieure",
            "text": "Cultivez l'harmonie en toi-même avant de la chercher à l'extérieur. Cette phase invite à la réconciliation avec tes propres paradoxes.",
            "keywords": ["paix", "harmonie intérieure", "réconciliation", "acceptation"]
        },
    ],

    # Scorpio insights
    ("Scorpio", "Nouvelle Lune"): [
        {
            "title": "Transformation Profonde",
            "text": "La Nouvelle Lune en Scorpion initie une métamorphose puissante. Plongez dans tes profondeurs et embrasse le pouvoir de la régénération.",
            "keywords": ["transformation", "profondeur", "régénération", "pouvoir"]
        },
    ],
    ("Scorpio", "Premier Croissant"): [
        {
            "title": "Intensité Croissante",
            "text": "Tes émotions et perceptions s'approfondissent. Explorez les vérités cachées avec courage et honnêteté radicale.",
            "keywords": ["intensité", "vérité", "courage", "profondeur"]
        },
    ],
    ("Scorpio", "Premier Quartier"): [
        {
            "title": "Confrontation Nécessaire",
            "text": "Les ombres demandent à être affrontées. Ta bravoure émotionnelle transforme les peurs en force authentique.",
            "keywords": ["confrontation", "ombres", "bravoure", "transformation"]
        },
    ],
    ("Scorpio", "Lune Gibbeuse"): [
        {
            "title": "Alchimie Intérieure",
            "text": "Le processus de transformation atteint son intensité maximale. Comme le phénix, tu renais de tes propres cendres.",
            "keywords": ["alchimie", "renaissance", "phénix", "intensité"]
        },
    ],
    ("Scorpio", "Pleine Lune"): [
        {
            "title": "Révélation des Mystères",
            "text": "La Pleine Lune en Scorpion dévoile ce qui était caché. Les secrets émergent — accueillez ces vérités avec maturité émotionnelle.",
            "keywords": ["révélation", "mystères", "secrets", "maturité"]
        },
    ],
    ("Scorpio", "Lune Disseminante"): [
        {
            "title": "Guérison Partagée",
            "text": "Ta capacité à transmuter la douleur en sagesse aide les autres. Partagez ta force issue des épreuves traversées.",
            "keywords": ["guérison", "sagesse", "transmutation", "force"]
        },
    ],
    ("Scorpio", "Dernier Quartier"): [
        {
            "title": "Mort Symbolique",
            "text": "Laissez mourir ce qui doit partir. Cette libération profonde fait place à la renaissance — accepte la fin comme un nouveau commencement.",
            "keywords": ["libération", "mort symbolique", "renaissance", "acceptation"]
        },
    ],
    ("Scorpio", "Dernier Croissant"): [
        {
            "title": "Gestation Sacrée",
            "text": "Dans le silence et l'obscurité, quelque chose de puissant se prépare. Honorez cette phase de gestation intérieure.",
            "keywords": ["gestation", "silence", "préparation", "sacré"]
        },
    ],

    # Sagittarius insights
    ("Sagittarius", "Nouvelle Lune"): [
        {
            "title": "Horizon Infini",
            "text": "La Nouvelle Lune en Sagittaire élargit ta vision. Osez explorer de nouveaux territoires physiques, mentaux et spirituels.",
            "keywords": ["exploration", "vision", "expansion", "aventure"]
        },
    ],
    ("Sagittarius", "Premier Croissant"): [
        {
            "title": "Quête de Sens",
            "text": "Ta soif de compréhension grandit. Suivez ton curiosité philosophique et laissez-te guider par la quête de vérité.",
            "keywords": ["quête", "sens", "philosophie", "vérité"]
        },
    ],
    ("Sagittarius", "Premier Quartier"): [
        {
            "title": "Optimisme Éprouvé",
            "text": "Les défis testent ton foi, mais ton optimisme naturel trouve des opportunités là où d'autres voient des obstacles.",
            "keywords": ["optimisme", "foi", "opportunités", "résilience"]
        },
    ],
    ("Sagittarius", "Lune Gibbeuse"): [
        {
            "title": "Sagesse Grandissante",
            "text": "Tes explorations portent leurs fruits. Intègre les leçons apprises et affinez ton compréhension du grand tableau.",
            "keywords": ["sagesse", "intégration", "compréhension", "vision"]
        },
    ],
    ("Sagittarius", "Pleine Lune"): [
        {
            "title": "Illumination Joyeuse",
            "text": "La Pleine Lune en Sagittaire révèle le sens profond de ton parcours. Célébrez la sagesse acquise avec gratitude et enthousiasme.",
            "keywords": ["illumination", "sens", "gratitude", "joie"]
        },
    ],
    ("Sagittarius", "Lune Disseminante"): [
        {
            "title": "Enseignement Inspirant",
            "text": "Partagez ton philosophie et ta vision avec générosité. Ton enthousiasme allume des flammes d'inspiration chez les autres.",
            "keywords": ["enseignement", "inspiration", "partage", "enthousiasme"]
        },
    ],
    ("Sagittarius", "Dernier Quartier"): [
        {
            "title": "Libération des Dogmes",
            "text": "Laisse partir les croyances rigides qui limitent ton expansion. La vraie sagesse embrasse le mystère et l'inconnu.",
            "keywords": ["libération", "croyances", "mystère", "ouverture"]
        },
    ],
    ("Sagittarius", "Dernier Croissant"): [
        {
            "title": "Préparation Nomade",
            "text": "Avant la prochaine aventure, prends le temps de te recentrer. Le voyageur sage sait quand se reposer.",
            "keywords": ["préparation", "repos", "recentrage", "sagesse"]
        },
    ],

    # Capricorn insights
    ("Capricorn", "Nouvelle Lune"): [
        {
            "title": "Ambition Structurée",
            "text": "La Nouvelle Lune en Capricorne t'invite à bâtir durablement. Définissez tes objectifs à long terme avec pragmatisme et détermination.",
            "keywords": ["ambition", "structure", "objectifs", "détermination"]
        },
    ],
    ("Capricorn", "Premier Croissant"): [
        {
            "title": "Ascension Méthodique",
            "text": "Grimpe ta montagne pas à pas. Chaque effort discipliné te rapproche du sommet — la patience est ton alliée.",
            "keywords": ["ascension", "discipline", "patience", "méthode"]
        },
    ],
    ("Capricorn", "Premier Quartier"): [
        {
            "title": "Responsabilité Mature",
            "text": "Les défis révèlent ta capacité à assumer tes responsabilités. Ta maturité et ton endurance font la différence.",
            "keywords": ["responsabilité", "maturité", "endurance", "force"]
        },
    ],
    ("Capricorn", "Lune Gibbeuse"): [
        {
            "title": "Excellence Professionnelle",
            "text": "Ton travail acharné porte ses fruits. Peaufine tes réalisations avec le professionnalisme qui te caractérise.",
            "keywords": ["excellence", "professionnalisme", "réalisation", "qualité"]
        },
    ],
    ("Capricorn", "Pleine Lune"): [
        {
            "title": "Sommet Atteint",
            "text": "La Pleine Lune en Capricorne couronne tes efforts. Contemplez le chemin parcouru et célébrez ton réussite méritée.",
            "keywords": ["sommet", "réussite", "accomplissement", "contemplation"]
        },
    ],
    ("Capricorn", "Lune Disseminante"): [
        {
            "title": "Mentorat Sage",
            "text": "Ta expérience et ta sagesse guident les plus jeunes. Partagez tes leçons de vie avec générosité et humilité.",
            "keywords": ["mentorat", "sagesse", "expérience", "guidance"]
        },
    ],
    ("Capricorn", "Dernier Quartier"): [
        {
            "title": "Libération du Fardeau",
            "text": "Même les épaules les plus fortes méritent du répit. Déposez les responsabilités inutiles et allégez ton charge.",
            "keywords": ["libération", "répit", "allègement", "repos"]
        },
    ],
    ("Capricorn", "Dernier Croissant"): [
        {
            "title": "Repos de l'Architecte",
            "text": "Avant de construire à nouveau, rechargez ta énergie. La solitude restauratrice prépare tes prochaines créations.",
            "keywords": ["repos", "restauration", "préparation", "solitude"]
        },
    ],

    # Aquarius insights
    ("Aquarius", "Nouvelle Lune"): [
        {
            "title": "Vision Innovante",
            "text": "La Nouvelle Lune en Verseau libère ton génie créatif. Osez penser différemment et imaginer des futurs alternatifs audacieux.",
            "keywords": ["innovation", "vision", "créativité", "futur"]
        },
    ],
    ("Aquarius", "Premier Croissant"): [
        {
            "title": "Communauté Éveillée",
            "text": "Tes idées progressistes trouvent écho dans ta tribu. Connecte-toi à ceux qui partagent ta vision d'un monde meilleur.",
            "keywords": ["communauté", "progressisme", "connexion", "vision"]
        },
    ],
    ("Aquarius", "Premier Quartier"): [
        {
            "title": "Rébellion Constructive",
            "text": "Face aux résistances, ton originalité devient une force révolutionnaire. Défiez le statu quo avec intelligence et compassion.",
            "keywords": ["rébellion", "originalité", "révolution", "intelligence"]
        },
    ],
    ("Aquarius", "Lune Gibbeuse"): [
        {
            "title": "Perfection Technologique",
            "text": "Affinez tes systèmes et innovations. Ton approche rationnelle crée des solutions élégantes aux problèmes complexes.",
            "keywords": ["technologie", "systèmes", "solutions", "élégance"]
        },
    ],
    ("Aquarius", "Pleine Lune"): [
        {
            "title": "Révélation Collective",
            "text": "La Pleine Lune en Verseau illumine la conscience collective. Tes intuitions visionnaires révèlent des vérités universelles.",
            "keywords": ["révélation", "collectif", "intuition", "universel"]
        },
    ],
    ("Aquarius", "Lune Disseminante"): [
        {
            "title": "Activation du Réseau",
            "text": "Partagez tes découvertes avec la communauté. Ta capacité à connecter les esprits catalyse le changement collectif.",
            "keywords": ["réseau", "partage", "connexion", "changement"]
        },
    ],
    ("Aquarius", "Dernier Quartier"): [
        {
            "title": "Libération du Système",
            "text": "Détache-toi des structures mentales rigides. L'innovation véritable naît de la liberté de penser au-delà des limites.",
            "keywords": ["libération", "liberté", "innovation", "détachement"]
        },
    ],
    ("Aquarius", "Dernier Croissant"): [
        {
            "title": "Repos du Visionnaire",
            "text": "Même les esprits les plus brillants ont besoin de silence. Rechargez ton génie créatif dans la solitude réflexive.",
            "keywords": ["repos", "silence", "réflexion", "recharge"]
        },
    ],

    # Pisces insights
    ("Pisces", "Nouvelle Lune"): [
        {
            "title": "Océan de Possibles",
            "text": "La Nouvelle Lune en Poissons dissout les frontières. Plongez dans ton imagination et laissez l'intuition guider ton chemin.",
            "keywords": ["imagination", "intuition", "possibilités", "fluidité"]
        },
    ],
    ("Pisces", "Premier Croissant"): [
        {
            "title": "Connexion Spirituelle",
            "text": "Ta sensibilité spirituelle s'approfondit. Cultivez ton lien avec le sacré à travers la méditation, l'art ou la nature.",
            "keywords": ["spiritualité", "connexion", "sacré", "sensibilité"]
        },
    ],
    ("Pisces", "Premier Quartier"): [
        {
            "title": "Compassion en Action",
            "text": "Les défis révèlent ta capacité d'empathie profonde. Ta compassion devient une force de guérison pour toi et les autres.",
            "keywords": ["compassion", "empathie", "guérison", "force"]
        },
    ],
    ("Pisces", "Lune Gibbeuse"): [
        {
            "title": "Raffinement Artistique",
            "text": "Ta créativité atteint des sommets subtils. Chaque œuvre est imprégnée d'une qualité éthérée et transcendante.",
            "keywords": ["créativité", "art", "subtilité", "transcendance"]
        },
    ],
    ("Pisces", "Pleine Lune"): [
        {
            "title": "Révélation Mystique",
            "text": "La Pleine Lune en Poissons ouvre les portes du mystère. Les rêves et les visions portent des messages importants — écoutez-les.",
            "keywords": ["mystère", "rêves", "visions", "révélation"]
        },
    ],
    ("Pisces", "Lune Disseminante"): [
        {
            "title": "Guérison Universelle",
            "text": "Ton énergie curative rayonne au-delà de toi. Partage ton don de compassion et d'acceptation inconditionnelle.",
            "keywords": ["guérison", "compassion", "acceptation", "don"]
        },
    ],
    ("Pisces", "Dernier Quartier"): [
        {
            "title": "Dissolution Sacrée",
            "text": "Laisse partir les illusions et les attachements qui te retiennent. Dans le lâcher-prise total, tu trouves la liberté véritable.",
            "keywords": ["dissolution", "lâcher-prise", "liberté", "illusions"]
        },
    ],
    ("Pisces", "Dernier Croissant"): [
        {
            "title": "Méditation Profonde",
            "text": "Avant la renaissance, plongez dans le silence intérieur. Cette phase invite à la fusion avec le tout et à l'acceptation du vide.",
            "keywords": ["méditation", "silence", "fusion", "acceptation"]
        },
    ],
}


def _get_deterministic_insight(date_str: str, sign: str, phase: str) -> Dict[str, Any]:
    """
    Génère un insight déterministe basé sur (date, sign, phase)

    Logique:
    - Cherche dans INSIGHT_TEMPLATES[(sign, phase)]
    - Si plusieurs insights disponibles, utilise hash(date) pour choisir
    - Garantit que le même jour + sign + phase = même insight
    """
    key = (sign, phase)

    # Fallback si combinaison non trouvée (ne devrait pas arriver)
    if key not in INSIGHT_TEMPLATES:
        logger.warning(f"No insight template for {key}, using generic fallback")
        return {
            "title": f"Lune en {sign}",
            "text": f"La Lune traverse le signe du {sign} en phase {phase}. C'est un moment propice pour se connecter aux énergies de ce signe.",
            "keywords": ["lune", sign.lower(), "astrologie", "conscience"],
        }

    templates = INSIGHT_TEMPLATES[key]

    # Si un seul template, le retourner directement
    if len(templates) == 1:
        return templates[0]

    # Si plusieurs templates, utiliser hash(date) pour choisir de manière déterministe
    # Hash la date pour obtenir un index stable
    hash_value = int(hashlib.md5(date_str.encode()).hexdigest(), 16)
    index = hash_value % len(templates)

    return templates[index]


def get_daily_climate() -> Dict[str, Any]:
    """
    Récupère le Daily Lunar Climate avec cache 24h

    Returns:
        {
            "date": "YYYY-MM-DD",
            "moon": {"sign": str, "degree": float, "phase": str},
            "insight": {
                "title": str,
                "text": str,
                "keywords": [str],
                "version": "v1"
            }
        }
    """
    global _CACHE

    # Date actuelle (UTC) au format YYYY-MM-DD
    current_date = date.today().isoformat()

    # Vérifier le cache
    if _CACHE["date"] == current_date and _CACHE["data"] is not None:
        logger.info(f"[DailyClimate] ✅ Cache hit (date: {current_date})")
        return _CACHE["data"]

    # Cache miss ou nouvelle date
    logger.info(f"[DailyClimate] 🔄 Cache miss, génération insight (date: {current_date})")

    # Récupérer position lunaire actuelle (avec son propre cache 5min)
    moon_position = get_current_moon_position()

    # Générer insight déterministe
    insight = _get_deterministic_insight(
        current_date,
        moon_position["sign"],
        moon_position["phase"]
    )

    # Ajouter version à l'insight
    insight_with_version = {
        **insight,
        "version": "v1"
    }

    # Construire réponse complète
    result = {
        "date": current_date,
        "moon": moon_position,
        "insight": insight_with_version
    }

    # Mettre en cache
    _CACHE["date"] = current_date
    _CACHE["data"] = result

    logger.info(f"[DailyClimate] 💾 Cache mis à jour (date: {current_date}, insight: {insight['title']})")

    return result


def clear_cache():
    """Efface le cache (utile pour les tests)"""
    global _CACHE
    _CACHE["date"] = None
    _CACHE["data"] = None
    logger.info("[DailyClimate] 🗑️ Cache effacé")
