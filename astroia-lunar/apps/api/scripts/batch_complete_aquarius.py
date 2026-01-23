"""Batch complet: Aquarius - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # ==================== MAISON 1 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Pionnier rebelle**

Ta Lune en Verseau en Maison 1 te pousse à te redéfinir, à affirmer ton unicité, ta différence. L'Ascendant Bélier ajoute l'impulsion de l'action : tu ne veux pas juste être différent·e, tu veux le montrer maintenant, briser les codes, agir.

**Domaine activé** : Maison 1 — Ton identité personnelle est en transformation. Tu cherches à t'émanciper des attentes, à t'affirmer dans ton individualité. Ton image devient un terrain d'expérimentation.

**Ton approche instinctive** : Tu fonces vers l'inconventionnel. Face à la norme, ton réflexe est de prendre le contre-pied, d'innover. Cette audace attire l'attention mais peut aussi déstabiliser ton entourage.

**Tensions possibles** : Le risque de te rebeller sans but clair, juste pour affirmer ta différence. L'impatience peut te faire rejeter des connexions qui auraient du sens.

**Conseil clé** : Canaliser ta vision novatrice vers un projet personnel qui incarne vraiment tes valeurs, pas juste ta rébellion.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te rend vraiment unique et assume-le pleinement.",
            'week_2': "Expérimente une nouvelle façon de te présenter au monde.",
            'week_3': "Connecte avec des personnes qui partagent ta vision originale.",
            'week_4': "Célèbre ta singularité. Laisse ton authenticité briller."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Révolution stable**

Ta Lune en Verseau veut transformer ton identité, briser les conventions. Ton Ascendant Taureau cherche la stabilité, le concret. Tu veux changer le monde, mais à ton rythme, de manière durable.

**Domaine activé** : Maison 1 — Ta personnalité cherche à s'exprimer différemment tout en gardant des racines solides. Tu veux être toi-même sans perdre ta sécurité intérieure.

**Ton approche instinctive** : Le Taureau tempère ton idéalisme verseau : tu préfères des changements progressifs, ancrés dans la réalité. Tu as besoin de sentir que tes innovations ont du sens pratique.

**Tensions possibles** : La frustration entre ton besoin de liberté et ton besoin de sécurité. Tu peux te sentir coincé·e entre tradition et innovation.

**Conseil clé** : Introduire des changements progressifs mais constants dans ta vie, sans tout bouleverser d'un coup.""",
        'weekly_advice': {
            'week_1': "Repère un aspect de ton identité que tu veux faire évoluer.",
            'week_2': "Fais un petit pas concret vers ce changement.",
            'week_3': "Ancre cette nouveauté dans ta routine quotidienne.",
            'week_4': "Apprécie le chemin parcouru. La transformation est en cours."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Esprit libre**

Double air : ta Lune en Verseau et ton Ascendant Gémeaux te donnent une liberté mentale exceptionnelle. Tu peux explorer ton identité de mille façons, sans te figer dans une seule version de toi-même.

**Domaine activé** : Maison 1 — Ton identité devient un terrain de curiosité infinie. Tu veux expérimenter différentes facettes de ta personnalité, sans te limiter à une seule image.

**Ton approche instinctive** : Tu communiques tes idées originales avec aisance. Ta spontanéité intellectuelle te rend fascinant·e mais peut aussi te disperser.

**Tensions possibles** : Le risque de papillonner sans jamais approfondir. Tu peux donner l'impression d'être insaisissable, de ne jamais te poser.

**Conseil clé** : Choisir une ou deux directions pour ta singularité ce mois-ci, plutôt que de tout explorer en surface.""",
        'weekly_advice': {
            'week_1': "Exprime une idée originale qui te tient à cœur.",
            'week_2': "Engage une conversation qui challenge les conventions.",
            'week_3': "Partage tes découvertes avec une communauté alignée.",
            'week_4': "Synthétise ce que tu as appris sur toi-même ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Humaniste sensible**

Ta Lune en Verseau te pousse vers l'universel, le collectif, la vision d'ensemble. Ton Ascendant Cancer te ramène à l'émotionnel, à l'intime. Tu veux transformer le monde en restant connecté·e aux émotions humaines.

**Domaine activé** : Maison 1 — Ton identité oscille entre détachement intellectuel et sensibilité profonde. Tu cherches à être toi-même tout en prenant soin des autres.

**Ton approche instinctive** : Tu ressens les injustices émotionnellement mais tu les analyses avec recul. Cette combinaison te donne une empathie lucide.

**Tensions possibles** : Le conflit entre ton besoin d'indépendance (Verseau) et ton besoin de sécurité émotionnelle (Cancer). Tu peux te sentir déchiré·e.

**Conseil clé** : Honorer à la fois ton besoin de liberté et ton besoin de connexion émotionnelle sans en sacrifier un.""",
        'weekly_advice': {
            'week_1': "Identifie une cause humanitaire qui te touche personnellement.",
            'week_2': "Engage-toi émotionnellement sans perdre ta perspective globale.",
            'week_3': "Crée un espace sûr pour exprimer ta singularité.",
            'week_4': "Reconnais que sensibilité et originalité peuvent coexister."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Éclat unique**

Opposition air-feu : ta Lune en Verseau veut se fondre dans le collectif, ton Ascendant Lion veut briller individuellement. Tu cherches à être remarquable tout en servant une vision plus grande que toi.

**Domaine activé** : Maison 1 — Ton identité personnelle est tiraillée entre ego et altruisme. Tu veux être célébré·e pour ta contribution au collectif.

**Ton approche instinctive** : Tu as le charisme pour porter des idées avant-gardistes. Les gens te suivent parce que tu incarnes une vision inspirante avec confiance.

**Tensions possibles** : Le risque de te perdre entre besoin de reconnaissance et désir de servir. Tu peux alterner entre égocentrisme et détachement.

**Conseil clé** : Utiliser ta visibilité pour mettre en lumière des causes qui te dépassent, pas juste ton image.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton unicité peut servir un projet collectif.",
            'week_2': "Prends de la place pour défendre tes idées novatrices.",
            'week_3': "Accepte les compliments sans perdre ton humilité.",
            'week_4': "Célèbre ton rôle dans quelque chose de plus grand."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Innovation pratique**

Ta Lune en Verseau apporte des idées visionnaires, ton Ascendant Vierge les rend applicables. Tu veux changer le monde de manière concrète, méthodique, utile.

**Domaine activé** : Maison 1 — Ton identité se construit autour de l'amélioration systématique. Tu veux être reconnu·e pour ton intelligence pratique et ton originalité fonctionnelle.

**Ton approche instinctive** : Tu analyses les dysfonctionnements avec détachement puis tu proposes des solutions innovantes. Ton approche est à la fois rationnelle et avant-gardiste.

**Tensions possibles** : Le risque de te perdre dans les détails et de perdre la vision d'ensemble. Ou à l'inverse, d'avoir des idées trop abstraites pour être applicables.

**Conseil clé** : Trouver l'équilibre entre vision idéaliste et exécution pragmatique.""",
        'weekly_advice': {
            'week_1': "Identifie un problème quotidien que tu peux résoudre différemment.",
            'week_2': "Crée un système pratique pour une idée novatrice.",
            'week_3': "Teste ton approche, ajuste selon les résultats.",
            'week_4': "Documente ce qui fonctionne pour le partager."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie rebelle**

Double air : ta Lune en Verseau et ton Ascendant Balance te donnent une intelligence sociale exceptionnelle. Tu veux transformer les relations humaines, créer de nouvelles formes de connexion.

**Domaine activé** : Maison 1 — Ton identité se définit à travers tes relations. Tu cherches à être toi-même tout en créant des ponts entre les gens.

**Ton approche instinctive** : Tu sais négocier entre l'individuel et le collectif. Ton charme naturel te permet d'introduire des idées radicales sans brusquer.

**Tensions possibles** : Le risque de te perdre dans le compromis et de diluer ta singularité. Ou à l'inverse, de sacrifier l'harmonie pour ton indépendance.

**Conseil clé** : Affirmer ta différence tout en maintenant la qualité de tes connexions.""",
        'weekly_advice': {
            'week_1': "Exprime une opinion non-conventionnelle avec diplomatie.",
            'week_2': "Crée un espace de dialogue autour d'idées novatrices.",
            'week_3': "Trouve l'équilibre entre authenticité et harmonie.",
            'week_4': "Célèbre les connexions que tu as enrichies."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Profondeur radicale**

Ta Lune en Verseau cherche le détachement intellectuel, ton Ascendant Scorpion plonge dans l'intensité émotionnelle. Tu veux transformer le monde en allant au fond des choses.

**Domaine activé** : Maison 1 — Ton identité oscille entre distance et intimité. Tu cherches à te comprendre en profondeur tout en gardant ta liberté.

**Ton approche instinctive** : Tu perces les façades avec ton regard pénétrant et tu proposes des visions radicales. Cette intensité peut fasciner ou effrayer.

**Tensions possibles** : Le conflit entre ton besoin de contrôle émotionnel (Scorpion) et ton besoin d'indépendance totale (Verseau). Tu peux te sentir tiraillé·e.

**Conseil clé** : Utiliser ton intensité pour défendre tes convictions sans t'y perdre émotionnellement.""",
        'weekly_advice': {
            'week_1': "Explore une vérité inconfortable sur toi-même.",
            'week_2': "Transforme cette prise de conscience en force.",
            'week_3': "Partage ta vision radicale avec authenticité.",
            'week_4': "Accepte que ta profondeur puisse déstabiliser."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Visionnaire libre**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent une soif de liberté et d'exploration sans limites. Tu veux comprendre le monde et le transformer à travers tes découvertes.

**Domaine activé** : Maison 1 — Ton identité se construit autour de ta quête de sens et de ta vision du futur. Tu cherches à être un·e éclaireur·se, un·e pionnier·ère.

**Ton approche instinctive** : Tu explores les idées avec enthousiasme et tu partages tes découvertes sans filtre. Ton optimisme radical inspire mais peut aussi sembler naïf.

**Tensions possibles** : Le risque de te disperser dans trop de directions sans jamais ancrer tes idéaux dans la réalité.

**Conseil clé** : Choisir une vision et t'y engager pleinement ce mois-ci, même si d'autres horizons t'appellent.""",
        'weekly_advice': {
            'week_1': "Définis ta vision idéale pour toi-même et le monde.",
            'week_2': "Explore une philosophie ou idée qui élargit ta perspective.",
            'week_3': "Partage tes découvertes avec générosité.",
            'week_4': "Célèbre la liberté que tu incarnes."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Révolution structurée**

Ta Lune en Verseau veut bouleverser l'ordre établi, ton Ascendant Capricorne veut construire des structures durables. Tu veux innover tout en restant pragmatique.

**Domaine activé** : Maison 1 — Ton identité se forge entre tradition et innovation. Tu cherches à te positionner comme quelqu'un de fiable mais avant-gardiste.

**Ton approche instinctive** : Tu introduis des changements avec méthodologie. Ton sérieux donne de la crédibilité à tes idées novatrices.

**Tensions possibles** : Le conflit entre ton désir de liberté et ton besoin de contrôle. Tu peux te sentir prisonnier·ère de tes propres structures.

**Conseil clé** : Utiliser ta discipline pour construire une nouvelle version de toi-même, pas pour te limiter.""",
        'weekly_advice': {
            'week_1': "Identifie une structure limitante que tu veux transformer.",
            'week_2': "Crée un plan concret pour cette transformation.",
            'week_3': "Avance pas à pas avec constance.",
            'week_4': "Reconnais que la vraie liberté se construit."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolution pure**

Double Verseau : tu es l'incarnation de l'originalité, de l'indépendance, de la vision d'avenir. Ce mois-ci, ton identité est en pleine émancipation. Tu ne veux plus jouer aucun rôle qui ne soit pas authentiquement toi.

**Domaine activé** : Maison 1 — Ton identité personnelle est au cœur de tout. Tu cherches à te libérer complètement des attentes extérieures et à affirmer ta singularité radicale.

**Ton approche instinctive** : Tu te détaches naturellement des normes. Face aux conventions, ton réflexe est de chercher l'alternative, la vision différente. Cette authenticité attire des personnes alignées.

**Tensions possibles** : Le risque de l'isolement. À force de te démarquer, tu peux te retrouver seul·e. Le détachement émotionnel peut créer une distance avec les autres.

**Conseil clé** : Assumer pleinement ton originalité tout en restant ouvert·e aux connexions authentiques.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te rend vraiment unique et embrasse-le.",
            'week_2': "Libère-toi d'une attente ou norme qui ne te correspond plus.",
            'week_3': "Connecte avec une communauté qui célèbre ta différence.",
            'week_4': "Célèbre ton authenticité. Tu es exactement où tu dois être."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Rêveur universel**

Ta Lune en Verseau te donne une vision humaniste, ton Ascendant Poissons ajoute une sensibilité intuitive. Tu veux sauver le monde en te connectant à l'invisible, au transcendant.

**Domaine activé** : Maison 1 — Ton identité oscille entre détachement intellectuel et empathie universelle. Tu cherches à être toi-même tout en te dissolvant dans le tout.

**Ton approche instinctive** : Tu captes les courants subtils, les besoins collectifs non exprimés. Ton intuition te guide vers des solutions innovantes et compassionnées.

**Tensions possibles** : Le risque de te perdre dans l'idéalisme sans ancrage. Tu peux avoir du mal à définir où tu commences et où le monde finit.

**Conseil clé** : Ancrer tes visions dans des actions concrètes et compassionnées.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition sur ce que le monde a besoin.",
            'week_2': "Trouve une manière créative d'exprimer cette vision.",
            'week_3': "Connecte avec d'autres rêveurs alignés.",
            'week_4': "Honore ta sensibilité comme une force, pas une faiblesse."
        }
    },

    # ==================== MAISON 2 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Ressources innovantes**

Ta Lune en Verseau en Maison 2 te pousse à repenser complètement ta relation à l'argent, aux ressources, à la valeur. L'Ascendant Bélier te donne l'audace d'agir sur ces idées immédiatement.

**Domaine activé** : Maison 2 — Tes finances et possessions deviennent un terrain d'expérimentation. Tu veux créer des sources de revenus originales, sortir des modèles conventionnels.

**Ton approche instinctive** : Tu fonces vers des opportunités non-conventionnelles. Les cryptos, l'économie collaborative, les revenus passifs te fascinent. Tu veux inventer ton indépendance financière.

**Tensions possibles** : Le risque de prendre des risques financiers par idéalisme ou impatience. Tes idées peuvent être trop avant-gardistes pour être immédiatement rentables.

**Conseil clé** : Tester tes idées financières novatrices sans mettre en péril ta stabilité de base.""",
        'weekly_advice': {
            'week_1': "Identifie une source de revenu alternative qui t'intéresse.",
            'week_2': "Fais des recherches concrètes sur sa viabilité.",
            'week_3': "Lance une première expérimentation à petite échelle.",
            'week_4': "Évalue les résultats et ajuste ta stratégie."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Valeur progressive**

Ta Lune en Verseau veut révolutionner ta relation à l'argent, ton Ascendant Taureau veut construire lentement. Tu cherches l'indépendance financière mais sans sacrifier ta sécurité.

**Domaine activé** : Maison 2 — Tes ressources matérielles sont en transformation. Tu veux des revenus qui reflètent tes valeurs tout en restant pragmatique.

**Ton approche instinctive** : Le Taureau te fait vérifier la solidité de tes idées financières avant de t'engager. Tu veux de l'innovation, mais pas au prix de l'instabilité.

**Tensions possibles** : La frustration entre désir de changement et besoin de sécurité. Tu peux hésiter trop longtemps et manquer des opportunités.

**Conseil clé** : Faire évoluer progressivement tes sources de revenus vers plus d'alignement avec tes valeurs.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui ne te correspond plus dans ta situation financière.",
            'week_2': "Recherche des alternatives stables et alignées.",
            'week_3': "Fais un petit ajustement concret dans ta gestion.",
            'week_4': "Consolide ce changement avant d'aller plus loin."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Ressources multiples**

Double air : tu veux diversifier tes sources de revenus, explorer différentes façons de créer de la valeur. La monétisation de tes idées et de ta communication t'intéresse.

**Domaine activé** : Maison 2 — Tes finances deviennent un terrain d'expérimentation intellectuelle. Tu veux gagner de l'argent avec ton intelligence, ta curiosité, tes connexions.

**Ton approche instinctive** : Tu identifies rapidement les opportunités émergentes. Ton réseau devient un actif financier. Tu peux jongler entre plusieurs projets rémunérés.

**Tensions possibles** : Le risque de te disperser sans approfondir aucune source de revenu. Tes idées peuvent rester au stade conceptuel sans devenir rentables.

**Conseil clé** : Choisir deux ou trois pistes financières et les développer sérieusement ce mois-ci.""",
        'weekly_advice': {
            'week_1': "Liste toutes tes idées de revenus potentiels.",
            'week_2': "Sélectionne les deux plus viables et alignées.",
            'week_3': "Crée un plan d'action concret pour chacune.",
            'week_4': "Commence à implémenter et mesure les premiers résultats."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sécurité alternative**

Ta Lune en Verseau veut repenser la sécurité matérielle, ton Ascendant Cancer a besoin de cette sécurité pour se sentir bien. Tu cherches des ressources stables mais non-conventionnelles.

**Domaine activé** : Maison 2 — Tes finances et possessions sont liées à ton sentiment de sécurité émotionnelle. Tu veux construire une base solide à ta manière.

**Ton approche instinctive** : Tu ressens les besoins émergents du marché. Ton intuition te guide vers des opportunités financières innovantes mais rassurantes.

**Tensions possibles** : Le conflit entre besoin de sécurité matérielle et désir d'indépendance financière. Tu peux avoir peur de sortir des sentiers battus.

**Conseil clé** : Construire progressivement une sécurité financière qui respecte tes valeurs uniques.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te ferait sentir vraiment en sécurité financièrement.",
            'week_2': "Explore des modèles non-conventionnels de stabilité.",
            'week_3': "Fais un pas vers plus d'autonomie financière.",
            'week_4': "Cultive la confiance que tu peux créer ta propre sécurité."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Valeur éclatante**

Ta Lune en Verseau veut redistribuer les richesses, ton Ascendant Lion veut créer de la valeur et être reconnu pour ça. Tu cherches l'abondance pour la partager.

**Domaine activé** : Maison 2 — Tes ressources matérielles deviennent un moyen d'exprimer ta générosité et ta vision. Tu veux gagner de l'argent pour financer tes idéaux.

**Ton approche instinctive** : Tu investis avec confiance dans des projets visionnaires. Ton charisme attire des opportunités financières. Tu veux briller tout en servant le collectif.

**Tensions possibles** : Le conflit entre ego financier et altruisme. Tu peux osciller entre générosité excessive et besoin de reconnaissance matérielle.

**Conseil clé** : Utiliser tes ressources pour créer quelque chose de grand qui te dépasse.""",
        'weekly_advice': {
            'week_1': "Définis comment l'argent peut servir ta vision du monde.",
            'week_2': "Investis dans un projet qui a de l'impact.",
            'week_3': "Partage généreusement sans t'appauvrir.",
            'week_4': "Célèbre l'abondance que tu crées et partages."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Efficacité innovante**

Ta Lune en Verseau apporte des idées financières originales, ton Ascendant Vierge les rend applicables et rentables. Tu veux optimiser tes ressources de manière intelligente.

**Domaine activé** : Maison 2 — Tes finances deviennent un système à perfectionner. Tu veux des revenus qui soient à la fois innovants et fiables.

**Ton approche instinctive** : Tu analyses tes flux financiers avec précision et tu identifies les inefficacités. Ton approche est méthodique mais ouverte aux nouvelles solutions.

**Tensions possibles** : Le risque de sur-analyser et de ne jamais passer à l'action. Ou à l'inverse, d'avoir des idées trop théoriques.

**Conseil clé** : Mettre en place un système financier simple mais innovant, puis le laisser tourner.""",
        'weekly_advice': {
            'week_1': "Audite tes revenus et dépenses avec détail.",
            'week_2': "Identifie une optimisation possible.",
            'week_3': "Implémente cette amélioration concrètement.",
            'week_4': "Mesure les résultats et ajuste si nécessaire."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équité financière**

Double air : tu veux des ressources qui reflètent tes valeurs d'équité et de justice. L'argent n'est pas qu'un outil personnel, c'est un moyen de créer de l'harmonie.

**Domaine activé** : Maison 2 — Tes finances sont liées à tes relations et à ta vision de la justice sociale. Tu veux gagner de l'argent de manière éthique.

**Ton approche instinctive** : Tu cherches des partenariats financiers équitables. L'économie collaborative, le commerce équitable, les investissements éthiques t'attirent.

**Tensions possibles** : Le risque de sacrifier ta stabilité financière pour tes idéaux. Tu peux avoir du mal à négocier pour toi-même.

**Conseil clé** : Créer des ressources qui servent à la fois ton bien-être et tes valeurs d'équité.""",
        'weekly_advice': {
            'week_1': "Évalue si tes sources de revenus sont alignées avec tes valeurs.",
            'week_2': "Identifie une opportunité de partenariat financier éthique.",
            'week_3': "Négocie des conditions équitables pour toutes les parties.",
            'week_4': "Célèbre les ressources créées en harmonie avec tes principes."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Transformation financière**

Ta Lune en Verseau veut révolutionner ta relation à l'argent, ton Ascendant Scorpion veut aller au fond des choses. Tu cherches une transformation radicale de tes ressources.

**Domaine activé** : Maison 2 — Tes finances sont en mutation profonde. Tu veux éliminer les dépendances matérielles et créer une vraie autonomie.

**Ton approche instinctive** : Tu explores les tabous financiers : argent et pouvoir, héritage, ressources partagées. Tu veux comprendre les mécanismes cachés de la richesse.

**Tensions possibles** : Le risque de l'obsession financière ou du contrôle excessif. Tes transformations peuvent être trop brutales.

**Conseil clé** : Transformer progressivement ta relation à l'argent en libérant les attachements toxiques.""",
        'weekly_advice': {
            'week_1': "Identifie une croyance limitante sur l'argent.",
            'week_2': "Plonge dans son origine et sa validité actuelle.",
            'week_3': "Prends une décision financière courageuse.",
            'week_4': "Célèbre ta nouvelle autonomie matérielle."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Abondance libre**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent une vision expansive des ressources. Tu veux créer de la richesse pour financer ta liberté et tes aventures.

**Domaine activé** : Maison 2 — Tes finances sont liées à ta quête de sens. Tu veux que l'argent te libère plutôt que de te limiter.

**Ton approche instinctive** : Tu investis avec optimisme dans des opportunités internationales ou éducatives. Tu crois en l'abondance et ça attire les ressources.

**Tensions possibles** : Le risque de l'excès de confiance financière. Tu peux sous-estimer les contraintes pratiques ou dépenser trop vite.

**Conseil clé** : Canaliser ton optimisme financier vers des investissements qui servent vraiment ta liberté.""",
        'weekly_advice': {
            'week_1': "Définis ce que signifie l'abondance pour toi.",
            'week_2': "Explore une opportunité financière internationale ou éducative.",
            'week_3': "Investis dans ce qui élargit tes horizons.",
            'week_4': "Célèbre la liberté que tes ressources te permettent."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Richesse restructurée**

Ta Lune en Verseau veut innover financièrement, ton Ascendant Capricorne veut construire méthodiquement. Tu cherches à créer une richesse durable mais non-conventionnelle.

**Domaine activé** : Maison 2 — Tes ressources matérielles sont en restructuration stratégique. Tu veux bâtir une sécurité financière à ta manière.

**Ton approche instinctive** : Tu planifies tes innovations financières sur le long terme. Ton sérieux donne de la crédibilité à tes idées avant-gardistes.

**Tensions possibles** : Le conflit entre prudence et audace financière. Tu peux te sentir tiraillé·e entre sécurité et innovation.

**Conseil clé** : Construire patiemment une base financière solide qui respecte tes valeurs uniques.""",
        'weekly_advice': {
            'week_1': "Évalue ta stratégie financière à long terme.",
            'week_2': "Identifie un ajustement innovant mais réaliste.",
            'week_3': "Mets-le en place avec discipline.",
            'week_4': "Consolide tes fondations financières renouvelées."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Indépendance matérielle**

Double Verseau sur tes ressources : tu veux inventer complètement ton modèle financier. Les schémas classiques de revenu, d'épargne, de consommation ne te correspondent plus.

**Domaine activé** : Maison 2 — Tes finances deviennent un terrain d'expérimentation radicale. Tu veux créer une autonomie matérielle qui reflète tes valeurs de liberté.

**Ton approche instinctive** : Tu explores toutes les alternatives : économie du don, troc, cryptos, revenus décentralisés. Tu veux te libérer du système traditionnel.

**Tensions possibles** : Le risque de l'instabilité financière par idéalisme. Tes expérimentations peuvent compromettre ta sécurité de base.

**Conseil clé** : Innover financièrement tout en gardant un filet de sécurité pragmatique.""",
        'weekly_advice': {
            'week_1': "Identifie ton modèle financier idéal, même s'il semble utopique.",
            'week_2': "Recherche des exemples concrets de personnes qui le vivent.",
            'week_3': "Fais une première expérimentation à petite échelle.",
            'week_4': "Évalue ce qui fonctionne et ce qui nécessite des ajustements."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Richesse intuitive**

Ta Lune en Verseau veut transformer ta relation à l'argent, ton Ascendant Poissons veut que tes ressources soient alignées spirituellement. Tu cherches l'abondance avec sens.

**Domaine activé** : Maison 2 — Tes finances sont liées à ta foi et à ton intuition. Tu veux que l'argent circule naturellement, sans attachement toxique.

**Ton approche instinctive** : Tu ressens les opportunités financières avant de les comprendre rationnellement. Ta créativité peut devenir une source de revenus.

**Tensions possibles** : Le risque du flou financier ou de la négligence matérielle. Tu peux avoir du mal à gérer concrètement tes ressources.

**Conseil clé** : Ancrer ton intuition financière dans des actions concrètes et mesurables.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition sur une opportunité financière.",
            'week_2': "Vérifie la viabilité pratique de cette intuition.",
            'week_3': "Crée quelque chose de valeur à partir de ta créativité.",
            'week_4': "Cultive la confiance que l'abondance peut venir naturellement."
        }
    },

    # ==================== MAISON 3 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Communicateur pionnier**

Ta Lune en Verseau en Maison 3 te pousse à communiquer tes idées novatrices. L'Ascendant Bélier ajoute l'urgence et l'audace : tu veux dire ce qui doit être dit, maintenant.

**Domaine activé** : Maison 3 — Communication, apprentissage, entourage proche. Tu veux révolutionner la manière dont on échange les idées. Tes conversations deviennent des espaces de transformation.

**Ton approche instinctive** : Tu ne mâches pas tes mots. Face aux conventions de pensée, tu challenges directement. Cette franchise peut choquer mais aussi libérer.

**Tensions possibles** : Le risque de brusquer ton entourage avec tes idées radicales. Tu peux manquer de diplomatie dans ta soif de vérité.

**Conseil clé** : Communiquer tes visions innovantes avec clarté mais aussi avec respect du rythme des autres.""",
        'weekly_advice': {
            'week_1': "Partage une idée non-conventionnelle qui te tient à cœur.",
            'week_2': "Initie une conversation qui challenge les normes.",
            'week_3': "Apprends quelque chose de complètement nouveau.",
            'week_4': "Synthétise ce que tu as découvert et partage-le."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Message ancré**

Ta Lune en Verseau veut communiquer des idées avant-gardistes, ton Ascendant Taureau veut que ces idées soient pratiques et utiles. Tu cherches à transformer la pensée par la simplicité.

**Domaine activé** : Maison 3 — Tes échanges quotidiens, ton apprentissage, ta curiosité intellectuelle cherchent un nouvel équilibre entre innovation et pragmatisme.

**Ton approche instinctive** : Tu prends le temps de digérer les idées nouvelles avant de les partager. Tu veux communiquer des concepts solides, pas juste des modes passagères.

**Tensions possibles** : Le conflit entre besoin de nouveauté intellectuelle et besoin de certitude. Tu peux hésiter à exprimer des idées non encore validées.

**Conseil clé** : Partager progressivement tes réflexions innovantes en les ancrant dans des exemples concrets.""",
        'weekly_advice': {
            'week_1': "Écoute attentivement une perspective différente de la tienne.",
            'week_2': "Intègre cette nouvelle vision à tes croyances existantes.",
            'week_3': "Partage une synthèse pratique de ce que tu as appris.",
            'week_4': "Consolide tes nouvelles connaissances par la pratique."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Esprit brillant**

Double air sur la communication : tu es dans ton élément. Ta Lune en Verseau et ton Ascendant Gémeaux te donnent une curiosité infinie et une capacité à connecter des idées apparemment sans lien.

**Domaine activé** : Maison 3 — Communication, apprentissage, mobilité mentale. Tu veux tout apprendre, tout partager, tout explorer intellectuellement.

**Ton approche instinctive** : Tu sautes d'une idée à l'autre avec aisance. Ton intelligence sociale te permet de partager des concepts complexes de manière accessible.

**Tensions possibles** : Le risque de la dispersion mentale. Tu peux surcharger ton entourage d'informations ou te perdre dans trop de directions.

**Conseil clé** : Choisir un ou deux sujets ce mois-ci et les approfondir vraiment.""",
        'weekly_advice': {
            'week_1': "Explore librement tous les sujets qui t'intéressent.",
            'week_2': "Identifie les deux thèmes les plus captivants.",
            'week_3': "Approfondis-les et crée des connexions originales.",
            'week_4': "Partage tes découvertes de manière structurée."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Parole empathique**

Ta Lune en Verseau veut communiquer des vérités universelles, ton Ascendant Cancer veut créer de la sécurité émotionnelle par les mots. Tu cherches à connecter les gens par l'échange.

**Domaine activé** : Maison 3 — Tes conversations, ton apprentissage, tes relations de proximité deviennent des espaces de soin émotionnel et d'ouverture intellectuelle.

**Ton approche instinctive** : Tu écoutes avec empathie puis tu offres une perspective nouvelle. Ton approche combine sensibilité et lucidité.

**Tensions possibles** : Le conflit entre détachement intellectuel et implication émotionnelle. Tu peux te sentir tiraillé·e entre objectivité et empathie.

**Conseil clé** : Utiliser tes idées pour créer du lien, pas pour te protéger de l'émotion.""",
        'weekly_advice': {
            'week_1': "Écoute vraiment quelqu'un de ton entourage proche.",
            'week_2': "Partage une perspective qui pourrait l'aider.",
            'week_3': "Apprends quelque chose sur les émotions humaines.",
            'week_4': "Crée un espace de dialogue sécurisant dans ton quotidien."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Porte-parole charismatique**

Ta Lune en Verseau veut partager des idées révolutionnaires, ton Ascendant Lion veut que ces idées brillent et inspirent. Tu deviens le messager d'une vision collective.

**Domaine activé** : Maison 3 — Ta communication, ton apprentissage, tes échanges quotidiens deviennent une scène où tu peux briller intellectuellement.

**Ton approche instinctive** : Tu communiques avec confiance et passion. Tes idées captivent parce que tu y crois vraiment. Tu veux inspirer par tes mots.

**Tensions possibles** : Le risque de l'ego intellectuel. Tu peux vouloir avoir raison plutôt que d'échanger vraiment. Ou à l'inverse, négliger ta voix par fausse modestie.

**Conseil clé** : Utiliser ton charisme communicationnel pour porter des idées qui te dépassent.""",
        'weekly_advice': {
            'week_1': "Identifie un message important que tu veux faire passer.",
            'week_2': "Trouve la manière la plus impactante de le communiquer.",
            'week_3': "Prends la parole publiquement sur ce sujet.",
            'week_4': "Célèbre l'impact de tes mots sur les autres."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Analyste précis**

Ta Lune en Verseau apporte des idées novatrices, ton Ascendant Vierge les analyse et les communique avec précision. Tu veux que tes concepts soient à la fois innovants et applicables.

**Domaine activé** : Maison 3 — Ton apprentissage, ta communication, ton traitement de l'information deviennent plus méthodiques et plus visionnaires à la fois.

**Ton approche instinctive** : Tu décortiques les idées nouvelles pour en extraire l'essence pratique. Ta communication est claire, détaillée, utile.

**Tensions possibles** : Le risque de la paralysie analytique. Tu peux sur-analyser au lieu de simplement partager. Ou à l'inverse, être trop théorique.

**Conseil clé** : Équilibrer analyse et intuition dans ta manière de traiter et partager l'information.""",
        'weekly_advice': {
            'week_1': "Analyse en profondeur un sujet qui t'intéresse.",
            'week_2': "Identifie les applications pratiques de tes découvertes.",
            'week_3': "Partage tes conclusions de manière structurée.",
            'week_4': "Affine ton système de traitement de l'information."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Médiateur d'idées**

Double air : ta communication devient un art. Tu veux créer des ponts entre les perspectives, faciliter les échanges, harmoniser les idées divergentes.

**Domaine activé** : Maison 3 — Tes conversations, ton apprentissage, tes relations de proximité deviennent des espaces de création d'harmonie intellectuelle.

**Ton approche instinctive** : Tu sais présenter des idées radicales de manière acceptable. Ton tact naturel te permet de faire passer des messages difficiles sans créer de conflit.

**Tensions possibles** : Le risque de diluer tes convictions pour maintenir l'harmonie. Tu peux éviter les conversations nécessaires mais inconfortables.

**Conseil clé** : Dire ta vérité avec diplomatie, sans la sacrifier pour la paix.""",
        'weekly_advice': {
            'week_1': "Facilite un échange entre deux perspectives opposées.",
            'week_2': "Partage une opinion tranchée avec élégance.",
            'week_3': "Apprends l'art de la communication non-violente.",
            'week_4': "Célèbre les connexions intellectuelles que tu as créées."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité incisive**

Ta Lune en Verseau veut communiquer des vérités collectives, ton Ascendant Scorpion veut aller au fond des non-dits. Ta parole devient un scalpel qui révèle.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage, tes conversations deviennent des espaces de transformation profonde. Tu ne parles pas pour combler le silence.

**Ton approche instinctive** : Tu perces les façades conversationnelles. Tes questions vont à l'essentiel. Cette intensité peut mettre mal à l'aise mais aussi libérer.

**Tensions possibles** : Le risque de la brutalité verbale ou de l'obsession intellectuelle. Tu peux effrayer ton entourage avec ton intensité.

**Conseil clé** : Doser ton intensité communicationnelle selon les capacités de réception de l'autre.""",
        'weekly_advice': {
            'week_1': "Pose une question qui révèle une vérité cachée.",
            'week_2': "Explore un sujet tabou intellectuellement.",
            'week_3': "Partage une observation inconfortable mais nécessaire.",
            'week_4': "Transforme une conversation superficielle en échange profond."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Enseignant inspiré**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent un enthousiasme communicatif pour les idées qui élargissent les perspectives. Tu veux éduquer et inspirer.

**Domaine activé** : Maison 3 — Ton apprentissage, ta communication, tes déplacements courts deviennent des aventures intellectuelles. Chaque échange est une opportunité de croissance.

**Ton approche instinctive** : Tu partages tes découvertes avec générosité et enthousiasme. Ton optimisme intellectuel est contagieux.

**Tensions possibles** : Le risque de l'excès de confiance dans tes idées ou de la tendance à prêcher plutôt qu'échanger.

**Conseil clé** : Rester ouvert·e à apprendre autant que tu enseignes dans tes interactions.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie ou vision du monde nouvelle.",
            'week_2': "Partage ce que tu apprends avec enthousiasme.",
            'week_3': "Engage une conversation qui élargit les horizons.",
            'week_4': "Synthétise comment ta vision du monde a évolué."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Stratège intellectuel**

Ta Lune en Verseau veut communiquer des idées visionnaires, ton Ascendant Capricorne veut que ces idées aient un impact stratégique durable.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage, ta communication deviennent plus structurés et orientés vers des objectifs à long terme.

**Ton approche instinctive** : Tu planifies tes communications pour maximiser leur impact. Tu sais quel message dire à quel moment. Cette maîtrise est impressionnante mais peut sembler calculée.

**Tensions possibles** : Le conflit entre spontanéité intellectuelle et contrôle communicationnel. Tu peux te censurer par excès de prudence.

**Conseil clé** : Laisser de la place à la spontanéité dans tes échanges tout en gardant ta vision stratégique.""",
        'weekly_advice': {
            'week_1': "Définis quel message tu veux faire passer ce mois-ci.",
            'week_2': "Crée une stratégie de communication claire.",
            'week_3': "Implémente cette stratégie avec discipline.",
            'week_4': "Évalue l'impact de tes communications."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Visionnaire verbal**

Double Verseau sur la communication : tu es le messager du futur. Tes idées sont avant-gardistes, ta manière de les partager aussi. Tu veux révolutionner le dialogue lui-même.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage, ta mobilité intellectuelle sont en pleine révolution. Tu ne veux plus communiquer comme avant.

**Ton approche instinctive** : Tu explores de nouveaux formats de communication : podcasts, threads, vidéos conceptuelles. Tu veux que la forme serve le fond innovant.

**Tensions possibles** : Le risque de l'incompréhension ou de l'isolement intellectuel. Tes idées peuvent être trop en avance.

**Conseil clé** : Trouver des traducteurs ou des ponts entre ta vision et la compréhension commune.""",
        'weekly_advice': {
            'week_1': "Exprime librement toutes tes idées novatrices.",
            'week_2': "Identifie celles qui méritent d'être développées.",
            'week_3': "Trouve un format de communication innovant pour les partager.",
            'week_4': "Connecte avec ceux qui comprennent ta vision."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Poésie prophétique**

Ta Lune en Verseau veut communiquer des vérités universelles, ton Ascendant Poissons veut les exprimer à travers l'art et l'intuition. Tes mots deviennent des ponts vers l'invisible.

**Domaine activé** : Maison 3 — Tes échanges, ton apprentissage, ta communication deviennent plus subtils, plus symboliques, plus inspirés.

**Ton approche instinctive** : Tu captes des idées qui flottent dans l'air du temps et tu les exprimes de manière poétique ou métaphorique.

**Tensions possibles** : Le risque du flou communicationnel. Tes messages peuvent être mal compris ou trop abstraits.

**Conseil clé** : Ancrer tes intuitions dans des mots suffisamment clairs pour être partagés.""",
        'weekly_advice': {
            'week_1': "Écoute les murmures de l'inconscient collectif.",
            'week_2': "Exprime ces intuitions de manière créative.",
            'week_3': "Partage ton art ou tes écrits inspirés.",
            'week_4': "Accepte que certains comprennent et d'autres non."
        }
    },

    # ==================== MAISON 4 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Foyer révolutionnaire**

Ta Lune en Verseau en Maison 4 questionne profondément ton rapport à la famille, aux racines, au foyer. L'Ascendant Bélier te pousse à agir vite pour transformer ton espace intime.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes fondations émotionnelles cherchent une nouvelle forme. Tu veux créer un chez-toi qui te ressemble vraiment.

**Ton approche instinctive** : Tu veux casser les modèles familiaux hérités. Face aux traditions, ton réflexe est de créer les tiennes, différentes, plus libres.

**Tensions possibles** : Le risque de brusquer ton entourage familial ou de rejeter trop vite ce qui pourrait encore avoir du sens.

**Conseil clé** : Transformer progressivement ton espace de vie pour qu'il reflète ta singularité sans tout détruire.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui ne te correspond plus dans ton foyer.",
            'week_2': "Fais un changement concret dans ton espace de vie.",
            'week_3': "Communique tes besoins à ta famille ou colocataires.",
            'week_4': "Crée un rituel personnel qui t'ancre chez toi."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Racines progressistes**

Ta Lune en Verseau veut réinventer le concept de foyer, ton Ascendant Taureau a besoin de stabilité et d'enracinement. Tu cherches une base solide mais non-conventionnelle.

**Domaine activé** : Maison 4 — Ton foyer, ta sécurité intérieure, tes fondations cherchent un équilibre entre tradition et modernité.

**Ton approche instinctive** : Tu construis lentement un espace de vie qui te ressemble. Tu veux du confort mais pas du conformisme.

**Tensions possibles** : Le conflit entre besoin de sécurité familiale et désir d'indépendance. Tu peux te sentir tiraillé·e entre appartenance et liberté.

**Conseil clé** : Créer un foyer qui soit à la fois sécurisant et authentiquement toi.""",
        'weekly_advice': {
            'week_1': "Évalue si ton espace de vie te nourrit vraiment.",
            'week_2': "Fais un ajustement qui le rend plus confortable et plus toi.",
            'week_3': "Ancre-toi dans ce nouveau confort.",
            'week_4': "Célèbre ton foyer unique."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Famille intellectuelle**

Double air : ton foyer devient un espace de stimulation intellectuelle. Tu veux vivre entouré·e de conversations, d'idées, de diversité.

**Domaine activé** : Maison 4 — Ton chez-toi, ta famille émotionnelle (choisie ou biologique), tes racines deviennent plus fluides, moins figées.

**Ton approche instinctive** : Tu veux un foyer ouvert, où circulent les idées et les personnes. La cohabitation créative t'attire plus que la famille traditionnelle.

**Tensions possibles** : Le risque de manquer de profondeur émotionnelle dans tes relations intimes. Tu peux intellectualiser ce qui devrait être ressenti.

**Conseil clé** : Créer un équilibre entre stimulation intellectuelle et ancrage émotionnel dans ton espace intime.""",
        'weekly_advice': {
            'week_1': "Invite quelqu'un d'intéressant chez toi pour échanger.",
            'week_2': "Réorganise ton espace pour favoriser la communication.",
            'week_3': "Explore tes racines familiales avec curiosité.",
            'week_4': "Définis ce que « famille » signifie vraiment pour toi."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Refuge atypique**

Ta Lune en Verseau veut repenser le foyer, ton Ascendant Cancer a un besoin profond de sécurité émotionnelle. Tu cherches un nid qui soit à la fois protecteur et libre.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes besoins de sécurité intérieure sont au cœur de tes préoccupations. Tu veux te sentir chez toi à ta manière.

**Ton approche instinctive** : Tu crées un espace intime qui nourrit émotionnellement tout en respectant ton besoin d'indépendance. C'est un paradoxe que tu explores.

**Tensions possibles** : Le conflit entre attachement familial et besoin de liberté. Tu peux te sentir coupable de vouloir t'éloigner des modèles familiaux.

**Conseil clé** : Honorer ton besoin de sécurité émotionnelle sans sacrifier ton authenticité.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te fait vraiment sentir en sécurité.",
            'week_2': "Crée cet espace de sécurité à ta manière.",
            'week_3': "Communique tes besoins à ta famille avec douceur.",
            'week_4': "Cultive ton cocon unique."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Foyer lumineux**

Ta Lune en Verseau veut un foyer non-conventionnel, ton Ascendant Lion veut que ce foyer soit magnifique et accueillant. Tu veux créer un espace qui inspire.

**Domaine activé** : Maison 4 — Ton foyer devient une expression de ta créativité et de ta vision. Tu veux que ton espace intime soit aussi une œuvre d'art.

**Ton approche instinctive** : Tu investis avec générosité dans ton espace de vie. Tu veux que les gens se sentent bien chez toi tout en respectant ton unicité.

**Tensions possibles** : Le risque de chercher la validation extérieure pour ton espace intime. Ton foyer doit d'abord te plaire à toi.

**Conseil clé** : Créer un chez-toi qui te ressemble vraiment, pas qui impressionne.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton foyer peut refléter ta créativité.",
            'week_2': "Fais un ajustement esthétique audacieux.",
            'week_3': "Invite des proches à célébrer ton espace.",
            'week_4': "Reconnais que ton foyer est un sanctuaire personnel."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Foyer optimisé**

Ta Lune en Verseau veut innover dans ton espace de vie, ton Ascendant Vierge veut que cet espace soit fonctionnel et sain. Tu cherches l'équilibre entre originalité et praticité.

**Domaine activé** : Maison 4 — Ton foyer, tes routines domestiques, ta base émotionnelle cherchent plus d'efficacité et de sens.

**Ton approche instinctive** : Tu analyses ce qui fonctionne et ce qui ne fonctionne pas dans ton espace de vie, puis tu améliores systématiquement.

**Tensions possibles** : Le risque de sur-optimiser au détriment de la spontanéité. Ton foyer peut devenir trop fonctionnel et manquer de chaleur.

**Conseil clé** : Créer un espace qui soit à la fois efficace et nourrissant émotionnellement.""",
        'weekly_advice': {
            'week_1': "Audite ton espace de vie : qu'est-ce qui ne fonctionne plus?",
            'week_2': "Implémente une amélioration pratique innovante.",
            'week_3': "Crée une routine domestique qui te simplifie la vie.",
            'week_4': "Apprécie ton foyer optimisé."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Foyer harmonieux**

Double air : ton foyer devient un espace de beauté et de connexion. Tu veux un chez-toi qui soit à la fois esthétique et ouvert aux autres.

**Domaine activé** : Maison 4 — Ton foyer, tes relations familiales, ta base émotionnelle cherchent plus d'équilibre et d'harmonie.

**Ton approche instinctive** : Tu crées un espace qui favorise les échanges harmonieux. Ton foyer devient un lieu de rencontre et de partage.

**Tensions possibles** : Le risque de sacrifier ton confort personnel pour accommoder les autres. Ton foyer doit d'abord te servir toi.

**Conseil clé** : Créer un équilibre entre hospitalité et préservation de ton espace intime.""",
        'weekly_advice': {
            'week_1': "Embellis ton espace de vie de manière originale.",
            'week_2': "Crée un espace de dialogue dans ton foyer.",
            'week_3': "Équilibre solitude et partage chez toi.",
            'week_4': "Célèbre l'harmonie que tu as créée."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Sanctuaire transformé**

Ta Lune en Verseau veut libérer ton espace intime, ton Ascendant Scorpion veut aller au fond de tes blessures familiales. Ton foyer devient un espace de guérison radicale.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes racines sont en transformation profonde. Tu veux nettoyer l'héritage émotionnel qui ne te sert plus.

**Ton approche instinctive** : Tu explores les non-dits familiaux, les patterns hérités. Cette plongée peut être intense mais libératrice.

**Tensions possibles** : Le risque de l'obsession sur le passé familial ou de la rupture brutale. Tu peux vouloir tout transformer d'un coup.

**Conseil clé** : Transformer progressivement ton espace intime en libérant ce qui est prêt à partir.""",
        'weekly_advice': {
            'week_1': "Identifie un pattern familial qui te limite.",
            'week_2': "Explore son origine avec honnêteté.",
            'week_3': "Prends une décision courageuse pour t'en libérer.",
            'week_4': "Célèbre ton nouveau sentiment de liberté intérieure."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foyer nomade**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent un rapport libre au foyer. Tu veux un chez-toi qui ne te limite pas dans ta quête d'exploration.

**Domaine activé** : Maison 4 — Ton foyer, tes racines, ta base émotionnelle cherchent plus de liberté et de sens.

**Ton approche instinctive** : Tu veux un espace qui te permette de partir et revenir librement. La notion de foyer devient plus philosophique que géographique.

**Tensions possibles** : Le risque de fuir l'intimité ou de manquer d'ancrage. Tu peux avoir du mal à t'engager dans un lieu.

**Conseil clé** : Créer un foyer qui te donne des racines ET des ailes.""",
        'weekly_advice': {
            'week_1': "Réfléchis à ce que « foyer » signifie vraiment pour toi.",
            'week_2': "Crée un espace qui respecte ton besoin de liberté.",
            'week_3': "Explore tes racines culturelles ou familiales.",
            'week_4': "Célèbre ton foyer unique et mobile."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fondations réinventées**

Ta Lune en Verseau veut révolutionner ton rapport au foyer, ton Ascendant Capricorne veut construire des bases solides. Tu cherches à créer un héritage différent.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes racines sont en restructuration stratégique. Tu veux bâtir quelque chose de durable mais de nouveau.

**Ton approche instinctive** : Tu planifies ton espace de vie à long terme. Tu veux créer un foyer qui serve de fondation solide pour ton avenir unique.

**Tensions possibles** : Le conflit entre respect des traditions familiales et besoin de les transformer. Tu peux te sentir tiraillé·e.

**Conseil clé** : Honorer ce qui est précieux dans ton héritage tout en le faisant évoluer.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui est précieux dans ton héritage familial.",
            'week_2': "Définis comment tu veux le faire évoluer.",
            'week_3': "Prends une action concrète vers cette transformation.",
            'week_4': "Consolide tes nouvelles fondations."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Foyer utopique**

Double Verseau sur ton espace intime : tu veux créer un foyer complètement différent de ce que tu as connu. La notion même de famille et de maison est à réinventer.

**Domaine activé** : Maison 4 — Ton foyer, ta famille (choisie ou biologique), tes racines sont en pleine révolution. Tu ne veux plus jouer selon les règles établies.

**Ton approche instinctive** : Tu explores des modèles de vie alternatifs : colocation intentionnelle, communauté, habitat partagé. Le conventionnel ne t'intéresse plus.

**Tensions possibles** : Le risque de l'instabilité ou de l'isolement. Ton besoin de liberté peut compromettre ta sécurité de base.

**Conseil clé** : Innover dans ton espace de vie tout en préservant un minimum de stabilité.""",
        'weekly_advice': {
            'week_1': "Imagine ton foyer idéal sans limites.",
            'week_2': "Recherche des exemples réels de modes de vie alternatifs.",
            'week_3': "Fais un changement concret vers cette vision.",
            'week_4': "Connecte avec d'autres qui partagent cette vision."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sanctuaire spirituel**

Ta Lune en Verseau veut un foyer libre, ton Ascendant Poissons veut un espace spirituel et artistique. Tu cherches à créer un refuge qui nourrit ton âme.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes fondations émotionnelles cherchent plus de transcendance et de sens.

**Ton approche instinctive** : Tu crées un espace inspiré, méditatif, créatif. Ton foyer devient un temple personnel où tu te reconnectes à l'essentiel.

**Tensions possibles** : Le risque du flou dans tes besoins domestiques ou de la négligence matérielle. Ton foyer peut manquer de structure.

**Conseil clé** : Ancrer ton idéal spirituel dans un espace concret et fonctionnel.""",
        'weekly_advice': {
            'week_1': "Crée un espace méditatif ou créatif chez toi.",
            'week_2': "Laisse ton intuition guider l'aménagement de ton foyer.",
            'week_3': "Purifie énergétiquement ton espace de vie.",
            'week_4': "Célèbre ton sanctuaire personnel."
        }
    },

    # ==================== MAISON 5 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Créativité audacieuse**

Ta Lune en Verseau en Maison 5 t'invite à exprimer ta créativité de manière originale. L'Ascendant Bélier ajoute l'impulsion d'agir : tu veux créer quelque chose de nouveau, maintenant.

**Domaine activé** : Maison 5 — Créativité, plaisir, romance, expression personnelle. Tu veux t'amuser différemment, aimer différemment, créer différemment.

**Ton approche instinctive** : Tu prends des risques créatifs sans hésiter. Tes projets sont avant-gardistes et audacieux. Cette spontanéité attire l'attention.

**Tensions possibles** : Le risque de la dispersion créative ou des relations amoureuses trop rapides. Tu peux chercher l'excitation sans construire.

**Conseil clé** : Canaliser ton énergie créative vers un projet qui a du potentiel à long terme.""",
        'weekly_advice': {
            'week_1': "Lance un projet créatif qui te fait vraiment vibrer.",
            'week_2': "Prends un risque dans ton expression personnelle.",
            'week_3': "Explore une forme d'art ou de jeu non-conventionnelle.",
            'week_4': "Célèbre ta création unique."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Plaisir authentique**

Ta Lune en Verseau veut explorer de nouvelles formes de créativité, ton Ascendant Taureau veut des plaisirs tangibles et durables. Tu cherches la joie qui reste.

**Domaine activé** : Maison 5 — Ta créativité, tes loisirs, tes romances cherchent un équilibre entre innovation et substance.

**Ton approche instinctive** : Tu construis lentement des projets créatifs originaux. Tu veux que ton plaisir soit réel, pas juste une stimulation passagère.

**Tensions possibles** : Le conflit entre besoin de nouveauté et besoin de stabilité dans tes plaisirs. Tu peux hésiter à sortir de ta zone de confort.

**Conseil clé** : Introduire progressivement de la nouveauté dans ce qui te fait plaisir.""",
        'weekly_advice': {
            'week_1': "Identifie un plaisir habituel que tu veux renouveler.",
            'week_2': "Expérimente une variation originale.",
            'week_3': "Crée quelque chose de beau et durable.",
            'week_4': "Savoure pleinement ta création."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Jeu intellectuel**

Double air : ta créativité devient ludique et conceptuelle. Tu veux jouer avec les idées, expérimenter sans te prendre au sérieux.

**Domaine activé** : Maison 5 — Ton expression créative, tes loisirs, tes romances deviennent plus légers, plus variés, plus spontanés.

**Ton approche instinctive** : Tu explores plusieurs projets créatifs à la fois. Le processus t'intéresse plus que le résultat. Cette légèreté est rafraîchissante.

**Tensions possibles** : Le risque de ne jamais finir ce que tu commences. Tes projets peuvent rester au stade d'ébauche.

**Conseil clé** : Choisir un ou deux projets créatifs et les mener à terme ce mois-ci.""",
        'weekly_advice': {
            'week_1': "Explore librement toutes tes envies créatives.",
            'week_2': "Identifie ce qui mérite d'être développé.",
            'week_3': "Engage-toi à finir au moins un projet.",
            'week_4': "Partage ta création avec légèreté."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Créativité émotionnelle**

Ta Lune en Verseau veut créer quelque chose d'original, ton Ascendant Cancer veut que cette créativité exprime tes émotions profondes.

**Domaine activé** : Maison 5 — Ta créativité, tes plaisirs, tes romances oscillent entre détachement et sensibilité.

**Ton approche instinctive** : Tu crées pour exprimer ce que tu ressens tout en gardant une perspective universelle. Ton art touche les gens.

**Tensions possibles** : Le conflit entre vulnérabilité émotionnelle et besoin de protection. Tu peux avoir peur de te montrer vraiment.

**Conseil clé** : Oser exprimer créativement tes émotions sans te protéger derrière l'intellectualisation.""",
        'weekly_advice': {
            'week_1': "Identifie une émotion que tu veux exprimer créativement.",
            'week_2': "Trouve le médium artistique qui lui correspond.",
            'week_3': "Crée sans censure ni jugement.",
            'week_4': "Partage ton œuvre avec ceux qui peuvent la recevoir."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Star visionnaire**

Opposition Verseau-Lion : tu veux créer quelque chose qui brille tout en servant le collectif. Ton expression personnelle devient un acte politique.

**Domaine activé** : Maison 5 — Ta créativité, ton désir de reconnaissance, tes plaisirs cherchent un équilibre entre ego et altruisme.

**Ton approche instinctive** : Tu crées avec confiance et générosité. Ton charisme naturel attire l'attention sur tes projets innovants.

**Tensions possibles** : Le risque de créer pour la validation plutôt que pour l'expression authentique. Ou à l'inverse, de nier ton besoin de reconnaissance.

**Conseil clé** : Utiliser ton talent créatif pour inspirer et servir, pas juste pour briller.""",
        'weekly_advice': {
            'week_1': "Définis quel message tu veux faire passer par ta créativité.",
            'week_2': "Crée avec audace et authenticité.",
            'week_3': "Partage ton œuvre publiquement.",
            'week_4': "Célèbre l'impact de ta création."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Artisanat innovant**

Ta Lune en Verseau apporte des idées créatives originales, ton Ascendant Vierge les rend excellentes dans l'exécution.

**Domaine activé** : Maison 5 — Ta créativité, tes projets personnels, tes loisirs deviennent plus précis et plus significatifs.

**Ton approche instinctive** : Tu perfectionnes tes créations avec soin. Ton travail est à la fois innovant et impeccable.

**Tensions possibles** : Le risque de sur-analyser ta créativité au point de la bloquer. La perfection peut étouffer la spontanéité.

**Conseil clé** : Laisser place à l'expérimentation imparfaite dans ton processus créatif.""",
        'weekly_advice': {
            'week_1': "Commence un projet créatif sans attendre qu'il soit parfait.",
            'week_2': "Affine progressivement ton exécution.",
            'week_3': "Accepte que l'œuvre soit terminée même si imparfaite.",
            'week_4': "Partage ton travail et reçois les retours avec ouverture."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Beauté collaborative**

Double air : ta créativité devient sociale et esthétique. Tu veux créer avec d'autres, pour d'autres, dans l'harmonie.

**Domaine activé** : Maison 5 — Ton expression créative, tes romances, tes plaisirs cherchent plus de partage et de beauté.

**Ton approche instinctive** : Tu co-crées naturellement. Tes projets artistiques impliquent souvent la collaboration ou visent à créer de l'harmonie.

**Tensions possibles** : Le risque de diluer ta vision créative pour plaire aux autres. Tu peux perdre ton originalité dans le compromis.

**Conseil clé** : Créer en collaboration tout en gardant ton empreinte unique visible.""",
        'weekly_advice': {
            'week_1': "Lance un projet créatif collaboratif.",
            'week_2': "Assure-toi que ta voix unique reste audible.",
            'week_3': "Crée quelque chose de beau qui serve l'harmonie collective.",
            'week_4': "Célèbre la co-création."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Passion intense**

Ta Lune en Verseau veut créer quelque chose d'original, ton Ascendant Scorpion veut y mettre toute ton intensité émotionnelle.

**Domaine activé** : Maison 5 — Ta créativité, tes romances, tes passions deviennent plus profondes et transformatrices.

**Ton approche instinctive** : Tu t'immerges complètement dans tes projets créatifs. Ton art explore les tabous, les profondeurs humaines.

**Tensions possibles** : Le risque de l'obsession créative ou des passions consumantes. Tu peux t'épuiser dans ton intensité.

**Conseil clé** : Doser ton intensité créative pour qu'elle reste soutenable et productive.""",
        'weekly_advice': {
            'week_1': "Identifie un sujet profond que tu veux explorer créativement.",
            'week_2': "Plonge sans retenue dans cette exploration.",
            'week_3': "Transforme tes découvertes en œuvre.",
            'week_4': "Prends du recul et intègre ce que tu as vécu."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventure créative**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent une créativité expansive et philosophique. Tu veux que ton art ait du sens.

**Domaine activé** : Maison 5 — Ta créativité, tes plaisirs, tes romances cherchent plus de liberté et de signification.

**Ton approche instinctive** : Tu explores avec enthousiasme. Tes projets créatifs sont audacieux et optimistes. Tu veux inspirer à travers ton art.

**Tensions possibles** : Le risque de commencer trop de projets sans les finir. Ton enthousiasme peut manquer de discipline.

**Conseil clé** : Canaliser ton inspiration créative vers un projet qui compte vraiment pour toi.""",
        'weekly_advice': {
            'week_1': "Définis ta vision créative idéale.",
            'week_2': "Explore librement sans te limiter.",
            'week_3': "Choisis un projet et engage-toi.",
            'week_4': "Partage ta création avec générosité."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Créativité ambitieuse**

Ta Lune en Verseau veut innover créativement, ton Ascendant Capricorne veut que ces créations aient un impact durable.

**Domaine activé** : Maison 5 — Ta créativité, tes projets personnels, tes plaisirs deviennent plus stratégiques et orientés vers des objectifs.

**Ton approche instinctive** : Tu travailles sérieusement sur tes projets créatifs. Tu veux créer quelque chose qui dure et qui ait de la valeur.

**Tensions possibles** : Le risque de perdre la spontanéité créative par excès de contrôle. Ton art peut devenir trop calculé.

**Conseil clé** : Laisser place au jeu et à l'expérimentation dans ton processus créatif.""",
        'weekly_advice': {
            'week_1': "Définis quel héritage créatif tu veux laisser.",
            'week_2': "Planifie un projet créatif ambitieux.",
            'week_3': "Travaille avec discipline sur ce projet.",
            'week_4': "Évalue tes progrès et ajuste ta stratégie."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Génie créatif**

Double Verseau sur ta créativité : ton expression personnelle est avant-gardiste, unique, révolutionnaire. Tu ne veux pas créer comme les autres.

**Domaine activé** : Maison 5 — Ton expression créative, tes plaisirs, tes romances sont en pleine expérimentation. Tu explores de nouvelles formes d'art et de joie.

**Ton approche instinctive** : Tu innoves naturellement. Tes créations sont originales au point parfois d'être incomprises. Cette singularité est ta force.

**Tensions possibles** : Le risque de l'isolement créatif ou du rejet de ton œuvre. Ton avant-gardisme peut déstabiliser.

**Conseil clé** : Créer pour toi d'abord, puis trouver ta tribu qui comprend ta vision.""",
        'weekly_advice': {
            'week_1': "Exprime librement ta créativité sans filtre.",
            'week_2': "Explore des médiums artistiques non-conventionnels.",
            'week_3': "Crée quelque chose qui n'existe pas encore.",
            'week_4': "Connecte avec d'autres créateurs visionnaires."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Art transcendant**

Ta Lune en Verseau veut créer quelque chose d'original, ton Ascendant Poissons veut que cette création touche l'âme et l'invisible.

**Domaine activé** : Maison 5 — Ta créativité, tes plaisirs, tes romances deviennent plus spirituels, plus inspirés, plus universels.

**Ton approche instinctive** : Tu canalises l'inspiration collective dans ton art. Tes créations sont à la fois innovantes et profondément émouvantes.

**Tensions possibles** : Le risque du flou créatif ou de la procrastination par manque de structure. Tes visions peuvent rester des rêves.

**Conseil clé** : Ancrer tes inspirations dans des créations concrètes et partageables.""",
        'weekly_advice': {
            'week_1': "Écoute ton inspiration créative sans jugement.",
            'week_2': "Trouve un médium artistique pour l'exprimer.",
            'week_3': "Crée en état de flow, sans forcer.",
            'week_4': "Partage ton art comme un cadeau au monde."
        }
    },

    # ==================== MAISON 6 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Travail révolutionnaire**

Ta Lune en Verseau en Maison 6 te pousse à révolutionner ton quotidien, ton travail, ta santé. L'Ascendant Bélier ajoute l'urgence d'agir maintenant.

**Domaine activé** : Maison 6 — Ton travail, tes routines, ta santé cherchent une nouvelle forme. Tu veux un quotidien qui te ressemble vraiment.

**Ton approche instinctive** : Tu rejettes les routines qui ne font plus sens. Tu veux innover dans ta manière de travailler et de prendre soin de toi.

**Tensions possibles** : Le risque de tout chambouler trop vite sans considérer les conséquences pratiques. L'impatience peut créer du chaos.

**Conseil clé** : Transformer progressivement ton quotidien en testant de nouvelles approches.""",
        'weekly_advice': {
            'week_1': "Identifie une routine qui ne te sert plus.",
            'week_2': "Expérimente une alternative innovante.",
            'week_3': "Ajuste selon les résultats observés.",
            'week_4': "Consolide les changements qui fonctionnent."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Santé progressive**

Ta Lune en Verseau veut optimiser ton quotidien, ton Ascendant Taureau veut des routines stables et plaisantes. Tu cherches l'équilibre entre innovation et confort.

**Domaine activé** : Maison 6 — Ton travail, ta santé, tes habitudes quotidiennes cherchent à évoluer sans perdre leur stabilité.

**Ton approche instinctive** : Tu améliores lentement mais sûrement. Tu veux des routines qui soient à la fois innovantes et durables.

**Tensions possibles** : Le conflit entre désir de changement et besoin de confort. Tu peux résister trop longtemps à des évolutions nécessaires.

**Conseil clé** : Introduire des améliorations graduelles dans ton quotidien qui deviennent de nouvelles habitudes saines.""",
        'weekly_advice': {
            'week_1': "Évalue ce qui fonctionne et ce qui ne fonctionne plus dans ton quotidien.",
            'week_2': "Fais un petit ajustement concret et plaisant.",
            'week_3': "Ancre cette nouvelle routine progressivement.",
            'week_4': "Apprécie ton quotidien amélioré."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Routine variée**

Double air : ton quotidien a besoin de diversité et de stimulation intellectuelle. Tu veux un travail qui nourrit ta curiosité.

**Domaine activé** : Maison 6 — Tes routines, ton travail, ta santé cherchent plus de flexibilité et de variété.

**Ton approche instinctive** : Tu jongle entre plusieurs tâches et projets. La monotonie t'épuise plus que la charge de travail.

**Tensions possibles** : Le risque de la dispersion ou de l'inconstance dans tes routines. Tu peux manquer de suivi.

**Conseil clé** : Créer des routines flexibles qui incorporent de la variété tout en assurant la constance nécessaire.""",
        'weekly_advice': {
            'week_1': "Identifie les aspects monotones de ton quotidien.",
            'week_2': "Introduis de la variété dans tes routines.",
            'week_3': "Alterne entre différents types de tâches.",
            'week_4': "Équilibre stimulation et constance."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Service empathique**

Ta Lune en Verseau veut améliorer le monde par le travail, ton Ascendant Cancer veut prendre soin des autres. Tu cherches à servir avec cœur.

**Domaine activé** : Maison 6 — Ton travail, ta santé, tes routines oscillent entre détachement efficace et implication émotionnelle.

**Ton approche instinctive** : Tu veux un travail qui ait du sens humain. Tu te préoccupes du bien-être de tes collègues et de ceux que tu sers.

**Tensions possibles** : Le risque de l'épuisement par surengagement émotionnel dans ton travail. Tu peux te sacrifier pour les autres.

**Conseil clé** : Servir avec efficacité tout en préservant ton énergie émotionnelle.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton travail peut avoir plus de sens humain.",
            'week_2': "Mets en place des routines qui nourrissent ton bien-être.",
            'week_3': "Apprends à dire non quand nécessaire.",
            'week_4': "Équilibre service aux autres et soin de soi."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Excellence quotidienne**

Ta Lune en Verseau veut optimiser ton quotidien, ton Ascendant Lion veut que ton travail soit remarquable et inspire les autres.

**Domaine activé** : Maison 6 — Ton travail, tes routines, ta santé deviennent des domaines où tu veux briller et innover.

**Ton approche instinctive** : Tu mets de la fierté dans ton travail quotidien. Tu veux que même tes routines reflètent ton excellence.

**Tensions possibles** : Le risque de l'ego dans le travail de service ou de négliger les tâches ingrates mais nécessaires.

**Conseil clé** : Exceller dans ton travail quotidien tout en restant humble et au service.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu peux élever la qualité de ton travail.",
            'week_2': "Apporte ta touche unique à tes routines.",
            'week_3': "Inspire tes collègues par ton exemple.",
            'week_4': "Célèbre l'excellence dans l'ordinaire."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Optimisation parfaite**

Ta Lune en Verseau apporte des idées innovantes, ton Ascendant Vierge les applique avec précision. Ton quotidien devient un laboratoire d'amélioration continue.

**Domaine activé** : Maison 6 — Ton travail, ta santé, tes routines sont en perfectionnement constant. Tu veux l'excellence pratique.

**Ton approche instinctive** : Tu analyses chaque aspect de ton quotidien pour l'optimiser. Ton approche est à la fois méthodique et visionnaire.

**Tensions possibles** : Le risque de la sur-optimisation ou de l'anxiété par perfectionnisme. Tu peux te perdre dans les détails.

**Conseil clé** : Viser le progrès constant plutôt que la perfection absolue.""",
        'weekly_advice': {
            'week_1': "Audite une dimension de ton quotidien (travail, santé, routines).",
            'week_2': "Identifie les inefficacités et les opportunités d'amélioration.",
            'week_3': "Implémente une optimisation concrète.",
            'week_4': "Mesure les résultats et ajuste si nécessaire."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Travail harmonieux**

Double air : tu veux un quotidien équilibré et des relations de travail saines. L'efficacité passe par l'harmonie pour toi.

**Domaine activé** : Maison 6 — Ton travail, tes routines, ta santé cherchent plus d'équilibre et de beauté.

**Ton approche instinctive** : Tu crées un environnement de travail agréable. Tu sais collaborer efficacement tout en gardant ton originalité.

**Tensions possibles** : Le risque de sacrifier l'efficacité pour l'harmonie ou d'éviter les conflits nécessaires au travail.

**Conseil clé** : Maintenir l'équilibre sans compromettre la qualité du travail.""",
        'weekly_advice': {
            'week_1': "Évalue l'équilibre dans ton quotidien professionnel.",
            'week_2': "Améliore ton environnement de travail esthétiquement.",
            'week_3': "Facilite la collaboration harmonieuse.",
            'week_4': "Célèbre l'équilibre créé."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Transformation quotidienne**

Ta Lune en Verseau veut optimiser ton quotidien, ton Ascendant Scorpion veut transformer profondément tes habitudes et ta relation au travail.

**Domaine activé** : Maison 6 — Ton travail, ta santé, tes routines sont en mutation radicale. Tu veux éliminer ce qui ne sert plus.

**Ton approche instinctive** : Tu plonges dans les dysfonctionnements de ton quotidien pour les comprendre et les transformer de la racine.

**Tensions possibles** : Le risque de l'obsession du travail ou des rituels de santé trop extrêmes. Tes transformations peuvent être brutales.

**Conseil clé** : Transformer progressivement sans tout détruire d'un coup.""",
        'weekly_advice': {
            'week_1': "Identifie une habitude toxique dans ton quotidien.",
            'week_2': "Comprends ses racines profondes.",
            'week_3': "Prends une décision radicale pour t'en libérer.",
            'week_4': "Consolide ta nouvelle routine transformée."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Routine expansive**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent besoin de sens et de liberté dans ton quotidien. Tu veux un travail qui élargit tes horizons.

**Domaine activé** : Maison 6 — Ton travail, tes routines, ta santé cherchent plus de signification et de variété.

**Ton approche instinctive** : Tu explores de nouvelles méthodes de travail avec enthousiasme. Tu veux que ton quotidien soit une aventure.

**Tensions possibles** : Le risque de négliger les tâches répétitives mais nécessaires. Tu peux manquer de discipline dans les routines.

**Conseil clé** : Trouver le sens même dans les tâches ordinaires pour maintenir ta motivation.""",
        'weekly_advice': {
            'week_1': "Identifie le sens profond de ton travail quotidien.",
            'week_2': "Explore une nouvelle approche ou méthode.",
            'week_3': "Intègre de la variété dans tes routines.",
            'week_4': "Célèbre l'apprentissage continu dans l'ordinaire."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Discipline innovante**

Ta Lune en Verseau veut innover dans ton quotidien, ton Ascendant Capricorne veut construire des routines solides et productives.

**Domaine activé** : Maison 6 — Ton travail, ta santé, tes habitudes quotidiennes sont en restructuration stratégique.

**Ton approche instinctive** : Tu planifies méthodiquement l'amélioration de ton quotidien. Tu veux des routines efficaces et durables.

**Tensions possibles** : Le conflit entre rigidité et besoin de changement. Tu peux te sentir prisonnier de tes propres structures.

**Conseil clé** : Construire des routines qui intègrent la flexibilité nécessaire à l'innovation.""",
        'weekly_advice': {
            'week_1': "Évalue l'efficacité de tes routines actuelles.",
            'week_2': "Planifie une amélioration structurée.",
            'week_3': "Implémente avec discipline.",
            'week_4': "Mesure les gains de productivité et bien-être."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Quotidien futuriste**

Double Verseau sur ton travail et ta santé : tu veux réinventer complètement ton quotidien. Les routines conventionnelles ne te correspondent plus.

**Domaine activé** : Maison 6 — Ton travail, tes habitudes, ta santé sont en pleine expérimentation. Tu explores des méthodes alternatives.

**Ton approche instinctive** : Tu testes des approches avant-gardistes : travail asynchrone, biohacking, productivité non-conventionnelle.

**Tensions possibles** : Le risque de l'instabilité dans ton quotidien ou de négliger les bases par excès d'expérimentation.

**Conseil clé** : Innover tout en maintenant une structure minimale qui assure ta stabilité.""",
        'weekly_advice': {
            'week_1': "Imagine ton quotidien idéal sans contraintes.",
            'week_2': "Recherche des modèles alternatifs de travail et santé.",
            'week_3': "Expérimente une approche non-conventionnelle.",
            'week_4': "Évalue ce qui fonctionne pour toi."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Service inspiré**

Ta Lune en Verseau veut optimiser ton quotidien, ton Ascendant Poissons veut que ton travail ait une dimension spirituelle ou artistique.

**Domaine activé** : Maison 6 — Ton travail, tes routines, ta santé cherchent à intégrer plus d'intuition et de sens spirituel.

**Ton approche instinctive** : Tu laisses ton intuition guider l'organisation de ton quotidien. Ton travail devient une pratique méditative.

**Tensions possibles** : Le risque du flou dans tes routines ou de la procrastination. Tu peux manquer de structure pratique.

**Conseil clé** : Ancrer ton inspiration dans des routines concrètes et mesurables.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition sur ce que ton corps et ton âme ont besoin.",
            'week_2': "Crée des routines qui nourrissent ton bien-être holistique.",
            'week_3': "Intègre la méditation ou l'art dans ton quotidien.",
            'week_4': "Célèbre le sacré dans l'ordinaire."
        }
    },

    # ==================== MAISON 7 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Partenariat libre**

Ta Lune en Verseau en Maison 7 questionne tes relations, ton besoin de partenariat. L'Ascendant Bélier te pousse à affirmer ton indépendance même dans le couple.

**Domaine activé** : Maison 7 — Tes relations intimes, partenariats, contrats. Tu veux des connexions qui respectent ta liberté.

**Ton approche instinctive** : Tu refuses les relations qui t'étouffent. Tu cherches un partenariat d'égaux, basé sur l'autonomie mutuelle.

**Tensions possibles** : Le risque de fuir l'engagement par peur de perdre ta liberté. Tu peux être trop indépendant pour créer de l'intimité.

**Conseil clé** : Trouver l'équilibre entre autonomie et connexion authentique.""",
        'weekly_advice': {
            'week_1': "Définis ce que liberté signifie pour toi en relation.",
            'week_2': "Communique tes besoins d'indépendance clairement.",
            'week_3': "Explore une nouvelle forme de partenariat.",
            'week_4': "Célèbre l'autonomie au sein de la connexion."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Engagement progressif**

Ta Lune en Verseau veut des relations non-conventionnelles, ton Ascendant Taureau veut de la stabilité et de la sécurité dans le couple.

**Domaine activé** : Maison 7 — Tes partenariats cherchent un équilibre entre innovation et stabilité.

**Ton approche instinctive** : Tu construis lentement des relations qui respectent à la fois ton besoin de nouveauté et ton besoin de sécurité.

**Tensions possibles** : Le conflit entre désir de liberté et besoin d'engagement. Tu peux hésiter à t'engager pleinement.

**Conseil clé** : Créer des partenariats qui évoluent progressivement vers plus de profondeur.""",
        'weekly_advice': {
            'week_1': "Évalue si tes relations te nourrissent vraiment.",
            'week_2': "Identifie ce qui pourrait évoluer positivement.",
            'week_3': "Fais un pas vers plus d'authenticité relationnelle.",
            'week_4': "Ancre les nouvelles dynamiques créées."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Amitié amoureuse**

Double air : tu veux des partenariats basés sur la stimulation intellectuelle et la communication. L'amitié est la base de tes relations intimes.

**Domaine activé** : Maison 7 — Tes partenariats deviennent plus légers, plus communicatifs, plus variés.

**Ton approche instinctive** : Tu cherches un partenaire qui soit aussi ton meilleur ami, avec qui tu peux tout discuter sans tabou.

**Tensions possibles** : Le risque d'intellectualiser les émotions ou de manquer de profondeur dans l'intimité.

**Conseil clé** : Équilibrer stimulation intellectuelle et connexion émotionnelle dans tes relations.""",
        'weekly_advice': {
            'week_1': "Engage une conversation profonde avec ton partenaire ou un proche.",
            'week_2': "Explore de nouveaux sujets ensemble.",
            'week_3': "Partage aussi tes émotions, pas que tes idées.",
            'week_4': "Célèbre la qualité de vos échanges."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Intimité libre**

Ta Lune en Verseau veut de l'indépendance, ton Ascendant Cancer veut de la sécurité émotionnelle. Tu cherches un partenariat qui offre les deux.

**Domaine activé** : Maison 7 — Tes relations intimes oscillent entre besoin de fusion et besoin de liberté.

**Ton approche instinctive** : Tu veux créer un espace relationnel sécurisant qui respecte l'individualité de chacun.

**Tensions possibles** : Le conflit entre attachement et détachement. Tu peux te sentir déchiré entre ces deux besoins.

**Conseil clé** : Créer une sécurité émotionnelle qui n'étouffe pas la liberté.""",
        'weekly_advice': {
            'week_1': "Identifie tes besoins émotionnels en relation.",
            'week_2': "Communique-les avec vulnérabilité.",
            'week_3': "Respecte aussi le besoin d'espace de l'autre.",
            'week_4': "Cultive une intimité qui libère."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Partenariat inspirant**

Opposition Verseau-Lion : tu veux un partenariat où chacun brille individuellement tout en créant quelque chose ensemble.

**Domaine activé** : Maison 7 — Tes relations cherchent un équilibre entre individualité et union.

**Ton approche instinctive** : Tu cherches un partenaire qui te célèbre et que tu peux célébrer. Vous vous inspirez mutuellement.

**Tensions possibles** : Le risque de la compétition dans le couple ou du besoin de reconnaissance qui éclipse le partenariat.

**Conseil clé** : Briller ensemble plutôt que l'un contre l'autre.""",
        'weekly_advice': {
            'week_1': "Identifie comment vous pouvez vous élever mutuellement.",
            'week_2': "Célèbre les succès de ton partenaire.",
            'week_3': "Créez un projet commun inspirant.",
            'week_4': "Reconnais la force de votre union."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Partenariat amélioré**

Ta Lune en Verseau veut innover dans tes relations, ton Ascendant Vierge veut qu'elles fonctionnent efficacement.

**Domaine activé** : Maison 7 — Tes partenariats sont en optimisation. Tu veux des relations qui soient à la fois saines et originales.

**Ton approche instinctive** : Tu analyses tes relations pour les améliorer. Tu communiques clairement sur ce qui fonctionne et ce qui ne fonctionne pas.

**Tensions possibles** : Le risque de sur-analyser ou de critiquer au lieu d'accepter. Tes partenariats peuvent devenir trop mentaux.

**Conseil clé** : Améliorer sans perdre la spontanéité et l'acceptation.""",
        'weekly_advice': {
            'week_1': "Évalue objectivement la santé de tes relations principales.",
            'week_2': "Identifie une amélioration constructive possible.",
            'week_3': "Communique-la avec bienveillance.",
            'week_4': "Apprécie les progrès réalisés ensemble."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre réinventé**

Double air : les relations sont ton terrain de jeu et d'évolution. Tu veux créer de nouvelles formes de partenariat harmonieux.

**Domaine activé** : Maison 7 — Tes relations intimes, contrats, partenariats cherchent plus d'équilibre et d'originalité.

**Ton approche instinctive** : Tu négocies naturellement des accords relationnels innovants. Tu sais créer l'harmonie tout en respectant l'unicité.

**Tensions possibles** : Le risque de perdre ton individualité dans le compromis ou d'idéaliser les relations.

**Conseil clé** : Créer l'harmonie sans te sacrifier.""",
        'weekly_advice': {
            'week_1': "Évalue l'équilibre dans tes relations principales.",
            'week_2': "Propose un ajustement qui honore les deux parties.",
            'week_3': "Expérimente une nouvelle forme de partenariat.",
            'week_4': "Célèbre l'harmonie créée ensemble."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Intimité transformée**

Ta Lune en Verseau veut de la liberté, ton Ascendant Scorpion veut de la fusion. Tu cherches une intimité profonde qui ne t'emprisonne pas.

**Domaine activé** : Maison 7 — Tes partenariats sont en transformation radicale. Tu veux aller au fond des choses relationnellement.

**Ton approche instinctive** : Tu explores les dynamiques de pouvoir, les attachements, les tabous dans tes relations.

**Tensions possibles** : Le conflit entre besoin de contrôle et besoin de liberté. Tes relations peuvent être intenses et instables.

**Conseil clé** : Transformer tes relations en libérant les attachements toxiques sans fuir l'intimité.""",
        'weekly_advice': {
            'week_1': "Identifie un pattern relationnel qui te limite.",
            'week_2': "Explore-le avec honnêteté et courage.",
            'week_3': "Prends une décision libératrice.",
            'week_4': "Cultive une intimité plus saine."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Partenariat aventurier**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent besoin de liberté et d'exploration dans tes relations.

**Domaine activé** : Maison 7 — Tes partenariats cherchent plus de sens, de liberté, d'aventure partagée.

**Ton approche instinctive** : Tu veux un partenaire qui soit aussi un compagnon d'aventure. Vous explorez le monde ensemble.

**Tensions possibles** : Le risque de fuir l'engagement par besoin d'espace. Tu peux avoir du mal avec les contraintes relationnelles.

**Conseil clé** : Créer un partenariat qui soit une aventure, pas une cage.""",
        'weekly_advice': {
            'week_1': "Définis ce que liberté signifie pour toi en couple.",
            'week_2': "Planifiez une exploration ou aventure ensemble.",
            'week_3': "Discutez de vos visions d'avenir respectives.",
            'week_4': "Célèbrez la liberté au sein de votre union."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Engagement moderne**

Ta Lune en Verseau veut réinventer le partenariat, ton Ascendant Capricorne veut construire quelque chose de solide.

**Domaine activé** : Maison 7 — Tes relations cherchent un équilibre entre tradition et innovation, entre engagement et liberté.

**Ton approche instinctive** : Tu veux un partenariat sérieux mais non-conventionnel. Vous construisez ensemble avec une vision unique.

**Tensions possibles** : Le conflit entre besoin de structure et besoin de liberté. Tu peux te sentir tiraillé.

**Conseil clé** : Créer des accords relationnels qui soient à la fois solides et respectueux de votre unicité.""",
        'weekly_advice': {
            'week_1': "Évalue ce que tu veux construire à long terme en relation.",
            'week_2': "Communique tes engagements et tes limites clairement.",
            'week_3': "Créez une structure relationnelle qui vous ressemble.",
            'week_4': "Consolidez vos fondations uniques."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Relation révolutionnaire**

Double Verseau sur tes partenariats : tu veux réinventer complètement les relations. Le modèle conventionnel ne t'intéresse pas.

**Domaine activé** : Maison 7 — Tes partenariats, contrats, relations intimes sont en pleine expérimentation. Tu explores de nouvelles formes d'union.

**Ton approche instinctive** : Tu cherches des relations polyamoureuses, des partenariats non-exclusifs, des accords personnalisés. La liberté est non-négociable.

**Tensions possibles** : Le risque de l'instabilité relationnelle ou de la peur de l'intimité déguisée en besoin de liberté.

**Conseil clé** : Innover dans tes relations tout en acceptant une certaine vulnérabilité.""",
        'weekly_advice': {
            'week_1': "Définis ton modèle relationnel idéal sans censure.",
            'week_2': "Recherche des exemples de relations alternatives.",
            'week_3': "Communique authentiquement tes besoins relationnels.",
            'week_4': "Connecte avec des personnes qui partagent ta vision."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Union spirituelle**

Ta Lune en Verseau veut une relation libre, ton Ascendant Poissons veut une fusion spirituelle. Tu cherches une connexion transcendante.

**Domaine activé** : Maison 7 — Tes partenariats cherchent à intégrer liberté individuelle et communion spirituelle.

**Ton approche instinctive** : Tu veux un partenaire avec qui tu partages une vision spirituelle ou artistique. Votre relation sert quelque chose de plus grand.

**Tensions possibles** : Le risque de l'idéalisation ou du flou dans les limites relationnelles. Tu peux te perdre dans l'autre.

**Conseil clé** : Créer une union qui transcende tout en respectant les individualités.""",
        'weekly_advice': {
            'week_1': "Partage ta vision spirituelle ou créative avec ton partenaire.",
            'week_2': "Créez un rituel ou pratique commune.",
            'week_3': "Respecte aussi les besoins d'indépendance de chacun.",
            'week_4': "Célèbre la connexion spirituelle unique que vous partagez."
        }
    },

    # ==================== MAISON 8 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Transformation radicale**

Ta Lune en Verseau en Maison 8 te pousse à transformer ta relation au pouvoir, à l'intimité, aux ressources partagées. L'Ascendant Bélier ajoute le courage d'aller au fond.

**Domaine activé** : Maison 8 — Transformation, intimité profonde, ressources partagées, tabous. Tu veux libérer ce qui était enfoui.

**Ton approche instinctive** : Tu explores les zones d'ombre sans peur. Tu veux comprendre les mécanismes cachés et les transformer.

**Tensions possibles** : Le risque de la brutalité dans la transformation ou de rejeter trop vite ce qui pourrait être guéri.

**Conseil clé** : Transformer avec courage mais aussi avec compassion pour toi-même.""",
        'weekly_advice': {
            'week_1': "Identifie un attachement ou peur qui te limite.",
            'week_2': "Explore son origine avec honnêteté.",
            'week_3': "Prends une décision libératrice courageuse.",
            'week_4': "Célèbre ta transformation intérieure."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sécurité partagée**

Ta Lune en Verseau veut transformer ta relation aux ressources partagées, ton Ascendant Taureau veut de la stabilité financière et émotionnelle.

**Domaine activé** : Maison 8 — Argent partagé, héritages, intimité profonde cherchent un équilibre entre transformation et sécurité.

**Ton approche instinctive** : Tu veux construire progressivement une base solide dans tes partenariats financiers et émotionnels.

**Tensions possibles** : Le conflit entre besoin de contrôle sur les ressources et désir de partage équitable.

**Conseil clé** : Créer des accords financiers et émotionnels qui sécurisent tout en permettant la croissance.""",
        'weekly_advice': {
            'week_1': "Évalue la santé de tes ressources partagées.",
            'week_2': "Communique sur les besoins de sécurité mutuelle.",
            'week_3': "Crée des accords clairs et équitables.",
            'week_4': "Ancre la confiance dans le partage."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Mystères intellectuels**

Double air : tu veux comprendre intellectuellement les profondeurs. Les tabous, la psychologie, l'ésotérisme t'intéressent sur le plan conceptuel.

**Domaine activé** : Maison 8 — Transformation, intimité, ressources partagées deviennent des sujets de curiosité intellectuelle.

**Ton approche instinctive** : Tu explores les zones d'ombre en les analysant, en lisant, en discutant. Cette approche peut manquer de profondeur émotionnelle.

**Tensions possibles** : Le risque d'intellectualiser ce qui devrait être ressenti. Tu peux éviter la vraie transformation.

**Conseil clé** : Laisser l'expérience émotionnelle accompagner la compréhension intellectuelle.""",
        'weekly_advice': {
            'week_1': "Explore un sujet tabou intellectuellement.",
            'week_2': "Engage une conversation profonde sur ce sujet.",
            'week_3': "Permets-toi de ressentir, pas juste de comprendre.",
            'week_4': "Intègre ce que tu as appris sur toi-même."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Guérison profonde**

Ta Lune en Verseau veut transformer objectivement, ton Ascendant Cancer ressent profondément les blessures à guérir.

**Domaine activé** : Maison 8 — Transformation émotionnelle, intimité, ressources partagées sont au cœur de ton processus de guérison.

**Ton approche instinctive** : Tu veux comprendre tes blessures pour les libérer. Cette combinaison permet une guérison à la fois lucide et compassionnée.

**Tensions possibles** : Le conflit entre détachement et attachement émotionnel. Tu peux osciller entre les deux.

**Conseil clé** : Honorer tes émotions tout en gardant la perspective nécessaire à la transformation.""",
        'weekly_advice': {
            'week_1': "Identifie une blessure émotionnelle prête à être guérie.",
            'week_2': "Accueille les émotions qui émergent avec douceur.",
            'week_3': "Trouve une nouvelle perspective libératrice.",
            'week_4': "Célèbre ta guérison progressive."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Pouvoir transformé**

Ta Lune en Verseau veut libérer le pouvoir collectif, ton Ascendant Lion veut exprimer ton pouvoir personnel. Tu cherches l'équilibre.

**Domaine activé** : Maison 8 — Pouvoir, transformation, ressources partagées deviennent des terrains d'exploration de ton leadership.

**Ton approche instinctive** : Tu veux transformer les dynamiques de pouvoir pour qu'elles soient plus justes. Ton charisme aide cette transformation.

**Tensions possibles** : Le risque de l'ego dans les zones d'ombre ou du besoin de contrôle déguisé en altruisme.

**Conseil clé** : Utiliser ton pouvoir personnel pour servir la transformation collective.""",
        'weekly_advice': {
            'week_1': "Identifie où tu as du pouvoir et comment tu l'utilises.",
            'week_2': "Explore tes motivations profondes avec honnêteté.",
            'week_3': "Transforme ta relation au pouvoir vers plus de service.",
            'week_4': "Célèbre l'impact positif de ton leadership."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Analyse transformatrice**

Ta Lune en Verseau veut transformer, ton Ascendant Vierge veut comprendre précisément comment. L'analyse devient un outil de libération.

**Domaine activé** : Maison 8 — Transformation, intimité, ressources partagées sont décortiquées pour être optimisées.

**Ton approche instinctive** : Tu analyses tes patterns psychologiques avec précision. Cette lucidité facilite la transformation.

**Tensions possibles** : Le risque de sur-analyser sans passer à l'action transformatrice. L'intellect peut bloquer le processus.

**Conseil clé** : Utiliser ton analyse comme point de départ, puis laisser la transformation opérer.""",
        'weekly_advice': {
            'week_1': "Analyse un pattern récurrent qui te limite.",
            'week_2': "Identifie sa fonction et son origine.",
            'week_3': "Prends une action concrète pour le transformer.",
            'week_4': "Mesure les changements observables."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Justice profonde**

Double air : tu veux transformer les dynamiques de pouvoir dans tes relations pour créer plus d'équité et d'harmonie.

**Domaine activé** : Maison 8 — Intimité profonde, ressources partagées, transformation relationnelle cherchent plus d'équilibre.

**Ton approche instinctive** : Tu négocies des accords équitables sur les ressources et le pouvoir partagés. Tu veux la justice même dans l'intime.

**Tensions possibles** : Le risque d'éviter les conflits nécessaires à la transformation. Tu peux chercher l'harmonie au détriment de la vérité.

**Conseil clé** : Accepter que la vraie transformation passe parfois par le conflit constructif.""",
        'weekly_advice': {
            'week_1': "Évalue l'équité dans tes relations intimes.",
            'week_2': "Identifie les déséquilibres de pouvoir ou ressources.",
            'week_3': "Engage une conversation honnête pour rééquilibrer.",
            'week_4': "Célèbre la nouvelle harmonie créée."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Alchimie radicale**

Ta Lune en Verseau veut libérer, ton Ascendant Scorpion veut transformer profondément. Cette combinaison est puissamment transformatrice.

**Domaine activé** : Maison 8 — Transformation, mort et renaissance, intimité profonde sont au cœur de ton expérience ce mois-ci.

**Ton approche instinctive** : Tu plonges sans peur dans les profondeurs pour en ramener des trésors transformés. Cette intensité est libératrice.

**Tensions possibles** : Le risque de l'obsession ou de la transformation trop brutale. Tu peux vouloir tout changer d'un coup.

**Conseil clé** : Respecter le timing naturel de la transformation, même si tu es impatient.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui est prêt à mourir en toi.",
            'week_2': "Laisse ce processus de mort opérer.",
            'week_3': "Accueille ce qui émerge de nouveau.",
            'week_4': "Célèbre ta renaissance."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Philosophie profonde**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent une approche philosophique de la transformation et des mystères de la vie.

**Domaine activé** : Maison 8 — Transformation, spiritualité profonde, ressources partagées sont explorées avec optimisme et ouverture.

**Ton approche instinctive** : Tu cherches le sens dans tes transformations. Les crises deviennent des opportunités d'expansion spirituelle.

**Tensions possibles** : Le risque d'éviter la vraie profondeur en restant dans l'optimisme philosophique. Tu peux manquer d'ancrage émotionnel.

**Conseil clé** : Descendre vraiment dans les profondeurs avant de chercher le sens.""",
        'weekly_advice': {
            'week_1': "Explore une crise ou transformation avec curiosité.",
            'week_2': "Cherche la leçon spirituelle qu'elle contient.",
            'week_3': "Intègre cette sagesse dans ta philosophie de vie.",
            'week_4': "Partage ce que tu as appris avec générosité."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Restructuration profonde**

Ta Lune en Verseau veut transformer radicalement, ton Ascendant Capricorne veut reconstruire solidement après la transformation.

**Domaine activé** : Maison 8 — Transformation, ressources partagées, pouvoir sont restructurés méthodiquement.

**Ton approche instinctive** : Tu déconstruis ce qui ne fonctionne plus puis tu reconstruis avec discipline. Cette approche est durable.

**Tensions possibles** : Le conflit entre besoin de contrôle et acceptation de la transformation imprévisible.

**Conseil clé** : Lâcher le contrôle suffisamment pour permettre la vraie transformation.""",
        'weekly_advice': {
            'week_1': "Identifie une structure (croyance, relation, système) qui s'effondre.",
            'week_2': "Accepte cet effondrement comme nécessaire.",
            'week_3': "Commence à reconstruire sur de nouvelles bases.",
            'week_4': "Consolide tes nouvelles fondations."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Libération totale**

Double Verseau sur ta transformation : tu veux te libérer complètement de tous les attachements, peurs, conditionnements. C'est radical.

**Domaine activé** : Maison 8 — Transformation profonde, intimité, ressources partagées sont en pleine révolution. Tu veux tout libérer.

**Ton approche instinctive** : Tu explores les tabous, les zones d'ombre avec détachement. Tu veux comprendre pour te libérer.

**Tensions possibles** : Le risque du détachement excessif ou de la fuite de l'intimité vraie. Tu peux intellectualiser la transformation.

**Conseil clé** : Permettre la vulnérabilité nécessaire à la vraie transformation.""",
        'weekly_advice': {
            'week_1': "Identifie tous les attachements qui te limitent.",
            'week_2': "Explore un tabou personnel avec courage.",
            'week_3': "Prends une décision radicalement libératrice.",
            'week_4': "Célèbre ta nouvelle liberté intérieure."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 8, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Transcendance mystique**

Ta Lune en Verseau veut libérer, ton Ascendant Poissons veut dissoudre dans l'universel. Ta transformation est spirituelle et compassionnée.

**Domaine activé** : Maison 8 — Transformation, spiritualité profonde, mort de l'ego cherchent une expression transcendante.

**Ton approche instinctive** : Tu laisses aller avec foi. Ton intuition te guide dans ta transformation. Cette approche est douce mais puissante.

**Tensions possibles** : Le risque de la confusion ou de la perte de limites. Tu peux te dissoudre sans te reconstruire.

**Conseil clé** : Ancrer ta transformation spirituelle dans ton corps et ta vie concrète.""",
        'weekly_advice': {
            'week_1': "Médite sur ce qui est prêt à être libéré.",
            'week_2': "Laisse aller avec confiance et compassion.",
            'week_3': "Accueille le vide créateur qui émerge.",
            'week_4': "Laisse une nouvelle version de toi naître naturellement."
        }
    },

    # ==================== MAISON 9 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Explorateur visionnaire**

Ta Lune en Verseau en Maison 9 t'appelle à explorer de nouvelles philosophies, cultures, horizons. L'Ascendant Bélier ajoute l'audace du pionnier.

**Domaine activé** : Maison 9 — Philosophie, voyages, études supérieures, spiritualité. Tu veux élargir ta vision du monde de manière audacieuse.

**Ton approche instinctive** : Tu fonces vers l'inconnu intellectuel et géographique. Les idées avant-gardistes et les voyages atypiques t'attirent.

**Tensions possibles** : Le risque de te disperser dans trop de directions sans approfondir. L'impatience peut te faire manquer la profondeur.

**Conseil clé** : Choisir une direction d'exploration et s'y engager pleinement ce mois-ci.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui élargit vraiment ta perspective.",
            'week_2': "Engage-toi dans une exploration intellectuelle ou géographique.",
            'week_3': "Partage ce que tu découvres avec enthousiasme.",
            'week_4': "Intègre cette nouvelle sagesse dans ta vie."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sagesse ancrée**

Ta Lune en Verseau veut explorer de nouvelles philosophies, ton Ascendant Taureau veut que cette sagesse soit pratique et durable.

**Domaine activé** : Maison 9 — Ta quête de sens, tes études, tes voyages cherchent un équilibre entre ouverture et ancrage.

**Ton approche instinctive** : Tu explores lentement mais profondément. Tu veux intégrer vraiment ce que tu apprends, pas juste l'accumuler.

**Tensions possibles** : Le conflit entre désir d'exploration et besoin de sécurité. Tu peux hésiter à sortir de ta zone de confort intellectuelle.

**Conseil clé** : Oser l'exploration tout en gardant des racines solides.""",
        'weekly_advice': {
            'week_1': "Choisis un sujet qui élargit ta vision du monde.",
            'week_2': "Étudie-le avec patience et profondeur.",
            'week_3': "Trouve des applications concrètes à cette sagesse.",
            'week_4': "Ancre ces nouvelles connaissances dans ta vie."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Érudit voyageur**

Double air : ta soif de connaissance et d'exploration est immense. Tu veux tout apprendre sur tout, voyager partout, comprendre toutes les perspectives.

**Domaine activé** : Maison 9 — Philosophie, voyages, études deviennent des terrains de jeu intellectuel infini.

**Ton approche instinctive** : Tu explores avec légèreté et curiosité. Tu connectes des idées de cultures et disciplines différentes avec aisance.

**Tensions possibles** : Le risque de rester en surface dans ton exploration. Tu peux papillonner sans jamais développer une vraie expertise.

**Conseil clé** : Approfondir au moins un domaine de sagesse ce mois-ci.""",
        'weekly_advice': {
            'week_1': "Explore librement tous les sujets qui t'intéressent.",
            'week_2': "Identifie celui qui résonne le plus profondément.",
            'week_3': "Approfondis cette direction spécifiquement.",
            'week_4': "Partage ta synthèse originale."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Philosophe empathique**

Ta Lune en Verseau cherche la vérité universelle, ton Ascendant Cancer veut que cette philosophie inclue l'humain et l'émotionnel.

**Domaine activé** : Maison 9 — Ta quête de sens, tes voyages, ta spiritualité oscillent entre détachement intellectuel et sensibilité.

**Ton approche instinctive** : Tu cherches une sagesse qui soit à la fois universelle et profondément humaine. Cette combinaison est rare et précieuse.

**Tensions possibles** : Le conflit entre objectivité philosophique et implication émotionnelle. Tu peux te sentir déchiré.

**Conseil clé** : Intégrer tête et cœur dans ta quête de sens.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie ou spiritualité qui honore les émotions.",
            'week_2': "Connecte intellectuellement et émotionnellement avec cette sagesse.",
            'week_3': "Applique-la dans tes relations et ta vie quotidienne.",
            'week_4': "Partage cette sagesse avec compassion."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Enseignant inspirant**

Ta Lune en Verseau veut partager des idées révolutionnaires, ton Ascendant Lion veut inspirer et éduquer avec charisme.

**Domaine activé** : Maison 9 — Philosophie, enseignement, voyages deviennent des moyens d'exprimer ta vision et ton leadership.

**Ton approche instinctive** : Tu partages tes découvertes avec confiance et générosité. Ton enthousiasme pour la sagesse est contagieux.

**Tensions possibles** : Le risque de l'ego intellectuel ou du besoin d'être reconnu comme sage. Tu peux enseigner pour briller plutôt que servir.

**Conseil clé** : Utiliser ton charisme pour transmettre des vérités qui te dépassent.""",
        'weekly_advice': {
            'week_1': "Identifie une sagesse importante à partager.",
            'week_2': "Trouve la manière la plus impactante de l'enseigner.",
            'week_3': "Partage publiquement avec authenticité.",
            'week_4': "Célèbre l'impact positif de ton enseignement."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Sagesse appliquée**

Ta Lune en Verseau explore des idées visionnaires, ton Ascendant Vierge veut les rendre pratiques et utiles au quotidien.

**Domaine activé** : Maison 9 — Philosophie, études, voyages cherchent à être à la fois inspirants et applicables.

**Ton approche instinctive** : Tu analyses les grandes théories pour en extraire les principes pratiques. Ta sagesse est utilisable.

**Tensions possibles** : Le risque de perdre la vision d'ensemble dans les détails ou d'être trop critique envers les philosophies imparfaites.

**Conseil clé** : Équilibrer idéalisme et pragmatisme dans ta quête de sagesse.""",
        'weekly_advice': {
            'week_1': "Étudie une philosophie ou système de pensée.",
            'week_2': "Identifie ses applications pratiques concrètes.",
            'week_3': "Teste ces principes dans ta vie quotidienne.",
            'week_4': "Affine ton système personnel de sagesse applicable."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomate culturel**

Double air : tu veux créer des ponts entre les cultures, les philosophies, les perspectives. L'harmonie interculturelle t'inspire.

**Domaine activé** : Maison 9 — Voyages, études, philosophie deviennent des moyens de créer plus de compréhension et d'équité dans le monde.

**Ton approche instinctive** : Tu explores avec ouverture et tu facilites le dialogue entre perspectives différentes. Cette capacité est précieuse.

**Tensions possibles** : Le risque de diluer ta propre perspective dans le compromis. Tu peux perdre tes convictions.

**Conseil clé** : Rester ouvert tout en affirmant ta propre philosophie.""",
        'weekly_advice': {
            'week_1': "Explore une culture ou perspective radicalement différente.",
            'week_2': "Cherche les points communs avec ta propre vision.",
            'week_3': "Crée un dialogue ou échange interculturel.",
            'week_4': "Célèbre la richesse de la diversité."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité profonde**

Ta Lune en Verseau cherche la vérité universelle, ton Ascendant Scorpion veut aller au fond des mystères spirituels et philosophiques.

**Domaine activé** : Maison 9 — Philosophie, spiritualité, quête de sens deviennent des explorations intenses et transformatrices.

**Ton approche instinctive** : Tu ne te contentes pas des réponses superficielles. Tu veux comprendre les vérités cachées, les mystères profonds.

**Tensions possibles** : Le risque de l'obsession intellectuelle ou du rejet de ce qui ne peut être prouvé. Tu peux être trop intense.

**Conseil clé** : Équilibrer quête de vérité et acceptation du mystère.""",
        'weekly_advice': {
            'week_1': "Identifie une question existentielle qui te hante.",
            'week_2': "Explore-la sans peur, en profondeur.",
            'week_3': "Accepte que certaines réponses restent mystérieuses.",
            'week_4': "Intègre la sagesse gagnée dans ta transformation."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventurier philosophe**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent une soif insatiable d'exploration, de connaissance, de sens. Tu es l'éternel chercheur.

**Domaine activé** : Maison 9 — Philosophie, voyages, spiritualité, études sont au cœur de ton expérience. Tu veux tout explorer.

**Ton approche instinctive** : Tu pars à l'aventure intellectuelle et géographique avec enthousiasme. Ton optimisme ouvre des portes.

**Tensions possibles** : Le risque de te disperser sans jamais approfondir ou d'être trop confiant dans tes convictions.

**Conseil clé** : Choisir une direction d'exploration et s'y engager vraiment.""",
        'weekly_advice': {
            'week_1': "Définis ta quête personnelle ce mois-ci.",
            'week_2': "Lance-toi dans une exploration audacieuse.",
            'week_3': "Partage tes découvertes généreusement.",
            'week_4': "Intègre cette sagesse dans ta philosophie de vie."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Sagesse structurée**

Ta Lune en Verseau explore des idées visionnaires, ton Ascendant Capricorne veut construire un système de sagesse solide et durable.

**Domaine activé** : Maison 9 — Philosophie, études, spiritualité sont abordées avec sérieux et ambition à long terme.

**Ton approche instinctive** : Tu construis méthodiquement ta compréhension du monde. Tu veux une sagesse qui tienne la route.

**Tensions possibles** : Le conflit entre ouverture à la nouveauté et attachement aux systèmes établis. Tu peux être trop rigide intellectuellement.

**Conseil clé** : Rester ouvert à réviser tes convictions quand de nouvelles évidences apparaissent.""",
        'weekly_advice': {
            'week_1': "Évalue ta philosophie de vie actuelle.",
            'week_2': "Identifie ce qui mérite d'être ajusté ou approfondi.",
            'week_3': "Étudie sérieusement pour enrichir ta compréhension.",
            'week_4': "Consolide ton système de sagesse renouvelé."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Visionnaire universel**

Double Verseau sur ta philosophie : tu veux comprendre le futur de l'humanité, les possibilités d'évolution collective. Ta vision est radicalement avant-gardiste.

**Domaine activé** : Maison 9 — Philosophie, spiritualité, voyages, études sont en pleine révolution. Tu explores des paradigmes complètement nouveaux.

**Ton approche instinctive** : Tu t'intéresses aux technologies émergentes, aux nouvelles spiritualités, aux philosophies futuristes.

**Tensions possibles** : Le risque de perdre le contact avec la réalité présente ou d'être incompris dans ta vision.

**Conseil clé** : Ancrer ta vision du futur dans des actions présentes.""",
        'weekly_advice': {
            'week_1': "Explore librement les idées les plus avant-gardistes.",
            'week_2': "Identifie celles qui résonnent vraiment avec toi.",
            'week_3': "Trouve des moyens concrets de vivre selon cette vision.",
            'week_4': "Connecte avec d'autres visionnaires."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 9, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Mystique universel**

Ta Lune en Verseau cherche la vérité universelle, ton Ascendant Poissons veut la vivre spirituellement et intuitivement.

**Domaine activé** : Maison 9 — Spiritualité, philosophie, voyages deviennent des chemins vers le transcendant et l'universel.

**Ton approche instinctive** : Tu captes les vérités spirituelles par intuition puis tu les conceptualises. Cette combinaison est rare et puissante.

**Tensions possibles** : Le risque du flou philosophique ou de l'idéalisme déconnecté. Tes visions peuvent manquer d'ancrage.

**Conseil clé** : Ancrer tes intuitions spirituelles dans des pratiques et concepts partageables.""",
        'weekly_advice': {
            'week_1': "Médite sur les grandes questions de l'existence.",
            'week_2': "Laisse ton intuition te guider vers des réponses.",
            'week_3': "Trouve des mots pour exprimer ces vérités ineffables.",
            'week_4': "Partage ta sagesse mystique avec compassion."
        }
    },

    # ==================== MAISON 10 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Carrière pionnière**

Ta Lune en Verseau en Maison 10 t'appelle à réinventer ta carrière, ta mission publique. L'Ascendant Bélier ajoute le courage d'agir audacieusement.

**Domaine activé** : Maison 10 — Carrière, réputation, accomplissement public. Tu veux créer un impact qui brise les normes.

**Ton approche instinctive** : Tu prends des risques professionnels pour suivre ta vision. Tu veux être reconnu pour ton originalité et ton innovation.

**Tensions possibles** : Le risque de l'impatience ou du rejet de toute autorité. Tu peux vouloir tout changer trop vite.

**Conseil clé** : Canaliser ton audace vers une vision professionnelle claire et durable.""",
        'weekly_advice': {
            'week_1': "Définis ta vision professionnelle idéale.",
            'week_2': "Identifie une action courageuse vers cette vision.",
            'week_3': "Prends cette initiative sans attendre la permission.",
            'week_4': "Assume publiquement ton originalité professionnelle."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Succès authentique**

Ta Lune en Verseau veut une carrière non-conventionnelle, ton Ascendant Taureau veut construire quelque chose de solide et durable.

**Domaine activé** : Maison 10 — Ta carrière, ton accomplissement public cherchent un équilibre entre innovation et stabilité.

**Ton approche instinctive** : Tu construis progressivement une réputation basée sur tes valeurs uniques. Tu veux un succès qui te ressemble.

**Tensions possibles** : Le conflit entre désir de sécurité professionnelle et besoin d'authenticité. Tu peux hésiter à prendre des risques.

**Conseil clé** : Évoluer professionnellement sans compromettre tes valeurs fondamentales.""",
        'weekly_advice': {
            'week_1': "Évalue si ta carrière reflète vraiment tes valeurs.",
            'week_2': "Identifie un ajustement qui t'alignerait davantage.",
            'week_3': "Prends un pas concret vers cet alignement.",
            'week_4': "Consolide cette nouvelle direction professionnelle."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Carrière polyvalente**

Double air : tu veux une carrière qui stimule ton intellect et te permet d'explorer plusieurs domaines. La communication est clé.

**Domaine activé** : Maison 10 — Ta carrière, ta réputation publique cherchent plus de diversité et de stimulation intellectuelle.

**Ton approche instinctive** : Tu explores plusieurs pistes professionnelles simultanément. Ton adaptabilité est un atout.

**Tensions possibles** : Le risque de te disperser professionnellement sans développer une vraie expertise. Tu peux manquer de focus.

**Conseil clé** : Trouver un fil conducteur qui unifie tes divers intérêts professionnels.""",
        'weekly_advice': {
            'week_1': "Liste tous tes intérêts professionnels.",
            'week_2': "Identifie le thème commun qui les unit.",
            'week_3': "Crée une identité professionnelle qui intègre cette diversité.",
            'week_4': "Communique clairement ta proposition de valeur unique."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Mission humanitaire**

Ta Lune en Verseau veut une carrière qui serve le collectif, ton Ascendant Cancer veut prendre soin et nourrir. Tu combines les deux.

**Domaine activé** : Maison 10 — Ta carrière, ton impact public oscillent entre vision humaniste et sensibilité empathique.

**Ton approche instinctive** : Tu veux être reconnu pour ton impact humain et social. Ton professionnalisme est empreint de compassion.

**Tensions possibles** : Le risque de l'épuisement par surengagement dans ta mission. Tu peux te sacrifier professionnellement.

**Conseil clé** : Servir le collectif tout en préservant ton bien-être personnel.""",
        'weekly_advice': {
            'week_1': "Clarifie l'impact humain que tu veux avoir professionnellement.",
            'week_2': "Identifie comment nourrir cette mission sans t'épuiser.",
            'week_3': "Mets en place des limites saines dans ton engagement.",
            'week_4': "Célèbre l'impact positif de ton travail."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Leader visionnaire**

Ta Lune en Verseau veut servir le collectif, ton Ascendant Lion veut briller et inspirer. Tu deviens un leader d'une cause collective.

**Domaine activé** : Maison 10 — Ta carrière, ton leadership public cherchent un équilibre entre ego et altruisme.

**Ton approche instinctive** : Tu utilises ton charisme pour porter des idées innovantes. Les gens te suivent parce que tu incarnes une vision inspirante.

**Tensions possibles** : Le risque de chercher la reconnaissance plutôt que l'impact. Ton ego peut éclipser ta mission.

**Conseil clé** : Utiliser ta visibilité pour servir une cause plus grande que toi.""",
        'weekly_advice': {
            'week_1': "Identifie la cause collective que tu veux servir.",
            'week_2': "Prends une position publique claire sur ce sujet.",
            'week_3': "Utilise ton influence pour faire avancer cette cause.",
            'week_4': "Célèbre l'impact collectif créé, pas juste ta reconnaissance."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Excellence innovante**

Ta Lune en Verseau apporte des idées professionnelles originales, ton Ascendant Vierge les exécute avec excellence.

**Domaine activé** : Maison 10 — Ta carrière, ton accomplissement public cherchent à être à la fois innovants et impeccables.

**Ton approche instinctive** : Tu perfectionnes tes innovations. Ton travail est à la fois avant-gardiste et de haute qualité.

**Tensions possibles** : Le risque de la paralysie par perfectionnisme. Tu peux retarder ton impact en cherchant la perfection.

**Conseil clé** : Viser l'excellence sans que cela empêche l'innovation et la prise de risque.""",
        'weekly_advice': {
            'week_1': "Identifie une innovation professionnelle que tu veux introduire.",
            'week_2': "Planifie son implémentation avec soin.",
            'week_3': "Lance-la même si elle n'est pas parfaite.",
            'week_4': "Ajuste et améliore selon les retours."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomatie professionnelle**

Double air : tu veux une carrière qui crée de l'harmonie et de la justice dans le monde. Ton leadership est collaboratif.

**Domaine activé** : Maison 10 — Ta carrière, ton impact public cherchent à créer plus d'équité et de beauté.

**Ton approche instinctive** : Tu sais naviguer les relations professionnelles avec élégance tout en portant des idées innovantes.

**Tensions possibles** : Le risque de diluer ton message pour plaire ou d'éviter les prises de position nécessaires.

**Conseil clé** : Maintenir ton intégrité tout en cultivant l'harmonie professionnelle.""",
        'weekly_advice': {
            'week_1': "Identifie comment créer plus d'équité dans ton domaine.",
            'week_2': "Crée des alliances professionnelles alignées.",
            'week_3': "Prends une position élégante mais ferme.",
            'week_4': "Célèbre l'harmonie et l'impact créés."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir transformateur**

Ta Lune en Verseau veut changer le monde professionnellement, ton Ascendant Scorpion veut transformer en profondeur les structures de pouvoir.

**Domaine activé** : Maison 10 — Ta carrière, ton impact public deviennent des outils de transformation sociale radicale.

**Ton approche instinctive** : Tu explores les dysfonctionnements systémiques et tu proposes des changements profonds. Cette intensité est puissante.

**Tensions possibles** : Le risque de l'obsession professionnelle ou de la lutte de pouvoir. Tu peux être trop intense.

**Conseil clé** : Utiliser ton pouvoir professionnel pour transformer, pas pour contrôler.""",
        'weekly_advice': {
            'week_1': "Identifie un dysfonctionnement dans ton domaine professionnel.",
            'week_2': "Comprends ses racines systémiques.",
            'week_3': "Propose une solution transformatrice courageuse.",
            'week_4': "Assume le leadership de cette transformation."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Mission expansive**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent une vision professionnelle large et optimiste. Tu veux un impact mondial.

**Domaine activé** : Maison 10 — Ta carrière, ta mission publique cherchent à avoir un impact qui dépasse les frontières.

**Ton approche instinctive** : Tu explores avec enthousiasme des opportunités professionnelles internationales ou éducatives.

**Tensions possibles** : Le risque de promettre plus que tu ne peux tenir ou de manquer de suivi dans tes projets.

**Conseil clé** : Canaliser ton optimisme vers des engagements professionnels réalistes et mesurables.""",
        'weekly_advice': {
            'week_1': "Définis ta vision professionnelle à grande échelle.",
            'week_2': "Identifie les premières étapes concrètes.",
            'week_3': "Engage-toi dans une opportunité qui élargit ton impact.",
            'week_4': "Célèbre le chemin parcouru vers cette vision."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Autorité réinventée**

Ta Lune en Verseau veut révolutionner les structures professionnelles, ton Ascendant Capricorne veut construire un succès durable.

**Domaine activé** : Maison 10 — Ta carrière, ton autorité publique sont en restructuration stratégique.

**Ton approche instinctive** : Tu grimpes méthodiquement tout en introduisant des innovations. Tu deviens une autorité dans un domaine avant-gardiste.

**Tensions possibles** : Le conflit entre respect des hiérarchies et besoin de les transformer. Tu peux te sentir tiraillé.

**Conseil clé** : Utiliser le système pour le changer de l'intérieur.""",
        'weekly_advice': {
            'week_1': "Évalue ta position et ton influence actuelles.",
            'week_2': "Identifie comment utiliser cette position pour innover.",
            'week_3': "Prends une initiative stratégique transformatrice.",
            'week_4': "Consolide ton autorité renouvelée."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolution professionnelle**

Double Verseau sur ta carrière : tu veux créer un modèle professionnel complètement nouveau. Le conventionnel ne t'intéresse absolument pas.

**Domaine activé** : Maison 10 — Ta carrière, ton impact public sont en pleine révolution. Tu veux être pionnier dans ton domaine.

**Ton approche instinctive** : Tu explores des carrières émergentes, des modèles de travail alternatifs. Tu veux être reconnu pour ton avant-gardisme.

**Tensions possibles** : Le risque de l'instabilité professionnelle ou du rejet de ton innovation. Tu peux être trop en avance.

**Conseil clé** : Innover tout en créant suffisamment de stabilité pour durer.""",
        'weekly_advice': {
            'week_1': "Imagine ta carrière idéale sans aucune contrainte.",
            'week_2': "Recherche qui vit déjà ce modèle.",
            'week_3': "Prends une décision radicale vers cette direction.",
            'week_4': "Assume publiquement ton choix non-conventionnel."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 10, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Mission inspirée**

Ta Lune en Verseau veut une carrière qui serve le collectif, ton Ascendant Poissons veut que cette mission soit spirituelle et compassionnée.

**Domaine activé** : Maison 10 — Ta carrière, ton impact public cherchent à intégrer vision humaniste et sensibilité spirituelle.

**Ton approche instinctive** : Ton intuition te guide vers une carrière de service créatif ou spirituel. Tu veux inspirer et guérir à travers ton travail.

**Tensions possibles** : Le risque du flou professionnel ou de la difficulté à te vendre. Tu peux manquer de structure.

**Conseil clé** : Ancrer ta mission inspirée dans une offre professionnelle claire.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition sur ta vraie vocation.",
            'week_2': "Trouve des modèles qui allient spiritualité et professionnalisme.",
            'week_3': "Crée une offre concrète autour de ta mission.",
            'week_4': "Partage ton travail comme un service au monde."
        }
    },

    # ==================== MAISON 11 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Militant communautaire**

Ta Lune en Verseau en Maison 11 t'appelle à t'engager dans des causes collectives. L'Ascendant Bélier ajoute le courage d'agir pour tes idéaux.

**Domaine activé** : Maison 11 — Amitiés, réseaux, projets collectifs, causes sociales. Tu veux créer le changement avec d'autres.

**Ton approche instinctive** : Tu t'engages avec passion dans des mouvements sociaux ou des projets innovants. Tu es un leader naturel dans ces contextes.

**Tensions possibles** : Le risque de l'impatience avec le rythme collectif ou de l'individualisme dans le groupe.

**Conseil clé** : Fédérer sans imposer, inspirer sans dominer.""",
        'weekly_advice': {
            'week_1': "Identifie une cause collective qui te passionne.",
            'week_2': "Rejoins ou crée une communauté autour de cette cause.",
            'week_3': "Prends une initiative concrète pour la faire avancer.",
            'week_4': "Célèbre l'impact collectif créé."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Communauté stable**

Ta Lune en Verseau veut participer à des projets collectifs innovants, ton Ascendant Taureau veut des amitiés durables et fiables.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs cherchent un équilibre entre innovation et stabilité.

**Ton approche instinctive** : Tu construis lentement un réseau de personnes alignées avec tes valeurs. Tes amitiés sont authentiques et durables.

**Tensions possibles** : Le conflit entre désir de nouveauté sociale et besoin de sécurité relationnelle.

**Conseil clé** : Créer une communauté qui évolue tout en restant solide.""",
        'weekly_advice': {
            'week_1': "Évalue la qualité de tes amitiés et réseaux actuels.",
            'week_2': "Identifie les connexions à approfondir.",
            'week_3': "Investis du temps de qualité dans ces relations.",
            'week_4': "Ancre ces amitiés dans des valeurs partagées."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Réseau vibrant**

Double air : tu es dans ton élément dans les réseaux, les communautés, les échanges d'idées. Tu connectes naturellement les gens.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs deviennent des espaces de stimulation intellectuelle infinie.

**Ton approche instinctive** : Tu animes des communautés par ta curiosité et ta communication. Tu es le pont entre les personnes.

**Tensions possibles** : Le risque de rester en surface dans tes amitiés ou de te disperser entre trop de groupes.

**Conseil clé** : Approfondir quelques connexions tout en maintenant la diversité.""",
        'weekly_advice': {
            'week_1': "Cartographie ton réseau actuel.",
            'week_2': "Crée des connexions entre personnes qui devraient se connaître.",
            'week_3': "Approfondis quelques amitiés clés.",
            'week_4': "Célèbre la richesse de ton écosystème social."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Famille choisie**

Ta Lune en Verseau veut des amitiés basées sur des valeurs partagées, ton Ascendant Cancer veut créer une famille émotionnelle.

**Domaine activé** : Maison 11 — Tes amitiés, ta communauté deviennent ton foyer émotionnel. Tu crées une tribu.

**Ton approche instinctive** : Tu nourris tes amitiés avec soin. Ton réseau est une famille choisie qui te soutient émotionnellement.

**Tensions possibles** : Le conflit entre besoin d'indépendance et besoin d'appartenance. Tu peux être possessif avec tes amis.

**Conseil clé** : Créer une communauté qui nourrit sans étouffer.""",
        'weekly_advice': {
            'week_1': "Identifie qui fait partie de ta famille choisie.",
            'week_2': "Exprime ta gratitude et ton affection.",
            'week_3': "Crée un rituel ou tradition avec ta communauté.",
            'week_4': "Cultive ce sentiment d'appartenance authentique."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Leader communautaire**

Ta Lune en Verseau veut servir le collectif, ton Ascendant Lion veut inspirer et rayonner dans ta communauté.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs deviennent des espaces où tu peux briller tout en servant.

**Ton approche instinctive** : Tu animes naturellement des groupes. Les gens gravitent autour de toi dans les contextes sociaux.

**Tensions possibles** : Le risque de chercher l'attention plutôt que de servir. Ton ego peut éclipser le collectif.

**Conseil clé** : Utiliser ton charisme pour élever le groupe, pas juste toi-même.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu peux servir ta communauté.",
            'week_2': "Prends une initiative qui bénéficie au collectif.",
            'week_3': "Inspire les autres par ton exemple.",
            'week_4': "Célèbre les succès collectifs, pas juste les tiens."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Service organisé**

Ta Lune en Verseau veut participer à des projets collectifs innovants, ton Ascendant Vierge veut que ces projets soient efficaces et utiles.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs cherchent à être à la fois visionnaires et pragmatiques.

**Ton approche instinctive** : Tu organises et optimises les initiatives collectives. Ton souci du détail sert le groupe.

**Tensions possibles** : Le risque de critiquer ou de micro-gérer. Tu peux être trop exigeant avec tes amis ou ta communauté.

**Conseil clé** : Servir le collectif sans perdre la spontanéité et la joie.""",
        'weekly_advice': {
            'week_1': "Identifie comment améliorer l'efficacité d'un projet collectif.",
            'week_2': "Propose tes services d'organisation.",
            'week_3': "Implémente des améliorations concrètes.",
            'week_4': "Apprécie l'impact de ton service discret."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie collective**

Double air : tu excelles à créer des espaces communautaires harmonieux. Tu facilites la collaboration et l'équité dans les groupes.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs deviennent des espaces de beauté et d'équilibre.

**Ton approche instinctive** : Tu es le médiateur naturel dans les conflits de groupe. Tu sais créer du consensus autour d'idées innovantes.

**Tensions possibles** : Le risque de sacrifier ta voix pour l'harmonie du groupe. Tu peux éviter les tensions nécessaires.

**Conseil clé** : Maintenir l'harmonie sans diluer les visions fortes.""",
        'weekly_advice': {
            'week_1': "Évalue l'équilibre dans tes relations communautaires.",
            'week_2': "Facilite un dialogue harmonieux sur un sujet difficile.",
            'week_3': "Crée un événement qui rassemble ta communauté.",
            'week_4': "Célèbre la beauté de la collaboration."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Transformation collective**

Ta Lune en Verseau veut servir le collectif, ton Ascendant Scorpion veut transformer profondément les dynamiques de groupe.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs deviennent des espaces de transformation radicale.

**Ton approche instinctive** : Tu explores les dynamiques de pouvoir dans les groupes. Tu veux des amitiés et communautés authentiques.

**Tensions possibles** : Le risque de l'intensité relationnelle ou du contrôle dans les amitiés. Tu peux être trop exigeant.

**Conseil clé** : Transformer les groupes avec compassion, pas par manipulation.""",
        'weekly_advice': {
            'week_1': "Identifie les non-dits dans tes communautés.",
            'week_2': "Ose aborder ces sujets avec honnêteté.",
            'week_3': "Facilite une transformation authentique du groupe.",
            'week_4': "Célèbre la nouvelle profondeur des connexions."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Réseau global**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent une vision communautaire large et inclusive. Tu veux connecter le monde.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs transcendent les frontières culturelles et géographiques.

**Ton approche instinctive** : Tu crées des ponts internationaux. Tes amitiés sont diverses et ta vision communautaire est expansive.

**Tensions possibles** : Le risque de manquer de profondeur dans tes connexions ou de trop te disperser.

**Conseil clé** : Créer un réseau large tout en cultivant quelques amitiés profondes.""",
        'weekly_advice': {
            'week_1': "Explore une communauté internationale ou multiculturelle.",
            'week_2': "Crée des connexions avec des personnes de cultures différentes.",
            'week_3': "Lance un projet qui unit des perspectives diverses.",
            'week_4': "Célèbre la richesse de la diversité."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Réseau stratégique**

Ta Lune en Verseau veut participer à des projets collectifs innovants, ton Ascendant Capricorne veut que ces projets aient un impact durable.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs sont abordés avec sérieux et ambition à long terme.

**Ton approche instinctive** : Tu construis méthodiquement un réseau professionnel et personnel aligné avec tes objectifs.

**Tensions possibles** : Le risque de l'instrumentalisation des relations ou du manque de spontanéité dans les amitiés.

**Conseil clé** : Cultiver des connexions authentiques qui servent aussi tes objectifs.""",
        'weekly_advice': {
            'week_1': "Évalue la qualité stratégique de ton réseau.",
            'week_2': "Identifie les connexions à cultiver pour l'impact à long terme.",
            'week_3': "Investis sérieusement dans ces relations clés.",
            'week_4': "Consolide ton réseau stratégique."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Tribu visionnaire**

Double Verseau sur ta communauté : tu veux créer ou rejoindre une tribu de visionnaires, de gens qui pensent le futur différemment.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs sont en pleine révolution. Tu cherches ta vraie tribu.

**Ton approche instinctive** : Tu es naturellement attiré par les communautés alternatives, les mouvements sociaux innovants, les réseaux avant-gardistes.

**Tensions possibles** : Le risque de l'isolement si tu ne trouves pas ta tribu ou du rejet des connexions mainstream.

**Conseil clé** : Créer ou trouver ta communauté tout en restant ouvert aux ponts.""",
        'weekly_advice': {
            'week_1': "Définis les valeurs non-négociables de ta tribu idéale.",
            'week_2': "Recherche activement ces personnes et communautés.",
            'week_3': "Engage-toi dans un projet collectif aligné.",
            'week_4': "Célèbre la connexion avec tes pairs visionnaires."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 11, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Communauté spirituelle**

Ta Lune en Verseau veut servir le collectif, ton Ascendant Poissons veut que cette communauté soit unie spirituellement et compassionnément.

**Domaine activé** : Maison 11 — Tes amitiés, réseaux, projets collectifs cherchent à intégrer vision humaniste et connexion spirituelle.

**Ton approche instinctive** : Tu crées ou rejoins des communautés basées sur des valeurs spirituelles ou artistiques partagées.

**Tensions possibles** : Le risque du flou dans les limites relationnelles ou de l'idéalisation de la communauté.

**Conseil clé** : Créer une communauté inspirée tout en maintenant des limites saines.""",
        'weekly_advice': {
            'week_1': "Identifie ta vision spirituelle du collectif.",
            'week_2': "Trouve ou crée une communauté qui la partage.",
            'week_3': "Contribue créativement ou spirituellement au groupe.",
            'week_4': "Célèbre l'unité dans la diversité."
        }
    },

    # ==================== MAISON 12 ====================

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Libération intérieure**

Ta Lune en Verseau en Maison 12 t'invite à libérer ton inconscient, à te connecter à l'universel. L'Ascendant Bélier te donne le courage d'explorer ces profondeurs.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, solitude créative, libération. Tu veux te libérer des conditionnements cachés.

**Ton approche instinctive** : Tu explores ton monde intérieur avec courage. Tu veux comprendre et libérer ce qui était enfoui.

**Tensions possibles** : Le risque de l'impatience avec le processus inconscient ou du rejet de la vulnérabilité.

**Conseil clé** : Accepter que certaines transformations prennent du temps et nécessitent de la douceur.""",
        'weekly_advice': {
            'week_1': "Crée un espace de solitude et d'introspection.",
            'week_2': "Explore tes rêves et ton inconscient avec curiosité.",
            'week_3': "Identifie un pattern inconscient à libérer.",
            'week_4': "Célèbre ta libération intérieure progressive."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Spiritualité enracinée**

Ta Lune en Verseau veut se connecter à l'universel, ton Ascendant Taureau veut que cette spiritualité soit ancrée dans le corps et la nature.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, repos cherchent un équilibre entre transcendance et ancrage.

**Ton approche instinctive** : Tu médites, tu te connectes à la nature, tu nourris ton âme par des pratiques simples et sensorielles.

**Tensions possibles** : Le conflit entre besoin de sécurité matérielle et désir de dissolution spirituelle.

**Conseil clé** : Cultiver une spiritualité qui honore à la fois le transcendant et le terrestre.""",
        'weekly_advice': {
            'week_1': "Crée une pratique spirituelle quotidienne simple.",
            'week_2': "Connecte-toi à la nature régulièrement.",
            'week_3': "Honore ton corps comme temple spirituel.",
            'week_4': "Savoure la paix intérieure cultivée."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Méditation mentale**

Double air : ton esprit cherche à comprendre l'incompréhensible. Tu veux conceptualiser l'invisible, l'inconscient, le spirituel.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, solitude deviennent des sujets de réflexion et d'étude.

**Ton approche instinctive** : Tu lis sur la spiritualité, tu analyses tes rêves, tu explores intellectuellement ton monde intérieur.

**Tensions possibles** : Le risque de rester dans le mental et de manquer l'expérience directe du spirituel.

**Conseil clé** : Laisser l'intellect se taire parfois pour expérimenter l'ineffable.""",
        'weekly_advice': {
            'week_1': "Étudie un aspect de la spiritualité qui t'intrigue.",
            'week_2': "Pratique une méditation silencieuse quotidiennement.",
            'week_3': "Partage tes réflexions sur l'invisible avec quelqu'un.",
            'week_4': "Intègre ce que tu as compris intellectuellement ET expérimenté."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Guérison émotionnelle**

Ta Lune en Verseau veut se libérer objectivement, ton Ascendant Cancer ressent profondément les blessures à guérir. Cette combinaison est puissamment guérissante.

**Domaine activé** : Maison 12 — Inconscient, guérison, spiritualité sont au cœur de ton processus émotionnel.

**Ton approche instinctive** : Tu plonges dans tes émotions profondes avec à la fois compassion et lucidité. Cette approche est thérapeutique.

**Tensions possibles** : Le risque de te perdre dans tes émotions ou à l'inverse de te détacher trop pour te protéger.

**Conseil clé** : Honorer tes émotions tout en gardant la perspective nécessaire à la guérison.""",
        'weekly_advice': {
            'week_1': "Crée un espace sûr pour ressentir pleinement.",
            'week_2': "Explore une blessure émotionnelle ancienne.",
            'week_3': "Trouve une nouvelle perspective libératrice.",
            'week_4': "Célèbre ta guérison en cours."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Ego dissous**

Ta Lune en Verseau veut dissoudre l'ego, ton Ascendant Lion a un ego fort. Cette tension peut être transformatrice.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, dissolution de l'ego deviennent des terrains d'exploration.

**Ton approche instinctive** : Tu explores l'humilité spirituelle, le service discret, l'effacement conscient. C'est challengeant mais libérateur.

**Tensions possibles** : Le conflit entre besoin de reconnaissance et désir de dissolution. Tu peux osciller entre les deux.

**Conseil clé** : Utiliser ta force pour servir l'invisible, pas pour briller.""",
        'weekly_advice': {
            'week_1': "Identifie où ton ego te limite.",
            'week_2': "Pratique le service anonyme ou discret.",
            'week_3': "Médite sur l'impermanence et l'universel.",
            'week_4': "Célèbre la liberté que donne l'humilité."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Service invisible**

Ta Lune en Verseau veut se connecter à l'universel, ton Ascendant Vierge veut servir humblement et efficacement dans l'ombre.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, service discret deviennent ta pratique quotidienne.

**Ton approche instinctive** : Tu sers sans attendre de reconnaissance. Tu purifies et optimises ton monde intérieur avec soin.

**Tensions possibles** : Le risque de la sur-analyse spirituelle ou de la critique de soi excessive.

**Conseil clé** : Servir avec humilité tout en t'accordant de la compassion.""",
        'weekly_advice': {
            'week_1': "Identifie comment servir discrètement.",
            'week_2': "Crée une pratique spirituelle quotidienne simple.",
            'week_3': "Purifie ton espace intérieur avec douceur.",
            'week_4': "Apprécie la paix que donne le service humble."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie invisible**

Double air : tu cherches l'équilibre spirituel, l'harmonie avec l'universel. Ta méditation est esthétique et paisible.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, solitude créative cherchent beauté et équilibre.

**Ton approche instinctive** : Tu crées un espace intérieur harmonieux. Ta spiritualité passe par l'art et la beauté.

**Tensions possibles** : Le risque d'éviter les aspects inconfortables de l'inconscient pour maintenir l'harmonie.

**Conseil clé** : Accepter que la vraie paix passe parfois par le déséquilibre temporaire.""",
        'weekly_advice': {
            'week_1': "Crée un espace méditatif esthétique.",
            'week_2': "Explore une pratique spirituelle créative.",
            'week_3': "Accepte les parts d'ombre avec élégance.",
            'week_4': "Célèbre l'équilibre intérieur trouvé."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Plongée mystique**

Ta Lune en Verseau veut se libérer, ton Ascendant Scorpion veut plonger dans les profondeurs les plus obscures. Cette combinaison est intensément transformatrice.

**Domaine activé** : Maison 12 — Inconscient, transformation spirituelle, mort de l'ego sont explorés sans peur.

**Ton approche instinctive** : Tu explores les zones les plus sombres de l'inconscient pour les transformer et te libérer.

**Tensions possibles** : Le risque de l'obsession spirituelle ou de la descente trop brutale dans l'ombre.

**Conseil clé** : Descendre avec courage mais aussi avec compassion pour toi-même.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui est prêt à mourir en toi.",
            'week_2': "Plonge dans cette transformation avec courage.",
            'week_3': "Accueille la renaissance qui émerge.",
            'week_4': "Célèbre ta libération spirituelle."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foi visionnaire**

Ta Lune en Verseau et ton Ascendant Sagittaire te donnent une spiritualité optimiste et expansive. Tu crois en un futur meilleur pour tous.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, solitude deviennent des espaces d'exploration philosophique et de foi.

**Ton approche instinctive** : Tu médites sur le sens de la vie, tu explores différentes spiritualités avec ouverture et enthousiasme.

**Tensions possibles** : Le risque de l'optimisme naïf spirituel ou d'éviter les profondeurs inconfortables.

**Conseil clé** : Cultiver la foi tout en acceptant le mystère et l'ombre.""",
        'weekly_advice': {
            'week_1': "Explore une tradition spirituelle nouvelle pour toi.",
            'week_2': "Médite sur ta vision du sens de la vie.",
            'week_3': "Partage ta foi et ton optimisme spirituel.",
            'week_4': "Célèbre la connexion au transcendant."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Structure spirituelle**

Ta Lune en Verseau veut se libérer spirituellement, ton Ascendant Capricorne veut construire une pratique spirituelle disciplinée et durable.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, repos sont abordés avec sérieux et méthode.

**Ton approche instinctive** : Tu crées une pratique spirituelle quotidienne disciplinée. Tu construis ton monde intérieur avec patience.

**Tensions possibles** : Le conflit entre contrôle et lâcher-prise spirituel. Tu peux vouloir tout maîtriser, même l'invisible.

**Conseil clé** : Cultiver la discipline spirituelle tout en acceptant de ne pas tout contrôler.""",
        'weekly_advice': {
            'week_1': "Crée une routine spirituelle quotidienne structurée.",
            'week_2': "Engage-toi sérieusement dans cette pratique.",
            'week_3': "Laisse place au mystère dans ta discipline.",
            'week_4': "Consolide ta fondation spirituelle."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Conscience collective**

Double Verseau dans l'inconscient : tu te connectes naturellement à l'inconscient collectif. Tu captes les courants invisibles de l'humanité.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, connexion universelle sont au cœur de ton expérience. Tu es un canal.

**Ton approche instinctive** : Tu reçois des intuitions sur l'évolution collective. Ton rôle est de canaliser ces visions pour les rendre accessibles.

**Tensions possibles** : Le risque de te perdre dans l'universel et de négliger ton ancrage personnel.

**Conseil clé** : Canaliser l'universel tout en restant ancré dans ton individualité.""",
        'weekly_advice': {
            'week_1': "Crée un espace de solitude pour écouter l'invisible.",
            'week_2': "Note les intuitions et visions qui émergent.",
            'week_3': "Trouve comment les partager de manière utile.",
            'week_4': "Célèbre ton rôle de canal pour le collectif."
        }
    },

    {
        'moon_sign': 'Aquarius', 'moon_house': 12, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution transcendante**

Ta Lune en Verseau veut libérer, ton Ascendant Poissons veut dissoudre dans l'universel. Cette combinaison est profondément mystique et compassionnée.

**Domaine activé** : Maison 12 — Inconscient, spiritualité, dissolution de l'ego, compassion universelle sont vécus intensément.

**Ton approche instinctive** : Tu te laisses porter par l'invisible, tu fais confiance au processus spirituel. Cette foi est ta force.

**Tensions possibles** : Le risque de la confusion ou de la perte de limites. Tu peux te dissoudre sans te reconstruire.

**Conseil clé** : Honorer la dissolution tout en gardant un fil d'ancrage dans le concret.""",
        'weekly_advice': {
            'week_1': "Lâche prise complètement dans ta pratique spirituelle.",
            'week_2': "Fais confiance à l'invisible qui te guide.",
            'week_3': "Exprime ta compassion universelle concrètement.",
            'week_4': "Célèbre ta connexion à l'unité de toute vie."
        }
    },

]

async def main():
    print(f"=== Insertion batch Aquarius complet: {len(BATCH)} interprétations ===")
    await insert_batch(BATCH)
    print("=== Terminé ===")

if __name__ == '__main__':
    asyncio.run(main())
