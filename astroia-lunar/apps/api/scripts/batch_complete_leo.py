"""Batch complet: Leo - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # ==================== MAISON 1 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Flamme rayonnante**

Ce mois-ci, tu es double feu : Lune en Lion en Maison 1, Ascendant lunaire Bélier. L'énergie est théâtrale, spontanée, tournée vers l'expression de soi avec panache. Tu ressens un besoin viscéral de briller, d'être vu·e, de montrer ta créativité au monde. Tes émotions demandent une scène.

**Domaine activé** : Maison 1 — Ton identité personnelle est en mode star. Tu veux rayonner, être reconnu·e pour qui tu es vraiment. Ton image, ton style, ta présence physique demandent de l'attention et de la grandeur.

**Ton approche instinctive** : Avec l'Ascendant Bélier, tu ne cherches pas l'approbation : tu imposes ta présence. Face aux obstacles, tu fonces avec courage et panache. Cette audace te rend magnétique mais peut sembler arrogante.

**Tensions possibles** : L'ego surdimensionné peut créer des conflits. Le besoin d'être au centre peut t'isoler si tu ne laisses pas de place aux autres. L'impatience face au manque de reconnaissance.

**Conseil clé** : Canaliser cette énergie solaire vers une expression créative authentique qui inspire les autres.""",
        'weekly_advice': {
            'week_1': "Ose te montrer sous ton meilleur jour sans fausse modestie.",
            'week_2': "Prends une initiative audacieuse qui exprime ta personnalité.",
            'week_3': "Partage ta lumière sans écraser celle des autres.",
            'week_4': "Célèbre ton rayonnement et prépare ton prochain acte créatif."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Présence majestueuse**

Ta Lune en Lion en Maison 1 veut briller et être admirée. Ton Ascendant lunaire Taureau ajoute une dimension de dignité calme : tu veux rayonner, mais avec élégance et stabilité. Le spectacle rencontre le bon goût.

**Domaine activé** : Maison 1 — Ton identité cherche à s'exprimer avec noblesse. Tu veux être reconnu·e non seulement pour ton éclat, mais pour ta substance, ta constance, ta qualité durable. L'image compte énormément.

**Ton approche instinctive** : Le Taureau te fait construire ta présence lentement mais sûrement. Tu veux que ton rayonnement soit solide, pas éphémère. Cette approche tempère le besoin de reconnaissance immédiate du Lion.

**Tensions possibles** : L'impatience de briller (Lion) contre le besoin de perfection stable (Taureau). Tu peux te frustrer si ton rayonnement ne se construit pas assez vite ou si tu te sens incompris·e.

**Conseil clé** : Bâtir une présence qui dure, une réputation solide basée sur la qualité réelle.""",
        'weekly_advice': {
            'week_1': "Définis l'image que tu veux projeter sur le long terme.",
            'week_2': "Investis dans ta présence : style, santé, confiance.",
            'week_3': "Avance à ton rythme, sans te comparer aux autres.",
            'week_4': "Savoure la solidité de ton rayonnement naissant."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Star polyvalente**

Ta Lune en Lion en Maison 1 cherche l'admiration et la reconnaissance. Ton Ascendant Gémeaux ajoute légèreté et versatilité : tu veux briller dans plusieurs domaines à la fois, être admiré·e pour ton intelligence et ton charme.

**Domaine activé** : Maison 1 — Ton identité veut se montrer sous toutes ses facettes. Tu cherches à être reconnu·e pour ta créativité ET ton intellect, ton charme ET ton esprit. Le multi-talent est ton terrain de jeu.

**Ton approche instinctive** : Le Gémeaux te rend communicatif·ve et adaptable. Tu sais comment captiver ton audience avec des mots, des histoires, de l'humour. Cette agilité mentale soutient ton besoin de briller.

**Tensions possibles** : Disperser ton énergie créative dans trop de directions. Le risque de devenir superficiel·le ou de jouer un rôle sans profondeur réelle. L'inconstance peut nuire à ton rayonnement.

**Conseil clé** : Utiliser ta polyvalence pour enrichir ton expression, pas pour te disperser.""",
        'weekly_advice': {
            'week_1': "Explore plusieurs facettes de ta créativité sans t'engager encore.",
            'week_2': "Communique qui tu es avec clarté et charme.",
            'week_3': "Choisis 2-3 talents principaux à développer ce mois-ci.",
            'week_4': "Partage ton histoire de manière captivante."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Chaleur rayonnante**

Ta Lune en Lion en Maison 1 veut être vue et admirée. Ton Ascendant Cancer ajoute une dimension émotionnelle profonde : tu veux briller, mais de manière chaleureuse, protectrice, nourricière. Le roi généreux.

**Domaine activé** : Maison 1 — Ton identité cherche à rayonner à travers la gentillesse et la générosité. Tu veux être reconnu·e non seulement pour ta force, mais pour ton cœur, ta capacité à prendre soin des autres avec panache.

**Ton approche instinctive** : Le Cancer te rend sensible aux besoins émotionnels de ton entourage. Tu veux créer un impact qui réchauffe les cœurs, pas seulement éblouir. Cette sensibilité adoucit la fierté du Lion.

**Tensions possibles** : L'oscillation entre besoin d'admiration et besoin de connexion intime. Tu peux te sentir vulnérable si on ne reconnaît pas ta générosité. Les sautes d'humeur peuvent affecter ton rayonnement.

**Conseil clé** : Rayonner à travers l'authenticité émotionnelle et la générosité du cœur.""",
        'weekly_advice': {
            'week_1': "Montre-toi tel·le que tu es, avec tes émotions sincères.",
            'week_2': "Crée quelque chose qui nourrit émotionnellement les autres.",
            'week_3': "Accepte ta vulnérabilité comme force, pas faiblesse.",
            'week_4': "Célèbre l'impact émotionnel que tu as eu ce mois-ci."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Soleil royal**

Triple Lion : Lune en Lion, Maison 1, Ascendant Lion. L'énergie est pure royauté, créativité maximale, besoin absolu d'être vu·e et célébré·e. Ce mois-ci, tu es la star de ta propre vie, sans compromis ni fausse modestie.

**Domaine activé** : Maison 1 — Ton identité EST l'expression créative incarnée. Tu veux rayonner sans limites, être admiré·e pour ta grandeur naturelle, ta générosité, ton cœur immense. Tout est théâtre et tu en es le personnage principal.

**Ton approche instinctive** : Triple feu fixe : tu ne fais rien à moitié. Quand tu brilles, c'est avec tout ton être. Cette intensité créative peut être magnifique ou écrasante selon comment tu la canalises.

**Tensions possibles** : L'ego démesuré peut te couper des autres. Le besoin constant d'admiration peut devenir épuisant. La fierté blessée si on ne te reconnaît pas à ta juste valeur. Le drame émotionnel peut exploser.

**Conseil clé** : Assumer pleinement ta grandeur tout en restant généreux·se et inclusif·ve.""",
        'weekly_advice': {
            'week_1': "Lance un projet créatif qui te représente pleinement.",
            'week_2': "Brille sans retenue, mais avec authenticité.",
            'week_3': "Partage ta lumière pour inspirer, pas pour dominer.",
            'week_4': "Célèbre ton rayonnement et prépare ton prochain chef-d'œuvre."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Excellence modeste**

Ta Lune en Lion en Maison 1 veut briller et être admirée. Ton Ascendant Vierge tempère cette grandeur par la modestie et le perfectionnisme : tu veux rayonner, mais de manière impeccable, utile, perfectionnée.

**Domaine activé** : Maison 1 — Ton identité cherche l'excellence. Tu veux être reconnu·e non seulement pour ton éclat, mais pour ta compétence, ta précision, ton utilité réelle. Le talent doit servir à quelque chose de concret.

**Ton approche instinctive** : La Vierge te pousse à perfectionner ton expression créative. Tu n'es jamais satisfait·e, tu veux toujours améliorer. Cette exigence peut sublimer ou bloquer ton rayonnement naturel.

**Tensions possibles** : L'autocritique excessive peut saboter ton besoin de briller. Tu risques de te dévaloriser ou de ne jamais te sentir assez bon·ne pour te montrer. Le perfectionnisme paralyse la spontanéité.

**Conseil clé** : Accepter que l'imperfection fait partie de l'authenticité créative.""",
        'weekly_advice': {
            'week_1': "Identifie un talent que tu veux perfectionner ce mois-ci.",
            'week_2': "Montre-toi même si tu ne te sens pas parfait·e.",
            'week_3': "Utilise ton exigence pour t'améliorer, pas pour te critiquer.",
            'week_4': "Célèbre tes progrès concrets et mesurables."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Grâce rayonnante**

Ta Lune en Lion en Maison 1 cherche l'admiration et la reconnaissance. Ton Ascendant Balance ajoute charme et diplomatie : tu veux briller, mais avec élégance, harmonie, en créant de la beauté qui plaît à tous.

**Domaine activé** : Maison 1 — Ton identité s'exprime à travers l'esthétique et les relations. Tu veux être admiré·e pour ton style, ton charme, ta capacité à créer de l'harmonie. L'apparence et la grâce comptent énormément.

**Ton approche instinctive** : La Balance te fait chercher l'approbation et l'équilibre. Tu veux briller sans choquer, plaire sans perdre ton authenticité. Cette dualité peut créer une présence magnétique ou indécise.

**Tensions possibles** : Le besoin de plaire peut diluer ton expression créative unique. Tu risques de trop adapter ton rayonnement aux attentes des autres. L'indécision sur comment te montrer vraiment.

**Conseil clé** : Briller avec grâce tout en restant fidèle à ta vérité créative.""",
        'weekly_advice': {
            'week_1': "Définis ton style personnel qui allie beauté et authenticité.",
            'week_2': "Crée quelque chose d'esthétiquement beau et significatif.",
            'week_3': "Cherche le feedback, mais ne t'y soumets pas aveuglément.",
            'week_4': "Célèbre comment tu as harmonisé expression et connexion."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Puissance magnétique**

Ta Lune en Lion en Maison 1 veut rayonner et être admirée. Ton Ascendant Scorpion ajoute intensité et profondeur : tu ne veux pas seulement briller, tu veux transformer, fasciner, avoir un impact puissant et durable.

**Domaine activé** : Maison 1 — Ton identité s'exprime avec une intensité dramatique. Tu veux être reconnu·e pour ta force intérieure, ton mystère, ton pouvoir de transformation. Pas de superficialité : tout ou rien.

**Ton approche instinctive** : Le Scorpion te pousse à creuser profond dans ton expression créative. Tu veux toucher les âmes, pas juste attirer les regards. Cette profondeur donne du poids à ton rayonnement solaire.

**Tensions possibles** : L'intensité émotionnelle peut devenir écrasante. Le besoin de contrôle peut rigidifier ton expression. La jalousie ou le ressentiment si on ne te reconnaît pas peuvent te consumer.

**Conseil clé** : Transformer ta puissance créative en force qui guérit et inspire.""",
        'weekly_advice': {
            'week_1': "Plonge dans les profondeurs de ton identité créative.",
            'week_2': "Exprime quelque chose de vulnérable et puissant.",
            'week_3': "Utilise ton magnétisme pour créer du lien, pas pour dominer.",
            'week_4': "Observe comment tu as transformé ta présence ce mois-ci."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Joie expansive**

Double feu entre ta Lune en Lion en Maison 1 et ton Ascendant Sagittaire : l'énergie est optimiste, généreuse, aventureuse. Tu veux rayonner en grand, inspirer, partager ta vision avec enthousiasme et foi en la vie.

**Domaine activé** : Maison 1 — Ton identité s'exprime avec exubérance et spontanéité. Tu veux être reconnu·e pour ta joie de vivre, ton optimisme contagieux, ta capacité à voir grand. L'aventure créative t'appelle.

**Ton approche instinctive** : Le Sagittaire te fait voir les possibilités infinies. Tu crois en ton potentiel de grandeur et tu n'as pas peur de viser haut. Cette confiance naturelle amplifie ton rayonnement solaire.

**Tensions possibles** : L'excès de confiance peut te rendre arrogant·e ou insouciant·e. Le manque de discernement sur où briller vraiment. Tu risques de promettre plus que tu ne peux tenir.

**Conseil clé** : Canaliser ton enthousiasme vers une vision créative inspirante mais réalisable.""",
        'weekly_advice': {
            'week_1': "Définis une vision créative qui t'enthousiasme vraiment.",
            'week_2': "Lance-toi avec confiance et générosité.",
            'week_3': "Partage ton inspiration pour élever les autres.",
            'week_4': "Célèbre tes audaces et prépare ta prochaine aventure."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Autorité rayonnante**

Ta Lune en Lion en Maison 1 veut briller et être admirée. Ton Ascendant Capricorne ajoute structure et ambition : tu veux non seulement rayonner, mais construire une réputation solide, être respecté·e autant qu'admiré·e.

**Domaine activé** : Maison 1 — Ton identité cherche la reconnaissance professionnelle et sociale. Tu veux être vu·e comme quelqu'un de compétent, d'ambitieux·se, de fiable, tout en gardant ton éclat créatif naturel.

**Ton approche instinctive** : Le Capricorne te fait planifier ton rayonnement sur le long terme. Tu construis ta présence pierre par pierre, avec discipline. Cette patience stratégique canalise bien l'énergie solaire du Lion.

**Tensions possibles** : La tension entre spontanéité créative (Lion) et contrôle rigide (Capricorne). Tu peux te sentir coincé·e entre authenticité et image professionnelle. La peur de l'échec peut bloquer ton expression.

**Conseil clé** : Bâtir une présence authentique ET respectée, sans sacrifier ta créativité.""",
        'weekly_advice': {
            'week_1': "Définis l'image professionnelle que tu veux projeter.",
            'week_2': "Prends une initiative visible qui montre ton sérieux.",
            'week_3': "Équilibre ambition et authenticité créative.",
            'week_4': "Mesure tes progrès vers une réputation solide."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Éclat unique**

Ta Lune en Lion en Maison 1 veut être admirée. Ton Ascendant Verseau (opposé au Lion) crée une tension créative : tu veux briller, mais de manière originale, unique, en dehors des conventions. L'individualité radicale.

**Domaine activé** : Maison 1 — Ton identité cherche à exprimer son unicité. Tu veux être reconnu·e pour ce qui te différencie, pas pour ta conformité. L'innovation créative et la rébellion élégante sont tes terrains.

**Ton approche instinctive** : Le Verseau te pousse à défier les attentes. Tu ne veux pas briller comme les autres brillent : tu veux créer ton propre langage, ton propre style. Cette originalité peut fasciner ou aliéner.

**Tensions possibles** : Le conflit entre besoin d'admiration (Lion) et détachement émotionnel (Verseau). Tu risques de paraître distant·e ou excentrique. La rébellion pour la rébellion peut saboter ton rayonnement.

**Conseil clé** : Assumer ton originalité tout en restant connecté·e aux autres humains.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te rend vraiment unique et assumable.",
            'week_2': "Exprime-toi de manière non-conventionnelle avec confiance.",
            'week_3': "Connecte ton originalité à une cause collective.",
            'week_4': "Célèbre comment tu as brisé des codes ce mois-ci."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Artiste inspiré·e**

Ta Lune en Lion en Maison 1 cherche l'admiration et la reconnaissance. Ton Ascendant Poissons ajoute sensibilité et imagination : tu veux briller à travers l'art, la spiritualité, l'expression de l'invisible. Le mystique créatif.

**Domaine activé** : Maison 1 — Ton identité s'exprime à travers l'imagination et l'intuition. Tu veux être reconnu·e pour ta sensibilité artistique, ta capacité à canaliser l'inspiration divine, ta compassion créative.

**Ton approche instinctive** : Le Poissons te fait créer depuis un espace de flow et d'inspiration. Tu ne forces pas ton rayonnement, tu le laisses émerger naturellement. Cette fluidité peut sublimer ou diluer ton expression solaire.

**Tensions possibles** : Le manque de limites claires peut affaiblir ton rayonnement. Tu risques de te perdre dans le rêve ou de fuir la responsabilité de briller. La victimisation si on ne te reconnaît pas.

**Conseil clé** : Ancrer ton inspiration créative dans une forme tangible et partageable.""",
        'weekly_advice': {
            'week_1': "Crée un espace pour canaliser ton inspiration artistique.",
            'week_2': "Exprime quelque chose de poétique ou spirituel.",
            'week_3': "Donne forme concrète à ton imagination.",
            'week_4': "Partage ton art avec douceur et confiance."
        }
    },

    # ==================== MAISON 2 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Richesse conquise**

Ta Lune en Lion active la Maison 2 : tes ressources, ta valeur, ta sécurité matérielle deviennent un terrain de créativité et de fierté. Avec l'Ascendant Bélier, tu veux conquérir l'abondance avec audace et panache.

**Domaine activé** : Maison 2 — Tes finances et possessions sont une question d'honneur. Tu veux gagner généreusement, avoir des ressources qui reflètent ta grandeur, vivre dans l'abondance. L'argent est un outil de rayonnement.

**Ton approche instinctive** : Double feu sur les ressources : tu fonces pour obtenir ce que tu veux. Les opportunités financières excitent ton ego. Tu es prêt·e à prendre des risques pour vivre royalement.

**Tensions possibles** : Les dépenses ostentatoires pour impressionner. L'impulsivité peut te faire investir sans réfléchir. Le besoin de montrer ta réussite peut créer de l'instabilité financière.

**Conseil clé** : Canaliser ton audace financière vers la création de valeur réelle et durable.""",
        'weekly_advice': {
            'week_1': "Identifie une opportunité financière audacieuse mais sensée.",
            'week_2': "Investis dans quelque chose qui élève ton statut.",
            'week_3': "Génère des revenus de manière créative et courageuse.",
            'week_4': "Évalue si ta générosité financière était stratégique."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Luxe stable**

Ta Lune en Lion en Maison 2 veut l'abondance et le luxe. Ton Ascendant Taureau, maître naturel de cette maison, apporte sagesse et patience : tu veux non seulement briller financièrement, mais construire une richesse solide.

**Domaine activé** : Maison 2 — Tes finances et possessions sont un terrain d'expression de ta valeur. Tu cherches le confort luxueux mais durable. La qualité prime sur la quantité, mais tu veux quand même impressionner.

**Ton approche instinctive** : Le Taureau te pousse à accumuler lentement mais sûrement. Tu veux des biens de valeur qui durent, un patrimoine solide. Cette approche tempère les dépenses impulsives du Lion.

**Tensions possibles** : La tension entre générosité ostentatoire (Lion) et accumulation prudente (Taureau). Tu risques d'alterner entre dépenses luxueuses et avarice. L'attachement excessif aux possessions.

**Conseil clé** : Investir dans le beau et le durable, pas juste dans l'impressionnant.""",
        'weekly_advice': {
            'week_1': "Définis un objectif financier ambitieux mais réaliste.",
            'week_2': "Investis dans quelque chose de luxueux et durable.",
            'week_3': "Construis ta sécurité sans sacrifier ton plaisir.",
            'week_4': "Savoure l'abondance que tu as créée ce mois-ci."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Profits versatiles**

Ta Lune en Lion en Maison 2 veut gagner généreusement. Ton Ascendant Gémeaux ajoute agilité et diversité : tu veux multiplier tes sources de revenus, gagner par ta créativité ET ton intelligence.

**Domaine activé** : Maison 2 — Tes finances sont un terrain de jeu intellectuel et créatif. Tu peux exceller dans la vente, la communication rémunérée, les projets multiples. L'argent vient par les mots et les idées.

**Ton approche instinctive** : Le Gémeaux te fait jongler avec plusieurs opportunités. Tu es doué·e pour négocier, communiquer ta valeur, créer des réseaux rentables. Cette versatilité peut multiplier tes gains ou te disperser.

**Tensions possibles** : Trop de projets simultanés diluent ton impact financier. Le risque de papillonner sans jamais vraiment capitaliser. Les promesses financières non tenues par manque de suivi.

**Conseil clé** : Utiliser ta polyvalence pour diversifier intelligemment, pas pour te disperser.""",
        'weekly_advice': {
            'week_1': "Explore 2-3 sources de revenus complémentaires.",
            'week_2': "Communique ta valeur avec clarté et charme.",
            'week_3': "Choisis les opportunités les plus lucratives à développer.",
            'week_4': "Fais le point sur tes revenus multiples."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Richesse nourricière**

Ta Lune en Lion en Maison 2 veut l'abondance et la reconnaissance matérielle. Ton Ascendant Cancer ajoute le besoin de sécurité émotionnelle : l'argent doit aussi nourrir le cœur, pas seulement l'ego.

**Domaine activé** : Maison 2 — Tes finances sont liées à ton bien-être émotionnel. Tu veux gagner pour protéger ceux que tu aimes, créer un foyer confortable, te sentir en sécurité. La générosité familiale est importante.

**Ton approche instinctive** : Le Cancer te fait épargner pour les jours difficiles tout en voulant offrir généreusement. Tu es sensible aux fluctuations financières qui affectent ta stabilité émotionnelle.

**Tensions possibles** : L'anxiété financière peut contredire ton besoin de vivre largement. Les dépenses émotionnelles (confort, cadeaux) peuvent déstabiliser ton budget. L'attachement sentimental aux possessions.

**Conseil clé** : Équilibrer générosité du cœur et sécurité financière à long terme.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te sécurise vraiment financièrement.",
            'week_2': "Épargne pour ton confort futur et celui de tes proches.",
            'week_3': "Offre généreusement sans te mettre en danger.",
            'week_4': "Célèbre l'abondance partagée que tu as créée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Or pur**

Double Lion sur la Maison 2 : l'énergie est royale, généreuse, tournée vers l'abondance ostentatoire. Tu veux non seulement avoir de l'argent, mais vivre comme un·e roi·reine, dans le luxe et la générosité.

**Domaine activé** : Maison 2 — Tes finances et possessions sont une extension de ta grandeur. Tu veux le meilleur, le plus beau, le plus impressionnant. L'argent est fait pour être dépensé avec panache et partagé généreusement.

**Ton approche instinctive** : Tu ne fais rien à moitié financièrement. Soit tu gagnes gros, soit tu galères, mais tu refuses la médiocrité. Ta confiance naturelle attire l'abondance, mais aussi les excès.

**Tensions possibles** : Les dépenses excessives pour maintenir une image de grandeur. La fierté peut t'empêcher de demander de l'aide en cas de difficulté. Le manque de gestion pratique.

**Conseil clé** : Assumer ton droit à l'abondance tout en gérant avec un minimum de sagesse.""",
        'weekly_advice': {
            'week_1': "Définis l'abondance selon tes propres termes royaux.",
            'week_2': "Génère des revenus de manière créative et généreuse.",
            'week_3': "Dépense avec panache mais pas au-delà de tes moyens.",
            'week_4': "Célèbre ta richesse et partage ta générosité."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Valeur perfectionnée**

Ta Lune en Lion en Maison 2 veut l'abondance et le luxe. Ton Ascendant Vierge tempère par le pragmatisme : tu veux gagner bien, mais de manière impeccable, organisée, utile. La richesse doit avoir du sens.

**Domaine activé** : Maison 2 — Tes finances sont un terrain de perfectionnement. Tu veux optimiser chaque euro, créer de la valeur par ton travail de qualité, être reconnu·e pour ton expertise rémunérée.

**Ton approche instinctive** : La Vierge te fait analyser chaque opportunité financière. Tu veux maximiser tes gains par l'efficacité et la compétence. Cette rigueur canalise bien l'énergie généreuse du Lion.

**Tensions possibles** : L'autocritique sur ta valeur financière. Tu risques de sous-estimer tes prix ou de te surinvestir sans demander ton dû. Le perfectionnisme peut bloquer les opportunités.

**Conseil clé** : Reconnaître ta vraie valeur et la facturer sans fausse modestie.""",
        'weekly_advice': {
            'week_1': "Évalue objectivement ta valeur marchande réelle.",
            'week_2': "Optimise tes processus de génération de revenus.",
            'week_3': "Demande ce que tu vaux sans te dévaloriser.",
            'week_4': "Mesure tes progrès financiers concrets."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Richesse élégante**

Ta Lune en Lion en Maison 2 cherche l'abondance et le luxe. Ton Ascendant Balance ajoute le goût, l'harmonie, les partenariats : tu veux gagner avec grâce, dans de beaux environnements, souvent avec les autres.

**Domaine activé** : Maison 2 — Tes finances sont liées à l'esthétique et aux relations. Tu peux gagner par ton charme, ton sens artistique, ta capacité à créer des partenariats gagnant-gagnant. Le beau paie.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre financier et la justice dans les échanges. Tu veux que tout le monde s'y retrouve, mais tu veux aussi ta part de luxe et de reconnaissance.

**Tensions possibles** : L'indécision sur les opportunités financières. Le besoin de plaire peut te faire sous-évaluer tes services. Les dépenses pour maintenir les apparences et l'harmonie sociale.

**Conseil clé** : Créer de la valeur esthétique tout en négociant fermement ton dû.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton sens esthétique peut générer des revenus.",
            'week_2': "Négocie des partenariats financiers équilibrés.",
            'week_3': "Investis dans la beauté qui prend de la valeur.",
            'week_4': "Célèbre l'harmonie financière que tu as créée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir matériel**

Ta Lune en Lion en Maison 2 veut l'abondance ostentatoire. Ton Ascendant Scorpion ajoute intensité et contrôle : l'argent c'est le pouvoir, et tu veux dominer ta situation financière complètement.

**Domaine activé** : Maison 2 — Tes finances sont un terrain de transformation profonde. Tu peux vouloir tout changer dans ta relation à l'argent, éliminer les dettes, reconstruire une richesse sur des bases solides.

**Ton approche instinctive** : Le Scorpion te fait creuser les mécanismes cachés de l'argent. Tu veux comprendre comment fonctionne vraiment la richesse et l'utiliser pour gagner du pouvoir personnel.

**Tensions possibles** : L'obsession du contrôle financier peut créer de l'anxiété. La peur de manquer vs le besoin de vivre luxueusement. Les secrets financiers ou les manipulations pour gagner.

**Conseil clé** : Transformer ta relation à l'argent en profondeur, pas juste accumuler.""",
        'weekly_advice': {
            'week_1': "Regarde en face ta situation financière sans illusion.",
            'week_2': "Élimine une source de dépendance ou de dette.",
            'week_3': "Investis dans ce qui te donne du pouvoir à long terme.",
            'week_4': "Observe comment tu as repris le contrôle financier."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Abondance joyeuse**

Double feu sur la Maison 2 : ta Lune en Lion et ton Ascendant Sagittaire créent une énergie d'abondance naturelle, de foi en la richesse, de générosité sans limites. Tu crois que l'univers pourvoit.

**Domaine activé** : Maison 2 — Tes finances sont un terrain d'expansion et d'aventure. Tu veux gagner pour explorer, voyager, vivre pleinement. L'argent est fait pour créer des expériences riches.

**Ton approche instinctive** : Le Sagittaire te fait voir les opportunités financières partout. Tu as foi en ton potentiel d'abondance. Cette confiance peut attirer la chance mais aussi l'insouciance.

**Tensions possibles** : L'excès d'optimisme financier peut te faire dépenser avant de gagner. Le manque de gestion pratique. Les paris risqués basés sur la foi plutôt que les chiffres.

**Conseil clé** : Garder ta foi en l'abondance tout en gérant concrètement tes ressources.""",
        'weekly_advice': {
            'week_1': "Définis une vision d'abondance inspirante mais chiffrée.",
            'week_2': "Prends un risque calculé pour multiplier tes gains.",
            'week_3': "Reste ouvert·e aux opportunités inattendues.",
            'week_4': "Évalue si ton optimisme a porté ses fruits."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fortune bâtie**

Ta Lune en Lion en Maison 2 veut l'abondance et le luxe. Ton Ascendant Capricorne apporte discipline et ambition à long terme : tu veux construire un empire financier solide, pas juste briller aujourd'hui.

**Domaine activé** : Maison 2 — Tes finances sont un projet d'ambition sérieuse. Tu veux que chaque action d'aujourd'hui contribue à ta richesse future. La discipline rencontre la générosité.

**Ton approche instinctive** : Le Capricorne te fait planifier ta richesse sur des décennies. Tu es prêt·e à travailler dur maintenant pour vivre royalement plus tard. Cette patience canalise bien l'impulsivité du Lion.

**Tensions possibles** : La frustration si les résultats ne viennent pas assez vite. Le conflit entre envie de dépenser luxueusement (Lion) et besoin d'épargner (Capricorne). Le travail acharné sans joie.

**Conseil clé** : Bâtir une fortune qui dure tout en t'autorisant des plaisirs mesurés.""",
        'weekly_advice': {
            'week_1': "Définis un plan financier ambitieux sur plusieurs années.",
            'week_2': "Prends une action concrète qui sert ce plan.",
            'week_3': "Persévère même si la croissance semble lente.",
            'week_4': "Mesure tes progrès objectivement et célèbre-les."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Richesse innovante**

Ta Lune en Lion en Maison 2 veut l'abondance et la reconnaissance matérielle. Ton Ascendant Verseau (opposé au Lion) crée une tension : tu veux gagner différemment, par l'innovation, pas par les voies conventionnelles.

**Domaine activé** : Maison 2 — Tes finances cherchent une expression unique. Tu peux être attiré·e par les cryptos, les nouvelles technologies, les business models disruptifs. L'argent doit servir ta liberté.

**Ton approche instinctive** : Le Verseau te fait penser différemment sur la richesse. Tu n'as pas peur de tester de nouvelles approches financières. Cette originalité peut créer des opportunités ou des pertes.

**Tensions possibles** : Le conflit entre besoin de luxe personnel (Lion) et idéaux collectifs (Verseau). Rejeter des opportunités qui marchent juste parce qu'elles sont classiques.

**Conseil clé** : Innover financièrement où ça a du sens, rester pragmatique ailleurs.""",
        'weekly_advice': {
            'week_1': "Explore une source de revenus non-conventionnelle.",
            'week_2': "Teste une approche originale de génération de valeur.",
            'week_3': "Équilibre innovation et bon sens financier.",
            'week_4': "Évalue si ton approche unique a payé."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Richesse fluide**

Ta Lune en Lion en Maison 2 veut l'abondance matérielle. Ton Ascendant Poissons ajoute fluidité et foi : tu crois que l'argent vient quand tu es aligné·e, que l'univers pourvoit. La richesse spirituelle compte aussi.

**Domaine activé** : Maison 2 — Tes finances sont influencées par ton intuition et ton état émotionnel. Tu peux attirer l'abondance de manière presque magique quand tu lâches prise, ou galèrer quand tu forces.

**Ton approche instinctive** : Le Poissons te fait faire confiance au flow. Tu peux gagner par ton art, ta sensibilité, ton aide aux autres. Cette approche manque parfois de pragmatisme mais peut être miraculeuse.

**Tensions possibles** : Le manque de limites financières claires. L'oscillation entre foi aveugle et anxiété matérielle. Les dépenses émotionnelles ou pour échapper à la réalité.

**Conseil clé** : Faire confiance à ton intuition financière tout en gardant les pieds sur terre.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition sur les opportunités financières.",
            'week_2': "Crée de la valeur par ton art ou ta sensibilité.",
            'week_3': "Ancre ton flow dans des structures concrètes.",
            'week_4': "Célèbre l'abondance venue naturellement."
        }
    },

    # ==================== MAISON 3 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Parole de feu**

Ta Lune en Lion active la Maison 3 : communication, apprentissage, entourage proche. Avec l'Ascendant Bélier, tu veux t'exprimer avec audace, dire ce que tu penses sans filtre, captiver par tes mots.

**Domaine activé** : Maison 3 — Tes échanges quotidiens deviennent une scène. Tu veux que ta voix soit entendue, que tes idées brillent, que tes conversations aient de l'impact. L'expression verbale est instinctive.

**Ton approche instinctive** : Double feu sur la communication : tu es direct·e, passionné·e, parfois impulsif·ve dans tes paroles. Tu n'as pas peur du conflit verbal si c'est pour défendre ta vérité.

**Tensions possibles** : L'impulsivité verbale peut blesser. Le besoin de dominer les conversations. L'impatience face aux échanges lents ou nuancés. Les conflits avec les proches par manque de tact.

**Conseil clé** : Canaliser ta passion verbale vers l'inspiration, pas la domination.""",
        'weekly_advice': {
            'week_1': "Exprime une idée importante avec confiance et clarté.",
            'week_2': "Lance une conversation courageuse avec un proche.",
            'week_3': "Écoute autant que tu parles, même si c'est difficile.",
            'week_4': "Célèbre les connexions créées par tes mots."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Voix stable**

Ta Lune en Lion en Maison 3 veut s'exprimer avec panache. Ton Ascendant Taureau tempère : tu veux communiquer avec autorité, mais de manière posée, réfléchie, avec une voix qui porte et qui dure.

**Domaine activé** : Maison 3 — Tes mots cherchent à créer de la valeur. Tu veux que ce que tu dis ait du poids, de la substance, qu'on s'en souvienne. L'éloquence calme et puissante est ton mode.

**Ton approche instinctive** : Le Taureau te fait peser tes mots avant de parler. Tu veux que chaque phrase compte. Cette réflexion peut frustrer ton besoin d'expression immédiate du Lion.

**Tensions possibles** : L'impatience de briller verbalement contre le besoin de réfléchir d'abord. Tu peux te sentir bloqué·e entre spontanéité et prudence. L'entêtement dans tes opinions.

**Conseil clé** : Parler avec confiance ET substance, pas juste pour briller.""",
        'weekly_advice': {
            'week_1': "Prépare ce que tu veux communiquer d'important.",
            'week_2': "Exprime-toi avec autorité calme et assurance.",
            'week_3': "Reste ouvert·e aux autres points de vue sans céder le tien.",
            'week_4': "Observe l'impact durable de tes paroles."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Conteur brillant**

Ta Lune en Lion en Maison 3 cherche l'admiration par les mots. Ton Ascendant Gémeaux, maître naturel de cette maison, amplifie : tu es un·e communicateur·rice né·e, charismatique, captivant·e, polyvalent·e.

**Domaine activé** : Maison 3 — La communication est ton terrain de jeu créatif. Tu excelles à raconter des histoires, à captiver une audience, à jongler avec les idées. Ton intellect brille naturellement.

**Ton approche instinctive** : Le Gémeaux te rend curieux·se et adaptable. Tu peux parler de mille sujets avec aisance. Cette versatilité soutient ton besoin de briller intellectuellement.

**Tensions possibles** : La dispersion mentale peut diluer ton impact. Le risque de parler pour briller sans profondeur réelle. L'inconstance dans tes échanges ou apprentissages.

**Conseil clé** : Utiliser ta brillance verbale pour inspirer et connecter, pas juste impressionner.""",
        'weekly_advice': {
            'week_1': "Explore plusieurs sujets qui t'enthousiasment vraiment.",
            'week_2': "Raconte une histoire qui captive et inspire.",
            'week_3': "Approfondis 1-2 domaines au lieu de tout survoler.",
            'week_4': "Partage ce que tu as appris avec générosité."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Parole chaleureuse**

Ta Lune en Lion en Maison 3 veut s'exprimer avec créativité. Ton Ascendant Cancer ajoute sensibilité émotionnelle : tu veux communiquer depuis le cœur, toucher les émotions, créer de l'intimité par les mots.

**Domaine activé** : Maison 3 — Tes échanges cherchent à nourrir émotionnellement. Tu veux que tes mots réchauffent, protègent, inspirent. Les conversations avec la famille et les proches sont importantes.

**Ton approche instinctive** : Le Cancer te rend empathique dans ta communication. Tu ressens ce que les autres ont besoin d'entendre. Cette sensibilité adoucit le besoin de briller du Lion.

**Tensions possibles** : Les sautes d'humeur affectent ta communication. Tu peux être théâtral·e dans l'expression de tes émotions. La susceptibilité si on ne valorise pas tes paroles.

**Conseil clé** : Communiquer avec authenticité émotionnelle tout en gardant de la force.""",
        'weekly_advice': {
            'week_1': "Partage quelque chose de vulnérable et sincère.",
            'week_2': "Écoute avec ton cœur, pas juste tes oreilles.",
            'week_3': "Utilise tes mots pour réconforter et inspirer.",
            'week_4': "Célèbre les liens créés par tes échanges."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Orateur royal**

Double Lion sur la Maison 3 : l'énergie de communication est dramatique, charismatique, centrée sur l'expression créative. Tu veux captiver, inspirer, briller par tes mots et tes idées.

**Domaine activé** : Maison 3 — Toute forme de communication devient une performance. Tu excelles naturellement à raconter des histoires, à enseigner avec passion, à captiver une audience. Ta voix porte.

**Ton approche instinctive** : Tu ne fais rien à moitié dans tes échanges. Soit tu es passionné·e et inspirant·e, soit tu te tais. Tes conversations sont rarement neutres : toujours un peu théâtrales.

**Tensions possibles** : Dominer les conversations sans laisser d'espace aux autres. Le besoin constant d'être écouté·e et admiré·e peut fatiguer. La fierté blessée si on ne valorise pas tes paroles.

**Conseil clé** : Utiliser ton charisme verbal pour élever les autres, pas juste te mettre en avant.""",
        'weekly_advice': {
            'week_1': "Lance une conversation importante avec confiance.",
            'week_2': "Partage tes idées créatives avec générosité.",
            'week_3': "Écoute vraiment les autres, pas juste attendre ton tour.",
            'week_4': "Célèbre comment tes mots ont inspiré ce mois-ci."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision brillante**

Ta Lune en Lion en Maison 3 veut s'exprimer avec créativité. Ton Ascendant Vierge tempère par l'analyse : tu veux communiquer avec précision, utilité, perfection. Le brillant rencontre le précis.

**Domaine activé** : Maison 3 — Tes mots cherchent l'excellence. Tu veux être reconnu·e pour ton intelligence pratique, ta capacité à expliquer clairement, ton utilité. L'apprentissage est perfectionniste.

**Ton approche instinctive** : La Vierge te fait analyser chaque mot avant de le dire. Tu veux être impeccable dans ta communication. Cette exigence peut affiner ou bloquer ton expression naturelle.

**Tensions possibles** : L'autocritique sur ta manière de communiquer. Tu risques de te censurer ou de ne jamais te sentir assez éloquent·e. Le perfectionnisme peut paralyser ton expression créative.

**Conseil clé** : Accepter que l'imperfection dans l'expression fait partie de l'authenticité.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine de connaissance à perfectionner.",
            'week_2': "Partage tes idées même si tu ne te sens pas parfait·e.",
            'week_3': "Utilise ta précision pour clarifier, pas pour critiquer.",
            'week_4': "Célèbre tes progrès en communication."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Charme éloquent**

Ta Lune en Lion en Maison 3 cherche l'admiration par les mots. Ton Ascendant Balance ajoute grâce et diplomatie : tu veux communiquer avec charme, créer de l'harmonie, plaire tout en brillant.

**Domaine activé** : Maison 3 — Tes échanges cherchent l'équilibre et la beauté. Tu excelles dans la diplomatie, la négociation, les conversations élégantes. Tes mots créent des ponts et séduisent.

**Ton approche instinctive** : La Balance te fait chercher l'approbation dans tes échanges. Tu veux que tout le monde apprécie ta manière de communiquer. Cette recherche d'harmonie peut diluer ton message.

**Tensions possibles** : L'indécision sur ce que tu veux vraiment dire. Le besoin de plaire peut te faire adapter ton discours jusqu'à perdre ton authenticité. Éviter les sujets qui fâchent.

**Conseil clé** : Communiquer avec grâce tout en restant fidèle à ta vérité.""",
        'weekly_advice': {
            'week_1': "Définis ce que tu veux vraiment communiquer ce mois-ci.",
            'week_2': "Exprime-toi avec charme mais sans compromis sur l'essentiel.",
            'week_3': "Crée des connexions harmonieuses par tes mots.",
            'week_4': "Célèbre les ponts que tu as construits."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Parole intense**

Ta Lune en Lion en Maison 3 veut s'exprimer avec créativité. Ton Ascendant Scorpion ajoute profondeur et intensité : tu veux que tes mots transforment, touchent l'âme, révèlent des vérités cachées.

**Domaine activé** : Maison 3 — Tes échanges ne sont jamais superficiels. Tu creuses en profondeur, tu poses les questions qui dérangent, tu communiques pour transformer. Les secrets te fascinent.

**Ton approche instinctive** : Le Scorpion te pousse à aller au cœur des choses dans tes conversations. Tu veux comprendre les motivations cachées, dire les vérités difficiles. Cette intensité peut intimider.

**Tensions possibles** : Les propos trop intenses peuvent effrayer. Le besoin de contrôler les conversations. La tendance à manipuler par les mots ou à être cassant·e si tu te sens menacé·e.

**Conseil clé** : Utiliser ta puissance verbale pour guérir et révéler, pas pour dominer.""",
        'weekly_advice': {
            'week_1': "Plonge dans une conversation profonde et transformante.",
            'week_2': "Dis une vérité difficile mais nécessaire avec tact.",
            'week_3': "Écoute ce qui est dit entre les lignes.",
            'week_4': "Observe comment tes mots ont transformé les autres."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vision inspirante**

Double feu sur la Maison 3 : ta Lune en Lion et ton Ascendant Sagittaire créent une communication enthousiaste, optimiste, visionnaire. Tu veux inspirer par tes mots, partager ta foi en la vie.

**Domaine activé** : Maison 3 — Tes échanges cherchent à élever. Tu veux transmettre de l'espoir, de la sagesse, des visions d'avenir. L'enseignement, la philosophie, les grandes idées t'attirent.

**Ton approche instinctive** : Le Sagittaire te fait communiquer avec franchise et générosité. Tu dis ce que tu penses sans filtre, avec foi en ton message. Cette spontanéité peut inspirer ou choquer.

**Tensions possibles** : L'excès de confiance dans tes opinions. Le manque de tact ou de nuance. Tu risques de prêcher sans vraiment écouter. L'exagération pour rendre tes histoires plus impressionnantes.

**Conseil clé** : Inspirer par ta vision tout en restant humble et à l'écoute.""",
        'weekly_advice': {
            'week_1': "Partage une vision optimiste qui t'enthousiasme.",
            'week_2': "Apprends quelque chose de nouveau qui élargit ta perspective.",
            'week_3': "Enseigne ou inspire sans imposer ta vérité.",
            'week_4': "Célèbre les connexions créées par ton enthousiasme."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Autorité verbale**

Ta Lune en Lion en Maison 3 veut s'exprimer avec créativité. Ton Ascendant Capricorne ajoute structure et sérieux : tu veux communiquer avec autorité, être reconnu·e pour ton expertise, parler avec poids.

**Domaine activé** : Maison 3 — Tes mots cherchent à construire quelque chose de durable. Tu veux que ta communication serve tes ambitions, que ton savoir soit respecté. L'apprentissage est stratégique.

**Ton approche instinctive** : Le Capricorne te fait peser chaque mot dans une logique à long terme. Tu veux que ce que tu dis renforce ta réputation. Cette gravité canalise le besoin de briller du Lion.

**Tensions possibles** : La tension entre spontanéité créative (Lion) et contrôle verbal (Capricorne). Tu peux paraître trop sérieux·se ou manquer de chaleur. La peur de dire quelque chose d'incorrect.

**Conseil clé** : Communiquer avec autorité tout en gardant de la chaleur et de l'authenticité.""",
        'weekly_advice': {
            'week_1': "Définis l'expertise pour laquelle tu veux être reconnu·e.",
            'week_2': "Partage tes connaissances avec autorité mesurée.",
            'week_3': "Construis ta réputation par des paroles qui comptent.",
            'week_4': "Mesure l'impact de ta communication sur tes objectifs."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Idées révolutionnaires**

Ta Lune en Lion en Maison 3 veut s'exprimer avec créativité. Ton Ascendant Verseau (opposé au Lion) crée une tension : tu veux briller par tes idées originales, choquer, innover verbalement.

**Domaine activé** : Maison 3 — Tes échanges cherchent l'originalité et l'innovation. Tu veux communiquer des idées avant-gardistes, défier les conventions, partager des visions futuristes. L'unique te fascine.

**Ton approche instinctive** : Le Verseau te pousse à penser différemment. Tu ne veux pas répéter ce que tout le monde dit : tu veux apporter une perspective radicalement nouvelle. Cette originalité peut fasciner ou aliéner.

**Tensions possibles** : Le conflit entre besoin d'admiration personnelle (Lion) et idéaux collectifs (Verseau). Être trop excentrique dans ta communication. Rejeter des idées juste parce qu'elles sont courantes.

**Conseil clé** : Innover verbalement tout en restant compréhensible et connecté.""",
        'weekly_advice': {
            'week_1': "Explore une idée vraiment originale qui te passionne.",
            'week_2': "Communique ta vision unique avec confiance.",
            'week_3': "Connecte tes idées aux besoins collectifs.",
            'week_4': "Célèbre comment tu as brisé des codes verbaux."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Poésie inspirée**

Ta Lune en Lion en Maison 3 cherche l'admiration par les mots. Ton Ascendant Poissons ajoute imagination et sensibilité : tu veux communiquer de manière poétique, inspirée, presque mystique.

**Domaine activé** : Maison 3 — Tes échanges sont teintés d'imagination et d'empathie. Tu excelles dans la communication artistique, les métaphores, les histoires qui touchent l'âme. L'invisible se dit.

**Ton approche instinctive** : Le Poissons te fait créer depuis l'intuition. Tes mots coulent naturellement quand tu es inspiré·e. Cette fluidité peut sublimer ou diluer ton message clair.

**Tensions possibles** : Le manque de structure dans ta communication. Tu risques de te perdre dans le flou ou les rêveries verbales. La difficulté à dire les choses concrètement.

**Conseil clé** : Ancrer ton inspiration poétique dans des mots que les autres peuvent comprendre.""",
        'weekly_advice': {
            'week_1': "Crée un espace pour l'écriture ou l'expression intuitive.",
            'week_2': "Communique quelque chose de poétique ou spirituel.",
            'week_3': "Donne forme concrète à tes inspirations verbales.",
            'week_4': "Partage ton art des mots avec douceur."
        }
    },

    # ==================== MAISON 4 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Foyer royal**

Ta Lune en Lion active la Maison 4 : ton foyer, tes racines, ta famille deviennent un terrain d'expression créative. Avec l'Ascendant Bélier, tu veux reconstruire ou transformer ton espace personnel avec audace.

**Domaine activé** : Maison 4 — Ton foyer doit refléter ta grandeur. Tu veux créer un espace qui t'inspire, qui impressionne, où tu te sens roi·reine. Les questions familiales demandent du courage.

**Ton approche instinctive** : Double feu sur les fondations : tu agis vite pour transformer ton environnement. Tu n'hésites pas à prendre des décisions radicales pour ton confort émotionnel.

**Tensions possibles** : Les conflits familiaux par manque de diplomatie. L'impatience avec les processus domestiques lents. Le besoin de dominer dans ton foyer peut créer des tensions.

**Conseil clé** : Créer un sanctuaire personnel qui nourrit ta créativité sans écraser les autres.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit changer dans ton espace personnel.",
            'week_2': "Lance un projet de transformation de ton foyer.",
            'week_3': "Résous un conflit familial avec courage et générosité.",
            'week_4': "Célèbre ton nouveau sanctuaire personnel."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Palais stable**

Ta Lune en Lion en Maison 4 veut un foyer magnifique. Ton Ascendant Taureau amplifie : tu veux créer un espace de confort luxueux et durable. La beauté et la stabilité domestique sont essentielles.

**Domaine activé** : Maison 4 — Ton foyer est un investissement dans ton bien-être. Tu veux que chaque élément soit de qualité, beau, confortable. L'enracinement passe par le luxe tangible.

**Ton approche instinctive** : Le Taureau te fait construire lentement ton palais. Tu choisis chaque pièce avec soin, tu veux que tout dure. Cette patience canalise le besoin d'immédiateté du Lion.

**Tensions possibles** : Les dépenses excessives pour ton foyer. L'attachement aux possessions domestiques. Le conflit entre besoin de changement (Lion) et résistance au changement (Taureau).

**Conseil clé** : Créer un foyer luxueux mais soutenable financièrement.""",
        'weekly_advice': {
            'week_1': "Définis le style de ton foyer idéal à long terme.",
            'week_2': "Investis dans un élément de qualité pour ton espace.",
            'week_3': "Organise et embellis ton environnement avec patience.",
            'week_4': "Savoure le confort durable que tu as créé."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Maison vivante**

Ta Lune en Lion en Maison 4 veut un foyer impressionnant. Ton Ascendant Gémeaux ajoute mouvement et communication : ton espace doit être stimulant intellectuellement, accueillir du monde, bouger.

**Domaine activé** : Maison 4 — Ton foyer est un lieu d'échanges et de créativité. Tu veux que les gens s'y sentent inspirés, que les conversations y soient riches. L'immobilité domestique t'ennuie.

**Ton approche instinctive** : Le Gémeaux te fait réaménager souvent, essayer de nouvelles choses. Tu veux un espace polyvalent qui reflète tes multiples facettes. Cette versatilité peut créer du chaos.

**Tensions possibles** : Le désordre par manque de structure. Tu risques de déménager ou changer trop souvent. Les besoins de stabilité familiale vs ton besoin de mouvement.

**Conseil clé** : Créer un foyer qui respire tout en gardant une base stable.""",
        'weekly_advice': {
            'week_1': "Réorganise un espace pour le rendre plus inspirant.",
            'week_2': "Invite des gens chez toi pour animer ton foyer.",
            'week_3': "Crée des zones multiples pour tes différentes activités.",
            'week_4': "Célèbre la vie que tu as insufflée dans ton espace."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Nid chaleureux**

Ta Lune en Lion en Maison 4 veut un foyer magnifique. Ton Ascendant Cancer, maître naturel de cette maison, amplifie : la famille et les racines deviennent le cœur de ton identité ce mois-ci.

**Domaine activé** : Maison 4 — Ton foyer est ton royaume émotionnel. Tu veux créer un sanctuaire qui nourrit, protège, réchauffe. La connexion avec tes racines et ta famille est puissante.

**Ton approche instinctive** : Le Cancer te rend protecteur·rice et nourricier·ère envers les tiens. Tu veux que tout le monde se sente aimé et en sécurité. Cette douceur adoucit le besoin de grandeur du Lion.

**Tensions possibles** : La sur-protection de ta famille. Les sautes d'humeur affectent l'ambiance domestique. Le besoin de contrôler l'espace par souci de sécurité.

**Conseil clé** : Créer un foyer qui rayonne de chaleur authentique et généreuse.""",
        'weekly_advice': {
            'week_1': "Renforce les liens avec ta famille ou tes proches.",
            'week_2': "Crée un moment spécial chez toi pour ceux que tu aimes.",
            'week_3': "Accepte ta vulnérabilité émotionnelle comme force.",
            'week_4': "Célèbre la sécurité émotionnelle que tu as bâtie."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Château personnel**

Double Lion sur la Maison 4 : ton foyer devient ton royaume absolu. L'énergie est dramatique, créative, centrée sur la création d'un espace qui reflète ta grandeur naturelle.

**Domaine activé** : Maison 4 — Ton foyer EST ton expression créative incarnée. Tu veux qu'il impressionne, qu'il inspire, qu'il raconte qui tu es vraiment. Chaque détail compte énormément.

**Ton approche instinctive** : Tu ne fais rien à moitié dans ton espace. Soit c'est grandiose, soit tu n'es pas satisfait·e. Cette exigence peut créer un palais ou une insatisfaction chronique.

**Tensions possibles** : Les attentes irréalistes sur ton foyer. Les dépenses excessives pour l'impressionner. Les conflits familiaux si tu imposes ta vision sans écouter.

**Conseil clé** : Créer un foyer qui te ressemble vraiment, sans chercher à prouver quoi que ce soit.""",
        'weekly_advice': {
            'week_1': "Définis l'espace qui reflète vraiment ton essence.",
            'week_2': "Lance un projet créatif dans ton foyer avec panache.",
            'week_3': "Partage ton espace avec générosité et fierté.",
            'week_4': "Célèbre le royaume que tu as créé."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Ordre élégant**

Ta Lune en Lion en Maison 4 veut un foyer impressionnant. Ton Ascendant Vierge tempère : tu veux que ton espace soit non seulement beau, mais parfaitement organisé, fonctionnel, impeccable.

**Domaine activé** : Maison 4 — Ton foyer cherche l'excellence pratique. Tu veux que chaque élément soit à sa place, serve un but, soit optimisé. La beauté ET l'utilité comptent.

**Ton approche instinctive** : La Vierge te fait analyser chaque aspect de ton espace. Tu veux perfectionner ton environnement. Cette exigence peut sublimer ou te paralyser.

**Tensions possibles** : L'autocritique sur ton foyer, jamais assez parfait. Tu risques de te surinvestir dans le nettoyage ou l'organisation. Le perfectionnisme crée de l'anxiété domestique.

**Conseil clé** : Créer un foyer impeccable sans perdre la chaleur et la spontanéité.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit être organisé dans ton espace.",
            'week_2': "Optimise un aspect de ton foyer avec précision.",
            'week_3': "Accepte l'imperfection domestique comme humaine.",
            'week_4': "Célèbre les améliorations concrètes réalisées."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Beauté partagée**

Ta Lune en Lion en Maison 4 veut un foyer magnifique. Ton Ascendant Balance ajoute harmonie et esthétique : ton espace doit être non seulement beau, mais équilibré, accueillant pour tous.

**Domaine activé** : Maison 4 — Ton foyer est un terrain d'expression artistique. Tu veux créer un environnement qui plaît à tous, qui facilite les connexions harmonieuses. Le design compte énormément.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre dans ton espace. Tu veux que chaque élément s'harmonise. Cette recherche esthétique peut embellir ou te rendre indécis·e.

**Tensions possibles** : L'indécision sur la décoration ou l'aménagement. Le besoin de plaire peut diluer ton style personnel. Les compromis constants sur ton espace.

**Conseil clé** : Créer un foyer esthétiquement parfait qui reste authentiquement le tien.""",
        'weekly_advice': {
            'week_1': "Définis ton style personnel pour ton espace.",
            'week_2': "Investis dans un élément esthétique qui t'inspire.",
            'week_3': "Crée de l'harmonie sans sacrifier ta personnalité.",
            'week_4': "Célèbre la beauté partagée que tu as créée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Sanctuaire profond**

Ta Lune en Lion en Maison 4 veut un foyer impressionnant. Ton Ascendant Scorpion ajoute intensité et mystère : ton espace doit être puissant, protégé, un lieu de transformation personnelle.

**Domaine activé** : Maison 4 — Ton foyer est ton temple secret. Tu veux créer un espace où tu peux te régénérer, explorer tes profondeurs, te sentir en contrôle absolu de ton environnement.

**Ton approche instinctive** : Le Scorpion te pousse à transformer radicalement ton espace ou tes racines. Tu veux éliminer ce qui ne sert plus, reconstruire depuis les fondations.

**Tensions possibles** : L'obsession du contrôle domestique. Les secrets de famille peuvent ressurgir. L'intensité émotionnelle affecte l'ambiance du foyer.

**Conseil clé** : Transformer ton espace en sanctuaire de guérison, pas de contrôle.""",
        'weekly_advice': {
            'week_1': "Regarde en face ce qui doit changer dans ton foyer.",
            'week_2': "Élimine ce qui ne nourrit plus ton âme.",
            'week_3': "Crée un espace de régénération profonde.",
            'week_4': "Observe comment ton foyer t'a transformé·e."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Base aventureuse**

Double feu sur la Maison 4 : ta Lune en Lion et ton Ascendant Sagittaire créent un foyer expansif, optimiste, ouvert sur le monde. Tu veux un espace qui inspire l'aventure et la croissance.

**Domaine activé** : Maison 4 — Ton foyer est un point de départ pour l'exploration. Tu veux qu'il reflète tes voyages, tes croyances, ta vision du monde. L'immobilité domestique t'étouffe.

**Ton approche instinctive** : Le Sagittaire te fait voir ton foyer comme une base d'opérations, pas une prison. Tu veux être libre même chez toi. Cette spontanéité peut créer de l'instabilité.

**Tensions possibles** : La difficulté à t'enraciner vraiment. Le besoin de bouger peut perturber la vie familiale. Les promesses domestiques non tenues par impatience.

**Conseil clé** : Créer un foyer qui nourrit ton esprit d'aventure sans fuir l'enracinement.""",
        'weekly_advice': {
            'week_1': "Définis ce que 'chez toi' signifie vraiment pour toi.",
            'week_2': "Intègre des éléments de tes voyages dans ton espace.",
            'week_3': "Crée un rituel domestique qui t'ancre sans t'enfermer.",
            'week_4': "Célèbre ton foyer comme base de tes aventures."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fondations solides**

Ta Lune en Lion en Maison 4 veut un foyer magnifique. Ton Ascendant Capricorne ajoute structure et ambition : tu veux construire un patrimoine familial durable, un foyer qui dure.

**Domaine activé** : Maison 4 — Ton foyer est un investissement à long terme. Tu veux créer une base solide pour ta réussite, un espace qui reflète ton statut tout en restant fonctionnel.

**Ton approche instinctive** : Le Capricorne te fait planifier ton enracinement sur des décennies. Tu construis ton foyer pierre par pierre, avec discipline. Cette patience canalise l'impulsivité du Lion.

**Tensions possibles** : La tension entre besoin de luxe immédiat (Lion) et construction patiente (Capricorne). Le foyer peut devenir trop sérieux, manquer de chaleur.

**Conseil clé** : Bâtir un foyer solide qui reste vivant et chaleureux.""",
        'weekly_advice': {
            'week_1': "Définis ton plan patrimonial domestique à long terme.",
            'week_2': "Prends une action concrète pour ton foyer futur.",
            'week_3': "Équilibre ambition et confort dans ton espace.",
            'week_4': "Mesure les fondations solides que tu as posées."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Foyer unique**

Ta Lune en Lion en Maison 4 veut un foyer impressionnant. Ton Ascendant Verseau (opposé au Lion) crée une tension : tu veux un espace original, non-conventionnel, qui te différencie.

**Domaine activé** : Maison 4 — Ton foyer cherche l'unicité. Tu veux créer un espace qui défie les normes, qui reflète ta vision futuriste. L'innovation domestique t'attire.

**Ton approche instinctive** : Le Verseau te pousse à expérimenter avec ton espace. Tu n'as pas peur des choix audacieux qui surprennent. Cette originalité peut fasciner ou aliéner.

**Tensions possibles** : Le conflit entre besoin de grandeur personnelle (Lion) et détachement (Verseau). Ton foyer peut paraître froid ou trop intellectuel.

**Conseil clé** : Créer un foyer unique qui reste humainement chaleureux.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui rend ton foyer vraiment unique.",
            'week_2': "Expérimente avec un élément non-conventionnel.",
            'week_3': "Connecte ton espace à des valeurs collectives.",
            'week_4': "Célèbre comment tu as brisé des codes domestiques."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Refuge inspiré**

Ta Lune en Lion en Maison 4 cherche un foyer magnifique. Ton Ascendant Poissons ajoute imagination et spiritualité : ton espace doit être un sanctuaire artistique, un lieu de rêve et d'inspiration.

**Domaine activé** : Maison 4 — Ton foyer est un espace de création et de méditation. Tu veux qu'il soit fluide, inspirant, presque magique. La frontière entre intérieur et imaginaire s'estompe.

**Ton approche instinctive** : Le Poissons te fait créer depuis l'intuition. Ton espace évolue selon ton inspiration. Cette fluidité peut créer de la beauté ou du chaos.

**Tensions possibles** : Le manque de limites claires dans ton foyer. Tu risques de fuir dans le rêve plutôt que d'affronter les responsabilités domestiques.

**Conseil clé** : Ancrer ton inspiration dans un foyer tangible et fonctionnel.""",
        'weekly_advice': {
            'week_1': "Crée un espace de méditation ou création chez toi.",
            'week_2': "Intègre des éléments artistiques ou spirituels.",
            'week_3': "Donne structure à ton inspiration domestique.",
            'week_4': "Célèbre le sanctuaire que tu as manifesté."
        }
    },

    # ==================== MAISON 5 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Créativité explosive**

Ta Lune en Lion active la Maison 5, sa maison naturelle : la créativité, le jeu, la romance, les enfants. Avec l'Ascendant Bélier, l'énergie est pure joie créative, audace, expression spontanée.

**Domaine activé** : Maison 5 — Tu es dans ton élément naturel. La créativité coule à flots, les romances s'embrasent, le jeu devient central. Tu veux exprimer ta grandeur par la joie pure.

**Ton approche instinctive** : Triple feu sur la créativité : tu te lances sans hésiter dans des projets créatifs, des romances passionnées, des aventures ludiques. L'audace est ton terrain de jeu.

**Tensions possibles** : L'impulsivité dans les romances peut créer du drame. Les projets créatifs commencés sans finition. Le besoin de risque peut mener à l'imprudence.

**Conseil clé** : Canaliser cette énergie créative explosive vers quelque chose qui dure.""",
        'weekly_advice': {
            'week_1': "Lance un projet créatif audacieux qui t'enflamme.",
            'week_2': "Prends un risque romantique ou ludique avec panache.",
            'week_3': "Exprime ta créativité sans censure ni hésitation.",
            'week_4': "Célèbre la joie pure que tu as générée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Beauté sensuelle**

Ta Lune en Lion en Maison 5 veut créer et s'amuser. Ton Ascendant Taureau ajoute sensualité et patience : tu veux que ta créativité soit belle, tangible, durable. Le plaisir devient art.

**Domaine activé** : Maison 5 — Ta créativité cherche la qualité et la beauté. Tu veux créer des œuvres qui durent, vivre des plaisirs sensuels, construire des romances solides. Le luxe créatif t'attire.

**Ton approche instinctive** : Le Taureau te fait savourer chaque moment créatif. Tu prends ton temps pour perfectionner, pour ressentir. Cette patience tempère l'urgence du Lion.

**Tensions possibles** : La tension entre besoin de reconnaissance immédiate (Lion) et processus créatif lent (Taureau). La possessivité dans les romances.

**Conseil clé** : Créer avec patience des œuvres et des moments qui durent.""",
        'weekly_advice': {
            'week_1': "Définis un projet créatif de qualité à développer.",
            'week_2': "Investis dans une expérience sensorielle luxueuse.",
            'week_3': "Construis lentement mais sûrement ta création.",
            'week_4': "Savoure la beauté durable que tu as créée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Jeu brillant**

Ta Lune en Lion en Maison 5 veut créer et jouer. Ton Ascendant Gémeaux amplifie : tu veux multiplier les projets créatifs, les flirts, les jeux intellectuels. La vie devient spectacle ludique.

**Domaine activé** : Maison 5 — Ta créativité est polyvalente et communicative. Tu excelles dans les arts qui mélangent intellect et expression : écriture créative, théâtre, jeux de mots. Le divertissement intelligent.

**Ton approche instinctive** : Le Gémeaux te fait jongler avec plusieurs projets créatifs. Tu aimes flirter avec des idées, des personnes, des possibilités. Cette versatilité peut disperser ton talent.

**Tensions possibles** : Trop de projets créatifs simultanés. Les romances superficielles par peur de l'engagement. Le manque de profondeur dans ton expression.

**Conseil clé** : Utiliser ta polyvalence créative sans te disperser dans tous les sens.""",
        'weekly_advice': {
            'week_1': "Explore 2-3 formes de créativité qui t'attirent.",
            'week_2': "Flirte avec de nouvelles idées et personnes.",
            'week_3': "Choisis un projet principal à développer vraiment.",
            'week_4': "Partage tes créations multiples avec légèreté."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Cœur créatif**

Ta Lune en Lion en Maison 5 veut créer et rayonner. Ton Ascendant Cancer ajoute profondeur émotionnelle : tu veux que ta créativité touche les cœurs, que tes romances soient nourricières.

**Domaine activé** : Maison 5 — Ta créativité vient du cœur. Tu veux créer des œuvres qui émeuvent, vivre des romances qui sécurisent, prendre soin des enfants avec fierté. L'amour devient créatif.

**Ton approche instinctive** : Le Cancer te rend sensible dans ton expression créative. Tu crées depuis tes émotions, tu veux toucher l'âme. Cette vulnérabilité sublime ton rayonnement.

**Tensions possibles** : Les sautes d'humeur affectent ta créativité. La sur-protection dans les romances ou avec les enfants. L'hypersensibilité aux critiques de ton travail créatif.

**Conseil clé** : Créer depuis ton cœur authentique sans te perdre dans l'émotion.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose qui exprime tes émotions vraies.",
            'week_2': "Partage ton cœur dans une romance ou amitié profonde.",
            'week_3': "Accepte ta vulnérabilité créative comme force.",
            'week_4': "Célèbre l'impact émotionnel de ton expression."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Pure joie solaire**

Triple Lion sur la Maison 5 naturelle du Lion : l'énergie créative est à son maximum. Tu es dans ton pouvoir absolu, rayonnant de créativité, de passion, de joie de vivre.

**Domaine activé** : Maison 5 — Ce mois-ci, tu ES la créativité incarnée. Tout ce que tu touches devient art, jeu, plaisir. Les romances s'embrasent, les enfants t'inspirent, la vie devient spectacle.

**Ton approche instinctive** : Tu ne retiens rien. Toute ton énergie va vers l'expression créative, le plaisir, la romance, le jeu. Cette intensité peut être magnifique ou épuisante.

**Tensions possibles** : L'ego créatif démesuré. Le besoin constant d'admiration pour ton travail. Les drames romantiques par excès. L'épuisement par trop de projets simultanés.

**Conseil clé** : Rayonner pleinement tout en restant généreux·se et ouvert·e aux autres.""",
        'weekly_advice': {
            'week_1': "Lance ton projet créatif le plus ambitieux.",
            'week_2': "Vis tes passions sans retenue ni excuses.",
            'week_3': "Partage ta joie de créer avec le monde.",
            'week_4': "Célèbre ta puissance créative maximale."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Art perfectionné**

Ta Lune en Lion en Maison 5 veut créer avec panache. Ton Ascendant Vierge tempère : tu veux que ta créativité soit non seulement brillante, mais parfaite, utile, impeccable.

**Domaine activé** : Maison 5 — Ta créativité cherche l'excellence technique. Tu veux maîtriser ton art, créer des œuvres impeccables, perfectionner chaque détail. Le talent rencontre le travail.

**Ton approche instinctive** : La Vierge te fait analyser et améliorer sans cesse ta créativité. Tu veux que chaque projet soit irréprochable. Cette exigence peut sublimer ou bloquer.

**Tensions possibles** : L'autocritique paralyse ton expression créative. Tu risques de ne jamais te sentir assez bon·ne pour partager. Le perfectionnisme tue la spontanéité.

**Conseil clé** : Accepter que la perfection créative inclut l'imperfection humaine.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine créatif à perfectionner.",
            'week_2': "Crée même si tu ne te sens pas parfait·e.",
            'week_3': "Utilise ton exigence pour t'améliorer, pas te critiquer.",
            'week_4': "Célèbre tes progrès créatifs mesurables."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Romance élégante**

Ta Lune en Lion en Maison 5 veut créer et aimer. Ton Ascendant Balance ajoute grâce et harmonie : ta créativité devient art esthétique, tes romances deviennent poésie, ton jeu devient danse.

**Domaine activé** : Maison 5 — Ta créativité cherche la beauté et l'équilibre. Tu veux créer des œuvres qui plaisent, vivre des romances harmonieuses, jouer avec élégance. L'esthétique règne.

**Ton approche instinctive** : La Balance te fait chercher l'approbation dans ta créativité. Tu veux que ton art séduise, que tes romances soient belles. Cette recherche peut diluer ton authenticité.

**Tensions possibles** : L'indécision créative par peur de déplaire. Les compromis dans les romances jusqu'à perdre ton identité. Le besoin de plaire affaiblit ton expression unique.

**Conseil clé** : Créer avec grâce tout en restant fidèle à ta vision unique.""",
        'weekly_advice': {
            'week_1': "Définis ton style créatif personnel et esthétique.",
            'week_2': "Crée quelque chose de beau et authentique.",
            'week_3': "Vis une romance équilibrée mais passionnée.",
            'week_4': "Célèbre l'harmonie créative que tu as manifestée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Passion transformante**

Ta Lune en Lion en Maison 5 veut créer et aimer avec panache. Ton Ascendant Scorpion ajoute intensité et profondeur : ta créativité devient cathartique, tes romances deviennent fusion.

**Domaine activé** : Maison 5 — Ta créativité explore les profondeurs. Tu veux créer des œuvres qui transforment, vivre des passions intenses, jouer avec le pouvoir. Rien de superficiel.

**Ton approche instinctive** : Le Scorpion te pousse à creuser dans ton expression créative. Tu veux toucher les zones d'ombre, révéler des vérités cachées. Cette intensité donne du poids à ton art.

**Tensions possibles** : L'obsession créative ou romantique. Les drames passionnels par jalousie. Le besoin de contrôler ton expression jusqu'à la rigidifier.

**Conseil clé** : Transformer ta puissance créative en force de guérison, pas de domination.""",
        'weekly_advice': {
            'week_1': "Plonge dans une créativité profonde et cathartique.",
            'week_2': "Vis une passion intense mais respectueuse.",
            'week_3': "Utilise ton art pour transformer, pas manipuler.",
            'week_4': "Observe comment tu as évolué par ta créativité."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Joie expansive**

Double feu sur la Maison 5 : ta Lune en Lion et ton Ascendant Sagittaire créent une énergie créative joyeuse, optimiste, expansive. La vie devient une célébration créative.

**Domaine activé** : Maison 5 — Ta créativité cherche l'inspiration et la liberté. Tu veux créer des œuvres qui inspirent, vivre des romances aventureuses, jouer sans limites. L'enthousiasme règne.

**Ton approche instinctive** : Le Sagittaire te fait voir les possibilités créatives infinies. Tu crois en ton talent, tu oses tout essayer. Cette foi peut créer des miracles ou des illusions.

**Tensions possibles** : L'excès d'optimisme créatif. Promettre des projets sans les finir. Les romances qui commencent fort et s'éteignent vite par impatience.

**Conseil clé** : Canaliser ton enthousiasme créatif vers des projets qui aboutissent.""",
        'weekly_advice': {
            'week_1': "Définis une vision créative inspirante mais réalisable.",
            'week_2': "Lance-toi dans l'aventure créative avec foi.",
            'week_3': "Partage ton enthousiasme pour inspirer les autres.",
            'week_4': "Célèbre la joie que tu as semée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Maîtrise créative**

Ta Lune en Lion en Maison 5 veut créer avec joie. Ton Ascendant Capricorne ajoute discipline et ambition : tu veux que ta créativité devienne une carrière, que ton talent soit reconnu professionnellement.

**Domaine activé** : Maison 5 — Ta créativité cherche la légitimité. Tu veux maîtriser ton art, être respecté·e pour ton talent, construire une réputation créative solide. Le jeu devient sérieux.

**Ton approche instinctive** : Le Capricorne te fait planifier ta carrière créative sur le long terme. Tu travailles dur pour perfectionner ton art. Cette discipline canalise l'impulsivité du Lion.

**Tensions possibles** : La tension entre spontanéité créative (Lion) et contrôle rigide (Capricorne). Le risque de perdre la joie dans le travail acharné.

**Conseil clé** : Bâtir une maîtrise créative sans perdre la joie qui la nourrit.""",
        'weekly_advice': {
            'week_1': "Définis tes ambitions créatives à long terme.",
            'week_2': "Prends une action sérieuse pour ton art.",
            'week_3': "Équilibre discipline et spontanéité créative.",
            'week_4': "Mesure tes progrès vers la maîtrise."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Art révolutionnaire**

Ta Lune en Lion en Maison 5 veut créer avec panache. Ton Ascendant Verseau (opposé au Lion) crée une tension : tu veux que ton art soit original, avant-gardiste, qui défie les conventions.

**Domaine activé** : Maison 5 — Ta créativité cherche l'innovation. Tu veux créer ce que personne n'a fait, surprendre, choquer peut-être. L'unicité créative est ton terrain.

**Ton approche instinctive** : Le Verseau te pousse à expérimenter radicalement. Tu refuses les formes créatives conventionnelles. Cette originalité peut fasciner ou aliéner ton audience.

**Tensions possibles** : Le conflit entre besoin d'admiration personnelle (Lion) et détachement (Verseau). Rejeter des formes créatives efficaces juste parce qu'elles sont classiques.

**Conseil clé** : Innover créativement tout en restant accessible et connecté·e.""",
        'weekly_advice': {
            'week_1': "Explore une forme créative vraiment originale.",
            'week_2': "Crée quelque chose qui défie les attentes.",
            'week_3': "Connecte ton art unique à des enjeux collectifs.",
            'week_4': "Célèbre comment tu as révolutionné ton expression."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Art inspiré**

Ta Lune en Lion en Maison 5 cherche l'admiration créative. Ton Ascendant Poissons ajoute imagination et spiritualité : tu veux créer depuis l'inspiration divine, canaliser l'invisible.

**Domaine activé** : Maison 5 — Ta créativité coule depuis ton intuition. Tu excelles dans les arts imaginatifs : musique, poésie, arts visuels. Le flow créatif est naturel quand tu lâches prise.

**Ton approche instinctive** : Le Poissons te fait créer depuis un espace de réceptivité. Tu canalises plus que tu ne construis. Cette fluidité peut créer de la magie ou de la confusion.

**Tensions possibles** : Le manque de structure dans tes projets créatifs. Tu risques de te perdre dans le rêve sans concrétiser. La difficulté à recevoir des critiques constructives.

**Conseil clé** : Ancrer ton inspiration créative dans des formes tangibles et partageables.""",
        'weekly_advice': {
            'week_1': "Crée un espace pour recevoir l'inspiration créative.",
            'week_2': "Laisse-toi guider par ton intuition artistique.",
            'week_3': "Donne forme concrète à tes visions créatives.",
            'week_4': "Partage ton art avec douceur et confiance."
        }
    },

    # ==================== MAISON 6 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Travail passionné**

Ta Lune en Lion active la Maison 6 : travail quotidien, santé, routines. Avec l'Ascendant Bélier, tu veux conquérir tes tâches avec panache, transformer ton quotidien en terrain d'héroïsme.

**Domaine activé** : Maison 6 — Ton travail doit refléter ta grandeur. Tu veux exceller dans ce que tu fais, être reconnu·e pour ton professionnalisme, transformer même les tâches banales en performances.

**Ton approche instinctive** : Double feu sur le travail : tu attaques tes responsabilités avec énergie et courage. Tu veux être le·la meilleur·e, gagner des batailles quotidiennes.

**Tensions possibles** : L'épuisement par excès d'intensité. Les conflits avec collègues ou hiérarchie par manque de diplomatie. L'impatience avec les processus lents.

**Conseil clé** : Canaliser ton énergie vers l'excellence sans te consumer.""",
        'weekly_advice': {
            'week_1': "Identifie où tu peux exceller dans ton travail.",
            'week_2': "Prends une initiative courageuse dans tes tâches.",
            'week_3': "Soigne ta santé avec la même passion que ton travail.",
            'week_4': "Célèbre tes victoires quotidiennes."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Excellence durable**

Ta Lune en Lion en Maison 6 veut briller au travail. Ton Ascendant Taureau ajoute patience et qualité : tu veux exceller dans ton travail, mais de manière stable, durable, avec du plaisir.

**Domaine activé** : Maison 6 — Ton travail cherche la qualité constante. Tu veux créer de la valeur par ton professionnalisme, être reconnu·e pour ton sérieux, ta fiabilité, ta constance.

**Ton approche instinctive** : Le Taureau te fait travailler lentement mais sûrement. Tu veux que chaque tâche soit bien faite. Cette patience tempère le besoin de reconnaissance immédiate du Lion.

**Tensions possibles** : La frustration si les résultats ne viennent pas vite. Le risque de routine ennuyeuse. L'entêtement dans tes méthodes de travail.

**Conseil clé** : Construire une excellence professionnelle qui dure, pas qui éblouit un jour.""",
        'weekly_advice': {
            'week_1': "Définis les standards de qualité que tu veux incarner.",
            'week_2': "Travaille avec constance et attention au détail.",
            'week_3': "Intègre du plaisir dans tes routines quotidiennes.",
            'week_4': "Savoure la solidité de ton travail accompli."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Polyvalence brillante**

Ta Lune en Lion en Maison 6 veut exceller au travail. Ton Ascendant Gémeaux ajoute agilité et communication : tu veux briller dans plusieurs domaines, jongler avec les tâches intelligemment.

**Domaine activé** : Maison 6 — Ton travail devient un terrain de jeu intellectuel. Tu excelles dans les tâches qui requièrent communication, adaptabilité, intelligence. La routine variée t'inspire.

**Ton approche instinctive** : Le Gémeaux te rend efficace dans les tâches multiples. Tu sais organiser, communiquer, déléguer. Cette versatilité peut maximiser ou disperser ton impact.

**Tensions possibles** : Trop de projets simultanés créent du stress. Le manque de profondeur dans ton expertise. La dispersion mentale affecte ta santé nerveuse.

**Conseil clé** : Utiliser ta polyvalence pour optimiser, pas pour te surcharger.""",
        'weekly_advice': {
            'week_1': "Organise tes tâches pour maximiser ton efficacité.",
            'week_2': "Communique brillamment dans ton travail.",
            'week_3': "Choisis 2-3 domaines principaux d'excellence.",
            'week_4': "Célèbre ta gestion intelligente du quotidien."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Service du cœur**

Ta Lune en Lion en Maison 6 veut exceller au travail. Ton Ascendant Cancer ajoute sensibilité et soin : tu veux que ton travail nourrisse les autres, que ton service vienne du cœur.

**Domaine activé** : Maison 6 — Ton travail devient une extension de ta générosité. Tu excelles dans les professions de soin, d'aide, de service. Ta santé est liée à ton bien-être émotionnel.

**Ton approche instinctive** : Le Cancer te rend empathique au travail. Tu prends soin de tes collègues, tu crées une ambiance chaleureuse. Cette sensibilité adoucit le besoin de reconnaissance du Lion.

**Tensions possibles** : La sur-implication émotionnelle dans ton travail. Les sautes d'humeur affectent ta performance. Le risque d'épuisement par excès de dévouement.

**Conseil clé** : Servir avec cœur tout en protégeant ton énergie émotionnelle.""",
        'weekly_advice': {
            'week_1': "Identifie comment ton travail peut nourrir les autres.",
            'week_2': "Crée une ambiance chaleureuse dans ton quotidien.",
            'week_3': "Protège ta santé émotionnelle au travail.",
            'week_4': "Célèbre l'impact humain de ton service."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Performance royale**

Double Lion sur la Maison 6 : ton travail quotidien devient une scène. Tu veux être le·la meilleur·e dans ce que tu fais, transformer même les tâches ordinaires en performances extraordinaires.

**Domaine activé** : Maison 6 — Ton travail EST ton expression créative. Tu n'acceptes pas la médiocrité, tu veux briller dans chaque tâche. Ta santé reflète ton rayonnement intérieur.

**Ton approche instinctive** : Tu ne fais rien à moitié au travail. Soit tu excelles avec panache, soit tu te sens frustré·e. Cette intensité peut te propulser ou te consumer.

**Tensions possibles** : L'épuisement par besoin constant de performance. Les conflits d'ego au travail. La fierté blessée face aux critiques professionnelles.

**Conseil clé** : Exceller dans ton travail sans que ton ego en dépende complètement.""",
        'weekly_advice': {
            'week_1': "Définis où tu veux vraiment exceller ce mois-ci.",
            'week_2': "Donne le meilleur de toi-même avec fierté.",
            'week_3': "Accepte l'imperfection sans perdre ton exigence.",
            'week_4': "Célèbre ton professionnalisme rayonnant."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfection humble**

Ta Lune en Lion en Maison 6 veut briller au travail. Ton Ascendant Vierge, maître naturel de cette maison, amplifie : tu veux non seulement exceller, mais être impeccable, utile, irréprochable.

**Domaine activé** : Maison 6 — Le travail devient ton terrain de perfectionnement absolu. Tu veux maîtriser chaque détail, optimiser chaque processus, être reconnu·e pour ton excellence technique.

**Ton approche instinctive** : La Vierge te rend analytique et exigeant·e. Tu vois chaque imperfection, tu veux tout améliorer. Cette rigueur peut sublimer ou paralyser ton travail.

**Tensions possibles** : L'autocritique excessive sur ta performance. Le perfectionnisme paralyse ton action. Le stress chronique affecte ta santé.

**Conseil clé** : Viser l'excellence sans tomber dans la tyrannie du perfectionnisme.""",
        'weekly_advice': {
            'week_1': "Identifie un domaine de travail à perfectionner.",
            'week_2': "Travaille avec exigence mais sans autocritique.",
            'week_3': "Soigne ta santé avec la même attention que ton travail.",
            'week_4': "Célèbre tes progrès mesurables et concrets."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Collaboration élégante**

Ta Lune en Lion en Maison 6 veut exceller au travail. Ton Ascendant Balance ajoute diplomatie et coopération : tu veux briller en travaillant harmonieusement avec les autres.

**Domaine activé** : Maison 6 — Ton travail cherche l'équilibre et l'esthétique. Tu excelles dans les collaborations, la médiation, les environnements harmonieux. Le travail d'équipe te valorise.

**Ton approche instinctive** : La Balance te fait chercher le consensus au travail. Tu veux que tout le monde s'entende, que l'ambiance soit agréable. Cette recherche peut diluer ton leadership.

**Tensions possibles** : L'indécision professionnelle par peur de déplaire. Le risque de trop adapter ton travail aux attentes des autres. L'évitement des conflits nécessaires.

**Conseil clé** : Travailler harmonieusement tout en affirmant ton excellence unique.""",
        'weekly_advice': {
            'week_1': "Définis comment tu veux contribuer en équipe.",
            'week_2': "Crée de l'harmonie professionnelle sans t'effacer.",
            'week_3': "Affirme ton expertise avec grâce et fermeté.",
            'week_4': "Célèbre les collaborations fructueuses créées."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Transformation par le travail**

Ta Lune en Lion en Maison 6 veut exceller au travail. Ton Ascendant Scorpion ajoute intensité et profondeur : tu veux que ton travail transforme, que ton impact soit puissant et durable.

**Domaine activé** : Maison 6 — Ton travail devient un terrain de transformation personnelle. Tu veux éliminer ce qui ne fonctionne pas, reconstruire depuis les fondations, avoir un pouvoir réel.

**Ton approche instinctive** : Le Scorpion te pousse à creuser en profondeur dans ton travail. Tu ne fais pas semblant, tu veux des résultats réels. Cette intensité peut transformer ou consumer.

**Tensions possibles** : L'obsession du contrôle au travail. Les luttes de pouvoir avec collègues ou hiérarchie. L'intensité émotionnelle affecte ta santé.

**Conseil clé** : Transformer ton environnement de travail sans le dominer par la force.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit vraiment changer dans ton travail.",
            'week_2': "Élimine une habitude professionnelle toxique.",
            'week_3': "Utilise ton pouvoir pour transformer, pas dominer.",
            'week_4': "Observe comment ton travail t'a transformé·e."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Service inspirant**

Double feu sur la Maison 6 : ta Lune en Lion et ton Ascendant Sagittaire créent un travail enthousiaste, optimiste, porteur de sens. Tu veux que ton travail inspire et élève.

**Domaine activé** : Maison 6 — Ton travail cherche un sens plus grand. Tu veux servir une vision, inspirer par ton exemple, créer de l'impact au-delà des tâches quotidiennes. Le sens compte autant que l'excellence.

**Ton approche instinctive** : Le Sagittaire te fait voir les possibilités d'expansion dans ton travail. Tu crois en ton potentiel professionnel. Cette foi peut t'élever ou te rendre insouciant·e.

**Tensions possibles** : L'excès d'optimisme sur ta charge de travail. Le manque d'attention aux détails pratiques. La difficulté avec les routines ennuyeuses.

**Conseil clé** : Trouver le sens dans ton travail quotidien sans négliger l'exécution.""",
        'weekly_advice': {
            'week_1': "Définis le sens profond de ton travail actuel.",
            'week_2': "Inspire tes collègues par ton enthousiasme.",
            'week_3': "Reste ancré·e dans les tâches concrètes.",
            'week_4': "Célèbre l'impact inspirant de ton service."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Maîtrise professionnelle**

Ta Lune en Lion en Maison 6 veut exceller au travail. Ton Ascendant Capricorne amplifie : tu veux construire une réputation professionnelle solide, être respecté·e pour ton sérieux et ton excellence.

**Domaine activé** : Maison 6 — Ton travail est un terrain d'ambition sérieuse. Tu veux grimper professionnellement, maîtriser ton domaine, être reconnu·e comme expert·e. La discipline rencontre le besoin de briller.

**Ton approche instinctive** : Le Capricorne te fait planifier ta carrière sur le long terme. Chaque tâche quotidienne sert un objectif plus grand. Cette patience stratégique canalise bien l'énergie du Lion.

**Tensions possibles** : Le conflit entre besoin de reconnaissance immédiate (Lion) et patience professionnelle (Capricorne). Le risque de devenir trop sérieux·se, de perdre la joie.

**Conseil clé** : Bâtir une excellence professionnelle durable sans perdre ta flamme.""",
        'weekly_advice': {
            'week_1': "Définis tes ambitions professionnelles à long terme.",
            'week_2': "Prends une action stratégique pour ta carrière.",
            'week_3': "Équilibre discipline et passion dans ton travail.",
            'week_4': "Mesure tes progrès vers la maîtrise professionnelle."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Travail innovant**

Ta Lune en Lion en Maison 6 veut exceller au travail. Ton Ascendant Verseau (opposé au Lion) crée une tension : tu veux briller en faisant les choses différemment, innover dans ton domaine.

**Domaine activé** : Maison 6 — Ton travail cherche l'originalité et l'innovation. Tu veux utiliser de nouvelles méthodes, challenger les processus établis, contribuer à une cause collective par ton travail.

**Ton approche instinctive** : Le Verseau te pousse à penser différemment sur ton travail. Tu refuses les routines rigides. Cette originalité peut révolutionner ou déstabiliser ton environnement.

**Tensions possibles** : Le conflit entre besoin de reconnaissance personnelle (Lion) et travail collectif (Verseau). Rejeter des méthodes efficaces juste parce qu'elles sont classiques.

**Conseil clé** : Innover professionnellement où ça apporte de la vraie valeur.""",
        'weekly_advice': {
            'week_1': "Identifie un processus de travail à révolutionner.",
            'week_2': "Teste une approche innovante dans tes tâches.",
            'week_3': "Connecte ton travail à une cause collective.",
            'week_4': "Célèbre comment tu as brisé des codes professionnels."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Service intuitif**

Ta Lune en Lion en Maison 6 cherche l'excellence au travail. Ton Ascendant Poissons ajoute sensibilité et intuition : tu veux servir depuis ton cœur, travailler dans le flow, guérir par ton service.

**Domaine activé** : Maison 6 — Ton travail est influencé par ton intuition. Tu excelles dans les professions d'aide, de soin, artistiques. Ta santé dépend de ton alignement spirituel et émotionnel.

**Ton approche instinctive** : Le Poissons te fait travailler depuis l'inspiration. Tu es dans le flow quand tu lâches prise. Cette fluidité peut créer de la magie ou du manque de structure.

**Tensions possibles** : Le manque de limites claires au travail. Tu risques de te sacrifier ou de fuir les responsabilités. La difficulté avec les tâches concrètes et répétitives.

**Conseil clé** : Servir intuitivement tout en gardant des structures qui te protègent.""",
        'weekly_advice': {
            'week_1': "Écoute ton intuition sur ton travail et ta santé.",
            'week_2': "Sers depuis un espace de compassion alignée.",
            'week_3': "Crée des limites saines dans ton service.",
            'week_4': "Célèbre l'impact guérisseur de ton travail."
        }
    },

    # ==================== MAISON 7 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Partenariats passionnés**

Ta Lune en Lion active la Maison 7 : relations, partenariats, collaborations. Avec l'Ascendant Bélier, tu veux des relations intenses, passionnées, où tu peux briller tout en respectant l'autre.

**Domaine activé** : Maison 7 — Tes relations deviennent un terrain d'expression créative. Tu veux des partenaires qui t'admirent, qui te challengent, qui te font rayonner. Les collaborations doivent être dynamiques.

**Ton approche instinctive** : Double feu dans les relations : tu es direct·e, passionné·e, parfois impulsif·ve. Tu veux conquérir mais aussi être conquis·e. L'intensité crée des étincelles.

**Tensions possibles** : Les conflits d'ego dans les partenariats. L'impatience avec les compromis nécessaires. Le besoin de dominer peut déséquilibrer la relation.

**Conseil clé** : Créer des partenariats où chacun peut briller sans écraser l'autre.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu veux vraiment dans tes relations.",
            'week_2': "Prends une initiative courageuse dans un partenariat.",
            'week_3': "Équilibre leadership et compromis relationnel.",
            'week_4': "Célèbre les connexions passionnées créées."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Unions stables**

Ta Lune en Lion en Maison 7 veut des relations admiratives. Ton Ascendant Taureau ajoute loyauté et stabilité : tu veux briller dans tes relations, mais avec des partenaires fiables, durables.

**Domaine activé** : Maison 7 — Tes partenariats cherchent la qualité et la durabilité. Tu veux être admiré·e mais dans une relation sécurisante. La loyauté et le luxe partagé comptent.

**Ton approche instinctive** : Le Taureau te fait construire lentement des relations solides. Tu veux des partenaires qui durent. Cette patience tempère le besoin d'intensité immédiate du Lion.

**Tensions possibles** : La tension entre besoin d'admiration (Lion) et besoin de confort (Taureau). La possessivité peut étouffer. L'entêtement dans les conflits relationnels.

**Conseil clé** : Construire des partenariats qui brillent ET qui durent.""",
        'weekly_advice': {
            'week_1': "Définis les valeurs essentielles dans tes relations.",
            'week_2': "Investis dans la qualité de tes partenariats existants.",
            'week_3': "Reste ouvert·e au changement sans perdre ta stabilité.",
            'week_4': "Savoure la solidité de tes connexions."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Connexions brillantes**

Ta Lune en Lion en Maison 7 veut des relations admiratives. Ton Ascendant Gémeaux ajoute communication et versatilité : tu veux des partenaires intellectuellement stimulants, avec qui tu peux briller verbalement.

**Domaine activé** : Maison 7 — Tes relations cherchent la stimulation mentale. Tu veux des conversations riches, des échanges d'idées, des partenaires qui comprennent ta complexité. La variété relationnelle t'attire.

**Ton approche instinctive** : Le Gémeaux te rend adaptable dans les relations. Tu sais communiquer tes besoins, négocier. Cette agilité peut enrichir ou disperser ton engagement.

**Tensions possibles** : La difficulté à s'engager profondément. Tu risques de papillonner entre plusieurs connexions. Le manque de profondeur émotionnelle.

**Conseil clé** : Utiliser ta communication pour approfondir, pas juste séduire.""",
        'weekly_advice': {
            'week_1': "Explore ce que tu cherches vraiment dans les relations.",
            'week_2': "Communique clairement tes besoins et désirs.",
            'week_3': "Approfondis 1-2 connexions au lieu de tout survoler.",
            'week_4': "Célèbre la richesse de tes échanges relationnels."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Amour nourrissant**

Ta Lune en Lion en Maison 7 veut briller dans les relations. Ton Ascendant Cancer ajoute profondeur émotionnelle : tu veux des partenariats qui nourrissent ton cœur, où tu peux être généreux·se et protégé·e.

**Domaine activé** : Maison 7 — Tes relations cherchent la sécurité émotionnelle ET l'admiration. Tu veux être vu·e dans ta grandeur mais aussi dans ta vulnérabilité. L'intimité profonde compte.

**Ton approche instinctive** : Le Cancer te rend protecteur·rice et nourricier·ère dans tes relations. Tu veux créer un cocon à deux. Cette sensibilité adoucit le besoin de dominer du Lion.

**Tensions possibles** : Les sautes d'humeur affectent tes partenariats. La sur-dépendance émotionnelle. Le besoin d'admiration peut créer de l'insécurité.

**Conseil clé** : Créer des partenariats où tu peux briller ET être vulnérable.""",
        'weekly_advice': {
            'week_1': "Identifie tes besoins émotionnels en relation.",
            'week_2': "Partage ta vulnérabilité avec un·e partenaire.",
            'week_3': "Nourris tes relations sans te perdre dedans.",
            'week_4': "Célèbre l'intimité profonde créée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Couple royal**

Double Lion sur la Maison 7 : les relations deviennent un terrain de performance mutuelle. Tu veux un·e partenaire aussi brillant·e que toi, avec qui créer un royaume à deux.

**Domaine activé** : Maison 7 — Tes partenariats cherchent la grandeur mutuelle. Tu veux que ta relation soit admirée, que vous brilliez ensemble. Le couple devient une création commune magnifique.

**Ton approche instinctive** : Tu ne fais rien à moitié en relation. Soit c'est passionné et grandiose, soit tu n'es pas intéressé·e. Cette intensité peut créer des légendes ou des drames.

**Tensions possibles** : Les conflits d'ego constants. Deux soleils peuvent se brûler mutuellement. Le besoin d'admiration de chacun peut créer de la compétition.

**Conseil clé** : Créer un partenariat où chacun brille sans éteindre l'autre.""",
        'weekly_advice': {
            'week_1': "Définis ce qu'un partenariat royal signifie pour toi.",
            'week_2': "Célèbre les succès de ton·ta partenaire autant que les tiens.",
            'week_3': "Partage la scène avec générosité et fierté.",
            'week_4': "Observe la grandeur créée ensemble."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfection à deux**

Ta Lune en Lion en Maison 7 veut des relations admiratives. Ton Ascendant Vierge tempère : tu veux un·e partenaire non seulement brillant·e, mais aussi compétent·e, utile, perfectionniste.

**Domaine activé** : Maison 7 — Tes partenariats cherchent l'excellence mutuelle. Tu veux améliorer et être amélioré·e. Les relations servent un but pratique autant qu'émotionnel.

**Ton approche instinctive** : La Vierge te rend analytique dans les relations. Tu vois les imperfections, tu veux optimiser. Cette exigence peut sublimer ou saboter ton bonheur relationnel.

**Tensions possibles** : L'autocritique et la critique du partenaire. Tu risques de ne jamais être satisfait·e. Le perfectionnisme paralyse l'intimité spontanée.

**Conseil clé** : Accepter que l'imperfection relationnelle fait partie de l'amour.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui compte vraiment dans une relation.",
            'week_2': "Apprécie ton·ta partenaire sans chercher à le·la améliorer.",
            'week_3': "Travaille sur toi sans projeter sur l'autre.",
            'week_4': "Célèbre les progrès relationnels accomplis."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie rayonnante**

Ta Lune en Lion en Maison 7 cherche l'admiration en relation. Ton Ascendant Balance, maître naturel de cette maison, amplifie : les partenariats deviennent centraux, élégants, harmonieux.

**Domaine activé** : Maison 7 — Tes relations sont ton terrain de jeu esthétique. Tu veux créer de la beauté à deux, briller dans l'harmonie. L'équilibre et l'admiration mutuelle sont essentiels.

**Ton approche instinctive** : La Balance te rend naturellement doué·e pour les partenariats. Tu cherches l'équilibre entre donner et recevoir. Cette recherche peut créer de l'harmonie ou de l'indécision.

**Tensions possibles** : L'indécision relationnelle par peur de choisir. Le besoin de plaire peut diluer ton authenticité. Trop de compromis éteint ta flamme.

**Conseil clé** : Créer des partenariats harmonieux qui respectent ton individualité.""",
        'weekly_advice': {
            'week_1': "Définis l'équilibre que tu cherches en relation.",
            'week_2': "Crée de la beauté partagée avec un·e partenaire.",
            'week_3': "Affirme tes besoins avec grâce mais fermeté.",
            'week_4': "Célèbre l'harmonie rayonnante créée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Fusion intense**

Ta Lune en Lion en Maison 7 veut des relations admiratives. Ton Ascendant Scorpion ajoute profondeur et intensité : tu veux des partenariats transformatifs, où vous vous connaissez jusqu'à l'âme.

**Domaine activé** : Maison 7 — Tes relations deviennent des terrains de transformation. Tu veux fusionner complètement, explorer les profondeurs, avoir un pouvoir partagé. Rien de superficiel.

**Ton approche instinctive** : Le Scorpion te pousse à tout donner en relation. Tu veux tout connaître de l'autre, tout partager. Cette intensité peut créer une fusion magique ou étouffante.

**Tensions possibles** : La jalousie et le besoin de contrôle. Les luttes de pouvoir dans le couple. L'obsession relationnelle peut consumer.

**Conseil clé** : Transformer ensemble tout en respectant l'individualité de chacun.""",
        'weekly_advice': {
            'week_1': "Regarde en face ce que tu cherches vraiment en relation.",
            'week_2': "Partage une vérité profonde avec ton·ta partenaire.",
            'week_3': "Lâche le contrôle pour vivre l'intimité vraie.",
            'week_4': "Observe comment la relation t'a transformé·e."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventure à deux**

Double feu sur la Maison 7 : ta Lune en Lion et ton Ascendant Sagittaire créent des partenariats aventureux, optimistes, expansifs. Tu veux explorer le monde à deux.

**Domaine activé** : Maison 7 — Tes relations cherchent la croissance et l'aventure. Tu veux un·e partenaire qui partage ta vision, qui ose avec toi, qui croit en vos possibilités infinies.

**Ton approche instinctive** : Le Sagittaire te rend optimiste et libre dans les relations. Tu veux de l'espace pour grandir. Cette indépendance peut enrichir ou fragiliser le lien.

**Tensions possibles** : La difficulté avec l'engagement à long terme. Le besoin de liberté peut être perçu comme fuite. Les promesses relationnelles non tenues.

**Conseil clé** : Créer des partenariats qui nourrissent la croissance mutuelle.""",
        'weekly_advice': {
            'week_1': "Définis la vision que tu veux partager en couple.",
            'week_2': "Lance une aventure commune avec ton·ta partenaire.",
            'week_3': "Équilibre liberté et engagement relationnel.",
            'week_4': "Célèbre l'expansion créée ensemble."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Partenariat solide**

Ta Lune en Lion en Maison 7 veut des relations admiratives. Ton Ascendant Capricorne ajoute sérieux et ambition : tu veux des partenariats qui durent, qui construisent quelque chose de grand ensemble.

**Domaine activé** : Maison 7 — Tes relations sont des projets à long terme. Tu veux un·e partenaire fiable, ambitieux·se, avec qui bâtir un empire. La stabilité et le respect mutuel comptent.

**Ton approche instinctive** : Le Capricorne te fait choisir tes partenaires stratégiquement. Tu construis des relations solides. Cette patience canalise l'impulsivité du Lion.

**Tensions possibles** : Le conflit entre besoin de passion (Lion) et pragmatisme (Capricorne). Les relations peuvent devenir trop sérieuses, manquer de chaleur.

**Conseil clé** : Construire des partenariats durables qui restent vivants et passionnés.""",
        'weekly_advice': {
            'week_1': "Définis ce que tu veux construire en relation.",
            'week_2': "Prends un engagement sérieux envers un partenariat.",
            'week_3': "Équilibre ambition et tendresse relationnelle.",
            'week_4': "Mesure les fondations solides posées ensemble."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Alliance unique**

Ta Lune en Lion en Maison 7 veut briller en relation. Ton Ascendant Verseau (opposé au Lion) crée une tension : tu veux des partenariats originaux, non-conventionnels, qui respectent ton individualité radicale.

**Domaine activé** : Maison 7 — Tes relations cherchent l'unicité et la liberté. Tu veux un·e partenaire qui te comprend dans ton originalité, qui partage tes idéaux avant-gardistes.

**Ton approche instinctive** : Le Verseau te rend détaché·e émotionnellement. Tu veux l'intimité intellectuelle plus qu'émotionnelle. Cette originalité peut fasciner ou créer de la distance.

**Tensions possibles** : Le conflit entre besoin d'admiration personnelle (Lion) et détachement (Verseau). La difficulté avec l'intimité émotionnelle profonde.

**Conseil clé** : Créer des partenariats uniques qui restent humainement chaleureux.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui rend tes relations vraiment uniques.",
            'week_2': "Expérimente un mode relationnel non-conventionnel.",
            'week_3': "Connecte ton besoin de liberté à l'intimité vraie.",
            'week_4': "Célèbre l'originalité de tes partenariats."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Amour inspiré**

Ta Lune en Lion en Maison 7 cherche l'admiration en relation. Ton Ascendant Poissons ajoute imagination et spiritualité : tu veux des partenariats qui transcendent, qui touchent l'âme.

**Domaine activé** : Maison 7 — Tes relations sont teintées de romantisme et d'idéalisme. Tu veux fusionner spirituellement, créer une connexion qui dépasse le matériel. L'amour devient mystique.

**Ton approche instinctive** : Le Poissons te rend empathique et fluide en relation. Tu t'adaptes, tu ressens, tu te dissous dans l'autre. Cette sensibilité peut créer de la magie ou de la confusion.

**Tensions possibles** : L'idéalisation du partenaire mène à la déception. Le manque de limites claires. Tu risques de te perdre dans la relation.

**Conseil clé** : Aimer de manière inspirée tout en gardant ton identité claire.""",
        'weekly_advice': {
            'week_1': "Identifie tes vrais besoins vs tes idéalisations.",
            'week_2': "Crée une connexion spirituelle avec ton·ta partenaire.",
            'week_3': "Maintiens des limites saines dans la fusion.",
            'week_4': "Célèbre l'amour transcendant créé."
        }
    },

    # ==================== MAISON 8 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Transformation courageuse**

Ta Lune en Lion active la Maison 8 : transformations profondes, ressources partagées, intimité. Avec l'Ascendant Bélier, tu affrontes tes zones d'ombre avec courage et volonté de renaître.

**Domaine activé** : Maison 8 — Les profondeurs t'appellent. Tu veux explorer tes peurs, transformer ce qui ne sert plus, renaître avec plus de pouvoir. L'intimité devient terrain de courage.

**Ton approche instinctive** : Double feu face aux ténèbres : tu attaques tes transformations de front. Tu n'as pas peur de regarder en face ce qui fait peur. Cette audace peut guérir ou brûler.

**Tensions possibles** : L'impulsivité dans les transformations profondes. Les confrontations intenses dans l'intimité. Le besoin de contrôler le processus de changement.

**Conseil clé** : Transformer avec courage tout en respectant le timing naturel.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit mourir pour que tu renaîsses.",
            'week_2': "Affronte une peur profonde avec courage.",
            'week_3': "Partage une intimité vraie sans te perdre.",
            'week_4': "Célèbre la transformation accomplie."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Richesse partagée**

Ta Lune en Lion en Maison 8 veut du pouvoir et de l'intimité. Ton Ascendant Taureau ajoute le focus sur les ressources partagées : tu veux construire une sécurité à deux, investir ensemble.

**Domaine activé** : Maison 8 — Les finances communes, héritages, investissements deviennent importants. Tu veux transformer ta relation à l'argent partagé, créer de la valeur durable à deux.

**Ton approche instinctive** : Le Taureau te rend pragmatique face aux ressources communes. Tu veux que les transformations soient tangibles. Cette stabilité ancre l'intensité du Lion.

**Tensions possibles** : Les conflits sur l'argent partagé. La possessivité sur les ressources communes. La résistance aux transformations nécessaires.

**Conseil clé** : Transformer les ressources partagées avec sagesse et générosité.""",
        'weekly_advice': {
            'week_1': "Clarifie ta relation aux ressources communes.",
            'week_2': "Investis dans quelque chose de durable à deux.",
            'week_3': "Lâche le contrôle sur ce qui ne t'appartient pas seul·e.",
            'week_4': "Savoure l'abondance partagée créée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Secrets révélés**

Ta Lune en Lion en Maison 8 veut explorer les profondeurs. Ton Ascendant Gémeaux ajoute curiosité intellectuelle : tu veux comprendre les mystères, parler de ce qui est caché.

**Domaine activé** : Maison 8 — Tu es attiré·e par les sujets tabous, les secrets, les connaissances ésotériques. La communication sur l'intimité devient importante. Explorer les zones d'ombre avec les mots.

**Ton approche instinctive** : Le Gémeaux te rend curieux·se des transformations. Tu veux analyser, comprendre, verbaliser. Cette approche peut éclairer ou intellectualiser trop.

**Tensions possibles** : La dispersion face aux profondeurs. Tu risques de rester en surface. La peur de vraiment plonger dans l'intensité émotionnelle.

**Conseil clé** : Explorer les profondeurs avec ton intelligence tout en restant présent·e émotionnellement.""",
        'weekly_advice': {
            'week_1': "Explore un sujet tabou ou mystérieux qui te fascine.",
            'week_2': "Parle d'intimité vraie avec quelqu'un de confiance.",
            'week_3': "Plonge au-delà de la compréhension intellectuelle.",
            'week_4': "Partage ce que tu as découvert dans les ombres."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Guérison émotionnelle**

Ta Lune en Lion en Maison 8 veut transformer en profondeur. Ton Ascendant Cancer ajoute sensibilité : tu veux guérir tes blessures émotionnelles, renaître émotionnellement plus fort·e.

**Domaine activé** : Maison 8 — Les transformations émotionnelles profondes sont au cœur. Tu explores tes traumas, tes peurs ancestrales, tes besoins de sécurité les plus profonds.

**Ton approche instinctive** : Le Cancer te rend vulnérable face aux profondeurs. Tu ressens intensément. Cette sensibilité peut faciliter la guérison ou te submerger.

**Tensions possibles** : Les sautes émotionnelles intenses. La peur de l'abandon resurgit. Tu risques de te noyer dans l'émotion plutôt que de transformer.

**Conseil clé** : Guérir tes blessures profondes avec douceur et courage.""",
        'weekly_advice': {
            'week_1': "Identifie une blessure émotionnelle à guérir.",
            'week_2': "Permets-toi de ressentir sans te perdre.",
            'week_3': "Cherche du soutien pour traverser l'intensité.",
            'week_4': "Célèbre la guérison émotionnelle accomplie."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Phénix royal**

Double Lion sur la Maison 8 : l'énergie de transformation est dramatique, puissante, centrée sur la renaissance. Tu veux mourir et renaître avec plus de pouvoir, plus de rayonnement.

**Domaine activé** : Maison 8 — Les transformations sont totales. Tu ne fais rien à moitié dans ta renaissance. Tu veux éliminer tout ce qui diminue ta grandeur, ressurgir plus fort·e.

**Ton approche instinctive** : Tu vis tes transformations avec intensité maximale. C'est toujours dramatique, puissant, cathartique. Cette intensité peut être libératrice ou épuisante.

**Tensions possibles** : L'ego face à la mort nécessaire. La fierté peut résister aux transformations. Les drames émotionnels intenses pendant les passages.

**Conseil clé** : Accepter que la vraie grandeur inclut la capacité de mourir et renaître.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit mourir pour ta renaissance.",
            'week_2': "Traverse la mort symbolique avec courage.",
            'week_3': "Laisse ton ego se dissoudre dans le processus.",
            'week_4': "Célèbre ta renaissance plus puissante."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Analyse des profondeurs**

Ta Lune en Lion en Maison 8 veut transformer avec panache. Ton Ascendant Vierge tempère : tu veux analyser, comprendre, perfectionner ton processus de transformation.

**Domaine activé** : Maison 8 — Tu abordes les transformations avec méthode. Tu veux comprendre les mécanismes, optimiser le processus, guérir avec précision.

**Ton approche instinctive** : La Vierge te fait analyser chaque aspect de tes zones d'ombre. Tu veux perfectionner ta guérison. Cette exigence peut éclairer ou te faire tourner en rond.

**Tensions possibles** : L'analyse peut bloquer le ressenti nécessaire. Tu risques de trop contrôler un processus qui demande le lâcher-prise. L'autocritique pendant la vulnérabilité.

**Conseil clé** : Utiliser ton intelligence pour comprendre tout en acceptant le chaos de la transformation.""",
        'weekly_advice': {
            'week_1': "Analyse objectivement ce qui doit changer.",
            'week_2': "Mets en place un processus de guérison structuré.",
            'week_3': "Lâche le contrôle mental, ressens vraiment.",
            'week_4': "Mesure tes progrès de transformation."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Transformation partagée**

Ta Lune en Lion en Maison 8 veut transformer en profondeur. Ton Ascendant Balance ajoute le focus relationnel : tu veux transformer à deux, équilibrer le pouvoir dans l'intimité.

**Domaine activé** : Maison 8 — Les transformations se font dans le contexte relationnel. Tu explores l'intimité profonde, les ressources partagées, le pouvoir mutuel avec grâce.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre même dans les profondeurs. Tu veux que les transformations soient justes, harmonieuses. Cette recherche peut adoucir ou diluer.

**Tensions possibles** : L'indécision face aux transformations nécessaires. Le besoin de plaire peut t'empêcher de plonger vraiment. Éviter l'intensité pour maintenir l'harmonie.

**Conseil clé** : Transformer avec grâce tout en acceptant que ça peut être chaotique.""",
        'weekly_advice': {
            'week_1': "Identifie les déséquilibres de pouvoir à transformer.",
            'week_2': "Plonge dans l'intimité vraie avec ton·ta partenaire.",
            'week_3': "Équilibre don et réception dans les profondeurs.",
            'week_4': "Célèbre la transformation harmonieuse accomplie."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Alchimie totale**

Ta Lune en Lion en Maison 8 veut transformer. Ton Ascendant Scorpion, maître naturel de cette maison, amplifie : les transformations sont profondes, radicales, complètes.

**Domaine activé** : Maison 8 — Tu es dans ton élément face aux profondeurs. La mort et la renaissance, les secrets, le pouvoir caché, l'intimité fusionnelle deviennent naturels.

**Ton approche instinctive** : Le Scorpion te donne le courage de tout affronter. Tu plonges dans les abysses sans peur. Cette intensité peut créer une transformation totale ou te consumer.

**Tensions possibles** : L'obsession des transformations. Le besoin de tout contrôler dans le chaos. L'intensité peut devenir destructrice.

**Conseil clé** : Transformer radicalement tout en respectant le timing naturel de la vie.""",
        'weekly_advice': {
            'week_1': "Regarde en face ce que tu as évité de voir.",
            'week_2': "Meurs symboliquement à ce qui ne sert plus.",
            'week_3': "Traverse les ténèbres avec confiance.",
            'week_4': "Observe ta renaissance complète."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Foi dans la renaissance**

Double feu sur la Maison 8 : ta Lune en Lion et ton Ascendant Sagittaire créent une transformation optimiste. Tu crois en ta capacité à renaître plus grand·e, plus sage.

**Domaine activé** : Maison 8 — Tes transformations sont guidées par la foi. Tu explores les profondeurs avec optimisme, tu cherches le sens dans les crises. La philosophie de la mort et renaissance.

**Ton approche instinctive** : Le Sagittaire te fait voir les possibilités même dans les ténèbres. Tu crois que chaque fin est un nouveau début. Cette foi peut te porter ou te rendre insouciant·e.

**Tensions possibles** : L'excès d'optimisme face aux vraies difficultés. Tu risques de fuir l'intensité par des promesses futures. Le manque d'ancrage dans le processus.

**Conseil clé** : Garder ta foi tout en respectant la gravité des transformations.""",
        'weekly_advice': {
            'week_1': "Trouve le sens dans ce qui doit mourir.",
            'week_2': "Traverse la transformation avec foi et courage.",
            'week_3': "Reste présent·e sans fuir vers le futur.",
            'week_4': "Célèbre la sagesse gagnée dans la renaissance."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Maîtrise du pouvoir**

Ta Lune en Lion en Maison 8 veut transformer avec panache. Ton Ascendant Capricorne ajoute structure : tu veux maîtriser ton pouvoir personnel, gérer les ressources partagées avec sagesse.

**Domaine activé** : Maison 8 — Les transformations sont stratégiques. Tu veux construire un pouvoir durable, gérer les héritages et ressources avec maturité. La mort et renaissance servent tes ambitions.

**Ton approche instinctive** : Le Capricorne te fait aborder les profondeurs avec pragmatisme. Tu structures tes transformations. Cette discipline canalise l'intensité du Lion.

**Tensions possibles** : La peur de perdre le contrôle dans les transformations. Le besoin de tout planifier face au chaos nécessaire. La rigidité émotionnelle.

**Conseil clé** : Construire un pouvoir solide tout en acceptant de lâcher prise quand nécessaire.""",
        'weekly_advice': {
            'week_1': "Définis le pouvoir que tu veux construire.",
            'week_2': "Prends le contrôle d'une situation de pouvoir.",
            'week_3': "Lâche ce qui ne sert plus tes ambitions.",
            'week_4': "Mesure le pouvoir personnel gagné."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolution intérieure**

Ta Lune en Lion en Maison 8 veut transformer. Ton Ascendant Verseau (opposé au Lion) crée une tension : tu veux révolutionner ta psyché, transformer radicalement, libérer.

**Domaine activé** : Maison 8 — Tes transformations défient les conventions. Tu explores des approches non-traditionnelles de guérison, de l'intimité, du pouvoir. L'innovation dans les profondeurs.

**Ton approche instinctive** : Le Verseau te fait penser différemment sur les transformations. Tu veux te libérer des patterns collectifs. Cette originalité peut révéler ou aliéner.

**Tensions possibles** : Le conflit entre besoin de pouvoir personnel (Lion) et détachement (Verseau). Le risque de fuir l'émotion par la rationalisation.

**Conseil clé** : Transformer radicalement tout en restant connecté·e à ton humanité.""",
        'weekly_advice': {
            'week_1': "Explore une approche non-conventionnelle de guérison.",
            'week_2': "Révolutionne un pattern profond qui te limite.",
            'week_3': "Connecte ta transformation à un enjeu collectif.",
            'week_4': "Célèbre ta libération intérieure."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 8, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution mystique**

Ta Lune en Lion en Maison 8 cherche la transformation. Ton Ascendant Poissons ajoute spiritualité : tu veux dissoudre ton ego, fusionner avec le divin, guérir spirituellement.

**Domaine activé** : Maison 8 — Tes transformations sont mystiques. Tu explores la mort de l'ego, la fusion spirituelle, la guérison par le pardon. L'invisible devient tangible.

**Ton approche instinctive** : Le Poissons te fait lâcher prise naturellement. Tu te laisses porter par le processus. Cette fluidité peut créer de la magie ou de la confusion.

**Tensions possibles** : Le manque de limites dans les transformations. Tu risques de te perdre complètement. La difficulté à ancrer tes guérisons spirituelles.

**Conseil clé** : Transformer spirituellement tout en gardant un ancrage terrestre.""",
        'weekly_advice': {
            'week_1': "Explore une pratique spirituelle de guérison.",
            'week_2': "Laisse ton ego se dissoudre dans le divin.",
            'week_3': "Pardonne et libère ce qui te retient.",
            'week_4': "Ancre tes guérisons mystiques dans le réel."
        }
    },

    # ==================== MAISON 9 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Conquérant inspiré**

Ta Lune en Lion en Maison 9 veut explorer, enseigner, inspirer à grande échelle. Ton Ascendant Bélier ajoute audace et spontanéité : tu pars à l'aventure sans plan, tu veux découvrir, créer un impact philosophique immédiat.

**Domaine activé** : Maison 9 — Ton besoin d'expansion passe par l'aventure créative. Tu veux voyager (physiquement ou mentalement), apprendre des enseignements qui nourrissent ton âme, partager ta vision du monde avec passion et grandeur.

**Ton approche instinctive** : Le Bélier te pousse à foncer vers l'inconnu sans hésitation. Tu veux être le premier à découvrir, à oser, à inspirer. Cette énergie pionnière dans le domaine des idées te rend magnétique mais parfois dogmatique.

**Tensions possibles** : L'impatience face aux doctrines établies peut créer des conflits idéologiques. Tu veux imposer ta vérité sans écouter. Le risque de manquer de profondeur par excès d'enthousiasme.

**Conseil clé** : Canaliser cette soif d'aventure vers une quête qui inspire authentiquement les autres.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans une exploration qui te passionne vraiment.",
            'week_2': "Partage ta vision du monde avec courage et authenticité.",
            'week_3': "Apprends quelque chose qui élargit ta perspective rapidement.",
            'week_4': "Célèbre les horizons que tu as ouverts ce mois-ci."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Sage majestueux**

Ta Lune en Lion en Maison 9 cherche l'expansion et la sagesse. Ton Ascendant Taureau ajoute stabilité et sensualité : tu veux explorer le monde avec dignité, construire une philosophie solide, enseigner avec présence calme.

**Domaine activé** : Maison 9 — Ton expansion passe par l'intégration profonde. Tu ne veux pas simplement voyager ou apprendre : tu veux ancrer la sagesse dans ton corps, ta vie quotidienne, tes valeurs durables. L'exploration devient art de vivre.

**Ton approche instinctive** : Le Taureau te fait avancer lentement mais sûrement dans ton expansion. Tu veux savourer chaque étape, construire une compréhension solide. Cette approche tempère l'impatience du Lion et donne du poids à ta sagesse.

**Tensions possibles** : La frustration face à la lenteur de l'expansion. Tu veux briller intellectuellement mais refuses de te précipiter. Le conflit entre besoin de confort et soif d'aventure peut te paralyser.

**Conseil clé** : Construire une philosophie de vie qui marie grandeur et simplicité, audace et stabilité.""",
        'weekly_advice': {
            'week_1': "Définis quelle sagesse tu veux vraiment intégrer à long terme.",
            'week_2': "Explore un enseignement qui résonne profondément en toi.",
            'week_3': "Ancre ta compréhension par des rituels ou pratiques régulières.",
            'week_4': "Savoure la richesse intérieure que tu as cultivée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Conteur inspiré**

Ta Lune en Lion en Maison 9 veut inspirer et enseigner. Ton Ascendant Gémeaux ajoute curiosité intellectuelle : tu explores mille idées, tu veux partager tes découvertes avec humour et intelligence, briller par ta culture.

**Domaine activé** : Maison 9 — Ton expansion passe par l'apprentissage multiple. Tu veux explorer différentes philosophies, voyager mentalement dans plusieurs directions, communiquer ta vision avec verve et créativité. Le monde des idées est ton terrain de jeu.

**Ton approche instinctive** : Le Gémeaux te rend agile intellectuellement. Tu captures des concepts rapidement, tu fais des connexions brillantes entre domaines variés. Cette polyvalence te permet de briller dans l'enseignement et l'écriture.

**Tensions possibles** : Disperser ton énergie dans trop de quêtes intellectuelles. Le risque de rester superficiel malgré ta brillance. L'inconstance peut nuire à ta crédibilité comme enseignant·e ou guide.

**Conseil clé** : Utiliser ta curiosité pour enrichir ta vision, pas pour t'éparpiller sans impact.""",
        'weekly_advice': {
            'week_1': "Explore plusieurs chemins philosophiques sans t'engager encore.",
            'week_2': "Communique tes découvertes avec clarté et enthousiasme.",
            'week_3': "Choisis 2-3 enseignements principaux à approfondir vraiment.",
            'week_4': "Partage ton savoir de manière captivante et inspirante."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Guide chaleureux**

Ta Lune en Lion en Maison 9 cherche à inspirer et enseigner. Ton Ascendant Cancer ajoute sensibilité émotionnelle : tu veux partager une sagesse qui nourrit les cœurs, créer une communauté autour de tes croyances, guider avec tendresse.

**Domaine activé** : Maison 9 — Ton expansion passe par la connexion émotionnelle. Tu ne veux pas simplement enseigner intellectuellement : tu veux toucher les âmes, créer un sentiment d'appartenance, inspirer par la compassion autant que par la grandeur.

**Ton approche instinctive** : Le Cancer te fait chercher une sagesse qui protège et nourrit. Tu veux créer un espace sécurisant pour explorer les grandes questions. Cette sensibilité adoucit la fierté du Lion et rend ton enseignement accessible.

**Tensions possibles** : L'oscillation entre besoin de briller intellectuellement et besoin de sécurité émotionnelle. Tu peux devenir protecteur·trice au point d'étouffer l'autonomie de ceux que tu guides.

**Conseil clé** : Inspirer à travers l'authenticité émotionnelle et la générosité du cœur.""",
        'weekly_advice': {
            'week_1': "Explore une sagesse qui résonne émotionnellement en toi.",
            'week_2': "Crée un espace d'apprentissage chaleureux et inclusif.",
            'week_3': "Partage tes croyances en respectant la sensibilité des autres.",
            'week_4': "Célèbre la communauté d'âmes que tu as nourrie."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Prophète solaire**

Double Lion en Maison 9 : tu es le guide suprême, l'enseignant charismatique, le voyageur qui inspire. Ce mois-ci, ta quête de sagesse est théâtrale, généreuse, absolue. Tu veux illuminer le monde avec ta vision.

**Domaine activé** : Maison 9 — Ton expansion est pure expression créative. Tu cherches une philosophie qui te permet de briller, un enseignement que tu peux incarner majestueusement. Le voyage devient spectacle inspirant.

**Ton approche instinctive** : Double Lion, tu n'as aucun doute sur la valeur de ta vision. Tu enseignes avec autorité naturelle, tu inspires par ta seule présence. Cette confiance magnétique attire des disciples mais peut sembler arrogante.

**Tensions possibles** : L'ego surdimensionné dans le domaine des croyances. Tu risques de confondre ta vérité personnelle avec la Vérité absolue. Le besoin d'être admiré·e peut nuire à ta crédibilité intellectuelle.

**Conseil clé** : Utiliser ta lumière pour inspirer le meilleur chez les autres, pas pour dominer.""",
        'weekly_advice': {
            'week_1': "Définis la vision du monde que tu veux incarner pleinement.",
            'week_2': "Partage ton enseignement avec générosité et authenticité.",
            'week_3': "Écoute aussi les vérités des autres pour enrichir ta sagesse.",
            'week_4': "Célèbre l'impact inspirant que tu as créé."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Maître précis**

Ta Lune en Lion en Maison 9 veut inspirer et enseigner. Ton Ascendant Vierge ajoute rigueur et perfectionnisme : tu veux briller par la qualité de ton enseignement, offrir une sagesse pratique et utile, perfectionner ta méthode.

**Domaine activé** : Maison 9 — Ton expansion passe par l'excellence technique. Tu cherches une philosophie applicable, un enseignement structuré, une sagesse qui sert vraiment. Le détail devient sacré dans ta quête de sens.

**Ton approche instinctive** : La Vierge te fait analyser chaque aspect de ta quête intellectuelle. Tu veux tout comprendre parfaitement avant d'enseigner. Cette exigence tempère la grandiloquence du Lion et donne de la crédibilité.

**Tensions possibles** : Le perfectionnisme peut t'empêcher de partager ta sagesse par peur de l'imperfection. Tu peux devenir critique envers les enseignements imparfaits, perdant la joie de l'exploration.

**Conseil clé** : Allier excellence technique et générosité inspirante dans ton enseignement.""",
        'weekly_advice': {
            'week_1': "Étudie un sujet avec profondeur et rigueur méthodique.",
            'week_2': "Structure ton savoir pour le rendre utile aux autres.",
            'week_3': "Ose partager même si ce n'est pas encore parfait.",
            'week_4': "Célèbre la qualité du travail intellectuel accompli."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomate inspiré**

Ta Lune en Lion en Maison 9 cherche à inspirer et enseigner. Ton Ascendant Balance ajoute harmonie et justice : tu veux partager une sagesse équilibrée, créer des ponts entre cultures, enseigner avec grâce et élégance.

**Domaine activé** : Maison 9 — Ton expansion passe par la relation et la beauté. Tu cherches une philosophie qui unit plutôt que divise, un enseignement esthétique, une sagesse qui valorise l'équilibre et la coopération internationale.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre dans tes explorations intellectuelles. Tu veux considérer tous les points de vue avant de former ta vision. Cette diplomatie tempère le dogmatisme potentiel du Lion.

**Tensions possibles** : L'indécision face aux grandes questions philosophiques. Tu peux tellement chercher l'équilibre que tu perds ta propre voix. Le besoin d'être apprécié·e peut diluer ton message.

**Conseil clé** : Trouver une vision personnelle forte tout en restant ouvert·e aux perspectives diverses.""",
        'weekly_advice': {
            'week_1': "Explore des philosophies qui valorisent l'harmonie et la justice.",
            'week_2': "Crée des connexions entre différentes traditions de sagesse.",
            'week_3': "Partage ton enseignement avec grâce et respect des différences.",
            'week_4': "Célèbre les ponts que tu as construits entre les mondes."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Mystique puissant**

Ta Lune en Lion en Maison 9 veut inspirer et enseigner. Ton Ascendant Scorpion ajoute intensité et profondeur : tu cherches une sagesse transformatrice, un enseignement qui change les vies radicalement, une vérité qui dérange.

**Domaine activé** : Maison 9 — Ton expansion passe par la confrontation avec les tabous philosophiques. Tu veux explorer les mystères ultimes, enseigner des vérités cachées, transformer la conscience collective par ta vision radicale.

**Ton approche instinctive** : Le Scorpion te fait plonger dans les profondeurs de la sagesse. Tu ne te satisfais pas des réponses superficielles. Cette intensité peut révéler des vérités puissantes mais aussi aliéner ceux qui ne sont pas prêts.

**Tensions possibles** : Le dogmatisme intense. Tu peux devenir fanatique de ta vérité, utilisant ton charisme pour manipuler plutôt qu'inspirer. Le refus de compromis peut limiter ton impact.

**Conseil clé** : Utiliser ton pouvoir de transformation intellectuelle avec responsabilité éthique.""",
        'weekly_advice': {
            'week_1': "Plonge dans un enseignement profond qui transforme ta vision.",
            'week_2': "Confronte une croyance limitante avec courage et honnêteté.",
            'week_3': "Partage ta vérité de manière puissante mais respectueuse.",
            'week_4': "Célèbre la transformation intellectuelle que tu as vécue."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventurier royal**

Ta Lune en Lion en Maison 9 cherche l'expansion et l'inspiration. Ton Ascendant Sagittaire (domicile de la Maison 9) amplifie cette énergie : tu es l'explorateur absolu, le philosophe optimiste, le voyageur qui inspire par son enthousiasme contagieux.

**Domaine activé** : Maison 9 — L'expansion est ton élément naturel ce mois-ci. Tu veux tout voir, tout comprendre, tout enseigner. Ta soif de sagesse est illimitée, ton enthousiasme pour l'aventure intellectuelle est débordant.

**Ton approche instinctive** : Le Sagittaire te fait voir grand naturellement. Tu crois en tes visions, tu inspires par ton optimisme sincère. Cette foi inébranlable dans le voyage de l'esprit te rend magnétique.

**Tensions possibles** : L'excès de confiance peut te faire surestimer tes connaissances. Tu risques de promettre plus que tu ne peux tenir, de partir dans trop de directions à la fois.

**Conseil clé** : Canaliser cet enthousiasme débordant vers une quête qui a un impact durable.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans la plus grande aventure intellectuelle possible.",
            'week_2': "Partage ton enthousiasme de manière contagieuse et généreuse.",
            'week_3': "Approfondis une direction plutôt que te disperser partout.",
            'week_4': "Célèbre l'expansion de conscience que tu as vécue."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Autorité sage**

Ta Lune en Lion en Maison 9 veut inspirer et enseigner. Ton Ascendant Capricorne ajoute structure et ambition : tu cherches une sagesse qui construit un héritage, un enseignement reconnu institutionnellement, une autorité intellectuelle durable.

**Domaine activé** : Maison 9 — Ton expansion passe par la discipline et la reconnaissance. Tu ne veux pas simplement explorer : tu veux devenir une référence, obtenir des diplômes, construire une réputation solide comme penseur·se ou enseignant·e.

**Ton approche instinctive** : Le Capricorne te fait gravir méthodiquement la montagne de la sagesse. Tu acceptes l'effort nécessaire pour maîtriser vraiment un domaine. Cette persévérance tempère l'impatience du Lion.

**Tensions possibles** : Le conflit entre besoin de reconnaissance immédiate (Lion) et patience requise (Capricorne). Tu peux devenir trop rigide dans tes croyances, perdant la spontanéité créative.

**Conseil clé** : Construire une autorité intellectuelle basée sur l'excellence réelle et la générosité.""",
        'weekly_advice': {
            'week_1': "Définis l'héritage intellectuel que tu veux laisser.",
            'week_2': "Travaille avec discipline sur un projet d'enseignement ambitieux.",
            'week_3': "Cherche une reconnaissance institutionnelle pour ta sagesse.",
            'week_4': "Célèbre les fondations solides que tu as posées."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Visionnaire rebelle**

Ta Lune en Lion en Maison 9 veut inspirer. Ton Ascendant Verseau (opposé au Lion) crée tension : tu cherches une sagesse révolutionnaire, un enseignement qui libère les esprits, une vision qui brise les dogmes établis.

**Domaine activé** : Maison 9 — Ton expansion défie les conventions intellectuelles. Tu explores des philosophies avant-gardistes, tu veux enseigner différemment, créer une communauté d'esprits libres autour de ta vision unique.

**Ton approche instinctive** : Le Verseau te fait penser radicalement différemment. Tu rejettes les autorités intellectuelles traditionnelles. Cette originalité peut être brillante mais aussi aliénante si tu refuses toute structure.

**Tensions possibles** : Le conflit entre besoin d'être reconnu·e comme autorité (Lion) et rejet de toute hiérarchie (Verseau). Le risque de devenir dogmatique dans ton anti-dogmatisme.

**Conseil clé** : Révolutionner la sagesse collective tout en respectant l'héritage des anciens.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie non-conventionnelle qui te passionne.",
            'week_2': "Partage une vision révolutionnaire avec courage et clarté.",
            'week_3': "Crée une communauté d'esprits libres autour de tes idées.",
            'week_4': "Célèbre l'impact libérateur de ton enseignement."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 9, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Mystique inspiré**

Ta Lune en Lion en Maison 9 cherche à inspirer et enseigner. Ton Ascendant Poissons ajoute spiritualité et compassion universelle : tu veux partager une sagesse qui transcende l'ego, enseigner par l'exemple de ta foi, inspirer spirituellement.

**Domaine activé** : Maison 9 — Ton expansion passe par la dissolution des frontières. Tu explores les mystères spirituels, tu cherches une sagesse qui unit toute l'humanité, tu veux enseigner la compassion et le pardon à grande échelle.

**Ton approche instinctive** : Le Poissons te fait enseigner par osmose plutôt que par autorité. Tu inspires par ta présence mystique, ta capacité à voir le divin en tout. Cette fluidité adoucit la fierté du Lion.

**Tensions possibles** : Le manque de structure dans ton enseignement. Tu risques de te perdre dans l'abstraction spirituelle, de confondre inspiration divine et ego personnel. La difficulté à établir des limites claires.

**Conseil clé** : Inspirer spirituellement tout en restant ancré·e dans la réalité pratique.""",
        'weekly_advice': {
            'week_1': "Explore une pratique spirituelle qui nourrit ton âme profondément.",
            'week_2': "Partage ta foi avec humilité et compassion universelle.",
            'week_3': "Laisse le divin te guider dans ton enseignement.",
            'week_4': "Ancre tes visions mystiques dans un message clair."
        }
    },

    # ==================== MAISON 10 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Leader combatif**

Ta Lune en Lion en Maison 10 veut briller publiquement, être reconnu·e professionnellement. Ton Ascendant Bélier ajoute audace guerrière : tu veux conquérir le sommet avec courage, imposer ta marque, diriger avec autorité naturelle.

**Domaine activé** : Maison 10 — Ta carrière et ta réputation publique demandent l'expression de ton leadership. Tu veux être vu·e comme pionnier·ère, créateur·trice visionnaire, leader charismatique. L'ambition est pure flamme.

**Ton approche instinctive** : Le Bélier te fait foncer vers le succès sans calcul stratégique. Tu veux gagner maintenant, être premier·ère, imposer ta vision. Cette spontanéité peut créer des percées rapides mais aussi des conflits hiérarchiques.

**Tensions possibles** : L'impatience face aux structures établies. Tu veux révolutionner ton domaine mais peux manquer de diplomatie. Le risque de brûler des ponts professionnels par excès d'audace.

**Conseil clé** : Canaliser cette énergie guerrière vers un leadership qui inspire plutôt qu'intimide.""",
        'weekly_advice': {
            'week_1': "Prends une initiative audacieuse dans ta carrière.",
            'week_2': "Affirme ton leadership avec courage et authenticité.",
            'week_3': "Montre ta valeur unique sans écraser la concurrence.",
            'week_4': "Célèbre les batailles professionnelles que tu as gagnées."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Bâtisseur prestigieux**

Ta Lune en Lion en Maison 10 cherche reconnaissance professionnelle et prestige. Ton Ascendant Taureau ajoute stabilité et persévérance : tu veux construire une réputation solide, durable, basée sur la qualité réelle de ton travail.

**Domaine activé** : Maison 10 — Ta carrière demande excellence et patience. Tu ne veux pas simplement briller temporairement : tu veux bâtir un héritage professionnel qui dure, une marque de qualité reconnue, un statut indéniable.

**Ton approche instinctive** : Le Taureau te fait gravir la montagne lentement mais sûrement. Tu refuses les raccourcis qui compromettraient ta réputation. Cette approche tempère l'impatience du Lion et construit une autorité solide.

**Tensions possibles** : La frustration face à la lenteur du succès. Tu veux briller maintenant mais refuses de te précipiter. Le conflit entre ambition et besoin de sécurité peut te paralyser.

**Conseil clé** : Construire un succès professionnel basé sur la substance réelle, pas l'apparence.""",
        'weekly_advice': {
            'week_1': "Définis le statut professionnel que tu veux vraiment atteindre.",
            'week_2': "Investis dans la qualité de ton travail, pas les apparences.",
            'week_3': "Avance à ton rythme vers l'excellence, sans te comparer.",
            'week_4': "Savoure la solidité de ta réputation naissante."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Communicateur star**

Ta Lune en Lion en Maison 10 veut briller professionnellement. Ton Ascendant Gémeaux ajoute agilité intellectuelle : tu veux être reconnu·e pour ta brillance communicative, ta polyvalence, ton intelligence médiatique.

**Domaine activé** : Maison 10 — Ta réputation publique passe par ta capacité à communiquer avec charisme. Tu veux être vu·e comme expert·e polyvalent·e, créateur·trice de contenu inspirant, porte-parole charismatique de ton domaine.

**Ton approche instinctive** : Le Gémeaux te rend adaptable dans ta quête de reconnaissance. Tu sais comment te présenter différemment selon ton audience. Cette agilité te permet de briller sur plusieurs plateformes.

**Tensions possibles** : Disperser ton énergie professionnelle dans trop de directions. Le risque de devenir superficiel·le malgré ta brillance. L'inconstance peut nuire à ta crédibilité à long terme.

**Conseil clé** : Utiliser ta polyvalence pour enrichir ta marque, pas pour te disperser sans impact.""",
        'weekly_advice': {
            'week_1': "Explore plusieurs façons de briller professionnellement.",
            'week_2': "Communique ta valeur unique avec clarté et charme.",
            'week_3': "Choisis 2-3 domaines principaux pour ta réputation.",
            'week_4': "Partage ton expertise de manière captivante et mémorable."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Leader nourricier**

Ta Lune en Lion en Maison 10 cherche reconnaissance professionnelle. Ton Ascendant Cancer ajoute sensibilité et protection : tu veux briller en prenant soin des autres, créer une carrière qui nourrit, diriger avec cœur et générosité.

**Domaine activé** : Maison 10 — Ta réputation publique passe par ta capacité à créer un impact émotionnel. Tu veux être reconnu·e non seulement pour ta compétence, mais pour ton humanité, ta bienveillance, ton leadership maternel/paternel.

**Ton approche instinctive** : Le Cancer te fait bâtir ta carrière sur les relations authentiques. Tu veux créer une famille professionnelle, un espace où les gens se sentent valorisés. Cette sensibilité humanise ton ambition.

**Tensions possibles** : L'oscillation entre besoin de reconnaissance publique et besoin de sécurité émotionnelle. Tu peux devenir trop protecteur·trice envers ton équipe, limitant leur autonomie.

**Conseil clé** : Construire une carrière basée sur l'authenticité émotionnelle et la générosité.""",
        'weekly_advice': {
            'week_1': "Montre ton humanité dans ta vie professionnelle.",
            'week_2': "Crée un environnement de travail chaleureux et inspirant.",
            'week_3': "Dirige avec cœur tout en maintenant des limites saines.",
            'week_4': "Célèbre l'impact émotionnel de ton leadership."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Monarque absolu**

Double Lion en Maison 10 : tu es l'incarnation du succès royal, du leader né pour briller publiquement. Ce mois-ci, ton ambition est pure expression créative. Tu veux régner sur ton domaine avec grandeur et générosité.

**Domaine activé** : Maison 10 — Ta carrière est ton royaume. Tu cherches non seulement la réussite mais la gloire, non seulement le respect mais l'admiration. Ta réputation doit refléter ta majesté naturelle.

**Ton approche instinctive** : Double Lion, tu incarnes naturellement l'autorité. Tu n'as aucun doute sur ta légitimité à diriger. Cette confiance magnétique attire les opportunités mais peut sembler arrogante.

**Tensions possibles** : L'ego surdimensionné dans le domaine professionnel. Tu risques d'écraser les autres par ton besoin de briller. Le refus de collaborer si tu n'es pas au centre peut limiter ton succès.

**Conseil clé** : Utiliser ta lumière naturelle pour élever les autres, pas pour les dominer.""",
        'weekly_advice': {
            'week_1': "Définis la vision professionnelle que tu veux incarner.",
            'week_2': "Prends ta place de leader avec authenticité et générosité.",
            'week_3': "Inspire ton équipe par l'exemple de ton excellence.",
            'week_4': "Célèbre le royaume professionnel que tu as construit."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfectionniste reconnu**

Ta Lune en Lion en Maison 10 veut briller professionnellement. Ton Ascendant Vierge ajoute exigence et service : tu veux être reconnu·e pour l'excellence de ton travail, la précision de ton expertise, l'utilité réelle de ton œuvre.

**Domaine activé** : Maison 10 — Ta réputation publique passe par la qualité irréprochable de ton travail. Tu ne veux pas simplement être célèbre : tu veux être respecté·e pour ton professionnalisme, ta compétence technique, ton intégrité.

**Ton approche instinctive** : La Vierge te fait perfectionner chaque aspect de ta carrière. Tu analyses, tu améliores, tu sers avec excellence. Cette exigence tempère la grandiloquence du Lion et construit une autorité crédible.

**Tensions possibles** : Le perfectionnisme peut t'empêcher de te mettre en avant par peur d'imperfection. Tu peux devenir critique envers toi-même et les autres, perdant la générosité du Lion.

**Conseil clé** : Allier excellence technique et générosité inspirante dans ton leadership.""",
        'weekly_advice': {
            'week_1': "Perfectionne un aspect clé de ton expertise professionnelle.",
            'week_2': "Offre un service d'excellence qui impressionne vraiment.",
            'week_3': "Ose te montrer même si ce n'est pas encore parfait.",
            'week_4': "Célèbre la qualité irréprochable de ton travail."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Leader élégant**

Ta Lune en Lion en Maison 10 cherche reconnaissance professionnelle. Ton Ascendant Balance ajoute diplomatie et esthétique : tu veux briller avec grâce, diriger avec équité, construire une réputation d'élégance et de justice.

**Domaine activé** : Maison 10 — Ta carrière passe par les relations harmonieuses et le sens de la beauté. Tu veux être reconnu·e non seulement pour ta compétence, mais pour ton charme, ta capacité à créer des alliances, ton leadership équilibré.

**Ton approche instinctive** : La Balance te fait bâtir ta réputation sur la collaboration. Tu cherches à briller avec les autres plutôt que seul·e. Cette approche tempère l'individualisme du Lion et crée des opportunités par le réseau.

**Tensions possibles** : L'indécision face aux choix de carrière. Tu veux plaire à tout le monde, ce qui peut diluer ton impact. Le besoin d'être apprécié·e peut te faire sacrifier ton authenticité.

**Conseil clé** : Construire un succès professionnel basé sur l'équilibre entre ambition et collaboration.""",
        'weekly_advice': {
            'week_1': "Crée des alliances stratégiques qui servent ton ambition.",
            'week_2': "Montre ton leadership avec grâce et diplomatie.",
            'week_3': "Défends tes intérêts tout en restant équitable envers les autres.",
            'week_4': "Célèbre les partenariats professionnels fructueux."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Stratège puissant**

Ta Lune en Lion en Maison 10 veut reconnaissance professionnelle. Ton Ascendant Scorpion ajoute intensité et pouvoir stratégique : tu veux dominer ton domaine, transformer ton industrie, exercer une influence profonde et durable.

**Domaine activé** : Maison 10 — Ta carrière est un jeu de pouvoir que tu es déterminé·e à gagner. Tu cherches non seulement le succès mais le contrôle, non seulement la reconnaissance mais la capacité de transformer les règles du jeu.

**Ton approche instinctive** : Le Scorpion te fait jouer le long terme. Tu investigues les faiblesses du système, tu construis des alliances stratégiques, tu attends le moment parfait pour frapper. Cette intensité peut intimider ou fasciner.

**Tensions possibles** : Le besoin de contrôle peut créer des conflits de pouvoir. Tu risques de devenir manipulateur·trice dans ta quête de domination. La méfiance excessive peut t'isoler professionnellement.

**Conseil clé** : Utiliser ton pouvoir stratégique pour créer un impact positif transformateur.""",
        'weekly_advice': {
            'week_1': "Analyse les dynamiques de pouvoir dans ton domaine.",
            'week_2': "Construis une stratégie à long terme pour ta domination.",
            'week_3': "Transforme une structure obsolète avec audace et intégrité.",
            'week_4': "Célèbre le pouvoir réel que tu as acquis."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Visionnaire inspirant**

Ta Lune en Lion en Maison 10 cherche reconnaissance professionnelle. Ton Ascendant Sagittaire ajoute vision et expansion : tu veux briller à l'international, inspirer par tes idées audacieuses, créer un impact qui dépasse les frontières.

**Domaine activé** : Maison 10 — Ta carrière passe par ta capacité à voir grand et inspirer les foules. Tu veux être reconnu·e comme visionnaire, leader d'opinion, pionnier·ère qui ouvre de nouveaux territoires dans ton domaine.

**Ton approche instinctive** : Le Sagittaire te fait viser toujours plus haut. Tu refuses les limites conventionnelles, tu crois en ta capacité à réussir à grande échelle. Cet optimisme contagieux attire les opportunités.

**Tensions possibles** : L'excès de confiance peut te faire surestimer tes capacités. Tu risques de promettre plus que tu ne peux tenir, de partir dans trop de directions à la fois.

**Conseil clé** : Canaliser cet optimisme débordant vers une vision professionnelle qui a un impact durable.""",
        'weekly_advice': {
            'week_1': "Définis la plus grande vision professionnelle possible pour toi.",
            'week_2': "Partage tes idées audacieuses avec confiance et enthousiasme.",
            'week_3': "Concentre ton énergie sur un projet d'envergure international.",
            'week_4': "Célèbre l'expansion de ton influence professionnelle."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Empereur stratège**

Ta Lune en Lion en Maison 10 veut briller professionnellement. Ton Ascendant Capricorne (maître de la Maison 10) amplifie cette énergie : tu es l'incarnation de l'ambition royale structurée, du leader qui construit un empire durable.

**Domaine activé** : Maison 10 — C'est ton élément naturel ce mois-ci. Tu combines la créativité charismatique du Lion avec la discipline stratégique du Capricorne. Ta capacité à bâtir un succès authentique et durable est maximale.

**Ton approche instinctive** : Le Capricorne te donne la patience et la stratégie nécessaires pour concrétiser l'ambition du Lion. Tu acceptes l'effort, tu respectes les hiérarchies utiles, tu construis pierre par pierre ton royaume professionnel.

**Tensions possibles** : Le conflit entre besoin de reconnaissance immédiate (Lion) et nécessité de patience stratégique (Capricorne). Tu peux devenir trop rigide, perdant la spontanéité créative.

**Conseil clé** : Construire un empire professionnel basé sur l'excellence, la persévérance et la générosité.""",
        'weekly_advice': {
            'week_1': "Définis l'héritage professionnel que tu veux laisser.",
            'week_2': "Travaille avec discipline sur ton projet de carrière le plus ambitieux.",
            'week_3': "Gravis méthodiquement les échelons vers le sommet.",
            'week_4': "Célèbre les fondations solides de ton empire naissant."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Rebelle lumineux**

Ta Lune en Lion en Maison 10 veut reconnaissance. Ton Ascendant Verseau (opposé au Lion) crée tension : tu cherches à briller en défiant les conventions, à être célèbre pour ton originalité radicale, à révolutionner ton domaine.

**Domaine activé** : Maison 10 — Ta carrière doit exprimer ton unicité absolue. Tu refuses de suivre les chemins établis vers le succès. Tu veux créer ton propre modèle, être reconnu·e comme innovateur·trice qui change les règles du jeu.

**Ton approche instinctive** : Le Verseau te fait rejeter les hiérarchies traditionnelles. Tu veux réussir sans compromettre ta liberté ou ton authenticité. Cette originalité peut être brillante mais aussi aliénante.

**Tensions possibles** : Le conflit entre besoin d'admiration personnelle (Lion) et idéaux collectifs (Verseau). Tu peux te saboter par excès de rébellion, refusant les opportunités conventionnelles.

**Conseil clé** : Révolutionner ton domaine tout en acceptant de construire une réputation solide.""",
        'weekly_advice': {
            'week_1': "Définis comment tu veux briller différemment dans ton domaine.",
            'week_2': "Ose une approche professionnelle radicalement originale.",
            'week_3': "Construis une communauté autour de ta vision unique.",
            'week_4': "Célèbre l'impact révolutionnaire de ta carrière."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 10, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Artiste inspiré**

Ta Lune en Lion en Maison 10 cherche reconnaissance professionnelle. Ton Ascendant Poissons ajoute sensibilité artistique et spiritualité : tu veux briller en inspirant spirituellement, créer une carrière qui touche les âmes, être reconnu·e pour ta compassion.

**Domaine activé** : Maison 10 — Ta réputation publique passe par ta capacité à créer de la beauté et de l'inspiration spirituelle. Tu veux être vu·e comme artiste visionnaire, guérisseur·se charismatique, leader qui unit par l'amour universel.

**Ton approche instinctive** : Le Poissons te fait bâtir ta carrière sur l'intuition et l'inspiration divine. Tu te laisses guider par quelque chose de plus grand que toi. Cette fluidité adoucit l'ego du Lion et crée une présence mystique.

**Tensions possibles** : Le manque de structure dans ton ascension professionnelle. Tu risques de te perdre dans les rêves sans concrétiser. La difficulté à négocier ta valeur par excès d'humilité ou de confusion.

**Conseil clé** : Construire une carrière inspirante tout en restant ancré·e dans la réalité pratique.""",
        'weekly_advice': {
            'week_1': "Explore comment ta créativité peut inspirer professionnellement.",
            'week_2': "Laisse ton intuition te guider vers les bonnes opportunités.",
            'week_3': "Crée quelque chose de beau qui élève la conscience collective.",
            'week_4': "Ancre ton succès spirituel dans une structure concrète."
        }
    },

    # ==================== MAISON 11 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Chef de meute**

Ta Lune en Lion en Maison 11 veut briller socialement, inspirer un groupe, créer un impact collectif. Ton Ascendant Bélier ajoute énergie guerrière : tu veux rallier les troupes, diriger une révolution, être le leader charismatique d'une cause audacieuse.

**Domaine activé** : Maison 11 — Tes amitiés et tes projets collectifs demandent ton leadership. Tu cherches à créer ou rejoindre une communauté où tu peux briller, inspirer, mobiliser les énergies vers un objectif commun ambitieux.

**Ton approche instinctive** : Le Bélier te fait foncer dans les projets de groupe avec enthousiasme. Tu veux initier des mouvements, pas suivre. Cette audace peut rallier des alliés fidèles mais aussi créer des conflits d'ego.

**Tensions possibles** : Le besoin de dominer le groupe peut t'isoler. Tu veux être le héros mais peux oublier que la force collective dépasse l'individu. L'impatience face aux processus démocratiques.

**Conseil clé** : Canaliser cette énergie guerrière pour inspirer un collectif, pas pour le dominer.""",
        'weekly_advice': {
            'week_1': "Prends l'initiative de lancer un projet de groupe ambitieux.",
            'week_2': "Rallie tes amis autour d'une cause qui te passionne.",
            'week_3': "Dirige avec courage tout en respectant la contribution de chacun.",
            'week_4': "Célèbre les victoires collectives que tu as inspirées."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Mécène généreux**

Ta Lune en Lion en Maison 11 cherche reconnaissance sociale et impact collectif. Ton Ascendant Taureau ajoute stabilité et générosité matérielle : tu veux construire une communauté solide, investir dans des amitiés durables, créer de la valeur partagée.

**Domaine activé** : Maison 11 — Tes réseaux sociaux et projets collectifs demandent qualité et substance. Tu ne veux pas simplement être populaire : tu veux bâtir des amitiés authentiques, soutenir des causes avec ressources réelles.

**Ton approche instinctive** : Le Taureau te fait investir patiemment dans tes relations sociales. Tu offres stabilité, générosité tangible, fidélité. Cette approche construit une réputation solide de personne sur qui on peut compter.

**Tensions possibles** : La possessivité envers tes amis. Tu peux devenir jaloux·se si le groupe évolue sans toi. La résistance au changement dans tes cercles sociaux peut te faire manquer de nouvelles opportunités.

**Conseil clé** : Construire une communauté basée sur la générosité authentique et la valeur durable.""",
        'weekly_advice': {
            'week_1': "Investis dans les amitiés qui comptent vraiment pour toi.",
            'week_2': "Offre un soutien matériel ou financier à une cause collective.",
            'week_3': "Construis des traditions qui solidifient ton groupe.",
            'week_4': "Savoure la richesse de tes connexions authentiques."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Connecteur brillant**

Ta Lune en Lion en Maison 11 veut briller socialement. Ton Ascendant Gémeaux ajoute agilité sociale : tu veux être au centre de multiples réseaux, connecter les gens, briller par ta capacité à créer des ponts entre communautés diverses.

**Domaine activé** : Maison 11 — Tes amitiés sont multiples et variées. Tu cherches à briller dans différents groupes, à être l'intermédiaire indispensable, à créer de la valeur par ta capacité à communiquer et connecter.

**Ton approche instinctive** : Le Gémeaux te rend socialement adaptable. Tu sais comment parler à tout le monde, comment animer un groupe, comment rendre chaque interaction intéressante. Cette polyvalence te rend populaire.

**Tensions possibles** : Disperser ton énergie sociale dans trop de directions. Le risque de relations superficielles malgré ta popularité. L'inconstance peut faire que tes amis ne se sentent pas prioritaires.

**Conseil clé** : Utiliser ta brillance sociale pour créer des connexions significatives, pas seulement nombreuses.""",
        'weekly_advice': {
            'week_1': "Explore différents cercles sociaux sans t'engager encore.",
            'week_2': "Connecte des personnes qui peuvent s'entraider mutuellement.",
            'week_3': "Choisis 2-3 communautés où investir vraiment ton énergie.",
            'week_4': "Partage une idée collective qui inspire plusieurs groupes."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Parent du groupe**

Ta Lune en Lion en Maison 11 cherche reconnaissance sociale. Ton Ascendant Cancer ajoute sensibilité nourricière : tu veux créer une famille d'âmes, être le cœur émotionnel du groupe, briller en prenant soin de ta communauté.

**Domaine activé** : Maison 11 — Tes amitiés sont des liens familiaux choisis. Tu cherches à créer un espace sécurisant où chacun peut s'exprimer, un collectif basé sur la vulnérabilité partagée et le soutien mutuel.

**Ton approche instinctive** : Le Cancer te fait protéger ton groupe avec férocité. Tu nourris émotionnellement tes amis, tu te souviens de leurs besoins, tu crées des rituels qui cimentent le lien. Cette générosité te rend indispensable.

**Tensions possibles** : La sur-protection du groupe peut étouffer l'autonomie individuelle. Tu peux devenir émotionnellement dépendant·e de la validation sociale. Les sautes d'humeur affectent la cohésion collective.

**Conseil clé** : Nourrir ta communauté tout en respectant l'indépendance de chacun.""",
        'weekly_advice': {
            'week_1': "Crée un espace émotionnellement sécurisant pour ton groupe.",
            'week_2': "Prends soin des besoins émotionnels de tes amis proches.",
            'week_3': "Établis des limites saines entre ta vie et celle du groupe.",
            'week_4': "Célèbre la famille d'âmes que tu as nourrie."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Star sociale**

Double Lion en Maison 11 : tu es le centre magnétique de ton cercle social, l'ami qui inspire, le leader naturel de tout groupe que tu rejoins. Ce mois-ci, ta popularité atteint des sommets et tu rayonnes socialement.

**Domaine activé** : Maison 11 — Tes amitiés et projets collectifs sont une extension de ta royauté personnelle. Tu cherches à briller à travers ton réseau, à inspirer un mouvement, à créer un impact qui dépasse l'individuel.

**Ton approche instinctive** : Double Lion, tu n'as aucun doute sur ta valeur sociale. Tu attires naturellement l'attention et l'admiration du groupe. Cette confiance magnétique fait de toi un leader d'opinion naturel.

**Tensions possibles** : Le besoin excessif d'être au centre peut aliéner certains amis. Tu risques de transformer chaque projet collectif en one-man-show. La difficulté à accepter de ne pas toujours briller le plus.

**Conseil clé** : Utiliser ta lumière sociale pour élever le collectif, pas pour éclipser les autres.""",
        'weekly_advice': {
            'week_1': "Définis le rôle social que tu veux incarner dans ton groupe.",
            'week_2': "Inspire ton cercle par l'exemple de ta générosité.",
            'week_3': "Crée un projet collectif où chacun peut briller aussi.",
            'week_4': "Célèbre les succès du groupe autant que les tiens."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Organisateur précieux**

Ta Lune en Lion en Maison 11 veut briller socialement. Ton Ascendant Vierge ajoute service et organisation : tu veux être reconnu·e pour ton utilité au groupe, briller en rendant le collectif plus efficace, servir avec excellence.

**Domaine activé** : Maison 11 — Tes amitiés et projets collectifs bénéficient de ton souci du détail. Tu veux être l'organisateur·trice indispensable, celui·celle qui fait fonctionner les rouages du groupe avec précision.

**Ton approche instinctive** : La Vierge te fait analyser les besoins du collectif. Tu identifies ce qui manque, tu améliores les processus, tu sers avec humilité. Cette efficacité te rend précieux·se même si moins visible.

**Tensions possibles** : Le perfectionnisme peut te faire critiquer le groupe excessivement. Tu peux te frustrer si ton travail d'organisation n'est pas assez reconnu. Le risque de te surcharger en servant les autres.

**Conseil clé** : Servir le collectif avec excellence tout en acceptant la reconnaissance pour ton rôle.""",
        'weekly_advice': {
            'week_1': "Identifie comment tu peux vraiment améliorer ton groupe.",
            'week_2': "Organise un projet collectif avec soin et précision.",
            'week_3': "Ose demander reconnaissance pour ton travail d'organisation.",
            'week_4': "Célèbre l'impact concret de ton service au collectif."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmoniseur charismatique**

Ta Lune en Lion en Maison 11 cherche reconnaissance sociale. Ton Ascendant Balance ajoute diplomatie et sens de la justice : tu veux briller en créant l'harmonie dans le groupe, être le médiateur apprécié, inspirer par ton équité.

**Domaine activé** : Maison 11 — Tes amitiés passent par ta capacité à créer des ponts. Tu cherches à briller socialement en étant celui·celle qui unit plutôt que divise, qui crée des alliances équitables, qui rend le groupe plus beau.

**Ton approche instinctive** : La Balance te fait chercher l'équilibre dans toutes tes relations sociales. Tu veux que chacun se sente valorisé. Cette approche te rend populaire et crée un capital social précieux.

**Tensions possibles** : L'indécision face aux conflits de groupe. Tu peux sacrifier tes propres convictions pour maintenir l'harmonie. Le besoin d'être apprécié·e peut te faire perdre ton authenticité.

**Conseil clé** : Créer l'harmonie sociale tout en restant fidèle à tes valeurs personnelles.""",
        'weekly_advice': {
            'week_1': "Identifie les tensions dans ton groupe et médite dessus.",
            'week_2': "Crée une alliance ou un partenariat collectif équitable.",
            'week_3': "Défends tes convictions tout en restant diplomatique.",
            'week_4': "Célèbre l'harmonie que tu as apportée au collectif."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Influenceur intense**

Ta Lune en Lion en Maison 11 veut reconnaissance sociale. Ton Ascendant Scorpion ajoute profondeur stratégique : tu cherches à exercer une influence réelle sur ton groupe, transformer collectivement, créer des liens intenses et durables.

**Domaine activé** : Maison 11 — Tes amitiés sont des alliances de pouvoir. Tu cherches non seulement à briller socialement, mais à transformer la conscience du groupe, à exercer une influence profonde sur les objectifs collectifs.

**Ton approche instinctive** : Le Scorpion te fait investiguer les dynamiques cachées du groupe. Tu identifies qui a vraiment du pouvoir, tu construis des alliances stratégiques. Cette intensité peut fasciner ou intimider.

**Tensions possibles** : Le besoin de contrôler le groupe. Tu peux devenir manipulateur·trice dans ta quête d'influence sociale. La méfiance excessive peut t'isoler malgré ton magnétisme.

**Conseil clé** : Utiliser ton influence sociale pour transformer positivement le collectif, pas pour dominer.""",
        'weekly_advice': {
            'week_1': "Analyse les dynamiques de pouvoir dans ton cercle social.",
            'week_2': "Construis une alliance stratégique avec des alliés clés.",
            'week_3': "Transforme une dynamique de groupe toxique avec courage.",
            'week_4': "Célèbre l'évolution profonde de ta communauté."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Visionnaire social**

Ta Lune en Lion en Maison 11 cherche reconnaissance sociale. Ton Ascendant Sagittaire ajoute optimisme et vision expansive : tu veux inspirer ton groupe vers des objectifs ambitieux, créer une communauté internationale, briller par ta foi contagieuse.

**Domaine activé** : Maison 11 — Tes amitiés dépassent les frontières. Tu cherches à créer ou rejoindre un mouvement qui a un impact à grande échelle, à briller en inspirant un collectif vers une vision audacieuse et optimiste.

**Ton approche instinctive** : Le Sagittaire te fait voir grand pour le groupe. Tu crois en la capacité collective à accomplir l'impossible. Cet enthousiasme contagieux attire des alliés passionnés mais peut manquer de réalisme.

**Tensions possibles** : L'excès de confiance dans les projets collectifs. Tu risques de promettre plus que le groupe ne peut tenir. La tendance à partir dans trop de directions peut disperser l'énergie collective.

**Conseil clé** : Inspirer le collectif vers une vision ambitieuse mais réalisable ensemble.""",
        'weekly_advice': {
            'week_1': "Définis la vision la plus inspirante pour ton groupe.",
            'week_2': "Partage ton optimisme de manière contagieuse et généreuse.",
            'week_3': "Concentre l'énergie collective sur un objectif principal.",
            'week_4': "Célèbre l'expansion de votre impact collectif."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Architecte social**

Ta Lune en Lion en Maison 11 veut briller socialement. Ton Ascendant Capricorne ajoute structure et ambition collective : tu cherches à construire une organisation solide, à créer une réputation sociale durable, à diriger avec autorité reconnue.

**Domaine activé** : Maison 11 — Tes amitiés et projets collectifs demandent professionnalisme. Tu ne veux pas simplement être populaire : tu veux bâtir une structure sociale qui dure, un réseau professionnel prestigieux, un héritage collectif.

**Ton approche instinctive** : Le Capricorne te fait aborder les relations sociales stratégiquement. Tu investis dans les bonnes connexions, tu respectes les hiérarchies utiles, tu construis patiemment ta position dans le groupe.

**Tensions possibles** : Le conflit entre besoin de reconnaissance immédiate (Lion) et patience stratégique (Capricorne). Tu peux devenir trop calculateur·trice dans tes amitiés, perdant l'authenticité.

**Conseil clé** : Construire une influence sociale basée sur l'excellence, la persévérance et la générosité.""",
        'weekly_advice': {
            'week_1': "Définis l'héritage social que tu veux laisser dans ton groupe.",
            'week_2': "Structure un projet collectif avec professionnalisme.",
            'week_3': "Gravis les échelons sociaux avec patience et intégrité.",
            'week_4': "Célèbre les fondations solides de ton réseau."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolutionnaire lumineux**

Ta Lune en Lion en Maison 11 veut reconnaissance. Ton Ascendant Verseau (maître de la Maison 11) amplifie cette énergie sociale mais crée tension : tu veux briller individuellement tout en servant le collectif, être unique mais appartenir.

**Domaine activé** : Maison 11 — C'est ton élément naturel ce mois-ci, mais avec paradoxe. Tu cherches à créer une communauté de rebelles, à être célèbre pour ton originalité radicale, à révolutionner les structures sociales établies.

**Ton approche instinctive** : Le Verseau te fait rejeter les normes sociales tout en voulant être admiré·e. Tu veux inspirer une révolution collective, créer une communauté basée sur la liberté individuelle absolue de chacun.

**Tensions possibles** : Le conflit entre besoin d'admiration personnelle (Lion) et idéaux d'égalité (Verseau). Tu peux te saboter en refusant de prendre le leadership nécessaire au groupe.

**Conseil clé** : Inspirer une révolution collective tout en acceptant ton rôle de leader lumineux.""",
        'weekly_advice': {
            'week_1': "Définis comment tu veux révolutionner ton cercle social.",
            'week_2': "Ose exprimer ta vision radicale avec courage et clarté.",
            'week_3': "Crée une communauté qui valorise l'unicité de chacun.",
            'week_4': "Célèbre la liberté collective que tu as inspirée."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 11, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Inspirateur mystique**

Ta Lune en Lion en Maison 11 cherche reconnaissance sociale. Ton Ascendant Poissons ajoute compassion universelle : tu veux inspirer spirituellement ton groupe, créer une communauté basée sur l'amour inconditionnel, briller par ta générosité d'âme.

**Domaine activé** : Maison 11 — Tes amitiés transcendent l'ego. Tu cherches à créer une famille d'âmes unies par la foi, la compassion, la créativité partagée. Le groupe devient espace de guérison et d'inspiration mutuelle.

**Ton approche instinctive** : Le Poissons te fait dissoudre les frontières dans le groupe. Tu te donnes complètement, tu ressens les émotions collectives, tu inspires par ta présence mystique. Cette fluidité peut créer de la magie.

**Tensions possibles** : Le manque de limites dans tes relations sociales. Tu risques de te perdre dans le collectif, de te sacrifier excessivement. La difficulté à dire non peut t'épuiser émotionnellement.

**Conseil clé** : Inspirer spirituellement ta communauté tout en préservant ton énergie individuelle.""",
        'weekly_advice': {
            'week_1': "Explore comment ta spiritualité peut nourrir ton groupe.",
            'week_2': "Crée un espace collectif de guérison et d'inspiration.",
            'week_3': "Établis des limites saines malgré ta générosité d'âme.",
            'week_4': "Célèbre la connexion spirituelle de ta communauté."
        }
    },

    # ==================== MAISON 12 ====================

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Héros caché**

Ta Lune en Lion en Maison 12 veut briller mais dans l'ombre, exprimer sa créativité en secret, guérir son ego. Ton Ascendant Bélier ajoute tension : tu veux agir courageusement mais l'univers te demande d'attendre, de te retirer, de combattre des démons intérieurs.

**Domaine activé** : Maison 12 — Ton besoin de reconnaissance entre en hibernation. Ce mois-ci, tu explores ton inconscient, tes peurs de ne pas être assez, ton rapport au sacrifice créatif. Le théâtre se joue en toi seul·e.

**Ton approche instinctive** : Le Bélier te pousse à vouloir agir immédiatement même dans le retrait. Tu te bats contre l'isolement, tu refuses la passivité. Cette résistance peut créer de la frustration ou des percées spirituelles.

**Tensions possibles** : La colère face à l'invisibilité temporaire. Tu peux te sentir emprisonné·e, frustré·e de ne pas pouvoir briller. Le risque d'actions impulsives autodestructrices pour échapper au silence.

**Conseil clé** : Accepter ce temps de retrait comme préparation à un rayonnement futur plus authentique.""",
        'weekly_advice': {
            'week_1': "Retire-toi volontairement pour explorer ton monde intérieur.",
            'week_2': "Combats tes peurs inconscientes avec courage et honnêteté.",
            'week_3': "Crée en secret sans chercher la validation externe.",
            'week_4': "Prépare-toi à ressortir de l'ombre plus fort·e et authentique."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Ermite créatif**

Ta Lune en Lion en Maison 12 cherche à briller dans l'invisible. Ton Ascendant Taureau ajoute besoin de sécurité matérielle : tu veux créer en retrait, te ressourcer dans le silence, guérir ton rapport à la valeur personnelle.

**Domaine activé** : Maison 12 — Ton ego créatif demande repos. Ce mois-ci, tu explores ce qui te nourrit vraiment au-delà de la reconnaissance externe. Tu découvres une créativité plus authentique quand personne ne regarde.

**Ton approche instinctive** : Le Taureau te fait accepter le retrait avec plus de grâce. Tu peux savourer le silence, créer lentement sans pression. Cette patience transforme ton rapport au besoin d'admiration.

**Tensions possibles** : La peur de perdre ta valeur si tu n'es pas visible. Tu peux t'accrocher à la sécurité matérielle par peur de l'inconnu spirituel. La résistance au lâcher-prise nécessaire.

**Conseil clé** : Utiliser ce temps caché pour construire une créativité plus solide et authentique.""",
        'weekly_advice': {
            'week_1': "Crée un espace sacré pour ton retrait créatif.",
            'week_2': "Explore ce qui te nourrit vraiment au-delà du regard des autres.",
            'week_3': "Lâche prise sur le besoin de validation externe.",
            'week_4': "Savoure la richesse intérieure que tu as cultivée en secret."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Conteur d'ombres**

Ta Lune en Lion en Maison 12 veut exprimer sa créativité dans l'ombre. Ton Ascendant Gémeaux ajoute curiosité intellectuelle : tu explores ton inconscient à travers l'écriture, les rêves, le dialogue intérieur. L'esprit visite les profondeurs.

**Domaine activé** : Maison 12 — Tes pensées explorent l'invisible. Ce mois-ci, tu découvres les histoires cachées de ton ego, tu communiques avec ton âme, tu documentes tes processus intérieurs sans les partager.

**Ton approche instinctive** : Le Gémeaux te fait analyser ton retrait intellectuellement. Tu journalises, tu cherches à comprendre tes patterns. Cette curiosité peut éclairer l'ombre ou te faire éviter l'émotion brute.

**Tensions possibles** : La tentation de partager prématurément tes découvertes intérieures. Tu peux intellectualiser tes émotions pour éviter leur profondeur. L'agitation mentale peut perturber le silence nécessaire.

**Conseil clé** : Utiliser ta curiosité pour explorer l'ombre sans fuir dans la distraction mentale.""",
        'weekly_advice': {
            'week_1': "Documente tes rêves et pensées inconscientes dans un journal secret.",
            'week_2': "Explore tes patterns mentaux cachés avec curiosité bienveillante.",
            'week_3': "Résiste à l'envie de partager tes découvertes trop tôt.",
            'week_4': "Intègre en silence ce que tu as appris sur toi-même."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Âme nourricière**

Ta Lune en Lion en Maison 12 cherche à briller dans l'invisible. Ton Ascendant Cancer amplifie l'émotion : tu plonges dans un océan de sensibilité, tu guéris des blessures émotionnelles profondes, ton cœur s'ouvre dans le silence.

**Domaine activé** : Maison 12 — Ton monde émotionnel demande attention. Ce mois-ci, tu explores les racines de ton besoin d'amour et de reconnaissance. Tu découvres comment te nourrir émotionnellement sans dépendre du regard des autres.

**Ton approche instinctive** : Le Cancer te fait ressentir profondément le retrait. Tu peux pleurer, te souvenir, pardonner. Cette sensibilité te permet une guérison émotionnelle authentique si tu acceptes la vulnérabilité.

**Tensions possibles** : Le risque de te noyer dans la mélancolie. Tu peux devenir trop isolé·e émotionnellement, coupé·e de tout soutien. Les blessures d'abandon peuvent ressurgir intensément.

**Conseil clé** : Utiliser ce temps caché pour guérir ton cœur tout en gardant quelques connexions sûres.""",
        'weekly_advice': {
            'week_1': "Plonge dans tes émotions les plus profondes sans jugement.",
            'week_2': "Pardonne-toi pour tes besoins d'amour et de reconnaissance.",
            'week_3': "Nourris ton enfant intérieur avec tendresse et patience.",
            'week_4': "Émerge de ton cocon émotionnel plus guéri·e et entier·ère."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Roi en exil**

Double Lion en Maison 12 : tu es le monarque dans l'ombre, le créateur qui doit temporairement renoncer à la gloire. Ce mois-ci, ton ego magnifique entre en chrysalide. C'est une mort nécessaire avant une renaissance plus authentique.

**Domaine activé** : Maison 12 — Ton identité créative se dissout. Ce mois-ci, tu explores qui tu es quand personne ne te regarde, quand tu ne peux pas briller. C'est douloureux mais transformateur pour ton rapport à la reconnaissance.

**Ton approche instinctive** : Double Lion, tu résistes naturellement à l'invisibilité. Tu peux te sentir en prison, frustré·e, en colère. Mais cette résistance elle-même révèle ce qui doit être guéri dans ton ego.

**Tensions possibles** : La dépression face à l'absence de reconnaissance. Tu peux te sentir complètement perdu·e sans la validation externe. Le risque d'autodestruction ou de retrait total.

**Conseil clé** : Accepter cette mort temporaire de l'ego comme préparation à une lumière plus puissante.""",
        'weekly_advice': {
            'week_1': "Accepte que ce mois-ci ne soit pas ton moment de briller.",
            'week_2': "Explore qui tu es vraiment au-delà de l'admiration des autres.",
            'week_3': "Crée pour le simple plaisir, sans attendre de reconnaissance.",
            'week_4': "Prépare-toi à renaître avec une authenticité plus profonde."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Serviteur humble**

Ta Lune en Lion en Maison 12 veut briller mais doit se retirer. Ton Ascendant Vierge ajoute service et humilité : ce mois-ci, tu découvres la joie de créer sans reconnaissance, de servir dans l'anonymat, de perfectionner ton art en secret.

**Domaine activé** : Maison 12 — Ton perfectionnisme se tourne vers l'intérieur. Ce mois-ci, tu améliores ton âme, tu nettoies tes patterns inconscients, tu sers une cause plus grande que ton ego. Le travail spirituel devient pratique quotidienne.

**Ton approche instinctive** : La Vierge te fait accepter le retrait comme opportunité de perfectionnement. Tu peux analyser tes patterns, améliorer ta discipline spirituelle, servir discrètement. Cette humilité guérit l'ego du Lion.

**Tensions possibles** : Le perfectionnisme spirituel peut devenir obsessionnel. Tu risques de te critiquer excessivement pendant ce retrait. La difficulté à accepter l'imperfection du processus de guérison.

**Conseil clé** : Utiliser ce temps caché pour perfectionner ton art tout en acceptant l'imperfection humaine.""",
        'weekly_advice': {
            'week_1': "Analyse tes patterns inconscients avec bienveillance et rigueur.",
            'week_2': "Sers une cause en secret, sans attendre de reconnaissance.",
            'week_3': "Perfectionne une pratique spirituelle ou créative dans l'ombre.",
            'week_4': "Célèbre le travail intérieur invisible que tu as accompli."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Artiste solitaire**

Ta Lune en Lion en Maison 12 cherche à créer dans l'ombre. Ton Ascendant Balance ajoute besoin d'harmonie : ce mois-ci, tu explores la beauté intérieure, tu crées de l'art pour ton âme seule, tu trouves l'équilibre loin du regard des autres.

**Domaine activé** : Maison 12 — Tes relations se dissolvent temporairement au profit de la relation avec toi-même. Ce mois-ci, tu découvres ton sens de la beauté et de la justice au-delà de l'approbation sociale.

**Ton approche instinctive** : La Balance te fait chercher l'harmonie même dans le retrait. Tu veux que ton monde intérieur soit beau, équilibré, juste. Cette quête esthétique adoucit la solitude.

**Tensions possibles** : La difficulté à rester seul·e sans partenaire ou public. Tu peux te sentir incomplet·ète sans le miroir des autres. L'indécision face à ce que tu es vraiment sans validation externe.

**Conseil clé** : Créer de la beauté pour toi-même, découvrir ton propre sens esthétique authentique.""",
        'weekly_advice': {
            'week_1': "Retire-toi pour explorer ce qui est beau pour toi seul·e.",
            'week_2': "Crée de l'art sans jamais le montrer à personne.",
            'week_3': "Trouve ton équilibre intérieur loin du regard des autres.",
            'week_4': "Émerge avec une esthétique plus authentiquement tienne."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Alchimiste d'ombre**

Ta Lune en Lion en Maison 12 veut transformer dans l'invisible. Ton Ascendant Scorpion amplifie l'intensité : ce mois-ci, tu plonges dans les profondeurs les plus sombres de ton ego, tu confrontes ton désir de pouvoir, tu transmutes ton orgueil.

**Domaine activé** : Maison 12 — Ton pouvoir créatif entre en transformation radicale. Ce mois-ci, tu meurs et renais spirituellement. Tu explores les tabous de ton ego, les secrets que tu caches même à toi-même.

**Ton approche instinctive** : Le Scorpion te fait plonger sans peur dans l'ombre. Tu ne fuis pas la douleur du retrait : tu l'utilises pour te transformer. Cette intensité peut créer une guérison profonde ou une crise spirituelle.

**Tensions possibles** : Le risque de te perdre complètement dans l'ombre. Tu peux devenir obsédé·e par tes démons intérieurs. La tentation de manipuler spirituellement pour regagner un sentiment de pouvoir.

**Conseil clé** : Utiliser ce temps d'alchimie intérieure pour transmuter l'ego en lumière authentique.""",
        'weekly_advice': {
            'week_1': "Confronte tes désirs de pouvoir et de reconnaissance les plus sombres.",
            'week_2': "Meurs symboliquement à ton ancien ego créatif.",
            'week_3': "Laisse l'alchimie spirituelle te transformer profondément.",
            'week_4': "Renais avec une puissance créative plus authentique et guérie."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Pèlerin intérieur**

Ta Lune en Lion en Maison 12 cherche à briller dans l'invisible. Ton Ascendant Sagittaire ajoute quête spirituelle : ce mois-ci, tu voyages intérieurement, tu explores ta foi quand personne ne regarde, tu cherches une vérité plus grande que ton ego.

**Domaine activé** : Maison 12 — Ton besoin d'expansion se tourne vers l'infini intérieur. Ce mois-ci, tu découvres que le plus grand voyage est celui de l'âme. Ta quête de sens transcende le besoin de reconnaissance.

**Ton approche instinctive** : Le Sagittaire te fait voir le retrait comme aventure spirituelle. Tu explores avec optimisme ton monde intérieur. Cette foi te permet de traverser l'ombre avec espoir et curiosité.

**Tensions possibles** : Le risque de fuir dans l'abstraction spirituelle pour éviter l'émotion brute. Tu peux minimiser la douleur du retrait par excès d'optimisme. La difficulté à rester ancré·e dans le processus.

**Conseil clé** : Voyager intérieurement avec foi tout en restant honnête sur la difficulté du chemin.""",
        'weekly_advice': {
            'week_1': "Entreprends un pèlerinage spirituel intérieur sans destination précise.",
            'week_2': "Explore ta foi quand personne ne peut la valider ou l'admirer.",
            'week_3': "Découvre une vérité qui transcende ton besoin de reconnaissance.",
            'week_4': "Émerge avec une sagesse plus humble et authentique."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Architecte silencieux**

Ta Lune en Lion en Maison 12 veut créer dans l'ombre. Ton Ascendant Capricorne ajoute discipline : ce mois-ci, tu construis patiemment ton monde intérieur, tu travailles sur ton âme avec la même rigueur que sur ta carrière, tu structures ton inconscient.

**Domaine activé** : Maison 12 — Ton ambition se tourne vers la maîtrise spirituelle. Ce mois-ci, tu acceptes que le vrai succès passe par le travail invisible sur soi. Tu gravis la montagne intérieure avec persévérance.

**Ton approche instinctive** : Le Capricorne te fait accepter le retrait comme étape nécessaire. Tu comprends que certaines fondations doivent être posées en secret. Cette patience transforme ton rapport à la reconnaissance.

**Tensions possibles** : Le conflit entre besoin de résultats visibles (Lion + Capricorne) et nature invisible du travail spirituel. Tu peux devenir trop rigide dans ta pratique spirituelle.

**Conseil clé** : Construire patiemment ton monde intérieur comme fondation d'un rayonnement futur authentique.""",
        'weekly_advice': {
            'week_1': "Structure une pratique spirituelle quotidienne rigoureuse.",
            'week_2': "Travaille sur ton âme avec la discipline d'un artisan.",
            'week_3': "Accepte que certaines fondations se posent dans l'ombre.",
            'week_4': "Célèbre le travail invisible que tu as accompli sur toi-même."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Génie isolé**

Ta Lune en Lion en Maison 12 cherche à briller dans l'invisible. Ton Ascendant Verseau (opposé au Lion) crée paradoxe : tu dois te retirer du collectif pour découvrir ton unicité véritable, te libérer des attentes sociales dans la solitude.

**Domaine activé** : Maison 12 — Ton individualité se dissout et se reforme. Ce mois-ci, tu découvres que ta vraie originalité émerge quand tu arrêtes de performer pour les autres. L'innovation naît du silence intérieur.

**Ton approche instinctive** : Le Verseau te fait voir le retrait comme libération. Tu utilises cette solitude pour déconstruire les conditionnements sociaux. Cette rébellion intérieure peut être brillante mais déstabilisante.

**Tensions possibles** : L'isolement peut devenir aliénation. Tu risques de te couper complètement de l'humanité dans ta quête d'unicité. La rébellion contre le besoin de reconnaissance peut devenir rigide.

**Conseil clé** : Utiliser ce temps d'isolement pour découvrir ton génie authentique au-delà des attentes.""",
        'weekly_advice': {
            'week_1': "Retire-toi complètement des attentes sociales et collectives.",
            'week_2': "Explore qui tu es vraiment quand personne ne définit ton unicité.",
            'week_3': "Libère-toi des patterns de performance conditionnés.",
            'week_4': "Prépare-toi à émerger avec une originalité plus authentique."
        }
    },

    {
        'moon_sign': 'Leo', 'moon_house': 12, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Artiste mystique**

Ta Lune en Lion en Maison 12 veut créer dans l'invisible. Ton Ascendant Poissons amplifie la spiritualité : ce mois-ci, tu dissous complètement ton ego créatif dans le divin, tu deviens canal d'inspiration universelle, tu crées par abandon total.

**Domaine activé** : Maison 12 — Ton identité créative fusionne avec l'infini. Ce mois-ci, tu découvres que ta plus grande œuvre est la dissolution de la séparation entre toi et le Tout. L'art devient prière silencieuse.

**Ton approche instinctive** : Le Poissons te fait lâcher prise naturellement. Tu te laisses porter par le courant spirituel, tu crées par inspiration divine plutôt que volonté personnelle. Cette fluidité peut créer de la magie pure.

**Tensions possibles** : Le risque de te perdre complètement, de ne plus pouvoir revenir. Tu peux confondre ego spirituel et véritable dissolution. La difficulté à maintenir toute structure ou frontière.

**Conseil clé** : Fusionner avec le divin tout en gardant un fil qui te ramène à ton humanité.""",
        'weekly_advice': {
            'week_1': "Abandonne complètement ton besoin de contrôle créatif.",
            'week_2': "Laisse l'inspiration divine créer à travers toi sans ego.",
            'week_3': "Dissous les frontières entre ton art et le sacré.",
            'week_4': "Reviens doucement à ton humanité, enrichi·e de l'infini."
        }
    },

]

if __name__ == "__main__":
    print(f"[*] Batch complet: Leo - {len(BATCH)} interprétations")
    asyncio.run(insert_batch(BATCH))
    print(f"[✓] Leo terminé - 144/1728 (8.3%)")
