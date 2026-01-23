"""Batch complet: Gemini - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # ==================== MAISON 1 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Esprit guerrier**

Ce mois-ci, ta Lune en Gémeaux en Maison 1 active ton besoin de communiquer, d'apprendre, de bouger constamment. Avec l'Ascendant lunaire Bélier, cette énergie mentale devient combative : tu veux convaincre, débattre, prouver que tu as raison. Tes mots deviennent des armes.

**Domaine activé** : Maison 1 — Ton identité personnelle passe par l'intellect et la communication. Tu te définis par ta vivacité d'esprit, ta curiosité, ta capacité à jongler avec les idées. Tu veux être reconnu·e pour ton intelligence.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu communiques de manière directe et sans filtre. Tu n'as pas peur de la confrontation verbale. Cette franchise peut rafraîchir ou brusquer selon les interlocuteurs.

**Tensions possibles** : Trop d'agressivité verbale peut créer des conflits inutiles. Tu risques de parler avant de réfléchir, de blesser avec tes mots sans t'en rendre compte.

**Conseil clé** : Utiliser ta vivacité intellectuelle pour inspirer plutôt que pour combattre.""",
        'weekly_advice': {
            'week_1': "Initie une conversation importante avec courage.",
            'week_2': "Défends tes idées mais écoute aussi les autres.",
            'week_3': "Tempère ta franchise pour ne pas blesser inutilement.",
            'week_4': "Célèbre ta capacité à penser vite et à t'adapter."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Parole ancrée**

Ta Lune en Gémeaux en Maison 1 te pousse à communiquer et à explorer mille sujets. Ton Ascendant lunaire Taureau tempère cette agitation mentale : tu veux que tes mots aient du poids, que tes idées soient concrètes et utiles.

**Domaine activé** : Maison 1 — Ton identité oscille entre légèreté intellectuelle et besoin de stabilité. Tu cherches à te montrer à la fois curieux·se et fiable, mental·e et ancré·e.

**Ton approche instinctive** : Le Taureau te fait réfléchir avant de parler. Tu pèses tes mots, tu veux qu'ils aient de la substance. Cette prudence peut frustrer ton besoin gémeau de spontanéité.

**Tensions possibles** : Le conflit entre vitesse mentale et lenteur de parole crée une friction interne. Tu peux te sentir bloqué·e entre le besoin de tout dire et celui de ne dire que l'essentiel.

**Conseil clé** : Parler moins mais mieux, en donnant du poids à chaque mot.""",
        'weekly_advice': {
            'week_1': "Identifie les idées qui méritent vraiment d'être partagées.",
            'week_2': "Prends le temps de formuler ta pensée avec clarté.",
            'week_3': "Privilégie la qualité sur la quantité dans tes échanges.",
            'week_4': "Savoure la solidité des liens créés par tes mots."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Mental pur**

Triple air : Lune en Gémeaux, Maison 1, Ascendant Gémeaux. Ce mois-ci, tu es pure énergie mentale. Ta curiosité est à son maximum, ton besoin de communiquer intense, ton identité entièrement tournée vers l'intellect et l'échange.

**Domaine activé** : Maison 1 — Ton identité personnelle est intellectuelle. Tu te définis par ce que tu sais, ce que tu apprends, comment tu communiques. Ton esprit est ton principal outil d'existence.

**Ton approche instinctive** : Double Gémeaux te fait papillonner constamment. Tu peux avoir dix conversations simultanées, lire trois livres en même temps, explorer mille sujets. Cette versatilité est fascinante mais épuisante.

**Tensions possibles** : La dispersion mentale peut t'empêcher de vraiment approfondir quoi que ce soit. Tu risques de survoler ta propre vie sans jamais t'ancrer nulle part.

**Conseil clé** : Choisir consciemment quelques domaines d'exploration ce mois-ci et y plonger vraiment.""",
        'weekly_advice': {
            'week_1': "Liste tout ce qui t'intéresse, puis sélectionne l'essentiel.",
            'week_2': "Approfondis un sujet au lieu d'en effleurer dix.",
            'week_3': "Autorise-toi des moments de silence mental.",
            'week_4': "Mesure ce que tu as vraiment intégré versus juste survolé."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Intelligence sensible**

Ta Lune en Gémeaux en Maison 1 te donne une identité intellectuelle et curieuse. Ton Ascendant Cancer ajoute profondeur émotionnelle : tes pensées sont chargées de sentiments, tes mots portent de la vulnérabilité.

**Domaine activé** : Maison 1 — Ton identité cherche à intégrer mental et émotionnel. Tu veux communiquer mais avec authenticité, apprendre mais sur ce qui touche ton cœur.

**Ton approche instinctive** : Le Cancer te fait communiquer par vagues émotionnelles. Tu peux être bavard·e puis silencieux·se selon ton état intérieur. Cette sensibilité dans les mots crée de l'intimité.

**Tensions possibles** : Tu risques de prendre les remarques intellectuelles trop à cœur. La légèreté du Gémeaux peut se heurter à ta sensibilité cancérienne.

**Conseil clé** : Honorer à la fois ton besoin de légèreté mentale et ta profondeur émotionnelle.""",
        'weekly_advice': {
            'week_1': "Partage tes pensées les plus vulnérables avec quelqu'un de confiance.",
            'week_2': "Apprends sur des sujets qui touchent ton cœur.",
            'week_3': "Protège ta sensibilité sans t'isoler intellectuellement.",
            'week_4': "Célèbre ta capacité à penser ET à ressentir profondément."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Brillance expressive**

Ta Lune en Gémeaux en Maison 1 te rend curieux·se et communicatif·ve. Ton Ascendant Lion ajoute théâtralité et besoin de briller : tu veux que tes idées soient remarquées, que ta parole soit écoutée, que ton intelligence soit reconnue.

**Domaine activé** : Maison 1 — Ton identité cherche la reconnaissance intellectuelle. Tu veux être admiré·e pour ta vivacité d'esprit, ta capacité à captiver par les mots, ton charisme mental.

**Ton approche instinctive** : Le Lion te fait communiquer avec flair et générosité. Tu sais raconter des histoires, captiver une audience. Cette présence peut inspirer mais aussi sembler narcissique.

**Tensions possibles** : Le besoin de briller peut te pousser à monopoliser la parole. Tu risques de parler pour impressionner plutôt que pour échanger vraiment.

**Conseil clé** : Utiliser ton charisme pour élever les conversations, pas juste pour te mettre en avant.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment exprimer au monde.",
            'week_2': "Partage tes idées avec générosité et authenticité.",
            'week_3': "Laisse aussi de l'espace aux autres pour briller.",
            'week_4': "Célèbre l'impact positif de ta parole sur les autres."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision mentale**

Ta Lune en Gémeaux en Maison 1 active ton intellect et ta curiosité. Ton Ascendant Vierge canalise cette énergie mentale vers l'analyse et le perfectionnement : tu veux comprendre en détail, communiquer avec précision, apprendre de manière méthodique.

**Domaine activé** : Maison 1 — Ton identité est intellectuelle et analytique. Tu te définis par ta capacité à discerner, à améliorer, à peaufiner ta pensée et ta communication.

**Ton approche instinctive** : La Vierge te fait analyser chaque mot, chaque idée. Tu veux être exact·e, utile, constructif·ve dans ta communication. Cette exigence peut enrichir ou paralyser.

**Tensions possibles** : Le perfectionnisme peut t'empêcher de communiquer spontanément. Tu risques de trop réfléchir avant de parler, perdant la légèreté gémeau.

**Conseil clé** : Viser l'excellence intellectuelle sans tomber dans la paralysie analytique.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine de connaissance à perfectionner.",
            'week_2': "Apprends de manière structurée et rigoureuse.",
            'week_3': "Autorise-toi aussi à penser de manière plus libre.",
            'week_4': "Apprécie la qualité de ta pensée affinée."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomatie mentale**

Ta Lune en Gémeaux en Maison 1 te rend communicatif·ve et intellectuellement curieux·se. Ton Ascendant Balance ajoute recherche d'harmonie : tu veux que tes échanges créent du lien, que tes idées rassemblent, que ta parole soit équilibrée.

**Domaine activé** : Maison 1 — Ton identité passe par la relation intellectuelle. Tu te définis par ta capacité à créer des ponts, à voir tous les angles, à communiquer de manière juste et élégante.

**Ton approche instinctive** : La Balance te fait peser chaque argument, chercher le consensus. Tu veux plaire tout en restant intellectuellement honnête. Cette diplomatie peut faciliter ou édulcorer tes échanges.

**Tensions possibles** : Le besoin de plaire peut te faire taire tes vraies opinions. Tu risques de papillonner intellectuellement pour éviter les conflits nécessaires.

**Conseil clé** : Chercher l'harmonie sans sacrifier ta vérité intellectuelle.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te censures pour plaire.",
            'week_2': "Exprime tes vraies opinions avec tact mais fermeté.",
            'week_3': "Crée du lien tout en restant authentique.",
            'week_4': "Célèbre ta capacité à unir par la parole."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Mental profond**

Ta Lune en Gémeaux en Maison 1 te pousse à la légèreté intellectuelle et à la curiosité variée. Ton Ascendant Scorpion ajoute intensité et profondeur : tu veux comprendre les mystères, percer les secrets, aller au-delà des apparences mentales.

**Domaine activé** : Maison 1 — Ton identité oscille entre légèreté et profondeur intellectuelle. Tu cherches à être à la fois curieux·se de tout et capable de vraiment sonder l'essence des choses.

**Ton approche instinctive** : Le Scorpion te fait creuser sous la surface. Tu ne te contentes pas des réponses faciles. Cette intensité peut transformer ta curiosité gémeau en véritable investigation.

**Tensions possibles** : L'obsession intellectuelle peut remplacer la légèreté. Tu risques de voir des complots partout ou de perdre la joie simple de la découverte.

**Conseil clé** : Honorer ta profondeur tout en gardant la légèreté de la curiosité.""",
        'weekly_advice': {
            'week_1': "Choisis un mystère ou une question profonde à explorer.",
            'week_2': "Creuse en profondeur sans devenir obsessionnel·le.",
            'week_3': "Autorise-toi aussi des moments de légèreté mentale.",
            'week_4': "Intègre tes découvertes profondes avec sagesse."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Esprit explorateur**

Ta Lune en Gémeaux en Maison 1 te rend intellectuellement curieux·se et communicatif·ve. Ton Ascendant Sagittaire amplifie cette soif de connaissance : tu veux explorer des philosophies, des cultures, des horizons mentaux toujours plus vastes.

**Domaine activé** : Maison 1 — Ton identité est celle d'un·e éternel·le étudiant·e du monde. Tu te définis par ta quête de sens, ta capacité à relier des idées diverses, ton ouverture intellectuelle.

**Ton approche instinctive** : Le Sagittaire te fait voir grand. Tu ne te contentes pas de détails, tu veux comprendre les grands principes. Cette vision peut élargir ou disperser ton énergie gémeau.

**Tensions possibles** : Trop d'ampleur intellectuelle peut te faire perdre le contact avec le concret. Tu risques de philosopher sans jamais appliquer tes idées.

**Conseil clé** : Explorer largement tout en ancrant quelques idées dans ta vie concrète.""",
        'weekly_advice': {
            'week_1': "Identifie une grande question philosophique qui te passionne.",
            'week_2': "Explore-la à travers différentes perspectives culturelles.",
            'week_3': "Connecte tes découvertes à ta vie quotidienne.",
            'week_4': "Partage ta vision élargie avec générosité."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Intelligence stratégique**

Ta Lune en Gémeaux en Maison 1 te rend curieux·se et mental·e. Ton Ascendant Capricorne canalise cette énergie vers l'utilité et l'ambition : tu veux apprendre ce qui sert, communiquer pour construire, développer une expertise reconnue.

**Domaine activé** : Maison 1 — Ton identité intellectuelle cherche la maîtrise et la reconnaissance professionnelle. Tu veux être pris·e au sérieux, développer une autorité basée sur tes connaissances.

**Ton approche instinctive** : Le Capricorne te fait structurer ta pensée. Tu veux que tes idées soient solides, applicables, utiles professionnellement. Cette discipline peut canaliser ou rigidifier ton esprit gémeau.

**Tensions possibles** : La peur du jugement peut te faire taire tes idées les plus créatives. Tu risques de privilégier le conventionnel au détriment de l'originalité.

**Conseil clé** : Construire une expertise solide sans étouffer ta curiosité naturelle.""",
        'weekly_advice': {
            'week_1': "Identifie le domaine où tu veux développer une vraie maîtrise.",
            'week_2': "Apprends de manière structurée et progressive.",
            'week_3': "Autorise-toi aussi des explorations non-utilitaires.",
            'week_4': "Mesure les fondations intellectuelles que tu as posées."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Génie connecté**

Ta Lune en Gémeaux en Maison 1 active ton intellect et ta communication. Ton Ascendant Verseau ajoute innovation et vision collective : tu veux penser différemment, connecter les esprits, contribuer à l'intelligence collective.

**Domaine activé** : Maison 1 — Ton identité est celle d'un·e innovateur·rice intellectuel·le. Tu te définis par ton originalité mentale, ta capacité à voir l'avenir, à connecter des idées que personne n'avait reliées.

**Ton approche instinctive** : Le Verseau te fait penser hors des sentiers battus. Tu es attiré·e par les idées avant-gardistes, les technologies nouvelles, les concepts révolutionnaires. Cette originalité est ta marque.

**Tensions possibles** : Trop d'excentricité intellectuelle peut te déconnecter du réel. Tu risques de vivre uniquement dans les concepts sans incarnation.

**Conseil clé** : Innover intellectuellement tout en restant relié·e aux vraies personnes.""",
        'weekly_advice': {
            'week_1': "Explore une idée ou une technologie d'avant-garde.",
            'week_2': "Connecte-toi à des esprits innovants et visionnaires.",
            'week_3': "Partage tes idées originales avec la communauté.",
            'week_4': "Vérifie que ton innovation sert vraiment le collectif."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Pensée intuitive**

Ta Lune en Gémeaux en Maison 1 te donne une identité intellectuelle et curieuse. Ton Ascendant Poissons ajoute intuition et fluidité : ta pensée devient poétique, ta communication porte une dimension spirituelle ou artistique.

**Domaine activé** : Maison 1 — Ton identité oscille entre mental et mystique. Tu cherches à exprimer l'ineffable, à communiquer ce qui se situe au-delà des mots, à penser avec ton âme autant qu'avec ton esprit.

**Ton approche instinctive** : Le Poissons te fait communiquer par symboles, métaphores, ressentis. Ta pensée n'est pas linéaire mais associative et intuitive. Cette fluidité peut inspirer ou confondre.

**Tensions possibles** : La confusion mentale peut remplacer la clarté gémeau. Tu risques de te perdre dans tes pensées ou de ne plus savoir ce qui est réel.

**Conseil clé** : Honorer ton intuition tout en gardant un ancrage mental minimal.""",
        'weekly_advice': {
            'week_1': "Explore tes pensées par l'écriture libre ou l'art.",
            'week_2': "Fais confiance à ton intuition dans ta communication.",
            'week_3': "Garde quand même des points de repère logiques clairs.",
            'week_4': "Intègre tes insights mystiques avec discernement."
        }
    },

    # ==================== MAISON 2 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Valeur agile**

Ta Lune en Gémeaux active la Maison 2 : tes ressources et ta sécurité matérielle passent par l'intellect et la communication. Avec l'Ascendant Bélier, tu veux gagner de l'argent rapidement avec tes idées, monétiser ton intelligence sans attendre.

**Domaine activé** : Maison 2 — Tes revenus, ta valeur personnelle sont liés à ta capacité à communiquer, enseigner, vendre des idées. Tu veux plusieurs sources de revenus, de la variété financière.

**Ton approche instinctive** : Le Bélier te pousse à foncer sur les opportunités financières. Tu n'as pas peur de prendre des risques avec tes ressources pour tester de nouvelles idées.

**Tensions possibles** : L'impulsivité financière peut créer de l'instabilité. Tu risques de disperser ton énergie sur trop de projets sans construire de vraie sécurité.

**Conseil clé** : Utiliser ton agilité intellectuelle pour créer des revenus tout en construisant une base stable.""",
        'weekly_advice': {
            'week_1': "Identifie comment monétiser une de tes compétences intellectuelles.",
            'week_2': "Lance une initiative concrète pour générer des revenus.",
            'week_3': "Diversifie sans te disperser complètement.",
            'week_4': "Fais le point sur la stabilité de tes sources de revenus."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Intelligence pratique**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par l'intellect et la communication. Ton Ascendant Taureau, maître naturel de cette maison, apporte pragmatisme : tu veux que tes idées rapportent concrètement, durablement.

**Domaine activé** : Maison 2 — Tes ressources cherchent à la fois variété intellectuelle et solidité matérielle. Tu veux des revenus multiples mais stables, gagner avec ton esprit tout en construisant du durable.

**Ton approche instinctive** : Le Taureau te fait évaluer la vraie valeur de tes compétences. Tu veux être payé·e à ta juste valeur, construire un patrimoine de connaissances monnayables.

**Tensions possibles** : Le conflit entre désir de variété et besoin de stabilité peut te bloquer. Tu risques de te disperser ou au contraire de te rigidifier par peur du changement.

**Conseil clé** : Construire une base financière solide avec quelques compétences clés bien développées.""",
        'weekly_advice': {
            'week_1': "Identifie 2-3 compétences vraiment monnayables.",
            'week_2': "Investis du temps pour les perfectionner.",
            'week_3': "Commence à les monétiser de manière concrète.",
            'week_4': "Savoure la sécurité que tes talents créent."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Revenus multiples**

Double Gémeaux sur la Maison 2 : tes ressources et ta sécurité matérielle sont entièrement liées à ta polyvalence intellectuelle. Tu veux plusieurs sources de revenus, plusieurs talents monétisés, une sécurité financière basée sur la variété.

**Domaine activé** : Maison 2 — Tes revenus passent par la communication, l'enseignement, le commerce, les échanges. Tu ne peux pas dépendre d'une seule source, tu as besoin de diversité pour te sentir en sécurité.

**Ton approche instinctive** : Double Gémeaux te fait jongler avec plusieurs projets financiers. Tu peux travailler comme freelance, avoir plusieurs clients, diversifier tes compétences monnayables.

**Tensions possibles** : La dispersion peut t'empêcher de vraiment développer une expertise lucrative. Tu risques de papillonner financièrement sans jamais construire de vraie richesse.

**Conseil clé** : Diversifier intelligemment sans perdre toute cohérence dans tes sources de revenus.""",
        'weekly_advice': {
            'week_1': "Liste toutes tes compétences potentiellement monnayables.",
            'week_2': "Choisis 3-4 qui se complètent bien.",
            'week_3': "Développe-les de manière coordonnée.",
            'week_4': "Mesure le revenu réel généré par chacune."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sécurité communicative**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par l'intellect. Ton Ascendant Cancer ajoute besoin de sécurité émotionnelle : tu veux gagner de l'argent avec ce qui nourrit ton cœur, travailler dans la communication mais avec authenticité.

**Domaine activé** : Maison 2 — Tes ressources cherchent à la fois variété intellectuelle et sécurité émotionnelle. Tu veux que ton travail te permette de prendre soin de toi et des tiens.

**Ton approche instinctive** : Le Cancer te fait investir émotionnellement dans tes sources de revenus. Tu as besoin de te sentir en sécurité affective dans ton travail, pas juste financièrement.

**Tensions possibles** : La peur de manquer peut te faire t'accrocher à des revenus qui ne te nourrissent plus intellectuellement. Tu risques d'osciller entre aventure et conservatisme.

**Conseil clé** : Créer des revenus qui nourrissent à la fois ton esprit et ton cœur.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te sécurise vraiment financièrement.",
            'week_2': "Développe des compétences qui ont du sens pour toi.",
            'week_3': "Protège ta sécurité sans t'emprisonner dedans.",
            'week_4': "Apprécie l'équilibre entre sécurité et stimulation."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Valeur brillante**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par l'intellect et la communication. Ton Ascendant Lion ajoute besoin de reconnaissance : tu veux être payé·e pour ton talent, que ta valeur soit reconnue publiquement.

**Domaine activé** : Maison 2 — Tes ressources passent par ta capacité à briller intellectuellement. Tu veux que ton intelligence soit admirée ET rémunérée, que ton talent de communication te rapporte de la richesse.

**Ton approche instinctive** : Le Lion te pousse à valoriser tes compétences avec fierté. Tu n'as pas peur de demander ce que tu vaux, de te mettre en avant pour vendre tes talents.

**Tensions possibles** : L'orgueil peut te faire surestimer ta valeur marchande. Tu risques de refuser des opportunités parce qu'elles ne flattent pas assez ton ego.

**Conseil clé** : Valoriser tes talents avec confiance tout en restant réaliste sur le marché.""",
        'weekly_advice': {
            'week_1': "Identifie tes talents uniques qui méritent d'être rémunérés.",
            'week_2': "Présente-toi avec confiance pour des opportunités.",
            'week_3': "Demande ce que tu vaux sans arrogance.",
            'week_4': "Célèbre les revenus générés par ton talent."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Expertise utile**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par l'intellect. Ton Ascendant Vierge canalise cette énergie vers le service et la compétence : tu veux développer une expertise réelle, être payé·e pour des compétences concrètes et utiles.

**Domaine activé** : Maison 2 — Tes ressources passent par ton perfectionnement professionnel. Tu veux maîtriser des techniques, des savoirs pratiques qui se monétisent bien et servent vraiment.

**Ton approche instinctive** : La Vierge te fait analyser quelle compétence développer pour maximiser ta valeur. Tu investis dans ta formation, tu perfectionnes tes techniques avec méthode.

**Tensions possibles** : Le perfectionnisme peut te bloquer dans la monétisation. Tu risques de penser que tu n'es jamais assez bon·ne pour faire payer tes services.

**Conseil clé** : Perfectionner tes compétences tout en acceptant de les monétiser dès maintenant.""",
        'weekly_advice': {
            'week_1': "Identifie une compétence utile à développer ou perfectionner.",
            'week_2': "Forme-toi de manière structurée et rigoureuse.",
            'week_3': "Commence à offrir tes services même imparfaitement.",
            'week_4': "Mesure la valeur réelle créée par ton expertise."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Valeur harmonieuse**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par la communication. Ton Ascendant Balance ajoute dimension esthétique et relationnelle : tu veux gagner de l'argent dans la beauté, l'harmonie, les partenariats équilibrés.

**Domaine activé** : Maison 2 — Tes ressources passent par ta capacité à créer du lien, de la beauté, de l'équilibre. Tu peux monétiser ton sens esthétique, ta diplomatie, ton talent pour les relations.

**Ton approche instinctive** : La Balance te fait chercher des collaborations financières équitables. Tu veux créer de la valeur avec d'autres, dans l'harmonie et la justice.

**Tensions possibles** : Le besoin de plaire peut te faire sous-évaluer tes services. Tu risques d'accepter des revenus insuffisants pour maintenir l'harmonie relationnelle.

**Conseil clé** : Créer de belles collaborations tout en défendant ta juste valeur.""",
        'weekly_advice': {
            'week_1': "Identifie des partenariats potentiellement lucratifs.",
            'week_2': "Négocie des accords équitables et clairs.",
            'week_3': "Utilise ton sens esthétique pour créer de la valeur.",
            'week_4': "Apprécie l'harmonie dans tes relations financières."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Richesse stratégique**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par l'intellect. Ton Ascendant Scorpion ajoute intensité et stratégie : tu veux comprendre les secrets de la richesse, développer une expertise rare et puissante.

**Domaine activé** : Maison 2 — Tes ressources passent par ta capacité à voir ce que les autres ne voient pas. Tu peux monétiser ton analyse profonde, ta compréhension des dynamiques cachées.

**Ton approche instinctive** : Le Scorpion te fait investir intensément dans le développement de compétences rares. Tu n'as pas peur de plonger dans des domaines complexes pour maîtriser quelque chose d'unique.

**Tensions possibles** : L'obsession financière peut remplacer la légèreté. Tu risques de devenir calculateur·rice au point de perdre la joie de l'échange.

**Conseil clé** : Développer une expertise puissante tout en gardant l'éthique de l'échange.""",
        'weekly_advice': {
            'week_1': "Identifie une niche où tu peux devenir expert·e.",
            'week_2': "Plonge en profondeur dans ce domaine.",
            'week_3': "Développe une stratégie de monétisation puissante.",
            'week_4': "Vérifie que ta quête de richesse reste alignée."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Abondance intellectuelle**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par l'intellect. Ton Ascendant Sagittaire amplifie cette vision : tu veux gagner de l'argent en enseignant, en partageant ta philosophie, en inspirant à grande échelle.

**Domaine activé** : Maison 2 — Tes ressources passent par ta capacité à voir grand et à partager ta vision. Tu peux monétiser ton enseignement, tes voyages, ton ouverture culturelle.

**Ton approche instinctive** : Le Sagittaire te fait avoir confiance en l'abondance. Tu crois que l'univers pourvoira si tu suis ta vérité. Cette foi peut attirer ou créer de l'irresponsabilité.

**Tensions possibles** : Trop d'optimisme financier peut créer de l'instabilité. Tu risques de dépenser avant de gagner ou de manquer de pragmatisme.

**Conseil clé** : Viser l'abondance avec foi tout en restant ancré·e dans la réalité financière.""",
        'weekly_advice': {
            'week_1': "Identifie comment partager ta vision de manière lucrative.",
            'week_2': "Développe une offre d'enseignement ou de coaching.",
            'week_3': "Garde les pieds sur terre dans ta gestion financière.",
            'week_4': "Célèbre l'abondance créée par ton inspiration."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Capital intellectuel**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par l'intellect. Ton Ascendant Capricorne structure cette énergie : tu veux construire un patrimoine de compétences, développer une expertise qui te donne autorité et revenus solides.

**Domaine activé** : Maison 2 — Tes ressources cherchent la reconnaissance professionnelle. Tu veux que tes connaissances soient respectées, que ton expertise intellectuelle te rapporte durablement.

**Ton approche instinctive** : Le Capricorne te fait investir patiemment dans ton développement professionnel. Tu construis ta valeur méthodiquement, avec ambition à long terme.

**Tensions possibles** : La rigidité peut t'empêcher d'explorer de nouvelles sources de revenus. Tu risques de t'enfermer dans un domaine par sécurité.

**Conseil clé** : Construire une expertise solide tout en gardant une curiosité ouverte.""",
        'weekly_advice': {
            'week_1': "Identifie le domaine où tu veux être reconnu·e comme expert·e.",
            'week_2': "Investis du temps et de l'argent dans ta formation.",
            'week_3': "Construis ta réputation méthodiquement.",
            'week_4': "Mesure les fondations professionnelles posées."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Revenus innovants**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par l'intellect. Ton Ascendant Verseau ajoute innovation : tu veux gagner de l'argent avec des idées nouvelles, des modèles économiques alternatifs, de la technologie.

**Domaine activé** : Maison 2 — Tes ressources passent par ton originalité et ton réseau. Tu peux monétiser ton innovation, ta capacité à connecter des esprits, ta vision d'avant-garde.

**Ton approche instinctive** : Le Verseau te fait expérimenter avec de nouvelles manières de gagner de l'argent. Tu n'as pas peur de tester des modèles non-conventionnels.

**Tensions possibles** : Trop d'expérimentation peut créer de l'instabilité financière. Tu risques de poursuivre l'originalité au détriment de la viabilité économique.

**Conseil clé** : Innover dans tes sources de revenus tout en gardant une base stable.""",
        'weekly_advice': {
            'week_1': "Explore de nouveaux modèles économiques ou technologies.",
            'week_2': "Teste une idée originale de monétisation.",
            'week_3': "Connecte-toi à des communautés qui partagent ta vision.",
            'week_4': "Vérifie la viabilité réelle de tes innovations."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Valeur intuitive**

Ta Lune en Gémeaux en Maison 2 veut créer de la valeur par l'intellect. Ton Ascendant Poissons ajoute intuition et fluidité : tu veux gagner de l'argent avec ce qui nourrit ton âme, monétiser ton inspiration créative ou spirituelle.

**Domaine activé** : Maison 2 — Tes ressources cherchent à intégrer mental et spirituel. Tu veux que ton travail ait du sens au-delà de l'argent, créer de la valeur qui soit aussi de la beauté.

**Ton approche instinctive** : Le Poissons te fait suivre ton intuition financière. Tu peux avoir du mal à valoriser tes talents ou au contraire avoir une foi totale en l'abondance.

**Tensions possibles** : Le manque de structure financière peut créer du chaos. Tu risques de te laisser exploiter ou de fuir la responsabilité matérielle.

**Conseil clé** : Honorer ton inspiration tout en maintenant une structure financière minimale.""",
        'weekly_advice': {
            'week_1': "Identifie comment monétiser ton inspiration créative.",
            'week_2': "Crée une structure simple pour gérer tes finances.",
            'week_3': "Fais confiance à ton intuition tout en restant réaliste.",
            'week_4': "Remercie l'abondance qui coule naturellement vers toi."
        }
    },

    # ==================== MAISON 3 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Communication fulgurante**

Double accent sur la communication : ta Lune en Gémeaux active sa maison naturelle (Maison 3), amplifiée par l'Ascendant Bélier. Tu veux parler vite, apprendre vite, convaincre avec force. Tes mots deviennent des actions directes.

**Domaine activé** : Maison 3 — Tes échanges quotidiens, tes apprentissages, ton environnement proche sont électrifiés. Tu as besoin de stimulation intellectuelle constante, de débats, de mouvements.

**Ton approche instinctive** : Le Bélier te fait communiquer sans filtre. Tu dis ce que tu penses instantanément, parfois de manière brutale. Cette franchise peut rafraîchir ou blesser.

**Tensions possibles** : Trop d'impulsivité verbale peut créer des conflits avec ton entourage. Tu risques de parler avant de réfléchir, de brusquer dans tes échanges.

**Conseil clé** : Utiliser ta vivacité verbale pour inspirer plutôt que pour attaquer.""",
        'weekly_advice': {
            'week_1': "Initie les conversations importantes sans les repousser.",
            'week_2': "Apprends quelque chose de complètement nouveau.",
            'week_3': "Tempère ta franchise pour ne pas blesser.",
            'week_4': "Célèbre tout ce que tu as découvert et échangé."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Parole posée**

Ta Lune en Gémeaux en Maison 3 veut communiquer et apprendre avec vivacité. Ton Ascendant Taureau tempère cette agitation : tu veux que tes mots aient du poids, que tes apprentissages soient concrets et durables.

**Domaine activé** : Maison 3 — Tes échanges et ta communication cherchent à la fois spontanéité et substance. Tu veux dire les choses clairement mais aussi qu'elles aient un impact réel.

**Ton approche instinctive** : Le Taureau te fait peser chaque mot avant de le prononcer. Tu peux être lent·e à répondre mais quand tu le fais, c'est réfléchi et solide.

**Tensions possibles** : La frustration monte quand tu dois répéter ou expliquer lentement. Le conflit entre vitesse mentale gémeau et lenteur taureau crée de la friction.

**Conseil clé** : Parler moins mais mieux, en donnant du poids et de la durée à chaque échange.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui mérite vraiment d'être appris ou dit.",
            'week_2': "Approfondis méthodiquement plutôt que de survoler.",
            'week_3': "Exprime tes idées avec clarté et fermeté.",
            'week_4': "Apprécie la solidité des connaissances intégrées."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Hyperconnexion mentale**

Triple Gémeaux : Lune, Maison 3, Ascendant. Ce mois-ci, tu es pure énergie communicative. Ton besoin d'échanger, d'apprendre, de bouger mentalement est à son maximum. Tu peux papillonner entre dix sujets, conversations, projets simultanément.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages sont au centre de tout. Tu vis dans les mots, les idées, les connexions intellectuelles. Ton environnement proche doit être stimulant.

**Ton approche instinctive** : Triple Gémeaux te fait jongler constamment. Tu peux lire plusieurs livres, suivre plusieurs formations, avoir des dizaines de conversations en parallèle. Cette agilité est fascinante.

**Tensions possibles** : La dispersion mentale extrême peut t'empêcher de vraiment intégrer quoi que ce soit. Tu risques de survoler tout sans rien approfondir.

**Conseil clé** : Choisir consciemment 2-3 domaines d'apprentissage ce mois-ci et s'y engager.""",
        'weekly_advice': {
            'week_1': "Liste tout ce qui t'intéresse, puis sélectionne l'essentiel.",
            'week_2': "Engage-toi à approfondir au lieu de survoler.",
            'week_3': "Autorise-toi des moments de silence et de digestion.",
            'week_4': "Mesure ce que tu as vraiment intégré versus juste consommé."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Communication du cœur**

Ta Lune en Gémeaux en Maison 3 veut échanger et apprendre intellectuellement. Ton Ascendant Cancer ajoute profondeur émotionnelle : tu veux des conversations qui touchent le cœur, apprendre ce qui nourrit ton âme.

**Domaine activé** : Maison 3 — Tes échanges quotidiens sont chargés d'émotion. Tu veux créer de l'intimité par la parole, partager des vulnérabilités, communiquer avec authenticité.

**Ton approche instinctive** : Le Cancer te fait communiquer par vagues selon ton état émotionnel. Tu peux être très bavard·e puis te retirer complètement. Cette sensibilité crée de la profondeur.

**Tensions possibles** : Tu risques de prendre les remarques trop à cœur ou de te fermer au moindre malaise. La légèreté gémeau se heurte à ta sensibilité.

**Conseil clé** : Honorer à la fois ton besoin de légèreté intellectuelle et ta profondeur émotionnelle.""",
        'weekly_advice': {
            'week_1': "Partage tes pensées les plus vulnérables avec confiance.",
            'week_2': "Apprends sur des sujets qui touchent ton cœur.",
            'week_3': "Protège ta sensibilité sans t'isoler intellectuellement.",
            'week_4': "Célèbre l'intimité créée par tes échanges authentiques."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Communication rayonnante**

Ta Lune en Gémeaux en Maison 3 veut communiquer et apprendre avec vivacité. Ton Ascendant Lion ajoute théâtralité : tu veux captiver par tes mots, briller dans tes échanges, être admiré·e pour ton intelligence.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages cherchent la reconnaissance. Tu veux que ta parole soit écoutée, que tes idées soient célébrées, que ton esprit soit apprécié.

**Ton approche instinctive** : Le Lion te fait communiquer avec générosité et flair. Tu sais raconter des histoires, captiver une audience. Cette présence magnétique peut inspirer.

**Tensions possibles** : Le besoin de briller peut te pousser à monopoliser la parole. Tu risques de parler pour impressionner plutôt que pour vraiment échanger.

**Conseil clé** : Utiliser ton charisme verbal pour élever les conversations, pas juste pour te mettre en avant.""",
        'weekly_advice': {
            'week_1': "Identifie le message important que tu veux transmettre.",
            'week_2': "Partage tes idées avec générosité et authenticité.",
            'week_3': "Laisse aussi de l'espace aux autres pour s'exprimer.",
            'week_4': "Célèbre l'impact positif de ta parole inspirante."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision communicative**

Ta Lune en Gémeaux en Maison 3 veut communiquer et apprendre avec agilité. Ton Ascendant Vierge canalise cette énergie vers la précision : tu veux dire exactement ce que tu penses, apprendre de manière méthodique et utile.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages cherchent l'exactitude. Tu veux communiquer clairement, apprendre des compétences concrètes, perfectionner ta pensée et ta parole.

**Ton approche instinctive** : La Vierge te fait analyser chaque mot, chaque idée. Tu veux être précis·e, utile, constructif·ve dans ta communication. Cette exigence enrichit tes échanges.

**Tensions possibles** : Le perfectionnisme peut paralyser ta communication spontanée. Tu risques de trop réfléchir avant de parler, perdant la légèreté gémeau.

**Conseil clé** : Viser la clarté et l'utilité tout en gardant la spontanéité de l'échange.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine où perfectionner ta communication.",
            'week_2': "Apprends de manière structurée et rigoureuse.",
            'week_3': "Autorise-toi aussi à penser et parler librement.",
            'week_4': "Apprécie la qualité de ta pensée affinée."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Dialogue harmonieux**

Ta Lune en Gémeaux en Maison 3 veut communiquer et échanger avec vivacité. Ton Ascendant Balance ajoute recherche d'harmonie : tu veux que tes échanges créent du lien, que tes mots rassemblent, que ta parole soit équilibrée.

**Domaine activé** : Maison 3 — Tes échanges quotidiens cherchent la beauté et la justice. Tu veux communiquer de manière élégante, créer des ponts entre les gens, faciliter la compréhension mutuelle.

**Ton approche instinctive** : La Balance te fait peser chaque argument, chercher le consensus dans tes échanges. Tu veux plaire tout en restant honnête intellectuellement.

**Tensions possibles** : Le besoin d'harmonie peut te faire taire tes vraies opinions. Tu risques d'édulcorer ta pensée pour éviter les conflits nécessaires.

**Conseil clé** : Chercher l'harmonie dans les échanges sans sacrifier ta vérité intellectuelle.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te censures pour maintenir la paix.",
            'week_2': "Exprime tes vraies opinions avec tact mais fermeté.",
            'week_3': "Crée du lien tout en restant authentique.",
            'week_4': "Célèbre ta capacité à unir par le dialogue."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Communication intense**

Ta Lune en Gémeaux en Maison 3 veut échanger légèrement et apprendre variablement. Ton Ascendant Scorpion ajoute profondeur : tu veux des conversations qui révèlent des vérités cachées, apprendre ce qui transforme.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages oscillent entre légèreté et intensité. Tu veux communiquer sur des sujets profonds, percer les mystères, aller au-delà des conversations superficielles.

**Ton approche instinctive** : Le Scorpion te fait creuser sous la surface de chaque échange. Tu poses des questions dérangeantes, tu veux comprendre les motivations cachées.

**Tensions possibles** : L'intensité peut effrayer dans les échanges quotidiens. Tu risques de voir des secrets partout ou de perdre la légèreté nécessaire à la communication fluide.

**Conseil clé** : Honorer ta profondeur tout en gardant la légèreté de la curiosité gémeau.""",
        'weekly_advice': {
            'week_1': "Choisis un sujet profond à explorer par l'échange.",
            'week_2': "Aie des conversations qui vont vraiment en profondeur.",
            'week_3': "Autorise-toi aussi des échanges légers et joyeux.",
            'week_4': "Intègre ce que tu as découvert dans tes interactions."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Curiosité infinie**

Ta Lune en Gémeaux en Maison 3 veut apprendre et communiquer avec agilité. Ton Ascendant Sagittaire amplifie cette soif : tu veux explorer des philosophies, des cultures, des horizons intellectuels toujours plus vastes.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages cherchent l'expansion. Tu veux apprendre sur tout, communiquer avec des gens de tous horizons, connecter des idées de différentes cultures.

**Ton approche instinctive** : Le Sagittaire te fait voir grand dans tes apprentissages. Tu ne te contentes pas de détails, tu veux comprendre les grands principes et les partager.

**Tensions possibles** : Trop d'ampleur peut créer de la dispersion extrême. Tu risques de survoler mille sujets sans jamais rien maîtriser vraiment.

**Conseil clé** : Explorer largement tout en ancrant quelques apprentissages en profondeur.""",
        'weekly_advice': {
            'week_1': "Identifie les grands thèmes qui te passionnent vraiment.",
            'week_2': "Explore-les à travers différentes perspectives.",
            'week_3': "Choisis-en un ou deux à vraiment approfondir.",
            'week_4': "Partage ta vision élargie avec générosité."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Communication stratégique**

Ta Lune en Gémeaux en Maison 3 veut communiquer et apprendre avec vivacité. Ton Ascendant Capricorne structure cette énergie : tu veux apprendre ce qui sert professionnellement, communiquer de manière autoritaire.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages cherchent l'utilité et la reconnaissance. Tu veux développer une expertise communicative, être pris·e au sérieux intellectuellement.

**Ton approche instinctive** : Le Capricorne te fait sélectionner rigoureusement ce que tu apprends. Tu veux que tes connaissances te donnent du pouvoir, de l'autorité, de la crédibilité.

**Tensions possibles** : La rigidité peut étouffer ta curiosité naturelle. Tu risques de ne plus explorer que ce qui est "utile", perdant la joie de l'apprentissage.

**Conseil clé** : Construire une expertise solide sans étouffer ta curiosité ludique.""",
        'weekly_advice': {
            'week_1': "Identifie les compétences communicatives stratégiques.",
            'week_2': "Apprends de manière structurée et ambitieuse.",
            'week_3': "Autorise-toi aussi des explorations non-utilitaires.",
            'week_4': "Mesure les fondations intellectuelles professionnelles posées."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Communication visionnaire**

Ta Lune en Gémeaux en Maison 3 veut échanger et apprendre avec agilité. Ton Ascendant Verseau ajoute innovation : tu veux communiquer différemment, apprendre sur l'avenir, connecter des esprits avant-gardistes.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages cherchent l'originalité. Tu veux explorer des idées nouvelles, utiliser des technologies de communication innovantes, penser l'avenir.

**Ton approche instinctive** : Le Verseau te fait expérimenter avec de nouvelles formes de communication et d'apprentissage. Tu es attiré·e par les concepts révolutionnaires, les réseaux alternatifs.

**Tensions possibles** : Trop d'excentricité peut te déconnecter de la communication ordinaire. Tu risques de devenir incompréhensible à force d'originalité.

**Conseil clé** : Innover dans ta communication tout en restant accessible et compréhensible.""",
        'weekly_advice': {
            'week_1': "Explore de nouvelles formes ou technologies de communication.",
            'week_2': "Connecte-toi à des esprits innovants et visionnaires.",
            'week_3': "Partage tes idées originales de manière claire.",
            'week_4': "Vérifie que ton innovation sert vraiment l'échange."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Parole poétique**

Ta Lune en Gémeaux en Maison 3 veut communiquer et apprendre intellectuellement. Ton Ascendant Poissons ajoute dimension poétique et intuitive : ta parole devient métaphorique, tes apprentissages passent par le ressenti.

**Domaine activé** : Maison 3 — Tes échanges et apprentissages oscillent entre mental et mystique. Tu veux communiquer l'ineffable, apprendre par symboles et synchronicités autant que par logique.

**Ton approche instinctive** : Le Poissons te fait communiquer par images, métaphores, ressentis. Ta pensée n'est pas linéaire mais associative et intuitive. Cette fluidité peut inspirer.

**Tensions possibles** : La confusion mentale peut remplacer la clarté gémeau. Tu risques de te perdre dans tes pensées ou de ne plus savoir communiquer clairement.

**Conseil clé** : Honorer ta dimension poétique tout en gardant un ancrage mental minimal.""",
        'weekly_advice': {
            'week_1': "Explore tes pensées par l'écriture créative ou poétique.",
            'week_2': "Fais confiance à ton intuition dans tes échanges.",
            'week_3': "Garde quand même des points de clarté logique.",
            'week_4': "Intègre tes insights mystiques avec discernement."
        }
    },

    # ==================== MAISON 4 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Foyer dynamique**

Ta Lune en Gémeaux active la Maison 4 : ton foyer et tes racines deviennent un espace de communication et de mouvement. Avec l'Ascendant Bélier, tu veux transformer ton chez-toi rapidement, créer un environnement stimulant.

**Domaine activé** : Maison 4 — Ton foyer, ta famille, tes fondations émotionnelles ont besoin de variété et de stimulation intellectuelle. Tu ne supportes pas un chez-toi statique ou ennuyeux.

**Ton approche instinctive** : Le Bélier te pousse à agir vite sur ton espace de vie. Tu peux déménager impulsivement, réaménager constamment, avoir besoin de changement dans ton cocon.

**Tensions possibles** : L'impulsivité peut créer de l'instabilité familiale ou résidentielle. Tu risques de manquer de vraie sécurité émotionnelle à force de bouger.

**Conseil clé** : Créer un foyer stimulant tout en maintenant une base de sécurité stable.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque de stimulation dans ton chez-toi.",
            'week_2': "Fais un changement concret dans ton espace de vie.",
            'week_3': "Crée des moments d'échange avec ta famille ou tes proches.",
            'week_4': "Ancre les nouvelles bases tout en gardant de la variété."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Racines communicantes**

Ta Lune en Gémeaux en Maison 4 veut un foyer intellectuellement stimulant. Ton Ascendant Taureau ajoute besoin de stabilité : tu veux un chez-toi confortable et sécurisant, mais aussi vivant et communicatif.

**Domaine activé** : Maison 4 — Ton foyer cherche à la fois variété intellectuelle et solidité matérielle. Tu veux pouvoir lire, apprendre, échanger chez toi, mais dans un cadre stable et beau.

**Ton approche instinctive** : Le Taureau te fait créer un foyer confortable et durable. Tu investis dans la qualité de ton espace de vie, tu veux que ce soit un vrai sanctuaire.

**Tensions possibles** : Le conflit entre besoin de changement (Gémeaux) et besoin de stabilité (Taureau) peut te bloquer. Tu oscilles entre réaménagement et conservatisme.

**Conseil clé** : Créer un foyer stable qui intègre de la variété et de la stimulation intellectuelle.""",
        'weekly_advice': {
            'week_1': "Identifie comment rendre ton chez-toi à la fois beau et stimulant.",
            'week_2': "Investis dans des livres, de l'art, des objets qui nourrissent ton esprit.",
            'week_3': "Crée des rituels de lecture ou d'apprentissage à la maison.",
            'week_4': "Savoure la richesse intellectuelle de ton cocon."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Maison bibliothèque**

Double Gémeaux sur la Maison 4 : ton foyer devient un espace entièrement dédié à l'intellect et à la communication. Tu veux vivre entouré·e de livres, d'idées, de possibilités d'apprentissage constant.

**Domaine activé** : Maison 4 — Ton chez-toi et tes fondations émotionnelles passent par le mental. Tu as besoin que ton foyer soit un lieu de stimulation intellectuelle, où tu peux lire, écrire, échanger librement.

**Ton approche instinctive** : Double Gémeaux te fait créer un foyer léger, flexible, peut-être un peu chaotique intellectuellement. Tu as des livres partout, des projets multiples en cours.

**Tensions possibles** : Le manque de vraie sécurité émotionnelle peut te rendre instable. Tu risques de fuir dans le mental au lieu de créer un vrai cocon affectif.

**Conseil clé** : Créer un foyer intellectuellement riche tout en nourrissant aussi tes besoins émotionnels.""",
        'weekly_advice': {
            'week_1': "Organise ton espace pour faciliter l'apprentissage et la créativité.",
            'week_2': "Crée des zones dédiées à différentes activités intellectuelles.",
            'week_3': "Autorise-toi aussi des moments de calme émotionnel chez toi.",
            'week_4': "Apprécie la richesse mentale de ton environnement."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Nid communicant**

Ta Lune en Gémeaux en Maison 4 veut un foyer stimulant intellectuellement. Ton Ascendant Cancer, maître naturel de cette maison, ajoute profondeur émotionnelle : tu veux un chez-toi où on peut à la fois échanger et se sentir en sécurité affective.

**Domaine activé** : Maison 4 — Ton foyer cherche à intégrer mental et émotionnel. Tu veux pouvoir parler de tout avec ta famille, mais aussi te sentir profondément nourri·e affectivement.

**Ton approche instinctive** : Le Cancer te fait créer un foyer chaleureux et protecteur. Tu veux que ton chez-toi soit un refuge émotionnel où la communication est libre et authentique.

**Tensions possibles** : Le conflit entre légèreté mentale et profondeur émotionnelle peut créer des malaises. Tu oscilles entre bavardage et retrait silencieux.

**Conseil clé** : Créer un foyer où mental et émotionnel cohabitent harmonieusement.""",
        'weekly_advice': {
            'week_1': "Identifie comment nourrir à la fois ton esprit et ton cœur chez toi.",
            'week_2': "Crée des moments d'échange authentique avec tes proches.",
            'week_3': "Autorise-toi aussi des moments de silence et de ressourcement.",
            'week_4': "Célèbre la richesse affective et intellectuelle de ton foyer."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Palais intellectuel**

Ta Lune en Gémeaux en Maison 4 veut un foyer stimulant. Ton Ascendant Lion ajoute besoin de beauté et de fierté : tu veux un chez-toi dont tu es fier·ère, qui reflète ton intelligence et ton goût.

**Domaine activé** : Maison 4 — Ton foyer devient une expression de ton identité intellectuelle. Tu veux que ton espace de vie soit à la fois stimulant mentalement et esthétiquement impressionnant.

**Ton approche instinctive** : Le Lion te fait créer un foyer chaleureux et généreux où tu aimes recevoir. Tu veux que ton chez-toi soit admiré, qu'il soit le théâtre de belles conversations.

**Tensions possibles** : L'orgueil peut te faire investir au-delà de tes moyens pour impressionner. Tu risques de privilégier l'apparence sur le vrai confort émotionnel.

**Conseil clé** : Créer un foyer beau et stimulant qui serve vraiment ton bien-être.""",
        'weekly_advice': {
            'week_1': "Identifie comment rendre ton chez-toi plus beau et inspirant.",
            'week_2': "Investis dans des objets qui élèvent ton espace intellectuellement.",
            'week_3': "Organise un moment d'échange stimulant chez toi.",
            'week_4': "Célèbre la fierté que tu ressens pour ton foyer."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Foyer fonctionnel**

Ta Lune en Gémeaux en Maison 4 veut un foyer intellectuellement riche. Ton Ascendant Vierge ajoute besoin d'ordre et d'efficacité : tu veux un chez-toi parfaitement organisé où tout a sa place et son utilité.

**Domaine activé** : Maison 4 — Ton foyer cherche à la fois stimulation intellectuelle et perfection fonctionnelle. Tu veux pouvoir apprendre et travailler efficacement chez toi dans un environnement impeccable.

**Ton approche instinctive** : La Vierge te fait organiser méticuleusement ton espace de vie. Chaque livre a sa place, chaque coin a sa fonction. Cette précision peut créer de la sérénité.

**Tensions possibles** : Le perfectionnisme peut te rendre anxieux·se chez toi. Tu risques de passer ton temps à ranger au lieu de vraiment te détendre.

**Conseil clé** : Créer un foyer organisé sans tomber dans l'obsession du contrôle.""",
        'weekly_advice': {
            'week_1': "Identifie comment optimiser ton espace pour le travail et l'apprentissage.",
            'week_2': "Organise méthodiquement ton foyer par zones fonctionnelles.",
            'week_3': "Autorise-toi aussi un peu de désordre créatif.",
            'week_4': "Apprécie la clarté et l'efficacité de ton environnement."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie communicative**

Ta Lune en Gémeaux en Maison 4 veut un foyer intellectuellement vivant. Ton Ascendant Balance ajoute recherche d'harmonie et de beauté : tu veux un chez-toi équilibré où règnent dialogue et esthétique.

**Domaine activé** : Maison 4 — Ton foyer cherche la paix dans la communication. Tu veux que ton espace de vie soit beau, équilibré, propice aux échanges harmonieux avec ta famille ou tes colocataires.

**Ton approche instinctive** : La Balance te fait créer un foyer élégant et accueillant. Tu aimes que ton chez-toi soit un lieu de partage, de dialogue, d'équilibre relationnel.

**Tensions possibles** : Le besoin d'harmonie peut te faire éviter les conversations difficiles mais nécessaires en famille. Tu risques de vivre dans une paix superficielle.

**Conseil clé** : Créer un foyer harmonieux tout en permettant l'authenticité des échanges.""",
        'weekly_advice': {
            'week_1': "Identifie comment améliorer l'harmonie dans ton espace de vie.",
            'week_2': "Embellis ton foyer pour qu'il soit plus apaisant.",
            'week_3': "Crée du dialogue authentique avec tes proches.",
            'week_4': "Célèbre l'équilibre et la beauté de ton environnement."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Sanctuaire secret**

Ta Lune en Gémeaux en Maison 4 veut un foyer intellectuellement stimulant. Ton Ascendant Scorpion ajoute profondeur et intimité : tu veux un chez-toi qui protège tes secrets, où tu peux explorer en profondeur.

**Domaine activé** : Maison 4 — Ton foyer oscille entre légèreté intellectuelle et intensité émotionnelle. Tu veux un espace privé où tu peux à la fois apprendre et te transformer loin des regards.

**Ton approche instinctive** : Le Scorpion te fait créer un foyer très privé, peut-être mystérieux. Tu choisis soigneusement qui tu invites dans ton espace intime. Cette sélectivité protège ton énergie.

**Tensions possibles** : L'isolement peut remplacer la communication. Tu risques de te couper des échanges familiaux par méfiance ou besoin de contrôle.

**Conseil clé** : Protéger ton intimité tout en maintenant des liens communicatifs authentiques.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux protéger dans ton foyer.",
            'week_2': "Crée un espace secret pour tes explorations profondes.",
            'week_3': "Autorise-toi aussi des échanges légers avec tes proches.",
            'week_4': "Intègre profondeur et légèreté dans ton cocon."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foyer mondial**

Ta Lune en Gémeaux en Maison 4 veut un foyer intellectuellement riche. Ton Ascendant Sagittaire amplifie cette vision : tu veux un chez-toi cosmopolite, ouvert sur le monde, où circulent idées et cultures diverses.

**Domaine activé** : Maison 4 — Ton foyer devient un carrefour culturel et intellectuel. Tu peux avoir des livres de partout, recevoir des gens d'horizons variés, vivre dans une atmosphère d'ouverture.

**Ton approche instinctive** : Le Sagittaire te fait créer un foyer généreux et expansif. Tu veux que ton chez-toi soit un lieu de liberté, d'exploration, de partage philosophique.

**Tensions possibles** : Le manque d'ancrage peut créer un sentiment de non-appartenance. Tu risques de ne jamais vraiment t'installer nulle part, toujours en quête d'ailleurs.

**Conseil clé** : Créer un foyer ouvert sur le monde tout en y trouvant un vrai ancrage.""",
        'weekly_advice': {
            'week_1': "Identifie comment ouvrir ton foyer à plus de diversité culturelle.",
            'week_2': "Intègre des éléments de différentes cultures dans ton espace.",
            'week_3': "Organise des échanges intellectuels ou culturels chez toi.",
            'week_4': "Ancre-toi dans cette richesse tout en restant enraciné·e."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fondations solides**

Ta Lune en Gémeaux en Maison 4 veut un foyer intellectuellement vivant. Ton Ascendant Capricorne structure cette énergie : tu veux construire un chez-toi stable, durable, qui soit aussi un lieu de travail et d'apprentissage.

**Domaine activé** : Maison 4 — Ton foyer cherche à la fois stimulation intellectuelle et solidité matérielle. Tu veux investir dans un bien immobilier de qualité qui serve aussi ton ambition professionnelle.

**Ton approche instinctive** : Le Capricorne te fait construire méthodiquement ta sécurité résidentielle. Tu veux posséder ton chez-toi, avoir des fondations solides qui durent dans le temps.

**Tensions possibles** : La rigidité peut étouffer la légèreté du foyer. Tu risques de transformer ton chez-toi en bureau au détriment du confort émotionnel.

**Conseil clé** : Construire des fondations solides tout en gardant un espace de légèreté et de jeu.""",
        'weekly_advice': {
            'week_1': "Identifie comment investir durablement dans ton foyer.",
            'week_2': "Crée des zones de travail efficaces chez toi.",
            'week_3': "Autorise-toi aussi des espaces de détente et de légèreté.",
            'week_4': "Apprécie la solidité des fondations que tu construis."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Habitat alternatif**

Ta Lune en Gémeaux en Maison 4 veut un foyer intellectuellement riche. Ton Ascendant Verseau ajoute originalité : tu veux vivre différemment, expérimenter avec des formes d'habitat alternatives, créer un espace unique.

**Domaine activé** : Maison 4 — Ton foyer devient un laboratoire d'expérimentation. Tu peux être attiré·e par la colocation, l'habitat participatif, les tiny houses, toute forme non-conventionnelle.

**Ton approche instinctive** : Le Verseau te fait innover dans ta manière d'habiter. Tu veux un chez-toi qui reflète tes valeurs progressistes, qui soit aussi un espace de connexion communautaire.

**Tensions possibles** : Trop d'expérimentation peut créer de l'instabilité. Tu risques de ne jamais vraiment t'ancrer nulle part à force de chercher l'originalité.

**Conseil clé** : Innover dans ton habitat tout en créant une vraie sécurité de base.""",
        'weekly_advice': {
            'week_1': "Explore des formes d'habitat alternatives qui te parlent.",
            'week_2': "Expérimente avec l'organisation de ton espace actuel.",
            'week_3': "Connecte-toi à des communautés qui partagent ta vision.",
            'week_4': "Vérifie que ton originalité te sécurise vraiment."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Refuge poétique**

Ta Lune en Gémeaux en Maison 4 veut un foyer intellectuellement stimulant. Ton Ascendant Poissons ajoute dimension artistique et spirituelle : tu veux un chez-toi qui soit aussi un espace de création et de rêverie.

**Domaine activé** : Maison 4 — Ton foyer oscille entre mental et mystique. Tu veux un espace où tu peux à la fois lire, écrire, créer artistiquement et te connecter à ton intuition.

**Ton approche instinctive** : Le Poissons te fait créer un foyer fluide, peut-être un peu chaotique mais inspirant. Tu veux que ton chez-toi nourrisse ton âme créative et ton esprit.

**Tensions possibles** : Le manque de structure peut créer du chaos. Tu risques de vivre dans le désordre ou de fuir la responsabilité matérielle du foyer.

**Conseil clé** : Créer un foyer inspirant tout en maintenant une structure minimale.""",
        'weekly_advice': {
            'week_1': "Identifie comment nourrir à la fois ton esprit et ton âme chez toi.",
            'week_2': "Crée un espace dédié à la créativité et à la rêverie.",
            'week_3': "Maintiens quand même un minimum d'ordre et de structure.",
            'week_4': "Remercie ton foyer d'être ton refuge poétique."
        }
    },

    # ==================== MAISON 5 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Créativité fulgurante**

Ta Lune en Gémeaux active la Maison 5 : ta créativité et ton expression personnelle passent par l'intellect et la communication. Avec l'Ascendant Bélier, tu veux créer vite, expérimenter audacieusement, t'amuser sans limites.

**Domaine activé** : Maison 5 — Ta créativité est verbale et intellectuelle. Tu t'exprimes par les mots, l'écriture, le débat. Tu veux jouer avec les idées, flirter intellectuellement, t'amuser mentalement.

**Ton approche instinctive** : Le Bélier te pousse à oser dans ta créativité. Tu lances des projets spontanément, tu testes de nouvelles formes d'expression sans peur du jugement.

**Tensions possibles** : L'impulsivité peut te faire démarrer mille projets créatifs sans en finir aucun. Tu risques de disperser ton talent par manque de persévérance.

**Conseil clé** : Oser créer avec audace tout en finissant au moins quelques projets.""",
        'weekly_advice': {
            'week_1': "Lance un projet créatif qui t'excite vraiment.",
            'week_2': "Expérimente sans craindre l'imperfection.",
            'week_3': "Choisis un ou deux projets à vraiment finir.",
            'week_4': "Célèbre ta capacité à créer avec spontanéité."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Art durable**

Ta Lune en Gémeaux en Maison 5 veut créer et s'amuser intellectuellement. Ton Ascendant Taureau ajoute recherche de beauté et de durabilité : tu veux créer quelque chose de beau et de tangible avec tes idées.

**Domaine activé** : Maison 5 — Ta créativité cherche à la fois légèreté et substance. Tu veux t'exprimer de manière intellectuelle mais aussi créer quelque chose qui dure, qui a de la valeur matérielle.

**Ton approche instinctive** : Le Taureau te fait développer tes projets créatifs avec patience. Tu veux que ce que tu crées soit non seulement intelligent mais aussi beau et bien fait.

**Tensions possibles** : Le conflit entre vitesse mentale et lenteur créative peut frustrer. Tu risques de commencer vite puis de te bloquer dans le perfectionnement.

**Conseil clé** : Créer avec légèreté tout en donnant du temps à la qualité.""",
        'weekly_advice': {
            'week_1': "Identifie un projet créatif qui mérite ton investissement.",
            'week_2': "Développe-le avec patience et souci du détail.",
            'week_3': "Trouve le plaisir dans le processus lent de création.",
            'week_4': "Savoure la beauté de ce que tu as créé."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Jeu intellectuel**

Double Gémeaux sur la Maison 5 : ta créativité et ton plaisir sont entièrement intellectuels. Tu t'amuses en apprenant, tu crées en jouant avec les mots et les idées, tu flirtes par l'esprit.

**Domaine activé** : Maison 5 — Ton expression personnelle passe par la légèreté mentale. Tu veux jouer, expérimenter, t'amuser sans te prendre au sérieux. Ton art peut être l'écriture, le théâtre, l'improvisation.

**Ton approche instinctive** : Double Gémeaux te fait jongler avec mille projets créatifs. Tu peux écrire, dessiner, jouer de la musique, tout simultanément. Cette versatilité est ta marque.

**Tensions possibles** : La dispersion peut t'empêcher de vraiment développer un talent. Tu risques de rester amateur dans tout par peur de te spécialiser.

**Conseil clé** : S'amuser créativement tout en développant vraiment une ou deux compétences.""",
        'weekly_advice': {
            'week_1': "Explore librement différentes formes d'expression créative.",
            'week_2': "Choisis celles qui te procurent le plus de joie.",
            'week_3': "Approfondis-les sans perdre la légèreté du jeu.",
            'week_4': "Célèbre ta versatilité créative unique."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Expression sensible**

Ta Lune en Gémeaux en Maison 5 veut créer avec légèreté intellectuelle. Ton Ascendant Cancer ajoute profondeur émotionnelle : tu veux que ta créativité exprime aussi tes sentiments, que ton art touche les cœurs.

**Domaine activé** : Maison 5 — Ton expression créative oscille entre légèreté mentale et profondeur affective. Tu veux créer quelque chose qui soit à la fois intelligent et émouvant.

**Ton approche instinctive** : Le Cancer te fait créer depuis tes émotions. Tes mots, tes créations portent ta vulnérabilité. Cette authenticité touche profondément.

**Tensions possibles** : La peur du jugement peut bloquer ta spontanéité créative. Tu risques de censurer tes idées les plus légères par souci de profondeur.

**Conseil clé** : Honorer à la fois ta légèreté intellectuelle et ta profondeur émotionnelle dans ta créativité.""",
        'weekly_advice': {
            'week_1': "Identifie ce que ton cœur veut vraiment exprimer.",
            'week_2': "Crée en intégrant mental et émotionnel.",
            'week_3': "Autorise-toi aussi la légèreté et l'humour.",
            'week_4': "Partage ta création avec authenticité."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Brillance créative**

Ta Lune en Gémeaux en Maison 5 veut créer intellectuellement. Ton Ascendant Lion, maître naturel de cette maison, amplifie cette énergie : tu veux briller par ta créativité, être admiré·e pour ton talent verbal.

**Domaine activé** : Maison 5 — Ton expression personnelle cherche la reconnaissance. Tu veux créer quelque chose qui impressionne, qui te met en lumière, qui célèbre ton intelligence unique.

**Ton approche instinctive** : Le Lion te donne confiance en ton talent créatif. Tu n'as pas peur de te montrer, de performer, de partager tes créations avec fierté.

**Tensions possibles** : L'ego peut nuire à ta créativité. Tu risques de créer uniquement pour être admiré·e plutôt que par vraie inspiration.

**Conseil clé** : Créer avec confiance tout en restant connecté·e à ta vraie inspiration.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment exprimer au monde.",
            'week_2': "Crée avec audace et générosité créative.",
            'week_3': "Partage tes créations sans attendre la validation.",
            'week_4': "Célèbre ta capacité à inspirer par ton art."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Artisanat intellectuel**

Ta Lune en Gémeaux en Maison 5 veut créer avec légèreté. Ton Ascendant Vierge canalise cette énergie vers la précision : tu veux perfectionner ton art, créer avec excellence, maîtriser ta technique créative.

**Domaine activé** : Maison 5 — Ton expression créative cherche la perfection. Tu veux que ce que tu crées soit non seulement intelligent mais aussi impeccablement exécuté.

**Ton approche instinctive** : La Vierge te fait peaufiner chaque détail de tes créations. Tu peux réécrire dix fois le même paragraphe jusqu'à ce qu'il soit parfait.

**Tensions possibles** : Le perfectionnisme peut tuer la spontanéité créative. Tu risques de ne jamais terminer ou partager tes œuvres par exigence excessive.

**Conseil clé** : Viser l'excellence tout en acceptant l'imperfection créative.""",
        'weekly_advice': {
            'week_1': "Identifie une compétence créative à perfectionner.",
            'week_2': "Pratique avec rigueur et attention au détail.",
            'week_3': "Autorise-toi aussi la création spontanée et imparfaite.",
            'week_4': "Apprécie la qualité de ce que tu as développé."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Art harmonieux**

Ta Lune en Gémeaux en Maison 5 veut créer intellectuellement. Ton Ascendant Balance ajoute sens esthétique et besoin d'harmonie : tu veux créer quelque chose de beau, équilibré, qui plait.

**Domaine activé** : Maison 5 — Ton expression créative cherche la beauté et l'élégance. Tu peux être attiré·e par l'art visuel, le design, tout ce qui combine intellect et esthétique.

**Ton approche instinctive** : La Balance te fait créer avec goût et équilibre. Tu veux que tes œuvres soient harmonieuses, agréables à l'œil ou à l'oreille.

**Tensions possibles** : Le besoin de plaire peut édulcorer ta créativité. Tu risques de censurer tes idées les plus audacieuses pour rester dans le consensus esthétique.

**Conseil clé** : Créer avec beauté tout en osant l'originalité.""",
        'weekly_advice': {
            'week_1': "Explore ce qui te semble vraiment beau et harmonieux.",
            'week_2': "Crée en intégrant ton sens esthétique.",
            'week_3': "Ose aussi dépasser les conventions de beauté.",
            'week_4': "Partage tes créations élégantes avec fierté."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Créativité intense**

Ta Lune en Gémeaux en Maison 5 veut créer avec légèreté. Ton Ascendant Scorpion ajoute profondeur et intensité : tu veux que ton art révèle des vérités cachées, transforme, provoque.

**Domaine activé** : Maison 5 — Ton expression créative oscille entre légèreté et profondeur. Tu veux créer quelque chose qui touche l'âme, qui dérange peut-être, qui ne laisse pas indifférent.

**Ton approche instinctive** : Le Scorpion te fait plonger dans les zones sombres de la créativité. Ton art peut explorer l'ombre, la transformation, l'intensité émotionnelle.

**Tensions possibles** : L'obsession créative peut remplacer la joie de créer. Tu risques de devenir trop sérieux·se, perdant la légèreté gémeau.

**Conseil clé** : Créer avec profondeur tout en gardant la joie du jeu créatif.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment explorer en profondeur.",
            'week_2': "Crée sans censurer ton intensité.",
            'week_3': "Autorise-toi aussi la légèreté et l'humour.",
            'week_4': "Partage tes créations puissantes avec courage."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Créativité expansive**

Ta Lune en Gémeaux en Maison 5 veut créer et s'amuser intellectuellement. Ton Ascendant Sagittaire amplifie cette énergie : tu veux créer à grande échelle, inspirer par ton art, partager ta vision avec générosité.

**Domaine activé** : Maison 5 — Ton expression créative cherche l'expansion et le sens. Tu veux que ton art enseigne, inspire, ouvre des horizons. Tu peux être attiré·e par l'écriture philosophique.

**Ton approche instinctive** : Le Sagittaire te fait créer avec optimisme et foi en ton talent. Tu veux partager largement, toucher un public international, avoir un impact culturel.

**Tensions possibles** : Le manque de discipline peut t'empêcher de concrétiser. Tu risques d'avoir de grandes visions créatives sans jamais les finir.

**Conseil clé** : Viser grand créativement tout en ancrant tes projets dans le réel.""",
        'weekly_advice': {
            'week_1': "Identifie la grande vision créative qui t'inspire.",
            'week_2': "Commence à la concrétiser par petits pas.",
            'week_3': "Garde ton enthousiasme tout en étant pragmatique.",
            'week_4': "Partage généreusement ce que tu crées."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Art structuré**

Ta Lune en Gémeaux en Maison 5 veut créer avec légèreté. Ton Ascendant Capricorne structure cette énergie : tu veux développer un talent professionnel, créer avec sérieux, construire une carrière créative.

**Domaine activé** : Maison 5 — Ton expression créative cherche la reconnaissance professionnelle. Tu veux que ton art soit pris au sérieux, qu'il te rapporte, qu'il construise ta réputation.

**Ton approche instinctive** : Le Capricorne te fait travailler ta créativité avec discipline. Tu pratiques régulièrement, tu perfectionnes ton métier, tu construis méthodiquement ton portfolio.

**Tensions possibles** : La rigidité peut tuer la spontanéité créative. Tu risques de transformer l'art en travail, perdant la joie du jeu.

**Conseil clé** : Construire une pratique créative solide sans perdre le plaisir.""",
        'weekly_advice': {
            'week_1': "Identifie le talent créatif que tu veux professionnaliser.",
            'week_2': "Crée un plan de développement structuré.",
            'week_3': "Pratique régulièrement avec discipline.",
            'week_4': "Autorise-toi aussi des moments de jeu créatif pur."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Innovation créative**

Ta Lune en Gémeaux en Maison 5 veut créer intellectuellement. Ton Ascendant Verseau ajoute originalité : tu veux inventer de nouvelles formes d'art, expérimenter avec la technologie, créer différemment.

**Domaine activé** : Maison 5 — Ton expression créative cherche l'innovation. Tu es attiré·e par l'art numérique, les nouveaux médias, tout ce qui révolutionne l'expression créative.

**Ton approche instinctive** : Le Verseau te fait expérimenter sans peur. Tu testes de nouvelles techniques, tu mélanges les genres, tu crées ce qui n'existe pas encore.

**Tensions possibles** : L'originalité à tout prix peut rendre ton art incompréhensible. Tu risques de créer uniquement pour être différent·e.

**Conseil clé** : Innover créativement tout en restant accessible et authentique.""",
        'weekly_advice': {
            'week_1': "Explore de nouvelles technologies ou formes créatives.",
            'week_2': "Expérimente sans te soucier du résultat.",
            'week_3': "Connecte-toi à des créateurs innovants.",
            'week_4': "Vérifie que ton originalité sert vraiment ton expression."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Art intuitif**

Ta Lune en Gémeaux en Maison 5 veut créer intellectuellement. Ton Ascendant Poissons ajoute dimension mystique : ta créativité devient poétique, inspirée, canalisée depuis ton intuition profonde.

**Domaine activé** : Maison 5 — Ton expression créative oscille entre mental et mystique. Tu veux créer quelque chose qui soit à la fois intelligent et spirituellement inspiré.

**Ton approche instinctive** : Le Poissons te fait créer depuis un état de flow. Tu te laisses porter par l'inspiration, tu crées parfois sans comprendre d'où ça vient.

**Tensions possibles** : La confusion peut remplacer la clarté créative. Tu risques de te perdre dans tes visions sans jamais les concrétiser.

**Conseil clé** : Canaliser ton inspiration tout en maintenant assez de structure pour créer.""",
        'weekly_advice': {
            'week_1': "Crée des espaces de connexion à ton inspiration profonde.",
            'week_2': "Laisse-toi porter par le flow créatif.",
            'week_3': "Donne forme concrète à tes visions.",
            'week_4': "Remercie ton canal créatif pour ce qu'il t'a offert."
        }
    },

    # ==================== MAISON 6 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Travail rapide**

Ta Lune en Gémeaux active la Maison 6 : ton quotidien et ton travail demandent variété et stimulation intellectuelle. Avec l'Ascendant Bélier, tu veux agir vite, multiplier les tâches, être efficace instantanément.

**Domaine activé** : Maison 6 — Ton travail quotidien a besoin de diversité. Tu ne supportes pas la routine répétitive, tu veux jongler entre plusieurs projets, apprendre en travaillant.

**Ton approche instinctive** : Le Bélier te pousse à attaquer tes tâches avec énergie. Tu peux travailler très vite sur plusieurs fronts simultanément, mais tu risques de te disperser.

**Tensions possibles** : L'impulsivité peut créer des erreurs dans les détails. Tu risques de bâcler certaines tâches par impatience ou de t'épuiser par suractivité.

**Conseil clé** : Utiliser ton énergie rapide tout en maintenant un minimum de qualité.""",
        'weekly_advice': {
            'week_1': "Organise tes tâches pour créer de la variété.",
            'week_2': "Attaque ton travail avec énergie mais attention.",
            'week_3': "Tempère ta vitesse pour ne pas faire d'erreurs.",
            'week_4': "Célèbre tout ce que tu as accompli efficacement."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Routine enrichissante**

Ta Lune en Gémeaux en Maison 6 veut de la variété dans le quotidien. Ton Ascendant Taureau ajoute besoin de stabilité : tu cherches une routine qui soit à la fois stimulante intellectuellement et confortable.

**Domaine activé** : Maison 6 — Ton travail quotidien oscille entre besoin de changement et besoin de sécurité. Tu veux une certaine régularité qui intègre quand même de la diversité.

**Ton approche instinctive** : Le Taureau te fait créer des routines solides. Tu travailles régulièrement, méthodiquement, mais tu as besoin d'intégrer de l'apprentissage et de la variété.

**Tensions possibles** : Le conflit entre variété et routine peut te bloquer. Tu oscilles entre envie de tout changer et peur du changement dans ton quotidien.

**Conseil clé** : Créer une routine stable qui intègre de la variété intellectuelle.""",
        'weekly_advice': {
            'week_1': "Identifie comment rendre ta routine plus stimulante.",
            'week_2': "Intègre de l'apprentissage dans ton quotidien.",
            'week_3': "Garde quand même des repères stables et confortables.",
            'week_4': "Apprécie l'équilibre entre stabilité et variété."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Multitâche extrême**

Double Gémeaux sur la Maison 6 : ton quotidien et ton travail sont entièrement organisés autour de la variété. Tu as besoin de jongler entre plusieurs tâches, plusieurs projets, plusieurs apprentissages simultanés.

**Domaine activé** : Maison 6 — Ton travail quotidien ne peut pas être monotone. Tu as besoin de changer constamment de tâche, d'apprendre de nouvelles compétences, de communiquer tout en travaillant.

**Ton approche instinctive** : Double Gémeaux te fait travailler sur dix choses à la fois. Tu peux avoir plusieurs jobs, plusieurs projets, plusieurs hobbies en parallèle. Cette agilité est fascinante.

**Tensions possibles** : La dispersion extrême peut t'empêcher de vraiment accomplir quoi que ce soit. Tu risques de te fatiguer nerveusement sans avancer vraiment.

**Conseil clé** : Organiser consciemment ta variété pour rester efficace malgré tout.""",
        'weekly_advice': {
            'week_1': "Liste toutes tes tâches et projets en cours.",
            'week_2': "Organise-les pour créer de la cohérence dans la variété.",
            'week_3': "Autorise-toi des moments de focus profond.",
            'week_4': "Mesure ce que tu as vraiment accompli versus juste commencé."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Service sensible**

Ta Lune en Gémeaux en Maison 6 veut de la variété au travail. Ton Ascendant Cancer ajoute dimension émotionnelle : tu veux travailler dans un environnement sécurisant, où tu te sens nourri·e affectivement.

**Domaine activé** : Maison 6 — Ton travail quotidien cherche à la fois stimulation intellectuelle et sécurité émotionnelle. Tu as besoin de te sentir bien dans ton environnement de travail.

**Ton approche instinctive** : Le Cancer te fait choisir un travail qui prend soin des autres ou qui te permet de créer de l'intimité. Tu peux être attiré·e par les métiers d'aide ou l'écriture.

**Tensions possibles** : La sensibilité peut rendre ton quotidien difficile. Tu risques de prendre trop à cœur les critiques professionnelles ou de te fatiguer émotionnellement.

**Conseil clé** : Créer un quotidien qui nourrit à la fois ton esprit et ton cœur.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te sécurise vraiment dans ton travail.",
            'week_2': "Crée un environnement de travail confortable.",
            'week_3': "Protège ta sensibilité sans t'isoler professionnellement.",
            'week_4': "Célèbre ta capacité à servir avec authenticité."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Travail brillant**

Ta Lune en Gémeaux en Maison 6 veut de la variété au travail. Ton Ascendant Lion ajoute besoin de reconnaissance : tu veux que ton travail quotidien te permette de briller, d'être admiré·e pour tes compétences.

**Domaine activé** : Maison 6 — Ton travail quotidien cherche la reconnaissance. Tu veux être apprécié·e pour ton intelligence, ta polyvalence, ta capacité à résoudre les problèmes avec créativité.

**Ton approche instinctive** : Le Lion te fait aborder ton travail avec fierté. Tu veux exceller dans ce que tu fais, être le·la meilleur·e dans ton domaine, inspirer tes collègues.

**Tensions possibles** : L'ego peut créer des tensions professionnelles. Tu risques de mal supporter les tâches "ingrates" ou de vouloir tout contrôler.

**Conseil clé** : Exceller dans ton travail tout en servant humblement.""",
        'weekly_advice': {
            'week_1': "Identifie où tu veux vraiment briller professionnellement.",
            'week_2': "Donne le meilleur de toi-même avec fierté.",
            'week_3': "Accepte aussi les tâches moins glorieuses avec grâce.",
            'week_4': "Célèbre ta contribution unique au travail."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Efficacité parfaite**

Ta Lune en Gémeaux en Maison 6 veut de la variété au travail. Ton Ascendant Vierge, maître naturel de cette maison, canalise cette énergie : tu veux être à la fois polyvalent·e et parfaitement organisé·e.

**Domaine activé** : Maison 6 — Ton travail quotidien cherche l'excellence dans la variété. Tu veux maîtriser plusieurs compétences, être efficace, utile, perfectionniste dans chaque tâche.

**Ton approche instinctive** : La Vierge te fait organiser méticuleusement ton quotidien. Tu as des systèmes pour tout, tu optimises chaque processus, tu veux être irréprochable.

**Tensions possibles** : Le perfectionnisme peut créer de l'anxiété au travail. Tu risques de te stresser sur les détails au point de nuire à ta santé.

**Conseil clé** : Viser l'excellence professionnelle sans tomber dans l'obsession.""",
        'weekly_advice': {
            'week_1': "Organise ton travail pour maximiser l'efficacité.",
            'week_2': "Perfectionne tes systèmes et tes compétences.",
            'week_3': "Autorise-toi aussi l'imperfection et le repos.",
            'week_4': "Apprécie la qualité de ton travail accompli."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Collaboration harmonieuse**

Ta Lune en Gémeaux en Maison 6 veut de la variété au travail. Ton Ascendant Balance ajoute besoin d'harmonie : tu veux travailler en équipe, dans un environnement équilibré et esthétiquement agréable.

**Domaine activé** : Maison 6 — Ton travail quotidien cherche la beauté et la collaboration. Tu veux travailler dans un cadre agréable, avec des gens que tu apprécies, sur des projets équilibrés.

**Ton approche instinctive** : La Balance te fait rechercher l'équilibre dans ton quotidien. Tu veux que ton travail soit harmonieux, que les relations professionnelles soient justes et agréables.

**Tensions possibles** : Le besoin de plaire peut te faire accepter trop de tâches. Tu risques de te surcharger pour maintenir l'harmonie au travail.

**Conseil clé** : Créer un environnement professionnel harmonieux tout en posant tes limites.""",
        'weekly_advice': {
            'week_1': "Identifie comment améliorer l'harmonie au travail.",
            'week_2': "Embellis ton environnement professionnel.",
            'week_3': "Collabore généreusement mais pose tes limites.",
            'week_4': "Célèbre l'équilibre créé dans ton quotidien."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Travail intense**

Ta Lune en Gémeaux en Maison 6 veut de la variété au travail. Ton Ascendant Scorpion ajoute profondeur : tu veux que ton travail quotidien ait du sens, qu'il te transforme, qu'il aille au-delà de la surface.

**Domaine activé** : Maison 6 — Ton travail quotidien oscille entre légèreté et intensité. Tu veux des tâches variées mais qui ont un impact réel, qui changent vraiment les choses.

**Ton approche instinctive** : Le Scorpion te fait t'investir totalement dans ton travail. Tu peux devenir obsédé·e par certains projets, creuser en profondeur jusqu'à maîtriser complètement.

**Tensions possibles** : L'obsession peut créer du burn-out. Tu risques de te consumer dans ton travail, oubliant de prendre soin de ta santé.

**Conseil clé** : T'investir profondément dans ton travail tout en préservant ton énergie.""",
        'weekly_advice': {
            'week_1': "Identifie les projets qui méritent vraiment ton intensité.",
            'week_2': "Plonge en profondeur sans perdre l'équilibre.",
            'week_3': "Autorise-toi aussi des tâches plus légères.",
            'week_4': "Vérifie que ton investissement ne nuit pas à ta santé."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Service inspirant**

Ta Lune en Gémeaux en Maison 6 veut de la variété au travail. Ton Ascendant Sagittaire amplifie cette soif : tu veux que ton travail quotidien ait du sens, qu'il te permette d'apprendre et de transmettre.

**Domaine activé** : Maison 6 — Ton travail quotidien cherche l'expansion et le sens. Tu peux être attiré·e par l'enseignement, le voyage, tout travail qui élargit les horizons.

**Ton approche instinctive** : Le Sagittaire te fait aborder ton travail avec optimisme et foi. Tu crois en la mission de ce que tu fais, tu veux servir une vision plus grande.

**Tensions possibles** : Le manque de discipline peut créer du chaos professionnel. Tu risques d'être peu fiable dans les détails par excès d'enthousiasme.

**Conseil clé** : Servir avec inspiration tout en maintenant la rigueur nécessaire.""",
        'weekly_advice': {
            'week_1': "Identifie le sens profond de ton travail quotidien.",
            'week_2': "Accomplis tes tâches avec foi et enthousiasme.",
            'week_3': "Garde quand même une discipline pratique.",
            'week_4': "Célèbre l'impact inspirant de ton service."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Productivité structurée**

Ta Lune en Gémeaux en Maison 6 veut de la variété au travail. Ton Ascendant Capricorne structure cette énergie : tu veux être productif·ve, efficace, construire une carrière solide par ton travail quotidien.

**Domaine activé** : Maison 6 — Ton travail quotidien cherche l'efficacité et l'avancement. Tu veux que chaque tâche serve ton ambition, que ton quotidien construise ta réputation professionnelle.

**Ton approche instinctive** : Le Capricorne te fait travailler avec discipline et sérieux. Tu as une éthique de travail forte, tu respectes les délais, tu construis méthodiquement.

**Tensions possibles** : La rigidité peut étouffer ta créativité au travail. Tu risques de t'épuiser par excès de travail ou de perdre toute joie dans ton quotidien.

**Conseil clé** : Construire une carrière solide sans sacrifier ta santé et ta joie.""",
        'weekly_advice': {
            'week_1': "Organise ton travail pour maximiser ta productivité.",
            'week_2': "Travaille avec discipline et ambition claire.",
            'week_3': "Autorise-toi aussi des pauses et de la variété.",
            'week_4': "Mesure les fondations professionnelles construites."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Travail innovant**

Ta Lune en Gémeaux en Maison 6 veut de la variété au travail. Ton Ascendant Verseau ajoute innovation : tu veux travailler différemment, utiliser de nouvelles technologies, contribuer au progrès collectif.

**Domaine activé** : Maison 6 — Ton travail quotidien cherche l'originalité et l'impact collectif. Tu es attiré·e par les startups, les technologies, tout environnement qui innove.

**Ton approche instinctive** : Le Verseau te fait expérimenter avec de nouvelles méthodes de travail. Tu peux être freelance, travailler à distance, inventer de nouveaux processus.

**Tensions possibles** : Trop d'expérimentation peut créer de l'instabilité professionnelle. Tu risques de manquer de routine saine par rejet des conventions.

**Conseil clé** : Innover dans ton travail tout en maintenant une base de stabilité.""",
        'weekly_advice': {
            'week_1': "Explore de nouvelles manières de travailler ou de t'organiser.",
            'week_2': "Expérimente avec des technologies ou méthodes innovantes.",
            'week_3': "Connecte-toi à des communautés professionnelles visionnaires.",
            'week_4': "Vérifie que ton innovation sert vraiment ton bien-être."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Service intuitif**

Ta Lune en Gémeaux en Maison 6 veut de la variété au travail. Ton Ascendant Poissons ajoute dimension spirituelle : tu veux que ton travail quotidien ait une dimension de service compassionnel.

**Domaine activé** : Maison 6 — Ton travail quotidien oscille entre mental et mystique. Tu peux être attiré·e par les métiers d'aide, l'art thérapie, tout travail qui intègre intuition et service.

**Ton approche instinctive** : Le Poissons te fait travailler depuis l'inspiration et la compassion. Tu te laisses guider par ton intuition dans ton quotidien professionnel.

**Tensions possibles** : Le manque de structure peut créer du chaos dans ton travail. Tu risques d'être peu fiable pratiquement par excès de fluidité.

**Conseil clé** : Servir avec intuition tout en maintenant une structure minimale.""",
        'weekly_advice': {
            'week_1': "Identifie comment servir depuis ton cœur et ton intuition.",
            'week_2': "Laisse-toi guider par ton ressenti dans ton travail.",
            'week_3': "Maintiens quand même des routines pratiques de base.",
            'week_4': "Remercie la fluidité qui nourrit ton service."
        }
    },

    # ==================== MAISON 7 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Partenariat dynamique**

Ta Lune en Gémeaux active la Maison 7 : tes relations et partenariats passent par la communication et l'échange intellectuel. Avec l'Ascendant Bélier, tu veux des relations stimulantes, directes, où tu peux débattre et te confronter.

**Domaine activé** : Maison 7 — Tes partenariats ont besoin de vivacité intellectuelle. Tu cherches des partenaires qui te challengent mentalement, avec qui tu peux échanger sans censure.

**Ton approche instinctive** : Le Bélier te fait aborder tes relations avec franchise. Tu dis ce que tu penses, tu n'as pas peur du conflit verbal, tu veux de l'authenticité immédiate.

**Tensions possibles** : L'agressivité verbale peut créer des ruptures. Tu risques de blesser tes partenaires par franchise excessive ou de chercher la confrontation.

**Conseil clé** : Cultiver des relations stimulantes tout en respectant la sensibilité de l'autre.""",
        'weekly_advice': {
            'week_1': "Initie des conversations importantes avec tes partenaires.",
            'week_2': "Exprime tes besoins clairement et directement.",
            'week_3': "Tempère ta franchise pour ne pas blesser inutilement.",
            'week_4': "Célèbre la vitalité de tes échanges relationnels."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Relation stable**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuellement stimulants. Ton Ascendant Taureau ajoute besoin de stabilité : tu cherches une relation qui combine échange mental et sécurité affective.

**Domaine activé** : Maison 7 — Tes partenariats oscillent entre besoin de variété intellectuelle et besoin de stabilité émotionnelle. Tu veux pouvoir tout discuter mais dans un cadre sécurisant.

**Ton approche instinctive** : Le Taureau te fait construire tes relations lentement mais sûrement. Tu veux des partenaires fiables avec qui tu peux aussi avoir des échanges riches.

**Tensions possibles** : Le conflit entre besoin de changement et besoin de stabilité peut créer des tensions. Tu oscilles entre envie de papillonner et désir d'engagement.

**Conseil clé** : Créer des partenariats stables qui intègrent de la variété intellectuelle.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te sécurise vraiment dans tes relations.",
            'week_2': "Construis la stabilité tout en nourrissant l'échange.",
            'week_3': "Communique tes besoins de variété avec clarté.",
            'week_4': "Apprécie l'équilibre entre stabilité et stimulation."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Connexion mentale**

Double Gémeaux sur la Maison 7 : tes partenariats sont entièrement basés sur l'échange intellectuel. Tu cherches un·e partenaire avec qui tu peux parler de tout, qui stimule ton esprit, qui est ton·ta meilleur·e ami·e.

**Domaine activé** : Maison 7 — Tes relations sont avant tout des amitiés intellectuelles. Tu as besoin d'un·e partenaire curieux·se, communicatif·ve, qui comprenne ton besoin de variété.

**Ton approche instinctive** : Double Gémeaux te fait chercher la connexion par les mots. Tu tombes amoureux·se d'un esprit, tu séduis par l'intelligence, tu communiques constamment.

**Tensions possibles** : Le manque de profondeur émotionnelle peut créer de la frustration. Tu risques de rester dans l'intellectualisation au détriment de l'intimité.

**Conseil clé** : Cultiver l'échange mental tout en développant aussi l'intimité émotionnelle.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment échanger avec ton·ta partenaire.",
            'week_2': "Nourris la connexion intellectuelle généreusement.",
            'week_3': "Autorise-toi aussi des moments de vulnérabilité émotionnelle.",
            'week_4': "Célèbre la richesse de votre complicité mentale."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Intimité communicative**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuels. Ton Ascendant Cancer ajoute profondeur émotionnelle : tu cherches une relation où tu peux à la fois échanger et te sentir profondément en sécurité.

**Domaine activé** : Maison 7 — Tes partenariats cherchent à intégrer mental et émotionnel. Tu veux pouvoir parler de tout avec ton·ta partenaire tout en créant une vraie intimité du cœur.

**Ton approche instinctive** : Le Cancer te fait chercher la sécurité affective dans tes relations. Tu veux un·e partenaire avec qui tu peux être vulnérable, qui te nourrit émotionnellement.

**Tensions possibles** : La peur de la vulnérabilité peut te faire fuir dans le mental. Tu risques d'intellectualiser tes émotions au lieu de les vivre dans la relation.

**Conseil clé** : Créer des partenariats où mental et émotionnel cohabitent harmonieusement.""",
        'weekly_advice': {
            'week_1': "Identifie ce que ton cœur attend vraiment de la relation.",
            'week_2': "Partage tes vulnérabilités avec ton·ta partenaire.",
            'week_3': "Nourris aussi la connexion intellectuelle.",
            'week_4': "Célèbre l'intimité profonde que vous créez."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Partenariat brillant**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuels. Ton Ascendant Lion ajoute besoin de reconnaissance : tu cherches un·e partenaire qui admire ton intelligence, avec qui tu peux briller socialement.

**Domaine activé** : Maison 7 — Tes partenariats cherchent la célébration mutuelle. Tu veux être admiré·e par ton·ta partenaire, former un couple qui impressionne, rayonner ensemble.

**Ton approche instinctive** : Le Lion te fait chercher un·e partenaire qui te valorise. Tu veux quelqu'un qui soit fier·ère de toi, qui célèbre ton intelligence et ta créativité.

**Tensions possibles** : L'ego peut créer des luttes de pouvoir. Tu risques de chercher l'admiration au détriment de l'égalité dans la relation.

**Conseil clé** : Créer un partenariat où vous brillez ensemble sans compétition.""",
        'weekly_advice': {
            'week_1': "Identifie comment vous pouvez vous élever mutuellement.",
            'week_2': "Célèbre les talents de ton·ta partenaire généreusement.",
            'week_3': "Laisse-toi aussi admirer sans orgueil excessif.",
            'week_4': "Rayonnez ensemble avec fierté partagée."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Partenariat utile**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuels. Ton Ascendant Vierge canalise cette énergie : tu cherches un·e partenaire avec qui tu peux construire concrètement, s'améliorer mutuellement.

**Domaine activé** : Maison 7 — Tes partenariats cherchent l'utilité et le perfectionnement. Tu veux une relation qui te fait grandir, où vous vous aidez mutuellement à devenir meilleurs.

**Ton approche instinctive** : La Vierge te fait analyser tes relations avec lucidité. Tu veux un·e partenaire fiable, compétent·e, avec qui tu peux avoir des échanges utiles et constructifs.

**Tensions possibles** : Le perfectionnisme peut créer de la critique excessive. Tu risques de pointer les défauts de ton·ta partenaire au lieu d'apprécier ses qualités.

**Conseil clé** : Cultiver un partenariat d'amélioration mutuelle sans tomber dans la critique.""",
        'weekly_advice': {
            'week_1': "Identifie comment vous aider mutuellement à grandir.",
            'week_2': "Communique tes observations avec bienveillance.",
            'week_3': "Accepte aussi l'imperfection dans la relation.",
            'week_4': "Apprécie tout ce que vous construisez ensemble."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre parfait**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuels. Ton Ascendant Balance, maître naturel de cette maison, amplifie cette énergie : tu cherches l'harmonie parfaite dans l'échange.

**Domaine activé** : Maison 7 — Tes partenariats sont au centre de ta vie ce mois-ci. Tu cherches l'équilibre idéal, la beauté dans la relation, l'harmonie dans la communication.

**Ton approche instinctive** : La Balance te fait chercher l'équité et la beauté relationnelle. Tu veux un·e partenaire avec qui tout est équilibré, juste, harmonieux.

**Tensions possibles** : Le besoin d'harmonie peut créer de la superficialité. Tu risques d'éviter les conversations difficiles pour maintenir la paix.

**Conseil clé** : Cultiver l'harmonie relationnelle tout en permettant l'authenticité.""",
        'weekly_advice': {
            'week_1': "Identifie les déséquilibres dans ta relation.",
            'week_2': "Communique pour rétablir l'équité et l'harmonie.",
            'week_3': "Autorise-toi aussi les conversations difficiles nécessaires.",
            'week_4': "Célèbre la beauté de votre équilibre."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Fusion intense**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuels légers. Ton Ascendant Scorpion ajoute profondeur : tu cherches une relation qui soit à la fois stimulante mentalement et intensément transformatrice.

**Domaine activé** : Maison 7 — Tes partenariats oscillent entre légèreté et profondeur. Tu veux pouvoir tout discuter avec ton·ta partenaire tout en vivant une fusion émotionnelle intense.

**Ton approche instinctive** : Le Scorpion te fait chercher l'intimité absolue. Tu veux connaître tous les secrets de ton·ta partenaire, créer une relation où rien n'est caché.

**Tensions possibles** : L'intensité peut étouffer la légèreté. Tu risques de devenir possessif·ve ou obsessionnel·le dans tes relations.

**Conseil clé** : Cultiver la profondeur relationnelle tout en gardant de la légèreté.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment partager en profondeur.",
            'week_2': "Crée de l'intimité par la vulnérabilité authentique.",
            'week_3': "Autorise-toi aussi des moments de légèreté et d'humour.",
            'week_4': "Apprécie l'intensité de votre connexion."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventure partagée**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuels. Ton Ascendant Sagittaire amplifie cette soif : tu cherches un·e partenaire d'aventure intellectuelle, avec qui explorer le monde et les idées.

**Domaine activé** : Maison 7 — Tes partenariats cherchent l'expansion et la liberté. Tu veux un·e partenaire qui t'inspire, avec qui voyager physiquement et intellectuellement.

**Ton approche instinctive** : Le Sagittaire te fait chercher un·e partenaire optimiste et aventureux·se. Tu veux quelqu'un qui partage ta vision, ta foi en la vie, ton enthousiasme.

**Tensions possibles** : Le besoin de liberté peut créer des difficultés d'engagement. Tu risques de fuir toute routine relationnelle ou de manquer de présence.

**Conseil clé** : Cultiver l'aventure partagée tout en créant aussi de la stabilité.""",
        'weekly_advice': {
            'week_1': "Identifie les aventures que vous voulez vivre ensemble.",
            'week_2': "Explorez de nouveaux horizons intellectuels ou géographiques.",
            'week_3': "Créez aussi des rituels qui ancrent votre relation.",
            'week_4': "Célèbre l'expansion que votre partenariat permet."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Partenariat solide**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuels. Ton Ascendant Capricorne structure cette énergie : tu cherches une relation sérieuse, durable, qui construit quelque chose de concret.

**Domaine activé** : Maison 7 — Tes partenariats cherchent la stabilité et la construction. Tu veux un·e partenaire avec qui tu peux bâtir un projet de vie, pas juste échanger des idées.

**Ton approche instinctive** : Le Capricorne te fait aborder les relations avec sérieux. Tu veux un engagement clair, des objectifs communs, une structure relationnelle solide.

**Tensions possibles** : La rigidité peut étouffer la spontanéité relationnelle. Tu risques de transformer la relation en projet au détriment de la légèreté.

**Conseil clé** : Construire un partenariat solide sans perdre la joie de l'échange.""",
        'weekly_advice': {
            'week_1': "Identifie ce que vous voulez construire ensemble.",
            'week_2': "Établissez des bases solides et des engagements clairs.",
            'week_3': "Autorise-toi aussi des moments de légèreté et de jeu.",
            'week_4': "Apprécie la solidité de ce que vous bâtissez."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Connexion visionnaire**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuels. Ton Ascendant Verseau ajoute originalité : tu cherches une relation non-conventionnelle, basée sur l'amitié intellectuelle et la liberté.

**Domaine activé** : Maison 7 — Tes partenariats cherchent l'innovation et l'indépendance. Tu veux un·e partenaire qui soit d'abord ton·ta ami·e, qui respecte ta liberté, qui partage ta vision d'avant-garde.

**Ton approche instinctive** : Le Verseau te fait expérimenter avec de nouvelles formes relationnelles. Tu peux être attiré·e par les relations ouvertes, les relations à distance, tout ce qui sort des conventions.

**Tensions possibles** : Le besoin de liberté peut créer de la distance émotionnelle. Tu risques de fuir l'intimité au nom de l'indépendance.

**Conseil clé** : Innover dans tes relations tout en créant de la vraie connexion.""",
        'weekly_advice': {
            'week_1': "Explore ce que tu veux vraiment comme relation.",
            'week_2': "Expérimente avec de nouvelles formes de partenariat.",
            'week_3': "Connecte-toi aussi émotionnellement malgré la liberté.",
            'week_4': "Célèbre l'originalité de votre lien."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Fusion poétique**

Ta Lune en Gémeaux en Maison 7 veut des partenariats intellectuels. Ton Ascendant Poissons ajoute dimension mystique : tu cherches une relation qui transcende les mots, une connexion d'âme autant que d'esprit.

**Domaine activé** : Maison 7 — Tes partenariats oscillent entre mental et mystique. Tu veux pouvoir tout discuter avec ton·ta partenaire tout en vivant une fusion spirituelle profonde.

**Ton approche instinctive** : Le Poissons te fait chercher la fusion totale. Tu veux dissoudre les frontières, créer une relation où vous ne faites qu'un·e, communiquer par intuition.

**Tensions possibles** : La confusion peut remplacer la clarté relationnelle. Tu risques de perdre tes limites ou d'idéaliser ton·ta partenaire.

**Conseil clé** : Cultiver la fusion spirituelle tout en gardant des frontières saines.""",
        'weekly_advice': {
            'week_1': "Identifie la connexion spirituelle que tu cherches.",
            'week_2': "Crée de l'intimité mystique par la vulnérabilité.",
            'week_3': "Maintiens quand même des limites et de la clarté.",
            'week_4': "Remercie la magie de votre connexion."
        }
    },

    # ==================== MAISON 8 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Secrets dévoilés**

Ta Lune en Gémeaux active la Maison 8 : tes transformations et ton rapport à l'intimité passent par la communication et la compréhension intellectuelle. Avec l'Ascendant Bélier, tu veux percer les mystères rapidement, parler sans tabou.

**Domaine activé** : Maison 8 — Ta sexualité, tes peurs profondes, ton rapport à la mort et à la transformation se vivent à travers les mots. Tu as besoin de nommer, comprendre, échanger sur ces sujets.

**Ton approche instinctive** : Le Bélier te pousse à aborder les sujets tabous frontalement. Tu n'as pas peur de parler de sexe, d'argent partagé, de mort. Cette franchise peut choquer ou libérer.

**Tensions possibles** : L'agressivité verbale peut créer des blessures dans l'intimité. Tu risques de forcer les révélations au lieu de respecter le rythme de l'autre.

**Conseil clé** : Explorer les profondeurs avec courage tout en respectant les limites.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment comprendre en profondeur.",
            'week_2': "Initie des conversations sur des sujets intimes ou tabous.",
            'week_3': "Respecte le rythme de l'autre dans les révélations.",
            'week_4': "Célèbre ta capacité à nommer ce qui est caché."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Valeurs partagées**

Ta Lune en Gémeaux en Maison 8 veut comprendre intellectuellement les mystères. Ton Ascendant Taureau ajoute dimension matérielle : tu veux sécuriser les ressources partagées, comprendre la valeur de l'intimité.

**Domaine activé** : Maison 8 — Tes transformations passent par la compréhension des ressources communes. Tu veux clarifier les questions d'argent dans les relations, sécuriser ce qui est partagé.

**Ton approche instinctive** : Le Taureau te fait aborder l'intimité avec prudence. Tu veux construire une confiance solide avant de te révéler, comprendre avant de fusionner.

**Tensions possibles** : La peur de perdre peut bloquer la vraie intimité. Tu risques de contrôler les ressources partagées par insécurité.

**Conseil clé** : Construire la sécurité dans le partage tout en osant la vulnérabilité.""",
        'weekly_advice': {
            'week_1': "Clarifie les questions de ressources partagées.",
            'week_2': "Communique tes peurs et tes besoins de sécurité.",
            'week_3': "Ose progressivement plus de vulnérabilité.",
            'week_4': "Apprécie la solidité de la confiance construite."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Curiosité profonde**

Double Gémeaux sur la Maison 8 : tu veux comprendre intellectuellement tous les mystères. Ta curiosité se porte sur le sexe, la mort, la psychologie, l'occultisme. Tu veux nommer l'innommable.

**Domaine activé** : Maison 8 — Tes transformations passent par la compréhension. Tu lis sur la psychologie, tu explores la spiritualité, tu veux comprendre ce qui est normalement caché ou tabou.

**Ton approche instinctive** : Double Gémeaux te fait intellectualiser les profondeurs. Tu peux parler de sujets intimes avec détachement, analyser tes peurs plutôt que les ressentir.

**Tensions possibles** : L'intellectualisation peut t'empêcher de vraiment vivre tes transformations. Tu risques de tout comprendre sans rien ressentir.

**Conseil clé** : Comprendre les mystères tout en acceptant aussi de les vivre émotionnellement.""",
        'weekly_advice': {
            'week_1': "Explore intellectuellement un sujet profond qui t'intrigue.",
            'week_2': "Lis, apprends, comprends les mécanismes cachés.",
            'week_3': "Autorise-toi aussi à ressentir au-delà de la compréhension.",
            'week_4': "Intègre ce que tu as compris ET ressenti."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Intimité vulnérable**

Ta Lune en Gémeaux en Maison 8 veut comprendre l'intimité intellectuellement. Ton Ascendant Cancer ajoute profondeur émotionnelle : tu veux créer une vraie sécurité affective dans la fusion avec l'autre.

**Domaine activé** : Maison 8 — Tes transformations oscillent entre besoin de comprendre et besoin de ressentir. Tu veux pouvoir parler de l'intimité tout en la vivant profondément.

**Ton approche instinctive** : Le Cancer te fait chercher la sécurité émotionnelle avant de te révéler. Tu as besoin de confiance absolue pour t'ouvrir vraiment sur tes peurs et tes désirs.

**Tensions possibles** : La peur de la vulnérabilité peut te faire fuir dans le mental. Tu risques d'analyser tes émotions au lieu de les partager vraiment.

**Conseil clé** : Créer une intimité où tu peux à la fois comprendre et ressentir profondément.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment partager en intimité.",
            'week_2': "Crée un espace sécurisant pour te révéler.",
            'week_3': "Partage tes vulnérabilités avec authenticité.",
            'week_4': "Célèbre la profondeur de l'intimité créée."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Transformation rayonnante**

Ta Lune en Gémeaux en Maison 8 veut comprendre les mystères. Ton Ascendant Lion ajoute dimension créative : tu veux transformer cette compréhension en expression, en art, en partage inspirant.

**Domaine activé** : Maison 8 — Tes transformations cherchent à être partagées. Tu peux vouloir parler publiquement de sujets tabous, créer de l'art depuis tes profondeurs.

**Ton approche instinctive** : Le Lion te fait transformer tes découvertes profondes en quelque chose de beau. Tu veux que tes transformations soient vues, reconnues, qu'elles inspirent.

**Tensions possibles** : L'ego peut nuire à la vraie transformation. Tu risques de mettre en scène tes profondeurs au lieu de les vivre vraiment.

**Conseil clé** : Vivre tes transformations authentiquement avant de les partager.""",
        'weekly_advice': {
            'week_1': "Plonge dans tes profondeurs sans public.",
            'week_2': "Vis tes transformations avec authenticité.",
            'week_3': "Ensuite seulement, partage ce qui mérite d'être partagé.",
            'week_4': "Inspire les autres par ta vraie transformation."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Analyse profonde**

Ta Lune en Gémeaux en Maison 8 veut comprendre les mystères. Ton Ascendant Vierge canalise cette énergie : tu veux analyser méthodiquement tes peurs, comprendre précisément les mécanismes de transformation.

**Domaine activé** : Maison 8 — Tes transformations passent par l'analyse détaillée. Tu peux être attiré·e par la psychothérapie, la recherche, tout ce qui permet de disséquer les profondeurs.

**Ton approche instinctive** : La Vierge te fait aborder tes peurs avec méthode. Tu veux comprendre chaque détail, améliorer progressivement, guérir par la compréhension.

**Tensions possibles** : L'analyse excessive peut bloquer le lâcher-prise nécessaire. Tu risques de vouloir tout contrôler au lieu d'accepter le mystère.

**Conseil clé** : Analyser pour comprendre tout en acceptant aussi l'inexplicable.""",
        'weekly_advice': {
            'week_1': "Identifie une peur ou un schéma à comprendre.",
            'week_2': "Analyse-le méthodiquement avec bienveillance.",
            'week_3': "Accepte aussi ce qui reste mystérieux.",
            'week_4': "Apprécie la guérison progressive obtenue."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Intimité équilibrée**

Ta Lune en Gémeaux en Maison 8 veut comprendre l'intimité intellectuellement. Ton Ascendant Balance ajoute recherche d'équilibre : tu veux créer une intimité juste, où les échanges profonds sont harmonieux.

**Domaine activé** : Maison 8 — Tes transformations passent par l'équilibre relationnel. Tu veux que l'intimité soit équitable, que les ressources partagées soient justes, que la vulnérabilité soit réciproque.

**Ton approche instinctive** : La Balance te fait chercher l'harmonie même dans les profondeurs. Tu veux que les échanges intimes soient beaux, équilibrés, respectueux.

**Tensions possibles** : Le besoin d'harmonie peut empêcher les vraies transformations. Tu risques d'éviter les confrontations nécessaires à la guérison.

**Conseil clé** : Chercher l'équilibre tout en acceptant le chaos de la transformation.""",
        'weekly_advice': {
            'week_1': "Identifie les déséquilibres dans l'intimité partagée.",
            'week_2': "Communique pour rétablir la justice et l'équité.",
            'week_3': "Accepte aussi les moments de déséquilibre transformateur.",
            'week_4': "Célèbre l'harmonie retrouvée dans la profondeur."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Mystères révélés**

Ta Lune en Gémeaux en Maison 8 veut comprendre intellectuellement les mystères. Ton Ascendant Scorpion, maître naturel de cette maison, amplifie cette énergie : tu veux percer tous les secrets, tout comprendre de l'ombre.

**Domaine activé** : Maison 8 — Ta curiosité intellectuelle rencontre les vrais mystères. Tu peux être obsédé·e par la compréhension de la mort, du sexe, du pouvoir, de la psyché profonde.

**Ton approche instinctive** : Le Scorpion te fait plonger sans peur dans les abysses. Tu veux tout savoir, tout comprendre, ne laisser aucun secret intact.

**Tensions possibles** : L'obsession peut remplacer la sagesse. Tu risques de te perdre dans les profondeurs ou de violer les limites de l'autre.

**Conseil clé** : Explorer les mystères avec respect et savoir quand s'arrêter.""",
        'weekly_advice': {
            'week_1': "Choisis un mystère profond à explorer.",
            'week_2': "Plonge avec courage mais respect des limites.",
            'week_3': "Intègre ce que tu découvres avec sagesse.",
            'week_4': "Transforme-toi par ce que tu as compris."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Sagesse transformatrice**

Ta Lune en Gémeaux en Maison 8 veut comprendre les mystères intellectuellement. Ton Ascendant Sagittaire amplifie cette quête : tu veux comprendre le sens philosophique de la mort, de la transformation, de la renaissance.

**Domaine activé** : Maison 8 — Tes transformations cherchent le sens et l'enseignement. Tu veux comprendre pourquoi nous souffrons, pourquoi nous mourons, ce qui se cache derrière les mystères.

**Ton approche instinctive** : Le Sagittaire te fait chercher la sagesse dans les épreuves. Tu veux transformer tes crises en compréhension, tes peurs en foi.

**Tensions possibles** : L'optimisme peut t'empêcher de vraiment vivre les profondeurs. Tu risques de philosopher sur la douleur au lieu de la ressentir.

**Conseil clé** : Chercher le sens tout en acceptant de vivre vraiment les transformations.""",
        'weekly_advice': {
            'week_1': "Explore le sens philosophique de tes épreuves.",
            'week_2': "Cherche la sagesse dans ce qui est difficile.",
            'week_3': "Autorise-toi aussi à simplement ressentir la douleur.",
            'week_4': "Partage la sagesse née de ta transformation."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Maîtrise des profondeurs**

Ta Lune en Gémeaux en Maison 8 veut comprendre les mystères. Ton Ascendant Capricorne structure cette exploration : tu veux maîtriser tes peurs, contrôler les ressources partagées, professionnaliser ta compréhension.

**Domaine activé** : Maison 8 — Tes transformations cherchent la maîtrise et le pouvoir. Tu peux vouloir devenir thérapeute, gérer les finances des autres, avoir du pouvoir sur les ressources partagées.

**Ton approche instinctive** : Le Capricorne te fait aborder les mystères avec sérieux et ambition. Tu veux développer une expertise dans les domaines profonds, être reconnu·e pour cette maîtrise.

**Tensions possibles** : Le besoin de contrôle peut empêcher le vrai lâcher-prise. Tu risques de vouloir tout maîtriser au lieu d'accepter la transformation.

**Conseil clé** : Développer ta maîtrise tout en acceptant de perdre le contrôle parfois.""",
        'weekly_advice': {
            'week_1': "Identifie le domaine profond où tu veux développer une expertise.",
            'week_2': "Apprends avec discipline et sérieux.",
            'week_3': "Autorise-toi aussi des moments de vulnérabilité.",
            'week_4': "Apprécie la maîtrise que tu développes."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Mystères partagés**

Ta Lune en Gémeaux en Maison 8 veut comprendre les mystères intellectuellement. Ton Ascendant Verseau ajoute dimension collective : tu veux partager cette compréhension, démocratiser l'accès aux profondeurs.

**Domaine activé** : Maison 8 — Tes transformations cherchent à servir le collectif. Tu peux vouloir parler publiquement de sujets tabous, créer des communautés de guérison, partager les ressources.

**Ton approche instinctive** : Le Verseau te fait aborder les mystères sans jugement. Tu veux comprendre différemment, connecter des gens autour de ces sujets, innover dans la transformation.

**Tensions possibles** : Le détachement peut t'empêcher de vraiment vivre tes transformations. Tu risques de rester dans l'observation au lieu de plonger.

**Conseil clé** : Partager la compréhension des mystères tout en vivant ta propre transformation.""",
        'weekly_advice': {
            'week_1': "Explore comment partager ta compréhension des profondeurs.",
            'week_2': "Connecte-toi à des communautés de transformation.",
            'week_3': "Vis aussi ta propre transformation personnelle.",
            'week_4': "Contribue à la guérison collective avec ton intelligence."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 8, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Mystique profond**

Ta Lune en Gémeaux en Maison 8 veut comprendre intellectuellement les mystères. Ton Ascendant Poissons ajoute dimension spirituelle : tu veux transcender la compréhension, fusionner avec les mystères plutôt que les analyser.

**Domaine activé** : Maison 8 — Tes transformations oscillent entre mental et mystique. Tu veux à la fois comprendre et te dissoudre dans le mystère, analyser et transcender.

**Ton approche instinctive** : Le Poissons te fait aborder les profondeurs par l'intuition et la spiritualité. Tu peux communiquer avec les morts, canaliser, accéder aux mystères par d'autres voies que l'intellect.

**Tensions possibles** : La confusion peut remplacer la clarté. Tu risques de te perdre dans les profondeurs sans pouvoir en revenir.

**Conseil clé** : Explorer les mystères tout en gardant un ancrage minimal dans le réel.""",
        'weekly_advice': {
            'week_1': "Explore les mystères par l'intuition et le ressenti.",
            'week_2': "Laisse-toi transformer par ce qui dépasse la compréhension.",
            'week_3': "Reviens aussi à la clarté mentale pour intégrer.",
            'week_4': "Remercie les mystères de t'avoir transformé·e."
        }
    },

    # ==================== MAISON 9 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Exploration audacieuse**

Ta Lune en Gémeaux active la Maison 9 : ton besoin d'expansion et de sens passe par l'apprentissage et la communication. Avec l'Ascendant Bélier, tu veux explorer rapidement, découvrir de nouveaux horizons intellectuels sans attendre.

**Domaine activé** : Maison 9 — Tes voyages, ta philosophie, tes études supérieures sont stimulés. Tu veux apprendre sur d'autres cultures, comprendre différentes visions du monde, élargir ta perspective.

**Ton approche instinctive** : Le Bélier te pousse à partir à l'aventure intellectuelle sans peur. Tu peux commencer plusieurs formations, voyager impulsivement, explorer de nouvelles philosophies avec enthousiasme.

**Tensions possibles** : L'impulsivité peut créer de la dispersion. Tu risques de commencer mille apprentissages sans jamais vraiment approfondir un domaine.

**Conseil clé** : Explorer largement tout en s'engageant vraiment dans quelques apprentissages.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans un nouvel apprentissage qui t'excite.",
            'week_2': "Explore avec audace et curiosité.",
            'week_3': "Choisis ensuite ce qui mérite vraiment ton engagement.",
            'week_4': "Célèbre tout ce que tu as découvert."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sagesse pratique**

Ta Lune en Gémeaux en Maison 9 veut explorer et apprendre. Ton Ascendant Taureau ajoute pragmatisme : tu veux que tes apprentissages soient concrets, applicables, qu'ils construisent quelque chose de durable.

**Domaine activé** : Maison 9 — Tes explorations cherchent à la fois expansion et utilité. Tu veux apprendre ce qui a de la valeur réelle, voyager confortablement, développer une philosophie pratique.

**Ton approche instinctive** : Le Taureau te fait apprendre lentement mais profondément. Tu veux maîtriser vraiment ce que tu étudies, pas juste survoler. Cette patience crée une vraie sagesse.

**Tensions possibles** : La lenteur peut frustrer ta curiosité gémeau. Tu risques de te bloquer entre envie d'explorer largement et besoin d'approfondir.

**Conseil clé** : Apprendre progressivement mais solidement, en intégrant vraiment chaque connaissance.""",
        'weekly_advice': {
            'week_1': "Choisis un domaine de connaissance vraiment précieux.",
            'week_2': "Apprends-le méthodiquement et profondément.",
            'week_3': "Applique concrètement ce que tu apprends.",
            'week_4': "Savoure la sagesse pratique que tu as acquise."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Étudiant perpétuel**

Double Gémeaux sur la Maison 9 : tu es un·e éternel·le étudiant·e du monde. Ta soif d'apprendre et de comprendre différentes cultures, philosophies, langues est infinie. Tu veux tout savoir sur tout.

**Domaine activé** : Maison 9 — Tes études et explorations sont au centre de ta vie. Tu peux suivre plusieurs formations simultanément, apprendre plusieurs langues, voyager constamment pour découvrir.

**Ton approche instinctive** : Double Gémeaux te fait papillonner entre tous les savoirs. Tu peux étudier la philosophie grecque le matin et la physique quantique l'après-midi.

**Tensions possibles** : La dispersion extrême peut t'empêcher de développer une vraie expertise. Tu risques de devenir un·e éternel·le débutant·e dans tout.

**Conseil clé** : Explorer largement tout en développant vraiment quelques domaines d'expertise.""",
        'weekly_advice': {
            'week_1': "Liste tout ce que tu veux apprendre ou explorer.",
            'week_2': "Sélectionne 2-3 domaines à vraiment approfondir.",
            'week_3': "Engage-toi dans un apprentissage structuré.",
            'week_4': "Mesure ce que tu as vraiment maîtrisé versus juste découvert."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sagesse nourricière**

Ta Lune en Gémeaux en Maison 9 veut explorer et apprendre. Ton Ascendant Cancer ajoute dimension émotionnelle : tu veux que tes apprentissages nourrissent ton âme, que tes voyages créent un sentiment d'appartenance.

**Domaine activé** : Maison 9 — Tes explorations cherchent à la fois expansion intellectuelle et sécurité émotionnelle. Tu veux apprendre sur ce qui touche ton cœur, voyager pour te sentir chez toi.

**Ton approche instinctive** : Le Cancer te fait chercher une philosophie qui te sécurise. Tu veux des croyances qui te nourrissent affectivement, pas juste intellectuellement.

**Tensions possibles** : La peur de l'inconnu peut limiter tes explorations. Tu risques de rester dans des apprentissages sécurisants au lieu d'oser vraiment l'aventure.

**Conseil clé** : Explorer de nouveaux horizons tout en gardant un sentiment d'appartenance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui nourrit à la fois ton esprit et ton cœur.",
            'week_2': "Explore de nouveaux domaines qui résonnent émotionnellement.",
            'week_3': "Crée-toi un cocon même dans l'exploration.",
            'week_4': "Célèbre la sagesse qui nourrit ton âme."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Sagesse rayonnante**

Ta Lune en Gémeaux en Maison 9 veut explorer et apprendre. Ton Ascendant Lion ajoute besoin de briller : tu veux que tes connaissances te donnent du prestige, enseigner ce que tu apprends, inspirer par ta sagesse.

**Domaine activé** : Maison 9 — Tes apprentissages cherchent la reconnaissance. Tu veux devenir expert·e dans un domaine admiré, enseigner avec charisme, être reconnu·e pour ta sagesse.

**Ton approche instinctive** : Le Lion te fait partager généreusement ce que tu apprends. Tu veux enseigner, inspirer, guider les autres par ta compréhension élargie.

**Tensions possibles** : L'ego peut nuire à ton apprentissage. Tu risques d'apprendre pour impressionner plutôt que par vraie curiosité.

**Conseil clé** : Apprendre avec humilité puis partager avec générosité.""",
        'weekly_advice': {
            'week_1': "Apprends d'abord pour toi, par vraie curiosité.",
            'week_2': "Développe une compréhension profonde et authentique.",
            'week_3': "Ensuite seulement, partage ta sagesse avec fierté.",
            'week_4': "Inspire les autres par ton exemple d'apprentissage."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Expertise méthodique**

Ta Lune en Gémeaux en Maison 9 veut explorer largement. Ton Ascendant Vierge canalise cette énergie : tu veux développer une vraie expertise, apprendre de manière rigoureuse, maîtriser parfaitement quelques domaines.

**Domaine activé** : Maison 9 — Tes apprentissages cherchent la perfection et l'utilité. Tu veux étudier de manière structurée, obtenir des diplômes reconnus, développer des compétences excellentes.

**Ton approche instinctive** : La Vierge te fait étudier avec méthode et rigueur. Tu prends des notes détaillées, tu vérifies tes sources, tu veux vraiment comprendre en profondeur.

**Tensions possibles** : Le perfectionnisme peut bloquer l'exploration. Tu risques de t'enfermer dans un domaine par peur de ne pas tout maîtriser.

**Conseil clé** : Développer une expertise solide tout en gardant une curiosité ouverte.""",
        'weekly_advice': {
            'week_1': "Choisis un domaine à vraiment maîtriser cette année.",
            'week_2': "Étudie-le de manière structurée et rigoureuse.",
            'week_3': "Autorise-toi aussi des explorations plus libres.",
            'week_4': "Apprécie la qualité de l'expertise développée."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Sagesse harmonieuse**

Ta Lune en Gémeaux en Maison 9 veut explorer et apprendre. Ton Ascendant Balance ajoute recherche d'équilibre : tu veux une philosophie qui crée de l'harmonie, apprendre sur la justice et la beauté.

**Domaine activé** : Maison 9 — Tes explorations cherchent l'équilibre et l'esthétique. Tu peux être attiré·e par la philosophie, le droit, l'art, tout ce qui unit beauté et sagesse.

**Ton approche instinctive** : La Balance te fait chercher une vision du monde équilibrée. Tu veux comprendre tous les points de vue, créer des ponts entre les cultures, enseigner l'harmonie.

**Tensions possibles** : Le besoin d'équilibre peut t'empêcher de prendre position. Tu risques de rester neutre au lieu de développer ta propre philosophie.

**Conseil clé** : Comprendre toutes les perspectives tout en développant ta propre vérité.""",
        'weekly_advice': {
            'week_1': "Explore différentes philosophies et visions du monde.",
            'week_2': "Cherche ce qui unit plutôt que ce qui divise.",
            'week_3': "Développe progressivement ta propre synthèse.",
            'week_4': "Partage ta vision harmonieuse avec tact."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Sagesse transformatrice**

Ta Lune en Gémeaux en Maison 9 veut explorer intellectuellement. Ton Ascendant Scorpion ajoute profondeur : tu veux comprendre les philosophies qui transforment, apprendre ce qui change vraiment la vie.

**Domaine activé** : Maison 9 — Tes explorations cherchent la transformation profonde. Tu es attiré·e par les enseignements ésotériques, la psychologie profonde, les philosophies qui révèlent la vérité cachée.

**Ton approche instinctive** : Le Scorpion te fait plonger intensément dans ce que tu étudies. Tu veux comprendre l'essence, pas juste la surface. Cette profondeur crée une vraie sagesse.

**Tensions possibles** : L'obsession peut remplacer l'ouverture. Tu risques de t'enfermer dans une seule philosophie au lieu de rester curieux·se.

**Conseil clé** : Plonger profondément tout en restant ouvert·e à d'autres perspectives.""",
        'weekly_advice': {
            'week_1': "Choisis un enseignement qui te transforme vraiment.",
            'week_2': "Plonge en profondeur dans cette sagesse.",
            'week_3': "Laisse-toi transformer par ce que tu apprends.",
            'week_4': "Intègre cette transformation avec discernement."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Expansion infinie**

Ta Lune en Gémeaux en Maison 9 veut explorer et apprendre. Ton Ascendant Sagittaire, maître naturel de cette maison, amplifie cette soif : tu veux tout explorer, tout comprendre, voyager partout, apprendre toutes les philosophies.

**Domaine activé** : Maison 9 — Tes explorations sont au maximum de leur intensité. Tu peux voyager constamment, étudier plusieurs domaines, enseigner tout en apprenant, vivre une expansion permanente.

**Ton approche instinctive** : Le Sagittaire te fait voir tout en grand. Tu veux comprendre les grands principes, voyager loin, avoir une vision cosmopolite et optimiste du monde.

**Tensions possibles** : L'excès d'expansion peut créer du chaos. Tu risques de te disperser tellement que tu n'ancres rien.

**Conseil clé** : Explorer infiniment tout en ancrant régulièrement tes découvertes.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans une grande aventure d'apprentissage.",
            'week_2': "Explore avec foi et enthousiasme maximum.",
            'week_3': "Prends le temps d'ancrer ce que tu découvres.",
            'week_4': "Partage ta vision élargie avec générosité."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Expertise reconnue**

Ta Lune en Gémeaux en Maison 9 veut explorer et apprendre. Ton Ascendant Capricorne structure cette énergie : tu veux obtenir des diplômes prestigieux, développer une expertise reconnue professionnellement.

**Domaine activé** : Maison 9 — Tes apprentissages cherchent la reconnaissance et l'autorité. Tu veux devenir expert·e dans un domaine respecté, enseigner dans des institutions sérieuses.

**Ton approche instinctive** : Le Capricorne te fait étudier avec ambition et discipline. Tu veux construire méthodiquement une expertise qui te donne du pouvoir et de la crédibilité.

**Tensions possibles** : L'ambition peut étouffer la vraie curiosité. Tu risques de n'étudier que ce qui est utile professionnellement.

**Conseil clé** : Construire une expertise solide sans perdre la joie de l'apprentissage.""",
        'weekly_advice': {
            'week_1': "Identifie le domaine où tu veux être reconnu·e comme expert·e.",
            'week_2': "Engage-toi dans des études sérieuses et structurées.",
            'week_3': "Autorise-toi aussi des explorations ludiques.",
            'week_4': "Mesure les fondations d'expertise construites."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Savoirs alternatifs**

Ta Lune en Gémeaux en Maison 9 veut explorer et apprendre. Ton Ascendant Verseau ajoute originalité : tu es attiré·e par les savoirs alternatifs, les philosophies avant-gardistes, l'apprentissage non-conventionnel.

**Domaine activé** : Maison 9 — Tes explorations cherchent l'innovation et la liberté. Tu peux apprendre en autodidacte, sur internet, dans des domaines futuristes ou marginaux.

**Ton approche instinctive** : Le Verseau te fait expérimenter avec de nouvelles formes d'apprentissage. Tu veux apprendre différemment, connecter des savoirs inattendus, penser l'avenir.

**Tensions possibles** : L'excentricité peut t'isoler intellectuellement. Tu risques de rejeter tout savoir traditionnel par principe.

**Conseil clé** : Innover dans tes apprentissages tout en restant connecté·e aux bases.""",
        'weekly_advice': {
            'week_1': "Explore des domaines ou méthodes d'apprentissage alternatifs.",
            'week_2': "Connecte-toi à des communautés de savoirs avant-gardistes.",
            'week_3': "Intègre aussi quelques bases traditionnelles solides.",
            'week_4': "Partage ta vision innovante de la connaissance."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 9, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sagesse mystique**

Ta Lune en Gémeaux en Maison 9 veut explorer intellectuellement. Ton Ascendant Poissons ajoute dimension spirituelle : tu veux transcender la connaissance intellectuelle, accéder à une sagesse mystique.

**Domaine activé** : Maison 9 — Tes explorations oscillent entre mental et mystique. Tu es attiré·e par les philosophies spirituelles, les enseignements mystiques, l'accès à la connaissance par intuition.

**Ton approche instinctive** : Le Poissons te fait apprendre par osmose et inspiration. Tu peux canaliser des connaissances, comprendre sans avoir étudié, accéder à la sagesse par d'autres voies.

**Tensions possibles** : La confusion peut remplacer la clarté. Tu risques de croire comprendre sans vraiment maîtriser intellectuellement.

**Conseil clé** : Honorer ton accès intuitif à la sagesse tout en structurant tes connaissances.""",
        'weekly_advice': {
            'week_1': "Explore les philosophies et enseignements spirituels.",
            'week_2': "Ouvre-toi à la connaissance intuitive et mystique.",
            'week_3': "Structure aussi intellectuellement ce que tu reçois.",
            'week_4': "Remercie les canaux de sagesse qui s'ouvrent à toi."
        }
    },

    # ==================== MAISON 10 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Carrière dynamique**

Ta Lune en Gémeaux active la Maison 10 : ta carrière et ta réputation publique passent par la communication et l'intellect. Avec l'Ascendant Bélier, tu veux réussir rapidement, être reconnu·e pour ton audace et ta vivacité.

**Domaine activé** : Maison 10 — Ton ambition professionnelle est stimulée. Tu veux être connu·e pour ton intelligence, ta capacité à communiquer, ta polyvalence. Tu cherches une carrière stimulante intellectuellement.

**Ton approche instinctive** : Le Bélier te pousse à foncer vers tes objectifs professionnels. Tu n'as pas peur de te lancer, de changer de voie, de prendre des risques pour ta carrière.

**Tensions possibles** : L'impulsivité peut nuire à ta réputation. Tu risques de changer trop souvent de direction ou de brûler des ponts professionnels.

**Conseil clé** : Foncer vers tes ambitions tout en construisant une réputation solide.""",
        'weekly_advice': {
            'week_1': "Clarifie tes ambitions professionnelles réelles.",
            'week_2': "Prends une initiative courageuse pour ta carrière.",
            'week_3': "Construis aussi ta réputation avec constance.",
            'week_4': "Célèbre le courage dont tu fais preuve."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Succès durable**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle variée. Ton Ascendant Taureau ajoute besoin de stabilité : tu veux construire une réputation solide, une carrière qui dure et qui rapporte.

**Domaine activé** : Maison 10 — Ton ambition professionnelle cherche à la fois variété et sécurité. Tu veux une carrière qui stimule ton esprit tout en te donnant une vraie stabilité financière.

**Ton approche instinctive** : Le Taureau te fait construire ta carrière lentement mais sûrement. Tu veux que ta réputation soit solide, que ton succès soit durable et tangible.

**Tensions possibles** : Le conflit entre besoin de changement et besoin de stabilité peut bloquer ton évolution. Tu oscilles entre envie de tout changer et peur du risque.

**Conseil clé** : Construire une carrière stable qui intègre de la variété intellectuelle.""",
        'weekly_advice': {
            'week_1': "Identifie comment rendre ta carrière plus stimulante.",
            'week_2': "Construis ta réputation avec patience et qualité.",
            'week_3': "Intègre de la variété sans tout remettre en question.",
            'week_4': "Apprécie la solidité de ce que tu construis."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Carrière multiple**

Double Gémeaux sur la Maison 10 : ta carrière et ta réputation publique sont entièrement basées sur ta polyvalence intellectuelle. Tu peux avoir plusieurs métiers, plusieurs identités professionnelles simultanées.

**Domaine activé** : Maison 10 — Ton ambition est de pouvoir exercer plusieurs talents à la fois. Tu veux être reconnu·e pour ta versatilité, ta capacité à jongler entre différents domaines.

**Ton approche instinctive** : Double Gémeaux te fait construire une carrière non-linéaire. Tu peux être journaliste et écrivain·e, consultant·e et formateur·rice, avoir plusieurs casquettes.

**Tensions possibles** : La dispersion peut nuire à ta réputation. Tu risques d'être vu·e comme quelqu'un qui papillonne au lieu de vraiment exceller.

**Conseil clé** : Valoriser ta polyvalence tout en développant quand même quelques expertises claires.""",
        'weekly_advice': {
            'week_1': "Identifie tes 2-3 identités professionnelles principales.",
            'week_2': "Construis une réputation cohérente autour de cette polyvalence.",
            'week_3': "Développe vraiment quelques expertises solides.",
            'week_4': "Célèbre ta capacité unique à exceller dans plusieurs domaines."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Carrière nourricière**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle. Ton Ascendant Cancer ajoute dimension émotionnelle : tu veux une carrière qui nourrit ton âme, où tu prends soin des autres par tes compétences.

**Domaine activé** : Maison 10 — Ton ambition professionnelle cherche à la fois reconnaissance et sens. Tu veux être reconnu·e publiquement mais pour quelque chose qui a vraiment de la valeur humaine.

**Ton approche instinctive** : Le Cancer te fait construire une carrière autour du soin et de la communication. Tu peux être thérapeute, enseignant·e, travailler dans l'aide à travers les mots.

**Tensions possibles** : La sensibilité peut rendre difficile l'exposition publique. Tu risques de prendre trop à cœur les critiques professionnelles.

**Conseil clé** : Construire une carrière publique tout en protégeant ta sensibilité.""",
        'weekly_advice': {
            'week_1': "Identifie comment servir les autres par ton intelligence.",
            'week_2': "Construis une réputation autour de cette mission.",
            'week_3': "Protège ta sensibilité face à l'exposition.",
            'week_4': "Célèbre l'impact nourrissant de ton travail."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Gloire intellectuelle**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle. Ton Ascendant Lion, dans l'axe naturel de cette maison, amplifie cette ambition : tu veux briller publiquement, être célèbre pour ton intelligence.

**Domaine activé** : Maison 10 — Ton ambition est au maximum. Tu veux être reconnu·e, admiré·e, célébré·e pour tes talents intellectuels. Tu cherches une carrière qui te met en lumière.

**Ton approche instinctive** : Le Lion te donne confiance en ta capacité à réussir publiquement. Tu n'as pas peur de la scène, tu veux que ton talent soit vu et apprécié.

**Tensions possibles** : L'ego peut nuire à ta réputation. Tu risques d'être perçu·e comme arrogant·e ou de chercher la célébrité au détriment de la substance.

**Conseil clé** : Briller publiquement tout en restant humble et authentique.""",
        'weekly_advice': {
            'week_1': "Clarifie ce pour quoi tu veux vraiment être reconnu·e.",
            'week_2': "Mets en avant tes talents avec confiance et générosité.",
            'week_3': "Reste connecté·e à ta vraie mission au-delà de l'ego.",
            'week_4': "Inspire les autres par ton exemple de réussite."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Excellence professionnelle**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle. Ton Ascendant Vierge canalise cette ambition : tu veux être reconnu·e pour ton excellence, ta compétence irréprochable, ton professionnalisme.

**Domaine activé** : Maison 10 — Ton ambition professionnelle cherche la perfection. Tu veux développer une expertise remarquable, être respecté·e pour ton sérieux et ta compétence.

**Ton approche instinctive** : La Vierge te fait construire ta carrière avec méthode et rigueur. Tu perfectionnes continuellement tes compétences, tu veux être le·la meilleur·e.

**Tensions possibles** : Le perfectionnisme peut retarder ton avancement. Tu risques de ne jamais te sentir prêt·e ou de te stresser excessivement.

**Conseil clé** : Viser l'excellence tout en acceptant de te montrer imparfait·e.""",
        'weekly_advice': {
            'week_1': "Identifie les compétences professionnelles à perfectionner.",
            'week_2': "Travaille ton métier avec rigueur et dévouement.",
            'week_3': "Ose aussi te montrer avant d'être parfait·e.",
            'week_4': "Apprécie l'excellence que tu as atteinte."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Réputation harmonieuse**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle. Ton Ascendant Balance ajoute dimension esthétique : tu veux être reconnu·e pour ton élégance professionnelle, ta diplomatie, ton sens de l'équité.

**Domaine activé** : Maison 10 — Ton ambition professionnelle cherche la beauté et l'harmonie. Tu peux travailler dans les relations publiques, la communication élégante, tout métier qui unit intellect et esthétique.

**Ton approche instinctive** : La Balance te fait construire ta réputation avec tact et diplomatie. Tu veux être apprécié·e, reconnu·e pour ta capacité à créer de l'harmonie professionnelle.

**Tensions possibles** : Le besoin de plaire peut nuire à ton affirmation professionnelle. Tu risques de ne pas défendre assez tes intérêts par souci d'harmonie.

**Conseil clé** : Construire une réputation harmonieuse tout en t'affirmant clairement.""",
        'weekly_advice': {
            'week_1': "Identifie comment créer plus d'harmonie professionnellement.",
            'week_2': "Construis ta réputation avec élégance et équité.",
            'week_3': "Défends aussi tes intérêts sans culpabilité.",
            'week_4': "Célèbre la beauté de ta présence professionnelle."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir stratégique**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle. Ton Ascendant Scorpion ajoute intensité : tu veux du pouvoir, de l'influence, une réputation qui te donne du contrôle et de l'impact.

**Domaine activé** : Maison 10 — Ton ambition professionnelle est profonde et stratégique. Tu veux comprendre les mécanismes du pouvoir, avoir de l'influence, transformer ton secteur.

**Ton approche instinctive** : Le Scorpion te fait construire ta carrière avec intensité et stratégie. Tu veux maîtriser ton domaine complètement, avoir du pouvoir réel, pas juste de la reconnaissance.

**Tensions possibles** : L'obsession du pouvoir peut nuire à ta réputation. Tu risques d'être perçu·e comme manipulateur·rice ou trop intense.

**Conseil clé** : Construire du pouvoir réel tout en restant éthique et ouvert·e.""",
        'weekly_advice': {
            'week_1': "Identifie le pouvoir que tu veux vraiment développer.",
            'week_2': "Construis ton influence avec stratégie et éthique.",
            'week_3': "Utilise ton pouvoir pour transformer positivement.",
            'week_4': "Apprécie l'impact réel de ton travail."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Carrière inspirante**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle. Ton Ascendant Sagittaire amplifie cette vision : tu veux une carrière qui inspire, qui enseigne, qui a un impact philosophique ou culturel.

**Domaine activé** : Maison 10 — Ton ambition professionnelle cherche le sens et l'expansion. Tu veux être reconnu·e pour ton enseignement, ta vision, ta capacité à inspirer à grande échelle.

**Ton approche instinctive** : Le Sagittaire te fait construire une carrière généreuse et optimiste. Tu veux partager ta sagesse, enseigner, avoir un impact positif sur le monde.

**Tensions possibles** : Le manque de pragmatisme peut nuire à ta carrière. Tu risques d'avoir de grandes visions sans les concrétiser vraiment.

**Conseil clé** : Viser l'inspiration et l'impact tout en construisant concrètement.""",
        'weekly_advice': {
            'week_1': "Clarifie la vision inspirante de ta carrière.",
            'week_2': "Partage généreusement ta sagesse et ton enseignement.",
            'week_3': "Ancre aussi tes ambitions dans des actions concrètes.",
            'week_4': "Célèbre l'impact inspirant de ton travail."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Autorité intellectuelle**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle. Ton Ascendant Capricorne, maître naturel de cette maison, structure cette ambition : tu veux devenir une autorité reconnue dans ton domaine.

**Domaine activé** : Maison 10 — Ton ambition professionnelle est au maximum de son sérieux. Tu veux construire méthodiquement une carrière prestigieuse, être respecté·e comme expert·e.

**Ton approche instinctive** : Le Capricorne te fait grimper les échelons avec patience et détermination. Tu veux du prestige, de l'autorité, une réputation inébranlable.

**Tensions possibles** : La rigidité peut étouffer ta créativité. Tu risques de sacrifier ta curiosité naturelle sur l'autel de l'ambition.

**Conseil clé** : Construire une autorité solide sans perdre ta légèreté et ta curiosité.""",
        'weekly_advice': {
            'week_1': "Clarifie tes ambitions professionnelles à long terme.",
            'week_2': "Travaille avec discipline et ambition claire.",
            'week_3': "Autorise-toi aussi des moments de légèreté créative.",
            'week_4': "Mesure l'autorité et la réputation construites."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Carrière visionnaire**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle. Ton Ascendant Verseau ajoute originalité : tu veux une carrière non-conventionnelle, qui innove, qui contribue au progrès collectif.

**Domaine activé** : Maison 10 — Ton ambition professionnelle cherche l'innovation et l'impact collectif. Tu veux être reconnu·e comme visionnaire, pionnier·ère dans ton domaine.

**Ton approche instinctive** : Le Verseau te fait construire une carrière différente. Tu peux être entrepreneur·e, travailler dans la tech, innover dans ton secteur professionnel.

**Tensions possibles** : L'excentricité peut nuire à ta crédibilité. Tu risques d'être trop en avance ou de rejeter toute structure par principe.

**Conseil clé** : Innover professionnellement tout en construisant une vraie crédibilité.""",
        'weekly_advice': {
            'week_1': "Identifie comment innover dans ton domaine professionnel.",
            'week_2': "Expérimente avec de nouvelles approches ou technologies.",
            'week_3': "Construis aussi une base solide et crédible.",
            'week_4': "Célèbre ton impact innovant sur ton secteur."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 10, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Carrière inspirée**

Ta Lune en Gémeaux en Maison 10 veut une carrière intellectuelle. Ton Ascendant Poissons ajoute dimension spirituelle : tu veux une carrière qui soit une vocation, qui serve quelque chose de plus grand.

**Domaine activé** : Maison 10 — Ton ambition professionnelle oscille entre mental et mystique. Tu veux être reconnu·e pour ton talent créatif, ton intuition, ta capacité à inspirer spirituellement.

**Ton approche instinctive** : Le Poissons te fait suivre ton intuition professionnelle. Tu peux avoir une carrière artistique, thérapeutique, spirituelle, qui ne suit pas de logique conventionnelle.

**Tensions possibles** : Le manque de structure peut nuire à ta carrière. Tu risques d'être peu fiable professionnellement ou de fuir les responsabilités.

**Conseil clé** : Suivre ton inspiration tout en maintenant une structure professionnelle minimale.""",
        'weekly_advice': {
            'week_1': "Identifie ce que ton âme veut vraiment accomplir professionnellement.",
            'week_2': "Suis ton intuition dans tes choix de carrière.",
            'week_3': "Crée quand même une structure minimale viable.",
            'week_4': "Remercie la guidance qui t'oriente vers ta vocation."
        }
    },

    # ==================== MAISON 11 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Réseau dynamique**

Ta Lune en Gémeaux active la Maison 11 : tes amitiés et tes projets collectifs passent par la communication et l'échange d'idées. Avec l'Ascendant Bélier, tu veux créer rapidement des connexions, lancer des projets audacieux.

**Domaine activé** : Maison 11 — Ton réseau social et tes amitiés sont stimulés. Tu veux rencontrer de nouvelles personnes, échanger des idées, construire des projets collectifs intellectuellement stimulants.

**Ton approche instinctive** : Le Bélier te pousse à initier des connexions sans attendre. Tu crées facilement du lien, tu n'as pas peur d'aborder les gens, de proposer des collaborations.

**Tensions possibles** : L'impulsivité peut créer des conflits dans tes groupes. Tu risques de foncer sans considérer l'avis du collectif.

**Conseil clé** : Créer du lien avec audace tout en respectant la dynamique de groupe.""",
        'weekly_advice': {
            'week_1': "Initie de nouvelles connexions intellectuelles.",
            'week_2': "Lance un projet collaboratif qui t'excite.",
            'week_3': "Écoute aussi les besoins et idées des autres.",
            'week_4': "Célèbre la vitalité de ton réseau."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Amitié durable**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles stimulantes. Ton Ascendant Taureau ajoute besoin de stabilité : tu cherches des amitiés qui durent, des groupes où tu te sens en sécurité.

**Domaine activé** : Maison 11 — Tes amitiés cherchent à la fois stimulation intellectuelle et solidité. Tu veux des ami·e·s avec qui tu peux échanger sur tout tout en construisant une vraie fidélité.

**Ton approche instinctive** : Le Taureau te fait choisir soigneusement tes ami·e·s. Tu construis lentement ton cercle mais une fois qu'une personne est dedans, c'est pour longtemps.

**Tensions possibles** : Le besoin de stabilité peut limiter ton réseau. Tu risques de t'enfermer dans un cercle trop étroit par peur du changement.

**Conseil clé** : Cultiver des amitiés solides tout en restant ouvert·e à de nouvelles connexions.""",
        'weekly_advice': {
            'week_1': "Identifie les amitiés qui méritent vraiment ton investissement.",
            'week_2': "Nourris ces liens avec constance et loyauté.",
            'week_3': "Ouvre-toi aussi à quelques nouvelles connexions.",
            'week_4': "Apprécie la solidité de ton cercle."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Réseau infini**

Double Gémeaux sur la Maison 11 : tes amitiés et ton réseau social sont au centre de ta vie. Tu as des centaines de connaissances, tu es connecté·e à mille communautés, tu es l'ambassadeur·rice de ton réseau.

**Domaine activé** : Maison 11 — Ton réseau social est immense et diversifié. Tu connais des gens de tous horizons, tu crées constamment de nouvelles connexions, tu es le·la lien entre différents groupes.

**Ton approche instinctive** : Double Gémeaux te fait papillonner socialement. Tu peux avoir des conversations avec dix personnes simultanément, connecter des gens entre eux constamment.

**Tensions possibles** : La superficialité peut remplacer la vraie amitié. Tu risques d'avoir mille connaissances sans vraiment d'ami·e·s proches.

**Conseil clé** : Cultiver un large réseau tout en approfondissant quelques vraies amitiés.""",
        'weekly_advice': {
            'week_1': "Identifie parmi ton réseau qui mérite une vraie amitié.",
            'week_2': "Approfondis quelques connexions plutôt que d'en créer mille.",
            'week_3': "Continue aussi à élargir ton réseau stratégiquement.",
            'week_4': "Célèbre ta capacité unique à connecter les gens."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Communauté nourricière**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles. Ton Ascendant Cancer ajoute profondeur émotionnelle : tu veux des ami·e·s qui soient comme une famille, des groupes où tu te sens vraiment chez toi.

**Domaine activé** : Maison 11 — Tes amitiés cherchent à la fois stimulation intellectuelle et sécurité affective. Tu veux des communautés où tu peux être vulnérable tout en échangeant librement.

**Ton approche instinctive** : Le Cancer te fait chercher une vraie intimité dans l'amitié. Tu veux des ami·e·s avec qui tu peux tout partager, qui te nourrissent émotionnellement.

**Tensions possibles** : La sensibilité peut créer des drames dans tes groupes. Tu risques de prendre trop personnellement les dynamiques collectives.

**Conseil clé** : Créer des amitiés profondes tout en gardant des limites saines.""",
        'weekly_advice': {
            'week_1': "Identifie qui dans ton réseau te nourrit vraiment.",
            'week_2': "Crée de l'intimité authentique avec ces personnes.",
            'week_3': "Protège ta sensibilité dans les groupes plus larges.",
            'week_4': "Célèbre la famille que tu as choisie."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Leader du réseau**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles. Ton Ascendant Lion ajoute besoin de briller : tu veux être au centre de ton réseau, admirer·e par tes ami·e·s, leader de tes communautés.

**Domaine activé** : Maison 11 — Tes amitiés et groupes cherchent ta présence rayonnante. Tu veux être reconnu·e dans tes communautés, admiré·e pour ton intelligence et ton charisme.

**Ton approche instinctive** : Le Lion te fait naturellement devenir leader dans tes groupes. Tu animes, tu inspires, tu fédères les gens autour de projets collectifs.

**Tensions possibles** : L'ego peut nuire à tes amitiés. Tu risques de vouloir monopoliser l'attention au détriment de l'égalité relationnelle.

**Conseil clé** : Briller dans ton réseau tout en célébrant aussi les autres.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu veux contribuer à tes communautés.",
            'week_2': "Prends un rôle de leadership avec générosité.",
            'week_3': "Célèbre aussi les talents des autres membres.",
            'week_4': "Apprécie l'impact positif de ta présence."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Réseau utile**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles. Ton Ascendant Vierge canalise cette énergie : tu veux des ami·e·s avec qui tu peux t'entraider concrètement, des groupes qui servent un but utile.

**Domaine activé** : Maison 11 — Tes amitiés et projets collectifs cherchent l'utilité et l'amélioration mutuelle. Tu veux des groupes de travail, des ami·e·s qui t'aident à progresser.

**Ton approche instinctive** : La Vierge te fait sélectionner soigneusement ton réseau. Tu veux des connexions de qualité, des ami·e·s fiables, des collaborations qui fonctionnent vraiment.

**Tensions possibles** : L'exigence peut créer de la critique dans tes groupes. Tu risques de pointer les défauts au lieu d'apprécier les qualités.

**Conseil clé** : Cultiver un réseau de qualité tout en acceptant l'imperfection humaine.""",
        'weekly_advice': {
            'week_1': "Identifie les connexions vraiment constructives dans ton réseau.",
            'week_2': "Investis dans ces relations avec attention et service.",
            'week_3': "Accepte aussi les imperfections de tes ami·e·s.",
            'week_4': "Apprécie la qualité des liens cultivés."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie collective**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles. Ton Ascendant Balance, en affinité avec cette maison, amplifie cette énergie : tu veux créer de l'harmonie dans tes groupes, des amitiés équilibrées.

**Domaine activé** : Maison 11 — Tes amitiés et projets collectifs cherchent la beauté et l'équité. Tu es le·la pacificateur·rice de tes groupes, celui·celle qui crée du lien et de l'équilibre.

**Ton approche instinctive** : La Balance te fait naturellement harmoniser les dynamiques de groupe. Tu veux que tout le monde s'entende, que les projets collectifs soient justes et agréables.

**Tensions possibles** : Le besoin d'harmonie peut t'empêcher d'exprimer tes vrais besoins. Tu risques de te sacrifier pour la paix du groupe.

**Conseil clé** : Créer de l'harmonie collective tout en t'affirmant clairement.""",
        'weekly_advice': {
            'week_1': "Identifie les déséquilibres dans tes groupes ou amitiés.",
            'week_2': "Facilite le dialogue et la compréhension mutuelle.",
            'week_3': "Exprime aussi tes propres besoins avec clarté.",
            'week_4': "Célèbre l'harmonie que tu crées naturellement."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Connexions intenses**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles légères. Ton Ascendant Scorpion ajoute profondeur : tu veux des ami·e·s avec qui tu peux vraiment fusionner, des groupes qui te transforment.

**Domaine activé** : Maison 11 — Tes amitiés oscillent entre légèreté intellectuelle et intensité émotionnelle. Tu veux pouvoir tout discuter avec tes ami·e·s tout en vivant une vraie intimité transformatrice.

**Ton approche instinctive** : Le Scorpion te fait chercher l'authenticité absolue dans l'amitié. Tu veux des ami·e·s qui te connaissent vraiment, avec qui aucun secret n'existe.

**Tensions possibles** : L'intensité peut effrayer ou étouffer. Tu risques de devenir possessif·ve en amitié ou de créer des drames dans tes groupes.

**Conseil clé** : Cultiver des amitiés profondes tout en respectant les limites de chacun·e.""",
        'weekly_advice': {
            'week_1': "Identifie qui mérite vraiment ton intimité authentique.",
            'week_2': "Crée de la profondeur avec ces personnes.",
            'week_3': "Autorise aussi des connexions plus légères.",
            'week_4': "Apprécie la transformation que tes ami·e·s t'offrent."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Réseau mondial**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles. Ton Ascendant Sagittaire amplifie cette ouverture : tu veux un réseau international, des ami·e·s de toutes cultures, des groupes qui partagent ta vision.

**Domaine activé** : Maison 11 — Tes amitiés et projets collectifs cherchent l'expansion et la diversité. Tu connectes des gens de partout, tu crées des ponts entre cultures.

**Ton approche instinctive** : Le Sagittaire te fait chercher des ami·e·s qui t'inspirent et t'élargissent. Tu veux des connexions qui te font grandir, qui ouvrent de nouveaux horizons.

**Tensions possibles** : Le manque d'ancrage peut créer de la superficialité. Tu risques d'avoir des ami·e·s partout sans vraie profondeur nulle part.

**Conseil clé** : Élargir ton réseau mondialement tout en approfondissant quelques liens.""",
        'weekly_advice': {
            'week_1': "Connecte-toi à de nouvelles personnes d'horizons variés.",
            'week_2': "Explore des projets collectifs à vision large.",
            'week_3': "Approfondis aussi quelques amitiés vraiment importantes.",
            'week_4': "Célèbre la richesse culturelle de ton réseau."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Réseau stratégique**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles. Ton Ascendant Capricorne structure ce réseau : tu veux des connexions utiles professionnellement, des ami·e·s qui t'aident à avancer.

**Domaine activé** : Maison 11 — Tes amitiés et projets collectifs cherchent l'utilité et l'ambition. Tu construis un réseau qui sert tes objectifs, des connexions qui ont de la valeur stratégique.

**Ton approche instinctive** : Le Capricorne te fait sélectionner soigneusement tes connexions. Tu investis dans les relations qui peuvent t'aider professionnellement ou qui partagent tes ambitions.

**Tensions possibles** : L'utilitarisme peut étouffer la vraie amitié. Tu risques de voir tes relations uniquement comme des opportunités.

**Conseil clé** : Construire un réseau stratégique sans perdre l'authenticité des liens.""",
        'weekly_advice': {
            'week_1': "Identifie les connexions stratégiques importantes pour toi.",
            'week_2': "Investis dans ces relations avec intention claire.",
            'week_3': "Cultive aussi des amitiés purement par affinité.",
            'week_4': "Apprécie la solidité du réseau construit."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Communauté visionnaire**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles. Ton Ascendant Verseau, maître naturel de cette maison, amplifie cette énergie : tu veux créer des communautés innovantes, des réseaux d'avant-garde.

**Domaine activé** : Maison 11 — Tes amitiés et projets collectifs sont au maximum de leur originalité. Tu connectes des esprits visionnaires, tu crées des groupes qui changent le monde.

**Ton approche instinctive** : Le Verseau te fait naturellement créer des communautés alternatives. Tu es attiré·e par les gens originaux, les groupes qui innovent, les mouvements progressistes.

**Tensions possibles** : L'excentricité peut t'isoler. Tu risques de rejeter toute amitié conventionnelle ou de rester uniquement dans des bulles alternatives.

**Conseil clé** : Innover dans tes connexions tout en restant accessible et inclusif·ve.""",
        'weekly_advice': {
            'week_1': "Connecte-toi à des esprits visionnaires et innovants.",
            'week_2': "Crée ou rejoins des communautés d'avant-garde.",
            'week_3': "Reste aussi ouvert·e à des connexions plus ordinaires.",
            'week_4': "Célèbre l'impact de ton réseau sur le progrès collectif."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 11, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Connexion spirituelle**

Ta Lune en Gémeaux en Maison 11 veut des amitiés intellectuelles. Ton Ascendant Poissons ajoute dimension spirituelle : tu veux des ami·e·s d'âme, des communautés qui partagent une vision mystique ou créative.

**Domaine activé** : Maison 11 — Tes amitiés oscillent entre mental et spirituel. Tu veux pouvoir échanger intellectuellement tout en vivant une connexion d'âme profonde.

**Ton approche instinctive** : Le Poissons te fait chercher des ami·e·s avec qui tu as une connexion intuitive. Tu peux sentir immédiatement qui est vraiment de ta tribu.

**Tensions possibles** : L'idéalisation peut créer des déceptions. Tu risques de projeter sur tes ami·e·s plus qu'ils·elles ne peuvent offrir.

**Conseil clé** : Cultiver des connexions spirituelles tout en restant ancré·e dans la réalité des personnes.""",
        'weekly_advice': {
            'week_1': "Identifie avec qui tu ressens une vraie connexion d'âme.",
            'week_2': "Nourris ces amitiés spirituellement et créativement.",
            'week_3': "Accepte aussi les limites humaines de tes ami·e·s.",
            'week_4': "Remercie ta tribu d'âme pour sa présence."
        }
    },

    # ==================== MAISON 12 ====================

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Pensée libérée**

Ta Lune en Gémeaux active la Maison 12 : ton inconscient, ta spiritualité, ton besoin de solitude passent par le mental et la compréhension. Avec l'Ascendant Bélier, tu veux comprendre rapidement tes ombres, libérer tes pensées.

**Domaine activé** : Maison 12 — Ton inconscient veut être compris, nommé, intégré. Tu as besoin de moments de solitude intellectuelle pour digérer, comprendre, te reconnecter à ton intuition.

**Ton approche instinctive** : Le Bélier te pousse à affronter courageusement ton ombre. Tu veux comprendre tes peurs, nommer tes démons, libérer ce qui était caché.

**Tensions possibles** : L'impatience peut t'empêcher de vraiment plonger. Tu risques de vouloir tout comprendre trop vite au lieu d'accepter le mystère.

**Conseil clé** : Explorer ton inconscient avec courage tout en acceptant le processus lent.""",
        'weekly_advice': {
            'week_1': "Crée des moments de solitude pour réfléchir profondément.",
            'week_2': "Nomme courageusement ce qui était caché en toi.",
            'week_3': "Accepte aussi que tout ne peut pas être compris immédiatement.",
            'week_4': "Célèbre la libération mentale obtenue."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Repos mental**

Ta Lune en Gémeaux en Maison 12 a besoin de comprendre son inconscient. Ton Ascendant Taureau ajoute besoin de repos : tu veux créer un sanctuaire mental, ralentir ta pensée, trouver la paix intérieure.

**Domaine activé** : Maison 12 — Ton inconscient te demande du repos. Tu as besoin de te retirer du bruit mental constant, de créer du silence intérieur, de te ressourcer profondément.

**Ton approche instinctive** : Le Taureau te fait chercher la sécurité dans la solitude. Tu veux un espace confortable où tu peux te retirer, méditer, simplement être sans penser.

**Tensions possibles** : La peur du vide mental peut te bloquer. Tu risques de fuir le silence en remplissant ton esprit constamment.

**Conseil clé** : Accepter de ralentir mentalement et de créer du vide intérieur.""",
        'weekly_advice': {
            'week_1': "Crée un espace physique confortable pour te retirer.",
            'week_2': "Pratique le silence mental régulièrement.",
            'week_3': "Accepte de ne rien faire, de ne rien comprendre parfois.",
            'week_4': "Savoure la paix intérieure retrouvée."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Mental mystique**

Double Gémeaux sur la Maison 12 : ton inconscient est intellectuel. Tu explores ton ombre par les mots, l'écriture, la compréhension. Tu as besoin de solitude pour penser librement.

**Domaine activé** : Maison 12 — Ton inconscient veut communiquer. Tu peux recevoir des intuitions sous forme de mots, des messages de ton âme par l'écriture automatique.

**Ton approche instinctive** : Double Gémeaux te fait explorer ton inconscient intellectuellement. Tu peux tenir un journal intime, écrire pour comprendre tes rêves, analyser tes schémas.

**Tensions possibles** : L'intellectualisation peut t'empêcher de vraiment lâcher prise. Tu risques de trop analyser ton inconscient au lieu de simplement le ressentir.

**Conseil clé** : Comprendre ton inconscient tout en acceptant aussi l'inexplicable.""",
        'weekly_advice': {
            'week_1': "Écris librement pour explorer ton inconscient.",
            'week_2': "Analyse tes rêves et tes intuitions.",
            'week_3': "Autorise-toi aussi le silence et le non-mental.",
            'week_4': "Intègre ce que ton inconscient t'a révélé."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Refuge intérieur**

Ta Lune en Gémeaux en Maison 12 a besoin de comprendre intellectuellement. Ton Ascendant Cancer, en exil ici, ajoute profondeur émotionnelle : tu veux créer un vrai refuge intérieur où mental et émotionnel se rencontrent.

**Domaine activé** : Maison 12 — Ton inconscient cherche à la fois compréhension et guérison émotionnelle. Tu as besoin de solitude pour pleurer, comprendre, te nourrir intérieurement.

**Ton approche instinctive** : Le Cancer te fait chercher la sécurité dans le retrait. Tu veux un cocon où tu peux être complètement vulnérable avec toi-même.

**Tensions possibles** : L'isolement peut devenir excessif. Tu risques de te couper du monde par peur ou sensibilité blessée.

**Conseil clé** : Te retirer pour guérir tout en restant connecté·e au monde.""",
        'weekly_advice': {
            'week_1': "Crée un espace sécurisant pour explorer tes émotions.",
            'week_2': "Autorise-toi à ressentir profondément dans la solitude.",
            'week_3': "Reviens progressivement vers les autres.",
            'week_4': "Célèbre la guérison intérieure accomplie."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Créativité cachée**

Ta Lune en Gémeaux en Maison 12 a besoin de solitude mentale. Ton Ascendant Lion ajoute dimension créative : tu veux exprimer ton inconscient par l'art, la créativité secrète.

**Domaine activé** : Maison 12 — Ton inconscient veut créer. Tu peux avoir des inspirations en solitude, écrire en secret, créer sans montrer, explorer ton âme par l'expression.

**Ton approche instinctive** : Le Lion te fait transformer ton exploration intérieure en quelque chose de beau. Tu peux tenir un journal artistique, créer pour toi seul·e.

**Tensions possibles** : Le besoin de reconnaissance peut entrer en conflit avec le besoin de secret. Tu oscilles entre vouloir montrer et vouloir cacher.

**Conseil clé** : Créer d'abord pour toi, partager ensuite si c'est juste.""",
        'weekly_advice': {
            'week_1': "Crée seul·e, sans public, juste pour ton âme.",
            'week_2': "Exprime ce qui émerge de ton inconscient.",
            'week_3': "Décide ensuite ce qui mérite d'être partagé.",
            'week_4': "Honore ta créativité sacrée et privée."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Purification mentale**

Ta Lune en Gémeaux en Maison 12 a besoin de comprendre son inconscient. Ton Ascendant Vierge canalise cette énergie : tu veux purifier ton mental, analyser tes schémas, guérir méthodiquement.

**Domaine activé** : Maison 12 — Ton inconscient cherche la guérison par la compréhension. Tu peux être attiré·e par la thérapie, l'analyse de tes rêves, tout ce qui permet de purifier ton mental.

**Ton approche instinctive** : La Vierge te fait aborder ton inconscient avec méthode. Tu veux identifier tes schémas, comprendre tes blocages, améliorer progressivement ton monde intérieur.

**Tensions possibles** : L'analyse excessive peut bloquer la vraie guérison. Tu risques de trop intellectualiser au lieu de simplement lâcher prise.

**Conseil clé** : Analyser pour guérir tout en acceptant le mystère de l'âme.""",
        'weekly_advice': {
            'week_1': "Identifie un schéma inconscient à comprendre et guérir.",
            'week_2': "Travaille-le méthodiquement avec bienveillance.",
            'week_3': "Accepte aussi ce qui ne peut pas être compris.",
            'week_4': "Apprécie la purification mentale accomplie."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Paix intérieure**

Ta Lune en Gémeaux en Maison 12 a besoin de comprendre intellectuellement. Ton Ascendant Balance ajoute recherche d'harmonie : tu veux créer la paix dans ton monde intérieur, équilibrer tes pensées.

**Domaine activé** : Maison 12 — Ton inconscient cherche l'équilibre et la beauté. Tu veux pacifier ton mental, créer de l'harmonie entre tes différentes parts intérieures.

**Ton approche instinctive** : La Balance te fait chercher la réconciliation intérieure. Tu veux que toutes tes voix intérieures puissent coexister harmonieusement.

**Tensions possibles** : Le besoin d'harmonie peut créer du déni. Tu risques d'éviter de regarder les parts sombres qui dérangent ton équilibre.

**Conseil clé** : Chercher la paix intérieure tout en acceptant aussi l'ombre.""",
        'weekly_advice': {
            'week_1': "Identifie les conflits intérieurs qui dérangent ta paix.",
            'week_2': "Cherche à les réconcilier avec douceur.",
            'week_3': "Accepte aussi que certaines tensions sont normales.",
            'week_4': "Célèbre l'harmonie intérieure retrouvée."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Plongée totale**

Ta Lune en Gémeaux en Maison 12 veut comprendre intellectuellement son inconscient. Ton Ascendant Scorpion amplifie cette exploration : tu veux plonger dans les abysses de ton âme, tout comprendre de ton ombre.

**Domaine activé** : Maison 12 — Ton inconscient veut être complètement exploré. Tu n'as pas peur de regarder ce qui est caché, tu veux comprendre tes peurs les plus profondes.

**Ton approche instinctive** : Le Scorpion te fait plonger sans peur dans ton ombre. Tu peux être obsédé·e par ton inconscient, vouloir tout analyser, tout transformer.

**Tensions possibles** : L'obsession peut t'emprisonner dans ton monde intérieur. Tu risques de te perdre dans tes abysses sans pouvoir en ressortir.

**Conseil clé** : Explorer profondément tout en gardant un lien avec la lumière.""",
        'weekly_advice': {
            'week_1': "Plonge courageusement dans ton ombre.",
            'week_2': "Explore ce qui était caché avec honnêteté.",
            'week_3': "Reviens régulièrement à la surface pour respirer.",
            'week_4': "Transforme-toi par ce que tu as découvert."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foi intuitive**

Ta Lune en Gémeaux en Maison 12 veut comprendre intellectuellement. Ton Ascendant Sagittaire, en exil ici, ajoute besoin de sens : tu veux comprendre le sens spirituel de ton inconscient, avoir foi en ton processus intérieur.

**Domaine activé** : Maison 12 — Ton inconscient cherche la sagesse et le sens. Tu veux comprendre pourquoi tu as certains schémas, quel est le sens spirituel de tes épreuves.

**Ton approche instinctive** : Le Sagittaire te fait chercher la sagesse dans ton inconscient. Tu veux transformer tes blessures en enseignements, ton ombre en lumière.

**Tensions possibles** : L'optimisme peut créer du déni. Tu risques de vouloir tout positiver au lieu d'accepter vraiment ton ombre.

**Conseil clé** : Chercher le sens tout en acceptant aussi l'absurde et la douleur.""",
        'weekly_advice': {
            'week_1': "Explore le sens spirituel de tes schémas inconscients.",
            'week_2': "Cherche la sagesse dans tes blessures.",
            'week_3': "Accepte aussi ce qui reste mystérieux ou douloureux.",
            'week_4': "Partage la sagesse née de ton exploration intérieure."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Structure intérieure**

Ta Lune en Gémeaux en Maison 12 veut comprendre son inconscient. Ton Ascendant Capricorne structure cette exploration : tu veux maîtriser ton monde intérieur, construire une discipline spirituelle.

**Domaine activé** : Maison 12 — Ton inconscient cherche l'ordre et la maîtrise. Tu veux développer une pratique spirituelle régulière, comprendre méthodiquement tes schémas.

**Ton approche instinctive** : Le Capricorne te fait aborder ton inconscient avec sérieux et discipline. Tu peux méditer quotidiennement, tenir un journal rigoureux, suivre une thérapie structurée.

**Tensions possibles** : Le besoin de contrôle peut bloquer le lâcher-prise nécessaire. Tu risques de vouloir tout maîtriser au lieu d'accepter le mystère.

**Conseil clé** : Construire une pratique intérieure solide tout en acceptant de perdre le contrôle.""",
        'weekly_advice': {
            'week_1': "Crée une pratique spirituelle régulière et structurée.",
            'week_2': "Explore ton inconscient avec discipline et patience.",
            'week_3': "Autorise-toi aussi des moments de lâcher-prise total.",
            'week_4': "Apprécie la structure intérieure que tu as construite."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Conscience collective**

Ta Lune en Gémeaux en Maison 12 veut comprendre son inconscient. Ton Ascendant Verseau ajoute dimension collective : tu veux comprendre l'inconscient collectif, connecter à la conscience universelle.

**Domaine activé** : Maison 12 — Ton inconscient se connecte au transpersonnel. Tu peux recevoir des intuitions pour le collectif, canaliser des informations, comprendre les schémas collectifs.

**Ton approche instinctive** : Le Verseau te fait explorer ton inconscient de manière non-conventionnelle. Tu peux méditer avec des technologies, explorer des pratiques alternatives.

**Tensions possibles** : La dépersonnalisation peut te faire perdre ton ancrage. Tu risques de te perdre dans le collectif au lieu de guérir ton individuel.

**Conseil clé** : Explorer la conscience collective tout en restant ancré·e dans ton individuation.""",
        'weekly_advice': {
            'week_1': "Explore des pratiques spirituelles innovantes ou technologiques.",
            'week_2': "Connecte-toi à la conscience collective avec intention.",
            'week_3': "Reviens aussi à ton inconscient personnel.",
            'week_4': "Intègre ce que tu as reçu pour le bien collectif."
        }
    },

    {
        'moon_sign': 'Gemini', 'moon_house': 12, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution mystique**

Ta Lune en Gémeaux en Maison 12 veut comprendre intellectuellement. Ton Ascendant Poissons, maître naturel de cette maison, amplifie l'énergie mystique : tu veux transcender la compréhension, fusionner avec le divin.

**Domaine activé** : Maison 12 — Ton inconscient veut se dissoudre dans l'universel. Tu peux vivre des expériences mystiques, canaliser, accéder à des états de conscience modifiés.

**Ton approche instinctive** : Le Poissons te fait lâcher le mental pour plonger dans l'océan de l'inconscient. Tu peux méditer profondément, rêver lucidement, vivre dans le flow.

**Tensions possibles** : La dissolution peut devenir de la confusion totale. Tu risques de te perdre complètement sans pouvoir revenir au réel.

**Conseil clé** : Plonger dans le mystique tout en gardant un fil d'Ariane vers le réel.""",
        'weekly_advice': {
            'week_1': "Autorise-toi à lâcher complètement le contrôle mental.",
            'week_2': "Explore des états de conscience modifiés avec respect.",
            'week_3': "Reviens régulièrement au concret pour t'ancrer.",
            'week_4': "Remercie le mystère de ce qu'il t'a révélé."
        }
    },

]

if __name__ == "__main__":
    print(f"Insertion de {len(BATCH)} interprétations Gemini...")
    asyncio.run(insert_batch(BATCH))
    print("✅ Batch Gemini complet inséré!")
