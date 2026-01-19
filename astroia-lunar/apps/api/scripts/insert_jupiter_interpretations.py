#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

# Signes et leurs noms français
SIGNS = {
    'aries': 'Bélier',
    'taurus': 'Taureau',
    'gemini': 'Gémeaux',
    'cancer': 'Cancer',
    'leo': 'Lion',
    'virgo': 'Vierge',
    'libra': 'Balance',
    'scorpio': 'Scorpion',
    'sagittarius': 'Sagittaire',
    'capricorn': 'Capricorne',
    'aquarius': 'Verseau',
    'pisces': 'Poissons'
}

# Interprétations Jupiter par signe et maison
JUPITER_INTERPRETATIONS = {
    # ARIES (Bélier) - 12 maisons
    ('aries', 1): """# ♃ Jupiter en Bélier
**En une phrase :** Tu incarnes une énergie d'expansion audacieuse qui pousse les autres à oser davantage dès qu'ils te croisent.

## Ton moteur
Jupiter en Bélier en Maison 1 te donne une présence magnétique de pionnier. Tu attaques la vie avec optimisme et une foi inébranlable dans tes capacités. Cette configuration amplifie ton besoin d'action immédiate : tu préfères te lancer quitte à ajuster ensuite plutôt que de planifier indéfiniment.

## Ton défi
Le piège : confondre impulsivité et courage, brûler les étapes par impatience, imposer ton enthousiasme sans vérifier que les autres suivent. L'expansion durable demande parfois de tempérer le feu.

## Maison 1 en Bélier
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un qui n'a peur de rien. Ton corps exprime l'action, ta gestuelle est directe. Tu attires ceux qui cherchent un électrochoc ou un coup de pouce pour démarrer.

## Micro-rituel du jour (2 min)
- Identifier une action concrète que tu repousses et la faire dans les 5 prochaines minutes
- Trois respirations dynamiques : inspirer en levant les bras, expirer en les baissant avec force
- Journal : « Quel nouveau défi ai-je envie de relever cette semaine ? »""",

    ('aries', 2): """# ♃ Jupiter en Bélier
**En une phrase :** Tu développes tes ressources en fonçant : pour toi, l'abondance vient à ceux qui osent prendre des risques calculés.

## Ton moteur
Jupiter en Bélier en Maison 2 pousse à conquérir l'autonomie financière par l'action directe. Tu n'attends pas que l'argent vienne : tu vas le chercher. Entreprendre, investir dans tes idées, monétiser tes talents — ton rapport à l'argent est actif, jamais passif.

## Ton défi
Le piège : dépenser aussi vite que tu gagnes, t'endetter pour des projets impulsifs, confondre valeur personnelle et compte en banque. L'abondance durable demande aussi de la patience.

## Maison 2 en Bélier
Jupiter amplifie ton désir d'indépendance matérielle. Tu as besoin de sentir que tes ressources sont le fruit de tes propres initiatives. Les revenus passifs t'ennuient — tu préfères les défis qui récompensent l'audace.

## Micro-rituel du jour (2 min)
- Identifier une compétence que tu pourrais mieux valoriser et noter une action pour la développer
- Trois respirations en visualisant l'énergie circuler librement vers tes projets
- Journal : « Quelle initiative récente a renforcé mon sentiment de valeur personnelle ? »""",

    ('aries', 3): """# ♃ Jupiter en Bélier
**En une phrase :** Ta communication est un sport de combat : tu transmets tes idées avec une énergie qui bouscule et stimule ceux qui t'écoutent.

## Ton moteur
Jupiter en Bélier en Maison 3 amplifie ta façon de penser et de parler. Tes mots sont directs, percutants, parfois provocateurs. Tu apprends vite, mais tu préfères l'expérimentation à la théorie. Les débats te stimulent : tu as besoin de confronter tes idées pour les affiner.

## Ton défi
Le piège : couper la parole, asséner tes vérités sans laisser de place au doute, confondre affirmation et agressivité verbale. La communication devient plus puissante quand elle sait aussi écouter.

## Maison 3 en Bélier
Jupiter amplifie ton besoin de mouvement intellectuel. Tu multiplies les échanges, les formations courtes, les discussions stimulantes. Ton entourage proche te perçoit comme un catalyseur d'idées nouvelles.

## Micro-rituel du jour (2 min)
- Envoyer un message à quelqu'un pour partager une idée qui t'enthousiasme
- Trois respirations en te concentrant sur l'écoute : inspirer pour recevoir, expirer pour lâcher
- Journal : « Quelle idée nouvelle ai-je découverte récemment et comment l'ai-je partagée ? »""",

    ('aries', 4): """# ♃ Jupiter en Bélier
**En une phrase :** Ton foyer est une base de lancement : tu as besoin d'un chez-toi qui te donne l'énergie de conquérir le monde extérieur.

## Ton moteur
Jupiter en Bélier en Maison 4 transforme ton rapport aux racines. Tu ne cherches pas un cocon protecteur mais un quartier général. Ton foyer doit être dynamique, peut-être un peu en chantier permanent, toujours prêt pour le prochain projet.

## Ton défi
Le piège : fuir l'intimité familiale pour l'action, imposer ton rythme à ceux qui vivent avec toi, confondre foyer et terrain de compétition. Le chez-soi demande aussi des moments de douceur.

## Maison 4 en Bélier
Jupiter amplifie ton besoin d'autonomie dans ta vie privée. Tu as peut-être quitté le nid familial tôt, ou tu as transformé les traditions héritées pour créer les tiennes. Ta famille t'a transmis le goût de l'indépendance.

## Micro-rituel du jour (2 min)
- Ranger ou réorganiser un coin de ton espace pour le rendre plus fonctionnel
- Trois respirations en visualisant ton foyer comme un tremplin plein d'énergie
- Journal : « Comment mon chez-moi soutient-il mes ambitions actuelles ? »""",

    ('aries', 5): """# ♃ Jupiter en Bélier
**En une phrase :** Tu vis la créativité comme une aventure : tes passions sont intenses, tes amours audacieuses, tes créations spontanées.

## Ton moteur
Jupiter en Bélier en Maison 5 amplifie ta flamme créative et ton goût pour le jeu. Tu as besoin de te sentir vivant à travers l'expression de toi-même — art, sport, romance, tout ce qui fait battre le cœur plus fort. Tu préfères créer dans l'instant plutôt que de peaufiner indéfiniment.

## Ton défi
Le piège : multiplier les conquêtes sans approfondir, t'ennuyer dès que la nouveauté s'estompe, confondre intensité et durabilité. La création mature demande parfois de la persévérance.

## Maison 5 en Bélier
Jupiter amplifie ton magnétisme dans les domaines du plaisir. Tu attires des partenaires qui aiment l'aventure. Avec les enfants ou dans tes projets créatifs, tu transmets l'audace et le goût du défi.

## Micro-rituel du jour (2 min)
- T'accorder 10 minutes de création libre sans enjeu : dessiner, écrire, jouer
- Trois respirations en visualisant une flamme intérieure qui s'intensifie
- Journal : « Quelle activité me fait me sentir le plus vivant en ce moment ? »""",

    ('aries', 6): """# ♃ Jupiter en Bélier
**En une phrase :** Tu optimises ton quotidien comme un athlète : chaque routine est une occasion de te dépasser et d'améliorer tes performances.

## Ton moteur
Jupiter en Bélier en Maison 6 transforme ton rapport au travail quotidien. Tu as besoin de défis concrets, de missions à accomplir, de problèmes à résoudre rapidement. La routine t'ennuie : tu cherches constamment à améliorer tes méthodes, tes outils, ton efficacité.

## Ton défi
Le piège : t'épuiser dans une hyperactivité non soutenable, négliger les signaux de fatigue de ton corps, imposer ton rythme effréné à tes collègues. La performance durable demande aussi du repos.

## Maison 6 en Bélier
Jupiter amplifie ton énergie dans le service aux autres. Tu préfères l'action concrète aux discours : aider quelqu'un, c'est faire quelque chose de tangible. Ta santé bénéficie d'une activité physique régulière et intense.

## Micro-rituel du jour (2 min)
- Identifier une tâche répétitive et trouver une façon de l'optimiser ou l'accélérer
- Trois respirations dynamiques pour relancer ton énergie en milieu de journée
- Journal : « Quelle amélioration concrète ai-je apportée à mon quotidien récemment ? »""",

    ('aries', 7): """# ♃ Jupiter en Bélier
**En une phrase :** Tes relations sont des aventures partagées : tu cherches des partenaires qui ont autant de feu que toi et qui te poussent à te dépasser.

## Ton moteur
Jupiter en Bélier en Maison 7 te pousse vers des partenariats dynamiques et stimulants. Tu attires des personnes entreprenantes, parfois compétitrices. En amour comme en affaires, tu as besoin de sentir que l'autre te challenge et partage ton goût pour l'action.

## Ton défi
Le piège : transformer les relations en rapport de force, chercher à dominer ou te mesurer constamment, fuir dès que la relation devient trop paisible. Le partenariat demande aussi de savoir faire équipe.

## Maison 7 en Bélier
Jupiter amplifie ton besoin d'indépendance dans le couple. Tu refuses les relations qui t'étouffent. Tu as besoin d'un partenaire qui a sa propre vie, ses propres projets, et qui respecte ton espace.

## Micro-rituel du jour (2 min)
- Proposer une activité nouvelle à un partenaire (pro ou perso) pour sortir de la routine
- Trois respirations en ouvrant les bras : accueillir l'autre sans perdre ton centre
- Journal : « Comment mes relations actuelles stimulent-elles ma croissance personnelle ? »""",

    ('aries', 8): """# ♃ Jupiter en Bélier
**En une phrase :** Tu explores les profondeurs avec audace : les crises deviennent des opportunités de renaissance, les tabous des territoires à conquérir.

## Ton moteur
Jupiter en Bélier en Maison 8 te donne une capacité rare à traverser les épreuves en ressortant plus fort. Tu n'as pas peur d'affronter ce que les autres évitent : la mort, le sexe, l'argent des autres, les zones d'ombre. Cette configuration amplifie ta résilience et ton goût pour la transformation.

## Ton défi
Le piège : chercher l'intensité à tout prix, provoquer des crises pour te sentir vivant, confondre courage et inconscience face aux dangers réels. La profondeur demande aussi du discernement.

## Maison 8 en Bélier
Jupiter amplifie ta capacité à rebondir après les pertes. Tu sais instinctivement que chaque fin est un début. Les ressources partagées (héritages, investissements communs) peuvent arriver soudainement ou suite à une prise de risque.

## Micro-rituel du jour (2 min)
- Identifier une peur que tu évites et faire un petit pas vers elle aujourd'hui
- Trois respirations profondes en visualisant une transformation en cours
- Journal : « Quelle situation difficile m'a récemment rendu plus fort ? »""",

    ('aries', 9): """# ♃ Jupiter en Bélier
**En une phrase :** Ta quête de sens est une aventure : tu explores les philosophies, les cultures et les horizons avec l'enthousiasme d'un pionnier.

## Ton moteur
Jupiter en Bélier en Maison 9 amplifie ta soif d'exploration. Voyager, étudier, enseigner — tout ce qui élargit ton horizon te fait vibrer. Tu as ta propre philosophie de vie, forgée par l'expérience directe plutôt que par les livres. Tu transmets tes convictions avec passion.

## Ton défi
Le piège : imposer tes croyances, confondre conviction et certitude, partir toujours plus loin sans intégrer ce que tu as appris. La sagesse demande aussi de la réflexion.

## Maison 9 en Bélier
Jupiter amplifie ton besoin d'horizons nouveaux. Tu apprends en faisant, en partant, en te confrontant à l'inconnu. Les études longues t'attirent si elles mènent à l'action. Tu pourrais enseigner, publier ou guider d'autres dans leurs explorations.

## Micro-rituel du jour (2 min)
- Planifier un voyage (même court) ou découvrir un contenu d'une culture différente
- Trois respirations en visualisant l'horizon s'élargir devant toi
- Journal : « Quelle croyance ou conviction ai-je remise en question récemment ? »""",

    ('aries', 10): """# ♃ Jupiter en Bélier
**En une phrase :** Ta carrière est une conquête : tu vises les sommets avec une ambition décomplexée et une confiance qui inspire le respect.

## Ton moteur
Jupiter en Bélier en Maison 10 te pousse vers des positions de leadership. Tu as besoin d'une carrière qui te permette d'agir, de décider, d'avoir un impact visible. Les structures trop rigides t'étouffent : tu préfères créer ton propre chemin vers la réussite.

## Ton défi
Le piège : brûler les étapes pour arriver au sommet, écraser les autres dans ta course, confondre réussite et reconnaissance. Le succès durable se construit aussi sur des alliances solides.

## Maison 10 en Bélier
Jupiter amplifie ta visibilité professionnelle. On te remarque, on te confie des responsabilités, on attend de toi que tu montres la voie. Ta réputation se construit sur ton audace et ta capacité à prendre des initiatives.

## Micro-rituel du jour (2 min)
- Identifier une action professionnelle audacieuse que tu pourrais entreprendre cette semaine
- Trois respirations en te tenant droit, visualisant ta place au sommet
- Journal : « Quel impact concret ai-je envie d'avoir dans ma carrière ? »""",

    ('aries', 11): """# ♃ Jupiter en Bélier
**En une phrase :** Tu fédères des troupes autour de projets audacieux : tes amitiés sont des alliances de combat pour changer le monde.

## Ton moteur
Jupiter en Bélier en Maison 11 te donne un talent pour rassembler des personnes autour de causes qui te passionnent. Tu n'aimes pas les groupes passifs : tu veux des collectifs qui agissent, des amis qui entreprennent, des réseaux qui font bouger les choses.

## Ton défi
Le piège : vouloir mener tous les groupes, frustrer ceux qui préfèrent un rythme plus lent, abandonner les projets collectifs dès qu'ils deviennent trop politiques. L'action collective demande aussi du compromis.

## Maison 11 en Bélier
Jupiter amplifie ton influence dans les réseaux. Tu attires des amis entreprenants, parfois compétiteurs mais toujours stimulants. Tes projets humanitaires ou associatifs ont une dimension d'innovation et d'action directe.

## Micro-rituel du jour (2 min)
- Rejoindre ou contacter un groupe qui partage tes valeurs pour proposer une action concrète
- Trois respirations en visualisant l'énergie du groupe qui amplifie la tienne
- Journal : « Quel projet collectif m'enthousiasme le plus en ce moment ? »""",

    ('aries', 12): """# ♃ Jupiter en Bélier
**En une phrase :** Tu explores l'invisible avec audace : ton monde intérieur est un territoire à conquérir, tes intuitions des guides vers l'action.

## Ton moteur
Jupiter en Bélier en Maison 12 crée une tension productive entre ton besoin d'agir et le monde subtil de l'inconscient. Tu as une foi instinctive qui te protège dans les moments difficiles. Tes intuitions sont souvent justes, surtout quand elles te poussent à l'action.

## Ton défi
Le piège : agir impulsivement sur des intuitions non vérifiées, fuir l'introspection par l'hyperactivité, ignorer les signaux d'épuisement spirituel. L'invisible demande aussi du temps et du silence.

## Maison 12 en Bélier
Jupiter amplifie ta connexion au mystère. Tu peux avoir des expériences spirituelles intenses et soudaines. Les retraites actives (méditation en marchant, arts martiaux méditatifs) te conviennent mieux que la contemplation immobile.

## Micro-rituel du jour (2 min)
- Prendre 5 minutes pour écouter ton intuition sur une décision en suspens
- Trois respirations profondes en laissant émerger ce qui est caché
- Journal : « Quel message de mon inconscient ai-je reçu récemment ? »""",
}

async def insert_interpretations():
    """Insère les interprétations Jupiter en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_INTERPRETATIONS.items():
            # Vérifier si l'interprétation existe déjà
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'jupiter',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP jupiter/{sign}/M{house} (existe déjà)")
                skipped += 1
                continue

            # Créer la nouvelle interprétation
            interp = PregeneratedNatalInterpretation(
                subject='jupiter',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT jupiter/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
