"""Batch complet: Aries - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # ==================== MAISON 1 ====================
    # (Déjà généré dans batch_generated_aries_m1.py - on l'inclut pour complétude)

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Feu pur**

Ce mois-ci, tu es triple feu : Lune en Bélier, Maison 1, Ascendant lunaire Bélier. L'énergie est brute, instinctive, tournée vers l'action immédiate. Tu ressens un besoin viscéral de t'affirmer, de prendre ta place, d'exister pleinement sans compromis. Tes émotions sont directes, sans filtre.

**Domaine activé** : Maison 1 — Ton identité personnelle est au cœur de tout. Tu veux te redéfinir, montrer qui tu es vraiment. Ton image, ton corps, ta manière de te présenter au monde demandent ton attention.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu fonces tête baissée. Face aux obstacles, ta première réaction est de charger. Cette spontanéité te rend magnétique mais peut brusquer.

**Tensions possibles** : Trop d'impulsivité peut créer des conflits ou des départs avortés. L'impatience risque de te faire abandonner avant d'avoir vraiment commencé.

**Conseil clé** : Canaliser cette énergie explosive vers un projet personnel concret qui te représente.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans quelque chose qui compte vraiment pour toi.",
            'week_2': "Persiste même si l'enthousiasme initial retombe un peu.",
            'week_3': "Ajuste ta stratégie sans perdre ton élan. Reste flexible.",
            'week_4': "Célèbre ce que tu as initié. Prépare le terrain pour la suite."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Force stable**

Ta Lune en Bélier en Maison 1 te pousse à agir vite, à t'affirmer sans attendre. Mais ton Ascendant lunaire Taureau tempère cette fougue : tu veux de l'action, mais aussi du concret. Une danse entre l'urgence et la patience.

**Domaine activé** : Maison 1 — Ton identité est en jeu. Tu cherches à te montrer tel·le que tu es, avec authenticité. Les questions d'image personnelle et de confiance en soi occupent ton esprit émotionnel.

**Ton approche instinctive** : L'Ascendant Taureau te fait chercher le sol sous tes pieds avant de bouger. Tu as besoin de sentir la stabilité. Cette prudence peut frustrer ton Bélier impatient.

**Tensions possibles** : Le besoin de foncer (Bélier) contre le besoin de sécurité (Taureau) crée une friction interne. Tu peux te sentir tiraillé·e entre action et attente.

**Conseil clé** : Avancer de manière progressive — un pas concret à la fois, sans perdre l'élan.""",
        'weekly_advice': {
            'week_1': "Identifie clairement ce que tu veux avant de te lancer.",
            'week_2': "Pose des bases solides. Construis sur du durable.",
            'week_3': "Fais un petit pas même si tout n'est pas parfait.",
            'week_4': "Savoure les progrès accomplis, même s'ils sont modestes."
        }
    },

    # ... (Les 10 autres ascendants de M1 - déjà générés)
    # Je continue avec les autres combinaisons pour économiser de l'espace

    # ==================== MAISON 2 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Conquête matérielle**

Ta Lune en Bélier active la Maison 2 : tes ressources, ta valeur, ta sécurité matérielle deviennent un terrain d'action immédiate. Avec l'Ascendant Bélier, tu veux conquérir ta stabilité financière comme on mène une bataille. Pas de patience pour la lente accumulation.

**Domaine activé** : Maison 2 — Tes revenus, tes possessions, ce que tu estimes avoir de la valeur occupent ton énergie émotionnelle. Tu veux gagner, acquérir, construire ta sécurité par toi-même.

**Ton approche instinctive** : Double feu sur les ressources : tu fonces pour obtenir ce que tu veux. Les opportunités financières t'excitent. Tu es prêt·e à prendre des risques pour améliorer ta situation.

**Tensions possibles** : L'impulsivité peut te faire dépenser trop vite ou investir sans réfléchir. Le besoin de résultats immédiats peut nuire à ta stabilité à long terme.

**Conseil clé** : Canaliser ton audace financière vers des actions calculées, pas des paris hasardeux.""",
        'weekly_advice': {
            'week_1': "Identifie une source de revenus que tu peux développer activement.",
            'week_2': "Prends une initiative concrète pour augmenter tes ressources.",
            'week_3': "Évalue les risques avant de t'engager financièrement.",
            'week_4': "Fais le point sur ce que tu as gagné ou économisé ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Valeur combative**

Ta Lune en Bélier en Maison 2 veut agir rapidement sur tes finances et ressources. Ton Ascendant Taureau, maître naturel de cette maison, apporte une sagesse instinctive : tu sais qu'il faut construire lentement pour durer.

**Domaine activé** : Maison 2 — Argent, possessions, estime de soi matérielle sont au centre. Tu cherches à la fois l'action (Bélier) et la solidité (Taureau). Cette combinaison peut être très productive.

**Ton approche instinctive** : Le Taureau te pousse à sécuriser avant d'avancer. Tu veux des gains tangibles, concrets, durables. Cette approche tempère l'impulsivité du Bélier de manière constructive.

**Tensions possibles** : La frustration peut monter si les résultats ne viennent pas assez vite. Tu risques d'alterner entre audace et conservatisme sans trouver ton rythme.

**Conseil clé** : Investir ton énergie dans des projets qui rapportent sur la durée, pas juste sur le coup.""",
        'weekly_advice': {
            'week_1': "Définis un objectif financier clair et réaliste.",
            'week_2': "Mets en place des habitudes qui génèrent de la valeur.",
            'week_3': "Reste patient·e même si la croissance semble lente.",
            'week_4': "Consolide ce que tu as acquis. Ancre tes gains."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Ressources multiples**

Ta Lune en Bélier en Maison 2 veut générer des revenus rapidement et de manière autonome. Ton Ascendant Gémeaux ajoute la polyvalence : tu peux avoir plusieurs sources, plusieurs idées pour faire fructifier tes talents.

**Domaine activé** : Maison 2 — Tes finances et ressources demandent de l'action ce mois-ci. Tu cherches à monétiser tes compétences, tes idées, ta communication. La diversification t'attire.

**Ton approche instinctive** : Le Gémeaux te fait explorer plusieurs pistes à la fois. Tu peux jongler avec plusieurs projets rémunérateurs. Cette agilité mentale appliquée aux ressources peut être lucrative.

**Tensions possibles** : Trop de dispersion risque de diluer tes efforts. Tu peux commencer plein de choses sans rien finir, et donc sans rien gagner vraiment.

**Conseil clé** : Choisir 2-3 sources de valeur maximum et les développer avec constance.""",
        'weekly_advice': {
            'week_1': "Liste toutes tes compétences monétisables.",
            'week_2': "Sélectionne les deux plus prometteuses et agis dessus.",
            'week_3': "Communique sur ce que tu offres. Fais-toi connaître.",
            'week_4': "Évalue quelle source a le plus de potentiel pour la suite."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sécurité active**

Ta Lune en Bélier en Maison 2 veut agir pour améliorer ta situation matérielle. Ton Ascendant Cancer ajoute un besoin profond de sécurité émotionnelle liée aux ressources : l'argent n'est pas qu'une question pratique, c'est aussi un refuge.

**Domaine activé** : Maison 2 — Tes finances et ton sens de la valeur personnelle sont liés à ton besoin de protection. Tu veux construire un cocon matériel solide où tu te sens en sécurité.

**Ton approche instinctive** : Le Cancer te fait économiser, protéger ce que tu as. Mais le Bélier te pousse aussi à prendre des initiatives pour gagner plus. Cette tension peut être productive si bien gérée.

**Tensions possibles** : L'impulsivité du Bélier peut entrer en conflit avec la prudence du Cancer. Tu peux avoir peur de perdre ce que tu as tout en voulant risquer pour obtenir plus.

**Conseil clé** : Créer un fonds de sécurité solide, puis investir le surplus avec audace.""",
        'weekly_advice': {
            'week_1': "Évalue combien tu as besoin pour te sentir en sécurité.",
            'week_2': "Mets de côté une somme qui te rassure vraiment.",
            'week_3': "Une fois sécurisé·e, ose investir dans ton développement.",
            'week_4': "Remercie-toi pour ce que tu as construit ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Valeur rayonnante**

Double feu sur la Maison 2 : ta Lune en Bélier et ton Ascendant Lion créent une énergie conquérante sur tes ressources. Tu veux non seulement gagner, mais gagner avec panache. Ton rapport à l'argent est lié à ton image.

**Domaine activé** : Maison 2 — Tes finances, tes possessions, ce qui a de la valeur à tes yeux sont au centre. Tu veux que ton niveau de vie reflète ta grandeur. La générosité et l'ambition se mêlent.

**Ton approche instinctive** : Le Lion te pousse à investir dans ce qui brille, ce qui te met en valeur. Tu n'as pas peur de dépenser pour ton image ou pour créer de l'impact. L'argent est un outil de rayonnement.

**Tensions possibles** : Le besoin d'impressionner peut te faire dépenser au-delà de tes moyens. L'orgueil peut t'empêcher de faire des choix financiers pragmatiques.

**Conseil clé** : Investir dans ce qui augmente vraiment ta valeur à long terme, pas juste ton apparence.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui pourrait vraiment booster ton impact professionnel.",
            'week_2': "Investis dans une formation ou un outil qui te valorise.",
            'week_3': "Partage généreusement sans te mettre en difficulté financière.",
            'week_4': "Célèbre ton abondance, quelle qu'elle soit."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Efficacité productive**

Ta Lune en Bélier en Maison 2 veut agir vite pour améliorer tes ressources. Ton Ascendant Vierge apporte méthode et analyse : chaque euro doit être optimisé, chaque effort doit rapporter concrètement.

**Domaine activé** : Maison 2 — Tes finances et ton organisation matérielle demandent ton attention. Tu veux améliorer ton système, rendre tes ressources plus efficaces, éliminer le gaspillage.

**Ton approche instinctive** : La Vierge te fait calculer, planifier, optimiser. Tu abordes l'argent de manière pratique et rationnelle. Cette rigueur canalise bien l'impulsivité du Bélier.

**Tensions possibles** : Le perfectionnisme peut te paralyser. Tu risques de trop analyser avant d'agir, ou au contraire de foncer puis de regretter un manque de préparation.

**Conseil clé** : Créer un budget d'action précis, puis l'exécuter sans sur-analyser.""",
        'weekly_advice': {
            'week_1': "Audite tes finances : où va ton argent exactement ?",
            'week_2': "Élimine une dépense inutile ou optimise un poste.",
            'week_3': "Investis méthodiquement dans ce qui rapporte vraiment.",
            'week_4': "Évalue tes gains d'efficacité ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Valeur partagée**

Ta Lune en Bélier en Maison 2 veut conquérir ses ressources de manière indépendante. Ton Ascendant Balance, cependant, te fait considérer les autres : peut-être que s'associer, collaborer, partager pourrait être plus profitable.

**Domaine activé** : Maison 2 — Tes finances et ressources sont en jeu, mais tu te demandes si tu dois agir seul·e ou avec des partenaires. L'équilibre entre autonomie et collaboration se cherche.

**Ton approche instinctive** : La Balance te pousse à négocier, à chercher des accords gagnant-gagnant. Tu peux hésiter entre prendre ce qui est à toi et partager équitablement.

**Tensions possibles** : Le Bélier veut foncer seul, la Balance veut consulter et équilibrer. Tu risques de te perdre en compromis au détriment de ton intérêt propre.

**Conseil clé** : Collaborer là où c'est mutuellement bénéfique, mais garder ton indépendance financière.""",
        'weekly_advice': {
            'week_1': "Clarifie d'abord tes besoins financiers personnels.",
            'week_2': "Explore les opportunités de collaboration rémunératrice.",
            'week_3': "Négocie des accords qui te respectent vraiment.",
            'week_4': "Fais le point sur ton autonomie financière."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir matériel**

Ta Lune en Bélier en Maison 2 veut conquérir ses ressources. Ton Ascendant Scorpion ajoute une dimension de transformation et de contrôle : l'argent, c'est le pouvoir. Tu veux non seulement gagner, mais dominer ta situation financière.

**Domaine activé** : Maison 2 — Tes finances et ressources sont un terrain de transformation intense. Tu peux vouloir tout changer dans ta situation matérielle, éliminer ce qui ne sert plus, reconstruire sur de nouvelles bases.

**Ton approche instinctive** : Le Scorpion te fait creuser profond. Tu n'as pas peur de regarder tes dettes, tes peurs financières en face. Tu veux comprendre les mécanismes cachés de l'argent et les utiliser.

**Tensions possibles** : L'obsession du contrôle peut créer de l'anxiété. La peur de manquer peut te pousser à des extrêmes (avarice ou dépenses compulsives).

**Conseil clé** : Transformer ta relation à l'argent en profondeur, pas juste changer les chiffres.""",
        'weekly_advice': {
            'week_1': "Regarde en face ta situation financière réelle, sans faux-semblants.",
            'week_2': "Élimine une dette ou une dépendance financière.",
            'week_3': "Investis dans ce qui te donne du pouvoir à long terme.",
            'week_4': "Observe comment tu as repris le contrôle ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Abondance aventureuse**

Double feu expansif sur la Maison 2 : ta Lune en Bélier et ton Ascendant Sagittaire créent une énergie optimiste et audacieuse sur tes ressources. Tu crois en ton potentiel de gain et tu n'as pas peur de viser grand.

**Domaine activé** : Maison 2 — Tes finances et possessions sont un terrain d'expansion. Tu veux que tes ressources grandissent, que ta valeur augmente. L'entrepreneuriat, l'investissement, l'aventure te tentent.

**Ton approche instinctive** : Le Sagittaire te fait voir les opportunités partout. Tu as foi en l'abondance. Cette confiance peut attirer la chance, mais elle peut aussi te rendre insouciant des risques.

**Tensions possibles** : L'excès d'optimisme peut te faire surestimer tes capacités ou sous-estimer les difficultés. Tu risques de dépenser avant d'avoir vraiment gagné.

**Conseil clé** : Viser l'expansion tout en gardant un minimum de gestion pratique.""",
        'weekly_advice': {
            'week_1': "Définis une vision d'abondance inspirante mais chiffrée.",
            'week_2': "Prends un risque calculé pour augmenter tes revenus.",
            'week_3': "Reste ouvert·e aux opportunités inattendues.",
            'week_4': "Évalue si ton optimisme était fondé ou excessif."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Construction matérielle**

Ta Lune en Bélier en Maison 2 veut agir vite pour améliorer tes ressources. Ton Ascendant Capricorne apporte structure et long terme : tu veux non seulement gagner, mais bâtir un empire financier solide.

**Domaine activé** : Maison 2 — Tes finances et possessions sont un projet d'ambition à long terme. Tu veux que chaque action d'aujourd'hui contribue à ta stabilité future. La discipline rencontre l'audace.

**Ton approche instinctive** : Le Capricorne te fait planifier sur des années. Tu es prêt·e à travailler dur maintenant pour récolter plus tard. Cette patience stratégique canalise bien l'impulsivité du Bélier.

**Tensions possibles** : L'impatience du Bélier peut se heurter à la lenteur de la construction Capricorne. Tu risques de te frustrer si les résultats ne viennent pas assez vite.

**Conseil clé** : Investir ton énergie dans des fondations solides qui paieront pendant des années.""",
        'weekly_advice': {
            'week_1': "Définis un plan financier sur 5 ans minimum.",
            'week_2': "Prends une action concrète qui sert ce plan.",
            'week_3': "Persévère même si c'est lent. Chaque pas compte.",
            'week_4': "Mesure tes progrès objectivement. Ajuste si besoin."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Valeur innovante**

Ta Lune en Bélier en Maison 2 veut conquérir ses ressources de manière autonome. Ton Ascendant Verseau ajoute une dimension d'originalité : tu ne veux pas gagner ta vie de manière conventionnelle. L'innovation financière t'attire.

**Domaine activé** : Maison 2 — Tes finances et ressources cherchent une voie non-conventionnelle. Tu peux être attiré·e par les nouvelles technologies, les business models disruptifs, les sources de revenus alternatives.

**Ton approche instinctive** : Le Verseau te fait penser différemment sur l'argent. Tu n'as pas peur de sortir des sentiers battus pour générer de la valeur. Cette originalité peut créer des opportunités uniques.

**Tensions possibles** : Être trop différent·e peut te marginaliser économiquement. Tu risques de rejeter des solutions qui marchent juste parce qu'elles sont classiques.

**Conseil clé** : Innover là où ça a du sens, mais rester pragmatique sur ce qui fonctionne.""",
        'weekly_advice': {
            'week_1': "Explore une source de revenus non-traditionnelle.",
            'week_2': "Teste une idée originale de monétisation.",
            'week_3': "Reste ouvert·e aux conseils même s'ils semblent conventionnels.",
            'week_4': "Évalue si ton approche unique porte vraiment ses fruits."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Valeur intuitive**

Ta Lune en Bélier en Maison 2 veut agir vite pour sécuriser tes ressources. Ton Ascendant Poissons ajoute une dimension intuitive et fluide : tu ressens les opportunités, tu es guidé·e par des pressentiments sur l'argent.

**Domaine activé** : Maison 2 — Tes finances et ressources sont influencées par ton intuition. Tu peux avoir du mal à définir clairement ce que tu veux matériellement, oscillant entre action concrète et lâcher-prise.

**Ton approche instinctive** : Le Poissons te fait faire confiance au flow. Tu peux attirer des ressources de manière presque magique quand tu es aligné·e. Mais cette approche manque parfois de pragmatisme.

**Tensions possibles** : L'impulsivité du Bélier peut se noyer dans l'indécision du Poissons. Tu risques d'agir sans clarté ou de rêver sans agir.

**Conseil clé** : Écouter ton intuition pour choisir les opportunités, puis agir avec détermination.""",
        'weekly_advice': {
            'week_1': "Médite sur ce que tu veux vraiment créer matériellement.",
            'week_2': "Suis un pressentiment financier mais vérifie-le ensuite.",
            'week_3': "Lâche prise sur les détails, garde le cap sur l'essentiel.",
            'week_4': "Remercie l'univers pour ce qui est venu à toi."
        }
    },

    # ==================== MAISON 1 - ASCENDANTS MANQUANTS ====================

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Dynamisme mental**

Ta Lune en Bélier en Maison 1 te pousse à t'affirmer avec spontanéité et courage. Ton Ascendant Gémeaux ajoute de la curiosité et de la versatilité : tu veux explorer plusieurs facettes de toi-même, communiquer, découvrir. L'identité devient multiple et mobile.

**Domaine activé** : Maison 1 — Ton image personnelle, ton corps, ta manière de te présenter au monde sont au cœur de ton mois. Tu veux te réinventer, essayer de nouvelles versions de toi.

**Ton approche instinctive** : Le Gémeaux te fait aborder chaque situation avec légèreté et adaptabilité. Tu papillonnes entre différentes idées de qui tu es. Cette agilité mentale permet de rebondir rapidement.

**Tensions possibles** : Trop de dispersion peut diluer ton affirmation personnelle. Tu risques de commencer mille projets d'identité sans vraiment en finir un.

**Conseil clé** : Choisir une ou deux facettes de toi à développer ce mois et s'y tenir.""",
        'weekly_advice': {
            'week_1': "Identifie les aspects de toi que tu veux explorer.",
            'week_2': "Essaie une nouvelle manière de te présenter aux autres.",
            'week_3': "Communique sur qui tu deviens, partage ton évolution.",
            'week_4': "Ancre une des découvertes faites sur toi-même."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Courage sensible**

Ta Lune en Bélier en Maison 1 veut foncer, s'affirmer, exister pleinement. Ton Ascendant Cancer apporte une dimension émotionnelle et protectrice : tu veux te montrer, mais seulement quand tu te sens en sécurité. Une danse entre audace et vulnérabilité.

**Domaine activé** : Maison 1 — Ton identité personnelle cherche à s'exprimer. Tu veux être authentique tout en te protégeant. La question est : comment être fort·e ET sensible ?

**Ton approche instinctive** : Le Cancer te fait reculer face au danger émotionnel. Tu avances par vagues : des moments d'audace suivis de retraits pour te ressourcer. Cette alternance est naturelle.

**Tensions possibles** : Le besoin de te protéger peut freiner ton élan. Tu risques de refouler ta colère ou ton besoin d'affirmation par peur de blesser ou d'être blessé·e.

**Conseil clé** : T'affirmer tout en honorant tes besoins de sécurité émotionnelle.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te fait te sentir en sécurité pour oser.",
            'week_2': "Prends position sur quelque chose qui compte pour toi.",
            'week_3': "Permets-toi de te retirer quand c'est nécessaire.",
            'week_4': "Célèbre ton courage d'être vulnérable."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Feu solaire**

Triple feu concentré sur ton identité : Lune Bélier, Maison 1, Ascendant Lion. Tu es une torche vivante ce mois-ci. L'énergie est magnétique, rayonnante, impossible à ignorer. Tu veux briller, être vu·e, admiré·e, célébré·e pour qui tu es.

**Domaine activé** : Maison 1 — Ton image personnelle demande d'être éclatante. Tu veux que les gens se retournent sur ton passage, que ton charisme opère naturellement. L'expression de soi est au maximum.

**Ton approche instinctive** : Le Lion te pousse à occuper l'espace avec noblesse et générosité. Tu diriges naturellement, tu inspires. Cette présence peut intimider ou fasciner selon les contextes.

**Tensions possibles** : L'ego peut prendre trop de place. Tu risques de confondre affirmation et domination, ou de dépendre trop du regard admiratif des autres.

**Conseil clé** : Rayonner authentiquement sans écraser, briller en élevant les autres aussi.""",
        'weekly_advice': {
            'week_1': "Lance quelque chose qui te met en lumière positivement.",
            'week_2': "Assume pleinement ton charisme sans t'excuser.",
            'week_3': "Utilise ton rayonnement pour inspirer ton entourage.",
            'week_4': "Vérifie que ton ego reste au service de ton cœur."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Action précise**

Ta Lune en Bélier en Maison 1 veut s'affirmer avec spontanéité et énergie. Ton Ascendant Vierge apporte analyse et perfectionnisme : tu veux agir, mais de la bonne manière. L'instinct rencontre la méthode.

**Domaine activé** : Maison 1 — Ton image personnelle et ton identité demandent à la fois audace et précision. Tu veux t'améliorer, te perfectionner, devenir la meilleure version de toi-même.

**Ton approche instinctive** : La Vierge te fait observer avant d'agir, ajuster ton approche. Tu peux critiquer ta propre impulsivité. Cette autocritique peut être utile ou paralysante selon le dosage.

**Tensions possibles** : Le perfectionnisme peut empêcher l'action spontanée. Tu risques de trop analyser ton image au lieu de simplement être toi-même.

**Conseil clé** : Agir avec détermination tout en gardant un œil critique constructif.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect de toi que tu veux améliorer concrètement.",
            'week_2': "Mets en place une routine quotidienne qui sert cet objectif.",
            'week_3': "Ajuste ton approche sans te juger durement.",
            'week_4': "Mesure objectivement tes progrès ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Affirmation diplomatique**

Ta Lune en Bélier en Maison 1 veut foncer, s'affirmer sans compromis. Ton Ascendant Balance cherche l'harmonie et l'équilibre relationnel. Une tension créative entre l'affirmation de soi et la considération de l'autre.

**Domaine activé** : Maison 1 — Ton identité personnelle se construit dans la relation aux autres. Tu te demandes : comment être pleinement moi tout en restant en lien harmonieux ?

**Ton approche instinctive** : La Balance te fait hésiter, peser le pour et le contre avant d'agir. Tu cherches le bon moment, la bonne manière de t'affirmer sans brusquer. Cette diplomatie peut adoucir ta fougue.

**Tensions possibles** : Tu risques de trop te modérer pour plaire, ou au contraire d'exploser quand la frustration s'accumule. L'équilibre entre soi et l'autre est à trouver.

**Conseil clé** : S'affirmer avec élégance et fermeté, sans sacrifier ni soi ni la relation.""",
        'weekly_advice': {
            'week_1': "Clarifie ce qui est non-négociable pour toi.",
            'week_2': "Communique tes besoins avec douceur mais fermeté.",
            'week_3': "Trouve des compromis qui te respectent vraiment.",
            'week_4': "Évalue si tu t'es trahi·e ou affirmé·e ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Intensité transformatrice**

Ta Lune en Bélier en Maison 1 veut s'affirmer avec courage et spontanéité. Ton Ascendant Scorpion ajoute profondeur et intensité : tu ne te contentes pas d'exister, tu veux te transformer radicalement, mourir et renaître.

**Domaine activé** : Maison 1 — Ton identité personnelle traverse une crise de métamorphose. Tu veux détruire les vieilles versions de toi pour révéler quelque chose de plus authentique et puissant.

**Ton approche instinctive** : Le Scorpion te fait tout vivre à fond. Tes émotions sont extrêmes, tes réactions passionnées. Tu n'as pas peur de regarder tes zones d'ombre en face.

**Tensions possibles** : L'intensité peut devenir épuisante pour toi et les autres. Tu risques de te perdre dans des obsessions identitaires ou de vouloir contrôler ton évolution au lieu de la laisser se faire.

**Conseil clé** : Embrasser la transformation sans forcer, laisser l'ancienne peau tomber naturellement.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui en toi demande à mourir.",
            'week_2': "Lâche une vieille croyance sur qui tu es.",
            'week_3': "Accueille l'inconfort de ne plus savoir qui tu es.",
            'week_4': "Observe qui tu deviens dans ce vide fertile."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventure identitaire**

Double feu expansif sur ton identité : Lune Bélier en Maison 1 et Ascendant Sagittaire. Tu veux te découvrir à travers l'aventure, l'exploration, le dépassement. Ton identité se construit dans le mouvement et la quête.

**Domaine activé** : Maison 1 — Ton image personnelle cherche à s'élargir, à intégrer de nouvelles dimensions. Tu veux devenir quelqu'un de plus grand, plus libre, plus vivant. Les horizons t'appellent.

**Ton approche instinctive** : Le Sagittaire te pousse à voir loin et large. Tu abordes ton développement personnel comme une quête philosophique. Cette vision optimiste donne confiance.

**Tensions possibles** : L'excès d'optimisme peut te faire surestimer tes capacités. Tu risques de te disperser en voulant tout expérimenter ou de fuir l'introspection par l'action constante.

**Conseil clé** : Explorer tout en gardant un fil conducteur identitaire clair.""",
        'weekly_advice': {
            'week_1': "Définis une quête personnelle inspirante pour ce mois.",
            'week_2': "Sors de ta zone de confort de manière significative.",
            'week_3': "Intègre les leçons apprises dans ton identité.",
            'week_4': "Célèbre qui tu deviens à travers l'expérience."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Autorité construite**

Ta Lune en Bélier en Maison 1 veut s'affirmer avec fougue et spontanéité. Ton Ascendant Capricorne apporte structure et ambition : tu veux construire une image personnelle solide, respectable, qui dure dans le temps.

**Domaine activé** : Maison 1 — Ton identité personnelle se professionnalise. Tu veux être pris·e au sérieux, incarner l'autorité et la compétence. L'image que tu projettes devient stratégique.

**Ton approche instinctive** : Le Capricorne te fait planifier ton développement personnel comme un projet à long terme. Tu es prêt·e à travailler dur maintenant pour devenir quelqu'un d'important plus tard.

**Tensions possibles** : L'impulsivité du Bélier peut entrer en conflit avec la discipline du Capricorne. Tu risques d'osciller entre spontanéité et rigidité.

**Conseil clé** : Construire ton identité avec patience tout en gardant ta flamme intérieure.""",
        'weekly_advice': {
            'week_1': "Définis l'image professionnelle que tu veux incarner.",
            'week_2': "Pose un acte concret qui sert cette image.",
            'week_3': "Persévère dans tes habitudes même si c'est difficile.",
            'week_4': "Mesure les progrès accomplis vers ton objectif identitaire."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Originalité rebelle**

Ta Lune en Bélier en Maison 1 veut s'affirmer avec courage et authenticité. Ton Ascendant Verseau ajoute une dimension d'originalité radicale : tu veux te démarquer, être unique, casser les codes établis de l'identité.

**Domaine activé** : Maison 1 — Ton image personnelle cherche l'innovation et la différence. Tu refuses de te conformer aux attentes sociales. Ta manière d'être dans le monde devient un acte de rébellion.

**Ton approche instinctive** : Le Verseau te fait expérimenter avec qui tu es. Tu n'as pas peur d'être bizarre, décalé·e, incompris·e. Cette liberté peut être libératrice mais aussi isolante.

**Tensions possibles** : Être différent·e juste pour l'être peut devenir une prison. Tu risques de rejeter tout ce qui est conventionnel même quand ça pourrait t'aider.

**Conseil clé** : Être authentiquement unique sans faire de ta différence une identité rigide.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui en toi est vraiment original et authentique.",
            'week_2': "Ose exprimer publiquement cet aspect unique.",
            'week_3': "Trouve ta tribu, ceux qui apprécient ton originalité.",
            'week_4': "Vérifie que ta rébellion te libère vraiment."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Guerrier mystique**

Ta Lune en Bélier en Maison 1 veut s'affirmer avec force et détermination. Ton Ascendant Poissons ajoute fluidité et sensibilité spirituelle : tu es un·e guerrier·ère qui se bat pour des causes invisibles, pour l'âme.

**Domaine activé** : Maison 1 — Ton identité personnelle oscille entre force d'action et dissolution mystique. Tu cherches à être à la fois toi-même et relié·e à quelque chose de plus grand.

**Ton approche instinctive** : Le Poissons te fait aborder la vie avec intuition et empathie. Tu ressens plus que tu ne comprends. Cette sensibilité peut adoucir ou diluer ta fougue naturelle.

**Tensions possibles** : Tu risques de perdre tes limites, de te dissoudre dans les autres ou dans des idéaux flous. L'action claire devient difficile quand tout est ressenti comme interconnecté.

**Conseil clé** : Honorer ta sensibilité tout en maintenant des frontières claires.""",
        'weekly_advice': {
            'week_1': "Médite sur qui tu es au-delà de l'ego et des rôles.",
            'week_2': "Agis pour une cause qui te touche spirituellement.",
            'week_3': "Protège ton énergie des influences extérieures.",
            'week_4': "Intègre tes insights mystiques dans des actions concrètes."
        }
    },

    # ==================== MAISON 3 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Communication-action**

Double feu sur la Maison 3 : ta Lune en Bélier et ton Ascendant Bélier activent intensément ta communication, tes apprentissages, ton environnement proche. Tu veux parler vite, apprendre vite, bouger vite. L'immobilité mentale t'est insupportable.

**Domaine activé** : Maison 3 — Tes échanges quotidiens, tes trajets, ta curiosité intellectuelle sont électrifiés. Tu veux débattre, convaincre, découvrir. Chaque conversation devient un terrain d'affirmation.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu communiques de manière directe et sans filtre. Tu dis ce que tu penses instantanément. Cette franchise peut rafraîchir ou blesser.

**Tensions possibles** : Tu risques de parler avant de réfléchir, de brusquer dans tes échanges. L'impatience peut te faire mal comprendre les autres ou être mal compris·e.

**Conseil clé** : Canaliser ton énergie verbale vers des apprentissages stimulants et des débats constructifs.""",
        'weekly_advice': {
            'week_1': "Initie une conversation importante que tu repoussais.",
            'week_2': "Apprends quelque chose de nouveau qui t'excite vraiment.",
            'week_3': "Écoute autant que tu parles dans tes échanges.",
            'week_4': "Fais le point sur ce que tu as découvert ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Parole ancrée**

Ta Lune en Bélier en Maison 3 veut communiquer vite et apprendre rapidement. Ton Ascendant Taureau apporte une dimension de réflexion et de pragmatisme : tu veux que tes mots aient du poids, que tes apprentissages soient concrets et utiles.

**Domaine activé** : Maison 3 — Tes échanges et ta communication cherchent à la fois spontanéité et substance. Tu veux dire les choses directement mais aussi qu'elles aient un impact durable.

**Ton approche instinctive** : Le Taureau te fait peser tes mots avant de les prononcer. Tu peux être lent·e à répondre mais quand tu le fais, c'est réfléchi. Cette stabilité tempère l'impulsivité du Bélier.

**Tensions possibles** : La frustration monte quand tu dois répéter ou expliquer lentement. Tu veux aller vite mais ton besoin de solidité te ralentit.

**Conseil clé** : Communiquer avec clarté et fermeté sans précipitation inutile.""",
        'weekly_advice': {
            'week_1': "Identifie un sujet que tu veux vraiment maîtriser.",
            'week_2': "Apprends méthodiquement, pas par à-coups.",
            'week_3': "Exprime une opinion importante de manière posée.",
            'week_4': "Vérifie que tes apprentissages sont ancrés durablement."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Curiosité explosive**

Ta Lune en Bélier en Maison 3 veut apprendre et communiquer avec énergie. Ton Ascendant Gémeaux, maître naturel de cette maison, amplifie cette dynamique : tu es une éponge intellectuelle survoltée. L'information devient ton terrain de jeu.

**Domaine activé** : Maison 3 — Tes apprentissages, tes échanges, ta communication sont au maximum de leur capacité. Tu peux jongler avec plusieurs sujets, plusieurs conversations, plusieurs projets intellectuels simultanément.

**Ton approche instinctive** : Le Gémeaux te fait papillonner d'un sujet à l'autre avec agilité. Tu adores découvrir, partager, connecter les idées. Cette versatilité est à la fois ta force et ton défi.

**Tensions possibles** : La dispersion intellectuelle peut t'empêcher d'approfondir vraiment. Tu risques de survoler tout sans rien maîtriser, de parler sans vraiment écouter.

**Conseil clé** : Choisir 2-3 domaines d'apprentissage maximum et s'y engager ce mois-ci.""",
        'weekly_advice': {
            'week_1': "Liste tout ce que tu veux apprendre, puis sélectionne l'essentiel.",
            'week_2': "Approfondis un sujet au lieu d'en effleurer dix.",
            'week_3': "Partage tes découvertes de manière structurée.",
            'week_4': "Évalue ce que tu as vraiment retenu et intégré."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Communication sensible**

Ta Lune en Bélier en Maison 3 veut s'exprimer avec franchise et spontanéité. Ton Ascendant Cancer ajoute une dimension émotionnelle : tes mots portent des sentiments profonds, tes apprentissages touchent ton cœur.

**Domaine activé** : Maison 3 — Tes échanges quotidiens et ta communication sont chargés d'émotion. Tu veux parler de ce qui compte vraiment, créer des liens authentiques à travers la parole.

**Ton approche instinctive** : Le Cancer te fait communiquer par vagues émotionnelles. Tu peux être bavard·e puis silencieux·se selon ton état intérieur. Cette sensibilité dans les mots peut créer de l'intimité.

**Tensions possibles** : Tu risques de prendre les remarques trop à cœur ou de te fermer quand tu te sens blessé·e. L'impulsivité verbale du Bélier peut contredire ta prudence émotionnelle.

**Conseil clé** : Exprimer tes émotions directement tout en restant à l'écoute de celles des autres.""",
        'weekly_advice': {
            'week_1': "Partage quelque chose de personnel avec quelqu'un de confiance.",
            'week_2': "Apprends quelque chose qui nourrit ton cœur.",
            'week_3': "Protège-toi des échanges toxiques ou blessants.",
            'week_4': "Remercie ceux qui ont écouté vraiment ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Expression brillante**

Double feu sur la Maison 3 : ta Lune en Bélier et ton Ascendant Lion créent une communication charismatique et passionnée. Tu veux que tes mots inspirent, captivent, marquent les esprits. Chaque échange devient une performance.

**Domaine activé** : Maison 3 — Ta communication et tes apprentissages cherchent l'excellence et la reconnaissance. Tu veux briller intellectuellement, être celui·celle qui dit les choses importantes avec panache.

**Ton approche instinctive** : Le Lion te fait communiquer avec générosité et théâtralité. Tu racontes des histoires, tu inspires. Cette capacité à captiver l'attention est magnétique.

**Tensions possibles** : Le besoin d'être admiré·e peut te faire monopoliser la parole. Tu risques de communiquer pour impressionner plutôt que pour échanger vraiment.

**Conseil clé** : Utiliser ton charisme verbal pour élever les conversations, pas pour dominer.""",
        'weekly_advice': {
            'week_1': "Partage une idée qui te tient à cœur avec passion.",
            'week_2': "Apprends quelque chose qui renforce ton expertise.",
            'week_3': "Donne la parole aux autres, sois un·e hôte généreux·se.",
            'week_4': "Célèbre les échanges enrichissants de ce mois."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision vive**

Ta Lune en Bélier en Maison 3 veut communiquer et apprendre rapidement. Ton Ascendant Vierge apporte analyse et méthodologie : tu veux non seulement comprendre vite, mais comprendre juste. La qualité rencontre la vitesse.

**Domaine activé** : Maison 3 — Tes apprentissages et ta communication cherchent l'efficacité et l'utilité. Tu veux acquérir des compétences pratiques, dire des choses qui servent vraiment.

**Ton approche instinctive** : La Vierge te fait observer les détails, corriger les erreurs. Tu peux être critique dans tes échanges, cherchant toujours à améliorer la précision de l'information.

**Tensions possibles** : Le perfectionnisme peut ralentir ta communication naturellement spontanée. Tu risques de trop corriger les autres ou de t'auto-censurer par souci de justesse.

**Conseil clé** : Accepter l'imperfection de la communication tout en visant la clarté.""",
        'weekly_advice': {
            'week_1': "Identifie une compétence concrète à développer.",
            'week_2': "Apprends méthodiquement, étape par étape.",
            'week_3': "Partage tes connaissances de manière pédagogique.",
            'week_4': "Évalue objectivement tes progrès d'apprentissage."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Dialogue équilibré**

Ta Lune en Bélier en Maison 3 veut s'exprimer franchement et directement. Ton Ascendant Balance cherche l'harmonie et l'équilibre dans les échanges : tu veux dire ta vérité mais sans rompre la relation. La diplomatie rencontre la franchise.

**Domaine activé** : Maison 3 — Ta communication cherche à la fois authenticité et élégance. Tu veux des échanges vrais mais justes, des débats qui éclairent plutôt que divisent.

**Ton approche instinctive** : La Balance te fait peser tes mots, chercher l'angle qui permettra à l'autre d'entendre. Cette sensibilité relationnelle peut adoucir la brutalité du Bélier.

**Tensions possibles** : Tu risques de trop édulcorer ton message pour plaire, ou d'exploser après avoir trop retenu. Trouver l'équilibre entre vérité et tact est un défi constant.

**Conseil clé** : Dire ce qui doit être dit avec grâce mais sans compromis sur le fond.""",
        'weekly_advice': {
            'week_1': "Prépare une conversation difficile avec soin.",
            'week_2': "Exprime ton désaccord de manière constructive.",
            'week_3': "Écoute vraiment le point de vue opposé.",
            'week_4': "Vérifie que tu n'as pas sacrifié ta vérité pour la paix."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Parole intense**

Ta Lune en Bélier en Maison 3 veut communiquer avec énergie et franchise. Ton Ascendant Scorpion ajoute profondeur et intensité : tes mots cherchent à atteindre l'essentiel, à transformer, à révéler ce qui est caché.

**Domaine activé** : Maison 3 — Ta communication et tes apprentissages ne s'intéressent qu'aux sujets profonds. Les bavardages superficiels t'ennuient. Tu veux parler de ce qui compte vraiment, comprendre les mécanismes cachés.

**Ton approche instinctive** : Le Scorpion te fait creuser sous la surface. Tu poses des questions qui dérangent, tu cherches la vérité même si elle est inconfortable. Cette intensité peut intimider.

**Tensions possibles** : Tu risques d'être trop brutal·e dans tes révélations ou obsessionnel·le dans tes quêtes intellectuelles. L'excès d'intensité peut fermer les échanges.

**Conseil clé** : Utiliser ton pouvoir de pénétration intellectuelle avec responsabilité.""",
        'weekly_advice': {
            'week_1': "Identifie une vérité que tu dois dire ou entendre.",
            'week_2': "Apprends quelque chose sur les dynamiques psychologiques.",
            'week_3': "Aie une conversation vraie, sans masques.",
            'week_4': "Vérifie que ta quête de vérité guérit au lieu de détruire."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Communication visionnaire**

Double feu expansif sur la Maison 3 : ta Lune en Bélier et ton Ascendant Sagittaire créent une communication inspirante et optimiste. Tu veux partager ta vision, enseigner, élargir les horizons mentaux de tous.

**Domaine activé** : Maison 3 — Tes apprentissages et échanges cherchent du sens et de la portée. Tu ne veux pas juste parler, mais inspirer. Chaque conversation peut devenir une leçon de vie.

**Ton approche instinctive** : Le Sagittaire te fait communiquer avec enthousiasme et foi. Tu vois le grand tableau, tu relies les idées à des principes universels. Cette perspective élargie est contagieuse.

**Tensions possibles** : Tu risques de prêcher au lieu d'échanger, de généraliser trop rapidement. Ton excès d'optimisme peut te faire ignorer les détails pratiques.

**Conseil clé** : Inspirer tout en restant ancré·e dans la réalité des échanges quotidiens.""",
        'weekly_advice': {
            'week_1': "Partage une idée qui pourrait inspirer d'autres.",
            'week_2': "Apprends quelque chose qui élargit ta vision du monde.",
            'week_3': "Écoute les perspectives différentes sans juger.",
            'week_4': "Vérifie que ton enthousiasme s'ancre dans le concret."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Communication stratégique**

Ta Lune en Bélier en Maison 3 veut communiquer spontanément et directement. Ton Ascendant Capricorne apporte structure et prudence : chaque mot doit servir un objectif, chaque apprentissage doit être utile à long terme.

**Domaine activé** : Maison 3 — Ta communication devient professionnelle et efficace. Tu veux que tes échanges construisent ta crédibilité, que tes apprentissages servent ton ambition.

**Ton approche instinctive** : Le Capricorne te fait réfléchir avant de parler. Tu communiques avec autorité et sérieux. Cette maîtrise peut impressionner mais aussi créer de la distance.

**Tensions possibles** : L'impulsivité verbale du Bélier peut entrer en conflit avec ta prudence stratégique. Tu risques d'osciller entre spontanéité et contrôle excessif.

**Conseil clé** : Communiquer avec authenticité tout en gardant tes objectifs à long terme en vue.""",
        'weekly_advice': {
            'week_1': "Définis quelles compétences de communication tu veux développer.",
            'week_2': "Apprends quelque chose qui sert directement tes ambitions.",
            'week_3': "Communique professionnellement sans perdre ton humanité.",
            'week_4': "Mesure l'impact de tes échanges ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Communication révolutionnaire**

Ta Lune en Bélier en Maison 3 veut s'exprimer avec énergie et originalité. Ton Ascendant Verseau ajoute une dimension d'innovation : tu veux communiquer différemment, partager des idées avant-gardistes, bousculer la pensée établie.

**Domaine activé** : Maison 3 — Ta communication et tes apprentissages cherchent l'originalité et la rupture. Tu ne veux pas répéter ce que tout le monde dit. Tu veux apporter une perspective unique.

**Ton approche instinctive** : Le Verseau te fait expérimenter avec la forme et le fond de tes messages. Tu peux être déconcertant·e, provocateur·rice intellectuellement. Cette originalité attire ou repousse.

**Tensions possibles** : Être différent·e juste pour l'être peut nuire à la clarté. Tu risques de te marginaliser en refusant toute convention de communication.

**Conseil clé** : Innover dans ta communication tout en restant compréhensible.""",
        'weekly_advice': {
            'week_1': "Explore une manière non-conventionnelle de communiquer.",
            'week_2': "Apprends quelque chose de futuriste ou d'avant-garde.",
            'week_3': "Partage une idée qui peut bousculer les perspectives.",
            'week_4': "Vérifie que ton originalité sert vraiment l'échange."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Parole intuitive**

Ta Lune en Bélier en Maison 3 veut communiquer directement et clairement. Ton Ascendant Poissons ajoute intuition et poésie : tes mots portent des dimensions invisibles, des résonances émotionnelles et spirituelles.

**Domaine activé** : Maison 3 — Ta communication et tes apprentissages sont guidés par l'intuition. Tu ressens ce qui doit être dit plus que tu ne le calcules. Les échanges deviennent des moments de connexion profonde.

**Ton approche instinctive** : Le Poissons te fait communiquer par images, métaphores, sensations. Tu peux être flou·e mais profondément juste. Cette dimension poétique touche l'âme.

**Tensions possibles** : La clarté du Bélier se dissout dans les brumes du Poissons. Tu risques de ne pas savoir exprimer précisément ce que tu ressens, ou de te perdre dans des digressions.

**Conseil clé** : Honorer ton intuition verbale tout en cherchant à articuler clairement.""",
        'weekly_advice': {
            'week_1': "Fais confiance à ce que ton intuition te pousse à dire.",
            'week_2': "Apprends quelque chose de créatif ou de spirituel.",
            'week_3': "Communique avec poésie mais aussi avec précision.",
            'week_4': "Vérifie que tes messages ont été vraiment compris."
        }
    },

    # ==================== MAISON 4 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Foyer-action**

Double feu sur la Maison 4 : ta Lune en Bélier et ton Ascendant Bélier activent intensément ton besoin de foyer et de racines, mais d'une manière dynamique. Tu veux créer ta base, ton refuge, mais à ta façon, rapidement, sans compromis.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes racines émotionnelles demandent ton attention. Tu peux vouloir déménager, rénover, redéfinir ce que "chez toi" signifie. L'intérieur appelle l'action.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu abordes même ton intimité avec fougue. Tu peux bousculer les dynamiques familiales, imposer tes besoins de sécurité sans attendre l'approbation.

**Tensions possibles** : L'impatience peut créer des conflits familiaux ou domestiques. Tu risques de vouloir tout changer d'un coup dans ton espace de vie sans considérer les autres.

**Conseil clé** : Construire ton sanctuaire personnel avec détermination tout en respectant le processus.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque à ton sentiment de chez-toi.",
            'week_2': "Prends une initiative concrète pour améliorer ton espace.",
            'week_3': "Adresse une tension familiale de manière directe mais constructive.",
            'week_4': "Célèbre le nid que tu as créé ou amélioré."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Racines solides**

Ta Lune en Bélier en Maison 4 veut agir vite pour créer sa sécurité émotionnelle. Ton Ascendant Taureau apporte une dimension de stabilité et de confort : tu veux un foyer beau, tangible, durable. La spontanéité rencontre la construction.

**Domaine activé** : Maison 4 — Ton espace de vie et tes fondations émotionnelles cherchent à la fois renouveau et solidité. Tu veux que ton chez-toi soit à la fois un lieu d'action et de repos profond.

**Ton approche instinctive** : Le Taureau te fait investir dans le confort et la beauté de ton foyer. Tu veux du concret, du tangible, du douillet. Cette approche sensuelle ancre bien l'impulsivité du Bélier.

**Tensions possibles** : L'impatience du Bélier peut se heurter à ton besoin de prendre le temps de bien faire. Tu risques de vouloir tout immédiatement alors que la construction demande de la patience.

**Conseil clé** : Investir progressivement dans ton espace de vie avec qualité et permanence.""",
        'weekly_advice': {
            'week_1': "Définis clairement à quoi ressemble ton foyer idéal.",
            'week_2': "Achète ou crée un objet qui embellit vraiment ton espace.",
            'week_3': "Prends le temps de savourer ton chez-toi.",
            'week_4': "Ancre-toi dans la stabilité que tu as construite."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Foyer mobile**

Ta Lune en Bélier en Maison 4 veut créer sa sécurité émotionnelle de manière autonome. Ton Ascendant Gémeaux ajoute curiosité et mouvement : ton chez-toi peut être multiple, changeant, stimulant intellectuellement.

**Domaine activé** : Maison 4 — Ton foyer et tes racines cherchent variété et stimulation. Tu peux avoir besoin de plusieurs espaces, de réorganiser souvent, de créer un lieu qui nourrit ton mental.

**Ton approche instinctive** : Le Gémeaux te fait aborder ton espace de vie avec légèreté. Tu peux déménager facilement, transformer constamment ton intérieur. Cette flexibilité peut perturber ou libérer.

**Tensions possibles** : Trop de changement peut t'empêcher de vraiment t'enraciner. Tu risques de fuir l'intimité émotionnelle profonde par le mouvement constant.

**Conseil clé** : Créer un foyer qui permet à la fois stabilité et variété.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te fait sentir vraiment chez toi.",
            'week_2': "Réorganise un espace pour qu'il soit plus stimulant.",
            'week_3': "Invite des échanges nourrissants dans ton foyer.",
            'week_4': "Vérifie que ton besoin de changement ne cache pas une fuite."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Refuge ardent**

Ta Lune en Bélier en Maison 4 veut construire activement sa sécurité. Ton Ascendant Cancer, maître naturel de cette maison, amplifie le besoin de foyer : ton chez-toi devient ton sanctuaire émotionnel absolu, à protéger férocement.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes racines profondes sont au cœur de tout. Tu veux créer un nid où tu peux être totalement toi-même, vulnérable, en sécurité. La protection est primordiale.

**Ton approche instinctive** : Le Cancer te fait investir émotionnellement à fond dans ton espace de vie. Tu nourris, tu protèges, tu prends soin. Cette sensibilité domestique peut apaiser l'agitation du Bélier.

**Tensions possibles** : L'impulsivité peut créer des vagues émotionnelles dans ta famille. Tu risques d'être sur-protecteur·rice ou de te replier trop sur ton cocon.

**Conseil clé** : Créer un foyer sécurisant sans s'y enfermer émotionnellement.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui nourrit vraiment ton besoin de sécurité.",
            'week_2': "Crée un rituel qui ancre la douceur dans ton quotidien.",
            'week_3': "Adresse les blessures familiales avec courage et tendresse.",
            'week_4': "Remercie ton foyer d'exister tel qu'il est."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Palais personnel**

Double feu sur la Maison 4 : ta Lune en Bélier et ton Ascendant Lion veulent un foyer majestueux, chaleureux, rayonnant. Ton chez-toi doit refléter ta grandeur, être un lieu où tu règnes avec générosité.

**Domaine activé** : Maison 4 — Ton espace de vie et tes racines émotionnelles cherchent l'éclat et la fierté. Tu veux que ton foyer soit beau, accueillant, impressionnant. C'est ton royaume privé.

**Ton approche instinctive** : Le Lion te fait investir dans la beauté et le confort noble de ton chez-toi. Tu veux recevoir, rayonner depuis ta base. Cette générosité domestique crée de la chaleur.

**Tensions possibles** : Le besoin d'impressionner peut te faire dépenser trop pour ton intérieur. Tu risques de confondre confort authentique et parade.

**Conseil clé** : Créer un foyer qui nourrit ton cœur, pas juste ton image.""",
        'weekly_advice': {
            'week_1': "Imagine ton foyer idéal sans limite de budget, puis adapte.",
            'week_2': "Investis dans un élément qui apporte vraiment de la chaleur.",
            'week_3': "Partage généreusement ton espace avec ceux que tu aimes.",
            'week_4': "Célèbre ton foyer comme un roi·une reine son château."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Foyer fonctionnel**

Ta Lune en Bélier en Maison 4 veut agir pour améliorer son espace de vie. Ton Ascendant Vierge apporte organisation et efficacité : chaque élément de ton foyer doit avoir une fonction, une utilité. La spontanéité rencontre la méthode.

**Domaine activé** : Maison 4 — Ton chez-toi cherche à être à la fois vivant et parfaitement organisé. Tu veux optimiser ton espace, éliminer le superflu, créer un système domestique qui fonctionne bien.

**Ton approche instinctive** : La Vierge te fait analyser et améliorer constamment ton environnement. Tu peux être critique de ton espace ou de ta famille. Cette exigence peut être constructive ou épuisante.

**Tensions possibles** : Le perfectionnisme peut t'empêcher de simplement profiter de ton chez-toi. Tu risques de toujours voir ce qui ne va pas au lieu de ce qui va bien.

**Conseil clé** : Créer un foyer efficace tout en acceptant l'imperfection vivante.""",
        'weekly_advice': {
            'week_1': "Audite ton espace : qu'est-ce qui fonctionne et qu'est-ce qui coince ?",
            'week_2': "Organise méthodiquement une zone de ton foyer.",
            'week_3': "Accepte que ton chez-toi soit vivant, donc imparfait.",
            'week_4': "Apprécie l'ordre que tu as créé sans chercher la perfection."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie domestique**

Ta Lune en Bélier en Maison 4 veut créer son espace personnel avec détermination. Ton Ascendant Balance cherche l'harmonie et la beauté : ton foyer doit être équilibré, esthétique, un lieu de paix relationnelle.

**Domaine activé** : Maison 4 — Ton chez-toi et tes relations familiales cherchent l'équilibre. Tu veux à la fois ton autonomie et des liens harmonieux. Le défi est de créer un foyer qui respecte tous.

**Ton approche instinctive** : La Balance te fait chercher le compromis dans les décisions domestiques. Tu veux que chacun se sente bien chez toi. Cette diplomatie peut apaiser les tensions.

**Tensions possibles** : Tu risques de sacrifier tes besoins de foyer pour maintenir la paix. L'impulsivité du Bélier peut exploser après trop de compromis accumulés.

**Conseil clé** : Créer un foyer beau et harmonieux qui honore aussi tes besoins personnels.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui crée de l'harmonie dans ton espace.",
            'week_2': "Embellis un coin de ton foyer avec soin.",
            'week_3': "Négocie un équilibre familial qui te respecte vraiment.",
            'week_4': "Vérifie que ton foyer reflète qui tu es, pas juste les autres."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Refuge intense**

Ta Lune en Bélier en Maison 4 veut construire sa sécurité avec détermination. Ton Ascendant Scorpion ajoute profondeur et transformation : ton foyer devient un lieu de métamorphose émotionnelle, un espace sacré et protégé.

**Domaine activé** : Maison 4 — Ton chez-toi et tes racines profondes traversent une période intense. Tu peux vouloir tout transformer dans ton espace de vie, éliminer les énergies stagnantes, recréer ton sanctuaire.

**Ton approche instinctive** : Le Scorpion te fait vivre ton foyer avec intensité émotionnelle. Tu protèges férocement ton espace privé. Les secrets familiaux peuvent remonter à la surface.

**Tensions possibles** : L'obsession du contrôle peut créer une atmosphère lourde. Tu risques de t'isoler dans ton cocon ou de vouloir contrôler tous les membres de ta famille.

**Conseil clé** : Transformer ton espace de vie en profondeur sans t'y enfermer émotionnellement.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui dans ton foyer demande une transformation profonde.",
            'week_2': "Nettoie énergétiquement ton espace, élimine le mort.",
            'week_3': "Adresse une vérité familiale difficile mais nécessaire.",
            'week_4': "Observe comment ton foyer est devenu plus authentique."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foyer aventureux**

Double feu expansif sur la Maison 4 : ta Lune en Bélier et ton Ascendant Sagittaire créent un rapport au foyer non-conventionnel. Tu veux un chez-toi qui soit une base de lancement pour l'aventure, pas une cage.

**Domaine activé** : Maison 4 — Ton espace de vie et tes racines cherchent à la fois ancrage et liberté. Tu peux vouloir voyager tout en ayant un port d'attache, ou créer un foyer qui reflète tes explorations.

**Ton approche instinctive** : Le Sagittaire te fait voir ton foyer comme temporaire ou multiple. Tu peux avoir du mal à t'enraciner définitivement. Cette liberté peut être libératrice ou déstabilisante.

**Tensions possibles** : La fuite de l'intimité domestique par l'aventure constante. Tu risques de négliger ton besoin profond de sécurité émotionnelle.

**Conseil clé** : Créer un foyer qui permet à la fois stabilité et expansion.""",
        'weekly_advice': {
            'week_1': "Définis ce que 'chez toi' signifie pour toi vraiment.",
            'week_2': "Intègre dans ton espace des souvenirs de tes aventures.",
            'week_3': "Autorise-toi à t'ancrer sans te sentir prisonnier·ère.",
            'week_4': "Célèbre ton foyer comme une base, pas une limite."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fondations structurées**

Ta Lune en Bélier en Maison 4 veut construire sa sécurité rapidement. Ton Ascendant Capricorne apporte vision long terme et structure : ton foyer doit être solide, durable, un investissement qui traverse le temps.

**Domaine activé** : Maison 4 — Ton espace de vie et tes racines familiales deviennent un projet d'ambition. Tu veux construire des fondations émotionnelles et matérielles qui te servent pendant des décennies.

**Ton approche instinctive** : Le Capricorne te fait planifier ton foyer comme on bâtit un empire. Tu es prêt·e à investir maintenant pour la stabilité future. Cette discipline canalise bien l'impulsivité du Bélier.

**Tensions possibles** : L'impatience peut se heurter à la lenteur de la construction solide. Tu risques de te frustrer si ton chez-toi ne correspond pas immédiatement à ton idéal.

**Conseil clé** : Construire ton foyer pierre par pierre avec patience et vision.""",
        'weekly_advice': {
            'week_1': "Définis à quoi ressemble ton foyer dans 10 ans.",
            'week_2': "Pose une action concrète qui sert cette vision.",
            'week_3': "Investis dans quelque chose de durable pour ton espace.",
            'week_4': "Mesure les fondations posées ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Foyer alternatif**

Ta Lune en Bélier en Maison 4 veut créer sa sécurité de manière autonome. Ton Ascendant Verseau ajoute originalité et innovation : ton chez-toi doit être unique, peut-être communautaire ou technologique, en tout cas pas conventionnel.

**Domaine activé** : Maison 4 — Ton espace de vie et ta conception du foyer sortent des sentiers battus. Tu peux expérimenter avec des modes de vie alternatifs, des espaces partagés, des solutions innovantes.

**Ton approche instinctive** : Le Verseau te fait voir ton foyer comme un projet social ou technologique. Tu veux que ton espace reflète tes idéaux progressistes. Cette originalité peut être inspirante.

**Tensions possibles** : Rejeter toute tradition peut te priver de la chaleur simple du foyer. Tu risques d'intellectualiser tes besoins émotionnels de base.

**Conseil clé** : Innover dans ton espace de vie tout en honorant tes besoins humains simples.""",
        'weekly_advice': {
            'week_1': "Explore des manières non-conventionnelles d'habiter.",
            'week_2': "Teste une idée originale pour ton espace de vie.",
            'week_3': "Connecte-toi à une communauté qui partage tes valeurs.",
            'week_4': "Vérifie que ton originalité te nourrit vraiment."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sanctuaire fluide**

Ta Lune en Bélier en Maison 4 veut créer sa sécurité avec détermination. Ton Ascendant Poissons ajoute dimension spirituelle et sensibilité : ton foyer devient un temple, un espace de guérison et de connexion à l'invisible.

**Domaine activé** : Maison 4 — Ton chez-toi et tes racines cherchent à la fois ancrage et transcendance. Tu veux un espace qui nourrit ton âme, où tu peux méditer, rêver, te dissoudre en paix.

**Ton approche instinctive** : Le Poissons te fait créer un foyer intuitif, fluide, peut-être un peu chaotique. Tu ressens l'énergie des lieux. Cette sensibilité peut créer des espaces magiques.

**Tensions possibles** : L'impulsivité du Bélier se dilue dans les brumes du Poissons. Tu risques de fuir la structure nécessaire au foyer ou de te perdre dans l'imaginaire.

**Conseil clé** : Créer un foyer qui nourrit l'âme tout en maintenant des limites claires.""",
        'weekly_advice': {
            'week_1': "Médite sur l'énergie que tu veux dans ton espace.",
            'week_2': "Crée un coin spirituel ou créatif chez toi.",
            'week_3': "Nettoie énergétiquement ton foyer avec intention.",
            'week_4': "Remercie ton espace d'être ton sanctuaire."
        }
    },

    # ==================== MAISON 5 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Passion pure**

Double feu sur la Maison 5 : ta Lune en Bélier et ton Ascendant Bélier créent une énergie créative et ludique explosive. Tu veux t'amuser, créer, séduire, t'exprimer sans retenue. Le plaisir devient une priorité vitale.

**Domaine activé** : Maison 5 — Ta créativité, tes loisirs, ta vie amoureuse et ton expression personnelle demandent toute ton énergie. Tu veux vivre intensément, prendre des risques pour le plaisir, jouer à fond.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu plonges tête première dans ce qui t'excite. Tu ne calcules pas, tu ressens et tu agis. Cette spontanéité rend la vie palpitante.

**Tensions possibles** : L'excès de prise de risques peut mener à des situations complexes. Tu peux brûler trop vite tes plaisirs ou brusquer dans tes élans romantiques.

**Conseil clé** : Vivre tes passions pleinement tout en gardant une conscience minimum des conséquences.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans un projet créatif qui t'enflamme.",
            'week_2': "Ose exprimer tes sentiments amoureux sans calcul.",
            'week_3': "Joue, amuse-toi, fais quelque chose juste pour le plaisir.",
            'week_4': "Célèbre ce que tu as créé et ressenti ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Plaisir sensuel**

Ta Lune en Bélier en Maison 5 veut créer et jouer avec passion. Ton Ascendant Taureau ajoute sensualité et appréciation : tu veux que tes plaisirs soient beaux, tangibles, délicieux. La spontanéité rencontre la qualité.

**Domaine activé** : Maison 5 — Ta créativité et tes loisirs cherchent à la fois intensité et beauté. Tu veux des expériences qui nourrissent tous tes sens, des créations qui ont de la substance.

**Ton approche instinctive** : Le Taureau te fait savourer lentement tes plaisirs. Tu veux que ça dure, que ce soit bon profondément. Cette sensualité peut enrichir ou ralentir ton feu créatif.

**Tensions possibles** : L'impatience du Bélier peut se heurter à ton besoin de prendre ton temps. Tu risques d'alterner entre fougue créative et blocage perfectionniste.

**Conseil clé** : Créer avec passion tout en prenant le temps de faire les choses bien.""",
        'weekly_advice': {
            'week_1': "Identifie un plaisir que tu veux vraiment savourer.",
            'week_2': "Crée quelque chose de beau avec tes mains.",
            'week_3': "Offre-toi une expérience sensorielle de qualité.",
            'week_4': "Ancre les joies vécues dans ta mémoire corporelle."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Jeu intellectuel**

Ta Lune en Bélier en Maison 5 veut s'exprimer et créer avec énergie. Ton Ascendant Gémeaux ajoute curiosité et versatilité : tu veux jouer avec les idées, les mots, les concepts. La créativité devient mentale et ludique.

**Domaine activé** : Maison 5 — Ta créativité et tes loisirs passent par la communication et l'apprentissage. Tu peux t'amuser à écrire, débattre, apprendre de nouvelles choses. Le plaisir est intellectuel.

**Ton approche instinctive** : Le Gémeaux te fait jouer avec la légèreté. Tu peux avoir plusieurs projets créatifs ou plusieurs flirts en même temps. Cette agilité rend la vie stimulante.

**Tensions possibles** : Trop de dispersion peut empêcher l'approfondissement créatif. Tu risques de papillonner sans vraiment créer quelque chose de complet.

**Conseil clé** : Jouer et explorer tout en choisissant quelques créations à vraiment développer.""",
        'weekly_advice': {
            'week_1': "Liste toutes les idées créatives qui te tentent.",
            'week_2': "Choisis-en une ou deux et commence à les matérialiser.",
            'week_3': "Partage tes créations, échange sur tes projets.",
            'week_4': "Évalue ce que tu as vraiment accompli versus juste pensé."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Création sensible**

Ta Lune en Bélier en Maison 5 veut s'exprimer avec fougue créative. Ton Ascendant Cancer ajoute profondeur émotionnelle : ta créativité vient du cœur, tes plaisirs sont liés à l'intimité, tes jeux protègent ta vulnérabilité.

**Domaine activé** : Maison 5 — Ta créativité et tes loisirs sont chargés d'émotion. Tu crées pour exprimer ce que tu ressens, tu joues quand tu te sens en sécurité. L'authenticité émotionnelle guide ton expression.

**Ton approche instinctive** : Le Cancer te fait créer depuis tes émotions profondes. Tu peux être timide puis explosif·ve artistiquement. Cette sensibilité donne une richesse émotionnelle à tes créations.

**Tensions possibles** : La peur d'être jugé·e peut bloquer ton expression. Tu risques d'hésiter entre t'exprimer franchement et te protéger émotionnellement.

**Conseil clé** : Créer courageusement depuis ton cœur sans craindre la vulnérabilité.""",
        'weekly_advice': {
            'week_1': "Identifie une émotion que tu veux exprimer créativement.",
            'week_2': "Crée quelque chose qui vient vraiment de ton cœur.",
            'week_3': "Partage ta création avec quelqu'un de confiance.",
            'week_4': "Célèbre le courage d'avoir été authentique."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Expression solaire**

Double feu sur la Maison 5, sa maison naturelle : ta Lune en Bélier et ton Ascendant Lion créent une créativité éclatante et un magnétisme romantique puissant. Tu veux briller, créer, séduire, être célébré·e.

**Domaine activé** : Maison 5 — Ta créativité, ton expression personnelle, ta vie amoureuse sont au sommet. Tu rayonnes naturellement. Tout ce que tu touches devient spectacle et inspiration pour les autres.

**Ton approche instinctive** : Le Lion te fait créer avec générosité et panache. Tu veux impressionner, inspirer, recevoir des applaudissements. Cette confiance créative est contagieuse.

**Tensions possibles** : Le besoin d'admiration peut rendre tes créations calculées. Tu risques de créer pour plaire plutôt que pour t'exprimer authentiquement.

**Conseil clé** : Créer depuis ton cœur généreux, pas depuis ton ego avide de reconnaissance.""",
        'weekly_advice': {
            'week_1': "Lance un projet créatif ambitieux qui te ressemble.",
            'week_2': "Exprime-toi publiquement, partage ton art ou tes talents.",
            'week_3': "Reçois les compliments avec grâce sans en devenir dépendant·e.",
            'week_4': "Célèbre tes créations et inspire les autres à créer aussi."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Artisanat passionné**

Ta Lune en Bélier en Maison 5 veut créer spontanément et jouer librement. Ton Ascendant Vierge apporte précision et perfectionnisme : tu veux que tes créations soient à la fois inspirées ET parfaitement exécutées.

**Domaine activé** : Maison 5 — Ta créativité cherche l'excellence technique. Tu veux maîtriser ton art, perfectionner ton expression. Le plaisir vient aussi du travail bien fait.

**Ton approche instinctive** : La Vierge te fait analyser et améliorer tes créations. Tu peux être ton critique le plus dur. Cette exigence peut élever ou bloquer ton expression créative.

**Tensions possibles** : Le perfectionnisme peut tuer la spontanéité créative. Tu risques de trop corriger au lieu de simplement laisser s'exprimer ton feu créatif.

**Conseil clé** : Créer avec passion puis affiner avec méthode, sans tuer l'élan initial.""",
        'weekly_advice': {
            'week_1': "Autorise-toi à créer sans jugement, version brouillon.",
            'week_2': "Affine ensuite une création qui te tient à cœur.",
            'week_3': "Trouve l'équilibre entre inspiration et technique.",
            'week_4': "Apprécie le chemin de perfectionnement, pas juste le résultat."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Romance artistique**

Ta Lune en Bélier en Maison 5 veut créer et aimer avec passion. Ton Ascendant Balance ajoute raffinement et sens esthétique : tu veux que tes créations soient belles, tes romances harmonieuses, tes plaisirs élégants.

**Domaine activé** : Maison 5 — Ta créativité et ta vie amoureuse cherchent l'équilibre entre intensité et grâce. Tu veux te laisser aller tout en gardant du style, aimer passionnément tout en restant juste.

**Ton approche instinctive** : La Balance te fait créer avec souci d'harmonie. Tu es sensible à la beauté des formes. Cette élégance peut adoucir ou contraindre ton feu créatif brut.

**Tensions possibles** : Tu risques de trop polir ton expression au détriment de l'authenticité. Le souci de plaire peut filtrer ta créativité spontanée.

**Conseil clé** : Créer et aimer avec ta fougue naturelle tout en cultivant l'élégance.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose de beau qui vient de ton cœur.",
            'week_2': "Exprime tes sentiments amoureux avec grâce et sincérité.",
            'week_3': "Cherche l'équilibre entre spontanéité et raffinement.",
            'week_4': "Célèbre la beauté que tu as créée ou vécue."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Passion transformatrice**

Ta Lune en Bélier en Maison 5 veut créer et aimer avec intensité. Ton Ascendant Scorpion ajoute profondeur et pouvoir : ta créativité touche les zones d'ombre, tes amours sont absolues, tes jeux deviennent rituels.

**Domaine activé** : Maison 5 — Ta créativité et tes romances atteignent des profondeurs extrêmes. Tu ne veux pas juste t'exprimer, tu veux transformer par ton art. Tes amours sont des fusions totales.

**Ton approche instinctive** : Le Scorpion te fait créer depuis tes abysses. Tu explores le tabou, l'intense, le caché. Cette puissance créative peut fasciner ou effrayer.

**Tensions possibles** : L'obsession créative ou amoureuse peut devenir destructrice. Tu risques de te perdre dans l'intensité au détriment de la légèreté nécessaire au jeu.

**Conseil clé** : Plonger dans tes passions créatives tout en gardant un fil vers la surface.""",
        'weekly_advice': {
            'week_1': "Explore un thème créatif profond qui t'habite.",
            'week_2': "Crée ou aime sans retenue, va au bout de l'intensité.",
            'week_3': "Vérifie que ta passion nourrit au lieu d'épuiser.",
            'week_4': "Intègre ce que cette intensité t'a révélé sur toi."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventure créative**

Double feu expansif sur la Maison 5 : ta Lune en Bélier et ton Ascendant Sagittaire créent une énergie créative et ludique débordante. Tu veux explorer, expérimenter, créer en grand, aimer sans frontières.

**Domaine activé** : Maison 5 — Ta créativité et tes loisirs cherchent l'aventure et la découverte. Tu veux que tes plaisirs t'enseignent quelque chose, que tes créations aient du sens et de la portée.

**Ton approche instinctive** : Le Sagittaire te fait créer avec optimisme et vision. Tu vois grand, tu vises haut. Cette confiance créative peut ouvrir des portes extraordinaires.

**Tensions possibles** : L'excès d'ambition peut disperser ton énergie créative. Tu risques de commencer cent projets sans en finir un, ou de promettre plus que tu ne peux donner amoureusement.

**Conseil clé** : Viser l'expansion créative tout en ancrant quelques projets dans le réel.""",
        'weekly_advice': {
            'week_1': "Définis une vision créative inspirante pour ce mois.",
            'week_2': "Expérimente un medium ou un style complètement nouveau.",
            'week_3': "Partage tes créations pour inspirer d'autres.",
            'week_4': "Vérifie que ton enthousiasme s'est traduit en réalisations."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Maîtrise créative**

Ta Lune en Bélier en Maison 5 veut créer avec spontanéité et passion. Ton Ascendant Capricorne apporte discipline et ambition : tu veux que ta créativité serve ton avancement, que tes talents soient reconnus professionnellement.

**Domaine activé** : Maison 5 — Ta créativité devient stratégique. Tu veux exceller dans ton expression, être pris·e au sérieux pour tes talents. Le jeu devient travail, le plaisir devient projet.

**Ton approche instinctive** : Le Capricorne te fait structurer ton expression créative. Tu es prêt·e à travailler dur pour maîtriser ton art. Cette discipline peut sublimer ou étouffer ton feu créatif.

**Tensions possibles** : Le plaisir spontané peut se perdre dans l'ambition. Tu risques de créer par devoir plutôt que par joie, ou de refouler ton besoin de légèreté.

**Conseil clé** : Construire ton excellence créative sans perdre la joie de créer.""",
        'weekly_advice': {
            'week_1': "Définis où tu veux exceller créativement.",
            'week_2': "Pratique avec discipline un talent que tu veux développer.",
            'week_3': "Autorise-toi aussi à jouer sans but productif.",
            'week_4': "Mesure tes progrès tout en célébrant le processus."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Créativité rebelle**

Ta Lune en Bélier en Maison 5 veut s'exprimer avec originalité et courage. Ton Ascendant Verseau amplifie cette différence : tu veux créer quelque chose de jamais vu, aimer de manière non-conventionnelle, jouer selon tes propres règles.

**Domaine activé** : Maison 5 — Ta créativité et tes loisirs cherchent l'innovation et la rupture. Tu refuses les formes d'expression conventionnelles. Ton art devient manifeste, tes amours expérimentales.

**Ton approche instinctive** : Le Verseau te fait expérimenter créativement sans peur du jugement. Tu es avant-gardiste, décalé·e. Cette originalité peut te rendre pionnier·ère ou marginalisé·e.

**Tensions possibles** : Être différent·e juste pour l'être peut limiter ton expression. Tu risques de rejeter ce qui marche simplement parce que c'est populaire.

**Conseil clé** : Innover créativement en restant connecté·e à ton authenticité profonde.""",
        'weekly_advice': {
            'week_1': "Explore une forme d'expression complètement nouvelle pour toi.",
            'week_2': "Crée quelque chose qui bouscule les conventions.",
            'week_3': "Connecte-toi à d'autres créateurs originaux.",
            'week_4': "Vérifie que ton originalité sert vraiment ton expression."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Art mystique**

Ta Lune en Bélier en Maison 5 veut créer avec passion et spontanéité. Ton Ascendant Poissons ajoute dimension spirituelle et intuitive : ta créativité devient channeling, tes amours transcendance, tes jeux rituels sacrés.

**Domaine activé** : Maison 5 — Ta créativité et tes loisirs se connectent à l'invisible. Tu crées depuis ton intuition profonde, tu aimes avec ton âme. L'expression devient méditation ou prière.

**Ton approche instinctive** : Le Poissons te fait créer en état de flow, sans contrôle mental. Tu peux être inspiré·e par des forces que tu ne comprends pas. Cette magie créative produit des œuvres touchantes.

**Tensions possibles** : Le manque de structure peut disperser ton feu créatif. Tu risques de rêver tes créations sans les matérialiser, ou de te perdre dans l'inspiration sans ancrage.

**Conseil clé** : Créer depuis l'inspiration divine tout en donnant forme concrète à tes visions.""",
        'weekly_advice': {
            'week_1': "Médite puis crée ce qui vient spontanément.",
            'week_2': "Donne forme matérielle à une vision ou une émotion.",
            'week_3': "Partage ton art comme offrande, pas comme performance.",
            'week_4': "Remercie la source d'inspiration qui t'habite."
        }
    },

    # ==================== MAISON 6 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Action quotidienne**

Double feu sur la Maison 6 : ta Lune en Bélier et ton Ascendant Bélier veulent révolutionner ton quotidien, ta routine, ta santé. Tu ne supportes pas la monotonie. Chaque jour doit être une nouvelle bataille gagnée.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé, tes habitudes demandent ton énergie guerrière. Tu veux optimiser, améliorer, conquérir ton organisation de vie. L'efficacité devient prioritaire.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu attaques tes tâches avec vigueur. Tu veux tout faire vite et bien. Cette énergie peut être productive ou épuisante selon la gestion.

**Tensions possibles** : L'impatience avec les détails répétitifs peut créer du stress. Tu risques de te surmener ou d'abandonner les routines nécessaires par ennui.

**Conseil clé** : Créer une routine quotidienne dynamique qui nourrit ton besoin d'action.""",
        'weekly_advice': {
            'week_1': "Identifie les aspects de ton quotidien qui te frustrent.",
            'week_2': "Révolutionne une habitude qui ne te sert plus.",
            'week_3': "Intègre de l'activité physique intense dans ta routine.",
            'week_4': "Évalue si ton nouveau rythme est durable."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Routine stable**

Ta Lune en Bélier en Maison 6 veut améliorer rapidement ton quotidien et ta santé. Ton Ascendant Taureau apporte patience et constance : tu veux des habitudes solides, un rythme qui dure, une santé robuste.

**Domaine activé** : Maison 6 — Ton quotidien et tes routines cherchent à la fois efficacité et durabilité. Tu veux que tes habitudes te servent vraiment, que ton travail soit concret et satisfaisant.

**Ton approche instinctive** : Le Taureau te fait construire tes routines progressivement. Tu veux du confort dans ton quotidien, pas juste de la performance. Cette stabilité peut apaiser ton impatience.

**Tensions possibles** : Le besoin de changement rapide se heurte à ton besoin de stabilité. Tu risques d'osciller entre bouleversement et stagnation de tes habitudes.

**Conseil clé** : Améliorer ton quotidien par petits pas constants qui s'ancrent dans la durée.""",
        'weekly_advice': {
            'week_1': "Identifie une habitude saine que tu veux installer.",
            'week_2': "Commence cette habitude doucement mais quotidiennement.",
            'week_3': "Rends ta routine confortable, pas juste efficace.",
            'week_4': "Apprécie la stabilité que tu as créée."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Quotidien varié**

Ta Lune en Bélier en Maison 6 veut un quotidien dynamique et efficace. Ton Ascendant Gémeaux ajoute besoin de variété et stimulation mentale : ta routine doit être flexible, diverse, intellectuellement intéressante.

**Domaine activé** : Maison 6 — Ton quotidien et ton travail cherchent diversité et apprentissage. Tu ne veux pas faire la même chose tous les jours. Tes habitudes doivent nourrir ton cerveau.

**Ton approche instinctive** : Le Gémeaux te fait jongler entre plusieurs tâches et projets. Tu peux être très productif·ve dans la variété. Cette agilité peut être un atout ou une dispersion.

**Tensions possibles** : Trop de changement peut empêcher l'ancrage de bonnes habitudes. Tu risques de papillonner sans vraiment améliorer ton organisation de vie.

**Conseil clé** : Créer une routine flexible qui permet variété dans un cadre stable.""",
        'weekly_advice': {
            'week_1': "Liste toutes les tâches que tu dois gérer.",
            'week_2': "Organise-les de manière à alterner les types d'activités.",
            'week_3': "Apprends quelque chose de nouveau dans ton domaine professionnel.",
            'week_4': "Vérifie que ta diversité sert vraiment ton efficacité."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Service sensible**

Ta Lune en Bélier en Maison 6 veut agir efficacement dans son quotidien. Ton Ascendant Cancer ajoute dimension de soin et d'émotion : ton travail doit nourrir les autres, tes routines te sécuriser émotionnellement.

**Domaine activé** : Maison 6 — Ton quotidien et ta santé sont liés à ton bien-être émotionnel. Tu veux servir, aider, prendre soin, mais tu dois aussi te protéger de l'épuisement.

**Ton approche instinctive** : Le Cancer te fait aborder ton travail comme un soin. Tu peux être dévoué·e jusqu'au sacrifice. Cette sensibilité doit être équilibrée avec des limites claires.

**Tensions possibles** : Tu risques de te surmener en prenant trop soin des autres. L'impulsivité du Bélier peut créer des réactions émotionnelles dans le travail.

**Conseil clé** : Servir avec cœur tout en préservant ton énergie et ta santé.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te donnes trop dans ton quotidien.",
            'week_2': "Pose des limites claires pour te protéger.",
            'week_3': "Crée des routines qui te nourrissent émotionnellement.",
            'week_4': "Vérifie que ton dévouement ne t'épuise pas."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Excellence quotidienne**

Double feu sur la Maison 6 : ta Lune en Bélier et ton Ascendant Lion veulent exceller dans le quotidien et le travail. Tu veux être le·la meilleur·e dans ce que tu fais, que ton organisation de vie soit exemplaire.

**Domaine activé** : Maison 6 — Ton quotidien et ton travail deviennent terrains de performance. Tu veux que tes routines soient efficaces, que ta santé soit optimale, que ton service soit reconnu.

**Ton approche instinctive** : Le Lion te fait aborder tes tâches avec fierté. Tu veux briller même dans les détails. Cette exigence peut élever ton quotidien ou créer de la pression.

**Tensions possibles** : Le besoin de reconnaissance peut te faire négliger l'humilité nécessaire au service. Tu risques de vouloir impressionner plus que d'être vraiment utile.

**Conseil clé** : Exceller dans ton quotidien avec fierté tout en servant avec générosité.""",
        'weekly_advice': {
            'week_1': "Définis un standard d'excellence pour ton travail.",
            'week_2': "Améliore un aspect de ta routine pour l'élever.",
            'week_3': "Partage tes méthodes généreusement avec d'autres.",
            'week_4': "Célèbre tes accomplissements quotidiens."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfectionnement total**

Ta Lune en Bélier en Maison 6 veut optimiser son quotidien rapidement. Ton Ascendant Vierge, maître naturel de cette maison, amplifie ce besoin : chaque détail doit être parfait, chaque routine optimisée au maximum.

**Domaine activé** : Maison 6 — Ton quotidien, ta santé, ton travail deviennent objets d'amélioration constante. Tu veux le système parfait, la routine idéale, la santé optimale. L'excellence est ton standard.

**Ton approche instinctive** : La Vierge te fait analyser chaque aspect de ta vie quotidienne. Tu corriges, tu ajustes, tu perfectionnes sans cesse. Cette rigueur peut être productive ou paralysante.

**Tensions possibles** : Le perfectionnisme peut devenir anxiété. Tu risques de ne jamais être satisfait·e de ton organisation, de ta santé, de ton travail.

**Conseil clé** : Viser l'excellence tout en acceptant l'imperfection humaine inévitable.""",
        'weekly_advice': {
            'week_1': "Audite complètement ton quotidien et ta santé.",
            'week_2': "Optimise méthodiquement un domaine à la fois.",
            'week_3': "Accepte qu'il y aura toujours des imperfections.",
            'week_4': "Apprécie le chemin de perfectionnement plus que la destination."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre quotidien**

Ta Lune en Bélier en Maison 6 veut agir efficacement dans son quotidien. Ton Ascendant Balance cherche l'équilibre et l'harmonie : ta routine doit être à la fois productive et agréable, ton travail juste et équilibré.

**Domaine activé** : Maison 6 — Ton quotidien et ta santé cherchent l'équilibre entre action et repos, effort et plaisir. Tu veux une vie qui fonctionne bien sans te consumer.

**Ton approche instinctive** : La Balance te fait chercher la juste mesure dans tout. Tu veux collaborer dans ton travail, créer de la beauté dans ton quotidien. Cette recherche d'harmonie peut apaiser ta fougue.

**Tensions possibles** : Tu risques de trop négocier avec tes propres besoins. L'impulsivité du Bélier peut rompre l'équilibre que tu tentes de créer.

**Conseil clé** : Créer un quotidien équilibré qui respecte à la fois l'action et le repos.""",
        'weekly_advice': {
            'week_1': "Identifie les déséquilibres dans ton quotidien.",
            'week_2': "Ajuste une routine pour créer plus d'harmonie.",
            'week_3': "Embellis ton espace de travail pour plus de plaisir.",
            'week_4': "Vérifie que ton équilibre te respecte vraiment."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Transformation quotidienne**

Ta Lune en Bélier en Maison 6 veut améliorer son quotidien avec détermination. Ton Ascendant Scorpion ajoute intensité et profondeur : tu veux transformer radicalement tes habitudes, purifier ta santé, éliminer ce qui ne sert plus.

**Domaine activé** : Maison 6 — Ton quotidien et ta santé passent par une crise de transformation. Tu veux détruire tes mauvaises habitudes, régénérer ton corps, reconstruire ton organisation de vie.

**Ton approche instinctive** : Le Scorpion te fait aborder santé et routine avec intensité. Tu peux être obsessionnel·le sur ton optimisation. Cette profondeur peut guérir ou épuiser.

**Tensions possibles** : L'extrémisme peut nuire à ta santé. Tu risques d'alterner entre discipline intense et abandon total, sans trouver le juste milieu.

**Conseil clé** : Transformer tes habitudes en profondeur sans tomber dans l'obsession.""",
        'weekly_advice': {
            'week_1': "Identifie une habitude toxique à éliminer complètement.",
            'week_2': "Purifie ton quotidien, tes espaces, ta santé.",
            'week_3': "Instaure une pratique de régénération profonde.",
            'week_4': "Observe comment tu as transformé ton quotidien."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Routine aventureuse**

Double feu sur la Maison 6 : ta Lune en Bélier et ton Ascendant Sagittaire veulent un quotidien qui a du sens, qui enseigne, qui élargit. Ta routine doit servir ta quête, ton travail doit avoir une portée.

**Domaine activé** : Maison 6 — Ton quotidien et ton travail cherchent sens et expansion. Tu ne veux pas juste faire des tâches, tu veux que chaque action serve une vision plus grande.

**Ton approche instinctive** : Le Sagittaire te fait voir ton quotidien comme une aventure. Tu peux rendre enthousiasmantes même les tâches répétitives en leur donnant du sens. Cette perspective inspire.

**Tensions possibles** : Le besoin de sens peut te faire négliger les détails pratiques. Tu risques de vouloir toujours plus, jamais satisfait·e de ton quotidien actuel.

**Conseil clé** : Donner du sens à ton quotidien tout en honorant les tâches simples.""",
        'weekly_advice': {
            'week_1': "Définis la vision qui donne sens à ton travail quotidien.",
            'week_2': "Trouve comment chaque tâche sert cette vision.",
            'week_3': "Apprends quelque chose qui élève ta pratique professionnelle.",
            'week_4': "Célèbre le sens que tu as insufflé dans ton quotidien."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Discipline productive**

Ta Lune en Bélier en Maison 6 veut optimiser son quotidien avec énergie. Ton Ascendant Capricorne apporte structure et ambition : tu veux que tes routines servent tes objectifs à long terme, que ton travail construise ton futur.

**Domaine activé** : Maison 6 — Ton quotidien devient stratégique. Chaque habitude doit servir ton ascension, chaque tâche contribuer à ton ambition. La discipline rencontre l'action.

**Ton approche instinctive** : Le Capricorne te fait structurer ton quotidien avec rigueur. Tu es prêt·e à faire des efforts maintenant pour récolter plus tard. Cette patience stratégique canalise bien ton feu.

**Tensions possibles** : Tu risques de te surcharger de travail en négligeant ta santé. L'impatience du Bélier peut se heurter à la lenteur de la construction.

**Conseil clé** : Construire une routine disciplinée qui sert tes ambitions sans te consumer.""",
        'weekly_advice': {
            'week_1': "Définis comment ton quotidien doit servir tes objectifs à 5 ans.",
            'week_2': "Structure tes journées pour maximiser ton avancement.",
            'week_3': "Maintiens ta discipline même quand c'est difficile.",
            'week_4': "Mesure objectivement tes progrès dans l'organisation."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Quotidien innovant**

Ta Lune en Bélier en Maison 6 veut améliorer son quotidien rapidement. Ton Ascendant Verseau ajoute innovation et originalité : tu veux révolutionner ta manière de travailler, inventer de nouvelles routines, hacker ta productivité.

**Domaine activé** : Maison 6 — Ton quotidien et ton travail cherchent l'innovation. Tu expérimentes avec des outils, des méthodes, des organisations alternatives. Tu refuses les routines conventionnelles.

**Ton approche instinctive** : Le Verseau te fait tester constamment de nouvelles approches. Tu es ouvert·e aux technologies et méthodes avant-gardistes. Cette créativité peut révolutionner ton efficacité.

**Tensions possibles** : Trop d'expérimentation peut créer de l'instabilité. Tu risques de changer constamment de système sans laisser le temps aux habitudes de s'ancrer.

**Conseil clé** : Innover dans ton organisation tout en gardant une base stable.""",
        'weekly_advice': {
            'week_1': "Explore de nouvelles méthodes de productivité.",
            'week_2': "Teste un outil ou une routine complètement nouvelle.",
            'week_3': "Garde ce qui fonctionne vraiment, abandonne le reste.",
            'week_4': "Évalue si tes innovations servent vraiment ton efficacité."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Service intuitif**

Ta Lune en Bélier en Maison 6 veut agir efficacement dans son quotidien. Ton Ascendant Poissons ajoute dimension spirituelle et fluide : ton travail devient service sacré, tes routines doivent honorer ton intuition et ton besoin de flow.

**Domaine activé** : Maison 6 — Ton quotidien et ta santé cherchent à la fois structure et fluidité. Tu veux servir avec ton cœur, travailler en étant connecté·e à quelque chose de plus grand.

**Ton approche instinctive** : Le Poissons te fait aborder ton travail avec compassion et adaptation. Tu peux manquer de limites, te dissoudre dans le service. Cette sensibilité doit être protégée.

**Tensions possibles** : Le manque de structure peut nuire à ton efficacité. Tu risques de te laisser submerger par les besoins des autres ou de fuir les tâches concrètes.

**Conseil clé** : Servir avec cœur tout en maintenant des limites et une structure minimale.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton travail peut être un service spirituel.",
            'week_2': "Crée des routines qui honorent ton intuition et ton flow.",
            'week_3': "Protège ton énergie avec des limites claires.",
            'week_4': "Vérifie que ton service ne t'épuise pas."
        }
    },

    # ==================== MAISON 7 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Partenariat conquérant**

Double feu sur la Maison 7 : ta Lune en Bélier et ton Ascendant Bélier activent intensément tes relations et partenariats, mais de manière combative. Tu veux des relations d'égal à égal, des défis stimulants, pas de la mièvrerie.

**Domaine activé** : Maison 7 — Tes relations de couple, tes partenariats, tes collaborations demandent authenticité et courage. Tu veux te confronter à l'autre, pas fusionner. Le conflit peut être une forme d'intimité.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu abordes les relations directement, sans détour. Tu dis ce que tu penses, tu prends des initiatives. Cette franchise peut rafraîchir ou brusquer.

**Tensions possibles** : Trop de combativité peut détruire l'harmonie nécessaire au partenariat. Tu risques de vouloir avoir raison au lieu de vouloir être en lien.

**Conseil clé** : Chercher des partenaires à ta hauteur tout en cultivant la coopération.""",
        'weekly_advice': {
            'week_1': "Clarifie ce que tu attends vraiment d'un partenariat.",
            'week_2': "Adresse un désaccord de manière directe mais constructive.",
            'week_3': "Cherche la complémentarité, pas juste la rivalité.",
            'week_4': "Célèbre la force que crée ton authenticité relationnelle."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Engagement stable**

Ta Lune en Bélier en Maison 7 veut des relations passionnées et authentiques. Ton Ascendant Taureau apporte loyauté et constance : tu veux un partenariat durable, ancré, où la passion se transforme en engagement solide.

**Domaine activé** : Maison 7 — Tes relations cherchent à la fois intensité et stabilité. Tu veux quelqu'un avec qui construire sur la durée, mais tu as besoin que ça reste vivant, pas routinier.

**Ton approche instinctive** : Le Taureau te fait investir lentement mais profondément dans tes relations. Une fois engagé·e, tu es loyal·e. Cette fidélité peut rassurer ou étouffer selon le partenaire.

**Tensions possibles** : L'impulsivité relationnelle du Bélier se heurte à ton besoin de sécurité. Tu peux osciller entre coup de foudre et prudence excessive.

**Conseil clé** : Construire des partenariats solides tout en gardant la flamme vivante.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui crée vraiment de la stabilité relationnelle pour toi.",
            'week_2': "Investis concrètement dans une relation importante.",
            'week_3': "Renouvelle la passion sans abandonner la sécurité.",
            'week_4': "Apprécie la solidité de l'engagement que tu as créé."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Partenariat stimulant**

Ta Lune en Bélier en Maison 7 veut des relations authentiques et directes. Ton Ascendant Gémeaux ajoute besoin de communication et de variété : tu veux un partenaire qui te stimule intellectuellement, avec qui tu peux échanger infiniment.

**Domaine activé** : Maison 7 — Tes relations et partenariats passent par la communication. Tu veux quelqu'un avec qui parler de tout, qui te challenge mentalement, qui reste intéressant.

**Ton approche instinctive** : Le Gémeaux te fait aborder les relations avec curiosité et légèreté. Tu peux avoir du mal à t'engager profondément, préférant la stimulation à l'intimité.

**Tensions possibles** : La peur de l'ennui peut t'empêcher d'approfondir. Tu risques de papillonner relationnellement sans créer de vraie connexion durable.

**Conseil clé** : Chercher la stimulation intellectuelle tout en acceptant l'approfondissement émotionnel.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te stimule vraiment dans une relation.",
            'week_2': "Aie des conversations profondes avec ton·ta partenaire.",
            'week_3': "Explore de nouvelles activités ensemble.",
            'week_4': "Vérifie que tu n'es pas juste en surface."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Intimité courageuse**

Ta Lune en Bélier en Maison 7 veut des relations authentiques et passionnées. Ton Ascendant Cancer ajoute profondeur émotionnelle et besoin de sécurité : tu veux un partenariat où tu peux être vulnérable en toute sécurité.

**Domaine activé** : Maison 7 — Tes relations cherchent à la fois passion et protection. Tu veux quelqu'un qui te voit vraiment, qui accueille tes émotions, qui crée un nid relationnel sécurisant.

**Ton approche instinctive** : Le Cancer te fait aborder les partenariats avec sensibilité. Tu donnes tout ton cœur une fois en confiance. Cette intensité émotionnelle peut créer une intimité profonde.

**Tensions possibles** : Tu risques d'être blessé·e par ta propre impulsivité émotionnelle. La peur de la vulnérabilité peut te faire alterner entre fusion et retrait.

**Conseil clé** : Oser l'intimité émotionnelle tout en gardant ton autonomie.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te fait te sentir en sécurité relationnellement.",
            'week_2': "Partage quelque chose de vulnérable avec ton·ta partenaire.",
            'week_3': "Crée des rituels d'intimité qui vous nourrissent.",
            'week_4': "Célèbre le courage d'avoir été vraiment toi-même."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Romance royale**

Double feu sur la Maison 7 : ta Lune en Bélier et ton Ascendant Lion créent des attentes élevées en amour et partenariat. Tu veux une relation digne d'un conte, où vous vous admirez mutuellement, où la passion ne faiblit jamais.

**Domaine activé** : Maison 7 — Tes relations et partenariats cherchent grandeur et générosité. Tu veux un·e partenaire qui brille autant que toi, avec qui créer quelque chose de magnifique ensemble.

**Ton approche instinctive** : Le Lion te fait aborder les relations avec fierté et générosité. Tu donnes largement, tu célèbres ton·ta partenaire. Cette chaleur peut être merveilleuse si réciproque.

**Tensions possibles** : Le besoin d'admiration peut créer une compétition au lieu d'une collaboration. Tu risques de vouloir briller plus que l'autre au lieu de briller ensemble.

**Conseil clé** : Créer un partenariat où vous vous élevez mutuellement sans rivalité.""",
        'weekly_advice': {
            'week_1': "Définis ce qu'un partenariat royal signifie pour toi.",
            'week_2': "Célèbre publiquement ton·ta partenaire.",
            'week_3': "Assure-toi que la réciprocité est présente.",
            'week_4': "Vérifie que votre relation nourrit deux royautés, pas une."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Partenariat perfectible**

Ta Lune en Bélier en Maison 7 veut des relations authentiques et passionnées. Ton Ascendant Vierge apporte analyse et perfectionnisme : tu veux améliorer ton partenariat, comprendre ce qui fonctionne et ce qui coince.

**Domaine activé** : Maison 7 — Tes relations deviennent objet d'attention et d'amélioration. Tu veux optimiser la communication, la collaboration, rendre le partenariat plus efficace et sain.

**Ton approche instinctive** : La Vierge te fait observer et analyser tes relations. Tu peux être critique de ton·ta partenaire ou de toi-même. Cette lucidité peut être constructive ou destructrice.

**Tensions possibles** : Le perfectionnisme peut empêcher l'acceptation. Tu risques de toujours voir ce qui ne va pas au lieu de ce qui va bien dans la relation.

**Conseil clé** : Améliorer ton partenariat tout en acceptant l'imperfection de l'amour humain.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect de ta relation à améliorer concrètement.",
            'week_2': "Communique tes besoins clairement et constructivement.",
            'week_3': "Accepte aussi ce qui est déjà bien dans la relation.",
            'week_4': "Vérifie que ton exigence ne détruit pas la légèreté nécessaire."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre passionné**

Ta Lune en Bélier en Maison 7 veut des relations authentiques et intenses. Ton Ascendant Balance, maître naturel de cette maison, amplifie le besoin de partenariat : tu te trouves dans la relation, tu existes pleinement dans le miroir de l'autre.

**Domaine activé** : Maison 7 — Tes relations sont au cœur de tout. Tu cherches l'équilibre parfait entre autonomie et union, passion et harmonie, confrontation et paix. Le partenariat est ton terrain d'évolution.

**Ton approche instinctive** : La Balance te fait chercher constamment l'équilibre relationnel. Tu veux l'harmonie mais le Bélier te pousse à l'authenticité brute. Cette tension crée une danse complexe.

**Tensions possibles** : Tu risques de te perdre dans la relation ou au contraire d'imposer trop ta volonté. Trouver le juste équilibre entre soi et l'autre est ton défi constant.

**Conseil clé** : Être pleinement toi-même tout en créant une vraie union avec l'autre.""",
        'weekly_advice': {
            'week_1': "Clarifie où se trouve l'équilibre entre tes besoins et ceux de l'autre.",
            'week_2': "Exprime tes désirs sans sacrifier l'harmonie.",
            'week_3': "Négocie un compromis qui te respecte vraiment.",
            'week_4': "Célèbre l'équilibre unique que vous avez créé."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Fusion intense**

Ta Lune en Bélier en Maison 7 veut des relations passionnées et authentiques. Ton Ascendant Scorpion amplifie cette intensité : tu veux une fusion totale, une intimité absolue, un partenariat qui transforme. Rien de superficiel.

**Domaine activé** : Maison 7 — Tes relations deviennent terrain de transformation profonde. Tu veux tout partager, tout vivre ensemble, mourir et renaître à travers le partenariat. L'intensité est maximale.

**Ton approche instinctive** : Le Scorpion te fait vivre tes relations avec une profondeur extrême. Tu donnes tout ou rien. Cette passion peut créer des liens puissants ou des dynamiques toxiques.

**Tensions possibles** : L'obsession relationnelle peut devenir étouffante. Tu risques de vouloir contrôler ton·ta partenaire ou de te perdre complètement dans la fusion.

**Conseil clé** : Vivre l'intensité relationnelle tout en préservant deux individualités distinctes.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu cherches vraiment dans l'intimité profonde.",
            'week_2': "Partage une vérité difficile avec ton·ta partenaire.",
            'week_3': "Traverse ensemble une transformation, un défi.",
            'week_4': "Vérifie que votre intensité reste saine et respectueuse."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Partenariat libre**

Double feu expansif sur la Maison 7 : ta Lune en Bélier et ton Ascendant Sagittaire veulent un partenariat qui libère au lieu d'enfermer. Tu cherches quelqu'un avec qui explorer le monde, grandir, découvrir ensemble.

**Domaine activé** : Maison 7 — Tes relations cherchent liberté et croissance. Tu veux un·e partenaire qui soit aussi ton·ta compagnon·compagne d'aventure, avec qui partager une quête, pas juste une routine.

**Ton approche instinctive** : Le Sagittaire te fait aborder les partenariats avec optimisme et confiance. Tu donnes beaucoup d'espace, tu fais confiance. Cette liberté peut créer des liens profonds ou de la distance.

**Tensions possibles** : La peur de l'enfermement peut t'empêcher de vraiment t'engager. Tu risques de fuir l'intimité au nom de la liberté.

**Conseil clé** : Créer un partenariat libre qui permet à la fois aventure et engagement.""",
        'weekly_advice': {
            'week_1': "Définis ce que liberté et engagement signifient pour toi ensemble.",
            'week_2': "Planifiez une aventure commune qui vous inspire.",
            'week_3': "Partagez vos visions, vos philosophies de vie.",
            'week_4': "Célèbre comment votre relation vous fait grandir."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Alliance stratégique**

Ta Lune en Bélier en Maison 7 veut des relations authentiques et passionnées. Ton Ascendant Capricorne ajoute dimension de construction et d'ambition : tu veux un partenariat qui dure, qui construit, qui sert vos objectifs mutuels.

**Domaine activé** : Maison 7 — Tes relations deviennent stratégiques. Tu cherches quelqu'un avec qui bâtir un projet de vie solide, qui partage ton ambition, avec qui créer un empire personnel ou professionnel.

**Ton approche instinctive** : Le Capricorne te fait aborder les partenariats avec sérieux et engagement. Tu choisis soigneusement, tu investis sur la durée. Cette maturité peut créer des unions solides.

**Tensions possibles** : L'impulsivité du Bélier se heurte à ta prudence relationnelle. Tu peux osciller entre coup de foudre et calcul froid.

**Conseil clé** : Construire un partenariat solide tout en gardant la passion vivante.""",
        'weekly_advice': {
            'week_1': "Définis ce qu'un partenariat durable signifie pour toi.",
            'week_2': "Investis concrètement dans un projet commun.",
            'week_3': "Équilibre responsabilité et romance.",
            'week_4': "Mesure les fondations que vous avez construites ensemble."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Partenariat unique**

Ta Lune en Bélier en Maison 7 veut des relations authentiques et directes. Ton Ascendant Verseau ajoute besoin d'originalité et de liberté : tu veux un partenariat qui sort des conventions, qui respecte l'individualité de chacun·e.

**Domaine activé** : Maison 7 — Tes relations cherchent à réinventer le couple ou le partenariat. Tu refuses les modèles traditionnels. Tu veux créer quelque chose d'unique qui vous ressemble vraiment.

**Ton approche instinctive** : Le Verseau te fait aborder les partenariats avec détachement et amitié. Tu veux un·e partenaire qui soit d'abord ton·ta meilleur·e ami·e, avec qui partager des idéaux.

**Tensions possibles** : Le détachement peut empêcher la vraie intimité. Tu risques d'intellectualiser la relation au détriment de l'émotion.

**Conseil clé** : Créer un partenariat original tout en honorant les besoins émotionnels de base.""",
        'weekly_advice': {
            'week_1': "Définis le type de relation non-conventionnelle que tu veux.",
            'week_2': "Communique clairement vos règles et frontières uniques.",
            'week_3': "Autorise aussi la vulnérabilité émotionnelle.",
            'week_4': "Célèbre l'originalité de votre union."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Fusion mystique**

Ta Lune en Bélier en Maison 7 veut des relations authentiques et passionnées. Ton Ascendant Poissons ajoute dimension spirituelle et fusionnelle : tu cherches une âme sœur, une union qui transcende l'ego, un amour qui touche le divin.

**Domaine activé** : Maison 7 — Tes relations cherchent la fusion d'âmes. Tu veux te dissoudre dans l'autre, ressentir l'unité absolue. Cette quête romantique peut créer de la magie ou de la confusion.

**Ton approche instinctive** : Le Poissons te fait aborder les partenariats avec idéalisme et empathie. Tu ressens tout, tu t'adaptes complètement. Cette sensibilité peut être une force ou te faire perdre tes limites.

**Tensions possibles** : L'impulsivité du Bélier se dilue dans les brumes du Poissons. Tu risques de perdre ton identité dans la relation ou de projeter un idéal impossible.

**Conseil clé** : Vivre la connexion spirituelle tout en gardant deux âmes distinctes.""",
        'weekly_advice': {
            'week_1': "Médite sur ce que l'union sacrée signifie pour toi.",
            'week_2': "Crée des moments de connexion spirituelle avec ton·ta partenaire.",
            'week_3': "Maintiens tes limites même dans la fusion.",
            'week_4': "Vérifie que ton idéal relationnel honore la réalité."
        }
    },

    # ==================== MAISON 8 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Transformation guerrière**

Double feu sur la Maison 8 : ta Lune en Bélier et ton Ascendant Bélier plongent dans les profondeurs avec fougue. Tu veux affronter tes peurs, tes crises, tes transformations de front. La mort et la renaissance deviennent terrain de conquête.

**Domaine activé** : Maison 8 — Les crises, les transformations, l'intimité profonde, les ressources partagées demandent ton courage. Tu es prêt·e à détruire l'ancien pour faire place au nouveau, à combattre tes démons.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu ne recules pas devant l'intensité. Tu plonges dans ce qui fait peur aux autres. Cette bravoure peut libérer ou te brûler.

**Tensions possibles** : L'impulsivité dans les zones d'ombre peut être dangereuse. Tu risques de forcer des transformations qui demandent du temps, de brusquer l'intimité profonde.

**Conseil clé** : Affronter courageusement tes zones d'ombre tout en respectant leur profondeur.""",
        'weekly_advice': {
            'week_1': "Identifie une peur ou une zone d'ombre à affronter.",
            'week_2': "Plonge dedans avec courage mais aussi respect.",
            'week_3': "Traverse la crise sans fuir ni forcer.",
            'week_4': "Célèbre la transformation que tu as osé vivre."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Régénération ancrée**

Ta Lune en Bélier en Maison 8 veut transformer rapidement et intensément. Ton Ascendant Taureau apporte ancrage et patience : tu veux que tes transformations soient profondes et durables, pas juste des révolutions superficielles.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées cherchent à la fois intensité et stabilité. Tu veux mourir et renaître solidement, pas dans le chaos.

**Ton approche instinctive** : Le Taureau te fait aborder les crises avec une forme de stabilité. Tu traverses lentement mais sûrement. Cette patience peut être frustrante mais salvatrice.

**Tensions possibles** : L'urgence de transformation se heurte à ton besoin de sécurité. Tu peux résister au changement nécessaire par peur de perdre tes repères.

**Conseil clé** : Accepter les transformations profondes tout en construisant de nouvelles bases solides.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit mourir pour que tu puisses renaître.",
            'week_2': "Lâche progressivement, sans tout détruire d'un coup.",
            'week_3': "Construis déjà les nouvelles fondations pendant la transition.",
            'week_4': "Ancre-toi dans la stabilité de ton nouveau soi."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Transformation mentale**

Ta Lune en Bélier en Maison 8 veut vivre des transformations intenses. Ton Ascendant Gémeaux ajoute dimension intellectuelle : tu veux comprendre tes crises, parler de tes zones d'ombre, explorer la psychologie des profondeurs.

**Domaine activé** : Maison 8 — Tes transformations et ton intimité passent par la compréhension et la communication. Tu veux nommer tes démons, analyser tes peurs, partager tes secrets.

**Ton approche instinctive** : Le Gémeaux te fait aborder les profondeurs avec légèreté et curiosité. Tu peux intellectualiser l'émotion, ce qui peut être une défense ou un outil de compréhension.

**Tensions possibles** : Tu risques de rester en surface par peur de vraiment ressentir. L'analyse peut devenir une fuite de l'expérience réelle de transformation.

**Conseil clé** : Comprendre tes transformations tout en les vivant émotionnellement, pas juste mentalement.""",
        'weekly_advice': {
            'week_1': "Lis ou écoute quelque chose sur les transformations psychologiques.",
            'week_2': "Parle de tes peurs ou zones d'ombre avec quelqu'un.",
            'week_3': "Permets-toi aussi de ressentir sans analyser.",
            'week_4': "Intègre ce que tu as compris de ton processus."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Guérison profonde**

Ta Lune en Bélier en Maison 8 veut affronter courageusement ses blessures. Ton Ascendant Cancer ajoute dimension émotionnelle et sensibilité : tes transformations touchent les blessures les plus anciennes, celles de l'enfance et de la famille.

**Domaine activé** : Maison 8 — Tes crises et transformations sont profondément émotionnelles. Tu peux revisiter des douleurs anciennes pour enfin les guérir. L'intimité devient terrain de régénération.

**Ton approche instinctive** : Le Cancer te fait vivre tes transformations dans ton corps émotionnel. Tu ressens tout intensément. Cette sensibilité peut faciliter la guérison si tu ne te noies pas dedans.

**Tensions possibles** : L'impulsivité du Bélier peut rouvrir des blessures brutalement. Tu risques de te laisser submerger par les émotions profondes sans protection.

**Conseil clé** : Guérir courageusement tes blessures tout en te protégeant de la submersion.""",
        'weekly_advice': {
            'week_1': "Identifie une blessure ancienne prête à être guérie.",
            'week_2': "Crée un espace sécurisant pour explorer cette douleur.",
            'week_3': "Traverse l'émotion avec courage et douceur.",
            'week_4': "Remercie-toi pour le courage de guérir."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Renaissance rayonnante**

Double feu sur la Maison 8 : ta Lune en Bélier et ton Ascendant Lion créent une capacité puissante de régénération. Tu traverses les crises avec courage et tu en ressors plus fort·e, plus rayonnant·e. La transformation te sublime.

**Domaine activé** : Maison 8 — Tes transformations et ton intimité cherchent à révéler ta puissance authentique. Tu veux brûler ce qui est faux pour révéler l'or de ton essence. C'est une alchimie du cœur.

**Ton approche instinctive** : Le Lion te fait vivre tes transformations avec dignité et force. Tu ne te laisses pas abattre par les crises. Cette résilience inspire les autres.

**Tensions possibles** : L'orgueil peut t'empêcher de montrer ta vulnérabilité. Tu risques de cacher tes difficultés pour maintenir ton image de force.

**Conseil clé** : Vivre tes transformations avec courage tout en acceptant d'être vulnérable.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui demande à mourir pour que tu brilles vraiment.",
            'week_2': "Traverse la crise avec la tête haute.",
            'week_3': "Partage généreusement ce que tu apprends de ta transformation.",
            'week_4': "Célèbre qui tu deviens à travers les épreuves."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Purification méthodique**

Ta Lune en Bélier en Maison 8 veut transformer rapidement et radicalement. Ton Ascendant Vierge apporte méthode et discernement : tu veux purifier tes profondeurs avec précision, éliminer ce qui toxique de manière chirurgicale.

**Domaine activé** : Maison 8 — Tes transformations et ton intimité passent par l'analyse et la purification. Tu veux comprendre les mécanismes de tes blessures, nettoyer tes zones d'ombre méthodiquement.

**Ton approche instinctive** : La Vierge te fait aborder les crises avec pragmatisme. Tu cherches des solutions concrètes, des protocoles de guérison. Cette approche peut être efficace ou désincarnée.

**Tensions possibles** : Le perfectionnisme peut devenir obsession. Tu risques de vouloir contrôler des processus qui demandent aussi du lâcher-prise.

**Conseil clé** : Purifier tes profondeurs avec méthode tout en acceptant le mystère de la transformation.""",
        'weekly_advice': {
            'week_1': "Analyse ce qui dans ta psyché demande à être nettoyé.",
            'week_2': "Mets en place un protocole de guérison concret.",
            'week_3': "Applique-le avec discipline mais sans rigidité.",
            'week_4': "Évalue objectivement ta progression dans la guérison."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Transformation relationnelle**

Ta Lune en Bélier en Maison 8 veut vivre l'intensité et la transformation. Ton Ascendant Balance ajoute dimension relationnelle : tes crises se vivent souvent à travers les autres, tes transformations passent par l'intimité partagée.

**Domaine activé** : Maison 8 — Tes transformations et ton intimité sont liées à tes partenariats. Tu traverses des crises relationnelles profondes qui te forcent à évoluer, à mourir à d'anciennes versions de toi.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre même dans les profondeurs. Tu veux que tes transformations soient justes, que l'intimité soit équitable. Ce souci de fairness peut adoucir l'intensité.

**Tensions possibles** : Tu risques de perdre ton centre dans la dynamique relationnelle. L'impulsivité du Bélier peut créer des ruptures brutales suivies de tentatives de réparation.

**Conseil clé** : Vivre les transformations relationnelles tout en gardant ton intégrité personnelle.""",
        'weekly_advice': {
            'week_1': "Identifie comment tes relations te forcent à évoluer.",
            'week_2': "Traverse une crise relationnelle avec authenticité et équité.",
            'week_3': "Maintiens ton équilibre intérieur dans l'intensité.",
            'week_4': "Célèbre comment la relation t'a transformé·e."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Alchimie totale**

Ta Lune en Bélier en Maison 8 veut transformer avec courage. Ton Ascendant Scorpion, maître naturel de cette maison, amplifie cette puissance : tu es un·e alchimiste de l'âme, capable de transmuter le plomb en or, la mort en vie.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes crises sont à leur maximum d'intensité. Tu vis des morts et renaissances profondes. Rien n'est superficiel ce mois-ci.

**Ton approche instinctive** : Le Scorpion te fait plonger sans peur dans les abysses. Tu vas au bout des choses, tu ne laisses rien dans l'ombre. Cette radicalité peut guérir ou détruire.

**Tensions possibles** : L'obsession des profondeurs peut devenir destructrice. Tu risques de te perdre dans les ténèbres ou de devenir trop intense pour les autres.

**Conseil clé** : Plonger dans les profondeurs tout en gardant un fil vers la lumière.""",
        'weekly_advice': {
            'week_1': "Identifie la transformation la plus radicale que tu dois vivre.",
            'week_2': "Plonge totalement, va au bout du processus.",
            'week_3': "Accueille ce qui meurt et ce qui naît en toi.",
            'week_4': "Intègre la puissance que cette alchimie t'a révélée."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Transformation libératrice**

Double feu sur la Maison 8 : ta Lune en Bélier et ton Ascendant Sagittaire vivent les crises comme des opportunités d'expansion. Tu veux que tes transformations t'ouvrent de nouveaux horizons, te libèrent de l'ancien.

**Domaine activé** : Maison 8 — Tes transformations et ton intimité cherchent sens et liberté. Tu veux comprendre la philosophie de tes crises, voir ce qu'elles t'enseignent, en sortir plus libre et plus sage.

**Ton approche instinctive** : Le Sagittaire te fait aborder même les profondeurs avec optimisme. Tu crois en ta capacité à renaître. Cette foi peut être une force immense ou un déni de la douleur.

**Tensions possibles** : Tu risques de fuir la vraie profondeur par l'excès de positivité. L'impulsivité peut te faire sauter d'une crise à l'autre sans vraiment guérir.

**Conseil clé** : Vivre tes transformations avec foi tout en honorant la profondeur de la douleur.""",
        'weekly_advice': {
            'week_1': "Identifie le sens que tu cherches dans ta crise actuelle.",
            'week_2': "Traverse l'épreuve en gardant une vision positive.",
            'week_3': "Autorise-toi aussi la douleur sans tout spiritualiser.",
            'week_4': "Célèbre la sagesse gagnée à travers l'épreuve."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Transformation structurée**

Ta Lune en Bélier en Maison 8 veut vivre des transformations intenses et rapides. Ton Ascendant Capricorne apporte structure et maîtrise : tu veux traverser tes crises avec dignité, reconstruire méthodiquement après chaque mort symbolique.

**Domaine activé** : Maison 8 — Tes transformations et ton intimité deviennent des projets à long terme. Tu veux gérer tes crises, contrôler ton processus de renaissance, construire une nouvelle vie solide.

**Ton approche instinctive** : Le Capricorne te fait aborder les profondeurs avec sérieux et responsabilité. Tu ne te laisses pas submerger. Cette maîtrise peut être une force ou une armure trop rigide.

**Tensions possibles** : Le besoin de contrôle peut bloquer le flow nécessaire à la transformation. Tu risques de résister au changement ou de te durcir pour ne pas sentir la douleur.

**Conseil clé** : Gérer tes transformations avec maturité tout en acceptant de perdre le contrôle.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu peux structurer ta transformation actuelle.",
            'week_2': "Crée un plan de reconstruction post-crise.",
            'week_3': "Autorise-toi aussi à ne pas tout contrôler.",
            'week_4': "Mesure les nouvelles fondations que tu as posées."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolution intérieure**

Ta Lune en Bélier en Maison 8 veut transformer avec courage. Ton Ascendant Verseau ajoute dimension de révolution et de libération : tu veux casser les chaînes intérieures, te libérer des conditionnements, renaître totalement différent·e.

**Domaine activé** : Maison 8 — Tes transformations et ton intimité passent par la rupture avec l'ancien. Tu veux une renaissance radicale, devenir quelqu'un de complètement nouveau, libre de toute attache passée.

**Ton approche instinctive** : Le Verseau te fait aborder tes crises avec détachement et originalité. Tu peux intellectualiser la transformation, ce qui peut être libérateur ou une fuite émotionnelle.

**Tensions possibles** : Le détachement peut t'empêcher de vraiment guérir émotionnellement. Tu risques de révolutionner en surface sans transformer en profondeur.

**Conseil clé** : Te libérer radicalement tout en traversant vraiment le processus émotionnel.""",
        'weekly_advice': {
            'week_1': "Identifie les chaînes intérieures dont tu veux te libérer.",
            'week_2': "Romps consciemment avec un conditionnement ancien.",
            'week_3': "Permets-toi de ressentir émotionnellement cette libération.",
            'week_4': "Célèbre ta renaissance dans une nouvelle liberté."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 8, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution sacrée**

Ta Lune en Bélier en Maison 8 veut transformer avec courage. Ton Ascendant Poissons ajoute dimension spirituelle et mystique : tes transformations deviennent des expériences de dissolution de l'ego, de fusion avec le Tout.

**Domaine activé** : Maison 8 — Tes transformations et ton intimité touchent le sacré. Tu vis des petites morts de l'ego, des dissolutions dans l'amour ou la spiritualité. C'est une alchimie mystique.

**Ton approche instinctive** : Le Poissons te fait vivre tes crises comme des initiations spirituelles. Tu lâches prise, tu fais confiance au processus. Cette foi peut faciliter ou compliquer la transformation.

**Tensions possibles** : L'impulsivité du Bélier se dissout dans les brumes du Poissons. Tu risques de perdre tes limites ou de fuir dans la spiritualité sans vraiment guérir.

**Conseil clé** : Vivre tes transformations comme des initiations tout en gardant les pieds sur terre.""",
        'weekly_advice': {
            'week_1': "Médite sur le sens spirituel de ta crise actuelle.",
            'week_2': "Lâche prise sur ce qui doit partir, fais confiance.",
            'week_3': "Maintiens quand même tes limites et ta structure.",
            'week_4': "Intègre les insights spirituels dans ta vie concrète."
        }
    },

    # ==================== MAISON 9 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Conquête philosophique**

Double feu sur la Maison 9 : ta Lune en Bélier et ton Ascendant Bélier te poussent à explorer, à conquérir de nouveaux horizons mentaux et géographiques. Tu veux voyager, apprendre, découvrir des philosophies qui élargissent ta vision.

**Domaine activé** : Maison 9 — Tes voyages, tes études supérieures, ta quête de sens demandent action immédiate. Tu veux partir loin, comprendre vite, intégrer de nouvelles perspectives qui nourrissent ta soif de découverte.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu plonges dans l'inconnu avec enthousiasme. Tu n'as pas peur de l'étranger, du différent. Cette audace peut ouvrir des portes extraordinaires.

**Tensions possibles** : L'impatience peut te faire survoler sans vraiment approfondir. Tu risques de collectionner les expériences sans les intégrer vraiment.

**Conseil clé** : Explorer avec passion tout en prenant le temps d'intégrer ce que tu découvres.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine que tu veux explorer en profondeur.",
            'week_2': "Lance-toi dans l'apprentissage avec enthousiasme.",
            'week_3': "Connecte ce que tu apprends à ta philosophie de vie.",
            'week_4': "Partage tes découvertes avec d'autres."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sagesse ancrée**

Ta Lune en Bélier en Maison 9 veut explorer et apprendre rapidement. Ton Ascendant Taureau apporte besoin d'ancrage : tu veux que tes découvertes soient concrètes, que ta philosophie soit pratique, que tes voyages nourrissent vraiment.

**Domaine activé** : Maison 9 — Tes explorations et ta quête de sens cherchent à la fois expansion et substance. Tu veux apprendre des choses utiles, voyager confortablement, construire une sagesse durable.

**Ton approche instinctive** : Le Taureau te fait approcher l'apprentissage avec patience et pragmatisme. Tu veux comprendre en profondeur, pas juste survoler. Cette lenteur peut frustrer ton Bélier impatient.

**Tensions possibles** : Le besoin de confort peut limiter ton exploration. Tu risques de rester dans ta zone de confort culturel par peur de l'inconfort de l'inconnu.

**Conseil clé** : Explorer de nouveaux horizons tout en ancrant tes découvertes dans le concret.""",
        'weekly_advice': {
            'week_1': "Définis ce que tu veux vraiment apprendre ou découvrir.",
            'week_2': "Commence un apprentissage structuré et profond.",
            'week_3': "Applique concrètement ce que tu apprends.",
            'week_4': "Ancre ces nouvelles connaissances dans ta vie quotidienne."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Curiosité infinie**

Ta Lune en Bélier en Maison 9 veut explorer avec passion. Ton Ascendant Gémeaux amplifie cette soif de découverte : tu veux tout apprendre, tout explorer, connecter des idées de différentes cultures, devenir un pont entre les mondes.

**Domaine activé** : Maison 9 — Tes voyages, tes apprentissages, ta quête philosophique sont intellectuellement stimulants. Tu peux étudier plusieurs sujets, explorer plusieurs cultures, communiquer sur ce que tu découvres.

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre différentes philosophies et domaines de connaissance. Tu adores comparer, relier, synthétiser. Cette agilité mentale est fascinante.

**Tensions possibles** : La dispersion peut t'empêcher d'approfondir vraiment. Tu risques de tout effleurer sans rien maîtriser, de voyager partout sans vraiment habiter nulle part.

**Conseil clé** : Explorer largement tout en choisissant quelques domaines à vraiment approfondir.""",
        'weekly_advice': {
            'week_1': "Liste toutes les philosophies ou cultures qui t'intéressent.",
            'week_2': "Choisis-en deux ou trois à explorer vraiment.",
            'week_3': "Trouve les connections entre ces différents domaines.",
            'week_4': "Partage ta synthèse avec d'autres."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Quête émotionnelle**

Ta Lune en Bélier en Maison 9 veut explorer courageusement de nouveaux horizons. Ton Ascendant Cancer ajoute dimension émotionnelle : tu cherches un sens qui nourrit ton cœur, une philosophie qui te fait te sentir chez toi partout.

**Domaine activé** : Maison 9 — Tes voyages et ta quête de sens sont profondément liés à ton besoin de sécurité émotionnelle. Tu cherches une sagesse qui te protège, une communauté spirituelle qui t'accueille.

**Ton approche instinctive** : Le Cancer te fait explorer avec sensibilité. Tu t'attaches émotionnellement aux lieux et aux idées. Cette profondeur émotionnelle enrichit ton exploration.

**Tensions possibles** : La peur de l'inconnu peut limiter ton exploration. Tu risques de chercher à recréer ton chez-toi partout au lieu d'accueillir vraiment la différence.

**Conseil clé** : Explorer courageusement tout en créant des points d'ancrage émotionnels.""",
        'weekly_advice': {
            'week_1': "Identifie quelle sagesse pourrait nourrir ton cœur.",
            'week_2': "Explore cette philosophie ou cette culture avec ouverture.",
            'week_3': "Trouve ce qui résonne émotionnellement avec toi.",
            'week_4': "Intègre cette sagesse dans ton cocon intérieur."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Vision inspirante**

Double feu sur la Maison 9 : ta Lune en Bélier et ton Ascendant Lion créent une quête de sens grandiose. Tu veux une philosophie qui t'inspire, des voyages qui te grandissent, une sagesse que tu peux partager généreusement.

**Domaine activé** : Maison 9 — Tes explorations et ta quête de sens cherchent grandeur et rayonnement. Tu veux non seulement apprendre mais aussi enseigner, non seulement voyager mais aussi inspirer les autres à s'ouvrir.

**Ton approche instinctive** : Le Lion te fait aborder l'exploration avec confiance et générosité. Tu veux partager ce que tu découvres, élever les autres avec ta sagesse. Cette inspiration est contagieuse.

**Tensions possibles** : Le besoin d'impressionner peut te faire adopter des philosophies pour leur prestige plutôt que leur vérité. Tu risques de prêcher au lieu d'échanger.

**Conseil clé** : Partager ta sagesse généreusement tout en restant humble face au mystère.""",
        'weekly_advice': {
            'week_1': "Définis la vision philosophique qui t'inspire vraiment.",
            'week_2': "Explore-la avec passion et confiance.",
            'week_3': "Partage généreusement tes découvertes.",
            'week_4': "Inspire les autres sans imposer ta vision."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Sagesse pratique**

Ta Lune en Bélier en Maison 9 veut explorer et apprendre rapidement. Ton Ascendant Vierge apporte discernement et pragmatisme : tu veux une sagesse qui serve vraiment, des connaissances applicables, pas juste des théories.

**Domaine activé** : Maison 9 — Tes explorations et apprentissages cherchent utilité et précision. Tu veux maîtriser ce que tu étudies, comprendre les détails, appliquer concrètement ce que tu apprends.

**Ton approche instinctive** : La Vierge te fait analyser chaque philosophie avec esprit critique. Tu ne gobes pas tout, tu testes, tu vérifies. Cette rigueur peut être une force ou te fermer à l'intuition.

**Tensions possibles** : Le perfectionnisme peut t'empêcher d'explorer librement. Tu risques de critiquer au lieu d'apprendre, de rejeter ce qui n'est pas immédiatement pratique.

**Conseil clé** : Apprendre avec discernement tout en restant ouvert·e à ce qui dépasse la logique.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine de connaissance pratiquement utile.",
            'week_2': "Étudie-le méthodiquement, en profondeur.",
            'week_3': "Applique concrètement ce que tu apprends.",
            'week_4': "Évalue l'utilité réelle de ces nouvelles connaissances."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Philosophie harmonieuse**

Ta Lune en Bélier en Maison 9 veut explorer avec passion. Ton Ascendant Balance ajoute recherche d'équilibre et de beauté : tu veux une philosophie qui crée l'harmonie, des voyages qui ouvrent au dialogue interculturel.

**Domaine activé** : Maison 9 — Tes explorations et ta quête de sens cherchent à relier plutôt qu'à diviser. Tu veux comprendre différentes perspectives, trouver des ponts entre les cultures, créer de la beauté dans la diversité.

**Ton approche instinctive** : La Balance te fait aborder l'apprentissage avec ouverture et diplomatie. Tu cherches ce qui unit plutôt que ce qui sépare. Cette capacité à voir tous les côtés enrichit ta sagesse.

**Tensions possibles** : Tu risques de rester en surface pour ne pas choisir. L'impulsivité du Bélier peut te pousser à juger avant d'avoir vraiment écouté.

**Conseil clé** : Explorer avec ouverture tout en osant prendre position quand nécessaire.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie ou culture très différente de la tienne.",
            'week_2': "Cherche les points communs avec ta propre vision.",
            'week_3': "Engage un dialogue respectueux sur les différences.",
            'week_4': "Intègre cette perspective élargie dans ta sagesse."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Quête profonde**

Ta Lune en Bélier en Maison 9 veut explorer avec courage. Ton Ascendant Scorpion ajoute besoin de profondeur et de transformation : tu ne veux pas des connaissances superficielles mais une sagesse qui change ta vie.

**Domaine activé** : Maison 9 — Tes explorations et ta quête de sens touchent les mystères de l'existence. Tu veux comprendre ce qui est caché, les philosophies occultes, les vérités taboues. La superficialité te répugne.

**Ton approche instinctive** : Le Scorpion te fait plonger dans les profondeurs du savoir. Tu veux tout comprendre, percer les secrets. Cette intensité peut mener à des insights profonds ou à l'obsession.

**Tensions possibles** : L'excès de sérieux peut tuer la joie de la découverte. Tu risques de tout voir comme initiation au lieu de simplement explorer.

**Conseil clé** : Chercher la profondeur tout en gardant la légèreté de l'explorateur.""",
        'weekly_advice': {
            'week_1': "Identifie un mystère philosophique qui t'obsède.",
            'week_2': "Plonge dans cette quête avec intensité.",
            'week_3': "Partage ce que tu découvres de transformant.",
            'week_4': "Intègre cette sagesse profonde dans ta vie."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Expansion totale**

Double feu sur la Maison 9, sa maison naturelle : ta Lune en Bélier et ton Ascendant Sagittaire créent une soif d'exploration et de sens maximale. Tu es né·e pour voyager, apprendre, enseigner, élargir constamment tes horizons.

**Domaine activé** : Maison 9 — Tes voyages, tes études, ta quête philosophique sont à leur maximum. Tu veux tout explorer, tout comprendre, connecter le monde entier. L'expansion est ton état naturel.

**Ton approche instinctive** : Le Sagittaire te fait aborder la vie comme une aventure de découverte. Tu es optimiste, ouvert, enthousiaste. Cette énergie inspirante peut ouvrir toutes les portes.

**Tensions possibles** : L'excès d'expansion peut créer de la dispersion. Tu risques de ne jamais t'installer, de fuir l'intimité par le mouvement constant.

**Conseil clé** : Explorer infiniment tout en trouvant aussi ton centre intérieur stable.""",
        'weekly_advice': {
            'week_1': "Planifie une aventure qui élargit vraiment tes horizons.",
            'week_2': "Lance-toi dans cette exploration avec confiance.",
            'week_3': "Partage tes découvertes généreusement.",
            'week_4': "Ancre aussi un peu cette expansion dans l'intégration."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Sagesse ambitieuse**

Ta Lune en Bélier en Maison 9 veut explorer et apprendre avec passion. Ton Ascendant Capricorne ajoute dimension d'ambition et de structure : tu veux que tes connaissances servent ta carrière, que ta sagesse construise ton autorité.

**Domaine activé** : Maison 9 — Tes études et explorations deviennent stratégiques. Tu veux acquérir des expertises reconnues, des diplômes prestigieux, une sagesse qui te donne du pouvoir et de la crédibilité.

**Ton approche instinctive** : Le Capricorne te fait aborder l'apprentissage avec sérieux et long terme. Tu es prêt·e à étudier longuement pour devenir expert·e. Cette discipline peut sublimer ton exploration.

**Tensions possibles** : L'ambition peut tuer la joie de la découverte. Tu risques d'apprendre pour impressionner plutôt que par passion véritable.

**Conseil clé** : Construire ton expertise avec ambition tout en gardant la passion de l'apprentissage.""",
        'weekly_advice': {
            'week_1': "Définis quelle expertise pourrait servir ton ambition.",
            'week_2': "Commence un cursus sérieux dans ce domaine.",
            'week_3': "Maintiens ta discipline même quand c'est difficile.",
            'week_4': "Mesure tes progrès vers la maîtrise."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Philosophie avant-garde**

Ta Lune en Bélier en Maison 9 veut explorer avec audace. Ton Ascendant Verseau ajoute originalité et vision futuriste : tu veux des philosophies innovantes, des sagesses alternatives, explorer ce que personne n'a encore découvert.

**Domaine activé** : Maison 9 — Tes explorations et ta quête de sens sortent des sentiers battus. Tu t'intéresses aux philosophies marginales, aux sciences avant-gardistes, aux cultures sous-représentées.

**Ton approche instinctive** : Le Verseau te fait aborder l'apprentissage avec indépendance et originalité. Tu refuses les dogmes établis. Cette liberté intellectuelle peut être révolutionnaire.

**Tensions possibles** : Être différent juste pour l'être peut te marginaliser. Tu risques de rejeter toute sagesse traditionnelle même quand elle a de la valeur.

**Conseil clé** : Explorer l'avant-garde tout en respectant aussi la sagesse ancestrale.""",
        'weekly_advice': {
            'week_1': "Identifie une philosophie ou un domaine vraiment innovant.",
            'week_2': "Explore-le avec un esprit libre et critique.",
            'week_3': "Connecte-toi à d'autres pionniers de ce domaine.",
            'week_4': "Vérifie que ton originalité sert vraiment ta quête de sens."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 9, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Quête mystique**

Ta Lune en Bélier en Maison 9 veut explorer courageusement. Ton Ascendant Poissons ajoute dimension spirituelle et intuitive : tu cherches une sagesse qui transcende la raison, une connexion au divin, une philosophie du cœur et de l'âme.

**Domaine activé** : Maison 9 — Tes explorations et ta quête de sens sont profondément spirituelles. Tu veux comprendre les mystères de l'univers, te connecter au sacré, trouver une philosophie qui nourrit ton âme.

**Ton approche instinctive** : Le Poissons te fait explorer par intuition et résonance. Tu ressens la vérité plus que tu ne la comprends. Cette sensibilité peut ouvrir des dimensions invisibles.

**Tensions possibles** : Le manque de structure peut te faire te perdre dans le mysticisme. Tu risques de croire n'importe quoi qui sonne spirituel sans discernement.

**Conseil clé** : Suivre ton intuition spirituelle tout en gardant un minimum de discernement.""",
        'weekly_advice': {
            'week_1': "Médite sur ce que ton âme cherche vraiment à comprendre.",
            'week_2': "Explore une philosophie spirituelle qui résonne avec toi.",
            'week_3': "Partage tes insights mystiques avec humilité.",
            'week_4': "Ancre tes découvertes spirituelles dans ta vie concrète."
        }
    },

    # ==================== MAISON 10 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Ambition conquérante**

Double feu sur la Maison 10 : ta Lune en Bélier et ton Ascendant Bélier activent intensément ton ambition, ta carrière, ton besoin de réussite publique. Tu veux atteindre le sommet, être reconnu·e, laisser ta marque.

**Domaine activé** : Maison 10 — Ta carrière, ton statut social, tes accomplissements publics demandent toute ton énergie. Tu veux être le·la premier·ère, le·la meilleur·e, celui·celle dont on se souvient.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu abordes ta carrière comme une bataille à gagner. Tu fonces, tu prends des risques, tu ne te laisses pas arrêter par les obstacles. Cette audace peut propulser ta réussite.

**Tensions possibles** : L'impatience peut te faire brûler les étapes nécessaires. Tu risques de vouloir tout maintenant, de brusquer les processus qui demandent du temps.

**Conseil clé** : Poursuivre tes ambitions avec fougue tout en acceptant les étapes de la construction.""",
        'weekly_advice': {
            'week_1': "Clarifie ton ambition professionnelle principale.",
            'week_2': "Prends une initiative audacieuse vers ce sommet.",
            'week_3': "Persiste face aux obstacles sans t'épuiser.",
            'week_4': "Célèbre les victoires obtenues ce mois-ci."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Réussite durable**

Ta Lune en Bélier en Maison 10 veut réussir rapidement et visiblement. Ton Ascendant Taureau apporte patience et construction : tu veux bâtir une carrière solide, un statut durable, une réussite qui traverse le temps.

**Domaine activé** : Maison 10 — Ta carrière et tes ambitions cherchent à la fois momentum et solidité. Tu veux avancer vite mais aussi construire des fondations professionnelles inébranlables.

**Ton approche instinctive** : Le Taureau te fait construire ta carrière progressivement, investir dans des compétences durables. Cette patience peut frustrer ton Bélier impatient mais elle assure ton succès.

**Tensions possibles** : Tu peux osciller entre fougue ambitieuse et prudence excessive. Le besoin de sécurité peut freiner les prises de risques nécessaires à l'avancement.

**Conseil clé** : Construire ton succès pierre par pierre tout en saisissant les opportunités.""",
        'weekly_advice': {
            'week_1': "Définis quel type de carrière durable tu veux construire.",
            'week_2': "Investis dans une compétence qui te servira longtemps.",
            'week_3': "Fais un pas concret même s'il semble petit.",
            'week_4': "Apprécie les fondations solides que tu as posées."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Carrière polyvalente**

Ta Lune en Bélier en Maison 10 veut réussir avec énergie. Ton Ascendant Gémeaux ajoute polyvalence et communication : tu peux exceller dans plusieurs domaines, ta carrière passe par tes talents de communicateur·rice.

**Domaine activé** : Maison 10 — Ta carrière et ton statut se construisent par la diversité. Tu peux avoir plusieurs casquettes professionnelles, jongler entre différents projets, te faire connaître par ta communication.

**Ton approche instinctive** : Le Gémeaux te fait aborder ta carrière avec agilité. Tu t'adaptes rapidement, tu apprends vite de nouvelles compétences. Cette versatilité est un atout dans le monde moderne.

**Tensions possibles** : La dispersion peut t'empêcher de vraiment exceller. Tu risques d'être bon·ne dans plein de choses sans être expert·e en rien, ce qui peut limiter ton ascension.

**Conseil clé** : Utiliser ta polyvalence comme force tout en développant une expertise centrale.""",
        'weekly_advice': {
            'week_1': "Liste toutes tes compétences professionnelles.",
            'week_2': "Identifie celle qui pourrait devenir ton cœur d'expertise.",
            'week_3': "Communique activement sur ce que tu sais faire.",
            'week_4': "Évalue si ta polyvalence sert vraiment ton avancement."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Leadership nourricier**

Ta Lune en Bélier en Maison 10 veut s'imposer professionnellement. Ton Ascendant Cancer ajoute dimension de soin et de protection : tu veux réussir en prenant soin des autres, diriger avec empathie, créer une carrière qui nourrit.

**Domaine activé** : Maison 10 — Ta carrière et ton statut passent par ta capacité à prendre soin. Tu peux exceller dans des domaines liés au service, à l'aide, à la création d'espaces sécurisants pour les autres.

**Ton approche instinctive** : Le Cancer te fait aborder ta carrière avec sensibilité et intuition. Tu ressens les besoins de ton public, de tes clients. Cette empathie peut être ta marque distinctive.

**Tensions possibles** : La sensibilité peut te faire prendre les critiques professionnelles trop à cœur. Tu risques de te sur-investir émotionnellement dans ton travail.

**Conseil clé** : Réussir par l'empathie tout en maintenant des limites professionnelles saines.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton travail peut nourrir les autres.",
            'week_2': "Prends une initiative qui montre ton leadership empathique.",
            'week_3': "Protège-toi de l'épuisement émotionnel au travail.",
            'week_4': "Célèbre l'impact positif que tu as créé."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Rayonnement professionnel**

Double feu sur la Maison 10 : ta Lune en Bélier et ton Ascendant Lion créent une ambition éclatante. Tu veux non seulement réussir mais briller, être célèbre, laisser un héritage dont on se souviendra. La grandeur t'appelle.

**Domaine activé** : Maison 10 — Ta carrière et ton statut cherchent la reconnaissance maximum. Tu veux être au sommet, inspirar les autres, recevoir les applaudissements que tu mérites. L'excellence est ton standard.

**Ton approche instinctive** : Le Lion te fait aborder ta carrière avec confiance royale. Tu ne doutes pas que tu peux atteindre le sommet. Cette foi en toi peut attirer le succès.

**Tensions possibles** : L'ego peut devenir obstacle. Tu risques de vouloir impressionner plus que servir, ou de mal gérer l'échec nécessaire à l'apprentissage.

**Conseil clé** : Viser le sommet avec confiance tout en restant humble face au chemin.""",
        'weekly_advice': {
            'week_1': "Définis quel héritage professionnel tu veux laisser.",
            'week_2': "Fais quelque chose d'audacieux qui te met en lumière.",
            'week_3': "Partage généreusement ton succès avec ton équipe.",
            'week_4': "Célèbre tes accomplissements sans arrogance."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Excellence méticuleuse**

Ta Lune en Bélier en Maison 10 veut réussir rapidement. Ton Ascendant Vierge apporte perfectionnisme et méthode : tu veux exceller par la qualité impeccable de ton travail, être reconnu·e pour ton expertise technique.

**Domaine activé** : Maison 10 — Ta carrière et ton statut se construisent par la maîtrise et le service d'excellence. Tu veux que chaque détail soit parfait, que ton travail soit irréprochable.

**Ton approche instinctive** : La Vierge te fait aborder ta carrière avec rigueur et dévouement. Tu travailles dur, tu améliores constamment. Cette discipline peut mener à la vraie maîtrise.

**Tensions possibles** : Le perfectionnisme peut devenir paralysie. Tu risques de ne jamais te sentir prêt·e, de trop critiquer ton propre travail, de manquer d'opportunités par excès de prudence.

**Conseil clé** : Viser l'excellence tout en acceptant que le parfait soit l'ennemi du bien.""",
        'weekly_advice': {
            'week_1': "Identifie le standard d'excellence que tu veux atteindre.",
            'week_2': "Travaille méthodiquement vers cette maîtrise.",
            'week_3': "Accepte aussi de montrer ton travail imparfait.",
            'week_4': "Mesure objectivement tes progrès professionnels."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomatie ambitieuse**

Ta Lune en Bélier en Maison 10 veut s'imposer professionnellement. Ton Ascendant Balance ajoute élégance et collaboration : tu veux réussir en créant des partenariats, en étant juste, en apportant beauté et harmonie.

**Domaine activé** : Maison 10 — Ta carrière et ton statut se construisent par tes capacités relationnelles. Tu peux exceller dans la négociation, la médiation, tout ce qui demande équilibre et grâce.

**Ton approche instinctive** : La Balance te fait aborder ta carrière avec diplomatie. Tu sais naviguer les politiques d'entreprise, créer des alliances. Cette intelligence relationnelle peut t'ouvrir des portes.

**Tensions possibles** : Tu risques de trop chercher l'approbation au détriment de ton authentique ambition. L'impulsivité du Bélier peut rompre l'harmonie que tu tentes de créer.

**Conseil clé** : Réussir par la collaboration tout en restant fidèle à ton ambition personnelle.""",
        'weekly_advice': {
            'week_1': "Identifie quels partenariats pourraient servir ton avancement.",
            'week_2': "Crée ou renforce une alliance professionnelle stratégique.",
            'week_3': "Négocie pour toi-même sans sacrifier la relation.",
            'week_4': "Évalue si tes collaborations te respectent vraiment."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir stratégique**

Ta Lune en Bélier en Maison 10 veut conquérir le sommet. Ton Ascendant Scorpion ajoute intensité et stratégie : tu ne veux pas juste réussir, tu veux le pouvoir réel, l'influence profonde, la transformation de ton domaine.

**Domaine activé** : Maison 10 — Ta carrière et ton statut deviennent terrain de conquête stratégique. Tu veux comprendre les mécanismes du pouvoir, les utiliser, transformer ton industrie de l'intérieur.

**Ton approche instinctive** : Le Scorpion te fait aborder ta carrière avec intensité et perspicacité. Tu vois ce que les autres ne voient pas, tu comprends les dynamiques cachées. Ce pouvoir peut être fascinant ou intimidant.

**Tensions possibles** : L'obsession du contrôle peut créer des ennemis. Tu risques de manipuler au lieu de diriger, de vouloir le pouvoir pour lui-même au lieu de servir une vision.

**Conseil clé** : Utiliser ton pouvoir stratégique au service d'une transformation positive.""",
        'weekly_advice': {
            'week_1': "Identifie les vrais leviers de pouvoir dans ton domaine.",
            'week_2': "Positionne-toi stratégiquement pour les influencer.",
            'week_3': "Utilise ton influence pour créer du changement positif.",
            'week_4': "Vérifie que ton ambition reste éthique."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vision inspirante**

Double feu sur la Maison 10 : ta Lune en Bélier et ton Ascendant Sagittaire créent une ambition visionnaire. Tu veux réussir en grand, inspirer le monde, créer quelque chose qui a du sens et de l'impact au-delà de toi.

**Domaine activé** : Maison 10 — Ta carrière et ton statut cherchent portée et signification. Tu ne veux pas juste un job, tu veux une mission. Ton succès doit servir une cause plus grande.

**Ton approche instinctive** : Le Sagittaire te fait aborder ta carrière avec optimisme et vision. Tu vois grand, tu inspires les autres avec ton enthousiasme. Cette énergie peut attirer des opportunités extraordinaires.

**Tensions possibles** : L'excès d'optimisme peut te faire sous-estimer les défis. Tu risques de promettre plus que tu ne peux livrer, ou de négliger les détails pratiques.

**Conseil clé** : Poursuivre ta grande vision tout en ancrant ton action dans le réel.""",
        'weekly_advice': {
            'week_1': "Définis la vision professionnelle qui t'inspire vraiment.",
            'week_2': "Partage cette vision pour rallier les autres.",
            'week_3': "Prends des actions concrètes, pas juste des discours.",
            'week_4': "Évalue si ton optimisme produit des résultats tangibles."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Ambition totale**

Ta Lune en Bélier en Maison 10 veut réussir avec énergie. Ton Ascendant Capricorne, maître naturel de cette maison, amplifie cette ambition : tu es né·e pour atteindre le sommet, construire un empire, laisser un héritage durable.

**Domaine activé** : Maison 10 — Ta carrière et ton statut sont ta priorité absolue. Tu veux exceller, être respecté·e, construire quelque chose qui dure après toi. L'ambition coule dans tes veines.

**Ton approche instinctive** : Le Capricorne te fait aborder ta carrière avec sérieux total. Tu es prêt·e à travailler plus dur et plus longtemps que quiconque. Cette discipline garantit presque ton succès.

**Tensions possibles** : L'obsession du succès peut te faire négliger tout le reste. Tu risques de sacrifier santé, relations, joie pour ton ambition.

**Conseil clé** : Construire ton empire tout en gardant une vie en dehors du travail.""",
        'weekly_advice': {
            'week_1': "Définis ton plan de carrière à 10 ans minimum.",
            'week_2': "Travaille avec discipline vers cet objectif.",
            'week_3': "Équilibre ambition et autres aspects de ta vie.",
            'week_4': "Mesure froidement tes progrès vers le sommet."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Carrière innovante**

Ta Lune en Bélier en Maison 10 veut réussir avec audace. Ton Ascendant Verseau ajoute originalité et vision futuriste : tu veux révolutionner ton domaine, créer une carrière unique, être reconnu·e pour ton avant-gardisme.

**Domaine activé** : Maison 10 — Ta carrière et ton statut passent par l'innovation. Tu refuses les chemins conventionnels de réussite. Tu veux créer ton propre modèle, être pionnier·ère dans ton domaine.

**Ton approche instinctive** : Le Verseau te fait aborder ta carrière avec indépendance totale. Tu n'as pas peur d'être différent·e, marginal·e si nécessaire. Cette originalité peut te rendre unique et précieux·se.

**Tensions possibles** : Être trop différent peut te marginaliser professionnellement. Tu risques de rejeter toute structure nécessaire à la réussite juste parce qu'elle est conventionnelle.

**Conseil clé** : Innover dans ta carrière tout en restant connecté·e aux réalités du marché.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu peux révolutionner ton domaine.",
            'week_2': "Lance un projet professionnel vraiment innovant.",
            'week_3': "Connecte-toi à d'autres innovateurs de ton secteur.",
            'week_4': "Vérifie que ton originalité crée vraiment de la valeur."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 10, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Carrière intuitive**

Ta Lune en Bélier en Maison 10 veut réussir avec passion. Ton Ascendant Poissons ajoute dimension spirituelle et créative : tu veux une carrière qui nourrit ton âme, un succès qui a du sens au-delà du matériel.

**Domaine activé** : Maison 10 — Ta carrière et ton statut cherchent à exprimer ton essence profonde. Tu veux réussir en faisant ce qui te touche vraiment, en servant quelque chose de plus grand que toi.

**Ton approche instinctive** : Le Poissons te fait suivre ton intuition professionnelle. Tu peux avoir un chemin de carrière non-linéaire, guidé par des pressentiments plus que par la logique. Cette sensibilité peut mener à une voie unique.

**Tensions possibles** : Le manque de structure peut nuire à ton avancement. Tu risques de rêver ta carrière au lieu de la construire concrètement.

**Conseil clé** : Suivre ton intuition professionnelle tout en créant une structure concrète.""",
        'weekly_advice': {
            'week_1': "Médite sur ce que ton âme veut vraiment accomplir.",
            'week_2': "Suis un pressentiment professionnel même s'il semble illogique.",
            'week_3': "Ancre aussi ton rêve dans des actions concrètes.",
            'week_4': "Vérifie que ton intuition te mène vers du tangible."
        }
    },

    # ==================== MAISON 11 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Réseau guerrier**

Double feu sur la Maison 11 : ta Lune en Bélier et ton Ascendant Bélier activent intensément tes amitiés, tes réseaux, tes projets collectifs. Tu veux créer une tribu de guerriers, une équipe qui partage tes idéaux et ton courage.

**Domaine activé** : Maison 11 — Tes amitiés, tes réseaux sociaux, tes projets de groupe demandent ton leadership. Tu veux rassembler des gens autour d'une cause, initier des mouvements, créer du changement collectif.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu es un leader naturel dans tes groupes. Tu prends des initiatives, tu motives les autres, tu fonces en avant. Cette énergie peut galvaniser ton réseau.

**Tensions possibles** : Tu risques de vouloir tout diriger au lieu de collaborer vraiment. L'impatience avec le rythme de groupe peut créer des conflits.

**Conseil clé** : Mener tes groupes avec énergie tout en respectant l'autonomie de chacun·e.""",
        'weekly_advice': {
            'week_1': "Identifie la cause collective qui te passionne vraiment.",
            'week_2': "Rassemble des gens autour de cette vision.",
            'week_3': "Lance une initiative collective concrète.",
            'week_4': "Célèbre ce que vous avez créé ensemble."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Communauté stable**

Ta Lune en Bélier en Maison 11 veut créer rapidement des projets collectifs. Ton Ascendant Taureau apporte loyauté et construction : tu veux des amitiés durables, un réseau solide, des projets de groupe qui résistent au temps.

**Domaine activé** : Maison 11 — Tes amitiés et réseaux cherchent à la fois dynamisme et fiabilité. Tu veux des gens sur qui compter vraiment, avec qui construire quelque chose de durable ensemble.

**Ton approche instinctive** : Le Taureau te fait choisir soigneusement tes ami·es et tes projets collectifs. Une fois engagé·e, tu es loyal·e et constant·e. Cette stabilité crée des liens profonds.

**Tensions possibles** : L'impulsivité du Bélier peut créer des engagements que ton Taureau regrette ensuite. Tu peux alterner entre enthousiasme pour le groupe et retrait pour te protéger.

**Conseil clé** : Créer des projets collectifs durables tout en gardant ton enthousiasme initial.""",
        'weekly_advice': {
            'week_1': "Identifie quels ami·es et réseaux méritent ton investissement.",
            'week_2': "Engage-toi concrètement dans un projet de groupe.",
            'week_3': "Construis la confiance progressivement.",
            'week_4': "Apprécie la solidité des liens que tu as créés."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Réseau vivant**

Ta Lune en Bélier en Maison 11 veut créer des projets collectifs avec énergie. Ton Ascendant Gémeaux ajoute curiosité et communication : tu veux un réseau diversifié, des amitiés stimulantes intellectuellement, des échanges constants.

**Domaine activé** : Maison 11 — Tes amitiés et réseaux passent par la communication et la variété. Tu peux avoir des ami·es de tous horizons, participer à plusieurs groupes, être le lien entre différentes communautés.

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre différents groupes et projets. Tu adores connecter les gens, faciliter les échanges. Cette agilité sociale est précieuse.

**Tensions possibles** : La dispersion peut t'empêcher d'approfondir vraiment tes amitiés. Tu risques d'avoir mille connaissances mais peu de vrais ami·es.

**Conseil clé** : Cultiver un réseau large tout en approfondissant quelques amitiés essentielles.""",
        'weekly_advice': {
            'week_1': "Explore de nouveaux cercles sociaux ou communautés.",
            'week_2': "Connecte des gens qui devraient se connaître.",
            'week_3': "Approfondis aussi une ou deux amitiés clés.",
            'week_4': "Évalue la qualité versus la quantité de ton réseau."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Tribu émotionnelle**

Ta Lune en Bélier en Maison 11 veut créer des projets collectifs avec passion. Ton Ascendant Cancer ajoute besoin d'intimité et de sécurité : tu veux un réseau qui soit comme une famille, des ami·es qui deviennent ta tribu du cœur.

**Domaine activé** : Maison 11 — Tes amitiés et projets de groupe sont profondément émotionnels. Tu veux créer un sentiment d'appartenance, nourrir tes ami·es, être nourri·e en retour. La communauté devient ton foyer élargi.

**Ton approche instinctive** : Le Cancer te fait aborder tes groupes avec sensibilité et protection. Tu prends soin de tes ami·es, tu crées des rituels collectifs. Cette chaleur crée des liens puissants.

**Tensions possibles** : Tu risques de te sur-investir émotionnellement dans tes groupes. L'impulsivité du Bélier peut créer des conflits dans ta famille choisie.

**Conseil clé** : Créer ta tribu émotionnelle tout en maintenant des limites saines.""",
        'weekly_advice': {
            'week_1': "Identifie qui dans ton réseau mérite vraiment ton cœur.",
            'week_2': "Crée des moments d'intimité collective avec ces personnes.",
            'week_3': "Protège-toi des dynamiques de groupe toxiques.",
            'week_4': "Célèbre la famille que tu as choisie."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Leadership inspirant**

Double feu sur la Maison 11 : ta Lune en Bélier et ton Ascendant Lion créent un magnétisme social puissant. Tu attires naturellement un réseau, tu inspires tes ami·es, tu mènes des projets collectifs avec charisme.

**Domaine activé** : Maison 11 — Tes amitiés et réseaux te mettent en lumière. Tu peux être le·la leader·euse naturel·le de tes groupes, celui·celle qui inspire et motive. Ta générosité sociale crée de la loyauté.

**Ton approche instinctive** : Le Lion te fait briller au sein de tes groupes. Tu donnes généreusement, tu célèbres tes ami·es. Cette chaleur et cette confiance attirent les gens vers toi.

**Tensions possibles** : Le besoin d'être au centre peut nuire à la dynamique de groupe. Tu risques de vouloir être la star au lieu de cultiver l'égalité.

**Conseil clé** : Inspirer ton réseau tout en laissant les autres briller aussi.""",
        'weekly_advice': {
            'week_1': "Rassemble ton réseau autour d'une vision inspirante.",
            'week_2': "Mène avec générosité et enthousiasme.",
            'week_3': "Célèbre aussi les succès des autres membres.",
            'week_4': "Vérifie que ton leadership sert le collectif, pas ton ego."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Service collectif**

Ta Lune en Bélier en Maison 11 veut créer des projets de groupe avec énergie. Ton Ascendant Vierge apporte organisation et utilité : tu veux que tes groupes servent vraiment, que tes projets collectifs soient efficaces et concrets.

**Domaine activé** : Maison 11 — Tes amitiés et réseaux cherchent à être utiles. Tu peux organiser des groupes de travail, créer des systèmes pour ton réseau, améliorer le fonctionnement de tes communautés.

**Ton approche instinctive** : La Vierge te fait aborder tes groupes avec pragmatisme. Tu vois ce qui doit être amélioré, tu proposes des solutions concrètes. Cette efficacité peut être précieuse.

**Tensions possibles** : Tu risques de critiquer tes ami·es ou tes groupes au lieu de simplement apprécier. Le perfectionnisme peut nuire à la légèreté nécessaire à l'amitié.

**Conseil clé** : Servir tes groupes efficacement tout en acceptant l'imperfection humaine.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu peux être vraiment utile à ton réseau.",
            'week_2': "Organise ou améliore un aspect de tes projets collectifs.",
            'week_3': "Accepte aussi de simplement profiter de tes ami·es.",
            'week_4': "Apprécie ce que ton réseau apporte, pas juste ce qui manque."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Réseau harmonieux**

Ta Lune en Bélier en Maison 11 veut créer des projets collectifs avec fougue. Ton Ascendant Balance, maître de la Maison 11 alternative, ajoute harmonie et équité : tu veux des groupes où règne la justice, des amitiés équilibrées.

**Domaine activé** : Maison 11 — Tes amitiés et réseaux cherchent l'équilibre parfait. Tu veux que chacun·e soit respecté·e, que les décisions soient prises ensemble, que l'harmonie règne dans tes groupes.

**Ton approche instinctive** : La Balance te fait chercher la paix dans tes relations collectives. Tu es le·la médiateur·rice naturel·le, celui·celle qui équilibre les tensions. Cette diplomatie crée de la cohésion.

**Tensions possibles** : Tu risques de sacrifier tes propres besoins pour la paix du groupe. L'impulsivité du Bélier peut rompre l'harmonie que tu tentes de créer.

**Conseil clé** : Créer de l'harmonie collective tout en exprimant aussi tes besoins personnels.""",
        'weekly_advice': {
            'week_1': "Identifie les déséquilibres dans tes groupes.",
            'week_2': "Propose des solutions qui respectent tous·tes.",
            'week_3': "Exprime aussi ce dont tu as besoin personnellement.",
            'week_4': "Célèbre l'harmonie que tu as contribué à créer."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Transformation collective**

Ta Lune en Bélier en Maison 11 veut créer des projets collectifs puissants. Ton Ascendant Scorpion ajoute intensité et profondeur : tu veux des groupes qui transforment vraiment, des ami·es avec qui explorer les profondeurs.

**Domaine activé** : Maison 11 — Tes amitiés et réseaux touchent les zones intenses. Tu peux créer des groupes de guérison, de transformation, de changement radical. Tes ami·es deviennent des allié·es dans ton évolution.

**Ton approche instinctive** : Le Scorpion te fait vivre tes groupes avec intensité. Tu veux des liens profonds, pas superficiels. Tu es loyal·e à mort mais exigeant·e. Cette profondeur peut créer des fraternités puissantes.

**Tensions possibles** : L'obsession du contrôle peut créer des dynamiques toxiques. Tu risques de vouloir que tes ami·es évoluent selon ta vision.

**Conseil clé** : Créer des transformations collectives tout en respectant le chemin de chacun·e.""",
        'weekly_advice': {
            'week_1': "Identifie quels ami·es sont prêt·es pour une vraie profondeur.",
            'week_2': "Crée un espace de transformation collective.",
            'week_3': "Respecte aussi les limites et le rythme des autres.",
            'week_4': "Célèbre la puissance de votre évolution commune."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Communauté visionnaire**

Double feu sur la Maison 11 : ta Lune en Bélier et ton Ascendant Sagittaire créent un réseau inspirant et optimiste. Tu veux rassembler des gens autour d'une vision, créer des mouvements qui changent le monde, explorer en groupe.

**Domaine activé** : Maison 11 — Tes amitiés et projets collectifs cherchent sens et expansion. Tu veux que tes groupes servent une cause plus grande, que tes ami·es partagent tes idéaux et ta soif d'aventure.

**Ton approche instinctive** : Le Sagittaire te fait créer des réseaux autour de visions inspirantes. Tu rassembles des gens de différents horizons autour de valeurs communes. Cette capacité à inspirer est puissante.

**Tensions possibles** : L'excès d'optimisme peut créer des désillusions. Tu risques de promettre plus que le groupe ne peut livrer, ou de t'enthousiasmer sans vraiment t'engager.

**Conseil clé** : Inspirer ton réseau avec ta vision tout en ancrant vos projets dans le réel.""",
        'weekly_advice': {
            'week_1': "Définis la vision collective qui t'inspire vraiment.",
            'week_2': "Rassemble des gens autour de cet idéal.",
            'week_3': "Lancez ensemble un projet concret, pas juste des discours.",
            'week_4': "Célèbre ce que votre vision a créé de tangible."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Réseau stratégique**

Ta Lune en Bélier en Maison 11 veut créer des projets collectifs avec énergie. Ton Ascendant Capricorne apporte structure et ambition : tu veux un réseau qui sert tes objectifs, des ami·es qui t'aident à grimper, des alliances stratégiques.

**Domaine activé** : Maison 11 — Tes amitiés et réseaux deviennent stratégiques pour ton avancement. Tu choisis soigneusement qui entre dans ton cercle, tu construis des alliances qui durent et qui servent.

**Ton approche instinctive** : Le Capricorne te fait aborder tes réseaux avec sérieux et long terme. Tu investis dans des relations qui peuvent t'aider professionnellement. Cette pragmatisme peut être efficace ou froid.

**Tensions possibles** : Tu risques de voir tes ami·es comme des outils. L'impulsivité du Bélier peut créer des liens que ton Capricorne calcule ensuite.

**Conseil clé** : Construire un réseau stratégique tout en cultivant aussi de vraies amitiés désintéressées.""",
        'weekly_advice': {
            'week_1': "Identifie quels réseaux servent vraiment tes ambitions.",
            'week_2': "Investis stratégiquement dans ces relations.",
            'week_3': "Cultive aussi des amitiés juste pour la joie.",
            'week_4': "Évalue si ton réseau t'aide vraiment à avancer."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolution collective**

Ta Lune en Bélier en Maison 11 veut créer des projets collectifs audacieux. Ton Ascendant Verseau, maître naturel de cette maison, amplifie cette énergie : tu veux révolutionner la société, créer des communautés alternatives, innover ensemble.

**Domaine activé** : Maison 11 — Tes amitiés, tes réseaux, tes projets collectifs sont au maximum de leur potentiel transformateur. Tu peux rassembler des marginaux, créer des mouvements avant-gardistes, être pionnier·ère social·e.

**Ton approche instinctive** : Le Verseau te fait voir tes groupes comme des laboratoires d'expérimentation sociale. Tu n'as pas peur de l'originalité collective. Cette vision peut créer de vraies innovations.

**Tensions possibles** : Tu risques de rejeter toute tradition collective même quand elle a de la valeur. L'excès d'idéalisme peut déconnecter tes projets de la réalité.

**Conseil clé** : Révolutionner le collectif tout en restant connecté·e aux besoins humains de base.""",
        'weekly_advice': {
            'week_1': "Identifie quel système collectif tu veux révolutionner.",
            'week_2': "Rassemble d'autres révolutionnaires autour de cette vision.",
            'week_3': "Expérimentez ensemble de nouvelles formes de communauté.",
            'week_4': "Évalue si votre innovation sert vraiment le bien commun."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 11, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Communauté spirituelle**

Ta Lune en Bélier en Maison 11 veut créer des projets collectifs avec passion. Ton Ascendant Poissons ajoute dimension spirituelle et empathique : tu veux une communauté d'âmes, un réseau qui partage ta quête mystique, des ami·es qui comprennent l'invisible.

**Domaine activé** : Maison 11 — Tes amitiés et projets de groupe cherchent connexion spirituelle. Tu peux créer des cercles de méditation, des communautés de guérison, des réseaux basés sur la compassion universelle.

**Ton approche instinctive** : Le Poissons te fait vivre tes groupes avec une sensibilité profonde. Tu ressens l'énergie collective, tu t'adaptes intuitivement. Cette empathie crée des liens d'âme.

**Tensions possibles** : Le manque de limites peut te faire perdre dans le groupe. Tu risques de te sacrifier pour la communauté ou de projeter des idéaux impossibles.

**Conseil clé** : Créer des communautés spirituelles tout en maintenant ton individualité.""",
        'weekly_advice': {
            'week_1': "Identifie quelle communauté spirituelle résonne avec ton âme.",
            'week_2': "Connecte-toi authentiquement à ces personnes.",
            'week_3': "Maintiens des limites claires malgré la fusion.",
            'week_4': "Célèbre la beauté de votre connexion d'âmes."
        }
    },

    # ==================== MAISON 12 ====================

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Guerrier intérieur**

Double feu sur la Maison 12 : ta Lune en Bélier et ton Ascendant Bélier plongent dans ton inconscient avec courage. Tu veux affronter tes démons intérieurs, conquérir tes peurs, libérer ce qui est caché en toi. La solitude devient terrain de bataille.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude demandent attention. Tu es appelé·e à explorer ton monde intérieur, à guérir tes blessures cachées, à te connecter à quelque chose de plus grand.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu n'as pas peur de plonger dans tes zones d'ombre. Tu veux tout affronter, tout comprendre. Cette bravoure intérieure peut être libératrice.

**Tensions possibles** : L'impulsivité peut brusquer des processus intérieurs qui demandent douceur. Tu risques de vouloir tout régler vite alors que l'inconscient a son propre rythme.

**Conseil clé** : Explorer courageusement ton monde intérieur tout en respectant son mystère.""",
        'weekly_advice': {
            'week_1': "Identifie une peur ou une ombre que tu veux affronter.",
            'week_2': "Crée de l'espace pour l'introspection et la solitude.",
            'week_3': "Traverse ce que tu découvres avec courage et douceur.",
            'week_4': "Intègre les insights gagnés dans ta vie consciente."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Paix ancrée**

Ta Lune en Bélier en Maison 12 veut explorer son inconscient avec énergie. Ton Ascendant Taureau apporte besoin d'ancrage et de douceur : tu veux que ta vie intérieure soit un refuge paisible, que ta spiritualité soit sensuelle et concrète.

**Domaine activé** : Maison 12 — Ton intériorité et ta spiritualité cherchent à la fois profondeur et confort. Tu as besoin de temps seul·e pour te ressourcer, de pratiques spirituelles qui nourrissent ton corps aussi.

**Ton approche instinctive** : Le Taureau te fait aborder ton monde intérieur avec patience. Tu prends le temps de sentir, de savourer le silence. Cette lenteur peut apaiser ton feu intérieur.

**Tensions possibles** : L'impatience du Bélier peut se heurter à ton besoin de lenteur intérieure. Tu peux résister à l'introspection par peur de perdre tes repères concrets.

**Conseil clé** : Explorer ton inconscient avec douceur et patience, sans forcer.""",
        'weekly_advice': {
            'week_1': "Crée un espace de ressourcement confortable pour toi.",
            'week_2': "Pratique une spiritualité incarnée (yoga, marche méditative).",
            'week_3': "Prends du temps seul·e dans la nature.",
            'week_4': "Ancre dans ton corps les insights de ton intériorité."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Inconscient parlant**

Ta Lune en Bélier en Maison 12 veut explorer son monde intérieur. Ton Ascendant Gémeaux ajoute besoin de comprendre et de nommer : tu veux analyser tes rêves, parler de ton inconscient, écrire sur tes découvertes intérieures.

**Domaine activé** : Maison 12 — Ton inconscient et ta spiritualité passent par les mots et la compréhension. Tu peux écrire un journal intime, explorer la psychologie, communiquer sur ton chemin spirituel.

**Ton approche instinctive** : Le Gémeaux te fait intellectualiser ton monde intérieur. Tu veux comprendre tes rêves, analyser tes patterns. Cette approche mentale peut éclairer ou te faire fuir le ressenti.

**Tensions possibles** : Tu risques de rester en surface par peur de vraiment plonger. L'analyse peut devenir une défense contre l'expérience réelle de l'inconscient.

**Conseil clé** : Comprendre ton monde intérieur tout en acceptant aussi le mystère indicible.""",
        'weekly_advice': {
            'week_1': "Commence un journal de tes rêves et insights intérieurs.",
            'week_2': "Lis ou écoute quelque chose sur la psychologie de l'inconscient.",
            'week_3': "Autorise-toi aussi à simplement ressentir sans analyser.",
            'week_4': "Partage certaines découvertes avec quelqu'un de confiance."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Guérison profonde**

Ta Lune en Bélier en Maison 12 veut affronter courageusement son inconscient. Ton Ascendant Cancer ajoute sensibilité émotionnelle : ton monde intérieur est un océan de sentiments anciens, de blessures à guérir, de douceur à retrouver.

**Domaine activé** : Maison 12 — Ton inconscient et ta spiritualité sont profondément émotionnels. Tu peux revisiter des blessures d'enfance, guérir ta relation avec ta mère ou ta famille, retrouver ton innocence perdue.

**Ton approche instinctive** : Le Cancer te fait vivre ton intériorité avec une grande sensibilité. Tu ressens tout profondément. Cette perméabilité émotionnelle peut faciliter la guérison si tu ne te noies pas.

**Tensions possibles** : Tu risques d'être submergé·e par tes émotions inconscientes. L'impulsivité du Bélier peut rouvrir des blessures sans protection adéquate.

**Conseil clé** : Guérir courageusement tes blessures profondes tout en te protégeant émotionnellement.""",
        'weekly_advice': {
            'week_1': "Identifie une blessure émotionnelle ancienne prête à guérir.",
            'week_2': "Crée un espace sécurisant pour explorer cette douleur.",
            'week_3': "Traverse l'émotion avec courage et auto-compassion.",
            'week_4': "Remercie-toi pour ce travail de guérison profonde."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Lumière intérieure**

Double feu sur la Maison 12 : ta Lune en Bélier et ton Ascendant Lion explorent l'inconscient avec confiance. Tu veux découvrir ton or caché, ta puissance intérieure, l'éclat de ton âme sous les couches d'ombre.

**Domaine activé** : Maison 12 — Ton inconscient et ta spiritualité cherchent à révéler ta grandeur authentique. Tu traverses l'ombre pour retrouver ta lumière essentielle. C'est une quête héroïque intérieure.

**Ton approche instinctive** : Le Lion te fait aborder ton monde intérieur avec dignité. Tu ne te laisses pas abattre par ce que tu découvres. Cette force intérieure peut transformer les ténèbres en lumière.

**Tensions possibles** : L'orgueil peut t'empêcher de vraiment accepter tes zones d'ombre. Tu risques de nier ce qui ne correspond pas à ton image idéale.

**Conseil clé** : Accepter toutes tes parts, lumière et ombre, pour devenir vraiment entier·ère.""",
        'weekly_advice': {
            'week_1': "Identifie quelle lumière tu caches dans ton ombre.",
            'week_2': "Explore courageusement tes zones les moins glorieuses.",
            'week_3': "Intègre ces découvertes avec compassion pour toi-même.",
            'week_4': "Célèbre qui tu deviens en embrassant ton entièreté."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Purification intérieure**

Ta Lune en Bélier en Maison 12 veut transformer son inconscient. Ton Ascendant Vierge apporte méthode et discernement : tu veux nettoyer ton psyché, purifier ton monde intérieur, éliminer les patterns toxiques avec précision.

**Domaine activé** : Maison 12 — Ton inconscient et ta spiritualité passent par l'analyse et la purification. Tu peux développer des pratiques de nettoyage mental et émotionnel, comprendre méthodiquement tes patterns.

**Ton approche instinctive** : La Vierge te fait aborder ton intériorité avec pragmatisme. Tu veux comprendre comment ton inconscient fonctionne, identifier les dysfonctionnements. Cette lucidité peut être libératrice.

**Tensions possibles** : Le perfectionnisme peut devenir obsession. Tu risques de trop analyser au lieu de simplement ressentir et guérir.

**Conseil clé** : Purifier ton monde intérieur avec méthode tout en acceptant l'imperfection humaine.""",
        'weekly_advice': {
            'week_1': "Identifie les patterns mentaux toxiques à éliminer.",
            'week_2': "Mets en place une pratique quotidienne de purification (méditation, écriture).",
            'week_3': "Accepte que la guérison ne soit pas parfaite ni linéaire.",
            'week_4': "Apprécie le chemin de purification plus que la destination."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Paix intérieure**

Ta Lune en Bélier en Maison 12 veut explorer son inconscient avec courage. Ton Ascendant Balance cherche harmonie et équilibre : tu veux pacifier ton monde intérieur, réconcilier tes parts en conflit, trouver la paix de l'âme.

**Domaine activé** : Maison 12 — Ton inconscient et ta spiritualité cherchent l'équilibre entre action et lâcher-prise, solitude et connexion. Tu veux une vie intérieure harmonieuse et belle.

**Ton approche instinctive** : La Balance te fait chercher la paix intérieure par la réconciliation de tes opposés. Tu veux que toutes tes parts s'entendent. Cette quête d'harmonie peut apaiser ton feu intérieur.

**Tensions possibles** : Tu risques d'éviter les zones d'ombre pour maintenir une fausse paix. L'impulsivité du Bélier peut rompre l'équilibre que tu tentes de créer.

**Conseil clé** : Créer la paix intérieure en embrassant aussi les tensions nécessaires.""",
        'weekly_advice': {
            'week_1': "Identifie quelles parts de toi sont en conflit intérieur.",
            'week_2': "Crée un dialogue entre ces parts, cherche la réconciliation.",
            'week_3': "Développe une pratique de paix intérieure (méditation, art).",
            'week_4': "Célèbre l'harmonie que tu as créée en toi."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Alchimie intérieure**

Ta Lune en Bélier en Maison 12 veut transformer son inconscient. Ton Ascendant Scorpion, en affinité avec cette maison, amplifie cette puissance : tu plonges dans tes abysses intérieurs pour en ressortir totalement transformé·e.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, tes zones d'ombre sont à leur maximum d'intensité. Tu vis des morts et renaissances psychiques profondes. Rien n'est superficiel dans ton monde intérieur.

**Ton approche instinctive** : Le Scorpion te fait plonger sans peur dans tes profondeurs les plus sombres. Tu veux tout voir, tout comprendre, tout transmuter. Cette radicalité intérieure peut être transformatrice ou destructrice.

**Tensions possibles** : L'obsession de tes zones d'ombre peut devenir paralysante. Tu risques de te perdre dans l'inconscient sans retrouver le chemin vers la lumière.

**Conseil clé** : Plonger dans tes profondeurs tout en gardant un fil vers la vie consciente.""",
        'weekly_advice': {
            'week_1': "Identifie la transformation intérieure la plus profonde qui t'appelle.",
            'week_2': "Plonge totalement dans ce processus.",
            'week_3': "Accueille ce qui meurt et ce qui naît en toi.",
            'week_4': "Intègre ta renaissance dans ta vie quotidienne."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foi intérieure**

Double feu sur la Maison 12 : ta Lune en Bélier et ton Ascendant Sagittaire explorent l'inconscient avec optimisme et foi. Tu veux trouver du sens dans ton monde intérieur, connecter ta spiritualité à une philosophie de vie inspirante.

**Domaine activé** : Maison 12 — Ton inconscient et ta spiritualité cherchent expansion et signification. Tu peux explorer différentes traditions spirituelles, voyager intérieurement, trouver une foi qui nourrit ton âme.

**Ton approche instinctive** : Le Sagittaire te fait aborder ton monde intérieur avec confiance. Tu crois en ta capacité à guérir, à grandir spirituellement. Cette foi peut être une force immense.

**Tensions possibles** : L'excès d'optimisme peut te faire éviter les vraies profondeurs. Tu risques de spiritualiser sans vraiment ressentir, de fuir la douleur par le positivisme.

**Conseil clé** : Cultiver ta foi spirituelle tout en honorant aussi l'obscurité nécessaire.""",
        'weekly_advice': {
            'week_1': "Explore une tradition spirituelle qui t'inspire.",
            'week_2': "Développe une pratique qui nourrit ta foi.",
            'week_3': "Autorise-toi aussi à douter, à ne pas savoir.",
            'week_4': "Intègre les insights spirituels dans ta philosophie de vie."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Structure intérieure**

Ta Lune en Bélier en Maison 12 veut explorer son inconscient avec courage. Ton Ascendant Capricorne apporte discipline et maîtrise : tu veux structurer ta vie intérieure, construire une spiritualité solide, gérer méthodiquement ton inconscient.

**Domaine activé** : Maison 12 — Ton inconscient et ta spiritualité deviennent un projet à long terme. Tu veux maîtriser ton monde intérieur, développer une pratique spirituelle régulière, construire ta paix intérieure avec patience.

**Ton approche instinctive** : Le Capricorne te fait aborder ton intériorité avec sérieux et discipline. Tu es prêt·e à faire le travail nécessaire, même si c'est difficile. Cette maturité spirituelle est rare.

**Tensions possibles** : Le besoin de contrôle peut bloquer le flow de l'inconscient. Tu risques de vouloir tout gérer alors que certaines choses demandent le lâcher-prise.

**Conseil clé** : Structurer ta vie intérieure tout en acceptant de perdre parfois le contrôle.""",
        'weekly_advice': {
            'week_1': "Crée une pratique spirituelle quotidienne structurée.",
            'week_2': "Tiens-toi à cette discipline même quand c'est difficile.",
            'week_3': "Autorise-toi aussi des moments de lâcher-prise total.",
            'week_4': "Mesure les fondations intérieures que tu as construites."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Libération intérieure**

Ta Lune en Bélier en Maison 12 veut transformer son inconscient. Ton Ascendant Verseau ajoute besoin de liberté et d'originalité : tu veux te libérer de tous tes conditionnements inconscients, devenir totalement libre intérieurement.

**Domaine activé** : Maison 12 — Ton inconscient et ta spiritualité cherchent libération radicale. Tu peux explorer des pratiques spirituelles alternatives, déconditionner ton mental, te libérer de l'ego.

**Ton approche instinctive** : Le Verseau te fait aborder ton monde intérieur avec détachement et innovation. Tu expérimentes avec différentes techniques, tu n'as pas peur de l'inconventionnel. Cette liberté peut être libératrice.

**Tensions possibles** : Le détachement peut devenir fuite émotionnelle. Tu risques d'intellectualiser ton inconscient au lieu de vraiment le vivre.

**Conseil clé** : Te libérer de tes chaînes intérieures tout en restant connecté·e à ton humanité.""",
        'weekly_advice': {
            'week_1': "Identifie les conditionnements inconscients dont tu veux te libérer.",
            'week_2': "Expérimente une pratique spirituelle non-conventionnelle.",
            'week_3': "Permets-toi aussi de ressentir pleinement tes émotions.",
            'week_4': "Célèbre la liberté intérieure que tu as gagnée."
        }
    },

    {
        'moon_sign': 'Aries', 'moon_house': 12, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution sacrée**

Ta Lune en Bélier en Maison 12 veut explorer courageusement son inconscient. Ton Ascendant Poissons, maître naturel de cette maison, amplifie cette dimension : tu es appelé·e à dissoudre ton ego, à te fondre dans le Tout, à vivre une expérience mystique profonde.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton lien au divin sont à leur maximum. Tu peux vivre des expériences de dissolution de soi, de fusion avec l'univers, de connexion au sacré. C'est une initiation mystique.

**Ton approche instinctive** : Le Poissons te fait vivre ton intériorité comme un océan sans fond. Tu te dissous dans tes émotions, dans le collectif, dans le divin. Cette perméabilité peut être transcendante ou désintégrante.

**Tensions possibles** : Le manque total de limites peut te faire perdre pied. Tu risques de te noyer dans l'inconscient ou de fuir la réalité par le mysticisme.

**Conseil clé** : Vivre la dissolution mystique tout en gardant un minimum d'ancrage terrestre.""",
        'weekly_advice': {
            'week_1': "Crée de l'espace pour la méditation profonde et la solitude.",
            'week_2': "Autorise-toi à lâcher complètement prise.",
            'week_3': "Vis l'expérience de dissolution de l'ego.",
            'week_4': "Reviens doucement à la terre et intègre ton expérience."
        }
    },

]

if __name__ == "__main__":
    print(f"[*] Batch complet: Aries - {len(BATCH)} interprétations")
    asyncio.run(insert_batch(BATCH))
    print(f"[✓] Aries terminé - 144/1728 (8.3%)")
