"""Batch complet: Libra - 144 interprétations (12 maisons × 12 ascendants)"""
import asyncio
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.insert_lunar_v2_manual import insert_batch

BATCH = [
    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Double harmonie**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 1, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 1 active identité et image. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans présentation personnelle, apparence, authenticité. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 1 — Identité et image devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de présentation personnelle, apparence, authenticité.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans identité et image.",
            'week_2': "Prends une initiative pour harmoniser présentation personnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans identité et image.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 2, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 2 active ressources et valeurs. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans finances, possessions, estime de soi matérielle. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 2 — Ressources et valeurs devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de finances, possessions, estime de soi matérielle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans ressources et valeurs.",
            'week_2': "Prends une initiative pour harmoniser finances.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans ressources et valeurs.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 3, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 3 active communication et apprentissage. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans échanges, voisinage, déplacements quotidiens. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 3 — Communication et apprentissage devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de échanges, voisinage, déplacements quotidiens.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communication et apprentissage.",
            'week_2': "Prends une initiative pour harmoniser échanges.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communication et apprentissage.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 4, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 4 active foyer et racines. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans maison, famille, intimité émotionnelle. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 4 — Foyer et racines devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de maison, famille, intimité émotionnelle.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans foyer et racines.",
            'week_2': "Prends une initiative pour harmoniser maison.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans foyer et racines.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 5, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 5 active créativité et plaisir. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans expression artistique, romance, jeu, enfants. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 5 — Créativité et plaisir devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de expression artistique, romance, jeu, enfants.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans créativité et plaisir.",
            'week_2': "Prends une initiative pour harmoniser expression artistique.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans créativité et plaisir.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 6, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 6 active travail et santé. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans quotidien, service, bien-être physique. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 6 — Travail et santé devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de quotidien, service, bien-être physique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans travail et santé.",
            'week_2': "Prends une initiative pour harmoniser quotidien.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans travail et santé.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Double harmonie**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 7, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 7 active partenariats et relations. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans couple, associations, contrats. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 7 — Partenariats et relations devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de couple, associations, contrats.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans partenariats et relations.",
            'week_2': "Prends une initiative pour harmoniser couple.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans partenariats et relations.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 8, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 8 active transformation et intimité. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ressources partagées, sexualité, profondeur. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 8 — Transformation et intimité devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de ressources partagées, sexualité, profondeur.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans transformation et intimité.",
            'week_2': "Prends une initiative pour harmoniser ressources partagées.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans transformation et intimité.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 9, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 9 active expansion et sagesse. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans voyages, philosophie, enseignement. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 9 — Expansion et sagesse devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de voyages, philosophie, enseignement.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans expansion et sagesse.",
            'week_2': "Prends une initiative pour harmoniser voyages.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans expansion et sagesse.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 10, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 10 active carrière et réputation. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans ambition professionnelle, image publique. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 10 — Carrière et réputation devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de ambition professionnelle, image publique.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans carrière et réputation.",
            'week_2': "Prends une initiative pour harmoniser ambition professionnelle.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans carrière et réputation.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 11, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 11 active communauté et idéaux. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans amitiés, réseaux, projets collectifs. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 11 — Communauté et idéaux devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de amitiés, réseaux, projets collectifs.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans communauté et idéaux.",
            'week_2': "Prends une initiative pour harmoniser amitiés.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans communauté et idéaux.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Aries',
        'interpretation': """**Ton mois en un mot : Équilibre actif**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Aries ajoute action, impulsivité, franchise, courage, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aries colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et action dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Taurus',
        'interpretation': """**Ton mois en un mot : Grâce solide**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Taurus ajoute stabilité, patience, sensorialité, pragmatisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Taurus colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et stabilité dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Taurus peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Gemini',
        'interpretation': """**Ton mois en un mot : Harmonie vive**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Gemini ajoute communication, curiosité, adaptabilité, légèreté, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Gemini colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et communication dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Gemini peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Cancer',
        'interpretation': """**Ton mois en un mot : Grâce tendre**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Cancer ajoute sensibilité, protection, empathie, sécurité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Cancer colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et sensibilité dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Cancer peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Leo',
        'interpretation': """**Ton mois en un mot : Équilibre leo**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Leo ajoute rayonnement, générosité, confiance, créativité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Leo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et rayonnement dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Virgo',
        'interpretation': """**Ton mois en un mot : Équilibre virgo**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Virgo ajoute précision, analyse, service, perfectionnisme, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Virgo colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et précision dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Virgo peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Libra',
        'interpretation': """**Ton mois en un mot : Triple harmonie**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Libra ajoute harmonie, diplomatie, esthétique, équilibre, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Libra colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche équilibrée et naturelle dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Libra peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Scorpio',
        'interpretation': """**Ton mois en un mot : Équilibre intense**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Scorpio ajoute intensité, transformation, profondeur, contrôle, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Scorpio colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intensité dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'intensité de ton Ascendant peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Sagittarius',
        'interpretation': """**Ton mois en un mot : Harmonie libre**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Sagittarius ajoute expansion, optimisme, liberté, philosophie, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Sagittarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et expansion dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Sagittarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Capricorn',
        'interpretation': """**Ton mois en un mot : Équilibre capricor**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Capricorn ajoute structure, ambition, discipline, responsabilité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Capricorn colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et structure dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Capricorn peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Aquarius',
        'interpretation': """**Ton mois en un mot : Harmonie originale**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Aquarius ajoute originalité, innovation, indépendance, collectif, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Aquarius colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et originalité dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Aquarius peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    },

    {
        'moon_sign': 'Libra', 'moon_house': 12, 'lunar_ascendant': 'Pisces',
        'interpretation': """**Ton mois en un mot : Grâce fluide**

Ta Lune en Balance en Maison 12 active spiritualité et transcendance. L'énergie harmonieuse et diplomatique de la Balance cherche l'équilibre dans retraite, guérison, inconscient. Ton Ascendant Pisces ajoute intuition, compassion, fluidité, spiritualité, créant une dynamique unique entre recherche d'harmonie et expression de cette énergie ascendante.

**Domaine activé** : Maison 12 — Spiritualité et transcendance devient central·e ce mois. Tu ressens un besoin profond de créer de l'équilibre, de la beauté, de la justice dans ce domaine. Tes décisions sont guidées par ton sens esthétique et relationnel.

**Ton approche instinctive** : L'Ascendant Pisces colore ta façon d'aborder cette quête d'harmonie. Cette combinaison te donne une approche unique qui allie diplomatie et intuition dans la gestion de retraite, guérison, inconscient.

**Tensions possibles** : Le conflit entre ton besoin d'harmonie (Balance) et l'énergie de ton Ascendant Pisces peut créer des moments d'indécision ou de déséquilibre temporaire. Tu cherches le juste milieu.

**Conseil clé** : Accepter que l'harmonie authentique passe parfois par des déséquilibres temporaires nécessaires à la croissance.""",
        'weekly_advice': {
            'week_1': "Identifie ce qui manque d'équilibre dans spiritualité et transcendance.",
            'week_2': "Prends une initiative pour harmoniser retraite.",
            'week_3': "Ajuste ton approche en écoutant les besoins de tous les acteurs concernés.",
            'week_4': "Célèbre l'harmonie que tu as créée dans spiritualité et transcendance.",
        }
    }
]

if __name__ == "__main__":
    print(f"Préparation de l'insertion de {len(BATCH)} interprétations Libra...")
    asyncio.run(insert_batch(BATCH))
    print("✅ Batch Libra complet inséré avec succès !")
