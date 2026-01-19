#!/usr/bin/env python3
"""Insert Pluto interpretations for Leo, Virgo, Libra, Scorpio (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_pluto_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'leo': '♇ Pluton en Lion',
        'virgo': '♇ Pluton en Vierge',
        'libra': '♇ Pluton en Balance',
        'scorpio': '♇ Pluton en Scorpion',
    }
    sign_fr = {
        'leo': 'Lion',
        'virgo': 'Vierge',
        'libra': 'Balance',
        'scorpio': 'Scorpion',
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
    # === LEO (M1-M12) ===
    ('leo', 1): make_pluto_interp('leo', 1,
        "Tu transformes ta vie par une expression radicale de ta créativité et de ta royauté intérieure.",
        "Pluton en Lion dans ta maison I te donne une présence magnétique et charismatique. Tu rayonnes d'une puissance qui attire naturellement l'attention et l'admiration des autres.",
        "Apprendre à briller sans dominer ni écraser. Ton égo peut être ton plus grand allié ou ton pire ennemi — le travail est de transformer l'orgueil en noblesse d'âme.",
        "Ton apparence dégage une aura de pouvoir et de créativité. Les transformations personnelles passent par l'expression dramatique de ton identité. Tu renais à travers l'art de te présenter au monde.",
        "Regarde-toi dans un miroir et reconnais la royauté qui habite tes yeux.",
        "Respire en visualisant une couronne de lumière dorée sur ta tête.",
        "De quelle façon unique suis-je appelé(e) à briller aujourd'hui ? »"),

    ('leo', 2): make_pluto_interp('leo', 2,
        "Tu transformes ta vie par une relation créative et généreuse à l'argent.",
        "Pluton en Lion dans ta maison II lie ta valeur personnelle à ta capacité de créer et de donner généreusement. L'argent vient à toi quand tu exprimes pleinement tes talents.",
        "Éviter l'orgueil financier ou la dépense ostentatoire. Ton défi est de valoriser ta créativité sans que ton estime dépende de la reconnaissance matérielle.",
        "Tes revenus sont liés à tes dons créatifs, artistiques ou de leadership. Les possessions ont une dimension de prestige. Tu es généreux quand tu te sens reconnu.",
        "Offre quelque chose de précieux à quelqu'un — un compliment sincère, un objet, ton temps.",
        "Respire en visualisant l'abondance dorée qui coule de ton cœur vers le monde.",
        "Comment ma générosité peut-elle se transformer en abondance ? »"),

    ('leo', 3): make_pluto_interp('leo', 3,
        "Tu transformes ta vie par une communication dramatique et inspirante.",
        "Pluton en Lion dans ta maison III fait de ta parole un acte de création. Tu parles avec autorité et charisme — tes mots peuvent enflammer ou inspirer profondément.",
        "Éviter de monopoliser les conversations ou de dramatiser à l'excès. Le défi est de communiquer avec puissance tout en laissant de l'espace aux autres voix.",
        "Les relations avec frères, sœurs ou voisins impliquent des dynamiques de leadership. L'apprentissage passe par l'expression créative. Tu enseignes avec passion et théâtralité.",
        "Raconte une histoire de ta journée comme si c'était une épopée héroïque.",
        "Respire en sentant ta voix comme un instrument royal qui porte la lumière.",
        "Quelle vérité glorieuse ai-je le courage de proclamer ? »"),

    ('leo', 4): make_pluto_interp('leo', 4,
        "Tu transformes ta vie par une réinvention royale de ton rapport aux racines.",
        "Pluton en Lion dans ta maison IV fait de ta famille un royaume à gouverner ou à transformer. Ton foyer est un espace de création et d'expression personnelle intense.",
        "Éviter de dominer ta famille ou de chercher constamment l'admiration des proches. Le défi est de créer un foyer où chacun peut briller, pas seulement toi.",
        "Les dynamiques familiales impliquent des luttes de pouvoir autour de la reconnaissance. Le père ou une figure d'autorité a une présence puissante. Ton histoire familiale est épique.",
        "Crée quelque chose de beau dans ton espace de vie — décore, arrange, illumine.",
        "Respire en visualisant ton foyer comme un palais de lumière dorée.",
        "Comment puis-je transformer mon foyer en espace de rayonnement joyeux ? »"),

    ('leo', 5): make_pluto_interp('leo', 5,
        "Tu transformes ta vie par une créativité incandescente et des amours passionnelles.",
        "Pluton en Lion dans ta maison V (son domicile naturel) fait de toi un créateur puissant. Tes œuvres portent une force vitale extraordinaire. L'amour est un feu qui te consume et te régénère.",
        "Éviter l'égo créatif qui ne supporte pas la critique ou les amours trop centrées sur soi. Le défi est de créer et aimer généreusement, pas pour l'admiration.",
        "Les romances sont théâtrales, passionnées, parfois dramatiques. La relation aux enfants implique des enjeux de fierté et de transmission. Le jeu est un art de vivre royal.",
        "Crée quelque chose d'audacieux et de beau, juste pour le plaisir de créer.",
        "Respire en visualisant un soleil qui brille dans ton plexus solaire.",
        "Quelle œuvre magnifique demande à naître de moi ? »"),

    ('leo', 6): make_pluto_interp('leo', 6,
        "Tu transformes ta vie par un travail où tu peux briller et une santé du cœur.",
        "Pluton en Lion dans ta maison VI fait du travail quotidien un espace d'expression créative. Ta santé est liée à ta capacité d'être reconnu et d'exprimer ta vitalité.",
        "Éviter de vouloir être le leader en toute circonstance ou de négliger les tâches humbles. Le défi est de mettre ta créativité au service des autres sans demander la couronne.",
        "Ton travail doit te permettre de briller et de créer. Le cœur est ton organe clé — stress et joie impactent directement ta vitalité. L'exercice expressif (danse, théâtre) te régénère.",
        "Fais une tâche ordinaire avec panache et créativité, comme si c'était un art.",
        "Respire en envoyant de la lumière dorée à ton cœur physique.",
        "Comment puis-je transformer mon travail quotidien en expression de ma créativité ? »"),

    ('leo', 7): make_pluto_interp('leo', 7,
        "Tu transformes ta vie par des partenariats avec des êtres solaires et puissants.",
        "Pluton en Lion dans ta maison VII attire des partenaires charismatiques et créatifs. Le couple est une scène où deux royautés apprennent à partager le trône.",
        "Éviter les luttes de pouvoir pour savoir qui brille le plus. Le défi est de créer des partenariats où les deux personnes se valorisent mutuellement sans compétition.",
        "Tes associations ont une dimension théâtrale et passionnée. Le partenaire peut représenter ton propre besoin de reconnaissance. Les contrats impliquent des enjeux d'honneur.",
        "Offre un compliment sincère et généreux à un partenaire ou associé.",
        "Respire en visualisant deux soleils qui brillent ensemble sans se faire d'ombre.",
        "Comment puis-je permettre à mon partenaire de briller autant que moi ? »"),

    ('leo', 8): make_pluto_interp('leo', 8,
        "Tu transformes ta vie par une plongée dramatique dans les mystères de la vie et de la mort.",
        "Pluton en Lion dans ta maison VIII fait de toi un maître des transformations profondes avec style. La sexualité est un acte créatif puissant. Les crises deviennent des spectacles de renaissance.",
        "Éviter de dramatiser les transformations ou de chercher l'attention dans les moments sombres. Le défi est de traverser les épreuves avec dignité plutôt qu'avec orgueil.",
        "Les héritages peuvent inclure des œuvres créatives ou des lignées artistiques. La sexualité est dramatique, intense, créative. Tu peux accompagner les autres dans leurs transformations avec charisme.",
        "Visualise une épreuve passée et reconnais comment elle t'a rendu plus royal intérieurement.",
        "Respire en imaginant un phénix d'or qui renaît de ses cendres dans ta poitrine.",
        "Quelle transformation peut devenir mon chef-d'œuvre ? »"),

    ('leo', 9): make_pluto_interp('leo', 9,
        "Tu transformes ta vie par une quête philosophique glorieuse et des voyages royaux.",
        "Pluton en Lion dans ta maison IX fait de ta spiritualité une voie royale. Ta philosophie est expansive, généreuse, créative. Les voyages sont des aventures épiques.",
        "Éviter le dogmatisme arrogant ou la croyance que ta vérité est la seule. Le défi est de partager ta sagesse avec générosité plutôt qu'avec condescendance.",
        "L'éducation supérieure te permet de briller et d'inspirer. Les voyages vers des lieux de pouvoir ou de beauté te transforment. Tu peux devenir un enseignant ou guide charismatique.",
        "Partage une sagesse ou une inspiration avec quelqu'un, généreusement.",
        "Respire en visualisant l'horizon qui s'illumine d'une lumière dorée.",
        "Quelle vérité glorieuse suis-je appelé(e) à partager avec le monde ? »"),

    ('leo', 10): make_pluto_interp('leo', 10,
        "Tu transformes ta vie par une carrière où tu règnes et inspires.",
        "Pluton en Lion dans ta maison X te destine à une position de pouvoir et de reconnaissance. Ta réputation est liée à ta capacité de leadership créatif et de charisme public.",
        "Éviter l'abus de pouvoir ou la dépendance à l'admiration publique. Le défi est de servir depuis ta position de pouvoir plutôt que de simplement régner.",
        "Ta carrière passe par des transformations liées à la reconnaissance et au prestige. Tu peux devenir une figure publique dans les arts, le spectacle, le leadership. L'échec peut être dramatique mais la renaissance aussi.",
        "Visualise-toi accomplissant ta mission de vie devant un public qui t'applaudit.",
        "Respire en ressentant le poids léger mais réel d'une couronne sur ta tête.",
        "Quel héritage de lumière veux-je laisser au monde ? »"),

    ('leo', 11): make_pluto_interp('leo', 11,
        "Tu transformes ta vie par des amitiés créatives et des projets collectifs inspirants.",
        "Pluton en Lion dans ta maison XI t'amène des amis talentueux et charismatiques. Tes projets collectifs visent à créer quelque chose de beau et d'inspirant pour le monde.",
        "Éviter de vouloir être le leader de tous les groupes ou de dominer tes amis. Le défi est de contribuer à des projets collectifs où chacun peut briller.",
        "Tes réseaux sont composés de créateurs, d'artistes, de personnes qui veulent faire une différence visible. Les projets collectifs ont une dimension artistique ou de spectacle.",
        "Célèbre le succès ou le talent d'un ami avec une générosité sincère.",
        "Respire en visualisant un cercle d'amis où chacun est une étoile qui brille.",
        "Comment puis-je contribuer à un projet qui illumine la vie des autres ? »"),

    ('leo', 12): make_pluto_interp('leo', 12,
        "Tu transformes ta vie par un travail sur l'égo et une spiritualité créative cachée.",
        "Pluton en Lion dans ta maison XII te confronte à l'ombre de ton égo — besoin d'admiration, orgueil blessé, peur de l'insignifiance. Ton travail spirituel est de trouver ta lumière intérieure.",
        "Éviter de cacher tes talents par fausse modestie ou de nourrir secrètement un égo blessé. Le défi est de briller de l'intérieur sans avoir besoin d'audience.",
        "L'inconscient porte des rêves de gloire ou des blessures liées à la non-reconnaissance. La créativité peut être un chemin de guérison profond. Les retraites artistiques sont transformatrices.",
        "Crée quelque chose de beau sans le montrer à personne — juste pour ton âme.",
        "Respire en visualisant une lumière dorée qui brille au centre de ton être, invisible mais puissante.",
        "Quelle lumière intérieure ai-je peur de reconnaître en moi ? »"),

    # === VIRGO (M1-M12) ===
    ('virgo', 1): make_pluto_interp('virgo', 1,
        "Tu transformes ta vie par une amélioration constante de toi-même et un souci du détail.",
        "Pluton en Vierge dans ta maison I te donne une présence discrète mais intense. Tu analyses tout, y compris toi-même, avec une précision chirurgicale. Chaque détail compte.",
        "Apprendre à accepter l'imperfection — la tienne et celle du monde. Ta critique peut devenir destructrice si elle n'est pas tempérée par la compassion.",
        "Ton apparence est soignée, précise, fonctionnelle. Les transformations personnelles passent par des ajustements minutieux plutôt que des révolutions. Tu renais par le perfectionnement.",
        "Regarde-toi dans un miroir et trouve trois choses que tu apprécies sincèrement.",
        "Respire en accueillant chaque partie de toi exactement comme elle est.",
        "Quel petit ajustement peut transformer ma journée ? »"),

    ('virgo', 2): make_pluto_interp('virgo', 2,
        "Tu transformes ta vie par une gestion méticuleuse et transformatrice de tes ressources.",
        "Pluton en Vierge dans ta maison II lie ta valeur personnelle à ta capacité d'être utile et efficace. L'argent est un outil à utiliser avec précision et discernement.",
        "Éviter l'anxiété obsessionnelle autour des finances ou la dévalorisation par manque de perfection. Ton défi est de reconnaître ta valeur même dans l'imperfection.",
        "Tes revenus sont liés à des compétences pratiques, analytiques ou de service. Les possessions sont fonctionnelles, bien organisées. Tu économises de façon méthodique.",
        "Organise un petit espace de ta vie — un tiroir, un dossier — avec soin et intention.",
        "Respire en visualisant tes ressources parfaitement organisées et en croissance ordonnée.",
        "Comment puis-je mieux honorer la valeur de ce que j'ai ? »"),

    ('virgo', 3): make_pluto_interp('virgo', 3,
        "Tu transformes ta vie par une communication analytique et précise.",
        "Pluton en Vierge dans ta maison III fait de ton mental un outil d'analyse puissant. Tu communiques avec précision et peux décortiquer n'importe quel problème.",
        "Éviter la critique excessive ou l'analyse paralysante. Le défi est de communiquer de façon constructive plutôt que de pointer tous les défauts.",
        "Les relations avec frères, sœurs ou voisins impliquent des échanges pratiques et analytiques. L'apprentissage est méthodique et détaillé. Tu excelles dans la correction et l'édition.",
        "Écris une liste de trois choses que tu veux améliorer, avec des étapes concrètes.",
        "Respire en sentant ton mental devenir clair et ordonné.",
        "Quelle analyse constructive puis-je faire aujourd'hui ? »"),

    ('virgo', 4): make_pluto_interp('virgo', 4,
        "Tu transformes ta vie par une purification et organisation de ton espace familial.",
        "Pluton en Vierge dans ta maison IV fait de ton foyer un lieu à constamment améliorer. Les racines familiales portent des patterns de critique ou de perfectionnisme à transformer.",
        "Éviter de critiquer constamment ta famille ou ton logement. Le défi est de créer un foyer qui fonctionne sans être obsédé par sa perfection.",
        "Ton espace de vie est fonctionnel, organisé, en constante amélioration. La relation au parent Vierge ou critique est transformatrice. Les secrets familiaux concernent souvent la santé ou le service.",
        "Nettoie ou range un petit espace de ton foyer avec conscience et gratitude.",
        "Respire en visualisant ton foyer comme un organisme sain et bien ordonné.",
        "Quel aspect de mon histoire familiale ai-je besoin de purifier ? »"),

    ('virgo', 5): make_pluto_interp('virgo', 5,
        "Tu transformes ta vie par une créativité précise et des amours perfectionnistes.",
        "Pluton en Vierge dans ta maison V fait de ta créativité un artisanat raffiné. Tes œuvres sont techniques, détaillées, parfaitement exécutées. L'amour est un service attentif.",
        "Éviter de critiquer tes créations au point de les étouffer ou de pointer les défauts de tes amours. Le défi est de créer et aimer imparfaitement, avec joie.",
        "Les romances impliquent le souci du détail et le désir d'améliorer l'autre (ou d'être amélioré). La relation aux enfants peut être éducative et analytique. Le jeu a une dimension d'apprentissage.",
        "Crée quelque chose d'imparfait et célèbre-le exactement comme il est.",
        "Respire en accueillant la beauté de l'imperfection dans tout ce que tu crées.",
        "Comment puis-je laisser ma créativité s'exprimer sans censure ? »"),

    ('virgo', 6): make_pluto_interp('virgo', 6,
        "Tu transformes ta vie par une maîtrise du travail quotidien et de la santé.",
        "Pluton en Vierge dans ta maison VI (son domicile naturel) te rend expert des routines transformatrices. Ton approche de la santé est analytique et efficace. Le travail est ton terrain de transformation.",
        "Éviter l'obsession de la santé ou du travail parfait. Le défi est de servir et travailler avec excellence sans t'épuiser dans la quête de perfection.",
        "Ton corps répond aux ajustements précis — alimentation, exercice, repos. Le travail quotidien demande de l'analyse et de l'amélioration constante. Tu peux guérir par l'attention aux détails.",
        "Fais un petit ajustement à une habitude de santé et observe son effet.",
        "Respire en visualisant chaque système de ton corps fonctionnant parfaitement.",
        "Quel petit changement peut avoir le plus grand impact sur ma santé ? »"),

    ('virgo', 7): make_pluto_interp('virgo', 7,
        "Tu transformes ta vie par des partenariats pratiques et des attentes réalistes.",
        "Pluton en Vierge dans ta maison VII attire des partenaires utiles, pratiques ou perfectionnistes. Le couple est un terrain d'amélioration mutuelle et de service réciproque.",
        "Éviter de critiquer constamment ton partenaire ou d'attendre la perfection de lui. Le défi est d'aider à améliorer sans juger ni contrôler.",
        "Tes associations ont une dimension pratique et fonctionnelle. Le partenaire peut représenter ton critique intérieur ou ton désir de service. Les contrats sont détaillés et précis.",
        "Offre un service pratique à un partenaire — aide concrète, pas juste des mots.",
        "Respire en visualisant des relations où chacun aide l'autre à s'améliorer avec gentillesse.",
        "Comment puis-je mieux servir mes partenaires sans les critiquer ? »"),

    ('virgo', 8): make_pluto_interp('virgo', 8,
        "Tu transformes ta vie par une analyse précise des processus de mort et renaissance.",
        "Pluton en Vierge dans ta maison VIII te donne un regard analytique sur les mystères de la vie. Tu peux disséquer les processus psychologiques avec une précision remarquable.",
        "Éviter de vouloir tout comprendre ou contrôler dans les moments de crise. Le défi est d'accepter le mystère tout en utilisant ton intelligence pour naviguer les transformations.",
        "La sexualité est attentive, technique, avec un souci de l'autre. Les héritages peuvent inclure des dettes à organiser ou des problèmes de santé à comprendre. Tu analyses les tabous.",
        "Fais une liste de ce que tu veux laisser mourir et ce que tu veux garder.",
        "Respire en accueillant l'inconnu comme un territoire à explorer, pas à contrôler.",
        "Quel processus de transformation bénéficierait d'une analyse plus fine ? »"),

    ('virgo', 9): make_pluto_interp('virgo', 9,
        "Tu transformes ta vie par une quête méthodique de connaissance et de sagesse pratique.",
        "Pluton en Vierge dans ta maison IX fait de ta philosophie un système pratique et applicable. Ta spiritualité est sobre, discernante, orientée vers l'amélioration.",
        "Éviter le scepticisme qui rejette toute sagesse non prouvée. Le défi est de trouver un équilibre entre analyse critique et ouverture à la transcendance.",
        "L'éducation supérieure est méthodique et orientée vers l'application pratique. Les voyages ont une dimension d'étude ou de service. Tu enseignes par l'exemple et la précision.",
        "Étudie ou apprends quelque chose de nouveau avec attention et méthode.",
        "Respire en visualisant ta connaissance qui s'organise en une sagesse pratique.",
        "Quelle connaissance ai-je besoin d'approfondir pour mieux servir ? »"),

    ('virgo', 10): make_pluto_interp('virgo', 10,
        "Tu transformes ta vie par une carrière de service et d'expertise technique.",
        "Pluton en Vierge dans ta maison X te destine à une réputation d'expert ou de perfectionniste. Ta carrière repose sur tes compétences analytiques et ton souci du détail.",
        "Éviter de te définir uniquement par ta productivité ou de critiquer ton parcours. Le défi est de construire une carrière de service sans t'y perdre.",
        "Ta carrière passe par des phases de réorganisation et d'amélioration. Tu peux exceller dans la santé, l'analyse, la qualité, le service. La critique peut venir de figures d'autorité perfectionnistes.",
        "Évalue honnêtement une compétence que tu veux améliorer dans ta carrière.",
        "Respire en ressentant la satisfaction d'un travail bien fait.",
        "Comment ma carrière peut-elle mieux servir les autres avec excellence ? »"),

    ('virgo', 11): make_pluto_interp('virgo', 11,
        "Tu transformes ta vie par des amitiés utiles et des projets d'amélioration collective.",
        "Pluton en Vierge dans ta maison XI t'amène des amis pratiques et compétents. Tes projets collectifs visent à améliorer concrètement la vie des gens ou des systèmes.",
        "Éviter de critiquer tes amis ou de n'avoir que des amitiés « utiles ». Le défi est de contribuer aux groupes avec tes compétences tout en acceptant l'imperfection collective.",
        "Tes réseaux sont composés de professionnels, d'experts, de gens pratiques. Les projets collectifs ont une dimension de service ou d'amélioration sociale.",
        "Offre une compétence ou une aide pratique à un groupe ou une cause.",
        "Respire en visualisant des systèmes collectifs qui s'améliorent grâce à ton apport.",
        "Comment mes compétences peuvent-elles servir le bien commun ? »"),

    ('virgo', 12): make_pluto_interp('virgo', 12,
        "Tu transformes ta vie par une guérison de la critique intérieure et du perfectionnisme.",
        "Pluton en Vierge dans ta maison XII te confronte à l'ombre de ton mental analytique — critique incessante, anxiété, peur de l'imperfection. Ton travail spirituel est d'accueillir ce qui est.",
        "Éviter de te perdre dans l'auto-analyse ou de te flageller pour tes imperfections. Le défi est de trouver la paix avec ce qui ne peut pas être amélioré.",
        "L'inconscient porte des voix critiques à identifier et à apaiser. Les retraites de silence ou de service désintéressé sont profondément transformatrices. Guérir les autres peut guérir ton critique intérieur.",
        "Fais quelque chose d'imparfait intentionnellement et accueille le résultat avec amour.",
        "Respire en visualisant ta voix critique intérieure qui se transforme en conseiller bienveillant.",
        "Quelle imperfection suis-je prêt(e) à accueillir avec compassion ? »"),

    # === LIBRA (M1-M12) ===
    ('libra', 1): make_pluto_interp('libra', 1,
        "Tu transformes ta vie par une quête d'harmonie et d'équilibre dans ton identité.",
        "Pluton en Balance dans ta maison I te donne un charme magnétique et une présence diplomatique. Tu cherches l'harmonie tout en portant une intensité relationnelle profonde.",
        "Apprendre à te définir par toi-même plutôt qu'à travers le regard des autres. Ta quête d'équilibre peut masquer tes vraies opinions et désirs.",
        "Ton apparence est soignée, équilibrée, esthétique. Les transformations personnelles passent souvent par les relations. Tu renais à travers les miroirs que les autres te tendent.",
        "Regarde-toi dans un miroir et dis ce que TU penses vraiment, pas ce qui est diplomate.",
        "Respire en trouvant un équilibre entre plaire aux autres et être authentique.",
        "Comment puis-je mieux m'affirmer tout en restant en relation ? »"),

    ('libra', 2): make_pluto_interp('libra', 2,
        "Tu transformes ta vie par une relation équilibrée mais profonde à l'argent et au partage.",
        "Pluton en Balance dans ta maison II lie ta valeur personnelle à ta capacité de créer des partenariats équitables. L'argent est souvent partagé ou lié aux relations.",
        "Éviter de dépendre financièrement des autres ou de perdre ton sens de la valeur dans les compromis. Ton défi est de valoriser ta contribution unique dans les échanges.",
        "Tes revenus peuvent venir de domaines liés à la beauté, la justice, les relations. Les possessions sont souvent partagées ou acquises avec d'autres. Tu cherches l'équité dans les échanges.",
        "Évalue si tes échanges financiers sont vraiment équilibrés et ajuste si nécessaire.",
        "Respire en visualisant des flux d'abondance parfaitement équilibrés.",
        "Comment puis-je créer plus d'équité dans mes échanges financiers ? »"),

    ('libra', 3): make_pluto_interp('libra', 3,
        "Tu transformes ta vie par une communication diplomatique et équilibrée.",
        "Pluton en Balance dans ta maison III fait de ta parole un art de la négociation. Tu excelles à présenter différents points de vue et à trouver des terrains d'entente.",
        "Éviter de dire ce que les autres veulent entendre au détriment de ta vérité. Le défi est de communiquer avec diplomatie sans perdre ton authenticité.",
        "Les relations avec frères, sœurs ou voisins impliquent des dynamiques de partenariat. L'apprentissage est collaboratif. Tu peux exceller en médiation, en droit, en relations publiques.",
        "Dis une chose vraie que tu as tendance à adoucir par diplomatie.",
        "Respire en trouvant l'équilibre entre gentillesse et honnêteté.",
        "Quelle vérité diplomatique ai-je besoin de partager ? »"),

    ('libra', 4): make_pluto_interp('libra', 4,
        "Tu transformes ta vie par la création d'un foyer harmonieux et équilibré.",
        "Pluton en Balance dans ta maison IV fait de ton foyer un lieu de beauté et d'harmonie à construire. Les racines familiales portent des enjeux relationnels profonds.",
        "Éviter de sacrifier tes besoins pour maintenir la paix familiale. Le défi est de créer un foyer équilibré où tes propres besoins sont aussi honorés.",
        "Ton espace de vie est esthétique, équilibré, apaisant. La relation aux parents implique des dynamiques de partenariat ou de médiation. Les secrets familiaux concernent souvent les relations.",
        "Crée un moment de beauté et d'harmonie dans ton espace de vie.",
        "Respire en visualisant ton foyer comme un sanctuaire d'équilibre parfait.",
        "Comment puis-je créer plus d'harmonie chez moi tout en respectant mes besoins ? »"),

    ('libra', 5): make_pluto_interp('libra', 5,
        "Tu transformes ta vie par une créativité élégante et des amours équilibrées.",
        "Pluton en Balance dans ta maison V fait de ta créativité un art de l'équilibre et de la beauté. Tes œuvres cherchent l'harmonie parfaite. L'amour est une danse de partenariat.",
        "Éviter de te perdre dans l'autre au nom de l'amour ou de créer uniquement pour plaire. Le défi est de créer et aimer depuis ton centre, pas pour obtenir l'approbation.",
        "Les romances sont élégantes, équilibrées, parfois superficielles si elles évitent les conflits. La relation aux enfants implique des enjeux de justice et d'équité. Le jeu est social et esthétique.",
        "Crée quelque chose qui exprime TON goût, pas ce qui plaira aux autres.",
        "Respire en sentant la beauté de ton expression créative unique.",
        "Quelle création authentique demande à naître de moi ? »"),

    ('libra', 6): make_pluto_interp('libra', 6,
        "Tu transformes ta vie par un travail en partenariat et une santé équilibrée.",
        "Pluton en Balance dans ta maison VI fait du travail quotidien un espace de collaboration. Ta santé dépend de l'équilibre — stress relationnel et harmonie affectent directement ton corps.",
        "Éviter de tout faire pour maintenir la paix au travail ou de négliger ta santé pour les autres. Le défi est de trouver l'équilibre entre servir et te préserver.",
        "Ton travail implique souvent des partenariats ou des clients. Les reins et la zone lombaire sont tes zones sensibles. L'exercice en duo ou avec un coach te convient bien.",
        "Trouve un équilibre entre ce que tu donnes et ce que tu reçois dans ton travail.",
        "Respire en visualisant chaque partie de ton corps en équilibre parfait.",
        "Comment puis-je mieux équilibrer travail et bien-être personnel ? »"),

    ('libra', 7): make_pluto_interp('libra', 7,
        "Tu transformes ta vie par des partenariats intenses et transformateurs.",
        "Pluton en Balance dans ta maison VII (son domicile naturel) fait de tes relations des espaces de transformation profonde. Le couple est un miroir puissant de ton évolution.",
        "Éviter les relations de dépendance ou les jeux de pouvoir masqués par la politesse. Le défi est de créer des partenariats vrais où la transformation mutuelle est consciente.",
        "Tes associations sont destinées à te transformer profondément. Le partenaire peut être intense, magnétique, parfois manipulateur. Les contrats impliquent des enjeux de pouvoir cachés.",
        "Identifie une dynamique de pouvoir cachée dans une relation et nomme-la.",
        "Respire en visualisant des relations transparentes où chacun se transforme librement.",
        "Quelle vérité relationnelle ai-je peur de regarder en face ? »"),

    ('libra', 8): make_pluto_interp('libra', 8,
        "Tu transformes ta vie par une exploration équilibrée des mystères partagés.",
        "Pluton en Balance dans ta maison VIII lie les processus de transformation aux relations. La sexualité est un acte d'équilibre et de partage profond.",
        "Éviter de te perdre dans les drames relationnels ou de fuir les profondeurs par le charme. Le défi est d'explorer l'ombre ensemble sans perdre ton centre.",
        "Les héritages impliquent souvent des partenaires ou des ex. La sexualité est une danse d'équilibre entre donner et recevoir. Tu peux aider les couples à traverser les crises.",
        "Partage une vérité profonde avec quelqu'un de confiance.",
        "Respire en accueillant l'intimité vraie qui transforme les deux partenaires.",
        "Quelle profondeur suis-je prêt(e) à explorer avec un autre ? »"),

    ('libra', 9): make_pluto_interp('libra', 9,
        "Tu transformes ta vie par une philosophie de justice et d'équilibre universel.",
        "Pluton en Balance dans ta maison IX fait de ta spiritualité une quête de justice cosmique. Ta philosophie cherche l'équilibre entre les opposés et la beauté de l'harmonie.",
        "Éviter de relativiser au point de ne plus avoir de valeurs ou de chercher l'équilibre parfait qui n'existe pas. Le défi est de trouver ta vérité dans la tension des opposés.",
        "L'éducation supérieure peut être liée au droit, à la diplomatie, à l'art. Les voyages t'amènent vers des cultures qui valorisent l'harmonie. Tu enseignes l'équilibre.",
        "Étudie un concept qui unit deux perspectives apparemment opposées.",
        "Respire en visualisant l'harmonie qui sous-tend toutes les apparentes contradictions.",
        "Quelle sagesse de l'équilibre ai-je à partager ? »"),

    ('libra', 10): make_pluto_interp('libra', 10,
        "Tu transformes ta vie par une carrière dans les relations, la justice ou la beauté.",
        "Pluton en Balance dans ta maison X te destine à une réputation liée aux partenariats ou à la justice. Ta carrière implique souvent des négociations de pouvoir élégantes.",
        "Éviter de sacrifier ton ambition pour maintenir l'harmonie ou de manipuler par le charme. Le défi est de construire une carrière authentique, pas seulement diplomatique.",
        "Ta carrière passe par des phases de partenariat et de transformation relationnelle. Tu peux exceller dans le droit, les arts, les relations publiques, la diplomatie.",
        "Identifie un partenariat professionnel qui peut te faire grandir.",
        "Respire en visualisant une carrière qui unit beauté, justice et pouvoir.",
        "Comment ma carrière peut-elle mieux servir la justice et l'harmonie ? »"),

    ('libra', 11): make_pluto_interp('libra', 11,
        "Tu transformes ta vie par des amitiés équilibrées et des projets de justice sociale.",
        "Pluton en Balance dans ta maison XI t'amène des amis avec qui tu créés des relations équilibrées. Tes projets collectifs visent la justice, l'équité, l'harmonie sociale.",
        "Éviter de perdre ton identité dans les groupes ou de manipuler pour maintenir l'harmonie. Le défi est de contribuer aux projets collectifs avec authenticité.",
        "Tes réseaux sont composés de personnes élégantes, diplomatiques, orientées vers la justice. Les projets collectifs peuvent concerner le droit, l'art, les relations internationales.",
        "Contribue à une cause de justice ou d'équité qui te tient à cœur.",
        "Respire en visualisant un monde plus équitable grâce à ton action.",
        "Comment puis-je contribuer à plus de justice et d'équilibre dans le monde ? »"),

    ('libra', 12): make_pluto_interp('libra', 12,
        "Tu transformes ta vie par une guérison de la dépendance relationnelle.",
        "Pluton en Balance dans ta maison XII te confronte à l'ombre de ton besoin des autres — codépendance, peur de la solitude, sacrifice de soi pour l'harmonie. Ton travail est l'autonomie intérieure.",
        "Éviter de te perdre dans des relations imaginaires ou de fuir la solitude. Le défi est de trouver l'harmonie en toi-même, pas seulement dans les relations.",
        "L'inconscient porte des patterns relationnels à identifier et à guérir. Les retraites en couple ou de travail relationnel sont transformatrices. L'équilibre intérieur précède l'équilibre extérieur.",
        "Passe un moment seul(e) et trouve la paix dans ta propre compagnie.",
        "Respire en visualisant un équilibre parfait entre solitude et relation.",
        "Quel besoin relationnel cache une blessure que je peux guérir seul(e) ? »"),

    # === SCORPIO (M1-M12) ===
    ('scorpio', 1): make_pluto_interp('scorpio', 1,
        "Tu transformes ta vie par une intensité magnétique et une présence qui ne laisse personne indifférent.",
        "Pluton en Scorpion dans ta maison I (double domicile) te donne une puissance de transformation exceptionnelle. Tu incarnes le mystère et la régénération. Ton regard pénètre les âmes.",
        "Apprendre à gérer ton intensité sans effrayer ou dominer. Ta présence peut être perçue comme menaçante — le travail est de la rendre guérissante plutôt que destructrice.",
        "Ton apparence dégage un magnétisme hypnotique. Les transformations personnelles sont radicales, profondes, définitives. Tu renais plusieurs fois au cours de ta vie.",
        "Regarde-toi dans un miroir et accepte la puissance que tu vois dans tes yeux.",
        "Respire profondément en accueillant toute l'intensité de ton être.",
        "Quelle transformation radicale suis-je prêt(e) à incarner ? »"),

    ('scorpio', 2): make_pluto_interp('scorpio', 2,
        "Tu transformes ta vie par un rapport obsessionnel puis libéré aux ressources matérielles.",
        "Pluton en Scorpion dans ta maison II intensifie ton rapport à l'argent et aux possessions. Tu as un don pour transformer les ressources et les faire fructifier de façon presque magique.",
        "Éviter l'obsession du contrôle financier ou la manipulation par l'argent. Ton défi est de transformer ton rapport à la sécurité pour qu'il ne soit plus basé sur la peur.",
        "Tes finances passent par des cycles de crise et de renaissance. Tu peux perdre beaucoup et reconstruire encore plus. L'argent a une dimension presque érotique dans ta vie.",
        "Fais un don à quelqu'un ou à une cause — laisse l'énergie circuler.",
        "Respire en visualisant l'abondance qui circule librement, sans attachement.",
        "Quel attachement financier suis-je prêt(e) à libérer ? »"),

    ('scorpio', 3): make_pluto_interp('scorpio', 3,
        "Tu transformes ta vie par une parole qui perce les secrets et révèle la vérité.",
        "Pluton en Scorpion dans ta maison III fait de ta communication une force de révélation. Tu vois ce qui est caché et tu as le pouvoir de le nommer.",
        "Éviter d'utiliser cette puissance pour blesser ou manipuler. Le défi est de révéler la vérité de façon qui guérit plutôt que qui détruit.",
        "Les relations avec frères, sœurs ou voisins sont intenses et transformatrices. L'apprentissage te passionne quand il touche les tabous. Tu excelles dans l'investigation, la psychologie.",
        "Écris une vérité que tu n'as jamais osé formuler, même pour toi.",
        "Respire en sentant le pouvoir de tes mots qui révèlent la lumière dans l'ombre.",
        "Quelle vérité cachée ai-je le courage de nommer ? »"),

    ('scorpio', 4): make_pluto_interp('scorpio', 4,
        "Tu transformes ta vie par une plongée dans les profondeurs de ton histoire familiale.",
        "Pluton en Scorpion dans ta maison IV enracine des transformations générationnelles profondes. Ta famille porte des secrets, des traumas, des pouvoirs à transmuter.",
        "Éviter de reproduire les patterns toxiques ou de rester prisonnier des drames familiaux. Le défi est de transformer l'héritage karmique pour les générations futures.",
        "Ton foyer est un espace intense, parfois sombre, toujours transformateur. La relation au parent Scorpion ou aux secrets familiaux est centrale. Les mémoires ancestrales refont surface.",
        "Honore tes ancêtres en allumant une bougie et en leur parlant en silence.",
        "Respire en visualisant les ombres familiales qui se transforment en lumière.",
        "Quel secret familial suis-je appelé(e) à transformer et libérer ? »"),

    ('scorpio', 5): make_pluto_interp('scorpio', 5,
        "Tu transformes ta vie par une créativité cathartique et des amours volcaniques.",
        "Pluton en Scorpion dans ta maison V fait de ta créativité une force de guérison profonde. Tes œuvres touchent les tabous et transforment ceux qui les contemplent. L'amour est fusion totale.",
        "Éviter les amours destructrices ou la créativité qui ne sert qu'à choquer. Le défi est de canaliser cette puissance en œuvres qui guérissent plutôt qu'elles ne traumatisent.",
        "Les romances sont des voyages au centre de la terre — intenses, transformatrices, parfois douloureuses. La relation aux enfants implique des enjeux de pouvoir à conscientiser. La création est une renaissance.",
        "Crée quelque chose qui exprime une émotion que tu n'oses montrer à personne.",
        "Respire en laissant ta créativité se nourrir de tes profondeurs les plus intimes.",
        "Quelle œuvre cathartique demande à naître de mes ombres ? »"),

    ('scorpio', 6): make_pluto_interp('scorpio', 6,
        "Tu transformes ta vie par un travail de régénération et une santé à surveiller.",
        "Pluton en Scorpion dans ta maison VI fait de ton travail quotidien un terrain de transformation intense. Ta santé reflète tes processus psychologiques profonds.",
        "Éviter de t'obsessionner sur la maladie ou de travailler jusqu'à l'épuisement. Le défi est de maintenir un équilibre entre intensité et récupération.",
        "Ton travail peut impliquer la guérison, la crise, la transformation des autres. Les organes reproducteurs et le système éliminatoire demandent attention. Les périodes de détox sont puissantes.",
        "Fais un acte de purification simple — douche consciente, respiration, jeûne léger.",
        "Respire en visualisant chaque cellule de ton corps se régénérer profondément.",
        "Quelle toxine physique ou émotionnelle suis-je prêt(e) à éliminer ? »"),

    ('scorpio', 7): make_pluto_interp('scorpio', 7,
        "Tu transformes ta vie par des partenariats intenses qui te mettent face à ton ombre.",
        "Pluton en Scorpion dans ta maison VII attire des partenaires magnétiques et transformateurs. Le couple est un creuset alchimique où tu te révèles et te transformes.",
        "Éviter les jeux de pouvoir destructeurs ou la projection de ton ombre sur le partenaire. Le défi est de créer des relations où la transformation est consciente et mutuellement désirée.",
        "Tes associations passent par des crises qui les renforcent ou les détruisent. Le partenaire est ton miroir sombre et lumineux. Les ruptures sont des morts symboliques puissantes.",
        "Identifie ce que tu reproches le plus à un partenaire — et regarde si c'est en toi.",
        "Respire en accueillant la vérité que tes relations te montrent sur toi-même.",
        "Quelle part de mon ombre mes relations me révèlent-elles ? »"),

    ('scorpio', 8): make_pluto_interp('scorpio', 8,
        "Tu transformes ta vie par une maîtrise des mystères de la mort, du sexe et de la renaissance.",
        "Pluton en Scorpion dans ta maison VIII (triple domicile) te donne un pouvoir de transformation extraordinaire. Tu es un initié naturel aux mystères les plus profonds de l'existence.",
        "Éviter de te perdre dans les ténèbres ou d'abuser de ton pouvoir sur les processus de vie et de mort. Le défi est d'utiliser cette puissance pour guérir et accompagner.",
        "La sexualité est tantrique, transformatrice, parfois compulsive. Les héritages portent des charges karmiques intenses. Tu as un don pour accompagner les mourants ou les personnes en crise.",
        "Médite sur ce que tu laisserais derrière toi si tu mourais demain.",
        "Respire en accueillant la mort comme ta plus grande alliée de transformation.",
        "Quel pouvoir de transformation suis-je appelé(e) à maîtriser et à servir ? »"),

    ('scorpio', 9): make_pluto_interp('scorpio', 9,
        "Tu transformes ta vie par une quête spirituelle intense et des voyages initiatiques.",
        "Pluton en Scorpion dans ta maison IX fait de ta spiritualité une voie de transformation radicale. Tu es attiré par les mystères, l'occulte, les traditions initiatiques.",
        "Éviter le fanatisme ou l'obsession des connaissances secrètes. Le défi est de trouver une sagesse qui intègre l'ombre plutôt que de s'y perdre.",
        "L'éducation supérieure te transforme profondément. Les voyages vers des lieux de pouvoir ou des sites anciens sont initiatiques. Tu peux devenir un maître spirituel puissant.",
        "Étudie un texte ou une tradition qui parle de mort et renaissance spirituelle.",
        "Respire en visualisant les portes de la connaissance secrète qui s'ouvrent devant toi.",
        "Quelle initiation spirituelle suis-je en train de traverser ? »"),

    ('scorpio', 10): make_pluto_interp('scorpio', 10,
        "Tu transformes ta vie par une carrière de pouvoir et de transformation sociale.",
        "Pluton en Scorpion dans ta maison X te destine à une position d'influence profonde. Ta réputation est liée à ton pouvoir de transformation et ta capacité à gérer les crises.",
        "Éviter l'abus de pouvoir ou la manipulation politique. Le défi est d'utiliser ton influence pour transformer les structures de façon éthique.",
        "Ta carrière passe par des morts et renaissances professionnelles. Tu peux exceller dans la psychologie, la finance, la politique, la gestion de crise. Le pouvoir vient naturellement.",
        "Visualise le changement que tu veux créer dans le monde par ton travail.",
        "Respire en ressentant le poids et la responsabilité de ton pouvoir d'influence.",
        "Quel pouvoir de transformation ai-je sur mon domaine professionnel ? »"),

    ('scorpio', 11): make_pluto_interp('scorpio', 11,
        "Tu transformes ta vie par des amitiés profondes et des mouvements de transformation sociale.",
        "Pluton en Scorpion dans ta maison XI t'amène des amis intenses et transformateurs. Tes projets collectifs visent des changements radicaux dans la société.",
        "Éviter les cercles toxiques ou les mouvements qui utilisent le groupe pour le pouvoir personnel. Le défi est de catalyser le changement collectif de façon éthique.",
        "Tes réseaux sont composés de personnes qui n'ont pas peur des profondeurs. Les projets collectifs peuvent concerner la psychologie, la mort/renaissance, la transformation sociale.",
        "Connecte-toi à un ami pour un échange authentique sur vos ombres respectives.",
        "Respire en visualisant un mouvement de transformation qui part de ton cercle.",
        "Comment mes connexions peuvent-elles catalyser une transformation plus large ? »"),

    ('scorpio', 12): make_pluto_interp('scorpio', 12,
        "Tu transformes ta vie par une plongée consciente dans les profondeurs de l'inconscient.",
        "Pluton en Scorpion dans ta maison XII te donne accès aux strates les plus profondes de la psyché. Tu portes la mémoire des ombres collectives et tu peux les transmuter.",
        "Éviter de te perdre dans les abysses ou de devenir obsédé par les forces obscures. Le défi est de descendre dans les profondeurs et d'en revenir avec des perles de sagesse.",
        "L'inconscient est ton royaume — rêves intenses, visions, intuitions psychiques. Les retraites en isolement ou le travail avec les mourants sont transformateurs. Tu guéris l'ombre collective.",
        "Avant de dormir, demande à ton inconscient de te révéler un secret.",
        "Respire en accueillant les profondeurs inconnues de ton être comme un territoire sacré.",
        "Quelle ombre inconsciente est prête à être transmutée en lumière ? »"),
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
