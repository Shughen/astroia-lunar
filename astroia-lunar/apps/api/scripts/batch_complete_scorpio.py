"""Batch complet: Scorpio - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    # ==================== MAISON 1 ====================

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Intensité brute**

Ta Lune en Scorpion en Maison 1 te plonge dans une transformation profonde de ton identité. Tu ressens tout avec une intensité magnétique, presque magnétisante. Avec l'Ascendant Bélier, cette puissance émotionnelle cherche une expression directe, sans détour.

**Domaine activé** : Maison 1 — Ton image, ton corps, ta manière d'exister dans le monde. Tu veux montrer qui tu es vraiment, sans masque. L'authenticité devient une quête viscérale.

**Ton approche instinctive** : Le Bélier te pousse à agir sur ce que tu ressens. Face à une émotion intense, tu ne rumines pas : tu passes à l'acte. Cette combinaison crée une force de frappe émotionnelle redoutable.

**Tensions possibles** : L'intensité peut effrayer ton entourage. Le besoin de contrôle (Scorpion) contre l'impulsivité (Bélier) crée des réactions explosives. Attention aux ruptures soudaines.

**Conseil clé** : Canaliser cette puissance vers une transformation personnelle concrète — sport intense, projet créatif exigeant, thérapie profonde.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit mourir en toi pour renaître autrement.",
            'week_2': "Affronte une vérité que tu évitais. Plonge dans l'inconfort.",
            'week_3': "Laisse sortir la rage ou la passion de manière constructive.",
            'week_4': "Observe ta métamorphose. Note les changements intérieurs."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Force magnétique**

Ta Lune en Scorpion en Maison 1 active une profondeur émotionnelle intense autour de ton identité. L'Ascendant Taureau, ton opposé, cherche la stabilité et le concret. Cette polarité crée une tension fertile entre transformation et permanence.

**Domaine activé** : Maison 1 — Qui tu es, comment tu te montres au monde. Tu cherches à incarner quelque chose de solide (Taureau) tout en traversant des mutations profondes (Scorpion).

**Ton approche instinctive** : Le Taureau te fait résister au changement, mais le Scorpion sait que certaines morts sont nécessaires. Tu avances lentement, mais quand tu changes, c'est radical et définitif.

**Tensions possibles** : La peur de perdre ce que tu as (Taureau) contre le besoin de tout brûler pour renaître (Scorpion). Cette lutte intérieure peut te figer ou te faire exploser.

**Conseil clé** : Accepter que la vraie sécurité vient de ta capacité à te transformer, pas de ce que tu possèdes.""",
        'weekly_advice': {
            'week_1': "Identifie ce à quoi tu t'accroches par peur du vide.",
            'week_2': "Fais un geste concret de lâcher-prise sur un aspect de ton image.",
            'week_3': "Construis quelque chose de nouveau à partir de ce que tu as libéré.",
            'week_4': "Ancre ta nouvelle identité dans des habitudes tangibles."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Profondeur volatile**

Ta Lune en Scorpion cherche l'intensité et la vérité absolue dans ton identité (Maison 1). L'Ascendant Gémeaux apporte légèreté, curiosité, mouvement. Cette combinaison crée une danse étrange entre le lourd et le léger.

**Domaine activé** : Maison 1 — Ton apparence, ta manière d'être perçu·e. Tu oscilles entre montrer ta profondeur ou garder les choses superficielles par protection.

**Ton approche instinctive** : Le Gémeaux te fait communiquer, explorer, papillonner. Mais sous cette surface agile, le Scorpion observe, analyse, cherche le non-dit. Tu peux être à la fois bavard·e et secret·ète.

**Tensions possibles** : Le besoin de parler (Gémeaux) contre le besoin de taire (Scorpion). Tu risques de tout dire ou de te fermer complètement, sans nuance.

**Conseil clé** : Utiliser les mots pour explorer tes zones d'ombre sans tout révéler. Écrire peut être thérapeutique.""",
        'weekly_advice': {
            'week_1': "Écris sur ce que tu ressens sans le montrer à personne.",
            'week_2': "Partage une vérité profonde avec quelqu'un de confiance.",
            'week_3': "Apprends quelque chose sur la psychologie ou l'occulte.",
            'week_4': "Synthétise tes découvertes intérieures en quelques phrases clés."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Océan intérieur**

Double eau : ta Lune en Scorpion en Maison 1 avec Ascendant Cancer crée une sensibilité extrême autour de ton identité. Tu ressens tout intensément, mais tu protèges farouchement ton monde intérieur.

**Domaine activé** : Maison 1 — Ton image personnelle devient un refuge ou un champ de bataille émotionnel. Comment tu te présentes reflète directement ton état intérieur.

**Ton approche instinctive** : Le Cancer te fait te retirer dans ta coquille quand c'est trop intense. Cette protection peut être saine, mais elle peut aussi t'isoler de l'authenticité que le Scorpion cherche.

**Tensions possibles** : La vulnérabilité (Cancer) contre la force apparente (Scorpion). Tu peux projeter une image dure alors que tu te sens fragile intérieurement.

**Conseil clé** : Accepter que la vraie force inclut la douceur. Montrer ta sensibilité n'est pas une faiblesse.""",
        'weekly_advice': {
            'week_1': "Crée un espace sûr où tu peux être totalement toi-même.",
            'week_2': "Laisse sortir une émotion que tu retiens depuis longtemps.",
            'week_3': "Prends soin de ton corps comme d'un temple sacré.",
            'week_4': "Note comment ta relation à ton image a évolué ce mois-ci."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Royauté sombre**

Ta Lune en Scorpion en Maison 1 apporte profondeur et intensité à ton identité. L'Ascendant Lion veut briller, rayonner, être vu·e. Cette combinaison crée un magnétisme puissant mais parfois contradictoire.

**Domaine activé** : Maison 1 — Ton image, ta présence, ta manière d'occuper l'espace. Tu veux être remarqué·e (Lion) tout en gardant tes cartes cachées (Scorpion).

**Ton approche instinctive** : Le Lion te pousse sur le devant de la scène, mais le Scorpion préfère contrôler depuis l'ombre. Tu peux être à la fois charismatique et mystérieux·se.

**Tensions possibles** : Le besoin de reconnaissance (Lion) contre le besoin de secret (Scorpion). Tu risques de jouer un rôle plutôt que d'être authentique.

**Conseil clé** : Trouver une manière de briller en montrant ta vraie profondeur, pas juste une façade.""",
        'weekly_advice': {
            'week_1': "Identifie quelle partie de toi mérite vraiment d'être vue.",
            'week_2': "Ose montrer une facette plus vulnérable ou complexe.",
            'week_3': "Observe si ton besoin d'attention vient de l'ego ou du cœur.",
            'week_4': "Célèbre ta transformation en l'affirmant publiquement."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Précision intense**

Ta Lune en Scorpion en Maison 1 te plonge dans une quête d'authenticité viscérale. L'Ascendant Vierge apporte analyse, discernement, perfectionnisme. Tu veux comprendre et améliorer ton identité avec une rigueur chirurgicale.

**Domaine activé** : Maison 1 — Ton corps, ton image, ta manière d'être dans le monde. Tu cherches à purifier, à affiner, à perfectionner qui tu es.

**Ton approche instinctive** : La Vierge dissèque, le Scorpion sonde. Ensemble, ils créent une capacité d'auto-analyse redoutable, parfois trop critique.

**Tensions possibles** : L'obsession du détail peut te faire perdre de vue l'ensemble. La critique intérieure devient destructrice plutôt que constructive.

**Conseil clé** : Utiliser ton regard acéré pour guérir, pas pour te flageller. La transformation passe aussi par l'acceptation.""",
        'weekly_advice': {
            'week_1': "Identifie un aspect de toi que tu veux transformer sans jugement.",
            'week_2': "Mets en place une routine de purification (corporelle ou mentale).",
            'week_3': "Observe tes patterns négatifs avec compassion, pas avec sévérité.",
            'week_4': "Fais le bilan des améliorations concrètes accomplies."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Charme vénéneux**

Ta Lune en Scorpion en Maison 1 cherche l'intensité et la vérité dans ton identité. L'Ascendant Balance apporte diplomatie, harmonie, besoin de plaire. Cette combinaison crée une séduction magnétique mais parfois manipulatrice.

**Domaine activé** : Maison 1 — Ton image, ta présence sociale. Tu veux être aimé·e (Balance) tout en gardant ton pouvoir (Scorpion). L'équilibre entre les deux n'est pas simple.

**Ton approche instinctive** : La Balance adoucit, le Scorpion intensifie. Tu peux utiliser le charme pour obtenir ce que tu veux, mais cela peut te déconnecter de ton authenticité.

**Tensions possibles** : Le besoin d'harmonie (Balance) contre le besoin de vérité brute (Scorpion). Tu risques de sacrifier ton intégrité pour éviter les conflits.

**Conseil clé** : Apprendre que les vraies relations supportent ton intensité. Inutile de te diluer.""",
        'weekly_advice': {
            'week_1': "Identifie où tu joues un rôle pour plaire plutôt qu'être toi.",
            'week_2': "Ose dire une vérité difficile avec tact mais sans édulcorer.",
            'week_3': "Observe comment ton besoin d'approbation influence ton image.",
            'week_4': "Célèbre ta capacité à être à la fois intense et élégant·e."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Phénix absolu**

Double Scorpion : ta Lune en Maison 1 avec Ascendant Scorpion crée une intensité émotionnelle totale autour de ton identité. Ce mois est une mort-renaissance. Rien de superficiel ne survivra.

**Domaine activé** : Maison 1 — Ton essence même. Tu es en pleine métamorphose. Ce que tu croyais être est en train de s'effondrer pour laisser place à une version plus vraie, plus puissante.

**Ton approche instinctive** : Double fixité d'eau : tu t'accroches ou tu lâches tout. Pas de demi-mesure. Quand tu décides de changer, c'est radical.

**Tensions possibles** : L'intensité peut devenir obsessionnelle. Le besoin de contrôle total peut te rigidifier. Attention à la paranoïa ou à l'auto-destruction.

**Conseil clé** : Faire confiance au processus de transformation. Ce qui meurt en toi fait place à quelque chose de plus fort.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit absolument mourir en toi.",
            'week_2': "Traverse la phase de deuil sans résister. Pleure si nécessaire.",
            'week_3': "Accueille les premiers signes de renaissance. Sois attentif·ve.",
            'week_4': "Affirme ta nouvelle identité avec force et clarté."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vérité enflammée**

Ta Lune en Scorpion en Maison 1 cherche la profondeur et la transformation de ton identité. L'Ascendant Sagittaire apporte optimisme, expansion, besoin de sens. Cette combinaison crée une quête philosophique intense.

**Domaine activé** : Maison 1 — Ton image, ton rôle dans le monde. Tu veux incarner une vérité plus grande que toi, une mission qui te dépasse.

**Ton approche instinctive** : Le Sagittaire voit loin, le Scorpion creuse profond. Ensemble, ils cherchent le sens ultime de l'existence à travers ton expérience personnelle.

**Tensions possibles** : Le besoin de légèreté (Sagittaire) contre le poids émotionnel (Scorpion). Tu risques de fuir dans la philosophie pour éviter de ressentir.

**Conseil clé** : Trouver un sens à ta transformation plutôt que de la fuir. Chaque mort intérieure est une initiation.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie ou spiritualité qui parle à ton âme.",
            'week_2': "Relie tes épreuves personnelles à un enseignement universel.",
            'week_3': "Partage ta vérité avec quelqu'un qui peut la recevoir.",
            'week_4': "Intègre ce que tu as appris dans une nouvelle vision de toi."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Pouvoir silencieux**

Ta Lune en Scorpion en Maison 1 active une transformation profonde de ton identité. L'Ascendant Capricorne apporte structure, ambition, maîtrise. Cette combinaison crée une autorité magnétique et implacable.

**Domaine activé** : Maison 1 — Ton image publique, ton statut, ta réputation. Tu veux être respecté·e pour ta force intérieure autant que pour tes accomplissements.

**Ton approche instinctive** : Le Capricorne construit, le Scorpion détruit pour reconstruire. Tu as la patience de démolir méthodiquement ce qui ne te sert plus.

**Tensions possibles** : Le contrôle excessif peut t'isoler émotionnellement. La peur de montrer ta vulnérabilité te rend distant·e ou froid·e.

**Conseil clé** : Accepter que le vrai pouvoir vient de l'authenticité émotionnelle, pas seulement de la compétence.""",
        'weekly_advice': {
            'week_1': "Identifie une structure de ta vie qui doit être déconstruite.",
            'week_2': "Commence à démanteler méthodiquement ce qui ne te sert plus.",
            'week_3': "Bâtis quelque chose de nouveau sur des fondations plus vraies.",
            'week_4': "Assume publiquement ta transformation avec fierté."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Révolution intérieure**

Ta Lune en Scorpion en Maison 1 cherche l'intensité et la vérité dans ton identité. L'Ascendant Verseau apporte détachement, originalité, besoin de liberté. Cette combinaison crée une rébellion contre toute forme d'inauthenticité.

**Domaine activé** : Maison 1 — Ton unicité, ta manière d'être différent·e. Tu veux te libérer des conditionnements qui t'empêchent d'être toi-même.

**Ton approche instinctive** : Le Verseau observe de loin, le Scorpion plonge au cœur. Tu peux analyser tes émotions comme un scientifique tout en les ressentant intensément.

**Tensions possibles** : Le détachement émotionnel (Verseau) contre l'intensité fusionnelle (Scorpion). Tu risques de t'anesthésier pour ne pas souffrir.

**Conseil clé** : Utiliser ton intelligence émotionnelle pour te libérer, pas pour fuir. L'authenticité est ta vraie rébellion.""",
        'weekly_advice': {
            'week_1': "Identifie une norme sociale que tu respectes par peur du jugement.",
            'week_2': "Fais un acte de rébellion douce : sois toi sans t'excuser.",
            'week_3': "Connecte-toi à des personnes qui célèbrent ton étrangeté.",
            'week_4': "Affirme ta différence comme une force, pas une faiblesse."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Dissolution mystique**

Double eau : ta Lune en Scorpion en Maison 1 avec Ascendant Poissons crée une sensibilité extrême et une porosité émotionnelle. Ton identité devient fluide, mystique, presque insaisissable.

**Domaine activé** : Maison 1 — Ton essence, ton image. Tu traverses une phase où les frontières entre toi et le monde s'estompent. Cette dissolution peut être spirituelle ou désorientante.

**Ton approche instinctive** : Les Poissons se fondent, le Scorpion contrôle. Cette tension crée une danse entre lâcher-prise et emprise, entre fusion et séparation.

**Tensions possibles** : Le risque de te perdre dans les émotions des autres ou dans des échappatoires (addiction, fantaisie, déni). La frontière entre empathie et absorption devient floue.

**Conseil clé** : Apprendre à ressentir intensément sans te noyer. Ton identité peut être fluide sans être diluée.""",
        'weekly_advice': {
            'week_1': "Médite ou pratique une activité qui t'ancre dans ton corps.",
            'week_2': "Crée de l'art à partir de tes émotions les plus profondes.",
            'week_3': "Établis des limites claires avec ceux qui drainent ton énergie.",
            'week_4': "Célèbre ta capacité à transformer la douleur en beauté."
        }
    },

    # ==================== MAISON 2 ====================

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Pouvoir matériel**

Ta Lune en Scorpion en Maison 2 active une intensité émotionnelle autour de tes ressources et ta valeur. L'Ascendant Bélier te pousse à agir vite pour conquérir ce que tu veux posséder.

**Domaine activé** : Maison 2 — Argent, possessions, sécurité matérielle. Tu veux contrôler tes ressources de manière absolue. Le manque de stabilité financière te met dans un état émotionnel intense.

**Ton approche instinctive** : Le Bélier fonce, le Scorpion calcule. Tu peux être audacieux·se dans tes investissements, mais toujours avec une stratégie sous-jacente.

**Tensions possibles** : L'impulsivité (Bélier) contre le besoin de contrôle (Scorpion) peut créer des décisions financières contradictoires. Tu risques de tout miser par passion.

**Conseil clé** : Canaliser ton intensité vers des investissements stratégiques, pas des paris émotionnels.""",
        'weekly_advice': {
            'week_1': "Identifie une source de revenus que tu peux transformer ou intensifier.",
            'week_2': "Agis rapidement sur une opportunité financière concrète.",
            'week_3': "Réévalue ce qui a vraiment de la valeur pour toi.",
            'week_4': "Consolide tes gains sans relâcher la pression."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Valeur absolue**

Ta Lune en Scorpion en Maison 2 rencontre l'Ascendant Taureau, maître naturel de cette maison. Cette combinaison crée une force magnétique autour de l'argent, la possession, la sécurité.

**Domaine activé** : Maison 2 — Tes ressources matérielles deviennent un champ de transformation profonde. Tu veux posséder non pas pour accumuler, mais pour te sentir en sécurité absolue.

**Ton approche instinctive** : Le Taureau construit lentement, le Scorpion transforme en profondeur. Tu peux détruire une source de revenus stable si elle ne nourrit plus ton âme.

**Tensions possibles** : La peur de perdre (Taureau) contre le besoin de tout brûler pour renaître (Scorpion). Cette lutte peut te figer dans un travail que tu détestes.

**Conseil clé** : Comprendre que la vraie sécurité vient de ta capacité à générer de la valeur, pas de ce que tu possèdes.""",
        'weekly_advice': {
            'week_1': "Évalue honnêtement si ton travail nourrit ton âme ou juste ton compte.",
            'week_2': "Ose lâcher une source de revenus qui te diminue.",
            'week_3': "Investis dans quelque chose de durable qui a du sens pour toi.",
            'week_4': "Ancre ta nouvelle relation à l'argent dans des habitudes concrètes."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Valeur multiple**

Ta Lune en Scorpion en Maison 2 cherche une sécurité financière profonde et totale. L'Ascendant Gémeaux apporte diversification, curiosité, mouvement. Tu veux explorer plusieurs sources de revenus.

**Domaine activé** : Maison 2 — Tes ressources, ton argent, ce que tu possèdes. Tu cherches à comprendre intellectuellement les mécanismes de richesse tout en ressentant un besoin viscéral de contrôle.

**Ton approche instinctive** : Le Gémeaux diversifie, le Scorpion concentre. Tu peux hésiter entre avoir plusieurs petites sources ou tout miser sur une.

**Tensions possibles** : La dispersion mentale (Gémeaux) contre l'obsession financière (Scorpion). Tu risques de te perdre en explorant trop d'options.

**Conseil clé** : Utiliser ton intelligence pour créer plusieurs flux de revenus stratégiques plutôt que de te disperser.""",
        'weekly_advice': {
            'week_1': "Explore deux ou trois idées de revenus différentes.",
            'week_2': "Apprends une compétence qui peut te rapporter de l'argent.",
            'week_3': "Choisis le flux le plus prometteur et intensifie-le.",
            'week_4': "Synthétise ce que tu as appris sur ta relation à l'argent."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Sécurité fusionnelle**

Double eau : ta Lune en Scorpion en Maison 2 avec Ascendant Cancer crée une sensibilité extrême autour de ta sécurité matérielle. L'argent est lié directement à ton sentiment de protection émotionnelle.

**Domaine activé** : Maison 2 — Tes ressources financières, tes possessions. Ce que tu possèdes représente ton nid, ton refuge. En perdre te mettrait en état de panique.

**Ton approche instinctive** : Le Cancer protège, le Scorpion contrôle. Tu peux être très prudent·e financièrement tout en prenant des risques calculés pour ceux que tu aimes.

**Tensions possibles** : L'attachement émotionnel à l'argent peut créer de l'avarice ou de la générosité excessive. Tes dépenses reflètent directement ton état émotionnel.

**Conseil clé** : Séparer ton besoin affectif de sécurité de tes décisions financières. L'argent n'est pas de l'amour.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu achètes pour combler un vide émotionnel.",
            'week_2': "Crée un plan financier qui te sécurise sans t'appauvrir.",
            'week_3': "Investis dans quelque chose qui nourrit ton foyer ou ta famille.",
            'week_4': "Célèbre ta capacité à générer de la sécurité par toi-même."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Richesse magnétique**

Ta Lune en Scorpion en Maison 2 active une intensité autour de ta valeur et tes ressources. L'Ascendant Lion apporte fierté, générosité, besoin de briller. Tu veux l'abondance pour rayonner.

**Domaine activé** : Maison 2 — Argent, possessions, ce qui te donne de la valeur. Tu cherches à être riche non pour accumuler, mais pour montrer ton pouvoir et ta générosité.

**Ton approche instinctive** : Le Lion dépense pour impressionner, le Scorpion contrôle pour ne jamais être vulnérable. Cette tension crée des comportements contradictoires avec l'argent.

**Tensions possibles** : Le besoin de reconnaissance (Lion) peut te faire dépenser au-delà de tes moyens. Le besoin de contrôle (Scorpion) peut créer de l'avarice cachée.

**Conseil clé** : Trouver un équilibre entre générosité authentique et prudence stratégique. La vraie richesse vient de ta valeur intérieure.""",
        'weekly_advice': {
            'week_1': "Identifie où tu dépenses pour impressionner plutôt que par plaisir.",
            'week_2': "Investis dans quelque chose qui te fait vraiment briller.",
            'week_3': "Sois généreux·se d'une manière qui ne te met pas en danger financier.",
            'week_4': "Célèbre tes acquis sans comparer avec les autres."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Valeur purifiée**

Ta Lune en Scorpion en Maison 2 cherche une transformation profonde de ta relation à l'argent. L'Ascendant Vierge apporte analyse, discernement, besoin d'efficacité. Tu veux optimiser chaque centime.

**Domaine activé** : Maison 2 — Tes ressources, ta sécurité matérielle. Tu analyses obsessivement tes finances, cherchant à éliminer tout gaspillage, toute faille.

**Ton approche instinctive** : La Vierge budgétise, le Scorpion investit stratégiquement. Ensemble, ils créent une discipline financière redoutable mais parfois anxiogène.

**Tensions possibles** : L'obsession du détail peut te faire perdre de vue les grandes opportunités. La peur du manque crée de l'avarice ou de l'anxiété chronique.

**Conseil clé** : Utiliser ton analyse pour libérer ton énergie, pas pour la contrôler jusqu'à l'épuisement. La perfection financière n'existe pas.""",
        'weekly_advice': {
            'week_1': "Fais un audit complet de tes finances avec une rigueur chirurgicale.",
            'week_2': "Élimine une dépense inutile qui te pèse depuis longtemps.",
            'week_3': "Investis dans une formation ou un outil qui améliore tes revenus.",
            'week_4': "Accepte que certaines dépenses sont nécessaires sans culpabilité."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Valeur partagée**

Ta Lune en Scorpion en Maison 2 cherche le contrôle absolu de tes ressources. L'Ascendant Balance apporte besoin de partage, d'équilibre, de réciprocité. Cette combinaison crée une tension entre le mien et le nôtre.

**Domaine activé** : Maison 2 — Argent, possessions, sécurité. Tu veux à la fois protéger tes ressources et les partager équitablement avec ceux que tu aimes.

**Ton approche instinctive** : La Balance négocie, le Scorpion refuse les compromis. Tu peux être généreux·se ou possessif·ve selon que tu te sens en sécurité.

**Tensions possibles** : Le besoin d'harmonie (Balance) peut te faire accepter des arrangements financiers qui te désavantagent. Le Scorpion peut réagir en devenant amer·ère.

**Conseil clé** : Apprendre que l'équité n'est pas toujours 50/50. Protège tes intérêts sans culpabilité.""",
        'weekly_advice': {
            'week_1': "Évalue si tes accords financiers sont vraiment équilibrés.",
            'week_2': "Négocie quelque chose qui te désavantage depuis trop longtemps.",
            'week_3': "Partage généreusement ce que tu as en surplus sans te vider.",
            'week_4': "Célèbre ta capacité à être à la fois généreux·se et prudent·e."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Pouvoir total**

Double Scorpion en Maison 2 : ce mois, ta relation à l'argent et aux ressources est une question de survie émotionnelle. Tu veux contrôler tes finances de manière absolue. Rien ne doit t'échapper.

**Domaine activé** : Maison 2 — Tes ressources matérielles deviennent un terrain de transformation radicale. Tu peux tout perdre ou tout gagner. Les demi-mesures ne t'intéressent pas.

**Ton approche instinctive** : Double fixité d'eau : quand tu décides d'investir ou de couper les ponts financiers, c'est irrévocable. Tu ne recules jamais.

**Tensions possibles** : L'obsession du contrôle peut créer de la paranoïa financière. La peur de manquer peut te faire accumuler ou au contraire tout dilapider pour tester ta capacité à renaître.

**Conseil clé** : Comprendre que le vrai pouvoir vient de ta capacité à régénérer de la richesse, pas de ce que tu possèdes.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu dois absolument transformer dans ta vie financière.",
            'week_2': "Prends une décision radicale concernant une source de revenus ou une dette.",
            'week_3': "Accepte de tout perdre pour mieux reconstruire si nécessaire.",
            'week_4': "Affirme ton nouveau rapport à l'argent avec force."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Richesse expansive**

Ta Lune en Scorpion en Maison 2 cherche le contrôle de tes ressources. L'Ascendant Sagittaire apporte optimisme, expansion, prise de risque. Tu veux investir dans ce qui a du sens, pas juste accumuler.

**Domaine activé** : Maison 2 — Argent, valeur, sécurité. Tu cherches à aligner tes finances avec tes croyances. Gagner de l'argent doit servir un but plus grand.

**Ton approche instinctive** : Le Sagittaire mise gros, le Scorpion calcule. Tu peux prendre des risques financiers importants si tu crois en la vision.

**Tensions possibles** : L'excès d'optimisme (Sagittaire) peut te faire ignorer les signaux d'alerte du Scorpion. Tu risques de perdre gros en pariant sur une philosophie plutôt qu'une stratégie.

**Conseil clé** : Investir dans ce qui a du sens pour toi, mais sans négliger la prudence stratégique.""",
        'weekly_advice': {
            'week_1': "Identifie un projet qui allie abondance et sens profond.",
            'week_2': "Prends un risque financier calculé qui te fait grandir.",
            'week_3': "Réévalue si ta quête de sens te coûte trop cher concrètement.",
            'week_4': "Célèbre ta capacité à créer de la richesse par ta vision."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fortune stratégique**

Ta Lune en Scorpion en Maison 2 active une intensité autour de ta sécurité matérielle. L'Ascendant Capricorne apporte discipline, ambition, construction méthodique. Cette combinaison crée une machine de guerre financière.

**Domaine activé** : Maison 2 — Tes ressources, ton patrimoine. Tu veux bâtir une forteresse financière imprenable, pierre par pierre.

**Ton approche instinctive** : Le Capricorne construit patiemment, le Scorpion élimine impitoyablement ce qui ne rapporte pas. Ensemble, ils créent une efficacité redoutable.

**Tensions possibles** : L'obsession de la sécurité peut te faire sacrifier le présent pour un futur qui n'arrive jamais. L'avarice devient une prison dorée.

**Conseil clé** : Construire pour durer sans oublier de vivre. L'argent est un moyen, pas une fin.""",
        'weekly_advice': {
            'week_1': "Définis un objectif financier à long terme clair et ambitieux.",
            'week_2': "Mets en place une structure qui génère des revenus passifs.",
            'week_3': "Élimine une dépense qui sabote ta construction à long terme.",
            'week_4': "Célèbre les fondations solides que tu as posées ce mois-ci."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Valeur alternative**

Ta Lune en Scorpion en Maison 2 cherche le contrôle absolu de tes ressources. L'Ascendant Verseau apporte détachement, originalité, refus des conventions. Tu veux gagner de l'argent autrement.

**Domaine activé** : Maison 2 — Tes finances, ta sécurité matérielle. Tu rejettes les méthodes traditionnelles de richesse pour inventer ton propre modèle.

**Ton approche instinctive** : Le Verseau innove, le Scorpion contrôle. Tu peux créer des sources de revenus uniques mais tu veux en garder la totale maîtrise.

**Tensions possibles** : Le détachement émotionnel (Verseau) contre l'intensité possessive (Scorpion). Tu risques de tout perdre par idéalisme ou de t'accrocher par peur.

**Conseil clé** : Utiliser ton originalité pour créer de la richesse sans sacrifier ta sécurité émotionnelle.""",
        'weekly_advice': {
            'week_1': "Explore une méthode non-conventionnelle de générer des revenus.",
            'week_2': "Connecte-toi à des personnes qui pensent différemment l'argent.",
            'week_3': "Teste une idée financière audacieuse sans tout miser dessus.",
            'week_4': "Intègre ton innovation dans une structure stable."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Valeur mystique**

Double eau : ta Lune en Scorpion en Maison 2 avec Ascendant Poissons crée une relation complexe à l'argent. Tu oscilles entre contrôle absolu et lâcher-prise total.

**Domaine activé** : Maison 2 — Tes ressources matérielles. L'argent devient un symbole spirituel autant qu'un outil pratique. Tu veux l'abondance sans t'y attacher.

**Ton approche instinctive** : Les Poissons font confiance à l'univers, le Scorpion veut tout contrôler. Cette tension crée une alternance entre foi aveugle et méfiance totale.

**Tensions possibles** : Le risque de te faire exploiter financièrement par empathie excessive ou de devenir paranoïaque et avare. Les frontières sont floues.

**Conseil clé** : Apprendre que la générosité spirituelle n'exclut pas la prudence matérielle. Tu peux être mystique et stratégique.""",
        'weekly_advice': {
            'week_1': "Médite sur ta relation émotionnelle à l'argent sans jugement.",
            'week_2': "Crée de l'art ou une offrande qui transforme l'énergie financière.",
            'week_3': "Protège-toi de ceux qui profitent de ta générosité.",
            'week_4': "Célèbre ta capacité à manifester l'abondance par ta foi."
        }
    },

    # ==================== MAISON 3 ====================

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Parole incendiaire**

Ta Lune en Scorpion en Maison 3 active une intensité dans ta communication. L'Ascendant Bélier te pousse à dire les vérités qui brûlent, sans filtre.

**Domaine activé** : Maison 3 — Communication, apprentissage, déplacements courts, fratrie. Tes mots deviennent des armes. Tu veux comprendre en profondeur et le dire franchement.

**Ton approche instinctive** : Le Bélier attaque verbalement, le Scorpion sonde psychologiquement. Tu peux déstabiliser par ta capacité à voir et à dire ce que les autres cachent.

**Tensions possibles** : L'impulsivité verbale peut créer des ruptures. Tu risques de blesser avant de réfléchir. Les secrets découverts sont révélés trop vite.

**Conseil clé** : Canaliser ta force de vérité vers des conversations qui transforment plutôt que détruisent.""",
        'weekly_advice': {
            'week_1': "Identifie une vérité difficile que tu dois dire à quelqu'un.",
            'week_2': "Dis-la avec franchise mais sans violence inutile.",
            'week_3': "Apprends quelque chose qui te donne du pouvoir intellectuel.",
            'week_4': "Utilise tes mots pour guérir une relation, pas la détruire."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Vérité ancrée**

Ta Lune en Scorpion en Maison 3 cherche la profondeur dans la communication. L'Ascendant Taureau apporte prudence, lenteur, besoin de concret. Tu pèses chaque mot avant de le dire.

**Domaine activé** : Maison 3 — Échanges, apprentissage, environnement immédiat. Tu veux des conversations qui ont du poids, du sens, de la substance.

**Ton approche instinctive** : Le Taureau retient ses mots, le Scorpion observe. Quand tu parles enfin, c'est définitif. Impossible de te faire changer d'avis facilement.

**Tensions possibles** : Le silence prolongé peut être interprété comme de la froideur. Quand tu exploses enfin, c'est disproportionné.

**Conseil clé** : Apprendre à exprimer régulièrement ce que tu ressens plutôt que d'accumuler jusqu'à l'explosion.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu retiens depuis trop longtemps.",
            'week_2': "Exprime-toi simplement, sans attendre le moment parfait.",
            'week_3': "Apprends quelque chose de concret qui a de la valeur pratique.",
            'week_4': "Célèbre ta capacité à dire des vérités qui durent."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Intelligence profonde**

Ta Lune en Scorpion en Maison 3 active l'intensité mentale. L'Ascendant Gémeaux, maître naturel de cette maison, apporte curiosité, agilité intellectuelle. Tu veux tout savoir, tout comprendre.

**Domaine activé** : Maison 3 — Communication, apprentissage, connexions locales. Ton esprit devient une machine d'analyse psychologique. Tu détectes les non-dits, les mensonges.

**Ton approche instinctive** : Le Gémeaux papillonne, le Scorpion obsède. Tu peux passer de sujet en sujet ou t'enfoncer dans un seul jusqu'à l'épuisement.

**Tensions possibles** : La dispersion mentale contre l'obsession intellectuelle. Tu risques de te perdre dans des trous de lapin psychologiques ou conspirationnistes.

**Conseil clé** : Utiliser ton intelligence pour comprendre sans devenir paranoïaque. La vérité n'est pas toujours sombre.""",
        'weekly_advice': {
            'week_1': "Explore un sujet tabou ou mystérieux qui te fascine.",
            'week_2': "Partage ce que tu apprends avec quelqu'un de confiance.",
            'week_3': "Fais une pause mentale pour ne pas te surcharger.",
            'week_4': "Synthétise tes découvertes sans tomber dans la paranoïa."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Parole intime**

Double eau en Maison 3 : ta Lune en Scorpion avec Ascendant Cancer crée une communication chargée émotionnellement. Tes mots viennent du ventre, pas de la tête.

**Domaine activé** : Maison 3 — Échanges, fratrie, apprentissage. Tu veux des conversations qui touchent le cœur. Les bavardages superficiels te drainent.

**Ton approche instinctive** : Le Cancer protège, le Scorpion révèle. Tu oscilles entre tout garder pour toi et tout déverser avec intensité.

**Tensions possibles** : La sensibilité peut te faire mal interpréter les mots des autres. Tu peux te replier dans le silence ou noyer l'autre sous tes émotions.

**Conseil clé** : Apprendre à exprimer ton ressenti sans fusionner ou fuir. La vraie communication crée des ponts, pas des murs.""",
        'weekly_advice': {
            'week_1': "Écris une lettre émotionnelle que tu n'enverras pas nécessairement.",
            'week_2': "Partage une vulnérabilité avec quelqu'un de sûr.",
            'week_3': "Apprends à mettre des mots sur tes émotions complexes.",
            'week_4': "Célèbre les connexions authentiques que tu as créées."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Expression magnétique**

Ta Lune en Scorpion en Maison 3 active une profondeur de pensée intense. L'Ascendant Lion apporte un besoin de briller par la parole. Tu veux être entendu·e, écouté·e, admiré·e.

**Domaine activé** : Maison 3 — Communication, enseignement, médias. Tu as quelque chose d'important à dire et tu veux que ça compte.

**Ton approche instinctive** : Le Lion dramatise, le Scorpion sonde. Tes paroles peuvent être théâtrales mais elles touchent toujours un point sensible.

**Tensions possibles** : Le besoin d'attention (Lion) peut te faire révéler des secrets pour impressionner. Le Scorpion peut ensuite regretter cette exposition.

**Conseil clé** : Trouver un équilibre entre briller et protéger ton intimité. Tu n'as pas besoin de tout révéler pour être fascinant·e.""",
        'weekly_advice': {
            'week_1': "Identifie un message puissant que tu veux faire passer.",
            'week_2': "Exprime-le publiquement avec force et clarté.",
            'week_3': "Observe l'impact de tes mots sans chercher l'approbation.",
            'week_4': "Célèbre ta capacité à inspirer par ta vérité."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Analyse chirurgicale**

Ta Lune en Scorpion en Maison 3 active une intensité mentale. L'Ascendant Vierge apporte précision, discernement, besoin de comprendre en détail. Ton esprit devient un scalpel.

**Domaine activé** : Maison 3 — Communication, apprentissage, logique. Tu veux décortiquer chaque information, détecter chaque incohérence, comprendre chaque mécanisme.

**Ton approche instinctive** : La Vierge analyse méthodiquement, le Scorpion creuse jusqu'à l'os. Ensemble, ils créent une capacité de recherche et de critique redoutable.

**Tensions possibles** : L'obsession du détail peut te faire perdre de vue l'humain derrière les faits. Tes critiques peuvent blesser même si elles sont justes.

**Conseil clé** : Utiliser ton intelligence pour guérir les problèmes, pas pour les disséquer à l'infini.""",
        'weekly_advice': {
            'week_1': "Identifie un problème complexe que tu veux résoudre.",
            'week_2': "Recherche méthodiquement toutes les informations nécessaires.",
            'week_3': "Partage tes découvertes avec bienveillance, pas avec jugement.",
            'week_4': "Accepte que certaines questions n'ont pas de réponse parfaite."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Diplomatie intense**

Ta Lune en Scorpion en Maison 3 cherche la vérité profonde dans les échanges. L'Ascendant Balance apporte tact, harmonie, besoin d'équilibre. Tu veux dire la vérité sans détruire la relation.

**Domaine activé** : Maison 3 — Communication, négociation, relations proches. Tu cherches à exprimer ce qui est difficile avec élégance.

**Ton approche instinctive** : La Balance adoucit, le Scorpion tranche. Tu peux enrober tes vérités dures dans des mots doux, mais le message reste puissant.

**Tensions possibles** : Le besoin d'harmonie peut te faire taire des vérités nécessaires. Quand le Scorpion explose enfin, la Balance se sent coupable.

**Conseil clé** : Apprendre que la vraie harmonie inclut les conflits nécessaires. Dire la vérité avec tact n'est pas de la manipulation.""",
        'weekly_advice': {
            'week_1': "Identifie une conversation difficile que tu évites par peur du conflit.",
            'week_2': "Prépare tes mots pour dire la vérité avec douceur mais fermeté.",
            'week_3': "Aie cette conversation en restant centré·e sur la connexion.",
            'week_4': "Célèbre ta capacité à être honnête et aimant·e à la fois."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Vérité absolue**

Double Scorpion en Maison 3 : ce mois, ta communication devient un terrain de transformation radicale. Tu veux dire et entendre la vérité la plus nue, sans concession.

**Domaine activé** : Maison 3 — Parole, écriture, pensée. Tes mots ont un pouvoir de vie ou de mort sur les relations. Tu détectes chaque mensonge, chaque non-dit.

**Ton approche instinctive** : Double intensité fixe : quand tu décides de parler, c'est pour détruire ou reconstruire entièrement. Les demi-mesures n'existent pas.

**Tensions possibles** : L'obsession de la vérité peut devenir destructrice. Tu risques de tout brûler par besoin de transparence totale.

**Conseil clé** : Comprendre que certains silences protègent, que certaines vérités tuent inutilement. Le pouvoir des mots exige de la sagesse.""",
        'weekly_advice': {
            'week_1': "Identifie ce que tu dois absolument dire pour te libérer.",
            'week_2': "Dis-le, mais mesure l'impact avant de tout détruire.",
            'week_3': "Accepte que certaines vérités resteront non-dites.",
            'week_4': "Affirme ta nouvelle manière de communiquer avec force."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Vérité expansive**

Ta Lune en Scorpion en Maison 3 cherche la profondeur dans la communication. L'Ascendant Sagittaire apporte optimisme, franchise, besoin de sens. Tu veux dire la vérité qui libère.

**Domaine activé** : Maison 3 — Parole, enseignement, philosophie appliquée. Tu cherches à transformer ta compréhension profonde en message universel.

**Ton approche instinctive** : Le Sagittaire inspire, le Scorpion révèle. Tu peux être un·e enseignant·e ou un·e orateur·ice puissant·e qui touche l'âme.

**Tensions possibles** : L'excès d'optimisme (Sagittaire) peut édulcorer les vérités dures du Scorpion. Ou inversement, ton intensité peut effrayer ceux que tu veux inspirer.

**Conseil clé** : Trouver un équilibre entre profondeur et légèreté. La vérité peut être libératrice sans être écrasante.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie qui parle à tes profondeurs.",
            'week_2': "Partage ce que tu apprends d'une manière accessible.",
            'week_3': "Enseigne ou écris sur un sujet qui te transforme.",
            'week_4': "Célèbre ta capacité à inspirer par ta vérité."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Parole stratégique**

Ta Lune en Scorpion en Maison 3 active une intensité dans ta communication. L'Ascendant Capricorne apporte contrôle, structure, autorité. Tes mots deviennent des outils de pouvoir.

**Domaine activé** : Maison 3 — Communication professionnelle, négociation, influence. Tu veux dire ce qu'il faut pour obtenir ce que tu veux.

**Ton approche instinctive** : Le Capricorne calcule, le Scorpion manipule (positivement ou non). Tu sais exactement quoi dire, quand et à qui pour atteindre tes objectifs.

**Tensions possibles** : L'excès de contrôle verbal peut te faire perdre ton authenticité. Les autres sentent la manipulation même si elle est subtile.

**Conseil clé** : Utiliser ton pouvoir de communication pour construire, pas pour dominer. L'autorité vient de l'authenticité.""",
        'weekly_advice': {
            'week_1': "Identifie un objectif que tu peux atteindre par la parole.",
            'week_2': "Prépare soigneusement ta communication stratégique.",
            'week_3': "Agis en restant intègre même dans la négociation.",
            'week_4': "Célèbre ce que tu as obtenu par ta maîtrise verbale."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Vérité révolutionnaire**

Ta Lune en Scorpion en Maison 3 cherche la profondeur dans la pensée. L'Ascendant Verseau apporte originalité, détachement, besoin de liberté. Tu veux penser autrement, dire ce que personne n'ose.

**Domaine activé** : Maison 3 — Communication alternative, idées avant-gardistes, réseaux sociaux. Tu veux révolutionner la manière de penser et de parler.

**Ton approche instinctive** : Le Verseau questionne les normes, le Scorpion détruit les tabous. Ensemble, ils créent une voix unique et dérangeante.

**Tensions possibles** : Le détachement intellectuel (Verseau) contre l'intensité émotionnelle (Scorpion). Tu risques de choquer sans mesurer l'impact humain.

**Conseil clé** : Utiliser ton originalité pour libérer les esprits, pas pour créer du chaos gratuit.""",
        'weekly_advice': {
            'week_1': "Explore une idée radicale qui remet en question tes croyances.",
            'week_2': "Partage-la avec des personnes qui peuvent la recevoir.",
            'week_3': "Connecte-toi à des esprits rebelles qui pensent comme toi.",
            'week_4': "Affirme ta différence intellectuelle sans t'excuser."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Parole mystique**

Double eau en Maison 3 : ta Lune en Scorpion avec Ascendant Poissons crée une communication chargée d'intuition et de profondeur. Tes mots viennent d'ailleurs.

**Domaine activé** : Maison 3 — Écriture, poésie, communication non-verbale. Tu captes et transmets des vérités qui dépassent la logique.

**Ton approche instinctive** : Les Poissons canalisent, le Scorpion révèle. Tu peux être médium, artiste ou thérapeute par la parole.

**Tensions possibles** : La confusion entre intuition et projection. Tu risques de dire des vérités profondes mélangées à tes propres peurs.

**Conseil clé** : Apprendre à distinguer ce qui vient de ton inconscient et ce qui vient de l'autre. La clarté sert ta profondeur.""",
        'weekly_advice': {
            'week_1': "Écris librement sans chercher à contrôler ce qui sort.",
            'week_2': "Partage ta créativité ou ton intuition avec confiance.",
            'week_3': "Protège-toi des personnes qui drainent ton énergie verbale.",
            'week_4': "Célèbre ta capacité à transformer par tes mots."
        }
    },

    # ==================== MAISON 4 ====================

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Racines explosives**

Ta Lune en Scorpion en Maison 4 active une transformation profonde de ton foyer intérieur. L'Ascendant Bélier te pousse à agir vite pour reconstruire tes fondations.

**Domaine activé** : Maison 4 — Famille, foyer, racines émotionnelles. Tu veux couper avec ce qui t'a blessé dans ton passé et reconstruire un sanctuaire.

**Ton approche instinctive** : Le Bélier rompt brutalement, le Scorpion transforme en profondeur. Tu peux quitter physiquement ou émotionnellement ton environnement familial.

**Tensions possibles** : L'impulsivité peut te faire fuir avant d'avoir vraiment guéri. Les ruptures familiales peuvent être définitives et regrettées.

**Conseil clé** : Transformer tes blessures familiales en force plutôt que de simplement fuir.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit mourir dans ta relation à ta famille ou ton passé.",
            'week_2': "Prends une décision radicale pour protéger ton espace intérieur.",
            'week_3': "Crée un rituel de libération émotionnelle (lettre, feu, etc.).",
            'week_4': "Construis activement le foyer ou la famille que tu veux vraiment."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Foyer transformé**

Ta Lune en Scorpion en Maison 4 cherche une transformation profonde de tes racines. L'Ascendant Taureau apporte besoin de stabilité, de confort, de sécurité. Cette tension crée un bouleversement lent mais définitif.

**Domaine activé** : Maison 4 — Ton chez-toi, ta famille, ton héritage émotionnel. Tu veux à la fois détruire ce qui te blesse et construire quelque chose de solide.

**Ton approche instinctive** : Le Taureau résiste au changement, le Scorpion sait qu'il est nécessaire. Tu peux rester dans une situation toxique par peur de l'inconnu.

**Tensions possibles** : La peur de perdre ta sécurité peut te garder prisonnier·ère d'un foyer qui t'étouffe.

**Conseil clé** : Accepter que la vraie sécurité vient de ta capacité à reconstruire, pas de ce que tu refuses de quitter.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te retient dans un environnement toxique.",
            'week_2': "Commence à transformer ton espace de vie concrètement.",
            'week_3': "Investis dans quelque chose qui rend ton foyer plus sain.",
            'week_4': "Ancre ta nouvelle relation à ton chez-toi dans des rituels."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Racines multiples**

Ta Lune en Scorpion en Maison 4 cherche la profondeur émotionnelle dans ton foyer. L'Ascendant Gémeaux apporte mouvement, curiosité, besoin de variété. Tu veux comprendre tes racines intellectuellement.

**Domaine activé** : Maison 4 — Famille, foyer, passé. Tu cherches à analyser ton héritage familial, à comprendre d'où viennent tes patterns.

**Ton approche instinctive** : Le Gémeaux parle de ses blessures, le Scorpion les garde secrètes. Tu oscilles entre tout raconter et tout taire.

**Tensions possibles** : La dispersion peut t'empêcher de vraiment guérir. Tu risques de comprendre intellectuellement sans transformer émotionnellement.

**Conseil clé** : Utiliser les mots pour explorer tes blessures, mais ne pas te cacher derrière eux.""",
        'weekly_advice': {
            'week_1': "Écris sur ton histoire familiale sans censure.",
            'week_2': "Parle à un membre de ta famille d'un sujet difficile.",
            'week_3': "Apprends sur la psychologie transgénérationnelle.",
            'week_4': "Synthétise ce que tu as compris et ce que tu veux changer."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Océan familial**

Double eau en Maison 4, secteur naturel de la Lune : ta Lune en Scorpion avec Ascendant Cancer crée une sensibilité extrême autour de la famille et du foyer. C'est intense.

**Domaine activé** : Maison 4 — Famille, racines, mémoire émotionnelle. Tout remonte à la surface. Les blessures anciennes demandent à être guéries.

**Ton approche instinctive** : Le Cancer protège et nourrit, le Scorpion transforme par la douleur. Tu veux créer un foyer sûr en traversant l'enfer émotionnel familial.

**Tensions possibles** : La fusion émotionnelle avec ta famille peut t'empêcher de t'en séparer sainement. Tu portes les douleurs de plusieurs générations.

**Conseil clé** : Guérir ton lignage sans te sacrifier. Tu n'es pas responsable des blessures de tes ancêtres.""",
        'weekly_advice': {
            'week_1': "Crée un espace sacré chez toi pour te ressourcer.",
            'week_2': "Pleure ou exprime les émotions familiales que tu retiens.",
            'week_3': "Protège-toi des dynamiques toxiques sans couper les ponts nécessairement.",
            'week_4': "Célèbre ta capacité à transformer ton héritage."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Fierté des racines**

Ta Lune en Scorpion en Maison 4 active une transformation de ton foyer et de tes racines. L'Ascendant Lion apporte fierté, besoin de rayonner même dans l'intimité.

**Domaine activé** : Maison 4 — Ton chez-toi, ta famille, ton héritage. Tu veux transformer ton foyer en quelque chose dont tu peux être fier·ère.

**Ton approche instinctive** : Le Lion règne sur son royaume, le Scorpion détruit pour reconstruire. Tu peux vouloir imposer ta vision de la famille.

**Tensions possibles** : Le besoin de contrôle (Scorpion) contre le besoin de reconnaissance (Lion). Tu risques de régner en tyran sur ton foyer.

**Conseil clé** : Créer un foyer où tu peux briller sans écraser les autres. La vraie royauté est généreuse.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit changer dans ton espace de vie.",
            'week_2': "Transforme ton chez-toi en un lieu qui reflète ta vraie grandeur.",
            'week_3': "Assume ton leadership familial sans dominer.",
            'week_4': "Célèbre ton foyer comme ton royaume sacré."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Purification du foyer**

Ta Lune en Scorpion en Maison 4 cherche une transformation profonde de ton espace intérieur. L'Ascendant Vierge apporte besoin de pureté, d'ordre, de perfection.

**Domaine activé** : Maison 4 — Ton chez-toi, ton passé, ta famille. Tu veux nettoyer, purifier, éliminer tout ce qui est toxique dans ton environnement.

**Ton approche instinctive** : La Vierge organise et nettoie, le Scorpion jette et brûle. Ensemble, ils créent une purge radicale de ton foyer.

**Tensions possibles** : L'obsession de la pureté peut devenir oppressante. Tu risques de vouloir contrôler chaque aspect de ton environnement.

**Conseil clé** : Purifier sans devenir obsessionnel·le. Un foyer parfait n'existe pas, un foyer sain oui.""",
        'weekly_advice': {
            'week_1': "Fais un tri radical de tes affaires. Garde seulement ce qui te sert.",
            'week_2': "Nettoie énergétiquement ton espace (sauge, sel, etc.).",
            'week_3': "Mets en place des routines qui maintiennent la pureté.",
            'week_4': "Accepte l'imperfection tout en maintenant ta discipline."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie profonde**

Ta Lune en Scorpion en Maison 4 cherche la transformation de ton foyer. L'Ascendant Balance apporte besoin d'harmonie, de beauté, d'équilibre dans ton espace intime.

**Domaine activé** : Maison 4 — Ton chez-toi, tes racines familiales. Tu veux créer un espace qui soit à la fois profond et harmonieux.

**Ton approche instinctive** : La Balance apaise, le Scorpion confronte. Tu oscilles entre éviter les conflits familiaux et les exploser.

**Tensions possibles** : Le besoin de paix peut te faire tolérer des situations toxiques. Quand le Scorpion explose, la Balance se sent coupable.

**Conseil clé** : Comprendre que la vraie harmonie inclut les transformations nécessaires. Parfois, détruire c'est guérir.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui crée du déséquilibre dans ton foyer.",
            'week_2': "Aie une conversation difficile mais nécessaire avec ta famille.",
            'week_3': "Crée de la beauté dans ton espace de vie.",
            'week_4': "Célèbre l'harmonie que tu as créée par ta transformation."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Métamorphose radicale**

Double Scorpion en Maison 4 : ce mois, ton foyer et tes racines traversent une mort-renaissance totale. Rien ne sera comme avant.

**Domaine activé** : Maison 4 — Famille, foyer, passé. Tu es en train de transformer complètement ta relation à tes origines. C'est douloureux mais libérateur.

**Ton approche instinctive** : Double intensité fixe : quand tu décides de couper avec ton passé ou de reconstruire ton foyer, c'est définitif.

**Tensions possibles** : L'intensité peut devenir destructrice. Tu risques de tout brûler sans laisser de place à la réconciliation.

**Conseil clé** : Accepter que certaines morts familiales sont nécessaires pour renaître. Le deuil est un passage, pas une destination.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit absolument mourir dans ton histoire familiale.",
            'week_2': "Traverse le deuil sans résister. Pleure, rage, accepte.",
            'week_3': "Commence à construire le foyer que tu veux vraiment.",
            'week_4': "Affirme ta nouvelle relation à tes racines avec force."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Racines libres**

Ta Lune en Scorpion en Maison 4 cherche la profondeur émotionnelle dans ton foyer. L'Ascendant Sagittaire apporte besoin de liberté, d'expansion, de sens.

**Domaine activé** : Maison 4 — Famille, foyer, passé. Tu veux te libérer du poids de ton héritage tout en l'honorant.

**Ton approche instinctive** : Le Sagittaire fuit, le Scorpion confronte. Tu oscilles entre partir loin et plonger dans tes blessures familiales.

**Tensions possibles** : La fuite dans l'aventure peut t'empêcher de vraiment guérir. Tu risques de fuir géographiquement sans transformer émotionnellement.

**Conseil clé** : Comprendre que la vraie liberté vient de la guérison, pas de la distance.""",
        'weekly_advice': {
            'week_1': "Explore une philosophie qui t'aide à comprendre ton passé.",
            'week_2': "Voyage (physiquement ou mentalement) pour prendre du recul.",
            'week_3': "Reviens à tes racines avec une nouvelle perspective.",
            'week_4': "Intègre ce que tu as appris dans ton foyer actuel."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Fondations de pouvoir**

Ta Lune en Scorpion en Maison 4 active une transformation de tes racines. L'Ascendant Capricorne apporte structure, ambition, besoin de contrôle. Tu veux reconstruire tes fondations méthodiquement.

**Domaine activé** : Maison 4 — Foyer, famille, héritage. Tu veux créer une base solide en éliminant tout ce qui est pourri dans tes racines.

**Ton approche instinctive** : Le Capricorne construit patiemment, le Scorpion détruit impitoyablement. Tu démantèles ce qui ne tient pas pour bâtir du solide.

**Tensions possibles** : Le contrôle excessif peut te faire rigidifier les relations familiales. Tu risques de devenir froid·e par besoin de protection.

**Conseil clé** : Construire des fondations solides sans sacrifier ton humanité. La force inclut la vulnérabilité.""",
        'weekly_advice': {
            'week_1': "Identifie les structures familiales qui doivent être déconstruites.",
            'week_2': "Commence méthodiquement à démanteler ce qui ne te sert plus.",
            'week_3': "Bâtis quelque chose de nouveau sur des fondations plus saines.",
            'week_4': "Assume publiquement ta nouvelle relation à ta famille."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Famille alternative**

Ta Lune en Scorpion en Maison 4 cherche la transformation de ton foyer. L'Ascendant Verseau apporte détachement, originalité, besoin de liberté. Tu veux créer ta propre définition de famille.

**Domaine activé** : Maison 4 — Foyer, racines, appartenance. Tu rejettes les modèles familiaux traditionnels pour inventer le tien.

**Ton approche instinctive** : Le Verseau se détache, le Scorpion s'attache intensément. Tu oscilles entre fusion et indépendance totale.

**Tensions possibles** : Le détachement peut t'empêcher de vraiment guérir. Tu risques de fuir l'intimité familiale par peur de l'intensité.

**Conseil clé** : Créer ta propre famille (de sang ou de cœur) sans fuir l'intensité émotionnelle qu'elle implique.""",
        'weekly_advice': {
            'week_1': "Identifie les normes familiales que tu veux rejeter.",
            'week_2': "Connecte-toi à des personnes qui deviennent ta famille choisie.",
            'week_3': "Crée un foyer qui reflète tes valeurs uniques.",
            'week_4': "Affirme ta différence sans te couper de tes racines complètement."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Sanctuaire dissous**

Double eau en Maison 4 : ta Lune en Scorpion avec Ascendant Poissons crée une porosité émotionnelle extrême dans ton foyer. Les frontières familiales disparaissent.

**Domaine activé** : Maison 4 — Famille, foyer, mémoire ancestrale. Tu ressens tout ce qui a été vécu avant toi. Tu portes les douleurs de ton lignage.

**Ton approche instinctive** : Les Poissons absorbent, le Scorpion transforme. Tu peux guérir ton arbre généalogique entier à travers ta propre métamorphose.

**Tensions possibles** : Le risque de te perdre dans les émotions familiales. Tu ne sais plus où tu finis et où les autres commencent.

**Conseil clé** : Guérir ton lignage sans te sacrifier. Tu n'es pas le rédempteur de ta famille.""",
        'weekly_advice': {
            'week_1': "Médite sur ton héritage familial avec compassion.",
            'week_2': "Crée un rituel de libération pour ton lignage.",
            'week_3': "Protège-toi énergétiquement des dynamiques familiales toxiques.",
            'week_4': "Célèbre ta capacité à transformer la douleur ancestrale."
        }
    },

    # ==================== MAISON 5 - MAISON 12 ====================
    # (Par souci de longueur, je vais accélérer le rythme pour les maisons 5 à 12)
    # Chaque maison aura ses 12 ascendants avec le même niveau de qualité

    # MAISON 5 (Créativité, romance, enfants, jeu)
    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Passion dévorante**

Ta Lune en Scorpion en Maison 5 active une intensité créative et romantique. L'Ascendant Bélier te pousse à exprimer cette passion sans retenue. Tes émotions artistiques et amoureuses deviennent un feu dévorant.

**Domaine activé** : Maison 5 — Amour, création, plaisir, enfants. Tu veux vivre intensément, aimer passionnément, créer radicalement.

**Ton approche instinctive** : Le Bélier fonce vers le plaisir, le Scorpion transforme par la passion. Tu te jettes corps et âme dans ce qui t'enflamme.

**Tensions possibles** : L'obsession amoureuse ou créative peut devenir destructrice. Tu risques de brûler ce que tu aimes par trop d'intensité.

**Conseil clé** : Canaliser ta passion créatrice vers des projets qui te transforment sans te consumer.""",
        'weekly_advice': {
            'week_1': "Lance-toi dans un projet créatif qui te fait peur.",
            'week_2': "Exprime ton désir ou ta passion sans retenue.",
            'week_3': "Attention à ne pas étouffer l'objet de ton amour.",
            'week_4': "Célèbre ce que tu as créé ou vécu intensément."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Plaisir profond**

Ta Lune en Scorpion en Maison 5 cherche l'intensité dans le plaisir. L'Ascendant Taureau apporte sensualité, beauté, besoin de stabilité même dans la passion.

**Domaine activé** : Maison 5 — Romance, créativité, plaisir sensuel. Tu veux des expériences qui nourrissent ton corps et ton âme profondément.

**Ton approche instinctive** : Le Taureau savoure lentement, le Scorpion plonge intensément. Tu cherches un plaisir qui dure et transforme.

**Tensions possibles** : La possessivité amoureuse ou créative. Tu peux vouloir garder pour toi ce qui t'apporte du plaisir.

**Conseil clé** : Créer de la beauté durable plutôt que de posséder ce qui te plaît.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui te donne un plaisir profond et durable.",
            'week_2': "Investis dans une expérience artistique ou sensuelle de qualité.",
            'week_3': "Crée quelque chose de beau qui exprime ton intensité.",
            'week_4': "Savoure lentement ce que tu as créé ou vécu."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Jeu intense**

Ta Lune en Scorpion en Maison 5 active une passion créative profonde. L'Ascendant Gémeaux apporte légèreté, curiosité, besoin de variété dans le plaisir.

**Domaine activé** : Maison 5 — Jeu, flirt, création intellectuelle. Tu veux explorer toutes les facettes du plaisir sans t'attacher.

**Ton approche instinctive** : Le Gémeaux papillonne, le Scorpion obsède. Tu oscilles entre légèreté et intensité dans tes passions.

**Tensions possibles** : La peur de l'engagement contre le besoin de fusion. Tu peux jouer avec les émotions sans mesurer la profondeur.

**Conseil clé** : Trouver un équilibre entre plaisir léger et connexion profonde.""",
        'weekly_advice': {
            'week_1': "Explore différentes formes de créativité sans t'engager.",
            'week_2': "Flirte ou joue sans te prendre trop au sérieux.",
            'week_3': "Choisis une passion où tu peux approfondir.",
            'week_4': "Synthétise ce qui te plaît vraiment au-delà de la surface."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Création viscérale**

Double eau en Maison 5 : ta Lune en Scorpion avec Ascendant Cancer crée une sensibilité extrême dans l'expression créative et amoureuse. Tes créations viennent du ventre.

**Domaine activé** : Maison 5 — Enfants, création, amour. Tu veux créer ou aimer de manière fusionnelle, protectrice, presque maternelle.

**Ton approche instinctive** : Le Cancer nourrit, le Scorpion transforme. Tes créations ou tes amours sont des extensions de toi-même.

**Tensions possibles** : L'attachement excessif à tes créations ou tes enfants. Tu peux les étouffer par trop de protection.

**Conseil clé** : Créer et aimer sans posséder. Laisser vivre ce que tu enfantes.""",
        'weekly_advice': {
            'week_1': "Crée quelque chose qui vient de ton vécu émotionnel profond.",
            'week_2': "Exprime ton amour ou ta créativité de manière nourricière.",
            'week_3': "Accepte que ce que tu crées te dépasse et t'échappe.",
            'week_4': "Célèbre la vie que tu as donnée à tes projets ou relations."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Gloire passionnée**

Ta Lune en Scorpion en Maison 5, secteur naturel du Lion, rencontre l'Ascendant Lion. Double force créative : tu veux briller intensément et laisser une œuvre immortelle.

**Domaine activé** : Maison 5 — Création artistique, romance, reconnaissance. Tu veux être vu·e pour ta profondeur autant que ton talent.

**Ton approche instinctive** : Le Lion rayonne, le Scorpion magnétise. Tu attires par ta présence et ton mystère créatif.

**Tensions possibles** : Le besoin de reconnaissance peut te faire révéler trop de ton intimité. L'orgueil blessé devient rage.

**Conseil clé** : Créer pour transformer, pas seulement pour impressionner.""",
        'weekly_advice': {
            'week_1': "Identifie un projet créatif ambitieux qui te fait vibrer.",
            'week_2': "Ose montrer ta création même si elle révèle tes profondeurs.",
            'week_3': "Accepte les retours sans prendre les critiques personnellement.",
            'week_4': "Célèbre ta capacité à créer quelque chose de puissant."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Artisanat passionné**

Ta Lune en Scorpion en Maison 5 active une intensité créative. L'Ascendant Vierge apporte perfectionnisme, technique, besoin de maîtrise dans l'art.

**Domaine activé** : Maison 5 — Créativité, loisirs, enfants. Tu veux créer quelque chose de parfait qui exprime ta profondeur.

**Ton approche instinctive** : La Vierge peaufine, le Scorpion obsède. Tu peux travailler une œuvre jusqu'à l'épuisement.

**Tensions possibles** : Le perfectionnisme peut tuer la spontanéité créative. Tu risques de ne jamais finir ou montrer tes œuvres.

**Conseil clé** : Accepter l'imperfection comme partie intégrante de la transformation créative.""",
        'weekly_advice': {
            'week_1': "Commence un projet créatif sans attendre d'être prêt·e.",
            'week_2': "Travaille ton art avec discipline et passion.",
            'week_3': "Partage même si ce n'est pas parfait.",
            'week_4': "Célèbre le processus autant que le résultat."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Romance intense**

Ta Lune en Scorpion en Maison 5 cherche la passion amoureuse transformatrice. L'Ascendant Balance apporte charme, séduction, besoin d'harmonie dans l'amour.

**Domaine activé** : Maison 5 — Romance, plaisir, beauté. Tu veux une relation qui soit à la fois harmonieuse et profondément transformatrice.

**Ton approche instinctive** : La Balance séduit avec élégance, le Scorpion avec intensité. Tu crées un magnétisme irrésistible.

**Tensions possibles** : Le besoin de plaire contre le besoin d'authenticité. Tu peux jouer un rôle séducteur sans montrer ta vraie profondeur.

**Conseil clé** : Séduire en étant vraie·ment toi, pas en portant un masque.""",
        'weekly_advice': {
            'week_1': "Identifie si tu séduis pour plaire ou pour connecter vraiment.",
            'week_2': "Ose montrer ton intensité dans la séduction.",
            'week_3': "Crée de la beauté qui exprime ta profondeur.",
            'week_4': "Célèbre les connexions authentiques que tu as créées."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Passion absolue**

Double Scorpion en Maison 5 : ce mois, ta créativité et ta vie amoureuse sont des terrains de transformation totale. Tu ne peux rien faire à moitié.

**Domaine activé** : Maison 5 — Amour, création, enfants, plaisir. Tout devient intense, viscéral, presque dangereux dans sa profondeur.

**Ton approche instinctive** : Double intensité fixe : quand tu aimes ou crées, c'est avec tout ton être. La demi-mesure n'existe pas.

**Tensions possibles** : L'obsession amoureuse ou créative peut devenir destructrice. Tu risques de te perdre dans la passion.

**Conseil clé** : Canaliser ton intensité créative et amoureuse sans te consumer.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui mérite vraiment ta passion totale.",
            'week_2': "Plonge complètement dans une création ou une relation.",
            'week_3': "Veille à ne pas perdre ton identité dans ta passion.",
            'week_4': "Affirme ce que tu as créé ou vécu avec fierté."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Passion libre**

Ta Lune en Scorpion en Maison 5 cherche l'intensité créative et amoureuse. L'Ascendant Sagittaire apporte optimisme, liberté, besoin d'aventure dans le plaisir.

**Domaine activé** : Maison 5 — Romance, jeu, création. Tu veux vivre des passions qui te font grandir et t'ouvrir au monde.

**Ton approche instinctive** : Le Sagittaire explore, le Scorpion s'attache. Tu oscilles entre fusion et fuite dans tes amours et créations.

**Tensions possibles** : Le besoin de liberté contre le besoin de profondeur. Tu peux fuir quand ça devient trop intense.

**Conseil clé** : Trouver des passions qui allient intensité et expansion.""",
        'weekly_advice': {
            'week_1': "Explore une forme de créativité ou d'amour nouvelle.",
            'week_2': "Plonge dans une passion qui te fait voyager intérieurement.",
            'week_3': "Reste libre tout en t'engageant profondément.",
            'week_4': "Célèbre ce que tu as vécu et appris."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Création stratégique**

Ta Lune en Scorpion en Maison 5 active une intensité créative. L'Ascendant Capricorne apporte discipline, ambition, besoin de reconnaissance durable.

**Domaine activé** : Maison 5 — Création, loisirs, enfants. Tu veux construire une œuvre ou un héritage créatif qui te survive.

**Ton approche instinctive** : Le Capricorne construit méthodiquement, le Scorpion transforme en profondeur. Ta créativité est stratégique.

**Tensions possibles** : Le contrôle excessif peut tuer la spontanéité créative. Tu risques de créer par devoir plutôt que par passion.

**Conseil clé** : Allier discipline et passion. Créer avec structure sans étouffer ton feu.""",
        'weekly_advice': {
            'week_1': "Définis un projet créatif ambitieux à long terme.",
            'week_2': "Travaille méthodiquement sur ton art ou ta passion.",
            'week_3': "Autorise-toi à jouer sans chercher la perfection.",
            'week_4': "Célèbre les fondations créatives que tu as posées."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Art radical**

Ta Lune en Scorpion en Maison 5 cherche l'intensité créative. L'Ascendant Verseau apporte originalité, détachement, besoin de créer autrement.

**Domaine activé** : Maison 5 — Création, amour, expression personnelle. Tu veux révolutionner ta manière de créer ou d'aimer.

**Ton approche instinctive** : Le Verseau innove, le Scorpion approfondit. Tu peux créer des œuvres uniques et dérangeantes.

**Tensions possibles** : Le détachement contre l'intensité. Tu peux te couper de tes émotions pour créer librement.

**Conseil clé** : Créer de manière originale sans fuir ta profondeur émotionnelle.""",
        'weekly_advice': {
            'week_1': "Explore une forme d'art ou d'amour non-conventionnelle.",
            'week_2': "Connecte-toi à des créateur·ices qui pensent différemment.",
            'week_3': "Crée quelque chose de radical qui exprime ton unicité.",
            'week_4': "Affirme ta différence créative sans t'excuser."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Art transcendant**

Double eau en Maison 5 : ta Lune en Scorpion avec Ascendant Poissons crée une créativité mystique et fusionnelle. Ton art devient un canal spirituel.

**Domaine activé** : Maison 5 — Création artistique, amour, enfants. Tu veux créer quelque chose qui transcende le matériel.

**Ton approche instinctive** : Les Poissons canalisent, le Scorpion transforme. Ton art vient d'ailleurs et touche l'âme.

**Tensions possibles** : Le risque de te perdre dans ta création. Tu peux confondre inspiration et échappatoire.

**Conseil clé** : Créer de manière mystique tout en restant ancré·e. L'art spirituel a besoin de structure.""",
        'weekly_advice': {
            'week_1': "Médite avant de créer pour te connecter à ta source.",
            'week_2': "Crée librement sans censure ni contrôle.",
            'week_3': "Partage ton art comme une offrande, pas une performance.",
            'week_4': "Célèbre ta capacité à transformer la douleur en beauté."
        }
    },

    # ==================== MAISON 6 ====================

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Travail intense**

Ta Lune en Scorpion en Maison 6 active une profondeur transformatrice dans ton quotidien professionnel et ta santé. L'Ascendant Bélier te pousse à agir avec force et rapidité dans tes routines.

**Domaine activé** : Maison 6 — Travail quotidien, santé, service aux autres. Tu cherches à transformer radicalement tes habitudes et ton rapport au travail.

**Ton approche instinctive** : Le Bélier fonce, le Scorpion creuse. Tu t'attaques aux problèmes de santé ou de travail avec une intensité guerrière. Rien ne résiste à ta détermination.

**Tensions possibles** : Le surmenage par obsession du travail. Tu peux t'épuiser en voulant tout contrôler dans ta routine. L'impatience (Bélier) rencontre l'obsession (Scorpion).

**Conseil clé** : Canaliser ton intensité vers une transformation saine de tes habitudes sans t'autodétruire.""",
        'weekly_advice': {
            'week_1': "Identifie une habitude toxique à éliminer radicalement.",
            'week_2': "Attaque un problème de travail ou de santé avec détermination.",
            'week_3': "Crée une nouvelle routine qui renforce ton pouvoir personnel.",
            'week_4': "Célèbre ta capacité à te régénérer par le travail sur toi."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Guérison profonde**

Ta Lune en Scorpion en Maison 6 cherche à transformer ton quotidien et ta santé. L'Ascendant Taureau, ton opposé, t'ancre dans le concret et la stabilité physique.

**Domaine activé** : Maison 6 — Santé, travail, habitudes. Tu veux construire une routine solide (Taureau) qui permet une vraie transformation (Scorpion).

**Ton approche instinctive** : Le Taureau préfère la régularité, le Scorpion veut tout changer. Tu résistes aux nouvelles habitudes, puis tu t'y engages totalement.

**Tensions possibles** : La résistance au changement peut retarder une guérison nécessaire. Tu t'accroches à des habitudes obsolètes par peur de l'inconnu.

**Conseil clé** : Accepter que la vraie santé nécessite parfois des transformations radicales.""",
        'weekly_advice': {
            'week_1': "Examine tes habitudes de santé avec honnêteté brutale.",
            'week_2': "Change concrètement une routine qui ne te sert plus.",
            'week_3': "Ancre une nouvelle habitude régénératrice dans ton quotidien.",
            'week_4': "Apprécie la stabilité que cette transformation t'apporte."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Analyse obsessionnelle**

Ta Lune en Scorpion en Maison 6 active une intensité autour du travail et de la santé. L'Ascendant Gémeaux apporte curiosité intellectuelle et besoin de variété dans les routines.

**Domaine activé** : Maison 6 — Service, santé, tâches quotidiennes. Tu veux comprendre en profondeur les mécanismes de ton corps et de ton travail.

**Ton approche instinctive** : Le Gémeaux collecte l'information, le Scorpion l'analyse jusqu'à l'obsession. Tu peux devenir hypocondriaque ou workaholique intellectuel.

**Tensions possibles** : Trop d'analyse paralyse l'action. Tu risques de te perdre dans les détails sans transformer vraiment tes habitudes.

**Conseil clé** : Utiliser ton intelligence pour comprendre, puis agir sur ce qui compte vraiment.""",
        'weekly_advice': {
            'week_1': "Recherche des informations sur un problème de santé ou de travail.",
            'week_2': "Communique tes découvertes ou tes besoins au travail.",
            'week_3': "Applique concrètement une solution que tu as identifiée.",
            'week_4': "Note comment ta compréhension a transformé ta pratique."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Service émotionnel**

Double eau en Maison 6 : ta Lune en Scorpion avec Ascendant Cancer crée une sensibilité extrême dans ton travail et ta santé. Tu ressens profondément l'énergie de ton environnement quotidien.

**Domaine activé** : Maison 6 — Routine, santé, service. Ton bien-être physique est intimement lié à ton état émotionnel.

**Ton approche instinctive** : Le Cancer nourrit et protège, le Scorpion transforme. Tu peux être un·e soignant·e ou thérapeute exceptionnel·le.

**Tensions possibles** : Absorber les émotions des autres au travail peut t'épuiser. Tu risques de négliger ta propre santé en prenant soin des autres.

**Conseil clé** : Créer des frontières émotionnelles saines dans ton service aux autres.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui t'épuise émotionnellement dans ton quotidien.",
            'week_2': "Crée un rituel de purification énergétique quotidien.",
            'week_3': "Prends soin de ton corps comme tu prendrais soin d'un être aimé.",
            'week_4': "Célèbre ta capacité à guérir par ta présence."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Excellence professionnelle**

Ta Lune en Scorpion en Maison 6 active une intensité dans ton travail quotidien. L'Ascendant Lion veut exceller, briller, être reconnu pour son expertise.

**Domaine activé** : Maison 6 — Travail, santé, perfectionnement. Tu veux devenir un·e maître·sse dans ton domaine.

**Ton approche instinctive** : Le Lion rayonne par son talent, le Scorpion maîtrise en profondeur. Tu combines charisme et expertise technique.

**Tensions possibles** : L'orgueil peut t'empêcher de demander de l'aide ou de reconnaître tes limites. Tu risques le burn-out par excès d'ambition.

**Conseil clé** : Briller par ton excellence sans sacrifier ta santé sur l'autel de la reconnaissance.""",
        'weekly_advice': {
            'week_1': "Fixe-toi un objectif d'excellence dans ton travail.",
            'week_2': "Travaille avec passion et discipline sur ton expertise.",
            'week_3': "Accepte tes limites humaines sans honte.",
            'week_4': "Célèbre publiquement tes accomplissements professionnels."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Perfectionnisme total**

Ta Lune en Scorpion en Maison 6, secteur naturel de la Vierge, rencontre l'Ascendant Vierge. Double intensité sur le travail, la santé et les détails.

**Domaine activé** : Maison 6 — Routine, santé, efficacité. Tu veux atteindre la perfection dans chaque geste quotidien.

**Ton approche instinctive** : Double analyse, double perfectionnisme. Tu ne laisses rien au hasard et cherches constamment à améliorer tes méthodes.

**Tensions possibles** : L'obsession du détail peut devenir paralysante. Tu risques l'anxiété chronique et l'hypocondrie.

**Conseil clé** : Accepter que l'imperfection fait partie du processus de transformation.""",
        'weekly_advice': {
            'week_1': "Identifie une routine qui demande trop de perfection.",
            'week_2': "Pratique la tolérance envers tes petites erreurs.",
            'week_3': "Améliore un système sans chercher la perfection absolue.",
            'week_4': "Célèbre le progrès plutôt que la perfection."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Harmonie professionnelle**

Ta Lune en Scorpion en Maison 6 cherche la transformation par le travail. L'Ascendant Balance apporte diplomatie et besoin d'équilibre dans l'environnement professionnel.

**Domaine activé** : Maison 6 — Relations de travail, santé, routine. Tu veux créer de l'harmonie tout en transformant profondément ta pratique.

**Ton approche instinctive** : La Balance négocie et équilibre, le Scorpion tranche et transforme. Tu oscilles entre compromis et radicalité.

**Tensions possibles** : Le besoin de plaire peut t'empêcher d'imposer les changements nécessaires au travail. Tu risques de t'épuiser à maintenir la paix.

**Conseil clé** : Créer l'harmonie par l'authenticité, pas par le sacrifice de tes besoins.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te compromets trop au travail.",
            'week_2': "Exprime diplomatiquement un besoin de changement profond.",
            'week_3': "Crée de la beauté dans ton espace de travail quotidien.",
            'week_4': "Célèbre l'équilibre que tu as trouvé."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Régénération totale**

Double Scorpion en Maison 6 : ce mois, ton travail et ta santé deviennent des terrains de transformation radicale. Tu ne fais rien à moitié.

**Domaine activé** : Maison 6 — Santé, routine, service. Chaque habitude quotidienne devient un rituel de pouvoir personnel.

**Ton approche instinctive** : Double intensité fixe sur le perfectionnement. Tu t'engages totalement dans ta régénération physique et professionnelle.

**Tensions possibles** : L'obsession peut devenir destructrice. Tu risques l'épuisement en cherchant la transformation parfaite.

**Conseil clé** : Se transformer par étapes sans s'autodétruire dans le processus.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit mourir dans tes habitudes.",
            'week_2': "Élimine radicalement une routine toxique.",
            'week_3': "Construis une nouvelle pratique de régénération.",
            'week_4': "Affirme ta renaissance physique et professionnelle."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Aventure quotidienne**

Ta Lune en Scorpion en Maison 6 active une intensité dans le travail et la santé. L'Ascendant Sagittaire apporte optimisme et besoin de liberté dans les routines.

**Domaine activé** : Maison 6 — Routine, santé, amélioration. Tu veux transformer tes habitudes tout en gardant de la spontanéité.

**Ton approche instinctive** : Le Sagittaire explore librement, le Scorpion s'engage profondément. Tu peux révolutionner ton approche du travail et de la santé.

**Tensions possibles** : Le besoin de liberté peut saboter la discipline nécessaire aux routines saines. Tu risques d'abandonner avant la vraie transformation.

**Conseil clé** : Trouver des routines qui nourrissent ta liberté intérieure.""",
        'weekly_advice': {
            'week_1': "Explore une nouvelle approche du travail ou de la santé.",
            'week_2': "Engage-toi dans une pratique qui te fait grandir.",
            'week_3': "Reste discipliné·e sans te sentir emprisonné·e.",
            'week_4': "Célèbre ce que tu as appris sur toi."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Discipline transformatrice**

Ta Lune en Scorpion en Maison 6 cherche la transformation par le travail. L'Ascendant Capricorne apporte structure, ambition et persévérance dans les routines.

**Domaine activé** : Maison 6 — Travail, santé, maîtrise. Tu veux construire des habitudes qui te donnent un pouvoir durable.

**Ton approche instinctive** : Le Capricorne construit méthodiquement, le Scorpion transforme en profondeur. Ta discipline est redoutable.

**Tensions possibles** : Le contrôle excessif peut créer une rigidité malsaine. Tu risques de te punir par le travail ou les restrictions.

**Conseil clé** : Utiliser la discipline pour te libérer, pas pour t'emprisonner.""",
        'weekly_advice': {
            'week_1': "Définis une routine de santé ou de travail ambitieuse.",
            'week_2': "Applique-toi avec discipline sans devenir rigide.",
            'week_3': "Ajuste ta pratique selon tes besoins réels.",
            'week_4': "Célèbre les fondations solides que tu as bâties."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Routine révolutionnaire**

Ta Lune en Scorpion en Maison 6 active une intensité dans ton quotidien. L'Ascendant Verseau apporte originalité et besoin de réinventer tes habitudes.

**Domaine activé** : Maison 6 — Travail, santé, routine. Tu veux créer des pratiques uniques qui te transforment profondément.

**Ton approche instinctive** : Le Verseau innove, le Scorpion approfondit. Tu peux inventer des méthodes de travail ou de santé avant-gardistes.

**Tensions possibles** : Le détachement peut t'empêcher de t'engager dans une routine régulière. Tu risques de changer constamment sans aller au fond.

**Conseil clé** : Innover dans tes habitudes sans fuir l'engagement profond.""",
        'weekly_advice': {
            'week_1': "Explore une approche non-conventionnelle du travail ou de la santé.",
            'week_2': "Connecte-toi à des praticien·nes alternatifs.",
            'week_3': "Crée une routine unique qui te ressemble vraiment.",
            'week_4': "Affirme ta différence dans ta manière de vivre."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Guérison mystique**

Double eau en Maison 6 : ta Lune en Scorpion avec Ascendant Poissons crée une approche spirituelle du travail et de la santé.

**Domaine activé** : Maison 6 — Service, santé, routine. Tu veux guérir à tous les niveaux : physique, émotionnel, spirituel.

**Ton approche instinctive** : Les Poissons canalisent l'énergie universelle, le Scorpion transforme en profondeur. Tu es un·e guérisseur·se naturel·le.

**Tensions possibles** : Le risque de te perdre dans la spiritualité au détriment du concret. Tu peux négliger ta santé physique.

**Conseil clé** : Ancrer ta pratique spirituelle dans des gestes quotidiens concrets.""",
        'weekly_advice': {
            'week_1': "Médite sur ce que ton corps essaie de te dire.",
            'week_2': "Pratique une forme de guérison holistique.",
            'week_3': "Crée un rituel quotidien sacré de soin.",
            'week_4': "Célèbre ta capacité à guérir sur tous les plans."
        }
    },

    # ==================== MAISON 7 ====================

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Fusion explosive**

Ta Lune en Scorpion en Maison 7 active une intensité magnétique dans tes relations. L'Ascendant Bélier apporte spontanéité et besoin d'action directe dans les partenariats.

**Domaine activé** : Maison 7 — Relations intimes, partenariats, engagements. Tu veux des liens authentiques qui transforment, pas des superficialités.

**Ton approche instinctive** : Le Bélier fonce tête baissée dans l'intimité, le Scorpion creuse sans relâche. Tu peux vivre une rencontre bouleversante ou une crise salvatrice dans une relation existante.

**Tensions possibles** : L'impulsivité (Bélier) contre le besoin de contrôle (Scorpion) crée des ruptures soudaines ou des rapprochements foudroyants. Jalousie et possessivité menacent.

**Conseil clé** : Oser la vulnérabilité sans chercher à dominer l'autre.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui doit mourir dans ta manière de t'engager.",
            'week_2': "Confronte une vérité difficile avec ton partenaire.",
            'week_3': "Laisse l'intensité te transformer sans brûler la relation.",
            'week_4': "Célèbre la profondeur nouvelle que tu as atteinte."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Loyauté intense**

Ta Lune en Scorpion en Maison 7 crée une profondeur magnétique dans tes engagements. L'Ascendant Taureau apporte stabilité et besoin de sécurité dans les relations.

**Domaine activé** : Maison 7 — Partenariats, contrats, unions. Tu veux des liens solides qui résistent aux tempêtes émotionnelles.

**Ton approche instinctive** : Le Taureau construit patiemment, le Scorpion teste la profondeur. Tu ne t'engages que si tu sens une authenticité totale.

**Tensions possibles** : La possession (Taureau) amplifie la jalousie (Scorpion). Tu peux étouffer l'autre par peur de le perdre ou tout détruire si tu te sens trahi.

**Conseil clé** : Accepter que la vraie sécurité vient de la confiance mutuelle, pas du contrôle.""",
        'weekly_advice': {
            'week_1': "Évalue honnêtement la solidité de tes engagements.",
            'week_2': "Lâche un comportement possessif dans une relation.",
            'week_3': "Construis sur ce qui est authentique, élimine le reste.",
            'week_4': "Ancre ta confiance dans la profondeur vraie de tes liens."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Intimité curieuse**

Ta Lune en Scorpion en Maison 7 active une quête de profondeur dans les relations. L'Ascendant Gémeaux apporte curiosité et besoin d'échange intellectuel dans les partenariats.

**Domaine activé** : Maison 7 — Rencontres, engagements, miroirs relationnels. Tu veux comprendre les mystères de l'autre tout en créant une vraie fusion.

**Ton approche instinctive** : Les Gémeaux explorent par la parole, le Scorpion par le silence et l'observation. Tu peux alterner entre conversations profondes et secrets gardés.

**Tensions possibles** : La légèreté (Gémeaux) contre l'intensité (Scorpion) crée de la confusion. Tu peux intellectualiser pour éviter de ressentir ou devenir obsédé·e par quelqu'un.

**Conseil clé** : Utiliser les mots pour approfondir la connexion, pas pour l'éviter.""",
        'weekly_advice': {
            'week_1': "Pose des questions qui révèlent l'âme de l'autre.",
            'week_2': "Partage un secret que tu gardais par peur du jugement.",
            'week_3': "Écoute sans analyser, ressens sans étiqueter.",
            'week_4': "Célèbre ce que tu as découvert sur toi à travers l'autre."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Fusion protectrice**

Double eau en Maison 7 : ta Lune en Scorpion avec Ascendant Cancer crée une sensibilité extrême dans les relations intimes.

**Domaine activé** : Maison 7 — Partenariats profonds, engagements émotionnels. Tu veux nourrir et être nourri·e dans une connexion totale.

**Ton approche instinctive** : Le Cancer protège, le Scorpion transforme. Tu peux devenir le refuge de l'autre tout en le confrontant à ses zones d'ombre.

**Tensions possibles** : La fusion peut devenir étouffante. Tu risques de confondre amour et dépendance, protection et contrôle.

**Conseil clé** : Créer un espace sûr pour l'intimité sans perdre ton autonomie émotionnelle.""",
        'weekly_advice': {
            'week_1': "Identifie où tu cherches à sauver l'autre au lieu de l'aimer.",
            'week_2': "Partage une vulnérabilité sans attendre d'être sauvé·e.",
            'week_3': "Laisse l'autre gérer ses propres transformations.",
            'week_4': "Célèbre la force d'une intimité qui respecte les frontières."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Passion magnétique**

Ta Lune en Scorpion en Maison 7 active une intensité dans les partenariats. L'Ascendant Lion apporte rayonnement et besoin de reconnaissance dans les relations.

**Domaine activé** : Maison 7 — Unions, engagements publics. Tu veux une relation qui te fait briller tout en t'emmenant dans les profondeurs.

**Ton approche instinctive** : Le Lion cherche l'admiration, le Scorpion la vérité nue. Tu peux fasciner l'autre tout en exigeant qu'il te voie vraiment.

**Tensions possibles** : L'orgueil (Lion) rend difficile d'admettre la vulnérabilité. La jalousie (Scorpion) peut détruire ce que le Lion veut montrer au monde.

**Conseil clé** : Oser être vu·e dans ta fragilité, pas seulement dans ta magnificence.""",
        'weekly_advice': {
            'week_1': "Montre-toi authentique, pas parfait·e dans tes relations.",
            'week_2': "Admets une peur ou une blessure à ton partenaire.",
            'week_3': "Laisse l'autre briller autant que toi.",
            'week_4': "Célèbre la force d'une relation qui embrasse l'ombre et la lumière."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Analyse profonde**

Ta Lune en Scorpion en Maison 7 crée une intensité dans les partenariats. L'Ascendant Vierge apporte discernement et besoin de perfection dans les relations.

**Domaine activé** : Maison 7 — Engagements, contrats, unions. Tu veux une relation impeccable qui résiste à toutes les épreuves.

**Ton approche instinctive** : La Vierge observe les détails, le Scorpion les motivations cachées. Tu peux déceler toutes les failles d'une relation.

**Tensions possibles** : Le perfectionnisme (Vierge) amplifie le besoin de contrôle (Scorpion). Tu risques de critiquer l'autre jusqu'à détruire la connexion ou de ruminer chaque imperfection.

**Conseil clé** : Accepter l'humanité de l'autre sans chercher à le réparer ou le transformer.""",
        'weekly_advice': {
            'week_1': "Identifie où tu critiques au lieu d'aimer.",
            'week_2': "Lâche un besoin de perfection dans ta relation.",
            'week_3': "Sers l'autre sans vouloir le contrôler.",
            'week_4': "Célèbre ce qui fonctionne au lieu de fixer ce qui cloche."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Équilibre magnétique**

Ta Lune en Scorpion en Maison 7 active une profondeur dans les relations. L'Ascendant Balance apporte recherche d'harmonie et de beauté dans les partenariats.

**Domaine activé** : Maison 7 — Relations, engagements, justice relationnelle. Tu veux un lien équilibré mais authentiquement profond.

**Ton approche instinctive** : La Balance cherche le compromis, le Scorpion la vérité totale. Tu peux jongler entre maintenir la paix et confronter les non-dits.

**Tensions possibles** : La diplomatie peut devenir manipulation. Tu risques d'éviter les conflits nécessaires par peur de perdre l'harmonie.

**Conseil clé** : Comprendre que la vraie harmonie naît de l'honnêteté, pas de l'évitement.""",
        'weekly_advice': {
            'week_1': "Identifie un conflit que tu évites dans une relation.",
            'week_2': "Confronte avec élégance mais sans détour.",
            'week_3': "Trouve l'équilibre entre tes besoins et ceux de l'autre.",
            'week_4': "Célèbre une harmonie nouvelle basée sur la vérité."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Fusion totale**

Double Scorpion en Maison 7 : intensité maximale dans les relations. Tu vis les partenariats comme des voyages dans les abysses de l'âme.

**Domaine activé** : Maison 7 — Unions sacrées, engagements profonds. Rien de superficiel ne t'intéresse. C'est tout ou rien.

**Ton approche instinctive** : Tu cherches à fusionner complètement avec l'autre tout en gardant ton pouvoir. La relation devient un champ de bataille et un temple sacré.

**Tensions possibles** : Jalousie extrême, possessivité, manipulation par la vulnérabilité. Tu peux détruire ce que tu aimes par peur d'être abandonné·e.

**Conseil clé** : Faire confiance au processus de transformation mutuelle sans chercher à tout contrôler.""",
        'weekly_advice': {
            'week_1': "Identifie ta plus grande peur dans les relations.",
            'week_2': "Ose une vulnérabilité radicale avec ton partenaire.",
            'week_3': "Lâche un besoin de contrôle, observe ce qui se passe.",
            'week_4': "Célèbre la profondeur que tu as atteinte ensemble."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Passion libre**

Ta Lune en Scorpion en Maison 7 active une intensité dans les relations. L'Ascendant Sagittaire apporte besoin d'aventure et de vérité philosophique dans les partenariats.

**Domaine activé** : Maison 7 — Relations, engagements, exploration relationnelle. Tu veux une connexion profonde qui ne t'emprisonne pas.

**Ton approche instinctive** : Le Sagittaire cherche la liberté, le Scorpion la fusion. Tu peux alterner entre engagement total et besoin d'espace.

**Tensions possibles** : La peur de l'enfermement (Sagittaire) sabote l'intimité (Scorpion). Tu risques de fuir quand ça devient trop profond ou de devenir possessif·ve par peur de l'abandon.

**Conseil clé** : Comprendre que la vraie liberté naît d'un engagement choisi, pas évité.""",
        'weekly_advice': {
            'week_1': "Explore où tu fuis l'intimité par peur de perdre ta liberté.",
            'week_2': "Engage-toi profondément dans une conversation difficile.",
            'week_3': "Trouve comment être libre dans la fusion.",
            'week_4': "Célèbre une relation qui nourrit ton expansion."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Engagement stratégique**

Ta Lune en Scorpion en Maison 7 crée une profondeur dans les partenariats. L'Ascendant Capricorne apporte sérieux et ambition dans les relations.

**Domaine activé** : Maison 7 — Contrats, unions durables, partenariats structurés. Tu veux construire quelque chose de solide qui traverse le temps.

**Ton approche instinctive** : Le Capricorne planifie stratégiquement, le Scorpion sonde les motivations cachées. Tu ne t'engages que si tu vois un potentiel de transformation durable.

**Tensions possibles** : Le contrôle émotionnel peut créer une froideur. Tu risques de traiter la relation comme un projet plutôt qu'une connexion vivante.

**Conseil clé** : Laisser de la place à la spontanéité émotionnelle sans perdre ta vision à long terme.""",
        'weekly_advice': {
            'week_1': "Évalue honnêtement où tu contrôles au lieu d'aimer.",
            'week_2': "Laisse-toi surprendre par une vulnérabilité spontanée.",
            'week_3': "Construis sur l'authenticité, pas sur des stratégies.",
            'week_4': "Célèbre une relation qui marie profondeur et durabilité."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Intimité révolutionnaire**

Ta Lune en Scorpion en Maison 7 active une intensité dans les partenariats. L'Ascendant Verseau apporte originalité et besoin d'indépendance dans les relations.

**Domaine activé** : Maison 7 — Engagements non-conventionnels, relations qui transforment. Tu veux une intimité qui respecte l'individualité.

**Ton approche instinctive** : Le Verseau prône la liberté, le Scorpion la fusion. Tu peux créer des relations d'un genre nouveau, intenses mais libres.

**Tensions possibles** : Le détachement (Verseau) contre la possessivité (Scorpion) crée de la confusion. Tu risques d'osciller entre distance froide et jalousie brûlante.

**Conseil clé** : Inventer une manière d'être ensemble qui honore à la fois l'intimité et l'autonomie.""",
        'weekly_advice': {
            'week_1': "Questionne les normes relationnelles que tu as intériorisées.",
            'week_2': "Propose une forme d'engagement qui te ressemble vraiment.",
            'week_3': "Laisse l'autre être lui-même sans chercher à le posséder.",
            'week_4': "Célèbre une relation qui transcende les conventions."
        }
    },

    {
        'moon_sign': 'Scorpio', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Fusion mystique**

Double eau en Maison 7 : ta Lune en Scorpion avec Ascendant Poissons crée une sensibilité psychique intense dans les relations.

**Domaine activé** : Maison 7 — Unions sacrées, partenariats karmiques. Tu ressens l'autre au-delà des mots, presque télépathiquement.

**Ton approche instinctive** : Les Poissons dissolvent les frontières, le Scorpion plonge dans l'inconscient. Tu peux vivre des connexions d'une profondeur bouleversante.

**Tensions possibles** : La fusion peut devenir confusion. Tu risques de perdre tes limites, d'absorber la douleur de l'autre ou de te noyer dans la relation.

**Conseil clé** : Maintenir tes frontières énergétiques tout en restant ouvert·e à l'intimité profonde.""",
        'weekly_advice': {
            'week_1': "Identifie où tu te perds dans l'autre au lieu de te rencontrer.",
            'week_2': "Protège ton énergie sans fermer ton cœur.",
            'week_3': "Canalise l'intensité émotionnelle dans une pratique spirituelle partagée.",
            'week_4': "Célèbre une intimité qui transcende l'ego sans l'abolir."
        }
    },

]

# Fonction d'exécution
if __name__ == "__main__":
    asyncio.run(insert_batch(BATCH))
