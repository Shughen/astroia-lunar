#!/usr/bin/env python3
"""Insert Lilith interpretations for Sagittarius, Capricorn, Aquarius, Pisces (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_lilith_interp(sign_name, house, phrase, ombre, pouvoir, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'sagittarius': '⚸ Lilith en Sagittaire',
        'capricorn': '⚸ Lilith en Capricorne',
        'aquarius': '⚸ Lilith en Verseau',
        'pisces': '⚸ Lilith en Poissons',
    }
    sign_fr = {
        'sagittarius': 'Sagittaire',
        'capricorn': 'Capricorne',
        'aquarius': 'Verseau',
        'pisces': 'Poissons',
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
    # === SAGITTARIUS (M1-M12) ===
    ('sagittarius', 1): make_lilith_interp('sagittarius', 1,
        "Ton ombre se loge dans la liberté excessive et le fanatisme — ton pouvoir est celui de l'explorateur sauvage.",
        "Lilith en Sagittaire dans ta maison I place ton ombre dans ton identité et ton besoin de liberté. Tu peux avoir un fanatisme refoulé ou une fuite dans l'aventure.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'expansion et de vision. Tu es un explorateur des frontières inconnues.",
        "En maison I, cette énergie est très visible dans ton besoin de liberté. Tu peux osciller entre fuite et prosélytisme. Trouve ta vérité sans l'imposer.",
        "Explore quelque chose de nouveau sans fuir le présent.",
        "Respire en sentant ta liberté intérieure.",
        "Quel besoin excessif de liberté ou fanatisme ai-je refoulé ? »"),

    ('sagittarius', 2): make_lilith_interp('sagittarius', 2,
        "Ton ombre se loge dans l'insouciance financière — ton pouvoir est celui de l'abondance philosophique.",
        "Lilith en Sagittaire dans ta maison II place ton ombre dans ta relation aux ressources. Tu peux avoir de l'insouciance financière ou croire que l'argent est « non-spirituel ».",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer de la richesse par ta vision et ta sagesse. Tes idées ont de la valeur.",
        "En maison II, cette énergie peut créer des hauts et des bas financiers. Apprends que l'abondance et la spiritualité ne sont pas incompatibles.",
        "Valorise tes idées et ta vision comme des ressources.",
        "Respire en accueillant l'abondance spirituelle et matérielle.",
        "Quel conflit ai-je entre argent et spiritualité ? »"),

    ('sagittarius', 3): make_lilith_interp('sagittarius', 3,
        "Ton ombre se loge dans le prêche et l'exagération — ton pouvoir est celui de la parole inspirante.",
        "Lilith en Sagittaire dans ta maison III place ton ombre dans ta communication. Tu peux avoir une tendance à prêcher, exagérer ou imposer tes vérités.",
        "En intégrant cette Lilith, tu accèdes à une parole visionnaire et inspirante. Tu peux élever les autres par tes mots.",
        "En maison III, cette énergie peut créer des communications intenses ou dogmatiques. Apprends à inspirer sans imposer.",
        "Partage une vision inspirante sans la prêcher.",
        "Respire en transmettant ta flamme sans brûler.",
        "Où mon enthousiasme devient-il du prosélytisme ? »"),

    ('sagittarius', 4): make_lilith_interp('sagittarius', 4,
        "Ton ombre se loge dans la fuite du foyer — ton pouvoir est celui des racines cosmopolites.",
        "Lilith en Sagittaire dans ta maison IV place ton ombre dans ta relation au foyer. Tu peux fuir les responsabilités familiales ou chercher ta maison partout sauf chez toi.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer un foyer qui est partout. Tu trouves des racines dans l'expansion.",
        "En maison IV, cette énergie peut créer un déracinement ou une famille éclatée. Apprends à être chez toi partout.",
        "Crée un espace sacré dans ton foyer actuel.",
        "Respire en te sentant chez toi, où que tu sois.",
        "Quelle fuite du foyer ou des racines ai-je dans l'ombre ? »"),

    ('sagittarius', 5): make_lilith_interp('sagittarius', 5,
        "Ton ombre se loge dans les amours aventurières — ton pouvoir est celui de la passion libre.",
        "Lilith en Sagittaire dans ta maison V place ton ombre dans tes amours et ta créativité. Tu peux fuir l'engagement amoureux ou chercher l'aventure plutôt que la profondeur.",
        "En intégrant cette Lilith, tu accèdes à une créativité et un amour expansifs. Tu aimes et crées avec une flamme aventurière.",
        "En maison V, cette énergie peut créer des amours multiples ou une créativité dispersée. Apprends à approfondir sans perdre la flamme.",
        "Aime ou crée avec passion ET engagement.",
        "Respire en unissant liberté et profondeur.",
        "Comment ma soif d'aventure a-t-elle affecté mes amours ou ma créativité ? »"),

    ('sagittarius', 6): make_lilith_interp('sagittarius', 6,
        "Ton ombre se loge dans la fuite du quotidien — ton pouvoir est celui du travail inspiré.",
        "Lilith en Sagittaire dans ta maison VI place ton ombre dans ton rapport au travail. Tu peux fuir les tâches répétitives ou chercher un travail qui soit une « mission ».",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer le travail en aventure. Tu trouves du sens dans le quotidien.",
        "En maison VI, cette énergie peut créer de l'instabilité professionnelle. Apprends que même les tâches ordinaires peuvent être sacrées.",
        "Trouve du sens et de l'aventure dans une tâche quotidienne.",
        "Respire en trouvant l'extraordinaire dans l'ordinaire.",
        "Quelle fuite du quotidien ou des responsabilités ai-je dans l'ombre ? »"),

    ('sagittarius', 7): make_lilith_interp('sagittarius', 7,
        "Ton ombre se loge dans la liberté en relation — ton pouvoir est celui des partenariats d'expansion.",
        "Lilith en Sagittaire dans ta maison VII place ton ombre dans tes relations. Tu peux fuir l'engagement ou chercher des partenaires qui ne te limitent pas.",
        "En intégrant cette Lilith, tu accèdes à des relations qui élèvent et expandent. Tu crées des partenariats de croissance mutuelle.",
        "En maison VII, cette énergie peut créer des relations instables ou un refus de s'engager. Apprends que l'engagement peut être une expansion.",
        "Engage-toi dans une relation comme dans une aventure partagée.",
        "Respire en sentant que l'amour peut être liberté.",
        "Comment mon besoin de liberté a-t-il affecté mes relations ? »"),

    ('sagittarius', 8): make_lilith_interp('sagittarius', 8,
        "Ton ombre se loge dans la fuite de l'intensité — ton pouvoir est celui de la transformation par la foi.",
        "Lilith en Sagittaire dans ta maison VIII place ton ombre dans ta relation aux crises et à l'intensité. Tu peux fuir les profondeurs en te réfugiant dans la philosophie.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer par la foi et la vision. Tu traverses les crises avec optimisme.",
        "En maison VIII, cette énergie peut créer une fuite spirituelle face aux émotions profondes. Apprends à descendre avant de monter.",
        "Traverse une intensité émotionnelle sans la fuir.",
        "Respire en descendant dans les profondeurs avec foi.",
        "Quelle intensité ai-je fuie en me réfugiant dans la philosophie ? »"),

    ('sagittarius', 9): make_lilith_interp('sagittarius', 9,
        "Ton ombre se loge dans le fanatisme ou le nihilisme — ton pouvoir est celui de la quête de vérité.",
        "Lilith en Sagittaire dans ta maison IX (son domicile) place ton ombre dans tes croyances. Tu peux osciller entre fanatisme et perte totale de foi.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir exceptionnel de quête de vérité. Tu peux trouver et enseigner des vérités profondes.",
        "En maison IX, cette énergie est particulièrement puissante. Tu es destiné à être un chercheur et un passeur de sagesse.",
        "Explore une vérité avec passion mais sans fanatisme.",
        "Respire en embrassant ta quête de sens.",
        "Quel fanatisme ou nihilisme ai-je dans ma relation à la vérité ? »"),

    ('sagittarius', 10): make_lilith_interp('sagittarius', 10,
        "Ton ombre se loge dans l'ambition de liberté — ton pouvoir est celui du leader visionnaire.",
        "Lilith en Sagittaire dans ta maison X place ton ombre dans ta carrière. Tu peux fuir les structures ou avoir une ambition d'être un « gourou ».",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de leadership visionnaire. Tu guides les autres vers de nouveaux horizons.",
        "En maison X, cette énergie peut créer une carrière instable ou un rejet de l'autorité. Apprends à structurer ta vision.",
        "Construis quelque chose de durable à partir de ta vision.",
        "Respire en assumant ton rôle de guide.",
        "Quelle fuite ou ambition démesurée ai-je dans ma carrière ? »"),

    ('sagittarius', 11): make_lilith_interp('sagittarius', 11,
        "Ton ombre se loge dans l'idéalisme excessif — ton pouvoir est celui d'inspirer les collectifs.",
        "Lilith en Sagittaire dans ta maison XI place ton ombre dans tes groupes et tes idéaux. Tu peux avoir un idéalisme déconnecté ou rejeter les groupes qui ne partagent pas ta vision.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'inspirer et de mobiliser les groupes vers de grands idéaux.",
        "En maison XI, cette énergie peut créer des conflits idéologiques dans les groupes. Apprends à rassembler au-delà des différences.",
        "Inspire un groupe avec ta vision sans l'imposer.",
        "Respire en partageant tes idéaux avec le collectif.",
        "Quel idéalisme excessif ou rejet ai-je dans mes relations de groupe ? »"),

    ('sagittarius', 12): make_lilith_interp('sagittarius', 12,
        "Ton ombre se loge dans la fuite spirituelle — ton pouvoir est celui de la connexion cosmique.",
        "Lilith en Sagittaire dans ta maison XII place ton ombre dans l'inconscient et la spiritualité. Tu peux fuir la réalité dans la quête spirituelle ou avoir des croyances karmiques à guérir.",
        "En intégrant cette Lilith, tu accèdes à une connexion cosmique directe. Tu peux canaliser des vérités universelles.",
        "En maison XII, cette énergie peut créer une fuite dans l'ailleurs ou des crises de foi. Apprends à être spirituel ET présent.",
        "Médite en restant ancré dans ton corps.",
        "Respire en connectant ciel et terre.",
        "Quelle fuite spirituelle ou croyance karmique porte mon âme ? »"),

    # === CAPRICORN (M1-M12) ===
    ('capricorn', 1): make_lilith_interp('capricorn', 1,
        "Ton ombre se loge dans le contrôle et la froideur — ton pouvoir est celui de l'autorité intègre.",
        "Lilith en Capricorne dans ta maison I place ton ombre dans ton identité et ton rapport à l'autorité. Tu peux avoir refoulé une froideur ou un besoin de contrôle excessif.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'autorité naturelle et d'intégrité. Tu es un pilier de force.",
        "En maison I, cette énergie est visible dans ta présence austère ou contrôlée. Apprends à mélanger autorité et chaleur.",
        "Assume ton autorité avec humanité.",
        "Respire en sentant ta force sans rigidité.",
        "Quelle froideur ou besoin de contrôle ai-je refoulé ? »"),

    ('capricorn', 2): make_lilith_interp('capricorn', 2,
        "Ton ombre se loge dans l'avarice ou la peur du manque — ton pouvoir est celui de la construction de richesse.",
        "Lilith en Capricorne dans ta maison II place ton ombre dans ta relation à l'argent. Tu peux avoir une avarice refoulée ou une peur intense de la pauvreté.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de construire une richesse durable. Tu bâtis avec patience et stratégie.",
        "En maison II, cette énergie peut créer une relation obsessionnelle à la sécurité financière. Apprends que la vraie sécurité est intérieure.",
        "Construis ta sécurité financière avec sagesse.",
        "Respire en relâchant la peur du manque.",
        "Quelle avarice ou peur de pauvreté ai-je dans l'ombre ? »"),

    ('capricorn', 3): make_lilith_interp('capricorn', 3,
        "Ton ombre se loge dans la parole d'autorité — ton pouvoir est celui de la communication structurée.",
        "Lilith en Capricorne dans ta maison III place ton ombre dans ta communication. Tu peux avoir une parole trop autoritaire ou un blocage dans l'expression.",
        "En intégrant cette Lilith, tu accèdes à une parole qui a du poids et de l'autorité. Tes mots construisent.",
        "En maison III, cette énergie peut créer des communications froides ou contrôlantes. Apprends à communiquer avec autorité ET chaleur.",
        "Communique avec autorité et bienveillance.",
        "Respire en donnant du poids à tes paroles.",
        "Comment ma communication est-elle trop contrôlante ou froide ? »"),

    ('capricorn', 4): make_lilith_interp('capricorn', 4,
        "Ton ombre se loge dans l'autorité familiale — ton pouvoir est celui de structurer le foyer.",
        "Lilith en Capricorne dans ta maison IV place ton ombre dans ta famille et ton foyer. Tu peux avoir vécu un père autoritaire ou porter trop de responsabilités familiales.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer un foyer structuré et sécurisant. Tu es le pilier de ta famille.",
        "En maison IV, cette énergie peut créer un foyer trop rigide ou un héritage d'autorité. Transforme la rigidité en structure aimante.",
        "Crée de la structure et de la chaleur dans ton foyer.",
        "Respire en étant le pilier aimant de ta famille.",
        "Quelle autorité excessive ou responsabilité familiale ai-je dans l'ombre ? »"),

    ('capricorn', 5): make_lilith_interp('capricorn', 5,
        "Ton ombre se loge dans le refus du plaisir — ton pouvoir est celui de la création disciplinée.",
        "Lilith en Capricorne dans ta maison V place ton ombre dans ta créativité et tes amours. Tu peux refuser le plaisir ou prendre l'amour trop au sérieux.",
        "En intégrant cette Lilith, tu accèdes à une créativité disciplinée et à un amour mature. Tu crées des œuvres qui durent.",
        "En maison V, cette énergie peut bloquer la joie ou la spontanéité. Apprends que le plaisir peut être responsable.",
        "Crée ou aime avec joie ET structure.",
        "Respire en autorisant le plaisir dans ta discipline.",
        "Comment mon sérieux a-t-il bloqué ma joie ou mes amours ? »"),

    ('capricorn', 6): make_lilith_interp('capricorn', 6,
        "Ton ombre se loge dans le surmenage — ton pouvoir est celui du travail efficace.",
        "Lilith en Capricorne dans ta maison VI place ton ombre dans ton rapport au travail. Tu peux te surmener ou avoir une relation obsessionnelle au devoir.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de travail efficace et endurant. Tu accomplies des choses durables.",
        "En maison VI, cette énergie peut créer de l'épuisement ou des problèmes de santé liés au stress. Apprends l'efficacité sans sacrifice.",
        "Travaille de façon efficace sans t'épuiser.",
        "Respire en relâchant la pression du devoir.",
        "Où me suis-je épuisé par sens du devoir ? »"),

    ('capricorn', 7): make_lilith_interp('capricorn', 7,
        "Ton ombre se loge dans les relations de pouvoir — ton pouvoir est celui du partenariat structuré.",
        "Lilith en Capricorne dans ta maison VII place ton ombre dans tes relations. Tu peux avoir des relations de pouvoir ou chercher un partenaire pour le statut.",
        "En intégrant cette Lilith, tu accèdes à des relations solides et durables. Tu crées des partenariats qui construisent.",
        "En maison VII, cette énergie peut créer des relations trop sérieuses ou basées sur le pouvoir. Apprends l'amour qui élève les deux.",
        "Crée un partenariat d'égaux qui construit.",
        "Respire en sentant l'amour au-delà du pouvoir.",
        "Quels jeux de pouvoir ou calculs ai-je dans mes relations ? »"),

    ('capricorn', 8): make_lilith_interp('capricorn', 8,
        "Ton ombre se loge dans le contrôle face à la mort — ton pouvoir est celui de la transformation structurée.",
        "Lilith en Capricorne dans ta maison VIII place ton ombre dans ta relation aux crises et au contrôle. Tu peux essayer de tout contrôler, même l'incontrôlable.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer avec stratégie. Tu traverses les crises avec force et structure.",
        "En maison VIII, cette énergie peut créer une peur de perdre le contrôle. Apprends que la transformation demande parfois l'abandon.",
        "Lâche le contrôle face à une transformation.",
        "Respire en acceptant ce qui ne peut être contrôlé.",
        "Où mon besoin de contrôle m'empêche-t-il de me transformer ? »"),

    ('capricorn', 9): make_lilith_interp('capricorn', 9,
        "Ton ombre se loge dans le dogmatisme traditionnel — ton pouvoir est celui de la sagesse structurée.",
        "Lilith en Capricorne dans ta maison IX place ton ombre dans tes croyances. Tu peux être attaché aux traditions ou rejeter toute spiritualité non « prouvée ».",
        "En intégrant cette Lilith, tu accèdes à une sagesse ancrée et pratique. Tu incarnes ce que tu crois.",
        "En maison IX, cette énergie peut créer du conservatisme spirituel. Apprends que la vraie sagesse inclut le mystère.",
        "Explore au-delà des croyances traditionnelles.",
        "Respire en ouvrant ta vision au-delà des structures.",
        "Quel attachement aux traditions ou dogmatisme ai-je dans l'ombre ? »"),

    ('capricorn', 10): make_lilith_interp('capricorn', 10,
        "Ton ombre se loge dans l'obsession de carrière — ton pouvoir est celui du leadership intègre.",
        "Lilith en Capricorne dans ta maison X (son domicile) place ton ombre dans ta carrière et ton statut. Tu peux avoir une obsession du succès ou une relation toxique au pouvoir.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de leadership exceptionnel. Tu peux atteindre les sommets avec intégrité.",
        "En maison X, cette énergie est particulièrement puissante. Tu es destiné à l'autorité. Utilise-la avec sagesse.",
        "Assume ton pouvoir avec intégrité.",
        "Respire en sentant ta légitimité de leader.",
        "Quelle obsession de carrière ou de statut ai-je dans l'ombre ? »"),

    ('capricorn', 11): make_lilith_interp('capricorn', 11,
        "Ton ombre se loge dans le contrôle des groupes — ton pouvoir est celui de structurer les collectifs.",
        "Lilith en Capricorne dans ta maison XI place ton ombre dans tes groupes et tes amitiés. Tu peux vouloir contrôler les groupes ou les utiliser pour ton ascension.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de structurer et d'organiser les collectifs. Tu crées des organisations qui durent.",
        "En maison XI, cette énergie peut créer des amitiés utilitaires ou du contrôle dans les groupes. Apprends l'amitié désintéressée.",
        "Contribue à un groupe sans chercher à le contrôler.",
        "Respire en appartenant sans dominer.",
        "Comment mon besoin de contrôle affecte-t-il mes relations de groupe ? »"),

    ('capricorn', 12): make_lilith_interp('capricorn', 12,
        "Ton ombre se loge dans la rigidité karmique — ton pouvoir est celui de l'autorité spirituelle.",
        "Lilith en Capricorne dans ta maison XII place ton ombre dans l'inconscient et le karma. Tu peux porter une culpabilité ancienne liée au pouvoir ou à l'autorité.",
        "En intégrant cette Lilith, tu accèdes à une autorité spirituelle et à une sagesse de l'âme. Tu guides depuis les profondeurs.",
        "En maison XII, cette énergie peut créer des schémas karmiques d'autorité. Tu es destiné à transformer ta relation au pouvoir.",
        "Médite sur l'autorité intérieure avec humilité.",
        "Respire en libérant les culpabilités anciennes.",
        "Quelle culpabilité karmique liée au pouvoir porte mon âme ? »"),

    # === AQUARIUS (M1-M12) ===
    ('aquarius', 1): make_lilith_interp('aquarius', 1,
        "Ton ombre se loge dans la rébellion et l'aliénation — ton pouvoir est celui de l'originalité radicale.",
        "Lilith en Verseau dans ta maison I place ton ombre dans ton identité et ta différence. Tu peux te sentir aliéné ou rejeter délibérément les normes.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'originalité et d'innovation. Tu es un pionnier qui ouvre de nouvelles voies.",
        "En maison I, cette énergie est visible dans ta différence. Tu peux osciller entre marginalité et conformisme réactif. Assume ton unicité.",
        "Sois toi-même sans te rebeller contre.",
        "Respire en embrassant ton originalité.",
        "Quelle rébellion ou aliénation ai-je dans mon identité ? »"),

    ('aquarius', 2): make_lilith_interp('aquarius', 2,
        "Ton ombre se loge dans le rejet de la matière — ton pouvoir est celui de l'innovation financière.",
        "Lilith en Verseau dans ta maison II place ton ombre dans ta relation à l'argent. Tu peux rejeter les systèmes financiers conventionnels ou avoir une relation erratique aux ressources.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer de nouvelles formes de richesse. Tu innoves dans la création de valeur.",
        "En maison II, cette énergie peut créer de l'instabilité financière. Apprends à utiliser le système tout en le transformant.",
        "Crée de la valeur de façon innovante.",
        "Respire en réconciliant idéaux et réalité matérielle.",
        "Quel rejet du système financier ai-je dans l'ombre ? »"),

    ('aquarius', 3): make_lilith_interp('aquarius', 3,
        "Ton ombre se loge dans la pensée rebelle — ton pouvoir est celui de la communication révolutionnaire.",
        "Lilith en Verseau dans ta maison III place ton ombre dans ta communication. Tu peux avoir des idées trop avant-gardistes ou un rejet de la communication conventionnelle.",
        "En intégrant cette Lilith, tu accèdes à une parole qui révolutionne. Tes idées ouvrent de nouveaux horizons.",
        "En maison III, cette énergie peut créer de l'incompréhension ou de l'isolement intellectuel. Apprends à connecter avec ta différence.",
        "Partage une idée originale en la rendant accessible.",
        "Respire en honorant ta pensée unique.",
        "Quelles idées révolutionnaires ai-je refoulées par peur du rejet ? »"),

    ('aquarius', 4): make_lilith_interp('aquarius', 4,
        "Ton ombre se loge dans le rejet de la famille — ton pouvoir est celui de créer de nouvelles formes de foyer.",
        "Lilith en Verseau dans ta maison IV place ton ombre dans ta famille et ton foyer. Tu peux te sentir étranger dans ta famille ou rejeter les modèles familiaux.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer des formes de foyer innovantes. Tu redéfinis ce qu'est une famille.",
        "En maison IV, cette énergie peut créer un déracinement ou un rejet des traditions familiales. Apprends à créer ta propre tribu.",
        "Crée un foyer qui reflète tes valeurs uniques.",
        "Respire en te sentant appartenir à ta façon.",
        "Comment me suis-je senti étranger dans ma propre famille ? »"),

    ('aquarius', 5): make_lilith_interp('aquarius', 5,
        "Ton ombre se loge dans les amours non-conventionnelles — ton pouvoir est celui de la créativité révolutionnaire.",
        "Lilith en Verseau dans ta maison V place ton ombre dans tes amours et ta créativité. Tu peux avoir des amours non-conventionnelles ou une créativité trop avant-gardiste.",
        "En intégrant cette Lilith, tu accèdes à une créativité qui innove et des amours qui libèrent. Tu crées et aimes en pionnier.",
        "En maison V, cette énergie peut créer des relations ou des créations trop détachées. Apprends à innover avec le cœur.",
        "Crée ou aime de façon originale ET engagée.",
        "Respire en unissant innovation et passion.",
        "Comment ma différence a-t-elle affecté mes amours ou ma créativité ? »"),

    ('aquarius', 6): make_lilith_interp('aquarius', 6,
        "Ton ombre se loge dans le rejet des routines — ton pouvoir est celui de l'innovation quotidienne.",
        "Lilith en Verseau dans ta maison VI place ton ombre dans ton rapport au travail. Tu peux rejeter les routines ou avoir du mal avec les environnements conventionnels.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer le quotidien. Tu innoves dans les méthodes de travail.",
        "En maison VI, cette énergie peut créer de l'instabilité professionnelle. Apprends à créer tes propres routines.",
        "Crée une routine qui te ressemble.",
        "Respire en trouvant ta liberté dans le quotidien.",
        "Quel rejet des routines ou du travail conventionnel ai-je dans l'ombre ? »"),

    ('aquarius', 7): make_lilith_interp('aquarius', 7,
        "Ton ombre se loge dans le détachement relationnel — ton pouvoir est celui des partenariats égalitaires.",
        "Lilith en Verseau dans ta maison VII place ton ombre dans tes relations. Tu peux avoir un détachement émotionnel ou refuser les relations conventionnelles.",
        "En intégrant cette Lilith, tu accèdes à des relations authentiquement égalitaires. Tu crées des partenariats de liberté mutuelle.",
        "En maison VII, cette énergie peut créer des relations trop distantes ou des fuites de l'engagement. Apprends l'engagement libre.",
        "Engage-toi dans une relation avec liberté et présence.",
        "Respire en aimant sans posséder ni fuir.",
        "Quel détachement ou fuite relationnelle ai-je dans l'ombre ? »"),

    ('aquarius', 8): make_lilith_interp('aquarius', 8,
        "Ton ombre se loge dans le détachement face à l'intensité — ton pouvoir est celui de la transformation collective.",
        "Lilith en Verseau dans ta maison VIII place ton ombre dans ta relation aux crises. Tu peux intellectualiser les émotions intenses ou fuir dans le détachement.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer les collectifs. Tu es un agent de changement pour les groupes.",
        "En maison VIII, cette énergie peut créer une déconnexion des émotions profondes. Apprends à être présent dans l'intensité.",
        "Reste présent dans une expérience intense.",
        "Respire en accueillant l'émotion sans la fuir.",
        "Quelle intensité ai-je fuie dans le détachement ? »"),

    ('aquarius', 9): make_lilith_interp('aquarius', 9,
        "Ton ombre se loge dans les croyances rebelles — ton pouvoir est celui de la pensée visionnaire.",
        "Lilith en Verseau dans ta maison IX place ton ombre dans tes croyances. Tu peux rejeter automatiquement les traditions ou avoir des croyances trop excentriques.",
        "En intégrant cette Lilith, tu accèdes à une vision du futur exceptionnelle. Tu peux voir ce qui n'existe pas encore.",
        "En maison IX, cette énergie peut créer un rejet systématique de toute sagesse ancienne. Apprends à intégrer passé et futur.",
        "Explore la sagesse ancienne avec un regard nouveau.",
        "Respire en honorant la tradition ET l'innovation.",
        "Quel rejet automatique des traditions ai-je dans l'ombre ? »"),

    ('aquarius', 10): make_lilith_interp('aquarius', 10,
        "Ton ombre se loge dans le rejet de l'autorité — ton pouvoir est celui du leadership innovant.",
        "Lilith en Verseau dans ta maison X place ton ombre dans ta carrière et ton rapport à l'autorité. Tu peux rejeter les structures ou avoir du mal à trouver ta place dans le système.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de leadership qui change les paradigmes. Tu crées de nouvelles structures.",
        "En maison X, cette énergie peut créer une carrière marginale ou un conflit avec l'autorité. Apprends à transformer le système de l'intérieur.",
        "Exerce ton influence pour changer les structures.",
        "Respire en assumant ton rôle de transformateur.",
        "Quel rejet de l'autorité ou du système ai-je dans ma carrière ? »"),

    ('aquarius', 11): make_lilith_interp('aquarius', 11,
        "Ton ombre se loge dans l'aliénation sociale — ton pouvoir est celui de créer des communautés nouvelles.",
        "Lilith en Verseau dans ta maison XI (son domicile) place ton ombre dans les groupes et l'appartenance. Tu peux te sentir trop différent pour appartenir ou rejeter les groupes.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir exceptionnel de créer des communautés innovantes. Tu rassembles les marginaux.",
        "En maison XI, cette énergie est particulièrement puissante. Tu es destiné à créer de nouvelles formes de collectif.",
        "Crée ou rejoins un groupe qui célèbre la différence.",
        "Respire en appartenant tout en restant unique.",
        "Quelle aliénation ou rejet des groupes ai-je dans l'ombre ? »"),

    ('aquarius', 12): make_lilith_interp('aquarius', 12,
        "Ton ombre se loge dans l'aliénation cosmique — ton pouvoir est celui de la connexion universelle.",
        "Lilith en Verseau dans ta maison XII place ton ombre dans l'inconscient et l'aliénation profonde. Tu peux te sentir étranger sur cette planète.",
        "En intégrant cette Lilith, tu accèdes à une connexion à la conscience universelle. Tu es un pont entre les dimensions.",
        "En maison XII, cette énergie porte une dimension transpersonnelle. Tu es peut-être une « vieille âme » venue d'ailleurs. Trouve ta place ici.",
        "Médite sur ta connexion à l'humanité.",
        "Respire en te sentant appartenir au cosmos.",
        "Quelle aliénation cosmique ou sentiment d'être étranger porte mon âme ? »"),

    # === PISCES (M1-M12) ===
    ('pisces', 1): make_lilith_interp('pisces', 1,
        "Ton ombre se loge dans la dissolution et la fuite — ton pouvoir est celui de la connexion mystique.",
        "Lilith en Poissons dans ta maison I place ton ombre dans ton identité et tes limites. Tu peux avoir des limites floues ou te dissoudre dans les autres.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de connexion mystique et de compassion universelle. Tu sens tout.",
        "En maison I, cette énergie peut créer une identité floue ou une fuite de soi. Apprends à être poreux ET défini.",
        "Définis qui tu es tout en restant ouvert.",
        "Respire en te sentant connecté mais distinct.",
        "Quelle dissolution ou fuite de mon identité ai-je dans l'ombre ? »"),

    ('pisces', 2): make_lilith_interp('pisces', 2,
        "Ton ombre se loge dans la négligence matérielle — ton pouvoir est celui de l'abondance spirituelle.",
        "Lilith en Poissons dans ta maison II place ton ombre dans ta relation à l'argent. Tu peux négliger le matériel ou avoir une relation floue aux finances.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer l'abondance par l'intuition et la foi. Tu attires sans effort.",
        "En maison II, cette énergie peut créer de l'instabilité financière. Apprends que le spirituel peut créer le matériel.",
        "Utilise ton intuition pour créer de l'abondance.",
        "Respire en accueillant l'abondance sans la fuir.",
        "Quelle négligence ou confusion ai-je autour de l'argent ? »"),

    ('pisces', 3): make_lilith_interp('pisces', 3,
        "Ton ombre se loge dans la communication floue — ton pouvoir est celui de la parole inspirée.",
        "Lilith en Poissons dans ta maison III place ton ombre dans ta communication. Tu peux avoir du mal à communiquer clairement ou te perdre dans les mots.",
        "En intégrant cette Lilith, tu accèdes à une parole poétique et inspirée. Tu communiques par images et ressentis.",
        "En maison III, cette énergie peut créer de la confusion dans les échanges. Apprends à traduire ton intuition en mots clairs.",
        "Exprime une vision intuitive de façon accessible.",
        "Respire en connectant l'invisible aux mots.",
        "Quelle difficulté à communiquer clairement ai-je dans l'ombre ? »"),

    ('pisces', 4): make_lilith_interp('pisces', 4,
        "Ton ombre se loge dans les secrets et les sacrifices familiaux — ton pouvoir est celui de guérir la lignée.",
        "Lilith en Poissons dans ta maison IV place ton ombre dans ta famille et les secrets cachés. Tu peux avoir absorbé les émotions familiales ou porté des secrets.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de guérir l'inconscient familial. Tu es le médium de ta lignée.",
        "En maison IV, cette énergie peut créer de la confusion familiale ou du sacrifice. Apprends à distinguer ton vécu de celui de ta famille.",
        "Libère ce qui ne t'appartient pas dans ta famille.",
        "Respire en te distinguant de l'inconscient familial.",
        "Quels secrets ou sacrifices familiaux ai-je absorbés ? »"),

    ('pisces', 5): make_lilith_interp('pisces', 5,
        "Ton ombre se loge dans les amours idéalisées — ton pouvoir est celui de l'amour et la création sacrés.",
        "Lilith en Poissons dans ta maison V place ton ombre dans tes amours et ta créativité. Tu peux idéaliser tes amours ou créer dans la confusion.",
        "En intégrant cette Lilith, tu accèdes à une créativité inspirée et à un amour transcendant. Tu crées et aimes depuis l'âme.",
        "En maison V, cette énergie peut créer des désillusions amoureuses ou une créativité floue. Apprends à incarner l'idéal.",
        "Crée ou aime avec inspiration ET ancrage.",
        "Respire en touchant le sacré dans la création.",
        "Comment mes idéalisations ont-elles affecté mes amours ou ma créativité ? »"),

    ('pisces', 6): make_lilith_interp('pisces', 6,
        "Ton ombre se loge dans le sacrifice au service — ton pouvoir est celui de la guérison.",
        "Lilith en Poissons dans ta maison VI place ton ombre dans ton rapport au service et à la santé. Tu peux te sacrifier excessivement ou avoir des problèmes de santé inexpliqués.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de guérison exceptionnel. Tu sers avec compassion sans te perdre.",
        "En maison VI, cette énergie peut créer de l'épuisement ou des maladies psychosomatiques. Apprends le service avec limites.",
        "Sers avec compassion tout en te protégeant.",
        "Respire en prenant soin de toi aussi.",
        "Où me suis-je sacrifié au point de me rendre malade ? »"),

    ('pisces', 7): make_lilith_interp('pisces', 7,
        "Ton ombre se loge dans la fusion relationnelle — ton pouvoir est celui de l'amour inconditionnel.",
        "Lilith en Poissons dans ta maison VII place ton ombre dans tes relations. Tu peux te dissoudre dans l'autre ou vivre des relations de sauveur-victime.",
        "En intégrant cette Lilith, tu accèdes à un amour inconditionnel qui ne perd pas le soi. Tu aimes profondément en restant toi.",
        "En maison VII, cette énergie peut créer des relations fusionnelles ou de dépendance. Apprends l'amour avec des limites saines.",
        "Aime profondément sans te perdre.",
        "Respire en restant toi-même dans la fusion.",
        "Comment me suis-je perdu ou dissous dans mes relations ? »"),

    ('pisces', 8): make_lilith_interp('pisces', 8,
        "Ton ombre se loge dans la peur de la dissolution — ton pouvoir est celui de la transformation mystique.",
        "Lilith en Poissons dans ta maison VIII place ton ombre dans ta relation à la mort et à la dissolution. Tu peux avoir peur de perdre le contrôle total.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformation mystique. Tu peux mourir et renaître à volonté.",
        "En maison VIII, cette énergie peut créer des peurs profondes ou des expériences de mort mystique. Apprends à te dissoudre pour renaître.",
        "Abandonne-toi à une transformation sans contrôle.",
        "Respire en faisant confiance à la dissolution.",
        "Quelle peur de la dissolution totale ai-je dans l'ombre ? »"),

    ('pisces', 9): make_lilith_interp('pisces', 9,
        "Ton ombre se loge dans la confusion spirituelle — ton pouvoir est celui de la connexion directe au divin.",
        "Lilith en Poissons dans ta maison IX place ton ombre dans tes croyances et ta spiritualité. Tu peux être vulnérable aux illusions ou te perdre dans les croyances.",
        "En intégrant cette Lilith, tu accèdes à une connexion mystique directe. Tu n'as pas besoin d'intermédiaire pour le sacré.",
        "En maison IX, cette énergie peut créer de la naïveté spirituelle ou des crises de foi. Apprends le discernement mystique.",
        "Connecte-toi au divin avec foi ET discernement.",
        "Respire en sentant le sacré sans illusion.",
        "Quelle confusion ou naïveté spirituelle ai-je dans l'ombre ? »"),

    ('pisces', 10): make_lilith_interp('pisces', 10,
        "Ton ombre se loge dans le sacrifice de carrière — ton pouvoir est celui de la vocation sacrée.",
        "Lilith en Poissons dans ta maison X place ton ombre dans ta carrière et ta mission. Tu peux te sacrifier pour ta mission ou avoir une vocation floue.",
        "En intégrant cette Lilith, tu accèdes à une vocation qui sert le tout. Tu es appelé à guérir ou à inspirer publiquement.",
        "En maison X, cette énergie peut créer une carrière sacrificielle ou peu définie. Apprends à servir sans te perdre.",
        "Clarifie ta mission tout en restant ouvert.",
        "Respire en servant ta vocation sacrée.",
        "Comment ma carrière est-elle devenue un sacrifice ? »"),

    ('pisces', 11): make_lilith_interp('pisces', 11,
        "Ton ombre se loge dans la dissolution dans les groupes — ton pouvoir est celui de la compassion collective.",
        "Lilith en Poissons dans ta maison XI place ton ombre dans les groupes et l'humanité. Tu peux te perdre dans les causes ou absorber les souffrances collectives.",
        "En intégrant cette Lilith, tu accèdes à une compassion universelle qui n'est pas envahissante. Tu sers l'humanité avec sagesse.",
        "En maison XI, cette énergie peut créer de l'épuisement face aux maux du monde. Apprends la compassion avec protection.",
        "Sers l'humanité sans absorber sa souffrance.",
        "Respire en protégeant ta compassion.",
        "Comment me suis-je perdu ou épuisé dans les causes collectives ? »"),

    ('pisces', 12): make_lilith_interp('pisces', 12,
        "Ton ombre se loge dans l'océan de l'inconscient — ton pouvoir est celui de l'unité cosmique.",
        "Lilith en Poissons dans ta maison XII (son domicile) place ton ombre dans les profondeurs ultimes de l'inconscient. Tu es connecté à tout, ce qui peut être accablant.",
        "En intégrant cette Lilith, tu accèdes au pouvoir ultime de connexion au tout. Tu es un canal entre les mondes.",
        "En maison XII, cette énergie est à son maximum. Tu es destiné à être un mystique, un guérisseur des profondeurs invisibles.",
        "Médite en te connectant au tout avec protection.",
        "Respire en étant un avec l'univers.",
        "Quelle connexion totale m'a submergé ou effrayé ? »"),
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
