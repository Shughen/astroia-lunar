#!/usr/bin/env python3
"""Insert Chiron interpretations for Sagittarius, Capricorn, Aquarius, Pisces (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_chiron_interp(sign_name, house, phrase, blessure, guerison, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'sagittarius': '⚷ Chiron en Sagittaire',
        'capricorn': '⚷ Chiron en Capricorne',
        'aquarius': '⚷ Chiron en Verseau',
        'pisces': '⚷ Chiron en Poissons',
    }
    sign_fr = {
        'sagittarius': 'Sagittaire',
        'capricorn': 'Capricorne',
        'aquarius': 'Verseau',
        'pisces': 'Poissons',
    }
    return f"""# {sign_titles[sign_name]}

**En une phrase :** {phrase}

## Ta blessure originelle
{blessure}

## Ton don de guérison
{guerison}

## Maison {house} en {sign_fr[sign_name]}
{maison_desc}

## Micro-rituel du jour (2 min)
- {ritual_action}
- {ritual_breath}
- Journal : « {ritual_journal} »"""

CHIRON_INTERPRETATIONS = {
    # === SAGITTARIUS (M1-M12) ===
    ('sagittarius', 1): make_chiron_interp('sagittarius', 1,
        "Ta blessure touche ta foi et ton sens de la vie — tu deviens guérisseur de la quête de sens.",
        "Chiron en Sagittaire dans ta maison I révèle une blessure profonde autour de ta foi dans la vie et de ton sens de direction. Tu as pu perdre espoir ou te sentir perdu.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à retrouver leur foi et leur direction dans la vie.",
        "Cette position en maison I rend la blessure visible dans ton optimisme parfois forcé ou ton cynisme. Tu apprends que ta quête de sens inspire les autres.",
        "Reconnecte-toi à une source d'inspiration ou de foi.",
        "Respire en sentant que ta vie a un sens profond.",
        "Où ai-je perdu foi dans la vie ou en moi-même ? »"),

    ('sagittarius', 2): make_chiron_interp('sagittarius', 2,
        "Ta blessure touche la valeur de la sagesse — tu deviens guérisseur de l'abondance spirituelle.",
        "Chiron en Sagittaire dans ta maison II révèle une blessure autour de la valeur de tes connaissances et de ta sagesse. Tu as pu douter que ta vision puisse avoir de la valeur.",
        "En traversant cette blessure, tu développes un don pour aider les autres à reconnaître la valeur de leur sagesse et à en vivre.",
        "Cette position en maison II peut créer un conflit entre spiritualité et matérialité. Tu apprends que la sagesse crée l'abondance.",
        "Valorise ta sagesse comme une ressource précieuse.",
        "Respire en te sentant riche de ta vision.",
        "Comment ai-je dévalorisé ma sagesse ou ma vision ? »"),

    ('sagittarius', 3): make_chiron_interp('sagittarius', 3,
        "Ta blessure touche la transmission du savoir — tu deviens guérisseur de l'enseignement.",
        "Chiron en Sagittaire dans ta maison III révèle une blessure autour de l'expression de tes croyances et de ta capacité à enseigner. Tu as pu te sentir illégitime à partager ta vision.",
        "En traversant cette blessure, tu développes un don pour aider les autres à communiquer leur sagesse et à enseigner avec authenticité.",
        "Cette position en maison III peut avoir créé des blocages dans l'expression de tes opinions profondes. Tu apprends que ta voix d'enseignant compte.",
        "Partage une croyance ou une sagesse avec confiance.",
        "Respire en validant ta légitimité à enseigner.",
        "Où me suis-je senti illégitime à partager ma vision ? »"),

    ('sagittarius', 4): make_chiron_interp('sagittarius', 4,
        "Ta blessure touche les racines spirituelles — tu deviens guérisseur de la foi familiale.",
        "Chiron en Sagittaire dans ta maison IV révèle une blessure autour des croyances familiales et du sens au foyer. Tu as pu grandir sans direction spirituelle ou avec des dogmes blessants.",
        "En traversant cette blessure, tu développes un don pour aider les familles à trouver leur propre sagesse et leurs croyances authentiques.",
        "Cette position en maison IV peut avoir créé une crise de foi liée à la famille. Tu apprends à créer un foyer qui nourrit l'esprit.",
        "Crée un espace de sagesse et d'inspiration dans ton foyer.",
        "Respire en te sentant spirituellement chez toi.",
        "Quelle blessure spirituelle vient de ma famille ? »"),

    ('sagittarius', 5): make_chiron_interp('sagittarius', 5,
        "Ta blessure touche la joie de croire — tu deviens guérisseur de l'enthousiasme.",
        "Chiron en Sagittaire dans ta maison V révèle une blessure autour de la joie de vivre et de l'enthousiasme. Tu as pu perdre ta capacité à t'émerveiller ou à t'amuser.",
        "En traversant cette blessure, tu développes un don pour aider les autres à retrouver leur joie et leur émerveillement face à la vie.",
        "Cette position en maison V peut avoir été marquée par une perte d'innocence ou de foi dans la joie. Tu apprends que la joie est un acte de foi.",
        "Fais quelque chose de joyeux comme un acte de foi.",
        "Respire en laissant la joie renaître en toi.",
        "Quand ai-je perdu ma capacité à m'émerveiller ? »"),

    ('sagittarius', 6): make_chiron_interp('sagittarius', 6,
        "Ta blessure touche le sens au quotidien — tu deviens guérisseur du travail inspiré.",
        "Chiron en Sagittaire dans ta maison VI révèle une blessure autour du sens de ton travail quotidien. Tu as pu te sentir perdu dans un travail sans signification.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver du sens dans leur travail et leur quotidien.",
        "Cette position en maison VI peut créer une tension entre l'idéal et le pratique. Tu apprends à infuser de la sagesse dans les tâches ordinaires.",
        "Trouve du sens dans une tâche quotidienne ordinaire.",
        "Respire en sentant que chaque action peut être sacrée.",
        "Où mon travail manque-t-il de sens pour moi ? »"),

    ('sagittarius', 7): make_chiron_interp('sagittarius', 7,
        "Ta blessure touche la foi en l'autre — tu deviens guérisseur des partenariats inspirés.",
        "Chiron en Sagittaire dans ta maison VII révèle une blessure autour de la confiance dans les relations et des croyances partagées. Tu as pu être déçu par des partenaires qui ne partageaient pas ta vision.",
        "En traversant cette blessure, tu développes un don pour aider les couples à grandir ensemble spirituellement et à partager une vision.",
        "Cette position en maison VII peut créer des difficultés à trouver des partenaires avec qui partager ta quête. Tu apprends la foi dans l'autre.",
        "Partage une vision ou une croyance avec un partenaire.",
        "Respire en faisant confiance à la sagesse de l'autre.",
        "Comment mes attentes spirituelles ont-elles affecté mes relations ? »"),

    ('sagittarius', 8): make_chiron_interp('sagittarius', 8,
        "Ta blessure touche la foi dans les crises — tu deviens guérisseur de la transformation spirituelle.",
        "Chiron en Sagittaire dans ta maison VIII révèle une blessure autour de la perte de foi dans les moments de crise. Tu as pu douter de l'univers dans les épreuves.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver du sens dans leurs crises et à se transformer spirituellement.",
        "Cette position en maison VIII peut avoir créé une crise de foi profonde lors de pertes. Tu apprends que le sens survit à la destruction.",
        "Trouve du sens dans une expérience difficile.",
        "Respire en sentant que même la crise a un sens.",
        "Quelle crise a ébranlé ma foi dans la vie ? »"),

    ('sagittarius', 9): make_chiron_interp('sagittarius', 9,
        "Ta blessure touche les croyances et la vérité — tu deviens guérisseur de la quête spirituelle.",
        "Chiron en Sagittaire dans ta maison IX (son domicile) révèle une blessure profonde autour des croyances, de la religion et de la vérité. Tu as pu être blessé par des dogmes ou perdre ta foi.",
        "En traversant cette blessure, tu développes un don exceptionnel pour guider les autres dans leur quête spirituelle vers leur propre vérité.",
        "Cette position en maison IX intensifie la blessure spirituelle. Tu as peut-être traversé des crises de foi profondes. Tu deviens un guide pour les chercheurs.",
        "Explore une nouvelle perspective spirituelle.",
        "Respire en honorant ton chemin unique vers la vérité.",
        "Quelle blessure spirituelle ou religieuse n'ai-je pas guérie ? »"),

    ('sagittarius', 10): make_chiron_interp('sagittarius', 10,
        "Ta blessure touche la mission de vie — tu deviens guérisseur de la vocation.",
        "Chiron en Sagittaire dans ta maison X révèle une blessure autour de ta mission et de ta vocation. Tu as pu douter de ton but dans la vie ou te sentir perdu professionnellement.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur mission et à aligner leur carrière avec leur vision.",
        "Cette position en maison X peut créer des difficultés à trouver ta place dans le monde. Tu apprends que ta mission est de guider.",
        "Clarifie un aspect de ta mission de vie.",
        "Respire en sentant l'appel de ta vocation.",
        "Où me suis-je senti perdu par rapport à ma mission de vie ? »"),

    ('sagittarius', 11): make_chiron_interp('sagittarius', 11,
        "Ta blessure touche la foi dans l'humanité — tu deviens guérisseur de l'espoir collectif.",
        "Chiron en Sagittaire dans ta maison XI révèle une blessure autour de la foi dans les groupes et dans l'humanité. Tu as pu être déçu par des causes ou des communautés.",
        "En traversant cette blessure, tu développes un don pour aider les communautés à retrouver leur vision et leur espoir.",
        "Cette position en maison XI peut avoir créé un cynisme envers les idéaux collectifs. Tu apprends à réinventer l'espoir.",
        "Contribue à une cause en laquelle tu crois.",
        "Respire en renouvelant ta foi dans l'humanité.",
        "Quelle déception collective m'a fait perdre foi dans les groupes ? »"),

    ('sagittarius', 12): make_chiron_interp('sagittarius', 12,
        "Ta blessure touche la foi cosmique — tu deviens guérisseur de la connexion au divin.",
        "Chiron en Sagittaire dans ta maison XII révèle une blessure profonde autour de la spiritualité et de ta connexion au divin. Tu peux porter une crise de foi existentielle.",
        "En traversant cette blessure, tu développes un don pour guider les autres vers une connexion authentique avec le sacré.",
        "Cette position en maison XII porte une dimension karmique spirituelle. Tu as peut-être été blessé par la religion dans d'autres vies. Tu apprends la foi sans dogme.",
        "Médite sur ta connexion personnelle au sacré.",
        "Respire en sentant la présence du divin.",
        "Quelle blessure spirituelle profonde porte mon âme ? »"),

    # === CAPRICORN (M1-M12) ===
    ('capricorn', 1): make_chiron_interp('capricorn', 1,
        "Ta blessure touche l'autorité et la structure — tu deviens guérisseur du leadership.",
        "Chiron en Capricorne dans ta maison I révèle une blessure profonde autour de l'autorité et de la structure. Tu as pu te sentir inadéquat face aux responsabilités ou rejeté par les figures d'autorité.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à assumer leur autorité et à structurer leur vie.",
        "Cette position en maison I rend la blessure visible dans ton rapport à la responsabilité. Tu apprends que ton autorité peut guérir.",
        "Assume une responsabilité avec confiance.",
        "Respire en te sentant capable de leadership.",
        "Où me suis-je senti inadéquat face à l'autorité ou aux responsabilités ? »"),

    ('capricorn', 2): make_chiron_interp('capricorn', 2,
        "Ta blessure touche la construction de la richesse — tu deviens guérisseur de l'abondance structurée.",
        "Chiron en Capricorne dans ta maison II révèle une blessure autour de la construction de ressources et de la sécurité à long terme. Tu as pu douter de ta capacité à bâtir.",
        "En traversant cette blessure, tu développes un don pour aider les autres à construire une base financière solide.",
        "Cette position en maison II peut créer une peur de ne jamais avoir assez ou une difficulté à construire. Tu apprends la patience de la construction.",
        "Construis quelque chose de durable pour ta sécurité.",
        "Respire en te sentant capable de bâtir ta richesse.",
        "Quelle peur de ne pas réussir à construire ma sécurité porte-je ? »"),

    ('capricorn', 3): make_chiron_interp('capricorn', 3,
        "Ta blessure touche la communication d'autorité — tu deviens guérisseur de la parole structurée.",
        "Chiron en Capricorne dans ta maison III révèle une blessure autour de ta légitimité à parler avec autorité. Tu as pu te sentir pas assez qualifié ou pas écouté.",
        "En traversant cette blessure, tu développes un don pour aider les autres à communiquer avec autorité et structure.",
        "Cette position en maison III peut avoir créé un sentiment d'illégitimité dans l'expression de tes idées. Tu apprends la parole qui bâtit.",
        "Communique une idée avec confiance et structure.",
        "Respire en te sentant légitime à parler avec autorité.",
        "Où me suis-je senti pas assez qualifié pour m'exprimer ? »"),

    ('capricorn', 4): make_chiron_interp('capricorn', 4,
        "Ta blessure touche l'autorité parentale — tu deviens guérisseur des racines structurées.",
        "Chiron en Capricorne dans ta maison IV révèle une blessure autour de la figure paternelle ou de l'autorité au foyer. Tu as pu manquer de structure ou subir une autorité froide.",
        "En traversant cette blessure, tu développes un don pour aider les autres à guérir leurs blessures paternelles et à créer des structures familiales saines.",
        "Cette position en maison IV peut avoir été marquée par un père absent, froid ou trop strict. Tu apprends l'autorité aimante.",
        "Crée une structure bienveillante dans ton foyer.",
        "Respire en te sentant soutenu par une autorité aimante.",
        "Quelle blessure paternelle ou d'autorité familiale n'ai-je pas guérie ? »"),

    ('capricorn', 5): make_chiron_interp('capricorn', 5,
        "Ta blessure touche la joie et l'ambition — tu deviens guérisseur de la création structurée.",
        "Chiron en Capricorne dans ta maison V révèle une blessure autour de la joie et de la créativité face à l'ambition. Tu as pu sacrifier le plaisir pour le devoir.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer et aimer tout en construisant quelque chose de durable.",
        "Cette position en maison V peut avoir créé un conflit entre joie et responsabilité. Tu apprends que la joie peut être une discipline.",
        "Crée quelque chose avec joie ET structure.",
        "Respire en autorisant la joie dans ta discipline.",
        "Comment ai-je sacrifié la joie au nom du devoir ? »"),

    ('capricorn', 6): make_chiron_interp('capricorn', 6,
        "Ta blessure touche le travail et le devoir — tu deviens guérisseur du travail sain.",
        "Chiron en Capricorne dans ta maison VI révèle une blessure autour du travail et de la responsabilité quotidienne. Tu as pu te sentir écrasé par le devoir ou jamais assez performant.",
        "En traversant cette blessure, tu développes un don pour aider les autres à travailler de façon structurée sans s'épuiser.",
        "Cette position en maison VI peut créer un rapport toxique au travail ou au perfectionnisme. Tu apprends le travail équilibré.",
        "Travaille avec structure mais aussi avec compassion pour toi.",
        "Respire en relâchant la pression du devoir.",
        "Où me suis-je épuisé à essayer d'atteindre des standards impossibles ? »"),

    ('capricorn', 7): make_chiron_interp('capricorn', 7,
        "Ta blessure touche l'engagement et le partenariat — tu deviens guérisseur des relations durables.",
        "Chiron en Capricorne dans ta maison VII révèle une blessure autour de l'engagement et de la responsabilité dans les relations. Tu as pu avoir peur de l'engagement ou te sentir piégé.",
        "En traversant cette blessure, tu développes un don pour aider les couples à bâtir des relations solides et durables.",
        "Cette position en maison VII peut créer des peurs de l'engagement ou des partenariats trop rigides. Tu apprends l'engagement flexible.",
        "Engage-toi dans une relation avec confiance.",
        "Respire en te sentant capable d'engagement sain.",
        "Comment mes peurs de l'engagement ont-elles affecté mes relations ? »"),

    ('capricorn', 8): make_chiron_interp('capricorn', 8,
        "Ta blessure touche le contrôle dans les crises — tu deviens guérisseur de la transformation structurée.",
        "Chiron en Capricorne dans ta maison VIII révèle une blessure autour du contrôle dans les moments de crise. Tu as pu te sentir impuissant malgré tous tes efforts.",
        "En traversant cette blessure, tu développes un don pour aider les autres à traverser les crises avec structure et résilience.",
        "Cette position en maison VIII peut créer une peur de perdre le contrôle dans les transformations. Tu apprends le lâcher-prise structuré.",
        "Lâche le contrôle tout en gardant ta structure intérieure.",
        "Respire en faisant confiance au processus.",
        "Où mon besoin de contrôle m'a-t-il empêché de me transformer ? »"),

    ('capricorn', 9): make_chiron_interp('capricorn', 9,
        "Ta blessure touche l'autorité spirituelle — tu deviens guérisseur de la sagesse structurée.",
        "Chiron en Capricorne dans ta maison IX révèle une blessure autour des institutions spirituelles et de l'autorité religieuse. Tu as pu être blessé par des structures dogmatiques.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver une spiritualité qui intègre structure et liberté.",
        "Cette position en maison IX peut avoir créé des conflits avec les institutions religieuses ou éducatives. Tu apprends la sagesse qui bâtit.",
        "Trouve une structure spirituelle qui te soutient sans t'enfermer.",
        "Respire en intégrant sagesse et structure.",
        "Quelle blessure institutionnelle ou religieuse n'ai-je pas guérie ? »"),

    ('capricorn', 10): make_chiron_interp('capricorn', 10,
        "Ta blessure touche le succès et la reconnaissance — tu deviens guérisseur de la réussite.",
        "Chiron en Capricorne dans ta maison X (son domicile) révèle une blessure profonde autour du succès, de la carrière et de la reconnaissance. Tu as pu te sentir jamais assez accompli.",
        "En traversant cette blessure, tu développes un don exceptionnel pour aider les autres à atteindre leur potentiel et à assumer leur réussite.",
        "Cette position en maison X intensifie la blessure d'accomplissement. Tu as peut-être eu un rapport difficile à l'ambition. Tu apprends la réussite authentique.",
        "Reconnais un de tes accomplissements avec fierté.",
        "Respire en te sentant assez, même sans plus d'accomplissement.",
        "Quelle blessure d'accomplissement ou de reconnaissance porte-je ? »"),

    ('capricorn', 11): make_chiron_interp('capricorn', 11,
        "Ta blessure touche la place dans la société — tu deviens guérisseur des structures collectives.",
        "Chiron en Capricorne dans ta maison XI révèle une blessure autour de ta place dans les structures sociales et les groupes organisés. Tu as pu te sentir exclu ou en conflit avec les hiérarchies.",
        "En traversant cette blessure, tu développes un don pour aider les groupes à créer des structures justes et inclusives.",
        "Cette position en maison XI peut créer des difficultés avec les organisations et les institutions. Tu apprends à transformer les structures.",
        "Contribue à améliorer une structure collective.",
        "Respire en te sentant capable de changer les systèmes.",
        "Où me suis-je senti exclu ou en conflit avec les structures sociales ? »"),

    ('capricorn', 12): make_chiron_interp('capricorn', 12,
        "Ta blessure touche l'autorité intérieure — tu deviens guérisseur de la structure spirituelle.",
        "Chiron en Capricorne dans ta maison XII révèle une blessure profonde autour de l'autorité karmique et de la structure intérieure. Tu peux porter une culpabilité ancienne liée au pouvoir.",
        "En traversant cette blessure, tu développes un don pour aider les autres à construire une autorité intérieure saine et spirituelle.",
        "Cette position en maison XII porte une dimension karmique d'autorité. Tu as peut-être été une figure d'autorité dans d'autres vies. Tu apprends l'autorité humble.",
        "Médite sur ton autorité intérieure avec humilité.",
        "Respire en sentant ta structure spirituelle.",
        "Quelle culpabilité liée au pouvoir porte mon âme ? »"),

    # === AQUARIUS (M1-M12) ===
    ('aquarius', 1): make_chiron_interp('aquarius', 1,
        "Ta blessure touche ta différence et ton originalité — tu deviens guérisseur de l'unicité.",
        "Chiron en Verseau dans ta maison I révèle une blessure profonde autour de ta différence et de ton originalité. Tu as pu te sentir trop différent, exclu ou bizarre.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à embrasser leur différence et à célébrer leur unicité.",
        "Cette position en maison I rend la blessure visible dans ton rapport à ta différence. Tu apprends que ton unicité est ton plus grand don.",
        "Célèbre quelque chose d'unique en toi.",
        "Respire en embrassant ta différence.",
        "Où me suis-je senti rejeté pour ma différence ? »"),

    ('aquarius', 2): make_chiron_interp('aquarius', 2,
        "Ta blessure touche la valeur de l'originalité — tu deviens guérisseur de l'abondance innovante.",
        "Chiron en Verseau dans ta maison II révèle une blessure autour de la valeur de tes idées originales. Tu as pu douter que ta créativité puisse avoir de la valeur.",
        "En traversant cette blessure, tu développes un don pour aider les autres à monétiser leur originalité et leurs innovations.",
        "Cette position en maison II peut créer un sentiment que tes idées révolutionnaires ne valent rien. Tu apprends que l'innovation crée de la valeur.",
        "Valorise une de tes idées originales.",
        "Respire en te sentant riche de ton originalité.",
        "Comment ai-je dévalorisé mes idées innovantes ? »"),

    ('aquarius', 3): make_chiron_interp('aquarius', 3,
        "Ta blessure touche la communication de tes idées uniques — tu deviens guérisseur de la pensée libre.",
        "Chiron en Verseau dans ta maison III révèle une blessure autour de l'expression de tes idées non-conventionnelles. Tu as pu te sentir incompris ou ridiculisé.",
        "En traversant cette blessure, tu développes un don pour aider les autres à exprimer leurs idées innovantes sans peur du jugement.",
        "Cette position en maison III peut avoir créé des blocages dans l'expression de pensées hors-normes. Tu apprends que ta vision mérite d'être partagée.",
        "Exprime une idée originale sans te censurer.",
        "Respire en validant ta pensée unique.",
        "Quelles idées originales ai-je gardées pour moi par peur du jugement ? »"),

    ('aquarius', 4): make_chiron_interp('aquarius', 4,
        "Ta blessure touche l'appartenance familiale — tu deviens guérisseur des familles non-conventionnelles.",
        "Chiron en Verseau dans ta maison IV révèle une blessure autour de ton appartenance à ta famille et de ta différence au sein du foyer. Tu as pu te sentir l'étranger de la famille.",
        "En traversant cette blessure, tu développes un don pour aider les familles à accepter leurs membres différents et à créer des foyers inclusifs.",
        "Cette position en maison IV peut avoir créé un sentiment d'être le « mouton noir » de la famille. Tu apprends à créer ta propre définition de la famille.",
        "Crée un espace d'acceptation dans ton foyer.",
        "Respire en te sentant appartenir malgré ta différence.",
        "Comment ma différence m'a-t-elle séparé de ma famille ? »"),

    ('aquarius', 5): make_chiron_interp('aquarius', 5,
        "Ta blessure touche la créativité innovante — tu deviens guérisseur de l'expression originale.",
        "Chiron en Verseau dans ta maison V révèle une blessure autour de ta créativité non-conventionnelle. Tu as pu te sentir trop bizarre pour créer ou aimer.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer et aimer de façon unique et authentique.",
        "Cette position en maison V peut avoir inhibé ta créativité ou tes amours par peur d'être trop différent. Tu apprends l'amour et la création libres.",
        "Crée quelque chose d'original et unique.",
        "Respire en célébrant ta créativité non-conformiste.",
        "Comment ma peur d'être trop différent a-t-elle limité ma créativité ou mes amours ? »"),

    ('aquarius', 6): make_chiron_interp('aquarius', 6,
        "Ta blessure touche la place au travail — tu deviens guérisseur des environnements de travail innovants.",
        "Chiron en Verseau dans ta maison VI révèle une blessure autour de ta différence dans le travail quotidien. Tu as pu te sentir inadapté aux environnements de travail conventionnels.",
        "En traversant cette blessure, tu développes un don pour créer des environnements de travail qui accueillent la différence et l'innovation.",
        "Cette position en maison VI peut créer des difficultés avec les routines et les structures rigides. Tu apprends à transformer le quotidien.",
        "Apporte de l'innovation dans une routine de travail.",
        "Respire en te sentant à ta place même si tu es différent.",
        "Où me suis-je senti inadapté au travail conventionnel ? »"),

    ('aquarius', 7): make_chiron_interp('aquarius', 7,
        "Ta blessure touche les relations non-conventionnelles — tu deviens guérisseur des partenariats uniques.",
        "Chiron en Verseau dans ta maison VII révèle une blessure autour de ta différence dans les relations. Tu as pu te sentir trop unique pour trouver un partenaire compatible.",
        "En traversant cette blessure, tu développes un don pour aider les couples à créer des relations uniques qui honorent la différence de chacun.",
        "Cette position en maison VII peut attirer des partenaires qui activent ta blessure de différence. Tu apprends les relations qui célèbrent l'unicité.",
        "Crée une relation qui honore ton unicité.",
        "Respire en te sentant aimable dans ta différence.",
        "Comment ma différence a-t-elle affecté mes relations ? »"),

    ('aquarius', 8): make_chiron_interp('aquarius', 8,
        "Ta blessure touche l'aliénation dans les crises — tu deviens guérisseur des transformations collectives.",
        "Chiron en Verseau dans ta maison VIII révèle une blessure autour de l'isolement dans les moments de crise. Tu as pu te sentir seul face aux transformations.",
        "En traversant cette blessure, tu développes un don pour aider les autres à traverser les crises ensemble et à transformer collectivement.",
        "Cette position en maison VIII peut créer un sentiment d'aliénation dans les moments difficiles. Tu apprends la transformation communautaire.",
        "Connecte-toi avec d'autres pour traverser une transformation.",
        "Respire en te sentant accompagné dans les crises.",
        "Où me suis-je senti isolé dans mes moments de crise ? »"),

    ('aquarius', 9): make_chiron_interp('aquarius', 9,
        "Ta blessure touche les idées révolutionnaires — tu deviens guérisseur de la pensée progressiste.",
        "Chiron en Verseau dans ta maison IX révèle une blessure autour de tes visions futuristes et de tes idées révolutionnaires. Tu as pu être rejeté pour tes idées avant-gardistes.",
        "En traversant cette blessure, tu développes un don pour aider les autres à embrasser des visions progressistes et à penser l'avenir.",
        "Cette position en maison IX peut avoir créé des conflits avec les institutions conservatrices. Tu apprends à être un pionnier de la pensée.",
        "Partage une vision futuriste avec confiance.",
        "Respire en te sentant légitime dans tes idées progressistes.",
        "Quelles idées révolutionnaires ai-je abandonnées face au rejet ? »"),

    ('aquarius', 10): make_chiron_interp('aquarius', 10,
        "Ta blessure touche la carrière non-conventionnelle — tu deviens guérisseur des parcours uniques.",
        "Chiron en Verseau dans ta maison X révèle une blessure autour de ta carrière et de ton chemin non-conventionnel. Tu as pu te sentir inadapté aux parcours classiques.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer des carrières uniques qui honorent leur différence.",
        "Cette position en maison X peut créer des difficultés dans les carrières traditionnelles. Tu apprends à tracer ton propre chemin.",
        "Assume ton parcours professionnel unique.",
        "Respire en te sentant légitime dans ta carrière non-conventionnelle.",
        "Comment mon inadaptation aux parcours classiques a-t-elle affecté ma carrière ? »"),

    ('aquarius', 11): make_chiron_interp('aquarius', 11,
        "Ta blessure touche l'appartenance au groupe — tu deviens guérisseur de l'inclusion.",
        "Chiron en Verseau dans ta maison XI (son domicile) révèle une blessure profonde autour de l'appartenance aux groupes et de l'acceptation de ta différence. Tu as pu te sentir exclu ou trop différent pour appartenir.",
        "En traversant cette blessure, tu développes un don exceptionnel pour créer des communautés inclusives qui célèbrent la diversité.",
        "Cette position en maison XI intensifie la blessure d'appartenance. Tu as peut-être été rejeté par des groupes. Tu deviens un créateur de communautés.",
        "Crée ou rejoins un groupe qui célèbre la différence.",
        "Respire en te sentant appartenir tout en étant unique.",
        "Quelle expérience de rejet de groupe n'ai-je pas guérie ? »"),

    ('aquarius', 12): make_chiron_interp('aquarius', 12,
        "Ta blessure touche l'aliénation cosmique — tu deviens guérisseur de la connexion universelle.",
        "Chiron en Verseau dans ta maison XII révèle une blessure profonde autour de l'aliénation et de la déconnexion. Tu peux te sentir étranger sur cette planète.",
        "En traversant cette blessure, tu développes un don pour aider les autres à se sentir connectés à l'humanité tout en honorant leur unicité.",
        "Cette position en maison XII porte une dimension karmique d'aliénation. Tu es peut-être une « vieille âme » qui se sent hors du temps. Tu apprends l'appartenance cosmique.",
        "Médite sur ta connexion à l'humanité.",
        "Respire en te sentant partie du tout.",
        "Quelle aliénation cosmique porte mon âme ? »"),

    # === PISCES (M1-M12) ===
    ('pisces', 1): make_chiron_interp('pisces', 1,
        "Ta blessure touche ta sensibilité et tes limites — tu deviens guérisseur de l'âme.",
        "Chiron en Poissons dans ta maison I révèle une blessure profonde autour de ta sensibilité extrême et de tes limites floues. Tu as pu te sentir submergé par les émotions ou perdu dans les autres.",
        "En traversant cette blessure, tu développes un don unique pour guérir l'âme des autres et les aider à naviguer leur sensibilité.",
        "Cette position en maison I rend la blessure visible dans ta porosité émotionnelle. Tu apprends que ta sensibilité est un don de guérison.",
        "Honore ta sensibilité comme une force.",
        "Respire en te sentant protégé malgré ta porosité.",
        "Où ma sensibilité a-t-elle été une source de souffrance ? »"),

    ('pisces', 2): make_chiron_interp('pisces', 2,
        "Ta blessure touche la valeur de l'invisible — tu deviens guérisseur de l'abondance spirituelle.",
        "Chiron en Poissons dans ta maison II révèle une blessure autour de la valeur de tes dons spirituels et intuitifs. Tu as pu douter que l'invisible puisse avoir de la valeur.",
        "En traversant cette blessure, tu développes un don pour aider les autres à reconnaître la valeur de leurs dons spirituels.",
        "Cette position en maison II peut créer un conflit entre le matériel et le spirituel. Tu apprends que l'invisible crée la vraie richesse.",
        "Valorise un de tes dons intuitifs ou spirituels.",
        "Respire en te sentant riche de tes dons invisibles.",
        "Comment ai-je dévalorisé mes dons spirituels ou intuitifs ? »"),

    ('pisces', 3): make_chiron_interp('pisces', 3,
        "Ta blessure touche la communication de l'invisible — tu deviens guérisseur de la parole intuitive.",
        "Chiron en Poissons dans ta maison III révèle une blessure autour de l'expression de tes perceptions intuitives. Tu as pu te sentir incompris ou pas cru.",
        "En traversant cette blessure, tu développes un don pour aider les autres à communiquer leurs intuitions et leurs perceptions subtiles.",
        "Cette position en maison III peut avoir créé des blocages dans l'expression de tes perceptions. Tu apprends à parler depuis l'âme.",
        "Exprime une perception intuitive sans la censurer.",
        "Respire en validant ta façon unique de percevoir.",
        "Quelles perceptions intuitives ai-je gardées pour moi par peur du jugement ? »"),

    ('pisces', 4): make_chiron_interp('pisces', 4,
        "Ta blessure touche les émotions familiales — tu deviens guérisseur de l'inconscient familial.",
        "Chiron en Poissons dans ta maison IV révèle une blessure autour des émotions non-dites et des secrets de ta famille. Tu as pu absorber la douleur familiale.",
        "En traversant cette blessure, tu développes un don pour aider les familles à guérir leurs traumatismes inconscients et leurs non-dits.",
        "Cette position en maison IV peut avoir fait de toi l'éponge émotionnelle de ta famille. Tu apprends à guérir sans absorber.",
        "Libère une émotion familiale que tu portes.",
        "Respire en distinguant tes émotions de celles des autres.",
        "Quelle douleur familiale ai-je absorbée sans qu'elle m'appartienne ? »"),

    ('pisces', 5): make_chiron_interp('pisces', 5,
        "Ta blessure touche la créativité et l'amour idéalisé — tu deviens guérisseur de l'art sacré.",
        "Chiron en Poissons dans ta maison V révèle une blessure autour de la créativité spirituelle et de l'amour idéal. Tu as pu être déçu par l'amour ou la création qui ne correspondait pas à ton idéal.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer et aimer de façon sacrée et transcendante.",
        "Cette position en maison V peut avoir créé des désillusions amoureuses ou créatives. Tu apprends l'amour et la création qui élèvent.",
        "Crée quelque chose qui touche l'âme.",
        "Respire en te connectant à ta source créative divine.",
        "Comment mes idéaux ont-ils créé des désillusions en amour ou en création ? »"),

    ('pisces', 6): make_chiron_interp('pisces', 6,
        "Ta blessure touche le service et le sacrifice — tu deviens guérisseur du quotidien.",
        "Chiron en Poissons dans ta maison VI révèle une blessure autour du service et du sacrifice quotidien. Tu as pu t'épuiser à donner sans limites.",
        "En traversant cette blessure, tu développes un don pour aider les autres à servir avec compassion sans se perdre.",
        "Cette position en maison VI peut créer des problèmes de santé liés à l'absorption des énergies des autres. Tu apprends le service avec limites.",
        "Sers quelqu'un tout en gardant tes limites.",
        "Respire en te protégeant énergétiquement.",
        "Où me suis-je épuisé à servir sans limites ? »"),

    ('pisces', 7): make_chiron_interp('pisces', 7,
        "Ta blessure touche la fusion dans les relations — tu deviens guérisseur de l'amour universel.",
        "Chiron en Poissons dans ta maison VII révèle une blessure autour de la fusion et de la perte de soi dans les relations. Tu as pu te perdre dans l'autre ou idéaliser tes partenaires.",
        "En traversant cette blessure, tu développes un don pour aider les autres à aimer profondément sans se perdre.",
        "Cette position en maison VII peut créer des relations où tu te dissous. Tu apprends l'amour qui préserve l'individualité.",
        "Aime profondément tout en gardant ton centre.",
        "Respire en te sentant entier même dans la fusion.",
        "Où me suis-je perdu dans mes relations ? »"),

    ('pisces', 8): make_chiron_interp('pisces', 8,
        "Ta blessure touche la dissolution dans les crises — tu deviens guérisseur des passages de l'âme.",
        "Chiron en Poissons dans ta maison VIII révèle une blessure autour de la perte, de la mort et de la dissolution. Tu as pu vivre des expériences de dissolution traumatiques.",
        "En traversant cette blessure, tu développes un don pour accompagner les autres dans les passages les plus profonds de l'âme.",
        "Cette position en maison VIII peut avoir créé des expériences de mort mystique ou de dissolution effrayantes. Tu apprends à naviguer les eaux profondes.",
        "Accompagne quelqu'un dans un passage difficile.",
        "Respire en faisant confiance au processus de dissolution.",
        "Quelle expérience de dissolution ou de perte n'ai-je pas intégrée ? »"),

    ('pisces', 9): make_chiron_interp('pisces', 9,
        "Ta blessure touche la foi et la désillusion — tu deviens guérisseur de la spiritualité authentique.",
        "Chiron en Poissons dans ta maison IX révèle une blessure autour de la foi et des désillusions spirituelles. Tu as pu perdre foi dans le divin ou être trahi par des gurus.",
        "En traversant cette blessure, tu développes un don pour guider les autres vers une spiritualité authentique, au-delà des illusions.",
        "Cette position en maison IX peut avoir créé des crises de foi ou des abus spirituels. Tu apprends la connexion directe au divin.",
        "Renoue avec ta propre connexion spirituelle authentique.",
        "Respire en sentant le sacré sans intermédiaire.",
        "Quelle désillusion spirituelle n'ai-je pas guérie ? »"),

    ('pisces', 10): make_chiron_interp('pisces', 10,
        "Ta blessure touche la vocation et le sacrifice — tu deviens guérisseur de la mission de service.",
        "Chiron en Poissons dans ta maison X révèle une blessure autour de ta vocation et du sacrifice pour ta mission. Tu as pu sacrifier ta vie personnelle pour une cause.",
        "En traversant cette blessure, tu développes un don pour aider les autres à servir leur mission sans se détruire.",
        "Cette position en maison X peut créer des carrières de service qui épuisent. Tu apprends à servir ta mission avec équilibre.",
        "Sers ta mission tout en prenant soin de toi.",
        "Respire en sentant ta vocation sans sacrifice excessif.",
        "Comment ai-je sacrifié ma vie personnelle pour ma mission ? »"),

    ('pisces', 11): make_chiron_interp('pisces', 11,
        "Ta blessure touche la fusion avec l'humanité — tu deviens guérisseur de la compassion collective.",
        "Chiron en Poissons dans ta maison XI révèle une blessure autour de ta connexion à l'humanité et de ta sensibilité aux souffrances collectives. Tu as pu te sentir submergé par les maux du monde.",
        "En traversant cette blessure, tu développes un don pour aider les communautés à guérir et à éveiller leur compassion collective.",
        "Cette position en maison XI peut créer une surcharge émotionnelle face aux problèmes du monde. Tu apprends la compassion avec limites.",
        "Contribue à une cause humanitaire sans te perdre.",
        "Respire en te protégeant de la souffrance collective.",
        "Comment ma sensibilité aux maux du monde m'a-t-elle submergé ? »"),

    ('pisces', 12): make_chiron_interp('pisces', 12,
        "Ta blessure touche la connexion au tout — tu deviens guérisseur de l'âme universelle.",
        "Chiron en Poissons dans ta maison XII (son domicile) révèle une blessure profonde et karmique autour de la spiritualité, de la dissolution et de la connexion au tout. Tu portes peut-être des blessures de l'humanité entière.",
        "En traversant cette blessure, tu développes un don exceptionnel pour guérir l'âme collective et accompagner les autres dans leur éveil spirituel.",
        "Cette position en maison XII est la plus puissante pour la guérison. Tu es un guérisseur né, connecté à la source. Tu apprends à guérir sans te dissoudre.",
        "Médite en envoyant de la guérison au monde.",
        "Respire en sentant ta connexion au tout.",
        "Quelle blessure de l'humanité porte mon âme ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in CHIRON_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'chiron',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP chiron/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='chiron',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT chiron/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
