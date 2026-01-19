#!/usr/bin/env python3
"""Insert North Node interpretations for Aries, Taurus, Gemini, Cancer (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_nn_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'aries': '☊ Nœud Nord en Bélier',
        'taurus': '☊ Nœud Nord en Taureau',
        'gemini': '☊ Nœud Nord en Gémeaux',
        'cancer': '☊ Nœud Nord en Cancer',
    }
    sign_fr = {
        'aries': 'Bélier',
        'taurus': 'Taureau',
        'gemini': 'Gémeaux',
        'cancer': 'Cancer',
    }
    return f"""# {sign_titles[sign_name]}

**En une phrase :** {phrase}

## Ton moteur
{moteur}

## Ton défi
{defi}

## Maison {house} en {sign_fr[sign_name]}
{maison_desc}

## Micro-rituel du jour (2 min)
- {ritual_action}
- {ritual_breath}
- Journal : « {ritual_journal} »"""

NORTH_NODE_INTERPRETATIONS = {
    # === ARIES (M1-M12) ===
    ('aries', 1): make_nn_interp('aries', 1,
        "Ton chemin d'âme t'appelle à devenir une personne courageuse et affirmée.",
        "Le Nœud Nord en Bélier dans ta maison I t'invite à développer ton identité propre avec courage. Tu quittes l'équilibre excessif de la Balance (Nœud Sud) pour apprendre à t'affirmer.",
        "Oser prendre des initiatives seul(e) sans attendre l'approbation des autres. Ta tendance à chercher l'harmonie relationnelle te retient — ton évolution passe par l'action indépendante.",
        "Ta présence physique et ton identité sont le terrain de ton évolution karmique. Tu dois oser être visible, prendre ta place, affirmer qui tu es sans compromis.",
        "Dis à voix haute : « J'ose être moi-même, sans permission. »",
        "Respire en gonflant ta poitrine, comme un guerrier qui se prépare.",
        "Quelle action courageuse ai-je évitée par peur du conflit ou du jugement ? »"),

    ('aries', 2): make_nn_interp('aries', 2,
        "Ton chemin d'âme t'appelle à conquérir tes propres ressources avec audace.",
        "Le Nœud Nord en Bélier dans ta maison II t'invite à développer ton indépendance financière. Tu quittes la dépendance aux ressources des autres pour créer ta propre valeur.",
        "Oser entreprendre seul(e) et valoriser tes talents uniques. Ta tendance passée à dépendre financièrement des partenaires ou des héritages te freine.",
        "Tes finances sont le terrain de ton courage. Tu apprends à générer tes propres revenus, à prendre des risques calculés, à te faire confiance dans le domaine matériel.",
        "Identifie une compétence que tu n'as jamais monétisée et envisage de le faire.",
        "Respire en visualisant l'énergie de l'argent qui vient de TES propres actions.",
        "Quelle peur financière me retient de créer ma propre abondance ? »"),

    ('aries', 3): make_nn_interp('aries', 3,
        "Ton chemin d'âme t'appelle à communiquer avec courage et authenticité.",
        "Le Nœud Nord en Bélier dans ta maison III t'invite à développer une parole directe et affirmée. Tu quittes les grandes philosophies pour l'expression concrète de ta vérité.",
        "Oser dire ce que tu penses vraiment sans tourner autour du pot. Ta tendance à intellectualiser ou à rester dans l'abstrait te retient de l'expression directe.",
        "Ta communication quotidienne est le terrain de ton courage. Tu apprends à affirmer tes opinions dans les discussions, avec tes frères, sœurs, voisins.",
        "Dis une chose que tu penses vraiment, sans l'enrober de diplomatie.",
        "Respire en sentant les mots directs qui montent de ton ventre.",
        "Quelle vérité ai-je besoin d'exprimer sans filtre diplomatique ? »"),

    ('aries', 4): make_nn_interp('aries', 4,
        "Ton chemin d'âme t'appelle à créer un foyer par ta propre initiative.",
        "Le Nœud Nord en Bélier dans ta maison IV t'invite à développer l'autonomie dans ta vie privée. Tu quittes la dépendance à la carrière ou au statut pour construire TES racines.",
        "Oser prendre des décisions familiales sans consensus permanent. Ta tendance à attendre l'approbation ou à te conformer aux attentes publiques te freine.",
        "Ton foyer est le terrain de ton courage. Tu dois oser créer une vie privée qui te ressemble, même si elle déplaît à certains.",
        "Prends une décision concernant ton logement ou ta famille sans demander d'avis.",
        "Respire en visualisant un foyer qui est UNIQUEMENT à ton image.",
        "Quelle décision familiale ai-je reportée par peur de déplaire ? »"),

    ('aries', 5): make_nn_interp('aries', 5,
        "Ton chemin d'âme t'appelle à créer et aimer avec courage et passion.",
        "Le Nœud Nord en Bélier dans ta maison V t'invite à développer ta créativité audacieuse et tes amours passionnées. Tu quittes la sécurité du groupe pour briller individuellement.",
        "Oser créer quelque chose d'original et aimer avec intensité. Ta tendance à te fondre dans le collectif ou à craindre l'attention te retient.",
        "Ta créativité et tes amours sont le terrain de ton courage. Tu apprends à être un créateur unique, un amant passionné, un parent qui affirme son style.",
        "Crée quelque chose de personnel et audacieux, sans chercher l'approbation du groupe.",
        "Respire en ressentant le feu créatif qui brûle dans ta poitrine.",
        "Quelle création audacieuse ai-je peur de montrer au monde ? »"),

    ('aries', 6): make_nn_interp('aries', 6,
        "Ton chemin d'âme t'appelle à travailler avec initiative et à défendre ta santé.",
        "Le Nœud Nord en Bélier dans ta maison VI t'invite à développer l'autonomie dans ton travail quotidien et ta santé. Tu quittes le sacrifice pour les autres pour prendre soin de toi.",
        "Oser prendre des initiatives au travail et mettre ta santé en priorité. Ta tendance au sacrifice ou à l'évasion te freine dans ton évolution quotidienne.",
        "Ton travail et ta santé sont le terrain de ton courage. Tu apprends à dire non, à défendre tes limites, à prendre les devants.",
        "Prends une initiative au travail sans attendre qu'on te le demande.",
        "Respire en visualisant ton corps comme un guerrier que tu dois entraîner.",
        "Quelle habitude de santé ai-je négligée par manque d'initiative ? »"),

    ('aries', 7): make_nn_interp('aries', 7,
        "Ton chemin d'âme t'appelle à t'affirmer dans tes relations.",
        "Le Nœud Nord en Bélier dans ta maison VII t'invite à développer le courage relationnel. Tu quittes l'excès d'autonomie solitaire pour apprendre à t'affirmer DANS les relations.",
        "Oser montrer qui tu es vraiment dans le couple et les partenariats. Ta tendance à l'indépendance excessive ou à éviter l'engagement te freine.",
        "Tes relations sont le terrain de ton courage. Tu apprends à t'engager, à défendre tes besoins face à l'autre, à être authentique en couple.",
        "Exprime un besoin ou une opinion à un partenaire, clairement et sans excuse.",
        "Respire en visualisant des relations où tu es pleinement toi-même.",
        "Qu'ai-je peur de demander ou d'affirmer dans mes relations ? »"),

    ('aries', 8): make_nn_interp('aries', 8,
        "Ton chemin d'âme t'appelle à plonger courageusement dans les transformations.",
        "Le Nœud Nord en Bélier dans ta maison VIII t'invite à développer le courage face aux crises et aux ressources partagées. Tu quittes la sécurité matérielle pour la transformation profonde.",
        "Oser traverser les crises avec audace et prendre des risques dans l'intimité. Ta tendance à t'accrocher à la sécurité ou aux possessions te freine.",
        "Les transformations profondes sont le terrain de ton courage. Tu apprends à mourir et renaître, à risquer dans l'intimité, à partager tes ressources.",
        "Identifie une peur profonde et fais un pas vers elle aujourd'hui.",
        "Respire en accueillant la transformation comme une bataille à mener courageusement.",
        "Quelle transformation évité-je par peur de perdre ma sécurité ? »"),

    ('aries', 9): make_nn_interp('aries', 9,
        "Ton chemin d'âme t'appelle à explorer tes propres croyances avec audace.",
        "Le Nœud Nord en Bélier dans ta maison IX t'invite à développer ta propre philosophie avec courage. Tu quittes l'accumulation d'informations pour forger TES convictions.",
        "Oser avoir tes propres opinions spirituelles et les défendre. Ta tendance à collecter des savoirs sans te positionner te freine dans ta quête de sens.",
        "Ta spiritualité et tes voyages sont le terrain de ton courage. Tu apprends à explorer par toi-même, à affirmer ta vérité, à prendre des risques dans l'inconnu.",
        "Affirme une croyance personnelle, même si elle est impopulaire.",
        "Respire en visualisant un horizon que TOI SEUL(E) choisis d'explorer.",
        "Quelle vérité spirituelle ai-je peur d'affirmer par peur du jugement ? »"),

    ('aries', 10): make_nn_interp('aries', 10,
        "Ton chemin d'âme t'appelle à devenir un leader dans ta carrière.",
        "Le Nœud Nord en Bélier dans ta maison X t'invite à développer l'ambition et le leadership. Tu quittes la sécurité du foyer pour conquérir ta place publique.",
        "Oser prendre des initiatives professionnelles et viser les positions de pouvoir. Ta tendance à rester dans l'ombre ou à privilégier la vie privée te freine.",
        "Ta carrière est le terrain de ton courage. Tu apprends à diriger, à te montrer, à assumer une position visible et à prendre des décisions audacieuses.",
        "Prends une initiative professionnelle ambitieuse que tu reportais.",
        "Respire en visualisant ta place au sommet de ta carrière.",
        "Quelle ambition professionnelle ai-je peur de poursuivre ? »"),

    ('aries', 11): make_nn_interp('aries', 11,
        "Ton chemin d'âme t'appelle à initier des projets collectifs.",
        "Le Nœud Nord en Bélier dans ta maison XI t'invite à développer le leadership dans les groupes. Tu quittes l'attention sur toi-même pour inspirer et initier dans le collectif.",
        "Oser prendre la tête de projets et défendre tes idéaux avec conviction. Ta tendance à rester centré sur toi ou à créer seul te freine.",
        "Tes amitiés et projets collectifs sont le terrain de ton courage. Tu apprends à être un pionnier social, à lancer des mouvements, à inspirer les autres.",
        "Propose un projet ou une idée à un groupe, sans attendre qu'on te sollicite.",
        "Respire en visualisant un cercle d'amis que TU inspires.",
        "Quel projet collectif ai-je peur d'initier ou de proposer ? »"),

    ('aries', 12): make_nn_interp('aries', 12,
        "Ton chemin d'âme t'appelle à affronter tes peurs avec courage.",
        "Le Nœud Nord en Bélier dans ta maison XII t'invite à développer le courage spirituel face à l'inconnu. Tu quittes le contrôle quotidien pour plonger dans l'invisible.",
        "Oser affronter tes démons intérieurs avec la bravoure d'un guerrier. Ta tendance à tout rationaliser ou à rester dans le monde visible te freine.",
        "L'inconscient et le monde spirituel sont le terrain de ton courage. Tu apprends à méditer, à confronter tes ombres, à avancer dans le brouillard avec confiance.",
        "Affronte une peur inconsciente en la nommant à voix haute.",
        "Respire en visualisant un guerrier de lumière qui descend dans les ténèbres.",
        "Quelle peur inconsciente suis-je appelé(e) à affronter avec courage ? »"),

    # === TAURUS (M1-M12) ===
    ('taurus', 1): make_nn_interp('taurus', 1,
        "Ton chemin d'âme t'appelle à développer la stabilité et la présence incarnée.",
        "Le Nœud Nord en Taureau dans ta maison I t'invite à développer la constance et l'ancrage corporel. Tu quittes l'intensité du Scorpion pour la paix du Taureau.",
        "Apprendre à te détendre, à construire plutôt qu'à transformer sans cesse. Ta tendance aux crises et à l'intensité émotionnelle te freine dans ton évolution.",
        "Ton corps et ta présence sont le terrain de ton évolution. Tu apprends à habiter ton corps, à cultiver la beauté simple, à être plutôt qu'à chercher sans cesse.",
        "Fais quelque chose de simple et plaisant pour ton corps — un bain, un bon repas.",
        "Respire lentement en sentant tes pieds ancrés dans le sol.",
        "Quel plaisir simple ai-je négligé en cherchant l'intensité ? »"),

    ('taurus', 2): make_nn_interp('taurus', 2,
        "Ton chemin d'âme t'appelle à créer ta propre sécurité matérielle.",
        "Le Nœud Nord en Taureau dans ta maison II (son domicile naturel) t'invite à développer l'autonomie financière et la confiance en tes propres ressources.",
        "Apprendre à générer ta propre valeur plutôt qu'à dépendre des ressources partagées. Ta tendance à fusionner tes finances avec d'autres te freine.",
        "Tes finances sont le terrain de ton évolution karmique. Tu apprends à valoriser TES talents, à construire TA prospérité, à faire confiance à TES capacités.",
        "Identifie une compétence unique que tu possèdes et valorise-la.",
        "Respire en visualisant tes propres racines qui puisent dans une terre fertile.",
        "Quelle valeur propre ai-je peur de reconnaître en moi ? »"),

    ('taurus', 3): make_nn_interp('taurus', 3,
        "Ton chemin d'âme t'appelle à communiquer avec calme et simplicité.",
        "Le Nœud Nord en Taureau dans ta maison III t'invite à développer une parole posée et concrète. Tu quittes l'intensité philosophique pour la communication terre-à-terre.",
        "Apprendre à parler simplement et à écouter patiemment. Ta tendance à intellectualiser ou à dramatiser te freine dans ta communication.",
        "Tes échanges quotidiens sont le terrain de ton évolution. Tu apprends la patience dans le dialogue, l'écoute attentive, les mots choisis avec soin.",
        "Dans ta prochaine conversation, parle lentement et écoute vraiment.",
        "Respire en laissant tes mots devenir doux et solides comme la terre.",
        "Comment puis-je communiquer avec plus de calme et de présence ? »"),

    ('taurus', 4): make_nn_interp('taurus', 4,
        "Ton chemin d'âme t'appelle à créer un foyer stable et sécurisant.",
        "Le Nœud Nord en Taureau dans ta maison IV t'invite à développer des racines solides. Tu quittes l'ambition publique pour construire un vrai chez-toi.",
        "Apprendre à valoriser la vie domestique et familiale. Ta tendance à privilégier la carrière ou le statut te freine dans la construction de tes racines.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à créer un espace beau et stable, à cultiver les traditions, à t'enraciner dans un lieu.",
        "Investis dans quelque chose qui rend ton foyer plus beau ou confortable.",
        "Respire en visualisant les racines de ton arbre de vie qui s'enfoncent profondément.",
        "Qu'est-ce qui manque à mon foyer pour qu'il soit vraiment un sanctuaire ? »"),

    ('taurus', 5): make_nn_interp('taurus', 5,
        "Ton chemin d'âme t'appelle à créer et aimer avec constance et sensualité.",
        "Le Nœud Nord en Taureau dans ta maison V t'invite à développer une créativité patiente et des amours durables. Tu quittes l'intensité du groupe pour la joie simple.",
        "Apprendre à créer avec patience et à aimer sans drame. Ta tendance à chercher l'intensité collective te freine dans ta joie personnelle.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends l'art de la patience créative, l'amour sensuel et constant, le jeu tranquille.",
        "Crée quelque chose lentement, avec tes mains, en savourant le processus.",
        "Respire en laissant la joie simple et sensuelle entrer dans ton cœur.",
        "Comment puis-je apporter plus de constance et de sensualité dans ma créativité ? »"),

    ('taurus', 6): make_nn_interp('taurus', 6,
        "Ton chemin d'âme t'appelle à développer des routines saines et stables.",
        "Le Nœud Nord en Taureau dans ta maison VI t'invite à développer la régularité dans le travail et la santé. Tu quittes le chaos ou l'évasion pour la structure quotidienne.",
        "Apprendre à maintenir des habitudes constantes et nourrissantes. Ta tendance à fuir la routine ou à te perdre dans l'imaginaire te freine.",
        "Ton travail quotidien et ta santé sont le terrain de ton évolution. Tu apprends la valeur des rituels, de l'alimentation consciente, du travail patient.",
        "Établis une routine simple et suis-la pendant une semaine.",
        "Respire en sentant la paix d'un corps bien nourri et entretenu.",
        "Quelle routine de santé ai-je évitée parce qu'elle semblait trop ordinaire ? »"),

    ('taurus', 7): make_nn_interp('taurus', 7,
        "Ton chemin d'âme t'appelle à créer des partenariats stables et durables.",
        "Le Nœud Nord en Taureau dans ta maison VII t'invite à développer des relations de confiance. Tu quittes l'excès d'autonomie pour la sécurité du lien durable.",
        "Apprendre à construire des relations solides basées sur la loyauté. Ta tendance à l'indépendance excessive ou aux relations intenses mais instables te freine.",
        "Tes partenariats sont le terrain de ton évolution. Tu apprends la fidélité, la patience dans le couple, la construction lente d'une confiance mutuelle.",
        "Fais un geste de loyauté et de constance envers un partenaire.",
        "Respire en visualisant des relations aussi solides que des chênes centenaires.",
        "Comment puis-je apporter plus de stabilité et de loyauté dans mes relations ? »"),

    ('taurus', 8): make_nn_interp('taurus', 8,
        "Ton chemin d'âme t'appelle à trouver la paix dans les transformations.",
        "Le Nœud Nord en Taureau dans ta maison VIII t'invite à développer le calme face aux crises. Tu quittes l'attachement aux possessions pour accepter les cycles de vie.",
        "Apprendre à traverser les transformations avec sérénité. Ta tendance à t'accrocher à la sécurité matérielle te freine dans les processus de mort/renaissance.",
        "Les transformations profondes sont le terrain de ton évolution. Tu apprends à lâcher prise avec grâce, à partager les ressources calmement, à embrasser le changement.",
        "Identifie quelque chose à laquelle tu t'accroches et visualise le lâcher avec paix.",
        "Respire en accueillant le changement comme une saison naturelle.",
        "Qu'est-ce que je refuse de lâcher par peur de l'instabilité ? »"),

    ('taurus', 9): make_nn_interp('taurus', 9,
        "Ton chemin d'âme t'appelle à ancrer ta spiritualité dans le concret.",
        "Le Nœud Nord en Taureau dans ta maison IX t'invite à développer une philosophie pratique. Tu quittes l'accumulation de détails pour la sagesse incarnée.",
        "Apprendre à vivre ta spiritualité plutôt qu'à juste l'étudier. Ta tendance à intellectualiser ou à te disperser dans les informations te freine.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends que la vraie sagesse est simple, incarnée, vécue au quotidien plutôt que dissertée.",
        "Pratique un enseignement spirituel concrètement dans ta journée.",
        "Respire en ancrant une vérité spirituelle dans ton corps.",
        "Quelle sagesse puis-je incarner plus concrètement aujourd'hui ? »"),

    ('taurus', 10): make_nn_interp('taurus', 10,
        "Ton chemin d'âme t'appelle à construire une carrière stable et durable.",
        "Le Nœud Nord en Taureau dans ta maison X t'invite à développer une réputation de fiabilité. Tu quittes la dépendance émotionnelle pour l'autorité tranquille.",
        "Apprendre à bâtir ta carrière pierre après pierre avec patience. Ta tendance aux changements émotionnels ou à la dépendance familiale te freine professionnellement.",
        "Ta carrière est le terrain de ton évolution. Tu apprends la constance, la patience, la construction d'une réputation solide dans ton domaine.",
        "Identifie un objectif professionnel et fais un petit pas constant vers lui.",
        "Respire en visualisant une carrière aussi solide qu'une montagne.",
        "Quelle constance dois-je développer pour construire ma carrière ? »"),

    ('taurus', 11): make_nn_interp('taurus', 11,
        "Ton chemin d'âme t'appelle à créer des amitiés durables et des projets stables.",
        "Le Nœud Nord en Taureau dans ta maison XI t'invite à développer des liens amicaux fiables. Tu quittes l'attention dramatique pour la contribution stable au groupe.",
        "Apprendre à être un ami loyal et un contributeur constant. Ta tendance au drame personnel ou à l'égocentrisme te freine dans les projets collectifs.",
        "Tes amitiés et projets collectifs sont le terrain de ton évolution. Tu apprends la valeur des contributions constantes, des amitiés durables, des projets à long terme.",
        "Offre une aide concrète et régulière à un groupe ou une cause.",
        "Respire en visualisant un réseau d'amis aussi solide qu'un jardin bien entretenu.",
        "Comment puis-je contribuer plus constamment aux projets qui me tiennent à cœur ? »"),

    ('taurus', 12): make_nn_interp('taurus', 12,
        "Ton chemin d'âme t'appelle à trouver la paix intérieure et l'ancrage spirituel.",
        "Le Nœud Nord en Taureau dans ta maison XII t'invite à développer la sérénité intérieure. Tu quittes l'anxiété du quotidien pour la paix de l'être.",
        "Apprendre à te détendre profondément et à trouver la sécurité en toi. Ta tendance à l'inquiétude ou au perfectionnisme te freine dans ta paix intérieure.",
        "L'inconscient et le repos sont le terrain de ton évolution. Tu apprends la méditation tranquille, le lâcher-prise profond, la confiance dans l'univers.",
        "Allonge-toi et ne fais absolument rien pendant 5 minutes.",
        "Respire en visualisant une paix profonde qui t'enveloppe comme une couverture.",
        "Quelle inquiétude puis-je lâcher pour trouver la paix intérieure ? »"),

    # === GEMINI (M1-M12) ===
    ('gemini', 1): make_nn_interp('gemini', 1,
        "Ton chemin d'âme t'appelle à développer la curiosité et la communication.",
        "Le Nœud Nord en Gémeaux dans ta maison I t'invite à développer ta flexibilité et ton ouverture d'esprit. Tu quittes les certitudes du Sagittaire pour la curiosité des Gémeaux.",
        "Apprendre à questionner plutôt qu'à prêcher. Ta tendance à avoir des opinions arrêtées et à vouloir enseigner te freine dans ton évolution personnelle.",
        "Ta présence et ton identité sont le terrain de ton évolution. Tu apprends à être curieux, adaptable, capable de voir plusieurs points de vue.",
        "Pose une vraie question à quelqu'un aujourd'hui, sans avoir de réponse préconçue.",
        "Respire en laissant ton mental devenir léger et curieux comme un enfant.",
        "Quelle question ai-je évitée parce que je pensais avoir la réponse ? »"),

    ('gemini', 2): make_nn_interp('gemini', 2,
        "Ton chemin d'âme t'appelle à développer ta valeur par l'apprentissage.",
        "Le Nœud Nord en Gémeaux dans ta maison II t'invite à développer des compétences multiples. Tu quittes la dépendance aux croyances pour la richesse des savoirs pratiques.",
        "Apprendre à valoriser tes capacités intellectuelles et communicatives. Ta tendance à chercher le sens philosophique avant la compétence pratique te freine.",
        "Tes finances et ta valeur personnelle sont le terrain de ton évolution. Tu apprends que plusieurs petites compétences valent autant qu'une grande vérité.",
        "Apprends quelque chose de nouveau et pratique aujourd'hui.",
        "Respire en visualisant tes nombreux talents qui s'assemblent comme une mosaïque.",
        "Quelle compétence pratique ai-je négligée en cherchant des vérités plus grandes ? »"),

    ('gemini', 3): make_nn_interp('gemini', 3,
        "Ton chemin d'âme t'appelle à maîtriser la communication et l'apprentissage.",
        "Le Nœud Nord en Gémeaux dans ta maison III (son domicile naturel) t'invite à développer pleinement tes capacités mentales et communicatives.",
        "Apprendre à écouter, questionner et partager l'information. Ta tendance à philosopher sans communiquer concrètement te freine.",
        "Ta communication quotidienne est le terrain de ton évolution. Tu apprends l'écoute active, l'écriture, les échanges avec ton environnement proche.",
        "Engage une conversation où tu poses plus de questions que tu ne donnes d'opinions.",
        "Respire en sentant l'air de la curiosité qui circule dans ton esprit.",
        "Comment puis-je mieux écouter et questionner dans mes conversations ? »"),

    ('gemini', 4): make_nn_interp('gemini', 4,
        "Ton chemin d'âme t'appelle à créer un foyer d'échanges et de curiosité.",
        "Le Nœud Nord en Gémeaux dans ta maison IV t'invite à développer une vie familiale stimulante intellectuellement. Tu quittes les certitudes héritées pour l'exploration familiale.",
        "Apprendre à communiquer vraiment au sein de ta famille. Ta tendance à imposer des vérités ou à rester dans des traditions rigides te freine.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à créer un espace de dialogue, de curiosité partagée, d'échanges entre générations.",
        "Engage une conversation curieuse avec un membre de ta famille sur un sujet nouveau.",
        "Respire en visualisant un foyer où la curiosité et le dialogue règnent.",
        "Quel dialogue ai-je évité dans ma famille par peur de questionner les certitudes ? »"),

    ('gemini', 5): make_nn_interp('gemini', 5,
        "Ton chemin d'âme t'appelle à créer et aimer avec légèreté et curiosité.",
        "Le Nœud Nord en Gémeaux dans ta maison V t'invite à développer une créativité ludique et des amours stimulantes. Tu quittes le sérieux pour le jeu de l'esprit.",
        "Apprendre à jouer avec les idées et à aimer avec légèreté. Ta tendance à prendre l'amour et la création trop au sérieux te freine.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends le flirt intellectuel, la création variée, le jeu des mots et des idées.",
        "Crée quelque chose de ludique, d'amusant, sans enjeu de perfection.",
        "Respire en laissant la légèreté et l'humour entrer dans ton expression.",
        "Comment puis-je apporter plus de légèreté et de jeu dans ma créativité ? »"),

    ('gemini', 6): make_nn_interp('gemini', 6,
        "Ton chemin d'âme t'appelle à développer des compétences multiples au quotidien.",
        "Le Nœud Nord en Gémeaux dans ta maison VI t'invite à développer la polyvalence au travail et la curiosité pour la santé. Tu quittes la confusion pour la clarté pratique.",
        "Apprendre à organiser ton quotidien avec intelligence. Ta tendance à te perdre dans l'imagination ou à fuir les détails te freine.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends à diversifier tes compétences, à comprendre ton corps, à communiquer au travail.",
        "Apprends une nouvelle compétence utile pour ton travail quotidien.",
        "Respire en visualisant un mental clair qui organise efficacement ton quotidien.",
        "Quelle information pratique sur ma santé ou mon travail ai-je négligée ? »"),

    ('gemini', 7): make_nn_interp('gemini', 7,
        "Ton chemin d'âme t'appelle à développer le dialogue dans tes relations.",
        "Le Nœud Nord en Gémeaux dans ta maison VII t'invite à développer la communication dans tes partenariats. Tu quittes l'affirmation solitaire pour l'échange à deux.",
        "Apprendre à dialoguer vraiment plutôt qu'à imposer ou à te battre seul. Ta tendance à l'action indépendante te freine dans la création de vrais partenariats.",
        "Tes relations sont le terrain de ton évolution. Tu apprends l'art de la conversation à deux, du compromis intelligent, de l'échange d'idées.",
        "Engage un vrai dialogue avec un partenaire où chacun écoute l'autre.",
        "Respire en visualisant des relations basées sur l'échange et le dialogue.",
        "Comment puis-je mieux communiquer avec mes partenaires ? »"),

    ('gemini', 8): make_nn_interp('gemini', 8,
        "Ton chemin d'âme t'appelle à comprendre intellectuellement les mystères.",
        "Le Nœud Nord en Gémeaux dans ta maison VIII t'invite à développer une approche curieuse des transformations. Tu quittes l'attachement matériel pour l'exploration psychologique.",
        "Apprendre à parler des sujets tabous et à explorer avec curiosité. Ta tendance à t'accrocher à la sécurité ou à fuir les sujets profonds te freine.",
        "Les transformations sont le terrain de ton évolution. Tu apprends à mettre des mots sur les mystères, à discuter ouvertement de la mort, du sexe, des crises.",
        "Engage une conversation sur un sujet que tu évites habituellement.",
        "Respire en accueillant la curiosité pour ce qui se cache dans l'ombre.",
        "De quel sujet tabou ai-je besoin de parler pour évoluer ? »"),

    ('gemini', 9): make_nn_interp('gemini', 9,
        "Ton chemin d'âme t'appelle à apprendre sans dogme et à explorer avec curiosité.",
        "Le Nœud Nord en Gémeaux dans ta maison IX t'invite à développer une spiritualité questionnante. Tu quittes le détail obsessionnel pour la quête de sens légère.",
        "Apprendre à explorer les croyances sans s'y attacher. Ta tendance au perfectionnisme ou à l'anxiété du détail te freine dans ta quête spirituelle.",
        "Ta philosophie et tes voyages sont le terrain de ton évolution. Tu apprends à questionner, à explorer plusieurs voies, à voyager avec curiosité.",
        "Explore une idée spirituelle nouvelle sans te demander si elle est vraie.",
        "Respire en laissant les questions être plus importantes que les réponses.",
        "Quelle certitude spirituelle gagnerait à être questionnée ? »"),

    ('gemini', 10): make_nn_interp('gemini', 10,
        "Ton chemin d'âme t'appelle à communiquer dans ta carrière.",
        "Le Nœud Nord en Gémeaux dans ta maison X t'invite à développer une carrière basée sur la communication. Tu quittes la sécurité émotionnelle pour la réputation intellectuelle.",
        "Apprendre à partager tes idées professionnellement et à te faire connaître. Ta tendance à rester dans ta zone de confort familiale te freine dans ta carrière.",
        "Ta carrière est le terrain de ton évolution. Tu apprends à parler en public, à écrire, à devenir une référence dans l'échange d'idées.",
        "Partage une idée professionnelle avec un public plus large.",
        "Respire en visualisant une carrière où ta voix compte et porte.",
        "Quelle idée professionnelle ai-je peur de partager publiquement ? »"),

    ('gemini', 11): make_nn_interp('gemini', 11,
        "Ton chemin d'âme t'appelle à connecter les gens et les idées.",
        "Le Nœud Nord en Gémeaux dans ta maison XI t'invite à développer des réseaux intellectuels. Tu quittes le besoin d'être spécial pour le plaisir de connecter.",
        "Apprendre à faciliter les échanges dans les groupes. Ta tendance à chercher l'attention personnelle ou la romance te freine dans le networking.",
        "Tes amitiés et projets collectifs sont le terrain de ton évolution. Tu apprends à être un connecteur, un facilitateur d'échanges, un pont entre les gens.",
        "Présente deux personnes qui pourraient s'enrichir mutuellement.",
        "Respire en visualisant un réseau d'idées et de connexions qui s'étend.",
        "Comment puis-je mieux connecter les gens et les idées autour de moi ? »"),

    ('gemini', 12): make_nn_interp('gemini', 12,
        "Ton chemin d'âme t'appelle à comprendre l'inconscient avec curiosité.",
        "Le Nœud Nord en Gémeaux dans ta maison XII t'invite à développer une exploration intellectuelle du monde invisible. Tu quittes la rigidité du contrôle pour la curiosité de l'inconnu.",
        "Apprendre à mettre des mots sur l'indicible et à explorer tes rêves. Ta tendance à rester dans le rationnel ou le quotidien te freine dans ton évolution spirituelle.",
        "L'inconscient est le terrain de ton évolution. Tu apprends à écrire tes rêves, à dialoguer avec ton ombre, à explorer l'invisible avec légèreté.",
        "Écris tes rêves ou tes intuitions sans les analyser.",
        "Respire en laissant la curiosité éclairer les coins sombres de ton esprit.",
        "Qu'est-ce que mon inconscient essaie de me dire en ce moment ? »"),

    # === CANCER (M1-M12) ===
    ('cancer', 1): make_nn_interp('cancer', 1,
        "Ton chemin d'âme t'appelle à développer la sensibilité et le soin de toi.",
        "Le Nœud Nord en Cancer dans ta maison I t'invite à développer ton côté émotionnel et protecteur. Tu quittes la rigidité du Capricorne pour la douceur du Cancer.",
        "Apprendre à être vulnérable et à prendre soin de toi-même. Ta tendance à l'ambition froide et au contrôle te freine dans ton épanouissement personnel.",
        "Ton identité est le terrain de ton évolution. Tu apprends à être sensible, à montrer tes émotions, à créer une coquille protectrice saine.",
        "Permets-toi une émotion que tu réprimes habituellement.",
        "Respire en visualisant une carapace douce qui te protège sans te fermer.",
        "Quelle vulnérabilité ai-je peur de montrer au monde ? »"),

    ('cancer', 2): make_nn_interp('cancer', 2,
        "Ton chemin d'âme t'appelle à créer une sécurité émotionnelle et matérielle.",
        "Le Nœud Nord en Cancer dans ta maison II t'invite à développer un rapport émotionnel sain à la sécurité. Tu quittes la dépendance aux ressources extérieures pour nourrir ta propre abondance.",
        "Apprendre à te nourrir toi-même et à créer ta sécurité intérieure. Ta tendance à dépendre des crises ou des transformations pour te sentir vivant te freine.",
        "Tes ressources sont le terrain de ton évolution. Tu apprends que la vraie richesse est émotionnelle, que l'argent doit nourrir, pas contrôler.",
        "Dépense pour quelque chose qui nourrit ton âme, pas ton ego.",
        "Respire en visualisant une source intérieure de sécurité qui ne tarit jamais.",
        "Qu'est-ce qui me ferait me sentir vraiment nourri(e) et en sécurité ? »"),

    ('cancer', 3): make_nn_interp('cancer', 3,
        "Ton chemin d'âme t'appelle à communiquer avec cœur et sensibilité.",
        "Le Nœud Nord en Cancer dans ta maison III t'invite à développer une communication émotionnelle. Tu quittes l'abstraction philosophique pour l'expression du cœur.",
        "Apprendre à parler avec émotion et à écouter avec empathie. Ta tendance à intellectualiser ou à prêcher te freine dans la vraie connexion.",
        "Ta communication est le terrain de ton évolution. Tu apprends à exprimer tes sentiments, à écrire avec le cœur, à dialoguer avec tes proches.",
        "Dis à quelqu'un ce que tu ressens vraiment, pas ce que tu penses.",
        "Respire en laissant les mots venir de ton cœur plutôt que de ta tête.",
        "Quelle émotion ai-je besoin d'exprimer à quelqu'un de proche ? »"),

    ('cancer', 4): make_nn_interp('cancer', 4,
        "Ton chemin d'âme t'appelle à créer un vrai foyer et des racines émotionnelles.",
        "Le Nœud Nord en Cancer dans ta maison IV (son domicile naturel) t'invite à développer pleinement ta vie intérieure et familiale.",
        "Apprendre à prioriser la famille et le foyer sur la carrière. Ta tendance à te définir par ton statut professionnel te freine dans ton épanouissement intime.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à nourrir les liens familiaux, à créer un sanctuaire, à honorer tes racines.",
        "Fais quelque chose de nourrissant pour ta famille ou ton foyer.",
        "Respire en visualisant des racines profondes qui te connectent à tes ancêtres.",
        "Comment puis-je mieux nourrir ma vie familiale et mon foyer ? »"),

    ('cancer', 5): make_nn_interp('cancer', 5,
        "Ton chemin d'âme t'appelle à créer et aimer avec le cœur.",
        "Le Nœud Nord en Cancer dans ta maison V t'invite à développer une créativité émotionnelle et des amours nourrissantes. Tu quittes le besoin d'approbation sociale pour la joie intime.",
        "Apprendre à créer depuis le cœur et à aimer avec tendresse. Ta tendance à chercher la reconnaissance du groupe te freine dans ta joie personnelle.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends l'art de nourrir, de protéger ce que tu crées, d'aimer comme une mère aime.",
        "Crée quelque chose d'intime que tu ne montreras à personne.",
        "Respire en laissant la tendresse nourrir ta créativité.",
        "Comment puis-je créer avec plus de cœur et de sensibilité ? »"),

    ('cancer', 6): make_nn_interp('cancer', 6,
        "Ton chemin d'âme t'appelle à prendre soin de toi et des autres au quotidien.",
        "Le Nœud Nord en Cancer dans ta maison VI t'invite à développer des habitudes nourrissantes. Tu quittes la confusion ou l'évasion pour le soin quotidien.",
        "Apprendre à nourrir ton corps et à servir avec le cœur. Ta tendance à te sacrifier ou à fuir la réalité te freine dans la création de bonnes habitudes.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends à cuisiner, à soigner, à créer des routines qui nourrissent.",
        "Prépare-toi un repas nourrissant avec amour et présence.",
        "Respire en visualisant chaque cellule de ton corps recevoir de la tendresse.",
        "Comment puis-je mieux prendre soin de moi au quotidien ? »"),

    ('cancer', 7): make_nn_interp('cancer', 7,
        "Ton chemin d'âme t'appelle à créer des partenariats nourrissants.",
        "Le Nœud Nord en Cancer dans ta maison VII t'invite à développer des relations émotionnellement profondes. Tu quittes l'indépendance froide pour l'intimité protectrice.",
        "Apprendre à s'ouvrir émotionnellement dans le couple. Ta tendance à l'autonomie ou à l'affirmation agressive te freine dans la création d'un vrai foyer à deux.",
        "Tes partenariats sont le terrain de ton évolution. Tu apprends à nourrir l'autre, à créer un nid commun, à être vulnérable ensemble.",
        "Offre un geste de soin ou de tendresse à un partenaire.",
        "Respire en visualisant des relations qui te nourrissent autant que tu les nourris.",
        "Comment puis-je mieux prendre soin de mes partenaires ? »"),

    ('cancer', 8): make_nn_interp('cancer', 8,
        "Ton chemin d'âme t'appelle à traverser les transformations avec le cœur.",
        "Le Nœud Nord en Cancer dans ta maison VIII t'invite à développer une approche émotionnelle des crises. Tu quittes l'attachement aux possessions pour la sécurité intérieure.",
        "Apprendre à nourrir toi et les autres dans les moments de crise. Ta tendance à t'accrocher aux biens matériels te freine dans les transformations.",
        "Les transformations sont le terrain de ton évolution. Tu apprends à accompagner avec tendresse, à pleurer, à guérir par l'amour.",
        "Permets-toi de pleurer ou de ressentir une perte avec douceur.",
        "Respire en accueillant les émotions de transformation avec tendresse maternelle.",
        "Quelle émotion de transformation ai-je besoin d'accueillir ? »"),

    ('cancer', 9): make_nn_interp('cancer', 9,
        "Ton chemin d'âme t'appelle à développer une spiritualité du cœur.",
        "Le Nœud Nord en Cancer dans ta maison IX t'invite à développer une philosophie émotionnelle. Tu quittes l'analyse détaillée pour la sagesse intuitive.",
        "Apprendre à faire confiance à ton intuition et à ton cœur dans ta quête de sens. Ta tendance à sur-analyser te freine dans ta connexion spirituelle.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends la sagesse du cœur, la philosophie maternelle, la religion de l'amour.",
        "Médite sur ce que ton cœur sait, sans analyse mentale.",
        "Respire en laissant la sagesse intuitive monter de ton ventre.",
        "Quelle vérité mon cœur connaît-il que mon mental ignore ? »"),

    ('cancer', 10): make_nn_interp('cancer', 10,
        "Ton chemin d'âme t'appelle à apporter le soin dans ta carrière.",
        "Le Nœud Nord en Cancer dans ta maison X t'invite à développer une réputation de personne bienveillante. Tu quittes les émotions privées pour le soin public.",
        "Apprendre à montrer ta sensibilité professionnellement. Ta tendance à cacher tes émotions derrière une façade de contrôle te freine dans ton impact.",
        "Ta carrière est le terrain de ton évolution. Tu apprends à diriger avec le cœur, à créer des entreprises qui nourrissent, à être une figure maternelle publique.",
        "Apporte un geste de soin ou d'attention dans ton environnement professionnel.",
        "Respire en visualisant une carrière qui nourrit le monde.",
        "Comment puis-je apporter plus de soin et de cœur dans ma carrière ? »"),

    ('cancer', 11): make_nn_interp('cancer', 11,
        "Ton chemin d'âme t'appelle à créer des communautés nourrissantes.",
        "Le Nœud Nord en Cancer dans ta maison XI t'invite à développer des amitiés de cœur. Tu quittes le besoin d'attention personnelle pour le soin de la communauté.",
        "Apprendre à nourrir les groupes et à créer des espaces d'accueil. Ta tendance à chercher l'attention ou la créativité personnelle te freine dans le soin collectif.",
        "Tes amitiés et projets sont le terrain de ton évolution. Tu apprends à créer des familles choisies, des communautés qui nourrissent, des projets du cœur.",
        "Organise un moment convivial pour un groupe d'amis.",
        "Respire en visualisant une communauté que tu nourris et qui te nourrit.",
        "Comment puis-je mieux prendre soin de mes amis et de ma communauté ? »"),

    ('cancer', 12): make_nn_interp('cancer', 12,
        "Ton chemin d'âme t'appelle à développer une compassion profonde.",
        "Le Nœud Nord en Cancer dans ta maison XII t'invite à développer une connexion émotionnelle à l'universel. Tu quittes l'anxiété du quotidien pour la paix du lâcher-prise.",
        "Apprendre à prendre soin de ton inconscient et à développer la compassion universelle. Ta tendance à t'inquiéter des détails te freine dans la confiance spirituelle.",
        "L'inconscient est le terrain de ton évolution. Tu apprends à bercer tes peurs, à materner tes ombres, à trouver la sécurité dans l'invisible.",
        "Berce-toi intérieurement comme tu bercerais un enfant effrayé.",
        "Respire en visualisant une présence aimante qui t'enveloppe.",
        "Quelle partie de moi a besoin d'être maternée avec tendresse ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in NORTH_NODE_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'north_node',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP north_node/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='north_node',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT north_node/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
