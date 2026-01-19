#!/usr/bin/env python3
"""Insert Lilith interpretations for Aries, Taurus, Gemini, Cancer (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_lilith_interp(sign_name, house, phrase, ombre, pouvoir, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'aries': '⚸ Lilith en Bélier',
        'taurus': '⚸ Lilith en Taureau',
        'gemini': '⚸ Lilith en Gémeaux',
        'cancer': '⚸ Lilith en Cancer',
    }
    sign_fr = {
        'aries': 'Bélier',
        'taurus': 'Taureau',
        'gemini': 'Gémeaux',
        'cancer': 'Cancer',
    }
    return f"""# {sign_titles[sign_name]}

**En une phrase :** {phrase}

## Ton ombre
{ombre}

## Ton pouvoir brut
{pouvoir}

## Maison {house} en {sign_fr[sign_name]}
{maison_desc}

## Micro-rituel du jour (2 min)
- {ritual_action}
- {ritual_breath}
- Journal : « {ritual_journal} »"""

LILITH_INTERPRETATIONS = {
    # === ARIES (M1-M12) ===
    ('aries', 1): make_lilith_interp('aries', 1,
        "Ton ombre se loge dans la rage et l'affirmation sauvage — ton pouvoir est celui de la guerrière intérieure.",
        "Lilith en Bélier dans ta maison I place ton ombre dans ton identité même. Tu peux avoir refoulé une colère profonde ou une rage d'exister, une partie de toi qui veut se battre et s'imposer.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir brut d'affirmation et de courage. Tu deviens capable de défendre ton droit d'exister avec une force primitive.",
        "En maison I, cette énergie est très personnelle. Ta rage peut se retourner contre toi-même ou s'exprimer de façon brute. Apprends à canaliser ce feu sans le renier.",
        "Exprime une colère refoulée de façon sécurisée (crier dans un coussin, sport intense).",
        "Respire en sentant ta force brute comme un allié.",
        "Quelle rage d'exister ai-je refoulée ? »"),

    ('aries', 2): make_lilith_interp('aries', 2,
        "Ton ombre se loge dans le rapport agressif à l'argent — ton pouvoir est celui de la conquête des ressources.",
        "Lilith en Bélier dans ta maison II place ton ombre dans ta relation aux possessions. Tu peux avoir honte de ton désir de conquérir ou une rage autour de ce qui t'a été refusé.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir brut pour générer des ressources. Tu deviens capable de prendre ce qui t'appartient avec audace.",
        "En maison II, cette énergie touche ta valeur personnelle. Tu peux avoir une relation tumultueuse avec l'argent, entre agressivité et culpabilité. Trouve l'équilibre.",
        "Affirme ce que tu vaux sans te justifier.",
        "Respire en te sentant digne de prendre ta part.",
        "Quelle rage autour de l'argent ou de ma valeur ai-je refoulée ? »"),

    ('aries', 3): make_lilith_interp('aries', 3,
        "Ton ombre se loge dans la parole tranchante — ton pouvoir est celui de la vérité crue.",
        "Lilith en Bélier dans ta maison III place ton ombre dans ta communication. Tu peux avoir refoulé des mots violents ou une capacité à blesser avec les mots.",
        "En intégrant cette Lilith, tu accèdes à une parole puissante et directe. Tu deviens capable de dire des vérités que personne n'ose dire.",
        "En maison III, cette énergie peut créer des conflits avec l'entourage proche. Ta langue peut être une arme. Apprends à l'utiliser pour libérer, pas pour détruire.",
        "Dis une vérité que tu retenais par peur de blesser.",
        "Respire en honorant ta capacité à parler vrai.",
        "Quels mots tranchants ai-je retenus en moi ? »"),

    ('aries', 4): make_lilith_interp('aries', 4,
        "Ton ombre se loge dans la rage familiale — ton pouvoir est celui de défendre les tiens.",
        "Lilith en Bélier dans ta maison IV place ton ombre dans ta famille et tes racines. Tu peux avoir refoulé une colère contre ta famille ou une violence héritée.",
        "En intégrant cette Lilith, tu accèdes à une force brute pour protéger ce qui t'est cher. Tu deviens capable de défendre ton foyer avec férocité.",
        "En maison IV, cette énergie peut créer des tensions familiales ou un foyer volcanique. Transmute la rage héritée en force de protection.",
        "Exprime une colère familiale refoulée de façon sécurisée.",
        "Respire en transformant la rage en force protectrice.",
        "Quelle rage familiale porte mon inconscient ? »"),

    ('aries', 5): make_lilith_interp('aries', 5,
        "Ton ombre se loge dans la création passionnelle — ton pouvoir est celui de la flamme créatrice.",
        "Lilith en Bélier dans ta maison V place ton ombre dans ta créativité et tes amours. Tu peux avoir refoulé une passion brûlante ou une jalousie dévorante.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir créatif brut et à une capacité d'aimer avec une intensité sauvage.",
        "En maison V, cette énergie peut créer des drames amoureux ou une créativité explosive. Apprends à canaliser cette flamme sans te brûler.",
        "Crée quelque chose avec une passion brute, sans censure.",
        "Respire en embrassant ta flamme créatrice.",
        "Quelle passion brûlante ai-je refoulée en amour ou en création ? »"),

    ('aries', 6): make_lilith_interp('aries', 6,
        "Ton ombre se loge dans la rage au travail — ton pouvoir est celui de l'action directe.",
        "Lilith en Bélier dans ta maison VI place ton ombre dans ton rapport au travail quotidien. Tu peux avoir refoulé une colère contre l'autorité ou un désir de tout casser.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'efficacité brutale et à une capacité de couper ce qui ne fonctionne pas.",
        "En maison VI, cette énergie peut créer des conflits au travail ou des problèmes de santé liés à la colère refoulée. Trouve des exutoires sains.",
        "Accomplis une tâche avec une énergie brute et directe.",
        "Respire en canalisant ta rage dans l'action productive.",
        "Quelle rage au travail ai-je refoulée ? »"),

    ('aries', 7): make_lilith_interp('aries', 7,
        "Ton ombre se loge dans les relations conflictuelles — ton pouvoir est celui de l'affirmation en couple.",
        "Lilith en Bélier dans ta maison VII place ton ombre dans tes partenariats. Tu peux avoir refoulé une agressivité dans tes relations ou attirer des partenaires colériques.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de t'affirmer pleinement dans tes relations. Tu deviens capable de dire non et de poser des limites fermes.",
        "En maison VII, cette énergie peut créer des relations explosives ou des luttes de pouvoir. Apprends à t'affirmer sans déclarer la guerre.",
        "Affirme une limite ferme dans une relation.",
        "Respire en te sentant fort dans tes partenariats.",
        "Quelle colère relationnelle ai-je refoulée ou projetée sur mes partenaires ? »"),

    ('aries', 8): make_lilith_interp('aries', 8,
        "Ton ombre se loge dans la rage de survie — ton pouvoir est celui de la transformation par le feu.",
        "Lilith en Bélier dans ta maison VIII place ton ombre dans les profondeurs de la transformation. Tu peux avoir une rage liée à des traumas ou à la mort.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformation radicale. Tu deviens capable de traverser les crises avec une force primitive.",
        "En maison VIII, cette énergie est particulièrement intense. Ta rage peut être liée à des expériences de pouvoir, de sexualité ou de mort. Transmute-la en renaissance.",
        "Affronte une peur avec la force d'un guerrier.",
        "Respire en sentant ta capacité à renaître de tes cendres.",
        "Quelle rage de survie ou trauma non-résolu porte mon inconscient ? »"),

    ('aries', 9): make_lilith_interp('aries', 9,
        "Ton ombre se loge dans le fanatisme — ton pouvoir est celui du pionnier spirituel.",
        "Lilith en Bélier dans ta maison IX place ton ombre dans tes croyances. Tu peux avoir une rage contre les religions ou un fanatisme refoulé.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de défendre tes convictions avec force et d'ouvrir de nouvelles voies spirituelles.",
        "En maison IX, cette énergie peut créer des conflits idéologiques ou une quête de vérité agressive. Sois un pionnier, pas un croisé.",
        "Défends une croyance avec passion sans imposer.",
        "Respire en honorant ta flamme spirituelle.",
        "Quelle rage contre les croyances ou les institutions ai-je refoulée ? »"),

    ('aries', 10): make_lilith_interp('aries', 10,
        "Ton ombre se loge dans l'ambition agressive — ton pouvoir est celui du leader audacieux.",
        "Lilith en Bélier dans ta maison X place ton ombre dans ta carrière. Tu peux avoir refoulé une ambition féroce ou une rage contre le système.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de leadership brut. Tu deviens capable de prendre le pouvoir avec audace.",
        "En maison X, cette énergie peut créer des conflits avec l'autorité ou une carrière tumultueuse. Utilise ta rage comme carburant, pas comme arme de destruction.",
        "Prends une initiative audacieuse dans ta carrière.",
        "Respire en assumant ton ambition sans culpabilité.",
        "Quelle rage contre le système ou l'autorité ai-je refoulée ? »"),

    ('aries', 11): make_lilith_interp('aries', 11,
        "Ton ombre se loge dans la rébellion — ton pouvoir est celui du révolutionnaire.",
        "Lilith en Bélier dans ta maison XI place ton ombre dans tes groupes et tes idéaux. Tu peux avoir une rage contre la société ou un désir de tout renverser.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de mobiliser les autres et de mener des révolutions. Tu deviens un catalyseur de changement.",
        "En maison XI, cette énergie peut créer des conflits dans les groupes ou une marginalisation. Sois un révolutionnaire constructif.",
        "Initie un changement dans un groupe ou une cause.",
        "Respire en canalisant ta rébellion vers la transformation positive.",
        "Quelle rage contre la société ou les groupes ai-je refoulée ? »"),

    ('aries', 12): make_lilith_interp('aries', 12,
        "Ton ombre se loge dans la rage inconsciente — ton pouvoir est celui du guerrier intérieur.",
        "Lilith en Bélier dans ta maison XII place ton ombre dans les profondeurs de l'inconscient. Tu peux avoir une rage que tu ne comprends pas, héritée ou karmique.",
        "En intégrant cette Lilith, tu accèdes à une force intérieure brute. Tu deviens capable de te battre contre tes propres démons avec courage.",
        "En maison XII, cette énergie est cachée mais puissante. Ta colère peut se retourner contre toi ou te saboter. Fais la paix avec ton guerrier intérieur.",
        "Médite sur ta rage sans la juger, juste en l'observant.",
        "Respire en faisant ami avec ton guerrier de l'ombre.",
        "Quelle rage inconsciente ou karmique porte mon âme ? »"),

    # === TAURUS (M1-M12) ===
    ('taurus', 1): make_lilith_interp('taurus', 1,
        "Ton ombre se loge dans la possessivité et la sensualité — ton pouvoir est celui de l'incarnation brute.",
        "Lilith en Taureau dans ta maison I place ton ombre dans ton identité corporelle. Tu peux avoir honte de ton corps, de tes désirs sensuels ou de ta possessivité.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'incarnation et de présence. Tu deviens magnétiquement ancré dans ta chair.",
        "En maison I, cette énergie est très visible. Tu peux attirer ou repousser par ta sensualité brute. Apprends à habiter pleinement ton corps.",
        "Habite ton corps avec une présence sensuelle assumée.",
        "Respire en sentant le pouvoir de ta chair.",
        "Quelle honte corporelle ou sensuelle ai-je refoulée ? »"),

    ('taurus', 2): make_lilith_interp('taurus', 2,
        "Ton ombre se loge dans l'attachement excessif — ton pouvoir est celui de l'abondance magnétique.",
        "Lilith en Taureau dans ta maison II (son domicile) place ton ombre dans tes possessions et ta valeur. Tu peux avoir une relation obsessionnelle à l'argent ou au confort.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir magnétique d'attirer l'abondance. Tu deviens un aimant à ressources.",
        "En maison II, cette énergie est particulièrement puissante. Tu peux passer de l'avarice à la prodigalité. Trouve l'équilibre entre avoir et être.",
        "Attire consciemment quelque chose de valeur vers toi.",
        "Respire en te sentant naturellement abondant.",
        "Quelle obsession ou honte autour des possessions ai-je refoulée ? »"),

    ('taurus', 3): make_lilith_interp('taurus', 3,
        "Ton ombre se loge dans la parole possessive — ton pouvoir est celui de la parole qui ancre.",
        "Lilith en Taureau dans ta maison III place ton ombre dans ta communication. Tu peux avoir refoulé une lenteur de parole ou des mots possessifs.",
        "En intégrant cette Lilith, tu accèdes à une parole qui a du poids et qui ancre. Tes mots ont un pouvoir matérialisant.",
        "En maison III, cette énergie peut créer de l'entêtement dans les échanges. Ta parole est lente mais puissante. Utilise-la avec conscience.",
        "Prononce des mots avec l'intention de les matérialiser.",
        "Respire en sentant le poids de tes paroles.",
        "Quelle possessivité ou entêtement ai-je dans ma communication ? »"),

    ('taurus', 4): make_lilith_interp('taurus', 4,
        "Ton ombre se loge dans l'attachement au foyer — ton pouvoir est celui de créer un sanctuaire.",
        "Lilith en Taureau dans ta maison IV place ton ombre dans ta relation au foyer et à la famille. Tu peux avoir une possessivité extrême de ton territoire.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer un espace sacré et protégé. Ton foyer devient un sanctuaire magnétique.",
        "En maison IV, cette énergie peut créer un attachement excessif aux racines ou au passé. Transforme la possessivité en ancrage sain.",
        "Crée un espace de confort sensuel dans ton foyer.",
        "Respire en sentant ton foyer comme ton sanctuaire.",
        "Quel attachement excessif à mon foyer ou à mon passé ai-je refoulé ? »"),

    ('taurus', 5): make_lilith_interp('taurus', 5,
        "Ton ombre se loge dans les plaisirs sensuels — ton pouvoir est celui de la création incarnée.",
        "Lilith en Taureau dans ta maison V place ton ombre dans la créativité et l'amour charnel. Tu peux avoir honte de tes désirs sensuels ou de ta gourmandise.",
        "En intégrant cette Lilith, tu accèdes à une créativité profondément incarnée. Tu crées avec tes sens et tu aimes avec ton corps.",
        "En maison V, cette énergie peut créer des passions sensuelles intenses ou une créativité très physique. Célèbre tes sens sans culpabilité.",
        "Crée quelque chose avec tous tes sens engagés.",
        "Respire en célébrant le plaisir de créer.",
        "Quels plaisirs sensuels ai-je refoulés par honte ? »"),

    ('taurus', 6): make_lilith_interp('taurus', 6,
        "Ton ombre se loge dans la paresse ou l'excès de travail — ton pouvoir est celui du rythme naturel.",
        "Lilith en Taureau dans ta maison VI place ton ombre dans ton rapport au travail et au corps. Tu peux osciller entre paresse et acharnement au travail.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de travailler en suivant ton rythme naturel. Tu deviens productif sans t'épuiser.",
        "En maison VI, cette énergie peut créer des conflits entre confort et devoir. Apprends à honorer ton corps tout en servant.",
        "Travaille à ton propre rythme, en écoutant ton corps.",
        "Respire en honorant le rythme naturel de ton corps.",
        "Où oscille-je entre paresse et excès de travail ? »"),

    ('taurus', 7): make_lilith_interp('taurus', 7,
        "Ton ombre se loge dans la possessivité amoureuse — ton pouvoir est celui de l'amour incarné.",
        "Lilith en Taureau dans ta maison VII place ton ombre dans tes relations. Tu peux avoir une possessivité intense envers tes partenaires ou attirer des partenaires possessifs.",
        "En intégrant cette Lilith, tu accèdes à un amour profondément charnel et loyal. Tu crées des liens durables et sensuels.",
        "En maison VII, cette énergie peut créer de la jalousie ou des attachements excessifs. Transforme la possessivité en dévotion saine.",
        "Exprime ton amour de façon sensuelle et ancrée.",
        "Respire en aimant sans chercher à posséder.",
        "Quelle possessivité relationnelle ai-je refoulée ou attirée ? »"),

    ('taurus', 8): make_lilith_interp('taurus', 8,
        "Ton ombre se loge dans l'attachement face à la perte — ton pouvoir est celui de la transformation matérielle.",
        "Lilith en Taureau dans ta maison VIII place ton ombre dans ta relation à la perte et au partage des ressources. Tu peux avoir une peur intense de perdre ce que tu as.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer les ressources et de renaître matériellement. Tu peux reconstruire après les pertes.",
        "En maison VIII, cette énergie crée une tension entre l'attachement et le lâcher-prise. Apprends que la vraie richesse survit à la perte.",
        "Lâche un attachement matériel consciemment.",
        "Respire en faisant confiance à ta capacité de reconstruire.",
        "Quelle peur de la perte matérielle porte mon inconscient ? »"),

    ('taurus', 9): make_lilith_interp('taurus', 9,
        "Ton ombre se loge dans le matérialisme spirituel — ton pouvoir est celui de la sagesse incarnée.",
        "Lilith en Taureau dans ta maison IX place ton ombre dans ta relation entre matière et esprit. Tu peux soit rejeter le matériel soit t'y accrocher dans ta quête spirituelle.",
        "En intégrant cette Lilith, tu accèdes à une spiritualité profondément incarnée. Tu trouves le sacré dans la matière.",
        "En maison IX, cette énergie peut créer des conflits entre confort et expansion. Apprends que le voyage peut être aussi ancré que libre.",
        "Trouve le sacré dans quelque chose de matériel.",
        "Respire en intégrant esprit et matière.",
        "Comment ma relation au matériel affecte-t-elle ma spiritualité ? »"),

    ('taurus', 10): make_lilith_interp('taurus', 10,
        "Ton ombre se loge dans l'ambition matérielle — ton pouvoir est celui de construire durablement.",
        "Lilith en Taureau dans ta maison X place ton ombre dans ta carrière et ton statut. Tu peux avoir une ambition de richesse refoulée ou une honte de vouloir le confort.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de construire une carrière solide et prospère. Tu crées une réputation de stabilité.",
        "En maison X, cette énergie peut créer une relation complexe au succès matériel. Assume ton désir de prospérité sans culpabilité.",
        "Construis quelque chose de durable dans ta carrière.",
        "Respire en assumant ton ambition de prospérité.",
        "Quelle honte ou obsession autour du succès matériel ai-je refoulée ? »"),

    ('taurus', 11): make_lilith_interp('taurus', 11,
        "Ton ombre se loge dans les valeurs de groupe — ton pouvoir est celui d'ancrer les idéaux.",
        "Lilith en Taureau dans ta maison XI place ton ombre dans ta relation aux groupes et aux valeurs partagées. Tu peux avoir des conflits autour des ressources collectives.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'ancrer les idéaux dans la réalité matérielle. Tu donnes de la substance aux rêves collectifs.",
        "En maison XI, cette énergie peut créer des tensions autour du partage ou de la possessivité dans les groupes. Apporte stabilité sans rigidité.",
        "Contribue de façon concrète à un idéal collectif.",
        "Respire en ancrant les rêves dans la matière.",
        "Quels conflits autour des ressources collectives ai-je refoulés ? »"),

    ('taurus', 12): make_lilith_interp('taurus', 12,
        "Ton ombre se loge dans l'attachement karmique — ton pouvoir est celui de la présence incarnée.",
        "Lilith en Taureau dans ta maison XII place ton ombre dans l'inconscient et le karma. Tu peux avoir des attachements profonds à des vies passées ou à des désirs refoulés.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de présence même dans la dissolution. Tu restes ancré dans les profondeurs.",
        "En maison XII, cette énergie peut créer des addictions sensuelles ou un attachement à des schémas passés. Transmute l'attachement en ancrage spirituel.",
        "Médite en sentant ton corps comme un temple.",
        "Respire en ancrant ta spiritualité dans la chair.",
        "Quels attachements karmiques ou désirs refoulés porte mon inconscient ? »"),

    # === GEMINI (M1-M12) ===
    ('gemini', 1): make_lilith_interp('gemini', 1,
        "Ton ombre se loge dans la duplicité et le mensonge — ton pouvoir est celui de la communication libérée.",
        "Lilith en Gémeaux dans ta maison I place ton ombre dans ton identité et ta parole. Tu peux avoir refoulé une capacité à manipuler par les mots ou une double personnalité.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de communication fluide et libre. Tu peux parler de tout et te réinventer à volonté.",
        "En maison I, cette énergie peut créer une personnalité changeante ou des mensonges identitaires. Embrasse ta multiplicité sans tromper.",
        "Exprime une facette de toi que tu cachais.",
        "Respire en embrassant ta nature multiple.",
        "Quelle partie de ma personnalité ai-je cachée ou menti sur elle ? »"),

    ('gemini', 2): make_lilith_interp('gemini', 2,
        "Ton ombre se loge dans la manipulation financière — ton pouvoir est celui de l'intelligence des affaires.",
        "Lilith en Gémeaux dans ta maison II place ton ombre dans ta relation à l'argent et à la valeur. Tu peux avoir utilisé des mots ou des idées pour obtenir des ressources de façon questionnable.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer de la valeur par tes idées et ta communication. Tes mots génèrent de la richesse.",
        "En maison II, cette énergie peut créer une relation entre intelligence et argent. Utilise ton esprit pour créer de la valeur éthiquement.",
        "Monétise une de tes idées de façon éthique.",
        "Respire en valorisant ton intelligence comme une ressource.",
        "Où ai-je utilisé des mots ou des idées de façon manipulatrice pour obtenir des ressources ? »"),

    ('gemini', 3): make_lilith_interp('gemini', 3,
        "Ton ombre se loge dans la parole qui blesse — ton pouvoir est celui de la vérité libératrice.",
        "Lilith en Gémeaux dans ta maison III (son domicile) place ton ombre dans la communication même. Tu peux avoir une langue de vipère refoulée ou des mots qui tuent.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de parole exceptionnel. Tu peux nommer l'innommable et libérer par les mots.",
        "En maison III, cette énergie est particulièrement puissante. Tes mots ont un pouvoir de vie et de mort. Utilise-les avec conscience.",
        "Dis une vérité que personne n'ose dire.",
        "Respire en honorant le pouvoir de tes mots.",
        "Quels mots destructeurs ai-je retenus ou utilisés ? »"),

    ('gemini', 4): make_lilith_interp('gemini', 4,
        "Ton ombre se loge dans les secrets de famille — ton pouvoir est celui de nommer les non-dits.",
        "Lilith en Gémeaux dans ta maison IV place ton ombre dans les communications familiales. Tu peux avoir appris le mensonge ou le secret dans ta famille.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de révéler les secrets familiaux et de nommer ce qui était tu. Tu brises le silence.",
        "En maison IV, cette énergie peut avoir créé un environnement de non-dits ou de doubles messages. Tu deviens celui qui dit la vérité de la famille.",
        "Nomme un secret ou un non-dit familial.",
        "Respire en libérant les mots retenus par ta lignée.",
        "Quels secrets ou mensonges familiaux ai-je portés ? »"),

    ('gemini', 5): make_lilith_interp('gemini', 5,
        "Ton ombre se loge dans la séduction intellectuelle — ton pouvoir est celui de l'expression créative libre.",
        "Lilith en Gémeaux dans ta maison V place ton ombre dans la créativité et les jeux amoureux. Tu peux avoir séduit par l'esprit ou joué des jeux de manipulation.",
        "En intégrant cette Lilith, tu accèdes à une créativité verbale et intellectuelle débridée. Tu crées avec les mots et séduis par l'intelligence.",
        "En maison V, cette énergie peut créer des amours intellectuels ou des jeux de séduction par les mots. Séduis avec authenticité.",
        "Crée quelque chose de verbalement audacieux.",
        "Respire en célébrant ta créativité mentale.",
        "Où ai-je utilisé mon intelligence pour séduire ou manipuler ? »"),

    ('gemini', 6): make_lilith_interp('gemini', 6,
        "Ton ombre se loge dans les commérages et la critique — ton pouvoir est celui de l'analyse pénétrante.",
        "Lilith en Gémeaux dans ta maison VI place ton ombre dans la communication au travail. Tu peux avoir été critique, commère ou manipulateur dans ton environnement professionnel.",
        "En intégrant cette Lilith, tu accèdes à une capacité d'analyse fine et de communication efficace. Tu peux améliorer par les mots.",
        "En maison VI, cette énergie peut créer des tensions verbales au travail. Transforme la critique en feedback constructif.",
        "Communique une analyse utile de façon constructive.",
        "Respire en utilisant tes mots pour améliorer.",
        "Où mes mots ont-ils été destructeurs au travail ? »"),

    ('gemini', 7): make_lilith_interp('gemini', 7,
        "Ton ombre se loge dans les relations doubles — ton pouvoir est celui de la communication relationnelle.",
        "Lilith en Gémeaux dans ta maison VII place ton ombre dans tes partenariats. Tu peux avoir eu des relations doubles, des triangles ou des mensonges relationnels.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de communication exceptionnelle dans les relations. Tu crées des liens par le dialogue.",
        "En maison VII, cette énergie peut créer des relations complexes ou des tromperies. Apprends à être authentique dans tes partenariats.",
        "Communique avec totale transparence dans une relation.",
        "Respire en créant la connexion par les mots vrais.",
        "Quels mensonges ou doubles jeux ai-je pratiqués en relation ? »"),

    ('gemini', 8): make_lilith_interp('gemini', 8,
        "Ton ombre se loge dans les secrets et les manipulations — ton pouvoir est celui de nommer les tabous.",
        "Lilith en Gémeaux dans ta maison VIII place ton ombre dans les communications profondes et les secrets. Tu peux détenir des informations puissantes ou avoir manipulé par le secret.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de parler de ce qui est tabou. Tu nommes les ombres et les transformes par les mots.",
        "En maison VIII, cette énergie est particulièrement puissante. Tes mots peuvent révéler ou détruire. Utilise ce pouvoir avec sagesse.",
        "Parle d'un sujet tabou avec conscience.",
        "Respire en assumant le pouvoir de tes révélations.",
        "Quels secrets ai-je gardés qui me donnent du pouvoir ? »"),

    ('gemini', 9): make_lilith_interp('gemini', 9,
        "Ton ombre se loge dans les mensonges idéologiques — ton pouvoir est celui de questionner toute vérité.",
        "Lilith en Gémeaux dans ta maison IX place ton ombre dans tes croyances et ta quête de vérité. Tu peux avoir menti sur tes croyances ou douté de toute vérité.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de questionnement et de pensée libre. Tu peux déconstruire n'importe quel dogme.",
        "En maison IX, cette énergie peut créer un scepticisme extrême ou un prosélytisme mental. Questionne sans tomber dans le nihilisme.",
        "Questionne une croyance que tu tenais pour vraie.",
        "Respire en honorant ta capacité à penser librement.",
        "Quels mensonges intellectuels ou spirituels ai-je entretenus ? »"),

    ('gemini', 10): make_lilith_interp('gemini', 10,
        "Ton ombre se loge dans la réputation de menteur — ton pouvoir est celui de la communication publique.",
        "Lilith en Gémeaux dans ta maison X place ton ombre dans ta réputation et ta communication professionnelle. Tu peux avoir été taxé de menteur ou avoir manipulé ton image.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de communication publique et d'influence par les mots. Tu peux façonner ton image.",
        "En maison X, cette énergie peut créer une réputation de beau parleur ou de manipulateur. Construis une réputation d'authenticité.",
        "Communique publiquement avec totale authenticité.",
        "Respire en assumant ta parole publique.",
        "Comment ai-je manipulé mon image ou ma réputation par les mots ? »"),

    ('gemini', 11): make_lilith_interp('gemini', 11,
        "Ton ombre se loge dans les manipulations de groupe — ton pouvoir est celui de connecter les gens.",
        "Lilith en Gémeaux dans ta maison XI place ton ombre dans les communications de groupe. Tu peux avoir été l'agent de rumeurs ou avoir manipulé des dynamiques collectives.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de réseautage et de connexion. Tu crées des ponts entre les gens par la communication.",
        "En maison XI, cette énergie peut créer des tensions dans les groupes par les mots. Utilise ta parole pour rassembler, pas diviser.",
        "Connecte des personnes par tes mots.",
        "Respire en créant des liens par la communication.",
        "Comment ai-je manipulé ou divisé des groupes par mes paroles ? »"),

    ('gemini', 12): make_lilith_interp('gemini', 12,
        "Ton ombre se loge dans les pensées refoulées — ton pouvoir est celui de la parole inconsciente.",
        "Lilith en Gémeaux dans ta maison XII place ton ombre dans l'inconscient et les pensées cachées. Tu peux avoir des pensées que tu n'oses pas exprimer ou une voix intérieure critique.",
        "En intégrant cette Lilith, tu accèdes à une communication avec l'invisible. Tu peux canaliser des messages et parler pour l'inconscient collectif.",
        "En maison XII, cette énergie peut créer un mental hyperactif ou des pensées obsédantes. Calme l'esprit et écoute la voix au-delà des mots.",
        "Écoute les pensées que tu n'oses pas exprimer.",
        "Respire en faisant silence dans ton mental.",
        "Quelles pensées refoulées habitent mon inconscient ? »"),

    # === CANCER (M1-M12) ===
    ('cancer', 1): make_lilith_interp('cancer', 1,
        "Ton ombre se loge dans la mère dévorante ou absente — ton pouvoir est celui de la maternance sauvage.",
        "Lilith en Cancer dans ta maison I place ton ombre dans ta relation à la mère et à ton identité nourricière. Tu peux avoir refoulé un côté maternel écrasant ou un manque.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de maternance instinctive et brute. Tu peux nourrir et protéger avec une force primitive.",
        "En maison I, cette énergie est très visible dans ta personnalité. Tu peux osciller entre dévoration et abandon. Trouve l'équilibre du soin.",
        "Prends soin de quelqu'un ou de toi-même de façon instinctive.",
        "Respire en embrassant ta nature nourricière.",
        "Quel schéma maternel ai-je refoulé ou hérité ? »"),

    ('cancer', 2): make_lilith_interp('cancer', 2,
        "Ton ombre se loge dans la sécurité émotionnelle — ton pouvoir est celui de l'abondance nourricière.",
        "Lilith en Cancer dans ta maison II place ton ombre dans ta relation à la sécurité matérielle et émotionnelle. Tu peux avoir une insécurité profonde ou un besoin excessif de contrôle.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer la sécurité par le soin. Tu nourris et tu reçois de l'abondance.",
        "En maison II, cette énergie peut créer une relation entre émotions et argent. Apprends que la vraie sécurité vient de l'intérieur.",
        "Crée de la sécurité par le soin plutôt que par le contrôle.",
        "Respire en te sentant sécurisé de l'intérieur.",
        "Quel lien existe entre mon insécurité émotionnelle et matérielle ? »"),

    ('cancer', 3): make_lilith_interp('cancer', 3,
        "Ton ombre se loge dans la communication émotionnelle — ton pouvoir est celui des mots qui touchent.",
        "Lilith en Cancer dans ta maison III place ton ombre dans ta communication et tes émotions. Tu peux avoir refoulé une communication chargée émotionnellement.",
        "En intégrant cette Lilith, tu accèdes à une parole qui touche le cœur. Tes mots ont le pouvoir de nourrir ou de blesser profondément.",
        "En maison III, cette énergie peut créer des échanges chargés avec l'entourage proche. Apprends à communiquer tes émotions avec conscience.",
        "Exprime une émotion profonde avec des mots.",
        "Respire en connectant ton cœur à ta parole.",
        "Quelles émotions n'ai-je jamais osé communiquer ? »"),

    ('cancer', 4): make_lilith_interp('cancer', 4,
        "Ton ombre se loge dans les blessures familiales — ton pouvoir est celui de guérir la lignée.",
        "Lilith en Cancer dans ta maison IV (son domicile) place ton ombre dans ta famille et tes racines. Tu portes des blessures maternelles ou familiales intenses.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformation de ta lignée. Tu peux briser les schémas et guérir les traumatismes familiaux.",
        "En maison IV, cette énergie est particulièrement puissante. Tu es l'alchimiste de ta famille. Transforme les ombres en lumière.",
        "Honore et transforme une blessure familiale.",
        "Respire en sentant ta capacité à guérir ta lignée.",
        "Quelle blessure familiale ou maternelle porte mon inconscient ? »"),

    ('cancer', 5): make_lilith_interp('cancer', 5,
        "Ton ombre se loge dans l'amour maternel ou l'enfant intérieur — ton pouvoir est celui de l'amour instinctif.",
        "Lilith en Cancer dans ta maison V place ton ombre dans ta créativité et tes amours. Tu peux avoir un rapport complexe à l'enfant intérieur ou à la maternité.",
        "En intégrant cette Lilith, tu accèdes à un amour et une créativité profondément instinctifs. Tu crées et aimes avec tout ton être.",
        "En maison V, cette énergie peut créer des drames autour des enfants ou de l'amour. Apprends à aimer sans étouffer.",
        "Crée ou aime de façon instinctive et fluide.",
        "Respire en accueillant ton enfant intérieur.",
        "Quel rapport à l'enfant intérieur ou à la maternité est dans l'ombre ? »"),

    ('cancer', 6): make_lilith_interp('cancer', 6,
        "Ton ombre se loge dans le service et le sacrifice — ton pouvoir est celui du soin quotidien.",
        "Lilith en Cancer dans ta maison VI place ton ombre dans ton rapport au service et à la santé. Tu peux te sacrifier excessivement ou négliger ton propre soin.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de soin et de service instinctif. Tu nourris par ton travail quotidien.",
        "En maison VI, cette énergie peut créer des problèmes de santé liés aux émotions ou un sacrifice excessif. Prends soin de toi aussi.",
        "Nourris ton corps et ton âme dans ton quotidien.",
        "Respire en te donnant le soin que tu donnes aux autres.",
        "Où me suis-je sacrifié au détriment de ma propre santé ? »"),

    ('cancer', 7): make_lilith_interp('cancer', 7,
        "Ton ombre se loge dans la dépendance relationnelle — ton pouvoir est celui de l'intimité profonde.",
        "Lilith en Cancer dans ta maison VII place ton ombre dans tes relations intimes. Tu peux avoir des schémas de dépendance ou de fusion excessifs.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer une intimité profonde et nourricière. Tu crées des relations qui soignent.",
        "En maison VII, cette énergie peut créer des relations parent-enfant ou des dépendances mutuelles. Apprends l'intimité dans l'autonomie.",
        "Crée de l'intimité sans perdre ton autonomie.",
        "Respire en te sentant complet même en relation.",
        "Quels schémas de dépendance ai-je dans mes relations ? »"),

    ('cancer', 8): make_lilith_interp('cancer', 8,
        "Ton ombre se loge dans les émotions refoulées — ton pouvoir est celui de transformer par les émotions.",
        "Lilith en Cancer dans ta maison VIII place ton ombre dans les émotions profondes et les transformations. Tu peux avoir refoulé un deuil ou des émotions liées à la perte.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformation émotionnelle. Tu traverses les crises avec l'instinct et le cœur.",
        "En maison VIII, cette énergie peut créer des crises émotionnelles intenses ou des deuils compliqués. Apprends à traverser les émotions.",
        "Traverse une émotion intense sans la refouler.",
        "Respire en laissant les émotions te transformer.",
        "Quelles émotions de perte ou de transformation ai-je refoulées ? »"),

    ('cancer', 9): make_lilith_interp('cancer', 9,
        "Ton ombre se loge dans les croyances émotionnelles — ton pouvoir est celui de la sagesse du cœur.",
        "Lilith en Cancer dans ta maison IX place ton ombre dans tes croyances et ta relation à l'étranger. Tu peux avoir des croyances teintées d'insécurité ou de peur de l'inconnu.",
        "En intégrant cette Lilith, tu accèdes à une sagesse intuitive et émotionnelle. Tu trouves la vérité par le cœur.",
        "En maison IX, cette énergie peut créer un attachement aux croyances de ta famille ou une peur de l'expansion. Explore avec confiance.",
        "Explore une croyance nouvelle avec ton cœur.",
        "Respire en faisant confiance à ta sagesse émotionnelle.",
        "Comment mes insécurités ont-elles façonné mes croyances ? »"),

    ('cancer', 10): make_lilith_interp('cancer', 10,
        "Ton ombre se loge dans le conflit carrière-famille — ton pouvoir est celui de la carrière nourricière.",
        "Lilith en Cancer dans ta maison X place ton ombre dans ta carrière et ta vie publique. Tu peux avoir des conflits entre ambition et famille ou une carrière dans le soin.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer une carrière qui nourrit. Tu deviens une figure publique protectrice.",
        "En maison X, cette énergie peut créer des tensions entre vie privée et publique. Intègre le soin dans ta mission professionnelle.",
        "Apporte du soin dans ta vie professionnelle.",
        "Respire en assumant ton rôle nourricier dans le monde.",
        "Quel conflit carrière-famille porte mon inconscient ? »"),

    ('cancer', 11): make_lilith_interp('cancer', 11,
        "Ton ombre se loge dans l'appartenance émotionnelle — ton pouvoir est celui de créer une famille choisie.",
        "Lilith en Cancer dans ta maison XI place ton ombre dans tes groupes et amitiés. Tu peux avoir cherché une famille dans les groupes ou te sentir émotionnellement exclu.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer des communautés nourricières. Tu fais des amitiés une famille.",
        "En maison XI, cette énergie peut créer une dépendance émotionnelle aux groupes ou un besoin de materner le collectif. Appartiens sans te perdre.",
        "Crée un lien familial avec des amis ou un groupe.",
        "Respire en te sentant appartenir à ta tribu choisie.",
        "Quel besoin d'appartenance émotionnelle ai-je dans les groupes ? »"),

    ('cancer', 12): make_lilith_interp('cancer', 12,
        "Ton ombre se loge dans la mère cosmique — ton pouvoir est celui de l'amour universel.",
        "Lilith en Cancer dans ta maison XII place ton ombre dans l'inconscient collectif et la maternité universelle. Tu peux porter les blessures maternelles de l'humanité.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de maternage universel. Tu peux nourrir l'âme collective et guérir les blessures collectives.",
        "En maison XII, cette énergie est transpersonnelle. Tu es connecté à la mère cosmique et aux blessures de toutes les mères. Canalise cette compassion.",
        "Médite en envoyant de l'amour maternel au monde.",
        "Respire en sentant la mère universelle en toi.",
        "Quelle blessure maternelle collective ou karmique porte mon âme ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in LILITH_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'lilith',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP lilith/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='lilith',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT lilith/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
