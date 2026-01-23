"""Batch complet: Cancer - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # ==================== MAISON 1 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Cœur guerrier**

Ta Lune en Cancer en Maison 1 fait de tes émotions ton identité même. Tu ressens tout intensément, ta sensibilité est à fleur de peau. L'Ascendant Bélier ajoute une couche de combativité : tu protèges férocement ton monde intérieur et ceux que tu aimes.

**Domaine activé** : Maison 1 — Ton identité personnelle est teintée d'émotionnel. Tu te présentes au monde avec ton cœur en avant, mais aussi avec une armure pour le protéger. Ta vulnérabilité devient ta force.

**Ton approche instinctive** : Avec le Bélier, tu réagis vite quand tu te sens menacé émotionnellement. Tu peux passer de la douceur maternelle à la défense agressive en un instant. Cette spontanéité protectrice te caractérise.

**Tensions possibles** : L'hypersensibilité peut te rendre réactif face aux critiques. Tu risques de surprotéger ton espace émotionnel au point de repousser les autres ou de partir en guerre pour un rien.

**Conseil clé** : Utiliser ton courage pour être vulnérable, pas pour te défendre sans cesse.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te rend vraiment vulnérable et accueille-le.",
            'week_2': "Exprime tes émotions directement sans peur du jugement.",
            'week_3': "Protège-toi intelligemment sans attaquer préventivement.",
            'week_4': "Célèbre ta capacité à être fort·e ET sensible."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Douceur enracinée**

Ta Lune en Cancer en Maison 1 fait de toi un être profondément émotionnel qui s'identifie à travers ses ressentis. L'Ascendant Taureau amplifie ce besoin de sécurité : tu veux te sentir stable dans ton corps et dans tes émotions.

**Domaine activé** : Maison 1 — Ton identité se construit autour du confort émotionnel et physique. Tu as besoin de te sentir bien dans ta peau, entouré·e de douceur et de beauté qui nourrissent ton âme.

**Ton approche instinctive** : Le Taureau te pousse à créer ton cocon de sécurité lentement, avec patience. Tu prends ton temps pour t'ouvrir aux autres, mais une fois en confiance, ta loyauté est inébranlable.

**Tensions possibles** : L'attachement excessif au confort peut te rendre résistant·e au changement. Tu risques de t'accrocher à des situations rassurantes même quand elles ne te nourrissent plus.

**Conseil clé** : Construire ta sécurité intérieure indépendamment des circonstances externes.""",
        'weekly_advice': {
            'week_1': "Crée un espace physique qui reflète ton besoin de douceur.",
            'week_2': "Nourris ton corps avec la même attention que tes émotions.",
            'week_3': "Autorise-toi à garder ce qui te réconforte vraiment.",
            'week_4': "Ancre-toi dans la gratitude pour ce qui est stable en toi."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Sentiment bavard**

Ta Lune en Cancer en Maison 1 te rend profondément émotionnel·le, tandis que l'Ascendant Gémeaux te pousse à verbaliser, analyser et partager ces émotions. Tu es un·e émotif·ve qui a besoin de mettre des mots sur tout ce qu'il ou elle ressent.

**Domaine activé** : Maison 1 — Ton identité oscille entre le ressenti profond et l'expression légère. Tu veux être compris·e émotionnellement, mais tu as aussi peur d'être trop lourd·e, alors tu intellectualises.

**Ton approche instinctive** : Le Gémeaux te fait parler de tes émotions, parfois pour les comprendre, parfois pour les évacuer. Tu cherches la connexion par la conversation, l'échange, le partage d'histoires personnelles.

**Tensions possibles** : Le mental peut devenir une fuite face à l'intensité émotionnelle. Tu risques de te disperser dans les mots au lieu de vraiment ressentir, ou d'épuiser les autres avec tes montagnes russes émotionnelles verbalisées.

**Conseil clé** : Équilibrer l'expression et le ressenti silencieux pour ne pas te perdre dans l'un ou l'autre.""",
        'weekly_advice': {
            'week_1': "Écris dans un journal pour externaliser tes émotions.",
            'week_2': "Partage tes ressentis avec quelqu'un de confiance.",
            'week_3': "Pratique aussi le silence émotionnel pour mieux sentir.",
            'week_4': "Observe comment tu utilises les mots pour gérer tes affects."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Pure émotion**

Triple Cancer : Lune en Cancer, Maison 1, Ascendant Cancer. Ce mois, tu es l'incarnation même de la sensibilité, de l'intuition, du maternel. Tes émotions sont ton identité, ton langage, ton mode d'être. C'est intense et puissant.

**Domaine activé** : Maison 1 — Ton identité personnelle est entièrement émotionnelle. Tu te présentes au monde comme un être de ressenti pur. Ta vulnérabilité est visible, ta capacité à nourrir aussi.

**Ton approche instinctive** : Triple eau : tu ressens tout avant de penser quoi que ce soit. Ton intuition est ton premier guide. Tu te protèges instinctivement quand tu sens un danger émotionnel, en te repliant dans ta carapace.

**Tensions possibles** : L'hypersensibilité peut devenir écrasante. Tu risques de te noyer dans tes propres émotions, de prendre tout personnellement, ou de te replier complètement pour te protéger.

**Conseil clé** : Honorer ta sensibilité comme un don tout en développant des frontières saines.""",
        'weekly_advice': {
            'week_1': "Accueille pleinement l'intensité de ce que tu ressens.",
            'week_2': "Pratique la protection émotionnelle sans te couper des autres.",
            'week_3': "Nourris-toi autant que tu nourris les autres.",
            'week_4': "Célèbre ta capacité unique à ressentir la vie en profondeur."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Cœur radieux**

Ta Lune en Cancer en Maison 1 te rend profondément sensible et introspectif·ve. L'Ascendant Lion ajoute une dimension de rayonnement : tu veux montrer ton cœur généreusement, briller par ta capacité à aimer et protéger.

**Domaine activé** : Maison 1 — Ton identité mêle vulnérabilité cancérienne et fierté léonine. Tu veux être reconnu·e pour ta grandeur émotionnelle, pour ta capacité à créer de la chaleur autour de toi.

**Ton approche instinctive** : Le Lion te pousse à exprimer tes émotions avec panache, à dramatiser parfois. Tu veux que ton ressenti soit vu, validé, applaudi. Cette expressivité peut être magnétique.

**Tensions possibles** : Le besoin de reconnaissance peut te rendre dépendant·e de l'attention des autres pour te sentir légitime. Tu risques d'osciller entre le repli blessé et le grand spectacle émotionnel.

**Conseil clé** : Briller par ton authenticité émotionnelle sans avoir besoin d'un public pour valider ce que tu ressens.""",
        'weekly_advice': {
            'week_1': "Montre fièrement qui tu es sans chercher l'approbation.",
            'week_2': "Crée quelque chose qui exprime ta générosité naturelle.",
            'week_3': "Rayonne tout en restant connecté·e à ta vraie sensibilité.",
            'week_4': "Célèbre ta capacité à illuminer la vie des autres."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Sensibilité utile**

Ta Lune en Cancer en Maison 1 te rend émotionnellement réceptif·ve et protecteur·rice. L'Ascendant Vierge ajoute un besoin de rendre tes émotions utiles, de les canaliser dans le service, l'aide, l'amélioration concrète.

**Domaine activé** : Maison 1 — Ton identité se construit dans la tension entre ressentir profondément et agir utilement. Tu veux que ta sensibilité serve à quelque chose, qu'elle ne soit pas juste un poids.

**Ton approche instinctive** : La Vierge te pousse à analyser tes émotions, à les trier, à les rendre productives. Tu peux devenir hypercritique de tes propres ressentis, cherchant à les "corriger" plutôt qu'à les accepter.

**Tensions possibles** : L'autocritique émotionnelle peut devenir toxique. Tu risques de te juger pour ta sensibilité, de vouloir la "réparer", ou de t'épuiser à aider les autres pour justifier tes émotions.

**Conseil clé** : Accepter que ressentir n'a pas besoin d'être utile pour être légitime.""",
        'weekly_advice': {
            'week_1': "Permets-toi de ressentir sans devoir immédiatement agir.",
            'week_2': "Canalise tes émotions dans un service authentique.",
            'week_3': "Arrête de critiquer ta sensibilité, elle est parfaite.",
            'week_4': "Trouve l'équilibre entre aider et simplement être."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie fragile**

Ta Lune en Cancer en Maison 1 te rend profondément émotionnel·le et réceptif·ve. L'Ascendant Balance ajoute un besoin d'équilibre relationnel : tu veux harmoniser tes émotions avec celles des autres, créer de la paix, de la beauté.

**Domaine activé** : Maison 1 — Ton identité se joue dans la relation. Tu existes à travers le miroir des autres, cherchant à être aimé·e, accepté·e, validé·e émotionnellement par ceux qui t'entourent.

**Ton approche instinctive** : La Balance te fait chercher l'approbation avant d'exprimer tes vrais ressentis. Tu ajustes tes émotions pour ne pas déranger, pour préserver l'harmonie. Cette diplomatie peut étouffer ton authenticité.

**Tensions possibles** : Le besoin de plaire peut te faire perdre contact avec ce que tu ressens vraiment. Tu risques de sacrifier ta vérité émotionnelle pour maintenir la paix, jusqu'à l'implosion.

**Conseil clé** : Oser exprimer tes besoins émotionnels même si cela crée une dissonance temporaire.""",
        'weekly_advice': {
            'week_1': "Identifie où tu étouffes tes émotions par politesse.",
            'week_2': "Dis ce que tu ressens vraiment, même si c'est inconfortable.",
            'week_3': "Cherche l'harmonie avec toi-même avant celle avec les autres.",
            'week_4': "Célèbre ta capacité à être authentique ET relationnel·le."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Profondeur intense**

Ta Lune en Cancer en Maison 1 te rend sensible et protecteur·rice. L'Ascendant Scorpion intensifie cette profondeur : tes émotions ne sont pas juste ressenties, elles sont vécues comme des expériences de transformation radicale.

**Domaine activé** : Maison 1 — Ton identité est celle d'un·e alchimiste émotionnel·le. Tu ne te contentes pas de ressentir, tu plonges dans les abysses, tu explores les zones d'ombre, tu transformes la douleur en pouvoir.

**Ton approche instinctive** : Le Scorpion te pousse à tout ressentir jusqu'au bout, sans compromis. Tu ne fuis pas l'intensité, tu la cherches. Cette puissance émotionnelle peut être magnétique ou effrayante pour les autres.

**Tensions possibles** : L'intensité constante peut être épuisante. Tu risques de créer des crises pour sentir que tu vis vraiment, ou de te noyer dans des émotions trop lourdes à porter seul·e.

**Conseil clé** : Vivre l'intensité sans s'y perdre, transformer sans se détruire.""",
        'weekly_advice': {
            'week_1': "Plonge dans une émotion que tu as évitée récemment.",
            'week_2': "Utilise cette intensité pour transformer quelque chose.",
            'week_3': "Protège-toi de l'épuisement émotionnel par des pauses.",
            'week_4': "Intègre ce que tu as découvert dans tes profondeurs."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventure émotive**

Ta Lune en Cancer en Maison 1 te rend profondément attaché·e au foyer, à la sécurité émotionnelle. L'Ascendant Sagittaire crée une tension : tu veux explorer le monde, t'envoler, tout en gardant ton port d'attache bien ancré.

**Domaine activé** : Maison 1 — Ton identité oscille entre le besoin de racines et celui d'ailes. Tu veux te sentir libre d'explorer tout en gardant un cocon sûr où revenir. Cette dualité te définit.

**Ton approche instinctive** : Le Sagittaire te pousse à donner du sens à tes émotions, à les transformer en philosophie, en quête de vérité. Tu cherches l'expansion là où Cancer cherche la protection.

**Tensions possibles** : Le conflit entre attachement et liberté peut te déchirer. Tu risques de fuir les engagements émotionnels par peur d'être piégé·e, ou de t'accrocher trop fort quand tu t'autorises à t'attacher.

**Conseil clé** : Comprendre que la vraie liberté inclut la capacité de s'attacher sans peur.""",
        'weekly_advice': {
            'week_1': "Explore de nouveaux horizons tout en restant ancré·e.",
            'week_2': "Donne du sens à tes émotions plutôt que de les fuir.",
            'week_3': "Autorise-toi l'aventure ET la sécurité émotionnelle.",
            'week_4': "Célèbre ta capacité unique à être enraciné·e ET libre."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Cœur structuré**

Ta Lune en Cancer en Maison 1 te rend émotionnellement sensible et réceptif·ve. L'Ascendant Capricorne oppose son sérieux : tu veux contrôler tes émotions, les rendre productives, ne pas paraître faible ou trop vulnérable.

**Domaine activé** : Maison 1 — Ton identité se construit dans la tension entre vulnérabilité et maîtrise. Tu ressens intensément mais tu te montres fort·e. Cette dualité peut être ta plus grande force ou ta plus grande prison.

**Ton approche instinctive** : Le Capricorne te pousse à construire une structure autour de tes émotions, à les gérer comme un projet. Tu peux paraître froid·e alors que tu es profondément sensible, juste protégé·e.

**Tensions possibles** : Le refoulement émotionnel peut créer une pression interne énorme. Tu risques de t'épuiser à paraître fort·e, ou de te couper de ta sensibilité naturelle pour réussir.

**Conseil clé** : Accepter que montrer ta vulnérabilité est aussi une forme de force et de maturité.""",
        'weekly_advice': {
            'week_1': "Permets-toi de ressentir sans devoir immédiatement contrôler.",
            'week_2': "Montre-toi vulnérable à quelqu'un de confiance.",
            'week_3': "Utilise ta sensibilité comme un atout, pas un fardeau.",
            'week_4': "Construis une vie qui honore autant ton cœur que tes ambitions."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Sentiment universel**

Ta Lune en Cancer en Maison 1 te rend profondément personnel·le et émotionnel·le. L'Ascendant Verseau crée un paradoxe : tu veux te détacher, intellectualiser, universaliser ce qui est intime et particulier en toi.

**Domaine activé** : Maison 1 — Ton identité oscille entre le besoin de connexion profonde et celui de liberté individuelle. Tu veux appartenir à une famille, une tribu, tout en restant unique, libre, différent·e.

**Ton approche instinctive** : Le Verseau te fait prendre de la distance avec tes propres émotions pour les observer objectivement. Cette froideur apparente peut protéger ta sensibilité mais aussi t'en couper.

**Tensions possibles** : Le conflit entre attachement émotionnel et détachement intellectuel peut créer une confusion identitaire. Tu risques de te sentir incompris·e, trop bizarre pour être normal·e, trop sensible pour être libre.

**Conseil clé** : Embrasser ton originalité émotionnelle comme une force, pas une contradiction.""",
        'weekly_advice': {
            'week_1': "Honore ta sensibilité même si elle semble en contradiction avec ton indépendance.",
            'week_2': "Trouve une communauté qui accepte ta complexité.",
            'week_3': "Utilise ton recul pour comprendre sans fuir tes émotions.",
            'week_4': "Célèbre ton mélange unique de cœur et d'esprit libre."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Océan intérieur**

Ta Lune en Cancer en Maison 1 te rend profondément sensible et protecteur·rice. L'Ascendant Poissons dissout toutes les frontières : tu es une éponge émotionnelle, ressentant tout ce qui t'entoure comme si c'était tien.

**Domaine activé** : Maison 1 — Ton identité est fluide, perméable, changeante comme les marées. Tu n'as pas de carapace solide, tu es pure sensibilité, pure réceptivité. C'est à la fois un don et un défi immense.

**Ton approche instinctive** : Le Poissons amplifie ta nature cancérienne jusqu'à la fusion totale. Tu te perds dans les émotions des autres, tu ressens leur douleur comme la tienne. Cette empathie extrême peut être transcendante ou épuisante.

**Tensions possibles** : Le manque de limites peut te faire perdre ton identité propre. Tu risques de te noyer dans les besoins des autres, de ne plus savoir ce qui est à toi et ce qui vient d'ailleurs.

**Conseil clé** : Développer des frontières psychiques saines pour protéger ton immense sensibilité.""",
        'weekly_advice': {
            'week_1': "Crée un espace sacré où tu peux te retirer seul·e.",
            'week_2': "Pratique la distinction entre tes émotions et celles des autres.",
            'week_3': "Nourris ta spiritualité pour donner sens à ta sensibilité.",
            'week_4': "Honore ton besoin de solitude et de silence émotionnel."
        }
    },

    # ==================== MAISON 2 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Sécurité combative**

Ta Lune en Cancer en Maison 2 lie tes émotions à ta sécurité matérielle. Tu as besoin de te sentir protégé·e financièrement pour être bien émotionnellement. L'Ascendant Bélier ajoute une urgence : tu veux conquérir cette sécurité rapidement.

**Domaine activé** : Maison 2 — Tes ressources, tes possessions, ton sentiment de valeur personnelle sont teintés d'émotion. Tu investis ton cœur dans ce qui t'appartient, créant un attachement fort.

**Ton approche instinctive** : Le Bélier te pousse à agir impulsivement pour sécuriser tes ressources. Tu peux être généreux·se quand tu te sens en sécurité, mais féroce dans la protection de ce qui est à toi.

**Tensions possibles** : L'impulsivité financière peut compromettre ta sécurité à long terme. Tu risques d'alterner entre accumulation protectrice et dépenses émotionnelles irréfléchies.

**Conseil clé** : Construire ta sécurité avec courage mais aussi avec patience et stratégie.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te fait vraiment te sentir en sécurité matériellement.",
            'week_2': "Prends une initiative pour améliorer ta situation financière.",
            'week_3': "Résiste à l'impulsion de dépenser pour combler un vide émotionnel.",
            'week_4': "Ancre-toi dans la gratitude pour ce que tu possèdes déjà."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Richesse nourricière**

Ta Lune en Cancer en Maison 2 cherche la sécurité émotionnelle à travers la sécurité matérielle. L'Ascendant Taureau, maître naturel de cette maison, amplifie ce besoin : tu veux accumuler, protéger, créer un cocon d'abondance.

**Domaine activé** : Maison 2 — Double terre-eau sur les ressources : tu construis lentement mais sûrement ta sécurité. La beauté, le confort, la qualité deviennent des besoins émotionnels, pas juste matériels.

**Ton approche instinctive** : Le Taureau te donne la patience et la constance pour bâtir ta sécurité pierre par pierre. Tu investis dans le durable, dans ce qui nourrit vraiment, dans ce qui te réconforte profondément.

**Tensions possibles** : L'attachement excessif aux possessions peut devenir toxique. Tu risques de confondre sécurité matérielle et sécurité émotionnelle, accumulant sans fin sans jamais te sentir satisfait·e.

**Conseil clé** : Cultiver la sécurité intérieure indépendamment de ce que tu possèdes.""",
        'weekly_advice': {
            'week_1': "Investis dans quelque chose de durable et réconfortant.",
            'week_2': "Crée un environnement qui nourrit tous tes sens.",
            'week_3': "Pratique la générosité pour assouplir ton attachement.",
            'week_4': "Savoure l'abondance que tu as déjà créée autour de toi."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Valeur changeante**

Ta Lune en Cancer en Maison 2 cherche la sécurité matérielle comme un ancrage émotionnel. L'Ascendant Gémeaux crée une variabilité : tes besoins financiers changent selon ton humeur, tes intérêts fluctuent, ton rapport à l'argent est intellectualisé.

**Domaine activé** : Maison 2 — Tes ressources sont un terrain d'exploration mentale et émotionnelle. Tu penses beaucoup à l'argent, tu en parles, tu lis dessus, mais l'action concrète peut être dispersée.

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre différentes sources de revenus ou façons de gérer tes ressources. Tu es curieux·se, adaptable, mais peut-être pas assez ancré·e pour construire solidement.

**Tensions possibles** : La dispersion mentale peut nuire à ta stabilité financière. Tu risques de multiplier les projets sans en finaliser aucun, ou de dépenser impulsivement selon tes humeurs changeantes.

**Conseil clé** : Choisir quelques sources de valeur stables et s'y tenir malgré la tentation de la nouveauté.""",
        'weekly_advice': {
            'week_1': "Simplifie tes finances pour plus de clarté mentale.",
            'week_2': "Apprends quelque chose de nouveau sur la gestion d'argent.",
            'week_3': "Engage-toi sur un projet financier concret et tiens-y.",
            'week_4': "Observe tes patterns de dépense émotionnelle et ajuste."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Nid précieux**

Triple Cancer en Maison 2 : ta sécurité matérielle EST ta sécurité émotionnelle. Tu ne peux pas séparer les deux. Ton foyer, tes possessions, tes ressources sont des extensions de ton monde intérieur, chargées d'affect et de mémoire.

**Domaine activé** : Maison 2 — Chaque objet que tu possèdes porte une histoire, une émotion, un souvenir. Tu n'accumules pas juste des choses, tu accumules des morceaux de toi-même, des preuves tangibles d'amour et de sécurité.

**Ton approche instinctive** : Triple eau sur les ressources : tu investis émotionnellement dans tout ce qui t'appartient. La générosité envers ceux que tu aimes est sans limites quand tu te sens en sécurité.

**Tensions possibles** : L'attachement émotionnel aux objets peut devenir paralysant. Tu risques de ne rien pouvoir jeter, de t'accrocher au passé matérialisé, ou de dépendre de tes possessions pour te sentir entier·e.

**Conseil clé** : Apprendre que la vraie sécurité vient de l'intérieur, pas de ce que tu accumules.""",
        'weekly_advice': {
            'week_1': "Trie tes possessions et garde seulement ce qui te nourrit vraiment.",
            'week_2': "Crée un autel ou espace sacré avec tes objets les plus chers.",
            'week_3': "Pratique le détachement en donnant quelque chose de précieux.",
            'week_4': "Ancre-toi dans la gratitude pour l'abondance émotionnelle."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Générosité royale**

Ta Lune en Cancer en Maison 2 cherche la sécurité matérielle comme un cocon émotionnel. L'Ascendant Lion ajoute une dimension de grandeur : tu veux non seulement la sécurité, mais aussi la beauté, le luxe, la capacité de donner généreusement.

**Domaine activé** : Maison 2 — Tes ressources sont un moyen d'exprimer ton cœur généreux. Tu veux pouvoir offrir, gâter, créer de la beauté et du confort pour toi et ceux que tu aimes. L'argent devient un outil d'amour.

**Ton approche instinctive** : Le Lion te pousse à être fier·ère de ce que tu possèdes et généreux·se dans le partage. Tu peux être royal·e dans tes dépenses, cherchant la qualité et l'impact émotionnel.

**Tensions possibles** : La générosité peut devenir excessive et compromettre ta sécurité. Tu risques de dépenser pour impressionner ou pour acheter l'affection, ou de te sentir diminué·e si tu ne peux pas offrir.

**Conseil clé** : Donner de ton cœur plutôt que de ton porte-monnaie, comprendre que ta valeur ne dépend pas de ta capacité à gâter.""",
        'weekly_advice': {
            'week_1': "Investis dans quelque chose de beau qui te fait te sentir royal·e.",
            'week_2': "Offre de la générosité authentique sans attendre de retour.",
            'week_3': "Équilibre ton besoin de donner et ton besoin de sécurité.",
            'week_4': "Célèbre ta richesse intérieure indépendamment du matériel."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Économie prudente**

Ta Lune en Cancer en Maison 2 cherche la sécurité émotionnelle à travers la sécurité matérielle. L'Ascendant Vierge ajoute un souci du détail : tu veux gérer tes ressources intelligemment, efficacement, avec une attention méticuleuse.

**Domaine activé** : Maison 2 — Tes finances deviennent un terrain d'organisation et de contrôle. Tu analyses chaque dépense, tu optimises, tu cherches la perfection dans ta gestion. Cette vigilance peut être rassurante ou anxiogène.

**Ton approche instinctive** : La Vierge te fait budgéter, planifier, anticiper chaque besoin. Tu es prudent·e, peut-être trop, cherchant la sécurité absolue à travers le contrôle total de tes ressources.

**Tensions possibles** : L'anxiété financière peut devenir obsessionnelle. Tu risques de te priver excessivement par peur du manque, ou de te critiquer pour chaque "erreur" de gestion.

**Conseil clé** : Trouver l'équilibre entre prudence saine et confiance dans l'abondance de la vie.""",
        'weekly_advice': {
            'week_1': "Crée un budget clair qui te rassure sans te priver.",
            'week_2': "Investis dans des outils ou formations pour mieux gérer tes ressources.",
            'week_3': "Autorise-toi une petite dépense plaisir sans culpabilité.",
            'week_4': "Observe ton anxiété financière et travaille à la détendre."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Beauté partagée**

Ta Lune en Cancer en Maison 2 cherche la sécurité matérielle pour nourrir son besoin de cocon. L'Ascendant Balance ajoute une dimension esthétique et relationnelle : tu veux que tes ressources créent de la beauté et de l'harmonie.

**Domaine activé** : Maison 2 — Tes possessions doivent être belles, équilibrées, partagées. Tu investis dans ce qui embellit ta vie et celle des autres. L'argent devient un moyen de créer du lien et de l'harmonie.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre dans tes finances, partager généreusement, investir dans les relations. Tu peux dépenser pour maintenir l'harmonie ou pour plaire.

**Tensions possibles** : Le besoin de plaire peut te faire dépenser au-delà de tes moyens. Tu risques de sacrifier ta sécurité pour ne pas paraître radin·e, ou de dépendre financièrement des autres.

**Conseil clé** : Construire ta sécurité personnelle avant de la partager, honorer tes besoins financiers autant que ceux des autres.""",
        'weekly_advice': {
            'week_1': "Identifie où tu sacrifies ta sécurité pour plaire aux autres.",
            'week_2': "Investis dans la beauté qui te nourrit vraiment, toi.",
            'week_3': "Pratique dire non aux demandes financières qui te fragilisent.",
            'week_4': "Célèbre l'équilibre entre générosité et auto-protection."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir caché**

Ta Lune en Cancer en Maison 2 cherche la sécurité émotionnelle à travers la sécurité matérielle. L'Ascendant Scorpion intensifie cette quête : tes ressources deviennent une question de pouvoir, de contrôle, de transformation profonde.

**Domaine activé** : Maison 2 — L'argent et les possessions sont chargés de signification émotionnelle intense. Tu peux garder tes ressources secrètes, les utiliser comme levier de pouvoir, ou les transformer radicalement.

**Ton approche instinctive** : Le Scorpion te pousse à tout ou rien : soit tu accumules obsessionnellement pour te sentir puissant·e, soit tu lâches tout dans un acte de transformation. Le contrôle des ressources égale contrôle de ta vie.

**Tensions possibles** : L'obsession du contrôle financier peut créer de la paranoïa. Tu risques de garder des secrets toxiques sur l'argent, de manipuler par les ressources, ou de détruire ta sécurité dans une crise.

**Conseil clé** : Utiliser ton pouvoir financier pour te transformer positivement, pas pour contrôler ou te protéger de fantômes.""",
        'weekly_advice': {
            'week_1': "Examine tes croyances profondes sur l'argent et le pouvoir.",
            'week_2': "Transforme une habitude financière toxique en habitude saine.",
            'week_3': "Partage un secret financier avec quelqu'un de confiance.",
            'week_4': "Libère-toi d'un attachement matériel qui te limite."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Abondance nomade**

Ta Lune en Cancer en Maison 2 cherche la sécurité matérielle comme un ancrage. L'Ascendant Sagittaire crée un paradoxe : tu veux la sécurité mais aussi la liberté de voyager, d'explorer, de ne pas être attaché·e par les possessions.

**Domaine activé** : Maison 2 — Tes ressources doivent servir ton expansion, pas t'enchaîner. Tu investis dans ce qui te permet de grandir, d'apprendre, de découvrir le monde. La richesse est un moyen, pas une fin.

**Ton approche instinctive** : Le Sagittaire te fait être généreux·se et optimiste avec l'argent. Tu crois en l'abondance de l'univers, parfois au point de négliger la gestion concrète de tes ressources.

**Tensions possibles** : Le conflit entre besoin de sécurité et désir de liberté peut créer de l'instabilité. Tu risques de dépenser pour des expériences au détriment de la construction solide, ou de te sentir piégé·e par tes responsabilités financières.

**Conseil clé** : Créer une sécurité mobile qui te permet à la fois l'ancrage et l'aventure.""",
        'weekly_advice': {
            'week_1': "Investis dans des expériences enrichissantes plutôt que des objets.",
            'week_2': "Crée un coussin de sécurité qui finance ta liberté.",
            'week_3': "Équilibre ton optimisme financier avec du réalisme.",
            'week_4': "Célèbre ta capacité unique à être libre ET en sécurité."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Patrimoine émotionnel**

Ta Lune en Cancer en Maison 2 cherche la sécurité émotionnelle à travers la sécurité matérielle. L'Ascendant Capricorne, signe opposé au Cancer, crée une tension productive : tu construis méthodiquement un patrimoine qui nourrit ton besoin de protection.

**Domaine activé** : Maison 2 — Axe Cancer-Capricorne sur les ressources : tu as à la fois le besoin émotionnel de sécurité et la discipline pour la construire. Cette combinaison peut créer une vraie abondance durable.

**Ton approche instinctive** : Le Capricorne te donne la patience et l'ambition pour bâtir solidement. Tu investis à long terme, tu planifies, tu crées un héritage. Mais tu dois aussi nourrir ton besoin émotionnel de confort immédiat.

**Tensions possibles** : Le sacrifice du présent pour le futur peut créer de la frustration émotionnelle. Tu risques de trop te priver, de devenir rigide, ou de confondre richesse matérielle et richesse émotionnelle.

**Conseil clé** : Construire ta sécurité sans oublier de vivre et de profiter dans le présent.""",
        'weekly_advice': {
            'week_1': "Pose un objectif financier à long terme et commence à y travailler.",
            'week_2': "Investis dans quelque chose de durable qui te rapproche de tes buts.",
            'week_3': "Autorise-toi un plaisir immédiat sans culpabilité.",
            'week_4': "Célèbre le chemin parcouru vers ta sécurité matérielle."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Valeur collective**

Ta Lune en Cancer en Maison 2 cherche la sécurité personnelle et familiale à travers les ressources. L'Ascendant Verseau universalise ce besoin : tu veux partager l'abondance, créer des systèmes communautaires, révolutionner le rapport à l'argent.

**Domaine activé** : Maison 2 — Tes ressources sont un terrain d'expérimentation sociale. Tu peux rejeter le modèle traditionnel d'accumulation, chercher des alternatives, investir dans le collectif plutôt que le personnel.

**Ton approche instinctive** : Le Verseau te fait intellectualiser tes besoins matériels, les détacher de l'émotion. Tu peux être brillant·e dans la gestion financière innovante, mais distant·e de tes vrais besoins émotionnels.

**Tensions possibles** : Le conflit entre sécurité personnelle et idéaux collectifs peut créer de l'instabilité. Tu risques de sacrifier ta sécurité pour une cause, ou de te sentir coupable d'avoir des besoins matériels "égoïstes".

**Conseil clé** : Honorer ton besoin de sécurité personnelle tout en contribuant au bien collectif.""",
        'weekly_advice': {
            'week_1': "Explore des modèles financiers alternatifs qui te parlent.",
            'week_2': "Investis dans un projet communautaire ou coopératif.",
            'week_3': "Respecte tes besoins de sécurité sans te sentir coupable.",
            'week_4': "Trouve l'équilibre entre ton bien-être et celui du collectif."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Abondance fluide**

Ta Lune en Cancer en Maison 2 cherche la sécurité matérielle comme un cocon protecteur. L'Ascendant Poissons dissout les frontières : l'argent devient fluide, spirituel, difficile à retenir. Tu donnes généreusement, parfois à ton détriment.

**Domaine activé** : Maison 2 — Double eau sur les ressources : tu as une relation émotionnelle et spirituelle à l'argent. Les possessions matérielles ont une charge symbolique forte, mais tu peux aussi les considérer comme transitoires.

**Ton approche instinctive** : Le Poissons te fait donner sans compter, croire en la providence, lâcher prise sur le contrôle matériel. Cette foi peut créer de l'abondance ou de la précarité selon ton niveau de conscience.

**Tensions possibles** : Le manque de limites peut compromettre ta sécurité matérielle. Tu risques de te faire exploiter financièrement, de donner plus que tu ne peux, ou de fuir dans le déni face aux problèmes d'argent.

**Conseil clé** : Développer des frontières financières claires tout en gardant ton cœur généreux.""",
        'weekly_advice': {
            'week_1': "Établis des limites claires sur ce que tu peux donner.",
            'week_2': "Nourris ta spiritualité sans négliger le matériel.",
            'week_3': "Fais face à une réalité financière que tu évitais.",
            'week_4': "Célèbre ta capacité unique à allier foi et sécurité."
        }
    },

    # ==================== MAISON 3 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Parole protectrice**

Ta Lune en Cancer en Maison 3 teinte ta communication d'émotion et de sensibilité. Tu parles avec ton cœur, tu cherches la connexion intime dans l'échange. L'Ascendant Bélier ajoute de la spontanéité : tu exprimes tes émotions sans filtre, directement.

**Domaine activé** : Maison 3 — Ta communication, tes apprentissages, tes relations de proximité sont chargés d'affect. Tu veux te sentir entendu·e et compris·e émotionnellement. Tes mots peuvent guérir ou blesser profondément.

**Ton approche instinctive** : Le Bélier te fait parler vite, réagir impulsivement, dire ce que tu ressens au moment où tu le ressens. Cette authenticité brute peut être rafraîchissante ou maladroite.

**Tensions possibles** : L'impulsivité verbale peut blesser sans le vouloir. Tu risques de regretter des mots trop directs, ou de te sentir incompris·e quand ta sensibilité s'exprime avec agressivité.

**Conseil clé** : Utiliser ta spontanéité pour exprimer ta vulnérabilité authentiquement, pas pour attaquer quand tu te sens menacé·e.""",
        'weekly_advice': {
            'week_1': "Exprime une émotion importante que tu as gardée pour toi.",
            'week_2': "Écoute vraiment quelqu'un sans préparer ta réponse.",
            'week_3': "Trouve les mots justes pour dire ce que tu ressens.",
            'week_4': "Célèbre ta capacité à communiquer avec authenticité."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Dialogue ancré**

Ta Lune en Cancer en Maison 3 rend ta communication émotionnelle et protectrice. L'Ascendant Taureau ajoute de la lenteur et de la profondeur : tu prends ton temps pour t'exprimer, tu choisis tes mots avec soin, tu privilégies la qualité à la quantité.

**Domaine activé** : Maison 3 — Tes échanges ont besoin de douceur, de constance, de confort. Tu crées des rituels de communication avec tes proches, des habitudes rassurantes qui nourrissent le lien.

**Ton approche instinctive** : Le Taureau te fait chercher la stabilité dans tes relations de proximité. Tu es loyal·e dans tes amitiés, patient·e dans tes apprentissages, fidèle à tes habitudes mentales.

**Tensions possibles** : La résistance au changement peut limiter ta croissance intellectuelle. Tu risques de rester dans des schémas de communication familiers même s'ils ne servent plus, ou de refuser d'apprendre de nouvelles choses.

**Conseil clé** : Garder ta profondeur tout en restant ouvert·e à de nouvelles façons de penser et communiquer.""",
        'weekly_advice': {
            'week_1': "Crée un rituel de communication avec un·e proche.",
            'week_2': "Apprends quelque chose de nouveau à ton rythme.",
            'week_3': "Exprime-toi avec authenticité même si c'est inconfortable.",
            'week_4': "Savoure la qualité de tes connexions proches."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Cœur bavard**

Ta Lune en Cancer en Maison 3 rend ta communication émotionnellement riche. L'Ascendant Gémeaux, maître naturel de cette maison, amplifie le besoin de parler, d'échanger, de partager : tu verbalises tes émotions pour les comprendre et te connecter.

**Domaine activé** : Maison 3 — Double énergie mercurienne : tu penses avec ton cœur, tu ressens avec ton mental. Tes apprentissages sont teintés d'émotion, tes relations fraternelles profondément importantes.

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre les sujets, les conversations, les connexions. Tu as besoin de variété intellectuelle et affective. Tu peux parler pendant des heures de ce que tu ressens.

**Tensions possibles** : La dispersion mentale peut t'empêcher d'approfondir vraiment. Tu risques de fuir l'intensité émotionnelle par le bavardage, ou d'épuiser les autres avec tes analyses infinies de tes ressentis.

**Conseil clé** : Équilibrer l'expression verbale et le silence ressenti pour vraiment intégrer tes émotions.""",
        'weekly_advice': {
            'week_1': "Écris chaque jour ce que tu ressens pour clarifier tes émotions.",
            'week_2': "Engage une conversation profonde avec quelqu'un de proche.",
            'week_3': "Pratique le silence émotionnel pour mieux sentir.",
            'week_4': "Célèbre ta capacité unique à mettre des mots sur l'indicible."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Intimité partagée**

Triple Cancer en Maison 3 : ta communication est pure émotion, pure sensibilité. Tu ne peux pas séparer ce que tu penses de ce que tu ressens. Chaque conversation devient une opportunité de connexion profonde ou une source de vulnérabilité.

**Domaine activé** : Maison 3 — Tes échanges quotidiens, tes apprentissages, tes relations de proximité sont ton terrain émotionnel principal. Tu as besoin de te sentir en sécurité pour t'exprimer librement.

**Ton approche instinctive** : Triple eau sur la communication : tu cherches l'intimité dans chaque échange. Les conversations superficielles te laissent vide. Tu veux toucher le cœur ou ne rien dire du tout.

**Tensions possibles** : L'hypersensibilité peut rendre la communication douloureuse. Tu risques de prendre tout personnellement, de te replier face à une remarque anodine, ou de sur-interpréter les intentions des autres.

**Conseil clé** : Développer une carapace légère qui protège sans isoler, communiquer ta sensibilité sans en faire un fardeau.""",
        'weekly_advice': {
            'week_1': "Choisis avec qui tu partages ta vulnérabilité.",
            'week_2': "Exprime tes besoins émotionnels clairement et directement.",
            'week_3': "Pratique de ne pas prendre personnellement ce qui n'est pas personnel.",
            'week_4': "Célèbre la profondeur de tes connexions intimes."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Expression rayonnante**

Ta Lune en Cancer en Maison 3 rend ta communication émotionnelle et protectrice. L'Ascendant Lion ajoute du rayonnement : tu veux que tes mots touchent, inspirent, qu'on se souvienne de ce que tu dis. Tu communiques avec le cœur et avec panache.

**Domaine activé** : Maison 3 — Ta voix, tes mots, tes idées deviennent des moyens d'expression créative et généreuse. Tu veux partager ton cœur avec chaleur et être apprécié·e pour ton authenticité.

**Ton approche instinctive** : Le Lion te pousse à dramatiser un peu, à rendre tes histoires captivantes, à chercher l'impact émotionnel dans tes échanges. Tu es un·e conteur·se naturel·le qui veut émouvoir.

**Tensions possibles** : Le besoin de reconnaissance peut te faire exagérer ou manipuler émotionnellement. Tu risques de transformer chaque conversation en spectacle, ou de te sentir rejeté·e si on ne réagit pas assez fort à tes mots.

**Conseil clé** : Communiquer authentiquement sans avoir besoin d'une audience pour valider ce que tu ressens.""",
        'weekly_advice': {
            'week_1': "Raconte une histoire personnelle qui a du sens pour toi.",
            'week_2': "Exprime ta créativité à travers l'écriture ou la parole.",
            'week_3': "Écoute autant que tu parles pour équilibrer l'échange.",
            'week_4': "Célèbre ta capacité unique à toucher les cœurs par tes mots."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Soin verbal**

Ta Lune en Cancer en Maison 3 rend ta communication chargée d'émotion et d'empathie. L'Ascendant Vierge ajoute de la précision : tu veux que tes mots soient justes, utiles, qu'ils aident vraiment. Tu communiques pour soigner, pour servir.

**Domaine activé** : Maison 3 — Tes échanges quotidiens deviennent des opportunités de service. Tu écoutes attentivement, tu donnes des conseils pratiques, tu analyses les émotions avec soin.

**Ton approche instinctive** : La Vierge te fait chercher le mot parfait, la formulation exacte qui va aider l'autre. Tu peux devenir hypercritique de ta propre communication, retravaillant mentalement chaque phrase.

**Tensions possibles** : L'autocritique verbale peut t'empêcher de t'exprimer spontanément. Tu risques de sur-analyser tes émotions au lieu de les vivre, ou de donner des conseils non sollicités par besoin de te sentir utile.

**Conseil clé** : Accepter que la communication émotionnelle n'a pas besoin d'être parfaite pour être valide.""",
        'weekly_advice': {
            'week_1': "Exprime-toi sans retoucher mentalement chaque phrase.",
            'week_2': "Offre ton aide verbale seulement quand c'est demandé.",
            'week_3': "Pratique l'écoute sans analyser ni chercher à réparer.",
            'week_4': "Célèbre ta capacité à communiquer avec précision et soin."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomatie tendre**

Ta Lune en Cancer en Maison 3 rend ta communication profondément émotionnelle. L'Ascendant Balance ajoute un besoin d'harmonie : tu veux que tes mots créent du lien, apaisent, équilibrent. Tu es un·e médiateur·rice naturel·le.

**Domaine activé** : Maison 3 — Tes échanges cherchent la beauté, l'équilibre, la justice relationnelle. Tu choisis tes mots pour maintenir la paix, parfois au détriment de ta vérité émotionnelle.

**Ton approche instinctive** : La Balance te fait chercher le consensus dans chaque conversation. Tu écoutes tous les points de vue, tu modères, tu cherches l'équité. Cette diplomatie peut étouffer ton authenticité.

**Tensions possibles** : Le besoin de plaire peut te faire taire tes vrais ressentis. Tu risques de perdre ta voix émotionnelle en cherchant toujours à ne pas déranger, ou de te sentir incompris·e sous ta politesse.

**Conseil clé** : Oser dire ta vérité émotionnelle même si elle crée une dissonance, tout en gardant ta douceur naturelle.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te censures pour maintenir la paix.",
            'week_2': "Exprime un désaccord avec douceur mais fermeté.",
            'week_3': "Équilibre l'écoute des autres avec l'expression de toi.",
            'week_4': "Célèbre ta capacité à être authentique ET harmonieux·se."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Parole intense**

Ta Lune en Cancer en Maison 3 rend ta communication émotionnellement riche. L'Ascendant Scorpion intensifie chaque mot : tu ne parles pas pour parler, tu veux toucher les profondeurs, révéler les vérités cachées, transformer par la parole.

**Domaine activé** : Maison 3 — Tes échanges quotidiens deviennent des opportunités de plongée psychologique. Tu poses les questions que personne n'ose poser, tu dis ce que tout le monde pense en silence.

**Ton approche instinctive** : Le Scorpion te fait communiquer avec intensité et stratégie. Tu observes, tu décodes, tu gardes des secrets. Quand tu parles, c'est pour un impact maximum, pas pour remplir le silence.

**Tensions possibles** : L'intensité peut être épuisante pour les autres. Tu risques de manipuler par les mots, de sonder trop profond trop vite, ou de créer du drame dans des échanges simples.

**Conseil clé** : Doser ton intensité communicationnelle selon le contexte, tout en gardant ta profondeur.""",
        'weekly_advice': {
            'week_1': "Engage une conversation profonde qui te fait peur.",
            'week_2': "Partage un secret ou une vérité cachée.",
            'week_3': "Pratique la légèreté dans l'échange sans perdre ta profondeur.",
            'week_4': "Célèbre ta capacité à transformer par tes mots."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Enseignement chaleureux**

Ta Lune en Cancer en Maison 3 rend ta communication émotionnelle et protectrice. L'Ascendant Sagittaire ajoute de l'expansion : tu veux partager tes émotions comme des enseignements, donner du sens à ton vécu, inspirer par tes histoires.

**Domaine activé** : Maison 3 — Tes échanges quotidiens deviennent des opportunités de croissance. Tu apprends et enseignes constamment, transformant chaque expérience émotionnelle en sagesse à transmettre.

**Ton approche instinctive** : Le Sagittaire te fait communiquer avec optimisme et générosité. Tu veux élever, inspirer, donner de l'espoir. Tes histoires personnelles deviennent des paraboles universelles.

**Tensions possibles** : Le besoin de donner du sens peut te faire éviter les émotions brutes. Tu risques de philosopher sur ce que tu ressens au lieu de le vivre, ou de prêcher au lieu d'écouter.

**Conseil clé** : Équilibrer le partage de sagesse et l'écoute humble, l'enseignement et l'apprentissage.""",
        'weekly_advice': {
            'week_1': "Partage une leçon apprise de ton expérience émotionnelle.",
            'week_2': "Apprends quelque chose de nouveau qui élargit ta vision.",
            'week_3': "Écoute vraiment sans chercher à enseigner.",
            'week_4': "Célèbre ta capacité à transformer l'émotion en sagesse."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Structure sensible**

Ta Lune en Cancer en Maison 3 rend ta communication émotionnelle et intuitive. L'Ascendant Capricorne ajoute de la retenue : tu contrôles ce que tu exprimes, tu structures tes émotions avant de les partager, tu veux paraître maître·sse de toi.

**Domaine activé** : Maison 3 — Axe Cancer-Capricorne sur la communication : tu ressens profondément mais tu t'exprimes avec prudence. Tu construis ta réputation sur ta fiabilité verbale.

**Ton approche instinctive** : Le Capricorne te fait peser chaque mot, anticiper l'impact de ce que tu dis. Tu es sérieux·se dans tes échanges, cherchant l'utilité et la crédibilité plutôt que la connexion émotionnelle immédiate.

**Tensions possibles** : Le refoulement verbal peut créer une distance avec les autres. Tu risques de paraître froid·e alors que tu es profondément sensible, ou de te couper de ta spontanéité émotionnelle.

**Conseil clé** : Autoriser ta vulnérabilité à s'exprimer tout en gardant ta sagesse et ta retenue quand nécessaire.""",
        'weekly_advice': {
            'week_1': "Partage une émotion que tu as l'habitude de contrôler.",
            'week_2': "Structure ta pensée sans étouffer ton ressenti.",
            'week_3': "Trouve l'équilibre entre fiabilité et authenticité.",
            'week_4': "Célèbre ta capacité à être sensible ET crédible."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Échange universel**

Ta Lune en Cancer en Maison 3 rend ta communication profondément personnelle et émotionnelle. L'Ascendant Verseau universalise : tu veux partager tes émotions comme des vérités humaines, créer des ponts entre ton vécu intime et l'expérience collective.

**Domaine activé** : Maison 3 — Tes échanges oscillent entre l'intimité cancérienne et la distance verseau. Tu intellectualises tes émotions pour les rendre partageables, les transformer en concepts.

**Ton approche instinctive** : Le Verseau te fait communiquer de manière originale, parfois détachée. Tu peux parler de sujets très personnels avec une objectivité déconcertante, ou apporter des idées révolutionnaires dans l'échange quotidien.

**Tensions possibles** : Le détachement peut te couper de ton ressenti réel. Tu risques de fuir l'intimité émotionnelle par l'abstraction intellectuelle, ou de te sentir incompris·e dans ta complexité.

**Conseil clé** : Honorer à la fois ton besoin de connexion intime et ton besoin de liberté intellectuelle dans la communication.""",
        'weekly_advice': {
            'week_1': "Partage une émotion personnelle sans l'intellectualiser.",
            'week_2': "Explore des idées nouvelles sur la façon de communiquer.",
            'week_3': "Trouve une communauté qui comprend ta complexité.",
            'week_4': "Célèbre ton mélange unique de cœur et d'esprit libre."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Poésie fluide**

Ta Lune en Cancer en Maison 3 rend ta communication émotionnellement riche et intuitive. L'Ascendant Poissons dissout les mots : tu communiques autant par le silence, le ressenti, l'énergie que par le langage verbal. Tu es poète de l'âme.

**Domaine activé** : Maison 3 — Double eau sur la communication : tes mots coulent comme une rivière, portant des émotions profondes, des visions, des rêves. Tu comprends au-delà de ce qui est dit explicitement.

**Ton approche instinctive** : Le Poissons te fait communiquer de manière non-linéaire, symbolique, parfois confuse. Tu captes ce que les autres ne disent pas, tu ressens l'intention derrière les mots.

**Tensions possibles** : Le manque de clarté peut créer des malentendus. Tu risques de te perdre dans l'implicite, de ne pas poser de limites verbales claires, ou de te noyer dans les émotions non-dites des autres.

**Conseil clé** : Développer une communication claire et directe quand nécessaire, tout en gardant ta sensibilité poétique.""",
        'weekly_advice': {
            'week_1': "Écris ou exprime tes émotions de manière créative et fluide.",
            'week_2': "Pratique la communication claire et directe sur tes besoins.",
            'week_3': "Protège-toi des émotions non-dites des autres.",
            'week_4': "Célèbre ta capacité unique à communiquer avec l'âme."
        }
    },

    # ==================== MAISON 4 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Foyer conquis**

Ta Lune en Cancer en Maison 4, son domicile naturel, amplifie ton besoin de foyer, de famille, de racines profondes. L'Ascendant Bélier ajoute une urgence : tu veux créer ou protéger ton nid avec une énergie guerrière.

**Domaine activé** : Maison 4 — Ton foyer intérieur et extérieur est ton territoire sacré. Tu défends férocement ton espace privé, ta famille, tes origines. C'est là que tu te ressources et te montres le plus vulnérable.

**Ton approche instinctive** : Le Bélier te fait agir rapidement pour sécuriser ton foyer. Tu peux déménager impulsivement, rénover avec passion, ou défendre ta famille avec une intensité surprenante.

**Tensions possibles** : L'agressivité protectrice peut créer des conflits familiaux. Tu risques de devenir trop contrôlant·e sur ton espace, ou de combattre pour des blessures d'enfance non résolues.

**Conseil clé** : Utiliser ton courage pour guérir ton passé, pas pour le défendre ou l'attaquer.""",
        'weekly_advice': {
            'week_1': "Améliore ton espace de vie d'une manière qui te fait te sentir en sécurité.",
            'week_2': "Affronte une blessure familiale que tu as évitée.",
            'week_3': "Crée des limites saines avec ta famille d'origine.",
            'week_4': "Célèbre le sanctuaire que tu as créé pour toi."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Racines solides**

Ta Lune en Cancer en Maison 4 fait de ton foyer ton centre émotionnel absolu. L'Ascendant Taureau amplifie ce besoin de sécurité : tu construis un nid durable, beau, confortable, un vrai sanctuaire de stabilité.

**Domaine activé** : Maison 4 — Double énergie de terre et d'eau sur ton foyer : tu crées un espace qui nourrit tous tes sens et ton âme. Ta maison devient ton chef-d'œuvre de confort et de beauté.

**Ton approche instinctive** : Le Taureau te pousse à investir patiemment dans ton foyer, à accumuler des objets de qualité, à créer des traditions familiales réconfortantes. Tu es l'architecte de ta sécurité domestique.

**Tensions possibles** : L'attachement excessif au foyer peut devenir une prison dorée. Tu risques de refuser de quitter ton cocon même quand la vie t'appelle ailleurs, ou de te définir uniquement par ton espace domestique.

**Conseil clé** : Créer un foyer mobile dans ton cœur qui peut voyager avec toi où que tu ailles.""",
        'weekly_advice': {
            'week_1': "Investis dans quelque chose qui embellit durablement ton espace.",
            'week_2': "Crée un rituel domestique réconfortant et régulier.",
            'week_3': "Pratique le lâcher-prise sur le contrôle total de ton environnement.",
            'week_4': "Savoure le sanctuaire de paix que tu as construit."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Foyer vivant**

Ta Lune en Cancer en Maison 4 fait de ton foyer ton ancrage émotionnel. L'Ascendant Gémeaux ajoute du mouvement : ton chez-toi a besoin de stimulation intellectuelle, de changement, de connexions variées pour te nourrir vraiment.

**Domaine activé** : Maison 4 — Ton foyer doit être à la fois un cocon sécurisant et un espace de découverte. Tu as besoin de racines flexibles, d'une base qui permet l'exploration.

**Ton approche instinctive** : Le Gémeaux te fait changer régulièrement ton espace, inviter des gens, remplir ta maison de livres et d'idées. Tu peux avoir plusieurs "chez-toi" ou bouger souvent sans perdre ton ancrage.

**Tensions possibles** : Le conflit entre besoin de stabilité et besoin de changement peut créer de l'agitation. Tu risques de déménager trop souvent par peur de l'ennui, ou de te sentir déraciné·e même chez toi.

**Conseil clé** : Créer une stabilité intérieure qui permet le mouvement extérieur sans perte de sécurité.""",
        'weekly_advice': {
            'week_1': "Réorganise ton espace pour créer une nouveauté rafraîchissante.",
            'week_2': "Invite quelqu'un chez toi pour partager ton cocon.",
            'week_3': "Explore tes racines familiales à travers les histoires.",
            'week_4': "Célèbre ta capacité à être enraciné·e ET adaptable."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Foyer sacré**

Triple Cancer en Maison 4 : le placement le plus puissant pour cette Lune. Ton foyer est ton temple, ta famille est ton église, tes racines sont ton identité même. C'est un mois de retour aux sources, de connexion profonde avec tes origines.

**Domaine activé** : Maison 4 — Énergie cancérienne pure sur ton foyer : chaque espace domestique devient chargé d'une signification émotionnelle intense. Ta maison te parle, te nourrit, te guérit.

**Ton approche instinctive** : Triple eau sur tes racines : tu ressens tout ce qui concerne ta famille, ton passé, ton foyer. Les blessures ancestrales peuvent remonter pour être guéries. Ton intuition domestique est infaillible.

**Tensions possibles** : L'attachement au passé peut devenir paralysant. Tu risques de te noyer dans la nostalgie, de rester prisonnier·ère de ton enfance, ou de confondre ta maison avec ton identité.

**Conseil clé** : Honorer tes racines tout en permettant à ton arbre de grandir vers le ciel.""",
        'weekly_advice': {
            'week_1': "Plonge dans ton histoire familiale pour mieux te comprendre.",
            'week_2': "Guéris une blessure d'enfance qui te limite encore.",
            'week_3': "Crée un espace sacré chez toi pour ton ressourcement.",
            'week_4': "Célèbre la profondeur de ton ancrage et de ton nid."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Palais chaleureux**

Ta Lune en Cancer en Maison 4 fait de ton foyer ton sanctuaire émotionnel. L'Ascendant Lion ajoute une touche de grandeur : tu veux que ton chez-toi soit magnifique, que ta famille soit fière, que ton héritage rayonne.

**Domaine activé** : Maison 4 — Ton foyer devient ton royaume où tu peux briller dans ton authenticité. Tu investis ton cœur généreux dans la création d'un espace chaleureux et impressionnant.

**Ton approche instinctive** : Le Lion te pousse à créer un foyer dont tu es fier·ère, à accueillir avec générosité royale, à construire un héritage familial mémorable. Ta maison reflète ta grandeur intérieure.

**Tensions possibles** : Le besoin de reconnaissance peut créer des tensions familiales. Tu risques de vouloir que ta famille te valorise constamment, ou de créer un foyer pour impressionner plutôt que pour nourrir.

**Conseil clé** : Créer un foyer qui honore ton cœur authentique, pas l'image que tu veux projeter.""",
        'weekly_advice': {
            'week_1': "Embellis ton espace d'une manière qui reflète ta vraie nature.",
            'week_2': "Organise un rassemblement familial chaleureux chez toi.",
            'week_3': "Exprime ta fierté de tes racines sans chercher l'approbation.",
            'week_4': "Célèbre le rayonnement de ton foyer et de ton cœur."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Foyer perfectionné**

Ta Lune en Cancer en Maison 4 fait de ton foyer ton centre émotionnel. L'Ascendant Vierge ajoute un souci du détail : tu veux que ton chez-toi soit impeccable, organisé, fonctionnel. Le nid parfait.

**Domaine activé** : Maison 4 — Ton espace domestique devient un projet d'amélioration continue. Tu cherches à créer un environnement qui serve efficacement tes besoins émotionnels et pratiques.

**Ton approche instinctive** : La Vierge te fait analyser chaque aspect de ton foyer, optimiser chaque espace, maintenir un ordre rassurant. Tu peux devenir hypercritique de ton environnement ou de ta famille.

**Tensions possibles** : Le perfectionnisme domestique peut créer de l'anxiété. Tu risques de ne jamais te sentir satisfait·e de ton chez-toi, ou de critiquer constamment ceux avec qui tu vis.

**Conseil clé** : Accepter que le foyer parfait est celui qui est vivant et aimant, pas nécessairement impeccable.""",
        'weekly_advice': {
            'week_1': "Organise un aspect de ton foyer qui te stresse.",
            'week_2': "Crée des systèmes qui facilitent la vie domestique.",
            'week_3': "Lâche prise sur le contrôle total de ton environnement.",
            'week_4': "Célèbre le foyer fonctionnel et aimant que tu as créé."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie domestique**

Ta Lune en Cancer en Maison 4 fait de ton foyer ton refuge émotionnel. L'Ascendant Balance ajoute un besoin d'esthétique et d'équilibre : tu veux un chez-toi beau, harmonieux, où règnent la paix et l'élégance.

**Domaine activé** : Maison 4 — Ton foyer doit être un espace de beauté et de relations équilibrées. Tu investis dans le design, dans la création d'une atmosphère apaisante et raffinée.

**Ton approche instinctive** : La Balance te pousse à médiatiser les conflits familiaux, à créer de l'harmonie, à sacrifier parfois tes besoins pour maintenir la paix domestique.

**Tensions possibles** : Le besoin d'harmonie peut t'empêcher d'exprimer tes vrais besoins. Tu risques d'étouffer tes émotions pour ne pas déranger l'équilibre familial, ou de dépendre de l'approbation domestique pour te sentir bien.

**Conseil clé** : Créer une vraie harmonie basée sur l'authenticité, pas sur l'évitement des conflits.""",
        'weekly_advice': {
            'week_1': "Embellis ton espace de vie d'une manière qui t'apaise vraiment.",
            'week_2': "Adresse un conflit familial avec douceur mais honnêteté.",
            'week_3': "Équilibre tes besoins et ceux de ta famille.",
            'week_4': "Célèbre l'harmonie authentique que tu as créée chez toi."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Profondeur ancestrale**

Ta Lune en Cancer en Maison 4 te connecte profondément à tes racines. L'Ascendant Scorpion intensifie cette plongée : tu explores les secrets familiaux, les blessures transgénérationnelles, les vérités cachées de ton héritage.

**Domaine activé** : Maison 4 — Double eau sur ton foyer : ton chez-toi devient un espace de transformation psychologique profonde. Les fantômes du passé peuvent ressurgir pour être exorcisés.

**Ton approche instinctive** : Le Scorpion te pousse à creuser sous la surface de ton histoire familiale. Tu veux comprendre les non-dits, guérir les traumatismes ancestraux, transformer ta lignée.

**Tensions possibles** : L'intensité émotionnelle familiale peut être écrasante. Tu risques de te perdre dans les drames ancestraux, de porter des fardeaux qui ne sont pas les tiens, ou de couper les ponts radicalement.

**Conseil clé** : Guérir ton passé sans t'y noyer, transformer ton héritage sans te laisser définir par lui.""",
        'weekly_advice': {
            'week_1': "Explore un secret ou non-dit familial que tu as toujours senti.",
            'week_2': "Libère-toi d'un pattern transgénérationnel toxique.",
            'week_3': "Transforme ton espace de vie pour refléter ton renouveau.",
            'week_4': "Célèbre la puissance de ta lignée guérie et transformée."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foyer nomade**

Ta Lune en Cancer en Maison 4 cherche des racines profondes et un foyer stable. L'Ascendant Sagittaire crée un paradoxe : tu veux appartenir à un lieu tout en gardant la liberté d'explorer le monde.

**Domaine activé** : Maison 4 — Ton foyer doit être à la fois un ancrage et un point de départ pour l'aventure. Tu cherches peut-être tes racines dans plusieurs cultures, pays, ou philosophies.

**Ton approche instinctive** : Le Sagittaire te fait élargir la notion de foyer au-delà du domestique. Le monde entier peut devenir ta maison, ou tu cherches le sens philosophique de l'appartenance.

**Tensions possibles** : Le conflit entre enracinement et liberté peut créer de l'instabilité. Tu risques de fuir ton foyer par peur d'être piégé·e, ou de te sentir déchiré·e entre partir et rester.

**Conseil clé** : Comprendre que les vraies racines sont mobiles et peuvent voyager avec toi.""",
        'weekly_advice': {
            'week_1': "Explore tes origines culturelles ou spirituelles.",
            'week_2': "Crée un foyer qui honore ton besoin d'expansion.",
            'week_3': "Trouve l'ancrage dans la quête elle-même, pas dans un lieu.",
            'week_4': "Célèbre ta capacité unique à être enraciné·e partout."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Héritage structuré**

Ta Lune en Cancer en Maison 4 active l'axe Cancer-Capricorne de plein fouet : foyer et carrière, émotion et structure, racines et sommet. Ce mois demande d'intégrer ces deux pôles apparemment opposés.

**Domaine activé** : Maison 4 — Opposition fondamentale : tu dois nourrir ton besoin de cocon tout en construisant ton empire. Ta famille et ton ambition se confrontent ou se soutiennent.

**Ton approche instinctive** : Le Capricorne te pousse à créer un héritage familial durable, à structurer ton foyer comme un projet sérieux. Tu peux être le pilier de ta famille, portant ses responsabilités avec maturité.

**Tensions possibles** : Le sacrifice de l'un pour l'autre crée du déséquilibre. Tu risques de négliger ton foyer pour ta carrière ou vice-versa, ou de porter le poids de ta famille comme un fardeau.

**Conseil clé** : Comprendre que le succès extérieur n'a de sens que s'il repose sur des fondations émotionnelles solides.""",
        'weekly_advice': {
            'week_1': "Équilibre concrètement temps familial et temps professionnel.",
            'week_2': "Construis un aspect de ton foyer qui durera dans le temps.",
            'week_3': "Libère-toi d'une responsabilité familiale qui n'est pas tienne.",
            'week_4': "Célèbre l'intégration de ton cœur et de ton ambition."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Tribu choisie**

Ta Lune en Cancer en Maison 4 cherche la sécurité du foyer traditionnel. L'Ascendant Verseau révolutionne cette notion : ta vraie famille est peut-être celle que tu choisis, ton foyer est peut-être une communauté alternative.

**Domaine activé** : Maison 4 — Opposition Cancer-Verseau : besoin d'appartenance contre besoin d'individualité. Tu redéfinis ce que foyer et famille signifient pour toi, au-delà des normes.

**Ton approche instinctive** : Le Verseau te pousse à créer un foyer non-conventionnel, une famille d'âmes choisies, un espace qui honore ton unicité. Tu peux te sentir aliéné·e de ta famille d'origine.

**Tensions possibles** : Le conflit entre loyauté familiale et authenticité personnelle peut déchirer. Tu risques de couper complètement avec tes racines ou de vivre une double vie pour maintenir le lien.

**Conseil clé** : Honorer tes origines tout en créant ton propre modèle de foyer qui reflète qui tu es vraiment.""",
        'weekly_advice': {
            'week_1': "Définis ce que foyer et famille signifient authentiquement pour toi.",
            'week_2': "Connecte-toi avec ta tribu choisie ou trouve-la.",
            'week_3': "Respecte tes racines sans te laisser définir par elles.",
            'week_4': "Célèbre ton foyer unique et ta famille authentique."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sanctuaire spirituel**

Ta Lune en Cancer en Maison 4 fait de ton foyer ton temple émotionnel. L'Ascendant Poissons spiritualise cet espace : ton chez-toi devient un sanctuaire sacré, un lieu de dissolution des frontières, de connexion au divin.

**Domaine activé** : Maison 4 — Triple eau sur ton foyer : ton espace domestique est chargé d'une énergie psychique et spirituelle puissante. Les mémoires ancestrales, les rêves, l'invisible habitent ta maison.

**Ton approche instinctive** : Le Poissons te pousse à créer un espace de paix transcendante, où les limites se dissolvent. Tu peux avoir besoin de solitude sacrée chez toi, ou d'ouvrir ton foyer aux âmes en détresse.

**Tensions possibles** : Le manque de limites peut envahir ton sanctuaire. Tu risques de perdre ton espace personnel en accueillant tout le monde, ou de te noyer dans les émotions familiales collectives.

**Conseil clé** : Créer des frontières sacrées qui protègent ton sanctuaire tout en restant ouvert au divin.""",
        'weekly_advice': {
            'week_1': "Consacre un espace chez toi à ta pratique spirituelle.",
            'week_2': "Nettoie énergétiquement ton foyer des mémoires lourdes.",
            'week_3': "Établis des limites claires sur qui peut entrer dans ton sanctuaire.",
            'week_4': "Célèbre la dimension sacrée de ton foyer et de tes racines."
        }
    },

    # ==================== MAISON 5 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Créativité courageuse**

Ta Lune en Cancer en Maison 5 teinte ta créativité d'émotion profonde. Tu crées depuis ton cœur, tes enfants ou projets sont nourris de ta sensibilité. L'Ascendant Bélier ajoute une audace : tu oses exprimer ton monde intérieur avec spontanéité et passion.

**Domaine activé** : Maison 5 — Ta créativité, tes amours, tes plaisirs sont intensément émotionnels. Tu t'investis à fond dans ce qui te fait vibrer, avec une vulnérabilité guerrière.

**Ton approche instinctive** : Le Bélier te pousse à créer impulsivement, à tomber amoureux·se rapidement, à jouer avec enthousiasme. Tu veux vivre tes émotions créatives intensément et maintenant.

**Tensions possibles** : L'impulsivité émotionnelle peut créer du drame. Tu risques de confondre passion et amour, de surprotéger tes créations, ou de t'épuiser dans l'intensité constante.

**Conseil clé** : Canaliser ton courage créatif avec discernement, créer depuis l'authenticité plutôt que depuis l'urgence.""",
        'weekly_advice': {
            'week_1': "Lance un projet créatif qui te tient vraiment à cœur.",
            'week_2': "Exprime tes émotions à travers une forme d'art ou de jeu.",
            'week_3': "Protège tes créations sans les étouffer par surprotection.",
            'week_4': "Célèbre ta capacité à créer depuis ton cœur courageux."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Plaisir nourrissant**

Ta Lune en Cancer en Maison 5 fait de ta créativité une extension de ton besoin de nourrir. L'Ascendant Taureau amplifie le plaisir sensoriel : tu crées de la beauté, tu aimes avec constance, tu jouis des plaisirs simples et profonds.

**Domaine activé** : Maison 5 — Tes créations doivent être belles, durables, réconfortantes. L'amour et le plaisir sont des terrains de sécurité autant que d'expression.

**Ton approche instinctive** : Le Taureau te fait créer lentement mais avec qualité, aimer fidèlement, cultiver des plaisirs qui nourrissent tous tes sens. Ta créativité est sensuelle et patiente.

**Tensions possibles** : L'attachement aux plaisirs peut devenir excessif. Tu risques de t'accrocher à des amours sécurisantes mais mortes, ou de surindulger dans le confort créatif sans prendre de risques.

**Conseil clé** : Équilibrer sécurité et spontanéité dans ta vie créative et amoureuse.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose de beau qui nourrit ton âme.",
            'week_2': "Savoure un plaisir simple avec pleine conscience.",
            'week_3': "Prends un risque créatif hors de ta zone de confort.",
            'week_4': "Célèbre ta capacité à créer beauté et stabilité."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Jeu expressif**

Ta Lune en Cancer en Maison 5 rend ta créativité émotionnellement chargée. L'Ascendant Gémeaux ajoute de la légèreté : tu exprimes tes sentiments de mille façons, tu joues avec les mots, les idées, les formes pour communiquer ton monde intérieur.

**Domaine activé** : Maison 5 — Ta créativité passe par la communication, l'échange, la variété. Tes amours sont intellectuellement stimulantes autant qu'émotionnellement nourrissantes.

**Ton approche instinctive** : Le Gémeaux te fait explorer différentes formes créatives, papillonner entre les passions, verbaliser tes émotions à travers l'art ou le jeu.

**Tensions possibles** : La dispersion peut diluer ta profondeur créative. Tu risques de ne jamais approfondir une forme d'expression, ou de fuir l'intensité émotionnelle par la légèreté intellectuelle.

**Conseil clé** : Choisir quelques expressions créatives et les approfondir tout en gardant ta curiosité vivante.""",
        'weekly_advice': {
            'week_1': "Expérimente une nouvelle forme d'expression créative.",
            'week_2': "Écris ou partage une histoire qui te touche profondément.",
            'week_3': "Engage-toi plus profondément dans un projet plutôt que de papillonner.",
            'week_4': "Célèbre ta polyvalence créative et émotionnelle."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Création maternelle**

Triple Cancer en Maison 5 : ta créativité est maternelle, nourricière, profondément émotionnelle. Tes projets sont tes enfants, ton art est ton lait maternel, ta joie est dans le fait de donner vie et de protéger ce que tu crées.

**Domaine activé** : Maison 5 — Chaque acte créatif est un accouchement émotionnel. Tu t'investis corps et âme dans ce que tu aimes, avec une vulnérabilité totale et une protection féroce.

**Ton approche instinctive** : Triple eau sur ta créativité : tu crées depuis les profondeurs de ton être. L'amour, l'art, le jeu sont des terrains d'expression de ton besoin viscéral de nourrir et d'être nourri·e.

**Tensions possibles** : La fusion avec tes créations peut devenir étouffante. Tu risques de surprotéger tes enfants ou projets, de les empêcher de vivre indépendamment de toi.

**Conseil clé** : Créer et aimer avec générosité tout en permettant l'autonomie et la séparation.""",
        'weekly_advice': {
            'week_1': "Donne naissance à un projet qui vient vraiment de ton cœur.",
            'week_2': "Nourris tes créations sans les étouffer de surprotection.",
            'week_3': "Permets à ce que tu aimes de grandir indépendamment.",
            'week_4': "Célèbre ta puissance créatrice maternelle unique."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Cœur en scène**

Ta Lune en Cancer en Maison 5 fait de ta créativité une affaire de cœur. L'Ascendant Lion, maître naturel de cette maison, amplifie le rayonnement : tu veux exprimer ton monde émotionnel de manière magnifique, être vu·e et célébré·e pour ton authenticité.

**Domaine activé** : Maison 5 — Double énergie léonine sur ta créativité : tu crées depuis le cœur et pour le cœur. Ton art, tes amours, ton jeu sont des expressions généreuses de qui tu es vraiment.

**Ton approche instinctive** : Le Lion te pousse à créer avec grandeur, à aimer passionnément, à briller par ta vulnérabilité assumée. Tu veux que ton cœur soit vu dans toute sa splendeur.

**Tensions possibles** : Le besoin de reconnaissance peut contaminer ta créativité. Tu risques de créer pour l'applaudissement plutôt que pour l'expression authentique, ou de dépendre de l'admiration pour te sentir valide.

**Conseil clé** : Créer et aimer depuis ton cœur véritable, que tu aies un public ou non.""",
        'weekly_advice': {
            'week_1': "Exprime-toi créativement sans chercher l'approbation.",
            'week_2': "Aime généreusement sans attendre de retour garanti.",
            'week_3': "Brille par ton authenticité plutôt que par la performance.",
            'week_4': "Célèbre la royauté de ton cœur créatif."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Art perfectionniste**

Ta Lune en Cancer en Maison 5 rend ta créativité émotionnellement profonde. L'Ascendant Vierge ajoute du perfectionnisme : tu veux que ton expression soit juste, utile, techniquement impeccable. Chaque détail de ta création compte.

**Domaine activé** : Maison 5 — Ta créativité devient un terrain d'amélioration continue. Tu peaufines, tu analyses, tu cherches l'excellence dans l'expression de tes émotions.

**Ton approche instinctive** : La Vierge te fait créer avec méthode et attention au détail. Tu peux devenir hypercritique de tes œuvres, retravaillant sans cesse jusqu'à ce qu'elles incarnent parfaitement ce que tu ressens.

**Tensions possibles** : L'autocritique peut paralyser ta créativité. Tu risques de ne jamais te sentir assez bon·ne, de bloquer ton expression par peur de l'imperfection, ou de perdre la spontanéité.

**Conseil clé** : Accepter que la créativité authentique est imparfaite par nature, et que c'est là sa beauté.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose sans chercher la perfection, juste l'expression.",
            'week_2': "Sers ton art au monde sans attendre qu'il soit parfait.",
            'week_3': "Observe ton critique intérieur et apprends à le faire taire.",
            'week_4': "Célèbre l'imperfection créative comme une forme de perfection."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Beauté partagée**

Ta Lune en Cancer en Maison 5 fait de ta créativité une expression de ton cœur. L'Ascendant Balance ajoute une dimension esthétique et relationnelle : tu crées de la beauté pour connecter, pour harmoniser, pour séduire.

**Domaine activé** : Maison 5 — Tes créations, tes amours, tes plaisirs doivent être beaux et partagés. Tu investis dans l'art qui crée du lien, dans les amours équilibrées et élégantes.

**Ton approche instinctive** : La Balance te pousse à créer pour plaire, à équilibrer esthétique et émotion, à chercher l'approbation dans ton expression créative.

**Tensions possibles** : Le besoin de plaire peut étouffer ton authenticité créative. Tu risques de créer ce que les autres attendent plutôt que ce que ton cœur demande, ou de perdre ta voix unique.

**Conseil clé** : Créer et aimer depuis ton propre centre tout en gardant ta sensibilité à la beauté et à l'harmonie.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose qui reflète tes goûts profonds, pas ceux des autres.",
            'week_2': "Équilibre ton besoin de plaire et ton besoin d'authenticité.",
            'week_3': "Partage ton art sans dépendre de l'approbation d'autrui.",
            'week_4': "Célèbre ta capacité à créer beauté et connexion."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Passion transformatrice**

Ta Lune en Cancer en Maison 5 rend ta créativité profondément émotionnelle. L'Ascendant Scorpion intensifie tout : tes amours sont obsessionnelles, ton art est cathartique, ton jeu est une exploration des profondeurs de l'âme.

**Domaine activé** : Maison 5 — Double eau sur la créativité : chaque acte créatif ou amoureux est une plongée dans les abysses. Tu ne crées pas pour décorer, tu crées pour transformer.

**Ton approche instinctive** : Le Scorpion te pousse à tout donner émotionnellement. Tes créations portent l'intensité de ton monde intérieur, tes amours sont totales ou inexistantes.

**Tensions possibles** : L'intensité constante peut être épuisante. Tu risques de brûler dans tes passions, de créer du drame dans l'amour, ou de t'épuiser émotionnellement dans ta créativité.

**Conseil clé** : Canaliser ton intensité créative sans te détruire, aimer profondément sans te perdre.""",
        'weekly_advice': {
            'week_1': "Crée une œuvre qui exprime tes profondeurs les plus cachées.",
            'week_2': "Transforme une douleur en art ou en beauté.",
            'week_3': "Dose ton intensité pour ne pas t'épuiser dans la passion.",
            'week_4': "Célèbre ton pouvoir de créer depuis les profondeurs."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Joie aventureuse**

Ta Lune en Cancer en Maison 5 rend ta créativité nourricière et protectrice. L'Ascendant Sagittaire ajoute de l'expansion : tu veux que ton art voyage, que tes amours élargissent ton monde, que ton jeu soit une quête de sens.

**Domaine activé** : Maison 5 — Ta créativité cherche la liberté et le sens. Tu crées pour explorer, pour enseigner, pour donner de l'espoir. L'amour est une aventure philosophique autant qu'émotionnelle.

**Ton approche instinctive** : Le Sagittaire te pousse à créer avec optimisme et générosité, à aimer sans attaches étouffantes, à jouer comme une célébration de la vie.

**Tensions possibles** : Le conflit entre attachement et liberté peut créer de l'instabilité amoureuse. Tu risques de fuir l'engagement par peur d'être piégé·e, ou de te sentir coupable de ton besoin d'espace.

**Conseil clé** : Créer et aimer avec engagement tout en gardant ta liberté intérieure et ton espace de croissance.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose qui élargit ta vision du monde.",
            'week_2': "Explore l'amour comme une aventure de croissance mutuelle.",
            'week_3': "Trouve l'équilibre entre engagement et liberté dans tes passions.",
            'week_4': "Célèbre ta capacité à aimer et créer librement."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Créativité construite**

Ta Lune en Cancer en Maison 5 rend ta créativité émotionnellement riche. L'Ascendant Capricorne ajoute de la structure : tu veux que ton art soit sérieux, durable, reconnu. L'amour devient un engagement construit patiemment.

**Domaine activé** : Maison 5 — Opposition Cancer-Capricorne sur la créativité : tu ressens profondément mais tu t'exprimes avec maîtrise. Tes créations portent une maturité émotionnelle.

**Ton approche instinctive** : Le Capricorne te fait créer avec discipline, aimer avec responsabilité, construire une réputation créative solide. Tu ne joues pas juste pour le plaisir, tu crées un héritage.

**Tensions possibles** : Le contrôle peut étouffer la spontanéité créative. Tu risques de prendre l'art trop au sérieux, de transformer l'amour en devoir, ou de perdre la joie dans la performance.

**Conseil clé** : Équilibrer discipline créative et spontanéité émotionnelle, construire sans perdre la capacité de jouer.""",
        'weekly_advice': {
            'week_1': "Engage-toi sérieusement sur un projet créatif à long terme.",
            'week_2': "Permets-toi aussi de créer juste pour le plaisir.",
            'week_3': "Aime avec engagement sans perdre ta spontanéité.",
            'week_4': "Célèbre l'équilibre entre structure et émotion dans ton art."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Art révolutionnaire**

Ta Lune en Cancer en Maison 5 rend ta créativité profondément personnelle et émotionnelle. L'Ascendant Verseau universalise : tu veux que ton art serve une cause, que ton amour soit libre, que ta créativité révolutionne.

**Domaine activé** : Maison 5 — Opposition Cancer-Verseau : tu crées depuis ton cœur intime mais pour le collectif. Ton art personnel porte un message universel.

**Ton approche instinctive** : Le Verseau te pousse à créer différemment, à aimer sans possession, à exprimer ton originalité unique. Tu ne veux pas créer ce qui a déjà été fait.

**Tensions possibles** : Le détachement peut te couper de ton cœur créatif. Tu risques d'intellectualiser ton art au point de perdre son âme, ou de fuir l'intimité amoureuse par besoin de liberté.

**Conseil clé** : Créer depuis ton cœur unique tout en servant une vision plus grande, aimer librement sans fuir l'intimité.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose d'original qui porte ton empreinte unique.",
            'week_2': "Explore comment ton art peut servir une cause collective.",
            'week_3': "Trouve l'équilibre entre liberté et intimité dans l'amour.",
            'week_4': "Célèbre ton originalité créative et émotionnelle."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Art transcendant**

Ta Lune en Cancer en Maison 5 rend ta créativité nourricière et protectrice. L'Ascendant Poissons la spiritualise : ton art devient un canal divin, tes amours sont fusionnelles, ton jeu est une méditation, une prière.

**Domaine activé** : Maison 5 — Triple eau sur la créativité : tu crées depuis un océan de sensibilité. Ton art touche l'âme parce qu'il vient de l'âme.

**Ton approche instinctive** : Le Poissons te fait créer de manière intuitive, quasi-channelée. Tu te perds dans ta créativité, tu aimes sans limites, tu joues avec l'invisible.

**Tensions possibles** : Le manque de limites peut diluer ton expression. Tu risques de te perdre dans tes créations, de te sacrifier dans l'amour, ou de fuir la réalité par l'art.

**Conseil clé** : Créer depuis la transcendance tout en restant ancré·e, aimer profondément tout en gardant tes frontières.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose qui exprime ta spiritualité ou ton ressenti le plus profond.",
            'week_2': "Utilise l'art comme pratique spirituelle, pas comme fuite.",
            'week_3': "Aime généreusement sans te perdre dans l'autre.",
            'week_4': "Célèbre ton canal créatif unique et transcendant."
        }
    },

    # ==================== MAISON 6 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Service guerrier**

Ta Lune en Cancer en Maison 6 fait de ton travail quotidien un terrain émotionnel. Tu veux servir, aider, nourrir à travers ta routine. L'Ascendant Bélier ajoute de l'urgence : tu combats pour améliorer les choses, tu défends ceux que tu sers.

**Domaine activé** : Maison 6 — Ton travail, ta santé, tes routines sont teintés d'émotion et de protection. Tu veux être utile, mais avec passion et initiative.

**Ton approche instinctive** : Le Bélier te pousse à agir vite pour aider, à réagir impulsivement aux besoins des autres, à te battre pour améliorer les conditions de travail ou de santé.

**Tensions possibles** : L'épuisement émotionnel dans le service peut te consumer. Tu risques de t'oublier en aidant les autres, ou de devenir agressif·ve quand tu te sens utilisé·e.

**Conseil clé** : Servir depuis ta force plutôt que depuis ton besoin de validation, protéger ta propre santé émotionnelle.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton travail peut nourrir les autres ET toi.",
            'week_2': "Prends une initiative pour améliorer ton quotidien.",
            'week_3': "Protège-toi de l'épuisement par des limites claires.",
            'week_4': "Célèbre ta capacité à servir avec courage et cœur."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Routine nourricière**

Ta Lune en Cancer en Maison 6 fait de ton quotidien un terrain de soin et de service. L'Ascendant Taureau ajoute de la stabilité : tu crées des routines réconfortantes, tu travailles avec patience, tu prends soin de ton corps comme d'un enfant.

**Domaine activé** : Maison 6 — Ton travail et ta santé sont des terrains de sécurité. Tu veux des routines stables, un environnement professionnel confortable, une santé robuste.

**Ton approche instinctive** : Le Taureau te fait créer des habitudes saines lentement mais sûrement. Tu es fiable dans ton travail, constant·e dans ton service, patient·e dans ton amélioration.

**Tensions possibles** : La résistance au changement peut rigidifier tes routines. Tu risques de t'accrocher à des habitudes confortables mais malsaines, ou de refuser d'adapter ton travail quand nécessaire.

**Conseil clé** : Construire des routines saines qui servent vraiment ton bien-être, tout en restant flexible quand la vie demande l'adaptation.""",
        'weekly_advice': {
            'week_1': "Établis une routine quotidienne qui nourrit ton corps et ton âme.",
            'week_2': "Investis dans ta santé avec patience et constance.",
            'week_3': "Adapte une habitude rigide qui ne te sert plus.",
            'week_4': "Savoure la stabilité que tes routines t'apportent."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Service communicant**

Ta Lune en Cancer en Maison 6 fait de ton travail un terrain de soin émotionnel. L'Ascendant Gémeaux ajoute de la variété : tu veux des routines flexibles, un travail intellectuellement stimulant, une santé mentale autant que physique.

**Domaine activé** : Maison 6 — Ton quotidien a besoin de diversité et de connexion. Tu sers à travers la communication, l'échange, le partage d'informations utiles.

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre différentes tâches, adapter tes routines selon ton humeur, chercher la variété dans ton travail quotidien.

**Tensions possibles** : La dispersion peut nuire à ta santé et ton efficacité. Tu risques de te surcharger mentalement, de négliger tes besoins physiques, ou de ne jamais établir de routines stables.

**Conseil clé** : Équilibrer variété mentale et stabilité pratique, communication et action concrète dans ton quotidien.""",
        'weekly_advice': {
            'week_1': "Crée une routine flexible qui permet la variété.",
            'week_2': "Utilise tes compétences de communication pour servir les autres.",
            'week_3': "Ancre-toi dans quelques habitudes stables malgré ta curiosité.",
            'week_4': "Célèbre ta capacité à adapter ton service intelligemment."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Soin maternel**

Triple Cancer en Maison 6 : ton travail quotidien est un acte de maternage. Tu nourris, tu soignes, tu protèges à travers tes routines. Ta santé est profondément liée à ton état émotionnel, ton estomac parle pour ton cœur.

**Domaine activé** : Maison 6 — Ton service est viscéral, émotionnel, total. Tu ne peux pas séparer ton travail de tes sentiments. Ton corps réagit intensément à ton environnement émotionnel.

**Ton approche instinctive** : Triple eau sur le service : tu donnes depuis ton cœur jusqu'à l'épuisement. Tu ressens les maladies des autres, ton estomac se noue quand tu es stressé·e, ta santé reflète ton monde émotionnel.

**Tensions possibles** : L'épuisement par sur-don est un risque majeur. Tu risques de te sacrifier complètement dans ton travail, de somatiser tes émotions, ou de devenir hypocondriaque.

**Conseil clé** : Te nourrir autant que tu nourris les autres, protéger ta santé émotionnelle comme ton bien le plus précieux.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te sacrifies dans ton travail quotidien.",
            'week_2': "Crée des routines qui nourrissent TON bien-être avant tout.",
            'week_3': "Écoute ce que ton corps te dit sur ton état émotionnel.",
            'week_4': "Célèbre ta capacité unique à soigner depuis le cœur."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Service royal**

Ta Lune en Cancer en Maison 6 fait de ton travail un terrain de soin et de service. L'Ascendant Lion ajoute de la grandeur : tu veux servir généreusement, briller dans ton travail quotidien, être reconnu·e pour ta contribution.

**Domaine activé** : Maison 6 — Ton service doit être visible, apprécié, célébré. Tu ne veux pas juste aider dans l'ombre, tu veux que ton cœur généreux soit vu et honoré.

**Ton approche instinctive** : Le Lion te pousse à servir avec panache, à créer des routines qui te mettent en valeur, à exceller dans ton travail pour recevoir de la reconnaissance.

**Tensions possibles** : Le besoin de reconnaissance peut corrompre ton service. Tu risques de t'épuiser pour être applaudi·e, ou de te sentir diminué·e dans les tâches quotidiennes "invisibles".

**Conseil clé** : Servir depuis ta générosité authentique plutôt que depuis ton besoin d'attention, honorer les petites tâches autant que les grandes.""",
        'weekly_advice': {
            'week_1': "Sers avec ton cœur généreux sans attendre d'applaudissements.",
            'week_2': "Trouve la grandeur dans les petites tâches quotidiennes.",
            'week_3': "Célèbre ton propre travail sans dépendre de la validation externe.",
            'week_4': "Rayonne dans ton service avec humilité et fierté."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfectionnisme soignant**

Ta Lune en Cancer en Maison 6 fait de ton travail un terrain émotionnel de service. L'Ascendant Vierge, maître naturel de cette maison, amplifie le perfectionnisme : tu veux servir impeccablement, améliorer chaque détail, être utile à la perfection.

**Domaine activé** : Maison 6 — Double énergie virginienne sur le service : tu analyses, tu optimises, tu perfectionnes chaque routine. Ta santé devient un projet d'amélioration constante.

**Ton approche instinctive** : La Vierge te fait servir avec précision méticuleuse, créer des routines ultra-efficaces, chercher l'excellence dans le moindre détail de ton travail quotidien.

**Tensions possibles** : L'autocritique peut devenir toxique. Tu risques de ne jamais te sentir assez utile, de t'épuiser dans la quête de la perfection, ou de développer de l'anxiété autour de ta santé.

**Conseil clé** : Accepter que le service parfait n'existe pas, que ton humanité imparfaite est précisément ce qui rend ton aide précieuse.""",
        'weekly_advice': {
            'week_1': "Sers utilement sans chercher l'impeccabilité absolue.",
            'week_2': "Crée une routine de santé raisonnable, pas parfaite.",
            'week_3': "Observe ton critique intérieur et apprends à le tempérer.",
            'week_4': "Célèbre l'utilité de ton service malgré ses imperfections."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Service harmonieux**

Ta Lune en Cancer en Maison 6 fait de ton travail un terrain de soin émotionnel. L'Ascendant Balance ajoute un besoin d'équilibre : tu veux des routines harmonieuses, un environnement de travail esthétique, des relations professionnelles équilibrées.

**Domaine activé** : Maison 6 — Ton service cherche l'harmonie et la justice. Tu travailles mieux dans la beauté et la collaboration, tu équilibres les besoins de chacun.

**Ton approche instinctive** : La Balance te pousse à créer de l'harmonie dans ton quotidien, à médiatiser les conflits au travail, à chercher l'équilibre entre donner et recevoir dans ton service.

**Tensions possibles** : Le besoin de plaire peut t'empêcher de poser des limites. Tu risques de te surcharger pour maintenir la paix, ou de négliger ta santé pour ne pas déranger.

**Conseil clé** : Servir équitablement en incluant tes propres besoins dans l'équation, créer l'harmonie sans te sacrifier.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te sacrifies pour maintenir la paix au travail.",
            'week_2': "Crée un environnement quotidien esthétiquement apaisant.",
            'week_3': "Équilibre ton service aux autres et ton service à toi-même.",
            'week_4': "Célèbre ta capacité à créer harmonie ET santé."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Service transformateur**

Ta Lune en Cancer en Maison 6 fait de ton travail un terrain de soin et de protection. L'Ascendant Scorpion intensifie ton service : tu veux aider profondément, transformer par ton travail, guérir les blessures cachées.

**Domaine activé** : Maison 6 — Double eau sur le service : tu ne fais pas les choses à moitié. Ton travail quotidien touche les profondeurs, ta santé est liée à ta vie émotionnelle intense.

**Ton approche instinctive** : Le Scorpion te pousse à servir avec intensité totale, à donner jusqu'à l'épuisement, à transformer les crises en opportunités de service.

**Tensions possibles** : L'intensité constante peut te consumer. Tu risques de t'épuiser émotionnellement dans ton travail, de porter les fardeaux des autres, ou de développer des problèmes psychosomatiques.

**Conseil clé** : Servir puissamment tout en protégeant ton énergie vitale, transformer sans te détruire dans le processus.""",
        'weekly_advice': {
            'week_1': "Offre ton service là où une vraie transformation est possible.",
            'week_2': "Protège ton énergie par des limites claires dans ton travail.",
            'week_3': "Transforme une habitude de santé toxique en habitude régénératrice.",
            'week_4': "Célèbre ton pouvoir de guérir et servir profondément."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Service inspirant**

Ta Lune en Cancer en Maison 6 fait de ton travail un terrain de soin nourricier. L'Ascendant Sagittaire ajoute du sens : tu veux que ton service ait un impact, que ton travail quotidien enseigne, inspire, élargisse les horizons.

**Domaine activé** : Maison 6 — Ton travail doit avoir un sens philosophique, pas juste être des tâches répétitives. Tu cherches la liberté même dans tes routines, la croissance dans ton service.

**Ton approche instinctive** : Le Sagittaire te pousse à servir avec optimisme et générosité, à enseigner à travers ton travail, à chercher le sens de chaque tâche quotidienne.

**Tensions possibles** : Le besoin de sens peut te faire mépriser les tâches simples. Tu risques de fuir les routines nécessaires, de négliger ta santé par excès d'optimisme, ou de t'éparpiller dans trop de projets.

**Conseil clé** : Trouver le sens dans les petites tâches, honorer le quotidien comme une pratique spirituelle.""",
        'weekly_advice': {
            'week_1': "Donne du sens à tes routines en les reliant à une vision plus large.",
            'week_2': "Sers en enseignant ou en inspirant à travers ton travail.",
            'week_3': "Ancre-toi dans des habitudes de santé simples mais constantes.",
            'week_4': "Célèbre la sagesse qui émerge de ton service quotidien."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Devoir structuré**

Ta Lune en Cancer en Maison 6 fait de ton travail un terrain émotionnel de service. L'Ascendant Capricorne ajoute de la discipline : tu structures tes routines, tu accomplis ton devoir avec sérieux, ta santé est une responsabilité.

**Domaine activé** : Maison 6 — Opposition Cancer-Capricorne : tu ressens profondément ton travail mais tu l'accomplis avec maîtrise. Le service devient un devoir honorable.

**Ton approche instinctive** : Le Capricorne te fait créer des routines strictes, servir avec fiabilité, construire une réputation professionnelle solide à travers ton travail quotidien exemplaire.

**Tensions possibles** : Le refoulement émotionnel peut nuire à ta santé. Tu risques de négliger tes besoins émotionnels pour accomplir ton devoir, ou de développer des maladies de stress.

**Conseil clé** : Équilibrer discipline et soin de soi, accomplir ton devoir sans sacrifier ton bien-être émotionnel.""",
        'weekly_advice': {
            'week_1': "Crée des routines disciplinées qui servent aussi ton cœur.",
            'week_2': "Accomplis ton travail avec sérieux ET avec compassion pour toi.",
            'week_3': "Libère les tensions émotionnelles avant qu'elles ne deviennent physiques.",
            'week_4': "Célèbre ta fiabilité et ta capacité à servir durablement."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Service révolutionnaire**

Ta Lune en Cancer en Maison 6 fait de ton travail un terrain de soin personnel. L'Ascendant Verseau universalise ton service : tu veux aider le collectif, révolutionner les méthodes de travail, servir une cause plus grande.

**Domaine activé** : Maison 6 — Opposition Cancer-Verseau : tu sers depuis ton cœur mais pour l'humanité. Tes routines sont peut-être non-conventionnelles, ton approche de la santé alternative.

**Ton approche instinctive** : Le Verseau te pousse à innover dans ton service, à utiliser la technologie, à créer des systèmes qui aident efficacement. Tu te détaches émotionnellement pour mieux servir objectivement.

**Tensions possibles** : Le détachement peut te couper de ton cœur de service. Tu risques d'intellectualiser le soin au point de perdre l'humanité, ou de sacrifier tes besoins pour une cause abstraite.

**Conseil clé** : Servir le collectif sans oublier tes besoins personnels, innover tout en gardant ton cœur dans ton travail.""",
        'weekly_advice': {
            'week_1': "Trouve comment ton service personnel peut servir une cause collective.",
            'week_2': "Expérimente des méthodes de travail ou de santé innovantes.",
            'week_3': "Reste connecté·e à ton cœur même en servant objectivement.",
            'week_4': "Célèbre ton originalité dans ta façon de servir."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sacrifice sacré**

Ta Lune en Cancer en Maison 6 fait de ton travail un acte de soin maternel. L'Ascendant Poissons spiritualise ton service : tu te sacrifies pour aider, ton travail devient une prière, ta santé est liée à ton état spirituel.

**Domaine activé** : Maison 6 — Triple eau sur le service : tu donnes sans compter, parfois sans limites. Ton corps absorbe les émotions de ton environnement, tu ressens les maladies des autres.

**Ton approche instinctive** : Le Poissons te pousse à servir avec une compassion infinie, à te fondre dans ton travail, à dissoudre tes limites pour mieux aider. Cette générosité peut être transcendante ou épuisante.

**Tensions possibles** : Le sacrifice de soi peut te détruire. Tu risques de perdre ton identité dans le service, de te rendre malade en absorbant la douleur des autres, ou de fuir dans la maladie pour te protéger.

**Conseil clé** : Servir depuis la compassion tout en gardant tes frontières, donner sans te perdre complètement.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te sacrifies de manière malsaine.",
            'week_2': "Crée des limites énergétiques claires dans ton service.",
            'week_3': "Utilise des pratiques spirituelles pour te régénérer après avoir servi.",
            'week_4': "Célèbre ta compassion infinie tout en te protégeant."
        }
    },

    # ==================== MAISON 7 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Partenaire protecteur**

Ta Lune en Cancer en Maison 7 fait de tes relations un besoin émotionnel profond. Tu cherches la sécurité dans le partenariat, tu nourris tes allié·es comme ta famille. L'Ascendant Bélier ajoute de la combativité : tu défends férocement tes relations.

**Domaine activé** : Maison 7 — Tes partenariats sont ton cocon émotionnel. Tu t'investis à fond, tu cherches la fusion, tu protèges tes alliances avec passion et parfois agressivité.

**Ton approche instinctive** : Le Bélier te fait agir rapidement en relation, peut-être trop vite. Tu peux te lancer dans des engagements impulsivement, puis les défendre avec acharnement même s'ils ne te nourrissent plus.

**Tensions possibles** : La dépendance émotionnelle aux partenaires peut créer des dynamiques toxiques. Tu risques de devenir possessif·ve, de projeter tes besoins sur l'autre, ou de combattre pour des relations qui te blessent.

**Conseil clé** : Cultiver la sécurité intérieure avant de la chercher dans le partenariat, choisir tes allié·es consciemment plutôt qu'impulsivement.""",
        'weekly_advice': {
            'week_1': "Examine ce que tu cherches vraiment dans tes relations.",
            'week_2': "Protège tes partenariats sans devenir possessif·ve.",
            'week_3': "Cultive ta sécurité émotionnelle indépendamment de l'autre.",
            'week_4': "Célèbre les relations qui te nourrissent vraiment."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Alliance stable**

Ta Lune en Cancer en Maison 7 fait de tes partenariats un besoin de sécurité émotionnelle. L'Ascendant Taureau amplifie la loyauté : tu construis des relations durables, fidèles, confortables. Tes alliances sont pour la vie.

**Domaine activé** : Maison 7 — Tes partenariats doivent être stables, prévisibles, nourrissants. Tu investis lentement mais profondément, créant des liens qui résistent au temps.

**Ton approche instinctive** : Le Taureau te fait choisir tes partenaires avec soin, construire la relation pierre par pierre, valoriser la constance et la fidélité par-dessus tout.

**Tensions possibles** : L'attachement excessif peut devenir une prison. Tu risques de rester dans des relations mortes par peur du changement, ou de confondre stabilité et stagnation.

**Conseil clé** : Construire des partenariats durables qui évoluent avec vous, honorer la loyauté sans sacrifier la croissance.""",
        'weekly_advice': {
            'week_1': "Investis dans une relation qui mérite ta loyauté à long terme.",
            'week_2': "Crée des rituels partagés qui nourrissent le lien.",
            'week_3': "Évalue honnêtement si tes relations stagnent ou évoluent.",
            'week_4': "Célèbre la profondeur et la durabilité de tes alliances."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Partenaire communicatif**

Ta Lune en Cancer en Maison 7 fait de tes relations un besoin émotionnel vital. L'Ascendant Gémeaux ajoute de la légèreté : tu veux des partenaires avec qui parler, échanger, explorer intellectuellement tout en te sentant en sécurité émotionnellement.

**Domaine activé** : Maison 7 — Tes partenariats ont besoin de communication fluide et de variété. Tu cherches la sécurité émotionnelle à travers l'échange verbal et la connexion mentale.

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre différentes connexions, chercher la stimulation intellectuelle dans tes relations, verbaliser tes besoins émotionnels constamment.

**Tensions possibles** : La dispersion peut empêcher l'approfondissement. Tu risques de fuir l'intimité émotionnelle par l'intellectualisation, ou de multiplier les relations superficielles.

**Conseil clé** : Équilibrer besoin de variété et besoin de profondeur, communiquer ET ressentir dans tes partenariats.""",
        'weekly_advice': {
            'week_1': "Engage une conversation profonde qui renforce une relation clé.",
            'week_2': "Explore différentes facettes d'un partenariat important.",
            'week_3': "Pratique l'intimité silencieuse au-delà des mots.",
            'week_4': "Célèbre ta capacité à créer des liens par la communication."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Fusion totale**

Triple Cancer en Maison 7 : tes relations sont ton identité même. Tu ne peux pas séparer qui tu es de tes partenariats. Tu cherches la fusion émotionnelle absolue, une famille choisie avec qui fusionner complètement.

**Domaine activé** : Maison 7 — Tes partenariats sont ta raison d'être. Tu t'investis corps et âme, tu deviens ce que l'autre a besoin, tu cherches quelqu'un qui devienne ton foyer vivant.

**Ton approche instinctive** : Triple eau sur les relations : tu veux te fondre dans l'autre, créer une unité émotionnelle totale, nourrir et être nourri·e dans une symbiose parfaite.

**Tensions possibles** : La fusion peut faire perdre ton identité. Tu risques de te perdre complètement dans l'autre, de devenir codépendant·e, ou de suffoquer tes partenaires par ton besoin d'intimité totale.

**Conseil clé** : Apprendre que l'amour véritable inclut deux individualités qui choisissent de se rejoindre, pas une fusion qui dissout les identités.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te perds dans tes relations.",
            'week_2': "Cultive ton individualité au sein du partenariat.",
            'week_3': "Crée des espaces de solitude saine dans la relation.",
            'week_4': "Célèbre l'intimité profonde sans perdre ton identité."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Partenaire royal**

Ta Lune en Cancer en Maison 7 fait de tes relations un besoin émotionnel profond. L'Ascendant Lion ajoute de la grandeur : tu veux un·e partenaire dont tu peux être fier·ère, des alliances qui te font briller, une relation qui rayonne.

**Domaine activé** : Maison 7 — Tes partenariats doivent nourrir ton cœur ET ton besoin de reconnaissance. Tu donnes généreusement mais tu veux aussi être célébré·e et admiré·e.

**Ton approche instinctive** : Le Lion te pousse à créer des relations magnifiques, à être généreux·se et loyal·e, à attendre que ton partenaire te traite royalement en retour.

**Tensions possibles** : Le besoin de reconnaissance peut contaminer l'amour. Tu risques de choisir des partenaires pour leur image plutôt que leur cœur, ou de te sentir diminué·e dans l'ombre de l'autre.

**Conseil clé** : Aimer depuis ton cœur généreux authentique, choisir des partenaires qui honorent ta valeur intrinsèque.""",
        'weekly_advice': {
            'week_1': "Choisis des alliances qui célèbrent ta véritable nature.",
            'week_2': "Donne généreusement sans attendre d'applaudissements.",
            'week_3': "Rayonne dans tes relations sans chercher à dominer.",
            'week_4': "Célèbre la royauté partagée dans tes partenariats."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Service mutuel**

Ta Lune en Cancer en Maison 7 fait de tes relations un besoin de sécurité émotionnelle. L'Ascendant Vierge ajoute du perfectionnisme : tu veux des partenariats utiles, fonctionnels, où chacun sert l'autre avec dévouement.

**Domaine activé** : Maison 7 — Tes partenariats sont des projets d'amélioration mutuelle. Tu analyses, tu optimises, tu cherches à créer des relations qui fonctionnent impeccablement.

**Ton approche instinctive** : La Vierge te fait servir tes partenaires méticuleusement, parfois trop. Tu peux devenir hypercritique des imperfections de la relation ou te sacrifier en croyant que c'est de l'amour.

**Tensions possibles** : Le perfectionnisme relationnel peut empêcher l'intimité vraie. Tu risques de critiquer l'autre au lieu de l'accepter, ou de te perdre dans le service jusqu'à l'épuisement.

**Conseil clé** : Accepter l'imperfection humaine dans les relations, servir sans se sacrifier, aimer l'autre tel qu'il est.""",
        'weekly_advice': {
            'week_1': "Identifie où tu critiques au lieu d'aimer.",
            'week_2': "Sers tes partenaires depuis l'amour, pas depuis le devoir anxieux.",
            'week_3': "Accepte une imperfection relationnelle avec grâce.",
            'week_4': "Célèbre les relations qui évoluent imparfaitement ensemble."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie fusionnelle**

Ta Lune en Cancer en Maison 7 fait de tes relations ton besoin émotionnel central. L'Ascendant Balance, maître naturel de cette maison, amplifie tout : tu existes à travers tes partenariats, tu cherches l'harmonie parfaite, l'équilibre idéal.

**Domaine activé** : Maison 7 — Double énergie relationnelle : tu es fait·e pour le partenariat. Ta sécurité émotionnelle dépend de la qualité de tes alliances, de l'harmonie que tu y trouves.

**Ton approche instinctive** : La Balance te pousse à chercher l'équilibre parfait, à sacrifier tes besoins pour maintenir la paix, à te définir entièrement par tes relations.

**Tensions possibles** : La dépendance relationnelle peut te faire perdre ton identité. Tu risques de ne plus savoir qui tu es sans l'autre, de sacrifier ton authenticité pour plaire.

**Conseil clé** : Construire des relations équilibrées qui incluent ton individualité, créer l'harmonie sans te perdre dedans.""",
        'weekly_advice': {
            'week_1': "Identifie qui tu es indépendamment de tes relations.",
            'week_2': "Crée de l'harmonie authentique basée sur la vérité mutuelle.",
            'week_3': "Équilibre tes besoins et ceux de tes partenaires honnêtement.",
            'week_4': "Célèbre les relations où tu peux être pleinement toi-même."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Fusion intense**

Ta Lune en Cancer en Maison 7 fait de tes relations ton besoin de sécurité émotionnelle. L'Ascendant Scorpion intensifie tout : tu veux la fusion totale, la transformation par l'autre, des partenariats qui touchent l'âme.

**Domaine activé** : Maison 7 — Double eau sur les relations : tes partenariats sont des plongées dans les profondeurs. Tu ne fais pas dans la superficialité, c'est tout ou rien, fusion ou solitude.

**Ton approche instinctive** : Le Scorpion te pousse à t'investir totalement, à tout partager, à transformer et être transformé·e par l'autre. Cette intensité peut être magnétique ou étouffante.

**Tensions possibles** : L'obsession relationnelle peut devenir toxique. Tu risques de devenir possessif·ve, manipulateur·rice, ou de créer des dynamiques de pouvoir destructrices.

**Conseil clé** : Aimer profondément sans posséder, transformer ensemble sans détruire les individualités.""",
        'weekly_advice': {
            'week_1': "Explore une vérité profonde avec un·e partenaire clé.",
            'week_2': "Libère le besoin de contrôler dans tes relations.",
            'week_3': "Transforme un pattern relationnel toxique.",
            'week_4': "Célèbre la puissance transformatrice de tes partenariats."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Partenaire libre**

Ta Lune en Cancer en Maison 7 fait de tes relations ton besoin de sécurité émotionnelle. L'Ascendant Sagittaire crée un paradoxe : tu veux l'engagement profond ET la liberté totale, l'intimité ET l'aventure.

**Domaine activé** : Maison 7 — Tes partenariats doivent nourrir ton besoin de foyer tout en respectant ta soif de croissance. Tu cherches des allié·es qui voyagent avec toi, pas qui t'attachent.

**Ton approche instinctive** : Le Sagittaire te pousse à chercher des partenaires qui élargissent ton monde, qui enseignent et apprennent avec toi, qui comprennent ton besoin d'espace.

**Tensions possibles** : Le conflit entre attachement et liberté peut déchirer tes relations. Tu risques de fuir l'engagement par peur d'être piégé·e, ou de te sentir coupable de ton besoin d'autonomie.

**Conseil clé** : Comprendre que l'engagement véritable inclut la liberté, créer des partenariats qui grandissent ensemble.""",
        'weekly_advice': {
            'week_1': "Explore comment tes relations peuvent nourrir ta croissance.",
            'week_2': "Engage-toi profondément sans sacrifier ton besoin d'espace.",
            'week_3': "Trouve des partenaires qui célèbrent ton indépendance.",
            'week_4': "Célèbre les relations qui t'ancrent ET te libèrent."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Engagement mûr**

Ta Lune en Cancer en Maison 7 active l'axe Cancer-Capricorne de plein fouet : besoin émotionnel de fusion contre besoin de structure et de maîtrise. Tes relations deviennent un terrain de maturation émotionnelle.

**Domaine activé** : Maison 7 — Opposition fondamentale : tu cherches la sécurité émotionnelle dans des partenariats structurés et durables. L'amour devient un engagement sérieux, une construction patiente.

**Ton approche instinctive** : Le Capricorne te pousse à choisir tes partenaires avec sagesse, à construire des alliances qui durent, à assumer les responsabilités relationnelles avec maturité.

**Tensions possibles** : Le contrôle émotionnel peut créer de la distance. Tu risques de traiter tes relations comme des contrats, de refouler tes besoins pour paraître fort·e, ou de porter le poids du partenariat seul·e.

**Conseil clé** : Équilibrer engagement mature et vulnérabilité émotionnelle, construire sans contrôler.""",
        'weekly_advice': {
            'week_1': "Engage-toi dans une relation avec sérieux ET avec cœur.",
            'week_2': "Assume tes responsabilités sans étouffer la spontanéité.",
            'week_3': "Permets-toi la vulnérabilité dans le partenariat.",
            'week_4': "Célèbre la maturité émotionnelle de tes alliances."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Alliance unique**

Ta Lune en Cancer en Maison 7 fait de tes relations ton besoin de sécurité émotionnelle. L'Ascendant Verseau révolutionne le partenariat : tu veux des alliances non-conventionnelles, une intimité qui respecte ton originalité.

**Domaine activé** : Maison 7 — Opposition Cancer-Verseau : tu cherches la fusion émotionnelle dans des formes relationnelles libres. Tes partenariats défient peut-être les normes sociales.

**Ton approche instinctive** : Le Verseau te pousse à créer des relations égalitaires, intellectuellement stimulantes, qui honorent l'individualité de chacun·e tout en créant du lien.

**Tensions possibles** : Le conflit entre besoin d'intimité et besoin de liberté peut créer de l'instabilité. Tu risques de fuir l'attachement par peur de perdre ton unicité.

**Conseil clé** : Créer des partenariats authentiques qui célèbrent à la fois l'intimité et l'individualité.""",
        'weekly_advice': {
            'week_1': "Définis ce que partenariat signifie authentiquement pour toi.",
            'week_2': "Trouve des allié·es qui célèbrent ton originalité.",
            'week_3': "Équilibre intimité émotionnelle et liberté individuelle.",
            'week_4': "Célèbre la forme unique de tes relations."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Amour transcendant**

Ta Lune en Cancer en Maison 7 fait de tes relations ton besoin émotionnel central. L'Ascendant Poissons dissout les frontières : tu veux l'amour absolu, la fusion spirituelle, des partenariats qui transcendent l'ego.

**Domaine activé** : Maison 7 — Triple eau sur les relations : tes partenariats sont des océans de fusion. Tu ne sais plus où tu finis et où l'autre commence. L'amour devient une expérience mystique.

**Ton approche instinctive** : Le Poissons te pousse à te sacrifier pour l'amour, à dissoudre ton identité dans le partenariat, à chercher l'union spirituelle par-delà la forme.

**Tensions possibles** : La perte totale de limites peut te détruire. Tu risques de te sacrifier complètement, de te faire exploiter émotionnellement, ou de perdre toute individualité dans la fusion.

**Conseil clé** : Aimer transcendantalement tout en gardant une ancre dans ton identité propre, fusionner sans disparaître.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te perds complètement dans tes relations.",
            'week_2': "Crée des frontières sacrées qui protègent ton individualité.",
            'week_3': "Aime spirituellement sans te sacrifier matériellement.",
            'week_4': "Célèbre la profondeur mystique de tes partenariats."
        }
    },

    # ==================== MAISON 8 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Transformation courageuse**

Ta Lune en Cancer en Maison 8 plonge tes émotions dans les profondeurs de la transformation. Tu ressens intensément les crises, les pertes, les renaissances. L'Ascendant Bélier ajoute du courage : tu affrontes les abysses avec combativité.

**Domaine activé** : Maison 8 — Tes émotions touchent la mort, la sexualité, les ressources partagées, les secrets. Tu vis tes sentiments comme des transformations radicales qui te forgent.

**Ton approche instinctive** : Le Bélier te pousse à affronter directement ce qui fait peur, à initier les transformations nécessaires, à combattre pour ta renaissance émotionnelle.

**Tensions possibles** : L'agressivité peut contaminer l'intimité. Tu risques de créer des crises pour te sentir vivant·e, ou de combattre contre la vulnérabilité qu'exige la vraie transformation.

**Conseil clé** : Utiliser ton courage pour traverser les morts nécessaires, pas pour les provoquer ou les éviter.""",
        'weekly_advice': {
            'week_1': "Affronte une peur profonde que tu as évitée.",
            'week_2': "Initie une transformation émotionnelle nécessaire.",
            'week_3': "Traverse une crise avec courage plutôt que d'attaquer.",
            'week_4': "Célèbre ta capacité à renaître de tes cendres."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Transformation ancrée**

Ta Lune en Cancer en Maison 8 te connecte aux profondeurs émotionnelles de la transformation. L'Ascendant Taureau cherche la stabilité : tu veux transformer lentement, solidement, en gardant un ancrage dans le concret.

**Domaine activé** : Maison 8 — Tes ressources partagées, ton intimité, tes transformations ont besoin de sécurité. Tu explores les profondeurs mais tu veux un port d'attache stable.

**Ton approche instinctive** : Le Taureau te fait résister au changement profond, mais quand tu t'engages dans une transformation, tu vas jusqu'au bout avec patience et ténacité.

**Tensions possibles** : La résistance à la mort symbolique peut bloquer ta croissance. Tu risques de t'accrocher à ce qui doit mourir, ou de vivre les transformations comme des pertes terrifiantes.

**Conseil clé** : Accepter que la vraie sécurité vient de ta capacité à traverser les transformations, pas de leur évitement.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit mourir pour que tu puisses renaître.",
            'week_2': "Ancre-toi dans ton corps pendant les transformations émotionnelles.",
            'week_3': "Lâche prise sur quelque chose que tu retiens par peur.",
            'week_4': "Célèbre ta capacité à te transformer tout en restant toi-même."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Mystère verbalisé**

Ta Lune en Cancer en Maison 8 te connecte aux profondeurs émotionnelles mystérieuses. L'Ascendant Gémeaux veut comprendre et communiquer : tu explores les abysses par les mots, tu intellectualises tes transformations.

**Domaine activé** : Maison 8 — Tes transformations passent par la communication, l'apprentissage, le partage des secrets. Tu mets des mots sur l'indicible pour le comprendre.

**Ton approche instinctive** : Le Gémeaux te fait parler de tes peurs, lire sur la mort, explorer intellectuellement la sexualité. Tu peux utiliser l'analyse pour éviter de vraiment ressentir les profondeurs.

**Tensions possibles** : La fuite intellectuelle peut t'empêcher la vraie transformation. Tu risques de parler de tes émotions au lieu de les vivre, ou de disperser ton énergie de transformation.

**Conseil clé** : Équilibrer compréhension mentale et ressenti viscéral, verbaliser après avoir traversé, pas à la place.""",
        'weekly_advice': {
            'week_1': "Explore une peur profonde en l'étudiant d'abord intellectuellement.",
            'week_2': "Puis plonge dans le ressenti sans les mots.",
            'week_3': "Partage un secret ou une vérité cachée avec quelqu'un.",
            'week_4': "Célèbre ta capacité à comprendre et vivre les mystères."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Abysses maternels**

Triple Cancer en Maison 8 : tes émotions plongent dans les profondeurs ancestrales, les mémoires transgénérationnelles, les secrets familiaux. Tu portes les transformations de toute ta lignée.

**Domaine activé** : Maison 8 — L'intimité la plus profonde, la mort, la renaissance sont ton territoire émotionnel. Tu ressens les fantômes du passé, les blessures héritées, les dons ancestraux.

**Ton approche instinctive** : Triple eau sur la transformation : tu traverses les crises émotionnelles comme des morts et renaissances. Ton intuition psychique est puissante mais peut être écrasante.

**Tensions possibles** : La fusion avec les morts symboliques peut te noyer. Tu risques de porter les traumatismes de ta lignée, de te perdre dans les abysses, ou de revivre sans cesse les mêmes patterns de mort-renaissance.

**Conseil clé** : Guérir les blessures ancestrales sans t'identifier à elles, honorer les morts sans rester avec eux.""",
        'weekly_advice': {
            'week_1': "Explore un pattern familial qui demande transformation.",
            'week_2': "Laisse mourir ce qui n'est pas à toi dans ton héritage.",
            'week_3': "Protège-toi psychiquement des énergies lourdes.",
            'week_4': "Célèbre ta capacité unique à transformer les lignées."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Renaissance rayonnante**

Ta Lune en Cancer en Maison 8 te plonge dans les transformations émotionnelles profondes. L'Ascendant Lion veut briller même dans les ténèbres : tu cherches la grandeur dans ta renaissance, la fierté dans ton courage face aux abysses.

**Domaine activé** : Maison 8 — Tes transformations doivent être significatives, visibles, célébrées. Tu veux renaître magnifiquement de tes crises, montrer ta puissance émotionnelle.

**Ton approche instinctive** : Le Lion te pousse à créer du sens et de la beauté même dans la mort symbolique, à transformer tes blessures en force rayonnante.

**Tensions possibles** : Le besoin de reconnaissance peut contaminer l'intimité. Tu risques de dramatiser tes crises pour l'attention, ou de refuser la vulnérabilité que demande la vraie transformation.

**Conseil clé** : Traverser les abysses authentiquement sans chercher d'applaudissements, briller après la renaissance plutôt que pendant la crise.""",
        'weekly_advice': {
            'week_1': "Affronte une transformation avec courage et authenticité.",
            'week_2': "Trouve la force dans ta vulnérabilité, pas dans ta façade.",
            'week_3': "Renais de tes cendres sans chercher de public.",
            'week_4': "Célèbre la magnificence de ta renaissance accomplie."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Purification profonde**

Ta Lune en Cancer en Maison 8 te connecte aux profondeurs émotionnelles et aux transformations. L'Ascendant Vierge veut purifier : tu analyses tes crises, tu cherches à améliorer ta gestion des transformations, à rendre tes renaissances utiles.

**Domaine activé** : Maison 8 — Tes transformations deviennent des projets d'amélioration. Tu veux comprendre tes patterns de crise, optimiser tes ressources partagées, perfectionner ton intimité.

**Ton approche instinctive** : La Vierge te fait analyser chaque transformation, chercher les leçons, créer des méthodes pour mieux gérer les crises futures.

**Tensions possibles** : L'analyse peut t'empêcher de vraiment traverser. Tu risques de critiquer ton processus de transformation au lieu de le vivre, ou de vouloir contrôler ce qui doit rester mystérieux.

**Conseil clé** : Accepter que certaines transformations échappent au contrôle, lâcher prise sur la perfection dans les abysses.""",
        'weekly_advice': {
            'week_1': "Identifie un pattern de crise que tu peux améliorer.",
            'week_2': "Traverse une transformation sans l'analyser sur le moment.",
            'week_3': "Sers les autres depuis ta sagesse acquise dans les abysses.",
            'week_4': "Célèbre la sagesse pratique née de tes transformations."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre des profondeurs**

Ta Lune en Cancer en Maison 8 te plonge dans les transformations émotionnelles intenses. L'Ascendant Balance cherche l'harmonie : tu veux transformer avec élégance, équilibrer les ressources partagées, créer de la beauté même dans les crises.

**Domaine activé** : Maison 8 — Tes transformations passent par tes relations intimes. L'intimité profonde, les ressources partagées, les crises relationnelles sont tes terrains de renaissance.

**Ton approche instinctive** : La Balance te pousse à chercher l'équité dans l'intimité, à transformer les relations plutôt que de les quitter, à maintenir l'harmonie même dans les profondeurs.

**Tensions possibles** : Le besoin d'harmonie peut t'empêcher les transformations nécessaires. Tu risques d'éviter les crises salutaires pour maintenir la paix, ou de perdre ton équilibre dans la fusion intime.

**Conseil clé** : Accepter que la vraie harmonie émerge après la transformation, pas avant ou pendant.""",
        'weekly_advice': {
            'week_1': "Engage une transformation relationnelle difficile mais nécessaire.",
            'week_2': "Équilibre honnêtement les ressources partagées.",
            'week_3': "Trouve la beauté dans tes blessures transformées.",
            'week_4': "Célèbre l'harmonie profonde née de tes crises."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Alchimie totale**

Ta Lune en Cancer en Maison 8 te plonge dans les profondeurs de la transformation. L'Ascendant Scorpion, maître naturel de cette maison, amplifie tout : c'est LE placement de l'alchimiste émotionnel, du phénix qui renaît sans cesse.

**Domaine activé** : Maison 8 — Double énergie scorpionnique : tu vis dans les profondeurs. Les crises, la mort, la sexualité, les secrets, les transformations radicales sont ton élément naturel.

**Ton approche instinctive** : Le Scorpion te pousse à tout ressentir jusqu'au bout, à transformer chaque blessure en pouvoir, à plonger dans les abysses sans peur et en ressortir régénéré·e.

**Tensions possibles** : L'intensité constante peut te consumer. Tu risques de créer des crises pour te sentir vivant·e, de devenir obsédé·e par le contrôle, ou de brûler dans tes propres transformations.

**Conseil clé** : Utiliser ton pouvoir transformateur pour guérir et créer, pas pour contrôler ou détruire.""",
        'weekly_advice': {
            'week_1': "Plonge dans une transformation que tu as évitée.",
            'week_2': "Transmute une blessure profonde en pouvoir créatif.",
            'week_3': "Libère le besoin de tout contrôler dans l'intimité.",
            'week_4': "Célèbre ta puissance alchimique unique."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Sagesse des abysses**

Ta Lune en Cancer en Maison 8 te connecte aux profondeurs émotionnelles et aux transformations. L'Ascendant Sagittaire cherche le sens : tu veux comprendre philosophiquement tes crises, transformer tes blessures en sagesse enseignable.

**Domaine activé** : Maison 8 — Tes transformations doivent avoir un sens plus grand. Tu explores les mystères pour en extraire des vérités universelles, tu traverses les crises comme des quêtes initiatiques.

**Ton approche instinctive** : Le Sagittaire te pousse à donner du sens à tes transformations, à enseigner ce que tu as appris dans les abysses, à garder l'optimisme même dans les ténèbres.

**Tensions possibles** : Le besoin de sens peut te faire éviter la douleur brute. Tu risques de philosopher sur tes crises au lieu de les vivre, ou de fuir l'intimité profonde par besoin de liberté.

**Conseil clé** : Traverser pleinement avant de chercher le sens, accepter que certaines transformations restent mystérieuses.""",
        'weekly_advice': {
            'week_1': "Plonge dans une transformation sans chercher immédiatement le sens.",
            'week_2': "Explore une peur profonde comme une quête de vérité.",
            'week_3': "Partage la sagesse acquise dans tes crises passées.",
            'week_4': "Célèbre la croissance née de tes transformations."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Transformation maîtrisée**

Ta Lune en Cancer en Maison 8 te plonge dans les profondeurs émotionnelles. L'Ascendant Capricorne oppose sa structure : tu veux contrôler tes transformations, gérer tes crises avec maîtrise, construire sur tes renaissances.

**Domaine activé** : Maison 8 — Opposition Cancer-Capricorne : tu ressens les abysses intensément mais tu cherches à les structurer, à en extraire quelque chose de durable et utile.

**Ton approche instinctive** : Le Capricorne te pousse à transformer avec discipline, à construire ta puissance sur tes cicatrices, à utiliser tes crises comme des opportunités de maturation.

**Tensions possibles** : Le contrôle excessif peut bloquer la transformation. Tu risques de refouler les émotions profondes, de vouloir gérer rationnellement ce qui doit être ressenti, ou de porter seul·e des fardeaux trop lourds.

**Conseil clé** : Lâcher prise sur le contrôle dans les moments de transformation, accepter la vulnérabilité comme une force mature.""",
        'weekly_advice': {
            'week_1': "Permets-toi de perdre le contrôle dans une transformation nécessaire.",
            'week_2': "Construis sur une blessure guérie plutôt que refoulée.",
            'week_3': "Assume une responsabilité transformatrice avec maturité.",
            'week_4': "Célèbre la sagesse et la puissance nées de tes crises."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolution intérieure**

Ta Lune en Cancer en Maison 8 te connecte aux profondeurs émotionnelles personnelles. L'Ascendant Verseau universalise : tu veux transformer le collectif à travers tes transformations personnelles, révolutionner l'approche des crises.

**Domaine activé** : Maison 8 — Opposition Cancer-Verseau : tu ressens profondément mais tu détaches intellectuellement. Tes transformations servent une cause plus grande que toi.

**Ton approche instinctive** : Le Verseau te fait prendre de la distance avec tes propres crises pour mieux les comprendre, innover dans ta façon de gérer l'intimité et les transformations.

**Tensions possibles** : Le détachement peut t'empêcher la vraie transformation. Tu risques d'intellectualiser tes blessures au lieu de les guérir, ou de sacrifier ton intimité personnelle pour une cause abstraite.

**Conseil clé** : Honorer tes besoins émotionnels profonds tout en servant ta vision collective, transformer authentiquement avant d'universaliser.""",
        'weekly_advice': {
            'week_1': "Plonge dans une émotion profonde sans la détacher intellectuellement.",
            'week_2': "Explore comment ta transformation personnelle peut servir le collectif.",
            'week_3': "Révolutionne ta façon d'aborder l'intimité et les crises.",
            'week_4': "Célèbre ton originalité dans ta façon de te transformer."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 8, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution sacrée**

Ta Lune en Cancer en Maison 8 te plonge dans les profondeurs de la transformation. L'Ascendant Poissons dissout toutes les frontières : tes transformations sont des dissolutions mystiques, des morts de l'ego, des renaissances spirituelles.

**Domaine activé** : Maison 8 — Triple eau sur la transformation : tu te noies et renais dans un océan de métamorphoses. Les limites entre vie et mort, soi et autre, matériel et spirituel s'effacent.

**Ton approche instinctive** : Le Poissons te fait traverser les transformations comme des expériences transcendantes, dissoudre ton identité pour renaître différemment, fusionner avec le mystère.

**Tensions possibles** : La perte totale de limites peut te détruire. Tu risques de te noyer dans les crises, de fuir dans le déni ou les addictions, ou de porter les blessures de tout le monde.

**Conseil clé** : Transformer spirituellement tout en gardant une ancre dans la réalité, mourir symboliquement sans se perdre totalement.""",
        'weekly_advice': {
            'week_1': "Plonge dans une transformation avec confiance spirituelle.",
            'week_2': "Protège-toi psychiquement pendant les crises.",
            'week_3': "Utilise des pratiques spirituelles pour intégrer tes transformations.",
            'week_4': "Célèbre ta capacité unique à renaître mystiquement."
        }
    },

    # ==================== MAISON 9 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Quête protectrice**

Ta Lune en Cancer en Maison 9 cherche un sens émotionnel au monde. Tu veux appartenir à une philosophie, une croyance, une vision qui te nourrit comme une famille spirituelle. L'Ascendant Bélier ajoute de l'ardeur : tu pars en quête avec passion.

**Domaine activé** : Maison 9 — Ton besoin de sens, d'expansion, de voyage est teinté d'émotion. Tu explores le monde pour trouver un foyer spirituel, une vérité qui te sécurise.

**Ton approche instinctive** : Le Bélier te pousse à partir impulsivement en quête, à défendre tes croyances comme ta famille, à conquérir de nouveaux horizons avec enthousiasme.

**Tensions possibles** : Le dogmatisme émotionnel peut te rigidifier. Tu risques de t'accrocher à tes croyances par besoin de sécurité, ou de combattre pour des vérités qui ne sont que tes projections.

**Conseil clé** : Chercher le sens avec courage tout en restant ouvert·e à remettre en question tes certitudes.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie ou croyance qui résonne avec ton cœur.",
            'week_2': "Pars en quête physique ou mentale d'un sens plus grand.",
            'week_3': "Questionne une croyance que tu défends par habitude.",
            'week_4': "Célèbre ta capacité à trouver du sens dans l'aventure."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sagesse enracinée**

Ta Lune en Cancer en Maison 9 cherche une philosophie qui nourrit ton âme. L'Ascendant Taureau veut que cette sagesse soit concrète, pratique, ancrée dans la réalité tangible.

**Domaine activé** : Maison 9 — Ton expansion intellectuelle et spirituelle doit être solide, éprouvée, durable. Tu construis ta vision du monde lentement mais sûrement.

**Ton approche instinctive** : Le Taureau te fait chercher des vérités stables, des traditions réconfortantes, une sagesse qui se transmet patiemment à travers les générations.

**Tensions possibles** : La résistance au changement peut limiter ta croissance. Tu risques de t'accrocher à des croyances confortables même quand elles ne servent plus, ou de refuser d'explorer de nouveaux horizons.

**Conseil clé** : Construire ta sagesse solidement tout en restant ouvert·e à de nouvelles perspectives.""",
        'weekly_advice': {
            'week_1': "Ancre ta spiritualité dans des pratiques concrètes quotidiennes.",
            'week_2': "Explore une tradition ou sagesse qui a résisté au temps.",
            'week_3': "Ouvre-toi à une idée nouvelle qui challenge tes certitudes.",
            'week_4': "Célèbre la profondeur de ta compréhension du monde."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Curiosité philosophique**

Ta Lune en Cancer en Maison 9 cherche une vision du monde qui nourrit ton cœur. L'Ascendant Gémeaux ajoute de la curiosité : tu explores mille philosophies, tu voyages mentalement partout, tu cherches le sens à travers l'apprentissage.

**Domaine activé** : Maison 9 — Ton expansion passe par la communication et l'échange. Tu veux comprendre toutes les perspectives, connecter différentes sagesses, créer ton propre système de pensée.

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre les croyances, lire sur toutes les philosophies, voyager pour apprendre plutôt que pour vivre.

**Tensions possibles** : La dispersion peut t'empêcher l'approfondissement. Tu risques de rester en surface de mille sagesses sans jamais en incarner aucune vraiment.

**Conseil clé** : Équilibrer exploration intellectuelle et incarnation profonde, choisir quelques vérités et les vivre.""",
        'weekly_advice': {
            'week_1': "Explore plusieurs perspectives sur un même sujet philosophique.",
            'week_2': "Choisis une sagesse et engage-toi à la pratiquer.",
            'week_3': "Partage ce que tu apprends avec quelqu'un d'ouvert.",
            'week_4': "Célèbre ta capacité à connecter différentes visions du monde."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Patrie spirituelle**

Triple Cancer en Maison 9 : tu cherches un foyer spirituel, une famille philosophique, une patrie de sens. Tes croyances doivent te nourrir émotionnellement, te protéger, te donner un sentiment d'appartenance.

**Domaine activé** : Maison 9 — Ta quête de sens est viscérale. Tu veux une vision du monde qui te berce, une spiritualité qui te materne, une philosophie qui te donne des racines cosmiques.

**Ton approche instinctive** : Triple eau sur le sens : tu ressens intuitivement les vérités avant de les comprendre intellectuellement. Ta spiritualité est profondément émotionnelle et personnelle.

**Tensions possibles** : L'attachement émotionnel aux croyances peut devenir dogmatique. Tu risques de rejeter toute perspective qui menace ta sécurité spirituelle, ou de te perdre dans la nostalgie d'une sagesse idéalisée.

**Conseil clé** : Honorer ton besoin de sens émotionnel tout en restant ouvert·e à l'évolution de tes croyances.""",
        'weekly_advice': {
            'week_1': "Identifie les croyances qui te nourrissent vraiment.",
            'week_2': "Crée un rituel spirituel qui te fait sentir chez toi dans l'univers.",
            'week_3': "Questionne une croyance que tu gardes par habitude émotionnelle.",
            'week_4': "Célèbre ta patrie spirituelle intérieure."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Vérité rayonnante**

Ta Lune en Cancer en Maison 9 cherche une philosophie qui nourrit ton âme. L'Ascendant Lion veut que cette vérité te fasse briller : tu cherches une vision du monde grandiose, inspirante, digne d'être partagée avec fierté.

**Domaine activé** : Maison 9 — Ton sens, tes croyances, ton expansion doivent être magnifiques, généreux, rayonnants. Tu veux une sagesse que tu peux enseigner avec cœur et panache.

**Ton approche instinctive** : Le Lion te pousse à incarner tes croyances avec grandeur, à inspirer les autres par ta vision du monde, à créer du sens depuis ton cœur généreux.

**Tensions possibles** : Le besoin de reconnaissance peut contaminer ta quête. Tu risques de choisir des croyances impressionnantes plutôt qu'authentiques, ou de prêcher plutôt que de vivre ta sagesse.

**Conseil clé** : Chercher la vérité pour toi-même d'abord, rayonner naturellement plutôt que performer.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie qui résonne avec ton cœur authentique.",
            'week_2': "Partage ta vision du monde généreusement, sans chercher l'applaudissement.",
            'week_3': "Incarne ta sagesse avec fierté humble.",
            'week_4': "Célèbre le rayonnement naturel de ta vérité vécue."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Sagesse pratique**

Ta Lune en Cancer en Maison 9 cherche un sens émotionnel au monde. L'Ascendant Vierge veut que cette sagesse soit utile, pratique, applicable concrètement au quotidien.

**Domaine activé** : Maison 9 — Ton expansion intellectuelle et spirituelle doit servir à quelque chose. Tu cherches une philosophie qui améliore la vie, une sagesse qui peut aider concrètement.

**Ton approche instinctive** : La Vierge te fait analyser les croyances, trier les philosophies, chercher la vérité qui fonctionne vraiment plutôt que celle qui sonne bien.

**Tensions possibles** : Le perfectionnisme peut t'empêcher d'embrasser une foi. Tu risques de critiquer toutes les philosophies sans jamais en adopter une, ou de rendre ta spiritualité anxieuse et rigide.

**Conseil clé** : Accepter que la sagesse soit imparfaite et mystérieuse, pas juste pratique et claire.""",
        'weekly_advice': {
            'week_1': "Trouve une pratique spirituelle simple mais efficace.",
            'week_2': "Applique une sagesse philosophique à un problème concret.",
            'week_3': "Lâche prise sur le besoin de tout comprendre rationnellement.",
            'week_4': "Célèbre la sagesse pratique née de ton expérience."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie universelle**

Ta Lune en Cancer en Maison 9 cherche une philosophie qui nourrit ton cœur. L'Ascendant Balance veut une vision du monde équilibrée, harmonieuse, qui crée des ponts entre les perspectives.

**Domaine activé** : Maison 9 — Ton expansion cherche l'équité, la beauté, l'harmonie. Tu veux une sagesse qui unit plutôt que divise, qui crée de la paix entre les croyances.

**Ton approche instinctive** : La Balance te fait chercher le consensus philosophique, peser toutes les perspectives, créer ta propre synthèse équilibrée.

**Tensions possibles** : Le besoin d'harmonie peut diluer ta vérité. Tu risques de ne jamais prendre position par peur d'offenser, ou de perdre ton authenticité dans le compromis.

**Conseil clé** : Honorer ta propre vérité tout en respectant celle des autres, créer l'harmonie sans sacrifier l'authenticité.""",
        'weekly_advice': {
            'week_1': "Explore comment différentes philosophies peuvent coexister harmonieusement.",
            'week_2': "Prends position sur une croyance importante pour toi.",
            'week_3': "Crée des ponts entre des perspectives opposées.",
            'week_4': "Célèbre ta capacité à trouver la beauté dans toutes les sagesses."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité profonde**

Ta Lune en Cancer en Maison 9 cherche un sens émotionnel profond. L'Ascendant Scorpion intensifie la quête : tu veux la vérité absolue, la sagesse qui transforme, les mystères qui touchent l'âme.

**Domaine activé** : Maison 9 — Double eau sur le sens : ta quête philosophique est une quête d'âme. Tu ne te contentes pas de croyances superficielles, tu veux les vérités qui brûlent et transforment.

**Ton approche instinctive** : Le Scorpion te pousse à plonger dans les mystères, à chercher la vérité cachée sous les dogmes, à transformer ta vision du monde radicalement.

**Tensions possibles** : L'obsession de la vérité absolue peut te rigidifier. Tu risques de devenir fanatique, de rejeter violemment ce qui ne correspond pas à ta vision, ou de te perdre dans des croyances extrêmes.

**Conseil clé** : Chercher la vérité profonde tout en acceptant que le mystère reste toujours en partie insondable.""",
        'weekly_advice': {
            'week_1': "Plonge dans un mystère philosophique ou spirituel qui t'appelle.",
            'week_2': "Transforme une croyance limitante en vision puissante.",
            'week_3': "Explore les zones d'ombre de tes propres certitudes.",
            'week_4': "Célèbre la profondeur de ta quête et ta sagesse transformée."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventure spirituelle**

Ta Lune en Cancer en Maison 9 cherche un sens qui nourrit ton cœur. L'Ascendant Sagittaire, maître naturel de cette maison, amplifie la quête : tu es un·e chercheur·se de vérité, un·e voyageur·se de l'âme, un·e explorateur·rice du sens.

**Domaine activé** : Maison 9 — Double énergie sagittarienne : l'expansion philosophique et spirituelle est ton élément naturel. Tu cherches, tu explores, tu enseignes, tu grandis constamment.

**Ton approche instinctive** : Le Sagittaire te pousse à voyager pour trouver du sens, à étudier toutes les sagesses, à enseigner ce que tu apprends, à garder l'optimisme dans ta quête.

**Tensions possibles** : La quête sans fin peut t'empêcher l'enracinement. Tu risques de fuir l'intimité émotionnelle par l'expansion constante, ou de rester en surface de mille sagesses.

**Conseil clé** : Équilibrer exploration et intégration, voyager tout en gardant un foyer intérieur.""",
        'weekly_advice': {
            'week_1': "Pars en quête physique ou mentale d'une nouvelle perspective.",
            'week_2': "Enseigne ou partage une sagesse que tu as intégrée.",
            'week_3': "Ancre-toi dans une pratique spirituelle régulière.",
            'week_4': "Célèbre ta croissance constante et ton optimisme."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Sagesse structurée**

Ta Lune en Cancer en Maison 9 cherche un sens émotionnel au monde. L'Ascendant Capricorne oppose sa structure : tu veux une philosophie mature, pratique, qui se construit patiemment à travers l'expérience.

**Domaine activé** : Maison 9 — Opposition Cancer-Capricorne : tu ressens le besoin de sens profondément mais tu le construis méthodiquement. Ta sagesse naît de l'expérience vécue, pas des livres.

**Ton approche instinctive** : Le Capricorne te fait bâtir ta philosophie comme un édifice solide, respecter les traditions éprouvées, enseigner avec autorité gagnée par l'expérience.

**Tensions possibles** : Le contrôle peut rigidifier ta vision. Tu risques de rejeter toute sagesse qui ne correspond pas à ta structure mentale, ou de négliger ton besoin émotionnel de foi pour ta rationalité.

**Conseil clé** : Construire ta sagesse solidement tout en restant ouvert·e au mystère et à l'intuition.""",
        'weekly_advice': {
            'week_1': "Construis ta philosophie sur des expériences vécues, pas des théories.",
            'week_2': "Assume le rôle d'enseignant·e depuis ta maturité acquise.",
            'week_3': "Permets à ton cœur d'influencer ta vision rationnelle du monde.",
            'week_4': "Célèbre la sagesse profonde née de ton expérience."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Vision universelle**

Ta Lune en Cancer en Maison 9 cherche un sens qui nourrit ton cœur. L'Ascendant Verseau universalise ta quête : tu veux une philosophie qui serve l'humanité, une vision qui révolutionne, une sagesse collective.

**Domaine activé** : Maison 9 — Opposition Cancer-Verseau : tu cherches le sens personnel dans l'universel. Ta spiritualité peut être non-conventionnelle, ta philosophie orientée vers le progrès collectif.

**Ton approche instinctive** : Le Verseau te pousse à chercher des vérités innovantes, à questionner les dogmes, à créer ta propre philosophie originale qui sert une cause plus grande.

**Tensions possibles** : Le détachement peut te couper de ton besoin émotionnel de sens. Tu risques d'intellectualiser ta spiritualité au point de perdre son âme, ou de sacrifier ton bien-être pour un idéal abstrait.

**Conseil clé** : Honorer ton besoin personnel de sens tout en servant ta vision collective.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie ou spiritualité non-conventionnelle.",
            'week_2': "Connecte ta quête personnelle à une vision collective.",
            'week_3': "Reste ancré·e dans ton cœur malgré ton idéalisme.",
            'week_4': "Célèbre ton originalité philosophique unique."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 9, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Foi mystique**

Ta Lune en Cancer en Maison 9 cherche un sens émotionnel profond. L'Ascendant Poissons dissout les frontières : ta quête devient mystique, ta foi transcendante, ta spiritualité une dissolution dans le divin.

**Domaine activé** : Maison 9 — Triple eau sur le sens : ta philosophie est intuitive, ta spiritualité fusionnelle, ta sagesse reçue plutôt qu'apprise. Tu channels plus que tu ne penses.

**Ton approche instinctive** : Le Poissons te fait chercher l'union avec le tout, la dissolution de l'ego dans la compréhension universelle, la foi absolue au-delà de la raison.

**Tensions possibles** : Le manque de limites peut te faire perdre pied. Tu risques de te noyer dans le mysticisme, de fuir la réalité par la spiritualité, ou de devenir naïf·ve face aux charlatans.

**Conseil clé** : Cultiver ta foi transcendante tout en gardant les pieds sur terre, ouvrir ton cœur sans perdre ton discernement.""",
        'weekly_advice': {
            'week_1': "Plonge dans une expérience spirituelle profonde et intuitive.",
            'week_2': "Pratique la foi sans abandonner ta sagesse pratique.",
            'week_3': "Ancre ta spiritualité dans des actes concrets de compassion.",
            'week_4': "Célèbre ta connexion mystique unique avec le sens de la vie."
        }
    },

    # ==================== MAISON 10 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Carrière nourricière**

Ta Lune en Cancer en Maison 10 fait de ta carrière un espace de soin et de protection. L'Ascendant Bélier te pousse à conquérir ta place publique avec courage, à défendre férocement ta vocation et ceux que tu protèges professionnellement.

**Domaine activé** : Maison 10 — Ta réputation se construit sur ta capacité à prendre soin, à créer un environnement sécurisant, à nourrir les autres dans ton rôle professionnel. Tu es vu·e comme protecteur·rice.

**Ton approche instinctive** : Le Bélier te fait foncer pour protéger ton territoire professionnel, lancer des initiatives qui prennent soin des autres, défendre ta position avec passion.

**Tensions possibles** : L'agressivité peut nuire à ton image nourricière. Tu risques de surprotéger ton domaine au point de bloquer les collaborations, ou de prendre trop personnellement les critiques professionnelles.

**Conseil clé** : Utiliser ton courage pour servir ta vocation de soin, pas pour te battre contre le monde.""",
        'weekly_advice': {
            'week_1': "Identifie comment ta carrière peut nourrir les autres authentiquement.",
            'week_2': "Défends ta place professionnelle sans agressivité inutile.",
            'week_3': "Prends soin de ton image publique avec douceur et fermeté.",
            'week_4': "Célèbre ta capacité à être fort·e ET attentionné·e professionnellement."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Réputation solide**

Ta Lune en Cancer en Maison 10 te fait construire une carrière basée sur le soin et la sécurité. L'Ascendant Taureau amplifie ce besoin de stabilité : tu bâtis patiemment une réputation fiable, confortable, rassurante.

**Domaine activé** : Maison 10 — Ta vocation se construit lentement mais solidement. Tu es reconnu·e pour ta loyauté professionnelle, ta capacité à créer des structures durables qui protègent et nourrissent.

**Ton approche instinctive** : Le Taureau te fait persévérer dans ta carrière avec patience, valoriser la sécurité matérielle dans tes choix professionnels, créer de la beauté dans ton travail.

**Tensions possibles** : L'attachement au confort peut te bloquer dans une carrière sécurisante mais insatisfaisante. Tu risques de refuser tout changement professionnel par peur de l'instabilité.

**Conseil clé** : Construire ta sécurité professionnelle sans sacrifier ta croissance et ton épanouissement.""",
        'weekly_advice': {
            'week_1': "Bâtis ta réputation sur des bases solides et durables.",
            'week_2': "Valorise ta loyauté professionnelle comme atout majeur.",
            'week_3': "Accepte un changement de carrière si ton cœur l'appelle.",
            'week_4': "Célèbre la stabilité que tu apportes dans ton domaine."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Communication protectrice**

Ta Lune en Cancer en Maison 10 oriente ta carrière vers le soin des autres. L'Ascendant Gémeaux te pousse à communiquer ce soin : tu es un·e éducateur·rice, un·e communicant·e, quelqu'un qui nourrit par les mots et les idées.

**Domaine activé** : Maison 10 — Ta réputation se bâtit sur ta capacité à informer, éduquer, connecter les gens. Tu protèges par la transmission de savoir, tu nourris par le partage d'informations utiles.

**Ton approche instinctive** : Le Gémeaux te fait multiplier les projets professionnels, communiquer constamment, créer des réseaux de soin et d'échange, rester curieux·se dans ta vocation.

**Tensions possibles** : La dispersion peut nuire à ton impact. Tu risques de papillonner professionnellement sans construire de réputation solide, ou d'intellectualiser ton besoin de vraiment prendre soin.

**Conseil clé** : Utiliser ta polyvalence pour servir une vocation cohérente de soin et d'éducation.""",
        'weekly_advice': {
            'week_1': "Identifie comment ta communication peut nourrir les autres.",
            'week_2': "Concentre tes projets multiples autour d'une mission centrale.",
            'week_3': "Partage ton savoir avec générosité et protection.",
            'week_4': "Célèbre ta capacité à connecter et éduquer professionnellement."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Vocation maternelle**

Triple Cancer en Maison 10 : ta carrière EST ton espace de soin pur. Tu es vu·e publiquement comme le parent, le protecteur, le nourricier. Ta réputation se construit entièrement sur ta capacité émotionnelle.

**Domaine activé** : Maison 10 — Pure énergie nourricière dans ta vocation. Tu es peut-être thérapeute, soignant·e, éducateur·rice, ou tout métier où tu prends soin des autres comme d'une famille.

**Ton approche instinctive** : Triple eau : tu ressens les besoins professionnels intuitivement, tu protèges ton territoire comme un foyer, tu nourris tes collaborateurs comme des proches.

**Tensions possibles** : L'hypersensibilité aux critiques professionnelles peut te paralyser. Tu risques de prendre toute critique comme une attaque personnelle, ou de surprotéger ton domaine au détriment de la croissance.

**Conseil clé** : Honorer ta vocation de soin tout en développant des frontières professionnelles saines.""",
        'weekly_advice': {
            'week_1': "Assume pleinement ta vocation de prendre soin des autres.",
            'week_2': "Protège ton énergie professionnelle avec des limites claires.",
            'week_3': "Nourris-toi autant professionnellement que tu nourris les autres.",
            'week_4': "Célèbre ta réputation unique de protecteur·rice et nourricier·ère."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Leadership bienveillant**

Ta Lune en Cancer en Maison 10 te fait briller par ta capacité à prendre soin. L'Ascendant Lion amplifie ce rayonnement : tu es un·e leader généreux·se, un·e figure publique qui protège et inspire.

**Domaine activé** : Maison 10 — Ta réputation se construit sur ton charisme nourricier. Tu veux être reconnu·e pour ta capacité à élever les autres, à créer des espaces où chacun peut briller en sécurité.

**Ton approche instinctive** : Le Lion te pousse à diriger avec le cœur, à créer ta propre vision de leadership protecteur, à inspirer par ton exemple de générosité et de force.

**Tensions possibles** : L'ego peut corrompre ton intention de servir. Tu risques de chercher la reconnaissance plus que le service authentique, ou de confondre protection et contrôle.

**Conseil clé** : Diriger avec ton cœur généreux tout en restant humble dans ton service.""",
        'weekly_advice': {
            'week_1': "Assume ton rôle de leader protecteur avec fierté.",
            'week_2': "Inspire par ton exemple de force ET de sensibilité.",
            'week_3': "Vérifie que ta recherche de reconnaissance sert vraiment les autres.",
            'week_4': "Célèbre ton leadership unique qui élève et protège."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Service attentif**

Ta Lune en Cancer en Maison 10 oriente ta carrière vers le soin. L'Ascendant Vierge affine ce service : tu veux être utile concrètement, améliorer les choses, servir avec excellence et précision.

**Domaine activé** : Maison 10 — Ta réputation se construit sur ton service attentif aux détails. Tu es reconnu·e pour ta capacité à anticiper les besoins, à créer des systèmes qui protègent et soutiennent efficacement.

**Ton approche instinctive** : La Vierge te fait analyser comment mieux servir, perfectionner tes méthodes de soin, t'améliorer constamment dans ta vocation, rester humble dans ta contribution.

**Tensions possibles** : Le perfectionnisme peut te paralyser ou te rendre critique. Tu risques de t'épuiser à vouloir tout faire parfaitement, ou de juger durement ton propre service comme insuffisant.

**Conseil clé** : Servir avec excellence tout en acceptant l'imperfection humaine, la tienne et celle des autres.""",
        'weekly_advice': {
            'week_1': "Identifie comment affiner ton service pour mieux protéger.",
            'week_2': "Améliore tes systèmes de travail sans te perdre dans les détails.",
            'week_3': "Accepte que servir suffisamment bien est déjà extraordinaire.",
            'week_4': "Célèbre ton service attentif et précis dans le monde."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomatie protectrice**

Ta Lune en Cancer en Maison 10 fait de ta carrière un espace de soin. L'Ascendant Balance te pousse à créer l'harmonie : tu protèges par la médiation, tu nourris par la beauté et l'équilibre relationnel.

**Domaine activé** : Maison 10 — Ta réputation se construit sur ta capacité à créer des environnements professionnels harmonieux, à résoudre les conflits avec douceur, à protéger les relations.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre dans ton leadership, valoriser la collaboration, créer de la beauté dans ton domaine, préserver la paix tout en prenant soin.

**Tensions possibles** : Le besoin de plaire peut t'empêcher de protéger vraiment. Tu risques d'éviter les conflits nécessaires au détriment de ceux que tu dois défendre, ou de sacrifier tes besoins pour l'harmonie.

**Conseil clé** : Créer l'harmonie sans sacrifier ton devoir de protection et tes limites personnelles.""",
        'weekly_advice': {
            'week_1': "Médiatise un conflit professionnel avec douceur et fermeté.",
            'week_2': "Embellis ton environnement de travail pour nourrir tous.",
            'week_3': "Défends quelqu'un même si ça crée un inconfort relationnel.",
            'week_4': "Célèbre ta capacité unique à protéger par l'harmonie."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir protecteur**

Ta Lune en Cancer en Maison 10 te donne une vocation de soin. L'Ascendant Scorpion intensifie tout : tu protèges avec un pouvoir transformateur, tu nourris en profondeur, tu défends férocement ton territoire professionnel.

**Domaine activé** : Maison 10 — Double eau : ta réputation se construit sur ton intensité émotionnelle et ton pouvoir de transformation. Tu es vu·e comme quelqu'un qui protège jusqu'à la mort, qui guérit profondément.

**Ton approche instinctive** : Le Scorpion te fait exercer ton pouvoir pour protéger, contrôler ton environnement professionnel pour assurer la sécurité, transformer les structures toxiques.

**Tensions possibles** : Le contrôle peut devenir manipulation. Tu risques de confondre protection et domination, ou de détruire ce qui résiste à ta vision de ce qui est bon pour les autres.

**Conseil clé** : Utiliser ton pouvoir transformateur pour libérer, pas pour contrôler sous couvert de protection.""",
        'weekly_advice': {
            'week_1': "Identifie où ton pouvoir professionnel peut vraiment protéger.",
            'week_2': "Transforme une structure professionnelle toxique avec courage.",
            'week_3': "Vérifie que ton contrôle sert vraiment les autres, pas ton ego.",
            'week_4': "Célèbre ton pouvoir unique de guérir et transformer."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Mission inspirante**

Ta Lune en Cancer en Maison 10 oriente ta carrière vers le soin. L'Ascendant Sagittaire élargit ta vision : tu veux protéger et nourrir à grande échelle, enseigner, inspirer, créer du sens à travers ta vocation.

**Domaine activé** : Maison 10 — Ta réputation se construit sur ton optimisme protecteur et ta capacité à donner du sens. Tu nourris par l'enseignement, tu protèges par la transmission de sagesse.

**Ton approche instinctive** : Le Sagittaire te pousse à partager tes valeurs avec générosité, à élargir constamment ton impact, à garder la foi en ta mission même dans les difficultés.

**Tensions possibles** : L'excès d'expansion peut diluer ton impact. Tu risques de vouloir sauver tout le monde au détriment de ton efficacité réelle, ou de promettre plus que tu ne peux tenir.

**Conseil clé** : Servir ta grande vision tout en restant présent·e et efficace dans tes engagements actuels.""",
        'weekly_advice': {
            'week_1': "Clarifie la mission profonde qui guide ta carrière.",
            'week_2': "Enseigne ou partage ta vision protectrice avec générosité.",
            'week_3': "Ancre ton optimisme dans des actions concrètes de service.",
            'week_4': "Célèbre l'ampleur de ton impact protecteur dans le monde."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Autorité bienveillante**

Ta Lune en Cancer en Maison 10 te donne une vocation de soin. L'Ascendant Capricorne structure cette vocation : tu construis patiemment une autorité basée sur ta capacité à protéger et guider avec sagesse.

**Domaine activé** : Maison 10 — Opposition Cancer-Capricorne : tu ressens profondément ton devoir de protection mais tu l'exerces avec maturité et structure. Ta réputation se construit lentement mais solidement.

**Ton approche instinctive** : Le Capricorne te fait assumer ta responsabilité de protecteur·rice avec sérieux, bâtir des structures durables de soin, persévérer dans ta vocation malgré les obstacles.

**Tensions possibles** : La rigidité peut étouffer ton cœur. Tu risques de devenir trop strict·e dans ta protection, ou de négliger tes propres besoins émotionnels pour ta carrière.

**Conseil clé** : Construire ton autorité protectrice sans perdre ta douceur et ta capacité à nourrir émotionnellement.""",
        'weekly_advice': {
            'week_1': "Assume ta responsabilité de protecteur·rice avec maturité.",
            'week_2': "Structure ta vocation de soin pour qu'elle dure dans le temps.",
            'week_3': "Permets à ton cœur d'adoucir ton autorité professionnelle.",
            'week_4': "Célèbre l'équilibre unique entre force et tendresse que tu incarnes."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Innovation sociale**

Ta Lune en Cancer en Maison 10 oriente ta carrière vers le soin. L'Ascendant Verseau universalise ta vocation : tu veux protéger l'humanité, créer des structures innovantes qui nourrissent collectivement.

**Domaine activé** : Maison 10 — Opposition Cancer-Verseau : tu cherches à prendre soin personnellement tout en servant une cause universelle. Ta réputation se construit sur ton originalité protectrice.

**Ton approche instinctive** : Le Verseau te pousse à révolutionner les systèmes de soin, à créer des communautés qui se protègent mutuellement, à innover dans ta façon de nourrir les autres.

**Tensions possibles** : Le détachement peut te couper de l'intimité nécessaire au soin véritable. Tu risques de sacrifier les besoins individuels pour un idéal collectif, ou de t'épuiser pour une cause au détriment de ta santé.

**Conseil clé** : Servir ta vision collective tout en honorant tes besoins personnels et ceux des individus que tu protèges.""",
        'weekly_advice': {
            'week_1': "Identifie comment innover dans ton domaine pour mieux servir.",
            'week_2': "Connecte ta vocation personnelle à une cause collective.",
            'week_3': "Reste présent·e aux individus malgré ta vision universelle.",
            'week_4': "Célèbre ton originalité unique dans ta façon de protéger."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 10, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Service transcendant**

Ta Lune en Cancer en Maison 10 fait de ta carrière une vocation de soin. L'Ascendant Poissons dissout les frontières : tu veux servir sans limite, te sacrifier pour les autres, offrir un amour inconditionnel dans ton travail.

**Domaine activé** : Maison 10 — Triple eau : ta réputation se construit sur ta compassion infinie et ton dévouement sans frontières. Tu es vu·e comme un ange, un sauveur, un canal de guérison pure.

**Ton approche instinctive** : Le Poissons te fait fusionner avec ceux que tu aides, donner sans compter, servir avec une foi absolue dans la bonté de ton œuvre.

**Tensions possibles** : Le manque de limites peut te détruire. Tu risques de t'épuiser complètement au service des autres, de te perdre dans le martyre, ou d'attirer des profiteurs.

**Conseil clé** : Servir avec compassion infinie tout en gardant des frontières qui te protègent et te permettent de durer.""",
        'weekly_advice': {
            'week_1': "Offre ton service avec tout ton cœur et toute ta compassion.",
            'week_2': "Identifie où tu as besoin de limites pour ne pas te perdre.",
            'week_3': "Ancre ta vocation spirituelle dans des actions pratiques.",
            'week_4': "Célèbre ta capacité unique à aimer et servir inconditionnellement."
        }
    },

    # ==================== MAISON 11 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Tribu guerrière**

Ta Lune en Cancer en Maison 11 fait de tes amitiés une famille choisie. L'Ascendant Bélier te pousse à défendre férocement cette tribu, à créer des communautés basées sur le courage et la loyauté.

**Domaine activé** : Maison 11 — Tes amitiés et groupes sont ton foyer émotionnel. Tu protèges tes ami·e·s comme ta famille, tu cherches une tribu qui te donne la sécurité tout en partageant ton esprit de combat.

**Ton approche instinctive** : Le Bélier te fait foncer pour protéger ton groupe, initier des projets communautaires, défendre ta vision collective avec passion, créer une tribu qui ose.

**Tensions possibles** : L'agressivité peut aliéner tes ami·e·s. Tu risques de devenir trop protecteur·rice au point d'étouffer la liberté de ta tribu, ou de te battre contre ceux qui la menacent de façon disproportionnée.

**Conseil clé** : Protéger ta communauté avec courage tout en respectant l'indépendance de chacun·e.""",
        'weekly_advice': {
            'week_1': "Identifie qui fait vraiment partie de ta famille choisie.",
            'week_2': "Défends un·e ami·e ou ton groupe face à une menace.",
            'week_3': "Initie un projet qui renforce les liens de ta tribu.",
            'week_4': "Célèbre la force de ta communauté et ta loyauté."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Communauté confortable**

Ta Lune en Cancer en Maison 11 cherche une tribu qui te nourrit émotionnellement. L'Ascendant Taureau te fait construire patiemment une communauté stable, confortable, loyale, où chacun·e se sent en sécurité.

**Domaine activé** : Maison 11 — Tes amitiés sont des relations durables et sécurisantes. Tu crées des espaces de convivialité, de partage, où l'on prend soin les uns des autres dans la douceur et la beauté.

**Ton approche instinctive** : Le Taureau te fait valoriser la qualité sur la quantité en amitiés, créer des rituels de partage (repas, célébrations), offrir un confort matériel à ta tribu.

**Tensions possibles** : L'attachement peut te rendre résistant·e aux changements de groupe. Tu risques de t'accrocher à des amitiés qui ne te nourrissent plus par peur de la solitude, ou de rejeter les nouveaux venus.

**Conseil clé** : Cultiver tes amitiés durables tout en restant ouvert·e à la croissance naturelle de ta communauté.""",
        'weekly_advice': {
            'week_1': "Crée un espace confortable pour réunir tes ami·e·s.",
            'week_2': "Offre un geste matériel de soin à ta communauté.",
            'week_3': "Accepte qu'une amitié puisse évoluer ou partir naturellement.",
            'week_4': "Célèbre la stabilité et la beauté de tes liens communautaires."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Réseau familial**

Ta Lune en Cancer en Maison 11 cherche des amitiés nourricières. L'Ascendant Gémeaux multiplie tes connexions : tu veux créer un réseau large mais intime, communiquer émotionnellement, connecter les gens comme une famille.

**Domaine activé** : Maison 11 — Tes amitiés sont nombreuses et variées mais tu cherches la profondeur émotionnelle dans chacune. Tu es le lien qui nourrit et informe, qui connecte et protège par l'échange.

**Ton approche instinctive** : Le Gémeaux te fait créer des groupes autour de l'échange d'idées, communiquer constamment avec tes ami·e·s, rester curieux·se des histoires de chacun·e, partager ta sensibilité par les mots.

**Tensions possibles** : La dispersion peut empêcher l'intimité réelle. Tu risques de papillonner entre mille ami·e·s sans construire de liens profonds, ou d'intellectualiser tes besoins émotionnels communautaires.

**Conseil clé** : Équilibrer ton réseau large avec quelques amitiés profondes où tu peux vraiment te nourrir émotionnellement.""",
        'weekly_advice': {
            'week_1': "Connecte deux ami·e·s qui pourraient se nourrir mutuellement.",
            'week_2': "Communique tes besoins émotionnels clairement à ta tribu.",
            'week_3': "Approfondis une amitié au lieu d'en multiplier de nouvelles.",
            'week_4': "Célèbre ta capacité unique à tisser des liens nourriciers."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Famille d'âmes**

Triple Cancer en Maison 11 : tes ami·e·s SONT ta famille, plus que tout. Tu cherches des liens communautaires qui nourrissent ton âme, où tu peux être complètement vulnérable et protégé·e.

**Domaine activé** : Maison 11 — Pure énergie familiale dans tes amitiés. Tu crées une tribu où l'on se protège mutuellement, où les émotions sont partagées profondément, où personne n'est laissé·e seul·e.

**Ton approche instinctive** : Triple eau : tu ressens intuitivement les besoins de ta communauté, tu nourris tes ami·e·s comme des proches, tu protèges ton groupe comme ton foyer.

**Tensions possibles** : L'hypersensibilité aux dynamiques de groupe peut te blesser profondément. Tu risques de prendre personnellement tout conflit, de surprotéger ta tribu au point de l'étouffer, ou de te replier si tu te sens rejeté·e.

**Conseil clé** : Aimer ta tribu inconditionnellement tout en gardant ton identité personnelle et des frontières saines.""",
        'weekly_advice': {
            'week_1': "Assume pleinement que tes ami·e·s sont ta famille choisie.",
            'week_2': "Protège un·e membre de ta tribu qui en a besoin.",
            'week_3': "Partage ta vulnérabilité émotionnelle avec ta communauté.",
            'week_4': "Célèbre la profondeur unique de tes liens communautaires."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Communauté rayonnante**

Ta Lune en Cancer en Maison 11 cherche des amitiés nourrissantes. L'Ascendant Lion te pousse à créer une communauté où chacun·e peut briller, à être le cœur généreux qui inspire et protège ta tribu.

**Domaine activé** : Maison 11 — Tes amitiés te permettent d'exprimer ta générosité et ton leadership bienveillant. Tu crées des espaces où les gens se sentent vus, valorisés, aimés.

**Ton approche instinctive** : Le Lion te fait rassembler les gens autour de ta chaleur, célébrer tes ami·e·s avec créativité, créer une tribu qui rayonne de joie et de sécurité.

**Tensions possibles** : Le besoin de reconnaissance peut corrompre tes intentions. Tu risques de créer une communauté pour ton ego plutôt que pour le bien commun, ou de dominer le groupe au lieu de le servir.

**Conseil clé** : Utiliser ton charisme pour élever ta communauté, pas pour te mettre en avant.""",
        'weekly_advice': {
            'week_1': "Crée un événement qui célèbre ta communauté généreusement.",
            'week_2': "Mets en lumière un·e ami·e qui mérite d'être reconnu·e.",
            'week_3': "Vérifie que tu nourris vraiment les autres, pas ton besoin d'attention.",
            'week_4': "Célèbre le rayonnement collectif de ta tribu."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Service communautaire**

Ta Lune en Cancer en Maison 11 cherche une tribu qui te nourrit. L'Ascendant Vierge te pousse à servir cette communauté concrètement, à améliorer le quotidien de ton groupe, à être utile.

**Domaine activé** : Maison 11 — Tes amitiés se basent sur l'entraide pratique et le soin attentif. Tu es celui ou celle qui anticipe les besoins, qui organise, qui s'assure que chacun·e est vraiment pris·e en charge.

**Ton approche instinctive** : La Vierge te fait analyser comment mieux servir ton groupe, créer des systèmes d'entraide efficaces, améliorer constamment le fonctionnement de ta communauté.

**Tensions possibles** : Le perfectionnisme peut te rendre critique envers tes ami·e·s ou toi-même. Tu risques de t'épuiser à vouloir tout arranger pour tout le monde, ou de juger ceux qui ne servent pas autant que toi.

**Conseil clé** : Servir ta communauté avec excellence tout en acceptant l'imperfection humaine de ton groupe.""",
        'weekly_advice': {
            'week_1': "Identifie un besoin pratique de ta communauté et réponds-y.",
            'week_2': "Organise un système d'entraide qui améliore le quotidien de tous.",
            'week_3': "Accepte que tes ami·e·s soient imparfait·e·s et c'est bien ainsi.",
            'week_4': "Célèbre ton service discret mais essentiel à ta tribu."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie collective**

Ta Lune en Cancer en Maison 11 cherche des amitiés qui te nourrissent. L'Ascendant Balance te pousse à créer une communauté harmonieuse, équilibrée, où chacun·e se sent accueilli·e et valorisé·e.

**Domaine activé** : Maison 11 — Tes amitiés sont basées sur l'équilibre relationnel et le partage esthétique. Tu protèges l'harmonie du groupe, tu nourris par la beauté et la diplomatie.

**Ton approche instinctive** : La Balance te fait médiatiser les conflits de ta tribu, créer des espaces de convivialité élégants, valoriser l'égalité et la justice dans tes amitiés.

**Tensions possibles** : Le besoin d'harmonie peut t'empêcher d'affronter les problèmes réels. Tu risques de maintenir des amitiés toxiques par peur de créer du déséquilibre, ou de te sacrifier pour la paix du groupe.

**Conseil clé** : Créer l'harmonie communautaire sans nier les conflits nécessaires ni sacrifier tes propres besoins.""",
        'weekly_advice': {
            'week_1': "Médiatise un conflit dans ton groupe avec douceur et fermeté.",
            'week_2': "Crée un espace esthétique qui rassemble ta communauté.",
            'week_3': "Défends tes besoins même si ça crée un inconfort temporaire.",
            'week_4': "Célèbre l'harmonie et la beauté de tes liens communautaires."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Tribu profonde**

Ta Lune en Cancer en Maison 11 cherche des amitiés nourricières. L'Ascendant Scorpion intensifie tout : tu veux des liens communautaires profonds, transformateurs, où l'on se protège jusqu'à la mort.

**Domaine activé** : Maison 11 — Double eau : tes amitiés sont intenses et fusionnelles. Tu crées une tribu basée sur la loyauté absolue, les secrets partagés, la transformation mutuelle.

**Ton approche instinctive** : Le Scorpion te fait sonder la profondeur de chaque amitié, créer des pactes de fidélité, éliminer les liens superficiels, protéger férocement ta communauté intime.

**Tensions possibles** : L'intensité peut repousser ou étouffer. Tu risques de demander trop d'intimité trop vite, de contrôler ton groupe sous couvert de protection, ou de te venger si tu te sens trahi·e.

**Conseil clé** : Cultiver la profondeur de tes liens tout en respectant le rythme et les limites des autres.""",
        'weekly_advice': {
            'week_1': "Approfondis une amitié en partageant ta vulnérabilité réelle.",
            'week_2': "Protège un·e ami·e de façon transformatrice, pas possessive.",
            'week_3': "Vérifie que tu ne contrôles pas ta communauté par peur.",
            'week_4': "Célèbre l'intensité et la loyauté de ta tribu."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Famille mondiale**

Ta Lune en Cancer en Maison 11 cherche une tribu nourrissante. L'Ascendant Sagittaire élargit ta vision : tu veux créer une communauté qui dépasse les frontières, qui unit les cultures, qui partage une quête de sens.

**Domaine activé** : Maison 11 — Tes amitiés sont diversifiées et inspirantes. Tu nourris par le partage de sagesse, tu protèges par l'ouverture d'esprit, tu crées une tribu qui grandit ensemble.

**Ton approche instinctive** : Le Sagittaire te fait rassembler des gens de tous horizons, enseigner et apprendre de ta communauté, garder l'optimisme dans les liens, explorer ensemble.

**Tensions possibles** : L'expansion peut empêcher l'intimité profonde. Tu risques d'avoir mille ami·e·s mais aucun·e vraiment proche, ou de fuir les besoins émotionnels réels par la philosophie.

**Conseil clé** : Créer une communauté large et diversifiée tout en cultivant quelques liens profonds et nourriciers.""",
        'weekly_advice': {
            'week_1': "Connecte-toi avec quelqu'un d'une culture ou vision différente.",
            'week_2': "Partage ta sagesse avec ta communauté généreusement.",
            'week_3': "Approfondis un lien au lieu de multiplier les connexions.",
            'week_4': "Célèbre la diversité et l'expansion de ta tribu."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Tribu responsable**

Ta Lune en Cancer en Maison 11 cherche des amitiés nourrissantes. L'Ascendant Capricorne structure ta communauté : tu construis patiemment une tribu mature, responsable, qui dure dans le temps.

**Domaine activé** : Maison 11 — Opposition Cancer-Capricorne : tu veux une famille choisie mais tu la bâtis avec sagesse et sélectivité. Tes amitiés sont des engagements sérieux et durables.

**Ton approche instinctive** : Le Capricorne te fait valoriser la qualité sur la quantité, assumer ta responsabilité envers ta tribu, créer des structures communautaires solides.

**Tensions possibles** : La rigidité peut étouffer la chaleur de tes liens. Tu risques de devenir trop exigeant·e envers tes ami·e·s, ou de sacrifier tes besoins émotionnels pour ta responsabilité communautaire.

**Conseil clé** : Construire une communauté stable et mature tout en gardant ton cœur ouvert et vulnérable.""",
        'weekly_advice': {
            'week_1': "Assume ta responsabilité envers un·e ami·e qui compte sur toi.",
            'week_2': "Crée une structure qui renforce la durabilité de ta tribu.",
            'week_3': "Permets à ton cœur d'adoucir tes attentes envers les autres.",
            'week_4': "Célèbre la maturité et la stabilité de tes liens communautaires."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Tribu visionnaire**

Ta Lune en Cancer en Maison 11 cherche une famille choisie. L'Ascendant Verseau, maître naturel de cette maison, universalise ta vision : tu veux créer une communauté qui change le monde, une tribu révolutionnaire.

**Domaine activé** : Maison 11 — Double énergie verseau : tes amitiés servent une cause plus grande. Tu nourris par l'innovation collective, tu protèges par la création de systèmes avant-gardistes.

**Ton approche instinctive** : Le Verseau te fait créer une communauté basée sur des idéaux partagés, innover dans ta façon de construire la tribu, rester libre tout en étant loyal·e.

**Tensions possibles** : Le détachement peut te couper de l'intimité émotionnelle. Tu risques de sacrifier les besoins individuels pour la cause collective, ou de fuir la vulnérabilité par l'intellectualisation.

**Conseil clé** : Servir ta vision collective tout en nourrissant tes besoins personnels et ceux de tes proches.""",
        'weekly_advice': {
            'week_1': "Connecte ta tribu autour d'une cause ou vision commune.",
            'week_2': "Innove dans ta façon de créer de la communauté.",
            'week_3': "Reste présent·e émotionnellement malgré ton idéalisme.",
            'week_4': "Célèbre ton originalité communautaire unique."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 11, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Tribu spirituelle**

Ta Lune en Cancer en Maison 11 cherche une famille d'âmes. L'Ascendant Poissons dissout les frontières : tu veux créer une communauté basée sur l'amour inconditionnel, la compassion universelle, la fusion spirituelle.

**Domaine activé** : Maison 11 — Triple eau : tes amitiés sont mystiques et fusionnelles. Ta communauté est une sangha spirituelle, un réseau d'âmes connectées au-delà de l'ego.

**Ton approche instinctive** : Le Poissons te fait aimer ta tribu inconditionnellement, te sacrifier pour ta communauté, créer des liens basés sur la compassion et la foi partagée.

**Tensions possibles** : Le manque de limites peut te détruire ou attirer des profiteurs. Tu risques de te perdre dans ta tribu, de te sacrifier jusqu'à l'épuisement, ou de maintenir des amitiés toxiques par compassion.

**Conseil clé** : Aimer ta communauté avec compassion infinie tout en gardant des frontières qui te protègent.""",
        'weekly_advice': {
            'week_1': "Offre ton amour inconditionnel à ta communauté avec tout ton cœur.",
            'week_2': "Identifie où tu as besoin de limites pour ne pas te perdre.",
            'week_3': "Ancre ta tribu spirituelle dans des actions concrètes de soin.",
            'week_4': "Célèbre la profondeur mystique de tes liens communautaires."
        }
    },

    # ==================== MAISON 12 ====================

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Guerrier intérieur**

Ta Lune en Cancer en Maison 12 plonge tes émotions dans l'inconscient. L'Ascendant Bélier te pousse à combattre courageusement tes démons intérieurs, à affronter tes blessures cachées avec force.

**Domaine activé** : Maison 12 — Tes émotions les plus profondes sont enfouies. Tu as besoin de solitude pour ressentir vraiment, de te retirer pour te ressourcer, de guérir tes blessures ancestrales.

**Ton approche instinctive** : Le Bélier te fait combattre tes peurs plutôt que les fuir, affronter ton ombre avec courage, défendre ton besoin de solitude quand nécessaire.

**Tensions possibles** : L'agression contre toi-même peut t'autodétruire. Tu risques de refouler ta sensibilité par peur de la vulnérabilité, ou de te battre contre ton besoin légitime de repos émotionnel.

**Conseil clé** : Utiliser ton courage pour plonger dans ton inconscient et guérir, pas pour fuir ou combattre ta sensibilité.""",
        'weekly_advice': {
            'week_1': "Prends du temps en solitude pour ressentir vraiment.",
            'week_2': "Affronte courageusement une blessure émotionnelle enfouie.",
            'week_3': "Défends ton besoin de te retirer pour te ressourcer.",
            'week_4': "Célèbre ton courage à plonger dans tes profondeurs."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Refuge secret**

Ta Lune en Cancer en Maison 12 cache tes émotions dans l'inconscient. L'Ascendant Taureau te pousse à créer un sanctuaire intérieur, un espace secret où tu peux te ressourcer dans la douceur et la sécurité.

**Domaine activé** : Maison 12 — Ton monde intérieur est ton refuge ultime. Tu as besoin de temps seul·e dans le confort, de rituels apaisants, de beauté qui nourrit ton âme en silence.

**Ton approche instinctive** : Le Taureau te fait créer patiemment ton cocon intérieur, valoriser le repos émotionnel, trouver la paix dans la stabilité de ta vie intérieure.

**Tensions possibles** : L'attachement au confort peut t'enfermer. Tu risques de te réfugier dans ton monde intérieur au lieu d'affronter la vie, ou de refuser toute confrontation émotionnelle par besoin de paix.

**Conseil clé** : Cultiver ton sanctuaire intérieur tout en restant ouvert·e à la vie et aux autres.""",
        'weekly_advice': {
            'week_1': "Crée un espace physique qui devient ton refuge émotionnel.",
            'week_2': "Pratique des rituels apaisants qui nourrissent ton âme.",
            'week_3': "Sors de ton confort intérieur pour affronter une émotion difficile.",
            'week_4': "Célèbre la paix profonde de ton monde intérieur."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Dialogue intérieur**

Ta Lune en Cancer en Maison 12 cache tes émotions profondes. L'Ascendant Gémeaux te pousse à explorer ton inconscient par les mots, à dialoguer avec ton monde intérieur, à comprendre tes émotions cachées.

**Domaine activé** : Maison 12 — Ton monde intérieur est complexe et multiple. Tu as besoin d'écrire, de parler à toi-même, de mettre des mots sur l'indicible pour comprendre tes émotions enfouies.

**Ton approche instinctive** : Le Gémeaux te fait intellectualiser tes émotions profondes pour les rendre supportables, chercher la compréhension mentale de ton inconscient, communiquer avec ton ombre.

**Tensions possibles** : L'intellectualisation peut t'empêcher de vraiment ressentir. Tu risques de fuir tes émotions profondes par l'analyse mentale, ou de te perdre dans mille interprétations sans guérir vraiment.

**Conseil clé** : Utiliser les mots pour explorer ton inconscient tout en permettant au ressenti silencieux d'émerger.""",
        'weekly_advice': {
            'week_1': "Écris dans un journal pour explorer tes émotions cachées.",
            'week_2': "Parle à ton monde intérieur avec curiosité et douceur.",
            'week_3': "Pratique aussi le silence pour ressentir sans interpréter.",
            'week_4': "Célèbre ta capacité unique à comprendre ton inconscient."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Océan intérieur**

Triple Cancer en Maison 12 : ton monde intérieur est un océan sans fond d'émotions, de rêves, de mémoires ancestrales. Tu es profondément connecté·e à l'inconscient collectif et à ton propre mystère.

**Domaine activé** : Maison 12 — Pure immersion dans l'inconscient. Ton besoin de solitude est absolu, ta sensibilité psychique intense, ta connexion aux mondes invisibles naturelle.

**Ton approche instinctive** : Triple eau : tu ressens l'invisible, tu channels l'inconscient collectif, tu guéris par l'intuition pure, tu te dissous dans le rêve et la contemplation.

**Tensions possibles** : Le risque de te noyer dans ton monde intérieur est réel. Tu peux te perdre dans tes émotions, te replier complètement du monde, ou sombrer dans la mélancolie.

**Conseil clé** : Honorer la profondeur de ton océan intérieur tout en gardant un ancrage dans le monde physique.""",
        'weekly_advice': {
            'week_1': "Plonge profondément dans ton monde intérieur avec confiance.",
            'week_2': "Pratique un ancrage quotidien pour ne pas te perdre.",
            'week_3': "Partage ta sensibilité psychique avec quelqu'un de confiance.",
            'week_4': "Célèbre la profondeur mystique unique de ton être."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Lumière cachée**

Ta Lune en Cancer en Maison 12 cache tes émotions dans l'ombre. L'Ascendant Lion veut briller : tension entre ton besoin de te retirer et ton désir de rayonner, entre ta vulnérabilité cachée et ta force visible.

**Domaine activé** : Maison 12 — Ton monde intérieur est généreux mais secret. Tu donnes beaucoup mais dans l'ombre, tu guéris les autres sans reconnaissance, tu rayonnes même dans ta solitude.

**Ton approche instinctive** : Le Lion te pousse à créer même dans ton retrait, à trouver ta dignité dans ta vulnérabilité, à briller depuis ta profondeur émotionnelle.

**Tensions possibles** : Le conflit entre visibilité et retrait peut te déchirer. Tu risques de cacher ta vraie nature par fierté, ou de t'épuiser à donner sans être vu·e et reconnu·e.

**Conseil clé** : Honorer ton besoin de solitude tout en permettant à ta lumière intérieure de rayonner authentiquement.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose depuis ta solitude sans attendre de reconnaissance.",
            'week_2': "Partage une part de ta vulnérabilité cachée avec fierté.",
            'week_3': "Ressource-toi dans le retrait pour mieux briller ensuite.",
            'week_4': "Célèbre ta capacité unique à être fort·e dans l'ombre."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Service invisible**

Ta Lune en Cancer en Maison 12 cache tes émotions dans l'inconscient. L'Ascendant Vierge te pousse à servir depuis l'ombre, à guérir discrètement, à prendre soin sans reconnaissance ni besoin d'être vu·e.

**Domaine activé** : Maison 12 — Ton service est secret et précis. Tu analyses tes émotions profondes pour mieux guérir, tu améliores ton monde intérieur, tu sers l'invisible avec dévouement.

**Ton approche instinctive** : La Vierge te fait perfectionner ton travail intérieur, servir les autres depuis l'ombre, trouver la paix dans l'humilité de ton service caché.

**Tensions possibles** : L'autocritique peut devenir destructrice dans la solitude. Tu risques de t'épuiser à servir sans jamais te nourrir toi-même, ou de te juger durement pour tes émotions enfouies.

**Conseil clé** : Servir avec excellence depuis l'ombre tout en honorant tes propres besoins émotionnels.""",
        'weekly_advice': {
            'week_1': "Sers quelqu'un discrètement sans attendre de reconnaissance.",
            'week_2': "Analyse tes émotions profondes avec douceur, pas jugement.",
            'week_3': "Nourris-toi autant que tu nourris les autres en secret.",
            'week_4': "Célèbre ton service invisible et précis dans le monde."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Paix intérieure**

Ta Lune en Cancer en Maison 12 cache tes émotions dans l'inconscient. L'Ascendant Balance te pousse à créer l'harmonie dans ton monde intérieur, à équilibrer tes émotions cachées, à trouver la beauté dans la solitude.

**Domaine activé** : Maison 12 — Ton monde intérieur cherche l'équilibre. Tu as besoin de solitude harmonieuse, de beauté contemplative, de relations intérieures apaisées entre tes différentes parts.

**Ton approche instinctive** : La Balance te fait médiatiser tes conflits internes, créer de la beauté dans ton retrait, chercher la paix émotionnelle dans la contemplation.

**Tensions possibles** : L'évitement du conflit intérieur peut bloquer ta guérison. Tu risques de refouler les émotions difficiles par besoin d'harmonie, ou de fuir ta solitude par peur du déséquilibre.

**Conseil clé** : Créer l'harmonie intérieure tout en acceptant d'affronter les conflits émotionnels nécessaires.""",
        'weekly_advice': {
            'week_1': "Crée un espace de solitude harmonieux et esthétique.",
            'week_2': "Médiatise un conflit intérieur avec douceur et équité.",
            'week_3': "Affronte une émotion difficile même si ça trouble ta paix.",
            'week_4': "Célèbre l'équilibre et la beauté de ton monde intérieur."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Transformation profonde**

Ta Lune en Cancer en Maison 12 plonge dans l'inconscient. L'Ascendant Scorpion intensifie tout : ton monde intérieur est un chaudron de transformation, de mort et renaissance émotionnelle, de pouvoir psychique.

**Domaine activé** : Maison 12 — Double eau profonde : tu explores les abysses de l'inconscient, tu transmutes tes blessures les plus sombres, tu guéris par la mort de l'ancien toi.

**Ton approche instinctive** : Le Scorpion te fait plonger sans peur dans tes zones les plus sombres, transformer tes démons en alliés, exercer ton pouvoir psychique depuis l'ombre.

**Tensions possibles** : L'obsession peut te faire sombrer. Tu risques de te perdre dans tes ténèbres intérieures, de devenir destructeur·rice envers toi-même, ou de manipuler depuis l'inconscient.

**Conseil clé** : Transformer courageusement tes profondeurs tout en gardant un ancrage dans la vie et la lumière.""",
        'weekly_advice': {
            'week_1': "Plonge dans une blessure profonde pour la transformer.",
            'week_2': "Utilise ton pouvoir psychique pour guérir, pas contrôler.",
            'week_3': "Ancre-toi dans la vie après chaque plongée dans l'ombre.",
            'week_4': "Célèbre ta capacité unique à renaître de tes cendres."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foi intérieure**

Ta Lune en Cancer en Maison 12 nourrit ton inconscient. L'Ascendant Sagittaire te pousse à chercher le sens dans ta solitude, à explorer ton monde intérieur comme un voyage spirituel, à garder la foi même dans l'ombre.

**Domaine activé** : Maison 12 — Ton retrait est une quête. Tu te retires non par peur mais pour grandir, tu explores ton inconscient avec optimisme, tu trouves la sagesse dans tes profondeurs.

**Ton approche instinctive** : Le Sagittaire te fait chercher la vérité dans ton monde intérieur, enseigner depuis ta sagesse cachée, garder l'espoir même dans tes moments les plus sombres.

**Tensions possibles** : La fuite spirituelle peut t'empêcher d'affronter vraiment. Tu risques d'intellectualiser tes émotions profondes par philosophie, ou de fuir tes blessures dans des quêtes spirituelles sans ancrage.

**Conseil clé** : Explorer ton monde intérieur avec foi tout en affrontant concrètement tes émotions enfouies.""",
        'weekly_advice': {
            'week_1': "Retire-toi en solitude pour une quête spirituelle profonde.",
            'week_2': "Cherche la sagesse dans une blessure émotionnelle.",
            'week_3': "Ancre ta foi spirituelle dans la guérison concrète.",
            'week_4': "Célèbre l'optimisme et la sagesse de ton monde intérieur."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Solitude responsable**

Ta Lune en Cancer en Maison 12 cache tes émotions profondes. L'Ascendant Capricorne structure ton inconscient : tu gères ton monde intérieur avec maturité, tu assumes la responsabilité de ta guérison, tu construis patiemment ta santé psychique.

**Domaine activé** : Maison 12 — Opposition Cancer-Capricorne : tu ressens profondément mais tu gères ta vie intérieure avec discipline. Ton retrait est productif, ta solitude structurée.

**Ton approche instinctive** : Le Capricorne te fait affronter tes émotions profondes avec courage et méthode, persévérer dans ta guérison, bâtir une force intérieure solide.

**Tensions possibles** : La répression émotionnelle peut t'enfermer. Tu risques de contrôler tes émotions au lieu de les guérir, ou de sacrifier ton besoin de vulnérabilité pour ta force apparente.

**Conseil clé** : Gérer ta vie intérieure avec maturité tout en permettant à tes émotions de s'exprimer librement.""",
        'weekly_advice': {
            'week_1': "Crée une structure pour ta pratique de guérison intérieure.",
            'week_2': "Assume la responsabilité de ton bien-être émotionnel.",
            'week_3': "Permets à ton cœur de s'exprimer malgré ton besoin de contrôle.",
            'week_4': "Célèbre la force et la maturité de ton monde intérieur."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Conscience collective**

Ta Lune en Cancer en Maison 12 te connecte à l'inconscient. L'Ascendant Verseau universalise ton monde intérieur : tu channels l'inconscient collectif, tu guéris des blessures ancestrales, tu innoves dans ta spiritualité.

**Domaine activé** : Maison 12 — Opposition Cancer-Verseau : tu ressens l'inconscient personnel ET collectif. Ta solitude est humanitaire, ton retrait visionnaire, ta guérison universelle.

**Ton approche instinctive** : Le Verseau te fait explorer ton inconscient avec originalité, te détacher de tes émotions pour les observer, servir l'humanité depuis ton monde intérieur.

**Tensions possibles** : Le détachement peut t'empêcher la guérison profonde. Tu risques d'intellectualiser tes blessures au lieu de les ressentir, ou de te sacrifier pour l'humanité sans te guérir toi-même.

**Conseil clé** : Servir ta vision collective tout en honorant tes besoins personnels de guérison émotionnelle.""",
        'weekly_advice': {
            'week_1': "Explore comment tes blessures personnelles servent l'humanité.",
            'week_2': "Innove dans ta pratique spirituelle et de guérison.",
            'week_3': "Ressens profondément au lieu d'observer détaché·e.",
            'week_4': "Célèbre ta connexion unique à l'inconscient collectif."
        }
    },

    {
        'moon_sign': 'Cancer', 'moon_house': 12, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution sacrée**

Ta Lune en Cancer en Maison 12 te plonge dans l'inconscient. L'Ascendant Poissons dissout toutes frontières : tu fusionne avec le divin, tu channels l'universel, tu te dissous dans l'océan cosmique de l'amour et de la compassion.

**Domaine activé** : Maison 12 — Triple eau mystique : ton monde intérieur est un temple sacré. Tu es médium naturel·le, guérisseur·se mystique, canal de grâce et de compassion infinies.

**Ton approche instinctive** : Le Poissons te fait te perdre volontairement dans ton monde intérieur, fusionner avec le tout, guérir par l'amour inconditionnel et la foi transcendante.

**Tensions possibles** : Le manque total de frontières peut te détruire. Tu risques de te perdre complètement, de fuir la vie par la spiritualité, de t'épuiser à absorber les souffrances du monde.

**Conseil clé** : Te dissoudre dans le divin tout en gardant un ancrage minimal dans ton corps et ta vie.""",
        'weekly_advice': {
            'week_1': "Plonge dans une expérience mystique profonde avec confiance.",
            'week_2': "Channels la compassion universelle sans te perdre.",
            'week_3': "Ancre-toi physiquement après chaque dissolution spirituelle.",
            'week_4': "Célèbre ta connexion sacrée unique avec l'infini."
        }
    },

]

if __name__ == "__main__":
    print(f"[*] Batch complet: Cancer M1-M12 (144 interprétations) - {len(BATCH)} interprétations chargées")
    asyncio.run(insert_batch(BATCH))
    print(f"[✓] Cancer M1-M9 généré - {len(BATCH)}/144 interprétations ({len(BATCH)*100//144}%)")
