"""Batch complet: Sagittarius - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # ==================== MAISON 1 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Feu libre**

Ce mois-ci, double feu sur ton identité : Lune en Sagittaire, Maison 1, Ascendant lunaire Bélier. L'énergie est explosive, optimiste, tournée vers l'expansion immédiate. Tu ressens un besoin viscéral de liberté, d'aventure, de sens. Tes émotions cherchent l'horizon.

**Domaine activé** : Maison 1 — Ton identité personnelle demande de l'espace et du mouvement. Tu veux te redéfinir à travers l'exploration, montrer qui tu es vraiment sans contraintes. Ton image, ta vision du monde, ta philosophie de vie occupent ton esprit.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu fonces vers ce qui t'inspire. Face aux obstacles, ta première réaction est de charger vers l'avant avec foi et courage. Cette spontanéité rend tout possible.

**Tensions possibles** : Trop d'impulsivité peut créer des départs sans retour ou des promesses non tenues. L'excès d'optimisme risque de te faire sous-estimer les défis réels.

**Conseil clé** : Canaliser cette énergie expansive vers une quête personnelle qui te représente vraiment.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans une aventure qui élargit ta vision de toi-même.",
            'week_2': "Explore un territoire nouveau, physique ou mental.",
            'week_3': "Ajuste ta trajectoire sans perdre ta foi en toi.",
            'week_4': "Célèbre tout ce que tu as découvert sur toi-même."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Expansion ancrée**

Ta Lune en Sagittaire en Maison 1 te pousse à explorer, à grandir, à t'ouvrir au monde. Mais ton Ascendant lunaire Taureau demande du concret et de la stabilité. Une danse entre la soif d'horizon et le besoin de terre sous les pieds.

**Domaine activé** : Maison 1 — Ton identité cherche à s'exprimer à travers la sagesse et l'expérience. Tu veux te montrer comme quelqu'un d'ouvert, de philosophe, mais aussi de fiable. Les questions de sens et d'authenticité te préoccupent.

**Ton approche instinctive** : L'Ascendant Taureau te fait construire ton expansion lentement. Tu veux croître de manière tangible, avec des preuves concrètes. Cette prudence tempère ton optimisme naturel.

**Tensions possibles** : Le besoin d'explorer (Sagittaire) contre le besoin de sécurité (Taureau) crée une friction. Tu peux te sentir tiraillé·e entre partir et rester, entre risquer et protéger.

**Conseil clé** : Grandir progressivement — chaque expérience solidement intégrée avant la suivante.""",
        'weekly_advice': {
            'week_1': "Identifie une direction d'expansion qui respecte tes valeurs.",
            'week_2': "Pose des bases concrètes pour ton développement personnel.",
            'week_3': "Fais un pas hors de ta zone de confort, mais pas un saut.",
            'week_4': "Savoure la croissance stable que tu as accomplie."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Explorateur mental**

Ta Lune en Sagittaire en Maison 1 cherche le sens et la vision globale. Ton Ascendant Gémeaux ajoute curiosité intellectuelle et agilité mentale. Tu es un·e voyageur·se des idées, un·e connecteur·se entre mondes.

**Domaine activé** : Maison 1 — Ton identité s'exprime à travers la quête de connaissance et de compréhension. Tu veux te montrer comme quelqu'un d'érudit, d'ouvert d'esprit, capable de voir les connexions que d'autres manquent.

**Ton approche instinctive** : Le Gémeaux te fait explorer par la communication et l'apprentissage multiple. Tu papillonnes d'un sujet à l'autre, cherchant toujours la pépite d'information qui ouvrira une nouvelle perspective.

**Tensions possibles** : La dispersion mentale peut t'empêcher d'atteindre la profondeur philosophique que tu cherches. Tu risques de confondre information et sagesse, quantité et qualité.

**Conseil clé** : Intégrer tes multiples découvertes dans une vision cohérente.""",
        'weekly_advice': {
            'week_1': "Lis, écoute, apprends sur des sujets qui élargissent ta vision.",
            'week_2': "Partage tes idées avec des gens de milieux différents.",
            'week_3': "Cherche le fil conducteur entre tes diverses explorations.",
            'week_4': "Synthétise ce que tu as appris en une compréhension plus vaste."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sagesse émotionnelle**

Ta Lune en Sagittaire en Maison 1 veut s'exprimer avec optimisme et expansion. Ton Ascendant Cancer ajoute profondeur émotionnelle et besoin de sécurité affective. Tu es un·e philosophe qui ressent profondément.

**Domaine activé** : Maison 1 — Ton identité oscille entre l'appel du large et le besoin de foyer. Tu cherches à te montrer comme quelqu'un d'ouvert au monde mais aussi profondément humain, capable d'empathie et de sagesse émotionnelle.

**Ton approche instinctive** : Le Cancer te fait approcher l'expansion avec sensibilité. Tu veux grandir en restant connecté·e à tes racines émotionnelles. Cette combinaison crée une sagesse nourricière.

**Tensions possibles** : La peur de perdre ta sécurité peut freiner ton besoin d'aventure. Tu risques d'alterner entre repli protecteur et élans d'optimisme qui te font fuir tes émotions.

**Conseil clé** : Honorer tes besoins affectifs tout en t'ouvrant à la croissance.""",
        'weekly_advice': {
            'week_1': "Définis ce que signifie 'foyer' dans ton exploration du monde.",
            'week_2': "Explore des territoires qui nourrissent ton âme.",
            'week_3': "Reste en contact avec tes proches pendant tes aventures.",
            'week_4': "Intègre tes découvertes dans ta vie émotionnelle."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Rayonnement inspirant**

Double feu créatif sur ton identité : ta Lune en Sagittaire et ton Ascendant Lion créent une présence magnétique et inspirante. Tu veux briller en montrant ta vision du monde, être reconnu·e pour ta sagesse et ton optimisme.

**Domaine activé** : Maison 1 — Ton identité personnelle cherche à s'exprimer de manière grandiose et généreuse. Tu veux te montrer comme quelqu'un de confiant, de noble, porteur d'une vision qui élève les autres.

**Ton approche instinctive** : Le Lion te fait incarner tes convictions avec fierté et créativité. Tu ne te contentes pas de croire, tu veux inspirer les autres à croire aussi. Cette générosité d'esprit attire naturellement l'attention.

**Tensions possibles** : L'excès de confiance peut virer à l'arrogance. Tu risques de prêcher plutôt que de dialoguer, de vouloir être admiré·e plutôt que compris·e.

**Conseil clé** : Inspirer par l'exemple plutôt que par les grands discours.""",
        'weekly_advice': {
            'week_1': "Exprime ta vision du monde avec authenticité et courage.",
            'week_2': "Crée quelque chose qui incarne tes convictions.",
            'week_3': "Partage ta lumière sans écraser celle des autres.",
            'week_4': "Célèbre la personne inspirante que tu deviens."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Sagesse pragmatique**

Ta Lune en Sagittaire en Maison 1 cherche le sens et l'expansion. Ton Ascendant Vierge ajoute discernement et attention aux détails. Tu es un·e philosophe qui vérifie ses sources, un·e optimiste réaliste.

**Domaine activé** : Maison 1 — Ton identité cherche à allier grande vision et compétence pratique. Tu veux te montrer comme quelqu'un de sage mais aussi d'utile, capable de transformer les idéaux en méthodes applicables.

**Ton approche instinctive** : La Vierge te fait analyser tes convictions. Tu ne crois pas aveuglément, tu cherches la vérité vérifiable. Cette rigueur peut parfois freiner ton enthousiasme naturel.

**Tensions possibles** : L'analyse excessive peut tuer l'inspiration. Tu risques de critiquer tes propres élans d'optimisme ou de te perdre dans les détails au lieu de voir la vision d'ensemble.

**Conseil clé** : Utiliser ton discernement pour affiner ta vision, pas pour la détruire.""",
        'weekly_advice': {
            'week_1': "Examine tes croyances avec honnêteté intellectuelle.",
            'week_2': "Mets en pratique une idée inspirante de manière concrète.",
            'week_3': "Affine ta méthode sans perdre ton enthousiasme.",
            'week_4': "Observe comment rigueur et foi se sont enrichies mutuellement."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie expansive**

Ta Lune en Sagittaire en Maison 1 cherche la vérité et l'aventure. Ton Ascendant Balance ajoute diplomatie et sens de l'équilibre. Tu es un·e explorateur·se qui cherche la paix, un·e philosophe relationnel·le.

**Domaine activé** : Maison 1 — Ton identité s'exprime à travers ta capacité à voir tous les points de vue. Tu veux te montrer comme quelqu'un d'ouvert, de juste, capable de créer des ponts entre cultures et perspectives.

**Ton approche instinctive** : La Balance te fait explorer les idées par le dialogue et la comparaison. Tu cherches la vérité dans l'échange, pas dans l'affirmation dogmatique. Cette approche collaborative enrichit ta philosophie.

**Tensions possibles** : Le besoin de plaire peut diluer tes convictions. Tu risques de relativiser tellement que tu perds ta propre boussole, ou d'éviter l'aventure par peur du conflit.

**Conseil clé** : Maintenir ton nord tout en honorant la diversité des perspectives.""",
        'weekly_advice': {
            'week_1': "Engage des conversations qui élargissent ta compréhension.",
            'week_2': "Cherche l'équilibre entre tes certitudes et ton ouverture.",
            'week_3': "Explore des perspectives opposées aux tiennes avec curiosité.",
            'week_4': "Intègre les insights relationnels dans ta vision personnelle."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité profonde**

Ta Lune en Sagittaire en Maison 1 cherche le sens et l'expansion. Ton Ascendant Scorpion ajoute intensité et besoin de transformation radicale. Tu ne veux pas juste comprendre, tu veux transmuter.

**Domaine activé** : Maison 1 — Ton identité s'exprime à travers une quête de vérité qui va jusqu'au bout, sans compromis. Tu veux te montrer comme quelqu'un d'authentique, qui a le courage de regarder dans les abîmes et d'en revenir avec la sagesse.

**Ton approche instinctive** : Le Scorpion te fait explorer les territoires dangereux de la psyché et du monde. Tu n'as pas peur de la face sombre de la vérité. Cette profondeur donne un poids réel à ton optimisme.

**Tensions possibles** : L'obsession de la vérité peut devenir destructrice. Tu risques de vouloir détruire les illusions des autres de manière brutale, ou de te perdre dans le cynisme déguisé en lucidité.

**Conseil clé** : Chercher la vérité profonde tout en gardant la foi en la possibilité de lumière.""",
        'weekly_advice': {
            'week_1': "Plonge dans une vérité que tu évitais de regarder en face.",
            'week_2': "Transforme une croyance limitante en conviction libératrice.",
            'week_3': "Explore les zones d'ombre de ta philosophie de vie.",
            'week_4': "Émerge avec une sagesse forgée dans les profondeurs."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Liberté totale**

Triple Sagittaire sur ton identité : Lune, Maison 1, Ascendant. L'énergie est pure expansion, optimisme sans limite, foi absolue en la vie. Tu es l'aventurier·ère archétypal·e, le·la philosophe libre, le·la voyageur·se éternel·le.

**Domaine activé** : Maison 1 — Ton identité personnelle EST la quête elle-même. Tu te définis par ton mouvement, ta croissance, ta capacité à voir toujours plus loin. Les limites te sont physiquement insupportables.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu vis selon tes convictions sans compromis. Tu crois en l'abondance, en la bonté fondamentale de l'univers. Cette foi peut déplacer des montagnes ou t'aveugler.

**Tensions possibles** : L'excès d'optimisme peut te déconnecter de la réalité. Tu risques de fuir toute contrainte, tout engagement, toute profondeur qui demande de rester en place.

**Conseil clé** : Honorer ta nature libre tout en acceptant que la croissance réelle demande parfois de s'arrêter pour intégrer.""",
        'weekly_advice': {
            'week_1': "Pars à l'aventure, physiquement ou mentalement.",
            'week_2': "Élargis tes horizons de manière audacieuse.",
            'week_3': "Vérifie que tu n'es pas en train de fuir quelque chose.",
            'week_4': "Intègre tes découvertes avant de repartir."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Vision structurée**

Ta Lune en Sagittarius en Maison 1 cherche l'expansion et le sens. Ton Ascendant Capricorne ajoute discipline et ambition à long terme. Tu es un·e visionnaire qui construit, un·e philosophe qui matérialise.

**Domaine activé** : Maison 1 — Ton identité cherche à allier grande vision et réalisation concrète. Tu veux te montrer comme quelqu'un qui ne se contente pas de rêver mais qui transforme les idéaux en institutions durables.

**Ton approche instinctive** : Le Capricorne te fait grimper vers tes visions. Tu es prêt·e à faire le travail dur pour atteindre tes idéaux. Cette combinaison crée un optimisme mature et responsable.

**Tensions possibles** : Le sérieux peut étouffer ta spontanéité naturelle. Tu risques de te sentir déchiré·e entre ton besoin de liberté et tes responsabilités, entre foi et cynisme pragmatique.

**Conseil clé** : Construire patiemment ta vision sans perdre l'inspiration qui l'anime.""",
        'weekly_advice': {
            'week_1': "Définis une vision à long terme qui t'inspire vraiment.",
            'week_2': "Crée un plan concret pour y arriver étape par étape.",
            'week_3': "Fais le travail même quand l'enthousiasme retombe.",
            'week_4': "Célèbre les fondations solides que tu as posées."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Avant-garde visionnaire**

Ta Lune en Sagittaire en Maison 1 cherche la vérité et l'expansion. Ton Ascendant Verseau ajoute innovation et conscience collective. Tu es un·e révolutionnaire philosophique, un·e porteur·se d'avenir.

**Domaine activé** : Maison 1 — Ton identité s'exprime à travers ta capacité à voir le futur et à libérer les consciences. Tu veux te montrer comme quelqu'un d'original, d'éclairé, qui ouvre des voies nouvelles pour l'humanité.

**Ton approche instinctive** : Le Verseau te fait chercher les idées qui changent le paradigme. Tu ne veux pas juste évoluer, tu veux révolutionner. Cette audace intellectuelle peut vraiment faire bouger les lignes.

**Tensions possibles** : L'excès d'abstraction peut te déconnecter de l'humain concret. Tu risques de devenir dogmatique sur ton progressisme ou de te perdre dans des utopies irréalistes.

**Conseil clé** : Rester ancré·e dans l'humanité réelle tout en portant la vision du futur.""",
        'weekly_advice': {
            'week_1': "Explore des idées vraiment nouvelles, même dérangeantes.",
            'week_2': "Connecte-toi à des communautés d'avant-garde.",
            'week_3': "Teste tes théories dans le monde réel.",
            'week_4': "Partage ta vision de manière accessible."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Mystique voyageur**

Ta Lune en Sagittaire en Maison 1 cherche le sens et la vérité. Ton Ascendant Poissons ajoute dimension spirituelle et dissolution des frontières. Tu es un·e pèlerin·e de l'âme, un·e philosophe mystique.

**Domaine activé** : Maison 1 — Ton identité s'exprime à travers ta quête de transcendance. Tu veux te montrer comme quelqu'un qui a accès à des vérités universelles, qui vit au-delà des limites ordinaires de l'ego.

**Ton approche instinctive** : Le Poissons te fait explorer par l'intuition et la sensibilité spirituelle. Tu ressens la vérité plus que tu ne la penses. Cette perméabilité peut créer une sagesse profonde.

**Tensions possibles** : Le manque de limites peut te faire perdre pied dans la réalité. Tu risques de confondre imagination et inspiration, illusion et illumination, fuite et foi.

**Conseil clé** : Vivre ta spiritualité expansive tout en gardant un minimum d'ancrage terrestre.""",
        'weekly_advice': {
            'week_1': "Médite sur les grandes questions existentielles.",
            'week_2': "Explore des pratiques spirituelles qui élargissent ta conscience.",
            'week_3': "Vérifie que tu n'es pas en train de fuir par le spirituel.",
            'week_4': "Intègre tes insights mystiques dans ta vie quotidienne."
        }
    },

    # ==================== MAISON 2 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Abondance conquise**

Ta Lune en Sagittaire active la Maison 2 : tes ressources deviennent terrain d'expansion. Avec l'Ascendant Bélier, tu veux conquérir l'abondance avec audace et foi. L'argent est un moyen de liberté, pas une fin.

**Domaine activé** : Maison 2 — Tes finances, tes possessions, ta valeur personnelle cherchent à croître. Tu veux que tes ressources augmentent pour soutenir ta quête d'aventure et de sens. L'investissement dans l'expérience t'attire.

**Ton approche instinctive** : Le Bélier te fait foncer vers les opportunités financières avec optimisme. Tu es prêt·e à prendre des risques pour l'abondance. Cette audace peut créer de vraies percées.

**Tensions possibles** : L'excès d'optimisme peut te faire surestimer tes capacités ou ignorer les limites réelles. Tu risques de dépenser avant d'avoir gagné, confiant que l'univers fournira.

**Conseil clé** : Canaliser ta foi en l'abondance vers des actions concrètes et calculées.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans une opportunité financière qui t'inspire.",
            'week_2': "Investis dans ton développement personnel payant.",
            'week_3': "Prends un risque calculé pour augmenter tes revenus.",
            'week_4': "Évalue si ton optimisme était fondé ou excessif."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Prospérité stable**

Ta Lune en Sagittaire en Maison 2 veut que tes ressources grandissent. Ton Ascendant Taureau, maître naturel de cette maison, apporte sagesse instinctive : tu sais que l'abondance réelle se construit lentement.

**Domaine activé** : Maison 2 — Tes finances et possessions cherchent à la fois expansion (Sagittaire) et solidité (Taureau). Tu veux croître de manière tangible, bâtir une prospérité durable qui soutient ta liberté.

**Ton approche instinctive** : Le Taureau te fait investir dans ce qui a de la vraie valeur. Tu cherches la qualité, le durable, le concret. Cette approche tempère ton optimisme de manière très productive.

**Tensions possibles** : La tension entre viser grand (Sagittaire) et sécuriser (Taureau) peut créer de l'hésitation. Tu risques de retenir ton expansion par peur ou de te forcer à une stabilité qui t'étouffe.

**Conseil clé** : Grandir financièrement de manière progressive mais continue.""",
        'weekly_advice': {
            'week_1': "Définis un objectif d'abondance inspirant mais réaliste.",
            'week_2': "Mets en place des habitudes qui génèrent de la valeur durable.",
            'week_3': "Investis dans ce qui garde sa valeur à long terme.",
            'week_4': "Savoure la prospérité stable que tu construis."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Revenus multiples**

Ta Lune en Sagittaire en Maison 2 cherche l'expansion financière. Ton Ascendant Gémeaux ajoute agilité et diversification. Tu veux créer de multiples sources de revenus, explorer divers moyens de prospérer.

**Domaine activé** : Maison 2 — Tes ressources se développent par la variété et l'adaptabilité. Tu es attiré·e par les opportunités intellectuelles payantes, l'entrepreneuriat multiple, les revenus qui viennent de ta capacité à connecter.

**Ton approche instinctive** : Le Gémeaux te fait explorer les opportunités financières par la communication et le réseau. Tu gagnes en partageant tes connaissances, en créant des ponts, en restant curieux·se.

**Tensions possibles** : La dispersion peut t'empêcher de capitaliser vraiment sur tes talents. Tu risques de papillonner financièrement sans jamais approfondir une source d'abondance.

**Conseil clé** : Diversifier intelligemment sans te disperser au point de perdre en efficacité.""",
        'weekly_advice': {
            'week_1': "Identifie plusieurs sources potentielles de revenus.",
            'week_2': "Développe tes compétences de communication payantes.",
            'week_3': "Crée des connexions qui peuvent mener à des opportunités.",
            'week_4': "Évalue quelle diversification fonctionne vraiment."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sécurité généreuse**

Ta Lune en Sagittaire en Maison 2 veut l'expansion financière. Ton Ascendant Cancer ajoute besoin de sécurité émotionnelle et familiale. Tes ressources doivent nourrir à la fois ton aventure et ton foyer.

**Domaine activé** : Maison 2 — Tes finances cherchent à créer une base sécurisante qui permet l'exploration. Tu veux l'abondance pour prendre soin de ceux que tu aimes et te donner la liberté d'explorer.

**Ton approche instinctive** : Le Cancer te fait protéger tes ressources tout en les partageant généreusement. Tu investis dans ce qui crée du confort et de la sécurité affective. L'argent est au service du lien.

**Tensions possibles** : La peur de manquer peut freiner ton expansion. Tu risques d'alterner entre générosité excessive et rétention anxieuse, entre foi et peur.

**Conseil clé** : Construire une sécurité qui libère plutôt qu'elle n'enferme.""",
        'weekly_advice': {
            'week_1': "Définis le niveau de sécurité qui te permet d'explorer.",
            'week_2': "Investis dans ce qui nourrit émotionnellement.",
            'week_3': "Partage ton abondance avec ceux qui comptent.",
            'week_4': "Vérifie que ta sécurité ne devient pas une prison."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Richesse rayonnante**

Double feu sur la Maison 2 : ta Lune en Sagittaire et ton Ascendant Lion créent une énergie d'abondance confiante. Tu crois en ta capacité à prospérer grandement, et cette foi attire les opportunités.

**Domaine activé** : Maison 2 — Tes ressources cherchent à croître de manière visible et généreuse. Tu veux une abondance qui te permet de vivre royalement et de partager avec magnificence. L'argent est au service de ta créativité.

**Ton approche instinctive** : Le Lion te fait investir dans ce qui a de la classe, de la beauté, de la noblesse. Tu ne veux pas juste l'argent, tu veux la prospérité qui exprime qui tu es vraiment.

**Tensions possibles** : L'excès de confiance peut mener à l'arrogance financière. Tu risques de dépenser pour impressionner ou de surestimer ta capacité à générer de l'abondance.

**Conseil clé** : Vivre avec générosité tout en maintenant une gestion réaliste.""",
        'weekly_advice': {
            'week_1': "Définis une vision d'abondance qui t'inspire vraiment.",
            'week_2': "Investis dans ce qui exprime ta valeur unique.",
            'week_3': "Partage ta prospérité avec créativité et noblesse.",
            'week_4': "Célèbre l'abondance que tu as créée et incarnée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Abondance analysée**

Ta Lune en Sagittaire en Maison 2 cherche l'expansion financière. Ton Ascendant Vierge ajoute discernement et attention aux détails. Tu es un·e optimiste qui vérifie ses chiffres, un·e croyant·e pragmatique.

**Domaine activé** : Maison 2 — Tes ressources cherchent à croître de manière intelligente et efficace. Tu veux l'abondance par la compétence, le service de qualité, l'amélioration continue de ce que tu offres au monde.

**Ton approche instinctive** : La Vierge te fait analyser tes opportunités financières. Tu ne crois pas aveuglément, tu vérifies. Cette rigueur peut protéger ton expansion de l'excès.

**Tensions possibles** : L'analyse excessive peut paralyser ton élan. Tu risques de critiquer tes propres opportunités ou de te perdre dans les détails au lieu de saisir la vision d'ensemble.

**Conseil clé** : Utiliser ton discernement pour affiner ta stratégie d'abondance, pas pour la bloquer.""",
        'weekly_advice': {
            'week_1': "Examine tes finances avec honnêteté et précision.",
            'week_2': "Améliore la qualité de ce que tu offres contre rémunération.",
            'week_3': "Optimise tes systèmes de gestion de ressources.",
            'week_4': "Observe comment rigueur et foi se sont enrichies."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Prospérité partagée**

Ta Lune en Sagittaire en Maison 2 cherche l'expansion des ressources. Ton Ascendant Balance ajoute sens de l'équité et besoin de partenariat. Ta prospérité passe par la collaboration et l'harmonie.

**Domaine activé** : Maison 2 — Tes finances se développent à travers les relations équitables. Tu veux créer de l'abondance partagée, des situations gagnant-gagnant, des partenariats qui enrichissent toutes les parties.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre dans tes échanges financiers. Tu veux que ce soit juste, beau, harmonieux. Cette approche relationnelle peut ouvrir des opportunités inattendues.

**Tensions possibles** : Le besoin d'harmonie peut te faire accepter moins que ta valeur. Tu risques de sacrifier ton expansion pour maintenir la paix ou de trop dépendre des autres pour ta prospérité.

**Conseil clé** : Créer des partenariats d'abondance tout en maintenant ton autonomie.""",
        'weekly_advice': {
            'week_1': "Identifie des opportunités de collaboration financière.",
            'week_2': "Négocie des accords qui respectent ta valeur et celle des autres.",
            'week_3': "Investis dans des relations qui créent de l'abondance mutuelle.",
            'week_4': "Évalue l'équité réelle de tes échanges financiers."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Richesse transformée**

Ta Lune en Sagittaire en Maison 2 cherche l'expansion financière. Ton Ascendant Scorpion ajoute intensité et transformation profonde. L'argent est un outil de pouvoir et de métamorphose personnelle.

**Domaine activé** : Maison 2 — Tes ressources traversent une transformation radicale. Tu veux non seulement augmenter tes finances mais changer complètement ta relation à l'argent, au pouvoir, à la valeur.

**Ton approche instinctive** : Le Scorpion te fait aller au fond des mécanismes financiers. Tu n'as pas peur de regarder tes peurs d'abondance en face, de transformer tes blocages profonds autour de la valeur.

**Tensions possibles** : L'obsession du contrôle financier peut créer de l'anxiété. Tu risques d'alterner entre générosité excessive et rétention compulsive, entre foi et cynisme.

**Conseil clé** : Transformer ta relation à l'argent en profondeur, pas juste changer les montants.""",
        'weekly_advice': {
            'week_1': "Regarde en face tes peurs et croyances sur l'argent.",
            'week_2': "Élimine une dette ou une dépendance financière.",
            'week_3': "Investis dans ce qui te donne du vrai pouvoir.",
            'week_4': "Observe la transformation de ta relation à la valeur."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foi en l'abondance**

Triple Sagittaire sur tes ressources : Lune, Maison 2, Ascendant. L'énergie est pure foi en l'abondance, optimisme financier total. Tu crois profondément que l'univers fournit, et cette croyance crée sa propre réalité.

**Domaine activé** : Maison 2 — Tes finances sont un terrain de pure expansion. Tu veux que tes ressources grandissent pour soutenir ta liberté et tes aventures. L'argent est au service de la croissance, jamais une fin en soi.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu vis selon la loi de l'abondance sans compromis. Tu donnes généreusement, tu investis audacieusement, tu crois que plus tu partages, plus tu reçois.

**Tensions possibles** : L'excès d'optimisme peut te déconnecter de la réalité financière. Tu risques de dépenser sans compter, d'ignorer les limites, de confondre foi et irresponsabilité.

**Conseil clé** : Honorer ta foi en l'abondance tout en gérant concrètement tes ressources.""",
        'weekly_advice': {
            'week_1': "Définis ta philosophie personnelle de l'abondance.",
            'week_2': "Agis selon ta foi en la prospérité.",
            'week_3': "Vérifie que ton optimisme est ancré dans le réel.",
            'week_4': "Célèbre l'abondance qui circule dans ta vie."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Empire bâti**

Ta Lune en Sagittaire en Maison 2 cherche l'expansion financière. Ton Ascendant Capricorne ajoute ambition à long terme et discipline. Tu construis une prospérité durable qui soutient ta vision.

**Domaine activé** : Maison 2 — Tes ressources cherchent à croître de manière structurée et ambitieuse. Tu veux bâtir une fortune, pas juste gagner de l'argent. L'investissement patient dans ta valeur à long terme t'attire.

**Ton approche instinctive** : Le Capricorne te fait grimper vers l'abondance étape par étape. Tu es prêt·e à faire le travail dur, à attendre, à construire patiemment. Cette maturité financière est rare et puissante.

**Tensions possibles** : Le sérieux peut étouffer ta générosité naturelle. Tu risques de te sentir déchiré·e entre expansion et conservation, entre foi et cynisme pragmatique.

**Conseil clé** : Construire patiemment ta prospérité sans perdre la joie de l'abondance.""",
        'weekly_advice': {
            'week_1': "Définis un objectif financier à 5-10 ans qui t'inspire.",
            'week_2': "Crée un plan concret pour y arriver progressivement.",
            'week_3': "Investis dans ce qui prend de la valeur avec le temps.",
            'week_4': "Célèbre les fondations solides de ta prospérité future."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Richesse collective**

Ta Lune en Sagittaire en Maison 2 cherche l'expansion des ressources. Ton Ascendant Verseau ajoute innovation et conscience sociale. Tu veux créer de l'abondance qui sert le collectif, qui libère les autres.

**Domaine activé** : Maison 2 — Tes finances se développent à travers des modèles novateurs et éthiques. Tu es attiré·e par l'économie collaborative, les revenus qui viennent de ta contribution à un futur meilleur.

**Ton approche instinctive** : Le Verseau te fait chercher des moyens originaux de prospérer. Tu veux que ton abondance soit alignée avec tes valeurs humanistes. Cette intégrité attire des opportunités uniques.

**Tensions possibles** : L'idéalisme peut te faire mépriser l'argent ou te déconnecter de tes besoins matériels réels. Tu risques de donner au point de t'appauvrir ou de rejeter la prospérité par peur de trahir tes idéaux.

**Conseil clé** : Créer de l'abondance innovante tout en honorant tes besoins concrets.""",
        'weekly_advice': {
            'week_1': "Explore des modèles financiers novateurs et éthiques.",
            'week_2': "Connecte-toi à des réseaux qui partagent tes valeurs.",
            'week_3': "Investis dans des projets qui servent le bien commun.",
            'week_4': "Évalue si tes idéaux financiers sont viables."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Abondance spirituelle**

Ta Lune en Sagittaire en Maison 2 cherche l'expansion des ressources. Ton Ascendant Poissons ajoute dimension spirituelle et fluidité. Tu veux une prospérité qui nourrit l'âme, pas juste le compte en banque.

**Domaine activé** : Maison 2 — Tes finances cherchent à refléter ta foi spirituelle. Tu es attiré·e par les revenus qui viennent de ta créativité, de ton intuition, de ta capacité à inspirer. L'argent doit avoir un sens.

**Ton approche instinctive** : Le Poissons te fait aborder l'abondance avec confiance mystique. Tu crois que l'univers fournit à ceux qui sont alignés. Cette foi peut créer des synchronicités financières étonnantes.

**Tensions possibles** : Le manque de limites peut créer le chaos financier. Tu risques de confondre foi et passivité, de fuir la gestion concrète par le spirituel, de te faire avoir par naïveté.

**Conseil clé** : Vivre ta foi en l'abondance tout en gérant concrètement tes ressources.""",
        'weekly_advice': {
            'week_1': "Médite sur ta relation spirituelle à l'argent.",
            'week_2': "Crée de la valeur à partir de tes dons intuitifs.",
            'week_3': "Vérifie que ta foi n'est pas de la passivité déguisée.",
            'week_4': "Ancre tes insights sur l'abondance dans des actions concrètes."
        }
    },

    # ==================== MAISON 3 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Communication audacieuse**

Ta Lune en Sagittaire active la Maison 3 : ta communication devient terrain d'expansion. Avec l'Ascendant Bélier, tu veux parler franchement, enseigner audacieusement, partager ta vérité sans filtre.

**Domaine activé** : Maison 3 — Tes échanges quotidiens, tes apprentissages, ton environnement proche sont illuminés par ta vision. Tu veux inspirer par tes mots, élargir les perspectives, faire bouger les idées.

**Ton approche instinctive** : Le Bélier te fait communiquer de manière directe et passionnée. Tu dis ce que tu penses, tu débats avec fougue, tu défends tes convictions. Cette franchise rafraîchit ou choque.

**Tensions possibles** : Tu risques de prêcher plutôt que de dialoguer, d'imposer ta vérité au lieu de la partager. L'excès de conviction peut fermer les oreilles au lieu de les ouvrir.

**Conseil clé** : Inspirer par l'exemple et l'invitation, pas par l'imposition.""",
        'weekly_advice': {
            'week_1': "Partage une vérité importante que tu portes.",
            'week_2': "Apprends quelque chose qui élargit vraiment ta vision.",
            'week_3': "Débats avec passion mais reste ouvert·e aux autres perspectives.",
            'week_4': "Observe comment tes mots ont inspiré ou fermé les autres."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sagesse partagée**

Ta Lune en Sagittaire en Maison 3 veut partager des vérités inspirantes. Ton Ascendant Taureau ajoute ancrage et patience. Tu es un·e enseignant·e qui prend le temps de bien transmettre, de construire la compréhension.

**Domaine activé** : Maison 3 — Ta communication cherche à allier vision et concrétude. Tu veux partager des idées qui ont une application pratique, enseigner de manière tangible ce que tu as compris.

**Ton approche instinctive** : Le Taureau te fait communiquer avec constance et simplicité. Tu veux que ton message soit accessible, utilisable, durable. Cette approche rend ta philosophie réellement applicable.

**Tensions possibles** : La tension entre vision expansive et expression concrète peut créer de la frustration. Tu risques de simplifier à l'excès ou de t'enliser dans les détails.

**Conseil clé** : Partager ta vision de manière progressive et assimilable.""",
        'weekly_advice': {
            'week_1': "Identifie une vérité que tu peux enseigner concrètement.",
            'week_2': "Construis un système de transmission patient et solide.",
            'week_3': "Vérifie que ton message est vraiment compris.",
            'week_4': "Savoure l'impact durable de tes mots."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Messager universel**

Ta Lune en Sagittaire en Maison 3 cherche le sens dans la communication. Ton Ascendant Gémeaux, maître naturel de cette maison, ajoute agilité mentale et curiosité. Tu es un·e traducteur·rice entre mondes et idées.

**Domaine activé** : Maison 3 — Tes apprentissages et échanges sont électrifiés. Tu veux tout apprendre, tout comprendre, connecter les savoirs. Ta communication devient un pont entre perspectives locales et visions universelles.

**Ton approche instinctive** : Le Gémeaux te fait explorer les idées par tous les angles. Tu papillonnes intellectuellement, cherchant toujours la connexion suivante, l'insight nouveau. Cette agilité mentale est rare.

**Tensions possibles** : La dispersion peut t'empêcher d'approfondir vraiment. Tu risques de confondre information et sagesse, de parler beaucoup sans dire grand-chose d'important.

**Conseil clé** : Intégrer tes multiples apprentissages dans une compréhension cohérente.""",
        'weekly_advice': {
            'week_1': "Explore des sujets variés qui élargissent ta perspective.",
            'week_2': "Connecte des idées qui semblaient séparées.",
            'week_3': "Partage tes insights avec différents publics.",
            'week_4': "Synthétise tes découvertes en une vision plus vaste."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Parole nourrissante**

Ta Lune en Sagittaire en Maison 3 cherche à inspirer par les mots. Ton Ascendant Cancer ajoute empathie et besoin de connexion émotionnelle. Tu es un·e conteur·se qui touche le cœur autant que l'esprit.

**Domaine activé** : Maison 3 — Ta communication cherche à créer du lien tout en élevant. Tu veux que tes mots nourrissent émotionnellement, créent de la sécurité, tout en ouvrant de nouveaux horizons.

**Ton approche instinctive** : Le Cancer te fait communiquer avec sensibilité et attention aux besoins émotionnels. Tu sens ce que les autres peuvent entendre. Cette intelligence émotionnelle rend ton enseignement accessible.

**Tensions possibles** : La peur de blesser peut diluer ta vérité. Tu risques d'adapter ton message au point de perdre ton nord, ou de protéger à l'excès au lieu de libérer.

**Conseil clé** : Honorer la sensibilité tout en osant dire des vérités qui dérangent avec amour.""",
        'weekly_advice': {
            'week_1': "Partage une vérité de manière émotionnellement intelligente.",
            'week_2': "Crée des connexions profondes par tes mots.",
            'week_3': "Ose élargir les perspectives tout en restant empathique.",
            'week_4': "Observe comment tu as nourri et libéré par ta communication."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Enseignement rayonnant**

Double feu sur la Maison 3 : ta Lune en Sagittaire et ton Ascendant Lion créent une communication inspirante et magnétique. Tu veux enseigner, créer, partager ta vision de manière qui captive et élève.

**Domaine activé** : Maison 3 — Tes mots, tes idées, tes apprentissages cherchent à briller et à inspirer. Tu veux communiquer avec noblesse, créativité, générosité d'esprit. Ton expression personnelle porte ta philosophie.

**Ton approche instinctive** : Le Lion te fait partager avec fierté et créativité. Tu ne te contentes pas de dire, tu performes ta vérité. Cette dimension théâtrale rend ton message mémorable.

**Tensions possibles** : L'excès d'ego peut transformer l'enseignement en spectacle. Tu risques de vouloir être admiré·e pour ta sagesse plutôt que de servir vraiment la compréhension.

**Conseil clé** : Briller par ta vérité, pas pour ton ego.""",
        'weekly_advice': {
            'week_1': "Exprime tes convictions avec courage et créativité.",
            'week_2': "Crée du contenu qui inspire et élève.",
            'week_3': "Partage généreusement ce que tu sais sans attendre de retour.",
            'week_4': "Célèbre l'impact de ta communication rayonnante."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision philosophique**

Ta Lune en Sagittaire en Maison 3 cherche à partager des visions vastes. Ton Ascendant Vierge ajoute discernement et attention aux détails. Tu es un·e enseignant·e qui vérifie ses sources, un·e philosophe rigoureux·se.

**Domaine activé** : Maison 3 — Ta communication cherche à allier grande vision et exactitude. Tu veux partager des vérités vérifiables, enseigner de manière claire et utile, faire la différence entre croyance et connaissance.

**Ton approche instinctive** : La Vierge te fait analyser et affiner tes idées avant de les partager. Tu veux être précis·e, utile, pratique. Cette rigueur donne du poids à ton enseignement.

**Tensions possibles** : L'analyse excessive peut bloquer ton inspiration. Tu risques de critiquer tes propres insights ou de te perdre dans les détails au lieu de partager la vision d'ensemble.

**Conseil clé** : Utiliser ton discernement pour clarifier ton message, pas pour le censurer.""",
        'weekly_advice': {
            'week_1': "Examine tes convictions avec honnêteté intellectuelle.",
            'week_2': "Affine la précision de ta communication.",
            'week_3': "Partage tes idées de manière claire et applicable.",
            'week_4': "Observe comment rigueur et inspiration se sont enrichies."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Dialogue harmonieux**

Ta Lune en Sagittaire en Maison 3 cherche la vérité dans la communication. Ton Ascendant Balance ajoute diplomatie et sens de l'équilibre. Tu es un·e facilitateur·rice de dialogue, un·e pont entre perspectives.

**Domaine activé** : Maison 3 — Ta communication cherche à créer de l'harmonie tout en élargissant les perspectives. Tu veux que tes échanges soient justes, beaux, équilibrés. Le dialogue devient art.

**Ton approche instinctive** : La Balance te fait explorer les idées par la comparaison et le débat respectueux. Tu cherches la vérité dans l'échange, pas dans l'affirmation unilatérale. Cette approche enrichit tout le monde.

**Tensions possibles** : Le besoin de plaire peut diluer ta vérité. Tu risques de relativiser tellement que tu perds ta propre voix, ou d'éviter les sujets importants par peur du conflit.

**Conseil clé** : Maintenir ton nord philosophique tout en honorant la diversité des perspectives.""",
        'weekly_advice': {
            'week_1': "Engage des dialogues qui élargissent mutuellement les perspectives.",
            'week_2': "Cherche l'équilibre entre partage et écoute.",
            'week_3': "Explore des points de vue opposés avec curiosité sincère.",
            'week_4': "Intègre les insights relationnels dans ta philosophie."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité profonde**

Ta Lune en Sagittaire en Maison 3 cherche à partager des visions inspirantes. Ton Ascendant Scorpion ajoute intensité et besoin de transformation. Tu veux dire les vérités que les autres évitent, plonger dans les zones d'ombre.

**Domaine activé** : Maison 3 — Ta communication cherche à aller au fond des choses. Tu ne veux pas des banalités inspirantes, tu veux la vérité crue qui libère vraiment. Tes mots ont un pouvoir transformateur.

**Ton approche instinctive** : Le Scorpion te fait creuser sous la surface des idées. Tu ne te contentes pas des réponses faciles, tu veux comprendre les mécanismes cachés, les motivations inconscientes.

**Tensions possibles** : L'intensité peut rendre ta communication trop lourde. Tu risques de forcer les vérités sur les autres, de traumatiser au lieu d'éclairer, de confondre profondeur et noirceur.

**Conseil clé** : Chercher et partager la vérité profonde avec compassion pour la fragilité humaine.""",
        'weekly_advice': {
            'week_1': "Ose dire une vérité que tout le monde évite.",
            'week_2': "Explore les zones d'ombre de tes croyances.",
            'week_3': "Partage ta compréhension profonde avec sensibilité.",
            'week_4': "Observe comment tu as transformé les perspectives par ta vérité."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Enseignant naturel**

Triple Sagittaire sur ta communication : Lune, Maison 3, Ascendant. L'énergie est pure expansion intellectuelle, enseignement spontané, partage généreux de sagesse. Tu ES le messager de la vérité.

**Domaine activé** : Maison 3 — Tes mots, tes apprentissages, tes échanges sont naturellement philosophiques. Tu ne peux pas t'empêcher d'enseigner, d'inspirer, d'élargir les perspectives. La communication est ta quête.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu communiques avec optimisme et franchise totale. Tu crois en la puissance libératrice de la vérité. Cette foi rend tes mots puissants.

**Tensions possibles** : L'excès de conviction peut te rendre dogmatique. Tu risques de prêcher sans écouter, d'imposer ta vision, de confondre ta vérité avec LA vérité absolue.

**Conseil clé** : Rester enseignant et éternel étudiant à la fois.""",
        'weekly_advice': {
            'week_1': "Partage généreusement ce que tu as compris.",
            'week_2': "Apprends quelque chose de complètement nouveau.",
            'week_3': "Vérifie que tu écoutes autant que tu enseignes.",
            'week_4': "Célèbre tout ce que tu as appris et partagé."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Autorité sage**

Ta Lune en Sagittaire en Maison 3 cherche à inspirer par les mots. Ton Ascendant Capricorne ajoute maturité et crédibilité. Tu es un·e enseignant·e qui a l'autorité de l'expérience, un·e sage respecté·e.

**Domaine activé** : Maison 3 — Ta communication cherche à construire une réputation de sagesse. Tu veux que tes mots aient du poids, que ton enseignement soit pris au sérieux, que ta vision influence durablement.

**Ton approche instinctive** : Le Capricorne te fait communiquer avec retenue et structure. Tu ne gaspilles pas tes mots, tu les doses. Cette économie donne de la valeur à chaque enseignement.

**Tensions possibles** : Le sérieux peut étouffer ton enthousiasme naturel. Tu risques de te sentir déchiré·e entre inspiration spontanée et communication contrôlée.

**Conseil clé** : Construire ton autorité intellectuelle sans perdre ta spontanéité philosophique.""",
        'weekly_advice': {
            'week_1': "Partage une sagesse mûrie par l'expérience.",
            'week_2': "Construis une structure pour transmettre durablement.",
            'week_3': "Communique avec autorité mais reste accessible.",
            'week_4': "Célèbre la crédibilité de ton enseignement."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolution mentale**

Ta Lune en Sagittaire en Maison 3 cherche à partager des visions inspirantes. Ton Ascendant Verseau ajoute innovation et conscience collective. Tu veux révolutionner les idées, libérer les esprits.

**Domaine activé** : Maison 3 — Ta communication cherche à changer les paradigmes. Tu ne veux pas juste informer, tu veux déconditionner, ouvrir à des perspectives radicalement nouvelles. Tes mots libèrent.

**Ton approche instinctive** : Le Verseau te fait explorer les idées avant-gardistes. Tu cherches ce qui n'a jamais été pensé, ce qui peut vraiment faire évoluer la conscience collective.

**Tensions possibles** : L'excès d'originalité peut te déconnecter de ton audience. Tu risques de devenir tellement abstrait que personne ne te comprend, ou dogmatique sur ton progressisme.

**Conseil clé** : Révolutionner les idées tout en restant compréhensible et humain.""",
        'weekly_advice': {
            'week_1': "Explore des idées vraiment neuves, même dérangeantes.",
            'week_2': "Connecte-toi à des réseaux d'avant-garde intellectuelle.",
            'week_3': "Partage ta vision révolutionnaire de manière accessible.",
            'week_4': "Observe comment tu as ouvert les esprits."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Poésie mystique**

Ta Lune en Sagittaire en Maison 3 cherche à partager la vérité et le sens. Ton Ascendant Poissons ajoute dimension spirituelle et sensibilité artistique. Tu es un·e poète philosophe, un·e mystique qui enseigne.

**Domaine activé** : Maison 3 — Ta communication devient canalisée, intuitive, presque visionnaire. Tu veux transmettre des vérités qui viennent d'au-delà du mental, toucher l'âme par les mots.

**Ton approche instinctive** : Le Poissons te fait communiquer par métaphores, histoires, symboles. Tu ressens le message plus que tu ne le penses. Cette approche poétique touche profondément.

**Tensions possibles** : Le manque de structure peut rendre ton message flou. Tu risques de confondre imagination et inspiration, de perdre ton audience dans les brumes, de fuir la clarté.

**Conseil clé** : Honorer ta sensibilité poétique tout en cherchant la clarté.""",
        'weekly_advice': {
            'week_1': "Laisse l'inspiration couler à travers toi sans censure.",
            'week_2': "Partage tes insights mystiques de manière créative.",
            'week_3': "Vérifie que ton message touche vraiment les autres.",
            'week_4': "Intègre tes visions en communication accessible."
        }
    },

    # ==================== MAISON 4 (suite) ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Foyer aventurier**

Ta Lune en Sagittaire active la Maison 4 : ton foyer et tes racines cherchent l'expansion. Avec l'Ascendant Bélier, tu veux créer un espace de vie qui soutient ta liberté, conquérir ta sécurité émotionnelle avec audace.

**Domaine activé** : Maison 4 — Ton chez-toi et tes fondations émotionnelles demandent de l'espace et du mouvement. Tu veux un foyer qui soit base d'exploration, pas prison. Les questions de liberté familiale te préoccupent.

**Ton approche instinctive** : Le Bélier te fait agir rapidement sur ton espace de vie. Tu veux changer, bouger, redéfinir ce que signifie 'maison' pour toi. Cette spontanéité peut libérer ou déstabiliser.

**Tensions possibles** : L'impulsivité peut créer de l'instabilité dans ton foyer. Tu risques de fuir toute routine domestique, de confondre liberté et absence de racines.

**Conseil clé** : Créer un foyer qui nourrit ta liberté plutôt qu'il ne l'entrave.""",
        'weekly_advice': {
            'week_1': "Redéfinis ce que 'maison' signifie pour toi.",
            'week_2': "Agis pour libérer ton espace de vie des contraintes.",
            'week_3': "Crée une base qui soutient ton exploration.",
            'week_4': "Observe si ton foyer te donne des ailes ou t'alourdit."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Racines libres**

Ta Lune en Sagittaire en Maison 4 cherche un foyer qui libère. Ton Ascendant Taureau, maître naturel des racines, ajoute besoin de stabilité et de confort. Tu veux une base solide qui permette l'aventure.

**Domaine activé** : Maison 4 — Ton chez-toi cherche à allier expansion et sécurité. Tu veux un espace qui soit à la fois ancrage profond et tremplin vers le monde. Les notions de maison multiple ou mobile t'attirent.

**Ton approche instinctive** : Le Taureau te fait construire ton foyer lentement, avec soin. Tu veux du confort et de la beauté qui nourrissent ta liberté. Cette approche crée des bases vraiment solides.

**Tensions possibles** : La tension entre enracinement (Taureau) et nomadisme (Sagittaire) peut créer de l'inconfort. Tu risques d'alterner entre attachement anxieux et fuite de tout engagement domestique.

**Conseil clé** : Construire une sécurité portable, des racines qui voyagent avec toi.""",
        'weekly_advice': {
            'week_1': "Définis le niveau de stabilité qui te libère vraiment.",
            'week_2': "Crée du confort dans ton espace de vie.",
            'week_3': "Vérifie que ta sécurité ne devient pas enfermement.",
            'week_4': "Savoure un foyer qui est base d'aventure."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Maison intellectuelle**

Ta Lune en Sagittaire en Maison 4 cherche un foyer qui nourrit l'esprit. Ton Ascendant Gémeaux ajoute besoin de stimulation mentale et de connexions. Ton chez-toi est une bibliothèque vivante, un carrefour d'idées.

**Domaine activé** : Maison 4 — Tes racines se trouvent dans la connaissance et les échanges. Tu veux un foyer rempli de livres, de conversations, d'apprentissages. La famille intellectuelle compte autant que la biologique.

**Ton approche instinctive** : Le Gémeaux te fait créer un espace de vie flexible et stimulant. Tu veux pouvoir apprendre, communiquer, explorer depuis ton foyer. Cette agilité est ta sécurité.

**Tensions possibles** : La dispersion peut t'empêcher de vraiment t'enraciner. Tu risques de papillonner entre domiciles, de confondre mouvement et croissance.

**Conseil clé** : Créer une base intellectuelle qui voyage avec toi.""",
        'weekly_advice': {
            'week_1': "Fais de ton foyer un espace d'apprentissage continu.",
            'week_2': "Connecte ton chez-toi au monde par les idées.",
            'week_3': "Partage ton espace avec des esprits curieux.",
            'week_4': "Observe comment ton foyer nourrit ton esprit."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Nid expansif**

Ta Lune en Sagittaire en Maison 4 cherche un foyer qui libère. Ton Ascendant Cancer, maître naturel de cette maison, ajoute besoin profond de sécurité émotionnelle et de famille. Le paradoxe est intense.

**Domaine activé** : Maison 4 — Ton chez-toi oscille entre besoin de cocon et appel du large. Tu veux créer un foyer qui nourrit émotionnellement tout en permettant l'exploration. La famille élargie, multiculturelle t'attire.

**Ton approche instinctive** : Le Cancer te fait protéger et nourrir ton foyer. Tu veux créer un espace de sécurité affective profonde. Cette sensibilité enrichit ton besoin d'expansion.

**Tensions possibles** : La peur de perdre ta base peut freiner ton aventure. Tu risques d'alterner entre accrochage anxieux et fuite émotionnelle déguisée en liberté.

**Conseil clé** : Honorer ton besoin de nid tout en gardant les fenêtres ouvertes sur le monde.""",
        'weekly_advice': {
            'week_1': "Définis ce qui te fait vraiment te sentir chez toi.",
            'week_2': "Crée de la sécurité émotionnelle portable.",
            'week_3': "Nourris tes racines sans t'y emprisonner.",
            'week_4': "Observe comment foyer et liberté se sont réconciliés."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Palais nomade**

Double feu sur la Maison 4 : ta Lune en Sagittaire et ton Ascendant Lion créent un foyer généreux et inspirant. Tu veux un espace de vie qui soit à la fois château et porte vers le monde.

**Domaine activé** : Maison 4 — Ton chez-toi cherche à exprimer ta noblesse et ta vision. Tu veux un foyer magnifique qui accueille largement, qui est à la fois ancrage et célébration de la vie.

**Ton approche instinctive** : Le Lion te fait créer un espace de vie avec fierté et créativité. Tu veux que ton foyer soit beau, généreux, reflet de qui tu es. Cette approche crée des espaces mémorables.

**Tensions possibles** : L'excès peut créer un foyer qui impressionne plus qu'il ne nourrit. Tu risques de surinvestir dans l'apparence ou de fuir toute intimité réelle.

**Conseil clé** : Créer un foyer qui rayonne tout en étant vraiment habité.""",
        'weekly_advice': {
            'week_1': "Exprime ta vision dans ton espace de vie.",
            'week_2': "Crée de la beauté et de la générosité chez toi.",
            'week_3': "Accueille le monde dans ton foyer avec noblesse.",
            'week_4': "Célèbre l'espace de vie inspirant que tu as créé."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Ordre libérateur**

Ta Lune en Sagittaire en Maison 4 cherche un foyer qui permette l'expansion. Ton Ascendant Vierge ajoute besoin d'ordre et de fonctionnalité. Tu veux un espace de vie organisé qui soutient efficacement ton aventure.

**Domaine activé** : Maison 4 — Ton chez-toi cherche à allier vision et praticité. Tu veux un foyer qui fonctionne bien, où tout a sa place, ce qui libère ton énergie pour l'exploration.

**Ton approche instinctive** : La Vierge te fait créer des systèmes domestiques efficaces. Tu veux que ton foyer soit sain, propre, organisé. Cette rigueur peut vraiment servir ta liberté.

**Tensions possibles** : L'excès de contrôle peut étouffer la spontanéité. Tu risques de te perdre dans les détails domestiques ou de critiquer ton foyer au lieu de l'habiter.

**Conseil clé** : Utiliser l'organisation pour libérer, pas pour contraindre.""",
        'weekly_advice': {
            'week_1': "Organise ton espace de vie de manière fonctionnelle.",
            'week_2': "Crée des systèmes qui simplifient ton quotidien.",
            'week_3': "Vérifie que ton ordre sert ta liberté.",
            'week_4': "Savoure un foyer qui fonctionne au service de ta vie."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Havre harmonieux**

Ta Lune en Sagittaire en Maison 4 cherche un foyer qui libère. Ton Ascendant Balance ajoute besoin d'harmonie et de beauté. Tu veux un espace de vie équilibré qui soit ouvert aux autres et au monde.

**Domaine activé** : Maison 4 — Ton chez-toi cherche à être à la fois refuge personnel et lieu de rencontre. Tu veux créer un foyer beau, harmonieux, qui accueille la diversité tout en nourrissant ton besoin de paix.

**Ton approche instinctive** : La Balance te fait créer un espace de vie esthétique et équilibré. Tu veux que ton foyer soit agréable pour toi et les autres. Cette approche relationnelle enrichit ton espace.

**Tensions possibles** : Le besoin d'harmonie peut t'empêcher de poser des limites. Tu risques de sacrifier ton besoin d'espace personnel pour plaire ou d'éviter les décisions domestiques par peur du conflit.

**Conseil clé** : Créer un foyer harmonieux qui respecte aussi ton besoin de liberté.""",
        'weekly_advice': {
            'week_1': "Définis l'équilibre entre ouverture et intimité chez toi.",
            'week_2': "Crée de la beauté dans ton espace de vie.",
            'week_3': "Accueille les autres sans te perdre toi-même.",
            'week_4': "Observe comment harmonie et liberté coexistent."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Sanctuaire transformé**

Ta Lune en Sagittaire en Maison 4 cherche un foyer qui permette l'expansion. Ton Ascendant Scorpion ajoute besoin de profondeur et de transformation. Ton chez-toi devient alchimie entre régénération et exploration.

**Domaine activé** : Maison 4 — Tes racines traversent une métamorphose radicale. Tu veux transformer complètement ta relation au foyer, aux origines, à la famille. Ce qui était base devient tremplin vers une renaissance.

**Ton approche instinctive** : Le Scorpion te fait plonger dans les profondeurs de ton histoire familiale. Tu n'as pas peur de regarder les secrets, les traumas, les non-dits. Cette lucidité peut vraiment libérer.

**Tensions possibles** : L'intensité peut rendre le foyer trop lourd. Tu risques de t'obséder sur le passé ou d'alterner entre fusion anxieuse et fuite radicale.

**Conseil clé** : Transformer tes racines en profondeur pour vraiment t'envoler.""",
        'weekly_advice': {
            'week_1': "Regarde en face l'héritage familial que tu portes.",
            'week_2': "Transforme une dynamique familiale toxique.",
            'week_3': "Crée un foyer qui soutient ta régénération.",
            'week_4': "Observe comment tu as métamorphosé tes fondations."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Monde-maison**

Triple Sagittaire sur ton foyer : Lune, Maison 4, Ascendant. L'énergie est pure expansion des racines, le monde entier comme maison. Tu es citoyen·ne du monde, ton chez-toi est partout et nulle part.

**Domaine activé** : Maison 4 — Tes fondations émotionnelles SE TROUVENT dans le mouvement, l'exploration, la découverte. Tu te sens chez toi dans l'inconnu, en sécurité dans l'aventure. Les notions traditionnelles de foyer t'étouffent.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu vis selon une philosophie nomade totale. Tu crois que la vraie sécurité vient de l'adaptabilité, de la foi en l'univers, pas des murs.

**Tensions possibles** : L'absence totale de racines peut créer une instabilité profonde. Tu risques de fuir toute intimité, de confondre liberté et incapacité à t'engager.

**Conseil clé** : Honorer ton nomadisme tout en trouvant des ancrages portables.""",
        'weekly_advice': {
            'week_1': "Explore ce que 'maison' signifie vraiment pour toi.",
            'week_2': "Crée des rituels qui voyagent avec toi.",
            'week_3': "Vérifie que tu ne fuis pas l'intimité par la liberté.",
            'week_4': "Célèbre ta capacité à être chez toi partout."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fondations solides**

Ta Lune en Sagittaire en Maison 4 cherche un foyer qui libère. Ton Ascendant Capricorne ajoute besoin de structure et de durabilité. Tu veux construire des racines solides qui soutiennent ton expansion.

**Domaine activé** : Maison 4 — Ton chez-toi cherche à allier vision et structure. Tu veux créer un patrimoine, des fondations durables qui permettent à toi et aux générations futures d'explorer librement.

**Ton approche instinctive** : Le Capricorne te fait investir patiemment dans ton foyer. Tu construis des bases solides, durables, qui résistent au temps. Cette maturité crée une vraie sécurité.

**Tensions possibles** : Le sérieux peut alourdir ton besoin de liberté. Tu risques de te sentir déchiré·e entre responsabilités familiales et appel de l'aventure.

**Conseil clé** : Construire des racines si solides qu'elles te permettent de t'envoler.""",
        'weekly_advice': {
            'week_1': "Définis un plan à long terme pour ton foyer.",
            'week_2': "Investis dans des fondations durables.",
            'week_3': "Assume tes responsabilités domestiques avec maturité.",
            'week_4': "Célèbre la base solide que tu as construite."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Communauté nomade**

Ta Lune en Sagittaire en Maison 4 cherche un foyer qui libère. Ton Ascendant Verseau ajoute besoin de communauté et d'innovation. Ton chez-toi est une expérimentation collective, un laboratoire de vie.

**Domaine activé** : Maison 4 — Tes racines se trouvent dans l'appartenance à une tribu choisie plutôt que biologique. Tu veux créer des formes de foyer alternatives, des communautés qui libèrent plutôt qu'elles n'enferment.

**Ton approche instinctive** : Le Verseau te fait expérimenter avec les notions de famille et de foyer. Tu cherches des modèles nouveaux, plus libres, plus égalitaires. Cette audace peut vraiment innover.

**Tensions possibles** : L'excès d'idéalisme peut te déconnecter de tes besoins affectifs réels. Tu risques de fuir l'intimité par l'intellectualisation ou de rejeter tout attachement par peur de perdre ta liberté.

**Conseil clé** : Innover dans tes formes de foyer tout en honorant tes besoins humains.""",
        'weekly_advice': {
            'week_1': "Explore des formes alternatives de foyer et de famille.",
            'week_2': "Connecte-toi à une communauté qui partage tes valeurs.",
            'week_3': "Expérimente avec de nouvelles façons d'habiter.",
            'week_4': "Observe si tes innovations te nourrissent vraiment."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Temple fluide**

Ta Lune en Sagittaire en Maison 4 cherche un foyer qui nourrit l'esprit. Ton Ascendant Poissons ajoute dimension spirituelle et fluidité. Ton chez-toi devient sanctuaire mystique, espace de dissolution des frontières.

**Domaine activé** : Maison 4 — Tes racines cherchent la transcendance. Tu veux un foyer qui soit à la fois ancrage dans le sacré et dissolution de l'ego. L'espace de vie devient pratique spirituelle.

**Ton approche instinctive** : Le Poissons te fait créer un foyer intuitif, inspiré, peut-être un peu chaotique. Tu ressens l'énergie des lieux. Cette sensibilité peut créer des espaces magiques.

**Tensions possibles** : Le manque de structure peut créer le chaos domestique. Tu risques de fuir toute organisation par le spirituel, de confondre dissolution et désordre.

**Conseil clé** : Créer un foyer spirituel tout en maintenant un minimum d'ancrage terrestre.""",
        'weekly_advice': {
            'week_1': "Médite sur l'énergie que tu veux dans ton espace.",
            'week_2': "Crée un sanctuaire spirituel chez toi.",
            'week_3': "Vérifie que ta fluidité n'est pas du chaos déguisé.",
            'week_4': "Ancre tes insights sur le foyer dans des pratiques concrètes."
        }
    },

    # ==================== MAISON 5 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Joie conquérante**

Ta Lune en Sagittaire active la Maison 5 : ta créativité et ton plaisir cherchent l'expansion. Avec l'Ascendant Bélier, tu veux vivre intensément, créer audacieusement, jouer avec le feu de la vie.

**Domaine activé** : Maison 5 — Ta créativité, tes amours, tes plaisirs demandent de l'espace et de l'aventure. Tu veux t'exprimer sans limites, aimer avec passion, vivre chaque moment comme une célébration. L'authenticité créative t'anime.

**Ton approche instinctive** : Le Bélier te fait créer avec courage et spontanéité. Tu fonçes vers ce qui t'excite, tu risques ton cœur, tu vis pleinement. Cette audace créative peut vraiment changer la donne.

**Tensions possibles** : L'excès d'impulsivité peut créer du chaos créatif ou affectif. Tu risques de brûler trop vite, de te disperser, de confondre intensité et profondeur.

**Conseil clé** : Canaliser ton énergie créative vers des projets qui ont vraiment du sens.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans un projet créatif qui t'inspire vraiment.",
            'week_2': "Prends des risques dans l'expression de qui tu es.",
            'week_3': "Vis tes passions avec intensité et authenticité.",
            'week_4': "Célèbre la joie que tu as créée et partagée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Plaisir sensuel**

Ta Lune en Sagittaire en Maison 5 cherche la joie expansive. Ton Ascendant Taureau ajoute dimension sensuelle et goût du beau. Tu veux créer et aimer de manière qui nourrit tous tes sens.

**Domaine activé** : Maison 5 — Ta créativité cherche à s'incarner dans la matière. Tu veux des plaisirs tangibles, des amours qui se vivent dans le corps, des créations belles et durables. L'art de vivre bien t'occupe.

**Ton approche instinctive** : Le Taureau te fait savourer chaque moment créatif. Tu prends ton temps, tu apprécies la qualité, tu construis ta joie lentement. Cette approche crée des œuvres et des amours solides.

**Tensions possibles** : La tension entre exploration (Sagittaire) et confort (Taureau) peut créer de l'hésitation. Tu risques de retenir ta créativité par prudence ou de t'accrocher à des plaisirs qui ne t'élèvent plus.

**Conseil clé** : Créer et aimer de manière qui nourrit vraiment, pas juste qui distrait.""",
        'weekly_advice': {
            'week_1': "Définis ce qui te donne vraiment du plaisir profond.",
            'week_2': "Crée quelque chose de beau avec tes mains.",
            'week_3': "Savoure les plaisirs sensuels sans culpabilité.",
            'week_4': "Apprécie la qualité de vie que tu as cultivée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Jeu intellectuel**

Ta Lune en Sagittaire en Maison 5 cherche la joie dans l'expression. Ton Ascendant Gémeaux ajoute dimension ludique et mentale. Tu veux créer par les mots, jouer avec les idées, communiquer ta joie.

**Domaine activé** : Maison 5 — Ta créativité est intellectuelle et communicative. Tu t'exprimes par l'écriture, la conversation, l'humour. Tes amours passent par le partage d'idées. Le jeu mental te nourrit.

**Ton approche instinctive** : Le Gémeaux te fait créer avec légèreté et variété. Tu explores différentes formes d'expression, tu expérimentes, tu t'amuses avec les concepts. Cette agilité créative est rafraîchissante.

**Tensions possibles** : La dispersion peut t'empêcher de finir tes créations. Tu risques de papillonner entre projets, de confondre amusement et superficialité, de fuir la profondeur par le jeu.

**Conseil clé** : Jouer sérieusement — s'amuser tout en créant quelque chose de significatif.""",
        'weekly_advice': {
            'week_1': "Expérimente avec plusieurs formes créatives.",
            'week_2': "Crée du contenu qui amuse et inspire.",
            'week_3': "Joue avec les idées sans te disperser.",
            'week_4': "Synthétise tes explorations en une création cohérente."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Créativité nourrissante**

Ta Lune en Sagittaire en Maison 5 cherche la joie expansive. Ton Ascendant Cancer ajoute profondeur émotionnelle et besoin de connexion. Tu veux créer ce qui touche le cœur, aimer en nourrissant l'âme.

**Domaine activé** : Maison 5 — Ta créativité cherche à créer du lien et de la sécurité affective. Tu t'exprimes à travers l'art qui émeut, les amours qui nourrissent, les plaisirs qui réconfortent. La famille créative t'attire.

**Ton approche instinctive** : Le Cancer te fait créer avec sensibilité et générosité. Tu veux que ton art prenne soin des autres, que tes amours créent un nid. Cette approche nourricière enrichit ta joie.

**Tensions possibles** : La peur de blesser peut freiner ton expression. Tu risques d'adapter ta créativité au point de perdre ton authenticité, ou de t'accrocher à des amours qui ne te font plus grandir.

**Conseil clé** : Créer et aimer de manière qui nourrit sans étouffer.""",
        'weekly_advice': {
            'week_1': "Définis ce qui nourrit vraiment ton âme créative.",
            'week_2': "Crée quelque chose qui touche émotionnellement.",
            'week_3': "Aime en restant ouvert·e à l'exploration.",
            'week_4': "Observe comment tu as nourri et été nourri·e."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Génie créatif**

Double feu sur la Maison 5 : ta Lune en Sagittaire et ton Ascendant Lion, maître naturel de cette maison, créent une puissance créative rare. Tu veux briller, créer, aimer avec grandeur et authenticité totale.

**Domaine activé** : Maison 5 — Ta créativité est au maximum de sa puissance. Tu veux t'exprimer de manière unique, inoubliable, inspirante. Tes amours sont passionnées, tes plaisirs nobles. L'art de vivre en grand te définit.

**Ton approche instinctive** : Le Lion te fait créer avec fierté et générosité. Tu ne te contentes pas d'exister, tu veux laisser une empreinte créative. Cette audace peut vraiment marquer le monde.

**Tensions possibles** : L'excès d'ego peut transformer la créativité en performance narcissique. Tu risques de créer pour l'admiration plutôt que pour l'expression, d'aimer pour briller plutôt que pour partager.

**Conseil clé** : Créer et aimer depuis ton cœur véritable, pas depuis ton besoin d'attention.""",
        'weekly_advice': {
            'week_1': "Exprime ton génie créatif unique sans retenue.",
            'week_2': "Aime avec la noblesse et la passion que tu mérites.",
            'week_3': "Partage ta créativité généreusement.",
            'week_4': "Célèbre l'œuvre et l'amour que tu as créés."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Art utile**

Ta Lune en Sagittaire en Maison 5 cherche la joie créative expansive. Ton Ascendant Vierge ajoute discernement et souci du détail. Tu veux créer ce qui est à la fois beau et utile, aimer de manière qui améliore.

**Domaine activé** : Maison 5 — Ta créativité cherche à allier inspiration et perfection technique. Tu veux que ton art serve à quelque chose, que tes amours soient saines, que tes plaisirs contribuent à ton bien-être.

**Ton approche instinctive** : La Vierge te fait affiner tes créations. Tu travailles les détails, tu améliores, tu perfectionnes. Cette rigueur peut vraiment élever la qualité de ton expression.

**Tensions possibles** : L'analyse excessive peut tuer la spontanéité créative. Tu risques de critiquer tes œuvres avant même de les terminer, de te perdre dans les détails, de juger ta joie au lieu de la vivre.

**Conseil clé** : Utiliser ton discernement pour perfectionner, pas pour paralyser.""",
        'weekly_advice': {
            'week_1': "Examine ce qui bloque ton expression créative.",
            'week_2': "Crée quelque chose d'utile ET de beau.",
            'week_3': "Affine tes créations sans perdre ta spontanéité.",
            'week_4': "Savoure l'excellence de ce que tu as créé."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Beauté partagée**

Ta Lune en Sagittaire en Maison 5 cherche la joie expansive. Ton Ascendant Balance ajoute sens esthétique et besoin de partage. Tu veux créer ce qui est beau, aimer avec harmonie, partager tes plaisirs.

**Domaine activé** : Maison 5 — Ta créativité cherche l'équilibre et la beauté. Tu t'exprimes à travers l'art raffiné, les relations amoureuses équilibrées, les plaisirs partagés. L'esthétique relationnelle te passionne.

**Ton approche instinctive** : La Balance te fait créer avec grâce et diplomatie. Tu veux que ton art soit accessible, que tes amours soient harmonieuses. Cette approche collaborative enrichit ta créativité.

**Tensions possibles** : Le besoin d'harmonie peut diluer ton authenticité. Tu risques d'adapter ta créativité pour plaire, de sacrifier ta vision pour la paix, de confondre équilibre et compromission.

**Conseil clé** : Créer et aimer avec harmonie tout en restant fidèle à ta vision.""",
        'weekly_advice': {
            'week_1': "Définis l'équilibre entre authenticité et harmonie.",
            'week_2': "Crée quelque chose de beau avec d'autres.",
            'week_3': "Aime de manière qui honore l'autre et toi-même.",
            'week_4': "Observe comment tu as créé de la beauté partagée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Passion transformée**

Ta Lune en Sagittaire en Maison 5 cherche la joie et l'expression. Ton Ascendant Scorpion ajoute intensité et profondeur. Tu veux créer ce qui transforme, aimer avec une passion qui régénère.

**Domaine activé** : Maison 5 — Ta créativité puise dans les profondeurs de l'âme. Tu t'exprimes à travers l'art cathartique, les amours transformatrices, les plaisirs qui touchent l'essence. Rien de superficiel ne t'intéresse.

**Ton approche instinctive** : Le Scorpion te fait créer avec intensité totale. Tu plonges dans tes zones d'ombre pour en extraire de l'or créatif. Cette profondeur donne un pouvoir réel à ton art.

**Tensions possibles** : L'obsession peut devenir destructrice. Tu risques de brûler dans ta passion créative ou amoureuse, de confondre intensité et toxicité, de vouloir tout contrôler.

**Conseil clé** : Vivre ta passion créative en profondeur tout en gardant la foi en la lumière.""",
        'weekly_advice': {
            'week_1': "Plonge dans tes profondeurs pour créer authentiquement.",
            'week_2': "Transforme une douleur en expression créative.",
            'week_3': "Aime avec intensité mais sans possession.",
            'week_4': "Observe comment tu as alchimisé ta passion."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Joie pure**

Triple Sagittaire sur ta créativité : Lune, Maison 5, Ascendant. L'énergie est pure célébration de la vie, expression joyeuse, amour libre. Tu ES la joie incarnée, le créateur·rice qui célèbre l'existence.

**Domaine activé** : Maison 5 — Ta créativité et tes amours sont terrain d'expansion illimitée. Tu veux créer ce qui inspire, aimer librement, vivre chaque plaisir comme une aventure. La vie est un terrain de jeu philosophique.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu crées et aimes avec optimisme total. Tu crois en la joie comme chemin spirituel. Cette foi rend ton expression magnétique.

**Tensions possibles** : L'excès d'optimisme peut créer de l'irresponsabilité créative ou affective. Tu risques de fuir la profondeur par le plaisir, de papillonner sans jamais t'engager vraiment.

**Conseil clé** : Vivre ta joie expansive tout en acceptant que la vraie création demande de la constance.""",
        'weekly_advice': {
            'week_1': "Crée et aime avec la joie et la liberté qui te définissent.",
            'week_2': "Explore de nouvelles formes d'expression créative.",
            'week_3': "Vérifie que tu ne fuis pas par le plaisir.",
            'week_4': "Célèbre la vie avec gratitude et générosité."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Génie discipliné**

Ta Lune en Sagittaire en Maison 5 cherche la joie créative. Ton Ascendant Capricorne ajoute discipline et ambition. Tu veux créer des œuvres durables, construire ta réputation créative patiemment.

**Domaine activé** : Maison 5 — Ta créativité cherche à allier inspiration et excellence professionnelle. Tu veux que ton art soit reconnu, que tes créations résistent au temps. Le travail créatif sérieux t'attire.

**Ton approche instinctive** : Le Capricorne te fait créer avec méthode et persévérance. Tu es prêt·e à faire le travail dur pour maîtriser ton art. Cette discipline peut vraiment mener à la virtuosité.

**Tensions possibles** : Le sérieux peut étouffer ta spontanéité créative. Tu risques de te sentir déchiré·e entre inspiration libre et contraintes professionnelles, entre joie et ambition.

**Conseil clé** : Construire ton excellence créative sans perdre ta joie de créer.""",
        'weekly_advice': {
            'week_1': "Définis un objectif créatif ambitieux mais inspirant.",
            'week_2': "Mets en place une discipline qui soutient ton art.",
            'week_3': "Travaille dur tout en gardant le plaisir de créer.",
            'week_4': "Célèbre le progrès concret de ton excellence."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Art révolutionnaire**

Ta Lune en Sagittaire en Maison 5 cherche l'expression créative. Ton Ascendant Verseau ajoute originalité et conscience sociale. Tu veux créer ce qui libère, aimer de manière qui révolutionne.

**Domaine activé** : Maison 5 — Ta créativité cherche à innover et à servir le collectif. Tu t'exprimes à travers l'art avant-gardiste, les amours non-conventionnelles, les plaisirs qui élèvent la conscience.

**Ton approche instinctive** : Le Verseau te fait créer en brisant les conventions. Tu explores des territoires créatifs vierges, tu expérimentes sans peur du jugement. Cette audace peut vraiment innover.

**Tensions possibles** : L'excès d'intellectualisation peut te déconnecter de ta joie spontanée. Tu risques de créer pour le concept plutôt que pour l'expression, de rejeter l'amour par peur de perdre ta liberté.

**Conseil clé** : Révolutionner ton expression tout en restant connecté·e à ton cœur.""",
        'weekly_advice': {
            'week_1': "Explore des formes créatives vraiment nouvelles.",
            'week_2': "Crée de l'art qui sert une vision collective.",
            'week_3': "Aime de manière libre mais vraie.",
            'week_4': "Observe comment ton originalité a inspiré."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Art mystique**

Ta Lune en Sagittaire en Maison 5 cherche l'expression joyeuse. Ton Ascendant Poissons ajoute dimension spirituelle et créativité intuitive. Tu veux créer ce qui transcende, aimer avec une dévotion mystique.

**Domaine activé** : Maison 5 — Ta créativité est canalisée depuis des plans supérieurs. Tu t'exprimes à travers l'art visionnaire, les amours spirituelles, les plaisirs qui nourrissent l'âme. La création est prière.

**Ton approche instinctive** : Le Poissons te fait créer par inspiration pure. Tu laisses le flot créatif passer à travers toi. Cette perméabilité peut créer des œuvres vraiment touchantes.

**Tensions possibles** : Le manque de structure peut disperser ton génie. Tu risques de confondre inspiration et illusion, de fuir la discipline créative par le spirituel.

**Conseil clé** : Honorer ton inspiration mystique tout en donnant forme concrète à ta vision.""",
        'weekly_advice': {
            'week_1': "Laisse l'inspiration couler sans censure.",
            'week_2': "Crée quelque chose qui touche l'âme.",
            'week_3': "Ancre tes visions dans des œuvres concrètes.",
            'week_4': "Partage ta créativité mystique avec le monde."
        }
    },

    # ==================== MAISON 6 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Service guerrier**

Ta Lune en Sagittaire active la Maison 6 : ton travail et ta santé cherchent le sens. Avec l'Ascendant Bélier, tu veux servir avec courage, travailler sur ce qui compte vraiment, défendre une cause.

**Domaine activé** : Maison 6 — Ton quotidien, ton service, ta santé demandent de l'inspiration et de l'action. Tu veux un travail qui ait un impact, des routines qui te font grandir. La quête de sens guide tes efforts.

**Ton approche instinctive** : Le Bélier te fait agir rapidement sur ce qui t'inspire. Tu veux révolutionner tes habitudes, combattre pour améliorer les systèmes. Cette audace peut vraiment transformer ton quotidien.

**Tensions possibles** : L'impulsivité peut créer de l'instabilité dans tes routines. Tu risques de te lancer dans mille projets sans finir, de brûler ton énergie par excès d'enthousiasme.

**Conseil clé** : Canaliser ton énergie vers un service qui a vraiment du sens pour toi.""",
        'weekly_advice': {
            'week_1': "Définis une cause à servir qui t'inspire vraiment.",
            'week_2': "Agis courageusement pour améliorer ton quotidien.",
            'week_3': "Prends soin de ton corps avec la même passion.",
            'week_4': "Célèbre l'impact de ton service inspiré."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Travail ancré**

Ta Lune en Sagittaire en Maison 6 cherche le sens dans le service. Ton Ascendant Taureau ajoute constance et ancrage physique. Tu veux un travail qui nourrit ton corps autant que ton esprit.

**Domaine activé** : Maison 6 — Ton quotidien cherche à allier grande vision et concrétude. Tu veux servir de manière tangible, créer des routines saines qui durent, travailler avec tes mains sur des projets inspirants.

**Ton approche instinctive** : Le Taureau te fait construire tes habitudes lentement. Tu veux que ton travail soit solide, tes routines agréables, ta santé vraiment robuste. Cette approche crée une discipline durable.

**Tensions possibles** : La tension entre vision expansive et réalisme peut créer de la frustration. Tu risques de retenir ton ambition par prudence ou de t'enliser dans des routines qui ne t'inspirent plus.

**Conseil clé** : Servir de manière stable tout en gardant ton besoin de croissance.""",
        'weekly_advice': {
            'week_1': "Définis un travail inspirant ET viable.",
            'week_2': "Crée des routines qui nourrissent ton corps et ton esprit.",
            'week_3': "Sers avec constance et qualité.",
            'week_4': "Savoure la santé et la stabilité que tu as construites."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Service multiple**

Ta Lune en Sagittaire en Maison 6 cherche le sens dans le quotidien. Ton Ascendant Gémeaux ajoute variété et agilité. Tu veux un travail intellectuellement stimulant, des routines flexibles, servir par la communication.

**Domaine activé** : Maison 6 — Ton service se fait par les mots et les connexions. Tu veux un travail varié, des habitudes qui s'adaptent, une santé qui passe par l'équilibre mental. La diversité te garde motivé·e.

**Ton approche instinctive** : Le Gémeaux te fait explorer différentes façons de servir. Tu apprends constamment, tu adaptes tes méthodes, tu communiques ta vision. Cette agilité rend ton travail vivant.

**Tensions possibles** : La dispersion peut t'empêcher de vraiment exceller. Tu risques de papillonner entre tâches sans jamais approfondir, de confondre activité et service efficace.

**Conseil clé** : Diversifier intelligemment ton service sans te disperser.""",
        'weekly_advice': {
            'week_1': "Explore différentes façons de servir.",
            'week_2': "Apprends des compétences qui élargissent ton impact.",
            'week_3': "Crée des routines flexibles mais efficaces.",
            'week_4': "Synthétise tes multiples activités en service cohérent."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Soin inspiré**

Ta Lune en Sagittaire en Maison 6 cherche le sens dans le service. Ton Ascendant Cancer ajoute empathie et besoin de nourrir. Tu veux servir en prenant soin, travailler dans un environnement qui te sécurise émotionnellement.

**Domaine activé** : Maison 6 — Ton service passe par le soin des autres et de toi-même. Tu veux un travail qui nourrit l'âme, des routines qui créent de la sécurité, une santé qui honore tes besoins émotionnels.

**Ton approche instinctive** : Le Cancer te fait servir avec sensibilité et dévouement. Tu crées un environnement de travail chaleureux, tu prends soin de tes collègues. Cette approche nourricière enrichit ton service.

**Tensions possibles** : La peur de l'inconnu peut limiter ton expansion professionnelle. Tu risques de te surinvestir émotionnellement dans ton travail ou de confondre soin et surprotection.

**Conseil clé** : Servir en prenant soin tout en te donnant la liberté de grandir.""",
        'weekly_advice': {
            'week_1': "Définis un service qui nourrit ton âme.",
            'week_2': "Crée un environnement de travail sécurisant.",
            'week_3': "Prends soin de ta santé émotionnelle autant que physique.",
            'week_4': "Observe comment tu as nourri et été nourri·e."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Service noble**

Double feu sur la Maison 6 : ta Lune en Sagittaire et ton Ascendant Lion créent un service généreux et inspirant. Tu veux travailler avec fierté, servir avec grandeur, briller par ton dévouement.

**Domaine activé** : Maison 6 — Ton travail cherche à exprimer ta noblesse. Tu veux servir de manière qui inspire les autres, créer des routines dignes de ton excellence, maintenir une santé rayonnante.

**Ton approche instinctive** : Le Lion te fait servir avec générosité et créativité. Tu ne te contentes pas de faire ton travail, tu veux laisser une empreinte. Cette approche donne du sens au quotidien.

**Tensions possibles** : L'ego peut transformer le service en performance. Tu risques de vouloir briller plus que servir vraiment, de mépriser les tâches humbles mais nécessaires.

**Conseil clé** : Servir avec noblesse tout en restant humble et efficace.""",
        'weekly_advice': {
            'week_1': "Exprime ta vision à travers ton travail quotidien.",
            'week_2': "Sers avec générosité et créativité.",
            'week_3': "Inspire par l'exemple de ton dévouement.",
            'week_4': "Célèbre l'impact noble de ton service."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfection utile**

Ta Lune en Sagittaire en Maison 6 cherche le sens dans le service. Ton Ascendant Vierge, maître naturel de cette maison, ajoute discernement et excellence. Tu veux servir avec compétence, améliorer constamment.

**Domaine activé** : Maison 6 — Ton service cherche à allier grande vision et perfection technique. Tu veux être vraiment utile, exceller dans ton domaine, créer des systèmes qui fonctionnent parfaitement.

**Ton approche instinctive** : La Vierge te fait servir avec attention aux détails. Tu analyses, tu optimises, tu perfectionnes. Cette rigueur peut vraiment élever la qualité de ton travail.

**Tensions possibles** : L'excès d'analyse peut paralyser ton action. Tu risques de te perdre dans les détails, de critiquer sans cesse ton travail, de viser une perfection impossible.

**Conseil clé** : Utiliser ton discernement pour améliorer, pas pour te bloquer ou t'épuiser.""",
        'weekly_advice': {
            'week_1': "Examine tes méthodes de travail avec honnêteté.",
            'week_2': "Optimise tes systèmes pour plus d'efficacité.",
            'week_3': "Sers avec excellence sans perfectionnisme paralysant.",
            'week_4': "Observe comment tu as amélioré ton service."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Service équilibré**

Ta Lune en Sagittaire en Maison 6 cherche le sens dans le quotidien. Ton Ascendant Balance ajoute sens de l'équilibre et besoin de justice. Tu veux servir équitablement, travailler en harmonie avec les autres.

**Domaine activé** : Maison 6 — Ton travail cherche à créer de la justice et de l'harmonie. Tu veux un service qui soit beau, équitable, collaboratif. L'équilibre travail-vie te préoccupe.

**Ton approche instinctive** : La Balance te fait servir avec diplomatie et sens de la justice. Tu crées des conditions de travail harmonieuses, tu médies les conflits. Cette approche améliore l'environnement pour tous.

**Tensions possibles** : Le besoin d'harmonie peut t'empêcher de dire non. Tu risques de te surinvestir pour maintenir la paix, de sacrifier ton bien-être pour l'équité apparente.

**Conseil clé** : Servir avec équilibre tout en honorant tes propres besoins.""",
        'weekly_advice': {
            'week_1': "Définis l'équilibre entre service et soin de soi.",
            'week_2': "Crée de l'harmonie dans ton environnement de travail.",
            'week_3': "Sers avec justice sans te sacrifier.",
            'week_4': "Observe comment tu as créé de l'équilibre."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Service transformé**

Ta Lune en Sagittaire en Maison 6 cherche le sens dans le travail. Ton Ascendant Scorpion ajoute intensité et besoin de transformation. Tu veux un service qui transforme vraiment, qui touche les profondeurs.

**Domaine activé** : Maison 6 — Ton travail devient outil de métamorphose personnelle et collective. Tu veux servir en allant au fond des problèmes, créer des changements radicaux, guérir en profondeur.

**Ton approche instinctive** : Le Scorpion te fait servir avec intensité totale. Tu n'as pas peur des situations difficiles, tu plonges dans ce que les autres évitent. Cette profondeur crée un service vraiment puissant.

**Tensions possibles** : L'obsession peut créer l'épuisement. Tu risques de te surcharger par besoin de contrôle, de ne pas savoir lâcher le travail, de confondre dévouement et compulsion.

**Conseil clé** : Transformer par ton service tout en préservant ton énergie vitale.""",
        'weekly_advice': {
            'week_1': "Plonge dans un travail qui transforme vraiment.",
            'week_2': "Élimine les habitudes de travail toxiques.",
            'week_3': "Sers avec intensité mais pose des limites.",
            'week_4': "Observe comment ton service t'a transformé·e."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Mission incarnée**

Triple Sagittaire sur ton travail : Lune, Maison 6, Ascendant. L'énergie est pure quête de sens dans le service. Tu ne veux pas juste un job, tu veux une mission qui change le monde.

**Domaine activé** : Maison 6 — Ton quotidien DOIT avoir du sens. Tu veux servir une cause qui te dépasse, travailler sur des projets qui inspirent, créer des routines qui te font grandir. Le travail insignifiant t'est insupportable.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu sers avec foi et enthousiasme. Tu crois que ton travail peut changer les choses. Cette conviction rend ton service vraiment impactant.

**Tensions possibles** : L'excès d'idéalisme peut te rendre insatisfait·e. Tu risques de fuir tout travail qui ne correspond pas à 100% à ta vision, de négliger les aspects pratiques du service.

**Conseil clé** : Trouver le sens dans le service tout en acceptant les aspects prosaïques.""",
        'weekly_advice': {
            'week_1': "Définis clairement ta mission de vie et de service.",
            'week_2': "Aligne ton travail quotidien avec ta vision.",
            'week_3': "Accepte que le sens se trouve aussi dans les petites tâches.",
            'week_4': "Célèbre l'impact de ton service inspiré."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Maîtrise construite**

Ta Lune en Sagittaire en Maison 6 cherche le sens dans le travail. Ton Ascendant Capricorne ajoute ambition et discipline. Tu veux devenir maître dans ton domaine, construire une réputation d'excellence.

**Domaine activé** : Maison 6 — Ton service cherche à allier vision et professionnalisme. Tu veux exceller dans un domaine inspirant, créer une expertise reconnue, servir avec autorité et compétence.

**Ton approche instinctive** : Le Capricorne te fait grimper patiemment vers la maîtrise. Tu es prêt·e à faire le travail dur, à perfectionner ton art sur le long terme. Cette discipline crée une vraie excellence.

**Tensions possibles** : Le sérieux peut étouffer ton enthousiasme. Tu risques de te sentir déchiré·e entre inspiration libre et contraintes professionnelles, entre mission et carrière.

**Conseil clé** : Construire ton expertise tout en gardant la flamme de ton inspiration.""",
        'weekly_advice': {
            'week_1': "Définis un plan à long terme pour ton excellence.",
            'week_2': "Travaille avec discipline sur ta maîtrise.",
            'week_3': "Sers avec autorité et humilité.",
            'week_4': "Célèbre les fondations de ton expertise."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Service révolutionnaire**

Ta Lune en Sagittaire en Maison 6 cherche le sens dans le quotidien. Ton Ascendant Verseau ajoute innovation et conscience collective. Tu veux révolutionner les systèmes de travail, servir le futur.

**Domaine activé** : Maison 6 — Ton service cherche à innover et à libérer. Tu veux travailler sur des projets avant-gardistes, créer des méthodes nouvelles, servir l'évolution collective. Le travail conventionnel t'étouffe.

**Ton approche instinctive** : Le Verseau te fait expérimenter avec de nouvelles façons de servir. Tu brises les conventions, tu proposes des alternatives. Cette audace peut vraiment faire évoluer ton domaine.

**Tensions possibles** : L'excès d'originalité peut te déconnecter de l'efficacité réelle. Tu risques de rejeter toute routine par principe, de devenir dogmatique sur ton progressisme.

**Conseil clé** : Révolutionner ton service tout en restant vraiment utile.""",
        'weekly_advice': {
            'week_1': "Explore des méthodes de travail innovantes.",
            'week_2': "Connecte-toi à des réseaux qui changent les paradigmes.",
            'week_3': "Sers le collectif de manière avant-gardiste.",
            'week_4': "Observe comment ton innovation a créé de l'impact."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Service spirituel**

Ta Lune en Sagittaire en Maison 6 cherche le sens dans le travail. Ton Ascendant Poissons ajoute dimension spirituelle et compassion universelle. Tu veux servir avec dévotion, guérir par ta présence.

**Domaine activé** : Maison 6 — Ton service devient pratique spirituelle. Tu veux travailler sur ce qui nourrit l'âme, servir avec compassion totale, créer de la guérison. Le travail purement matériel ne suffit pas.

**Ton approche instinctive** : Le Poissons te fait servir par intuition et empathie. Tu ressens les besoins avant qu'ils ne soient exprimés. Cette sensibilité crée un service vraiment touchant.

**Tensions possibles** : Le manque de limites peut créer l'épuisement compassionnel. Tu risques de te dissoudre dans le service, de fuir tes responsabilités pratiques par le spirituel.

**Conseil clé** : Servir avec dévotion tout en maintenant des limites saines.""",
        'weekly_advice': {
            'week_1': "Médite sur ta vocation de service.",
            'week_2': "Sers avec compassion mais pose des limites claires.",
            'week_3': "Ancre ta spiritualité dans un service concret.",
            'week_4': "Observe comment tu as servi et pris soin de toi."
        }
    },

    # ==================== MAISON 7 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Partenariat libre**

Ta Lune en Sagittaire active la Maison 7 : tes relations cherchent l'expansion. Avec l'Ascendant Bélier, tu veux des partenariats qui te défient, des relations qui respectent ta liberté totale.

**Domaine activé** : Maison 7 — Tes partenariats intimes et professionnels demandent de l'espace et de l'aventure. Tu veux des relations qui te font grandir, qui sont basées sur la vérité mutuelle et le respect de l'indépendance.

**Ton approche instinctive** : Le Bélier te fait aborder les relations avec audace et franchise. Tu veux des partenaires qui n'ont pas peur de ta force. Cette authenticité crée des liens puissants ou des conflits nets.

**Tensions possibles** : L'excès d'indépendance peut empêcher la vraie intimité. Tu risques de fuir dès que ça devient profond, de confondre liberté et incapacité à t'engager.

**Conseil clé** : Créer des partenariats qui honorent la liberté ET l'engagement.""",
        'weekly_advice': {
            'week_1': "Définis ce que liberté signifie dans tes relations.",
            'week_2': "Ose être vulnérable tout en restant authentique.",
            'week_3': "Crée des accords clairs qui respectent l'autonomie mutuelle.",
            'week_4': "Célèbre les partenariats qui te font grandir."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Engagement stable**

Ta Lune en Sagittaire en Maison 7 cherche l'expansion par les relations. Ton Ascendant Taureau ajoute besoin de sécurité et de constance. Tu veux des partenariats qui allient liberté et stabilité.

**Domaine activé** : Maison 7 — Tes relations cherchent à être à la fois inspirantes et durables. Tu veux un·e partenaire qui t'encourage à explorer tout en créant une base solide. La fidélité évolutive t'attire.

**Ton approche instinctive** : Le Taureau te fait construire tes relations lentement. Tu veux de la profondeur, de la sensualité, de la constance. Cette approche crée des partenariats vraiment enracinés.

**Tensions possibles** : La tension entre exploration (Sagittaire) et sécurité (Taureau) peut créer des conflits. Tu risques d'alterner entre besoin de nouveauté et peur du changement.

**Conseil clé** : Créer des partenariats stables qui permettent la croissance mutuelle.""",
        'weekly_advice': {
            'week_1': "Définis l'équilibre entre stabilité et aventure.",
            'week_2': "Construis la confiance qui permet l'exploration.",
            'week_3': "Nourris tes relations avec constance et présence.",
            'week_4': "Savoure les partenariats qui sont à la fois sûrs et vivants."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Dialogue expansif**

Ta Lune en Sagittaire en Maison 7 cherche des relations qui inspirent. Ton Ascendant Gémeaux, en opposition à cette maison, crée une tension créative. Tu veux des partenaires qui stimulent ton esprit et élargissent ta vision.

**Domaine activé** : Maison 7 — Tes relations sont basées sur l'échange intellectuel et la découverte mutuelle. Tu veux des partenaires curieux, avec qui tu peux explorer des idées infiniment. La conversation est ta forme d'intimité.

**Ton approche instinctive** : Le Gémeaux te fait chercher la variété et la stimulation mentale. Tu veux des relations légères mais profondes, multiples mais sincères. Cette complexité enrichit tes partenariats.

**Tensions possibles** : La peur de l'ennui peut t'empêcher de vraiment t'engager. Tu risques de papillonner relationnellement, de fuir dès que ça devient prévisible.

**Conseil clé** : Créer des partenariats intellectuellement stimulants qui acceptent aussi la profondeur émotionnelle.""",
        'weekly_advice': {
            'week_1': "Engage des conversations qui élargissent ta vision.",
            'week_2': "Cherche des partenaires qui stimulent ton esprit.",
            'week_3': "Accepte que la vraie intimité demande aussi du silence.",
            'week_4': "Observe comment tu as équilibré légèreté et profondeur."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Foyer à deux**

Ta Lune en Sagittaire en Maison 7 cherche l'expansion par les relations. Ton Ascendant Cancer ajoute besoin de sécurité émotionnelle et de famille. Tu veux un·e partenaire qui soit à la fois aventurier·ère et nid.

**Domaine activé** : Maison 7 — Tes relations oscillent entre besoin de fusion et besoin de liberté. Tu veux créer une famille choisie qui explore le monde ensemble. Le partenaire devient base émotionnelle pour l'aventure.

**Ton approche instinctive** : Le Cancer te fait nourrir tes relations avec dévotion. Tu crées de la sécurité émotionnelle pour ton·ta partenaire. Cette sensibilité crée des liens profonds.

**Tensions possibles** : La peur de perdre peut freiner ton besoin d'exploration. Tu risques d'alterner entre accrochage anxieux et fuite émotionnelle déguisée en liberté.

**Conseil clé** : Créer des partenariats qui nourrissent tout en libérant.""",
        'weekly_advice': {
            'week_1': "Définis ce qui te fait sentir en sécurité dans les relations.",
            'week_2': "Crée un espace émotionnel sûr pour toi et ton·ta partenaire.",
            'week_3': "Explore ensemble tout en maintenant la connexion affective.",
            'week_4': "Observe comment intimité et liberté se sont réconciliées."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Amour royal**

Double feu sur la Maison 7 : ta Lune en Sagittaire et ton Ascendant Lion créent des relations passionnées et généreuses. Tu veux un·e partenaire qui brille avec toi, qui célèbre la grandeur de l'amour.

**Domaine activé** : Maison 7 — Tes partenariats cherchent à être nobles et inspirants. Tu veux vivre un grand amour, créer avec ton·ta partenaire, être vu·e et admiré·e dans la relation. La médiocrité relationnelle t'est intolérable.

**Ton approche instinctive** : Le Lion te fait aimer avec fierté et générosité. Tu veux un·e partenaire qui soit à ta hauteur, qui ne diminue pas ta lumière. Cette grandeur crée des relations mémorables.

**Tensions possibles** : L'ego peut transformer l'amour en compétition. Tu risques de vouloir briller plus que ton·ta partenaire, de confondre amour et admiration.

**Conseil clé** : Créer des partenariats où vous brillez ensemble, pas l'un contre l'autre.""",
        'weekly_advice': {
            'week_1': "Exprime ta vision d'un grand amour.",
            'week_2': "Crée avec ton·ta partenaire quelque chose de noble.",
            'week_3': "Célèbre la grandeur de l'autre autant que la tienne.",
            'week_4': "Observe comment vous vous êtes élevé·es mutuellement."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Partenariat perfectionné**

Ta Lune en Sagittaire en Maison 7 cherche l'expansion par les relations. Ton Ascendant Vierge ajoute discernement et besoin d'amélioration. Tu veux des partenariats qui fonctionnent vraiment bien, qui se bonifient constamment.

**Domaine activé** : Maison 7 — Tes relations cherchent à allier grande vision et efficacité pratique. Tu veux un·e partenaire compétent·e avec qui tu peux co-créer, quelqu'un qui t'aide à t'améliorer et que tu aides en retour.

**Ton approche instinctive** : La Vierge te fait analyser tes relations. Tu vois ce qui fonctionne et ce qui doit s'améliorer. Cette lucidité peut vraiment élever la qualité de tes partenariats.

**Tensions possibles** : L'excès de critique peut empoisonner l'amour. Tu risques de te focaliser sur les défauts au lieu de célébrer les qualités, de vouloir perfectionner l'autre au lieu de l'accepter.

**Conseil clé** : Améliorer tes relations tout en acceptant l'imperfection humaine.""",
        'weekly_advice': {
            'week_1': "Examine honnêtement ce qui fonctionne dans tes relations.",
            'week_2': "Améliore tes patterns relationnels sans juger.",
            'week_3': "Sers ton·ta partenaire avec compétence et humilité.",
            'week_4': "Célèbre le progrès de votre partenariat."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie inspirante**

Ta Lune en Sagittaire en Maison 7 cherche l'expansion par les relations. Ton Ascendant Balance, maître naturel de cette maison, ajoute sens de l'équilibre et beauté relationnelle. Tu veux des partenariats parfaits.

**Domaine activé** : Maison 7 — Tes relations cherchent l'équilibre idéal entre autonomie et union. Tu veux un·e partenaire avec qui tu crées de la beauté, qui te complète tout en te laissant libre. L'harmonie et l'expansion ensemble.

**Ton approche instinctive** : La Balance te fait chercher l'équité dans tes relations. Tu veux que ce soit juste, beau, équilibré. Cette approche diplomatique crée des partenariats harmonieux.

**Tensions possibles** : Le besoin d'harmonie peut te faire sacrifier ta vérité. Tu risques de trop céder pour maintenir la paix, de te perdre dans le compromis.

**Conseil clé** : Créer des partenariats équilibrés qui honorent aussi ton besoin de vérité.""",
        'weekly_advice': {
            'week_1': "Définis l'équilibre entre union et autonomie.",
            'week_2': "Crée de la beauté et de l'harmonie dans tes relations.",
            'week_3': "Ose dire ta vérité même si ça crée du conflit temporaire.",
            'week_4': "Observe comment tu as créé de vrais partenariats."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Fusion transformée**

Ta Lune en Sagittaire en Maison 7 cherche l'expansion par les relations. Ton Ascendant Scorpion ajoute intensité et besoin de transformation. Tu veux des partenariats qui te changent en profondeur.

**Domaine activé** : Maison 7 — Tes relations traversent une métamorphose radicale. Tu veux une intimité totale, un·e partenaire qui n'a pas peur de tes profondeurs. Les relations superficielles ne t'intéressent plus.

**Ton approche instinctive** : Le Scorpion te fait plonger dans l'intimité avec intensité. Tu veux tout connaître de l'autre, fusionner complètement. Cette profondeur crée des liens puissants ou des ruptures nettes.

**Tensions possibles** : L'obsession peut devenir toxique. Tu risques d'alterner entre fusion anxieuse et fuite radicale, de vouloir contrôler par peur de perdre.

**Conseil clé** : Vivre l'intensité relationnelle tout en respectant les limites saines.""",
        'weekly_advice': {
            'week_1': "Regarde en face tes patterns relationnels profonds.",
            'week_2': "Transforme une dynamique toxique dans tes relations.",
            'week_3': "Accepte l'intimité sans chercher à contrôler.",
            'week_4': "Observe comment tes relations t'ont transformé·e."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Compagnons d'aventure**

Triple Sagittaire sur tes relations : Lune, Maison 7, Ascendant. L'énergie est pure exploration à deux, partenariats d'aventuriers. Tu veux un·e compagnon·ne de route, pas un·e geôlier·ère.

**Domaine activé** : Maison 7 — Tes partenariats DOIVENT être basés sur la liberté et la croissance mutuelle. Tu veux explorer le monde ensemble, partager une quête philosophique, grandir côte à côte. L'amour possessif t'étouffe.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu crois en l'amour libre et expansif. Tu veux un·e partenaire qui soit aussi indépendant·e que toi. Cette foi peut créer des relations vraiment libérantes.

**Tensions possibles** : L'excès de liberté peut empêcher la vraie intimité. Tu risques de fuir tout engagement, de confondre amour et amitié philosophique.

**Conseil clé** : Créer des partenariats libres qui acceptent aussi la vulnérabilité.""",
        'weekly_advice': {
            'week_1': "Définis ta philosophie du partenariat.",
            'week_2': "Cherche un·e compagnon·ne d'aventure, pas un·e gardien·ne.",
            'week_3': "Accepte que la vraie liberté inclut l'engagement choisi.",
            'week_4': "Célèbre les explorations que vous avez partagées."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Alliance durable**

Ta Lune en Sagittaire en Maison 7 cherche l'expansion par les relations. Ton Ascendant Capricorne ajoute sérieux et ambition. Tu veux des partenariats qui durent et qui construisent quelque chose d'important.

**Domaine activé** : Maison 7 — Tes relations cherchent à allier vision et structure. Tu veux un·e partenaire avec qui bâtir un héritage, créer quelque chose de durable tout en explorant. Le partenariat devient projet à long terme.

**Ton approche instinctive** : Le Capricorne te fait construire tes relations patiemment. Tu veux un engagement sérieux, un·e partenaire responsable. Cette maturité crée des partenariats vraiment solides.

**Tensions possibles** : Le sérieux peut étouffer la spontanéité. Tu risques de te sentir déchiré·e entre besoin de liberté et sens du devoir relationnel.

**Conseil clé** : Construire des partenariats durables qui permettent aussi l'exploration.""",
        'weekly_advice': {
            'week_1': "Définis un objectif relationnel à long terme inspirant.",
            'week_2': "Construis les fondations d'un partenariat durable.",
            'week_3': "Assume tes engagements tout en gardant ta vision.",
            'week_4': "Célèbre la solidité de ce que vous construisez."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Amour révolutionnaire**

Ta Lune en Sagittaire en Maison 7 cherche l'expansion par les relations. Ton Ascendant Verseau ajoute originalité et conscience collective. Tu veux des partenariats qui changent les paradigmes.

**Domaine activé** : Maison 7 — Tes relations expérimentent avec de nouveaux modèles. Tu veux des partenariats non-conventionnels, basés sur l'amitié profonde et la liberté totale. Les formes traditionnelles ne te conviennent pas.

**Ton approche instinctive** : Le Verseau te fait chercher l'égalité et l'originalité. Tu veux un·e partenaire qui soit ton·ta meilleur·e ami·e, qui partage ta vision d'un monde meilleur. Cette approche peut vraiment innover.

**Tensions possibles** : L'excès d'intellectualisation peut te déconnecter de l'intimité réelle. Tu risques de fuir l'amour par peur de perdre ta liberté, de rejeter l'engagement par principe.

**Conseil clé** : Révolutionner tes partenariats tout en acceptant les besoins humains d'intimité.""",
        'weekly_advice': {
            'week_1': "Explore des modèles relationnels vraiment nouveaux.",
            'week_2': "Connecte-toi à des partenaires qui partagent ta vision.",
            'week_3': "Expérimente avec la liberté ET l'intimité.",
            'week_4': "Observe comment ton originalité a enrichi tes relations."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Fusion mystique**

Ta Lune en Sagittaire en Maison 7 cherche l'expansion par les relations. Ton Ascendant Poissons ajoute dimension spirituelle et dissolution des frontières. Tu veux une union sacrée, un amour transcendant.

**Domaine activé** : Maison 7 — Tes relations cherchent la transcendance. Tu veux un·e partenaire avec qui fusionner spirituellement, explorer les mystères de l'existence. L'amour devient chemin mystique.

**Ton approche instinctive** : Le Poissons te fait aimer avec dévotion totale. Tu t'abandonnes dans l'amour, tu ressens l'autre profondément. Cette sensibilité crée une intimité rare.

**Tensions possibles** : Le manque de limites peut créer des relations toxiques. Tu risques de te perdre dans l'autre, de confondre fusion et dissolution, de fuir les conflits par le spirituel.

**Conseil clé** : Vivre l'union mystique tout en maintenant ton intégrité personnelle.""",
        'weekly_advice': {
            'week_1': "Médite sur ta vision sacrée du partenariat.",
            'week_2': "Crée une connexion spirituelle profonde avec ton·ta partenaire.",
            'week_3': "Pose des limites saines même dans l'amour fusionnel.",
            'week_4': "Ancre ta relation mystique dans la réalité quotidienne."
        }
    },

    # ==================== MAISON 8 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Renaissance audacieuse**

Ta Lune en Sagittaire active la Maison 8 : ta transformation et tes ressources partagées cherchent le sens. Avec l'Ascendant Bélier, tu veux renaître avec courage, explorer les mystères avec audace.

**Domaine activé** : Maison 8 — Tes transformations profondes, ta sexualité, tes ressources communes sont illuminées par ta quête de vérité. Tu veux comprendre la mort et la renaissance, plonger dans l'intimité totale.

**Ton approche instinctive** : Le Bélier te fait affronter les profondeurs sans peur. Tu fonces vers ce qui transforme, tu oses regarder l'ombre en face. Ce courage peut vraiment libérer ton pouvoir.

**Tensions possibles** : L'impulsivité peut te faire brûler dans tes transformations. Tu risques de forcer les processus au lieu de les laisser mûrir, de confondre courage et inconscience.

**Conseil clé** : Affronter tes profondeurs avec courage tout en respectant le timing de la transformation.""",
        'weekly_advice': {
            'week_1': "Plonge dans une vérité sur toi que tu évitais.",
            'week_2': "Transforme une peur en force.",
            'week_3': "Explore l'intimité profonde sans fuite.",
            'week_4': "Célèbre ta renaissance courageuse."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Transformation ancrée**

Ta Lune en Sagittaire en Maison 8 cherche le sens dans la transformation. Ton Ascendant Taureau ajoute besoin de sécurité et d'ancrage. Tu veux évoluer profondément mais progressivement.

**Domaine activé** : Maison 8 — Tes ressources partagées et transformations cherchent la stabilité dans le changement. Tu veux comprendre les mystères de manière tangible, construire une sécurité financière commune.

**Ton approche instinctive** : Le Taureau te fait transformer lentement. Tu veux que les changements soient solides, durables, incarnés dans le corps. Cette approche crée des métamorphoses vraiment intégrées.

**Tensions possibles** : La peur du changement peut bloquer ta transformation. Tu risques de t'accrocher à ce qui est familier même quand ça te limite, de résister par besoin de sécurité.

**Conseil clé** : Accepter les transformations nécessaires tout en les ancrant concrètement.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit changer pour ta croissance.",
            'week_2': "Crée de la sécurité dans le processus de transformation.",
            'week_3': "Ancre les changements dans ton corps et ta vie.",
            'week_4': "Savoure la stabilité dans ta nouvelle forme."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Mystères explorés**

Ta Lune en Sagittaire en Maison 8 cherche le sens dans les profondeurs. Ton Ascendant Gémeaux ajoute curiosité intellectuelle. Tu veux comprendre les mystères par l'étude et l'échange.

**Domaine activé** : Maison 8 — Ta transformation passe par la compréhension. Tu explores la psychologie, l'occultisme, les mystères de la vie et de la mort avec ton esprit curieux. La connaissance transforme.

**Ton approche instinctive** : Le Gémeaux te fait explorer les profondeurs par la communication et l'apprentissage. Tu lis, tu questionnes, tu dialogues sur les tabous. Cette approche intellectualise la transformation.

**Tensions possibles** : L'intellectualisation peut t'empêcher de vraiment ressentir. Tu risques de rester en surface mentalement au lieu de vivre la transformation émotionnellement.

**Conseil clé** : Comprendre les mystères tout en acceptant de les vivre dans ton corps.""",
        'weekly_advice': {
            'week_1': "Étudie un sujet qui touche aux mystères de l'existence.",
            'week_2': "Dialogue sur ce qui est habituellement tabou.",
            'week_3': "Descends de ta tête dans ton corps émotionnel.",
            'week_4': "Intègre ce que tu as compris ET ressenti."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Renaissance émotionnelle**

Ta Lune en Sagittaire en Maison 8 cherche la transformation profonde. Ton Ascendant Cancer ajoute sensibilité émotionnelle intense. Tu veux guérir les blessures profondes, comprendre les cycles de vie.

**Domaine activé** : Maison 8 — Tes transformations touchent les racines émotionnelles. Tu explores l'héritage familial, les traumas transgénérationnels, les secrets de famille. La guérison devient quête spirituelle.

**Ton approche instinctive** : Le Cancer te fait plonger dans les eaux émotionnelles profondes. Tu ressens intensément les processus de mort et renaissance. Cette sensibilité permet une vraie catharsis.

**Tensions possibles** : La peur de la douleur peut te faire fuir la transformation. Tu risques d'alterner entre plongée émotionnelle et protection excessive.

**Conseil clé** : Accepter la vulnérabilité nécessaire à la vraie transformation.""",
        'weekly_advice': {
            'week_1': "Explore un héritage familial qui te pèse.",
            'week_2': "Laisse mourir ce qui doit mourir émotionnellement.",
            'week_3': "Nourris ta renaissance avec douceur.",
            'week_4': "Observe comment tu as guéri en profondeur."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Phénix rayonnant**

Double feu sur la Maison 8 : ta Lune en Sagittaire et ton Ascendant Lion créent une transformation puissante et visible. Tu veux renaître de manière spectaculaire, briller depuis tes profondeurs.

**Domaine activé** : Maison 8 — Ta transformation devient créative et inspirante. Tu veux que ta renaissance soit vue, que ton pouvoir profond rayonne. L'alchimie personnelle devient art.

**Ton approche instinctive** : Le Lion te fait transformer avec fierté et créativité. Tu ne caches pas tes métamorphoses, tu les célèbres. Cette approche inspire les autres à oser leur propre transformation.

**Tensions possibles** : L'ego peut empêcher la vraie vulnérabilité. Tu risques de performer ta transformation au lieu de la vivre, de vouloir contrôler l'image de ta renaissance.

**Conseil clé** : Renaître authentiquement, pas pour le spectacle mais pour ton essence.""",
        'weekly_advice': {
            'week_1': "Ose montrer ta vulnérabilité en transformation.",
            'week_2': "Crée de la beauté depuis tes profondeurs.",
            'week_3': "Brille depuis ton pouvoir réel, pas ton masque.",
            'week_4': "Célèbre ta renaissance avec authenticité."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Guérison précise**

Ta Lune en Sagittaire en Maison 8 cherche le sens dans la transformation. Ton Ascendant Vierge ajoute discernement et capacité de guérison. Tu veux comprendre les mécanismes de la métamorphose.

**Domaine activé** : Maison 8 — Ta transformation est analytique et méthodique. Tu explores la psychologie profonde, les techniques de guérison, les processus de purification. Le détail révèle le sens.

**Ton approche instinctive** : La Vierge te fait analyser tes transformations. Tu vois les patterns, tu comprends les mécanismes, tu affines le processus. Cette rigueur peut vraiment accélérer la guérison.

**Tensions possibles** : L'analyse excessive peut éviter le ressenti. Tu risques de disséquer ta transformation au lieu de la vivre, de contrôler au lieu de t'abandonner.

**Conseil clé** : Utiliser ton discernement pour guider la transformation, pas pour l'empêcher.""",
        'weekly_advice': {
            'week_1': "Analyse honnêtement tes patterns de transformation.",
            'week_2': "Mets en place des pratiques de purification.",
            'week_3': "Lâche le contrôle et laisse le processus opérer.",
            'week_4': "Observe comment tu as affiné ta métamorphose."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Transformation partagée**

Ta Lune en Sagittaire en Maison 8 cherche le sens dans les profondeurs. Ton Ascendant Balance ajoute dimension relationnelle. Tu veux transformer à travers les relations, équilibrer pouvoir et vulnérabilité.

**Domaine activé** : Maison 8 — Tes transformations passent par l'intimité partagée. Tu explores les dynamiques de pouvoir dans les relations, les ressources communes, la vulnérabilité mutuelle. L'autre devient miroir.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre même dans les profondeurs. Tu veux que la transformation soit juste, harmonieuse, partagée. Cette approche crée des métamorphoses relationnelles.

**Tensions possibles** : Le besoin d'harmonie peut éviter les conflits nécessaires. Tu risques de sacrifier ta transformation pour maintenir la paix relationnelle.

**Conseil clé** : Accepter que la vraie transformation demande parfois du déséquilibre temporaire.""",
        'weekly_advice': {
            'week_1': "Explore les dynamiques de pouvoir dans tes relations.",
            'week_2': "Ose la vulnérabilité totale avec quelqu'un de confiance.",
            'week_3': "Transforme ensemble tout en restant toi-même.",
            'week_4': "Observe comment l'intimité vous a changé·es."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Alchimie totale**

Ta Lune en Sagittaire en Maison 8 cherche le sens dans la transformation. Ton Ascendant Scorpion, maître naturel de cette maison, ajoute puissance et profondeur. Tu es l'alchimiste qui transforme le plomb en or.

**Domaine activé** : Maison 8 — Ta transformation atteint son maximum de puissance. Tu veux descendre aux enfers et en revenir régénéré·e. Rien de superficiel, tout doit être transmué radicalement.

**Ton approche instinctive** : Le Scorpion te fait plonger sans peur dans les abysses. Tu explores les tabous, tu affrontes la mort symbolique, tu ressuscites transformé·e. Cette intensité crée une vraie métamorphose.

**Tensions possibles** : L'obsession peut devenir destructrice. Tu risques de te perdre dans les ténèbres, de confondre transformation et autodestruction.

**Conseil clé** : Plonger dans les profondeurs tout en gardant foi en la lumière qui attend.""",
        'weekly_advice': {
            'week_1': "Affronte ta peur la plus profonde.",
            'week_2': "Laisse mourir complètement ce qui doit partir.",
            'week_3': "Accepte l'inconfort de la chrysalide.",
            'week_4': "Émerge transformé·e, régénéré·e, puissant·e."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Phénix philosophe**

Triple Sagittaire sur ta transformation : Lune, Maison 8, Ascendant. L'énergie est pure quête de sens à travers la mort et la renaissance. Tu veux comprendre les grands mystères, transformer par la foi.

**Domaine activé** : Maison 8 — Ta transformation devient quête spirituelle. Tu explores les mystères existentiels, tu cherches le sens de la vie et de la mort. La métamorphose est voyage philosophique.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu crois que chaque fin est un nouveau départ. Tu traverses les crises avec optimisme et foi. Cette perspective rend tes renaissances inspirantes.

**Tensions possibles** : L'excès d'optimisme peut t'empêcher d'intégrer vraiment. Tu risques de fuir la douleur de la transformation par la spiritualisation, de papillonner entre crises.

**Conseil clé** : Vivre pleinement chaque transformation avant de passer à la suivante.""",
        'weekly_advice': {
            'week_1': "Médite sur le sens de ce qui meurt en toi.",
            'week_2': "Traverse la transformation avec foi.",
            'week_3': "Intègre vraiment les leçons avant de rebondir.",
            'week_4': "Célèbre ta renaissance philosophique."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Pouvoir construit**

Ta Lune en Sagittaire en Maison 8 cherche le sens dans la transformation. Ton Ascendant Capricorne ajoute discipline et ambition. Tu veux transformer pour accéder au vrai pouvoir, construire ta force profonde.

**Domaine activé** : Maison 8 — Ta transformation devient stratégique et durable. Tu explores les mécanismes du pouvoir, tu construis des ressources partagées, tu grimpes vers la maîtrise de tes profondeurs.

**Ton approche instinctive** : Le Capricorne te fait transformer avec patience et structure. Tu ne cherches pas la catharsis spectaculaire mais la métamorphose solide. Cette maturité crée un pouvoir réel.

**Tensions possibles** : Le contrôle peut empêcher la vraie transformation. Tu risques de vouloir gérer des processus qui demandent l'abandon, de résister par peur de perdre le contrôle.

**Conseil clé** : Construire ton pouvoir profond tout en acceptant la vulnérabilité de la transformation.""",
        'weekly_advice': {
            'week_1': "Définis le pouvoir profond que tu veux développer.",
            'week_2': "Crée une structure qui soutient ta transformation.",
            'week_3': "Lâche le contrôle quand le processus le demande.",
            'week_4': "Célèbre le pouvoir réel que tu as construit."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolution intérieure**

Ta Lune en Sagittaire en Maison 8 cherche le sens dans la transformation. Ton Ascendant Verseau ajoute innovation et conscience collective. Tu veux transformer les paradigmes, libérer par la conscience.

**Domaine activé** : Maison 8 — Ta transformation touche les structures collectives. Tu explores comment changer les systèmes de pouvoir, libérer les tabous sociaux, révolutionner l'intimité.

**Ton approche instinctive** : Le Verseau te fait transformer de manière originale. Tu brises les patterns anciens, tu explores des voies nouvelles de guérison. Cette audace peut vraiment innover.

**Tensions possibles** : L'intellectualisation peut éviter la vraie profondeur. Tu risques de fuir l'intimité par l'abstraction, de révolutionner en surface sans vraie transformation.

**Conseil clé** : Révolutionner tes profondeurs tout en restant connecté·e à l'humain.""",
        'weekly_advice': {
            'week_1': "Explore des approches nouvelles de transformation.",
            'week_2': "Libère-toi d'un tabou personnel ou collectif.",
            'week_3': "Connecte ta transformation à celle du collectif.",
            'week_4': "Observe comment tu as innové dans ta métamorphose."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 8, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution mystique**

Ta Lune en Sagittaire en Maison 8 cherche le sens dans la transformation. Ton Ascendant Poissons ajoute dimension spirituelle et dissolution. Tu veux fusionner avec le mystère, te dissoudre dans l'universel.

**Domaine activé** : Maison 8 — Ta transformation devient expérience mystique. Tu explores la mort de l'ego, la fusion avec le divin, la transcendance par l'abandon. La métamorphose est spirituelle.

**Ton approche instinctive** : Le Poissons te fait transformer par l'abandon et la foi. Tu laisses le processus t'emporter, tu t'ouvres aux dimensions invisibles. Cette perméabilité permet une vraie transcendance.

**Tensions possibles** : Le manque de limites peut créer la confusion. Tu risques de te perdre complètement, de confondre dissolution spirituelle et désintégration psychique.

**Conseil clé** : Vivre la dissolution mystique tout en gardant un fil qui te ramène.""",
        'weekly_advice': {
            'week_1': "Médite sur la mort de l'ego et la renaissance spirituelle.",
            'week_2': "Abandonne-toi au processus de transformation.",
            'week_3': "Pose des limites pour ne pas te perdre complètement.",
            'week_4': "Intègre ton expérience mystique dans la vie concrète."
        }
    },

    # ==================== MAISON 9 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Guerrier philosophe**

Ta Lune en Sagittaire active la Maison 9, sa maison naturelle : ta quête de sens est amplifiée. Avec l'Ascendant Bélier, tu veux conquérir la sagesse, explorer le monde avec audace, défendre tes convictions.

**Domaine activé** : Maison 9 — Tes voyages, ta philosophie, ton enseignement sont au cœur de ton mois. Tu veux élargir tes horizons physiquement et mentalement, découvrir de nouvelles vérités, partager ce que tu apprends.

**Ton approche instinctive** : Le Bélier te fait foncer vers l'inconnu. Tu voyages spontanément, tu apprends avec passion, tu débats avec fougue. Cette audace ouvre vraiment de nouveaux territoires.

**Tensions possibles** : L'impulsivité peut te faire partir sans préparation. Tu risques de te disperser entre mille explorations, de prêcher plus que d'écouter.

**Conseil clé** : Canaliser ton énergie exploratrice vers une quête qui a vraiment du sens.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans une aventure qui élargit ta vision.",
            'week_2': "Étudie une philosophie ou culture nouvelle.",
            'week_3': "Débats avec passion mais reste ouvert·e.",
            'week_4': "Célèbre tout ce que tu as découvert."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sagesse incarnée**

Ta Lune en Sagittaire en Maison 9 cherche la vérité et l'expansion. Ton Ascendant Taureau ajoute ancrage et pragmatisme. Tu veux une philosophie qui se vit dans le corps et le quotidien.

**Domaine activé** : Maison 9 — Ta quête de sens cherche à s'incarner concrètement. Tu voyages pour expérimenter vraiment, tu apprends ce qui a une application pratique, tu construis une sagesse durable.

**Ton approche instinctive** : Le Taureau te fait explorer lentement et profondément. Tu veux savourer chaque découverte, intégrer chaque leçon dans ton corps. Cette approche crée une sagesse vraiment enracinée.

**Tensions possibles** : La prudence peut limiter ton exploration. Tu risques de retenir ton expansion par peur, de rester dans ta zone de confort philosophique.

**Conseil clé** : Oser l'aventure tout en ancrant chaque découverte.""",
        'weekly_advice': {
            'week_1': "Définis une exploration qui respecte ton rythme.",
            'week_2': "Voyage de manière qui nourrit ton corps et ton esprit.",
            'week_3': "Intègre chaque leçon avant de passer à la suivante.",
            'week_4': "Savoure la sagesse incarnée que tu as développée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Voyageur mental**

Ta Lune en Sagittaire en Maison 9 cherche la vérité universelle. Ton Ascendant Gémeaux, en opposition à cette maison, crée une tension créative. Tu veux explorer tous les horizons, connecter toutes les perspectives.

**Domaine activé** : Maison 9 — Ton exploration est à la fois vaste et multiple. Tu voyages mentalement partout, tu apprends de tout le monde, tu connectes les savoirs locaux et universels. Le monde est ta salle de classe.

**Ton approche instinctive** : Le Gémeaux te fait papillonner entre cultures et philosophies. Tu explores avec curiosité insatiable, tu communiques ce que tu découvres. Cette agilité mentale est rare.

**Tensions possibles** : La dispersion peut t'empêcher d'approfondir vraiment. Tu risques de collectionner les expériences sans jamais intégrer de vraie sagesse.

**Conseil clé** : Explorer largement tout en synthétisant en une compréhension cohérente.""",
        'weekly_advice': {
            'week_1': "Explore plusieurs cultures ou philosophies différentes.",
            'week_2': "Voyage virtuellement ou physiquement dans des territoires nouveaux.",
            'week_3': "Cherche les connexions entre tes diverses découvertes.",
            'week_4': "Synthétise tout ce que tu as appris en une vision élargie."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Pèlerin émotionnel**

Ta Lune en Sagittaire en Maison 9 cherche le sens et l'expansion. Ton Ascendant Cancer ajoute profondeur émotionnelle et besoin de connexion. Tu veux explorer le monde tout en restant connecté·e à tes racines.

**Domaine activé** : Maison 9 — Ton exploration cherche à nourrir l'âme. Tu voyages pour comprendre d'autres façons de vivre en famille, tu étudies pour enrichir ton héritage émotionnel. Le voyage devient quête de foyer élargi.

**Ton approche instinctive** : Le Cancer te fait explorer avec sensibilité. Tu crées des connexions émotionnelles partout où tu vas, tu ressens les cultures. Cette approche crée une compréhension vraiment profonde.

**Tensions possibles** : La peur de perdre ta sécurité peut freiner ton exploration. Tu risques d'alterner entre besoin d'aventure et accrochage au familier.

**Conseil clé** : Explorer le monde tout en portant ton foyer dans ton cœur.""",
        'weekly_advice': {
            'week_1': "Définis ce que 'foyer' signifie dans ton exploration.",
            'week_2': "Explore des cultures qui honorent la famille différemment.",
            'week_3': "Crée des connexions émotionnelles dans tes découvertes.",
            'week_4': "Intègre tes apprentissages dans ton héritage émotionnel."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Explorateur royal**

Double feu sur la Maison 9 : ta Lune en Sagittaire dans sa maison naturelle et ton Ascendant Lion créent une quête magnifique et inspirante. Tu veux explorer grandement, enseigner noblement.

**Domaine activé** : Maison 9 — Ta quête de sens devient expression de ta grandeur. Tu veux voyager avec style, étudier pour briller, enseigner pour inspirer. Ta philosophie est généreuse et créative.

**Ton approche instinctive** : Le Lion te fait explorer avec fierté et créativité. Tu ne te contentes pas de découvrir, tu veux vivre des aventures mémorables. Cette approche rend ton exploration vraiment inspirante.

**Tensions possibles** : L'ego peut transformer la quête en performance. Tu risques de voyager pour impressionner, d'enseigner pour être admiré·e plutôt que pour servir la vérité.

**Conseil clé** : Explorer et enseigner avec noblesse depuis ton cœur véritable.""",
        'weekly_advice': {
            'week_1': "Définis une quête digne de ton cœur noble.",
            'week_2': "Explore avec courage et générosité d'esprit.",
            'week_3': "Partage ta sagesse de manière qui inspire.",
            'week_4': "Célèbre l'explorateur magnifique que tu es."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Sagesse vérifiée**

Ta Lune en Sagittaire en Maison 9 cherche la vérité et l'expansion. Ton Ascendant Vierge ajoute discernement et rigueur. Tu veux une philosophie qui résiste à l'examen, des voyages qui t'enseignent vraiment.

**Domaine activé** : Maison 9 — Ta quête de sens est méthodique et précise. Tu étudies sérieusement, tu vérifies tes sources, tu analyses ce que tu apprends. La rigueur intellectuelle enrichit ton exploration.

**Ton approche instinctive** : La Vierge te fait explorer avec attention aux détails. Tu veux comprendre vraiment, pas juste collectionner des expériences. Cette approche crée une sagesse solide.

**Tensions possibles** : L'analyse excessive peut tuer l'inspiration. Tu risques de critiquer toute philosophie au lieu de te laisser inspirer, de te perdre dans les détails.

**Conseil clé** : Utiliser ton discernement pour affiner ta compréhension, pas pour bloquer ta vision.""",
        'weekly_advice': {
            'week_1': "Examine tes croyances avec honnêteté intellectuelle.",
            'week_2': "Étudie en profondeur ce qui t'attire.",
            'week_3': "Vérifie tes sources mais garde ton ouverture.",
            'week_4': "Observe comment rigueur et foi se sont enrichies."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomate universel**

Ta Lune en Sagittaire en Maison 9 cherche la vérité. Ton Ascendant Balance ajoute sens de l'équilibre et diplomatie. Tu veux créer des ponts entre cultures, trouver la vérité dans le dialogue.

**Domaine activé** : Maison 9 — Ton exploration cherche l'harmonie universelle. Tu voyages pour créer des connexions, tu étudies pour comprendre tous les points de vue. La philosophie devient art du dialogue.

**Ton approche instinctive** : La Balance te fait explorer avec ouverture et équité. Tu cherches ce qui unit plutôt que ce qui divise. Cette approche crée une compréhension vraiment inclusive.

**Tensions possibles** : Le relativisme peut diluer ta vérité personnelle. Tu risques de tellement voir tous les points de vue que tu perds ton propre nord.

**Conseil clé** : Honorer toutes les perspectives tout en gardant ta propre boussole.""",
        'weekly_advice': {
            'week_1': "Engage des dialogues interculturels enrichissants.",
            'week_2': "Cherche ce qui unit les différentes philosophies.",
            'week_3': "Maintiens ton nord tout en restant ouvert·e.",
            'week_4': "Intègre la diversité dans ta vision personnelle."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité radicale**

Ta Lune en Sagittaire en Maison 9 cherche le sens et l'expansion. Ton Ascendant Scorpion ajoute intensité et besoin de transformation. Tu veux les vérités profondes, pas les philosophies de surface.

**Domaine activé** : Maison 9 — Ta quête devient exploration des mystères ultimes. Tu veux comprendre la vie, la mort, le pouvoir, la transcendance. Tes voyages sont initiatiques.

**Ton approche instinctive** : Le Scorpion te fait plonger dans les aspects cachés des cultures. Tu explores les tabous, les rituels de transformation. Cette profondeur crée une sagesse vraiment puissante.

**Tensions possibles** : L'obsession de la vérité peut devenir destructrice. Tu risques de rejeter toute légèreté, de voir le côté sombre partout.

**Conseil clé** : Chercher la vérité profonde tout en gardant foi en la lumière.""",
        'weekly_advice': {
            'week_1': "Plonge dans une philosophie qui touche les profondeurs.",
            'week_2': "Explore les aspects cachés d'une culture.",
            'week_3': "Transforme une croyance limitante radicalement.",
            'week_4': "Émerge avec une sagesse forgée dans les profondeurs."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Pèlerin éternel**

Triple Sagittaire sur ta quête : Lune, Maison 9, Ascendant. L'énergie est pure exploration philosophique, quête de vérité absolue. Tu ES le chercheur, l'aventurier, le philosophe éternel.

**Domaine activé** : Maison 9 — Ta vie ENTIÈRE est une quête de sens. Tu veux tout comprendre, tout explorer, tout expérimenter. Le voyage est ton état naturel, l'apprentissage ta respiration.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu vis selon ta quête sans compromis. Tu crois en l'expansion infinie de la conscience. Cette foi rend ton chemin magnétique.

**Tensions possibles** : L'excès peut te faire fuir toute profondeur par le mouvement constant. Tu risques de chercher éternellement sans jamais trouver, de voyager sans jamais arriver.

**Conseil clé** : Accepter que parfois la vraie découverte demande de s'arrêter pour intégrer.""",
        'weekly_advice': {
            'week_1': "Pars à l'aventure avec foi et enthousiasme total.",
            'week_2': "Explore sans limite tout ce qui t'attire.",
            'week_3': "Vérifie que tu cherches vraiment, pas que tu fuis.",
            'week_4': "Intègre tes découvertes avant de repartir."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Maître sage**

Ta Lune en Sagittaire en Maison 9 cherche la vérité et l'expansion. Ton Ascendant Capricorne ajoute discipline et ambition. Tu veux devenir une autorité dans ton domaine, construire une sagesse reconnue.

**Domaine activé** : Maison 9 — Ta quête devient carrière et héritage. Tu veux étudier sérieusement, enseigner avec autorité, créer une philosophie qui dure. L'expertise à long terme t'attire.

**Ton approche instinctive** : Le Capricorne te fait grimper patiemment vers la maîtrise. Tu es prêt·e à faire le travail dur pour comprendre vraiment. Cette maturité crée une sagesse solide.

**Tensions possibles** : Le sérieux peut étouffer ton enthousiasme naturel. Tu risques de te sentir déchiré·e entre inspiration spontanée et études rigoureuses.

**Conseil clé** : Construire ton expertise tout en gardant la flamme de ta curiosité.""",
        'weekly_advice': {
            'week_1': "Définis un domaine où devenir vraiment expert·e.",
            'week_2': "Étudie avec discipline et rigueur.",
            'week_3': "Construis une réputation de sagesse crédible.",
            'week_4': "Célèbre les fondations de ton autorité philosophique."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Visionnaire universel**

Ta Lune en Sagittaire en Maison 9 cherche la vérité. Ton Ascendant Verseau ajoute innovation et conscience collective. Tu veux une philosophie qui libère l'humanité, explorer le futur.

**Domaine activé** : Maison 9 — Ta quête est avant-gardiste et humaniste. Tu explores les idées qui peuvent changer le monde, tu voyages pour comprendre comment créer un futur meilleur.

**Ton approche instinctive** : Le Verseau te fait chercher les paradigmes nouveaux. Tu veux des vérités qui libèrent, des philosophies qui révolutionnent. Cette audace peut vraiment innover.

**Tensions possibles** : L'excès d'abstraction peut te déconnecter du réel. Tu risques de te perdre dans des utopies, de rejeter la sagesse ancienne par principe.

**Conseil clé** : Explorer le futur tout en honorant les vérités intemporelles.""",
        'weekly_advice': {
            'week_1': "Explore des idées vraiment révolutionnaires.",
            'week_2': "Connecte-toi à des communautés visionnaires.",
            'week_3': "Cherche comment ta philosophie peut servir le collectif.",
            'week_4': "Partage ta vision d'un futur meilleur."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 9, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Mystique voyageur**

Ta Lune en Sagittaire en Maison 9 cherche le sens ultime. Ton Ascendant Poissons ajoute dimension spirituelle et dissolution. Tu veux une vérité qui transcende, explorer les dimensions invisibles.

**Domaine activé** : Maison 9 — Ta quête devient pèlerinage mystique. Tu voyages pour l'éveil spirituel, tu étudies les traditions sacrées, tu cherches l'union avec le divin. La philosophie est prière.

**Ton approche instinctive** : Le Poissons te fait explorer par l'intuition et la foi. Tu ressens la vérité plus que tu ne la penses. Cette perméabilité permet des insights profonds.

**Tensions possibles** : Le manque de structure peut créer la confusion. Tu risques de te perdre dans des illusions spirituelles, de confondre imagination et illumination.

**Conseil clé** : Vivre ta quête mystique tout en gardant un minimum d'ancrage.""",
        'weekly_advice': {
            'week_1': "Médite sur les grandes questions spirituelles.",
            'week_2': "Explore une tradition mystique qui t'attire.",
            'week_3': "Vérifie que ta quête n'est pas une fuite déguisée.",
            'week_4': "Intègre tes insights spirituels dans la vie concrète."
        }
    },

    # ==================== MAISON 10 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Conquérant visionnaire**

Ta Lune en Sagittaire en Maison 10 cherche une carrière inspirante et porteuse de sens. Ton Ascendant Bélier ajoute audace et leadership. Tu veux briller professionnellement en montrant une vision courageuse.

**Domaine activé** : Maison 10 — Ton ambition cherche l'expansion et l'impact. Tu veux une reconnaissance qui va au-delà du succès matériel : tu veux inspirer, ouvrir des chemins, être un·e pionnier·ère dans ton domaine.

**Ton approche instinctive** : Le Bélier te fait foncer vers tes objectifs professionnels avec foi et détermination. Tu prends des risques calculés pour ta carrière, tu oses proposer des visions ambitieuses.

**Tensions possibles** : L'impulsivité peut compromettre ta réputation. Tu risques de promettre trop, de brûler des étapes, ou de négliger les aspects politiques de ton ascension.

**Conseil clé** : Canaliser ton audace vers une ambition qui a du sens.""",
        'weekly_advice': {
            'week_1': "Définis une vision professionnelle qui t'inspire vraiment.",
            'week_2': "Prends une initiative audacieuse dans ta carrière.",
            'week_3': "Montre ton leadership avec enthousiasme et conviction.",
            'week_4': "Consolide les avancées faites avec courage."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Bâtisseur de sens**

Ta Lune en Sagittaire en Maison 10 veut une carrière qui a du sens. Ton Ascendant Taureau ajoute patience et construction solide. Tu veux bâtir une réputation durable fondée sur des valeurs.

**Domaine activé** : Maison 10 — Ton ambition cherche à créer quelque chose de tangible et porteur de vision. Tu veux être reconnu·e pour ton expertise, ta sagesse pratique, ta capacité à concrétiser l'inspiration.

**Ton approche instinctive** : Le Taureau te fait construire ta carrière progressivement, avec persévérance. Tu investis du temps pour maîtriser vraiment ton domaine, pour créer une œuvre qui dure.

**Tensions possibles** : La prudence peut freiner l'expansion naturelle de ta carrière. Tu risques de rester trop longtemps dans une zone de confort par peur de perdre ta sécurité.

**Conseil clé** : Grandir professionnellement tout en restant fidèle à tes valeurs.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment construire professionnellement.",
            'week_2': "Pose des fondations solides pour ton expansion de carrière.",
            'week_3': "Fais un pas mesuré vers plus de visibilité.",
            'week_4': "Apprécie la croissance stable que tu crées."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Communicateur influent**

Ta Lune en Sagittaire en Maison 10 cherche une carrière qui inspire. Ton Ascendant Gémeaux ajoute polyvalence et talent de communication. Tu veux être reconnu·e pour ta capacité à partager des idées qui changent les perspectives.

**Domaine activé** : Maison 10 — Ta réputation se construit sur ta capacité à connecter, enseigner, transmettre. Tu veux être un·e pont entre mondes différents, un·e vulgarisateur·rice de concepts complexes.

**Ton approche instinctive** : Le Gémeaux te fait explorer plusieurs voies professionnelles. Tu avances par la diversité, l'apprentissage constant, l'adaptation. Cette agilité crée des opportunités.

**Tensions possibles** : La dispersion peut diluer ton impact. Tu risques de papillonner professionnellement sans jamais approfondir assez pour devenir vraiment influent·e.

**Conseil clé** : Choisir une direction principale tout en gardant ta polyvalence.""",
        'weekly_advice': {
            'week_1': "Communique ta vision avec clarté et enthousiasme.",
            'week_2': "Multiplie les connexions professionnelles stratégiques.",
            'week_3': "Identifie le fil conducteur de tes diverses activités.",
            'week_4': "Consolide ta réputation d'expert·e polyvalent·e."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Leader nourricier**

Ta Lune en Sagittaire en Maison 10 veut une carrière inspirante. Ton Ascendant Cancer ajoute empathie et sensibilité au besoin des autres. Tu veux être reconnu·e pour ta capacité à guider avec humanité.

**Domaine activé** : Maison 10 — Ton ambition est de créer un impact émotionnellement significatif. Tu veux une carrière qui nourrit les autres tout en ayant une portée large. Le care rencontre la vision.

**Ton approche instinctive** : Le Cancer te fait construire ta réputation sur la confiance et l'authenticité émotionnelle. Tu inspires parce que tu es profondément humain·e dans ton leadership.

**Tensions possibles** : La peur de blesser peut t'empêcher de prendre des décisions difficiles. Tu risques de confondre popularité et véritable impact.

**Conseil clé** : Diriger avec cœur tout en gardant ta vision claire.""",
        'weekly_advice': {
            'week_1': "Définis comment nourrir les autres professionnellement.",
            'week_2': "Montre ton humanité dans ton leadership.",
            'week_3': "Prends des décisions difficiles avec compassion.",
            'week_4': "Célèbre l'impact humain que tu crées."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Étoile inspirante**

Ta Lune en Sagittaire en Maison 10 cherche à inspirer par ta carrière. Ton Ascendant Lion ajoute charisme et besoin de reconnaissance. Tu veux briller comme un phare qui guide les autres vers la grandeur.

**Domaine activé** : Maison 10 — Ton ambition est de devenir une figure emblématique, quelqu'un dont la vision et la présence inspirent. Tu veux une carrière qui te permette d'être un modèle.

**Ton approche instinctive** : Le Lion te fait rayonner ta vision avec confiance. Tu diriges par l'exemple et l'inspiration, tu crées un magnétisme naturel qui attire les opportunités.

**Tensions possibles** : L'ego peut dominer la vision. Tu risques de chercher l'admiration plus que l'impact réel, ou de devenir arrogant·e dans ton succès.

**Conseil clé** : Utiliser ta lumière pour éclairer le chemin des autres.""",
        'weekly_advice': {
            'week_1': "Ose montrer ta vision avec fierté et passion.",
            'week_2': "Rayonne ton enthousiasme professionnellement.",
            'week_3': "Vérifie que tu sers une cause plus grande que toi.",
            'week_4': "Célèbre tes succès tout en restant humble."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Maître pragmatique**

Ta Lune en Sagittaire en Maison 10 cherche une carrière inspirante. Ton Ascendant Vierge ajoute précision et service. Tu veux être reconnu·e pour ton expertise pratique au service d'une vision plus grande.

**Domaine activé** : Maison 10 — Ton ambition est de perfectionner ton art tout en ayant un impact significatif. Tu veux une réputation d'excellence technique couplée à une compréhension profonde.

**Ton approche instinctive** : La Vierge te fait construire ta carrière par l'amélioration constante. Tu analyses, tu raffines, tu sers avec dévouement. Cette rigueur crée une expertise reconnue.

**Tensions possibles** : Le perfectionnisme peut retarder ton expansion. Tu risques de te perdre dans les détails au détriment de la vision globale.

**Conseil clé** : Équilibrer excellence technique et inspiration visionnaire.""",
        'weekly_advice': {
            'week_1': "Définis des standards élevés pour ton travail.",
            'week_2': "Perfectionne un aspect clé de ton expertise.",
            'week_3': "Sers une cause qui dépasse ton travail quotidien.",
            'week_4': "Apprécie la maîtrise que tu as développée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Ambassadeur élégant**

Ta Lune en Sagittaire en Maison 10 cherche une carrière qui inspire. Ton Ascendant Balance ajoute diplomatie et sens de l'esthétique. Tu veux être reconnu·e pour ta capacité à créer l'harmonie tout en ayant une vision.

**Domaine activé** : Maison 10 — Ton ambition est de créer du beau et du juste professionnellement. Tu veux une carrière qui allie expansion et équilibre, inspiration et collaboration.

**Ton approche instinctive** : La Balance te fait construire ta réputation sur les relations. Tu avances par les partenariats stratégiques, la négociation élégante, l'influence douce.

**Tensions possibles** : Le besoin d'approbation peut diluer ta vision. Tu risques de compromiser ton authenticité pour plaire ou maintenir l'harmonie.

**Conseil clé** : Garder ta vision claire tout en collaborant avec grâce.""",
        'weekly_advice': {
            'week_1': "Construis des alliances professionnelles inspirantes.",
            'week_2': "Présente ta vision avec élégance et diplomatie.",
            'week_3': "Négocie pour tes ambitions sans perdre ton cap.",
            'week_4': "Célèbre les collaborations créées."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Réformateur puissant**

Ta Lune en Sagittaire en Maison 10 cherche une carrière inspirante. Ton Ascendant Scorpion ajoute intensité et pouvoir transformateur. Tu veux être reconnu·e pour ta capacité à révolutionner ton domaine.

**Domaine activé** : Maison 10 — Ton ambition est de transformer profondément ton secteur. Tu ne veux pas juste réussir, tu veux changer les règles du jeu, révéler des vérités cachées.

**Ton approche instinctive** : Le Scorpion te fait construire ton pouvoir stratégiquement. Tu vois ce que les autres manquent, tu utilises l'intensité pour créer l'impact. Cette profondeur est magnétique.

**Tensions possibles** : L'obsession du contrôle peut créer des conflits de pouvoir. Tu risques de manipuler ou de forcer les transformations au lieu de les inspirer.

**Conseil clé** : Transformer avec vision tout en respectant le libre arbitre.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit changer dans ton domaine.",
            'week_2': "Utilise ton intensité stratégiquement.",
            'week_3': "Propose des transformations radicales mais justes.",
            'week_4': "Consolide le pouvoir que tu as gagné."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Visionnaire libre**

Triple Sagittaire sur ta carrière : Lune, Maison 10, Ascendant. L'énergie est pure expansion professionnelle, ambition inspirante. Tu veux une carrière qui incarne ta quête de sens et de liberté.

**Domaine activé** : Maison 10 — Ta vie professionnelle EST ta philosophie en action. Tu ne peux pas séparer carrière et quête de vérité. Ton ambition est d'inspirer le monde à grandir.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu construis ta carrière selon tes convictions sans compromis. Tu prends des risques professionnels par foi en ta vision.

**Tensions possibles** : L'excès d'optimisme peut créer des promesses non tenues. Tu risques de surestimer tes capacités ou de manquer de discipline dans ton ascension.

**Conseil clé** : Canaliser ton enthousiasme vers un impact professionnel durable.""",
        'weekly_advice': {
            'week_1': "Lance une initiative professionnelle audacieuse.",
            'week_2': "Partage ta vision avec enthousiasme contagieux.",
            'week_3': "Vérifie que tu peux tenir tes engagements.",
            'week_4': "Célèbre l'expansion professionnelle créée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Architecte inspiré**

Ta Lune en Sagittaire en Maison 10 cherche une carrière inspirante. Ton Ascendant Capricorne ajoute discipline et ambition structurée. Tu veux construire un empire qui a du sens.

**Domaine activé** : Maison 10 — Ton ambition est de créer une œuvre professionnelle durable et visionnaire. Tu veux être reconnu·e comme un·e leader sage et stratégique.

**Ton approche instinctive** : Le Capricorne te fait grimper patiemment vers ton objectif. Tu es prêt·e à faire le travail dur, à accepter les responsabilités, à bâtir pierre par pierre.

**Tensions possibles** : La rigidité peut étouffer ton inspiration. Tu risques de sacrifier ton enthousiasme sur l'autel du pragmatisme.

**Conseil clé** : Construire avec patience tout en gardant la vision vivante.""",
        'weekly_advice': {
            'week_1': "Planifie ton ascension professionnelle à long terme.",
            'week_2': "Accepte des responsabilités qui te font grandir.",
            'week_3': "Construis ta réputation avec sérieux et intégrité.",
            'week_4': "Célèbre les fondations solides créées."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Innovateur humaniste**

Ta Lune en Sagittaire en Maison 10 cherche une carrière inspirante. Ton Ascendant Verseau ajoute innovation et conscience collective. Tu veux révolutionner ton domaine pour le bien commun.

**Domaine activé** : Maison 10 — Ton ambition est d'être un·e pionnier·ère qui change les paradigmes. Tu veux une carrière qui libère, qui ouvre des possibilités nouvelles pour tous.

**Ton approche instinctive** : Le Verseau te fait construire ta réputation sur l'originalité. Tu oses proposer des solutions avant-gardistes, tu t'associes à des causes progressistes.

**Tensions possibles** : La rébellion peut nuire à ton influence. Tu risques de rejeter toute autorité par principe ou de te marginaliser par excès d'originalité.

**Conseil clé** : Innover stratégiquement pour maximiser ton impact collectif.""",
        'weekly_advice': {
            'week_1': "Propose une idée vraiment innovante professionnellement.",
            'week_2': "Connecte-toi à des réseaux avant-gardistes.",
            'week_3': "Vérifie que ton innovation sert vraiment le collectif.",
            'week_4': "Consolide ta réputation de visionnaire."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 10, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Guide spirituel**

Ta Lune en Sagittaire en Maison 10 cherche une carrière inspirante. Ton Ascendant Poissons ajoute dimension spirituelle et sensibilité artistique. Tu veux être reconnu·e pour ta sagesse transcendante.

**Domaine activé** : Maison 10 — Ton ambition est de guider les autres vers l'éveil. Tu veux une carrière qui nourrit l'âme, qui inspire à travers l'art, la spiritualité, la compassion.

**Ton approche instinctive** : Le Poissons te fait construire ta réputation sur l'authenticité émotionnelle. Tu inspires par ta vulnérabilité, ta capacité à canaliser quelque chose de plus grand.

**Tensions possibles** : Le manque de structure peut compromettre ton impact. Tu risques de rêver ta carrière au lieu de la construire.

**Conseil clé** : Incarner ta vision spirituelle avec suffisamment de pragmatisme.""",
        'weekly_advice': {
            'week_1': "Définis comment servir spirituellement à travers ta carrière.",
            'week_2': "Crée quelque chose qui touche l'âme des gens.",
            'week_3': "Ajoute de la structure à ton inspiration.",
            'week_4': "Célèbre l'impact transcendant que tu crées."
        }
    },

    # ==================== MAISON 11 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Rallye collectif**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés inspirantes et des projets collectifs porteurs de sens. Ton Ascendant Bélier ajoute leadership et initiative. Tu veux être celui/celle qui unit les autres autour d'une vision.

**Domaine activé** : Maison 11 — Tes rêves collectifs prennent feu. Tu veux des amitiés basées sur des valeurs partagées, des projets qui changent le monde. La camaraderie philosophique t'appelle.

**Ton approche instinctive** : Le Bélier te pousse à initier des mouvements collectifs. Tu fonces pour créer la communauté que tu veux voir, tu rallies les troupes avec enthousiasme.

**Tensions possibles** : L'impulsivité peut créer des frictions dans le groupe. Tu risques de vouloir diriger au lieu de collaborer, ou de partir si ça ne va pas assez vite.

**Conseil clé** : Inspirer le collectif tout en respectant la diversité des rythmes.""",
        'weekly_advice': {
            'week_1': "Lance une initiative collective inspirante.",
            'week_2': "Rassemble des alliés autour d'une vision partagée.",
            'week_3': "Fonce vers vos objectifs communs avec courage.",
            'week_4': "Célèbre ce que vous avez accompli ensemble."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Tribu stable**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés inspirantes. Ton Ascendant Taureau ajoute loyauté et besoin de communauté fiable. Tu veux des connexions qui durent et qui ont du sens.

**Domaine activé** : Maison 11 — Tes rêves collectifs cherchent un ancrage. Tu veux construire des amitiés solides basées sur des valeurs partagées, créer une tribu qui grandit ensemble.

**Ton approche instinctive** : Le Taureau te fait investir lentement dans tes relations. Tu construis des amitiés qui résistent au temps, tu es loyal·e et fiable pour ta communauté.

**Tensions possibles** : La peur du changement peut limiter ton réseau. Tu risques de t'accrocher à des amitiés qui ne t'inspirent plus par confort.

**Conseil clé** : Cultiver des amitiés stables tout en restant ouvert·e à la nouveauté.""",
        'weekly_advice': {
            'week_1': "Identifie les valeurs qui fondent tes amitiés.",
            'week_2': "Investis dans une communauté qui dure.",
            'week_3': "Ouvre-toi prudemment à de nouvelles connexions.",
            'week_4': "Apprécie la tribu solide que tu as cultivée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Réseau inspirant**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés intellectuelles. Ton Ascendant Gémeaux ajoute curiosité sociale et multiplicité. Tu veux un réseau diversifié qui élargit continuellement tes horizons.

**Domaine activé** : Maison 11 — Tes amitiés sont basées sur l'échange d'idées et l'apprentissage mutuel. Tu veux des connexions stimulantes intellectuellement, des projets collectifs innovants.

**Ton approche instinctive** : Le Gémeaux te fait papillonner socialement. Tu connectes des gens différents, tu tisses des réseaux, tu crées des ponts entre communautés.

**Tensions possibles** : La superficialité peut empêcher les liens profonds. Tu risques d'avoir beaucoup de connaissances mais peu de vrais amis.

**Conseil clé** : Approfondir certaines amitiés tout en gardant ton réseau large.""",
        'weekly_advice': {
            'week_1': "Multiplie les rencontres intellectuellement stimulantes.",
            'week_2': "Connecte des personnes qui devraient se connaître.",
            'week_3': "Approfondis une amitié qui compte vraiment.",
            'week_4': "Célèbre la richesse de ton réseau diversifié."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Famille choisie**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés inspirantes. Ton Ascendant Cancer ajoute besoin de connexion émotionnelle profonde. Tu veux une communauté qui soit comme une famille choisie.

**Domaine activé** : Maison 11 — Tes amitiés nourrissent ton âme autant qu'elles élargissent ta vision. Tu cherches des connexions qui allient exploration et sécurité affective.

**Ton approche instinctive** : Le Cancer te fait créer une tribu émotionnellement sûre. Tu prends soin de tes amis, tu crées des espaces où chacun peut être vulnérable et authentique.

**Tensions possibles** : La peur de l'abandon peut te rendre possessif·ve. Tu risques de vouloir garder ta communauté fermée par peur de perdre ton cocon.

**Conseil clé** : Nourrir ta tribu tout en l'ouvrant à la croissance.""",
        'weekly_advice': {
            'week_1': "Crée un espace sécurisant pour ta communauté.",
            'week_2': "Partage émotionnellement avec tes proches.",
            'week_3': "Ouvre ton cercle à des personnes inspirantes.",
            'week_4': "Célèbre la famille que tu as choisie."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Cour inspirée**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés inspirantes. Ton Ascendant Lion ajoute générosité et besoin de rayonnement. Tu veux briller au centre d'une communauté qui partage ta vision.

**Domaine activé** : Maison 11 — Tes amitiés sont basées sur l'inspiration mutuelle et la créativité. Tu veux une cour d'âmes nobles qui s'élèvent ensemble vers la grandeur.

**Ton approche instinctive** : Le Lion te fait rassembler les autres par ton charisme. Tu inspires ta communauté, tu crées des expériences mémorables, tu donnes généreusement.

**Tensions possibles** : L'ego peut dominer la dynamique. Tu risques de vouloir être le centre d'attention au détriment de l'égalité dans les amitiés.

**Conseil clé** : Rayonner pour éclairer le collectif, pas pour t'en distinguer.""",
        'weekly_advice': {
            'week_1': "Rassemble ta communauté autour d'une célébration.",
            'week_2': "Inspire tes amis par ton enthousiasme généreux.",
            'week_3': "Assure-toi que chacun brille à sa manière.",
            'week_4': "Célèbre ce que vous avez créé ensemble."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Service collectif**

Ta Lune en Sagittaire en Maison 11 cherche des projets collectifs inspirants. Ton Ascendant Vierge ajoute efficacité et dévouement. Tu veux des amitiés basées sur le service d'une cause plus grande.

**Domaine activé** : Maison 11 — Tes rêves collectifs se concrétisent par l'action utile. Tu veux une communauté qui travaille efficacement pour améliorer le monde.

**Ton approche instinctive** : La Vierge te fait contribuer au collectif par le travail concret. Tu analyses, tu organises, tu améliores les systèmes communautaires avec dévouement.

**Tensions possibles** : La critique peut créer des tensions. Tu risques de voir les défauts plus que les forces de ta communauté.

**Conseil clé** : Servir le collectif avec excellence tout en acceptant l'imperfection.""",
        'weekly_advice': {
            'week_1': "Identifie comment servir ta communauté utilement.",
            'week_2': "Organise un projet collectif avec efficacité.",
            'week_3': "Améliore les processus sans critiquer les personnes.",
            'week_4': "Apprécie le travail collectif accompli."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Cercle harmonieux**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés inspirantes. Ton Ascendant Balance ajoute diplomatie et sens de l'équilibre. Tu veux créer une communauté harmonieuse unie par des idéaux partagés.

**Domaine activé** : Maison 11 — Tes amitiés cherchent la justice et la beauté collectives. Tu veux des relations équilibrées où chacun contribue à l'expansion mutuelle.

**Ton approche instinctive** : La Balance te fait cultiver l'harmonie dans le groupe. Tu médies les conflits, tu crées la cohésion, tu assures que chacun se sent valorisé.

**Tensions possibles** : Le besoin d'approbation peut te faire éviter les désaccords nécessaires. Tu risques de sacrifier l'authenticité pour maintenir la paix.

**Conseil clé** : Créer l'harmonie authentique, pas artificielle.""",
        'weekly_advice': {
            'week_1': "Cultive l'équilibre dans tes amitiés.",
            'week_2': "Crée de la beauté collective (art, événements).",
            'week_3': "Adresse les tensions avec grâce et honnêteté.",
            'week_4': "Célèbre l'harmonie que vous avez co-créée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Fraternité profonde**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés inspirantes. Ton Ascendant Scorpion ajoute intensité et besoin de vérité. Tu veux des connexions profondes unies par une quête radicale.

**Domaine activé** : Maison 11 — Tes amitiés explorent les profondeurs. Tu veux une communauté qui ose aller au-delà des apparences, qui transforme le monde ensemble.

**Ton approche instinctive** : Le Scorpion te fait sonder l'authenticité des connexions. Tu ne veux que des amitiés vraies, intenses, engagées. Cette exigence crée des liens puissants.

**Tensions possibles** : La méfiance peut isoler. Tu risques de tester constamment la loyauté ou de rejeter des personnes avant qu'elles aient pu prouver leur valeur.

**Conseil clé** : S'ouvrir prudemment tout en gardant des standards élevés.""",
        'weekly_advice': {
            'week_1': "Identifie qui mérite vraiment ta confiance.",
            'week_2': "Approfondis une amitié avec vulnérabilité.",
            'week_3': "Engage-toi dans un projet transformateur collectif.",
            'week_4': "Célèbre les liens profonds créés."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventuriers unis**

Triple Sagittaire sur tes amitiés : Lune, Maison 11, Ascendant. L'énergie est pure exploration collective, quête de sens partagée. Tes amis sont tes compagnons de voyage philosophique.

**Domaine activé** : Maison 11 — Tes amitiés SONT des aventures. Tu veux des connexions basées sur la croissance mutuelle, l'exploration commune, la foi en un avenir meilleur.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu rassembles les autres par ta vision optimiste. Tu crées des communautés de chercheurs, d'aventuriers, de croyants.

**Tensions possibles** : L'excès peut créer des attentes irréalistes. Tu risques de rejeter des amis qui ne partagent pas ton enthousiasme à 100%.

**Conseil clé** : Accepter la diversité des rythmes dans la quête collective.""",
        'weekly_advice': {
            'week_1': "Organise une aventure collective inspirante.",
            'week_2': "Partage ta vision avec enthousiasme contagieux.",
            'week_3': "Respecte que chacun avance à son rythme.",
            'week_4': "Célèbre la croissance collective accomplie."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Réseau stratégique**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés inspirantes. Ton Ascendant Capricorne ajoute ambition et construction à long terme. Tu veux des connexions qui servent vos objectifs mutuels.

**Domaine activé** : Maison 11 — Tes amitiés sont stratégiques autant qu'inspirantes. Tu veux construire un réseau solide de personnes qui s'élèvent mutuellement vers le succès.

**Ton approche instinctive** : Le Capricorne te fait choisir tes connexions avec soin. Tu investis dans des relations qui durent et qui apportent une valeur réelle.

**Tensions possibles** : Le calcul peut rendre tes amitiés froides. Tu risques de négliger l'aspect émotionnel au profit de l'utilité.

**Conseil clé** : Cultiver des amitiés authentiques qui servent aussi vos ambitions.""",
        'weekly_advice': {
            'week_1': "Identifie des connexions alignées avec tes objectifs.",
            'week_2': "Construis des relations professionnelles inspirantes.",
            'week_3': "Assure-toi de l'authenticité derrière la stratégie.",
            'week_4': "Apprécie le réseau solide que tu as bâti."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Tribu visionnaire**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés inspirantes. Ton Ascendant Verseau ajoute innovation et conscience collective. Tu veux une communauté qui révolutionne le monde ensemble.

**Domaine activé** : Maison 11 — Tes amitiés sont avant-gardistes. Tu veux un réseau de visionnaires, d'innovateurs, de rebelles qui créent le futur basé sur des idéaux humanistes.

**Ton approche instinctive** : Le Verseau te fait rassembler des esprits libres. Tu crées des communautés égalitaires, tu défends des causes progressistes, tu inspires par ton originalité.

**Tensions possibles** : La rébellion peut isoler. Tu risques de rejeter toute structure communautaire ou de te marginaliser par excès d'anticonformisme.

**Conseil clé** : Révolutionner tout en créant une vraie appartenance.""",
        'weekly_advice': {
            'week_1': "Connecte-toi à des communautés avant-gardistes.",
            'week_2': "Propose des idées révolutionnaires pour le collectif.",
            'week_3': "Équilibre liberté individuelle et cohésion de groupe.",
            'week_4': "Célèbre la tribu visionnaire que vous formez."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 11, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sangha spirituelle**

Ta Lune en Sagittaire en Maison 11 cherche des amitiés inspirantes. Ton Ascendant Poissons ajoute dimension spirituelle et compassion. Tu veux une communauté unie par la quête de transcendance.

**Domaine activé** : Maison 11 — Tes amitiés sont des connexions d'âmes. Tu veux une sangha spirituelle qui explore ensemble les mystères, qui s'élève par la compassion collective.

**Ton approche instinctive** : Le Poissons te fait créer une communauté par la résonance émotionnelle. Tu ressens intuitivement qui appartient à ta tribu, tu nourris par ta présence empathique.

**Tensions possibles** : Le manque de limites peut créer la confusion. Tu risques d'absorber les émotions du groupe ou de te perdre dans des illusions collectives.

**Conseil clé** : Cultiver la communion spirituelle tout en gardant des limites saines.""",
        'weekly_advice': {
            'week_1': "Cherche des âmes sœurs sur le chemin spirituel.",
            'week_2': "Crée des espaces sacrés de connexion collective.",
            'week_3': "Protège ton énergie dans les dynamiques de groupe.",
            'week_4': "Célèbre la sangha que vous avez co-créée."
        }
    },

    # ==================== MAISON 12 ====================

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Guerrier intérieur**

Ta Lune en Sagittaire en Maison 12 cherche le sens dans les profondeurs. Ton Ascendant Bélier ajoute courage pour affronter l'inconscient. Tu explores les territoires intérieurs avec la foi du pionnier.

**Domaine activé** : Maison 12 — Ton monde intérieur s'illumine d'une quête spirituelle. Tu explores tes croyances inconscientes, tu affrontes tes peurs avec optimisme, tu cherches la sagesse dans la solitude.

**Ton approche instinctive** : Le Bélier te fait plonger courageusement dans tes profondeurs. Tu ne fuis pas l'ombre, tu la conquiers. Cette bravoure guérit.

**Tensions possibles** : L'impulsivité peut créer la confusion. Tu risques de forcer les processus spirituels ou de fuir dans l'action quand l'introspection devient difficile.

**Conseil clé** : Explorer l'intérieur avec autant de courage que l'extérieur.""",
        'weekly_advice': {
            'week_1': "Affronte une peur inconsciente avec courage.",
            'week_2': "Médite sur ta foi et tes croyances profondes.",
            'week_3': "Trouve du sens dans la solitude et le retrait.",
            'week_4': "Intègre la sagesse gagnée dans l'ombre."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sanctuaire intérieur**

Ta Lune en Sagittaire en Maison 12 cherche le sens spirituel. Ton Ascendant Taureau ajoute besoin d'ancrage et de confort dans l'exploration intérieure. Tu veux créer un sanctuaire pour ta quête.

**Domaine activé** : Maison 12 — Ton monde intérieur demande de l'espace et du temps. Tu explores lentement tes croyances inconscientes, tu intègres progressivement tes insights spirituels.

**Ton approche instinctive** : Le Taureau te fait construire une pratique spirituelle stable. Tu crées des rituels nourrissants, tu explores l'inconscient avec patience et sensorialité.

**Tensions possibles** : La résistance peut bloquer l'évolution. Tu risques de t'accrocher à des croyances rassurantes même quand elles limitent.

**Conseil clé** : Créer la sécurité tout en s'ouvrant à la transformation.""",
        'weekly_advice': {
            'week_1': "Crée un espace sacré pour ton exploration intérieure.",
            'week_2': "Développe une pratique spirituelle régulière.",
            'week_3': "Lâche une croyance qui ne te sert plus.",
            'week_4': "Savoure la paix intérieure que tu as cultivée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Bibliothèque de l'âme**

Ta Lune en Sagittaire en Maison 12 cherche le sens spirituel. Ton Ascendant Gémeaux ajoute curiosité intellectuelle sur l'inconscient. Tu explores ton monde intérieur comme une bibliothèque infinie.

**Domaine activé** : Maison 12 — Ton inconscient regorge de symboles et d'histoires à déchiffrer. Tu étudies tes rêves, tu lis sur la spiritualité, tu cherches à comprendre les mystères.

**Ton approche instinctive** : Le Gémeaux te fait explorer l'inconscient par l'apprentissage. Tu journalises, tu analyses, tu communiques avec ton moi profond.

**Tensions possibles** : L'intellectualisation peut t'éloigner de l'expérience. Tu risques de conceptualiser au lieu de vivre ta spiritualité.

**Conseil clé** : Équilibrer compréhension et ressenti dans l'exploration intérieure.""",
        'weekly_advice': {
            'week_1': "Étudie un système spirituel qui t'intrigue.",
            'week_2': "Journalise tes rêves et tes insights.",
            'week_3': "Médite en silence, au-delà des mots.",
            'week_4': "Intègre ce que tu as compris profondément."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Océan émotionnel**

Ta Lune en Sagittaire en Maison 12 cherche le sens spirituel. Ton Ascendant Cancer ajoute profondeur émotionnelle et sensibilité psychique. Tu explores l'inconscient avec l'intuition comme boussole.

**Domaine activé** : Maison 12 — Ton monde intérieur est un océan d'émotions et de mémoires. Tu plonges dans les profondeurs pour guérir les blessures anciennes, tu cherches la sagesse émotionnelle.

**Ton approche instinctive** : Le Cancer te fait ressentir ton inconscient plutôt que le penser. Tu te connectes à ton enfant intérieur, tu nourris ton âme avec compassion.

**Tensions possibles** : L'hypersensibilité peut submerger. Tu risques de te noyer dans les émotions ou de t'isoler par peur d'être blessé·e.

**Conseil clé** : Honorer tes émotions profondes tout en gardant un ancrage.""",
        'weekly_advice': {
            'week_1': "Crée un cocon sûr pour ton exploration émotionnelle.",
            'week_2': "Plonge dans une blessure émotionnelle pour la guérir.",
            'week_3': "Nourris ton enfant intérieur avec tendresse.",
            'week_4': "Intègre la guérison émotionnelle accomplie."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Lumière cachée**

Ta Lune en Sagittaire en Maison 12 cherche le sens spirituel. Ton Ascendant Lion ajoute créativité et besoin d'expression même dans l'ombre. Tu veux rayonner de l'intérieur.

**Domaine activé** : Maison 12 — Ton monde intérieur cherche à créer et à briller. Tu explores ton inconscient pour libérer ta créativité authentique, pour trouver ta véritable magnificence.

**Ton approche instinctive** : Le Lion te fait transformer ton exploration intérieure en œuvre créative. Tu exprimes artistiquement ce que tu découvres dans les profondeurs.

**Tensions possibles** : L'ego peut résister à la dissolution nécessaire. Tu risques de vouloir briller même quand il faut s'effacer et écouter.

**Conseil clé** : Accepter l'humilité du travail spirituel tout en honorant ta lumière.""",
        'weekly_advice': {
            'week_1': "Explore comment ton ego limite ta croissance spirituelle.",
            'week_2': "Crée quelque chose d'inspiré par ton monde intérieur.",
            'week_3': "Pratique l'humilité dans ta quête spirituelle.",
            'week_4': "Rayonne la sagesse gagnée dans l'ombre."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Alchimie intérieure**

Ta Lune en Sagittaire en Maison 12 cherche le sens spirituel. Ton Ascendant Vierge ajoute analyse et perfectionnement. Tu veux comprendre et purifier ton monde intérieur avec précision.

**Domaine activé** : Maison 12 — Ton inconscient demande à être trié, analysé, guéri. Tu explores méthodiquement tes schémas, tu travailles sur toi avec dévotion et rigueur.

**Ton approche instinctive** : La Vierge te fait aborder la spiritualité comme un artisanat. Tu raffines ton être, tu améliores tes pratiques, tu sers ta croissance intérieure.

**Tensions possibles** : La critique peut bloquer l'acceptation. Tu risques de juger ton processus au lieu de l'accueillir avec compassion.

**Conseil clé** : Perfectionner ta pratique tout en acceptant l'imperfection du chemin.""",
        'weekly_advice': {
            'week_1': "Analyse un schéma inconscient récurrent.",
            'week_2': "Développe une routine spirituelle précise.",
            'week_3': "Sers ta guérison avec dévouement quotidien.",
            'week_4': "Apprécie le travail intérieur accompli."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre de l'âme**

Ta Lune en Sagittaire en Maison 12 cherche le sens spirituel. Ton Ascendant Balance ajoute quête d'harmonie intérieure. Tu veux trouver la paix en réconciliant tes polarités.

**Domaine activé** : Maison 12 — Ton monde intérieur cherche l'équilibre entre expansion et repos, foi et doute, action et contemplation. Tu médies entre tes parts opposées.

**Ton approche instinctive** : La Balance te fait explorer ton inconscient en cherchant la justice et la beauté. Tu veux harmoniser tes parts en conflit, créer la paix intérieure.

**Tensions possibles** : L'indécision peut paralyser ta croissance. Tu risques d'éviter les choix nécessaires ou de chercher un équilibre impossible.

**Conseil clé** : Accepter que certaines tensions sont créatives et nécessaires.""",
        'weekly_advice': {
            'week_1': "Identifie une polarité en conflit en toi.",
            'week_2': "Écoute chaque partie avec équanimité.",
            'week_3': "Trouve une voie médiane qui honore les deux.",
            'week_4': "Célèbre la paix intérieure que tu as créée."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Phénix spirituel**

Ta Lune en Sagittaire en Maison 12 cherche le sens ultime. Ton Ascendant Scorpion ajoute intensité et pouvoir transformateur. Tu explores les abîmes pour renaître complètement.

**Domaine activé** : Maison 12 — Ton inconscient demande une transformation radicale. Tu plonges dans tes zones les plus sombres pour en extraire la sagesse et mourir à qui tu étais.

**Ton approche instinctive** : Le Scorpion te fait explorer sans compromis. Tu vas jusqu'au bout de ta quête intérieure, tu ne recules devant aucune vérité, aussi difficile soit-elle.

**Tensions possibles** : L'intensité peut devenir obsession. Tu risques de te perdre dans les profondeurs ou de forcer des transformations non naturelles.

**Conseil clé** : Faire confiance au timing de ta renaissance spirituelle.""",
        'weekly_advice': {
            'week_1': "Plonge dans ta zone d'ombre la plus effrayante.",
            'week_2': "Laisse mourir ce qui ne sert plus ton évolution.",
            'week_3': "Accepte la vulnérabilité du processus.",
            'week_4': "Émerge transformé·e avec une sagesse profonde."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Pèlerinage intérieur**

Triple Sagittaire sur ton inconscient : Lune, Maison 12, Ascendant. L'énergie est pure quête spirituelle, foi absolue en un sens transcendant. Ton monde intérieur est un univers à explorer.

**Domaine activé** : Maison 12 — Ta vie ENTIÈRE est un pèlerinage vers la vérité ultime. Tu explores ton inconscient avec la même foi que tu explorerais le monde, cherchant l'illumination.

**Ton approche instinctive** : Avec l'Ascendant Sagittaire, tu vis ta spiritualité avec optimisme total. Tu crois en l'expansion infinie de la conscience, tu explores sans peur.

**Tensions possibles** : L'excès peut créer des illusions spirituelles. Tu risques de fuir la réalité dans des croyances irréalistes ou de chercher éternellement sans jamais t'incarner.

**Conseil clé** : Intégrer ta sagesse spirituelle dans la vie concrète.""",
        'weekly_advice': {
            'week_1': "Pars en retraite spirituelle, physique ou mentale.",
            'week_2': "Explore une tradition mystique avec foi.",
            'week_3': "Vérifie que tu ne fuis pas la vie incarnée.",
            'week_4': "Ramène tes insights dans ton quotidien."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Maîtrise spirituelle**

Ta Lune en Sagittaire en Maison 12 cherche le sens spirituel. Ton Ascendant Capricorne ajoute discipline et ambition même dans l'exploration intérieure. Tu veux maîtriser ton inconscient.

**Domaine activé** : Maison 12 — Ton monde intérieur demande structure et engagement. Tu explores ton inconscient avec la rigueur d'une pratique spirituelle sérieuse, tu construis ta sagesse pierre par pierre.

**Ton approche instinctive** : Le Capricorne te fait aborder la spiritualité avec maturité. Tu es prêt·e à faire le travail difficile de l'introspection, à accepter les responsabilités de ta croissance.

**Tensions possibles** : Le contrôle peut bloquer la dissolution nécessaire. Tu risques de vouloir gérer ton inconscient au lieu de t'y abandonner.

**Conseil clé** : Discipliner ta pratique tout en lâchant prise sur les résultats.""",
        'weekly_advice': {
            'week_1': "Définis une pratique spirituelle rigoureuse.",
            'week_2': "Travaille sur toi avec discipline et patience.",
            'week_3': "Accepte de ne pas tout contrôler.",
            'week_4': "Apprécie la maîtrise intérieure que tu développes."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Conscience collective**

Ta Lune en Sagittaire en Maison 12 cherche le sens spirituel. Ton Ascendant Verseau ajoute conscience humaniste et innovation. Tu explores ton inconscient pour libérer l'humanité.

**Domaine activé** : Maison 12 — Ton monde intérieur se connecte à l'inconscient collectif. Tu explores les archétypes universels, tu cherches une spiritualité qui transcende l'individu.

**Ton approche instinctive** : Le Verseau te fait aborder la spiritualité avec originalité. Tu explores des paradigmes nouveaux, tu t'intéresses aux dimensions technologiques ou futuristes de la conscience.

**Tensions possibles** : Le détachement peut créer la déconnexion. Tu risques de te perdre dans l'abstrait ou de négliger ta guérison personnelle.

**Conseil clé** : Honorer ton humanité individuelle tout en servant le collectif.""",
        'weekly_advice': {
            'week_1': "Explore des pratiques spirituelles avant-gardistes.",
            'week_2': "Connecte-toi à l'inconscient collectif en méditation.",
            'week_3': "Vérifie que tu n'évites pas ton vécu personnel.",
            'week_4': "Partage tes insights pour le bien commun."
        }
    },

    {
        'moon_sign': 'Sagittarius', 'moon_house': 12, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution mystique**

Ta Lune en Sagittaire en Maison 12 cherche le sens ultime. Ton Ascendant Poissons ajoute perméabilité et connexion au divin. Tu te dissous dans l'océan spirituel, cherchant l'union totale.

**Domaine activé** : Maison 12 — Ton inconscient devient portail vers le transcendant. Tu explores les dimensions mystiques, tu cherches à dissoudre l'ego dans l'unité cosmique. La spiritualité est ton élément naturel.

**Ton approche instinctive** : Le Poissons te fait vivre ta spiritualité par l'expérience directe. Tu médites profondément, tu ressens l'unité, tu t'abandonnes au flow divin.

**Tensions possibles** : La dissolution peut devenir perte. Tu risques de te perdre complètement, d'être submergé·e, ou de confondre échappement et transcendance.

**Conseil clé** : S'ouvrir à l'infini tout en maintenant un minimum d'ancrage.""",
        'weekly_advice': {
            'week_1': "Médite sur l'union mystique avec le tout.",
            'week_2': "Pratique la compassion universelle.",
            'week_3': "Vérifie que tu ne te perds pas complètement.",
            'week_4': "Ramène doucement ta conscience vers le monde incarné."
        }
    },

]

if __name__ == "__main__":
    print(f"[*] Batch complet: Sagittarius - {len(BATCH)} interprétations générées")
    asyncio.run(insert_batch(BATCH))
