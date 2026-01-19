#!/usr/bin/env python3
"""
Insert Ascendant interpretations for Leo, Virgo, Libra, Scorpio (48 entries)
Version 2 format with consistent structure
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from uuid import uuid4
from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation


def make_asc_interp(sign_name: str, house: int, phrase: str, masque: str, approche: str, tips: list[str]) -> str:
    """Generate Ascendant interpretation with consistent structure."""
    tips_formatted = "\n".join(f"- {t}" for t in tips)
    return f"""# ↑ Ascendant en {sign_name}

**En une phrase :** {phrase}

## Ton masque au monde
{masque}

## Ton approche spontanée
{approche}

## Pistes d'intégration
{tips_formatted}"""


ASCENDANT_INTERPRETATIONS = {
    # LEO ASCENDANT
    ('leo', 1): make_asc_interp(
        "Lion", 1,
        "Tu te présentes au monde avec éclat — ton approche spontanée est celle de l'expression créative.",
        "Ton masque est celui du roi, de l'être lumineux et charismatique. Les gens te perçoivent comme quelqu'un de confiant, généreux et dramatique. Tu dégages une aura de noblesse qui attire l'attention. Ta présence physique est souvent imposante, avec une allure fière.",
        "Tu abordes la vie comme une scène où tu es la star. Face à une situation, ton instinct est de briller, de créer, d'exprimer. Cette expressivité te rend magnétique mais parfois centré sur toi-même. Tu préfères être admiré à passer inaperçu.",
        ["Brille de ton éclat authentique.", "Partage ta lumière sans chercher l'approbation.", "Journal : « Comment mon besoin de reconnaissance me guide-t-il dans la vie ? »"]
    ),
    ('leo', 2): make_asc_interp(
        "Lion", 2,
        "Tu te présentes au monde avec fierté — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie royale influence ta façon de gagner et de dépenser. Tu es perçu comme quelqu'un de généreux qui apprécie le luxe et la qualité. Tu veux des ressources qui reflètent ta valeur et ta dignité.",
        "Tu abordes les questions d'argent avec un sens du prestige. Tu préfères dépenser pour des choses qui impressionnent ou qui sont de qualité. Tu es généreux avec ceux que tu aimes mais tu attends aussi d'être traité royalement.",
        ["Exprime ta générosité avec tes ressources.", "Évite de dépenser pour impressionner.", "Journal : « Comment mon sens du prestige influence-t-il mes finances ? »"]
    ),
    ('leo', 3): make_asc_interp(
        "Lion", 3,
        "Tu te présentes au monde avec panache — ton approche spontanée s'exprime dans ta communication.",
        "Ta façon de communiquer est dramatique, expressive. Les gens te perçoivent comme quelqu'un qui a du charisme quand il parle. Dans ton environnement proche, tu es celui qui capte l'attention. Tes échanges avec frères et sœurs peuvent être compétitifs pour la reconnaissance.",
        "Tu communiques avec flair et tu aimes être écouté. Ton esprit est créatif et tu as le don de raconter des histoires. Tu as besoin que tes idées soient reconnues et appréciées.",
        ["Exprime-toi avec ton cœur créatif.", "Écoute les autres autant que tu parles.", "Journal : « Comment mon besoin de reconnaissance colore-t-il ma communication ? »"]
    ),
    ('leo', 4): make_asc_interp(
        "Lion", 4,
        "Tu te présentes au monde avec chaleur — ton approche spontanée crée un foyer royal.",
        "Ton énergie de leader se manifeste dans ta vie privée et familiale. Tu as besoin d'un chez-toi qui soit un palais, même modeste — un lieu qui te reflète et dont tu peux être fier. Tes racines sont marquées par une fierté familiale ou un parent charismatique.",
        "Tu abordes ta vie privée avec un besoin de créer quelque chose de spécial. Tu veux que ta famille soit fière et que ton foyer soit accueillant et impressionnant. Tu peux avoir tendance à vouloir contrôler l'image de ta famille.",
        ["Crée un foyer dont tu es fier.", "Laisse chaque membre de la famille briller à sa façon.", "Journal : « Comment mon besoin de fierté influence-t-il ma vie familiale ? »"]
    ),
    ('leo', 5): make_asc_interp(
        "Lion", 5,
        "Tu te présentes au monde avec majesté — ton approche spontanée s'épanouit dans la créativité.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement l'énergie léonine de création et d'expression. Tu es perçu comme quelqu'un de passionné et créatif. En amour, tu brilles et tu veux être admiré. Avec les enfants, tu es un parent fier et joueur.",
        "Tu abordes les loisirs et la romance comme des occasions de briller. Tes créations sont une extension de toi et tu y mets tout ton cœur. Tu as besoin d'applaudissements pour te sentir vivant.",
        ["Exprime ta créativité sans retenue.", "Apprécie l'admiration sans en dépendre.", "Journal : « Comment mon éclat naturel s'exprime-t-il dans mes passions et mes amours ? »"]
    ),
    ('leo', 6): make_asc_interp(
        "Lion", 6,
        "Tu te présentes au monde avec dignité — ton approche spontanée s'applique au service.",
        "Ta façon d'aborder le travail quotidien est fière et consciencieuse. Tu es perçu comme quelqu'un qui apporte de la qualité et de l'éclat à son travail. Tu excelles dans les rôles où tu peux montrer ton talent et être reconnu.",
        "Tu abordes les routines avec un besoin de les rendre spéciales. Tu as du mal avec les tâches ingrates ou invisibles. Ta santé est liée à ta capacité à t'exprimer — réprimer ta créativité affecte ton cœur.",
        ["Apporte ton éclat à ton travail quotidien.", "Trouve de la fierté même dans les tâches simples.", "Journal : « Comment mon besoin de reconnaissance influence-t-il mon travail ? »"]
    ),
    ('leo', 7): make_asc_interp(
        "Lion", 7,
        "Tu te présentes au monde avec grandeur — ton approche spontanée recherche des relations admiratives.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes qui t'admirent ou qui sont elles-mêmes admirables. Tu veux un partenaire dont tu peux être fier. Tu peux avoir tendance à vouloir être le centre de la relation.",
        "Tu abordes les associations avec un besoin de briller ensemble. Tu veux des relations qui élèvent, qui impressionnent. Tu as du mal avec les partenaires qui te font de l'ombre ou qui ne te valorisent pas.",
        ["Crée des partenariats où chacun peut briller.", "Admire ton partenaire autant que tu veux être admiré.", "Journal : « Comment mon besoin d'être vu influence-t-il mes partenariats ? »"]
    ),
    ('leo', 8): make_asc_interp(
        "Lion", 8,
        "Tu te présentes au monde avec force — ton approche spontanée s'applique aux transformations profondes.",
        "Tu abordes les crises et les transformations avec courage et dignité. Tu refuses de montrer ta vulnérabilité facilement. Les questions d'intimité et de pouvoir sont abordées avec fierté — tu veux garder le contrôle même dans la vulnérabilité.",
        "Face aux épreuves, ton instinct est de rester noble et fort. Tu peux avoir du mal à demander de l'aide ou à montrer ta faiblesse. Mais ta capacité à transformer l'adversité en force est remarquable.",
        ["Traverse les crises avec ta dignité intacte.", "Permets-toi d'être vulnérable avec ceux qui t'aiment.", "Journal : « Comment mon besoin de contrôle influence-t-il ma façon de gérer les crises ? »"]
    ),
    ('leo', 9): make_asc_interp(
        "Lion", 9,
        "Tu te présentes au monde avec enthousiasme — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances et d'aventure est teintée de grandeur. Tu es attiré par les philosophies qui élèvent l'âme humaine. Tu explores le monde comme un souverain découvrant son royaume — avec curiosité et assurance.",
        "Tu abordes les études supérieures et les voyages avec enthousiasme et fierté. Tu veux apprendre ce qui te rend plus grand. Tes convictions sont fortes et tu les défends avec passion.",
        ["Explore de nouveaux horizons avec ton cœur généreux.", "Reste humble face aux sagesses millénaires.", "Journal : « Comment mon sens de la grandeur influence-t-il ma vision du monde ? »"]
    ),
    ('leo', 10): make_asc_interp(
        "Lion", 10,
        "Tu te présentes au monde comme une figure d'autorité — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un de charismatique, ambitieux et né pour diriger. Ta réputation est celle d'un leader créatif. Tu excelles dans les rôles visibles qui te permettent de briller et d'inspirer.",
        "Tu abordes ta carrière avec un besoin de laisser ta marque. Tu vises les positions de prestige et de reconnaissance. Tu as du mal avec les carrières où tu restes dans l'ombre.",
        ["Utilise ton charisme pour inspirer.", "Construis une réputation de générosité et de leadership.", "Journal : « Comment mon besoin de reconnaissance façonne-t-il ma vie professionnelle ? »"]
    ),
    ('leo', 11): make_asc_interp(
        "Lion", 11,
        "Tu te présentes au monde avec générosité — ton approche spontanée anime tes projets collectifs.",
        "Dans les groupes, tu prends naturellement le devant de la scène. Tu attires des amis qui admirent ton éclat ou qui sont eux-mêmes brillants. Tes idéaux pour l'avenir sont généreux et tu veux laisser un héritage.",
        "Tu abordes l'amitié et les projets de groupe avec ton cœur. Tu es un ami loyal qui veut le meilleur pour les siens. Tu peux avoir du mal à collaborer si tu ne reçois pas assez de reconnaissance.",
        ["Mets ton charisme au service des autres.", "Laisse tes amis briller aussi.", "Journal : « Comment ma générosité enrichit-elle mes amitiés et mes causes ? »"]
    ),
    ('leo', 12): make_asc_interp(
        "Lion", 12,
        "Tu te présentes au monde avec un éclat discret — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie royale opère dans l'ombre. Tu peux avoir une vie intérieure riche où tu te sens puissant et créatif, même si tu ne le montres pas toujours. Tu as des talents et des désirs de reconnaissance secrets.",
        "Tu abordes la spiritualité et l'inconscient avec ton cœur. Tu cherches à comprendre ta vraie valeur au-delà des apparences. Tu peux avoir un ego caché ou te saboter par peur de briller vraiment.",
        ["Explore ta lumière intérieure.", "Libère l'artiste caché en toi.", "Journal : « Quelle partie de mon éclat je garde secrète et pourquoi ? »"]
    ),

    # VIRGO ASCENDANT
    ('virgo', 1): make_asc_interp(
        "Vierge", 1,
        "Tu te présentes au monde avec précision — ton approche spontanée est celle de l'analyse.",
        "Ton masque est celui de l'analyste, de l'être méthodique et serviable. Les gens te perçoivent comme quelqu'un de réfléchi, organisé et fiable. Tu dégages une aura de compétence qui inspire confiance. Ta présence physique est souvent soignée, avec une attention aux détails.",
        "Tu abordes la vie par l'analyse et le service. Face à une situation, ton instinct est d'examiner, d'organiser, d'améliorer. Cette précision te rend efficace mais parfois trop critique. Tu préfères l'ordre au chaos.",
        ["Utilise ton sens du détail comme une force.", "Sois indulgent envers l'imperfection.", "Journal : « Comment mon besoin de perfection me guide-t-il dans la vie ? »"]
    ),
    ('virgo', 2): make_asc_interp(
        "Vierge", 2,
        "Tu te présentes au monde avec modestie — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie pratique influence ta façon de gagner et de gérer tes ressources. Tu es perçu comme quelqu'un de prudent avec l'argent. Tu préfères économiser et investir intelligemment plutôt que de gaspiller.",
        "Tu abordes les questions d'argent avec méthode et analyse. Tu examines chaque dépense, tu compares les prix, tu optimises. Tu peux avoir tendance à te priver par excès de prudence.",
        ["Gère tes ressources avec sagesse.", "Permets-toi quelques plaisirs sans culpabilité.", "Journal : « Comment mon sens pratique influence-t-il mes finances ? »"]
    ),
    ('virgo', 3): make_asc_interp(
        "Vierge", 3,
        "Tu te présentes au monde avec clarté — ton approche spontanée s'exprime dans ta communication précise.",
        "Ta façon de communiquer est claire, précise, détaillée. Les gens te perçoivent comme quelqu'un qui explique bien. Dans ton environnement proche, tu es celui qui organise et qui clarifie. Tes échanges avec frères et sœurs peuvent être critiques mais aussi très aidants.",
        "Tu apprends avec méthode et tu retiens les détails. Ton esprit est analytique, capable de décortiquer les informations complexes. Tu peux avoir tendance à critiquer la façon dont les autres s'expriment.",
        ["Communique avec clarté et bienveillance.", "Accepte l'approximation dans les échanges informels.", "Journal : « Comment mon sens du détail enrichit-il ou complique-t-il ma communication ? »"]
    ),
    ('virgo', 4): make_asc_interp(
        "Vierge", 4,
        "Tu te présentes au monde avec efficacité — ton approche spontanée crée un foyer ordonné.",
        "Ton besoin d'ordre se manifeste dans ta vie privée et familiale. Tu as besoin d'un chez-toi propre, organisé et fonctionnel. Tes racines sont marquées par une éducation qui valorisait le travail et le service — ou par un manque d'ordre qui t'a marqué.",
        "Tu abordes ta vie privée avec un besoin de tout organiser. Tu peux avoir du mal à te détendre si tout n'est pas en ordre. Ta famille te voit comme celui qui prend soin des détails pratiques.",
        ["Crée un foyer fonctionnel et apaisant.", "Accepte un peu de désordre créatif.", "Journal : « Comment mon besoin d'ordre influence-t-il ma vie familiale ? »"]
    ),
    ('virgo', 5): make_asc_interp(
        "Vierge", 5,
        "Tu te présentes au monde avec modestie — ton approche spontanée s'exprime dans la créativité soignée.",
        "Ton énergie analytique s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un qui fait les choses avec soin. En amour, tu es attentionné et serviable. Avec les enfants, tu es le parent qui enseigne la rigueur.",
        "Tu abordes les loisirs et la romance avec un certain perfectionnisme. Tu peux avoir du mal à te laisser aller complètement. Tes créations sont souvent techniques et détaillées.",
        ["Exprime ta créativité sans viser la perfection.", "Permets-toi de jouer sans but.", "Journal : « Comment mon perfectionnisme influence-t-il ma créativité et mes amours ? »"]
    ),
    ('virgo', 6): make_asc_interp(
        "Vierge", 6,
        "Tu te présentes au monde avec compétence — ton approche spontanée excelle dans le service.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement l'énergie de la Vierge : travail soigné, santé, service. Tu es perçu comme quelqu'un d'ultra-compétent dans son domaine. Tu excelles dans tout ce qui demande précision et méthode.",
        "Tu abordes les routines comme ton élément naturel. Tu optimises, tu améliores, tu perfectionnes. Ta santé est une préoccupation constante — tu fais attention à ton alimentation et à ton corps.",
        ["Excelle dans ton domaine avec fierté.", "Prends soin de toi sans devenir hypocondriaque.", "Journal : « Comment mon sens du service s'exprime-t-il dans mon quotidien ? »"]
    ),
    ('virgo', 7): make_asc_interp(
        "Vierge", 7,
        "Tu te présentes au monde avec discernement — ton approche spontanée analyse les relations.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes pratiques ou par celles qui ont besoin de ton aide. Tu es un partenaire attentionné qui remarque les petits détails. Tu peux avoir tendance à critiquer ton partenaire.",
        "Tu abordes les associations avec un regard analytique. Tu évalues les compatibilités, tu remarques les défauts. Tu as du mal avec les partenaires désorganisés ou irresponsables.",
        ["Sois serviable dans tes relations sans te perdre.", "Accepte l'imperfection de ton partenaire.", "Journal : « Comment mon sens critique influence-t-il mes partenariats ? »"]
    ),
    ('virgo', 8): make_asc_interp(
        "Vierge", 8,
        "Tu te présentes au monde avec retenue — ton approche spontanée s'applique aux transformations méthodiques.",
        "Tu abordes les crises et les transformations avec analyse et méthode. Tu essaies de comprendre ce qui se passe, de trouver des solutions pratiques. Les questions d'intimité sont abordées avec une certaine réserve.",
        "Face aux épreuves, ton instinct est d'analyser et de résoudre. Tu peux avoir du mal avec le chaos émotionnel des crises. Mais ta capacité à garder la tête froide te permet de traverser les tempêtes avec compétence.",
        ["Utilise ton analyse pour naviguer les transformations.", "Permets-toi de ressentir sans tout analyser.", "Journal : « Comment mon besoin de contrôle influence-t-il ma façon de gérer les crises ? »"]
    ),
    ('virgo', 9): make_asc_interp(
        "Vierge", 9,
        "Tu te présentes au monde avec discernement — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances est méthodique et pratique. Tu es attiré par les philosophies qui ont des applications concrètes. Tu explores le monde en cherchant à comprendre comment les choses fonctionnent.",
        "Tu abordes les études supérieures avec rigueur et les voyages avec préparation. Tu préfères apprendre ce qui est utile et applicable. Tes convictions sont basées sur l'expérience et l'analyse.",
        ["Explore de nouveaux horizons avec ton esprit analytique.", "Reste ouvert aux vérités qui dépassent la logique.", "Journal : « Comment mon sens pratique influence-t-il ma vision du monde ? »"]
    ),
    ('virgo', 10): make_asc_interp(
        "Vierge", 10,
        "Tu te présentes au monde comme un expert — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un de compétent, méthodique et fiable. Ta réputation est celle d'un professionnel minutieux. Tu excelles dans les rôles qui demandent précision, analyse ou service.",
        "Tu abordes ta carrière avec sérieux et méthode. Tu vises l'excellence plutôt que la gloire. Tu peux avoir du mal à te vendre ou à te mettre en avant, préférant que ton travail parle pour toi.",
        ["Utilise ta compétence pour construire ta réputation.", "Apprends à te valoriser autant que ton travail.", "Journal : « Comment mon perfectionnisme façonne-t-il ma vie professionnelle ? »"]
    ),
    ('virgo', 11): make_asc_interp(
        "Vierge", 11,
        "Tu te présentes au monde avec utilité — ton approche spontanée s'applique aux projets collectifs.",
        "Dans les groupes, tu apportes organisation et sens pratique. Tu attires des amis qui apprécient ta fiabilité. Tes idéaux pour l'avenir sont réalistes et tu travailles concrètement pour les atteindre.",
        "Tu abordes l'amitié et les projets de groupe avec ton sens du service. Tu es l'ami qui aide, qui organise, qui résout les problèmes. Tu peux avoir du mal avec les groupes désorganisés ou les idéalistes impractiques.",
        ["Apporte ton organisation aux projets collectifs.", "Accepte que tout ne soit pas parfait.", "Journal : « Comment mon sens pratique enrichit-il mes amitiés et mes causes ? »"]
    ),
    ('virgo', 12): make_asc_interp(
        "Vierge", 12,
        "Tu te présentes au monde avec une compétence discrète — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie analytique opère dans l'ombre. Tu peux avoir une vie intérieure très organisée que tu ne montres pas. Tu analyses secrètement tout, y compris toi-même. Tu peux avoir des inquiétudes cachées ou une autocritique sévère.",
        "Tu abordes la spiritualité et l'inconscient avec méthode. Tu cherches à comprendre et à améliorer ton monde intérieur. Tu peux te saboter par excès d'analyse ou de critique envers toi-même.",
        ["Explore ton monde intérieur avec compassion.", "Libère-toi de l'autocritique excessive.", "Journal : « Quelles imperfections je cache et pourquoi ? »"]
    ),

    # LIBRA ASCENDANT
    ('libra', 1): make_asc_interp(
        "Balance", 1,
        "Tu te présentes au monde avec grâce — ton approche spontanée est celle de l'harmonie.",
        "Ton masque est celui du diplomate, de l'être raffiné et équilibré. Les gens te perçoivent comme quelqu'un de charmant, aimable et élégant. Tu dégages une aura d'harmonie qui apaise les tensions. Ta présence physique est souvent attrayante, avec un sens du style.",
        "Tu abordes la vie par la relation et l'équilibre. Face à une situation, ton instinct est de peser le pour et le contre, de chercher le compromis. Cette diplomatie te rend agréable mais parfois indécis. Tu préfères la paix au conflit.",
        ["Cultive l'harmonie sans te perdre.", "Ose trancher quand c'est nécessaire.", "Journal : « Comment mon besoin d'équilibre me guide-t-il dans la vie ? »"]
    ),
    ('libra', 2): make_asc_interp(
        "Balance", 2,
        "Tu te présentes au monde avec élégance — ton approche spontanée colore ta relation aux ressources.",
        "Ton sens de l'harmonie influence ta façon de gagner et de dépenser. Tu es perçu comme quelqu'un qui a du goût. Tu dépenses pour la beauté, l'art et tout ce qui crée de l'harmonie dans ton environnement.",
        "Tu abordes les questions d'argent en cherchant l'équilibre. Tu peux avoir du mal à négocier durement ou à être avare. Tu partages facilement mais tu attends aussi que les autres soient justes avec toi.",
        ["Crée de la beauté avec tes ressources.", "Apprends à défendre tes intérêts financiers.", "Journal : « Comment mon sens de l'équilibre influence-t-il mes finances ? »"]
    ),
    ('libra', 3): make_asc_interp(
        "Balance", 3,
        "Tu te présentes au monde avec charme — ton approche spontanée s'exprime dans ta communication diplomatique.",
        "Ta façon de communiquer est agréable, nuancée et diplomatique. Les gens te perçoivent comme quelqu'un avec qui il est facile de parler. Dans ton environnement proche, tu es celui qui maintient l'harmonie. Tes échanges avec frères et sœurs sont généralement pacifiques.",
        "Tu communiques en cherchant l'accord. Tu pèses tes mots pour ne pas offenser. Tu peux avoir du mal à dire des vérités difficiles ou à prendre position clairement.",
        ["Communique avec grâce et authenticité.", "Ose dire ce que tu penses vraiment.", "Journal : « Comment mon besoin de plaire colore-t-il ma communication ? »"]
    ),
    ('libra', 4): make_asc_interp(
        "Balance", 4,
        "Tu te présentes au monde avec raffinement — ton approche spontanée crée un foyer harmonieux.",
        "Ton besoin d'harmonie se manifeste dans ta vie privée et familiale. Tu as besoin d'un chez-toi beau, équilibré et paisible. Tes racines sont marquées par une importance accordée aux relations et à l'esthétique — ou par un manque d'harmonie familiale qui t'a sensibilisé.",
        "Tu abordes ta vie privée en cherchant la paix et la beauté. Tu décores avec soin, tu évites les conflits familiaux. Tu peux avoir du mal à imposer tes besoins dans le contexte familial.",
        ["Crée un foyer qui nourrit ton sens de la beauté.", "Maintiens l'harmonie sans te sacrifier.", "Journal : « Comment mon besoin d'équilibre influence-t-il ma vie familiale ? »"]
    ),
    ('libra', 5): make_asc_interp(
        "Balance", 5,
        "Tu te présentes au monde avec élégance — ton approche spontanée s'exprime dans la créativité artistique.",
        "Ton sens de l'harmonie s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un de romantique et de cultivé. En amour, tu cherches l'harmonie parfaite. Avec les enfants, tu enseignes les bonnes manières et l'appréciation du beau.",
        "Tu abordes les loisirs et la romance avec ton sens de l'esthétique. Tu aimes les activités culturelles et artistiques. Tu peux idéaliser l'amour et avoir du mal avec ses aspects moins harmonieux.",
        ["Exprime ta créativité à travers l'art et la beauté.", "Accepte que l'amour ne soit pas toujours harmonieux.", "Journal : « Comment mon sens de l'harmonie enrichit-il ma créativité et mes amours ? »"]
    ),
    ('libra', 6): make_asc_interp(
        "Balance", 6,
        "Tu te présentes au monde avec coopération — ton approche spontanée s'applique au travail d'équipe.",
        "Ta façon d'aborder le travail quotidien et la santé est équilibrée. Tu es perçu comme un collègue agréable qui favorise l'harmonie au travail. Tu excelles dans les environnements collaboratifs et esthétiques.",
        "Tu abordes les routines en cherchant l'équilibre entre travail et plaisir. Ta santé dépend de l'harmonie dans ta vie — les conflits t'affectent physiquement. Tu as besoin de beauté dans ton environnement de travail.",
        ["Crée de l'harmonie dans ton travail quotidien.", "Équilibre effort et repos.", "Journal : « Comment mon besoin d'équilibre influence-t-il ma santé et mon travail ? »"]
    ),
    ('libra', 7): make_asc_interp(
        "Balance", 7,
        "Tu te présentes au monde avec charme — ton approche spontanée s'épanouit dans les relations.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement l'énergie de la Balance : partenariat, équilibre, diplomatie. Tu es né pour être en relation. Tu attires naturellement les partenaires et tu excelles dans l'art de la relation.",
        "Tu abordes les associations comme ton domaine naturel. Tu comprends intuitivement la dynamique relationnelle. Tu peux avoir du mal à être seul ou à faire des choix sans consulter les autres.",
        ["Épanouis-toi dans les partenariats équilibrés.", "Apprends à exister pleinement par toi-même.", "Journal : « Comment ma nature relationnelle façonne-t-elle ma vie ? »"]
    ),
    ('libra', 8): make_asc_interp(
        "Balance", 8,
        "Tu te présentes au monde avec diplomatie — ton approche spontanée s'applique aux transformations en douceur.",
        "Tu abordes les crises et les transformations en cherchant l'équilibre. Tu essaies de négocier même avec les forces de changement. Les questions d'intimité et de pouvoir sont abordées avec un désir de justice et d'équité.",
        "Face aux épreuves, ton instinct est de chercher le compromis ou la médiation. Tu peux avoir du mal avec les aspects brutaux des transformations. Mais ta capacité à voir les deux côtés te permet de traverser les crises avec grâce.",
        ["Utilise ta diplomatie pour naviguer les transformations.", "Accepte que certains changements ne soient pas négociables.", "Journal : « Comment mon besoin d'harmonie influence-t-il ma façon de gérer les crises ? »"]
    ),
    ('libra', 9): make_asc_interp(
        "Balance", 9,
        "Tu te présentes au monde avec ouverture — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances est équilibrée et ouverte. Tu es attiré par les philosophies qui prônent la justice, l'harmonie et la beauté. Tu explores le monde en cherchant à comprendre différentes perspectives.",
        "Tu abordes les études supérieures et les voyages avec curiosité pour les cultures et les idées différentes. Tu préfères les approches nuancées aux dogmes. Tes convictions sont flexibles et ouvertes au dialogue.",
        ["Explore de nouveaux horizons avec ton sens de l'équilibre.", "Ose avoir des convictions fermes.", "Journal : « Comment mon ouverture d'esprit influence-t-elle ma vision du monde ? »"]
    ),
    ('libra', 10): make_asc_interp(
        "Balance", 10,
        "Tu te présentes au monde comme un diplomate — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un de charmant, équilibré et juste. Ta réputation est celle d'un médiateur ou d'un esthète. Tu excelles dans les rôles qui demandent diplomatie, sens artistique ou justice.",
        "Tu abordes ta carrière en cherchant l'équilibre et la reconnaissance pour tes qualités relationnelles. Tu as du mal avec les environnements de travail conflictuels ou injustes.",
        ["Utilise tes talents diplomatiques dans ta carrière.", "Construis une réputation d'équité et d'élégance.", "Journal : « Comment mon sens de l'harmonie façonne-t-il ma vie professionnelle ? »"]
    ),
    ('libra', 11): make_asc_interp(
        "Balance", 11,
        "Tu te présentes au monde avec sociabilité — ton approche spontanée anime tes projets collectifs.",
        "Dans les groupes, tu apportes harmonie et connexion. Tu attires des amis de tous horizons et tu excelles à créer des liens. Tes idéaux pour l'avenir sont justes et inclusifs.",
        "Tu abordes l'amitié et les projets de groupe avec ton sens naturel de la relation. Tu es l'ami qui réconcilie, qui connecte, qui embellit les rassemblements. Tu peux avoir du mal avec les conflits dans les groupes.",
        ["Connecte les gens au service de l'harmonie collective.", "Ose prendre position même au risque de déplaire.", "Journal : « Comment mon charme social enrichit-il mes amitiés et mes causes ? »"]
    ),
    ('libra', 12): make_asc_interp(
        "Balance", 12,
        "Tu te présentes au monde avec une grâce discrète — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie harmonieuse opère dans l'ombre. Tu peux avoir une vie intérieure très riche en beauté et en relations imaginaires. Tu cherches l'équilibre dans ton monde intérieur. Tu peux avoir des amours secrets ou des idéaux de paix cachés.",
        "Tu abordes la spiritualité et l'inconscient en cherchant l'harmonie. Tu médites sur l'équilibre et la beauté. Tu peux te saboter en évitant les conflits intérieurs nécessaires.",
        ["Explore ton monde intérieur avec grâce.", "Fais face aux déséquilibres intérieurs avec courage.", "Journal : « Quelle harmonie je cherche secrètement ? »"]
    ),

    # SCORPIO ASCENDANT
    ('scorpio', 1): make_asc_interp(
        "Scorpion", 1,
        "Tu te présentes au monde avec intensité — ton approche spontanée est celle de la profondeur.",
        "Ton masque est celui du mystérieux, de l'être intense et magnétique. Les gens te perçoivent comme quelqu'un de puissant, perçant et parfois intimidant. Tu dégages une aura de profondeur qui attire ou repousse. Ta présence physique est souvent magnétique, avec un regard pénétrant.",
        "Tu abordes la vie en cherchant la vérité cachée. Face à une situation, ton instinct est de creuser, de transformer, d'aller au fond des choses. Cette intensité te rend perspicace mais parfois obsessionnel. Tu préfères la profondeur à la superficialité.",
        ["Utilise ton intensité comme une force de transformation.", "Laisse parfois les choses être légères.", "Journal : « Comment ma profondeur me guide-t-elle dans la vie ? »"]
    ),
    ('scorpio', 2): make_asc_interp(
        "Scorpion", 2,
        "Tu te présentes au monde avec puissance — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie intense influence ta façon de gagner et de contrôler tes ressources. Tu es perçu comme quelqu'un qui sait ce qu'il veut et comment l'obtenir. Tu peux être très stratégique avec l'argent, préférant le contrôle à la dépendance.",
        "Tu abordes les questions d'argent avec intensité et détermination. Tu veux la sécurité financière absolue. Tu peux être secret sur tes finances ou utiliser l'argent comme un outil de pouvoir.",
        ["Transforme ta relation à l'argent en source de pouvoir sain.", "Évite les obsessions financières.", "Journal : « Comment mon besoin de contrôle influence-t-il mes finances ? »"]
    ),
    ('scorpio', 3): make_asc_interp(
        "Scorpion", 3,
        "Tu te présentes au monde avec acuité — ton approche spontanée s'exprime dans ta communication perçante.",
        "Ta façon de communiquer est profonde, incisive et parfois provocatrice. Les gens te perçoivent comme quelqu'un qui voit au-delà des mots. Dans ton environnement proche, tu es celui qui détecte les non-dits. Tes échanges avec frères et sœurs peuvent être intenses ou conflictuels.",
        "Tu communiques pour aller à l'essentiel. Tu poses les questions que les autres évitent. Tu peux avoir une tendance à sonder les gens ou à utiliser l'information comme pouvoir.",
        ["Communique avec ta perspicacité au service de la vérité.", "Respecte les secrets des autres.", "Journal : « Comment mon intensité colore-t-elle ma communication ? »"]
    ),
    ('scorpio', 4): make_asc_interp(
        "Scorpion", 4,
        "Tu te présentes au monde avec magnétisme — ton approche spontanée crée un foyer intense.",
        "Ton énergie transformatrice se manifeste dans ta vie privée et familiale. Tu as besoin d'un chez-toi qui soit un sanctuaire, un lieu de régénération. Tes racines sont marquées par des secrets familiaux, des transformations ou une intensité émotionnelle.",
        "Tu abordes ta vie privée avec profondeur. Ta maison est ton antre, où tu te régénères. Tu peux avoir des secrets familiaux ou une vie privée très protégée.",
        ["Crée un foyer qui permet la transformation.", "Libère les secrets familiaux qui pèsent.", "Journal : « Comment l'intensité de mes racines façonne-t-elle ma vie privée ? »"]
    ),
    ('scorpio', 5): make_asc_interp(
        "Scorpion", 5,
        "Tu te présentes au monde avec passion — ton approche spontanée s'exprime dans la créativité transformatrice.",
        "Ton énergie intense s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un de magnétique et entier. En amour, tu vis des passions profondes et parfois dévorantes. Avec les enfants, tu enseignes l'authenticité et la profondeur.",
        "Tu abordes les loisirs et la romance avec tout ton être. Tu ne fais pas les choses à moitié. Tes créations sont souvent intenses, profondes, transformatrices.",
        ["Exprime ta créativité à travers la transformation.", "Laisse parfois tes passions être légères.", "Journal : « Comment mon intensité enrichit-elle ma créativité et mes amours ? »"]
    ),
    ('scorpio', 6): make_asc_interp(
        "Scorpion", 6,
        "Tu te présentes au monde avec détermination — ton approche spontanée s'applique au travail en profondeur.",
        "Ta façon d'aborder le travail quotidien et la santé est intense et transformatrice. Tu es perçu comme quelqu'un qui travaille avec acharnement et qui va au fond des choses. Tu excelles dans les rôles qui demandent investigation ou transformation.",
        "Tu abordes les routines avec intensité. Tu veux comprendre le pourquoi des choses. Ta santé peut être affectée par les émotions refoulées — les toxines émotionnelles ont besoin d'être libérées.",
        ["Transforme ton quotidien par ton intensité.", "Libère les tensions accumulées régulièrement.", "Journal : « Comment mon intensité influence-t-elle ma santé et mon travail ? »"]
    ),
    ('scorpio', 7): make_asc_interp(
        "Scorpion", 7,
        "Tu te présentes au monde avec magnétisme — ton approche spontanée s'exprime dans des relations intenses.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes intenses, puissantes ou transformatrices. Tu es un partenaire passionné qui s'engage totalement. Tu peux avoir des relations qui transforment profondément les deux partenaires.",
        "Tu abordes les associations avec intensité et profondeur. Tu veux connaître l'autre jusqu'au fond de son âme. Tu as du mal avec les relations superficielles et tu peux être jaloux ou possessif.",
        ["Crée des partenariats transformateurs.", "Donne de l'espace à ton partenaire.", "Journal : « Comment mon intensité influence-t-elle mes partenariats ? »"]
    ),
    ('scorpio', 8): make_asc_interp(
        "Scorpion", 8,
        "Tu te présentes au monde avec puissance — ton approche spontanée excelle dans les transformations.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement l'énergie scorpionne : transformation, profondeur, pouvoir. Tu es né pour naviguer les eaux profondes de la vie — crises, intimité, mort et renaissance.",
        "Tu abordes les transformations comme ton élément naturel. Tu n'as pas peur de ce qui effraie les autres. Tu comprends intuitivement les cycles de mort et de renaissance.",
        ["Embrasse ton pouvoir de transformation.", "Guide les autres à travers leurs crises.", "Journal : « Comment ma nature transformatrice s'exprime-t-elle pleinement ? »"]
    ),
    ('scorpio', 9): make_asc_interp(
        "Scorpion", 9,
        "Tu te présentes au monde avec profondeur — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances est intense et transformatrice. Tu es attiré par les philosophies qui explorent les mystères de l'existence. Tu explores le monde en cherchant les vérités cachées.",
        "Tu abordes les études supérieures et les voyages avec un désir de transformation. Tu préfères les enseignements ésotériques aux doctrines superficielles. Tes convictions sont profondes et tu peux être dogmatique.",
        ["Explore de nouveaux horizons de conscience.", "Reste ouvert aux vérités qui défient tes convictions.", "Journal : « Comment ma quête de profondeur influence-t-elle ma vision du monde ? »"]
    ),
    ('scorpio', 10): make_asc_interp(
        "Scorpion", 10,
        "Tu te présentes au monde comme une force de transformation — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un de puissant, stratégique et transformateur. Ta réputation est celle de quelqu'un qui peut gérer les situations difficiles. Tu excelles dans les rôles qui impliquent pouvoir, investigation ou transformation.",
        "Tu abordes ta carrière avec intensité et ambition. Tu vises le pouvoir et l'influence. Tu as du mal avec les environnements de travail superficiels ou où le pouvoir est mal utilisé.",
        ["Utilise ton pouvoir pour transformer positivement.", "Construis une réputation d'intégrité et de profondeur.", "Journal : « Comment mon intensité façonne-t-elle ma vie professionnelle ? »"]
    ),
    ('scorpio', 11): make_asc_interp(
        "Scorpion", 11,
        "Tu te présentes au monde avec intensité — ton approche spontanée transforme les projets collectifs.",
        "Dans les groupes, tu apportes profondeur et transformation. Tu attires des amis intenses ou tu transformes ceux que tu côtoies. Tes idéaux pour l'avenir sont radicaux et tu veux des changements profonds dans la société.",
        "Tu abordes l'amitié et les projets de groupe avec intensité. Tu es l'ami qui transforme, qui pousse à aller plus loin. Tu peux avoir du mal avec les groupes superficiels ou les amitiés légères.",
        ["Transforme les collectifs par ta profondeur.", "Respecte les limites des autres.", "Journal : « Comment mon intensité enrichit-elle mes amitiés et mes causes ? »"]
    ),
    ('scorpio', 12): make_asc_interp(
        "Scorpion", 12,
        "Tu te présentes au monde avec un mystère profond — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie transformatrice opère dans l'ombre. Tu as une vie intérieure très intense que tu ne montres pas. Tu explores les profondeurs de ton inconscient. Tu peux avoir des pouvoirs psychiques ou une intuition très développée.",
        "Tu abordes la spiritualité et l'inconscient comme un territoire familier. Tu n'as pas peur de tes ombres. Tu peux te transformer profondément à travers le travail intérieur.",
        ["Explore tes profondeurs avec courage.", "Transforme tes ombres en lumière.", "Journal : « Quels pouvoirs cachés je porte en moi ? »"]
    ),
}


async def insert_interpretations():
    """Insert Ascendant interpretations into database."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in ASCENDANT_INTERPRETATIONS.items():
            # Check if already exists
            query = select(PregeneratedNatalInterpretation).where(
                PregeneratedNatalInterpretation.subject == "ascendant",
                PregeneratedNatalInterpretation.sign == sign,
                PregeneratedNatalInterpretation.house == house,
                PregeneratedNatalInterpretation.version == 2,
                PregeneratedNatalInterpretation.lang == "fr"
            )
            result = await db.execute(query)
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️ SKIP ascendant/{sign}/M{house} (already exists)")
                skipped += 1
                continue

            # Insert new interpretation
            interpretation = PregeneratedNatalInterpretation(
                id=uuid4(),
                subject="ascendant",
                sign=sign,
                house=house,
                version=2,
                lang="fr",
                content=content,
                length=len(content)
            )
            db.add(interpretation)
            print(f"✅ INSERT ascendant/{sign}/M{house} ({len(content)} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == "__main__":
    asyncio.run(insert_interpretations())
