"""Batch complet: Taurus - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # ==================== MAISON 1 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Ancrage dynamique**

Ta Lune en Taureau en Maison 1 veut construire une identité stable et authentique. Mais ton Ascendant Bélier ajoute une urgence d'action : tu veux incarner qui tu es MAINTENANT, sans attendre. Une tension fertile entre patience et impulsion.

**Domaine activé** : Maison 1 — Ton identité personnelle, ton apparence, ta manière de te présenter au monde sont au cœur de ce mois. Tu cherches à te sentir solide dans ton corps et dans ton image.

**Ton approche instinctive** : L'Ascendant Bélier te pousse à agir vite sur ton apparence ou ton expression personnelle. Tu veux des changements visibles, concrets, immédiats dans la façon dont tu te montres.

**Tensions possibles** : Le besoin de stabilité du Taureau peut freiner l'impulsivité du Bélier. Tu risques de t'élancer puis de reculer, hésitant entre transformation rapide et sécurité.

**Conseil clé** : Poser des petits gestes concrets qui changent ton image sans déstabiliser ton sentiment de sécurité.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect de ton apparence que tu veux transformer.",
            'week_2': "Fais un petit changement visible qui te ressemble vraiment.",
            'week_3': "Observe comment tu te sens dans cette nouvelle expression.",
            'week_4': "Ancre ce qui fonctionne, ajuste ce qui ne te convient pas."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Être incarné**

Triple Taureau sur ton identité : Lune, Maison 1 et Ascendant. C'est un mois où tu es profondément toi-même, ancré·e dans ton corps, connecté·e à tes sens. L'authenticité est totale, la patience est reine.

**Domaine activé** : Maison 1 — Ton identité personnelle rayonne dans sa forme la plus pure. Tu cherches à te sentir confortable dans ta peau, à habiter pleinement ton corps et ton espace personnel.

**Ton approche instinctive** : Double Taureau te fait avancer lentement mais sûrement. Tu ne te précipites pas pour changer, tu laisses les choses mûrir. Cette stabilité peut être rassurante ou, parfois, un peu figée.

**Tensions possibles** : La résistance au changement peut devenir de l'inertie. Tu risques de rester dans ta zone de confort même quand elle ne te sert plus vraiment.

**Conseil clé** : Cultiver ton bien-être personnel sans tomber dans la complaisance ou l'immobilisme.""",
        'weekly_advice': {
            'week_1': "Prends soin de ton corps avec intention et plaisir.",
            'week_2': "Crée un rituel qui t'ancre dans ton identité profonde.",
            'week_3': "Reste ouvert·e à une petite évolution qui te fait du bien.",
            'week_4': "Savoure la sensation d'être pleinement toi-même."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Curiosité ancrée**

Ta Lune en Taureau en Maison 1 veut une identité stable et cohérente. Ton Ascendant Gémeaux ajoute de la versatilité : tu explores différentes facettes de toi-même, tu te cherches à travers la variété et l'échange.

**Domaine activé** : Maison 1 — Ton identité personnelle est en exploration. Tu veux te sentir solide (Taureau) tout en restant curieux·se et adaptable (Gémeaux). Comment être stable et flexible à la fois ?

**Ton approche instinctive** : Le Gémeaux te fait communiquer sur qui tu es, tester différentes versions de toi-même. Cette légèreté peut déstabiliser ton besoin taurien de cohérence et de constance.

**Tensions possibles** : L'hésitation entre rester fidèle à toi-même et explorer de nouvelles identités. Tu peux te disperser ou te sentir incohérent·e dans ton expression personnelle.

**Conseil clé** : Explorer différentes facettes de ton identité tout en gardant un socle stable de valeurs.""",
        'weekly_advice': {
            'week_1': "Essaie une nouvelle façon de te présenter ou de t'exprimer.",
            'week_2': "Partage avec d'autres qui tu es vraiment, sans filtre.",
            'week_3': "Garde ce qui résonne avec ton essence profonde.",
            'week_4': "Intègre les découvertes sans perdre ta cohérence."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Douceur protectrice**

Ta Lune en Taureau en Maison 1 cherche la stabilité dans ton identité. Ton Ascendant Cancer ajoute une dimension émotionnelle et protectrice : tu veux te sentir en sécurité dans ton corps et tes émotions avant de te montrer.

**Domaine activé** : Maison 1 — Ton identité personnelle est teintée de sensibilité. Tu as besoin de te sentir à l'aise émotionnellement pour t'exprimer pleinement. Ton apparence reflète ton état intérieur.

**Ton approche instinctive** : Le Cancer te fait créer une carapace de confort autour de ton identité. Tu te montres quand tu te sens en sécurité, tu te retires quand tu es blessé·e.

**Tensions possibles** : La double nature terre-eau peut créer une tendance à s'isoler ou à se replier sur soi par excès de prudence. Tu risques de te cacher au lieu de t'affirmer.

**Conseil clé** : Créer un cocon de sécurité émotionnelle qui te permet de rayonner, pas de te cacher.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te fait te sentir en sécurité dans ton corps.",
            'week_2': "Nourris ton identité avec douceur et bienveillance.",
            'week_3': "Ose te montrer même si tu te sens vulnérable.",
            'week_4': "Célèbre la force de ta sensibilité assumée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Rayonnement solide**

Ta Lune en Taureau en Maison 1 veut une identité stable et naturelle. Ton Ascendant Lion ajoute du panache : tu veux briller, être vu·e, reconnu·e pour qui tu es. La discrétion taurine rencontre l'éclat léonin.

**Domaine activé** : Maison 1 — Ton identité personnelle demande à être célébrée. Tu cherches à te montrer sous ton meilleur jour, avec authenticité (Taureau) et générosité (Lion).

**Ton approche instinctive** : Le Lion te pousse à prendre de la place, à assumer ton charisme. Cette confiance peut t'aider à dépasser la timidité ou l'inertie du Taureau quand il se sent jugé.

**Tensions possibles** : Le besoin d'approbation du Lion peut entrer en conflit avec l'authenticité tranquille du Taureau. Tu risques de forcer ton expression pour plaire.

**Conseil clé** : Briller dans ta vérité la plus simple, sans artifice ni recherche excessive de validation.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te rend vraiment fier·e de toi-même.",
            'week_2': "Montre-toi avec générosité et authenticité.",
            'week_3': "Reçois les compliments sans douter de ta valeur.",
            'week_4': "Ancre ta confiance dans ce qui est réel, pas dans le regard des autres."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfectionnement tranquille**

Double terre sur ton identité : ta Lune en Taureau et ton Ascendant Vierge créent une approche pragmatique et méthodique de qui tu es. Tu veux améliorer ton apparence, ton bien-être, ton expression personnelle de manière concrète.

**Domaine activé** : Maison 1 — Ton identité personnelle est un projet d'optimisation. Tu cherches à affiner ton image, ton hygiène de vie, ta présentation pour qu'elle soit à la fois authentique et excellente.

**Ton approche instinctive** : La Vierge te fait analyser comment tu te présentes, chercher les détails à améliorer. Cette exigence peut enrichir ton expression ou créer une autocritique excessive.

**Tensions possibles** : Le perfectionnisme peut bloquer ta spontanéité. Tu risques de ne jamais te sentir assez bien pour te montrer pleinement, toujours en train de peaufiner.

**Conseil clé** : Viser l'amélioration continue sans perdre le contact avec ta beauté naturelle imparfaite.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect de ton identité que tu veux affiner.",
            'week_2': "Mets en place une routine qui t'améliore vraiment.",
            'week_3': "Accepte que l'imperfection fasse partie de ton charme.",
            'week_4': "Célèbre les progrès sans oublier d'apprécier ce qui est déjà là."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie incarnée**

Ta Lune en Taureau en Maison 1 cherche une identité stable et sensorielle. Ton Ascendant Balance ajoute une dimension esthétique et relationnelle : tu veux que ton apparence soit à la fois authentique et harmonieuse.

**Domaine activé** : Maison 1 — Ton identité personnelle est influencée par le regard des autres et ton sens de l'esthétique. Tu cherches à être beau/belle, à créer une image qui plaît tout en restant toi-même.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre dans ton expression personnelle. Tu veux plaire sans te trahir, être apprécié·e sans devenir superficiel·le.

**Tensions possibles** : La tendance à adapter ton identité pour créer l'harmonie peut t'éloigner de ton authenticité taurine. Tu risques de perdre ton centre en cherchant trop à plaire.

**Conseil clé** : Cultiver une beauté qui vient de ton être profond, pas d'une recherche extérieure de validation.""",
        'weekly_advice': {
            'week_1': "Définis ce qui est beau pour toi, indépendamment des modes.",
            'week_2': "Crée une harmonie entre ton apparence et ton essence.",
            'week_3': "Écoute les retours sans perdre ton sens de toi-même.",
            'week_4': "Savoure le plaisir d'être à la fois authentique et harmonieux·se."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Puissance tranquille**

Opposition Taureau-Scorpion sur ton identité : ta Lune veut la simplicité, la stabilité, l'authenticité naturelle. Ton Ascendant Scorpion ajoute de l'intensité, du mystère, une profondeur magnétique. Le calme apparent cache une force volcanique.

**Domaine activé** : Maison 1 — Ton identité personnelle est un terrain de transformation profonde. Tu peux vouloir changer radicalement ton apparence ou révéler une facette cachée de toi-même.

**Ton approche instinctive** : Le Scorpion te fait chercher la vérité sous la surface. Tu ne te contentes pas d'une identité superficielle, tu veux toucher l'essence de qui tu es vraiment, même si c'est dérangeant.

**Tensions possibles** : Le besoin de contrôle peut créer de la rigidité. Tu risques d'osciller entre une présence paisible et des moments d'intensité déstabilisante pour toi et les autres.

**Conseil clé** : Accepter ta complexité sans forcer la transformation ni résister au changement nécessaire.""",
        'weekly_advice': {
            'week_1': "Regarde en face une partie de toi que tu caches d'habitude.",
            'week_2': "Laisse une transformation personnelle se produire naturellement.",
            'week_3': "Assume l'intensité de ton être sans t'en excuser.",
            'week_4': "Observe comment tu as évolué dans ton expression de toi-même."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Expansion ancrée**

Ta Lune en Taureau en Maison 1 veut une identité stable et concrète. Ton Ascendant Sagittaire ajoute une soif d'exploration et d'expansion : tu veux être toi-même tout en grandissant, en découvrant de nouveaux horizons.

**Domaine activé** : Maison 1 — Ton identité personnelle est en quête de sens et d'aventure. Tu cherches à t'affirmer de manière optimiste et ouverte, tout en gardant tes racines bien plantées.

**Ton approche instinctive** : Le Sagittaire te fait voir grand sur qui tu peux devenir. Cette vision peut inspirer ton évolution personnelle ou créer de l'impatience face à la lenteur taurine.

**Tensions possibles** : Le besoin de liberté et d'expansion peut entrer en conflit avec le besoin de sécurité et de stabilité. Tu risques de te sentir tiraillé·e entre partir et rester.

**Conseil clé** : Grandir et explorer tout en gardant des racines qui te nourrissent et te stabilisent.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu veux grandir en tant que personne.",
            'week_2': "Explore une facette de toi qui demande à s'exprimer plus librement.",
            'week_3': "Garde contact avec ce qui te stabilise pendant l'exploration.",
            'week_4': "Intègre les découvertes sans perdre ton centre."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Construction personnelle**

Double terre cardinale et fixe : ta Lune en Taureau et ton Ascendant Capricorne créent une approche sérieuse et constructive de ton identité. Tu veux bâtir une image solide, durable, respectable.

**Domaine activé** : Maison 1 — Ton identité personnelle est un projet à long terme. Tu cherches à développer une présence qui inspire le respect et la confiance, basée sur des qualités réelles et durables.

**Ton approche instinctive** : Le Capricorne te fait structurer ton développement personnel. Tu veux des résultats concrets, mesurables. Cette discipline peut enrichir ou rigidifier ton expression.

**Tensions possibles** : L'excès de sérieux peut étouffer ta spontanéité et ton plaisir. Tu risques de t'imposer des standards si élevés que tu ne te sens jamais assez bien.

**Conseil clé** : Bâtir ton identité avec patience et rigueur tout en gardant de la douceur envers toi-même.""",
        'weekly_advice': {
            'week_1': "Définis l'image de toi que tu veux construire sur le long terme.",
            'week_2': "Pose une pierre concrète dans cette construction.",
            'week_3': "Persévère même si les résultats sont lents à venir.",
            'week_4': "Reconnais le travail accompli sans oublier de savourer le chemin."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Authenticité originale**

Ta Lune en Taureau en Maison 1 veut une identité stable et naturelle. Ton Ascendant Verseau ajoute une dimension d'originalité et de détachement : tu veux être toi-même d'une manière unique, hors des conventions.

**Domaine activé** : Maison 1 — Ton identité personnelle cherche à concilier authenticité et singularité. Tu veux être fidèle à toi-même tout en assumant ce qui te rend différent·e des autres.

**Ton approche instinctive** : Le Verseau te fait questionner les normes sociales sur l'apparence et l'identité. Tu peux vouloir choquer ou surprendre pour affirmer ta liberté personnelle.

**Tensions possibles** : Le besoin de sécurité du Taureau peut freiner l'audace du Verseau. Tu risques d'osciller entre conformisme rassurant et rébellion déstabilisante.

**Conseil clé** : Être original·e dans ton expression sans perdre ton ancrage ni chercher à être différent·e pour le principe.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te rend unique sans jugement.",
            'week_2': "Assume une particularité que tu caches habituellement.",
            'week_3': "Trouve l'équilibre entre appartenance et singularité.",
            'week_4': "Savoure la liberté d'être toi-même sans te justifier."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Fluidité ancrée**

Ta Lune en Taureau en Maison 1 cherche une identité stable et tangible. Ton Ascendant Poissons ajoute de la fluidité et de l'intuition : tu ressens qui tu es plutôt que de le définir rationnellement.

**Domaine activé** : Maison 1 — Ton identité personnelle est à la fois concrète et insaisissable. Tu veux te sentir solide dans ton corps tout en restant ouvert·e aux influences subtiles et aux transformations intuitives.

**Ton approche instinctive** : Le Poissons te fait adapter ton expression personnelle selon ton ressenti. Cette flexibilité peut adoucir la rigidité du Taureau ou créer de la confusion identitaire.

**Tensions possibles** : La difficulté à maintenir des limites claires. Tu risques de te perdre dans les attentes des autres ou de manquer de cohérence dans ton expression personnelle.

**Conseil clé** : Cultiver une identité à la fois stable et fluide, ancrée dans ton essence mais ouverte au mystère.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition sur qui tu es vraiment en ce moment.",
            'week_2': "Crée des rituels qui t'ancrent dans ton corps et ton être.",
            'week_3': "Reste ouvert·e aux transformations subtiles de ton identité.",
            'week_4': "Intègre ce qui a du sens sans te disperser."
        }
    },

    # ==================== MAISON 2 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Conquête matérielle**

Ta Lune en Taureau en Maison 2 est dans son élément naturel : sécurité, ressources, valeur personnelle. Ton Ascendant Bélier ajoute de l'audace : tu veux construire ta stabilité financière rapidement, avec initiative.

**Domaine activé** : Maison 2 — Tes finances, possessions et estime de soi matérielle sont au cœur de ce mois. Tu cherches à la fois la sécurité à long terme et l'action immédiate pour améliorer ta situation.

**Ton approche instinctive** : Le Bélier te pousse à prendre des risques calculés pour augmenter tes ressources. Tu veux agir vite, mais le Taureau te rappelle l'importance de construire sur du solide.

**Tensions possibles** : L'impatience du Bélier peut te faire dépenser avant d'avoir vraiment sécurisé. Tu risques d'osciller entre audace et prudence sans trouver ton rythme.

**Conseil clé** : Agir avec détermination sur tes finances tout en gardant une vision de stabilité à long terme.""",
        'weekly_advice': {
            'week_1': "Identifie une opportunité concrète pour augmenter tes revenus.",
            'week_2': "Prends une initiative audacieuse mais réfléchie.",
            'week_3': "Consolide ce que tu as gagné avant de te lancer ailleurs.",
            'week_4': "Fais le point sur ton équilibre entre audace et prudence."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Abondance naturelle**

Triple Taureau sur la Maison 2 : c'est LE mois des ressources et de la sécurité matérielle. Tu es totalement aligné·e avec le besoin de construire, d'accumuler, de créer une base solide pour ta vie.

**Domaine activé** : Maison 2 — Tes finances et possessions sont au maximum de leur importance. Tu veux sentir la solidité de tes ressources, le poids de ce que tu possèdes, la sécurité que l'argent peut apporter.

**Ton approche instinctive** : Triple Taureau te fait avancer lentement mais sûrement. Tu construis ta richesse pierre par pierre, avec patience. Cette approche est fiable mais peut manquer d'audace.

**Tensions possibles** : La peur de manquer peut créer de l'avarice ou du matérialisme excessif. Tu risques de confondre ta valeur personnelle avec ton compte en banque.

**Conseil clé** : Cultiver l'abondance avec sagesse, en restant généreux·se et détaché·e de la possession compulsive.""",
        'weekly_advice': {
            'week_1': "Définis ce que la sécurité matérielle signifie vraiment pour toi.",
            'week_2': "Mets en place une habitude qui génère de la valeur durable.",
            'week_3': "Savoure ce que tu possèdes déjà sans anxiété du futur.",
            'week_4': "Partage une partie de ton abondance avec générosité."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Ressources multiples**

Ta Lune en Taureau en Maison 2 veut une sécurité financière stable et durable. Ton Ascendant Gémeaux ajoute de la diversité : tu explores plusieurs sources de revenus, tu restes flexible dans ta gestion.

**Domaine activé** : Maison 2 — Tes finances cherchent à la fois la stabilité et la variété. Tu peux développer plusieurs projets parallèles, diversifier tes investissements, explorer différentes façons de générer de la valeur.

**Ton approche instinctive** : Le Gémeaux te fait communiquer sur tes compétences, réseauter pour créer des opportunités. Cette agilité peut enrichir ton approche taurine ou créer de la dispersion.

**Tensions possibles** : La difficulté à te concentrer sur une seule source de revenus. Tu risques de te disperser sans jamais vraiment capitaliser sur tes talents.

**Conseil clé** : Diversifier intelligemment tout en gardant un socle financier stable et fiable.""",
        'weekly_advice': {
            'week_1': "Identifie 2-3 sources de revenus potentielles à développer.",
            'week_2': "Teste une nouvelle approche pour monétiser tes compétences.",
            'week_3': "Garde l'essentiel de ton énergie sur ce qui rapporte vraiment.",
            'week_4': "Évalue quelle diversification sert réellement ta sécurité."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sécurité nourricière**

Double besoin de sécurité : ta Lune en Taureau et ton Ascendant Cancer créent une sensibilité intense aux questions financières. L'argent est lié à ton sentiment de protection et de bien-être émotionnel.

**Domaine activé** : Maison 2 — Tes finances et ressources sont teintées d'émotions. Tu as besoin de sentir que tu as assez, que ceux que tu aimes sont protégés matériellement, que le futur est sécurisé.

**Ton approche instinctive** : Le Cancer te fait économiser, protéger, préparer pour les jours difficiles. Cette prudence peut être sage ou créer de l'anxiété financière excessive.

**Tensions possibles** : La peur de manquer peut bloquer ta générosité ou ta capacité à investir. Tu risques de thésauriser par anxiété plutôt que par sagesse.

**Conseil clé** : Construire une sécurité financière solide sans laisser la peur diriger tes décisions.""",
        'weekly_advice': {
            'week_1': "Identifie tes peurs financières et regarde-les en face.",
            'week_2': "Crée un coussin de sécurité qui te rassure vraiment.",
            'week_3': "Pratique la générosité mesurée pour dépasser la peur de manquer.",
            'week_4': "Célèbre la solidité de ce que tu as construit."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Abondance généreuse**

Ta Lune en Taureau en Maison 2 veut construire une richesse solide et durable. Ton Ascendant Lion ajoute de la générosité et du panache : tu veux non seulement avoir, mais aussi donner et rayonner par ton abondance.

**Domaine activé** : Maison 2 — Tes finances et ressources sont un terrain d'expression de ta valeur personnelle. Tu veux que ton niveau de vie reflète ta grandeur intérieure, que ta richesse serve aussi les autres.

**Ton approche instinctive** : Le Lion te fait voir grand et dépenser généreusement pour créer de la beauté et du plaisir. Cette approche peut enrichir ta vie ou créer des dépenses excessives.

**Tensions possibles** : Le besoin de sécurité du Taureau peut entrer en conflit avec la générosité du Lion. Tu risques d'alterner entre économies strictes et dépenses flamboyantes.

**Conseil clé** : Cultiver une abondance qui permet à la fois la sécurité et la générosité mesurée.""",
        'weekly_advice': {
            'week_1': "Définis un budget qui inclut plaisir ET sécurité.",
            'week_2': "Investis dans quelque chose qui te fait te sentir fier·e.",
            'week_3': "Partage ton abondance sans compromettre ta stabilité.",
            'week_4': "Savoure le plaisir d'avoir et de donner en équilibre."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Gestion parfaite**

Double terre sur la Maison 2 : ta Lune en Taureau et ton Ascendant Vierge créent une approche minutieuse et pragmatique de tes finances. Tu veux optimiser chaque euro, construire une richesse méthodique.

**Domaine activé** : Maison 2 — Tes finances et ressources sont un projet d'organisation et d'amélioration continue. Tu analyses tes revenus, optimises tes dépenses, cherches l'efficacité maximale.

**Ton approche instinctive** : La Vierge te fait créer des systèmes, suivre des budgets, améliorer ta gestion. Cette rigueur peut sécuriser ton avenir ou créer de l'anxiété obsessionnelle.

**Tensions possibles** : Le perfectionnisme financier peut te paralyser. Tu risques de ne jamais te sentir assez riche, toujours en train d'optimiser sans profiter.

**Conseil clé** : Gérer tes finances avec sagesse tout en gardant du plaisir et de la spontanéité.""",
        'weekly_advice': {
            'week_1': "Analyse tes finances avec précision et honnêteté.",
            'week_2': "Optimise une habitude de dépense ou d'épargne.",
            'week_3': "Autorise-toi une dépense plaisir sans culpabilité.",
            'week_4': "Célèbre l'équilibre entre rigueur et douceur."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Valeur harmonieuse**

Ta Lune en Taureau en Maison 2 cherche la sécurité matérielle solide. Ton Ascendant Balance ajoute une dimension esthétique et relationnelle : tu veux que ton argent crée de la beauté et de l'harmonie.

**Domaine activé** : Maison 2 — Tes finances et possessions sont influencées par ton sens de l'esthétique et ton besoin d'équilibre. Tu veux que ce que tu possèdes soit beau autant que fonctionnel.

**Ton approche instinctive** : La Balance te fait dépenser pour créer un environnement harmonieux. Tu investis dans le beau, le confortable, ce qui plaît. Cette approche peut enrichir ta vie ou créer des dépenses superficielles.

**Tensions possibles** : La difficulté à choisir peut bloquer tes décisions financières. Tu risques de dépenser trop pour plaire ou créer l'harmonie au détriment de ta sécurité.

**Conseil clé** : Cultiver la beauté dans ta vie matérielle sans sacrifier ta stabilité financière.""",
        'weekly_advice': {
            'week_1': "Définis ce qui a vraiment de la valeur esthétique pour toi.",
            'week_2': "Investis dans quelque chose de beau qui dure.",
            'week_3': "Trouve l'équilibre entre plaisir esthétique et prudence.",
            'week_4': "Savoure l'harmonie que tu as créée dans ton environnement."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir matériel**

Opposition Taureau-Scorpion sur la Maison 2 : ta Lune veut une sécurité simple et tangible. Ton Ascendant Scorpion ajoute de l'intensité et du contrôle : l'argent est pouvoir, transformation, ressource pour renaître.

**Domaine activé** : Maison 2 — Tes finances sont un terrain de transformation profonde. Tu peux vouloir changer radicalement ta situation matérielle, éliminer les dettes, reconstruire ta richesse depuis les fondations.

**Ton approche instinctive** : Le Scorpion te fait regarder tes finances sans faux-semblants. Tu veux comprendre les mécanismes cachés de l'argent, utiliser des ressources partagées, transformer ta valeur personnelle.

**Tensions possibles** : L'obsession du contrôle financier peut créer de l'anxiété ou de l'avarice. Tu risques de manipuler ou d'être manipulé·e dans les questions d'argent.

**Conseil clé** : Transformer ta relation à l'argent en profondeur tout en gardant la simplicité taurine.""",
        'weekly_advice': {
            'week_1': "Regarde ta situation financière réelle sans déni ni dramatisation.",
            'week_2': "Élimine une dette ou une dépendance financière toxique.",
            'week_3': "Explore une source de revenus ou un investissement profond.",
            'week_4': "Observe comment tu as repris le pouvoir sur ton argent."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Expansion matérielle**

Ta Lune en Taureau en Maison 2 veut construire une sécurité solide et progressive. Ton Ascendant Sagittaire ajoute de l'optimisme et de la vision : tu veux que ta richesse grandisse, que tes ressources servent une vie plus vaste.

**Domaine activé** : Maison 2 — Tes finances cherchent à s'étendre au-delà du simple confort. Tu veux que ton argent finance des aventures, des apprentissages, une vie plus riche de sens et d'expériences.

**Ton approche instinctive** : Le Sagittaire te fait voir les opportunités partout et croire en l'abondance. Cette confiance peut attirer la chance ou créer de l'insouciance financière.

**Tensions possibles** : L'excès d'optimisme peut te faire prendre des risques inconsidérés. Tu risques de dépenser pour des rêves sans sécuriser le présent.

**Conseil clé** : Viser l'expansion financière tout en gardant des bases solides et réalistes.""",
        'weekly_advice': {
            'week_1': "Définis une vision d'abondance inspirante mais chiffrée.",
            'week_2': "Prends un risque calculé pour augmenter tes ressources.",
            'week_3': "Reste ancré·e dans la réalité de tes finances actuelles.",
            'week_4': "Évalue si ton optimisme était fondé ou excessif."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Patrimoine construit**

Double terre cardinale et fixe sur la Maison 2 : ta Lune en Taureau et ton Ascendant Capricorne créent une approche sérieuse et ambitieuse de ta richesse. Tu veux bâtir un patrimoine durable.

**Domaine activé** : Maison 2 — Tes finances sont un projet de construction à long terme. Chaque euro économisé, chaque investissement est une pierre dans l'édifice de ta sécurité future.

**Ton approche instinctive** : Le Capricorne te fait planifier sur des décennies, accepter les sacrifices présents pour la richesse future. Cette discipline peut créer une vraie fortune ou une vie trop austère.

**Tensions possibles** : L'excès de sérieux peut t'empêcher de profiter de ce que tu as. Tu risques de toujours économiser sans jamais savourer ton abondance.

**Conseil clé** : Construire ta richesse avec patience et rigueur tout en t'autorisant des plaisirs présents.""",
        'weekly_advice': {
            'week_1': "Définis un plan financier sur 10-20 ans minimum.",
            'week_2': "Pose une pierre concrète dans ce patrimoine.",
            'week_3': "Autorise-toi un petit plaisir sans culpabilité.",
            'week_4': "Célèbre la solidité de ce que tu construis patiemment."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Richesse alternative**

Ta Lune en Taureau en Maison 2 veut une sécurité matérielle traditionnelle et solide. Ton Ascendant Verseau ajoute de l'originalité : tu explores des moyens non-conventionnels de créer de la valeur.

**Domaine activé** : Maison 2 — Tes finances cherchent un équilibre entre sécurité et innovation. Tu peux être attiré·e par les cryptomonnaies, l'économie collaborative, des business models disruptifs.

**Ton approche instinctive** : Le Verseau te fait penser différemment sur l'argent. Tu questionnes le rapport traditionnel à la richesse, explores des alternatives. Cette originalité peut créer des opportunités uniques.

**Tensions possibles** : Le besoin de sécurité du Taureau peut freiner l'innovation du Verseau. Tu risques d'osciller entre conservatisme rassurant et expérimentations risquées.

**Conseil clé** : Innover dans ta gestion financière tout en gardant un socle de sécurité traditionnel.""",
        'weekly_advice': {
            'week_1': "Explore une approche non-conventionnelle de générer de la valeur.",
            'week_2': "Teste une petite innovation financière sans risquer l'essentiel.",
            'week_3': "Garde 70% de tes ressources sur du traditionnel et sûr.",
            'week_4': "Évalue si tes expérimentations portent vraiment leurs fruits."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Abondance intuitive**

Ta Lune en Taureau en Maison 2 veut une sécurité matérielle concrète et tangible. Ton Ascendant Poissons ajoute de la fluidité et de l'intuition : tu ressens les opportunités financières plutôt que de les calculer.

**Domaine activé** : Maison 2 — Tes finances sont influencées par ton intuition et ta connexion spirituelle. Tu peux attirer l'abondance de manière mystérieuse quand tu lâches prise sur le contrôle.

**Ton approche instinctive** : Le Poissons te fait faire confiance au flow de l'argent. Tu donnes généreusement, tu reçois mystérieusement. Cette approche peut être magique ou manquer de pragmatisme.

**Tensions possibles** : La difficulté à gérer concrètement tes finances. Tu risques de te faire avoir par excès de confiance ou de générosité mal placée.

**Conseil clé** : Cultiver la confiance dans l'abondance tout en gardant une gestion terre-à-terre.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition sur une opportunité financière.",
            'week_2': "Crée des structures concrètes pour gérer ton argent.",
            'week_3': "Pratique la générosité sans te mettre en danger.",
            'week_4': "Observe l'équilibre entre lâcher-prise et responsabilité."
        }
    },

    # ==================== MAISON 3 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Communication directe**

Ta Lune en Taureau en Maison 3 veut des échanges stables et concrets. Ton Ascendant Bélier ajoute de la spontanéité : tu dis ce que tu penses sans détour, tu communiques avec franchise et urgence.

**Domaine activé** : Maison 3 — Ta communication, tes apprentissages, tes relations de proximité sont au cœur de ce mois. Tu veux échanger de manière authentique et pratique.

**Ton approche instinctive** : Le Bélier te fait parler vite et fort. Tu n'as pas peur de dire des vérités dérangeantes, de lancer des conversations importantes. Cette directivité peut être rafraîchissante ou brusque.

**Tensions possibles** : L'impatience peut te faire couper la parole ou ne pas écouter assez. Tu risques de blesser par franchise sans le vouloir.

**Conseil clé** : Communiquer avec authenticité et courage tout en restant à l'écoute de l'autre.""",
        'weekly_advice': {
            'week_1': "Identifie une conversation importante que tu dois avoir.",
            'week_2': "Exprime-toi avec franchise mais dans le respect.",
            'week_3': "Écoute vraiment avant de répondre impulsivement.",
            'week_4': "Observe comment ta directivité a impacté tes relations."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Parole posée**

Triple Taureau sur la Maison 3 : ta communication est lente, réfléchie, ancrée dans le concret. Tu parles quand tu as quelque chose de vraiment substantiel à dire, tu écoutes avec patience.

**Domaine activé** : Maison 3 — Tes échanges, apprentissages et relations de proximité prennent un rythme tranquille. Tu cherches des conversations profondes et utiles, pas du bavardage superficiel.

**Ton approche instinctive** : Triple Taureau te fait prendre ton temps pour comprendre et t'exprimer. Cette lenteur peut être sage ou créer des malentendus par manque de réactivité.

**Tensions possibles** : La résistance à changer d'avis ou à explorer de nouvelles idées. Tu risques de t'enfermer dans tes certitudes par confort.

**Conseil clé** : Cultiver la profondeur dans tes échanges sans tomber dans la rigidité mentale.""",
        'weekly_advice': {
            'week_1': "Choisis un sujet que tu veux vraiment approfondir.",
            'week_2': "Engage des conversations qui nourrissent ton intelligence.",
            'week_3': "Reste ouvert·e à des idées qui challengent tes croyances.",
            'week_4': "Savoure la richesse d'avoir compris quelque chose en profondeur."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Curiosité ancrée**

Ta Lune en Taureau en Maison 3 veut des apprentissages utiles et concrets. Ton Ascendant Gémeaux, maître naturel de cette maison, ajoute légèreté et variété : tu explores mille sujets avec enthousiasme.

**Domaine activé** : Maison 3 — Ta communication et tes apprentissages oscillent entre profondeur et diversité. Tu veux à la fois maîtriser un savoir solide et papillonner entre différents intérêts.

**Ton approche instinctive** : Le Gémeaux te fait communiquer avec aisance, multiplier les échanges, apprendre rapidement. Cette agilité peut enrichir ton Taureau ou créer de la dispersion.

**Tensions possibles** : La difficulté à approfondir un sujet jusqu'au bout. Tu risques de survoler sans jamais vraiment ancrer tes connaissances.

**Conseil clé** : Explorer largement tout en choisissant quelques domaines à vraiment maîtriser.""",
        'weekly_advice': {
            'week_1': "Identifie 2-3 sujets qui méritent ton attention soutenue.",
            'week_2': "Autorise-toi la curiosité sans culpabilité.",
            'week_3': "Reviens à l'essentiel et approfondis ce qui compte.",
            'week_4': "Célèbre l'équilibre entre largeur et profondeur."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Échange protecteur**

Ta Lune en Taureau en Maison 3 veut des communications stables et rassurantes. Ton Ascendant Cancer ajoute de l'empathie : tu écoutes avec ton cœur, tu parles pour nourrir et protéger l'autre.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages sont teintés d'émotions. Tu veux des conversations qui créent de l'intimité, du lien, de la sécurité affective avec ton entourage proche.

**Ton approche instinctive** : Le Cancer te fait communiquer avec douceur et sensibilité. Tu captes les non-dits, tu rassures par tes mots. Cette empathie peut enrichir tes relations ou t'épuiser.

**Tensions possibles** : La difficulté à mettre des limites dans tes échanges. Tu risques de prendre sur toi les émotions de tes proches ou de censurer ta vérité pour ne pas blesser.

**Conseil clé** : Communiquer avec empathie sans porter les fardeaux émotionnels des autres.""",
        'weekly_advice': {
            'week_1': "Identifie un proche avec qui tu veux créer plus de connexion.",
            'week_2': "Écoute vraiment sans chercher à résoudre ou à porter.",
            'week_3': "Exprime tes propres besoins émotionnels clairement.",
            'week_4': "Célèbre la qualité de tes liens de proximité."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Parole rayonnante**

Ta Lune en Taureau en Maison 3 veut une communication authentique et substantielle. Ton Ascendant Lion ajoute du charisme : ta parole a du poids, tu t'exprimes avec confiance et générosité.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages portent ta signature personnelle. Tu veux que ce que tu dis ait de l'impact, inspire, marque les esprits par son authenticité.

**Ton approche instinctive** : Le Lion te fait communiquer avec assurance et créativité. Tu racontes des histoires, tu captives ton auditoire. Cette présence peut enrichir tes échanges ou devenir envahissante.

**Tensions possibles** : Le besoin d'être au centre de la conversation. Tu risques de moins écouter que parler, de chercher l'admiration plutôt que l'échange réel.

**Conseil clé** : Rayonner dans ta communication tout en laissant de l'espace aux autres.""",
        'weekly_advice': {
            'week_1': "Identifie un message important que tu veux faire passer.",
            'week_2': "Exprime-toi avec confiance et authenticité.",
            'week_3': "Écoute autant que tu parles. Partage la lumière.",
            'week_4': "Observe si tes mots ont vraiment touché ou juste brillé."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision utile**

Double terre sur la Maison 3 : ta Lune en Taureau et ton Ascendant Vierge créent une communication pragmatique et précise. Tu parles pour transmettre quelque chose d'utile, tu apprends pour maîtriser.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages sont orientés vers l'efficacité et la qualité. Tu veux des informations fiables, des conversations productives, des connaissances applicables.

**Ton approche instinctive** : La Vierge te fait analyser chaque mot, chercher la précision, corriger les erreurs. Cette rigueur peut améliorer tes communications ou créer de la critique excessive.

**Tensions possibles** : Le perfectionnisme peut bloquer ton expression. Tu risques de te censurer par peur de ne pas être assez clair·e ou précis·e.

**Conseil clé** : Viser la clarté et l'utilité sans perdre la spontanéité de l'échange humain.""",
        'weekly_advice': {
            'week_1': "Identifie une compétence pratique que tu veux développer.",
            'week_2': "Communique avec précision sur des sujets concrets.",
            'week_3': "Accepte l'imperfection dans tes échanges quotidiens.",
            'week_4': "Célèbre ce que tu as vraiment compris et maîtrisé."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Dialogue harmonieux**

Ta Lune en Taureau en Maison 3 veut des échanges stables et authentiques. Ton Ascendant Balance ajoute de la diplomatie : tu cherches l'harmonie dans tes conversations, l'équilibre dans tes relations de proximité.

**Domaine activé** : Maison 3 — Tes communications et apprentissages cherchent la beauté et l'équilibre. Tu veux que tes échanges créent du lien, de la compréhension mutuelle, de l'harmonie relationnelle.

**Ton approche instinctive** : La Balance te fait adapter ton discours pour créer l'harmonie. Tu écoutes tous les points de vue, tu cherches le consensus. Cette diplomatie peut enrichir ou édulcorer tes échanges.

**Tensions possibles** : La difficulté à dire des vérités dérangeantes. Tu risques de sacrifier ton authenticité taurine pour maintenir la paix superficielle.

**Conseil clé** : Chercher l'harmonie dans tes échanges sans censurer ta vérité profonde.""",
        'weekly_advice': {
            'week_1': "Identifie une relation où tu veux plus d'équilibre dans l'échange.",
            'week_2': "Pratique l'écoute vraie et la parole authentique.",
            'week_3': "Dis une vérité difficile avec diplomatie mais clarté.",
            'week_4': "Savoure l'harmonie créée par l'authenticité partagée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité profonde**

Opposition Taureau-Scorpion sur la Maison 3 : ta Lune veut une communication simple et directe. Ton Ascendant Scorpion creuse sous la surface : tu veux des échanges qui touchent l'essentiel, qui transforment.

**Domaine activé** : Maison 3 — Tes conversations et apprentissages cherchent la profondeur et la vérité cachée. Tu ne te contentes pas du bavardage, tu veux comprendre les motivations secrètes, les non-dits.

**Ton approche instinctive** : Le Scorpion te fait poser des questions dérangeantes, creuser jusqu'à l'os. Cette intensité peut créer des échanges puissants ou mettre mal à l'aise.

**Tensions possibles** : L'excès d'intensité dans tes communications. Tu risques de sonder trop profond, de chercher des complots où il n'y en a pas.

**Conseil clé** : Chercher la profondeur tout en respectant les limites et la légèreté nécessaire.""",
        'weekly_advice': {
            'week_1': "Identifie une vérité que tu veux explorer sans faux-semblants.",
            'week_2': "Engage une conversation profonde avec quelqu'un de confiance.",
            'week_3': "Respecte le rythme de l'autre dans le dévoilement.",
            'week_4': "Observe comment la vérité a transformé ton rapport aux autres."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Exploration bavarde**

Ta Lune en Taureau en Maison 3 veut des apprentissages concrets et utiles. Ton Ascendant Sagittaire ajoute de l'expansion : tu veux apprendre pour comprendre le monde, communiquer pour partager des visions.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages cherchent le sens et l'horizon. Tu veux que tes conversations t'ouvrent à de nouvelles perspectives, que tes études te donnent une compréhension globale.

**Ton approche instinctive** : Le Sagittaire te fait communiquer avec enthousiasme et optimisme. Tu partages tes découvertes, tu inspires par ton ouverture. Cette générosité peut enrichir ou devenir du prosélytisme.

**Tensions possibles** : Le besoin de confort du Taureau peut freiner l'exploration du Sagittaire. Tu risques de rester dans des sujets familiers par peur de l'inconnu.

**Conseil clé** : Explorer largement tout en gardant un ancrage dans le concret et l'applicable.""",
        'weekly_advice': {
            'week_1': "Identifie un sujet qui élargit vraiment ta vision du monde.",
            'week_2': "Engage une conversation avec quelqu'un de très différent de toi.",
            'week_3': "Ramène tes découvertes à quelque chose de pratique.",
            'week_4': "Partage ce que tu as appris avec générosité."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Communication structurée**

Double terre cardinale et fixe sur la Maison 3 : ta Lune en Taureau et ton Ascendant Capricorne créent une approche sérieuse de l'apprentissage et de la communication. Tu veux maîtriser, structurer, utiliser.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages sont orientés vers l'efficacité et l'ambition. Tu communiques pour atteindre des objectifs, tu apprends pour développer ton expertise professionnelle.

**Ton approche instinctive** : Le Capricorne te fait organiser tes connaissances, planifier ton apprentissage. Cette discipline peut créer une vraie maîtrise ou étouffer la spontanéité de l'échange.

**Tensions possibles** : L'excès de sérieux peut rendre tes communications rigides ou distantes. Tu risques de manquer les moments de connexion spontanée et joyeuse.

**Conseil clé** : Structurer tes apprentissages et communications sans perdre la légèreté et le plaisir.""",
        'weekly_advice': {
            'week_1': "Définis un plan d'apprentissage structuré sur un sujet clé.",
            'week_2': "Communique de manière professionnelle mais authentique.",
            'week_3': "Autorise-toi un échange léger et spontané.",
            'week_4': "Célèbre la maîtrise que tu as construite patiemment."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Idées originales**

Ta Lune en Taureau en Maison 3 veut des apprentissages pratiques et des échanges concrets. Ton Ascendant Verseau ajoute de l'originalité : tu explores des sujets non-conventionnels, tu communiques de manière unique.

**Domaine activé** : Maison 3 — Tes conversations et apprentissages oscillent entre pragmatisme et innovation. Tu veux des connaissances utiles mais qui sortent des sentiers battus.

**Ton approche instinctive** : Le Verseau te fait penser différemment, questionner les consensus, explorer l'avant-garde. Cette originalité peut enrichir tes échanges ou te marginaliser intellectuellement.

**Tensions possibles** : Le besoin de sécurité du Taureau peut freiner l'audace intellectuelle du Verseau. Tu risques d'osciller entre conformisme rassurant et rébellion mentale.

**Conseil clé** : Penser original tout en restant ancré·e dans des connaissances solides et éprouvées.""",
        'weekly_advice': {
            'week_1': "Explore un sujet qui challenge tes croyances habituelles.",
            'week_2': "Engage une conversation sur des idées non-conventionnelles.",
            'week_3': "Garde les pieds sur terre en vérifiant tes sources.",
            'week_4': "Intègre ce qui a vraiment du sens dans ton système de pensée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Parole poétique**

Ta Lune en Taureau en Maison 3 veut des échanges clairs et concrets. Ton Ascendant Poissons ajoute de la fluidité et de l'intuition : tu communiques par ressenti, tu comprends entre les mots.

**Domaine activé** : Maison 3 — Tes conversations et apprentissages sont influencés par ton intuition. Tu captes des nuances subtiles, tu t'exprimes de manière imagée, parfois floue mais toujours évocatrice.

**Ton approche instinctive** : Le Poissons te fait communiquer par métaphores, histoires, émotions. Cette approche poétique peut enrichir tes échanges ou créer des malentendus par manque de clarté.

**Tensions possibles** : La difficulté à être précis·e et factuel·le. Tu risques de te perdre dans des digressions émotionnelles ou de mal comprendre par excès d'interprétation.

**Conseil clé** : Cultiver la beauté poétique de tes échanges tout en gardant un ancrage dans le concret.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment communiquer au-delà des mots.",
            'week_2': "Exprime-toi avec ton cœur et ton intuition.",
            'week_3': "Vérifie que tu as bien été compris·e concrètement.",
            'week_4': "Savoure la richesse des échanges au-delà du rationnel."
        }
    },

    # ==================== MAISON 4 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Foyer dynamique**

Ta Lune en Taureau en Maison 4 cherche un nid douillet et stable. Ton Ascendant Bélier ajoute de l'action : tu veux transformer ton espace de vie rapidement, créer un foyer qui te ressemble MAINTENANT.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes racines sont au cœur de ce mois. Tu cherches à la fois le cocooning rassurant et l'envie de bouger, changer, dynamiser ton espace personnel.

**Ton approche instinctive** : Le Bélier te pousse à agir vite sur ton habitat. Tu veux déménager, rénover, réorganiser avec énergie. Cette impulsion peut revitaliser ton foyer ou créer du chaos.

**Tensions possibles** : Le besoin de stabilité domestique du Taureau peut être bousculé par l'impulsivité du Bélier. Tu risques de déstabiliser ton cocon en voulant l'améliorer trop vite.

**Conseil clé** : Améliorer ton espace de vie avec énergie tout en préservant le sentiment de sécurité.""",
        'weekly_advice': {
            'week_1': "Identifie un changement concret que tu veux dans ton chez-toi.",
            'week_2': "Prends une initiative rapide mais réfléchie.",
            'week_3': "Laisse le temps à ton foyer de s'adapter au changement.",
            'week_4': "Savoure l'énergie nouvelle dans ton espace stabilisé."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Nid parfait**

Triple Taureau sur la Maison 4 : c'est LE mois du cocooning ultime. Ton foyer est ton sanctuaire, ton refuge, ta source de régénération. Tu veux que ton espace soit confortable, beau, nourrissant.

**Domaine activé** : Maison 4 — Ton chez-toi, ta famille, tes racines sont au maximum de leur importance. Tu investis ton énergie dans créer un environnement qui nourrit tous tes sens.

**Ton approche instinctive** : Triple Taureau te fait construire un nid douillet pierre par pierre. Tu choisis chaque objet avec soin, tu crées une atmosphère de paix et de confort total.

**Tensions possibles** : La tendance à t'isoler dans ton cocon par excès de confort. Tu risques de ne plus vouloir sortir, de te replier sur ton foyer au détriment de ta vie sociale.

**Conseil clé** : Créer un foyer ressourçant sans en faire une prison dorée qui t'isole du monde.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque à ton foyer pour être vraiment parfait.",
            'week_2': "Investis dans le confort et la beauté de ton espace.",
            'week_3': "Invite des proches à partager ton cocon.",
            'week_4': "Savoure ton chez-toi tout en restant ouvert·e au monde extérieur."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Foyer communicant**

Ta Lune en Taureau en Maison 4 veut un foyer stable et apaisant. Ton Ascendant Gémeaux ajoute du mouvement : ton chez-toi devient un lieu d'échanges, de passage, de stimulation intellectuelle.

**Domaine activé** : Maison 4 — Ton foyer et ta famille oscillent entre besoin de calme et besoin de variété. Tu veux un nid douillet qui accueille aussi des conversations, des apprentissages, du mouvement.

**Ton approche instinctive** : Le Gémeaux te fait transformer ton foyer en espace de communication. Tu invites du monde, tu crées des zones de travail et d'étude, tu bouges les meubles souvent.

**Tensions possibles** : La difficulté à trouver le calme dans ton foyer. Tu risques de créer trop de stimulation dans ton espace personnel au détriment de la paix.

**Conseil clé** : Créer un foyer qui nourrit à la fois ton besoin de stabilité et ta curiosité.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton foyer peut servir tes deux besoins.",
            'week_2': "Crée une zone de calme et une zone de stimulation.",
            'week_3': "Alterne entre cocooning et ouverture sociale.",
            'week_4': "Savoure l'équilibre trouvé entre repos et échange."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Cocon émotionnel**

Double besoin de sécurité domestique : ta Lune en Taureau et ton Ascendant Cancer créent une sensibilité intense à ton foyer. C'est ton refuge émotionnel absolu, ta source de réconfort.

**Domaine activé** : Maison 4 — Ton chez-toi et ta famille sont le centre de ton monde émotionnel. Tu veux créer un nid qui protège, nourrit, rassure tous ceux que tu aimes.

**Ton approche instinctive** : Le Cancer te fait materner ton foyer et tes proches. Tu cuisines, tu décores, tu crées une atmosphère de tendresse. Cette douceur peut être merveilleuse ou étouffante.

**Tensions possibles** : La tendance à fusionner avec ton foyer et ta famille. Tu risques de perdre tes limites, de porter les émotions de tous, de te replier sur ton clan.

**Conseil clé** : Créer un foyer nourricier tout en gardant ton autonomie émotionnelle.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te fait vraiment te sentir chez toi.",
            'week_2': "Crée des rituels familiaux qui nourrissent l'âme.",
            'week_3': "Garde du temps pour toi dans ton propre foyer.",
            'week_4': "Célèbre la chaleur du cocon sans t'y enfermer."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Palais personnel**

Ta Lune en Taureau en Maison 4 veut un foyer confortable et solide. Ton Ascendant Lion ajoute du panache : ton chez-toi doit être beau, impressionnant, digne de qui tu es.

**Domaine activé** : Maison 4 — Ton foyer et ta famille sont un terrain d'expression de ta créativité et de ta générosité. Tu veux que ton espace reflète ta grandeur intérieure.

**Ton approche instinctive** : Le Lion te fait créer un foyer qui impressionne et accueille généreusement. Tu investis dans le beau, tu reçois avec faste. Cette magnificence peut être inspirante ou excessive.

**Tensions possibles** : Le risque de dépenser trop pour ton foyer par besoin d'apparat. Tu peux confondre confort authentique et démonstration de statut.

**Conseil clé** : Créer un foyer qui rayonne ta vraie nature sans chercher l'admiration extérieure.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui rendrait ton foyer vraiment royal pour toi.",
            'week_2': "Investis dans quelque chose de beau qui dure.",
            'week_3': "Partage la chaleur de ton foyer avec générosité.",
            'week_4': "Savoure ton palais personnel avec gratitude."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Foyer optimisé**

Double terre sur la Maison 4 : ta Lune en Taureau et ton Ascendant Vierge créent une approche pragmatique de ton foyer. Tu veux un espace fonctionnel, sain, parfaitement organisé.

**Domaine activé** : Maison 4 — Ton chez-toi et ta famille sont un projet d'optimisation. Tu ranges, tu nettoies, tu améliores chaque détail pour créer l'environnement le plus efficient possible.

**Ton approche instinctive** : La Vierge te fait analyser chaque aspect de ton foyer. Tu identifies les dysfonctionnements, tu crées des systèmes. Cette rigueur peut améliorer ton confort ou créer de l'anxiété.

**Tensions possibles** : Le perfectionnisme domestique peut t'épuiser. Tu risques de ne jamais te sentir chez toi car ton foyer n'est jamais assez parfait.

**Conseil clé** : Améliorer ton foyer avec soin tout en acceptant l'imperfection chaleureuse du vivant.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect de ton foyer à optimiser vraiment.",
            'week_2': "Crée un système qui améliore ton quotidien durablement.",
            'week_3': "Accepte le désordre temporaire comme signe de vie.",
            'week_4': "Savoure le confort de l'amélioration sans la quête de perfection."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie domestique**

Ta Lune en Taureau en Maison 4 veut un foyer stable et confortable. Ton Ascendant Balance ajoute une dimension esthétique : ton chez-toi doit être beau, harmonieux, équilibré.

**Domaine activé** : Maison 4 — Ton foyer et ta famille cherchent l'équilibre et la beauté. Tu veux créer un espace qui plaît à l'œil et apaise l'âme, où chacun trouve sa place.

**Ton approche instinctive** : La Balance te fait décorer avec goût, créer des espaces harmonieux. Tu cherches le consensus familial sur l'aménagement. Cette recherche d'harmonie peut embellir ou diluer ton foyer.

**Tensions possibles** : La difficulté à imposer tes choix domestiques. Tu risques de céder aux préférences des autres au détriment de ton propre confort.

**Conseil clé** : Créer un foyer harmonieux qui reflète aussi authentiquement tes goûts personnels.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui créerait plus d'harmonie dans ton foyer.",
            'week_2': "Investis dans la beauté avec tes propres critères esthétiques.",
            'week_3': "Négocie l'espace domestique sans t'effacer.",
            'week_4': "Savoure l'équilibre entre tes besoins et ceux des autres."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Sanctuaire secret**

Opposition Taureau-Scorpion sur la Maison 4 : ta Lune veut un foyer simple et confortable. Ton Ascendant Scorpion ajoute de l'intensité : ton chez-toi est un lieu de transformation, un sanctuaire privé.

**Domaine activé** : Maison 4 — Ton foyer et tes racines familiales sont un terrain de profondeur émotionnelle. Tu peux vouloir transformer radicalement ton espace, explorer des secrets familiaux, créer un refuge sacré.

**Ton approche instinctive** : Le Scorpion te fait protéger férocement ton intimité domestique. Tu choisis qui entre dans ton foyer avec soin. Cette intensité peut créer un espace puissant ou une forteresse isolée.

**Tensions possibles** : L'obsession du contrôle de ton espace personnel. Tu risques de devenir possessif·ve de ton foyer ou d'y vivre des drames émotionnels intenses.

**Conseil clé** : Créer un sanctuaire intime tout en gardant une ouverture mesurée au monde.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui dans ton foyer mérite transformation profonde.",
            'week_2': "Crée un espace vraiment privé pour ta régénération.",
            'week_3': "Explore tes racines familiales avec honnêteté.",
            'week_4': "Observe comment ton foyer est devenu plus authentique."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foyer ouvert**

Ta Lune en Taureau en Maison 4 veut un nid stable et rassurant. Ton Ascendant Sagittaire ajoute de l'ouverture : ton foyer est un point d'ancrage pour explorer le monde, pas une prison dorée.

**Domaine activé** : Maison 4 — Ton chez-toi et ta famille oscillent entre enracinement et envie d'ailleurs. Tu veux un foyer qui te ressource pour mieux voyager, explorer, grandir.

**Ton approche instinctive** : Le Sagittaire te fait voir ton foyer comme une base d'aventures. Tu accueilles des cultures différentes, tu crées un espace ouvert sur le monde. Cette vision peut enrichir ou déstabiliser ton cocon.

**Tensions possibles** : La difficulté à te sentir vraiment chez toi quelque part. Tu risques de fuir ton foyer dès qu'il devient trop routinier ou de le remplir d'agitation.

**Conseil clé** : Créer un foyer stable qui nourrit ton besoin d'expansion plutôt que de le freiner.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton foyer peut servir tes aventures.",
            'week_2': "Crée un espace qui reflète tes voyages et ta vision.",
            'week_3': "Reviens vraiment chez toi entre deux expansions.",
            'week_4': "Savoure l'équilibre entre racines et ailes."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fondations solides**

Double terre cardinale et fixe sur la Maison 4 : ta Lune en Taureau et ton Ascendant Capricorne créent une approche sérieuse de ton foyer. Tu veux construire un patrimoine familial durable.

**Domaine activé** : Maison 4 — Ton foyer et ta famille sont un projet à long terme. Tu investis dans l'immobilier, tu construis des fondations qui dureront des générations.

**Ton approche instinctive** : Le Capricorne te fait planifier l'héritage familial, structurer ton espace domestique avec rigueur. Cette approche peut créer une vraie sécurité ou une atmosphère trop austère.

**Tensions possibles** : L'excès de sérieux peut étouffer la chaleur du foyer. Tu risques de transformer ton chez-toi en projet plutôt qu'en refuge.

**Conseil clé** : Construire un foyer solide avec patience tout en cultivant la tendresse et le confort.""",
        'weekly_advice': {
            'week_1': "Définis ta vision de foyer idéal sur 10-20 ans.",
            'week_2': "Investis dans quelque chose de durable pour ton chez-toi.",
            'week_3': "Crée aussi de la chaleur et de la spontanéité.",
            'week_4': "Célèbre les fondations que tu construis patiemment."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Habitat alternatif**

Ta Lune en Taureau en Maison 4 veut un foyer traditionnel et rassurant. Ton Ascendant Verseau ajoute de l'originalité : tu explores des formes d'habitat non-conventionnelles, des structures familiales alternatives.

**Domaine activé** : Maison 4 — Ton foyer et ta famille cherchent un équilibre entre sécurité et innovation. Tu peux être attiré·e par le coliving, l'habitat partagé, des configurations familiales modernes.

**Ton approche instinctive** : Le Verseau te fait questionner ce que "foyer" signifie vraiment pour toi. Tu veux te sentir chez toi d'une manière unique, libéré·e des conventions.

**Tensions possibles** : Le besoin de sécurité du Taureau peut freiner l'expérimentation du Verseau. Tu risques d'osciller entre conformisme rassurant et marginalité déstabilisante.

**Conseil clé** : Innover dans ta conception du foyer tout en gardant un ancrage de sécurité.""",
        'weekly_advice': {
            'week_1': "Explore ce que foyer signifie vraiment pour toi, au-delà des normes.",
            'week_2': "Teste une petite innovation dans ton espace domestique.",
            'week_3': "Garde ce qui te fait vraiment te sentir en sécurité.",
            'week_4': "Intègre l'original et le rassurant dans ton chez-toi."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Refuge fluide**

Ta Lune en Taureau en Maison 4 veut un foyer concret et tangible. Ton Ascendant Poissons ajoute de la fluidité : ton chez-toi est un espace de rêverie, de spiritualité, de connexion subtile.

**Domaine activé** : Maison 4 — Ton foyer et ta famille oscillent entre matérialité et mysticisme. Tu veux un espace qui nourrit ton corps et ton âme, qui est à la fois refuge terrestre et sanctuaire spirituel.

**Ton approche instinctive** : Le Poissons te fait créer une atmosphère onirique chez toi. Tu utilises la musique, les couleurs, les textures pour créer un espace qui transcende le matériel.

**Tensions possibles** : La difficulté à maintenir des structures domestiques claires. Tu risques de laisser ton foyer devenir chaotique ou poreux aux influences extérieures.

**Conseil clé** : Créer un foyer à la fois concret et spirituel, ancré et inspiré.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui nourrit ton âme dans ton espace personnel.",
            'week_2': "Crée un sanctuaire pour la méditation ou la créativité.",
            'week_3': "Garde des structures pratiques qui soutiennent ta fluidité.",
            'week_4': "Savoure l'équilibre entre terre et ciel dans ton foyer."
        }
    },

    # ==================== MAISON 5 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Passion créative**

Ta Lune en Taureau en Maison 5 veut créer avec ses mains, profiter des plaisirs simples et sensoriels. Ton Ascendant Bélier ajoute de l'audace : tu te lances dans des projets créatifs avec fougue et spontanéité.

**Domaine activé** : Maison 5 — Ta créativité, tes plaisirs, tes amours sont au cœur de ce mois. Tu cherches à la fois la jouissance sensorielle stable et l'excitation de la nouveauté.

**Ton approche instinctive** : Le Bélier te pousse à initier des projets créatifs sans trop réfléchir. Tu veux t'amuser MAINTENANT, séduire avec audace, créer impulsivement.

**Tensions possibles** : L'impatience peut te faire abandonner tes créations avant qu'elles soient vraiment abouties. Tu risques de papillonner entre plaisirs sans vraiment savourer.

**Conseil clé** : Lancer des projets créatifs avec élan tout en leur donnant le temps de mûrir.""",
        'weekly_advice': {
            'week_1': "Identifie un projet créatif qui t'excite vraiment.",
            'week_2': "Lance-toi sans attendre la perfection.",
            'week_3': "Persiste même quand l'enthousiasme initial retombe.",
            'week_4': "Savoure ce que tu as créé avec tes mains."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Volupté pure**

Triple Taureau sur la Maison 5 : c'est LE mois des plaisirs sensoriels, de la création artistique, de la jouissance de vivre. Tu veux profiter de chaque instant avec tous tes sens.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs sont au maximum de leur intensité. Tu veux créer quelque chose de beau et durable, savourer les bonnes choses de la vie, aimer avec tendresse.

**Ton approche instinctive** : Triple Taureau te fait chercher le plaisir dans la matière : bonne nourriture, sexualité sensuelle, création artistique tactile. Cette approche peut être profondément satisfaisante ou devenir hédoniste.

**Tensions possibles** : La tendance à l'excès de plaisirs sensuels. Tu risques de glisser vers la paresse, la gourmandise, la recherche de plaisir au détriment de tes responsabilités.

**Conseil clé** : Savourer les plaisirs de la vie avec présence sans tomber dans l'excès ou la complaisance.""",
        'weekly_advice': {
            'week_1': "Identifie les plaisirs qui nourrissent vraiment ton âme.",
            'week_2': "Crée quelque chose de beau avec tes mains.",
            'week_3': "Partage tes plaisirs avec générosité.",
            'week_4': "Trouve l'équilibre entre jouissance et discipline."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Jeu léger**

Ta Lune en Taureau en Maison 5 veut des plaisirs stables et sensoriels. Ton Ascendant Gémeaux ajoute de la légèreté : tu explores différentes formes de créativité, tu joues avec les idées et les mots.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs oscillent entre profondeur sensorielle et papillonnage joyeux. Tu veux à la fois savourer et explorer, créer et jouer.

**Ton approche instinctive** : Le Gémeaux te fait multiplier les projets créatifs, communiquer sur tes passions, séduire par l'esprit. Cette agilité peut enrichir ton expression ou créer de la dispersion.

**Tensions possibles** : La difficulté à approfondir un projet créatif. Tu risques de commencer mille choses sans jamais vraiment finir ni savourer.

**Conseil clé** : Explorer largement tout en choisissant quelques plaisirs à vraiment savourer en profondeur.""",
        'weekly_advice': {
            'week_1': "Identifie 2-3 sources de plaisir à cultiver ce mois.",
            'week_2': "Autorise-toi la curiosité et l'exploration.",
            'week_3': "Reviens à l'essentiel et approfondis ce qui compte.",
            'week_4': "Célèbre l'équilibre entre variété et profondeur."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Création tendre**

Ta Lune en Taureau en Maison 5 veut créer et profiter avec ses sens. Ton Ascendant Cancer ajoute de l'émotion : tes créations expriment tes sentiments, tes plaisirs nourrissent ton cœur.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs sont teintés de tendresse et de nostalgie. Tu veux créer quelque chose qui touche les cœurs, aimer avec douceur, profiter en famille.

**Ton approche instinctive** : Le Cancer te fait créer pour exprimer et guérir tes émotions. Tes œuvres sont personnelles, intimes, chargées de mémoire. Cette sensibilité peut enrichir ou vulnérabiliser ton expression.

**Tensions possibles** : La peur de te montrer peut bloquer ton expression créative. Tu risques de censurer tes créations ou tes plaisirs par pudeur ou peur du jugement.

**Conseil clé** : Créer et profiter avec authenticité émotionnelle tout en gardant des limites saines.""",
        'weekly_advice': {
            'week_1': "Identifie une émotion que tu veux exprimer créativement.",
            'week_2': "Crée quelque chose de personnel et touchant.",
            'week_3': "Partage ta création avec des personnes de confiance.",
            'week_4': "Savoure la connexion créée par ta vulnérabilité."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Rayonnement créatif**

Ta Lune en Taureau en Maison 5 veut créer avec authenticité et savourer les plaisirs simples. Ton Ascendant Lion, maître naturel de cette maison, ajoute du panache : tu veux briller, être vu·e, célébré·e pour ta créativité.

**Domaine activé** : Maison 5 — Ta créativité, tes amours et tes plaisirs demandent à rayonner. Tu veux créer quelque chose d'impressionnant, aimer généreusement, profiter avec magnificence.

**Ton approche instinctive** : Le Lion te fait créer pour toucher un public, séduire avec charisme, profiter avec grandeur. Cette confiance peut libérer ton talent ou devenir de la vanité.

**Tensions possibles** : Le besoin d'approbation peut te faire perdre ton authenticité taurine. Tu risques de créer pour plaire plutôt que pour exprimer ta vérité.

**Conseil clé** : Rayonner dans ta créativité tout en restant fidèle à ton expression personnelle.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment exprimer au monde.",
            'week_2': "Crée avec générosité et confiance.",
            'week_3': "Partage ta création sans attendre de validation.",
            'week_4': "Célèbre ton talent tout en restant humble et authentique."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Artisanat parfait**

Double terre sur la Maison 5 : ta Lune en Taureau et ton Ascendant Vierge créent une approche méticuleuse de la créativité. Tu veux créer quelque chose de beau ET de parfaitement exécuté.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs sont orientés vers l'excellence et l'utilité. Tu veux que tes créations soient à la fois belles et fonctionnelles, que tes plaisirs soient sains.

**Ton approche instinctive** : La Vierge te fait peaufiner chaque détail de tes créations. Tu analyses, améliores, perfectionnes. Cette exigence peut produire de l'excellence ou bloquer ta spontanéité.

**Tensions possibles** : Le perfectionnisme peut t'empêcher de créer ou de profiter. Tu risques de critiquer tes œuvres au lieu de les savourer.

**Conseil clé** : Viser l'excellence dans ta créativité sans perdre la joie de créer et de profiter.""",
        'weekly_advice': {
            'week_1': "Identifie un projet créatif qui mérite ton attention méticuleuse.",
            'week_2': "Crée avec soin et présence.",
            'week_3': "Accepte l'imperfection comme partie du charme.",
            'week_4': "Savoure ce que tu as accompli sans le dévaluer."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Beauté harmonieuse**

Double Vénus sur la Maison 5 : ta Lune en Taureau et ton Ascendant Balance créent une approche esthétique raffinée de la créativité. Tu veux créer et profiter avec harmonie et élégance.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs cherchent la beauté sous toutes ses formes. Tu veux créer des œuvres harmonieuses, aimer avec romance, profiter avec raffinement.

**Ton approche instinctive** : La Balance te fait créer pour toucher les sens et l'âme. Tu cherches l'équilibre esthétique, tu séduis avec charme. Cette recherche d'harmonie peut produire de la beauté ou de la superficialité.

**Tensions possibles** : La difficulté à assumer une créativité dissonante ou dérangeante. Tu risques de privilégier le joli au détriment de l'authentique.

**Conseil clé** : Créer et profiter avec beauté tout en restant fidèle à ta vérité même imparfaite.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui est vraiment beau pour toi, au-delà des conventions.",
            'week_2': "Crée quelque chose qui allie harmonie et authenticité.",
            'week_3': "Autorise-toi l'imperfection esthétique si elle sert ton expression.",
            'week_4': "Savoure la beauté que tu as créée et partagée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Passion intense**

Opposition Taureau-Scorpion sur la Maison 5 : ta Lune veut des plaisirs simples et sensuels. Ton Ascendant Scorpion ajoute de l'intensité : tes créations touchent les profondeurs, tes amours sont magnétiques.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs cherchent la transformation et la vérité. Tu veux créer quelque chose qui dérange et fascine, aimer avec passion obsessionnelle, profiter intensément.

**Ton approche instinctive** : Le Scorpion te fait créer depuis tes abîmes personnels. Tes œuvres explorent l'ombre, tes amours sont fusionnelles. Cette intensité peut être puissante ou destructrice.

**Tensions possibles** : L'excès de contrôle ou de possessivité dans tes plaisirs et amours. Tu risques de basculer dans l'obsession ou la jalousie.

**Conseil clé** : Créer et aimer avec intensité tout en respectant la légèreté et la liberté.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment explorer créativement.",
            'week_2': "Crée depuis ta vérité la plus profonde sans censure.",
            'week_3': "Aime passionnément sans perdre ton individualité.",
            'week_4': "Observe comment l'intensité a transformé ton expression."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Joie expansive**

Ta Lune en Taureau en Maison 5 veut des plaisirs concrets et sensuels. Ton Ascendant Sagittaire ajoute de l'expansion : tu veux que tes créations touchent le monde, que tes plaisirs soient des aventures.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs cherchent le sens et l'horizon. Tu veux créer quelque chose qui inspire, aimer librement, profiter avec enthousiasme.

**Ton approche instinctive** : Le Sagittaire te fait créer pour partager une vision, explorer de nouvelles formes de plaisir, aimer avec optimisme. Cette générosité peut enrichir ta vie ou créer de l'excès.

**Tensions possibles** : Le besoin de sécurité du Taureau peut freiner l'audace créative du Sagittaire. Tu risques de te retenir par peur de sortir de ta zone de confort.

**Conseil clé** : Explorer largement dans ta créativité et tes plaisirs tout en gardant un ancrage.""",
        'weekly_advice': {
            'week_1': "Identifie une forme de créativité ou de plaisir à explorer.",
            'week_2': "Ose sortir de ta zone de confort artistique ou ludique.",
            'week_3': "Garde ce qui résonne avec ton essence profonde.",
            'week_4': "Savoure l'équilibre entre confort et aventure."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Création sérieuse**

Ta Lune en Taureau en Maison 5 veut créer et profiter avec authenticité. Ton Ascendant Capricorne ajoute de la discipline : tu veux que ta créativité serve un objectif, que tes plaisirs soient productifs.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs sont orientés vers l'accomplissement et la reconnaissance. Tu veux créer une œuvre durable, aimer de manière constructive.

**Ton approche instinctive** : Le Capricorne te fait professionnaliser ta créativité. Tu structures tes projets artistiques, tu planifies tes plaisirs. Cette discipline peut produire de l'excellence ou étouffer la joie.

**Tensions possibles** : L'excès de sérieux peut tuer le plaisir et la spontanéité créative. Tu risques de transformer tes loisirs en obligations.

**Conseil clé** : Structurer ta créativité pour l'excellence tout en gardant la joie pure de créer.""",
        'weekly_advice': {
            'week_1': "Définis un objectif créatif ambitieux mais joyeux.",
            'week_2': "Travaille sur ta création avec discipline et plaisir.",
            'week_3': "Autorise-toi du temps pour jouer sans but.",
            'week_4': "Célèbre ce que tu as accompli et savouré."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Art original**

Ta Lune en Taureau en Maison 5 veut créer de manière classique et sensorielle. Ton Ascendant Verseau ajoute de l'innovation : tu explores des formes d'expression avant-gardistes, des plaisirs non-conventionnels.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs oscillent entre tradition et innovation. Tu veux créer quelque chose de nouveau tout en gardant une base solide.

**Ton approche instinctive** : Le Verseau te fait expérimenter dans ta créativité, explorer des plaisirs alternatifs. Cette originalité peut libérer ton expression ou te marginaliser artistiquement.

**Tensions possibles** : Le besoin de sécurité du Taureau peut freiner l'audace du Verseau. Tu risques d'osciller entre conformisme rassurant et rébellion artistique.

**Conseil clé** : Innover dans ta créativité tout en gardant un ancrage dans ce qui résonne vraiment.""",
        'weekly_advice': {
            'week_1': "Explore une forme d'expression ou de plaisir non-conventionnel.",
            'week_2': "Expérimente sans jugement ni pression de résultat.",
            'week_3': "Garde ce qui a du sens pour toi au-delà de l'originalité.",
            'week_4': "Intègre l'innovation qui enrichit vraiment ton expression."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Inspiration sensible**

Ta Lune en Taureau en Maison 5 veut créer avec ses mains et ses sens. Ton Ascendant Poissons ajoute de l'inspiration : ta créativité vient de ton intuition, tes plaisirs sont spirituels autant que sensuels.

**Domaine activé** : Maison 5 — Ta créativité et tes plaisirs sont à la fois concrets et transcendants. Tu veux créer quelque chose qui touche l'âme à travers les sens, profiter avec présence mystique.

**Ton approche instinctive** : Le Poissons te fait créer depuis tes rêves et visions. Tu te laisses guider par l'inspiration plutôt que la planification. Cette fluidité peut produire de la magie ou du chaos.

**Tensions possibles** : La difficulté à concrétiser tes visions créatives. Tu risques de rêver tes créations sans jamais les matérialiser.

**Conseil clé** : Laisser l'inspiration guider ta créativité tout en la matérialisant concrètement.""",
        'weekly_advice': {
            'week_1': "Écoute ton inspiration créative sans la juger.",
            'week_2': "Matérialise une vision en création tangible.",
            'week_3': "Profite des plaisirs avec présence méditative.",
            'week_4': "Savoure l'équilibre entre inspiration et manifestation."
        }
    },

    # ==================== MAISON 6 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Routine dynamique**

Ta Lune en Taureau en Maison 6 veut des habitudes stables et un rythme apaisant. Ton Ascendant Bélier ajoute de l'urgence : tu veux améliorer ton quotidien rapidement, optimiser ta santé avec intensité.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé oscillent entre stabilité nécessaire et besoin de changement. Tu veux une routine efficace mais pas ennuyeuse.

**Ton approche instinctive** : Le Bélier te pousse à révolutionner tes habitudes brutalement. Cette impulsion peut initier des changements nécessaires ou créer du chaos dans ta routine apaisante.

**Tensions possibles** : L'impatience du Bélier peut ruiner les efforts de régularité du Taureau. Tu risques de commencer fort puis abandonner tes nouvelles habitudes.

**Conseil clé** : Initier des changements dans ta routine tout en les maintenant avec patience.""",
        'weekly_advice': {
            'week_1': "Identifie une habitude quotidienne à améliorer.",
            'week_2': "Lance le changement avec énergie et engagement.",
            'week_3': "Maintiens la nouvelle routine même si c'est ennuyeux.",
            'week_4': "Savoure la stabilité que cette constance t'apporte."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Rituel ancré**

Double Taureau sur la Maison 6 : ton besoin de stabilité quotidienne est décuplé. Tu veux des routines solides, une santé robuste, un travail qui nourrit ton corps et ton compte en banque.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé demandent de la régularité absolue. Tu veux des habitudes qui te sécurisent, une routine qui t'ancre, un rythme qui te ressource.

**Ton approche instinctive** : Avec l'Ascendant Taureau, tu construis tes routines lentement mais sûrement. Tu aimes les rituels, les habitudes répétitives, la prévisibilité quotidienne. Cette stabilité peut être ressourçante ou étouffante.

**Tensions possibles** : La résistance excessive au changement peut te maintenir dans des habitudes dépassées. Tu risques de confondre confort et immobilisme.

**Conseil clé** : Créer des routines nourrissantes tout en restant ouvert aux ajustements nécessaires.""",
        'weekly_advice': {
            'week_1': "Observe quelles routines te nourrissent vraiment.",
            'week_2': "Renforce les habitudes qui te font du bien.",
            'week_3': "Identifie une habitude devenue automatisme mort.",
            'week_4': "Ajuste doucement pour plus de vitalité quotidienne."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Routine variée**

Ta Lune en Taureau en Maison 6 veut des habitudes stables et répétitives. Ton Ascendant Gémeaux ajoute de la variété : tu veux un quotidien structuré mais jamais ennuyeux, des routines flexibles.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé oscillent entre besoin de régularité et besoin de stimulation. Tu veux une base stable avec de la diversité.

**Ton approche instinctive** : Le Gémeaux te fait multiplier les activités quotidiennes, jongler entre plusieurs tâches. Cette polyvalence peut enrichir ton quotidien ou créer de la dispersion épuisante.

**Tensions possibles** : La difficulté à maintenir des routines par ennui. Tu risques de papillonner entre habitudes sans jamais les ancrer durablement.

**Conseil clé** : Créer une structure quotidienne stable avec de la variété à l'intérieur.""",
        'weekly_advice': {
            'week_1': "Définis 2-3 routines non-négociables pour ta stabilité.",
            'week_2': "Maintiens ces bases tout en variant les détails.",
            'week_3': "Expérimente de nouvelles activités dans ton cadre stable.",
            'week_4': "Évalue ce qui mérite de devenir une nouvelle habitude."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Cocon quotidien**

Ta Lune en Taureau en Maison 6 veut des habitudes concrètes et ressourçantes. Ton Ascendant Cancer ajoute de l'émotion : ton quotidien doit te nourrir émotionnellement, ta routine doit te protéger.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé sont liés à ton bien-être émotionnel. Tu veux des habitudes qui te sécurisent intérieurement, une routine qui te berce.

**Ton approche instinctive** : Le Cancer te fait créer un cocon quotidien. Tu cuisines pour te réconforter, tu organises ton espace pour te sentir en sécurité. Cette douceur peut être thérapeutique ou régressante.

**Tensions possibles** : La tendance à te replier dans des routines trop protectrices. Tu risques d'éviter ce qui te challengerait sainement par besoin de confort.

**Conseil clé** : Créer un quotidien nourrissant tout en t'exposant doucement à de nouveaux défis.""",
        'weekly_advice': {
            'week_1': "Identifie les routines qui te réconfortent vraiment.",
            'week_2': "Renforce ton cocon quotidien avec soin.",
            'week_3': "Sors doucement de ta zone de confort dans une activité.",
            'week_4': "Observe comment l'équilibre nourrit ta stabilité."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Routine rayonnante**

Ta Lune en Taureau en Maison 6 veut des habitudes simples et efficaces. Ton Ascendant Lion ajoute de la grandeur : tu veux un quotidien qui te mette en valeur, une routine qui reflète ta qualité.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé doivent avoir de la classe. Tu veux des habitudes dignes de toi, une routine qui impressionne, un mode de vie exemplaire.

**Ton approche instinctive** : Le Lion te fait théâtraliser ton quotidien. Tu transformes ta routine en performance, tu veux être admiré pour ta discipline. Cette fierté peut te motiver ou créer de la pression.

**Tensions possibles** : L'ego blessé quand ta routine n'est pas parfaite ou reconnue. Tu risques de te décourager si tes efforts ne sont pas applaudis.

**Conseil clé** : Créer un quotidien de qualité pour toi-même, pas pour l'audience.""",
        'weekly_advice': {
            'week_1': "Définis une routine qui te rend fier sans chercher la validation.",
            'week_2': "Maintiens tes standards même dans l'invisible.",
            'week_3': "Trouve de la dignité dans les tâches simples.",
            'week_4': "Célèbre ta constance pour toi-même."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfection quotidienne**

Ta Lune en Taureau en Maison 6 veut des habitudes solides et confortables. Ton Ascendant Vierge ajoute de l'analyse : tu veux optimiser chaque détail de ton quotidien, perfectionner ta routine, maximiser ta santé.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé sont sous le microscope. Tu veux tout améliorer, tout rationaliser, tout purifier. L'excellence pratique devient ta quête.

**Ton approche instinctive** : La Vierge te fait analyser et ajuster constamment tes habitudes. Tu optimises ton alimentation, ton sommeil, ton organisation. Cette précision peut produire du bien-être ou de l'obsession.

**Tensions possibles** : Le perfectionnisme qui rend ton quotidien anxiogène. Tu risques de transformer tes routines en obligations stressantes impossible à satisfaire.

**Conseil clé** : Viser l'excellence pratique tout en acceptant l'imperfection humaine.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect de ta routine à optimiser.",
            'week_2': "Améliore avec méthode sans devenir obsessionnel.",
            'week_3': "Accepte qu'une bonne routine vaut mieux qu'une parfaite.",
            'week_4': "Savoure le bien-être pratique que tu as créé."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre quotidien**

Ta Lune en Taureau en Maison 6 veut des routines stables et concrètes. Ton Ascendant Balance ajoute de l'harmonie : tu veux un quotidien équilibré, une routine esthétique, un travail relationnel.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé recherchent la beauté et l'équilibre. Tu veux une routine agréable visuellement, des habitudes harmonieuses, un environnement de travail plaisant.

**Ton approche instinctive** : La Balance te fait rechercher le juste milieu dans tes habitudes. Tu équilibres travail et repos, effort et plaisir. Cette quête d'harmonie peut créer du bien-être ou de l'indécision chronique.

**Tensions possibles** : La difficulté à trancher et maintenir une routine par peur de déséquilibrer. Tu risques de procrastiner sur l'organisation par besoin de considérer tous les angles.

**Conseil clé** : Créer un quotidien harmonieux en acceptant qu'aucun équilibre n'est permanent.""",
        'weekly_advice': {
            'week_1': "Identifie les déséquilibres dans ton quotidien.",
            'week_2': "Choisis une routine qui rééquilibre sans sur-analyser.",
            'week_3': "Maintiens cette routine même si l'équilibre parfait n'existe pas.",
            'week_4': "Ajuste doucement en fonction de ton ressenti."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Routine intense**

Ta Lune en Taureau en Maison 6 veut des habitudes simples et apaisantes. Ton Ascendant Scorpion ajoute de l'intensité : tu veux transformer ton quotidien en profondeur, purger tes mauvaises habitudes, régénérer ta santé.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé deviennent un terrain de transformation. Tu veux des habitudes qui te régénèrent, une routine qui te purifie, un travail qui a du sens profond.

**Ton approche instinctive** : Le Scorpion te fait aborder ta routine avec passion. Tu t'engages à fond dans tes nouvelles habitudes ou tu les rejettes totalement. Cette intensité peut créer de vraies transformations ou du burn-out.

**Tensions possibles** : L'obsession pour certaines routines ou l'auto-sabotage quand tu perds le contrôle. Tu risques de basculer dans l'excès ou l'abandon.

**Conseil clé** : Transformer ton quotidien en profondeur tout en gardant de la douceur.""",
        'weekly_advice': {
            'week_1': "Identifie une habitude toxique à éliminer complètement.",
            'week_2': "Purge cette habitude sans compromis mais sans violence.",
            'week_3': "Installe une nouvelle routine régénératrice à la place.",
            'week_4': "Observe la transformation que cela crée en toi."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Liberté quotidienne**

Ta Lune en Taureau en Maison 6 veut des routines prévisibles et sécurisantes. Ton Ascendant Sagittaire ajoute de l'expansion : tu veux un quotidien qui t'ouvre des horizons, des habitudes qui te libèrent, un travail qui a du sens.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé oscillent entre besoin de structure et besoin de liberté. Tu veux une routine qui ne t'enferme pas, des habitudes qui te propulsent.

**Ton approche instinctive** : Le Sagittaire te fait résister aux routines trop rigides. Tu veux de la spontanéité dans ton quotidien, de la variété dans tes habitudes. Cette liberté peut être vivifiante ou chaotique.

**Tensions possibles** : La rébellion contre toute discipline quotidienne par besoin de liberté. Tu risques de manquer de structure et de t'épuiser dans le chaos.

**Conseil clé** : Créer une structure quotidienne légère qui te libère au lieu de t'enfermer.""",
        'weekly_advice': {
            'week_1': "Identifie les routines qui t'étouffent vraiment.",
            'week_2': "Allège ta structure tout en gardant les bases essentielles.",
            'week_3': "Intègre de l'aventure dans ton quotidien cadré.",
            'week_4': "Savoure la liberté que te donne cette discipline légère."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Discipline productive**

Ta Lune en Taureau en Maison 6 veut des habitudes confortables et durables. Ton Ascendant Capricorne ajoute de l'ambition : tu veux un quotidien productif, des routines qui te font progresser, une santé optimale pour performer.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé sont orientés vers l'accomplissement. Tu veux des habitudes qui construisent ton succès, une routine de champion, une discipline de fer.

**Ton approche instinctive** : Le Capricorne te fait structurer ton quotidien comme un athlète professionnel. Tu planifies, tu optimises, tu persévères. Cette rigueur peut produire de l'excellence ou de l'épuisement.

**Tensions possibles** : Le surmenage par excès de discipline et manque de repos. Tu risques de transformer ta vie quotidienne en machine à produire sans joie.

**Conseil clé** : Construire une routine productive tout en préservant le plaisir simple de vivre.""",
        'weekly_advice': {
            'week_1': "Définis une routine ambitieuse mais soutenable.",
            'week_2': "Maintiens cette discipline avec constance.",
            'week_3': "Intègre du plaisir pur dans ton quotidien structuré.",
            'week_4': "Célèbre ce que tu as accompli ET savouré."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Routine alternative**

Ta Lune en Taureau en Maison 6 veut des habitudes traditionnelles et rassurantes. Ton Ascendant Verseau ajoute de l'innovation : tu explores des routines non-conventionnelles, des approches de santé alternatives, un travail atypique.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé oscillent entre tradition et innovation. Tu veux des habitudes qui marchent tout en étant original dans ton approche.

**Ton approche instinctive** : Le Verseau te fait expérimenter des routines inhabituelles. Tu testes des méthodes de santé alternatives, tu organises ton travail différemment. Cette originalité peut être libératrice ou déstabilisante.

**Tensions possibles** : L'instabilité créée par trop d'expérimentation. Tu risques de changer constamment de routine sans jamais bénéficier de la constance.

**Conseil clé** : Innover dans ton quotidien tout en maintenant une base stable qui fonctionne.""",
        'weekly_advice': {
            'week_1': "Garde les routines de base qui te stabilisent vraiment.",
            'week_2': "Expérimente une approche alternative dans un domaine.",
            'week_3': "Évalue objectivement si l'innovation t'apporte du bien.",
            'week_4': "Intègre ce qui fonctionne vraiment pour toi."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Rituel intuitif**

Ta Lune en Taureau en Maison 6 veut des routines concrètes et terre-à-terre. Ton Ascendant Poissons ajoute de l'intuition : tu veux un quotidien qui nourrit ton âme, des habitudes spirituelles, une approche holistique de la santé.

**Domaine activé** : Maison 6 — Ton quotidien, ton travail, ta santé intègrent le spirituel et le matériel. Tu veux des routines qui ancrent ton corps tout en élevant ton esprit.

**Ton approche instinctive** : Le Poissons te fait suivre ton intuition dans tes habitudes quotidiennes. Tu médites, tu écoutes ton corps, tu te laisses guider. Cette fluidité peut être ressourçante ou désorganisante.

**Tensions possibles** : La difficulté à maintenir une structure par manque de discipline. Tu risques de t'évaporer dans tes rêves au lieu de gérer ton quotidien concrètement.

**Conseil clé** : Écouter ton intuition pour créer une routine qui nourrit corps et âme.""",
        'weekly_advice': {
            'week_1': "Écoute ce que ton corps et ton âme réclament vraiment.",
            'week_2': "Crée une routine simple qui honore ces besoins.",
            'week_3': "Maintiens cette routine même quand l'inspiration fluctue.",
            'week_4': "Savoure l'équilibre entre structure et fluidité."
        }
    },

    # ==================== MAISON 7 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Relation directe**

Ta Lune en Taureau en Maison 7 veut des relations stables et durables. Ton Ascendant Bélier ajoute de l'impulsion : tu veux conquérir l'autre rapidement, clarifier les choses brutalement, affirmer tes besoins sans détour.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements oscillent entre besoin de stabilité et impulsion du moment. Tu veux de la loyauté mais tu agis avec spontanéité.

**Ton approche instinctive** : Le Bélier te fait foncer dans les relations. Tu clarifie ce que tu veux rapidement, tu confrontes les problèmes directement. Cette franchise peut assainir ou brusquer la relation.

**Tensions possibles** : L'impatience qui brusque la lente construction de confiance nécessaire au Taureau. Tu risques de forcer l'engagement trop vite ou de fuir par frustration.

**Conseil clé** : Affirmer clairement tes besoins tout en laissant la relation mûrir à son rythme.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment dans tes relations.",
            'week_2': "Exprime tes besoins clairement mais sans ultimatum.",
            'week_3': "Laisse l'autre digérer et répondre à son rythme.",
            'week_4': "Observe si la stabilité se construit naturellement."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Engagement total**

Double Taureau sur la Maison 7 : ton besoin de relations stables et engagées est décuplé. Tu veux un partenariat solide, une loyauté absolue, une relation qui dure pour la vie.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements cherchent la sécurité maximale. Tu veux construire quelque chose de durable avec l'autre, créer une base inébranlable ensemble.

**Ton approche instinctive** : Avec l'Ascendant Taureau, tu construis tes relations lentement mais sûrement. Tu prends ton temps pour t'engager mais une fois engagé, c'est pour de bon. Cette fidélité peut être magnifique ou possessive.

**Tensions possibles** : La possessivité et la résistance au changement dans la relation. Tu risques de confondre stabilité et immobilisme, sécurité et contrôle.

**Conseil clé** : Construire une relation stable tout en laissant l'espace de l'évolution.""",
        'weekly_advice': {
            'week_1': "Observe ce qui te sécurise vraiment dans tes relations.",
            'week_2': "Communique tes besoins de stabilité sans exiger.",
            'week_3': "Laisse de l'espace pour que l'autre respire aussi.",
            'week_4': "Savoure la sécurité que crée la confiance mutuelle."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Dialogue ancré**

Ta Lune en Taureau en Maison 7 veut une relation stable et prévisible. Ton Ascendant Gémeaux ajoute de la communication : tu veux dialoguer constamment, échanger des idées, garder la relation vivante intellectuellement.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements oscillent entre besoin de stabilité et besoin de stimulation mentale. Tu veux une base solide avec des conversations passionnantes.

**Ton approche instinctive** : Le Gémeaux te fait communiquer beaucoup dans tes relations. Tu veux tout discuter, tout comprendre, tout explorer verbalement. Cette curiosité peut enrichir ou éparpiller la relation.

**Tensions possibles** : La difficulté à t'engager pleinement par peur de t'ennuyer. Tu risques de papillonner relationnellement au lieu de construire la profondeur.

**Conseil clé** : Communiquer abondamment tout en s'engageant dans la durée.""",
        'weekly_advice': {
            'week_1': "Identifie les sujets qui nourrissent vraiment ta relation.",
            'week_2': "Engage des conversations profondes et récurrentes.",
            'week_3': "Observe comment la répétition crée de l'intimité.",
            'week_4': "Savoure la richesse d'une relation stable ET stimulante."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Cocon à deux**

Ta Lune en Taureau en Maison 7 veut une relation concrète et stable. Ton Ascendant Cancer ajoute de l'émotion : tu veux une relation qui te nourrit émotionnellement, un partenariat qui te protège, un amour qui te berce.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements cherchent la sécurité totale. Tu veux créer un cocon avec l'autre, une famille, un nid douillet où vous protéger mutuellement.

**Ton approche instinctive** : Le Cancer te fait fusionner émotionnellement avec ton partenaire. Tu nourris la relation avec soin, tu crées de l'intimité profonde. Cette tendresse peut créer de la beauté ou de la dépendance.

**Tensions possibles** : La fusion excessive qui étouffe l'autonomie de chacun. Tu risques de devenir trop dépendant ou possessif par besoin de sécurité affective.

**Conseil clé** : Créer une intimité profonde tout en préservant l'individualité de chacun.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu nourris vraiment ta relation.",
            'week_2': "Renforce l'intimité émotionnelle avec authenticité.",
            'week_3': "Prends du temps pour toi sans culpabiliser.",
            'week_4': "Observe comment l'autonomie renforce votre lien."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Loyauté fière**

Ta Lune en Taureau en Maison 7 veut une relation simple et loyale. Ton Ascendant Lion ajoute de la grandeur : tu veux une relation admirée, un partenariat qui te met en valeur, un amour dont tu es fier.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements doivent avoir de la classe. Tu veux un partenaire à la hauteur, une relation exemplaire, un couple qui rayonne.

**Ton approche instinctive** : Le Lion te fait briller dans ta relation. Tu veux être admiré par ton partenaire et admirer l'autre. Cette fierté peut créer de la noblesse ou de l'ego démesuré.

**Tensions possibles** : L'ego blessé qui sabote la relation ou la compétition pour savoir qui brille le plus. Tu risques de vouloir dominer au lieu de co-créer.

**Conseil clé** : Créer une relation digne tout en honorant l'égalité des partenaires.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui rend ta relation vraiment spéciale.",
            'week_2': "Célèbre les qualités de ton partenaire sincèrement.",
            'week_3': "Laisse-toi admirer sans dominer l'espace.",
            'week_4': "Savoure la fierté mutuelle que vous créez."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Service mutuel**

Ta Lune en Taureau en Maison 7 veut une relation confortable et stable. Ton Ascendant Vierge ajoute de la précision : tu veux améliorer la relation, servir ton partenaire utilement, optimiser votre fonctionnement ensemble.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements sont analysés et perfectionnés. Tu veux une relation qui fonctionne bien pratiquement, un partenariat efficace, un amour utile.

**Ton approche instinctive** : La Vierge te fait analyser la relation en détail. Tu notes ce qui fonctionne et ce qui doit être amélioré. Cette précision peut créer de l'excellence ou de la critique constante.

**Tensions possibles** : Le perfectionnisme qui rend la relation anxiogène. Tu risques de critiquer ton partenaire au lieu d'accepter ses imperfections humaines.

**Conseil clé** : Améliorer la relation par service concret tout en acceptant l'imperfection.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect pratique de ta relation à améliorer.",
            'week_2': "Agis pour améliorer sans critiquer l'autre.",
            'week_3': "Accepte consciemment une imperfection de ton partenaire.",
            'week_4': "Savoure la relation fonctionnelle et humaine que vous créez."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie solide**

Ta Lune en Taureau en Maison 7 veut une relation stable et loyale. Ton Ascendant Balance ajoute de l'équilibre : tu veux une harmonie parfaite, une beauté relationnelle, une justice dans le partenariat.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements cherchent l'équilibre idéal. Tu veux une relation où chacun donne et reçoit équitablement, où l'harmonie règne, où la beauté est présente.

**Ton approche instinctive** : La Balance te fait rechercher constamment l'harmonie dans ta relation. Tu équilibres les besoins de chacun, tu adoucis les conflits. Cette diplomatie peut créer de la paix ou de l'évitement.

**Tensions possibles** : L'évitement des conflits nécessaires par peur de déséquilibrer. Tu risques de sacrifier tes besoins pour maintenir une harmonie superficielle.

**Conseil clé** : Créer une harmonie authentique en incluant les désaccords constructifs.""",
        'weekly_advice': {
            'week_1': "Identifie les déséquilibres réels dans ta relation.",
            'week_2': "Communique tes besoins calmement mais clairement.",
            'week_3': "Traverse le conflit pour atteindre un nouvel équilibre.",
            'week_4': "Savoure l'harmonie plus profonde que vous avez créée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Fusion intense**

Ta Lune en Taureau en Maison 7 veut une relation simple et stable. Ton Ascendant Scorpion ajoute de l'intensité : tu veux une relation totale, une fusion complète, une loyauté absolue ou rien.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements deviennent profonds et transformateurs. Tu veux tout partager avec l'autre, tout vivre intensément, fusionner complètement.

**Ton approche instinctive** : Le Scorpion te fait plonger dans les profondeurs relationnelles. Tu veux connaître tous les secrets de l'autre, créer une intimité totale. Cette intensité peut créer de la magie ou de l'obsession.

**Tensions possibles** : La jalousie, la possessivité, le contrôle excessif par peur d'être trahi. Tu risques d'étouffer la relation par ton intensité.

**Conseil clé** : Créer une intimité profonde tout en respectant les mystères de l'autre.""",
        'weekly_advice': {
            'week_1': "Identifie tes peurs dans la relation sans les projeter.",
            'week_2': "Partage tes vulnérabilités au lieu de contrôler.",
            'week_3': "Fais confiance même quand c'est inconfortable.",
            'week_4': "Observe comment la confiance approfondit votre intimité."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Liberté partagée**

Ta Lune en Taureau en Maison 7 veut une relation stable et sécurisante. Ton Ascendant Sagittaire ajoute de l'expansion : tu veux une relation qui te libère, un partenariat qui vous fait grandir, un amour qui ouvre des horizons.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements oscillent entre besoin de sécurité et besoin de liberté. Tu veux une base stable avec de l'aventure partagée.

**Ton approche instinctive** : Le Sagittaire te fait résister à l'enfermement relationnel. Tu veux explorer le monde avec ton partenaire, partager des aventures, grandir ensemble. Cette expansion peut enrichir ou disperser la relation.

**Tensions possibles** : La peur de l'engagement par crainte de perdre ta liberté. Tu risques de fuir la profondeur par besoin d'horizons nouveaux.

**Conseil clé** : Créer une relation stable qui vous libère tous les deux.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui t'étouffe vraiment dans la relation.",
            'week_2': "Communique ton besoin de liberté avec responsabilité.",
            'week_3': "Crée de l'aventure partagée dans votre engagement.",
            'week_4': "Savoure la stabilité que crée votre liberté mutuelle."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Partenariat solide**

Ta Lune en Taureau en Maison 7 veut une relation durable et loyale. Ton Ascendant Capricorne ajoute de l'ambition : tu veux un partenariat qui construit quelque chose, une relation qui vous fait progresser, un engagement sérieux.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements sont orientés vers l'accomplissement. Tu veux construire une vie ensemble, atteindre des objectifs communs, créer un héritage à deux.

**Ton approche instinctive** : Le Capricorne te fait aborder la relation avec sérieux. Tu planifies l'avenir ensemble, tu construis méthodiquement. Cette maturité peut créer de la solidité ou de la froideur.

**Tensions possibles** : La transformation de la relation en projet au détriment de l'intimité. Tu risques d'oublier de simplement aimer dans ta quête d'accomplissement commun.

**Conseil clé** : Construire ensemble tout en préservant la tendresse simple.""",
        'weekly_advice': {
            'week_1': "Identifie un objectif commun qui vous motive vraiment.",
            'week_2': "Planifiez ensemble les étapes concrètes.",
            'week_3': "Prenez du temps pour la tendresse sans but.",
            'week_4': "Célébrez votre progression ET votre amour."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Amitié stable**

Ta Lune en Taureau en Maison 7 veut une relation traditionnelle et rassurante. Ton Ascendant Verseau ajoute de l'originalité : tu veux une relation non-conventionnelle, un partenariat d'égaux libres, un amour atypique.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements oscillent entre tradition et innovation. Tu veux une base stable avec une forme relationnelle unique.

**Ton approche instinctive** : Le Verseau te fait expérimenter des formes de relation alternatives. Tu veux de l'amitié autant que de l'amour, de l'indépendance dans l'engagement. Cette originalité peut libérer ou dérouter.

**Tensions possibles** : La difficulté à t'engager dans une forme traditionnelle qui sécurise le Taureau. Tu risques d'osciller entre désir de stabilité et besoin de liberté totale.

**Conseil clé** : Créer une relation originale qui vous stabilise tous les deux.""",
        'weekly_advice': {
            'week_1': "Identifie quelle forme de relation résonne vraiment.",
            'week_2': "Communique tes besoins d'autonomie dans l'engagement.",
            'week_3': "Co-créez des règles qui libèrent et sécurisent.",
            'week_4': "Savoure votre relation unique et stable."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Amour transcendant**

Ta Lune en Taureau en Maison 7 veut une relation concrète et tangible. Ton Ascendant Poissons ajoute de la spiritualité : tu veux une relation qui transcende le quotidien, un amour mystique, une fusion d'âmes.

**Domaine activé** : Maison 7 — Tes relations, tes partenariats, tes engagements mêlent le matériel et le spirituel. Tu veux une relation ancrée dans le réel mais ouverte sur l'invisible.

**Ton approche instinctive** : Le Poissons te fait idéaliser ta relation. Tu vois l'âme de l'autre, tu ressens une connexion mystique. Cette sensibilité peut créer de la beauté ou de l'illusion.

**Tensions possibles** : La difficulté à voir l'autre clairement à travers tes projections. Tu risques de t'accrocher à l'image idéalisée au lieu de la personne réelle.

**Conseil clé** : Honorer la dimension spirituelle de votre lien tout en voyant l'humain réel.""",
        'weekly_advice': {
            'week_1': "Observe ton partenaire sans filtre ni idéalisation.",
            'week_2': "Accueille l'humain imparfait avec compassion.",
            'week_3': "Honore aussi la connexion d'âme que vous partagez.",
            'week_4': "Savoure la relation qui embrasse humain et divin."
        }
    },

    # ==================== MAISON 8 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Transformation directe**

Ta Lune en Taureau en Maison 8 veut des ressources stables et une intimité sécurisante. Ton Ascendant Bélier ajoute de l'impulsion : tu veux transformer ta vie rapidement, affronter tes peurs brutalement, conquérir tes démons.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées demandent du courage. Tu dois lâcher l'ancien pour renaître, mais tu veux le faire vite.

**Ton approche instinctive** : Le Bélier te fait foncer dans les profondeurs. Tu affrontes tes peurs sans détour, tu provoques les crises pour les résoudre. Cette bravoure peut accélérer la transformation ou créer du chaos.

**Tensions possibles** : La précipitation dans les processus de transformation qui nécessitent du temps. Tu risques de forcer au lieu de laisser mûrir.

**Conseil clé** : Affronter courageusement tes profondeurs tout en respectant leur rythme.""",
        'weekly_advice': {
            'week_1': "Identifie une peur ou un attachement qui te limite.",
            'week_2': "Affronte cette profondeur avec courage mais sans violence.",
            'week_3': "Laisse la transformation opérer à son rythme.",
            'week_4': "Observe ce qui renaît de cette mort symbolique."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Transformation lente**

Double Taureau sur la Maison 8 : tu résistes aux transformations profondes mais quand tu changes, c'est pour de bon. Tu veux des ressources stables même dans l'incertitude, de la sécurité même dans l'intimité totale.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées se font lentement. Tu dois lâcher l'ancien mais chaque perte est difficile. La mort symbolique est ton plus grand défi.

**Ton approche instinctive** : Avec l'Ascendant Taureau, tu résistes au changement profond jusqu'à ce qu'il soit inévitable. Puis tu te transformes complètement mais lentement. Cette patience peut être sage ou entêtée.

**Tensions possibles** : La résistance excessive qui empêche les transformations nécessaires. Tu risques de t'accrocher à ce qui doit mourir par peur de l'inconnu.

**Conseil clé** : Accepter les transformations nécessaires tout en les vivant à ton rythme.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit vraiment mourir en toi.",
            'week_2': "Commence le processus de lâcher-prise doucement.",
            'week_3': "Persévère même si c'est inconfortable.",
            'week_4': "Savoure ce qui émerge de cette transformation."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Exploration profonde**

Ta Lune en Taureau en Maison 8 veut de la sécurité dans l'intimité. Ton Ascendant Gémeaux ajoute de la curiosité : tu veux comprendre tes profondeurs intellectuellement, explorer la psychologie, communiquer sur tes peurs.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées passent par la compréhension mentale. Tu analyses tes peurs, tu verbalisé tes traumas, tu explores tes tabous.

**Ton approche instinctive** : Le Gémeaux te fait intellectualiser tes profondeurs. Tu lis sur la psychologie, tu parles de tes peurs, tu analyses tes transformations. Cette approche peut éclairer ou éviter le ressenti.

**Tensions possibles** : La tendance à rester en surface par peur de plonger vraiment dans l'émotion brute. Tu risques de comprendre sans transformer.

**Conseil clé** : Explorer intellectuellement tes profondeurs tout en les ressentant vraiment.""",
        'weekly_advice': {
            'week_1': "Lis ou écoute sur un sujet psychologique qui te touche.",
            'week_2': "Applique cette compréhension à ton expérience réelle.",
            'week_3': "Ressens ce qui émerge au-delà des mots.",
            'week_4': "Intègre la compréhension ET le ressenti."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Intimité totale**

Ta Lune en Taureau en Maison 8 veut de la sécurité dans la vulnérabilité. Ton Ascendant Cancer ajoute de l'émotion : tu veux fusionner émotionnellement, créer une intimité totale, partager tes profondeurs.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées sont émotionnelles. Tu dois t'ouvrir complètement, montrer tes blessures, partager tes peurs les plus profondes.

**Ton approche instinctive** : Le Cancer te fait créer une intimité émotionnelle profonde. Tu nourris l'autre de ta vulnérabilité, tu crées un cocon dans lequel vous pouvez être totalement vrais. Cette fusion peut être thérapeutique ou fusionnelle.

**Tensions possibles** : La difficulté à maintenir des limites saines dans l'intimité. Tu risques de fusionner au point de perdre ton individualité ou de devenir dépendant émotionnellement.

**Conseil clé** : Créer une intimité profonde tout en gardant ton centre.""",
        'weekly_advice': {
            'week_1': "Identifie une vulnérabilité que tu caches encore.",
            'week_2': "Partage-la avec quelqu'un de confiance.",
            'week_3': "Observe ta tendance à fusionner ou te perdre.",
            'week_4': "Cultive l'intimité qui nourrit sans dissoudre."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Pouvoir personnel**

Ta Lune en Taureau en Maison 8 veut des ressources stables et durables. Ton Ascendant Lion ajoute de la puissance : tu veux du pouvoir personnel, de la reconnaissance pour ta force intérieure, de l'éclat même dans l'ombre.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées touchent ton pouvoir personnel. Tu dois revendiquer ta puissance, affirmer ta dignité dans la vulnérabilité.

**Ton approche instinctive** : Le Lion te fait briller même dans les profondeurs. Tu transformes tes blessures en force, tu rayonnes depuis ton authenticité. Cette fierté peut être inspirante ou refuser la vraie vulnérabilité.

**Tensions possibles** : L'ego qui refuse de s'effondrer pour permettre la vraie transformation. Tu risques de vouloir contrôler l'image au lieu de lâcher prise.

**Conseil clé** : Affirmer ta puissance tout en acceptant de te défaire pour renaître.""",
        'weekly_advice': {
            'week_1': "Identifie où ton ego te protège de ta transformation.",
            'week_2': "Accepte de perdre le contrôle de ton image.",
            'week_3': "Traverse la vulnérabilité avec dignité.",
            'week_4': "Rayonne depuis ta vérité transformée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Guérison pratique**

Ta Lune en Taureau en Maison 8 veut de la sécurité dans les crises. Ton Ascendant Vierge ajoute de la méthode : tu veux guérir méthodiquement, purifier tes blessures, optimiser ta transformation.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées passent par la guérison concrète. Tu analyses tes blessures, tu identifies les patterns, tu te soignes avec précision.

**Ton approche instinctive** : La Vierge te fait aborder ta guérison avec méthode. Tu cherches les causes, tu appliques des solutions pratiques, tu améliores méthodiquement. Cette approche peut être efficace ou éviter la profondeur émotionnelle.

**Tensions possibles** : Le perfectionnisme qui empêche d'accepter les parts d'ombre. Tu risques de vouloir tout purifier au lieu d'intégrer toutes tes parts.

**Conseil clé** : Guérir méthodiquement tout en acceptant tes zones d'ombre.""",
        'weekly_advice': {
            'week_1': "Identifie un pattern blessé qui se répète.",
            'week_2': "Analyse les causes avec clarté sans jugement.",
            'week_3': "Applique une action concrète de guérison.",
            'week_4': "Accepte que la guérison soit un processus imparfait."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre des ombres**

Ta Lune en Taureau en Maison 8 veut de la stabilité dans la vulnérabilité. Ton Ascendant Balance ajoute de l'harmonie : tu veux équilibrer tes ombres et ta lumière, partager tes profondeurs avec justesse.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées cherchent l'équilibre. Tu dois intégrer tes parts sombres avec grâce, créer de l'harmonie dans le chaos.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre même dans tes profondeurs. Tu veux transformer avec élégance, partager tes ressources équitablement. Cette recherche d'harmonie peut adoucir ou éviter la nécessaire confrontation.

**Tensions possibles** : L'évitement des profondeurs dérangeantes par besoin d'harmonie. Tu risques de rester en surface pour ne pas déséquilibrer.

**Conseil clé** : Plonger dans tes profondeurs pour atteindre un équilibre plus vrai.""",
        'weekly_advice': {
            'week_1': "Identifie une part d'ombre que tu évites par politesse.",
            'week_2': "Accueille-la même si elle dérange ton harmonie.",
            'week_3': "Trouve comment l'intégrer avec grâce.",
            'week_4': "Savoure l'équilibre plus profond que cela crée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Régénération totale**

Ta Lune en Taureau en Maison 8 résiste aux transformations profondes. Ton Ascendant Scorpion exige la mort et la renaissance : tu dois lâcher complètement pour renaître totalement. Ce mois est intense.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées demandent la régénération complète. Tu dois mourir symboliquement pour renaître plus fort, plus vrai.

**Ton approche instinctive** : Le Scorpion te plonge dans les profondeurs sans compromis. Tu explores tes zones les plus sombres, tu affrontes tes plus grandes peurs. Cette intensité peut être transformatrice ou dévastatrice.

**Tensions possibles** : L'obsession, la destruction excessive, la difficulté à reconstruire après avoir tout détruit. Tu risques de rester dans la crise au lieu de renaître.

**Conseil clé** : Traverser la mort symbolique pour permettre la vraie renaissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit vraiment mourir en toi.",
            'week_2': "Laisse cette mort s'accomplir sans résistance.",
            'week_3': "Traverse le vide avec confiance.",
            'week_4': "Accueille ce qui renaît naturellement."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Exploration mystique**

Ta Lune en Taureau en Maison 8 veut de la sécurité dans l'intimité. Ton Ascendant Sagittaire ajoute de l'exploration : tu veux comprendre le sens de tes crises, explorer la spiritualité, trouver la sagesse dans tes blessures.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées cherchent le sens. Tu veux que tes crises t'enseignent, que tes transformations t'élèvent, que ton intimité soit philosophique.

**Ton approche instinctive** : Le Sagittaire te fait chercher le sens dans tes profondeurs. Tu transformes tes blessures en sagesse, tu explores les philosophies de transformation. Cette quête peut éclairer ou éviter le ressenti brut.

**Tensions possibles** : La tendance à fuir dans la philosophie au lieu de ressentir vraiment. Tu risques de chercher le sens pour éviter la douleur.

**Conseil clé** : Chercher le sens dans tes transformations tout en les vivant pleinement.""",
        'weekly_advice': {
            'week_1': "Ressens une blessure sans chercher de sens immédiat.",
            'week_2': "Laisse la transformation opérer dans ton corps.",
            'week_3': "Observe quel sens émerge naturellement.",
            'week_4': "Intègre la sagesse que ta blessure t'offre."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Pouvoir structuré**

Ta Lune en Taureau en Maison 8 veut des ressources stables et durables. Ton Ascendant Capricorne ajoute de l'ambition : tu veux construire du pouvoir réel, maîtriser tes ressources partagées, transformer avec méthode.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées sont stratégiques. Tu veux transformer pour construire plus fort, partager pour accumuler du pouvoir, te renouveler pour progresser.

**Ton approche instinctive** : Le Capricorne te fait aborder tes transformations avec sérieux. Tu planifies ta guérison, tu structures ton intimité, tu gères tes ressources partagées professionnellement. Cette maîtrise peut créer de la solidité ou de la froideur.

**Tensions possibles** : La difficulté à lâcher le contrôle nécessaire à la vraie transformation. Tu risques de vouloir tout maîtriser au lieu de te laisser transformer.

**Conseil clé** : Construire du pouvoir réel tout en acceptant la perte de contrôle.""",
        'weekly_advice': {
            'week_1': "Identifie où tu contrôles par peur de te transformer.",
            'week_2': "Lâche méthodiquement ce contrôle une étape à la fois.",
            'week_3': "Observe la force qui émerge de ta vulnérabilité.",
            'week_4': "Construis depuis ce nouveau pouvoir authentique."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Libération profonde**

Ta Lune en Taureau en Maison 8 veut de la sécurité dans le changement. Ton Ascendant Verseau ajoute de la révolution : tu veux te libérer des attachements toxiques, transformer radicalement, expérimenter l'intimité autrement.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées cherchent la liberté. Tu veux te détacher de ce qui te limite, partager sans possessivité, transformer sans souffrance.

**Ton approche instinctive** : Le Verseau te fait expérimenter des formes alternatives de transformation. Tu explores des approches non-conventionnelles de guérison, tu redéfinis l'intimité. Cette originalité peut libérer ou éviter la profondeur émotionnelle.

**Tensions possibles** : La tendance à te détacher émotionnellement au lieu de transformer. Tu risques d'intellectualiser tes blessures pour éviter de les ressentir.

**Conseil clé** : Innover dans ta transformation tout en ressentant vraiment.""",
        'weekly_advice': {
            'week_1': "Explore une approche alternative de guérison.",
            'week_2': "Applique-la tout en restant connecté à ton ressenti.",
            'week_3': "Observe si tu te libères ou si tu évites.",
            'week_4': "Intègre ce qui te transforme vraiment."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 8, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution mystique**

Ta Lune en Taureau en Maison 8 veut de la solidité dans la transformation. Ton Ascendant Poissons ajoute de la dissolution : tu veux fusionner avec l'univers, transcender tes blessures, te dissoudre pour renaître.

**Domaine activé** : Maison 8 — Tes transformations, ton intimité profonde, tes ressources partagées deviennent spirituelles. Tu veux que tes crises soient des initiations mystiques, que ton intimité transcende l'ego.

**Ton approche instinctive** : Le Poissons te fait te dissoudre dans tes transformations. Tu te perds pour te retrouver, tu lâches prise totalement, tu te laisses transformer par l'invisible. Cette fluidité peut être transcendante ou désorganisante.

**Tensions possibles** : La difficulté à rester ancré pendant la transformation. Tu risques de te perdre complètement sans pouvoir revenir avec ce que tu as appris.

**Conseil clé** : Te dissoudre mystiquement tout en gardant un fil qui te ramène.""",
        'weekly_advice': {
            'week_1': "Laisse-toi aller dans une méditation profonde.",
            'week_2': "Explore la dissolution de ton ego dans l'intimité.",
            'week_3': "Ramène consciemment ce que tu as trouvé.",
            'week_4': "Ancre la sagesse mystique dans ta vie concrète."
        }
    },

    # ==================== MAISON 9 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Aventure solide**

Ta Lune en Taureau en Maison 9 veut des croyances stables et un apprentissage lent. Ton Ascendant Bélier ajoute de l'impulsion : tu veux explorer rapidement, conquérir de nouveaux horizons, affirmer ta vérité brutalement.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons oscillent entre besoin de certitude et soif d'aventure. Tu veux une philosophie solide mais tu t'ennuies dans la routine mentale.

**Ton approche instinctive** : Le Bélier te fait explorer avec audace. Tu fonçes vers de nouvelles idées, tu voyages impulsivement, tu affirmes tes croyances avec force. Cette bravoure peut ouvrir des portes ou créer des conflits idéologiques.

**Tensions possibles** : L'impatience qui t'empêche d'approfondir vraiment ton apprentissage. Tu risques de survoler les sujets au lieu de les intégrer durablement.

**Conseil clé** : Explorer courageusement tout en prenant le temps d'intégrer profondément.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans l'exploration d'un nouveau sujet.",
            'week_2': "Creuse au-delà de l'excitation initiale.",
            'week_3': "Intègre pratiquement ce que tu as appris.",
            'week_4': "Observe comment cette connaissance te transforme durablement."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sagesse enracinée**

Double Taureau sur la Maison 9 : tu veux des croyances solides qui résistent au temps, une philosophie concrète et pratique, un apprentissage qui porte ses fruits tangibles. La sagesse doit se prouver dans le réel.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons cherchent la solidité. Tu veux des vérités éprouvées, des connaissances utiles, une philosophie qui améliore ta vie concrètement.

**Ton approche instinctive** : Avec l'Ascendant Taureau, tu construis ta compréhension du monde lentement. Tu apprends par l'expérience répétée, tu intègres profondément, tu crées une philosophie personnelle enracinée. Cette patience peut créer de la sagesse ou de la rigidité.

**Tensions possibles** : La résistance aux nouvelles idées qui challengent tes croyances établies. Tu risques de t'enfermer dans ta vision au lieu d'évoluer.

**Conseil clé** : Construire une sagesse solide tout en restant ouvert à l'évolution.""",
        'weekly_advice': {
            'week_1': "Identifie une croyance qui te limite sans te servir.",
            'week_2': "Explore doucement une perspective alternative.",
            'week_3': "Teste pratiquement cette nouvelle compréhension.",
            'week_4': "Intègre ce qui enrichit vraiment ta sagesse."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Curiosité ancrée**

Ta Lune en Taureau en Maison 9 veut des vérités stables et durables. Ton Ascendant Gémeaux ajoute de la curiosité : tu veux tout apprendre, explorer mille sujets, comprendre toutes les perspectives.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons oscillent entre profondeur et diversité. Tu veux maîtriser un sujet mais tu es attiré par tant d'autres.

**Ton approche instinctive** : Le Gémeaux te fait papillonner intellectuellement. Tu lis beaucoup, tu explores différentes philosophies, tu accumules des connaissances. Cette curiosité peut enrichir ou disperser ton apprentissage.

**Tensions possibles** : La difficulté à approfondir par besoin de variété constante. Tu risques de tout effleurer sans jamais maîtriser vraiment.

**Conseil clé** : Explorer largement tout en approfondissant certains domaines clés.""",
        'weekly_advice': {
            'week_1': "Explore librement plusieurs sujets qui t'attirent.",
            'week_2': "Identifie celui qui résonne le plus profondément.",
            'week_3': "Approfondis ce sujet avec constance.",
            'week_4': "Savoure la maîtrise qui émerge de l'approfondissement."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sagesse nourricière**

Ta Lune en Taureau en Maison 9 veut des croyances concrètes et pratiques. Ton Ascendant Cancer ajoute de l'émotion : tu veux une philosophie qui nourrit, des croyances qui protègent, une sagesse qui berce.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons cherchent la sécurité émotionnelle. Tu veux une vision du monde qui te réconforte, des croyances qui te font sentir chez toi.

**Ton approche instinctive** : Le Cancer te fait chercher une sagesse maternelle. Tu apprends ce qui te nourrit émotionnellement, tu créés une philosophie qui te protège. Cette douceur peut être ressourçante ou limiter ton expansion.

**Tensions possibles** : La tendance à rejeter les idées qui déstabilisent ta sécurité émotionnelle. Tu risques de t'enfermer dans des croyances rassurantes mais limitantes.

**Conseil clé** : Créer une philosophie nourricière tout en t'ouvrant à l'inconfortable.""",
        'weekly_advice': {
            'week_1': "Identifie une croyance rassurante qui te limite.",
            'week_2': "Explore doucement ce qui te fait peur au-delà.",
            'week_3': "Intègre une vérité plus large avec bienveillance.",
            'week_4': "Observe comment cela enrichit ton monde intérieur."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Vérité rayonnante**

Ta Lune en Taureau en Maison 9 veut des croyances simples et solides. Ton Ascendant Lion ajoute de la grandeur : tu veux une philosophie noble, une vérité qui t'élève, une sagesse qui impressionne.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons cherchent la grandeur. Tu veux une vision du monde digne, des croyances qui te font briller, une sagesse royale.

**Ton approche instinctive** : Le Lion te fait affirmer tes vérités avec fierté. Tu veux être reconnu pour ta sagesse, admirer pour ta compréhension. Cette noblesse peut inspirer ou devenir arrogance.

**Tensions possibles** : L'ego qui t'empêche d'apprendre de ceux que tu perçois comme inférieurs. Tu risques de défendre tes croyances par fierté au lieu de chercher la vérité.

**Conseil clé** : Rayonner ta sagesse tout en restant humble dans l'apprentissage.""",
        'weekly_advice': {
            'week_1': "Identifie où ton ego bloque ton apprentissage.",
            'week_2': "Apprends de quelqu'un que tu sous-estimais.",
            'week_3': "Intègre cette humilité dans ta compréhension.",
            'week_4': "Rayonne une sagesse plus grande et plus humble."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Sagesse pratique**

Ta Lune en Taureau en Maison 9 veut des vérités concrètes et utiles. Ton Ascendant Vierge ajoute de la précision : tu veux une philosophie rationnelle, des croyances vérifiables, une sagesse applicable.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons cherchent l'utilité. Tu veux des connaissances qui améliorent ta vie pratiquement, une sagesse qui se mesure à ses résultats.

**Ton approche instinctive** : La Vierge te fait analyser chaque enseignement. Tu vérifies, tu testes, tu optimises ta compréhension. Cette rigueur peut créer de la maîtrise ou du scepticisme excessif.

**Tensions possibles** : Le rejet du mystère et de l'irrationnel par besoin de tout comprendre. Tu risques de t'enfermer dans le rationnel au détriment de la sagesse intuitive.

**Conseil clé** : Viser l'excellence dans ton apprentissage tout en acceptant le mystère.""",
        'weekly_advice': {
            'week_1': "Étudie un sujet avec rigueur et méthode.",
            'week_2': "Applique pratiquement ce que tu apprends.",
            'week_3': "Laisse place à ce qui ne s'explique pas rationnellement.",
            'week_4': "Intègre raison et intuition dans ta sagesse."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Philosophie équilibrée**

Ta Lune en Taureau en Maison 9 veut des croyances stables et claires. Ton Ascendant Balance ajoute de la nuance : tu veux considérer toutes les perspectives, créer une philosophie harmonieuse, voir tous les côtés.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons cherchent l'équilibre. Tu veux une vision du monde juste, des croyances qui honorent toutes les vérités, une sagesse diplomatique.

**Ton approche instinctive** : La Balance te fait peser chaque idée. Tu considères les pour et les contre, tu cherches la synthèse, tu créés des ponts entre philosophies. Cette nuance peut créer de la sagesse ou de l'indécision.

**Tensions possibles** : La difficulté à choisir une position claire par peur d'exclure une vérité. Tu risques de rester dans le relativisme au lieu de t'engager.

**Conseil clé** : Considérer toutes les perspectives tout en choisissant ta vérité.""",
        'weekly_advice': {
            'week_1': "Explore des perspectives opposées sur un sujet.",
            'week_2': "Trouve ce qui est vrai dans chaque position.",
            'week_3': "Choisis ta vérité en connaissance de cause.",
            'week_4': "Engage-toi dans cette vérité tout en restant ouvert."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité profonde**

Ta Lune en Taureau en Maison 9 veut des croyances simples et rassurantes. Ton Ascendant Scorpion ajoute de l'intensité : tu veux la vérité absolue, explorer les mystères, plonger dans les profondeurs philosophiques.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons deviennent obsessionnels. Tu veux comprendre l'essence des choses, percer les secrets, accéder aux vérités cachées.

**Ton approche instinctive** : Le Scorpion te fait plonger dans les profondeurs philosophiques. Tu explores l'ésotérisme, la psychologie profonde, les tabous. Cette intensité peut révéler ou consumer.

**Tensions possibles** : L'obsession pour certaines vérités qui t'enferme dans une vision sombre. Tu risques de voir les profondeurs sans reconnaître la beauté en surface.

**Conseil clé** : Plonger dans les mystères tout en gardant un équilibre.""",
        'weekly_advice': {
            'week_1': "Explore un enseignement profond ou ésotérique.",
            'week_2': "Plonge intensément dans cette compréhension.",
            'week_3': "Remonte à la surface avec ce que tu as trouvé.",
            'week_4': "Intègre cette vérité profonde dans ta vie simple."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Sagesse expansive**

Ta Lune en Taureau en Maison 9 veut ancrer ses connaissances durablement. Ton Ascendant Sagittaire amplifie la Maison 9 : tu veux tout explorer, comprendre le monde entier, voyager constamment, apprendre sans fin.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons sont illimités. Tu veux tout voir, tout comprendre, tout expérimenter. Le monde entier est ton école.

**Ton approche instinctive** : Le Sagittaire te fait voyager physiquement et mentalement. Tu explores des cultures, des philosophies, des visions du monde. Cette expansion peut t'enrichir ou te disperser.

**Tensions possibles** : La difficulté à t'ancrer dans une sagesse stable par soif constante de nouveauté. Tu risques de voyager sans intégrer vraiment ce que tu apprends.

**Conseil clé** : Explorer largement tout en intégrant profondément.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans une grande exploration intellectuelle.",
            'week_2': "Accumule des expériences et connaissances diverses.",
            'week_3': "Ralentis pour intégrer ce que tu as découvert.",
            'week_4': "Ancre les enseignements qui transforment vraiment ta vision."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Sagesse structurée**

Ta Lune en Taureau en Maison 9 veut des croyances solides et concrètes. Ton Ascendant Capricorne ajoute de l'ambition : tu veux maîtriser ton domaine, construire une expertise reconnue, obtenir des diplômes qui prouvent ta sagesse.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons sont orientés vers l'accomplissement. Tu veux une sagesse qui te fait progresser socialement, des connaissances qui construisent ton autorité.

**Ton approche instinctive** : Le Capricorne te fait structurer ton apprentissage. Tu planifies ton éducation, tu vises l'expertise, tu construis méthodiquement ta compréhension. Cette discipline peut créer de la maîtrise ou de la rigidité.

**Tensions possibles** : L'apprentissage motivé par le statut plutôt que par la vraie curiosité. Tu risques d'accumuler des diplômes sans sagesse véritable.

**Conseil clé** : Construire une expertise solide tout en gardant l'émerveillement de l'apprentissage.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine d'expertise à construire sérieusement.",
            'week_2': "Planifie ton parcours d'apprentissage avec méthode.",
            'week_3': "Étudie avec rigueur tout en gardant ta curiosité.",
            'week_4': "Célèbre ta progression et ta compréhension croissante."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Sagesse alternative**

Ta Lune en Taureau en Maison 9 veut des vérités traditionnelles et éprouvées. Ton Ascendant Verseau ajoute de l'innovation : tu explores des philosophies alternatives, des enseignements non-conventionnels, des vérités avant-gardistes.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons oscillent entre tradition et révolution. Tu veux une sagesse solide mais originale, des croyances qui te distinguent.

**Ton approche instinctive** : Le Verseau te fait expérimenter des voies d'apprentissage atypiques. Tu explores des enseignements marginaux, tu créés ta propre philosophie. Cette originalité peut libérer ou marginaliser.

**Tensions possibles** : Le rejet des sagesses traditionnelles par besoin de différence. Tu risques d'être original sans être profond.

**Conseil clé** : Innover dans ta compréhension tout en respectant les sagesses éprouvées.""",
        'weekly_advice': {
            'week_1': "Explore un enseignement non-conventionnel qui t'attire.",
            'week_2': "Teste cette approche alternative avec ouverture.",
            'week_3': "Compare avec les sagesses traditionnelles sur le même sujet.",
            'week_4': "Intègre le meilleur des deux dans ta compréhension unique."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 9, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sagesse mystique**

Ta Lune en Taureau en Maison 9 veut des vérités concrètes et terre-à-terre. Ton Ascendant Poissons ajoute de la spiritualité : tu veux une sagesse qui transcende le rationnel, une compréhension intuitive, une vérité mystique.

**Domaine activé** : Maison 9 — Ta quête de sens, ton apprentissage, tes horizons deviennent spirituels. Tu veux comprendre l'invisible, recevoir des enseignements par l'intuition, fusionner avec la sagesse universelle.

**Ton approche instinctive** : Le Poissons te fait recevoir la sagesse plus que l'apprendre. Tu médites, tu rêves, tu canalises. Cette réceptivité peut ouvrir à de grandes vérités ou créer de la confusion.

**Tensions possibles** : La difficulté à ancrer ta sagesse mystique dans le réel. Tu risques de rêver des vérités sans les vivre concrètement.

**Conseil clé** : Recevoir la sagesse intuitive tout en l'ancrant dans ta vie pratique.""",
        'weekly_advice': {
            'week_1': "Médite pour recevoir des enseignements intuitifs.",
            'week_2': "Accueille ce qui émerge sans le juger.",
            'week_3': "Teste cette sagesse dans ta vie concrète.",
            'week_4': "Intègre ce qui améliore vraiment ton existence."
        }
    },

    # ==================== MAISON 10 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Carrière conquérante**

Ta Lune en Taureau en Maison 10 veut construire une carrière stable et respectée. Ton Ascendant Bélier ajoute de l'audace : tu veux réussir vite, conquérir ton domaine, prouver ta valeur immédiatement.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation sont au cœur de ce mois. Tu veux grimper solidement tout en avançant rapidement. L'ambition rencontre la patience.

**Ton approche instinctive** : Le Bélier te fait foncer sur tes objectifs professionnels. Tu prends des initiatives audacieuses, tu cherches la reconnaissance rapide. Cette urgence peut bousculer ton besoin de sécurité.

**Tensions possibles** : L'impatience du Bélier versus la lenteur du Taureau. Tu risques de forcer les étapes puis de te freiner par peur de perdre ce que tu as construit.

**Conseil clé** : Oser des initiatives professionnelles tout en construisant des fondations durables.""",
        'weekly_advice': {
            'week_1': "Lance un projet ambitieux dans ta carrière.",
            'week_2': "Avance avec détermination sur cet objectif.",
            'week_3': "Consolide ce que tu as initié avec patience.",
            'week_4': "Célèbre tes progrès concrets et visibles."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Carrière ancrée**

Triple Taureau sur ta carrière : Lune, Maison 10 et Ascendant. C'est un mois où ta réussite professionnelle se construit pierre par pierre, avec persévérance et authenticité. La patience est ta plus grande alliée.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation se développent naturellement. Tu veux un succès solide, durable, qui te ressemble vraiment et te procure une sécurité matérielle concrète.

**Ton approche instinctive** : Double Taureau te fait avancer méthodiquement vers tes objectifs. Tu ne cherches pas la gloire rapide mais la reconnaissance qui dure. Cette constance peut créer de grandes réussites ou de la lenteur excessive.

**Tensions possibles** : La résistance au changement professionnel par peur de perdre ta sécurité. Tu risques de rester dans une situation confortable mais limitante.

**Conseil clé** : Construire ta carrière avec patience tout en restant ouvert aux opportunités d'évolution.""",
        'weekly_advice': {
            'week_1': "Identifie une étape concrète vers ta réussite à long terme.",
            'week_2': "Travaille avec rigueur sur cet objectif professionnel.",
            'week_3': "Apprécie les progrès même s'ils semblent lents.",
            'week_4': "Ancre ta progression dans des résultats tangibles."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Carrière polyvalente**

Ta Lune en Taureau en Maison 10 veut une carrière stable et prévisible. Ton Ascendant Gémeaux ajoute de la diversité : tu explores plusieurs pistes professionnelles, tu communiques pour te faire connaître, tu diversifies tes activités.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation oscillent entre spécialisation et polyvalence. Tu veux une base solide tout en gardant plusieurs options ouvertes.

**Ton approche instinctive** : Le Gémeaux te fait communiquer sur ton expertise, réseauter pour avancer, explorer différentes directions. Cette mobilité peut enrichir ou disperser ton énergie professionnelle.

**Tensions possibles** : La difficulté à t'engager dans une voie unique par peur de manquer d'autres opportunités. Tu risques de papillonner professionnellement sans construire d'expertise solide.

**Conseil clé** : Développer plusieurs compétences tout en construisant une identité professionnelle cohérente.""",
        'weekly_advice': {
            'week_1': "Identifie 2-3 domaines professionnels qui t'attirent vraiment.",
            'week_2': "Explore comment les connecter de façon cohérente.",
            'week_3': "Communique sur cette polyvalence comme une force.",
            'week_4': "Ancre ta réputation dans cette diversité maîtrisée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Carrière bienveillante**

Ta Lune en Taureau en Maison 10 veut une carrière concrète et productive. Ton Ascendant Cancer ajoute de l'empathie : tu veux réussir en prenant soin, en nourrissant, en créant un environnement professionnel chaleureux.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation se construisent autour de l'humain. Tu veux un succès qui protège, nourrit et soutient les autres tout en te sécurisant matériellement.

**Ton approche instinctive** : Le Cancer te fait aborder ta carrière avec sensibilité. Tu crées des liens émotionnels au travail, tu veilles sur ton équipe. Cette approche maternante peut inspirer ou créer de la dépendance.

**Tensions possibles** : La difficulté à imposer ton autorité professionnelle par excès de gentillesse. Tu risques de trop donner au détriment de ta propre sécurité.

**Conseil clé** : Construire une carrière solide en prenant soin des autres sans te sacrifier.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton travail peut nourrir les autres.",
            'week_2': "Développe cette dimension tout en protégeant tes besoins.",
            'week_3': "Pose des limites claires dans ta générosité professionnelle.",
            'week_4': "Célèbre l'équilibre entre donner et recevoir."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Carrière rayonnante**

Ta Lune en Taureau en Maison 10 veut construire une carrière solide et reconnue. Ton Ascendant Lion ajoute de l'éclat : tu veux briller professionnellement, être admiré pour ton expertise, incarner l'excellence dans ton domaine.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation deviennent visibles. Tu veux réussir avec panache, être reconnu non seulement pour ta compétence mais aussi pour ton charisme professionnel.

**Ton approche instinctive** : Le Lion te fait viser les sommets avec confiance. Tu te positionnes comme une référence, tu cherches les projecteurs professionnels. Cette ambition peut t'élever ou créer de l'arrogance.

**Tensions possibles** : La quête de reconnaissance qui prend le pas sur le travail solide. Tu risques de privilégier l'apparence du succès plutôt que sa substance.

**Conseil clé** : Rayonner professionnellement tout en construisant une expertise réellement solide.""",
        'weekly_advice': {
            'week_1': "Identifie où tu veux briller dans ta carrière.",
            'week_2': "Développe l'excellence concrète dans ce domaine.",
            'week_3': "Communique sur ton expertise avec fierté et humilité.",
            'week_4': "Savoure la reconnaissance méritée de ton travail."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Carrière perfectionnée**

Ta Lune en Taureau en Maison 10 veut une carrière stable et productive. Ton Ascendant Vierge ajoute du perfectionnisme : tu veux exceller dans les détails, être irréprochable dans ton travail, améliorer constamment tes processus professionnels.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation se construisent sur la qualité. Tu veux être reconnu pour ton sérieux, ta fiabilité, ton attention méticuleuse à bien faire les choses.

**Ton approche instinctive** : La Vierge te fait analyser chaque aspect de ton travail. Tu optimises, tu corriges, tu perfectionnes. Cette rigueur peut créer l'excellence ou la paralysie par sur-analyse.

**Tensions possibles** : Le perfectionnisme qui retarde tes progrès professionnels. Tu risques de ne jamais te sentir prêt à avancer par peur de l'imperfection.

**Conseil clé** : Viser l'excellence sans tomber dans la perfection paralysante.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine professionnel à améliorer.",
            'week_2': "Travaille méthodiquement sur cette optimisation.",
            'week_3': "Accepte que 'assez bon' soit suffisant parfois.",
            'week_4': "Célèbre la qualité de ton travail sans te critiquer."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Carrière harmonieuse**

Ta Lune en Taureau en Maison 10 veut une carrière concrète et sécurisante. Ton Ascendant Balance ajoute de la diplomatie : tu veux réussir en créant des partenariats professionnels équilibrés, en maintenant l'harmonie dans ton environnement de travail.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation se développent à travers les relations. Tu veux un succès qui crée de la beauté, de l'équilibre, de la collaboration fructueuse.

**Ton approche instinctive** : La Balance te fait chercher le consensus professionnel. Tu négocies, tu collabores, tu crées des ponts. Cette diplomatie peut faciliter ton ascension ou te faire perdre ta direction par excès de compromis.

**Tensions possibles** : La difficulté à prendre des décisions professionnelles fermes par peur de déplaire. Tu risques de sacrifier tes objectifs pour maintenir la paix.

**Conseil clé** : Construire ta carrière sur des partenariats équilibrés sans perdre ton cap.""",
        'weekly_advice': {
            'week_1': "Identifie les collaborations professionnelles qui te nourrissent.",
            'week_2': "Développe ces partenariats avec équité et clarté.",
            'week_3': "Pose tes limites dans ces relations de travail.",
            'week_4': "Célèbre les succès partagés avec tes alliés professionnels."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Carrière transformée**

Ta Lune en Taureau en Maison 10 veut une carrière stable et prévisible. Ton Ascendant Scorpion ajoute de l'intensité : tu veux transformer ton domaine, exercer un pouvoir professionnel réel, aller au fond des choses dans ta carrière.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation passent par des mutations profondes. Tu veux un succès qui te transforme et transforme ton environnement professionnel, pas juste une progression linéaire.

**Ton approche instinctive** : Le Scorpion te fait investiguer les profondeurs de ton métier. Tu détectes les enjeux de pouvoir, tu ne te contentes pas de la surface. Cette perspicacité peut t'élever ou créer des conflits.

**Tensions possibles** : L'obsession du contrôle professionnel qui crée de la méfiance. Tu risques de voir des complots partout et de t'isoler dans ta carrière.

**Conseil clé** : Exercer ton pouvoir professionnel avec profondeur tout en gardant la confiance.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect profond de ta carrière à transformer.",
            'week_2': "Plonge intensément dans cette transformation.",
            'week_3': "Gère le pouvoir que tu acquiers avec responsabilité.",
            'week_4': "Intègre cette mutation professionnelle durablement."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Carrière expansive**

Ta Lune en Taureau en Maison 10 veut une carrière ancrée localement et concrète. Ton Ascendant Sagittaire ajoute de l'expansion : tu veux une carrière internationale, une influence large, une vision professionnelle qui transcende les frontières.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation oscillent entre ancrage local et rayonnement mondial. Tu veux construire solidement tout en visant l'infini.

**Ton approche instinctive** : Le Sagittaire te fait voir grand professionnellement. Tu explores de nouveaux territoires, tu enseignes, tu partages ta vision. Cette expansion peut t'enrichir ou te disperser.

**Tensions possibles** : La difficulté à t'ancrer dans une carrière stable par soif constante de nouveaux horizons. Tu risques de changer de direction sans construire d'expertise durable.

**Conseil clé** : Viser large professionnellement tout en construisant des fondations solides.""",
        'weekly_advice': {
            'week_1': "Identifie comment élargir ton influence professionnelle.",
            'week_2': "Explore de nouveaux territoires dans ton domaine.",
            'week_3': "Ancre ce qui fonctionne vraiment pour toi.",
            'week_4': "Construis une expertise qui rayonne au-delà de ton environnement immédiat."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Carrière maîtrisée**

Ta Lune en Taureau en Maison 10 veut une carrière solide et confortable. Ton Ascendant Capricorne amplifie la Maison 10 : tu veux atteindre le sommet, construire une autorité incontestable, réussir socialement de façon durable.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation sont au maximum de leur puissance. Tu veux grimper l'échelle sociale avec détermination, établir ton autorité, laisser un héritage professionnel.

**Ton approche instinctive** : Le Capricorne te fait structurer ta progression professionnelle. Tu planifies ta carrière à long terme, tu acceptes les sacrifices nécessaires. Cette ambition peut créer le succès ou la rigidité.

**Tensions possibles** : L'obsession du statut qui te fait sacrifier ton bien-être. Tu risques de grimper sans savourer le chemin ni profiter de ce que tu construis.

**Conseil clé** : Construire une carrière ambitieuse tout en préservant ton équilibre de vie.""",
        'weekly_advice': {
            'week_1': "Définis clairement tes objectifs professionnels à long terme.",
            'week_2': "Travaille avec discipline sur ton avancement.",
            'week_3': "Prends du temps pour savourer tes accomplissements.",
            'week_4': "Équilibre ambition et qualité de vie."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Carrière innovante**

Ta Lune en Taureau en Maison 10 veut une carrière traditionnelle et sécurisante. Ton Ascendant Verseau ajoute de l'innovation : tu veux révolutionner ton domaine, apporter des idées avant-gardistes, te démarquer par ton originalité professionnelle.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation oscillent entre conformité et rébellion. Tu veux un succès stable mais original, une reconnaissance pour ton unicité tout en gardant ta sécurité.

**Ton approche instinctive** : Le Verseau te fait expérimenter professionnellement. Tu explores des voies non-conventionnelles, tu innoves, tu refuses les chemins tout tracés. Cette originalité peut te distinguer ou te marginaliser.

**Tensions possibles** : Le besoin de sécurité versus le désir de révolutionner. Tu risques d'être paralysé entre conformité rassurante et innovation risquée.

**Conseil clé** : Innover dans ta carrière tout en construisant une base économique solide.""",
        'weekly_advice': {
            'week_1': "Identifie une innovation possible dans ton domaine.",
            'week_2': "Expérimente cette approche originale avec prudence.",
            'week_3': "Mesure les résultats concrets de ton innovation.",
            'week_4': "Ancre ce qui fonctionne dans ta pratique professionnelle."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 10, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Carrière inspirée**

Ta Lune en Taureau en Maison 10 veut une carrière concrète et matériellement productive. Ton Ascendant Poissons ajoute de la transcendance : tu veux une carrière qui a du sens spirituellement, qui contribue à quelque chose de plus grand.

**Domaine activé** : Maison 10 — Ta carrière, ton statut, ta réputation se construisent entre matériel et spirituel. Tu veux réussir dans le monde concret tout en servant une mission plus élevée.

**Ton approche instinctive** : Le Poissons te fait aborder ta carrière avec intuition et compassion. Tu te laisses guider par des inspirations, tu choisis des voies qui nourrissent ton âme. Cette réceptivité peut ouvrir des portes inattendues ou créer de la confusion.

**Tensions possibles** : La difficulté à concilier besoins matériels et aspirations spirituelles. Tu risques de sacrifier ta sécurité financière pour une mission ou de te sentir coupable de chercher le succès matériel.

**Conseil clé** : Construire une carrière matériellement solide qui nourrit aussi ton âme.""",
        'weekly_advice': {
            'week_1': "Identifie le sens profond que tu veux donner à ton travail.",
            'week_2': "Explore comment incarner cette mission concrètement.",
            'week_3': "Ancre ta carrière dans des résultats tangibles.",
            'week_4': "Célèbre l'harmonie entre réussite matérielle et sens spirituel."
        }
    },

    # ==================== MAISON 11 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Amitiés conquérantes**

Ta Lune en Taureau en Maison 11 veut des amitiés stables et durables. Ton Ascendant Bélier ajoute du dynamisme : tu veux créer de nouveaux liens rapidement, te lancer dans des projets collectifs audacieux, conquérir de nouveaux cercles sociaux.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux sont en mouvement. Tu veux des relations solides mais tu n'as pas envie d'attendre pour les créer.

**Ton approche instinctive** : Le Bélier te fait initier des connexions sociales avec énergie. Tu proposes des projets, tu rassembles les gens, tu fonces dans l'action collective. Cette impulsivité peut créer des liens ou des malentendus.

**Tensions possibles** : L'impatience relationnelle qui te fait forcer les amitiés. Tu risques de te rapprocher trop vite puis de te sentir déçu si la profondeur n'est pas au rendez-vous.

**Conseil clé** : Créer de nouveaux liens tout en laissant le temps à la confiance de s'installer.""",
        'weekly_advice': {
            'week_1': "Lance une initiative qui rassemble tes proches.",
            'week_2': "Fonce dans l'action collective avec enthousiasme.",
            'week_3': "Laisse les relations s'approfondir naturellement.",
            'week_4': "Ancre les amitiés qui résonnent vraiment."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Amitiés ancrées**

Triple Taureau sur tes amitiés : Lune, Maison 11 et Ascendant. C'est un mois où tes relations amicales sont solides comme le roc. Tu cherches la loyauté durable, les projets collectifs concrets, les groupes qui partagent tes valeurs fondamentales.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux sont ancrés dans le concret. Tu veux des relations authentiques, confortables, qui durent dans le temps sans drame ni instabilité.

**Ton approche instinctive** : Double Taureau te fait cultiver tes amitiés lentement mais profondément. Tu es fidèle, présent, fiable. Cette stabilité crée de la sécurité mais peut limiter l'ouverture à de nouvelles personnes.

**Tensions possibles** : La résistance à élargir ton cercle par attachement excessif à tes habitudes sociales. Tu risques de rester dans ta zone de confort relationnelle même si elle se rétrécit.

**Conseil clé** : Cultiver tes amitiés solides tout en restant ouvert à de nouvelles connexions.""",
        'weekly_advice': {
            'week_1': "Célèbre les amitiés durables qui enrichissent ta vie.",
            'week_2': "Partage des moments simples et authentiques avec eux.",
            'week_3': "Reste ouvert à une nouvelle rencontre amicale.",
            'week_4': "Ancre ta gratitude pour ton réseau loyal."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Amitiés curieuses**

Ta Lune en Taureau en Maison 11 veut des amitiés stables et peu nombreuses. Ton Ascendant Gémeaux ajoute de la diversité : tu veux multiplier les connexions, explorer différents cercles sociaux, communiquer avec tout le monde.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux oscillent entre profondeur et variété. Tu veux des relations solides mais tu es attiré par la diversité sociale.

**Ton approche instinctive** : Le Gémeaux te fait papillonner socialement. Tu communiques avec de nombreuses personnes, tu explores différents groupes. Cette versatilité peut enrichir ton réseau ou disperser ton énergie relationnelle.

**Tensions possibles** : La difficulté à approfondir les amitiés par besoin constant de nouveauté. Tu risques d'avoir beaucoup de connaissances mais peu d'amis vraiment proches.

**Conseil clé** : Diversifier tes connexions tout en cultivant quelques amitiés en profondeur.""",
        'weekly_advice': {
            'week_1': "Explore un nouveau cercle social qui t'intrigue.",
            'week_2': "Communique ouvertement avec de nouvelles personnes.",
            'week_3': "Identifie qui mérite un investissement plus profond.",
            'week_4': "Ancre quelques relations nouvelles dans la durée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Amitiés nourricières**

Ta Lune en Taureau en Maison 11 veut des amitiés confortables et loyales. Ton Ascendant Cancer ajoute de la tendresse : tu veux des amis qui sont comme une famille, des relations qui te nourrissent émotionnellement, un groupe où tu te sens protégé.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux sont teintés d'affection. Tu cherches des liens qui prennent soin de toi et réciproquement, un cercle chaleureux et sécurisant.

**Ton approche instinctive** : Le Cancer te fait créer une famille de cœur avec tes amis. Tu nourris tes proches, tu crées du cocon collectif. Cette tendresse peut approfondir les liens ou créer de la dépendance émotionnelle.

**Tensions possibles** : Le besoin excessif de réassurance dans tes amitiés. Tu risques de te sentir blessé facilement si tes amis ne te donnent pas l'attention que tu attends.

**Conseil clé** : Créer des amitiés nourrissantes sans tomber dans la dépendance affective.""",
        'weekly_advice': {
            'week_1': "Identifie les amis qui te nourrissent vraiment.",
            'week_2': "Offre-leur ta présence et ton attention chaleureuse.",
            'week_3': "Respecte aussi ton besoin de solitude ressourçante.",
            'week_4': "Célèbre l'équilibre entre donner et recevoir."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Amitiés rayonnantes**

Ta Lune en Taureau en Maison 11 veut des amitiés simples et authentiques. Ton Ascendant Lion ajoute de l'éclat : tu veux être admiré par tes amis, créer des projets collectifs ambitieux, rayonner dans ton cercle social.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux prennent de l'ampleur. Tu veux des relations qui te valorisent, des groupes où tu peux briller, des causes nobles qui te grandissent.

**Ton approche instinctive** : Le Lion te fait prendre ta place dans tes amitiés. Tu organises, tu diriges, tu inspires ton cercle. Cette générosité peut rassembler ou créer des jalousies si tu éclipses les autres.

**Tensions possibles** : Le besoin d'être au centre de l'attention dans tes amitiés. Tu risques de dominer les échanges ou de te sentir blessé si tu n'es pas reconnu.

**Conseil clé** : Rayonner dans tes amitiés tout en laissant de la place aux autres.""",
        'weekly_advice': {
            'week_1': "Organise un événement qui rassemble tes amis.",
            'week_2': "Partage généreusement ton énergie et tes idées.",
            'week_3': "Écoute aussi les besoins et aspirations des autres.",
            'week_4': "Célèbre les succès collectifs, pas seulement les tiens."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Amitiés utiles**

Ta Lune en Taureau en Maison 11 veut des amitiés confortables et agréables. Ton Ascendant Vierge ajoute du pragmatisme : tu veux des relations qui t'aident concrètement, des projets collectifs efficaces, des groupes organisés et productifs.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux sont orientés vers l'utilité. Tu veux des connexions qui améliorent ta vie, des collaborations qui produisent des résultats tangibles.

**Ton approche instinctive** : La Vierge te fait analyser tes relations. Tu évalues qui t'apporte quoi, tu améliores le fonctionnement de tes groupes. Cette efficacité peut optimiser ou assécher l'aspect spontané des amitiés.

**Tensions possibles** : Le jugement excessif qui te fait rejeter des amitiés imparfaites. Tu risques de critiquer tes amis ou de t'isoler par standards trop élevés.

**Conseil clé** : Cultiver des amitiés utiles sans perdre la chaleur de la connexion humaine.""",
        'weekly_advice': {
            'week_1': "Identifie les amitiés qui t'enrichissent concrètement.",
            'week_2': "Contribue aussi de façon pratique à ces relations.",
            'week_3': "Accepte les imperfections humaines avec bienveillance.",
            'week_4': "Célèbre la qualité de tes amitiés authentiques."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Amitiés harmonieuses**

Ta Lune en Taureau en Maison 11 veut des amitiés loyales et stables. Ton Ascendant Balance ajoute de la diplomatie : tu veux créer de l'harmonie dans tes groupes, équilibrer les besoins de chacun, être le médiateur qui maintient la paix sociale.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux cherchent l'équilibre. Tu veux des relations justes, belles, où chacun se sent valorisé et entendu.

**Ton approche instinctive** : La Balance te fait harmoniser tes relations. Tu créés des ponts entre les gens, tu évites les conflits, tu cherches le consensus. Cette douceur peut créer de la cohésion ou de l'évitement des vraies tensions.

**Tensions possibles** : L'excès de compromis qui dilue tes besoins personnels. Tu risques de maintenir des amitiés déséquilibrées pour éviter les ruptures.

**Conseil clé** : Créer de l'harmonie dans tes amitiés sans sacrifier ton authenticité.""",
        'weekly_advice': {
            'week_1': "Identifie les déséquilibres dans tes amitiés.",
            'week_2': "Communique tes besoins avec diplomatie et clarté.",
            'week_3': "Trouve des solutions équitables pour tous.",
            'week_4': "Célèbre l'harmonie restaurée dans tes relations."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Amitiés intenses**

Ta Lune en Taureau en Maison 11 veut des amitiés tranquilles et confortables. Ton Ascendant Scorpion ajoute de la profondeur : tu veux des connexions intimes, des amitiés qui voient ton ombre, des projets collectifs transformateurs.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux oscillent entre simplicité et intensité. Tu veux des relations authentiques qui vont au fond des choses, pas des amitiés superficielles.

**Ton approche instinctive** : Le Scorpion te fait investiguer tes relations. Tu testes la loyauté, tu cherches la vérité, tu ne supportes pas le faux-semblant. Cette profondeur peut créer des liens puissants ou effrayer ceux qui préfèrent la légèreté.

**Tensions possibles** : La méfiance excessive qui te fait repousser de potentielles amitiés. Tu risques de voir de la trahison partout et de t'isoler par protection.

**Conseil clé** : Cultiver la profondeur dans tes amitiés tout en gardant la confiance.""",
        'weekly_advice': {
            'week_1': "Identifie les amis avec qui tu peux être vraiment toi-même.",
            'week_2': "Ose partager ta vulnérabilité avec eux.",
            'week_3': "Accueille aussi leur authenticité sans jugement.",
            'week_4': "Célèbre la force de ces liens profonds."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Amitiés expansives**

Ta Lune en Taureau en Maison 11 veut un cercle social stable et local. Ton Ascendant Sagittaire ajoute de l'ouverture : tu veux des amis du monde entier, des projets collectifs qui élargissent tes horizons, une communauté internationale.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux deviennent globaux. Tu veux explorer différentes cultures à travers tes relations, apprendre de la diversité, connecter avec des gens qui élargissent ta vision.

**Ton approche instinctive** : Le Sagittaire te fait chercher l'aventure dans tes amitiés. Tu explores de nouveaux groupes, tu voyages pour voir tes amis, tu partages des idéaux universels. Cette ouverture peut enrichir ou disperser.

**Tensions possibles** : La difficulté à approfondir les amitiés locales par soif constante de nouveauté. Tu risques d'avoir des amis partout mais nulle part vraiment.

**Conseil clé** : Explorer de nouveaux cercles tout en ancrant quelques amitiés profondes.""",
        'weekly_advice': {
            'week_1': "Connecte avec quelqu'un d'une culture différente.",
            'week_2': "Explore ce que cette diversité t'apprend.",
            'week_3': "Ancre aussi tes amitiés locales et durables.",
            'week_4': "Célèbre la richesse de ton réseau diversifié."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Amitiés stratégiques**

Ta Lune en Taureau en Maison 11 veut des amitiés simples et authentiques. Ton Ascendant Capricorne ajoute de l'ambition : tu veux des connexions qui t'aident professionnellement, un réseau qui soutient tes objectifs, des amitiés mutuellement bénéfiques.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux sont orientés vers l'accomplissement. Tu veux des relations qui construisent quelque chose de durable, des alliances qui font progresser tout le monde.

**Ton approche instinctive** : Le Capricorne te fait structurer ton réseau social. Tu cultives des relations utiles, tu investis dans des connexions stratégiques. Cette approche peut créer des opportunités ou assécher la spontanéité amicale.

**Tensions possibles** : L'utilitarisme relationnel qui transforme tes amitiés en transactions. Tu risques de perdre la chaleur humaine au profit du networking.

**Conseil clé** : Cultiver un réseau utile sans perdre l'authenticité des vraies amitiés.""",
        'weekly_advice': {
            'week_1': "Identifie les connexions qui soutiennent tes objectifs.",
            'week_2': "Développe ces relations avec générosité et intégrité.",
            'week_3': "Préserve aussi des amitiés purement affectives.",
            'week_4': "Célèbre l'équilibre entre réseau et vraies amitiés."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Amitiés fraternelles**

Ta Lune en Taureau en Maison 11 veut des amitiés traditionnelles et confortables. Ton Ascendant Verseau amplifie la Maison 11 : tu veux créer des communautés innovantes, défendre des causes collectives, connecter avec des esprits libres qui partagent tes idéaux.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux sont au maximum de leur puissance. Tu veux changer le monde avec tes amis, créer des mouvements, appartenir à des groupes qui font la différence.

**Ton approche instinctive** : Le Verseau te fait rechercher la fraternité universelle. Tu veux des relations égalitaires, libres, sans possessivité. Cette indépendance peut libérer ou créer de la distance émotionnelle.

**Tensions possibles** : La difficulté à créer de l'intimité par peur de perdre ta liberté. Tu risques d'avoir beaucoup d'amis mais de te sentir seul dans ta différence.

**Conseil clé** : Cultiver l'idéal fraternel tout en créant quelques liens vraiment intimes.""",
        'weekly_advice': {
            'week_1': "Engage-toi dans une cause collective qui te passionne.",
            'week_2': "Connecte avec ceux qui partagent cet idéal.",
            'week_3': "Approfondis quelques relations au-delà de la cause commune.",
            'week_4': "Célèbre l'équilibre entre fraternité et intimité."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 11, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Amitiés compassionnelles**

Ta Lune en Taureau en Maison 11 veut des amitiés concrètes et loyales. Ton Ascendant Poissons ajoute de la compassion : tu veux des connexions spirituelles, des amitiés qui transcendent l'ego, des projets collectifs qui servent l'humanité.

**Domaine activé** : Maison 11 — Tes amitiés, tes projets collectifs, tes idéaux deviennent universels. Tu veux fusionner avec tes amis, sentir l'unité, servir quelque chose de plus grand que vos intérêts individuels.

**Ton approche instinctive** : Le Poissons te fait aborder les amitiés avec empathie et intuition. Tu ressens profondément les autres, tu te dévoues pour tes amis. Cette compassion peut créer de la beauté ou de la perte de limites.

**Tensions possibles** : L'absence de frontières qui te fait absorber les problèmes de tes amis. Tu risques de te perdre dans les autres ou d'attirer ceux qui profitent de ta générosité.

**Conseil clé** : Cultiver la compassion dans tes amitiés tout en préservant tes limites.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu peux servir tes amis avec ton cœur.",
            'week_2': "Offre ton soutien avec présence et empathie.",
            'week_3': "Protège aussi ton énergie et ton bien-être.",
            'week_4': "Célèbre l'équilibre entre donner et te ressourcer."
        }
    },

    # ==================== MAISON 12 ====================

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Ressourcement actif**

Ta Lune en Taureau en Maison 12 veut te retirer dans le confort et la contemplation. Ton Ascendant Bélier ajoute de l'urgence : tu veux agir sur ton inconscient, conquérir tes peurs rapidement, transformer ton monde intérieur sans attendre.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude sont en tension avec ton désir d'action. Tu oscilles entre retraite nécessaire et impatience de revenir dans le monde.

**Ton approche instinctive** : Le Bélier te fait vouloir résoudre rapidement tes enjeux intérieurs. Tu veux méditer efficacement, guérir vite, comprendre ton ombre immédiatement. Cette urgence peut bousculer ton processus.

**Tensions possibles** : L'impatience face au temps nécessaire à l'introspection. Tu risques de forcer ton monde intérieur au lieu de le laisser se révéler doucement.

**Conseil clé** : Agir sur ton monde intérieur tout en respectant son rythme naturel.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans une pratique spirituelle ou thérapeutique.",
            'week_2': "Plonge activement dans ton monde intérieur.",
            'week_3': "Accepte que certaines choses prennent du temps.",
            'week_4': "Intègre ce qui a émergé avec patience."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Retraite sensorielle**

Triple Taureau sur ton monde intérieur : Lune, Maison 12 et Ascendant. C'est un mois de profonde connexion à ton inconscient à travers le corps et les sens. Tu as besoin de solitude confortable, de ressourcement tangible, de spiritualité incarnée.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude s'expriment à travers le concret. Tu médites en marchant dans la nature, tu guéris par le toucher, tu te reconnectes par les plaisirs simples.

**Ton approche instinctive** : Double Taureau te fait chercher la transcendance dans l'immanence. Tu trouves le sacré dans la matière, la paix dans le confort physique. Cette approche peut être profondément ressourçante ou éviter les vraies profondeurs émotionnelles.

**Tensions possibles** : La confusion entre confort et fuite. Tu risques d'utiliser les plaisirs physiques pour éviter d'affronter ton ombre plutôt que pour vraiment guérir.

**Conseil clé** : Te ressourcer dans le confort tout en accueillant ce qui émerge de ton inconscient.""",
        'weekly_advice': {
            'week_1': "Crée un espace de retraite confortable et sensoriel.",
            'week_2': "Ressource-toi par le corps et les plaisirs simples.",
            'week_3': "Accueille aussi ce qui remonte de ton inconscient.",
            'week_4': "Intègre cette sagesse intérieure dans ta vie."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Introspection mentale**

Ta Lune en Taureau en Maison 12 veut une retraite silencieuse et contemplative. Ton Ascendant Gémeaux ajoute du mental : tu veux comprendre intellectuellement ton inconscient, lire sur la psychologie, communiquer sur tes découvertes intérieures.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude oscillent entre silence et réflexion. Tu explores ton monde intérieur par l'écriture, la lecture, l'analyse de tes rêves.

**Ton approche instinctive** : Le Gémeaux te fait intellectualiser ton inconscient. Tu analyses tes émotions, tu cherches à comprendre tes patterns. Cette approche mentale peut éclairer ou éviter le ressenti profond.

**Tensions possibles** : La tendance à parler de ton intériorité plutôt qu'à la vivre. Tu risques de conceptualiser ton ombre sans vraiment la transformer.

**Conseil clé** : Explorer ton monde intérieur intellectuellement tout en restant connecté au ressenti.""",
        'weekly_advice': {
            'week_1': "Lis ou étudie un sujet lié à l'inconscient qui t'intrigue.",
            'week_2': "Applique ces concepts à ta propre psyché.",
            'week_3': "Ressens aussi ce qui émerge au-delà des mots.",
            'week_4': "Intègre cette compréhension tête et cœur."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Retraite émotionnelle**

Ta Lune en Taureau en Maison 12 veut se ressourcer dans le confort matériel. Ton Ascendant Cancer ajoute de la sensibilité : tu as besoin de te retirer dans ton cocon émotionnel, de pleurer ce qui doit l'être, de te laisser bercer par tes émotions profondes.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude sont intensément émotionnels. Tu te retires pour guérir tes blessures, pour te reconnecter à ton enfant intérieur, pour pleurer en paix.

**Ton approche instinctive** : Le Cancer te fait chercher la sécurité dans la solitude. Tu crées un nid protecteur où tu peux être vulnérable sans danger. Cette sensibilité peut être curative ou amplifier ta mélancolie.

**Tensions possibles** : Le risque de rumination émotionnelle dans l'isolement. Tu peux te perdre dans ta tristesse au lieu de la traverser pour guérir.

**Conseil clé** : Accueillir tes émotions profondes tout en gardant un ancrage dans le présent.""",
        'weekly_advice': {
            'week_1': "Crée un espace sûr pour accueillir tes émotions.",
            'week_2': "Laisse remonter ce qui doit être ressenti et libéré.",
            'week_3': "Prends soin de toi avec douceur et tendresse.",
            'week_4': "Reviens dans le monde avec ton cœur guéri."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Ombre lumineuse**

Ta Lune en Taureau en Maison 12 veut se retirer dans l'ombre et le silence. Ton Ascendant Lion ajoute de la lumière : tu veux transformer ton monde intérieur en force créative, illuminer ton inconscient, faire rayonner ta spiritualité.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude oscillent entre retrait et expression. Tu explores ton ombre pour en faire de l'or, tu transmutes tes blessures en création.

**Ton approche instinctive** : Le Lion te fait vouloir briller même dans ton introspection. Tu cherches la lumière dans l'obscurité, tu veux que ton travail intérieur soit vu. Cette fierté peut motiver ou empêcher la vraie vulnérabilité.

**Tensions possibles** : La difficulté à accepter les parts de toi qui ne sont pas glorieuses. Tu risques de spiritualiser ton ego au lieu de vraiment descendre dans ton ombre.

**Conseil clé** : Explorer ton inconscient avec humilité tout en honorant ta lumière intérieure.""",
        'weekly_advice': {
            'week_1': "Retire-toi pour explorer ce que tu caches habituellement.",
            'week_2': "Accueille tes parts d'ombre avec compassion.",
            'week_3': "Trouve la lumière qui naît de cette acceptation.",
            'week_4': "Reviens dans le monde avec une authenticité renouvelée."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Guérison méthodique**

Ta Lune en Taureau en Maison 12 veut se ressourcer simplement et naturellement. Ton Ascendant Vierge ajoute de la précision : tu veux guérir méthodiquement ton inconscient, purifier tes patterns, perfectionner ta pratique spirituelle.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude deviennent un travail consciencieux. Tu veux optimiser ta santé mentale, créer des rituels qui guérissent vraiment, analyser tes rêves avec rigueur.

**Ton approche instinctive** : La Vierge te fait structurer ton introspection. Tu établis une routine de méditation, tu tiens un journal précis de tes insights, tu cherches à comprendre les détails de ton fonctionnement. Cette discipline peut être curative ou obsessionnelle.

**Tensions possibles** : Le perfectionnisme spirituel qui crée de l'angoisse. Tu risques de juger ton processus intérieur au lieu de l'accueillir avec bienveillance.

**Conseil clé** : Travailler sur ton monde intérieur avec méthode tout en acceptant l'imperfection du processus.""",
        'weekly_advice': {
            'week_1': "Établis une routine quotidienne de pratique intérieure.",
            'week_2': "Observe avec précision ce qui émerge sans juger.",
            'week_3': "Ajuste ta pratique selon ce que tu découvres.",
            'week_4': "Célèbre les progrès subtils de ta guérison."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Solitude harmonieuse**

Ta Lune en Taureau en Maison 12 veut se ressourcer dans le confort et la beauté. Ton Ascendant Balance ajoute de l'esthétique : tu veux une retraite harmonieuse, un espace intérieur équilibré, une spiritualité qui crée de la paix et de la beauté.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude cherchent l'harmonie. Tu te retires pour restaurer ton équilibre intérieur, pour créer de la beauté dans ton âme.

**Ton approche instinctive** : La Balance te fait rechercher l'équilibre dans ton monde intérieur. Tu médites pour trouver la paix, tu guéris les déséquilibres. Cette quête d'harmonie peut apaiser ou éviter les parts plus sombres de ton psyché.

**Tensions possibles** : La tendance à éviter les aspects inconfortables de ton inconscient par besoin de beauté. Tu risques de spiritualiser superficiellement au lieu de plonger vraiment.

**Conseil clé** : Créer de l'harmonie intérieure tout en accueillant ce qui est déséquilibré.""",
        'weekly_advice': {
            'week_1': "Crée un espace de retraite esthétique et apaisant.",
            'week_2': "Médite sur ce qui demande à être équilibré en toi.",
            'week_3': "Accueille aussi le chaos qui fait partie de la vie.",
            'week_4': "Intègre un nouvel équilibre plus authentique."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Plongée profonde**

Ta Lune en Taureau en Maison 12 veut une retraite confortable et apaisante. Ton Ascendant Scorpion ajoute de l'intensité : tu veux plonger dans les profondeurs de ton inconscient, affronter ton ombre la plus noire, mourir et renaître intérieurement.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude deviennent transformateurs. Tu ne cherches pas le confort mais la vérité, même si elle dérange. Tu veux guérir en profondeur, pas superficiellement.

**Ton approche instinctive** : Le Scorpion te fait explorer les abysses de ton psyché. Tu n'as pas peur de ce que tu vas trouver dans ton ombre. Cette intensité peut créer une vraie transformation ou te perdre dans l'obscurité.

**Tensions possibles** : L'obsession de ton ombre qui te fait négliger la lumière. Tu risques de rester dans les profondeurs sans jamais revenir à la surface.

**Conseil clé** : Plonger profondément dans ton inconscient tout en gardant un lien avec la vie.""",
        'weekly_advice': {
            'week_1': "Retire-toi pour affronter ce que tu évites habituellement.",
            'week_2': "Plonge dans ton ombre sans peur, avec courage.",
            'week_3': "Commence à remonter avec ce que tu as trouvé.",
            'week_4': "Intègre cette transformation dans ta vie quotidienne."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Retraite expansive**

Ta Lune en Taureau en Maison 12 veut une retraite simple et locale. Ton Ascendant Sagittaire ajoute de l'expansion : tu veux un pèlerinage spirituel, une quête de sens qui élargit ta conscience, une retraite qui te fait voyager intérieurement.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude deviennent une aventure. Tu explores ton monde intérieur comme un territoire vaste, tu cherches le sens dans ton ombre.

**Ton approche instinctive** : Le Sagittaire te fait voir l'introspection comme une exploration. Tu médites sur le sens de la vie, tu cherches des enseignements spirituels qui élargissent ta vision. Cette quête peut t'ouvrir ou te faire fuir le travail émotionnel concret.

**Tensions possibles** : La tendance à intellectualiser ou philosophiser ton inconscient au lieu de le ressentir. Tu risques de chercher le sens sans faire le travail de guérison.

**Conseil clé** : Explorer largement ton monde intérieur tout en ancrant tes découvertes.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans une quête spirituelle qui t'inspire.",
            'week_2': "Explore les enseignements qui résonnent avec ton âme.",
            'week_3': "Ancre ces découvertes dans ton corps et tes émotions.",
            'week_4': "Intègre cette sagesse dans ta vie concrète."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Retraite structurée**

Ta Lune en Taureau en Maison 12 veut se ressourcer naturellement. Ton Ascendant Capricorne ajoute de la discipline : tu veux structurer ton travail intérieur, maîtriser ton inconscient, construire une pratique spirituelle solide et durable.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude deviennent un projet à long terme. Tu veux guérir méthodiquement, progresser dans ta vie intérieure avec la même rigueur que dans ta carrière.

**Ton approche instinctive** : Le Capricorne te fait aborder l'introspection avec sérieux. Tu établis une discipline spirituelle stricte, tu mesures tes progrès intérieurs. Cette structure peut soutenir ou rigidifier ton processus.

**Tensions possibles** : Le contrôle excessif de ton monde intérieur qui empêche les émergences spontanées. Tu risques de vouloir diriger ton inconscient au lieu de l'écouter.

**Conseil clé** : Structurer ta pratique intérieure tout en restant ouvert aux surprises de l'inconscient.""",
        'weekly_advice': {
            'week_1': "Établis une pratique spirituelle régulière et engagée.",
            'week_2': "Maintiens cette discipline même si c'est difficile.",
            'week_3': "Laisse aussi de la place pour l'imprévu intérieur.",
            'week_4': "Célèbre la solidité de ta connexion intérieure."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Solitude libératrice**

Ta Lune en Taureau en Maison 12 veut une retraite confortable et traditionnelle. Ton Ascendant Verseau ajoute de l'innovation : tu explores ton inconscient de façon non-conventionnelle, tu expérimentes des pratiques spirituelles alternatives, tu libères ton âme des conditionnements.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude deviennent un laboratoire d'expérimentation. Tu veux te libérer des patterns qui t'enferment, trouver ta voie spirituelle unique.

**Ton approche instinctive** : Le Verseau te fait révolutionner ton rapport à l'inconscient. Tu essaies des approches avant-gardistes, tu refuses les dogmes spirituels. Cette originalité peut libérer ou te faire rejeter ce qui pourrait t'aider.

**Tensions possibles** : Le rejet des pratiques traditionnelles par besoin de différence. Tu risques d'expérimenter sans ancrage solide et de te perdre.

**Conseil clé** : Innover dans ton approche spirituelle tout en gardant un ancrage concret.""",
        'weekly_advice': {
            'week_1': "Explore une pratique spirituelle non-conventionnelle.",
            'week_2': "Expérimente avec ouverture et discernement.",
            'week_3': "Garde ce qui fonctionne vraiment pour toi.",
            'week_4': "Ancre ta pratique unique dans ta vie quotidienne."
        }
    },

    {
        'moon_sign': 'Taurus', 'moon_house': 12, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Fusion spirituelle**

Ta Lune en Taureau en Maison 12 veut se ressourcer dans le concret et la nature. Ton Ascendant Poissons amplifie la Maison 12 : tu veux fusionner avec l'univers, dissoudre les frontières de l'ego, expérimenter l'unité mystique avec le tout.

**Domaine activé** : Maison 12 — Ton inconscient, ta spiritualité, ton besoin de solitude sont au maximum de leur puissance. Tu as besoin de te retirer du monde pour te connecter au divin, à l'invisible, à la source universelle.

**Ton approche instinctive** : Le Poissons te fait chercher la transcendance complète. Tu médites profondément, tu rêves lucidement, tu accèdes à des états modifiés de conscience. Cette sensibilité peut être mystique ou te faire perdre pied dans la réalité.

**Tensions possibles** : La difficulté à revenir dans le monde concret après tes expériences spirituelles. Tu risques de vouloir rester dans l'invisible et de négliger ta vie matérielle.

**Conseil clé** : Expérimenter la transcendance tout en gardant un ancrage dans ton corps et ta vie.""",
        'weekly_advice': {
            'week_1': "Retire-toi pour méditer profondément et te connecter.",
            'week_2': "Accueille les expériences mystiques qui émergent.",
            'week_3': "Commence à redescendre dans ton corps et tes sens.",
            'week_4': "Intègre cette spiritualité dans ta vie matérielle concrète."
        }
    },
]

if __name__ == "__main__":
    asyncio.run(insert_batch(BATCH))
