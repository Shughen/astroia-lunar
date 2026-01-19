#!/usr/bin/env python3
"""Insert Pluto interpretations for Aries, Taurus, Gemini, Cancer (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_pluto_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'aries': '♇ Pluton en Bélier',
        'taurus': '♇ Pluton en Taureau',
        'gemini': '♇ Pluton en Gémeaux',
        'cancer': '♇ Pluton en Cancer',
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

PLUTO_INTERPRETATIONS = {
    # === ARIES (M1-M12) ===
    ('aries', 1): make_pluto_interp('aries', 1,
        "Tu transformes ta vie par l'affirmation radicale de ton identité unique.",
        "Pluton en Bélier dans ta maison I t'offre un pouvoir de renaissance personnelle exceptionnel. Chaque crise devient l'occasion de te réinventer complètement, de détruire les anciennes versions de toi pour renaître plus authentique.",
        "Apprendre à canaliser ton intensité sans détruire ce qui t'entoure. Ta puissance peut effrayer ou fasciner — trouver l'équilibre entre affirmation et domination est ton travail d'une vie.",
        "Ton apparence physique et ta présence portent une charge magnétique intense. Les gens sentent immédiatement ta force. Tu renais littéralement à travers des transformations corporelles ou de style radical.",
        "Regarde-toi dans un miroir et dis à voix haute : « Je suis ma propre révolution. »",
        "Respire profondément en visualisant un feu qui brûle ce qui ne te sert plus.",
        "Quelle partie de moi suis-je prêt(e) à laisser mourir aujourd'hui ? »"),

    ('aries', 2): make_pluto_interp('aries', 2,
        "Tu transformes ta vie par une relation intense et combative avec l'argent et les possessions.",
        "Pluton en Bélier dans ta maison II te pousse à conquérir la sécurité matérielle avec une énergie guerrière. L'argent est pour toi un terrain de bataille où tu prouves ta valeur.",
        "Éviter les comportements destructeurs autour des finances — dépenses impulsives ou obsession du contrôle. Ton rapport à l'argent reflète ton rapport au pouvoir personnel.",
        "Tes revenus connaissent des cycles de destruction et reconstruction. Tu peux tout perdre et tout reconstruire avec une force phénoménale. La possession devient un acte d'affirmation identitaire.",
        "Tiens un billet ou une pièce en main et ressens l'énergie de transformation qu'il représente.",
        "Respire en visualisant l'abondance qui coule vers toi comme une source intarissable.",
        "Qu'est-ce que je suis prêt(e) à sacrifier pour ma liberté financière ? »"),

    ('aries', 3): make_pluto_interp('aries', 3,
        "Tu transformes ta vie par une parole percutante et une pensée révolutionnaire.",
        "Pluton en Bélier dans ta maison III fait de ta communication une arme de transformation. Tes mots ont le pouvoir de détruire des illusions et d'éveiller les consciences.",
        "Apprendre à mesurer l'impact de tes paroles — elles peuvent blesser profondément. Le défi est d'utiliser cette puissance verbale pour construire plutôt que démolir.",
        "Tes relations avec frères, sœurs ou voisins passent par des crises transformatrices. Chaque conversation peut devenir un duel ou une alliance profonde. L'apprentissage est un combat passionnant.",
        "Écris une phrase qui dit exactement ce que tu penses vraiment, sans filtre.",
        "Respire en imaginant tes mots comme des flèches de lumière qui éclairent la vérité.",
        "Quelle vérité ai-je peur de dire à voix haute ? »"),

    ('aries', 4): make_pluto_interp('aries', 4,
        "Tu transformes ta vie par une reconstruction radicale de tes racines familiales.",
        "Pluton en Bélier dans ta maison IV indique des dynamiques de pouvoir intenses dans ta famille d'origine. Tu es là pour briser des schémas familiaux anciens avec courage.",
        "Ne pas reproduire les luttes de pouvoir familiales dans ta propre vie. Transformer l'héritage de conflits en héritage de force authentique demande un travail profond.",
        "Ton foyer est un lieu de transformation constante. Tu peux déménager de façon radicale ou rénover intensément. La relation au père ou à l'autorité parentale porte une charge karmique puissante.",
        "Touche un objet familial et remercie-le pour ce qu'il t'a appris, bon ou difficile.",
        "Respire en visualisant ta lignée derrière toi, transformée en lumière de soutien.",
        "Quel schéma familial suis-je en train de guérir par ma propre transformation ? »"),

    ('aries', 5): make_pluto_interp('aries', 5,
        "Tu transformes ta vie par une créativité ardente et des amours passionnelles.",
        "Pluton en Bélier dans ta maison V fait de ta créativité un volcan. Tes œuvres portent une intensité qui touche profondément les autres. L'amour est pour toi un terrain de renaissance.",
        "Éviter les relations amoureuses destructrices ou les créations qui brûlent tout. Ta passion doit trouver des canaux constructifs pour ne pas consumer tout ce qu'elle touche.",
        "Tes romances sont intenses, transformatrices, parfois douloureuses. La relation aux enfants (réels ou créatifs) implique des dynamiques de pouvoir à conscientiser. Le jeu devient un acte de libération.",
        "Crée quelque chose d'impulsif pendant 2 minutes — dessin, danse, quelques mots.",
        "Respire en visualisant un feu créatif qui brûle dans ton cœur sans te consumer.",
        "Qu'est-ce qui demande à naître de moi aujourd'hui ? »"),

    ('aries', 6): make_pluto_interp('aries', 6,
        "Tu transformes ta vie par une approche guerrière de la santé et du travail.",
        "Pluton en Bélier dans ta maison VI te pousse à transformer radicalement tes habitudes. Le travail quotidien devient un terrain de conquête personnelle et de dépassement.",
        "Éviter le burn-out par excès de combativité. Ton corps parle fort — apprendre à écouter ses signaux d'alerte plutôt que de foncer tête baissée.",
        "Ta santé passe par des cycles de crise et régénération. Le travail peut être source de conflits de pouvoir ou d'affirmation personnelle intense. Le service aux autres est une forme de combat sacré.",
        "Fais un mouvement physique intense pendant 30 secondes — jumping jacks, squats.",
        "Respire en visualisant chaque cellule de ton corps se régénérer avec puissance.",
        "Quelle habitude destructrice suis-je prêt(e) à éliminer maintenant ? »"),

    ('aries', 7): make_pluto_interp('aries', 7,
        "Tu transformes ta vie par des relations intenses qui te confrontent à ton propre pouvoir.",
        "Pluton en Bélier dans ta maison VII attire des partenaires puissants qui te transforment. Chaque relation significative est un miroir de ton ombre et de ta force.",
        "Éviter les dynamiques de domination/soumission dans le couple. L'enjeu est de créer des partenariats d'égal à égal où la puissance de chacun est honorée.",
        "Tes associations passent par des crises transformatrices. Les ruptures sont des morts symboliques qui te permettent de renaître. L'ennemi peut devenir allié, et vice versa.",
        "Pense à une personne qui te confronte et remercie-la intérieurement pour cette croissance.",
        "Respire en visualisant l'équilibre des forces entre toi et un partenaire.",
        "Qu'est-ce que mes relations m'apprennent sur mon propre pouvoir ? »"),

    ('aries', 8): make_pluto_interp('aries', 8,
        "Tu transformes ta vie par une plongée courageuse dans les profondeurs de la psyché.",
        "Pluton en Bélier dans ta maison VIII (son domicile naturel) décuple ta capacité de transformation. Tu n'as pas peur de regarder la mort, le sexe, les tabous en face.",
        "Éviter de devenir obsédé par le pouvoir occulte ou la manipulation. Cette position puissante demande une éthique impeccable dans tout ce qui touche aux ressources partagées.",
        "La sexualité est transformatrice, parfois tantrique. Les héritages et dettes karmiques se règlent avec toi. Tu as un don pour accompagner les autres dans leurs propres morts/renaissances.",
        "Ferme les yeux et imagine ce que tu libérerais si tu n'avais plus peur de rien.",
        "Respire profondément en accueillant l'ombre comme une partie sacrée de toi.",
        "Quel secret suis-je prêt(e) à transformer en force aujourd'hui ? »"),

    ('aries', 9): make_pluto_interp('aries', 9,
        "Tu transformes ta vie par une quête spirituelle passionnée et conquérante.",
        "Pluton en Bélier dans ta maison IX fait de toi un guerrier spirituel. Ta philosophie de vie se forge dans le feu de l'expérience directe et des voyages transformateurs.",
        "Éviter le fanatisme ou l'imposition de tes croyances aux autres. Ta conviction peut devenir une arme — le défi est de l'utiliser pour libérer plutôt qu'opprimer.",
        "Les voyages lointains sont des initiations. L'éducation supérieure transforme radicalement ta vision du monde. Tu peux devenir un guide spirituel puissant ou un enseignant révolutionnaire.",
        "Lis ou écoute une phrase de sagesse et laisse-la te traverser comme une flèche de lumière.",
        "Respire en visualisant l'horizon qui s'élargit infiniment devant toi.",
        "Quelle croyance limitante suis-je prêt(e) à brûler aujourd'hui ? »"),

    ('aries', 10): make_pluto_interp('aries', 10,
        "Tu transformes ta vie par une ambition féroce et une carrière de pionnier.",
        "Pluton en Bélier dans ta maison X te destine à une carrière qui transforme le monde. Tu veux être le premier, ouvrir des voies nouvelles, marquer l'histoire de ton empreinte.",
        "Éviter les luttes de pouvoir destructrices dans le milieu professionnel. Ton ambition peut te mener très haut ou très bas — l'éthique du pouvoir est ton examen constant.",
        "Ta réputation publique passe par des transformations radicales. Tu peux être adulé puis critiqué, pour renaître encore plus fort. La relation aux figures d'autorité est intense et karmique.",
        "Visualise-toi au sommet de ta carrière et ressens cette puissance dans ton corps.",
        "Respire en imaginant que chaque expiration te rapproche de ta destinée.",
        "Quel héritage veux-je laisser au monde ? »"),

    ('aries', 11): make_pluto_interp('aries', 11,
        "Tu transformes ta vie par un engagement révolutionnaire dans les causes collectives.",
        "Pluton en Bélier dans ta maison XI fait de toi un leader de mouvements. Tes amitiés sont intenses et transformatrices. Tu attires des alliés puissants pour des causes audacieuses.",
        "Éviter de vouloir dominer les groupes ou de confondre engagement et guerre. Le défi est de catalyser le changement collectif sans imposer ta vision personnelle.",
        "Tes réseaux sociaux passent par des ruptures et reconstructions. Les projets collectifs te transforment profondément. Tu peux être le fer de lance d'une révolution sociale ou technologique.",
        "Pense à une cause qui te passionne et envoie-lui mentalement ton énergie de soutien.",
        "Respire en visualisant un cercle d'alliés puissants qui partagent ta vision.",
        "Quelle révolution suis-je appelé(e) à initier ou soutenir ? »"),

    ('aries', 12): make_pluto_interp('aries', 12,
        "Tu transformes ta vie par un combat spirituel avec tes démons intérieurs.",
        "Pluton en Bélier dans ta maison XII te confronte à des peurs profondes et des ennemis cachés — souvent en toi-même. Ta force réside dans ta capacité à transmuter l'ombre en lumière.",
        "Éviter la projection de tes propres parts sombres sur les autres. Le travail est intérieur — descendre dans tes enfers personnels pour en revenir transformé.",
        "L'inconscient est un champ de bataille et de trésor. Les rêves sont intenses et révélateurs. Les épreuves cachées forgent une force spirituelle exceptionnelle.",
        "Ferme les yeux et dialogue avec une peur — demande-lui ce qu'elle protège.",
        "Respire en visualisant une lumière qui descend dans les profondeurs de ton être.",
        "Quel combat intérieur suis-je en train de gagner silencieusement ? »"),

    # === TAURUS (M1-M12) ===
    ('taurus', 1): make_pluto_interp('taurus', 1,
        "Tu transformes ta vie par une reconstruction lente mais totale de ton rapport au corps.",
        "Pluton en Taureau dans ta maison I te donne un magnétisme terrestre puissant. Ta présence physique dégage une force tranquille mais implacable. Les transformations corporelles sont profondes.",
        "Apprendre à lâcher prise sur le contrôle des ressources et du corps. Ta résistance au changement peut devenir destructrice — accepter les cycles de mort/renaissance physique.",
        "Ton apparence se transforme lentement mais radicalement au fil des années. Tu incarnes la puissance de la nature — patient, endurant, mais capable de séismes quand tu bouges.",
        "Touche ta peau consciemment et remercie ton corps pour sa capacité de régénération.",
        "Respire en sentant tes pieds ancrés dans la terre, comme des racines profondes.",
        "Quel aspect de mon apparence ou de ma présence est en train de se transformer ? »"),

    ('taurus', 2): make_pluto_interp('taurus', 2,
        "Tu transformes ta vie par une relation obsessionnelle puis libérée à l'argent.",
        "Pluton en Taureau dans ta maison II (son domicile naturel) intensifie ton rapport aux possessions. Tu as le pouvoir de créer et détruire de grandes fortunes. L'argent est un pouvoir que tu dois maîtriser.",
        "Éviter l'avarice obsessionnelle ou la destruction de tes ressources. Ton défi est de transformer ton rapport à la matière pour qu'elle serve ta croissance plutôt qu'elle ne t'emprisonne.",
        "Tes finances passent par des cycles de mort et renaissance. Tu peux tout perdre et reconstruire mieux. Les possessions ont une dimension karmique — certaines choses viennent à toi pour être transformées.",
        "Tiens un objet précieux et demande-toi s'il te possède ou si tu le possèdes vraiment.",
        "Respire en visualisant l'énergie de l'abondance qui circule librement à travers toi.",
        "Quelle relation à l'argent suis-je en train de transformer profondément ? »"),

    ('taurus', 3): make_pluto_interp('taurus', 3,
        "Tu transformes ta vie par une communication profonde et enracinée.",
        "Pluton en Taureau dans ta maison III donne à tes paroles un poids considérable. Tu parles peu mais chaque mot compte. Ta pensée est lente, profonde, transformatrice.",
        "Éviter la rumination obsessionnelle ou le mutisme défensif. Le défi est de communiquer tes transformations intérieures sans te fermer ou dominer par le silence.",
        "Les relations avec frères, sœurs ou voisins passent par des transformations profondes. L'apprentissage est lent mais permanent — ce que tu apprends s'inscrit dans ta chair.",
        "Écris lentement une seule phrase qui exprime une vérité profonde pour toi.",
        "Respire en imaginant tes mots comme des graines plantées dans une terre fertile.",
        "Quelle parole ai-je besoin de dire, même si elle me coûte ? »"),

    ('taurus', 4): make_pluto_interp('taurus', 4,
        "Tu transformes ta vie par un ancrage profond puis une libération des héritages familiaux.",
        "Pluton en Taureau dans ta maison IV ancre des transformations générationnelles dans ta lignée. La terre ancestrale, la propriété familiale portent une charge intense à transmuter.",
        "Éviter de t'accrocher à des possessions familiales par peur du changement. Ton défi est de transformer l'héritage matériel en héritage de valeurs vivantes.",
        "Ton foyer est un lieu de transformation lente mais totale. Les déménagements sont rares mais radicaux. Le rapport à la mère ou aux racines porte des enjeux de possession à libérer.",
        "Touche un mur de ton logement et ressens toute l'histoire qu'il contient.",
        "Respire en visualisant les racines de ton arbre familial se purifier dans la terre.",
        "Quel attachement familial suis-je prêt(e) à transformer ou libérer ? »"),

    ('taurus', 5): make_pluto_interp('taurus', 5,
        "Tu transformes ta vie par une créativité sensuelle et des amours profondes.",
        "Pluton en Taureau dans ta maison V rend ta créativité charnelle, presque érotique. Tes œuvres ont une présence physique qui touche les sens. L'amour est une fusion terrestre intense.",
        "Éviter la possessivité destructrice en amour ou l'attachement obsessionnel à tes créations. Le défi est de laisser mourir les vieilles formes pour que de nouvelles naissent.",
        "Les romances sont lentes à s'établir mais transformatrices. La relation aux enfants ou à la créativité implique des leçons sur la possession et le lâcher-prise. Les plaisirs sont intenses.",
        "Crée quelque chose avec tes mains — touche la matière et transforme-la.",
        "Respire en ressentant le plaisir simple d'être vivant dans un corps.",
        "Quelle création demande à naître de mes mains aujourd'hui ? »"),

    ('taurus', 6): make_pluto_interp('taurus', 6,
        "Tu transformes ta vie par un travail patient et une santé à reconstruire.",
        "Pluton en Taureau dans ta maison VI fait de ton travail quotidien un terrain de transformation profonde. Ta santé physique reflète tes processus de mort/renaissance intérieurs.",
        "Éviter de négliger ton corps jusqu'à la crise. Le défi est de maintenir des habitudes durables qui soutiennent ta transformation plutôt que de tout changer d'un coup.",
        "Ton rapport au travail passe par des cycles de stabilité et bouleversement. Le corps demande une attention constante — alimentation, sommeil, rythmes sont des terrains de transformation.",
        "Fais un étirement lent et profond en sentant chaque muscle se régénérer.",
        "Respire en visualisant chaque organe de ton corps recevoir de l'énergie guérissante.",
        "Quelle habitude de santé suis-je en train de transformer en profondeur ? »"),

    ('taurus', 7): make_pluto_interp('taurus', 7,
        "Tu transformes ta vie par des partenariats stables mais profondément transformateurs.",
        "Pluton en Taureau dans ta maison VII attire des partenaires qui transforment ton rapport aux valeurs et à la sécurité. Le couple est un terrain d'ancrage et de bouleversement.",
        "Éviter la possessivité étouffante ou la résistance au changement dans les relations. Ton défi est de construire des partenariats qui évoluent sans se figer.",
        "Tes associations sont durables mais passent par des mues profondes. Le partenaire peut représenter tes propres enjeux autour de l'argent, du corps, de la possession.",
        "Pense à un partenaire et visualise l'énergie qui circule entre vous sans attachement.",
        "Respire en ressentant l'équilibre entre donner et recevoir dans tes relations.",
        "Qu'est-ce que mes relations m'apprennent sur mon rapport à la sécurité ? »"),

    ('taurus', 8): make_pluto_interp('taurus', 8,
        "Tu transformes ta vie par une gestion puissante des ressources partagées.",
        "Pluton en Taureau dans ta maison VIII intensifie tout ce qui touche à l'argent commun, l'héritage, les dettes. La sexualité est profonde, terrestre, transformatrice.",
        "Éviter les manipulations financières ou l'attachement obsessionnel aux possessions héritées. Le défi est de transformer ta relation à ce qui t'est donné par d'autres.",
        "Les héritages matériels portent des charges karmiques à transmuter. La mort physique d'un proche peut être un catalyseur de transformation profonde. Le tantra est ton domaine naturel.",
        "Visualise un bien hérité ou partagé et libère tout attachement excessif.",
        "Respire en imaginant les richesses karmiques qui se transforment en bénédictions.",
        "Quelle dette émotionnelle ou matérielle suis-je prêt(e) à libérer ? »"),

    ('taurus', 9): make_pluto_interp('taurus', 9,
        "Tu transformes ta vie par une philosophie enracinée et des voyages initiatiques.",
        "Pluton en Taureau dans ta maison IX ancre ta spiritualité dans le corps et la terre. Ta philosophie se construit lentement mais solidement. Les voyages te transforment physiquement.",
        "Éviter de figer tes croyances ou de résister aux expansions de conscience. Le défi est de garder ta sagesse ancrée tout en restant ouvert aux remises en question.",
        "L'éducation supérieure transforme ton rapport au monde matériel. Les voyages dans la nature ou vers des lieux anciens sont particulièrement puissants. Tu incarnes une sagesse terrestre.",
        "Touche la terre (ou une plante) et connecte-toi à la sagesse de la nature.",
        "Respire en sentant ton corps comme un temple de sagesse ancestrale.",
        "Quelle vérité mon corps connaît-il que mon mental ignore encore ? »"),

    ('taurus', 10): make_pluto_interp('taurus', 10,
        "Tu transformes ta vie par une carrière qui construit des structures durables.",
        "Pluton en Taureau dans ta maison X te destine à bâtir des entreprises ou institutions solides. Ta réputation se construit lentement mais devient indestructible.",
        "Éviter de t'accrocher au pouvoir ou au statut acquis. Le défi est de laisser mourir les vieilles structures professionnelles quand elles ne servent plus ta croissance.",
        "Ta carrière passe par des transformations lentes mais radicales. Tu peux devenir une autorité dans tout ce qui touche à la terre, l'argent, le corps, la construction.",
        "Visualise ta contribution professionnelle comme un bâtiment solide qui traverse le temps.",
        "Respire en ressentant la solidité de ce que tu construis dans le monde.",
        "Quelle structure professionnelle suis-je en train de construire ou transformer ? »"),

    ('taurus', 11): make_pluto_interp('taurus', 11,
        "Tu transformes ta vie par des amitiés durables et des projets à long terme.",
        "Pluton en Taureau dans ta maison XI t'amène des amis loyaux mais rares. Tes projets collectifs visent des changements concrets et durables dans le monde matériel.",
        "Éviter la possessivité dans les amitiés ou la résistance au changement des groupes. Le défi est de contribuer à des évolutions collectives sans vouloir les contrôler.",
        "Tes réseaux sont stables mais passent par des transformations profondes. Tu peux être un pilier pour des mouvements écologiques ou économiques alternatifs.",
        "Pense à un ami fidèle et envoie-lui mentalement de la gratitude pour sa constance.",
        "Respire en visualisant un cercle d'alliés qui construisent ensemble quelque chose de durable.",
        "Quelle contribution concrète puis-je apporter au collectif ? »"),

    ('taurus', 12): make_pluto_interp('taurus', 12,
        "Tu transformes ta vie par un travail profond sur les attachements inconscients.",
        "Pluton en Taureau dans ta maison XII te confronte à des peurs profondes autour de la perte, du manque, de l'insécurité. Ton travail spirituel passe par le corps.",
        "Éviter de fuir dans l'accumulation ou de te couper de tes besoins corporels. Le défi est de transformer ton rapport à la matière au niveau le plus profond.",
        "L'inconscient porte des mémoires de privation ou d'abus de ressources à transmuter. La retraite dans la nature est profondément régénératrice. Les rêves parlent du corps et de la terre.",
        "Allonge-toi et laisse la terre (le sol) supporter tout ton poids sans effort.",
        "Respire en visualisant la terre qui absorbe tes peurs et les transforme en engrais.",
        "Quel attachement inconscient mon corps porte-t-il encore ? »"),

    # === GEMINI (M1-M12) ===
    ('gemini', 1): make_pluto_interp('gemini', 1,
        "Tu transformes ta vie par une réinvention constante de ton identité et de ta parole.",
        "Pluton en Gémeaux dans ta maison I fait de ta personnalité un kaléidoscope en perpétuelle transformation. Ta présence est électrique, ton esprit acéré — tu fascines et déstabilises.",
        "Apprendre à aller en profondeur au lieu de survoler. Ta multiplicité peut devenir dispersion si tu évites les transformations profondes par le changement constant.",
        "Ton apparence et ton style changent souvent, reflétant tes mues intérieures. Tu as plusieurs facettes qui peuvent dérouter — chaque version de toi est une mort et renaissance.",
        "Regarde-toi dans un miroir et nomme trois versions différentes de toi-même.",
        "Respire en sentant les multiples facettes de ton être coexister harmonieusement.",
        "Quelle version de moi demande à émerger aujourd'hui ? »"),

    ('gemini', 2): make_pluto_interp('gemini', 2,
        "Tu transformes ta vie par une relation fluide mais intense à l'argent et aux idées.",
        "Pluton en Gémeaux dans ta maison II lie ta valeur personnelle à ta capacité de communication. L'argent vient et va au gré de tes idées — la vraie richesse est intellectuelle.",
        "Éviter la dispersion financière ou les manipulations par la parole. Ton défi est de valoriser tes talents de communication sans en abuser.",
        "Tes revenus sont variables, liés aux activités de communication, d'écriture, de commerce. Les biens matériels passent par des cycles rapides d'acquisition et de libération.",
        "Écris trois façons dont tes talents de communication peuvent te rapporter de la valeur.",
        "Respire en visualisant tes idées qui se transforment en ressources concrètes.",
        "Comment puis-je mieux valoriser mes capacités intellectuelles ? »"),

    ('gemini', 3): make_pluto_interp('gemini', 3,
        "Tu transformes ta vie par une communication profondément transformatrice.",
        "Pluton en Gémeaux dans ta maison III (son domicile naturel) fait de toi un maître des mots qui transforment. Ta parole a un pouvoir hypnotique — tu peux changer les esprits.",
        "Éviter la manipulation verbale ou la dispersion mentale. Le défi est d'utiliser ton pouvoir de persuasion de façon éthique et de penser profondément plutôt que brillamment.",
        "Les relations avec frères, sœurs ou voisins sont intenses et transformatrices. Chaque conversation peut être un tournant. L'écriture, l'enseignement sont des voies de pouvoir.",
        "Écris une phrase destinée à transformer la pensée de quelqu'un — puis ressens son poids.",
        "Respire en imaginant tes mots comme des clés qui ouvrent des portes fermées.",
        "Quelle vérité ai-je le pouvoir de transmettre aujourd'hui ? »"),

    ('gemini', 4): make_pluto_interp('gemini', 4,
        "Tu transformes ta vie par une réinvention constante de ton rapport aux racines.",
        "Pluton en Gémeaux dans ta maison IV indique un foyer mental agité, des racines multiples. Tu peux avoir plusieurs maisons ou une maison qui bouge constamment d'idées.",
        "Éviter la superficialité dans les liens familiaux ou la fuite par le mental. Le défi est de créer de vraies racines émotionnelles malgré ta mobilité naturelle.",
        "Ton histoire familiale est marquée par des secrets de communication ou des non-dits puissants. Le foyer est un lieu d'échanges intenses — le silence peut être assourdissant.",
        "Appelle ou écris à quelqu'un de ta famille et partage une chose vraie que tu n'as jamais dite.",
        "Respire en visualisant tes racines comme un réseau de connexions plutôt qu'un ancrage fixe.",
        "Quel secret familial demande à être mis en lumière ou transformé ? »"),

    ('gemini', 5): make_pluto_interp('gemini', 5,
        "Tu transformes ta vie par une créativité verbale et des amours stimulantes.",
        "Pluton en Gémeaux dans ta maison V fait de ta créativité un jeu d'esprit intense. Tes œuvres ont du mordant, de l'ironie, une profondeur cachée sous la légèreté.",
        "Éviter le cynisme ou la manipulation dans les relations amoureuses. Le défi est de laisser ton cœur s'engager vraiment plutôt que de jouer aux jeux de l'esprit.",
        "Les romances sont des joutes verbales stimulantes. La relation aux enfants passe par la communication — éduquer, transmettre, dialoguer. Le jeu est intellectuel mais intense.",
        "Écris un petit texte créatif qui dit ce que ton cœur ressent vraiment.",
        "Respire en laissant ton mental se calmer pour que la créativité du cœur émerge.",
        "Comment puis-je exprimer ma créativité avec plus de profondeur émotionnelle ? »"),

    ('gemini', 6): make_pluto_interp('gemini', 6,
        "Tu transformes ta vie par un travail intellectuel intense et une santé du système nerveux.",
        "Pluton en Gémeaux dans ta maison VI fait du travail mental ton quotidien. Ton système nerveux est ton baromètre — stress et régénération passent par là.",
        "Éviter la surcharge mentale qui épuise le corps. Le défi est de transformer ton rapport au travail pour qu'il nourrisse plutôt qu'il draine ton énergie nerveuse.",
        "Ton travail quotidien implique communication, écriture, échanges multiples. La santé demande attention aux poumons, aux mains, au système respiratoire. L'anxiété est ton signal d'alarme.",
        "Arrête toute activité mentale pendant 2 minutes — juste respirer et être présent.",
        "Respire lentement en comptant jusqu'à 4 à l'inspire, 6 à l'expire pour calmer le mental.",
        "Comment puis-je simplifier mon travail quotidien pour protéger mon énergie ? »"),

    ('gemini', 7): make_pluto_interp('gemini', 7,
        "Tu transformes ta vie par des partenariats stimulants et des dialogues transformateurs.",
        "Pluton en Gémeaux dans ta maison VII attire des partenaires vifs d'esprit qui te challengent. Le couple est un espace de dialogue intense — les mots peuvent blesser ou guérir.",
        "Éviter les jeux de pouvoir par la parole ou la manipulation dans les relations. Ton défi est de créer une vraie intimité au-delà de la brillance des échanges.",
        "Tes associations passent par des phases de communication intense puis de silence. Les contrats et négociations ont une dimension de pouvoir. L'autre est ton miroir intellectuel.",
        "Écris trois choses que tu n'as jamais osé dire à un partenaire, même sur papier.",
        "Respire en visualisant un dialogue où chacun parle et écoute vraiment.",
        "Qu'est-ce que j'ai peur de dire ou d'entendre dans mes relations proches ? »"),

    ('gemini', 8): make_pluto_interp('gemini', 8,
        "Tu transformes ta vie par une exploration mentale des tabous et des mystères.",
        "Pluton en Gémeaux dans ta maison VIII t'attire vers la psychologie des profondeurs, l'occultisme, les secrets. Tu as un don pour mettre des mots sur l'indicible.",
        "Éviter l'obsession mentale des sujets sombres ou la manipulation par l'information. Le défi est de transformer par la parole sans rester bloqué dans les ténèbres.",
        "La sexualité passe par les mots — le dirty talk, l'écriture érotique, la communication intime. Les héritages peuvent inclure des documents, des secrets, des connaissances cachées.",
        "Écris sur un sujet tabou que tu n'oses pas aborder à voix haute.",
        "Respire en visualisant les mots qui dissolvent les peurs et les secrets.",
        "Quel mystère suis-je appelé(e) à explorer ou à révéler ? »"),

    ('gemini', 9): make_pluto_interp('gemini', 9,
        "Tu transformes ta vie par une quête intellectuelle de vérité et des voyages de l'esprit.",
        "Pluton en Gémeaux dans ta maison IX fait de toi un chercheur infatigable de vérité. Ta philosophie évolue constamment — chaque nouvelle information peut tout remettre en question.",
        "Éviter le cynisme intellectuel ou la quête sans fin qui n'aboutit jamais. Le défi est de trouver des vérités auxquelles t'ancrer tout en restant ouvert.",
        "Les études supérieures sont transformatrices. Les voyages sont des quêtes d'information, de connexion. Tu peux devenir un passeur de connaissances profondes.",
        "Lis ou écoute une idée nouvelle et laisse-la transformer ta vision du monde.",
        "Respire en visualisant ton esprit qui s'ouvre comme un ciel infini.",
        "Quelle croyance suis-je prêt(e) à questionner ou transformer ? »"),

    ('gemini', 10): make_pluto_interp('gemini', 10,
        "Tu transformes ta vie par une carrière dans la communication et le pouvoir des mots.",
        "Pluton en Gémeaux dans ta maison X te destine à influencer par la parole, l'écriture, les médias. Ta réputation est liée à ton intelligence et ton pouvoir de persuasion.",
        "Éviter les manipulations de l'opinion publique ou la dispersion professionnelle. Le défi est de construire une autorité stable basée sur la profondeur, pas seulement la brillance.",
        "Ta carrière passe par des changements de direction multiples mais cohérents. Tu peux devenir une figure publique dans les médias, l'éducation, la politique par le verbe.",
        "Écris une phrase qui résume ta mission professionnelle — ton message au monde.",
        "Respire en visualisant tes mots qui touchent des milliers de personnes.",
        "Quel message suis-je destiné(e) à transmettre au monde ? »"),

    ('gemini', 11): make_pluto_interp('gemini', 11,
        "Tu transformes ta vie par des réseaux intellectuels et des projets de communication.",
        "Pluton en Gémeaux dans ta maison XI t'amène des amis brillants et stimulants. Tes projets collectifs visent à transformer par l'information, l'éducation, la connexion.",
        "Éviter les cercles toxiques de rumeurs ou la manipulation des groupes. Le défi est de créer des réseaux authentiques où l'échange est vraiment transformateur.",
        "Tes amitiés passent par des phases de connexion intense et de silence. Les projets collectifs utilisent la technologie, les médias, l'écriture comme outils de changement.",
        "Contacte un ami pour un échange authentique — pas de small talk, une vraie question.",
        "Respire en visualisant un réseau de connexions lumineuses qui s'étend.",
        "Comment mes connexions peuvent-elles servir quelque chose de plus grand ? »"),

    ('gemini', 12): make_pluto_interp('gemini', 12,
        "Tu transformes ta vie par un travail sur les pensées obsessionnelles et les peurs mentales.",
        "Pluton en Gémeaux dans ta maison XII te confronte à l'ombre de ton mental — pensées intrusives, anxiétés cachées, doubles intérieurs. L'inconscient parle et tu dois l'écouter.",
        "Éviter de fuir les pensées sombres par l'hyperactivité mentale. Le défi est de descendre sous la surface brillante de l'esprit pour y trouver la sagesse cachée.",
        "L'inconscient est bavard — rêves complexes, intuitions fulgurantes, voix intérieures. L'écriture automatique ou le journaling sont des outils puissants de transformation.",
        "Écris pendant 2 minutes sans t'arrêter, laissant sortir tout ce qui vient.",
        "Respire en laissant les pensées passer comme des nuages sans t'y accrocher.",
        "Quelle pensée cachée demande à être vue et transformée ? »"),

    # === CANCER (M1-M12) ===
    ('cancer', 1): make_pluto_interp('cancer', 1,
        "Tu transformes ta vie par une exploration profonde de tes émotions et de ton identité.",
        "Pluton en Cancer dans ta maison I te donne une intensité émotionnelle palpable. Ta présence touche les gens au niveau du cœur. Tes transformations personnelles sont profondes et viscérales.",
        "Apprendre à ne pas te laisser submerger par l'intensité de tes propres émotions. Ta sensibilité est un pouvoir — mais aussi une vulnérabilité à protéger.",
        "Ton apparence reflète tes états émotionnels profonds. Tu peux sembler fermé puis soudain t'ouvrir avec une intensité qui déroute. Les mues identitaires passent par le cœur.",
        "Pose ta main sur ton cœur et demande-lui comment il se sent vraiment, maintenant.",
        "Respire en visualisant une coquille protectrice autour de ton cœur sensible.",
        "Quelle émotion demande à être pleinement ressentie et transformée ? »"),

    ('cancer', 2): make_pluto_interp('cancer', 2,
        "Tu transformes ta vie par un rapport émotionnel intense à la sécurité matérielle.",
        "Pluton en Cancer dans ta maison II lie ta valeur personnelle à ta capacité à nourrir et protéger. L'argent est émotionnel — tu accumules par peur du manque ou donnes par amour.",
        "Éviter les comportements de thésaurisation anxieuse ou de dépendance financière. Le défi est de transformer ton rapport à la sécurité pour qu'il ne soit plus basé sur la peur.",
        "Tes finances reflètent tes états émotionnels. Les biens ont une valeur sentimentale qui dépasse le matériel. Tu investis dans la maison, la famille, ce qui nourrit le cœur.",
        "Touche un objet qui te rappelle un être cher et ressens sa valeur émotionnelle.",
        "Respire en visualisant l'abondance comme une mer nourricière qui ne tarit jamais.",
        "Quelle peur autour de l'argent suis-je prêt(e) à transformer en confiance ? »"),

    ('cancer', 3): make_pluto_interp('cancer', 3,
        "Tu transformes ta vie par une communication émotionnellement profonde.",
        "Pluton en Cancer dans ta maison III donne à ta parole une charge émotionnelle intense. Tu communiques avec le cœur — tes mots peuvent réconforter ou blesser profondément.",
        "Éviter la manipulation émotionnelle ou le repli dans le silence boudeur. Le défi est d'exprimer tes émotions profondes de façon constructive.",
        "Les relations avec frères, sœurs ou voisins sont émotionnellement chargées. L'apprentissage passe par le ressenti. Tu retiens ce qui touche ton cœur.",
        "Écris une lettre à quelqu'un, même sans l'envoyer, en disant ce que ton cœur ressent.",
        "Respire en laissant tes émotions colorer tes pensées sans les submerger.",
        "Quelle émotion ai-je besoin de communiquer à quelqu'un de proche ? »"),

    ('cancer', 4): make_pluto_interp('cancer', 4,
        "Tu transformes ta vie par une plongée dans les profondeurs de ton histoire familiale.",
        "Pluton en Cancer dans ta maison IV (son domicile naturel) concentre d'intenses transformations autour de la famille et du foyer. Les racines sont ton terrain de mort/renaissance.",
        "Éviter de reproduire les schémas toxiques familiaux ou de rester prisonnier du passé. Le défi est de transformer l'héritage émotionnel pour les générations futures.",
        "Ton foyer est un utérus symbolique de transformation. La relation à la mère ou à la lignée maternelle porte des enjeux karmiques profonds. Les souvenirs d'enfance ont un pouvoir transformateur.",
        "Regarde une photo de famille ancienne et laisse les émotions te traverser librement.",
        "Respire en visualisant l'amour de ta lignée qui te soutient, malgré les blessures.",
        "Quel pattern familial suis-je en train de transformer par ma propre guérison ? »"),

    ('cancer', 5): make_pluto_interp('cancer', 5,
        "Tu transformes ta vie par une créativité émotionnelle et des amours maternantes.",
        "Pluton en Cancer dans ta maison V rend ta créativité profondément émotionnelle. Tes œuvres touchent le cœur. L'amour est maternel, protecteur, parfois étouffant.",
        "Éviter la surprotection en amour ou la création par besoin de validation émotionnelle. Le défi est de créer et aimer depuis la plénitude plutôt que le manque.",
        "Les romances impliquent des dynamiques de soin et de protection. La relation aux enfants (réels ou symboliques) est intensément émotionnelle. Le jeu est régressif, guérisseur.",
        "Crée quelque chose qui exprime une émotion que tu as du mal à dire avec des mots.",
        "Respire en visualisant ton cœur qui s'ouvre comme une fleur qui offre sa beauté.",
        "Quelle création pourrait naître de la tendresse que je porte en moi ? »"),

    ('cancer', 6): make_pluto_interp('cancer', 6,
        "Tu transformes ta vie par un travail de soin et une attention à ton corps émotionnel.",
        "Pluton en Cancer dans ta maison VI fait du travail quotidien un acte de maternage. Ta santé est liée à tes émotions — le corps parle le langage du cœur.",
        "Éviter de te négliger pour prendre soin des autres ou de somatiser tes émotions. Le défi est de prendre soin de toi avec la même tendresse que tu offres aux autres.",
        "Ton travail implique souvent le soin — santé, alimentation, accueil. L'estomac et la poitrine sont tes zones sensibles. Les troubles alimentaires peuvent être des messages émotionnels.",
        "Prépare ou mange quelque chose de nourrissant en pleine conscience, avec amour.",
        "Respire en visualisant chaque cellule de ton corps recevoir de l'amour et de la tendresse.",
        "Comment puis-je mieux prendre soin de mon corps émotionnel au quotidien ? »"),

    ('cancer', 7): make_pluto_interp('cancer', 7,
        "Tu transformes ta vie par des partenariats émotionnellement intenses et protecteurs.",
        "Pluton en Cancer dans ta maison VII attire des partenaires avec qui tu crées une famille ou un nid émotionnel. Le couple est un cocon de transformation profonde.",
        "Éviter les relations de dépendance émotionnelle ou de maternage excessif. Le défi est de créer des partenariats d'adultes qui nourrissent sans étouffer.",
        "Tes associations sont des espaces de sécurité émotionnelle ou au contraire de grande vulnérabilité. Le partenaire peut représenter la mère ou réveiller des blessures d'abandon.",
        "Pense à un partenaire et visualise un lien d'amour qui vous relie sans vous enchaîner.",
        "Respire en ressentant l'équilibre entre donner du soin et recevoir du soin.",
        "Qu'est-ce que mes relations m'apprennent sur ma façon de nourrir et d'être nourri(e) ? »"),

    ('cancer', 8): make_pluto_interp('cancer', 8,
        "Tu transformes ta vie par une plongée dans les eaux profondes de l'émotionnel.",
        "Pluton en Cancer dans ta maison VIII intensifie les processus de mort et renaissance émotionnelle. Tu vis des deuils profonds qui te transforment au niveau cellulaire.",
        "Éviter de te noyer dans les émotions des autres ou de porter les fardeaux familiaux. Le défi est de transformer sans te perdre dans les profondeurs.",
        "La sexualité est fusionnelle, régressive, guérisseuse. Les héritages émotionnels de la lignée passent par toi pour être transmutés. Tu es un alchimiste des blessures familiales.",
        "Visualise une émotion difficile et imagine-la se transformer en lumière dans ton cœur.",
        "Respire en accueillant les vagues d'émotion comme des marées qui nettoient.",
        "Quelle blessure familiale suis-je en train de guérir à travers moi ? »"),

    ('cancer', 9): make_pluto_interp('cancer', 9,
        "Tu transformes ta vie par une spiritualité maternelle et des voyages vers les origines.",
        "Pluton en Cancer dans ta maison IX teinte ta philosophie d'une profonde sagesse émotionnelle. Ta spiritualité est celle de la Grande Mère, nourricière et cyclique.",
        "Éviter de projeter tes besoins maternels sur des figures spirituelles ou de fuir par les voyages. Le défi est de trouver une sagesse qui honore le cœur et le foyer.",
        "Les voyages vers les terres ancestrales sont transformateurs. L'éducation supérieure peut être liée à la psychologie, l'histoire, la généalogie. Tu enseignes avec le cœur.",
        "Recherche une image ou un symbole de la Grande Mère et médite dessus.",
        "Respire en visualisant la Terre comme une mère qui te porte et te nourrit.",
        "Quelle sagesse du cœur ai-je à partager avec le monde ? »"),

    ('cancer', 10): make_pluto_interp('cancer', 10,
        "Tu transformes ta vie par une carrière qui nourrit et protège.",
        "Pluton en Cancer dans ta maison X te destine à une carrière où tu prends soin — santé, éducation, restauration, immobilier. Ta réputation est celle d'un protecteur.",
        "Éviter de confondre vie professionnelle et vie familiale ou de chercher une figure parentale dans l'autorité. Le défi est de trouver ta propre autorité émotionnelle.",
        "Ta carrière passe par des transformations liées aux besoins familiaux. Tu peux devenir une figure maternelle/paternelle publique. Le foyer peut devenir ton lieu de travail.",
        "Visualise ta carrière comme un grand arbre qui offre ombre et fruits à ceux qui en ont besoin.",
        "Respire en ressentant la fierté d'une contribution qui nourrit vraiment le monde.",
        "Comment ma carrière peut-elle mieux servir mes valeurs de soin et de protection ? »"),

    ('cancer', 11): make_pluto_interp('cancer', 11,
        "Tu transformes ta vie par des amitiés familiales et des projets communautaires.",
        "Pluton en Cancer dans ta maison XI transforme tes amis en famille et ta famille en amis. Tes projets collectifs visent à créer des communautés nourricières.",
        "Éviter le favoritisme clanique ou l'exclusion de ceux qui sont « hors du cercle ». Le défi est d'élargir ton cercle de soin au-delà de ta tribu immédiate.",
        "Tes réseaux sociaux sont émotionnellement chargés. Les projets collectifs peuvent concerner la famille, le logement, l'alimentation, la santé communautaire.",
        "Invite un ami à partager un repas ou envoie-lui un message de soin sincère.",
        "Respire en visualisant ta communauté comme un grand village où chacun prend soin de l'autre.",
        "Comment puis-je contribuer à créer une communauté plus nourricière ? »"),

    ('cancer', 12): make_pluto_interp('cancer', 12,
        "Tu transformes ta vie par une guérison des blessures maternelles et ancestrales.",
        "Pluton en Cancer dans ta maison XII te connecte aux mémoires émotionnelles de ta lignée. L'inconscient est une mer de souvenirs — les douleurs familiales refont surface pour être guéries.",
        "Éviter de te perdre dans les émotions du passé ou de porter les fardeaux qui ne sont pas les tiens. Le défi est de transformer l'héritage émotionnel sans t'y noyer.",
        "Les rêves sont peuplés de figures familiales et d'images d'eau. Les retraites près de l'eau ou dans des lieux liés à tes origines sont profondément transformatrices.",
        "Prends un moment pour honorer tes ancêtres — dis merci à voix basse.",
        "Respire en visualisant une eau claire qui lave les mémoires douloureuses de ta lignée.",
        "Quelle mémoire ancestrale est prête à être libérée à travers moi ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in PLUTO_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'pluto',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP pluto/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='pluto',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT pluto/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
